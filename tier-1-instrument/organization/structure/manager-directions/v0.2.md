# Manager Direction — CS Verification of Tier 1 Repo Structure v0.2

**Received:** 2026-06-14 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — model-free verification requested from CS; no file moves authorized.

---

To: CS Engineer
Cc: Senior Engineer, Team Lead
From: Manager
Re: Verification of `TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.2.md`
Status: Model-free verification requested; no file moves authorized

CS,

Please verify:

```text
TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.2.md
```

This v0.2 revision incorporates the four polish notes from your prior PASS on v0.1. The structure remains accepted in principle, but no file moves are authorized until v0.2 is verified and a separate move plan is approved.

## Required verification

Please check that v0.2 fully resolves the four prior notes:

```text
1. Paper A reference corrected:
   - release artifact is PAPER-A-v1.0.md
   - no "-DRAFT-" release filename
   - canonical sha256 reference updated to 4272e12a…

2. G6 routing language tightened:
   - G6 spec FILE routes to /tier-1-instrument/specs/
   - G6 module-work directory routes to /tier-1-instrument/modules/g6-standing-rejection-audit/
   - the spec file and module-work directory are not treated as the same thing

3. Closed gates updated:
   - "No file moves until separately approved" appears explicitly in §10

4. Move-time inventory requirement added:
   - before any reorganization, CS must produce a complete artifact inventory
   - this must include currently unenumerated certification-readiness materials
   - no artifact may be dropped, duplicated, or routed into the wrong track
```

## Track-separation check

Please verify that the four-track separation remains intact:

```text
1. Paper A:
   /papers/paper-a-before-retention/

2. Tier 1 instrument:
   /tier-1-instrument/

3. CAL-Q finding track:
   /finding-tracks/cal-q-format-sensitive-abstention/

4. Paper B and D4 history:
   /paper-b/planning/
   /archive/d4-closed-route/
```

Confirm that:

```text
- Paper A remains a finished release, not an active instrument workspace.
- Tier 1 instrument is the active tool-spec and module-spec track.
- CAL-Q finding diagnostics remain secondary future research.
- CAL-Q is not filed as D4 rescue.
- Paper B remains deferred stress-rung planning only.
- D4 remains historical archive only and is not reopened.
```

## Placeholder honesty check

Please verify that the following are still marked as placeholders or future work, not existing artifacts:

```text
schemas
human-read templates
worked examples
implementation stubs
Paper B planning artifacts
```

Also verify that `/tier-1-instrument/implementation/` is reserved only and does not imply software build authorization.

## Source-of-truth check

Please verify that the structure preserves the following source-of-truth hierarchy:

```text
Paper A v1.0:
  source of truth for the instrument paper and scope

EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1:
  source of truth for the Tier 1 tool architecture

G6-STANDING-REJECTION-AUDIT-SPEC-v0.1:
  source of truth for the G6 module spec
```

Schema files, when later extracted, must be described as faithful lifts from the specs, not independent sources of truth.

## File-move boundary

This direction does not authorize file moves.

Please verify v0.2 only.

If v0.2 passes, the next Manager decision will be whether to authorize a complete artifact inventory for move planning. The inventory is a separate step from the move itself.

## Return format

Please return one of:

```text
PASS:
  v0.2 resolves prior polish notes and is safe to use as the repo-organization plan.

HOLD:
  Specific routing, source-of-truth, placeholder, or closed-gate issue must be fixed before inventory/move planning.

FAIL:
  v0.2 materially mixes tracks, reopens closed routes, implies a build/execution, or risks artifact loss.
```

If HOLD or FAIL, include the exact blocker and proposed correction.

## Closed gates

Closed:

```text
No file moves.
No directory creation.
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
```

## Intent

The structure is accepted in principle.

This verification confirms the map is clean before we inventory or move anything.

— Manager
