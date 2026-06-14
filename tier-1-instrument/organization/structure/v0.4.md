# TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.4

**Version:** v0.4. River and Canyon program. Repository organization plan — WHOLE-REPO coverage. (v0.4 extends the CS-PASSED v0.3 to cover the full inventory; see foot. REVISION CHECK: on every version bump, update the line-1 TITLE and the version block together — title-version lag has recurred.)
**Goal:** extend the accepted v0.3 structure so that **every inventoried artifact category has a clear home** before any file move is authorized. v0.3 mapped the Tier 1 / Paper A / CAL-Q / Paper B / D4 subset cleanly; the first complete inventory found the repository is larger than that map (2,634 in-scope files, multiple categories with no v0.3 destination). v0.4 extends the map to the whole terrain.
**Status:** MODEL-FREE STRUCTURE REVISION. Authorizes no file moves, no directory creation, no renaming, no deletion, no execution. This document proposes organization; it moves no bytes. Sealed bytes DO NOT MOVE. Paper A v1.0, the Tool Spec v0.1, and the G6 spec v0.1 remain the sources of truth. Anchored on origin/main HEAD e960addd.
**Owner split:** Senior (drafter — extend coverage, preserve the v0.3 accepted core) → CS (verify whole-repo coverage, ambiguity resolutions, INDEX correction, and that v0.3 accepted elements are unweakened) → Team Lead (route) → Manager (decides whether to authorize inventory v0.2 against v0.4, then — separately — any move).

---

## 1. Executive summary

v0.3 passed CS verification through three revisions as the organization plan **for the Tier 1 instrument and its immediate neighbors**. The first complete artifact inventory then returned HOLD with a correct finding: the repository contains far more than the four-track subset — older papers (1, 2, 3), B1-harness work, multiple governance epochs, standing and passdown governance, root docs, ancillary directories, and a large body of experiment data (the `experiments/` tree alone is ~2,138 files). None of these had a home under v0.3.

v0.4 keeps the v0.3 routing principle — **one track, one directory tree, no cross-contamination** — and extends it from a five-track subset to a whole-repository map. It adds homes for the eight out-of-scope categories, resolves the sub-directory ambiguities the inventory flagged, and corrects the INDEX location (which is **not** at workspace root, contrary to v0.3). Nothing accepted in v0.3 is weakened; the four-track core is carried forward intact.

This is structure work only. It is not the inventory-v0.2 pass and it is not the move.

## 2. Current state (whole-repo, from the first complete inventory)

```text
TOP-LEVEL (real, observed on origin/main HEAD e960addd):
  root files:   README.md, STATUS.md, REVIEW.md, ONBOARDING-CS.md, .gitignore
  papers/       paper1-survival-is-not-correctness/, paper2-correctness-is-not-
                constructibility/, paper3-certification-before-retention/  (29 files)
                NOTE: Paper A ("before-retention") is NOT yet a directory here — it
                lives in the working library + the paper-a/ GitHub bundle; v0.4
                routes it into papers/ alongside 1/2/3.
  governance/   ~354 files across ~13 dated epochs + standing/ + passdown/
  experiments/  2026-06-09_b1-harness-v2/, 2026-06-10_lane-1a-sweep/,
                2026-06-11_lane-1a-prime/  (~2,138 files — the bulk of the repo)
  tier0-run/    Qwen2.5-3B-Instruct-mlx-int4/, -int8/, governance/  (153 files)
  diagrams/ (14)  notes/ (20)  writing/ (18)  review/ (1)

INDEX (correction to v0.3): there is NO root-level INDEX. Two INDEX files exist:
  - governance/2026-06-11_lane-1a-prime/INDEX.md   (the active program catalog)
  - tier0-run/governance/2026-06-09_post-paper2-alignment/INDEX.md  (a tier0 catalog)

RELEASE-ARTIFACT HASH (carried from v0.3): Paper A release artifact is
  PAPER-A-v1.0.md (bundle paper.md, sha256 4272e12a…; no "-DRAFT-").
```

