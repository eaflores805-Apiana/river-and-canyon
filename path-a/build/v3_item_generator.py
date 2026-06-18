#!/usr/bin/env python3
"""
v3_item_generator.py — V3 (same-depth-competitor construction) item generator.

Realizes the four open slots from PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3
§"Open slots still requiring CS realization":

  1. Item generator + seed
  2. Concrete token pool
  3. Direct-query filler realization
  4. Relation-balancing realization

Authority: TL / Manager ACTION 2026-06-17 ("Begin V3 Build Open Slots") —
BUILD EFFORT ONLY. This generator produces conformance-checkable spec items
shaped to pass the Path A inspector C1-C9 in REAL-RUN mode (no
`_fixture_mode`, no `_sweep_mode`) under the Manager-locked parameter point
(k=5, D=5, p=5, m=10, margin=0.25; F=0.20; success threshold=0.45).

This module does NOT execute a model. It does NOT write prompt strings. It
produces construction specs only — items in the sense the inspector consumes:
JSON objects describing the construction at the schema/property level. A
downstream prompt-realization layer (which Manager by-name authorization would
gate, not this build) would compose these specs into concrete prompts for the
four contexts (composite / hop1 / hop2 / direct_query).

Token convention (per-item independence):
  - every item gets a unique prefix `i{NNN}_` so cross-item token collisions
    are impossible by construction (item N's tokens cannot alias item M's)
  - within an item, role-based names: prefix + role letter + index
    (e.g. i007_C1, i007_B1, i007_X2, i007_Q3, i007_Ti4)
  - the prefix scheme generalizes to N=96 (and beyond) without any change
    to the schema or this generator

Seed plan (determinism):
  - item N uses seed = N (1-indexed)
  - C* position slot for item N: ((N - 1) mod p) + 1, cycling 1..p
  - direct-query filler form rotated by seed mod len(filler_forms)
  - all other content is a pure function of seed + position; no randomness,
    no clock, no environment dependencies → byte-identical reproduction
    from the same (item_index, position, seed) tuple

This generator does not authorize: build approval covers this generator's
*existence and output*, NOT a model run, item materialization beyond the
build-demonstration batch, prompt generation, compression, Claim C, Paper B,
capability claim, or mechanism claim. The Path A FP16 K=5 FAIL stays closed.

— CS Engineer, 2026-06-17
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

# Manager-locked values (must match path-a/inspector/constants.py exactly).
# Repeated here as a sanity assertion at import time; the inspector is the
# enforcer, this is a sanity guard for the build.
LOCKED_K        = 5
LOCKED_D        = 5
LOCKED_P        = 5
LOCKED_M        = 10
LOCKED_MARGIN   = 0.25

# Competitor relation pairs (head, tail). Order is fixed and deterministic.
# Pairs chosen disjoint from {r1, r2} so C4 (r1 unique) holds; both within a
# pair and across pairs all values are unique strings.
_COMPETITOR_RELATION_PAIRS = [
    ("s1", "s2"),
    ("t1", "t2"),
    ("u1", "u2"),
    ("v1", "v2"),
    ("w1", "w2"),
]
assert len(_COMPETITOR_RELATION_PAIRS) >= LOCKED_D, \
    f"competitor relation pool ({len(_COMPETITOR_RELATION_PAIRS)}) < D ({LOCKED_D})"

# Filler templates (length-matched in characters when {W} and {V} are
# replaced by short neutral tokens). Each template uses 5 letters between
# {W} and {V} so length-matching is by-construction; selection is per-seed.
_FILLER_FORMS = [
    "{W} holds {V}",
    "{W} marks {V}",
    "{W} types {V}",
    "{W} pairs {V}",
    "{W} links {V}",
]


def _item_prefix(item_index: int) -> str:
    """e.g., 'i007_' for item 7. Guarantees cross-item token independence."""
    return f"i{item_index:03d}_"


def _make_target(prefix: str) -> dict:
    return {
        "A":      f"{prefix}A",
        "B":      f"{prefix}B1",
        "C_star": f"{prefix}C1",
        "T":      f"{prefix}T0",
        "r1":     f"{prefix}r1",
        "r2":     f"{prefix}r2",
        "post_C_star_relations": [f"{prefix}rX", f"{prefix}rY"],
    }


def _make_depth_2_competitors(prefix: str, D: int) -> list[dict]:
    """D=LOCKED_D same-depth competitors at the head. Each uses a distinct
    relation pair disjoint from {r1, r2}, with a unique B_competitor and X.
    """
    out = []
    for i in range(D):
        head_rel, second_rel = _COMPETITOR_RELATION_PAIRS[i]
        out.append({
            "head_relation":   f"{prefix}{head_rel}",
            "B_competitor":    f"{prefix}B{i + 2}",   # B2..B(D+1); B1 is the target B
            "second_relation": f"{prefix}{second_rel}",
            "X":               f"{prefix}X{i + 2}",   # X2..X(D+1); X1 (== C_star) reserved for target
        })
    return out


def _make_decoy_chains(prefix: str, k: int) -> list[dict]:
    """k=LOCKED_K decoy chains (chain-level clutter). Each has its own head,
    bridge, answer, and decoy terminal."""
    return [
        {
            "head":   f"{prefix}P{i + 1}",
            "bridge": f"{prefix}Q{i + 1}",
            "answer": f"{prefix}S{i + 1}",
            "T_i":    f"{prefix}Ti{i + 1}",
        }
        for i in range(k)
    ]


def _make_relation_balance(prefix: str, D: int) -> dict:
    """C6 / E8 relation balance: every relation appears exactly once,
    head relations at position 0, tail relations at position 1. Inspector
    C6 checks balanced frequency + role-grouped order positions."""
    head_relations = [f"{prefix}r1"] + [
        f"{prefix}{_COMPETITOR_RELATION_PAIRS[i][0]}" for i in range(D)
    ]
    tail_relations = [f"{prefix}r2"] + [
        f"{prefix}{_COMPETITOR_RELATION_PAIRS[i][1]}" for i in range(D)
    ]
    return {
        "frequency": {r: 1 for r in head_relations + tail_relations},
        "order_positions": {
            **{r: [0] for r in head_relations},
            **{r: [1] for r in tail_relations},
        },
    }


def _make_direct_query(seed: int) -> dict:
    """E5 direct-query filler: neutral, length-matched, contains neither B
    nor C*. Templates use {W} and {V} placeholders to be filled at prompt-
    realization time (downstream of this build) with neutral tokens drawn
    from a pool disjoint from the per-item token namespace."""
    return {
        "withhold_fact_role":          "B_to_C_star",
        "filler_form":                 _FILLER_FORMS[seed % len(_FILLER_FORMS)],
        "filler_contains_B_or_C_star": False,
    }


_CONTEXTS = {
    "composite":     {"present_facts": "full"},
    "hop1":          {"context_isolated_from_composite": True},
    "hop2":          {"context_isolated_from_composite": True},
    "direct_query":  {"context_isolated_from_composite": True},
    "load_matched":  True,
}


def generate_item(item_index: int, c_star_position: int, seed: int) -> dict:
    """Generate one V3 spec at (item_index, p-slot, seed).

    item_index >= 1
    c_star_position in 1..LOCKED_P
    seed >= 1
    """
    if item_index < 1:
        raise ValueError(f"item_index must be >= 1; got {item_index}")
    if not 1 <= c_star_position <= LOCKED_P:
        raise ValueError(
            f"c_star_position must be 1..{LOCKED_P}; got {c_star_position}"
        )
    if seed < 1:
        raise ValueError(f"seed must be >= 1; got {seed}")

    prefix = _item_prefix(item_index)
    return {
        "construction_id": (
            f"path_a_v3_item_{item_index:03d}_"
            f"pos{c_star_position}_seed{seed:03d}_v0.1"
        ),
        "params": {
            "k":      LOCKED_K,
            "D":      LOCKED_D,
            "p":      LOCKED_P,
            "m":      LOCKED_M,
            "margin": LOCKED_MARGIN,
        },
        "target":              _make_target(prefix),
        "depth_2_competitors": _make_depth_2_competitors(prefix, LOCKED_D),
        "decoy_chains":        _make_decoy_chains(prefix, LOCKED_K),
        "relation_balance":    _make_relation_balance(prefix, LOCKED_D),
        "direct_query":        _make_direct_query(seed),
        "contexts":            _CONTEXTS,
        "_build_provenance": {
            "item_index":      item_index,
            "c_star_position": c_star_position,
            "seed":            seed,
            "generator":       "v3_item_generator.py v0.1",
            "scope":           "build-realization only; not run-authorized",
        },
    }


def slot_for_index(item_index: int) -> int:
    """Deterministic C* position assignment: item N → position ((N-1) mod p) + 1.
    Cycles through positions 1..p uniformly. The seed plan exposes this so
    the same item_index always yields the same position."""
    return ((item_index - 1) % LOCKED_P) + 1


def seed_for_index(item_index: int) -> int:
    """Deterministic seed assignment: item N → seed N. The simplest plan that
    gives byte-identical reproduction at the same item_index."""
    return item_index


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    p.add_argument("--out-dir", type=Path, required=True,
                   help="output directory for generated items")
    p.add_argument("--count", type=int, default=8,
                   help="number of items in demonstration batch (default 8)")
    p.add_argument("--verbose", action="store_true",
                   help="print each generated item's path + sha256")
    args = p.parse_args(argv)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    paths_and_hashes = []
    for n in range(1, args.count + 1):
        position = slot_for_index(n)
        seed     = seed_for_index(n)
        item     = generate_item(n, position, seed)
        body     = json.dumps(item, indent=2, sort_keys=False) + "\n"
        out_path = args.out_dir / f"item_{n:03d}.json"
        out_path.write_text(body)
        sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
        paths_and_hashes.append((out_path, sha))
        if args.verbose:
            print(f"{sha}  {out_path}")

    if not args.verbose:
        print(f"wrote {len(paths_and_hashes)} items to {args.out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
