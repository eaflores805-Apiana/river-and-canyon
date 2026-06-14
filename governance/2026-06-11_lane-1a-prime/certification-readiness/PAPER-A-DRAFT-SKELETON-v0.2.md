# PAPER-A-DRAFT — "Before Retention: Baseline Certification and Claim-Safe Refusal in LLM Stress Evaluation"

**Working title (alt):** A Fail-Closed Metrological Protocol for LLM Stress-Retention Evaluation **Version:** SKELETON v0.2. **Supersedes v0.1.** River and Canyon program. The "instrument paper" (Paper A) per Manager decision (MANAGER-DECISION-PAPER-A-NOW-v0.1, 1d901d5d): write A now, loop next. **Status:** model-free assembly. This stitches the review-hardened sections into one Paper-A draft so the whole shape is visible. v0.2: (1) all paragraphs UNWRAPPED (v0.1 was hard-wrapped at ~78 chars, which broke sentences across lines in many viewers); (2) abstract REVISED to match Paper 1's house style (read from /mnt/project/survivalisnotcorrectness.pdf) — opens on the program's own framing, tightened to Paper 1's declarative cadence, and the disclaimers moved into a titled "What we do not claim" section directly after the abstract, exactly as Paper 1 does. Component provenance below; each section retains its own versioned source file as the editable master. Anchored on origin/main HEAD 0f7e9a7. Authorizes nothing; model-free; pre-stress.
**Component provenance:**
- Abstract — NEW (written here for the first time; confirmed for Paper A by the Manager decision; not yet reviewed).
- §2 Background and Related Work — from PAPER-POSITIONING-SECTION-DRAFT-v0.7 (34cedb30; hardened through 7 review rounds; citations verified).
- §3 The Instrument — from PAPER-INSTRUMENT-ARCHITECTURE-SECTION-DRAFT-v0.2 (6b111f3a; forcing-function framing + implemented/specified split).
- §1 Introduction, §4 Methods (D1–D7), §5 Rejection audit, §6 Discussion, Supplement — STUBS (model-free build remaining).
**Scope (binding, from §2.5/§3.5):** one synthetic task family, one model (Qwen2.5-3B FP16), pre-stress. No compression rung run. Claims a protocol + a worked demonstration, NOT a general method / compression result / seam.

---

## Abstract

Quantizing a model and measuring which behaviours "survive" is a common way to ask whether compression damages capability. We argue that this measurement is unsafe unless the baseline it is compared against is first shown to measure the intended capability at all. A retention score is a comparison against a baseline; if that baseline rests on a shortcut, saturates at ceiling, or is mis-scored, the retention number inherits the defect and reports it as preserved capability. The field has extensively *diagnosed* evaluation-validity failures — shortcut learning, construct-validity gaps, abstention fragility, scorer artifacts, and quantization-induced degradation — and a recent certification literature *enforces* the statistical reliability of judges and outputs, emitting refusal as a first-class result. Our contribution is narrower and complementary: a staged, fail-closed protocol that enforces *construct validity at the baseline* — whether the baseline measured the intended capability at all — as a precondition on a retention claim, and whose output is a route decision, including "not safe to compare," rather than a score. We specify the protocol as an ordered set of validity gates and report which are implemented and exercised on a synthetic multi-hop task family — a baseline-certification gate, a strict-versus-concept scorer audit, four-way reporting of absence-defined behaviour, a construct-validity gate, and provenance control — and which remain specified: same-error identity, a rejection audit, cross-family generality, and the full stress pipeline. The protocol's non-vacuousness is shown by a worked case in which the gate refused the authors' own candidate baseline. A difficulty manipulation lowered clean accuracy — the sought-after result — but per-item inspection showed it had collapsed the model's abstention on absence-defined items, so the baseline no longer measured the intended construct, and the protocol refused it on the observable validity failure. The claim is methodological and bounded: before a retention comparison can be interpreted, the baseline must be certified to measure the intended construct, and in this program the staged instrument refused a baseline that surface metrics passed.

