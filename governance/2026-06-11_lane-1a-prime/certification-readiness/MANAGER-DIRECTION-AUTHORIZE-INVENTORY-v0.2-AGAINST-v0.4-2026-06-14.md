# Manager Direction — Authorize Inventory v0.2 Against Repo Structure v0.4

**Received:** 2026-06-14 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — model-free inventory authorized; no file moves or directory creation authorized.

---

To: CS Engineer
Cc: Senior Engineer, Team Lead
From: Manager
Re: `COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.2` against whole-repo structure
Status: Model-free inventory authorized; no file moves or directory creation authorized

CS,

I accept the PASS on:

```text
TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4.md
```

v0.4 is now the accepted whole-repo organization plan.

Please prepare:

```text
COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.2
```

## Purpose

The purpose of inventory v0.2 is to rerun the complete artifact inventory against the accepted v0.4 whole-repo map.

This is still inventory only.

It is not the move.

## Required scope

Reconcile the full inventory against v0.4, including:

```text
1. Paper A release artifacts
2. Papers 1, 2, and 3
3. Tier 1 instrument artifacts
4. Tool Spec and G6 Spec
5. CAL-Q finding-track artifacts
6. Paper B planning placeholders
7. D4 closed-route historical materials
8. governance/standing/
9. governance/passdown/
10. governance dated epochs
11. experiments/
12. tier0-run/
13. root-level docs
14. diagrams/
15. notes/
16. writing/
17. review/
18. all verification records
19. all superseded versions
20. all INDEX/catalog files
```

## Required checks

Please verify:

```text
1. Every in-scope artifact has exactly one proposed destination under v0.4.
2. No artifact is dropped.
3. No artifact is double-homed.
4. No active artifact is archived by mistake.
5. No historical artifact is routed into an active module track by mistake.
6. CAL-Q remains a finding track, not D4 rescue.
7. first-compression-rung remains historical Lane-1a-prime evidence, not Paper B activation and not D4.
8. sweep bytes are flagged according to v0.4: source bytes vs governance interpretation clearly distinguished.
9. Paper A supplement references canonical bytes by hash and does not duplicate run-data bytes into /papers/.
10. sealed bytes remain DO NOT MOVE.
11. INDEX/catalog files are handled according to v0.4:
    - actual current locations recorded
    - /_meta/INDEX.md remains future target only
    - promotion/reconciliation deferred to move-time decision.
12. root docs and ancillary directories are not incorrectly routed into Tier 1 instrument.
```

## Special Manager-ratification flags

Please explicitly flag any item needing Manager decision before moves, especially:

```text
- sweep-bytes relocation authorization
- first-compression-rung ratification as historical Lane-1a-prime evidence
- any physical duplication between Paper A supplement, D4 archive, governance, and experiments
- INDEX promotion or reconciliation
- sealed-byte handling
```

## Return format

Please return one of:

```text
PASS:
  Inventory v0.2 fully reconciles all artifacts against v0.4 and is ready for Manager move-planning review.

HOLD:
  Inventory is complete, but specific Manager routing decisions are required before move planning.

FAIL:
  Inventory cannot safely support repo move planning.
```

If HOLD or FAIL, include exact blockers and proposed decisions.

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

## Intent

The whole-repo map is now accepted.

Now reconcile every artifact against that map before moving anything.

— Manager
