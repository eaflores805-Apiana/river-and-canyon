# PAPER-INSTRUMENT-ARCHITECTURE-SECTION-DRAFT-v0.1

**Version:** v0.2. **Supersedes v0.1** (9de8e4c7), retained. River and Canyon program. DRAFT of the instrument-architecture section (§3, "What the instrument is") for the proposed Tier 1 measurement/experience paper. Companion to the positioning section (PAPER-POSITIONING-SECTION-DRAFT, §2) and the methodology record (failure→control provenance).
**Status:** model-free draft of academic prose. Built from the C6/contributor architecture inventory, with two corrections enforced against the on-disk evidence: (1) every module is tagged IMPLEMENTED-AND-DEMONSTRATED vs SPECIFIED-BUT-UNBUILT — the paper must never let a specified module wear the costume of a demonstrated one; (2) maturity percentages are stripped (they imply a product maturity the pre-stress, N≈1 status does not support and cannot be cited). Anchored on origin/main HEAD 0f7e9a7. Authorizes nothing; model-free. v0.2 integrates Contributor 4 review (which was filed against the TL evidence-breakdown document, NOT this section — see reconciliation note) plus the two honesty sharpenings flagged earlier: (1) §3.2 now states the FORCING-FUNCTION / necessity-proof framing explicitly as the section's evidential logic (modules shown necessary-via-counterexample and in some cases shown to fire, NEITHER a claim of generality), and (2) the construct-validity module adds the D1–D7 evidential-grain nuance (gates vary in support: some have a specific counterexample, others are logically-required-but-not-individually-stress-tested).

RECONCILIATION NOTE (TL evidence document vs this section): C4's feedback targeted the TL evidence-breakdown ("strongly proven / substantially proven" + Strong/Medium/Low table). Two findings: (a) every NUMBER in the TL document was verified against the bytes this turn and HOLDS exactly — CAL-A/B/C/E clean 1.000/0.975/0.950/0.975, CAL-Q clean 0.650, CAL-Q defective abstention 0.000 / false-emission 1.000, CAL-E rescore defective strict 0.575→concept-abstention 0.90 with abstention_forms {NONE:23, none:13} confirming the "13 of 17 lowercase mis-scores" claim; (b) C4's framing correction ("proven"→"demonstrated-as-necessary-via-counterexample") is CORRECT and is the same standard this section already used — so the two documents agree on FACTS and should converge on the conservative STANDARD. Disposition: this section (§3) is the canonical paper-prose version at C4's standard; the TL document is the richer evidence appendix (raw numbers, sweep table, 13-of-17) and its "proven" language should be tightened by its owner (C4 offered to do this). The two stay distinct artifacts, cross-referenced, converged on one honesty standard. Not silently merged.
**Evidence anchors (verified this turn):** four-way defective reporting is COMPUTED in `cal-q_run.json` (defective summary carries `strict_accuracy`, `concept_abstention_accuracy`, `true_false_emission_rate`, `format_abstention_artifact`); strict-vs-concept re-score in `cal-abce_rescore_summary.json`; same-error identity is computed on NO run (Paper-1 principle only) → SPECIFIED; no rejection-audit artifact exists → SPECIFIED; D1–D7 gate defined in Paper 3 (`certificationbeforeretention.pdf`).
Owner/drafter: Senior Engineer · CS: verify module/evidence claims against artifacts · Team Lead: route into paper draft surface + the run-loop decision surface · Manager: scope/venue + any execution authorization.

---

## DRAFTING NOTES (internal — not part of the paper)

```text
PURPOSE: this section answers "what is the instrument?" It reframes the contribution
from "a benchmark runner" to "a validity gate whose output is a ROUTE DECISION, not
a score." The section's integrity rule: each module is labelled by its evidence
status. IMPLEMENTED-AND-DEMONSTRATED = there is a computed artifact on disk showing
it ran on D4. SPECIFIED-BUT-UNBUILT = it is part of the designed architecture but
has no implementation/run yet. This split is the paper's defence against the exact
over-claim the program exists to catch; it is also what an external reviewer (who
flagged N≈1 evidence and pre-stress status) will check first.
DO NOT include maturity percentages. They are a private morale estimate, not a
measured quantity, and they imply product-readiness the evidence does not support.
SCOPE INHERITANCE: this section inherits §2.5's limits — one synthetic family, one
model (Qwen2.5-3B FP16), pre-stress. Nothing here claims generality or a stress result.
```

---

## 3. The Instrument: A Fail-Closed Validity Gate

### 3.1 What the instrument is