## What we do not claim

We do not claim that a compositional seam exists or does not exist. We do not claim to have measured compression fragility: the program is pre-stress, and no certified baseline has been carried through an executed compression rung. We do not claim a validated general method — the demonstrations are drawn from one synthetic task family on one open-weights model (Qwen2.5-3B, FP16). We do not claim to have discovered shortcut learning, construct-validity failure, or abstention instability; each is field-owned, and our contribution is the fail-closed enforcement architecture, not the underlying concepts. We do not claim a product or a market-validated tool. What the instrument has done, it has done once, on its own constructed baseline; establishing cross-family generality and carrying a certified baseline through a stress rung are stated as required future work, and are the substance of the planned follow-on (Paper B).

---

## 1. Introduction  *(STUB — model-free, to draft)*

```text
TO WRITE: the baseline-inheritance problem as motivation (a retention score inherits
its baseline's defects), the pre-stress honest framing, and the contribution in one
paragraph (a fail-closed validity gate that refuses uncertified baselines, with a
worked refusal of the authors' own baseline). Pull the motivating mechanism from the
abstract; do not over-claim beyond §2.5/§3.5 scope.
```

## 2. Background and Related Work

### 2.1 The field has diagnosed evaluation-validity failure

A substantial body of work establishes that benchmark scores can fail to measure the capability they are taken to represent. Geirhos et al. [2020] characterise *shortcut learning* — decision rules that perform well on a benchmark but rely on spurious cues and fail to transfer — as a unifying account of many deep-learning failures (arXiv:2004.07780). For language models specifically, a recent systematic review of 445 benchmarks by Bean et al. [2025] documents widespread weaknesses in how phenomena are operationalised, how tasks are constructed, and how metrics are chosen, and argues these weaknesses undermine the validity of the resulting claims (arXiv:2511.04703). Freiesleben and Zezulka [2025] develop construct-validity conditions for predictive benchmarking from psychometric measurement theory (arXiv:2510.23191), continuing a line that includes Evidence-Centered Benchmark Design [2024] (arXiv:2406.08723) and earlier critiques of benchmark validity [Raji et al. 2021]. Reproducibility-focused infrastructure such as the LM Evaluation Harness [Biderman et al. 2024] addresses a complementary problem — consistency of measurement across runs and models — while explicitly bracketing validity (arXiv:2405.14782).

Two adjacent literatures bear directly on the present setting. First, abstention: AbstentionBench [2025] shows that frontier models systematically fail to abstain on unanswerable questions, that the failure is not resolved by scale, and — notably — that reasoning fine-tuning *degrades* abstention by roughly 24% on average (arXiv:2506.09038; NeurIPS 2025); a recent survey catalogues the broader abstention literature [TACL 2025]. Second, compression: low-bit quantisation is known to degrade reasoning specifically, with reported losses up to ~32% on mathematical reasoning under aggressive INT4 schemes and a pronounced sensitivity for smaller models [Quantization Meets Reasoning 2025, arXiv:2501.03035; ZeroQuant-V2 2023].

We take all of the above as established. This paper does not claim to discover that evaluations can be invalid, that models exploit shortcuts, that abstention is unstable, or that compression degrades reasoning. Each is field-owned, and several are the subject of recent, prominent, large-scale studies.

### 2.2 The gap: diagnosis is not enforcement

The work above is, with few exceptions, *diagnostic* or *advisory*. It identifies validity failures, surveys their prevalence, and — at its most operational, in Bean et al. [2025] — provides a **checklist** that benchmark authors are encouraged to consult during design and to report as an appendix. A checklist of this kind is a valuable instrument for improving practice. It is also, by construction, *non-binding*: it advises an author, who remains free to proceed past an unmet item. Its unit of action is the conscientious researcher. An advisory checklist improves the probability that such an author will notice a problem; it does not prevent a pipeline from emitting a retention number whose baseline was never certified to measure the intended construct.

