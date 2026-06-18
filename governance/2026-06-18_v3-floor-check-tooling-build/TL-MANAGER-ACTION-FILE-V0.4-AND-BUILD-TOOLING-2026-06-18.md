# TL / Manager Action — File V3 Floor-Check Prereg v0.4 and Begin Tooling Build

**To:** CS Engineer
**Cc:** Senior Engineer, C5, Manager
**From:** Manager / Team Lead
**Subject:** File V3 Floor-Check Preregistration v0.4 and Build Floor-Check Tooling
**Status:** ACTION — filing + tooling build only
**Route State:** YELLOW — no run authorization

CS,

Senior returned:

```text
PREREGISTRATION — V3 FLOOR CHECK (Path A) v0.4
```

Team Lead accepts v0.4 for filing and authorizes the next non-run tooling-build step.

## Step 1 — File v0.4

Commit the v0.4 bytes verbatim to:

```text
path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.4.md
```

Do not edit scientific content while filing.

Return:

```text
PASS — v0.4 filed
```

with:

```text
- commit
- final remote HEAD
- filed path
- sha256 digest
- clean-fetch confirmation
- confirmation bytes match Senior v0.4 source
```

## Step 2 — Build floor-check tooling

After filing v0.4, CS is authorized to build the named tooling artifacts only:

```text
path-a/build/v3_floor_check_analyzer.py
path-a/build/v3_prompt_realizer.py
path-a/build/v3_prompt_conformance_checker.py
path-a/build/v3_neutral_token_pool.md
```

The tooling must match the contracts in v0.4:

```text
- analyzer computes hop1/hop2 rates, Wilson CIs, direct-query count, invalidated count, exclusions, post-exclusion denominators, and final branch
- prompt realizer renders four concrete prompts per item under the same-template-class + ≤8 character delta rule
- prompt conformance checker verifies no leakage, preserved foreclose-all properties, and ≤8 character delta
- neutral-token pool is either a separate fixed file or explicitly embedded in the realizer and bound by the realizer digest
```

## Required tooling return

Return:

```text
PASS — floor-check tooling built for SE verification
```

Include:

```text
- paths
- commit
- final remote HEAD
- sha256 digest for each tooling artifact
- clean-fetch confirmation
- summary of deterministic behavior
- confirmation no model imports, no model execution, no prompt execution, no N=96 materialization
- confirmation MAX_DELTA = 8 is implemented as character-count gate
- any feasibility blocker, especially if ≤8 characters is not achievable with the realizer
```

## Next route after tooling return

```text
CS tooling build
→ SE verifies tool bytes
→ CS feasibility re-review
→ TL approval consideration
→ Manager by-name run authorization only if approved later
```

## Boundaries

This action does not authorize:

```text
N=96 materialization
prompt generation for execution
model run
floor-check run
compression
Claim C
Paper B
certification claim
capability claim
mechanism claim
```

The Path A FP16 K=5 FAIL remains closed.

Manager / Team Lead
