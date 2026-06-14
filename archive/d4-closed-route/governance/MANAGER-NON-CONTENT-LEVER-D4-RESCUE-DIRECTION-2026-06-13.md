# Manager Direction — One Final Non-Content-Lever Attempt Before D4 Pivot

**Received:** 2026-06-13 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — model-free specification authorized; **no execution authorized**

---

To: Senior Engineer, CS Engineer
Cc: Team Lead
From: Manager
Re: CAL-E interpretation and next bounded repair path
Status: Model-free specification authorized; no execution authorized

Team,

I have reviewed the CAL-E interpretation.

CAL-E missed all three targets:

```text
clean target:        0.88-0.92
clean actual:        0.975

defective target:    ≤0.10
defective actual:    0.575

separation target:   ≳0.78
separation actual:   0.400
```

The important finding is not just that CAL-E failed. It failed in the exact way the design was supposed to prevent.

Senior's design hypothesis was that length and depth would lower clean accuracy without inflating defective accuracy. The run falsified that hypothesis. At constant near-miss, increasing length and depth inflated defective accuracy sharply.

That puts the D4 route in:

```text
PIVOT WATCH
```

not ordinary "one more tweak."

## Manager decision

I am authorizing **one final bounded model-free repair attempt**, and only because it changes lever class.

This next attempt must **not** be another length/depth/near-miss content-lever escalation.

The only authorized direction is:

```text
non-content difficulty
```

Meaning: make the clean query harder without adding more decoy content that gives the defective item false answer material.

Examples may include:

```text
indirect-key query form
query wording transformation
query-side constraint
format-side lookup requirement
```

But the core requirement is:

```text
Increase clean difficulty without increasing defective answerability.
```

## Required artifact

Senior is authorized to draft:

```text
NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1.md
```

## Required purpose

The artifact must answer:

```text
Can a non-content lever move clean accuracy into the band while preserving clean/defective separation?
```

Target band remains: `0.6625 < clean accuracy < 0.95`
Separation requirement remains: defective accuracy ≤ ~0.10; clean − defective separation ≳ 0.78

## Required design constraint

The spec must explicitly avoid the failure mode CAL-E revealed:

```text
Do not add more content load that gives the defective/key-absent item more false answer material.
```

If the proposed lever makes defective items more answerable, reject it at the design stage.

## Required contents (13 sections)

1. Executive summary
2. CAL-E falsification summary
3. Why content levers are now blocked
4. Proposed non-content lever
5. How the lever pressures clean accuracy
6. Why it should not inflate defective accuracy
7. Clean target
8. Defective target
9. Single-difference preservation
10. Semantic-read requirements
11. Pre-declared decision rule
12. Checklist
13. Closed gates

## Required decision rule (pre-declared, before any run)

```text
BAND PLAUSIBLE:
  clean lands strictly inside 0.6625 < clean < 0.95
  and defective remains low enough to preserve separation.

NEEDS REPAIR:
  clean remains at/above 0.95,
  clean drops too close to the shortcut floor,
  or defective rises enough to erode separation.

PIVOT:
  the non-content lever also inflates defective or fails to create a clean in-band point.
```

This is the final D4 rescue attempt unless the result cleanly identifies a new, specific, non-handwavy repair.

## CS instructions

CS should **not run anything yet**.

CS supports this stage by verifying:

- paths
- commit
- sha256
- source artifacts
- INDEX row
- CAL-E run record
- CAL-E interpretation
- that the proposed spec remains model-free
- that no run authorization language slipped in

Once spec is drafted, CS also checks:

- single-difference feasibility
- whether the proposed lever changes only query-side difficulty
- whether content load / decoy material is unchanged
- whether defective answerability is not increased by construction

## Boundary

This authorizes no model execution.

Closed:

- No model execution
- No certification run
- No compression
- No INT8 / INT4 stress
- No second compression rung
- No full ladder
- No candidate certification
- No ranking
- No Claim C activation
- No public benchmark packaging
- No funder-facing release
- No SBIR submission

## Intent

This is not an invitation to keep searching indefinitely.

This is one final bounded test of a different lever class.

If a non-content lever can create an in-band clean point while keeping defective low, the D4 route may still be viable.

If it cannot, the honest next move is to stop pursuing D4 certification-readiness and pivot toward Tier 1 eval-validity auditing.

— Manager
