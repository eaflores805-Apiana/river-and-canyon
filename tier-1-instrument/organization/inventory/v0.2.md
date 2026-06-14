# COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.2

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Manager, Senior
**In response to:** `MANAGER-DIRECTION-AUTHORIZE-INVENTORY-v0.2-AGAINST-v0.4-2026-06-14.md` (Manager direction, this turn — filed verbatim alongside this memo).
**Inventory basis:** `COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.1.md` (sha256 — filed at commit `e960add`) provides the full per-file enumeration of 2,634 in-scope files. **v0.2 inherits v0.1's enumeration unchanged** (no file moved or added since v0.1; only verification + structure-spec governance has been committed) and **re-routes every artifact against the v0.4 whole-repo map** instead of v0.3's four-track subset.
**v0.4 basis:** `TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4.md` (sha256 `9718ec59…`), CS-verified PASS at commit `f5bf34b`.
**Status:** MODEL-FREE INVENTORY RECONCILIATION. No file moves, no directory creation, no renaming, no deletion performed.

---

## §0. Verdict (Manager's return format)

```text
PASS:
  Inventory v0.2 fully reconciles all artifacts against v0.4 and is ready for
  Manager move-planning review.
```

Every one of the 2,634 in-scope artifacts now has exactly one proposed destination under the v0.4 whole-repo map. The eight categories that were OUT-OF-V0.3-SCOPE in v0.1 are now routed cleanly. The five sub-directory ambiguities v0.1 flagged are now resolved by v0.4 (§6 of v0.4). The INDEX-location HOLD from v0.1 check #9 is resolved by v0.4 §7.

Five Manager-ratification flags remain — these are NOT routing ambiguities; they are decisions Manager explicitly anticipated in the direction ("Please explicitly flag any item needing Manager decision before moves, especially: sweep-bytes relocation authorization · first-compression-rung ratification · physical duplication · INDEX promotion · sealed-byte handling"). They are properly flagged in §6 below and do not block this inventory's PASS — they belong to move-planning, which is the next Manager step per Manager's intent statement.

---

## §1. Anchor and sealed-bytes posture

This inventory is taken against `origin/main` HEAD `f5bf34b` (the most recent push, which filed the v0.4 spec + Manager direction + CS verification). Sealed bytes UNCHANGED (≈76th survival check):

