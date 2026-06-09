# Cell03 Dummy Policy Response — Revision 3 (Brainstorm)

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Requested by:** Team Lead memo — "Critical Design Problem — Endpoint-Attraction Dummy Definition Before Cell03 Scorer Amendment" 2026-06-08
**Supersedes:** CELL03-DUMMY-POLICY-RESPONSE-R2.md §2–§4 (always_return_query_role_object as ceiling-bearing)
**Status:** FILED — brainstorm response; awaiting Team Lead / Senior disposition before scorer amendment

---

## Purpose

This document responds to the five brainstorm questions (A–E) in the Team Lead memo and provides the 8-point structured response. The central conclusion is that `always_return_query_role_object` cannot be a ceiling-bearing Gate 5 dummy and should be retired. The reasoning is developed below.

---

## Core Diagnosis

Gate 5 detects shortcuts that produce **high correct scores**. The question for any proposed dummy is: under what conditions does this dummy score above the Gate 5 ceiling (9/24)?

For any dummy that returns `ct` across query types:

```text
query_type      expected answer     dummy return    score
hop1            bt                  ct              0/n     (ct ≠ bt by construction)
hop2            ct                  ct              n/n     (trivially correct by construction)
composite       ct                  ct              n/n     (trivially correct by construction)
negative_graph  NULL                ct              0/n     (ct ≠ NULL)
```

The rows that score HIGH (n/n) are hop2 and composite — but these are trivially correct because `ct` IS the correct answer. There is no shortcut being detected: this is the definition of the correct answer. These rows are reference-only by construction.

The rows that score LOW (0/n) are hop1 and negative_graph — the dummy is wrong here. A Gate 5 ceiling check on these rows is vacuous: 0/n < 9/24 always passes, regardless of what the dummy does.

**Conclusion: there is no query type where a ct-returning dummy produces a high correct score that is not already trivially expected by construction. The ct-anchoring signal is a failure mode (§8), not a Gate 5 shortcut.**

---

## Question A — What Should This Dummy Model?

The Cell02 observation was:

```text
hop1 expected bt
model returned ct  (11/15 hop1 failures)
```

This is a **failure-mode signal**. The model scores LOW on hop1 by returning the wrong answer. Gate 5 is designed to catch shortcuts that score HIGH. The ct-anchoring pattern produces low-correct behavior on hop1, which is the opposite of what Gate 5 is built to catch.

What `always_return_query_role_object` was intended to model — answer-domain salience / relation-role matching — is equivalent to:

```text
hop1:           returns bt (correct hop1 answer — not a shortcut, that IS the answer)
hop2/composite: returns ct (correct hop2/composite answer — trivially correct)
negative_graph: returns ct (wrong — scores 0)
```

There is no combination of query-type returns that:
1. Returns `ct` where `ct` is not the expected answer AND
2. Scores HIGH enough to be a Gate 5 ceiling concern

because whenever `ct` is wrong, the dummy scores 0/n (below ceiling), and whenever `ct` is right, it is trivially correct.

**The concept of a ceiling-bearing Gate 5 endpoint-attraction dummy for ct is structurally incoherent under Two-Hop L1 construction.**

The ct-anchoring failure mode (hop1 returning ct when bt expected) is a §8 axis diagnostic, not a Gate 5 ceiling concern. It cannot be made into a Gate 5 control without either:
- Trivially failing Gate 5 on positive query types (ceiling-bearing + n/n = fail), or
- Scoring 0/n on all interesting rows (below ceiling = vacuous Gate 5 control)

---

## Question B — Query-Type Return Table

The only coherent table for a ct-returning dummy is:

```text
query_type      expected answer     dummy return    dummy score     ceiling status
hop1            bt                  ct              0/n             reference-only
                                                                    (0/n < ceiling; vacuous as ceiling check)
hop2            ct                  ct              n/n             reference-only
                                                                    (trivially correct by construction)
composite       ct                  ct              n/n             reference-only
                                                                    (trivially correct by construction)
negative_graph  NULL                ct              0/n             reference-only
                                                                    (0/n < ceiling; vacuous as ceiling check)
```

This is `always_return_ct`. No new dummy is needed.

There is no table variant where any row is usefully ceiling-bearing:
- Any row where ct is correct scores n/n → reference-only required
- Any row where ct is wrong scores 0/n → trivially below ceiling, adds no Gate 5 signal

---

## Question C — One Dummy or Multiple?

**Recommended: two reference-only diagnostics; no new ceiling-bearing endpoint-attraction dummy.**

```text
always_return_ct (reference-only):
  Returns item["chain"]["c_target"] for all query types.
  Covers: target-token upper bound (hop2/composite), ct-intrusion reference (hop1),
  endpoint-under-abstention reference (negative_graph).
  Already established in policy.

always_return_NULL (reference-only):
  Returns NULL for all query types.
  Covers: abstention upper bound (negative_graph n/n by construction).
  Already established in policy.
```

These two reference diagnostics, combined with the rank-based ceiling dummies, provide full coverage of the diagnostic space. No new dummy is required.

Splitting into additional named dummies (e.g., `always_return_intruding_ct` for hop1/negative_graph rows only) would create a dummy that scores 0/n on its designated ceiling-bearing rows — a vacuous Gate 5 control that adds no information.

---

## Question D — Should Positive Composite Be Ceiling-Bearing for This Dummy?

No. If a dummy returns `ct` on composite, it returns the correct answer by construction. Composite correct answer = ct for all items. The dummy scores n/n on composite not because of a shortcut but because it is constructed to always return the right token. Making this ceiling-bearing would fail Gate 5 for every correctly constructed cell.

The policy already established (R2) that `always_return_ct` is reference-only for this reason. That reasoning applies to any ct-returning dummy.

