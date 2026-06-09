# Tier 0 — Results Intake Template

*The blank instrument. Every number the protocol produces has a labeled home here, so interpretation is mechanical, not improvised. Fill the cells when the run produces them; do not pre-fill, do not estimate. A cell with no measurement stays empty — an empty cell is honest, a guessed cell is not.*

**This template records measurement only.** It is the counterpart to the analysis in `notes/fragility-probe-protocol.md`. The analysis is complete; this is where the missing input goes.

---

# RESULTS INTAKE — Tier 0C Calibration-Invariant Local Null

*Filled: 2026-06-06. Results files: `results_code_1780740617.json`, `results_prose_1780741032.json`.*

---

## 0. Run header

| Field | Value |
|---|---|
| Date | 2026-06-06 |
| Model (HF repo) | `Qwen/Qwen2.5-7B-Instruct` |
| Model size | 7B |
| Quantization method | MLX `quantize_model` in-place (group_size=64); INT4 loaded from `mlx-community/Qwen2.5-7B-Instruct-4bit` |
| Bit-depths swept | FP16, INT8, INT4 |
| Calibration set A label | `code` |
| Calibration set B label | `prose` |
| Scoring method | exact-match (narrow); key-fact checklist (broad); exact-match (component checks) |
| Total pairs in tasks.py | 18 |
| Eligible pairs for ΔR | 17 (P01R excluded: FP16 narrow baseline = 0, capability floor not compression) |
| Bootstrap iterations | 1000, seed=0 |
| Hardware | Apple Silicon (MLX, macOS 15+) |
| Decoding | temperature=0.0 (greedy, deterministic) |
| Max tokens | 512 |
| Pre-registered before run? | **Y** — `PREREGISTRATION-SMOKE-SWEEP.md` locked before Tier 0A; `PREREGISTRATION-TIER0B.md` locked before Tier 0B; tasks.py locked before baseline check |

---

## 0b. Pre-registered predictions

**Date locked:** 2026-06-06 (smoke sweep locked earlier; ladder pairs locked before FP16 baseline check)

**Prediction 1 (the ΔR claim):**
> On matched task pairs, precision-demanding ("narrow") items will show lower stress-retention than matched robustness-tolerant ("broad") controls — i.e. ΔR = R_broad − R_narrow > 0 with a bootstrap CI excluding zero — *after* controlling for baseline accuracy, output length, state-load, and calibration set, and *invariant* across both calibration sets.

**Kill condition for P1:** ΔR interval includes zero, OR ranking flips across calibration sets.

**Result:** P1 did not survive. ΔR intervals include zero at both rungs under both calibrations. Ranking invariant across calibrations (both flat, no ranking to flip).

**Prediction 2 (the retention-blind-spot claim):**
> At least some counterexample items will show high same-error retention under quantization.

**Result:** P2 did not appear. No robust-wrong flags on this task family with the 7B model. (P06 showed stable-wrong on the 1.5B in Tier 0B, but shortcut causality was not fully established — broad arm also failed at FP16 on 1.5B.)

**Joint outcome:** Both absent/flat → under matched, symmetric, calibration-invariant conditions, neither framework-specific claim appeared. This is the correct thing to report.

---

## 1. Core Tier 0 table — the ΔR measurement

### Calibration A (label: code) — `results_code_1780740617.json`

**ΔR summary:**

| Bit-depth | mean R_broad | mean R_narrow | ΔR | bootstrap 95% CI | Outcome |
|---|---|---|---|---|---|
| INT8 | 0.9815 | 1.0000 | −0.0196 | [−0.059, 0.0] | flat |
| INT4 | 1.0000 | 1.0000 | 0.0000 | [0.0, 0.0] | flat |

n_pairs_used: 17 (P01R excluded, NaN baseline on narrow arm)