The instrument proposed in this work is not, in its primary function, a benchmark
runner that returns a score. It is a *validity gate* for evaluation results, whose
output is a route decision about whether a result can be trusted for a stated
purpose. The question it is built to answer is not "what did the model score?" but
"can this result be trusted enough to compare, to stress, or to support a claim?" —
and a first-class, legitimate answer is *no: not safe to compare*. A measurement
pipeline that can return that answer, with the per-item evidence that justifies it,
is the artifact this paper describes.

The instrument's output classes are therefore route decisions rather than scalar
scores. We distinguish: PASS (the baseline is certified; safe to compare or
proceed); NEEDS-REPAIR (the construct may be fixable, with a specified defect to
address); QUARANTINE (the data may be informative but cannot support a claim);
and PIVOT / FAIL-CLOSED (the route is invalid for the intended measurement, and no
claim is licensed). The load-bearing class is the refusal: *not safe to compare*,
emitted upstream of any retention comparison. This is the operational form of the
contribution positioned in §2 — construct-validity enforcement at the baseline,
gating a retention claim.

### 3.2 Architecture overview

At the level of design, the instrument takes an evaluation setup (baseline outputs,
stressed outputs if available, the scorer, the task specification, and the artifact
or provenance trail) and applies an ordered set of checks, each of which can route
the result away from PASS. The checks are: baseline correctness and constructibility;
shortcut-floor and off-ceiling band; scorer validity; defective-case discrimination;
format-artifact detection; same-error identity; provenance and route control; and a
rejection audit of the instrument's own refusals. The design is fail-closed: a
result reaches PASS only if every applicable check is satisfied, and the absence of
any one routes to refusal, repair, or quarantine rather than to a reported number.

The remainder of this section describes each module **and states its evidence
status**. We distinguish modules that are *implemented and demonstrated* — for which
a computed artifact exists showing the module ran on the D4 task family — from
modules that are *specified but not yet built* — part of the designed architecture,
but without an implementation or a run. This distinction is not incidental
bookkeeping; it is the boundary between what this paper demonstrates and what it
proposes, and we hold it explicitly because the instrument's entire purpose is to
prevent unsupported claims, including our own.

A note on the *kind* of evidence this section offers, because it determines what
the demonstrations can and cannot support. The modules below were not designed in
the abstract and then validated; they were *forced into existence by documented
failures and near-failures* in the program's own development. The argument for each
is therefore a forcing function — "without this check, a specific wrong decision
would have been (or nearly was) made" — rather than a claim of broad positive
validation. This yields two honest categories of support: a module can be shown
*necessary* (its absence demonstrably produced a wrong route on a real case) and,
in some cases, shown to *fire correctly* (it caught the defect on the case at
hand). Neither is a claim of *generality*: a forcing function on one or two cases
establishes that a check is needed and that it worked there, not that it
generalises across task families or models. Where this section says a module is
demonstrated, it means demonstrated-as-necessary-via-a-documented-counterexample,
at the case count stated — not proven in general. The distinction is the program's
own standard applied to its own instrument, and it is what keeps the strong claims
("the gate refused a baseline that surface metrics passed") separate from the
claims not yet earned ("the gate generalises").

### 3.3 Implemented and demonstrated modules

The following modules exist as computed artifacts and were exercised on the D4
synthetic key-value family on Qwen2.5-3B (FP16).

**Baseline gate (IMPLEMENTED-AND-DEMONSTRATED).** The instrument does not trust a
baseline merely because the model answers correctly. It checks whether clean
accuracy is off the saturation ceiling (so there is headroom to measure a
degradation), above the shortcut floor (so the score is not attributable to a
position or layout cue), and whether the defective case remains defective. The D4
calibration sweep exercised this gate directly: candidate baselines were routed by
exactly these criteria, and the recurring failure was clean saturation at ceiling,
which the gate is built to catch.

**Scorer-validity / strict-versus-concept audit (IMPLEMENTED-AND-DEMONSTRATED).**
A scorer that mis-categorises an output corrupts every downstream number. The
instrument computes a strict score and a concept-level score and compares them; a
divergence flags a scoring artifact. This module was not designed in the abstract —
it was forced by a real failure (the CAL-E episode), in which a case-sensitive
parser scored a lowercase abstention as a wrong answer; the concept-level read
showed the model was in fact abstaining. The re-scored result is on disk
(`cal-abce_rescore_summary.json`), and the strict/concept divergence is the
computed evidence that the module fires.

