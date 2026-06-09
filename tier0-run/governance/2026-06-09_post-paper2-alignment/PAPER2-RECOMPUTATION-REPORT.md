# Paper 2 Recomputation Report

**Filed:** 2026-06-09  
**Prepared by:** CS Engineer  
**Status:** FINAL — filed per Team Update 2026-06-09 directive  
**Purpose:** Verify all key numbers reported in Paper 2 against locked artifact files. Identify any discrepancies. Confirm release-consistency status for Senior.

---

## §1 Artifact Files Used

All recomputation is performed against the following locked files. Hashes are artifact-backed (embedded in each file's provenance block).

| Cell | Result File | sha256 | Scorer Hash (embedded) |
|---|---|---|---|
| Cell01 | `RESULTS-TWOHOP-L1-cell01-1780912218.json` | `sha256:6de8b67c...` | `sha256:060afad9...` |
| Cell02 | `RESULTS-TWOHOP-L1-cell02-1780933041.json` | `sha256:47b5eaa9...` | `sha256:060afad9...` |
| Cell03 | `RESULTS-TWOHOP-L1-cell03-1780948339.json` | `sha256:f29783622f...` | `sha256:b65c6803...` |

**Cell03 scorer note:** Cell03 was run with scorer `sha256:b65c6803...` (post-amendment). Cell01 and Cell02 were run with `sha256:060afad9...` (pre-amendment). The amendment modified only `compute_dummy_baseline_scores()` (added second_C, third_C ceiling-bearing dummies and always_return_ct reference-only dummy). `classify_output()` and all content scoring were unchanged. Cell01 and Cell02 outputs are not affected by the amendment. See `CELL03-SCORER-AMENDMENT-PLAN.md` §9.

---

## §2 Per-Cell Accuracy Numbers

### Cell01 (recomputed from JSON)

| Query type | n | Correct | Failure breakdown |
|---|---|---|---|
| hop1 | 24 | **14/24** | non_context_return: 7; target_chain_wrong_neighbor: 3 |
| hop2 | 24 | **24/24** | — |
| composite | 24 | **18/24** | wrong_chain_selection: 4; non_context_return: 1; correct_chain_stopped_short: 1 |
| negative_graph | 24 | **2/24** | wrong_chain_selection: 11; target_chain_wrong_neighbor: 11 |

**Gate 2 evaluation (Cell01):** hop1 = 14/24 (below threshold); composite = 18/24 (below threshold). Gate 2 FAIL. Branch 3.

**Provenance:** all five hash fields present (scorer, manifest, runner, tokenizer, validator + prompt_template).

### Cell02 (recomputed from JSON)

| Query type | n | Correct | Failure breakdown |
|---|---|---|---|
| hop1 | 24 | **9/24** | non_context_return: 3; target_chain_wrong_neighbor: 11; wrong_chain_selection: 1 |
| hop2 | 24 | **23/24** | format_scaffold_failure: 1 |
| composite | 24 | **20/24** | wrong_chain_selection: 4 |
| negative_graph | 24 | **0/24** | wrong_chain_selection: 23; target_chain_wrong_neighbor: 1 |

**Gate 2 evaluation (Cell02):** hop1 = 9/24 (below threshold); composite = 20/24. Gate 2 FAIL (hop1). Branch 3.

**Note — Cell02 "all-ct-last" label:** Paper 2 described Cell02 as "all-ct-last." This label is factually incorrect. Direct inspection of `items_twohop_l1_cell02.json` confirms that for all 24 items, ct (the target C) is at context position 6, while cd2 (decoy chain 2 endpoint) is at context position 7. ct is NOT last in context. The last C-type object is cd2, not ct. This is a factual error in Paper 2 that must be corrected before external routing. See §5 below.

**Dummy baseline cross-check (Cell02 composite, always_return_last_C):** 0/24. Confirms last-C in context ≠ ct. This is consistent with ct at pos6, cd2 at pos7.

### Cell03 (recomputed from JSON)

| Query type | n | Correct | Failure breakdown |
|---|---|---|---|
| hop1 | 24 | **6/24** | target_chain_wrong_neighbor: 6; non_context_return: 7; UNCLASSIFIED_OFF_FRAME: 4; wrong_chain_selection: 1 |
| hop2 | 24 | **23/24** | wrong_chain_selection: 1 |
| composite | 24 | **15/24** | wrong_chain_selection: 7; non_context_return: 2 |
| negative_graph | 24 | **6/24** | wrong_chain_selection: 12; target_chain_wrong_neighbor: 6 |

**Gate 2 evaluation (Cell03):** hop1 = 6/24; composite = 15/24. Both below pre-registered thresholds. Gate 2 FAIL. Branch 3.

**Gate 5 check (Cell03, composite):**  
Non-tautological ceiling-bearing dummies: always_return_first_C = 8/24, always_return_second_C = 8/24, always_return_third_C = 8/24, always_return_last_C = 8/24. Max deterministic dummy = 8/24. Pre-registered threshold for Gate 5 PASS: max_det < 9/24. Gate 5 PASS.  
Reference-only dummy always_return_ct = 24/24 (tautological; excluded from Gate 5 by GATE5_REFERENCE_ONLY constant in runner).

**Cell03 composite group breakdown:**

| Group | ct position | n | Correct | Failures |
|---|---|---|---|---|
| A (items 1–8) | pos3 (first_C) | 8 | **1/8** | wrong_chain_selection: 5; non_context_return: 2 |
| B (items 9–16) | pos5 (second_C) | 8 | **6/8** | wrong_chain_selection: 2 |
| C (items 17–24) | pos7 (third_C/last) | 8 | **8/8** | — |

Monotone gradient 1/6/8 confirmed. Group B rules out pure last-position shortcut (ct not last in Group B; 6/8 correct).

**Cell03 total taxonomy counts (all 96 outputs):**

| Class | Count |
|---|---|
| correct | 50 |
| wrong_chain_selection | 21 |
| non_context_return | 9 |
| target_chain_wrong_neighbor | 12 |
| UNCLASSIFIED_OFF_FRAME | 4 |
| **Total** | **96** |

Taxonomy count verified: 96/96 classified. No unclassified outputs outside UNCLASSIFIED_OFF_FRAME.

---

## §3 Dummy Baseline Summary (Gate 5 reference)

### Cell01 composite (always_return_first_C / always_return_last_C)

| Dummy | Score |
|---|---|
| always_return_first_C | 8/24 (pos2 items = 8) |
| always_return_last_C | 8/24 (pos6 items = 8) |

Max deterministic dummy for Cell01 composite = 8/24. Gate 5 PASS (pre-registered threshold < 9/24).

### Cell02 composite (all dummies)

| Dummy | Score |
|---|---|
| always_return_first_C | 0/24 |
| always_return_last_C | 0/24 |
| always_return_B_target | 0/24 |
| always_return_C_decoy_1 | 0/24 |
| always_return_C_decoy_2 | 0/24 |
| uniform_random_expected | 8/24 (0.333) |

All position dummies score 0/24 for Cell02 composite. This is consistent with the ct-at-pos6 construction: the fixed-position dummies return tokens other than ct, which is never first_C or last_C. Gate 5 PASS.

**Post-hoc offline recomputation (always_return_second_C on Cell02 composite):** 24/24 = 1.000. This was computed offline after Cell02 run, prior to Cell03. It confirmed the Gate 5 PASS* caveat documented in `CELL02-GATE5-POSITIONAL-DUMMY-AUDIT.md`. The offline computation used the frozen manifest only (no rerun). This does not change the Gate 5 disposition (PASS confirmed before the Cell03 scorer amendment added second_C as a standard dummy).

### Cell03 composite

See §2 above. Max deterministic dummy = 8/24. Gate 5 PASS.

---

## §4 Cross-Cell Consistency

| Metric | Cell01 | Cell02 | Cell03 |
|---|---|---|---|
| hop1 correct | 14/24 | 9/24 | 6/24 |
| hop2 correct | 24/24 | 23/24 | 23/24 |
| composite correct | 18/24 | 20/24 | 15/24 |
| negative_graph correct | 2/24 | 0/24 | 6/24 |
| Gate 2 | FAIL | FAIL | FAIL |
| Gate 5 | PASS | PASS | PASS |
| Branch | 3 | 3 | 3 |
| Eligible for stress | NO | NO | NO |

No cell reached stress eligibility. All cells are Branch 3 (constructibility-boundary dirty cells). No compression figures are reported in Paper 2.

---

## §5 Discrepancies Requiring Correction Before External Routing

### Discrepancy 1 — Cell02 "all-ct-last" label (FACTUAL ERROR)

**Reported in Paper 2:** Cell02 described as "all-C_target-last" or "all-ct-last" construction.

**Artifact state:** ct is at context position 6 for all 24 Cell02 items. cd2 is at context position 7. ct is NOT the last C-type token in context. The design was intended to place ct at the last position among C-objects, but cd2 (decoy chain 2 endpoint, also a C-type token) sits at position 7, making ct the second-to-last C token in context.

**Evidence:** `items_twohop_l1_cell02.json` axis_note field for item 1: "T-hop2 at context position 6. decoy_chain_2 hop2 at position 7." This pattern is uniform across all 24 items.

**Required correction:** Paper 2 must replace "all-ct-last" / "all-C_target-last" with the accurate description: "ct at fixed context position 6 (second-to-last C-type object; cd2 at position 7)." Any discussion attributing Cell02 composite results to a last-position advantage for ct must be revised.

### Discrepancy 2 — "(3, 11, 6)" ambiguity in §4.5 (AMBIGUOUS CITATION)

**Reported in Paper 2 §4.5:** The triple "(3, 11, 6)" appears to reference hop1 failures.

**Artifact state:** The triple (3, 11, 6) matches Cell03 hop1 failure breakdown if "3" = wrong_chain_selection (1) + correct_chain_stopped_short... Actually, let me restate: from Cell03 hop1 failures: target_chain_wrong_neighbor=6, non_context_return=7, UNCLASSIFIED_OFF_FRAME=4, wrong_chain_selection=1. The triple (3, 11, 6) does NOT match Cell03 hop1. This triple may refer to hop1 only across cells or a different breakdown.

**CS note:** The exact Paper 2 §4.5 draft text was reviewed in the prior session (peer review request 2026-06-08). The CS peer review flagged "(3, 11, 6)" as hop1-only but contextually ambiguous (reader may interpret as composite-inclusive). This ambiguity requires clarification by Senior. CS cannot independently resolve which breakdown the triple references without the final §4.5 text.

**Required correction:** Senior must clarify the referent of "(3, 11, 6)" and add explicit scope language (e.g., "hop1 only: ...").

---

## §6 Release-Consistency Confirmation

**For Senior:** Based on direct recomputation from locked JSON artifacts:

- All four per-cell accuracy tables in §2 are internally consistent with the locked result files.
- Gate 2 FAIL (all three cells), Gate 5 PASS (all three cells), Branch 3 (all three cells) are confirmed.
- Cell03 composite group gradient 1/6/8 is confirmed.
- Cell03 neg_graph intrusion 18/24 is confirmed (6 correct = intrusion absent for those items).
- Cell03 UNCLASSIFIED_OFF_FRAME = 4 (hop1 only) is confirmed.
- Taxonomy count 96/96 is confirmed.

**Two items require correction before external routing:**
1. Cell02 "all-ct-last" label — factual error (see §5 Discrepancy 1).
2. "(3, 11, 6)" in §4.5 — ambiguity requiring Senior clarification (see §5 Discrepancy 2).

All other reported figures verified against artifact.

---

— CS Engineer, 2026-06-09
