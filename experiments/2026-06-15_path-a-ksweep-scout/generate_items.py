#!/usr/bin/env python3
"""
generate_items.py -- Path A K-Sweep Scout item generator (K-parameterized).

Per the LOCKED PREREGISTRATION v1.0 (sha 248581f6...) + Manager by-name run
authorization 2026-06-15, this script materializes n=96-item construction
sets for each K-cell (K = 1, 2, 3, 4, 5) deterministically from per-cell
seeds (SEED.json). NO MODEL EXECUTION here.

Behaves identically to the closed K=5 run's generate_items.py except:
  - K (decoy-chain count) is per-cell-parameterized, read from CLI arg.
  - Per-cell seed is read from SEED.json["per_cell_seeds"]["K{K}"].
  - construction_spec carries `_sweep_mode: true` + `_sweep_locked_K_list:
    [1,2,3,4,5]` so the inspector validates in SWEEP mode (C9 mode='sweep').
  - Output filenames carry the K suffix (items_materialized_K{K}.json, etc.).

K=5 reproduction property: with seed 20260615 and K=5, the rng draws traverse
the exact same path as the closed K=5 run's generator, so items_materialized_K5.json
contains byte-identical per-item entity sets (items[]) compared to that run's
items_materialized.json. Top-level wrapper differs (run-name + seed slot) but
items[] -- the load-bearing field -- is identical. Downstream FP16 outputs
must therefore reproduce 18/96 validated-R1 byte-exactly.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from pathlib import Path

# Import Manager-locked constants (single source of truth for D, P, M_MIN, MARGIN,
# N; we override only K per cell).
REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "path-a" / "inspector"))
import constants  # noqa: E402

D = constants.D_DEPTH_COMPETITORS                   # 5  (NOT swept)
P = constants.P_POSITION_SLOTS                      # 5
M_MIN = constants.M_MIN_EQUAL_SALIENCE_CANDIDATES   # 10
N = constants.N_ITEMS_PER_CELL                      # 96
MARGIN = constants.MARGIN                           # 0.25
LOCKED_K_LIST = [1, 2, 3, 4, 5]                     # per prereg v1.0 §2

# Relations (locked here; queried path uses r1, r2)
R1 = "links_to"
R2 = "maps_to"
POST_C_REL = "leads_to"

# Competitor relations (D=5)
COMPETITOR_HEAD_RELS = ["sA_head", "sB_head", "sC_head", "sD_head", "sE_head"]
COMPETITOR_TAIL_RELS = ["sA_tail", "sB_tail", "sC_tail", "sD_tail", "sE_tail"]

HOLDS_REL = "holds"

_TOKEN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_TOKEN_SUFFIX_LEN = 4


def gen_token(rng: random.Random, prefix: str, used: set[str]) -> str:
    while True:
        tok = prefix + "".join(rng.choice(_TOKEN_ALPHABET) for _ in range(_TOKEN_SUFFIX_LEN))
        if tok not in used:
            used.add(tok)
            return tok


def generate_item(rng: random.Random, item_id: str, K_cell: int) -> dict:
    used: set[str] = set()

    # Target chain
    A      = gen_token(rng, "tA_", used)
    B      = gen_token(rng, "tB_", used)
    C_star = gen_token(rng, "tC_", used)
    T      = gen_token(rng, "tT_", used)

    # Same-depth competitors (D=5, unchanged across cells)
    competitors = []
    for i in range(D):
        competitors.append({
            "head_relation":   COMPETITOR_HEAD_RELS[i],
            "B_competitor":    gen_token(rng, f"cB{i+1}_", used),
            "second_relation": COMPETITOR_TAIL_RELS[i],
            "X":               gen_token(rng, f"cX{i+1}_", used),
        })

    # Decoy chains -- K_cell varies per cell
    decoys = []
    for i in range(K_cell):
        decoys.append({
            "head":   gen_token(rng, f"dA{i+1}_", used),
            "bridge": gen_token(rng, f"dB{i+1}_", used),
            "answer": gen_token(rng, f"dC{i+1}_", used),
            "T_i":    gen_token(rng, f"dT{i+1}_", used),
        })

    # Holds facts (2)
    holds = []
    for _ in range(2):
        holds.append({
            "W": gen_token(rng, "hW_", used),
            "V": gen_token(rng, "hV_", used),
        })

    filler_W = gen_token(rng, "fW_", used)
    filler_V = gen_token(rng, "fV_", used)

    position_slot = rng.randint(1, P)

    target_facts = [
        {"subject": A,      "relation": R1,         "object": B,      "role": "target_hop1"},
        {"subject": B,      "relation": R2,         "object": C_star, "role": "target_hop2"},
        {"subject": C_star, "relation": POST_C_REL, "object": T,      "role": "target_post_C_to_T"},
    ]
    competitor_facts = []
    for i, c in enumerate(competitors):
        competitor_facts.append({"subject": A,                  "relation": c["head_relation"],   "object": c["B_competitor"], "role": f"competitor_{i+1}_head"})
        competitor_facts.append({"subject": c["B_competitor"],  "relation": c["second_relation"], "object": c["X"],            "role": f"competitor_{i+1}_tail"})
    decoy_facts = []
    for i, d in enumerate(decoys):
        decoy_facts.append({"subject": d["head"],   "relation": R1,         "object": d["bridge"], "role": f"decoy_{i+1}_hop1"})
        decoy_facts.append({"subject": d["bridge"], "relation": R2,         "object": d["answer"], "role": f"decoy_{i+1}_hop2"})
        decoy_facts.append({"subject": d["answer"], "relation": POST_C_REL, "object": d["T_i"],    "role": f"decoy_{i+1}_post_to_T_i"})
    holds_facts = [
        {"subject": h["W"], "relation": HOLDS_REL, "object": h["V"], "role": f"holds_{i+1}"}
        for i, h in enumerate(holds)
    ]
    canonical_facts = target_facts + competitor_facts + decoy_facts + holds_facts

    return {
        "item_id":          item_id,
        "position_slot":    position_slot,
        "target":           {"A": A, "B": B, "C_star": C_star, "T": T,
                              "r1": R1, "r2": R2, "post_C_star_relations": [POST_C_REL]},
        "depth_2_competitors": competitors,
        "decoy_chains":     decoys,
        "holds_facts":      holds,
        "direct_query_filler": {"W": filler_W, "V": filler_V},
        "canonical_facts":  canonical_facts,
        "n_canonical_facts": len(canonical_facts),
        "queries": {
            "composite":    {"query_anchor": A, "expected_answer": C_star,
                             "question_template": "{anchor} links to something, which maps to what?"},
            "hop1":         {"query_anchor": A, "expected_answer": B,
                             "question_template": "{anchor} links to what?"},
            "hop2":         {"query_anchor": B, "expected_answer": C_star,
                             "question_template": "{anchor} maps to what?"},
            "direct_query": {"query_anchor": A, "expected_answer": "NULL",
                             "question_template": "{anchor} links to something, which maps to what?"},
        },
    }


def per_item_conformance(item: dict) -> dict:
    failures: list[str] = []
    t = item["target"]

    decoy_terminals = {d["T_i"] for d in item["decoy_chains"]}
    if t["C_star"] == t["T"]:
        failures.append("C1_C_star_equals_target_T")
    if t["C_star"] in decoy_terminals:
        failures.append("C1_C_star_in_decoy_terminals")

    all_tokens = [t["A"], t["B"], t["C_star"], t["T"]]
    for d in item["decoy_chains"]:
        all_tokens += [d["head"], d["bridge"], d["answer"], d["T_i"]]
    for c in item["depth_2_competitors"]:
        all_tokens += [c["B_competitor"], c["X"]]
    for h in item["holds_facts"]:
        all_tokens += [h["W"], h["V"]]
    all_tokens += [item["direct_query_filler"]["W"], item["direct_query_filler"]["V"]]
    if len(set(all_tokens)) != len(all_tokens):
        from collections import Counter
        dups = {k: v for k, v in Counter(all_tokens).items() if v > 1}
        failures.append(f"C2_token_duplicates: {dups}")

    X_set = {c["X"] for c in item["depth_2_competitors"]}
    if t["C_star"] in X_set:
        failures.append("C3_C_star_aliased_to_X")
    if t["B"] in {c["B_competitor"] for c in item["depth_2_competitors"]}:
        failures.append("C3_B_aliased_to_B_competitor")

    if t["r1"] in {c["head_relation"] for c in item["depth_2_competitors"]}:
        failures.append("C4_r1_in_competitor_head_relations")

    for qt in ("composite", "hop1", "hop2", "direct_query"):
        if qt not in item["queries"]:
            failures.append(f"C8_missing_query_{qt}")

    return {"item_id": item["item_id"], "passes": len(failures) == 0, "failures": failures}


def assemble_construction_spec(rep_item: dict, K_cell: int) -> dict:
    """Build a single-item-representative construction_spec for inspector
    validation. Carries `_sweep_mode: true` + `_sweep_locked_K_list: [1..5]`
    so the inspector validates with C9 mode='sweep'."""
    t = rep_item["target"]
    head_rels = [t["r1"]] + [c["head_relation"]   for c in rep_item["depth_2_competitors"]]
    tail_rels = [t["r2"]] + [c["second_relation"] for c in rep_item["depth_2_competitors"]]
    frequency = {**{r: 1 for r in head_rels}, **{r: 1 for r in tail_rels}}
    order_positions = {
        **{r: [0] for r in head_rels},
        **{r: [1] for r in tail_rels},
    }

    return {
        "construction_id": f"path_a_ksweep_scout_2026-06-15_K{K_cell}_v1.0",
        "_sweep_mode": True,
        "_sweep_locked_K_list": LOCKED_K_LIST,
        "params": {
            "k":      K_cell,
            "D":      D,
            "p":      P,
            "m":      M_MIN,
            "margin": MARGIN,
        },
        "target": {
            "A":                      t["A"],
            "B":                      t["B"],
            "C_star":                 t["C_star"],
            "T":                      t["T"],
            "r1":                     t["r1"],
            "r2":                     t["r2"],
            "post_C_star_relations":  t["post_C_star_relations"],
        },
        "depth_2_competitors": rep_item["depth_2_competitors"],
        "decoy_chains":        rep_item["decoy_chains"],
        "relation_balance": {
            "frequency":       frequency,
            "order_positions": order_positions,
        },
        "direct_query": {
            "withhold_fact_role":            "B_to_C_star",
            "filler_form":                   "{W} holds {V}",
            "filler_contains_B_or_C_star":   False,
        },
        "contexts": {
            "composite":     {"present_facts": "full"},
            "hop1":          {"context_isolated_from_composite": True},
            "hop2":          {"context_isolated_from_composite": True},
            "direct_query":  {"context_isolated_from_composite": True},
            "load_matched":  True,
        },
    }


def render_facts_block(facts_with_positions: list[dict]) -> str:
    sorted_facts = sorted(facts_with_positions, key=lambda x: x["position_index"])
    return "\n".join(f"{f['subject']} {f['relation']} {f['object']}." for f in sorted_facts)


def position_facts(rng: random.Random, item: dict, withhold_target_hop2: bool = False) -> list[dict]:
    other_facts = [f for f in item["canonical_facts"] if f["role"] != "target_hop2"]
    target_hop2 = [f for f in item["canonical_facts"] if f["role"] == "target_hop2"][0]

    if withhold_target_hop2:
        filler = {
            "subject": item["direct_query_filler"]["W"],
            "relation": HOLDS_REL,
            "object":  item["direct_query_filler"]["V"],
            "role":    "direct_query_filler_for_withheld_bridge",
        }
        replacement = filler
    else:
        replacement = target_hop2

    shuffled = list(other_facts)
    rng.shuffle(shuffled)

    n_facts_total = len(shuffled) + 1
    slot = item["position_slot"]
    quintile_size = n_facts_total // P
    lo = (slot - 1) * quintile_size
    hi = slot * quintile_size if slot < P else n_facts_total
    insert_at = rng.randint(lo, max(lo, hi - 1))

    positioned = []
    for idx, f in enumerate(shuffled):
        positioned.append({**f, "position_index": idx if idx < insert_at else idx + 1})
    positioned.append({**replacement, "position_index": insert_at})
    return positioned


def render_prompt(template: str, facts_block: str, anchor: str, question_template: str) -> str:
    question = question_template.format(anchor=anchor)
    return template.replace("{CONTEXT}", facts_block).replace("{QUERY}", question)


def render_all_contexts(item: dict, template: str, rng: random.Random) -> dict:
    out = {}
    for qt in ("composite", "hop1", "hop2", "direct_query"):
        withhold = (qt == "direct_query")
        facts_positioned = position_facts(rng, item, withhold_target_hop2=withhold)
        facts_block = render_facts_block(facts_positioned)
        q = item["queries"][qt]
        prompt_text = render_prompt(template, facts_block, q["query_anchor"], q["question_template"])
        out[qt] = {
            "query_type":         qt,
            "anchor":             q["query_anchor"],
            "expected_answer":    q["expected_answer"],
            "fact_block_n_lines": len(facts_positioned),
            "prompt":             prompt_text,
            "prompt_sha256":      hashlib.sha256(prompt_text.encode("utf-8")).hexdigest(),
        }
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--K", type=int, required=True, choices=LOCKED_K_LIST,
                    help="K (decoy-chain count) for this cell; must be in locked list [1..5]")
    args = ap.parse_args()
    K_cell = args.K

    here = Path(__file__).resolve().parent
    seed_doc = json.loads((here / "SEED.json").read_text())
    SEED = seed_doc["per_cell_seeds"][f"K{K_cell}"]
    template = (here / "prompt_template.txt").read_text()

    rng = random.Random(SEED)

    print(f"== K-Sweep Scout: K={K_cell}  seed={SEED} ==")
    print(f"Generating {N} items ...")
    items = [generate_item(rng, f"path_a_ksweep_K{K_cell}_item_{i+1:03d}", K_cell) for i in range(N)]

    conformance_results = [per_item_conformance(it) for it in items]
    n_pass = sum(1 for r in conformance_results if r["passes"])
    print(f"per-item conformance: {n_pass}/{N} pass; {N - n_pass} fail")
    if n_pass < N:
        for r in conformance_results:
            if not r["passes"]:
                print(f"  FAIL {r['item_id']}: {r['failures']}")

    spec = assemble_construction_spec(items[0], K_cell)

    print(f"Rendering 4 contexts × {N} items = {4*N} prompts ...")
    rng_render = random.Random(SEED + 1)
    renderings = []
    for it in items:
        renderings.append({
            "item_id":   it["item_id"],
            "contexts":  render_all_contexts(it, template, rng_render),
        })

    items_path   = here / f"items_materialized_K{K_cell}.json"
    spec_path    = here / f"construction_spec_K{K_cell}.json"
    prompts_path = here / f"prompts_rendered_K{K_cell}.json"

    items_path.write_text(
        json.dumps({
            "K_cell":                K_cell,
            "n_items":               len(items),
            "seed":                  SEED,
            "items":                 items,
            "per_item_conformance":  conformance_results,
            "n_conformance_pass":    n_pass,
        }, indent=2) + "\n"
    )
    spec_path.write_text(json.dumps(spec, indent=2) + "\n")
    prompts_path.write_text(
        json.dumps({
            "K_cell":          K_cell,
            "n_items":         len(items),
            "contexts":        ["composite", "hop1", "hop2", "direct_query"],
            "n_prompts_total": 4 * len(items),
            "renderings":      renderings,
        }, indent=2) + "\n"
    )

    print(f"\nWrote (K={K_cell}):")
    for path in (items_path, spec_path, prompts_path):
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        size = path.stat().st_size
        print(f"  {path.name:42s}  sha {sha}  size {size} bytes")
    return 0 if n_pass == N else 1


if __name__ == "__main__":
    raise SystemExit(main())
