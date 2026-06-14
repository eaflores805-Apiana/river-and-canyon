# The Gate That Refused Its Authors: Construct-Validity Enforcement at the Baseline of LLM Stress-Retention Evaluation

*Working title (alt): Before Retention — A Fail-Closed Validity Gate for Stress-Retention Evaluation*

E. A. Flores · Apiana AI, Inc.

---

## Abstract

Quantizing a model and measuring which behaviors "survive" is a common way to ask whether compression damages capability. We argue that this measurement is unsafe unless the baseline it is compared against is first shown to measure the intended capability at all. A retention score is a comparison against a baseline; if that baseline rests on a shortcut, saturates at ceiling, or is mis-scored, the retention number inherits the defect and reports it as preserved capability.

We built a fail-closed validity gate for this setting and exercised it on a synthetic multi-hop task family, and it refused a baseline its own authors were trying to construct. The gate is a staged protocol that enforces construct validity at the baseline — whether the baseline measured the intended capability at all — as a precondition on a retention claim, and whose output is a route decision, including *not safe to compare*, rather than a score. The field has diagnosed evaluation-validity failure at length (shortcut learning, construct-validity gaps, abstention fragility, scorer artifacts, quantization-induced degradation), and a recent certification literature already enforces the statistical reliability of judges and outputs and emits refusal as a first-class result. Our contribution is narrower and complementary: it certifies the baseline itself, rather than the measurement process, and does so at the per-item and provenance level, in the specific setting of a stress-retention comparison.

That refusal is the paper's central evidence that the gate is non-vacuous — that it blocks baselines that would otherwise pass. A difficulty manipulation lowered clean accuracy — the sought-after result — but per-item inspection showed it had collapsed the model's abstention on absence-defined items, so the baseline no longer measured the intended construct, and the protocol refused it on the observable validity failure. We report which gates are implemented and exercised on the family (baseline certification, strict-versus-concept scorer audit, four-way reporting of absence-defined behavior, a construct-validity gate, provenance control) and which remain specified (same-error identity, the rejection audit as a standing component, cross-family generality, the full stress pipeline). The claim is methodological and bounded: before a retention comparison can be interpreted, the baseline must be certified to measure the intended construct, and in this program the staged instrument refused a baseline that surface metrics passed.

## What we do not claim

We do not claim that a compositional seam exists or does not exist. We do not claim to have measured compression fragility: the program is pre-stress, and no certified baseline has been carried through an executed compression rung. We do not claim a validated general method — the demonstrations are drawn from one synthetic task family on one open-weights model (Qwen2.5-3B, FP16). We do not claim to have discovered shortcut learning, construct-validity failure, or abstention instability; each is field-owned, and our contribution is the fail-closed enforcement architecture, not the underlying concepts. We do not claim a product or a market-validated tool. What the instrument has done, it has done on baselines the present authors themselves constructed; establishing cross-family generality, demonstrating the gate on an externally constructed evaluation, and carrying a certified baseline through a stress rung are stated as required future work, and are the substance of the planned follow-on (Paper B).

---

## 1. Introduction

### 1.1 The baseline-inheritance problem

A natural way to ask whether weight quantization harms a capability is to run a task at full precision and at a low bit-depth, compute how much of the behavior is retained, and read a drop as evidence of damage. The method is tempting and, as stated, unsafe — not because retention is the wrong quantity, but because of what retention is measured against.

A retention score is a comparison against a baseline. If the baseline rests on a shortcut, the retention number measures how well the shortcut survives. If the baseline saturates at ceiling, there is no headroom for a drop to be visible, and retention reports stability that the task could not have revealed. If the baseline is mis-scored — a parser miscategorizing the model's output — the retention number inherits the scoring artifact. In every case the defect is laundered: a number that looks like preserved capability is in fact preserved shortcut, preserved ceiling, or preserved parser error. The baseline's defects are inherited by every measurement taken against it, and a retention metric, by construction, cannot see them.

This is the upstream half of a problem the program's first paper named downstream: survival is not correctness — a component that still emits under stress is not thereby emitting correctly. The present paper addresses the precondition: even before stress is applied, the baseline must be shown to measure the intended capability, or the retention comparison is uninterpretable regardless of what the model does under compression.

### 1.2 The refusal, in miniature

The clearest evidence that this precondition has teeth is a case from our own program in which it refused a result we wanted.

