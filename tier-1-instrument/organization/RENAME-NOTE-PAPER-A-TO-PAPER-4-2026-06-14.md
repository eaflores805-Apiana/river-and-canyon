# Rename Note — `papers/paper-a-before-retention/` → `papers/paper4-before-retention/`

**Author:** CS Engineer
**Date:** 2026-06-14
**Scope:** path-rename housekeeping only; no structural change to any spec; no content change to any artifact.
**Routed to:** Team Lead → Senior, Manager (informational; no decision requested).

---

## §1. What changed

On 2026-06-14 (commit `535421a` on `origin/main`, with sealed-tree-revert follow-up at `18c357d`), the directory `papers/paper-a-before-retention/` was renamed to `papers/paper4-before-retention/` for naming-convention consistency with the existing `papers/paper1-*`, `paper2-*`, `paper3-*` slugs. The rename was a `git mv` (preserves history for every file in the tree). All 38 files inside the bundle moved with it byte-for-byte.

Live-facing references updated in the same commit: `README.md`, `STATUS.md`, `REVIEW.md`, `_meta/INDEX.md`, `governance/epochs/2026-06-11_lane-1a-prime/INDEX.md`.

## §2. Why this note exists

Two CS-PASSed currently-authoritative governance documents were filed *before* the rename and still reference the old path:

- `tier-1-instrument/organization/structure/v0.4.md` (the current accepted whole-repo structure spec).
- `tier-1-instrument/organization/inventory/v0.2.md` (the current inventory reconciliation against v0.4).

Per the program's **supersede-don't-rewrite** discipline, those frozen versions are not edited in place. Their references to `papers/paper-a-before-retention/` were correct at acceptance time and remain correct as a record of the as-filed state. This note is the forward-reference that resolves the path drift without modifying either spec.

(A separate ~13 files in `tier-1-instrument/organization/structure/{,verifications/,manager-directions/}` for v0.1–v0.3, `inventory/v0.1.md`, `move/v0.1.md`, `move/verifications/v0.1.md`, and two CS verifications under `papers/paper4-before-retention/revisions/verifications/` and `finding-tracks/.../verifications/` also reference the old path. Those are correctly-historical — they describe the state at their respective filing dates. This note covers them by reference too.)

## §3. The forward-reference rule (binding)

**Read every `papers/paper-a-before-retention/...` path reference in any pre-2026-06-14-rename document as `papers/paper4-before-retention/...`** when resolving the path on disk. The contents and tree structure under the new directory are byte-identical to what was filed under the old name; only the parent directory name changed.

Applies to (non-exhaustive):

| Document | Status | Path reference still says |
|---|---|---|
| `tier-1-instrument/organization/structure/v0.4.md` | current accepted structure | `papers/paper-a-before-retention/` |
| `tier-1-instrument/organization/inventory/v0.2.md` | current inventory PASS | `papers/paper-a-before-retention/` |
| `tier-1-instrument/organization/structure/v0.1.md`–`v0.3.md` | superseded | `papers/paper-a-before-retention/` |
| `tier-1-instrument/organization/structure/verifications/v0.1.md`–`v0.4.md` | filed as-PASSed | `papers/paper-a-before-retention/` |
| `tier-1-instrument/organization/structure/manager-directions/v0.1.md`–`v0.3.md` | filed verbatim | `papers/paper-a-before-retention/` |
| `tier-1-instrument/organization/inventory/v0.1.md` | superseded HOLD | `papers/paper-a-before-retention/` |
| `tier-1-instrument/organization/move/v0.1.md` | execution complete | `papers/paper-a-before-retention/` |
| `tier-1-instrument/organization/move/verifications/v0.1.md` | filed as-PASSed | `papers/paper-a-before-retention/` |
| `papers/paper4-before-retention/revisions/verifications/CS-PAPER-A-GITHUB-BUNDLE-SWEEP-AND-VERIFICATION-v0.1.md` | filed as-PASSed | `papers/05_paper-a-before-retention/` (original pre-move) |
| `finding-tracks/cal-q-format-sensitive-abstention/verifications/CS-CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1-VERIFICATION-v0.1.md` | filed as-PASSed | `papers/paper-a-before-retention/` |

## §4. What this note does NOT do

- Does not modify any spec or verification.
- Does not retroactively edit the as-filed text of v0.4, inventory v0.2, or any other document.
- Does not change any sha256: the bundle's contents are byte-identical to what was filed under the old name; only the parent directory name changed.
- Does not commit the program to renaming "Paper A" → "Paper 4" in prose. The directory slug is `paper4-` for naming-convention consistency with `paper1/2/3-`; whether the program's prose identifier for the paper changes from "Paper A" to "Paper 4" is a separate editorial decision (Senior flagged this as worth a nod; CS is surfacing it to Manager).

## §5. What a future structure-spec version (v0.5) would do

If/when a structure-spec v0.5 is directed, it would supersede this note by reflecting the rename in §3 of the spec itself. Until then, this note is the standing forward-reference.

## §6. Sealed-bytes posture

Sealed bytes UNCHANGED (≈79th survival check):

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`)
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`)
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`)
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`)

— CS Engineer, 2026-06-14
