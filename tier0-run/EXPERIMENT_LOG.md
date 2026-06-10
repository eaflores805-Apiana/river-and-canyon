# EXPERIMENT LOG — LLM Quantization Seam Fragility Research

**Last updated:** 2026-06-09  
**Research question:** Does INT4 quantization cause compositional seam fragility — do individual hop-facts (components) survive while the linked composite answer fails?  
**Primary claim (Test 1):** Open. Not triggered across eight experiments, two models.  
**Secondary finding (Test 2):** Resolved. The Exp 3/4 format cliff is scaffold-sensitive — a stronger explicit instruction eliminates it.

---

## How to read this log

Each section covers one experiment: what was tested, what happened, what it means, and what changed going forward. Numbers in brackets are 95% confidence intervals. "G" is the gap metric: G = component_retention − composite_retention, computed over substantive pairs only. A positive G means composites degrade more than components — the seam-fragility pattern.

**Outcome codes:**
- **A** — Seam candidate: G_content CI lower bound > 0, calibration-invariant
- **B** — Baseline floor: fewer than 8 stable pairs
- **C** — Format cliff: G_strict CI excludes zero, G_content CI includes zero
- **D** — Flat / local null: both G metric CIs overlap zero
- **E** — Task failure: stability gate not met before stress sweep
- **F** — Cliff persists under forced format
- **G** — Cliff disappears under forced format

---

## Tier 0 (Experiments A, B, C)

**Model:** Qwen2.5-7B-Instruct (A, C) / Qwen2.5-1.5B-Instruct (B)  
**Task family:** 3-hop (A, B) and 5-hop (C) multi-step chains  
**Scorer:** Strict format only (dual scorer not yet built)  
**Outcome:** Flat / task ceiling across all three rungs

### What was tested
Early feasibility runs to verify the measurement infrastructure and establish whether short-to-medium hop chains show any quantization sensitivity at all.

### What happened
No statistically significant gap between component and composite retention at any bit depth. Both 7B and 1.5B models, both 3-hop and 5-hop tasks, produced flat G metrics. Task performance on 3-hop chains was high enough at FP16 that there was little room to detect degradation — a ceiling effect.

### What it means
Short chains are not the right stress test. The model handles them well even at INT4. The seam hypothesis requires harder tasks. Longer chains needed.

### What changed
Moved to 6–7 hop tasks in Exp 2 to escape the ceiling effect.

---

## Experiment 2

**Model:** Qwen2.5-7B-Instruct  
**Task family:** 6–7 hop multi-step chains  
**Scorer:** Strict format only  
**Outcome: D — Flat / local null**  
**Result files:** `results_baseline_check_exp2_1780743372.json`, `results_baseline_check_exp2_v2_1780743894.json`  
**Pre-registration:** `PREREGISTRATION-EXP2.md`

### What was tested
Whether a larger model (7B) on longer chains (6–7 hops) shows composite-vs-component degradation under INT4.

### What happened

| Rung | G(INT4) | 95% CI | Outcome |
|---|---|---|---|
| INT4 | −0.0259 | [−0.0611, 0.0000] | includes zero |

CI includes zero. No significant gap. The 7B model retained both composite and component answers well across all bit depths.

### What it means
The 7B model is robust on 6–7 hop tasks. Either the model is too large to show the effect, or the task family does not stress the seam adequately. Switched to the smaller 1.5B model for Exp 3 to increase quantization sensitivity.

### What changed
Dropped model size to 1.5B. Kept 6–7 hop task family. Kept strict scorer.

---

## Experiment 3

**Model:** Qwen2.5-1.5B-Instruct  
**Task family:** 6–7 hop multi-step chains  
**Scorer:** Strict format only → revealed as inadequate; dual scorer built in response  
**Outcome: Apparent C → dissolved under content rescore (format artifact)**  
**Result files:** `results_code_1780745541.json`, `results_prose_1780745788.json`  
**Pre-registration:** `PREREGISTRATION-EXP3.md`

### What was tested
Whether the smaller 1.5B model on 6–7 hop tasks shows the seam pattern under INT4.

### What happened

| Rung | G_strict(INT4) | 95% CI | Interpretation |
|---|---|---|---|
| INT4 | −0.0494 | [−0.0926, −0.0123] | excludes zero → apparent Outcome C |

The strict scorer flagged a real gap. This looked like a seam signal. Manual inspection revealed a different story: the INT4 model was producing the correct answer embedded in a sentence rather than in the clipped `ANSWER: <value>` format. The model knew the answer — it just stopped following the format contract under INT4.

Rescoring with a content-aware scorer (does the correct value appear anywhere in the output?) dissolved the gap:

| Rung | G_content(INT4) | 95% CI |
|---|---|---|
| INT4 | −0.0123 | [−0.0370, 0.0000] |

CI includes zero. No content-level gap. The strict-only drop was a format compliance artifact, not a seam signal.

### Key lesson
**A strict-only gap that does not appear under content scoring is a format artifact, not a seam signal.** This was encoded as a locked rule in all subsequent pre-registrations. The dual scorer (`strict_format_score` + `content_slot_score`) was designed in response.

### What changed
Built the dual scorer. Pre-registered it. Ran Exp 4 to formally replicate and confirm the finding under the new instrument.

---

## Experiment 4

**Model:** Qwen2.5-1.5B-Instruct  
**Task family:** 6–7 hop multi-step chains (same tasks as Exp 3: `tasks_exp3.py`)  
**Scorer:** Dual — `strict_format_score` + `content_slot_score` (pre-registered, 9 unit tests)  
**Calibrations:** Code (A) and Prose (B) — both identical outputs  
**Outcome: C — Calibration-invariant format cliff under dual scoring**  
**Result files:** `results_code_1780765654.json` (Cal A), `results_prose_1780765846.json` (Cal B)  
**Pre-registration:** `PREREGISTRATION-EXP4.md`

### What was tested
Formal replication of Exp 3 under the pre-registered dual scorer. Confirms whether the Exp 3 strict gap is a format artifact (CI includes zero under content scoring) or a genuine content effect (CI excludes zero under content scoring).

### What happened

| Rung | G_strict | 95% CI | G_content | 95% CI |
|---|---|---|---|---|
| INT8 | +0.0000 | [0.0, 0.0] | +0.0000 | [0.0, 0.0] |
| INT4 | −0.0494 | [−0.0926, −0.0123] | −0.0123 | [−0.0370, +0.0000] |

G_strict CI excludes zero. G_content CI includes zero. Outcome C confirmed — calibration-invariant across both calibration runs.

**Failure anatomy (INT4):**
- FORMAT_COMPLIANCE_LOSS: 6 items — in every case the correct answer appeared in the output but in a sentence wrapper rather than the clipped format. `content_slot_score = 1`, `strict_format_score = 0`.
- COMPOUND_NOUN_DROP: 1 item (FC1/vault3_token) — the adjective "silver" dropped, only "token" returned. Both scorers return 0. Single item, no statistical power.
- CONTENT_LOSS: 0 items — no item at any rung produced output entirely lacking the correct answer.

**Calibration-invariance gate: PASSED.** Both calibration runs bit-identical.

### What it means
INT4 compression degrades format compliance while preserving answer content. The model retains the correct answer but sometimes stops following the clipped output contract. This is instruction-following degradation, not reasoning degradation, not seam fragility. The dual scorer makes the separation clean.

### What changed
Format-degradation finding (Test 2) locally supported. Need to determine if it is scaffold-sensitive. Exp 5 designed to test whether a stronger explicit format instruction eliminates the cliff.

---

## Experiment 5

**Model:** Qwen2.5-1.5B-Instruct  
**Task family:** 6–7 hop multi-step chains (new tasks: `tasks_exp5_stable.py`, 10 stable substantive pairs)  
**Scorer:** Dual (unchanged from Exp 4)  
**Format instruction:** `"Respond using only this exact format with nothing before or after: ANSWER:"` (stronger than Exp 4)  
**Calibrations:** Code (A) and Prose (B) — both identical outputs  
**Outcome: G — Format cliff disappears under forced format (calibration-invariant)**  
**Result files:** `results_code_1780767539.json` (Cal A), `results_prose_1780767822.json` (Cal B)  
**Stability screen:** `stability_screen_1780767489.json` (13 stable, 1 excluded: FD4 capability floor)  
**Pre-registration:** `PREREGISTRATION-EXP5.md`

### What was tested
Whether the Exp 3/4 format cliff survives a stronger explicit format instruction. If the cliff disappears, root cause is instruction-following degradation. If the cliff persists (Outcome F), root cause is something deeper — logit-space style drift under quantization.

### What happened

| Rung | G_strict | 95% CI | G_content | 95% CI |
|---|---|---|---|---|
| INT8 | +0.0000 | [0.0, 0.0] | +0.0000 | [0.0, 0.0] |
| INT4 | +0.0522 | [−0.0878, +0.2778] | +0.0689 | [−0.0711, +0.2889] |

Both CIs include zero. Outcome G — cliff disappears. The Exp 3/4 format cliff was scaffold-sensitive.

**Format compliance improvement at INT4:**
- Broad arm: 0.750 (Exp 4) → 1.000 (Exp 5)
- FORMAT_COMPLIANCE_LOSS: 6 items (Exp 4) → 1 item (Exp 5)

**New failure class — CONTENT_LOSS (3 items at INT4):**
- FA2/narrow: semantic inversion — model returned INACTIVE when correct was ACTIVE. All component checks for FA2 passed. Structurally resembles the seam pattern but is a single item; G_content CI includes zero.
- FC1/comp[panelB_door]: input echo — model returned PANELB (the query entity) instead of DOOR6.
- FD2/comp[labEpsilon_division]: input echo — same pattern.

These content errors are genuine (both scorers return 0) but do not rise to statistical significance.

### What it means
**The Exp 3/4 format cliff was an instruction-following artifact, not a fundamental quantization effect.** A stronger prompt instruction reduces format drift substantially. Root cause: instruction-following degrades under INT4 for this model on short-context prompts. Not a logit-space style shift.

Format-degradation finding (Test 2) is now resolved: the cliff is real but correctable via instruction engineering.

### What changed
Format question closed. Returned focus to Test 1 (seam hypothesis). Exp 6 designed as the first formal seam test with a proper dual-scorer instrument, forced-format scaffold, and stability screen gate from the start.

---

## Experiment 6

**Model:** Qwen2.5-1.5B-Instruct  
**Task family:** 3-hop / 4-node seam design (15 items: SA1–SA8, DE1–DE4, NC1, AC1–AC2)  
**Scorer:** Dual (unchanged)  
**Quantization rungs run:** FP16 only (stability gate failed; stress sweep blocked)  
**Outcome: E — Task failure / stability gate not met**  
**Stability screen:** `stability_screen_1780771434.json`  
**Pre-registration:** `PREREGISTRATION-EXP6.md`

### What was tested
First formal seam test. Designed to produce stable FP16 baselines for 8 SA items, then stress those items across INT8 and INT4 to detect composite-vs-component degradation.

### What happened
Stability gate threshold: ≥6 stable SA pairs (included_in_G=True).  
**Stable SA pairs: 3 / 8 (SA2, SA3, SA7). Gate failed.**

Stress sweep not run. No seam signal — or non-signal — licensed.

**Two construction artifacts identified:**

**Artifact 1 — Last-value distractor anchoring:**  
In every SA item, the distractor fact (`ENTITY holds VALUE`) was appended at the END of the context. On a subset of items, the model returned the distractor value rather than traversing the chain — it anchored on the last value in context. Affected: SA1 (partial), SA4 (full), SA8 (full).

```
Context (Exp6 structure):
AXFOB connects to TUNNB. TUNNB leads to ALCV5. ALCV5 grants ZUNIP. GATEP holds BRIFQ.
                                                                    ↑ LAST VALUE ← anchor
```

**Artifact 2 — S2 verb compound-output on component prompts:**  
The S2 skeleton used `opens into` as a relation verb. On component prompts like "TORPX opens into what?", the model reproduced the full relation fact sentence (`TORPX opens into CLAVB.`) rather than just the formatted answer. This is a FORMAT_COMPLIANCE_LOSS on the component arm caused by the verb forming a fluent fill-in-the-blank template. Affected: SA5/comp[torpx_clavb].

### What it means
The stability gate did its job — it blocked a dirty run. The task construction had two artifacts that would have produced spurious INT4 findings if the stress sweep had proceeded. This is a task-construction finding, not a model-capability finding. Seam claim open, no movement.

### What changed
Exp 7 designed as a construction repair: move distractor to the front of context (Fix 1), drop the S2 skeleton entirely (Fix 2).

---

## Experiment 7

**Model:** Qwen2.5-1.5B-Instruct  
**Task family:** 3-hop / 4-node seam design — construction repair of Exp 6 (new token pools, 15 items: SA1–SA8, DE1–DE4, NC1, AC1–AC2)  
**Scorer:** Dual (unchanged)  
**Quantization rungs run:** FP16 only (stability gate failed; stress sweep blocked)  
**Outcome: E — Task failure / stability gate not met (again)**  
**Stability screen:** `stability_screen_1780776502.json`  
**Log:** `stability_screen_exp7_log.txt`  
**Pre-registration:** `PREREGISTRATION-EXP7.md`

### Construction repairs applied
**Fix 1:** Distractor moved to FRONT of context:
```
GATEP holds BRIFQ. AXFOB connects to TUNNB. TUNNB leads to ALCV5. ALCV5 grants ZUNIP.
↑ DISTRACTOR FIRST        ↑ CHAIN RUNS AFTER DISTRACTOR
```
**Fix 2:** S1 skeleton only (`connects / leads / grants`) for all 8 SA items. No S2.

### What happened
Stability gate threshold: ≥6 stable SA pairs (included_in_G=True).  
**Stable SA pairs: 3 / 8 (SA1, SA3, SA4). Gate failed again.**

| Item | Classification | Narrow orig | Narrow para | Comp pattern |
|---|---|---|---|---|
| SA1 | STABLE | 1.00 | 1.00 | All comps pass |
| SA2 | COMP_FAIL | 1.00 | 1.00 | Hop-1, Hop-2 return FLIPN (distractor broad value = first in context) |
| SA3 | STABLE | 1.00 | 1.00 | All comps pass |
| SA4 | STABLE | 1.00 | 1.00 | All comps pass |
| SA5 | FLOOR | 0.00 | 1.00 | Narrow orig returns GLIVN; vompl_jaxol comp returns GLIVN |
| SA6 | COMP_FAIL | 1.00 | 1.00 | Hop-1, Hop-2 return BROXN (decoy value; last in context — not terminal) |
| SA7 | FLOOR | 0.00 | 1.00 | Narrow orig returns KARVO; drizp_zarvp comp returns NIXBL |
| SA8 | COMP_FAIL | 1.00 | 1.00 | flumb_nakvi returns VEFLM (terminal) |

