# LOCK-RECORD Draft Structure v0.2 — Lane 1a′

```text
DRAFT / REVIEW ONLY
D2 PACKAGE-ASSEMBLY ARTIFACT
NO D2 AUTHORIZATION GRANTED
NO EXECUTION AUTHORIZED
NO SWEEP_ID CREATED
NO MODEL RUNS
NO DATA GENERATED
NO VALIDATION OUTPUTS POPULATED
```

From: CS Engineer
To: Team Lead, New Senior Engineer
Cc: Senior Engineer, Contributor 5, Contributor 6, Manager
Date: 2026-06-11
Re: LOCK-RECORD Draft Structure v0.2 — Lane 1a′ (D2 package-assembly artifact)
Status: D2 package assembly — incorporates AL-Q5-opt per-table validation_artifact_hashes sub-block

---

**Supersession record.**
This document supersedes `LOCK-RECORD-DRAFT-STRUCTURE-v0.1.md` (sha256 `6c07d2e7…`). The v0.1 file remains on disk as historical record per "supersede, don't rewrite". v0.2 changes from v0.1 are catalogued in §0 below.

---

## 0. v0.1 → v0.2 changes

| Change | v0.1 location | v0.2 location | Source carry-forward |
|---|---|---|---|
| Banner change (D1 → D2 PACKAGE-ASSEMBLY) | top | top | Team Lead memo of 2026-06-11 §6 |
| Add `validation_artifact_hashes` per-table sub-block | — | **§2.1** | **AL-Q5-opt** |
| §3 field documentation extended for validation_artifact_hashes | §3 | **§3** (extended) | AL-Q5-opt |
| Updated §10 no-population-under-D2 rule | §10 (D1) | **§10** (D2) | banner consistency |

All other content carries from v0.1.

---

## 1. Scope (unchanged from v0.1)

LOCK-RECORD binds the Lane 1a′ packet to a specific hash state at
lock time. Carries addresses of all locked artifacts, addendum /
standing-rule version pins, G1-open check, token-prior authorization
slot (D4), C2 considered-memos enumeration.

Per Team Lead D2 package assembly authorization:

```text
NO LOCK-RECORD hash values are populated under D2 package assembly.
NO sweep_id is created under D2 package assembly.
NO sealed state is reached under D2 package assembly.
```

This document defines the **structure only**.

Authority: Team Lead D2 package assembly authorization of 2026-06-11
(supersedes D1 packet-preparation authority for this v0.2 artifact;
D2 itself remains not granted).

## 2. Schema (YAML skeleton)

```yaml
# governance/2026-06-11_lane-1a-prime/LOCK-RECORD.yaml
# Populated only at packet seal — NOT POPULATED UNDER D2 PACKAGE ASSEMBLY

lock_record:
  schema_version: "v0.2"
  state: PENDING

  identity:
    lock_id: <placeholder>
    lane: "lane-1a-prime"
    sweep_id: <placeholder>            # NOT CREATED UNDER D2 PACKAGE ASSEMBLY
    created_at: <placeholder>
    sealed_at: <placeholder>
    superseded_at: <placeholder>
    superseded_by_lock_id: <placeholder>

  bound_hashes:
    # All hashes are sha256 of the locked artifact bytes.
    # Populated at seal; cross-checked against artifacts on disk.
    design_packet_hash:                <placeholder>   # NS-owned
    t1_plan_hash:                      <placeholder>   # NS-owned
    t2_plan_hash:                      <placeholder>   # NS-owned
    t3_plan_hash:                      <placeholder>   # NS-owned
    t4_plan_hash:                      <placeholder>   # NS-owned
    execution_packet_proposal_hash:    <placeholder>   # CS-owned
    manifest_schema_hash:              <placeholder>   # CS-owned
    manifest_recipe_hash:              <placeholder>
    runner_source_hash:                <placeholder>   # CS-owned
    runner_wrapper_source_hash:        <placeholder>   # CS-owned
    runner_config_hash:                <placeholder>   # CS-owned
    analysis_script_hash:              <placeholder>   # CS-owned
    instrument_validation_report_hash: <placeholder>   # sealed at D3
    non_authorization_section_hash:    <placeholder>   # CS-owned

  bound_versions:
    addendum_path: "governance/standing/PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM.md"
    addendum_sha256:                "124f6046d57d365dd47596877fd1eb09088f6990ec3c9a52ac150d0c8ca103b8"
    addendum_adoption_commit:       "e76e7f8"
    standing_review_discipline_sha256: <placeholder>
    standing_non_authorizations_sha256: <placeholder>
    paper3_tag:                     "paper3-certification-protocol-v1.1"
    mlx_lm_version:                 <placeholder>
    production_python:              <placeholder>
    model_id:                       <placeholder>
    model_snapshot:                 <placeholder>

  # Per New Senior D1 ack item 7 (unchanged from v0.1)
  token_prior_authorization:
    state: NOT_AUTHORIZED            # NOT_AUTHORIZED | AUTHORIZED | DECLINED
    manager_memo_path: <placeholder>
    manager_memo_sha256: <placeholder>
    by_name_decision_text: <placeholder>
    decision_date: <placeholder>
    declined_rationale: <placeholder>

  # Per New Senior D1 ack item 7 + C2 standing rule (unchanged from v0.1)
  c2_considered_memos:
    - memo_id: <placeholder>
      memo_path: <placeholder>
      memo_sha256: <placeholder>
      review_state: <placeholder>
      considered_for_gate: <placeholder>

  g1_open_check:
    timestamp: <placeholder>
    checker: <placeholder>
    g1_open_count: 0
    pending_memo_ids: []
    confirmation: <placeholder>

  r6_inheritance_screen:
    screened_prior_lane_requirements:
      - requirement: <placeholder>
        prior_lane: <placeholder>
        disposition: adopted | adapted | declined
        rationale: <placeholder>

  audit:
    created_at: <placeholder>
    created_by: "CS Engineer"
    sealed_at: <placeholder>
    sealed_by: <placeholder>
    audit_log_hash_at_seal: <placeholder>
    last_modified_at: <placeholder>
```

