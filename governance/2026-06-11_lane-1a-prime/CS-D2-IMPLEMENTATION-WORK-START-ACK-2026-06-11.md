# CS D2 Implementation Work-Start Acknowledgement — Lane 1a′

```text
DRAFT / REVIEW ONLY
D2 PACKET-PREPARATION + IMPLEMENTATION ARTIFACT
NO D3 / D4 / D5 ACCEPTANCE
NO MODEL RUNS AUTHORIZED
NO SWEEP_ID CREATED
NO SWEEP EXECUTION
NO CANDIDATE / MODEL OUTPUTS PRODUCED
```

From: CS Engineer
To: Team Lead, Manager
Cc: New Senior Engineer, Senior Engineer, Contributor 5, Contributor 6
Date: 2026-06-11
Re: D2 code implementation + model-free validation work authorization received; CS work-start acknowledgement
Status: D2 implementation scope confirmed; CS proposes phased implementation plan; awaits user direction on Phase 1 start

---

## 1. Authorization received

```text
Joint D2 disposition set:           APPROVED (Manager + Team Lead)
Code implementation under D2:       AUTHORIZED (writing source; not invoking against model)
Model-free validation scope:        CONFIRMED (pilot construction; deterministic
                                     policy execution; oracle pre-flight; A6;
                                     T1-T4 result population; Validation Report)
Execution ledger requirement:       NOTED (required with first model-free
                                     validation return)
D3 / D4 / D5:                       NOT GRANTED
```

## 2. CS scope under this authorization

### Authorized

| Category | Activity | Notes |
|---|---|---|
| Code | runner source; wrapper source; schemas; policy modules; control modules; A6 machinery; lock_packet machinery; tests; dry-run interface checks; non-executing packet infrastructure | Source code only. No model invocation. |
| Validation (model-free) | pilot manifest construction; deterministic dummy-policy execution against pilot manifests; oracle-case pre-flight against synthetic/oracle records; A6 final-manifest re-verification; T1–T4 validation result-field population; Instrument Validation Report preparation | All offline. All artifacts carry `SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION` per §8 of the joint memo. |

### Still prohibited

```text
- Invoking any model (no subprocess against runner that triggers model load).
- Creating a sweep_id (LOCK-RECORD identity.sweep_id stays placeholder).
- Sweep execution.
- unconditioned_token_prior model generation (D4 by-name only).
- scrambled_binding_retrieval model generation (no D2 authorization).
- Candidate selection / ranking / threshold / certification / retention work.
- Modifying B1 v2 source (sibling-artifact rule).
- Modifying Paper 3 v1.1 release bytes (locked tag).
- Touching tier0-run/ (sealed).
- Sealing LOCK-RECORD.
- Producing artifacts labeled RECONNAISSANCE (those carry real model output; not produced under D2).
```

## 3. Proposed implementation plan (5 phases)

CS proposes the following phased plan. Phase boundaries are natural
check-in points for user review/redirection.

### Phase 1 — Foundation (manifest schema + experiment directory)

**Goal:** establish the data shape everything else depends on.

| Item | Deliverable |
|---|---|
| 1.1 | Create `experiments/2026-06-11_lane-1a-prime/` directory (per adopted Path Conventions rule; under D2 it is no longer provisional). |
| 1.2 | `experiments/2026-06-11_lane-1a-prime/schemas/manifest_schema.yaml` — JSON Schema for `manifest_record` per CS-EP v0.2 §4 (incorporates IS-2 real-pair-block boundary fields). |
| 1.3 | `experiments/2026-06-11_lane-1a-prime/schemas/sidecar_schema.yaml` — `runner-attested sidecar` + `diagnostic_sidecar` patterns per CS-EP v0.2 §5/§5.1 (closes AL-Q4). |
| 1.4 | `experiments/2026-06-11_lane-1a-prime/schemas/rung_result_schema.yaml` — per-rung result with `elimination_label_basis` enum + `boundary_proximity_flag` diagnostic field; `additionalProperties: false` (closes AL-Q2-schema). |
| 1.5 | `experiments/2026-06-11_lane-1a-prime/schemas/lock_record_schema.yaml` — full LOCK-RECORD v0.2 schema + `validation_artifact_hashes` sub-block + `control_prompt_shell_hash` field. |
| 1.6 | Test stub: `tests/test_schemas.py` — schema validates valid records; rejects records carrying control names in elimination basis; rejects records carrying any `fails` token. |

### Phase 2 — Deterministic core (policies + controls)

**Goal:** implement the policies (deterministic) and the control modules (T2 specs only; no model invocation).

