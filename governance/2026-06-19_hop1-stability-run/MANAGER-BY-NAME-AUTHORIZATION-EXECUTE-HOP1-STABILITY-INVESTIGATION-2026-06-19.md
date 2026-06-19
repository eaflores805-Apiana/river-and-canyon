# Manager By-Name Authorization — Execute Hop1 Stability Investigation

**To:** CS Engineer
**Cc:** Senior Engineer, C5, Team Lead
**From:** Manager
**Subject:** Authorization to Execute Hop1 Stability Investigation
**Status:** AUTHORIZED — HOP1 STABILITY RUN ONLY

I authorize CS to execute the Hop1 Stability Investigation by name:

```text
PREREGISTRATION — HOP1 STABILITY INVESTIGATION (Path A) v0.1
```

This authorization is limited to the approved Hop1 Stability package.

## Run target

```text
Fresh seed blocks:
  F1: 193..288
  F2: 289..384
  F3: 385..480
  F4: 481..576
  F5: 577..672
  F6: 673..768

N = 96 per block
Total fresh items = 576
Contexts executed: hop1 + hop2-control only
Model: Qwen/Qwen2.5-3B-Instruct
Precision: FP16
Decoding: greedy
```

The prior sets `001..096` and `097..192` are anchors only. They must not enter the fresh stability branch decision.

## Locked tooling

Use the approved tools:

```text
v3_hop1_stability_analyzer.py
sha256: 31224f6fe7b66d303924a40fa9307f3aded05f8ba73d4952f518c8deecd69f0f

v3_hop1_covariate_logger.py
sha256: b9532490f49970396cd9a14d926393450ede2e6a17c5374b2ac69d115f39953f
```

Use reused tooling unchanged as previously locked.

## Execution requirements

CS may now:

```text
1. Materialize fresh V3 items for seeds 193..768.
2. Confirm all indices are 3-digit and MAX_DELTA=8 remains valid.
3. Realize prompts as needed, but execute only hop1 and hop2-control.
4. Run C1–C9 admissibility and prompt-conformance checks.
5. Execute hop1 and hop2 prompts exactly once.
6. Run the covariate logger.
7. Run the Hop1 Stability analyzer.
8. Return the final branch.
```

Branch priority:

```text
1. CONSTRUCT-FAIL
2. HOP2-CONTROL-FAIL
3. HOP1-STABLE-ADMISSIBLE / HOP1-STABLE-INADMISSIBLE / HOP1-UNSTABLE
```

## Required return

Return:

```text
CS RETURN — HOP1 STABILITY INVESTIGATION EXECUTED
```

Include:

```text
- commit
- final remote HEAD
- clean-fetch confirmation
- item/spec paths and hashes
- prompt paths and hashes
- scored output paths and hashes
- run_record.json path and hash
- covariate log path and hash
- analyzer decision path and hash
- per-block hop1 rates and Wilson CIs
- per-block hop2-control rates and Wilson CIs
- per-block floor verdicts
- final branch
- P-role co-occurrence result
- exploratory covariate summary
```

## Interpretation boundary

This run may report only:

```text
cross-block hop1 materialization-admissibility
```

It must not report:

```text
model stability
general hop1 capability
mechanism
binding failure
attention failure
reasoning failure
shortcut claim
composite-gate result
certification
compression readiness
Claim C
Paper B
```

## Boundaries

No composite-gate retry.
No compression.
No INT8.
No INT4.
No Claim C.
No Paper B.
No certification claim.
No capability claim.
No mechanism claim.
No rerun until a preferred branch appears.
No post-hoc covariate fishing.
No prompt edits after execution.
No tooling edits after data.

The Path A FP16 K=5 FAIL remains closed.

Manager authorizes this run by name.

— Manager
