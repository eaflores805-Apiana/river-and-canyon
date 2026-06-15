#!/usr/bin/env python3
"""
g6_evaluator_v0_3.py — G6 Evaluator v0.3 (Path A multiclass scorer)

Extends v0.2 with:
  - R1 / R2 / R3 / R4 / R4b / R5 / R6cat multiclass categorization (per construct
    definition v0.3 §2)
  - R6 invalidators a-f (computable side per OI-10)
  - Derived F = max(1/p, 1/m, 1/D); success threshold = F + margin (OI-3)
  - §8 outcome branches: CERTIFY / INCONCLUSIVE / FAIL / REJECTED-CONSTRUCTION /
    SUBSTRATE-INFEASIBILITY (per construct definition v0.3 §8)
  - Per-item / per-query token logging + computable vs judgment-flagged exclusions

Reads a fixture or run directory containing:
  - construction_spec.json  (the entity set per item; what tokens are C*/B/T/T_i/X_i)
  - fp16_raw_outputs.json   (results: [{item_id, query_type, raw_output, expected, ...}])
                            query_type ∈ {composite, hop1, hop2, direct_query}

Authority: TL ACTION 2026-06-15 ("Build Path A Inspector + G6 v0.3").
Static software; no model execution; reads bytes only.

The known v0.1 disposition for each fixture lives in
  expected/path_a/<fixture>_expected.json
NOT in this evaluator. The evaluator is generic.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


# Pre-declared category vocabulary (locked).
R1_CORRECT_COMPOSITION      = "R1_correct_composition"
R2_TARGET_TERMINAL_GRAB     = "R2_target_terminal_grab"
R3_STOPPED_SHORT            = "R3_stopped_short"
R4_DECOY_TERMINAL_GRAB      = "R4_decoy_terminal_grab"
R4B_DEPTH_COMPETITOR_GRAB   = "R4b_depth_competitor_grab"
R5_ABSTAIN                  = "R5_abstain"
R6CAT_OTHER                 = "R6cat_other"

# Outcome branches.
OUTCOME_CERTIFY                  = "CERTIFY"
OUTCOME_INCONCLUSIVE             = "INCONCLUSIVE"
OUTCOME_FAIL                     = "FAIL"
OUTCOME_REJECTED_CONSTRUCTION    = "REJECTED_CONSTRUCTION"
OUTCOME_SUBSTRATE_INFEASIBILITY  = "SUBSTRATE_INFEASIBILITY_CANDIDATE"
OUTCOME_BUNDLE_INSUFFICIENT      = "BUNDLE_INSUFFICIENT"

# Failure-signature dominance threshold (a single category > 0.25 of items is
# "dominant" per construct definition v0.3 §11; declared here for the scorer).
DOMINANT_RATE_THRESHOLD = 0.25

_ANSWER_RE = re.compile(r"^ANSWER:\s+(.+?)\s*$", re.IGNORECASE)


def extract_answer(raw_output: str) -> str | None:
    """Extract the model's answer token from a raw output. Returns None on
    format failure; the string 'NULL' is treated as the abstain form."""
    m = _ANSWER_RE.match(raw_output.strip())
    if not m:
        return None
    return m.group(1).strip()


def classify_response(token: str | None,
                      query_type: str,
                      target_C_star: str,
                      target_B: str,
                      target_T: str,
                      decoy_terminals: set[str],
                      depth_competitors_X: set[str]) -> str:
    """Pre-registered classification rule per construct definition v0.3 §2.
    Returns one of the seven category constants."""
    if token is None or token == "":
        return R6CAT_OTHER
    if token == "NULL":
        return R5_ABSTAIN

    # R1: correct composition — token equals C* (further invalidation by R6 a-f
    # is applied downstream, not here; this is the raw category).
    if token == target_C_star:
        return R1_CORRECT_COMPOSITION
    if token == target_T:
        return R2_TARGET_TERMINAL_GRAB
    if token == target_B:
        return R3_STOPPED_SHORT
    if token in decoy_terminals:
        return R4_DECOY_TERMINAL_GRAB
    if token in depth_competitors_X:
        return R4B_DEPTH_COMPETITOR_GRAB
    return R6CAT_OTHER


def per_item_index(results: list[dict]) -> dict[str, dict[str, dict]]:
    """Build {item_id: {query_type: result_dict}}."""
    out: dict[str, dict[str, dict]] = {}
    for r in results:
        out.setdefault(r["item_id"], {})[r["query_type"]] = r
    return out


# ── R6 invalidators (computable; per construct definition v0.3 R6 a-f) ──────
def invalidate_R1(per_item: dict[str, dict[str, dict]],
                  spec: dict) -> dict[str, list[str]]:
    """For each item whose composite token == C*, determine if any R6
    invalidator applies. Returns {item_id: [list of invalidator names]}."""
    invalidations: dict[str, list[str]] = {}
    target_C_star = spec["target"]["C_star"]
    target_T      = spec["target"]["T"]
    decoy_terminals = {d["T_i"] for d in spec.get("decoy_chains", [])}

    for item_id, queries in per_item.items():
        composite = queries.get("composite")
        if not composite:
            continue
        comp_token = extract_answer(composite["raw_output"])
        if comp_token != target_C_star:
            continue
        invalidators: list[str] = []

        # R6a: terminal coincidence (if R8.1 was breached and composite happens
        # to land on a terminal that = C*). Mechanically: composite token in
        # terminals.
        if comp_token in decoy_terminals or comp_token == target_T:
            invalidators.append("R6a_terminal_coincidence")

        # R6b: components not available — hop1 or hop2 control failed.
        for ctrl in ("hop1", "hop2"):
            ctrl_r = queries.get(ctrl)
            if ctrl_r:
                ctrl_tok = extract_answer(ctrl_r["raw_output"])
                if ctrl_tok != ctrl_r.get("expected"):
                    invalidators.append(f"R6b_{ctrl}_control_failed")
                    break

        # R6c (empirical side): direct-query control returned C*.
        dq = queries.get("direct_query")
        if dq:
            dq_tok = extract_answer(dq["raw_output"])
            if dq_tok == target_C_star:
                invalidators.append("R6c_direct_query_shortcut")

        # R6e: cross-query constant-token (composite + hop1 + hop2 + direct_query
        # all emit the same token).
        all_tokens = [extract_answer(queries[qt]["raw_output"]) for qt in queries
                      if qt in ("composite", "hop1", "hop2", "direct_query")]
        if len(set(all_tokens)) == 1 and all_tokens[0] is not None:
            invalidators.append("R6e_cross_query_constant_token")

        if invalidators:
            invalidations[item_id] = invalidators
    return invalidations


# ── Heuristic floor (derived from spec params) ──────────────────────────────
def compute_floor(spec: dict) -> dict:
    """F = max(1/p, 1/m, 1/D). Reads params from spec; falls back to Manager
    defaults if unspecified."""
    params = spec.get("params", {})
    p = int(params.get("p", 5))
    m = int(params.get("m", 10))
    D = int(params.get("D", 5))
    margin = float(params.get("margin", 0.25))
    F_terminal_grab  = 0.0   # by R8.1 enforcement
    F_direct_query   = 0.0   # measured ≈ 0 on retained subset
    F_position       = 1.0 / p
    F_token_pick     = 1.0 / m
    F_depth_select   = 1.0 / D
    F = max(F_terminal_grab, F_direct_query, F_position, F_token_pick, F_depth_select)
    threshold = F + margin
    return {
        "F":           F,
        "components": {
            "F_terminal_grab":  F_terminal_grab,
            "F_direct_query":   F_direct_query,
            "F_position_1_p":   F_position,
            "F_token_pick_1_m": F_token_pick,
            "F_depth_1_D":      F_depth_select,
        },
        "margin":       margin,
        "threshold":    threshold,
        "params_used": {"p": p, "m": m, "D": D, "margin": margin},
    }


# ── Outcome branch derivation (§8) ──────────────────────────────────────────
def derive_outcome(categorized: list[dict],
                   floor_info: dict,
                   invalidations: dict[str, list[str]],
                   spec: dict) -> dict:
    """Apply construct definition v0.3 §8 outcome rules:
      8.1 CERTIFY   R1 rate ≥ threshold, controls pass, no failure signature dominant
      8.2 INCONCLUSIVE   R1 rate in the inconclusive band
      8.3 FAIL   a failure signature dominant, or R1 below threshold
      8.4 REJECTED-CONSTRUCTION   R6a fired (terminal coincidence)
      8.5 SUBSTRATE-INFEASIBILITY   pre-committed; does not fire here without
                                     cross-construction history (informational)
    """
    composite_rows = [c for c in categorized if c["query_type"] == "composite"]
    n_composite = len(composite_rows)
    if n_composite == 0:
        return {"outcome": OUTCOME_BUNDLE_INSUFFICIENT,
                "reason": "no composite generations present"}

    # Per-item: R1 base count → subtract R6-invalidated items.
    item_ids_R1_raw = [c["item_id"] for c in composite_rows
                       if c["category"] == R1_CORRECT_COMPOSITION]
    item_ids_R1_invalidated = [i for i in item_ids_R1_raw if i in invalidations]
    n_R1_raw = len(item_ids_R1_raw)
    n_R1_invalidated = len(item_ids_R1_invalidated)
    n_R1 = n_R1_raw - n_R1_invalidated
    R1_rate = n_R1 / n_composite

    # Category rates on composite.
    cat_counts = Counter(c["category"] for c in composite_rows)
    cat_rates  = {cat: cnt / n_composite for cat, cnt in cat_counts.items()}

    # 8.4 REJECTED if R6a fired anywhere (R8.1 breach).
    if any("R6a_terminal_coincidence" in v for v in invalidations.values()):
        return {
            "outcome": OUTCOME_REJECTED_CONSTRUCTION,
            "reason": "R6a (terminal coincidence) fired — R8.1 admissibility breach at scoring time.",
            "R1_rate": R1_rate,
            "category_rates": cat_rates,
        }

    # Failure-signature dominance check.
    dominant_signatures: list[str] = []
    for sig, cat in [
        ("R2_dominant_target_terminal_attraction", R2_TARGET_TERMINAL_GRAB),
        ("R4_dominant_cross_chain_salience",       R4_DECOY_TERMINAL_GRAB),
        ("R4b_dominant_depth_selection",           R4B_DEPTH_COMPETITOR_GRAB),
        ("R3_dominant_hop2_in_composition_failure", R3_STOPPED_SHORT),
        ("R5_dominant_abstention_regime",          R5_ABSTAIN),
    ]:
        if cat_rates.get(cat, 0.0) > DOMINANT_RATE_THRESHOLD:
            dominant_signatures.append(sig)

    # Cross-query constant-token prevalence check.
    constant_token_items = sum(1 for v in invalidations.values()
                               if "R6e_cross_query_constant_token" in v)
    constant_token_rate = constant_token_items / n_composite if n_composite else 0.0
    if constant_token_rate > DOMINANT_RATE_THRESHOLD:
        dominant_signatures.append("cross_query_constant_token_prevalent")

    F = floor_info["F"]
    threshold = floor_info["threshold"]

    # 8.3 FAIL: dominant signature OR R1 below threshold.
    if dominant_signatures:
        return {
            "outcome": OUTCOME_FAIL,
            "reason": f"failure signature(s) dominant: {dominant_signatures}",
            "R1_rate": R1_rate,
            "dominant_signatures": dominant_signatures,
            "category_rates": cat_rates,
        }
    if R1_rate < F:
        return {
            "outcome": OUTCOME_FAIL,
            "reason": f"R1 rate {R1_rate:.3f} below derived floor F = {F:.3f}",
            "R1_rate": R1_rate,
            "category_rates": cat_rates,
        }

    # 8.1 / 8.2: CERTIFY or INCONCLUSIVE.
    if R1_rate >= threshold:
        return {
            "outcome": OUTCOME_CERTIFY,
            "reason": f"R1 rate {R1_rate:.3f} ≥ threshold {threshold:.3f} (= F + margin); no failure signature dominant.",
            "R1_rate": R1_rate,
            "category_rates": cat_rates,
        }
    return {
        "outcome": OUTCOME_INCONCLUSIVE,
        "reason": f"R1 rate {R1_rate:.3f} in inconclusive band (F = {F:.3f} ≤ R1 < threshold = {threshold:.3f}).",
        "R1_rate": R1_rate,
        "category_rates": cat_rates,
    }


# ── Main evaluator ──────────────────────────────────────────────────────────
def evaluate(run_dir: Path) -> dict:
    spec_path = run_dir / "construction_spec.json"
    raw_path  = run_dir / "fp16_raw_outputs.json"

    if not (spec_path.exists() and raw_path.exists()):
        return {
            "evaluator_version": "0.3",
            "run_dir":           str(run_dir),
            "status":            OUTCOME_BUNDLE_INSUFFICIENT,
            "reason":            "construction_spec.json and/or fp16_raw_outputs.json missing.",
        }

    spec = json.loads(spec_path.read_text())
    raw_data = json.loads(raw_path.read_text())
    results = raw_data.get("results", [])

    target_C_star = spec["target"]["C_star"]
    target_B      = spec["target"]["B"]
    target_T      = spec["target"]["T"]
    decoy_terminals = {d["T_i"] for d in spec.get("decoy_chains", [])}
    depth_competitors_X = {c["X"] for c in spec.get("depth_2_competitors", [])}

    # Categorize every generation.
    categorized: list[dict] = []
    for r in results:
        token = extract_answer(r["raw_output"])
        category = classify_response(
            token, r["query_type"],
            target_C_star, target_B, target_T,
            decoy_terminals, depth_competitors_X,
        )
        categorized.append({**r, "extracted_token": token, "category": category})

    # Build per-item index and compute R6 invalidators.
    by_item = per_item_index(results)
    invalidations = invalidate_R1(by_item, spec)

    # Heuristic floor + threshold.
    floor_info = compute_floor(spec)

    # Outcome branch.
    outcome = derive_outcome(categorized, floor_info, invalidations, spec)

    # Per-query category counts.
    by_query: dict[str, dict[str, int]] = {}
    for c in categorized:
        qt = c["query_type"]
        by_query.setdefault(qt, Counter())[c["category"]] += 1
    by_query = {qt: dict(cnt) for qt, cnt in by_query.items()}

    # Computable vs judgment-flagged exclusions tag.
    computable_invalidators = ["R6a", "R6b", "R6c (empirical)", "R6d", "R6e", "R6f"]
    judgment_flagged = ["R6cat ambiguity adjudication (e.g., near-miss / typo'd C*)"]

    forbidden = [
        "Claim C progress",
        "Paper B activation",
        "general compression robustness",
        "certified baseline (the evaluator emits CERTIFY only when the run+gate clear it; it is not a certification of-record)",
        "task family viability",
        "model passed / capability established / not shortcut-driven",
        "product/funder-facing result",
        "mechanism / architecture / training-distribution claim",
        "depth-2 heuristic approximates traversal (E6 binding forbidden justification)",
    ]

    return {
        "evaluator_version":     "0.3",
        "run_dir":               str(run_dir),
        "status":                "EVALUATED",
        "construction_id":       spec.get("construction_id", "<unknown>"),
        "n_generations":         len(results),
        "n_items":               len(by_item),
        "per_query_category_counts": by_query,
        "R6_invalidations": {
            "by_item":                  invalidations,
            "n_items_invalidated":      len(invalidations),
        },
        "heuristic_floor":       floor_info,
        "outcome":               outcome,
        "computable_invalidators": computable_invalidators,
        "judgment_flagged":      judgment_flagged,
        "forbidden_interpretations": forbidden,
        "rule_sources": [
            "TARGET-CONSTRUCT-DEFINITION-v0.3 (sha eb72abb2…) §§2, 3, 8, 11",
            "PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3 (sha 38e05460…) §§2, 4, 7, 8",
            "G6 evaluator v0.2 (sha edfb6fec…) — Rule B (R6e) carried forward",
        ],
    }


def main() -> int:
    p = argparse.ArgumentParser(description="G6 Evaluator v0.3 (Path A multiclass).")
    p.add_argument("--run",      type=Path, required=True, help="run / fixture directory")
    p.add_argument("--output",   type=Path, required=True, help="output disposition JSON")
    p.add_argument("--expected", type=Path, default=None,  help="optional expected disposition")
    args = p.parse_args()

    result = evaluate(args.run)
    result["timestamp_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if args.expected and args.expected.exists():
        exp = json.loads(args.expected.read_text())
        exp_outcome = (exp.get("outcome") or {}).get("outcome") if isinstance(exp.get("outcome"), dict) else exp.get("outcome")
        emitted_outcome = (result.get("outcome") or {}).get("outcome") if isinstance(result.get("outcome"), dict) else result.get("outcome", result.get("status"))
        result["_expected_outcome"] = exp_outcome
        result["_emitted_outcome"]  = emitted_outcome
        result["_expected_match"]   = (emitted_outcome == exp_outcome)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")

    if result.get("status") == OUTCOME_BUNDLE_INSUFFICIENT:
        print(f"status: {result['status']} — {result.get('reason', '')}")
    else:
        oc = result.get("outcome", {})
        print(f"outcome: {oc.get('outcome')}")
        print(f"R1 rate: {oc.get('R1_rate', 'n/a')}")
        print(f"reason:  {oc.get('reason', '')}")
    if "_expected_match" in result:
        print(f"emitted == expected: {result['_expected_match']}")
    print(f"output: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
