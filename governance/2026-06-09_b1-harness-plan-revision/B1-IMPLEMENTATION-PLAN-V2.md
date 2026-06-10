# B1 Implementation Plan — V2 (Paper 3 §8 Alignment)

**Filed:** 2026-06-09
**Prepared by:** CS Engineer
**Status:** REVISION — design only; B1 implementation remains BLOCKED pending Manager code-change authorization
**Supersedes:** `tier0-run/governance/2026-06-09_post-paper2-alignment/B1-IMPLEMENTATION-PLAN.md` (v1)
**Driving spec (new):** Paper 3 *Certification Before Retention* v0.4 §8 (B1 dependency); Appendix A.1 (threshold sheet); Appendix A.2 (`gate_summary` schema)
**Driving spec (carried forward):** Team Update — Post-Paper 2 Alignment 2026-06-09 (original B1 bounded validity-hardening scope); Paper 2 Reproduction Acceptance Test Plan

---

## §1 Authorization basis

Two stacked authorizations define this plan's scope; neither has been extended to code execution.

**v1 authorization (carried forward):** Team Update 2026-06-09 approved B1 as bounded validity-hardening of the runner. v1 fields enumerated there — `model_snapshot_hash`, `mlx_lm_version`, `python_version`, `precision_rung`, `gate_summary`, `stress_eligible`, runtime fail-closed blocking, same-error identity analysis — remain in scope.

**v2 driver (new):** Paper 3 v0.4 §8 names B1 as a hard precondition for D6 clearance and (transitively) for D5's structural-proxy computation, D2's per-item contingency tables, and D7's per-item outcome logging. Team Lead v0.4 readiness check directs CS to update the B1 implementation plan against §8.

**Authorization gap:** This revision is a planning artifact. B1 code-change authorization has not been granted. No implementation work begins until Manager authorizes.

---

## §2 Scope

**In scope (v2 cumulative):**

*Carried over from v1:*
- Provenance fields: `model_snapshot_hash`, `mlx_lm_version`, `python_version`, `precision_rung`, `quant_method`
- Output block: `gate_summary` JSON, `stress_eligible` boolean, `eligibility_reason_code`, `voided_run_log`, `comparison_table` (stress-runner only)
- Per-item fields: `fp16_raw_output`, `exact_output_match`, `same_error_identity_key`
- Runtime fail-closed Gate 2 blocking
- Unit tests for above

*Added in v2 (Paper 3 §8):*
- Provenance fields: `analysis_script_hash`, `first_candidate_data_access_timestamp`
- `gate_summary` per-gate schema per Paper 3 Appendix A.2: `gate_id`, `status`, `observed_value`, `threshold_value`, `delta`, `reason_code`, `evidence_artifact_hash`, `evaluated_by`, `evaluated_at`, `short_circuit`, `framework_version`, `threshold_sheet_hash`, `analysis_script_hash`
- Per-item structural-proxy block (D5 substrate) — schema only, not candidate-specific proxies
- Per-item outcome logging adequate for D7 baseline-noise model or derivation rule
- Data-access timestamp capture sufficient to enforce Appendix A.1 data-access firewall
- Locked-artifact hash registry mechanism (D6: manifest, runner, scorer, analysis script all verifiable at run time)
- Unit tests for v2 additions (B1-T15 through B1-T24)

