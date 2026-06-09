# Experiment 5 — Results

*Filled: 2026-06-06. Results files: `results_code_1780767539.json` (Calibration A), `results_prose_1780767822.json` (Calibration B). Tasks: `tasks_exp5_stable.py`. Pre-registration: `PREREGISTRATION-EXP5.md`.*

---

## 0. Run identity

| Field | Value |
|---|---|
| Date | 2026-06-06 |
| Model | `Qwen/Qwen2.5-1.5B-Instruct` |
| Quantization | FP16 baseline; INT8 in-place (group_size=64); INT4 from `mlx-community/Qwen2.5-1.5B-Instruct-4bit` |
| Bit-depths swept | FP16, INT8, INT4 |
| Task file | `tasks_exp5_stable.py` (13 pairs: 10 substantive + 3 controls) |
| Calibration A | `code` |
| Calibration B | `prose` |
| Hardware | Apple Silicon (MLX, macOS 15+) |
| Decoding | temperature=0.0 (greedy, deterministic) |
| Max tokens | 512 |
| Pre-registered | **Y** — `PREREGISTRATION-EXP5.md` locked before tasks file construction |
| Scorer | Dual: `strict_format_score` + `content_slot_score` (token-phrase matching) |
| Format instruction | `"Respond using only this exact format with nothing before or after: ANSWER:"` |

---

## 1. Pre-registration reference

`PREREGISTRATION-EXP5.md` locked 2026-06-06 before any task file was built. Locked elements:

- Forced-format instruction (§4): `"Respond using only this exact format with nothing before or after: ANSWER: <value>"`
- Paraphrase for stability screen (§4): `"Your entire response must be exactly this and nothing else: ANSWER: <value>"`
- Outcome table (§9): F (cliff persists), G (cliff disappears), H (content degrades), B (floor)
- Scorer: unchanged from Exp 4 — 9 unit tests from PREREGISTRATION-EXP4.md §9 must pass before any run
- Calibration-invariance gate (§10)

---

## 2. Scorer validation gate

**Unit tests:** All 9 pre-registered cases passed before each run. Gate confirmed by terminal output before any model loading.

---

## 3. Stability screen

**Screen file:** `stability_screen_1780767489.json`  
**Protocol:** Same as Experiment 3 — narrow arm must score 1.0 on both forced-format original and forced-format paraphrase at FP16. All component checks ≥ 0.5. Broad arm ≥ 0.5.

| Classification | Pairs |
|---|---|
| STABLE (13) | FA1, FA2, FA3, FA4, FB1, FB4, FC1, FC4, FD1, FD2, AC1, AC2, NC1 |
| COMP_FAIL (1) | FD4 |
| BOUNDARY (0) | — |
| BROAD_FAIL (0) | — |
| FLOOR (0) | — |

**FD4 exclusion:** Component check `junction9_tower` returned `ANSWER: JUNCT9` (the input entity) at FP16; expected `ANSWER: SIGTOW1` (the output entity). This is a genuine FP16 content failure — the model cannot answer that intermediate hop correctly even at full precision. FD4 is excluded on capability grounds, not format grounds.

**Stable substantive pairs:** 10 / 11. Threshold of 8 met. Proceeded to stress sweep.

---

## 4. Output provenance note

Calibration A (`code`) and Calibration B (`prose`) produced bit-identical scores, CIs, and failure-class distributions at every rung. Both runs were fresh model loads against the same task prompts. The `--calib` flag is metadata attached to the result file; it does not alter the prompts sent to the model.

**Output provenance not independently verified at the prompt level:** identical outputs are expected and do not constitute independent replication across different prompt distributions. The calibration-invariance gate confirms results are not an artifact of calibration-label assignment, not that the results replicate across genuinely distinct prompt conditions. Same limitation stated in RESULTS-EXP4.md §3.

---

## 5. Calibration A readout — `results_code_1780767539.json`

### G metrics (substantive pairs, n=10)

| Rung | G_strict | 95% CI | G_content | 95% CI | Outcome |
|---|---|---|---|---|---|
| INT8 | +0.0000 | [+0.0000, +0.0000] | +0.0000 | [+0.0000, +0.0000] | flat |
| INT4 | **+0.0522** | **[−0.0878, +0.2778]** | **+0.0689** | **[−0.0711, +0.2889]** | **both flat (CI includes zero)** |

