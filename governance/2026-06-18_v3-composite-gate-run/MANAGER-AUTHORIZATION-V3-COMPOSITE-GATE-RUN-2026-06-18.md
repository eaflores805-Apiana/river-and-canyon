# Manager By-Name Authorization — Execute V3 Composite Gate Fresh Run

**To:** CS Engineer
**Cc:** Senior Engineer, C5, Team Lead
**From:** Manager
**Subject:** Authorization to Execute V3 Composite Gate Fresh Run
**Status:** AUTHORIZED — V3 COMPOSITE GATE RUN ONLY

I authorize CS to execute the fresh V3 Composite Gate run by name:

```text
PREREGISTRATION — V3 COMPOSITE GATE (Path A) v0.2
```

This authorization is limited to the locked V3 Composite Gate package approved by Team Lead.

## Run target

```text
fresh seed range: 097..192
N = 96
model: Qwen/Qwen2.5-3B-Instruct
precision: FP16
decoding: greedy
```

The floor-check set `001..096` is already seen and must not be reused as gate evidence.

## Authorized execution sequence

CS may now perform the following, in order:

```text
1. Generate fresh composite-gate item specs for seeds 097..192.
2. Confirm 097..192 is byte-distinct from 001..096.
3. Confirm C1–C9 admissibility, real-run mode, 96/96 PASS.
4. Realize four-context prompts for all 96 items.
5. Run prompt-conformance checks, including MAX_DELTA = 8.
6. Execute the 384 prompts exactly once under the locked model/run profile.
7. Build r6_log.json.
8. Run v3_composite_error_logger.py.
9. Run v3_composite_gate_analyzer.py.
10. Return the final §7 / §8 branch.
```

## Locked tooling

Use the approved tooling:

```text
v3_composite_gate_item_generator.py
sha256: cc07e5a2c49757e9171831af7944b5f7f8b1de235c7cb35cb18e48b06ce534a2

v3_composite_gate_analyzer.py
sha256: 3a3e954e1988ec3331d3e405bf2cbd90eae11d132d6ae9276cba10e1ca7e7c5f

v3_composite_error_logger.py
sha256: 2ed466281c949ca3a47843934c031b87e4d016b15d6d1db0ac83db6d4687c226
```

Use the approved reused artifacts unchanged:

```text
v3_item_generator.py
sha256: 6a2ceee15442ebbd1f6cc4bbbd14a76d1264af9904ad3e5d6062c1554f530c53

v3_prompt_realizer.py
sha256: fb561fdc526115da94c6137b739e8bb3b6adf30825d83f864cda713bc0750909

v3_prompt_conformance_checker.py
sha256: b8afa3f89dd7f375058500820bdf2bf58a46384d2283c8f2a31f1b8c92ad2b82

v3_neutral_token_pool.md
sha256: bc2020c2c4e1293f62c9f83a9b24a61f98c1ede35d5a071ee8cfd72a316ab0d9

inspector.py
sha256: cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9

constants.py
sha256: 1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
```

## Required result branch

Return one of the locked branches:

```text
GATE-CLEARED-THIS-RUN
COMPOSITE-DOES-NOT-CLEAR-THIS-RUN
PRECONDITION-FAIL
CONSTRUCT-FAIL
```

A successful branch may only be interpreted as:

```text
the V3 composite baseline shows behavior consistent with two-hop composition under foreclose-all controls on this run
```

It is not final certification.

## Required return

Return:

```text
CS RETURN — V3 COMPOSITE GATE RUN EXECUTED
```

Include:

```text
- commit
- final remote HEAD
- clean-fetch confirmation
- item materialization paths and hashes
- prompt paths and hashes
- admissibility summary
- prompt-conformance summary
- model/run profile
- raw/scored output paths and hashes
- r6_log.json path and hash
- error_log path and hash
- analyzer_decision.json path and hash
- composite-correct rate and Wilson 95% CI
- 0.75 reliability gate result
- 0.45 not-shortcut floor result
- hop1 / hop2 / direct-query precondition results
- invalidated item count
- final §7 / §8 branch
```

## Boundaries

This authorization does **not** authorize:

```text
compression
INT8
INT4
Claim C
Paper B
final certification claim
general capability claim
mechanism claim
seam evidence claim
rerun
post-hoc slicing
prompt edits after generation
floor adjustment
tooling edit after data
```

The Path A FP16 K=5 FAIL remains closed.

Manager authorizes this run by name.

— Manager