### 2.1 Validation-artifact hashes (NEW for v0.2, AL-Q5-opt)

Per Team Lead D2 package-assembly carry-forward of AL-Q5-opt, the
LOCK-RECORD adds a per-table `validation_artifact_hashes` sub-block
that breaks down the `instrument_validation_report_hash` into per-
artifact sealed hashes. This produces a finer audit trail at D3
seal:

```yaml
lock_record:
  validation_artifact_hashes:
    # All hashes populated at D3 (Instrument Validation Report seal),
    # not at packet seal. The instrument_validation_report_hash above
    # remains the top-level binding hash; this sub-block provides
    # per-artifact granularity.
    t1_sealed_hash:                    <placeholder>  # populated T1 battery-degeneracy-audit table
    t2_sealed_hash:                    <placeholder>  # populated T2 control-spec sheets (both controls)
    t3_sealed_hash:                    <placeholder>  # populated T3 pass-region checklist
    t4_sealed_hash:                    <placeholder>  # populated T4 dispositions
    ideal_witness_record_hash:         <placeholder>  # T3-locked ideal-witness record
    pilot_iteration_log_hash:          <placeholder>  # E11 log (all iterations retained)
    oracle_case_verdict_table_hash:    <placeholder>  # A5 pre-flight verdicts
    a6_reverification_block_hash:      <placeholder>  # final-manifest re-verification block
    drift_tolerance_declaration_hash:  <placeholder>  # IS-7 pre-pilot declaration
```

**Relationship to `instrument_validation_report_hash` (top-level
binding):** the top-level hash binds the entire sealed validation
report; the sub-block here is an itemized breakdown for audit
clarity. Both must be present and recomputable at seal time.
Mismatch on any sub-hash refuses seal.

## 3. Field-by-field documentation

### `state`, `bound_hashes.*`, `bound_versions.*`, `token_prior_authorization`, `c2_considered_memos`, `g1_open_check`, `r6_inheritance_screen`, `audit.*`

Documentation unchanged from v0.1 §3. See `LOCK-RECORD-DRAFT-STRUCTURE-v0.1.md`
for full text.

### `validation_artifact_hashes` (NEW for v0.2)

| Field | Meaning | Populated at |
|---|---|---|
| `t1_sealed_hash` | sha256 of the sealed T1 battery-degeneracy-audit table (all rows populated) | D3 (Instrument Validation Report seal) |
| `t2_sealed_hash` | sha256 of the sealed T2 control-spec sheets — both `unconditioned_token_prior` and `scrambled_binding_retrieval` | D3 |
| `t3_sealed_hash` | sha256 of the sealed T3 ideal-witness / pass-region checklist | D3 |
| `t4_sealed_hash` | sha256 of the sealed T4 review-to-lock disposition table | D3 |
| `ideal_witness_record_hash` | sha256 of the T3-locked ideal-witness record (declared, reviewed, locked before pass-region checklist) | locked pre-pilot; recorded at D3 |
| `pilot_iteration_log_hash` | sha256 of the E11 pilot-iteration log (all failed pilots retained) | D3 |
| `oracle_case_verdict_table_hash` | sha256 of the A5 oracle-case pre-flight verdict table | D3 |
| `a6_reverification_block_hash` | sha256 of the A6 final-manifest re-verification block (per-policy + envelope + drift) | D3 |
| `drift_tolerance_declaration_hash` | sha256 of the IS-7 pre-pilot drift tolerance declaration | declared pre-pilot at D2; hashed at D3 |

