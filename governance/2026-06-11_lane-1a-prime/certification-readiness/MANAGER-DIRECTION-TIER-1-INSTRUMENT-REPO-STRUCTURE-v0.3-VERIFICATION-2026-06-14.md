# Manager Direction — CS Verification of Repo Structure v0.3

**Received:** 2026-06-14 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — model-free verification requested from CS; no file moves or directory creation authorized.

---

To: CS Engineer
Cc: Senior Engineer, Team Lead
From: Manager
Re: Verification of `TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.3.md`
Status: Model-free verification requested; no file moves or directory creation authorized

CS,

Please verify:

```text
TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.3.md
```

This revision is a cleanup pass after your v0.2 PASS. The structure remains accepted in principle. No file moves are authorized.

## Verification purpose

Confirm that v0.3 resolves the two remaining polish issues without changing the accepted structure, routing, or boundaries.

## Required checks

Please verify:

```text
1. Header/version consistency:
   - line-1 title says v0.3
   - version block says v0.3
   - no lingering v0.1/v0.2 title mismatch remains

2. Paper A routing clarity:
   - release artifact remains PAPER-A-v1.0.md
   - release hash remains 4272e12a…
   - no "-DRAFT-" release filename is introduced
   - the prior working-master / 464a8889 reference no longer creates move-time ambiguity or double-counting risk

3. Four-track separation remains unchanged:
   - Paper A release artifacts route to /papers/paper-a-before-retention/
   - Tier 1 instrument artifacts route to /tier-1-instrument/
   - CAL-Q finding diagnostics route to /finding-tracks/cal-q-format-sensitive-abstention/
   - Paper B planning and D4 historical archive remain separate

4. G6 routing remains clear:
   - G6 spec FILE routes to /tier-1-instrument/specs/
   - G6 module-work directory routes to /tier-1-instrument/modules/g6-standing-rejection-audit/
   - spec file and module-work directory are not treated as the same artifact

5. Placeholder honesty remains intact:
   - schemas are future lifts from specs
   - human-read templates are future
   - examples are future
   - implementation is placeholder only
   - Paper B planning artifacts are not implied to exist

6. Move-time inventory requirement remains intact:
   - before any reorganization, CS must produce a complete artifact inventory
   - the inventory must include currently unenumerated certification-readiness materials
   - no artifact may be dropped, duplicated, or routed into the wrong track

7. Closed gates remain intact:
   - no file moves
   - no directory creation
   - no software implementation
   - no model execution
   - no D4 rescue
   - no CAL-Q rerun
   - no Paper B stress work
```

## Return format

Please return one of:

```text
PASS:
  v0.3 resolves the remaining cleanup notes and is safe to use as the final repo-organization plan before artifact inventory.

HOLD:
  Specific cleanup, routing, placeholder, or boundary issue must be fixed before inventory authorization.

FAIL:
  v0.3 materially changes the accepted structure, mixes tracks, reopens closed routes, implies execution/build, or risks artifact loss.
```

If HOLD or FAIL, include the exact blocker and proposed correction.

## Boundary

This verification does not authorize file moves.

Closed:

```text
No file moves.
No directory creation.
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
```

## Next decision if PASS

If v0.3 passes, the next Manager decision will be whether to authorize:

```text
COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.1
```

That inventory is not the move.

The actual repo reorganization remains a later, separately approved step.

— Manager
