# Cell03 Scorer Amendment Planning Packet

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Requested by:** Team Lead memo — "Cell03 Dummy Policy Status — R3 Direction Accepted for Senior Review" 2026-06-08
**Current scorer:** scorer_twohop_l1.py — sha256:060afad9... (LOCKED)
**Amendment target:** add full-rank C dummies + always_return_ct reference diagnostic
**Status:** PLANNING ONLY — scorer amendment not yet authorized

---

## Scope Correction from Prior Policy Documents

Prior documents (CELL03-DUMMY-POLICY-CONFIRMATION.md, R1, R2) listed `always_return_NULL` as a new addition. **This was incorrect.**

`always_return_NULL` is already implemented in `compute_dummy_baseline_scores()` at line 264:

```python
"always_return_NULL": score("NULL"),
```

It scores 1.0 when `expected_answer == "NULL"` (negative_graph), 0.0 otherwise.

**Revised amendment scope:** three new dummies only, not four.

---

## 1. Retired Names — Confirmed Not Added

The following names must not appear anywhere in the amended scorer:

```text
always_return_query_role_object
always_return_most_recent_role_match
always_return_answer_shaped
```

These concepts are retired. The scorer amendment adds no role-match or answer-shaped dummy.
No placeholder, no stub, no comment referencing these names.

---

## 2. Missing Full-Rank C Dummies — Additions Required

**Current state of `compute_dummy_baseline_scores()`:**

```python
"always_return_first_C":   score(c_by_pos[0])  if c_by_pos else 0.0,   # rank 1 — EXISTS
"always_return_last_C":    score(c_by_pos[-1]) if c_by_pos else 0.0,   # rank last — EXISTS
```

**Missing dummies to add:**

```python
# always_return_second_C — rank-2 C by context position
# Ceiling-bearing Gate 5 control. Required for Cell03 and all future ranked-C constructions.
"always_return_second_C":  score(c_by_pos[1]) if len(c_by_pos) >= 2 else 0.0,

# always_return_third_C — rank-3 C by context position
# Required when construction has 3+ C-endpoints (Cell03 has cd1, ct, cd2: required).
# Guarded: falls back to 0.0 when fewer than 3 C-endpoints present.
# Note: for Cell03 (3 endpoints), third_C == last_C — both rows reported explicitly.
"always_return_third_C":   score(c_by_pos[2]) if len(c_by_pos) >= 3 else 0.0,
```

**Ceiling-bearing status:** both are ceiling-bearing Gate 5 controls, subject to max_det ≤ 9/24.

**Why always_return_second_C is critical:**
In Cell02 (ct fixed as second_C for all items), `always_return_second_C` would have scored 24/24
on composite — a Gate 5 ceiling failure. This is the coverage gap documented in
CELL02-GATE5-POSITIONAL-DUMMY-AUDIT.md. Cell03's balanced design prevents this coincidence but
the dummy remains required to detect it in any future construction.

---

## 3. always_return_ct — Reference-Only Addition

**Not currently in scorer.** Must be added.

```python
# always_return_ct — target-token upper bound diagnostic
# Reference-only: excluded from max_det ceiling calculation.
# Records the "always return the target C endpoint" oracle score.
# Expected scores: hop1 = 0.0, hop2 = 1.0, composite = 1.0, negative_graph = 0.0.
# hop2/composite score 1.0 by construction (ct IS the correct answer) — not a shortcut.
# hop1 score 0.0 documents ct-intrusion failure reference (ct ≠ bt by construction).
# negative_graph score 0.0 documents endpoint-under-abstention reference (ct ≠ NULL).
c_target = target_chain.get("C_object")
baselines["always_return_ct"] = score(c_target) if c_target else 0.0
```

**Gate 5 reference-only policy:** `always_return_ct` and `always_return_NULL` are reported in the
Gate 5 output table but excluded from the max_det ceiling calculation. Their n/n scores on
composite (always_return_ct) and negative_graph (always_return_NULL) are trivially correct by
construction and are not shortcut signals.

The Gate 5 analysis layer must identify both as reference-only:

