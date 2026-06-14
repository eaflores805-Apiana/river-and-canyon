# NORTH STAR — What Must Be True For This To Become A Real Measurement Tool

**Version:** v1.2. River and Canyon program. Strategic guiding document.
**Status:** standing North Star. Not a gated experimental artifact, not a claim ledger, not a routing. It authorizes nothing and constrains nothing operationally. Its job is to be the thing the team re-reads when it loses the thread — to convert "what can we run next?" into "what must be true for this to be worth running?" Maintained as a living document; supersede by versioned replacement only, no silent edits. Owner: Manager. Review cadence: quarterly or upon ladder advancement. (Change log: Appendix A.)

---

## 0. How to use this document

Read this when any of these happen:

```text
- someone proposes the next experiment before the last one is interpreted
- the work starts to feel like a pile of clever runs rather than a tool
- a result tempts a claim bigger than the evidence ("INT8 is robust")
- the team disagrees about what we are even measuring
- a deadline or a funder makes "ship something" louder than "ship something true"
- a quarantined result tempts promotion to the official sequence
- a run is proposed because the infrastructure is ready, not because the
  question is ready
```

It is deliberately not a task list. §8's ladder is the closest thing to "what next," but the rest is the *standard against which any next step is judged.* If a proposed action does not move us along the ladder or harden one of the questions below, it is motion, not progress.

---

## 1. The one question

```text
Can this become a trustworthy measurement system for model behavior under stress,
not just a collection of interesting experiments?
```

Everything else is a sub-question of this. The honest test of value is not "did we run a compression rung" — it is "can a stranger trust what the rung's number means." A ruler is valuable because of what it *refuses* to measure sloppily, not only because of what it measures.

---

## 2. What the program is, and the governing rule (operational)

A physical analogy — weights as carved stone, activations as water — is used **only as a disciplined hypothesis generator, never as evidence.** Ideas it produces are stripped of metaphor, stressed until they break, and only what survives becomes a claim, a paper, or an experiment. The current domain is **quantization as behavioral stress metrology**: measuring what capabilities retain under numerical stress while preventing retention metrics from mistaking preserved *error* for preserved *capability*.

**The stressor is a basis, not a dial (v1.2 detail).** "Numerical stress" is not a single knob turned from FP16 down to INT4. Quantization is a *family* of distinct methods — weight-only versus weight-plus-activation; INT8 / INT4 / FP8; AWQ, GPTQ, SmoothQuant, rotation-based and codebook methods; QAT — each of which preserves and discards different structure. Treated as a basis rather than a dial, a failure stops being a verdict ("fragile") and becomes a coordinate ("fails under *this* method, survives *that* one"). A pattern across methods is then a structural **hypothesis** about what kind of representation a behavior lives in — evidence only after the measurement confounds below are ruled out per rung, never structural on its own. Two cautions bind that inference: methods are entangled bundles, not clean scalpels (AWQ and GPTQ differ in calibration sensitivity and outlier handling at once, not only in "what they preserve"), so a profile localizes representation only insofar as the methods' other differences are matched; and the deeper target — does linked/compositional behavior have a different fragility profile than its component operations? — must be guarded against the mundane reading that the harder task simply degrades first, ruled out only by matching difficulty/headroom across component and composite items (the load-matching the program already builds in). With those guards, the "seam" is reframed from a single cliff at some bit-depth to a **difference between profiles** — a candidate, never self-certifying. This is a sharpening of *what "stress" means in the one question above*, not a new goal. It is the right question to ask, **not a known result**: we are reaching to learn whether method-resolved stress can expose structure at all, prepared for the honest answer to be "not legibly, not yet, not here." It raises the bar on certification rather than lowering it — a richer readout has more ways to manufacture apparent structure from artifacts (shortcut, calibration mismatch, scorer artifact, format instability, task saturation), so no profile is trusted until baseline and measurement are certified and methods are compared only after each rung is independently interpretable. **This frame is a question, not a warrant:** no sweep may cite it as authorization to run, and no per-method result may cite it to upgrade itself from a coordinate to a structural claim. (Full framing kept as the companion note "What Kind of Smoothing?" v0.2, of which this paragraph is the compression.)

