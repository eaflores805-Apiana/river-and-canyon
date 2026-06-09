# Stage 0 Instrument Lock Packet — Two-Hop Level 1

**Date:** 2026-06-07
**Owner:** CS Engineer
**Status:** STAGE 0 CLOSED — hashes locked (scorer amended 2026-06-08; see §10)
**Confirmed by:** Team Lead (memo: "Stage 0 Open Items — Team Lead Confirmation")
**Amendment authorized by:** Team Lead disposition — "Scorer fact_role Mismatch — Team Lead Disposition" 2026-06-08 (Option D)

---

## 1. Deliverables

| Item | File | Status |
|---|---|---|
| Two-hop manifest schema + validator | `tasks_twohop_l1.py` | LOCKED |
| Single deterministic scorer | `scorer_twohop_l1.py` | LOCKED |
| Failure taxonomy version | `FAILURE_TAXONOMY_VERSION = "v1.0"` in scorer | LOCKED |
| Smoke test (22/22 pass, no model inference) | `smoke_test_twohop_l1.py` | LOCKED |
| Dummy baseline implementation | in `scorer_twohop_l1.py` | LOCKED |
| Token-construction audit (Levenshtein + trigram-Jaccard) | in `tasks_twohop_l1.py` | LOCKED |
| Negative graph control validation | in `tasks_twohop_l1.py` | LOCKED |
| Run_Summary template | `RUN-SUMMARY-TEMPLATE-TWOHOP-L1.md` | LOCKED |
| Hash manifest | this document § 2 | LOCKED |
| Threshold proposal | — | BLOCKED — pending threshold-setting phase |

---

## 2. Hash manifest (locked)

```
tasks_twohop_l1.py              sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
scorer_twohop_l1.py             sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd  ← amended 2026-06-08
smoke_test_twohop_l1.py         sha256:58749ca88ab69e0fc6cf34cfb3417ee57f42c1ebe13c5c7cfd384726182c3989

Prior scorer hash (original Stage 0 lock, superseded):
  scorer_twohop_l1.py           sha256:6921e58059e3ef4806c1ae75f73a9670f4a02962bff2eb27fd2da77bad82c473
```

Any amendment changes a hash. No in-place patching of locked files. Any amendment requires Team Lead approval, increments `FAILURE_TAXONOMY_VERSION` or `MANIFEST_SCHEMA_VERSION` as appropriate, and reissues this packet.

**Amendment note 2026-06-08:** `scorer_twohop_l1.py` line 229 amended (backward-compatible); `FAILURE_TAXONOMY_VERSION` unchanged at "v1.0" (no failure class or priority-order change). See §10 for full amendment record.

---

## 3. Unit and smoke test summary

```
Scorer unit tests:  14/14 pass
Smoke tests:        22/22 pass

Coverage:
  correct                        — all query types
  format_scaffold_failure        — no scaffold prefix
  non_context_return             — out-of-registry token; NULL on positive query
  correct_chain_stopped_short    — composite returns B_target
  anchor_echo                    — composite/hop1/hop2 anchor returns
  wrong_chain_selection          — decoy endpoint; decoy intermediate
  target_chain_wrong_neighbor    — target_neighbor_decoy
  UNCLASSIFIED_OFF_FRAME         — covered by class; not triggered in smoke items
  validator: well-formed pass    — clean item validates
  validator: hash mismatch       — caught
  validator: positive_sufficiency — caught
  validator: disjoint role       — caught
  string metrics: levenshtein    — 0-edit, 1-edit, 2-edit
  string metrics: trigram-Jaccard — identical=1.0, disjoint<1.0, 1-edit>0.0
  dummy baselines                — B_target, anchor_A, first_C, last_C, NULL, decoy_1
  uniform_random_expected        — composite=0.5, hop1=0.5, neg_graph=1/3, lm=None
```

---

## 4. Final priority order (confirmed)

```
1. format_scaffold_failure
2. non_context_return
3. correct_chain_stopped_short   (composite only)
4. anchor_echo                   (confirmed at position 4, before wrong_neighbor)
5. wrong_chain_selection
6. target_chain_wrong_neighbor   (includes target_neighbor_decoy objects)
7. UNCLASSIFIED_OFF_FRAME
```

Rationale for anchor_echo at position 4: anchor_echo is a more specific classification than wrong_neighbor. Anchor_A objects belong to the target chain; placing wrong_neighbor before anchor_echo makes anchor_echo unreachable for all anchor_A returns, defeating its purpose. Confirmed as specification correction by Team Lead.

---

## 5. Role map (final)

```
Role tag                        Object                         Hop1 denominator  Hop2/Composite denom
answer_C                        Target chain C (endpoint)      no                yes
hop1_B                          Target chain B (intermediate)  yes               no
anchor_A                        Target chain A (source)        no                no
target_neighbor_decoy           Planted near-C decoy           no                no
distractor_chain_endpoint       Decoy chain C (endpoint)       no                yes
distractor_chain_intermediate   Decoy chain B (intermediate)   yes               no
other_context                   Decoy chain A (source)         no                no
inert_filler                    Filler fact object             no                no
null_no_link                    NULL / NO_LINK token           no                no (yes +1 for neg_graph)
```

