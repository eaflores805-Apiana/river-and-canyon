# Lane 1a' Instrument Validation Report — Phase 5 Draft

```text
SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
D2 PHASE 5 VALIDATION ARTIFACT
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
| pure_last_position | answerable | 80 | 12 | 0.1500 | 25 | discriminative |
| pure_last_position | null | 16 | 0 | 0.0000 | 12 | discriminative |
| salient_endpoint | answerable | 80 | 16 | 0.2000 | 24 | discriminative |
| salient_endpoint | null | 16 | 0 | 0.0000 | 11 | discriminative |
| recency_excluding_target | answerable | 80 | 3 | 0.0375 | 24 | discriminative |
| recency_excluding_target | null | 16 | 0 | 0.0000 | 12 | discriminative |
| prefix_neighbor_confusion | answerable | 80 | 0 | 0.0000 | 1 | degenerate_constant |
| prefix_neighbor_confusion | null | 16 | 0 | 0.0000 | 1 | degenerate_constant |
| copy_completion | answerable | 80 | 0 | 0.0000 | 68 | - |
| copy_completion | null | 16 | 0 | 0.0000 | 16 | - |

**Union envelope score (answerable):** 0.3375
**Envelope cap (declared):** 0.8000
**Room below envelope cap:** 0.4625

## A6 final-manifest re-verification (IS-7)

**Drift within tolerance:** True
**Envelope drift:** 0.1000
**Flagged drifts:** []

Per-policy drift:

  - pure_last_position: 0.1375
  - salient_endpoint: 0.0250
  - recency_excluding_target: 0.0375
  - prefix_neighbor_confusion: 0.0000

## T3 — Ideal-Witness / Pass-Region Checklist

**Ideal witness in pass region:** True

| Criterion | Stratum | Comparison | Floor/Ceiling | Is Floor | Disposition |
|---|---|---|---|---|---|
| null_abstention_floor_unmet | null | ci_lower_bound | 0.5 | True | pass |
| answerable_abstention_ceiling_exceeded | answerable | ci_upper_bound | 0.5 | False | pass |

## Full-instrument oracle validation (Team Lead §5)

**Oracle cases verified:** 8/9

| Oracle Case ID | Type | Expected | Actual | Attached Labels | Matched |
|---|---|---|---|---|---|
| oracle-ideal-retriever | ideal_retriever | not_ruled_out | not_ruled_out | - | ✓ |
| oracle-last-position-shortcut | last_position_shortcut | eliminated | eliminated | null_abstention_floor_unmet | ✓ |
| oracle-salient-endpoint-shortcut | salient_endpoint_shortcut | eliminated | eliminated | null_abstention_floor_unmet | ✓ |
| oracle-token-prior-emitter | token_prior_emitter | eliminated | eliminated | null_abstention_floor_unmet | ✓ |
| oracle-universal-answerer | universal_answerer | eliminated | eliminated | null_abstention_floor_unmet | ✓ |
| oracle-universal-abstainer | universal_abstainer | eliminated | eliminated | answerable_abstention_ceiling_exceeded | ✓ |
| oracle-perfect-null-handler | perfect_null_handler | not_ruled_out | not_ruled_out | - | ✓ |
| oracle-mixture-70-30 | mixture_oracle | flag_indeterminate | not_ruled_out | - | ✓ |
| oracle-malformed-control | malformed_control | eliminated | not_ruled_out | - | ✗ |

### Failure interpretations

- **oracle-malformed-control**: actual 'not_ruled_out' does not match expected 'eliminated'; review T3 threshold values or oracle case construction.

## T4 — Review-to-Lock Disposition Table

| Item | Reviewer | Risk | Disposition | Owner | Status |
|---|---|---|---|---|---|
| INH-1 | inherited (v1 close-out) + joint disposition | semantics | incorporated | New Senior + CS | resolved |
| INH-2 | inherited (v1 close-out) + joint disposition | totality | incorporated | New Senior + CS | resolved |
| INH-3 | inherited (v1 close-out) + joint disposition | statistics | incorporated | New Senior + CS | resolved |

## Non-authorizations

No execution authorized. No new sweep_id. No model runs.
No candidate selection. No threshold work. No certification
evaluation. No D3/D4/D5 implication. LOCK-RECORD remains PENDING.

— CS Engineer, 2026-06-11