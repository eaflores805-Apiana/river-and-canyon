# Cell03 Scorer Amendment — Pre-Lock Confirmations

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Requested by:** Team Lead memo — "Senior Confirmation Received — Cell03 Scorer Amendment May Route to Manager with Re-lock Conditions" 2026-06-08
**Preconditions addressed:** three conditions listed in Team Lead §5 before scorer re-lock
**Status:** FILED — confirmations for Manager routing preparation

---

## Confirmation 1 — Fixed C-Object Count R

**R = 3. R ∈ {3, 4}. Full-rank coverage confirmed.**

```text
Two-Hop Level 1 construction (Cell01, Cell02, Cell03):
  Chains per item:    3  (1 target + 2 decoy)
  C-objects per item: 3  (ct from target chain; cd1, cd2 from decoy chains)
  R = 3

Full-rank dummy set for R = 3:
  always_return_first_C    → c_by_pos[0]   (rank 1)
  always_return_second_C   → c_by_pos[1]   (rank 2)
  always_return_third_C    → c_by_pos[2]   (rank 3)
  always_return_last_C     → c_by_pos[-1]  (rank last = rank 3 when R = 3)

Coverage gap analysis:
  R = 3 → third_C == last_C.
  Both dummies are included explicitly:
    always_return_third_C  — referenced by ordinal label "third"
    always_return_last_C   — referenced by positional label "last"
  When R = 3, both return the same object.
  Both are reported separately in the Gate 5 table.
  There is no uncovered rank gap.

If R ≥ 5 in a future construction:
  Intermediate ranks between third_C and last_C would need to be added.
  This confirmation applies to Cell03 only (R = 3).
  Future constructions with R ≥ 5 require a separate dummy-set review.
```

**Disambiguation rule for C-objects at multiple positions:**

The scorer's `_c_objects_by_context_position()` already handles this case (lines 233–235):

```python
if c_obj not in c_pos or pos < c_pos[c_obj]:
    c_pos[c_obj] = pos
```

**Rule: use the earliest (lowest) position_index occurrence.**

Under Two-Hop Level 1 construction, each C-object appears in exactly one hop2-type fact per item — multiple-position appearances are not expected. The guard is defensive. The rule is: if a C-object appears in more than one hop2-type fact, it is assigned the position of the first (lowest index) such fact.

This rule is confirmed and will be documented in the amendment note within the scorer.

---

## Confirmation 2 — T_new_1 Through T_new_6 Enumerated

All six tests are specified below, satisfying:

```text
(a) tautology guard: no ceiling-bearing dummy scores n/n by acting as a perfect solver
(b) full-rank completeness
(c) ct / NULL excluded from max_det
(d) second_C functionality
(e) third_C functionality
(f) balanced fixture with ct appearing at different ranks
```

### Test fixtures

Two fixtures required (ct at different ranks):

**Fixture_A — ct at rank 2 (second_C)**

```python
_TEST_ITEM_DUMMY_A = {
    "item_id": "UNIT_DUMMY_A",
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
# first_C = FVPLX (cd1)
# second_C = CPQVX (ct)     ← ct is at rank 2
# third_C = last_C = IMNCX (cd2)
```

**Fixture_B — ct at rank 1 (first_C)**

```python
_TEST_ITEM_DUMMY_B = {
    "item_id": "UNIT_DUMMY_B",
    "chains": [
        {"chain_id": "target",  "role": "target",
         "A_object": "ARVUX", "B_object": "BMNIX", "C_object": "CPQVX"},
        {"chain_id": "decoy_1", "role": "decoy",
         "A_object": "DXQNV", "B_object": "EJMRX", "C_object": "FVPLX"},
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
        {"fact_role": "hop2",            "chain_id": "target",  "position_index": 2},
        {"fact_role": "decoy_hop2_fact", "chain_id": "decoy_1", "position_index": 5},
        {"fact_role": "decoy_hop2_fact", "chain_id": "decoy_2", "position_index": 7},
    ]},
}
# c_by_pos = ["CPQVX"(pos2), "FVPLX"(pos5), "IMNCX"(pos7)]
# first_C = CPQVX (ct)      ← ct is at rank 1
# second_C = FVPLX (cd1)
# third_C = last_C = IMNCX (cd2)
```

### Test cases

