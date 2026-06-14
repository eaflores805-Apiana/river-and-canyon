# Rename-Revert Note — `papers/paper4-before-retention/` → `papers/paper-a-before-retention/` (revert + canonical A/B convention)

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior, Manager (informational; user-directed; supersedes the prior `RENAME-NOTE-PAPER-A-TO-PAPER-4-2026-06-14.md`).
**Status:** REVERT EXECUTED on `main` (commit at push). The rename at `535421a` (paper-a → paper4) has been reversed. Both the original rename and this revert remain in git history; sealed bytes UNCHANGED throughout.

---

## §1. What changed

On 2026-06-14, after Senior raised the lineage-collapse concern and user confirmed, the directory `papers/paper4-before-retention/` was renamed back to `papers/paper-a-before-retention/` via `git mv`. All 38 files in the bundle moved with it byte-for-byte. The same 5 live-facing references that were updated forward (README, STATUS, REVIEW, `_meta/INDEX`, `governance/epochs/2026-06-11_lane-1a-prime/INDEX`) were updated back.

The prior `RENAME-NOTE-PAPER-A-TO-PAPER-4-2026-06-14.md` (filed at commit `5d38805`) is **superseded by this note** but retained on disk per supersede-don't-rewrite. Both notes together record the round-trip: rename happened, was caught by review, was reverted.

## §2. Why the revert — the A/B paper lineage (now stated authoritatively)

**The River and Canyon program maintains two distinct paper lineages, and they are not interchangeable.** This is a load-bearing program-organization fact that should be hit before any future "rename for consistency" impulse.

### §2.1 Lineage one — numbered metrology series (`paper1/2/3-`)

A sequential arc of pre-stress metrology papers building toward the compression-stress seam:

- `papers/paper1-survival-is-not-correctness/` — the metrology method.
- `papers/paper2-correctness-is-not-constructibility/` — the first result.
- `papers/paper3-certification-before-retention/` — the certification protocol.

Each is a numbered step in the *method → result → protocol* progression. The slug convention `paper{N}-{short-title}` reflects sequential authorship in that arc.

### §2.2 Lineage two — lettered instrument/stress dyad (`paper-a-` / future `paper-b-`)

A pair of papers distinct from the metrology series:

- `papers/paper-a-before-retention/` — Paper A, the *instrument* paper. The fail-closed validity gate that decides whether a baseline is safe to compare BEFORE any retention claim is made. Came OUT of *applying* Paper 3 to a candidate baseline (the D4 episode). Released v1.0. Distinct kind of paper from the 1/2/3 method/result/protocol arc: it is an instrument distilled from a worked refusal, not the next step of the metrology progression.
- `/paper-b/planning/` — Paper B, the *stress-retention* paper. Future work. Uses a gate-cleared baseline (from Paper A's protocol) to run the compression sweep and report retention. **DEFERRED.** Requires separate Manager authorization. Currently a placeholder.

The lettered convention (A / B) encodes the **instrument ↔ stress** pairing: Paper A is the gate; Paper B is the stress that the gate authorizes. They are paired by function, not sequenced by method.

### §2.3 Why naming matters

Renaming `paper-a-` → `paper4-` collapses the two lineages into one by implying Paper A is the fourth step of the numbered metrology arc. By symmetry, future Paper B would have to become `paper5-`, which is semantically false: Paper B is not the fifth metrology paper, it is the stress paper paired with Paper A. The collapse erases the structural distinction the program deliberately made (visible in the existing `/paper-b/planning/` top-level directory, which already commits to the lettered convention).

The right way to read `ls papers/` is:

```text
paper1-survival-is-not-correctness/        \
paper2-correctness-is-not-constructibility/ |  numbered metrology series
paper3-certification-before-retention/      /
paper-a-before-retention/                  -- lettered instrument/stress dyad,
                                              paired with future /paper-b/
```

Paper A "sticks out" because it genuinely is a different kind of object in a different lineage. That asymmetry is honest, not sloppy.

## §3. What this note authoritatively asserts

For any future repo-organization work or rename impulse, the binding rules are:

1. **Two paper lineages exist.** Numbered metrology series (`paper1/2/3-`) AND lettered instrument/stress dyad (`paper-a-` + future `paper-b-`).
2. **Do not rename across lineages.** Specifically, do not propose `paper4-` for Paper A or `paper5-` for Paper B. The slug encodes the lineage; renaming changes the meaning.
3. **Future Paper B materialization** should use the `paper-b-{short-title-slug}/` form to make the dyad legible in the listing (e.g., `papers/paper-b-retention-under-compression/` or similar). The existing `/paper-b/planning/` placeholder is preserved.
4. **The structure spec v0.4** still describes paths as they were at acceptance time (using `paper-a-before-retention/`). That continues to be correct.

## §4. Disposition of the prior rename note

`tier-1-instrument/organization/RENAME-NOTE-PAPER-A-TO-PAPER-4-2026-06-14.md` (commit `5d38805`) is **SUPERSEDED by this note**. The prior note assumed the rename was the new canonical state and instructed readers to interpret `papers/paper-a-before-retention/` references as forward-references to `paper4-`. That instruction is now incorrect — the canonical state is back to `papers/paper-a-before-retention/`. Readers should disregard the forward-reference rule from the prior note; all old `paper-a-before-retention/` references in any document now resolve to their original paths directly.

The prior note remains on disk as a record of the round-trip. Per supersede-don't-rewrite it is not deleted; this note is the canonical disposition going forward.

## §5. Recommended follow-on (CS-flagged, Senior-drafted)

Senior recommended that the A/B lineage distinction belongs in the **structure spec itself**, not just in this revert note + CS memory. A future v0.5 structure spec (Senior-drafted, CS-verified) whose only delta from v0.4 is to explicitly enumerate the two paper lineages + the lettered-dyad convention would close the gap permanently: the next rename impulse would hit the rationale in the canonical spec before reaching for a directory rename.

This note holds the line until v0.5 lands.

## §6. Sealed-bytes posture

Sealed bytes UNCHANGED throughout the rename, the forward note, and this revert (≈80th survival check):

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`)
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`)
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`)
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`)

— CS Engineer, 2026-06-14
