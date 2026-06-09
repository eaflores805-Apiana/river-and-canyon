# Pre-Registration: Tier 0B Smaller-Model Calibration Sweep

*Locked before results. Do not modify after the run starts.*
*Date: 2026-06-06*

---

## Purpose

Calibration sweep — find whether the existing task set enters a fragility zone on a weaker model.
This is **not** the main Tier 0 result. It is a dose-finding experiment.

Primary question:
> Are these tasks capable of entering a fragility zone at all?

---

## Separation from Tier 0A

```
Tier 0A: Qwen2.5-7B-Instruct, code calib
Result:  Good pipeline / no signal / task ceiling
         All eligible pairs scored 1.0 at FP16, INT8, INT4
         ΔR = 0.0, CI = [0.0, 0.0]
         Interpretation: tasks below 7B fragility threshold under this INT4 setup
```

Tier 0B does **not** update, revise, or compete with Tier 0A. They are separate runs
on different models. Cross-model comparison is not claim-bearing here.

---

## Run configuration

```
Run name:  Tier 0B smaller-model calibration sweep
Model:     Qwen/Qwen2.5-1.5B-Instruct
Bit depths: 16, 8, 4
Task set:  identical to Tier 0A (tasks.py unchanged)
Calib:     code
Decoding:  temperature = 0.0 (deterministic)
Max tokens: 256
Purpose:   calibration only
```

---

## Eligible pairs (same as Tier 0A)

P02R, P03, P04, P05, P06 — all with FP16 baseline > 0 on the 7B model.
Note: 1.5B may fail some of these at FP16. If so, those pairs are re-classified
as "below 1.5B capability floor" and excluded from ΔR the same way P01R was.

---

## Outcome interpretation (pre-declared)

| Pattern | Meaning |
|---|---|
| 1.5B also 1.0 across all rungs | Tasks too easy for this model family. Move to harder 3-5 hop chains with distractors. |
| 1.5B fails everything including P05 (atomic clean) | Model too weak or INT4 too destructive. Not seam evidence. Check scores and outputs. |
| 1.5B components pass, composite items fail | Scent trail. Not a result — worth scaling into harder 7B tasks. |
| 1.5B same-wrong errors on P06 or composite traps | Strengthens error-identity argument. Note and preserve. |

---

## What this sweep cannot support

- Any claim about the main Tier 0 hypothesis (different model = different experiment)
- Any statement about Qwen2.5-7B fragility
- Any comparison of 7B vs 1.5B as a fragility finding (model size is a confound)

## What this sweep does support

- Whether the task family has a usable stress gradient at all
- Which pairs and which hops are near the capability edge for smaller models
- Task design decisions for the next round of harder 7B pairs

---

*Locked: E. A. Flores, Apiana AI, Inc., 2026-06-06*