## 3. Proposed whole-repo directory structure

The v0.3 four-track core is preserved verbatim (marked *). v0.4 adds the rest.

```text
/papers/                                   * + extended
  paper-a-before-retention/                * Paper A release bundle (routed in from library)
  paper1-survival-is-not-correctness/      + existing
  paper2-correctness-is-not-constructibility/   + existing
  paper3-certification-before-retention/   + existing
  README.md                                # paper register: which released, which superseded

/tier-1-instrument/                        * (unchanged from v0.3)
  README.md  ROADMAP.md
  specs/        (eval-validity-gate-tool-spec, g6-standing-rejection-audit-spec)
  schemas/      (route-decision / evidence-packet / quarantine — future lifts; PLACEHOLDER)
  modules/      (g6-standing-rejection-audit/ + G1-G9 register)
  human-read-templates/  (PLACEHOLDER)
  examples/     (PLACEHOLDER)
  implementation/  (PLACEHOLDER — EXPLICITLY NOT A BUILD)
  archive/

/finding-tracks/                           * + room for future tracks
  cal-q-format-sensitive-abstention/       * CAL-Q diagnostic plan (secondary; not D4 rescue)

/paper-b/                                   *
  planning/                                * deferred stress loop (no artifacts; separate auth)

/governance/                               + NEW top-level home for program governance
  standing/                                # standing governance (incl the hash-integrity note pair)
  passdown/                                # passdown governance
  epochs/                                  # the dated governance epochs, by date
    2026-06-09_*/  2026-06-10_*/  2026-06-11_lane-1a-prime/  ...
  README.md                                # what governance is; epoch index; INDEX pointer

/experiments/                              + NEW top-level home for experiment data (the bulk)
  2026-06-09_b1-harness-v2/
  2026-06-10_lane-1a-sweep/
  2026-06-11_lane-1a-prime/                # incl certification_readiness/, sweep_outputs/
  README.md                                # experiment-epoch index; SEALED BYTES — do not move

/tier0-run/                                + NEW top-level home (early tier-0 run artifacts)
  Qwen2.5-3B-Instruct-mlx-int4/  -int8/  governance/

/archive/                                  * + extended
  d4-closed-route/                         * D4 historical evidence only (never reopened)
  superseded/                              # superseded versions across tracks (supersede-don't-delete)

/_meta/                                    + NEW home for repo-level docs + INDEX target
  README.md  STATUS.md  REVIEW.md  ONBOARDING-CS.md   # the root docs (described, see §6)
  INDEX.md                                 # FUTURE root-level INDEX TARGET (does NOT exist yet — §7)
```

## 4. What each NEW directory is for (the v0.3 cores are unchanged; see v0.3 §4)

```text
/papers/ (extended)
    All papers, each in its own subdir. Paper A is routed in from the library/bundle
    to sit beside Papers 1-3. Each paper dir is a finished/maintained release; paper
    GOVERNANCE (release memos, reviews) lives under /governance/epochs/, not here, to
    keep release artifacts separate from the decision record that produced them.

/governance/ (new top-level)
    The program's decision-and-verification record, in three parts:
      standing/   — durable governance that is not epoch-bound, including the
                    "Hash-Integrity Is Not Construct-Validity" standing note (the
                    paper-hash-integrity standing note CS flagged).
      passdown/   — passdown governance (session-to-session handoff record).
      epochs/     — the dated governance epochs (B1-harness plan/merge/lock, Lane-1a
                    authorization, Lane-1a + Lane-1a-prime, Paper 2/3 releases, Paper 3
                    external review + threshold-framework review, scaling discussion).
                    Paper 2/3 governance and B1 governance live here, by date.

/experiments/ (new top-level)
    The experiment data — the bulk of the repo (~2,138 files). Epoch subdirs
    (b1-harness-v2, lane-1a-sweep, lane-1a-prime). This tree is SEALED-BYTES territory:
    run records, sweep outputs, rescore summaries. It is evidence, not editable
    workspace; the do-not-move boundary applies with particular force here.

/tier0-run/ (new top-level)
    Early tier-0 run artifacts (Qwen2.5-3B int4/int8) and their local governance,
    including the second INDEX. Historical run evidence; sealed.

/archive/superseded/ (new under the * archive)
    Superseded versions across ALL tracks (Paper A v0.3-v0.9, superseded structure
    drafts, etc.), retained under supersede-don't-delete. Distinct from
    archive/d4-closed-route/ which is the CLOSED-ROUTE historical evidence specifically.

/_meta/ (new top-level)
    Repo-level documents (README, STATUS, REVIEW, ONBOARDING-CS) and the FUTURE
    root/meta INDEX target. See §6 (root docs) and §7 (INDEX) for exact handling —
    the INDEX does NOT exist here yet and v0.4 does not imply it does.
```

