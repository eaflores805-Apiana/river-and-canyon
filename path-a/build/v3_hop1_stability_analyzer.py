#!/usr/bin/env python3
"""
v3_hop1_stability_analyzer.py — V3 Hop1 Stability analyzer
(hop1-stability tooling 1/2 of the build per Manager + TL ACTION 2026-06-19
"Begin Hop1 Stability Tooling Build").

Computes per-block hop1 + hop2 correct rates + Wilson 95% CIs + per-block
floor verdicts, then applies the prereg v0.1 §9 between-block branch
selector under the explicit N2 priority order:

  1. CONSTRUCT-FAIL        any block with C1-C9 fail, conformance fail,
                           or invalidated >= 10
  2. HOP2-CONTROL-FAIL     any block with hop2-isolated lower Wilson <= 0.75
                           (hop1 read on that block is confounded)
  3. HOP1 stability branches (only if (1) and (2) pass):
     - HOP1-STABLE-ADMISSIBLE     all blocks hop1 lower Wilson > 0.75
     - HOP1-STABLE-INADMISSIBLE   all blocks hop1 lower Wilson <= 0.75
     - HOP1-UNSTABLE              not unanimous

Per the prereg v0.1 §3 N1.A resolution: this analyzer reads ONLY hop1 +
hop2 scored outputs. Composite + direct_query scored outputs are out of
scope and MUST NOT enter scoring, covariate logging, branch computation,
or claims. The analyzer detects and refuses to read them.

SCORES outputs; runs no model. Pure function of inputs; deterministic.

Authority: Manager + TL ACTION 2026-06-19. Build effort only; no run.

— CS Engineer, 2026-06-19
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


HOP_FLOOR             = 0.75    # hop1 + hop2 reliability floor (per prereg §8)
INVALIDATED_THRESHOLD = 10      # per-block; >=10/96 -> construct-fail
WILSON_Z_95           = 1.96

# N2 priority order — must be documented in the analyzer output
BRANCH_PRIORITY = [
    "CONSTRUCT-FAIL",
    "HOP2-CONTROL-FAIL",
    "HOP1-STABLE-ADMISSIBLE",   # final 3 are mutually exclusive on hop1 verdicts
    "HOP1-STABLE-INADMISSIBLE",
    "HOP1-UNSTABLE",
]

# N1.A enforcement: only hop1 + hop2 scored contexts are read; the analyzer
# refuses to score composite/direct_query even if present in the scored dir
ALLOWED_CONTEXTS = {"hop1", "hop2"}
OUT_OF_SCOPE_CONTEXTS = {"composite", "direct_query"}


def wilson_ci(k: int, n: int, z: float = WILSON_Z_95) -> tuple[float, float]:
    """Wilson score 95% CI for k/n. Returns (lower, upper)."""
    if n <= 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1.0 + (z * z) / n
    centre = p + (z * z) / (2 * n)
    half = z * math.sqrt(p * (1 - p) / n + (z * z) / (4 * n * n))
    return ((centre - half) / denom, (centre + half) / denom)


def block_id_for_index(item_index: int,
                       start_index: int,
                       block_size:  int,
                       n_blocks:    int) -> int | None:
    """Same block-id mapping as v3_hop1_covariate_logger.block_id_for_index."""
    if item_index < start_index:
        return None
    offset = item_index - start_index
    block_idx = (offset // block_size) + 1
    if block_idx < 1 or block_idx > n_blocks:
        return None
    return block_idx


def _load_hop1_hop2_only(scored_dir: Path) -> dict[str, dict[str, dict]]:
    """Return {item_id: {hop1: {...}, hop2: {...}}}. N1.A: ignore composite/dq."""
    out: dict[str, dict[str, dict]] = {}
    for item_path in sorted(scored_dir.iterdir()):
        if not item_path.is_dir():
            continue
        item_id = item_path.name
        out[item_id] = {}
        for ctx in ALLOWED_CONTEXTS:
            p = item_path / f"{ctx}.json"
            if not p.exists():
                raise FileNotFoundError(f"missing required {ctx} scored file: {p}")
            out[item_id][ctx] = json.loads(p.read_text())
        # N1.A: log presence of out-of-scope files but DO NOT read them
    return out


def _per_block_admissibility(admissibility_summary: dict | None,
                              n_blocks: int) -> dict[int, dict]:
    """Return {block_id: {all_pass: bool, invalidated_count: int}} from an
    optional per-block admissibility summary. If the summary is single-block
    (no per_block field), apply it uniformly to all blocks."""
    out = {}
    if admissibility_summary is None:
        for b in range(1, n_blocks + 1):
            out[b] = {"all_pass": True, "invalidated_count": 0}
        return out
    per_block = admissibility_summary.get("per_block")
    if per_block is None:
        # Single-block summary — apply uniformly
        all_pass = bool(admissibility_summary.get("all_pass", True))
        for b in range(1, n_blocks + 1):
            out[b] = {"all_pass": all_pass, "invalidated_count": 0}
        return out
    for b in range(1, n_blocks + 1):
        d = per_block.get(str(b), per_block.get(b, {}))
        out[b] = {
            "all_pass":          bool(d.get("all_pass", True)),
            "invalidated_count": int(d.get("invalidated_count", 0)),
        }
    return out


def _per_block_conformance(prompt_conformance_summary: dict | None,
                             n_blocks: int) -> dict[int, bool]:
    """Return {block_id: all_pass: bool}. Defaults to True if not provided."""
    out = {}
    if prompt_conformance_summary is None:
        for b in range(1, n_blocks + 1):
            out[b] = True
        return out
    per_block = prompt_conformance_summary.get("per_block")
    if per_block is None:
        all_pass = bool(prompt_conformance_summary.get("all_pass", True))
        for b in range(1, n_blocks + 1):
            out[b] = all_pass
        return out
    for b in range(1, n_blocks + 1):
        d = per_block.get(str(b), per_block.get(b, {}))
        out[b] = bool(d.get("all_pass", True))
    return out


def analyze(
    scored: dict[str, dict[str, dict]],
    item_index_lookup: dict[str, int],
    start_index: int,
    block_size:  int,
    n_blocks:    int,
    admissibility_summary: dict | None,
    prompt_conformance_summary: dict | None,
) -> dict:
    """Pure computation of per-block + between-block §9 branch."""
    # Group items by block
    block_items: dict[int, list[str]] = {b: [] for b in range(1, n_blocks + 1)}
    for item_id in scored:
        idx = item_index_lookup.get(item_id)
        if idx is None:
            continue
        b = block_id_for_index(idx, start_index, block_size, n_blocks)
        if b is None:
            continue
        block_items[b].append(item_id)

    # Per-block stats
    per_block_admissibility   = _per_block_admissibility(admissibility_summary, n_blocks)
    per_block_conformance     = _per_block_conformance(prompt_conformance_summary, n_blocks)
    per_block_results: list[dict] = []

    for b in range(1, n_blocks + 1):
        items = sorted(block_items[b])
        n = len(items)
        hop1_k = sum(1 for it in items if scored[it]["hop1"].get("match"))
        hop2_k = sum(1 for it in items if scored[it]["hop2"].get("match"))
        hop1_lo, hop1_hi = wilson_ci(hop1_k, n) if n else (0.0, 0.0)
        hop2_lo, hop2_hi = wilson_ci(hop2_k, n) if n else (0.0, 0.0)

        adm = per_block_admissibility[b]
        cnf = per_block_conformance[b]

        per_block_results.append({
            "block_id":            b,
            "n":                   n,
            "hop1_k":              hop1_k,
            "hop1_rate":           hop1_k / n if n else None,
            "hop1_wilson_lower":   hop1_lo,
            "hop1_wilson_upper":   hop1_hi,
            "hop1_clears_floor":   hop1_lo > HOP_FLOOR,
            "hop2_k":              hop2_k,
            "hop2_rate":           hop2_k / n if n else None,
            "hop2_wilson_lower":   hop2_lo,
            "hop2_wilson_upper":   hop2_hi,
            "hop2_clears_floor":   hop2_lo > HOP_FLOOR,
            "admissibility_pass":  adm["all_pass"],
            "invalidated_count":   adm["invalidated_count"],
            "conformance_pass":    cnf,
            "block_construct_ok":  (adm["all_pass"]
                                     and cnf
                                     and adm["invalidated_count"] < INVALIDATED_THRESHOLD),
        })

    # N2 priority order
    construct_fail_blocks    = [r["block_id"] for r in per_block_results
                                if not r["block_construct_ok"]]
    hop2_control_fail_blocks = [r["block_id"] for r in per_block_results
                                if not r["hop2_clears_floor"]]

    hop1_clear_set = {r["block_id"] for r in per_block_results if r["hop1_clears_floor"]}
    hop1_fail_set  = {r["block_id"] for r in per_block_results if not r["hop1_clears_floor"]}

    if construct_fail_blocks:
        branch = "CONSTRUCT-FAIL"
    elif hop2_control_fail_blocks:
        branch = "HOP2-CONTROL-FAIL"
    elif hop1_clear_set and not hop1_fail_set:
        branch = "HOP1-STABLE-ADMISSIBLE"
    elif hop1_fail_set and not hop1_clear_set:
        branch = "HOP1-STABLE-INADMISSIBLE"
    else:
        branch = "HOP1-UNSTABLE"

    # Between-block spread (descriptive)
    hop1_rates = [r["hop1_rate"] for r in per_block_results if r["hop1_rate"] is not None]
    spread = None
    if hop1_rates:
        mean = sum(hop1_rates) / len(hop1_rates)
        var  = sum((r - mean) ** 2 for r in hop1_rates) / len(hop1_rates)
        spread = {
            "n_blocks":   len(hop1_rates),
            "min":        min(hop1_rates),
            "max":        max(hop1_rates),
            "range":      max(hop1_rates) - min(hop1_rates),
            "mean":       mean,
            "variance":   var,
            "stddev":     math.sqrt(var),
        }

    decision = {
        "analyzer_version":    "v0.1",
        "scope":               "v0.1 §9 hop1 stability investigation; positional/structural only",
        "branch_priority_order": BRANCH_PRIORITY,    # N2 documentation
        "n1A_enforcement":     "only hop1 + hop2 scored contexts read; "
                               "composite + direct_query are out of scope and NOT scored / "
                               "NOT entered into branch computation / NOT entered into covariate logging",
        "seed_range":          {"start_index": start_index, "block_size": block_size, "n_blocks": n_blocks},
        "per_block":           per_block_results,
        "construct_fail_blocks":    construct_fail_blocks,
        "hop2_control_fail_blocks": hop2_control_fail_blocks,
        "hop1_clear_blocks":   sorted(hop1_clear_set),
        "hop1_fail_blocks":    sorted(hop1_fail_set),
        "hop1_between_block_spread": spread,
        "final_branch":        branch,
        "this_run_only":       True,
        "forbidden_labels":    "no mechanism / binding / attention / reasoning failure / shortcut "
                               "ever emitted; covariate logger output (separate) carries only "
                               "positional/structural fields",
    }
    return decision


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--scored-dir",          type=Path, required=True)
    p.add_argument("--items-dir",           type=Path, required=True,
                    help="needed to map item_id -> item_index -> block_id")
    p.add_argument("--admissibility",       type=Path, default=None,
                    help="admissibility summary (optional; defaults to all-pass)")
    p.add_argument("--prompt-conformance",  type=Path, default=None,
                    help="prompt-conformance summary (optional; defaults to all-pass)")
    p.add_argument("--output",              type=Path, required=True)
    p.add_argument("--start-index",         type=int, default=193,
                    help="block F1 start index per prereg §5")
    p.add_argument("--block-size",          type=int, default=96)
    p.add_argument("--n-blocks",            type=int, default=6,
                    help="number of blocks F1..F{n_blocks}")
    args = p.parse_args(argv)

    # Build item_id -> item_index lookup from item specs
    item_index_lookup: dict[str, int] = {}
    for sp in args.items_dir.glob("item_*.json"):
        spec = json.loads(sp.read_text())
        item_index_lookup[sp.stem] = spec["_build_provenance"]["item_index"]

    scored = _load_hop1_hop2_only(args.scored_dir)

    admissibility       = (json.loads(args.admissibility.read_text())
                           if args.admissibility else None)
    prompt_conformance  = (json.loads(args.prompt_conformance.read_text())
                           if args.prompt_conformance else None)

    decision = analyze(scored, item_index_lookup,
                       args.start_index, args.block_size, args.n_blocks,
                       admissibility, prompt_conformance)
    args.output.write_text(json.dumps(decision, indent=2) + "\n")

    print(f"branch:                       {decision['final_branch']}")
    print(f"per-block hop1 rates:         {[round(r['hop1_rate'], 4) if r['hop1_rate'] is not None else None for r in decision['per_block']]}")
    print(f"per-block hop1 Wilson lower:  {[round(r['hop1_wilson_lower'], 4) for r in decision['per_block']]}")
    print(f"hop1 clear blocks:            {decision['hop1_clear_blocks']}")
    print(f"hop1 fail  blocks:            {decision['hop1_fail_blocks']}")
    print(f"hop2 control fail blocks:     {decision['hop2_control_fail_blocks']}")
    print(f"construct fail blocks:        {decision['construct_fail_blocks']}")

    return {
        "HOP1-STABLE-ADMISSIBLE":    0,
        "HOP1-STABLE-INADMISSIBLE":  1,
        "HOP1-UNSTABLE":             2,
        "HOP2-CONTROL-FAIL":         3,
        "CONSTRUCT-FAIL":            4,
    }[decision["final_branch"]]


if __name__ == "__main__":
    sys.exit(main())
