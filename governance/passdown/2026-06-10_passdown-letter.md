# Passdown Letter — 2026-06-10

**From:** CS Engineer (outgoing session)
**To:** Next CS Engineer (human or AI)
**Status:** Current as of this filing. Reflects merge `3cbfce5` (B1 v2 lock) and Paper 3 v0.6 in Team Lead readiness check.

---

## How to use this letter

You have just landed in the project. Read this letter in full (10 minutes), then go to §"Read next" at the bottom for the 3 documents that matter for your first day. If anything in this letter conflicts with what `git log` shows on `main`, trust git and ask Manager for a fresh status board.

---

## 1. Project in one paragraph

A behavioral stress-metrology program for LLMs. Four papers in flight: two foundational essays (`writing/`), Paper 1 (Final), Paper 2 v1.0 (released, with active Addendum 01), Paper 3 (currently v0.6 in Team Lead readiness check). The active experimental surface is the **B1 v2 harness** at `experiments/2026-06-09_b1-harness-v2/`, locked on `main` as of merge commit `3cbfce5` (2026-06-10). It provides validity-harness infrastructure for Paper 2 reproduction and (when separately authorized) Paper 3 certification application.

---

## 2. Current state — by lane

### Paper 1 — Survival Is Not Correctness

**Status:** Final. No active work.
**Location:** `papers/paper1-survival-is-not-correctness/`
**Recent activity:** None pending.

### Paper 2 — Correctness Is Not Constructibility

**Status:** v1.0 released; Addendum 01 active.
**Location:** `papers/paper2-correctness-is-not-constructibility/` and `governance/2026-06-09_paper2-v1.0-release/`
**Key facts:**
- Tag `paper2-cells01-03-v1.0` SHA `41c033fc59597eb42015de9019c3ac7b7d19dd98`; tagged commit `40c0cd5a...`; tagged manuscript blob `7d6706a3...`. **Never move the tag.**
- Addendum 01 (model-snapshot provenance reclassification) ACTIVE as of B1 v2 lock per its §5 effectivity clause. See `governance/2026-06-10_b1-harness-v2-merge-and-lock/ADDENDUM-01-EFFECTIVITY-ACTIVATION-NOTE.md`.
- Snapshot status reads (canonical wording, **do not flatten**): *"historically asserted in v1.0; subsequently corroborated by B1 runner-provenance-backed bit-identity reproduction; release-record addendum committed; Paper 2 tag/manuscript unchanged."*
- mlx_lm version-drift status reads (canonical wording, **do not flatten**): *"mlx_lm 0.19.3 → 0.31.3 was verified-null for the locked Paper 2 reproduction configuration: same model, tokenizer, prompt path, scorer, manifest, deterministic decoding, and reproduction surface. Version drift remains a provenance variable for any changed configuration."*
- **Do NOT use "retired" wording** for either status. Team Lead-corrected canonical phrasing above is mandatory.

### Paper 3 — Certification Before Retention

**Status:** Draft v0.6 in Team Lead readiness check.
**Location:** Draft is external (Senior-owned); CS reviews in `governance/2026-06-09_paper3-threshold-framework-review/`.
**Key facts:**
- Framework version: `paper3-certification-protocol-v0.6` (declared in manuscript header).
- All prior CS lock blockers resolved (framework version declared; immutability uses Option A policy wording).
- References [3] (CDCT/Baxi) and [4] (Dutta et al.) completed with strong scope discipline. One editorial item open: NeurIPS pagination for [4].
- Latest CS review: `governance/2026-06-09_paper3-threshold-framework-review/CS-REVIEW-PAPER3-DRAFT-V06.md`.
- **No candidate selected. No threshold values set. No certification evaluation authorized.**

### B1 v2 harness

