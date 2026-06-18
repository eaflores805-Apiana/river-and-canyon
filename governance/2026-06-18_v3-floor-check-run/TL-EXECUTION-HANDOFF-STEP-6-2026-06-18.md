# Execution Handoff — V3 Floor Check Step 6

**To:** External Execution Surface / CS Execution Operator
**Cc:** CS Engineer, Senior Engineer, Team Lead, Manager
**From:** Team Lead
**Subject:** Execute V3 Floor Check Step 6 — Model Inference Only
**Status:** ACTION — external execution handoff
**Route State:** YELLOW — run authorized only within existing Manager envelope

The V3 Floor Check has completed preparation steps 1–5.

CS cannot execute Step 6 in the current Claude Code environment because the environment lacks the required model weights and inference runtime. This is an environmental boundary, not a construct or prereg failure.

## Prepared artifacts

Use the committed artifacts at:

```text
experiments/2026-06-18_v3-floor-check-run/items/
experiments/2026-06-18_v3-floor-check-run/prompts/
experiments/2026-06-18_v3-floor-check-run/manifest.json
```

The prompt set contains:

```text
96 items × 4 contexts = 384 prompt files
```

## Preconditions already passed

```text
N=96 materialization: PASS
C1–C9 admissibility: 96/96 PASS
C9 mode: real-run for every item
Prompt realization: 384 prompt files
Prompt conformance: 96/96 PASS
MAX_DELTA: every item exactly delta = 8
```

## Step 6 task

Run inference on the 384 prepared prompts under the locked V3 Floor Check run envelope.

Do not alter:

```text
items
prompts
tooling
thresholds
floors
MAX_DELTA
scoring rules
run schema
```

Do not add, remove, rewrite, or regenerate prompts.

## Required outputs

Return committed outputs under:

```text
experiments/2026-06-18_v3-floor-check-run/scored/<item>/<context>.json
experiments/2026-06-18_v3-floor-check-run/r6_log.json
experiments/2026-06-18_v3-floor-check-run/run_record.json
```

Each scored context JSON must use this schema:

```text
{
  "item": "...",
  "context": "composite | hop1 | hop2 | direct_query",
  "ground_truth": "...",
  "predicted": "...",
  "match": true | false
}
```

The R6 log must use this schema:

```text
{
  "<item>": ["invalidator_name", "..."]
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
confirmation that prompts were consumed exactly as committed
confirmation no prompt regeneration occurred
```

## After Step 6 returns

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

No compression.
No INT8.
No INT4.
No rerun.
No prompt edits.
No post-hoc slicing.
No floor adjustment.
No tooling edit after data.
No Claim C.
No Paper B.
No certification claim.
No capability claim.
No mechanism claim.

The Path A FP16 K=5 FAIL remains closed.

Team Lead
