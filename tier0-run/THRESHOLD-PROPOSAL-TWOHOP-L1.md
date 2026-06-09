# Threshold Proposal — Two-Hop Level 1 (Revised)

**Date:** 2026-06-07
**Revision:** 2 (incorporating reviewer consensus and Team Lead direction)
**Author:** CS Engineer
**Status:** APPROVED — locked 2026-06-08. See amendment note below.
**Manager approval:** Elias, Manager — memo "Threshold Proposal Revision 2 — Manager Approval," 2026-06-08
**Basis:** Stage 0 Instrument Lock Packet (closed 2026-06-07); Team Lead memo "Threshold Proposal Review — Shortcut Definition and Revision Request," 2026-06-07

---

## Amendment record — BPE-Jaccard j

BPE-Jaccard tokenizer-specific inspection (2026-06-08) found that the approved j ≥ 0.50 does not match the actual Qwen2.5-3B-Instruct tokenizer behavior: the declared near-miss pair (CPQVX / CPQWX, Levenshtein = 1) produces BPE-Jaccard = 0.40, below the approved threshold.

**Amendment:** j ≥ 0.50 → j ≥ 0.40
**Rationale:** Production-tokenizer calibration. j ≥ 0.40 preserves the intended separation between near-prefix-family pairs (≥ 0.40) and cross-family pairs (≤ 0.333) under the locked Qwen2.5-3B-Instruct tokenizer.
**Status: APPROVED / LOCKED — Manager, 2026-06-08** (memo: "Stage 1 Blockers — Manager Confirmation on BPE-Jaccard and Gate 1 FORMAT_PASS")

Full inspection details: `BPE-JACCARD-INSPECTION-TWOHOP-L1.md`

---

## Gate 1 FORMAT_PASS — addition (proposed 2026-06-08)

**Gate 1 FORMAT_PASS threshold: APPROVED / LOCKED — Manager, 2026-06-08** (memo: "Stage 1 Blockers — Manager Confirmation on BPE-Jaccard and Gate 1 FORMAT_PASS")

**Value:** 1.000 per query type, no pooling

**Gate meaning:** Gate 1 (contract adherence) passes only if every item in the scored query type produces FORMAT_PASS output at FP16. A single FORMAT_FAIL at FP16 fails Gate 1 and routes to Branch 2.

**Manager clarifications (locked):**
- NULL / NO_LINK returned under the negative-graph contract counts as FORMAT_PASS. Gate 1 measures contract adherence only.
- Correctness is excluded from Gate 1. An item that returns `ANSWER: WRONGTOKEN` is FORMAT_PASS; it fails Gate 2, not Gate 1.
- Per query type, not pooled: FORMAT_PASS = 1.000 must hold for hop1, hop2, composite, and negative_graph independently.

**Why 1.000 and not a fractional threshold:**

The output contract `^ANSWER:\s+[A-Z]{4,8}$` is simple and explicit. A FP16 model with a well-constructed prompt should always satisfy it. More importantly, FORMAT_FAIL items are excluded from all downstream gate computations (Gates 2–5 use FORMAT_PASS as their denominator). If FORMAT_FAIL items appear at FP16, the effective n shrinks below 24, making the integer ceilings calibrated at n=24 technically misapplied. The cleanest resolution is Gate 1 = 1.000: a FORMAT_FAIL at FP16 means the cell is not stress-eligible and must be redesigned.

A fractional Gate 1 threshold would require recalibrating all n=24 integer ceilings for the smaller FORMAT_PASS subset, adding complexity without interpretive benefit.

**What partial results mean (FORMAT_PASS < 1.000):**
- ≥ 21/24: Branch 2 — format boundary evidence reportable; cell not stress-eligible
- < 21/24: Cell is not interpretable at content level; construction must be revised before any further use

**Alignment with Team Lead provisional:** agree. 1.000 for stress eligibility confirmed.

---

## Authorization note

