# Run-2 Retention Block (E11 / PH5-5)

```text
SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
RUN-2 SUPERSEDED -- RETAINED PER E11 DISCIPLINE
NO MODEL INVOKED · NO SWEEP_ID CREATED · NO SWEEP EXECUTION
```

*CS Engineer, 2026-06-11.*

## Status

Run-2 of the corrective Phase 5 pipeline is **superseded**, **retained**,
and **not erased**. Run-3 (post-lock) is the actually-authorized
execution and is gated behind the PH5-1 joint lock event +
Team-Lead-PASS filter.

## pilot_iteration_count

**3** (run-1 superseded; run-2 superseded; run-3 to be authorized at the
filed and TL-PASSED PH5-1 joint lock event).

## reason_for_re-pilot (run-2 → run-3)

Run-2 was executed under the provisional T3 bounds and 4-stratum recipe
before the NS bounds-side review was reconciled at the joint PH5-1 lock
event. Per TL §14 of the joint-lock-event-ordering memo, the corrective
re-run remained gated; the run-2 execution was therefore premature.

CS owns this. The honest disclosure was filed in
`CS-CO-SIGNATURE-T3-BOUNDS-AND-ORC10-v0.1.md` §11.

## changed_fields_between_pilots (run-2 vs run-3)

### T3 bounds (provisional → locked)

| criterion | run-2 value | run-3 value | change |
|---|---|---|---|
| null_abstention_floor_unmet | 0.50 | 0.75 | floor raised; severity calibration from NULL contract |
| answerable_abstention_ceiling_exceeded | 0.50 | 0.20 | ceiling lowered; symmetric severity on answerable contract |
| accuracy_indistinguishable_from_token_prior | 0.10 | 0.10 | unchanged |
| accuracy_indistinguishable_from_declared_policy_envelope | 0.10 | 0.10 | unchanged |
| insufficient_measurement_headroom (bound) | 0.20 | 0.15 | bound lowered; cap-tautology eliminated |
| insufficient_measurement_headroom (source) | candidate attempted-proportion | (1 − envelope) | semantic corrected; envelope-derived per NS rationale |
| strict_content_gap_instability | 0.20 | 0.30 | bound raised; format-cliff-class threshold |

### Stratified recipe (4-stratum → 5-stratum disjoint)

| stratum | run-2 count | run-3 count | change |
|---|---|---|---|
| gold_at_last_position | 20 | 12 | reduced; per intended-rate band [0.06, 0.20] |
| gold_at_salient_endpoint | 20 | 12 | reduced; same |
| gold_in_prefix_neighborhood | 20 | 12 | reduced; same |
| gold_recency_adjacent | (absent) | 12 | NEW stratum; pins recency_excluding_target hit rate |
| no_structural_feature / at_none_of_these | 20 | 32 | renamed and expanded |

### Oracle verdict table (v1 → v2)

| change | row | detail |
|---|---|---|
| ORC-08 permitted_co_labels | universal_abstainer | removed `insufficient_measurement_headroom` (TL §4 cleanup) |

### Implementation surface

| change | location |
|---|---|
| HEAD measurement source | `validation._build_measurements_for_predictions` |
| ManifestRecipe stratification | `validation.ManifestRecipe` (5 fields, sum check) |
| recency_adjacent stratum constructor | `validation.construct_pilot_manifests` (new branch) |
| Pre-flight artifact hashes | `validation/run_validation.py` (three new sha256s) |
| Tests | `tests/test_validation.py` (new fields; locked-schedule default test) |

## failed_pilot_records_retained

All eight run-2 output artifacts are preserved in this directory:

- `pilot_manifests_L01.json`
- `final_manifests_L01.json`
- `oracle_validation_results.json`
- `t1_report.json`
- `t3_report.json`
- `t4_report.json`
- `instrument_validation_report.md`
- `execution_ledger.json`

No artifact is deleted or modified. The IVR for run-2 records 12/12
overall_matched under provisional bounds — a state that was internally
consistent with the artifacts that produced it but is **not the locked
state** under PH5-1.

## Relationship to run-1 retention

`validation/superseded_run-1/` and `validation/superseded_run-2/` stand
side by side. Run-1 retention reasons (reduced criteria; unlocked
verdict table; unstratified recipe; A6 drift exceedance) and run-2
retention reason (executed under provisional bounds before lock-event
reconciliation) are distinct and cumulative. Both retention blocks are
referenced from the run-3 IVR §D.6 pilot iteration log when run-3
executes.

## Non-claim (verbatim)

This retention block records pilot iteration history under the E11 /
PH5-5 discipline. It does not constitute corrective re-run authorization,
candidate evidence, capability evidence, certification evidence, or
threshold support. LOCK-RECORD remains PENDING.

— CS Engineer, 2026-06-11
