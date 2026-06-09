# Stage 1 Preparation Lock Packet — Two-Hop Level 1
## Revision 2

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Status:** AWAITING TEAM LEAD REVIEW
**Per:** Manager authorization memo — Stage 1 Preparation Authorization — Two-Hop Level 1, 2026-06-08
**Supersedes:** Revision 1 (same date — scorer fact_role mismatch and cell regeneration required)

**Changes from Revision 1:**
- Option D implemented: scorer amended to recognize "hop2_fact"/"decoy_hop2_fact" (backward-compatible; smoke/unit tests PASS)
- Option B implemented: cell regenerated with 3-chain 7-fact 8+8+8 design; Gate 5 dummy ceiling PASS (first_C = last_C = 8/24 ≤ 9/24)
- All affected hashes updated: scorer, manifest, runner
- Tokenizer hash formally accepted by Team Lead (unchanged from Rev 1 finding)

---

## 1. Generated cell JSON path and hash

```
Path:     tier0-run/items_twohop_l1_cell01.json
Hash:     sha256:00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28
Items:    n = 24
Cell ID:  cell01
Design:   3 chains per item (target + decoy_1 + decoy_2); 7 facts per context
Ordering: 8+8+8 — items 1-8 C_target-first, items 9-16 C_target-middle, items 17-24 C_target-last
RNG seed: random.Random(20260608) — deterministic, reproducible
Generator: tier0-run/generate_cell01.py (one-time script, not locked)
```

---

## 2. Runner script path and hash

```
Path:  tier0-run/runner_twohop_l1.py
Hash:  sha256:ed2fbdc3e21375060f15a0645da111c24db890b840d9be476ee24d8bb06c5aaf
```

**Runner embedded provenance constants:**

```
EXPECTED_VALIDATOR_HASH  = sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
EXPECTED_SCORER_HASH     = sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd
EXPECTED_TOKENIZER_HASH  = sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
MODEL_ID                 = Qwen/Qwen2.5-3B-Instruct
DECODING_SETTINGS        = {temperature: 0.0, max_tokens: 16}
AXIS_CONFIGURATION       = Single axis: token identities vary across items.
                           Ordering 8+8+8: items 1-8 C_target-first (T-hop2 at position 2),
                           items 9-16 C_target-middle (T-hop2 at position 4),
                           items 17-24 C_target-last (T-hop2 at position 6).
FROZEN_SETTINGS          = relation_hop1='links to'; relation_hop2='maps to';
                           relation_hold='holds'; context_length=7 facts;
                           chains_per_item=3 (target + decoy_1 + decoy_2);
                           query_phrasing=template;
                           instruction_prefix=prompt_template_twohop_l1.txt
FAILURE_TAXONOMY_VERSION = v1.0
```

**Dry-run status:**

```
python runner_twohop_l1.py --dry-run

Step 1: Recording provenance hashes...
  validator_hash: OK
  scorer_hash: OK
Step 2: Loading and validating manifest...
  validate_manifest(): 24/24 pass
Step 3: Confirming FP16 tokenizer hash...
  tokenizer_hash: OK   [sha256:c0382117...]
Dry-run mode: provenance and manifest checks complete. No model inference performed.

Result: PASSES
```

---

## 3. Prompt template path and hash

```
Path:  tier0-run/prompt_template_twohop_l1.txt
Hash:  sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
```

**Template content (verbatim — unchanged from Rev 1):**

```
You are given a set of facts and a question. Answer using only information in the facts provided. Respond using only this exact format with nothing before or after: ANSWER: <TOKEN>
If no answer can be determined from the facts, respond: ANSWER: NULL

Facts:
{CONTEXT}

Question: {QUERY}
```

**Query text per query type:**

```
hop1:           {anchor} links to what?
hop2:           {anchor} maps to what?
composite:      {anchor} links to something, which maps to what?
negative_graph: {anchor} links to something, which maps to what?
```

---

## 4. FP16 tokenizer hash confirmation

**Status: ACCEPTED by Team Lead 2026-06-08**

```
FP16 HuggingFace tokenizer.json hash: sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
Local int4/int8 reference hash:       sha256:3fd169731d2cbde95e10bf356d66d5997fd885dd8dbb6fb4684da3f23b2585d8
```

Hash difference is JSON serialization format only (merges stored as strings vs lists). Vocabulary identical (151,643 tokens). Normalized merges identical. BPE behavior identical. Runner dry-run confirms tokenizer_hash: OK. Accepted per Team Lead disposition 2026-06-08. Gate 0.5 tokenizer check CLOSED.

---

## 5. Scorer amendment record (Option D)

**Amendment authorized:** Team Lead disposition 2026-06-08

**Change:** `scorer_twohop_l1.py` line 229

```python
# Before (locked Stage 0 original):
if f.get("fact_role") == "hop2":

# After (amended 2026-06-08):
if f.get("fact_role") in ("hop2", "hop2_fact", "decoy_hop2_fact"):
```

