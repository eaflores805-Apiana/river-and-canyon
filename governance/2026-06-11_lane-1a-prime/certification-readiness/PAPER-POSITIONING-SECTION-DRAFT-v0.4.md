# PAPER-POSITIONING-SECTION-DRAFT-v0.1

**Version:** v0.4. **Supersedes v0.3** (5aff96d7), retained. River and Canyon program. DRAFT of the positioning / related-work + contribution section for the proposed Tier 1 methods paper ("A Fail-Closed Metrological Protocol for LLM Stress-Retention Evaluation" / "Before Retention: Baseline Certification and Claim-Safe Refusal"). v0.3 integrates Contributor 5 review (the structural fix). C5 identified that v0.2 distinguished against the WEAKEST prior art (Bean's advisory checklist) and routed around the CLOSEST: a fail-closed certification literature that already enforces and already emits refusal. All three of C5's named papers were independently verified (citations + claims confirmed via web search). v0.3 changes: (1) §2.2 rewritten to engage Noisy-but-Valid (2601.20913), Selective-Risk-Certification (2509.12527), and Safety-Under-Scaffolding (2603.10044) HEAD-ON, conceding that enforcement-posture and refusal-as-output are SHARED, and claiming only the narrow cell: construct-validity enforcement at the BASELINE gating a RETENTION claim, vs. statistical-reliability certification of a judge; (2) §2.3 now states the CAL-Q 0.00 collapse was confirmed by a CAL-Q-format scorer positive control (re-verified from bytes: format_abstention_artifact=0.0, 40/40 genuine emissions) and replaces the "displaced" mechanism claim with "refused on the observable validity failure regardless of mechanism"; (3) AbstentionBench softened from "corroboration of that direction" to "consistent with the broader finding that abstention is fragile" (their training-time intervention vs our inference-time manipulation = different mechanisms); (4) three citations flagged for CS independent confirmation before submission. v0.4 is a light polish per Contributor 4 (who assessed v0.3 "ready to move forward with only light polishing"): (a) §2.3 sharpened so the OBJECT of certification is the explicit point of difference — the certification literature certifies the *measurement process* (judge error rate, output reliability), this work certifies the *baseline itself* (did it measure the intended capability at all); (b) the longest sentences in §2.3 and the §2.4 abstention paragraph broken for readability, with the AbstentionBench mention now explicitly marked "context, not support" to further reduce the lean-on-a-big-result risk C4 flagged as the highest residual.
**Status:** model-free draft of academic prose (a paper section, not a governance memo). This is the paper's spine and highest-risk point: it must carve the program's narrow contribution against the closest prior art (Bean et al. 2025) crisply enough that a reviewer does not read the work as a domain-specific checklist instance. Anchored on origin/main HEAD a4d0709. Authorizes nothing; model-free.
**Citations:** real, from the literature search filed in TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK-v0.1 (dbb3833c). CS should verify metadata; arXiv IDs are given inline for checking.
Owner/drafter: Senior Engineer · CS: citation/metadata verification · Team Lead: route into the paper draft surface · Manager: positioning approval.

---

## DRAFTING NOTES (not part of the paper — for internal review)

```text
PURPOSE of this section in the paper: establish that the field already owns the
DIAGNOSIS of evaluation-validity failure, and that the contribution is the
ENFORCEMENT — a fail-closed gate that blocks a stress-retention claim, demonstrated
by a case where the gate refused the authors' own baseline. The load-bearing move
is the Bean-2025 distinction (advisory checklist vs claim-blocking gate). The
worked proof is D4/CAL-Q. The scope limit (one family, one model, pre-stress) is
stated here, not hidden.
REVIEW TARGETS: (1) is the Bean distinction crisp enough to survive "isn't this
their checklist?" (2) is the scope stated without burying it? (3) does it avoid the
forbidden over-claims (discovered shortcut learning / abstention / construct
validity / tested the seam)?
```

---

## 2. Background and Related Work

### 2.1 The field has diagnosed evaluation-validity failure

A substantial body of work establishes that benchmark scores can fail to measure
the capability they are taken to represent. Geirhos et al. [2020] characterise
*shortcut learning* — decision rules that perform well on a benchmark but rely on
spurious cues and fail to transfer — as a unifying account of many deep-learning
failures (arXiv:2004.07780). For language models specifically, a recent systematic
review of 445 benchmarks by Bean et al. [2025] documents widespread weaknesses in
how phenomena are operationalised, how tasks are constructed, and how metrics are
chosen, and argues these weaknesses undermine the validity of the resulting claims
(arXiv:2511.04703). Freiesleben and Zezulka [2025] develop construct-validity
conditions for predictive benchmarking from psychometric measurement theory
(arXiv:2510.23191), continuing a line that includes Evidence-Centered Benchmark
Design [2024] (arXiv:2406.08723) and earlier critiques of benchmark validity
[Raji et al. 2021]. Reproducibility-focused infrastructure such as the LM
Evaluation Harness [Biderman et al. 2024] addresses a complementary problem —
consistency of measurement across runs and models — while explicitly bracketing
validity (arXiv:2405.14782).

Two adjacent literatures bear directly on the present setting. First, abstention:
AbstentionBench [2025] shows that frontier models systematically fail to abstain
on unanswerable questions, that the failure is not resolved by scale, and —
notably — that reasoning fine-tuning *degrades* abstention by roughly 24% on
average (arXiv:2506.09038; NeurIPS 2025); a recent survey catalogues the broader
abstention literature [TACL 2025]. Second, compression: low-bit quantisation is
known to degrade reasoning specifically, with reported losses up to ~32% on
mathematical reasoning under aggressive INT4 schemes and a pronounced sensitivity
for smaller models [Quantization Meets Reasoning 2025, arXiv:2501.03035;
ZeroQuant-V2 2023].

We take all of the above as established. This paper does not claim to discover that
evaluations can be invalid, that models exploit shortcuts, that abstention is
unstable, or that compression degrades reasoning. Each is field-owned, and several
are the subject of recent, prominent, large-scale studies.

### 2.2 The gap: diagnosis is not enforcement

The work above is, with few exceptions, *diagnostic* or *advisory*. It identifies
validity failures, surveys their prevalence, and — at its most operational, in
Bean et al. [2025] — provides a **checklist** that benchmark authors are
encouraged to consult during design and to report as an appendix. A checklist of
this kind is a valuable instrument for improving practice. It is also, by
construction, *non-binding*: it advises an author, who remains free to proceed past
an unmet item. Its unit of action is the conscientious researcher. An advisory
checklist improves the probability that such an author will notice a problem; it
does not prevent a pipeline from emitting a retention number whose baseline was
never certified to measure the intended construct.

The present work addresses a different unit of action. In the specific setting of
**stress-retention evaluation** — measuring whether a capability survives a
controlled degradation such as quantisation — the central risk is not only that an
author overlooks a validity concern, but that a *pipeline* emits a retention number
whose baseline was never certified to measure the capability in the first place. A
retention score is a comparison against a baseline; if the baseline measured a
shortcut, or saturated at ceiling, or was scored by a parser that mis-categorised
the model's output, the retention number inherits that defect and reports it as
preserved capability [cf. the program's Paper 1, *survival is not correctness*].
An advisory checklist does not prevent this; it relies on the author to have caught
it.

We therefore propose to move validity discipline from *advice* to *enforcement*:
a **fail-closed protocol** in which a stress-retention claim is not emitted unless
a verified clean baseline, a fuzz-checked scorer, an artifact-locked provenance
trail, and a certified construct are all present, and in which the absence of any
one yields a logged *refusal* rather than a number.

### 2.3 Relation to fail-closed certification of evaluation

Enforcement and refusal are not, by themselves, new. A recent line of work already
treats evaluation as something to be *certified* rather than merely reported, and
already emits abstention or rejection as a first-class output with formal
guarantees. We engage it directly, because it is the closest prior art to the
present proposal and the distinction from it is what defines our contribution.

Noisy but Valid [2026, arXiv:2601.20913] certifies whether an LLM's failure rate
lies below a safety threshold under an imperfect judge, deriving a
variance-corrected critical value that guarantees finite-sample Type-I error
control: a genuine accept/reject gate on an evaluation. Selective Risk
Certification [2025, arXiv:2509.12527] issues information-lift certificates with
formal abstention guarantees, emitting *refusal* as a first-class output under
bounded risk. Safety Under Scaffolding [2026, arXiv:2603.10044] runs a
pre-registered specification-curve analysis across scoring degrees of freedom and
finds, among other things, that changing answer format on identical items shifts
measured scores by 5–20 points — larger than the effect under study — the same
scorer- and format-sensitivity our own reporting is designed to surface.

Against this work, "we enforce, the field advises" is too strong a claim, and we
do not make it. These methods enforce, and they emit refusal. They differ from the
present work in the *object* they certify. They take the construct as given and
certify properties of the *measurement process*: a judge's error rate, or whether
a given output is reliable enough to answer rather than abstain. The present work
certifies a property of the *baseline itself* — whether it measured the intended
capability at all (shortcut-free, off-ceiling, correctly parsed) — before any
retention comparison is permitted. Three things follow from this shift of object.
The trigger is not a bounded error rate but an uncertified construct. The gated
object is not a single measurement but a relative survival claim across a
controlled degradation. And the integration point is a per-item, provenance-locked
read rather than a distributional guarantee. We share the enforcement posture and
the refusal-as-output with this literature, and claim only this cell:
construct-validity enforcement on the baseline of a stress-retention comparison,
with per-item and provenance integration. This is also the distinction from the
advisory checklist of §2.2 — a checklist an author may pass and a gate that does
not let the claim through — but the sharper line is the one drawn here, against the
certification work that already enforces.

### 2.4 Demonstrating that the gate is non-vacuous

A blocking gate is only meaningful if it blocks things that would otherwise pass —
if it is not merely a gate that never closes on anything real, nor one calibrated
so loosely that it never fires. We substantiate the gate's non-vacuousness with the
program's own development history, in which the protocol repeatedly refused
artifacts that an advisory process would have waved through, including artifacts
the authors were motivated to accept.

The decisive case is the one for which we name the protocol. In constructing a
calibration baseline for a synthetic key-value lookup family, every content-based
attempt to move the clean baseline off its accuracy ceiling failed (the model
remained saturated, leaving no headroom to measure a degradation). A query-side
manipulation — an in-prompt code-book that required the model to resolve an alias
before performing the lookup — finally produced the first off-ceiling clean point
in the program's history. By the surface objective (off-ceiling difficulty), this
was the sought-after result. The protocol refused it. The refusal followed from a
per-item inspection. That inspection showed the query-form change had coincided
with a collapse of the model's abstention on absence-defined (key-absent) items:
the model emitted a value on every such item where it had previously abstained,
with measured abstention falling from ~0.92 to 0.00 on otherwise identical
content. Because a perfect 0.00 under a large format change is also the signature
of a scoring artifact — a parser failing to recognise the abstention token in the
new format — we verified the collapse with a positive control: a scorer exercised
on the CAL-Q output format confirmed that the emitted values were genuine
non-abstentions, not unrecognised abstention strings (no abstention token of any
casing appeared in the 40 key-absent outputs).[^1] The collapse is a real change
in the model's behaviour, not a measurement artifact. We do not adjudicate its
mechanism — whether the format change degraded abstention directly, or raised
difficulty which in turn degraded it — because the gate does not depend on the
mechanism: it refused the baseline on the *observable* validity failure, namely
that the off-ceiling task no longer measured key-presence discrimination at all.
The pre-declared decision rule classified this as a construct-validity failure of
the difficulty lever and blocked the baseline. The direction of the observation —
stress coinciding with degraded abstention — is consistent with the broader
finding that abstention is fragile and unsolved [AbstentionBench 2025]. We note
this only as context, not support: that work studies a training-time intervention
and ours an inference-time manipulation, and we claim no mechanistic agreement.
The contribution we do claim is the protocol's action: a candidate baseline
meeting every surface criterion was rejected by an automated validity gate on an
item-level check — precisely the enforcement an advisory checklist cannot compel.

Beyond this decisive case, the development history records further instances of the
same enforcement: a scorer/parser artifact caught by per-item reading before it
could distort a discrimination measurement, and a saturation-versus-elimination
diagnosis that separated fixable constructs from validly-rejected ones. We report
these not as findings about models but as evidence that the gate fires on real
defects rather than blocking arbitrarily or never closing.

### 2.5 Scope and what we do not claim

The evidence in this paper is deliberately narrow, and we state its limits plainly
rather than in a footnote. Our demonstrations are drawn from a single synthetic
key-value task family, on a single open-weights model (Qwen2.5-3B, FP16), and the
program is *pre-stress*: at the time of writing no certified baseline has been
carried through to an executed compression rung. We therefore do **not** claim to
have measured compression fragility, to have found or refuted any specific
"compositional seam," or to have established that the protocol generalises across
task families or models. We claim a *protocol* and a *demonstration that it
enforces*: a fail-closed metrological gate for stress-retention evaluation, shown
on a controlled case to refuse a baseline that failed a construct-validity check
the surface metrics passed. A broader claim would require demonstrating that the
protocol continues to fire on real defects across multiple task families, and that
a certified baseline can be carried through an actual compression rung; those
extensions are stated as required future work. Until they are done, the
contribution is a protocol with a worked example, not a validated general method
and not a product.

[^1]: Full per-item data, the pre-declared decision rule, the four-way abstention
reporting (strict / concept-level / true false-emission / format artifact), and the
CAL-Q-format scorer positive control used to rule out a parsing artifact are in the
supplementary material. The four-way reporting is itself a consequence of an earlier
enforcement episode, in which a case-sensitive NULL parser mis-scored lowercase
abstentions as emissions; per-item reading corrected the aggregate, and the
reporting schema was hardened so the artifact could not recur unnoticed. (Citation
note for finalisation: three references in §2.1 — Quantization Meets Reasoning,
arXiv:2501.03035, and its ~32% figure; the abstention survey listed as TACL 2025;
and ZeroQuant-V2's identifiers — require independent confirmation before submission;
the certification references in §2.3, arXiv:2601.20913, 2509.12527, and 2603.10044,
have been verified.)

---

## POST-DRAFT REVIEW (internal — against the three targets)

```text
TARGET 0 (C5, the structural fix) — Does the section engage the CLOSEST prior art,
  not just the weakest? v0.2 beat Bean's advisory checklist and routed around the
  fail-closed certification literature that already enforces and emits refusal. v0.3
  adds §2.3 engaging Noisy-but-Valid (2601.20913), Selective-Risk-Certification
  (2509.12527), and Safety-Under-Scaffolding (2603.10044) head-on; concedes
  enforcement + refusal-as-output are SHARED; claims only the narrow cell
  (construct-validity enforcement at the baseline gating a retention claim, vs.
  statistical-reliability certification of a judge). Assessment: the dangerous
  reviewer ("fail-closed eval certification already exists — what's new?") is now
  pre-answered with a narrow, defensible cell. All three citations independently
  verified. This was the load-bearing fix.
TARGET 1 — Bean distinction crisp? §2.2 states it as advisory/non-binding
  (unit = conscientious researcher) vs fail-closed/claim-blocking (unit = pipeline,
  output = refusal); §2.3 now adds that the sharper line is against the
  certification work, not the checklist. Assessment: crisp, and no longer the
  load-bearing distinction (the §2.3 cell is). Residual risk noted in §2.3: we
  concede the checklist could be automated and claim only the construct-validity
  trigger.
TARGET 2 — Scope stated, not buried? §2.4 puts it in prose, names the model, the
  single family, and pre-stress status, and lists the three forbidden over-claims.
  Assessment: met; scope is a titled subsection, not a footnote.
TARGET 3 — Avoids forbidden over-claims? §2.1 explicitly disclaims discovering
  shortcut/validity/abstention; §2.3 explicitly frames the abstention observation
  as corroboration not discovery; §2.4 disclaims seam/compression/generality.
  Assessment: met, hardened further in v0.3 per C5: (a) the 0.00 collapse is now
  stated as VERIFIED by a CAL-Q-format positive control (re-confirmed from bytes:
  format_abstention_artifact=0.0), removing the irony of an uncited number in a
  paper about uncited numbers; (b) the "displaced" mechanism claim is replaced with
  "refused on the observable validity failure regardless of mechanism"; (c)
  AbstentionBench softened to "consistent with the broader finding that abstention
  is fragile," with their training-time vs our inference-time mechanisms explicitly
  distinguished and no mechanistic agreement claimed.
OPEN ITEMS FOR THE FULL PAPER (not this section):
  - methods section formalising D1–D7 (Paper 3 material) as the gate;
  - the rejection-audit control (the symmetric half — the gate audits its own
    REFUSALS too) strengthens §2.3's non-vacuousness argument and should be drafted;
  - citation metadata verification (CS);
  - a precise statement of the pre-declared rule in the methods, since §2.3 leans on
    "pre-declared" doing real work.
```

---

## Closed gates

```text
No new run · No D4 rescue · No CAL-Q rerun · No certification · No compression · No
INT8/INT4 stress · No second compression rung · No full ladder · No Claim C
activation · No public benchmark packaging · No funder-facing release · No SBIR
submission. This is a model-free draft of a paper section.
```

— Senior Engineer
