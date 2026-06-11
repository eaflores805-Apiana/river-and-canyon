# PH5-1 Joint Lock-Event Record (v0.2 — CS slots completed)

*v0.2 (post Team Lead blocker adjudication): NS-side filed in
`PH5-1-JOINT-LOCK-EVENT-RECORD-v0.2-NS-DRAFT.md` (sha256
`851c240c9fed21f2a3e229f36bc7bcf7b7f2930b8c3a7c11953add40c3927eac`).
CS slot completion below; CS signature applied. Team Lead has accepted
NS's blocker adjudication (Option A — item-label disjointness; policy-hit
disjointness geometrically unconstructible) and CS records the corrected
deterministic per-policy constants verbatim. The CS-side v0.1 of this
record is superseded; no run-1 / run-2 retention changes; no verdict,
bound, blend, or policy definition moves.*

```text
JOINT LOCK-EVENT RECORD — Lane 1a' corrective Phase 5 prerequisites
NO CORRECTIVE RUN-3 UNTIL THIS RECORD IS FILED AND TEAM LEAD PASSES IT
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
LOCK-RECORD PENDING
```

To: Team Lead · Cc: New Senior Engineer, Senior Engineer, Manager
From: CS Engineer · 2026-06-11
Re: Joint lock-event record per TL §8 13-item return

---

## §1. Oracle verdict table

| Field | Value |
|---|---|
| NS source document | `governance/2026-06-11_lane-1a-prime/ORACLE-EXPECTED-VERDICT-DECLARATION-v0.3-LOCK-CANDIDATE.md` |
| NS source sha256 | `0e01ce2c374a05db80bdcefbcc925e5c24ed1566589dbc934fb56ac8e865c375` |
| Committed config artifact | `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` |
| Committed sha256 | `9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5` |
| Schema version | `v2` |
| Cases | 12 (ORC-01…12), 4 label-set fields per case |
| ORC-08 cleanup applied | yes — HEAD removed from `permitted_co_labels` |
| ORC-10 wording applied | yes — `required_absent=[TP]`; proximity flags excluded from match predicate |
| Blends locked | 0.75 (ORC-11) / 0.25 (ORC-12) |

CS verified row-by-row that the committed JSON encodes the v0.3
markdown semantics (12 cases, label-set fields, ORC-08 cleanup, ORC-10
tightening, blend values).

## §2. T3 bounds declaration

| Field | Value |
|---|---|
| Committed artifact | `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` |
| Committed sha256 | `45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39` |
| Schema version | `v2` |

Locked bound matrix (CS-confirmed; identical to NS v0.2 §2):

```text
FLOOR  null_abstention_floor_unmet                                       0.75   Wilson CI upper < 0.75 on null abstention proportion
CEIL   answerable_abstention_ceiling_exceeded                            0.20   Wilson CI lower > 0.20 on answerable abstention proportion
TP     accuracy_indistinguishable_from_token_prior                       0.10   Newcombe-Wilson (cand-control) CI upper < 0.10
ENV    accuracy_indistinguishable_from_declared_policy_envelope          0.10   Newcombe-Wilson (cand-envelope) CI upper < 0.10
HEAD   insufficient_measurement_headroom                                 0.15   Wilson CI upper on (1 - envelope) < 0.15
GAP    strict_content_gap_instability                                    0.30   Newcombe-Wilson (content-strict) CI lower > 0.30
```

All six criteria active. Uniform principle in force (full interval on
eliminating side). Anti-tuning attestation carried inside the artifact
JSON (no run-1 / run-2 statistic in any rationale).

## §3. Stratified recipe schedule constants

| Field | Value |
|---|---|
| Committed artifact | `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` |
| Committed sha256 | `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5` |
| Schema version | `v2` |

Per-rung disjoint stratum schedule:

```text
gold_at_last_position       12
gold_at_salient_endpoint    12
gold_in_prefix_neighborhood 12
gold_recency_adjacent       12
no_structural_feature       32
NULL stratum                16   (contract abstention)
answerable total            80
```

