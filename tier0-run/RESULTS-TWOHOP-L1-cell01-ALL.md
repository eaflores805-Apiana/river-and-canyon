# Run Summary — Two-Hop Level 1 Cell 01 — All Query Types

**Template version:** Stage 0 — 2026-06-07
**Filed:** 2026-06-08
**Filed by:** CS Engineer

---

## 1. Run identity

```
Date:              2026-06-08
Cell ID:           cell01
Query types:       hop1, hop2, composite, negative_graph (all 4 — single combined run)
Model:             Qwen/Qwen2.5-3B-Instruct
Precision:         FP16
Runner script:     tier0-run/runner_twohop_l1.py (amended — sha256:f346e4f2...)
Authorization:     Manager memo — "FP16 Stage 1 Execution Authorization — Two-Hop Level 1"
                   and "FP16 Stage 1 Run Escalation — Disposition and Runner Amendment Authorization"
                   both 2026-06-08
Status:            FAIL (Gate 2 — hop1 14/24, composite 18/24 below ≥21/24 threshold)

Run artifact:      tier0-run/RESULTS-TWOHOP-L1-cell01-1780912218.json
Voided prior run:  tier0-run/RESULTS-TWOHOP-L1-cell01-1780911140.json
                   (VOID — environment/runner incompatibility; not Stage 1 data)
```

---

## 2. Gate results (ordered — a failed gate blocks all below)

```
Gate 0    Axis-control & manifest    PASS
            24/24 validate_manifest pass; axis = single axis (token identity);
            ordering 8+8+8; frozen settings documented; identical_context_hash verified;
            negative_graph path-absence confirmed (all items)

Gate 0.5  Token-construction audit   PASS (reconciled 2026-06-08 — see §16)
            BPE round-trip 0 failures; Lev ≤ 2 violations 0; trigram-Jaccard violations 0;
            BPE-Jaccard cross-chain C violations 0; 24 declared near-miss pairs confirmed
            (lev ≤ 2, tjac ≥ 0.20, bjac ≥ 0.40)
            Original audit tokenizer:  sha256:3fd169731d... (INT4 MLX serialization)
            Re-run under run tokenizer: sha256:c0382117... (FP16 HuggingFace) — PASS
            Equivalence confirmed: vocab identical (151,643); normalized merges identical (151,387);
            BPE behavior identical. See TOKENIZER-HASH-RECONCILIATION-TWOHOP-L1.md.

Gate 1    Contract adherence         PASS
            hop1:          24/24 FORMAT_PASS  (0 format_scaffold_failure)
            hop2:          24/24 FORMAT_PASS  (0 format_scaffold_failure)
            composite:     24/24 FORMAT_PASS  (0 format_scaffold_failure)
            negative_graph: 24/24 FORMAT_PASS (0 format_scaffold_failure)

Gate 2    FP16 baseline correctness  FAIL
            hop1:      14/24 = 0.583  threshold ≥ 21/24  → FAIL (G2a)
            hop2:      24/24 = 1.000  threshold ≥ 21/24  → PASS (G2b)
            composite: 18/24 = 0.750  threshold ≥ 21/24  → FAIL (G2c)
            [negative_graph not part of G2; 2/24 reported in §4]

Gate 3    Operation fidelity         BLOCKED by Gate 2
            (computed for diagnostic record — not binding)
            stopped_short:    1/24  ceiling ≤ 3/24  → PASS
            shortcut_single:  0/24  ceiling ≤ 2/24  → PASS
            wrong_chain:      4/24  ceiling ≤ 3/24  → FAIL (exceeds ceiling)
            wrong_neighbor:   0/24  ceiling ≤ 3/24  → PASS
            anchor_echo:      0/24  ceiling ≤ 3/24  → PASS

Gate 4a   Classifier reliability     BLOCKED by Gate 2
            (computed) unique_assignment_rate = 1.000 (scorer guarantee — PASS)
            (computed) UNCLASSIFIED_OFF_FRAME = 0/24 = 0.000 ≤ 0.05 → PASS
            watch trigger (> 0.02): not triggered

Gate 4b   Failure-class separability BLOCKED by Gate 2

Gate 5    Control adequacy           BLOCKED by Gate 2
            (dummy baselines verified at construction):
            max_dummy = 8/24 = 0.333 ≤ 9/24 = 0.375 → PASS
            Gate-2 composite (18) − max_dummy (8) = 10 ≥ 10 → PASS (at minimum)
            max_dummy 0.333 ≤ chance 0.333 + 0.05 → PASS
            negative_graph null_return: 2/24 = 0.083 (see §7)

Gate 5.5  Baseline-stability confirm N/A (Manager-authorized only)

Gate 6    Stress eligibility         NOT ELIGIBLE
            Gate 2 fails; cell is not stress-eligible

First failed gate:    Gate 2
Blocking reason:      hop1 14/24 < 21/24; composite 18/24 < 21/24
                      Cell falls below FP16 constructibility floor on two of three required
                      query types. Cell is a constructibility-boundary result, not a clean cell.
```