In constructing a calibration baseline for a synthetic key-value lookup family, every content-based attempt to move the clean baseline off its accuracy ceiling failed: the model remained saturated, leaving no headroom to measure a future degradation. A query-side manipulation — an in-prompt code-book requiring the model to resolve an alias before performing the lookup — finally produced the first off-ceiling clean point. By the surface objective, off-ceiling difficulty, this was the result we were trying to construct.

The protocol refused it. A per-item inspection showed that the query-form change had coincided with a collapse of the model's abstention on absence-defined (key-absent) items: the model emitted a value on every such item where it had previously abstained, with measured abstention falling from approximately 0.92 to 0.00 on otherwise identical content. The off-ceiling baseline was off ceiling because it had stopped measuring key-presence discrimination — not because the intended capability had become harder. The pre-declared decision rule classified this as a construct-validity failure of the difficulty lever and blocked the baseline, before any retention comparison was permitted.

### 1.3 Contribution

We describe a fail-closed validity gate for stress-retention evaluation: an ordered set of checks applied to a baseline whose output is a route decision — pass, needs repair, quarantine, or refuse — rather than a score, and in which the absence of construct validity at the baseline yields a logged refusal rather than a retention number. The contribution is not the recognition that evaluations can be invalid, which is field-owned and surveyed in §2; it is the enforcement architecture — a gate that does not let a claim through — together with a worked demonstration that the gate refuses a baseline that surface metrics passed, including one the authors were motivated to accept. We state plainly throughout what is implemented and exercised versus specified but unbuilt (§4), and we bound the contribution to what one synthetic family on one model can support (§6).

---

## 2. Background and Related Work

### 2.1 The field has diagnosed evaluation-validity failure

A substantial body of work establishes that benchmark scores can fail to measure the capability they are taken to represent. Geirhos et al. (2020) characterize shortcut learning — decision rules that perform well on a benchmark but rely on spurious cues and fail to transfer — as a unifying account of many deep-learning failures (arXiv:2004.07780). For language models specifically, a systematic review of 445 benchmarks by Bean et al. (2025) documents widespread weaknesses in how phenomena are operationalized, how tasks are constructed, and how metrics are chosen, and argues these weaknesses undermine the validity of the resulting claims (arXiv:2511.04703). Freiesleben and Zezulka (2025) develop construct-validity conditions for predictive benchmarking from psychometric measurement theory (arXiv:2510.23191), continuing a line that includes Evidence-Centered Benchmark Design (2024, arXiv:2406.08723) and earlier critiques of benchmark validity (Raji et al. 2021). Reproducibility-focused infrastructure such as the LM Evaluation Harness (Biderman et al. 2024) addresses a complementary problem — consistency of measurement across runs and models — while explicitly bracketing validity (arXiv:2405.14782).

Two adjacent literatures bear directly on the present setting. First, abstention: AbstentionBench (2025) shows that frontier models systematically fail to abstain on unanswerable questions, that the failure is not resolved by scale, and that reasoning fine-tuning degrades abstention by roughly 24% on average (arXiv:2506.09038; NeurIPS 2025); a survey catalogues the broader abstention literature (Wen et al., "Know Your Limits," TACL vol. 13, 2025). Second, compression: low-bit quantization is known to degrade reasoning specifically, with reported losses up to roughly 32% on mathematical reasoning under aggressive INT4 schemes and a pronounced sensitivity for smaller models (Quantization Meets Reasoning, 2025, arXiv:2501.03035; ZeroQuant-V2, arXiv:2303.08302).

We take all of the above as established. This paper does not claim to discover that evaluations can be invalid, that models exploit shortcuts, that abstention is unstable, or that compression degrades reasoning. Each is field-owned, and several are the subject of recent, prominent, large-scale studies.

### 2.2 The gap: diagnosis is not enforcement

The work above is, with few exceptions, diagnostic or advisory. It identifies validity failures, surveys their prevalence, and — at its most operational, in Bean et al. (2025) — provides a checklist that benchmark authors are encouraged to consult during design and to report as an appendix. A checklist of this kind is a valuable instrument for improving practice. It is also, by construction, non-binding: it advises an author, who remains free to proceed past an unmet item. Its unit of action is the conscientious researcher. An advisory checklist improves the probability that such an author notices a problem; it does not prevent a pipeline from emitting a retention number whose baseline was never certified to measure the intended construct.

