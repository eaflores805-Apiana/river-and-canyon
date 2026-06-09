# Cell03 Scorer Re-Lock Packet

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Requested by:** Team Lead memo — "Authorized — Execute Cell03 Scorer Amendment Only" 2026-06-08
**Prior scorer hash:** sha256:060afad9...
**Amended scorer hash:** sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde
**Status:** FILED — awaiting Team Lead review before Cell03 construction proceeds

---

## 1. Amended Scorer File

```text
File:             scorer_twohop_l1.py
Prior hash:       sha256:060afad9...
Amended hash:     sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde
Amendment scope:  compute_dummy_baseline_scores() — three additions
                  _TEST_ITEM_DUMMY_A, _TEST_ITEM_DUMMY_B fixtures added
                  _DUMMY_BASELINE_CASES, run_dummy_baseline_tests() added
                  __main__ updated to call run_dummy_baseline_tests()
```

Changes to `compute_dummy_baseline_scores()`:

```python
# Added variable:
c_target  = target_chain.get("C_object")

# Added to baselines dict (between always_return_first_C and always_return_last_C):
"always_return_second_C":  score(c_by_pos[1])  if len(c_by_pos) >= 2 else 0.0,
"always_return_third_C":   score(c_by_pos[2])  if len(c_by_pos) >= 3 else 0.0,

# Added to baselines dict (between always_return_last_C and always_return_NULL):
"always_return_ct":        score(c_target),
```

Nothing else in the scorer was modified:
- `classify_output()` — unchanged
- `FAILURE_TAXONOMY_VERSION` — unchanged ("v1.0")
- `_c_objects_by_context_position()` — unchanged
- `compute_uniform_random_expected()` — unchanged
- All 14 existing `_UNIT_CASES` — unchanged

---

## 2. Amended Analysis / Validator File List

```text
tasks_twohop_l1.py            — NOT modified (LOCKED)
smoke_test_twohop_l1.py       — NOT modified (LOCKED)
runner_twohop_l1_cell02.py    — NOT modified (Cell02 runner, LOCKED)
prompt_template_twohop_l1.txt — NOT modified (LOCKED)
```

No validator or analysis files were modified. The Gate 5 reference-only policy for
`always_return_ct` and `always_return_NULL` is implemented in the Cell03 runner/analysis
layer (not yet constructed) via the `GATE5_REFERENCE_ONLY` constant documented in
CELL03-SCORER-AMENDMENT-PLAN.md.

---

## 3. Full Test Output — 20/20

```text
$ python scorer_twohop_l1.py

Unit tests: 14/14 passed
Dummy baseline tests: 6/6 passed
FAILURE_TAXONOMY_VERSION: v1.0
scorer_hash: sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde
```

**Total: 20/20 tests passed.**

Test breakdown:

```text
Existing (14/14):
  composite correct, hop1 correct, hop2 correct, negative_graph NULL correct,
  no scaffold prefix, non-context token, NULL on positive query, composite stopped-short,
  composite anchor echo (A), hop1 anchor echo (A), hop2 anchor echo (B),
  decoy chain endpoint, decoy chain intermediate, target neighbor decoy

New (6/6):
  T_new_1: second_C functionality — ct at rank 2, composite = 1.0         PASS
  T_new_2: second_C tautology guard — ct at rank 1, composite = 0.0       PASS
  T_new_3: third_C functionality — third_C=cd2 ≠ ct, composite = 0.0     PASS
  T_new_4: third_C guard — empty c_by_pos, returns 0.0, no IndexError     PASS
  T_new_5: always_return_ct hop1 reference — ct ≠ bt, score = 0.0         PASS
  T_new_6: always_return_ct composite reference — trivially 1.0            PASS
```

---

## 4. Updated Scorer Hash

```text
sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde
```

Short form used in filings: `sha256:b65c6803...`

This hash must replace `sha256:060afad9...` in all Cell03 preparation and lock documents.
It must NOT be applied retroactively to Cell01 or Cell02 documents.

---

## 5. Updated Validator / Analysis Hash

Not applicable. No validator or analysis files were modified.

---

## 6. Dummy Manifest — Ceiling-Bearing vs Reference-Only

```text
CEILING-BEARING (subject to Gate 5 max_det ≤ 9/24 ceiling):
  always_return_first_C       returns c_by_pos[0];   existed prior to amendment
  always_return_second_C      returns c_by_pos[1];   ADDED this amendment
  always_return_third_C       returns c_by_pos[2];   ADDED this amendment (guarded)
  always_return_last_C        returns c_by_pos[-1];  existed prior to amendment
  Note: for R=3 (Two-Hop L1), third_C == last_C; both reported explicitly.

REFERENCE-ONLY (reported in Gate 5 table; excluded from max_det ceiling):
  always_return_ct            returns c_target;      ADDED this amendment
    Rationale: scores n/n on hop2/composite by construction (ct IS the correct answer).
               Scores 0/n on hop1 and negative_graph.
               Reference diagnostic — target-token upper bound; not a shortcut signal.
  always_return_NULL          returns "NULL";        existed prior to amendment
    Rationale: scores n/n on negative_graph by construction (NULL IS the correct answer).
               Scores 0/n on all positive query types.
               Reference diagnostic — abstention upper bound; not a shortcut signal.

ADDITIONAL BASELINES (not Gate 5 ceiling dummies; diagnostic reference):
  always_return_B_target      returns b_target;      existed prior to amendment
  always_return_anchor_A      returns anchor_a;      existed prior to amendment
  always_return_C_decoy_{i}   returns decoy_i C;     existed prior to amendment
  uniform_random_expected     closed-form chance;    existed prior to amendment

RETIRED (not in scorer; must not appear in Gate 5 analysis):
  always_return_query_role_object       — retired (see CELL03-DUMMY-POLICY-RESPONSE-R3.md)
  always_return_most_recent_role_match  — retired
  always_return_answer_shaped           — retired
```