Governing rule, verbatim and load-bearing:

```text
The analogy points. Mechanism judges. Experiments execute. Papers report only
what the evidence earns. Mechanism claims are BLOCKED program-wide; everything
is behavioral.
```

**Made operational (not aspirational):**

```text
- No claim may contain the analogy.
- Every experimental authorization must name (a) the specific behavioral
  construct being tested and (b) the minimum evidence required to interpret the
  result.
- If either is missing, the gate is HOLD by default.
```

### "No Mountain in the Sentence" — the two-step check

The companion epistemic rule: strip the analogy out of any claim and state it in the real system's own terms. If you cannot, you do not have a claim. Made into a checklist that must actually run:

```text
1. The AUTHOR supplies the metaphor-stripped version of the claim, using only
   model, task, artifact, and measurement terms — no analogy.
2. The REVIEWER attests that the stripped version stands on its own without the
   analogy.
If either step is missing: HOLD by default.
```

The North Star is the place these rules point to: the tool is real exactly to the degree its claims survive having the metaphor removed *and a second person confirms it.*

---

## 3. What is already TRUE (the North Star is not pure ambition)

A guiding document that only lists aspirations becomes a wish. To stay honest — and to obey the program's own anti-inflation discipline — here is the current standing, stated at the same strictness we demand of any result:

```text
ESTABLISHED (released or byte-verified):
  - Survival ≠ correctness. Staged fail-closed scoring; a retention score can
    preserve error as if it were capability. (Paper 1, RELEASED.)
  - Correctness ≠ constructibility. A baseline can score well via a
    position-contaminated shortcut rather than genuine operation. (Paper 2,
    RELEASED; Claim B; salient-endpoint attraction is the recurring confound.)
  - Hash integrity ≠ construct validity. Matching bytes proves transmission,
    not that an artifact instantiates the concept it claims. (Standing note.)
  - Certification before retention. A D1–D7 fail-closed gate must pass as a
    STRUCTURE, not a score, before a surface can host a retention reading.
    (Paper 3, RELEASED.)
  - The gate is non-vacuous. It catches something real (the Cell03
    decomposition), it does not block trivially.
  - The instrument can fire on a real candidate, in one condition class:
    the constructed-positive validation eliminated a planted defect and spared
    its matched clean twin, at FP16.
      → PRECISE SCOPE: Layer-2 is PRESENT for the constructed-positive condition
        class ONLY; ABSENT for real-candidate elimination generally.

NOT YET TRUE (honest, and central):
  - No CERTIFIED-baseline compression rung has been run. The one INT8 rung is
    quarantined (procedurally nonconforming) and does not count.
  - The program is PRE-STRESS in its official sequence. Every purpose-built
    construction so far failed its FP16 baseline gate — which is why the
    MEASUREMENT INSTRUMENT, not the original seam hypothesis, is the primary
    contribution to date.
  - Generality is unclaimed: one task family (key→value lookup), one model
    family (Qwen2.5), one scale (3B), one precision step (FP16→INT8).
```

The most important sentence in this section: **the instrument is the contribution so far, and that is a real result, not a consolation prize.** A validated ruler that has not yet measured anything under stress is worth more than an unvalidated measurement of everything.

### 3a. Governance-state (process honesty)

```text
Route discipline has been tested twice under ambiguity:
  - the Path A schedule mismatch;
  - INT8-RUNG-1 executed during route reconciliation.
Both required quarantine or heavy qualification.
Semantic-read is ACTIVE for artifact validity.
Route-level ambiguity protection remains INCOMPLETE — it is a known open edge,
  not a solved problem, and Phase 0 of the Program Stage Map exists to close it.
```

---

## 4. The value proposition, sharpened

Why would a researcher or company use this instead of existing evals?

