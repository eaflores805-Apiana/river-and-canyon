# CS Deviation Report — Python Environment / mlx_lm Version Mismatch (Sweep Failed at Import; No Model Load; No Successful Generations)

From: CS Engineer
To: Elias / Manager
Cc: Team Lead, Senior Engineer, New Senior Engineer
Date: 2026-06-10
Status: Sweep execution failed instrument-side; first data access INCOMPLETE; Manager direction required

---

## 0. TL;DR

```text
Manager reauthorization received and acknowledged.
LOCK-RECORD finalization touch executed (timestamp 2026-06-11T03:05:57Z);
  post-touch hash: 270078a0f3321d5b2698372bdb9b6d22ceec11c3fa1a3bbab750d56e85de5554
17-item preflight: 17/17 PASS.
Sweep driver launched via background nohup.

DEVIATION:
  wrapper uses sys.executable for subprocess; sys.executable in the
  background context resolved to /opt/anaconda3/bin/python (anaconda
  Python 3.10 in PATH).
  anaconda's mlx_lm is version 0.19.3 — older API without
  `make_sampler` in `mlx_lm.sample_utils`.
  System Python 3.13 has mlx_lm 0.31.3 with `make_sampler`.

  Every subprocess invocation of lane1a_runner.py hit:
    ImportError: cannot import name 'make_sampler' from 'mlx_lm.sample_utils'
  BEFORE mlx_lm.load() was ever called.

Sweep state:
  31 runner_started events recorded
  30 runner_anomaly events recorded (the 31st was the in-flight
     invocation killed by CS to prevent burning all 32 attempts)
  0 generations completed
  0 raw outputs written (raw/ directory is empty)
  0 sidecar files written
  No model load occurred (import failed before load() call).

CS killed the sweep when the pattern became clear.

The 31 logged (rung_id, stratum) pairs are now subject to the
no-re-execution rule and cannot be re-attempted within this sweep
without fresh Manager authorization.
```

## 1. The defect

`lane1a_runner_wrapper.py` invokes the runner via subprocess:

```python
cmd = [sys.executable, str(LANE1A_RUNNER), ...]
proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
```

`sys.executable` in the wrapper context is the Python interpreter
running the wrapper module. In the production environment, that
resolved to `/opt/anaconda3/bin/python` (anaconda Python 3.10), which
has `mlx_lm 0.19.3` — an older release that does not expose
`make_sampler` from `mlx_lm.sample_utils`.

The runner mirrors B1 v2's import pattern:

```python
# lane1a_runner.py (mirrors B1 v2 runner_b1_v2.py line 844)
from mlx_lm.sample_utils import make_sampler
```

This import succeeds on `mlx_lm 0.31.3` but fails on `0.19.3` with:

```
ImportError: cannot import name 'make_sampler' from 'mlx_lm.sample_utils'
(/opt/anaconda3/lib/python3.10/site-packages/mlx_lm/sample_utils.py)
```

The failure is at module import time, **before** `mlx_lm.load(MODEL_ID)`
is called. No model bytes were read; no inference was performed.

## 2. Why the preflight passed

The Manager-listed 17-item preflight verified hashes, schemas, locked
constants, lock-timestamp ordering, no-prior-attempts — all
infrastructure invariants. It did NOT include a runtime smoke test of
`subprocess.run([sys.executable, str(LANE1A_RUNNER), "--validate-only"])`,
which would have caught this at preflight time rather than at sweep
time.

CS's earlier `mlx_lm availability` check (filed at commit `a37ca24`)
also missed this because it ran in the preflight script's interpreter
(Python 3.13 with mlx_lm 0.31.3), not in the subprocess's interpreter
(anaconda Python 3.10 with mlx_lm 0.19.3). The two interpreters have
different mlx_lm versions.

This is consistent with the prior two deviations: the unit-test surface
covered Python-logic invariants on synthetic inputs but did not
cross-reference the actual runtime subprocess execution environment
against B1 v2's runtime environment.

## 3. Audit-log state