**Audit guarantee:** the sub-block converts the
`instrument_validation_report_hash` from a single opaque hash to a
per-artifact ledger. Future readers can identify which specific
sealed artifact has drifted from expectation without having to
unpack and re-verify the entire report.

## 4. Sealed-hash binding rules (unchanged from v0.1)

Rule 1: every artifact affecting execution semantics is bound.
Rule 2: hashes computed at seal, not creation.
Rule 3: seal is atomic.
Rule 4: recompute-and-verify is mandatory.
Rule 5: SEALED is immutable.

**v0.2 clarification:** Rule 4 applies to both `bound_hashes.*` and
`validation_artifact_hashes.*`. The recompute step is atomic across
both blocks.

## 5. Token-prior-authorization slot (D4) (unchanged from v0.1)

Per Bundle v0.3 §I.5 + §VI #4 and standing token-prior gate.

## 6. C2 considered-memos enumeration (unchanged from v0.1)

Per adopted addendum §7 C2 and standing review-discipline rule.

## 7. G1-open check fields (unchanged from v0.1)

Per adopted addendum G1 + standing G1-open production rule.

## 8. Audit trail (unchanged from v0.1)

`audit.*` + `audit_log_hash_at_seal` binds LOCK-RECORD to the append-
only audit log state.

## 9. State machine (unchanged from v0.1)

```text
                ┌──────────┐
                │  PENDING │  <-- D2 package-assembly default
                └────┬─────┘
                     │
                     │  Required preconditions for SEALED transition:
                     │    1. D2 review PASS (Manager)
                     │    2. D3 review PASS (Team Lead)
                     │    3. D4 sweep-execution authorization (Manager)
                     │       — token_prior_authorization.state resolved
                     │         by name (AUTHORIZED | DECLINED)
                     │    4. g1_open_check.g1_open_count == 0
                     │    5. ALL bound_hashes recompute-and-verify match
                     │    6. ALL validation_artifact_hashes recompute-and-verify match
                     │    7. r6_inheritance_screen complete
                     │
                     v
                 ┌──────────┐
                 │  SEALED  │
                 └────┬─────┘
                      │
                      v
              ┌──────────────┐
              │  SUPERSEDED  │
              └──────────────┘
```

## 10. No-population-under-D2-package-assembly rule

Under Team Lead D2 package-assembly authorization, the LOCK-RECORD
remains a **structure document only**. No fields are populated with
real values. The skeleton above is the v0.2 deliverable; CS does not
create a populated `LOCK-RECORD.yaml` until later gates authorize
the seal step.

Specifically prohibited under D2 package assembly (same prohibition
list as v0.1's D1 rule, extended explicitly):

```text
- creating a sweep_id
- computing artifact hashes for execution-side artifacts (analysis script,
  runner source, etc. — none exist beyond standing governance)
- recording a SEALED state
- writing the audit_log_hash_at_seal
- writing any validation_artifact_hashes (D3 fills these; not D2)
- recording any AUTHORIZED state in token_prior_authorization
```

## 11. Non-authorizations

Refer to companion artifact `NON-AUTHORIZATION-CONSUMPTION-SIDE-EXCLUSION-LANGUAGE-v0.2.md`.

Summary:

```text
No execution authorized.
No new sweep_id.
No model runs.
No data generation.
No execution packet execution.
No offline pilot execution.
No oracle pre-flight execution.
No candidate selection.
No candidate ranking.
No threshold-sheet work.
No certification evaluation.
No stress-retention testing.
No B1 v2.1 implementation.
No Paper 3 revision.
No Claim C activation.
No Fork A reactivation.
No Paper 6 activation.
No public benchmark packaging.
```

All execution gates remain CLOSED.

## 12. CS sign-off

```text
Document status:                  DRAFT v0.2 — D2 package-assembly artifact
D2 authorization granted:         NO
Execution authorized:             NO
sweep_id created:                 NO
Model runs:                       NO
Data generated:                   NO
Validation outputs populated:     NO
LOCK-RECORD populated with values: NO

v0.1 -> v0.2 change:
  Added validation_artifact_hashes per-table sub-block (AL-Q5-opt)
  per Team Lead D2 carry-forward.

All six required slots from New Senior D1 ack item 7 still present:
  D4 by-name token-prior resolution (§2 token_prior_authorization + §5)
  sealed-hash binding (§2 bound_hashes + §4)
  C2 considered-memos enumeration (§2 + §6)
  R6 inheritance screen reference (§2 r6_inheritance_screen)
  T1-T4 validation artifact references (§2 bound_hashes + §2.1 NEW
                                         validation_artifact_hashes)
  non-authorization block (§11)
```

— CS Engineer, 2026-06-11
