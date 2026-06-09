# Experiment 4 — Results

*Filled: 2026-06-06. Results files: `results_code_1780765654.json` (Calibration A), `results_prose_1780765846.json` (Calibration B). Tasks: `tasks_exp3.py`. Pre-registration: `PREREGISTRATION-EXP4.md`.*

---

## 0. Run identity

| Field | Value |
|---|---|
| Date | 2026-06-06 |
| Model | `Qwen/Qwen2.5-1.5B-Instruct` |
| Quantization | FP16 baseline; INT8 in-place (group_size=64); INT4 from `mlx-community/Qwen2.5-1.5B-Instruct-4bit` |
| Bit-depths swept | FP16, INT8, INT4 |
| Task file | `tasks_exp3.py` (12 pairs: 9 substantive + 3 controls) |
| Calibration A | `code` |
| Calibration B | `prose` |
| Hardware | Apple Silicon (MLX, macOS 15+) |
| Decoding | temperature=0.0 (greedy, deterministic) |
| Max tokens | 512 |
| Pre-registered | **Y** — `PREREGISTRATION-EXP4.md` locked before scorer implementation |
| Scorer | Dual: `strict_format_score` + `content_slot_score` (token-phrase matching) |

---

## 1. Pre-registration reference

`PREREGISTRATION-EXP4.md` locked 2026-06-06 before scorer implementation. The following were frozen before any live run:

- Scorer definitions (`strict_format_score`, `content_slot_score`, `partial_content_score`)
- Failure taxonomy (PASS, FORMAT_COMPLIANCE_LOSS, COMPOUND_NOUN_DROP, CONTENT_LOSS, ROBUST_WRONG)
- Scoring hierarchy: `content_slot_score` primary for content/capability claims; `strict_format_score` primary for format-compliance claims only
- Nine pre-labeled unit test cases
- Outcome table (A–E)
- Calibration-invariance gate

---

## 2. Scorer validation gate

**Unit tests:** All 9 pre-registered cases passed before each run (verified from run logs).

**Historical regression:** `regression_check_exp3.py` applied the dual scorer to stored Exp 3 outputs (`results_code_1780745541.json`) and reproduced the manual Option A verdict to four decimal places:

| Metric | Manual rescore | Regression check | Match? |
|---|---|---|---|
| G_strict(INT4) | −0.0494 [−0.0926, −0.0123] | −0.0494 [−0.0926, −0.0123] | **Y** |
| G_content(INT4) | −0.0123 [−0.0370, 0.0000] | −0.0123 [−0.0370, +0.0000] | **Y** |
| FC1/vault3_token class | COMPOUND_NOUN_DROP | COMPOUND_NOUN_DROP | **Y** |

The scorer was validated against a known historical failure case before any fresh run began.

---

## 3. Output provenance note

Calibration A (`code`) and Calibration B (`prose`) produced identical scores, CIs, and failure-class distributions at every rung. The two runs were executed as separate fresh model loads against the same task prompts, under their respective calibration labels. No per-prompt calibration manipulation is applied by `run_tier0.py` to the prompt text itself — the calibration label is metadata attached to the result file and used only for the invariance check.

**Output provenance not independently verified at the prompt level:** because `--calib code` and `--calib prose` do not alter the actual prompts sent to the model, and both runs share the same tasks and model, bit-identical outputs are expected and do not constitute independent replication of different prompt conditions. The calibration-invariance gate confirms that the result is not an artifact of calibration-label assignment, but does not provide independent replication across different prompt distributions. This limitation is stated explicitly per the protocol requirement that calibration distribution be reported and interpretable.

---

## 4. Calibration A readout — `results_code_1780765654.json`

### G metrics (substantive pairs, n=9)

| Rung | G_strict | 95% CI | G_content | 95% CI | Outcome |
|---|---|---|---|---|---|
| INT8 | +0.0000 | [+0.0000, +0.0000] | +0.0000 | [+0.0000, +0.0000] | flat |
| INT4 | **−0.0494** | **[−0.0926, −0.0123]** | **−0.0123** | **[−0.0370, +0.0000]** | **strict: negative / content: flat** |

### Format compliance rate

| Rung | narrow | broad | comps |
|---|---|---|---|
| FP16 | 1.000 | 1.000 | 1.000 |
| INT8 | 0.917 | 0.917 | 1.000 |
| INT4 | 0.917 | 0.750 | 0.949 |

### Failure class distribution

| Rung | PASS | FORMAT_COMPLIANCE_LOSS | COMPOUND_NOUN_DROP | CONTENT_LOSS |
|---|---|---|---|---|
| FP16 | 83 | 0 | 0 | 0 |
| INT8 | 81 | 2 | 0 | 0 |
| INT4 | 76 | 6 | 1 | 0 |

---

## 5. Calibration B readout — `results_prose_1780765846.json`

### G metrics (substantive pairs, n=9)

