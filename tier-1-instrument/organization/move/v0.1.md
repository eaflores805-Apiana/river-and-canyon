# REPO-MOVE-PLAN-v0.1

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Manager, Senior
**In response to:** `MANAGER-DIRECTION-RATIFY-INVENTORY-v0.2-FLAGS-AND-AUTHORIZE-MOVE-PLAN-DRAFT-2026-06-14.md` (Manager direction this turn — filed verbatim alongside this plan).
**Plan basis:** `COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.2.md` PASS + Manager's ratification of all 5 inventory flags + `TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4.md` accepted whole-repo map.
**Status:** MODEL-FREE PLANNING. This document drafts the move; **it does not move any file, create any directory, rename anything, or delete anything.** No file moves are authorized by this artifact. CS verifies the plan, TL routes, Manager decides whether to authorize execution.

---

## §1. Executive summary

The move plan is **execution choreography for a small physical change.** Inventory v0.2's reconciliation against v0.4 revealed that **only ~270 files physically move** (the cert-readiness/ split + governance epoch restructure + paper-a directory rename + sweep-byte relocation + root-doc relocation). The remaining ~2,364 inventory-scope files have v0.4 destinations that match their current paths and **do not physically move**.

Move composition (estimates; exact counts in §5):

| Move bucket | Approx files | Action |
|---|---|---|
| Paper A bundle directory rename (`papers/05_paper-a-before-retention/` → `papers/paper-a-before-retention/`) | 17 | git mv (tree rename) |
| Governance dated-epoch restructure (`governance/<date>_*/` → `governance/epochs/<date>_*/`) | ~70 files across ~11 epoch dirs + the 264-file Lane-1a-prime tree | git mv (tree-by-tree) |
| Cert-readiness/ split into Tier-1 / CAL-Q / D4-archive / Paper A revisions tracks | ~67 files in cert-readiness/ + 10 in paper-a-revisions/ + 5 in sweep_run_records/ + 2 in reference-imagery/ | git mv (file-by-file per §5 table) |
| Quarantine + constructed-positive → `/archive/d4-closed-route/` | 9 | git mv (tree) |
| First-compression-rung → `/governance/epochs/.../first-compression-rung/` (per flag 2) | 5 | git mv (tree) |
| Sweep-bytes physical relocation (flag 1) → `/experiments/.../` | 7 | git mv (specific files) |
| Root docs → `/_meta/` (except `.gitignore`) | 4 | git mv |
| **NEW FILE creation** (`/_meta/INDEX.md` per flag 4 option c) | 1 | written, not moved |
| Duplicate-master deletions (flag 3, AFTER verification) | 5 | git rm |
| **Total physical changes** | ~395 git ops | sequenced in §11 procedure |

**Files that do NOT physically move:** ~2,364 (paths unchanged under v0.4):
- All of `/experiments/` (~2,135 files)
- All of `/tier0-run/` (~2,135 files; categorically SEALED)
- `/governance/standing/` (25 files; path unchanged)
- `/governance/passdown/` (4 files; path unchanged)
- `/diagrams/` (14), `/notes/` (20), `/writing/` (18), `/review/` (1)
- `/papers/paper1-survival-is-not-correctness/`, `paper2-correctness-is-not-constructibility/`, `paper3-certification-before-retention/` (already in place)
- The 4 sealed bytes (DO NOT MOVE under flag 5)
- `.gitignore` (stays at workspace root per git semantics)

**Move is risk-low** because: (a) most files don't move; (b) every move is a `git mv` (preserves history and bytes); (c) hashes are pre-computed and post-verified; (d) sealed bytes excluded by category; (e) rollback is `git revert` of the move-commit.

---

## §2. Source structure (current; `origin/main` HEAD `38b9ada`)

Brief overview; full per-file enumeration in inventory v0.1 + v0.2:

```text
/                                                  root
├── .gitignore                                     (stays at root)
├── ONBOARDING-CS.md                               (move to /_meta/)
├── README.md                                      (move to /_meta/)
├── REVIEW.md                                      (move to /_meta/)
├── STATUS.md                                      (move to /_meta/)
├── diagrams/ (14)                                 (stays in place)
├── notes/ (20)                                    (stays in place)
├── review/ (1)                                    (stays in place)
├── writing/ (18)                                  (stays in place)
├── papers/
│   ├── 05_paper-a-before-retention/ (17)          (RENAME to paper-a-before-retention/)
│   ├── paper1-survival-is-not-correctness/ (13)   (stays in place)
│   ├── paper2-correctness-is-not-constructibility/ (stays in place)
│   └── paper3-certification-before-retention/     (stays in place)
├── governance/
│   ├── .gitkeep
│   ├── standing/ (25)                             (stays in place)
│   ├── passdown/ (4)                              (stays in place)
│   ├── 2026-06-09_b1-harness-plan-revision/ (1)   (MOVE to governance/epochs/)
│   ├── 2026-06-09_b1-harness-v2-merge-readiness/ (3) (MOVE to governance/epochs/)
│   ├── 2026-06-09_paper2-v1.0-release/ (2)        (MOVE to governance/epochs/)
│   ├── 2026-06-09_paper3-threshold-framework-review/ (14) (MOVE to governance/epochs/)
│   ├── 2026-06-09_scaling-discussion-item/ (1)    (MOVE to governance/epochs/)
│   ├── 2026-06-10_b1-harness-v2-merge-and-lock/ (3) (MOVE to governance/epochs/)
│   ├── 2026-06-10_lane-1a-authorization/ (1)      (MOVE to governance/epochs/)
│   ├── 2026-06-10_lane1a/ (67)                    (MOVE to governance/epochs/)
│   ├── 2026-06-10_paper3-external-review/ (6)     (MOVE to governance/epochs/)
│   ├── 2026-06-10_paper3-v1.0-release/ (9)        (MOVE to governance/epochs/)
│   ├── 2026-06-10_paper3-v1.1-release/ (2)        (MOVE to governance/epochs/)
│   └── 2026-06-11_lane-1a-prime/ (264, sub-tree split — see §4)
│       ├── INDEX.md                               (stays at current path per flag 5/v0.4 §7)
│       ├── LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md (move to governance/epochs/.../)
│       ├── certification-readiness/ (84)          (SPLIT — see §4)
│       │   ├── 67 direct files
│       │   ├── paper-a-revisions/ (10)
│       │   ├── sweep_run_records/ (5)
│       │   └── reference-imagery/ (2)
│       ├── quarantine/ (5)                        (MOVE to /archive/d4-closed-route/)
│       ├── constructed-positive-validation/ (4)   (MOVE to /archive/d4-closed-route/)
│       └── first-compression-rung/ (5)            (MOVE to governance/epochs/.../first-compression-rung/ per flag 2)
├── experiments/ (2,135)                           (stays in place; sealed bytes inside; SEE flag 5)
├── tier0-run/ (categorically SEALED)              (stays in place)
└── .git/, .pytest_cache/                          (excluded)
```

## §3. Target structure (v0.4)

