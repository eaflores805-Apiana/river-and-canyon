# Cell03 Dummy Policy Clarification — Revision 1

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Requested by:** Team Lead memo — "Cell03 Dummy Policy Confirmation Received — Definitions Require Review Before Scorer Amendment" 2026-06-08
**Supersedes:** CELL03-DUMMY-POLICY-CONFIRMATION.md §2 (always_return_ct policy), §3 (always_return_answer_shaped definition and name), §5 final dummy list
**Status:** PARTIALLY SUPERSEDED — see CELL03-DUMMY-POLICY-RESPONSE-R2.md
  Superseded sections: §1 (always_return_ct ceiling status), §4 (negative_graph policy), §5 (dummy name), §6 (final list)
  §2 (Gate 5 when second_C == ct), §3 (query-type table logic): remain in force

---

## Purpose

This document addresses the five clarification points raised by Team Lead review of CELL03-DUMMY-POLICY-CONFIRMATION.md. It revises the affected policy sections and provides the concrete examples and distinctions required before scorer amendment can be routed to Manager.

---

## 1. always_return_ct — Revised Policy: Reference-Only, NOT Pass-Enabling

**Team Lead's distinction accepted:**

```text
Rank-index C dummies (first_C, second_C, third_C, last_C) = ceiling-bearing Gate 5 controls
always_return_ct = reference diagnostic only
```

**Revised policy:**

```text
always_return_ct is included in the Gate 5 table as a reference row.
It is NOT included in the max_det ceiling calculation.
It is NOT a pass-enabling exclusion.

Reference-only means:
  - The dummy is scored and reported.
  - Its score does not affect Gate 5 PASS/FAIL determination.
  - It provides a target-rank / target-token upper-bound anchor.

Reference-only does NOT mean:
  - A cell is protected from Gate 5 failure because always_return_ct is excluded.
  - An equivalent ceiling-bearing dummy may exceed the ceiling without consequence.
```

**Rationale:**

`always_return_ct` scores n/n on hop2 and composite by construction — the correct answer IS ct for those query types. This is a structural property, not a shortcut. Excluding it from the ceiling recognizes that n/n composite is expected for a dummy that by definition returns the correct answer.

The shortcut question is: *can a model return ct without reasoning through the chain?* That question is answered by rank-based dummies. If a rank-based dummy (e.g., `always_return_second_C`) is equivalent to `always_return_ct` for a given construction, it is ceiling-bearing and its ceiling failure stands.

`always_return_ct` documents what the oracle knows. The rank dummies document what a position/rank shortcut can achieve. These are different questions.

---

## 2. Gate 5 Handling When always_return_second_C == ct

Under Cell02:

```text
ct was always second_C. For all 24 items:
  always_return_second_C(item, query_type) == always_return_ct(item, query_type)

If always_return_second_C had been scored:
  composite: 24/24   (because ct == second_C for all items, and composite answer is ct)
  24/24 > 9/24 ceiling → Gate 5 FAIL for composite.

This is why Cell02 Gate 5 was filed as PASS* (coverage gap):
  The gap WOULD HAVE been a ceiling failure.
  always_return_ct reference-only classification has no bearing on this.
  The ceiling failure is owned by always_return_second_C (ceiling-bearing).
```

**Policy (confirmed):**

```text
If always_return_second_C == always_return_ct for all items in a construction:
  always_return_second_C is ceiling-bearing.
  It must be tested.
  If it exceeds 9/24, Gate 5 FAILS for that shortcut.
  The always_return_ct reference row does not rescue that failure.

"Reference-only" for always_return_ct applies only to always_return_ct's own score row.
It does not modify the ceiling rule for equivalent rank dummies.
```

Under Cell03 (balanced ct position / C-rank):

```text
ct will NOT always be second_C.
always_return_second_C ≠ always_return_ct for items where ct is first_C or third_C/last_C.

always_return_second_C will correctly score those items where ct happens to be second_C.
always_return_ct will still score n/n on composite (ct is always the correct composite answer).

These are now distinct diagnostics:
  always_return_second_C: tests rank-2 position bias; ceiling-bearing.
  always_return_ct: tests target-token oracle; reference-only.

Gate 5 ceiling applies to always_return_second_C (and all rank dummies).
Gate 5 failure via any rank dummy stands regardless of always_return_ct reference row.
```

---

## 3. Query-Type Table for always_return_most_recent_role_match

*(See §4 below for the naming revision.)*

The dummy returns the object of the most recently seen fact (by ascending context `position_index`) whose relation role matches the query's expected relation type.

```text
query_type      expected         dummy return rule                            return under
                relation type                                                 current construction
─────────────────────────────────────────────────────────────────────────────────────────────────
hop1            "links to"       object of the last "links to" fact           bt
                                 in context (by ascending position_index)     (same as always_return_B_target)

hop2            "maps to"        object of the last "maps to" fact            ct
                                 whose SUBJECT matches the query anchor       (same as always_return_ct)
                                 (by ascending position_index)

composite       "maps to"        same as hop2 lookup                          ct
                                 (same anchor resolution rule)                (same as always_return_ct)

negative_graph  (no link         no "maps to" fact with the query anchor      NULL
                expected)        as subject remains in context —              (same as always_return_NULL)
                                 hop2 fact is removed; lookup returns NULL
```