The present work addresses a different unit of action. In the specific setting of **stress-retention evaluation** — measuring whether a capability survives a controlled degradation such as quantisation — the central risk is not only that an author overlooks a validity concern, but that a *pipeline* emits a retention number whose baseline was never certified to measure the capability in the first place. A retention score is a comparison against a baseline; if the baseline measured a shortcut, or saturated at ceiling, or was scored by a parser that mis-categorised the model's output, the retention number inherits that defect and reports it as preserved capability [cf. the program's Paper 1, *survival is not correctness*]. An advisory checklist does not prevent this; it relies on the author to have caught it.

We therefore propose to move validity discipline from *advice* to *enforcement*: a **fail-closed protocol** in which a stress-retention claim is not emitted unless a verified clean baseline, a validated scorer, an artifact-locked provenance trail, and a certified construct are all present, and in which the absence of any one yields a logged *refusal* rather than a number.

### 2.3 Relation to fail-closed certification of evaluation

Enforcement and refusal are not, by themselves, new. A recent line of work already treats evaluation as something to be *certified* rather than merely reported, and already emits abstention or rejection as a first-class output with formal guarantees. We engage it directly, because it is the closest prior art to the present proposal and the distinction from it is what defines our contribution.

Noisy but Valid [2026, arXiv:2601.20913] certifies whether an LLM's failure rate lies below a safety threshold under an imperfect judge, deriving a variance-corrected critical value that guarantees finite-sample Type-I error control: a genuine accept/reject gate on an evaluation. Selective Risk Certification [2025, arXiv:2509.12527] issues information-lift certificates with formal abstention guarantees, emitting *refusal* as a first-class output under bounded risk. Safety Under Scaffolding [2026, arXiv:2603.10044] runs a pre-registered specification-curve analysis across scoring degrees of freedom and finds, among other things, that changing answer format on identical items shifts measured scores by 5–20 points — larger than the effect under study — the same scorer- and format-sensitivity our own reporting is designed to surface.

Against this work, "we enforce, the field advises" is too strong a claim, and we do not make it. These methods enforce, and they emit refusal. They differ from the present work in the *object* they certify. They take the construct as given and certify properties of the *measurement process*: a judge's error rate, or whether a given output is reliable enough to answer rather than abstain. The present work certifies a property of the *baseline itself* — whether it measured the intended capability at all (shortcut-free, off-ceiling, correctly parsed) — before any retention comparison is permitted. Three things follow from this shift of object. The trigger is not a bounded error rate but an uncertified construct. The gated object is not a single measurement but a relative survival claim across a controlled degradation. And the integration point is a per-item, provenance-locked read rather than a distributional guarantee. We share the enforcement posture and the refusal-as-output with this literature, and claim only this cell: construct-validity enforcement on the baseline of a stress-retention comparison, with per-item and provenance integration. This is also the distinction from the advisory checklist of §2.2 — a checklist an author may pass and a gate that does not let the claim through — but the sharper line is the one drawn here, against the certification work that already enforces.

The distinction is concrete at the level of the worked example in §2.4. Selective Risk Certification could examine a single CAL-Q output and refuse to answer it as low-confidence; it operates on individual outputs of a measurement whose construct is assumed. Our gate operates one level up: it refuses the entire CAL-Q *baseline* — upstream of any retention comparison — on the finding that the baseline no longer measures the intended construct at all. The two are complementary rather than competing: per-output reliability certification and baseline construct-validity enforcement gate different objects at different points in the pipeline. We also note, to forestall a natural objection, that none of these three certification methods addresses stress-retention or compression evaluation; each certifies a property of a measurement taken in isolation, whereas the construct-validity gate is a precondition specifically on a *relative* survival claim across a controlled degradation. The retention setting is therefore not incidental to the contribution but part of the cell being claimed.

### 2.4 Demonstrating that the gate is non-vacuous

