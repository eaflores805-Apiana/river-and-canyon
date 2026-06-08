# The River and the Canyon

A pair of essays that build a physical analogy for how large language models work — then stress-test it, propose a way to measure it, and reflect on the method itself.

## The work, in order

**1. The River and the Canyon**
A physical analogy for a transformer: weights as a frozen mountain, activations as water moving over fixed stone, training as the slow carving of the rock, inference as water running over stone that no longer moves. The second half deliberately tries to break the analogy to find exactly where it stops being the territory.
→ [`the-river-and-the-canyon/`](the-river-and-the-canyon/) — **new here? start with the lean edition** (`-lean`), the whole picture in one fast read; the full paper develops each step and stress-tests every claim. Both come in Markdown (reads in-browser), PDF (typeset), and Word. Figures are in `assets/`.

**2. What Kind of Water Carves the Mountain?** *(companion)*
The first paper followed only one river: human language. This one asks what changes when the water changes — code, video, simulation, action — and finds a second axis underneath the obvious one. Not just *where* a capability's structure came from (provenance), but *how much precision it needs to survive* (fragility), with quantization as the instrument that exposes the second. The compact claim, and the guard against over-reading it: **provenance shapes the mix, not the fate.** It is framed as a perspective worth testing, not a finished framework.
→ [`what-kind-of-water/`](what-kind-of-water/)

Read the two in order; the second assumes the first.

## Notes and proposals

**No Mountain in the Sentence** — a short companion essay on the *method* behind the papers: the discipline for trusting an analogy exactly as far as it earns. It states one rule (say the claim with no mountain in the sentence) and three questions, then applies them to the mountain analogy itself.
→ in [`the-river-and-the-canyon/`](the-river-and-the-canyon/)

**A Fragility Probe for Carved Structure** — a *proposed* experiment (not a completed result) for testing one prediction of the second paper: whether precision-demanding capabilities retain less of their full-precision performance under quantization than matched broad ones. A small, runnable, falsifiable pilot, with a pre-declared decision rule that allows a flat result. *(Now executed — its Tier 0 run is written up in* Survival Is Not Correctness*, below, which returned the flat/redesign outcome the decision rule allowed for.)*
→ [`notes/fragility-probe-protocol.md`](notes/fragility-probe-protocol.md)

**Survival Is Not Correctness** — **the Tier 0 run**, written up as a metrology paper, and the realized form of the correctness/same-error guard: the discipline for telling whether behavior that survives quantization is retained capability or retained *error*. It logs baseline correctness, stressed correctness, and same-error identity together, so a perfectly-retained wrong answer cannot read as robustness. It executes the Fragility Probe / Tier 0 design and returns the disciplined "no" the protocol allowed for: chain-task runs completed FP16/INT8/INT4 sweeps (a scoring-artifact finding and bounded nulls), and the core Cell-4 seam construction failed its FP16 feasibility gate and reached no clean stress sweep — so claim #5 stays open, and the lesson is that *construction validity*, not the stress effect, is the binding constraint. It *owns that pivot*: the durable contribution is the measurement contract, not a seam result. No claim that a compositional seam exists; same-error identity *specified and operationalized*, not established. *Reach is not validity.*
→ [`survival-is-not-correctness/`](survival-is-not-correctness/)

**Analogy as Scaffold** — a method note on using a physical analogy without letting the picture smuggle claims into the mechanism: three registers kept separate (analogy for questions, mechanism for claims, measurement for results), and the three risks the image imports (reification, false continuity, imported agency).
→ [`notes/analogy-as-scaffold.md`](notes/analogy-as-scaffold.md)

**Capability Under Load** — a seed note (explicitly speculative, not a result) on a downstream implication: that capacity and *usable structure* may be different things — a model can have representational room for a capability without having carved a structure that bears load under stress.
→ [`notes/capability-under-load.md`](notes/capability-under-load.md)

**Where things stand** — current status of each piece and the one open question (does provenance predict fragility beyond task-type?) is in [`STATUS.md`](STATUS.md); what the post-publication literature search found — the fragility axis is established, the provenance question is open — is in [`notes/literature-notes.md`](notes/literature-notes.md).

**Parked open question — the uneven-support pattern** — a side note, explicitly *not* a finding: the carving analogy can be used to generate a long list of failure patterns, but the high match-rate to real LLM errors is a sign of the frame's flexibility, not its validity (it is post-hoc, and reduces to field-established families). The note keeps the intuition while stripping its authority, and reframes the durable residue as *behavioral parameters* rather than defects. Its raw object-to-think-against is a companion list. The guardrail for the whole branch: *reach is not validity.*
→ [`notes/open-question-uneven-support.md`](notes/open-question-uneven-support.md) and [`notes/carved-path-pattern-list.md`](notes/carved-path-pattern-list.md)

**Claim Ledger** — for claim status and epistemic boundaries: a one-page control sheet that sorts every major claim into field consensus, original framing, empirical anchor, open hypothesis, interpretation, or conditional implication — and states what would change each. It exists to stop the project from being misread, not to impress. The governing rule: implications are conditional; they are not evidence.
→ [`notes/claim-ledger-practice-note.md`](notes/claim-ledger-practice-note.md)

## Governance diagrams

Six diagrams make the project's discipline legible at a glance — what it is, what it isn't, what's left to do, and what each result would mean. Each owns one failure mode: the **lineage** (what the analogy generated and what unequally survived), the **boundary** and the **Venn** (what the method can and cannot decide, in table and spatial form), the **gap map** (unexplored areas by field), the **decision matrix** (what each Tier 0 outcome means, pre-registered), and the **status ladder** (what promotes a claim, so one run is not mistaken for a framework). The set, with a gallery and the governance finding behind the Venn, is in [`diagrams/`](diagrams/).

## On method

The papers share one discipline: the analogy is allowed to be vivid only as long as the mechanism underneath it stays in view. Claims are sorted by how well the evidence actually supports them, limits are stated plainly, and where the work reaches past what is established it says so. The picture is a way of asking sharper questions, not a machine for predicting what will work. Where the work proposes rather than demonstrates — the provenance-by-fragility interaction, the fragility probe, the capability-under-load idea — it is marked as a proposal, not a result.

*Written by E. A. Flores, Apiana AI, Inc. Licensed CC BY-NC 4.0.*