| Item | Deliverable |
|---|---|
| 2.1 | `lane1a_prime/policies.py` — five policy implementations: `pure_last_position`, `salient_endpoint`, `recency_excluding_target`, `prefix_neighbor_confusion`, `copy_completion` |
| 2.2 | `PolicyInputView` interface per CS-EP v0.2 §6 (DE-1 blinding via construction). |
| 2.3 | Total-function definition for `prefix_neighbor_confusion` (4 clauses; token-id-sequence equality after tokenizer canonicalization; closes IS-9). |
| 2.4 | `lane1a_prime/controls.py` — control specs only (T2 declarations; no model invocation path). `LabelInput` / `ControlOutput` typed boundary per CS-EP v0.2 §7. |
| 2.5 | Tests: `test_policy_view_excludes_queried_key`; `test_label_input_does_not_carry_control_outputs`; `test_emit_elimination_label_signature`; `test_diagnostic_sidecar_disjoint_from_envelope`; `test_no_fails_token_in_any_output`. |

### Phase 3 — Outcome chooser + analysis script

**Goal:** implement the three-way INH-2 outcome model + INH-1 stratum aggregation + INH-3 Wilson CI.

| Item | Deliverable |
|---|---|
| 3.1 | `lane1a_prime/outcome.py` — `RungOutcome` enum (three-way); `EliminationLabel` enum (six descriptive values); `compute_rung_outcome()` with exhaustiveness property test. |
| 3.2 | `lane1a_prime/analysis.py` — per-stratum aggregation (INH-1); Wilson + Newcombe-Wilson CI (INH-3); `CriterionComparison` enum. |
| 3.3 | Fixed-language constants for K=0, K=1, K≥2 statements (with "not ruled out" wording per joint disposition). |
| 3.4 | Tests: `test_outcome_enum_has_no_passes_value`; `test_emit_outcome_statement_uses_fixed_constants`; `test_no_other_ci_method_in_analysis` (anti-Wald check); `test_outcome_chooser_exhaustiveness` (every rung maps to exactly one outcome). |

### Phase 4 — Runner + wrapper + lock_packet

**Goal:** runner architecture; production-path subprocess smoke; lock_packet structural refusals.

| Item | Deliverable |
|---|---|
| 4.1 | `lane1a_prime/runner.py` — standalone runner per CS-EP v0.2 §3. `render_prompt()` pure function for dry-run (closes AL-Q1). MODEL_ID `<placeholder>` (locked at packet seal). |
| 4.2 | `lane1a_prime/wrapper.py` — subprocess invocation per Path E.1. PRODUCTION_PYTHON + EXPECTED_MLX_LM_VERSION `<placeholder>`. `--dry-run` flag. `write_sidecar()` byte-disjoint from runner output. |
| 4.3 | `lane1a_prime/lock_packet.py` — A6 `a6_final_manifest_reverification()` (IS-7 drift tolerance); `lock_packet()` with `PacketLockRefused` for operation-equivalent policies (IS-8). |
| 4.4 | Tests: full Path A.1 sibling-artifact cross-reference suite; full Path E.1 production-path subprocess smoke (verifies import surface but does NOT model-load); `test_lock_refuses_operation_equivalent_in_negative_battery`; `test_a6_drift_within_tolerance`. |

### Phase 5 — Model-free validation execution

**Goal:** execute the model-free validation steps and produce the Instrument Validation Report.

| Item | Deliverable |
|---|---|
| 5.1 | Construct pilot manifests under the locked recipe (deterministic seeds; no model). |
| 5.2 | Execute policy battery (A1) against pilot manifests. |
| 5.3 | Execute synthetic oracle cases (A5 pre-flight): ideal retriever; each declared policy; token-prior emitter (synthetic, no model); universal answerer; universal abstainer; NULL-on-NULL handler; one malformed control; ≥1 mixture oracle. |
| 5.4 | Construct final manifests; execute A6 re-verification; compute drift. |
| 5.5 | Populate T1 (battery degeneracy audit) + T3 (pass-region checklist) + T4 (review-to-lock disposition) result fields. |
| 5.6 | Assemble Instrument Validation Report draft. |
| 5.7 | Produce execution ledger per joint memo §9. |
| 5.8 | Final return bundle with required confirmations (no model invoked; no sweep_id; no sweep execution; no candidate/model outputs). |

### Phases 4 and 5 — model invocation boundary

**Critical:** Phase 4 implements the runner module but **does not invoke a
model**. The Path E.1 production-path subprocess smoke test verifies
the import surface (module imports successfully under
PRODUCTION_PYTHON; mlx_lm version matches expected) but does **not**
load a model or generate. Phase 5 does not invoke a model either —
it constructs synthetic data, runs deterministic policies, and
populates validation result fields per the addendum's offline-only
validation discipline.

