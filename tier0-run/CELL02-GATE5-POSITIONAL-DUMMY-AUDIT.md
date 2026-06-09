# Cell02 Gate 5 Positional-Dummy Audit

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Authorized by:** Team Lead memo — "Cell02 Follow-Up — i08 Label Accepted; Gate 5 Positional-Dummy Audit Required" 2026-06-08
**Status:** COMPLETE — Gate 5 PASS confirmed for current dummy set; positional-coverage gap identified

---

## Purpose

Team Lead requested an offline Gate 5 / positional-dummy audit to resolve the following question:

```text
Senior's concern: In an all-C_target-last design where ct is consistently at a
fixed context position, does always_return_last_C = 0/24 mean the positional
shortcut was actually controlled for, or does it mean the dummy was blind,
non-functional, or defined differently than expected?
```

This document answers the 8 required questions and states the final Gate 5 status.

No model inference was performed. All results are derived from offline inspection of:

```text
items_twohop_l1_cell02.json     (manifest)
RESULTS-TWOHOP-L1-cell02-1780933041.json  (run artifact)
scorer_twohop_l1.py             (sha256:060afad9...)
```

---

## Answer 1 — C-object collector results per item

The scorer's `_c_objects_by_context_position()` function collects objects from facts whose `fact_role` is `hop2_fact` or `decoy_hop2_fact`, sorted by `position_index`.

For all 24 Cell02 items, the arrangement is:

```text
pos 2: dc1 hop2 fact → cd1   (C_decoy_1)
pos 6: target chain hop2 fact → ct   (C_target)
pos 7: dc2 hop2 fact → cd2   (C_decoy_2)
```

Full per-item table:

```text
Item                   ct (target)   c_by_pos: [cd1:2, ct:6, cd2:7]   first_C   last_C
twohop_l1_c02_i01      RRWRO         LVQLN:2, RRWRO:6, VBLTH:7        LVQLN     VBLTH
twohop_l1_c02_i02      VHPZM         EQNPV:2, VHPZM:6, EPXRX:7       EQNPV     EPXRX
twohop_l1_c02_i03      SKMNK         WJPGX:2, SKMNK:6, PVMEO:7       WJPGX     PVMEO
twohop_l1_c02_i04      UDNSZ         PPQDD:2, UDNSZ:6, MLIMZ:7        PPQDD     MLIMZ
twohop_l1_c02_i05      AWILF         FJUDM:2, AWILF:6, SYPKQ:7        FJUDM     SYPKQ
twohop_l1_c02_i06      IXENM         FLZAC:2, IXENM:6, DAAXS:7        FLZAC     DAAXS
twohop_l1_c02_i07      NTELO         SGEJJ:2, NTELO:6, OFWGM:7        SGEJJ     OFWGM
twohop_l1_c02_i08      AJLAC         DVRRO:2, AJLAC:6, PBKNW:7        DVRRO     PBKNW
twohop_l1_c02_i09      LVQLN         VBLTH:2, LVQLN:6, RRWRO:7        VBLTH     RRWRO
twohop_l1_c02_i10      EQNPV         EPXRX:2, EQNPV:6, VHPZM:7        EPXRX     VHPZM
twohop_l1_c02_i11      WJPGX         PVMEO:2, WJPGX:6, SKMNK:7        PVMEO     SKMNK
twohop_l1_c02_i12      PPQDD         MLIMZ:2, PPQDD:6, UDNSZ:7        MLIMZ     UDNSZ
twohop_l1_c02_i13      FJUDM         SYPKQ:2, FJUDM:6, AWILF:7        SYPKQ     AWILF
twohop_l1_c02_i14      FLZAC         DAAXS:2, FLZAC:6, IXENM:7        DAAXS     IXENM
twohop_l1_c02_i15      SGEJJ         OFWGM:2, SGEJJ:6, NTELO:7        OFWGM     NTELO
twohop_l1_c02_i16      DVRRO         PBKNW:2, DVRRO:6, AJLAC:7        PBKNW     AJLAC
twohop_l1_c02_i17      VBLTH         RRWRO:2, VBLTH:6, LVQLN:7        RRWRO     LVQLN
twohop_l1_c02_i18      EPXRX         VHPZM:2, EPXRX:6, EQNPV:7       VHPZM     EQNPV
twohop_l1_c02_i19      PVMEO         SKMNK:2, PVMEO:6, WJPGX:7        SKMNK     WJPGX
twohop_l1_c02_i20      MLIMZ         UDNSZ:2, MLIMZ:6, PPQDD:7        UDNSZ     PPQDD
twohop_l1_c02_i21      SYPKQ         AWILF:2, SYPKQ:6, FJUDM:7        AWILF     FJUDM
twohop_l1_c02_i22      DAAXS         IXENM:2, DAAXS:6, FLZAC:7        IXENM     FLZAC
twohop_l1_c02_i23      OFWGM         NTELO:2, OFWGM:6, SGEJJ:7        NTELO     SGEJJ
twohop_l1_c02_i24      PBKNW         AJLAC:2, PBKNW:6, DVRRO:7        AJLAC     DVRRO
```

