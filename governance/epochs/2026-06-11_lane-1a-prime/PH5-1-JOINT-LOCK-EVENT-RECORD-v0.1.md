# PH5-1 Joint Lock-Event Record (v0.1)

```text
DRAFT / JOINT REVIEW — CS-SIDE COMPLETE, NS-SIDE PENDING
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
LOCK-RECORD PENDING UNTIL NS+CS BOTH SIGN AND TEAM LEAD FILTERS
CORRECTIVE RE-RUN STILL GATED (per TL §6 of the joint-ordering memo)
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID CREATED · NO SWEEP EXECUTION
```

To: Team Lead · Cc: New Senior Engineer, Senior Engineer, Manager
From: CS Engineer (joint return; NS counter-signature awaited)
Date: 2026-06-11
Re: PH5-1 joint lock-event record per TL §7 14-item return

This memo binds the three lock-event artifacts (oracle verdict table,
T3 bounds declaration, recipe schedule constants) by sha256, records
NS+CS co-signature lines, and codifies the pre-flight refusal
precondition the validation harness honors at runtime. The record
supersedes the earlier `PH5-1-JOINT-LOCK-EVENT-RECORD-2026-06-11.md`,
which referenced the provisional (run-2) artifact hashes.

---

## §1. Oracle verdict table — path and sha256

| Field | Value |
|---|---|
| path | `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` |
| sha256 | `9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5` |
| schema_version | `v2` |
| change vs v1 | ORC-08 `permitted_co_labels` reduced (HEAD removed) per TL §4 cleanup |
| source memo | `NEW-SENIOR-ORACLE-EXPECTED-VERDICT-DECLARATION-v0.2-PROPOSED-2026-06-11.md` |

## §2. T3 bounds declaration — path and sha256

| Field | Value |
|---|---|
| path | `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` |
| sha256 | `45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39` |
| schema_version | `v2` |

Locked bound matrix:

| criterion | bound | comparison | source |
|---|---|---|---|
| null_abstention_floor_unmet | **0.75** | Wilson CI upper < bound | NULL-stratum abstention proportion |
| answerable_abstention_ceiling_exceeded | **0.20** | Wilson CI lower > bound | answerable-stratum abstention proportion |
| accuracy_indistinguishable_from_token_prior | **0.10** | Newcombe–Wilson difference upper < bound | (candidate − control_token_prior) accuracy |
| accuracy_indistinguishable_from_declared_policy_envelope | **0.10** | Newcombe–Wilson difference upper < bound | (candidate − envelope) accuracy |
| insufficient_measurement_headroom | **0.15** | Wilson CI upper < bound | **(1 − envelope_score_answerable)** |
| strict_content_gap_instability | **0.30** | Newcombe–Wilson difference lower > bound | (content − strict) accuracy |

Anti-tuning attestation: every bound derives from contract semantics
(FLOOR/CEIL), shell construction (TP_margin), declared cap structure
(ENV_margin/HEAD), and the documented format-cliff class (GAP). No
value is derived from any Phase 5 run-1 or run-2 numeric outcome.

## §3. Recipe schedule constants — path and sha256

| Field | Value |
|---|---|
| path | `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` |
| sha256 | `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5` |
| schema_version | `v2` |

Per-rung disjoint stratum schedule:

| stratum | count | rate |
|---|---|---|
| gold_at_last_position | 12 | 0.15 |
| gold_at_salient_endpoint | 12 | 0.15 |
| gold_in_prefix_neighborhood | 12 | 0.15 |
| gold_recency_adjacent | 12 | 0.15 |
| no_structural_feature | 32 | 0.40 |
| (NULL stratum) | 16 | — |
| **answerable total** | **80** | — |

Construction consequences: union envelope = 48/80 = 0.60 exactly under
the disjoint-item assignment; (1 − envelope) headroom = 0.40 — well
above the locked HEAD bound 0.15.

**BLOCKER — requires Team Lead decision before lock:**
under the current `recency_excluding_target` policy definition (emits
`candidates_excluding_queried_key[-1].value`), the `gold_recency_adjacent`
stratum's construction (last non-target pair value = gold) also causes
`pure_last_position` to hit those 12 items, because `pure_last_position`
emits `pairs[-1].value` which equals the last non-target pair's value
when queried is not at last. The disjointness is therefore at the
ITEM-LABEL level (each item carries exactly one feature label as the
schedule prescribes), not at the POLICY-HIT level.

