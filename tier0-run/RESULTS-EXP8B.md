# RESULTS-EXP8B.md

**Date:** 2026-06-07  
**Experiment:** Exp8B  
**Arm:** 2B — Single-variable query wording test on Exp8A items  
**Phase:** FP16 feasibility screen (n=8)  
**Status:** NOT FEASIBLE — Condition 1 not met

---

## 1. Outcome

```
Arm 2B FP16 pass count:      6 / 8
Feasibility threshold:        ≥ 7 / 8
Condition 1 (content pass):   NOT MET
Numeric OOC count:            0
Condition 2 (zero numeric):   MET
Result:                       NOT FEASIBLE
n≥20 expansion:               not authorized
INT8 / INT4:                  not authorized
Exp8C:                        not authorized without explicit Manager / Team Lead decision
```

Exp8B is the final unconditional Arm 2 construction attempt. No further repair loop is authorized without explicit Manager / Team Lead decision after results.

---

## 2. Provenance

```
Model:                     Qwen/Qwen2.5-1.5B-Instruct  (FP16)
Decoding:                  temperature=0.0, max_tokens=16
fresh_generation:          True
Output file:               fp16_screen_exp8b_1780789038.json
Runner script:             fp16_screen_exp8b.py
Tasks file:                tasks_exp8b.py

Manifest hash (approved pre-run):
  sha256:695b1ac90aa0745765f9785435f527757a248f4ad27a85ce8f249230610ec56e

Scoring functions:         imported unchanged from tasks_exp8.py
  score_arm2_content, score_arm2_scaffold, score_arm2_format
```

**Single variable changed from Exp8A:**
```
Exp8A query: "Which value is associated with SUBJ_T?"
Exp8B query: "Which token is assigned to SUBJ_T?"
```

All item geometry (subjects, objects, fact order, target positions, relation "maps to",
context line structure, scaffold, decoding) is identical to Exp8A.
Confirmed by 32-check validator (256 checks across 8 items — all passed).

---

## 3. Scoring axes (three-axis, unchanged from Exp8A amendment)

**scaffold_class**
```
SCAFFOLD_PRESENT  output contains ANSWER: followed by at least one non-whitespace token
SCAFFOLD_ABSENT   no usable ANSWER: prefix with following token found
```

**format_class** (strict — unchanged)
```
FORMAT_PASS       stripped output exactly matches ^ANSWER:\s+[A-Z]{4,8}$
FORMAT_FAIL       anything else
```

**content_class** (9 classes, priority order)
```
RETURNED_TARGET_OBJ       correct answer (priority 1)
RETURNED_OBJ_POS_k        non-target object at fact k, k∈{1,2,3,4,5}\{target_pos}
RETURNED_SUBJ_TOKEN       any subject token from context
RETURNED_NON_CONTEXT_TOKEN token not in any context slot
UNCLASSIFIED              no extractable token found (scaffold absent)
```

---

## 4. Per-item results

| Item | target_pos | target | scaffold | format | content | returned_token | PASS |
|---|---|---|---|---|---|---|---|
| L2_01 | 2 | ARVUX→ICVLX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | ICVLX | ✓ |
| L2_02 | 2 | CIRNX→OBLVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | OBLVX | ✓ |
| L2_03 | 2 | HIBNX→OICVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_OBJ_POS_1 | OHIBX | ✗ |
| L2_04 | 3 | UFBNX→PCIVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_OBJ_POS_2 | PBCVX | ✗ |
| L2_05 | 3 | EBVNX→SCIVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | SCIVX | ✓ |
| L2_06 | 3 | HGIVX→IDBVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | IDBVX | ✓ |
| L2_07 | 4 | UNVBX→OECVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | OECVX | ✓ |
| L2_08 | 4 | ACNLX→PJBVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | PJBVX | ✓ |

Pass by target_pos:
- pos=2: 2/3 (L2_01 ✓, L2_02 ✓, L2_03 ✗)
- pos=3: 2/3 (L2_05 ✓, L2_06 ✓, L2_04 ✗)
- pos=4: 2/2

scaffold_class: SCAFFOLD_PRESENT on all 8 items.
format_class:   FORMAT_PASS on all 8 items.
All failures are pure content errors.

---

## 5. Raw outputs (failed items)

```
L2_03  raw_output: "ANSWER: OHIBX"
       target=OICVX (pos=2), returned=OHIBX (pos=1)
       same_error_identity: RETURNED_OBJ_POS_1|OHIBX|1

L2_04  raw_output: "ANSWER: PBCVX"
       target=PCIVX (pos=3), returned=PBCVX (pos=2)
       same_error_identity: RETURNED_OBJ_POS_2|PBCVX|2
```

Both failures return the object at position (target_pos − 1): off-by-one toward the beginning of context.

---

## 6. Comparison with Exp8A