### Format compliance rate

| Rung | narrow | broad | comps |
|---|---|---|---|
| FP16 | 1.000 | 1.000 | 1.000 |
| INT8 | 1.000 | 1.000 | 1.000 |
| INT4 | 0.923 | 1.000 | 0.955 |

### Failure class distribution

| Rung | PASS | FORMAT_COMPLIANCE_LOSS | CONTENT_LOSS | COMPOUND_NOUN_DROP |
|---|---|---|---|---|
| FP16 | 92 | 0 | 0 | 0 |
| INT8 | 92 | 0 | 0 | 0 |
| INT4 | 88 | 1 | 3 | 0 |

---

## 6. Calibration B readout — `results_prose_1780767822.json`

### G metrics (substantive pairs, n=10)

| Rung | G_strict | 95% CI | G_content | 95% CI | Outcome |
|---|---|---|---|---|---|
| INT8 | +0.0000 | [+0.0000, +0.0000] | +0.0000 | [+0.0000, +0.0000] | flat |
| INT4 | **+0.0522** | **[−0.0878, +0.2778]** | **+0.0689** | **[−0.0711, +0.2889]** | **both flat (CI includes zero)** |

### Format compliance rate

| Rung | narrow | broad | comps |
|---|---|---|---|
| FP16 | 1.000 | 1.000 | 1.000 |
| INT8 | 1.000 | 1.000 | 1.000 |
| INT4 | 0.923 | 1.000 | 0.955 |

### Failure class distribution

| Rung | PASS | FORMAT_COMPLIANCE_LOSS | CONTENT_LOSS | COMPOUND_NOUN_DROP |
|---|---|---|---|---|
| FP16 | 92 | 0 | 0 | 0 |
| INT8 | 92 | 0 | 0 | 0 |
| INT4 | 88 | 1 | 3 | 0 |

---

## 7. Cross-calibration comparison — invariance gate

| Metric | Calib A (code) | Calib B (prose) | Invariant? |
|---|---|---|---|
| INT8 G_strict | +0.0000 [0.0, 0.0] | +0.0000 [0.0, 0.0] | **Y** |
| INT8 G_content | +0.0000 [0.0, 0.0] | +0.0000 [0.0, 0.0] | **Y** |
| INT4 G_strict | +0.0522 [−0.0878, +0.2778] | +0.0522 [−0.0878, +0.2778] | **Y** |
| INT4 G_content | +0.0689 [−0.0711, +0.2889] | +0.0689 [−0.0711, +0.2889] | **Y** |
| fmt_compliance narrow INT4 | 0.923 | 0.923 | **Y** |
| fmt_compliance broad INT4 | 1.000 | 1.000 | **Y** |
| fmt_compliance comps INT4 | 0.955 | 0.955 | **Y** |
| CONTENT_LOSS | 3 | 3 | **Y** |
| FORMAT_COMPLIANCE_LOSS | 1 | 1 | **Y** |

**Calibration-invariance gate: PASSED.** All metrics identical across both calibration runs. See §4 for provenance note.

---

## 8. Failure-class anatomy (INT4)

### FORMAT_COMPLIANCE_LOSS (1 item)

| Item | FP16/INT8 output | INT4 output | strict | content |
|---|---|---|---|---|
| FA3/comp[cabinet_tray] | `ANSWER: SILVTRAY` | `ANSWER: CABN3 stores SILVTRAY.` | 0 | 1 |

The forced-format instruction reduced FORMAT_COMPLIANCE_LOSS from 6 (Exp 4) to 1 (Exp 5). The single surviving case added a sentence wrapper around the correct value. The correct value SILVTRAY is present; only the format contract is violated.

### CONTENT_LOSS (3 items)

| Item | FP16/INT8 output | INT4 output | strict | content | Pattern |
|---|---|---|---|---|---|
| FA2/narrow | `ANSWER: ACTIVE` | `ANSWER: INACTIVE` | 0 | 0 | Wrong fact — semantic inversion |
| FC1/comp[panelB_door] | `ANSWER: DOOR6` | `ANSWER: PANELB` | 0 | 0 | Input echo — model answers with question entity, not answer entity |
| FD2/comp[labEpsilon_division] | `ANSWER: DIV3` | `ANSWER: LABEPS` | 0 | 0 | Input echo — same pattern |

