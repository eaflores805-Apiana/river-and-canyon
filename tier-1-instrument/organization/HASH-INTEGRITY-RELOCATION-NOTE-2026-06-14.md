# Hash Integrity Relocation Note — `governance/standing/` → `papers/standing-notes/`

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior, Manager (informational; executes Manager Option 3 disposition).
**Status:** Forward-reference for any pre-relocation document that still cites the old path. Hash Integrity v0.7.2 has been moved per Manager direction (Option 3 from `CS-ROUTING-HASH-INTEGRITY-CATEGORIZATION-REQUEST-2026-06-14.md`).

---

## §1. What changed

On 2026-06-14, by Manager direction (TL ACTION memo "CS Action: Hash Integrity Option 3 Filing"), the Hash Integrity standing note + its 8 associated figure files were relocated:

**From:**
- `governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md`
- `governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.pdf`
- `governance/standing/figures/fig1_triad.{png,svg}`
- `governance/standing/figures/fig2_halo.{png,svg}`
- `governance/standing/figures/fig3_signature.{png,svg}`
- `governance/standing/figures/fig4_gate.{png,svg}`

**To:**
- `papers/standing-notes/hash-integrity-is-not-construct-validity-v0.7.2/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md`
- `papers/standing-notes/hash-integrity-is-not-construct-validity-v0.7.2/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.pdf`
- `papers/standing-notes/hash-integrity-is-not-construct-validity-v0.7.2/figures/fig{1,2,3,4}_*.{png,svg}`

Plus a new `papers/standing-notes/README.md` that explains the sub-tree's purpose (paper-class artifacts deliberately NOT released as numbered/lettered papers).

All 10 files were `git mv`'d (history preserved); all 10 post-move sha256 hashes match pre-move (byte-faithful preservation verified). The bundle's internal `figures/...` relative paths still resolve correctly (the figures moved with the md to maintain the same relative structure).

## §2. Why this note exists (the same pattern as the Paper A rename revert)

Two pre-2026-06-14 documents are CS-PASSed and currently authoritative but still reference the old `governance/standing/HASH-INTEGRITY-...` path:

- `tier-1-instrument/organization/structure/v0.4.md` (the current accepted whole-repo structure spec) — references `governance/standing/` as the home for the hash-integrity standing note (via the `governance/standing/` track description).
- `tier-1-instrument/organization/inventory/v0.2.md` (the current inventory PASS reconciliation against v0.4) — references the old path in its enumeration.

Per the program's **supersede-don't-rewrite** discipline, those frozen versions are not edited in place. This note is the forward-reference that resolves the path drift without modifying either spec.

Additional historical references (do NOT need updating — correct as as-filed records of their respective filing dates):

- `tier-1-instrument/organization/CS-ROUTING-HASH-INTEGRITY-CATEGORIZATION-REQUEST-2026-06-14.md` (this CS routing request was filed *before* the move; references old path as the request's subject)
- `tier-1-instrument/organization/inventory/v0.1.md` (superseded HOLD; same as-filed status)
- `governance/epochs/2026-06-11_lane-1a-prime/MANAGER-HASH-INTEGRITY-LIFECYCLE-CLOSEOUT-2026-06-12.md` (historical Manager direction)
- `governance/epochs/2026-06-11_lane-1a-prime/CS-HASH-INTEGRITY-OVERVIEW-INTEGRATION-VERIFY-v0.1.md` (historical CS verification)
- `governance/epochs/2026-06-11_lane-1a-prime/CS-HASH-INTEGRITY-v0.7.2-FINAL-VERIFY.md` (historical CS verification)
- `governance/epochs/2026-06-11_lane-1a-prime/CS-HASH-INTEGRITY-v0.7.2-FILING-RETURN.md` (historical CS filing return)
- `governance/epochs/2026-06-11_lane-1a-prime/CS-HASH-INTEGRITY-v0.7.1-FINAL-VERIFY.md` (historical CS verification of v0.7.1)
- `governance/epochs/2026-06-11_lane-1a-prime/CS-SEMANTIC-READ-MINI-MAP-REVIEW-v0.1.md` (historical CS review citing the standing note)

## §3. The forward-reference rule (binding)

**Read every `governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.{md,pdf}` reference in any pre-relocation document as `papers/standing-notes/hash-integrity-is-not-construct-validity-v0.7.2/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.{md,pdf}`** when resolving the file on disk. The contents and the bundle's internal figure-references are byte-identical to what was filed under the old location; only the parent directory location changed.

**Read every `governance/standing/figures/fig{1,2,3,4}_*.{png,svg}` reference** (if any document still does this — most cite the figures via the md's relative `figures/...` path, which is unchanged inside the bundle) **as `papers/standing-notes/hash-integrity-is-not-construct-validity-v0.7.2/figures/fig{1,2,3,4}_*.{png,svg}`**.

## §4. Live-facing references updated (not part of forward-ref scope)

The 3 live-facing references were updated in the same commit:

- `README.md` (root)
- `REVIEW.md` (root)
- `governance/epochs/2026-06-11_lane-1a-prime/INDEX.md` (active program catalog)

These point at the new path directly; no forward-reference is required to resolve them.

(`STATUS.md` does not reference the old path; no update needed.)

## §5. What the relocation does NOT do (Manager-binding constraints from the TL ACTION memo)

- Does **not** alter the scientific claim of Hash Integrity (the note's text is unchanged).
- Does **not** promote Hash Integrity to Paper 4. The artifact remains a standing governance note; the `standing-notes/` sub-dir name preserves the designation.
- Does **not** renumber the paper sequence. `papers/paper1/2/3-` and `papers/paper-a-` are unchanged.
- Does **not** modify model-facing artifacts.
- Does **not** execute code or models.
- Does **not** open G6 implementation.
- Does **not** activate Paper B.
- Does **not** reopen D4.
- Does **not** touch compression / INT8 / INT4 routes.
- Does **not** create external-release language (the artifact's "not for external promotion without blinded review" status is unchanged).

## §6. What `governance/standing/` retains

After the move, `governance/standing/` retains all non-paper-class standing artifacts: NORTH-STAR (v1.1 + v1.2), PROGRAM-MAP-v2.0, PROGRAM-POSITION-v0.1, PROGRAM-STAGE-MAP (v0.1 + v0.2), ROUTE-STATE-GATE-v0.1, SHOWN-SEMANTIC-READ-TEMPLATE-v1.0, STANDARD-RETURN-TEMPLATE-v1.0, STANDING-NON-AUTHORIZATIONS, STANDING-REVIEW-DISCIPLINE, SUBMAP-CONVENTION-v1.0, VERIFICATION-PROTOCOL-v1.0, CLOSEOUT-TEMPLATE-v1.0, CONDITIONAL-LIFECYCLE-AUTHORIZATION-PATTERN-v0.1, PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM, and WHAT-KIND-OF-SMOOTHING-v0.2. None of these are paper-class; all stay in `governance/standing/`.

The `governance/standing/figures/` subdirectory was removed (it held only Hash Integrity figures; now empty and unused).

## §7. Sealed-bytes posture

Sealed bytes UNCHANGED (~84th survival check):

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`)
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`)
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`)
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`)

Sealed-tree boundary preserved: targeted `git mv` + `git add` only, no `-A`.

— CS Engineer, 2026-06-14