Revision 2 threshold set was approved by Manager on 2026-06-08. Two open items remain before Stage 1 cell generation is authorized: (1) BPE-Jaccard amendment Manager confirmation; (2) Gate 1 FORMAT_PASS threshold approval. Near-miss Levenshtein k ≤ 2 is approved (Manager, 2026-06-08). No run is authorized by this document.

---

## 1. Gate-2 FP16 pass rate

**Threshold proposed:** per query type, not pooled

```
hop1      ≥ 0.875  (≥ 21/24 at n=24)
hop2      ≥ 0.875  (≥ 21/24 at n=24)
composite ≥ 0.875  (≥ 21/24 at n=24)
```

Gate 2 fails if any required query type falls below 0.875. A failed Gate 2 blocks all downstream gates regardless of other query types. Passing Gate 2 does not mean a threshold on other query types is waived — each query type is evaluated independently.

**Why per-query-type:** The two-hop instrument distinguishes three qualitatively different operations (one-hop lookup, two-hop lookup, chained lookup). Pooling them would allow a composite failure to be masked by high hop1/hop2 scores. The constructibility claim requires each operation to be individually interpretable.

**Why 0.875 and not 0.80:** The prior review explained this. The Exp8A and Exp8B feasibility screens used ≥ 7/8 = 0.875 on a simpler task (single-lookup, 5-fact context). Two-hop is harder; a cell that cannot exceed the single-lookup feasibility threshold has found a ceiling, not a floor. If a cell lands between 0.80 and 0.875 at FP16, the correct action is to redesign the cell, not lower the gate.

**Integer interpretation at n=24:**
- Pass condition: ≥ 21 correct items per query type
- Fail condition: ≤ 20 correct items for any query type

---

## 2. Dummy ceiling (two-condition rule)

**Threshold proposed:** both conditions must be met

```
Condition 1: max_dummy_score ≤ 0.375      (absolute ceiling)
Condition 2: Gate-2 composite − max_dummy_score ≥ 0.40    (minimum margin)
Condition 3: no dummy exceeds chance + 0.05               (chance guard)
```

Where "chance" = uniform_random_expected for the query type (composite: 0.50 for 1-target + 1-decoy cell).

**What counts as a "dummy":** all baselines in `compute_dummy_baseline_scores()` — always_return_B_target, always_return_anchor_A, always_return_first_C, always_return_last_C, always_return_NULL, always_return_C_decoy_{i}. `uniform_random_expected` is a reference value, not a dummy score; it is excluded from the ceiling check.

**Integer interpretation at n=24:**
- Condition 1: max_dummy ≤ 9/24 items
- Condition 2: correct_count − max_dummy_count ≥ 0.40 × 24 = 9.6 → difference ≥ 10 items
- Condition 3: max_dummy ≤ (0.50 + 0.05) × 24 = 13.2 → max_dummy ≤ 13/24 items

**Binding constraint at n=24:** Condition 1 (max_dummy ≤ 9/24) is the most restrictive. Given Gate-2 ≥ 21/24 and Condition 1, Conditions 2 and 3 are automatically satisfied: margin = 21 − 9 = 12 ≥ 10 ✓; 9/24 = 0.375 < 0.55 ✓. All three conditions are retained as documenting constraints, not as independent runtime checks.

**Construction implication:** For a 2-chain cell, the dangerous dummies are always_return_first_C and always_return_last_C. Target C scores 1.0 on always_return_first_C for items where target C has a lower position_index than decoy C, and vice versa. With Condition 1 (max_dummy ≤ 9/24), target C must be "first C in context" for at most 9 items and "last C in context" for at most 9 items. Cell construction must interleave fact ordering so that neither position is systematically favored.

---

## 3. Near-miss Levenshtein k

**Threshold proposed:** k ≤ 2

**IMPORTANT: Manager approval required before this threshold is used in any run or construction constraint.** Levenshtein k is the only threshold in this proposal requiring separate Manager approval.

**Flag meaning:**
- *Construction audit (Gate 0.5):* The declared `target_neighbor_decoy` must satisfy `char_edit_distance(token, C_target) ≤ 2`. Tokens with distance > 2 are not near-misses by this criterion and must be replaced with a closer decoy.
- *Accidental near-miss screen:* Any non-target-neighbor-decoy token pair with `char_edit_distance ≤ 2` is flagged as a construction concern. If found, the relevant tokens must be reviewed and replaced before cell validation passes Gate 0.5.