**Four-way defective reporting (IMPLEMENTED-AND-DEMONSTRATED).** For absence-defined
(key-absent) items, a single accuracy number conflates distinct behaviours. The
instrument reports four separate quantities: strict accuracy, concept-level
abstention, true false-emission rate, and a format-abstention artifact fraction.
All four are computed in the D4 run records (the `cal-q_run.json` defective summary
carries `strict_accuracy`, `concept_abstention_accuracy`, `true_false_emission_rate`,
and `format_abstention_artifact`). This is a concrete reporting schema, not a
described intention, and it is itself a consequence of the CAL-E enforcement episode.

**Construct-validity gate (IMPLEMENTED-AND-DEMONSTRATED, on one case).** The
instrument checks whether a manipulation intended to change task difficulty
preserved the behaviour being measured. The CAL-Q episode is the demonstration: a
query-side code-book lowered clean accuracy — which by the surface objective looked
like success — while collapsing the model's abstention on key-absent items from
~0.92 to 0.00. The gate classified this as a construct-validity failure (the
manipulation displaced rather than stressed the measured behaviour) and refused the
baseline. The per-item data and the positive control ruling out a scoring artifact
are on disk. We state the evidence scope precisely: this module is *demonstrated on
a single case*, the one for which the protocol is named; it is not yet shown across
families or models.

A clarification on the certification protocol as a whole (the D1–D7 gate
specified in the methods section). The gates were forced into existence
collectively by the program's failures, but they do not all carry the same weight
of direct evidence, and we do not present them as uniformly demonstrated. Some have
a specific counterexample behind them — the strict-scoring-stability gate is forced
by the CAL-E parser artifact, and the retention-sensitivity gate is forced by D4's
saturation leaving no headroom to measure a degradation. Others are, at present,
better described as *logically required but not yet individually stress-tested
across many cases* — they follow from the same reasoning but lack a dedicated
counterexample in the current record. The methods section states this gate-by-gate
rather than claiming the whole protocol is empirically validated; here we flag only
that "the D1–D7 gate exists" is a design-and-necessity claim, not a claim that every
gate has been independently demonstrated.

**Provenance / route control (IMPLEMENTED-AND-DEMONSTRATED).** The instrument treats
authorization, route state, and artifact sealing (hashes, paths, model-free-versus-
execution status) as part of claim safety, not bureaucracy. A retention claim is
licensed only if its evidence is on an authorized route with a sealed artifact
trail. This module is realised in the program's governance records and commit/hash
discipline, which gate whether a given result may be used for a claim at all.

### 3.4 Specified but not-yet-built modules

The following are part of the designed architecture but have **no implementation or
run**. We list them as specified — not demonstrated — because the paper's integrity
depends on the distinction.

**Same-error identity (SPECIFIED-BUT-UNBUILT).** A retention measurement should not
ask only "did the answer survive?" but "was it correct before, correct after, and
if wrong, was it the *same* wrong answer?" — distinguishing preserved capability
from preserved error. This is a designed scoring layer and, in the program's
judgement, an important one; it follows directly from Paper 1's argument that
survival is not correctness. But it is computed on no run in the present work: it is
a *proposed* layer the protocol specifies, not a demonstrated one. We are explicit
about this because same-error identity is exactly the kind of compelling idea whose
status (designed vs demonstrated) is easy to blur, and the instrument's purpose
forbids that blur.

**Rejection audit (SPECIFIED-BUT-UNBUILT).** A fail-closed instrument can fail by
being too strict — refusing valid constructs as readily as invalid ones. The
designed remedy is a rejection audit: for each refusal, check whether it was
correct, whether it could be a scoring artifact, whether per-item reads confirm it,
and whether the rule was pre-declared rather than post-hoc. The CAL-E and CAL-Q
episodes together motivate this module (each is, in effect, a refusal whose
soundness had to be checked), but it is not yet built as a standing component, and
no rejection-audit artifact exists. It is named by an external review as required
content before the instrument's non-vacuousness claim is fully supported; we
concur, and it is the highest-value model-free module remaining to design.

**Cross-family / cross-model generality (SPECIFIED-BUT-UNBUILT).** The instrument
has been exercised on one synthetic task family and one model. Demonstrating that
its gates continue to fire on real defects — and do not over-reject valid
constructs — across a second task family, an external benchmark slice, or a
different model is specified as necessary, and not yet done.

**Full stress-retention pipeline (SPECIFIED-BUT-UNBUILT).** The end-to-end path the
instrument is ultimately for — certified baseline → compression stress → retention
interpretation — has not been run. The program is pre-stress: no certified baseline
has been carried through an executed compression rung. This is why the work cannot
yet be presented as a compression-retention result or product; the instrument is
the precondition machinery, demonstrated up to but not through the stress step.