**Summary:** For all 24 items without exception:
```text
first_C = cd1 (pos 2)
second_C = ct  (pos 6)   ← C_TARGET IS ALWAYS SECOND IN POSITION ORDER
last_C  = cd2 (pos 7)
ct == first_C: False (all 24)
ct == last_C:  False (all 24)
```

---

## Answer 2 — Is target C last among the collector's C-object list?

```text
No. ct is NOT last for any of the 24 items.

For all 24 items:
  ct is at context position 6 — the SECOND C-endpoint in position order.
  cd2 is at context position 7 — the LAST C-endpoint in position order.

This is the Gate 5 forced arrangement (see generate_cell02.py and
CELL02-PREP-LOCK-PACKET-TWOHOP-L1.md): dc2 hop2 was placed at pos 7
specifically to prevent last_C = ct = 24/24 → Gate 5 FAIL.

The forced arrangement is verified to be present in all 24 items.
The Gate 5 fix was applied correctly.
```

---

## Answer 3 — Query types to which always_return_first_C and always_return_last_C are applied

The scorer's `compute_dummy_baseline_scores(item, query_type)` is called for every query type. The C-object collection (`_c_objects_by_context_position`) does not depend on `query_type`. The same `c_by_pos` list (and therefore the same `first_C` and `last_C` values) is used for all four query types.

```text
always_return_first_C applied to:   hop1 ✓  hop2 ✓  composite ✓  negative_graph ✓
always_return_last_C  applied to:   hop1 ✓  hop2 ✓  composite ✓  negative_graph ✓
```

These dummies are not selectively applied. They are computed for every item × query_type combination (96 total).

---

## Answer 4 — Per-query-type dummy scores (full table)

Scores are aggregated over 24 items per query type:

```text
Dummy baseline                    hop1    hop2    composite   negative_graph
always_return_first_C             0/24    0/24    0/24        0/24
always_return_last_C              0/24    0/24    0/24        0/24
always_return_C_decoy_1           0/24    0/24    0/24        0/24
always_return_C_decoy_2           0/24    0/24    0/24        0/24
always_return_B_target           24/24    0/24    0/24        0/24
always_return_anchor_A            0/24    0/24    0/24        0/24
always_return_NULL                0/24    0/24    0/24       24/24
uniform_random_expected           8/24    8/24    8/24        6/24
```

Notes:
- always_return_B_target = 24/24 on hop1 (expected — hop1 answer is always bt)
- always_return_NULL = 24/24 on negative_graph (expected — correct answer is NULL)
- always_return_C_decoy_1 = always_return_first_C in this construction (cd1 at pos 2)
- always_return_C_decoy_2 = always_return_last_C in this construction (cd2 at pos 7)

---

## Answer 5 — Composite-query scores for first_C and last_C

```text
composite: always_return_first_C = 0/24
composite: always_return_last_C  = 0/24
```

Both positional dummies score 0/24 on composite. Neither cd1 (pos 2) nor cd2 (pos 7) is the correct composite answer. The correct composite answer is always ct (pos 6), which is not tested by any positional dummy in the current set.

---

## Answer 6 — Why composite always_return_last_C = 0/24 despite all-C_target-last construction

```text
The all-C_target-last construction places T-hop2 (ct) at context position 6.
last_C is defined by the scorer as the C-endpoint introduced LAST in context order.
In Cell02, the forced arrangement places cd2 (decoy_chain_2 hop2) at pos 7 — AFTER ct at pos 6.

Therefore:
  c_by_pos = [cd1(2), ct(6), cd2(7)]
  last_C = cd2 (pos 7) ≠ ct

always_return_last_C returns cd2, which is the wrong answer for composite (expected: ct).
Result: 0/24. This is correct behavior for the Gate 5 forced arrangement.

The 0/24 does NOT mean the dummy was blind or non-functional.
It means the dummy was functional and correctly reflected that the last-positioned
C-endpoint (cd2 at pos 7) is not the composite answer.
The Gate 5 fix worked as designed.
```

---

## Answer 7 — Does any always_return_last_C score exceed the Gate 5 ceiling?

```text
Gate 5 ceiling: max_det ≤ 9/24

always_return_last_C composite = 0/24 ≤ 9/24 ✓ — does NOT exceed ceiling
always_return_first_C composite = 0/24 ≤ 9/24 ✓ — does NOT exceed ceiling
max_det over all 8 dummies across all query types = 0/24 (excluding the structurally
  expected 24/24 cases: hop1/always_return_B_target and neg_graph/always_return_NULL,
  which are correct and not shortcuts)

Gate 5 ceiling is not violated by any included dummy.
```

---

## Answer 8 — Final Gate 5 status for Cell02

```text
Gate 5: PASS — confirmed for current dummy set
  Max over all non-trivially-expected dummies = 0/24 ≤ 9/24
  The positional dummies (first_C, last_C) were applied correctly to composite
  The Gate 5 forced arrangement (cd2 at pos 7) was present in all 24 items
  The always_return_last_C = 0/24 result is correct and non-degenerate

HOWEVER: positional-coverage gap identified (see §9)
```

