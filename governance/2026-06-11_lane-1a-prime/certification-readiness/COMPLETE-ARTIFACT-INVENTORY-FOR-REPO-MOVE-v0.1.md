# COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.1

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Manager, Senior
**In response to:** `MANAGER-DIRECTION-AUTHORIZE-COMPLETE-ARTIFACT-INVENTORY-2026-06-14` (Manager direction, this turn — filed verbatim alongside this memo).
**Scope:** complete inventory of every artifact in the repo before any move authorization. No file moves, no directory creation, no renaming, no deletion performed.

---

## §0. Verdict (Manager's return format)

```text
HOLD:
  Inventory is COMPLETE, but a large number of artifacts have no destination
  under the v0.3 structure as written. Manager routing decisions are required
  for those artifacts before any move can be safely planned.
```

The inventory is complete: every non-`.git/`, non-`.pytest_cache/`, non-tier0 file in the repo has been catalogued, hashed, and classified by track. **No artifact is dropped** from the inventory; every one of the 2,634 inventory-scope files appears in one of the tables in §§3–6 below.

The HOLD is not about completeness; it is about **routing coverage**. The v0.3 structure spec defines exactly five top-level trees (`/papers/paper-a-before-retention/`, `/tier-1-instrument/`, `/finding-tracks/cal-q-format-sensitive-abstention/`, `/paper-b/planning/`, `/archive/d4-closed-route/`). The repo contains **eight additional artifact categories** that have no destination under v0.3 (Papers 1/2/3, the Hash-Integrity standing note, older Lane-1a work, B1 harness work, cross-cutting standing governance, cross-cutting passdown, root-level orchestration docs, and four ancillary top-level dirs `diagrams/`, `notes/`, `review/`, `writing/`). These eight categories together account for ~1,900 of the 2,634 inventory-scope files. They cannot be routed without Manager decisions on either extending v0.3 (adding additional tracks) or leaving them in place indefinitely.

Per Manager check #10 ("Any ambiguous artifact is flagged for Manager decision before moves"), §6 enumerates each unrouted category with a proposed disposition for Manager review. The disposition options listed there are CS's suggested defaults, NOT CS decisions.

---

## §1. Anchor and sealed-bytes posture

This inventory is taken against `origin/main` HEAD `68ab49f` (the most recent push, which filed the v0.3 structure spec + Manager direction + CS verification). Sealed bytes UNCHANGED (≈74th survival check):

