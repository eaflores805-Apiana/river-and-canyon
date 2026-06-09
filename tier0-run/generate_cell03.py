"""
Stage 1 cell generation script — Two-Hop Level 1 Cell 03
Generates items_twohop_l1_cell03.json

Authorization: Manager / Team Lead memo "Authorized — Construct Cell03 Manifest Only"
2026-06-08

Primary axis:  adjacency / proximity between target chain hop1 and hop2 facts.
  Cell02: target hop1 (pos 5) and hop2 (pos 6) adjacent.
  Cell03: neighbor fact (fl holds cn) interposed between target hop1 and hop2 in all items.

Control repairs (not tested axes — required to prevent re-introduction of Cell02 confounds):
  ct C-rank balanced:       8 items each at rank 1 (first_C), rank 2 (second_C),
                            rank 3 (third_C = last_C).
  ct absolute position:     pos 3 (Group A), pos 5 (Group B), pos 7 (Group C).

Context arrangements (3 groups x 8 items each):

  Group A — ct rank 1 (first_C, pos 3), items 1-8:
    pos 1: target_chain  hop1_fact         (at  links to bt)
    pos 2: neighbor_context neighbor_decoy_fact  (fl  holds   cn)   <- interposed
    pos 3: target_chain  hop2_fact         (bt  maps to  ct)        <- ct pos 3 (first_C)
    pos 4: decoy_chain_1 decoy_hop1_fact   (ad1 links to bd1)
    pos 5: decoy_chain_1 decoy_hop2_fact   (bd1 maps to  cd1)      <- cd1 pos 5 (second_C)
    pos 6: decoy_chain_2 decoy_hop1_fact   (ad2 links to bd2)
    pos 7: decoy_chain_2 decoy_hop2_fact   (bd2 maps to  cd2)      <- cd2 pos 7 (third_C)
    c_by_pos = [ct(3), cd1(5), cd2(7)]  first_C = ct

  Group B — ct rank 2 (second_C, pos 5), items 9-16:
    pos 1: decoy_chain_1 decoy_hop1_fact   (ad1 links to bd1)
    pos 2: decoy_chain_1 decoy_hop2_fact   (bd1 maps to  cd1)      <- cd1 pos 2 (first_C)
    pos 3: target_chain  hop1_fact         (at  links to bt)
    pos 4: neighbor_context neighbor_decoy_fact  (fl  holds   cn)   <- interposed
    pos 5: target_chain  hop2_fact         (bt  maps to  ct)        <- ct pos 5 (second_C)
    pos 6: decoy_chain_2 decoy_hop1_fact   (ad2 links to bd2)
    pos 7: decoy_chain_2 decoy_hop2_fact   (bd2 maps to  cd2)      <- cd2 pos 7 (third_C)
    c_by_pos = [cd1(2), ct(5), cd2(7)]  second_C = ct

  Group C — ct rank 3 = last_C (pos 7), items 17-24:
    pos 1: decoy_chain_1 decoy_hop1_fact   (ad1 links to bd1)
    pos 2: decoy_chain_1 decoy_hop2_fact   (bd1 maps to  cd1)      <- cd1 pos 2 (first_C)
    pos 3: decoy_chain_2 decoy_hop1_fact   (ad2 links to bd2)
    pos 4: decoy_chain_2 decoy_hop2_fact   (bd2 maps to  cd2)      <- cd2 pos 4 (second_C)
    pos 5: target_chain  hop1_fact         (at  links to bt)
    pos 6: neighbor_context neighbor_decoy_fact  (fl  holds   cn)   <- interposed
    pos 7: target_chain  hop2_fact         (bt  maps to  ct)        <- ct pos 7 (third_C=last_C)
    c_by_pos = [cd1(2), cd2(4), ct(7)]  third_C = last_C = ct

Gate 5 precheck (by design, each rank dummy scores exactly 8/24):
  always_return_first_C:  8/24 (Group A) <= 9/24 ceiling
  always_return_second_C: 8/24 (Group B) <= 9/24 ceiling
  always_return_third_C:  8/24 (Group C) <= 9/24 ceiling
  always_return_last_C:   8/24 (Group C) <= 9/24 ceiling
  max_det = 8/24 = 0.333 <= 9/24 = 0.375 -> Gate 5 PASS

Frozen from Cell01/Cell02:
  relations, context_length (7 facts), chains_per_item (3),
  prompt template, scorer (sha256:b65c6803...), validator,
  thresholds, query wording, decoding settings.

No model inference is performed by this script.
"""

