# CS Path A Remediation Return — Lane 1a Runner

From: CS Engineer
To: Elias / Manager
Cc: Team Lead, Senior Engineer
Date: 2026-06-10
Status: Path A remediation complete; 35/35 unit tests pass; LOCK-RECORD re-sealed; awaiting Senior intent-preservation confirmation + Team Lead combined re-review + Manager re-reauthorization

---

## 0. TL;DR

```text
Path A authorized:               Manager direction 2026-06-10
New runner artifact:             lane1a_runner.py (uses mlx_lm directly;
                                   B1 v2-compatible provenance;
                                   B1 v2 source UNEDITED)
Wrapper updated:                 subprocesses lane1a_runner.py
                                   sidecar pattern preserved
                                   runner output byte-preserved (unit-tested)
Schema updated:                  sidecar fields renamed (runner_output_*)
                                   const-locks lane-1a fields
runner_config.yaml updated:      misleading b1v2 invocation block removed
                                   correct Path A wording in 'runner:' section
Tests:                           35/35 PASS
                                   (22 prior + 3 updated sidecar + 7 new runner
                                   manifest-validation + 3 new runner provenance)
LOCK-RECORD re-sealed:           68edbdcd68660e60b99ad19d9ccae0cdfb8b246cea50b8d8036fbbd7f8a743f9
                                   (PENDING_TEAM_LEAD_REVIEW timestamp)
First data access:               NOT EXECUTED
Model load:                      DID NOT OCCUR
B1 v2 source:                    UNEDITED
B1 v2.1:                         NOT CREATED OR USED
Native B1 v2 execution claim:    REMOVED from all documentation
```

## 1. Eleven-item CS return (per Manager memo §7)

### 1. Complete changed artifact list