---

## 9. Positional-coverage gap — critical finding

```text
COVERAGE GAP: "always_return_second_C" shortcut is not tested

For all 24 Cell02 items:
  ct is at position 6 — consistently the SECOND C-endpoint in context order

A positional shortcut "return the second C-endpoint by context position"
would return ct for all 24 items. Applied to composite:
  always_return_second_C (composite) = 24/24

This shortcut is NOT included in the current dummy set.
No existing dummy (first_C, last_C, C_decoy_1, C_decoy_2) tests it.

The Gate 5 fix successfully blocked "return-last-C" = cd2 → 0/24.
But it placed ct at a different consistent position (6 of 7 facts),
creating a new positional regularity that any second_C shortcut exploits perfectly.

Why this happened:
  The standard Gate 5 design tests first_C and last_C as the most obvious
  positional shortcuts. In Cell01's mixed 8+8+8 design, ct appeared at different
  positions for different items, so no consistent "return-position-X" shortcut existed.
  In Cell02's all-C_target-last design, ct is locked at position 6 for all 24 items,
  creating a position-invariant structural regularity not anticipated by the existing
  positional dummy set.

Impact assessment:
  composite score = 20/24
  always_return_second_C (composite) would = 24/24
  Cell02 composite (20/24) < always_return_second_C (24/24)
  This is inconsistent with the model purely using the "return-second-C" shortcut.
  However: it does NOT exclude partial shortcut use. A model could use this
  structural shortcut for some items and fail others for independent reasons.
  Without an explicit dummy, partial use cannot be quantified.

Classification:
  Gate 5: PASS as currently defined (max_det = 0/24 for included dummies — confirmed)
  Control-integrity: COVERAGE GAP for all-C_target-last axis design
    The current dummy set does not test the second-C positional shortcut
    If always_return_second_C were added, it would score 24/24 on composite
    → Gate 5 would FAIL if this dummy were included
    → Cell02 composite diagnostic should carry a control-integrity caveat

Required caveat (per Team Lead filing instructions):
  Cell02 Gate 5 is not a verified control pass for the always_return_second_C
  (= always_return_ct) positional shortcut. Composite diagnostics should be read
  with the caveat that the "return the second-by-position C-endpoint" shortcut
  was not excluded by the current dummy set. This shortcut would score 24/24
  on composite. Cell02 composite (20/24) is below this ceiling, but partial
  use cannot be excluded.
```

---

## 10. Impact on Cell02 stress eligibility and Claim B status

```text
Gate 1 remains the first failed gate (hop2 FORMAT_PASS 23/24).
Cell02 is NOT stress-eligible regardless of Gate 5 status.
The Claim B dirty-cell constructibility-boundary point filing stands.

The Gate 5 coverage gap affects:
  (a) Interpretation of Cell02 composite (20/24) — "return-second-C" shortcut not excluded
  (b) The composite diagnostic in CLAIM-B-MAP-ENTRY-TWOHOP-L1-CELL02.md §4 Axis B
  (c) The Gate 5 entry in RESULTS-TWOHOP-L1-cell02-ALL.md §5

The Gap does NOT affect:
  hop1 diagnostic (9/24) — the "return-second-C" shortcut doesn't help hop1
    (hop1 correct answer is bt, not ct; second_C = ct = always_return_ct ≠ bt)
  hop2 near-ceiling (23/24) — expected; hop2 directly tests ct retrieval
  negative_graph 0/24 — not affected
  Adjacency-driven endpoint-attraction finding (11/15 hop1 wrong_neighbor)
  Cell03 axis recommendation (adjacency separation)
  Gate 1 result
```

---

## 11. Required document updates

Per Team Lead instructions:

```text
Update Gate 5 status in:
  RESULTS-TWOHOP-L1-cell02-ALL.md        — §5 Gate table (add coverage-gap note)
  CLAIM-B-MAP-ENTRY-TWOHOP-L1-CELL02.md  — §3 Gate summary (add coverage-gap note)
  EXPERIMENT_LOG.md                       — authorization record update

Required caveat text:
  "Cell02 Gate 5 is not a verified control pass for the always_return_second_C
  positional shortcut. Composite diagnostics should be read with the caveat that
  the return-second-C (= return-ct) shortcut was not tested by the current dummy set.
  If tested, it would score 24/24 on composite. Cell02 composite (20/24) is below
  this ceiling, but partial use cannot be excluded."
```

---

## 12. Authorization boundary

```text
This document authorizes:
  offline inspection and classification of Gate 5 control integrity
  documentation updates as specified

This document does NOT authorize:
  rerun
  Cell03 construction
  Gate 5 dummy set amendment (would require new scorer hash and Manager authorization)
  model inference of any kind
```

---

**Gate 5 positional-dummy audit complete.**
**Gate 5 PASS confirmed for current dummy set. Positional-coverage gap identified and documented.**

— CS Engineer, 2026-06-08