```text
Normal evals mostly ask: did the score change?
This framework asks, before it trusts any score:
  - was the measured CONSTRUCT valid? (or saturated / shortcut-driven / invalid?)
  - was the BASELINE certified as a structure, not just high-scoring?
  - did the SAME behavior actually survive, or did stable wrongness masquerade
    as retention?
  - is apparent retention real capability, or preserved error?
  - which firing CRITERION fired, and is it stable, or format-contingent?
```

The product is **trustworthy refusal as much as trustworthy measurement.** The differentiator is not a better accuracy number; it is a defensible statement of when a number is meaningless.

But the balance must hold both ways: **a tool whose refusals never lead to valid measurement is not yet a usable measurement tool.** The refusals earn their value only if valid measurement eventually happens behind them. If the control apparatus grows while the measurement apparatus does not, the program has built a gate that guards an empty room. Governance is accountable to measurement (see the proof-of-life criteria in the Program Stage Map), not a replacement for it.

### 4a. What "semantic-read" actually means (not review prose)

Wherever this document says "artifact semantic-read," it means a specific, required validity artifact — **not vague review commentary.** It is:

```text
- the nine-field shown-read form (artifact / path / commit SHA / sha256 /
  claimed concept / check performed / observed structure / required structure /
  surplus check), closed with a disposition;
- subject to a MECHANICAL-RENDERING FLOOR — the artifact's actual bytes are
  rendered and read, not summarized or reconstructed from memory;
- carrying path / commit SHA / sha256 so the read is anchored to exact bytes;
- disposed PASS / HOLD / UNCERTAIN (UNCERTAIN routes as HOLD for any
  decision-bearing artifact);
- carrying an OWNER SIGNATURE — a named reviewer who performed the read and
  stands behind the disposition (an unsigned read is not a completed read).
```

A "semantic-read" that is prose without the nine fields, the rendering floor, the byte anchors, and an owner signature is not a semantic-read and does not satisfy any gate that requires one.

### 4b. Making refusals countable

"Trustworthy refusal" is the product, so it must be loggable, not rhetorical:

```text
A REFUSAL COUNTS when it is:
  1. issued BEFORE model execution,
  2. cites a NAMED prerequisite that is false (e.g. baseline uncertified,
     construct saturated, artifact semantic-mismatch, route unauthorized), and
  3. confirmed by a LATER AUDIT to have prevented an uninterpretable result.
Refusals meeting all three are logged. The count of audited, execution-preventing
refusals is a primary value metric — not a side effect.
```

---

## 5. The questions that must be answered (the original ten, with "answered when")

These are the load-bearing questions from the founding analysis. Each is paired with a concrete "answered when" so the North Star is checkable.

```text
1. WHAT ARE WE MEASURING (operationally, not metaphorically)?
   Answered when: every reported quantity maps to a named construct —
   baseline correctness, retention, same-error identity, criterion identity,
   abstention stability, format-vs-content separation, artifact/concept
   validity, clean/defective discrimination, component-vs-composite
   vulnerability — with no metaphor in the definition.

2. WHY BETTER THAN NORMAL BENCHMARKS?
   Answered when: a third party can state the validity guarantee this gives
   that a raw eval does not, in one sentence, without reference to us.

3. CAN THE RULER CATCH BAD CASES?
   Partially answered (one defect class, one condition class fired).
   Fully answered when: it catches MULTIPLE defect types, avoids
   over-eliminating clean controls, separates format from capability errors,
   flags task invalidity BEFORE model execution, and quarantines nonconforming
   runs. (Ladder L1→L2, L5.)

4. CAN IT WORK ACROSS MODELS?
   Answered when: gate STRUCTURE ports across Qwen / Llama / Mistral / Gemma,
   across sizes, across quantization methods, across tasks — with the explicit
   caveat that THRESHOLDS are construction/model/task-specific until
   independently justified. Do not scale a confused ruler; that buys faster
   confusion. (Ladder L3.)

5. CAN IT PRODUCE DECISION-USEFUL REPORTS?
   Answered when: the output fits the schema in §7 and a non-author can act on it.

6. CAN IT REDUCE FALSE CONFIDENCE?
   The biggest one. Answered when: the tool demonstrably BLOCKS bad claims
   ("INT8 is robust", "INT4 preserves reasoning", "this benchmark proves
   compression safety") on evidence that only supports something narrower.
   Catching false GOOD news is the proof. (Ladder L4.)

7. CAN IT BE EFFICIENT?
   Answered when: artifact checks, semantic-read templates, baseline
   certification, scorer runs, identity tracking, failure classification,
   quarantine labels, and claim-safe report generation are AUTOMATED, and the
   human layer approves gates and interprets edge cases rather than babysitting
   rows. (Ladder L6.) SUBJECT TO the automation limits in §7a.

8. CAN IT GENERATE PAPERS AND EXPERIMENTS CLEANLY?
   Answered when: each stage yields something publishable OR reusable, and
   every paper claim follows the evidence, not the ambition. A negative result
   is a publishable result of record — that is a feature, not a fallback.

9. CAN IT TELL US WHEN NOT TO TEST?
   Underrated and central. Answered when: the tool reliably says "do not run
   yet" — artifact invalid, route unauthorized, baseline uncertified, construct
   saturated, result would be uninterpretable — and is RIGHT. (See the EXIT
   rule, §9, and the refusal definition, §4b.)

10. WHAT WOULD PROVE IT IS VALUABLE?
    The validation ladder, §8.
```