import hashlib
import itertools
import json
import os
import string
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tasks_twohop_l1 import (
    validate_manifest, compute_context_hash,
    levenshtein, trigram_jaccard,
    ROLE_ANSWER_C, ROLE_HOP1_B, ROLE_ANCHOR_A,
    ROLE_TARGET_NEIGHBOR_DECOY, ROLE_DISTRACTOR_CHAIN_ENDPOINT,
    ROLE_DISTRACTOR_CHAIN_INTERMEDIATE, ROLE_INERT_FILLER,
    ROLE_OTHER_CONTEXT,
)

import random

# ── Tokenizer ─────────────────────────────────────────────────────────────────
def _load_tokenizer_data():
    hf_cache = Path(os.environ.get(
        "HF_HOME", Path.home() / ".cache" / "huggingface" / "hub"))
    fp16_path = None
    for candidate in hf_cache.rglob("tokenizer.json"):
        if "Qwen2.5-3B-Instruct" in str(candidate) and "mlx" not in str(candidate):
            fp16_path = candidate
            break
    if fp16_path is not None and fp16_path.exists():
        data = json.loads(fp16_path.read_bytes())
        h = "sha256:" + hashlib.sha256(fp16_path.read_bytes()).hexdigest()
        print(f"  Tokenizer: {fp16_path}")
        print(f"  Tokenizer hash: {h}")
    else:
        fallback = Path("Qwen2.5-3B-Instruct-mlx-int4/tokenizer.json")
        data = json.loads(fallback.read_bytes())
        h = "sha256:" + hashlib.sha256(fallback.read_bytes()).hexdigest()
        print(f"  Tokenizer: {fallback} (INT4 fallback - confirmed equivalent by normalization)")
        print(f"  Tokenizer hash: {h}")
    return data, h


print("Loading tokenizer...")
tok_data, _tok_hash_used = _load_tokenizer_data()
vocab  = tok_data["model"]["vocab"]
merges = tok_data["model"]["merges"]
merge_ranks = {}
for idx, m in enumerate(merges):
    pair = (m[0], m[1]) if isinstance(m, list) else tuple(m.split(" ", 1))
    merge_ranks[pair] = idx


def bpe(word):
    toks = list(word)
    while True:
        if len(toks) < 2:
            break
        pairs = [(toks[i], toks[i + 1]) for i in range(len(toks) - 1)]
        best = min((merge_ranks.get(p, float("inf")), p) for p in pairs)
        if best[0] == float("inf"):
            break
        a, b = best[1]
        merged, i = [], 0
        while i < len(toks):
            if i < len(toks) - 1 and toks[i] == a and toks[i + 1] == b:
                merged.append(a + b)
                i += 2
            else:
                merged.append(toks[i])
                i += 1
        toks = merged
    return toks


def bjac(a, b):
    sa, sb = set(bpe(a)), set(bpe(b))
    u = len(sa | sb)
    return round(len(sa & sb) / u, 4) if u else 0.0


def rt_ok(tok):
    return all(vocab.get(s) is not None for s in bpe(tok))


lev  = levenshtein
tjac = trigram_jaccard

# ── Phase 1: Find 24 globally-compatible (C_target, C_neighbor) pairs ─────────
RNG = random.Random(20260615)
L   = string.ascii_uppercase

print("\nPhase 1: Generating candidate C_target pool...")


def tok_compatible(new_tok, existing_set):
    for e in existing_set:
        if lev(new_tok, e) <= 2:
            return False
        if tjac(new_tok, e) >= 0.20:
            return False
    return True


