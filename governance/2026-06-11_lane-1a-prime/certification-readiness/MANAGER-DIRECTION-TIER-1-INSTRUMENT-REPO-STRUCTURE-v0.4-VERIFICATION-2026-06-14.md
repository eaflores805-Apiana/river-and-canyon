# Manager Direction — CS Verification of Repo Structure v0.4

**Received:** 2026-06-14 via session (routed through TL)
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — model-free verification requested from CS; no file moves or directory creation authorized.

---

To: CS Engineer
Cc: Senior Engineer, Team Lead
From: Manager
Re: Verification of `TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4.md`
Status: Model-free verification requested; no file moves or directory creation authorized

CS,

Please verify:

```text
TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4.md
```

This v0.4 revision extends the CS-passed v0.3 structure to cover the whole repository after the complete inventory returned HOLD.

The purpose is to determine whether v0.4 is sufficient to support inventory v0.2.

This is not a move authorization.

## Required verification

Please verify that v0.4:

```text
1. Preserves the accepted v0.3 Tier 1 structure.
2. Extends coverage to the whole repository.
3. Routes all eight previously out-of-scope categories.
4. Resolves the INDEX-location issue.
5. Resolves or flags the sub-directory ambiguities.
6. Preserves sealed-byte boundaries.
7. Implies no file moves, directory creation, execution, build, deletion, or renaming.
```

## Eight out-of-scope categories

Please verify that v0.4 provides a destination for:

```text
1. Papers 1, 2, 3 + paper-hash-integrity standing note
2. Older Lane-1a work under governance/2026-06-10_lane1a/
3. B1 harness governance + experiments
4. Paper 2/3 governance
5. Standing governance under governance/standing/
6. Passdown governance under governance/passdown/
7. Root-level docs
8. Ancillary directories:
   diagrams/
   notes/
   writing/
   review/
```

## Ambiguity checks

Please verify the following resolutions:

```text
- revisions/, verifications/, and organization/ route with their parent artifact.
- sweep-byte relocation is flagged, not authorized.
- Paper A supplement vs D4/archive duplication risk is handled by reference-not-copy.
- first-compression-rung is routed as Lane-1a-prime historical evidence, not Paper B activation and not D4.
- ancillary directories are not routed into the Tier 1 instrument.
```

## INDEX check

Please verify that v0.4 no longer claims a root-level INDEX currently exists.

It should state:

```text
- active program INDEX currently lives at governance/2026-06-11_lane-1a-prime/INDEX.md
- tier0 INDEX lives under tier0-run/governance/...
- /_meta/INDEX.md is only a future target
- promotion/reconciliation of INDEX files is a move-time decision
```

## Source-of-truth and boundary checks

Please verify that these remain intact:

```text
- Paper A v1.0 remains the paper source of truth.
- Tool Spec v0.1 remains the Tier 1 architecture source of truth.
- G6 Spec v0.1 remains the G6 module source of truth.
- schemas remain future lifts from specs.
- /tier-1-instrument/implementation/ remains placeholder only.
- /paper-b/ remains deferred and inactive.
- D4 remains closed historical archive only.
- CAL-Q remains finding track, not D4 rescue.
```

## Return format

Please return one of:

```text
PASS:
  v0.4 covers the whole repo and is safe to use for inventory v0.2.

HOLD:
  Specific category, ambiguity, INDEX, sealed-byte, or boundary issue must be fixed before inventory v0.2.

FAIL:
  v0.4 materially mixes tracks, reopens closed routes, implies a move/build/execution, or risks artifact loss.
```

If HOLD or FAIL, include the exact blocker and proposed correction.

## Closed gates

Closed:

```text
No file moves.
No directory creation.
No renaming.
No deletion.
No software build.
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
No Paper B activation.
Sealed bytes DO NOT MOVE.
```

## Next decision if PASS

If v0.4 passes, the next Manager decision will be whether to authorize:

```text
COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.2
```

That inventory v0.2 is still not the move.

Actual file moves remain a later, separately approved step.

— Manager