```text
/                                                  root
├── .gitignore                                     (unchanged path; root-required)
├── _meta/
│   ├── README.md                                  (from root)
│   ├── STATUS.md                                  (from root)
│   ├── REVIEW.md                                  (from root)
│   ├── ONBOARDING-CS.md                           (from root)
│   └── INDEX.md                                   (NEW; top-level pointer per flag 4 option c)
├── diagrams/ notes/ review/ writing/              (unchanged)
├── papers/
│   ├── paper-a-before-retention/                  (renamed from 05_paper-a-before-retention/)
│   │   ├── (existing 17 bundle files)
│   │   └── revisions/                             (NEW sub-dir)
│   │       ├── PAPER-A-DRAFT-SKELETON-v0.2.md
│   │       ├── PAPER-A-DRAFT-v0.3.md
│   │       ├── PAPER-A-DRAFT-v0.4.md
│   │       ├── PAPER-A-DRAFT-v0.5.md
│   │       ├── PAPER-A-v0.6.md/.pdf
│   │       ├── PAPER-A-v0.7.md/.pdf
│   │       ├── PAPER-A-v0.8.md/.pdf
│   │       ├── PAPER-A-v0.9.md/.pdf
│   │       ├── PAPER-A-v1.0.md/.pdf               (byte-identical revision-anchor of bundle paper.{md,pdf}; KEEP both — intentional revision-chain pattern)
│   │       ├── sections/                          (positioning v0.1/v0.3/v0.4/v0.5/v0.6 historical drafts)
│   │       └── verifications/                     (CS-PAPER-A-* verification memos)
│   ├── paper1-survival-is-not-correctness/        (unchanged)
│   ├── paper2-correctness-is-not-constructibility/ (unchanged)
│   └── paper3-certification-before-retention/     (unchanged)
├── tier-1-instrument/
│   ├── README.md ROADMAP.md                       (NEW; written at move time)
│   ├── specs/
│   │   ├── eval-validity-gate-tool-spec-v0.1.md   (from cert-readiness/EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1.md, renamed lowercase)
│   │   ├── g6-standing-rejection-audit-spec-v0.1.md
│   │   ├── README.md                              (NEW; spec index)
│   │   └── verifications/                         (NEW)
│   │       ├── CS-EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1-VERIFICATION-v0.1.md
│   │       ├── CS-G6-STANDING-REJECTION-AUDIT-SPEC-v0.1-VERIFICATION-v0.1.md
│   │       ├── MANAGER-DIRECTION-EVAL-VALIDITY-GATE-TOOL-SPEC-VERIFICATION-2026-06-14.md
│   │       └── MANAGER-DIRECTION-G6-STANDING-REJECTION-AUDIT-SPEC-VERIFICATION-2026-06-14.md
│   ├── schemas/                                   (placeholder dirs + READMEs; created at move time)
│   ├── modules/g6-standing-rejection-audit/       (placeholder with README; created at move time)
│   ├── human-read-templates/                      (placeholder)
│   ├── examples/                                  (placeholder)
│   ├── implementation/                            (placeholder; EXPLICITLY NOT A BUILD)
│   ├── archive/                                   (placeholder)
│   └── organization/                              (CS-proposed; created at move time)
│       ├── structure/
│       │   ├── v0.1.md  v0.2.md  v0.3.md  v0.4.md (from cert-readiness/TIER-1-INSTRUMENT-REPO-STRUCTURE-v*.md)
│       │   ├── verifications/
│       │   │   ├── v0.1.md  v0.2.md  v0.3.md  v0.4.md (from cert-readiness/CS-TIER-1-INSTRUMENT-REPO-STRUCTURE-v*-VERIFICATION-v0.1.md)
│       │   └── manager-directions/
│       │       └── v0.1.md  v0.2.md  v0.3.md  v0.4.md
│       ├── inventory/
│       │   ├── v0.1.md  v0.2.md
│       │   └── manager-directions/
│       │       └── v0.1.md  v0.2.md
│       └── move/
│           ├── v0.1.md
│           └── manager-direction-v0.1.md
├── finding-tracks/
│   └── cal-q-format-sensitive-abstention/
│       ├── cal-q-finding-diagnostic-plan-v0.1.md  (from cert-readiness/CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1.md, renamed lowercase)
│       ├── README.md                              (NEW)
│       ├── findings/
│       │   ├── CAL-Q-FORMAT-SENSITIVE-ABSTENTION-FINDING-v0.1.md
│       │   ├── CAL-Q-RUN-INTERPRETATION-v0.1.md
│       │   └── CS-CAL-Q-RUN-REPORT-v0.1.md
│       └── verifications/
│           └── CS-CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1-VERIFICATION-v0.1.md
├── paper-b/planning/                              (placeholder; only stub README at move time)
├── governance/
│   ├── standing/                                  (unchanged path)
│   ├── passdown/                                  (unchanged path)
│   ├── epochs/                                    (NEW)
│   │   ├── 2026-06-09_b1-harness-plan-revision/
│   │   ├── 2026-06-09_b1-harness-v2-merge-readiness/
│   │   ├── 2026-06-09_paper2-v1.0-release/
│   │   ├── 2026-06-09_paper3-threshold-framework-review/
│   │   ├── 2026-06-09_scaling-discussion-item/
│   │   ├── 2026-06-10_b1-harness-v2-merge-and-lock/
│   │   ├── 2026-06-10_lane-1a-authorization/
│   │   ├── 2026-06-10_lane1a/                     (with c6_proposal_archive/ sub-tree)
│   │   ├── 2026-06-10_paper3-external-review/
│   │   ├── 2026-06-10_paper3-v1.0-release/
│   │   ├── 2026-06-10_paper3-v1.1-release/
│   │   └── 2026-06-11_lane-1a-prime/
│   │       ├── LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md
│   │       ├── INDEX.md                           (stays at current path per flag 5)
│   │       ├── certification-readiness/           (the remainder after split)
│   │       └── first-compression-rung/            (per flag 2)
│   ├── .gitkeep                                   (unchanged)
│   └── README.md                                  (NEW; epoch index)
├── archive/
│   ├── d4-closed-route/
│   │   ├── governance/                            (from cert-readiness/ D4-direct memos)
│   │   ├── cal-sweep/                             (from cert-readiness/ CAL-* and OFF-CEILING-* + NON-CONTENT-LEVER-D4-RESCUE-*)
│   │   ├── quarantine/                            (from gov/.../quarantine/)
│   │   ├── constructed-positive-validation/       (from gov/.../constructed-positive-validation/)
│   │   ├── reference-imagery/                     (from cert-readiness/reference-imagery/)
│   │   └── README.md                              (NEW)
│   └── superseded/                                (placeholder; for any future cross-track superseded items)
├── experiments/                                   (unchanged paths; sealed bytes inside)
└── tier0-run/                                     (unchanged paths; categorically SEALED)
```

## §4. Per-category move plan

### §4.1 Paper A bundle directory rename (17 files)

| Action | Source | Destination |
|---|---|---|
| `git mv -k papers/05_paper-a-before-retention papers/paper-a-before-retention` | tree | tree (all 17 files inside follow) |

Hash basis: each of the 17 file hashes is recorded in inventory v0.1 §3.1; post-move hash must match.

### §4.2 Governance dated-epoch restructure (11 epoch dirs + Lane-1a-prime)