CANDIDATE_POOL_SIZE = 300
candidate_pool = []
attempts = 0
while len(candidate_pool) < CANDIDATE_POOL_SIZE and attempts < 500000:
    tok = "".join(RNG.choices(L, k=5))
    attempts += 1
    if not rt_ok(tok):
        continue
    if not tok_compatible(tok, set(candidate_pool)):
        continue
    candidate_pool.append(tok)

print(f"  Candidate pool: {len(candidate_pool)} tokens ({attempts} attempts)")

print("  Building near-miss pair index...")
pair_index = {}
for ct_cand in candidate_pool:
    partners = []
    for pos in range(5):
        for ch in L:
            if ch == ct_cand[pos]:
                continue
            cand = ct_cand[:pos] + ch + ct_cand[pos + 1:]
            if not rt_ok(cand):
                continue
            lv = lev(ct_cand, cand)
            bv = bjac(ct_cand, cand)
            tv = tjac(ct_cand, cand)
            if lv <= 2 and bv >= 0.40 and tv >= 0.20:
                partners.append(cand)
    for p1, p2 in itertools.combinations(range(5), 2):
        for ch1 in L:
            if ch1 == ct_cand[p1]:
                continue
            for ch2 in L:
                if ch2 == ct_cand[p2]:
                    continue
                cand = list(ct_cand)
                cand[p1] = ch1
                cand[p2] = ch2
                cand = "".join(cand)
                if not rt_ok(cand):
                    continue
                lv = lev(ct_cand, cand)
                bv = bjac(ct_cand, cand)
                tv = tjac(ct_cand, cand)
                if lv <= 2 and bv >= 0.40 and tv >= 0.20:
                    partners.append(cand)
    pair_index[ct_cand] = list(set(partners))

print("  Greedy selection of 24 globally-compatible (C_target, C_neighbor) pairs...")
selected_pairs     = []
all_used_tokens    = set()
selected_c_targets = []

for ct_cand in candidate_pool:
    if len(selected_pairs) == 24:
        break
    if not tok_compatible(ct_cand, all_used_tokens):
        continue
    if any(bjac(ct_cand, prev) >= 0.40 for prev in selected_c_targets):
        continue
    others = all_used_tokens - {ct_cand}
    chosen_cn = None
    for cn_cand in pair_index.get(ct_cand, []):
        if cn_cand in all_used_tokens:
            continue
        if tok_compatible(cn_cand, others):
            chosen_cn = cn_cand
            break
    if chosen_cn is None:
        continue
    selected_pairs.append((ct_cand, chosen_cn))
    all_used_tokens.add(ct_cand)
    all_used_tokens.add(chosen_cn)
    selected_c_targets.append(ct_cand)

if len(selected_pairs) < 24:
    print(f"FATAL: only found {len(selected_pairs)} pairs.")
    sys.exit(1)

print(f"  Found {len(selected_pairs)} pairs.")
for i, (ct_tok, cn_tok) in enumerate(selected_pairs):
    print(f"  [{i + 1:02d}] {ct_tok} / {cn_tok}  "
          f"lev={lev(ct_tok, cn_tok)} bjac={bjac(ct_tok, cn_tok)} tjac={tjac(ct_tok, cn_tok)}")

# ── Phase 2: Assign C_decoy_1 and C_decoy_2 ──────────────────────────────────
C_TARGETS   = [p[0] for p in selected_pairs]
C_NEIGHBORS = {p[0]: p[1] for p in selected_pairs}
C_DECOYS_1  = [C_TARGETS[(i + 8)  % 24] for i in range(24)]
C_DECOYS_2  = [C_TARGETS[(i + 16) % 24] for i in range(24)]

print("\nVerifying C_decoy compatibility (bjac < 0.40, lev > 2):")
decoy_ok = True
for i in range(24):
    for label, cd in (("cd1", C_DECOYS_1[i]), ("cd2", C_DECOYS_2[i])):
        bv = bjac(C_TARGETS[i], cd)
        lv = lev(C_TARGETS[i], cd)
        if bv >= 0.40 or lv <= 2:
            print(f"  VIOLATION item {i+1}: ct={C_TARGETS[i]} {label}={cd} lev={lv} bjac={bv}")
            decoy_ok = False
    bv12 = bjac(C_DECOYS_1[i], C_DECOYS_2[i])
    lv12 = lev(C_DECOYS_1[i], C_DECOYS_2[i])
    if bv12 >= 0.40 or lv12 <= 2:
        print(f"  VIOLATION item {i+1}: cd1={C_DECOYS_1[i]} cd2={C_DECOYS_2[i]} lev={lv12} bjac={bv12}")
        decoy_ok = False
