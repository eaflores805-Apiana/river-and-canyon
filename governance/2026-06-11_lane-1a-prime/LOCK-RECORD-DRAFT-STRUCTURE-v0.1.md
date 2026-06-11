# LOCK-RECORD Draft Structure v0.1 — Lane 1a′

```text
DRAFT / REVIEW ONLY
D1 PACKET-PREPARATION ARTIFACT
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
Re: LOCK-RECORD draft structure for Lane 1a′ (skeleton)
Status: DRAFT v0.1; structure only; no values populated

---

## 1. Scope

LOCK-RECORD is the sealed-hash record that binds the Lane 1a′ packet
to a specific hash state at lock time. It carries the addresses of
all locked artifacts, the addendum/standing-rule version pins, the
G1-open check, the token-prior authorization slot (D4), and the C2
considered-memos enumeration.

Per Manager D1 direction:

```text
NO LOCK-RECORD hash values are populated under D1.
NO sweep_id is created under D1.
NO sealed state is reached under D1.
```

This document defines the **structure only**. The values are
populated by CS at packet seal, after the design packet + T1–T4
plans + execution-packet proposal pass review and the Manager grants
the appropriate gate authorizations.

Authority: D1 design authorization (Manager memo of 2026-06-11; commit
`d80ad4b`); Team Lead direction of 2026-06-11 (CS may begin CS-owned
proposal artifacts in skeleton form).

## 2. Schema (YAML skeleton)

```yaml
# governance/2026-06-11_lane-1a-prime/LOCK-RECORD.yaml
# Populated only at packet seal — NOT POPULATED UNDER D1

lock_record:
  schema_version: "v0.1"
  state: PENDING                       # PENDING | SEALED | SUPERSEDED
                                       # transitions: see §9 state machine

  identity:
    lock_id: <placeholder>             # uuidv4 at seal
    lane: "lane-1a-prime"              # constant
    sweep_id: <placeholder>            # NOT CREATED UNDER D1
    created_at: <placeholder>          # ISO 8601 at first PENDING write
    sealed_at: <placeholder>           # ISO 8601 at SEALED transition
    superseded_at: <placeholder>       # ISO 8601 if state transitions to SUPERSEDED
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
    manifest_recipe_hash:              <placeholder>   # per v0.2 §13 recipe
    runner_source_hash:                <placeholder>   # CS-owned
    runner_wrapper_source_hash:        <placeholder>   # CS-owned
    runner_config_hash:                <placeholder>   # CS-owned
    analysis_script_hash:              <placeholder>   # CS-owned
    instrument_validation_report_hash: <placeholder>   # sealed at D3
    non_authorization_section_hash:    <placeholder>   # CS-owned

  bound_versions:
    # Pins to externally-versioned references.
    addendum_path: "governance/standing/PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM.md"
    addendum_sha256:                "124f6046d57d365dd47596877fd1eb09088f6990ec3c9a52ac150d0c8ca103b8"
    addendum_adoption_commit:       "e76e7f8"
    standing_review_discipline_sha256: <placeholder>  # cross-checked at lock
    standing_non_authorizations_sha256: <placeholder> # cross-checked at lock
    paper3_tag:                     "paper3-certification-protocol-v1.1"
    mlx_lm_version:                 <placeholder>     # locked at packet (Path E.1 carry)
    production_python:              <placeholder>     # locked at packet (Path E.1 carry)
    model_id:                       <placeholder>     # locked at packet (Path A.1 carry)
    model_snapshot:                 <placeholder>     # tokenizer + weights snapshot

  # Per New Senior D1 ack item 7
  token_prior_authorization:
    state: NOT_AUTHORIZED            # NOT_AUTHORIZED | AUTHORIZED | DECLINED
                                     # AUTHORIZED state only after Manager
                                     # opens by name at D4
    manager_memo_path: <placeholder>
    manager_memo_sha256: <placeholder>
    by_name_decision_text: <placeholder>   # "by name, never by bundle" — verbatim Manager decision
    decision_date: <placeholder>
    declined_rationale: <placeholder>      # if state == DECLINED

  # Per New Senior D1 ack item 7 + C2 standing rule
  c2_considered_memos:
    - memo_id: <placeholder>            # human-readable id
      memo_path: <placeholder>          # repo-relative path
      memo_sha256: <placeholder>        # bytes on disk
      review_state: <placeholder>       # COMMITTED | HASH-CONFIRMED | SUPERSEDED | OUT-OF-SCOPE
      considered_for_gate: <placeholder> # which gate (D1..D5) the memo was considered for
    # NOTE: PASS records that close a gate enumerate these by hash;
    #       any review-in-flight is confirmed delivered-or-withdrawn
    #       before a PASS is recorded.

  g1_open_check:
    # Required for any state transition (PENDING -> SEALED, etc.)
    timestamp: <placeholder>
    checker: <placeholder>             # CS Engineer at packet seal
    g1_open_count: 0                   # must be 0 for SEALED transition
    pending_memo_ids: []               # empty for SEALED transition
    confirmation: <placeholder>        # "no condition memo affecting this lock is G1-open"

  r6_inheritance_screen:
    # Per addendum §8 R6 + v0.2 §3
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
    last_modified_at: <placeholder>    # for PENDING-state edits only;
                                       # SEALED records are immutable
