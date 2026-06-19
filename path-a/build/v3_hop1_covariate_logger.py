#!/usr/bin/env python3
"""
v3_hop1_covariate_logger.py — V3 Hop1 Stability covariate logger
(hop1-stability tooling 2/2 of the build per Manager + TL ACTION 2026-06-19
"Begin Hop1 Stability Tooling Build").

Emits the §6 predeclared positional/structural covariates per item from the
hop1-stability prereg v0.1, working ONLY on the hop1 scored outputs +
item specs. All covariates are deterministic, positional, and structural;
NO mechanism labels are emitted (per prereg §6 forbidden labels).

PRIMARY (confirmatory hypothesis):
  predicted_is_P_role_distractor   predicted ∈ {d.head for d in spec.decoy_chains}
                                   (P_1..P_5 = r1-SUBJECTs of relation-reusing
                                    distractor chains; suggested by the seen
                                    097..192 result, tested fresh here)

SECONDARY (descriptive co-occurrence; reported alongside but separately):
  seed_block                       which fresh block this item belongs to
                                   (derived from item_index + locked range mapping)
  target_B_token                   spec.target.B (identity + char width)
  predicted_token                  scored.predicted (identity)
  predicted_role_class             one of {C_star, B, T, T_i_i, X_i, B_competitor_i,
                                     P_i (decoy head), Q_i (decoy bridge), S_i
                                     (decoy answer), r-class relation, neutral
                                     pool, free-form}
  r1_identity                      spec.target.r1
  relation_position                always 0 (head relation; constant per scheme)
  fact_line_position_target_hop1   always 0 (target hop1 fact at index 0; constant)
  prompt_char_count                len(prompt) — read from realization summary if
                                   available, else None
  token_width_class                width bucket of role tokens (e.g., 6 or 7 chars
                                   under i{NNN}_ scheme)
  competitor_distractor_role_class same as predicted_role_class but specifically
                                   classifies non-correct predictions

Pure function of (scored, item_specs, [realization_summary]). No clock, no RNG,
no environment, no network, no model imports.

Authority: Manager + TL ACTION 2026-06-19. Build effort only; no run.

— CS Engineer, 2026-06-19
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


# Locked seed-range mapping per prereg v0.1 §5 (defaults; can be overridden via CLI)
DEFAULT_START_INDEX = 193   # block F1 starts here
DEFAULT_BLOCK_SIZE  = 96
DEFAULT_N_BLOCKS    = 6      # F1..F6 → 193..768


# Locked filler-verb pool from v3_direct_query_filler.md (used here only to
# classify "predicted is a filler verb token" if it ever appears)
LOCKED_FILLER_VERBS = {"holds", "marks", "types", "pairs", "links"}

# Identifier-like pattern for free-form tokens
_ID_TOKEN_RE = re.compile(r"[A-Za-z][\w]*")


def block_id_for_index(item_index: int,
                       start_index: int = DEFAULT_START_INDEX,
                       block_size:  int = DEFAULT_BLOCK_SIZE,
                       n_blocks:    int = DEFAULT_N_BLOCKS) -> int | None:
    """Return block id (1..n_blocks) for an item_index, or None if out of range.
    Block F1 contains indices [start_index, start_index + block_size).
    Block Fk contains [start_index + (k-1)*block_size, start_index + k*block_size).
    """
    if item_index < start_index:
        return None
    offset = item_index - start_index
    block_idx = (offset // block_size) + 1
    if block_idx < 1 or block_idx > n_blocks:
        return None
    return block_idx


def classify_predicted_role(spec: dict, predicted: str) -> str:
    """Mechanical classification of the predicted token's role within the item's
    token namespace. Returns one of:
       C_star, B, T, T_i, X_i_competitor, B_i_competitor,
       P_decoy_head, Q_decoy_bridge, S_decoy_answer, T_i_decoy_terminal,
       r1, r2, post_C_star_relation, head_competitor_relation, tail_competitor_relation,
       filler_verb, neutral_pool, free_form
    """
    t = spec["target"]
    if predicted == t["C_star"]:           return "C_star"
    if predicted == t["B"]:                 return "B"
    if predicted == t["T"]:                 return "T"
    if predicted == t["r1"]:                return "r1"
    if predicted == t["r2"]:                return "r2"
    if predicted in t.get("post_C_star_relations", []):
                                            return "post_C_star_relation"

    for c in spec.get("depth_2_competitors", []):
        if predicted == c["X"]:             return "X_i_competitor"
        if predicted == c["B_competitor"]:  return "B_i_competitor"
        if predicted == c["head_relation"]: return "head_competitor_relation"
        if predicted == c["second_relation"]: return "tail_competitor_relation"

    for d in spec.get("decoy_chains", []):
        if predicted == d["head"]:          return "P_decoy_head"
        if predicted == d["bridge"]:        return "Q_decoy_bridge"
        if predicted == d["answer"]:        return "S_decoy_answer"
        if predicted == d["T_i"]:           return "T_i_decoy_terminal"

    if predicted in LOCKED_FILLER_VERBS:    return "filler_verb"
    # Otherwise: free-form (any tokens that aren't in the per-item namespace)
    return "free_form"


def char_width_class(role_token: str) -> int:
    """The per-item-prefix scheme produces 6- or 7-char role tokens
    (i{NNN}_ + 1-char suffix = 6; i{NNN}_ + 2-char suffix = 7)."""
    return len(role_token)


def build_log(
    scored_dir: Path,
    items_dir:  Path,
    start_index: int = DEFAULT_START_INDEX,
    block_size:  int = DEFAULT_BLOCK_SIZE,
    n_blocks:    int = DEFAULT_N_BLOCKS,
    realization_summary: dict | None = None,
) -> dict:
    """Build the per-item covariate log + summary."""
    # Build per-item char counts from the realization summary if present
    char_counts: dict[str, int] = {}
    if realization_summary is not None:
        for r in realization_summary.get("per_item", []):
            cc = r.get("char_counts", {})
            char_counts[r["item"]] = cc.get("hop1")   # may be None if hop1 not rendered

    per_item: list[dict] = []
    # Aggregates
    n_total                       = 0
    n_hop1_match                  = 0
    primary_p_role_count          = 0
    primary_p_role_among_wrong    = 0
    role_class_distribution       = defaultdict(int)
    role_class_among_wrong        = defaultdict(int)
    width_distribution            = defaultdict(int)
    block_counts                  = defaultdict(int)

    items_seen = sorted(p.stem for p in items_dir.glob("item_*.json"))
    for item_id in items_seen:
        spec_path = items_dir / f"{item_id}.json"
        spec = json.loads(spec_path.read_text())
        item_index = spec["_build_provenance"]["item_index"]
        block_id   = block_id_for_index(item_index, start_index, block_size, n_blocks)
        # Skip items outside the locked block range
        if block_id is None:
            continue

        hop1_path = scored_dir / item_id / "hop1.json"
        if not hop1_path.exists():
            raise FileNotFoundError(f"missing hop1 scored file: {hop1_path}")
        hop1 = json.loads(hop1_path.read_text())

        predicted    = hop1.get("predicted", "")
        ground_truth = hop1.get("ground_truth", "")
        match        = bool(hop1.get("match"))

        # PRIMARY: P-role distractor landing
        p_role_set = {d["head"] for d in spec.get("decoy_chains", [])}
        predicted_is_P_role = predicted in p_role_set

        # SECONDARY: positional / structural
        role_class    = classify_predicted_role(spec, predicted)
        target_b      = spec["target"]["B"]
        r1_token      = spec["target"]["r1"]
        target_b_width = char_width_class(target_b)
        char_count    = char_counts.get(item_id)   # may be None if no realization summary

        per_item.append({
            "item":                                   item_id,
            "item_index":                             item_index,
            "block_id":                               block_id,
            "predicted":                              predicted,
            "ground_truth":                           ground_truth,
            "match":                                  match,
            # PRIMARY
            "predicted_is_P_role_distractor":         predicted_is_P_role,
            # SECONDARY
            "predicted_role_class":                   role_class,
            "target_B_token":                         target_b,
            "target_B_width":                         target_b_width,
            "r1_identity":                            r1_token,
            "relation_position":                      0,   # constant: r1 at slot 0
            "fact_line_position_target_hop1":         0,   # constant: target hop1 at index 0
            "prompt_hop1_char_count":                 char_count,
            "competitor_distractor_role_class":       role_class if not match else None,
        })

        n_total += 1
        if match: n_hop1_match += 1
        block_counts[block_id] += 1
        if predicted_is_P_role:
            primary_p_role_count += 1
            if not match:
                primary_p_role_among_wrong += 1
        role_class_distribution[role_class] += 1
        if not match:
            role_class_among_wrong[role_class] += 1
        width_distribution[target_b_width] += 1

    n_hop1_wrong = n_total - n_hop1_match

    summary = {
        "n_items":                                    n_total,
        "n_hop1_match":                               n_hop1_match,
        "n_hop1_wrong":                               n_hop1_wrong,
        "block_range":                                {"start_index": start_index,
                                                       "block_size":  block_size,
                                                       "n_blocks":    n_blocks},
        "per_block_item_counts":                      dict(block_counts),
        # PRIMARY: confirmatory P-role hypothesis result (descriptive)
        "primary_P_role_distractor_count":            primary_p_role_count,
        "primary_P_role_among_wrong_count":           primary_p_role_among_wrong,
        "primary_P_role_among_wrong_rate":            (primary_p_role_among_wrong / n_hop1_wrong
                                                       if n_hop1_wrong > 0 else None),
        # SECONDARY: descriptive distributions
        "secondary_role_class_distribution":          dict(role_class_distribution),
        "secondary_role_class_among_wrong":           dict(role_class_among_wrong),
        "secondary_target_B_width_distribution":      dict(width_distribution),
        "forbidden_labels_used":                      "none (mechanism / binding / attention / "
                                                     "reasoning failure / shortcut all forbidden "
                                                     "per prereg §6 and never emitted)",
    }

    return {
        "logger_version":           "v0.1",
        "scope":                    "prereg v0.1 §6 same-prediction covariate logging; "
                                    "positional/structural only; co-occurrence not cause",
        "n_items":                  n_total,
        "summary":                  summary,
        "per_item":                 per_item,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--scored-dir",          type=Path, required=True)
    p.add_argument("--items-dir",           type=Path, required=True)
    p.add_argument("--output",              type=Path, required=True)
    p.add_argument("--realization-summary", type=Path, default=None,
                    help="optional path to realization_summary.json for prompt char counts")
    p.add_argument("--start-index",         type=int, default=DEFAULT_START_INDEX)
    p.add_argument("--block-size",          type=int, default=DEFAULT_BLOCK_SIZE)
    p.add_argument("--n-blocks",            type=int, default=DEFAULT_N_BLOCKS)
    args = p.parse_args(argv)

    realization_summary = None
    if args.realization_summary is not None and args.realization_summary.exists():
        realization_summary = json.loads(args.realization_summary.read_text())

    log = build_log(args.scored_dir, args.items_dir,
                    args.start_index, args.block_size, args.n_blocks,
                    realization_summary)
    args.output.write_text(json.dumps(log, indent=2) + "\n")

    s = log["summary"]
    print(f"items processed:                            {s['n_items']}")
    print(f"hop1 match / wrong:                         {s['n_hop1_match']} / {s['n_hop1_wrong']}")
    print(f"PRIMARY P-role distractor count:            {s['primary_P_role_distractor_count']}")
    print(f"  (of which among wrong predictions):       {s['primary_P_role_among_wrong_count']}")
    if s['primary_P_role_among_wrong_rate'] is not None:
        print(f"  P-role share of wrong predictions:        {s['primary_P_role_among_wrong_rate']:.4f}")
    print(f"per-block item counts:                      {s['per_block_item_counts']}")
    print(f"role-class distribution:                    {s['secondary_role_class_distribution']}")
    print(f"role-class among wrong:                     {s['secondary_role_class_among_wrong']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
