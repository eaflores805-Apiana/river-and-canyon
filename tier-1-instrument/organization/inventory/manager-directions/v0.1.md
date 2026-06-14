# Manager Direction — Authorize Complete Artifact Inventory for Repo Move Planning

**Received:** 2026-06-14 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — model-free inventory authorized; no file moves or directory creation authorized.

---

To: CS Engineer
Cc: Senior Engineer, Team Lead
From: Manager
Re: Complete artifact inventory before Tier 1 repo reorganization
Status: Model-free inventory authorized; no file moves or directory creation authorized

CS,

The repo structure has passed through v0.3 and is accepted as the final organization plan before inventory.

Please prepare:

```text
COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.1
```

## Purpose

The purpose is to inventory every artifact before any repo reorganization is authorized.

This is the inventory step only.

It is not the move.

## Required scope

Please produce a complete artifact inventory covering:

```text
1. Paper A release artifacts
2. Paper A governance records
3. Tier 1 instrument specs
4. G6 spec and related verification records
5. CAL-Q finding-track artifacts
6. D4 closed-route historical materials
7. certification-readiness/ contents
8. run records
9. rescore records
10. verification memos
11. superseded versions
12. INDEX / catalog records
```

## Required routing fields

For each artifact, include:

```text
- current path
- filename
- sha256 or available hash
- artifact type
- current status
- proposed destination under v0.3 structure
- track assignment:
  Paper A / Tier 1 Instrument / CAL-Q Finding / Paper B / D4 Archive / Root Index
- whether it is active, historical, superseded, placeholder, or source-of-truth
- whether it should move, remain, be copied, or be referenced only
- notes / ambiguity flags
```

## Required checks

Please verify:

```text
1. No artifact is dropped.
2. No artifact is double-homed.
3. No active artifact is archived by mistake.
4. No historical D4 artifact is routed into the active Tier 1 instrument.
5. CAL-Q finding artifacts are not filed as D4 rescue.
6. Paper A release artifacts remain distinct from drafts or working files.
7. Tool Spec and G6 Spec remain under Tier 1 instrument.
8. Future placeholders are not treated as existing files.
9. INDEX remains root-level and indexes all tracks.
10. Any ambiguous artifact is flagged for Manager decision before moves.
```

## Boundary

This authorizes inventory only.

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
```

## Return format

Please return:

```text
PASS:
  Complete inventory is ready for Manager review and move planning.

HOLD:
  Inventory incomplete or ambiguous artifacts require Manager routing decisions.

FAIL:
  Inventory cannot safely support move planning.
```

If HOLD or FAIL, include exact blockers.

## Intent

The map is clean.

Now inventory every artifact before moving anything.

— Manager
