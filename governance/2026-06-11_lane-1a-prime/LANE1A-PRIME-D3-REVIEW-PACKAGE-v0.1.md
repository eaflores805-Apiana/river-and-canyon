# Lane 1a' D3 Review Package (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
MANAGER-FACING D3 DECISION REQUEST — INSTRUMENT LOCK-ELIGIBILITY ONLY
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
NO CANDIDATE/MODEL OUTPUTS PRODUCED · LOCK-RECORD PENDING
```

To: Manager · Cc: Team Lead, New Senior Engineer, Senior Engineer
From: CS Engineer (joint package; NS counter-signature in §8)
Date: 2026-06-11
Re: TL §10 D3 review package per the run-3-incidental-disposition PASS

Per Team Lead direction (run-3 incidental structural-hit disposition
PASS; run-3 confirmed D3 candidate), CS files the D3 review package
for Manager consideration. The package consolidates the lock-event
artifacts, the corrective-run-3 results, the supersession ledger, the
incidental-hit disposition (jointly counter-signed), and the explicit
non-claim block into a single Manager-facing record.

The D3 question — narrowly framed per TL §8 — appears in §8 below.

---

## §1. File list (commit `c7b5fef`)

**Lock-event artifacts (CS+NS+TL hash-bound at PH5-1 PASS):**

```text
experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json
experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json
experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json
```

**Run-3 outputs (canonical; passed all six T3 criteria; 12/12 oracle match):**

```text
experiments/2026-06-11_lane-1a-prime/validation/pilot_manifests_L01.json
experiments/2026-06-11_lane-1a-prime/validation/final_manifests_L01.json
experiments/2026-06-11_lane-1a-prime/validation/oracle_validation_results.json
experiments/2026-06-11_lane-1a-prime/validation/t1_report.json
experiments/2026-06-11_lane-1a-prime/validation/t3_report.json
experiments/2026-06-11_lane-1a-prime/validation/t4_report.json
experiments/2026-06-11_lane-1a-prime/validation/instrument_validation_report.md
experiments/2026-06-11_lane-1a-prime/validation/execution_ledger.json
```

**Governance memos (the D3 record):**

```text
governance/2026-06-11_lane-1a-prime/PH5-1-JOINT-LOCK-EVENT-RECORD-v0.2.md
governance/2026-06-11_lane-1a-prime/PH5-1-LIVE-REFUSAL-CHECK-CONFIRMATION-v0.1.md
governance/2026-06-11_lane-1a-prime/PHASE5-v0.2-CORRECTIVE-RUN3-COMPLETION-SUMMARY.md
governance/2026-06-11_lane-1a-prime/RUN3-INCIDENTAL-STRUCTURAL-HIT-DISPOSITION-v0.1.md
governance/2026-06-11_lane-1a-prime/NEW-SENIOR-COUNTERSIGN-RUN3-INCIDENTAL-DISPOSITION-v0.1.md
```

**Retention dirs (E11 / PH5-5 discipline; auditable forever):**

```text
experiments/2026-06-11_lane-1a-prime/validation/superseded_run-1/  (8 files + RUN-1-RETENTION.md)
experiments/2026-06-11_lane-1a-prime/validation/superseded_run-2/  (8 files + RUN-2-RETENTION.md)
experiments/2026-06-11_lane-1a-prime/validation/superseded_run-3/  (8 files + RUN-3-FIRST-ATTEMPT-RETENTION.md)
```

## §2. sha256 hashes

### Lock-event artifacts

| artifact | sha256 |
|---|---|
| `ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5` |
| `T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39` |
| `STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5` |

### Run-3 outputs

| artifact | sha256 |
|---|---|
| `pilot_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| `final_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| `oracle_validation_results.json` | `37759f9acfffd6766d73cb0b6c5e66c0cd74e1608b424b41650a7f7c6ebefaad` |
| `t1_report.json` | `03ff6353c2fe38c2584312d1d1c08185a78799e15a01372df71a8ce085353a0f` |
| `t3_report.json` | `ca6e627cceaa9c70b47e343378d5a29d7511069801733e7190aea59280e843f4` |
| `t4_report.json` | `104ff3d64a05f0228e53a17ae404586bf421716ad5503ed0c62345dca4a44782` |
| `instrument_validation_report.md` | `2ba4670893f9b3cc4d4e41a0ceba863d7f6722000d574e7cd13a09638890cde8` |
| `execution_ledger.json` | `c48790eadfd25f5070128f83ab7256893a2842157146584e89be1581eb2611e8` |

Pilot and final manifests carry identical sha256 (`afe0e545…`) — PH5-3
identical-seed property verified; A6 drift = 0 by construction.

### Governance memos

| memo | sha256 |
|---|---|
| `PH5-1-JOINT-LOCK-EVENT-RECORD-v0.2.md` | `264cc47e90f7c9d3aebb93dd122340f2d4cb255e1111290f34e2a238ed744e29` |
| `PH5-1-LIVE-REFUSAL-CHECK-CONFIRMATION-v0.1.md` | `5bb368a331ab1ee5b0172991bc9c2bf1eeb6ecfb71c19be70de82984096e80b6` |
| `PHASE5-v0.2-CORRECTIVE-RUN3-COMPLETION-SUMMARY.md` | `9655b8c5c56377f5311c94a480a760023a40db6e2d1fe198801c26565b0df7e4` |
| `RUN3-INCIDENTAL-STRUCTURAL-HIT-DISPOSITION-v0.1.md` | `98f55a2e798eca848d577eb2ccd434b5016bccfc644839686820f982ad640a30` |
| `NEW-SENIOR-COUNTERSIGN-RUN3-INCIDENTAL-DISPOSITION-v0.1.md` | `cce6be71050028a1526678d5350872c95c9f7a25cba3c24bf31b8916fec2d89d` |

### Retention memos

| retention memo | sha256 |
|---|---|
| `superseded_run-1/RUN-1-RETENTION.md` | `0d94dc385227dbdd93369595fc9afe439ed0923154406008016d733f1c58ec88` |
| `superseded_run-2/RUN-2-RETENTION.md` | `065255d8d8464106afafdae2646048297d1597998ff6269a64dd9ddedd676a55` |
| `superseded_run-3/RUN-3-FIRST-ATTEMPT-RETENTION.md` | `b437fccc9afa8bafe4f12d7760d9258e329ee2d8b9515befc490a40e7eda1195` |

## §3. Commit SHA

```text
c7b5fef346c73525c0d166b5e46e5cd2fa2f8c0f   (short: c7b5fef)
```

This commit is on `origin/main` at the time of filing. A subsequent
commit may add this D3 package memo itself and the NS counter-sign
mirror — the canonical run-3 artifacts and the four governance memos
listed in §2 are already at `c7b5fef`.

## §4. Validation result summary

```text
Oracle validation (full-instrument; label-set matching):  12/12 overall_matched
T3 checklist (6 criteria; locked bounds):                  ALL PASS
Ideal witness in pass region:                              True
A6 final-manifest re-verification:                         drift 0.0000 every component
                                                           (pilot == final by construction)
