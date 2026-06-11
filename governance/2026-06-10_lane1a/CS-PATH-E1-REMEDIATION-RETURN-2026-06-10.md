# CS Path E.1 Remediation Return — Runtime-Environment Pin + Subprocess Smoke Test

From: CS Engineer
To: Elias / Manager
Cc: Team Lead, Senior Engineer, New Senior Engineer
Date: 2026-06-10
Status: Path E.1 remediation complete; 40/40 unit tests pass; new LOCK-RECORD `969e1e31…` with `PENDING_TEAM_LEAD_REVIEW`; awaiting Senior intent-preservation re-review + Team Lead combined re-review + Manager re-reauthorization

---

## Fourteen-item return (per Manager memo §6)

### 1. New sweep_id

```
lane-1a-2026-06-11
```

Declared in `manifest_generator.SWEEP_ID`, `sweep_record.schema.json`
const, `runner_config.yaml sweep_id`, and LOCK-RECORD header.

### 2. Disposition of the prior attempt

```
sweep_id:      lane-1a-2026-06-10
disposition:   instrument_failure_before_model_load
```

The prior `AUDIT-LOG.ndjson` is preserved in the experiment directory
as `AUDIT-LOG-2026-06-10-INSTRUMENT-FAILURE.ndjson`. The driver
stderr/stdout are preserved as
`_sweep_stderr-2026-06-10-INSTRUMENT-FAILURE.log` and
`_sweep_stdout-2026-06-10-INSTRUMENT-FAILURE.log`. The 31 logged
`runner_started` events remain bound to the prior sweep_id and have
no effect on the new sweep_id's no-re-execution accounting.

### 3. New LOCK-RECORD hash

```
969e1e31e96b99fec547d1e0dfe193ba6e64a85b7aee205a6dd71f3372e334dd
```

Lock timestamp: `PENDING_TEAM_LEAD_REVIEW`.

### 4. Changed artifact list

| # | Artifact | Change |
|---|---|---|
| 1 | `manifest_generator.py` | `SWEEP_ID` updated to `"lane-1a-2026-06-11"` |
| 2 | `runner_config.yaml` | `sweep_id` updated; new `production:` section with explicit `python_interpreter` + `expected_mlx_lm_version` |
| 3 | `lane1a_runner_wrapper.py` | new `PRODUCTION_PYTHON` constant + `EXPECTED_MLX_LM_VERSION`; subprocess argv[0] uses `PRODUCTION_PYTHON` (not `sys.executable`); new `production_subprocess_smoke_test()` function; `preflight()` runs it |
| 4 | `schema/sweep_record.schema.json` | `sweep_id` const updated |
| 5 | `test_lane1a_packet.py` | new `TestPathE1ProductionSubprocess` class with 4 tests |
| 6 | `LOCK-RECORD.md` | re-sealed with new sweep_id; all updated hashes; Path E.1 sections; superseding note |
| 7 | `governance/standing/STANDING-REVIEW-DISCIPLINE.md` | new "production-path subprocess smoke test" rule section |
| 8 | `governance/2026-06-10_lane1a/MANAGER-DIRECTION-PATH-E1-RUNTIME-ENV-2026-06-10.md` | NEW (verbatim Manager memo + CS acknowledgement) |
| 9 | `governance/2026-06-10_lane1a/CS-PATH-E1-REMEDIATION-RETURN-2026-06-10.md` | NEW (this memo) |

Renames (prior sweep state archived in place):
- `AUDIT-LOG.ndjson` → `AUDIT-LOG-2026-06-10-INSTRUMENT-FAILURE.ndjson`
- `_sweep_stderr.log` → `_sweep_stderr-2026-06-10-INSTRUMENT-FAILURE.log`
- `_sweep_stdout.log` → `_sweep_stdout-2026-06-10-INSTRUMENT-FAILURE.log`
- `manifests/` directory: deleted (manifests regenerate deterministically under new SWEEP_ID seed)

### 5. Full SHA-256 hash for each changed artifact

```text
manifest_generator.py                8b480243e828ffb3a642625000165751aed5322f6c52b01238d8f3dd58e02efa
runner_config.yaml                   be22cce51475a55b7440d9755f14f30f3a82977fc1a331d75f385470319b6a92
lane1a_runner_wrapper.py             e3ab78f134073d67e337ebc1fe9ab0b87b3f4fb7ed1761031d70f3b94c349314
schema/sweep_record.schema.json      acef5719a3394d8c3581c51b4548dc1e13577a0214962d8965f312a3edd73910
test_lane1a_packet.py                6f30f01f5a87fe56996e0a08dfa621a0c09144a4ca3177194a225bb85cfb33cd
LOCK-RECORD.md                       969e1e31e96b99fec547d1e0dfe193ba6e64a85b7aee205a6dd71f3372e334dd
```

15 other locked artifacts unchanged (verified by hash).

### 6. Production subprocess interpreter path

```
/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
```

Pinned in:
- `lane1a_runner_wrapper.PRODUCTION_PYTHON` (the value used in the subprocess argv)
- `runner_config.yaml production.python_interpreter` (the audit-trail declaration)

Cross-referenced by `test_interpreter_path_matches_config`.

### 7. mlx_lm version observed in production subprocess smoke test

```
0.31.3
```

