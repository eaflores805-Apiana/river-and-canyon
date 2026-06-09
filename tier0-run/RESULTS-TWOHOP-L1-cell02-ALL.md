# Run Summary — Two-Hop Level 1 Cell02
## Standard Return Packet — Constructibility Run

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Status:** COMPLETE — AWAITING TEAM LEAD DISPOSITION
**Format:** Standard Return Packet Policy (Team Lead memo 2026-06-08)
**Per:** Manager memo — "FP16 Cell02 Execution Authorization — Two-Hop Level 1" 2026-06-08

---

## 1. Run identity

```
cell_id:          twohop_l1_cell02
run_id:           RESULTS-TWOHOP-L1-cell02-1780933041
date:             2026-06-08
model:            Qwen/Qwen2.5-3B-Instruct
precision:        FP16
model_snapshot:   aa8e72537993ba99e69dfaafa59ed015b17504d1
n_items:          24
n_queries:        96 (24 items × 4 query types)
axis_under_test:  position / ordering
design:           all-C_target-last — T-hop2 at context position 6, all 24 items
                  decoy_chain_2 hop2 at position 7 (Gate 5 mechanically forced)
rng_seed:         20260610
authorized_scope: FP16 constructibility run, Cell02 only, locked item set
purpose:          constructibility mapping only — Claim B floor-mapping
```

---

## 2. Authorization boundary

```
Authorized:
  Load FP16 model (Qwen/Qwen2.5-3B-Instruct)
  Run locked Cell02 item set through locked runner
  Score outputs with locked scorer
  Produce raw and scored outputs
  Produce Run_Summary
  Update EXPERIMENT_LOG

Not authorized:
  INT8
  INT4
  7B
  confirmation pass
  cell redesign
  prompt repair
  threshold changes
  scorer changes
  runner changes after seeing outputs
  Track B
  Claim C testing
  mechanism claims
  seam claims
  compression claims
```

---

## 3. Provenance match table

Expected hashes from CELL02-PREP-LOCK-PACKET-TWOHOP-L1.md. Observed hashes from run artifact provenance block (RESULTS-TWOHOP-L1-cell02-1780933041.json).

```
Artifact           Expected hash                                                              Observed hash                                                              Status
Cell02 JSON        sha256:b81d471616f8830fba76b99b9e1b04e23d3e4af13284c27627481ae89528f4c9   sha256:b81d471616f8830fba76b99b9e1b04e23d3e4af13284c27627481ae89528f4c9   MATCH
Runner             sha256:d14f6424340699785a8bdc12a8bb6c2b7cb33f96069de49e1fcb945bbc12b0fa   sha256:d14f6424340699785a8bdc12a8bb6c2b7cb33f96069de49e1fcb945bbc12b0fa   MATCH
Prompt template    sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e   sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e   MATCH
Scorer             sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd   sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd   MATCH
Validator          sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b   sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b   MATCH
Tokenizer          sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539   sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539   MATCH
Model snapshot     aa8e72537993ba99e69dfaafa59ed015b17504d1                                  aa8e72537993ba99e69dfaafa59ed015b17504d1                                  MATCH
```

**All 7 artifacts: MATCH. No provenance deviations. Interpretation may proceed.**

---

## 4. Output artifacts

```
raw_output_json:    RESULTS-TWOHOP-L1-cell02-1780933041.json
raw_output_hash:    sha256:47b5eaa9b954645ca2572fe20873a0255776f60f29b0a544d8c350dcddc181ca
scored_output_json: RESULTS-TWOHOP-L1-cell02-1780933041.json
scored_output_hash: sha256:47b5eaa9b954645ca2572fe20873a0255776f60f29b0a544d8c350dcddc181ca

Note: raw output and scored output are the same artifact.
Scoring is performed inline by the runner; the single JSON contains both
raw_output and all scored fields (failure_class, is_correct, returned_token,
returned_role, scaffold_class, format_class, dummy_baselines).

run_summary:            RESULTS-TWOHOP-L1-cell02-ALL.md (this document)
experiment_log_entry:   EXPERIMENT_LOG.md (updated 2026-06-08, Two-Hop L1 Cell02 section)
```

---

## 5. Gate table

