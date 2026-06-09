# Experiment 2 — Results

*Filled: 2026-06-06. Results files: `results_code_1780744063.json`, `results_prose_1780744458.json`. FP16 screens: `results_baseline_check_exp2_1780743372.json` (v1), `results_baseline_check_exp2_v2_1780743894.json` (v2).*

---

## 0. Run header

| Field | Value |
|---|---|
| Date | 2026-06-06 |
| Model | `Qwen/Qwen2.5-7B-Instruct` |
| Quantization | FP16 baseline; INT8 in-place (group_size=64); INT4 from `mlx-community/Qwen2.5-7B-Instruct-4bit` |
| Bit-depths swept | FP16, INT8, INT4 |
| Task file | `tasks_exp2.py` |
| Calibration A | `code` |
| Calibration B | `prose` |
| Total pairs in tasks_exp2.py | 22 |
| Eligible for ΔR / G(w) | 15 (12 substantive + 3 controls) |
| Ineligible (FP16 failure) | 7: FA1, FA3, FB2, FC1, FE1, FE2, FE3 |
| Bootstrap iterations | 1000, seed=0 |
| Hardware | Apple Silicon (MLX, macOS 15+) |
| Decoding | temperature=0.0 (greedy, deterministic) |
| Max tokens | 512 |
| Pre-registered | **Y** — `PREREGISTRATION-EXP2.md` locked before FP16 screen |

---

## 1. FP16 eligibility screen

**Eligibility criteria (per pre-registration):** composite narrow = 1.0, all components ≥ 0.5, broad ≥ 0.5.

**Two FP16 screens run:** v1 revealed systematic scoring errors (compound-noun expected-answer mismatches, negation-bleed in FB distractors). Fixed in `tasks_exp2.py` before v2. No model was re-run; only expected answers and distractor text were corrected to match actual model output patterns.

### Eligible pairs (15)

| Family | Pairs |
|---|---|
| A (6-hop clean) | FA2, FA4 |
| B (6-hop + distractor + negation) | FB1, FB3, FB4 |
| C (7-hop role-swap) | FC2, FC3, FC4 |
| D (trap + distractor) | FD1, FD2, FD3, FD4 |
| Controls | AC1, AC2, NC1 |

### Ineligible pairs (7) and reasons

| Pair | Reason | Notes |
|---|---|---|
| FA1 | Narrow = 0.00 at FP16 — capability floor | All 6 components pass at FP16. INT4 recovers to 1.00 (greedy path artifact). |
| FA3 | Narrow = 0.00 at FP16 — capability floor | Same pattern as FA1. Recovers at INT4. |
| FB2 | Narrow = 0.00 at FP16; shelf_block comp context-dependent | FA2/narrow passes; FB2 distractor still confuses even after rephrasing. shelf_block expected answer flips (FA2: "the jade block"; FB2: "jade block") — same context-dependence as Exp 1 LB2/LC2. |
| FC1 | Narrow = 0.00 at FP16 — capability floor | 7-hop dual chain; model cannot link Nalo to CYAN at FP16 via greedy decoding. Recovers at INT4. |
| FE1 | Narrow = 0.00 at all rungs | Arithmetic capability floor; multi-step computation fails even though each step passes independently. Persistent at INT4. |
| FE2 | Narrow = 0.00 at all rungs | Same as FE1. |
| FE3 | Narrow = 0.00 at all rungs | Same as FE1. |

---

## 2. Primary readout — G(w) and ΔR

### Calibration A (code) — `results_code_1780744063.json`

**ΔR:**

| Bit-depth | mean R_broad | mean R_narrow | ΔR | bootstrap 95% CI | Outcome |
|---|---|---|---|---|---|
| INT8 | 1.0000 | 1.0000 | 0.0000 | [0.0, 0.0] | flat |
| INT4 | 1.0000 | 1.0000 | 0.0000 | [0.0, 0.0] | flat |

**G(w) per eligible pair:**

| Pair | G(INT8) | G(INT4) | Component events |
|---|---|---|---|
| FA2 | 0.0000 | 0.0000 | — |
| FA4 | 0.0000 | 0.0000 | — |
| FB1 | 0.0000 | 0.0000 | — |
| FB3 | 0.0000 | 0.0000 | — |
| FB4 | 0.0000 | 0.0000 | — |
| FC2 | 0.0000 | −0.1111 | zone2_module: 1.0→1.0→0.0 @ INT4 (composite stays 1.0) |
| FC3 | 0.0000 | 0.0000 | — |
| FC4 | 0.0000 | 0.0000 | — |
| FD1 | 0.0000 | 0.0000 | — |
| FD2 | 0.0000 | 0.0000 | — |
| FD3 | 0.0000 | 0.0000 | — |
| FD4 | 0.0000 | −0.2000 | maya_path: 1.0→1.0→0.0 @ INT4 (composite stays 1.0) |
| AC1–NC1 | N/A (no comps) | N/A | — |

**Mean G(w) bootstrap CI:**