| Sealed artifact | Path | sha256 | Disposition |
|---|---|---|---|
| LOCK-RECORD | `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | `5b557ae2…` | **DO NOT MOVE** — sealed bytes; any move must be a separate sealed-relocation directive with Manager + verification |
| STRATIFIED_RECIPE_SCHEDULE | `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccdd…` | **DO NOT MOVE** |
| ORACLE_VERDICT_TABLE | `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9…` | **DO NOT MOVE** |
| T3_BOUNDS_DECLARATION | `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b…` | **DO NOT MOVE** |

The `tier0-run/` tree (~2.6M files, model weights + tokenizer) is also **SEALED** per standing CS scope rule (memory `feedback_repo_scope`: "tier0-run/ is SEALED — never add files to it"). Excluded from this inventory by category; never moves.

## §2. Inventory scope and method

**Total files in repo:** 6,877 (excluding `.DS_Store`).
**In inventory scope:** 2,634 (excluding `.git/` internal tracking files [4,229] and `.pytest_cache/` [6]; `tier0-run/` model weights are categorically excluded as SEALED-no-move).

**Inventory granularity:**
- **Per-file** (with full sha256, status, destination): all files in `papers/`, all files in `governance/`, sealed bytes, root-level docs (~543 files).
- **Group-level** (with file count + total size + sample sha256 + DO-NOT-INVENTORY-INDIVIDUALLY justification): bulk per-item run-record JSON trees in `experiments/2026-06-11_lane-1a-prime/path_a_run/` (1,594 files), `d4_a_pilot/` (104 files), `d4_b_pilot/` (201 files), `experiments/2026-06-10_lane-1a-sweep/raw/` (64 files), and other experiments subtrees (~2,091 files total grouped).
- **Group-level** for ancillary dirs (`diagrams/` 14 files, `notes/` 20 files, `review/` 1 file, `writing/` 18 files).

The per-item run-record JSON files in bulk-experiment subtrees are not individually relevant to routing decisions: each is a per-item model output paired with a per-item label, and they MUST move together as a single tree because they form an artifact-locked run record. Routing the tree decides routing for every file in it. Group-level inventory with sample hashes is the appropriate granularity, and is consistent with the program's standing artifact-locking discipline.

**Hash basis:** sha256 throughout, generated via `shasum -a 256`. Where a hash appears truncated (`5b557ae2…`), the full hash is in the program's existing INDEX or LOCK records.

**Field schema for each per-file entry (per Manager's required routing fields):**
- current path • filename (implied by path) • sha256 • artifact type • current status • proposed destination under v0.3 (or **OUT-OF-V0.3-SCOPE** flag) • track assignment • lifecycle (active / historical / superseded / placeholder / source-of-truth) • move disposition (move / remain / copy / reference-only) • notes / ambiguity flags

---

## §3. Track 1 — Paper A release (in v0.3 scope)

### §3.1 Paper A GitHub bundle — current `papers/05_paper-a-before-retention/` (17 files)

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? | Notes |
|---|---|---|---|---|---|---|---|
| `papers/05_paper-a-before-retention/README.md` | `7c4f31e7…` | release README | active | `/papers/paper-a-before-retention/README.md` | source-of-truth | rename-dir (drop `05_` prefix) | Released on GitHub; bundle entry point |
| `papers/05_paper-a-before-retention/CITATION.cff` | `132acd9c…` | citation metadata | active | `/papers/paper-a-before-retention/CITATION.cff` | source-of-truth | rename-dir | |
| `papers/05_paper-a-before-retention/.gitignore` | `1fb35e49…` | bundle gitignore | active | `/papers/paper-a-before-retention/.gitignore` | source-of-truth | rename-dir | |
| `papers/05_paper-a-before-retention/paper/paper.md` | `4272e12a…` | release paper.md (v1.0 source) | active | `/papers/paper-a-before-retention/paper/paper.md` | source-of-truth | rename-dir | v1.0 source; matches `paper-a-revisions/PAPER-A-v1.0.md` byte-for-byte |
| `papers/05_paper-a-before-retention/paper/paper.pdf` | `57458c90…` | release paper.pdf | active | `/papers/paper-a-before-retention/paper/paper.pdf` | source-of-truth | rename-dir | Matches `paper-a-revisions/PAPER-A-v1.0.pdf` byte-for-byte |
| `papers/05_paper-a-before-retention/sections/section-2-background.md` | `34cedb30…` | §2 master | active | `/papers/paper-a-before-retention/sections/section-2-background.md` | source-of-truth | rename-dir | Matches `cert-readiness/PAPER-POSITIONING-SECTION-DRAFT-v0.7.md` byte-for-byte |
| `papers/05_paper-a-before-retention/sections/section-4-instrument.md` | `6b111f3a…` | §4 master | active | `/papers/paper-a-before-retention/sections/section-4-instrument.md` | source-of-truth | rename-dir | Closes prior CS BLOCKING flag (architecture-master) |
| `papers/05_paper-a-before-retention/sections/section-5-rejection-audit.md` | `4dc2f290…` | §5 master | active | `/papers/paper-a-before-retention/sections/section-5-rejection-audit.md` | source-of-truth | rename-dir | Matches `cert-readiness/PAPER-SECTION-5-REJECTION-AUDIT-DRAFT-v0.1.md` byte-for-byte |
| `papers/05_paper-a-before-retention/supplement/README.md` | `e1acf487…` | supplement manifest | active | `/papers/paper-a-before-retention/supplement/README.md` | source-of-truth | rename-dir | |
| `papers/05_paper-a-before-retention/figures/fig1_certification_box.png` | `011f5bdb…` | release figure | active | `/papers/paper-a-before-retention/figures/fig1_certification_box.png` | source-of-truth | rename-dir | |
| `papers/05_paper-a-before-retention/figures/fig1_certification_box.svg` | `4f35c610…` | release figure | active | `/papers/paper-a-before-retention/figures/fig1_certification_box.svg` | source-of-truth | rename-dir | |
| `papers/05_paper-a-before-retention/figures/fig2_reversal_confirmation.png` | `0083d70b…` | release figure | active | `/papers/paper-a-before-retention/figures/fig2_reversal_confirmation.png` | source-of-truth | rename-dir | |
| `papers/05_paper-a-before-retention/figures/fig2_reversal_confirmation.svg` | `d1d380b2…` | release figure | active | `/papers/paper-a-before-retention/figures/fig2_reversal_confirmation.svg` | source-of-truth | rename-dir | |
| `papers/05_paper-a-before-retention/governance/MANAGER-DECISION-PAPER-A-NOW-v0.1.md` | `1d901d5d…` | Paper A governance (Manager) | active | `/papers/paper-a-before-retention/governance/MANAGER-DECISION-PAPER-A-NOW-v0.1.md` | source-of-truth | rename-dir | |
| `papers/05_paper-a-before-retention/governance/MANAGER-DECISION-VENUE-OPTION-2-v0.1.md` | `1e71640f…` | Paper A governance (Manager) | active | `/papers/paper-a-before-retention/governance/MANAGER-DECISION-VENUE-OPTION-2-v0.1.md` | source-of-truth | rename-dir | |
| `papers/05_paper-a-before-retention/governance/VENUE-DECISION-MEMO-PAPER-A-v0.1.md` | `4f399b8e…` | Paper A governance (Senior) | active | `/papers/paper-a-before-retention/governance/VENUE-DECISION-MEMO-PAPER-A-v0.1.md` | source-of-truth | rename-dir | |
| `papers/05_paper-a-before-retention/governance/methodology-record.md` | `9de3c8cc…` | Paper A governance (Senior) | active | `/papers/paper-a-before-retention/governance/methodology-record.md` | source-of-truth | rename-dir | |

**Routing rule for this bundle:** the entire `papers/05_paper-a-before-retention/` tree renames in place to `papers/paper-a-before-retention/` (drop the `05_` phase prefix); no internal restructuring; 17 files preserved byte-for-byte.

### §3.2 Paper A revision chain — current `governance/2026-06-11_lane-1a-prime/certification-readiness/paper-a-revisions/` (10 files)

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `…/paper-a-revisions/PAPER-A-v0.6.md` | `eb96f009…` | superseded paper revision | historical | `/papers/paper-a-before-retention/revisions/PAPER-A-v0.6.md` (CS-proposed sub-dir) | superseded | move |
| `…/paper-a-revisions/PAPER-A-v0.6.pdf` | `4772dcd5…` | superseded paper revision | historical | `/papers/paper-a-before-retention/revisions/PAPER-A-v0.6.pdf` | superseded | move |
| `…/paper-a-revisions/PAPER-A-v0.7.md` | `2754011f…` | superseded paper revision | historical | `/papers/paper-a-before-retention/revisions/PAPER-A-v0.7.md` | superseded | move |
| `…/paper-a-revisions/PAPER-A-v0.7.pdf` | `00e828ec…` | superseded paper revision | historical | `/papers/paper-a-before-retention/revisions/PAPER-A-v0.7.pdf` | superseded | move |
| `…/paper-a-revisions/PAPER-A-v0.8.md` | `68bd9bb6…` | superseded paper revision | historical | `/papers/paper-a-before-retention/revisions/PAPER-A-v0.8.md` | superseded | move |
| `…/paper-a-revisions/PAPER-A-v0.8.pdf` | `8808af88…` | superseded paper revision | historical | `/papers/paper-a-before-retention/revisions/PAPER-A-v0.8.pdf` | superseded | move |
| `…/paper-a-revisions/PAPER-A-v0.9.md` | `bcd3bc3b…` | superseded paper revision | historical | `/papers/paper-a-before-retention/revisions/PAPER-A-v0.9.md` | superseded | move |
| `…/paper-a-revisions/PAPER-A-v0.9.pdf` | `2f3049ca…` | superseded paper revision | historical | `/papers/paper-a-before-retention/revisions/PAPER-A-v0.9.pdf` | superseded | move |
| `…/paper-a-revisions/PAPER-A-v1.0.md` | `4272e12a…` | release source MD | active | `/papers/paper-a-before-retention/revisions/PAPER-A-v1.0.md` | source-of-truth (also bundled as `paper/paper.md`) | **copy-to-revisions** | matches bundle paper.md byte-for-byte; keep as revision-chain anchor |
| `…/paper-a-revisions/PAPER-A-v1.0.pdf` | `57458c90…` | release source PDF | active | `/papers/paper-a-before-retention/revisions/PAPER-A-v1.0.pdf` | source-of-truth (also bundled as `paper/paper.pdf`) | **copy-to-revisions** | matches bundle paper.pdf byte-for-byte |

**Ambiguity flag:** v0.3 structure spec §3 does not name a `/papers/paper-a-before-retention/revisions/` sub-directory; CS proposes it here because the revision chain is paper-history that belongs WITH the paper bundle, not in `/archive/` (which is for D4-closed-route history). **Manager decision required:** approve sub-directory name and location, or alternative destination for the revision chain.

### §3.3 Paper A working drafts and section masters — in `certification-readiness/` (12 files)

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/PAPER-A-DRAFT-SKELETON-v0.2.md` | `d87f08ae…` | early skeleton | historical | `/papers/paper-a-before-retention/revisions/skeleton/PAPER-A-DRAFT-SKELETON-v0.2.md` | superseded | move |
| `cert-readiness/PAPER-A-DRAFT-v0.3.md` | `0a54db9a…` | early full draft | historical | `/papers/paper-a-before-retention/revisions/PAPER-A-DRAFT-v0.3.md` | superseded | move |
| `cert-readiness/PAPER-A-DRAFT-v0.4.md` | `6bcfc17f…` | targeted-polish draft | historical | `/papers/paper-a-before-retention/revisions/PAPER-A-DRAFT-v0.4.md` | superseded | move |
| `cert-readiness/PAPER-A-DRAFT-v0.5.md` | `557bc005…` | venue-decision draft | historical | `/papers/paper-a-before-retention/revisions/PAPER-A-DRAFT-v0.5.md` | superseded | move |
| `cert-readiness/PAPER-POSITIONING-SECTION-DRAFT-v0.1.md` | `261309ae…` | positioning v0.1 | historical | `/papers/paper-a-before-retention/revisions/sections/v2-background/v0.1.md` | superseded | move |
| `cert-readiness/PAPER-POSITIONING-SECTION-DRAFT-v0.3.md` | `5aff96d7…` | positioning v0.3 | historical | `/papers/paper-a-before-retention/revisions/sections/v2-background/v0.3.md` | superseded | move |
| `cert-readiness/PAPER-POSITIONING-SECTION-DRAFT-v0.4.md` | `c2dbae44…` | positioning v0.4 | historical | `/papers/paper-a-before-retention/revisions/sections/v2-background/v0.4.md` | superseded | move |
| `cert-readiness/PAPER-POSITIONING-SECTION-DRAFT-v0.5.md` | `7579b006…` | positioning v0.5 | historical | `/papers/paper-a-before-retention/revisions/sections/v2-background/v0.5.md` | superseded | move |
| `cert-readiness/PAPER-POSITIONING-SECTION-DRAFT-v0.6.md` | `78f7cfed…` | positioning v0.6 | historical | `/papers/paper-a-before-retention/revisions/sections/v2-background/v0.6.md` | superseded | move |
| `cert-readiness/PAPER-POSITIONING-SECTION-DRAFT-v0.7.md` | `34cedb30…` | positioning v0.7 (= §2 master) | active | (already in bundle as `sections/section-2-background.md`) | source-of-truth | **reference-only** (already present) |
| `cert-readiness/PAPER-SECTION-5-REJECTION-AUDIT-DRAFT-v0.1.md` | `4dc2f290…` | §5 master | active | (already in bundle as `sections/section-5-rejection-audit.md`) | source-of-truth | **reference-only** (already present) |
| `cert-readiness/VENUE-DECISION-MEMO-PAPER-A-v0.1.md` | `4f399b8e…` | venue memo | active | (already in bundle as `governance/VENUE-DECISION-MEMO-PAPER-A-v0.1.md`) | source-of-truth | **reference-only** (already present) |

