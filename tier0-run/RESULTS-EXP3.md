# Experiment 3 — Results

*Filled: 2026-06-06. Results files: `results_code_1780745541.json`, `results_prose_1780745788.json`. Stability screen: `stability_screen_1780745371.json`. Filtered tasks: `tasks_exp3.py`.*

---

## 0. Run header

| Field | Value |
|---|---|
| Date | 2026-06-06 |
| Model | `Qwen/Qwen2.5-1.5B-Instruct` |
| Quantization | FP16 baseline; INT8 in-place (group_size=64); INT4 from `mlx-community/Qwen2.5-1.5B-Instruct-4bit` |
| Bit-depths swept | FP16, INT8, INT4 |
| Task file | `tasks_exp3.py` (filtered from `tasks_exp2.py` by stability screen) |
| Calibration A | `code` |
| Calibration B | `prose` |
| Total pairs in tasks_exp3.py | 12 (9 substantive + 3 controls) |
| Stability screen | `run_stability_screen.py` — original + paraphrase both must pass FP16 |
| Hardware | Apple Silicon (MLX, macOS 15+) |
| Decoding | temperature=0.0 (greedy, deterministic) |
| Max tokens | 512 |
| Pre-registered | **Y** — `PREREGISTRATION-EXP3.md` locked before stability screen |

---

## 1. Stability screen results

**Protocol:** Each narrow arm run at FP16 with original prompt AND paraphrase ("Reply with exactly: ANSWER:" → "Answer using this format: ANSWER:"). Both must score 1.0. Component checks and broad arm scored on original prompt only (≥ 0.5 required).

| Classification | Count | IDs |
|---|---|---|
| STABLE | 12 | FA1, FA4, FB1, FB4, FC1, FC4, FD1, FD2, FD4, AC1, AC2, NC1 |
| BOUNDARY | 0 | — |
| COMP_FAIL | 3 | FB3, FC2, FC3 |
| FLOOR | 7 | FA2, FA3, FB2, FD3, FE1, FE2, FE3 |

**Stable substantive pairs: 9** (FA1, FA4, FB1, FB4, FC1, FC4, FD1, FD2, FD4). Threshold met (≥ 8).

**No BOUNDARY items** — the 1.5B has a clean boundary. Every pair either passes both phrasings or fails the original. No coin-flip items.

### Notable stability screen observations

**1. Model inversion (7B vs 1.5B):**  
FA1 and FC1 were FP16 capability floor items for the 7B in Experiment 2 (needed INT4 greedy-path recovery to produce the correct answer). The 1.5B solves both stably at FP16 under both phrasings. The models are differently situated relative to these task families — larger is not uniformly more capable here.

**2. COMP_FAIL items are scoring artifacts, not genuine failures:**  
- FB3/sector_cabinet: 1.5B outputs "cabinet" (correct concept, drops the number "3")
- FC2/zone2_module: 1.5B outputs "module" (correct concept, drops "alpha")
- FC3/revi_pass: 1.5B outputs "jade" (correct concept, drops "pass")  
All are the same compound-noun truncation pattern documented in Experiments 1 and 2. Excluded per pre-registration (COMP_FAIL classification); sufficient substantive pairs remain.

**3. FD3 negation sensitivity:**  
FD3/narrow original: "ANSWER: OFF" (wrong — distractor trap triggered); paraphrase: "ANSWER: ON" (correct). Answer is sensitive to instruction phrasing. Correctly excluded as FLOOR. This is the strongest evidence yet that the "Reply with exactly:" phrasing interacts with distractor content in the 1.5B.

---

## 2. Primary readout — G(w) and ΔR

### Calibration A (code) — `results_code_1780745541.json`

**ΔR:**

| Bit-depth | mean R_broad | mean R_narrow | ΔR | bootstrap 95% CI | Outcome |
|---|---|---|---|---|---|
| INT8 | 0.9167 | 0.9167 | 0.0000 | [0.0, 0.0] | flat |
| INT4 | 0.7500 | 0.9167 | −0.1667 | [−0.4167, 0.0] | flat (CI includes zero) |