For each dated epoch directory at `governance/<date>_*/`, the action is:

| Action | Source | Destination |
|---|---|---|
| `git mv -k governance/<date>_* governance/epochs/<date>_*` | tree | tree |

Applied to:
- `governance/2026-06-09_b1-harness-plan-revision/` (1 file)
- `governance/2026-06-09_b1-harness-v2-merge-readiness/` (3 files)
- `governance/2026-06-09_paper2-v1.0-release/` (2 files)
- `governance/2026-06-09_paper3-threshold-framework-review/` (14 files)
- `governance/2026-06-09_scaling-discussion-item/` (1 file)
- `governance/2026-06-10_b1-harness-v2-merge-and-lock/` (3 files)
- `governance/2026-06-10_lane-1a-authorization/` (1 file)
- `governance/2026-06-10_lane1a/` (67 files including `c6_proposal_archive/` sub-tree)
- `governance/2026-06-10_paper3-external-review/` (6 files)
- `governance/2026-06-10_paper3-v1.0-release/` (9 files)
- `governance/2026-06-10_paper3-v1.1-release/` (2 files)
- `governance/2026-06-11_lane-1a-prime/` (264 files MINUS the sub-trees handled separately: `certification-readiness/` split per §4.3, `quarantine/` per §4.4, `constructed-positive-validation/` per §4.5, `first-compression-rung/` per §4.6; INDEX.md stays at current path per flag 5)

Post-move governance epoch dirs all live at `governance/epochs/<date>_*/`. The `governance/standing/` and `governance/passdown/` sibling dirs are untouched.

### §4.3 cert-readiness/ split (see §5 for the full file-by-file table)

The cert-readiness/ directory contents split into five tracks:

1. **Tier-1 Tool Spec + G6 Spec FILES** → `/tier-1-instrument/specs/`
2. **Tier-1 verifications + Manager directions** → `/tier-1-instrument/specs/verifications/`
3. **Structure spec + inventory + move-plan + their verifications and directions** → `/tier-1-instrument/organization/{structure,inventory,move}/`
4. **CAL-Q diagnostic plan + verification + finding writeups** → `/finding-tracks/cal-q-format-sensitive-abstention/{,findings/,verifications/}`
5. **D4-direct governance + CAL-sweep artifacts + sweep bytes** → `/archive/d4-closed-route/{governance/,cal-sweep/}` AND sweep bytes → `/experiments/...` per flag 1
6. **Paper A working drafts + section masters + revision chain + verifications** → `/papers/paper-a-before-retention/revisions/{,sections/,verifications/}` (with 5 duplicate working masters deleted per flag 3)

The remainder of cert-readiness/ (after these extractions) is empty; the empty dir is removed at move time.

### §4.4 Quarantine + constructed-positive-validation → D4 archive

| Action | Source | Destination |
|---|---|---|
| `git mv -k governance/2026-06-11_lane-1a-prime/quarantine archive/d4-closed-route/quarantine` | tree (5 files) | tree |
| `git mv -k governance/2026-06-11_lane-1a-prime/constructed-positive-validation archive/d4-closed-route/constructed-positive-validation` | tree (4 files) | tree |

### §4.5 first-compression-rung (flag 2 ratified)

| Action | Source | Destination |
|---|---|---|
| `git mv -k governance/2026-06-11_lane-1a-prime/first-compression-rung governance/epochs/2026-06-11_lane-1a-prime/first-compression-rung` | tree (5 files) | tree |

NOTE: this is implicitly handled by §4.2's Lane-1a-prime tree-move IF the cert-readiness/ split is done first (so first-compression-rung/ is still inside Lane-1a-prime when Lane-1a-prime moves to epochs/). The ordering (§11) handles this. Per flag 2, first-compression-rung stays attached to Lane-1a-prime governance, NOT routed to D4-archive.

### §4.6 Sweep-bytes physical relocation (flag 1 ratified)

| Action | Source | Destination |
|---|---|---|
| `git mv governance/2026-06-11_lane-1a-prime/certification-readiness/sweep_run_records/cal-a_run.json experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_run_records/cal-a_run.json` | 1 | 1 |
| (repeat for cal-b_run.json, cal-c_run.json, cal-e_run.json, cal-q_run.json) | 4 | 4 |
| `git mv governance/2026-06-11_lane-1a-prime/certification-readiness/cal-abce_rescore_summary.json experiments/2026-06-11_lane-1a-prime/certification_readiness/cal-abce_rescore_summary.json` | 1 | 1 |
| `git mv governance/2026-06-11_lane-1a-prime/certification-readiness/cal-e_defective_error_table.json experiments/2026-06-11_lane-1a-prime/certification_readiness/cal-e_defective_error_table.json` | 1 | 1 |

**Total: 7 sweep-byte files relocated from governance to experiments.** Paper A supplement manifest already references these by hash — no copy made into `/papers/`; reference-by-hash preserved per v0.4 §6.

### §4.7 Root docs (4 files) → `/_meta/`

| Action | Source | Destination |
|---|---|---|
| `git mv README.md _meta/README.md` | 1 | 1 |
| `git mv STATUS.md _meta/STATUS.md` | 1 | 1 |
| `git mv REVIEW.md _meta/REVIEW.md` | 1 | 1 |
| `git mv ONBOARDING-CS.md _meta/ONBOARDING-CS.md` | 1 | 1 |

`.gitignore` STAYS at workspace root (git semantics require it there).

### §4.8 INDEX promotion (flag 4 option c — NEW file)

| Action | Source | Destination |
|---|---|---|
| Write new `_meta/INDEX.md` | (none — new file) | `_meta/INDEX.md` |

Contents (CS-proposed): a top-level pointer that names both existing INDEX files:
- `governance/2026-06-11_lane-1a-prime/INDEX.md` (or post-move `governance/epochs/2026-06-11_lane-1a-prime/INDEX.md` — see §4.2 NOTE) — the active program catalog
- `tier0-run/governance/2026-06-09_post-paper2-alignment/INDEX.md` — the tier0 catalog

Per Manager flag 4 ratification: "create a future top-level `/_meta/INDEX.md` that references both existing INDEX files rather than silently replacing either one." This is a CREATE, not a MOVE.

**Move-time INDEX-location wrinkle:** governance/2026-06-11_lane-1a-prime/INDEX.md will be at `governance/epochs/2026-06-11_lane-1a-prime/INDEX.md` post-move (because the parent tree moves under §4.2). The `/_meta/INDEX.md` pointer must reference the POST-MOVE path. Inventory v0.2 already flagged this; the pointer creation happens AFTER the governance-epoch restructure, with the correct post-move path baked in.

### §4.9 Duplicate-master deletions (flag 3 ratified — AFTER verification)

The 5 working-master files that duplicate Paper A bundle files (byte-identical, same sha256) are deleted AFTER the post-move verification confirms byte-identity has been preserved on the canonical bundle copy:

| File to delete | sha256 | Verified-identical-with |
|---|---|---|
| `governance/2026-06-11_lane-1a-prime/certification-readiness/PAPER-POSITIONING-SECTION-DRAFT-v0.7.md` | `34cedb30…` | `papers/paper-a-before-retention/sections/section-2-background.md` (same sha256) |
| `governance/2026-06-11_lane-1a-prime/certification-readiness/PAPER-SECTION-5-REJECTION-AUDIT-DRAFT-v0.1.md` | `4dc2f290…` | `papers/paper-a-before-retention/sections/section-5-rejection-audit.md` (same sha256) |
| `governance/2026-06-11_lane-1a-prime/certification-readiness/MANAGER-DECISION-PAPER-A-NOW-v0.1.md` | `1d901d5d…` | `papers/paper-a-before-retention/governance/MANAGER-DECISION-PAPER-A-NOW-v0.1.md` (same sha256) |
| `governance/2026-06-11_lane-1a-prime/certification-readiness/MANAGER-DECISION-VENUE-OPTION-2-v0.1.md` | `1e71640f…` | `papers/paper-a-before-retention/governance/MANAGER-DECISION-VENUE-OPTION-2-v0.1.md` (same sha256) |
| `governance/2026-06-11_lane-1a-prime/certification-readiness/VENUE-DECISION-MEMO-PAPER-A-v0.1.md` | `4f399b8e…` | `papers/paper-a-before-retention/governance/VENUE-DECISION-MEMO-PAPER-A-v0.1.md` (same sha256) |

The PAPER-A-v1.0.md and PAPER-A-v1.0.pdf in `paper-a-revisions/` (which are byte-identical to `paper-a-before-retention/paper/paper.{md,pdf}`) are **NOT deleted** — they are intentional revision-chain anchors that mirror the release snapshot. The revision chain keeps the v1.0 entry so the historical record reads correctly.

**Total deletions: 5 files** (after move + post-move verification).

## §5. Exact file-move table — cert-readiness/ split (the operational core)

Per-file moves for the 67 + 17 + 5 + 2 = 91 files in cert-readiness/ and its sub-trees. (Source: every entry from inventory v0.1 §3, §4, §5, §6, §7, §10 + the v0.4-routed-now-files for inventory v0.2 + move-plan + their Manager directions.)

### §5.1 Tool Spec + G6 Spec FILES → `/tier-1-instrument/specs/`

| Source path | Destination | Action |
|---|---|---|
| `governance/.../cert-readiness/EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1.md` (`fc0bee3f…`) | `tier-1-instrument/specs/eval-validity-gate-tool-spec-v0.1.md` | git mv + rename to lowercase |
| `governance/.../cert-readiness/G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md` (`2b4cedf8…`) | `tier-1-instrument/specs/g6-standing-rejection-audit-spec-v0.1.md` | git mv + rename |

### §5.2 Tier-1 spec verifications + Manager directions → `/tier-1-instrument/specs/verifications/`

| Source path | Destination | Action |
|---|---|---|
| `…/CS-EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1-VERIFICATION-v0.1.md` (`f072616e…`) | `tier-1-instrument/specs/verifications/CS-EVAL-…-v0.1.md` | git mv |
| `…/CS-G6-STANDING-REJECTION-AUDIT-SPEC-v0.1-VERIFICATION-v0.1.md` (`e080b74b…`) | `tier-1-instrument/specs/verifications/CS-G6-…-v0.1.md` | git mv |
| `…/MANAGER-DIRECTION-EVAL-VALIDITY-GATE-TOOL-SPEC-VERIFICATION-2026-06-14.md` (`52369271…`) | `tier-1-instrument/specs/verifications/MANAGER-DIRECTION-EVAL-…-2026-06-14.md` | git mv |
| `…/MANAGER-DIRECTION-G6-STANDING-REJECTION-AUDIT-SPEC-VERIFICATION-2026-06-14.md` (`418edb0e…`) | `tier-1-instrument/specs/verifications/MANAGER-DIRECTION-G6-…-2026-06-14.md` | git mv |

### §5.3 Structure spec revision chain → `/tier-1-instrument/organization/structure/`

| Source path | Destination | Action |
|---|---|---|
| `…/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.1.md` (`2048396d…`) | `tier-1-instrument/organization/structure/v0.1.md` | git mv |
| `…/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.2.md` (`bc9a4014…`) | `tier-1-instrument/organization/structure/v0.2.md` | git mv |
| `…/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.3.md` (`d691ded8…`) | `tier-1-instrument/organization/structure/v0.3.md` | git mv |
| `…/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4.md` (`9718ec59…`) | `tier-1-instrument/organization/structure/v0.4.md` | git mv |
| `…/CS-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.1-VERIFICATION-v0.1.md` (`adaa204a…`) | `tier-1-instrument/organization/structure/verifications/v0.1.md` | git mv |
| `…/CS-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.2-VERIFICATION-v0.1.md` (`3db8fadb…`) | `tier-1-instrument/organization/structure/verifications/v0.2.md` | git mv |
| `…/CS-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.3-VERIFICATION-v0.1.md` (`aace3406…`) | `tier-1-instrument/organization/structure/verifications/v0.3.md` | git mv |
| `…/CS-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4-VERIFICATION-v0.1.md` (sha at commit) | `tier-1-instrument/organization/structure/verifications/v0.4.md` | git mv |
| `…/MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-VERIFICATION-2026-06-14.md` (`c2b73632…`) | `tier-1-instrument/organization/structure/manager-directions/v0.1.md` | git mv |
| `…/MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.2-VERIFICATION-2026-06-14.md` (`43b199b8…`) | `tier-1-instrument/organization/structure/manager-directions/v0.2.md` | git mv |
| `…/MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.3-VERIFICATION-2026-06-14.md` (`f4720f08…`) | `tier-1-instrument/organization/structure/manager-directions/v0.3.md` | git mv |
| `…/MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4-VERIFICATION-2026-06-14.md` (sha at commit) | `tier-1-instrument/organization/structure/manager-directions/v0.4.md` | git mv |

### §5.4 Inventory chain → `/tier-1-instrument/organization/inventory/`

| Source path | Destination | Action |
|---|---|---|
| `…/COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.1.md` (sha at commit `e960add`) | `tier-1-instrument/organization/inventory/v0.1.md` | git mv |
| `…/COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.2.md` (sha at commit `e676011`) | `tier-1-instrument/organization/inventory/v0.2.md` | git mv |
| `…/MANAGER-DIRECTION-AUTHORIZE-COMPLETE-ARTIFACT-INVENTORY-2026-06-14.md` (sha at commit) | `tier-1-instrument/organization/inventory/manager-directions/v0.1.md` | git mv |
| `…/MANAGER-DIRECTION-AUTHORIZE-INVENTORY-v0.2-AGAINST-v0.4-2026-06-14.md` (sha at commit) | `tier-1-instrument/organization/inventory/manager-directions/v0.2.md` | git mv |

### §5.5 Move plan (this artifact + its direction) → `/tier-1-instrument/organization/move/`

| Source path | Destination | Action |
|---|---|---|
| `…/REPO-MOVE-PLAN-v0.1.md` (this file; sha at commit) | `tier-1-instrument/organization/move/v0.1.md` | git mv |
| `…/MANAGER-DIRECTION-RATIFY-INVENTORY-v0.2-FLAGS-AND-AUTHORIZE-MOVE-PLAN-DRAFT-2026-06-14.md` (sha at commit) | `tier-1-instrument/organization/move/manager-directions/v0.1.md` | git mv |