```

## 3. Field-by-field documentation

### `state` (PENDING | SEALED | SUPERSEDED)

- `PENDING`: the LOCK-RECORD is being populated. Field values may be edited. **Default under D1 (NOT POPULATED).**
- `SEALED`: all fields populated; hash bound; immutable thereafter. Reachable only after every prerequisite gate has authorized the seal.
- `SUPERSEDED`: a later LOCK-RECORD has replaced this one (e.g., post-defect correction). Per the "supersede, don't rewrite" governance rule, the SEALED record is never edited; supersession creates a new LOCK-RECORD that references the old one by `superseded_by_lock_id`.

### `bound_hashes.*`

Every artifact CS or New Senior produces in the Lane 1a′ packet has a
hash field here. The lock-time check spawns a process that recomputes
each hash from disk and compares to the LOCK-RECORD value; any
mismatch refuses the seal.

### `bound_versions.*`

External version pins. The addendum path + sha256 + adoption commit
are already populated (resolved at adoption commit `e76e7f8`). Other
pins resolve at packet preparation.

### `token_prior_authorization`

**Critical slot per New Senior D1 ack item 7.** This field is the
**only** path by which `unconditioned_token_prior` control generations
may be authorized. The state cannot transition to `AUTHORIZED` without
a Manager memo that:

- names `unconditioned_token_prior` explicitly,
- is filed at a specific path,
- is hashed and recorded here,
- carries verbatim the "by name, never by bundle" disposition text.

No bundle authorization or implicit authorization moves this field.
Per addendum §6 and v0.2 §12 D4: token-prior generations remain
closed until this slot is `AUTHORIZED`.

### `c2_considered_memos`

**Critical slot per New Senior D1 ack item 7 + standing C2 rule.**
Every PASS record closing a gate enumerates the condition memos it
considered, by hash, here. A review-in-flight must be confirmed
delivered-or-withdrawn before a PASS is recorded; "a memo no one
knows exists cannot hold a gate" (standing rule).

### `g1_open_check`

Standing G1-open production rule: no production cycle while a
condition memo affecting it is G1-open. The lock-time seal performs
the check; `g1_open_count` must be 0 and `pending_memo_ids` must be
empty for the seal to proceed.

### `r6_inheritance_screen`

Carries v0.2 §3 R6 screen forward; documents each prior-lane
requirement screened for portability with its disposition.

### `audit.*`

Append-only audit metadata. The `audit_log_hash_at_seal` field binds
the LOCK-RECORD to the entire append-only audit log at the moment of
seal, so any later audit-log mutation is detectable.

## 4. Sealed-hash binding rules

**Rule 1 — every artifact that affects execution semantics is bound.**
If a file change would alter what `lane1a_prime_runner.py` produces,
how it produces it, or how its output is interpreted, that file is
in `bound_hashes`. The exhaustive list at v0.1 is the §2 enumeration;
the list grows only at later versions of this draft.

**Rule 2 — hashes are computed at seal, not at creation.** The LOCK-RECORD
is created in `PENDING` state with `<placeholder>` values; hashes
populate only when CS executes the seal step (after gate authorizations).

**Rule 3 — seal is atomic.** All hashes populate in a single transactional
write. A partial populate is not a valid LOCK-RECORD state.

**Rule 4 — recompute-and-verify is mandatory.** The seal step
recomputes each hash from disk and compares to the LOCK-RECORD field.
A mismatch refuses the seal and emits an audit event.

**Rule 5 — SEALED is immutable.** Once `state == SEALED`, no field may
be edited. Corrections create a new LOCK-RECORD with `state == PENDING`
that, on seal, transitions the old record's state to `SUPERSEDED`.

## 5. Token-prior-authorization slot (D4)

Per v0.2 §6 + §12 D4 and standing token-prior gate
(`STANDING-NON-AUTHORIZATIONS.md` "unconditioned token-prior runs"):

```text
The token_prior_authorization.state field begins NOT_AUTHORIZED at every
new LOCK-RECORD creation, even if a prior superseded LOCK-RECORD had
AUTHORIZED. The authorization does not inherit across LOCK-RECORDs;
it must be reissued by-name at the new gate.