**Software abstraction (SPECIFIED-BUT-UNBUILT).** The instrument currently exists as
a protocol, a set of scorers and run records, governance gates, and manual per-item
reads. A reusable product form — a CLI or library, fixed input/output schemas,
automated claim-safe reports, an audit packet — is specified but early; most of the
repeatable machinery is not yet abstracted into a tool another team could run.

### 3.5 What this section claims

This section claims an *architecture* — a fail-closed validity gate whose output is
a route decision — of which a coherent subset is implemented and demonstrated on one
task family, and the remainder specified. It does not claim a finished tool, a
validated general method, or a stress-retention result. The honest summary is
structural rather than quantitative: the architecture is specified; the baseline
gate, scorer-validity audit, four-way reporting, construct-validity gate, and
provenance control are implemented and were exercised on D4; same-error identity,
the rejection audit, cross-family generality, the full stress pipeline, and the
software abstraction are specified but unbuilt; and no compression rung has run.
What the instrument can already do — refuse a baseline that surface metrics passed,
on a per-item construct-validity failure — it has done. What it cannot yet do, it
does not claim.

---

## POST-DRAFT REVIEW (internal — against the integrity rule)

```text
INTEGRITY RULE — every module labelled by evidence status?
  Implemented-and-demonstrated (5): baseline gate, scorer-validity/strict-vs-concept,
    four-way reporting, construct-validity gate (one case), provenance control.
    Each tied to a named on-disk artifact. PASS.
  Specified-but-unbuilt (5): same-error identity, rejection audit, generality,
    full stress pipeline, software abstraction. Each labelled, none costumed as
    demonstrated. PASS.
PERCENTAGES STRIPPED? Yes — §3.5 gives a structural summary, no numbers. PASS.
SCOPE INHERITED FROM §2.5? Yes — one family, Qwen2.5-3B FP16, pre-stress restated.
OVER-CLAIM CHECK: same-error identity (the inventory's "strongest idea") is
  explicitly demoted to SPECIFIED — the single most important correction, since it
  was the item most at risk of wearing the demonstrated costume. PASS.
RESIDUAL: "construct-validity gate" is demonstrated on N=1 (CAL-Q). Labelled as
  such in 3.3 and 3.5. A reviewer will still note N=1; that is a true limit, stated,
  not hidden — and the rejection-audit + generality modules are exactly its remedy.
OPEN FOR THE FULL PAPER:
  - the methods section formalising D1–D7 (Paper 3 material) as the gate spec;
  - the rejection-audit module design (model-free, highest-value next);
  - CS verification of each module/artifact claim.
```

---

## Closed gates

```text
No new run · No D4 rescue · No CAL-Q rerun · No certification · No compression · No
INT8/INT4 stress · No second compression rung · No full ladder · No Claim C
activation · No public benchmark packaging · No funder-facing release · No SBIR
submission. This is a model-free draft of a paper section.
```

---

## Note for Team Lead — the run-loop decision surface

```text
The architecture section makes the run-loop fork concrete and routable.
THE DECISION (Manager-owned, execution-gated): run a full end-to-end loop now
  (certified baseline → compression stress → retention interpretation), OR write
  paper (A) on the architecture-and-demonstration already on disk and defer the loop.
THE TWO ROUTES:
  (A) Measurement/experience paper — WRITABLE NOW, model-free. Contribution = the
      validity-gate architecture + the implemented modules + the D4/CAL-Q
      demonstration + honest scope. Positioning (§2) done; this architecture section
      (§3) drafted; methodology record supplies failure→control evidence. The
      external reviewer named this a credible contribution once §4.1–4.3 are addressed.
  (B) Methods paper with empirical core — REQUIRES the loop (execution-gated, Manager
      authorization). Adds an external demonstration + ≥1 stress rung. Cannot be
      written until the runs happen.
WHY THE FRAMING MATTERS: the two routes are mutually informative. Writing (A) first
  specifies exactly what the loop in (B) most needs to demonstrate (which module to
  exercise externally, which stress rung discriminates), so (A)-then-(B) may be more
  efficient than (B)-cold. But that is a recommendation, not a decision; the loop
  authorization is the Manager's.
SENIOR POSITION (advisory): (A) is earned now and de-risks (B). Recommend routing
  the loop question to Manager WITH the option to sequence (A) first.
```

— Senior Engineer