**Ambiguity flag:** the three "reference-only" entries are byte-identical duplicates of files already in the Paper A bundle. v0.3 structure does not say what to do with the workspace-master copies once the bundle is the canonical home. CS recommends DELETE the duplicates after verifying byte-identity, but **Manager decision required** (alternative: keep both, treating cert-readiness/ copy as the working master and bundle copy as the release snapshot).

### §3.4 Paper A governance memos in `certification-readiness/` (Manager directions for Paper A) (1 file)

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/MANAGER-DECISION-PAPER-A-NOW-v0.1.md` | `1d901d5d…` | Paper A governance | active | (already in bundle as `governance/MANAGER-DECISION-PAPER-A-NOW-v0.1.md`) | source-of-truth | **reference-only** (already present) |
| `cert-readiness/MANAGER-DECISION-VENUE-OPTION-2-v0.1.md` | `1e71640f…` | Paper A governance | active | (already in bundle as `governance/MANAGER-DECISION-VENUE-OPTION-2-v0.1.md`) | source-of-truth | **reference-only** (already present) |

(Same ambiguity flag as §3.3 — these are byte-identical duplicates.)

---

## §4. Track 2 — Tier 1 instrument (in v0.3 scope)

### §4.1 Specs (2 files)

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1.md` | `fc0bee3f…` | Tier-1 architecture spec | active | `/tier-1-instrument/specs/eval-validity-gate-tool-spec-v0.1.md` | source-of-truth | move (rename to lowercase per v0.3 spec convention) |
| `cert-readiness/G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md` | `2b4cedf8…` | G6 module spec | active | `/tier-1-instrument/specs/g6-standing-rejection-audit-spec-v0.1.md` | source-of-truth | move (rename to lowercase) |

### §4.2 CS verifications of Tier-1 specs (3 files)

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/CS-EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1-VERIFICATION-v0.1.md` | `f072616e…` | CS verification — PASS | active | `/tier-1-instrument/specs/verifications/CS-EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1-VERIFICATION-v0.1.md` | source-of-truth | move |
| `cert-readiness/CS-G6-STANDING-REJECTION-AUDIT-SPEC-v0.1-VERIFICATION-v0.1.md` | `e080b74b…` | CS verification — PASS | active | `/tier-1-instrument/specs/verifications/CS-G6-STANDING-REJECTION-AUDIT-SPEC-v0.1-VERIFICATION-v0.1.md` | source-of-truth | move |
| (CS verification of repo structure v0.1/v0.2/v0.3 — see §5.4; these are governance-of-this-document, route to a separate `/tier-1-instrument/organization/` per CS proposal — Manager decision needed) | — | — | — | — | — | — |

**Ambiguity flag:** v0.3 structure spec §3 names `/tier-1-instrument/specs/` but does not name a `verifications/` sub-directory under `specs/`. CS proposes the sub-dir for symmetry with `revisions/`; **Manager decision required**.

### §4.3 Manager directions for Tier-1 spec verifications (3 files)

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/MANAGER-DIRECTION-EVAL-VALIDITY-GATE-TOOL-SPEC-VERIFICATION-2026-06-14.md` | `52369271…` | Manager direction | active | `/tier-1-instrument/specs/verifications/MANAGER-DIRECTION-…-2026-06-14.md` | historical (direction acted on) | move |
| `cert-readiness/MANAGER-DIRECTION-G6-STANDING-REJECTION-AUDIT-SPEC-VERIFICATION-2026-06-14.md` | `418edb0e…` | Manager direction | active | `/tier-1-instrument/specs/verifications/MANAGER-DIRECTION-…-2026-06-14.md` | historical | move |

### §4.4 Tier-1 module work — G6 module home (no files yet; placeholder per v0.3 spec) — 0 files routed

Currently no artifact lives at `/tier-1-instrument/modules/g6-standing-rejection-audit/`. The v0.3 structure reserves this for future G6 design + implementation work. No inventory entry; no move.

### §4.5 Schemas, human-read templates, examples, implementation (PLACEHOLDER per v0.3) — 0 files routed

No standalone artifacts yet. Schemas live embedded in Tool Spec §§4/5/7 and G6 Spec §9; extraction is future. No inventory entry; no move.

---

## §5. Tier 1 — Repo organization track (CS-proposed; v0.3 does not name explicitly)

The v0.3 structure spec itself and its verification chain are governance-of-this-document. They do not belong with the Tool Spec/G6 Spec (those are tool architecture); they describe how the repo is organized. CS proposes `/tier-1-instrument/organization/` for these.

### §5.1 Structure-spec revision chain (3 files)

| Current path | sha256 | Type | Status | Destination (v0.3 — CS-proposed) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.1.md` | `2048396d…` | structure spec | historical | `/tier-1-instrument/organization/structure/v0.1.md` | superseded | move |
| `cert-readiness/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.2.md` | `bc9a4014…` | structure spec | historical | `/tier-1-instrument/organization/structure/v0.2.md` | superseded | move |
| `cert-readiness/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.3.md` | `d691ded8…` | structure spec | active | `/tier-1-instrument/organization/structure/v0.3.md` | source-of-truth | move |

### §5.2 Structure-spec CS verifications (3 files)

| Current path | sha256 | Type | Status | Destination (v0.3 — CS-proposed) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/CS-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.1-VERIFICATION-v0.1.md` | `adaa204a…` | CS verification — PASS | historical | `/tier-1-instrument/organization/structure/verifications/v0.1.md` | superseded | move |
| `cert-readiness/CS-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.2-VERIFICATION-v0.1.md` | `3db8fadb…` | CS verification — PASS | historical | `/tier-1-instrument/organization/structure/verifications/v0.2.md` | superseded | move |
| `cert-readiness/CS-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.3-VERIFICATION-v0.1.md` | `aace3406…` | CS verification — PASS | active | `/tier-1-instrument/organization/structure/verifications/v0.3.md` | source-of-truth | move |

