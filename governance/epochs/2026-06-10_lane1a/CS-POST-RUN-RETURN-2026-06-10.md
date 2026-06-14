# CS Post-Run Return — Lane 1a Sweep `lane-1a-2026-06-11` Complete

From: CS Engineer
To: Elias / Manager
Cc: Team Lead, Senior Engineer, New Senior Engineer
Date: 2026-06-10 (UTC: 2026-06-11)
Status: Sweep executed cleanly; 32/32 generations succeeded; **K = 0 (unoccupied window)**; outputs are reconnaissance-only per Lane 1a doctrine

---

## 0. TL;DR

```text
sweep_id:                    lane-1a-2026-06-11
lock timestamp:              2026-06-11T03:37:50Z
first_data_access timestamp: 2026-06-11T03:42:54.391+00:00  (postdates lock by ~5 min)
sweep_complete timestamp:    2026-06-11T03:55:46.739+00:00  (~12.9 min wall clock)
analysis_completed:          2026-06-11T04:01:19.655+00:00

Generations:
  planned:       1,536
  attempted:     1,536 (32 invocations across 8 rungs × 4 strata)
  succeeded:     1,536
  re-execution:  0
  anomalies:     0

Outputs (all on disk under experiments/2026-06-10_lane-1a-sweep/):
  raw/*.json                          32 (one per [rung,stratum] invocation)
  raw/*.lane1a.sidecar.json           32 (one per invocation; byte-preservation verified)
  sweep_record.json                   sha256 f10f777c534218a203f3bd030aabe4966d8f51e69a82b20b8b40cce1ab848328
  AUDIT-LOG.ndjson                    sha256 cf02549b6ed5ea08af00bbb2214f563ec06e98afc5dc3f9094c5c025f1269b73
  figures/diag_*.png                  8 per-rung diagnostic-point panels
  figures/rung_label_grid.png         1 rung × label categorical grid

K = 0  (no surviving rungs)
Survivors:  []
Fixed outcome statement: STATEMENT_A (unoccupied window) + STATEMENT_C (winner's-curse)

  "The certification window, while logically nonempty, was unoccupied
   for this task family at this scale: every rung carried at least
   one elimination label under the pre-registered sweep classification."

  + (always-append)

  "Any construction examined after this sweep is expected to perform
   worse during fresh certification than during sweep exploration;
   regression from sweep behavior is not instrument failure and must
   not be used to tune thresholds."
```

## 1. Seventeen-item return (per Manager memo §7)

### 1. Final post-touch LOCK-RECORD hash

```text
5b557ae2a4c90bf34d2c050dc2b713b0ae29c2dd4eeb1f54a4099b5fb6cd5869
```

### 2. Lock timestamp

```text
2026-06-11T03:37:50Z
```

### 3. First-data-access timestamp

```text
2026-06-11T03:42:54.391+00:00
```

(Recorded by the wrapper's `preflight()` at the moment the
production-subprocess smoke test passed and the first model load was
authorized.)

### 4. Confirmation that first data access postdated lock timestamp

**CONFIRMED.** `2026-06-11T03:42:54.391Z` > `2026-06-11T03:37:50Z` (~5 min margin).

### 5. Preflight result

22/22 PASS (Manager §4 list). Item 4 (manifest-hash match) verified
via canonical-form comparison consistent with
`manifest_generator.manifest_sha256()`; on-disk JSON is indented for
human readability but hashes against canonical-form (`sort_keys=True`,
`separators=(",", ":")`) match `MANIFEST-HASHES.lock` 8/8. Production
subprocess smoke test PASS: interpreter
`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`;
mlx_lm 0.31.3; `make_sampler` importable.

### 6. Final audit log

`experiments/2026-06-10_lane-1a-sweep/AUDIT-LOG.ndjson`
sha256 `cf02549b6ed5ea08af00bbb2214f563ec06e98afc5dc3f9094c5c025f1269b73`

```
event counts:
  first_data_access     1
  runner_started       32
  runner_completed     32
  sweep_complete        1
  analysis_started      2   (analyzer was re-run once after a stdout formatting fix; both runs produce the same scoring)
  analysis_completed    1
  plot_generated        9   (8 diagnostic panels + 1 categorical grid)

  total                78 lines
```

No `runner_anomaly` events. No `re_execution_refused` events.

### 7. Per-rung result records

Embedded in `sweep_record.json["rungs"]`. Summary:

| rung | strict_acc | content_acc | gap (c−s) | control_acc | union_envelope | labels |
|---|---|---|---|---|---|---|
| L01 | 0.963 | 0.975 | 0.012 | 0.925 | (per record) | 4 — env / token / **headroom** / abstention |
| L02 | 0.825 | 0.925 | 0.100 | 0.863 | | 3 — env / token / abstention |
| L03 | 0.713 | 0.875 | 0.162 | 0.762 | | 4 — env / token / **gap** / abstention |
| L04 | 0.988 | 0.988 | 0.000 | 0.975 | | 4 — env / token / **headroom** / abstention |
| L05 | 0.912 | 0.950 | 0.037 | 0.887 | | 4 — env / token / **headroom** / abstention |
| L06 | 0.850 | 0.887 | 0.037 | 0.938 | | 3 — env / token / abstention |
| L07 | 0.850 | 0.963 | 0.113 | 0.863 | | 3 — env / token / abstention |
| L08 | 0.887 | 0.963 | 0.075 | 0.887 | | 3 — env / token / abstention |

(Full records — including SEs, `void_count` per stratum, full
`union_envelope_score`, `max_dummy_score`, `headroom`,
`abstention_rate`, flags — in `sweep_record.json`.)

### 8. Sweep-level record

`experiments/2026-06-10_lane-1a-sweep/sweep_record.json`
sha256 `f10f777c534218a203f3bd030aabe4966d8f51e69a82b20b8b40cce1ab848328`

Conforms to `schema/sweep_record.schema.json` shape (additional
property guards on `framework_version: "none"`, sweep_id const,
artifact_class / certification_relevance const).

### 9. Output artifact hashes

```text
sweep_record.json:    f10f777c534218a203f3bd030aabe4966d8f51e69a82b20b8b40cce1ab848328
AUDIT-LOG.ndjson:     cf02549b6ed5ea08af00bbb2214f563ec06e98afc5dc3f9094c5c025f1269b73

raw/                  32 runner-output JSON files (preserved byte-for-byte by the wrapper)
                      32 *.lane1a.sidecar.json companion files (each carries the b1-compatible
                      pattern: runner_output_path, runner_output_sha256, wrapper_attestation
                      with const-locked Lane 1a tags, context_functional_statement >= 200 chars)

figures/              8 per-rung diagnostic point panels + 1 categorical grid
                      (each carries the mandatory artifact-tag footer +
                      fixed_outcome_statement preview at bottom)
```

(Full per-output sha256 list will be appended to `sweep_record.json`
if Manager requests; currently embedded in each sidecar's
`runner_output_sha256` field.)

### 10. Test / validation summary

```text
pre-sweep:      40/40 tests PASS (36 prior + 4 Path E.1 tests; 1 jsonschema skip)
sweep-time:     22/22 preflight items PASS (Manager §4 list)
post-sweep:     32/32 runner_completed events;
                0 runner_anomaly;
                0 re_execution_refused;
                analysis driver assigned all per-rung labels via
                locked analyzer.assign_labels() with B1 gap sign +
                B2 inconclusive preempt + B3 control denom 80
```

### 11. Confirmation that no re-execution occurred

**CONFIRMED.** No `re_execution_refused` events in audit log. No
`runner_started` event for any (rung_id, stratum) pair beyond its
first attempt. The no-re-execution rule held — every rung+stratum had
exactly one attempt.

### 12. Confirmation that B1 v2 was not edited

**CONFIRMED.** `git diff experiments/2026-06-09_b1-harness-v2/` is
empty. B1 v2 remains at merge `3cbfce57`.

### 13. Confirmation that B1 v2.1 was not used

**CONFIRMED.** No file under `experiments/` named for B1 v2.1; no code
path imports B1 v2.1 features. The `mlx_lm` dependency is shared with
B1 v2 but at the third-party library layer only.

### 14. Fixed outcome statement emitted