## 5. What artifacts move where (the eight out-of-scope categories + the v0.3 set)

```text
CATEGORY (CS-identified)                          ->  DESTINATION (under v0.4)
[v0.3 set — unchanged]
  Paper A release bundle                          ->  /papers/paper-a-before-retention/
  Tool Spec + G6 spec (FILES)                     ->  /tier-1-instrument/specs/
  G6 module work                                  ->  /tier-1-instrument/modules/g6-.../
  CAL-Q diagnostic plan                           ->  /finding-tracks/cal-q-.../
  D4 historical evidence                          ->  /archive/d4-closed-route/
[1] Papers 1, 2, 3                                 ->  /papers/paper{1,2,3}-.../  (already there)
    paper-hash-integrity standing note             ->  /governance/standing/
[2] Older Lane-1a (governance/2026-06-10_lane1a/)  ->  /governance/epochs/2026-06-10_lane1a/
[3] B1 harness governance + experiments            ->  governance/epochs/<b1-*>/ (governance)
                                                       + /experiments/2026-06-09_b1-harness-v2/ (data)
[4] Paper 2/3 governance                           ->  /governance/epochs/<paper2-*, paper3-*>/
[5] Standing governance (governance/standing/)     ->  /governance/standing/  (path unchanged under tree)
[6] Passdown governance (governance/passdown/)     ->  /governance/passdown/
[7] Root-level docs (README/STATUS/REVIEW/ONBOARD)  ->  /_meta/  (described, see §6)
[8] Ancillary: diagrams/ notes/ writing/ review/    ->  see §6 (kept as working-support dirs)

NOTE: the actual git moves are a SEPARATE, separately-approved step. v0.4 authorizes
neither the move nor directory creation. The complete move requires inventory v0.2
(every one of the 2,634 files routed + hashed) reconciled against THIS structure
before any move authorization.
```

## 6. Ambiguity resolutions (the sub-directory questions CS flagged)

