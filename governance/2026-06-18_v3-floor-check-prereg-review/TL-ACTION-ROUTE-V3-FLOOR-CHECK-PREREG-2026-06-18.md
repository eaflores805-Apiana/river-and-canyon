# TL Action — Route V3 Floor-Check Prereg for CS Feasibility and C5 Claim-Risk

**To:** CS Engineer, C5
**Cc:** Senior Engineer
**From:** Team Lead
**Subject:** Review V3 Floor-Check Preregistration v0.1
**Status:** ACTION — review only
**Route State:** YELLOW — no run authorization

CS, C5,

Senior has drafted:

```text
PREREGISTRATION — V3 FLOOR CHECK (Path A) v0.1
```

Team Lead accepts the draft for routing, not approval.

The prereg correctly frames the next empirical question:

```text
Does hop2 clear its reliability floor under V3 same-depth-competitor competition?
```

This is not a composite certification run. It is not a model run authorization.

## CS feasibility review

Please check whether the prereg is executable as written.

Focus on:

```text
- full N=96 materialization feasibility
- four-context prompt realization feasibility
- prompt-level conformance checks
- length/format matching across composite / hop1 / hop2 / direct_query
- real-run assertions
- artifact paths and hashes required before any run
- whether scorer / analysis code is explicitly named and lockable
```

Also confirm whether the decision rules can be computed exactly once from the artifacts.

## C5 claim-risk review

Please review claim safety and interpretation boundaries.

Focus on:

```text
- whether "substrate-infeasibility" is safe as written
- whether "clean construct" is overclaimed if prompt realization later introduces new risks
- whether hop2-below-floor is correctly separated from construct-fail
- whether hop2-clears-floor is safely bounded as component-admissible, not certification
- whether any wording implies mechanism, composition, or capability
```

## Specific watchpoints

Please explicitly answer these three:

```text
1. Wilson threshold:
   The prereg uses lower Wilson bound > 0.75 for hop2 floor.
   At N=96 this requires a high point score. Confirm that this strictness is intentional.

2. Direct-query ceiling:
   The prereg says direct_query retrieval of C* must be at/below 0.20.
   Convert this into an exact N=96 count rule or state the intended interval rule.

3. R6 invalidator scope:
   The prereg says any R6 invalidator invalidates the construct for that item,
   and also requires no R6 invalidator at set level.
   Clarify whether one item-level invalidator fails the whole construct or whether
   a predeclared item-level handling rule is needed.
```

## Required returns

CS returns:

```text
PASS — executable as written
HOLD — feasible with required edits
FAIL — not executable as written
```

C5 returns:

```text
PASS — claim boundaries safe
HOLD — claim-risk edits required
FAIL — claim framing unsafe
```

## Boundaries

No build changes.
No full N=96 materialization.
No prompt generation for model execution.
No model run.
No compression.
No Claim C.
No Paper B.
No certification claim.
No capability claim.
No mechanism claim.

The Path A FP16 K=5 FAIL remains closed.

Team Lead