**Notable pair-level movements (code, not composite degradation):**
- LB1/broad: 0.67 at all rungs (checklist artifact — 2-fact answer omits "gate b"; stable, not degradation)
- LC1/broad: 0.67 at all rungs (same cause as LB1)
- LD3/broad: 1.0 @ 16b → 0.67 @ 8b → 1.0 @ 4b (non-monotonic; 8b checklist misses one required fact; drives the −0.0196 ΔR at INT8)
- LD4/comp_0[hira_tag]: 1.0 @ 16b → 0.0 @ 8b → 1.0 @ 4b (non-monotonic component blip; does not surface at composite level)
- LC2/comp_3[file_code]: 1.0 @ 16b → 1.0 @ 8b → 0.0 @ 4b (monotonic component degradation; composite LC2/narrow stays 1.0 at all rungs)

### Calibration B (label: prose) — `results_prose_1780741032.json`

**ΔR summary:**

| Bit-depth | mean R_broad | mean R_narrow | ΔR | bootstrap 95% CI | Outcome |
|---|---|---|---|---|---|
| INT8 | 0.9815 | 1.0000 | −0.0196 | [−0.059, 0.0] | flat |
| INT4 | 1.0000 | 1.0000 | 0.0000 | [0.0, 0.0] | flat |

**Identical to Calibration A** — every pair-level score, every component score, and every ΔR value matched exactly. Runs are deterministic (temp=0, same quantization weights).

### Cross-calibration invariance gate

| | Calibration A (code) | Calibration B (prose) | Invariant? |
|---|---|---|---|
| INT8 ΔR | −0.0196, CI [−0.059, 0.0] | −0.0196, CI [−0.059, 0.0] | **Y** |
| INT4 ΔR | 0.0000, CI [0.0, 0.0] | 0.0000, CI [0.0, 0.0] | **Y** |
| Pair-level ranking | all flat | all flat | **Y** |
| Component noise pattern | LD3/broad@8b=0.67, LD4/hira_tag@8b=0.0, LC2/file_code@4b=0.0 | identical | **Y** |

**Calibration-invariance gate: PASSED.**

No calibration artifact observed. The flat result holds across both calibration labels with no ranking reversal, no magnitude change, and no pair-level divergence.

---

## 2. Outcome classification

| Outcome | Definition | Count |
|---|---|---|
| **A — real fragility** | baseline correct, retention drops on narrow more than broad, ΔR>0 CI excludes zero | 0 |
| **B — metric-cliff artifact** | gap dissolves under chance-correction or scoring symmetry check | 0 |
| **C — pair/task confound** | gap traced to difficulty/length/state-load mismatch | 0 |
| **flat** | ΔR interval overlaps zero | 17/17 |
| **robust-wrong flag** | baseline wrong, high retention, same wrong answer under stress | 0 |

**Final outcome: Outcome C — task ceiling / calibration-invariant local null.**

Interpretation: the task family did not enter the 7B model's fragility band under the tested stress profile. Every narrow/compositional arm remained correct at FP16, INT8, and INT4. The only aggregate movement was a small negative ΔR at INT8 caused by broad-arm degradation (not narrow-arm degradation), which recovered at INT4.

This is not evidence against the global connection/continuity hypothesis. It is a local null for this model, task family, bit-depth ladder, quantization setup, and calibration pair.

> **This task family did not enter the 7B model's fragility band under the tested stress profile.**

---

## 3. Diagnostic sub-table — Seam test

Not run. Tier 1 diagnostics require Outcome A. No pair produced composite degradation with components preserved at any rung. The seam test precondition was not met.

**Exception noted for the record:**

LC2/file_code showed monotonic component degradation at INT4 (1.0 → 1.0 → 0.0) while the LC2/narrow composite arm stayed correct at all rungs. This is the inverse of the seam pattern (component fails, composite holds). It is a diagnostic observation, not a seam signal.

**Classification: single component-level degradation; no composite-level retention gap; not a seam signal.**

---

## 4. Diagnostic sub-table — Robust-wrong test

Not triggered. No robust-wrong flags in this run.

