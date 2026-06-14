# Phase 5 v0.2 Corrective Run-3 Completion Summary

```text
SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
CORRECTIVE PHASE 5 RUN-3 EXECUTION RECORD (UNDER PH5-1 PASS AUTHORIZATION)
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID CREATED · NO SWEEP EXECUTION
NO CANDIDATE/MODEL OUTPUTS PRODUCED · LOCK-RECORD PENDING
```

*CS Engineer, 2026-06-11. Filed under TL §4 corrective run-3
authorization (model-free D2 boundary). Reports the corrected
execution that satisfies the PH5-1 lock-event preconditions and the
TL §2 corrected expected constants. Includes honest disclosure of a
CS-detected construction bug in run-3 attempt 1 and its E11 retention
under `validation/superseded_run-3/`. No D3 implication.*

---

## §1. Commit SHA

```text
HEAD at the time of this filing: 5a12ee83ad60145ca8181ee1e00530dba5c5cdc6
(short: 5a12ee8) — the PH5-1 PASS commit.

A new commit will follow this memo, carrying:
  - corrected validation.py (prefix-neighbor stratum fix)
  - run-3 current outputs in validation/
  - validation/superseded_run-3/ with RUN-3-FIRST-ATTEMPT-RETENTION.md
  - this completion summary
```

(Commit SHA of the new HEAD is reported in the final delivery
enumeration at the end of this memo after the commit lands.)

## §2. File list

Current (canonical run-3) artifacts at
`experiments/2026-06-11_lane-1a-prime/validation/`:

```text
pilot_manifests_L01.json
final_manifests_L01.json
oracle_validation_results.json
t1_report.json
t3_report.json
t4_report.json
instrument_validation_report.md
execution_ledger.json
```

Lock-event artifacts (unchanged from PH5-1):

```text
ORACLE_VERDICT_TABLE.json
T3_BOUNDS_DECLARATION.json
STRATIFIED_RECIPE_SCHEDULE.json
```

Retention paths (E11/PH5-5; all three retained side by side):

```text
validation/superseded_run-1/  (run-1 outputs + RUN-1-RETENTION.md)
validation/superseded_run-2/  (run-2 outputs + RUN-2-RETENTION.md)
validation/superseded_run-3/  (run-3 attempt-1 outputs + RUN-3-FIRST-ATTEMPT-RETENTION.md)
```

## §3. sha256 hashes (run-3 current outputs)

| file | sha256 |
|---|---|
| `pilot_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| `final_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| `oracle_validation_results.json` | `37759f9acfffd6766d73cb0b6c5e66c0cd74e1608b424b41650a7f7c6ebefaad` |
| `t1_report.json` | `03ff6353c2fe38c2584312d1d1c08185a78799e15a01372df71a8ce085353a0f` |
| `t3_report.json` | `ca6e627cceaa9c70b47e343378d5a29d7511069801733e7190aea59280e843f4` |
| `t4_report.json` | `104ff3d64a05f0228e53a17ae404586bf421716ad5503ed0c62345dca4a44782` |
| `instrument_validation_report.md` | `2ba4670893f9b3cc4d4e41a0ceba863d7f6722000d574e7cd13a09638890cde8` |
| `execution_ledger.json` | `c48790eadfd25f5070128f83ab7256893a2842157146584e89be1581eb2611e8` |

Pilot and final manifests carry identical sha256
(`afe0e545…`) — PH5-3 stratified-recipe identical-seed property
verified: A6 drift = 0.00 by construction (byte-identical manifests).

Updated `validation.py` sha256 (post construction-bug fix):
`db69519fe84396e7854f80460b41b60c7aeb1ef06948171b7fd91b4c1860bcac`.

## §4. Test status

`pytest experiments/2026-06-11_lane-1a-prime/tests/`: **247 passed**
(no failures, no errors, no warnings). Includes three PH5-4
pre-flight refusal tests (missing-artifact; hash-mismatch;
matching-hashes) verifying the refusal machinery is exercised in unit
form independent of the live run.

## §5. Oracle verdict table hash used

`9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5`

Path: `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json`
(unchanged from PH5-1 PASS).

## §6. T3 bounds declaration hash used