```text
event counts:
  first_data_access:  1
  runner_started:    31
  runner_anomaly:    30   (the 31st invocation was killed mid-flight by CS;
                           the wrapper did not get to write its anomaly)
  runner_completed:   0
  sweep_complete:     0   (the driver did not finish; CS killed it)

(rung_id, stratum) pairs with runner_started — now blocked from re-execution
under the no-re-execution rule:
  L01/answerable, L01/null, L01/answerable_mirror, L01/null_mirror
  L02/answerable, L02/null, L02/answerable_mirror, L02/null_mirror
  L03/answerable, L03/null, L03/answerable_mirror, L03/null_mirror
  L04/answerable, L04/null, L04/answerable_mirror, L04/null_mirror
  L05/answerable, L05/null, L05/answerable_mirror, L05/null_mirror
  L06/answerable, L06/null, L06/answerable_mirror, L06/null_mirror
  L07/answerable, L07/null, L07/answerable_mirror, L07/null_mirror
  L08/answerable, L08/null, L08/answerable_mirror  (L08/null_mirror was
                                                    NOT yet started when
                                                    CS killed the driver)
```

The audit log is append-only by design. It records honestly that the
sweep was started and failed at every attempt due to the import error.

## 4. Why this is structurally different from prior deviations

The first two deviations (manifest interface incompatibility; MODEL_ID
mismatch) were caught **before** any first data access; the audit log
was empty; no `runner_started` events existed; recovery was a clean
re-seal of the LOCK-RECORD followed by a fresh review chain.

This deviation occurred **after** the LOCK-RECORD was finalized and
the wrapper successfully passed preflight. The audit log now contains
31 `runner_started` events. The no-re-execution rule was designed to
prevent selective re-running of "ambiguous-looking" rungs as a
backdoor selection channel; it was not designed for instrument-failure
recovery.

That said: **no actual data was accessed.** No model load completed.
No item was scored. No raw output was written. The sweep's
"first_data_access" event was emitted by the wrapper's preflight per
the locked design, but the actual first data access (mlx_lm load() +
stream_generate()) never occurred in any subprocess. This is a real
distinction Manager may want to consider when deciding the
remediation path.

## 5. Available remediation paths

CS lists options for Manager decision. CS does not act on any of
them without authorization.

### Path E.1 — New sweep_id; new LOCK-RECORD; fresh review chain (CLEAN BUT EXPENSIVE)

Treat the failed sweep as terminated. Produce a new sweep packet under
a new `sweep_id` (e.g., `lane-1a-2026-06-11`) with:
- Wrapper updated to use an explicit Python interpreter path (or to
  spawn the runner via `exec(...)` inside the wrapper process,
  guaranteeing same-interpreter execution).
- New unit test: wrapper subprocess uses a Python interpreter whose
  `mlx_lm.sample_utils.make_sampler` is importable.
