# Tier 0 Run — the experiment, finally

This folder is the turn from analysis to measurement. The papers, the protocol,
the pressure-test record — all complete. The one thing missing from the whole
project has always been a number. This is where you get it.

## What's here

- **`run_tier0.py`** — runnable MLX harness. Quantizes a model across bit-depths,
  runs the task list, scores with symmetric strictness, computes retention and the
  paired ΔR with bootstrap CIs, flags robust-wrong cases, writes JSON.
- **`tasks.py`** — the matched pairs. Two worked examples; **you build the rest.**
  This is the real intellectual work — the harness is just plumbing.
- **`RESULTS-INTAKE-TEMPLATE.md`** — where the numbers land, with the two
  diagnostic sub-tables (forced-intermediate for seams, counterfactual for robust-wrong).

## Setup (on your Mac — 48GB is plenty)

```bash
# macOS 15.0+ required by MLX
pip install mlx-lm numpy

# sanity check: one line should download + run a small model
python -c "from mlx_lm import load, generate; m,t = load('mlx-community/Llama-3.2-3B-Instruct-4bit'); print(generate(m,t,prompt='hi',max_tokens=10))"
```

## The run

```bash
# 1. Build your pairs in tasks.py (20-40 pairs). Lock them BEFORE looking at results.
# 2. First calibration pass:
python run_tier0.py --model Qwen/Qwen2.5-7B-Instruct --bits 16 8 4 --calib code

# 3. Second calibration pass (the invariance gate):
python run_tier0.py --model Qwen/Qwen2.5-7B-Instruct --bits 16 8 4 --calib prose

# 4. Compare the two: the ΔR pair-ranking must be invariant. If it flips,
#    the signal is a calibration artifact — discard, don't report.
```

*(Note: the simplest calibration handling for a first pilot is to run the same
pairs and let MLX's default quantization stand; true two-calibration AWQ/GPTQ
calibration is a refinement. For the very first look, even a single clean
FP16→INT8→INT4 sweep with symmetric scoring is a legitimate pilot — the
cross-calibration gate is what upgrades it from "provisional" to "validated.")*

## What counts as a result

**Any outcome is a result. The only non-result is not running.**

- **Outcome A** (ΔR>0, CI excludes zero, ranking invariant) → matched-pair
  fragility is real for this model. Tier 1 diagnostics earn the right to run.
- **robust-wrong flags** → the retention-blind-spot is observed, not just argued.
  The one durable contribution, demonstrated on a real model.
- **flat / B / C** → the effect dissolved under matched, symmetric, invariant
  conditions. This is publishable and honest: "the gap did not survive controls."

## The honest framing (unchanged from the whole project)

This pilot tests whether **the framework's own claims** hold — the matched-pair
ΔR and the retention-blind-spot detection. The field has already shown the
*phenomena* exist (compositional gaps, shortcut learning, quantization cliffs).
What's unrun is whether *this specific controlled measurement* isolates them and
adds value. One model, one size is a pilot, not a claim — the protocol wants a
second size before generalizing. Plan it in.

If the result is flat, that is not failure. It is the experiment doing its job.
The whole point of building it this carefully was so that a "no" would be as
trustworthy as a "yes."

## Start here: task design

Before the CSV or the run, the task set is designed in [`task_design.md`](task_design.md) — the four-cell structure, the closed-world rule, review-trigger thresholds, and one worked example per cell. The matched pairs are left blank to be filled; that is the core of the experiment. Order: fill the pairs → generate `tasks/tier0_tasks.csv` → smoke-test → run → record in `RESULTS-INTAKE-TEMPLATE.md`.
