# Lane 1a' Instrument Validation Report — Phase 5 Corrective Re-Run

```text
SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 PHASE 5 v0.2 VALIDATION ARTIFACT (CORRECTIVE RE-RUN)
NO MODEL INVOKED -- NO SWEEP_ID CREATED -- NO SWEEP EXECUTION
```

## Report-level non-claim (E16)

> A Validation Report PASS means pre-lock adequacy on declared
> cases, pilots, and required checks only. It is not candidate
> evidence, not general field validity, not certification evidence,
> and not threshold support.

## Rung under validation: L01

## T1 — Battery Degeneracy Audit

| Policy | Stratum | N_eff | Correct | Accuracy | Distinct | Classification |
|---|---|---|---|---|---|---|
| pure_last_position | answerable | 80 | 22 | 0.2750 | 24 | discriminative |
| pure_last_position | null | 16 | 0 | 0.0000 | 11 | discriminative |
| salient_endpoint | answerable | 80 | 21 | 0.2625 | 26 | discriminative |
| salient_endpoint | null | 16 | 0 | 0.0000 | 10 | discriminative |
| recency_excluding_target | answerable | 80 | 2 | 0.0250 | 26 | discriminative |
| recency_excluding_target | null | 16 | 0 | 0.0000 | 11 | discriminative |
| prefix_neighbor_confusion | answerable | 80 | 0 | 0.0000 | 14 | discriminative |
| prefix_neighbor_confusion | null | 16 | 0 | 0.0000 | 1 | discriminative |
| copy_completion | answerable | 80 | 0 | 0.0000 | 66 | - |
| copy_completion | null | 16 | 0 | 0.0000 | 16 | - |

**Union envelope score (answerable):** 0.5375
**Envelope cap (declared):** 0.8000
**Room below envelope cap:** 0.2625

## A6 final-manifest re-verification (IS-7)

**Drift within tolerance:** True
**Envelope drift:** 0.0000
**Flagged drifts:** []

Per-policy drift:

  - pure_last_position: 0.0000
  - salient_endpoint: 0.0000
  - recency_excluding_target: 0.0000
  - prefix_neighbor_confusion: 0.0000

## T3 — Ideal-Witness / Pass-Region Checklist (6 criteria, locked bounds)

**Ideal witness in pass region:** True

| Criterion | Stratum | Comparison | Floor/Ceiling | Is Floor | Disposition |
|---|---|---|---|---|---|
| null_abstention_floor_unmet | null | ci_upper_bound | 0.5 | True | pass |
| answerable_abstention_ceiling_exceeded | answerable | ci_lower_bound | 0.5 | False | pass |
| accuracy_indistinguishable_from_token_prior | answerable | difference_interval | 0.1 | True | pass |
| accuracy_indistinguishable_from_declared_policy_envelope | answerable | difference_interval | 0.1 | True | pass |
| insufficient_measurement_headroom | answerable | ci_upper_bound | 0.2 | True | pass |
| strict_content_gap_instability | answerable | difference_interval | 0.2 | False | pass |

## Full-instrument oracle validation (Team Lead §5; v0.2 label-set matching)

**Oracle cases overall_matched:** 12/12

