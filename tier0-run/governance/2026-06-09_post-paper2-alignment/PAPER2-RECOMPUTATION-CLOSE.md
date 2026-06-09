# Paper 2 Recomputation Close

**Filed:** 2026-06-09  
**Prepared by:** CS Engineer  
**Status:** FINAL — closes Paper 2 recomputation hold for Senior  
**Source:** Direct computation from locked artifact JSONs. All counts recomputed from `RESULTS-TWOHOP-L1-cell0{1,2,3}-*.json` — no summary language relied upon.

---

## Confirmation 1 — Locked JSON files checked

| Cell | File | sha256 |
|---|---|---|
| Cell01 (valid run) | `RESULTS-TWOHOP-L1-cell01-1780912218.json` | `sha256:6de8b67c0267a65f088e7bccd68b3cd070c675938c71470dd97a5411daca6f47` |
| Cell02 | `RESULTS-TWOHOP-L1-cell02-1780933041.json` | `sha256:47b5eaa9b954645ca2572fe20873a0255776f60f29b0a544d8c350dcddc181ca` |
| Cell03 | `RESULTS-TWOHOP-L1-cell03-1780948339.json` | `sha256:f29783622fb14caca1c2a5829da8b874836add5d111356ea42be1f7d4a7b73f7` |

---

## Confirmation 2 — All 12 per-cell accuracy counts

Counts are `is_correct=True` by `query_type`, computed directly from each result JSON.

| Cell | hop1 | hop2 | composite | negative_graph |
|---|---|---|---|---|
| Cell01 | **14/24** | **24/24** | **18/24** | **2/24** |
| Cell02 | **9/24** | **23/24** | **20/24** | **0/24** |
| Cell03 | **6/24** | **23/24** | **15/24** | **6/24** |

---

## Confirmation 3 — Match against Paper 2

**All 12 counts match Paper 2 as reported.** No numeric discrepancy identified between the locked artifact files and the Paper 2 accuracy tables.

---

## Confirmation 4 — Cell02 composite value

**Confirmed: Cell02 composite = 20/24.** Failure breakdown: wrong_chain_selection = 4. No other failure classes in composite.

---

## Confirmation 5 — Cell03 group decomposition

**Confirmed from artifact (composite query_type, by item_id range):**

| Group | n | Correct | wrong_chain to cd2@pos7 | NULL (non_context_return) |
|---|---|---|---|---|
| A (i01–i08, ct=first_C, pos3) | 8 | **1/8** | **5/8** | **2/8** |
| B (i09–i16, ct=second_C, pos5) | 8 | **6/8** | **2/8** | **0/8** |
| C (i17–i24, ct=third_C/last, pos7) | 8 | **8/8** | **0/8** | **0/8** |

**Additional confirmation on wrong_chain tokens:** All 7 wrong_chain_selection failures in composite were confirmed by §8 diagnostics to return `C_decoy_endpoint` tokens at absolute position 7 (cd2). The `distractor_chain_endpoint` role is confirmed for all 7. Gradient 1/6/8 confirmed.

---

## Confirmation 6 — Negative-graph endpoint taxonomy

**Confirmed from §8 `s8_diagnostics.returned_role` field, computed directly from artifact JSON:**

| Intrusion type | Count | §8 role value | failure_class |
|---|---|---|---|
| Distractor chain endpoint | **10** | `distractor_chain_endpoint` | wrong_chain_selection |
| Distractor chain intermediate | **2** | `distractor_chain_intermediate` | wrong_chain_selection |
| hop1_B (target-chain B-node) | **6** | `hop1_B` | target_chain_wrong_neighbor |
| ct return | **0** | — | — |
| **Total intrusions** | **18** | | |
| Correct (NULL) | **6** | | |

All 18 intrusion outputs have `neg_graph_endpoint_intrusion: True` in §8 diagnostics. Zero ct returns confirmed.

**Group breakdown (negative_graph):**

| Group | Correct (NULL) | distractor_chain_endpoint | distractor_chain_intermediate | hop1_B |
|---|---|---|---|---|
| A (i01–i08) | 5 | 3 | 0 | 0 |
| B (i09–i16) | 0 | 6 | 2 | 1 |
| C (i17–i24) | 1 | 1 | 0 | 5 |

---

## Confirmation 7 — Gate 5 max_det

**Confirmed: Gate 5 max_det = 8/24 for all three cells.**

Cell03 ceiling-bearing dummies (composite): always_return_first_C = 8/24, always_return_second_C = 8/24, always_return_third_C = 8/24, always_return_last_C = 8/24. Max = 8/24. Threshold = 9/24. Gate 5 PASS.

Cell01 ceiling-bearing dummies (composite): always_return_first_C = 8/24, always_return_last_C = 8/24. Max = 8/24. Gate 5 PASS.

Cell02 ceiling-bearing dummies (composite): always_return_first_C = 0/24, always_return_last_C = 0/24. Max non-tautological = uniform_random_expected = 8/24 (0.333). Gate 5 PASS.

---

## Confirmation 8 — Voided Cell01 run excluded

**Confirmed: voided run excluded from all counts and Paper 2.**

Voided run file: `RESULTS-TWOHOP-L1-cell01-1780911140.json`  
Disposition: 96/96 FORMAT_FAIL (SCAFFOLD_PRESENT + FORMAT_FAIL for all items). Caused by mlx_lm 0.8.0 environment + missing chat template. Voided per `RUNNER-AMENDMENT-LOCK-NOTE-TWOHOP-L1.md`.  
Valid Cell01 run: `RESULTS-TWOHOP-L1-cell01-1780912218.json` — used for all Paper 2 counts.

No output from the voided run appears in any Paper 2 table or figure.

---

## Confirmation 9 — Mismatches, unresolved artifact issues, recomputation caveats

**No numeric mismatches identified.**

**Two non-numeric issues remain (both previously routed to Senior):**

1. **Cell02 "all-ct-last" label — factual framing error.** ct is at context pos6, cd2 at pos7. The label "all-ct-last" incorrectly implies ct is the last C-type token in context. See `PAPER2-CORRECTION-CONFIRMATION.md` — Senior has already corrected this per the Team Lead memo.

2. **§4.5 "(3, 11, 6)" scope ambiguity.** Already clarified as hop1-only per Senior's correction. See `PAPER2-CORRECTION-CONFIRMATION.md`.

**No other recomputation caveats.** All 12 counts, Gate 5 values, group gradient, and endpoint taxonomy are artifact-backed and match Paper 2.

---

## Release-consistency status

**Paper 2 recomputation: CONFIRMED.**

All reported numbers match locked artifact files. Gate evaluations confirmed. Voided run excluded. Senior may move Paper 2 from release candidate to release-consistency confirmed, pending acceptance of the two framing corrections (§PAPER2-CORRECTION-CONFIRMATION.md).

---

— CS Engineer, 2026-06-09