boundary_proximity_flags:                                  none fired
Per-policy hit rates (vs TL §2 expected):
  pure_last_position             24/80 = 0.3000   ✓
  salient_endpoint               13/80 = 0.1625   +1 incidental (dispositioned §6)
  recency_excluding_target       12/80 = 0.1500   ✓
  prefix_neighbor_confusion      12/80 = 0.1500   ✓
  copy_completion                 0/80 = 0.0000   ✓
Measured policy-union envelope:                            49/80 = 0.6125
                                                           (cap 0.80; room 0.1875)
Intended item-label envelope (PH5-1 lock event):           48/80 = 0.6000
HEAD (1 - envelope) Wilson CI upper:                       ≈ 0.51  (does not fire; bound 0.15)
Locked T3 bound matrix:
  FLOOR  null_abstention_floor_unmet                       0.75
  CEIL   answerable_abstention_ceiling_exceeded            0.20
  TP     accuracy_indistinguishable_from_token_prior       0.10
  ENV    accuracy_indistinguishable_from_declared_envelope 0.10
  HEAD   insufficient_measurement_headroom                 0.15
  GAP    strict_content_gap_instability                    0.30
Test suite at this filing:                                 247 passed
PH5-4 pre-flight refusal (runtime + 3 unit tests):         exercised, all PASS
```

All instrument invariants hold. No criterion verdict changes between
the intended (0.60) and measured (0.6125) envelope; the eliminative
machinery is union-based and overlap-insensitive to the +1 incidental
per NS adjudication.

## §5. Supersession ledger

| run | status | retention path | retention memo sha256 |
|---|---|---|---|
| run-1 | superseded | `validation/superseded_run-1/` | `0d94dc38…` |
| run-2 | superseded | `validation/superseded_run-2/` | `065255d8…` |
| run-3 attempt-1 | superseded | `validation/superseded_run-3/` | `b437fccc…` |
| run-3 attempt-2 | **current (D3 candidate)** | `validation/` | — |

`pilot_iteration_count` at this filing: **4** (cumulative across all
attempts).

Documented reasons (per retention memos; each cumulative and distinct):

- **run-1**: reduced-criteria run (CS used 2 of 6); unlocked verdict
  table; unstratified recipe; A6 drift exceedance.
- **run-2**: executed under provisional bounds (FLOOR/CEIL 0.50/0.50;
  HEAD 0.20 candidate-derived; GAP 0.20) and 4-stratum recipe before
  NS bounds-side review reconciled at the PH5-1 lock event.
- **run-3 attempt-1**: CS-detected construction bug in
  `gold_in_prefix_neighborhood` stratum (prefix-sharing neighbor's
  value was a random draw rather than gold; envelope came out 0.4875).
  Fixed in attempt-2 by deterministic non-edge placement with
  value = gold and forced last-slot value ≠ gold.

A D3 PASS does not erase any of the three retention dirs; they remain
auditable forever per E11 / PH5-5.

## §6. Incidental-hit disposition summary

Joint disposition (CS sha256 `98f55a2e…`; NS counter-signature
`cce6be71…`; TL PASS via the filter memo).

**Harmonized interpretation (per TL §2 of the filter memo, verbatim):**

> A for the construction. B for the record.
> A — the incidental overlap is acceptable under the adjudicated
> item-label-disjoint construction.
> B — the lock-event record required documentation correction because
> "exactly" overstated the relationship between intended schedule
> constants and measured policy-union values.
> Neither letter should be cited alone going forward.
> The accepted language is: **acceptable incidental overlap plus
> required documentation correction.**

**Intended-vs-measured distinction (TL-accepted):**

| quantity | intended item-label | measured policy-union |
|---|---|---|
| envelope | 48/80 = 0.60 | 49/80 = 0.6125 |
| `salient_endpoint` | 12/80 = 0.15 | 13/80 = 0.1625 |

The instrument evaluates measured values. The +1 incidental is honest
shortcut-surface coincidence (a position-0-reading biased policy would
genuinely answer correctly on that item); it is not noise.

**Cause:** one chance value-pool coincidence in the
`no_structural_feature` stratum where `position[0]`'s uniform-VALUE_POOL
distractor value happened to equal gold (expected incidentals per
policy ≈ 32/26 ≈ 1.23 per run; measured: 1).

**Effect:** none on any criterion verdict, oracle match (12/12), T3
disposition (all PASS), A6 result (drift 0.00 every component), or
HEAD firing (non-firing under both intended and measured envelope).

**Disposition:** no re-run required; no artifacts superseded; locked
recipe artifact (sha256 `7ad3ccdd…`) does NOT mutate; the
interpretation gloss lives in the two disposition memos (CS + NS) and
is referenced from this D3 package memo.

## §7. Non-claim block (explicit; verbatim carry)

Per the standing addendum E16 and NS-final boundary text incorporated
into the joint lock-event record:

> A Validation Report PASS means **pre-lock adequacy on declared
> cases, pilots, and required checks only**. It is not candidate
> evidence, not general field validity, not certification evidence,
> and not threshold support.

Per the joint lock-event record §Appendix B (Boundary and non-claim
text):

> All run-3 artifacts are labeled
> `SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION`.
> They determine instrument lock-eligibility only; instrument
> validation ≠ model evaluation; Lane 1a' may rule out and may not
> rule in; passing the declared battery does not rule out undeclared
> shortcuts or partial shortcut contribution.
> Permitted phrasing: **"not explained by the declared shortcut battery."**
> Forbidden phrasing: **"not shortcut-driven."**

This non-claim block governs every artifact in §1–§2 and every
interpretation in §4–§6.

## §8. D3 decision question

Per Team Lead §8 narrow framing, the Manager-facing question is:

> **Does the completed model-free validation package establish that
> the Lane 1a' instrument is lock-eligible for the next authorized
> step?**

This question is **not** framed as:

- Does Lane 1a' prove model capability?
- Does Lane 1a' certify a candidate?
- Does Lane 1a' activate Claim C?

Evidence offered to support the D3 decision:

1. **Lock-event integrity** — three artifacts hash-bound (CS+NS+TL
   signed); PH5-4 pre-flight refusal mechanically prevents drift from
   the locked declaration (verified in source, by unit tests, and at
   runtime per PH5-1-LIVE-REFUSAL-CHECK-CONFIRMATION sha256 `5bb368a3…`).
2. **Anti-pathology** — 12/12 oracle expected-verdict match under the
   four-clause label-set predicate; all six T3 criteria PASS on the
   ideal witness; A6 drift 0.0000 on every component (pilot==final by
   construction); no `boundary_proximity_flag` fires.
3. **Construction transparency** — the intended-vs-measured envelope
   distinction is dispositioned by joint CS+NS memo with TL PASS; the
   +1 incidental is honest shortcut-surface accounting, not a
   construction defect.
4. **Anti-tuning** — no bound, count, blend, or verdict was chosen
   from any Phase 5 run-1, run-2, or run-3 numeric outcome; the
   locked values derive from contract semantics, shell construction,
   declared cap structure, and the documented format-cliff class.
5. **E11 / PH5-5 discipline** — three superseded runs retained in
   full; reasons enumerated; changed fields cumulatively documented;
   a D3 PASS erases nothing.

CS recommends Manager review the joint package and decide on D3
acceptance. CS does not request a particular D3 outcome; this package
furnishes the evidence base.

## §9. Confirmation: no model invoked

**CONFIRMED.** No model has been invoked at any point in the D2
implementation, the PH5-1 lock event, the live refusal check, the
corrective run-3 execution, the incidental-hit disposition, or this
D3 package filing. Source-level guarantee carried by
`test_validation_source_no_model_imports` and
`test_oracle_cases_source_no_model_imports`.

## §10. Confirmation: no sweep_id created

**CONFIRMED.** No sweep_id created; no sweep configuration generated
or stored.

## §11. Confirmation: no sweep execution

**CONFIRMED.** No sweep execution occurred. No batched or distributed
candidate generation initiated.

## §12. Confirmation: LOCK-RECORD remains PENDING

**CONFIRMED.** LOCK-RECORD remains PENDING. This D3 review package is
instrument-validation evidence under the D2 model-free boundary. D3
acceptance is a Manager decision and is not requested or pre-empted
by this filing.

All downstream gates remain CLOSED: D4 sweep authorization; D5
close-out; model runs; model loading; new sweep_id; sweep execution;
token-prior model generations; scrambled-binding model generations;
candidate/model outputs; candidate selection; ranking; threshold
work; certification evaluation; stress-retention testing; Claim C
activation; public benchmark packaging.

---

## Appendix A — Reading order for Manager review

1. Start here: **this package (§1–§8)** for the consolidated view.
2. `governance/2026-06-11_lane-1a-prime/PH5-1-JOINT-LOCK-EVENT-RECORD-v0.2.md`
   for the locked semantics and the three hash-bound artifacts.
3. `PHASE5-v0.2-CORRECTIVE-RUN3-COMPLETION-SUMMARY.md` for the run-3
   detailed result tables (per-policy hit rates, T3 dispositions,
   oracle expected-vs-actual, A6 drift block).
4. `validation/instrument_validation_report.md` for the IVR in canonical
   form (Synthetic/Diagnostic labeled; all standing-addendum §9
   sections present).
5. `RUN3-INCIDENTAL-STRUCTURAL-HIT-DISPOSITION-v0.1.md` and
   `NEW-SENIOR-COUNTERSIGN-RUN3-INCIDENTAL-DISPOSITION-v0.1.md` for the
   incidental-hit disposition (joint).
6. `superseded_run-{1,2,3}/RUN-*-RETENTION.md` for the supersession
   ledger and pilot iteration history.
7. `PH5-1-LIVE-REFUSAL-CHECK-CONFIRMATION-v0.1.md` for the live
   integrity verification of the PH5-4 refusal machinery.

## Appendix B — Standing carry (non-authorizations, verbatim)

This D3 review package does not authorize: D3 acceptance; D4 sweep
authorization; D5 close-out; model runs; model loading; new sweep_id;
sweep execution; token-prior model generations; scrambled-binding
model generations; candidate/model outputs; candidate selection;
ranking; threshold work; certification evaluation; stress-retention
testing; Claim C activation; public benchmark packaging.

All model-touching and sweep-execution gates remain CLOSED. D3 is a
Manager decision; this filing furnishes evidence only.

— CS Engineer, 2026-06-11