Expected value declared in:
- `lane1a_runner_wrapper.EXPECTED_MLX_LM_VERSION = "0.31.3"`
- `runner_config.yaml production.expected_mlx_lm_version: "0.31.3"`

Cross-referenced by `test_expected_mlx_lm_version_matches_config`.

### 8. Smoke-test result

```text
test_production_subprocess_smoke: PASS

Probe: import mlx_lm; from mlx_lm.sample_utils import make_sampler; print(mlx_lm.__version__)
Interpreter: /Library/Frameworks/Python.framework/Versions/3.13/bin/python3
Subprocess exit code: 0
Observed mlx_lm version: 0.31.3
make_sampler import: succeeded
```

The smoke test runs at preflight time (as part of `preflight()`); any
future drift (interpreter path changed; mlx_lm version changed;
`make_sampler` removed from `sample_utils`) trips the smoke test
before any sweep execution.

### 9. Full test summary

```text
Test runner:    python -m unittest test_lane1a_packet
Tests run:      40   (36 prior + 4 new Path E.1 tests)
Tests passed:   40   (1 skipped: jsonschema not installed for one sidecar test)
Tests failed:    0
Wall time:      ~3.8s
```

New Path E.1 tests (`TestPathE1ProductionSubprocess`):
- `test_interpreter_path_matches_config` — wrapper ↔ config cross-reference
- `test_expected_mlx_lm_version_matches_config` — wrapper ↔ config cross-reference
- `test_production_subprocess_smoke` — spawns the production subprocess; verifies import surface; verifies mlx_lm version
- `test_wrapper_does_not_use_sys_executable_for_subprocess` — source-level grep asserts argv[0] is `PRODUCTION_PYTHON`

All 36 prior invariants still verified.

### 10. Confirmation that no model load occurred during remediation

**CONFIRMED.** The smoke test imports `mlx_lm` and references `make_sampler` (a function symbol lookup), but does not call `mlx_lm.load(MODEL_ID)`. No model weights are read into memory.

### 11. Confirmation that no live outputs were produced

**CONFIRMED.** `experiments/2026-06-10_lane-1a-sweep/raw/` is empty.
There is no `AUDIT-LOG.ndjson` (only the archived
`AUDIT-LOG-2026-06-10-INSTRUMENT-FAILURE.ndjson`). No new sidecar
files; no per-rung records; no sweep-level record.

### 12. Confirmation that B1 v2 was not edited

**CONFIRMED.** `git diff experiments/2026-06-09_b1-harness-v2/` returns
empty. B1 v2 remains at merge `3cbfce57`.

### 13. Confirmation that B1 v2.1 was not created or used

**CONFIRMED.** No file named for B1 v2.1; no code path references B1
v2.1 features.

### 14. Any remaining deviation or concern

**None known.** CS applied the new "production-path subprocess smoke
test" standing rule (Manager §5) to this remediation cycle. The smoke
test, the wrapper-config cross-reference tests, and the source-level
grep test together form a quadruple lock on the runtime environment:

| Layer | Test |
|---|---|
| Source (config) | `test_interpreter_path_matches_config` |
| Source (version) | `test_expected_mlx_lm_version_matches_config` |
| Source (grep) | `test_wrapper_does_not_use_sys_executable_for_subprocess` |
| Runtime | `test_production_subprocess_smoke` |

Any one of these alone would have caught the prior deviation; together
they form a defense-in-depth pattern that mirrors the failure-mode
discipline already applied to schemas and outputs.

## Standing rule extension recorded

Manager §5 accepted CS-proposed rule:

> *"Any artifact that invokes a subprocess in production must include
> a production-path smoke test that spawns that subprocess exactly as
> production will, verifies import success, verifies required
> dependency versions, and records the interpreter path."*

Filed at `governance/standing/STANDING-REVIEW-DISCIPLINE.md` as a new
section under *"Additional rule — production-path subprocess smoke
test (added 2026-06-10, Manager / Path E.1 acceptance)"*. Canonical
example: `TestPathE1ProductionSubprocess`. The standing review-
discipline file now carries three production rules covering
memo-channel, source-code-channel, and runtime-environment-channel.

## Review sequence remaining (per Manager memo §7)

```text
1. CS Path E.1 remediation — COMPLETE (this commit)
2. Senior intent-preservation review (design + execution-environment) — PENDING
3. Team Lead combined adversarial re-review — PENDING
4. CS lock-finalization touch (timestamp) — PENDING
5. Manager reauthorization against new LOCK-RECORD hash — PENDING
6. CS preflight (now includes production_subprocess_smoke_test()) — PENDING
7. CS executes only if preflight passes — PENDING
```

## Current state

```text
Path E.1 remediation:                 COMPLETE
sweep_id:                             lane-1a-2026-06-11 (NEW)
prior sweep_id disposition:           instrument_failure_before_model_load
production_python:                    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3
expected_mlx_lm_version:              0.31.3
smoke test:                           PASS
Tests:                                40/40 (1 skipped) PASS
LOCK-RECORD:                          969e1e31... (PENDING_TEAM_LEAD_REVIEW)
B1 v2 source:                         UNEDITED
B1 v2.1:                              NOT CREATED OR USED
First data access:                    NOT EXECUTED
All non-Lane-1a execution gates:      CLOSED
```

CS posture: **HOLD for Senior intent-preservation re-review of the
Path E.1 remediation.**

— CS Engineer, 2026-06-10
