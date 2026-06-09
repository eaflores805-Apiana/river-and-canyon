# RESULTS-FORK-A-INT8.md

**Date:** 2026-06-07
**Track:** Synthetic Key-Value Selection Constructibility
**Run type:** 3B INT8 stress run
**Rung:** 3B — Qwen/Qwen2.5-3B-Instruct (INT8, q_bits=8, q_group_size=64)
**Phase:** INT8 stress run on frozen n=24 L3 manifest
**Status:** PASS — 23/24

---

## 1. Outcome

```
Run:             3B INT8 stress run
Pass count:      23 / 24
Feasibility gate: ≥21 / 24 (87.5%)
Result:          PASS

Retention (vs FP16):    23/24  (95.8%)
Exact-output agreement: 23/24  (95.8%)
Strict-format gap:       1
Content gap (vs FP16):   1
Numeric OOC count:       0
```

---

## 2. Authorization chain

The INT8 n=24 stress run did not outrun the gate sequence. The full
authorization chain is:

```
1. 3B FP16 n=8 feasibility run:         8/8 PASS
2. Manager authorization for n≥20 / n=24 FP16 expansion
3. 3B FP16 n=24 baseline run:           24/24 PASS
4. Manager authorization for INT8 stress-readiness and stress run
5. INT8 Pass 1:                         conversion + hash locking only
                                        no items scored
6. Manager authorization for INT8 Pass 2 scored run
7. INT8 Pass 2 (this run):              23/24 PASS
```

---

## 3. Provenance

```
Model:              Qwen/Qwen2.5-3B-Instruct  (INT8)
Conversion:         q_bits=8, q_group_size=64, dtype=bfloat16
Bits per weight:    8.501
Converted dir:      tier0-run/Qwen2.5-3B-Instruct-mlx-int8/
Decoding:           temperature=0.0, max_tokens=16, sampler=make_sampler(temp=0.0)
fresh_generation:   True
Output file:        stress_constructibility_3b_int8_1780870164.json
Runner script:      stress_constructibility_3b.py
```

---

## 4. All hashes

```
manifest_hash:              sha256:28d249dc6a56fbad54be5606c4285eaa78f286f31acf22610357e40bf12a3481
scorer_hash:                sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc
validator_hash:             sha256:28d249dc6a56fbad54be5606c4285eaa78f286f31acf22610357e40bf12a3481
tokenizer_hash:             sha256:29caa515cc153c78bf846329ad2a4e94df271c49c309024635cc015834acacce
runner_hash:                sha256:3622a9efb88f6877d32d1408e9682dbd4af3531fd6390b6fe3ed4a85fc8bb0a9
quant_config_hash:          sha256:0a73a0b1727e55ef5637e32e9897ad3f10b6d525f4d76c506ab7e9b87042d5f8
quant_model_manifest_hash:  sha256:3f94f6430eb5b2bed59a2500b38a3b42b554a146cc6cb89eb3468dddb833a023
```

### Validator hash explanation (Outcome C)

```
validator_hash equals manifest_hash.

Reason: validate_tasks() is defined in tasks_fork_a_n24.py (line 186),
the same file as the n=24 item manifest. get_manifest_hash() in that file
hashes Path(__file__), i.e., tasks_fork_a_n24.py itself (line 489).
Therefore the validator's correctness is version-pinned by the manifest hash.

This is distinct from scorer_hash, which is the hash of tasks_exp8.py —
the separate file where the three-axis scorer functions are defined
(score_arm2_content, score_arm2_format, score_arm2_scaffold).

Two independent source files, two independent hashes:
  tasks_fork_a_n24.py  →  manifest_hash = validator_hash = sha256:28d249dc...
  tasks_exp8.py        →  scorer_hash               = sha256:4036b1ad...
```

---

## 5. Preflight — all STOP gates cleared

```
manifest_hash             ✓ match  sha256:28d249dc...
scorer_hash               ✓ match  sha256:4036b1ad...
validator                 ✓ pass   624/624 checks
tokenizer_hash            ✓ verified
quant_config_hash         ✓ match  (locked in runner constants)
quant_model_manifest_hash ✓ match  (locked in runner constants)
model load                ✓ success
```

---

## 6. Validator-count explanation

```
n=8  manifest (tasks_exp8.py):       208 checks /  8 items = 26 checks per item
n=24 manifest (tasks_fork_a_n24.py): 624 checks / 24 items = 26 checks per item
```

