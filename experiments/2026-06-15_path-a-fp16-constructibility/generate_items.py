#!/usr/bin/env python3
"""
generate_items.py — Path A item generator (pre-run materialization).

Per TL ACTION 2026-06-15 ("Path A Pre-Run Materialization + Inspector Pass") +
Manager approval, this script materializes the n=96-item Path A construction
deterministically from a fixed seed (SEED.json) using the of-record Manager-
locked values via path-a/inspector/constants.py.

NO MODEL EXECUTION. Static synthetic item generation only. The output supports
the inspector pass and, on subsequent Manager by-name run authorization, the
four-context renderer + a separately-authorized model run.

Schema realized per:
  TARGET-CONSTRUCT-DEFINITION-v0.4 (of-record; sha 4b616afb...)
  PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3 (in-review; sha 38e05460...)
  PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3 (of-record; sha d9bd9b21...)

Per item:
  - Target chain: A —r1→ B —r2→ C*; C* sits as INTERIOR node; chain extends past
    C* via `leads_to` to a salient sink T (terminal ≠ answer per R8.1).
  - D = 5 same-depth competitors at the head (relations s1..s5, all DISJOINT from
    {r1, r2, leads_to}; competitor depth-2 nodes X_i are also interior).
  - k = 5 chain-level decoy chains (head → bridge → answer → T_i sink).
  - 2 holds facts ("W holds V") for the distinguishability floor.
  - 2 separate direct-query filler tokens (W_filler, V_filler) used only when
    the bridge fact is withheld in the direct-query context.
  - Per-item position_slot ∈ {1..5} for where the target hop2 fact ("B maps to C*")
    sits in the shuffled fact block (P=5 layout-diagnostic positions).

Relation balance (E8 binding admissibility property):
  All "head" relations {r1, s1_head, s2_head, s3_head, s4_head, s5_head} appear
  exactly once per item, each at the SAME role-position (slot 0 of their path).
  All "tail" relations {r2, s1_tail, ..., s5_tail} appear exactly once, each at
  slot 1 of their path. Frequencies are equal across competitor and queried
  relations. The decoy-chain relations reuse {r1, r2} per design (decoys mirror
  the target's relational shape so they are structurally indistinguishable
  except by head).
"""
from __future__ import annotations

import hashlib
import json
import random
import sys
from pathlib import Path

# Import Manager-locked constants
REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "path-a" / "inspector"))
import constants  # noqa: E402

# ── Manager-locked values (sanity bound; constants is the source of truth) ──
K = constants.K_DECOY_CHAINS                        # 5
D = constants.D_DEPTH_COMPETITORS                   # 5
P = constants.P_POSITION_SLOTS                      # 5
M_MIN = constants.M_MIN_EQUAL_SALIENCE_CANDIDATES   # 10
N = constants.N_ITEMS_PER_CELL                      # 96
MARGIN = constants.MARGIN                           # 0.25

# Relations (locked here; queried path uses r1, r2)
R1 = "links_to"
R2 = "maps_to"
POST_C_REL = "leads_to"            # off the queried path; reaches the sink T

# Competitor relations (D=5 pairs of head/tail; all DISJOINT from {r1, r2, leads_to})
COMPETITOR_HEAD_RELS = ["sA_head", "sB_head", "sC_head", "sD_head", "sE_head"]
COMPETITOR_TAIL_RELS = ["sA_tail", "sB_tail", "sC_tail", "sD_tail", "sE_tail"]

# Decoy chains use the same relational shape as the target so they are
# structurally indistinguishable except by head (per design v0.3 §2).
# Each decoy chain: head r1 bridge ; bridge r2 answer ; answer leads_to T_i.

# Holds-facts use a distinct relation as filler.
HOLDS_REL = "holds"

# Per-item token-pool sizes the generator must emit unique tokens for:
#   target chain:           A, B, C*, T                              -> 4
#   D depth-2 competitors:  per competitor: B_comp, X                -> 10
#   k decoy chains:         per chain: head, bridge, answer, T_i     -> 20
#   2 holds facts:          per fact: W, V                           -> 4
#   2 direct-query fillers: W_f, V_f                                 -> 2
# Total tokens per item: 40