```text
revisions/ , verifications/ , organization/
    These are NOT standalone top-level directories in the current tree; the inventory
    encountered them as RECURRING SUB-STRUCTURE inside governance epochs and artifact
    folders (e.g. a spec's revision history, a CS verification set). RESOLUTION: they
    are routed WITH their parent artifact, not hoisted to their own track — a
    revision/verification of an artifact in /governance/epochs/X/ stays under X. This
    is the "one track, one directory tree" rule applied at the sub-folder level: a
    verification belongs to the thing it verifies.

sweep-bytes relocation
    Sweep run-records/outputs exist in TWO places: governance/2026-06-11_lane-1a-prime/
    certification-readiness/sweep_run_records/ AND experiments/2026-06-11_lane-1a-prime/
    .../sweep_outputs/. RESOLUTION: sweep BYTES (the raw data) are EXPERIMENT artifacts
    -> /experiments/...; the GOVERNANCE that interprets them (rescore summaries cited by
    Paper A, decision records) stays in /governance/epochs/.../. Where a file is
    genuinely both, the governance copy is the citing reference and the experiments copy
    is the source of truth for the bytes; the duplication is RESOLVED AT MOVE TIME by
    inventory v0.2 (which must hash both and record which is canonical), NOT by this doc.
    Relocation of sweep bytes is therefore FLAGGED, not authorized here.

INDEX location
    See §7 (its own section, per Manager direction).

paper-A supplement vs D4 archive duplication risk
    Paper A's supplement cites certification-readiness data (rescore summaries, the
    CAL-Q run record). The same underlying data is D4-lineage and could be claimed by
    BOTH /papers/paper-a-before-retention/supplement/ AND /archive/d4-closed-route/.
    RESOLUTION: the canonical bytes live ONCE — in /experiments/ (source) — and both the
    Paper A supplement and any D4 archive entry REFERENCE them by hash rather than
    duplicating them. Paper A's supplement holds its manifest (with hashes), not copies
    of the run data. Inventory v0.2 must verify no run-data file is physically duplicated
    across /papers/ and /archive/; if duplication exists today, it is recorded and
    de-duplicated AT MOVE TIME, not silently here.

first-compression-rung/ (newly noted; contains INT8 run results)
    governance/2026-06-11_lane-1a-prime/first-compression-rung/ contains int8_run_result
    .json, INT8 per-item tables, and a Senior interpretation. This is COMPRESSION data,
    which is adjacent to Paper B / stress territory — but it is part of the Lane-1a-prime
    HISTORICAL record, not active Paper B work. RESOLUTION (and FLAG for Manager): route
    it as historical Lane-1a-prime evidence under /governance/epochs/2026-06-11_lane-1a-
    prime/ (governance/interpretation) + /experiments/2026-06-11_lane-1a-prime/ (the
    int8 bytes). It is NOT routed into /paper-b/ (that would imply Paper B is active) and
    NOT into /archive/d4-closed-route/ (it is not D4). If the Manager intends this INT8
    rung to seed Paper B, that is a separate decision; v0.4 routes it as history.

diagrams/ notes/ writing/ review/  (ancillary)
    Working-support directories (drafts, sketches, scratch). RESOLUTION: retain as
    top-level working-support dirs OR fold under /_meta/working/ — RECOMMEND retain as-is
    for now and revisit post-move, since they are low-risk and not track-critical. They
    are NOT instrument artifacts and must not be routed into /tier-1-instrument/.
```

## 7. INDEX location clarification (Manager-required; do not assume root-level)

```text
FINDING: v0.3 stated the INDEX "stays at workspace root." That is INCORRECT. There is
no root-level INDEX. The actual INDEX files are:
  - governance/2026-06-11_lane-1a-prime/INDEX.md   — the ACTIVE program catalog
  - tier0-run/governance/2026-06-09_post-paper2-alignment/INDEX.md — a tier0 catalog

RESOLUTION (Manager option 3 — both current and target, with move-time handling):
  - CURRENT: the active INDEX is described accurately at its real location
    (governance/2026-06-11_lane-1a-prime/INDEX.md); the tier0 INDEX stays with tier0-run/.
  - TARGET: a future repo-level INDEX is DEFINED as a target at /_meta/INDEX.md, but
    DOES NOT EXIST YET and v0.4 does not imply it does (it is a PLACEHOLDER target).
  - MOVE-TIME HANDLING: whether to promote the active governance INDEX to /_meta/INDEX.md
    (and how to reconcile the two existing INDEX files) is decided at move time by
    inventory v0.2, NOT here. Until then, the active INDEX remains where it is.
```

## 8. What is explicitly not a build / not a move

