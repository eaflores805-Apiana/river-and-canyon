# RESULTS-FORK-A-3B.md

**Date:** 2026-06-07
**Track:** Synthetic Key-Value Selection Constructibility
**Run type:** Two-rung frozen-construction constructibility check
**Rung:** 3B — Qwen/Qwen2.5-3B-Instruct (FP16)
**Phase:** FP16 feasibility screen (n=8)
**Status:** FEASIBLE — 8/8

---

## 1. Outcome

```
Rung:                    3B (Qwen/Qwen2.5-3B-Instruct, FP16)
Pass count:              8 / 8
Feasibility gate:        ≥ 7 / 8
Result:                  FEASIBLE

Ladder rule applied:
  3B PASSES → stop ladder
  Request Manager authorization for n≥20 before proceeding

7B rung:                 not started (ladder stopped at first pass)
n≥20:                    not authorized
INT8 / INT4:             not authorized
Seam claim:              not authorized
```

---

## 2. Provenance

```
Model:              Qwen/Qwen2.5-3B-Instruct  (FP16)
Decoding:           temperature=0.0, max_tokens=16, sampler=make_sampler(temp=0.0)
fresh_generation:   True
Output file:        fp16_constructibility_3b_1780865740.json
Runner script:      fp16_constructibility_check.py

Manifest hash (approved and verified pre-run):
  sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc

Scorer hash:        sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc
Validator hash:     sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc
Tokenizer hash:     sha256:29caa515cc153c78bf846329ad2a4e94df271c49c309024635cc015834acacce
Runner hash:        sha256:321a49a570652a516be1c5fa4d56817ac1db5b64b619cc6d667154478032d719

Note: scorer_hash and validator_hash are identical to manifest_hash.
scorer and validator are defined in tasks_exp8.py (same file as items).

Validator gate:     208/208 checks passed (tasks_exp8.py validate_tasks)
Preflight:          preflight_ok = True (all gates cleared)
```

---

## 3. Scoring axes (three-axis, unchanged from Exp8 amendment)

**scaffold_class:** SCAFFOLD_PRESENT / SCAFFOLD_ABSENT
**format_class:** FORMAT_PASS (`^ANSWER:\s+[A-Z]{4,8}$`) / FORMAT_FAIL
**content_class:** 9 classes, priority order (locked)

---

## 4. Per-item results

| Item | target_pos | target | scaffold | format | content | returned_token | PASS |
|---|---|---|---|---|---|---|---|
| L2_01 | 2 | ARVUX→ICVLX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | ICVLX | ✓ |
| L2_02 | 2 | CIRNX→OBLVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | OBLVX | ✓ |
| L2_03 | 2 | HIBNX→OICVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | OICVX | ✓ |
| L2_04 | 3 | UFBNX→PCIVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | PCIVX | ✓ |
| L2_05 | 3 | EBVNX→SCIVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | SCIVX | ✓ |
| L2_06 | 3 | HGIVX→IDBVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | IDBVX | ✓ |
| L2_07 | 4 | UNVBX→OECVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | OECVX | ✓ |
| L2_08 | 4 | ACNLX→PJBVX | SCAFFOLD_PRESENT | FORMAT_PASS | RETURNED_TARGET_OBJ | PJBVX | ✓ |

Pass by target_pos:
- pos=2: 3/3 (L2_01 ✓, L2_02 ✓, L2_03 ✓)
- pos=3: 3/3 (L2_04 ✓, L2_05 ✓, L2_06 ✓)
- pos=4: 2/2 (L2_07 ✓, L2_08 ✓)

scaffold_class: SCAFFOLD_PRESENT on all 8 items.
format_class:   FORMAT_PASS on all 8 items.
content_class:  RETURNED_TARGET_OBJ on all 8 items.
No failures.

---

## 5. Decision-token top-k (diagnostic / provenance only)

All 8 items: decision token at response position 3. Top-1 logprob = 0.000 on all items.

```
Note: decision-token top-k logs are provenance and diagnostic artifacts only.
They are NOT used to make capability or mechanism claims.
```

| Item | decision_pos | generated | top-3 |
|---|---|---|---|
| L2_01 | 3 | ' IC' | ' IC'(0.000), ' IF'(-4.875), ' IB'(-6.000) |
| L2_02 | 3 | ' O' | ' O'(0.000), ' OB'(-12.625), ' OC'(-16.125) |
| L2_03 | 3 | ' O' | ' O'(0.000), ' OH'(-10.000), ' OE'(-15.000) |
| L2_04 | 3 | ' PC' | ' PC'(0.000), ' P'(-12.875), ' PF'(-13.375) |
| L2_05 | 3 | ' SC' | ' SC'(0.000), ' SF'(-5.250), ' CF'(-11.000) |
| L2_06 | 3 | ' ID' | ' ID'(0.000), ' I'(-6.125), ' IE'(-6.125) |
| L2_07 | 3 | ' O' | ' O'(0.000), ' OE'(-7.250), ' OF'(-7.875) |
| L2_08 | 3 | ' P' | ' P'(0.000), ' PA'(-14.000), ' ANSW'(-14.000) |

---

## 6. Diagnostic annotations

```
Homogeneous subject-prefix items: L2_01 (A), L2_02 (C), L2_03 (H), L2_04 (U)
  All four homogeneous-prefix items pass at 3B.
  Contrast: Exp8A/Exp8B at 1.5B — both failures were homogeneous-prefix items
  (L2_03 all-H, L2_04 all-U).
  This is a diagnostic observation. No capability claim is licensed.

Numeric OOC count: 0
```

---

## 7. Ladder rule outcome

```
3B: FEASIBLE (8/8)
Ladder stopped at first pass per authorized ladder rule.
7B rung: not started.

Next step: Manager authorization required for n≥20 at 3B.
```

---

## 8. Reading (Control 2 — outcome→reading map)

Per the pre-registered outcome→reading map:

```
Passing rung: 3B clears the feasibility gate.
Construction is provisionally adequate at the first passing size (3B).

Lower-rung failure content (1.5B — Exp8A/Exp8B):
  Exp8A: RETURNED_NON_CONTEXT_TOKEN (numeric) — 2 failures
  Exp8B: RETURNED_OBJ_POS_1, RETURNED_OBJ_POS_2 — 2 failures (positional anchoring)
  All failures at 1.5B: SCAFFOLD_PRESENT, FORMAT_PASS (output-contract intact)

Provisional reading: consistent with capacity-bound at 1.5B.
  Lower-rung failures were content failures with intact output contract.
  3B clears under identical construction.

This reading is provisional. Lower-rung failure content informs but does
not determine the ladder-level reading at two rungs only.
No threshold claim is licensed from a two-rung result.
```

**Not licensed from this result:**
```
No seam hypothesis reading
No quantization claim
No general retrieval/capacity claim
No generalization beyond this frozen construction
No monotone threshold claim across untested sizes
```

---

## 9. Files

```
fp16_constructibility_check.py        — runner (3B and 7B)
fp16_constructibility_3b_1780865740.json  — raw output JSON, full provenance
RESULTS-FORK-A-3B.md                  — this file
tasks_exp8.py                         — frozen construction (manifest hash gates all runs)
```
