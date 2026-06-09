# Pre-Registration — Experiment 4: Dual-Scoring Degradation Test

**Locked:** 2026-06-06  
**Status:** LOCKED — do not edit after scorer implementation begins.

---

## 0. Rationale

Experiment 3 produced a statistically significant inverse seam under strict exact-match scoring (G(4b) CI [−0.0926, −0.0123]). Option A lenient rescore dissolved the signal: under content-aware scoring, G(4b) CI [−0.0370, 0.0000] includes zero. The apparent inverse seam was a format-compliance artifact — the model retained the correct answer content but stopped following the clipped output format on short-context prompts under INT4 compression.

This revealed that the experimental infrastructure conflated two distinct failure modes:

1. **Content loss** — the model no longer produces the correct answer in any form.
2. **Format compliance loss** — the model produces the correct answer but embeds it in a sentence or adds surrounding context, violating the strict output contract.

Strict exact-match scoring cannot distinguish them. Any future retention signal (positive or negative) is ambiguous unless both modes are scored explicitly and separately.

**Experiment 4 goal:** Separate content loss from format compliance loss, and run both seam tests simultaneously with the right scorer for each.

---

## 1. Model and hardware

| Field | Value |
|---|---|
| Model | `Qwen/Qwen2.5-1.5B-Instruct` |
| INT8 quantization | In-place via `quantize_model` (group_size=64) |
| INT4 source | `mlx-community/Qwen2.5-1.5B-Instruct-4bit` |
| Hardware | Apple Silicon (MLX, macOS 15+) |
| Decoding | temperature=0.0 (greedy, deterministic) |
| Max tokens | 512 |

Same model as Experiment 3. Format degradation was observed on this model; the dual scorer is designed to characterize it.

---

## 2. Tasks

**Task file:** `tasks_exp3.py` — the 12 stable pairs from Experiment 3 (9 substantive + 3 controls).

No new tasks are added. The stability screen results from Experiment 3 carry over. The dual scorer is the only change.

**Note on short-context controls:** AC1 and AC2 are 1-hop atomic controls. AC1 showed format compliance failure at INT8 in Experiment 3. These items are kept as-is; their format compliance behavior under dual scoring is part of what Experiment 4 characterizes.

---

## 3. Dual scoring — definitions (LOCKED)

### 3.1 strict_format_score

```
strict_format_score(output, expected) = float(norm(expected) in norm(output))

where norm(s) = "".join(s.lower().split())
```

Requires the full expected answer string to appear verbatim (case-insensitive, whitespace-collapsed) in the output. This is the pre-registered scorer from Experiments 1–3.

### 3.2 content_slot_score

```
content_slot_score(output, expected) =
  1.0 if value_tokens appears as a contiguous token sequence in output_tokens
  0.0 otherwise

where:
  expected_value = everything after the first "ANSWER:" in expected, stripped
                   (falls back to full expected string if "ANSWER:" absent)
  value_tokens   = re.sub(r'[^a-z0-9\s]', '', expected_value.lower()).strip().split()
  output_tokens  = re.sub(r'[^a-z0-9\s]', '', output.lower()).strip().split()
```

Checks whether the expected *value* (not the full format string) appears as a contiguous sequence of tokens anywhere in the normalized output. Token-phrase matching is used — not raw substring matching — to prevent false positives where the value string is a proper substring of an unrelated output token (e.g., "active" appearing as a substring of "inactive" would be a false positive under raw substring matching; token-phrase matching correctly returns 0).

A content_slot_score of 1 means the model produced the correct answer somewhere in its output, regardless of format. Does not require the "ANSWER:" prefix.

For items where `expected` does not contain "ANSWER:", content_slot_score falls back to strict_format_score.

### 3.3 partial_content_score (compound-noun diagnostic)

```
partial_content_score(output, expected) =
  count of value_tokens found in norm_content(output)
  / total value_tokens

where value_tokens = value.split()
```

Used to detect compound-noun modifier drops (e.g., "silver token" → "token": partial_content_score = 0.5, content_slot_score = 0). Not used as a primary metric; logged for failure classification only.

### 3.4 Hierarchy rule (LOCKED)