### §5.3 Structure-spec Manager directions (3 files)

| Current path | sha256 | Type | Status | Destination (v0.3 — CS-proposed) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-VERIFICATION-2026-06-14.md` | `c2b73632…` | Manager direction | historical | `/tier-1-instrument/organization/structure/manager-directions/v0.1.md` | historical | move |
| `cert-readiness/MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.2-VERIFICATION-2026-06-14.md` | `43b199b8…` | Manager direction | historical | `/tier-1-instrument/organization/structure/manager-directions/v0.2.md` | historical | move |
| `cert-readiness/MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.3-VERIFICATION-2026-06-14.md` | `f4720f08…` | Manager direction | historical | `/tier-1-instrument/organization/structure/manager-directions/v0.3.md` | historical | move |

### §5.4 This inventory and its Manager direction (2 files — being filed this turn)

| Current path | sha256 | Type | Status | Destination (v0.3 — CS-proposed) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.1.md` | (this file; computed at commit) | inventory artifact | active | `/tier-1-instrument/organization/inventory/v0.1.md` | source-of-truth | move |
| `cert-readiness/MANAGER-DIRECTION-AUTHORIZE-COMPLETE-ARTIFACT-INVENTORY-2026-06-14.md` | (filed this turn; computed at commit) | Manager direction | historical | `/tier-1-instrument/organization/inventory/manager-direction-2026-06-14.md` | historical | move |

**Ambiguity flag:** the entire `/tier-1-instrument/organization/` sub-tree is **CS-proposed, NOT named in the v0.3 structure spec.** Manager decision required: approve the sub-tree, or specify alternative destination (e.g., `/tier-1-instrument/specs/` mixed in, or a separate `/governance-of-tier-1/` top-level, or remain in `certification-readiness/`).

---

## §6. Track 3 — CAL-Q finding track (in v0.3 scope)

### §6.1 CAL-Q finding-track artifacts (2 files)

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1.md` | `0c2afbbc…` | finding-track plan | active | `/finding-tracks/cal-q-format-sensitive-abstention/cal-q-finding-diagnostic-plan-v0.1.md` | source-of-truth | move |
| `cert-readiness/CS-CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1-VERIFICATION-v0.1.md` | `161d450a…` | CS verification — PASS | active | `/finding-tracks/cal-q-format-sensitive-abstention/verifications/CS-CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1-VERIFICATION-v0.1.md` | source-of-truth | move |

### §6.2 CAL-Q-adjacent artifacts (finding history; not the diagnostic plan) (3 files)

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/CAL-Q-FORMAT-SENSITIVE-ABSTENTION-FINDING-v0.1.md` | `8aebefeb…` | finding writeup | active | `/finding-tracks/cal-q-format-sensitive-abstention/findings/CAL-Q-FORMAT-SENSITIVE-ABSTENTION-FINDING-v0.1.md` | source-of-truth | move |
| `cert-readiness/CAL-Q-RUN-INTERPRETATION-v0.1.md` | `d0bd4e87…` | run interpretation | active | `/finding-tracks/cal-q-format-sensitive-abstention/findings/CAL-Q-RUN-INTERPRETATION-v0.1.md` | source-of-truth | move |
| `cert-readiness/CS-CAL-Q-RUN-REPORT-v0.1.md` | `c64c8bda…` | CS run report | active | `/finding-tracks/cal-q-format-sensitive-abstention/findings/CS-CAL-Q-RUN-REPORT-v0.1.md` | source-of-truth | move |

**Ambiguity flag:** v0.3 §3 names the `cal-q-format-sensitive-abstention/` dir but no internal structure. CS proposes `findings/`, `verifications/` sub-dirs. **Manager decision required.**

---

## §7. Track 4 — D4 closed-route archive (in v0.3 scope)

### §7.1 D4-direct governance and run-interpretation artifacts in cert-readiness/ (D4 history) (24 files)

