# CS Routing — Hash Integrity Categorization (Manager decision requested)

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Manager (Senior CC; Senior recommendation aligned and rides along).
**Status:** **REQUEST FOR MANAGER AUTHORIZATION.** CS will not execute any change to the artifact's location without Manager approval. Sealed bytes UNCHANGED. No file moves, no directory creation, no renaming, no deletion performed.

---

## §1. The question

`governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.{md,pdf}` (plus 8 figure files in `governance/standing/figures/`) is paper-like (versioned, has PDF, has figures, has a full review chain) but is deliberately designated **"standing governance note, NOT Paper 4"** per its own header + STATUS line 48 + REVIEW line 57. It currently sits at `governance/standing/`. A reader landing on `papers/` would not find it there and might be surprised.

User raised the discoverability gap; Senior agrees the gap is real and aligned with CS on diagnosis. Decision needed: how to resolve the gap without erasing the "not Paper 4" designation that is itself a deliberate Manager-level call.

## §2. Why this is Manager-scope (not CS-execute)

This is a **categorization decision**, not a housekeeping move. It changes how the program *names what Hash Integrity is*, not just where the file sits. CS scope covers byte-faithful filing and routing-discipline housekeeping; categorization changes require Manager authorization through TL.

This memo is the request; CS will not move bytes on this without explicit Manager direction.

## §3. The three coherent options (and CS+Senior recommendation)

### Option 1 — Leave it at `governance/standing/`

- **Preserves** the "not Paper 4" designation (the file lives in standing governance, where the designation is honored).
- **Relies on prose** (README/STATUS/REVIEW) to point readers from `papers/` toward the file's actual location.
- **Risk:** the discoverability gap that produced this question once is preserved; the same surprise can re-occur.

### Option 2 — Promote to `papers/`

E.g., `papers/paper-hash-integrity-is-not-construct-validity/`.

- **Closes** the discoverability gap directly.
- **But:** flips the deliberate Manager decision that Hash Integrity is NOT Paper 4. Erases the "this is enforceable discipline, not a publication" distinction. **Same category of error as the `paper4-` rename CS just reverted** — both are "rename/relocate to flatten an asymmetry the program made on purpose."
- **CS+Senior judgment:** wrong direction.

### Option 3 (CS+Senior RECOMMENDATION) — Add `papers/standing-notes/` sub-tree

E.g., `papers/standing-notes/hash-integrity-is-not-construct-validity-v0.7.2/` containing the md, pdf, and figures/.

- **Closes** the discoverability gap (the artifact is now visible from `papers/`).
- **Preserves** the "not Paper 4" designation (it's in a `standing-notes/` sub-tree, visibly distinct from `paper1/2/3-` and `paper-a-`; a reader sees immediately that it's a different category of artifact).
- **Expresses the real distinction in structure** rather than relying on prose — which is the same principle CS+Senior just learned the hard way from the Paper A revert.
- **Symmetric with the Paper A lesson:** Paper A was kept at `papers/paper-a-` (not flattened to `paper4-`) because the lettered slug expresses a real lineage; Hash Integrity gets `papers/standing-notes/` (not flattened to `papers/paper-...`) because the standing-note slug expresses a real designation.
- **One caveat (informational):** the `governance/standing/` location of Hash Integrity is referenced in several live-facing docs (README, STATUS, REVIEW) and in the v0.4 structure spec. A move would re-update the live refs (~5 files) and would benefit from a forward-reference note in `tier-1-instrument/organization/` for the v0.4 spec, same pattern as the paper-a/paper4 revert note. CS would handle all of that as part of the move execution.

## §4. The recurring principle this resolves

Senior named (and CS has saved to memory): the repo has a **recurring pattern** — "artifact whose true category doesn't match its `ls` appearance." Two known cases as of 2026-06-14: Paper A (just resolved by *not* renaming to `paper4-`) and Hash Integrity (this memo).

**The settled principle, applied:** when `ls` surprises, the fix is to **express the real distinction in structure** (add a sub-tree, restore a slug), **never to rename to flatten** a real distinction. Option 3 is the structural application of that principle to Hash Integrity. Option 2 would be the same kind of error as the paper4- rename.

Senior has separately offered to draft a short addition to a future v0.5 structure spec that folds this principle into the canonical structure spec itself. CS supports that draft (Senior-scope; CS verifies on filing). This memo is the case-specific Manager decision; the v0.5 spec addition is the durable case-independent record.

## §5. What CS will execute on Manager approval of Option 3

1. Create `papers/standing-notes/` with a stub README explaining the sub-tree (standing-governance-class artifacts that are paper-shaped but explicitly NOT released as numbered/lettered papers).
2. `git mv governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.{md,pdf} papers/standing-notes/hash-integrity-is-not-construct-validity-v0.7.2/` (or chosen sub-dir name per Manager direction).
3. `git mv governance/standing/figures/fig{1,2,3,4}_*.{png,svg}` into the new sub-tree's `figures/` (assuming all 8 figure files belong to this note; CS will verify by reading the note's figure references and only moving the ones it cites).
4. Update live-facing references in README.md, STATUS.md, REVIEW.md, `_meta/INDEX.md`, `governance/epochs/2026-06-11_lane-1a-prime/INDEX.md` to the new path.
5. File `tier-1-instrument/organization/HASH-INTEGRITY-RELOCATION-NOTE-2026-06-14.md` as the forward-reference for the v0.4 structure spec (which still says `governance/standing/`).
6. Hash verification: every pre-move sha256 still present at the new path. Sealed-tree boundary preserved (targeted `git add`, not `-A`).
7. Single commit, push, verify post-push HEAD.

## §6. What CS will NOT do without further Manager direction

- Will not promote Hash Integrity to `papers/paper-N-...` or `papers/paper-X-...` (Option 2). That requires a separate re-designation decision.
- Will not touch the v0.4 structure spec (frozen; supersede-don't-rewrite).
- Will not move other items currently in `governance/standing/` (NORTH-STAR, PROGRAM-MAP, templates, etc. — those are not paper-class; they belong where they are).

## §7. Sealed-bytes posture

Sealed bytes UNCHANGED (≈81st survival check):

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`)
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`)
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`)
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`)

## §8. Disposition requested from Manager

```text
[ ] APPROVE OPTION 3 — papers/standing-notes/ sub-tree. CS executes per §5.
[ ] APPROVE OPTION 1 — leave at governance/standing/. No move; relies on prose.
[ ] APPROVE OPTION 2 — promote to papers/paper-X-... (re-designation). CS executes after Manager specifies the new designator.
[ ] OTHER — Manager-specified alternative.
```

CS recommendation: Option 3 (with Senior alignment).

— CS Engineer, 2026-06-14