**Rationale:** The token pool uses 5-character uppercase identifiers. Distance 1 = one substituted character (e.g., CPQVX → CPQWX). Distance 2 = two substitutions. Distance 3 covers more than half the characters of a 5-char token, making the pair too similar to serve as a clean near-miss. Distance 0 is trivially excluded (same token).

---

## 4. BPE-Jaccard j

**Threshold proposed:** j ≥ 0.50, pending tokenizer-specific empirical inspection under the production tokenizer.

**Blocking clarification:** Stage 0 was correctly scoped to offline schema and scorer validation; no tokenizer was called and no tokenizer hash was locked at Stage 0. This is not a Stage 0 gap. The blocking is that the proposed value j = 0.50 was derived from first principles and has not been empirically validated against actual BPE segmentations for this token pool. Before j = 0.50 is used as a construction constraint, the production tokenizer must be locked (tokenizer_hash recorded) and at least a sample of token-pool pairs must be inspected to verify the threshold places the boundary where intended.

**What remains pending:** (1) tokenizer lock (tokenizer_hash populated in run provenance); (2) segmentation inspection for representative token pairs including at least one 1-edit pair (e.g., CPQVX / CPQWX) and one 2-edit pair; (3) confirmation that j = 0.50 correctly separates near-miss from non-near-miss at the BPE level.

---

## 5. Trigram-Jaccard j

**Threshold proposed:** j ≥ 0.20

**Usage:** same dual-application as Levenshtein k. Confirmatory (declared near-miss pair must show j ≥ 0.20) and protective (non-intended pairs with j ≥ 0.20 are flagged as construction concerns).

**Calibration:** CPQVX / CPQWX (1-edit pair) produces j = 0.20 (trigrams: {CPQ,PQV,QVX} vs {CPQ,PQW,QWX}; intersection = {CPQ}; union = 5; 1/5 = 0.20). This is the natural calibration point for a 5-char token pool and is retained from the original proposal.

---

## 6. Length-matched tolerance

**Threshold proposed:** ± 10 prompt tokens

**Measurement basis:** prompt tokens as rendered under the locked tokenizer. The tolerance applies to the total rendered prompt token count, not to the context block alone.

**Rationale:** Smoke test item has total_token_count = 80. ± 10 is ~12.5% of context size. This is wide enough to accommodate single-fact variation in token count without requiring exact replication, and tight enough to prevent controls that are substantially shorter or longer than the target prompt.

**Scaling note for review:** For cells with total_token_count > 150, a flat ±10 tolerance may be insufficient (< 7% of total). Team Lead may wish to specify a scaling rule (e.g., ± 8% of total prompt token count) for larger cells. The flat ±10 is the primary proposal for standard cells of the current size.

---

## 7. Unique-assignment reliability

**Threshold proposed:** deterministic unique assignment = 1.000 for all parseable, in-taxonomy outputs

**Clarification:** This is a property of the scorer design, not a runtime-measured threshold. `classify_output()` is deterministic and always assigns exactly one of the 8 failure classes to any FORMAT_PASS output. UNCLASSIFIED_OFF_FRAME is the catch-all class that handles outputs not matching any prior condition. Therefore, unique_assignment_rate = 1.000 is guaranteed by the locked scorer for all FORMAT_PASS items.

If unique assignment < 1.000 for a FORMAT_PASS item, that indicates a scorer implementation error, not a gate condition. It must be investigated and resolved before any run results are reported.

**Operational implication:** This threshold requires no runtime gate check. The relevant gate check is the UNCLASSIFIED ceiling (threshold 8).

---

## 8. UNCLASSIFIED / OFF-FRAME ceiling

**Threshold proposed:** UNCLASSIFIED_OFF_FRAME rate ≤ 0.05

**Gate meaning:** Gate 4a. If UNCLASSIFIED rate > 0.05, the failure taxonomy is incomplete for this cell and the run is not fully interpretable.