# ── Token sampling ──────────────────────────────────────────────────────────
_TOKEN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_TOKEN_SUFFIX_LEN = 4  # 4 random letters; 26^4 ≈ 457K unique per prefix


def gen_token(rng: random.Random, prefix: str, used: set[str]) -> str:
    """Generate a fresh prefixed 4-letter-suffix token, rejecting collisions
    within the item. Prefixes are role-mnemonic ("TA_" = target A); they are
    NOT load-bearing for the scorer (which uses token identity)."""
    while True:
        tok = prefix + "".join(rng.choice(_TOKEN_ALPHABET) for _ in range(_TOKEN_SUFFIX_LEN))
        if tok not in used:
            used.add(tok)
            return tok


# ── Single item generator ───────────────────────────────────────────────────
def generate_item(rng: random.Random, item_id: str) -> dict:
    used: set[str] = set()

    # Target chain: A → B → C* → T
    A      = gen_token(rng, "tA_", used)   # head
    B      = gen_token(rng, "tB_", used)   # bridge
    C_star = gen_token(rng, "tC_", used)   # INTERIOR target (not a terminal)
    T      = gen_token(rng, "tT_", used)   # salient sink (terminal ≠ answer per R8.1)

    # Same-depth competitors (D=5) — each at structural depth 2 from A via
    # distinct relations, off the queried r1→r2 path.
    competitors = []
    for i in range(D):
        head_rel = COMPETITOR_HEAD_RELS[i]
        tail_rel = COMPETITOR_TAIL_RELS[i]
        B_comp = gen_token(rng, f"cB{i+1}_", used)
        X      = gen_token(rng, f"cX{i+1}_", used)
        competitors.append({
            "head_relation":   head_rel,
            "B_competitor":    B_comp,
            "second_relation": tail_rel,
            "X":               X,
        })

    # Decoy chains (k=5) — same relational shape, different heads/contents.
    decoys = []
    for i in range(K):
        decoys.append({
            "head":   gen_token(rng, f"dA{i+1}_", used),
            "bridge": gen_token(rng, f"dB{i+1}_", used),
            "answer": gen_token(rng, f"dC{i+1}_", used),
            "T_i":    gen_token(rng, f"dT{i+1}_", used),
        })

    # Holds facts (2 per item — the distinguishability floor; never removed).
    holds = []
    for _ in range(2):
        holds.append({
            "W": gen_token(rng, "hW_", used),
            "V": gen_token(rng, "hV_", used),
        })

    # Direct-query filler tokens (used to replace the withheld bridge fact in
    # the direct-query context; pool disjoint from B and C* and everything else
    # in the item by virtue of used-set rejection).
    filler_W = gen_token(rng, "fW_", used)
    filler_V = gen_token(rng, "fV_", used)

    # Per-item C*-position slot (1..P=5) — layout-diagnostic; not a depth control.
    position_slot = rng.randint(1, P)

    # Build fact lists in canonical (pre-shuffle) order for transparency.
    # Each fact is a triple {subject, relation, object} with a render template
    # "{subject} {relation} {object}." used by the renderer.
    target_facts = [
        {"subject": A,      "relation": R1,         "object": B,      "role": "target_hop1"},
        {"subject": B,      "relation": R2,         "object": C_star, "role": "target_hop2"},
        {"subject": C_star, "relation": POST_C_REL, "object": T,      "role": "target_post_C_to_T"},
    ]
    competitor_facts = []
    for i, c in enumerate(competitors):
        competitor_facts.append({"subject": A,             "relation": c["head_relation"],   "object": c["B_competitor"], "role": f"competitor_{i+1}_head"})
        competitor_facts.append({"subject": c["B_competitor"], "relation": c["second_relation"], "object": c["X"],         "role": f"competitor_{i+1}_tail"})
    decoy_facts = []
    for i, d in enumerate(decoys):
        decoy_facts.append({"subject": d["head"],   "relation": R1,         "object": d["bridge"], "role": f"decoy_{i+1}_hop1"})
        decoy_facts.append({"subject": d["bridge"], "relation": R2,         "object": d["answer"], "role": f"decoy_{i+1}_hop2"})
        decoy_facts.append({"subject": d["answer"], "relation": POST_C_REL, "object": d["T_i"],    "role": f"decoy_{i+1}_post_to_T_i"})
    holds_facts = [
        {"subject": h["W"], "relation": HOLDS_REL, "object": h["V"], "role": f"holds_{i+1}"}
        for i, h in enumerate(holds)
    ]
    # Composite-context full fact list (BEFORE shuffle).
    canonical_facts = target_facts + competitor_facts + decoy_facts + holds_facts
    # Total: 3 + 10 + 15 + 2 = 30 facts.

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


