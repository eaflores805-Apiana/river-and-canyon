# Cell03 Dummy Policy Response — Revision 2

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Requested by:** Team Lead memo — "Cell03 Dummy Policy — Three Definition Questions Before Scorer Amendment" 2026-06-08
**Supersedes:** CELL03-DUMMY-POLICY-CLARIFICATION-R1.md §1 (always_return_ct ceiling status), §4 (negative_graph policy), §5 (dummy name), §6 (final list)
**Prior documents:** CELL03-DUMMY-POLICY-CONFIRMATION.md → CELL03-DUMMY-POLICY-CLARIFICATION-R1.md → this document
**Status:** SUPERSEDED on §2–§4 by CELL03-DUMMY-POLICY-RESPONSE-R3.md
  always_return_query_role_object retired from ceiling-bearing set (incoherent as ceiling dummy)
  §1 (always_return_ct reference-only), §3 (naming), §5 (R1 supersession): remain in force
**Amendment (2026-06-08):** §2 and §4 revised per Team Lead direction — endpoint-attraction dummy
  returns endpoint token (ct) on negative_graph and scores 0; NULL-returning behavior filed as
  separate abstention/NULL-calibration baseline (reference-only). §3 definition updated to match.
**Team Lead provisional acceptance covers:**
  (1) always_return_ct reference-only in all constructions
  (2) rank-index C dummies ceiling-bearing
  (3) always_return_query_role_object ceiling-bearing
  (4) always_return_query_role_object covers endpoint-bias-under-negative-graph
  (5) always_return_NULL reference-only, abstention/NULL-calibration baseline
**Required caveat (must remain explicit in all future filings):**
  Gate 5 does not close target-token anchoring as a composite shortcut.
  Tracked via §8 axis diagnostics, especially hop1 failures returning ct.

---

## Purpose

This document responds to the three definition questions raised in Team Lead review of R1 and Contributor 5 feedback. It provides CS Engineer's position on each question and a revised final dummy list for Team Lead / Senior confirmation.

---

## 1. always_return_ct Ceiling Status for Cell03

**CS position: always_return_ct remains reference-only under Cell03.**

**Contributor 5's concern:** Under Cell03 balanced construction, ct no longer coincides with one fixed rank dummy. No ceiling-bearing dummy consistently tests target-token anchoring. `always_return_ct` may be the only such test.

**Resolution:**

```text
Gate 5 is designed to detect shortcuts that produce CORRECT answers.

always_return_ct on composite scores n/n by construction.
The correct answer for composite IS ct — this is a structural property, not a shortcut.
Making always_return_ct ceiling-bearing would require Gate 5 to fail every correctly
constructed cell on composite. That is not the intended function of Gate 5.

Target-token anchoring (ct-anchoring) manifests as hop1 FAILURES:
  The model returns ct when bt is the expected answer.
  This produces WRONG answers on hop1, not correct ones.
  It is detectable via hop1 failure analysis (§8 Axis diagnostics), not via Gate 5 ceiling.

Gate 5 and the §8 failure breakdown are complementary diagnostics:
  Gate 5:   detects shortcuts that explain correct scores.
  §8:       detects recurring failure patterns (including ct-anchoring on hop1).
```

**Redundancy rule from R1: revised and narrowed.**

The construction-conditional framing raised in Q1 would be:

```text
always_return_ct reference-only when redundant with a ceiling-bearing rank dummy.
always_return_ct ceiling-bearing when balanced rank makes it non-redundant.
```

This rule is rejected. Making always_return_ct ceiling-bearing under balanced construction would produce trivial Gate 5 FAIL for every cell where the composite answer is ct — which is all correctly constructed Two-Hop L1 cells. The Gate 5 ceiling would be violated not by a shortcut but by the definition of the correct answer.

**Correct rule:**

```text
always_return_ct: reference-only in all constructions.

Rationale:
  It cannot be a Gate 5 ceiling-bearing dummy because its composite n/n score
  is expected by construction and is not evidence of a shortcut.

  Target-token anchoring is a failure-mode diagnostic, not a Gate 5 ceiling signal.
  It belongs in §8 failure-class breakdown and behavioral observation.

Explicit coverage gap:
  Cell03 Gate 5 does NOT cover target-token anchoring as a shortcut for composite.
  The ct-anchoring diagnostic is handled by hop1 failure analysis (§8), where
  a model exploiting target-token identity would return ct when bt is expected.
  This gap is acknowledged, documented, and does not affect Gate 5 PASS/FAIL.
```

**Impact on R1:** The construction-conditional framing is withdrawn. `always_return_ct` is reference-only in all constructions. R1 §1 is superseded by this section.

---

## 2. negative_graph Behavior for the Role/Attraction Dummy

