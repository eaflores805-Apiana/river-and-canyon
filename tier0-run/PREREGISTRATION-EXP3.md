# Pre-Registration — Experiment 3: 1.5B on Experiment 2 Tasks

**Locked:** 2026-06-06  
**Status:** LOCKED — do not edit after stability screen begins.

---

## 0. Rationale

Experiments 1 and 2 both produced calibration-invariant local nulls on Qwen2.5-7B. The 7B model clears every task family built so far — including 6-hop distractor chains, 7-hop dual-chain role-swaps, and intermediate-value traps — without composite degradation at INT4.

The 7B is above the cliff. Experiment 3 changes the model to find the cliff.

**Hypothesis:** Qwen2.5-1.5B sits closer to the capability boundary for these task families. Items that the 7B solves stably at FP16 may be near the 1.5B's FP16 ceiling. If so, INT4 compression may push some items over the edge — composites fail while components survive.

---

## 1. Model and hardware

| Field | Value |
|---|---|
| Model | `Qwen/Qwen2.5-1.5B-Instruct` |
| INT8 quantization | In-place via `quantize_model` (group_size=64) |
| INT4 source | `mlx-community/Qwen2.5-1.5B-Instruct-4bit` |
| Hardware | Apple Silicon (MLX, macOS 15+) |
| Decoding | temperature=0.0 (greedy, deterministic) |
| Max tokens | 512 |

---

## 2. Tasks

**No new tasks.** The Experiment 2 task set (`tasks_exp2.py`) is used as-is.

22 pairs across families A–E + controls. Eligibility is determined by the stability screen below, not by FP16 score alone.

---

## 3. Margin-aware stability screen

**Motivation:** In Experiment 2, four items failed at FP16 and INT8, then recovered at INT4 (FA1, FA3, FC1, FB2). This demonstrated that temperature=0 greedy decoding can flip near the capability boundary due to small logit perturbations from quantization. Items near the boundary in either direction (failure or success) are unreliable. The stability screen excludes them.

**Screen protocol:** For each task pair, run the narrow arm at FP16 with:
1. The original prompt (as written in tasks_exp2.py)
2. A paraphrase variant: "Reply with exactly: ANSWER:" → "Answer using this format: ANSWER:"

Both must score 1.0 for the narrow arm to be considered stable.

Additionally, all component checks must score ≥ 0.5 on their original prompts at FP16, and the broad arm must score ≥ 0.5 on its original prompt at FP16.

**Stability classifications:**
- **STABLE:** narrow original = 1.0, narrow paraphrase = 1.0, all comps ≥ 0.5, broad ≥ 0.5 → enters stress sweep
- **BOUNDARY:** narrow original = 1.0, narrow paraphrase < 1.0 → excluded (near capability ceiling; answer depends on instruction phrasing)
- **FLOOR:** narrow original < 1.0 → excluded (below FP16 capability for this model)

**Minimum eligible count:** ≥ 8 substantive pairs (excluding controls) required to proceed to stress sweep. If fewer, Experiment 3 outcome is immediately Outcome B (baseline floor).

---

## 4. Stress sweep

Run `run_tier0.py` with `--tasks tasks_exp3` (auto-generated filtered task file from stable pairs) using `--bits 16 8 4`. Primary calibration: `--calib code`. Calibration-invariance check: repeat with `--calib prose`.

---

## 5. Primary readout — G(w)

For each eligible pair at each rung w ∈ {INT8, INT4}:

```
G(w) = R_component(w) − R_composite(w)
```

where R_composite = narrow score at w / narrow score at FP16, and R_component = mean component retention across all checks with valid FP16 baseline.

Bootstrap CI on mean G(w), 1000 iterations, seed=0.

**Seam signal:** mean G(w) CI excludes zero from below (i.e., CI lower bound > 0), replicated under both calibrations.

**ΔR (secondary):** mean(R_broad) − mean(R_narrow) across eligible pairs.

---

## 6. Pre-declared outcome table

| Outcome | Definition | Action |
|---|---|---|
| **A — seam candidate** | G(w) CI lower bound > 0 at any rung, calibration-invariant, not attributable to scoring asymmetry | First positive signal; inspect pair-level seam flags; run forced-intermediate follow-up |
| **B — baseline floor** | Fewer than 8 stable pairs after stability screen; or most eligible pairs fail FP16 even on original prompt | Tasks too hard for 1.5B; design Experiment 4 with easier task families scaled for 1.5B |
| **C — inverse seam** | G(w) < 0 and CI upper bound < 0 — component drops, composite holds | Strengthens inverse-seam watch; not the target signal |
| **D — flat** | G(w) CI overlaps zero at all rungs under both calibrations | 1.5B clears the task family too; both models above the cliff for these tasks |

---

## 7. Kill conditions

**Kill for Outcome A promotion:**
- G(w) CI includes zero at any rung
- G(w) ranking flips across calibrations (code vs. prose)
- Gap traced to difficulty asymmetry: narrow arm harder at FP16 than broad arm on the same pair
- Scoring asymmetry found between narrow and broad arms

**Kill for proceeding to stress sweep:**
- Fewer than 8 stable substantive pairs after stability screen → report Outcome B immediately

---

## 8. Forced-intermediate follow-up (if Outcome A)

If any pair shows composite failure (R_composite < 0.5) while all components pass (R_component = 1.0) at any rung: run a forced-intermediate variant where the penultimate hop value is supplied explicitly in the question. If that recovers the score, the failure is localized to the final integration step — a confirmed seam observation.

---

## 9. Calibration-invariance gate

Results count only if the G(w) ranking (and ΔR ranking) is invariant across:
- Calibration A: `calib=code`  
- Calibration B: `calib=prose`

A result that flips sign or ranking across calibrations is treated as Outcome B (artifact).

---

## 10. What this pre-registration does not commit to

- The exact number of stable pairs (unknown until stability screen; minimum 8 required)
- Whether the 1.5B can pass any particular item at FP16 (determined empirically)
- That the seam signal will appear — only that this is the right experiment to find it if it exists for this task family
