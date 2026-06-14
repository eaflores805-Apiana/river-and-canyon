# TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK-v0.1

**Version:** v0.1. River and Canyon program. Tier 1 positioning memo (model-free synthesis).
**Status:** model-free. Consolidates an ACTUAL literature search (run for this memo) into a citable prior-art and audience boundary. Authorizes nothing. Anchored on origin/main HEAD f87325b.
**Provenance note (important):** the Manager memo referenced "incoming literature checks." No prior literature-check artifact existed on disk. So this memo IS the literature check — its claims rest on a live web search of published work performed for this draft, cited below, not on phantom prior memos. Citation confidence is stated per row; CS should verify the source metadata independently.
Owner/drafter: Senior Engineer · CS: verify source names/metadata/overlap language/closed gates, flag unsupported claims · Team Lead: route to strategic record + prepare paper/playbook/audience decision surface · Manager: positioning decision.

---

## 1. Executive summary

The literature confirms the boundary the Manager drew, but is CLOSER to the
program's territory than the memo's framing assumed — and saying so is the point
of a prior-art check. Shortcut learning, construct validity in LLM evaluation,
abstention instability, aggregate-metric insufficiency, and quantization-degrades-
reasoning are ALL field-owned, several with very recent, prominent, directly
adjacent work. What remains plausibly distinctive is narrow and specific: **a
staged, fail-closed OPERATIONAL PROTOCOL that refuses to license a stress-
retention measurement until the baseline, scorer, artifact path, and construct
are certified — i.e. validity discipline wired as a gate that blocks the claim,
not as a checklist or a post-hoc critique.** That is defensible as a near-term
Tier 1 contribution, but the distinctiveness is in the *enforcement architecture*,
not in any of the underlying concepts, and the memo scopes it accordingly.

## 2. Research novelty boundary

```text
FIELD-OWNED (not ours, must be cited, must not be claimed as discovered):
  - shortcut learning / spurious cues          (Geirhos et al. 2020, Nat. Mach. Intell.)
  - construct validity in LLM/ML evaluation    (Bean et al. 2025 "Measuring what
                                                Matters", 445-benchmark review;
                                                Freiesleben & Zezulka 2025; ECBD 2024;
                                                Raji et al. 2021)
  - abstention instability / unanswerable Qs   (AbstentionBench, NeurIPS 2025;
                                                "Know Your Limits" survey, TACL 2025;
                                                SelfAware, 2023)
  - aggregate-metric insufficiency / reproducibility (lm-eval "Lessons from the
                                                Trenches" 2024; perplexity-isn't-
                                                correctness is standard)
  - quantization degrades reasoning            ("Quantization Meets Reasoning"
                                                2501.03035 / 2505.11574; ZeroQuant-V2;
                                                Llama-3.1 500k-eval study)
PLAUSIBLY DISTINCTIVE (ours, stated narrowly):
  - fail-closed OPERATIONAL ENFORCEMENT before stress-retention claims: a protocol
    where an uncertified baseline / scorer / artifact / construct BLOCKS the
    retention claim by construction, and "refuse to measure" is a first-class,
    logged output. Not the concepts — the gate that makes them binding.
```

## 3. Field-owned claims (the program must cite, not claim)

```text
- "Models exploit shortcuts / spurious cues." → Geirhos et al. 2020. OWNED.
- "Benchmarks often lack construct validity; tasks/metrics undermine claims." →
  Bean et al. 2025 reviewed 445 benchmarks and published an operational checklist
  for construct validity. OWNED — and this is the closest prior art (see §7).
- "LLMs fail to abstain on unanswerable questions; the capability is unstable, and
  reasoning training can DEGRADE it." → AbstentionBench 2025. OWNED — and directly
  adjacent to the CAL-Q finding (see §8).
- "Aggregate scores / perplexity don't equal correctness; evaluation needs
  validity not just numbers." → multiple. OWNED.
- "INT4 quantization degrades reasoning specifically, more than surface metrics
  suggest." → Quantization Meets Reasoning 2025. OWNED — and adjacent to the SEAM
  hypothesis itself (see §6).
```

## 4. Plausibly distinctive contribution (stated at the right scope)