The present work addresses a different unit of action. In the specific setting of stress-retention evaluation — measuring whether a capability survives a controlled degradation such as quantization — the central risk is not only that an author overlooks a validity concern, but that a pipeline emits a retention number whose baseline was never certified to measure the capability in the first place. We therefore propose to move validity discipline from advice to enforcement: a fail-closed protocol in which a stress-retention claim is not emitted unless a verified clean baseline, a validated scorer, an artifact-locked provenance trail, and a certified construct are all present, and in which the absence of any one yields a logged refusal rather than a number.

### 2.3 Relation to fail-closed certification of evaluation

Enforcement and refusal are not, by themselves, new. A recent line of work already treats evaluation as something to be certified rather than merely reported, and already emits abstention or rejection as a first-class output with formal guarantees. We engage it directly, because it is the closest prior art and the distinction from it is what defines our contribution.

*Noisy but Valid* (2026, arXiv:2601.20913) certifies whether an LLM's failure rate lies below a safety threshold under an imperfect judge, deriving a variance-corrected critical value that guarantees finite-sample Type-I error control: a genuine accept/reject gate on an evaluation. *Selective Risk Certification* (2025, arXiv:2509.12527) issues information-lift certificates with formal abstention guarantees, emitting refusal as a first-class output under bounded risk. *Safety Under Scaffolding* (2026, arXiv:2603.10044) runs a pre-registered specification-curve analysis across scoring degrees of freedom and finds, among other things, that changing answer format on identical items shifts measured scores by 5–20 points — larger than the effect under study — the same scorer- and format-sensitivity our own reporting is designed to surface.

Against this work, "we enforce, the field advises" is too strong a claim, and we do not make it. These methods enforce, and they emit refusal. They differ from the present work in the object they certify. They take the construct as given and certify properties of the measurement process: a judge's error rate, or whether a given output is reliable enough to answer rather than abstain. The present work certifies a property of the baseline itself — whether it measured the intended capability at all (shortcut-free, off-ceiling, correctly parsed) — before any retention comparison is permitted. Three things follow from this shift of object: the trigger is not a bounded error rate but an uncertified construct; the gated object is not a single measurement but a relative survival claim across a controlled degradation; and the integration point is a per-item, provenance-locked read rather than a distributional guarantee. We share the enforcement posture and refusal-as-output with this literature, and claim only this cell — construct-validity enforcement on the baseline of a stress-retention comparison, with per-item and provenance integration. None of these three certification methods addresses stress-retention or compression evaluation; each certifies a property of a measurement taken in isolation, whereas the construct-validity gate is a precondition specifically on a relative survival claim across a controlled degradation. The retention setting is therefore part of the cell being claimed, not incidental to it.

---

## 3. The Worked Case: A Gate That Refused Its Authors

This section expands §1.2 in full. It is the paper's central evidence that the gate is non-vacuous — that it blocks things that would otherwise pass, including artifacts the authors were motivated to accept. We report it as a development episode and an instrument demonstration, not as a finding about model behavior; the negative-use scope on the per-item numbers is stated at the end of the section.

### 3.1 The construction and the difficulty lever

The task family is a synthetic, closed-world key-value lookup: each item presents a set of key-value facts and queries one key, with absence-defined (key-absent) items included so that correct abstention is part of the measured construct. A valid baseline must do two things — return the correct value when the key is present, and abstain when the key is absent — because the capability under study is key-presence discrimination, not value emission alone.

The clean baseline saturated at ceiling: the model performed the lookup essentially perfectly, leaving no headroom in which a future compression-induced drop could be measured. A baseline at ceiling cannot serve as a retention substrate, because retention is computed relative to the baseline and a ceiling baseline can only stay flat or fall to the floor. We therefore sought a difficulty manipulation that would lower clean accuracy into a measurable band while preserving the construct. (Figure 1 plots the full calibration sweep against the certifiable region: every content-lever candidate sits at the ceiling wall, and the one off-ceiling candidate falls to the discrimination floor — the certifiable region is empty.)

![**Figure 1.** No candidate baseline lands in the certifiable region. Clean accuracy versus defective discrimination for the five calibration candidates; the certifiable region (off-ceiling band, discrimination preserved) is shaded. Four content-lever candidates sit at the ceiling wall with discrimination intact; the one off-ceiling candidate (CAL-Q) falls to the discrimination floor. The certifiable region is empty. Synthetic key-value family, Qwen2.5-3B (FP16); evidence about the instrument, not the model.](figures/fig1_certification_box.png){width=80%}