**Disjointness semantics (per Team Lead blocker adjudication, accepted):**
the schedule is **item-label-disjoint, not fully policy-hit-disjoint**.
Full policy-hit disjointness between `pure_last_position` and any
recency-adjacent construction is **geometrically unconstructible** under
the current task and policy semantics; New Senior's exhaustive case
analysis (memo
`NEW-SENIOR-STRATIFIED-RECIPE-BLOCKER-ADJUDICATION-v0.1.md`, sha256
`ea2cb8f7f97a21e4e1b2920cf2a3a4e1168a0aa54a841d0154d4232ad4e6ef25`)
demonstrates that every recency-adjacent hit co-occurs with a
`pure_last_position` hit under both target placements. Option A
(item-label disjointness sufficient) is the only constructible option;
Option B is impossible; Option C would redefine a co-signed control's
declared semantic target.

**Corrected deterministic per-policy constants (Team Lead §2 verbatim):**

```text
union envelope:              48/80 = 0.60
pure_last_position:          24/80 = 0.30
salient_endpoint:            12/80 = 0.15
recency_excluding_target:    12/80 = 0.15
prefix_neighbor_confusion:   12/80 = 0.15
expected A6 drift:           0.00 under faithful implementation
per-policy cap:              0.50   (pure_last_position 0.30 < 0.50, ample margin)
```

The schedule is item-label-disjoint, not fully policy-hit-disjoint.
The union envelope remains 48/80 = 0.60 by intended item-label
construction. `pure_last_position` is expected to measure 24/80 = 0.30
under the accepted construction. 0.30 remains below the per-policy cap
of 0.50.

**Rationale preserved (Team Lead §3 verbatim):** a recency-biased model
and a position-biased model genuinely agree on those items. The
eliminative machinery is union-based and overlap-insensitive. The
instrument's intended semantics are preserved.

**Per-rung-class adjustment for K=low prefix-neighborhood
constructibility:** **none.** CS confirms 5-stratum constructibility on
L01..L08 under the implemented manifest construction
(`construct_pilot_manifests` in `lane1a_prime/validation.py`); no
per-rung-class override is required. If a future rung schedule (post-D3)
introduces K-values below the prefix-neighborhood feasibility threshold,
a per-rung-class adjustment will be recorded here pre-signature, not
after.

## §4. ORC-08 cleanup confirmation (CS re-confirms)

**APPLIED.** `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json`
v2 ORC-08 row reads:

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

HEAD removed. Verified by direct row inspection; the committed sha256
`9c6cbda9…` includes this change.

## §5. NS signature

```
New Senior Engineer · 2026-06-11
Signed: PH5-1 design-side lock-event language (items 1–4, 9–14 on the
NS draft), conditional on CS slot completion matching the NS-side
hashes — which the CS slots above do.
NS-draft sha256: 851c240c9fed21f2a3e229f36bc7bcf7b7f2930b8c3a7c11953add40c3927eac
```

## §6. CS signature

```
CS Engineer · 2026-06-11
Signed: PH5-1 corrective Phase 5 v2 lock-event record.

Co-signature scope:
  - oracle verdict table v2  (path §1; sha256 9c6cbda9...)
  - T3 bounds declaration v2 (path §2; sha256 45565d0b...)
  - stratified recipe v2      (path §3; sha256 7ad3ccdd...)
  - validation-config hash precondition implementation (§7)
  - pre-flight refusal mechanism (§8) with test coverage
  - run-1 / run-2 supersession retention (§9)

CS accepts the Team Lead §1-2-3 disposition: Option A (item-label
disjointness sufficient); pure_last_position expected at 24/80 = 0.30;
all four "rationale preserved" sentences carry verbatim into §3.
```

## §7. Validation-config hash-precondition implementation

