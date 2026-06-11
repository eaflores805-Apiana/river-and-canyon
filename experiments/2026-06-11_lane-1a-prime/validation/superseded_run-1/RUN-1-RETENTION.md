# Run-1 Retention Record — Phase 5 (Superseded)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
SUPERSEDED VALIDATION ARTIFACTS — PHASE 5 RUN-1
RETAINED PER E11 / PH5-5 RETENTION DISCIPLINE
LOCK-RECORD REMAINS PENDING
```

This directory contains the Phase 5 run-1 validation artifacts that
have been **SUPERSEDED** by the corrective Phase 5 v0.2 re-run. Per
E11 retention discipline + PH5-5 (joint corrective disposition,
TL/Manager-authorized), these files are **retained and auditable**,
not erased.

A passing run-2 does NOT erase run-1; the failure modes that
prompted the re-run are documented here.

---

## Pointer to run-1 artifacts

The eight superseded artifacts are in this directory:
- `pilot_manifests_L01.json` (run-1 sha256 `bcf5f9bc…`)
- `final_manifests_L01.json` (run-1 sha256 `ab1629dc…`)
- `oracle_validation_results.json` (run-1 sha256 `e8877197…`)
- `t1_report.json` (run-1+A6-corrected sha256 `63760bf9…`)
- `t3_report.json` (run-1 sha256 `9522b29d…`)
- `t4_report.json` (run-1 sha256 `a9f812ea…`)
- `instrument_validation_report.md` (run-1+A6-corrected sha256 `122780d5…`)
- `execution_ledger.json` (run-1+A6-corrected sha256 `bd281869…`)

Repo commits where these artifacts lived:
- Original Phase 5 v0.1: commit `618e217`
- A6 tolerance correction (commit b071b37): `t1_report.json`, `instrument_validation_report.md`, `execution_ledger.json`, `run_validation.py` updated

---

## E11 retention block

Per addendum E11: "every failed pilot validation attempt must be
retained in the validation report; a passing final battery does not
erase prior failed pilot attempts (no unrecorded garden of forking
paths)."

```text
pilot_iteration_count: 2
  iteration 1 (this directory): run-1 v0.1; failed
  iteration 2 (parent directory): run-2 v0.2; corrective; pending result

failed_pilot_records_retained:
  - validation/superseded_run-1/pilot_manifests_L01.json
  - validation/superseded_run-1/final_manifests_L01.json
  - validation/superseded_run-1/oracle_validation_results.json
  - validation/superseded_run-1/t1_report.json
  - validation/superseded_run-1/t3_report.json
  - validation/superseded_run-1/t4_report.json
  - validation/superseded_run-1/instrument_validation_report.md
  - validation/superseded_run-1/execution_ledger.json

reason_for_each_repilot:
  - reduced-criteria run: CS Phase 5 v0.1 used 2 of 6 T3 criteria
    (the symmetric abstention pair); envelope, token_prior,
    headroom, and gap criteria were absent.
  - unlocked verdict table: NS-PROPOSED Oracle Expected-Verdict
    Declaration v0.1/v0.2 was filed but not co-signed before
    Phase 5 run-1 executed. CS ran with a CS-local verdict table
    (9 cases) instead of the joint 12-case table (NS v0.2).
  - unstratified recipe: ManifestRecipe placed gold position
    uniformly at random across answerable items; structural
    hit-rates were per-draw random variables, not construction
    constants. A6 drift at 0.10 envelope; 0.1375 pure_last_position.
  - A6 drift exceedance: under the joint-disposition tolerance
    (0.05/0.05), envelope_drift 0.10 > 0.05 and
    pure_last_position drift 0.1375 > 0.05. drift_within_tolerance
    became False under the joint disposition tolerance (was True
    under a CS demo tolerance of 0.30 that was not anti-tuning
    compliant).

changed_fields_between_pilots:
  apply_criterion:
    OLD (v0.1): is_floor=True used ci_lower; is_floor=False used ci_upper
                  (CS's local "any CI bound on elimination side" rule)
    NEW (v0.2): is_floor=True uses ci_upper; is_floor=False uses ci_lower
                  (uniform principle: entire CI on elimination side per
                  D2-APPROVED v0.2 §B; never silent Wald)

  DEFAULT_T3_CRITERIA:
    OLD (v0.1): 2 criteria with placeholder bounds
    NEW (v0.2): 6 criteria loaded from
                T3_BOUNDS_DECLARATION.json (locked at PH5-1)

  ORACLE_CASE_CATALOG:
    OLD (v0.1): 9 cases with CS-local expected verdicts
    NEW (v0.2): 12 cases loaded from
                ORACLE_VERDICT_TABLE.json (locked at PH5-1);
                ORC-10 semantic redefined to post-scramble-gold
                with required_absent={TP};
                ORC-04, ORC-05, ORC-11, ORC-12 added.

  ManifestRecipe:
    OLD (v0.1): random uniform placement
    NEW (v0.2): stratified counts per structural feature
                (n_at_last_position, n_at_salient_endpoint,
                n_in_prefix_neighborhood, n_at_none_of_these)

  run_validation tolerance:
    OLD (v0.1 original): 0.30 (anti-tuning non-compliant)
    OLD (v0.1+ corrected at commit b071b37): 0.05 (correct;
                drift_within_tolerance=False)
    NEW (v0.2): 0.05 (unchanged from corrected v0.1+)
                Under stratified recipe, drift is near zero by
                construction; A6 trivially passes (verifying
                implementation fidelity rather than sampling luck).

  Oracle verdict-matching:
    OLD (v0.1): verdict-only (outcome match only)
    NEW (v0.2): 4-clause label-set matching:
                outcome + required_present + required_absent_absent
                + only_required_or_permitted_attached

  Pre-flight precondition:
    OLD (v0.1): none
    NEW (v0.2): ValidationPreFlightConfig + verify_pre_flight_config;
                refuses to run unless verdict-table hash + bounds hash
                + recipe schedule hash match the PH5-1 lock event.
                Pattern-equivalent to PacketLockRefused (IS-8).
```

---

## Anti-tuning attestation (CS)

Per joint corrective disposition (commit `915d261`):

- **NO threshold value, criterion comparison rule, or A6 tolerance
  has been adjusted in response to Phase 5 run-1 outcomes.** Bounds
  derived from structural rationales (chance baseline; ideal-corner
  CI; expected single-policy hit rates), not from run-1 outcomes.

- **Run-1 numerics are quarantined from the v0.2 bound declarations.**
  The bound rationales in `T3_BOUNDS_DECLARATION.json` are pre-registered
  and audit-traceable.

- **Run-1 retention is mechanical**, not procedural: the superseded
  artifacts live in `validation/superseded_run-1/` and are
  cross-referenced from the run-2 IVR. A passing run-2 cannot erase
  run-1 because run-1 lives at a separate filesystem path.

---

## Confirmations (CS)

```text
No model was invoked in run-1.
No model was loaded in run-1.
No sweep_id was created in run-1.
No sweep execution occurred in run-1.
No candidate/model outputs were produced in run-1.
LOCK-RECORD remained PENDING throughout run-1.
LOCK-RECORD remains PENDING under run-2.
```

— CS Engineer, 2026-06-11