| Rung | Mean G(w) | 95% CI | Outcome |
|---|---|---|---|
| INT8 | 0.0000 | [0.0000, 0.0000] | flat |
| INT4 | −0.0259 | [−0.0611, 0.0000] | flat (CI includes zero; upper bound = 0) |

**Kill condition met:** G(w) CI includes zero at both rungs. Seam signal not observed.

### Calibration B (prose) — `results_prose_1780744458.json`

**Identical to Calibration A** — every pair-level score, every component score, and every G(w) value matched exactly. Runs are deterministic (temp=0, same quantization weights).

### Cross-calibration invariance gate

| | Calibration A (code) | Calibration B (prose) | Invariant? |
|---|---|---|---|
| INT8 ΔR | 0.0000, CI [0.0, 0.0] | 0.0000, CI [0.0, 0.0] | **Y** |
| INT4 ΔR | 0.0000, CI [0.0, 0.0] | 0.0000, CI [0.0, 0.0] | **Y** |
| INT8 mean G(w) | 0.0000, CI [0.0, 0.0] | 0.0000, CI [0.0, 0.0] | **Y** |
| INT4 mean G(w) | −0.0259, CI [−0.0611, 0.0] | −0.0259, CI [−0.0611, 0.0] | **Y** |
| Pair-level rankings | all flat | all flat | **Y** |
| Component noise pattern | FC2/zone2_module@4b=0.0, FD4/maya_path@4b=0.0 | identical | **Y** |

**Calibration-invariance gate: PASSED.**

---

## 3. Outcome classification

| Outcome | Definition | Count |
|---|---|---|
| **A — seam signal** | G(w) CI excludes zero, calibration-invariant | 0 |
| **B — metric artifact** | Gap dissolves under scoring symmetry | 0 |
| **C — task/pair confound** | Gap traced to difficulty or length mismatch | 0 |
| **D — calibrated local null** | G(w) CI overlaps zero at all rungs, both calibrations | 12/12 |
| **robust-wrong flag** | Baseline wrong, high retention, same wrong answer | 0 |

**Final outcome: Outcome D — calibrated local null.**

The 7B model navigated 6-hop chains with distractors and negation, 7-hop dual-chain role-swap items, and intermediate-value trap tasks without composite degradation at INT8 or INT4. Every narrow arm that passed FP16 remained correct at INT4. G(w) ≤ 0 at all pairs and both rungs — no pair showed composite degradation with component preservation.

> **The harder task families did not enter the 7B model's fragility band under the tested stress profile.**

---

## 4. Diagnostic observations

### 4a. Inverse-seam pattern at INT4 (component drops, composite holds)

Two eligible pairs showed component-level degradation at INT4 while their composite narrow arm remained correct:

| Pair | Component | 16b | 8b | 4b | Composite narrow at 4b |
|---|---|---|---|---|---|
| FC2 | zone2_module | 1.0 | 1.0 | 0.0 | 1.0 |
| FD4 | maya_path | 1.0 | 1.0 | 0.0 | 1.0 |

Classification: inverse seam (G(w) < 0, not > 0). The composite answer is more robust than one of its components. This is not the target signal. Single items, non-replicated.

### 4b. FP16-floor recovery at INT4 (quantization improves greedy path)

Four items that failed the FP16 eligibility screen (narrow=0) recovered to narrow=1.0 at INT4:

| Pair | Narrow @ 16b | Narrow @ 8b | Narrow @ 4b | Components @ 16b |
|---|---|---|---|---|
| FA1 | 0.0 | 0.0 | 1.0 | all 1.0 |
| FA3 | 0.0 | 0.0 | 1.0 | all 1.0 |
| FB2 | 0.0 | 0.0 | 1.0 | all 1.0 (narrow fails due to distractor) |
| FC1 | 0.0 | 0.0 | 1.0 | 7/9 = 1.0 (2 name-type comps fail) |

**Interpretation:** Greedy decoding is sensitive to small logit perturbations. INT4 quantization noise shifts the probability landscape enough that these specific chain-traversal prompts take a different (correct) decoding path. This is not a reliability improvement — re-running at different seeds would not be deterministic. These items were appropriately excluded from ΔR and G(w) computation (NaN baseline).

**This is not evidence for INT4 superiority.** It is evidence that greedy decoding at temperature=0 can produce non-monotonic accuracy profiles across bit-depths for items near the capability boundary.

### 4c. FE items — persistent capability floor, not compression

FE1, FE2, FE3: arithmetic multi-step fails at FP16, INT8, and INT4 identically (same wrong answer at each rung). Each individual arithmetic step (component check) passes at all rungs. This is a capability floor for end-to-end arithmetic composition, independent of quantization.

Contrast with FA1/FA3/FC1 (4b recovery): those items' answers changed between rungs. FE items' answers did not change — the model consistently produces the same wrong answer regardless of bit-depth. This is the more typical capability floor pattern.

---

## 5. Error-source ledger