**Rationale:** Backward-compatible extension. Accepts original schema value `"hop2"` (smoke test item still passes) AND item schema values `"hop2_fact"` (target chain) and `"decoy_hop2_fact"` (decoy chains), allowing `_c_objects_by_context_position()` to function correctly with generated items.

```
Prior scorer hash:   sha256:6921e58059e3ef4806c1ae75f73a9670f4a02962bff2eb27fd2da77bad82c473
Amended scorer hash: sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd

Smoke test (smoke_test_twohop_l1.py):  22/22 PASS
Scorer unit tests (run_unit_tests()):  14/14 PASS
```

---

## 6. Cell regeneration record (Option B)

**Regeneration authorized:** Team Lead disposition 2026-06-08

**Design change summary:**

| Property | Rev 1 (rejected) | Rev 2 (current) |
|---|---|---|
| Chains per item | 2 (target + decoy_1) | 3 (target + decoy_1 + decoy_2) |
| Context facts per item | 5 | 7 |
| Context ordering | 12/12 (target-first / decoy-first) | 8/8/8 (C_target first / middle / last) |
| C-role objects per item | 2 | 3 |
| uniform_random_expected | 1/2 = 0.500 | 1/3 = 0.333 |
| always_return_first_C (composite) | 0/24 (non-functional) | 8/24 = 0.333 (functional) |
| always_return_last_C (composite) | 0/24 (non-functional) | 8/24 = 0.333 (functional) |
| Gate 5 dummy ceiling (9/24) | Passes by structural zero | Passes by genuine construction |

**New non-C-role tokens (role-locked across items):**

```
ZG prefix: A_object for decoy_chain_2 (role: other_context)
ZH prefix: B_object for decoy_chain_2 (role: distractor_chain_intermediate)
```

**Rotation assignments:**

```
C_decoy_1[i] = C_TARGETS[(i + 8)  % 24]   ← decoy_chain_1 endpoint
C_decoy_2[i] = C_TARGETS[(i + 16) % 24]   ← decoy_chain_2 endpoint
```

All 3 per-item C objects drawn from the globally-compatible C_TARGETS pool (pairwise BPE-j < 0.40 confirmed).

---

## 7. Validation summary — all n=24 cells

```
validate_manifest() via tasks_twohop_l1.py (sha256:bcc26ca0..., unchanged)

Result: 24 / 24 PASS
Errors: 0
```

All required fields, query types, positive_sufficiency_exclusion, negative_graph_control, same_context_controls, and dummy_baselines present and valid. Context hash verified on all items.

---

## 8. BPE-Jaccard / token-construction inspection summary

**Token pool:**

```
C-role tokens (globally selected, 24 C_target + 24 C_neighbor):
  C_target (answer_C):              24 distinct tokens
  C_neighbor (target_neighbor_decoy): 24 tokens, 1-1 with C_target
  C_decoy_1 (distractor_chain_endpoint): C_TARGETS[(i+8)%24]
  C_decoy_2 (distractor_chain_endpoint): C_TARGETS[(i+16)%24]

Non-C role-locked tokens (24 unique per role):
  ZA prefix: anchor_A
  ZB prefix: hop1_B
  ZD prefix: A_object of decoy_chain_1 (other_context)
  ZE prefix: B_object of decoy_chain_1 (distractor_chain_intermediate)
  ZF prefix: inert_filler
  ZG prefix: A_object of decoy_chain_2 (other_context)      ← new
  ZH prefix: B_object of decoy_chain_2 (distractor_chain_intermediate) ← new
```

**Full token-pool audit (216 unique tokens, 23,220 pairs):**

```
BPE round-trip failures:                              0
Levenshtein ≤ 2 violations (non-declared):            0
Trigram-Jaccard ≥ 0.20 violations (non-declared):     0
BPE-Jaccard ≥ 0.40 violations (cross-chain C-pairs, non-declared): 0
```

**Declared near-miss pairs (all 24 C_target / C_neighbor):**

```
All 24 pairs confirmed:
  Levenshtein ≤ 2:        YES (all)
  Trigram-Jaccard ≥ 0.20: YES (all)
  BPE-Jaccard ≥ 0.40:     YES (all)   [j ≥ 0.40 per LOCKED amendment 2026-06-08]
```

---

## 9. Dummy baseline summary

**Method:** `scorer_twohop_l1.py::compute_dummy_baseline_scores()` (amended scorer, sha256:060afad9...) over all 24 items × 4 query types. `_c_objects_by_context_position()` now functional.

**Composite query — deterministic strategy scores:**

```
Strategy                    Score     Rate
always_return_B_target      0/24      0.000
always_return_C_decoy_1     0/24      0.000
always_return_C_decoy_2     0/24      0.000
always_return_NULL          0/24      0.000
always_return_anchor_A      0/24      0.000
always_return_first_C       8/24      0.333   ← functional; items 1-8 correct
always_return_last_C        8/24      0.333   ← functional; items 17-24 correct
uniform_random_expected     ≈8/24     0.333   [theoretical 1/3 — not a strategy score]
```