**G(w) per eligible pair:**

| Pair | G(INT8) | G(INT4) | Component events |
|---|---|---|---|
| FA1 | 0.0000 | −0.1667 | box_file: 1.0→1.0→0.0 @ INT4 (format verbosity) |
| FA4 | 0.0000 | −0.1667 | drawer_log: 1.0→1.0→0.0 @ INT4 (format verbosity) |
| FB1 | 0.0000 | 0.0000 | — |
| FB4 | 0.0000 | 0.0000 | — |
| FC1 | 0.0000 | −0.1111 | vault3_token: 1.0→1.0→0.0 @ INT4 (compound-noun drop) |
| FC4 | 0.0000 | 0.0000 | — |
| FD1 | 0.0000 | 0.0000 | — |
| FD2 | 0.0000 | 0.0000 | — |
| FD4 | 0.0000 | 0.0000 | — |
| AC1–NC1 | N/A | N/A | — |

**Mean G(w) bootstrap CI:**

| Rung | Mean G(w) | 95% CI | Outcome |
|---|---|---|---|
| INT8 | 0.0000 | [0.0000, 0.0000] | flat |
| INT4 | −0.0494 | [−0.0926, −0.0123] | **CI excludes zero — inverse seam (Outcome C)** |

**Outcome C confirmed.** G(4b) CI [−0.0926, −0.0123] has both bounds negative. Component retention drops below composite retention at INT4, with statistical confidence. The direction is the inverse of the seam signal.

---

## 3. Failure anatomy — format compliance degradation

All score drops in this run share a single root cause: **the 1.5B model stops following the exact-format instruction under quantization, specifically for short-context prompts.**

| Item | Prompt type | FP16/INT8 output | INT4 (or INT8) output | Score |
|---|---|---|---|---|
| FA1/box_file | Component — "What does the amber box store?" | `ANSWER: File K` | `ANSWER: amber box stores File K.` | 0 |
| FA4/drawer_log | Component — "What does the obsidian drawer store?" | `ANSWER: Log 3` | `ANSWER: obsidian drawer stores Log 3` | 0 |
| FA1/broad | "What does the amber box store?" | `ANSWER: File K` | `ANSWER: amber box stores File K.` | 0 |
| FA4/broad | "What does the obsidian drawer store?" | `ANSWER: Log 3` | `ANSWER: obsidian drawer stores Log 3` | 0 |
| FC1/vault3_token | Component — "What does Vault 3 hold?" | `ANSWER: silver token` | `ANSWER: token` | 0 |
| AC1 (both arms) | Atomic 1-hop — "What does the blue locker contain?" | `ANSWER: silver disk` | `ANSWER: The blue locker contains the silver disk.` | 0 |

**Pattern:**
- The model knows the correct fact at all rungs — it includes the answer in its output at every rung
- Under quantization, it adds surrounding context ("amber box stores") or a full sentence ("The blue locker contains the silver disk.")
- The exact-match scorer requires the ANSWER tag immediately followed by the item; a longer answer fails even if the item is present

**This is format compliance degradation, not factual degradation.**

The content is correct; the format instruction ("Reply with exactly: ANSWER: <item>") is being ignored under quantization for short-context prompts.

### Why short-context prompts degrade but long-context chains do not

All 9 narrow arm chain questions (FA1–FD4) produce clean format-compliant answers at INT4: `ANSWER: APPROVED`, `ANSWER: CLEAR`, `ANSWER: CYAN`, etc. The hard 6–7 hop questions survive.

The degrading items all involve prompts where a single short fact is in context and the question asks directly about it — the classic "look this up and repeat it" format. For these, the model at INT4 produces a sentence rather than a clipped value.