A blocking gate is only meaningful if it blocks things that would otherwise pass — if it is not merely a gate that never closes on anything real, nor one calibrated so loosely that it never fires. We substantiate the gate's non-vacuousness with the program's own development history, in which the protocol repeatedly refused artifacts that an advisory process would have waved through, including artifacts the authors were motivated to accept.

The clearest worked case for the protocol's enforcement role is the D4/CAL-Q episode. In constructing a calibration baseline for a synthetic key-value lookup family, every content-based attempt to move the clean baseline off its accuracy ceiling failed (the model remained saturated, leaving no headroom to measure a degradation). A query-side manipulation — an in-prompt code-book that required the model to resolve an alias before performing the lookup — finally produced the first off-ceiling clean point in the D4 rescue sequence. By the surface objective (off-ceiling difficulty), this was the sought-after result. The protocol refused it. The refusal followed from a per-item inspection. That inspection showed the query-form change had coincided with a collapse of the model's abstention on absence-defined (key-absent) items: the model emitted a value on every such item where it had previously abstained, with measured abstention falling from ~0.92 to 0.00 on otherwise identical content. Because a perfect 0.00 under a large format change is also the signature of a scoring artifact — a parser failing to recognise an abstention in the new format — we verified the collapse with a positive control. The control was conducted at the level of output *form*, not merely token casing, because the program's own thesis is that a format change can change the form an abstention takes (a phrase such as "no matching alias" rather than a case variant of the abstention token). Item-level inspection of the forty key-absent outputs confirmed that every output was a substantive single-character value emission: none was an abstention in any form — not a cased token variant, not a multi-token phrase, not a symbolic or empty response. A form-shifted abstention cannot be concealed within a single-character value, so the collapse is a real change in the model's behaviour, not a scoring artifact.[^1] We do not adjudicate its mechanism — whether the format change degraded abstention directly, or raised difficulty which in turn degraded it — because the gate does not depend on the mechanism: it refused the baseline on the *observable* validity failure, namely that the off-ceiling task no longer measured key-presence discrimination at all. The pre-declared decision rule classified this as a construct-validity failure of the difficulty lever and blocked the baseline. The direction of the observation — stress coinciding with degraded abstention — is consistent with the broader finding that abstention is fragile and unsolved [AbstentionBench 2025]. We note this only as context, not support: that work studies a training-time intervention and ours an inference-time manipulation, and we claim no mechanistic agreement. The contribution we do claim is the protocol's action: a candidate baseline meeting every surface criterion was rejected by an automated validity gate on an item-level check — precisely the enforcement an advisory checklist cannot compel.

Beyond this worked case, the development history records further instances of the same enforcement: a scorer/parser artifact caught by per-item reading before it could distort a discrimination measurement, and a saturation-versus-elimination diagnosis that separated fixable constructs from validly-rejected ones. We report these not as findings about models but as evidence that the gate fires on real defects rather than blocking arbitrarily or never closing.

### 2.5 Scope and what we do not claim

The evidence in this paper is deliberately narrow, and we state its limits plainly rather than in a footnote. Our demonstrations are drawn from a single synthetic key-value task family, on a single open-weights model (Qwen2.5-3B, FP16), and the program is *pre-stress*: at the time of writing no certified baseline has been carried through to an executed compression rung. We therefore do **not** claim to have measured compression fragility, to have found or refuted any specific "compositional seam," or to have established that the protocol generalises across task families or models. We claim a *protocol* and a *demonstration that it enforces*: a fail-closed metrological gate for stress-retention evaluation, shown on a controlled case to refuse a baseline that failed a construct-validity check the surface metrics passed. A broader claim would require demonstrating that the protocol continues to fire on real defects across multiple task families, and that a certified baseline can be carried through an actual compression rung; those extensions are stated as required future work. Until they are done, the contribution is a protocol with a worked example, not a validated general method and not a product.