### §5.6 CAL-Q finding-track → `/finding-tracks/cal-q-format-sensitive-abstention/`

| Source path | Destination | Action |
|---|---|---|
| `…/CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1.md` (`0c2afbbc…`) | `finding-tracks/cal-q-format-sensitive-abstention/cal-q-finding-diagnostic-plan-v0.1.md` | git mv + rename |
| `…/CS-CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1-VERIFICATION-v0.1.md` (`161d450a…`) | `finding-tracks/cal-q-format-sensitive-abstention/verifications/CS-…-v0.1.md` | git mv |
| `…/CAL-Q-FORMAT-SENSITIVE-ABSTENTION-FINDING-v0.1.md` (`8aebefeb…`) | `finding-tracks/cal-q-format-sensitive-abstention/findings/CAL-Q-FORMAT-SENSITIVE-ABSTENTION-FINDING-v0.1.md` | git mv |
| `…/CAL-Q-RUN-INTERPRETATION-v0.1.md` (`d0bd4e87…`) | `finding-tracks/cal-q-format-sensitive-abstention/findings/CAL-Q-RUN-INTERPRETATION-v0.1.md` | git mv |
| `…/CS-CAL-Q-RUN-REPORT-v0.1.md` (`c64c8bda…`) | `finding-tracks/cal-q-format-sensitive-abstention/findings/CS-CAL-Q-RUN-REPORT-v0.1.md` | git mv |

### §5.7 D4-direct governance + cal-sweep artifacts → `/archive/d4-closed-route/`

| Source path | Destination | Action |
|---|---|---|
| `…/MANAGER-D4-PIVOT-DECISION-AND-CALQ-FINDING-TRACK-2026-06-13.md` (`86f3e5ff…`) | `archive/d4-closed-route/governance/MANAGER-D4-PIVOT-DECISION-AND-CALQ-FINDING-TRACK-2026-06-13.md` | git mv |
| `…/MANAGER-NON-CONTENT-LEVER-D4-RESCUE-DIRECTION-2026-06-13.md` (`d24cd53a…`) | `archive/d4-closed-route/governance/…-2026-06-13.md` | git mv |
| `…/MANAGER-OFF-CEILING-CALIBRATION-SWEEP-AUTHORIZATION-2026-06-13.md` (`6fba3f39…`) | `archive/d4-closed-route/governance/…-2026-06-13.md` | git mv |
| `…/MANAGER-CAL-E-TARGETED-REPAIR-AUTHORIZATION-2026-06-13.md` (`fecb0b37…`) | `archive/d4-closed-route/governance/…-2026-06-13.md` | git mv |
| `…/MANAGER-POST-D4-STRATEGIC-POSITION-DIRECTION-2026-06-13.md` (`8c222fcc…`) | `archive/d4-closed-route/governance/post-d4/MANAGER-POST-D4-STRATEGIC-POSITION-DIRECTION-2026-06-13.md` | git mv |
| `…/MANAGER-TIER-1-PRIOR-ART-AND-AUDIENCE-DIRECTION-2026-06-13.md` (`fe119b12…`) | `archive/d4-closed-route/governance/post-d4/…-2026-06-13.md` | git mv |
| `…/POST-D4-STRATEGIC-POSITION-v0.1.md` (`af27ce8b…`) | `archive/d4-closed-route/governance/post-d4/POST-D4-STRATEGIC-POSITION-v0.1.md` | git mv |
| `…/TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK-v0.1.md` (`dbb3833c…`) | `archive/d4-closed-route/governance/post-d4/TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK-v0.1.md` | git mv |
| `…/CS-TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK-v0.1-VERIFICATION-v0.1.md` (`9429dff1…`) | `archive/d4-closed-route/governance/post-d4/CS-TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK-v0.1-VERIFICATION-v0.1.md` | git mv |
| `…/CS-CERT-READINESS-SUBMAP-STAGE-1-2-VERIFICATION-v0.1.md` (`9b51056b…`) | `archive/d4-closed-route/governance/CS-CERT-READINESS-SUBMAP-STAGE-1-2-VERIFICATION-v0.1.md` | git mv |
| `…/CAL-ABCE-RESCORE-REINTERPRETATION-v0.1.md` (`8433e32f…`) | `archive/d4-closed-route/cal-sweep/CAL-ABCE-RESCORE-REINTERPRETATION-v0.1.md` | git mv |
| `…/CAL-E-DEFECTIVE-ERROR-ANALYSIS-v0.1.md` (`fc5569da…`) | `archive/d4-closed-route/cal-sweep/CAL-E-DEFECTIVE-ERROR-ANALYSIS-v0.1.md` | git mv |
| `…/CAL-E-INTERPRETATION-v0.1.md` (`4cafaedb…`) | `archive/d4-closed-route/cal-sweep/CAL-E-INTERPRETATION-v0.1.md` | git mv |
| `…/CAL-E-TARGETED-REPAIR-SPEC-v0.1.md` (`f90f7132…`) | `archive/d4-closed-route/cal-sweep/CAL-E-TARGETED-REPAIR-SPEC-v0.1.md` | git mv |
| `…/CS-CAL-ABCE-NULL-NORMALIZED-RESCORE-v0.1.md` (`d1703d43…`) | `archive/d4-closed-route/cal-sweep/CS-CAL-ABCE-NULL-NORMALIZED-RESCORE-v0.1.md` | git mv |
| `…/CS-CAL-E-DEFECTIVE-OUTPUT-EXTRACTION-v0.1.md` (`cdf11691…`) | `archive/d4-closed-route/cal-sweep/CS-CAL-E-DEFECTIVE-OUTPUT-EXTRACTION-v0.1.md` | git mv |
| `…/CS-CAL-E-TARGETED-REPAIR-RUN-REPORT-v0.1.md` (`bf62652e…`) | `archive/d4-closed-route/cal-sweep/CS-CAL-E-TARGETED-REPAIR-RUN-REPORT-v0.1.md` | git mv |
| `…/CS-NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1-VERIFICATION-v0.1.md` (`10958c9f…`) | `archive/d4-closed-route/cal-sweep/CS-NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1-VERIFICATION-v0.1.md` | git mv |
| `…/CS-NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.2-VERIFICATION-v0.1.md` (`2be56f91…`) | `archive/d4-closed-route/cal-sweep/CS-NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.2-VERIFICATION-v0.1.md` | git mv |
| `…/CS-NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.3-VERIFICATION-v0.1.md` (`6f00c877…`) | `archive/d4-closed-route/cal-sweep/CS-NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.3-VERIFICATION-v0.1.md` | git mv |
| `…/CS-OFF-CEILING-CALIBRATION-SWEEP-RUN-REPORT-v0.1.md` (`3cad1a96…`) | `archive/d4-closed-route/cal-sweep/CS-OFF-CEILING-CALIBRATION-SWEEP-RUN-REPORT-v0.1.md` | git mv |
| `…/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1.md` (`d0bb0217…`) | `archive/d4-closed-route/cal-sweep/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1.md` | git mv |
| `…/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.2.md` (`d88cfef9…`) | `archive/d4-closed-route/cal-sweep/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.2.md` | git mv |
| `…/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.3.md` (`83924900…`) | `archive/d4-closed-route/cal-sweep/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.3.md` | git mv |
| `…/OFF-CEILING-CALIBRATION-READ-VERDICT-v0.1.md` (`5b37de7a…`) | `archive/d4-closed-route/cal-sweep/OFF-CEILING-CALIBRATION-READ-VERDICT-v0.1.md` | git mv |
| `…/OFF-CEILING-CALIBRATION-SWEEP-INTERPRETATION-v0.1.md` (`e666c2e4…`) | `archive/d4-closed-route/cal-sweep/OFF-CEILING-CALIBRATION-SWEEP-INTERPRETATION-v0.1.md` | git mv |
| `…/OFF-CEILING-CALIBRATION-SWEEP-RUNSPEC-v0.1.md` (`84ad4008…`) | `archive/d4-closed-route/cal-sweep/OFF-CEILING-CALIBRATION-SWEEP-RUNSPEC-v0.1.md` | git mv |
| `…/OFF-CEILING-CALIBRATION-SWEEP-SPEC-v0.1.md` (`18ac212f…`) | `archive/d4-closed-route/cal-sweep/OFF-CEILING-CALIBRATION-SWEEP-SPEC-v0.1.md` | git mv |
| `…/OFF-CEILING-D4-REPAIR-DESIGN-v0.1.md` (`15041107…`) | `archive/d4-closed-route/cal-sweep/OFF-CEILING-D4-REPAIR-DESIGN-v0.1.md` | git mv |
| `…/reference-imagery/ChatGPT-Image-2026-06-13-08_24_45-PM.png` (`346c2edb…`) | `archive/d4-closed-route/reference-imagery/ChatGPT-Image-2026-06-13-08_24_45-PM.png` | git mv |
| `…/reference-imagery/ChatGPT-Image-2026-06-13-08_31_16-PM.png` (`dd6d5ee8…`) | `archive/d4-closed-route/reference-imagery/ChatGPT-Image-2026-06-13-08_31_16-PM.png` | git mv |

