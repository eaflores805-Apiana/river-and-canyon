#!/usr/bin/env python3
"""
analyze.py -- Path A K-Sweep Scout per-cell analysis.

Per locked prereg v1.0 (sha 248581f6...) §3 + §4. Reads
items_materialized_K{K}.json + fp16_raw_outputs_K{K}.json; emits scored_K{K}.json.

PRIMARY metric (locked, descriptive):
  validated-R1 per cell + Wilson 95% CI (NOT Clopper-Pearson; matches closed K=5 run).

SECONDARY metrics (per prereg §3, reported alongside, NEVER blended into primary):
  - OFF-MAP POSITIONAL RATE = (decoy answer-depth dC + decoy bridge dB) landings / n
  - DIAL A = answer-depth landing rate (composite in {C*, X_i, decoy.answer_i}) / n
  - DIAL B = right-chain share among answer-depth landings; reported vs per-K base rate
            (base = 1/(1+K+D) where K = decoy chains in this cell, D = competitors = 5)
  - CROSS-QUERY CHAIN-MEMBERSHIP PATTERN: per item, classify composite/hop1/hop2 by
            chain (target / decoy_i / competitor_i / off); GATED on component load-floor
            (hop1+hop2 pass); reported as the distribution (NOT a single rate, per
            prereg explicitly).
  - CONTROL MARGINS: terminal-grab rate (R2), R4b rate (depth-competitor grab),
            direct-query pass rate, hop1/hop2 control-floor headroom.

NO outcome rule applied at the cell level (this is a descriptive scout, not a
certification run). Cross-cell band/null/boundary disposition is in scout_summary.py.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(RUN_DIR.parents[1] / "path-a" / "inspector"))
import constants as path_a_constants

DOMINANCE_THRESHOLD     = path_a_constants.DOMINANT_RATE_THRESHOLD   # 0.25 (informational only at cell level)
SUCCESS_THRESHOLD       = path_a_constants.success_threshold()       # 0.45 (informational only; descriptive scout)
HEURISTIC_FLOOR         = path_a_constants.heuristic_floor()         # 0.20 (informational only)
N_ITEMS                 = path_a_constants.N_ITEMS_PER_CELL          # 96
D_COMPETITORS           = path_a_constants.D_DEPTH_COMPETITORS       # 5 (fixed across sweep)
WILSON_Z                = 1.95996398454005

_ANSWER_RE = re.compile(r"^ANSWER:\s+(.+?)\s*$", re.IGNORECASE)


def extract(raw: str) -> str | None:
    m = _ANSWER_RE.match(raw.strip())
    if not m: return None
    return m.group(1).strip()


def classify_composite(token: str | None, t: dict, decoy_terminals: set, X_set: set) -> str:
    """R1..R6cat classification matching the closed K=5 run's scorer."""
    if token is None or token == "":  return "R6cat"
    if token == "NULL":               return "R5"
    if token == t["C_star"]:          return "R1"
    if token == t["T"]:               return "R2"
    if token == t["B"]:               return "R3"
    if token in decoy_terminals:      return "R4"
    if token in X_set:                return "R4b"
    return "R6cat"


def classify_chain_membership(token: str | None, item: dict) -> str:
    """Which chain is this token on?
       'target' / 'decoy_i' / 'competitor_i' / 'off'
       A is the anchor (shared); tokens uniquely on the target = {B, C*, T}."""
    if token is None or token == "" or token == "NULL":
        return "off"
    t = item["target"]
    if token in {t["B"], t["C_star"], t["T"]}:
        return "target"
    for i, d in enumerate(item["decoy_chains"], 1):
        if token in {d["head"], d["bridge"], d["answer"], d["T_i"]}:
            return f"decoy_{i}"
    for i, c in enumerate(item["depth_2_competitors"], 1):
        if token in {c["B_competitor"], c["X"]}:
            return f"competitor_{i}"
    return "off"