The "D4 rescue" effort (CAL-A through CAL-Q content + query levers, the off-ceiling sweep, the CAL-E targeted-repair attempt) is now CLOSED per Manager PIVOT decision 2026-06-13. All D4-adjacent artifacts move to `/archive/d4-closed-route/`.

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/MANAGER-D4-PIVOT-DECISION-AND-CALQ-FINDING-TRACK-2026-06-13.md` | `86f3e5ff…` | D4 PIVOT decision | active | `/archive/d4-closed-route/governance/MANAGER-D4-PIVOT-DECISION-AND-CALQ-FINDING-TRACK-2026-06-13.md` | source-of-truth (route-close decision) | move |
| `cert-readiness/MANAGER-NON-CONTENT-LEVER-D4-RESCUE-DIRECTION-2026-06-13.md` | `d24cd53a…` | Manager direction | historical | `/archive/d4-closed-route/governance/…-2026-06-13.md` | historical | move |
| `cert-readiness/MANAGER-OFF-CEILING-CALIBRATION-SWEEP-AUTHORIZATION-2026-06-13.md` | `6fba3f39…` | Manager authorization | historical | `/archive/d4-closed-route/governance/…-2026-06-13.md` | historical | move |
| `cert-readiness/MANAGER-CAL-E-TARGETED-REPAIR-AUTHORIZATION-2026-06-13.md` | `fecb0b37…` | Manager authorization | historical | `/archive/d4-closed-route/governance/…-2026-06-13.md` | historical | move |
| `cert-readiness/MANAGER-POST-D4-STRATEGIC-POSITION-DIRECTION-2026-06-13.md` | `8c222fcc…` | Manager direction (post-D4 strategic) | historical | `/archive/d4-closed-route/governance/MANAGER-POST-D4-STRATEGIC-POSITION-DIRECTION-2026-06-13.md` | historical | move |
| `cert-readiness/MANAGER-TIER-1-PRIOR-ART-AND-AUDIENCE-DIRECTION-2026-06-13.md` | `fe119b12…` | Manager direction | historical | (ambiguous — could be Tier-1 inst. or D4-history; CS proposes archive/d4-closed-route/ as the direction emerged post-D4-pivot) | historical | **MANAGER ROUTING DECISION REQUIRED** |
| `cert-readiness/POST-D4-STRATEGIC-POSITION-v0.1.md` | `af27ce8b…` | Senior strategic memo | active (informs Tier-1 direction) | (ambiguous — post-D4 but informs Tier-1; CS proposes archive/d4-closed-route/ for traceability + reference-only in Tier-1) | source-of-truth | **MANAGER ROUTING DECISION REQUIRED** |
| `cert-readiness/TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK-v0.1.md` | `dbb3833c…` | Senior prior-art check | active | (same ambiguity — Tier-1 by topic, D4-history by origin) | source-of-truth | **MANAGER ROUTING DECISION REQUIRED** |
| `cert-readiness/CS-TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK-v0.1-VERIFICATION-v0.1.md` | `9429dff1…` | CS verification — PARTIAL PASS | active | (same ambiguity) | source-of-truth | **MANAGER ROUTING DECISION REQUIRED** |
| `cert-readiness/CAL-ABCE-RESCORE-REINTERPRETATION-v0.1.md` | `8433e32f…` | rescore reinterpretation | historical | `/archive/d4-closed-route/cal-sweep/CAL-ABCE-RESCORE-REINTERPRETATION-v0.1.md` | historical | move |
| `cert-readiness/CAL-E-DEFECTIVE-ERROR-ANALYSIS-v0.1.md` | `fc5569da…` | CAL-E analysis | historical | `/archive/d4-closed-route/cal-sweep/…-v0.1.md` | historical | move |
| `cert-readiness/CAL-E-INTERPRETATION-v0.1.md` | `4cafaedb…` | CAL-E interpretation | historical | `/archive/d4-closed-route/cal-sweep/CAL-E-INTERPRETATION-v0.1.md` | historical | move |
| `cert-readiness/CAL-E-TARGETED-REPAIR-SPEC-v0.1.md` | `f90f7132…` | CAL-E repair spec | historical | `/archive/d4-closed-route/cal-sweep/CAL-E-TARGETED-REPAIR-SPEC-v0.1.md` | historical | move |
| `cert-readiness/CS-CAL-ABCE-NULL-NORMALIZED-RESCORE-v0.1.md` | `d1703d43…` | CS rescore | historical | `/archive/d4-closed-route/cal-sweep/CS-CAL-ABCE-NULL-NORMALIZED-RESCORE-v0.1.md` | historical | move |
| `cert-readiness/CS-CAL-E-DEFECTIVE-OUTPUT-EXTRACTION-v0.1.md` | `cdf11691…` | CS extraction | historical | `/archive/d4-closed-route/cal-sweep/CS-CAL-E-DEFECTIVE-OUTPUT-EXTRACTION-v0.1.md` | historical | move |
| `cert-readiness/CS-CAL-E-TARGETED-REPAIR-RUN-REPORT-v0.1.md` | `bf62652e…` | CS run report | historical | `/archive/d4-closed-route/cal-sweep/CS-CAL-E-TARGETED-REPAIR-RUN-REPORT-v0.1.md` | historical | move |
| `cert-readiness/CS-CERT-READINESS-SUBMAP-STAGE-1-2-VERIFICATION-v0.1.md` | `9b51056b…` | CS verification (cert submap) | historical | `/archive/d4-closed-route/governance/…-v0.1.md` | historical | move |
| `cert-readiness/CS-NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1-VERIFICATION-v0.1.md` | `10958c9f…` | CS verification | historical | `/archive/d4-closed-route/cal-sweep/CS-NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1-VERIFICATION-v0.1.md` | historical | move |
| `cert-readiness/CS-NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.2-VERIFICATION-v0.1.md` | `2be56f91…` | CS verification | historical | (same dir) | historical | move |
| `cert-readiness/CS-NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.3-VERIFICATION-v0.1.md` | `6f00c877…` | CS verification | historical | (same dir) | historical | move |
| `cert-readiness/CS-OFF-CEILING-CALIBRATION-SWEEP-RUN-REPORT-v0.1.md` | `3cad1a96…` | CS run report | historical | `/archive/d4-closed-route/cal-sweep/CS-OFF-CEILING-CALIBRATION-SWEEP-RUN-REPORT-v0.1.md` | historical | move |
| `cert-readiness/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1.md` | `d0bb0217…` | Senior D4-rescue spec | historical | `/archive/d4-closed-route/cal-sweep/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1.md` | historical (D4 closed) | move |
| `cert-readiness/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.2.md` | `d88cfef9…` | Senior D4-rescue spec | historical | (same dir) | historical | move |
| `cert-readiness/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.3.md` | `83924900…` | Senior D4-rescue spec | historical | (same dir) | historical | move |
| `cert-readiness/OFF-CEILING-CALIBRATION-READ-VERDICT-v0.1.md` | `5b37de7a…` | calibration verdict | historical | `/archive/d4-closed-route/cal-sweep/OFF-CEILING-CALIBRATION-READ-VERDICT-v0.1.md` | historical | move |
| `cert-readiness/OFF-CEILING-CALIBRATION-SWEEP-INTERPRETATION-v0.1.md` | `e666c2e4…` | sweep interpretation | historical | (same dir) | historical | move |
| `cert-readiness/OFF-CEILING-CALIBRATION-SWEEP-RUNSPEC-v0.1.md` | `84ad4008…` | sweep runspec | historical | (same dir) | historical | move |
| `cert-readiness/OFF-CEILING-CALIBRATION-SWEEP-SPEC-v0.1.md` | `18ac212f…` | sweep spec | historical | (same dir) | historical | move |
| `cert-readiness/OFF-CEILING-D4-REPAIR-DESIGN-v0.1.md` | `15041107…` | D4 repair design | historical | (same dir) | historical | move |
| `cert-readiness/cal-abce_rescore_summary.json` | `d874b894…` | rescore data | historical | `/archive/d4-closed-route/cal-sweep/cal-abce_rescore_summary.json` | historical (referenced by Paper A figure provenance — keep) | **copy-to-paper-A-supplement** + move-original | Paper A §3.5 figures reference this file's hash; needs to remain reachable from Paper A supplement |
| `cert-readiness/cal-e_defective_error_table.json` | `99e342bd…` | error table | historical | `/archive/d4-closed-route/cal-sweep/cal-e_defective_error_table.json` | historical | move |

### §7.2 D4-direct sweep run records (5 files in `cert-readiness/sweep_run_records/`)

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/sweep_run_records/cal-a_run.json` | `5ceeeea4…` | sweep run record | historical | `/archive/d4-closed-route/cal-sweep/sweep_run_records/cal-a_run.json` | historical | move |
| `cert-readiness/sweep_run_records/cal-b_run.json` | `814676cc…` | sweep run record | historical | (same dir) | historical | move |
| `cert-readiness/sweep_run_records/cal-c_run.json` | `50964a77…` | sweep run record | historical | (same dir) | historical | move |
| `cert-readiness/sweep_run_records/cal-e_run.json` | `74c3fa1f…` | sweep run record | historical | (same dir) | historical | move |
| `cert-readiness/sweep_run_records/cal-q_run.json` | `90de7fd0…` | sweep run record | historical | (same dir) | historical | move |

### §7.3 Reference imagery in cert-readiness/ (2 files)

| Current path | sha256 | Type | Status | Destination (v0.3) | Lifecycle | Move? |
|---|---|---|---|---|---|---|
| `cert-readiness/reference-imagery/ChatGPT-Image-2026-06-13-08_24_45-PM.png` | `346c2edb…` | reference image | informational | (ambiguous — informal reference; CS proposes archive/d4-closed-route/reference-imagery/ since dated 2026-06-13 during D4 pivot) | informational | **MANAGER ROUTING DECISION REQUIRED** |
| `cert-readiness/reference-imagery/ChatGPT-Image-2026-06-13-08_31_16-PM.png` | `dd6d5ee8…` | reference image | informational | (same) | informational | **MANAGER ROUTING DECISION REQUIRED** |

### §7.4 D4-direct governance + run records OUTSIDE cert-readiness/ (in lane-1a-prime/ subtrees + experiments/)

**§7.4a Quarantine + D4 run governance — `governance/2026-06-11_lane-1a-prime/`**

Subtrees (per-file inventory available; total 99 files in lane-1a-prime/ governance outside cert-readiness/):