Content-based manipulations failed to move the ceiling. A query-side manipulation succeeded: an in-prompt code-book required the model to resolve an alias before performing the lookup. This produced the first off-ceiling clean point. By the surface objective — off-ceiling difficulty with a still-high clean score — this was the baseline we were trying to build.

### 3.2 The refusal and the per-item finding

The protocol refused the baseline. The refusal followed from a per-item inspection rather than from the aggregate score, which the surface metrics passed.

The inspection showed that the query-form change had coincided with a collapse of the model's abstention on absence-defined items. On key-absent items the model now emitted a value on every item where it had previously abstained; measured abstention on those items fell from approximately 0.92 to 0.00 on otherwise identical content. The off-ceiling baseline was off ceiling, at least in part, because it had stopped discriminating key presence from key absence — emitting a value indiscriminately — which is a different behavior from the one the baseline was meant to measure. A baseline that no longer discriminates presence from absence is not a harder version of the intended construct; it is a different construct that happens to score lower.

### 3.3 Ruling out the scoring artifact: a form-level positive control

A measured abstention of exactly 0.00 under a large format change has an innocent alternative explanation: a parser failing to recognize an abstention rendered in the new format. If the model were abstaining in a form the parser did not count — a phrase such as "no matching alias" rather than the expected token — the collapse would be a scoring artifact, and refusing the baseline on it would be the wrong call. We ruled this out with a positive control at the level of output form, not merely token casing. Item-level inspection confirmed that all forty key-absent outputs were substantive single-character value emissions, with no abstention in any form — cased token, multi-token phrase, or symbolic. A form-shifted abstention cannot hide inside a single-character value, so the collapse is a real behavioral change, not a parser miss. (The per-item classification is in the supplement.)

### 3.4 What the gate did, and did not, adjudicate

We do not adjudicate the mechanism of the collapse — whether the format change degraded abstention directly, or raised difficulty which in turn degraded abstention. The gate does not depend on the mechanism: it refused the baseline on the observable validity failure, namely that the off-ceiling task no longer measured key-presence discrimination at all. The direction of the observation — a difficulty manipulation coinciding with degraded abstention — is consistent with the broader finding that abstention is fragile and unsolved (AbstentionBench 2025), but we note this only as context, not support: that work studies a training-time intervention and ours an inference-time manipulation, and we claim no mechanistic agreement.

The contribution this episode demonstrates is the protocol's action: a candidate baseline meeting every surface criterion was rejected by an automated validity gate on an item-level check, under a pre-declared decision rule, before it could enter a retention comparison — precisely the enforcement an advisory checklist cannot compel.

*Negative-use scope.* The per-item numbers in this section (the abstention rates, the forty-item control) are reported solely to substantiate the refusal. They license no claim about the model's capability, robustness, or behavior under stress, and no claim about the task family's viability; they are evidence about the instrument, not about the model.

### 3.5 The same discipline that confirmed this refusal also prevented a false one

The development history records a second episode of a different kind, which together with §3.2 establishes that the discipline fires in both directions — that the per-item read can both confirm a refusal and overturn an apparent failure that would otherwise have triggered a wrong one.

In a separate episode (the scorer-audit case), a case-sensitive NULL parser mis-scored lowercase abstentions as value emissions, making a baseline's discrimination look collapsed when it was not. Here the per-item read overturned an apparent failure before it could be acted on: thirteen of seventeen apparent "errors" were lowercase abstentions the parser had miscategorized, and the true emission rate, once corrected, was stable (approximately 0.10). The aggregate had reported a defect that the item-level read showed was an artifact of the scorer — and the read prevented a wrong pivot rather than reversing a refusal already issued.

The two episodes are the paper's bidirectional evidence (Figure 2).