Three possible resolutions for NS+TL:
- (a) Accept the policy-level overlap: `pure_last_position` total
  measured hit-rate becomes 12/80 (gold_at_last_position) + 12/80
  (gold_recency_adjacent incidental) = 0.30; envelope stays 0.60;
  per-policy designated-stratum hit-rate is unchanged at 12/80 each.
  The structural cap [0.06, 0.20] from D2 v0.1 is exceeded for
  `pure_last_position` only.
- (b) Redefine `recency_excluding_target` policy to "second-most-recent
  non-target pair" so its hit stratum can be constructed without
  position-`[-1]` value coincidence — preserves disjointness at the
  policy-hit level but is a policy redefinition.
- (c) Drop the `gold_recency_adjacent` stratum from the schedule and
  reallocate to a 4-stratum schedule (12/12/12/12 = 48 plus 32 no-feature);
  recency_excluding_target's hit rate stops being structurally pinned.

CS has implemented option (a) as the default so the harness is testable
under the locked artifacts; the BLOCKER stays open until NS+TL elect.
A choice does not change the lock-event hashes if the change is in the
policy definition (option b) or in the manifest construction (would
require recipe schedule sha256 to change). Option (a) leaves the
artifacts as hashed.

## §4. ORC-08 HEAD permitted_co_label cleanup — applied

**APPLIED.** The `ORACLE_VERDICT_TABLE.json` v2 ORC-08 row reads:

```json
{
  "required_labels": ["answerable_abstention_ceiling_exceeded"],
  "permitted_co_labels": [
    "accuracy_indistinguishable_from_token_prior",
    "accuracy_indistinguishable_from_declared_policy_envelope"
  ],
  "required_absent_labels": []
}
```

`insufficient_measurement_headroom` removed from permitted_co_labels.
Rationale: under the v2 HEAD semantic (envelope-derived), HEAD
evaluates a manifest property and never depends on the oracle candidate;
with envelope = 0.60 by the locked schedule, HEAD never attaches to any
oracle case, so the prior permission was dead. Per TL §4 cleanup
direction.

## §5. NS signature

```
[ AWAITING NEW SENIOR CO-SIGNATURE ]

New Senior may sign on review of this CS-side return. The CS-side hashes
and 14 items are final; NS may sign verbatim or return narrow edits
through the joint-review step prior to signature.
```

## §6. CS signature

```
CS Engineer · 2026-06-11
Signed: corrective Phase 5 v2 lock-event record
Co-signature scope: oracle verdict table v2 (sha256 9c6cbda9…),
                    T3 bounds declaration v2 (sha256 45565d0b…),
                    stratified recipe schedule v2 (sha256 7ad3ccdd…),
                    pre-flight refusal precondition wired in
                    run_validation.py and verify_pre_flight_config.
```

## §7. Validation-config hash-precondition description

The validation harness (`validation/run_validation.py`) carries the
three lock-event sha256 hashes (§1–§3 above) as Python module-level
constants. Before any manifest construction, policy battery, A6
re-verification, oracle validation, or report assembly is performed,
the runtime calls `verify_pre_flight_config()` (in `lane1a_prime.analysis`)
with a `ValidationPreFlightConfig` dataclass whose four fields are:

```python
ValidationPreFlightConfig(
    oracle_verdict_table_path=Path(".../ORACLE_VERDICT_TABLE.json"),
    oracle_verdict_table_hash="9c6cbda9...",
    t3_bounds_path=Path(".../T3_BOUNDS_DECLARATION.json"),
    t3_bounds_hash="45565d0b...",
    stratified_recipe_path=Path(".../STRATIFIED_RECIPE_SCHEDULE.json"),
    stratified_recipe_hash="7ad3ccdd...",
)
```

`verify_pre_flight_config` computes the sha256 of each on-disk file and
raises `ValidationPreFlightRefused` (subclass of `PacketLockRefused`)
if any of the three hashes does not match. On match, stdout prints
`PH5-4 pre-flight: PASSED (all lock-event artifact hashes match)` and
the pipeline proceeds. On mismatch, no manifests are constructed, no
oracle cases run, and no reports are written — the run aborts with the
operation-equivalent hard refusal pattern (PacketLockRefused).

## §8. Pre-flight refuses without all required hashes

**CONFIRMED.** Three independent failure modes are exercised:

1. File missing (any of the three paths absent): `FileNotFoundError`
   raised before hash computation.
2. File present but hash mismatch (any of the three hashes wrong):
   `ValidationPreFlightRefused` raised inside `verify_pre_flight_config`
   with the field name and expected-vs-actual hashes in the message.