```
Gate    Name                        Status     Metric / threshold / result
──────────────────────────────────────────────────────────────────────────────
Gate 0  Manifest schema             PASS       validate_manifest: 24/24
                                               threshold: 24/24
                                               notes: carried from prep lock packet

Gate 0.5 Token construction audit  PASS       lev violations: 0
                                               trig violations: 0
                                               BPE-j violations (C-role): 0
                                               declared near-miss pairs j ≥ 0.40: 24/24
                                               tokenizer: sha256:c0382117...
                                               notes: carried from prep lock packet

★ FIRST FAILED GATE:
Gate 1  Format adherence            FAIL       hop1 FORMAT_PASS:  24/24 = 1.000  PASS
                                               hop2 FORMAT_PASS:  23/24 = 0.958  FAIL ←
                                               composite FORMAT_PASS: 24/24 = 1.000  PASS
                                               neg_graph FORMAT_PASS: 24/24 = 1.000  PASS
                                               threshold: 1.000 per query type
                                               notes: 1 format_scaffold_failure on i08/hop2
                                                 raw output: 'ANSWER: ZBCDF maps to AJLAC.'
                                                 (sentence-level; model had correct answer;
                                                  isolated incident — all other 95 OK)

Gate 2  FP16 pass rate              FAIL       hop1:      9/24 = 0.375   FAIL  (diagnostic)
        (diagnostic — Gate 1        (diag.)    hop2:     23/24 = 0.958   PASS  (Gate 1 contam.)
         already failed)                       composite: 20/24 = 0.833   FAIL  (diagnostic)
                                               neg_graph:  0/24 = 0.000   N/A   (contract)
                                               threshold: ≥ 21/24 per query type
                                               notes: hop1 and composite independently fail
                                                 Gate 2. hop2 would pass Gate 2 but is
                                                 Gate 1-contaminated.

Gate 3  Operation fidelity          BLOCKED    stopped_short_rate:       0/24 = 0.000  PASS
        (diagnostic only)           (diag.)    shortcut_single_hop_rate: 0/24 = 0.000  PASS
                                               wrong_chain_routing_rate: 4/24 = 0.167  FAIL
                                               wrong_neighbor_rate:      0/24 = 0.000  PASS
                                               denominator: composite FORMAT_PASS = 24
                                               threshold: wrong_chain ≤ 3/24
                                               notes: wrong_chain_routing 4/24 exceeds ceiling;
                                                 would fail Gate 3 independently.
                                                 Blocked by Gate 1 / Gate 2.

Gate 4a Classifier reliability      BLOCKED    unique_assignment_rate: 1.000 (PASS — computed)
                                    (diag.)    UNCLASSIFIED_OFF_FRAME: 0/96 = 0.000 ≤ 0.05 PASS
                                               watch trigger (> 0.02): NOT TRIGGERED
                                               notes: all 96 outputs classified; taxonomy
                                                 exhaustive for this cell. Blocked by Gate 1/2.

Gate 4b Failure-class separability  BLOCKED    notes: requires Gate 2 PASS. Not computed.

Gate 5  Control adequacy            PASS*      max_det: 0/24 = 0.000 ≤ 9/24  PASS
                                               first_C = cd1 (pos 2) ≠ ct: CONFIRMED
                                               last_C  = cd2 (pos 7) ≠ ct: CONFIRMED
                                               Gate 2 composite (20) − max_det (0) = 20 ≥ 10 PASS
                                               neg_graph null_return: 0/24 = 0.000
                                               threshold: max_det ≤ 9/24
                                               notes: Gate 5 passes for current dummy set.
                                               * POSITIONAL-COVERAGE GAP (audit 2026-06-08):
                                                 ct is second-by-position (pos 6) for all 24 items.
                                                 always_return_second_C = always_return_ct = 24/24
                                                 composite — not tested by any current dummy.
                                                 If included, Gate 5 would FAIL for composite.
                                                 See CELL02-GATE5-POSITIONAL-DUMMY-AUDIT.md.

Gate 5.5 Baseline-stability confirm N/A        notes: Manager-authorized only. Not applicable
                                               to this constructibility run.

Gate 6  Stress eligibility          NOT        requires Gate 2 PASS on hop1, hop2, composite
                                    ELIGIBLE   notes: Gate 2 FAIL; cell is not stress-eligible.
                                               INT8 / INT4 / Track B not authorized.
```

---

## 6. Query-type score table