> **content_slot_score is the primary scorer for all content/capability claims.**  
> **strict_format_score is the primary scorer for format-compliance claims only.**

G(w) for seam detection is computed from content_slot_score.  
G_strict(w) for format-degradation characterization is computed from strict_format_score.  
These are reported separately and interpreted separately.

A seam claim requires G_content(w) to exclude zero. A strict-scoring result that is not confirmed by content scoring is classified as a format-compliance artifact, not a seam signal.

---

## 4. Failure taxonomy (LOCKED)

Every item at every rung is classified into exactly one failure class. Classification uses both scorers and partial_content_score.

| Class | strict | content | partial | Definition |
|---|---|---|---|---|
| `PASS` | 1 | 1 | — | Correct answer, correct format |
| `FORMAT_COMPLIANCE_LOSS` | 0 | 1 | — | Correct answer present; format violated |
| `COMPOUND_NOUN_DROP` | 0 | 0 | > 0 | Partial answer present; modifier(s) dropped |
| `CONTENT_LOSS` | 0 | 0 | 0 | Correct answer absent from output entirely |
| `ROBUST_WRONG` | 0 | 0 | 0 | Same wrong answer at all rungs (consistent hallucination) |

`ROBUST_WRONG` is flagged when: content_slot_score = 0 at FP16 and at the stressed rung, and the output is identical or near-identical across rungs. Items that fail at FP16 are excluded from the stress sweep (inherited from stability screen), so ROBUST_WRONG should not appear for stable pairs; the class is included for completeness.

**Aggregate per rung:** Report count and fraction of each class across all items. The format compliance rate = fraction of items in `PASS` + `FORMAT_COMPLIANCE_LOSS` (content present but format may vary).

---

## 5. Primary readout

### 5.1 G_content(w) — seam test (Test 1)

For each eligible pair at each rung w ∈ {INT8, INT4}:

```
R_composite_content(w) = content_slot_score_narrow(w) / content_slot_score_narrow(FP16)
R_component_content(w) = mean content_slot_score across component checks at w
                         / mean content_slot_score across component checks at FP16

G_content(w) = R_component_content(w) − R_composite_content(w)
```

Bootstrap CI on mean G_content(w), 1000 iterations, seed=0.

**Seam signal (Test 1):** mean G_content(w) CI lower bound > 0, calibration-invariant.

### 5.2 G_strict(w) — format-degradation test (Test 2)

```
R_composite_strict(w) = strict_format_score_narrow(w) / strict_format_score_narrow(FP16)
R_component_strict(w) = mean strict_format_score across component checks at w
                        / mean strict_format_score across component checks at FP16

G_strict(w) = R_component_strict(w) − R_composite_strict(w)
```

Bootstrap CI on mean G_strict(w), 1000 iterations, seed=0.

**Format-degradation finding (Test 2):** G_strict(w) CI excludes zero (in either direction) AND G_content(w) CI includes zero — strict score drops while content score is flat.

### 5.3 Format compliance rate per rung

```
format_compliance_rate(w) = fraction of all items where strict_format_score(w) = 1
```

Tracked for narrow arm, broad arm, and component checks separately. A declining format compliance rate at INT8 or INT4 is the primary characterization of Test 2.

### 5.4 ΔR (secondary)

```
ΔR_content(w) = mean R_broad_content(w) − mean R_narrow_content(w)
ΔR_strict(w)  = mean R_broad_strict(w)  − mean R_narrow_strict(w)
```

Both reported. ΔR_content is primary for capability claims.

---

## 6. Outcome table

| Outcome | Definition | Action |
|---|---|---|
| **A — seam candidate** | G_content(w) CI lower bound > 0, calibration-invariant | First positive content-level signal; inspect pair-level seam flags; run forced-intermediate follow-up |
| **B — baseline floor** | < 8 stable pairs (inherited from Exp 3 stability screen) | Not applicable — stability screen already run |
| **C — format cliff** | G_strict(w) CI excludes zero; G_content(w) CI includes zero | Format compliance degrades under compression; content retained; characterize by prompt length and context size |
| **D — flat** | Both G metrics CI overlap zero at all rungs under both calibrations | Neither seam nor format degradation detected at these rungs |
| **E — content inverse seam** | G_content(w) CI upper bound < 0 | Content-level inverse seam: components lose content, composite retains. Requires investigation. |