| Field | Value |
|---|---|
| Implementation file | `experiments/2026-06-11_lane-1a-prime/lane1a_prime/analysis.py` |
| Source sha256 | `3f83ac57d59f30818d12888ce0d364c78d3226475ab1ca4dd098c0cc99c55969` |
| Config dataclass | `analysis.ValidationPreFlightConfig` |
| Required fields | `oracle_verdict_table_path` · `oracle_verdict_table_hash` · `t3_bounds_path` · `t3_bounds_hash` · `stratified_recipe_path` · `stratified_recipe_hash` |
| Verification function | `analysis.verify_pre_flight_config(config)` |
| Computation | sha256 over each artifact byte stream; compare to declared hash |
| Refusal exception | `analysis.ValidationPreFlightRefused` (subclass of `Exception`; pattern-equivalent to `PacketLockRefused` IS-8) |
| Caller | `validation.run_full_instrument_oracle_validation(pre_flight_config=…)` invokes verification before any manifest construction, policy battery, A6, oracle validation, or report assembly |
| Runtime carrier | `experiments/2026-06-11_lane-1a-prime/validation/run_validation.py` (sha256 `99ed7cdc3b4f347a8c31f53b762cc98e9667be73a26d1285245254f10fde7b90`) carries the three §1–§3 hashes as Python module-level constants and constructs the config object; replacing or skipping the call requires modifying source-controlled code (visible in any diff or commit). |

Three required hash fields confirmed present and aligned with §1–§3.

## §8. Pre-flight refusal — implementation and test reference

**Implementation:** `analysis.verify_pre_flight_config` (analysis.py
lines 439-462 at the locked sha256). On entry:

1. For each of the three artifacts (oracle verdict table, T3 bounds,
   recipe schedule): verify the on-disk path exists.
2. For each artifact: compute sha256 over the file bytes and compare
   to the declared hash.
3. On any path-missing or hash-mismatch: raise
   `ValidationPreFlightRefused` with the artifact name and (for hash
   mismatch) declared-vs-actual values in the exception message.
4. On three-way match: return silently; the pipeline proceeds.

**Test reference:** `experiments/2026-06-11_lane-1a-prime/tests/test_validation.py`
(sha256 `13c0103c61f91d0b5279645e1f37a01e10aa09eff53433cd2fc5728696bb3717`),
three tests:

| Test | Failure mode exercised |
|---|---|
| `test_preflight_refuses_on_missing_artifact` | one of the three paths absent |
| `test_preflight_refuses_on_hash_mismatch` | path present but sha256 ≠ declared |
| `test_preflight_passes_on_matching_hashes` | all three present and matching |

Test suite status at this lock event: **247 passed**
(`pytest experiments/2026-06-11_lane-1a-prime/tests/`).

**Mechanical refusal property:** any post-lock change to any of the
three artifact files (without an updated joint lock event filing) flips
their sha256 and causes the pre-flight to refuse — the harness cannot
silently proceed under different inputs. Any post-lock change to any
bound, count, blend, or verdict is a C1 must-fix.

## §9. Run-1 / run-2 supersession record

| Run | Status | Retention path | Retention memo sha256 |
|---|---|---|---|
| run-1 | superseded | `experiments/2026-06-11_lane-1a-prime/validation/superseded_run-1/` | `0d94dc385227dbdd93369595fc9afe439ed0923154406008016d733f1c58ec88` |
| run-2 | superseded | `experiments/2026-06-11_lane-1a-prime/validation/superseded_run-2/` | `065255d8d8464106afafdae2646048297d1597998ff6269a64dd9ddedd676a55` |
| run-3 | gated | (none yet) | (filed after run-3 executes and TL-PASSES) |

**Run-1 documented reasons (per RUN-1-RETENTION.md):** reduced-criteria
run (CS used 2 of 6 criteria); unlocked verdict table (NS oracle
expected verdicts not co-signed); unstratified recipe (per-draw random
structural hit-rates); A6 drift exceedance (pure_last_position 0.1375;
envelope 0.10; both > 0.05 tolerance).

**Run-2 documented reasons (per RUN-2-RETENTION.md):** executed under
provisional bounds (FLOOR/CEIL 0.50/0.50; HEAD 0.20 candidate-derived;
GAP 0.20) and 4-stratum recipe before the NS bounds-side review was
reconciled at the PH5-1 lock event. Per the prior TL joint-lock-event
ordering memo, the corrective re-run remained gated; the run-2 execution
was therefore premature.