---

## 6. Anti-goals — what this must NOT become

A North Star says what we steer away from as clearly as what we steer toward. The program fails if it becomes any of these, even while producing impressive-looking output:

```text
- A leaderboard. We are not racing accuracy numbers; we are certifying whether
  numbers mean anything.
- A confused ruler scaled wide. Portability before the measurement logic is
  locked produces fast, confident, wrong answers across many models.
- An analogy that forgot it was an analogy. The moment "the seam" or "the
  canyon" appears in a claim instead of the real-system mechanism, stop.
- A retroactive milestone machine. An off-sequence or ambiguous-gate run is not
  promoted to an official result because the data looked good.
- A SYSTEM THAT TREATS PROCEDURALLY NONCONFORMING RUNS AS OFFICIAL MILESTONES
  WHEN THE DATA LOOKS USABLE. This is not hypothetical: INT8-RUNG-1 produced a
  clean-looking pattern and was correctly QUARANTINED rather than promoted. The
  quarantine is the behavior to repeat, not the exception to regret.
- An ambition-led paper mill. Claims that outrun evidence destroy the one asset
  the tool has — that its refusals can be trusted.
- A system that only says "run." A ruler that cannot say "do not test" is just
  another eval with extra steps.
```

The single anti-goal that dominates the rest: **the day a stress number is trusted that should not be, the tool is worth less than no tool**, because it now launders false confidence with a credibility we built specifically to prevent that.

---

## 7. The report the tool must eventually produce

The external artifact has to be simple enough that a lab, company, or reviewer can act on it without reading the methodology:

```text
Model:
Stress condition:
Result status:                               OFFICIAL / QUARANTINED / EXPLORATORY
Baseline certified (structure, not score):   yes / no
Artifact semantic-read:                       PASS / HOLD / UNCERTAIN
Construct validity (saturated / shortcut / valid):
Retention result:
Correctness result (capability vs preserved error):
Same-error identity:
Criterion identity (and is it stable / format-contingent?):
Abstention stability:
Failure class:
Claim-safe interpretation:
Use recommendation:  SAFE TO COMPARE / NOT SAFE TO COMPARE /
                     BASELINE UNCERTIFIED / SEMANTIC MISMATCH /
                     SCHEDULE DEGENERATE / TELEMETRY QUARANTINED /
                     RESULT QUARANTINED
```

If the tool can fill this in honestly and a third party can reproduce it, it is real. The "Result status" and "Use recommendation" lines are the product.

### 7a. Automation limits

```text
Clerical operations MAY be automated (artifact checks, template population,
hash recomputation, report scaffolding, label propagation).
Automation is STRUCTURALLY BARRED from model-facing execution gates.
No script or template may substitute for fresh human semantic review of
load-bearing artifacts.
```

Efficiency is a goal; it is bounded by the rule that a machine may prepare a gate but may not open one, and may not stand in for the human reading of a load-bearing artifact.

