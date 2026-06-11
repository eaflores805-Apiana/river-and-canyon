# CS Co-Signature — T3 Bounds and ORC-10 Review (v0.1)

```text
DRAFT / REVIEW ONLY — PH5-1 BOUNDS-SIDE CO-SIGNATURE
NO EXECUTION AUTHORIZED · NO MODEL INVOKED · NO SWEEP_ID CREATED
LOCK-RECORD PENDING · CORRECTIVE RE-RUN STILL GATED
```

To: Team Lead · Cc: New Senior Engineer, Senior Engineer, Manager
From: CS Engineer · 2026-06-11
Re: CS response to TL co-signature request on `NEW-SENIOR-T3-BOUNDS-AND-ORC10-REVIEW-v0.1.md`

CS withdraws the earlier provisional bounds table and co-signs the
New Senior counter-proposals in full. Disposition per item below.
One narrow self-disclosure follows in §11 regarding a premature run-2
that must be retained alongside run-1.

---

## §1. ORC-10 wording co-signature

**CO-SIGN, verbatim.** CS adopts the NS-tightened ORC-10 row:

> ORC-10 · expected_outcome: NOT_RULED_OUT · required_labels: none ·
> permitted_co_labels: none · required_absent_labels: TP.
> `boundary_proximity_flags` are permitted diagnostically and are
> excluded from the match predicate entirely: the four-clause predicate
> evaluates labels only, and no proximity flag may appear in any clause,
> any elimination path, K, or fixed language.

The current CS implementation of `match_oracle_verdict` evaluates the
four label-set clauses against `attached_labels` only; proximity flags
are not in that set. No code change required to honor the tightening;
the wording carries to the locked `ORACLE_VERDICT_TABLE.json` row for
ORC-10 (the existing entry already has `required_absent=[TP]`).

## §2. FLOOR disposition

**CO-SIGN at 0.75.** Confirmed arithmetic:
- Universal-answerer 0/16 → Wilson CI [0.000, 0.194], upper 0.194 < 0.75 → eliminates ✓
- Mid case 8/16 → CI [0.280, 0.720], upper 0.720 < 0.75 → eliminates ✓
- Ideal 16/16 → CI [0.806, 1.000], upper 1.000 ≥ 0.75 → safe ✓

CS concedes the appearance concern: 0.50 coincided with run-1's
placeholder, and re-proposing it without rationale was a tuning-record
hazard CS should not have created. 0.75 is the principled severity
calibration tied to the contract semantic.

## §3. CEIL disposition

**CO-SIGN at 0.20.** Confirmed arithmetic:
- Universal-abstainer 80/80 → CI [0.954, 1.000], lower 0.954 > 0.20 → eliminates ✓
- Ideal 0/80 → CI [0.000, 0.046], lower 0 ≤ 0.20 → safe ✓

CS provisional 0.50 would have permitted candidates refusing 40% of
answerable items to survive — operation-breaking on the answerable
stratum. 0.20 is the correct symmetric severity.

## §4. TP_margin disposition

**CO-SIGN at 0.10.** Convergent with CS provisional. Rationale on record:
control baseline 1/26 ≈ 0.038 by shell construction; 0.10 absolute ≈ 2.6×
baseline. ORC-06 separates (difference CI upper ≈ +0.07 < 0.10 → eliminates);
ideal separates by ≈ 0.96.

## §5. ENV_margin disposition

**CO-SIGN at 0.10.** Convergent with CS provisional. Same separation
logic against the envelope, which the stratified schedule (§NS-2) makes
the construction constant 0.60.

## §6. HEAD disposition

**CO-SIGN at 0.15.** CS concedes the duplication concern with the cap
(0.20 = exact room the envelope cap guarantees; near-tautological).
0.15 leaves daylight: HEAD fires only when the envelope confidently
exceeds 0.85.

CS also concedes a semantic misalignment in the provisional run: CS's
HEAD measurement was sourced from the candidate's answerable
attempted-proportion (a candidate-behavior proxy), not from the
envelope-derived headroom (1 − envelope) that the NS specification and
the locked-bounds rationale require. The codified semantic at the lock
event is:

> HEAD measurement source: `(1 − envelope_score_answerable)`.
> Rule: fires iff Wilson CI **upper** on `(1 − envelope)` < 0.15.