**Gate 5 dummy ceiling check (composite):**

```
Ceiling:                      ≤ 9/24 = 0.375
Max deterministic strategy:   8/24  = 0.333
Result:                       0.333 < 0.375 → PASS

Second condition: Gate-2 composite − max_dummy ≥ 10/24
  If Gate-2 composite = 21/24 (minimum for Gate 2 PASS):
  21/24 − 8/24 = 13/24 ≥ 10/24 → PASS
```

**Position-dummy strategies are genuine:** `first_C` returns C_target for items 1-8 (where C_target appears at position 2, before the decoy chains); `last_C` returns C_target for items 17-24 (where C_target appears at position 6, after both decoy chains). 8 correct out of 24 each — genuine construction score, not a structural zero.

---

## 10. Gate 0 / Gate 0.5 preflight status

### Gate 0 — Axis-control and manifest

```
All 24 items validate_manifest():             PASS (24/24, 0 errors)
Axis configuration documented:                PASS
  — single axis: token identities vary across items
  — ordering 8+8+8: C_target first (items 1-8), middle (9-16), last (17-24)
Frozen settings documented:                   PASS
  — relation_hop1='links to'; relation_hop2='maps to'; relation_hold='holds'
  — context_length=7 facts; chains_per_item=3
  — query_phrasing=template; instruction_prefix=prompt_template_twohop_l1.txt
identical_context_hash verified:              PASS — present on all items
negative_graph path absence confirmed:        PASS
  — valid_A_to_C_path_exists=false on all items
  — removed_edge="target_chain/hop2" on all items
manifest_hash recorded:                       sha256:00a7adf8...
validator_hash confirmed (unchanged):         sha256:bcc26ca0...

Gate 0 status: PASS
```

### Gate 0.5 — Token-construction audit

```
BPE round-trip verified (216 tokens):         PASS — 0 failures
Levenshtein scan (23,220 pairs):              PASS — 0 violations
Trigram-Jaccard scan:                         PASS — 0 violations
BPE-Jaccard scan:                             PASS — 0 cross-chain C-pair violations
target_neighbor_decoy confirmed (24 pairs):   PASS — all lev≤2, tjac≥0.20, bjac≥0.40
scorer_hash (amended):                        sha256:060afad9...
runner_hash:                                  sha256:ed2fbdc3...
prompt_template_hash (unchanged):             sha256:c8a81a29...
tokenizer_hash (FP16, Team Lead accepted):    sha256:c0382117...

Gate 0.5 status: PASS
```

---

## 11. Run Summary template path

```
Path:     tier0-run/RUN-SUMMARY-TEMPLATE-TWOHOP-L1.md
Version:  Stage 0 — 2026-06-07
Status:   LOCKED (Stage 0 instrument, unchanged)
```

Output runs will file as:
```
RESULTS-TWOHOP-L1-cell01-hop1.md
RESULTS-TWOHOP-L1-cell01-hop2.md
RESULTS-TWOHOP-L1-cell01-composite.md
RESULTS-TWOHOP-L1-cell01-negative_graph.md
```

---

## 12. No-model-inference confirmation

**No model inference has been performed under this authorization.**

```
Authorization scope:      Stage 1 preparation work only (Manager memo 2026-06-08)
Model inference status:   NOT PERFORMED
Model inference auth:     NOT GRANTED
Dry-run executed:         YES (--dry-run; steps 1-3 only; no model load, no model call)
Model loaded:             NO
Any scored result:        NONE
Raw output artifact:      NONE
```

---

## Summary and routing

**Lock packet completeness (Revision 2):**

| # | Required item | Status |
|---|---|---|
| 1 | Cell JSON path and hash | COMPLETE — sha256:00a7adf8... |
| 2 | Runner script path and hash | COMPLETE — sha256:ed2fbdc3... |
| 3 | Prompt template path and hash | COMPLETE — sha256:c8a81a29... (unchanged) |
| 4 | FP16 tokenizer hash confirmation | COMPLETE — accepted by Team Lead |
| 5 | Validation summary n=24 | COMPLETE — 24/24 PASS |
| 6 | BPE-Jaccard / token construction summary | COMPLETE — 23,220 pairs, 0 violations |
| 7 | Dummy baseline summary | COMPLETE — functional; first_C=last_C=8/24; Gate 5 PASS |
| 8 | Gate 0 / Gate 0.5 preflight | COMPLETE — Gate 0 PASS; Gate 0.5 PASS |
| 9 | Run Summary template path | COMPLETE |
| 10 | No-model-inference confirmation | CONFIRMED |

**Additional item (Option D):** Scorer amendment record included (§5) with prior/new hashes and test results.

**All blocking items from Rev 1 are resolved.**

**Routing:** Revised lock packet submitted for Team Lead review. If accepted, request routing to Manager for FP16 inference authorization decision.

**No model inference authorized. No model inference performed.**

— CS Engineer, 2026-06-08
