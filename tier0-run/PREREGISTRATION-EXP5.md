# Pre-Registration — Experiment 5: Format-Cliff Replication / Prompt-Sensitivity Test (Option C)

**Locked:** 2026-06-06  
**Status:** LOCKED — do not edit after task file construction begins.

---

## 0. Rationale

Experiments 3 and 4 established a format cliff under INT4 quantization on Qwen2.5-1.5B:

- `G_strict(INT4)` = −0.0494, CI [−0.0926, −0.0123] — excludes zero
- `G_content(INT4)` = −0.0123, CI [−0.0370, +0.0000] — includes zero
- CONTENT_LOSS = 0, COMPOSITE_FAILURE = 0

The failing items all shared the same pattern: the model produced the correct answer content but stopped following the clipped output format on short-context prompts. The format instruction used in those experiments was:

```
Reply with exactly: ANSWER: <value>
```

**Open question:** Is the format cliff a property of the INT4 model's output-style behavior under compression, or is it scaffold-sensitive — i.e., does a stronger, more explicit format instruction reduce or eliminate it?

This experiment directly tests that question. It is **not** a seam test. It is a **format-cliff replication / prompt-sensitivity test**.

---

## 1. Locked question

> **Does INT4 format degradation persist under a stronger explicit forced-format prompt scaffold, while content remains intact?**

Two informative outcomes:

| Outcome | Interpretation |
|---|---|
| Format cliff **persists** (G_strict excludes zero) | Format degradation is robust to instruction strength. The model's output-style shift at INT4 is not correctable by stronger format instructions alone. Likely a logit-space style drift. |
| Format cliff **disappears** (G_strict includes zero) | Format degradation is scaffold-sensitive. A stronger explicit instruction anchors format compliance at INT4. The Exp 3/4 cliff was an instruction-following degradation, not a fundamental style shift. |

Both outcomes are informative. Neither is a failure.

---

## 2. Model and hardware

| Field | Value |
|---|---|
| Model | `Qwen/Qwen2.5-1.5B-Instruct` |
| INT8 quantization | In-place via `quantize_model` (group_size=64) |
| INT4 source | `mlx-community/Qwen2.5-1.5B-Instruct-4bit` |
| Hardware | Apple Silicon (MLX, macOS 15+) |
| Decoding | temperature=0.0 (greedy, deterministic) |
| Max tokens | 512 |

Same model as Experiments 3 and 4. The format cliff was observed on this model; the test is whether it survives a new scaffold.

---

## 3. What changes vs. Experiment 4

**One variable changes:** the format instruction in every prompt.

| | Exp 3 / Exp 4 | Exp 5 |
|---|---|---|
| Format instruction | `Reply with exactly: ANSWER:` | `Respond using only this exact format with nothing before or after: ANSWER:` |
| Factual content | same | same chains; some items may be reused or replaced |
| Model | same | same |
| Scorer | same | same |
| Stress ladder | same | same |
| Task structure | same | same |

Everything else is held fixed. The format instruction is the only independent variable.

---

## 4. Forced-format instruction (LOCKED)

The new format instruction, used in all Exp 5 prompts:

```
Respond using only this exact format with nothing before or after: ANSWER: <value>
```

The paraphrase variant (for the stability screen):

```
Your entire response must be exactly this and nothing else: ANSWER: <value>
```

These replace `"Reply with exactly: ANSWER:"` and `"Answer using this format: ANSWER:"` from Experiments 3–4. All other prompt elements (context, question) are unchanged.

---

## 5. Tasks

**Task file:** `tasks_exp5.py` — new file constructed from a subset of the task content used in Experiments 2–4, with the forced-format instruction substituted into every prompt.

**Construction rule:** Take the factual chains and questions from `tasks_exp2.py`. Substitute the new format instruction. Do not change context strings, hop questions, or expected answer values. The expected answers remain identical.

**Priority for inclusion:** Items that showed FORMAT_COMPLIANCE_LOSS in Experiment 4 should be included if they pass the stability screen. This ensures a direct comparison between old-scaffold and new-scaffold behavior on the same items.

**Minimum eligible count:** ≥ 8 stable substantive pairs required to proceed to stress sweep (inherited from Exp 3 stability screen protocol).

---

## 6. Stability screen

Same protocol as Experiment 3 (`run_stability_screen.py`), but run against the new `tasks_exp5.py`.

- Narrow arm must score 1.0 on both the original forced-format prompt AND the forced-format paraphrase at FP16.
- All component checks must score ≥ 0.5 at FP16.
- Broad arm must score ≥ 0.5 at FP16.

