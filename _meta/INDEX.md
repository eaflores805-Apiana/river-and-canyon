# INDEX (top-level pointer)

This is a top-level pointer index per Manager flag-4 ratification (option c). It does NOT supersede or replace either of the two existing INDEX files; it provides a single entry point that names both.

## Existing INDEX files in this repository

| INDEX file | Path | Purpose |
|---|---|---|
| Active program catalog | `governance/epochs/2026-06-11_lane-1a-prime/INDEX.md` | The active Lane-1a-prime program INDEX. Catalogs every CS-filed governance artifact in the current lane, in chronological order, with sha256 anchors. Includes gate-state line + standing constraints + "where canonical artifacts live" pointer. |
| Tier 0 catalog | `tier0-run/governance/2026-06-09_post-paper2-alignment/INDEX.md` | The tier-0 run-artifact catalog (Qwen2.5-3B-Instruct-mlx-int4 / -int8 + tier-0 governance). |

## Where to look first

- **For Paper A release artifacts** → `/papers/paper-a-before-retention/` (paper + figures + sections + supplement + bundled Paper A governance + revisions/).
- **For the Tier 1 instrument architecture** → `/tier-1-instrument/specs/` (Tool Spec v0.1, G6 Spec v0.1).
- **For the CAL-Q finding track** → `/finding-tracks/cal-q-format-sensitive-abstention/`.
- **For closed D4 history** → `/archive/d4-closed-route/`.
- **For the dated governance epochs** → `/governance/epochs/<date>_*/` (the active program INDEX lives at `epochs/2026-06-11_lane-1a-prime/INDEX.md`).
- **For standing governance** → `/governance/standing/` (north star, program map, hash-integrity standing note, templates, standing non-authorizations).
- **For passdown / onboarding** → `/governance/passdown/` and `/_meta/ONBOARDING-CS.md`.
- **For experiment data (run records, sweep outputs, validation bytes)** → `/experiments/` (sealed bytes inside are DO NOT MOVE).
- **For tier-0 model artifacts** → `/tier0-run/` (categorically SEALED).

## Other repo-level documents

| Document | Path | Purpose |
|---|---|---|
| Project README | `/_meta/README.md` | Top-level project overview. |
| Status | `/_meta/STATUS.md` | Current program status. |
| Review | `/_meta/REVIEW.md` | Review notes. |
| Onboarding (CS) | `/_meta/ONBOARDING-CS.md` | CS Engineer onboarding pointer. |

## Repository organization (v0.4)

The repository is organized per `tier-1-instrument/organization/structure/v0.4.md` (the accepted whole-repo structure). The actual move that placed artifacts here was executed per `tier-1-instrument/organization/move/v0.1.md` on branch `repo-move-v0.1`, with hash verification and sealed-byte protection.

- Move plan: `tier-1-instrument/organization/move/v0.1.md`
- Move authorization: `tier-1-instrument/organization/move/manager-directions/v0.2.md`
- Post-move CS verification: `tier-1-instrument/organization/move/verifications/v0.1.md`

— Pointer maintained by CS Engineer (post-move 2026-06-14)
