# Manager Direction — Ratify Inventory v0.2 Flags and Authorize Move Plan Draft

**Received:** 2026-06-14 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — move plan drafting authorized; no file moves authorized.

---

To: CS Engineer
Cc: Senior Engineer, Team Lead
From: Manager
Re: Move-planning step after `COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.2` PASS
Status: Move plan drafting authorized; no file moves authorized

CS,

I accept the PASS on:

```text
COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.2
```

Inventory v0.2 has fully reconciled the repository against:

```text
TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4.md
```

The next step is move planning.

This direction authorizes drafting the move plan only.

It does not authorize file moves.

## Ratification of inventory flags

I ratify the following five inventory flags as move-planning assumptions:

```text
1. Sweep-byte relocation:
   Sweep run records and rescore JSONs currently in certification-readiness/ should be planned for physical relocation to experiments/ at move time, with hash verification.

2. First-compression-rung:
   Ratify v0.4 routing as Lane-1a-prime historical evidence.
   It is NOT Paper B activation.
   It is NOT D4.

3. Duplicate pairs:
   The 7 known byte-identical Paper A bundle vs certification-readiness working-master duplicate pairs should be handled by deleting the redundant working masters only after the move plan verifies byte identity and preservation of canonical release artifacts.

4. INDEX promotion:
   Use option (c):
   create a future top-level /_meta/INDEX.md that references both existing INDEX files rather than silently replacing either one.

5. Sealed bytes:
   Ratify in-place routing.
   Sealed bytes remain DO NOT MOVE.
```

## Authorized next artifact

Please prepare:

```text
REPO-MOVE-PLAN-v0.1
```

## Required contents

The move plan should include:

```text
1. Executive summary
2. Source structure
3. Target structure
4. Per-category move plan
5. Exact file-move table for all files that will physically move
6. Explicit list of files that will not move
7. Duplicate-pair handling plan
8. Sweep-byte relocation plan
9. INDEX promotion/reconciliation plan
10. Sealed-byte handling plan
11. Hash-verification procedure
12. Rollback plan
13. Post-move verification checklist
14. Closed gates
```

## Required distinction

Please distinguish clearly between:

```text
- files that move
- files that remain in place
- files that are referenced by hash
- duplicate files proposed for deletion after verification
- future placeholders that are not created yet
```

## Boundary

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
No Paper B activation.
No public benchmark packaging.
No funder-facing release.
No SBIR submission.
Sealed bytes DO NOT MOVE.
```

## Return path

After `REPO-MOVE-PLAN-v0.1` is drafted:

```text
CS verifies the plan.
Team Lead routes it.
Manager decides whether to authorize the actual move.
```

Actual file movement remains a later, separately approved step.

## Intent

The map is accepted.

The inventory passed.

Now draft the move plan before moving anything.

— Manager