`45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39`

Path: `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json`
(unchanged from PH5-1 PASS).

## §7. Stratified recipe schedule hash used

`7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5`

Path: `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json`
(unchanged from PH5-1 PASS).

## §8. Pre-flight confirmation

Runtime stdout at the start of `run_validation.py` invocation:

```text
PH5-4 pre-flight: PASSED (all lock-event artifact hashes match)
```

The three lock-event artifacts at the locked paths returned sha256s
identical to the three declared hashes embedded in `run_validation.py`
(also unchanged from PH5-1 PASS). The pipeline proceeded to manifest
construction, policy battery, A6 re-verification, oracle validation,
and report assembly only after pre-flight returned silently.

## §9. A6 results

```text
drift_within_tolerance: True
declared_tolerance: 0.05 (joint disposition; IS-7)
envelope_drift: 0.0000
flagged_drifts: []
per_policy_drift:
  pure_last_position:        0.0000
  salient_endpoint:          0.0000
  recency_excluding_target:  0.0000
  prefix_neighbor_confusion: 0.0000
```

A6 PASS: pilot and final manifests are byte-identical
(`afe0e545…` shared sha256) — drift is zero by construction under the
locked stratified recipe + identical-seed property (PH5-3).

## §10. T1 report (battery degeneracy audit + envelope)

Per-policy hit rates (answerable / null):

| policy | answerable | null | classification |
|---|---|---|---|
| pure_last_position | 24/80 = 0.3000 | 0/16 = 0.0000 | discriminative |
| salient_endpoint | 13/80 = 0.1625 | 0/16 = 0.0000 | discriminative |
| recency_excluding_target | 12/80 = 0.1500 | 0/16 = 0.0000 | discriminative |
| prefix_neighbor_confusion | 12/80 = 0.1500 | 0/16 = 0.0000 | discriminative |
| copy_completion | 0/80 = 0.0000 | 0/16 = 0.0000 | — |

| envelope quantity | value |
|---|---|
| union envelope (answerable) | 49/80 = 0.6125 |
| deterministic expectation per TL §2 / PH5-1 schedule | 48/80 = 0.6000 |
| envelope cap (declared) | 0.8000 |
| room below cap | 0.1875 |

**Comparison to TL §2 corrected expected constants:**

| policy | TL §2 expected | run-3 measured | match? |
|---|---|---|---|
| pure_last_position | 24/80 = 0.30 | 24/80 = 0.30 | exact ✓ |
| salient_endpoint | 12/80 = 0.15 | 13/80 = 0.1625 | within ~1 item incidental |
| recency_excluding_target | 12/80 = 0.15 | 12/80 = 0.15 | exact ✓ |
| prefix_neighbor_confusion | 12/80 = 0.15 | 12/80 = 0.15 | exact ✓ |
| union envelope | 48/80 = 0.60 | 49/80 = 0.6125 | within 1 incidental |
| expected A6 drift | 0.00 | 0.00 | exact ✓ |

The one-item variance in `salient_endpoint` and `union envelope` is a
chance coincidence of an item in the `no_structural_feature` stratum
having its position-0 distractor value equal to gold by random draw
(probability ≈ 1/26 per item × 32 no-feature items ≈ 1.2 expected
incidentals). The per-policy cap (0.50) and envelope cap (0.80) both
hold with ample margin; no criterion is altered.

All policies discriminative (point estimate ≤ envelope cap 0.80).
A2 / A3 caps respected. No required behavioral signature collapses.

## §11. T3 report (six-criterion checklist)

Ideal witness in pass region: **True**.

| criterion | comparison | bound | is_floor | disposition |
|---|---|---|---|---|
| null_abstention_floor_unmet | ci_upper_bound | 0.75 | True | **pass** |
| answerable_abstention_ceiling_exceeded | ci_lower_bound | 0.20 | False | **pass** |
| accuracy_indistinguishable_from_token_prior | difference_interval | 0.10 | True | **pass** |
| accuracy_indistinguishable_from_declared_policy_envelope | difference_interval | 0.10 | True | **pass** |
| insufficient_measurement_headroom | ci_upper_bound | 0.15 | True | **pass** |
| strict_content_gap_instability | difference_interval | 0.30 | False | **pass** |

