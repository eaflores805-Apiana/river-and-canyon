# Tier 0 Task Design

*Design before data. This document defines the task structure, the controls, and one worked example per cell. **The actual matched pairs are left blank for the author to fill** — task design is the intellectual core of the experiment, and the pairs are where it succeeds or fails. Fill the slots, then generate `tasks/tier0_tasks.csv` from this design, then smoke-test, then run.*

**Status: scaffold — pairs not yet written. No run has occurred.**

---

## The one rule that governs everything

> **Tier 0 tasks minimize reliance on uncontrolled world knowledge. Compositional probes use closed-world facts whenever possible — the relevant facts live *inside the prompt* — so that a failure can be attributed to task structure under stress rather than to missing, ambiguous, or outdated knowledge.**

Why this rule exists: a real-world multi-hop chain (e.g. "author → birthplace → capital") conflates four different failure causes — the model may have broken the chain, or never known the author, or never known the birthplace, or been confused by wording. A closed-world prompt with the fact table supplied removes all of that. It lets you control, per item: the facts (A, B, C…), the expected answer, the chain length, the token length, the entity rarity, the distractors, and the state-load. That control is the whole point; without it a clean probe becomes a trivia swamp.

---

## The four cells

Every pair belongs to one cell. The cells cross **structure** (atomic vs compositional) with **support/shortcut** (high vs low), which is exactly the precision-demand contrast the protocol specifies — translated into runnable task families.

| Cell | What it is | What it probes |
|---|---|---|
| **1 · Atomic + high-shortcut** | single-step task with a spurious cue available | same-error / robust-wrong probe — does a *stable wrong answer* survive stress? |
| **2 · Atomic + low-shortcut** | single-step task, no exploitable cue | atomic clean control — should retain well; "boring controls pay rent" |
| **3 · Compositional + high-support** | familiar multi-step structure, closed-world facts | familiar-composition control — composition without rarity confound |
| **4 · Compositional + low-support** | rare/unfamiliar multi-step structure, closed-world facts | **the core ΔR stress target** — where retention is predicted to drop most |

The live comparison is **Cell 4 vs its matched control** (Cell 3 or a matched atomic), with Cells 1 and 2 supplying the same-error and clean-retention anchors. The negative-control pairs from the protocol (broad–broad, narrow–narrow; must show *no* within-pair gap) are carried over and should appear here too.

---

## One worked example per cell (from the design discussion — illustrative, not the run set)

These show the *shape* of a good item in each cell. They are examples of the form, not the pairs to be used. Replace and expand.

**Cell 1 — Atomic + high-shortcut** (same-error probe)
> Sentiment with negation, NLI with lexical overlap, or multiple-choice with a position cue — a task where a shortcut gives a confident *wrong* answer. The probe: does that same wrong answer persist identically under stress (high same-error rate = robust-wrong)?

**Cell 2 — Atomic + low-shortcut** (clean control)
> *Given: Toma = blue. Rika = green.*
> *Question: What color is Rika?*
> Closed-world lookup or arithmetic — no recall, no cue. Should retain near-perfectly; if it doesn't, the instrument itself is suspect.

**Cell 3 — Compositional + high-support** (familiar-composition control)
> *Given: France → Paris. Paris → population category "large."*
> *Question: What population category belongs to France's capital?*
> Familiar relation structure, but facts supplied in-prompt so it isn't testing recall. Composition with the rarity confound removed.

**Cell 4 — Compositional + low-support** (core stress target)
> *Given: Nalo owns the red key. The red key opens Vault 3. Vault 3 contains the silver token.*
> *Question: Which token does Nalo have access to?*
> Matched control (same structure, different bindings):
> *Given: Kira owns the blue key. The blue key opens Vault 2. Vault 2 contains the bronze token.*
> *Question: Which token does Kira have access to?*
> Rare/synthetic combination, fully closed-world. Vary across items: 2-hop vs 3-hop, distractor facts, unusual constraints, forced-intermediate vs not, output length.

---

## Pair slots — TO FILL

*Target ~20 matched pairs for a real pilot (the protocol notes 4 is a directional smoke test only). Each row: the closed-world prompt, the matched control, the cell, the chain length, the pre-registered precision-demand label, and the expected answer. The label must precede any model result — that is what keeps the experiment non-circular.*

| # | Cell | Prompt (closed-world) | Matched control | Chain len | Pre-registered label | Expected answer |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |
| 9 |  |  |  |  |  |  |
| 10 |  |  |  |  |  |  |
| 11 |  |  |  |  |  |  |
| 12 |  |  |  |  |  |  |
| 13 |  |  |  |  |  |  |
| 14 |  |  |  |  |  |  |
| 15 |  |  |  |  |  |  |
| 16 |  |  |  |  |  |  |
| 17 |  |  |  |  |  |  |
| 18 |  |  |  |  |  |  |
| 19 |  |  |  |  |  |  |
| 20 |  |  |  |  |  |  |

*Include at least one broad–broad and one narrow–narrow negative-control pair among the 20. Record why any candidate pair was excluded.*

---

## Thresholds — review triggers, not proof

> Pre-register **ΔR > 0.15** and **same-error rate > 0.7** as **review triggers, not proof thresholds.** With ~10–20 items, crossing them is smoke-test evidence that the effect is worth a larger, controlled look — not a result. Below them is equally informative: a local null is a real outcome (see the decision matrix in `diagrams/`).

These are the values to *examine* a result against, fixed before the run so the bar can't move afterward. They certify nothing on their own.

---

## Order of operations from here

1. **Fill the pair slots above** (the author's work — this is the experiment).
2. Generate `tasks/tier0_tasks.csv` from the filled table.
3. Run a tiny smoke test (2–3 pairs) to confirm the harness, scoring, and logging fire correctly.
4. Only then expand to the full set and run.
5. Record results in `RESULTS-INTAKE-TEMPLATE.md` — which has a pre-registered blank run-slot waiting for the first real number.

*Companion to the Fragility Probe Protocol (`notes/fragility-probe-protocol.md`) and the Tier 0 harness (`run_tier0.py`). Scaffold by structure; the pairs, and the experiment, are the author's.*
