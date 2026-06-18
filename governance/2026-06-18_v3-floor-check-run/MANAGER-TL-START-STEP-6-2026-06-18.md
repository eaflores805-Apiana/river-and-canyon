# Start Memo — Execute V3 Floor Check Step 6

**To:** CS Engineer / External Execution Operator
**Cc:** Senior Engineer, Team Lead, Manager
**From:** Manager / Team Lead
**Subject:** Start Step 6 — V3 Floor Check Model Execution
**Status:** START AUTHORIZED — Step 6 only

Begin **Step 6** of the V3 Floor Check.

This memo starts model execution only, under the existing Manager by-name authorization.

## Run target

Use the committed V3 Floor Check artifacts:

```text
experiments/2026-06-18_v3-floor-check-run/items/
experiments/2026-06-18_v3-floor-check-run/prompts/
experiments/2026-06-18_v3-floor-check-run/manifest.json
```

Run the prepared prompt set:

```text
96 items × 4 contexts = 384 prompts
```

Contexts:

```text
composite
hop1
hop2
direct_query
```

## Model/run profile

Run the authorized FP16 floor check only:

```text
model: Qwen2.5-3B-Instruct
precision: FP16
decoding: greedy
prompt source: committed prompt files only
```

Do not regenerate, rewrite, reorder, or edit prompts.

## Required outputs

Commit results under:

```text
experiments/2026-06-18_v3-floor-check-run/scored/<item>/<context>.json
experiments/2026-06-18_v3-floor-check-run/r6_log.json
experiments/2026-06-18_v3-floor-check-run/run_record.json
```

Each scored context JSON must use:

```json
{
  "item": "...",
  "context": "composite | hop1 | hop2 | direct_query",
  "ground_truth": "...",
  "predicted": "...",
  "match": true
}
```

Use `false` for `match` when the prediction does not equal the locked ground truth.

The R6 log must use:

```json
{
  "<item>": ["invalidator_name"]
}
```

Allowed invalidator names only:

```text
terminal_coincidence
controls_unavailable
direct_recall
interior_position
constant_token
```

If no invalidator fires for an item, record an empty list.

The run record must include:

```text
model name
model revision / commit sha
precision / dtype
decoding profile
execution host
runtime/library versions
timestamp
operator
confirmation prompts were consumed exactly as committed
confirmation no prompt regeneration occurred
```

## After outputs land

CS will run the locked analyzer:

```text
python3 path-a/build/v3_floor_check_analyzer.py \
  --scored-dir experiments/2026-06-18_v3-floor-check-run/scored \
  --r6-log experiments/2026-06-18_v3-floor-check-run/r6_log.json \
  --admissibility experiments/2026-06-18_v3-floor-check-run/admissibility_summary.json \
  --prompt-conformance experiments/2026-06-18_v3-floor-check-run/prompt_conformance_summary.json \
  --output experiments/2026-06-18_v3-floor-check-run/analyzer_decision.json
```

## Boundaries

This authorizes only Step 6 model execution.

Do not perform:

```text
compression
INT8
INT4
rerun
prompt edits
prompt regeneration
post-hoc slicing
floor adjustment
tooling edit after data
Claim C
Paper B
certification claim
capability claim
mechanism claim
```

The Path A FP16 K=5 FAIL remains closed.

## Required return

Return:

```text
CS / Execution Return — V3 Floor Check Step 6 Complete
```

Include:

```text
commit
final remote HEAD
clean-fetch confirmation
scored output paths and hashes
r6_log path and hash
run_record path and hash
model/run profile
confirmation 384 prompts were executed exactly once
confirmation no prompt edits or regeneration occurred
```

— Manager / Team Lead