```
query_type       pass_count   fail_count   FORMAT_PASS   dominant_failure_classes
hop1             9            15           24/24         target_chain_wrong_neighbor (11),
                                                         non_context_return/NULL (3),
                                                         wrong_chain_selection (1)
hop2             23           1            23/24         format_scaffold_failure (1) — format only
composite        20           4            24/24         wrong_chain_selection (4)
negative_graph   0            24           24/24         wrong_chain_selection (23),
                                                         target_chain_wrong_neighbor (1)
```

---

## 7. Failure-class breakdown

Counts shown per query type. Denominator = 24 per query type (96 total).

```
Failure class                   hop1   hop2   composite   negative_graph   total
──────────────────────────────────────────────────────────────────────────────────
correct                         9      23     20          0                52
format_scaffold_failure         0      1      0           0                1
non_context_return              3      0      0           0                3
correct_chain_stopped_short     0      0      0           0                0
wrong_chain_selection           1      0      4           23               28
target_chain_wrong_neighbor     11     0      0           1                12
anchor_echo                     0      0      0           0                0
NULL / NO_LINK wrong return     0      0      0           0                0
UNCLASSIFIED / OFF-FRAME        0      0      0           0                0
──────────────────────────────────────────────────────────────────────────────────
total                           24     24     24          24               96
```

**Notes:**
- hop1 dominant failure: target_chain_wrong_neighbor (11/15 = 73% of hop1 failures)
  All 11 cases: returned ct (C_target, pos 6) instead of bt (B_target, pos 5)
- i08/hop2 FSF: isolated sentence-format response; model semantically correct
- negative_graph i20: target_chain_wrong_neighbor (returned anchor_A = ZBATA, not a C-endpoint)
- UNCLASSIFIED: 0/96 — taxonomy exhaustive for this cell

---

## 8. Axis-specific diagnostics

### Axis A — Contract / abstention behavior

```
status:           FRAGILE (same as Cell01)
evidence:         negative_graph correct NULL: 0/24 (was 2/24 in Cell01)
                  Endpoint return: 24/24 (23 wrong_chain + 1 wrong_neighbor)
label_confidence: HIGH — 0/24 is a clean floor; no ambiguity in classification
ambiguity_note:   Ordering change had no effect on NULL-calibration.
                  The 2/24 Cell01 correct NULLs were in C_target-first (absent here),
                  but that is insufficient evidence that ordering drives abstention.
                  Axis A fragility is a persistent structural feature, not ordering-dependent.
```

### Axis B — Content / distractor / chain-selection behavior

```
status:           STABLE FRAGILITY (same rate as Cell01)
evidence:         composite wrong_chain_selection: 4/24 (items i01, i12, i15, i21)
                  wrong_chain_routing_rate: 4/24 (Gate 3 ceiling 3/24 — would fail)
                  hop2 correct: 23/24 — no selection pressure; target chain at pos 6 reliable
                  Cell01 composite wrong_chain: also 4/24 (different items)
label_confidence: HIGH for i01, i15, i21 — clean wrong-chain endpoint returns
                  MEDIUM for i12: returned UDNSZ (= ct of a rotated item);
                  difficult to attribute cleanly to distractor pressure vs. endpoint attraction
ambiguity_note:   Axis B fragility rate is identical across cells (4/24 both).
                  Independent of the ordering change. Suggests Axis B is not the
                  load-bearing variable for ordering effects.
                  The 4/24 composite wrong_chain may be a structural floor for this
                  token pool size and distractor geometry.
```

### Axis C — Position / ordering behavior

```
status:           HYPOTHESIS NOT SUPPORTED
evidence:         hop1: 9/24 under all-C_target-last
                  Cell01 overall hop1: 14/24 — Cell02 is a regression
                  Cell01 C_target-last subgroup: 8/8 — not reproduced at n=24
                  Dominant new failure: target_chain_wrong_neighbor (11/15 hop1 failures)
                  All 11 cases: model returned ct (pos 6) for hop1 (expects bt at pos 5)
                  ct-anchoring observed; cue unresolved
label_confidence: HIGH for target_chain_wrong_neighbor classification —
                  returned tokens confirmed as ct from item metadata
                  HIGH for the hypothesis result (NOT SUPPORTED)
ambiguity_note:   Four confounded candidate cues for ct-anchoring in Cell02:
                  (a) Adjacency / proximity: hop1 at pos 5, hop2 at pos 6 — adjacent
                  (b) Absolute position: ct fixed at pos 6 for all 24 items
                  (c) C-rank slot: ct fixed as second_C for all 24 items
                      (Gate 5 audit: always_return_second_C = 24/24 composite — not tested)
                  (d) Answer-domain salience: ct is the composite correct answer; may be
                      structurally more answer-shaped than cd1 or cd2 independent of position
                  All four were simultaneously true in Cell02. "Adjacency-driven" is retired.
                  Safe label: ct-anchoring; cue unresolved
                  Cell01 C_target-last subgroup 8/8 result is established as
                  item-specific or interaction-dependent, not purely ordering-causal.
```