```text
The contribution is NOT a concept; it is an enforcement architecture:
  (a) FAIL-CLOSED GATING: the protocol refuses to emit a stress-retention/
      compression-fragility claim unless a verified clean baseline, a fuzz-checked
      scorer, an artifact-locked provenance trail, and a certified construct are
      ALL present. Absent any one, the output is a logged REFUSAL, not a number.
  (b) STAGED CERTIFICATION (D1–D7 in the program's Paper 3): certification precedes
      retention measurement, as an ordered gate.
  (c) REFUSAL-AS-PRODUCT: "this measurement is not safe to interpret" is a
      first-class deliverable, with the per-item read and provenance that justify it.
What makes this plausibly distinctive vs. the field-owned validity work: the
existing work largely DIAGNOSES validity failures (checklists, surveys, post-hoc
critique). The program's claim is to OPERATIONALIZE the diagnosis as a BLOCKING
GATE specific to the stress-retention setting — the validity check is wired to
stop the claim, not to advise the author. That is a narrower, defensible delta.
```

## 5. Closest prior-art risks

```text
HIGHEST RISK — Bean et al. 2025, "Measuring what Matters" (construct validity in
  LLM benchmarks, 445-benchmark review + OPERATIONAL CHECKLIST). This is the
  nearest neighbor: it already operationalizes construct validity into an actionable
  checklist for benchmark design. The program must distinguish "a checklist authors
  SHOULD follow" (theirs) from "a fail-closed gate that BLOCKS a retention claim
  when unmet" (ours). If that distinction is not crisp, a reviewer will see the
  program's contribution as a domain-specific instance of their checklist.
HIGH RISK — Quantization Meets Reasoning 2025: a step-aligned protocol dissecting
  WHERE quantization degrades reasoning, with error-dimension taxonomy. This is
  adjacent to BOTH the seam hypothesis AND the instrument. The program's distinction:
  it does not yet measure degradation at all (pre-stress); its contribution is the
  VALIDITY GATE before such measurement, not the degradation finding (which they
  already have).
MODERATE RISK — AbstentionBench 2025: see §8.
MODERATE RISK — lm-eval reproducibility work: owns "consistent measurement across
  runs/models." The program's adjacent-but-distinct angle is validity-before-claim,
  not run-to-run reproducibility (they explicitly bracket validity; the program
  centers it).
```

## 6. Compression / retention overlap

```text
Quantization-degrades-reasoning is ESTABLISHED (INT4 up to ~32% reasoning-accuracy
loss on MATH; small models hit hardest, per ZeroQuant-V2). Implications:
  - The program must NOT claim novelty for "compression degrades reasoning" — it is
    known, including the reasoning-specific angle close to the seam.
  - The seam HYPOTHESIS (compression breaks LINKAGE while sparing components) is a
    more specific mechanistic claim than the literature's aggregate degradation
    findings — but the program has NOT tested it (pre-stress). So even the seam's
    distinctiveness is currently a hypothesis, not a result.
  - The defensible near-term position: the program's contribution is the
    VALIDITY-GATING that would let a seam measurement be TRUSTED, given that the
    literature shows degradation is real but measured with instruments whose baseline
    validity is rarely certified. The gate, not the degradation, is the contribution.
```

## 7. Construct-validity overlap

```text
This is the overlap that most constrains the novelty claim. Construct validity in
ML/LLM evaluation is an active, prominent area (Bean et al. 2025; Freiesleben &
Zezulka 2025; ECBD 2024; the Jacobs & Wallach measurement-modeling line). The
program CANNOT position itself as introducing construct validity to ML evaluation
— that framing would be rejected. The only defensible delta is the one in §4:
operational, fail-closed, claim-blocking enforcement in the specific stress-
retention setting, vs. the field's checklists/surveys/critiques. The memo's
forbidden list (§11) encodes this.
```

## 8. Abstention overlap

```text
AbstentionBench (NeurIPS 2025) is both a prior-art risk AND an unexpected
corroborator. It found that reasoning fine-tuning DEGRADES abstention (~24% avg),
and that abstention is an unsolved, scale-resistant problem. The program's CAL-Q
finding — abstention collapsed when the code-book query raised difficulty — is a
SMALL, SPECIFIC, SAME-DIRECTION echo (difficulty/format stress degrades abstention).
Implications:
  - The program must NOT claim to have discovered abstention instability — it is
    field-owned and the headline of a NeurIPS paper.
  - The honest framing: the CAL-Q finding is CONSISTENT WITH AbstentionBench, in a
    constructed controlled setting, and isolates a format/difficulty trigger. It is
    corroborating detail, not a new phenomenon. (This also strengthens the CAL-Q
    finding's external credibility — it aligns with independent large-scale evidence.)
```

## 9. Audience / buyer map (Table 2)

(Evidence-needed-before-pitch is intentionally demanding; nothing here is a
market claim — see §11/forbidden.)

