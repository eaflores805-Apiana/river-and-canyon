# Neutral Diagnostic Addendum — Compositional Seam & Robust-Wrong Tests

*This addendum locks the skeptic-acceptable form of the two survivor questions from the pressure-test series. It does **not** modify Tier 0's primary hypothesis. It specifies how these two diagnostic claims must be tested **if** Tier 0 produces a meaningful retention signal, or **if** high-retention wrong behavior appears.*

---

## Architecture (so this stays in its box)

| Layer | Role |
|---|---|
| **Tier 0 core** | Broad vs. narrow retention under quantization. Untouched by this addendum. |
| Guardrail inside Tier 0 | Correctness column + error-identity (already in the protocol) |
| **This addendum** | The two survivor diagnostics, locked to a neutral method |
| Claim ledger | Prevents the analogy from becoming a mechanism claim |
| S5 | Records the taxonomy's death and the survivor questions |

**These two tests are Tier-1 diagnostics. They run only after Tier 0 returns Outcome A (a real, calibration-invariant retention gap) or surfaces robust-wrong flags. Running them before Tier 0 has signal is the map-before-measurement error.**

---

## The method standard (one bar, no range)

A design choice is admissible only if it meets this test:

> **Would a skeptic who thinks the carving analogy is nonsense accept this as a fair test?**

This has three hard consequences:

1. **The analogy gets no vote in methodology.** It may explain how a question was *discovered*. It may not *justify* the test. Every test below must stand on prior literature, non-analogical mechanism, the metric's definition, confound controls, and a falsification criterion — with the analogy stripped out entirely. If a design choice's only justification is "the analogy implies it," it is cut.

2. **The boring explanation is not an optional confound — it is constitutive.** Baseline difficulty, output length, state-load, context position, scorer strictness, calibration invariance, chance correction, the same-error definition, and shortcut-cue control are not "extra rigor that can be dialed down." Without them the result is **not interpretable** — not "less rigorous," uninterpretable, regardless of which way it comes out. The method is built to give the boring explanation every chance to win; an effect that survives that is worth something, an effect that doesn't was never there.

3. **The causal manipulation is mandatory, not a diagnostic bolt-on.** Each test includes the one intervention a confound cannot survive. A correlation gets stronger by adding controls; a causal test gets strong by including the manipulation the boring explanation can't fake. Those manipulations (below) are what make these questions answerable at all.

---

## Test 1 — Compositional seam

**Justification, analogy stripped:**
> Training data densely constrains common patterns more than rare compositions. Compositional-generalization failure is already documented (Hupkes 2023; Dziri/Li 2024; "shattered compositionality" 2026). The smoothing argument — SGD averages over the training distribution, leaving underconstrained regions where data is sparse — predicts composition as such a region. Therefore it is reasonable to test whether compositional tasks show distinct stress-retention behavior. No analogy is required for this justification, and it is the field's phenomenon, not this work's.

**The claim being tested:**
> Compositional A→B tasks show lower stress-retention than matched non-compositional controls under quantization.

**Constitutive controls (all required, or the result is uninterpretable):**
- Subskills A and B verified to **pass in isolation at every bit-depth** — otherwise "A→B fails" may just be "B was weak." This is a precondition, not an analysis step.
- Non-compositional control matched on **baseline difficulty, generation length, and state-load** — because a longer or harder control would lose retention for reasons unrelated to composition (activation-outlier accumulation, ordinary fragility).
- Context position matched (evidence at comparable locations).
- Scorer strictness identical across arms (the central confound).
- Calibration invariance: ranking holds across two calibration hashes.

**The mandatory causal manipulation — forced intermediate:**
> Run A→B with the correct intermediate state *supplied*. If free-chain A→B **fails** but forced-intermediate A→B **recovers**, the failure is the handoff — and no length or difficulty confound can produce this pattern, because a confound would break the forced version too. This single comparison is what makes Test 1 causal about the seam rather than correlational about "hard long things break."

**Falsification (any one kills the local claim):**
- Compositional retention ≈ control retention (gap absent), OR
- the gap dissolves under chance-correction / scoring-symmetry, OR
- the pair ranking flips across calibration sets, OR
- forced-intermediate does **not** recover the failure (then the problem is in A or B, not the seam).