**Watch condition:** UNCLASSIFIED rate > 0.02 (not a gate fail) triggers mandatory manual inspection and clustering assessment. Unclassified outputs must be described in Watch Conditions section of Run Summary. If a coherent cluster is identified, it is a taxonomy-expansion candidate and requires a new Team Lead review cycle and `scorer_twohop_l1.py` amendment (hash change, TL approval required).

**Integer interpretation at n=24, composite query type:**
- Gate fail: ≥ 2 UNCLASSIFIED outputs (2/24 = 0.083 > 0.05)
- Gate pass with watch condition: exactly 1 UNCLASSIFIED output (1/24 = 0.042 > 0.02)
- Gate pass, no watch condition: 0 UNCLASSIFIED outputs

---

## 9. Gate-3 operation-fidelity ceilings (composite query only)

**Denominator for all five rates:**

```
denominator = count of composite items with FORMAT_PASS
```

Do not use all items (inflates denominator with FORMAT_FAIL items). Do not use failures-only (converts rates to conditional probabilities, unsuitable for gates). Failure-share metrics may be reported in Watch Conditions as diagnostics only.

**Failure class mapping:**

| Gate-3 metric | Source | Numerator |
|---|---|---|
| stopped_short_rate | scorer | failure_class = `correct_chain_stopped_short` |
| shortcut_single_hop_rate | validator flags (see § 9a below) | composite items: is_correct = True AND validator flags shortcut |
| wrong_chain_rate | scorer | failure_class = `wrong_chain_selection` |
| wrong_neighbor_rate | scorer | failure_class = `target_chain_wrong_neighbor` |
| anchor_echo_rate | scorer | failure_class = `anchor_echo` |

**Gate-3 pass condition:** all five rates simultaneously below their ceilings.

---

### 9a. shortcut_single_hop_rate — definition and implementation

**Definition (Team Lead, 2026-06-07):**

```
shortcut_single_hop_rate =
  count(composite items: FORMAT_PASS AND is_correct = True
        AND validator_flags shortcut as single-hop-sufficient)
/ count(composite items: FORMAT_PASS)
```

A composite item is flagged as shortcut if any of the following apply:

```
1. Expected C can be inferred from A alone under the rendered question/context.
2. Expected C can be inferred from one visible edge without using B.
3. Validator identifies a direct A→C shortcut or answer leak.
4. C is uniquely recoverable by surface role, position, or wording without traversal.
5. A control or dummy baseline demonstrates recovery above the dummy ceiling
   without requiring the two-hop structure.
```

This is a construction-validity failure. Do not use for ordinary wrong outputs; those are classified by the scorer.

**Implementation note (not a request for amendment):**

The existing `validate_positive_sufficiency()` in the locked `tasks_twohop_l1.py` already catches structural shortcut conditions by rejecting items where `answer_from_hop1_alone_possible = True`, `answer_from_hop2_alone_possible = True`, or `composite_answer == hop1_answer`. Any item passing full validation should have no structural shortcut path.

Team Lead conditions 4 and 5 (surface role/position recovery, dummy policy recovery) are checked at cell construction time by the dummy ceiling test and manifest inspection, not per-output by the scorer.

**Operational consequence:** For a cell passing full manifest validation, shortcut_single_hop_rate should be 0 by construction. The ceiling ≤ 0.10 (≤ 2/24) is a belt-and-suspenders guard. If a validated cell produces a non-zero rate, this indicates a validator gap and must be investigated before stress.

**Runner responsibility:** The runner script must check each composite item's `positive_sufficiency_exclusion` block for shortcut flags before recording a correct composite output as a clean pass. If `answer_from_hop1_alone_possible = True` or equivalent, the item should be counted in the shortcut numerator, not as clean evidence.

---

### 9b. Proposed ceilings

**Fraction form:**

```
stopped_short_rate       ≤ 0.15
shortcut_single_hop_rate ≤ 0.10
wrong_chain_rate         ≤ 3/24 (see recommendation below)
wrong_neighbor_rate      ≤ 0.15
anchor_echo_rate         ≤ 0.15
```

