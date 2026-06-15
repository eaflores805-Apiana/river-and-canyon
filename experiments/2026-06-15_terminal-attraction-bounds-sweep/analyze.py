#!/usr/bin/env python3
"""
analyze.py — TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1

Reads items_materialized.json + raw_outputs.json, applies the byte-locked scorer
(tier0-run/scorer_twohop_l1.py) for correctness columns and the pre-registered
classifier.py for attraction-type columns. Builds the 6-cell §6 table, runs the
§6 validity checks, and applies the §8 pre-declared readings to identify which
holds. No model execution; deterministic; reads committed bytes only.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
REPO = RUN_DIR.parents[1]
sys.path.insert(0, str(REPO / "tier0-run"))
sys.path.insert(0, str(RUN_DIR))

import scorer_twohop_l1 as scorer    # byte-locked sha b65c6803
import classifier                     # pre-registered §5(b)


def shrink_item_for_scorer(it: dict) -> dict:
    """The byte-locked scorer expects items in the cell03-style schema. Our
    new items use a simpler shape. Build a minimal-shape adapter that exposes
    the fields scorer.classify_output reads (queries.<qt>.expected_answer +
    item context for role inference). For attraction analysis we use our
    classifier; the scorer here is only for correctness columns."""
    # Build the object_roles dict the scorer uses to look up returned tokens.
    object_roles = {}
    # target chain
    object_roles[it["target_chain"]["A"]] = "anchor_A"
    object_roles[it["target_chain"]["B"]] = "hop1_B"
    object_roles[it["target_chain"]["C"]] = "answer_C"
    # decoy chains: classify as distractor-chain endpoints (terminals) / intermediates
    for d in it["decoy_chains"]:
        object_roles[d["A"]] = "distractor_chain_intermediate"  # decoy A
        object_roles[d["B"]] = "distractor_chain_intermediate"  # decoy B
        object_roles[d["C"]] = "distractor_chain_endpoint"      # decoy C
    # holds: inert filler
    for h in it["holds"]:
        object_roles[h["W"]] = "inert_filler"
        object_roles[h["V"]] = "inert_filler"
    return {
        "item_id":    it["item_id"],
        "queries":    it["queries"],
        "object_roles": object_roles,
        "chains": [
            {"chain_id": "target_chain", "fact_role": "hop1_fact"},
        ],
    }


def main() -> int:
    items = {it["item_id"]: it for it in json.loads((RUN_DIR / "items_materialized.json").read_text())}
    raw = json.loads((RUN_DIR / "raw_outputs.json").read_text())

    # Per-generation annotations.
    annotated = []
    for r in raw["results"]:
        item = items[r["item_id"]]
        # Scorer column (correctness only)
        scorer_item = shrink_item_for_scorer(item)
        try:
            scorer_cls = scorer.classify_output(r["raw_output"], scorer_item, r["query_type"])
            scorer_correct = bool(scorer_cls.get("is_correct"))
        except Exception as e:
            scorer_cls = {"error": f"{type(e).__name__}: {e}"}
            scorer_correct = False
        # Classifier column (attraction type)
        clf = classifier.classify_item(r["raw_output"], r["query_type"], item)
        annotated.append({
            **r,
            "scorer_failure_class": scorer_cls.get("failure_class"),
            "scorer_correct":       scorer_correct,
            "classifier_token":     clf["token"],
            "classifier_category":  clf["category"],
        })

    # Write per-row annotated outputs.
    (RUN_DIR / "scored.json").write_text(json.dumps({"annotated": annotated}, indent=2) + "\n")
    (RUN_DIR / "classifier_output.json").write_text(json.dumps(
        [{"item_id": r["item_id"], "cell": r["cell"], "query_type": r["query_type"],
          "raw_output": r["raw_output"], "classifier_category": r["classifier_category"]}
         for r in annotated], indent=2) + "\n")

    # Build the 6-cell §6 table.
    cells = sorted({r["cell"] for r in annotated})
    table = {}
    for cell in cells:
        cell_rows = [r for r in annotated if r["cell"] == cell]
        by_qt = {qt: [r for r in cell_rows if r["query_type"] == qt] for qt in ("hop1", "hop2", "composite")}

        def cat_counts(rows: list[dict]) -> dict[str, int]:
            return dict(Counter(r["classifier_category"] for r in rows))

        n_per_qt = {qt: len(rows) for qt, rows in by_qt.items()}
        cat_by_qt = {qt: cat_counts(rows) for qt, rows in by_qt.items()}

        # Primary metric (per §6): hop1 TARGET_TERMINAL_GRAB rate.
        hop1_grab = cat_by_qt["hop1"].get("TARGET_TERMINAL_GRAB", 0)
        hop1_abstain = cat_by_qt["hop1"].get("ABSTAIN", 0)
        hop1_correct = cat_by_qt["hop1"].get("CORRECT", 0)

        # Secondary: hop2 CORRECT rate (the validity control).
        hop2_correct = cat_by_qt["hop2"].get("CORRECT", 0)

        # Seam-context: composite metrics.
        comp_correct = cat_by_qt["composite"].get("CORRECT", 0)
        comp_decoy_grab = cat_by_qt["composite"].get("DECOY_TERMINAL_GRAB", 0)
        comp_abstain = cat_by_qt["composite"].get("ABSTAIN", 0)
        comp_stopped_short = cat_by_qt["composite"].get("STOPPED_SHORT", 0)

        n = n_per_qt["hop1"]
        table[cell] = {
            "n": n,
            "PRIMARY_hop1_target_terminal_grab_rate": hop1_grab / n if n else 0.0,
            "hop1_abstain_rate":                     hop1_abstain / n if n else 0.0,
            "hop1_correct_rate":                     hop1_correct / n if n else 0.0,
            "VALIDITY_hop2_correct_rate":            hop2_correct / n if n else 0.0,
            "composite_correct_rate":                comp_correct / n if n else 0.0,
            "composite_decoy_terminal_grab_rate":    comp_decoy_grab / n if n else 0.0,
            "composite_abstain_rate":                comp_abstain / n if n else 0.0,
            "composite_stopped_short_rate":          comp_stopped_short / n if n else 0.0,
            "counts_by_query_type":                  cat_by_qt,
        }

    # Validity flags (§6).
    validity_flags = {"hop2_control_per_cell": {}, "composite_at_k1_distinguishability_limited": True}
    for cell, row in table.items():
        validity_flags["hop2_control_per_cell"][cell] = {
            "hop2_correct_rate": row["VALIDITY_hop2_correct_rate"],
            "cell_uninterpretable_if_collapsed": row["VALIDITY_hop2_correct_rate"] < 0.75,
        }

    # §8 pre-declared readings — compute on the PRIMARY metric.
    def avg_grab(cells_set: list[str]) -> float:
        vals = [table[c]["PRIMARY_hop1_target_terminal_grab_rate"] for c in cells_set]
        return sum(vals) / len(vals)

    avg_k1 = avg_grab(["k1_EARLY", "k1_LATE"])
    avg_k3 = avg_grab(["k3_EARLY", "k3_LATE"])
    avg_k5 = avg_grab(["k5_EARLY", "k5_LATE"])

    avg_early = avg_grab(["k1_EARLY", "k3_EARLY", "k5_EARLY"])
    avg_late  = avg_grab(["k1_LATE",  "k3_LATE",  "k5_LATE"])

    # Reading SMOOTH SCALING: hop1 grab rate rises with k (≥ +0.25 from k=1 to k=5, monotone-ish across both positions).
    early_monotone = (table["k3_EARLY"]["PRIMARY_hop1_target_terminal_grab_rate"]
                      >= table["k1_EARLY"]["PRIMARY_hop1_target_terminal_grab_rate"] - 0.05
                      and table["k5_EARLY"]["PRIMARY_hop1_target_terminal_grab_rate"]
                      >= table["k3_EARLY"]["PRIMARY_hop1_target_terminal_grab_rate"] - 0.05)
    late_monotone = (table["k3_LATE"]["PRIMARY_hop1_target_terminal_grab_rate"]
                     >= table["k1_LATE"]["PRIMARY_hop1_target_terminal_grab_rate"] - 0.05
                     and table["k5_LATE"]["PRIMARY_hop1_target_terminal_grab_rate"]
                     >= table["k3_LATE"]["PRIMARY_hop1_target_terminal_grab_rate"] - 0.05)
    smooth_scaling = (avg_k5 - avg_k1 >= 0.25) and early_monotone and late_monotone

    # Reading MAXED AT k=1: hop1 grab already substantial at k=1 (≥0.50) and roughly flat across k.
    maxed_at_k1 = (avg_k1 >= 0.50) and (abs(avg_k5 - avg_k1) < 0.15)

    # Reading POSITION EFFECT: hop1 grab (and/or composite decoy-grab) differs by EARLY vs LATE at fixed k (≥0.25 gap).
    position_gap_by_k = {k: abs(table[f"k{k}_EARLY"]["PRIMARY_hop1_target_terminal_grab_rate"]
                                - table[f"k{k}_LATE"]["PRIMARY_hop1_target_terminal_grab_rate"])
                         for k in [1, 3, 5]}
    position_effect = any(gap >= 0.25 for gap in position_gap_by_k.values())

    readings_held = {
        "SMOOTH_SCALING": smooth_scaling,
        "MAXED_AT_k1":    maxed_at_k1,
        "POSITION_EFFECT": position_effect,
    }
    if not any(readings_held.values()):
        primary_reading = "FLAT_or_MIXED"
    else:
        # If multiple hold, report all but pick the most informative (per §8).
        primary_reading = "+".join(k for k, v in readings_held.items() if v)

    summary = {
        "run_name": "TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1",
        "six_cell_table": table,
        "validity_flags": validity_flags,
        "averages": {
            "avg_grab_at_k1": avg_k1,
            "avg_grab_at_k3": avg_k3,
            "avg_grab_at_k5": avg_k5,
            "avg_grab_EARLY": avg_early,
            "avg_grab_LATE":  avg_late,
            "position_gap_by_k": position_gap_by_k,
        },
        "readings_held": readings_held,
        "primary_reading": primary_reading,
    }
    (RUN_DIR / "six_cell_table.json").write_text(json.dumps(summary, indent=2) + "\n")

    # ── Pretty-print summary ──
    print(f"\n=== 6-cell table: PRIMARY hop1 TARGET_TERMINAL_GRAB rate ===")
    print(f"{'cell':<12}  {'grab':>6}  {'abstain':>8}  {'correct':>8}  {'hop2_ctrl':>10}  {'comp_corr':>9}  {'comp_decoy':>10}")
    for cell in ["k1_EARLY", "k1_LATE", "k3_EARLY", "k3_LATE", "k5_EARLY", "k5_LATE"]:
        r = table[cell]
        print(f"  {cell:<10}  "
              f"{r['PRIMARY_hop1_target_terminal_grab_rate']:.3f}  "
              f"{r['hop1_abstain_rate']:.3f}     "
              f"{r['hop1_correct_rate']:.3f}     "
              f"{r['VALIDITY_hop2_correct_rate']:.3f}       "
              f"{r['composite_correct_rate']:.3f}      "
              f"{r['composite_decoy_terminal_grab_rate']:.3f}")
    print(f"\naverages: k1={avg_k1:.3f} k3={avg_k3:.3f} k5={avg_k5:.3f}  EARLY={avg_early:.3f} LATE={avg_late:.3f}")
    print(f"position gap by k: {position_gap_by_k}")
    print(f"readings held:  {readings_held}")
    print(f"PRIMARY READING: {primary_reading}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
