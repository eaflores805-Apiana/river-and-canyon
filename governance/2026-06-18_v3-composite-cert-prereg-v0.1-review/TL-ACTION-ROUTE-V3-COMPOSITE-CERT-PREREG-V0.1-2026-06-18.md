# TL Action — Route V3 Composite-Certification Prereg v0.1 for Review

**To:** CS Engineer, C5
**Cc:** Senior Engineer, Manager
**From:** Team Lead
**Subject:** Review V3 Composite-Certification Preregistration v0.1
**Status:** ACTION — review only
**Route State:** YELLOW — no approval / no run authorization

Senior has drafted:

```text
PREREGISTRATION — V3 COMPOSITE CERTIFICATION (Path A) v0.1
```

Team Lead accepts the draft for routing, not approval.

## Review object

Review the draft as a fresh-run preregistration for the next empirical question:

```text
Does the full V3 two-hop composite clear a predeclared certification gate on a fresh N=96 materialization?
```

The draft correctly states that the already-seen floor-check composite result is informational only and cannot be used as certification data.

## CS feasibility review

Please return:

```text
PASS — executable as written
HOLD — feasible with required edits
FAIL — not executable / not lockable
```

Focus on:

```text
1. Fresh-run materialization:
   Confirm how new seeds / fresh items will be generated and kept distinct from the floor-check set.

2. Reused tooling:
   Confirm the existing realizer, checker, neutral-token pool, inspector, constants, and generator can be reused unchanged.

3. New tooling:
   Confirm feasibility of:
     - path-a/build/v3_composite_certification_analyzer.py
     - path-a/build/v3_composite_error_logger.py

4. Analyzer lockability:
   Identify required inputs, outputs, digest locks, and exact branch computation.

5. Error-structure logging:
   Confirm whether "correct chain, wrong depth," "decoy chain depth-2," and "competitor / other token" are mechanically computable from scored outputs and ground truth.

6. Fresh preconditions:
   Confirm hop1, hop2, direct-query, C1–C9, prompt conformance, invalidators, and dominance checks can be recomputed on the fresh set.

7. No hidden execution:
   Confirm this draft authorizes no tooling build, no materialization, no prompts, no model run, and no compression.
```

## C5 claim-risk review

Please return:

```text
PASS — claim boundaries safe
HOLD — claim-risk edits required
FAIL — claim framing unsafe
```

Focus on:

```text
1. Certification wording:
   Review whether "certifies composition on V3" is too strong.
   Consider whether the safer claim should be:
     "certifies the V3 composite baseline as behavior consistent with two-hop composition under foreclose-all controls."

2. "Via the correct chain" wording:
   Confirm whether this is operationally safe, or whether it should be rewritten as:
     "returns the correct-chain target C* under controls."
   The model's internal path is not observed.

3. Fresh-run requirement:
   Confirm that the already-seen composite 80/96 is correctly barred from certification use.

4. Threshold:
   Review the proposed lower Wilson > 0.75 composite gate and the necessary >0.45 not-shortcut floor.

5. Replication boundary:
   Review the distinction between:
     - GATE-CLEARED-THIS-RUN
     - FINAL certification requiring Manager/standard decision and possible confirmation

6. Forbidden interpretations:
   Confirm no capability, mechanism, compression, Claim C, or Paper B leakage.
```

## Specific TL watchpoints

Please explicitly answer:

```text
A. Should this artifact be titled "composite certification," or should it use a safer title like
   "V3 Composite Gate Preregistration" until final certification standard is decided?

B. Is the phrase "certifies composition on V3" acceptable if bounded, or should it be replaced?

C. Is the fresh-run seed/materialization rule precise enough, or does the prereg need exact seed ranges before approval?

D. Is one fresh run enough for "gate-cleared-this-run," while final certification remains separate?
```

## Boundaries

No new run.
No rerun.
No fresh materialization.
No prompt generation for execution.
No tooling creation.
No compression.
No INT8.
No INT4.
No Claim C.
No Paper B.
No certification claim yet.
No capability claim.
No mechanism claim.

The Path A FP16 K=5 FAIL remains closed.

Team Lead