The validator check count increased from 208 to 624 because the manifest
expanded from n=8 to n=24 items. The per-item rule count is identical at
both sizes (26 checks per item). No validator rules were added after results
were visible. The n=24 validator encodes the same construction requirements
as the n=8 validator, applied to the larger item set.

---

## 7. Scoring axes (three-axis, locked)

```
scaffold_class:  SCAFFOLD_PRESENT / SCAFFOLD_ABSENT
format_class:    FORMAT_PASS (^ANSWER:\s+[A-Z]{4,8}$) / FORMAT_FAIL
content_class:   9 classes, priority order (locked in tasks_exp8.py)
```

---

## 8. Per-item results

| Item | pos | target | scaffold | format | content | returned_token | exact_match | PASS |
|---|---|---|---|---|---|---|---|---|
| L3_01 | 2 | TANVX→QANBX | PRESENT | PASS | RETURNED_TARGET_OBJ | QANBX | ✓ | ✓ |
| L3_02 | 2 | TBNVX→QBNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | QBNBX | ✓ | ✓ |
| L3_03 | 2 | TCNVX→QCNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | QCNBX | ✓ | ✓ |
| L3_04 | 2 | TDNVX→QDNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | QDNBX | ✓ | ✓ |
| L3_05 | 2 | TENVX→QENBX | PRESENT | PASS | RETURNED_TARGET_OBJ | QENBX | ✓ | ✓ |
| L3_06 | 2 | TFNVX→QFNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | QFNBX | ✓ | ✓ |
| L3_07 | 2 | TGNVX→QGNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | QGNBX | ✓ | ✓ |
| L3_08 | 2 | THNVX→QHNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | QHNBX | ✓ | ✓ |
| L3_09 | 3 | RINVX→XINBX | PRESENT | PASS | RETURNED_TARGET_OBJ | XINBX | ✓ | ✓ |
| L3_10 | 3 | RJNVX→XJNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | XJNBX | ✓ | ✓ |
| L3_11 | 3 | RKNVX→XKNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | XKNBX | ✓ | ✓ |
| L3_12 | 3 | RLNVX→XLNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | XLNBX | ✓ | ✓ |
| L3_13 | 3 | RMNVX→XMNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | XMNBX | ✓ | ✓ |
| L3_14 | 3 | RNNVX→XNNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | XNNBX | ✓ | ✓ |
| L3_15 | 3 | RONVX→XONBX | ABSENT  | FAIL | UNCLASSIFIED        | None  | ✗ | ✗ |
| L3_16 | 3 | RPNVX→XPNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | XPNBX | ✓ | ✓ |
| L3_17 | 4 | FQNVX→YQNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | YQNBX | ✓ | ✓ |
| L3_18 | 4 | FRNVX→YRNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | YRNBX | ✓ | ✓ |
| L3_19 | 4 | FSNVX→YSNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | YSNBX | ✓ | ✓ |
| L3_20 | 4 | FTNVX→YTNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | YTNBX | ✓ | ✓ |
| L3_21 | 4 | FUNVX→YUNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | YUNBX | ✓ | ✓ |
| L3_22 | 4 | FVNVX→YVNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | YVNBX | ✓ | ✓ |
| L3_23 | 4 | FWNVX→YWNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | YWNBX | ✓ | ✓ |
| L3_24 | 4 | FXNVX→YXNBX | PRESENT | PASS | RETURNED_TARGET_OBJ | YXNBX | ✓ | ✓ |

Pass by target_pos:
- pos=2: 8/8
- pos=3: 7/8  (L3_15 fails)
- pos=4: 8/8

scaffold_class: SCAFFOLD_PRESENT on 23/24. SCAFFOLD_ABSENT on L3_15.
format_class:   FORMAT_PASS on 23/24. FORMAT_FAIL on L3_15.
content_class:  RETURNED_TARGET_OBJ on 23/24. UNCLASSIFIED on L3_15.

---

## 9. L3_15 failure record

```
Item:              L3_15
target_pos:        3
target:            RONVX → XONBX

Official strict scorer result:
  scaffold_class:  SCAFFOLD_ABSENT
  format_class:    FORMAT_FAIL
  content_class:   UNCLASSIFIED
  returned_token:  None
  is_correct:      False
  L3_15 fails under the locked scorer.

Diagnostic raw-output observation:
  FP16 raw_output: 'ANSWER: XONBX'
  INT8 raw_output: 'XONBX'
  The correct target object XONBX is visibly emitted without the required
  ANSWER: scaffold. This is a format-contract / scaffold-dropout failure.

Not described as:
  content-selection failure
  target-object loss
  numeric OOC
  positional anchoring
```

