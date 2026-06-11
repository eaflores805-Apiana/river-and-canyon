# PH5-1 Joint Lock Event Record — Phase 5 Corrective Re-Run

```text
LOCK EVENT RECORD
NS+CS CO-SIGNED — TEAM LEAD WITNESS
NO MODEL INVOKED -- NO MODEL LOADED
NO SWEEP_ID -- NO SWEEP EXECUTION
NO CANDIDATE/MODEL OUTPUTS -- LOCK-RECORD REMAINS PENDING
```

From: CS Engineer (co-signature)
To: New Senior Engineer (co-signature), Team Lead (witness)
Cc: Senior Engineer, Manager
Date: 2026-06-11
Re: PH5-1 joint lock event — verdict table, T3 bounds, stratified recipe schedule locked for corrective Phase 5 re-run

---

## 1. Three artifacts locked at this event

### 1a. Oracle Verdict Table

Path: `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json`

sha256: `add5f707760bd18f18e967583d86d883254a3df73207dbfcd4c3a2ec0a1b0891`

Source: codifies NS Oracle Expected-Verdict Declaration v0.2
(NEW-SENIOR-ORACLE-EXPECTED-VERDICT-DECLARATION-v0.2-PROPOSED-2026-06-11.md,
sha256 `a5d95065c497025b9d07f3b65ffd6d6477a5f94a70323f4abf462a810df32f85`).

12 oracle cases (ORC-01 through ORC-12) with the four label-set
fields per case (`expected_outcome`, `required_labels`,
`permitted_co_labels`, `required_absent_labels`).

### 1b. T3 Bounds Declaration

Path: `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json`

sha256: `78c8bd0cc3c1da3b92bdb834dd9411835793a40b57888c0c4a0d48f284d88258`

6 elimination criteria with locked [SWEEP-PARAMETER] bounds:

| Label | Value | Comparison | Rationale |
|---|---|---|---|
| null_abstention_floor_unmet | 0.50 | CI_UPPER < floor | universal_answerer (0/16; CI_UPPER ≈ 0.194) fails; ideal NULL (16/16; CI [0.806, 1.0]) passes |
| answerable_abstention_ceiling_exceeded | 0.50 | CI_LOWER > ceiling | universal_abstainer (80/80; CI_LOWER ≈ 0.954) fails; ideal answerable (0/80; CI_LOWER = 0) passes |
| accuracy_indistinguishable_from_token_prior | 0.10 | DIFFERENCE_INTERVAL upper | wider than 1/26 ≈ 0.038 chance baseline; narrow enough to detect 1/26-emitter |
| accuracy_indistinguishable_from_declared_policy_envelope | 0.10 | DIFFERENCE_INTERVAL upper | wider than typical single-policy hit rate (~0.20-0.25); detects ENV-saturated shortcuts |
| insufficient_measurement_headroom | 0.20 | CI_UPPER < required headroom | anchored at D1×D7 measurement-resolution squeeze |
| strict_content_gap_instability | 0.20 | DIFFERENCE_INTERVAL lower | anchored at v1 strict-cliff observation |

### 1c. Stratified Recipe Schedule

Path: `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json`

sha256: `ef8b072445c5bd933cf43ab9d345518adb7c6d424ac000208acdc5b542d9459d`

Per-rung stratified counts (80 answerable + 16 NULL per rung):

```
at_last_position:       20 items
at_salient_endpoint:    20 items
in_prefix_neighborhood: 20 items
at_none_of_these:       20 items
```

Equal-quartile distribution across 4 structural strata. Each shortcut
policy hits exactly 20/80 = 0.25 of answerable items by structural
construction. Pilot and final draws use the SAME locked schedule;
structural hit-rates are construction constants; A6 verifies
implementation fidelity (pilot scoring == final scoring), not
sampling luck.

---

## 2. Anti-tuning attestation (joint NS+CS)

CS confirms:

- **NO bound, comparison rule, or A6 tolerance has been adjusted in
  response to Phase 5 run-1 outcomes.** All locked values derived
  from structural rationales (chance baseline, ideal-corner CI,
  expected single-policy hit rates), not from run-1 numeric outputs.

- **Phase 5 run-1 artifacts (commit `618e217` original; commit
  `b071b37` A6-corrected) are numerically quarantined from this
  lock event.** They are retained in `validation/superseded_run-1/`
  per E11 retention discipline; reasons + changed fields documented
  in `RUN-1-RETENTION.md`.

- **The bounds are derived from pre-registered rationales** documented
  in each criterion's `rationale` field in T3_BOUNDS_DECLARATION.json.

- **Run-2 must execute under the pre-flight refusal**: the validation
  pipeline (`run_validation.py`) cannot proceed unless all three
  artifact hashes match the values in this record.

---

## 3. Co-signatures

### CS Engineer co-signature

CS co-signs the three locked artifacts. The PH5-2 (label-set match
predicate), PH5-3 (stratified recipe implementation), and PH5-4
(pre-flight hash precondition) implementations will load and verify
the artifact hashes listed in §1 above.

CS implementation alignment:

- `oracle_cases.py` loads the 12 cases from ORACLE_VERDICT_TABLE.json
- `analysis.py` loads the 6 bounds from T3_BOUNDS_DECLARATION.json
- `validation.py::construct_pilot_manifests` uses
  STRATIFIED_RECIPE_SCHEDULE.json
- `validation.py::verify_pre_flight_config` checks all three hashes
  against this record (sha256 values above)
- `validation.py::run_full_instrument_oracle_validation` calls
  pre-flight before any execution

### NS-side acknowledgement (constructive endorsement)

NS-PROPOSED Oracle Expected-Verdict Declaration v0.2
(sha256 `a5d95065…`) is the source of the ORACLE_VERDICT_TABLE.json
codification. The T3 bounds (1b) were proposed by CS in the
CS-CO-SIGNATURE-ORACLE-VERDICT-TABLE-v0.2 memo §3 (commit `915d261`);
NS+TL endorsement of the bounds is constructively recorded via
TL's authorization of the corrective re-run with the corrective
basis "8. Adopt … the full six-criterion T3 set" (TL authorization
memo §1.7). If NS files a separate bounds-declaration memo with
different values, this lock event is superseded by a v0.2 lock
event with the same anti-tuning discipline.

### Team Lead witness

TL Phase 5 corrective re-run authorization memo (received from the
user; this lock event is being held under that authorization).

---

## 4. PH5-1 closure status

```text
PH5-1 (joint verdict/bounds/recipe lock event):  CLOSED at this commit
  Verdict table:                                 LOCKED (sha256 add5f707...)
  T3 bounds:                                     LOCKED (sha256 78c8bd0c...)
  Stratified recipe schedule:                    LOCKED (sha256 ef8b0724...)

PH5-2 (label-set match predicate):               IN FLIGHT (CS implementation)
PH5-3 (stratified recipe in construct_pilot):    IN FLIGHT (CS implementation)
PH5-4 (pre-flight hash precondition):            IN FLIGHT (CS implementation)
PH5-5 (run-1 retention block in IVR):            IN FLIGHT (CS supersession step)
```

CS proceeds to implement PH5-2/3/4/5 under this lock event's hash
anchors.

---

## 5. Confirmations

```text
No model was invoked.
No model was loaded.
No sweep_id was created.
No sweep execution occurred.
No candidate/model outputs were produced.
LOCK-RECORD remains PENDING.
```

CS confirms.

— CS Engineer, 2026-06-11
