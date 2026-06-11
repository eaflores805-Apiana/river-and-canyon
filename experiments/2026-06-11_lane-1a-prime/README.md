# Lane 1a′ Experiment Workspace — D2 Phase 1

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION

D2 IMPLEMENTATION ARTIFACT
NO MODEL INVOKED
NO SWEEP_ID CREATED
NO SWEEP EXECUTION AUTHORIZED
NO CANDIDATE/MODEL OUTPUTS
```

## Purpose

This directory is the code workspace for the Lane 1a′ packet-stage
implementation under D2 authorization. It is a D2 implementation
workspace only; the directory name does not imply a sweep_id, and no
sweep is bound here.

Governance home: `governance/2026-06-11_lane-1a-prime/`.
Authority: Manager D2 authorization (2026-06-11; commit `3398fa9`);
joint disposition set approved at commit `019a964`; Phase 1 authorized
by Team Lead direction of 2026-06-11.

## Phase 1 scope (this commit)

- `schemas/manifest_schema.yaml` — JSON Schema for manifest records
  per CS-EP v0.2 §4 (closes IS-2: real-pair-block boundary fields).
- `schemas/sidecar_schema.yaml` — JSON Schema for runner-attested and
  diagnostic sidecars per CS-EP v0.2 §5/§5.1 (closes AL-Q4 diagnostic
  sidecar; closes AL-Q2-schema Layer 2 via closed-enum on
  `elimination_label_basis.basis_policies`).
- `schemas/rung_result_schema.yaml` — JSON Schema for per-rung result
  records per joint disposition INH-2 (three-way outcome:
  `inconclusive_not_actionable | eliminated | not_ruled_out`; six
  descriptive elimination labels; `boundary_proximity_flag` as
  diagnostic-only per-criterion field).
- `schemas/lock_record_schema.yaml` — JSON Schema for LOCK-RECORD
  per LOCK-RECORD v0.2 §2 + §2.1 (PENDING state; sweep_id null;
  validation_artifact_hashes sub-block; control_prompt_shell_hash
  field).
- `tests/test_schemas.py` — pytest suite: per-schema validity tests +
  cross-schema invariants (no `fails` token; no `passes` token;
  `scrambled_binding_retrieval` structurally unrepresentable in any
  elimination basis; `copy_completion` correctly absent from union
  envelope basis; artifact-label vocabulary matches E15).

## What is NOT in Phase 1

- No runner / wrapper / policy / control / analysis / outcome-chooser
  Python source (Phases 2–4).
- No pilot manifest construction (Phase 5; model-free, but later
  phase).
- No oracle pre-flight (Phase 5).
- No A6 re-verification execution (Phase 5).
- No model invocation. Ever.
- No `sweep_id`. Stays `null` throughout D2.
- No SEALED LOCK-RECORD.

## Standing-governance compliance

This workspace operates under:

- Pre-Lock Instrument Validation Addendum (`governance/standing/`)
- R6 requirement-inheritance check
- Path Conventions rule (this directory follows
  `experiments/<date>_<lane>/`)
- G1-open production rule
- Sibling-artifact cross-reference rule
- Production-path subprocess smoke test rule
- "Supersede, don't rewrite" governance rule

## Boundary statement

Every artifact in this directory inherits the banner above. No
artifact produced here is candidate evidence, threshold support,
certification evidence, or model-capability evidence. The Lane 1a′
doctrine — *may rule out; may not rule in; no survivor ranking; no
positive candidate-selection inference* — applies to every output.

— CS Engineer, 2026-06-11