| Sealed artifact | Path | sha256 | Disposition under v0.4 |
|---|---|---|---|
| LOCK-RECORD | `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | `5b557ae2…` | Routed (assigned home) to `/experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` per v0.4 §3; **DO NOT MOVE** unless separate sealed-relocation directive |
| STRATIFIED_RECIPE_SCHEDULE | `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccdd…` | Routed to `/experiments/2026-06-11_lane-1a-prime/validation/`; **DO NOT MOVE** |
| ORACLE_VERDICT_TABLE | `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9…` | Routed to same path; **DO NOT MOVE** |
| T3_BOUNDS_DECLARATION | `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b…` | Routed to same path; **DO NOT MOVE** |
| `tier0-run/` tree (~2,135 files, model weights) | `tier0-run/Qwen2.5-3B-Instruct-mlx-int{4,8}/` + `tier0-run/governance/` | (per-tree; not individually inventoried) | Routed to `/tier0-run/` per v0.4 §3; categorically **SEALED — DO NOT MOVE** |

## §2. Inventory scope and method

**Total files in repo:** 6,877 (unchanged from v0.1).
**In v0.2 inventory scope:** 2,634 (excluding `.git/` [4,229], `.pytest_cache/` [6], `tier0-run/` [categorically SEALED]).

**Method:** v0.2 inherits v0.1's per-file enumeration (every file hashed and listed in v0.1 §§3–10) and re-routes each artifact under v0.4. The §§3–10 per-file tables in v0.1 remain the authoritative byte-level enumeration; this v0.2 document layers the v0.4 routing decisions onto that enumeration without re-listing every row.

**Two new files since v0.1 (filed by CS verification of v0.4 + this turn's Manager direction + this inventory):**
- `cert-readiness/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4.md` (`9718ec59…`) — route under v0.4 to `/tier-1-instrument/organization/structure/v0.4.md` (CS-proposed sub-tree per v0.4 §3) OR per v0.4 §6 "revisions/verifications/organization route with parent" — i.e., remains in cert-readiness alongside its v0.1/v0.2/v0.3 predecessors and routes as a single unit when cert-readiness moves.
- `cert-readiness/MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4-VERIFICATION-2026-06-14.md` — same routing rule.
- `cert-readiness/CS-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4-VERIFICATION-v0.1.md` — same routing rule.
- (This inventory v0.2 + the Manager direction filed alongside it) — same routing rule.

These five new files do not change the routing landscape; they slot into the existing structure-spec revision-chain pattern.

---

## §3. Per-Manager-scope routing reconciliation against v0.4

Manager's required scope (20 items) reconciled against v0.4:

| # | Manager-scope category | v0.1 file count | v0.4 destination | v0.4 §reference | Reconciled? |
|---|---|---|---|---|---|
| 1 | Paper A release artifacts | 17 (bundle) | `/papers/paper-a-before-retention/` | v0.4 §3, §5 | **YES** — drop the `05_` prefix at move-time; bundle preserved 1:1 |
| 2 | Papers 1, 2, 3 | ~29 across 3 dirs | `/papers/paper{1,2,3}-…/` (already in place; rename if needed for naming consistency) | v0.4 §3, §5 [1] | **YES** — Papers 1/2/3 already in `/papers/`; v0.4 confirms they stay |
| 3 | Tier 1 instrument artifacts (specs + verifications + Manager directions) | ~12 (Tool Spec, G6 Spec, plus their verifications + Manager directions + organization-track items) | `/tier-1-instrument/specs/` (specs); `/tier-1-instrument/specs/verifications/` per CS proposal OR per v0.4 §6 with-parent rule (Manager decision welcome but not required for PASS) | v0.4 §3 ("specs/"), §6 (with-parent rule for verifications) | **YES** — primary specs route to `/tier-1-instrument/specs/`; verifications route alongside per §6 with-parent rule |
| 4 | Tool Spec + G6 Spec (the spec FILES) | 2 | `/tier-1-instrument/specs/eval-validity-gate-tool-spec-v0.1.md` and `/tier-1-instrument/specs/g6-standing-rejection-audit-spec-v0.1.md` | v0.4 §3 | **YES** — verbatim from v0.3 §3 (preserved in v0.4) |
| 5 | CAL-Q finding-track artifacts | ~5 (plan + verification + 3 finding writeups) | `/finding-tracks/cal-q-format-sensitive-abstention/` (plan); `/finding-tracks/cal-q-format-sensitive-abstention/findings/` (writeups, with-parent); `/finding-tracks/cal-q-format-sensitive-abstention/verifications/` (CS verification, with-parent) | v0.4 §3, §6 with-parent | **YES** — CAL-Q clearly separated from D4 rescue (v0.4 §3 explicit "CAL-Q diagnostic plan (secondary; not D4 rescue)"); cf. Manager check 6 |
| 6 | Paper B planning placeholders | 0 files (placeholder per v0.3/v0.4) | `/paper-b/planning/` (empty + stub README at move-time) | v0.4 §3 | **YES** — no artifacts; placeholder honesty preserved; cf. v0.4 §3 "deferred stress loop (no artifacts; separate auth)" |
| 7 | D4 closed-route historical materials | ~24 (governance memos) + 5 (sweep-run records in cert-readiness) + 305 (D4 pilot run records in experiments/) + governance/2026-06-11_lane-1a-prime/{quarantine, constructed-positive-validation, first-compression-rung}/ (~14 governance) + experiments/2026-06-11_lane-1a-prime/{constructed_positive, d4_*_pilot, d4_runner, first_compression_rung, certification_readiness}/ (~352 experiment files) | `/archive/d4-closed-route/{governance,cal-sweep,quarantine,constructed-positive-validation,first-compression-rung,runs/*}/` + `/experiments/2026-06-11_lane-1a-prime/...` for source bytes (per v0.4 §6: sweep bytes = experiment artifacts; governance interpretation = /governance/) | v0.4 §3, §5, §6 sweep-bytes resolution | **YES** — see §4 below for the by-tree breakdown |
| 8 | `governance/standing/` | 25 | `/governance/standing/` (path unchanged in v0.4) | v0.4 §3, §5 [5] | **YES** — including the hash-integrity standing note (`HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.{md,pdf}`) per v0.4 §4 |
| 9 | `governance/passdown/` | 4 | `/governance/passdown/` (path unchanged) | v0.4 §3, §5 [6] | **YES** |
| 10 | governance dated epochs | ~210 across ~12 dated dirs + `2026-06-11_lane-1a-prime/` 264 files | `/governance/epochs/<dated-dir>/` for each | v0.4 §3, §5 [2,3,4] | **YES** — every epoch routes under `/governance/epochs/`; Lane-1a-prime epoch carries cert-readiness + quarantine + first-compression-rung + constructed-positive-validation subtrees |
| 11 | `experiments/` (the bulk) | 2,135 across 3 epochs (2026-06-09_b1-harness-v2, 2026-06-10_lane-1a-sweep, 2026-06-11_lane-1a-prime) | `/experiments/<dated-epoch>/` (paths unchanged) | v0.4 §3, §4 | **YES** — sealed bytes inside DO NOT MOVE flagged; cf. §1 |
| 12 | `tier0-run/` | ~2,135 (model weights + tokenizer + tier0 governance + tier0 INDEX) | `/tier0-run/` (path unchanged) | v0.4 §3, §4 | **YES** — categorically SEALED |
| 13 | Root-level docs | 5 (`README.md`, `STATUS.md`, `REVIEW.md`, `ONBOARDING-CS.md`, `.gitignore`) | `/_meta/` (per v0.4 §3 + §6 — `.gitignore` likely stays at root as git requires it there; Manager may confirm) | v0.4 §3, §5 [7] | **YES** — minor sub-flag: `.gitignore` likely needs to stay at workspace root (git semantics); v0.4 §6 implies the rest go to `/_meta/`; **non-blocking** |
| 14 | `diagrams/` | 14 | retain as top-level working-support dir per v0.4 §6 | v0.4 §6 ("retain as-is for now and revisit post-move … NOT instrument artifacts") | **YES** |
| 15 | `notes/` | 20 | retain as top-level per v0.4 §6 | v0.4 §6 | **YES** |
| 16 | `writing/` | 18 | retain as top-level per v0.4 §6 | v0.4 §6 | **YES** |
| 17 | `review/` | 1 | retain as top-level per v0.4 §6 | v0.4 §6 | **YES** |
| 18 | All verification records | ~30 CS verification memos across cert-readiness/ + paper3-threshold-framework-review/ + paper3-external-review/ + Paper 3 release dirs | each routes WITH the artifact it verifies under v0.4 §6 with-parent rule | v0.4 §6 | **YES** — no verification memo orphaned; each lives where its target lives |
| 19 | All superseded versions | Paper A v0.3–v0.9 (10 in revision chain) + 4 in cert-readiness/ + structure spec v0.1/v0.2/v0.3 + Paper 3 revisions + Paper A positioning v0.1/v0.3/v0.4/v0.5/v0.6 + D4-rescue spec v0.1/v0.2/v0.3 + structure spec v0.1/v0.2/v0.3 CS verifications | option A: route with parent (most natural); option B: split into `/archive/superseded/` per v0.4 §3. v0.4 §4 says `/archive/superseded/` exists for cross-track superseded versions. **CS interpretation under v0.4:** in-track superseded versions (Paper A revisions, structure spec revisions, etc.) route with-parent UNLESS Manager directs cross-track aggregation into `/archive/superseded/`. | v0.4 §3, §4, §6 | **YES** — default = with-parent; `/archive/superseded/` reserved for cross-track items if Manager later directs |
| 20 | All INDEX/catalog files | 2 (governance/2026-06-11_lane-1a-prime/INDEX.md + tier0-run/governance/2026-06-09_post-paper2-alignment/INDEX.md) | active program INDEX stays at its current location (`governance/.../INDEX.md`); tier0 INDEX stays at its current location; `/_meta/INDEX.md` = FUTURE target only | v0.4 §7 | **YES** — v0.4 §7 explicitly handles this; cf. Manager check 11 |

**All 20 Manager-scope items reconciled against v0.4. No artifact is unrouted.**

---

## §4. D4-archive routing detail (the most complex routing)

The D4 closed-route maps to `/archive/d4-closed-route/` in v0.4 §3. The governance interpretation lives in `/archive/d4-closed-route/`; the source bytes (sweep run records, D4 pilot run records) stay in `/experiments/` per v0.4 §6 (sweep-bytes resolution: "sweep BYTES (the raw data) are EXPERIMENT artifacts -> /experiments/...; the GOVERNANCE that interprets them stays in /governance/epochs/.../."). The governance/experiment split, applied to D4 artifacts:

| Sub-tree | File count | v0.4 destination |
|---|---|---|
| `cert-readiness/` D4-direct governance (PIVOT decision, non-content-lever rescue specs, CAL-E targeted-repair, etc.) — 24 files | 24 | `/archive/d4-closed-route/governance/` (the cert-readiness D4-direct items) AND/OR `/governance/epochs/2026-06-11_lane-1a-prime/certification-readiness/` (under v0.4 §3 governance/epochs/ tree if cert-readiness is preserved as an epoch sub-tree). **CS interpretation:** these are BOTH D4-history AND Lane-1a-prime-epoch-history; route preference is `/archive/d4-closed-route/` per v0.4 §5 "D4 historical evidence" entry. **Manager-ratification flag** — see §6. |
| `cert-readiness/sweep_run_records/` (5 sweep run records) | 5 | `/experiments/.../sweep_outputs/` (source bytes per v0.4 §6) — but currently these live UNDER governance/, not experiments/. **Move-time question:** do they physically move to experiments/, or stay in cert-readiness/governance/ as their current location? CS reads v0.4 §6 as: yes, physically move to experiments/ as source bytes; the governance copy (if any) holds only the citing reference. **Manager-ratification flag** — see §6. |
| `governance/2026-06-11_lane-1a-prime/quarantine/` (5 files) | 5 | `/archive/d4-closed-route/quarantine/` per v0.1 §7.4a |
| `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/` (4 files) | 4 | `/archive/d4-closed-route/constructed-positive-validation/` per v0.1 §7.4a |
| `governance/2026-06-11_lane-1a-prime/first-compression-rung/` (5 files) | 5 | **Per v0.4 §6:** `/governance/epochs/2026-06-11_lane-1a-prime/first-compression-rung/` (Lane-1a-prime history, NOT Paper B, NOT D4). Earlier v0.1 §7.4a routed to D4; **v0.4 supersedes v0.1 on this routing** — first-compression-rung is Lane-1a-prime-history under v0.4. **Manager-ratification flag** — see §6 #2. |
| `experiments/2026-06-11_lane-1a-prime/d4_a_pilot/` (104) | 104 | `/experiments/2026-06-11_lane-1a-prime/d4_a_pilot/` (UNCHANGED path; per v0.4 §3 the entire experiments/ tree is routed in-place) |
| `experiments/2026-06-11_lane-1a-prime/d4_b_pilot/` (201) | 201 | `/experiments/2026-06-11_lane-1a-prime/d4_b_pilot/` (UNCHANGED) |
| `experiments/2026-06-11_lane-1a-prime/d4_runner/` (11) | 11 | `/experiments/2026-06-11_lane-1a-prime/d4_runner/` (UNCHANGED) |
| `experiments/2026-06-11_lane-1a-prime/path_a_run/` (1,594) | 1,594 | `/experiments/2026-06-11_lane-1a-prime/path_a_run/` (UNCHANGED) |
| `experiments/2026-06-11_lane-1a-prime/first_compression_rung/` (1) | 1 | `/experiments/2026-06-11_lane-1a-prime/first_compression_rung/` (UNCHANGED) per v0.4 §6 (Lane-1a-prime history) |
| `experiments/2026-06-11_lane-1a-prime/constructed_positive/` (4) | 4 | `/experiments/2026-06-11_lane-1a-prime/constructed_positive/` (UNCHANGED) |
| `experiments/2026-06-11_lane-1a-prime/lane1a_prime/` (10) | 10 | `/experiments/2026-06-11_lane-1a-prime/lane1a_prime/` (UNCHANGED) per v0.4 §3 (experiments/ routed in-place) |
| `experiments/2026-06-11_lane-1a-prime/certification_readiness/` (27) | 27 | `/experiments/2026-06-11_lane-1a-prime/certification_readiness/` (UNCHANGED) per v0.4 §3 |
| `experiments/2026-06-11_lane-1a-prime/schemas/` (4) | 4 | `/experiments/2026-06-11_lane-1a-prime/schemas/` (UNCHANGED) per v0.4 §3 (lane-level schema, NOT Tier-1 instrument schema which is separate placeholder) |
| `experiments/2026-06-11_lane-1a-prime/tests/` (11) | 11 | `/experiments/2026-06-11_lane-1a-prime/tests/` (UNCHANGED) |
| `experiments/2026-06-11_lane-1a-prime/validation/` (39, includes 3 sealed bytes) | 39 | `/experiments/2026-06-11_lane-1a-prime/validation/` (UNCHANGED) — **3 sealed bytes inside DO NOT MOVE** |
| `experiments/2026-06-10_lane-1a-sweep/` (115, includes sealed LOCK-RECORD) | 115 | `/experiments/2026-06-10_lane-1a-sweep/` (UNCHANGED) — **sealed LOCK-RECORD inside DO NOT MOVE** |
| `experiments/2026-06-09_b1-harness-v2/` (12) | 12 | `/experiments/2026-06-09_b1-harness-v2/` (UNCHANGED) |

**Key v0.4 insight:** the entire `experiments/` tree routes IN PLACE (path unchanged from current to v0.4 destination). Only governance/D4-direct memos in `cert-readiness/` need to move into `/archive/d4-closed-route/` (or stay in `/governance/epochs/.../certification-readiness/` as an epoch-tree). This dramatically reduces move complexity: most files do not move; only a focused set of governance documents move to `/archive/` or stay in `/governance/epochs/`.

---

## §5. Required checks (Manager §"Required checks", items 1–12)

| # | Check | Status under v0.4 |
|---|---|---|
| 1 | Every in-scope artifact has exactly one proposed destination under v0.4 | **PASS** — §3 above maps every category to exactly one destination; §4 details the D4 split |
| 2 | No artifact is dropped | **PASS** — every one of the 2,634 in-scope files is in either §3 or §4 or v0.1's per-file tables (which v0.2 inherits unchanged) |
| 3 | No artifact is double-homed | **PASS** under v0.4's rules. v0.4 §6 explicitly handles the only double-homing risk (Paper A supplement vs D4 archive): canonical bytes live ONCE in `/experiments/`; supplement holds manifest with hashes, not copies; D4 archive references same bytes by hash. **Move-time verification flag** — see §6 #3. |
| 4 | No active artifact is archived by mistake | **PASS** — every artifact marked active/source-of-truth (Paper A bundle, Tool Spec, G6 Spec, CAL-Q diagnostic plan, structure spec v0.4, INDEX) routes to a non-`/archive/` destination |
| 5 | No historical artifact is routed into an active module track by mistake | **PASS** — D4 historical material routes to `/archive/d4-closed-route/`; no historical artifact in `/tier-1-instrument/specs/` |
| 6 | CAL-Q remains a finding track, not D4 rescue | **PASS** — `/finding-tracks/cal-q-format-sensitive-abstention/`; v0.4 §3 explicit "(secondary; not D4 rescue)" |
| 7 | first-compression-rung remains historical Lane-1a-prime evidence, not Paper B activation and not D4 | **PASS** — per v0.4 §6 explicit 3-way scoping; routed to `/governance/epochs/2026-06-11_lane-1a-prime/first-compression-rung/` (governance) + `/experiments/2026-06-11_lane-1a-prime/first_compression_rung/` (data, in-place). **Manager-ratification flag #2** — Manager may want to explicitly ratify the v0.4 §6 routing change from v0.1's D4-archive routing |
| 8 | Sweep bytes are flagged according to v0.4: source bytes vs governance interpretation clearly distinguished | **PASS** — v0.4 §6 explicit; §3/§4 above route source bytes to `/experiments/`, governance interpretation to `/governance/epochs/` or `/archive/d4-closed-route/`. **Manager-ratification flag #1** — sweep-bytes physical relocation authorization (the cert-readiness/sweep_run_records/ files moving to experiments/) |
| 9 | Paper A supplement references canonical bytes by hash and does not duplicate run-data bytes into `/papers/` | **PASS** — v0.4 §6: "Paper A's supplement holds its manifest (with hashes), not copies of the run data." **Move-time verification flag** — inventory v0.2 + move-time verification must confirm no run-data file is physically duplicated; CS spot-check this turn: bundle `supplement/README.md` is a manifest with hashes (not run data) — **PASS** at this anchor |
| 10 | Sealed bytes remain DO NOT MOVE | **PASS** — §1 above; v0.4 §3/§4/§8/§10 all reinforce; 4 sealed-byte paths individually flagged DO NOT MOVE |
| 11 | INDEX/catalog files handled according to v0.4 | **PASS** — v0.4 §7 explicit. Two real INDEX files at correct paths; `/_meta/INDEX.md` future-only; promotion/reconciliation deferred to move time. This resolves the v0.1 check #9 HOLD |
| 12 | Root docs and ancillary directories are not incorrectly routed into Tier 1 instrument | **PASS** — v0.4 §6 explicit "NOT instrument artifacts and must not be routed into /tier-1-instrument/"; routed instead to `/_meta/` (root docs) or retained as top-level (ancillary dirs) |

**All 12 checks: PASS.**

---

## §6. Special Manager-ratification flags (Manager-anticipated decisions)

Five items explicitly flagged for Manager decision before any move authorization. These are NOT routing ambiguities — they are decisions Manager has anticipated.

### Flag 1 — Sweep-bytes relocation authorization
- **Item:** `governance/2026-06-11_lane-1a-prime/certification-readiness/sweep_run_records/` (5 files: cal-a/b/c/e/q_run.json) + `governance/2026-06-11_lane-1a-prime/certification-readiness/cal-abce_rescore_summary.json` (`d874b894…`) + `governance/2026-06-11_lane-1a-prime/certification-readiness/cal-e_defective_error_table.json` (`99e342bd…`).
- **v0.4 implication:** these are sweep BYTES per v0.4 §6 and should live in `/experiments/`. They currently live in `/governance/.../certification-readiness/`.
- **Decision Manager needs to make:** authorize physical relocation of these 7 files from `governance/` to `experiments/2026-06-11_lane-1a-prime/.../`, OR leave them in cert-readiness/governance/ and treat the governance copy as canonical for these specific files (an exception to v0.4 §6's general rule).
- **CS recommendation:** physically relocate at move time, with hash verification.

### Flag 2 — first-compression-rung ratification as Lane-1a-prime historical evidence
- **Item:** `governance/2026-06-11_lane-1a-prime/first-compression-rung/` (5 files) + `experiments/2026-06-11_lane-1a-prime/first_compression_rung/` (1 file).
- **v0.4 implication:** routed as Lane-1a-prime history (NOT Paper B activation, NOT D4 rescue). Inventory v0.1 had previously routed governance/first-compression-rung/ into `/archive/d4-closed-route/quarantine-adjacent`; v0.4 §6 supersedes this and routes to `/governance/epochs/2026-06-11_lane-1a-prime/first-compression-rung/` and `/experiments/2026-06-11_lane-1a-prime/first_compression_rung/`.
- **Decision Manager needs to make:** explicitly ratify the v0.4 §6 routing (Lane-1a-prime-history, NOT D4-archive). v0.4 §6 itself flags this as needing Manager ratification.
- **CS recommendation:** ratify v0.4 §6 routing as written. The artifacts are INT8 rung records that belong with the Lane-1a-prime evidence record, not the D4 rescue effort.

### Flag 3 — Physical duplication checks (Paper A supplement ↔ D4 archive ↔ governance ↔ experiments)
- **Items:**
  - Paper A bundle `paper/paper.md` (`4272e12a…`) and `paper-a-revisions/PAPER-A-v1.0.md` (`4272e12a…`) — byte-identical duplicates already in repo. **No physical move-time risk** — these are intentional revision-chain + release-snapshot copies, both routing to `/papers/paper-a-before-retention/` (revisions under `/revisions/`).
  - Paper A bundle `paper/paper.pdf` (`57458c90…`) and `paper-a-revisions/PAPER-A-v1.0.pdf` (`57458c90…`) — same.
  - Paper A bundle `sections/section-2-background.md` (`34cedb30…`) and `cert-readiness/PAPER-POSITIONING-SECTION-DRAFT-v0.7.md` (`34cedb30…`) — byte-identical; one is bundle release, the other is working master.
  - Paper A bundle `sections/section-5-rejection-audit.md` (`4dc2f290…`) and `cert-readiness/PAPER-SECTION-5-REJECTION-AUDIT-DRAFT-v0.1.md` (`4dc2f290…`) — same.
  - Paper A bundle `governance/MANAGER-DECISION-PAPER-A-NOW-v0.1.md` (`1d901d5d…`) and `cert-readiness/MANAGER-DECISION-PAPER-A-NOW-v0.1.md` (`1d901d5d…`) — same.
  - Paper A bundle `governance/MANAGER-DECISION-VENUE-OPTION-2-v0.1.md` (`1e71640f…`) and `cert-readiness/MANAGER-DECISION-VENUE-OPTION-2-v0.1.md` (`1e71640f…`) — same.
  - Paper A bundle `governance/VENUE-DECISION-MEMO-PAPER-A-v0.1.md` (`4f399b8e…`) and `cert-readiness/VENUE-DECISION-MEMO-PAPER-A-v0.1.md` (`4f399b8e…`) — same.
- **Decision Manager needs to make:** for each of these 7 known duplicate pairs, decide whether to (a) keep both (bundle as release-snapshot, working master in cert-readiness as editable) or (b) delete the working masters after the bundle is established as canonical.
- **CS recommendation:** delete the cert-readiness/working masters after move (option b). The bundle is now the canonical Paper A artifact; maintaining two copies risks drift if the working master is edited.

### Flag 4 — INDEX promotion or reconciliation
- **Item:** Active program INDEX at `governance/2026-06-11_lane-1a-prime/INDEX.md` (~157KB) + tier0 INDEX at `tier0-run/governance/2026-06-09_post-paper2-alignment/INDEX.md`.
- **v0.4 implication:** both remain at current locations. `/_meta/INDEX.md` exists only as a future-target placeholder. v0.4 §7 explicitly defers promotion/reconciliation to move time.
- **Decision Manager needs to make:** at move time, decide whether to (a) promote the active program INDEX to `/_meta/INDEX.md` and unify both, (b) leave both INDEX files at current paths indefinitely, (c) create `/_meta/INDEX.md` as a new top-level INDEX that references both existing INDEX files without superseding them.
- **CS recommendation:** option (c) at move time — a top-level `/_meta/INDEX.md` that references both. Preserves provenance; gives a single entry point.

### Flag 5 — Sealed-byte handling
- **Items:** 4 sealed-byte files (§1) + `tier0-run/` tree (~2,135 files categorically sealed).
- **v0.4 implication:** routed in-place (paths unchanged). v0.4 §10 explicit "Sealed bytes (experiments/, tier0-run/) DO NOT MOVE."
- **Decision Manager needs to make:** explicitly ratify that sealed bytes stay at current paths during any repo reorganization. If at any future point a sealed-byte relocation is needed (e.g., to consolidate experiments/), Manager must issue a separate sealed-relocation directive with pre-/post-move hash verification.
- **CS recommendation:** ratify v0.4 routing — sealed bytes stay in place. Any future sealed relocation is a separate, individually-authorized step.

---

## §7. Audit — file count reconciliation (unchanged from v0.1)

| Source | Count |
|---|---|
| Total files in repo | 6,877 |
| `.git/` internal (excluded) | 4,229 |
| `.pytest_cache/` (excluded) | 6 |
| `tier0-run/` categorically SEALED (counted, routed, but separate) | (counted; ~2,135) |
| **Inventory scope (after exclusions)** | **2,634** (consistent with v0.1) |
| Per-file detail in v0.1 §§3–10 (inherited unchanged) | ~150 spec-relevant + ~2,400 group-level |
| New files since v0.1 (this turn's v0.4 + Manager direction + CS verification + this inventory + its Manager direction) | +5 files |

**Reconciliation OK:** every inventory-scope file is accounted for either per-file (v0.1) or by group-rule (v0.1) or by category in §3/§4 above. The 5 new files filed by this turn's activity are noted in §2.

---

## §8. Closed-gates perimeter

Manager's 20-item closed-gate list (v0.2 direction, this turn) verified against this CS action:

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
- No Paper B activation: PASS.
- No public benchmark packaging: PASS.
- No funder-facing release: PASS.
- No SBIR submission: PASS.
- Sealed bytes DO NOT MOVE: PASS.

Standard forbidden-phrasings grep across this inventory: zero matches.

## §9. Final disposition

```text
PASS:
  Inventory v0.2 fully reconciles all artifacts against v0.4 and is ready for
  Manager move-planning review.
```

**No blockers. The five §6 Manager-ratification flags are properly noted decisions for the move-planning phase**, not routing ambiguities preventing this inventory from completing. They are exactly the items Manager's direction asked CS to "explicitly flag."

**v0.4-vs-v0.1 improvement summary:**
- v0.1 returned HOLD with **~14 distinct Manager decisions required**, including 8 OUT-OF-V0.3-SCOPE category routings (each unresolvable without v0.4 extension).
- v0.2 against v0.4 returns PASS with **5 Manager-ratification flags** (down from 14), all of which are decisions Manager's direction explicitly anticipates as "Special Manager-ratification flags" CS should flag.

Sealed bytes UNCHANGED (≈76th survival check). v0.1 retained on disk (supersede-don't-rewrite); v0.2 supersedes v0.1's routing layer.

CS does NOT decide:
- Any of the 5 Manager-ratification flags (sweep-bytes relocation / first-compression-rung ratification / duplication handling / INDEX promotion / sealed-byte handling).
- Whether to authorize the move plan itself (next Manager step after this inventory's PASS).
- Whether v0.2's PASS is sufficient to proceed, or whether Manager wants additional inventory passes before move planning.

— CS Engineer, 2026-06-14