if decoy_ok:
    print("  All OK.")

# ── Phase 3: Generate non-C-role tokens ───────────────────────────────────────
ALL_C_ROLE = set(C_TARGETS) | set(C_NEIGHBORS.values())


def gen_pool(n, prefix, existing):
    pool, combined = [], set(existing)
    att = 0
    while len(pool) < n:
        rest = "".join(RNG.choices(L, k=5 - len(prefix)))
        tok = prefix + rest
        att += 1
        if att > 300000:
            raise RuntimeError(f"Pool exhaustion (prefix={prefix}, needed={n}, got={len(pool)})")
        if not rt_ok(tok):
            continue
        if not tok_compatible(tok, combined):
            continue
        pool.append(tok)
        combined.add(tok)
        att = 0
    return pool


print("\nPhase 3: Generating non-C-role token pools...")
base = set(ALL_C_ROLE)
a_targets  = gen_pool(24, "ZA", base); base |= set(a_targets)
print(f"  A_target:   {a_targets[:3]}...")
a_decoys_1 = gen_pool(24, "ZD", base); base |= set(a_decoys_1)
print(f"  A_decoy_1:  {a_decoys_1[:3]}...")
b_targets  = gen_pool(24, "ZB", base); base |= set(b_targets)
print(f"  B_target:   {b_targets[:3]}...")
b_decoys_1 = gen_pool(24, "ZE", base); base |= set(b_decoys_1)
print(f"  B_decoy_1:  {b_decoys_1[:3]}...")
fillers    = gen_pool(24, "ZF", base); base |= set(fillers)
print(f"  Filler:     {fillers[:3]}...")
a_decoys_2 = gen_pool(24, "ZG", base); base |= set(a_decoys_2)
print(f"  A_decoy_2:  {a_decoys_2[:3]}...")
b_decoys_2 = gen_pool(24, "ZH", base); base |= set(b_decoys_2)
print(f"  B_decoy_2:  {b_decoys_2[:3]}...")

# ── Phase 4: Full token-pool audit ────────────────────────────────────────────
all_unique_tokens = list(set(
    C_TARGETS + list(C_NEIGHBORS.values())
    + a_targets + a_decoys_1 + a_decoys_2
    + b_targets + b_decoys_1 + b_decoys_2
    + fillers
))
declared = {(C_TARGETS[i], C_NEIGHBORS[C_TARGETS[i]]) for i in range(24)}
declared |= {(v, k) for k, v in C_NEIGHBORS.items()}
c_role_set = set(C_TARGETS)

n_pairs = len(list(itertools.combinations(all_unique_tokens, 2)))
print(f"\nPhase 4: Full audit over {len(all_unique_tokens)} tokens ({n_pairs} pairs)...")

lev_v, trig_v, bpe_v = [], [], []
for a, b in itertools.combinations(all_unique_tokens, 2):
    is_decl = (a, b) in declared
    lv = lev(a, b)
    tv = tjac(a, b)
    if lv <= 2 and not is_decl:
        lev_v.append((a, b, lv))
    if tv >= 0.20 and not is_decl:
        trig_v.append((a, b, tv))
    if a in c_role_set and b in c_role_set and not is_decl:
        bv = bjac(a, b)
        if bv >= 0.40:
            bpe_v.append((a, b, bv))

print(f"  Lev violations  (<=2, undeclared):           {len(lev_v)}")
print(f"  Trig violations (>=0.20, undeclared):        {len(trig_v)}")
print(f"  BPE violations  (C-role, >=0.40, undeclared): {len(bpe_v)}")
for x in lev_v[:5]:  print(f"    LEV  {x}")
for x in trig_v[:5]: print(f"    TRIG {x}")
for x in bpe_v[:5]:  print(f"    BPE  {x}")