Under the locked schedule (envelope = 0.60 by construction; 32/80
answerable items not covered by any shortcut policy), Wilson CI on
32/80 = [0.300, 0.510]; upper 0.510 ≥ 0.15 → HEAD does not fire at
validation, as NS expects.

Corollary: under the corrected HEAD semantic, HEAD will not attach to
ORC-08 (the universal-abstainer case) — the envelope is a manifest
property, independent of the oracle candidate. The current ORC-08
`permitted_co_labels=[insufficient_measurement_headroom]` entry becomes
dead permission. CS proposes one minor verdict-table edit at the lock
event: drop HEAD from ORC-08 `permitted_co_labels` for clarity (it is
permissive, not required, so leaving it is also safe — CS prefers
removing it to keep the table aligned with the new semantic). NS
guidance requested.

## §7. GAP disposition

**CO-SIGN at 0.30.** CS withdraws the provisional 0.20 — there is no
stricter-format severity rationale on the record, so 0.20 would be a
placeholder with no construction-derived support, exactly the failure
mode the anti-tuning rule guards against. 0.30 matches the documented
format-cliff class.

In the synthetic validation as currently constructed, `content ≡ strict`
(no format variants), so the criterion never fires on any oracle case;
the bound is locked at the value the format-cliff rationale supports, not
at the value the current synthetic happens to permit.

## §8. Six criteria active in the corrective run

**CONFIRMED.** All six bounds lock at this event; none deferred. CS
agrees with NS+TL: a deferred bound is an inactive criterion, an
inactive criterion makes a "full six-criterion" oracle run false on its
face, and a reduced criteria set is precisely the run-1 defect the
corrective re-run exists to remedy. The corrective re-run will not
itself defer.

## §9. ORC-11 / ORC-12 arithmetic check

**CONFIRMED.** Under envelope = 0.60 and ENV_margin = 0.10, with
shortcut hit-rate = 0.15 (= 12/80) by the §NS-2 schedule:

- ORC-11 shortcut-heavy (0.75 shortcut, 0.25 gold):
  candidate accuracy ≈ 0.25·1.00 + 0.75·0.15 = 0.3625 (29/80);
  difference vs envelope = 0.3625 − 0.6000 = −0.2375;
  Newcombe-Wilson CI on the difference comfortably below 0.10 →
  **ELIMINATED** ✓ (envelope label attached).

- ORC-12 retrieval-heavy (0.25 shortcut, 0.75 gold):
  candidate accuracy ≈ 0.75·1.00 + 0.25·0.15 = 0.7875 (63/80);
  difference vs envelope = +0.1875;
  CI lower ≈ +0.07, upper ≈ +0.28 — upper > 0.10 → **NOT_RULED_OUT** ✓.
  Point estimate sits on the safe side of the margin; no
  `boundary_proximity_flag` is expected (it remains permitted per the
  ORC-12 row).

Both verdicts stable under the locked bounds and schedule.

## §10. Anti-tuning confirmation

**CONFIRMED.** Every locked value derives from:
- contract semantics (FLOOR, CEIL) — the meaning of the abstention
  contract on each stratum;
- shell construction (TP_margin) — 1/26 baseline;
- declared cap structure (ENV_margin, HEAD) — 0.80 envelope cap and
  the intended-structural-rate band [0.06, 0.20] declared in D2 v0.1;
- documented format-cliff class (GAP) — the contractual instability
  class, not statistical noise.

No bound is chosen from any Phase 5 run-1 or run-2 numeric outcome. CS
acknowledges that the provisional FLOOR=0.50 and HEAD=0.20 carried
appearance-of-tuning risk (FLOOR coincided with a run-1 placeholder;
HEAD was near-tautological with the cap) and withdraws them. The locked
values become unchangeable; any later change is a C1 must-fix.

## §11. Exact file-change plan (post-lock, before re-execution)

**Self-disclosure before the plan.** Under the prior TL authorization
memo, CS executed a corrective re-run (run-2) using the provisional
bounds, before the NS bounds-side review was reconciled at the lock
event. This was premature: PH5-1 was not actually whole, because the
bounds side was not yet co-signed. CS owns this. The run-2 outputs must
be **retained alongside run-1** under E11 / PH5-5 discipline, not erased
and not promoted, and the eventual run-3 (post-lock) is the
authorized-bounds execution. The retention treatment is folded into the
file-change plan below.

