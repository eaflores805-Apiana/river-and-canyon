# RESULTS-FORK-A-INT4.md

**Date:** 2026-06-07
**Track:** Synthetic Key-Value Selection Constructibility
**Run type:** 3B INT4 stress run
**Rung:** 3B — Qwen/Qwen2.5-3B-Instruct (INT4, q_bits=4, q_group_size=64)
**Phase:** INT4 stress run on frozen n=24 L3 manifest
**Status:** PASS — 24/24

---

## 1. Outcome

```
Run:              3B INT4 stress run
Pass count:       24 / 24  (100.0%)
Feasibility gate: ≥21 / 24  (87.5%)
Result:           PASS

Retention (vs FP16):      24/24  (100.0%)
Exact-output agreement:   24/24  (100.0%)
Strict-format gap:         0
Content gap (vs FP16):     0
Numeric OOC count:         0
Failures:                  none
```

---

## 2. Authorization chain

```
1. 3B FP16 n=8 feasibility run:          8/8 PASS
2. Manager authorization for n≥20 / n=24 FP16 expansion
3. 3B FP16 n=24 baseline run:            24/24 PASS
4. Manager authorization for INT8 stress-readiness and INT8 stress run
5. INT8 Pass 1:                          conversion + hash locking only
6. Manager authorization for INT8 Pass 2 scored run
7. INT8 Pass 2:                          23/24 PASS
8. Manager acceptance of INT8 result + addenda
9. Manager authorization for INT4 stress run
10. INT4 Pass 1:                         conversion + hash locking only
11. Manager authorization for INT4 Pass 2 scored run
12. INT4 Pass 2 (this run):              24/24 PASS
```

---

## 3. Provenance

```
Model:              Qwen/Qwen2.5-3B-Instruct  (INT4)
Conversion:         q_bits=4, q_group_size=64, dtype=bfloat16
Bits per weight:    4.501
Converted dir:      tier0-run/Qwen2.5-3B-Instruct-mlx-int4/
Decoding:           temperature=0.0, max_tokens=16, sampler=make_sampler(temp=0.0)
fresh_generation:   True
Output file:        stress_constructibility_3b_int4_1780872258.json
Runner script:      stress_constructibility_3b.py
```

---

## 4. All hashes

```
manifest_hash:              sha256:28d249dc6a56fbad54be5606c4285eaa78f286f31acf22610357e40bf12a3481
scorer_hash:                sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc
validator_hash:             sha256:28d249dc6a56fbad54be5606c4285eaa78f286f31acf22610357e40bf12a3481
tokenizer_hash:             sha256:29caa515cc153c78bf846329ad2a4e94df271c49c309024635cc015834acacce
runner_hash:                sha256:d17661946de856e86f7833cb9a247065b1fadbf345f01f7de284eba3110b20d6
quant_config_hash:          sha256:9e79b9b727d0e06db1389f06c0b8e77fdb91fe00accfac0718db98fdeb7c5d3e
quant_model_manifest_hash:  sha256:7ca665f0005a428d2826bc38b836ad566fe16744f9b7697cad57f384adcf2678
```

Runner hash note: updated from INT8 Pass 2 value (sha256:3622a9ef...) due to
the per-bits dict fix applied between INT8 Pass 2 and INT4 Pass 1. This is the
correct runner_hash for this run.

Validator hash note: equals manifest_hash. validate_tasks() is defined in
tasks_fork_a_n24.py (line 186), the same file as the item manifest.
Validator behavior is version-pinned by the manifest hash.
(Outcome C — same rationale as INT8 run.)

---

## 5. Preflight — all STOP gates cleared

```
manifest_hash             ✓ match  sha256:28d249dc...
scorer_hash               ✓ match  sha256:4036b1ad...
validator                 ✓ pass   624/624 checks
tokenizer_hash            ✓ verified
quant_config_hash         ✓ match  (locked in APPROVED_QUANT_CONFIG_HASH[4])
quant_model_manifest_hash ✓ match  (locked in APPROVED_QUANT_MODEL_MANIFEST_HASH[4])
model load                ✓ success
```

