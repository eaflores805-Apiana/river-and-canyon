#!/usr/bin/env python3
"""
build_r6_log.py — Build the R6 invalidation log from step-6 scored outputs.

Per v0.4 §8 LOCKED_R6_INVALIDATORS:
  {terminal_coincidence, controls_unavailable, direct_recall,
   interior_position, constant_token}

This script honestly computes the two invalidators that are mechanically
determinable from the scored outputs + item specs alone:

  direct_recall:   fires on item N iff scored[N]["direct_query"].match == True
                   (model produced C* despite bridge fact withheld → direct-recall
                   shortcut; per v0.4 §6/§8 also gated set-level by dq ≤ 19/96
                   ceiling, but per v0.4 §8 the item-level invalidator excludes the
                   item from the relevant validated numerator)

  constant_token:  fires on item N iff all 4 contexts emitted the SAME predicted
                   token AND that token is NOT equal to any of the locked ground
                   truths (so it's a uniform wrong response — a fixed-token
                   shortcut across queries per v0.4 §8 / R6e cross-query invariant)

The other three invalidators (terminal_coincidence, controls_unavailable,
interior_position) are NOT fired by this script because they require deeper
diagnostic analysis that this scored-output snapshot alone does not provide
cleanly (e.g., interior_position requires per-item layout-position evidence;
terminal_coincidence overlaps with admissibility which is already gated at
the inspector C1 layer; controls_unavailable depends on hop1/hop2 retrieval
failure which is captured in §9 conditions iii directly).

Honest reporting: empty list for items where neither direct_recall nor
constant_token fires.

— CS Engineer, 2026-06-18
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


CONTEXTS = ("composite", "hop1", "hop2", "direct_query")


def build_r6_log(scored_dir: Path, items_dir: Path) -> dict[str, list[str]]:
    r6 = {}
    items = sorted(scored_dir.iterdir(), key=lambda p: p.name)
    for item_path in items:
        if not item_path.is_dir():
            continue
        item_id = item_path.name

        # Read the 4 scored contexts + the matching spec for ground-truth set
        scored = {}
        for ctx in CONTEXTS:
            scored[ctx] = json.loads((item_path / f"{ctx}.json").read_text())
        spec = json.loads((items_dir / f"{item_id}.json").read_text())

        invs: list[str] = []

        # direct_recall
        if scored["direct_query"]["match"] is True:
            invs.append("direct_recall")

        # constant_token
        predictions = {ctx: scored[ctx]["predicted"] for ctx in CONTEXTS}
        all_same = len(set(predictions.values())) == 1
        if all_same:
            constant_value = list(predictions.values())[0]
            ground_truths = {scored[ctx]["ground_truth"] for ctx in CONTEXTS}
            if constant_value not in ground_truths:
                invs.append("constant_token")

        r6[item_id] = invs
    return r6


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--scored-dir", type=Path, required=True)
    p.add_argument("--items-dir",  type=Path, required=True)
    p.add_argument("--output",     type=Path, required=True)
    args = p.parse_args(argv)

    r6 = build_r6_log(args.scored_dir, args.items_dir)
    args.output.write_text(json.dumps(r6, indent=2) + "\n")

    n_total            = len(r6)
    n_with_any         = sum(1 for invs in r6.values() if invs)
    n_direct_recall    = sum(1 for invs in r6.values() if "direct_recall" in invs)
    n_constant_token   = sum(1 for invs in r6.values() if "constant_token" in invs)

    print(f"r6_log written: {args.output}")
    print(f"  n items:           {n_total}")
    print(f"  items with any R6: {n_with_any}")
    print(f"  direct_recall:     {n_direct_recall}")
    print(f"  constant_token:    {n_constant_token}")
    print(f"  (other invalidators: not mechanically determinable from this snapshot)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