### §5.8 Paper A working drafts + section masters → `/papers/paper-a-before-retention/revisions/`

| Source path | Destination | Action |
|---|---|---|
| `…/PAPER-A-DRAFT-SKELETON-v0.2.md` (`d87f08ae…`) | `papers/paper-a-before-retention/revisions/PAPER-A-DRAFT-SKELETON-v0.2.md` | git mv |
| `…/PAPER-A-DRAFT-v0.3.md` (`0a54db9a…`) | `papers/paper-a-before-retention/revisions/PAPER-A-DRAFT-v0.3.md` | git mv |
| `…/PAPER-A-DRAFT-v0.4.md` (`6bcfc17f…`) | `papers/paper-a-before-retention/revisions/PAPER-A-DRAFT-v0.4.md` | git mv |
| `…/PAPER-A-DRAFT-v0.5.md` (`557bc005…`) | `papers/paper-a-before-retention/revisions/PAPER-A-DRAFT-v0.5.md` | git mv |
| `…/PAPER-POSITIONING-SECTION-DRAFT-v0.1.md` (`261309ae…`) | `papers/paper-a-before-retention/revisions/sections/section-2-background/v0.1.md` | git mv |
| `…/PAPER-POSITIONING-SECTION-DRAFT-v0.3.md` (`5aff96d7…`) | `papers/paper-a-before-retention/revisions/sections/section-2-background/v0.3.md` | git mv |
| `…/PAPER-POSITIONING-SECTION-DRAFT-v0.4.md` (`c2dbae44…`) | `papers/paper-a-before-retention/revisions/sections/section-2-background/v0.4.md` | git mv |
| `…/PAPER-POSITIONING-SECTION-DRAFT-v0.5.md` (`7579b006…`) | `papers/paper-a-before-retention/revisions/sections/section-2-background/v0.5.md` | git mv |
| `…/PAPER-POSITIONING-SECTION-DRAFT-v0.6.md` (`78f7cfed…`) | `papers/paper-a-before-retention/revisions/sections/section-2-background/v0.6.md` | git mv |
| `…/PAPER-POSITIONING-SECTION-DRAFT-v0.7.md` (`34cedb30…`) | **DELETE** (see §4.9) — byte-identical to bundle `section-2-background.md` | git rm (after verification) |
| `…/PAPER-SECTION-5-REJECTION-AUDIT-DRAFT-v0.1.md` (`4dc2f290…`) | **DELETE** — byte-identical to bundle `section-5-rejection-audit.md` | git rm (after verification) |
| `…/MANAGER-DECISION-PAPER-A-NOW-v0.1.md` (`1d901d5d…`) | **DELETE** — byte-identical to bundle `governance/MANAGER-DECISION-PAPER-A-NOW-v0.1.md` | git rm |
| `…/MANAGER-DECISION-VENUE-OPTION-2-v0.1.md` (`1e71640f…`) | **DELETE** — byte-identical to bundle `governance/MANAGER-DECISION-VENUE-OPTION-2-v0.1.md` | git rm |
| `…/VENUE-DECISION-MEMO-PAPER-A-v0.1.md` (`4f399b8e…`) | **DELETE** — byte-identical to bundle `governance/VENUE-DECISION-MEMO-PAPER-A-v0.1.md` | git rm |
| `…/CS-PAPER-A-DRAFT-v0.4-CITATION-AND-PROVENANCE-VERIFICATION-v0.1.md` (`918489…`) | `papers/paper-a-before-retention/revisions/verifications/CS-PAPER-A-DRAFT-v0.4-CITATION-AND-PROVENANCE-VERIFICATION-v0.1.md` | git mv |
| `…/CS-PAPER-A-GITHUB-BUNDLE-SWEEP-AND-VERIFICATION-v0.1.md` (`d026a974…`) | `papers/paper-a-before-retention/revisions/verifications/CS-PAPER-A-GITHUB-BUNDLE-SWEEP-AND-VERIFICATION-v0.1.md` | git mv |

### §5.9 paper-a-revisions/ → `/papers/paper-a-before-retention/revisions/`

All 10 files (PAPER-A-v0.6 through v1.0, md + pdf each) move as a tree:

| Source path | Destination | Action |
|---|---|---|
| `…/paper-a-revisions/PAPER-A-v0.6.md` (`eb96f009…`) | `papers/paper-a-before-retention/revisions/PAPER-A-v0.6.md` | git mv (tree) |
| `…/paper-a-revisions/PAPER-A-v0.6.pdf` (`4772dcd5…`) | `papers/paper-a-before-retention/revisions/PAPER-A-v0.6.pdf` | git mv (tree) |
| (repeat for v0.7, v0.8, v0.9, v1.0 — both .md and .pdf) | — | — |

Note: PAPER-A-v1.0.md/.pdf in revisions/ are byte-identical to bundle's `paper/paper.{md,pdf}` (`4272e12a…` / `57458c90…`); both copies are retained as intentional revision-chain anchor + release snapshot. Not deleted.

