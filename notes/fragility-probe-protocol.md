# A Fragility Probe for Carved Structure

*A proposed bit-depth sweep for testing whether precision demand predicts quantization sensitivity.*

*Companion protocol note to* The River and the Canyon *and* What Kind of Water Carves the Mountain?

---

> **Status: proposed experiment, not a completed result.** This document does not prove the two-axis framework from *What Kind of Water Carves the Mountain?* It specifies the smallest clean experiment that would test **one** of its predictions, states what would support that prediction, and states what would weaken it. It is written so that someone with the compute, tooling, and evaluation infrastructure — which the author does not currently have — could pick it up and run it. The author's contribution here is the question and the design, not the data.

## The claim under test

The companion paper proposes two distinct axes: *provenance* (what kind of structure the training medium carved) and *fragility* (how much precision that structure needs to survive coarsening). This protocol tests only the fragility axis, and only its cleanest prediction:

> **At a fixed bit depth, capabilities that demand exact, precision-sensitive computation should retain a smaller fraction of their full-precision performance than capabilities that are broad and tolerant — when the two are matched on everything except precision demand.**

This is deliberately narrow. It does not test provenance. It does not establish margin geometry. It tests whether "fragility" shows up as a *measurable difference in degradation curves* inside a single model, rather than remaining an aesthetic category.

## Why this experiment first, and not the provenance comparison

The conceptually interesting question — does a code-trained model degrade differently from a text-trained one? — has too many confounders to be a clean first move: model choice, training mixture, benchmark quality, calibration data, tokenizer effects, and the ever-present risk of measuring task difficulty while believing you are measuring provenance.

The within-model bit-depth sweep removes almost all of that. One model, one quantization recipe, one evaluation set, held constant. The only thing that varies between the paired tasks is precision demand. Establish the baseline fragility signature here first; the provenance comparison is only interpretable once you know the within-model effect is real.

## Design

**One model.** A single dense open-weights model. (Mixture-of-experts is deferred — router behavior under quantization is a separate failure mode and adds a variable.)

**One quantization recipe**, fixed and fully specified — including whether it quantizes weights only or weights and activations, since the two behave differently and a reader needs to know which is being tested. Calibration data is **held fixed across all bit depths**. Changing the calibration set between rungs introduces a variable that masquerades as a precision effect. Make this checkable rather than promised: use one calibration file, record its hash, and reuse the identical file at every width — so "we held calibration constant" is something a reader can verify, not something they have to trust. If task pairs span text, code, and math, a mixed-domain calibration set is preferable to pure text, which could bias quantization toward language behavior and let a critic attribute code degradation to calibration mismatch rather than precision demand.

**A bit-depth ladder:** FP16/BF16 → INT8 → INT4. Optionally INT6 between, and INT3 if you want to see the cliff. The full-precision run is the per-task baseline.

**Matched task pairs.** This is the real experiment, and pair construction is where it succeeds or fails. Each pair shares source material, length band, and prompt skeleton; only the *instruction* changes, so the two halves differ in precision demand and as little else as possible:

| Domain | Broad / tolerant half | Narrow / precision-demanding half |
| --- | --- | --- |
| Text | Broad summarization | Exact logical / temporal tracking |
| Code | High-level explanation of what code does | Exact output on hidden input |
| Math | Conceptual explanation | Multi-step numerical execution |
| State | Loose story comprehension | Exact entity / state tracking |