All six criteria active (no deferred bounds). `perfect_model_eliminable`
is False on every row (no criterion would eliminate the ideal
witness). Uniform principle in force: full interval on eliminating
side; uncertainty → NOT_RULED_OUT; data insufficiency → INCONCLUSIVE.

## §12. T4 report (review-to-lock disposition)

| review item | reviewer | risk class | disposition | owner | status |
|---|---|---|---|---|---|
| INH-1 | inherited + joint disposition | semantics | incorporated | NS+CS | resolved |
| INH-2 | inherited + joint disposition | totality | incorporated | NS+CS | resolved |
| INH-3 | inherited + joint disposition | statistics | incorporated | NS+CS | resolved |
| PH5-1 | TL+NS+CS joint lock event | process | incorporated | NS+CS | resolved |
| PH5-2 | CS implementation | implementation | incorporated | CS | resolved |
| PH5-3 | CS implementation | implementation | incorporated | CS | resolved |
| PH5-4 | CS implementation | implementation | incorporated | CS | resolved |
| PH5-5 | CS implementation | implementation | incorporated | CS | resolved |

## §13. Full-instrument oracle expected-vs-actual table

| Case | Type | Expected | Actual | Attached labels | Required-present | Required-absent-absent | Only required/permitted | Overall |
|---|---|---|---|---|---|---|---|---|
| ORC-01 | ideal_retriever | NOT_RULED_OUT | NOT_RULED_OUT | (none) | ✓ | ✓ | ✓ | PASS |
| ORC-02 | pure_last_position_shortcut | ELIMINATED | ELIMINATED | ENV, FLOOR | ✓ | ✓ | ✓ | PASS |
| ORC-03 | salient_endpoint_shortcut | ELIMINATED | ELIMINATED | ENV, FLOOR | ✓ | ✓ | ✓ | PASS |
| ORC-04 | recency_excluding_target_shortcut | ELIMINATED | ELIMINATED | ENV, FLOOR | ✓ | ✓ | ✓ | PASS |
| ORC-05 | prefix_neighbor_confusion_shortcut | ELIMINATED | ELIMINATED | ENV, FLOOR | ✓ | ✓ | ✓ | PASS |
| ORC-06 | token_prior_emitter | ELIMINATED | ELIMINATED | TP, ENV, FLOOR | ✓ | ✓ | ✓ | PASS |
| ORC-07 | universal_answerer | ELIMINATED | ELIMINATED | FLOOR, TP, ENV | ✓ | ✓ | ✓ | PASS |
| ORC-08 | universal_abstainer | ELIMINATED | ELIMINATED | CEIL, ENV | ✓ | ✓ | ✓ | PASS |
| ORC-09 | perfect_null_on_null_handler | NOT_RULED_OUT | NOT_RULED_OUT | (none) | ✓ | ✓ | ✓ | PASS |
| ORC-10 | malformed_control_semantic_separation_guard | NOT_RULED_OUT | NOT_RULED_OUT | (none) | ✓ | ✓ (TP absent) | ✓ | PASS |
| ORC-11 | mixture_shortcut_heavy | ELIMINATED | ELIMINATED | ENV | ✓ | ✓ (FLOOR, CEIL absent) | ✓ | PASS |
| ORC-12 | mixture_retrieval_heavy | NOT_RULED_OUT | NOT_RULED_OUT | (none) | ✓ | ✓ (TP, FLOOR, CEIL absent) | ✓ | PASS |

(Attached labels are abbreviated per the ORACLE_VERDICT_TABLE.json key:
TP=accuracy_indistinguishable_from_token_prior;
ENV=accuracy_indistinguishable_from_declared_policy_envelope;
HEAD=insufficient_measurement_headroom;
GAP=strict_content_gap_instability;
FLOOR=null_abstention_floor_unmet;
CEIL=answerable_abstention_ceiling_exceeded.)

## §14. Label-set matching results

**Overall: 12/12 cases `overall_matched`.** All four clauses pass on
every case:

| clause | pass count |
|---|---|
| `outcome_matched` | 12/12 |
| `required_labels_present` | 12/12 |
| `required_absent_labels_absent` | 12/12 |
| `only_required_or_permitted_attached` | 12/12 |

Notable: ORC-10 (malformed-control semantic-separation guard) passes
with `required_absent_labels=[TP]` — the v1 mislabeling regression is
not re-introduced. ORC-08 (universal abstainer) passes under the
corrected ORC-08 row with `permitted_co_labels=[TP, ENV]` (HEAD
removed per TL §4 cleanup); HEAD does not attach (envelope-derived
HEAD measurement, locked schedule envelope 0.60, CI upper on (1 −
envelope) ≈ 0.510 above the 0.15 bound).

## §15. boundary_proximity_flags, if any

**None.** No `boundary_proximity_flag` fired on any oracle case.

ORC-12 (retrieval-heavy mixture) sits on the safe side of the
envelope margin with candidate accuracy ≈ 0.825 and envelope 0.6125,
giving a difference point-estimate of +0.213. The Newcombe-Wilson CI
on the difference is comfortably above the +0.10 margin, so the
boundary-proximity diagnostic (which fires only when the interval
straddles the bound while the point estimate lies past it) does not
trigger. NS's ORC-12 row notes proximity flags as
"expected-permitted" diagnostically; their non-firing on this run is
consistent with the locked declaration and reflects the schedule's
deterministic placement of ORC-12 in the safe region.

## §16. Run-1 supersession / retention record

Path: `experiments/2026-06-11_lane-1a-prime/validation/superseded_run-1/`
Retention memo: `RUN-1-RETENTION.md`
(sha256 `0d94dc385227dbdd93369595fc9afe439ed0923154406008016d733f1c58ec88`).

Documented reasons: reduced-criteria run (CS used 2 of 6 criteria);
unlocked verdict table (NS oracle expected verdicts not co-signed);
unstratified recipe (per-draw random structural hit-rates); A6 drift
exceedance (`pure_last_position` 0.1375; envelope 0.10; both above the
0.05 tolerance).

## §17. Run-2 supersession / retention record

Path: `experiments/2026-06-11_lane-1a-prime/validation/superseded_run-2/`
Retention memo: `RUN-2-RETENTION.md`
(sha256 `065255d8d8464106afafdae2646048297d1597998ff6269a64dd9ddedd676a55`).

Documented reasons: executed under provisional bounds (FLOOR/CEIL
0.50/0.50; HEAD 0.20 candidate-derived; GAP 0.20) and 4-stratum recipe
before the NS bounds-side review was reconciled at the PH5-1 lock
event. Per the standing TL ordering memo, the corrective re-run
remained gated; the run-2 execution was premature.

**Disclosure of run-3 attempt-1 supersession** (E11 / PH5-5 also
applies to this iteration):

Path: `experiments/2026-06-11_lane-1a-prime/validation/superseded_run-3/`
Retention memo: `RUN-3-FIRST-ATTEMPT-RETENTION.md`.

Reason: CS-discovered construction bug in `construct_pilot_manifests`
`gold_in_prefix_neighborhood` stratum (prefix-sharing neighbor's value
was a random draw rather than gold; envelope came out 0.4875 instead
of 0.60). Fixed by deterministic placement of neighbor at non-edge
slot 1 with `value_token_ids = [gold_token]`, and by forcing the last
slot's value ≠ gold. No locked artifact mutates; bounds, verdicts,
schedule constants, and ORC-08/ORC-10 wording unchanged. The
corrected execution is the canonical run-3 reported in this summary.
`pilot_iteration_count` at this filing: **4**.

Run-1, run-2, run-3 attempt-1 retention dirs stand side by side; this
run-3 PASS does not erase any of them.

## §18. Instrument Validation Report update

The IVR (committed at
`validation/instrument_validation_report.md` sha256
`2ba4670893f9b3cc4d4e41a0ceba863d7f6722000d574e7cd13a09638890cde8`)
contains, per the standing addendum §9 format:

- D.1 T1 battery degeneracy audit + A6 drift block (per §10, §9 above)
- D.2 full-instrument oracle verdict table — 12 cases × 8 fields, all
  label-set columns populated; `expected_verdict_matched` = True on
  every row (per §13, §14 above)