**CS position: Family A only (NULL on negative_graph). Family B deferred. Gap documented.**

The two families raised in Q2:

```text
Family A — Correct-abstention / role-match control:
  Returns NULL on negative_graph.
  Behavior: follows the context — hop2 removed, no matching fact, no return token.

Family B — Endpoint-attraction control:
  Returns an endpoint-shaped token on negative_graph.
  Intent: tests whether a model is biased toward returning an endpoint even under
  abstention conditions (when the correct answer is NULL).
```

**Cell03 scope: Family B for always_return_query_role_object; Family A as separate baseline.**

*(Amended per Team Lead direction 2026-06-08. Original R2 recommended Family A only — reversed.)*

```text
always_return_query_role_object is the Gate 5 endpoint-attraction dummy.
It returns an endpoint token on negative_graph and scores 0/n.

Rationale:
  The dummy tests answer-domain / relation-role salience: does the model return
  an endpoint-shaped token because it matches the expected role, regardless of
  whether the chain is valid?
  On negative_graph, the chain is broken (hop2 removed). If a model is attracted
  to the endpoint, it will return ct even when the correct answer is NULL.
  The dummy should model this behavior — return ct, score 0 — not collapse to NULL.
  A dummy that returns NULL on negative_graph is a correct-abstention baseline,
  not an endpoint-attraction test.

NULL-returning behavior:
  Filed as a separate abstention / NULL-calibration baseline (always_return_NULL).
  Reference-only. See §4.
  It is NOT the Gate 5 endpoint-attraction dummy.
```

---

## 3. Final Dummy Name

**CS position: Option B — `always_return_query_role_object`.**

Contributor 5's concern: "most_recent" encodes a recency hypothesis that has not been isolated from answer-domain salience. A model returning ct because it is the most recently seen "maps to" fact could be exhibiting recency bias, not answer-domain salience.

```text
Under current Two-Hop L1 construction:
  There is exactly ONE "maps to" fact with the query anchor as subject per item.
  There is exactly ONE "links to" fact for the target chain per item.
  "Most recently seen" and "the unique role-matching fact" are the same object.
  The names produce identical behavior on current items.

The distinction matters for:
  (a) Interpretive cleanliness: recency bias and role/answer salience are different cues.
      The dummy name should not presuppose which one is operating.
  (b) Future extensibility: when a construction has multiple competing "maps to" facts,
      the selection rule must be specified explicitly — not assumed from the name.
```

**Rejected name:** `always_return_most_recent_role_match`
Reason: encodes recency as the selection principle without evidence that recency is the relevant cue. If a future construction shows the dummy is sensitive to fact order, the name would retroactively suggest recency was always the mechanism.

**Adopted name:** `always_return_query_role_object`

```text
always_return_query_role_object

Definition:
  Returns the object of the fact in the context whose:
    (a) relation type matches the query's expected relation type, AND
    (b) subject matches the query anchor (where applicable)
  On negative_graph, where the hop2 fact is removed and no matching context fact
  exists, returns the absent endpoint from item metadata.

  hop1 expected relation: "links to" → returns bt
    (object of the "links to" fact for the target chain)

  hop2 expected relation: "maps to" → returns ct
    (object of the "maps to" fact for the target chain anchor)

  composite: same as hop2 → returns ct

  negative_graph: hop2 fact removed; no context-matching "maps to" fact for anchor.
    → returns item["chain"]["c_target"] (ct — the absent endpoint)
    → scores 0/n (expected NULL; endpoint token is wrong)
    → tests endpoint-attraction under abstention conditions

Selection rule for multiple candidates (future constructions):
  Unspecified at this time. Must be documented when a construction with
  multiple competing facts of the same relation type is designed.
  Do not default to recency without explicit authorization.

Under current Two-Hop L1 construction:
  One matching fact per query type per item (for hop1/hop2/composite). Unambiguous.
  Numerically:
    hop1:           ≡ always_return_B_target
    hop2/composite: ≡ always_return_ct
    negative_graph: ≡ always_return_ct (returns ct; scores 0 — NOT always_return_NULL)
```

---

## 4. Final Ceiling-Bearing vs Reference-Only Dummy List

### Ceiling-bearing (subject to max_det ≤ 9/24)