**Four artifact patterns in component checks:**

- **Pattern A — First-value anchoring (SA2):** Hop-1 and hop-2 component checks return the distractor's object value, which is now the first value in context after Fix 1. Model anchors on the first value in context.
- **Pattern B — Last-context-position anchoring on decoy (SA6):** Hop-1 and hop-2 return BROXN, the `decoy_value` field for SA6. Context structure: `BLIXO holds QUAFT. MAXBI→GRULP→WOXEN→NORVA. KARBX marks BROXN.` — BROXN is the final value in the context string, placed in the last sentence. Terminal is NORVA (not returned). Model anchors on the last context value, which is the decoy, not the terminal. *(Corrected 2026-06-07: previously described as "returns chain terminal" — provenance check confirmed BROXN is decoy_value.)*
- **Pattern C — Terminal over-retrieval (SA8):** flumb_nakvi component check (`FLUMB leads to what?`, expected NAKVI) returns VEFLM, the chain terminal. Context structure: `GRAFI holds LORVX. TROXB→FLUMB→NAKVI→VEFLM. PLOMV marks WULFT.` — the last context value is WULFT (decoy), not VEFLM. Model skips the requested intermediate node and returns the terminal. *(Corrected 2026-06-07: previously grouped with SA6 under "last-value anchoring" — these are distinct mechanisms. SA8 is terminal over-retrieval; SA6 is last-context-position anchoring on decoy.)*
- **Pattern D — Penultimate-node return on narrow (SA5, SA7):** Narrow original fails; narrow paraphrase passes. Model returns a mid-chain entity rather than the chain terminal on the original phrasing.

**Root cause analysis:**  
All component checks present the full 5-fact context (chain + distractor). The distractor fact and decoy facts designed to ensure composite robustness become noise for 1-hop retrieval. The model cannot isolate a single hop when shown the full graph. Hop-3 checks pass consistently (the terminal node is the most salient target). Hops 1 and 2 are unstable — the model tends to return the most salient endpoint (first or last value in context) rather than the correct intermediate node.

### What it means
A second consecutive stability gate failure. The problem is not context ordering per se (moving distractor first partly helped — SA1, SA3, SA4 became stable where only SA2, SA3, SA7 were stable in Exp 6). The deeper problem is that component checks with full 5-fact context cannot isolate individual hops: the full context introduces anchoring artifacts that corrupt 1-hop retrieval even when the model can do the full chain.

Seam claim open, no movement. Task-construction finding only.

### What changed
Exp 8 introduced a new measurement architecture: a four-rung ladder (copy floor → load-matched single-lookup → full-context chain-hop → composite target) to address the copy-vs-binding objection and isolate the seam effect without full-context component contamination. Arm 2 (load-matched single-lookup baseline) was the first feasibility target.

---

## Experiment 8 — Arm 2 (Feasibility Screen Only)

**Model:** Qwen2.5-1.5B-Instruct  
**Task family:** 5-fact uniform-relation retrieval (Arm 2: load-matched single-lookup baseline)  
**Scorer:** Three-axis (scaffold_class + format_class + content_class — amended post-run)  
**Quantization rungs run:** FP16 only (feasibility gate failed; expansion not authorized)  
**Phase:** n=8 feasibility screen  
**Outcome: NOT FEASIBLE — threshold not met**  
**Result files:** `tasks_exp8.py`, `fp16_screen_exp8_arm2.py`, `fp16_screen_exp8_arm2_1780781863.json`  
**Results document:** `RESULTS-EXP8-ARM2-FEASIBILITY.md`

### Design

Arm 2 is the second rung of the four-rung ladder: a load-matched single-lookup task. Five facts in context, one relation (`maps to`), query asks for the value associated with a specific subject at target position ∈ {2, 3, 4}. The model must retrieve one fact from a 5-fact context — same cognitive load as a single-hop check in prior experiments, but without the multi-hop chain structure that introduces anchoring artifacts.

**Feasibility criterion:** ≥7/8 items FORMAT_PASS + RETURNED_TARGET_OBJ at FP16.

### Three-axis scoring (amended post-run)
- **scaffold_class:** SCAFFOLD_PRESENT / SCAFFOLD_ABSENT — was ANSWER: prefix present?
- **format_class (strict, unchanged):** FORMAT_PASS = `^ANSWER:\s+[A-Z]{4,8}$` exactly; FORMAT_FAIL otherwise
- **content_class (9 classes, priority order):** RETURNED_TARGET_OBJ → RETURNED_OBJ_POS_k (k∈1..5) → RETURNED_SUBJ_TOKEN → RETURNED_NON_CONTEXT_TOKEN → UNCLASSIFIED

**Amendment note:** Original scorer conflated scaffold absence with non-alphabetic ANSWER content. Revised scorer separates the two. FORMAT_PASS kept strict; scaffold_class added as new diagnostic axis.

### What happened

| Item | target_pos | scaffold | format | content | returned | PASS |
|---|---|---|---|---|---|---|
| L2_01 | 2 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | ICVLX | ✓ |
| L2_02 | 2 | SCAFFOLD_PRESENT | FORMAT_FAIL | RETURNED_NON_CONTEXT_TOKEN | 0 | ✗ |
| L2_03 | 2 | SCAFFOLD_PRESENT | FORMAT_FAIL | RETURNED_NON_CONTEXT_TOKEN | 10 | ✗ |
| L2_04 | 3 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | PCIVX | ✓ |
| L2_05 | 3 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | SCIVX | ✓ |
| L2_06 | 3 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | IDBVX | ✓ |
| L2_07 | 4 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | OECVX | ✓ |
| L2_08 | 4 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | PJBVX | ✓ |

**Pass count: 6/8. Threshold: ≥7/8. NOT FEASIBLE.**

Pass by position: pos=2: 1/3 ✗ | pos=3: 3/3 ✓ | pos=4: 2/2 ✓

All 8 items: SCAFFOLD_PRESENT — model used the ANSWER: prefix every time. Both failures are content failures, not scaffold abandonments.

**Failure observation (construction finding, not resolvable at n=8):**
- Both failures at target_pos=2
- Both failures: homogeneous subject-prefix pool (L2_02: all C-prefix; L2_03: all H-prefix)
- Both failures: all O-prefix objects in context
- Both failures: numeric output returned ("0", "10") — not present in context

Numeric returns may indicate a wording/index artifact in specific subject-pool configurations. Not resolvable from n=8.

**Hash provenance:**
- Task/manifest hash (approved pre-run): `sha256:14129d0bfe2cae1c3e4d817a8423eaf5513665741c04f1d388ac8da34a9074de`
- Scorer/code hash (post-amendment, scorer only): `sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc`
- Task items and prompts were unchanged by the amendment. Raw model outputs are from the original run; no rerun was performed.

### What it means
Arm 2 does not advance. The feasibility gate failed before n≥20 expansion. This is a task-construction finding — the homogeneous subject-prefix pool configuration may be producing an indexing artifact at position 2. Not resolvable from 8 items.

No inference about quantization sensitivity or seam fragility is licensed from Exp8 Arm 2.

### Status
n≥20 expansion: not authorized. INT8 / INT4: not authorized. No further execution on Arm 2 under current construction. Senior Engineer will handle ledger wording.

---

## Experiment 8B — Arm 2B (Single-Variable Wording Test, Feasibility Screen Only)

**Model:** Qwen2.5-1.5B-Instruct  
**Task family:** 5-fact uniform-relation retrieval — exact Exp8A items, query wording only changed  
**Scorer:** Three-axis (scaffold_class + format_class + content_class — unchanged from Exp8A amendment)  
**Quantization rungs run:** FP16 only (feasibility gate failed; no further execution authorized)  
**Phase:** n=8 feasibility screen  
**Outcome: NOT FEASIBLE — Condition 1 not met**  
**Result files:** `tasks_exp8b.py`, `fp16_screen_exp8b.py`, `fp16_screen_exp8b_1780789038.json`  
**Results document:** `RESULTS-EXP8B.md`

### Design

Single-variable wording test on exact Exp8A items. All item geometry (subjects, objects, fact order, target positions, relation, context lines) is identical to Exp8A. Only the query wording changed:

```
Exp8A: "Which value is associated with SUBJ_T?"
Exp8B: "Which token is assigned to SUBJ_T?"
```

**Pass condition (both must be met):**
1. FP16 content pass count ≥7/8
2. Zero numeric out-of-context returns

### What happened

| Item | target_pos | scaffold | format | content | returned | PASS |
|---|---|---|---|---|---|---|
| L2_01 | 2 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | ICVLX | ✓ |
| L2_02 | 2 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | OBLVX | ✓ |
| L2_03 | 2 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_OBJ_POS_1 | OHIBX | ✗ |
| L2_04 | 3 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_OBJ_POS_2 | PBCVX | ✗ |
| L2_05 | 3 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | SCIVX | ✓ |
| L2_06 | 3 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | IDBVX | ✓ |
| L2_07 | 4 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | OECVX | ✓ |
| L2_08 | 4 | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | PJBVX | ✓ |

**Pass count: 6/8. Numeric OOC: 0.**

```
Condition 1 — ≥7/8 content PASS:  NOT MET  (6/8)
Condition 2 — zero numeric OOC:   MET      (0)
Result: NOT FEASIBLE
```

### Comparison with Exp8A

| Item | Exp8A result | Exp8B result | Change |
|---|---|---|---|
| L2_01 | ✓ RETURNED_TARGET_OBJ | ✓ RETURNED_TARGET_OBJ | same |
| L2_02 | ✗ RETURNED_NON_CONTEXT_TOKEN ("0") | ✓ RETURNED_TARGET_OBJ | **fixed** |
| L2_03 | ✗ RETURNED_NON_CONTEXT_TOKEN ("10") | ✗ RETURNED_OBJ_POS_1 ("OHIBX") | failure mode changed |
| L2_04 | ✓ RETURNED_TARGET_OBJ | ✗ RETURNED_OBJ_POS_2 ("PBCVX") | **new failure** |
| L2_05–L2_08 | ✓ (all) | ✓ (all) | same |

**Output string exact match for the 6 Exp8A passers:** 5/6 bit-identical. L2_04 changed (correct → wrong; off-by-one to pos=2 object).

### What it means
The wording change eliminated numeric OOC returns (Condition 2 met) but did not achieve Condition 1. Pass count remained 6/8 in both Exp8A and Exp8B. The wording change redistributed failures rather than resolving the underlying construction problem: L2_02 was rescued, L2_03 traded numeric OOC for positional anchoring (RETURNED_OBJ_POS_1), and L2_04 was newly destabilized with an off-by-one error (returned pos=2 object instead of pos=3 target).

The 5/6 bit-stability of Exp8A passers confirms the wording change was mostly non-perturbing to stable items. L2_04's destabilization is an n=8 observation only.

### Branch F — Confirmed failure set (manuscript case material)

All four failures across Exp8A and Exp8B confirmed from raw output JSONs:

| Item | Exp | content_class | raw token | context status | Diagnostic flag |
|---|---|---|---|---|---|
| L2_02 | 8A | RETURNED_NON_CONTEXT_TOKEN | `0` | Not in context | Degenerate numeric return |
| L2_03 | 8A | RETURNED_NON_CONTEXT_TOKEN | `10` | Not in context | Degenerate numeric return |
| L2_03 | 8B | RETURNED_OBJ_POS_1 | `OHIBX` | In-context (pos=1) | Wrong in-context position return |
| L2_04 | 8B | RETURNED_OBJ_POS_2 | `PBCVX` | In-context (pos=2) | Wrong in-context neighbor / orthographic similarity to target |

**Branch F story (failure-surface migration):**
```
Exp8A:  numeric non-context returns  (RETURNED_NON_CONTEXT_TOKEN)
Exp8B:  wrong in-context object returns  (RETURNED_OBJ_POS_k)
```
The wording change reduced numeric-output behavior but did not stabilize retrieval. The failure surface migrated from non-context degenerate outputs to in-context positional anchoring.

**Manuscript rule:** Do not cite `OTHER_NON_CONTEXT_SYNTHETIC` as an observed Exp8A/Exp8B category. No real observation of an alphabetic non-context synthetic-token return exists in the current dataset. If that category appears in the paper at all, it must be labeled as a possible future diagnostic annotation, not case material. Preferred: omit from the main case table.

**Scorer registry:** 9 content classes locked. RETURNED_NON_CONTEXT_TOKEN remains flat. Diagnostic flags are post-hoc paper annotations only, separate from scorer output.

### Status
Exp8B is the final unconditional Arm 2 construction attempt. No n≥20 expansion. No INT8/INT4. No Exp8C. No further execution without explicit Manager / Team Lead decision.

---

## Master Ledger

| Run | Model | Task family | Scorer | G_strict INT4 CI | G_content INT4 CI | Outcome |
|---|---|---|---|---|---|---|
| Tier 0A | Qwen2.5-7B | 3-hop | strict only | — | — | flat / task ceiling |
| Tier 0B | Qwen2.5-1.5B | 3-hop | strict only | — | — | flat / task ceiling |
| Tier 0C | Qwen2.5-7B | 5-hop | strict only | — | — | flat / task ceiling |
| Exp 2 | Qwen2.5-7B | 6–7-hop | strict only | — | [−0.061, 0.000] | D — flat / local null |
| Exp 3 | Qwen2.5-1.5B | 6–7-hop | strict only | — | [−0.037, 0.000] | C (strict) → dissolved under content rescore |
| Exp 4 (code) | Qwen2.5-1.5B | 6–7-hop | dual | [−0.0926, −0.0123] | [−0.0370, +0.0000] | C — format cliff, content flat |
| Exp 4 (prose) | Qwen2.5-1.5B | 6–7-hop | dual | [−0.0926, −0.0123] | [−0.0370, +0.0000] | C — format cliff, content flat |
| Exp 5 (code) | Qwen2.5-1.5B | 6–7-hop forced fmt | dual | [−0.0878, +0.2778] | [−0.0711, +0.2889] | G — cliff disappears |
| Exp 5 (prose) | Qwen2.5-1.5B | 6–7-hop forced fmt | dual | [−0.0878, +0.2778] | [−0.0711, +0.2889] | G — cliff disappears |
| Exp 6 | Qwen2.5-1.5B | 3-hop/4-node seam | dual | FP16 only | FP16 only | E — stability gate failed (3/8) |
| Exp 7 | Qwen2.5-1.5B | 3-hop/4-node seam (repair) | dual | FP16 only | FP16 only | E — stability gate failed (3/8) |
| Exp 8 Arm 2 | Qwen2.5-1.5B | 5-fact single-lookup | 3-axis | FP16 only | FP16 only | NOT FEASIBLE (6/8) |
| Exp 8B Arm 2B | Qwen2.5-1.5B | 5-fact single-lookup (wording change) | 3-axis | FP16 only | FP16 only | NOT FEASIBLE (6/8, 0 numeric OOC) |

