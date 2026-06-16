#!/usr/bin/env python3
"""
analyze.py — Path A FP16 Constructibility analysis (per-item-validated R1 + Wilson 95% CI).

Per locked preregistration §12 + §14 (v0.3 of-record):
  - Global R1 is computed over per-item-validated items.
  - Validation gates numerator inclusion BEFORE aggregation:
      (a) R7 controls pass: hop1 == B AND hop2 == C* AND direct-query did NOT produce C*
      (b) no R6 invalidator fires (terminal coincidence; components-unavailable;
          direct-query shortcut; interior-position; cross-query constant-token)
  - Test statistic: per-item-validated R1 proportion over n=96
  - CI: two-sided 95% Wilson score interval (NOT Clopper-Pearson per TL correction)
  - Decision rule (MECE):
      CERTIFY    lower CI > 0.45 AND no dominant failure signature
      FAIL       upper CI < 0.20 OR any dominant failure signature
      INCONCLUSIVE otherwise
  - Failure signatures (§15):
      rate-based (≥ 0.25 dominance threshold on composite query):
        R2 dominant, R4 dominant, R4b dominant, R3 dominant, R5 dominant,
        cross-query constant-token prevalent, direct-query shortcut prevalent
      own-criteria:
        control-floor failure (controls below threshold)
        other-rate-ceiling breach (composite R6cat > 0.10, ONLY residual R6cat)
"""
from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent

# Locked-here per preregistration §11 + §15 (read from constants for cross-check).
sys.path.insert(0, str(RUN_DIR.parents[1] / "path-a" / "inspector"))
import constants as path_a_constants

DOMINANCE_THRESHOLD     = path_a_constants.DOMINANT_RATE_THRESHOLD   # 0.25
SUCCESS_THRESHOLD       = path_a_constants.success_threshold()       # 0.45
HEURISTIC_FLOOR         = path_a_constants.heuristic_floor()         # 0.20
OTHER_RATE_CEILING      = 0.10                                       # prereg §15 (residual R6cat only)
N_ITEMS                 = path_a_constants.N_ITEMS_PER_CELL          # 96
WILSON_Z                = 1.95996398454005    # two-sided 95% z

_ANSWER_RE = re.compile(r"^ANSWER:\s+(.+?)\s*$", re.IGNORECASE)


def extract(raw: str) -> str | None:
    m = _ANSWER_RE.match(raw.strip())
    if not m: return None
    return m.group(1).strip()


def classify(token: str | None, t: dict, decoy_terminals: set, X_set: set) -> str:
    """Classify a composite-query response per R1–R6cat (v0.4 §2)."""
    if token is None or token == "":  return "R6cat"
    if token == "NULL":               return "R5"
    if token == t["C_star"]:          return "R1"
    if token == t["T"]:               return "R2"
    if token == t["B"]:               return "R3"
    if token in decoy_terminals:      return "R4"
    if token in X_set:                return "R4b"
    return "R6cat"


def wilson_ci(k: int, n: int, z: float = WILSON_Z) -> tuple[float, float, float]:
    """Two-sided 100(1-α)% Wilson score interval for a binomial proportion.
    Returns (point_estimate, lower, upper)."""
    if n == 0: return (0.0, 0.0, 1.0)
    p = k / n
    denom = 1.0 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = (z / denom) * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (p, max(0.0, center - half), min(1.0, center + half))


