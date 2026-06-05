# Status

Where each piece stands, and what's actually open — updated as the work and the literature move.

> **Update — June 5, 2026.** Tightened the video claim in *What Kind of Water* (and three smaller wording fixes); added six confound-guards to the Fragility Probe Protocol so it can fail honestly when run; built the **Claim Ledger** (`notes/claim-ledger-practice-note.md`) — a one-page control sheet sorting every claim by evidential status; built the inference-ranking record cross-checking outside rankings of the work. Repo current. **Next step is not more writing — it is running Tier 0 (or handing it off).**

| Piece | Status |
|---|---|
| **The River and the Canyon** | Explanatory framework. An analogy for transformer mechanics, with its limits stated. Teaches; does not claim to discover. Stable. |
| **What Kind of Water Carves the Mountain?** | Hypothesis and synthesis. Organizes an emerging empirical finding (task-dependent fragility under quantization) under a physical analogy, and names the open provenance question. Framing, not discovery. |
| **Analogy as Scaffold** | Method note. The discipline for using a physical analogy without letting it overclaim. |
| **No Mountain in the Sentence** | Method essay. The reasoning rule the papers apply. |
| **Fragility Probe Protocol** | Reproducibility / metrology protocol. A clean, matched-pair design that controls the task-difficulty confound cross-benchmark studies carry. Tests *whether the known fragility finding survives a tighter control* — not whether fragility exists. |
| **Capability Under Load** | Seed note. Speculative. Downstream of the above; reachable, not established. |
| **Speculative Companion — Failure Modes Under Pressure** | Quarantined speculation, pressure-tested six ways (in-house + five independent). The seven-defect taxonomy did not survive. Residue: one contribution — retention measures survival, not correctness (a real blind spot in standard robustness evaluation) — and one falsifiable but field-owned test-target — failures concentrate at compositional/OOD boundaries. Pre-data; not a framework, not an axis. |
| **Literature Notes** | What the post-publication search found: the fragility axis is established; the provenance question is open. |

## The open question

After several literature searches, the *explanatory* questions are answered or substantially so:

| Topic | Status |
|---|---|
| Fragility (capabilities differ in robustness under coarsening) | Supported by literature |
| Provenance effects (training composition shapes capability + robustness) | Supported by controlled studies |
| Capacity vs. usable structure | Hypothesis |
| Qualification metric (retention vs. accuracy as reliability predictor) | Open question |

Both fragility and provenance-effects have substantial prior art (see Literature Notes) — so the framework's role toward them is **synthesis**, not discovery, and the literature confirms those *phenomena* without confirming the framework's geometric *account* of them.

What remains genuinely open is *practical*, not explanatory, and sits to the side of the whole explanatory program:

> **Does a capability's retention under stress (compression, perturbation) predict its real-world deployment reliability better than its peak benchmark accuracy?**

The *concept* of reliability-style evaluation is itself active (robustness benchmarks, stress-testing, "accuracy-alone is insufficient for deployment" work). What appears possibly open is the narrow competing-predictors test: retention-under-compression vs. peak accuracy, head to head, as predictors of reliability. Its value does **not** depend on originality or on any mechanism being correct — a stress test that predicts field failure is useful regardless. This is the framework's honest forward edge.

## What would move this forward

Not more writing — measurement. The explanatory questions are largely handled by the field; the open, in-wheelhouse one is the qualification metric:

1. **Metrology check.** Confirm a matched-pair probe reproduces the field's known task-type fragility on one model. Validates the instrument. (Small.)
2. **Qualification test (the primary open direction).** Across a panel of models, compare *retention under stress* against *peak benchmark accuracy* as competing predictors of deployment reliability. Does retention add predictive value beyond accuracy? Needs no fine-tuning, no provenance isolation, no mechanism — only a measurement that works. Possibly still open as a clean head-to-head; valuable regardless of originality; squarely a qualification-engineering question. (Tractable.)

The provenance comparison that earlier looked like the frontier has substantial controlled prior art (composition→capability, composition→perturbation-robustness) and is no longer the priority; a quantization-specific corner may remain but is likely an obvious extension others are pursuing.

*E. A. Flores, Apiana AI, Inc.*