if lev_v or trig_v or bpe_v:
    print("FATAL: token pool audit failed.")
    sys.exit(1)
print("  Token pool audit: PASS")

# ── Phase 5: Build items ───────────────────────────────────────────────────────
RELATION_HOP1 = "links to"
RELATION_HOP2 = "maps to"
RELATION_HOLD = "holds"

GROUP_LABELS  = {i: "A" for i in range(8)}
GROUP_LABELS.update({i: "B" for i in range(8, 16)})
GROUP_LABELS.update({i: "C" for i in range(16, 24)})

GROUP_CT_RANKS  = {"A": "first_C",       "B": "second_C",      "C": "third_C_last_C"}
GROUP_CT_POS    = {"A": 3,               "B": 5,               "C": 7}
GROUP_HOP1_POS  = {"A": 1,               "B": 3,               "C": 5}
GROUP_NBR_POS   = {"A": 2,               "B": 4,               "C": 6}


def build_facts_group_a(at, bt, ct, ad1, bd1, cd1, ad2, bd2, cd2, fl, cn):
    return [
        {"fact_id": "f01", "chain_id": "target_chain",     "fact_role": "hop1_fact",
         "text": f"{at} {RELATION_HOP1} {bt}.",  "position_index": 1},
        {"fact_id": "f02", "chain_id": "neighbor_context", "fact_role": "neighbor_decoy_fact",
         "text": f"{fl} {RELATION_HOLD} {cn}.",  "position_index": 2},
        {"fact_id": "f03", "chain_id": "target_chain",     "fact_role": "hop2_fact",
         "text": f"{bt} {RELATION_HOP2} {ct}.",  "position_index": 3},
        {"fact_id": "f04", "chain_id": "decoy_chain_1",    "fact_role": "decoy_hop1_fact",
         "text": f"{ad1} {RELATION_HOP1} {bd1}.", "position_index": 4},
        {"fact_id": "f05", "chain_id": "decoy_chain_1",    "fact_role": "decoy_hop2_fact",
         "text": f"{bd1} {RELATION_HOP2} {cd1}.", "position_index": 5},
        {"fact_id": "f06", "chain_id": "decoy_chain_2",    "fact_role": "decoy_hop1_fact",
         "text": f"{ad2} {RELATION_HOP1} {bd2}.", "position_index": 6},
        {"fact_id": "f07", "chain_id": "decoy_chain_2",    "fact_role": "decoy_hop2_fact",
         "text": f"{bd2} {RELATION_HOP2} {cd2}.", "position_index": 7},
    ]


def build_facts_group_b(at, bt, ct, ad1, bd1, cd1, ad2, bd2, cd2, fl, cn):
    return [
        {"fact_id": "f01", "chain_id": "decoy_chain_1",    "fact_role": "decoy_hop1_fact",
         "text": f"{ad1} {RELATION_HOP1} {bd1}.", "position_index": 1},
        {"fact_id": "f02", "chain_id": "decoy_chain_1",    "fact_role": "decoy_hop2_fact",
         "text": f"{bd1} {RELATION_HOP2} {cd1}.", "position_index": 2},
        {"fact_id": "f03", "chain_id": "target_chain",     "fact_role": "hop1_fact",
         "text": f"{at} {RELATION_HOP1} {bt}.",  "position_index": 3},
        {"fact_id": "f04", "chain_id": "neighbor_context", "fact_role": "neighbor_decoy_fact",
         "text": f"{fl} {RELATION_HOLD} {cn}.",  "position_index": 4},
        {"fact_id": "f05", "chain_id": "target_chain",     "fact_role": "hop2_fact",
         "text": f"{bt} {RELATION_HOP2} {ct}.",  "position_index": 5},
        {"fact_id": "f06", "chain_id": "decoy_chain_2",    "fact_role": "decoy_hop1_fact",
         "text": f"{ad2} {RELATION_HOP1} {bd2}.", "position_index": 6},
        {"fact_id": "f07", "chain_id": "decoy_chain_2",    "fact_role": "decoy_hop2_fact",
         "text": f"{bd2} {RELATION_HOP2} {cd2}.", "position_index": 7},
    ]