# ── Per-item structural conformance check (post-generation) ─────────────────
def per_item_conformance(item: dict) -> dict:
    """Verify per-item structural invariants the inspector's C1–C4 + C8 expect
    to hold across all 96 items (the inspector's spec-level check covers one
    representative item; this conformance check confirms each item is well-formed)."""
    failures: list[str] = []
    t = item["target"]

    # C1: C* not any terminal (target T or any decoy T_i).
    decoy_terminals = {d["T_i"] for d in item["decoy_chains"]}
    if t["C_star"] == t["T"]:
        failures.append("C1_C_star_equals_target_T")
    if t["C_star"] in decoy_terminals:
        failures.append("C1_C_star_in_decoy_terminals")

    # C2: pairwise distinct across all roles.
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

    # C3: depth-2 competitor tokens distinct from C*/B/T/decoy_terminals.
    X_set = {c["X"] for c in item["depth_2_competitors"]}
    if t["C_star"] in X_set:
        failures.append("C3_C_star_aliased_to_X")
    if t["B"] in {c["B_competitor"] for c in item["depth_2_competitors"]}:
        failures.append("C3_B_aliased_to_B_competitor")

    # C4: r1 edge unique — competitor head relations must be disjoint from r1.
    if t["r1"] in {c["head_relation"] for c in item["depth_2_competitors"]}:
        failures.append("C4_r1_in_competitor_head_relations")

    # C8 (per-item shape): four-context separability — the four query types
    # must each have well-formed queries.
    for qt in ("composite", "hop1", "hop2", "direct_query"):
        if qt not in item["queries"]:
            failures.append(f"C8_missing_query_{qt}")

    return {"item_id": item["item_id"], "passes": len(failures) == 0, "failures": failures}