Three distinct content failures at INT4:

**FA2/narrow (wrong fact):** Asked for the final status of Dex's chain. At FP16 and INT8: `ANSWER: ACTIVE`. At INT4: `ANSWER: INACTIVE`. The model knows the status class (ACTIVE/INACTIVE), flips the sign. All component checks for FA2 passed at INT4 — the individual hops are correct, but the composite answer is wrong. This is structurally the seam-hypothesis pattern (composite fails, components pass), but is a single item and the G_content CI includes zero.

**FC1/comp[panelB_door] and FD2/comp[labEpsilon_division] (input echo):** Both prompt-style failures follow the same pattern. The prompt asked "What does PANELB control?" and the model answered `ANSWER: PANELB` instead of `ANSWER: DOOR6`. The model echoed the entity it was asked about rather than retrieving the answer. This is a hop-resolution failure: the model retrieves the right edge of the graph but outputs the wrong endpoint.

### COMPOUND_NOUN_DROP (0 items)

No compound-noun drop observed. All values are single no-space tokens. The Exp 5 token redesign (SILVTOK, SILVDISK, etc.) eliminated this failure class as intended.

---

## 9. Primary comparison — Exp 4 vs. Exp 5

| Metric | Exp 4 (standard format) | Exp 5 (forced format) | Change |
|---|---|---|---|
| G_strict(INT4) CI | [−0.0926, −0.0123] **excludes zero** | [−0.0878, +0.2778] **includes zero** | Cliff disappeared |
| G_content(INT4) CI | [−0.0370, +0.0000] includes zero | [−0.0711, +0.2889] includes zero | Both flat |
| G_strict(INT4) point | −0.0494 | +0.0522 | Sign flipped, CI wide |
| G_content(INT4) point | −0.0123 | +0.0689 | Direction shifted, CI wide |
| fmt_compliance narrow INT4 | 0.917 | 0.923 | Slight improvement |
| fmt_compliance broad INT4 | 0.750 | 1.000 | Large improvement |
| fmt_compliance comps INT4 | 0.949 | 0.955 | Slight improvement |
| FORMAT_COMPLIANCE_LOSS | 6 | 1 | −5 items |
| CONTENT_LOSS | 0 | 3 | +3 items (new failure class) |
| COMPOUND_NOUN_DROP | 1 | 0 | Eliminated by token redesign |

The forced-format instruction substantially reduced format non-compliance (broad arm: 0.750 → 1.000; total FCL: 6 → 1). The aggregate strict-scoring cliff disappeared. However, 3 CONTENT_LOSS items appeared that were absent in Exp 4. These are not format artifacts — both strict and content scorers return 0 on them.

---

## 10. Outcome classification

| Outcome | Definition | Result |
|---|---|---|
| **F — cliff persists** | G_strict(INT4) CI excludes zero, same direction as Exp 4 | Not observed |
| **G — cliff disappears** | G_strict(INT4) CI includes zero | **Observed — calibration-invariant** |
| **H — content degrades** | G_content(INT4) CI excludes zero | Not observed (CI includes zero) |
| **B — baseline floor** | < 8 stable pairs | Not applicable (10 stable substantive pairs) |

**Final outcome: Outcome G — calibration-invariant format-cliff disappearance.**

> **Under a stronger explicit format instruction, the format cliff observed in Experiments 3 and 4 disappears. G_strict(INT4) CI includes zero. The Exp 4 cliff was scaffold-sensitive, not a fundamental style shift at INT4.**

---

## 11. What this run does not show

- That the format cliff is permanently gone — one scaffold change on one task family is local evidence.
- That INT4 is content-clean — 3 CONTENT_LOSS items appeared; content is not uniformly preserved.
- That the FA2 composite failure is a seam signal — it is a single item; G_content CI includes zero.
- That the input-echo failures (FC1/panelB_door, FD2/labEpsilon_division) are a replicable phenomenon — two items, no statistical power.
- That the calibration-invariance result reflects independent replication (see §4).
- That compression broke reasoning — the model answered most items correctly at every rung.
- That a stronger forced format is universally sufficient to eliminate format drift — FA3/cabinet_tray still added sentence context despite the instruction.