Classification is identical to Exp 3: STABLE, BOUNDARY, COMP_FAIL, BROAD_FAIL, FLOOR.

If fewer than 8 substantive pairs are STABLE, report Outcome B (baseline floor) immediately.

---

## 7. Scorer — unchanged (LOCKED)

The dual scorer from `run_tier0.py` is used without modification:

- `strict_format_score` — primary for format-compliance claims
- `content_slot_score` — primary for content/capability claims (token-phrase matching)
- `partial_content_score` — diagnostic for COMPOUND_NOUN_DROP only
- Failure taxonomy: PASS, FORMAT_COMPLIANCE_LOSS, COMPOUND_NOUN_DROP, CONTENT_LOSS, ROBUST_WRONG
- 9 pre-registered unit tests from PREREGISTRATION-EXP4.md §9 must pass before any run

The scorer is not modified to match the new format instruction. If `strict_format_score` passes the new scaffold outputs, it will be because the model is producing compliant outputs — not because the scorer was adjusted.

---

## 8. Primary readout

Same as Experiment 4: G_strict(w) and G_content(w) computed per rung, with bootstrap CIs (1000 iterations, seed=0).

### Primary comparison (Exp 4 vs. Exp 5)

| Metric | Exp 4 (standard format) | Exp 5 (forced format) | Interpretation |
|---|---|---|---|
| G_strict(INT4) | −0.0494 [−0.0926, −0.0123] | TBD | Did cliff persist? |
| G_content(INT4) | −0.0123 [−0.0370, +0.0000] | TBD | Did content remain intact? |
| format_compliance_rate(INT4) | narrow=0.917, broad=0.750 | TBD | Did compliance improve? |
| CONTENT_LOSS | 0 | TBD | Still zero? |

**Cliff persists:** Exp 5 G_strict(INT4) CI excludes zero, in the same direction as Exp 4.  
**Cliff disappears:** Exp 5 G_strict(INT4) CI includes zero — format cliff is scaffold-sensitive.  
**Content preserved:** Exp 5 G_content(INT4) CI includes zero — content retained regardless of scaffold.  
**Content degrades:** Exp 5 G_content(INT4) CI excludes zero — unexpected; treat as surprise case requiring item audit.

---

## 9. Outcome table

| Outcome | Definition | Action |
|---|---|---|
| **F — cliff persists** | G_strict(INT4) CI excludes zero; G_content CI includes zero; calibration-invariant | Format cliff is robust to instruction strength. Log as replication. Consider new model or new task family. |
| **G — cliff disappears** | G_strict(INT4) CI includes zero; G_content CI includes zero | Cliff was scaffold-sensitive. Format compliance at INT4 is instruction-anchored. Log mechanism. |
| **H — content degrades** | G_content(INT4) CI excludes zero | Unexpected: content-level degradation appeared. Conduct item audit immediately before any interpretation. |
| **B — baseline floor** | < 8 stable pairs after stability screen | Tasks too hard or too easy for 1.5B under forced-format instruction; redesign. |

---

## 10. Calibration-invariance gate

Same as Experiments 3–4: results count only if G_strict(w) and G_content(w) rankings are invariant across:
- Calibration A: `calib=code`
- Calibration B: `calib=prose`

---

## 11. Kill conditions

**Kill for Outcome F (cliff persists) promotion:**
- G_strict CI includes zero at INT4
- G_strict direction flips across calibrations

**Kill for Outcome G (cliff disappears) promotion:**
- G_strict CI excludes zero (cliff still present under forced format)

**Kill for item audit (Outcome H):**
- Any G_content CI that excludes zero triggers a mandatory item-level audit before any claim is made

---

## 12. What this pre-registration does not commit to

- That the format cliff will persist or disappear — the experiment decides
- The exact forced-format phrasing will be sufficient to anchor compliance — it is a strong scaffold, not guaranteed to work
- That Option C closes the format-degradation finding — one positive result under one scaffold change is local replication, not a general law
- That the seam hypothesis (Test 1) is addressed in any way by this experiment

---

## 13. Ordering constraint

```
1. This pre-registration frozen                ← you are here
2. tasks_exp5.py constructed (forced-format prompts)
3. Stability screen run on tasks_exp5.py
4. tasks_exp5_stable.py auto-generated
5. Calibration A run (calib=code)
6. Calibration B run (calib=prose) after A is archived
7. Results recorded in RESULTS-EXP5.md
```

Do not construct tasks or run the stability screen before this file is finalized.