---

## 3. Provenance

```
manifest_hash:              sha256:00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28
scorer_hash:                sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd
validator_hash:             sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
runner_hash:                sha256:f346e4f2cf93b881e129ba25bea469e2f6349ce1b6d430f8ddfb7269f3d0d7ce
tokenizer_hash:             sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
                            (FP16 HuggingFace — confirmed run tokenizer; reconciled 2026-06-08)
tokenizer_hash_audit:       sha256:3fd169731d2cbde95e10bf356d66d5997fd885dd8dbb6fb4684da3f23b2585d8
                            (INT4 MLX — used in original BPE-Jaccard audit; confirmed serialization
                             variant only; vocab and normalized merges identical — see §16)
prompt_template_hash:       sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
failure_taxonomy_version:   v1.0
model_id:                   Qwen/Qwen2.5-3B-Instruct
model_snapshot:             aa8e72537993ba99e69dfaafa59ed015b17504d1
model_local_path:           ~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/
                            snapshots/aa8e72537993ba99e69dfaafa59ed015b17504d1
decoding_settings:          temperature=0.0, max_tokens=16
                            (sampler: stream_generate temp= kwarg via generate_step)
axis_configuration:         Single axis: token identities vary across items.
                            Ordering 8+8+8: items 1-8 C_target-first (T-hop2 at pos 2),
                            items 9-16 C_target-middle (T-hop2 at pos 4),
                            items 17-24 C_target-last (T-hop2 at pos 6).
frozen_settings:            relation_hop1='links to'; relation_hop2='maps to';
                            relation_hold='holds'; context_length=7 facts;
                            chains_per_item=3 (target + decoy_1 + decoy_2);
                            query_phrasing=template;
                            instruction_prefix=prompt_template_twohop_l1.txt
raw_output_path:            tier0-run/RESULTS-TWOHOP-L1-cell01-1780912218.json
per_item_failure_label_path: tier0-run/RESULTS-TWOHOP-L1-cell01-1780912218.json
                             (failure_class field per result entry)
unclassified_outputs_path:  NONE (0 UNCLASSIFIED_OFF_FRAME)
```

---

## 4. Scoring breakdown

### hop1

```
n_items:          24
pass_count:       14
pass_rate:        0.583  (14/24)
feasibility_gate: ≥ 21/24
result:           FAIL

scaffold_class:    SCAFFOLD_PRESENT: 24   SCAFFOLD_ABSENT: 0
format_class:      FORMAT_PASS: 24        FORMAT_FAIL: 0

failure_class distribution:
  correct:                       14
  format_scaffold_failure:        0
  non_context_return:             7  (all return NULL)
  correct_chain_stopped_short:    0
  anchor_echo:                    0
  wrong_chain_selection:          0
  target_chain_wrong_neighbor:    3
  UNCLASSIFIED_OFF_FRAME:         0
```

### hop2

```
n_items:          24
pass_count:       24
pass_rate:        1.000  (24/24)
feasibility_gate: ≥ 21/24
result:           PASS

scaffold_class:    SCAFFOLD_PRESENT: 24   SCAFFOLD_ABSENT: 0
format_class:      FORMAT_PASS: 24        FORMAT_FAIL: 0

failure_class distribution:
  correct:                       24
  all other classes:              0
```

### composite

