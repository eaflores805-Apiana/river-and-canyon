# Implications — A Scored Reference Index

*An index of what the River-and-Canyon framework implies, sorted by how well each implication is supported and how much it depends on the framework being right. This is a map, not a claim. Nothing here is presented as established by this work; the columns exist precisely to keep "interesting implication" from being mistaken for "demonstrated finding."*

> **Status: intake closed; refined against three rounds of external feedback; scores provisional.** Seven implication-sources were collected and merged (the last three added 2/0/0 new, confirming saturation); three feedback rounds then added a handful of verified boundary/method rows, two testable mechanism-dependent conjectures, and corrected one miscategorization (retention-baseline definition promoted to Tier A). Across all feedback the *center of gravity did not move*: A8 remains the only open, mechanism-independent, actionable question. Scores are the starting point for argument, not a verdict. The point of this document is sobriety — the highest-ranked items should be the most *boring and supported* ones, not the most exciting.

## How the scoring works

Each implication is scored on five axes. **None of them measures how exciting or high-impact the idea would be if true** — that axis is deliberately omitted, because it is the one that turns a reference index into a hype generator.

- **Evidence** — `Lit` (supported by external literature) · `Project` (supported by the project's own reasoning/mechanism) · `Hypothesis` (plausible, untested) · `Speculative` (a glimmer; downstream of other unproven claims).
- **Mechanism-dependent?** — does the implication require the river-and-canyon *account* to be correct? `No` is stronger: it survives even if the framework's explanation is wrong. *This is the most important column.*
- **Originality** — `Field` (the field established it) · `Synthesis` (the framework organizes/anticipates it but did not originate it) · `Ours?` (no clear prior art found — flagged with a question mark because "we didn't find it" is not "it doesn't exist").
- **Type** — `Mech` (mechanistic) · `Eval` (evaluation) · `Practical` · `Method` (methodological) · `Spec` (speculative-structural).
- **Actionable now?** — is there a concrete next step, or is it framing only?

A rough **Confidence tier** (A/B/C) summarizes the first two columns: **A** = supported and/or mechanism-independent; **B** = plausible but unproven; **C** = speculative, preserved-not-promoted.

---

## Tier A — Supported and/or mechanism-independent

The core. These are the ones to trust and lead with.

| # | Implication | Evidence | Mech-dep? | Originality | Type | Actionable? |
|---|---|---|---|---|---|---|
| A1 | **Analogies earn their keep by generating *testable distinctions*, not by feeling explanatory.** The image's job is to open questions; measurement carries the answer. The transferable *procedure* is **de-imaging**: strip the metaphor, restate the claim as bare mechanism, and keep only what survives the restatement (the no-mountain / no-force test). | Project | No | Synthesis | Method | No — it's the method itself |
| A2 | **The training/inference distinction is best understood as what's *fixed* vs. what's *transient*** (permanence/transience), not as a surface metaphor. | Project | No | Synthesis | Mech | No — framing |
| A3 | **Quantization is not only compression; it can act as a diagnostic stress test** — coarsening asks which structures survive reduced precision. | Lit | No | Synthesis | Eval | Partly — it's the probe's basis |
| A4 | **Fluent behavior can survive while exact reasoning quietly degrades.** Surface competence is not a proxy for load-bearing capability — the deployment-risk implication. | Lit | No | Synthesis | Eval | No — but it motivates A8 |
| A5 | **Precision-demand matters: capabilities differ in fragility under coarsening.** Math/reasoning degrade disproportionately; broad language is more preserved. | Lit | Partly | Field | Mech | No — established |
| A6 | **Failures may localize at the first fragile step, then cascade** — not degrade uniformly across a task. Logging the first-failing-step index would be stronger evidence than retention alone. | Lit | Partly | Synthesis | Mech | Yes — protocol logs it |
| A7 | **Provenance shapes the mix, not the fate.** Training origin shapes *which* structures form, but does not by itself determine any capability's fragility — blocks "code-trained = exact, text-trained = fuzzy." | Lit | Partly | Field | Mech | No — established |
| A8 | **The most practical open question: does stress-retention predict deployment reliability better than peak accuracy?** Inherits *none* of the framework's explanatory burden. The pilot needs only (a) some capabilities are more precision-sensitive and (b) we've been under-measuring it — not the geometric account. | Hypothesis | **No** | Ours? (concept active; clean head-to-head maybe open) | Eval/Practical | **Yes — the priority experiment** |
| A9 | **Inference is passive: there is no active driving force during a forward pass.** The activation trajectory is the direct evaluation of a fixed function, layer by layer — no minimization, path-search, or relaxation toward equilibrium. "Force" in these systems is rarely primary; structure is primary, force its derivative. | Project | No | Synthesis | Mech | No — framing, but it disciplines force-talk |
| A10 | **FlashAttention / memory-efficient attention are *safe* optimizations** — exact up to floating-point rounding; they change data movement, not geometry. The framework's lone *negative* implication: a class of changes it says you do *not* need to worry about. | Lit | No | Synthesis | Mech | Yes — deploy without capability-loss concern |
| A11 | **Weights are immutable at inference — permanence is an operational guarantee, not a metaphor.** You can run unlimited inferences without model drift; any serving-time "learning" must be *external* (KV-cache, tools, retrieval), never weight change. | Lit | No | Synthesis | Mech | Yes — treat the model as frozen; state lives outside it |
| A12 | **The quantization claims are scoped to *post-training* quantization only** — a verified boundary, not a hedge. QAT changes the carving process itself, so the probe says nothing about QAT pipelines. | Lit | No | Synthesis | Method | Yes — prevents overclaiming to QAT/hardware teams |
| A13 | **Retention must be measured relative to each task's *own* full-precision baseline.** This is a measurement *definition* (not a hypothesis) — it prevents the error of comparing raw drops across tasks of different base difficulty. *Promoted from Tier B: a definition cannot be "unproven," only adopted.* | Project | No | Synthesis | Method | Yes — defines the metric |

## Tier B — Plausible, unproven by this work

Real ideas, properly hedged. Not to be presented as more than hypotheses.

| # | Implication | Evidence | Mech-dep? | Originality | Type | Actionable? |
|---|---|---|---|---|---|---|
| B1 | **Architecture is part of the substrate, not a passive container, and governs *failure continuity*** — a dense transformer degrades via smooth, continuous trajectory drift under coarsening; a sparse MoE is prone to *discontinuous step-function* failure when a router-logit flip misroutes activation into a foreign expert. Testable via the *smoothness (derivative) of the retention curve*: smooth = dense-style, cliff = router-flip. | Hypothesis | Yes | Synthesis | Mech | Yes — compare derivative of dense vs. MoE retention curves |
| B2 | **Models are non-uniformly load-bearing** — a small minority of weights/channels carry disproportionate importance; capability is not evenly smeared. *The phenomenon is field-established (Tier-A-grade evidence); the framework's geometric **reading** of it ("these are the load-bearing ridges") is what keeps the row at B — phenomenon confirmed, interpretation not.* | Lit | Partly | Field | Mech | No — established (salient-weight work) |
| B3 | **Chain-of-thought is robust because it's *distributed*** — spreading a computation across externalized tokens gives more margin to lose before failure; not a new skill, a different physical implementation. | Lit | Partly | Synthesis | Mech | Maybe — testable via retention on CoT vs. compressed |
| B4 | **The training *objective* shapes fragility, not just the data** — reward-only-the-answer compresses steps into one brittle transition; reward-the-chain distributes them. Reward hacking as a fragility phenomenon. | Hypothesis | Yes | Synthesis | Mech | Hard |
| B5 | **"Usable capability" may differ from apparent capability** — a behavior can show under comfortable conditions without a structure that survives stress. (The bridge held on a sunny day.) | Hypothesis | Yes | Ours? | Eval | Via A8 |
| B6 | **Capacity and usable structure may be separable** — a model may have representational room for a capability without having carved a stable load-bearing path for it. | Speculative | Yes | Ours? | Mech | No — glimmer (seed note) |
| B7 | **Capability should be described by retention profiles, not just peak scores** — measure what survives under a *declared battery* of stresses (quantization, long context, adversarial phrasing, distribution shift, tool use, routing). | Hypothesis | No | Synthesis | Eval | Via A8 |
| B9 | **A flat result would still be informative** — this is a *design property* of the probe (it can come back "no"): a null means the pair design or the fragility axis needs reformulation. Not a hypothesis about models; a property of the experiment. | Project | No | Synthesis | Method | Yes — built into protocol |
| B10 | **Mechanistic localization matters more than task labels** — "fine spacing, salient channels, router flip, first-error step" are less mushy than "reasoning/math/code." | Hypothesis | Partly | Synthesis | Mech | Partly |
| B11 | **The Gradeability Mandate** — language carves broad/forgiving structure, so LMs may not self-generate sustainable synthetic data without *external checkable constraint* (compilers, verifiers, sandboxes, simulators). To scale synthetic without collapse, bind generation to formal graders. | Hypothesis | Partly | Synthesis | Practical | Partly — testable in synthetic pipelines |
| B12 | **Catastrophic tail erosion** — recursive training on uncurated synthetic data preferentially erodes low-density tails (rare, fine distinctions). *Collapse is documented; the "narrow-structure-first" mechanism is the framework's interpretation, not measured.* | Lit (collapse) / Hypothesis (mechanism) | Partly | Field/Synthesis | Mech | No |
| B13 | **The rescue test** — protecting salient weights and seeing what recovers *separates* fine-spacing fragility from outlier-channel fragility. Quantize, re-enable a salient-weight mask, measure which tasks return. = Tier 1 of the fragility protocol. | Hypothesis | No | Synthesis | Method | **Yes — concrete, cheap, possibly 2nd-most-actionable after A8** |
| B14 | **Cross-lineage model merging** is governed by parameter-geometry compatibility (re-basining / permutation alignment), not shared ancestry — disparate lineages merge if they can be permuted into a common low-loss basin. | Hypothesis | No | Field | Mech | Hard (permutation discovery is its own problem) |
| B15 | **The polysemantic interpretability wall** — superposition means features bleed across near-orthogonal directions; complex capabilities live as distributed webs, not clean channels. *Distinct from B2:* not "few weights carry load" but "concepts can't be cleanly isolated." (Sparse dictionaries partially un-mix.) | Lit | Partly | Field | Mech | Partly (directions/subspaces, not single units) |
| B16 | **SLAs/contracts move to "accuracy under declared stresses."** A model is qualified only for stresses it was tested against; contracts specify bit depth, context length, shift; exceeding them requires re-qualification. *Consequence of A8 — inherits its "if."* | Hypothesis | No | Ours? | Practical | No (gated on A8) |
| B17 | **Per-capability bit budgets beat uniform quantization** — keep high precision for the few fragile channels/layers, low elsewhere; mixed precision *by capability*, not by layer size. (Software/pipeline version; distinct from the hardware row.) | Hypothesis | Partly | Synthesis | Practical | Hard (needs reliable localization) |
| B18 | **Data provenance becomes model-card documentation** — if origin predicts fragility, users need lineage to estimate it; model cards include provenance fractions + stress tests run. | Hypothesis | No | Ours? | Practical | Partly |
| B19 | **Architecture–provenance *fit* as a design principle** — capability = medium × architecture × objective; code+MoE may need router-stability regularization, video/sim+SSM temporal-consistency objectives. More specific than B1. | Hypothesis | Yes | Synthesis | Mech | Hard (no proven pairings) |
| B20 | **Silent alignment decay** — alignment/guardrails are precision-demanding, so may fracture first under compression: model stays polite/fluent while fine-grained safety boundaries erode. ⚠️ *Important + plausible + UNPROVEN. Source stated it as fact; demoted. The defensible version is "test safety under stress," not "quantization destroys alignment." Importance must not inflate evidence — watch hardest when scoring.* | Hypothesis | Yes | Synthesis | Eval | Partly — run safety evals across bit-depth ladders |
| B21 | **First-error-step index is a stronger evaluation signal than aggregate retention** — reporting *where* a task first breaks (median first-failing step) distinguishes margin-collapse from later cascade. The *evaluation* form of A6. | Lit | Partly | Synthesis | Eval | Yes — report median first-failing step alongside retention |
| B22 | **Fine-tuning preserves the base model's fragility profile unless it applies targeted pressure at fragile crossings** — follows from permanence (fine-tuning is bounded erosion, not remelting). Explains why LoRA on broad data rarely improves math robustness, but LoRA on near-miss traces sometimes does. | Project | Partly | Synthesis | Mech | Partly — testable via fragility profile before/after FT |
| B23 | **The rescue test for *mechanism*: salient-weight protection separates fine-spacing from outlier-channel fragility.** (See B13.) A second framing emphasizes the *evaluation* payoff: the recovered-vs-not split tells you whether to fix *training* (spacing) or *architecture* (outliers). | Hypothesis | No | Synthesis | Method | Yes — see B13 |
| B24 | **Information collapse under compression may occur at the attention weighted sum (A×V), not at softmax** — softmax is near-order-preserving; the A×V blend is where token identities merge irreversibly. ⚠️ *A mechanism-dependent conjecture, not established; the "collapse is at A×V not softmax" localization is unverified.* | Hypothesis | Yes | Synthesis/Ours? | Mech | Yes — separate quantization ladders on QK^T vs. V/O projections |
| B25 | **KV-cache eviction may be *dual* to weight-quantization** — both coarsen (one in parameter-space, one in temporal-context-space), so aggressive cache-eviction degradation should map onto the *same* task-dependent fragility ranking as bit-depth reduction. | Hypothesis | Yes | Ours? | Eval/Method | Yes — rank-correlate eviction-ladder vs. quantization-ladder retention |
| B26 | **Retention-curve *shape* is a structural fingerprint** — gradual decay across bit-depths implies *distributed* (redundant) structure; a sharp cliff implies *concentrated* (brittle) structure. | Hypothesis | Partly | Synthesis/Ours? | Eval/Mech | Yes — use curve shape, not just endpoint, as a diagnostic |
| B27 | **Some fragility is structural and cannot be fixed by prompting** — if a capability was carved shallowly, inference-time prompting cannot deepen it (permanence: prompting doesn't change weights). Identifies a class of "unfixable-by-prompting" failures. | Hypothesis | Yes | Synthesis | Mech | Yes — fragility probe flags capabilities prompting can't rescue |
| B28 | **Cross-stress fragility correlation** — if a fragility signal is capability-level rather than a quantization-format artifact, the *same* narrow tasks should retain less than their broad partners under a *second* stress (activation noise, pruning, layerwise quant, KV-truncation), and the task-retention rank order should correlate across stresses. Stable ranking → general fragility signature; divergent ranking → stress-specific mechanisms. Mechanism-independent; the test that would upgrade the probe from "quantization-sensitivity test" to "general fragility probe." *Protocol track 1c; contingent on Tier 0 producing a signal first.* | Hypothesis | No | Ours? | Eval/Method | **Yes — rerun matched pairs under a second stress, rank-correlate retention** |

## Tier C — Speculative, preserved not promoted

Kept because they're worth not losing. Clearly marked as glimmers. None drives a decision.

| # | Implication | Evidence | Mech-dep? | Originality | Type | Actionable? |
|---|---|---|---|---|---|---|
| C1 | **The most precious training data may not be the most voluminous** — a small targeted dose of sharper flow makes broad cheap flow load-bearing (the LoRA / quantization-recovery / action-grounding pattern). | Speculative | Yes | Synthesis | Spec | No |
| C2 | **Better models may come from diagnostic-guided repair, not just scale** — find weak crossings, apply targeted high-structure data, retest retention. | Speculative | Yes | Ours? | Practical | No (gated on A8) |
| C3 | **Training media sit on a causal ladder** — observation (video) < intervention (simulation) < consequence (action); higher rungs may carve more transferable, less spurious structure. | Speculative | Yes | Synthesis | Spec | No |
| C4 | **Three distinct evaluation questions, not one** — "knows" vs. "can use" vs. "can retain under stress" may come apart. | Speculative | Yes | Ours? | Eval | No (subsumed by A8/B7) |
| C5 | **Some AI failures may be invisible at the surface** because the broad basin survives while the narrow exact operation is lost — the user notices halfway across the missing bridge. | Hypothesis | Partly | Synthesis | Eval | No (this is A4 applied) |
| C6 | **Provenance × fragility as a model-comparison space** — compare code/text/video/sim/action-trained models by what survives coarsening. (Substantial prior art on composition→robustness; the quantization-retention version is narrower.) *Per-medium predictions, all speculative, are instances of this row, not separate findings: video-trained → temporally-robust but symbolically-fragile; simulation-trained → causally-robust under counterfactual perturbation; action-trained → uniquely load-bearing. Each lacks direct quantization-retention evidence.* | Speculative | Yes | Field/Synthesis | Spec | Hard |
| C7 | **The normalization plumbing artifact** — activation outlier channels (targeted by quantization compilers) may be a *numerical byproduct* of normalization × high-frequency tokens, not a measure of conceptual density. ⚠️ *Stated as fact by two sources; it is a CONTESTED interpretation (outlier-feature work treats these channels as important). Demoted to Speculative. If true, it's a confound for A3/A5 — fragility may partly reflect plumbing, not precision-demand. The rescue test (B13/B23) is what would separate them.* | Speculative | — | Field (contested) | Mech | No |
| C8 | **Split-domain silicon** — because capabilities are lumpy, uniform-precision hardware is inefficient; future chips might route ultra-low-bit semantic cores + high-precision gates triggered on fine-spaced ridges. ⚠️ *Hardware-futures speculation, several floors down; source overstated ("point toward"). Heavily hedged.* | Speculative | Yes | Synthesis | Spec | No (massive scheduling hurdle) |
| C9 | **Geometric vulnerability probing** — jailbreaks/injections as locating thin-curvature ridges where a minimal perturbation spills the flow into an unaligned valley. ⚠️ *Elegant reframe, stated confidently by source; speculative. Preserved, not promoted.* | Speculative | Yes | Ours? | Spec | No |
| C10 | **Provenance auditing as a safety control** — if action-trained policies carve consequence differently than language-trained ones, deployed agents might disclose training-pressure types. *Consequence-of-a-consequence; institutional; far downstream.* | Speculative | Yes | Ours? | Practical | No |
| C11 | **Quantization might detect shortcut reliance** — brittle heuristics (pattern-matching instead of reasoning) rely on narrow distinctions, so should break early under coarsening. ⚠️ *Self-defeating confound: cannot currently distinguish shortcut-fragility from genuine precision-fragility, which is exactly what would make it a usable detector. Glimmer only.* | Speculative | Yes | Ours? | Eval | No (confounded) |
| C12 | **The three-register discipline is required to keep the framework honest** — analogy, mechanism, and measurement must never share a sentence; the translation table stays qualitative to prevent false precision. *Not a finding about models; a guardrail for using the framework without smuggling commitments. (The method the whole index enacts.)* | Project | No | Synthesis | Method | No — it's the operating discipline |

---

## What the table shows at a glance

The pattern is the point, and it is a *disciplining* pattern:

- **Only a handful of implications are both a real open question AND mechanism-independent: A8, B13, A10** stand out. A8 (retention-vs-accuracy) is the live, in-wheelhouse experiment; B13 (the rescue test) is the cheapest concrete follow-on and separates two fragility mechanisms; A10 (FlashAttention-safe) is the lone *negative* implication — the only one marking what the framework says you *needn't* worry about, which is disproportionately valuable as a boundary. Everything else is established-by-field, framing/synthesis, or hedged hypothesis.
- **The mechanism-independent column is the real map.** Strip out everything that needs the river-and-canyon *account* to be right, and the durable core is: **A1–A4, A8, A9, A10, A11, A12, A13, B7, B9, B13, B23, B28, C12** — framing, boundary conditions, measurement definitions, the safe-optimization and out-of-scope markers, and above all **A8** (the open question), **B13/B23** (the rescue test), and **B28** (cross-stress validation, which would distinguish a real fragility signature from a format artifact). These survive even if the metaphor is wrong. Everything marked `Yes` or `Partly` inherits the framework's risk.
- **Originality is mostly `Field` or `Synthesis`.** The searches confirmed it: the framework's value is organizing-compression, not discovery. Every `Ours?` carries a question mark because "not found" is not "not there."
- **The exciting items cluster in Tier C, and several arrived overclaiming** (C7 normalization-artifact, C8 split-domain-silicon, C9 vulnerability-probing, plus B20 silent-alignment-decay) — stated as fact by their sources, demoted here to their real evidence level. That excitement and evidence are inversely correlated is *why* we score for evidence, not excitement.

## Implications vs. consequences — a structural caveat

A large share of the collected material (especially the domain-by-domain "what changes if this holds" lists) consists of **consequences, not implications.** The distinction matters:

- An **implication** is what the framework *claims* (e.g. "capabilities differ in fragility").
- A **consequence** is what the world *looks like* if the claim holds (e.g. "therefore leaderboards add a retention column," "therefore SLAs specify bit depth," "therefore chips route precision dynamically").

The consequences are vivid and operational, which makes them *feel* solid — but their entire support is inherited from the premise above them, and most premises here are hypotheses (A8 especially). **Specificity is not evidence.** A precisely-described consequence of an unproven premise is still unproven; it has simply been rendered in more convincing detail. The rows above marked "consequence of A8" or "far downstream" (B16, C10, much of the hardware/safety material) are kept for foresight value, not because the detail makes them more established. Read them as "*if* the core qualification claim survives, here is the shape of what follows" — never as independent findings.

A methodological note that strengthens the probe (B8/B9): any fragility contrast must include **negative controls** — a broad–broad and a narrow–narrow pair scored with identical strictness, which must show *no* within-pair retention gap. If they do, the apparent fragility signal is contaminated by task difficulty or metric bias. This is the control that separates a real effect from "benchmark soup in a lab coat."

## A note on this document's own discipline

This index exists to *resist* the temptation it could easily feed. Scoring implications in a tidy table makes every one of them feel more solid than prose would. The guard is the omitted column: there is no "impact if true" score, because that is the number that would let a Tier-C glimmer outrank a Tier-A observation. If a future version of this document starts ranking by interestingness, or starts reading like an argument that the implications are established, it has drifted from index to advocacy — and should be pulled back.

*Working reference, Apiana AI. Intake ongoing. Scores provisional and meant to be contested.*

---

# Insights — what the closed table shows

*This section is interpretation, not more rows. It synthesizes what emerged when the table above was read as a whole — by the author and by several independent reviewers who converged, without coordination, on the same conclusions. The table is the asset; this is the reading of it.*

## The center of gravity is tiny — and that is the point

Of 50-plus rows, only a handful are both **mechanism-independent and actionable now**: **A8** (does retention-under-stress predict deployment reliability better than peak accuracy), **B13/B23** (the rescue test, which separates fine-spacing fragility from outlier-channel fragility), and **A10** (FlashAttention-class optimizations are safe). Everything else either inherits the river-and-canyon story or is already established by the field. That convergence is not a weakness — it is the honest signature of a framework that was stress-tested to failure and audited against the literature, and came out the other side with its real contribution clarified rather than inflated.

## The framework's durable contribution is method and measurement, not new mechanism

When you filter Tier A strictly, what dominates is **framing** (A1, A2, A9), **verified boundaries / negative implications** (A10, A11, A12), and **measurement definitions** (A3, A13). The most trustworthy outputs of the whole project are *what the analogy does not let you claim* and *how to measure cleanly* — not new facts about how transformers work. The methodology is the contribution at this stage, more than any single mechanistic claim. The portable asset is the procedure named in A1: find the variable underneath, render it as physical structure, read off the next question, then **de-image** — strip the metaphor and keep only what survives as bare mechanism.

## The mechanism-independent column is the real spine

The A/B/C tier label matters less than the **Mech-dep?** column. A Tier-B idea that is mechanism-independent can be more practically valuable than a Tier-A idea that is only a field observation, because the mechanism-independent ones survive even if the geometric account is merely a useful picture rather than a literal description of parameter space. This filter is the single most useful way to read the index when deciding what to lead with externally or where to spend research effort.

## Excitement and evidence are inversely correlated here

The vivid, operational items — silent alignment decay, split-domain silicon, stress-based SLAs, dynamic-precision hardware — cluster in Tier C and carry overclaim flags. **Specificity is not evidence.** A precisely-rendered consequence inherits 100% of its risk from the unproven premise beneath it. The enthusiasm clusters exactly where the evidence is thinnest, which is precisely why the table scores for evidence and not for excitement. Keeping these rows in Tier C is what prevents building expensive scaffolds over unmapped ground.

## Negative implications and boundaries are doing quiet heavy lifting

A framework that only produces alarms is a smoke detector with anxiety. This one produces clean negatives: A10 (what's safe), A11 (weights immutable at inference), A12 (scoped to post-training quantization only), B9 (a flat result is still informative), C12 (the three-register discipline itself). These tell practitioners what they do *not* need to worry about and where the framework stops applying — and that boundary-drawing is what earns trust.

## The minimal viable research program

A8 and B13 form a short, falsifiable sequence: (1) does retention under stress add predictive value beyond peak accuracy? — and if so, (2) does protecting salient channels recover some capabilities but not others, separating the two fragility mechanisms? **If A8 is the pilot, B13 is the diagnostic that tells you whether to chase training (fine-spacing) or architecture (outliers) next.** Note that B13 is also what would *decide* the contested C7 (normalization-artifact) question — it is not assumed; it is tested.

## A future direction, recorded but not built: stress-retention as MI triage

Future mechanistic work should treat stress-retention as a triage signal, not a circuit localizer: quantization and related stresses may identify behaviors whose margin or error stability makes them valuable targets for activation patching, ablation, salience analysis, or other mechanistic tools, but no mechanistic claim should be made until a later stage supplies causal evidence. This is recorded as a direction, not built — the handoff schema, matched-twin selection, and dataset manifest such a bridge would require are post-run artifacts that must be shaped by actual Tier 0 outputs, not by an imagination of what those outputs might look like. Designing that infrastructure before the run is the loading-dock-before-the-truck error; the schema waits for data because the data is what should design it. See `diagrams/boundary-venn-insights.md` for the spatial form of this boundary rule: behavioral measurement is complete work, not incomplete mechanism.

## The one-line summary

> The framework's most robust and actionable contribution is not a new explanation of why capabilities are fragile. It is a disciplined way to *ask* whether they are, a clean measurement language for *testing* it, and a short list of things the picture does *not* let you claim. The live empirical question it leaves the field is narrow and well-posed: **does retention under stress predict real deployment reliability better than peak accuracy, and can a cheap rescue test separate the mechanisms?**

The analogy's value is that it generated these testable distinctions and then got out of the way — it is logically *un*necessary to defend the conclusions, though it was necessary to *find* them. The scaffold came down once the building stood. The claim map is complete; the physics must now decide.

*Insights compiled from the author's reading and several independent reviews that converged on the same center of gravity. Synthesis, not data — the scored table above is the reference of record.*