---

## 12. Claim-status update

**Primary seam claim (Test 1):** Not triggered. G_content(INT4) CI [−0.0711, +0.2889] includes zero. No statistically significant content-level gap between composite and component retention at any rung. The FA2 composite failure is noted as a candidate item but does not constitute a statistically significant seam signal.

**Format-degradation finding (Test 2):** Scaffold-sensitive. The Exp 3/4 format cliff disappears under a stronger explicit format instruction. Root cause is instruction-following degradation at INT4, not a logit-space style shift that is impervious to prompting. The format cliff is real but correctable via instruction engineering.

**New observation (not pre-registered as primary):** Three CONTENT_LOSS items at INT4 that were absent in Exp 4. These are genuine content errors (wrong fact, input echo), not format artifacts. They were not pre-registered as an expected finding. Their appearance does not constitute a content-degradation claim (G_content CI includes zero), but they are a pattern worth tracking:
  - 1 semantic inversion (ACTIVE → INACTIVE)
  - 2 input-echo hop failures (model outputs question entity rather than answer entity)

---

## 13. Ledger update

| Run | Model | Task family | Format instruction | G_strict INT4 CI | G_content INT4 CI | Outcome |
|---|---|---|---|---|---|---|
| Tier 0A–0C | 7B | 3–5-hop | standard | — | — | flat / task ceiling |
| Exp 2 | 7B | 6–7-hop | standard | — | [−0.061, 0.0] | flat / local null |
| Exp 3 | 1.5B | 6–7-hop | standard | — | [−0.093, −0.012] | Outcome C strict — dissolved by content rescore |
| Exp 4 (code) | 1.5B | 6–7-hop | `Reply with exactly: ANSWER:` | [−0.0926, −0.0123] | [−0.0370, +0.0000] | Outcome C — format cliff, content flat |
| Exp 4 (prose) | 1.5B | 6–7-hop | `Reply with exactly: ANSWER:` | [−0.0926, −0.0123] | [−0.0370, +0.0000] | Outcome C — format cliff, content flat |
| **Exp 5 (code)** | **1.5B** | **6–7-hop** | `Respond using only this exact format...` | **[−0.0878, +0.2778]** | **[−0.0711, +0.2889]** | **Outcome G — cliff disappears** |
| **Exp 5 (prose)** | **1.5B** | **6–7-hop** | `Respond using only this exact format...` | **[−0.0878, +0.2778]** | **[−0.0711, +0.2889]** | **Outcome G — cliff disappears** |

**Connection/continuity claim status:** Open. Not triggered across five experiments, two models.

**Format-degradation mechanism:** Locally resolved. The Exp 3/4 format cliff is scaffold-sensitive — a stronger explicit instruction eliminates it under this model and task family.

---

## 14. Next action

Experiment 5 closes the format-degradation question with a clear answer: the Exp 3/4 cliff is scaffold-sensitive. This is informative but local. The experiment also surfaced a new failure class (CONTENT_LOSS: wrong fact and input-echo) that was not present in Exp 4.

Options going forward:

**Option D — Harder seam tasks (Test 1):**
Return to the seam hypothesis with the dual scorer in place from the start. Tasks need: multi-step narrow and component arms with symmetric format pressure, short ALL-CAPS terminal values, explicit design to stress the composite→component difference. The FA2 composite failure in this experiment is a weak hint that the seam pattern can appear — it needs a task set designed to find it systematically.

**Option E — Replicate CONTENT_LOSS pattern:**
The input-echo failures (FC1/panelB_door, FD2/labEpsilon_division) and semantic inversion (FA2/narrow) at INT4 may be a new signal. Designing tasks specifically to stress mid-chain hop resolution could isolate whether this is a systematic effect or noise from two items. Requires pre-registration before building task file.

**Recommendation:** Option D. The seam hypothesis (Test 1) is the original research question and has not been formally tested with a well-designed dual-scorer instrument from the start. The Exp 3–5 sequence built the instrument and established that format artifacts are controllable with forced-format instructions. The scaffold for a proper seam test is now in place.
