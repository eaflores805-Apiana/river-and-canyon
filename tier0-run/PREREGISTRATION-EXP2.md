# Pre-Registration — Experiment 2: Harder 7B Ladder

**Locked:** 2026-06-06  
**Status:** LOCKED — do not edit after FP16 screen begins.

---

## 0. Purpose

Experiment 1 (Tier 0C) produced a calibration-invariant local null: the 7B model navigated 5-hop closed-world chains without error at INT4. The task family was below the fragility threshold.

Experiment 2 uses the same model, same harness, same calibration-invariance gate — but harder chains designed to enter the 7B fragility band.

**Research question:** Can INT4 quantization break a linked composite answer (end-to-end chain) while the individual hop components survive?

---

## 1. Model and hardware

| Field | Value |
|---|---|
| Model | `Qwen/Qwen2.5-7B-Instruct` |
| Quantization | FP16 baseline; INT8 via `quantize_model` in-place (group_size=64); INT4 loaded from `mlx-community/Qwen2.5-7B-Instruct-4bit` |
| Hardware | Apple Silicon (MLX, macOS 15+) |
| Decoding | temperature=0.0 (greedy, deterministic) |
| Max tokens | 512 |

---

## 2. Task families

### Family A — 6-hop clean (FA1–FA4)
Six sequential hops, no distractor, no negation. Person → Object → Location → Sub-location → Container → Item → Status. Terminal value is a single ALL-CAPS token. Establishes whether the chain length alone breaks the composite answer.

### Family B — 6-hop + distractor + negation (FB1–FB4)
Identical chain structure to Family A, with one surface-similar distractor entity added (shares a surface feature with the correct chain) and one explicit negation statement ("Person does NOT hold [wrong item]"). Tests whether distractor presence degrades composite retention more than component retention.

### Family C — 7-hop role-swap (FC1–FC4)
Two complete parallel chains in the same prompt context. Both persons and their chains are fully specified. Narrow question asks about one specific person's terminal value. Broad question asks about a fact from the same chain that is not the terminal value. Components verify individual hops from both chains. Tests whether the model can maintain binding when two chains share structural positions.

### Family D — intermediate-value trap + distractor + negation (FD1–FD4)
Chain with a plausible wrong answer derivable from partial traversal (digit swap, wrong route, surface-similar value). Explicit negation of the trap answer. Narrow: correct terminal value. Broad: a mid-chain fact. Tests whether the trap disrupts composite retention more than component retention.

### Family E — arithmetic/state dependency (FE1–FE3)
Multi-step arithmetic chains where intermediate values are reused. Narrow: final computed result. Broad: an intermediate value. Component checks provide full arithmetic context and ask single-step questions.

### Controls
- **AC1, AC2:** Atomic single-step lookup (1 hop). Both broad. Expected retention = 1.0 at all rungs. Used to confirm harness is not universally degrading.
- **NC1:** Broad-broad negative control (both arms broad). Expected ΔR ≈ 0 by construction.

---

## 3. Eligibility screen

All items in `tasks_exp2.py` must pass FP16 baseline before entering the INT8/INT4 sweep:
- Composite narrow arm: score = 1.0 at FP16
- All component checks: score ≥ 0.5 at FP16 (exact-match components: 1.0; checklist-scored: ≥ 0.5)
- Broad arm: score ≥ 0.5 at FP16

Items failing any condition are excluded from the ΔR computation and flagged in the results. The sweep proceeds only if ≥ 15 eligible pairs remain after FP16 screen.

---

## 4. Primary readout — G(w)

For each eligible pair at each stress rung w ∈ {INT8, INT4}:

```
G(w) = R_component(w) − R_composite(w)
```

where:
- `R_composite(w)` = composite narrow score at w / composite narrow score at FP16
- `R_component(w)` = mean retention across all component checks for that pair

**Seam signal:** G(w) > 0 with bootstrap CI excluding zero, replicated across both calibration sets.

**ΔR (secondary):** same as Experiment 1 — mean(R_broad) − mean(R_narrow) across eligible pairs.

---

## 5. Pre-declared outcomes

| Outcome | Definition | Action |
|---|---|---|
| **A — seam signal** | G(w) CI excludes zero (components hold, composite degrades), calibration-invariant | Promote hypothesis: chain-boundary fragility exists |
| **B — metric artifact** | Gap dissolves under scoring symmetry check or chance correction | Demote: artifact, not signal |
| **C — task/pair confound** | Gap traced to difficulty mismatch, length mismatch, or state-load asymmetry | Redesign pairs, rerun |
| **D — calibrated local null** | G(w) CI overlaps zero at all rungs under both calibrations | Local null for this task family; no promotion, no demotion |

---

## 6. Kill conditions

**Kill for primary claim (seam signal):**
- G(w) CI includes zero at any tested rung, OR
- G(w) ranking reverses across calibration sets (code vs. prose)

**Kill for Outcome A promotion:**
- Scoring asymmetry found (broad arm penalized more than narrow arm for same output quality)
- Pair-level difficulty mismatch not controlled (narrow arm harder at FP16 than broad arm)

---

## 7. Forced-intermediate follow-up

If any pair shows composite failure (R_composite < 0.5) while all components pass (R_component = 1.0) at any rung: run a forced-intermediate variant where the question supplies the output of the penultimate hop explicitly and asks only the final step. If that recovers the score, the failure is localized to the final integration step — a positive seam observation.

---

## 8. Calibration-invariance gate

Results count ONLY if the G(w) ranking (and ΔR ranking) is invariant across:
- Calibration A: `calib=code`
- Calibration B: `calib=prose`

A result that flips sign or ranking across calibrations is treated as Outcome B (artifact) regardless of CI behavior.

---

## 9. What this pre-registration does not commit to

- The exact wording of prompts (these are locked in `tasks_exp2.py`, which is checked in before the FP16 screen)
- The exact number of eligible pairs after the FP16 screen (unknown until run; minimum threshold is 15)
- Model behavior at FP16 for new items (some may fail eligibility; that is expected)
