# CS Verification — Tier 1 Instrument Repo Structure v0.4

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior, Manager
**In response to:** `MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4-VERIFICATION-2026-06-14.md` (Manager direction, this turn — routed via TL).
**Artifact verified:** `governance/2026-06-11_lane-1a-prime/certification-readiness/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4.md` (sha256 `9718ec597abaec0a804e58eacf5ce451c1a86b9a375b657f86573f29a01b2f15`)

---

## §0. Verdict (Manager's return format)

```text
PASS:
  v0.4 covers the whole repo and is safe to use for inventory v0.2.
```

v0.4 extends the v0.3 four-track core to whole-repository coverage without weakening anything accepted in v0.3, routes all eight previously out-of-scope categories the inventory v0.1 HOLD identified, resolves the five flagged sub-directory ambiguities, corrects the INDEX-location error from v0.3 (acknowledging no root-level INDEX exists), preserves source-of-truth hierarchy and sealed-byte boundaries, and implies no move, build, execution, or directory creation. File-move boundary observed: CS moved no file.

---

## §1. Anchor and sealed-bytes posture

Spec §0 anchors on `origin/main HEAD e960addd` — current at draft time (matches my most recent push, the inventory-v0.1 HOLD commit). Sealed bytes UNCHANGED (≈75th survival check):

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`) UNCHANGED.

## §2. Required verification (Manager §"Required verification", items 1–7)

| # | Check | v0.4 evidence | Verdict |
|---|---|---|---|
| 1 | Preserves the accepted v0.3 Tier 1 structure | §3 marks the v0.3 four-track core with `*` (preserved verbatim); §4: "the v0.3 cores are unchanged; see v0.3 §4"; §10 extended closed gates preserve all v0.3 closures including "No file moves until separately approved." | **PASS** |
| 2 | Extends coverage to the whole repository | §3 adds `/governance/` (standing + passdown + epochs), `/experiments/` (~2,138 files SEALED), `/tier0-run/`, `/archive/superseded/`, `/_meta/`; §3 also extends `/papers/` for Papers 1–3 + Paper A; root docs routed; sealed trees routed-but-not-moved. | **PASS** |
| 3 | Routes all eight previously out-of-scope categories | §5 table maps each (see §3 of this verification for per-category PASS). | **PASS** |
| 4 | Resolves the INDEX-location issue | §7 explicit: "v0.3 stated the INDEX 'stays at workspace root.' That is INCORRECT. There is no root-level INDEX." Both real INDEX files named at actual locations; `/_meta/INDEX.md` defined as a future target that "DOES NOT EXIST YET and v0.4 does not imply it does." | **PASS** |
| 5 | Resolves or flags the sub-directory ambiguities | §6 resolves all five: revisions/verifications/organization route with-parent; sweep-bytes relocation flagged-not-authorized; Paper A supplement vs D4 duplication → reference-not-copy; first-compression-rung → Lane-1a-prime history (NOT Paper B, NOT D4); ancillary dirs → kept as working-support, NOT routed into Tier-1. | **PASS** |
| 6 | Preserves sealed-byte boundaries | §3 `/experiments/` README "SEALED BYTES — do not move"; §4 "SEALED-BYTES territory: ... the do-not-move boundary applies with particular force"; §8 "experiments/ and tier0-run/ trees are SEALED BYTES — the do-not-move boundary applies with particular force; they are routed (assigned a home) but not moved"; §10 closed-gate list: "Sealed bytes (experiments/, tier0-run/) DO NOT MOVE." | **PASS** |
| 7 | Implies no file moves / directory creation / execution / build / deletion / renaming | §0/Status: "Authorizes no file moves, no directory creation, no renaming, no deletion, no execution"; §8: "v0.4 is ORGANIZATION. It creates no directory, moves no file, renames nothing, deletes nothing, builds no software, runs no model"; §10 closed-gate list (extended) covers all. | **PASS** |

All seven items: **PASS.**

## §3. Eight out-of-scope categories — Manager §"Eight out-of-scope categories"

| # | Category | v0.4 destination (per §5) | Verdict |
|---|---|---|---|
| 1 | Papers 1, 2, 3 + paper-hash-integrity standing note | `/papers/paper{1,2,3}-…/` (Papers 1–3 in place; Paper A added beside); paper-hash-integrity → `/governance/standing/` | **PASS** |
| 2 | Older Lane-1a work (`governance/2026-06-10_lane1a/`) | `/governance/epochs/2026-06-10_lane1a/` | **PASS** |
| 3 | B1 harness governance + experiments | governance → `/governance/epochs/<b1-*>/`; experiments → `/experiments/2026-06-09_b1-harness-v2/` | **PASS** |
| 4 | Paper 2/3 governance | `/governance/epochs/<paper2-*, paper3-*>/` | **PASS** |
| 5 | Standing governance | `/governance/standing/` (path unchanged) | **PASS** |
| 6 | Passdown governance | `/governance/passdown/` | **PASS** |
| 7 | Root-level docs | `/_meta/` (described in §6 of v0.4) | **PASS** |
| 8 | Ancillary directories (`diagrams/`, `notes/`, `writing/`, `review/`) | §6 RECOMMENDS "retain as-is for now and revisit post-move … NOT instrument artifacts and must not be routed into /tier-1-instrument/" | **PASS** |

All eight: **PASS.**

## §4. Ambiguity checks — Manager §"Ambiguity checks"

| Manager-required resolution | v0.4 §6 evidence | Verdict |
|---|---|---|
| revisions/, verifications/, organization/ route with their parent artifact | "they are routed WITH their parent artifact, not hoisted to their own track — a revision/verification of an artifact in /governance/epochs/X/ stays under X. This is the 'one track, one directory tree' rule applied at the sub-folder level: a verification belongs to the thing it verifies." | **PASS** |
| sweep-byte relocation is flagged, not authorized | "Relocation of sweep bytes is therefore FLAGGED, not authorized here." | **PASS** (verbatim match to Manager's required framing) |
| Paper A supplement vs D4/archive duplication risk handled by reference-not-copy | "the canonical bytes live ONCE — in /experiments/ (source) — and both the Paper A supplement and any D4 archive entry REFERENCE them by hash rather than duplicating them. Paper A's supplement holds its manifest (with hashes), not copies of the run data." | **PASS** |
| first-compression-rung routed as Lane-1a-prime historical evidence, NOT Paper B activation, NOT D4 | "RESOLUTION (and FLAG for Manager): route it as historical Lane-1a-prime evidence under /governance/epochs/2026-06-11_lane-1a-prime/ (governance/interpretation) + /experiments/2026-06-11_lane-1a-prime/ (the int8 bytes). It is NOT routed into /paper-b/ (that would imply Paper B is active) and NOT into /archive/d4-closed-route/ (it is not D4)." | **PASS** (verbatim three-way scoping match) |
| ancillary directories are not routed into the Tier 1 instrument | §6: "They are NOT instrument artifacts and must not be routed into /tier-1-instrument/" | **PASS** |

All five: **PASS.**

## §5. INDEX check — Manager §"INDEX check"

| Manager-required INDEX statement | v0.4 §7 evidence | Verdict |
|---|---|---|
| active program INDEX currently lives at `governance/2026-06-11_lane-1a-prime/INDEX.md` | §7: "governance/2026-06-11_lane-1a-prime/INDEX.md — the ACTIVE program catalog"; §2 also names this path | **PASS** |
| tier0 INDEX lives under `tier0-run/governance/...` | §7: "tier0-run/governance/2026-06-09_post-paper2-alignment/INDEX.md — a tier0 catalog" | **PASS** |
| `/_meta/INDEX.md` is only a future target | §7: "a future repo-level INDEX is DEFINED as a target at /_meta/INDEX.md, but DOES NOT EXIST YET and v0.4 does not imply it does (it is a PLACEHOLDER target)." | **PASS** (verbatim) |
| promotion/reconciliation of INDEX files is a move-time decision | §7: "whether to promote the active governance INDEX to /_meta/INDEX.md (and how to reconcile the two existing INDEX files) is decided at move time by inventory v0.2, NOT here. Until then, the active INDEX remains where it is." | **PASS** (verbatim) |

All four: **PASS.** v0.4 also explicitly removes the v0.3 incorrect claim: §7 "FINDING: v0.3 stated the INDEX 'stays at workspace root.' That is INCORRECT."

## §6. Source-of-truth and boundary checks — Manager §"Source-of-truth and boundary checks"

| Manager-required preservation | v0.4 evidence | Verdict |
|---|---|---|
| Paper A v1.0 remains paper source of truth | §0: "Paper A v1.0 … remain[s] the source[s] of truth"; §2 cites release-artifact hash `4272e12a…` (no -DRAFT-) | **PASS** |
| Tool Spec v0.1 remains Tier 1 architecture source of truth | §0 (above) | **PASS** |
| G6 Spec v0.1 remains G6 module source of truth | §0 (above) | **PASS** |
| schemas remain future lifts from specs | §3 schemas/ "(route-decision / evidence-packet / quarantine — future lifts; PLACEHOLDER)" | **PASS** |
| `/tier-1-instrument/implementation/` remains placeholder only | §3 "(PLACEHOLDER — EXPLICITLY NOT A BUILD)"; §8 "remains reserved-empty (EXPLICITLY NOT A BUILD)" | **PASS** |
| `/paper-b/` remains deferred and inactive | §3 "deferred stress loop (no artifacts; separate auth)"; §10 "No Paper B activation" | **PASS** |
| D4 remains closed historical archive only | §3 "D4 historical evidence only (never reopened)"; §6 first-compression-rung "NOT into /archive/d4-closed-route/ (it is not D4)" | **PASS** |
| CAL-Q remains finding track, not D4 rescue | §3 "CAL-Q diagnostic plan (secondary; not D4 rescue)" | **PASS** |

All eight: **PASS.**

## §7. Closed-gates perimeter (Manager §"Closed gates")

Manager's 20-item closed-gate list vs v0.4 §10:

| Manager-required closure | v0.4 §10 entry | Match |
|---|---|---|
| No file moves | "No file moves." + "No file moves until separately approved." | **Match (2x)** |
| No directory creation | "No directory creation." + "No directory creation until separately approved." | **Match (2x)** |
| No renaming | "No renaming." | **Match** |
| No deletion | "No deletion." | **Match** |
| No software build | "No software build." | **Match** |
| No model execution | "No model execution." | **Match** |
| No new run | "No new run." | **Match** |
| No D4 rescue | "No D4 rescue." | **Match** |
| No CAL-Q rerun | "No CAL-Q rerun." | **Match** |
| No certification run | "No certification run." | **Match** |
| No compression | "No compression." | **Match** |
| No INT8 / INT4 stress | "No INT8 / INT4 stress." | **Match** |
| No second compression rung | "No second compression rung." | **Match** |
| No full ladder | "No full ladder." | **Match** |
| No Claim C activation | "No Claim C activation." | **Match** |
| No public benchmark packaging | "No public benchmark packaging." | **Match** |
| No funder-facing release | "No funder-facing release." | **Match** |
| No SBIR submission | "No SBIR submission." | **Match** |
| No Paper B activation | "No Paper B activation (first-compression-rung routed as history)." | **Match** (with first-compression-rung scoping note) |
| Sealed bytes DO NOT MOVE | "Sealed bytes (experiments/, tier0-run/) DO NOT MOVE." | **Match** |

**20-for-20 verbatim/substantive match.**

## §8. Standard forbidden-phrasings perimeter — PASS

Grep across v0.4 for the standard binding-forbidden phrasings (`model passed` / `capability established` / `candidate certified` / `task family viable` / `Claim C progressed` / `seam evidence` / `public benchmark result` / `certification achieved` / `compression-robust` / `not shortcut-driven` / `breadth passed`): **zero matches.**

## §9. v0.3 → v0.4 preservation sanity-check

v0.4 §3 marks the v0.3 four-track core with `*` and the v0.4 additions with `+`. The four `*` trees (`/papers/paper-a-before-retention/`, `/tier-1-instrument/`, `/finding-tracks/cal-q-format-sensitive-abstention/`, `/paper-b/planning/`, `/archive/d4-closed-route/`) all appear with their v0.3 paths intact. v0.4 §4 explicitly states "the v0.3 cores are unchanged; see v0.3 §4." No element accepted in v0.3 is weakened or contradicted.

Two minor v0.4 corrections to v0.3 that strengthen (rather than weaken) the structure:
- §7 corrects the v0.3 INDEX-location error (root-level INDEX claim).
- §3 adds `/archive/superseded/` as a sibling to `/archive/d4-closed-route/` — distinguishes superseded-version archive (cross-track) from D4-closed-route archive (specific to D4 history). This sharpens v0.3's `/archive/` definition without weakening it.

## §10. File-move boundary observed

Per Manager: "Closed: No file moves. No directory creation. No renaming. No deletion. …"

CS has not moved any file, created any directory, renamed anything, or deleted anything in response to v0.4. This CS verification creates only three documents (Manager direction filed verbatim, v0.4 structure spec filed in `certification-readiness/`, this verification memo) and updates INDEX. No directory created at `/governance/` (as a new top-level), `/experiments/` (no reorganization), `/tier0-run/` (no reorganization), `/archive/superseded/`, or `/_meta/`. **File-move boundary observed.**

v0.1, v0.2, and v0.3 of the structure spec are retained alongside v0.4 (supersede-don't-rewrite). All four versions are tracked.

## §11. Final verdict

```text
PASS:
  v0.4 covers the whole repo and is safe to use for inventory v0.2.
```

**No blockers. No HOLD-worthy issues.** v0.4 cleanly resolves every blocker the inventory v0.1 HOLD raised. The structure can be approved and used as the basis for inventory v0.2.

Per Manager's "Next decision if PASS" note, the next Manager decision is whether to authorize `COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.2`. That inventory v0.2, when produced, will re-run the 2,634-file routing against the v0.4 whole-repo map and either return a clean PASS (every artifact routed without ambiguity) or a smaller HOLD with only those artifacts whose routing is not deterministic from v0.4 (CS expects only sweep-bytes relocation authorization + first-compression-rung Manager flag to remain as decisions, plus any move-time duplication-resolution that inventory v0.2 surfaces).

CS does NOT decide:
- Whether v0.4 is approved as the basis for inventory v0.2 (Manager).
- Whether to authorize `COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.2` (Manager — next decision per direction).
- The first-compression-rung disposition (Manager flag in v0.4 §6 — CS reads as appropriately scoped; Manager may want to ratify the "Lane-1a-prime history, not Paper B, not D4" routing explicitly).
- The eventual move authorization (still a separate later step after inventory v0.2).

— CS Engineer, 2026-06-14