---

## 10. Scorer-caveat addendum

```
Scorer behavior on L3_15 — strict scorer, not content rescue

The three-axis scorer's content extractor depends on the ANSWER: scaffold
to locate the answer span. When scaffold_class is SCAFFOLD_ABSENT, the
scorer does not automatically extract the bare correct token from the raw
output. It returns:

  content_class:   UNCLASSIFIED
  returned_token:  None

This is strict scorer behavior, not a content rescue or a scoring override.

Reporting split:

  Strict-format retention (gate-relevant):
    23/24 items passed under the locked scorer.
    L3_15 fails. This is the only number that applies to the pass gate.

  Target-object-visible diagnostic (non-gate):
    24/24 raw outputs contained the target object in the raw output string.
    L3_15: XONBX visibly emitted without scaffold.
    This is a human raw-output diagnostic observation only.
    It does not modify the gate or reclassify L3_15 as a pass.
```

---

## 11. Strict scoring breakdown

```
Content class breakdown (INT8):
  RETURNED_TARGET_OBJ:  23
  UNCLASSIFIED:          1

Content class breakdown (FP16 reference):
  RETURNED_TARGET_OBJ:  24
```

---

## 12. Failure-class transition table

| Item | FP16 class | INT8 class | same_error_identity_key |
|---|---|---|---|
| L3_15 | RETURNED_TARGET_OBJ | UNCLASSIFIED | UNCLASSIFIED\|None\|None |

Comparison to prior L2 failure identities (Exp8A/Exp8B) is diagnostic only
and does not affect the stress interpretation.

---

## 13. Decision-token top-k (diagnostic / provenance only)

All 23 passing items: decision token at response_pos=3. Top-1 logprob=0.000
on 22/23 passing items.

Exception:
```
L3_11: top-1 logprob=−0.125, top-2 ' Z' at −2.750 (correct, clear margin)
```

L3_15: no decision token annotated. The ANSWER: scaffold prefix was never
emitted so the annotator found no scaffold boundary and recorded no decision
token.

```
Note: decision-token top-k logs are provenance and diagnostic artifacts only.
They are NOT used to make capability or mechanism claims.
```

---

## 14. Position subgroup (diagnostic — does not modify gate)

```
pos=2: 8/8
pos=3: 7/8  (L3_15 fails — scaffold dropout)
pos=4: 8/8
```

Note: partial subgroup success does not license INT4 or seam testing.

---

## 15. Numeric OOC observation

```
No numeric out-of-context returns were observed in this 3B INT8 run.
Numeric OOC count: 0
```

This observation applies only to this run under the frozen construction.
It does not state or imply that numeric artifacts observed in prior runs
(Exp8A: items L2_03, L2_04 at 1.5B) are resolved in general.

---

## 16. Scope boundary

This INT8 result applies only to:

```
Task:            frozen n=24 five-fact uniform-relation Synthetic Key-Value
                 Selection Constructibility task
Prompt:          locked (tasks_fork_a_n24.py)
Tokenizer:       locked (tokenizer_hash above)
Scorer:          locked (tasks_exp8.py, scorer_hash above)
Validator:       locked (tasks_fork_a_n24.py, validator_hash above)
Decoding:        temperature=0.0, max_tokens=16, sampler=make_sampler(temp=0.0)
Output contract: ^ANSWER:\s+[A-Z]{4,8}$
Model:           Qwen/Qwen2.5-3B-Instruct
Quantization:    INT8 (q_bits=8, q_group_size=64)
```

This result does not generalize to:

```
multi-hop tasks
heterogeneous-relation tasks
natural-language tasks
other model sizes
other quantization methods
INT4
```

---

## 17. Not licensed from this result

```
No seam claim
No broad quantization claim beyond this INT8 result
No mechanism claim
No general retrieval / binding / reasoning claim
No generalization beyond this frozen construction
No INT4 authorization (requires separate Manager decision)
```

---

## 18. Files

```
stress_constructibility_3b.py                     — runner (INT8/INT4, INT4 auth-gated)
stress_constructibility_3b_int8_1780870164.json   — raw output JSON, full provenance
RESULTS-FORK-A-INT8.md                            — this file
tasks_fork_a_n24.py                               — frozen n=24 L3 manifest + validator
tasks_exp8.py                                     — frozen three-axis scorer
fp16_constructibility_3b_n24_1780867214.json      — FP16 baseline reference (immutable)
```