3. Hash present in code but file mutated post-lock: same path as (2).

In all three modes, no manifests are constructed, no policy battery
runs, no A6 check executes, no oracle cases run, and no reports are
written. The validation harness honors the lock-event preconditions as
a hard refusal at the earliest possible point in the pipeline.

## §9. Supersession record for run-1 and run-2

| Run | Status | Location | Retention memo |
|---|---|---|---|
| run-1 | superseded | `validation/superseded_run-1/` | `RUN-1-RETENTION.md` (sha256 `0d94dc38...`) |
| run-2 | superseded | `validation/superseded_run-2/` | `RUN-2-RETENTION.md` (sha256 `065255d8...`) |
| run-3 | gated | (none yet) | (to be filed after run-3 executes) |

Each retention block enumerates `pilot_iteration_count`,
`reason_for_each_repilot`, and `changed_fields_between_pilots`. No
run-1 or run-2 artifact is deleted or modified.

`pilot_iteration_count` at this PH5-1 lock event: **3** (the next
executed run will be run-3).

## §10. No model invoked

**CONFIRMED.** No model has been invoked in the assembly of this lock
event record or any of its three referenced artifacts. The entire
exchange remains in the model-free instrument-validation scope per the
Manager + TL standing constraints.

## §11. No model loaded

**CONFIRMED.** No model has been loaded into memory, no model file is
referenced by any code path exercised in this exchange, and no
mlx_lm / from_pretrained / load_model references exist in the
validation harness (enforced by `test_validation_source_no_model_imports`
and `test_oracle_cases_source_no_model_imports`).

## §12. No sweep_id created

**CONFIRMED.** No sweep_id has been created. No sweep configuration is
referenced or generated by this exchange.

## §13. No sweep execution

**CONFIRMED.** No sweep execution has occurred. No batched or
distributed candidate generation has been initiated. The validation
harness has not been re-executed since the run-2 supersession; the
corrective run-3 remains gated behind the joint-lock + TL-filter
sequence per TL §6 of the joint-ordering memo.

## §14. LOCK-RECORD remains PENDING

**CONFIRMED.** LOCK-RECORD remains PENDING. This joint lock-event
record closes only on:

1. NS counter-signature on the three sha256s and the §3 BLOCKER
   resolution.
2. Team Lead filter (PASS) on the filed record.
3. After (1) and (2) the corrective run-3 may proceed under the
   already-approved model-free D2 boundary per TL §6.

Until then, no run-3 execution. All downstream gates (D3 acceptance;
D4 sweep authorization; D5 close-out; model runs; model loading; new
sweep_id; sweep execution; token-prior model generations;
scrambled-binding model generations; candidate/model outputs; candidate
selection; ranking; threshold work; certification evaluation;
stress-retention testing; Claim C activation; public benchmark
packaging) remain CLOSED.

---

## Appendix A — Implementation surface (CS-side hashes)

For audit:

| File | sha256 |
|---|---|
| `lane1a_prime/validation.py` | `6a30139426b3aa91065d2d79d3cf5e626caceb366caea0905d76905c8e70c758` |
| `lane1a_prime/oracle_cases.py` | `04c5aad868bb7a32f01f8b6e24a0ea791de679bd2bef248fc00ce03f536f5b71` |
| `validation/run_validation.py` | `99ed7cdc3b4f347a8c31f53b762cc98e9667be73a26d1285245254f10fde7b90` |
| `tests/test_validation.py` | `6bdf3af0bc5f05e992cc123ebf70b48f630dd6bb1844b597d41713c7eec76eae` |
| `validation/superseded_run-2/RUN-2-RETENTION.md` | `065255d8d8464106afafdae2646048297d1597998ff6269a64dd9ddedd676a55` |

Test suite status at this lock event: **244 passed** (single
`pytest experiments/2026-06-11_lane-1a-prime/tests/` invocation).

## Appendix B — Standing carry (verbatim)

This joint lock-event record does not authorize: corrective run-3
execution; D3 acceptance; D4 sweep authorization; D5 close-out; model
runs; model loading; new sweep_id; sweep execution; token-prior model
generations; scrambled-binding model generations; candidate/model
outputs; candidate selection; ranking; threshold work; certification
evaluation; stress-retention testing; Claim C activation; public
benchmark packaging.

All model-touching and sweep-execution gates remain CLOSED.

— CS Engineer, 2026-06-11