---

## Claim Status (as of 2026-06-09)

**Primary seam claim (Test 1):** OPEN. Not triggered across eight experiments, two models.  
The claim has never been formally adjudicated because no experiment has passed the stability gate and run the stress sweep. The constructibility-floor program (Two-Hop L1, see below) established why: no stress-eligible baseline exists. The seam cannot be tested until a constructibility-certified baseline clears Gate 2.

**Format-degradation finding (Test 2):** RESOLVED.  
The Exp 3/4 format cliff is real but scaffold-sensitive. Under a stronger explicit format instruction (Exp 5), the strict-score gap disappears: G_strict(INT4) CI [−0.0878, +0.2778] includes zero. Root cause: instruction-following degradation at INT4, not logit-space style drift. The format cliff cannot be used as evidence for seam fragility.

---

## Two-Hop L1 Constructibility Program — COMPLETE (2026-06-09)

**Program question:** Is a two-hop construction constructible at full precision? What is the floor?

Three cells run, all Branch 3. Cells01–03 are pre-stress baseline mapping, not a seam-fragility test. Results are published as *Correctness Is Not Constructibility* (Paper 2, v1.0, tagged `paper2-cells01-03-v1.0`).

**Master ledger — Two-Hop L1:**

| Cell | Model | hop1 | hop2 | composite | neg_graph | Gate 1 | Gate 2 | Branch |
|---|---|---|---|---|---|---|---|---|
| Cell01 | Qwen2.5-3B FP16 | 14/24 | 24/24 | 18/24 | 2/24 | PASS | FAIL | 3 |
| Cell02 | Qwen2.5-3B FP16 | 9/24 | 23/24 | 20/24 | 0/24 | FAIL (1 FSF) | FAIL | 3 |
| Cell03 | Qwen2.5-3B FP16 | 6/24 | 23/24 | 15/24 | 6/24 | PASS | FAIL | 3 |

**Key finding:** The construction's hop1 floor blocks stress eligibility across all three cells; hop2 is near-ceiling. The failure landscape is structured and classifiable (taxonomy saturated, 288/288 outputs classified). Floor is mappable but not cleared. No compression sweep has run.

**Artifact hashes (13/13 verified at tag):**

| Artifact | sha256 (first 8) |
|---|---|
| items_twohop_l1_cell01.json | 00a7adf8 |
| items_twohop_l1_cell02.json | b81d4716 |
| items_twohop_l1_cell03.json | 7d5099cb |
| runner_twohop_l1.py | f346e4f2 |
| runner_twohop_l1_cell02.py | d14f6424 |
| runner_twohop_l1_cell03.py | f23d99df |
| scorer_twohop_l1.py | b65c6803 |
| RESULTS-TWOHOP-L1-cell01-1780912218.json | 6de8b67c |
| RESULTS-TWOHOP-L1-cell02-1780933041.json | 47b5eaa9 |
| RESULTS-TWOHOP-L1-cell03-1780948339.json | f29783622f |
| RESULTS-TWOHOP-L1-cell01-ALL.md | 696a1e0c |
| RESULTS-TWOHOP-L1-cell02-ALL.md | b4274643 |
| RESULTS-TWOHOP-L1-cell03-ALL.md | 6c6c6dfc |

**Paper 2 v1.0 release (2026-06-09):**
- Tag: `paper2-cells01-03-v1.0` on commit `40c0cd5a`
- Tagged manuscript blob: `7d6706a346bb634bed6752ff147fd67e1ad2596f`
- Release governance: `governance/2026-06-09_post-paper2-alignment/` (this folder) and `governance/2026-06-09_paper2-v1.0-release/` (repo root)
- Published: `papers/paper2-correctness-is-not-constructibility/` (repo root)

**Current CS state:**
- `tier0-run/` is SEALED — never add files here
- B1 harness hardening is the next CS lane — BLOCKED pending Manager code-change authorization
- Paper 3 threshold framework design is the next parallel lane (design only, no runs)

— CS Engineer, 2026-06-09

---

## B1 v2 Lock — 2026-06-10

B1 v2 harness merged to `main` per Manager authorization 2026-06-10.

| Item | Value |
|---|---|
| Merge commit SHA | `3cbfce57d42536e8a5e1f35a92c931a03fe4e974` |
| Merge type | `--no-ff` |
| Branch merged | `b1-harness-v2` |
| Branch tip at merge | `ff8466b2702205e9b9f95458cfe2d9023cb98ccb` |
| Locked runner hash | `sha256:7f5efdcbf8a51a9368ee1868be7bcb734fb4ceeedbe580f29f9ff2ac87f90fe6` |
| Model snapshot (runner-provenance-backed) | `sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20` |
| Full regression artifact hash | `sha256:c9114c192dbaafc66d85babf6dacc62b9df8e4ffb87886fb868c875a202893f8` |
| Smoke regression artifact hash | `sha256:7cc17649a7a20d3bf99c7c9517fe8604a9a537a6cb3baf734d78ff0e71058f39` |

**Test outcomes recorded at lock:**

| Test | Result |
|---|---|
| B1 unit tests (B1-T01 → B1-T24) | 24/24 PASS |
| Paper 2 reproduction sanity tests | 2/2 PASS |
| Smoke regression (i01 × 4 query types) | 4/4 raw_output bit-identical |
| Full regression (96 records) | 96/96 raw_output bit-identical; all gate decisions match Paper 2 v1.0; v1 shape 7/7 |

**Paper 2 v1.0 surface at lock:**

| Item | Value |
|---|---|
| Tag SHA | `41c033fc59597eb42015de9019c3ac7b7d19dd98` (unmoved) |
| Tagged commit | `40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce` (unmoved) |
| Tagged manuscript blob | `7d6706a346bb634bed6752ff147fd67e1ad2596f` (preserved in tag) |
| Manuscript blob on main | `34ada312b96dd20138b3553e2a78a53ff0681b09` (post-v1.0 release status-label commit, predates this merge; documented in commit `69df8be`) |
| tier0-run/ artifacts | not modified by merge |

**Addendum 01 effectivity:** `governance/2026-06-09_paper2-v1.0-release/ADDENDUM-01-model-snapshot-backing.md` §5 effectivity clause activates at this merge. Snapshot status of v1.0 is now recorded as *historically asserted in v1.0; subsequently corroborated by B1 runner-provenance-backed bit-identity reproduction; release-record addendum committed; Paper 2 tag/manuscript unchanged.*

**Paper 3 substrate posture:** config-gated, disabled by default. Runner defaults are `--mode dry-run`, `--context paper2-reproduction`, `--framework-version none`. Activating Paper 3 substrate at runtime is not the same as authorization to apply Paper 3 certification; certification application requires separate Manager authorization.

**What the lock does NOT do:**
- Does not activate Paper 3 certification.
- Does not select a candidate or set any threshold value.
- Does not introduce any candidate threshold sheet, candidate output, or certification result.
- Does not authorize new runs, re-runs, INT8/INT4 execution, multi-model execution, or any other blocked lane.

**Governance records for this lock:**
- `governance/2026-06-09_b1-harness-v2-merge-readiness/` — pre-merge merge-ready note, branch evidence packet, wording correction report
- `governance/2026-06-10_b1-harness-v2-merge-and-lock/` — lock note + post-merge confirmation report
- `governance/2026-06-09_paper2-v1.0-release/ADDENDUM-01-model-snapshot-backing.md` — addendum, now active

**Next CS state:**
- B1 v2 is the active validity-harness infrastructure.
- No further CS deliverables pending until next authorization.
- Boundaries remain closed: no candidate selection, no thresholds, no Paper 3 execution, no new runs, no INT8/INT4, no multi-model, no Fork A, no Claim C.

— CS Engineer, 2026-06-10

---

## Paper 3 v1.0 Release — 2026-06-10

Paper 3 (*Certification Before Retention*) released to `main` per Manager authorization 2026-06-10.

| Item | Value |
|---|---|
| Release commit SHA | `63d217216752f833b257d426665c872a21c5f422` |
| Tag name | `paper3-certification-protocol-v1.0` |
| Tag object SHA | `6dbdcc1238a186af32baac076d3d82c92fd7c205` |
| Tagged manuscript blob (git, 40-hex) | `798f7dceacf7ea05630009d80106a6dbff47b031` |
| Tagged manuscript sha256 | `b948521ebab74b3a225a98509a07488c0f1a4c86d1802d46796e57b2d361e714` |
| PDF sha256 | `6223cf85a65f1bc6fe4621f717997e6b8d2b253b6156951715d6d30005080d8f` |
| Figures | 4 PNG + 4 SVG; full hashes in `governance/2026-06-10_paper3-v1.0-release/RELEASE-RECORD.md` |

**Paper 2 lesson incorporated.** The RC text IS the final v1.0 text; the commit that landed the manuscript is the commit that was tagged. No post-tag masthead flip. Tagged blob (`798f7dce...`) == main blob (`798f7dce...`) — no divergence. The audit pattern that complicated Paper 2 is explicitly avoided here.

