# Tokenizer Hash Reconciliation — Two-Hop Level 1

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Requested by:** Team Lead memo — "FP16 Stage 1 Return Packet — Branch 3 Accepted Pending Tokenizer Hash Reconciliation" 2026-06-08
**Status:** RECONCILED — BPE-Jaccard audit confirmed under FP16 tokenizer; all 5 questions answered

---

## Background

The BPE-Jaccard j ≥ 0.40 construction audit (Gate 0.5) was performed during cell generation using the local MLX INT4/INT8 tokenizer file:

```
File: tier0-run/Qwen2.5-3B-Instruct-mlx-int4/tokenizer.json
Hash: sha256:3fd169731d2cbde95e10bf356d66d5997fd885dd8dbb6fb4684da3f23b2585d8
```

The Stage 1 FP16 run used the HuggingFace-hosted tokenizer loaded via `mlx_lm.load()`:

```
File: ~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/
      snapshots/aa8e72537993ba99e69dfaafa59ed015b17504d1/tokenizer.json
Hash: sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
```

The hashes differ. Team Lead required reconciliation before accepting the audit result as Gate 0.5 evidence for the run.

---

## Question 1 — Are the two tokenizer files the same tokenizer?

**Yes.** Both files are the Qwen2.5-3B-Instruct tokenizer (model snapshot aa8e72537993ba99e69dfaafa59ed015b17504d1). They differ only in JSON serialization format for the BPE merge list, not in tokenizer content.

The INT4/INT8 MLX file (`sha256:3fd169731d...`) serializes BPE merges as JSON arrays: `["Ġ", "Ġ"]`.  
The FP16 HuggingFace file (`sha256:c0382117...`) serializes BPE merges as space-delimited strings: `"Ġ Ġ"`.

Both formats are standard representations of the same BPE merge rule. No vocabulary entries, merge rules, or special tokens differ.

---

## Question 2 — Why are they identical (vocab, normalized merges, BPE behavior)?

Empirical verification performed 2026-06-08:

```
Vocab size:
  FP16 (sha256:c0382117...):   151,643 entries
  INT4 (sha256:3fd169731d...): 151,643 entries
  Match: YES

Merge count:
  FP16 (string format "Ġ Ġ"):     151,387 rules
  INT4 (list format ['Ġ','Ġ']):    151,387 rules
  Match: YES

Normalized merge comparison (string format, after splitting):
  fp16_norm == int4_norm: True
  Every merge rule at every index is identical after normalization.

Vocabulary dict comparison:
  fp16['model']['vocab'] == int4['model']['vocab']: True
  Every token → token-id mapping is identical.
```

BPE behavior is therefore identical: given any input string, both tokenizers produce the same token sequence. The SHA-256 hash difference is a JSON serialization artifact, not a tokenizer difference.

---

## Question 3 — Was the BPE-Jaccard audit performed under sha256:c0382117…?

**No.** The BPE-Jaccard audit in `BPE-JACCARD-INSPECTION-TWOHOP-L1.md` and in `generate_cell01.py` was performed under `sha256:3fd169731d...` (the local MLX INT4/INT8 tokenizer file at `Qwen2.5-3B-Instruct-mlx-int4/tokenizer.json`).

The audit was not re-run under the FP16 HuggingFace tokenizer before the Stage 1 run.

---

## Question 4 — Re-run under sha256:c0382117… — does j ≥ 0.40 still hold?

**Yes.** BPE-Jaccard audit re-run 2026-06-08 under the FP16 tokenizer (sha256:c0382117...):

```
Tokenizer used:          sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
Total unique tokens:     216  (all C-role tokens across 24 items × all 3 chains)
Round-trip failures:     0    (every token encodes and decodes to itself)

Cross-chain C-role pair violations (j ≥ 0.40):   0
  [No unintended near-miss pairs across chains — zero constraint violations]

Declared near-miss pairs — 24/24 j ≥ 0.40 confirmed:
  ZJMOL / ZJMZY    j = 0.50   ✓
  DBKSD / IMKSD    j = 0.50   ✓
  MRZSP / VDZSP    j = 0.50   ✓
  YYQGH / PJQGH    j = 0.50   ✓
  BAGCR / BAGQI    j = 0.40   ✓  (minimum — matches threshold exactly)
  [remaining 19 pairs all j ≥ 0.40 — not individually listed; available in raw audit output]

Result: PASS — Gate 0.5 BPE-Jaccard constraint satisfied under FP16 tokenizer.
```

The audit result is unchanged. Because the two tokenizers are byte-for-byte equivalent after normalization (Question 2), the BPE tokenization of all 216 C-role tokens is identical under both files, and the j-values are identical.

---

## Summary

| Question | Answer |
|---|---|
| Q1. Same tokenizer? | YES — serialization difference only |
| Q2. Why identical? | Vocab 151,643 identical; merges 151,387 normalized-identical; BPE behavior identical |
| Q3. Audit under sha256:c0382117...? | NO — audit used sha256:3fd169731d... |
| Q4. Re-run result under sha256:c0382117...? | PASS — 0 violations, 24/24 near-miss pairs j ≥ 0.40 |
| Q5. Documents updated? | YES — Run_Summary §2/§3/§16 and EXPERIMENT_LOG updated (this note) |

---

## Gate 0.5 status (post-reconciliation)

```
Gate 0.5  Token-construction audit   PASS (reconciled)
  BPE round-trip:                    0 failures
  Levenshtein violations:            0
  Trigram-Jaccard violations:        0
  C-role cross-pair violations:      0
  Declared near-miss pairs:          24/24 j ≥ 0.40 confirmed
  Tokenizer:                         sha256:c0382117...  (FP16 HuggingFace; confirmed run tokenizer)
  Original audit tokenizer:          sha256:3fd169731d... (INT4 MLX — serialization variant only)
  Equivalence confirmed:             vocab identical; normalized merges identical; BPE behavior identical
```

Gate 0.5 is unambiguously PASS under the run tokenizer.

---

**Reconciliation complete. No outstanding tokenizer hash discrepancy.**

— CS Engineer, 2026-06-08