```python
GATE5_REFERENCE_ONLY = {"always_return_ct", "always_return_NULL"}
# These dummies are reported in Gate 5 table but excluded from max_det ceiling check.
# Rationale: their high-scoring rows are trivially correct by construction, not shortcuts.
```

Note: this constant belongs in the Gate 5 analysis code (runner or post-processing), not
in the scorer itself. The scorer reports all dummy scores; the Gate 5 layer applies the
ceiling policy.

---

## 4. always_return_NULL — Already in Scorer; Reference-Only Status to Be Made Explicit

**Current implementation** (line 264, no change required to scorer):

```python
"always_return_NULL": score("NULL"),
```

Scores 1.0 on negative_graph (expected == "NULL"), 0.0 on all positive query types.

**Policy clarification required:** `always_return_NULL` scores n/n on negative_graph by
construction (the correct negative_graph answer IS "NULL"). This is the abstention upper bound,
parallel to `always_return_ct` on composite. It must be treated as reference-only in Gate 5
analysis — excluded from max_det ceiling calculation.

**No scorer code change required.** Gate 5 analysis layer must add "always_return_NULL" to
`GATE5_REFERENCE_ONLY`.

---

## 5. §8 ct-Anchoring Diagnostics — Preserved Without Scorer Change

The scorer already captures all information needed for §8 ct-anchoring analysis:

```python
# classify_output() returns:
{
    "failure_class":  ...,      # e.g., FC_WRONG_NEIGHBOR if ct returned on hop1
    "returned_token": token,    # the actual token returned (e.g., "CPQVX" = ct)
    "returned_role":  role,     # role of returned token (e.g., ROLE_ANSWER_C)
    "is_correct":     False,
}
```

A ct-return on hop1 is classified as `FC_WRONG_NEIGHBOR` (ct has role ROLE_ANSWER_C, which is
in TARGET_CHAIN_ROLES) with `returned_token` = the ct token value.

The §8 analyst reads `returned_token` from failed hop1 items and checks:
- How many returned the known ct value?
- What was their `returned_role`?
- What was their context position / C-rank?

**No scorer code change is needed.** The failure class taxonomy and token-capture already support
§8 ct-anchoring analysis. Future Cell03 run summaries must include §8 diagnostics per Team Lead
standing requirement:

```text
hop1 expected bt, returned ct
negative_graph expected NULL, returned endpoint
returned ct vs returned other C endpoint
returned B endpoint vs returned C endpoint
absolute position of returned endpoint
C-rank of returned endpoint
adjacency/proximity of returned endpoint
```

---

## 6. Scorer/Validator File List

```text
Files requiring amendment:
  scorer_twohop_l1.py (sha256:060afad9...)
    — compute_dummy_baseline_scores(): add always_return_second_C, always_return_third_C,
      always_return_ct
    — Unit test section: add T_new_1 through T_new_6 (see §7)

Files NOT requiring amendment (locked, unchanged):
  tasks_twohop_l1.py            — manifest schema, validator (LOCKED)
  smoke_test_twohop_l1.py       — 22 offline checks (LOCKED; no new dummy checks required)
  runner_twohop_l1_cell02.py    — Cell02 runner (LOCKED; not used for Cell03)
  prompt_template_twohop_l1.txt — prompt template (LOCKED)

Files requiring Gate 5 analysis layer update (not scorer code):
  runner_twohop_l1_cell03.py (future)
    — Gate 5 post-processing must include GATE5_REFERENCE_ONLY constant
    — Both always_return_ct and always_return_NULL excluded from max_det ceiling
  Cell03 prep lock packet (future)
    — Must reference amended scorer hash
```

---

## 7. Expected Unit Test Additions

Six new unit tests. All tests reside in the existing `_UNIT_CASES` / `run_unit_tests()` pattern
in scorer_twohop_l1.py, extended with a supplementary dummy-baseline test fixture and test loop.

### Test fixture required

The existing `_TEST_ITEM` has `"context": {"ordered_facts": []}` — no hop2 facts — so
`c_by_pos` is empty. The new dummy tests require a fixture with positioned hop2 facts:

