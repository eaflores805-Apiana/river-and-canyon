# Speculative Companion — Failure Modes Under Pressure

*A quarantined note, and a record of its own pressure test — now five independent tests plus the in-house one. It began as a broad "groove-defect" taxonomy: the claim that learned capabilities are likely defect-bearing in seven distinguishable ways. Tested hard, most of it did not survive. The honest headline, after the full series: the taxonomy is dead, and what remains is **one contribution and one borrowed test-target.** The contribution is a warning — retention measures survival, not correctness, so a stable-but-wrong capability can pass a retention test while remaining wrong. The test-target is a falsifiable prediction — failures concentrate at compositional / out-of-distribution boundaries — which is worth testing but which the field already owns (compositional-generalization gap, shortcut learning), so it is not this work's to claim. The sections below record how the taxonomy broke and how the survivor count narrowed from seven, to two, to one-and-a-half, across six independent attacks. Smaller than it started, and stronger, because what is left can be killed and most of it has been.*

---

## Status

- Speculative note, not part of the rigorous papers, not a framework.
- The broad defect taxonomy **did not survive its own pressure test.** This note records what broke and what held.
- Pre-data: the surviving claims are Tier 1 follow-ups, testable but untested. Each is stated with a falsification path so a result can end it.

## What broke, and why

The original prior — *learned capabilities are likely defect-bearing: incomplete, discontinuous, mistrained, entangled, brittle, plumbing-dependent* — failed under three attacks:

1. **The process analogy points the wrong way.** The motivating intuition (messy training conditions → messy structure, like defects in crystal growth) predicts the wrong sign. Crystal defects form because growth is *local* and cannot see global structure. Training is the opposite: SGD over massive data optimizes against a loss computed over the *whole* distribution — it *averages*, amplifying what is consistent and attenuating the idiosyncratic. So the grounded prediction is that training *smooths toward* redundant, defect-tolerant structure, not toward defects. The analogy undercut the claim rather than supporting it.

2. **The categories are not cleanly separable.** A stable failure at step 4 could mean the model never learned step 4 (*incomplete*), learned a wrong step 4 (*mistrained*), or cannot pass state into step 4 (*discontinuous*). Same observed behavior, three stories. Behaviorally, "missing" and "wrong" are indistinguishable — both produce a consistent wrong output. A taxonomy whose categories collapse into the same observation has no diagnostic power.

3. **"Defects of some kind are likely" is unfalsifiable.** Model fails → confirmed. Model succeeds → "defect not triggered." Results messy → "defects entangled." No observation could end it. A claim that survives every outcome predicts nothing, and the careful hedges ("form unknown," "may not resemble defects as we know them") drained content rather than adding honesty.

So the seven-defect taxonomy is retired as a diagnostic framework. The terms (imperfect, incomplete, entangled, plumbing-dependent, brittle crossing) remain useful vocabulary *only if each is separately operationalized* — not as a taxonomy.

## Survivor 1 — Compositional and out-of-distribution boundaries

The smoothing objection (Attack 1) does not actually oppose the defect prior; it *partitions* with it. Averaging cleans up structure **on the training distribution** — it says nothing about regions the data underconstrains: composition of subskills, length-generalization, novel combination. Those are out-of-distribution in the relevant sense, exactly where averaging never had data to smooth. So the prior, corrected, sharpens:

> **Failures are most likely at compositional and out-of-distribution boundaries — where training data underconstrains the connection between otherwise competent subskills.**

**Test.** Subskill A works in isolation; subskill B works in isolation; measure A→B against a matched non-compositional control of equal difficulty. The prediction is that the compositional task shows a retention/accuracy gap *beyond* what step-independence predicts, and larger than the control's.

**Falsification.** If chained performance tracks isolated-skill performance (chained ≈ what independence predicts), or if the compositional gap is no larger than the matched control's, the claim weakens or dies. It can bleed — which is why it is worth keeping.

This is the survivor that gives "discontinuous" a real role: not one of seven equals, but the single flagship case, because composition is the one boundary that is cleanly separable from non-composition.

## Survivor 2 — Retention measures survival, not correctness (the keeper)

This survives every attack because it is **analytic, not empirical** — true by the definition of the metric. Retention is (score under stress) / (score at baseline). If the baseline answer is already wrong, a retention of 1.0 means the model *perfectly retained a wrong answer*.

