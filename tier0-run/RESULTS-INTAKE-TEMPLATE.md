# Tier 0 — Results Intake Template

*The blank instrument. Every number the protocol produces has a labeled home here, so interpretation is mechanical, not improvised. Fill the cells when the run produces them; do not pre-fill, do not estimate. A cell with no measurement stays empty — an empty cell is honest, a guessed cell is not.*

**This template records measurement only.** It is the counterpart to the analysis in `notes/fragility-probe-protocol.md`. The analysis is complete; this is where the missing input goes.

---

## 0. Run header (fill once per run)

| Field | Value |
|---|---|
| Date | |
| Model (HF repo) | e.g. `Qwen/Qwen2.5-7B-Instruct` |
| Model size | |
| Quantization method | MLX `nn.quantize` (default) / other |
| Bit-depths swept | e.g. FP16, INT8, INT4 |
| Calibration set A (hash) | code-heavy — record file hash |
| Calibration set B (hash) | prose-heavy — record file hash |
| Scoring method | exact-match / key-fact checklist / constrained-choice |
| Pairs count | |
| Bootstrap iterations | e.g. 1000 |
| Hardware | e.g. M-series, 48GB |
| Pre-registered before run? (Y/N) | **must be Y for the result to count — see protocol** |

---

## 0b. Pre-registered predictions (LOCK THESE BEFORE RUNNING — date and do not edit after)

*This block exists to defeat the "too convenient" risk. Literature alignment after the fact is weak evidence; a prediction written down before the result is risked. Fill the date, commit this file, and do not change these statements once a run has started. A failed prediction recorded here is worth more than a successful one added later.*

**Date locked:** ________  **Committed (hash/Y):** ________

**Prediction 1 (the ΔR claim):**
> On matched task pairs, precision-demanding ("narrow") items will show lower stress-retention than matched robustness-tolerant ("broad") controls — i.e. ΔR = R_broad − R_narrow > 0 with a bootstrap CI excluding zero — *after* controlling for baseline accuracy, output length, state-load, and calibration set, and *invariant* across both calibration hashes.

**Kill condition for P1:** ΔR interval includes zero, OR the gap dissolves under chance-correction / scoring-symmetry check, OR the pair ranking flips across calibration sets. Any of these = P1 did not survive. Record it as such.

**Prediction 2 (the retention-blind-spot claim):**
> At least some counterexample items will show *high same-error retention* under quantization (the same wrong answer at FP16 and INT4) despite failing the counterexample at baseline — demonstrating a robustly-wrong capability that a retention-only metric would score as strong.

**Kill condition for P2:** no item shows stable same-error retention — every wrong answer either corrects under stress or becomes random/incoherent. That would mean robust-wrong, while analytically possible, did not appear in this model/task set. Record it.