![**Figure 2.** The same per-item discipline reverses one apparent failure and confirms another. Left: the CAL-E aggregate (0.575) is lifted by the per-item read to 0.90 — a scorer artifact, refusal averted. Right: the CAL-Q aggregate (0.00) is confirmed at floor — a real construct collapse, refusal upheld. The identical aggregate signature means opposite things; only the per-item read distinguishes them. Synthetic key-value family, Qwen2.5-3B (FP16).](figures/fig2_reversal_confirmation.png){width=92%}
 In §3.2 the per-item read confirmed a refusal that the aggregate would have passed; in §3.5 the per-item read overturned an apparent failure that the aggregate would have failed, before any refusal was acted on. A gate that only ever refused, or only ever confirmed, could be a gate calibrated to one direction; a gate that does both, on per-item evidence, is responding to the artifacts rather than to a fixed disposition. This bidirectional behavior is also the motivating material for the rejection audit specified in §5: the one time a refusal would have been wrong is exactly the case the discipline must catch, and §3.5 is an instance of the per-item read catching it.

---

## 4. The Instrument: A Fail-Closed Validity Gate

The general architecture is described here, after the worked case, so that it is read as a generalization of a demonstrated event rather than as an asserted design. The section's load-bearing feature is the line drawn between what is implemented and exercised and what is specified but unbuilt; the paper's integrity depends on that line, and we draw it explicitly in §4.3.

### 4.1 What the instrument is

The instrument is not, in its primary function, a benchmark runner that returns a score. It is a validity gate whose output is a route decision about whether a result can be trusted for a stated purpose. The question it answers is not "what did the model score?" but "can this result be trusted enough to compare, to stress, or to support a claim?" — and a first-class, legitimate answer is *no: not safe to compare*. A measurement pipeline that can return that answer, with the per-item evidence that justifies it, is the artifact this paper describes.

The output classes are route decisions rather than scalar scores: **PASS** (the baseline is certified; safe to compare or proceed); **NEEDS-REPAIR** (the construct may be fixable, with a specified defect to address); **QUARANTINE** (the data may be informative but cannot support a claim); and **PIVOT / FAIL-CLOSED** (the route is invalid for the intended measurement, and no claim is licensed). The load-bearing class is the refusal — *not safe to compare*, emitted upstream of any retention comparison.

### 4.2 Architecture overview

The instrument takes an evaluation setup (baseline outputs, stressed outputs if available, the scorer, the task specification, and the artifact or provenance trail) and applies an ordered set of checks, each of which can route the result away from PASS. The checks are: baseline correctness and constructibility; shortcut-floor and off-ceiling band; scorer validity; defective-case discrimination; format-artifact detection; same-error identity; provenance and route control; and a rejection audit of the instrument's own refusals. The design is fail-closed: a result reaches PASS only if every applicable check is satisfied, and the absence of any one routes to refusal, repair, or quarantine rather than to a reported number.

### 4.3 Implemented and exercised, versus specified but unbuilt

The paper's integrity depends on this distinction, so we state it as a table of status rather than as prose that could blur it.

**Implemented and exercised on the synthetic family (Qwen2.5-3B, FP16):**

- **Baseline certification gate** — correctness, off-ceiling band, and the construct-validity check demonstrated in §3 (the abstention-collapse refusal; the sweep and the empty certifiable region are shown in Figure 1).
- **Strict-versus-concept scorer audit** — the per-item read that distinguishes a true content failure from a scoring/parser artifact, demonstrated in §3.5 (the lowercase-abstention correction).
- **Four-way reporting of absence-defined behavior** — strict / concept-level / true false-emission / format-artifact, the reporting schema hardened after the §3.5 parser episode so that artifact could not recur unnoticed.
- **Construct-validity gate (CAL-Q)** — the check that refuses a baseline whose surface score is real but whose construct has collapsed, demonstrated in §3.
- **Provenance and route control** — artifact-locked, with official results admitted only via protocol compliance and non-conforming runs quarantined rather than allowed to shape claims.

**Specified but unbuilt (no implementation or exercised run):**

- **Same-error identity.** A retention measurement should ask not only "did the answer survive?" but "was it correct before, correct after, and if wrong, the same wrong answer?" — distinguishing preserved capability from preserved error. This follows directly from Paper 1's argument that survival is not correctness. It is a designed scoring layer, computed on no run in the present work. We mark it specified, not demonstrated, because it is exactly the kind of compelling idea whose status is easy to blur.
- **Rejection audit as a standing component.** The design is given in §5, and two worked episodes (§3.2, §3.5) motivate it, but it is not yet built as a standing module and no rejection-audit artifact exists.
- **Cross-family / cross-model generality.** The gate has been exercised on one synthetic family and one model. Demonstrating that its checks continue to fire on real defects — and do not over-reject valid constructs — across a second family, an external benchmark slice, or a different model is specified and not done.
- **Full stress-retention pipeline.** The end-to-end path the instrument is ultimately for — certified baseline → compression stress → retention interpretation — has not been run. The program is pre-stress: no certified baseline has been carried through an executed compression rung.
- **Software abstraction.** The instrument exists as a protocol, a set of scorers and run records, governance gates, and manual per-item reads. A reusable product form — a CLI or library, fixed I/O schemas, automated claim-safe reports, an audit packet — is specified but early.

