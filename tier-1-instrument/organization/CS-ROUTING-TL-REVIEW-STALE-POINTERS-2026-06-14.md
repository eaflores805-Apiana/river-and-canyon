# CS Routing — TL Repo Review: Stale-Pointer Cleanup (Senior + Manager scope)

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior (for PROGRAM-POSITION anchor refresh) + Manager (for PROGRAM-MAP-v2.0 companion-pointer refresh).
**Status:** CS executes one of three TL-flagged stale-pointer fixes (the README, CS-scope); surfaces the other two to TL because they touch documents that are not CS-scope to edit unilaterally. No model execution, no claim change, sealed bytes UNCHANGED.

---

## §1. What TL flagged

TL's repo review (this turn) identified three stale-pointer issues, all "scientific issues 0 / hygiene 3" in TL's framing:

1. **README** — Hash Integrity section still said *"figures in `governance/standing/figures/`"* despite the figures having moved with the note to `papers/standing-notes/hash-integrity-is-not-construct-validity-v0.7.2/figures/` (commit `fd9f653`). Real pointer mismatch.
2. **PROGRAM-POSITION-v0.1** — anchored at `origin/main 6a4e604`; current HEAD is several commits later (now `9f0b3587` as of last commit). The document explicitly says *"if this and the record disagree, the record wins and this is stale — re-sync."* So the anchor needs a refresh.
3. **PROGRAM-MAP-v2.0** — companion pointer at line 6 says *"Companions: NORTH-STAR-v1.1.md (the standard)…"* and §"How they fit together" at line 34 says *"North Star v1.1: the standing standard…"* — both stale since NORTH-STAR-v1.2 was filed (commit `292b478`). Pointer-only; no scientific claim depends on the version.

## §2. CS disposition of the three issues by scope

| # | Issue | Scope | CS action |
|---|---|---|---|
| 1 | README Hash Integrity figure path | **CS-scope** (root-facing live doc; CS has been editing it throughout this session for path updates: figure-rendering fix, Paper-A rename revert, Hash Integrity relocation, etc.) | **Executed in this commit** — changed "figures in `governance/standing/figures/`" → "figures alongside in `figures/`" (parallel to how Paper 2/3 describe their bundled-figure locations) |
| 2 | PROGRAM-POSITION-v0.1 anchor refresh | **Senior-scope** (per program convention: PROGRAM-POSITION is maintained by Senior; CS does not update unilaterally; recorded in CS memory `feedback_apiana_program_position` from a past violation) | **Surfaced to TL → Senior** below |
| 3 | PROGRAM-MAP-v2.0 companion pointer | **Manager-scope** (PROGRAM-MAP is a Manager-owned standing doc per its own header convention; CS does not edit Manager-owned standing docs in place) | **Surfaced to TL → Manager** below |

## §3. CS action this commit (Issue 1)

Single one-line edit in `README.md` line 42:

```diff
- → [`papers/.../HASH-INTEGRITY-...-v0.7.2.md`](...) — Markdown and PDF; figures in `governance/standing/figures/`.
+ → [`papers/.../HASH-INTEGRITY-...-v0.7.2.md`](...) — Markdown and PDF; figures alongside in `figures/`.
```

The phrasing "figures alongside in `figures/`" matches Paper 2/3's bundle-figure convention. The figures live at `papers/standing-notes/hash-integrity-is-not-construct-validity-v0.7.2/figures/` — "alongside" the md/pdf in the same bundle directory.

## §4. Surfaced to Senior (Issue 2) — PROGRAM-POSITION-v0.1 anchor refresh

The document at `governance/standing/PROGRAM-POSITION-v0.1.md` currently states (line 4):

> Status: the one document that answers "where are we right now?" Updated when a stage closes; kept byte-true to the record (anchor: origin/main **6a4e604**). If this and the record disagree, the record wins and this is stale — re-sync.

Current `origin/main` HEAD is several commits later than `6a4e604` (commits since then have filed: Hash Integrity Option 3 move + relocation note; v0.5 structure-spec addition; this CS routing memo). The document's own re-sync ritual applies.

**Recommended Senior action:** refresh the anchor on line 4 from `6a4e604` to the current HEAD at time of refresh. Optionally update any other position-tracker content that has drifted in the intervening commits (TL's review notes the doc still says "current stage is D4 PIVOT approved, CAL-Q preserved on a finding track, and Tier 1 is next" — which is current as of this writing per TL, so the substance may be fine; the anchor is the main refresh).

CS will NOT touch this document without Senior direction.

## §5. Surfaced to Manager (Issue 3) — PROGRAM-MAP-v2.0 companion-pointer refresh

The document at `governance/standing/PROGRAM-MAP-v2.0.md` has two stale references:

- Line 6: *"Companions: NORTH-STAR-v1.1.md (the standard), PROGRAM-STAGE-MAP-v0.1/v0.2 (the phases), ROUTE-STATE-GATE-v0.1 (GREEN/YELLOW/RED), PROGRAM-MAP-RECONCILIATION-v0.1 (the decision this map executes)."*
- Line 34: *"North Star v1.1: the standing standard ("what must be true")."*

NORTH-STAR-v1.2 was filed at commit `292b478` (per Appendix A change log: Senior-drafted refinement; "bit-depth stress" → "numerical stress" + other precision edits; C5 claim-risk review integrated). Both v1.1 and v1.2 are on disk per supersede-don't-rewrite; v1.2 is the current canonical version.

**Recommended Manager action — two options:**

- **Option A (in-place edit):** update PROGRAM-MAP-v2.0 in place, changing two `v1.1` references to `v1.2`. Pragmatic; treats PROGRAM-MAP as a living standing doc.
- **Option B (supersede with v2.1):** file PROGRAM-MAP-v2.1 whose only delta from v2.0 is the companion-pointer refresh. Conservative; preserves v2.0 as filed under supersede-don't-rewrite.

CS recommendation, with light preference: **Option B** for symmetry with how NORTH-STAR itself supersedes (v1.1 → v1.2 with both retained); but Option A is also coherent if Manager treats PROGRAM-MAP as a living maintenance doc. Either way, CS does not execute without Manager direction.

## §6. Boundaries observed (per TL's "No model execution. No compression. No Paper B. No D4 reopening." carry-over)

- No model execution.
- No new run.
- No compression / INT8 / INT4 / second rung / full ladder.
- No D4 reopening / no CAL-Q rerun.
- No Paper B activation.
- No Claim C activation.
- No G6 build (Tier-1 instrument architecture stays at spec stage).
- No external release.
- No sealed-byte movement (4-of-4 byte-identical; ~86th survival check at this filing).
- No new research claims; no change to the scientific meaning of any paper or note (per v0.5 §F).
- No promotion of Hash Integrity to Paper 4 (per v0.5 §B + §G).
- No renumbering of Paper A or the numbered series (per v0.5 §C + §G).

Standard forbidden-phrasings grep across this memo: zero matches.

— CS Engineer, 2026-06-14