---

## Question E — Naming

`always_return_query_role_object` should be retired. The correct entity it was approximating is `always_return_ct` (reference-only), which already exists in the policy.

If future constructions require a genuine role-object dummy (where the role-matching answer is not trivially the same as the correct answer), the name `always_return_query_role_object` could be revisited at that time with a properly specified query-type table.

For Cell03, no new name is needed. The dummy family is: rank dummies (ceiling-bearing) + `always_return_ct` (reference) + `always_return_NULL` (reference).

---

## 8-Point Structured Response

```text
1. Recommended dummy architecture:

   Ceiling-bearing (Gate 5 controls):
     always_return_first_C      — rank-1 C by context position
     always_return_second_C     — rank-2 C by context position
     always_return_third_C      — rank-3 C by context position (guarded: 3+ endpoints)
     always_return_last_C       — rank-last C by context position

   Reference-only (Gate 5 reference rows, excluded from max_det ceiling):
     always_return_ct           — target-token upper bound; covers hop1 ct-intrusion,
                                  hop2/composite trivial-correct, neg_graph endpoint-attraction
     always_return_NULL         — abstention upper bound; covers neg_graph trivial-NULL,
                                  hop1/hop2/composite always-wrong-by-refusing

   RETIRED: always_return_query_role_object
     Cannot be ceiling-bearing without trivially failing Gate 5 on positive queries.
     Its diagnostic value is fully covered by always_return_ct (reference-only).

2. Query-type return table (for always_return_ct, reference-only):

   query_type      expected     return    score    ceiling status
   hop1            bt           ct        0/n      reference-only
   hop2            ct           ct        n/n      reference-only (trivially correct)
   composite       ct           ct        n/n      reference-only (trivially correct)
   negative_graph  NULL         ct        0/n      reference-only

3. Which rows are ceiling-bearing:
   Rank-based dummies (first_C, second_C, third_C, last_C): all query types, ceiling-bearing.
   No ct-returning dummy rows are ceiling-bearing.

4. Which rows are reference-only:
   always_return_ct: all rows (hop1/hop2/composite/negative_graph).
   always_return_NULL: all rows.

5. What shortcut / failure mode it models:
   Rank dummies: test whether a rank-position rule for C-endpoints achieves high composite
     accuracy. This is the correct Gate 5 control for ranked-C constructions.
   always_return_ct: documents the target-token upper bound. On hop1 it documents that a
     ct-anchored model would score 0/n (failure mode, not shortcut). On hop2/composite it
     documents the n/n ceiling that a perfect-token oracle achieves (trivially correct by
     construction). On negative_graph it documents endpoint-under-abstention behavior (0/n).
   always_return_NULL: documents the always-abstain upper bound for negative_graph.

6. What it does NOT test (Gate 5):
   Gate 5 does not test ct-anchoring as a composite shortcut. [STANDING CAVEAT]
   Gate 5 does not detect that a model consistently returns ct on hop1 (failure mode) — this
   produces 0/n, below ceiling, invisible to Gate 5. This is a §8 failure-breakdown diagnostic.
   Gate 5 does not test answer-domain salience independently of rank position (the two are
   confounded in current construction and cannot be separated by a single Gate 5 dummy).

7. Recommended dummy name:
   No new ceiling-bearing dummy name required for Cell03.
   always_return_ct (reference-only) covers the target-token diagnostic space.
   always_return_query_role_object: RETIRED for Cell03.
   If a genuine role-object dummy becomes relevant in a future construction where the
   role-matching answer is not trivially ct, the name may be revisited at that time.

8. Whether R2 requires R3 before Manager scorer-amendment authorization:
   YES. R2 provisionally accepted always_return_query_role_object as ceiling-bearing.
   That classification is incoherent: it trivially fails Gate 5 on positive queries by
   construction. R3 (this document) retires that dummy from the ceiling-bearing set.
   The scorer amendment plan must be revised accordingly before Manager authorization.
```

---

## Revised Scorer Amendment Scope (for reference)

Under this architecture, the scorer amendment adds:

```text
Ceiling-bearing dummies (new):
  always_return_second_C         — returns c_by_pos[1]
  always_return_third_C          — returns c_by_pos[2] (guarded: len(c_by_pos) >= 3)

Reference-only rows (new):
  always_return_ct               — returns item["chain"]["c_target"]
  always_return_NULL             — returns None

Existing (unchanged):
  always_return_first_C          — returns c_by_pos[0]
  always_return_last_C           — returns c_by_pos[-1]

NOT included:
  always_return_query_role_object — retired
  always_return_most_recent_role_match — previously retired name; remains retired
  always_return_answer_shaped     — previously retired name; remains retired
```

Unit tests required: second_C, third_C (+ guard case), always_return_ct, always_return_NULL, regression on all 14 existing tests. Minimum 5 new tests.

Gate 5 ceiling check:
```text
Ceiling-bearing rows: first_C, second_C, third_C, last_C — all query types
Reference rows:       always_return_ct, always_return_NULL — reported, excluded from max_det
```

---

## Standing Caveat (Required in All Future Filings)

```text
Gate 5 does not close target-token anchoring as a composite shortcut.
The ct-anchoring failure mode (model returns ct on hop1 when bt is expected) produces
0/n on hop1 — below Gate 5 ceiling — and is diagnosed via §8 hop1 failure breakdown.
This gap is acknowledged and does not affect Gate 5 PASS/FAIL.
```

---

**R3 filed. Recommends retiring always_return_query_role_object from ceiling-bearing set. Awaiting Team Lead / Senior disposition before scorer amendment is revised and routed to Manager.**

— CS Engineer, 2026-06-08
