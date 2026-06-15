#!/usr/bin/env python3
"""
generate_items.py — TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1

Deterministically materializes the 72-item set per the locked preregistration §4.
Fixed seed; same input → same bytes. Output: items_materialized.json (committed
+ hashed BEFORE any model run, per §11 provenance precondition #1).
"""
from __future__ import annotations

import json
import random
from pathlib import Path

# ── Locked design (per preregistration §3, §4) ─────────────────────────────────
SEED         = 20260615      # date-based fixed seed
N_PER_CELL   = 12
K_VALUES     = [1, 3, 5]
POSITIONS    = ["EARLY", "LATE"]   # target hop2 fact placed in first or last third of fact block


def gen_token(rng: random.Random, prefix: str, used: set[str]) -> str:
    """Generate a fresh 5-letter uppercase token with given prefix, rejecting
    any that collides with `used`. Adds the new token to `used`."""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    suffix_len = 5 - len(prefix)
    assert suffix_len >= 1
    while True:
        token = prefix + "".join(rng.choice(chars) for _ in range(suffix_len))
        # Reject tokens that look like role-marked target tokens unless this IS
        # a target-A or target-B draw (callers control via prefix).
        if not prefix.startswith("Z") and (token.startswith("ZA") or token.startswith("ZB")):
            continue
        if token not in used:
            used.add(token)
            return token


def gen_chain(rng: random.Random, used: set[str], is_target: bool) -> dict:
    """Generate one chain (A → B → C). Target chain forces ZA*/ZB* prefixes for
    A and B; decoy chains use pure-random tokens (with the rule above forbidding
    accidental ZA*/ZB* in non-target roles)."""
    if is_target:
        A = gen_token(rng, "ZA", used)
        B = gen_token(rng, "ZB", used)
    else:
        A = gen_token(rng, "", used)
        B = gen_token(rng, "", used)
    C = gen_token(rng, "", used)
    return {"A": A, "B": B, "C": C}


def gen_holds_facts(rng: random.Random, used: set[str]) -> list[dict]:
    """Generate two 'W holds V' distractor facts (the distinguishability floor
    per §7 — never removed in any cell)."""
    out = []
    for _ in range(2):
        W = gen_token(rng, "", used)
        V = gen_token(rng, "", used)
        out.append({"W": W, "V": V})
    return out


def build_facts(target: dict, decoys: list[dict], holds: list[dict]) -> list[dict]:
    facts = []
    facts.append({"chain": "target", "role": "hop1",
                  "text": f"{target['A']} links to {target['B']}.",
                  "is_target_hop2": False})
    facts.append({"chain": "target", "role": "hop2",
                  "text": f"{target['B']} maps to {target['C']}.",
                  "is_target_hop2": True})
    for i, d in enumerate(decoys, start=1):
        facts.append({"chain": f"decoy_{i}", "role": "hop1",
                      "text": f"{d['A']} links to {d['B']}.",
                      "is_target_hop2": False})
        facts.append({"chain": f"decoy_{i}", "role": "hop2",
                      "text": f"{d['B']} maps to {d['C']}.",
                      "is_target_hop2": False})
    for h in holds:
        facts.append({"chain": "holds", "role": "holds",
                      "text": f"{h['W']} holds {h['V']}.",
                      "is_target_hop2": False})
    return facts


def order_facts(rng: random.Random, facts: list[dict], position: str) -> list[dict]:
    """Shuffle all non-target-hop2 facts, then insert the target hop2 fact into
    the first third (EARLY) or last third (LATE) of the fact block."""
    target_hop2 = [f for f in facts if f["is_target_hop2"]]
    others      = [f for f in facts if not f["is_target_hop2"]]
    assert len(target_hop2) == 1
    rng.shuffle(others)

    n_total = len(facts)
    first_third_end = max(1, n_total // 3)
    last_third_start = n_total - first_third_end

    if position == "EARLY":
        insert_at = rng.randint(0, first_third_end - 1)
    elif position == "LATE":
        insert_at = rng.randint(last_third_start, n_total - 1)
    else:
        raise ValueError(f"unknown position: {position}")

    ordered = list(others)
    ordered.insert(insert_at, target_hop2[0])
    return ordered


def generate_item(rng: random.Random, item_id: str, k: int, position: str) -> dict:
    used: set[str] = set()
    chains = [gen_chain(rng, used, is_target=(i == 0)) for i in range(k)]
    target = chains[0]
    decoys = chains[1:]
    holds = gen_holds_facts(rng, used)
    raw_facts = build_facts(target, decoys, holds)
    ordered_facts = order_facts(rng, raw_facts, position)

    # Determine where the target hop2 fact landed (for provenance + classifier metadata).
    target_hop2_index = next(
        i for i, f in enumerate(ordered_facts) if f["is_target_hop2"]
    )

    return {
        "item_id":          item_id,
        "cell":             f"k{k}_{position}",
        "k":                k,
        "position":         position,
        "target_chain":     target,
        "decoy_chains":     decoys,
        "holds":            holds,
        "all_terminals":    sorted({c["C"] for c in chains}),
        "all_intermediates": sorted({c["B"] for c in chains}),
        "ordered_facts":    [
            {"position_index": i + 1, "chain": f["chain"], "role": f["role"], "text": f["text"]}
            for i, f in enumerate(ordered_facts)
        ],
        "target_hop2_position_index": target_hop2_index + 1,
        "n_facts":          len(ordered_facts),
        "queries": {
            "hop1":      {"query_anchor": target["A"], "expected_answer": target["B"], "verb": "links to"},
            "hop2":      {"query_anchor": target["B"], "expected_answer": target["C"], "verb": "maps to"},
            "composite": {"query_anchor": target["A"], "expected_answer": target["C"], "verb": "composite"},
        },
    }


def main() -> int:
    rng = random.Random(SEED)
    items = []
    for k in K_VALUES:
        for position in POSITIONS:
            for n in range(N_PER_CELL):
                item_id = f"tabs_v01_k{k}_{position[0]}_{n+1:02d}"
                items.append(generate_item(rng, item_id, k, position))

    out_path = Path(__file__).parent / "items_materialized.json"
    out_path.write_text(json.dumps(items, indent=2) + "\n")

    # Summary
    by_cell = {}
    for it in items:
        by_cell.setdefault(it["cell"], 0)
        by_cell[it["cell"]] += 1
    print(f"Generated {len(items)} items @ seed {SEED} -> {out_path}")
    for cell, count in sorted(by_cell.items()):
        print(f"  cell {cell}: {count} items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
