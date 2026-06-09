# Cell03 Scorer — Tautology Guard Fixture Verification

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**In response to:** Team Lead memo — "Re-lock Disposition and Gate 3 Recommendation — Accepted with Guardrail" §2, 2026-06-08
**Status:** FILED for Senior verification — open item from scorer re-lock disposition

---

## Purpose

Senior flagged one open verification item before Cell03 relies on the tautology guard:

```text
The tautology guard must be verified against the actual _TEST_ITEM_DUMMIES fixture
and T_new_2 assertion. A 20/20 pass count does not prove the guard is meaningful.
The guard is only meaningful if the fixture tests ct across ranks or otherwise proves
rank-dummy non-oracle behavior.
```

This document provides the fixture excerpts, the T_new_2 assertion, and the rank mapping
that demonstrates the guard is not vacuous.

---

## 1. Fixture Excerpts

The amendment adds two balanced fixtures: **Fixture_A** (ct at rank 2) and **Fixture_B**
(ct at rank 1). Both use the same target chain tokens (`ct = CPQVX`, `bt = BMNIX`).

### Fixture_A — ct at rank 2

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
```

C-object rank derivation (via `_c_objects_by_context_position()`):

```text
Fact at pos 2 → chain_id "decoy_1" → C_object "FVPLX"  → rank 1 (first_C)
Fact at pos 6 → chain_id "target"  → C_object "CPQVX"  → rank 2 (second_C = ct)
Fact at pos 7 → chain_id "decoy_2" → C_object "IMNCX"  → rank 3 (third_C = last_C)

c_by_pos = ["FVPLX", "CPQVX", "IMNCX"]
ct = CPQVX = c_by_pos[1] = second_C   ← ct is at rank 2
```

### Fixture_B — ct at rank 1

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
```

C-object rank derivation:

```text
Fact at pos 2 → chain_id "target"  → C_object "CPQVX"  → rank 1 (first_C = ct)
Fact at pos 5 → chain_id "decoy_1" → C_object "FVPLX"  → rank 2 (second_C)
Fact at pos 7 → chain_id "decoy_2" → C_object "IMNCX"  → rank 3 (third_C = last_C)

c_by_pos = ["CPQVX", "FVPLX", "IMNCX"]
ct = CPQVX = c_by_pos[0] = first_C    ← ct is at rank 1 (different from Fixture_A)
```

---

## 2. T_new_2 Assertion

T_new_2 is the tautology guard. It uses Fixture_B (ct at rank 1):

```python
(_TEST_ITEM_DUMMY_B, QT_COMPOSITE, "always_return_second_C", 0.0,
 "T_new_2: second_C tautology guard — ct at rank 1, second_C scores 0"),
```

Execution trace:

```text
Item:            _TEST_ITEM_DUMMY_B
Query type:      composite
Expected answer: CPQVX  (ct, target chain C_object)

c_by_pos:        ["CPQVX"(pos2), "FVPLX"(pos5), "IMNCX"(pos7)]
always_return_second_C → c_by_pos[1] = "FVPLX"

score("FVPLX") = 1.0 if "FVPLX" == "CPQVX" else 0.0
             = 0.0   ← FVPLX ≠ CPQVX

T_new_2 assertion: expected 0.0, actual 0.0 → PASS
```

---

## 3. Tautology Guard Analysis

**The tautology guard is meaningful. The fixture set tests ct at two different ranks.**

Rank mapping summary:

```text
Fixture       ct token   ct rank   second_C   score(second_C, composite)
---------     --------   -------   --------   --------------------------
Fixture_A     CPQVX      rank 2    CPQVX      1.0   (second_C == ct == expected answer)
Fixture_B     CPQVX      rank 1    FVPLX      0.0   (second_C != ct; second_C = cd1)
```

The guard is non-vacuous because:

1. **ct is the same token in both fixtures** (CPQVX). The difference is structural —
   the context ordering places the target hop2 fact earlier (pos 2) in Fixture_B and
   later (pos 6) in Fixture_A. This changes ct's rank without changing ct's identity.

2. **T_new_1 + T_new_2 together prove rank-sensitivity**: T_new_1 confirms `second_C`
   returns 1.0 when ct is at rank 2. T_new_2 confirms `second_C` returns 0.0 when
   ct is at rank 1. If the scorer implementation had `second_C` hardcoded to return
   ct rather than `c_by_pos[1]`, T_new_2 would fail (it would return 1.0 not 0.0).

3. **The guard specifically tests the condition Senior named**: "the fixture tests ct
   across ranks." Fixture_A places ct at rank 2; Fixture_B places ct at rank 1.
   Both pass their respective expected scores. The guard is not vacuous.

**What the guard does NOT test**: ct at rank 3. For Cell03 completeness, third_C tautology
behavior is covered by T_new_3 (which uses Fixture_A where third_C = IMNCX ≠ ct, scores 0.0)
and by construction: if ct were at rank 3 in a future fixture, `always_return_third_C` would
score 1.0 and `always_return_second_C` would score 0.0 — symmetrically correct behavior.

No additional fixture is required for rank-3 coverage. T_new_3 covers the third_C
functionality case, and T_new_4 covers the guard condition (len < 3).

---

## 4. Full T_new_1 through T_new_6 Assertion Summary

For Senior reference:

```text
T_new_1  _TEST_ITEM_DUMMY_A  composite  always_return_second_C  expected=1.0
           c_by_pos[1] = CPQVX = ct = expected → 1.0
           [functionality test: second_C correctly identifies rank-2 object when ct is rank 2]

T_new_2  _TEST_ITEM_DUMMY_B  composite  always_return_second_C  expected=0.0
           c_by_pos[1] = FVPLX ≠ ct → 0.0
           [TAUTOLOGY GUARD: second_C scores 0 when ct is not at rank 2]

T_new_3  _TEST_ITEM_DUMMY_A  composite  always_return_third_C   expected=0.0
           c_by_pos[2] = IMNCX ≠ CPQVX → 0.0
           [functionality test: third_C correctly identifies rank-3 object when ct is rank 2]

T_new_4  _TEST_ITEM          composite  always_return_third_C   expected=0.0
           c_by_pos = [] → len < 3 → guarded fallback → 0.0
           [guard test: no IndexError on empty c_by_pos]

T_new_5  _TEST_ITEM_DUMMY_A  hop1       always_return_ct        expected=0.0
           ct = CPQVX ≠ BMNIX = expected_hop1 → 0.0
           [reference behavior: ct returns 0/n on hop1; confirms reference-only rationale]

T_new_6  _TEST_ITEM_DUMMY_A  composite  always_return_ct        expected=1.0
           ct = CPQVX = expected_composite → 1.0
           [reference behavior: ct returns n/n on composite by construction; confirms
            reference-only classification rationale — trivially correct, not a shortcut]
```

---

## 5. Conclusion

The tautology guard (T_new_2) is meaningful:

```text
Guard fixture:    _TEST_ITEM_DUMMY_B (ct at rank 1)
Guard dummy:      always_return_second_C
Guard assertion:  score = 0.0 (second_C returns FVPLX, not ct)
Guard property:   always_return_second_C is NOT an oracle;
                  it scores 0.0 when ct is pinned to a rank other than 2
```

The fixture pair tests ct at rank 1 (Fixture_B) and rank 2 (Fixture_A), directly proving
rank-sensitivity. The scorer is not a tautological implementation.

**Open verification item from §2 is complete from CS side. Filed for Senior review.**

---

— CS Engineer, 2026-06-08
