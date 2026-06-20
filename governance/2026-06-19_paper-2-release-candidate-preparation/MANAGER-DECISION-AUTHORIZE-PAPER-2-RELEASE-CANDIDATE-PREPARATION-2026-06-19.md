# Manager Decision — Authorize Paper 2 Release-Candidate Preparation

**To:** CS Engineer, Senior Engineer
**Cc:** C5, Team Lead
**From:** Manager
**Subject:** Authorize Release-Candidate Preparation for Revised Paper 2
**Status:** AUTHORIZED — release-candidate preparation only

Manager chooses:

```text
A. Authorize release-candidate preparation.
```

## Source reviewed manuscript

Use the reviewed integrated manuscript:

```text
papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-REVISED-MANUSCRIPT-DRAFT-v0.1.md
sha256: d19c060a5325ba5f3a71aa6fd395dec5fc9550087f2d89ba8dcc540afc2f5917
HEAD: e5fe1d328ea18fc061812c3d1f54bee15280b2c7
```

This manuscript has cleared:

```text
C5 integrated claim-risk: PASS
CS provenance / digest review: PASS
```

## Authorized task

Prepare a clean release-candidate manuscript file for Paper 2 by extracting the manuscript body from the reviewed draft.

The reviewer cover note must not be included in the release-candidate manuscript.

## Authorized scope

CS/Senior may:

```text
1. Create a clean Paper 2 release-candidate manuscript file.
2. Remove only the reviewer cover note.
3. Preserve the manuscript body exactly from the reviewed draft after the BEGIN REVISED MANUSCRIPT marker.
4. File the release-candidate manuscript to the appropriate Paper 2 path.
5. Recompute sha256.
6. Confirm exact body match against the reviewed draft body.
```

## Not authorized

No claim prose changes.
No edits to argument, wording, tables, references, appendix text, or claims.
No new experiment.
No rerun.
No construction redesign.
No compression.
No INT8.
No INT4.
No tooling edit.
No threshold change.
No prompt or artifact regeneration.

If any claim-bearing prose changes, return to C5 before proceeding.

## Required return

Return:

```text
CS RETURN — PAPER 2 RELEASE-CANDIDATE PREPARATION COMPLETE
```

Include:

```text
- commit SHA
- final remote HEAD
- clean-fetch confirmation
- release-candidate manuscript path
- release-candidate manuscript sha256
- source reviewed manuscript path and sha256
- confirmation reviewer cover note was removed
- confirmation manuscript body is byte-preserved from the reviewed draft after BEGIN REVISED MANUSCRIPT
- confirmation Paper 2 v1.0 tag remains untouched
- confirmation released Paper 2 file, if separate, was not overwritten unless explicitly intended
- confirmation no run / rerun / compression / tooling / threshold change occurred
```

## Boundary

This authorizes release-candidate preparation only.

It does not authorize public release, publication, tagging, or replacing the released Paper 2 artifact unless separately approved.

The Path A FP16 K=5 FAIL remains closed.

— Manager