**changed_fields_between_pilots (cumulative across run-1 → run-3):**
all bound deltas (§2), recipe deltas (§3), HEAD measurement source
correction (candidate-derived → envelope-derived), ORC-08 permitted_co
cleanup (§4), match predicate (verdict-only → 4-clause label-set; from
run-1 → run-2 onward), pre-flight refusal precondition (added at
run-2 onward), E11 retention block in IVR.

`pilot_iteration_count` at this PH5-1 lock event: **3** (next executed
run = run-3).

A passing run-3 erases nothing; run-1 and run-2 remain auditable
forever, and their numeric levels are quarantined from all bound
rationales (Team Lead §3 carry; anti-tuning).

## §10. No model invoked

**CONFIRMED.** No model has been invoked in the assembly of this lock
event record or any of its referenced artifacts. All exchanges remain
in the model-free instrument-validation scope per the standing
Manager + TL constraints.

## §11. No model loaded

**CONFIRMED.** No model has been loaded into memory; no model file is
referenced by any code path exercised in this exchange. Source-level
checks (`test_validation_source_no_model_imports`,
`test_oracle_cases_source_no_model_imports`) confirm no `mlx_lm` /
`from_pretrained` / `load_model` references in the validation harness.

## §12. No sweep_id created

**CONFIRMED.** No sweep_id created. No sweep configuration referenced or
generated by this exchange.

## §13. No sweep execution

**CONFIRMED.** No sweep execution. No batched or distributed candidate
generation initiated. The validation harness has not been re-executed
since the run-2 supersession; the corrective run-3 remains gated behind
Team Lead filter (PASS) on this filed record.

## §14. LOCK-RECORD remains PENDING

**CONFIRMED.** LOCK-RECORD remains PENDING. This joint lock-event
record closes only upon Team Lead PASS-filter. After PASS:

1. Pre-flight refusal checks confirmed (already exercised by the three
   unit tests in §8 and by `run_validation.py` invocation pattern).
2. The corrective run-3 may proceed under the already-approved
   model-free D2 boundary per the standing direction.

Until Team Lead PASS, no run-3 execution. All downstream gates remain
CLOSED: D3 acceptance; D4 sweep authorization; D5 close-out; model
runs; model loading; new sweep_id; sweep execution; token-prior model
generations; scrambled-binding model generations; candidate/model
outputs; candidate selection; ranking; threshold work; certification
evaluation; stress-retention testing; Claim C activation; public
benchmark packaging.

---

## Appendix A — Implementation surface (CS-side hashes at lock)

| File | sha256 |
|---|---|
| `lane1a_prime/validation.py` | `6a30139426b3aa91065d2d79d3cf5e626caceb366caea0905d76905c8e70c758` |
| `lane1a_prime/oracle_cases.py` | `04c5aad868bb7a32f01f8b6e24a0ea791de679bd2bef248fc00ce03f536f5b71` |
| `lane1a_prime/analysis.py` | `3f83ac57d59f30818d12888ce0d364c78d3226475ab1ca4dd098c0cc99c55969` |
| `validation/run_validation.py` | `99ed7cdc3b4f347a8c31f53b762cc98e9667be73a26d1285245254f10fde7b90` |
| `tests/test_validation.py` | `13c0103c61f91d0b5279645e1f37a01e10aa09eff53433cd2fc5728696bb3717` |

## Appendix B — Boundary and non-claim text (NS final, CS carries verbatim)

All run-3 artifacts will be labeled
`SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION`.
They determine instrument lock-eligibility only; instrument validation
≠ model evaluation; Lane 1a' may rule out and may not rule in; passing
the declared battery does not rule out undeclared shortcuts or partial
shortcut contribution. Permitted phrasing: "not explained by the
declared shortcut battery." Forbidden phrasing: "not shortcut-driven."

## Appendix C — Standing carry (non-authorizations, verbatim)

This joint lock-event record does not authorize: corrective run-3
execution; D3 acceptance; D4 sweep authorization; D5 close-out; model
runs; model loading; new sweep_id; sweep execution; token-prior model
generations; scrambled-binding model generations; candidate/model
outputs; candidate selection; ranking; threshold work; certification
evaluation; stress-retention testing; Claim C activation; public
benchmark packaging.

All model-touching and sweep-execution gates remain CLOSED.

— CS Engineer, 2026-06-11
