# Cell03 Dummy Policy Confirmation Packet — Two-Hop Level 1

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Requested by:** Team Lead memo — "Cell02 / Cell03 Filing Updates Received — Dummy Policy Confirmation Next" 2026-06-08
**Status:** PARTIALLY SUPERSEDED — see CELL03-DUMMY-POLICY-CLARIFICATION-R1.md
  Superseded sections: §2 (always_return_ct policy), §3 (answer_shaped definition and name), §5 final dummy list
  §1 (full-rank C coverage), §4 (scorer amendment required), §5 re-lock plan: remain in force

---

## Purpose

This packet provides the dummy-policy confirmation required before any scorer amendment or Cell03 construction authorization. It covers the six required points requested by Team Lead.

---

## 1. Full-Rank C Dummy Coverage Definition

For any construction with ranked C-endpoints (i.e., multiple C-type objects in the context), Gate 5 must include the following dummies:

```text
always_return_first_C
  Returns c_by_pos[0] — the C-endpoint appearing earliest in the context by position_index.
  Already in scorer (sha256:060afad9...).

always_return_second_C
  Returns c_by_pos[1] — the C-endpoint at rank 2 by context position.
  NEW — required for any construction with 2+ C-endpoints.
  NOT in current scorer.

always_return_third_C
  Returns c_by_pos[2] — the C-endpoint at rank 3 by context position.
  NEW — required if the construction has 3+ C-endpoints (Cell03 has cd1, ct, cd2: 3 endpoints).
  NOT in current scorer.

always_return_last_C
  Returns c_by_pos[-1] — the C-endpoint appearing latest in context by position_index.
  Already in scorer. For Cell02/Cell03 constructions with 3 C-endpoints:
    last_C == third_C, so always_return_third_C and always_return_last_C return the same value.
  Both must still be included explicitly (third_C by rank label; last_C by position label).

always_return_ct
  Returns the target chain's C_object (ct) regardless of query type.
  NEW — required for all Cell03 constructions.
  NOT in current scorer.
  Gate 5 policy: reference-only (see §2).
```

**Standing policy:** Gate 5 must include the full ranked-C set for all future constructions.
No construction may use a scorer that omits any applicable ranked-C dummy.

For Cell03 (3 C-endpoints: cd1, ct, cd2), the required Gate 5 dummy set is:

```text
always_return_first_C      (existing)
always_return_second_C     (NEW)
always_return_third_C      (NEW)
always_return_last_C       (existing)
always_return_ct           (NEW — reference-only)
always_return_answer_shaped (NEW — see §3)
```

---

## 2. always_return_ct Definition

```text
Inputs:   item (dict), query_type (str)
Returns:  item["chain"]["c_target"]  for all query types

Score:
  score(item, query_type) = 1.0 if ct == expected_answer(item, query_type) else 0.0

Expected scores under correct construction:
  hop1:           0/n  — expected answer is bt; ct ≠ bt by construction
  hop2:           n/n  — expected answer is ct; trivially correct
  composite:      n/n  — expected answer is ct; trivially correct
  negative_graph: 0/n  — expected answer is NULL; ct is not NULL

Gate 5 ceiling policy:
  always_return_ct is EXCLUDED from the max_det ceiling calculation.
  Its composite n/n score is an expected upper-bound anchor, not a Gate 5 failure signal.
  It is recorded in the Gate 5 table as a reference row, labeled (ref only).
  All other dummies remain subject to max_det ≤ 9/24.

Rationale:
  always_return_ct is informative because it quantifies the "always return the right token"
  composite upper bound. The model's composite correct rate can then be assessed relative
  to this anchor — a correct composite score near n/n is consistent with always_return_ct
  behavior; a low composite score is not.
  For Cell03, ct will not be fixed at a single position or C-rank across items (balance
  requirement). If the model still scores high on composite relative to always_return_ct,
  the composite correct rate cannot be explained by fixed-rank or fixed-position shortcuts.
```

---

## 3. always_return_answer_shaped Operational Definition

```text
Inputs:   item (dict), query_type (str)
Returns:  object of the most recently seen relation fact (by context position_index)
          whose relation type matches the query's expected relation type, defined as:

    hop1 expected relation:         "links to"
      → returns the object of the last "links to" fact in the context
        (by ascending position_index)
      → under current two-hop construction: returns bt (same as always_return_B_target)

    hop2 expected relation:         "maps to"
      → returns the object of the last "maps to" fact whose subject is the query anchor
      → under current two-hop construction: returns ct (same as always_return_ct)

    composite expected relation:    "maps to" (composite query resolves via the two-hop chain)
      → same as hop2 lookup
      → under current two-hop construction: returns ct

    negative_graph:                 NULL
      → no valid "maps to" chain exists (hop2 fact removed); answer-shaped = NULL
      → same as always_return_NULL

Numerical equivalence under current construction:
  hop1:           ≡ always_return_B_target
  hop2:           ≡ always_return_ct
  composite:      ≡ always_return_ct
  negative_graph: ≡ always_return_NULL

Why include despite numerical equivalence:
  (a) Formally closes the answer-domain salience hypothesis for Cell03.
      The cue "ct is more answer-shaped than cd1 or cd2" can be explicitly scored and
      compared rather than left as an informal argument.
  (b) Becomes independently informative in future constructions where:
      — multiple "maps to" facts compete for the same anchor
      — relation types vary across items
      — answer-shaped token differs structurally from the pure ct / bt by-construction label
  (c) Documenting the definition now locks it before scorer amendment, preventing
      post-hoc definitional drift.

Status: PROPOSED — requires Team Lead and Senior confirmation before scorer amendment.
Implementation requirement: scorer must implement this dummy explicitly; it may not
remain informal. A confirmed implementation must be reviewed before scorer amendment.
```