```python
_TEST_ITEM_DUMMIES = {
    "item_id": "UNIT_DUMMY_01",
    "chains": [
        {"chain_id": "decoy_1", "role": "decoy",
         "A_object": "DXQNV", "B_object": "EJMRX", "C_object": "FVPLX"},
        {"chain_id": "target",  "role": "target",
         "A_object": "ARVUX", "B_object": "BMNIX", "C_object": "CPQVX"},
        {"chain_id": "decoy_2", "role": "decoy",
         "A_object": "GVPQX", "B_object": "HJKLX", "C_object": "IMNCX"},
    ],
    "queries": {
        QT_HOP1:      {"expected_answer": "BMNIX", "query_anchor": "ARVUX"},
        QT_HOP2:      {"expected_answer": "CPQVX", "query_anchor": "BMNIX"},
        QT_COMPOSITE: {"expected_answer": "CPQVX", "query_anchor": "ARVUX"},
        QT_NEG_GRAPH: {"expected_answer": "NULL",  "query_anchor": "ARVUX"},
    },
    "context": {"ordered_facts": [
        {"fact_role": "decoy_hop2_fact", "chain_id": "decoy_1", "position_index": 2},
        {"fact_role": "hop2",            "chain_id": "target",  "position_index": 6},
        {"fact_role": "decoy_hop2_fact", "chain_id": "decoy_2", "position_index": 7},
    ]},
}
# c_by_pos = ["FVPLX"(pos2), "CPQVX"(pos6), "IMNCX"(pos7)]
# first_C = FVPLX, second_C = CPQVX (= ct), third_C = last_C = IMNCX
```

### Test cases

```text
T_new_1: always_return_second_C — composite
  item = _TEST_ITEM_DUMMIES, query_type = composite
  expected: score == 1.0   (second_C = CPQVX = expected composite answer)
  tests: second_C returns c_by_pos[1] correctly

T_new_2: always_return_second_C — hop1
  item = _TEST_ITEM_DUMMIES, query_type = hop1
  expected: score == 0.0   (second_C = CPQVX ≠ BMNIX = expected hop1 answer)
  tests: second_C scores 0 where C endpoint is wrong

T_new_3: always_return_third_C — composite (3 C-endpoints)
  item = _TEST_ITEM_DUMMIES, query_type = composite
  expected: score == 0.0   (third_C = IMNCX ≠ CPQVX)
  tests: third_C returns c_by_pos[2] correctly when len(c_by_pos) >= 3

T_new_4: always_return_third_C — guard (fewer than 3 C-endpoints)
  item = _TEST_ITEM (context.ordered_facts = []) so c_by_pos = []
  query_type = composite
  expected: score == 0.0   (graceful fallback, no IndexError)
  tests: third_C guard handles empty / short c_by_pos without exception

T_new_5: always_return_ct — hop1
  item = _TEST_ITEM_DUMMIES, query_type = hop1
  expected: score == 0.0   (ct = CPQVX ≠ BMNIX = expected hop1 answer)
  tests: always_return_ct returns 0.0 on hop1 (ct-intrusion reference score)

T_new_6: always_return_ct — composite
  item = _TEST_ITEM_DUMMIES, query_type = composite
  expected: score == 1.0   (ct = CPQVX = expected composite answer)
  tests: always_return_ct returns 1.0 on composite (trivially correct by construction)

Regression:
  All 14 existing unit tests must pass without modification.
  Run run_unit_tests() against original _TEST_ITEM and _UNIT_CASES unchanged.
```

Total new tests: 6 (T_new_1 through T_new_6).
Total tests after amendment: 20 (14 existing + 6 new).

---

## 8. Re-Lock Plan and Hash Placeholders