### §5.10 The Manager direction for THIS move plan (filed verbatim this turn)

| Source path | Destination | Action |
|---|---|---|
| `…/MANAGER-DIRECTION-RATIFY-INVENTORY-v0.2-FLAGS-AND-AUTHORIZE-MOVE-PLAN-DRAFT-2026-06-14.md` | `tier-1-instrument/organization/move/manager-directions/v0.1.md` | git mv |

---

## §6. Explicit list of files that do not move (the large majority)

Files whose path under v0.4 matches their current path → **no physical move**:

- All `experiments/**` (~2,135 files including 4 sealed bytes; SEE §10)
- All `tier0-run/**` (~2,135 files; categorically SEALED — SEE §10)
- All `governance/standing/**` (25 files)
- All `governance/passdown/**` (4 files)
- `governance/.gitkeep`
- All `diagrams/**` (14), `notes/**` (20), `writing/**` (18), `review/**` (1)
- All `papers/paper1-survival-is-not-correctness/**` (13 files)
- All `papers/paper2-correctness-is-not-constructibility/**` (existing files)
- All `papers/paper3-certification-before-retention/**` (existing files)
- `.gitignore` (workspace root; git semantics)
- `governance/2026-06-11_lane-1a-prime/INDEX.md` (or post-move-equivalent path; see §9)

**Total "stay in place" inventory-scope files:** ~2,364 (the vast majority of the 2,634 in-scope total).

## §7. Duplicate-pair handling plan (flag 3)

Per Manager flag 3 ratification, **5 working-master files in cert-readiness/ are deleted ONLY AFTER**:

1. The corresponding bundle file is confirmed present at the destination `papers/paper-a-before-retention/{sections,governance}/`.
2. The bundle file's sha256 matches the pre-move working-master sha256 byte-for-byte.
3. Hash-verification step §11 completes PASS.

**Sequencing:** the 5 deletions happen LAST in the move sequence, after all moves complete and post-move verification (§13) confirms byte-identity preservation.

**The 2 paper-a-revisions PAPER-A-v1.0.{md,pdf} files are NOT deleted** — they are intentional revision-chain anchors that record v1.0 as a historical version alongside the bundle's release snapshot.

## §8. Sweep-byte relocation plan (flag 1)

Per Manager flag 1 ratification, **7 sweep-byte files physically relocate** from `governance/` to `experiments/`:

- 5 files in `governance/.../cert-readiness/sweep_run_records/`
- 2 files in `governance/.../cert-readiness/` (`cal-abce_rescore_summary.json`, `cal-e_defective_error_table.json`)

**Destinations:** under `experiments/2026-06-11_lane-1a-prime/certification_readiness/` to keep them adjacent to the lane-1a-prime certification-readiness experiment context.

**Paper A supplement preservation:** the supplement manifest (`papers/paper-a-before-retention/supplement/README.md`) currently references these files by sha256. **The sha256 references remain valid post-move** because the bytes don't change — only the path does. Verification step §13 includes: "Paper A supplement hash references still resolve to the same bytes (which now live at experiments/ paths)."

**No copy is made into `/papers/`** per v0.4 §6 reference-not-copy rule.

## §9. INDEX promotion/reconciliation plan (flag 4 option c)

Per Manager flag 4 ratification:

1. **Active program INDEX** stays at its current path post-move: `governance/epochs/2026-06-11_lane-1a-prime/INDEX.md` (the path becomes `epochs/`-prefixed because the parent tree moves under §4.2; the INDEX file itself does NOT move, but its containing dir moves around it — a tree-rename move).
2. **Tier0 INDEX** stays at its current path: `tier0-run/governance/2026-06-09_post-paper2-alignment/INDEX.md` (unchanged; tier0-run is categorically untouched).
3. **NEW** `_meta/INDEX.md` created at move time as a top-level pointer:
   - References the active program INDEX at its post-move path.
   - References the tier0 INDEX at its current path.
   - Does NOT supersede or replace either; provides a single entry point.

**Content of new `_meta/INDEX.md`:** a brief README-style pointer doc with two named cross-references and a one-line description of each. No catalog rows are duplicated.

## §10. Sealed-byte handling plan (flag 5)

Per Manager flag 5 ratification: **sealed bytes are NOT moved.**

Sealed-byte paths (unchanged post-move):
1. `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`)
2. `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`)
3. `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`)
4. `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`)
5. The entire `tier0-run/` tree (~2,135 files).

**These paths appear in §6 ("stay in place").** No git operation touches them.

**Verification (§13) re-hashes the 4 individual sealed files plus a sample of tier0-run/ contents to confirm bytes preserved.** Any post-move hash mismatch on a sealed byte is a CRITICAL FAIL → immediate rollback per §12.

## §11. Hash-verification procedure

The move-execution sequence interleaves git operations with hash checkpoints. CS proposes this sequence (Manager may adjust):

**Step 1 — Pre-move snapshot.**
- Hash every inventory-scope file (`shasum -a 256`) and record in a file `MOVE-PRE-SNAPSHOT.json` (path → sha256).
- Verify total inventory-scope file count matches v0.2 (2,634).
- Verify all 4 sealed bytes + sample tier0-run/ files are unchanged from baseline.

**Step 2 — Branch creation.**
- Create a branch `repo-move-v0.1` off `origin/main` HEAD. Move operations happen on this branch; main is untouched until merge.

**Step 3 — Move execution (in order — see §11.1 sub-steps below).**
- Each sub-step ends with a partial-snapshot hash check before proceeding.

**Step 4 — Post-move snapshot.**
- Hash every file at its NEW path.
- Build `MOVE-POST-SNAPSHOT.json` (path → sha256).
- Compare: for every (old-path, new-path) pair in the move-plan tables, assert `pre[old-path].sha256 == post[new-path].sha256`.
- For every "stay in place" file, assert `pre[path].sha256 == post[path].sha256`.
- For every duplicate-deletion candidate, assert `post[deleted-path]` does not exist AND `post[canonical-bundle-path].sha256 == pre[working-master-path].sha256`.

**Step 5 — Sealed-byte explicit re-verification.**
- The 4 sealed-byte hashes individually re-verified. Critical fail → rollback.

**Step 6 — Merge to main.**
- After all checks PASS, merge `repo-move-v0.1` to main.

### §11.1 Move execution sub-steps (order matters)

