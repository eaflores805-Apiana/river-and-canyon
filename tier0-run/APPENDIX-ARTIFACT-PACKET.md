# APPENDIX-ARTIFACT-PACKET.md

**Date:** 2026-06-07
**Owner:** CS Engineer
**Purpose:** Appendix-ready artifact packet for the metrology paper (v0.95 → v1.0 closure)
**Scope:** Exp6 through Exp8B only. Track 2 results excluded per Manager instruction.

---

## A. Dummy-Baseline Results Table

Source: `tasks_exp8.py` — `validate_tasks()` function, executed 2026-06-07.
Manifest hash verified: `sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc`

These baselines apply to the n=8 L2 Arm 2 construction (Exp8A items).

| Dummy baseline type | Score | Threshold | Pass/Fail | Shortcut ruled out |
|---|---|---|---|---|
| always return fact-1 object | 0.000 | 0.875 | FAIL | position-1 anchoring |
| always return fact-2 object | 0.375 | 0.875 | FAIL | position-2 anchoring (max) |
| always return fact-3 object | 0.375 | 0.875 | FAIL | position-3 anchoring (max) |
| always return fact-4 object | 0.250 | 0.875 | FAIL | position-4 anchoring |
| always return fact-5 object | 0.000 | 0.875 | FAIL | position-5 anchoring |
| always return first object in context | 0.000 | 0.875 | FAIL | primacy anchoring |
| always return last object in context | 0.000 | 0.875 | FAIL | recency anchoring |

```
max_dummy_score:      0.375
feasibility_threshold: 0.875
[OK] max_dummy (0.375) < threshold (0.875) — baseline inflation not a concern
```

**Interpretation:** No deterministic single-position shortcut achieves above 0.375. The feasibility threshold (0.875) is more than twice the maximum dummy score. A model that simply memorizes or anchors to any single position cannot pass the gate.

**Artifact path:** `tasks_exp8.py` — validator source; run `python3 tasks_exp8.py` to reproduce.

---

## B. Validator Execution Log

### B.1 — Exp8 / Arm 2 (n=8 L2 manifest)

```
Source file:     tasks_exp8.py
Manifest hash:   sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc
Run date:        2026-06-07 (freshly executed for this packet)
Check count:     208 checks across 8 items (26 checks per item)
Result:          ALL CHECKS PASSED

Check types (26 per item):
  Token format checks (5-char uppercase)
  Pool exclusion checks (no overlap with prior exp tokens)
  Subject/object distinctness checks
  Prompt structure checks (scaffold present, fact ordering)
  BPE round-trip checks (all 80 tokens round-trip correctly)
  Dummy baseline verification (max_dummy < threshold)

Scorer unit tests: 9 pre-registered cases, all passed
BPE piece distribution: {2: 2, 3: 64, 4: 14}
```

**Provenance note:** Validator and scorer are defined in the same file (`tasks_exp8.py`). Validator hash equals manifest hash. This is intentional — validator behavior is version-pinned by the manifest artifact.

---

## C. Reproducibility Table — Exp6 through Exp8B

### Provenance notes before table

The following artifact gaps apply to Exp6 and Exp7:

```
Exp6/Exp7 artifact gaps (documented 2026-06-07):
  - manifest_hash: absent from Exp6 JSON; present in Exp7 JSON only
  - tokenizer_hash: absent from both Exp6 and Exp7 JSONs
  - runner_hash: absent from both Exp6 and Exp7 JSONs
  - scorer_hash: absent from both Exp6 and Exp7 JSONs
  - decoding settings: NOT stored in Exp6/Exp7 JSON artifacts
    max_tokens=512, temperature=0.0 reconstructed from run_stability_screen.py
    source code only — not self-documenting at JSON level
  - This is a closed provenance gap. Settings are derived from source inspection,
    not from the artifact. Exp6/Exp7 results should be cited with this caveat.
```

The following artifact gaps apply to Exp8A:

```
Exp8A artifact gaps (documented 2026-06-07):
  - scorer_hash: absent (pre-scorer-amendment; three-axis scorer not yet locked)
  - tokenizer_hash: absent
  - runner_hash: absent
  - prompt_hash: absent from result items
  - scaffold_class: absent from result items (pre-scaffold-axis amendment)
  - content_class for numeric failures: recorded as UNCLASSIFIED in JSON artifact
    Post-hoc reclassification as RETURNED_NON_CONTEXT_TOKEN was applied in
    documentation and memory only; the JSON artifact retains UNCLASSIFIED.
    See Section D for transition matrix using actual artifact values.

  NOT a gap (confirmed 2026-06-07 by direct artifact inspection):
  - decoding settings: PRESENT in artifact as {"temperature": 0.0, "max_tokens": 16}
    Do not cite decoding as source-reconstructed for Exp8A.
```

### Reproducibility table

