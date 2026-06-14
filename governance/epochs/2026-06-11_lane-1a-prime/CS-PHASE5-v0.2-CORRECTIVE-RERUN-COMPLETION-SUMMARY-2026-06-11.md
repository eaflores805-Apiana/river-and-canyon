# CS — Phase 5 v0.2 Corrective Re-Run Completion Summary

```text
SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 PHASE 5 v0.2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION
NO CANDIDATE/MODEL OUTPUTS PRODUCED
```

*CS Engineer, 2026-06-11. Closes the corrective Phase 5 re-run authorized
under Team Lead §9. The run-1 pilot was retained, not erased, per E11 /
PH5-5. All five corrective items (PH5-1 joint lock event, PH5-2 label-set
match predicate, PH5-3 stratified recipe, PH5-4 pre-flight hash
precondition, PH5-5 run-1 retention block) are implemented and verified.
LOCK-RECORD remains PENDING. No D3 implication.*

---

## §1. Lock-event artifacts (PH5-1; CS+NS+TL co-signed)

| Artifact | sha256 |
|---|---|
| validation/ORACLE_VERDICT_TABLE.json | `add5f707760bd18f18e967583d86d883254a3df73207dbfcd4c3a2ec0a1b0891` |
| validation/T3_BOUNDS_DECLARATION.json | `78c8bd0cc3c1da3b92bdb834dd9411835793a40b57888c0c4a0d48f284d88258` |
| validation/STRATIFIED_RECIPE_SCHEDULE.json | `ef8b072445c5bd933cf43ab9d345518adb7c6d424ac000208acdc5b542d9459d` |

Lock-event memo (governance): `PH5-1-JOINT-LOCK-EVENT-RECORD-2026-06-11.md`
(sha256 `f365fa8c2218460f921ec8f9a0509a27132acbffa23f9f1c44953d83f0280523`).

## §2. Run-2 output artifacts (current; LOCK-RECORD PENDING)

| Artifact | sha256 |
|---|---|
| validation/pilot_manifests_L01.json | `ddb2401531263464ea70d8517d05b31f660efeca6cf164d894fc1c8a71bed730` |
| validation/final_manifests_L01.json | `ddb2401531263464ea70d8517d05b31f660efeca6cf164d894fc1c8a71bed730` |
| validation/oracle_validation_results.json | `8e3761de2b4fd8c75ff6fe930de4facc711dab7fd890be4e88892e41d4abab41` |
| validation/t1_report.json | `41ddf8fba1b2aa1515844d5b8b3062aa0772d45e7d34e56181e7a3ae04d82304` |
| validation/t3_report.json | `e12a4893c31d14dd1febe6c3f50e9b9be9c9b2c5f3dee37ad788ba103074cd7c` |
| validation/t4_report.json | `104ff3d64a05f0228e53a17ae404586bf421716ad5503ed0c62345dca4a44782` |
| validation/instrument_validation_report.md | `1af478dea6e3fa2b377a1081152893b56c7d5d45e0fbb4d4420d8a3a94181547` |
| validation/execution_ledger.json | `b625627bde42e0fb9be3220c61a848a2e85c90cf6e9cc0e2be4ee354eda5315c` |

**Note (PH5-3 verification):** the pilot and final manifests have identical
sha256s. Under the stratified recipe + identical-seed protocol, A6 drift
is zero by construction; the byte-identical hashes confirm the property.

## §3. Source-of-truth implementation (PH5-2/3/4)

| File | sha256 |
|---|---|
| lane1a_prime/oracle_cases.py | `04c5aad868bb7a32f01f8b6e24a0ea791de679bd2bef248fc00ce03f536f5b71` |
| lane1a_prime/validation.py | `907e228fd001300d6fe723cb763d2b57d02e2fc8ca11498d0d99f275be22bc52` |
| lane1a_prime/analysis.py | `3f83ac57d59f30818d12888ce0d364c78d3226475ab1ca4dd098c0cc99c55969` |
| validation/run_validation.py | `875916eac0749ebd5b79431ce47d56902855e3fdf80d7a6d98368a41388e12aa` |
| tests/test_validation.py | `b13a64d2be18707a2332138c74c04ba1e7ed1967bc55cab6a80caa69264a08c3` |

## §4. Run-1 retention block (PH5-5; E11 discipline)

| Artifact | sha256 |
|---|---|
| validation/superseded_run-1/RUN-1-RETENTION.md | `0d94dc385227dbdd93369595fc9afe439ed0923154406008016d733f1c58ec88` |

Retained files (run-1 outputs): `pilot_manifests_L01.json`,
`final_manifests_L01.json`, `oracle_validation_results.json`,
`t1_report.json`, `t3_report.json`, `t4_report.json`,
`instrument_validation_report.md`, `execution_ledger.json` — all under
`validation/superseded_run-1/`.

`pilot_iteration_count`: 2 · `failed_pilot_records_retained`: yes
(superseded_run-1/) · `reason_for_each_repilot`: enumerated in
RUN-1-RETENTION.md (reduced-criteria run; unlocked verdict table;
unstratified recipe; A6 drift exceedance) · `changed_fields_between_pilots`:
enumerated in IVR §E11 block.

## §5. Test suite status

`pytest experiments/2026-06-11_lane-1a-prime/tests/`: **243 passed**.

Coverage of corrective items:
- PH5-1 (joint lock event): `test_t3_bounds_declaration_loads_from_disk`,
  `test_oracle_verdict_table_loads_from_disk` (analysis-side);
  schema tests confirm the three lock-event artifacts parse.
- PH5-2 (label-set match predicate): `test_match_oracle_verdict_*`
  (5 tests covering pass, outcome mismatch, required-missing,
  required-absent-present, unexpected-label).
