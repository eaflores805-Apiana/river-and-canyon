#!/usr/bin/env python3
"""
v3_floor_check_analyzer.py — V3 floor-check analyzer (floor-check tooling 1/4).

Deterministically computes the floor-check metrics and the §9/§10 final branch
from per-context scored model outputs, the R6 invalidation log, the inspector
admissibility results, and the prompt-conformance gate.

Per v0.4 §T (1): SCORES outputs; runs no model. Pure function of inputs.

Inputs (CLI):
  --scored-dir       directory of per-item per-context scored JSON files:
                       <scored-dir>/<item>/<context>.json   for ctx in
                       {composite, hop1, hop2, direct_query}
                     each JSON: {item: str, context: str, ground_truth: str,
                                  predicted: str, match: bool}
  --r6-log           path to R6 invalidation log JSON:
                       {<item>: [list of invalidator names], ...}
                     valid invalidator names are the FIVE non-circular
                     item-level invalidators per v0.4 §8: terminal_coincidence,
                     controls_unavailable, direct_recall, interior_position,
                     constant_token.
  --admissibility    path to JSON summary of C1–C9 inspector results across N:
                       {all_pass: bool, n_pass: int, n_total: int, ...}
  --prompt-conformance path to prompt_conformance_summary.json (from the checker)

Output:
  --output           path to write the analyzer decision JSON

Authority: Manager + TL ACTION 2026-06-18. Build effort only; no run.

§9 conditions:
  (i)   hop2 lower Wilson 95% bound > 0.75
  (ii)  direct_query C* count ≤ 19/96
  (iii) hop1 lower Wilson 95% bound > 0.75
  (iv)  invalidated item count ≤ 9/96
  (v)   C1–C9 admissibility PASS for all materialized items
  (vi)  prompt-realization conformance PASS

§10 branches:
  COMPONENT-ADMISSIBLE-UNDER-COMPETITION    all (i)-(vi) PASS
  ONE-RUN-EVIDENCE-TOWARD-SUBSTRATE-INFEASIBILITY
                                            (i) FAIL while (ii)-(vi) PASS
                                            (clean executable construct)
  CONSTRUCT-FAIL                            (iv'≥10/96) OR (dq≥20/96) OR
                                            hop1 below floor OR admissibility
                                            fail OR conformance fail
  (FINAL-substrate-infeasibility is explicitly OUT OF SCOPE for a single run
  and is computed across multiple admissible runs by a future aggregator.)

— CS Engineer, 2026-06-18
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


# Locked thresholds (v0.4 §6 + §9)
HOP_FLOOR                  = 0.75
DQ_POINT_CEILING_COUNT     = 19    # ≤19 passes; ≥20 fails
INVALIDATED_THRESHOLD      = 10    # ≥10 is set-level construct-fail (≤9 tolerated)
WILSON_Z_95                = 1.96  # two-sided 95% CI

# v0.4 §8 item-level invalidators (the five non-circular ones)
LOCKED_R6_INVALIDATORS = {
    "terminal_coincidence",
    "controls_unavailable",
    "direct_recall",
    "interior_position",
    "constant_token",
}


def wilson_ci(k: int, n: int, z: float = WILSON_Z_95) -> tuple[float, float]:
    """Wilson score 95% CI for k successes in n trials. Returns (lower, upper)."""
    if n <= 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1.0 + (z * z) / n
    centre = p + (z * z) / (2 * n)
    half = z * math.sqrt(p * (1 - p) / n + (z * z) / (4 * n * n))
    return ((centre - half) / denom, (centre + half) / denom)


def _load_scored(scored_dir: Path) -> dict[str, dict[str, dict]]:
    """Return {item_id: {context: scored_json}}."""
    out: dict[str, dict[str, dict]] = {}
    for item_path in sorted(scored_dir.iterdir()):
        if not item_path.is_dir():
            continue
        item_id = item_path.name
        out[item_id] = {}
        for ctx in ("composite", "hop1", "hop2", "direct_query"):
            p = item_path / f"{ctx}.json"
            if not p.exists():
                raise FileNotFoundError(f"missing scored file: {p}")
            out[item_id][ctx] = json.loads(p.read_text())
    return out


def _validate_r6_log(r6_log: dict) -> None:
    """All R6 invalidator names must be from the locked set per v0.4 §8."""
    for item, invs in r6_log.items():
        if not isinstance(invs, list):
            raise ValueError(f"r6 log entry for {item!r} is not a list: {invs!r}")
        for inv in invs:
            if inv not in LOCKED_R6_INVALIDATORS:
                raise ValueError(
                    f"unknown R6 invalidator {inv!r} on item {item!r}; "
                    f"valid set is {sorted(LOCKED_R6_INVALIDATORS)}"
                )


def analyze(
    scored: dict[str, dict[str, dict]],
    r6_log: dict[str, list[str]],
    admissibility: dict,
    prompt_conformance: dict,
) -> dict:
    """Pure computation of §9 conditions + §10 branch."""
    _validate_r6_log(r6_log)

    all_items = sorted(scored.keys())
    # Item-level exclusions: any item with ≥1 R6 invalidator is excluded from
    # the relevant validated numerator/denominator per v0.4 §8
    excluded = sorted(item for item in all_items if r6_log.get(item))
    included = [item for item in all_items if item not in excluded]

    n_total       = len(all_items)
    n_excluded    = len(excluded)
    n_included    = len(included)

    # hop2-isolated rate on the post-exclusion denominator
    hop2_k = sum(1 for item in included if scored[item]["hop2"].get("match"))
    hop2_lo, hop2_hi = wilson_ci(hop2_k, n_included) if n_included > 0 else (0.0, 0.0)

    # hop1-isolated rate on the post-exclusion denominator
    hop1_k = sum(1 for item in included if scored[item]["hop1"].get("match"))
    hop1_lo, hop1_hi = wilson_ci(hop1_k, n_included) if n_included > 0 else (0.0, 0.0)

    # direct-query C* count: # included items whose dq prediction == C* (i.e., match=True
    # means the model produced C* despite the bridge being withheld → direct-recall signal)
    dq_count = sum(1 for item in included if scored[item]["direct_query"].get("match"))

    # §9 conditions
    cond_i   = hop2_lo > HOP_FLOOR
    cond_ii  = dq_count <= DQ_POINT_CEILING_COUNT
    cond_iii = hop1_lo > HOP_FLOOR
    cond_iv  = n_excluded < INVALIDATED_THRESHOLD  # ≤9 tolerated; ≥10 fails
    cond_v   = bool(admissibility.get("all_pass"))
    cond_vi  = bool(prompt_conformance.get("all_pass"))

    # §10 branch selection
    clean_executable = cond_ii and cond_iii and cond_iv and cond_v and cond_vi
    if clean_executable and cond_i:
        branch = "COMPONENT-ADMISSIBLE-UNDER-COMPETITION"
    elif clean_executable and not cond_i:
        branch = "ONE-RUN-EVIDENCE-TOWARD-SUBSTRATE-INFEASIBILITY"
    else:
        branch = "CONSTRUCT-FAIL"

    # Compute the minimum count that would clear the floor on the post-exclusion
    # denominator (informational, per v0.4 §E4)
    def _min_clearing_count(n: int) -> int | None:
        if n <= 0:
            return None
        # Find smallest k such that wilson_lower(k, n) > HOP_FLOOR
        for k in range(n + 1):
            lo, _ = wilson_ci(k, n)
            if lo > HOP_FLOOR:
                return k
        return None  # impossible at this n

    min_count = _min_clearing_count(n_included)

    decision = {
        "analyzer_version": "v0.1",
        "scope":            "build-realization only; not run-authorized",
        "n_total":          n_total,
        "n_excluded":       n_excluded,
        "n_included":       n_included,
        "excluded_items":   excluded,
        "hop2": {
            "k":                  hop2_k,
            "n":                  n_included,
            "rate":               hop2_k / n_included if n_included else None,
            "wilson_lower_95":    hop2_lo,
            "wilson_upper_95":    hop2_hi,
            "floor":              HOP_FLOOR,
            "min_clearing_count": min_count,
            "condition_i_pass":   cond_i,
        },
        "hop1": {
            "k":                  hop1_k,
            "n":                  n_included,
            "rate":               hop1_k / n_included if n_included else None,
            "wilson_lower_95":    hop1_lo,
            "wilson_upper_95":    hop1_hi,
            "floor":              HOP_FLOOR,
            "min_clearing_count": min_count,
            "condition_iii_pass": cond_iii,
        },
        "direct_query": {
            "count":                dq_count,
            "ceiling_count":        DQ_POINT_CEILING_COUNT,
            "condition_ii_pass":    cond_ii,
        },
        "invalidated": {
            "count":                n_excluded,
            "threshold":            INVALIDATED_THRESHOLD,
            "condition_iv_pass":    cond_iv,
        },
        "admissibility": {
            "all_pass":             cond_v,
            "condition_v_pass":     cond_v,
        },
        "prompt_conformance": {
            "all_pass":             cond_vi,
            "condition_vi_pass":    cond_vi,
        },
        "conditions": {
            "(i)_hop2_wilson_gt_floor":      cond_i,
            "(ii)_dq_count_le_ceiling":      cond_ii,
            "(iii)_hop1_wilson_gt_floor":    cond_iii,
            "(iv)_invalidated_lt_threshold": cond_iv,
            "(v)_admissibility_pass":        cond_v,
            "(vi)_conformance_pass":         cond_vi,
        },
        "clean_executable_construct": clean_executable,
        "final_branch":              branch,
    }
    return decision


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--scored-dir",         type=Path, required=True)
    p.add_argument("--r6-log",             type=Path, required=True)
    p.add_argument("--admissibility",      type=Path, required=True)
    p.add_argument("--prompt-conformance", type=Path, required=True)
    p.add_argument("--output",             type=Path, required=True)
    args = p.parse_args(argv)

    scored             = _load_scored(args.scored_dir)
    r6_log             = json.loads(args.r6_log.read_text())
    admissibility      = json.loads(args.admissibility.read_text())
    prompt_conformance = json.loads(args.prompt_conformance.read_text())

    decision = analyze(scored, r6_log, admissibility, prompt_conformance)
    args.output.write_text(json.dumps(decision, indent=2) + "\n")

    print(f"branch:               {decision['final_branch']}")
    print(f"n_total / n_included: {decision['n_total']} / {decision['n_included']}")
    print(f"hop2 k/n:             {decision['hop2']['k']} / {decision['hop2']['n']}  "
          f"Wilson lower {decision['hop2']['wilson_lower_95']:.4f}  "
          f"(floor {decision['hop2']['floor']})  "
          f"{'CLEARS' if decision['hop2']['condition_i_pass'] else 'fails'}")
    print(f"hop1 k/n:             {decision['hop1']['k']} / {decision['hop1']['n']}  "
          f"Wilson lower {decision['hop1']['wilson_lower_95']:.4f}  "
          f"{'CLEARS' if decision['hop1']['condition_iii_pass'] else 'fails'}")
    print(f"dq count:             {decision['direct_query']['count']} (ceiling {DQ_POINT_CEILING_COUNT})  "
          f"{'PASSES' if decision['direct_query']['condition_ii_pass'] else 'fails'}")
    print(f"invalidated:          {decision['invalidated']['count']} (threshold {INVALIDATED_THRESHOLD})  "
          f"{'tolerated' if decision['invalidated']['condition_iv_pass'] else 'CONSTRUCT-FAIL'}")
    return {
        "COMPONENT-ADMISSIBLE-UNDER-COMPETITION":          0,
        "ONE-RUN-EVIDENCE-TOWARD-SUBSTRATE-INFEASIBILITY": 1,
        "CONSTRUCT-FAIL":                                  2,
    }[decision["final_branch"]]


if __name__ == "__main__":
    sys.exit(main())