# ── Construction spec assembler (representative item → spec for inspector) ─
def assemble_construction_spec(rep_item: dict) -> dict:
    """Build a single-item-representative construction_spec.json that the
    path-a/inspector/inspector.py validates schema-side. Real-run mode (no
    `_fixture_mode` flag); Manager-lock binding enforced by C9.

    The representative item's tokens fill the spec's target/competitors/decoys
    sections. Per-item structural checks on the other 95 items are performed
    by per_item_conformance() and reported alongside."""
    t = rep_item["target"]
    # Build the relation_balance block.
    head_rels = [t["r1"]] + [c["head_relation"]   for c in rep_item["depth_2_competitors"]]
    tail_rels = [t["r2"]] + [c["second_relation"] for c in rep_item["depth_2_competitors"]]
    frequency = {**{r: 1 for r in head_rels}, **{r: 1 for r in tail_rels}}
    order_positions = {
        **{r: [0] for r in head_rels},   # head relations at slot 0 of their path
        **{r: [1] for r in tail_rels},   # tail relations at slot 1
    }

    return {
        "construction_id": "path_a_constructibility_2026-06-15_v0.1",
        "params": {
            "k":      K,
            "D":      D,
            "p":      P,
            "m":      M_MIN,            # equal-salience candidate count
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
        # No `_fixture_mode` key -> real-run mode; inspector C9 will enforce.
    }


# ── Prompt renderer (per-item, per-context) ─────────────────────────────────
def render_facts_block(facts_with_positions: list[dict]) -> str:
    """Render shuffled+positioned facts as the prompt's {CONTEXT} block."""
    sorted_facts = sorted(facts_with_positions, key=lambda x: x["position_index"])
    return "\n".join(f"{f['subject']} {f['relation']} {f['object']}." for f in sorted_facts)


def position_facts(rng: random.Random, item: dict, withhold_target_hop2: bool = False) -> list[dict]:
    """Shuffle the item's facts and place the target hop2 fact at the
    item's per-item position_slot (1..P) — quintile-mapped into the fact block.
    If withhold_target_hop2=True, replace it with a neutral length-matched
    'filler_W holds filler_V.' fact (used for direct-query context)."""
    other_facts = [f for f in item["canonical_facts"] if f["role"] != "target_hop2"]
    target_hop2 = [f for f in item["canonical_facts"] if f["role"] == "target_hop2"][0]

    if withhold_target_hop2:
        # Replace the bridge fact with a neutral, length-matched filler ("W holds V.").
        filler = {
            "subject": item["direct_query_filler"]["W"],
            "relation": HOLDS_REL,
            "object":  item["direct_query_filler"]["V"],
            "role":    "direct_query_filler_for_withheld_bridge",
        }
        replacement = filler
    else:
        replacement = target_hop2

    # Shuffle the non-target-hop2 facts deterministically (rng is item-local).
    shuffled = list(other_facts)
    rng.shuffle(shuffled)

    # Map position_slot ∈ {1..P} → fact-block insertion index.
    # n_facts = len(shuffled) + 1; split into P equal quintiles; pick a position
    # within the corresponding quintile.
    n_facts_total = len(shuffled) + 1
    slot = item["position_slot"]
    quintile_size = n_facts_total // P  # integer division; e.g., 31 // 5 = 6
    lo = (slot - 1) * quintile_size
    hi = slot * quintile_size if slot < P else n_facts_total  # last slot extends to end
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
    """Render the four context prompts for one item. Each context uses its own
    fact ordering (separate clutter-matched contexts per R7 of v0.4)."""
    out = {}
    for qt in ("composite", "hop1", "hop2", "direct_query"):
        # Per the prereg, each context is a SEPARATE generation with its own
        # fact ordering. We use independent RNG draws by passing the same rng;
        # the draws stay deterministic (seed-bound). Composite is rendered first;
        # the order of rendering does not affect output (model isn't run here).
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


# ── Driver ──────────────────────────────────────────────────────────────────
def main() -> int:
    here = Path(__file__).resolve().parent
    seed_doc = json.loads((here / "SEED.json").read_text())
    SEED = seed_doc["seed"]
    template = (here / "prompt_template.txt").read_text()

    rng = random.Random(SEED)

    print(f"Generating {N} items at seed {SEED} ...")
    items = [generate_item(rng, f"path_a_item_{i+1:03d}") for i in range(N)]

    # Per-item conformance check.
    conformance_results = [per_item_conformance(it) for it in items]
    n_pass = sum(1 for r in conformance_results if r["passes"])
    print(f"per-item conformance: {n_pass}/{N} pass; {N - n_pass} fail")
    if n_pass < N:
        for r in conformance_results:
            if not r["passes"]:
                print(f"  FAIL {r['item_id']}: {r['failures']}")

    # Construction spec (representative = item 0).
    spec = assemble_construction_spec(items[0])

    # Prompt renderings (4 contexts × 96 items = 384 prompts).
    print(f"Rendering 4 contexts × {N} items = {4*N} prompts ...")
    rng_render = random.Random(SEED + 1)  # separate stream for layout/position decisions
    renderings = []
    for it in items:
        renderings.append({
            "item_id":   it["item_id"],
            "contexts":  render_all_contexts(it, template, rng_render),
        })

    # Write outputs (deterministic JSON ordering).
    (here / "items_materialized.json").write_text(
        json.dumps({
            "n_items":               len(items),
            "seed":                  SEED,
            "items":                 items,
            "per_item_conformance":  conformance_results,
            "n_conformance_pass":    n_pass,
        }, indent=2) + "\n"
    )
    (here / "construction_spec.json").write_text(json.dumps(spec, indent=2) + "\n")
    (here / "prompts_rendered.json").write_text(
        json.dumps({
            "n_items":         len(items),
            "contexts":        ["composite", "hop1", "hop2", "direct_query"],
            "n_prompts_total": 4 * len(items),
            "renderings":      renderings,
        }, indent=2) + "\n"
    )

    print(f"\nWrote:")
    for name in ("items_materialized.json", "construction_spec.json", "prompts_rendered.json"):
        path = here / name
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        size = path.stat().st_size
        print(f"  {name:32s}  sha {sha}  size {size} bytes")
    return 0 if n_pass == N else 1


if __name__ == "__main__":
    raise SystemExit(main())
