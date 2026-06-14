# Manager / Team Lead Direction — Lane 1a Runtime Environment Remediation (Path E.1)

From: Elias / Manager
To: CS Engineer
Cc: Senior Engineer, Team Lead, New Senior Engineer
Date: 2026-06-10
Status: Path E.1 selected; CS executing remediation; first data access NOT authorized

---

## Verbatim memo (summary)

> Manager / Team Lead accepts deviation at commit `b3ce758`. The
> reported failure is an instrument failure, not a measurement
> result. The current attempt is archived as
> `instrument_failure_before_model_load`. Manager selects **Path E.1**:
>
> - New sweep_id (e.g., `lane-1a-2026-06-11`)
> - New LOCK-RECORD
> - Production-path subprocess smoke test (spawns the production
>   subprocess exactly as production will; verifies import success;
>   verifies required dependency versions; records interpreter path)
> - Explicit Python interpreter path / invocation mechanism in
>   LOCK-RECORD; no ambiguous PATH resolution
> - Unit/integration test proving production subprocess uses the
>   intended interpreter
> - Preserve sidecar, MODEL_ID, no-reexecution, artifact-boundary
>   protections.
>
> Standing rule extension accepted: *"Any artifact that invokes a
> subprocess in production must include a production-path smoke test
> that spawns that subprocess exactly as production will, verifies
> import success, verifies required dependency versions, and records
> the interpreter path."*
>
> CS return (14 items) + Senior intent-preservation review + Team Lead
> combined re-review + Manager re-reauthorization before any new first
> data access.
>
> — Elias / Manager

---

## CS acknowledgement and execution declaration

CS confirms:

1. **Path E.1 authorized.** New `sweep_id = "lane-1a-2026-06-11"`.
2. **Prior attempt archived** as `instrument_failure_before_model_load`.
   The prior `AUDIT-LOG.ndjson` is renamed to
   `AUDIT-LOG-2026-06-10-INSTRUMENT-FAILURE.ndjson` and preserved in
   the experiment directory for audit. The 31 logged `runner_started`
   events remain bound to `sweep_id = "lane-1a-2026-06-10"` and have
   no effect on the new sweep_id's no-re-execution accounting (the
   wrapper checks rung+stratum within its current audit log).
3. **Explicit Python interpreter** declared in `runner_config.yaml`
   under a new `production:` section and asserted in
   `lane1a_runner_wrapper.py` as a `PRODUCTION_PYTHON` constant.
   Cross-reference test asserts the two values match byte-for-byte.
4. **Subprocess smoke test** added: spawns the production subprocess
   with `--validate-only`; verifies import surface; checks `mlx_lm`
   version against the locked expected value.
5. **B1 v2 still UNEDITED.** No new imports from B1 v2; the runtime
   environment is the only thing CS is fixing.
6. **B1 v2.1 not created.** No new harness capability.
7. **Standing rule extension** accepted; filed at
   `governance/standing/STANDING-REVIEW-DISCIPLINE.md` in this
   remediation cycle.
8. **No first data access this commit.** No model load. No live
   outputs.

— CS Engineer, 2026-06-10