**Proposed mechanism:** The long chain context (8–16 sentences of closed-world facts) strongly primes the model toward the structured `ANSWER: <VALUE>` format — the terminal value of a chain is the only free slot in a heavily constrained prompt. For short-context prompts (1–3 sentences), the model has more freedom to produce natural language, and quantization-induced logit perturbation at INT4 pushes it toward sentence completion rather than the clipped format.

This is a behavioral observation. The mechanism is not confirmed.

### The AC1 finding — format compliance fails at INT8

AC1 (atomic 1-hop control) fails at INT8, not just INT4:
- FP16: `ANSWER: silver disk` ✓
- INT8: `ANSWER: The blue locker contains the silver disk.` ✗
- INT4: same full sentence ✗

This is qualitatively different from the chain question behavior (which survives INT4 clean). The 1.5B model's format compliance threshold on short-context prompts is somewhere between FP16 and INT8 — a lower quantization stress level than any of the compositional tasks.

---

## 4. Outcome classification

| Outcome | Definition | Result |
|---|---|---|
| **A — seam candidate** | G(w) CI lower bound > 0, calibration-invariant | Not observed |
| **B — baseline floor** | < 8 stable substantive pairs | Not observed (9 stable pairs) |
| **C — inverse seam** | G(w) CI upper bound < 0 — component drops, composite holds | **Observed. G(4b) CI [−0.0926, −0.0123]. Outcome C.** |
| **D — flat** | G(w) CI overlaps zero | Not the outcome at INT4 |

**Final outcome: Outcome C — statistically significant inverse seam.**

The direction of fragility is the inverse of the seam hypothesis: composites are MORE robust than components under INT4 compression. The 6–7 hop chain answer (narrow arm) survives intact; simpler direct-retrieval questions lose format compliance.

> **The 1.5B model at INT4 is more reliably correct on the hard question than on the easy one.**

---

## 5. What this run validates

1. Margin-aware stability screening works — the paraphrase filter caught no BOUNDARY items for 1.5B on these tasks, confirming the model has a clean ceiling (pass/fail, not coin-flip).
2. G(w) < 0 with CI excluding zero is statistically detectable.
3. Format compliance is a distinct failure mode from factual recall under quantization.
4. The inverse seam is real and reproducible (all failures share a single mechanism).
5. The AC1 atomic control failure at INT8 sets the format compliance threshold for this model on short-context prompts — below INT8.

---

## 6. What this run does not show

- That composite answers are generally more robust than components under quantization.
- That the 1.5B cannot be broken on compositional tasks — only that these specific task families do not break it at INT8 or INT4.
- That format compliance is the only failure mode under quantization for 1.5B.
- That the mechanism (long context anchors format compliance) is correct — it is a post-hoc observation, not a controlled test.

---

## 7. Calibration-invariance check

Results file: `results_prose_1780745788.json`

| | Calibration A (code) | Calibration B (prose) | Invariant? |
|---|---|---|---|
| INT8 ΔR | 0.0000, CI [0.0, 0.0] | 0.0000, CI [0.0, 0.0] | **Y** |
| INT4 ΔR | −0.1667, CI [−0.417, 0.0] | −0.1667, CI [−0.417, 0.0] | **Y** |
| INT8 mean G(w) | 0.0000, CI [0.0, 0.0] | 0.0000, CI [0.0, 0.0] | **Y** |
| INT4 mean G(w) | −0.0494, CI [−0.093, −0.012] | −0.0494, CI [−0.093, −0.012] | **Y** |
| Pair-level scores | all identical | all identical | **Y** |
| Component noise pattern | FA1/box_file@4b=0, FA4/drawer_log@4b=0, FC1/vault3_token@4b=0, AC1@8b+4b=0 | identical | **Y** |

**Calibration-invariance gate: PASSED.** Bit-for-bit identical across both calibration labels.

---

## 8. Run family summary — full ledger to date

