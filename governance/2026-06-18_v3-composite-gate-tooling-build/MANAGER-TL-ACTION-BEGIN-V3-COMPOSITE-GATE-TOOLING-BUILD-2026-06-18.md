# TL / Manager Action — Begin V3 Composite Gate Tooling Build

**To:** CS Engineer
**Cc:** Senior Engineer, C5, Manager
**From:** Manager / Team Lead
**Subject:** Begin V3 Composite Gate Tooling Build
**Status:** AUTHORIZED — tooling build only
**Route State:** YELLOW — no run authorization

C5 claim-risk has passed on:

```text
PREREGISTRATION — V3 COMPOSITE GATE (Path A) v0.2
sha256: df26dc65ac3dd76bb09fa84c4688b8835f49282e2a8f77ea4b94991308e57275
```

CS feasibility has passed with one carried implementation dependency: the fresh seed range `097..192` must be mechanically realizable and byte-distinct from the floor-check range `001..096`.

CS is authorized to begin tooling build only.

## Build scope

Build the following artifacts:

```text
path-a/build/v3_composite_gate_analyzer.py
path-a/build/v3_composite_error_logger.py
```

Also resolve fresh materialization support for:

```text
composite-gate seeds: 097..192
floor-check seeds:    001..096
```

Preferred implementation:

```text
path-a/build/v3_composite_gate_item_generator.py
```

as a wrapper that preserves the existing `v3_item_generator.py` bytes unchanged while producing the fresh `097..192` materialization.

If CS determines the wrapper is not cleanly implementable and instead needs to patch `v3_item_generator.py`, return HOLD before making that change. Patching the generator would change a previously reused digest and may require a prereg binding update.

## Required tooling behavior

The composite gate analyzer must:

```text
- compute composite-correct rate
- compute Wilson 95% CI
- apply lower-Wilson > 0.75 reliability gate
- apply lower-Wilson > 0.45 not-shortcut floor
- confirm fresh preconditions: hop1, hop2, direct-query, admissibility, prompt conformance
- apply invalidator rules
- emit the final branch:
  GATE-CLEARED-THIS-RUN /
  COMPOSITE-DOES-NOT-CLEAR /
  PRECONDITION-FAIL /
  CONSTRUCT-FAIL
```

The error logger must:

```text
- classify composite errors by landed token class
- distinguish correct-chain wrong depth, decoy-chain depth-2, competitor, other
- record inherited component failure versus composition-specific failure
- make no mechanism claim
```

The fresh-item wrapper must:

```text
- generate or materialize items 097..192
- prove no overlap with 001..096
- preserve the 3-digit token-width scheme
- preserve MAX_DELTA = 8 eligibility
- produce byte-distinct specs/prompts relative to the floor-check set
```

## Required return

Return:

```text
PASS — V3 Composite Gate tooling built for SE verification
```

Include:

```text
- paths
- commit
- final remote HEAD
- sha256 digest for each new artifact
- clean-fetch confirmation
- confirmation whether wrapper or generator patch was used
- confirmation 097..192 is mechanically realizable
- confirmation 097..192 is disjoint from 001..096
- confirmation token-width remains 3-digit and MAX_DELTA = 8 remains valid
- deterministic behavior summary
- no model imports / no model execution confirmation
```

## Next route

After CS returns:

```text
CS tooling build
→ SE verifies tool bytes
→ CS feasibility re-review against locked tooling
→ TL approval consideration
→ Manager by-name run authorization only if approved later
```

## Boundaries

No fresh N=96 run materialization for execution.
No prompt generation for execution.
No model run.
No compression.
No INT8.
No INT4.
No Claim C.
No Paper B.
No certification claim yet.
No capability claim.
No mechanism claim.

The Path A FP16 K=5 FAIL remains closed.

Manager / Team Lead
