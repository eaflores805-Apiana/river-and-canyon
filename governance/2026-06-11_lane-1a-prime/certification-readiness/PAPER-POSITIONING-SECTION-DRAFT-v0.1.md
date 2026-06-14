# PAPER-POSITIONING-SECTION-DRAFT-v0.1

**Version:** v0.1. River and Canyon program. DRAFT of the positioning / related-work + contribution section for the proposed Tier 1 methods paper ("A Fail-Closed Metrological Protocol for LLM Stress-Retention Evaluation" / "Before Retention: Baseline Certification and Claim-Safe Refusal").
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
an unmet item. Its unit of action is the conscientious researcher.

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
one yields a logged *refusal* rather than a number. The contribution is not the
validity concepts — those are field-owned — but the *enforcement architecture*:
validity wired as a gate that blocks the claim, with refusal as a first-class,
auditable output. This is the distinction between a checklist an author may pass
and a gate that does not let the claim through.

### 2.3 Demonstrating that the gate is non-vacuous

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
was the sought-after result. The protocol refused it. Reading the per-item outputs
showed that the same manipulation that lowered clean accuracy had simultaneously
collapsed the model's abstention on absence-defined (key-absent) items from ~0.92
to 0.00: under the harder query format the model emitted a value on every item
rather than abstaining. The difficulty manipulation had not stressed the measured
behaviour; it had *displaced* it, so the harder task no longer measured key-presence
discrimination at all. The protocol's pre-declared rule classified this as a
construct-validity failure of the difficulty lever and refused the baseline.[^1]

We emphasise what this example is and is not. It is *not* a discovery that
abstention is format-sensitive in general; that abstention degrades under stress is
established at scale [AbstentionBench 2025], and our observation is a controlled,
single-family corroboration of that direction, not a new phenomenon. What the
example demonstrates is the *protocol's* behaviour: a candidate baseline that met
the surface objective, that a results-driven process would have accepted, was
refused by a fail-closed gate on the basis of a per-item validity check — precisely
the action an advisory checklist cannot compel. The development history records
further instances of the same enforcement (a scorer/parser artifact caught by
per-item reading before it could distort a discrimination measurement; a
saturation-versus-elimination diagnosis that separated fixable from validly-rejected
constructs), which we report not as findings about models but as evidence that the
gate fires on real defects.

### 2.4 Scope and what we do not claim

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
the surface metrics passed. Establishing cross-family and cross-model generality,
and carrying a certified baseline through an actual stress rung, are stated as
required future work; until they are done, the contribution is a protocol with a
worked example, not a validated general method and not a product.

[^1]: Full per-item data, the pre-declared decision rule, and the four-way
abstention reporting (strict / concept-level / true false-emission / format
artifact) are in the supplementary material. The four-way reporting is itself a
consequence of an earlier enforcement episode, in which a case-sensitive NULL
parser mis-scored lowercase abstentions as emissions; per-item reading corrected
the aggregate, and the reporting schema was hardened so the artifact could not
recur unnoticed.

---

## POST-DRAFT REVIEW (internal — against the three targets)

```text
TARGET 1 — Bean distinction crisp? §2.2 states it as advisory/non-binding
  (unit = conscientious researcher) vs fail-closed/claim-blocking (unit = pipeline,
  output = refusal). The distinction is named explicitly and tied to the
  stress-retention setting where a pipeline can emit an uncertified retention
  number. Assessment: crisp; the reviewer's "isn't this their checklist?" is
  pre-answered. Residual risk: a reviewer may argue the checklist COULD be enforced;
  the paper should concede that and claim only that the present work IS the
  enforcement, in the retention setting, with a worked refusal.
TARGET 2 — Scope stated, not buried? §2.4 puts it in prose, names the model, the
  single family, and pre-stress status, and lists the three forbidden over-claims.
  Assessment: met; scope is a titled subsection, not a footnote.
TARGET 3 — Avoids forbidden over-claims? §2.1 explicitly disclaims discovering
  shortcut/validity/abstention; §2.3 explicitly frames the abstention observation
  as corroboration not discovery; §2.4 disclaims seam/compression/generality.
  Assessment: met. The AbstentionBench corroboration is the riskiest spot (it could
  read as leaning on a big result); it is framed as same-direction support, not
  borrowed credit.
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