```
n_items:          24
pass_count:       18
pass_rate:        0.750  (18/24)
feasibility_gate: ≥ 21/24
result:           FAIL

scaffold_class:    SCAFFOLD_PRESENT: 24   SCAFFOLD_ABSENT: 0
format_class:      FORMAT_PASS: 24        FORMAT_FAIL: 0

failure_class distribution:
  correct:                       18
  format_scaffold_failure:        0
  non_context_return:             1
  correct_chain_stopped_short:    1
  anchor_echo:                    0
  wrong_chain_selection:          4
  target_chain_wrong_neighbor:    0
  UNCLASSIFIED_OFF_FRAME:         0
```

### negative_graph

```
n_items:          24
pass_count:       2
pass_rate:        0.083  (2/24)
feasibility_gate: N/A (negative_graph not in G2a/b/c)

scaffold_class:    SCAFFOLD_PRESENT: 24   SCAFFOLD_ABSENT: 0
format_class:      FORMAT_PASS: 24        FORMAT_FAIL: 0

failure_class distribution:
  correct:                        2  (items i04, i08 — both in C_target-first group)
  format_scaffold_failure:        0
  non_context_return:             0
  correct_chain_stopped_short:    0
  anchor_echo:                    0
  wrong_chain_selection:         11
  target_chain_wrong_neighbor:   11
  UNCLASSIFIED_OFF_FRAME:         0
```

---

## 5. Dummy baseline results (composite query — Gate 5)

```
Dummy                     Score     Rate      Gate (≤9/24)   Pass/Fail
always_return_B_target     0/24     0.000     ≤ 9/24         PASS
always_return_anchor_A     0/24     0.000     ≤ 9/24         PASS
always_return_first_C      8/24     0.333     ≤ 9/24         PASS
always_return_last_C       8/24     0.333     ≤ 9/24         PASS
always_return_NULL         0/24     0.000     ≤ 9/24         PASS
always_return_C_decoy_1    0/24     0.000     ≤ 9/24         PASS
always_return_C_decoy_2    0/24     0.000     ≤ 9/24         PASS
uniform_random_expected   ~8/24     0.333     N/A            N/A

max_dummy_score:            8/24 = 0.333
feasibility_gate:           ≤ 9/24 = 0.375
max_dummy < gate:           OK  (0.333 < 0.375)

Margin check (G2e): Gate-2 composite (18) − max_dummy (8) = 10 ≥ 10 → PASS (at minimum)
Chance guard (G2f): max_dummy (0.333) ≤ chance (0.333) + 0.05 = 0.383 → PASS
```

---

## 6. Operation fidelity diagnostics — composite (Gate 3, blocked)

```
stopped_short_rate:        1/24 = 0.042    threshold ≤ 3/24    PASS
shortcut_single_hop_rate:  0/24 = 0.000    threshold ≤ 2/24    PASS (structural guarantee)
wrong_chain_routing_rate:  4/24 = 0.167    threshold ≤ 3/24    FAIL
wrong_neighbor_rate:       0/24 = 0.000    threshold ≤ 3/24    PASS
anchor_echo_rate:          0/24 = 0.000    threshold ≤ 3/24    PASS

Note: Gate 3 blocked by Gate 2 failure. Diagnostic values recorded for constructibility
mapping (Claim B). wrong_chain_selection at 4/24 exceeds the 3/24 ceiling and would
fail Gate 3 independently if Gate 2 were passed.
```

---

## 7. Control adequacy (Gate 5, blocked)

```
length_matched_control:
  Length-matched query type not in cell design. Gate 6 / G6 tolerance check: N/A.

same_context_controls:
  hop1 pass rate:       14/24 = 0.583
  hop2 pass rate:       24/24 = 1.000
  composite pass rate:  18/24 = 0.750
  identical_context_hash verified: YES (present on all items; confirmed by validate_manifest)

negative_graph_control:
  null_return_rate:     2/24 = 0.083
    (i04 NULL correct; i08 NULL correct; 22/24 return non-NULL)
  forced_endpoint_rate: 22/24 = 0.917
    11 wrong_chain_selection (decoy endpoint); 11 target_chain_wrong_neighbor (hop1_B)
  path_traversal_verified_clean: YES
    (removed_edge="target_chain/hop2" confirmed; valid_A_to_C_path_exists=false on all items)

dummy_ceiling_check:    PASS (max_dummy 8/24 ≤ 9/24; confirmed at construction and runtime)
```