def build_facts_group_c(at, bt, ct, ad1, bd1, cd1, ad2, bd2, cd2, fl, cn):
    return [
        {"fact_id": "f01", "chain_id": "decoy_chain_1",    "fact_role": "decoy_hop1_fact",
         "text": f"{ad1} {RELATION_HOP1} {bd1}.", "position_index": 1},
        {"fact_id": "f02", "chain_id": "decoy_chain_1",    "fact_role": "decoy_hop2_fact",
         "text": f"{bd1} {RELATION_HOP2} {cd1}.", "position_index": 2},
        {"fact_id": "f03", "chain_id": "decoy_chain_2",    "fact_role": "decoy_hop1_fact",
         "text": f"{ad2} {RELATION_HOP1} {bd2}.", "position_index": 3},
        {"fact_id": "f04", "chain_id": "decoy_chain_2",    "fact_role": "decoy_hop2_fact",
         "text": f"{bd2} {RELATION_HOP2} {cd2}.", "position_index": 4},
        {"fact_id": "f05", "chain_id": "target_chain",     "fact_role": "hop1_fact",
         "text": f"{at} {RELATION_HOP1} {bt}.",  "position_index": 5},
        {"fact_id": "f06", "chain_id": "neighbor_context", "fact_role": "neighbor_decoy_fact",
         "text": f"{fl} {RELATION_HOLD} {cn}.",  "position_index": 6},
        {"fact_id": "f07", "chain_id": "target_chain",     "fact_role": "hop2_fact",
         "text": f"{bt} {RELATION_HOP2} {ct}.",  "position_index": 7},
    ]


GROUP_BUILDERS = {"A": build_facts_group_a, "B": build_facts_group_b, "C": build_facts_group_c}