### 4.4 What this section claims

This section claims an architecture — a fail-closed validity gate whose output is a route decision — of which a coherent subset is implemented and demonstrated on one task family, and the remainder specified. It does not claim a finished tool, a validated general method, or a stress-retention result. The honest summary is structural rather than quantitative: the baseline gate, scorer-validity audit, four-way reporting, construct-validity gate, and provenance control are implemented and were exercised; same-error identity, the rejection audit as a standing component, cross-family generality, the full stress pipeline, and the software abstraction are specified but unbuilt; and no compression rung has run. What the instrument can already do — refuse a baseline that surface metrics passed, on a per-item construct-validity failure — it has done. What it cannot yet do, it does not claim.

---

## 5. The Rejection Audit: Auditing the Instrument's Own Refusals

A fail-closed instrument's characteristic failure is the symmetric one to the failure it is built to prevent. A validity gate exists to stop invalid baselines from passing (over-acceptance); its own risk is to stop valid baselines from passing (over-rejection). A gate that refuses everything is as useless as one that refuses nothing, and a fail-closed design is structurally biased toward the former. The rejection audit is the control that holds the gate accountable for its refusals; we present its design here, and note that as a standing component it is specified but unbuilt (§4.3), demonstrated to date only by the two worked episodes it generalizes.

### 5.1 What the audit checks

For each refusal the gate emits, the audit asks four questions, each pre-declared rather than applied post hoc:

1. **Was the refusal correct?** Does an independent per-item read confirm the defect the gate fired on, or was the gate responding to an aggregate artifact?
2. **Could the refusal be a scoring artifact?** Specifically, could the signal the gate refused on be produced by the scorer rather than by the model — the §3.3 question, asked of every refusal, not only the abstention case.
3. **Do per-item reads confirm it?** The refusal must be grounded in inspectable items, not in a summary statistic; the audit requires the items.
4. **Was the rule pre-declared?** A refusal under a rule fixed before the data was observed is evidence; a refusal under a rule chosen after seeing the data is post-hoc tuning and is recorded as such.

A refusal that passes all four is a sound refusal — the gate correctly declined a baseline with a demonstrable defect. A refusal that fails question 1 or 2 is an over-rejection — the gate declined a baseline that was in fact valid, and the audit must surface it so the rule can be corrected.

### 5.2 Why the worked episodes motivate it

The two episodes of §3 are, in effect, decisions whose soundness had to be checked, and they are the audit's motivating cases — one of each kind.

The CAL-Q episode (§3.2) is a confirmed refusal: the per-item read and the form-level positive control together established that the baseline's construct had genuinely collapsed, so the refusal was sound. The scorer-audit episode (§3.5) is an overturned apparent failure: the per-item read showed that an aggregate-level defect was a parser artifact, so a baseline that the aggregate would have failed was in fact valid, and the read prevented a wrong pivot. The second case is precisely the over-rejection the audit exists to catch — the one time an aggregate-driven refusal would have been wrong — and it demonstrates that the per-item discipline can catch it. What does not yet exist is the standing component that performs this audit on every refusal as a matter of course; building it is, in our judgement, the highest-value model-free module remaining, and an external review named it as required content before the non-vacuousness claim of §3 is fully supported. We concur.

---

## 6. Discussion and Limitations

### 6.1 Scope, stated in the body

The evidence in this paper is deliberately narrow, and we state its limits in the body rather than in a footnote. Our demonstrations are drawn from a single synthetic key-value task family, on a single open-weights model (Qwen2.5-3B, FP16), and the program is pre-stress: at the time of writing no certified baseline has been carried through to an executed compression rung. We therefore do **not** claim to have measured compression fragility, to have found or refuted any specific compositional seam, or to have established that the protocol generalizes across task families or models. We claim a protocol and a demonstration that it enforces: a fail-closed metrological gate for stress-retention evaluation, shown on a controlled case to refuse a baseline that failed a construct-validity check the surface metrics passed.