Emitted by `analyzer.emit_outcome()` per the deterministic K-rule
(K = 0 since no rung's labels list equals `["requires_further_investigation"]`).
Embedded in `sweep_record.json["fixed_outcome_statement"]` verbatim:

```text
The certification window, while logically nonempty, was unoccupied
for this task family at this scale: every rung carried at least one
elimination label under the pre-registered sweep classification.

Any construction examined after this sweep is expected to perform
worse during fresh certification than during sweep exploration;
regression from sweep behavior is not instrument failure and must
not be used to tune thresholds.
```

### 15. Inconclusive_not_actionable rungs

**NONE.** Every rung was measurable. `void_count_total > 5` was not
triggered on any rung (per-rung total voids stayed well within
budget). `harness_anomaly_flag = false` on every rung.
`missing_required_outputs_flag = false` on every rung. The B2 preempt
rule did not fire anywhere; every rung went through the full
classification path and accumulated its multi-attach label set.

### 16. Any failure, anomaly, or deviation

**NONE.** No `runner_anomaly` events. No re-execution attempts. No
mismatch between wrapper-recorded `runner_output_sha256` and on-disk
file hash. No deviation between the smoke-test-verified production
interpreter and the interpreter that ran. The execution itself was
clean.

(For audit-trail completeness: prior CS deviations of the day — B1 v2
manifest interface, MODEL_ID, runtime env / mlx_lm — were all
remediated through Path A / A.1 / E.1 before this sweep started.
Those deviations are documented in their respective CS deviation
reports under `governance/2026-06-10_lane1a/`. No new deviation
surfaced during this execution.)

### 17. Confirmation that Lane 1a outputs remain negative-use only

**CONFIRMED.** Lane 1a outputs are negative-use only. Per the §1.10
exclusion block embedded verbatim in `sweep_record.json["exclusion_block"]`:

> *"Lane 1a outputs are excluded from threshold design, excluded from
> certification evidence, and excluded from the D6 historical-information
> allowance for threshold derivation. A later Candidate Selection Memo
> may cite this sweep only for coarse elimination; it may not rank,
> prefer, shortlist, or positively justify any construction from it.
> A later threshold-sheet process must attest: 'No statistic computed
> in Lane 1a was copied into any threshold-sheet field, directly or by
> transformation.'"*

K = 0 means the sweep eliminated every rung — there is no survivor
set to rank, prefer, or shortlist. The negative finding stands: the
**certification window was unoccupied for this task family at this
scale**. Future Candidate Selection memos may cite this sweep only
for that coarse elimination.

## 2. Substantive read of the result

CS submits this section as informational context, not as a Lane 1a
output. The reasoning is for Senior/Team Lead/Manager to interpret;
Lane 1a's output is the K=0 verdict + per-rung label set.

The all-rungs-eliminated outcome arises from three converging signals
that fired on essentially every rung:

1. **`accuracy_indistinguishable_from_token_prior`** (8/8).
   `strict_acc − control_acc ≤ 2·SE_diff` everywhere. The token-prior
   control (80 answerable-mirror prompts with scrambled bindings)
   scored within ~5 percentage points of the candidate on every rung.
   Strong indication that the model is relying on token-prior /
   surface patterns rather than actual retrieval through the
   in-context list.

2. **`accuracy_indistinguishable_from_declared_policy_envelope`**
   (8/8). The union of the 5 declared dummy policies
   (pure_last_position, target_recency, salient_endpoint,
   copy_completion, homogeneous_prefix_completion) collectively
   accounts for ≥ candidate accuracy on every rung. Whatever the
   model is doing, the declared shortcut family explains it.

3. **`abstention_contract_instability`** (8/8). NULL-stratum
   abstention rate fell outside the locked band `[0.50, 0.95]` on
   every rung. The model is answering when it should abstain.

Two additional findings on specific rungs:

- **`insufficient_measurement_headroom`** (L01, L04, L05). Near
  ceiling: `strict_acc ≥ 1 − 3·SE(p̂)`. A plausible retention drop
  would sit inside finite-N noise.

- **`strict_content_gap_instability`** (L03 only). `gap = 0.162 ≥
  0.15`. Strict-vs-content scoring divergence on L03's specific
  D=16/K=low/base configuration; flagged for tokenization/format
  follow-up if anyone ever revisits this task family.

The interpretation: at this scale, on this task family, this model
cannot be cleanly used as a certification substrate. The sweep
delivered exactly the negative finding it was authorized to produce.

## 3. Standing posture

All execution gates other than Lane 1a packet preparation + this sweep
remain CLOSED. Specifically and explicitly:

```text
Candidate selection memo:                NOT AUTHORIZED
Candidate ranking / shortlist:           NOT AUTHORIZED
Threshold-sheet population / lock:       NOT AUTHORIZED
Certification evaluation:                NOT AUTHORIZED
INT8/INT4 stress-retention run:          NOT AUTHORIZED
B1 v2.1 implementation:                  NOT AUTHORIZED
Claim C activation:                      NOT AUTHORIZED
Fork A reactivation:                     NOT AUTHORIZED
Paper 6 activation:                      NOT AUTHORIZED
Public benchmark packaging:              NOT AUTHORIZED
```

No statistic from this sweep may be copied into any threshold-sheet
field. No survivor exists to be selected. The K=0 verdict closes the
Lane 1a window for this task family at this scale.

— CS Engineer, 2026-06-10