def wilson_ci(k: int, n: int, z: float = WILSON_Z) -> tuple[float, float, float]:
    if n == 0: return (0.0, 0.0, 1.0)
    p = k / n
    denom = 1.0 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = (z / denom) * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (p, max(0.0, center - half), min(1.0, center + half))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--K", type=int, required=True, choices=[1, 2, 3, 4, 5])
    args = ap.parse_args()
    K_cell = args.K

    items_doc = json.loads((RUN_DIR / f"items_materialized_K{K_cell}.json").read_text())
    raw_doc   = json.loads((RUN_DIR / f"fp16_raw_outputs_K{K_cell}.json").read_text())

    items_by_id = {it["item_id"]: it for it in items_doc["items"]}
    raw_by_key = {(r["item_id"], r["query_type"]): r for r in raw_doc["results"]}

    per_item: list[dict] = []
    for item_id, item in items_by_id.items():
        t = item["target"]
        decoy_terminals = {d["T_i"] for d in item["decoy_chains"]}
        decoy_bridges   = {d["bridge"] for d in item["decoy_chains"]}
        decoy_answers   = {d["answer"] for d in item["decoy_chains"]}
        decoy_heads     = {d["head"] for d in item["decoy_chains"]}
        X_set           = {c["X"] for c in item["depth_2_competitors"]}
        B_comp_set      = {c["B_competitor"] for c in item["depth_2_competitors"]}

        composite = raw_by_key[(item_id, "composite")]
        hop1 = raw_by_key[(item_id, "hop1")]
        hop2 = raw_by_key[(item_id, "hop2")]
        dq   = raw_by_key[(item_id, "direct_query")]

        composite_token = extract(composite["raw_output"])
        hop1_token      = extract(hop1["raw_output"])
        hop2_token      = extract(hop2["raw_output"])
        dq_token        = extract(dq["raw_output"])

        composite_category = classify_composite(composite_token, t, decoy_terminals, X_set)

        # R7 controls
        hop1_pass = (hop1_token == t["B"])
        hop2_pass = (hop2_token == t["C_star"])
        dq_pass = (dq_token != t["C_star"])
        controls_pass = hop1_pass and hop2_pass and dq_pass

        # R6 invalidators
        invalidators: list[str] = []
        if composite_token == t["C_star"] and (
            composite_token == t["T"] or composite_token in decoy_terminals
        ):
            invalidators.append("R6a_terminal_coincidence")
        if not hop1_pass:
            invalidators.append("R6b_hop1_control_failed")
        if not hop2_pass:
            invalidators.append("R6b_hop2_control_failed")
        if not dq_pass:
            invalidators.append("R6c_direct_query_shortcut")
        all_tokens = [composite_token, hop1_token, hop2_token, dq_token]
        if len(set(all_tokens)) == 1 and all_tokens[0] is not None:
            invalidators.append("R6e_cross_query_constant_token")

        is_R1_candidate = (composite_category == "R1")
        is_R1_validated = (is_R1_candidate and controls_pass and not invalidators)

        # Off-map positional landings on this item
        is_decoy_answer_landing = (composite_token in decoy_answers)
        is_decoy_bridge_landing = (composite_token in decoy_bridges)
        is_decoy_head_landing   = (composite_token in decoy_heads)
        # Dial A: depth-2 answer-position landing (target OR decoy OR competitor X)
        is_answer_depth_landing = (
            composite_token == t["C_star"] or
            composite_token in decoy_answers or
            composite_token in X_set
        )
        is_right_chain_at_answer_depth = (composite_token == t["C_star"])

        # Chain membership per query (composite/hop1/hop2)
        composite_chain = classify_chain_membership(composite_token, item)
        hop1_chain      = classify_chain_membership(hop1_token, item)
        hop2_chain      = classify_chain_membership(hop2_token, item)

        per_item.append({
            "item_id":            item_id,
            "position_slot":      item["position_slot"],
            "composite_token":    composite_token,
            "hop1_token":         hop1_token,
            "hop2_token":         hop2_token,
            "dq_token":           dq_token,
            "composite_category": composite_category,
            "hop1_pass":          hop1_pass,
            "hop2_pass":          hop2_pass,
            "dq_pass":            dq_pass,
            "controls_pass":      controls_pass,
            "invalidators":       invalidators,
            "is_R1_candidate":    is_R1_candidate,
            "is_R1_validated":    is_R1_validated,
            "is_decoy_answer_landing":         is_decoy_answer_landing,
            "is_decoy_bridge_landing":         is_decoy_bridge_landing,
            "is_decoy_head_landing":           is_decoy_head_landing,
            "is_answer_depth_landing":         is_answer_depth_landing,
            "is_right_chain_at_answer_depth":  is_right_chain_at_answer_depth,
            "composite_chain":    composite_chain,
            "hop1_chain":         hop1_chain,
            "hop2_chain":         hop2_chain,
        })

    # ── Aggregates ──────────────────────────────────────────────────────────
    n_items = len(per_item)
    composite_category_counts = Counter(r["composite_category"] for r in per_item)
    composite_rates = {k: v / n_items for k, v in composite_category_counts.items()}
    n_R1_validated = sum(1 for r in per_item if r["is_R1_validated"])
    n_R1_candidates = sum(1 for r in per_item if r["is_R1_candidate"])
    R1_validated_rate, R1_ci_lower, R1_ci_upper = wilson_ci(n_R1_validated, n_items)

    # OFF-MAP POSITIONAL RATE: (decoy answer-depth + decoy bridge) / n
    n_decoy_answer  = sum(1 for r in per_item if r["is_decoy_answer_landing"])
    n_decoy_bridge  = sum(1 for r in per_item if r["is_decoy_bridge_landing"])
    n_decoy_head    = sum(1 for r in per_item if r["is_decoy_head_landing"])
    off_map_positional_count = n_decoy_answer + n_decoy_bridge
    off_map_positional_rate  = off_map_positional_count / n_items
    off_map_dC_rate          = n_decoy_answer / n_items  # decoy answer depth
    off_map_dB_rate          = n_decoy_bridge / n_items  # decoy bridge depth

    # DIAL A: answer-depth landing rate (target + decoy answers + competitor X)
    n_answer_depth = sum(1 for r in per_item if r["is_answer_depth_landing"])
    dial_A_answer_depth_rate = n_answer_depth / n_items

    # DIAL B: right-chain share among answer-depth landings; vs per-K base rate
    n_right_chain_at_depth = sum(1 for r in per_item if r["is_right_chain_at_answer_depth"])
    if n_answer_depth > 0:
        dial_B_right_chain_share = n_right_chain_at_depth / n_answer_depth
    else:
        dial_B_right_chain_share = None
    # base rate: with 1 target + D competitors + K_cell decoys, naive uniform answer-depth
    # distribution = right-chain share base = 1 / (1 + D + K)
    dial_B_base_rate = 1.0 / (1 + D_COMPETITORS + K_cell)
    dial_B_gain_over_base = (
        dial_B_right_chain_share - dial_B_base_rate
        if dial_B_right_chain_share is not None else None
    )

    # CROSS-QUERY CHAIN-MEMBERSHIP PATTERN -- gated on hop1+hop2 pass
    pattern_counts = Counter()
    pattern_breakdown_per_item = []
    for r in per_item:
        gated = r["hop1_pass"] and r["hop2_pass"]
        if not gated:
            pattern = "gated_out_no_component_floor"
        else:
            triple = (r["composite_chain"], r["hop1_chain"], r["hop2_chain"])
            # Note: hop1_chain reflects the bridge answer; hop2_chain reflects the C* answer.
            # We classify: anchor-tracking = all on 'target' (composite==C*, hop1==B, hop2==C*)
            #             fixed = all three on the same wrong chain (e.g., all decoy_3)
            #             switching = otherwise
            if all(c == "target" for c in triple):
                pattern = "anchor_tracking_target"
            elif triple[0] == triple[1] == triple[2] and triple[0] != "target":
                pattern = f"fixed_wrong_chain_{triple[0]}"
            else:
                pattern = "switching"
        pattern_counts[pattern] += 1
        pattern_breakdown_per_item.append({"item_id": r["item_id"], "pattern": pattern,
                                            "chains": (r["composite_chain"], r["hop1_chain"], r["hop2_chain"])})
    # Collapse fixed_wrong_chain_* into a single bucket for headline; keep detail
    pattern_summary = Counter()
    for pat, ct in pattern_counts.items():
        if pat.startswith("fixed_wrong_chain_"):
            pattern_summary["fixed_wrong_chain"] += ct
        else:
            pattern_summary[pat] += ct

    # CONTROL MARGINS
    hop1_pass_rate = sum(1 for r in per_item if r["hop1_pass"]) / n_items
    hop2_pass_rate = sum(1 for r in per_item if r["hop2_pass"]) / n_items
    dq_pass_rate   = sum(1 for r in per_item if r["dq_pass"]) / n_items
    terminal_grab_R2_rate = composite_rates.get("R2", 0.0)
    R4b_depth_competitor_rate = composite_rates.get("R4b", 0.0)
    R4_decoy_terminal_rate = composite_rates.get("R4", 0.0)
    control_floor_threshold = 0.75
    hop1_headroom = hop1_pass_rate - control_floor_threshold
    hop2_headroom = hop2_pass_rate - control_floor_threshold

    # Per-position diagnostic
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

    summary = {
        "stage":                    "scored",
        "K_cell":                   K_cell,
        "preregistration_sha":      "248581f673df2300ddf8567bd7fb826f1c3536dd459ff20576b689a07ea5ab90",
        "n_items":                  n_items,
        # PRIMARY
        "primary": {
            "R1_validated":          n_R1_validated,
            "R1_validated_rate":     R1_validated_rate,
            "wilson_95_ci": {
                "lower":             R1_ci_lower,
                "upper":             R1_ci_upper,
                "half_width":        (R1_ci_upper - R1_ci_lower) / 2.0,
                "z":                 WILSON_Z,
                "method":            "two-sided 95% Wilson score interval",
            },
            "R1_candidates_total":   n_R1_candidates,
        },
        # SECONDARY (per prereg §3)
        "secondary": {
            "off_map_positional": {
                "rate":                off_map_positional_rate,
                "count":               off_map_positional_count,
                "decoy_answer_depth_dC": {"count": n_decoy_answer, "rate": off_map_dC_rate},
                "decoy_bridge_depth_dB": {"count": n_decoy_bridge, "rate": off_map_dB_rate},
                "decoy_head_landings":   {"count": n_decoy_head,   "rate": n_decoy_head/n_items},
                "interpretation":      "POSITIONAL where-tokens-land vs K; not mechanism (per prereg §3 + closed K=5 R6cat decomposition)",
            },
            "dial_A_answer_depth_landing": {
                "rate":                dial_A_answer_depth_rate,
                "count":               n_answer_depth,
                "interpretation":      "fraction at depth-2 answer position (target C*, decoy answers, competitor X); NOT 'walk rate'",
            },
            "dial_B_right_chain_share": {
                "share":               dial_B_right_chain_share,
                "n_right_at_depth":    n_right_chain_at_depth,
                "n_at_depth_total":    n_answer_depth,
                "base_rate":           dial_B_base_rate,
                "base_rate_formula":   "1/(1+D+K)  with D=5, K=K_cell",
                "gain_over_base":      dial_B_gain_over_base,
                "interpretation":      "right-chain share among answer-depth landings, baselined; gain > 0 = chain selection beats uniform",
            },
            "chain_membership_pattern": {
                "pattern_summary":     dict(pattern_summary),
                "pattern_detailed":    dict(pattern_counts),
                "gated_on":            "hop1_pass AND hop2_pass (component load-floor)",
                "interpretation":      "PATTERN distribution, not a single rate (per prereg explicit)",
            },
            "control_margins": {
                "hop1_pass_rate":       hop1_pass_rate,
                "hop2_pass_rate":       hop2_pass_rate,
                "hop1_headroom_vs_075": hop1_headroom,
                "hop2_headroom_vs_075": hop2_headroom,
                "dq_pass_rate":         dq_pass_rate,
                "terminal_grab_R2_rate": terminal_grab_R2_rate,
                "decoy_terminal_R4_rate": R4_decoy_terminal_rate,
                "depth_competitor_R4b_rate": R4b_depth_competitor_rate,
                "control_floor_threshold": control_floor_threshold,
            },
        },
        # Diagnostic context
        "composite_category_counts": dict(composite_category_counts),
        "composite_rates":           composite_rates,
        "per_position_diagnostic":   per_position,
        # Thresholds (informational only at cell level; cross-cell disposition in scout_summary.py)
        "thresholds_informational": {
            "success_threshold":     SUCCESS_THRESHOLD,
            "heuristic_floor":       HEURISTIC_FLOOR,
            "dominance_threshold":   DOMINANCE_THRESHOLD,
            "note":                  "These are informational at the cell level. The K-sweep scout is DESCRIPTIVE; no CERTIFY/FAIL outcome is computed per cell. The closed K=5 run (sha b46725bf...) carries the binding FAIL outcome for K=5; this run's K=5 cell is a reproduction harness check, not a re-run of that outcome.",
        },
    }

    out = {"per_item": per_item, "summary": summary,
           "pattern_breakdown_per_item": pattern_breakdown_per_item}
    (RUN_DIR / f"scored_K{K_cell}.json").write_text(json.dumps(out, indent=2) + "\n")

    print(f"=== K={K_cell} scoring ===")
    print(f"  composite categories (n={n_items}):")
    for cat, ct in sorted(composite_category_counts.items()):
        print(f"    {cat:8s}  count={ct:3d}  rate={ct/n_items:.4f}")
    print(f"  control pass rates:  hop1={hop1_pass_rate:.3f}  hop2={hop2_pass_rate:.3f}  dq={dq_pass_rate:.3f}")
    print(f"  PRIMARY  R1_validated = {n_R1_validated}/{n_items} = {R1_validated_rate:.4f}   Wilson 95% CI = [{R1_ci_lower:.4f}, {R1_ci_upper:.4f}]")
    print(f"  SECONDARY  off-map positional rate = {off_map_positional_rate:.4f}  (dC={off_map_dC_rate:.3f}  dB={off_map_dB_rate:.3f})")
    print(f"  SECONDARY  Dial A (answer-depth landing) = {dial_A_answer_depth_rate:.4f}")
    if dial_B_right_chain_share is not None:
        print(f"  SECONDARY  Dial B (right-chain share at depth) = {dial_B_right_chain_share:.4f}   base = {dial_B_base_rate:.4f}   gain = {dial_B_gain_over_base:+.4f}")
    print(f"  SECONDARY  chain-membership pattern: {dict(pattern_summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