---

## 8a. Comparison-integrity caveat

```
Cell02 content metrics are diagnostic downstream of a Gate 1 failure.
Comparisons to Cell01 should be read with that caveat.

Construction-integrity check (CELL02-HOP2-FSF-INSPECTION-TWOHOP-L1.md, 2026-06-08):
  The single hop2 FSF (item i08) has been classified as FORMAT_COMPLIANCE_LOSS
  (isolated, orthogonal format-only event; model demonstrably knew the answer).
  No construction defect was found. Gate 0.5 is confirmed valid.
  The "position/ordering NOT SUPPORTED" conclusion and the ct-anchoring / cue-unresolved
  finding (11/15 hop1 wrong_neighbor) are unaffected.
  This caveat is preserved per filing instructions regardless of classification outcome.
```

---

## 9. Prior-cell comparison

```
Compared against:        Cell01 (twohop_l1_cell01, FP16, sha256:6de8b67c...)
Hypothesis under test:   Position/ordering is the primary causal factor for
                         Cell01 hop1 fragility (all-C_target-last should restore hop1)

Expected movement:
  hop1:      improve from 14/24 → near 24/24
  hop2:      maintain ≈ 24/24
  composite: maintain or improve from 18/24
  neg_graph: maintain near-0 (not ordering-sensitive)

Observed movement:
  hop1:      9/24  ← regression from 14/24 (−5)
  hop2:      23/24 ← near-maintained (1 FSF)
  composite: 20/24 ← slight improvement from 18/24 (+2)
  neg_graph: 0/24  ← no improvement from near-0

Interpretation:
  The position/ordering hypothesis is NOT SUPPORTED.
  This specific all-C_target-last manipulation did not support the
  position/ordering hypothesis as a sufficient explanation of Cell01.
  The Cell01 C_target-last subgroup success (8/8) appears item-specific
  or interaction-dependent rather than purely ordering-causal.
  Moving all items to C_target-last did not restore the hop1 floor.
  This does not establish that position is irrelevant — it establishes
  that this manipulation was not a sufficient intervention.
```

Per-group cross-cell detail:

```
Subgroup                    hop1     hop2     composite
Cell01 C_target-first (8)   0/8      8/8      4/8
Cell01 C_target-middle (8)  6/8      8/8      7/8
Cell01 C_target-last (8)    8/8      8/8      7/8
Cell02 all-C_target-last    9/24     23/24    20/24
```

---

## 10. Branch routing

```
first_failed_gate:    Gate 1 — format adherence
                      hop2 FORMAT_PASS 23/24 < 1.000
                      (1 format_scaffold_failure, item i08, isolated)
branch:               constructibility-boundary result — Claim B dirty cell
                      second data point with distinct failure profile from Cell01
stress_eligibility:   NOT ELIGIBLE (Gate 2 FAIL on hop1 and composite)
Track B:              BLOCKED
Claim C:              NOT TESTED
```

---

## 11. Safe interpretation

Under this locked construction (3-chain 7-fact all-C_target-last, Qwen2.5-3B-Instruct FP16, n=24), the cell did not reach the constructibility floor. Gate 1 failed on hop2 (1 FORMAT_COMPLIANCE_LOSS event, item i08) and Gate 2 failed on both hop1 (9/24) and composite (20/24). The observed failure pattern was dominated by target_chain_wrong_neighbor on hop1 (11/15 failures), in which the model returned ct rather than bt. This pattern is labeled ct-anchoring; the cue is unresolved across four candidate dimensions — adjacency/proximity, absolute position, C-rank slot, and answer-domain salience — all of which were simultaneously fixed for ct in Cell02. Cell02 strengthens the candidate convergence read that the Two-Hop Level 1 floor may involve recurring salient endpoint-return behavior, but it does not establish which cue drives that behavior. This is a Claim B mapping point only — a second dirty-cell constructibility-boundary data point with a distinct failure profile from Cell01.