def main() -> int:
    items_doc = json.loads((RUN_DIR / "items_materialized.json").read_text())
    raw_doc   = json.loads((RUN_DIR / "fp16_raw_outputs.json").read_text())

    items_by_id = {it["item_id"]: it for it in items_doc["items"]}
    raw_by_key = {(r["item_id"], r["query_type"]): r for r in raw_doc["results"]}

    # Per-item analysis
    per_item: list[dict] = []
    for item_id, item in items_by_id.items():
        t = item["target"]
        decoy_terminals = {d["T_i"] for d in item["decoy_chains"]}
        X_set = {c["X"] for c in item["depth_2_competitors"]}

        composite = raw_by_key[(item_id, "composite")]
        hop1 = raw_by_key[(item_id, "hop1")]
        hop2 = raw_by_key[(item_id, "hop2")]
        dq   = raw_by_key[(item_id, "direct_query")]

        composite_token = extract(composite["raw_output"])
        hop1_token      = extract(hop1["raw_output"])
        hop2_token      = extract(hop2["raw_output"])
        dq_token        = extract(dq["raw_output"])

        composite_category = classify(composite_token, t, decoy_terminals, X_set)

        # R7 controls
        hop1_pass = (hop1_token == t["B"])
        hop2_pass = (hop2_token == t["C_star"])
        # Direct-query control: the model should NOT produce C* with the bridge withheld.
        # A pass = model did NOT emit C* (so emitted NULL or anything else != C*).
        dq_pass = (dq_token != t["C_star"])

        controls_pass = hop1_pass and hop2_pass and dq_pass

        # R6 invalidators applied to composite-R1 candidacy
        invalidators: list[str] = []
        # R6a — terminal coincidence: composite == C* AND C* is a terminal.
        if composite_token == t["C_star"] and (
            composite_token == t["T"] or composite_token in decoy_terminals
        ):
            invalidators.append("R6a_terminal_coincidence")
        # R6b — controls not available
        if not hop1_pass:
            invalidators.append("R6b_hop1_control_failed")
        if not hop2_pass:
            invalidators.append("R6b_hop2_control_failed")
        # R6c — direct A→C* shortcut
        if not dq_pass:
            invalidators.append("R6c_direct_query_shortcut")
        # R6e — cross-query constant-token
        all_tokens = [composite_token, hop1_token, hop2_token, dq_token]
        if len(set(all_tokens)) == 1 and all_tokens[0] is not None:
            invalidators.append("R6e_cross_query_constant_token")

        # R1 validation (R1 candidate AND R7 pass AND no invalidator)
        is_R1_candidate = (composite_category == "R1")
        is_R1_validated = (is_R1_candidate and controls_pass and not invalidators)

        per_item.append({
            "item_id":           item_id,
            "position_slot":     item["position_slot"],
            "composite_token":   composite_token,
            "hop1_token":        hop1_token,
            "hop2_token":        hop2_token,
            "dq_token":          dq_token,
            "composite_category": composite_category,
            "hop1_pass":         hop1_pass,
            "hop2_pass":         hop2_pass,
            "dq_pass":           dq_pass,
            "controls_pass":     controls_pass,
            "invalidators":      invalidators,
            "is_R1_candidate":   is_R1_candidate,
            "is_R1_validated":   is_R1_validated,
        })

    # Aggregates
    n_items = len(per_item)
    composite_category_counts = Counter(r["composite_category"] for r in per_item)
    composite_rates = {k: v / n_items for k, v in composite_category_counts.items()}
    n_R1_validated = sum(1 for r in per_item if r["is_R1_validated"])
    n_R1_candidates = sum(1 for r in per_item if r["is_R1_candidate"])
    R1_validated_rate, R1_ci_lower, R1_ci_upper = wilson_ci(n_R1_validated, n_items)

    # Failure signatures (rate-based, on composite query)
    rate_based_signatures = []
    for sig, cat in [("R2_dominant", "R2"), ("R4_dominant", "R4"), ("R4b_dominant", "R4b"),
                      ("R3_dominant", "R3"), ("R5_dominant", "R5")]:
        if composite_rates.get(cat, 0.0) >= DOMINANCE_THRESHOLD:
            rate_based_signatures.append(sig)

    # cross-query constant-token prevalent
    constant_token_count = sum(1 for r in per_item if "R6e_cross_query_constant_token" in r["invalidators"])
    constant_token_rate = constant_token_count / n_items
    if constant_token_rate >= DOMINANCE_THRESHOLD:
        rate_based_signatures.append("cross_query_constant_token_prevalent")

    # direct-query shortcut prevalent
    direct_query_shortcut_count = sum(1 for r in per_item if "R6c_direct_query_shortcut" in r["invalidators"])
    direct_query_shortcut_rate = direct_query_shortcut_count / n_items
    if direct_query_shortcut_rate >= DOMINANCE_THRESHOLD:
        rate_based_signatures.append("direct_query_shortcut_prevalent")

    # Own-criteria signatures
    own_signatures = []
    # control-floor failure: per-item hop1/hop2/dq controls below threshold globally
    hop1_pass_rate = sum(1 for r in per_item if r["hop1_pass"]) / n_items
    hop2_pass_rate = sum(1 for r in per_item if r["hop2_pass"]) / n_items
    dq_pass_rate   = sum(1 for r in per_item if r["dq_pass"]) / n_items
    if hop1_pass_rate < 0.75:
        own_signatures.append(f"control_floor_failure_hop1_{hop1_pass_rate:.3f}")
    if hop2_pass_rate < 0.75:
        own_signatures.append(f"control_floor_failure_hop2_{hop2_pass_rate:.3f}")
    if dq_pass_rate < 0.75:
        own_signatures.append(f"control_floor_failure_direct_query_{dq_pass_rate:.3f}")

    # other-rate-ceiling breach: composite R6cat > 0.10 (residual ONLY; R4b is separate)
    R6cat_rate = composite_rates.get("R6cat", 0.0)
    if R6cat_rate > OTHER_RATE_CEILING:
        own_signatures.append(f"other_rate_ceiling_breach_R6cat_{R6cat_rate:.3f}_threshold_{OTHER_RATE_CEILING}")

    all_dominant_signatures = rate_based_signatures + own_signatures

    # Decision rule (MECE per prereg §14)
    if R1_ci_upper < HEURISTIC_FLOOR or all_dominant_signatures:
        outcome = "FAIL"
        if R1_ci_upper < HEURISTIC_FLOOR and not all_dominant_signatures:
            reason = f"upper CI {R1_ci_upper:.4f} < floor {HEURISTIC_FLOOR}; R1 below floor (no failure signature dominant)"
        elif all_dominant_signatures and R1_ci_upper >= HEURISTIC_FLOOR:
            reason = f"failure signature(s) dominant: {all_dominant_signatures}"
        else:
            reason = f"both: upper CI {R1_ci_upper:.4f} < floor {HEURISTIC_FLOOR} AND dominant signature(s): {all_dominant_signatures}"
    elif R1_ci_lower > SUCCESS_THRESHOLD and not all_dominant_signatures:
        outcome = "CERTIFY"
        reason = f"lower CI {R1_ci_lower:.4f} > threshold {SUCCESS_THRESHOLD}; no dominant failure signature"
    else:
        outcome = "INCONCLUSIVE"
        reason = (f"CI [{R1_ci_lower:.4f}, {R1_ci_upper:.4f}] does not satisfy CERTIFY "
                  f"(lower > {SUCCESS_THRESHOLD}) and does not satisfy FAIL "
                  f"(upper < {HEURISTIC_FLOOR}); no dominant signature.")

    # Per-position diagnostic (R6d layout-position post-hoc)
    by_position = {}
    for r in per_item:
        slot = r["position_slot"]
        bucket = by_position.setdefault(slot, {"n": 0, "R1_validated": 0})
        bucket["n"] += 1
        if r["is_R1_validated"]:
            bucket["R1_validated"] += 1
    per_position = {
        slot: {**v, "R1_validated_rate": v["R1_validated"] / v["n"]}
        for slot, v in sorted(by_position.items())
    }

    # Summary
    summary = {
        "stage":                    "scored",
        "preregistration_sha":      "d9bd9b219badd25901811ddfbb43b811a04750a77723f6a1f076c7dd641f091c",
        "n_items":                  n_items,
        "composite_category_counts": dict(composite_category_counts),
        "composite_rates":          composite_rates,
        "control_pass_rates": {
            "hop1": hop1_pass_rate,
            "hop2": hop2_pass_rate,
            "direct_query": dq_pass_rate,
        },
        "invalidation_counts": {
            "R6c_direct_query_shortcut":      direct_query_shortcut_count,
            "R6e_cross_query_constant_token": constant_token_count,
            "R1_candidates_total":            n_R1_candidates,
            "R1_candidates_invalidated":      n_R1_candidates - n_R1_validated,
            "R1_validated":                   n_R1_validated,
        },
        "R1_validated_rate":        R1_validated_rate,
        "wilson_95_ci": {
            "lower":                R1_ci_lower,
            "upper":                R1_ci_upper,
            "half_width":           (R1_ci_upper - R1_ci_lower) / 2.0,
            "z":                    WILSON_Z,
            "method":               "two-sided 95% Wilson score interval (locked per prereg §14)",
        },
        "thresholds_used": {
            "success_threshold":    SUCCESS_THRESHOLD,
            "heuristic_floor":      HEURISTIC_FLOOR,
            "dominance_threshold":  DOMINANCE_THRESHOLD,
            "other_rate_ceiling":   OTHER_RATE_CEILING,
        },
        "failure_signatures": {
            "rate_based_dominant":  rate_based_signatures,
            "own_criteria":         own_signatures,
            "all":                  all_dominant_signatures,
            "any_dominant":         bool(all_dominant_signatures),
        },
        "per_position_diagnostic":  per_position,
        "outcome":                  outcome,
        "outcome_reason":           reason,
    }

    (RUN_DIR / "scored.json").write_text(json.dumps({"per_item": per_item, "summary": summary}, indent=2) + "\n")

    print(f"=== Path A FP16 Constructibility — analysis ===")
    print(f"  composite categories (n={n_items}):")
    for cat, ct in sorted(composite_category_counts.items()):
        print(f"    {cat:8s}  count={ct:3d}  rate={ct/n_items:.4f}")
    print(f"  control pass rates:  hop1={hop1_pass_rate:.3f}  hop2={hop2_pass_rate:.3f}  dq={dq_pass_rate:.3f}")
    print(f"  R1 candidates: {n_R1_candidates}; R1 validated: {n_R1_validated}; rate = {R1_validated_rate:.4f}")
    print(f"  Wilson 95% CI: [{R1_ci_lower:.4f}, {R1_ci_upper:.4f}]   half-width={summary['wilson_95_ci']['half_width']:.4f}")
    print(f"  thresholds: floor={HEURISTIC_FLOOR}  threshold={SUCCESS_THRESHOLD}  dominance={DOMINANCE_THRESHOLD}  other_ceiling={OTHER_RATE_CEILING}")
    if all_dominant_signatures:
        print(f"  dominant failure signatures: {all_dominant_signatures}")
    print(f"  OUTCOME: {outcome}")
    print(f"    reason: {reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
