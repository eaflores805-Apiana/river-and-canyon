# TL Action — File V3 Floor-Check Prereg v0.3 for CS/C5 Re-Review

**To:** CS Engineer
**Cc:** Senior Engineer, C5, Manager
**From:** Team Lead
**Subject:** File V3 Floor-Check Preregistration v0.3 for Review
**Status:** ACTION — filing and review only
**Route State:** YELLOW — no approval / no run authorization

CS,

Senior returned:

```text
PREREGISTRATION — V3 FLOOR CHECK (Path A) v0.3
```

Team Lead accepts v0.3 for filing and review routing.

This version addresses the prior CS feasibility HOLD items E1–E5 in substance:

```text
E1 — named analyzer path: path-a/build/v3_floor_check_analyzer.py
E2 — direct-query ceiling fixed as exact point-count: ≤19/96 pass, ≥20/96 fail
E3 — R6 split clarified: item-level exclude/log; set-level ≥10/96 construct-fail
E4 — hop1 lower-Wilson rule made parallel to hop2
E5 — prompt length matching set to character count + same template class
```

## Required action

Commit the v0.3 bytes verbatim to a C5-readable in-review path:

```text
path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.3.md
```

Do not edit scientific content while filing.

## Review routing

After filing, route the committed artifact to:

```text
CS — feasibility re-review
C5 — claim-risk review against actual bytes
```

## TL watchpoints for review

CS should specifically confirm:

```text
1. Analyzer lockability:
   The analyzer path is named, but the analyzer itself must exist and have a lockable sha before approval.

2. Prompt length matching:
   v0.3 still uses "predeclared MAX DELTA."
   This must become an exact numeric tolerance before TL approval.

3. Analyzer digest:
   The analyzer digest is not yet locked; it must be fixed before any run authorization.

4. No hidden run:
   The prereg must remain draft/review only.
```

## Required CS return

Return:

```text
PASS — v0.3 filed for CS/C5 review
```

Include:

```text
- commit
- final remote HEAD
- filed path
- sha256 digest
- clean-fetch confirmation
- confirmation bytes match Senior v0.3 source
- confirmation C5 can access the object
```

## Boundaries

No build changes.
No N=96 materialization.
No prompt generation for execution.
No model run.
No floor-check run.
No compression.
No Claim C.
No Paper B.
No certification claim.
No capability claim.
No mechanism claim.

The Path A FP16 K=5 FAIL remains closed.

Team Lead