> **A robustly-wrong capability — a stable shortcut that survives quantization, paraphrase, and perturbation while remaining incorrect — is invisible to a retention-only metric. Retention certifies stability, not truth.**

**Test.** Build counterexample tasks where a common shortcut gives the wrong answer; quantize and paraphrase aggressively; measure whether the *wrong* answer stays stable. A stable wrong answer across all stresses is a robustly-wrong capability.

**Why it matters.** This is a structural blind spot in the entire fragility/retention program, not a quirk. A fragile-correct capability fails loudly — you see it break, you fix it. A robust-wrong capability passes every stress test and is still wrong, and the only defense is *knowing to look for it at all*, because the instrument cannot see it. It is exactly what benchmark overfitting and reward-on-final-answer-only training produce. Naming it is a genuine contribution regardless of whether anything else here holds, because it marks the edge of what the measurement can certify.

## The replacement thesis

> The original grain-defect taxonomy was too broad. Under pressure it narrows to two claims. First, failures should be most likely at compositional and out-of-distribution boundaries, where training data underconstrains the connection between otherwise competent subskills — testable as a chained-vs-isolated gap beyond independence, against a matched control. Second, retention measures survival, not correctness; a robustly-wrong shortcut can retain under stress and remain invisible to a retention-only metric. These two replace the broader taxonomy until data justifies more categories.

*Smaller than the original, and stronger — because it can be killed. The gate is unchanged: no further category re-enters without its own behavioral signature, measurement, and falsification path. And the next real input is data, not another pass.*

---

## In-house pressure test (the baseline) — five attacks

This is the original in-house test, recorded in full as a peer to the independent ones rather than only referenced. It ran five attacks; the "What broke" section above is its first three landed hits, restated here with the two that did not fully land, and with an honest note on where it was *weaker* than the independent tests that followed.

