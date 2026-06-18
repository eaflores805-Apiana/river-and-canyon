# TL Action — File and Review V3 Composite Gate Prereg v0.2

**To:** CS Engineer, C5
**Cc:** Senior Engineer, Manager
**From:** Team Lead
**Subject:** File and Review V3 Composite Gate Preregistration v0.2
**Status:** ACTION — filing and review only
**Route State:** YELLOW — no approval / no run authorization

Senior returned:

```text
PREREGISTRATION — V3 COMPOSITE GATE (Path A) v0.2
```

Team Lead accepts v0.2 for filing and review routing.

## What v0.2 fixes

This draft addresses the prior C5 and CS concerns:

```text
- Retitles the artifact from "Composite Certification" to "Composite Gate"
- Replaces "certifies composition" with bounded validity language
- Replaces "via the correct chain" with "returns the correct-chain target C* under controls"
- Bars the already-seen floor-check composite 80/96 from gate use
- Declares a fresh disjoint seed range:
    floor-check: 001..096
    composite-gate: 097..192
- Preserves MAX_DELTA = 8 by keeping indices <= 999
- Separates GATE-CLEARED-THIS-RUN from FINAL certification
- Strengthens forbidden interpretations:
    no capability, no mechanism, no seam evidence, no compression readiness, no Claim C, no Paper B
```

## CS action — file v0.2

Please commit the v0.2 bytes verbatim to a readable in-review path:

```text
path-a/in-review/PREREGISTRATION-V3-COMPOSITE-GATE-v0.2.md
```

Return:

```text
PASS — v0.2 filed for CS/C5 review
```

with:

```text
- commit
- final remote HEAD
- filed path
- sha256 digest
- clean-fetch confirmation
- confirmation bytes match Senior v0.2 source
- confirmation C5 can access the object
```

## CS feasibility review focus

After filing, review feasibility and return:

```text
PASS — executable as written
HOLD — feasible with required edits
FAIL — not executable / not lockable
```

Focus especially on:

```text
1. Fresh materialization:
   Can the current generator actually produce seeds/items 097..192?

2. Generator support:
   Prior CS review said v3_item_generator.py lacked --start-index.
   Confirm whether start-index support now exists or must be added.

3. Disjointness:
   Confirm 097..192 is mechanically disjoint from 001..096 and produces byte-distinct items/prompts.

4. MAX_DELTA:
   Confirm indices 097..192 preserve the 3-digit token-width scheme and therefore do not reopen the MAX_DELTA=8 caveat.

5. New tools:
   Confirm feasibility of:
     path-a/build/v3_composite_gate_analyzer.py
     path-a/build/v3_composite_error_logger.py

6. Reused tools:
   Confirm realizer/checker/pool/inspector/constants can be reused unchanged after fresh materialization support is resolved.

7. No hidden execution:
   Confirm this draft authorizes no run, no materialization, no prompt generation, and no tooling build by itself.
```

## C5 claim-risk review focus

C5 should review the actual filed bytes and return:

```text
PASS — claim boundaries safe
HOLD — claim-risk edits required
FAIL — claim framing unsafe
```

Focus on whether v0.2 resolves the standing rulings:

```text
- title uses Composite Gate, not Composite Certification
- success language is behavior-consistent, not "the model composes"
- correct-chain target C* wording avoids internal-path claims
- seen floor-check composite is barred from gate use
- fresh seeds are exact and disjoint
- 0.75 reliability gate and 0.45 not-shortcut floor are distinct
- GATE-CLEARED-THIS-RUN does not become FINAL certification
- forbidden interpretations block seam/compression/capability/mechanism leakage
```

## Boundaries

No new run.
No fresh materialization.
No prompt generation.
No tooling creation.
No model execution.
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
