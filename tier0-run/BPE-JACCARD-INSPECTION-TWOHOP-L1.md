# BPE-Jaccard Tokenizer Inspection — Two-Hop Level 1

**Date:** 2026-06-08
**Author:** CS Engineer
**Status:** COMPLETE — amendment required before Stage 1 cell generation
**Authorization basis:** Manager memo "Threshold Proposal Revision 2 — Manager Approval," 2026-06-08

---

## 1. Tokenizer

**Model family:** Qwen2.5-3B-Instruct (BPE, 151,643-token vocabulary)
**Tokenizer type:** Byte-level BPE with Split+ByteLevel pre-tokenizer

**Tokenizer hash (confirmed identical across both local model variants):**

```
Qwen2.5-3B-Instruct-mlx-int4/tokenizer.json
sha256:3fd169731d2cbde95e10bf356d66d5997fd885dd8dbb6fb4684da3f23b2585d8

Qwen2.5-3B-Instruct-mlx-int8/tokenizer.json
sha256:3fd169731d2cbde95e10bf356d66d5997fd885dd8dbb6fb4684da3f23b2585d8
```

**FP16 model note:** The Stage 1 FP16 runner uses `Qwen/Qwen2.5-3B-Instruct` loaded via mlx-lm from HuggingFace. This model shares architecture and tokenizer with the local quantized variants. Before any Stage 1 run, the FP16 tokenizer hash must be confirmed at download time and recorded in run provenance. Expected hash: same as above (same tokenizer across precision variants). If hash differs, halt and escalate to Team Lead.

---

## 2. Token pool segmentations (smoke test tokens)

All tokens use the byte-level BPE algorithm. Segmentations are deterministic given the locked tokenizer.

```
CPQVX  →  ['CP', 'Q', 'V', 'X']    (4 subwords, ids: 7123, 48, 53, 55)
CPQWX  →  ['CP', 'Q', 'WX']        (3 subwords, ids: 7123, 48, 65376)
ARVUX  →  ['AR', 'V', 'UX']        (3 subwords, ids: 934, 53, 13401)
BMNIX  →  ['BM', 'N', 'IX']        (3 subwords, ids: 28942, 45, 5396)
FVPLX  →  ['F', 'V', 'PL', 'X']    (4 subwords, ids: 37, 53, 2916, 55)
EJMRX  →  ['E', 'J', 'MR', 'X']    (4 subwords, ids: 36, 41, 18446, 55)
DXQNV  →  ['DX', 'Q', 'NV']        (3 subwords, ids: 16591, 48, 36326)
CPQVY  →  ['CP', 'Q', 'V', 'Y']    (4 subwords, ids: 7123, 48, 53, 56)
CPQWY  →  ['CP', 'Q', 'W', 'Y']    (4 subwords, ids: 7123, 48, 54, 56)
```

Key observation: all five-character uppercase identifiers segment into 3–4 subwords. None is a single-token unit in the vocabulary — every identifier requires at least two BPE merge steps to produce subword units.

---

## 3. BPE-Jaccard values — key pairs

BPE-Jaccard(A, B) = |subwords(A) ∩ subwords(B)| / |subwords(A) ∪ subwords(B)|

```
Pair                         Levenshtein  BPE-Jaccard  Intersection           Union-size
CPQVX / CPQWX  (near-miss)   1            0.4000       {CP, Q}                5
CPQVX / CPQVY  (1-edit)      1            0.6000       {CP, Q, V}             5
CPQVY / CPQWY  (1-edit)      1            0.6000       {CP, Q, Y}             5
CPQWX / CPQVY  (2-edit)      2            0.4000       {CP, Q}                5
CPQWX / CPQWY  (2-edit)      2            0.4000       {CP, Q}                5
CPQVX / CPQWY  (2-edit)      2            0.3333       {CP, Q}                6
CPQVX / FVPLX  (dissimilar)  4            0.3333       {V, X}                 6
CPQVX / ARVUX  (dissimilar)  4            0.1667       {V}                    6
BMNIX / EJMRX  (dissimilar)  5            0.0000       {}                     7
ARVUX / BMNIX  (dissimilar)  5            0.0000       {}                     6
```

---

## 4. Key finding — j ≥ 0.50 requires amendment

**The approved BPE-Jaccard threshold of j ≥ 0.50 is incorrect for this tokenizer.**

The declared near-miss pair — CPQVX / CPQWX (Levenshtein = 1) — produces BPE-Jaccard = 0.40. This is below the approved threshold of 0.50. Under the approved threshold, this pair would NOT be flagged as a near-miss, defeating the purpose of the BPE-Jaccard confirmatory check.

The approved threshold assumed near-miss pairs would produce j ≥ 0.50. Empirical inspection shows the correct range for 1-edit near-miss pairs is j = 0.40–0.60, depending on where the edit falls in the token string and which BPE merges apply.

**Why CPQVX/CPQWX produces j = 0.40 while CPQVX/CPQVY produces j = 0.60:**
- CPQVX = {CP, Q, V, X}; CPQWX = {CP, Q, WX} — the last-character edit collapses W+X into a single merged subword (WX = id 65376), creating an asymmetric intersection
- CPQVX = {CP, Q, V, X}; CPQVY = {CP, Q, V, Y} — the last-character edit changes only X→Y while preserving the V subword, producing higher intersection