**Integer interpretation at n=24 composite FORMAT_PASS items:**

| Metric | Fraction ceiling | At n=24 | Integer ceiling | Why integer ≠ fraction × 24 |
|---|---|---|---|---|
| stopped_short | ≤ 0.15 | ≤ 3.6 | ≤ 3/24 | 4/24 = 0.167 > 0.15 → 4 items fails |
| shortcut_single_hop | ≤ 0.10 | ≤ 2.4 | ≤ 2/24 | 3/24 = 0.125 > 0.10 → 3 items fails |
| wrong_chain | ≤ 3/24 | ≤ 3 | ≤ 3/24 | exact integer specification |
| wrong_neighbor | ≤ 0.15 | ≤ 3.6 | ≤ 3/24 | 4/24 = 0.167 > 0.15 → 4 items fails |
| anchor_echo | ≤ 0.15 | ≤ 3.6 | ≤ 3/24 | 4/24 = 0.167 > 0.15 → 4 items fails |

**Wrong-chain rate recommendation:**

Reviewer positions at n=24:

```
Senior Engineer:  ≤ 0.10 = ≤ 2/24
Contributor 1:    ≤ 0.15 = ≤ 3/24
Team Lead prov.:  ≤ 3/24
CS Engineer:      ≤ 0.20 = ≤ 4/24 (prior proposal, revised)
```

**CS recommendation: ≤ 3/24**, aligned with Team Lead provisional and Contributor 1.

Justification in item-count terms at n=24:

- 3/24 allows 3 items to select the decoy chain at FP16. In a well-constructed cell, 3 decoy-chain selections at FP16 indicates the decoy is moderately attractive — a real observation, not a noise artifact. This is acceptable as a starting baseline.
- 3/24 is tight enough to detect a meaningful increase under stress: an increase from 3 to 6+ wrong-chain items at INT4 (doubling) is statistically notable at n=24 and clearly interpretable.
- 2/24 (Senior) risks rejecting valid cells on the basis of 1–2 items where the decoy is genuinely confusable at FP16. Since the purpose of Track B is to measure whether quantization increases this rate, an FP16 cell with 2–3 wrong-chain items is exactly the type of cell where the measurement is interesting. Blocking it at 2/24 could filter out the most informative cells.
- 4/24 (original CS proposal) is too permissive for a constructibility floor claim: 4/24 = 16.7% of composite items selecting the decoy at FP16 is more noise than signal.

**Note on wrong-chain watch condition:** A wrong_chain_rate in the range 2–3/24 at FP16 should be flagged in Watch Conditions even when below the ceiling. A cell that passes at exactly 3/24 wrong-chain is at the limit; stress results must be interpreted with additional care.

---

## 10. Threshold summary table

Approval status codes: **LOCKED** = Manager-approved 2026-06-08; **TL-REC** = Team Lead recommended, Manager confirmation pending; **PROPOSED** = CS proposal, TL + Manager approval required.