```text
AUDIENCE 1: LLM eval teams at model labs / safety teams
  PAIN: stress/robustness evals that may be measuring artifacts (saturation,
        shortcuts, scorer bugs) and can't tell.
  EXISTING SUBSTITUTE: construct-validity checklists (Bean 2025), internal review.
  GAP: those are advisory; nothing BLOCKS a claim when the baseline is uncertified.
  WHY OURS MATTERS: a fail-closed gate that refuses the claim, with provenance.
  EVIDENCE NEEDED BEFORE PITCH: demonstrate the gate on a NON-synthetic eval
        (current evidence is one synthetic family); show it catches a real artifact
        a checklist missed.

AUDIENCE 2: Quantization / efficiency teams shipping compressed models
  PAIN: need to claim "retains capability" but degradation is task-specific and
        baseline validity is rarely certified.
  EXISTING SUBSTITUTE: standard quant eval (perplexity + downstream benchmarks).
  GAP: those don't certify whether the baseline measured the capability or a shortcut.
  WHY OURS MATTERS: certify the baseline before the retention claim is allowed.
  EVIDENCE NEEDED BEFORE PITCH: a single end-to-end certified baseline → stress
        rung (the program has NEVER run one; this is the missing proof).

AUDIENCE 3: Eval-tooling / benchmark vendors and standards efforts
  PAIN: validity critiques exist but aren't enforceable in a pipeline.
  EXISTING SUBSTITUTE: lm-eval (reproducibility), checklists (validity advice).
  GAP: no fail-closed validity GATE component.
  WHY OURS MATTERS: a drop-in refusal gate for stress-retention claims.
  EVIDENCE NEEDED BEFORE PITCH: a reusable, model-agnostic implementation (current
        work is bespoke to one family/model).

AUDIENCE 4 (weakest, name honestly): funders / SBIR
  PAIN: want a defensible metrology story.
  EXISTING SUBSTITUTE: the broader eval-validity literature.
  GAP: operational enforcement.
  WHY OURS MATTERS: a concrete protocol + a track record of catching its own errors.
  EVIDENCE NEEDED BEFORE PITCH: cross-family generality + at least one stress rung;
        without these the funder pitch is premature (see forbidden §11).
```

## 10. Safe paper framing

```text
CENTRAL FRAMING (per Manager): "The field has diagnosed many evaluation-validity
failures. This program contributes a staged, fail-closed operational protocol for
deciding when a stress-retention measurement is not safe to interpret."
TITLE OPTIONS (both acceptable):
  - "A Fail-Closed Metrological Protocol for LLM Stress-Retention Evaluation"
  - "Before Retention: Baseline Certification and Claim-Safe Refusal in LLM Stress
     Evaluation"
REQUIRED POSITIONING IN THE PAPER:
  - cite the field-owned work (§3) up front as the foundation;
  - claim ONLY the operational/fail-closed/claim-blocking delta (§4);
  - present the program's failure→control history (the methodology record) as the
    evidence the gate is non-vacuous (it caught real artifacts: the parser bug, the
    lever-validity failure, the saturation/elimination split);
  - state the scope limit plainly (one synthetic family, one model, pre-stress).
THE NEAR-TERM PUBLISHABLE CONTRIBUTION IS NOT THE SEAM RESULT. It is the
fail-closed validity instrument that prevented an invalid seam baseline from being
used — stated exactly that way.
```

## 11. Forbidden positioning

```text
Do NOT frame the work as (per Manager, each now backed by a specific prior-art
reason from the search):
  - "We discovered construct validity." → owned: Bean 2025, Jacobs & Wallach, etc.
  - "We discovered shortcut learning." → owned: Geirhos 2020.
  - "We discovered abstention instability." → owned: AbstentionBench 2025.
  - "We proved all absence-defined tasks fail." → one family, one model.
  - "We proved no task family can host a clean baseline." → only THIS family tested.
  - "We tested compression fragility." → pre-stress; never ran a rung.
  - "We found or refuted the seam." → untested; hypothesis only.
  - "We have a market-validated product." → no market evidence exists (§9 lists
    what each pitch would still need).
ADDITIONAL (from the search):
  - "We are the first to operationalize evaluation validity." → too strong; Bean
    2025 published an operational checklist. Claim the narrower fail-closed/
    claim-blocking/stress-retention-specific delta only.
```

## 12. Strategic implication

```text
The Tier 1 instrument is a REAL near-term deliverable, but its defensible novelty
is NARROWER than "we operationalize eval validity" — it is "fail-closed,
claim-blocking enforcement in the stress-retention setting." That is publishable
as a methods/protocol contribution IF positioned against the prior art honestly.
The audience is real but every near-term pitch has a concrete missing-evidence
item (§9), and the strongest two (cross-family generality, one certified stress
rung) are exactly what the program has not yet done. So: the instrument is
defensible as a PAPER now (with honest scoping); it is NOT yet defensible as a
PRODUCT (market unproven) or as a GENERAL method (one family). The hybrid strategy
holds, and this memo sharpens what "instrument-as-deliverable" can honestly claim
TODAY: a scoped protocol contribution, not a validated product.
```

