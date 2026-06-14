# Manager Direction — Authorize Repo Move Execution Under REPO-MOVE-PLAN-v0.1

**Received:** 2026-06-14 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — repo move execution AUTHORIZED under plan constraints on branch `repo-move-v0.1`. Sealed bytes DO NOT MOVE.

---

To: CS Engineer
Cc: Senior Engineer, Team Lead
From: Manager
Re: Execute repo reorganization under `REPO-MOVE-PLAN-v0.1`
Status: Repo move authorized under plan constraints only

CS,

I accept the PASS on:

```text
REPO-MOVE-PLAN-v0.1
```

You are authorized to execute the repo reorganization exactly under that plan.

## Authorization

Proceed with the move on the planned branch:

```text
repo-move-v0.1
```

Follow the 13-phase execution sequence A–M from `REPO-MOVE-PLAN-v0.1`.

Do not merge to main until all post-move checks PASS.

## Ratified execution assumptions

The five inventory flags remain ratified:

```text
1. Sweep-byte relocation:
   Move the 7 sweep-byte files to experiments/ only with hash verification.

2. First-compression-rung:
   Route as Lane-1a-prime historical evidence.
   Not Paper B.
   Not D4.

3. Duplicate working masters:
   Delete only the redundant byte-identical working masters after verification confirms canonical release artifacts are preserved.

4. INDEX:
   Create _meta/INDEX.md as a pointer index referencing both existing INDEX files at their post-move paths.
   Do not silently replace either source INDEX.

5. Sealed bytes:
   Sealed bytes remain DO NOT MOVE.
   Any sealed-byte hash mismatch is a critical fail and triggers rollback.
```

## Required execution controls

During execution, preserve:

```text
- hash verification before and after move
- no dropped artifacts
- no double-homed artifacts unless explicitly reference-only
- no active artifact archived by mistake
- no historical D4 artifact routed into active Tier 1
- CAL-Q remains finding track, not D4 rescue
- Paper B remains inactive
- first-compression-rung remains historical Lane-1a-prime evidence
- Paper A release artifacts remain canonical
- Paper A supplement references canonical bytes by hash rather than duplicating run data
```

## Post-move verification

After execution, return a verification report covering:

```text
1. branch used
2. commit hash
3. files moved
4. files left in place
5. directories created
6. duplicate files deleted after verification
7. hash verification results
8. sealed-byte verification
9. INDEX reconciliation result
10. Paper A artifact verification
11. Tier 1 instrument verification
12. CAL-Q finding-track verification
13. D4 archive verification
14. rollback status
15. final PASS / HOLD / FAIL disposition
```

## Failure handling

If any of the following occurs, stop and return HOLD or FAIL:

```text
- sealed-byte hash mismatch
- missing artifact
- unexpected duplicate
- failed hash verification
- Paper A canonical artifact ambiguity
- CAL-Q routed as D4 rescue
- first-compression-rung routed into Paper B
- D4 route reopened
- INDEX conflict unresolved
- any move outside the approved plan
```

## Still closed

This repo move does not authorize:

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
No Paper B activation.
No software build.
No public benchmark packaging.
No funder-facing release.
No SBIR submission.
```

## Intent

The map passed.

The inventory passed.

The move plan passed.

Now execute the repo move under controlled branch, hash checks, sealed-byte protection, and rollback discipline.

— Manager