Four pairs is a pilot. The point of pairing is to isolate precision demand instead of accidentally measuring that one task was simply harder to begin with. To keep that honest, hold each pair to explicit acceptance criteria before the run: both halves drawn from the same source item where possible, output budgets within roughly 10% of each other (so one side isn't penalized for length), comparable FP16 baselines, and no tasks where a trivial substring of the prompt is a correct answer. Record why any candidate pair was excluded. A pair that can't meet these isn't a clean test of precision demand and shouldn't be in the pilot.

**Negative controls.** Alongside the four contrast pairs, include at least one *broad–broad* pair and one *narrow–narrow* pair — two tasks of the same precision class, scored with identical strictness. These should *not* show a within-pair retention gap. If they do, the apparent fragility effect in the contrast pairs is suspect: the paired design itself may be leaking task difficulty or metric bias rather than precision demand. The controls are how the experiment checks its own instrument before trusting its main result.

## Metric

The test is **retention relative to each task's own full-precision baseline**, not absolute accuracy. A hard task that starts at 60% has more room to fall than an easy one at 95%; comparing raw drops would compare apples to anvils.

For each task, at bit width *w* (here "width" means quantized bit depth — FP16, INT8, INT4, and so on):

> **R_w = mean(score at width w) / mean(score at FP16)**

The prediction becomes, within each matched pair, at the same width:

> **R_w(narrow) < R_w(broad)**

**Metric per task type is fixed before any results are seen.** Broad tasks use a tolerant metric (ROUGE, or a frozen LLM judge); narrow tasks use exact match. This asymmetry is *part of the hypothesis*, not a flaw: broad capabilities are broad partly because correctness tolerates equivalent phrasings, while narrow capabilities are narrow because small deviations flip correctness. A critic will nonetheless argue the metric difference *creates* the effect, so where possible, broad-task scoring should be calibrated against a small human-checked sample before the sweep, to confirm the tolerant metric tracks real quality. If an LLM judge is used, freeze the judge model, prompt, rubric, temperature, and output format — otherwise the evaluator becomes a second moving model.

**Guards.**
- Drop any pair scoring below ~0.20 at FP16 — retention ratios on near-floor tasks are noise.
- Flag any broad task above ~0.98 at FP16 — apparent stability may be a ceiling effect rather than true robustness.
- Report **both** retention and raw scores. Retention is the test; raw scores are the audit trail that keeps it honest.

**Sample size.** Aim for 50–100 items per task, or the retention curves jitter and a real bend can't be told from sampling variance. With only four pairs, any significance test (e.g. Wilcoxon over the deltas) is a directional check at best — the plot and bootstrap intervals carry more interpretive weight than a p-value over four points. Four pairs is a pilot, not a verdict.

**Optional, and worth it if tasks are step-structured:** log the index of the first failing step. "Narrow tasks degrade first" is a result; "narrow tasks degrade first *and* the failure localizes to an early step that then cascades" is a stronger one, and consistent with existing step-localization findings in the quantization-and-reasoning literature.

## The pre-declared decision rule

This is what makes it a measurement rather than a confirmation ritual.

- **If** the narrow half of each pair consistently retains less than its matched broad half at INT4 → the fragility axis has measurable bite, and it is worth expanding (more pairs, the salient-weight rescue test, then the provenance comparison).
- **If** two or more pairs reverse, or show bootstrap intervals on the paired retention difference that substantially overlap zero → **publish the flat result.** Do not rationalize it. A flat result means either the pair design needs work or the fragility axis needs a better formulation — and either is a real finding the framework should absorb.

The experiment must be able to come back "no." If it can only confirm, it is worthless.

## Where this sits in a larger program

This pilot is **Tier 0**. If it shows something, the natural sequence is:

- **Tier 1 — Rescue test.** Protect salient weights/channels and see which capabilities recover. This separates fine-spacing fragility from outlier-channel fragility — the two distinct mechanisms the companion paper argues can come apart.
- **Tier 2 — Provenance comparison.** Compare code-heavy vs. text-heavy (or world-model) variants, now that a within-model baseline exists. This is where provenance × fragility finally becomes testable.
- **Tier 3 — Pressure loop.** Add targeted high-checkability training examples, then rerun the suite, to ask whether pressure can *widen a narrow ridge* rather than merely raise raw accuracy.

Tiers 1–3 are not promised here. Tier 0 is the door.

## What a positive result would and would not mean

It **would** mean: precision demand predicts quantization sensitivity in a measurable, repeatable way — fragility is measurable under this probe, not merely descriptive. And if the directional signal holds, the retention curve becomes a yardstick other labs can adopt *without adopting the whole worldview* — the measurement stands on its own, and someone can run it, report it, and build on it while ignoring the river-and-canyon framing entirely. That portability is a feature: the protocol asks to be tested, not believed.

It **would not** mean: that the margin-geometry interpretation is confirmed, that provenance predicts fragility, or that the analogy in the parent papers is mechanically true. Those are separate questions requiring separate work. This tests one prediction. That is all it claims to do.

---

*Companion to* The River and the Canyon *and* What Kind of Water Carves the Mountain? *Proposed, not performed. If you have the compute and want to run it — or want to break the design — that is exactly the point of writing it down. Written by E. A. Flores, Apiana AI, Inc. Licensed CC BY-NC 4.0.*