- PH5-3 (stratified recipe): `test_construct_pilot_manifests_*`
  (deterministic; default 96 records; stratum split 80/16;
  schema-conformant; pilot==final under same seed;
  ManifestRecipe rejects sum mismatch).
- PH5-4 (pre-flight refusal): wired into `run_full_instrument_oracle_validation`;
  exercised in `validation/run_validation.py` (stdout: "PH5-4 pre-flight:
  PASSED").
- PH5-5 (retention block): `test_assemble_validation_report_includes_retention_block`.

## §6. A6 drift corrected results (under 0.05 tolerance)

| Component | Drift | Within 0.05? |
|---|---|---|
| pure_last_position | 0.0000 | ✓ |
| salient_endpoint | 0.0000 | ✓ |
| recency_excluding_target | 0.0000 | ✓ |
| prefix_neighbor_confusion | 0.0000 | ✓ |
| union envelope | 0.0000 | ✓ |

A6 overall: **PASS** (no flagged drift).

## §7. Oracle expected-vs-actual table (PH5-2 label-set matching)

**Overall:** 12/12 cases `overall_matched`.

All four label-set clauses pass on all 12 cases:
- `outcome_matched`: 12/12
- `required_labels_present`: 12/12
- `required_absent_labels_absent`: 12/12
- `only_required_or_permitted_attached`: 12/12

Full table per case appears in
`validation/instrument_validation_report.md` §"Full-instrument oracle
validation" (12 rows, 8 columns per case).

## §8. T1 update (battery degeneracy audit)

- 5 policies × 2 strata; all answerable rows discriminative
  (point estimate ≤ envelope cap 0.80).
- Union envelope (answerable): 0.5375. Room below cap: 0.2625.
- A6 drift block: included with declared tolerance 0.05.
- Full table in IVR §T1 (10 rows).

## §9. T3 update (6-criterion checklist; locked bounds)

| Criterion | Comparison | Bound | Is-Floor | Disposition |
|---|---|---|---|---|
| null_abstention_floor_unmet | ci_upper_bound | 0.50 | True | pass |
| answerable_abstention_ceiling_exceeded | ci_lower_bound | 0.50 | False | pass |
| accuracy_indistinguishable_from_token_prior | difference_interval | 0.10 | True | pass |
| accuracy_indistinguishable_from_declared_policy_envelope | difference_interval | 0.10 | True | pass |
| insufficient_measurement_headroom | ci_upper_bound | 0.20 | True | pass |
| strict_content_gap_instability | difference_interval | 0.20 | False | pass |

Ideal witness in pass region: **True** (no criterion fires against
the ideal retriever).

## §10. T4 update (review-to-lock disposition table)

INH-1 / INH-2 / INH-3: incorporated (joint disposition, run-1).
PH5-1 / PH5-2 / PH5-3 / PH5-4 / PH5-5: all incorporated (this re-run).

## §11. IVR (Instrument Validation Report)

Section presence verified:
- D.1 T1 + A6 drift block ✓
- D.2 full-instrument oracle verdict table (8 fields per case) ✓
- D.3 (control conformance fields, per design declarations) ✓
- D.4 T3 checklist verdicts ✓
- D.5 T4 disposition table (INH + PH5 rows) ✓
- D.6 pilot iteration log ✓ (in E11 retention block)
- D.7 execution ledger ✓ (9 fields)
- D.8 report-level non-claim E16 verbatim ✓

LOCK-RECORD: **PENDING** (re-stated in IVR §Non-authorizations).

## §12. Run-1 supersession block

Run-1 outputs relocated to `validation/superseded_run-1/` with
`RUN-1-RETENTION.md` documenting:
- 4 distinct reasons for the re-pilot (reduced criteria; unlocked
  verdict table; unstratified recipe; A6 drift exceedance ≥ 0.05).
- 7 changed_fields between pilots (apply_criterion CI bound;
  DEFAULT_T3_CRITERIA; ORACLE_CASE_CATALOG; ManifestRecipe;
  run_validation tolerance; match_oracle_verdict predicate;
  verify_pre_flight_config refusal precondition).
- Retention discipline: run-1 retained, not erased.

## §13. Execution ledger

| Field | Value |
|---|---|
| no_model_invoked | CONFIRMED |
| no_sweep_id_created | CONFIRMED |
| no_sweep_execution | CONFIRMED |
| no_candidate_or_model_outputs | CONFIRMED |
| no_threshold_work | CONFIRMED |
| outputs_validation_only | "SYNTHETIC/DIAGNOSTIC — instrument validation artifacts only" |
| files_created | 8 (run-2 outputs in §2) |
| what_was_generated | manifests + oracle results + T1/T3/T4 reports + IVR |
| what_was_computed | per-policy hit rates; A6 drift; oracle label-set matching; T3 disposition under locked bounds |

## §14. Confirmations (Manager §11 items 6–9, plus PH5 items)

1. **No model invoked** during this corrective re-run.
2. **No sweep_id** created.
3. **No sweep execution** occurred.
4. **No candidate/model outputs** produced.
5. **PH5-1 lock event** completed: three artifacts hashed and the
   hashes vendored into run_validation.py for pre-flight verification.
6. **PH5-4 pre-flight precondition** verified at runtime: stdout
   confirms "PH5-4 pre-flight: PASSED (all lock-event artifact hashes
   match)".

---

## Non-authorizations (standing carry, restated)

This corrective re-run is instrument-validation work under the confirmed
model-free scope. It is not candidate evidence, not capability evidence,
not certification evidence, not threshold support. It does not authorize
D3 (candidate execution), D4 (per-rung outcomes), or D5 (cross-rung
synthesis). The LOCK-RECORD remains PENDING pending Team Lead review of
this packet.

— CS Engineer, 2026-06-11