---

## 8. Watch conditions

```
Novel failure classes this cell:    NONE (all 8 failure classes used; no off-frame items)
Novel class trend (saturation):     Saturating — same 7 failure classes present, standard distribution
UNCLASSIFIED_OFF_FRAME rate:        0/24 = 0.000    ceiling ≤ 0.05    OK
UNCLASSIFIED clustering:            NO

Diagnostic observation (not an interpretive claim):
  hop1 failures are concentrated in C_target-first group (items 1-8: 0/8 correct).
  Items 9-16 (C_target-middle): 6/8 hop1 correct.
  Items 17-24 (C_target-last): 8/8 hop1 correct.
  This positional pattern is a constructibility-boundary data point, not a seam or
  mechanism claim. It is recorded here for completeness only.

  hop2 is 24/24 correct across all positional groups.
  negative_graph: 2/24 NULL correct; model predominantly returns chain endpoints.
```

---

## 9. Per-item failure summary

```
item_id              hop1_fc                    hop1_tok   hop2_fc    hop2_tok   composite_fc               composite_tok  neg_graph_fc               neg_graph_tok
twohop_l1_c01_i01    non_context_return         NULL       correct    ZJMOL      wrong_chain_selection      FSLIY          wrong_chain_selection      FSLIY
twohop_l1_c01_i02    non_context_return         NULL       correct    DBKSD      correct                    DBKSD          wrong_chain_selection      UEBLS
twohop_l1_c01_i03    non_context_return         NULL       correct    MRZSP      wrong_chain_selection      HGKLW          wrong_chain_selection      HGKLW
twohop_l1_c01_i04    non_context_return         NULL       correct    YYQGH      non_context_return         NULL           correct                    NULL
twohop_l1_c01_i05    non_context_return         NULL       correct    BAGCR      correct                    BAGCR          wrong_chain_selection      PLFBI
twohop_l1_c01_i06    target_chain_wrong_neigh   XFCPN      correct    XFCPN      correct                    XFCPN          wrong_chain_selection      QDBJV
twohop_l1_c01_i07    non_context_return         NULL       correct    GTJWG      wrong_chain_selection      SVHZX          wrong_chain_selection      SVHZX
twohop_l1_c01_i08    target_chain_wrong_neigh   YXPPV      correct    YXPPV      correct                    YXPPV          correct                    NULL
twohop_l1_c01_i09    correct                    ZBUIE      correct    FSLIY      correct                    FSLIY          target_chain_wrong_neigh   ZBUIE
twohop_l1_c01_i10    correct                    ZBNBZ      correct    UEBLS      correct                    UEBLS          target_chain_wrong_neigh   ZBNBZ
twohop_l1_c01_i11    correct                    ZBRAL      correct    HUCAX      correct                    HUCAX          target_chain_wrong_neigh   ZBRAL
twohop_l1_c01_i12    correct                    ZBFSG      correct    PLZEG      correct                    PLZEG          wrong_chain_selection      QYQYP
twohop_l1_c01_i13    correct                    ZBBDR      correct    QKUOR      wrong_chain_selection      BAGCR          wrong_chain_selection      BAGCR
twohop_l1_c01_i14    correct                    ZBCXB      correct    QDBJV      correct                    QDBJV          target_chain_wrong_neigh   ZBCXB
twohop_l1_c01_i15    target_chain_wrong_neigh   SVHZX      correct    SVHZX      correct                    SVHZX          wrong_chain_selection      GTJWG
twohop_l1_c01_i16    non_context_return         NULL       correct    BKMVE      correct                    BKMVE          wrong_chain_selection      YXPPV
twohop_l1_c01_i17    correct                    ZBKYX      correct    DNXUT      correct                    DNXUT          target_chain_wrong_neigh   ZBKYX
twohop_l1_c01_i18    correct                    ZBAMV      correct    PZUPT      correct                    PZUPT          target_chain_wrong_neigh   ZBAMV
twohop_l1_c01_i19    correct                    ZBGQC      correct    HGKLW      correct                    HGKLW          target_chain_wrong_neigh   ZBGQC
twohop_l1_c01_i20    correct                    ZBOVW      correct    QYQYP      correct                    QYQYP          target_chain_wrong_neigh   ZBOVW
twohop_l1_c01_i21    correct                    ZBMFK      correct    PLFBI      correct                    PLFBI          target_chain_wrong_neigh   ZBMFK
twohop_l1_c01_i22    correct                    ZBLNF      correct    BNEQN      correct_chain_stopped_short ZBLNF         target_chain_wrong_neigh   ZBLNF
twohop_l1_c01_i23    correct                    ZBVLS      correct    DFHLZ      correct                    DFHLZ          target_chain_wrong_neigh   ZBVLS
twohop_l1_c01_i24    correct                    ZBDGA      correct    JEMZC      correct                    JEMZC          wrong_chain_selection      BKMVE

Ordering note: items 1-8 C_target-first; items 9-16 C_target-middle; items 17-24 C_target-last.
```

