#!/usr/bin/env python3
"""
v3_prompt_realizer.py — V3 four-context prompt realizer (floor-check tooling 2/4).

Renders each schema-level item spec into four concrete prompts:
  composite / hop1 / hop2 / direct_query

under the v0.4 §4 / F1 length-matching constraint:
  MAX_DELTA = 8 characters per item-set (same-template-class, character-count gating).

Authority: Manager + TL ACTION 2026-06-18 ("File V3 Floor-Check Prereg v0.4
and Begin Tooling Build"), Step 2. **Build effort only.** This tool does NOT
import any model, does NOT execute any prompt, does NOT materialize the
locked N=96, and does NOT authorize a run. It is a pure function of
(item_spec, neutral_token_pool) — same inputs → byte-identical output.

Determinism: no clock, no RNG, no environment, no network.

Template class: each of the four prompts shares an identical 3-section layout:
  ── HEADER ──   (fixed string, identical across contexts)
  ── FACTS ──    (22 fact lines; identical across composite/hop1/hop2; for
                  direct_query, the target bridge fact at line index 1 is
                  replaced by a filler triple of character-comparable length)
  ── QUERY ──    (single line, varies by context, drawn from a fixed template
                  pool with width-balanced role-substitution)

— CS Engineer, 2026-06-18
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


# Manager-locked values (consistency check; the inspector / constants is the enforcer)
LOCKED_K, LOCKED_D, LOCKED_P, LOCKED_M = 5, 5, 5, 10

# v0.4 §4 / F1 length-matching tolerance — character-count gating
MAX_DELTA = 8

# Neutral-token pool (mirrors v3_neutral_token_pool.md §2; if that file is the
# of-record digest, this constant is the in-realizer copy bound by the
# realizer digest per v0.4 §T embedding option B; default is separate file —
# realizer reads it from the .md file when called via CLI. See §"main".)
NEUTRAL_W_DEFAULT = [
    "neutral", "placebo", "abstain", "padding",
    "default", "fillerX", "blankXY", "ineutrl",
]
NEUTRAL_V_DEFAULT = [
    "placebo", "abstain", "padding", "default",
    "fillerX", "blankXY", "ineutrl", "neutral",
]

# Filler verbs (5 chars each; mirrors v3_direct_query_filler.md)
FILLER_VERBS = ["holds", "marks", "types", "pairs", "links"]


# ── Prompt section primitives ──────────────────────────────────────────────

_HEADER = "FACTS"
_QUERY_HEADER = "QUERY"


def _fact_triple(subj: str, rel: str, obj: str) -> str:
    """Render one fact as a structured triple. Uniform format → uniform width
    contribution given uniform-width role tokens."""
    return f"({subj}, {rel}, {obj})"


def _select_neutral_pair(
    item_index: int,
    w_pool: list[str],
    v_pool: list[str],
) -> tuple[str, str]:
    """Deterministic (W, V) selection per v3_neutral_token_pool.md §4."""
    W = w_pool[(item_index - 1) % len(w_pool)]
    V = v_pool[item_index % len(v_pool)]
    assert W != V, f"W == V for item {item_index}: {W!r}"
    return W, V


def _filler_triple(item_index: int, w_pool: list[str], v_pool: list[str]) -> str:
    """Build the dq filler triple: (W, verb, V) with rotation per seed."""
    W, V = _select_neutral_pair(item_index, w_pool, v_pool)
    verb = FILLER_VERBS[item_index % len(FILLER_VERBS)]
    return _fact_triple(W, verb, V)


def _build_fact_lines(spec: dict) -> list[str]:
    """Return the 22 fact lines (2 target + 5*2 competitor + 5*2 decoy) in
    deterministic order. Identical across composite/hop1/hop2 for an item."""
    t = spec["target"]
    lines = [
        _fact_triple(t["A"],  t["r1"], t["B"]),       # 0: target hop1
        _fact_triple(t["B"],  t["r2"], t["C_star"]),  # 1: target bridge (the substitutable line)
    ]
    # 5 same-depth competitors, 2 facts each
    for c in spec["depth_2_competitors"]:
        lines.append(_fact_triple(t["A"], c["head_relation"],   c["B_competitor"]))
        lines.append(_fact_triple(c["B_competitor"], c["second_relation"], c["X"]))
    # 5 decoy chains, 2 facts each
    for d in spec["decoy_chains"]:
        lines.append(_fact_triple(d["head"],   t["r1"], d["bridge"]))
        lines.append(_fact_triple(d["bridge"], t["r2"], d["answer"]))
    assert len(lines) == 2 + 2 * LOCKED_D + 2 * LOCKED_K, \
        f"fact-list length unexpected: {len(lines)}"
    return lines


def _query_line(spec: dict, context: str) -> str:
    """Return the QUERY line for the given context. Width-balanced by design.

    composite, dq: "QUERY: ({A}, {r1}.{r2}, ?)"
    hop1:          "QUERY: ({A}, {r1}, ?)"
    hop2:          "QUERY: ({B}, {r2}, ?)"

    Per the realizer's template-class invariant, all four queries share the
    same `QUERY: (..., ..., ?)` skeleton; only the SUBJ and REL slots vary.
    Length deltas come from REL = `r1.r2` (5 chars incl. dot) vs `r1` or
    `r2` (2 chars); SUBJ widths are within 1 char (A vs B1).
    """
    t = spec["target"]
    if context == "composite" or context == "direct_query":
        subj, rel = t["A"], f"{t['r1']}.{t['r2']}"
    elif context == "hop1":
        subj, rel = t["A"], t["r1"]
    elif context == "hop2":
        subj, rel = t["B"], t["r2"]
    else:
        raise ValueError(f"unknown context: {context!r}")
    return f"{_QUERY_HEADER}: ({subj}, {rel}, ?)"


# ── Realizer entrypoint ────────────────────────────────────────────────────

def realize_item(
    spec: dict,
    w_pool: list[str] | None = None,
    v_pool: list[str] | None = None,
) -> dict:
    """Render one item spec into four prompts + character counts.

    Returns:
      {
        "item_id":         <construction_id>,
        "prompts": {
            "composite":    str,
            "hop1":         str,
            "hop2":         str,
            "direct_query": str,
        },
        "char_counts": {
            "composite":    int,
            "hop1":         int,
            "hop2":         int,
            "direct_query": int,
        },
        "char_delta":      int,   # max - min over the four counts
        "max_delta_gate":  bool,  # True iff char_delta <= MAX_DELTA
      }
    """
    w_pool = w_pool if w_pool is not None else NEUTRAL_W_DEFAULT
    v_pool = v_pool if v_pool is not None else NEUTRAL_V_DEFAULT
    item_index = spec["_build_provenance"]["item_index"]

    fact_lines_base = _build_fact_lines(spec)

    # Direct-query: substitute the bridge fact at index 1 with the filler triple
    fact_lines_dq = list(fact_lines_base)
    fact_lines_dq[1] = _filler_triple(item_index, w_pool, v_pool)

    def render(facts: list[str], context: str) -> str:
        body = "\n".join(facts)
        query = _query_line(spec, context)
        return f"{_HEADER}:\n{body}\n{query}\n"

    prompts = {
        "composite":    render(fact_lines_base, "composite"),
        "hop1":         render(fact_lines_base, "hop1"),
        "hop2":         render(fact_lines_base, "hop2"),
        "direct_query": render(fact_lines_dq,   "direct_query"),
    }
    char_counts = {ctx: len(p) for ctx, p in prompts.items()}
    counts = list(char_counts.values())
    delta = max(counts) - min(counts)

    return {
        "item_id":        spec["construction_id"],
        "prompts":        prompts,
        "char_counts":    char_counts,
        "char_delta":     delta,
        "max_delta_gate": delta <= MAX_DELTA,
    }


def _read_pool(neutral_pool_path: Path | None) -> tuple[list[str], list[str]]:
    """Read the W/V pools. If neutral_pool_path is None, use the in-realizer
    defaults (per v0.4 §T option B; realizer digest then binds the pool)."""
    if neutral_pool_path is None:
        return NEUTRAL_W_DEFAULT, NEUTRAL_V_DEFAULT
    text = neutral_pool_path.read_text()
    # Parse the markdown table at §2 by extracting the literal token strings
    # between double quotes inside the NEUTRAL_W_TOKENS / NEUTRAL_V_TOKENS
    # blocks. This is a deliberately simple parser tied to the file's
    # documented layout; if §2 is restructured, this needs updating in lockstep.
    def _extract_pool(block_name: str) -> list[str]:
        marker = f"{block_name} = ["
        i = text.index(marker)
        j = text.index("]", i)
        block = text[i:j]
        out = []
        k = 0
        while True:
            a = block.find('"', k)
            if a == -1:
                break
            b = block.find('"', a + 1)
            if b == -1:
                break
            out.append(block[a + 1:b])
            k = b + 1
        return out
    return _extract_pool("NEUTRAL_W_TOKENS"), _extract_pool("NEUTRAL_V_TOKENS")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    p.add_argument("--items-dir",   type=Path, required=True,
                   help="directory of item_*.json specs (input)")
    p.add_argument("--out-dir",     type=Path, required=True,
                   help="directory to write per-item subdirectories with four prompt files (output)")
    p.add_argument("--summary-path", type=Path, required=True,
                   help="path to write realization_summary.json")
    p.add_argument("--neutral-pool", type=Path, default=None,
                   help="optional path to v3_neutral_token_pool.md (if omitted, in-realizer defaults are used; "
                        "v0.4 §T embedding option B applies, and the realizer digest binds the pool)")
    args = p.parse_args(argv)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    w_pool, v_pool = _read_pool(args.neutral_pool)

    items = sorted(args.items_dir.glob("item_*.json"))
    if not items:
        print(f"no item_*.json found in {args.items_dir}", file=sys.stderr)
        return 2

    summary_rows = []
    all_gate_pass = True
    for spec_path in items:
        spec = json.loads(spec_path.read_text())
        result = realize_item(spec, w_pool, v_pool)
        item_dir = args.out_dir / spec_path.stem
        item_dir.mkdir(parents=True, exist_ok=True)
        for ctx, text in result["prompts"].items():
            (item_dir / f"{ctx}.txt").write_text(text)
        summary_rows.append({
            "item":           spec_path.stem,
            "construction_id": result["item_id"],
            "char_counts":    result["char_counts"],
            "char_delta":     result["char_delta"],
            "max_delta_gate": result["max_delta_gate"],
        })
        if not result["max_delta_gate"]:
            all_gate_pass = False

    summary = {
        "realizer_version":   "v0.1",
        "max_delta_gate":     MAX_DELTA,
        "items_dir":          str(args.items_dir),
        "out_dir":            str(args.out_dir),
        "neutral_pool_path":  str(args.neutral_pool) if args.neutral_pool else "<in-realizer defaults>",
        "n_items":            len(summary_rows),
        "n_gate_pass":        sum(1 for r in summary_rows if r["max_delta_gate"]),
        "n_gate_fail":        sum(1 for r in summary_rows if not r["max_delta_gate"]),
        "all_gate_pass":      all_gate_pass,
        "per_item":           summary_rows,
        "scope":              "build-realization only; not run-authorized",
    }
    args.summary_path.write_text(json.dumps(summary, indent=2) + "\n")
    print(f"items: {summary['n_items']}  gate-pass: {summary['n_gate_pass']}  "
          f"gate-fail: {summary['n_gate_fail']}  all_gate_pass: {summary['all_gate_pass']}")
    print(f"summary: {args.summary_path}")
    return 0 if all_gate_pass else 1


if __name__ == "__main__":
    sys.exit(main())