items = []
for i in range(24):
    n   = i + 1
    grp = GROUP_LABELS[i]
    ct  = C_TARGETS[i];   cn  = C_NEIGHBORS[ct]
    cd1 = C_DECOYS_1[i];  cd2 = C_DECOYS_2[i]
    at  = a_targets[i];   bt  = b_targets[i]
    ad1 = a_decoys_1[i];  bd1 = b_decoys_1[i]
    ad2 = a_decoys_2[i];  bd2 = b_decoys_2[i]
    fl  = fillers[i]
    item_id = f"twohop_l1_c03_i{n:02d}"

    facts    = GROUP_BUILDERS[grp](at, bt, ct, ad1, bd1, cd1, ad2, bd2, cd2, fl, cn)
    ctx      = {"ordered_facts": facts}
    ctx_hash = compute_context_hash({"context": ctx})

    ct_rank  = GROUP_CT_RANKS[grp]
    ct_pos   = GROUP_CT_POS[grp]
    hop1_pos = GROUP_HOP1_POS[grp]
    nbr_pos  = GROUP_NBR_POS[grp]

    item = {
        "item_id": item_id,
        "chains": [
            {"chain_id": "target_chain",  "role": "target",
             "A_object": at,  "B_object": bt,  "C_object": ct},
            {"chain_id": "decoy_chain_1", "role": "decoy",
             "A_object": ad1, "B_object": bd1, "C_object": cd1},
            {"chain_id": "decoy_chain_2", "role": "decoy",
             "A_object": ad2, "B_object": bd2, "C_object": cd2},
        ],
        "object_roles": {
            at:  ROLE_ANCHOR_A,
            bt:  ROLE_HOP1_B,
            ct:  ROLE_ANSWER_C,
            ad1: ROLE_OTHER_CONTEXT,
            bd1: ROLE_DISTRACTOR_CHAIN_INTERMEDIATE,
            cd1: ROLE_DISTRACTOR_CHAIN_ENDPOINT,
            ad2: ROLE_OTHER_CONTEXT,
            bd2: ROLE_DISTRACTOR_CHAIN_INTERMEDIATE,
            cd2: ROLE_DISTRACTOR_CHAIN_ENDPOINT,
            cn:  ROLE_TARGET_NEIGHBOR_DECOY,
            fl:  ROLE_INERT_FILLER,
        },
        "queries": {
            "hop1":           {"query_anchor": at, "expected_answer": bt},
            "hop2":           {"query_anchor": bt, "expected_answer": ct},
            "composite":      {"query_anchor": at, "expected_answer": ct},
            "negative_graph": {"query_anchor": at, "expected_answer": "NULL"},
        },
        "context": ctx,
        "positive_sufficiency_exclusion": {
            "composite_requires_hop1":         True,
            "composite_requires_hop2":         True,
            "answer_from_hop1_alone_possible": False,
            "answer_from_hop2_alone_possible": False,
            "validation_method":               "manifest_structure",
        },
        "same_context_controls": {"identical_context_hash": ctx_hash},
        "negative_graph_control": {
            "negative_graph_source_cell": "twohop_l1_cell03",
            "removed_edge":               "target_chain/hop2",
            "independently_constructed":  True,
            "valid_A_to_C_path_exists":   False,
        },
        "dummy_baselines": {
            "uniform_random": {
                "strategy":       "uniform_random_over_context_objects",
                "c_role_options": 3,
                "expected_score": round(1 / 3, 6),
            },
        },
        "cue_balance": {
            "group":                    grp,
            "ct_c_rank":                ct_rank,
            "ct_abs_position":          ct_pos,
            "hop1_abs_position":        hop1_pos,
            "hop2_abs_position":        ct_pos,
            "neighbor_abs_position":    nbr_pos,
            "adjacency_broken":         True,
            "hop1_hop2_gap":            2,
        },
        "axis_note":        f"cell03_group_{grp}_ct_{ct_rank}",
        "axis_note_detail": (
            f"Group {grp}: hop1 at pos {hop1_pos}, neighbor interposed at pos {nbr_pos} "
            f"(gap=2, breaks adjacency), hop2 at pos {ct_pos} (ct={ct_rank}). "
            "Adjacency broken in all 24 items; C-rank balanced 8+8+8 (A=first,B=second,C=third/last); "
            "ct absolute position balanced (pos 3/5/7 for groups A/B/C)."
        ),
    }
    items.append(item)

# ── Phase 6: validate_manifest() ──────────────────────────────────────────────
print("\nPhase 6: validate_manifest()...")
result = validate_manifest(items)
print(f"  Total={result['total']}  Pass={result['pass_count']}  Fail={result['fail_count']}")
if not result["all_pass"]:
    for iid, errs in result["errors"].items():
        for e in errs:
            print(f"  ERROR [{iid}] {e}")
    sys.exit(1)
print("  validate_manifest(): ALL PASS")

# ── Phase 7: Write JSON and hash ───────────────────────────────────────────────
out = Path("items_twohop_l1_cell03.json")
out.write_text(json.dumps(items, indent=2))
manifest_hash = "sha256:" + hashlib.sha256(out.read_bytes()).hexdigest()
print(f"\nWrote: {out}")
print(f"manifest_hash: {manifest_hash}")

# ── Phase 8: Dummy baseline verification ──────────────────────────────────────
print("\nPhase 8: Dummy baseline verification (composite query)...")
import importlib.util

spec = importlib.util.spec_from_file_location(
    "scorer_twohop_l1", Path(__file__).parent / "scorer_twohop_l1.py")
scorer_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scorer_mod)

GATE5_REFERENCE_ONLY = {"always_return_ct", "always_return_NULL"}

qt = "composite"
strategy_sums = {}
for item in items:
    scores = scorer_mod.compute_dummy_baseline_scores(item, qt)
    for k, v in scores.items():
        if v is not None:
            strategy_sums[k] = strategy_sums.get(k, 0.0) + v