| Case ID | Type | Expected | Actual | Attached | Required | Required Absent | Matched |
|---|---|---|---|---|---|---|---|
| ORC-01 | ideal_retriever | not_ruled_out | not_ruled_out | - | - | accuracy_indistinguishable_from_token_prior,accuracy_indistinguishable_from_declared_policy_envelope,insufficient_measurement_headroom,strict_content_gap_instability,null_abstention_floor_unmet,answerable_abstention_ceiling_exceeded | PASS |
| ORC-02 | pure_last_position_shortcut | eliminated | eliminated | accuracy_indistinguishable_from_declared_policy_envelope,null_abstention_floor_unmet | accuracy_indistinguishable_from_declared_policy_envelope | - | PASS |
| ORC-03 | salient_endpoint_shortcut | eliminated | eliminated | accuracy_indistinguishable_from_declared_policy_envelope,null_abstention_floor_unmet | accuracy_indistinguishable_from_declared_policy_envelope | - | PASS |
| ORC-04 | recency_excluding_target_shortcut | eliminated | eliminated | accuracy_indistinguishable_from_declared_policy_envelope,accuracy_indistinguishable_from_token_prior,null_abstention_floor_unmet | accuracy_indistinguishable_from_declared_policy_envelope | - | PASS |
| ORC-05 | prefix_neighbor_confusion_shortcut | eliminated | eliminated | accuracy_indistinguishable_from_declared_policy_envelope,accuracy_indistinguishable_from_token_prior,null_abstention_floor_unmet | accuracy_indistinguishable_from_declared_policy_envelope | - | PASS |
| ORC-06 | token_prior_emitter | eliminated | eliminated | accuracy_indistinguishable_from_declared_policy_envelope,accuracy_indistinguishable_from_token_prior,null_abstention_floor_unmet | accuracy_indistinguishable_from_token_prior | - | PASS |
| ORC-07 | universal_answerer | eliminated | eliminated | accuracy_indistinguishable_from_declared_policy_envelope,accuracy_indistinguishable_from_token_prior,null_abstention_floor_unmet | null_abstention_floor_unmet | - | PASS |
| ORC-08 | universal_abstainer | eliminated | eliminated | accuracy_indistinguishable_from_declared_policy_envelope,accuracy_indistinguishable_from_token_prior,answerable_abstention_ceiling_exceeded,insufficient_measurement_headroom | answerable_abstention_ceiling_exceeded | - | PASS |
| ORC-09 | perfect_null_on_null_handler | not_ruled_out | not_ruled_out | - | - | accuracy_indistinguishable_from_token_prior,accuracy_indistinguishable_from_declared_policy_envelope,insufficient_measurement_headroom,strict_content_gap_instability,null_abstention_floor_unmet,answerable_abstention_ceiling_exceeded | PASS |
| ORC-10 | malformed_control_semantic_separation_guard | not_ruled_out | not_ruled_out | - | - | accuracy_indistinguishable_from_token_prior | PASS |
| ORC-11 | mixture_shortcut_heavy | eliminated | eliminated | accuracy_indistinguishable_from_declared_policy_envelope | accuracy_indistinguishable_from_declared_policy_envelope | null_abstention_floor_unmet,answerable_abstention_ceiling_exceeded | PASS |
| ORC-12 | mixture_retrieval_heavy | not_ruled_out | not_ruled_out | - | - | accuracy_indistinguishable_from_token_prior,null_abstention_floor_unmet,answerable_abstention_ceiling_exceeded | PASS |

## T4 — Review-to-Lock Disposition Table

| Item | Reviewer | Risk | Disposition | Owner | Status |
|---|---|---|---|---|---|
| INH-1 | inherited (v1 close-out) + joint disposition | semantics | incorporated | New Senior + CS | resolved |
| INH-2 | inherited (v1 close-out) + joint disposition | totality | incorporated | New Senior + CS | resolved |
| INH-3 | inherited (v1 close-out) + joint disposition | statistics | incorporated | New Senior + CS | resolved |
| PH5-1 | TL+NS+CS joint lock event | process | incorporated | NS + CS | resolved |
| PH5-2 | CS implementation | implementation | incorporated | CS | resolved |
| PH5-3 | CS implementation | implementation | incorporated | CS | resolved |
| PH5-4 | CS implementation | implementation | incorporated | CS | resolved |
| PH5-5 | CS implementation | implementation | incorporated | CS | resolved |

## E11 / PH5-5 Run-1 Retention Block

- **Superseded artifact pointer:** validation/superseded_run-1/
- **pilot_iteration_count:** 2 (run-1 superseded; run-2 current)
- **failed_pilot_records_retained:** validation/superseded_run-1/
- **reason_for_each_repilot:**
    - reduced-criteria run (CS used 2 of 6 criteria)
    - unlocked verdict table (NS oracle expected verdicts not co-signed)
    - unstratified recipe (per-draw random structural hit-rates)
    - A6 drift exceedance (pure_last_position 0.1375; envelope 0.10; both > 0.05)
- **changed_fields_between_pilots:**
    - apply_criterion CI bound (CI_LOWER -> CI_UPPER for floor; CI_UPPER -> CI_LOWER for ceiling)
    - DEFAULT_T3_CRITERIA (2 -> 6 criteria; loaded from T3_BOUNDS_DECLARATION.json)
    - ORACLE_CASE_CATALOG (9 -> 12 cases; ORC-10 semantic redefined; loaded from ORACLE_VERDICT_TABLE.json)
    - ManifestRecipe (added stratification fields; n_at_last/salient/prefix/none)
    - run_validation tolerance (0.30 -> 0.05; identical seed for pilot/final irrelevant after stratification)
    - match_oracle_verdict predicate (4-clause label-set match replaces verdict-only)
    - verify_pre_flight_config refusal precondition (PH5-4)

## Non-authorizations

No execution authorized. No new sweep_id. No model runs.
No candidate selection. No threshold work. No certification
evaluation. No D3/D4/D5 implication. LOCK-RECORD remains PENDING.

— CS Engineer, 2026-06-11