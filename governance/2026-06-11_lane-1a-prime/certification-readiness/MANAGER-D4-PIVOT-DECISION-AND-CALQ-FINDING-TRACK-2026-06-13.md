# Manager Decision — D4 Pivot Approved; CAL-Q Finding Track Opened

**Received:** 2026-06-13 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — D4 route closed (PIVOT); CAL-Q finding track opened; no model execution authorized

---

To: Senior Engineer, CS Engineer, Team Lead
From: Manager
Re: D4 route disposition and CAL-Q mechanism finding
Status: Approved

Team,

Decision approved.

## Route decision

D4 is closed as the current certification-readiness baseline route.

Disposition:

```text
D4: PIVOT
Classification: valuable negative result
Reason: under the tested levers, D4 cannot currently host a clean off-ceiling baseline with preserved defective discrimination.
```

This closes the D4 rescue loop. No further D4 repair attempts are authorized under the current route.

## Finding preserved

We are not discarding the CAL-Q result.

CAL-Q produced a more interesting finding than a simple pass/fail:

```text
Direct-query D4 preserved defective abstention but stayed saturated.
The code-book query pulled clean off ceiling but collapsed defective abstention to zero.
```

This suggests that abstention behavior in this construct is format-sensitive and may be coupled to retrieval difficulty.

This is now a finding track, not a rescue track.

## New artifact requested

Senior to draft:

```text
CAL-Q-FORMAT-SENSITIVE-ABSTENTION-FINDING-v0.1.md
```

Purpose: preserve the CAL-Q mechanism finding, define the allowed claim, define the forbidden claims, and identify what future diagnostics would be required before generalizing.

## Required sections

1. Executive summary
2. Evidence base
3. What CAL-Q showed
4. Why D4 closes as a certification route
5. Mechanism hypothesis: format-sensitive abstention / difficulty-abstention coupling
6. Allowed claims
7. Forbidden claims
8. Implications for future task-family design
9. Minimal future diagnostics
10. Relation to Tier 1 eval-validity auditing
11. Closed gates

## Safe claim wording (per Manager)

> In the D4 key-value family, direct-query defective abstention was robust across content-lever variants, but did not transfer to the code-book query format. The first query-side lever that produced meaningful clean difficulty also collapsed defective abstention to zero. This suggests abstention behavior in this construct is format-sensitive and may be coupled to retrieval difficulty.

## Forbidden claims

- Models cannot abstain.
- All absence-defined tasks fail.
- No task family can host a clean baseline.
- The seam is false.
- Compression fragility has been tested.
- D4 can never work under a fundamentally different structure.

## Closed gates

- No new D4 run.
- No CAL-Q rerun.
- No certification run.
- No compression.
- No INT8 / INT4 stress.
- No second compression rung.
- No full ladder.
- No candidate certification.
- No ranking.
- No Claim C activation.
- No public benchmark packaging.
- No funder-facing release.
- No SBIR submission.

## Intent

The route pivots.

The finding stays.

D4 failed as the ruler, but CAL-Q may have revealed something important about the material: abstention may not be portable across prompt formats when retrieval difficulty rises.

That is worth preserving carefully.

— Manager
