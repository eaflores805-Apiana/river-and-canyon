# Manager Direction — CS Verification of Tier 1 Instrument Repo Structure

**Received:** 2026-06-14 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — structure accepted for CS verification; no file moves, software build, or execution authorized yet.

---

To: CS Engineer
Cc: Senior Engineer, Team Lead
From: Manager
Re: Verification of `TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.1.md`
Status: Structure accepted for CS verification; no file moves, software build, or execution authorized yet

CS,

I accept the proposed Tier 1 instrument repo structure in principle.

Please verify:

```text
TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.1.md
```

## Purpose

The goal is to organize the program so the completed Paper A, the active Tier 1 instrument specs, the CAL-Q finding track, future Paper B planning, and closed D4 history remain cleanly separated.

The organizing principle is:

```text
one track, one directory tree, no cross-contamination
```

## Required checks

Please verify:

```text
1. Paper A release artifacts have a clear home under /papers/paper-a-before-retention/.
2. Tier 1 instrument artifacts have a clear home under /tier-1-instrument/.
3. Tool Spec v0.1 and G6 Spec v0.1 route under /tier-1-instrument/specs/.
4. Future schemas, modules, human-read templates, examples, and implementation stubs are clearly marked as placeholders where appropriate.
5. /implementation/ is reserved only and does not imply a software build.
6. CAL-Q finding-track artifacts route under /finding-tracks/cal-q-format-sensitive-abstention/.
7. CAL-Q is not filed as a D4 rescue.
8. Paper B planning is separate under /paper-b/planning/.
9. D4 materials route only to historical archive.
10. D4 remains closed and is not reopened by this structure.
11. No artifact is double-homed.
12. No existing artifact is dropped.
13. Paper A, Tool Spec, and G6 Spec remain sources of truth for their respective tracks.
14. Schema files are described as future lifts from specs, not as existing artifacts.
15. The structure implies no model execution, no software build, no benchmark packaging, and no public/funder release.
```

## File-move boundary

This direction does **not** authorize file moves yet.

Please return a verification disposition first.

Actual git moves, if any, should be a separate CS-checkable step after Manager approval.

## Return format

Please return one of:

```text
PASS:
  Structure preserves track separation and is safe to use as the repo-organization plan.

HOLD:
  Specific routing or boundary issue must be fixed before file moves.

FAIL:
  Structure materially mixes tracks, reopens closed routes, implies a build/execution, or risks artifact loss.
```

If HOLD or FAIL, include the exact blocker and proposed correction.

## Closed gates

Closed:

```text
No model execution.
No new run.
No D4 rescue.
No CAL-Q rerun.
No certification run.
No compression.
No INT8 / INT4 stress.
No second compression rung.
No full ladder.
No Claim C activation.
No public benchmark packaging.
No funder-facing release.
No SBIR submission.
No software implementation.
No file moves until separate approval.
```

## Intent

The specs have passed. Now we are organizing the instrument as an instrument.

The structure should make the path legible:

```text
Paper A → Tool Spec → G6 Spec → future module designs → eventual implementation
```

without mixing it with CAL-Q finding diagnostics, D4 history, or Paper B stress work.

— Manager
