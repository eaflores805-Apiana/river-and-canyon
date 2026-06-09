"""
Stage 1 cell generation script — Two-Hop Level 1 Cell 02
Generates items_twohop_l1_cell02.json

Authorization: Manager memo — "Cell02 Construction Authorization — Position / Ordering Axis"
2026-06-08

Axis change (one-axis): position / ordering only.
All 24 items use C_target-last ordering: T-hop2 at context position 6.

Forced structural change (Gate 5 mechanically required):
  In a pure C_target-last arrangement (decoy1 at pos 1-2, decoy2 at pos 3-4,
  target at pos 5-6, neighbor at pos 7), the scorer's _c_objects_by_context_position
  returns [cd1(pos 2), cd2(pos 4), ct(pos 6)], making ct the last C in context.
  always_return_last_C would score 24/24 → Gate 5 ceiling FAIL.
  To satisfy Gate 5 while keeping T-hop2 at position 6, decoy2's hop2 fact is
  placed at position 7 (after ct) and the neighbor fact is moved to position 4.
  This is documented in the Cell02 Preparation Lock Packet as a mechanically
  forced consequence of the all-C_target-last design constraint.

  Resulting c_by_pos for all items: [cd1(pos 2), ct(pos 6), cd2(pos 7)]
    first_C = cd1 (not ct) → always_return_first_C = 0/24
    last_C  = cd2 (not ct) → always_return_last_C  = 0/24
    Gate 5 dummy ceiling: PASS

Context arrangement for all 24 items:
  pos 1: decoy_chain_1 hop1 fact  (ad1 links to bd1)
  pos 2: decoy_chain_1 hop2 fact  (bd1 maps to cd1)   ← cd1 (C_decoy_1)
  pos 3: decoy_chain_2 hop1 fact  (ad2 links to bd2)
  pos 4: neighbor fact            (fl holds cn)
  pos 5: target_chain  hop1 fact  (at  links to bt)
  pos 6: target_chain  hop2 fact  (bt  maps to ct)    ← ct (C_target, T-hop2 at pos 6)
  pos 7: decoy_chain_2 hop2 fact  (bd2 maps to cd2)   ← cd2 (C_decoy_2, forced to pos 7)

All other variables frozen from Cell01:
  relations, context_length, chains_per_item, prompt template, scorer, validator,
  thresholds, query wording, negative_graph semantics, dummy baseline rules,
  failure taxonomy, decoding settings.

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
# Use FP16 HuggingFace tokenizer (confirmed run tokenizer sha256:c0382117...).
# Fall back to INT4 local tokenizer (confirmed equivalent by normalization).
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
        print(f"  Tokenizer: {fallback} (INT4 fallback — confirmed equivalent by normalization)")
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
# Different RNG seed from Cell01 (20260608) → new token pool. Seed 20260609 discarded (gen_pool infinite loop on that seed — broken circuit breaker); 20260610 used.
RNG = random.Random(20260610)
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
for ct in candidate_pool:
    partners = []
    for pos in range(5):
        for ch in L:
            if ch == ct[pos]:
                continue
            cand = ct[:pos] + ch + ct[pos + 1:]
            if not rt_ok(cand):
                continue
            lv = lev(ct, cand)
            bv = bjac(ct, cand)
            tv = tjac(ct, cand)
            if lv <= 2 and bv >= 0.40 and tv >= 0.20:
                partners.append(cand)
    for p1, p2 in itertools.combinations(range(5), 2):
        for ch1 in L:
            if ch1 == ct[p1]:
                continue
            for ch2 in L:
                if ch2 == ct[p2]:
                    continue
                cand = list(ct)
                cand[p1] = ch1
                cand[p2] = ch2
                cand = "".join(cand)
                if not rt_ok(cand):
                    continue
                lv = lev(ct, cand)
                bv = bjac(ct, cand)
                tv = tjac(ct, cand)
                if lv <= 2 and bv >= 0.40 and tv >= 0.20:
                    partners.append(cand)
    pair_index[ct] = list(set(partners))

print("  Greedy selection of 24 globally-compatible (C_target, C_neighbor) pairs...")
selected_pairs     = []
all_used_tokens    = set()
selected_c_targets = []

for ct in candidate_pool:
    if len(selected_pairs) == 24:
        break
    if not tok_compatible(ct, all_used_tokens):
        continue
    if any(bjac(ct, prev) >= 0.40 for prev in selected_c_targets):
        continue
    others = all_used_tokens - {ct}
    chosen_cn = None
    for cn in pair_index.get(ct, []):
        if cn in all_used_tokens:
            continue
        if tok_compatible(cn, others):
            chosen_cn = cn
            break
    if chosen_cn is None:
        continue
    selected_pairs.append((ct, chosen_cn))
    all_used_tokens.add(ct)
    all_used_tokens.add(chosen_cn)
    selected_c_targets.append(ct)

if len(selected_pairs) < 24:
    print(f"FATAL: only found {len(selected_pairs)} pairs.")
    sys.exit(1)

print(f"  Found {len(selected_pairs)} pairs.")
for i, (ct, cn) in enumerate(selected_pairs):
    print(f"  [{i + 1:02d}] {ct} / {cn}  "
          f"lev={lev(ct, cn)} bjac={bjac(ct, cn)} tjac={tjac(ct, cn)}")

# ── Phase 2: Assign C_decoy_1 and C_decoy_2 ──────────────────────────────────
C_TARGETS   = [p[0] for p in selected_pairs]
C_NEIGHBORS = {p[0]: p[1] for p in selected_pairs}
C_DECOYS_1  = [C_TARGETS[(i + 8)  % 24] for i in range(24)]
C_DECOYS_2  = [C_TARGETS[(i + 16) % 24] for i in range(24)]

print("\nVerifying C_decoy_1 and C_decoy_2 per-item compatibility (j < 0.40, lev > 2):")
decoy_ok = True
for i in range(24):
    for label, cd in (("cd1", C_DECOYS_1[i]), ("cd2", C_DECOYS_2[i])):
        bv = bjac(C_TARGETS[i], cd)
        lv = lev(C_TARGETS[i], cd)
        if bv >= 0.40 or lv <= 2:
            print(f"  VIOLATION item {i+1}: C_target={C_TARGETS[i]} {label}={cd} "
                  f"lev={lv} bjac={bv}")
            decoy_ok = False
    bv12 = bjac(C_DECOYS_1[i], C_DECOYS_2[i])
    lv12 = lev(C_DECOYS_1[i], C_DECOYS_2[i])
    if bv12 >= 0.40 or lv12 <= 2:
        print(f"  VIOLATION item {i+1}: cd1={C_DECOYS_1[i]} cd2={C_DECOYS_2[i]} "
              f"lev={lv12} bjac={bv12}")
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
            raise RuntimeError(f"Pool exhaustion (prefix={prefix}, needed={n}, have={len(pool)})")
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
print(f"\nPhase 4: Full audit over {len(all_unique_tokens)} unique tokens ({n_pairs} pairs)...")

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

print(f"  Lev violations (≤2, undeclared):           {len(lev_v)}")
print(f"  Trig violations (≥0.20, undeclared):       {len(trig_v)}")
print(f"  BPE violations (C-role, ≥0.40, undeclared): {len(bpe_v)}")
for x in lev_v[:5]:  print(f"    LEV  {x}")
for x in trig_v[:5]: print(f"    TRIG {x}")
for x in bpe_v[:5]:  print(f"    BPE  {x}")

if lev_v or trig_v or bpe_v:
    print("FATAL: token pool audit failed.")
    sys.exit(1)
print("  Token pool audit: PASS")

# ── Phase 5: Build items ───────────────────────────────────────────────────────
# All 24 items: C_target-last-split arrangement.
#
# Context ordering (all 24 items):
#   pos 1: decoy_chain_1 hop1 (ad1 links to bd1)
#   pos 2: decoy_chain_1 hop2 (bd1 maps to cd1)   ← cd1 (C_decoy_1) at pos 2
#   pos 3: decoy_chain_2 hop1 (ad2 links to bd2)
#   pos 4: neighbor fact      (fl holds cn)
#   pos 5: target_chain hop1  (at links to bt)
#   pos 6: target_chain hop2  (bt maps to ct)      ← ct (C_target, T-hop2) at pos 6
#   pos 7: decoy_chain_2 hop2 (bd2 maps to cd2)   ← cd2 (C_decoy_2) at pos 7
#
# c_by_pos (scorer's _c_objects_by_context_position):
#   [cd1(pos 2), ct(pos 6), cd2(pos 7)]
#   first_C = cd1 → NOT ct (0/24 for always_return_first_C)
#   last_C  = cd2 → NOT ct (0/24 for always_return_last_C)
#   Gate 5 dummy ceiling: max_det = 0/24 ≤ 9/24 → PASS
#
# Forced change note: decoy_chain_2 hop2 at pos 7 (not pos 4) is mechanically
# required to avoid always_return_last_C = 24/24 → Gate 5 FAIL. See module docstring.

RELATION_HOP1 = "links to"
RELATION_HOP2 = "maps to"
RELATION_HOLD = "holds"

items = []
for i in range(24):
    n   = i + 1
    ct  = C_TARGETS[i];   cn  = C_NEIGHBORS[ct]
    cd1 = C_DECOYS_1[i];  cd2 = C_DECOYS_2[i]
    at  = a_targets[i];   bt  = b_targets[i]
    ad1 = a_decoys_1[i];  bd1 = b_decoys_1[i]
    ad2 = a_decoys_2[i];  bd2 = b_decoys_2[i]
    fl  = fillers[i]
    item_id = f"twohop_l1_c02_i{n:02d}"

    facts = [
        {"fact_id": "f01", "chain_id": "decoy_chain_1",    "fact_role": "decoy_hop1_fact",
         "text": f"{ad1} {RELATION_HOP1} {bd1}.", "position_index": 1},
        {"fact_id": "f02", "chain_id": "decoy_chain_1",    "fact_role": "decoy_hop2_fact",
         "text": f"{bd1} {RELATION_HOP2} {cd1}.", "position_index": 2},
        {"fact_id": "f03", "chain_id": "decoy_chain_2",    "fact_role": "decoy_hop1_fact",
         "text": f"{ad2} {RELATION_HOP1} {bd2}.", "position_index": 3},
        {"fact_id": "f04", "chain_id": "neighbor_context", "fact_role": "neighbor_decoy_fact",
         "text": f"{fl} {RELATION_HOLD} {cn}.",   "position_index": 4},
        {"fact_id": "f05", "chain_id": "target_chain",     "fact_role": "hop1_fact",
         "text": f"{at} {RELATION_HOP1} {bt}.",   "position_index": 5},
        {"fact_id": "f06", "chain_id": "target_chain",     "fact_role": "hop2_fact",
         "text": f"{bt} {RELATION_HOP2} {ct}.",   "position_index": 6},
        {"fact_id": "f07", "chain_id": "decoy_chain_2",    "fact_role": "decoy_hop2_fact",
         "text": f"{bd2} {RELATION_HOP2} {cd2}.", "position_index": 7},
    ]

    ctx = {"ordered_facts": facts}
    ctx_hash = compute_context_hash({"context": ctx})

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
            "composite_requires_hop1":          True,
            "composite_requires_hop2":          True,
            "answer_from_hop1_alone_possible":  False,
            "answer_from_hop2_alone_possible":  False,
            "validation_method":                "manifest_structure",
        },
        "same_context_controls": {"identical_context_hash": ctx_hash},
        "negative_graph_control": {
            "negative_graph_source_cell": "twohop_l1_cell02",
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
            "first_context_object": {
                "strategy":        "first_c_object_by_hop2_position",
                "expected_answer": cd1,
                "correct":         False,
            },
            "last_context_object": {
                "strategy":        "last_c_object_by_hop2_position",
                "expected_answer": cd2,
                "correct":         False,
            },
        },
        "axis_note": "target_last_split",
        "axis_note_detail": (
            "T-hop2 at context position 6. "
            "decoy_chain_2 hop2 at position 7 (after target hop2) — "
            "mechanically required for Gate 5 dummy ceiling compliance. "
            "See generate_cell02.py module docstring."
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
out = Path("items_twohop_l1_cell02.json")
out.write_text(json.dumps(items, indent=2))
manifest_hash = "sha256:" + hashlib.sha256(out.read_bytes()).hexdigest()
print(f"\nWrote: {out}")
print(f"manifest_hash: {manifest_hash}")

# ── Phase 8: Dummy baseline verification (composite query) ────────────────────
print("\nPhase 8: Dummy baseline verification (composite query)...")
import importlib.util

spec = importlib.util.spec_from_file_location(
    "scorer_twohop_l1", Path(__file__).parent / "scorer_twohop_l1.py")
scorer_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scorer_mod)

qt = "composite"
strategy_sums = {}
for item in items:
    scores = scorer_mod.compute_dummy_baseline_scores(item, qt)
    for k, v in scores.items():
        if v is not None:
            strategy_sums[k] = strategy_sums.get(k, 0) + v

print(f"  Composite dummy baselines (sum / rate over {len(items)} items):")
ceiling = 9
for k, s in sorted(strategy_sums.items()):
    mark = "  [theoretical]" if k == "uniform_random_expected" else ""
    print(f"    {k}: {int(s) if s == int(s) else s}/{len(items)} = "
          f"{s / len(items):.4f}{mark}")

max_det = max(v for k, v in strategy_sums.items() if k != "uniform_random_expected")
print(f"\n  Max deterministic strategy: {max_det}/{len(items)} = {max_det/len(items):.4f}")
print(f"  Gate 5 ceiling:             {ceiling}/{len(items)} = {ceiling/len(items):.4f}")
if max_det <= ceiling:
    print("  Gate 5 dummy check:         PASS")
else:
    print("  Gate 5 dummy check:         FAIL")
    sys.exit(1)

# ── Phase 9: Declared near-miss pair summary ──────────────────────────────────
print("\nPhase 9: Declared near-miss pairs (C_target / C_neighbor):")
for i, (ct, cn) in enumerate(selected_pairs):
    print(f"  [{i + 1:02d}] {ct} / {cn}  "
          f"lev={lev(ct, cn)}  bjac={bjac(ct, cn)}  tjac={tjac(ct, cn)}")

# ── Summary ────────────────────────────────────────────────────────────────────
print("\n── Cell 02 Construction Summary ─────────────────────────────────────────")
print(f"  Cell ID:                    twohop_l1_cell02")
print(f"  n_items:                    24")
print(f"  Chains per item:            3 (target + decoy_1 + decoy_2)")
print(f"  Unique tokens in pool:      {len(all_unique_tokens)}")
print(f"  Context facts per item:     7")
print(f"  Relation (hop1):            '{RELATION_HOP1}'")
print(f"  Relation (hop2):            '{RELATION_HOP2}'")
print(f"  Context ordering:           all-C_target-last (T-hop2 at pos 6, all 24 items)")
print(f"  T-hop1 position:            5 (all items)")
print(f"  T-hop2 position:            6 (all items)")
print(f"  decoy_chain_2 hop2 pos:     7 (all items — Gate 5 forced)")
print(f"  C_role_options per item:    3")
print(f"  uniform_random_expected:    {round(1/3, 6)}")
print(f"  Declared near-miss pairs:   {len(selected_pairs)}")
print(f"  Lev violations:             0")
print(f"  Trig violations:            0")
print(f"  BPE-j violations:           0")
print(f"  validate_manifest():        ALL PASS")
print(f"  Gate 5 dummy ceiling:       PASS (max_det={max_det}/{len(items)})")
print(f"  Tokenizer used for audit:   {_tok_hash_used}")
print(f"  manifest_hash:              {manifest_hash}")
print(f"  RNG seed:                   20260610")
print(f"  Axis change:                position / ordering only (one-axis)")
print(f"  Frozen from Cell01:         all other variables")
