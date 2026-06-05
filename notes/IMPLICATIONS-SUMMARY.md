# Implications — Summary (front door)

*A short companion to `implications.md`. This is the reference's front door: the scoring logic, the core (Tier A) rows, what the full table shows, and the one-line summary. For Tiers B/C, the conjectures, boundary rows, and the document's own discipline notes, see the full index.*

**Status: reference document, not argument.** Used to decide what can be led with, what must be hedged, and what waits for data. Scores are provisional and meant to be contested.

---

## How the scoring works

Each implication is scored on five axes. **None measures how exciting or high-impact the idea would be if true** — that axis is deliberately omitted, because it is the one that turns a reference index into a hype generator.

- **Evidence** — `Lit` (external literature) · `Project` (the project's own reasoning) · `Hypothesis` (plausible, untested) · `Speculative` (downstream of other unproven claims).
- **Mechanism-dependent?** — does it require the river-and-canyon *account* to be correct? `No` is stronger: it survives even if the framework's explanation is wrong. **This is the spine of the document.**
- **Originality** — `Field` (the field established it) · `Synthesis` (the framework organizes/anticipates it but did not originate it) · `Ours?` (no clear prior art found — flagged because "we didn't find it" is not "it doesn't exist").
- **Type** — `Mech` · `Eval` · `Practical` · `Method` · `Spec`.
- **Actionable now?** — concrete next step, or framing only?

**Confidence tier:** **A** = supported and/or mechanism-independent; **B** = plausible but unproven; **C** = speculative, preserved-not-promoted.

---

## Tier A — the core (trust and lead with these)

| # | Implication | Evidence | Mech-dep? | Originality | Type | Actionable? |
|---|---|---|---|---|---|---|
| A1 | **Analogies earn their keep by generating *testable distinctions*, not by feeling explanatory.** Transferable procedure: **de-imaging** — strip the metaphor, restate as bare mechanism, keep only what survives. | Project | No | Synthesis | Method | No — it's the method itself |
| A2 | **Training/inference is best understood as *fixed* vs. *transient*** (permanence/transience), not a surface metaphor. | Project | No | Synthesis | Mech | No — framing |
| A3 | **Quantization is not only compression; it can act as a diagnostic stress test** — coarsening asks which structures survive reduced precision. | Lit | No | Synthesis | Eval | Partly — the probe's basis |
| A4 | **Fluent behavior can survive while exact reasoning quietly degrades.** Surface competence is not a proxy for load-bearing capability. | Lit | No | Synthesis | Eval | No — motivates A8 |
| A5 | **Precision-demand matters: capabilities differ in fragility under coarsening.** Math/reasoning degrade disproportionately; broad language is more preserved. | Lit | Partly | Field | Mech | No — established |
| A6 | **Failures may localize at the first fragile step, then cascade** — not uniform degradation. First-failing-step index is stronger evidence than retention alone. | Lit | Partly | Synthesis | Mech | Yes — protocol logs it |
| A7 | **Provenance shapes the mix, not the fate.** Training origin shapes *which* structures form, not any capability's fragility. | Lit | Partly | Field | Mech | No — established |
| A8 | **The live question: does stress-retention predict deployment reliability better than peak accuracy?** Inherits *none* of the framework's explanatory burden. | Hypothesis | **No** | Ours? (concept active; clean head-to-head maybe open) | Eval/Practical | **Yes — the priority experiment** |
| A9 | **Inference is passive: no active driving force in a forward pass.** Structure is primary, force its derivative. | Project | No | Synthesis | Mech | No — disciplines force-talk |
| A10 | **FlashAttention / memory-efficient attention are *safe*** — exact up to rounding; they change data movement, not geometry. The lone *negative* implication. | Lit | No | Synthesis | Mech | Yes — deploy without capability-loss concern |
| A11 | **Weights are immutable at inference** — permanence is an operational guarantee. Serving-time "learning" must be external (KV-cache, tools, retrieval). | Lit | No | Synthesis | Mech | Yes — treat the model as frozen |
| A12 | **Quantization claims are scoped to *post-training* quantization only** — a verified boundary. Says nothing about QAT. | Lit | No | Synthesis | Method | Yes — prevents overclaiming to QAT/hardware |
| A13 | **Retention is measured relative to each task's *own* full-precision baseline** — a measurement *definition*, not a hypothesis. | Project | No | Synthesis | Method | Yes — defines the metric |

---

## What the table shows

- **The center of gravity is tiny — and that's the point.** Of 50+ rows, only a handful are both mechanism-independent and actionable now: **A8** (retention vs. peak accuracy), **B13/B23** (the rescue test separating fine-spacing from outlier fragility), **A10** (FlashAttention-class optimizations are safe). Everything else inherits the analogy's story or is field-established. That convergence is the signature of a framework stress-tested to failure and audited against the literature.

- **The durable contribution is method and measurement, not new mechanism.** Filtered strictly, Tier A is dominated by *framing* (A1, A2, A9), *verified boundaries* (A10, A11, A12), and *measurement definitions* (A3, A13). The most trustworthy outputs are *what the analogy does not let you claim* and *how to measure cleanly*.

- **The mechanism-independent column is the real spine.** A mechanism-independent Tier-B idea can be more valuable than a mechanism-dependent Tier-A one, because it survives even if the geometric account is merely a useful picture. This is the filter for deciding what to lead with.

- **Excitement and evidence are inversely correlated here.** The vivid downstream items (SLAs, hardware routing, safety stress testing) cluster in Tier C with overclaim flags. **Specificity is not evidence** — a precisely-rendered consequence inherits 100% of its risk from the unproven premise beneath it.

- **Boundaries do quiet heavy lifting.** Clean negatives (A10, A11, A12) tell practitioners what they do *not* need to worry about and where the framework stops applying — and that boundary-drawing earns trust.

- **The minimal viable research program:** A8 → B13. Does retention add predictive value beyond peak accuracy? If so, does salient-channel protection separate the two fragility mechanisms? B28 (cross-stress validation) tests whether it's real fragility or quantization-specific weirdness.

---

## One-line summary

> The framework's most robust and actionable contribution is not a new explanation of why capabilities are fragile. It is a disciplined way to *ask* whether they are, a clean measurement language for *testing* it, and a short list of things the picture does *not* let you claim. The live empirical question it leaves the field is narrow and well-posed: **does retention under stress predict real deployment reliability better than peak accuracy, and can a cheap rescue test separate the mechanisms?**

The analogy generated these testable distinctions and then got out of the way — logically *un*necessary to defend the conclusions, though necessary to *find* them. **The claim map is complete; the physics must now decide.**

*Front-door summary of `implications.md` (the full reference of record). Synthesis, not data.*