```text
Step 0 — [CURRENT] Dummy policy confirmed by Team Lead (R3)
  Standing caveats in force. always_return_query_role_object retired.
  Senior Engineer confirmation pending.

Step 1 — Senior Engineer confirmation of Gate 5 / §8 split
  Senior confirms R3 is technically sound before Manager routing.

Step 2 — Manager authorization for scorer amendment
  Authorization request must explicitly name:
    (a) Dummies added: always_return_second_C, always_return_third_C, always_return_ct
    (b) Dummy NOT added: always_return_query_role_object (retired)
    (c) Reference-only policy confirmed for: always_return_ct, always_return_NULL
    (d) New unit test count: 6 (T_new_1 through T_new_6)
    (e) Current scorer hash: sha256:060afad9...
  Scorer amendment is NOT authorized until Manager explicitly approves.

Step 3 — CS drafts scorer amendment offline
  Edits to compute_dummy_baseline_scores() only.
  Adds _TEST_ITEM_DUMMIES fixture and T_new_1 through T_new_6 test cases.
  run_unit_tests() must pass all 20 tests.

Step 4 — New sha256 hash computed and locked
  After amendment: compute new hash.
  Hash placeholder: sha256:[CELL03-SCORER-HASH-TBD]
  This placeholder must be replaced with the actual hash before Cell03 Stage 0 lock.

Step 5 — EXPERIMENT_LOG.md and STAGE-FILES table updated
  sha256:060afad9... → sha256:[CELL03-SCORER-HASH-TBD]
  Amendment note filed in log.

Step 6 — Cell03 Stage 0 lock packet
  Must reference sha256:[CELL03-SCORER-HASH-TBD].
  No Cell03 Stage 0 lock may be filed with sha256:060afad9...

Step 7 — Cell03 Stage 1 prep lock and runner amendment
  runner_twohop_l1_cell03.py must include GATE5_REFERENCE_ONLY constant.
  Dry-run must pass before Stage 1 lock.

Step 8 — Cell03 Stage 1 execution authorization (separate)
  Separate authorization from construction authorization.
```

---

## 9. Cell01 and Cell02 — Not Retroactively Rescored

The scorer amendment adds new dummy baselines only. It does not change:

```text
Unchanged:
  classify_output() — failure class scoring logic unchanged
  score_scaffold(), score_format(), _extract_answer_token() — unchanged
  compute_uniform_random_expected() — unchanged
  _c_objects_by_context_position() — unchanged
  FAILURE_TAXONOMY_VERSION — "v1.0", unchanged
  All 14 existing unit tests — must pass without modification

Existing baselines (unchanged):
  always_return_B_target      — already in scorer
  always_return_anchor_A      — already in scorer
  always_return_first_C       — already in scorer
  always_return_last_C        — already in scorer
  always_return_NULL          — already in scorer (reference-only policy clarified, no code change)
  always_return_C_decoy_{i}   — already in scorer
  uniform_random_expected     — already in scorer
```

Cell01 and Cell02 filed results:

```text
RESULTS-TWOHOP-L1-cell01-1780912218.json — scored with sha256:f346e4f2... (runner hash)
  using scorer sha256:060afad9... — FINAL, NOT RESCORED

RESULTS-TWOHOP-L1-cell02-1780933041.json — scored with runner hash sha256:d14f6424...
  using scorer sha256:060afad9... — FINAL, NOT RESCORED

Cell01 and Cell02 run summaries and map entries are locked.
The scorer amendment applies to Cell03 and future cells only.
No retroactive Gate 5 recalculation for Cell01 or Cell02 is authorized or required.
The Cell02 Gate 5 PASS* (with documented always_return_second_C coverage gap) stands as filed.
```

---

## Summary of Amendment Scope

```text
File amended:         scorer_twohop_l1.py (sha256:060afad9... → sha256:[CELL03-SCORER-HASH-TBD])
Function modified:    compute_dummy_baseline_scores() — three additions only

Dummies ADDED (ceiling-bearing):
  always_return_second_C   — c_by_pos[1]; guarded (len >= 2)
  always_return_third_C    — c_by_pos[2]; guarded (len >= 3)

Dummy ADDED (reference-only, Gate 5 excluded):
  always_return_ct         — target_chain["C_object"]

Dummy NOT added (reference-only, already exists):
  always_return_NULL       — already implemented; Gate 5 reference policy clarified, no code change

Dummy NOT added (retired):
  always_return_query_role_object — retired; must not appear in scorer

Unit tests:           +6 new (T_new_1 through T_new_6); total 20 after amendment
Authorization needed: Manager (Step 2 above)
```

---

**Scorer-amendment planning packet filed. Awaiting Senior Engineer confirmation (Gate 5 / §8 split) and Manager authorization before amendment proceeds.**

— CS Engineer, 2026-06-08
