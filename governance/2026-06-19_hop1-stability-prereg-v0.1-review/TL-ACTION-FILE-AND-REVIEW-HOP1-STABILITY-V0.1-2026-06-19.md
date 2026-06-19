# TL Action — File and Review Hop1 Stability Preregistration v0.1

**To:** CS Engineer, C5
**Cc:** Senior Engineer, Manager
**From:** Team Lead
**Subject:** File and Review Hop1 Stability Investigation Preregistration v0.1
**Status:** ACTION — filing and review only
**Route State:** YELLOW — no approval / no run authorization

Senior has drafted:

```text
PREREGISTRATION — HOP1 STABILITY INVESTIGATION (Path A) v0.1
sha256: 71f00482e1d94bd7fb06a5068391a7977a4b71d9baac690b286511d29e052c26
```

Team Lead accepts the draft for filing and review routing.

## Filing action

CS should commit the bytes verbatim to a readable in-review path, preferably:

```text
path-a/in-review/PREREGISTRATION-HOP1-STABILITY-PATH-A-v0.1.md
```

Return:

```text
PASS — Hop1 stability prereg v0.1 filed for CS/C5 review.
```

Include:

```text
- commit
- final remote HEAD
- filed path
- sha256 digest
- clean-fetch confirmation
- confirmation bytes match Senior v0.1 source
- confirmation C5 can access the object
```

## CS feasibility review

After filing, CS should review feasibility and return:

```text
PASS — executable as written
HOLD — feasible with required edits
FAIL — not executable / not lockable
```

Please focus on:

```text
1. Seed ranges:
   Confirm 193..768 are available, 3-digit, disjoint from 001..192, and mechanically realizable.

2. Scale:
   Confirm 6 blocks × 96 items × 2 contexts = 1,152 prompts is feasible.

3. Reused tooling:
   Confirm wrapper / generator / realizer / checker can be reused unchanged.

4. New tooling:
   Confirm feasibility of:
     path-a/build/v3_hop1_stability_analyzer.py
     path-a/build/v3_hop1_covariate_logger.py

5. Scoring:
   Confirm hop1 and hop2 exact-match scoring is computable from artifacts.

6. Covariates:
   Confirm all declared covariates are mechanically extractable from item specs, prompts, and scored outputs.

7. Branches:
   Confirm STABLE-ADMISSIBLE / STABLE-INADMISSIBLE / UNSTABLE / HOP2-CONTROL-FAIL / CONSTRUCT-FAIL are mechanically computable.

8. No hidden execution:
   Confirm this prereg authorizes no run, no materialization, no tooling build, no prompt generation, no model execution.
```

## C5 claim-risk review

C5 should review the actual filed bytes and return:

```text
PASS — claim boundaries safe
HOLD — claim-risk edits required
FAIL — claim framing unsafe
```

Please focus on:

```text
1. Anchors:
   Confirm 001..096 and 097..192 are treated as anchors only, not fresh evidence.

2. P-role hypothesis:
   Confirm the P-role distractor pattern is framed as a fresh-tested confirmatory hypothesis, not as a claim from seen data.

3. Exploratory covariates:
   Confirm secondary covariates are descriptive only and do not become fishing-driven claims.

4. Branch language:
   Confirm HOP1-STABLE-ADMISSIBLE / STABLE-INADMISSIBLE / UNSTABLE are bounded to materialization-level admissibility, not model capability.

5. Mechanism boundary:
   Confirm no attention/binding/reasoning/shortcut/mechanism labels are used.

6. Composite boundary:
   Confirm this is not a composite-gate rerun and does not reopen certification.

7. Downstream boundary:
   Confirm no compression, Claim C, Paper B, capability, mechanism, or certification implication leaks in.
```

## TL watchpoints

Please explicitly answer:

```text
A. Is 6 fresh blocks the right fixed size, or should TL/Manager reduce before approval?

B. Is "stability = unanimous floor verdict across fresh blocks" claim-safe and mechanically clear?

C. Is the P-role confirmatory hypothesis stated narrowly enough?

D. Is hop2-control failure handled safely, without turning the investigation into a broader component-stability study?
```

## Boundaries

No run.
No fresh materialization.
No prompt generation.
No tooling creation.
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

Team Lead
