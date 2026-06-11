# Lane 1a Audit Log Format (locked; hash-recorded in LOCK-RECORD.md)

The audit log is append-only NDJSON written by `audit_log.py`. One event
per line. The wrapper, analyzer, and plotter all emit through the same
writer.

## Event schema

```json
{
  "ts": "RFC 3339 timestamp with milliseconds, UTC",
  "event": "<one of the enumerated events below>",
  "rung_id": "L01..L08 or null",
  "attempt_id": "integer >= 1, or null",
  "stratum": "answerable | null | answerable_mirror | null_mirror | null (for non-item events)",
  "details": {
    "artifact_class": "lane-1a-reconnaissance",
    "certification_relevance": "none",
    "...": "event-specific fields"
  }
}
```

## Enumerated events

| `event` | When emitted | Notes |
|---|---|---|
| `lock_record_sealed` | Once at lock time | `details.lock_record_hash` recorded |
| `manifest_generated` | Once per rung at lock time | `details.manifest_hash`, `details.per_rung_seed` |
| `recipe_acceptance_check` | Once per rung at lock time | `details.policies_nondegenerate`, `details.distinct_predictions_count` |
| `novelty_ledger_check` | Once at lock time | `details.construction_inputs_hash`, `details.overlap_fraction` |
| `first_data_access` | Once per sweep | `details.first_access_ts` (must postdate `lock_record_sealed`) |
| `runner_started` | One per generation attempt | `details.attempt_id`, `details.b1v2_invocation_args`, `details.stratum` |
| `runner_completed` | One per successful generation | `details.runner_output_path`, `details.context_override_applied` |
| `runner_anomaly` | If a generation attempt fails or harness anomaly | `details.anomaly_kind`, `details.rung_id`, `details.attempt_id`; rung will receive `inconclusive_not_actionable` |
| `re_execution_refused` | If wrapper sees prior `runner_started` for same `(rung_id, stratum)` | enforces CS 5f no-re-execution rule |
| `analysis_started` | Once per sweep | `details.classification_criteria_hash` |
| `analysis_completed` | Once per sweep | `details.K`, `details.survivor_count` (== K) |
| `plot_generated` | One per figure produced | `details.figure_path`, `details.figure_type` |
| `sweep_complete` | Once per sweep | `details.planned_generation_count`, `details.total_attempt_count` (must equal `planned_generation_count`), `details.zero_re_executions` (must be true) |

## B5 — total_attempts semantics (pinned)

```text
total_attempts = sum of all "runner_started" events
              == candidate_generations + control_generations
Under Option A (Manager-authorized):       768 + 768 = 1,536
Under offline fallback (B4 Option B):      768 +   0 =   768
```

A sweep where `total_attempts != planned_generation_count` indicates
either incomplete execution OR a re-execution attempt (which the
wrapper should have refused). Either way, the sweep is treated as
incomplete and no fixed outcome is emitted; the analyzer instead
records an `inconclusive_not_actionable` label on every affected rung
and routes through the `inconclusive_not_actionable` preempt branch.

## Append-only enforcement

The audit log file is opened with `mode="a"` only. The writer never
seeks or truncates. Any process that attempts to modify a prior event
fails the unit test
`test_lane1a_packet.py::test_audit_log_append_only`.

## B4 — token-prior authorization recording

The `lock_record_sealed` event's `details.token_prior_control_authorization`
field carries the value from LOCK-RECORD.md. The wrapper reads this
value at startup; if it is not the Manager-authorized literal string,
the wrapper enters fallback mode and emits `runner_started` events only
for candidate generations (no control generations). The `sweep_complete`
event then records `total_attempts = 768` under fallback.

## Locked
Edits after lock are prohibited.