print(f"  Composite dummy baselines (sum / rate over {len(items)} items):")
ceiling = 9
max_det = 0.0
for k, s in sorted(strategy_sums.items()):
    ref   = "  (ref only)"   if k in GATE5_REFERENCE_ONLY else ""
    theor = "  [theoretical]" if k == "uniform_random_expected" else ""
    count_str = str(int(s)) if s == int(s) else str(s)
    print(f"    {k}: {count_str}/{len(items)} = {s/len(items):.4f}{ref}{theor}")
    if k not in GATE5_REFERENCE_ONLY and k != "uniform_random_expected":
        if s > max_det:
            max_det = s

print(f"\n  Max deterministic (ceiling-bearing): {int(max_det)}/{len(items)} = {max_det/len(items):.4f}")
print(f"  Gate 5 ceiling:                      {ceiling}/{len(items)} = {ceiling/len(items):.4f}")
if max_det <= ceiling:
    print("  Gate 5 dummy precheck:               PASS")
else:
    print("  Gate 5 dummy precheck:               FAIL")
    sys.exit(1)

# ── Phase 9: Per-group breakdown ──────────────────────────────────────────────
print("\nPhase 9: Per-group composite dummy breakdown:")
for grp_label in ["A", "B", "C"]:
    grp_items = [items[i] for i in range(24) if GROUP_LABELS[i] == grp_label]
    grp_sums  = {}
    for it in grp_items:
        sc = scorer_mod.compute_dummy_baseline_scores(it, "composite")
        for k, v in sc.items():
            if v is not None:
                grp_sums[k] = grp_sums.get(k, 0.0) + v
    ng = len(grp_items)
    print(f"  Group {grp_label} ({ng} items, ct={GROUP_CT_RANKS[grp_label]}, ct_pos={GROUP_CT_POS[grp_label]}):")
    for k in ["always_return_first_C", "always_return_second_C",
              "always_return_third_C",  "always_return_last_C",
              "always_return_ct"]:
        s   = grp_sums.get(k, 0.0)
        ref = " (ref)" if k in GATE5_REFERENCE_ONLY else ""
        print(f"    {k}: {int(s)}/{ng}{ref}")

# ── Phase 10: Declared near-miss pair summary ─────────────────────────────────
print("\nPhase 10: Declared near-miss pairs (C_target / C_neighbor):")
for i, (ct_tok, cn_tok) in enumerate(selected_pairs):
    print(f"  [{i+1:02d}] {ct_tok} / {cn_tok}  "
          f"lev={lev(ct_tok,cn_tok)}  bjac={bjac(ct_tok,cn_tok)}  tjac={tjac(ct_tok,cn_tok)}")

# ── Summary ────────────────────────────────────────────────────────────────────
print("\n-- Cell 03 Construction Summary " + "-" * 42)
print(f"  Cell ID:                    twohop_l1_cell03")
print(f"  n_items:                    24")
print(f"  Chains per item:            3 (target + decoy_1 + decoy_2)")
print(f"  Unique tokens in pool:      {len(all_unique_tokens)}")
print(f"  Context facts per item:     7")
print(f"  Relation (hop1):            '{RELATION_HOP1}'")
print(f"  Relation (hop2):            '{RELATION_HOP2}'")
print(f"  Primary axis:               adjacency/proximity (broken all 24 items; gap=2)")
print(f"  Group A (items 1-8):        ct first_C  pos 3; hop1 pos 1; neighbor pos 2")
print(f"  Group B (items 9-16):       ct second_C pos 5; hop1 pos 3; neighbor pos 4")
print(f"  Group C (items 17-24):      ct third_C  pos 7; hop1 pos 5; neighbor pos 6")
print(f"  Declared near-miss pairs:   {len(selected_pairs)}")
print(f"  Lev violations:             0")
print(f"  Trig violations:            0")
print(f"  BPE-j violations:           0")
print(f"  validate_manifest():        ALL PASS")
print(f"  Gate 5 dummy precheck:      PASS (max_det={int(max_det)}/{len(items)})")
print(f"  Tokenizer used for audit:   {_tok_hash_used}")
print(f"  manifest_hash:              {manifest_hash}")
print(f"  RNG seed:                   20260615")
print(f"  Scorer hash:                sha256:b65c6803...")
print(f"  No model inference performed.")