- New unit test: wrapper subprocess execution path is the canonical
  Python 3.13 + mlx_lm 0.31.3 environment (cross-referenced against
  B1 v2's documented runtime environment if available).
- New LOCK-RECORD.
- Senior intent-preservation + Team Lead combined adversarial review
  + Manager reauthorization.

**Cost:** full review-chain replay.
**Risk:** none beyond the cost.

### Path E.2 — Authorized audit-log annotation; re-attempt within current sweep (UNCONVENTIONAL)

Manager authorizes CS to append a special audit-log event
(`runner_started_retroactively_classified_as_preflight_extension`)
for each of the 31 logged pairs, explicitly noting that no model load
occurred and no first data access happened in the strict sense. The
wrapper would need a one-shot modification to honor the retroactive
classification (i.e., a `runner_started` followed by
`runner_anomaly: import_error_no_model_load` should not block
re-execution).

**Cost:** wrapper edit + new LOCK-RECORD + new review chain (same as
E.1 in practice, with an additional audit-log fixup component).
**Risk:** introduces an "amnesia" path on the audit log; arguably
weakens the no-re-execution rule conceptually.

**CS does NOT recommend Path E.2.** Cleaner to use E.1.

### Path E.3 — Declare sweep failed-with-zero-evidence; do not re-attempt; archive (HONEST BUT POSSIBLY PREMATURE)

Manager rules that Lane 1a's first authorized data-access attempt
produced no evidence due to instrument failure, and chooses NOT to
re-attempt at this time. CS files the sweep-level record as
`completed_attempts=0` and `anomalies=31`, with the failure mode
documented; no analyzer is run; no plotter is run; the fixed-outcome
statement is not emitted (none of the §1.9 conditions are factually
true).

**Cost:** small.
**Risk:** Lane 1a remains in an "attempted but no evidence" state.
Manager may want to revisit later.

### CS recommendation

**Path E.1.** Clean instrument re-build with a new sweep_id, with
unit tests that cross-reference the subprocess execution environment
against the host Python's mlx_lm version. This is the disciplined
move: the standing sibling-artifact cross-reference rule should now
apply to the **execution environment** as well as to source code
values.

## 6. Standing review-discipline rule extension

The new standing rule (Manager 2026-06-10):

> *"CS production of any artifact that integrates with a locked
> sibling artifact must include a unit test that cross-references
> concrete values against the sibling artifact's source."*

The Lane 1a manifest-interface and MODEL_ID deviations were
**source-side** cross-reference failures. This third deviation is an
**environment-side** cross-reference failure: the runtime mlx_lm
version (the environment running the subprocess) was not
cross-referenced against B1 v2's documented runtime environment.

CS proposes the following extension to the standing rule:

> *"The cross-reference test must include a subprocess-execution
> smoke test: spawn the subprocess used in production (with the
> same interpreter resolution) and verify the runner's import
> surface succeeds in that subprocess. Pure same-process import
> checks are insufficient — they exercise the test runner's
> interpreter, not the runner's."*

CS will propose this extension to the standing review-discipline
file if Manager and Team Lead concur.

## 7. State of every Manager §6 return item (partial; sweep terminated mid-flight)

| # | Item | State |
|---|---|---|
| 1 | Final post-touch LOCK-RECORD hash | `270078a0f3321d5b2698372bdb9b6d22ceec11c3fa1a3bbab750d56e85de5554` |
| 2 | Lock timestamp | `2026-06-11T03:05:57Z` |
| 3 | First-data-access timestamp (audit event) | recorded; but no actual model access occurred |
| 4 | Confirmation that first data access postdated lock | yes (event timestamp) |
| 5 | Preflight result | 17/17 PASS (per Manager's literal list) |
| 6 | Final audit log | 31 runner_started; 30 runner_anomaly; 0 completed; not closed |
| 7 | Per-rung result records | NONE generated |
| 8 | Sweep-level record | NONE generated; sweep_complete event not emitted |
| 9 | Output artifact hashes | NONE generated |
| 10 | Test / validation summary | 36/36 unit tests pass (pre-sweep state); 0 generations completed |
| 11 | No re-execution occurred | confirmed (no re-execution; failures were first-attempt anomalies) |
| 12 | B1 v2 not edited | confirmed |
| 13 | B1 v2.1 not used | confirmed |
| 14 | Fixed outcome statement emitted | none (factually no condition holds) |
| 15 | Inconclusive_not_actionable rungs | by the B2 preempt rule applied at analysis time, all 8 rungs would be inconclusive — but CS has not run the analyzer because the situation is instrument failure, not measurement failure |
| 16 | **Any failure, anomaly, or deviation** | **THIS REPORT.** |
| 17 | STANDING-REVIEW-DISCIPLINE.md | path: `governance/standing/STANDING-REVIEW-DISCIPLINE.md`; sha256: `fa3142e91262cefe10eb246bfbb6799860921d37ef46f360517a6e98276bf5ab` (after Path A.1 addition; CS proposes further extension per §6 above) |

## 8. Standing posture

```text
LOCK-RECORD finalization touch:        EXECUTED (timestamp 2026-06-11T03:05:57Z)
Post-touch LOCK-RECORD hash:           270078a0...
Preflight (Manager's literal 17 items): 17/17 PASS
mlx_lm interpreter cross-reference:    NOT in preflight; would have caught this
Sweep execution:                       FAILED at subprocess import
                                       31 runner_started; 30 runner_anomaly;
                                       0 runner_completed
Raw outputs:                           NONE
Sidecar files:                         NONE
Model load:                            DID NOT OCCUR
B1 v2 source:                          UNEDITED
B1 v2.1:                               NOT CREATED OR USED
Locked artifacts:                      UNMODIFIED
```

CS posture: **STOPPED at instrument-failure discovery; awaiting
Manager direction on Path E.1 / E.2 / E.3.** (CS recommends E.1.)

## 9. Additional note — driver script (`_sweep_driver.py`)

CS produced a small driver script at
`experiments/2026-06-10_lane-1a-sweep/_sweep_driver.py` to orchestrate
the 32 subprocess invocations. The underscore prefix marks it as
non-locked (it is the execution tool, not part of the locked packet;
the LOCK-RECORD does not include its hash). The driver only calls
locked APIs: `preflight()`, `invoke_runner()`, `AuditLogWriter`. It
adds nothing to the locked surface; it does not change Lane 1a's
semantics. CS will retain or remove it per Manager direction.

— CS Engineer, 2026-06-10