```text
T_new_1 — second_C functionality
  fixture:     Fixture_A (ct at rank 2)
  query_type:  composite
  call:        compute_dummy_baseline_scores(Fixture_A, QT_COMPOSITE)["always_return_second_C"]
  expected:    1.0   (second_C = CPQVX = ct = expected composite answer)
  satisfies:   (d) second_C functionality; (b) full-rank completeness

T_new_2 — second_C tautology guard
  fixture:     Fixture_B (ct at rank 1)
  query_type:  composite
  call:        compute_dummy_baseline_scores(Fixture_B, QT_COMPOSITE)["always_return_second_C"]
  expected:    0.0   (second_C = FVPLX = cd1 ≠ CPQVX = ct — not the correct answer)
  satisfies:   (a) tautology guard — second_C does NOT score n/n when ct is not pinned to rank 2;
               (f) balanced fixture — verifies rank sensitivity using ct at a different rank

T_new_3 — third_C functionality
  fixture:     Fixture_A (ct at rank 2; third_C = cd2)
  query_type:  composite
  call:        compute_dummy_baseline_scores(Fixture_A, QT_COMPOSITE)["always_return_third_C"]
  expected:    0.0   (third_C = IMNCX = cd2 ≠ CPQVX = ct)
  satisfies:   (e) third_C functionality — returns c_by_pos[2] correctly even when ≠ ct

T_new_4 — third_C guard (R < 3)
  fixture:     _TEST_ITEM (context.ordered_facts = [] → c_by_pos = [])
  query_type:  composite
  call:        compute_dummy_baseline_scores(_TEST_ITEM, QT_COMPOSITE)["always_return_third_C"]
  expected:    0.0   (graceful fallback — no IndexError when len(c_by_pos) < 3)
  satisfies:   (e) third_C guard behavior

T_new_5 — always_return_ct reference (hop1 = 0.0)
  fixture:     Fixture_A
  query_type:  hop1
  call:        compute_dummy_baseline_scores(Fixture_A, QT_HOP1)["always_return_ct"]
  expected:    0.0   (ct = CPQVX ≠ BMNIX = expected hop1 answer; ct ≠ bt by construction)
  satisfies:   (c) ct excluded from max_det — hop1 reference score confirms 0/n behavior;
               documents ct-intrusion failure reference (ct wrong on hop1)

T_new_6 — always_return_ct reference (composite = 1.0)
  fixture:     Fixture_A
  query_type:  composite
  call:        compute_dummy_baseline_scores(Fixture_A, QT_COMPOSITE)["always_return_ct"]
  expected:    1.0   (ct = CPQVX = expected composite answer; trivially correct by construction)
  satisfies:   (c) ct excluded from max_det — composite reference score 1.0 by construction;
               confirms reference-only classification rationale (n/n composite is not a shortcut)
```

**Regression confirmation:** all 14 existing `_UNIT_CASES` tests must pass without modification against `_TEST_ITEM`. These tests cover `classify_output()` only and are unaffected by `compute_dummy_baseline_scores()` additions.

**Total after amendment: 20 tests (14 existing + 6 new).**

---

## Confirmation 3 — Cell01 / Cell02 Model Results Frozen

```text
Cell01 model output (locked):
  RESULTS-TWOHOP-L1-cell01-1780912218.json — sha256:6de8b67c...
  Scored with scorer sha256:060afad9...
  Model outputs: frozen. Not rescored. Not modified.

Cell02 model output (locked):
  RESULTS-TWOHOP-L1-cell02-1780933041.json — sha256:47b5eaa9...
  Scored with scorer sha256:060afad9...
  Model outputs: frozen. Not rescored. Not modified.
```

**Offline baseline computation scope (authorized per Team Lead §7):**

```text
Allowed:
  Run compute_dummy_baseline_scores() (amended version) on:
    items_twohop_l1_cell01.json   (manifest only — no model outputs)
    items_twohop_l1_cell02.json   (manifest only — no model outputs)
  to compute the missing dummy baselines (always_return_second_C, always_return_third_C,
  always_return_ct) for all 24 items in each cell.

  This is a metadata computation:
    input:  item manifest (chains, context, queries) — no model outputs
    output: dummy baseline scores for the new dummies
    method: deterministic Python function, no model inference

  The Cell02 always_return_second_C composite score is expected to be 24/24 (n/n),
  confirming the documented Gate 5 PASS* coverage gap.

Not allowed:
  Any modification to model output files.
  Any retroactive Gate 5 PASS/FAIL reclassification of Cell01 or Cell02.
  Any inference, rerun, or confirmation pass.
```

**Offline computation does not change the Cell01/Cell02 filed results or Gate 5 dispositions.** It provides a reference record of what the new dummies would have scored on existing constructions, which may inform future Cell03 interpretation.

---

## Summary — Conditions Met

```text
Condition 1 — R ∈ {3,4}: CONFIRMED (R = 3 for Cell01/02/03)
  Disambiguation rule: earliest position_index (already in scorer; to be documented in amendment)
  Future constructions with R ≥ 5: require separate dummy-set review

Condition 2 — T_new_1 through T_new_6: ENUMERATED
  Two balanced fixtures: Fixture_A (ct at rank 2), Fixture_B (ct at rank 1)
  All six required properties satisfied
  Total test count after amendment: 20

Condition 3 — Cell01/Cell02 frozen: CONFIRMED
  Offline baseline computation authorized on manifests only
  Model outputs unchanged; Gate 5 dispositions unchanged
```

**All three pre-lock conditions are satisfied. Scorer amendment is eligible for Manager routing.**

Manager authorization request must specify:
```text
File:             scorer_twohop_l1.py (sha256:060afad9...)
Function amended: compute_dummy_baseline_scores()
Dummies added:    always_return_second_C, always_return_third_C (ceiling-bearing)
                  always_return_ct (reference-only)
Dummies retired:  always_return_query_role_object (and equivalent names)
Unit tests added: 6 (T_new_1 through T_new_6); total 20 after amendment
C-object count:   R = 3 for Cell03
New hash:         sha256:[CELL03-SCORER-HASH-TBD]
```

Cell03 construction remains blocked until scorer re-lock is complete.

---

— CS Engineer, 2026-06-08