## 13. Next evidence needed

```text
Before a PUBLIC paper:
  - crisp, defensible distinction from Bean et al. 2025 (checklist vs fail-closed
    gate) — the single most important positioning task;
  - the failure→control history written as the non-vacuousness evidence (the
    methodology record already largely does this);
  - explicit scope statement (one family, one model, pre-stress).
Before a FUNDER-facing pitch (all currently MISSING):
  - cross-family generality (≥1 second task family);
  - ≥1 end-to-end certified baseline → stress rung;
  - a reusable, model-agnostic gate implementation.
Before any PRODUCT claim:
  - evidence a named audience will adopt/pay (none exists yet).
RECOMMENDED IMMEDIATE NEXT (model-free): the §11 rejection-audit control draft
(unblocked, bounded), then a positioning section that nails the Bean-2025
distinction. Neither needs a run.
```

## 14. Closed gates

```text
No new run · No D4 rescue · No CAL-Q rerun · No certification · No compression · No
INT8/INT4 stress · No second compression rung · No full ladder · No Claim C
activation · No public benchmark packaging · No funder-facing release · No SBIR
submission. This memo is model-free (literature synthesis).
```

---

## Table 1 — Research novelty boundary

```text
SOURCE/AREA           OWNS                         OVERLAP RISK   WHAT REMAINS OURS              SAFE WORDING                              CITE CONF.
Geirhos 2020          shortcut learning            LOW            shortcut floor as a BLOCKING   "building on shortcut-learning           HIGH (Nat.
(shortcut learning)   (spurious-cue exploitation)                gate in stress setting         work (Geirhos 2020), we gate on it"       Mach Intell)
Bean 2025             construct validity in LLM     HIGH          fail-closed CLAIM-BLOCKING     "prior work provides validity             HIGH (arXiv
(construct validity)  benchmarks + op. checklist                 enforcement vs. advisory        checklists; we wire validity as a         2511.04703,
                                                                  checklist                       refusal gate"                             42 authors)
Quant-Meets-Reasoning compression degrades         HIGH          validity gate BEFORE the        "degradation is established; we           HIGH (arXiv
2025                  reasoning (step-aligned)                   degradation measurement         certify the baseline that makes it        2501.03035)
                                                                                                  trustworthy"
AbstentionBench 2025  abstention instability;       MODERATE       CAL-Q = controlled,            "consistent with AbstentionBench,         HIGH (NeurIPS
(abstention)          difficulty degrades it                     same-direction corroboration    we isolate a format/difficulty trigger"   2025)
lm-eval 2024          reproducible measurement      MODERATE       validity-before-claim, not     "complements reproducibility work;        HIGH (arXiv
(reproducibility)     across runs/models                         run-to-run consistency          we center validity they bracket"          2405.14782)
```

## Table 2 — Audience / buyer map

(Full version in §9. Compact form:)

```text
AUDIENCE              PAIN                    SUBSTITUTE        GAP                  WHY OURS              EVIDENCE NEEDED
lab eval/safety teams artifact-blind stress  validity          advisory only,       fail-closed refusal   non-synthetic demo +
                      evals                   checklists        nothing blocks       + provenance          catch-a-real-artifact
quant/efficiency      "retains capability"    perplexity +      no baseline          certify baseline      1 end-to-end certified
teams                 claims unverified       benchmarks        certification        before the claim      baseline→stress rung
eval-tooling/vendors  validity not            lm-eval +         no fail-closed       drop-in refusal       reusable model-agnostic
                      enforceable             checklists        validity gate        gate                  implementation
funders / SBIR        want metrology story    eval-validity     operational          protocol + error-     cross-family + ≥1 rung
(weakest)                                     literature        enforcement          catch track record    (else premature)
```

## Note on provenance discipline

```text
This memo was required to consolidate "incoming literature checks" that did not
exist on disk. Rather than cite phantom checks, the literature search was actually
performed for this draft and the sources are named with citation-confidence levels
for CS to verify. This is the program's own provenance standard applied to its own
strategy memo: do not assert a body of evidence you have not read. The single most
consequential finding is that the construct-validity overlap (Bean et al. 2025) is
CLOSER than the original framing assumed, which narrows — but does not eliminate —
the defensible Tier 1 contribution.
```

— Senior Engineer