**Numerical equivalence under current construction:**

```text
hop1:           ≡ always_return_B_target
hop2:           ≡ always_return_ct
composite:      ≡ always_return_ct
negative_graph: ≡ always_return_NULL
```

The dummy is numerically redundant under the current construction but is included to formally close the answer-domain salience hypothesis and to lock the definition before construction changes make it non-redundant.

---

## 4. negative_graph Behavior — Explicit Policy

The Team Lead correctly identifies that two distinct behaviors are possible:

```text
(a) Return NULL when no link exists.
    → Collapses to always_return_NULL for negative_graph.
    → Tests whether the dummy correctly refuses the query.

(b) Return an endpoint-shaped token despite NULL expected.
    → Tests endpoint bias under abstention conditions.
    → A model-diagnostic question: does the model return ct
      even when the hop2 fact is absent from the context?
```

**Policy for always_return_most_recent_role_match:**

```text
This dummy implements behavior (a).
For negative_graph, no matching "maps to" fact exists (hop2 removed).
The dummy returns NULL.
always_return_most_recent_role_match ≡ always_return_NULL for negative_graph.
```

These are NOT collapsed — behavior (b) is explicitly excluded.

If endpoint bias under abstention needs to be tested, that requires a separate dummy:

```text
Proposed name (if authorized later):
  always_return_ct_regardless_of_graph

Behavior:
  Returns ct for ALL query types including negative_graph.
  Scores: hop1 = 0/n, hop2 = n/n, composite = n/n, negative_graph = 0/n.

Status: NOT proposed for Cell03. Separate authorization required if needed.
```

The two dummies address different hypotheses and must not be combined or confused.

---

## 5. Naming Revision

**Retired name:** `always_return_answer_shaped`

**Reason:** The name implies a vague semantic category ("answer-shaped"). The dummy is not defined by semantic appearance but by a precise rule: most recently seen fact matching query's expected relation role.

**Proposed name:** `always_return_most_recent_role_match`

```text
always_return_most_recent_role_match

Meaning:
  Returns the object of the most recently seen fact (by ascending position_index)
  whose relation role matches the query's expected relation type.

  hop1:           last "links to" object → bt
  hop2:           last "maps to" object (matching anchor) → ct
  composite:      same as hop2 → ct
  negative_graph: no matching "maps to" fact → NULL
```

Alternative short form: `always_return_role_match` — acceptable only if the implementation comment specifies "most recently seen by position_index."

**Proposed final name: `always_return_most_recent_role_match`** — pending Team Lead / Senior confirmation.

---

## 6. Final Dummy List — Ceiling-Bearing vs Reference-Only

**Ceiling-bearing (subject to max_det ≤ 9/24):**

```text
always_return_first_C
  Returns c_by_pos[0]. Existing. Tests rank-1 position bias.

always_return_second_C
  Returns c_by_pos[1]. NEW. Tests rank-2 position bias.
  Critical: equivalent to always_return_ct under Cell02 fixed-rank construction.

always_return_third_C
  Returns c_by_pos[2]. NEW (guarded: only if len(c_by_pos) >= 3).
  Tests rank-3 position bias. Cell03 has 3 C-endpoints — required.

always_return_last_C
  Returns c_by_pos[-1]. Existing. Tests last-position bias.
  For Cell03 (3 endpoints): last_C == third_C. Both rows reported explicitly.

always_return_most_recent_role_match
  Returns object of last fact matching query's expected relation role.
  NEW (pending name confirmation). Tests answer-domain / relation-role salience.
  Ceiling-bearing. Subject to max_det ceiling.
```

**Reference-only (NOT in max_det ceiling calculation):**

```text
always_return_ct
  Returns item["chain"]["c_target"] for all query types.
  Scores n/n on hop2 / composite by construction. Reference row only.
  Documents: target-rank / target-token exposure upper bound.
  Cannot rescue Gate 5 failure owned by ceiling-bearing rank dummies.
  If always_return_second_C == always_return_ct for all items and exceeds ceiling:
    Gate 5 FAILS. always_return_ct reference classification has no effect.
```

---

## 7. Scorer Amendment Readiness

This revision is complete and supersedes CELL03-DUMMY-POLICY-CONFIRMATION.md on the above points.

The scorer amendment remains blocked on:

```text
[PENDING] Team Lead / Senior confirmation of:
  (a) always_return_ct reference-only policy and ceiling-non-rescue constraint (§1–§2 above)
  (b) always_return_most_recent_role_match query-type table (§3 above)
  (c) negative_graph behavior: NULL, not endpoint token (§4 above)
  (d) naming: always_return_most_recent_role_match (§5 above)
  (e) final ceiling-bearing vs reference-only classification (§6 above)

[NOT YET STARTED] Manager authorization for scorer amendment
  Blocked on Team Lead / Senior confirmation.
```

Cell03 construction remains blocked. No model inference is authorized.

---

**Clarification filed. Awaiting Team Lead / Senior confirmation of §1–§6 before scorer amendment is routed to Manager.**

— CS Engineer, 2026-06-08