Two further extensions are required before the non-vacuousness claim of §2.4 is fully supported, and we name them rather than defer them silently. First, an *external* demonstration: the gate exercised on an evaluation the present authors did not construct, since catching one's own constructed defects is suggestive but not independent evidence. Second, a *rejection audit*: evidence that the gate does not over-reject valid constructs — the symmetric failure to over-acceptance, and the one a fail-closed instrument is most at risk of. A gate that refuses everything is as useless as one that refuses nothing; the audit must show the gate admits constructs later confirmed valid and refuses only those with a demonstrable defect. Both are required content for the eventual paper, not optional follow-on work, and both are model-free to design though the external demonstration will require a run to execute.

[^1]: Full per-item data, the pre-declared decision rule, the four-way abstention
reporting (strict / concept-level / true false-emission / format artifact), and the CAL-Q-format scorer positive control used to rule out a parsing artifact are in the supplementary material. The four-way reporting is itself a consequence of an earlier enforcement episode, in which a case-sensitive NULL parser mis-scored lowercase abstentions as emissions; per-item reading corrected the aggregate, and the reporting schema was hardened so the artifact could not recur unnoticed. (Citation note for finalisation: three references in §2.1 — Quantization Meets Reasoning, arXiv:2501.03035, and its ~32% figure; the abstention survey (Wen et al., "Know Your Limits," TACL vol. 13 2025, DOI 10.1162/tacl_a_00754); and ZeroQuant-V2, arXiv:2303.08302 — have now been verified against source; the certification references in §2.3, arXiv:2601.20913, 2509.12527, and 2603.10044, have been verified; per-citation verifiable facts are recorded below for independent confirmation. The three §2.1 references have now also been verified: Quantization Meets Reasoning (arXiv:2501.03035; the "~32%" is the paper's 32.39% AWQ/GPTQ figure on Llama-3); the abstention survey is Wen et al., "Know Your Limits," TACL vol. 13 (2025), pp. 529–556, DOI 10.1162/tacl_a_00754 (arXiv:2407.18418); and ZeroQuant-V2 is arXiv:2303.08302 (INT4 small-model degradation lessening with model size). Independent re-confirmation before submission remains recommended as standing practice.) [Drafting note: in the final paper this footnote should split into 2–3 — supplementary-material pointer, the four-way-reporting provenance, and the citation-status note — for readability.]

---

## 3. The Instrument: A Fail-Closed Validity Gate

### 3.1 What the instrument is

The instrument proposed in this work is not, in its primary function, a benchmark runner that returns a score. It is a *validity gate* for evaluation results, whose output is a route decision about whether a result can be trusted for a stated purpose. The question it is built to answer is not "what did the model score?" but "can this result be trusted enough to compare, to stress, or to support a claim?" — and a first-class, legitimate answer is *no: not safe to compare*. A measurement pipeline that can return that answer, with the per-item evidence that justifies it, is the artifact this paper describes.

The instrument's output classes are therefore route decisions rather than scalar scores. We distinguish: PASS (the baseline is certified; safe to compare or proceed); NEEDS-REPAIR (the construct may be fixable, with a specified defect to address); QUARANTINE (the data may be informative but cannot support a claim); and PIVOT / FAIL-CLOSED (the route is invalid for the intended measurement, and no claim is licensed). The load-bearing class is the refusal: *not safe to compare*, emitted upstream of any retention comparison. This is the operational form of the contribution positioned in §2 — construct-validity enforcement at the baseline, gating a retention claim.

### 3.2 Architecture overview

At the level of design, the instrument takes an evaluation setup (baseline outputs, stressed outputs if available, the scorer, the task specification, and the artifact or provenance trail) and applies an ordered set of checks, each of which can route the result away from PASS. The checks are: baseline correctness and constructibility; shortcut-floor and off-ceiling band; scorer validity; defective-case discrimination; format-artifact detection; same-error identity; provenance and route control; and a rejection audit of the instrument's own refusals. The design is fail-closed: a result reaches PASS only if every applicable check is satisfied, and the absence of any one routes to refusal, repair, or quarantine rather than to a reported number.

The remainder of this section describes each module **and states its evidence status**. We distinguish modules that are *implemented and demonstrated* — for which a computed artifact exists showing the module ran on the D4 task family — from modules that are *specified but not yet built* — part of the designed architecture, but without an implementation or a run. This distinction is not incidental bookkeeping; it is the boundary between what this paper demonstrates and what it proposes, and we hold it explicitly because the instrument's entire purpose is to prevent unsupported claims, including our own.

A note on the *kind* of evidence this section offers, because it determines what the demonstrations can and cannot support. The modules below were not designed in the abstract and then validated; they were *forced into existence by documented failures and near-failures* in the program's own development. The argument for each is therefore a forcing function — "without this check, a specific wrong decision would have been (or nearly was) made" — rather than a claim of broad positive validation. This yields two honest categories of support: a module can be shown *necessary* (its absence demonstrably produced a wrong route on a real case) and, in some cases, shown to *fire correctly* (it caught the defect on the case at hand). Neither is a claim of *generality*: a forcing function on one or two cases establishes that a check is needed and that it worked there, not that it generalises across task families or models. Where this section says a module is demonstrated, it means demonstrated-as-necessary-via-a-documented-counterexample, at the case count stated — not proven in general. The distinction is the program's own standard applied to its own instrument, and it is what keeps the strong claims ("the gate refused a baseline that surface metrics passed") separate from the claims not yet earned ("the gate generalises").

### 3.3 Implemented and demonstrated modules

The following modules exist as computed artifacts and were exercised on the D4 synthetic key-value family on Qwen2.5-3B (FP16).

**Baseline gate (IMPLEMENTED-AND-DEMONSTRATED).** The instrument does not trust a baseline merely because the model answers correctly. It checks whether clean accuracy is off the saturation ceiling (so there is headroom to measure a degradation), above the shortcut floor (so the score is not attributable to a position or layout cue), and whether the defective case remains defective. The D4 calibration sweep exercised this gate directly: candidate baselines were routed by exactly these criteria, and the recurring failure was clean saturation at ceiling, which the gate is built to catch.

**Scorer-validity / strict-versus-concept audit (IMPLEMENTED-AND-DEMONSTRATED).**
A scorer that mis-categorises an output corrupts every downstream number. The instrument computes a strict score and a concept-level score and compares them; a divergence flags a scoring artifact. This module was not designed in the abstract — it was forced by a real failure (the CAL-E episode), in which a case-sensitive parser scored a lowercase abstention as a wrong answer; the concept-level read showed the model was in fact abstaining. The re-scored result is on disk (`cal-abce_rescore_summary.json`), and the strict/concept divergence is the computed evidence that the module fires.

**Four-way defective reporting (IMPLEMENTED-AND-DEMONSTRATED).** For absence-defined (key-absent) items, a single accuracy number conflates distinct behaviours. The instrument reports four separate quantities: strict accuracy, concept-level abstention, true false-emission rate, and a format-abstention artifact fraction. All four are computed in the D4 run records (the `cal-q_run.json` defective summary carries `strict_accuracy`, `concept_abstention_accuracy`, `true_false_emission_rate`, and `format_abstention_artifact`). This is a concrete reporting schema, not a described intention, and it is itself a consequence of the CAL-E enforcement episode.

**Construct-validity gate (IMPLEMENTED-AND-DEMONSTRATED, on one case).** The instrument checks whether a manipulation intended to change task difficulty preserved the behaviour being measured. The CAL-Q episode is the demonstration: a query-side code-book lowered clean accuracy — which by the surface objective looked like success — while collapsing the model's abstention on key-absent items from ~0.92 to 0.00. The gate classified this as a construct-validity failure (the manipulation displaced rather than stressed the measured behaviour) and refused the baseline. The per-item data and the positive control ruling out a scoring artifact are on disk. We state the evidence scope precisely: this module is *demonstrated on a single case*, the one for which the protocol is named; it is not yet shown across families or models.

A clarification on the certification protocol as a whole (the D1–D7 gate specified in the methods section). The gates were forced into existence collectively by the program's failures, but they do not all carry the same weight of direct evidence, and we do not present them as uniformly demonstrated. Some have a specific counterexample behind them — the strict-scoring-stability gate is forced by the CAL-E parser artifact, and the retention-sensitivity gate is forced by D4's saturation leaving no headroom to measure a degradation. Others are, at present, better described as *logically required but not yet individually stress-tested across many cases* — they follow from the same reasoning but lack a dedicated counterexample in the current record. The methods section states this gate-by-gate rather than claiming the whole protocol is empirically validated; here we flag only that "the D1–D7 gate exists" is a design-and-necessity claim, not a claim that every gate has been independently demonstrated.

**Provenance / route control (IMPLEMENTED-AND-DEMONSTRATED).** The instrument treats authorization, route state, and artifact sealing (hashes, paths, model-free-versus- execution status) as part of claim safety, not bureaucracy. A retention claim is licensed only if its evidence is on an authorized route with a sealed artifact trail. This module is realised in the program's governance records and commit/hash discipline, which gate whether a given result may be used for a claim at all.

### 3.4 Specified but not-yet-built modules

The following are part of the designed architecture but have **no implementation or run**. We list them as specified — not demonstrated — because the paper's integrity depends on the distinction.

**Same-error identity (SPECIFIED-BUT-UNBUILT).** A retention measurement should not ask only "did the answer survive?" but "was it correct before, correct after, and if wrong, was it the *same* wrong answer?" — distinguishing preserved capability from preserved error. This is a designed scoring layer and, in the program's judgement, an important one; it follows directly from Paper 1's argument that survival is not correctness. But it is computed on no run in the present work: it is a *proposed* layer the protocol specifies, not a demonstrated one. We are explicit about this because same-error identity is exactly the kind of compelling idea whose status (designed vs demonstrated) is easy to blur, and the instrument's purpose forbids that blur.

**Rejection audit (SPECIFIED-BUT-UNBUILT).** A fail-closed instrument can fail by being too strict — refusing valid constructs as readily as invalid ones. The designed remedy is a rejection audit: for each refusal, check whether it was correct, whether it could be a scoring artifact, whether per-item reads confirm it, and whether the rule was pre-declared rather than post-hoc. The CAL-E and CAL-Q episodes together motivate this module (each is, in effect, a refusal whose soundness had to be checked), but it is not yet built as a standing component, and no rejection-audit artifact exists. It is named by an external review as required content before the instrument's non-vacuousness claim is fully supported; we concur, and it is the highest-value model-free module remaining to design.

**Cross-family / cross-model generality (SPECIFIED-BUT-UNBUILT).** The instrument has been exercised on one synthetic task family and one model. Demonstrating that its gates continue to fire on real defects — and do not over-reject valid constructs — across a second task family, an external benchmark slice, or a different model is specified as necessary, and not yet done.

**Full stress-retention pipeline (SPECIFIED-BUT-UNBUILT).** The end-to-end path the instrument is ultimately for — certified baseline → compression stress → retention interpretation — has not been run. The program is pre-stress: no certified baseline has been carried through an executed compression rung. This is why the work cannot yet be presented as a compression-retention result or product; the instrument is the precondition machinery, demonstrated up to but not through the stress step.

**Software abstraction (SPECIFIED-BUT-UNBUILT).** The instrument currently exists as a protocol, a set of scorers and run records, governance gates, and manual per-item reads. A reusable product form — a CLI or library, fixed input/output schemas, automated claim-safe reports, an audit packet — is specified but early; most of the repeatable machinery is not yet abstracted into a tool another team could run.

### 3.5 What this section claims

This section claims an *architecture* — a fail-closed validity gate whose output is a route decision — of which a coherent subset is implemented and demonstrated on one task family, and the remainder specified. It does not claim a finished tool, a validated general method, or a stress-retention result. The honest summary is structural rather than quantitative: the architecture is specified; the baseline gate, scorer-validity audit, four-way reporting, construct-validity gate, and provenance control are implemented and were exercised on D4; same-error identity, the rejection audit, cross-family generality, the full stress pipeline, and the software abstraction are specified but unbuilt; and no compression rung has run. What the instrument can already do — refuse a baseline that surface metrics passed, on a per-item construct-validity failure — it has done. What it cannot yet do, it does not claim.

---

## 4. Methods: The D1–D7 Certification Gate  *(STUB — model-free, to draft)*

```text
TO WRITE: formalise the D1–D7 gate (Paper 3 material) as the protocol spec —
provenance precheck, baseline correctness, shortcut resistance, strict-scoring
stability, NULL/abstention calibration, load matching, retention-sensitivity. Per the
C4/D1–D7 nuance recorded in §3: state each gate's evidential grain (some have a
specific counterexample — CAL-E forces strict-scoring stability, D4 saturation forces
retention-sensitivity; others are logically-required-but-not-yet-individually-stress-
tested). Do NOT present the whole gate as uniformly empirically validated.
```

## 5. Rejection Audit  *(STUB — model-free, HIGHEST-VALUE next per external reviewer)*

```text
TO WRITE / DESIGN: the symmetric control — the gate must audit its own REFUSALS, not
just acceptances (does it over-reject valid constructs?). An external reviewer named
this REQUIRED before the non-vacuousness claim of §3 holds. Currently SPECIFIED-BUT-
UNBUILT (§3.4). Design is model-free. The CAL-E (refusal reversed by item-read) vs
CAL-Q (refusal confirmed by item-read) contrast is the motivating material: the
discipline must fire even when the answer is "yes, really refuse," so the one time a
refusal would be wrong gets caught.
```

## 6. Discussion and Limitations  *(STUB — model-free, to draft)*

```text
TO WRITE: restate scope honestly (one family/one model/pre-stress); name the two
required extensions (external demonstration + the stress rung) as the path to Paper B;
position the contribution as an instrument paper, not a method or product. The
external reviewer's verdict — "the positioning is ready; the paper is not [yet a
methods submission]" — is the honest frame: this is a credible measurement/experience
contribution scoped to what is demonstrated.
```

## Supplement  *(STUB — model-free, to assemble)*

```text
TO ASSEMBLE: CAL-Q per-item data; the pre-declared decision rule; the four-way
reporting schema (strict / concept / true-false-emission / format-artifact); the
CAL-Q-format positive control (the §2.4 / §3 control confirming the 0.00 collapse is
real, not a parser artifact — 40/40 single-character value emissions). The TL evidence
document (numbers verified vs bytes this session: CAL sweep 1.000/0.975/0.950/0.975,
CAL-Q 0.650 + abstention 0.000/false-emission 1.000, CAL-E 13-of-17 lowercase
mis-scores) is the raw-evidence source, once its "proven" language is tightened to the
forcing-function standard.
```

---

## Closed gates (unchanged)

```text
No new run · No D4 rescue · No CAL-Q rerun · No certification · No compression · No
INT8/INT4 stress · No second compression rung · No full ladder · No Claim C
activation · No public benchmark packaging · No funder-facing release · No SBIR
submission. This is a model-free assembly of a paper draft. Paper B (the stress loop)
is PLANNED, not started; its loop requires a separate future Manager authorization.
```

## Assembly note

```text
This skeleton is a VIEW of the paper's shape, not the editable master of each section.
The versioned section files remain canonical: edit §2 in PAPER-POSITIONING-SECTION-
DRAFT, §3 in PAPER-INSTRUMENT-ARCHITECTURE-SECTION-DRAFT, then re-assemble. The
abstract, drafted here for the first time, should be split into its own reviewable
artifact if it goes to adversarial review (as the other sections did). Internal
scaffolding (per-section drafting notes, post-draft reviews, citation verification
record) is intentionally EXCLUDED here and retained in the source files; it must not
ship in the submitted paper but must be preserved for provenance.
```

— Senior Engineer