```text
always_return_first_C
  Returns c_by_pos[0]. Existing. Tests rank-1 position bias.

always_return_second_C
  Returns c_by_pos[1]. NEW. Tests rank-2 position bias.
  In Cell02: equivalent to always_return_ct. Gate 5 coverage gap identified.
  In Cell03: non-equivalent (ct balanced across ranks).

always_return_third_C
  Returns c_by_pos[2]. NEW. Guarded: only if len(c_by_pos) >= 3.
  Tests rank-3 position bias. Cell03 has 3 C-endpoints: required.
  Equivalent to always_return_last_C for Cell03 (3 endpoints). Both reported.

always_return_last_C
  Returns c_by_pos[-1]. Existing. Tests last-position bias.

always_return_query_role_object
  Returns object of fact matching query's expected relation type and anchor.
  NEW. Tests answer-domain / relation-role salience including endpoint-attraction
  under abstention.
  Ceiling-bearing. Subject to max_det ceiling.
  On negative_graph: returns ct (item["chain"]["c_target"]); scores 0/n.
    (Amended from R2 original — see amendment note in header.)
```

### Reference-only (NOT in max_det ceiling calculation)

```text
always_return_ct
  Returns item["chain"]["c_target"] for all query types.
  Expected scores: hop1 = 0/n, hop2 = n/n, composite = n/n, neg_graph = 0/n.
  Reference-only in all constructions (not construction-conditional).

  Function: documents target-rank / target-token upper-bound.
  Gate 5 role: reported as reference row; excluded from max_det ceiling.
  Cannot rescue Gate 5 failure owned by equivalent ceiling-bearing rank dummies.
  Cannot be made ceiling-bearing without trivially failing Gate 5 for all
  correctly constructed cells on composite.

  Target-token anchoring diagnostic: handled by hop1 failure analysis (§8),
  not by Gate 5 ceiling.

always_return_NULL
  Returns NULL for all query types.
  Expected scores: hop1 = 0/n, hop2 = 0/n, composite = 0/n, neg_graph = n/n.
  Reference-only. Abstention / NULL-calibration baseline.

  Function: documents the "always abstain" upper bound for negative_graph.
    Parallel to always_return_ct for composite — trivially correct on one query type
    by construction; not a shortcut signal.
  Gate 5 role: reported as reference row; excluded from max_det ceiling.
  This is the NULL-returning behavior separated from always_return_query_role_object.
  It is NOT the endpoint-attraction dummy.
```

### Documented Gate 5 gaps for Cell03

```text
Gap 1 — Target-token anchoring:
  Not covered by Gate 5. Diagnosed via hop1 failure breakdown (§8).
  Acknowledged; does not affect Gate 5 PASS/FAIL.

Gap 2 — Endpoint-bias-under-negative-graph:
  CLOSED. always_return_query_role_object returns ct on negative_graph and scores 0/n.
  This dummy covers endpoint-attraction under abstention as a ceiling-bearing Gate 5 control.
```

---

## 5. Whether R1 Requires Revision Before Manager Scorer-Amendment Authorization

**Yes. R1 requires revision on the following points before Manager routing:**

```text
Point 1 — always_return_ct construction-conditional framing (R1 §1):
  R1 did not include the construction-conditional proposal (that was Q1 in the Team Lead memo).
  R1 §1 is superseded by §1 of this document:
    - Construction-conditional framing rejected.
    - Reference-only in all constructions confirmed.
    - Explicit documentation of Gate 5 gap required.

Point 2 — always_return_answer_shaped naming (R1 §5):
  R1 §5 proposed always_return_most_recent_role_match.
  This document supersedes that with always_return_query_role_object.

Point 3 — negative_graph behavior (R1 §4, further amended):
  R1 §4 stated "Family B deferred" — reversed by Team Lead direction.
  This document (as amended): always_return_query_role_object returns ct on neg_graph
  (Family B, endpoint-attraction); always_return_NULL is a separate reference-only baseline.
  Gap 2 (endpoint-bias-under-negative-graph) is now CLOSED.

Point 4 — Final dummy list (R1 §6):
  Superseded by §4 of this document (new name, gap statements added).
```

**R1 sections that remain in force:**
- R1 §2 (Gate 5 handling when always_return_second_C == ct): unchanged.
- R1 §3 (query-type table): updated for new name only; logic unchanged.

**Scorer amendment authorization path:**

```text
[PENDING] Team Lead / Senior confirmation of this document (R2):
  (a) always_return_ct: reference-only in all constructions (§1)
  (b) always_return_query_role_object: Family B, negative_graph = ct (endpoint token), scores 0 (§2–§3)
  (c) Naming: always_return_query_role_object adopted (§3)
  (d) Final ceiling-bearing vs reference-only list (§4)
  (e) Two documented Gate 5 gaps (§4)

[NOT YET STARTED] Manager authorization for scorer amendment
  Blocked on Team Lead / Senior confirmation.
```

Cell03 construction remains blocked. No model inference is authorized.

---

**Response R2 filed. Awaiting Team Lead / Senior confirmation of §1–§5 before scorer amendment is routed to Manager.**

— CS Engineer, 2026-06-08