| Run | Model | Model tag | Manifest hash | Prompt hash | Tokenizer hash | Scorer hash | Validator hash | Decoding | Raw packet path |
|---|---|---|---|---|---|---|---|---|---|
| Exp6 | Qwen2.5-1.5B-Instruct | FP16 | *(absent)* | *(absent)* | *(absent)* | *(absent)* | *(absent)* | temp=0.0, max_tokens=512 *(from source)* | `stability_screen_1780771434.json` |
| Exp7 | Qwen2.5-1.5B-Instruct | FP16 | sha256:177c5f7f1fa39d902fafe4974e5d449f005e6200fe5101efb54b25186096f20e | *(absent)* | *(absent)* | *(absent)* | sha256:177c5f7f... | temp=0.0, max_tokens=512 *(from source)* | `stability_screen_1780776502.json` |
| Exp8A | Qwen2.5-1.5B-Instruct | FP16 | sha256:14129d0bfe2cae1c3e4d817a8423eaf5513665741c04f1d388ac8da34a9074de | *(absent from items)* | *(absent)* | *(absent — pre-amendment)* | sha256:14129d0b... | temp=0.0, max_tokens=16 *(artifact-backed)* | `fp16_screen_exp8_arm2_1780781863.json` |
| Exp8B | Qwen2.5-1.5B-Instruct | FP16 | sha256:695b1ac90aa0745765f9785435f527757a248f4ad27a85ce8f249230610ec56e | present per item | *(absent)* | *(absent — post-amendment scorer not stored in JSON)* | sha256:695b1ac9... | temp=0.0, max_tokens=16 *(artifact-backed)* | `fp16_screen_exp8b_1780789038.json` |

**Scorer note for Exp8A/Exp8B:**
The three-axis scorer (`tasks_exp8.py`, `sha256:4036b1ad...`) was locked after Exp8A ran. Exp8A was not rescored under the three-axis scorer. Exp8B used the three-axis scorer. The scorer hash `sha256:4036b1ad...` applies to Exp8B and all Fork A runs; it does not apply to the Exp8A artifact.

---

## D. Paired Exp8A → Exp8B Transition Matrix

Source artifacts:
- Exp8A: `fp16_screen_exp8_arm2_1780781863.json`
- Exp8B: `fp16_screen_exp8b_1780789038.json`

Both runs: Qwen/Qwen2.5-1.5B-Instruct, FP16, temp=0.0, max_tokens=16.
Single variable changed: query wording only (Exp8A: "Which value is associated with SUBJ_T?"; Exp8B: "Which token is assigned to SUBJ_T?").

| item_id | pos | target | Exp8A raw | Exp8A class | Exp8A pass | Exp8B raw | Exp8B class | Exp8B pass | Transition label |
|---|---|---|---|---|---|---|---|---|---|
| L2_01 | 2 | ARVUX→ICVLX | `ANSWER: ICVLX` | RETURNED_TARGET_OBJ | ✓ | `ANSWER: ICVLX` | RETURNED_TARGET_OBJ | ✓ | STABLE PASS |
| L2_02 | 2 | CIRNX→OBLVX | `ANSWER: 0` | UNCLASSIFIED | ✗ | `ANSWER: OBLVX` | RETURNED_TARGET_OBJ | ✓ | RESCUED (numeric OOC → correct) |
| L2_03 | 2 | HIBNX→OICVX | `ANSWER: 10` | UNCLASSIFIED | ✗ | `ANSWER: OHIBX` | RETURNED_OBJ_POS_1 | ✗ | MIGRATED FAIL (numeric → positional) |
| L2_04 | 3 | UFBNX→PCIVX | `ANSWER: PCIVX` | RETURNED_TARGET_OBJ | ✓ | `ANSWER: PBCVX` | RETURNED_OBJ_POS_2 | ✗ | DESTABILIZED (correct → positional) |
| L2_05 | 3 | EBVNX→SCIVX | `ANSWER: SCIVX` | RETURNED_TARGET_OBJ | ✓ | `ANSWER: SCIVX` | RETURNED_TARGET_OBJ | ✓ | STABLE PASS |
| L2_06 | 3 | HGIVX→IDBVX | `ANSWER: IDBVX` | RETURNED_TARGET_OBJ | ✓ | `ANSWER: IDBVX` | RETURNED_TARGET_OBJ | ✓ | STABLE PASS |
| L2_07 | 4 | UNVBX→OECVX | `ANSWER: OECVX` | RETURNED_TARGET_OBJ | ✓ | `ANSWER: OECVX` | RETURNED_TARGET_OBJ | ✓ | STABLE PASS |
| L2_08 | 4 | ACNLX→PJBVX | `ANSWER: PJBVX` | RETURNED_TARGET_OBJ | ✓ | `ANSWER: PJBVX` | RETURNED_TARGET_OBJ | ✓ | STABLE PASS |

```
Pass count:  Exp8A 6/8   Exp8B 6/8   (both NOT FEASIBLE, threshold ≥7/8)

Stable passes:        5  (L2_01, L2_05, L2_06, L2_07, L2_08)
Rescued:              1  (L2_02 — numeric OOC eliminated by wording change)
Migrated fail:        1  (L2_03 — numeric OOC → positional anchoring)
Destabilized:         1  (L2_04 — correct in Exp8A → positional fail in Exp8B)
```