| Task | Effect | Probe | Plausible source | Evidence |
|---|---|---|---|---|
| FC2/zone2_module | Monotonic component degradation at INT4 (1.0→1.0→0.0); composite unaffected | Component check isolated | INT4 disrupts "Which zone does Hub 5 connect to?" in dual-chain context but not the full chain traversal | low — single item |
| FD4/maya_path | Monotonic component degradation at INT4 (1.0→1.0→0.0); composite unaffected | Component check isolated | INT4 changes "Which path is Maya assigned to?" answer in trap+distractor context | low — single item |
| FA1, FA3/narrow | Capability floor at FP16/INT8; recovers at INT4 | Component checks pass at all rungs | Greedy path artifact — INT4 logit shift produces correct answer; not a stable improvement | medium — deterministic, consistent across calibrations |
| FC1/narrow | Same FP16 floor / INT4 recovery | Components mostly pass (2 name-type fails) | Same greedy path artifact | medium — consistent |
| FE1–3/narrow | Persistent failure at all rungs; same wrong answer | Component checks all pass at all rungs | End-to-end arithmetic composition is below 7B capability regardless of bit-depth | high — stable, wrong answer unchanged |
| FB2/shelf_block | Context-dependent compound noun (FA2: "the jade block"; FB2: "jade block") | Same question, different distractor context | Distractor presence shifts article usage in model output for compound objects | medium — mirrors Exp 1 LB2/LC2 pattern |

---

## 6. Run family summary — full ledger to date

| Run | Model | Calib | Eligible pairs | INT8 ΔR | INT4 ΔR | INT8 G(w) | INT4 G(w) | Outcome |
|---|---|---|---|---|---|---|---|---|
| Tier 0A | Qwen2.5-7B | code | 5 | 0.0 | 0.0 | — | — | flat / task ceiling |
| Tier 0B | Qwen2.5-1.5B | code | 3 | 0.0 | 0.0 | — | — | flat / task ceiling |
| Tier 0C (code) | Qwen2.5-7B | code | 17 | −0.0196 | 0.0 | — | — | flat / task ceiling |
| Tier 0C (prose) | Qwen2.5-7B | prose | 17 | −0.0196 | 0.0 | — | — | flat / task ceiling |
| Exp 2 (code) | Qwen2.5-7B | code | 15 | 0.0 | 0.0 | 0.0 | −0.0259 | flat / local null |
| Exp 2 (prose) | Qwen2.5-7B | prose | 15 | 0.0 | 0.0 | 0.0 | −0.0259 | flat / local null |

G(w) not tracked in Tier 0A/0B/0C (pre-dated the primary readout definition).

---

## 7. Ledger update

**Connection/continuity claim status:** open / not promoted / not demoted.

**Reason:** Two calibration-invariant flat experiments on the 7B model with progressively harder tasks. Neither ΔR nor G(w) showed a positive signal at any rung or calibration. The 7B model correctly retrieves terminal values for 6- and 7-hop chains, dual-chain role-swaps, and trap+distractor items under INT4.

**Demotion condition not met:** the flat result is still attributable to task ceiling (model solves even the harder chains at FP16 and retains them under compression), not to demonstrated component/composite parity under stress. We haven't yet found a task family that enters the stress band.

---

## 8. What this run validates

1. G(w) = R_component − R_composite is computable from existing harness output.
2. The seam-fragility pattern (G(w) > 0, calibration-invariant) did not appear in this task family.
3. The inverse pattern (G(w) < 0: component drops, composite holds) appeared at two pairs at INT4.
4. Calibration-invariance gate passed for both primary readouts.
5. The FP16-floor / INT4-recovery pattern is real, consistent, and limited to items near the FP16 capability boundary.

---

## 9. What this run does not show

- That chain-boundary fragility does not exist under any quantization scheme.
- That 7-hop chains are universally robust at INT4.
- That the model never makes seam errors — only that it didn't on these specific tasks.
- That the INT4-recovery items represent a stable improvement — they represent a greedy-path sensitivity artifact.

Mechanism remains blocked. Behavioral measurement only.

---

## 10. Next action

The 7B model has cleared two progressively harder task ladders. Two options:

**Option A — Push 7B harder:**
- 8–9 hop chains
- Cross-domain property chains (hop 1 in access-control domain, hop 4 in spatial domain, terminal in numeric domain)
- Binding interference: multiple chains with shared intermediate values but different terminals
- Adversarial surface similarity: distractor shares surface features with correct chain at 3+ positions

**Option B — Try the same tasks on a smaller model:**
- Qwen2.5-1.5B on the Exp 2 task family (Tier 0B used 3 pairs; Exp 2 has 12 substantive)
- Smaller model may have a lower ceiling and enter the fragility band on 6-hop chains
- Risk: FP16 eligibility screen may exclude too many pairs (smaller model may not pass the chains at FP16 at all)

**Option C — Target arithmetic chains specifically:**
- FE items showed the exact seam pattern at FP16: components pass, composite fails
- This is a capability floor, not compression — but a smaller model with arithmetic capability at the component level but not chain level could show compression-induced seam fragility if the FP16 composite barely passes
- Design: simpler arithmetic chains that a 1.5B can do in one shot at FP16 but that INT4 breaks

The most tractable path for finding a positive G(w) signal is Option C or Option B with the 1.5B — the 7B is simply too capable for the current task designs.