| Run | Model | Task family | Eligible pairs | INT8 G(w) CI | INT4 G(w) CI | Outcome |
|---|---|---|---|---|---|---|
| Tier 0A | 7B | 3-hop | 5 | — | — | flat / task ceiling |
| Tier 0B | 1.5B | 3-hop | 3 | — | — | flat / task ceiling |
| Tier 0C (code) | 7B | 5-hop | 17 | — | — | flat / task ceiling |
| Tier 0C (prose) | 7B | 5-hop | 17 | — | — | flat / task ceiling |
| Exp 2 (code) | 7B | 6–7-hop | 15 | [0.0, 0.0] | [−0.061, 0.0] | flat / local null |
| Exp 2 (prose) | 7B | 6–7-hop | 15 | [0.0, 0.0] | [−0.061, 0.0] | flat / local null |
| Exp 3 (code) | 1.5B | 6–7-hop | 12 | [0.0, 0.0] | **[−0.093, −0.012]** | **Outcome C — inverse seam** |
| Exp 3 (prose) | 1.5B | 6–7-hop | 12 | [0.0, 0.0] | **[−0.093, −0.012]** | **Outcome C — inverse seam** |

G(w) not tracked in Tier 0A/0B/0C (pre-dated the primary readout).

---

## 9. Ledger update

**Connection/continuity claim status:** open / not promoted / not demoted.

**Reason:** Experiment 3 under strict scoring produced a statistically significant inverse seam (Outcome C). Option A content rescore (Section 10) confirmed this is a format compliance artifact — under content-aware scoring the signal collapses to flat (CI includes zero). The factual content is retained at all rungs for all items except a single compound-noun adjective drop (FC1/vault3_token at INT4: "silver token" → "token").

The positive seam signal (G(w) > 0: composite degrades, components hold) has not appeared in any run across three experiments, two models, multiple task families, and multiple bit-depths.

**What would change the ledger:**
- A task family where the composite narrow answer degrades at INT4 while the component checks remain correct, under content-aware scoring
- Currently all component degradation (when present) traces to format compliance failures on short-context prompts or compound-noun truncation; the full-chain answer remains intact

---

## 10. Option A — Lenient content rescore

**Executed:** 2026-06-06, after full strict-scoring sweep.

**Question:** Is the inverse seam (G(w) < 0, CI excludes zero) a format compliance artifact or genuine factual loss under INT4?

### Methodology

Content scorer extracts the expected value (everything after `"ANSWER:"` in the expected answer string), normalizes via `re.sub(r'[^a-z0-9\s]', '', s.lower()).strip()`, and checks whether that value appears anywhere in the normalized model output. A strict failure that recovers under content scoring = the model knew the fact but didn't follow the format instruction.

### Items where strict ≠ content

| Item | Rung | Strict | Content | Strict output |
|---|---|---|---|---|
| FA1/box_file | INT4 | 0 | 1 | `amber box stores File K.` |
| FA1/broad | INT4 | 0 | 1 | `amber box stores File K.` |
| FA4/drawer_log | INT4 | 0 | 1 | `obsidian drawer stores Log 3` |
| FA4/broad | INT4 | 0 | 1 | `obsidian drawer stores Log 3` |
| AC1/narrow | INT8 | 0 | 1 | `The blue locker contains the silver disk.` |
| AC1/narrow | INT4 | 0 | 1 | `The blue locker contains the silver disk.` |
| AC1/broad | INT8 | 0 | 1 | `The blue locker contains the silver disk.` |
| AC1/broad | INT4 | 0 | 1 | `The blue locker contains the silver disk.` |

**FC1/vault3_token does NOT recover:** strict output at INT4 is `ANSWER: token`; expected value is `silver token`; `token` appears in `silver token` but `silver token` does not appear in `token`. This is a genuine compound-noun content drop — the model drops the adjective "silver" at INT4.

### G(w) comparison — strict vs content scoring

| Rung | Scoring | Mean G(w) | 95% CI | Outcome |
|---|---|---|---|---|
| INT8 | strict | 0.0000 | [0.0000, 0.0000] | flat |
| INT8 | content | 0.0000 | [0.0000, 0.0000] | flat |
| INT4 | strict | −0.0494 | [−0.0926, −0.0123] | **Outcome C (CI excludes zero)** |
| INT4 | content | −0.0123 | [−0.0370, 0.0000] | **flat (CI includes zero)** |