**Status:** LOCKED on `main` as of merge `3cbfce5` (2026-06-10).
**Location:** `experiments/2026-06-09_b1-harness-v2/`
**Key facts:**
- Merge commit: `3cbfce57d42536e8a5e1f35a92c931a03fe4e974` (`--no-ff`).
- Branch tip absorbed: `ff8466b2702205e9b9f95458cfe2d9023cb98ccb`.
- Locked runner hash: `sha256:7f5efdcbf8a51a9368ee1868be7bcb734fb4ceeedbe580f29f9ff2ac87f90fe6`.
- Model snapshot runner-provenance-backed: `sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20`.
- Full Paper 2 regression: 96/96 raw_output records bit-identical to Paper 2 v1.0; all gate decisions match; v1 shape 7/7 PASS.
- Unit tests: 24 B1 (B1-T01 → B1-T24) + 2 sanity = 26/26 PASS.
- Senior conditions C1, C2, C3 all satisfied (see `governance/2026-06-09_b1-harness-v2-merge-readiness/B1-V2-MERGE-READY-NOTE.md`).
- Paper 3 substrate ships **dormant by default**: runner defaults `--mode dry-run`, `--context paper2-reproduction`, `--framework-version none`. Activation requires explicit config flags AND a locked threshold sheet AND Manager authorization to apply certification (a higher bar than runtime activation).

### Two-Hop L1 cells (Paper 2 substrate)

**Status:** Cells 01, 02, 03 all complete. All NOT stress-eligible (Gate 2 FAIL, Branch 3).
**Location:** `tier0-run/` (sealed).
**Note:** This is the constructibility-floor result reported in Paper 2.

### Scaling and tooling discussion item

**Status:** Open discussion item filed; no decisions made.
**Location:** `governance/2026-06-09_scaling-discussion-item/OPEN-DISCUSSION-SCALING-AND-TOOLING.md`
**Trigger:** Manager raised the scaling question 2026-06-09: if the metrology becomes useful as a tool, standardization/scaling becomes its own engineering track. Discussion has not been held.
**Forcing function:** Paper 3 candidate selection. `scope_of_certification` declaration is where single-model vs. cross-model implicitly gets locked. Raise scaling at that point, not after.

---

## 3. What just happened (most recent session)