```text
- v0.4 is ORGANIZATION. It creates no directory, moves no file, renames nothing,
  deletes nothing, builds no software, runs no model.
- Every NEW directory named in §3 is a PROPOSED target, not a created one.
- /tier-1-instrument/implementation/ remains reserved-empty (EXPLICITLY NOT A BUILD).
- /_meta/INDEX.md is a PROPOSED future target that DOES NOT EXIST (§7).
- The experiments/ and tier0-run/ trees are SEALED BYTES — the do-not-move boundary
  applies with particular force; they are routed (assigned a home) but not moved.
- The eventual move requires inventory v0.2 (all 2,634 files routed + hashed) and a
  separate move authorization.
```

## 9. CS verification checklist

```text
- WHOLE-REPO COVERAGE: that every one of the eight out-of-scope categories (§5) and
  every observed top-level tree (papers/, governance/, experiments/, tier0-run/,
  diagrams/, notes/, writing/, review/, root docs) has exactly one destination, with
  no category left unhomed and none double-homed.
- AMBIGUITY RESOLUTIONS (§6): that revisions/verifications/organization are routed
  with-parent; that sweep-bytes duplication is flagged-not-authorized; that the
  paper-A-supplement vs D4 duplication risk is resolved by reference-not-copy; that
  first-compression-rung is routed as history (not Paper B, not D4).
- INDEX (§7): that v0.4 does NOT claim a root-level INDEX, describes the two real
  INDEX files at their actual locations, and marks /_meta/INDEX.md as a future target
  that does not yet exist.
- V0.3 PRESERVED: that the four-track core, Paper A release home, Tier-1 home, CAL-Q
  separation, Paper B deferred, D4 archive, G6 spec-file-vs-module-dir, placeholder
  honesty, source-of-truth hierarchy, complete-inventory requirement, sealed-bytes
  boundary, and "no file moves until separately approved" are all intact / unweakened.
- NOT-A-BUILD / NOT-A-MOVE: no directory creation, no move, no execution implied;
  closed gates (§10) intact.
```

## 10. Closed gates (extended for v0.4)

```text
No file moves.            No second compression rung.
No directory creation.    No full ladder.
No renaming.              No Claim C activation.
No deletion.              No public benchmark packaging.
No software build.        No funder-facing release.
No model execution.       No SBIR submission.
No new run.               No file moves until separately approved.
No D4 rescue.             No directory creation until separately approved.
No CAL-Q rerun.           No Paper B activation (first-compression-rung routed as history).
No certification run.     Sealed bytes (experiments/, tier0-run/) DO NOT MOVE.
No compression.
No INT8 / INT4 stress.
```

This is structure work only. v0.4 extends the v0.3 map to cover the whole repository so every inventoried category has a home, resolves the flagged ambiguities, and corrects the INDEX location — without weakening anything accepted in v0.3 and without moving a single byte. The next step is CS verification of v0.4; if PASS, inventory v0.2 reconciles all 2,634 files against this structure; only then does a move become a Manager decision.

---

*v0.4 changes (extend v0.3 to whole-repo coverage per Manager direction after the inventory HOLD; no weakening of v0.3): ADDS top-level homes for governance/ (standing + passdown + dated epochs), experiments/ (the ~2,138-file bulk; sealed bytes), tier0-run/, /papers/ extension for Papers 1-3 + Paper A, /archive/superseded/, and /_meta/ (root docs + future INDEX target). ROUTES the 8 out-of-scope categories (§5). RESOLVES the flagged ambiguities (§6): revisions/verifications/organization routed with-parent; sweep-bytes duplication flagged-not-authorized; paper-A-supplement vs D4 duplication resolved by reference-not-copy; newly-noted first-compression-rung INT8 data routed as Lane-1a-prime history (NOT Paper B, NOT D4) with a Manager flag. CORRECTS the INDEX location (§7): no root-level INDEX exists; two real INDEX files described at their actual locations; /_meta/INDEX.md defined as a future target that does not yet exist. PRESERVES verbatim every v0.3 accepted element (four-track core, homes, separations, placeholder honesty, source-of-truth, inventory requirement, sealed-bytes + no-move boundaries). Sealed bytes UNCHANGED; no move, no directory creation, model-free.*