The `unconditioned_token_prior` control invocation against a real
model is **gated at D4 by name only**. Same for
`scrambled_binding_retrieval`.

## 4. Execution-ledger commitment

Per joint memo §9 and NS materials v0.2 §9b, CS will produce the
execution ledger with the first model-free validation return (Phase 5
deliverable 5.7). Format:

```text
what_was_generated:            <pilot manifests by seed/rung; oracle records>
what_was_computed:             <per-policy vectors/scores; envelope; oracle verdicts; checklist rows>
files_created:                 <paths>
artifact_hashes:               <sha256 per file>
no_model_invoked:              CONFIRMED
no_sweep_id_created:           CONFIRMED
no_sweep_execution:            CONFIRMED
no_candidate_or_model_outputs: CONFIRMED
outputs_validation_only:       CONFIRMED — SYNTHETIC/DIAGNOSTIC, NON-BINDING, NOT FOR THRESHOLD DERIVATION
```

## 5. Standing-governance compliance

CS continues to operate under all standing rules:

- Pre-Lock Instrument Validation Addendum (first applied instance)
- R6 requirement-inheritance check
- Path Conventions rule (governance/ vs experiments/)
- G1-open production rule
- Sibling-artifact cross-reference rule
- Production-path subprocess smoke test rule
- "Supersede, don't rewrite" governance rule
- Standing review-discipline rules (failure-mode prompt; protection-layer taxonomy)

## 6. Coordination items with NS during Phase 1-5

NS may need to provide / confirm during implementation:

| Item | Phase | NS deliverable |
|---|---|---|
| Manifest recipe locked-form (padding placement; novelty rule; deterministic seeds; per-rung void budget; per-item answer-slot recording) | 1, 5.1 | NS specifies; CS implements |
| T1 declared-cap values: per-policy 0.50, envelope 0.80, drift ±0.05 (already declared in NS materials v0.2 §2; CS co-endorsed) | 2, 5.5 | NS values already declared; CS implements |
| T2 control-spec field-level finalization | 2 | NS T2 plan |
| T3 ideal-witness record format finalization | 3, 5.3, 5.5 | NS T3 plan |
| T3 per-criterion comparison declaration (point-estimate / CI lower / CI upper / difference interval) | 3, 5.5 | NS T3 plan |
| Final N + answerable/NULL split + void budget confirmation | 5.1 | NS confirms at packet validation |
| INH-3 Wilson with or without continuity correction (CS proposes without; NS endorsed without) | 3 | already confirmed; CS implements |
| Cross-review of CS code as it lands | 2-5 | NS cross-review per the standing G1-open + sibling-artifact rules |

## 7. Boundaries preserved

```text
No model invocation under any circumstance.
No new sweep_id.
No sweep execution.
No unconditioned_token_prior model generation (D4 by name only).
No scrambled_binding_retrieval model generation.
No candidate / model outputs.
No candidate selection / ranking / threshold / certification / retention work.
No D3 / D4 / D5 implied or solicited.
All artifacts produced under D2 carry SYNTHETIC / DIAGNOSTIC label per §8.
LOCK-RECORD remains PENDING; no SEALED state.
B1 v2 source unedited.
Paper 3 v1.1 release bytes unedited.
tier0-run/ untouched.
```

All execution gates remain CLOSED.

## 8. CS posture

```text
D2 disposition approval:               received (Manager + Team Lead)
D2 code implementation:                AUTHORIZED (source only)
D2 model-free validation:              AUTHORIZED (offline only)
Implementation plan:                   5 phases proposed (§3)
Execution-ledger requirement:          acknowledged (§4)

CS next action:                        proposes starting Phase 1
                                        (manifest + sidecar + rung_result +
                                        LOCK-RECORD schemas + tests)
                                        in next turn
                                        OR holds for user direction on
                                        order/scope.

CS commitment:                          no model invocation; no sweep_id;
                                        no sweep execution; no candidate/
                                        model outputs at any phase

Lane 1a close-out v1.2 (parallel):     CLOSED-PENDING-ADOPTION
                                        (Senior owns)

All execution gates:                   CLOSED
```

**CS proposes proceeding with Phase 1 (schemas + experiment directory
+ test stubs) in the next turn. CS holds for user direction or
"proceed" to begin Phase 1.**

Alternative orderings the user may prefer:
- (A) Start with Phase 1 (schemas + foundation) — CS recommendation
- (B) Start with the lock_packet machinery + tests first (validates the standing rules early)
- (C) Start with the analysis script + outcome chooser (semantics-first within code, parallel to the governance co-drafts)
- (D) Other ordering

— CS Engineer, 2026-06-11