| Item | Exp8A raw | Exp8B raw | Exp8A pass | Exp8B pass | output_exact_match |
|---|---|---|---|---|---|
| L2_01 | `ANSWER: ICVLX` | `ANSWER: ICVLX` | ✓ | ✓ | **True** |
| L2_02 | `ANSWER: 0` | `ANSWER: OBLVX` | ✗ | ✓ | False — **fixed** |
| L2_03 | `ANSWER: 10` | `ANSWER: OHIBX` | ✗ | ✗ | False — failure mode changed |
| L2_04 | `ANSWER: PCIVX` | `ANSWER: PBCVX` | ✓ | ✗ | False — **new failure** |
| L2_05 | `ANSWER: SCIVX` | `ANSWER: SCIVX` | ✓ | ✓ | **True** |
| L2_06 | `ANSWER: IDBVX` | `ANSWER: IDBVX` | ✓ | ✓ | **True** |
| L2_07 | `ANSWER: OECVX` | `ANSWER: OECVX` | ✓ | ✓ | **True** |
| L2_08 | `ANSWER: PJBVX` | `ANSWER: PJBVX` | ✓ | ✓ | **True** |

**Bit-stability of 6 Exp8A passers:** 5/6 exact match. L2_04 changed output and became incorrect.

**Reading:** 5 of the 6 Exp8A-passing items are bit-identical across the wording change. The intervention was mostly non-perturbing. The failure redistribution is:
- L2_02: rescued (numeric OOC → correct pass)
- L2_03: failure mode changed (numeric OOC → off-by-one positional anchor)
- L2_04: newly destabilized (correct → off-by-one positional anchor)

Net change: 0 (6/8 in both experiments).

---

## 7. Construction observation (for design record only)

```
Both failures: off-by-one positional anchoring (returned object at target_pos − 1)
  L2_03: target_pos=2, returned pos=1 object (OHIBX instead of OICVX)
  L2_04: target_pos=3, returned pos=2 object (PBCVX instead of PCIVX)

L2_03 homogeneous subject-prefix pool: all H-prefix subjects
L2_04 homogeneous subject-prefix pool: all U-prefix subjects

L2_03 Exp8A failure:    numeric OOC ("10")
L2_03 Exp8B failure:    positional anchor (OHIBX at pos=1)

Query wording "Which token is assigned to" may shift the model's
positional indexing relative to "Which value is associated with" —
but not resolvable at n=8. Observational only.
```

Exp8B does not adjudicate any seam claim. The feasibility gate failed before n≥20 expansion. This is a task-construction finding.

**Branch F story (failure-surface migration):**
```
Exp8A:  numeric non-context returns  (RETURNED_NON_CONTEXT_TOKEN, tokens "0" and "10")
Exp8B:  wrong in-context object returns  (RETURNED_OBJ_POS_1, RETURNED_OBJ_POS_2)
```
The wording change reduced numeric-output behavior but did not stabilize retrieval. The failure surface migrated from non-context degenerate outputs to in-context positional anchoring.

**Confirmed failure set across Exp8A and Exp8B (manuscript case material):**

| Item | Exp | content_class | raw token | context status | Diagnostic flag |
|---|---|---|---|---|---|
| L2_02 | 8A | RETURNED_NON_CONTEXT_TOKEN | `0` | Not in context | Degenerate numeric return |
| L2_03 | 8A | RETURNED_NON_CONTEXT_TOKEN | `10` | Not in context | Degenerate numeric return |
| L2_03 | 8B | RETURNED_OBJ_POS_1 | `OHIBX` | In-context (pos=1) | Wrong in-context position return |
| L2_04 | 8B | RETURNED_OBJ_POS_2 | `PBCVX` | In-context (pos=2) | Wrong in-context neighbor / orthographic similarity to target |

**Manuscript rule:** `OTHER_NON_CONTEXT_SYNTHETIC` is not an observed category in the Exp8A/Exp8B dataset. Do not cite it as case material. If it appears at all in the paper, label it as a possible future diagnostic annotation only. Preferred: omit from the main case table.

Diagnostic flags are post-hoc paper annotations. Scorer classes (9, locked) are separate.

---

## 8. Files

```
tasks_exp8b.py                         — Exp8B task items, 32-check validator
                                         (6 new Exp8B-specific checks B01–B06)
fp16_screen_exp8b.py                   — FP16 runner script
fp16_screen_exp8b_1780789038.json      — raw output JSON, full provenance
RESULTS-EXP8B.md                       — this file
```

Related Exp8A files:
```
tasks_exp8.py                          — Exp8A task items (source of exact item reuse)
fp16_screen_exp8_arm2_1780781863.json  — Exp8A raw outputs (for comparison)
RESULTS-EXP8-ARM2-FEASIBILITY.md      — Exp8A results
```