P06 context (from Tier 0B, 1.5B model): stable-wrong narrow behavior observed on 1.5B, but shortcut causality not confirmed because the broad (counterfactual) arm also failed at FP16 on 1.5B — rescue condition not met. Not a confirmed robust-wrong. Preserved as a diagnostic observation only.

---

## 5. Error-source ledger

| Task | Effect observed | Probe / intervention | Plausible source (cautious) | Evidence strength |
|---|---|---|---|---|
| LC2/file_code | Monotonic component degradation at INT4; composite unaffected | Component check isolated; composite checked independently | INT4 disrupts isolated semantic binding ("what does file X contain?") but not full chain inference | low — single item, no replication |
| LD3/broad | Non-monotonic broad arm drop at INT8 (1.0→0.67→1.0) | None — checklist score reflects fact-listing choice | INT8 produces different 2-fact answer for this context, one that misses a checklist term | low — single item, non-monotonic, deterministic artifact |
| LD4/hira_tag | Non-monotonic component blip at INT8 (1.0→0.0→1.0) | None | INT8 answers differently for "which tag does Hira carry?" despite composite stability | low — single item, non-monotonic, does not surface at composite |
| P01R/narrow | Persistent baseline failure at FP16 — capability floor | Component checks pass; composite fails at all rungs | 7B cannot compare two known times to produce ordered comparison with named referent | medium — stable across all runs; classified as capability floor, not compression |

---

## Run family summary — full ledger to date

| Run | Model | Calib | Pairs | INT8 ΔR | INT4 ΔR | Outcome |
|---|---|---|---|---|---|---|
| Tier 0A | Qwen2.5-7B | code | 5 | 0.0 | 0.0 | flat / task ceiling |
| Tier 0B | Qwen2.5-1.5B | code | 3 | 0.0 | 0.0 | flat / task ceiling |
| Tier 0C (code) | Qwen2.5-7B | code | 17 | −0.0196 | 0.0 | flat / task ceiling |
| Tier 0C (prose) | Qwen2.5-7B | prose | 17 | −0.0196 | 0.0 | flat / task ceiling |

**Calibration invariance across Tier 0C:** confirmed — identical results under both labels.

---

## Ledger update

**Connection/continuity claim status:** open / not promoted / not demoted.

**Reason:** the tested task family produced a calibration-invariant flat result due to task ceiling. The 7B navigated 5-hop chains with two distractors and negation without error at INT4.

**Next promotion condition:** a future task batch must enter the model's stress band — FP16 composite and component competence high, followed by INT4 composite degradation while components remain correct, surviving calibration invariance.

**Next demotion condition:** a future calibrated task family enters the stress band and still shows equal component and composite retention after difficulty matching, scoring symmetry, and calibration invariance.

---

## What the run validates

1. Harness ran across full bit-depth ladder (FP16/INT8/INT4) without error.
2. Pair-level scoring remained interpretable and symmetric across arms.
3. ΔR and bootstrap CIs computed correctly with NaN exclusion for zero-baseline pairs.
4. Cross-calibration invariance checked and passed.
5. Component-level blips logged separately from composite-level effects.
6. Local null was legible rather than opaque.

The instrument works. The task family just wasn't hard enough.

---

## What the run does not show

- That connection/continuity is not compression-separable in general.
- That quantization does not affect compositional reasoning.
- That 5-hop tasks are universally robust.
- That the mechanism behind any observed component blip is known.
- That the 7B has no fragility band — only that these chains are below it.

Mechanism remains blocked. This is a behavioral measurement result only.

---

## Next action

Stop squeezing this task family.

Build a harder 7B task ladder targeting the fragility band:

- 6–7 hop chains
- Adversarial distractors sharing surface features with the correct chain
- Intermediate-value traps (wrong answer plausible from partial chain traversal)
- Role swaps and entity re-binding across hops
- Property-chaining across semantic domains
- Arithmetic/state chains with intermediate reuse
- Forced-intermediate variants for any composite failure with components preserved

Screen at FP16 first. Only pairs with correct composite answers AND correct component checks at FP16 enter the INT8/INT4 stress sweep. One bad baseline wastes a rung.