1. **Phase A — Rename Paper A bundle directory.** `git mv -k papers/05_paper-a-before-retention papers/paper-a-before-retention`. Hash check on the 17 files at new paths.
2. **Phase B — Create new top-level directories** (empty + READMEs + placeholders): `tier-1-instrument/`, `finding-tracks/`, `paper-b/planning/`, `archive/d4-closed-route/{governance,cal-sweep,quarantine,constructed-positive-validation,reference-imagery,post-d4}/`, `archive/superseded/`, `_meta/`, `governance/epochs/`.
3. **Phase C — Sweep-byte relocation** (flag 1): move the 7 sweep-byte files from governance/cert-readiness/ to experiments/.../. Hash check.
4. **Phase D — cert-readiness/ split:** execute §5.1–§5.9 file moves. Hash check after each sub-section.
5. **Phase E — Quarantine + constructed-positive-validation tree moves** (§4.4) → archive/d4-closed-route/.
6. **Phase F — First-compression-rung move** (§4.5 / flag 2): NOT to archive — to `governance/epochs/2026-06-11_lane-1a-prime/first-compression-rung/`.
7. **Phase G — Governance dated-epoch restructure** (§4.2): `git mv` each `governance/<date>_*/` → `governance/epochs/<date>_*/`. Includes the (now-partially-emptied) Lane-1a-prime tree as a single move (its INDEX.md and remaining cert-readiness/ sub-tree go with it).
8. **Phase H — Root docs to `/_meta/`** (§4.7).
9. **Phase I — Create new `_meta/INDEX.md`** (flag 4 option c). Write the pointer file. Verify it references the post-move INDEX paths correctly.
10. **Phase J — Post-move hash check + sealed-byte verification.**
11. **Phase K — Duplicate-master deletions** (flag 3): execute the 5 `git rm` only AFTER Phase J PASSes. Re-hash after deletion.
12. **Phase L — Cleanup empty directories** (e.g., the now-empty cert-readiness/ if all contents extracted): `git mv` cannot remove dirs; rely on git's empty-dir handling (git doesn't track empty dirs).
13. **Phase M — Final hash audit.**

## §12. Rollback plan

**Trigger conditions for rollback:**
- Any sealed-byte hash mismatch post-move → IMMEDIATE rollback.
- Any inventory-scope file post-move hash differs from pre-move hash for the same byte sequence (i.e., a moved file's content changed somehow) → rollback.
- Any duplicate-deletion candidate not byte-identical to its canonical bundle counterpart at deletion time → DO NOT delete; defer to Manager.
- Any inventory-scope file present pre-move but missing both at old AND new paths post-move → rollback.

**Rollback mechanism:**
- All moves happen on branch `repo-move-v0.1` (Step 2). The branch is NOT merged to main until all checks PASS.
- Rollback = `git checkout main && git branch -D repo-move-v0.1`. Main is untouched.
- If the branch was merged: `git revert <merge-commit>` on main; force-push not used; create follow-up commit.

**Manual recovery:** the full pre-move snapshot (Step 1) provides a path → sha256 mapping that can rebuild any file from git history (since `git mv` preserves blob contents).

## §13. Post-move verification checklist

Executed by CS after Phase M of §11. PASS-required items:

1. Every pre-move file's bytes (by sha256) exist exactly once in the post-move repo (either at the moved-to path or, for "stay in place", at the unchanged path; or, for deleted working masters, at the canonical bundle path).
2. The 4 sealed-byte hashes match pre-move values at their paths.
3. The tier0-run/ tree sample hashes match.
4. The 17 Paper A bundle files exist at `papers/paper-a-before-retention/` with hashes matching pre-move bundle hashes.
5. The 10 paper-a-revisions/ files exist at `papers/paper-a-before-retention/revisions/` with hashes matching pre-move.
6. The 7 sweep-byte files exist at their new `experiments/.../` paths with hashes matching pre-move.
7. The 5 working-master deletions verified: each deleted-path no longer exists; each canonical bundle path holds the same byte content.
8. The new `_meta/INDEX.md` exists; its content references the two existing INDEX files at their post-move paths.
9. The cert-readiness/ directory either no longer exists or holds only the files that weren't extracted (i.e., the Lane-1a-prime/cert-readiness/ "remainder" — primarily this move plan itself and the new structure-spec/inventory artifacts if they were filed before the move and didn't get extracted).
10. The `governance/epochs/` directory exists and contains all 12 dated epoch sub-dirs (including the moved Lane-1a-prime).
11. The `governance/standing/` and `governance/passdown/` paths are unchanged.
12. Inventory v0.2 file-count audit: 2,634 inventory-scope files still total 2,634 (modulo the 5 working-master deletions → 2,629 + 1 new INDEX.md → 2,630). Account for any net change exactly.
13. Sealed-bytes survival check increments (~77th).
14. Standard forbidden-phrasings grep across moved files: zero new matches.

## §14. Closed gates (drafting boundary)

This plan was drafted under Manager's 20-item closed-gate list (verified verbatim against `MANAGER-DIRECTION-RATIFY-INVENTORY-v0.2-FLAGS-AND-AUTHORIZE-MOVE-PLAN-DRAFT-2026-06-14.md`):

- No file moves — PASS (CS moved zero files in producing this draft).
- No directory creation — PASS.
- No renaming — PASS.
- No deletion — PASS.
- No software build — PASS.
- No model execution — PASS.
- No new run — PASS.
- No D4 rescue — PASS.
- No CAL-Q rerun — PASS.
- No certification run — PASS.
- No compression — PASS.
- No INT8 / INT4 stress — PASS.
- No second compression rung — PASS.
- No full ladder — PASS.
- No Claim C activation — PASS.
- No Paper B activation — PASS.
- No public benchmark packaging — PASS.
- No funder-facing release — PASS.
- No SBIR submission — PASS.
- Sealed bytes DO NOT MOVE — PASS (sealed bytes are explicitly excluded from move scope per §10).

Standard forbidden-phrasings grep across this plan: zero matches.

## §15. CS self-verification of this plan

Per Manager direction's return path ("CS verifies the plan. Team Lead routes it. Manager decides whether to authorize the actual move."), CS records the self-verification disposition here.

**Self-verification disposition: PASS** — the move plan is internally consistent, every required Manager content item (§1–§14) is present, every ratified flag is operationalized (flag 1 in §4.6 + §8; flag 2 in §4.5; flag 3 in §4.9 + §7; flag 4 in §4.8 + §9; flag 5 in §10), and the move-execution choreography (§11) is bounded, reversible (§12), and verifiable (§13).

**Two non-blocking notes for Senior/Manager review:**
- The `tier-1-instrument/organization/` sub-tree (§5.3–§5.5) is CS-proposed under v0.4 §3 which does NOT explicitly name it. v0.4 §6's "revisions/verifications/organization route-with-parent" rule supports the CS proposal but does not mandate it. Manager may direct an alternative location for these governance-of-the-organization-document artifacts.
- The move-plan execution (Phase B in §11.1 creates ~10 new directories) is the FIRST time directory creation happens in this entire workflow. The current direction forbids directory creation, so directory creation is gated by the SUBSEQUENT move-authorization direction Manager will issue after this plan PASSes verification.

## §16. Final disposition

```text
REPO-MOVE-PLAN-v0.1 DRAFTED.
CS self-verification: PASS.
Ready for Team Lead routing and Manager decision on whether to
authorize the actual move.
```

CS does NOT decide:
- Whether to approve this plan (Manager — after TL routing).
- Whether to authorize the actual move (Manager — separate step after plan approval).
- Whether the CS-proposed `tier-1-instrument/organization/` sub-tree is the right home for organization-of-the-organization-document artifacts (Manager, per §15 note 1).
- Whether move execution should happen in one PR or staged across multiple PRs (Manager, per §11 sequencing — CS proposes single branch + single merge).

Sealed bytes UNCHANGED (≈77th survival check, taken at the drafting of this plan).

— CS Engineer, 2026-06-14