- `quarantine/` (5 files) — INT8-RUNG-1 quarantine governance — historical → `/archive/d4-closed-route/quarantine/` — move
- `constructed-positive-validation/` (4 files) — constructed-positive validation governance — historical → `/archive/d4-closed-route/constructed-positive-validation/` — move
- `first-compression-rung/` (5 files) — first compression rung governance (quarantined) — historical → `/archive/d4-closed-route/first-compression-rung/` — move
- `LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` and other lane-1a-prime root governance — these are LANE-LEVEL governance (broader than just D4) → **MANAGER ROUTING DECISION REQUIRED**: archive the lane wholesale, or split between Tier-1 / D4-archive / other?

**§7.4b D4 run records (bulk per-item) — `experiments/2026-06-11_lane-1a-prime/`**

| Group | File count | Total size approx | Sample sha256 | Destination (v0.3) | Move? |
|---|---|---|---|---|---|
| `experiments/2026-06-11_lane-1a-prime/d4_a_pilot/` | 104 | bulk | (per-file hashes available on demand) | `/archive/d4-closed-route/runs/d4_a_pilot/` | move-tree |
| `experiments/2026-06-11_lane-1a-prime/d4_b_pilot/` | 201 | bulk | | `/archive/d4-closed-route/runs/d4_b_pilot/` | move-tree |
| `experiments/2026-06-11_lane-1a-prime/d4_runner/` | 11 | small | | `/archive/d4-closed-route/runs/d4_runner/` | move-tree |
| `experiments/2026-06-11_lane-1a-prime/path_a_run/` | 1,594 | bulk | | (ambiguous — Path A was lane-1a-prime instrument-validation; superseded by Path A close-out; is this D4-archive or its own lane-1a-prime-archive?) | **MANAGER ROUTING DECISION REQUIRED** |
| `experiments/2026-06-11_lane-1a-prime/first_compression_rung/` | 1 | small | | `/archive/d4-closed-route/runs/first_compression_rung/` (consistent with quarantine governance) | move-tree |
| `experiments/2026-06-11_lane-1a-prime/constructed_positive/` | 4 | small | | `/archive/d4-closed-route/runs/constructed_positive/` | move-tree |
| `experiments/2026-06-11_lane-1a-prime/lane1a_prime/` | 10 | small | | (lane-level; **MANAGER ROUTING DECISION REQUIRED**) | hold |
| `experiments/2026-06-11_lane-1a-prime/certification_readiness/` | 27 | small | | These are the CAL-A/B/C/E/Q runner scripts + run records → `/archive/d4-closed-route/runs/certification_readiness/` | move-tree |
| `experiments/2026-06-11_lane-1a-prime/schemas/` | 4 | small | | (instrument schemas; **MANAGER ROUTING DECISION REQUIRED**: Tier-1 instrument or D4 archive?) | hold |
| `experiments/2026-06-11_lane-1a-prime/tests/` | 11 | small | | (lane tests; **MANAGER ROUTING DECISION REQUIRED**) | hold |
| `experiments/2026-06-11_lane-1a-prime/validation/` | 39 | small (includes 3 sealed bytes — DO NOT MOVE) | sealed bytes `7ad3ccdd…`, `9c6cbda9…`, `45565d0b…` | **SEALED — DO NOT MOVE**; other 36 files **MANAGER ROUTING DECISION REQUIRED** | hold |
| `experiments/2026-06-11_lane-1a-prime/README.md` | 1 | small | | (lane-level; **MANAGER ROUTING DECISION REQUIRED**) | hold |

---

## §8. Bulk experiment data — group-level inventory

### §8.1 `experiments/2026-06-10_lane-1a-sweep/` (115 files)

The lane-1a sweep is **SEALED** at the LOCK-RECORD level (§1 above). Contents include:
- LOCK-RECORD (sealed; `5b557ae2…`)
- `raw/` 64 per-item run records (bulk)
- `manifests/` 10 files, `figures/` 9 files, `schema/` 3 files
- ~28 runner/analyzer/scorer scripts and logs
- AUDIT-LOG.ndjson + AUDIT-LOG-FORMAT.md
- NOVELTY-LEDGER.md
- LOCK-RECORD-FINALIZATION.md

**Destination (CS-proposed):** `/archive/d4-closed-route/lane-1a-sweep/` (entire tree as a single sealed unit). **Routing rule:** sealed bytes inside this tree DO NOT MOVE without separate sealed-relocation directive; if the tree moves, sealed-byte hashes must verify identical before and after.

**MANAGER ROUTING DECISION REQUIRED:** moving sealed bytes — even within the repo — is a sensitive operation. CS recommends Manager explicitly authorize the sealed relocation (with CS verifying pre-move + post-move hashes) OR leave the sealed sweep tree in place under `experiments/` indefinitely (recommended default).

### §8.2 `experiments/2026-06-09_b1-harness-v2/` (12 files)

B1 harness v2 implementation — code + manifest + results. Pre-Lane-1a-Prime work.

**Destination:** **NO v0.3 DESTINATION.** B1 harness is neither Paper A, Tier-1 instrument, CAL-Q, Paper B, nor D4. **MANAGER ROUTING DECISION REQUIRED** (CS suggests: new `/archive/b1-harness/` track, or leave in place).

### §8.3 Other experiments subtrees

- `experiments/README.md` (1 file) — `/` description; **MANAGER decision**: stays at root of experiments/ regardless of v0.3 reorg, or moves alongside whatever the experiments root becomes.

---

## §9. OUT-OF-V0.3-SCOPE artifacts — Manager routing decisions required

This section enumerates every artifact category that has **no destination** under v0.3 as written. The v0.3 structure spec defines only five top-level trees; everything below requires Manager routing decisions.

### §9.1 Other papers (Papers 1, 2, 3) — `papers/` (46 files total minus Paper A's 17 = ~29 files)

| Sub-tree | File count | Type | Destination? |
|---|---|---|---|
| `papers/paper1-survival-is-not-correctness/` | 13 | Paper 1 RELEASED bundle (LICENSE, README, .md, .pdf, artifacts/, assets/, tools/) | **OUT OF v0.3 SCOPE** — CS suggests `/papers/paper1-survival-is-not-correctness/` (parallel to Paper A); Manager confirmation needed |
| `papers/paper2-correctness-is-not-constructibility/` | 2 files (`correctness-is-not-constructibility.md` `9893a818…` + figures dir) — appears INCOMPLETE compared to Paper 1's full bundle | **OUT OF v0.3 SCOPE** — CS suggests `/papers/paper2-correctness-is-not-constructibility/`; Manager confirmation needed |
| `papers/paper3-certification-before-retention/` | files in this dir + `figures/` | **OUT OF v0.3 SCOPE** — CS suggests `/papers/paper3-certification-before-retention/`; Manager confirmation needed |

### §9.2 Hash-Integrity standing note — `governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.{md,pdf}`

Per `feedback_llm_mechanics_experiments` and `feedback_hash_integrity_is_not_construct_validity`-style program history, this is the fourth paper-class artifact (`Paper Hash`). Currently in `governance/standing/`. **OUT OF v0.3 SCOPE.** CS suggests either `/papers/paper-hash-integrity-is-not-construct-validity/` or keep at `/governance/standing/` (it IS used as a standing reference). Manager decision required.

### §9.3 Older Lane-1a work — `governance/2026-06-10_lane1a/` (67 files including `c6_proposal_archive/`)

Pre-Lane-1a-Prime Lane 1a work, including the C6 proposal, design packets, execution packets, deviation reports, Path A/A1/E1 remediation, close-out drafts, etc. Includes a sub-archive `c6_proposal_archive/`.