---

## 6. Scoring breakdown

```
scaffold_class:
  SCAFFOLD_PRESENT: 24
  SCAFFOLD_ABSENT:   0

format_class:
  FORMAT_PASS: 24
  FORMAT_FAIL:  0

content_class (INT4):
  RETURNED_TARGET_OBJ: 24

content_class (FP16 reference):
  RETURNED_TARGET_OBJ: 24

numeric_ooc_count: 0
failures: none
```

---

## 7. Per-item results (summary)

All 24 items: SCAFFOLD_PRESENT / FORMAT_PASS / RETURNED_TARGET_OBJ / exact_output_match=True / PASS.

No per-item failure records.

---

## 8. Non-monotone per-rung observation

```
FP16 (baseline):  24/24  SCAFFOLD_PRESENT, FORMAT_PASS, RETURNED_TARGET_OBJ on all items
INT8:             23/24  1 scaffold-contract dropout at L3_15 (SCAFFOLD_ABSENT / UNCLASSIFIED)
INT4:             24/24  SCAFFOLD_PRESENT, FORMAT_PASS, RETURNED_TARGET_OBJ on all items
```

INT8 had one scaffold-contract dropout (L3_15: raw='XONBX', scaffold absent).
INT4 had no strict-format, content, numeric, or scaffold failures. L3_15: raw='ANSWER: XONBX', strict pass.

This is a non-monotone per-rung observation. It does not imply monotone bit-depth
degradation. It does not license:

```
INT4 is generally safer than INT8.
Compression improves performance.
Quantization is harmless.
```

---

## 9. Permitted Track 2 statement (per Manager authorization)

```
On the frozen n=24 Synthetic Key-Value Selection Constructibility construction at 3B,
both INT8 and INT4 cleared the pre-registered stress gate. INT8 produced one
scaffold-contract dropout; INT4 produced 24/24 strict-format correct outputs. These
results apply only to this construction, model, quantization method, tokenizer, scorer,
validator, decoding settings, and output contract.
```

---

## 10. Position subgroup (diagnostic — does not modify gate)

```
pos=2: 8/8
pos=3: 8/8
pos=4: 8/8
```

---

## 11. Decision-token top-k (diagnostic / provenance only)

All 24 items: decision token at response_pos=3. Top-1 logprob=0.000 on all 24 items.

```
Note: decision-token top-k logs are provenance and diagnostic artifacts only.
They are NOT used to make capability or mechanism claims.
```

---

## 12. Scope boundary

This INT4 result applies only to:

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
Quantization:    INT4 (q_bits=4, q_group_size=64)
```

This result does not generalize to:

```
multi-hop tasks
heterogeneous-relation tasks
natural-language tasks
other model sizes
other quantization methods
```

---

## 13. Not licensed from this result

```
No seam claim
No mechanism claim
No general quantization robustness claim
No general retrieval / binding / reasoning claim
No multi-hop claim
No natural-language generalization
No other-model-size claim
No further stress runs (require separate Manager authorization)
```

Track 2 results remain Track 2. They do not enter the metrology paper
unless Manager explicitly authorizes inclusion.

---

## 14. Files

```
stress_constructibility_3b.py                     — runner (INT8 + INT4)
stress_constructibility_3b_int4_1780872258.json   — raw output JSON, full provenance
RESULTS-FORK-A-INT4.md                            — this file
tasks_fork_a_n24.py                               — frozen n=24 L3 manifest + validator
tasks_exp8.py                                     — frozen three-axis scorer
fp16_constructibility_3b_n24_1780867214.json      — FP16 baseline reference (immutable)
RESULTS-FORK-A-INT8.md                            — INT8 results for cross-rung reference
```