Manager authorization that moves the state to AUTHORIZED must:
  - be a memo committed at a specific path in governance/
  - name "unconditioned_token_prior" explicitly
  - carry the verbatim "by name, never by bundle" decision text
  - be hash-confirmed in this slot at seal time
  - be enumerated in c2_considered_memos
```

## 6. C2 considered-memos enumeration (standing C2 rule)

Per addendum §7 C2 and standing review-discipline rule:

```text
SEND-TO-CS is intent. Delivery is a confirmed commit SHA at the
intended path in the target repository; for release-affecting or
execution-affecting artifacts, delivery also requires filename and
hash or blob identifier. A review that closes a gate enumerates,
by hash, the condition memos it considered; any review-in-flight is
confirmed delivered-or-withdrawn before a PASS is recorded — a memo
no one knows exists cannot hold a gate.
```

Implementation in LOCK-RECORD: every memo that closed a gate
authorizing any aspect of this LOCK-RECORD is listed in
`c2_considered_memos` with path + sha256 + review state + gate
considered for.

## 7. G1-open check fields

Per addendum G1 + standing G1-open production rule:

```text
A production cycle includes (but is not limited to) writing locked
artifacts, hash-recording in a lock record, or any work whose semantic
depends on the resolution of a still-in-flight instruction. No
production cycle may begin while any condition memo affecting that
production cycle is G1-open.
```

Implementation in LOCK-RECORD: at every state-transition step, CS
performs the G1-open check; the check fields record the result. The
seal cannot proceed unless `g1_open_count == 0`.

## 8. Audit trail

The `audit.*` fields carry the standard creation/modification/seal
timestamps. The `audit_log_hash_at_seal` field carries the hash of
the entire append-only audit log at the moment of seal — binding the
LOCK-RECORD to the audit log's state. Any later audit-log mutation
shifts the hash and is detectable on re-verification.

## 9. State machine

```text
                ┌──────────────────────────┐
                │ creation (CS at packet   │
                │  prep; D1 authorized)    │
                └────────────┬─────────────┘
                             │
                             v
                       ┌───────────┐
                       │  PENDING  │
                       └─────┬─────┘
                             │
                             │  CS edit cycles
                             │  (allowed in PENDING)
                             │
                             │  Required preconditions for SEALED transition:
                             │    1. D2 review PASS (Manager)
                             │    2. D3 review PASS (Team Lead)
                             │    3. D4 sweep-execution authorization (Manager)
                             │       — token_prior_authorization.state
                             │         resolved by name (AUTHORIZED | DECLINED)
                             │    4. g1_open_check.g1_open_count == 0
                             │    5. All bound_hashes recompute-and-verify match
                             │    6. r6_inheritance_screen complete
                             │
                             v
                       ┌──────────┐
                       │  SEALED  │ <─────── IMMUTABLE; cannot be edited
                       └─────┬────┘
                             │
                             │  (only via supersession; never edit-in-place)
                             │
                             v
                     ┌──────────────┐
                     │  SUPERSEDED  │ <───── superseded_by_lock_id points to
                     └──────────────┘         the new LOCK-RECORD
```

## 10. No-population-under-D1 rule

Under D1 authorization, the LOCK-RECORD is a **structure document
only**. No fields are populated with real values. The skeleton above
is the deliverable; CS does not create a `LOCK-RECORD.yaml` file
populated with values until later gates authorize the seal step.

Specifically prohibited under D1:

```text
- creating a sweep_id
- computing artifact hashes (no artifacts exist to hash yet beyond
  what's already adopted standing governance)
- recording a SEALED state
- writing the audit_log_hash_at_seal
- recording any AUTHORIZED state in token_prior_authorization
```

## 11. Non-authorizations

Refer to the companion artifact
`NON-AUTHORIZATION-CONSUMPTION-SIDE-EXCLUSION-LANGUAGE-v0.1.md` (CS,
same folder) for the verbatim block. Summary:

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
Document status:                  DRAFT v0.1 — structure only
D1 packet-preparation artifact:   YES
Execution authorized:             NO
sweep_id created:                 NO
Model runs:                       NO
Data generated:                   NO
Validation outputs populated:     NO
LOCK-RECORD populated with values: NO

Next:                             cross-review with New Senior design
                                   packet + T1-T4 plans; refine bound_hashes
                                   list once New Senior artifacts land;
                                   joint return to Manager at D2 gate

Three required slots (per New Senior D1 ack item 7) all present in §2:
  - token_prior_authorization (§2 + §5)
  - sealed-hash binding fields (§2 bound_hashes + §4)
  - c2_considered_memos enumeration (§2 + §6)
```

— CS Engineer, 2026-06-11