**Provenance note on Exp8A content_class:** The Exp8A JSON artifact records UNCLASSIFIED for L2_02 and L2_03. The three-axis scorer introduced RETURNED_NON_CONTEXT_TOKEN as a class after Exp8A ran. Exp8A was not rescored. The artifact values (UNCLASSIFIED) are used here, not post-hoc reclassifications. See Section C for scorer amendment history.

---

## E. Canonicalization / Scorer Snippet

Source: `tasks_exp8.py` — locked, `sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc`

### E.1 — Instruction scaffold

```python
_SCAFFOLD = "Respond using only this exact format with nothing before or after: ANSWER:"
# Appended to each prompt: "Which value is associated with {target_subj}? {_SCAFFOLD}"
```

### E.2 — Scaffold detection (axis 1)

```python
def score_arm2_scaffold(output: str) -> dict:
    if "ANSWER:" in output and len(output.split("ANSWER:", 1)[1].strip()) > 0:
        return {"scaffold_class": "SCAFFOLD_PRESENT"}
    return {"scaffold_class": "SCAFFOLD_ABSENT"}
```

`SCAFFOLD_PRESENT`: output contains 'ANSWER:' followed by non-empty content.
`SCAFFOLD_ABSENT`: output does not contain a usable ANSWER: prefix.

### E.3 — Format scoring (axis 2)

```python
FORMAT_PASS regex: ^ANSWER:\s+[A-Z]{4,8}$

def score_arm2_format(output: str) -> dict:
    stripped = output.strip()
    if re.match(r'^ANSWER:\s+[A-Z]{4,8}$', stripped):
        return {"format_class": "FORMAT_PASS"}
    return {"format_class": "FORMAT_FAIL"}
```

`FORMAT_PASS`: stripped output exactly matches the regex (4–8 uppercase letters after `ANSWER: `).
`FORMAT_FAIL`: anything else.

### E.4 — Answer extraction (used by content scorer)

```python
def _extract_answer_token(output: str):
    stripped = output.strip()
    if re.match(r'^ANSWER:\s+[A-Z]{4,8}$', stripped):
        return stripped.split(None, 1)[1]   # token after "ANSWER:"
    return None
```

The extractor depends on the ANSWER: scaffold. If the scaffold is absent or malformed, the extractor returns None and content_class becomes UNCLASSIFIED. This is strict scorer behavior — no bare-token rescue.

### E.5 — Content scoring priority order (axis 3, 9 classes locked)

```
Priority (locked):
  1. RETURNED_TARGET_OBJ        — extracted token == target object
  2. RETURNED_OBJ_POS_1..5      — extracted token == non-target object at position k
  3. RETURNED_SUBJ_TOKEN        — extracted token == any subject in context
  4. RETURNED_NON_CONTEXT_TOKEN — extracted token is not any subject or object in context
  5. UNCLASSIFIED               — extractor returned None (scaffold absent or format fail)
```

### E.6 — Scorer amendment history

```
Pre-Exp8A:   two-axis scorer (format_class + content_class, no scaffold axis)
Exp8A run:   two-axis scorer applied; numeric failures recorded as UNCLASSIFIED
             (RETURNED_NON_CONTEXT_TOKEN class did not exist at run time)
Amendment:   three-axis scorer locked (scaffold_class added; RETURNED_NON_CONTEXT_TOKEN
             added to content priority list; renamed from OUT_OF_CONTEXT_TOKEN)
Exp8B run:   three-axis scorer applied; scaffold_class present in all result items
Rescoring:   Exp8A was NOT rescored under three-axis scorer.
             Exp8A JSON artifact retains two-axis classifications.
```

---

## F. Artifact Status Summary

| Item | Status | Note |
|---|---|---|
| Dummy-baseline numbers | **PROVIDED** | From tasks_exp8.py validator; max dummy 0.375 < threshold 0.875 |
| Validator execution log | **PROVIDED** | 208 checks, 26 per item, all pass |
| Exp6 reproducibility | **PARTIAL** | manifest/tokenizer/runner/scorer hashes absent from JSON; decoding from source only |
| Exp7 reproducibility | **PARTIAL** | manifest hash present; tokenizer/runner/scorer hashes absent; decoding from source |
| Exp8A reproducibility | **PARTIAL** | manifest hash present; scorer/tokenizer/runner hashes absent; scaffold_class absent |
| Exp8B reproducibility | **PARTIAL** | manifest + prompt hashes present; scorer/tokenizer/runner hashes absent |
| Exp8A→Exp8B transition matrix | **PROVIDED** | Artifact-backed from both JSONs |
| Scorer / canonicalization snippet | **PROVIDED** | From locked tasks_exp8.py |

**Guidance for Senior:** The dummy-baseline numbers exist and are provided above (Section A). The shortcut-resistance claim is supported for the n=8 L2 Arm 2 construction. The provenance gaps for Exp6/Exp7 are real and should be reflected in the manuscript (e.g., "decoding settings reconstructed from source" rather than "stored in artifact"). Exp8A's UNCLASSIFIED vs RETURNED_NON_CONTEXT_TOKEN discrepancy between artifact and documentation should be noted if the paper cites item-level failure classes for Exp8A.