**Tag name matches lock-eligible framework identifier.** `paper3-certification-protocol-v1.0` is the first lock-eligible framework version (per the manuscript's own framework-version rule). A future threshold sheet's `framework_version` field can name the tag byte-for-byte; no mapping table required.

**Pre-release verification chain (all PASS):**
- CS release-consistency checklist: 10/10 items PASS (`governance/2026-06-10_paper3-v1.0-release/CS-RELEASE-CONSISTENCY-CHECKLIST.md`)
- F1 (hash drift on md/pdf): cleared by Senior manifest refresh
- F2 (PDF geometry): cleared by Senior `fitz` zero-overflows + visual confirmation
- Senior, Team Lead, Manager authorizations all archived in `governance/2026-06-10_paper3-v1.0-release/`

**Boundaries unchanged.** This release does NOT activate Paper 3 application. No candidate selection, no threshold-sheet population, no threshold lock, no certification evaluation, no runs, no INT8/INT4, no multi-model, no Fork A reactivation, no Claim C activation, no B1 v2.1 implementation, no public benchmark packaging.

**B1 v2.1 backlog item #5 has a concrete rule.** Drafts use `paper3-certification-protocol-v0.*` (B1 refuses lock); released uses `paper3-certification-protocol-v1.*+` (B1 may proceed). Enforced at the future B1 v2.1 Paper 3 substrate-completion pass.

**Governance records for this release:**
- `governance/2026-06-10_paper3-v1.0-release/RELEASE-RECORD.md` — this release
- `governance/2026-06-10_paper3-v1.0-release/CS-RELEASE-CONSISTENCY-CHECKLIST.md` — 10-item verification
- `governance/2026-06-10_paper3-v1.0-release/CS-COMMIT-AND-TAG-PROCEDURE.md` — staged procedure (now executed)
- `governance/2026-06-10_paper3-v1.0-release/CS-RELEASE-CONFIRMATION-REPORT.md` — pre-release CS confirmation
- `governance/2026-06-10_paper3-v1.0-release/CS-RELEASE-EXECUTION-REPORT.md` — post-release CS confirmation
- `governance/2026-06-10_paper3-v1.0-release/PAPER3-RELEASE-CANDIDATE-PACKAGE.md` — Senior RC package (refreshed)
- `governance/2026-06-09_paper3-threshold-framework-review/` — full review arc (v0.2 → v1.0)

— CS Engineer, 2026-06-10

---

## Paper 3 v1.1 Release — 2026-06-10

Paper 3 v1.1 (manuscript-only remediation of v1.0 under the v1.1 scope authorization of 2026-06-10) released to `main` per Manager authorization 2026-06-10.

| Item | Value |
|---|---|
| Release commit SHA | `f769c03468bb3e39a29d10a406df4d7a59766531` |
| Tag name | `paper3-certification-protocol-v1.1` |
| Tag object SHA | `0b63b2ef10974a9e5ce2f7a0c28b11799649c566` |
| Tagged manuscript blob (git, 40-hex) | `489d0744a43d35b600096661b4a666785ab73cee` |
| Tagged manuscript sha256 | `b93f60a64c93134fff229466c92639bb2553e8e29e7ffd609551876675864089` |
| Tagged PDF blob (git, 40-hex) | `0babd141dcad135130350bd0f6da78544100f1d1` |
| PDF sha256 | `c7095f89ef9585d9a191f0749c1c30866677964a36ad1de162b4e94bf5393be7` |
| Figures | unchanged from v1.0 release (4 PNG + 4 SVG, bit-identical to v1.0 tag) |

**Paper 2 lesson incorporated.** The RC text IS the final v1.1 text; the commit that landed the manuscript is the commit that was tagged. Tagged blob == main blob — no divergence. Tag points at `f769c03`, which is the current HEAD of `main`.

**v1.0 disposition.** The v1.0 tag and tagged manuscript are unmodified; v1.0 is now **superseded-released** per the H3 framework supersession rule introduced in this revision: lock-eligibility by default is now exclusively `paper3-certification-protocol-v1.1`. Use of v1.0 as a `framework_version` on a new threshold sheet is refused absent explicit written Manager authorization naming v1.0 and the specified purpose.

**v1.1 scope items, all eight present in the released manuscript:** E1 three-mode D2; E2 D6 storage mapping; M1/M2 Appendix B [SYNTHETIC] satisfiability note; M3 §9 certifier operating characteristics; Q1 `reporting_mode` recording field; Q2 three quote-safe non-claim blocks per Team Lead Option A adjudication (Abstract / §6 / §10); H3 framework supersession rule; G1 strengthened transfer rule (governance, not manuscript text).

**Three CS soft observations from the Draft 2 review (commit `21e33cc`) adopted into the released manuscript:**
- A — D2b binding-vs-reported_only choice must be justified in threshold-sheet statistical plan
- B — §5 cross-attempt clause: `full_profile` diagnostics may not derive or adjust subsequent attempts' thresholds
- C — gate provenance table header "Documented motivating record — ancestry, not validation"

**Pre-release verification chain (all PASS):**
- Source RC manuscript bit-identity vs. Senior G1 enumeration: PASS (`b93f60a6…`)
- Source RC PDF bit-identity vs. Senior G1 PDF enumeration: PASS (`c7095f89…`)
- All four PNG figure hashes bit-identical to v1.0 release: PASS
- Vehicle-decision sentence present under whitespace-collapsed identity: PASS
- Three-block non-claim functional alignment per Q2 Option A: PASS
- Framework target `paper3-certification-protocol-v1.1` present; v1.0 identifier appears only in H3 supersession-rule sentence: PASS
- Post-commit blob hash == content hash for both md and pdf: PASS
- Tag blob == main blob (Paper 2 lesson check): PASS
- Senior G1 SEND-TO-CS for manuscript (Draft 3) verified CS-side at commit `7585afd`
- Senior G1 SEND-TO-CS for PDF (Option A) verified CS-side at this release commit

**Boundaries unchanged.** This release does NOT authorize Lane 1a execution, ladder construction, candidate selection, candidate ranking, threshold-sheet population, threshold lock, certification evaluation, new runs, INT8/INT4 stress, multi-model execution, B1 v2.1 implementation, Claim C activation, Fork A reactivation, Paper 3 application, Paper 6 activation, or public benchmark packaging. All execution gates remain closed. v1.1 lock-eligibility is a precondition, not an authorization.

**Governance records for this release:**
- `governance/2026-06-10_paper3-v1.1-release/RELEASE-RECORD.md` — this release
- `governance/2026-06-10_paper3-v1.1-release/CS-EXECUTION-REPORT.md` — post-release CS execution report
- Senior G1 delivery notes (audit trail; held in Senior working area until v1.1 review archive opens): `G1-DELIVERY-NOTE-DRAFT3.md` and `G1-DELIVERY-NOTE-RC-PDF.md`
- `governance/2026-06-09_paper3-threshold-framework-review/` — full review arc (Draft 1 → Draft 2 → Draft 3)
- `governance/2026-06-10_paper3-v1.0-release/MANAGER-AUTHORIZATION-v1.1-SCOPE.md` — v1.1 scope authorization

— CS Engineer, 2026-06-10

**Instrument status:** LOCKED.  
- Dual scorer (`strict_format_score` + `content_slot_score`) pre-registered and unit-tested.
- Three-axis scorer (scaffold_class / format_class / content_class) implemented for Exp 8.
- Key rule: a strict-only gap that dissolves under content scoring is a format artifact, not a seam signal.

---

## Decoding Provenance Record

**Status: CLOSED — confirmed 2026-06-07 as manuscript dependency.**  
All experiments listed below used deterministic single-draw greedy decoding. No sampling, no top_p/top_k, no seed.

| Experiment | Model | Bits | Temp | Decoding | Draws/item | max_tokens | Seed | Decoding in JSON artifact? |
|---|---|---|---|---|---|---|---|---|
| Exp6 | Qwen2.5-1.5B | FP16 | 0.0 | Greedy | 1 | 512 | None | **No** |
| Exp7 | Qwen2.5-1.5B | FP16 | 0.0 | Greedy | 1 | 512 | None | **No** |
| Exp8 Arm 2 | Qwen2.5-1.5B | FP16 | 0.0 | Greedy | 1 | 16 | None | Yes |
| Exp8B Arm 2B | Qwen2.5-1.5B | FP16 | 0.0 | Greedy | 1 | 16 | None | Yes |

**Provenance gap note (preserved for manuscript):**  
Exp6 and Exp7 decoding settings are reconstructed from source code (`run_stability_screen.py`: `make_sampler(temp=0.0)`, `--max-tokens` default=512, single `run_prompt` call per item) and are not stored directly in the JSON artifacts. Exp8 Arm 2 and Exp8B are self-documenting at the JSON level (`decoding`, `bits`, `fresh_generation` fields present).

---

## Stage 0 — Two-Hop Level 1 Instrument Lock

**Status:** CLOSED — 2026-06-07  
**Accepted by:** Team Lead (memo: "Stage 0 Closure Accepted — Log Update and Threshold Proposal Next," 2026-06-07)  
**No model inference occurred at any Stage 0 step.**

### Locked files and SHA-256 hashes

```
tasks_twohop_l1.py              sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
scorer_twohop_l1.py             sha256:6921e58059e3ef4806c1ae75f73a9670f4a02962bff2eb27fd2da77bad82c473
smoke_test_twohop_l1.py         sha256:58749ca88ab69e0fc6cf34cfb3417ee57f42c1ebe13c5c7cfd384726182c3989
RUN-SUMMARY-TEMPLATE-TWOHOP-L1.md   (template — not hashed)
STAGE0-INSTRUMENT-LOCK-PACKET.md    (packet document — not hashed)
```

**No amendment to locked Stage 0 files is authorized without Team Lead approval.**

### Test results

```
Scorer unit tests:  14/14 pass
Smoke tests:        22/22 pass
Model inference:    none — offline instrument correctness only
```

### Specification completions (accepted as part of Stage 0 record)

**1. anchor_echo priority correction**

The approved residual priority order placed `anchor_echo` at position 6, after `wrong_chain_selection` at position 5. Since `anchor_A` objects belong to `TARGET_CHAIN_ROLES`, the `target_chain_wrong_neighbor` check fires first for any anchor-A return under that order, making `anchor_echo` permanently unreachable. Corrected to position 4, before `wrong_chain_selection`. Confirmed by Team Lead as a specification completion, not a taxonomy change.

Final priority order (locked):
```
1. format_scaffold_failure
2. non_context_return
3. correct_chain_stopped_short  (composite only)
4. anchor_echo                  (corrected: before wrong_chain_selection)
5. wrong_chain_selection
6. target_chain_wrong_neighbor
7. UNCLASSIFIED_OFF_FRAME
```

**2. Decoy chain A-position role: `other_context`**

No designated role existed for the source/anchor object of a decoy chain. Assigning `distractor_chain_intermediate` to that position would contaminate the hop1 denominator, which must count only B-position objects. Assigned `other_context` to all decoy chain A-position objects. Confirmed by Team Lead. Rationale: preserves hop1 denominator integrity.

### Threshold status

**Manager approval received 2026-06-08** — Revision 2 threshold set approved. Full approval details in THRESHOLD-PROPOSAL-TWOHOP-L1.md.

**Approved thresholds (locked 2026-06-08):**

```
Gate-2 FP16 pass rate (per query type)   hop1/hop2/composite ≥ 0.875 (≥ 21/24)
Dummy ceiling                            max_dummy ≤ 0.375 (≤ 9/24)
                                         Gate-2 composite − max_dummy ≥ 0.40
                                         no dummy > chance + 0.05
Near-miss Levenshtein k                  k ≤ 2 (Manager-authorized)
BPE-Jaccard j                            j ≥ 0.40 — LOCKED 2026-06-08 (Manager)
Trigram-Jaccard j                        j ≥ 0.20
Length-matched tolerance                 ± 10 prompt tokens
Unique-assignment reliability            1.000 (scorer guarantee; operational gate = UNCLASSIFIED ≤ 0.05)
UNCLASSIFIED / OFF-FRAME ceiling         ≤ 0.05; watch trigger > 0.02
Gate-3 ceilings (composite, FORMAT_PASS denominator):
  stopped_short                          ≤ 3/24
  shortcut_single_hop                    ≤ 2/24
  wrong_chain                            ≤ 3/24
  wrong_neighbor                         ≤ 3/24
  anchor_echo                            ≤ 3/24
```

**BPE-Jaccard amendment — j ≥ 0.50 → j ≥ 0.40 — LOCKED 2026-06-08 (Manager):**
Offline tokenizer inspection (2026-06-08) found the approved j ≥ 0.50 does not match the Qwen2.5-3B-Instruct tokenizer: declared near-miss CPQVX/CPQWX (Levenshtein=1) has BPE-Jaccard = 0.40. Team Lead recommended j ≥ 0.40 (2026-06-08). Manager confirmed and locked (2026-06-08). Construction tokenizer hash: `sha256:3fd169731d2cbde95e10bf356d66d5997fd885dd8dbb6fb4684da3f23b2585d8` (local int4/int8). FP16 HuggingFace tokenizer confirmed: `sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539` (serialization variant only — vocabulary identical 151,643; normalized merges identical 151,387; BPE behavior identical; **RECONCILED 2026-06-08** — see `TOKENIZER-HASH-RECONCILIATION-TWOHOP-L1.md`). BPE-Jaccard re-audit under sha256:c0382117...: 0 violations, 24/24 near-miss pairs j ≥ 0.40 — PASS. Gate 0.5 unambiguous under run tokenizer. Inspection artifact: `BPE-JACCARD-INSPECTION-TWOHOP-L1.md`.

**Gate 1 FORMAT_PASS threshold — LOCKED 2026-06-08 (Manager):**
Gate 1 FORMAT_PASS = 1.000 per query type for stress eligibility. Manager clarifications (2026-06-08): NULL / NO_LINK returned under negative_graph contract = FORMAT_PASS (format adherence, not correctness); correctness excluded; evaluated per query type, no pooling.

**shortcut_single_hop validator — CLOSED (Team Lead disposition 2026-06-08):**
Coverage confirmed in canonical locked artifact `tier0-run/tasks_twohop_l1.py`, `sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b`. `validate_positive_sufficiency()` present at line 201; checks confirmed: `answer_from_hop1_alone_possible` (line 205), `answer_from_hop2_alone_possible` (line 207), `composite_answer == hop1_answer` (lines 217–221); called from `validate_item()` at line 276. No Stage 0 Amendment A required. shortcut_single_hop_rate = 0 by construction for any validated cell.
*Provenance note: a prior conflicting inspection referenced non-canonical path `stage0/validator.py` (sha256:e15fe39f…06b2), which does not exist in the repository; canonical artifact reconciliation resolved the discrepancy (Path A, Team Lead 2026-06-08).*

### Current authorization boundary

**Stage 1 preparation — AUTHORIZED AND COMPLETE (Manager 2026-06-08, Team Lead Rev 2 accepted):**
```
scorer amendment (sha256:6921e580→sha256:060afad9 — Option D, Team Lead 2026-06-08)
cell regeneration Rev 2 (items_twohop_l1_cell01.json — 3-chain 7-fact 8+8+8, n=24, sha256:00a7adf8...)
runner update (runner_twohop_l1.py — sha256:ed2fbdc3...; AXIS/FROZEN/SCORER hash updated for Rev 2)
prompt template unchanged (sha256:c8a81a29...)
FP16 tokenizer hash confirmed (sha256:c0382117... — accepted by Team Lead 2026-06-08)
offline validation (validate_manifest: 24/24 PASS)
Stage 1 Preparation Lock Packet Rev 2 (STAGE1-PREP-LOCK-PACKET-TWOHOP-L1.md — filed 2026-06-08)
```

**Stage 1 FP16 execution — AUTHORIZED (Manager 2026-06-08):**
```
VOIDED RUN: RESULTS-TWOHOP-L1-cell01-1780911140.json
  Status: VOID — environment / runner incompatibility
  Cause: mlx_lm 0.8.0 (only version with temp= API) does not stop generation
         for Qwen2.5-Instruct without chat template; 96/96 format_scaffold_failure
         from trailing continuation, not model inability (all 96 raw outputs begin ANSWER:)
  Runner hash at void run: sha256:ed2fbdc3...

RUNNER AMENDMENT: authorized by Manager 2026-06-08 (Option R1)
  Change 1: import stream_generate (was generate)
  Change 2: dry-run prompt rendering display added
  Change 3: generate() replaced with chat-template + stream_generate() accumulation
  mlx_lm version: 0.19.3
  Old runner hash: sha256:ed2fbdc3e21375060f15a0645da111c24db890b840d9be476ee24d8bb06c5aaf
  New runner hash: sha256:f346e4f2cf93b881e129ba25bea469e2f6349ce1b6d430f8ddfb7269f3d0d7ce
  Dry-run PASSES (amended runner, 2026-06-08)

RERUN: authorized by Manager 2026-06-08 under amended runner
  Result artifact: RESULTS-TWOHOP-L1-cell01-1780912218.json
    sha256:6de8b67c0267a65f088e7bccd68b3cd070c675938c71470dd97a5411daca6f47
  Result: Gate 1 PASS, Gate 2 FAIL (hop1 14/24, hop2 24/24, composite 18/24), Branch 3
  Run_Summary: RESULTS-TWOHOP-L1-cell01-ALL.md — accepted by Team Lead (Branch 3)
  Tokenizer reconciliation: COMPLETE 2026-06-08 — Gate 0.5 confirmed PASS under run tokenizer
    See TOKENIZER-HASH-RECONCILIATION-TWOHOP-L1.md
```

**Cell02 construction — AUTHORIZED (Manager 2026-06-08, position/ordering axis, Option A):**
```
Cell02 generation: items_twohop_l1_cell02.json
  sha256:b81d471616f8830fba76b99b9e1b04e23d3e4af13284c27627481ae89528f4c9
  RNG seed: 20260610 (seed 20260609 discarded — gen_pool broken circuit breaker fixed)
  Axis: all-C_target-last (T-hop2 at pos 6 for all 24 items)
  Gate 0: PASS (24/24 validate_manifest)
  Gate 0.5: PASS (0 violations, 24/24 near-miss pairs j ≥ 0.40)
  Gate 5 dummy ceiling: PASS (max_det = 0/24)
  Runner (Cell02): runner_twohop_l1_cell02.py
    sha256:d14f6424340699785a8bdc12a8bb6c2b7cb33f96069de49e1fcb945bbc12b0fa
    Amendment: ITEMS_PATH + AXIS_CONFIGURATION only; all other constants frozen
  Dry-run: PASS (2026-06-08) — all 4 query types rendered; tokenizer hash confirmed
  Prep Lock Packet: CELL02-PREP-LOCK-PACKET-TWOHOP-L1.md — filed 2026-06-08
  Status: AWAITING TEAM LEAD REVIEW for FP16 execution authorization
```

**Cell02 FP16 execution — AUTHORIZED AND COMPLETE (Manager 2026-06-08):**
```
Run artifact: RESULTS-TWOHOP-L1-cell02-1780933041.json
  sha256:47b5eaa9b954645ca2572fe20873a0255776f60f29b0a544d8c350dcddc181ca
Results:
  hop1:           9/24   Gate 2 FAIL
  hop2:           23/24  Gate 1 FAIL (1 FSF — i08 sentence-format output)
  composite:      20/24  Gate 2 FAIL
  negative_graph: 0/24   (abstention contract)
Gate 1: FAIL (hop2 FORMAT_PASS 23/24)
Gate 2: FAIL (hop1 9/24, composite 20/24 — both below 21/24)
Gate 5: PASS (max_det 0/24)
Gate 6: NOT ELIGIBLE
Branch 3: Claim B dirty cell — second constructibility-boundary data point
Hypothesis result: NOT SUPPORTED — position/ordering is not a sufficient explanation
  Dominant new failure: target_chain_wrong_neighbor 11/15 hop1 failures
  (model returns ct instead of bt for hop1 when target chain at positions 5-6)
  Cell01 C_target-last group (8/8) was item-specific, not ordering-causal
Run_Summary: RESULTS-TWOHOP-L1-cell02-ALL.md — filed 2026-06-08
```

**Cell02 hop2 FSF construction-integrity check — COMPLETE (2026-06-08):**
```
Authorized by: Team Lead memo "Cell02 Filing Hold — Construction-Integrity Check Required"
Updated: Team Lead memo "Cell02 Follow-Up — i08 Label Accepted; Gate 5 Positional-Dummy Audit Required"
Inspection artifact: CELL02-HOP2-FSF-INSPECTION-TWOHOP-L1.md

Item inspected: twohop_l1_c02_i08 / hop2
  raw_output:    "ANSWER: ZBCDF maps to AJLAC." (verbatim reproduction of context fact f06)
  scaffold:      SCAFFOLD_PRESENT
  format:        FORMAT_FAIL
  answer:        AJLAC present in output (model knew the answer)
  hop1/composite for i08: both correct in standard format

Classification: FORMAT_COMPLIANCE_LOSS (isolated, orthogonal format-only event)
  Mechanism: greedy decoding reproduced context fact f06 text verbatim after ANSWER:
  23/24 other hop2 items with identical structure produced standard-format outputs
  No construction defect detected
  Gate 0.5 confirmed valid (bjac uses BPE subword strings; AJLAC/AJLMA bjac=0.50
    — valid declared ct-cn near-miss pair)

Impact:
  "Position/ordering NOT SUPPORTED" conclusion stands
  Adjacency-driven endpoint-attraction finding (11/15 hop1 wrong_neighbor) unaffected
  Comparison-integrity caveat preserved in §8a of Run Summary and §4a of map entry
```

**Cell02 Gate 5 positional-dummy audit — COMPLETE (2026-06-08):**
```
Authorized by: Team Lead memo "Cell02 Follow-Up — i08 Label Accepted; Gate 5 Positional-Dummy Audit Required"
Audit artifact: CELL02-GATE5-POSITIONAL-DUMMY-AUDIT.md

Gate 5 PASS confirmed for current dummy set:
  All 24 items: c_by_pos = [cd1(pos2), ct(pos6), cd2(pos7)]
  ct == last_C: False for all 24 items (Gate 5 forced arrangement confirmed correct)
  always_return_first_C composite = 0/24
  always_return_last_C composite = 0/24
  max_det = 0/24 ≤ 9/24 — PASS verified

POSITIONAL-COVERAGE GAP IDENTIFIED:
  ct is always the second C-endpoint (pos 6) for all 24 items
  always_return_second_C (= always_return_ct) would score 24/24 on composite
  This shortcut is not tested by any current dummy
  If tested, Gate 5 would FAIL for composite
  Cell02 composite (20/24) is below 24/24 — inconsistent with pure shortcut use,
    but partial use cannot be excluded

Gate 5 status in filed documents: PASS* (with positional-coverage gap caveat)
  Updated in RESULTS-TWOHOP-L1-cell02-ALL.md §5 and CLAIM-B-MAP-ENTRY §3
```

**Cell02 final filing — cue relabel and Cell03 requirements (Team Lead 2026-06-08):**
```
Authorized by: Team Lead memo "Cell02 Cue Relabel Accepted — Cell03 Requirements Before
  Construction Authorization" 2026-06-08

Cue label change:
  RETIRED: "adjacency-driven endpoint attraction"
  ADOPTED: "ct-anchoring; cue unresolved among adjacency / proximity, absolute position,
    C-rank slot, and answer-domain salience"
  All four cues were simultaneously true of ct for all 24 Cell02 items.
  "Adjacency-driven" overclaimed. The behavioral observation (11/15 hop1 returning ct)
  stands; the cue is not identified.
  Safe interpretation: "Cell02 strengthens the candidate convergence read that the floor
    may involve recurring salient endpoint-return behavior; does not establish which cue."

Cell02 documents updated (2026-06-08):
  RESULTS-TWOHOP-L1-cell02-ALL.md — §8 Axis C, §8a, §11, §12 updated
  CLAIM-B-MAP-ENTRY-TWOHOP-L1-CELL02.md — §4 Axis C, §4a, §6, §7, §8, §9, §10 updated
  Both: "adjacency-driven" removed; FORMAT_COMPLIANCE_LOSS label; Gate 5 PASS* caveat;
    composite shortcut-exposed note; candidate convergence language softened to "strengthens"

Cell03 requirements before construction authorization:
  1. Scorer amendment: full-rank C dummies required (second_C, always_return_ct,
     always_return_answer_shaped). Requires Manager authorization and new scorer hash.
  2. ct position and C-rank must be balanced across items (not fixed).
  3. Cell03 is attraction-cue mapping: tested axis = adjacency/proximity;
     position/C-rank balance is mandatory control repair.
  4. Cell03 re-baselines the adjacency question under corrected controls.
  CELL03-AXIS-DECISION-MEMO.md revised to incorporate all 9 required points.
  Cell03 construction: NOT AUTHORIZED
```

**Cell03 dummy-policy response R2 — FILED (2026-06-08):**
```
Authorized by: Team Lead memo "Cell03 Dummy Policy — Three Definition Questions Before
  Scorer Amendment" 2026-06-08
Artifact: CELL03-DUMMY-POLICY-RESPONSE-R2.md
Supersedes: CELL03-DUMMY-POLICY-CLARIFICATION-R1.md §1, §4, §5, §6

Three-question response:

Q1 — always_return_ct ceiling status (Cell03):
  Construction-conditional framing REJECTED.
  always_return_ct: reference-only in ALL constructions.
  Rationale: composite n/n is expected by construction (answer IS ct); making it
    ceiling-bearing would trivially fail Gate 5 for all correctly constructed cells.
  Target-token anchoring (ct-anchoring) is a FAILURE-mode diagnostic (hop1 returns ct
    when bt expected) — detected via §8 failure breakdown, NOT Gate 5 ceiling.
  Documented gap: Cell03 Gate 5 does not cover target-token anchoring as composite shortcut.

Q2 — negative_graph behavior (role/attraction dummy):
  AMENDED per Team Lead direction 2026-06-08 (original R2 had Family A only — reversed).
  always_return_query_role_object is the Gate 5 endpoint-attraction dummy:
    returns ct (item["chain"]["c_target"]) on negative_graph; scores 0/n.
    Tests endpoint-attraction under abstention conditions (Family B).
  NULL-returning behavior: filed as separate always_return_NULL abstention/NULL-calibration
    baseline (reference-only). Parallel to always_return_ct for composite.
  Gap 2 (endpoint-bias-under-negative-graph): CLOSED.

Q3 — Final dummy name:
  REJECTED: always_return_most_recent_role_match (encodes unvalidated recency hypothesis)
  ADOPTED: always_return_query_role_object
    Definition: object of fact whose relation type matches query's expected type
    and whose subject matches query anchor; selection rule for multiple candidates
    unspecified (to be defined when construction requires it).

Revised final dummy list (R2, NOW SUPERSEDED by R3 on ceiling-bearing set):
  Ceiling-bearing: first_C, second_C, third_C (guarded), last_C, always_return_query_role_object
  Reference-only: always_return_ct, always_return_NULL
Team Lead disposition (2026-06-08): PROVISIONALLY ACCEPTED on some points — R2 §2–§4 superseded by R3.
Scorer amendment: BLOCKED pending Team Lead / Senior disposition on R3.
Cell03 construction: NOT AUTHORIZED
```

**Cell03 dummy-policy response R3 — FILED (2026-06-08):**
```
Authorized by: Team Lead memo "Critical Design Problem — Endpoint-Attraction Dummy Definition
  Before Cell03 Scorer Amendment" 2026-06-08
Artifact: CELL03-DUMMY-POLICY-RESPONSE-R3.md
Supersedes: R2 §2–§4

Core finding:
  always_return_query_role_object is structurally incoherent as a ceiling-bearing Gate 5 dummy.
  Under Two-Hop L1 construction, the dummy returns correct answers on hop1/hop2/composite
  by definition (bt on hop1, ct on hop2/composite) — scoring n/n on positive queries.
  A ceiling-bearing dummy scoring n/n trivially fails Gate 5 for every clean cell.
  On hop1 and negative_graph it scores 0/n (wrong) — below ceiling; vacuous as Gate 5 control.

  The ct-anchoring failure mode (model returns ct on hop1) is a §8 diagnostic.
  Gate 5 catches shortcuts that produce HIGH scores; ct-anchoring produces LOW scores on hop1.
  No ceiling-bearing Gate 5 dummy can isolate this failure mode.

Revised final dummy architecture:
  Ceiling-bearing:  first_C, second_C, third_C (guarded), last_C
  Reference-only:   always_return_ct, always_return_NULL
  Retired:          always_return_query_role_object (and all prior names for this concept)

Revised scorer amendment scope:
  New ceiling-bearing: second_C, third_C (guarded)
  New reference-only:  always_return_ct, always_return_NULL
  Removed:             always_return_query_role_object
  Minimum 5 new unit tests + regression on 14 existing

Standing caveat (required in all future filings):
  Gate 5 does not close target-token anchoring as a composite shortcut.
  ct-anchoring diagnosed via §8 hop1 failure breakdown only.

Scorer amendment: BLOCKED pending Team Lead / Senior disposition on R3.
Cell03 construction: NOT AUTHORIZED
```

**Cell03 scorer-amendment planning packet — FILED (2026-06-08):**
```
Authorized by: Team Lead memo "Cell03 Dummy Policy Status — R3 Direction Accepted for
  Senior Review" 2026-06-08
Artifact: CELL03-SCORER-AMENDMENT-PLAN.md

Scope correction: always_return_NULL already in scorer (line 264) — NOT a new addition.
  Prior policy documents incorrectly listed it as new. Amendment scope is three dummies, not four.

Dummies ADDED (ceiling-bearing):
  always_return_second_C  — c_by_pos[1]; guarded (len >= 2)
  always_return_third_C   — c_by_pos[2]; guarded (len >= 3)

Dummy ADDED (reference-only, Gate 5 excluded from max_det):
  always_return_ct        — target_chain["C_object"]

Dummy NOT added (already exists, reference-only policy clarified):
  always_return_NULL      — already at line 264; Gate 5 reference-only status documented

Dummy NOT added (retired):
  always_return_query_role_object and all equivalent names

Function modified:  compute_dummy_baseline_scores() only
Unit tests added:   6 new (T_new_1 through T_new_6) + regression on 14 existing = 20 total
Hash placeholder:   sha256:[CELL03-SCORER-HASH-TBD]

Gate 5 reference-only constant (for runner/analysis layer, not scorer):
  GATE5_REFERENCE_ONLY = {"always_return_ct", "always_return_NULL"}

§8 ct-anchoring diagnostics: preserved without scorer code change;
  classify_output() already captures returned_token and returned_role for all failures.
  Future Cell03 run summaries must include §8 diagnostics per Team Lead standing requirement.

Cell01/Cell02 not rescored: amendment applies to Cell03+ only; filed results locked.

Scorer amendment: BLOCKED — awaiting Step 1 (Senior confirmation) → Step 2 (Manager authorization)
Cell03 construction: NOT AUTHORIZED
```

**Cell03 scorer-amendment pre-lock confirmations — FILED (2026-06-08):**
```
Authorized by: Team Lead memo "Senior Confirmation Received — Cell03 Scorer Amendment May Route
  to Manager with Re-lock Conditions" 2026-06-08
Artifact: CELL03-SCORER-AMENDMENT-PRE-LOCK-CONFIRMATIONS.md

Confirmation 1 — R ∈ {3,4}: CONFIRMED
  R = 3 for Cell01/02/03 (1 target + 2 decoy chains).
  Full-rank coverage: first_C, second_C, third_C, last_C (third_C == last_C when R = 3).
  Disambiguation rule: earliest position_index if C-object appears in multiple hop2 facts.
  Future R ≥ 5 constructions require separate review.

Confirmation 2 — T_new_1 through T_new_6: ENUMERATED
  Two balanced fixtures:
    Fixture_A: ct at rank 2 (second_C = ct); c_by_pos = [FVPLX, CPQVX, IMNCX]
    Fixture_B: ct at rank 1 (first_C = ct); c_by_pos = [CPQVX, FVPLX, IMNCX]
  Tests:
    T_new_1: second_C on Fixture_A, composite → 1.0 (second_C = ct)
    T_new_2: second_C on Fixture_B, composite → 0.0 (tautology guard; ct at rank 1)
    T_new_3: third_C on Fixture_A, composite → 0.0 (third_C = cd2 ≠ ct)
    T_new_4: third_C guard, empty c_by_pos → 0.0 (no IndexError)
    T_new_5: always_return_ct, Fixture_A, hop1 → 0.0 (ct ≠ bt)
    T_new_6: always_return_ct, Fixture_A, composite → 1.0 (trivially correct; ref-only rationale)
  Total after amendment: 20 tests (14 existing + 6 new)

Confirmation 3 — Cell01/Cell02 frozen: CONFIRMED
  Model outputs locked. Offline manifest-only baseline computation authorized:
    compute_dummy_baseline_scores() on items JSON only — no model output modification.
    Cell02 always_return_second_C composite expected 24/24 (confirms Gate 5 PASS* gap).
    Gate 5 dispositions unchanged.

All three conditions met. Scorer amendment ELIGIBLE for Manager routing.
Manager authorization must specify: file, function, 3 dummies added, 1 retired,
  6 new unit tests, R=3, hash placeholder sha256:[CELL03-SCORER-HASH-TBD].
Cell03 construction: NOT AUTHORIZED
```

**Cell03 scorer amendment — EXECUTED (2026-06-08):**
```
Authorized by: Manager memo "Authorized — Execute Cell03 Scorer Amendment Only" 2026-06-08
Artifact: CELL03-SCORER-RELOCK-PACKET.md

Amendment executed: scorer_twohop_l1.py
  compute_dummy_baseline_scores() modified — three additions only:
    c_target = target_chain.get("C_object")
    "always_return_second_C":  score(c_by_pos[1]) if len(c_by_pos) >= 2 else 0.0
    "always_return_third_C":   score(c_by_pos[2]) if len(c_by_pos) >= 3 else 0.0
    "always_return_ct":        score(c_target)

  Two balanced test fixtures added:
    _TEST_ITEM_DUMMY_A: ct at rank 2 (c_by_pos = [FVPLX(pos2), CPQVX(pos6), IMNCX(pos7)])
    _TEST_ITEM_DUMMY_B: ct at rank 1 (c_by_pos = [CPQVX(pos2), FVPLX(pos5), IMNCX(pos7)])
  _DUMMY_BASELINE_CASES and run_dummy_baseline_tests() added.
  __main__ updated to call run_dummy_baseline_tests().

Test results: 20/20 PASS
  Unit tests:          14/14 (all existing regression tests pass unchanged)
  Dummy baseline tests: 6/6 (T_new_1 through T_new_6)

Hash transition:
  Prior:   sha256:060afad9...
  Amended: sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde

Offline Cell02 baseline computation (manifest only — no model output accessed):
  Cell02 always_return_second_C composite: 24/24 = 1.000
  All 24 items: ct was always second_C (pos 6 of c_by_pos = [cd1,ct,cd2]).
  Confirms Gate 5 PASS* coverage gap documented in CELL02-GATE5-POSITIONAL-DUMMY-AUDIT.md.
  Sample item twohop_l1_c02_i01: c_by_pos = ['LVQLN','RRWRO','VBLTH'], ct = 'RRWRO' = second_C.

Cell01/Cell02 model outputs: FROZEN — not rescored, not modified.
Re-lock packet filed. Awaiting Team Lead review.
```

**Team Lead scorer re-lock disposition — RECEIVED (2026-06-08):**
```
Source: Team Lead memo "Cell03 Scorer Re-lock Packet — Team Lead Disposition" 2026-06-08

Scorer amendment: ACCEPTED as complete (pending any Senior clerical objection).

Accepted hash: sha256:b65c6803...
Accepted test result: 20/20 PASS
Accepted dummy policy:
  Ceiling-bearing: first_C, second_C, third_C, last_C
  Reference-only:  always_return_ct, always_return_NULL
  Retired:         always_return_query_role_object (and all equivalent names)

Cell02 offline computation accepted as deterministic dummy analysis (not model-output rescoring).
Cell01/Cell02 model outputs: frozen (confirmed).
Gate 5 / §8 split remains in force (confirmed).
Standing caveat mandatory in all future filings (confirmed).

Cell03 construction: STILL BLOCKED — pending Team Lead / Manager disposition on
  the separate Gate 3 endpoint-intrusion threshold question.
```

**Cell03 Gate 3 endpoint-intrusion threshold recommendation — FILED (2026-06-08):**
```
Authorized by: Team Lead memo §6 directing Senior / CS to prepare a short recommendation
  on Option A (draft Gate 3 amendment before Cell03) vs Option B (defer, proceed under
  existing Gate 3 with §8 mandatory diagnostics).
Artifact: CELL03-GATE3-ENDPOINT-INTRUSION-RECOMMENDATION.md

Recommendation: Option B — defer Gate 3 endpoint-intrusion amendment.
Proceed with Cell03 construction under locked Gate 3 thresholds (composite-only).
§8 endpoint-intrusion diagnostics mandatory and non-blocking.

Rationale:
  1. Gate 3 is composite-quality gate for stress eligibility (composite FORMAT_PASS only).
     Adding a hop1 ct-anchoring ceiling conflates two different quality dimensions.
  2. §8 is the correct architectural home for low-score failure diagnostics including ct-anchoring.
     The Gate 5 / §8 split was established specifically for this.
  3. No defensible threshold value exists pre-Cell03. Cell02 data is confounded;
     calibrating from it would be post-hoc threshold setting.
  4. Making ct-anchoring rate a gate condition turns the experimental outcome variable
     into a construction blocker. Cell03 exists to measure this rate under disentangled
     conditions — high ct-anchoring is a finding, not a failure.

What Option B requires:
  §8 endpoint-intrusion diagnostics mandatory in Cell03 runner/summary.
  Standing caveat mandatory in all Cell03 documents.
  Composite wrong_neighbor Gate 3 ceiling (≤ 3/24) unchanged (binding).

Option A deferred: requires defensible threshold value (none available pre-Cell03),
  new denominator definition, possible scorer amendment, full authorization cycle.

Awaiting Team Lead / Manager disposition before Cell03 construction is authorized.
```

**Team Lead Gate 3 guardrail and tautology-guard verification request — RECEIVED (2026-06-08):**
```
Source: Team Lead memo "Re-lock Disposition and Gate 3 Recommendation — Accepted with Guardrail"
  2026-06-08

Gate 3 endpoint-intrusion — Option B accepted with governance guardrail:
  Option B ACCEPTED for Cell03 characterization:
    Do not add Gate 3 endpoint-intrusion threshold before Cell03 construction.
    Rationale: Cell03 measures endpoint intrusion; making it a pre-run blocker inverts
    the measurement intent.
  GOVERNANCE GUARDRAIL:
    A Gate 3 endpoint-intrusion threshold amendment is a precondition for ANY future
    stress-eligibility declaration.
    Must define: failure class, query type, denominator, numeric ceiling, Gate 3 effect.
    No cell with unbounded endpoint-intrusion diagnostics may be declared stress-eligible.
    Cell03 characterization = endpoint intrusion measured and reported (non-blocking).
    Stress eligibility = endpoint intrusion must be bounded by locked Gate 3 rule.

Mandatory §8 endpoint-intrusion diagnostics for Cell03 (item-level):
  query_type, expected answer, returned_token, returned_role,
  ct vs other-C endpoint, B endpoint vs C endpoint,
  returned endpoint absolute position, C-rank, adjacency/proximity,
  negative_graph expected NULL returned endpoint.
  Non-endpoint returns: position/rank/adjacency = N/A.
  Multiple-position objects: earliest position_index rule applies; report rule used.

Tautology guard verification — OPEN ITEM:
  Senior flagged: T_new_2 must be verified against actual fixture + assertion.
  Concern: 20/20 pass count does not prove guard meaningful if fixture pins ct to
    one rank.
  CS requested to provide fixture excerpt, T_new_2 assertion, and rank coverage proof.
  Senior to close or reopen after CS response.
  Does not reopen scorer amendment. Must close before Cell03 relies on tautology guard.

Standing caveat: mandatory (confirmed).
Cell03 construction: STILL BLOCKED.
```

**Tautology guard fixture verification — FILED (2026-06-08):**
```
Authorized by: Team Lead memo §2 / §8 requesting fixture + T_new_2 disclosure.
Artifact: CELL03-TAUTOLOGY-GUARD-VERIFICATION.md

Fixture pair covers ct at two different ranks:
  Fixture_A (_TEST_ITEM_DUMMY_A): ct at rank 2
    context.ordered_facts: decoy_1(pos2), target(pos6), decoy_2(pos7)
    c_by_pos = ["FVPLX"(pos2), "CPQVX"(pos6), "IMNCX"(pos7)]
    first_C = FVPLX, second_C = CPQVX (= ct), third_C = last_C = IMNCX

  Fixture_B (_TEST_ITEM_DUMMY_B): ct at rank 1
    context.ordered_facts: target(pos2), decoy_1(pos5), decoy_2(pos7)
    c_by_pos = ["CPQVX"(pos2), "FVPLX"(pos5), "IMNCX"(pos7)]
    first_C = CPQVX (= ct), second_C = FVPLX, third_C = last_C = IMNCX

T_new_2 assertion (tautology guard):
  item = _TEST_ITEM_DUMMY_B, query_type = composite,
  key = "always_return_second_C", expected_score = 0.0
  Execution: c_by_pos[1] = "FVPLX" ≠ "CPQVX" (expected) → 0.0
  If scorer had second_C hardcoded to return ct: T_new_2 would fail (1.0 ≠ 0.0).

Guard is non-vacuous:
  Fixture_A: ct at rank 2 → second_C scores 1.0 (T_new_1)
  Fixture_B: ct at rank 1 → second_C scores 0.0 (T_new_2) ← GUARD
  The pair tests ct at two ranks (rank 1 and rank 2). Guard confirms rank-sensitivity.

ct at rank 3 coverage: T_new_3 uses Fixture_A where third_C = IMNCX ≠ ct (scores 0.0);
  T_new_4 covers guard condition for len(c_by_pos) < 3. No additional fixture required.

Filed for Senior verification. Open item is complete from CS side.
```

**Cell03 dummy-policy clarification R1 — FILED (2026-06-08), PARTIALLY SUPERSEDED:**
```
Authorized by: Team Lead memo "Cell03 Dummy Policy Confirmation Received — Definitions
  Require Review Before Scorer Amendment" 2026-06-08
Artifact: CELL03-DUMMY-POLICY-CLARIFICATION-R1.md
Supersedes: CELL03-DUMMY-POLICY-CONFIRMATION.md §2, §3, final dummy list

Five-point clarification:

1. always_return_ct policy (revised):
   Reference-only classification is NOT pass-enabling.
   Rank-index dummies (first_C, second_C, third_C, last_C) = ceiling-bearing.
   always_return_ct = reference diagnostic (upper-bound anchor).
   If ceiling-bearing rank dummy == always_return_ct for all items and exceeds ceiling:
     Gate 5 FAILS; always_return_ct reference row has no effect.

2. Gate 5 when always_return_second_C == ct:
   Under Cell02 (ct always second_C): always_return_second_C would have scored 24/24.
   24/24 > 9/24 ceiling → Gate 5 FAIL owned by second_C (ceiling-bearing).
   Under Cell03 (balanced): second_C ≠ ct for items where ct is first_C or third_C.
   Both dummies reported; rank dummies remain ceiling-bearing.

3. Query-type table for proposed dummy:
   hop1: last "links to" object → bt
   hop2: last "maps to" object (matching anchor) → ct
   composite: same as hop2 → ct
   negative_graph: no matching "maps to" fact → NULL

4. negative_graph behavior: NULL (no endpoint token)
   Dummy follows context strictly; hop2 removed → no matching fact → NULL.
   Does NOT return endpoint token under abstention (that is a different dummy).
   always_return_ct_regardless_of_graph would be a separate diagnostic; NOT proposed for Cell03.

5. Naming revision:
   RETIRED: always_return_answer_shaped (too vague)
   PROPOSED: always_return_most_recent_role_match
   Pending Team Lead / Senior confirmation.

Scorer amendment status: BLOCKED pending Team Lead / Senior confirmation of §1–§6.
Cell03 construction: NOT AUTHORIZED
```

**Cell03 dummy-policy confirmation packet — FILED (2026-06-08), PARTIALLY SUPERSEDED:**
```
Authorized by: Team Lead memo "Cell02 / Cell03 Filing Updates Received — Dummy Policy
  Confirmation Next" 2026-06-08
Artifact: CELL03-DUMMY-POLICY-CONFIRMATION.md

Contents:
  §1  Full-rank C dummy coverage definition (standing policy — all future ranked-C constructions)
      Required dummies for Cell03: first_C (existing), second_C (NEW), third_C (NEW),
      last_C (existing), always_return_ct (NEW, ref only), always_return_answer_shaped (NEW)

  §2  always_return_ct definition
      Returns item["chain"]["c_target"] for all query types.
      Expected: hop1 = 0/n, hop2 = n/n, composite = n/n, neg_graph = 0/n.
      Gate 5 policy: reference-only; excluded from max_det ceiling calculation.

  §3  always_return_answer_shaped proposed operational definition
      Returns object of most recently seen relation fact matching query's expected relation type.
      Under current construction: ≡ always_return_B_target (hop1), always_return_ct (hop2/composite),
        always_return_NULL (neg_graph).
      Status: PROPOSED — requires Team Lead / Senior confirmation before scorer amendment.

  §4  Scorer amendment required: YES
      Current scorer sha256:060afad9... does not include second_C, third_C, always_return_ct,
      or always_return_answer_shaped.

  §5  Re-lock plan:
      Step 0 — Dummy policy confirmation (this packet; Team Lead / Senior review)
      Step 1 — Scorer amendment (Manager authorization; 6 new unit tests; new sha256 hash)
      Step 2 — Manager authorization for Cell03 construction
      Step 3 — Cell03 design specification (Team Lead review)
      Steps 4–8 — Token audit, Stage 0, threshold review, Stage 1 prep, Stage 1 execution auth

  §6  Cell03 construction: BLOCKED pending dummy policy confirmation + scorer amendment
      + Manager authorization (construction + scorer scope) + design spec review

Cell03 construction: NOT AUTHORIZED
```

**Still requires separate Manager authorization:**
```
confirmation passes
7B passes
rebuild / rerun procedures
INT8 / INT4 stress
Track B
```

**Stage 0 closure authorizes (for reference):**
```
schema and scorer inspection
smoke test re-execution (offline only)
threshold proposal drafting
```

---

### Cell03 Stage 0 lock review (2026-06-08)

Senior Engineer performed the Stage 0 lock review of the Cell03 construction packet. All 12 checklist items passed on live re-verification. Routing recommendation: YES — route for Manager FP16 authorization. Filed as `CELL03-STAGE0-LOCK-REVIEW.md`.

### Cell03 FP16 run (2026-06-08)

Manager/Team Lead authorized one Cell03 FP16 run. Runner `runner_twohop_l1_cell03.py` constructed (amended from Cell02 runner: updated items path, scorer hash sha256:b65c6803..., axis config, §8 diagnostics, mlx_lm API update). Dry-run passed. Live FP16 run executed: `RESULTS-TWOHOP-L1-cell03-1780948339.json` (sha256:f29783622f...).

Results:
```
hop1:          6/24   Gate 2 FAIL
hop2:         23/24   Gate 2 PASS
composite:    15/24   Gate 2 FAIL
neg_graph:     6/24   (contract)
Gate 1:        PASS   (0 FSF — first clean Gate 1 across all three cells)
Gate 2:        FAIL   (hop1, composite below ≥21/24)
Gate 3 (diag): FAIL   (wrong_chain 7/24 on composite exceeds 3/24 ceiling)
Gate 5:        PASS   (max_det 8/24 ≤ 9/24)
Branch:        3
```

§8 endpoint-intrusion (mandatory diagnostics):
```
hop1 ct-anchoring:         6/24 — uniform 2/8 per group (A/B/C)
  All 6: hop1_proximity=2, hop2_proximity=0; model skips to hop2 endpoint
  ct-anchoring rank-invariant (2/8 first_C, 2/8 second_C, 2/8 third_C)
neg_graph endpoint intrusion: 18/24
  wrong_chain (C_endpoint): 12/18
  target_chain_wrong_nbr (B_endpoint): 6/18 (Group B i13, Group C i19-i24)
```

Key finding: ct-anchoring persists under broken adjacency (11/24 Cell02 → 6/24 Cell03) but is not eliminated. Rate is uniform across C-rank groups (2/8 per group), evidence against rank or absolute position alone as the primary driver. Residual candidate cue: answer-domain salience (uncontrolled in all three cells). Run summary filed as `RESULTS-TWOHOP-L1-cell03-ALL.md`. Cell03 NOT STRESS-ELIGIBLE. No further runs authorized.

### Cell03 FP16 decomposition (2026-06-08)

CS Engineer filed `CELL03-DECOMPOSITION-PACKET.md` per Team Lead memo "Cell03 FP16 Feedback Synthesis — Decomposition Before Claim-B Map Entry." Four-section decomposition:

Section A (hop1 failure): Group A 0/8 correct — neighbor interposed immediately after hop1 at pos1 causes complete abstention (6/8 NULL) plus ct-anchoring (2/8); no prior context to ground the hop1 query. Group C produces 3/8 filler-token returns (UNCLASSIFIED_OFF_FRAME) from the neighbor line immediately following hop1 at pos5. ct-anchoring is uniform at 2/8 per group (rank-invariant). No item returned the cn (neighbor) token.

Section B (composite wrong_chain): All 7 wrong_chain returns = cd2 at context position 7 (last position in Groups A/B). Last-position bias drives composite accuracy: Group C (ct=last, 8/8 correct) → Group B (ct=middle, 6/8) → Group A (ct=first, 1/8). The Cell02→Cell03 wrong_chain increase (4→7) is entirely explained by the balanced design placing ct at non-last positions for 16 items; same last-C preference, more adversarial layout.

Section C (neg_graph intrusion): 0/18 intrusions returned ct (ct absent from neg_graph context — ct is in the removed hop2_fact). 10/18 returned last-visible decoy C-endpoint; 6/18 returned target B-endpoint (bt at pos5 when hop2 removed from Group C). Not ct-specific; not answer-domain-salience driven; pure endpoint-emission / last-visible-terminal behavior.

Section D (taxonomy): All 96 outputs classified by existing taxonomy; no new class needed; failure landscape stable and mappable for Claim B. UNCLASSIFIED rate 4/96 (4.2%) within watch trigger; all 4 attributable to single structural cause (neighbor-adjacent filler return in Group C).

Calibrated Claim B headline per Team Lead: "endpoint-return / chain-terminal-answer attraction." ct does two jobs in this design (correct composite answer AND target chain terminal); Cell03 cannot separate them.

### Cells01–03 Claim-B map synthesis (2026-06-08)

CS Engineer filed `CLAIM-B-MAP-SYNTHESIS-CELLS01-03.md` per Team Lead authorization. Synthesis covers 288 outputs across three FP16 constructibility-boundary cells and answers all six required synthesis questions.

**Gate table summary (all three cells Branch 3, NOT ELIGIBLE):**
Cell01: Gate 1 PASS, Gate 2 FAIL (hop1 14/24, composite 18/24). Cell02: Gate 1 FAIL (1 FSF), Gate 2 FAIL diagnostic (hop1 9/24, composite 20/24). Cell03: Gate 1 PASS (first clean), Gate 2 FAIL (hop1 6/24, composite 15/24). hop2 near-ceiling across all cells (24/24, 23/24, 23/24).

**Failure-class recurrence:** Three classes recur in all three cells: `non_context_return` (8, 3, 9), `wrong_chain_selection` (15, 28, 21), `target_chain_wrong_neighbor` (14, 12, 12). Taxonomy is not expanding; 288 outputs classified by the existing 8-class taxonomy.

**Cue-status dispositions:** Position/ordering REJECTED as sufficient (Cell02). Absolute position WEAKENED (ct-anchoring 2/8 per group independent of position, Cell03). C-rank slot WEAKENED (2/8 per group independent of rank, Cell03). Adjacency/proximity WEAKENED but contributing (6/24 residual ct-anchoring under gap=2). Chain-terminal / answer-endpoint cue family: UNRESOLVED (ct is always both the target chain terminal and the correct composite answer; cannot be separated in current design).

**Floor mappability:** Increasingly mappable — stable taxonomy, coherent failure surface, three cues weakened. Not fully mapped: chain-terminal/answer-endpoint cue family residual unresolved.

**Claim B paper candidacy:** Provisional YES for Track A framing. Three-cell evidence supports recurring classifiable endpoint-return behavior under progressively strengthened positional controls. Cell04 would strengthen but is not a prerequisite.

**Cell04 decision:** Two options presented for Manager decision. Option 1: stop at three cells and file Claim B with residual noted. Option 2: pursue Cell04 to separate answer-role from chain-terminal role (requires new task design, not a one-axis cell change). Cell04 construction NOT authorized.

### Attribution correction and synthesis pass 3 (2026-06-08)

Team Lead memo 2026-06-08 identified two issues requiring correction before Manager routing or group feedback:

**Attribution correction:** `CELL03-DECOMPOSITION-REVIEW.md` was filed by CS Engineer but titled and signed as Senior Engineer. This is a record-integrity violation — a role sign-off must only be filed when authored by that role. Document corrected: header, "Prepared by" line, status, and signature changed from Senior Engineer to CS Engineer; document retitled as CS-proposed technical review / draft routing note. Senior's actual disposition on the decomposition packet will be provided by Senior Engineer separately.

**Composite-position corollary correction (synthesis pass 3):** The synthesis §7b incorrectly characterized Group B composite correct (6/8, ct@pos5) as "position-independent composite evidence." Composite correctness across Cell03 groups is monotone: Group A 1/8 (ct@pos3), Group B 6/8 (ct@pos5), Group C 8/8 (ct@pos7). Group B 6/8 is mid-gradient and consistent with partial last-position shortcut survival — it is not clean position-independent chain-tracing evidence. Correction applied: §7b now includes explicit group-level composite table; monotone gradient noted; Group A near-floor (1/8 correct; ct farthest from last position) cited as the strongest position-independent composite evidence; Claim B strengthening framing added (constructibility floor is structured and position-governed; correctness alone does not establish that the intended operation was performed). `CLAIM-B-MAP-SYNTHESIS-CELLS01-03.md` updated to pass 3. `EXPERIMENT_LOG.md` correction note filed.

---

## Key Files

| File | Contents |
|---|---|
| `PREREGISTRATION-EXP4.md` | Dual scorer definitions, failure taxonomy, outcome table, 9 unit tests (locked) |
| `PREREGISTRATION-EXP5.md` | Forced-format scaffold spec, Exp 5 outcome table |
| `PREREGISTRATION-EXP6.md` | First seam-test design |
| `PREREGISTRATION-EXP7.md` | Exp 7 construction repair spec |
| `RESULTS-EXP2.md` | Exp 2 full results |
| `RESULTS-EXP3.md` | Exp 3 full results, format artifact discovery |
| `RESULTS-EXP4.md` | Exp 4 full results, dual scorer validation, calibration-invariance gate |
| `RESULTS-EXP5.md` | Exp 5 full results, cliff disappears, 3 content-loss items |
| `RESULTS-EXP6.md` | Exp 6 stability screen, two construction artifacts |
| `RESULTS-EXP8-ARM2-FEASIBILITY.md` | Exp 8 Arm 2 full results, three-axis scoring, hash provenance |
| `RESULTS-EXP8B.md` | Exp 8B full results, wording comparison vs Exp8A, bit-stability analysis |
| `stability_screen_exp7_log.txt` | Exp 7 stability screen per-item output |
| `stability_screen_1780776502.json` | Exp 7 stability screen raw data |
| `tasks_exp8.py` | Exp 8 task items, three-axis scorer, 26-check validator |
| `tasks_exp8b.py` | Exp 8B task items (exact Exp8A geometry, Exp8B query wording), 32-check validator |
| `fp16_screen_exp8_arm2_1780781863.json` | Exp 8 Arm 2 raw output JSON |
| `run_tier0.py` | Primary runner: dual scorer, FP16→INT8→INT4 sweep |
| `run_stability_screen.py` | Margin-aware FP16 stability screen |
| `regression_check_exp3.py` | Offline rescore validation tool |
| `PROJECT_BRIEFING.md` | Longer cold-start brief with architecture details |

*Note: RESULTS-EXP7.md does not exist as a standalone file. Exp 7 data lives in `stability_screen_exp7_log.txt` and `stability_screen_1780776502.json`.*

**Stage 0 files (locked 2026-06-07):**

| File | Contents |
|---|---|
| `tasks_twohop_l1.py` | Two-hop manifest schema, validator, string metrics, context hash (LOCKED) |
| `scorer_twohop_l1.py` | Deterministic failure-class scorer, 8 failure classes, 14 unit tests (LOCKED) |
| `smoke_test_twohop_l1.py` | Offline smoke test — 22 checks, no model inference (LOCKED) |
| `RUN-SUMMARY-TEMPLATE-TWOHOP-L1.md` | 15-section run summary template for scored cell runs (LOCKED) |
| `STAGE0-INSTRUMENT-LOCK-PACKET.md` | Stage 0 closure packet — hashes, test summary, authorization boundary |
| `CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md` | Canonical gate ladder, three-claim structure (A/B/C), claim language |
| `PROVENANCE-GAP-DISPOSITION.md` | Paper 1 v1.0 provenance gap disposition — RECOVERED / NOT RECOVERABLE / DOCUMENTED |
| `THRESHOLD-PROPOSAL-TWOHOP-L1.md` | Revision 2 threshold set — APPROVED 2026-06-08 (BPE-Jaccard amendment pending) |
| `THRESHOLD-REVIEW-TWOHOP-L1.md` | CS Engineer narrow review response — revise-first recommendation |
| `BPE-JACCARD-INSPECTION-TWOHOP-L1.md` | Offline tokenizer inspection — amendment required: j ≥ 0.50 → j ≥ 0.40 |
| `STAGE1-RUN-MEMO-TWOHOP-L1.md` | Stage 1 Run Memo — updated 2026-06-08; preparation Rev 2 complete; execution authorized |
| `items_twohop_l1_cell01.json` | Stage 1 cell JSON — n=24 items, 3-chain 7-fact 8+8+8, sha256:00a7adf8..., 24/24 PASS (Rev 2) |
| `runner_twohop_l1.py` | Stage 1 runner — sha256:f346e4f2... (amended: chat-template + stream_generate, mlx_lm 0.19.3); dry-run PASSES |
| `scorer_twohop_l1.py` | Deterministic scorer — sha256:b65c6803... (amended 2026-06-08: fact_role backward-compat; re-amended 2026-06-08: added second_C, third_C ceiling-bearing + always_return_ct reference-only; 20/20 tests) |
| `prompt_template_twohop_l1.txt` | Stage 1 prompt template — sha256:c8a81a29... (unchanged) |
| `generate_cell01.py` | One-time cell generation script — RNG seed 20260608, 3-chain design (not locked) |
| `STAGE1-PREP-LOCK-PACKET-TWOHOP-L1.md` | Stage 1 Preparation Lock Packet Rev 2 — all 10 required items + scorer/cell records; filed 2026-06-08 |
| `RESULTS-TWOHOP-L1-cell01-1780911140.json` | VOIDED RUN — environment/runner incompatibility (mlx_lm 0.8.0 + no chat template); 96/96 format_scaffold_failure |
| `RUNNER-AMENDMENT-LOCK-NOTE-TWOHOP-L1.md` | Runner amendment lock note — voided run disposition, Option R1 amendment, dry-run confirmation |
| `RESULTS-TWOHOP-L1-cell01-1780912218.json` | Stage 1 FP16 run — valid result; sha256:6de8b67c...; hop1 14/24, hop2 24/24, composite 18/24, negative_graph 2/24; Gate 1 PASS, Gate 2 FAIL, Branch 3 |
| `RESULTS-TWOHOP-L1-cell01-ALL.md` | Run_Summary — all 15 sections + §16 tokenizer reconciliation; Branch 3; NOT ELIGIBLE for stress |
| `TOKENIZER-HASH-RECONCILIATION-TWOHOP-L1.md` | Tokenizer hash reconciliation — sha256:3fd169731d... (audit) vs sha256:c0382117... (run); RECONCILED; Gate 0.5 confirmed PASS under run tokenizer |
| `CLAIM-B-MAP-ENTRY-TWOHOP-L1-CELL01.md` | Claim B map entry — Cell01 multi-axis constructibility-boundary point; per-axis classification (A/B/C); failure-overlap analysis; safe/forbidden interpretations; recommended next axis |
| `CELL02-AXIS-DECISION-MEMO.md` | Cell02 axis decision — position/ordering recommended; one-axis constraint; design requirements; pre-authorization requirements; Cell02 NOT yet authorized |
| `CELL02-CONSTRUCTION-PROPOSAL-TWOHOP-L1.md` | Cell02 construction proposal — all C_target-last design; frozen variables; diagnostic predictions; gate expectations; Manager decision required |
| `generate_cell02.py` | Cell02 generation script — RNG seed 20260610; all-C_target-last; fixed gen_pool circuit breaker; Gate 5 forced arrangement |
| `items_twohop_l1_cell02.json` | Cell02 manifest — 24 items, all-C_target-last; sha256:b81d4716...; Gate 0/0.5/5 PASS |
| `runner_twohop_l1_cell02.py` | Cell02 runner — sha256:d14f6424...; amended from Cell01 runner (ITEMS_PATH + AXIS_CONFIG only); dry-run PASS |
| `CELL02-PREP-LOCK-PACKET-TWOHOP-L1.md` | Cell02 Preparation Lock Packet — all 16 required items; filed 2026-06-08 |
| `RESULTS-TWOHOP-L1-cell02-1780933041.json` | Cell02 FP16 run — sha256:47b5eaa9...; hop1 9/24, hop2 23/24 (1 FSF), composite 20/24, neg_graph 0/24; Gate 2 FAIL, Branch 3 |
| `RESULTS-TWOHOP-L1-cell02-ALL.md` | Cell02 Run_Summary — Gate ladder, provenance match table, hypothesis result (ordering NOT supported), branch routing; filed 2026-06-08 |
| `CLAIM-B-MAP-ENTRY-TWOHOP-L1-CELL02.md` | Cell02 Claim B map entry — second dirty-cell boundary point; per-axis classification; position/ordering NOT SUPPORTED; adjacency-driven endpoint attraction candidate; filed 2026-06-08 |
| `CELL02-HOP2-FSF-INSPECTION-TWOHOP-L1.md` | hop2 FSF construction-integrity inspection — i08 classified FORMAT_COMPLIANCE_LOSS (isolated, orthogonal format-only event); Gate 0.5 confirmed valid; filing hold resolved |
| `CELL02-GATE5-POSITIONAL-DUMMY-AUDIT.md` | Gate 5 positional-dummy audit — PASS confirmed for current dummies (0/24); coverage gap: always_return_second_C = 24/24 composite not tested; Gate 5 filed as PASS* with caveat |
| `CELL03-AXIS-DECISION-MEMO.md` | Cell03 axis decision (revised 2026-06-08) — attraction-cue mapping framing; four confounded Cell02 cues; full-rank C dummy policy; always_return_answer_shaped proposed; position/C-rank balance required; Cell03 NOT authorized pending scorer amendment + Manager authorization |
| `CELL03-DUMMY-POLICY-CONFIRMATION.md` | Dummy-policy confirmation packet (2026-06-08) — PARTIALLY SUPERSEDED by R1; §1 full-rank C coverage and §4–§5 re-lock plan remain in force; §2/§3/final list superseded |
| `CELL03-DUMMY-POLICY-CLARIFICATION-R1.md` | Dummy-policy clarification R1 (2026-06-08) — PARTIALLY SUPERSEDED by R2; §2 Gate 5 second_C==ct handling and §3 query-type table logic remain in force; §1/§4/§5/§6 superseded |
| `CELL03-DUMMY-POLICY-RESPONSE-R2.md` | Dummy-policy response R2 (2026-06-08, amended) — SUPERSEDED on §2–§4 by R3; §1 always_return_ct reference-only reasoning and §3 naming remain in force |
| `CELL03-DUMMY-POLICY-RESPONSE-R3.md` | Dummy-policy response R3 / brainstorm (2026-06-08) — always_return_query_role_object retired (incoherent as ceiling dummy; scores n/n on positive queries by construction); revised architecture: rank dummies ceiling-bearing; always_return_ct + always_return_NULL reference-only; ct-anchoring diagnosed via §8 only; scorer amendment scope revised; awaiting Team Lead / Senior disposition |
| `CELL03-SCORER-AMENDMENT-PLAN.md` | Scorer amendment planning packet (2026-06-08) — scope correction: always_return_NULL already in scorer (not new); adds second_C + third_C (ceiling-bearing) + always_return_ct (reference-only); 6 new unit tests + regression; _TEST_ITEM_DUMMIES fixture specified; GATE5_REFERENCE_ONLY constant for runner layer; §8 no scorer change needed; Cell01/Cell02 not rescored; hash placeholder sha256:[CELL03-SCORER-HASH-TBD]; blocked pending Senior confirmation → Manager authorization |
| `CELL03-SCORER-AMENDMENT-PRE-LOCK-CONFIRMATIONS.md` | Scorer amendment pre-lock confirmations (2026-06-08) — R=3 confirmed (∈{3,4}); disambiguation rule: earliest position_index; T_new_1–T_new_6 enumerated with two balanced fixtures (ct at rank 2 / rank 1); tautology guard, full-rank, ct/NULL exclusion, second_C/third_C functionality all covered; Cell01/Cell02 model outputs frozen; offline manifest-only baseline computation authorized; all 3 conditions met; eligible for Manager routing |
| `CELL03-SCORER-RELOCK-PACKET.md` | Scorer re-lock packet (2026-06-08) — Manager-authorized amendment executed; prior sha256:060afad9... → amended sha256:b65c6803...; 20/20 tests (14 regression + 6 new); Cell02 offline second_C = 24/24 confirms Gate 5 PASS* gap; Cell01/Cell02 frozen; dummy manifest: ceiling-bearing (first_C, second_C, third_C, last_C), reference-only (always_return_ct, always_return_NULL), retired (always_return_query_role_object); Team Lead disposition: ACCEPTED (pending Senior clerical review) |
| `CELL03-GATE3-ENDPOINT-INTRUSION-RECOMMENDATION.md` | Gate 3 endpoint-intrusion threshold recommendation (2026-06-08) — recommends Option B: defer Gate 3 amendment, proceed under existing composite-only Gate 3 thresholds with mandatory non-blocking §8 diagnostics; rationale: Gate 3 is composite-quality gate; §8 is architectural home for ct-anchoring; no defensible pre-Cell03 threshold value; making experimental outcome variable a gate condition is methodologically inverted; Option A deferred pending empirical basis; Team Lead accepted Option B with governance guardrail (Gate 3 endpoint-intrusion threshold required before any future stress-eligibility declaration) |
| `CELL03-TAUTOLOGY-GUARD-VERIFICATION.md` | Tautology guard fixture verification (2026-06-08) — filed for Senior review; fixture excerpts and T_new_2 assertion; ct tested at rank 1 (Fixture_B) and rank 2 (Fixture_A); T_new_2 proves always_return_second_C scores 0.0 when ct is at rank 1 (guard is non-vacuous; not hardcoded to return ct); rank-sensitivity confirmed by T_new_1 + T_new_2 pair |
| `generate_cell03.py` | Cell03 generation script — RNG seed 20260615; 3-group design (Group A: ct=first_C pos 3; Group B: ct=second_C pos 5; Group C: ct=third_C/last_C pos 7); neighbor interposed between hop1 and hop2 in all 24 items (gap=2, adjacency broken); uses scorer sha256:b65c6803...; 24/24 PASS; manifest_hash sha256:7d5099cb...; Gate 5 precheck PASS (max_det=8/24) |
| `items_twohop_l1_cell03.json` | Cell03 manifest — 24 items, 3-group balanced design; sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1; 24/24 PASS; adjacency broken all items; ct C-rank balanced 8 first_C / 8 second_C / 8 third_C-last_C; ct position balanced pos 3/5/7; no model inference |
| `CELL03-CONSTRUCTION-PACKET.md` | Cell03 construction packet (2026-06-08) — 11-item packet: manifest hash sha256:7d5099cb..., scorer hash sha256:b65c6803..., 24/24 validation PASS, token audit PASS (0 violations), dummy baseline table, Gate 5 precheck PASS (max_det=8/24 ≤ 9/24), §8 diagnostic readiness CONFIRMED, cue-balance table (all 24 items adjacency broken gap=2), standing caveat, no-inference confirmation; filed awaiting Team Lead Stage 0 lock review |
| `CELL03-STAGE0-LOCK-REVIEW.md` | Cell03 Stage 0 lock review (2026-06-08, Senior Engineer) — 12/12 checklist PASS; all Cell02 confounds resolved; §8 readiness 10/10 fields confirmed; standing caveat and no-inference confirmed; 3 non-blocking minor observations (ct_c_rank JSON label format, C-token rotation design note, hop2_abs_position naming); routing recommendation: YES — route for Manager FP16 authorization; disposition to Team Lead |
| `runner_twohop_l1_cell03.py` | Cell03 runner — sha256:f23d99df... (amended from Cell02 runner: items path, scorer hash sha256:b65c6803..., axis config, §8 diagnostics added, mlx_lm API update make_sampler+GenerationResponse); dry-run PASS |
| `RESULTS-TWOHOP-L1-cell03-1780948339.json` | Cell03 FP16 run — sha256:f29783622fb14caca1c2a5829da8b874836add5d111356ea42be1f7d4a7b73f7; hop1 6/24, hop2 23/24, composite 15/24, neg_graph 6/24; Gate 1 PASS (first clean Gate 1 — 0 FSF); Gate 2 FAIL; Branch 3 |
| `RESULTS-TWOHOP-L1-cell03-ALL.md` | Cell03 Run_Summary — Standard Return Packet 14-section format; Gate 1 PASS (0 FSF); Gate 2 FAIL (hop1 6/24, composite 15/24); Gate 3 FAIL diagnostic (wrong_chain 7/24); Gate 5 PASS (max_det 8/24); Branch 3; §8 ct-anchoring 6/24 uniform 2/8 per group; neg_graph intrusion 18/24; standing caveat present; NOT ELIGIBLE for stress; filed 2026-06-08 |
| `CLAIM-B-MAP-SYNTHESIS-CELLS01-03.md` | Cells01–03 Claim-B map synthesis (2026-06-08; revised pass 4 — §7b symmetric non-identifiability added) — 14-section document + Appendix A/B; §7b: pure shortcut predicts 0/0/8 step; observed 1/6/8 monotone; Group B 6/8 correct with cd2 last rules out pure shortcut; non-identifiability symmetric (gradient rules out clean tracing; Group B rules out pure shortcut); three-way confound (chain-tracing, partial shortcut, target-recency); warranted closing ("nor that it was not"); evidence record aligned with Paper 2 §4.3 and Fig 3; gate/score/recurrence tables; §5 cue-status table; taxonomy saturation 288/288 classified; provisional Claim B Track A candidate YES; standing caveat present; no-inference statement |
| `CELL03-DECOMPOSITION-REVIEW.md` | Cell03 decomposition packet CS-proposed technical review / draft routing note (2026-06-08; attribution-corrected 2026-06-08 per Team Lead memo — originally filed as "Senior technical review" by CS, not Senior-authored; Senior actual disposition forthcoming) — 4/4 sections confirmed against §8 diagnostic tables and raw JSON; interpretive scope CLEAN (structural attribution, no mechanism overclaim); 96/96 taxonomy count verified; 3 non-blocking observations; standing caveat noted as absent from decomposition body (acceptable for decomposition type; required in subsequent synthesis/claim docs); 6/6 synthesis questions addressable from decomposition evidence; draft routing note: READY for synthesis preparation |
| `CELL03-DECOMPOSITION-PACKET.md` | Cell03 FP16 decomposition packet (2026-06-08) — 4-section failure decomposition per Team Lead memo; Section A: hop1 Group A complete failure (0/8 correct), 6 NULL from neighbor-interposed layout, 3 Group C filler-return artifacts (neighbor-proximity), ct-anchoring uniform 2/8 per group, 0 cn returns; Section B: composite wrong_chain all 7 returns = cd2 at pos7 (last-position bias), gradient Group C 8/8 → Group B 6/8 → Group A 1/8 exactly matches ct distance from last position, 4→7 increase explained by balanced design; Section C: neg_graph intrusion NOT ct-specific (ct absent from context), 0/18 ct returns, 10/18 last-visible decoy C-endpoint, 6/18 target B-endpoint (Group C hop1-to-bt follows), pure endpoint-emission behavior; Section D: all 96 outputs classified by existing taxonomy, no new class needed, UNCLASSIFIED_OFF_FRAME (4) neighbor-proximity attributable, taxonomy stable for Claim B; filed for Team Lead synthesis preparation |
| `governance/2026-06-09_post-paper2-alignment/INDEX.md` | Governance filing index — post-paper-2 alignment directory; 6 files filed 2026-06-09 per Team Update directive |
| `governance/2026-06-09_post-paper2-alignment/TEAM-UPDATE-POST-PAPER2-ALIGNMENT.md` | Team Update governance record (2026-06-09) — retraction disposition (VERIFIED WITH PROVENANCE CAVEAT); two Paper 2 corrections required before external routing; CS deliverable status table; B1 authorization prerequisites |
| `governance/2026-06-09_post-paper2-alignment/PAPER2-RECOMPUTATION-REPORT.md` | Paper 2 recomputation report (2026-06-09) — all key numbers verified from locked JSONs; Cell01: 14/24/18/2; Cell02: 9/23/20/0; Cell03: 6/23/15/6; Gate 2 FAIL all cells; Gate 5 PASS all cells; two discrepancies: Cell02 "all-ct-last" factual error + §4.5 "(3,11,6)" ambiguity |
| `governance/2026-06-09_post-paper2-alignment/FREEZE-TAG-REPORT.md` | Freeze/tag report (2026-06-09) — Paper 1 tag synthesis-cells01-03-pass4 confirmed (commit 49aa222); Paper 2 freeze tag paper2-cells01-03-v1.0 recommended pending corrections + Manager authorization |
| `governance/2026-06-09_post-paper2-alignment/FORK-A-CLARIFICATION-RETRACTION-NOTE.md` | Fork A clarification and retraction note (2026-06-09) — figures 8/8, 24/24, 23/24, 24/24 all artifact-backed; same-error identity confirmed logged; provenance gap: empty provenance block, missing scorer/manifest/runner/mlx_lm_version hashes — below B1 standard |
| `governance/2026-06-09_post-paper2-alignment/B1-IMPLEMENTATION-PLAN.md` | B1 harness backfill implementation plan (2026-06-09) — gap analysis vs Cell03 runner; new fields: model_snapshot_hash, mlx_lm_version, python_version, precision_rung, gate_summary, stress_eligible; runtime fail-closed Gate 2 block; same-error identity per-item; 10 unit tests (B1-T1–T10); execution order; prerequisites |
| `governance/2026-06-09_post-paper2-alignment/PAPER2-REPRODUCTION-ACCEPTANCE-TEST-PLAN.md` | Paper 2 reproduction acceptance test plan (2026-06-09) — 8 acceptance tests (AT-1–AT-8); pre-run checklist; all 12 per-cell accuracy counts; Cell03 taxonomy 96/96; group gradient 1/6/8; gate summaries; provenance completeness; hash locks; same-error identity; dummy baselines; protocol and disposition |
