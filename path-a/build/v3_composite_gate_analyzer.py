#!/usr/bin/env python3
"""
v3_composite_gate_analyzer.py — V3 Composite Gate analyzer (composite-gate
tooling 1/3 of the composite-gate build per Manager + TL ACTION 2026-06-18
"Begin V3 Composite Gate Tooling Build").

Deterministically computes the composite-gate decision per
PREREGISTRATION-V3-COMPOSITE-GATE-v0.2 §7 / §8 from:
  - per-context scored model outputs (composite/hop1/hop2/direct_query)
  - the R6 invalidation log
  - the inspector admissibility summary (C1-C9 96/96)
  - the prompt-conformance summary (P1-P10 + §9(vi))
  - the composite error-structure log (from v3_composite_error_logger.py)

SCORES outputs; runs no model. Pure function of inputs; deterministic.

§7 GATE-CLEARED-THIS-RUN requires ALL of:
  (a) composite-correct lower Wilson 95% > 0.75   (primary reliability gate)
  (b) composite-correct lower Wilson 95% > 0.45   (necessary not-shortcut floor)
  (c) preconditions hold on the fresh set (hop2 admissible, hop1 admissible,
       dq C* count <= 19/96)
  (d) construct clean (C1-C9 96/96, prompt-conformance 96/96, invalidated <= 9/96)
  (e) error-structure non-pathological (no composition_specific successes per
       the error logger's pathological flag)

§8 branches:
  GATE-CLEARED-THIS-RUN              (a) AND (b) AND (c) AND (d) AND (e)
  COMPOSITE-DOES-NOT-CLEAR-THIS-RUN  (c) AND (d) AND (e) hold, (a) and/or (b) fail
                                     (sub-message records 0.45 < lower-Wilson <= 0.75:
                                      "not explained by foreclosed shortcuts,
                                       but not reliably composing")
  PRECONDITION-FAIL                  (c) fails: hop2/hop1 below floor or dq >= 20/96
                                     (gate is NOT read)
  CONSTRUCT-FAIL                     (d) or (e) fails: invalidated >= 10/96, OR
                                     C1-C9 fail, OR conformance fail, OR pathological

THIS-RUN vs FINAL: this analyzer emits GATE-CLEARED-THIS-RUN at most. FINAL
certification is a SEPARATE Manager/standard decision per v0.2 §7.

— CS Engineer, 2026-06-18
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


# Locked thresholds (v0.2 §7)
HOP_FLOOR                = 0.75   # hop1, hop2 reliability floor
DQ_POINT_CEILING_COUNT   = 19     # ≤19 passes; ≥20 fails (direct-recall)
INVALIDATED_THRESHOLD    = 10     # ≥10 = set-level construct-fail (≤9 tolerated)
COMPOSITE_PRIMARY_GATE   = 0.75   # composite-correct lower Wilson 95% > 0.75
COMPOSITE_FLOOR_GATE     = 0.45   # composite-correct lower Wilson 95% > 0.45 (F + margin)
WILSON_Z_95              = 1.96

# v0.2 §8 item-level invalidators (the five non-circular ones)
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
    """All R6 invalidator names must be from the locked set per v0.2 §8."""
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
    error_log: dict,
) -> dict:
    """Pure computation of §7 conditions + §8 branch."""
    _validate_r6_log(r6_log)

    all_items = sorted(scored.keys())
    excluded = sorted(item for item in all_items if r6_log.get(item))
    included = [item for item in all_items if item not in excluded]

    n_total    = len(all_items)
    n_excluded = len(excluded)
    n_included = len(included)

    # composite-correct rate on the post-exclusion denominator
    composite_k = sum(1 for item in included if scored[item]["composite"].get("match"))
    composite_lo, composite_hi = (
        wilson_ci(composite_k, n_included) if n_included > 0 else (0.0, 0.0)
    )

    # hop2 + hop1 + dq on the post-exclusion denominator
    hop2_k = sum(1 for item in included if scored[item]["hop2"].get("match"))
    hop1_k = sum(1 for item in included if scored[item]["hop1"].get("match"))
    dq_k   = sum(1 for item in included if scored[item]["direct_query"].get("match"))

    hop2_lo, hop2_hi = wilson_ci(hop2_k, n_included) if n_included > 0 else (0.0, 0.0)
    hop1_lo, hop1_hi = wilson_ci(hop1_k, n_included) if n_included > 0 else (0.0, 0.0)

    # §7 condition checks (a)-(e)
    cond_a = composite_lo > COMPOSITE_PRIMARY_GATE
    cond_b = composite_lo > COMPOSITE_FLOOR_GATE
    cond_c_hop2 = hop2_lo > HOP_FLOOR
    cond_c_hop1 = hop1_lo > HOP_FLOOR
    cond_c_dq   = dq_k <= DQ_POINT_CEILING_COUNT
    cond_c      = cond_c_hop2 and cond_c_hop1 and cond_c_dq
    cond_d_admissibility = bool(admissibility.get("all_pass"))
    cond_d_conformance   = bool(prompt_conformance.get("all_pass"))
    cond_d_invalidated   = n_excluded < INVALIDATED_THRESHOLD
    cond_d = cond_d_admissibility and cond_d_conformance and cond_d_invalidated
    cond_e = not bool(error_log.get("pathological_error_structure", False))

    # §8 branch selection
    if not cond_c:
        branch = "PRECONDITION-FAIL"
    elif not cond_d or not cond_e:
        branch = "CONSTRUCT-FAIL"
    elif cond_a and cond_b:
        branch = "GATE-CLEARED-THIS-RUN"
    else:
        # cond_c + cond_d + cond_e hold; gate (a) and/or (b) fail
        branch = "COMPOSITE-DOES-NOT-CLEAR-THIS-RUN"

    # Sub-message for the "not explained by foreclosed shortcuts" case
    submessage = None
    if branch == "COMPOSITE-DOES-NOT-CLEAR-THIS-RUN":
        if cond_b and not cond_a:
            submessage = ("not explained by foreclosed shortcuts, but not reliably "
                          "composing (cleared 0.45 floor; did not clear 0.75 reliability gate)")
        elif not cond_b:
            submessage = "composite below the not-shortcut floor (0.45)"

    # min-count thresholds for hop2/hop1/composite at the post-exclusion N
    def _min_clearing_count(n: int, threshold: float) -> int | None:
        if n <= 0:
            return None
        for k in range(n + 1):
            lo, _ = wilson_ci(k, n)
            if lo > threshold:
                return k
        return None

    decision = {
        "analyzer_version": "v0.1",
        "scope":            "composite-gate analysis; NOT certification",
        "this_run_only":    True,
        "final_separate":   "FINAL certification is a separate Manager/standard decision per v0.2 §7",
        "n_total":          n_total,
        "n_excluded":       n_excluded,
        "n_included":       n_included,
        "excluded_items":   excluded,
        "composite": {
            "k":                  composite_k,
            "n":                  n_included,
            "rate":               composite_k / n_included if n_included else None,
            "wilson_lower_95":    composite_lo,
            "wilson_upper_95":    composite_hi,
            "primary_gate":       COMPOSITE_PRIMARY_GATE,
            "floor_gate":         COMPOSITE_FLOOR_GATE,
            "min_clearing_count_primary": _min_clearing_count(n_included, COMPOSITE_PRIMARY_GATE),
            "min_clearing_count_floor":   _min_clearing_count(n_included, COMPOSITE_FLOOR_GATE),
            "condition_a_pass":   cond_a,
            "condition_b_pass":   cond_b,
        },
        "hop2": {
            "k": hop2_k, "n": n_included,
            "rate": hop2_k / n_included if n_included else None,
            "wilson_lower_95":    hop2_lo, "wilson_upper_95": hop2_hi,
            "floor":              HOP_FLOOR,
            "min_clearing_count": _min_clearing_count(n_included, HOP_FLOOR),
            "precondition_pass":  cond_c_hop2,
        },
        "hop1": {
            "k": hop1_k, "n": n_included,
            "rate": hop1_k / n_included if n_included else None,
            "wilson_lower_95":    hop1_lo, "wilson_upper_95": hop1_hi,
            "floor":              HOP_FLOOR,
            "min_clearing_count": _min_clearing_count(n_included, HOP_FLOOR),
            "precondition_pass":  cond_c_hop1,
        },
        "direct_query": {
            "k":                   dq_k,
            "ceiling_count":       DQ_POINT_CEILING_COUNT,
            "precondition_pass":   cond_c_dq,
        },
        "invalidated": {
            "count":              n_excluded,
            "threshold":          INVALIDATED_THRESHOLD,
            "construct_pass":     cond_d_invalidated,
        },
        "admissibility": {
            "all_pass":           cond_d_admissibility,
            "construct_pass":     cond_d_admissibility,
        },
        "prompt_conformance": {
            "all_pass":           cond_d_conformance,
            "construct_pass":     cond_d_conformance,
        },
        "error_structure": {
            "pathological":       not cond_e,
            "construct_pass":     cond_e,
            "error_log_summary":  error_log.get("summary", {}),
        },
        "conditions": {
            "(a)_composite_wilson_gt_primary":  cond_a,
            "(b)_composite_wilson_gt_floor":    cond_b,
            "(c)_preconditions_pass":            cond_c,
            "(d)_construct_clean":               cond_d,
            "(e)_error_structure_non_pathological": cond_e,
        },
        "final_branch":           branch,
        "submessage":             submessage,
    }
    return decision


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--scored-dir",         type=Path, required=True)
    p.add_argument("--r6-log",             type=Path, required=True)
    p.add_argument("--admissibility",      type=Path, required=True)
    p.add_argument("--prompt-conformance", type=Path, required=True)
    p.add_argument("--error-log",          type=Path, required=True)
    p.add_argument("--output",             type=Path, required=True)
    args = p.parse_args(argv)

    scored             = _load_scored(args.scored_dir)
    r6_log             = json.loads(args.r6_log.read_text())
    admissibility      = json.loads(args.admissibility.read_text())
    prompt_conformance = json.loads(args.prompt_conformance.read_text())
    error_log          = json.loads(args.error_log.read_text())

    decision = analyze(scored, r6_log, admissibility, prompt_conformance, error_log)
    args.output.write_text(json.dumps(decision, indent=2) + "\n")

    print(f"branch:               {decision['final_branch']}")
    if decision['submessage']:
        print(f"submessage:           {decision['submessage']}")
    print(f"n_total / n_included: {decision['n_total']} / {decision['n_included']}")
    print(f"composite k/n:        {decision['composite']['k']} / {decision['composite']['n']}  "
          f"Wilson lower {decision['composite']['wilson_lower_95']:.4f}  "
          f"primary {COMPOSITE_PRIMARY_GATE}  floor {COMPOSITE_FLOOR_GATE}")
    print(f"hop2 / hop1:          {decision['hop2']['k']}/{decision['hop2']['n']}  "
          f"/ {decision['hop1']['k']}/{decision['hop1']['n']}")
    print(f"dq count:             {decision['direct_query']['k']} (ceiling {DQ_POINT_CEILING_COUNT})")
    print(f"invalidated:          {decision['invalidated']['count']} (threshold {INVALIDATED_THRESHOLD})")
    print(f"error_structure:      {'PATHOLOGICAL' if decision['error_structure']['pathological'] else 'OK'}")

    return {
        "GATE-CLEARED-THIS-RUN":              0,
        "COMPOSITE-DOES-NOT-CLEAR-THIS-RUN":  1,
        "PRECONDITION-FAIL":                  2,
        "CONSTRUCT-FAIL":                     3,
    }[decision["final_branch"]]


if __name__ == "__main__":
    sys.exit(main())