---

## 8. The validation ladder (the proof-of-value path)

This is the closest thing to a roadmap, and the only place "what next" lives. Each level is a gate; do not claim a level until it is earned.

```text
L1  catches planted defects and spares clean controls
      → STATUS: achieved ONLY for one constructed-positive condition class, at
        FP16, single surface, single model family, single scale. Not multi-class.
L2  catches multiple defect classes
L3  works across several models (structure ports; thresholds re-justified)
L4  detects stable wrongness that naive retention would score as success
      AND reports it as NOT SAFE TO COMPARE
L5  separates format drift, content loss, abstention loss, criterion shift
L6  produces reports a third party can reproduce
L7  predicts/explains where compression changes behavior better than aggregate
    benchmarks  ← the honest forward edge; the qualification question
```

**Ladder progression condition:**

```text
A proposed ladder advance must show that the prior rung's invariants are not
just DOCUMENTED but OPERATIONALLY ENFORCED in the mainline system. No L_n action
is authorized while L_(n-1) invariants are merely written down and not active.
```

The forward edge (L7) is the real prize and the program's stated open question: **does retention under stress predict deployment reliability better than peak accuracy?** That is the question that would make this a tool the field needs, not just a tool we trust.

---

## 9. When NOT to test — route control and the EXIT rule

The clearest expression of the value proposition (§4) is the tool's ability to refuse. The route-control rules:

```text
- The mini-map EXIT rule:  F EMPTY overrides D and E → DO NOT DRIVE YET.
  (If the surface is saturated — no resolvable room below ceiling — then no
  matter how well the premise (D) holds or how feasible the design (E) is, a
  retention reading is uninterpretable. Saturation wins; do not run.)
- Route-state must be unambiguous before execution. A run launched during a
  routing pause is procedurally nonconforming (see INT8-RUNG-1).
- The refusal definition (§4b) governs what counts as a real "do not test."
```

---

## 10. The standing reminders (the discipline that makes the above possible)

```text
- Fail closed. An instrument must demonstrate clean baselines before stress
  results are load-bearing.
- Architect broad, execute narrow, productize later.
- Gate structure is portable; threshold values are not, until independently
  justified.
- Verify bytes, read the artifact, do not reconstruct from memory and call it
  a reading. (The program has caught itself doing exactly this; it is the named
  irony, and the standard exists because the failure is easy.)
- A negative result is a result of record. "The certification window, while
  logically nonempty, was unoccupied for this task family at this scale" is a
  finding, not a failure.
- Happy but not satisfied. The correct posture: real progress, no resting on it.
```

---

## 11. The short version (for when even this document is too long)

```text
Build a ruler that is:
  valid (measures a real, named construct, metaphor removed and reviewer-confirmed),
  reproducible (a stranger gets the same answer),
  portable across models (structure ports; thresholds re-earned),
  cheap enough to run (automation prepares gates; humans open them),
  strict enough to prevent false claims (it can say "not safe to compare"),
  and useful enough that someone else would trust it.

The next phase is designed around "what must be true for this to be a real
measurement tool?" — never around "what can we run next?"

And the deepest cut: a tool whose REFUSALS can be trusted is worth more than a
tool that always produces a number. Guard the refusals. They are the product.

And its complement, equally load-bearing: a tool whose refusals NEVER lead to
valid measurement is not yet a usable measurement tool. Refusals are the product
only if measurement eventually happens behind them. Governance must be
accountable to measurement, not a substitute for it.
```

---

## 12. Productization tiers (honestly scoped)

```text
TIER 1 — eval-validity auditing.
  "Was your construct valid / your baseline certified / your apparent retention
   real?" Tier 1 is the NEAREST-TERM DEFENSIBLE OFFERING today, within
   demonstrated task families and with explicit scope limits.
     - Tier 1 MAY cite Papers 1–3 and the Hash Integrity / semantic-read work.
     - Tier 1 MAY NOT cite INT8-RUNG-1 as official stress evidence.
TIER 2 — stress-retention measurement.
  "What does your model retain under compression?" Larger market.
     - NOT OFFERED, even informally, until a certified-baseline compression rung
       exists in the official NON-QUARANTINED sequence.
TIER 3 — the qualification metric as a product.
  "Does retention predict reliability?" Pending L7. The biggest prize, the
  furthest out, claim only when the evidence exists.
```