---

## 7. always_return_query_role_object Absent from Gate 5 max_det

```text
Confirmed absent.

always_return_query_role_object is not implemented in scorer_twohop_l1.py.
It does not appear in compute_dummy_baseline_scores() output.
It does not appear in any Gate 5 calculation.
The name does not appear anywhere in the amended scorer file.
```

---

## 8. always_return_ct and always_return_NULL Excluded from max_det

```text
Policy confirmed (Gate 5 analysis layer):
  GATE5_REFERENCE_ONLY = {"always_return_ct", "always_return_NULL"}

Both dummies score n/n on one query type by construction:
  always_return_ct:   n/n on hop2 and composite (ct IS the correct answer)
  always_return_NULL: n/n on negative_graph (NULL IS the correct answer)

Making either ceiling-bearing would trivially fail Gate 5 for every correctly
constructed cell. Both are reference-only — they document upper bounds, not shortcuts.

Implementation requirement:
  The Cell03 runner/analysis layer must implement GATE5_REFERENCE_ONLY.
  Both dummies must be reported in the Gate 5 table with label "(ref only)".
  Neither may be included in the max_det ceiling calculation.
  Their n/n scores on their trivially-correct query types do not constitute
  Gate 5 failures and cannot rescue or erase ceiling failures from
  ceiling-bearing rank dummies.
```

---

## 9. Cell01 / Cell02 Model Outputs Remain Frozen

```text
Cell01 model output:
  RESULTS-TWOHOP-L1-cell01-1780912218.json — sha256:6de8b67c...
  Scored with scorer sha256:060afad9... (prior hash)
  Status: FROZEN — not rescored, not modified

Cell02 model output:
  RESULTS-TWOHOP-L1-cell02-1780933041.json — sha256:47b5eaa9...
  Scored with scorer sha256:060afad9... (prior hash)
  Status: FROZEN — not rescored, not modified

The amended scorer (sha256:b65c6803...) was NOT used to rescore Cell01 or Cell02.
Their filed results, Gate 5 dispositions, and map entries are unchanged.
The offline Cell02 computation below (§10) used only the item manifest —
no model output file was read or modified.
```

---

## 10. Offline Cell02 always_return_second_C Baseline Computation

**Method:** deterministic Python — loaded `items_twohop_l1_cell02.json` (manifest only),
called `compute_dummy_baseline_scores(item, "composite")["always_return_second_C"]` for
all 24 items using the amended scorer. No model output file was accessed.

**Result:**

```text
Cell02 always_return_second_C composite: 24/24 = 1.0000
All 24 items: always_return_second_C == 1.0
```

**Sample item confirmation (item twohop_l1_c02_i01):**

```text
c_by_pos:             ['LVQLN', 'RRWRO', 'VBLTH']
ct (target C_object): RRWRO
second_C:             RRWRO  (= ct; c_by_pos[1] at position rank 2)
always_return_second_C composite:  1.0  (RRWRO == expected composite answer)
always_return_ct composite:        1.0  (reference-only; ct == correct composite)
always_return_ct hop1:             0.0  (ct ≠ bt; correct reference behavior)
always_return_NULL negative_graph: 1.0  (reference-only; NULL == correct neg_graph answer)
```

**Interpretation:**

```text
For all 24 Cell02 items: c_by_pos[1] = ct.
This confirms ct was fixed as second_C for every Cell02 item.

always_return_second_C composite = 24/24 = 1.000
24/24 > Gate 5 ceiling (9/24 = 0.375) → Gate 5 FAIL for composite.

This is the Gate 5 coverage gap documented in CELL02-GATE5-POSITIONAL-DUMMY-AUDIT.md.
Cell02 Gate 5 disposition (PASS* with caveat) is confirmed correct:
  Current dummies (first_C, last_C) passed at 0/24.
  Missing dummy (second_C) would have failed at 24/24.
  Cell02 is shortcut-exposed via always_return_second_C under all-C_target-last design.
  Cell03's balanced design prevents ct from being fixed at second_C for all items.
```

---

## Scorer Amendment Summary

```text
Prior:    sha256:060afad9...
Amended:  sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde

Added ceiling-bearing:     always_return_second_C, always_return_third_C
Added reference-only:      always_return_ct
Confirmed reference-only:  always_return_NULL (already present; policy now documented)
Retired:                   always_return_query_role_object (and prior names)

Tests: 20/20 passed (14 existing regression + 6 new)
All 14 existing unit tests: unchanged and passing
Cell01/Cell02 model outputs: frozen
```

**Scorer re-lock packet filed. Awaiting Team Lead review before Cell03 construction is unblocked.**

— CS Engineer, 2026-06-08