| # | Path | Status |
|---|---|---|
| 1 | `experiments/2026-06-10_lane-1a-sweep/lane1a_runner.py` | NEW |
| 2 | `experiments/2026-06-10_lane-1a-sweep/lane1a_runner_wrapper.py` | UPDATED (subprocesses lane1a_runner.py; canonical field name `runner_output_*`) |
| 3 | `experiments/2026-06-10_lane-1a-sweep/runner_config.yaml` | UPDATED (b1v2 invocation block removed; runner: section added) |
| 4 | `experiments/2026-06-10_lane-1a-sweep/schema/lane1a_sidecar.schema.json` | UPDATED (fields: runner_output_path / runner_output_sha256 / runner_name=lane1a_runner.py) |
| 5 | `experiments/2026-06-10_lane-1a-sweep/test_lane1a_packet.py` | UPDATED (3 sidecar tests updated to new field names; 10 new tests for lane1a_runner.py) |
| 6 | `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | RE-SEALED (Path A entries; superseding prior `ef170fd7…`) |
| 7 | `governance/2026-06-10_lane1a/MANAGER-DIRECTION-PATH-A-2026-06-10.md` | NEW (governance archive) |
| 8 | `governance/2026-06-10_lane1a/CS-PATH-A-REMEDIATION-RETURN-2026-06-10.md` | NEW (this memo) |

All 16 other locked artifacts are unchanged (verified by hash).

### 2. Full sha256 hash for each changed artifact

```text
lane1a_runner.py                      23a480e701d583a91f435eca0d2d641af0e4797684d64b442d2ec9da5565d531
lane1a_runner_wrapper.py              4bed7fbdb938021638bda3908b7cbdb1e68e4dcc6305c7455b24df345cb444b1
runner_config.yaml                    bbb4655e5789a0eb767a26b54d58dbe4bdc428f31469082dc0cc151d47596dc3
schema/lane1a_sidecar.schema.json     23195986fe8bba1fa0754f9af1d9a80ce984e62f2056320d7ac9da281b4ac4aa
test_lane1a_packet.py                 934f39773cd90c998edf19b07b621ec83ac925721804a0c6d319e47abfb2701e
LOCK-RECORD.md                        68edbdcd68660e60b99ad19d9ccae0cdfb8b246cea50b8d8036fbbd7f8a743f9
```

### 3. Updated LOCK-RECORD hash

```text
Path A LOCK-RECORD.md sha256: 68edbdcd68660e60b99ad19d9ccae0cdfb8b246cea50b8d8036fbbd7f8a743f9
Lock timestamp:                PENDING_TEAM_LEAD_REVIEW
```

Supersedes the prior LOCK-RECORD `ef170fd7…` (which corresponded to
the wrapper that subprocessed B1 v2 CLI — incompatible with Lane 1a
manifests).

### 4. Test summary

```text
Test runner:    python -m unittest test_lane1a_packet
Tests run:      35
Tests passed:   35
Tests failed:    0
Wall time:      ~0.28s
```

Coverage of Manager §6 required tests:

| Manager-required test | CS test that verifies it |
|---|---|
| `lane1a_runner.py` accepts Lane 1a manifest schema | `TestLane1aRunnerManifestValidation::test_valid_manifest_accepted` + `test_actual_generated_manifests_validate` (all 8 generated rungs pass) |
| Manifest validation fails on malformed Lane 1a manifests | `test_missing_top_level_keys_rejected`, `test_wrong_artifact_class_rejected`, `test_wrong_certification_relevance_rejected`, `test_invalid_stratum_rejected`, `test_missing_item_field_rejected` |
| Model identity / snapshot provenance recorded | `TestLane1aRunnerProvenance::test_compute_model_snapshot_hash_signature` (returns `sha256:` + 64 hex; B1 v2-compatible format) |
| Runner output preserved byte-for-byte | `TestWrapperSidecarPattern::test_runner_output_preserved_byte_for_byte` |
| Lane 1a metadata remains in sidecar only | `TestWrapperSidecarPattern::test_lane1a_metadata_only_in_sidecar` |
| `artifact_class = lane-1a-reconnaissance` | const-locked in `artifact_tags.py`; `TestArtifactTagsRejectOverride`; sidecar schema `wrapper_attestation.artifact_class: { const: "lane-1a-reconnaissance" }` |
| `certification_relevance = none` | const-locked in `artifact_tags.py`; sidecar schema; runner provenance record |
| `framework_version = none` | sweep_record schema `framework_version: { const: "none" }`; runner provenance `framework_version: "none"`; `TestSchemaRejectionOfOrderFields::test_sweep_schema_blocks_paper3_framework_version` |
| no-re-execution rule enforced | wrapper `invoke_runner` checks `audit.has_prior("runner_started", rung_id, stratum)`; raises `ReExecutionRefused`; `TestAuditLogAppendOnly` |
| planned_generation_count = 1,536 | recorded in `classification_criteria.yaml`; in LOCK-RECORD; in `runner_config.yaml` |
| B1 v2 source remains unedited | `TestLane1aRunnerProvenance::test_no_b1v2_imports` (asserts `lane1a_runner.py` does NOT import `runner_b1_v2` or any module from `experiments/2026-06-09_b1-harness-v2/`); `git diff` clean on B1 v2 dir |
| B1 v2.1 not created or used | no file named for B1 v2.1 anywhere in repo; verified by `find` |

### 5. Confirmation that no first data access occurred

**CONFIRMED.** No invocation of `lane1a_runner_wrapper.py preflight()`.
No invocation of `lane1a_runner_wrapper.py invoke_runner()`. No
invocation of `lane1a_runner.py`. `AUDIT-LOG.ndjson` still absent.

### 6. Confirmation that no model load occurred

**CONFIRMED.** mlx_lm.load() not called in this session.

### 7. Confirmation that no live outputs were produced

**CONFIRMED.** `experiments/2026-06-10_lane-1a-sweep/raw/` does not
exist. The only outputs present are the 8 deterministic Lane 1a
manifests (`manifests/L01..L08.json` + `MANIFEST-HASHES.lock` +
`RECIPE-ACCEPTANCE-CHECK-RESULTS.json`), all produced by the offline
manifest generator (no model call).

### 8. Confirmation that B1 v2 was not edited

**CONFIRMED.** `git diff experiments/2026-06-09_b1-harness-v2/` returns
empty. B1 v2 remains at merge `3cbfce57`.

### 9. Confirmation that B1 v2.1 was not created or used

**CONFIRMED.** No file named for B1 v2.1. No code path references B1
v2.1 features. Verified by `find` and by unit test
`TestLane1aRunnerProvenance::test_no_b1v2_imports`.

### 10. Confirmation that the packet no longer claims native B1 v2 execution

**CONFIRMED.** The Manager-prescribed wording is applied verbatim in:

- `LOCK-RECORD.md` §"Runner integration (Path A)"
- `runner_config.yaml` top-of-file comment + `runner:` block
- `lane1a_runner_wrapper.py` `CONTEXT_FUNCTIONAL_STATEMENT` constant
- Every Lane 1a sidecar file (`wrapper_attestation.context_functional_statement`)
- This remediation return

The earlier wrapper's CONTEXT_FUNCTIONAL_STATEMENT (which referred to
"B1 v2 `--context paper2-reproduction`") is replaced with the
Path A statement. No string in the new artifact set claims native B1
v2 execution; no string claims B1 v2.1.

### 11. Any remaining implementation concern

**One soft note** (non-blocking; flagging for Team Lead awareness):

- The `lane1a_runner.py` module imports `mlx_lm` at runtime inside
  `run()` (not at module top level). This is intentional so that
  manifest validation and provenance computation work in environments
  where `mlx_lm` is not installed (e.g., unit tests with mocked
  runner output). The `--validate-only` CLI flag exercises this path
  and is used by Team Lead to spot-check manifests without loading
  the model. If Team Lead prefers an explicit "import-or-fail-fast"
  semantic at module top, CS can change to that form; the current
  form is more conservative and CS recommends keeping it.

## 2. Standing review-discipline check on this remediation

Failure-mode prompt: *How could a runner-substitution remediation
become a hidden authorization or quietly drift away from the
attestation discipline?*

CS-verified protections:

- Manager's Path A direction is filed verbatim in
  `MANAGER-DIRECTION-PATH-A-2026-06-10.md`; CS does not exceed it.
- The new runner has **no path** to invoke B1 v2; the wrapper
  subprocess argv targets `lane1a_runner.py` exclusively (constant
  `LANE1A_RUNNER` is the only RUNNER reference in the wrapper).
- `lane1a_runner.py` has **no path** to import B1 v2; unit-tested by
  `test_no_b1v2_imports`. The only shared surface is the `mlx_lm`
  dependency, which is a third-party library both runners consume.
- The model attestation algorithm in `lane1a_runner.py` is a
  re-implementation of B1 v2's `compute_model_snapshot_hash` (same
  algorithm, separate source); the resulting hash is byte-comparable
  to B1 v2's record but is produced by Lane 1a code.
- The sidecar pattern is preserved: runner output preserved
  byte-for-byte; Lane 1a metadata only in `*.lane1a.sidecar.json`;
  unit-tested.
- The Manager-prescribed wording is applied verbatim wherever the
  runner integration is described.
- First data access remains gated by:
  Senior intent-preservation confirmation → Team Lead combined
  adversarial review → lock-timestamp append → Manager
  reauthorization → preflight pass → invoke.

Protection layer: **schema/code class** (hash equality, validator
schemas, code-level enforcement; no purely wording-class protection
introduced).

## 3. Review sequence remaining (per Manager memo §8)

```text
1. CS Path A remediation — COMPLETE (this commit)
2. Senior intent-preservation confirmation — PENDING
3. Team Lead combined adversarial review — PENDING
4. LOCK-RECORD timestamp finalized — PENDING (CS appends after Team
   Lead PASS; new post-timestamp hash recorded)
5. Manager reauthorizes first data access against final hash set —
   PENDING
6. CS may execute only if preflight passes — PENDING
```

## 4. Current state

```text
Path A remediation:              COMPLETE
Tests:                           35/35 PASS
Lane 1a runner artifact:         lane1a_runner.py (23a480e7...)
Wrapper artifact:                lane1a_runner_wrapper.py (4bed7fbd...)
Sidecar schema artifact:         lane1a_sidecar.schema.json (23195986...)
Updated config:                  runner_config.yaml (bbb4655e...)
Updated tests:                   test_lane1a_packet.py (934f3977...)
LOCK-RECORD:                     68edbdcd... (PENDING_TEAM_LEAD_REVIEW)
Native B1 v2 execution claim:    REMOVED
B1 v2 source:                    UNEDITED (verified)
B1 v2.1:                         NOT CREATED OR USED
First data access:               NOT EXECUTED
All non-Lane-1a execution gates: CLOSED
```

CS posture: **HOLD for Senior intent-preservation confirmation and
Team Lead combined adversarial review of the Path A packet.**

— CS Engineer, 2026-06-10
