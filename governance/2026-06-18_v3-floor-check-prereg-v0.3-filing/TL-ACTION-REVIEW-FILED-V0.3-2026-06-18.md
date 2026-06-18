# TL Action — Review Filed V3 Floor-Check Preregistration v0.3

**To:** CS Engineer, C5
**Cc:** Senior Engineer, Manager
**From:** Team Lead
**Subject:** Review Filed V3 Floor-Check Preregistration v0.3
**Status:** ACTION — review only
**Route State:** YELLOW — no approval / no run authorization

CS, C5,

The V3 Floor-Check Preregistration v0.3 has been filed at a contributor-readable path:

```text
path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.3.md
sha256: df82b34c4f96e085ea51b8e6e1a735849a39b108b321f79e30b9f20cffa19d5b
```

CS confirmed clean-fetch match and byte-identical filing from Senior's v0.3 draft.

Proceed with substantive review.

## CS task — feasibility re-review

Return one of:

```text
PASS — executable as written
HOLD — feasible with required edits
FAIL — not executable as written
```

Please specifically address:

```text
1. Analyzer lockability:
   v0.3 names path-a/build/v3_floor_check_analyzer.py.
   Confirm whether this path exists and whether the analyzer can be locked before approval.
   If missing, return HOLD and specify required analyzer artifact.

2. Prompt length matching:
   v0.3 still uses "predeclared MAX DELTA."
   Confirm whether this is executable as written.
   If not, propose the exact numeric tolerance required for lockability.

3. Analyzer digest:
   Confirm what artifact and digest must be locked before approval.

4. Exact decision-rule computability:
   Confirm whether §9/§10 can be computed exactly once from declared artifacts after analyzer bytes exist.

5. No hidden execution:
   Confirm that review, filing, and prereg language authorize no model run, no N=96 materialization, and no prompt generation for execution.
```

## C5 task — claim-risk review

C5's prior HOLD was access-based. The object is now filed and readable.

Return one of:

```text
PASS — claim boundaries safe
HOLD — claim-risk edits required
FAIL — claim framing unsafe
```

Please review the actual filed bytes and confirm whether v0.3 resolves the prior claim-risk rulings:

```text
- R6 item-level / set-level split
- direct-query exact count boundary
- hop2 Wilson strictness bounded as component-admissibility only
- one-run substrate-infeasibility language bounded as evidence-toward, not final classification
- clean construct contingent on prompt-realization conformance
- no certification / capability / mechanism / composition overclaim
```

## Boundaries

No build changes.
No analyzer creation yet unless separately authorized.
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