Decoy chain A-position objects carry `other_context`. Rationale: preserves hop1 denominator as B-position objects only. Confirmed by Team Lead.

---

## 6. Instrument summary

### tasks_twohop_l1.py — manifest schema + validator

```
MANIFEST_SCHEMA_VERSION = "v1.0"
Role tags (9):     answer_C, hop1_B, anchor_A, target_neighbor_decoy,
                   distractor_chain_endpoint, distractor_chain_intermediate,
                   inert_filler, other_context, null_no_link
Query types (5):   hop1, hop2, composite, negative_graph, length_matched
Required queries:  hop1, hop2, composite, negative_graph

compute_context_hash()     SHA-256 of NFC-normalized canonical ordered_facts
levenshtein()              case-insensitive edit distance
trigram_jaccard()          trigram-Jaccard similarity
audit_near_miss()          both metrics, no threshold applied (thresholds blocked)
audit_round_trip()         BPE round-trip (requires locked tokenizer)

validate_required_fields()       required top-level and query-type fields
validate_object_roles()          registry, target roles, collision, disjoint check
validate_positive_sufficiency()  composite_requires both hops; no single-hop shortcut
validate_context_hash()          recomputes and compares identical_context_hash
validate_negative_graph_control() structural fields, path_exists=False
validate_item()                  all validators
validate_manifest()              validate_item over list
get_manifest_hash()              SHA-256 of this file
```

### scorer_twohop_l1.py — single deterministic scorer

```
FAILURE_TAXONOMY_VERSION = "v1.0"
Failure classes (8): correct, format_scaffold_failure, non_context_return,
                     correct_chain_stopped_short, anchor_echo, wrong_chain_selection,
                     target_chain_wrong_neighbor, UNCLASSIFIED_OFF_FRAME
Output contract: ^ANSWER:\s+[A-Z]{4,8}$  (NULL accepted for negative_graph)

classify_output(raw, item, query_type)
compute_uniform_random_expected(item, query_type)
compute_dummy_baseline_scores(item, query_type)
run_unit_tests()
get_scorer_hash()
```

---

## 7. Thresholds (all blocked)

```
near_miss Levenshtein k            proposed ≤ 2 — Manager approval required
near_miss BPE-Jaccard j            not set
char_overlap trigram-Jaccard j     not set
length_matched token_count ±x      not set
Gate-2 FP16 pass rate              not set
dummy ceiling                      not set
unique-assignment reliability      not set
UNCLASSIFIED / OFF-FRAME ceiling   not set
Gate-3 fidelity ceilings           not set
```

Threshold proposal is the next Stage 0 deliverable. Must be approved before any cell run.

---

## 8. Authorization boundary

Stage 0 closure authorizes:

```
schema and scorer inspection
smoke test re-execution (offline only)
threshold proposal drafting
```

Stage 0 closure does NOT authorize:

```
cell generation
model inference
confirmation pass
7B capacity-control pass
INT8 / INT4 stress
Track B
any run
```

---

## 9. Files (Stage 0 complete set)

```
tasks_twohop_l1.py                  manifest schema + validator (LOCKED — unchanged)
scorer_twohop_l1.py                 deterministic scorer (LOCKED — amended 2026-06-08; new hash in §2)
smoke_test_twohop_l1.py             offline smoke test (LOCKED — unchanged)
RUN-SUMMARY-TEMPLATE-TWOHOP-L1.md  run summary template (LOCKED — unchanged)
STAGE0-INSTRUMENT-LOCK-PACKET.md    this document
CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md  canonical gate ladder and claim structure
```

---

## 10. Scorer amendment record — 2026-06-08

**Amendment authorized:** Team Lead disposition memo — "Scorer fact_role Mismatch — Team Lead Disposition" 2026-06-08, Option D

**Change:** `scorer_twohop_l1.py` line 229 only

```python
# Before (original Stage 0 lock):
if f.get("fact_role") == "hop2":

# After (amended 2026-06-08):
if f.get("fact_role") in ("hop2", "hop2_fact", "decoy_hop2_fact"):
```

**Rationale:** Backward-compatible extension. Accepts original smoke-test schema value `"hop2"` AND item-generation schema values `"hop2_fact"` (target chain) and `"decoy_hop2_fact"` (decoy chains). Required so `_c_objects_by_context_position()` returns correct C-role objects for generated items. Affects `compute_dummy_baseline_scores()` only; `classify_output()` is unaffected.

**Scope of change:**
- `FAILURE_TAXONOMY_VERSION`: unchanged ("v1.0") — no failure class or priority-order change
- `MANIFEST_SCHEMA_VERSION`: unchanged — no schema change
- Smoke test 22/22 PASS confirmed (backward-compatible; smoke item still uses `"hop2"`)
- Scorer unit tests 14/14 PASS confirmed

```
Prior hash (superseded):  sha256:6921e58059e3ef4806c1ae75f73a9670f4a02962bff2eb27fd2da77bad82c473
Amended hash (current):   sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd
```