---

## 12. Forbidden interpretations

```
No stress result.
No INT8 / INT4 result unless specifically authorized.
No seam result.
No compression result.
No mechanism claim.
No general model-capability claim.
No Claim C test unless Track B was explicitly authorized.
No claim that position/ordering is confirmed as causal.
No claim that Cell01 C_target-last group (8/8) generalizes to n=24.
No claim that adjacency is the identified or confirmed cue for ct-anchoring.
  The cue is unresolved across adjacency, absolute position, C-rank, and answer-domain salience.
No claim that composite (20/24) excludes the always_return_second_C / always_return_ct
  positional shortcut. Gate 5 did not test this shortcut. Composite result is shortcut-exposed.
```

---

## 13. Recommended next action

```
Claim B Map Entry filed: CLAIM-B-MAP-ENTRY-TWOHOP-L1-CELL02.md — 2026-06-08

Pending Team Lead disposition on Cell02 map entry.

No further construction authorized pending Manager decision on next axis.
```

---

## 14. No-extra-run statement

```
No additional model inference was performed beyond the authorized scope.
FP16 only. Cell02 item set only. Locked runner only.
No rerun. No confirmation pass. No INT8. No INT4. No 7B. No Track B.
```

---

## Appendix A — Per-item failure table

```
Item    hop1                            hop2            composite               neg_graph
i01     non_context_return (NULL)       correct         wrong_chain (VBLTH)     wrong_chain (VBLTH)
i02     target_chain_wrong_neigh (ct)   correct         correct                 wrong_chain (EPXRX)
i03     correct                         correct         correct                 wrong_chain (PVMEO)
i04     target_chain_wrong_neigh (ct)   correct         correct                 wrong_chain (MLIMZ)
i05     correct                         correct         correct                 wrong_chain (SYPKQ)
i06     target_chain_wrong_neigh (ct)   correct         correct                 wrong_chain (DAAXS)
i07     target_chain_wrong_neigh (ct)   correct         correct                 wrong_chain (OFWGM)
i08     correct                         FSF (sentence)  correct                 wrong_chain (PBKNW)
i09     correct                         correct         correct                 wrong_chain (RRWRO)
i10     wrong_chain (VHPZM)             correct         correct                 wrong_chain (VHPZM)
i11     target_chain_wrong_neigh (ct)   correct         correct                 wrong_chain (SKMNK)
i12     target_chain_wrong_neigh (ct)   correct         wrong_chain (UDNSZ)     wrong_chain (UDNSZ)
i13     target_chain_wrong_neigh (ct)   correct         correct                 wrong_chain (AWILF)
i14     correct                         correct         correct                 wrong_chain (IXENM)
i15     non_context_return (NULL)       correct         wrong_chain (NTELO)     wrong_chain (NTELO)
i16     correct                         correct         correct                 wrong_chain (AJLAC)
i17     target_chain_wrong_neigh (ct)   correct         correct                 wrong_chain (LVQLN)
i18     target_chain_wrong_neigh (ct)   correct         correct                 wrong_chain (EQNPV)
i19     non_context_return (NULL)       correct         correct                 wrong_chain (WJPGX)
i20     correct                         correct         correct                 wrong_neigh (ZBATA)
i21     correct                         correct         wrong_chain (FJUDM)     wrong_chain (FJUDM)
i22     target_chain_wrong_neigh (ct)   correct         correct                 wrong_chain (FLZAC)
i23     correct                         correct         correct                 wrong_chain (SGEJJ)
i24     target_chain_wrong_neigh (ct)   correct         correct                 wrong_chain (DVRRO)
```

---

## Appendix B — Authorization chain

```
Cell02 FP16 execution authorized by:
  Manager memo — "FP16 Cell02 Execution Authorization — Two-Hop Level 1" 2026-06-08
  Preparation Lock Packet reviewed: CELL02-PREP-LOCK-PACKET-TWOHOP-L1.md
  Axis authorization: position / ordering (one-axis, Option A)
  Standard Return Packet Policy per: Team Lead memo 2026-06-08
```

---

— CS Engineer, 2026-06-08