- D.4 T3 checklist verdicts under the §B comparison rules (per §11 above)
- D.5 T4 dispositions (per §12 above)
- D.6 pilot iteration log including the run-3 attempt-1 retention
  block (E11 / PH5-5)
- D.7 execution ledger (per §19 below)
- D.8 report-level non-claim (E16) verbatim

Report-level non-claim re-stated in IVR:

> A Validation Report PASS means pre-lock adequacy on declared cases,
> pilots, and required checks only. It is not candidate evidence, not
> general field validity, not certification evidence, and not
> threshold support.

LOCK-RECORD remains PENDING re-stated in IVR §Non-authorizations.

## §19. Execution ledger

```text
no_model_invoked:                CONFIRMED
no_sweep_id_created:             CONFIRMED
no_sweep_execution:              CONFIRMED
no_candidate_or_model_outputs:   CONFIRMED
no_threshold_work:               CONFIRMED
outputs_validation_only:         "SYNTHETIC/DIAGNOSTIC instrument
                                  validation artifacts only"
files_created:                   8 (per §2)
what_was_generated:              manifests + oracle results + T1/T3/T4
                                  reports + IVR + execution ledger
what_was_computed:               per-policy hit rates; A6 drift; oracle
                                  label-set matching; T3 dispositions
                                  under locked bounds
```

## §20. No model invoked

**CONFIRMED.** No model was invoked during run-3 execution or this
filing. The validation harness is model-free at source level
(`test_validation_source_no_model_imports` and
`test_oracle_cases_source_no_model_imports` enforce no `mlx_lm` /
`from_pretrained` / `load_model` references).

## §21. No model loaded

**CONFIRMED.** No model file or weights were loaded into memory at
any point of run-3 execution.

## §22. No sweep_id created

**CONFIRMED.** No sweep configuration was generated, referenced, or
stored. No identifier of any kind was emitted by run-3.

## §23. No sweep execution

**CONFIRMED.** No batched or distributed candidate generation
occurred. The only pipeline executed was the model-free instrument
validation pipeline authorized under D2.

## §24. No candidate/model outputs produced

**CONFIRMED.** All run-3 outputs are synthetic validation artifacts:
manifests, policy battery outputs (deterministic shortcut emissions),
oracle case predictions (synthetic per the oracle_cases catalog), and
reports/ledgers. No candidate model output, no real model generation,
no sample from any neural model exists in any run-3 artifact.

## §25. LOCK-RECORD remains PENDING

**CONFIRMED.** PH5-1 closed (Team Lead PASS); the corrective run-3
PASS reported here is instrument-validation evidence under the D2
model-free boundary. It does not constitute D3 acceptance, D4
authorization, or D5 close-out. The LOCK-RECORD remains PENDING until
the corresponding lock filing under a future authorization.

All downstream gates remain CLOSED: D3 acceptance; D4 sweep
authorization; D5 close-out; model runs; model loading; new sweep_id;
sweep execution; token-prior model generations; scrambled-binding
model generations; candidate/model outputs; candidate selection;
ranking; threshold work; certification evaluation; stress-retention
testing; Claim C activation; public benchmark packaging.

---

## Appendix A — Boundary and non-claim text (verbatim)

All run-3 artifacts are labeled
`SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION`.
They determine instrument lock-eligibility only; instrument validation
≠ model evaluation; Lane 1a' may rule out and may not rule in;
passing the declared battery does not rule out undeclared shortcuts or
partial shortcut contribution. Permitted phrasing: "not explained by
the declared shortcut battery." Forbidden phrasing: "not
shortcut-driven."

## Appendix B — Standing carry (non-authorizations, verbatim)

This memo does not authorize: D3 acceptance; D4 sweep authorization;
D5 close-out; model runs; model loading; new sweep_id; sweep
execution; token-prior model generations; scrambled-binding model
generations; candidate/model outputs; candidate selection; ranking;
threshold work; certification evaluation; stress-retention testing;
Claim C activation; public benchmark packaging.

All model-touching and sweep-execution gates remain CLOSED.

— CS Engineer, 2026-06-11