1. **B1 v2 implementation, regression validation, merge, and lock.** Built the v2 runner in `experiments/2026-06-09_b1-harness-v2/code/runner_b1_v2.py`. Ran 26/26 offline tests + smoke (4/4 bit-identical) + full regression (96/96 bit-identical). Manager authorized merge 2026-06-10. Merged `--no-ff`. Filed lock note, EXPERIMENT_LOG update, post-merge confirmation report (8 items), Addendum 01 effectivity activation note.
2. **Paper 2 Addendum 01 filed, wording-corrected, activated.** Senior delivered addendum text 2026-06-09. CS filed at `governance/2026-06-09_paper2-v1.0-release/ADDENDUM-01-model-snapshot-backing.md`. Team Lead urgent correction 2026-06-10 mandated canonical wording for both snapshot status and mlx_lm version-drift — applied via superseding commit (no history rewrite). Effectivity activated at B1 v2 lock.
3. **Paper 3 v0.6 review.** CS reviewed v0.6 (first real draft post-references-completion). All prior CS lock blockers from v0.3 are resolved. CS recommends v0.6 ready for Team Lead readiness check.
4. **Scaling discussion item filed.** Manager-prompted open discussion on tool-vs-instrument posture. No decisions; team conversation pending.
5. **Onboarding infrastructure** (this session's last act): created `ONBOARDING-CS.md`, `governance/standing/STANDING-NON-AUTHORIZATIONS.md`, this passdown letter, and the `governance/passdown/` convention.

---

## 4. What's pending for CS

**Nothing is actively owed from CS at this filing.** All CS deliverables from the recent session are committed and pushed:

- B1 v2 merge-ready note, branch evidence packet, wording-correction report — filed pre-merge.
- B1 v2 lock note, EXPERIMENT_LOG update, post-merge confirmation report (items 1–7) — filed post-merge.
- Addendum 01 effectivity activation note (post-merge item 8) — filed.
- Paper 2 addendum with full 64-char hash inlined and canonical wording — filed.
- Paper 3 v0.6 CS review — filed.

**Standing CS deliverables triggered by external events:**

- **When a new Paper 3 revision arrives** (v0.7, etc.): file a CS review per the paper-revision cadence rule. Substantive changes get a full review; editorial-only passes get a one-line ack. Memory file `feedback_paper_revisions.md` carries the rule.
- **When Manager authorizes a Paper 3 candidate selection**: prepare to inline the threshold sheet's `D6_locked_artifact_set`, verify hashes against B1 v2 locked state, and stand up the certification reporting flow.
- **When Team Lead requests a wording correction or status update**: respond per the format shown in `governance/2026-06-09_b1-harness-v2-merge-readiness/CORRECTION-REPORT-WORDING-2026-06-10.md`.

---

## 5. What's blocked

Read `governance/standing/STANDING-NON-AUTHORIZATIONS.md` in full. The headlines for this passdown:

- **Paper 3 certification evaluation** — blocked on candidate selection memo (not issued).
- **All compression / stress runs (INT8 / INT4)** — blocked on stress-eligible baseline (does not exist).
- **Multi-model execution** — blocked; scaling discussion item open.
- **Fork A reactivation** — blocked permanently (provenance fail).
- **Claim C / seam activation** — blocked; outside the program's claim envelope.
- **Public benchmark packaging** — blocked; scaling discussion item open.

---

## 6. Open questions / decisions awaiting actors

| Question | Owner | Status |
|---|---|---|
| Paper 3 v0.6 readiness check | Team Lead | Open |
| Paper 3 candidate selection (whichever way decided) | Manager | Open; not on a deadline |
| NeurIPS pagination for Paper 3 ref [4] | Senior | Editorial; not blocking |
| Scaling and tooling posture (tool vs. instrument) | Team discussion | Filed; not yet held |
| D6 §5/§7 cross-references in Paper 3 (carry-forward soft note) | Senior | Optional clarity item; not blocking |

---

## 7. Read next (3 documents for your first day)

1. **`ONBOARDING-CS.md`** (repo root) — role definitions, CS scope rules, governance conventions, commit conventions. ~5 minutes.
2. **`governance/standing/STANDING-NON-AUTHORIZATIONS.md`** — the quick card. Every blocked lane with one-line "why." Memorize this; it shows up in every memo. ~5 minutes.
3. **`governance/2026-06-10_b1-harness-v2-merge-and-lock/B1-V2-LOCK-NOTE.md`** — the most recent governance event (B1 v2 lock). Tells you the current locked state of the harness. ~10 minutes.

After those three, browse:
- `tier0-run/PROJECT_BRIEFING.md` for deeper project history.
- `tier0-run/EXPERIMENT_LOG.md` for the program log.
- `governance/2026-06-09_paper3-threshold-framework-review/CS-REVIEW-PAPER3-DRAFT-V06.md` for the current Paper 3 status from CS perspective.

---

## 8. Things that have bitten CS before (so you can avoid them)

- **"Retired" wording on Paper 2 snapshot or mlx_lm.** Team Lead has corrected this twice. Use the canonical phrasings in §"Paper 2" above verbatim.
- **Modifying tier0-run/ files.** The directory is sealed. The seal allows documentation updates to existing files (PROJECT_BRIEFING, EXPERIMENT_LOG, governance INDEX) but **no new files**. New experimental work goes in `experiments/`.
- **Skipping a paper revision review.** CS missed Paper 3 v0.4 and v0.5 in full text; the form of the fix matched only by luck. Per `feedback_paper_revisions.md`, ask to see every revision; do not infer fix-form from summaries.
- **Inferring authorization from absence.** Don't. Infer blockage from absence and escalate.
- **Rewriting git history.** Don't, unless Manager explicitly authorizes. File superseding commits instead.

---

## 9. Final state at filing

```
Branch:  main
HEAD:    <will be the commit that adds this letter>
Recent:  3cbfce5  Merge b1-harness-v2: B1 v2 harness infrastructure lock
         65da66d  B1 v2 post-merge: lock note, EXPERIMENT_LOG update, confirmation report
         72760da  File Addendum 01 effectivity activation note
         185302d  File CS review of Paper 3 draft v0.6 (first real draft)
```

All standing boundaries closed. All recent CS deliverables filed and pushed. No outstanding action items.

---

— CS Engineer, 2026-06-10