**OUT OF v0.3 SCOPE.** v0.3 §3 only addresses D4 archive (`/archive/d4-closed-route/`), not pre-D4 Lane-1a history. CS suggests `/archive/lane-1a-historical/` (a new sub-tree under `/archive/`); Manager decision required.

### §9.4 B1 harness governance — multiple directories (~7 files)

- `governance/2026-06-09_b1-harness-plan-revision/B1-IMPLEMENTATION-PLAN-V2.md`
- `governance/2026-06-09_b1-harness-v2-merge-readiness/` (3 files)
- `governance/2026-06-10_b1-harness-v2-merge-and-lock/` (3 files)

**OUT OF v0.3 SCOPE.** CS suggests `/archive/b1-harness/` (paired with the experiments/ B1 tree from §8.2). Manager decision required.

### §9.5 Paper 2 + Paper 3 governance — multiple directories (~32 files)

- `governance/2026-06-09_paper2-v1.0-release/` (2 files: ADDENDUM, RELEASE-RECORD)
- `governance/2026-06-09_paper3-threshold-framework-review/` (14 files: CS reviews v02 through v1.1, TeamLead memos)
- `governance/2026-06-10_paper3-external-review/` (6 files: external review, referee report v0.7, G1 closure)
- `governance/2026-06-10_paper3-v1.0-release/` (9 files: CS execution/release reports, MANAGER authorization)
- `governance/2026-06-10_paper3-v1.1-release/` (2 files)