### 6.2 The gate has only been tested on baselines we built

One limitation bounds the non-vacuousness argument specifically, and we state it directly rather than folding it into general future work. Every demonstration in this paper is the gate catching defects in baselines the present authors constructed. Catching one's own constructed defects is suggestive but not independent evidence: a gate tuned by the same people who built the test cases it catches is at risk of being calibrated to its own constructions. This bounds non-vacuousness, not only generality. The remedy is an external demonstration — the gate exercised on an evaluation the present authors did not construct — and until that is done, the strongest honest statement is that the gate fires on real defects in baselines we built, which is weaker than "the gate fires on real defects" simpliciter.

### 6.3 Required extensions, and the path to Paper B

Two extensions are required before the contribution can be presented as more than a protocol with a worked example, and we name them rather than defer them silently. First, the external demonstration of §6.2, which is model-free to design but will require a run to execute. Second, an executed stress rung: carrying a certified baseline through an actual compression step and interpreting retention against it, which is the end-to-end path the instrument is ultimately for. Both are the substance of the planned follow-on (Paper B), which requires separate authorization and is not begun. A third extension, the standing rejection-audit component (§5), is model-free and is the highest-value remaining build.

### 6.4 The contribution at its altitude

The honest frame for this work is an instrument paper: a credible measurement and experience contribution scoped to what is demonstrated, not a finished method and not a product. The durable claim is not about quantization. It is that validity discipline can move from advice to enforcement, with refusal as a first-class output — and the evidence is a gate that refused its own authors' candidate baseline on a per-item construct-validity check. We close with one consequence for the certification setting from which §2.3 distinguished this work. Certifying a model against a baseline assumes the baseline measures the intended construct; if it does not, the certificate is empty. Construct-validity enforcement is therefore logically prior to certifying the measurement process: before certifying how well a model is measured, verify that the test object measures what it is named to measure at all.

---

## 7. Non-claims and Status

This paper makes no model-behavior claim: it establishes no capability, no incapability, no breadth behavior, no certification readiness, no retention property, no compositional-seam evidence. Its subjects are the artifact and protocol layer and this program's process. The worked episodes may not be cited as findings about the model, the task family's viability, or compression behavior; they are evidence that the gate enforces. The implemented/specified split of §4.3 is binding: the same-error identity layer, the standing rejection-audit component, cross-family generality, the full stress pipeline, and the software abstraction are specified but unbuilt, and the contribution is the architecture plus a demonstrated subset, not a validated general method or a product.

The program's standing commitments hold: a failed validation is an instrument result, not a project failure; and the contribution retains a negative-result form — if the external demonstration and the stress rung are not completed, the work remains a protocol with a worked example, scoped accordingly, and is not promoted past that.

---

## Supplement (to assemble)

The following materials are referenced in the body and belong in supplementary material; they are listed here as an assembly manifest, not reproduced.

- **CAL-Q per-item data** (the abstention-collapse case, §3.2): per-item baseline and post-manipulation outputs on the key-absent items, with the measured abstention rates.
- **The pre-declared decision rule** that classified the abstention collapse as a construct-validity failure (§3.2, §3.4).
- **The form-level positive control** (§3.3): item-level classification of the forty key-absent outputs confirming single-character value emissions with no abstention in any form.
- **The four-way reporting schema** (strict / concept-level / true false-emission / format-artifact) and the scorer-audit per-item data behind the §3.5 lowercase-abstention correction.
- **Figure 1 — the certifiable-region scatter** (`figures/fig1_certification_box.png` / `.svg`): clean accuracy versus defective discrimination for the five calibration candidates, with the certifiable region (off-ceiling band, discrimination preserved) shaded; generated from the rescore summary and the CAL-Q run record. Shows the certifiable region is empty.
- **Figure 2 — reversal versus confirmation** (`figures/fig2_reversal_confirmation.png` / `.svg`): the per-item read reversing the CAL-E aggregate (a scorer artifact, refusal averted) and confirming the CAL-Q aggregate (a real construct collapse, refusal upheld), against a preserved-discrimination reference band; generated from the same records.
- **Citation-status record:** per-citation verifiable facts for the §2.1 and §2.3 references, for independent confirmation before submission. Independent re-confirmation against source before submission is retained as standing practice.

---