**What each outcome means (decided in advance, so the result can't be rationalized after):**
- P1 holds, P2 holds → both framework claims survived first contact with measurement on this model. Pilot, not proof; plan the second model size.
- P1 flat, P2 holds → the matched-pair retention gap did not appear, but the blind-spot is real and observed. Honest, publishable, and *narrows the contribution to exactly the analytic survivor.*
- P1 holds, P2 absent → fragility gap real here; robust-wrong not exhibited by this model/tasks (does not refute the analytic point, only its appearance here).
- Both absent/flat → under matched, symmetric, calibration-invariant conditions, neither framework-specific claim showed up. This is a real result and the correct thing to report. The analogy generated useful questions; this model's data answered them "no." That is the system working, not failing.

**On effect-size thresholds — set them, but justify them.** The predictions above commit to *direction* and *kill condition*; they deliberately do not yet hardcode a magnitude, because a fabricated precise threshold ("ΔR ≥ 0.1", "≥5% of items", "retention > 0.9") is worse than an honest directional one — it dresses a guess as a calibrated prediction. Before locking, set a *minimum meaningful effect size* from one of: a tiny pilot (run 5 pairs, observe the noise floor, set the threshold above it), a power consideration for your N, or an explicit "smallest gap a deployment team would care about" judgment. Write down *which* basis you used. Illustrative placeholders, NOT yet justified: a mean retention gap around 0.1 under INT4, or on the order of 5% of adversarial items showing <40% baseline with >0.9 same-error retention — these are reasonable starting guesses to calibrate against a pilot, not thresholds to adopt as-is. Note also: for a small pilot, the bootstrap CI excluding zero is the primary test; a reflexive p < 0.05 is secondary and can mislead at small N (the protocol says this explicitly).

---

## 1. Core Tier 0 table — the ΔR measurement

*One block per calibration hash. The headline result is ΔR = R_broad − R_narrow at each bit-depth, with a bootstrap CI. Prediction: ΔR > 0 with interval excluding zero. Interval overlapping zero = flat, not weak.*

### Calibration A (code-heavy)

| Pair ID | Arm | Baseline score (FP16) | INT8 score | INT4 score | R (INT8) | R (INT4) | R_chance-corrected (INT4) | Counterexample survives? | Error identity (same-wrong / random) | State-load matched? (Y/N) |
|---|---|---|---|---|---|---|---|---|---|---|
| P01 | narrow | | | | | | | | | |
| P01 | broad | | | | | | | | | |
| P02 | narrow | | | | | | | | | |
| P02 | broad | | | | | | | | | |
| … | | | | | | | | | | |

**ΔR summary (Calibration A):**

| Bit-depth | mean R_broad | mean R_narrow | ΔR | bootstrap 95% CI | Outcome (A / B / C / flat) |
|---|---|---|---|---|---|
| INT8 | | | | | |
| INT4 | | | | | |

### Calibration B (prose-heavy)

| Pair ID | Arm | Baseline score (FP16) | INT8 score | INT4 score | R (INT8) | R (INT4) | R_chance-corrected (INT4) | Counterexample survives? | Error identity | State-load matched? |
|---|---|---|---|---|---|---|---|---|---|---|
| P01 | narrow | | | | | | | | | |
| … | | | | | | | | | | |

**ΔR summary (Calibration B):** *(same structure)*

### Cross-calibration invariance gate (REQUIRED)

| | Calibration A | Calibration B | Ranking invariant? (Y/N) |
|---|---|---|---|
| Rank order of pairs by ΔR(INT4) | | | |

> **Validation rule:** the fragility signature counts only if the retention *ranking* of pairs is invariant across A and B. If the ranking flips, discard as a calibration artifact — do not report as fragility.

---

## 2. Outcome classification (per pair, per bit-depth)

Fill from the joint read of baseline-correctness × retention × error-identity:

| Outcome | Definition | Count |
|---|---|---|
| **A — real fragility** | baseline correct, retention drops on narrow more than broad, ΔR>0 CI excludes zero | |
| **B — metric-cliff artifact** | gap dissolves under chance-correction or scoring symmetry check | |
| **C — pair/task confound** | gap traced to difficulty/length/state-load mismatch, not precision | |
| **flat** | ΔR interval overlaps zero | |
| **robust-wrong flag** | baseline WRONG, high retention, same wrong answer under stress — the dangerous cell | |

> Tier 1 diagnostics run **only if Outcome A**. If B/C/flat, fix Tier 0 first — there is no signal to diagnose.

---

## 3. Diagnostic sub-table — Seam test (forced-intermediate rescue)

*Run only on pairs flagged as compositional. The clean split: if forcing the intermediate state restores accuracy, the failure is the handoff, not A or B.*

| Pair ID | A-only | B-only (state supplied) | A→B free chain | A→B forced intermediate | Interpretation |
|---|---|---|---|---|---|
| | high? | high? | low? | recovered? | handoff weakness if last col recovers |

> If A→B forced-intermediate **recovers** while free-chain **fails**: evidence for a handoff/seam failure (the survivor's compositional prediction). If forced-intermediate does *not* recover, the problem is in A or B, not the seam.

---

## 4. Diagnostic sub-table — Robust-wrong test (counterfactual edit + same-error retention)

*Run on counterexample items. Two questions: is the wrong answer a shortcut, and does the shortcut survive stress?*

| Item ID | Original counterexample | Minimal shortcut-breaking edit | INT4 original | Paraphrased original | Interpretation |
|---|---|---|---|---|---|
| | wrong shortcut? | correct/different? | same wrong? | same wrong? | robust-wrong if edit fixes it AND stress preserves it |

> Same wrong answer on original + INT4 + paraphrase, but **corrected by a minimal shortcut-breaking edit** = a preserved specific wrong route (robust-wrong). This is the cell retention alone cannot see — the S5 keeper.

---

## 5. Error-source ledger (optional, builds over many tasks)

*Not a defect taxonomy. Effect → intervention that moved it → cautious source → evidence strength. Over many rows, real structure may emerge statistically. Until then, each row is one cautious measurement statement, never a defect-type claim.*

| Task | Effect observed | Probe / intervention that changed it | Plausible source (cautious) | Evidence strength |
|---|---|---|---|---|
| | | | | low / med / high |

> Rule: **no internal-mechanism claim without a non-analogical workload, a falsification path, and evidence.** "Failure correlates with activation outlier spike near the transition" = data. "The defect is at the layer-18 handoff" = metaphor in a lab coat. Record the first kind only.

---

## What a filled version of this means

- **Outcome A across both calibrations, invariant ranking** → the matched-pair fragility signal is real for this model/size. *Then* Tier 1 (the diagnostics in §3–§4) earns the right to run.
- **Robust-wrong flags present** → the retention-blind-spot is not just analytic but observed here — the one contribution, demonstrated.
- **flat / B / C** → the apparent effect dissolved. This is a real, publishable result too: "under matched, scoring-symmetric, calibration-invariant conditions, the precision-demand retention gap did not appear." Reality is allowed to say no.

The point of this template is that *any* of those outcomes is a result. The only non-result is not running.