### Verdict

**The inverse seam is a format compliance artifact.**

Under content scoring, G(4b) CI [−0.0370, 0.0000] includes zero. The strict Outcome C signal collapses entirely when scoring asks whether the model *knows* the answer rather than whether it *formatted* the answer correctly.

The sole genuine content event is FC1/vault3_token at INT4: model outputs `token` when the answer is `silver token` — a compound-noun adjective drop. This is a single item and insufficient to produce a statistically significant G(w) signal on its own.

**Revised outcome classification:**

| Scoring mode | G(4b) CI | Outcome |
|---|---|---|
| Strict (pre-registered) | [−0.0926, −0.0123] | C — inverse seam |
| Content (Option A rescore) | [−0.0370, 0.0000] | D — flat / format artifact |

**The factual content is retained at INT4 for all items except FC1/vault3_token (single compound-noun adjective drop). No seam signal of any direction survives content-aware scoring.**

---

## 12. Next Action — Updated After Option A Rescore

Option A has now been run. The strict-scoring inverse seam did not survive content scoring.

### Final readout

Under pre-registered strict scoring:

* `G(INT4) = −0.0494`
* `CI95 = [−0.0926, −0.0123]`
* Classification: inverse seam under strict scoring

Under Option A content scoring:

* `G(INT4) = −0.0123`
* `CI95 = [−0.0370, 0.0000]`
* Classification: flat / not significant

### Interpretation

The Experiment 3 inverse seam was a format-compliance artifact.

At INT4, Qwen2.5-1.5B generally retained the target content but sometimes violated the required clipped answer format on short-context prompts. The failing outputs often contained the correct answer embedded in a sentence rather than returned as the required exact value.

Therefore, the strict-scoring inverse seam should not be interpreted as component degradation or as evidence against the compositional-seam hypothesis.

### Item-level note

The only genuine content-level event was `FC1/vault3_token`, where the model dropped the adjective in the compound noun:

* expected: `silver token`
* output: `token`

This is logged as a single compound-noun adjective drop. It is not sufficient to support a content-level inverse-seam claim.

### Claim status

The primary connection/continuity claim is not triggered.

Experiment 3 does not show:

* composite degradation with components preserved,
* content-level component degradation relative to composites,
* or robust-wrong behavior.

Experiment 3 does show:

* strict-format fragility on short-context prompts under INT4,
* content retention despite format violation,
* and the value of scoring-layer separation.

### Ledger update

Record Experiment 3 as:

> Outcome C — strict-scoring inverse seam dissolved under content rescore. Final classification: format-compliance artifact. Primary seam claim remains open and unpromoted. The run validates the scoring-layer guard by showing that strict exact-match scoring can manufacture an apparent retention gap that content scoring removes.

### Historical decision point

Before Option A was run, the next-action section listed Options A–D. That decision point is retained here historically, but it is now resolved.

* Option A — lenient/content rescore: completed.
* Result: strict inverse seam dissolved.
* Options B–D are no longer immediate next steps for this result.

### Next experimental action

Do not proceed directly to a new model run based on the strict inverse seam.

The next build should harden scoring symmetry before further stress testing:

1. Add dual scoring to every item:

   * strict canonical format score,
   * content/slot score.

2. Separate failure classes explicitly:

   * content loss,
   * format-compliance loss,
   * compound-noun modifier loss,
   * component failure,
   * composite failure.

3. Redesign short-context controls so their output contract is comparable to long-chain prompts.

4. Re-run only after the scorer distinguishes:

   * "answer content absent"
   * from "answer content present but formatted incorrectly."

The immediate lesson from Experiment 3 is not that components are less robust than composites. The lesson is that exact-format scoring can create an apparent inverse seam when compression perturbs output style while preserving answer content.
