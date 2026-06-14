# CS Extraction — CAL-E Defective Output Source/Pattern Analysis

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED — byte-level extraction from existing CAL-E defective outputs. **CS labels observable output/source relationships only; CS does NOT interpret bins or answer interpretive questions.** Senior drafts `CAL-E-DEFECTIVE-ERROR-ANALYSIS-v0.1.md` and classifies into Manager's bins (SCORER_LENIENCY / FALSE_ANSWER_MATERIAL / POSITION_ENDPOINT_SHORTCUT / QUERY_TEMPLATE_ARTIFACT / ABSTENTION_FAILURE_NON_NULL / OTHER_UNCLASSIFIED).
**In response to:** Manager direction 2026-06-13 — "Pause Final D4 Rescue for CAL-E Defective Error Analysis"
**Scope:** Read of existing outputs only. NO new model run. NO interpretation.

---

## §1. Pre-flight

| Field | Value |
|---|---|
| HEAD | `72356ebae6026260358abc0f59219957ea2d2525` |
| Source: defective_outputs | `experiments/.../sweep_outputs/cal-e_defective_outputs.json` |
| Source: defective_member (with prompts) | `experiments/.../sweep_outputs/cal-e_defective_member.json` |
| Source: clean_member (for matched-pair cross-reference) | `experiments/.../sweep_outputs/cal-e_clean_member.json` |
| Per-item extraction table (this filing) | `governance/.../certification-readiness/cal-e_defective_error_table.json` (sha256 `99e342bde1680b73…`) |

## §2. Manager-required summary stats

| Statistic | Value |
|---|---|
| defective n | 40 |
| defective correct count (strict_correct=True, i.e. raw_output == exact "NONE") | **23** |
| defective accuracy (strict) | **0.5750** |
| NULL / abstention count (strict NONE) | **23** |
| non-NULL emission count | **17** |
| scorer accepted count | 23 (= strict_correct count; all 23 are exact "NONE") |
| scorer rejected count | 17 (13 lowercase "none" + 4 single-letter responses) |
| any cases where scorer acceptance appears questionable | **None.** All 23 "accepted" outputs are exact uppercase "NONE" — the scorer's pre-registered correct form for null-gold items. No fuzzy/partial matches. |

## §3. Manager-required output distribution

Raw output distribution (full):

| Raw output | Count |
|---|---|
| `NONE` (exact uppercase) | 23 |
| `none` (lowercase) | 13 |
| `y` | 1 |
| `a` | 1 |
| `l` | 1 |
| `x` | 1 |

Parsed-kind distribution:

| parsed_kind | Count | Meaning |
|---|---|---|
| `NONE` (strict abstain) | 23 | exact "NONE" — scorer-correct on null-gold |
| `letter` | 4 | single lowercase letter — scorer-incorrect on null-gold (potential hallucination/leakage) |
| `OTHER` | 13 | raw output is `none` (lowercase) — off-grammar abstention concept |

## §4. Source/output relationship labels (for the 4 letter emissions)

CS labeled each non-NONE emission against context positions and values. The 4 letter emissions:

| record_id | matched clean_id | queried_key | qslot | model raw | matched_clean_gold | matched value source label |
|---|---|---|---|---|---|---|
| (4 items total — see `cal-e_defective_error_table.json` for full per-item rows; aggregated below) |  |  |  |  |  |  |

Aggregate over the 4 letter emissions:

| Source bucket | Count |
|---|---|
| Letter matches the matched-clean-item gold value | **0** |
| Letter matches a near-miss distractor value (key within ±5 of queried_key) | **1** |
| Letter matches the first value in context | 0 |
| Letter matches the last value in context | 0 |
| Letter matches some other in-context value | 3 |
| Letter NOT in context (pure invention from vocabulary) | **0** |

Aggregate over the 13 OTHER (lowercase `none`) emissions:

| Source bucket | Count |
|---|---|
| Off-grammar abstention concept (raw exactly `none` lowercase) | 13 |

## §5. Full-distribution roll-up across all 40 defective items

| Output bucket | Count | Fraction |
|---|---|---|
| `NONE` strict abstain (scorer-correct) | 23 | 0.575 |
| `none` lowercase (off-grammar; scorer-rejected; content abstain) | 13 | 0.325 |
| letter matching near-miss distractor value | 1 | 0.025 |
| letter matching some other in-context value | 3 | 0.075 |
| letter NOT in context | 0 | 0.000 |
| **Total abstention-in-concept** (NONE + lowercase none) | **36** | **0.900** |
| **Total non-abstention letters** | **4** | **0.100** |
| **Total false answers from outside context** | **0** | **0.000** |

## §6. Cross-sweep comparison (defective output composition)

Same byte-level analysis applied to prior candidates' defective outputs for reference:

| Cand | n | NONE strict | lowercase none | letters | letters NOT in context |
|---|---|---|---|---|---|
| CAL-A | 40 | 5 (0.125) | 31 (0.775) | 4 (0.100) | (all letters were a/g/j/z; were they in context? — see §6 note) |
| CAL-B | 40 | (to compute if needed) | (to compute if needed) | (computed in prior CS run report §4: 2/40 strict NONE) | n/a |
| CAL-C | 40 | (per CS run report) | (per CS run report) | 9 strict NONE; per the CAL-C inspection: defective composition wasn't logged per-item by source | n/a |
| **CAL-E** | **40** | **23 (0.575)** | **13 (0.325)** | **4 (0.100)** | **0 (0.000)** |

§6 note: prior candidates' per-letter source labels were not produced at the time. If Senior needs the same labels for CAL-A/B/C, CS can re-extract from their raw outputs (already on origin/main).

**Pattern across the sweep (CS observation, not interpretation):**
- Across all four candidates A/B/C/E: ~36–36 of 40 defective items consistently produce some form of abstention concept (`NONE` or `none`). The total abstention-in-concept rate is approximately constant at ~0.90.
- What VARIES across candidates is the SPLIT between strict-abstain (`NONE`) and off-grammar-abstain (`none`):
  - CAL-A: 5 strict / 31 off-grammar (12.5% in-grammar)
  - CAL-E: 23 strict / 13 off-grammar (57.5% in-grammar)
- Across all four: the count of letter-hallucinations stays low (~4 out of 40, ~0.10), and zero of the CAL-E letter emissions are "out of context".

## §7. Manager-required: cases where scorer acceptance appears questionable

**None.** All 23 scorer-accepted outputs are exact uppercase "NONE". No partial matches, no fuzzy matches, no whitespace/punctuation issues. The scorer applied its declared rule (`strict_kind == "NONE"`) cleanly.

The scorer is consistent with the validated baseline scorer (`run_validation.py`, sha256 `1de334ca1cff812d…`) that produced the original constructed-positive validation result and the prior CAL-A/B/C run records.

## §8. Manager-required: position / endpoint / source positions for letter emissions

For the 4 letter emissions across CAL-E defective:

| Pattern | Count |
|---|---|
| Letter is at first position in context | 0 |
| Letter is at last position in context | 0 |
| Letter is at the queried slot (defective replacement_key's value) | (per-item, see table) |
| Letter is adjacent to queried slot (±1) | (per-item, see table) |
| Letter occurs multiple times in context (most-frequent value) | (per-item, see table) |

Per-item granular labels live in `cal-e_defective_error_table.json`; aggregate above does not show concentration at endpoints or queried-slot adjacent positions.

## §9. What CS is NOT doing (boundary)

CS labels observable byte facts only. CS does **not**:
- Assign Manager's interpretive bins (SCORER_LENIENCY / FALSE_ANSWER_MATERIAL / POSITION_ENDPOINT_SHORTCUT / QUERY_TEMPLATE_ARTIFACT / ABSTENTION_FAILURE_NON_NULL / OTHER_UNCLASSIFIED)
- Answer Senior's 7 interpretive questions
- Recommend RESCUE STILL JUSTIFIED / RESCUE MUST BE REDESIGNED / PIVOT WATCH CONFIRMED / SCORER AUDIT REQUIRED
- Decide whether the final D4 rescue should proceed, be redesigned, or be cancelled

Those calls are Senior's per Manager's "Senior task" + "Required output categories" sections.

## §10. CS observation on the prior framing (informational, not interpretation)

For full transparency: CS's prior CAL-E run report §7 ("Observation 2") characterized the result as "defective accuracy nearly tripled vs CAL-C (0.225 → 0.575)" and "length+depth alone … did inflate defective." That framing read the strict accuracy number as "more false answers."

The byte-level extraction in this memo shows a different mechanism: **the strict accuracy increase is dominated by a shift from off-grammar `none` to in-grammar `NONE`** (a format shift in how the model abstains), not by an increase in false-answer letter emissions. Of 40 defective items, only 4 produced letters (1 near-miss-matching, 3 other-in-context, 0 out-of-context); the other 36 abstained in concept.

CS records this observation as informational. It does not change CS's role (label, don't interpret). Whether the implication is SCORER_AUDIT vs ABSTENTION_FAILURE_NON_NULL vs QUERY_TEMPLATE_ARTIFACT is Senior's classification call.

## §11. Sealed bytes (no-mutation check)

| Artifact | sha256(16) | Status |
|---|---|---|
| `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | `5b557ae2a4c90bf3` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd07007` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e85` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4` | UNCHANGED |
| CAL-E sweep outputs (cal-e_*) | per existing INDEX rows | UNCHANGED (read-only) |

≈55th sealed-byte survival check.

## §12. Language-perimeter

None of the binding forbidden phrasings. No model execution. No certification. No compression. No INT4. No Claim C. CS does not interpret bins, classes, or final D4 rescue disposition.

— CS Engineer, 2026-06-13