Both pairs have Levenshtein = 1, but BPE-Jaccard depends on whether the edit happens to collapse or split a merge boundary.

---

## 5. Distribution survey — broader token pool

Pairwise BPE-Jaccard over 14-token sample (91 pairs):

```
≥ 0.50:          [0.60, 0.60]                   — 2 pairs (CPQ-family, last-char edits only)
[0.40, 0.49]:    [0.40, 0.40, 0.40, 0.40]       — 4 pairs (CPQ-family or near-CPQ, 1–2-edit)
[0.30, 0.39]:    [0.33, 0.33, 0.33, 0.33, 0.33] — 5 pairs (includes dissimilar: CPQVX/FVPLX)
[0.20, 0.29]:    [0.20, 0.20, 0.20, 0.20]       — 4 pairs
< 0.20:          77 pairs
```

**Natural gap:** Values cluster at ≥ 0.40 (near-family pairs) and ≤ 0.333 (cross-family pairs). There are no values in [0.34, 0.39] in this sample.

---

## 6. Structural finding — BPE-Jaccard limitations for this token pool

**BPE-Jaccard is a less reliable discriminant than Levenshtein for this token pool.** Two reasons:

**Reason 1 — BPE fragmentation of short uppercase identifiers.** The Qwen2.5 BPE tokenizer has specific merges for common 2-char uppercase pairs (CP, AR, BM, MR, PL, UX, IX, etc.) but does not have vocabulary entries for complete 5-char identifiers. Every token in the pool segments into 3–4 subwords. Individual single-character subwords (V, X, Q, etc.) appear in many different tokens, creating spurious BPE-Jaccard similarity for tokens that share no Levenshtein proximity.

Example: CPQVX and FVPLX share {V, X} in their subword sets (BPE-Jaccard = 0.333) despite having Levenshtein distance = 4. Under a j ≥ 0.30 threshold, this pair would be flagged as similar — a false positive.

**Reason 2 — Merge-boundary sensitivity.** Two tokens with identical Levenshtein distance produce very different BPE-Jaccard depending on where the edit falls relative to merge boundaries. CPQVX/CPQVY (j=0.60) and CPQVX/CPQWX (j=0.40) both have Levenshtein=1, but differ by 0.20 in BPE-Jaccard because one edit preserves a merge boundary and the other collapses one.

---

## 7. Revised BPE-Jaccard threshold recommendation

**Revised proposal: j ≥ 0.40 (down from j ≥ 0.50)**

Rationale:
- j ≥ 0.40 correctly flags the declared near-miss (CPQVX/CPQWX, j=0.40) as near-miss
- j ≥ 0.40 does NOT flag cross-family dissimilar pairs (max j = 0.333 in this survey)
- Natural gap in the observed distribution between j = 0.333 (highest dissimilar pair) and j = 0.400 (lowest intended near-miss pair)
- j ≥ 0.40 is the lowest threshold that correctly separates the near-miss from all observed dissimilar pairs in this sample

**Construction constraint implication:** Any two C-role tokens (from different chains) in the same cell with BPE-Jaccard ≥ 0.40 must be reviewed. Cross-chain C-role token pairs should be drawn from different letter families to keep BPE-Jaccard below the threshold.

**BPE-Jaccard as supplementary diagnostic, not standalone gate:** Given the merge-boundary sensitivity, BPE-Jaccard should not be the sole gate for near-miss detection. Levenshtein k ≤ 2 (approved, Manager-authorized) remains the primary criterion. BPE-Jaccard provides supplementary signal at the subword embedding level.

---

## 8. Amendment required

The approved BPE-Jaccard threshold (j ≥ 0.50) must be amended before Stage 1 cell generation. This is a narrow empirical correction driven by inspection, not a design change.

**Amendment:** j ≥ 0.50 → j ≥ 0.40

**Routing:** This amendment requires Team Lead approval (narrow correction to approved threshold, same class as the anchor_echo priority correction from Stage 0). If Team Lead approves, Manager confirmation is recommended given the original threshold required Manager approval.

**Stage 1 cell generation is blocked until this amendment is approved.**

---

## 9. BPE round-trip (audit_round_trip) — status

`audit_round_trip()` in `tasks_twohop_l1.py` requires an instantiated tokenizer object (not just the tokenizer.json file). Running round-trip validation requires the tokenizer to be loaded via the mlx-lm or transformers library. This can be done offline (no model inference required). Round-trip validation should be run on all unique token-pool identifiers before any Stage 1 cell is finalized.

This step is not blocked pending the BPE-Jaccard amendment — it can proceed in parallel.

---

## 10. Files

```
BPE-JACCARD-INSPECTION-TWOHOP-L1.md   this document
tokenizer.json (int4):                 sha256:3fd169731d2cbde95e10bf356d66d5997fd885dd8dbb6fb4684da3f23b2585d8
tokenizer.json (int8):                 sha256:3fd169731d2cbde95e10bf356d66d5997fd885dd8dbb6fb4684da3f23b2585d8
tasks_twohop_l1.py:                    sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
```

— CS Engineer