---

## 4. Scorer Amendment Required?

**Yes. Scorer amendment is required.**

The current scorer (sha256:060afad9..., LOCKED) does not include:

```text
always_return_second_C       — not implemented
always_return_third_C        — not implemented
always_return_ct             — not implemented
always_return_answer_shaped  — not implemented
```

No Cell03 Gate 5 run may proceed without the amended scorer.
The amendment requires Manager authorization and a new hash lock before any use.

---

## 5. Affected File(s), Expected Test Additions, Re-Lock Plan

### 5.1 Affected file

```text
scorer_twohop_l1.py  (sha256:060afad9...)
```

No other instrument files are affected by the dummy additions.

### 5.2 Expected test additions

The amendment must add or extend the following:

```text
compute_dummy_baseline_scores(item, query_type):
  Add:
    "always_return_second_C":     c_by_pos[1]
    "always_return_third_C":      c_by_pos[2]  (guarded: only if len(c_by_pos) >= 3)
    "always_return_ct":           item["chain"]["c_target"]
    "always_return_answer_shaped": per §3 operational definition above

Gate 5 scoring logic:
  Exclude always_return_ct from max_det ceiling computation.
  Record it as a reference row in Gate 5 output.
  All other new dummies included in ceiling check.
```

Unit test additions required (minimum):

```text
T_new_1: always_return_second_C returns c_by_pos[1] for all query types
T_new_2: always_return_third_C returns c_by_pos[2] for all query types;
         raises or returns None gracefully if len(c_by_pos) < 3
T_new_3: always_return_ct returns item["chain"]["c_target"] for all query types
T_new_4: always_return_ct excluded from max_det ceiling; recorded as reference row
T_new_5: always_return_answer_shaped returns bt for hop1, ct for hop2/composite,
         NULL for negative_graph under standard two-hop construction
T_new_6: amended scorer passes all 14 existing unit tests (regression)
```

Minimum: 6 new unit tests (T_new_1 through T_new_6), all must pass before lock.

### 5.3 Re-lock plan

```text
Step 1 — Dummy policy confirmation
  Team Lead and Senior confirm or revise:
    (a) always_return_answer_shaped operational definition (§3)
    (b) always_return_ct Gate 5 exclusion policy (§2)
    (c) third_C handling when len(c_by_pos) < 3
  CS addresses any revisions before proceeding.

Step 2 — Amendment draft
  CS drafts scorer amendment offline.
  Adds four new dummies to compute_dummy_baseline_scores().
  Adds T_new_1 through T_new_5 unit tests.
  Verifies all 14 existing unit tests pass (T_new_6).

Step 3 — Manager authorization
  CS submits scorer amendment for Manager authorization.
  Authorization must explicitly cover:
    — four new dummies by name
    — Gate 5 ceiling exclusion for always_return_ct
    — new unit test count
  Current scorer hash referenced in authorization request: sha256:060afad9...

Step 4 — New hash lock
  After Manager authorization, amend scorer_twohop_l1.py.
  Compute new sha256 hash.
  File amended hash in EXPERIMENT_LOG.md and STAGE-FILES table.
  Update all references to scorer hash in Cell03 prep documentation.

Step 5 — Stage 0 lock
  Cell03 Stage 0 lock packet must reference amended scorer hash.
  No Cell03 Stage 0 lock may be filed with sha256:060afad9...

Step 6 — Stage 1 preparation lock
  Cell03 runner must be amended to use updated scorer.
  Dry-run must pass with amended scorer before Stage 1 lock.
```

---

## 6. Cell03 Construction Status

**Cell03 construction remains BLOCKED.**

The following must be resolved in order before construction is authorized:

```text
[PENDING] Step 0 — Dummy policy confirmation
  Team Lead and Senior must confirm or revise:
    always_return_answer_shaped operational definition
    always_return_ct Gate 5 exclusion policy
    Full-rank C dummy set for Cell03
  This packet constitutes the CS policy proposal.
  Construction is blocked at this step.

[NOT YET STARTED] Step 1 — Scorer amendment
  Manager authorization required.
  New scorer hash required.
  Blocked on Step 0.

[NOT YET STARTED] Step 2 — Manager authorization for Cell03 construction
  Must cover: adjacency axis + position/C-rank balance + scorer amendment scope.
  Blocked on Step 1.

[NOT YET STARTED] Step 3 — Cell03 design specification
  Team Lead review required.
  Must specify context arrangement, position-balance strategy,
  C-rank variation method, n_items, RNG seed.
  Blocked on Step 2.

[NOT YET STARTED] Steps 4–8 — Token audit, Stage 0 lock, threshold review,
  Stage 1 prep, Stage 1 execution authorization.
  All blocked on upstream steps.
```

No Cell03 item generation, token pool construction, runner preparation, or model inference
is authorized at this time.

---

**Dummy-policy confirmation packet filed. Awaiting Team Lead and Senior confirmation of §3 (always_return_answer_shaped definition) and §2 (always_return_ct Gate 5 exclusion policy) before scorer amendment proceeds.**

— CS Engineer, 2026-06-08
