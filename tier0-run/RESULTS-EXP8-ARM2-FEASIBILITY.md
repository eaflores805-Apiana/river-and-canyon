# RESULTS-EXP8-ARM2-FEASIBILITY.md

**Date:** 2026-06-06  
**Experiment:** Exp8  
**Arm:** 2 — Load-matched single-lookup baseline  
**Phase:** FP16 feasibility screen (n=8)  
**Status:** NOT FEASIBLE — threshold not met

---

## 1. Outcome

```
Arm 2 FP16 pass count:     6 / 8
Feasibility threshold:     ≥ 7 / 8
Result:                    NOT FEASIBLE
n≥20 expansion:            not authorized
INT8 / INT4:               not authorized
```

Exp8 Arm 2 does not advance. The stability gate failed before any stress
sweep. This result is a construction finding only.

---

## 2. Provenance

```
Model:                     Qwen/Qwen2.5-1.5B-Instruct  (FP16)
Decoding:                  temperature=0.0, max_tokens=16
fresh_generation:          True
Output file:               fp16_screen_exp8_arm2_1780781863.json

Original task/manifest hash (items and prompts — approved pre-run):
  sha256:14129d0bfe2cae1c3e4d817a8423eaf5513665741c04f1d388ac8da34a9074de

Amended scorer/code hash (scorer functions only — post-run amendment):
  sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc

Hash change reflects: addition of score_arm2_scaffold, revision of
  score_arm2_format docstring (strict rule unchanged), extension of
  _extract_answer_token to capture non-alphabetic tokens, rename of
  OUT_OF_CONTEXT_TOKEN → RETURNED_NON_CONTEXT_TOKEN in _CONTENT_CLASSES.
  Task items, fact tuples, and prompts are identical under both hashes.
  Raw model outputs are from the original run; no rerun was performed.
```

---

## 3. Scoring axes (amended, 2026-06-06)

Three independent axes:

**scaffold_class**
```
SCAFFOLD_PRESENT  output contains ANSWER: followed by at least one
                  non-whitespace token
SCAFFOLD_ABSENT   no usable ANSWER: prefix with following token found
```

**format_class** (strict — unchanged from original design)
```
FORMAT_PASS       stripped output exactly matches ^ANSWER:\s+[A-Z]{4,8}$
FORMAT_FAIL       anything else
```

**content_class** (9 classes, priority order)
```
RETURNED_TARGET_OBJ       correct answer (priority 1)
RETURNED_OBJ_POS_k        non-target object at fact k, k∈{1,2,3,4,5}\{target_pos}
RETURNED_SUBJ_TOKEN       any subject token from context
RETURNED_NON_CONTEXT_TOKEN token not in any context slot (alphabetic or numeric)
UNCLASSIFIED              no extractable token found (scaffold absent)
```

**Amendment note:**  
Original scorer conflated scaffold absence with non-alphabetic ANSWER content:
"ANSWER: 0" was FORMAT_FAIL + UNCLASSIFIED. Revised scorer separates scaffold
compliance from content-token validity. FORMAT_PASS remains strict.
scaffold_class is the new diagnostic axis that captures whether the ANSWER:
prefix was present regardless of format shape.

---

## 4. Per-item results

| Item | target_pos | target | scaffold | format | content | returned_token | PASS |
|---|---|---|---|---|---|---|---|
| L2_01 | 2 | ARVUX→ICVLX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | ICVLX | ✓ |
| L2_02 | 2 | CIRNX→OBLVX | SCAFFOLD_PRESENT | FORMAT_FAIL | RETURNED_NON_CONTEXT_TOKEN | 0 | ✗ |
| L2_03 | 2 | HIBNX→OICVX | SCAFFOLD_PRESENT | FORMAT_FAIL | RETURNED_NON_CONTEXT_TOKEN | 10 | ✗ |
| L2_04 | 3 | UFBNX→PCIVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | PCIVX | ✓ |
| L2_05 | 3 | EBVNX→SCIVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | SCIVX | ✓ |
| L2_06 | 3 | HGIVX→IDBVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | IDBVX | ✓ |
| L2_07 | 4 | UNVBX→OECVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | OECVX | ✓ |
| L2_08 | 4 | ACNLX→PJBVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | PJBVX | ✓ |

Pass by target_pos:
- pos=2: 1/3 (L2_01 ✓, L2_02 ✗, L2_03 ✗)
- pos=3: 3/3
- pos=4: 2/2

scaffold_class: SCAFFOLD_PRESENT on all 8 items. The model used the ANSWER:
prefix every time. Both failures are content failures, not scaffold abandonments.

---

## 5. Raw outputs (failed items)

```
L2_02  raw_output: "ANSWER: 0"
L2_03  raw_output: "ANSWER: 10"
```

---

## 6. Construction observation (for design record only)

```
Both failures: target_pos=2
Both failures: homogeneous subject-prefix pool (L2_02: all C-prefix; L2_03: all H-prefix)
Both failures: all O-prefix objects in context
Both failures: numeric output returned ("0", "10")

L2_07 (PASS): O-prefix target object (OECVX), mixed subject prefixes

Numeric returns may indicate a wording/index artifact in specific
subject-pool configurations. Not resolvable from n=8. Observational
only. Feeds next-design discussion.
```

Exp8 Arm 2 does not adjudicate any seam claim. The feasibility gate
failed before n≥20 expansion. This result is a task-construction finding.

---

## 7. Files

```
tasks_exp8.py                              — task items, three-axis scorer
                                             (amended 2026-06-06)
fp16_screen_exp8_arm2.py                  — FP16 runner script
fp16_screen_exp8_arm2_1780781863.json     — raw output JSON, full provenance
RESULTS-EXP8-ARM2-FEASIBILITY.md         — this file
```
