#!/usr/bin/env python3
"""
v3_composite_error_logger.py — V3 Composite-error structure logger.

Produces the §9 same-error / wrong-address characterization required by
PREREGISTRATION-V3-COMPOSITE-GATE-v0.2:

For every composite ERROR (and successes too, for the pathological check), logs:
  WHERE THE OUTPUT TOKEN LANDS (positional / structural — NOT mechanism):
    correct_chain_wrong_depth   predicted ∈ {target.B, target.T}
    decoy_chain_depth_2          predicted ∈ {decoy_chains[*].answer}
    competitor_or_other          everything else, including
                                 {X_i depth-2 competitors, B_i depth-1 competitors,
                                  decoy heads/bridges/terminals, free-form tokens}
  CO-OCCURRENCE WITH hop2-isolated (component-vs-chain failure partition):
    inherited_component_failure  composite_match=False AND hop2_match=False
                                 (composite error inherits the component failure)
    composition_specific         composite_match=False AND hop2_match=True
                                 (component works on this item but the chain
                                  doesn't — composition-specific failure)
    composition_specific_success composite_match=True AND hop2_match=False
                                 (model got the chain "right" without the component;
                                  suggests coincidence rather than traversal —
                                  the PATHOLOGICAL signal)
    fully_correct                composite_match=True AND hop2_match=True
                                 (both ok; counts as a valid success)
    n/a                          if composite_match=True (covered above)

PATHOLOGICAL-ERROR-STRUCTURE FLAG (v0.2 §7e and §9):
  pathological IFF any item has composite_match=True AND hop2_match=False
  (a strict, mechanically defensible interpretation: even a single
  "composite success without component success" signals that the
  chain output may not be traceable through the component, which
  would invalidate the "success via correct chain under controls"
  reading required by v0.2 §3).

Pure function of (scored, item_specs). No clock, no RNG, no environment,
no network, no model imports. Deterministic.

Authority: Manager + TL ACTION 2026-06-18 ("Begin V3 Composite Gate
Tooling Build"). Build effort only; no run.

— CS Engineer, 2026-06-18
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path


CONTEXTS = ("composite", "hop1", "hop2", "direct_query")


def classify_landed_token(spec: dict, predicted: str) -> str:
    """Mechanical classification of where the composite output token landed."""
    t = spec["target"]
    correct_chain_set = {t["B"], t["T"]}              # B (bridge) or T (target terminal)
    if predicted in correct_chain_set:
        return "correct_chain_wrong_depth"
    decoy_answers = {d["answer"] for d in spec.get("decoy_chains", [])}
    if predicted in decoy_answers:
        return "decoy_chain_depth_2"
    return "competitor_or_other"


def classify_cooccurrence(composite_match: bool, hop2_match: bool) -> str:
    if not composite_match and not hop2_match:
        return "inherited_component_failure"
    if not composite_match and hop2_match:
        return "composition_specific"
    if composite_match and not hop2_match:
        return "composition_specific_success"  # the PATHOLOGICAL signal
    return "fully_correct"


def build_error_log(
    scored_dir: Path,
    items_dir:  Path,
) -> dict:
    items_seen = sorted(p.stem for p in items_dir.glob("item_*.json"))
    per_item = []
    counts = defaultdict(int)        # landed-token classification
    cooc_counts = defaultdict(int)   # co-occurrence partition

    composition_specific_success_count = 0
    composite_match_count = 0
    composite_error_count = 0

    for item_id in items_seen:
        spec_path = items_dir / f"{item_id}.json"
        spec = json.loads(spec_path.read_text())
        comp_path = scored_dir / item_id / "composite.json"
        hop2_path = scored_dir / item_id / "hop2.json"
        if not comp_path.exists() or not hop2_path.exists():
            raise FileNotFoundError(f"missing scored files for {item_id}")
        comp_scored = json.loads(comp_path.read_text())
        hop2_scored = json.loads(hop2_path.read_text())

        composite_match = bool(comp_scored.get("match"))
        hop2_match      = bool(hop2_scored.get("match"))
        predicted       = comp_scored.get("predicted", "")

        landed = "correct" if composite_match else classify_landed_token(spec, predicted)
        cooc   = classify_cooccurrence(composite_match, hop2_match)

        counts[landed] += 1
        cooc_counts[cooc] += 1

        if composite_match:
            composite_match_count += 1
            if cooc == "composition_specific_success":
                composition_specific_success_count += 1
        else:
            composite_error_count += 1

        per_item.append({
            "item":               item_id,
            "ground_truth":       comp_scored.get("ground_truth"),
            "predicted":          predicted,
            "composite_match":    composite_match,
            "hop2_match":         hop2_match,
            "landed_token_class": landed,
            "cooccurrence":       cooc,
        })

    pathological = composition_specific_success_count > 0

    summary = {
        "n_items":                                  len(per_item),
        "composite_match_count":                    composite_match_count,
        "composite_error_count":                    composite_error_count,
        "composition_specific_success_count":       composition_specific_success_count,
        "pathological_error_structure":             pathological,
        "pathological_rule":                        "composition_specific_success_count > 0",
        "landed_token_distribution":                dict(counts),
        "cooccurrence_distribution":                dict(cooc_counts),
    }

    return {
        "logger_version":                "v0.1",
        "scope":                         "v0.2 §9 same-error / wrong-address logging",
        "pathological_error_structure":  pathological,
        "summary":                       summary,
        "per_item":                      per_item,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--scored-dir", type=Path, required=True)
    p.add_argument("--items-dir",  type=Path, required=True)
    p.add_argument("--output",     type=Path, required=True)
    args = p.parse_args(argv)

    log = build_error_log(args.scored_dir, args.items_dir)
    args.output.write_text(json.dumps(log, indent=2) + "\n")

    s = log["summary"]
    print(f"items:                                  {s['n_items']}")
    print(f"composite match:                        {s['composite_match_count']}")
    print(f"composite error:                        {s['composite_error_count']}")
    print(f"composition_specific_success count:     {s['composition_specific_success_count']}")
    print(f"pathological_error_structure:           {s['pathological_error_structure']}")
    print(f"landed token distribution:              {s['landed_token_distribution']}")
    print(f"cooccurrence distribution:              {s['cooccurrence_distribution']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