| Rung | G_strict | 95% CI | G_content | 95% CI | Outcome |
|---|---|---|---|---|---|
| INT8 | +0.0000 | [+0.0000, +0.0000] | +0.0000 | [+0.0000, +0.0000] | flat |
| INT4 | **−0.0494** | **[−0.0926, −0.0123]** | **−0.0123** | **[−0.0370, +0.0000]** | **strict: negative / content: flat** |

### Format compliance rate

| Rung | narrow | broad | comps |
|---|---|---|---|
| FP16 | 1.000 | 1.000 | 1.000 |
| INT8 | 0.917 | 0.917 | 1.000 |
| INT4 | 0.917 | 0.750 | 0.949 |

### Failure class distribution

| Rung | PASS | FORMAT_COMPLIANCE_LOSS | COMPOUND_NOUN_DROP | CONTENT_LOSS |
|---|---|---|---|---|
| FP16 | 83 | 0 | 0 | 0 |
| INT8 | 81 | 2 | 0 | 0 |
| INT4 | 76 | 6 | 1 | 0 |

---

## 6. Cross-calibration comparison — invariance gate

| Metric | Calib A (code) | Calib B (prose) | Invariant? |
|---|---|---|---|
| INT8 G_strict | +0.0000 [0.0, 0.0] | +0.0000 [0.0, 0.0] | **Y** |
| INT8 G_content | +0.0000 [0.0, 0.0] | +0.0000 [0.0, 0.0] | **Y** |
| INT4 G_strict | −0.0494 [−0.0926, −0.0123] | −0.0494 [−0.0926, −0.0123] | **Y** |
| INT4 G_content | −0.0123 [−0.0370, +0.0000] | −0.0123 [−0.0370, +0.0000] | **Y** |
| fmt_compliance narrow INT4 | 0.917 | 0.917 | **Y** |
| fmt_compliance broad INT4 | 0.750 | 0.750 | **Y** |
| fmt_compliance comps INT4 | 0.949 | 0.949 | **Y** |
| CONTENT_LOSS | 0 | 0 | **Y** |
| COMPOSITE_FAILURE | 0 | 0 | **Y** |
| Failure pattern INT4 | FCL×6, CND×1 | FCL×6, CND×1 | **Y** |

**Calibration-invariance gate: PASSED.** All metrics identical across both calibration runs. See §3 for provenance note on why bit-identical results are expected given the prompt architecture.

---

## 7. Failure-class anatomy

All score drops in this run share a single root cause: **the 1.5B model stops following the clipped-answer format instruction under INT4 on short-context prompts, while retaining the correct answer content.**

### FORMAT_COMPLIANCE_LOSS (6 items at INT4)

| Item | FP16/INT8 output | INT4 output | strict | content |
|---|---|---|---|---|
| FA1/broad | `ANSWER: File K` | `ANSWER: amber box stores File K.` | 0 | 1 |
| FA1/comp[box_file] | `ANSWER: File K` | `ANSWER: amber box stores File K.` | 0 | 1 |
| FA4/broad | `ANSWER: Log 3` | `ANSWER: obsidian drawer stores Log 3` | 0 | 1 |
| FA4/comp[drawer_log] | `ANSWER: Log 3` | `ANSWER: obsidian drawer stores Log 3` | 0 | 1 |
| AC1/narrow | `ANSWER: silver disk` | `ANSWER: The blue locker contains the silver disk.` | 0 | 1 |
| AC1/broad | `ANSWER: silver disk` | `ANSWER: The blue locker contains the silver disk.` | 0 | 1 |

In every case the correct value appears in the output. The strict scorer returns 0 because the output format contract ("Reply with exactly: ANSWER: \<item\>") is violated. The content scorer returns 1 because the value token sequence is present.

**AC1 note:** AC1 (1-hop atomic control) fails at INT8, not just INT4. This was observed in Experiment 3 and reproduces here. The format compliance threshold for short-context prompts on this model is below INT8.

### COMPOUND_NOUN_DROP (1 item at INT4)

| Item | FP16 output | INT4 output | strict | content | partial |
|---|---|---|---|---|---|
| FC1/comp[vault3_token] | `ANSWER: silver token` | `ANSWER: token` | 0 | 0 | 0.5 |

The adjective "silver" is dropped. The noun head "token" survives. This is a genuine content-level event — the full expected value "silver token" is not present in the output. It is not a format compliance failure; the format is correct. Classified COMPOUND_NOUN_DROP per the pre-registered taxonomy.

Single item, insufficient to produce a statistically significant G_content signal.

### CONTENT_LOSS (0 items)

No item at any rung produced output that entirely lacked the expected answer content. The correct answer appeared in every output at every rung, sometimes in a sentence rather than the clipped format.

### ROBUST_WRONG (0 items)

No consistent wrong answer was detected across rungs.

---

## 8. Item-level divergences (strict ≠ content)