**Out of scope (v2):**
- Candidate selection (Manager-gated, not B1)
- Specific D2 shortcut null models (candidate-specific; specified in per-candidate threshold sheet)
- Specific D5 structural proxies (candidate-specific; computed by B1 from manifest fields the candidate's threshold sheet declares)
- Specific D7 baseline-noise model (candidate-specific; B1 produces logs adequate for either form)
- Threshold-sheet immutability enforcement tooling (separate scoping — see §10)
- New manifests, scoring axes, failure classes, dummy baselines
- Any B or C claim, any FP16 run, any stress run

---

## §3 What changed from v1

| Area | v1 (Paper 2 reproduction context) | v2 (Paper 3 §8 alignment, cumulative) |
|---|---|---|
| Driving spec | Paper 2 reproduction acceptance test plan | Adds Paper 3 v0.4 §8 |
| Provenance fields | 5 fields (snapshot, mlx_lm, python, precision_rung, quant_method) | Adds `analysis_script_hash`, `first_candidate_data_access_timestamp` |
| `gate_summary` block | Top-level object with gate_1, gate_2, gate_5 keys (Paper 2 gate ladder) | Same gates *plus* per-gate Paper 3 A.2 schema (status / observed / threshold / delta / reason_code / evidence_artifact_hash / evaluated_by / evaluated_at / short_circuit / framework_version / threshold_sheet_hash / analysis_script_hash) |
| Per-item logging | failure_class, scaffold_class, format_class, same_error_identity_key | Adds `structural_proxies` (schema only), D7-adequate outcome logging |
| Data-access firewall | Not present | New: capture timestamp of first candidate-data read; refuse run if threshold-sheet lock postdates first access |
| Locked-artifact verification | Constants in runner header (`EXPECTED_RUNNER_HASH`, etc.) checked at boot | Extended to a registry the runner can verify (manifest, runner, scorer, analysis script all checked against threshold-sheet declared hashes) |
| Unit tests | B1-T1 through B1-T14 | Adds B1-T15 through B1-T24 |

The v1 plan's structure, file targets, and conservative philosophy carry forward unchanged; v2 layers Paper 3 substrate on top, it does not rewrite v1 decisions.

---

## §4 Gap analysis — current runner vs. B1 v2 requirement

Reference runner: `runner_twohop_l1_cell03.py` (sha256:f23d99df...). v1 gap table reproduced and extended.

### 4.1 Provenance block — v2 additions

| Field | v1 status | v2 requirement |
|---|---|---|
| (v1 fields) | See v1 plan §3 | Unchanged in v2 |
| `analysis_script_hash` | Not present | sha256 over the analysis script that consumes runner output for gate computation. If gate computation runs inside the runner itself, set to `"sha256:in-runner"` and record the runner_hash. If gate computation runs in a separate analysis script, record that script's sha256. |
| `first_candidate_data_access_timestamp` | Not present | ISO-8601 UTC timestamp captured at the first read of candidate-evaluation data (per Paper 3 v0.4 D6 definition: fresh evaluation data produced under the B1 harness for the certification attempt). Recorded by the runner the moment it opens the manifest JSON for evaluation purposes. |
| `framework_version` | Not present | String literal `"paper3-certification-protocol-v0.4"` for runs targeting Paper 3 certification. For runs not under a Paper 3 certification attempt (e.g., Paper 2 reproduction), set to `"none"`. |
| `threshold_sheet_hash` | Not present | When a threshold sheet is in force, the sha256 of the locked threshold sheet (Paper 3 A.1 `threshold_sheet_content_hash`). When no threshold sheet (e.g., Paper 2 reproduction context), set to `"none"`. |

### 4.2 `gate_summary` — v2 per-gate schema

v1 `gate_summary` is a top-level object with `gate_1`, `gate_2`, `gate_5` keys, each containing pass/fail and threshold used. v2 requires each gate record to populate the full Paper 3 A.2 schema:

```python
gate_record = {
    "gate_id":               str,    # e.g., "gate_2" for Paper 2 ladder; "D1".."D7" for Paper 3 certification
    "status":                str,    # "pass" | "fail" | "not_evaluated"
    "observed_value":        any,    # the measured value (e.g., 14 for hop1_correct)
    "threshold_value":       any,    # the pre-registered threshold (e.g., 20)
    "delta":                 any,    # observed - threshold (signed; convention: negative = below threshold)
    "reason_code":           str,    # machine-readable; e.g., "GATE2_FAIL_HOP1_14_BELOW_20"
    "evidence_artifact_hash": str,   # sha256 of the table / JSON path / file that is the pass/fail evidence
    "evaluated_by":          str,    # "runner-builtin" or path/hash of the analysis script
    "evaluated_at":          str,    # ISO-8601 UTC timestamp
    "short_circuit":         bool,   # true if review stopped before this gate was reached
    "framework_version":     str,    # propagated from provenance
    "threshold_sheet_hash":  str,    # propagated from provenance; "none" if no sheet
    "analysis_script_hash":  str,    # propagated from provenance
}
```

**Two distinct evaluation contexts to handle:**

1. **Paper 2 reproduction / Two-Hop L1 context.** Gate IDs are `gate_1`, `gate_2`, `gate_5` (the Two-Hop L1 ladder). `framework_version = "none"`, `threshold_sheet_hash = "none"`. The runner-builtin gate evaluator populates the record.
2. **Paper 3 certification context.** Gate IDs are `D1` through `D7`. `framework_version = "paper3-certification-protocol-v0.4"`, `threshold_sheet_hash = <sha256 of locked sheet>`. Gate evaluation may be runner-builtin or by a separate analysis script; either path populates the same schema.

The v1 evaluation logic for Two-Hop L1 gates carries forward unchanged in terms of pass/fail criteria; only the record shape is wider.

### 4.3 Per-item result — v2 additions

| Field | v1 status | v2 requirement |
|---|---|---|
| (v1 fields) | See v1 plan §3 | Unchanged in v2 |
| `structural_proxies` | Not present | Dict of structural metrics computed from manifest JSON only — *schema slot only at v2*. For Two-Hop L1 reproduction context, leave empty `{}`. For Paper 3 certification context, populated per the candidate's threshold-sheet `D5_structural_difficulty_proxies` declaration. Computation must be deterministic and require no model output (D5 rule: no model-accuracy-based proxies). |
| Per-item outcome detail for D7 | Implicit (failure_class, is_correct already present) | Per-item correctness and per-item failure-class records must be adequate to support either form of `D7_baseline_noise_model_or_derivation_rule` (specified noise model OR bootstrap from per-item logs). v1 already records per-item is_correct and failure_class; v2 confirms these are retained and adds documentation that they constitute the D7-adequate substrate. |

### 4.4 Data-access firewall enforcement

The Paper 3 v0.4 D6 firewall states: any candidate-data access preceding threshold-sheet lock results in automatic *not certified*. v2 implementation:

1. Runner captures `first_candidate_data_access_timestamp` at the moment it opens the candidate's manifest JSON for evaluation.
2. If a threshold sheet is in force (Paper 3 context), the runner is given the `threshold_sheet_timestamp` as a configuration input.
3. **Precondition check** at runner boot: if `first_candidate_data_access_timestamp` would precede `threshold_sheet_timestamp`, the runner refuses to proceed and writes a `not_certified` record with `reason_code = "FIREWALL_VIOLATION_DATA_ACCESS_PRELOCK"`.
4. The captured timestamp is written into provenance, so the firewall check is independently verifiable from the result file.

For non-Paper 3 contexts (no threshold sheet), the timestamp is still captured for completeness, and the firewall check is bypassed (the firewall is a Paper 3 certification rule).

### 4.5 Locked-artifact hash registry

v1 already verifies runner / scorer / manifest hashes via runner-header constants (`EXPECTED_RUNNER_HASH`, `EXPECTED_SCORER_HASH`, `EXPECTED_MANIFEST_HASH`). v2 extends this to include `EXPECTED_ANALYSIS_SCRIPT_HASH` and, in Paper 3 context, verification of all four against the threshold sheet's `D6_locked_artifact_set`. Hash mismatch at boot → runner refuses to proceed.

---

## §5 File-level changes (v2 cumulative)

### 5.1 Primary file: `runner_twohop_l1_cell03.py`

All v1 changes (§4.1 of v1 plan) carry forward. Additions for v2:

**Provenance additions:**
```python
"analysis_script_hash":                  compute_analysis_script_hash(),  # "sha256:in-runner" if gate eval is in-runner
"framework_version":                     FRAMEWORK_VERSION,               # config-driven; "none" or "paper3-certification-protocol-v0.4"
"threshold_sheet_hash":                  THRESHOLD_SHEET_HASH,            # config-driven; "none" or sha256
"first_candidate_data_access_timestamp": <captured at manifest open>,
```

**Wider `gate_summary` record per gate** — see §4.2 schema. Existing pass/fail logic is wrapped to emit the wider record shape.

**Per-item structural_proxies slot:**
```python
result_record = {
    ...existing fields...,
    "structural_proxies": {},  # empty for Two-Hop L1 reproduction; populated in Paper 3 context
}
```

**Boot-time firewall precondition check** — new code block before any manifest read in a Paper 3 context.

**Boot-time hash registry verification** — extend the existing `EXPECTED_*_HASH` checks to include analysis script and (in Paper 3 context) the four-artifact set from the threshold sheet.

### 5.2 New file: `runner_b1_v2_paper3_adapter.py` (conditional)

If layering the Paper 3 firewall, threshold-sheet plumbing, and dynamic framework-version configuration into `runner_twohop_l1_cell03.py` would entangle the Two-Hop L1 runner with Paper 3 specifics, create a thin adapter module that:
- Reads the threshold-sheet input (if any) and produces the runtime config dict.
- Wraps the underlying runner with the boot-time firewall and hash-registry checks.
- Leaves the Two-Hop L1 runner clean for Paper 2 reproduction context.

**Decision rule:** Adapt in place if Paper 3 context can be activated by a config flag without changing the runner's structural code. Create the adapter if firewall/registry plumbing requires structural changes that would complicate Paper 2 reproduction use.

### 5.3 Structural-proxy computation module: `structural_proxies.py` (new)

D5 requires deterministic, model-free computation of structural proxies from manifest JSON. v2 adds a separate module with one function per supported proxy (token length, context-window utilization, graph distance, number of hops, number of keys, nesting depth, distractor count, distractor entropy, answer-position distribution, token-prefix overlap, NULL/non-NULL balance). The candidate's threshold sheet declares which proxies are used; the runner calls only the declared ones.

This module ships in v2 with the function signatures and unit tests but no candidate-specific calling convention — candidate selection has not occurred.

---

## §6 Unit test additions (v2)

v1 tests B1-T1 through B1-T14 carry forward. v2 adds:

| Test ID | Test | Pass condition |
|---|---|---|
| B1-T15 | `analysis_script_hash` present in provenance | Field present; starts with `"sha256:"` or equals `"sha256:in-runner"` |
| B1-T16 | `first_candidate_data_access_timestamp` present in provenance | Field present; valid ISO-8601 UTC string |
| B1-T17 | `framework_version` in provenance equals configured value | For Paper 3 context test fixture, equals `"paper3-certification-protocol-v0.4"` |
| B1-T18 | `threshold_sheet_hash` in provenance equals configured value | For Paper 3 context test fixture, equals the test threshold sheet's sha256 |
| B1-T19 | `gate_summary` per-gate record populates all A.2 schema fields | Every required A.2 field present and typed correctly on every gate record |
| B1-T20 | `short_circuit` field correctly set for unevaluated gates | When earlier gate fails and review stops, later gates have `status="not_evaluated"` and `short_circuit=true` |
| B1-T21 | Firewall precondition rejects pre-lock data access | Synthetic test: set threshold_sheet_timestamp to a future time relative to runner boot; runner refuses with reason_code `"FIREWALL_VIOLATION_DATA_ACCESS_PRELOCK"` |
| B1-T22 | Firewall passes when data access postdates lock | Threshold_sheet_timestamp in the past; runner proceeds; access timestamp recorded |
| B1-T23 | Hash registry verification rejects mismatched artifacts | Mock a manifest with altered hash; runner refuses at boot with hash-mismatch reason_code |
| B1-T24 | `structural_proxies` module functions are deterministic | Each proxy function returns the same value on identical manifest input across repeated calls |

Total B1 v2 test count: **24** (14 from v1 + 10 from v2).

---

## §7 Execution order (v2)

1. Confirm v1 prerequisites (Gate 2 thresholds, Paper 2 reproduction acceptance plan).
2. Implement v1 fields and tests (B1-T1 through B1-T14) — unchanged from v1 plan §5.
3. Implement `compute_analysis_script_hash()` helper.
4. Implement `first_candidate_data_access_timestamp` capture at manifest-open.
5. Wrap existing gate-summary records to emit the Paper 3 A.2 per-gate schema.
6. Implement `structural_proxies.py` with function signatures and unit tests; no calling convention until candidate selected.
7. Implement boot-time firewall precondition check.
8. Extend boot-time hash registry to include analysis script and (if Paper 3 context) four-artifact threshold-sheet set.
9. Run all unit tests (B1-T1 through B1-T24).
10. Dry-run pass on a Two-Hop L1 cell (Paper 2 reproduction context: `framework_version="none"`, no threshold sheet) — confirm v1 behavior preserved.
11. Dry-run pass on a synthetic Paper 3 test fixture (with a mock threshold sheet) — confirm Paper 3 plumbing works without selecting a real candidate.
12. Compute new runner hash; update `EXPECTED_RUNNER_HASH`.
13. File runner amendment lock note (v2).
14. Update `EXPERIMENT_LOG.md` with B1 v2 runner hash.

---

## §8 What B1 v2 does NOT change

- `scorer_twohop_l1.py` — not amended.
- All manifest files (`items_twohop_l1_cell0*.json`) — not amended.
- All existing result JSON files (Cells 01–03) — not amended or rewritten.
- All RESULTS-ALL markdown files — not amended.
- Two-Hop L1 gate thresholds — not changed; v1 values preserved.
- Failure taxonomy — not changed.
- Paper 2 reproduction acceptance test pass/fail criteria — not changed.
- The tier0-run/ directory contents — SEALED; no additions.
- Candidate selection — not made.
- D2 shortcut null models, D5 specific proxies, D7 specific noise model — not specified; remain candidate-specific deliverables of the per-candidate threshold sheet.

---

## §9 Prerequisites for B1 v2 execution

- [x] Team Lead Gate 2 threshold confirmation (received 2026-06-09)
- [x] Paper 3 v0.4 §8 spec finalized (Team Lead accepted v0.4 for controlled circulation, 2026-06-09)
- [ ] **Manager authorization for B1 code-change execution.** Original Team Update 2026-06-09 approved "bounded validity-hardening"; CS reads this as covering v1 fields. v2 expands the field set; Manager should confirm whether the original authorization extends to v2 scope or whether v2 requires a fresh authorization.
- [ ] Paper 2 Reproduction Acceptance Test Plan reviewed against v2 (no change expected; v2 is additive)

---

## §10 Status and adjacent CS deliverables

**B1 v2 status:** Design plan complete. Implementation BLOCKED pending Manager code-change authorization (see §9).

**Adjacent CS deliverable not in v2 scope:** Threshold-sheet immutability enforcement tooling. Paper 3 v0.4 A.1 states locked threshold sheets must not be overwritten; v0.4 explicitly avoided claiming automatic tooling enforcement (per Team Lead readiness check §2). If the program later decides to build automatic enforcement, CS would scope a separate deliverable: a pre-commit hook or governance-check script maintaining a registry of locked threshold-sheet hashes and refusing commits that modify a registered file. That is not included in B1 v2.

---

## Non-authorizations (carried forward)

```
new runs · re-runs · INT8 / INT4 execution · multi-model execution
unconditioned token-prior runs · activation logging · candidate selection
threshold values · Fork A reactivation · Claim C activation
Paper 3 execution as an experiment · Paper 6 activation
artifact mutation · public benchmark packaging
```

---

— CS Engineer, 2026-06-09