- **Attack 1 — process-analogy direction (LANDED).** The crystal/defect intuition predicts the wrong sign: SGD averages over the whole distribution, smoothing toward clean structure, so defects should be the exception, not the default. Killed the motivating prior. (This attack later reappeared independently as test #1's causal-direction test and test #2's Test 1 — three-way convergence on the same kill.)
- **Attack 2 — non-separability (LANDED).** The three "new" categories collapse behaviorally: a stable wrong output at step 4 is consistent with incomplete, mistrained, *or* discontinuous. Killed the taxonomy as a diagnostic framework.
- **Attack 3 — unfalsifiability (LANDED).** "Defects are likely" survives every outcome, so predicts nothing. Killed the broad prior; spared only the two narrow, killable versions.
- **Attack 4 — direct assault on the survivors (PARTIAL).** Tried to kill the two survivors. Result: the compositional claim survived by *partitioning* with the smoothing objection (averaging cleans in-distribution structure; defects live at the under-constrained seams), and the retention-blind-spot survived because it is analytic, not empirical. This is where the survivor count settled at two.
- **Attack 5 — "so what" / does it change the intervention (PARTIAL, and weaker than the independent version).** Asked whether the diagnosis matters. The in-house test answered this incompletely; independent test #1 answered it better (discontinuous → train compositions not examples; mistrained → check correctness not just survival), and independent test #2 answered it *against* the idea more sharply (most fixes reduce to "add targeted data," so only mistrained truly diverges).

**Where the in-house test was weaker than the independents (recorded honestly):** it missed two hits the harder independent tests landed. It did **not** ask whether the defect label adds predictive variance beyond provenance + fragility — test #2 did, and the answer (no) is a real strike the baseline missed. And it did **not** find the calibration-contamination confound or the activation-outlier-vs-composition confound — test #3 did, and those produced the two genuine protocol hardenings. So the in-house test killed the taxonomy correctly but was *less thorough on the survivors and the instrument* than the independent assault that followed. The baseline established the two survivors; the independent tests stress-tested them harder than the baseline had, which is exactly what independent replication is for.

**In-house verdict:** taxonomy dead (three landed attacks); two survivors established (compositional-boundary, retention-blind-spot); survivor-novelty and instrument-confounds left under-examined — gaps the independent tests then closed.

---

## Independent pressure test #1 — tally against the in-house result

An independent analytic pressure test (a fresh seven-test battery — non-analogical translation, unique prediction, falsification, diagnostic usefulness, redundancy, Tier 0 compatibility, hard counterexample — not a rerun of the in-house five attacks) was run against the same claim. Recorded here and tallied, because an independent *kill attempt* that converges by a different route is stronger evidence than agreement among passes that shared context.

**Where it converged with the in-house result (the substance):**
- **Killed the same thing.** Taxonomy retired; "defects are likely" rejected; four of seven (imperfect, incomplete, entangled, brittle, plumbing — minus the two) flagged as already-covered or too generic — "old ideas with canyon hats." Same kill, reached independently.
- **Spared the same two.** Compositional/OOD boundary and retention-blind-spot survived its battery exactly as they survived the in-house one. No third survivor; no survivor fell.
- **Independently reached the analytic/empirical split.** It classifies the retention point as "a measurement theorem / limitation — survival and correctness are different quantities," which is the in-house note's "analytic, not empirical" by another name. Two independent tests agreeing that one survivor is *analytic* (certain) and the other *empirical* (falsifiable, killable) is the strongest form of convergence available here.

**What it added that the in-house test did not:**
- A cleaner **diagnostic-usefulness** axis: discontinuous changes training from "more examples" → "composition/handoff examples"; mistrained changes evaluation from "does it survive?" → "is what survived correct?" This answers the in-house Attack 5 ("so what — does the diagnosis change the intervention?") more completely than the in-house test did: for these two, yes, and differently from each other.

**Where it disagreed with the in-house result (recorded, not papered over):**
- **Tier 0 placement of the correctness check.** This test (Test 6) says the core protocol is *unchanged* — the retention-vs-correctness warning belongs as a limitation / future requirement, not a Tier 0 change. The in-house follow-up had added the correctness check *into* Tier 0 as an instrument-guard. **Resolution:** the test is partly right. Tier 0's raw measurement (the ΔR comparison) genuinely does not *require* correctness data to produce a number. But *interpreting* a high retention safely does — a robustly-wrong narrow task inflates retention and contaminates the read. So the honest placement is between the two positions: the correctness check is a **required interpretation guard, not a required measurement input** — you can produce ΔR without it; you cannot read "high retention = robust" without it. The protocol's current wording (pair retention with a correctness check; state the limit in positioning) already sits at this resolution rather than at "Tier 0 fails without it," so no further protocol change follows from this disagreement — but the disagreement is logged, and the resolution is the narrower, correct one.

**Tally:** independent kill attempt, different battery, **same two survivors, no survivor fell, no new fatal attack, one placement disagreement resolved to a narrower position.** Convergence on the substance; one genuine refinement (the disagreement sharpened where the correctness check binds). This is the result a pressure test is supposed to produce when the surviving claims are real: a fresh adversary, attacking differently, lands in the same place.

---

## Independent pressure test #2 — the hardest, and it lands harder than the in-house test

A second independent test, run guilty-until-proven-useful: eight tests fixed *before* looking at the idea, scored blind. It is the harshest of the three, and it should be recorded as such — it fails more of the idea than the in-house five-attack test did, and it lands one attack the in-house test did not run. Recording where an independent test is *harder* than mine is the point of the exercise.

**Scorecard: 6 fails, 1 partial, 1 conditional.** Causal direction (FAIL — the smoothing argument, same as in-house Attack 1), empirical precedent (PARTIAL — two of three types exist in literature, "incomplete" does not), distinguishability (FAIL — the three collapse to two clusters), falsifiability (FAIL broad / PASS narrow), incremental predictive power (FAIL — provenance + fragility already predict where/how it breaks), intervention divergence (FAIL — all three fixes reduce to "add targeted data"), adversarial reinterpretation (FAIL — all three redescribe as ordinary underfitting/biased coverage), cost of being wrong (FAIL — adopting a false three-way classifier wastes measurement effort).

**Same two survivors, reached by a harsher route:** compositional-fragility hypothesis (falsifiable, mechanistically consistent with the smoothing argument) and retention ≠ correctness (true by definition, survives all eight). Identical to the in-house result and to independent test #1. Three independent kill attempts, three methods, same two survivors — this is now robust.

**Two attacks this test landed that the in-house test did not, and both are verified:**

1. **Test 5 — incremental predictive power (FAIL).** The in-house test never asked whether the defect label adds variance *beyond provenance + fragility*. This test did, and the answer is no: if you already know a capability's provenance and its fragility, calling it "discontinuous" predicts nothing new. This is a real hit the in-house test missed — the surviving compositional claim is valuable as a *search direction*, but it does not add an independent predictive variable on top of the two axes already in Paper 2.

2. **Test 2 + Test 7 — the survivors are largely the field's, not ours (VERIFIED against literature).** Searched to check: the **compositional generalization gap is an established, named phenomenon** (Hupkes et al. 2023; Dziri et al. 2024; "shattered compositionality," 2026) — it is specifically a training-coverage-at-compositional-seams effect, exactly the surviving claim's mechanism. **Shortcut learning / spurious correlation (the mistrained survivor) is equally established.** So the harsh verdict is correct and the verification sharpens it: *both* survivors describe phenomena the field already has names and benchmarks for. The contribution is not discovering them. At most it is (a) connecting compositional-gap to quantization-retention specifically, and (b) the framing that retention is blind to the established shortcut-learning failure. The phenomena are the field's; only the *measurement-side connection* is arguably ours — and even that is thin.

**The one place this test overreaches, flagged:** Test 7 ("adversarial reinterpretation — all three reduce to insufficient/biased coverage, no defect ontology needed") is correct *and* it is not actually a strike against the two survivors — it is a strike against the *defect-ontology framing*, which was already retired. "Compositional failure = insufficient A→B coverage" is not a refutation of the compositional hypothesis; it is the *mechanism* of it (the smoothing argument says exactly this). So Test 7 kills the ontology (already dead) and re-states the survivor's mechanism — it does not kill the survivor. Logged so the survivor is not double-counted as dead.

**Tally across all three pressure tests (in-house + two independent):**
- **Unanimous kill:** the three-type taxonomy, the "defects are likely" prior, and four-to-five of the named defects as renamings. Dead by every method.
- **Unanimous survival:** compositional-boundary hypothesis (falsifiable) and retention ≠ correctness (analytic). Survive all three, by three different batteries.
- **New from test #2, verified:** the two survivors add little *novel* — the phenomena are established (compositional gap, shortcut learning); the defect label adds no predictive variance beyond provenance + fragility. So the honest status of the survivors drops from "our two contributions" to **"one established phenomenon we connect to quantization-retention (compositional gap), and one largely-analytic warning about a known failure (shortcut learning) that retention is blind to."** Thinner than it looked two tests ago — which is what the hardest test is for.

**Net:** three independent adversaries converge on the same two survivors, and the harshest one establishes that even those two are mostly the field's, with our contribution narrowed to the measurement-side connections. The pressure test worked: it did not just kill the taxonomy, it correctly deflated the survivors to their true, smaller size.

---

## Independent pressure test #3 — the assault on the durable center (the hardest target, partially verified)

The third independent test turned the blades on the *core* — the inverse-problem framing and both survivors — rather than the dead taxonomy. It is the most technically aggressive, landing four mechanism-level attacks. Two of its mechanisms were verified against the literature before recording; the verdict below separates what genuinely lands from what the test asserts. It also does a move the record must flag: it *attacks, then reconstructs*, and presents the reconstruction ("hardened core," "new guard") as the test's output — the reconstruction is prosecuted here, not accepted.

**Attack 1 — "quantization measures cumulative softmax-entropy noise, not geometry" — VERIFIED, and it lands against the *narrative*, not the *measurement*.** The mechanism is real: there is a literature on quantization *error propagation* (arXiv 2504.09629 — error accumulates and grows across layers, prohibitive at low bit-depth), and removing outlier dimensions cuts top-1 softmax mass >20% and degrades perplexity 600–1000% (LLM.int8(), 2208.07339). So the attack correctly kills any claim that quantization is a literal camera of "loss-landscape geometry" or "groove depth." **But it does not touch the protocol's actual target**, which was never absolute decay — it is the *paired difference* ΔR between matched halves sharing source and context-depth. Layer-wise noise affects both arms; the matched control subtracts substrate noise. So Attack 1 kills a narrative the protocol had already abandoned (geometry-as-measured-fact, retired in the v0.1 papers) and leaves ΔR standing. **Lands against the aesthetic, not the instrument.**

**Attack 2 — "compositional failure is activation-outlier blowout (plumbing), not geometry" — MECHANISM VERIFIED, CAUSAL LINK TO COMPOSITION NOT.** Activation outliers are established as the main cause of quantization degradation, and LayerNorm amplifies them with depth (2306.11987; 2603.04308; Bondarenko 2021). So the *plumbing mechanism* is real. **But the test's specific claim — that *composition specifically* induces these outliers more than matched non-composition — is asserted, not established.** Nothing found shows chained tasks produce differential outlier blowout versus difficulty-matched controls. This is the test's own inference wearing verified-mechanism clothing — the same move flagged in test #2's Test 7 and in Set 4 of the ranking record. **Status: a real confound to control for, not a demonstrated kill.** And it has a direct test: the matched non-compositional control is difficulty-matched, so if the chained gap were pure outlier-blowout, the difficulty-matched control (which also stresses the residual stream) should show comparable blowout. The design already partially guards it; the attack sharpens the requirement that the control be matched on *generation length and state-maintenance load*, not just task difficulty.

**Attack 3 — "calibration data contaminates the result" — GENUINE, and the new guard it forces is real.** PTQ methods compute clipping thresholds from the calibration set, so a skewed calibration file distorts which pathways survive — the result could be measuring cross-entropy distance between eval task and calibration data, not intrinsic fragility. This is a real, unguarded vulnerability in the protocol as written. **The forced guard — the Cross-Calibration Sanity Check — is legitimate and is the one genuine protocol addition from this test:** run Tier 0 across two distinct calibration hashes (e.g. code-heavy vs. prose-heavy); the fragility ranking is validated only if it is *invariant* across both; if the ranking flips, discard as a calibration artifact. This is an instrument-guard by the protocol's own test (it closes a way the existing measurement is fooled), so it goes in.

**Attack 4 — "the instrument-limit claim is a suicide pact: a tool blind to robust-wrong can't be a safety gate" — does NOT land; it confuses scope with failure.** The attack is right that retention cannot certify a robust-wrong shortcut, but wrong that this defeats the framework. It defines the tool's *position*, not its worthlessness: Tier 0 retention qualifies a capability's *operational margin under load*; it does not *authenticate behavioral correctness* — those are different gates in a defense-in-depth model. The honest framing (already the note's Survivor 2): a model must pass an adversarial correctness suite to verify *direction*, then the retention ladder to qualify *margin*. Naming a blind spot is not a failure of the instrument; pretending it had no blind spot would be. **The instrument-limit claim hardens; it does not die.**

**The reconstruction, prosecuted (not accepted as given):** the test presents a "Hardened Metrology Core" with three outputs. Holding them to the same standard as their own attacks:
- **ΔR Pivot — accepted.** This is correct and was already the protocol's position (the paired-difference guard). The test re-derives it under fire, which strengthens it, but it is not new.
- **Cross-Calibration Guard — accepted and added.** Genuinely new, genuinely closes Attack 3, instrument-guard by the protocol's rule. Goes in.
- **"Deflective Safety Rule" (retention qualifies margin, not alignment) — accepted as framing, already present** as Survivor 2 plus the correctness-check column added earlier.

**Tally — test #3 vs. the in-house and prior independent tests:**
- It did **not** kill either survivor. ΔR survives Attacks 1–2 (matched-pair subtraction); the instrument-limit survives Attack 4 (scope, not failure).
- It landed **one genuine new guard** the prior tests missed: the **Cross-Calibration Sanity Check** (invariance across two calibration hashes). This is the most valuable single output of the whole pressure-test series — an unguarded fatal confound, now closed.
- It landed **one verified caution**: composition could be confounded by activation-outlier blowout, so the non-compositional control must match on generation length and state-maintenance load, not just difficulty.
- It **over-reached once** (Attack 2's composition→outlier causal link asserted as established; flagged) and **once dressed a retired-narrative kill as a core kill** (Attack 1 kills geometry-as-measured-fact, already abandoned).

**Net across all three independent tests + in-house:** the taxonomy is dead by every method; the two survivors hold against four independent batteries including a direct mechanism-level assault on the core; the survivors are confirmed to be mostly the field's phenomena (test #2) with our contribution narrowed to measurement-side connections; and the assault produced **one real protocol hardening** — the Cross-Calibration Guard — plus a sharpened control requirement for the compositional test. The durable center (ΔR + instrument-limit) survived the hardest attack aimed directly at it. That is the strongest evidence available, short of data, that the two survivors are real.

---

## Independent pressure test #4 — convergent, no new signal (logged briefly, by discipline)

A fourth independent test (five attacks: is-it-just-brittle, falsifiability, beyond-the-fragility-axis, operationalizability, placement-in-stack). It reaches **the same conclusions as tests #1–#3 and adds no new attack and no new survivor** — and it is *gentler* than tests #2 and #3, landing neither test #2's "no predictive variance beyond provenance + fragility" hit nor test #3's calibration/outlier confounds. Logged in one entry rather than at full length, deliberately: a fourth convergent-but-weaker pass is confirmation, not accumulating evidence, and writing it up as if it were new would inflate the record the way a soft-axis ranking pass inflates a ranking. Its verdict — taxonomy survives only as a quarantined hypothesis-generator, each defect earns status only via a distinct pre-registered signature, never geometry, never a third axis — is already the note's standing position.

**What it confirms (now five-way, counting the in-house test):** taxonomy dead as a framework; survives only as test-generating vocabulary under quarantine; not a literal-geometry claim; not an axis on par with provenance/fragility. Five independent batteries, same verdict.

**What it adds:** nothing to the record. One *prompt* worth naming and declining (below).

**The recurring prompt, and why it's declined tonight:** this test, like two before it, closes with "pick one defect (discontinuous or mistrouted) and sketch a tiny real protocol you could run." Three readers have now had this instinct, which is itself a signal the instinct is sound — *eventually*. But sketching a defect-specific protocol now would (a) restart the build-loop on a body of work whose own stop-rule says the next move is data, and (b) be premature: the compositional-seam test is a **Tier 1 follow-up, gated on Tier 0 returning Outcome A** — designing it before Tier 0 runs is drawing the Tier 1 map before the Tier 0 measurement exists, the exact "maps before measurements" error. The discontinuous/compositional protocol gets sketched *when there is a Tier 0 gap to follow up on*, not before. Until then it stays where it is: the surviving hypothesis, gated, awaiting the run.

**Standing tally — in-house + four independent pressure tests:**
- Taxonomy: dead by five methods.
- Two survivors (compositional-boundary hypothesis; retention ≠ correctness): held against all five, including a direct mechanism-level assault on the core (#3).
- Survivors confirmed mostly the field's, contribution narrowed to measurement-side connections (#2, verified).
- Protocol hardened by the process: correctness-check column (in-house follow-up), Cross-Calibration invariance gate and state-load-matched control (#3).
- Tests #1 and #4: convergent confirmation, no new signal.

The pressure-test series has reached saturation: new tests now confirm rather than move the result. By the same logic as the ranking record's stop-rule — convergence established, further passes of the same kind do not update it — **the next real input is data, not a fifth pressure test or a pre-data protocol sketch.**

---

## Independent pressure test #5 — the one that disagrees, and resolves a tension the others left open

A fifth independent test (six scored criteria; overall 4.7/10) — and unlike test #4, this one does **not** simply converge. It lands *harder* than the prior four and reaches a different count of survivors, which makes it the most useful one to record carefully. Where tests #1–#3 kept **two** survivors (compositional-boundary + retention-blind-spot), this test keeps essentially **one**: it preserves the retention-blind-spot as the only thing that "clearly survives hard pressure testing," and is openly skeptical of the compositional/discontinuous category — its scored verdict is that the discontinuous and incomplete distinctions are not sharply separable (4/10), add limited new experimental power (5/10), and mostly fragment the existing fragility axis without superior diagnostic gain (4.5/10).

**Is this a harder-correct read or a miss? Adjudicated: harder-correct, and it completes the prior logic rather than contradicting it.** The prior tests kept compositional-boundary because it is falsifiable and mechanistically grounded — which it is, and that does not change. But test #2 already established (verified against literature: Hupkes 2023, Dziri 2024, "shattered compositionality" 2026) that the compositional-generalization gap is an **established phenomenon, not this project's contribution.** This test draws the inference that follows from #2's finding: if the compositional claim is (a) the field's already and (b) adds no diagnostic variance beyond the existing precision-demand axis, then it survives *as a true statement* but not *as something this note contributes*. So tests #1–#3 and test #5 are reconciled, not in conflict:

- **Compositional-boundary:** true, falsifiable, mechanistically sound — **and the field's.** Survives as a correct prediction; does *not* survive as a contribution of this work. (Tests #1–#3 logged its truth; test #2 logged its non-novelty; test #5 draws the conclusion.)
- **Retention ≠ correctness:** survives as the one point that is both true *and* worth flagging as this note's distinct observation — because it is the one place the field's standard practice (retention/robustness evaluation) has a blind spot this framing names cleanly. Survives all five tests.

**The corrected status of the whole idea, after five tests:** the durable residue is **one clean warning, not a taxonomy and not two contributions.** Stated in this test's words, which are the tightest version in the record:

> Some learned capabilities form stable but incorrect structure. These can retain performance under stress while remaining wrong. Retention under stress is therefore not sufficient to certify that a behavior is correct.

Everything else — discontinuous, incomplete, entangled, brittle, plumbing-dependent — is either the field's (compositional gap, shortcut learning, salient-channel fragility) or too overlapping to function as a named diagnostic.

**Standing tally — in-house + five independent tests:**
- Taxonomy: dead by six methods.
- **Survivor count corrected from two to one-and-a-half.** The retention-blind-spot is the one durable *contribution* (true + names a real gap in standard practice). The compositional-boundary prediction is true and falsifiable but is the field's, not ours — it remains the sharpest thing to *test*, but not something this note can claim.
- Protocol hardening from the series stands regardless: correctness-check column, Cross-Calibration gate, state-load-matched control. Those are real improvements to the instrument independent of how the speculative note nets out.

**What this does to the note's framing:** the honest one-line summary of this entire companion is now: *the pressure-test series killed a taxonomy and left one warning — retention measures survival, not correctness — plus a falsifiable prediction (compositional seams) that is worth testing but belongs to the field, not to this work.* The note should not present itself as contributing a failure-mode framework. It contributes one warning and one well-aimed (borrowed) test target.

## The analogy as a measurement prior — what the literature confirms, and what it does not

The carving analogy did not reveal literal defects in model weights, and no claim here rests on internal geometry. What it did was generate behavioral expectations *before the project fully integrated the literature* — about where learned structure should be weakest — and those expectations later aligned with already-documented model failures. (Stated carefully: this is alignment-after-the-fact with existing literature, not a formally pre-registered prediction tested against fresh data. The distinction matters and the weaker phrasing is the honest one.)

The expectations that aligned: failures at **seams rather than centers** (compositional generalization gaps — Hupkes 2023, Dziri/Li 2024, "shattered compositionality" 2026); **shortcut routes rather than random error** (shortcut learning and spurious correlations — e.g. SDOH clinical-cue work, ACL 2025); **correlated rather than independent wrong answers** (large-scale error-correlation across 350+ models, arXiv 2506.07962, showing wrong routes can be systematic and shared); **cliffs rather than smooth degradation** (quantization-reasoning degradation up to 69.81% with early-step cascade — arXiv 2505.11574, though from a single unreplicated cluster, and the broader conditional-degradation picture across model families in arXiv 2504.04823). All field-owned phenomena, documented under their own names.

So the analogy's value is **a measurement prior, not a mechanism**: *look where training coverage is thin, where subskills must connect, where shortcuts can masquerade as capability, and where stress preserves behavior without validating it.* That is a useful search heuristic and it is the honest size of what the analogy earned. It is **not** a method this note contributes — generating a candidate, stripping the metaphor, checking the literature, and testing or killing it is ordinary careful inquiry, not a discovery, and is not claimed as one.

And the literature confirms the *phenomena*, which makes the two survivors **worth testing** — it does not confirm the framework's own two claims, which remain unrun: the matched-pair ΔR (does a precision-demanding task retain less than a matched-difficulty broad task under comparable scoring) and the retention-blind-spot *detection method* (do the correctness + error-identity columns actually catch a robust-wrong capability under stress). The field has shown the failures exist. Whether this protocol cleanly isolates and measures them is the unrun question. The hard rule stands: no internal-mechanism claim without a non-analogical workload, a falsification path, and evidence.