Outcome C is the pre-declared expected result based on Experiment 3 evidence. Confirming it under dual scoring with explicit failure-class counts closes the format-compliance characterization loop.

---

## 7. Kill conditions

**Kill for Outcome A promotion:**
- G_content(w) CI includes zero at any rung
- G_content(w) ranking flips across calibrations
- Gap traced to FP16 difficulty asymmetry between narrow and component arms
- Scoring asymmetry found between strict and content scorers that is not explained by format compliance

**Kill for Outcome C:**
- G_content(w) CI excludes zero (signal is not purely format) — reclassify as Outcome A or E depending on direction

---

## 8. Calibration-invariance gate

Results count only if G_content(w) and G_strict(w) rankings are invariant across:
- Calibration A: `calib=code`
- Calibration B: `calib=prose`

A result that flips sign or direction across calibrations is a calibration artifact, not a model behavior finding.

---

## 9. Scorer unit tests (required before implementation)

The dual scorer must pass the following hand-labeled examples before any live run. These are fixed here and must not be modified after scorer implementation begins.

### Strict = 1, Content = 1 (PASS)

| output | expected | strict | content |
|---|---|---|---|
| `ANSWER: File K` | `ANSWER: File K` | 1 | 1 |
| `ANSWER: APPROVED` | `ANSWER: APPROVED` | 1 | 1 |
| `ANSWER: silver token` | `ANSWER: silver token` | 1 | 1 |

### Strict = 0, Content = 1 (FORMAT_COMPLIANCE_LOSS)

| output | expected | strict | content |
|---|---|---|---|
| `ANSWER: amber box stores File K.` | `ANSWER: File K` | 0 | 1 |
| `ANSWER: obsidian drawer stores Log 3` | `ANSWER: Log 3` | 0 | 1 |
| `ANSWER: The blue locker contains the silver disk.` | `ANSWER: silver disk` | 0 | 1 |

### Strict = 0, Content = 0, Partial > 0 (COMPOUND_NOUN_DROP)

| output | expected | strict | content | partial |
|---|---|---|---|---|
| `ANSWER: token` | `ANSWER: silver token` | 0 | 0 | 0.5 |
| `ANSWER: jade` | `ANSWER: jade pass` | 0 | 0 | 0.5 |
| `ANSWER: cabinet` | `ANSWER: Cabinet 3` | 0 | 0 | 0.5 |

### Strict = 0, Content = 0, Partial = 0 (CONTENT_LOSS)

| output | expected | strict | content | partial |
|---|---|---|---|---|
| `ANSWER: INACTIVE` | `ANSWER: ACTIVE` | 0 | 0 | 0 |
| `ANSWER: OFF` | `ANSWER: ON` | 0 | 0 | 0 |
| `ANSWER: <status>UNKNOWN` | `ANSWER: PENDING` | 0 | 0 | 0 |

---

## 10. What this pre-registration does not commit to

- That Outcome C (format cliff) will be observed — it is pre-declared as the expected result, but the scorer decides
- The exact format compliance rate at each rung (measured, not predicted)
- Whether the AC1 INT8 failure observed in Experiment 3 will reproduce exactly (deterministic run, but fresh model load)
- That the dual scorer will reveal a seam signal — it is designed to be able to find one if it exists, not to find one

---

## 11. Ordering constraint (process lock)

The following order is required. Steps may not be reordered.

```
1. This pre-registration frozen          ← you are here
2. Failure taxonomy frozen               ← locked above in Section 4
3. Scorer definitions frozen             ← locked above in Section 3
4. Scorer unit tests written from Section 9 hand-labeled examples
5. Dual scorer implemented in run_tier0.py
6. Scorer validated against unit tests (must pass before live run)
7. Experiment 4 run (fresh, no peeking at outputs to adjust scorer)
8. Results recorded
```

The scorer serves the claim contract. The claim contract does not bend to match the scorer.
