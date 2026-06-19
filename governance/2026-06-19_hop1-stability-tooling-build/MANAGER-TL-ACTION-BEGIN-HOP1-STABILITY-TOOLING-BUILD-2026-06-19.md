# TL / Manager Action — Begin Hop1 Stability Tooling Build

**To:** CS Engineer
**Cc:** Senior Engineer, C5, Manager
**From:** Manager / Team Lead
**Subject:** Begin Hop1 Stability Tooling Build
**Status:** AUTHORIZED — tooling build only
**Route State:** YELLOW — no run authorization

CS,

C5 has passed claim-risk review on:

```text
PREREGISTRATION — HOP1 STABILITY INVESTIGATION (Path A) v0.1
sha256: 71f00482e1d94bd7fb06a5068391a7977a4b71d9baac690b286511d29e052c26
```

CS feasibility has also passed, with two implementation notes.

You are authorized to build the Hop1 Stability tooling only.

## Build scope

Build the two named tools:

```text
path-a/build/v3_hop1_stability_analyzer.py
path-a/build/v3_hop1_covariate_logger.py
```

## Required behavior

The stability analyzer must compute:

```text
- per-block hop1 correct rate
- per-block hop1 Wilson 95% CI
- per-block hop1 floor verdict against lower Wilson > 0.75
- per-block hop2 control rate and Wilson 95% CI
- HOP2-CONTROL-FAIL branch when applicable
- STABLE-ADMISSIBLE / STABLE-INADMISSIBLE / UNSTABLE branches
- per-block rate distribution
- between-block spread / variance
- final branch under prereg §9
```

The covariate logger must compute the predeclared positional/structural covariates, including:

```text
- predicted_is_P_role_distractor
- seed/index block
- target B token
- predicted token and role class
- relation token identity
- relation position
- fact-line position
- distance from query line
- prompt character count
- token-width class
- competitor / distractor role class
```

Covariate outputs are co-occurrence logs only. Do not label anything as mechanism, binding, attention, reasoning failure, or shortcut.

## Implementation notes to resolve

### N1 — Realizer context handling

CS previously noted that the realizer renders all four contexts while this prereg uses hop1 + hop2 only.

Use the smallest-touch option unless a blocker appears:

```text
N1.A — render four contexts, execute only hop1 and hop2.
```

Requirement:

```text
Unexecuted composite/direct_query contexts must not enter scoring, covariate logging, branch computation, or claims.
```

### N2 — Branch priority

Implement explicit branch priority:

```text
1. CONSTRUCT-FAIL
2. HOP2-CONTROL-FAIL
3. HOP1 stability branches:
   - HOP1-STABLE-ADMISSIBLE
   - HOP1-STABLE-INADMISSIBLE
   - HOP1-UNSTABLE
```

This priority must be documented in the analyzer output.

## Required return

Return:

```text
PASS — Hop1 Stability tooling built for SE verification.
```

Include:

```text
- paths
- commit
- final remote HEAD
- sha256 digest for each new tool
- clean-fetch confirmation
- deterministic behavior summary
- branch-coverage test results
- confirmation N1 is resolved
- confirmation N2 priority is implemented
- confirmation no model imports / no model execution
- confirmation no run, no materialization-for-execution, and no prompt execution occurred
```

## Next route

After CS returns:

```text
CS tooling build
→ SE verifies tool bytes
→ CS final feasibility re-review
→ TL approval consideration
→ Manager by-name run authorization only if approved later
```

## Boundaries

No run.
No fresh materialization for execution.
No prompt execution.
No model execution.
No composite-gate retry.
No compression.
No INT8.
No INT4.
No Claim C.
No Paper B.
No certification claim.
No capability claim.
No mechanism claim.

The Path A FP16 K=5 FAIL remains closed.

Manager / Team Lead