---

## 10. Branch routing

```
Applicable branch:      Branch 3
Branch description:     Content / distractor / position failure
                        Gate 1 passes (FORMAT_PASS = 1.000 all query types).
                        Gate 2 fails on hop1 and composite.
                        hop2 24/24 — single-hop (B→C) fully constructible at FP16.
                        hop1 14/24 — single-hop (A→B) below floor; dominant failure = NULL
                        return on C_target-first items.
                        composite 18/24 — two-hop below floor; dominant failure =
                        wrong_chain_selection (decoy chain endpoint selected instead of
                        target chain endpoint).

Next action:            Record as constructibility-boundary data for Claim B mapping.
                        Cell is not stress-eligible. Track B not unlocked.
                        Further action (cell redesign, additional cells) requires
                        separate Manager authorization.
Manager authorization:  YES — required for any next action beyond filing this result.
```

---

## 11. Scope boundary

```
This result applies only to:
  Task:       frozen cell construction cell01 (3-chain, 7-fact, 8+8+8)
  Query types: hop1, hop2, composite, negative_graph
  Context:    7 facts per item; 3 chains per item
  Prompt:     locked (prompt_template_hash sha256:c8a81a29...)
  Tokenizer:  locked (tokenizer_hash sha256:c0382117...)
  Scorer:     locked amended (scorer_hash sha256:060afad9..., FAILURE_TAXONOMY_VERSION=v1.0)
  Decoding:   temperature=0.0, max_tokens=16
  Model:      Qwen/Qwen2.5-3B-Instruct (snapshot aa8e7253...)
  Precision:  FP16

This result does not generalize to:
  other cells
  other query types
  other context orderings
  other model sizes
  other precision levels (INT8, INT4)
  natural-language tasks
```

---

## 12. Clean-cell handoff statement

Not applicable. Gate 6 = NOT ELIGIBLE. This cell is not clean and does not route to stress testing.

---

## 13. Forbidden claims

The following claims are forbidden regardless of result:

```
the seam exists / does not exist
quantization breaks reasoning
INT4 is harmful or harmless
this model cannot do two-hop linkage
a constructibility boundary is a capability boundary
a composite drop is linkage degradation without failure-class separability
behavioral evidence implies mechanism
```

Safe form: Under this frozen construction (cell01, 3-chain, 7-fact, 8+8+8), at 3B FP16,
hop1 did not reach the constructibility floor (14/24); hop2 reached it fully (24/24);
composite did not reach it (18/24). The cell is a boundary result, not a stress-eligible cell.

**FP16 only. No INT8. No INT4. No Track B.**

---

## 14. Authorization chain

```
1. Stage 0 closure — Team Lead, 2026-06-07
2. Threshold proposal review — Team Lead, 2026-06-08
3. Stage 1 preparation authorization — Manager, 2026-06-08
4. FP16 tokenizer acceptance + scorer/cell amendment (Option B + Option D) — Team Lead, 2026-06-08
5. Stage 1 Preparation Lock Packet Rev 2 accepted — Team Lead, 2026-06-08
6. FP16 Stage 1 Execution Authorization — Manager, 2026-06-08
7. FP16 Stage 1 Run Escalation Disposition + Runner Amendment Authorization (Option R1) — Manager, 2026-06-08
```