Tier discipline mirrors claim discipline: offer only what the current rung of the ladder supports.

---

## 13. The INT8-RUNG-1 datum (canonical handling, for reference)

```text
Classification (verbatim): INT8-RUNG-1 (QUARANTINED): scientifically retainable,
  procedurally nonconforming, pending governance reconciliation.
Permitted framing (canonical): "Under one nonconforming INT8 run on a single
  constructed-positive surface, the active criterion re-eliminated the defective
  member via the same criterion identity, with byte-identical clean output;
  defective outputs were not byte-stable. No generality, sensitivity, ladder,
  certification, or Claim C inference is drawn."
On reconciliation: completion of route reconciliation clears the PROCEDURAL bar
  ONLY. The quarantined INT8-RUNG-1 datum is NOT itself promotable to official
  first-rung status. Official first-rung evidence requires a conforming,
  authorized run.
CP-DEF-018 label (direction-neutral): local defective-member output drift /
  abstention-form drift-or-instability watch item. (NOT established degradation.)
```

---

## Appendix A — Change log

```text
v1.0  2026-06-13 / source: founding strategic analysis ("what must be true")
      / purpose: first North Star; established-vs-aspirational framing,
        ten questions, anti-goals, validation ladder, tiers.
v1.1  2026-06-13 / feedback-integrated revision (Manager direction): bound
      semantic-read to the nine-field form + rendering floor + byte anchors + owner signature;
      added Result status + expanded use-recommendation enum; scoped Tier 1
      precisely and barred Tier 2 until a non-quarantined certified rung; added
      the F-EMPTY EXIT rule; operationalized No-Mountain (author/reviewer
      two-step) and the governing rule (construct + minimum-evidence or HOLD);
      made refusals countable; added §3a governance-state; strengthened
      anti-goals (nonconforming-as-milestone); added automation limits; added
      ladder progression condition; precision edits to Layer-2/L1/L4; refined
      INT8 + CP-DEF-018 language; added this change log. [v1.1 maintenance edit: added the complementary control — refusals must lead to valid measurement; governance accountable to measurement — in §4 and §11, paired with the Program Stage Map proof-of-life criteria.]
v1.2  2026-06-14 / refinement (Manager-delegated to Senior; C5 claim-risk review
      integrated): §2 domain sentence "bit-depth stress" -> "numerical stress";
      added the "stressor is a basis, not a dial" paragraph (quantization as a
      family of distinct structural probes; failure as a coordinate not a verdict;
      the seam as a cross-method PROFILE / components-vs-composition difference,
      not a single cliff). Per C5 review, three claim-risk points bound into the
      prose: a cross-method pattern is a structural HYPOTHESIS, evidence only after
      confounds are ruled out per rung (not "structural evidence"); methods are
      entangled bundles not clean scalpels, so a profile localizes representation
      only insofar as other method differences are matched; the components-vs-
      composition differential is guarded against "the harder task degrades first"
      via load-matching. Added the negative-use guardrail: the frame is a question,
      not a warrant — no sweep cites it as authorization, no per-method result
      cites it to upgrade coordinate->structure. Full framing retained as the
      companion note WHAT-KIND-OF-SMOOTHING-v0.2 (Manager: keep BOTH — North Star
      references it; standalone retained as the long-form); this paragraph is its
      compression. No claim, no authorization, no gate change; all of §0-§11 and
      the ladder otherwise verbatim from v1.1.
Maintenance: supersede by versioned replacement only. No silent edits.
  Owner: Manager. Review cadence: quarterly or upon ladder advancement.
```

---

*Maintained as the program's North Star. When the path is unclear, this is the document to re-read first. It records the standard; the lanes, ledgers, and routings record the work. Keep them distinct — and keep the claims no larger than the evidence earns.*
