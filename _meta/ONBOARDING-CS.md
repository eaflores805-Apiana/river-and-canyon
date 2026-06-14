# CS Engineer Onboarding

*If you are a new CS Engineer (human or AI) picking up this project, start here. This file
is stable — it doesn't change with each session. For "what's happening right now," follow
the pointer in §"Start here."*

---

## 1. What this project is

A behavioral stress-metrology program for large language models. Four papers published or
in flight:

- **The River and the Canyon** + **What Kind of Water Carves the Mountain** (`writing/`) —
  physical-analogy essays. Foundational framing; not active experimental work.
- **Paper 1 — Survival Is Not Correctness** (`papers/paper1-survival-is-not-correctness/`) —
  metrology protocol. Final.
- **Paper 2 — Correctness Is Not Constructibility** (`papers/paper2-correctness-is-not-constructibility/`) —
  pre-stress baseline mapping. v1.0 released 2026-06-09. Addendum 01 active.
- **Paper 3 — Certification Before Retention** — protocol/methods paper. Currently at
  draft v0.6, in Team Lead readiness check.

The active experimental surface is the **B1 v2 harness**
(`experiments/2026-06-09_b1-harness-v2/`), which provides validity-harness infrastructure
for both Paper 2 reproduction and (when separately authorized) Paper 3 certification
application.

---

## 2. Roles

```
Manager      Elias Flores. Sets priorities. Authorizes scope changes,
             merges, runs, candidate selection, threshold values.

Team Lead    Coordinates between Senior, CS, and Manager. Issues readiness
             checks, status boards, and wording-correction memos.

Senior       External engineer. Owns paper manuscripts and reference work.
             Drafts and revises Papers 1–6. Provides addenda.

CS Engineer  You. Writes runner/scorer code, executes authorized experiments,
             files governance memos, maintains harness infrastructure.
             Does not select candidates, set thresholds, or authorize runs.
```

The decision rule is: **Manager decides; Team Lead routes; Senior writes; CS implements
and verifies.** CS escalates ambiguity rather than guessing.

---

## 3. CS scope

| Directory | CS access |
|---|---|
| `tier0-run/` | **SEALED** — frozen Paper 1/2 provenance record. Never add files. Documentation updates to existing files (PROJECT_BRIEFING.md, EXPERIMENT_LOG.md, governance INDEX.md) are permitted. |
| `experiments/` | CS-active. All new experimental work lands here under `<YYYY-MM-DD>_<slug>/`. |
| `governance/` (root) | CS-active. All new governance filings land here. |
| `papers/` | Senior-owned. CS does not edit manuscripts. CS may file release-record addenda in `governance/<paper-release-dir>/`. |
| `writing/` | Stable. Foundational essays. CS does not modify. |
| `notes/`, `diagrams/`, `review/` | User-owned. CS does not modify unless explicitly asked. |

---

## 4. Standing constraints

Read this before doing anything substantive:

→ **`governance/standing/STANDING-NON-AUTHORIZATIONS.md`** — the quick card listing every
blocked lane and why. Every CS memo carries the relevant subset verbatim. Items move off
this list only by explicit Manager authorization.

Two protected surfaces in particular:
- Paper 2 v1.0 tag `paper2-cells01-03-v1.0` and tagged manuscript blob — never moved.
- `tier0-run/` directory — sealed; no additions.

---

## 5. Start here — current state

Before doing any CS work, read the **most recent passdown letter**:

→ **`governance/passdown/`** — directory of dated passdown letters. Read the file with
the most recent date prefix. Each letter is the date-stamped snapshot of: what just
happened, what's pending, what's blocked, and what to read next.

The passdown letter exists because this is a long-running program with multiple papers,
governance memos, and standing decisions. Reading the entire governance archive cold
would take hours; reading the latest passdown letter takes 10 minutes and points you at
the 3–5 docs that matter right now.

If the passdown letter looks stale (more than a session old, or refers to commits/state
that's clearly behind `git log`), say so and ask Manager for a fresh status board before
proceeding.

---

## 6. Governance memo conventions

Every CS-authored governance memo follows the same shape:

```
# <Memo Title>

**Date:** YYYY-MM-DD
**From:** CS Engineer
**To:** <primary actor>; Cc: <others>
**Re:** <one-line subject>
**Status:** <one-line status>

---

## Record status

```
<short code block summarizing where this filing sits in the process>
```

---

## <Body sections>

---

## Non-authorizations (carried forward)

```
<verbatim subset from STANDING-NON-AUTHORIZATIONS quick card,
 relevant to this memo>
```

---

— CS Engineer, YYYY-MM-DD
```

**Sign-off is mandatory.** Every CS document closes with `— CS Engineer, YYYY-MM-DD`.

**Memos go in dated governance directories.** New work creates a new dir under
`governance/<YYYY-MM-DD>_<topic>/`. Related memos cluster in the same dir.

---

## 7. Commit conventions

- One coherent change per commit. Don't bundle unrelated work.
- Title: imperative, <70 chars. Example: `File Paper 2 v1.0 Addendum 01 — model-snapshot provenance reclassification`
- Body: multi-paragraph if needed. Reference governance memo paths and SHAs explicitly.
- Co-author line: `Co-Authored-By: Claude <noreply@anthropic.com>` (model-agnostic).
- **Do not rewrite history** unless Manager explicitly authorizes. Corrections file as
  superseding commits, not as `--amend` or rebase.
- **Push after each meaningful commit.** The remote is the audit trail.

---

## 8. Memory expectations (for AI CS instances)

If you are an AI CS instance (e.g., Claude), expect the following memory files to be
loaded automatically when running in `~/.claude/`:

- `user_profile.md` — Manager profile, plan, preferences.
- `llm_mechanics_experiments.md` — project state at last passdown (kept current in
  parallel with the passdown letter; if they diverge, the passdown letter is
  authoritative — memory is point-in-time).
- `feedback_*.md` — accumulated guidance: repo scope, return-packet format, sign-off,
  paper-revision cadence.

Memory is point-in-time. The repo is the source of truth. If memory says "X exists at
path Y," verify the file before acting on it.

---

## 9. Where to find what

```
ONBOARDING-CS.md                          → this file
governance/passdown/<latest>.md           → current state (read first)
governance/standing/STANDING-*.md         → rules of the road
governance/<dated dirs>/                  → historical governance archive
tier0-run/PROJECT_BRIEFING.md             → long cold-start brief
tier0-run/EXPERIMENT_LOG.md               → program log
experiments/<dated dirs>/                 → active experimental work
papers/                                   → released paper packages
```

---

## 10. If you're stuck

Escalate to Manager with a specific question. Don't infer authorization from absence;
infer blockage from absence. The non-authorization quick card is the answer to most
scope questions.

---

— CS Engineer, 2026-06-10