---

## 15. Files

```
tier0-run/RESULTS-TWOHOP-L1-cell01-1780912218.json  — raw + scored output (this run)
  sha256:6de8b67c0267a65f088e7bccd68b3cd070c675938c71470dd97a5411daca6f47

tier0-run/RESULTS-TWOHOP-L1-cell01-1780911140.json  — VOIDED run (environment incompatibility)
  sha256:1adeb548d4e83bdb730f4c708d91a11f6506995e87d87a433ebbf16aa9fa0c8e

tier0-run/RESULTS-TWOHOP-L1-cell01-ALL.md           — this summary

tier0-run/runner_twohop_l1.py                        — amended runner
  sha256:f346e4f2cf93b881e129ba25bea469e2f6349ce1b6d430f8ddfb7269f3d0d7ce

tier0-run/RUNNER-AMENDMENT-LOCK-NOTE-TWOHOP-L1.md   — runner amendment lock note

tier0-run/scorer_twohop_l1.py                        — amended scorer
  sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd

tier0-run/items_twohop_l1_cell01.json                — locked cell JSON
  sha256:00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28

tier0-run/tasks_twohop_l1.py                         — locked validator
  sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b

tier0-run/prompt_template_twohop_l1.txt              — locked prompt template
  sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e

tier0-run/STAGE1-PREP-LOCK-PACKET-TWOHOP-L1.md      — Revision 2 preparation lock packet
tier0-run/STAGE1-RUN-MEMO-TWOHOP-L1.md              — Stage 1 Run Memo
tier0-run/STAGE0-INSTRUMENT-LOCK-PACKET.md           — Stage 0 instrument lock (scorer amendment §10)
tier0-run/TOKENIZER-HASH-RECONCILIATION-TWOHOP-L1.md — Tokenizer hash reconciliation (Gate 0.5 re-audit)
```

---

## 16. Tokenizer hash reconciliation (Gate 0.5 — post-filing)

**Requested by:** Team Lead, 2026-06-08  
**Status:** RECONCILED

### Discrepancy

The BPE-Jaccard audit (Gate 0.5) was originally performed during cell generation using:

```
sha256:3fd169731d2cbde95e10bf356d66d5997fd885dd8dbb6fb4684da3f23b2585d8
(local MLX INT4/INT8 tokenizer.json at Qwen2.5-3B-Instruct-mlx-int4/tokenizer.json)
```

The Stage 1 FP16 run was performed using:

```
sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
(FP16 HuggingFace tokenizer.json, snapshot aa8e7253...)
```

### Resolution

**Q1 — Same tokenizer?** YES. Serialization difference only. The INT4 MLX file stores BPE merges as JSON arrays (`["Ġ","Ġ"]`); the FP16 HuggingFace file stores them as space-delimited strings (`"Ġ Ġ"`). No content difference.

**Q2 — Why identical?**
```
Vocab:                  151,643 entries — identical
Merges (normalized):    151,387 rules   — identical (every index matches after normalization)
BPE behavior:           identical — same token sequence for any input string
fp16_norm == int4_norm: True
vocab dicts equal:      True
```

**Q3 — Was audit under sha256:c0382117…?** NO — original audit used sha256:3fd169731d...

**Q4 — Re-run under sha256:c0382117…:**
```
Tokenizer:                    sha256:c0382117...
Total unique C-role tokens:   216
Round-trip failures:          0
Cross-chain C violations:     0  (j ≥ 0.40 threshold — zero unintended near-miss pairs)
Near-miss pairs 24/24:        j ≥ 0.40 — PASS
  ZJMOL/ZJMZY j=0.50, DBKSD/IMKSD j=0.50, MRZSP/VDZSP j=0.50,
  YYQGH/PJQGH j=0.50, BAGCR/BAGQI j=0.40 (minimum)
Result:                       PASS — identical to original audit result
```

**Gate 0.5 status:** PASS — unambiguously under the run tokenizer sha256:c0382117...

Full reconciliation note: `tier0-run/TOKENIZER-HASH-RECONCILIATION-TWOHOP-L1.md`