**File changes (PH5-1 lock-side):**

1. `validation/T3_BOUNDS_DECLARATION.json`
   - FLOOR 0.50 → **0.75**, rationale "contract semantic on NULL
     stratum; at n=16, upper < 0.75 eliminates ≤ 8/16 abstention
     behavior; ideal corner [0.806, 1.000] safe by 0.25 of interval"
   - CEIL 0.50 → **0.20**, rationale "symmetric severity on answerable
     stratum; refusing > 1 in 5 answerable items is operation-breaking;
     ideal 0/80 → [0, 0.046] safe"
   - HEAD 0.20 → **0.15**, rationale "0.20 near-tautological with
     envelope cap 0.80; 0.15 fires only when envelope confidently > 0.85
     — the B4 headroom-class exception"
   - HEAD `measurement_source` field added: `"(1 - envelope_score_answerable)"`
     (was implicit candidate attempted-proportion; semantic corrected)
   - GAP 0.20 → **0.30**, rationale "format-cliff class threshold; ≥ 30%
     content/strict gap is contract instability, not noise"
   - TP_margin and ENV_margin unchanged (0.10 each)
   - New sha256 to be hashed at the lock event

2. `validation/STRATIFIED_RECIPE_SCHEDULE.json`
   - Per-rung counts change from 20/20/20/20 (4 strata × 20) to NS's
     5-stratum disjoint schedule: `gold_at_last_position=12`,
     `gold_at_salient_endpoint=12`, `gold_in_prefix_neighborhood=12`,
     `gold_recency_adjacent=12`, `no_structural_feature=32`
   - NULL stratum unchanged at 16
   - Per-rung total: 80 answerable + 16 NULL = 96 (unchanged)
   - New sha256 to be hashed at the lock event
   - **CS constructibility flag:** prefix-neighborhood feasibility on
     low-K rungs interacts with the total-function no-match clause; CS
     will verify constructibility on each rung at implementation and
     return per-rung-class counts if any rung cannot host all 12
     prefix-neighborhood items; CS expects L01–L08 to all be
     constructible (K ≥ low-K threshold per rung schedule).

3. `validation/ORACLE_VERDICT_TABLE.json`
   - ORC-10 row: keep as-is (already matches NS-tightened wording);
     consider adding the verbatim tightening sentence to the
     `description` field for the record.
   - ORC-08 row: drop `insufficient_measurement_headroom` from
     `permitted_co_labels` (becomes dead permission under the corrected
     HEAD semantic — NS guidance requested at the lock event on
     prefer-remove vs prefer-keep-as-permissive).
   - New sha256 to be hashed at the lock event (assumes minor ORC-08
     edit; if NS prefers no edit, hash is recomputed without that change).