| # | Gate | Threshold | Value | Status |
|---|---|---|---|---|
| G1 | Gate 1 | FORMAT_PASS rate per query type | 1.000 | LOCKED 2026-06-08 |
| G2a | Gate 2 | FP16 hop1 pass rate | ≥ 21/24 | LOCKED 2026-06-08 |
| G2b | Gate 2 | FP16 hop2 pass rate | ≥ 21/24 | LOCKED 2026-06-08 |
| G2c | Gate 2 | FP16 composite pass rate | ≥ 21/24 | LOCKED 2026-06-08 |
| G2d | Gate 5 / dummy | Dummy absolute ceiling | max_dummy ≤ 9/24 | LOCKED 2026-06-08 |
| G2e | Gate 5 / dummy | Dummy margin | Gate-2 composite − max_dummy ≥ 10 items | LOCKED 2026-06-08 |
| G2f | Gate 5 / dummy | Dummy chance guard | no dummy > chance + 0.05 | LOCKED 2026-06-08 |
| G3 | Gate 0.5 | Near-miss Levenshtein k | k ≤ 2 | LOCKED 2026-06-08 |
| G4 | Gate 0.5 | BPE-Jaccard j | j ≥ 0.40 (amended from 0.50) | LOCKED 2026-06-08 |
| G5 | Gate 0.5 | Trigram-Jaccard j | j ≥ 0.20 | LOCKED 2026-06-08 |
| G6 | Gate 5 | Length-matched tolerance | ± 10 prompt tokens | LOCKED 2026-06-08 |
| G7 | Gate 4a | Unique-assignment reliability | 1.000 (scorer guarantee) | LOCKED 2026-06-08 |
| G8 | Gate 4a | UNCLASSIFIED ceiling | ≤ 0.05 | LOCKED 2026-06-08 |
| G8w | Gate 4a | UNCLASSIFIED watch trigger | > 0.02 triggers inspection | LOCKED 2026-06-08 |
| G9a | Gate 3 | stopped_short ceiling | ≤ 3/24 | LOCKED 2026-06-08 |
| G9b | Gate 3 | shortcut_single_hop ceiling | ≤ 2/24 (structural guarantee; see §9a) | LOCKED 2026-06-08 |
| G9c | Gate 3 | wrong_chain ceiling | ≤ 3/24 | LOCKED 2026-06-08 |
| G9d | Gate 3 | wrong_neighbor ceiling | ≤ 3/24 | LOCKED 2026-06-08 |
| G9e | Gate 3 | anchor_echo ceiling | ≤ 3/24 | LOCKED 2026-06-08 |

---

## 11. Open items status (as of 2026-06-08)

All threshold items are now resolved. No threshold blockers remain for Stage 1.

| Item | Status | Resolved by |
|---|---|---|
| BPE-Jaccard j ≥ 0.40 amendment | **LOCKED** | Manager, 2026-06-08 |
| Gate 1 FORMAT_PASS = 1.000 | **LOCKED** | Manager, 2026-06-08 |
| shortcut_single_hop validator flag | **CLOSED** — no amendment required | Manager confirmation, 2026-06-08 |
| Near-miss Levenshtein k ≤ 2 | **LOCKED** | Manager, 2026-06-08 |
| Full Revision 2 threshold set | **LOCKED** | Manager, 2026-06-08 |
| Wrong-chain ceiling ≤ 3/24 | **LOCKED** | Manager, 2026-06-08 |
| BPE-Jaccard inspection timing | **COMPLETED** | Inspection performed 2026-06-08 |

**Remaining pre-execution actions (not threshold items — require separate authorization):**
- Cell generation authorization (Manager decision)
- Runner script construction and lock (CS, once cell generation authorized)
- Prompt template construction and lock (CS, once cell generation authorized)
- FP16 model tokenizer hash confirmation (CS, at download time)

---

## 12. Authorization boundary

```
Revision 2 threshold set: FULLY LOCKED — Manager, 2026-06-08.
All thresholds approved. No threshold blockers remain.

Stage 1 Run Memo: submitted for Team Lead final review.
Stage 1 execution requires separate Manager authorization.

Regardless of threshold lock, the following are NOT authorized:
  cell generation
  model inference
  Stage 1 execution
  confirmation pass
  7B pass
  INT8 / INT4 stress
  Track B
```

---

## 13. Files

```
THRESHOLD-PROPOSAL-TWOHOP-L1.md         this document (revision 2 — APPROVED 2026-06-08; 2 items pending)
THRESHOLD-REVIEW-TWOHOP-L1.md           CS Engineer review response, 2026-06-07
BPE-JACCARD-INSPECTION-TWOHOP-L1.md     tokenizer inspection, 2026-06-08
STAGE1-RUN-MEMO-TWOHOP-L1.md            Stage 1 Run Memo draft
STAGE0-INSTRUMENT-LOCK-PACKET.md        Stage 0 closure packet
CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md  canonical gate ladder, claim structure
scorer_twohop_l1.py                     sha256:6921e58059e3ef4806c1ae75f73a9670f4a02962bff2eb27fd2da77bad82c473
tasks_twohop_l1.py                      sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
```

— CS Engineer
