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
| pure_last_position | answerable | 80 | 24 | 0.3000 | 25 | discriminative |
| pure_last_position | null | 16 | 0 | 0.0000 | 12 | discriminative |
| salient_endpoint | answerable | 80 | 13 | 0.1625 | 24 | discriminative |
| salient_endpoint | null | 16 | 0 | 0.0000 | 11 | discriminative |
| recency_excluding_target | answerable | 80 | 12 | 0.1500 | 26 | discriminative |
| recency_excluding_target | null | 16 | 0 | 0.0000 | 12 | discriminative |
| prefix_neighbor_confusion | answerable | 80 | 12 | 0.1500 | 9 | discriminative |
| prefix_neighbor_confusion | null | 16 | 0 | 0.0000 | 1 | discriminative |
| copy_completion | answerable | 80 | 0 | 0.0000 | 67 | - |
| copy_completion | null | 16 | 0 | 0.0000 | 16 | - |

**Union envelope score (answerable):** 0.6125
**Envelope cap (declared):** 0.8000
**Room below envelope cap:** 0.1875

## T3 — Ideal-Witness / Pass-Region Checklist (6 criteria, locked bounds)

**Ideal witness in pass region:** True

| Criterion | Stratum | Comparison | Floor/Ceiling | Is Floor | Disposition |
|---|---|---|---|---|---|
| null_abstention_floor_unmet | null | ci_upper_bound | 0.75 | True | pass |
| answerable_abstention_ceiling_exceeded | answerable | ci_lower_bound | 0.2 | False | pass |
| accuracy_indistinguishable_from_token_prior | answerable | difference_interval | 0.1 | True | pass |
| accuracy_indistinguishable_from_declared_policy_envelope | answerable | difference_interval | 0.1 | True | pass |
| insufficient_measurement_headroom | answerable | ci_upper_bound | 0.15 | True | pass |
| strict_content_gap_instability | answerable | difference_interval | 0.3 | False | pass |

## Full-instrument oracle validation (Team Lead §5; v0.2 label-set matching)

**Oracle cases overall_matched:** 0/0

| Case ID | Type | Expected | Actual | Attached | Required | Required Absent | Matched |
|---|---|---|---|---|---|---|---|

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
## Non-authorizations

No execution authorized. No new sweep_id. No model runs.
No candidate selection. No threshold work. No certification
evaluation. No D3/D4/D5 implication. LOCK-RECORD remains PENDING.

— CS Engineer, 2026-06-11

## D4-B Candidate Run (Manager-authorized TP-ACTIVE pilot)



- candidate sweep_id: `lane1a-prime-d4b-cand-20260611-220303-ueitv3`

- tp sweep_id: `lane1a-prime-d4b-tp-20260611-220303-bt29ky`

- model: Qwen2.5-3B-Instruct (bf16)

- model_snapshot_hash: `sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20`

- mlx_lm version: 0.31.3 (Option A pin substitution carried from D4-A)



### TP banner (ACTIVE — Manager Q4 authorized)



- tp_criterion_status: ACTIVE

- tp_inactivity_authority: n/a (Manager authorized TP generations for this run)

- tp_generation_status: RUN (authorized)

- tp_elimination_labels_enabled: True



### Candidate per-stratum measurements



- answerable correct: 80/80 (1.0000)

- answerable abstained: 0/80

- null abstained: 16/16

- candidate parse failures: 0/96 (void_rate 0.0000; budget 0.05)



### TP control (no-bindings shell) measurements



- TP control correct: 1/80 (0.0125)

- TP control abstained: 38/80

- TP control parse failures: 0/96 (void_rate 0.0000; budget 0.05)



### Candidate vs TP comparison



- candidate accuracy: 1.0000

- TP control accuracy: 0.0125

- point difference: 0.9875

- Newcombe-Wilson CI on difference: [0.9159, 0.9978]

- locked TP margin: 0.10

- TP criterion fires (CI upper < 0.10): False



### Final candidate outcome (six active criteria)



- attached_labels: (none)

- outcome: **NOT_RULED_OUT**



### Non-claim block (verbatim)



> D4-B is an instrument-use step, not a capability claim. Even if D4-B returns NOT_RULED_OUT under six active criteria, it remains instrument use, not a capability claim. The instrument may rule out; it may not rule in. Passing the declared battery is reportable only as "not explained by the declared shortcut battery," never as "not shortcut-driven." We have improved the ruler; we are only beginning to touch the territory.



— CS Engineer, 2026-06-11