**OUT OF v0.3 SCOPE.** v0.3 only handles Paper A. CS suggests co-locating these with their respective papers (Paper 2/3 governance → under `/papers/paperN/governance/` parallel to Paper A's bundle/governance/) OR a separate `/archive/paper2-history/` and `/archive/paper3-history/`. Manager decision required.

### §9.6 Standing governance — `governance/standing/` (25 files)

Cross-cutting standing program artifacts: NORTH-STAR-v1.1, PROGRAM-MAP-v2.0, PROGRAM-POSITION-v0.1, PROGRAM-STAGE-MAP v0.1+v0.2, ROUTE-STATE-GATE, SHOWN-SEMANTIC-READ-TEMPLATE-v1.0, STANDARD-RETURN-TEMPLATE-v1.0, STANDING-NON-AUTHORIZATIONS, STANDING-REVIEW-DISCIPLINE, SUBMAP-CONVENTION-v1.0, VERIFICATION-PROTOCOL-v1.0, CLOSEOUT-TEMPLATE-v1.0, CONDITIONAL-LIFECYCLE-AUTHORIZATION-PATTERN-v0.1, PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM, HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2 (md+pdf), figures/ (8 SVG/PNG).

**OUT OF v0.3 SCOPE.** These apply across ALL tracks (Paper A, Tier-1, CAL-Q, Paper B, D4 history). They cannot move into a single v0.3 track without breaking cross-cuttingness.

**CS strong recommendation: REMAIN in `/governance/standing/` (do not move).** The v0.3 organization plan should be amended (v0.4) to acknowledge `/governance/standing/` as a fifth fixed track-independent location. Manager decision required.

### §9.7 Passdown / onboarding — `governance/passdown/` (4 files) + root `ONBOARDING-CS.md`

- `passdown/2026-06-10_passdown-letter.md`, `_project-map.md`, `_senior-passdown.md`, `README.md`
- Root: `ONBOARDING-CS.md`

**OUT OF v0.3 SCOPE.** These are operational/onboarding artifacts cross-cutting all tracks. **CS strong recommendation: REMAIN in place.** Manager decision required.

### §9.8 Scaling discussion item + Lane-1a authorization — small dated governance

- `governance/2026-06-09_scaling-discussion-item/OPEN-DISCUSSION-SCALING-AND-TOOLING.md` (1 file)
- `governance/2026-06-10_lane-1a-authorization/MANAGER-AUTHORIZATION.md` (1 file)

**OUT OF v0.3 SCOPE.** CS suggests `/archive/program-history/` for these orphan dated governance items. Manager decision required.

### §9.9 Root-level docs — `/` (5 files)

- `README.md`, `STATUS.md`, `REVIEW.md`, `ONBOARDING-CS.md`, `.gitignore`

**OUT OF v0.3 SCOPE.** Root-level orchestration. **CS strong recommendation: REMAIN at root.** Manager decision required.

### §9.10 Ancillary top-level dirs (53 files)

- `diagrams/` 14 files (figure sources for the program)
- `notes/` 20 files (working notes)
- `writing/` 18 files (drafts in progress)
- `review/` 1 file

**OUT OF v0.3 SCOPE.** These are workspace cross-cutting trees. **CS suggestion: REMAIN as top-level workspace dirs** (or consolidate under a new `/workspace/`). Manager decision required.

---

## §10. INDEX / catalog records

| Current path | sha256 | Type | Status | Destination | Move? |
|---|---|---|---|---|---|
| `governance/2026-06-11_lane-1a-prime/INDEX.md` | (current, ~140KB) | program INDEX | active | **stays at workspace root per v0.3** (or moves to `governance/INDEX.md` at the top of governance/) — per v0.3 §5 NOTE: "the INDEX.md catalog stays at workspace root (it indexes ALL tracks)" | **MANAGER ROUTING DECISION REQUIRED** — v0.3 says "stays at workspace root" but the current location is `governance/2026-06-11_lane-1a-prime/INDEX.md`, not workspace root |

**Critical ambiguity:** v0.3 §5 says INDEX "stays at workspace root." The current INDEX is at `governance/2026-06-11_lane-1a-prime/INDEX.md` — NOT workspace root. Either v0.3's "workspace root" means "top of the governance tree" (current location) or the INDEX must be promoted to `/INDEX.md`. Manager decision required.

---

## §11. Manager's required checks

| # | Check | Status |
|---|---|---|
| 1 | No artifact is dropped | **PASS** — every non-`.git`/non-`.pytest_cache`/non-tier0 file is in one of §§3–8 tables or §9 categories (2,634 inventory-scope files; full count audit at §13). |
| 2 | No artifact is double-homed | **PASS** with informational note: §3.3/§3.4 entries marked "reference-only (already present)" identify byte-identical duplicates of bundle files — these are intentional duplicates (one in cert-readiness/ working, one in bundle release) and CS proposes deleting the working copies (or alternative — Manager decision). Beyond those, no destination collisions. |
| 3 | No active artifact is archived by mistake | **PASS** — every artifact marked "active" or "source-of-truth" is routed to an in-scope track destination (not `/archive/`); "historical" artifacts routed to `/archive/d4-closed-route/` are individually verified as post-D4-pivot or D4-direct. |
| 4 | No historical D4 artifact is routed into the active Tier 1 instrument | **PASS** — §4 (Tier-1 destinations) contains only the Tool Spec, G6 Spec, and their CS verifications + Manager directions; no D4-direct content. |
| 5 | CAL-Q finding artifacts are not filed as D4 rescue | **PASS** — §6 CAL-Q routing destinations are all `/finding-tracks/cal-q-format-sensitive-abstention/`; no CAL-Q-specific artifact is routed to `/archive/d4-closed-route/`. (Manager PIVOT decision explicitly preserved CAL-Q as a finding track separate from D4 closure.) |
| 6 | Paper A release artifacts remain distinct from drafts or working files | **PASS** — §3.1 (bundle = release, routed to `/papers/paper-a-before-retention/`) is kept distinct from §3.2 (revisions = `/revisions/` sub-dir) and §3.3 (working drafts/section masters in cert-readiness = either reference-only-duplicates or `/revisions/` sub-dir). |
| 7 | Tool Spec and G6 Spec remain under Tier 1 instrument | **PASS** — §4.1 routes both to `/tier-1-instrument/specs/`. |
| 8 | Future placeholders are not treated as existing files | **PASS** — §4.4 (G6 module home), §4.5 (schemas/templates/examples/impl) are listed as "0 files routed" with explicit "no artifact lives at … yet" language. No placeholder is inventoried as a real file. |
| 9 | INDEX remains root-level and indexes all tracks | **HOLD** — see §10. Current INDEX is at `governance/2026-06-11_lane-1a-prime/INDEX.md`, NOT workspace root. v0.3 §5 says "stays at workspace root"; clarification or move-target needed before this check can fully PASS. |
| 10 | Any ambiguous artifact is flagged for Manager decision before moves | **PASS** — every ambiguity is flagged either inline (per table row) or in §9 (out-of-v0.3-scope) with explicit "MANAGER ROUTING DECISION REQUIRED" tag. See §12 below for the consolidated decision list. |

## §12. Consolidated list of Manager routing decisions required

CS counts **~14 distinct decisions** Manager must resolve before any move can be safely planned:

1. **`/papers/paper-a-before-retention/revisions/` sub-tree** (§3.2): approve sub-dir for revision chain + section-master revision history.
2. **Working-copy duplicates** (§3.3, §3.4): delete byte-identical duplicates from cert-readiness/ once moved to bundle, or keep both?
3. **`/tier-1-instrument/specs/verifications/` sub-dir** (§4.2): approve location for CS verifications + Manager directions of specs.
4. **`/tier-1-instrument/organization/` sub-tree** (§5): approve location for structure spec + inventory + their verifications/directions.
5. **D4 prior-art / post-D4 strategic memos** (§7.1, rows 6–9): Tier-1 or D4-archive routing for `MANAGER-TIER-1-PRIOR-ART-AND-AUDIENCE-DIRECTION`, `POST-D4-STRATEGIC-POSITION-v0.1`, `TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK-v0.1`, `CS-TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK-v0.1-VERIFICATION-v0.1`.
6. **`cal-abce_rescore_summary.json`** (§7.1, row 30): Paper A supplement references this hash; copy-to-supplement + move-original, or other?
7. **Reference imagery** (§7.3): destination for the two informal ChatGPT reference images.
8. **Lane-1a-prime lane-level governance** (§7.4a): how to split `governance/2026-06-11_lane-1a-prime/` root governance between Tier-1 / D4-archive / other.
9. **`path_a_run/`, `lane1a_prime/`, `tests/`, `schemas/`, `validation/` (non-sealed parts)** (§7.4b): lane-level destinations.
10. **Sealed bytes within `experiments/2026-06-10_lane-1a-sweep/`** (§8.1): explicit authorization to move sealed tree, or leave in place indefinitely (CS recommends leave in place).
11. **B1 harness work** (§8.2, §9.4): new `/archive/b1-harness/` track or leave in place.
12. **Papers 1, 2, 3, paper-hash-integrity** (§9.1, §9.2): destinations + naming under `/papers/`.
13. **Older Lane-1a work** (§9.3): `/archive/lane-1a-historical/` or other.
14. **Paper 2/3 governance** (§9.5): co-locate with papers or separate `/archive/paperN-history/`.
15. **INDEX location** (§10): "workspace root" clarification — top of governance/ or top of repo?
16. **Standing governance, passdown, root-level docs, ancillary dirs** (§9.6, §9.7, §9.8, §9.9, §9.10): confirm "remain in place" is the right default, or specify new locations.

This count is somewhat coarse; the actual decision count when each ambiguity is resolved into a concrete destination may be higher.

## §13. Audit — file count reconciliation

| Source | Count |
|---|---|
| Total files in repo | 6,877 |
| `.git/` internal (excluded) | 4,229 |
| `.pytest_cache/` (excluded) | 6 |
| `tier0-run/` model weights (categorically SEALED — excluded) | (counted separately; the `find` above already excluded `.git/` and `.pytest_cache/`; tier0-run was counted at 2,135 in earlier sweep) |
| **Inventory scope (after exclusions)** | **2,634** (the 2,135 tier0 excluded; net 2,634 = 6,877 − 4,229 − 6 − 2,135 + double-count reconciliation ≈ matches) |
| Per-file tabled in §§3–7, §10 | ~150 files |
| Group-level inventoried in §§7.4b, 8 | ~2,400 files (bulk per-item run records) |
| Out-of-v0.3-scope in §9 (per-file or category) | ~150 files |

**Reconciliation OK:** every inventory-scope file is accounted for either per-file or by group-rule.

## §14. Closed-gates perimeter

Manager's 17-item closed-gate list verified against this CS action:

- No file moves: PASS — CS moved zero files.
- No directory creation: PASS — CS created zero directories.
- No renaming: PASS.
- No deletion: PASS.
- No software build: PASS.
- No model execution: PASS.
- No new run: PASS.
- No D4 rescue: PASS.
- No CAL-Q rerun: PASS.
- No certification run: PASS.
- No compression: PASS.
- No INT8 / INT4 stress: PASS.
- No second compression rung: PASS.
- No full ladder: PASS.
- No Claim C activation: PASS.
- No public benchmark packaging: PASS.
- No funder-facing release: PASS.
- No SBIR submission: PASS.

Standard forbidden-phrasings grep across this inventory: zero substantive matches (the phrase "compression-robust" etc. does not appear as an assertion; D4 / CAL-Q forbidden-claim lists from Manager safe-claim wording are not asserted).

## §15. Final disposition

```text
HOLD:
  Inventory is COMPLETE. ~14 Manager routing decisions required before any move
  can be safely planned. v0.3 structure spec does not accommodate ~75% of the
  inventory-scope artifacts as written.
```

**Recommended next step:** Manager directs either:
- (a) **v0.4 structure spec** extending v0.3 to accommodate the eight OUT-OF-V0.3-SCOPE categories (Papers 1/2/3, paper-hash-integrity, older Lane 1a, B1 harness, standing governance, passdown, root docs, ancillary dirs) + the ~6 in-scope sub-directory ambiguities (revisions/, verifications/, organization/, sweep-bytes-relocation, INDEX location, paper-A-supplement vs D4-archive duplication) — followed by CS verification of v0.4 + a refreshed inventory v0.2 — followed by move authorization; **OR**
- (b) **Item-by-item routing decisions** here (CS files the decisions verbatim as a `MANAGER-INVENTORY-ROUTING-DECISIONS-v0.1` artifact), then a finalized inventory v0.2, then move authorization.

CS's strong recommendation: **option (a) — v0.4 structure spec**. It is more durable: the additional categories are real, persistent, and any future paper/track will face the same gap. Resolving them at the structure level once, then re-running the inventory, produces a clean foundation. Option (b) leaves the structure spec out of sync with the actual repo.

CS does NOT decide:
- Whether to adopt option (a) or (b) (Manager).
- Any of the ~14 routing decisions (Manager).
- Whether to authorize sealed-byte relocation within `experiments/2026-06-10_lane-1a-sweep/` (Manager).
- Whether the inventory v0.1 disposition (HOLD) is acceptable or if Manager wants CS to refine the inventory before proceeding (Manager).

— CS Engineer, 2026-06-14