All eight divergent items are FORMAT_COMPLIANCE_LOSS. No item is strict=0, content=0 except FC1/vault3_token (COMPOUND_NOUN_DROP). The dual scorer cleanly separates the two failure modes: format loss is visible in G_strict, absent in G_content; the compound-noun drop appears in G_content but is a single item.

---

## 9. Outcome classification

| Outcome | Definition | Result |
|---|---|---|
| **A — seam candidate** | G_content CI lower bound > 0, calibration-invariant | Not observed |
| **B — baseline floor** | < 8 stable pairs | Not applicable (inherited from Exp 3) |
| **C — format cliff** | G_strict CI excludes zero; G_content CI includes zero | **Observed at INT4, calibration-invariant** |
| **D — flat** | Both G metrics CI overlap zero | Not the outcome at INT4 for G_strict |
| **E — content inverse seam** | G_content CI upper bound < 0 | Not observed |

**Final outcome: Outcome C — calibration-invariant format cliff under dual scoring.**

> **INT4 compression degrades strict format-compliance while preserving answer content.**

The model generally retains the correct answer but sometimes stops following the clipped output contract on short-context prompts. This is not reasoning degradation, not content loss, and not seam fragility. It is a behavior change in output style under quantization.

---

## 10. What this run does not show

- That compression broke reasoning.
- That components degraded more than composites at the content level.
- That the model forgot the facts — every answer was present in the output.
- That the format cliff generalizes across models, task families, or quantization methods.
- That the calibration-invariance result reflects independent replication across genuinely different prompt distributions (see §3).

The correct summary of Experiment 4's finding:

> **Compression perturbed answer-format compliance while preserving answer content.**

---

## 11. Claim-status update

**Primary seam claim (Test 1):** Not triggered. G_content(INT4) CI [−0.0370, +0.0000] includes zero. No content-level gap between composite and component retention was detected at any rung.

**Format-degradation candidate (Test 2):** Locally supported. G_strict(INT4) CI [−0.0926, −0.0123] excludes zero, calibration-invariant. The effect is confined to this model, this task family, and this quantization method. A stronger result requires replication on new tasks, new prompts, or a second model.

---

## 12. Ledger update

| Run | Model | Task family | Scorer | G_strict INT4 CI | G_content INT4 CI | Outcome |
|---|---|---|---|---|---|---|
| Tier 0A | 7B | 3-hop | strict only | — | — | flat / task ceiling |
| Tier 0B | 1.5B | 3-hop | strict only | — | — | flat / task ceiling |
| Tier 0C | 7B | 5-hop | strict only | — | — | flat / task ceiling |
| Exp 2 | 7B | 6–7-hop | strict only | — | [−0.061, 0.0] | flat / local null |
| Exp 3 | 1.5B | 6–7-hop | strict only | — | [−0.093, −0.012] | Outcome C strict — dissolved by content rescore |
| **Exp 4 (code)** | **1.5B** | **6–7-hop** | **dual** | **[−0.0926, −0.0123]** | **[−0.0370, +0.0000]** | **Outcome C — format cliff, content flat** |
| **Exp 4 (prose)** | **1.5B** | **6–7-hop** | **dual** | **[−0.0926, −0.0123]** | **[−0.0370, +0.0000]** | **Outcome C — format cliff, content flat** |

**Connection/continuity claim status:** open / not promoted / not demoted.

Experiment 4 replicates the Experiment 3 strict-scoring result under a pre-registered dual scorer, and confirms that the G_strict signal is a format-compliance artifact rather than a content-level retention gap. The positive seam signal (G_content > 0, CI excludes zero) has not appeared across four experiments, two models, multiple task families, and multiple bit-depths.

The dual scorer is now the standard instrument. Strict-only results are no longer sufficient to support a seam or content-degradation claim.

---

## 13. Next action

Experiment 4 supports Test 2 locally: format compliance degrades under INT4 on this model and this task family, while content is retained. This is a local result. Before drawing broader conclusions, the next decision point is:

**Decide whether to run a fresh replication of Test 2 on a different task family.**

Options:

**Option A — Same model, new short-context task family:**  
Design component checks with multi-token expected values that are more likely to trigger compound-noun drops and format violations. Verify that the format cliff reproduces across tasks, not just FA/FA4/AC1.

**Option B — Different model, same task family:**  
Run the dual scorer against a third model (e.g., Qwen2.5-0.5B or a non-Qwen family) to test whether the format cliff is model-specific or a general INT4 artifact.

**Option C — Forced-format prompt variant:**  
Add an explicit format instruction prefix ("You MUST respond with exactly: ANSWER: \<value\> and nothing else") to component checks and rerun. If the format cliff disappears, the root cause is the instruction-following degradation, not logit-space content loss.

**Option D — Accept and close Test 2 as locally confirmed:**  
Record Experiment 4 as a locally confirmed format-cliff finding and shift focus back to designing harder seam tasks for Test 1 with the dual scorer in place from the start.

The Exp 3/4 sequence validated the scoring infrastructure. A new model run should only proceed after the next task design is pre-registered.