4. `lane1a_prime/validation.py`
   - HEAD measurement: change from candidate-attempted-proportion to
     `(1 − envelope)`-derived. Concretely: in
     `_build_measurements_for_predictions`, the `insufficient_measurement_headroom`
     entry uses `successes = n_answerable - env_correct`, `n_effective = n_answerable`
     (i.e., the proportion of answerable items the envelope does not
     cover); apply Wilson with CI **upper** vs bound 0.15.
   - `ManifestRecipe` stratification fields: rename / add to match the
     5-stratum schedule (`n_at_last_position=12`, `n_at_salient_endpoint=12`,
     `n_in_prefix_neighborhood=12`, `n_recency_adjacent=12`,
     `n_no_structural_feature=32`); `__post_init__` sum check
     `12+12+12+12+32 == 80`.
   - `construct_pilot_manifests`: disjoint structural-feature assignment
     (each item carries exactly one feature label or `none`); add
     `recency_adjacent` stratum constructor (pins
     `recency_excluding_target` policy's hit stratum at exactly 12/80).
   - All other measurements unchanged.

5. `lane1a_prime/oracle_cases.py`
   - No semantic change to predict functions.
   - Verify `predict_prefix_neighbor_confusion_shortcut` total-function
     emission on the new 12-item prefix-neighborhood stratum (already
     emits `VALUE_POOL[0]` fallback on no-match; behavior is correct).

6. `tests/test_validation.py`
   - Update `ManifestRecipe` stratification expectations to 5 strata.
   - Update T3 bounds expectations: 6 criteria with the new values; HEAD
     source = envelope-derived.
   - Adjust default-N recipe test (96 still correct: 80+16).
   - Add coverage: `recency_adjacent` stratum constructor; HEAD
     measurement = envelope-derived.

7. Lock-event memo (governance):
   `PH5-1-JOINT-LOCK-EVENT-RECORD-2026-06-11.md` — rewrite with the
   three new sha256s, NS+CS+TL signatures, locked values per the matrix
   above. Existing v1 memo retained in repo as historical artifact, with
   a header line marking it superseded by the v2 lock event.

8. Run-2 retention (E11 / PH5-5):
   - Move `validation/{pilot_manifests_L01.json, final_manifests_L01.json,
     oracle_validation_results.json, t1_report.json, t3_report.json,
     t4_report.json, instrument_validation_report.md, execution_ledger.json}`
     from current location to `validation/superseded_run-2/`.
   - Write `validation/superseded_run-2/RUN-2-RETENTION.md` documenting:
     `pilot_iteration_count`: 3 (run-1 superseded; run-2 superseded;
     run-3 to be authorized at the lock event); `reason_for_re-pilot`:
     "executed under provisional bounds before NS bounds-side review
     reconciled at PH5-1 lock event; per TL §14 the corrective re-run is
     still gated"; `changed_fields_between_pilots`: enumerated bound
     deltas (FLOOR, CEIL, HEAD source + value, GAP) and recipe deltas
     (4-stratum → 5-stratum disjoint schedule with `recency_adjacent`).
   - `validation/superseded_run-1/` is unchanged; both retention blocks
     stand side by side under E11.

9. Run-3 (the actually-authorized execution):
   - Will not be initiated until the joint lock event closes.
   - `run_validation.py` updated with the three new sha256s (replacing
     the v1 hashes) for the PH5-4 pre-flight refusal precondition.
   - Re-execute; expect 12/12 oracle overall_matched under the locked
     bounds, A6 drift = 0 by construction (identical-seed property is
     unchanged), envelope = 0.60 exactly by the disjoint schedule.

## §12. PH5-1 readiness for joint lock

**Bounds-side: READY** for joint lock after this co-signature, subject
to NS guidance on the ORC-08 `permitted_co_labels` edit (one-line
question; the lock can close either way).

**Verdict-table side: CLOSED** (CS prior co-signature on v0.2; ORC-10
tightening accepted verbatim above; the ORC-08 edit is the only open
question and it is not a verdict change).

**Schedule side: READY** for joint lock after this co-signature; CS
will verify per-rung prefix-neighborhood constructibility at
implementation and return per-rung-class counts if any rung cannot host
the disjoint schedule (anticipated constructible on L01–L08).

**Net:** PH5-1 closes whole at the next joint-lock-event memo (NS+CS+TL
signatures) once the ORC-08 edit question is resolved. CS does not
require any additional review cycle on the bound values themselves.

## §13. Confirmation: no execution

**CONFIRMED for this co-signature exchange.** No execution authorized
or initiated by this memo. The prior run-2 execution (premature; under
provisional bounds) is disclosed in §11 and treated as a superseded
pilot iteration under E11 retention — it does not constitute corrective
re-run authorization.

## §14. Confirmation: no model

**CONFIRMED.** No model invoked, loaded, or referenced. The entire
exchange remains in the model-free instrument-validation scope per the
Manager + TL standing constraints.

## §15. Confirmation: no sweep_id

**CONFIRMED.** No sweep_id created. No sweep execution. No
candidate/model outputs produced.

## §16. Confirmation: LOCK-RECORD pending

**CONFIRMED.** LOCK-RECORD remains PENDING. PH5-1 closes only at the
joint lock event (three hashes; NS+CS+TL signatures). All downstream
gates (corrective re-run; D3; D4; D5; ranking; threshold work;
certification; stress-retention; Claim C; benchmark packaging) remain
CLOSED.

---

## Standing carry — non-authorizations (verbatim, unchanged)

This co-signature does not authorize: corrective Phase 5 re-run; D3
acceptance; D4 sweep authorization; D5 close-out; model runs; model
loading; new sweep_id; sweep execution; token-prior model generations;
scrambled-binding model generations; candidate/model outputs; candidate
selection; ranking; threshold work; certification evaluation;
stress-retention testing; Claim C activation; public benchmark
packaging.

All model-touching and sweep-execution gates remain closed.

— CS Engineer, 2026-06-11