**Scope of a null:** a null retires the seam hypothesis **for this model family / task family / stress configuration** — not globally. One null kills the local claim, not every possible version.

---

## Test 2 — Robust-wrong

**Justification, analogy stripped:**
> Retention is (score under stress)/(score at baseline) — a survival metric, not a correctness metric, true by definition. Shortcut learning and spurious correlation are documented (e.g. SDOH clinical-cue work, ACL 2025; large-scale error-correlation, 2506.07962). Therefore high retention must be checked against correctness and error identity. No analogy is required.

**The claim being tested:**
> Some adversarial/counterexample items show low baseline correctness but high same-error retention under stress — a robustly-wrong capability invisible to a retention-only metric.

**The under-specified piece that must be locked first — "same error":**
> "Same wrong answer" must be defined *before the run* and precisely enough that it cannot be fudged. Recommended: same final answer **and** same error category (pre-declared), not merely the same string. Too loose over-detects (labels noise as a shortcut); too strict misses shortcuts that surface slightly differently. Lock the definition, write it down, do not change it after seeing data.

**The mandatory causal manipulation — counterfactual edit:**
> A baseline-wrong, stress-stable answer is **not yet** a shortcut — it could be a deterministic model giving the same output to the same prompt (trivial). The discriminator: apply a **minimal shortcut-breaking edit**. If the edit **fixes** the answer, the error was riding the shortcut → real robust-wrong. If the edit changes nothing, it is just stably bad, not shortcut-driven. The edit is constitutive: without it, "robust-wrong" cannot be distinguished from "stably weak."

**A robust-wrong item is therefore defined as ALL three:**
1. wrong at baseline,
2. corrected by a minimal shortcut-breaking edit (proves shortcut-driven),
3. same error identity retained under stress.

**Falsification:**
- No item meets all three (then robust-wrong, while analytically possible, did not appear in this model/task set), OR
- the shortcut-breaking edit does not change the wrong answers (then they were stably weak, not shortcuts — the danger claim does not apply here).

**Note on the analytic core:** the *general* warning (retention ≠ correctness) is true by the metric's definition and does not need this test. Test 2 asks the narrower empirical question of whether robust-wrong behavior *appears in this model* — a null here does not refute the analytic point, only its appearance in this case.

---

## Recorded follow-on (not run here): the salient-weight rescue test (B13/B23)

If Tier 0 flags fragile items, the depth-vs-redundancy question — is a capability's fragility due to concentrated numerical dependence or distributed margin loss — has a cheap diagnostic, already recorded as B13/B23 in the implications index: protect the top-k most salient weights/channels, requantize, and re-run the *same* fragile items, logging recovery. **It runs only on Tier-0-flagged fragile items — it has nothing to rescue before Tier 0 identifies a fragility signal, so it waits for that output exactly as the rest of the diagnostics do.** Two cautions are constitutive, not optional: (1) it requires a salience estimate aligned to the weights (MLX's default quantization does not hand you one — you compute an activation-weighted proxy, and *that estimation is the load-bearing, error-prone step*, not the masking); (2) the result is **asymmetric** — a small mask rescuing a behavior suggests concentrated salient-weight dependence, but failure to rescue does **not** prove redundancy: the mask could be wrong, the calibration wrong, or the failure activation-side rather than weight-side. So it is a one-directional probe (it can confirm concentration; it cannot cleanly establish distribution), and any positive result is an *exploratory rescue pilot*, not a finding, until replicated.

---

## What this addendum deliberately does not do

- It does not modify Tier 0's broad-vs-narrow hypothesis.
- It does not build the factorial 2×2×2 extension — that is a later design, justified only if these diagnostics return signal.
- It does not let the analogy justify any target; every justification above is mechanism- or literature-based with the analogy removed.
- It does not offer a range of rigor. One bar: skeptic-acceptable, boring-explanation-favored, causal-manipulation-required.
- It does not build the rescue-test salience code, the MI handoff schema, twin-matching, or any dataset infrastructure — all post-Tier-0 artifacts that the data should shape.

The point of locking this now, before any run, is to remove the last methodological wiggle room — so that neither the experimenter nor the analogy can tilt the test after results arrive.
