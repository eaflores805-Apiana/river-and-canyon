# Manager Direction — Strategic Position Before Next Drafting

**Received:** 2026-06-13 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — model-free synthesis requested from Senior + TL; CS is CC. No model execution.

---

To: Senior Engineer, Team Lead
Cc: CS Engineer
From: Manager
Re: Strategic position after D4 pivot and CAL-Q finding
Status: Model-free synthesis requested; no execution authorized

Team,

D4 is now closed as the current certification-readiness route.

CAL-Q is preserved as a finding track, not a rescue track.

Before we draft more methodology sections or open any new experimental design, I want one strategic position memo.

Please draft:

```text
POST-D4-STRATEGIC-POSITION-v0.1.md
```

## Question to answer

```text
Is the near-term program now best framed as Tier 1 eval-validity instrumentation,
with seam work deferred until a valid baseline family exists?
```

## Required framing

Compare two possible north stars:

```text
A. Instrument-as-deliverable:
   The near-term product is the evaluation-validity instrument:
   fail-closed baseline gates, scorer/artifact audits, construct-validity checks,
   rejection audit, and task-family certification discipline.

B. Seam-as-deliverable:
   The near-term product remains the compression/seam experiment:
   find a valid baseline family, certify it, then run compression stress.
```

## Required assessment per option

1. What evidence supports it
2. What evidence weakens it
3. What work it makes urgent
4. What work it defers
5. What claim it can support now
6. What claim it cannot yet support

## Evidence to consider (the current record)

- D4 closed as PIVOT / valuable negative result.
- CAL-Q preserved as format-sensitive abstention finding.
- Direct-query D4 preserved abstention but stayed saturated.
- Code-book CAL-Q pulled clean off ceiling but collapsed defective abstention.
- Seam question remains unanswered.
- No certified compression rung has run.
- Tier 1 eval-validity findings are now independently supported:
  - survival is not correctness;
  - correctness is not constructibility;
  - hash integrity is not construct validity;
  - scorer/parser artifact caught;
  - lever-validity failure identified;
  - D4 route killed under pre-declared rule.

## Required recommendation

```text
Recommended near-term north star:
  Instrument-as-deliverable
  or
  Seam-as-deliverable
  or
  Hybrid: instrument first, seam deferred
```

Manager's current prior:

```text
Hybrid: instrument first, seam deferred.
```

Meaning: the seam remains an open research question, but the near-term program should prioritize the validity instrument, because that is what the evidence has already earned.

## Required next-step ordering

Recommend an ordering among:

1. Literature check
2. §11 rejection-audit control
3. Tier 1 methodology consolidation
4. Alternative task-family search
5. Future diagnostics for CAL-Q format-sensitive abstention

## Boundaries

This is model-free strategy work.

Closed:
- No new run.
- No D4 rescue.
- No CAL-Q rerun.
- No certification.
- No compression.
- No INT8 / INT4 stress.
- No second compression rung.
- No full ladder.
- No Claim C activation.
- No public benchmark packaging.
- No funder-facing release.
- No SBIR submission.

## Intent

The goal is to prevent drift after the D4 pivot.

We are not abandoning the seam question.

We are deciding whether the program's near-term center of gravity should now be the evaluation-validity instrument that the work has already produced.

— Manager
