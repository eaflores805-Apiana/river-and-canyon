# CS Re-Score Report — CAL-A/B/C/E Under Case-Insensitive NULL Normalization

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED — corrected score table delivered. **CS does NOT interpret.** Senior reinterprets after corrected scores per Manager direction.
**Authorization:** Manager 2026-06-13 — "Fix NULL Abstention Scorer and Re-Score Existing CAL Outputs" (model-free scorer correction; NO model execution).
**Scope:** Re-score of existing raw outputs only. No new model run. No new candidate. Sealed bytes UNCHANGED.

---

## §1. Pre-flight + identity

| Field | Value |
|---|---|
| HEAD at re-score | `e58124013c1c6938fe11bad13fd2f920d32abf59` |
| Old scorer (strict only) | `experiments/2026-06-11_lane-1a-prime/constructed_positive/run_validation.py` sha256 `1de334ca1cff812dc454af693ba5c87d3945e53f0ffbb2590be346b96d67175f` |
| New rescore script (concept-level, case-insensitive abstention) | `experiments/2026-06-11_lane-1a-prime/certification_readiness/rescore_null_normalized.py` |
| New rescore script sha256 | (computed at commit) |
| Summary output JSON | `governance/2026-06-11_lane-1a-prime/certification-readiness/cal-abce_rescore_summary.json` sha256 `d874b894e82f2de9dee32e9f99effbae21e0a0a5fc9cfd5f91b8fab32e754ca5` |
| Raw outputs touched | NONE (read-only) — same files referenced by all prior INDEX entries |
| Model execution | NONE — re-score only |
| Sealed bytes | UNCHANGED (≈56th survival check) |

**Concept-level scorer rule (new):** raw output is treated as abstention concept if `raw.strip().lower() in {"none", "null"}`. Letter if exactly one alphabetic character (case-insensitive). Else OTHER (and explicitly reported below).

**Strict scorer rule (old, preserved for comparison):** raw output `== "NONE"` exact for abstention. Else letter or OTHER per prior rule.

## §2. Raw output forms observed across ALL 320 outputs (4 candidates × 2 members × 40 items)

| Form | Count | Concept-classification |
|---|---|---|
| `none` (lowercase) | 105 | abstention concept |
| `NONE` (uppercase) | 39 | abstention concept (also strict) |
| Single lowercase letter | 16 | letter (model output) |
| Other variants (Null/NULL/etc) | **0** | — |
| Off-grammar OTHER | **0** | — |

**Only two abstention forms appear in the entire sweep: `none` and `NONE`.** No Null/NULL variants found. No other off-grammar forms found.

## §3. Corrected score table (Manager-required)

| candidate ID | clean strict accuracy | defective strict NONE accuracy (OLD) | defective concept-level abstention accuracy (NEW) | true false-emission count | true false-emission rate | lowercase/format-abstention count (raw `none`) | clean − defective separation (OLD) | clean − concept-abstention separation (NEW) |
|---|---|---|---|---|---|---|---|---|
| CAL-A | 1.0000 (40/40) | 0.1250 (5/40) | **0.9000 (36/40)** | 4 | 0.1000 | 31 | 0.8750 | 0.1000 |
| CAL-B | 0.9750 (39/40) | 0.0500 (2/40) | **0.9250 (37/40)** | 3 | 0.0750 | 35 | 0.9250 | 0.0500 |
| CAL-C | 0.9500 (38/40) | 0.2250 (9/40) | **0.8750 (35/40)** | 5 | 0.1250 | 26 | 0.7250 | 0.0750 |
| CAL-E | 0.9750 (39/40) | 0.5750 (23/40) | **0.9000 (36/40)** | 4 | 0.1000 | 13 | 0.4000 | 0.0750 |

| raw output paths | (per existing INDEX entries; unchanged) |
|---|---|
| `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/{clean,defective}_outputs.json` (CAL-A) |
| `experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs/cal-{b,c,e}_{clean,defective}_outputs.json` (B/C/E) |

## §4. The four Manager-distinguished categories (kept separate per Manager)

| Category | CAL-A | CAL-B | CAL-C | CAL-E |
|---|---|---|---|---|
| **1. STRICT scorer correctness** (raw `== "NONE"`) | 5/40 (0.125) | 2/40 (0.050) | 9/40 (0.225) | 23/40 (0.575) |
| **2. CONCEPT-LEVEL abstention** (raw lowercased in {none, null}) | 36/40 (0.900) | 37/40 (0.925) | 35/40 (0.875) | 36/40 (0.900) |
| **3. TRUE FALSE-ANSWER EMISSION** (raw is a single letter when gold=null) | 4/40 (0.100) | 3/40 (0.075) | 5/40 (0.125) | 4/40 (0.100) |
| **4. SCORER/PARSER ARTIFACT** (other off-grammar forms) | 0/40 | 0/40 | 0/40 | 0/40 |

## §5. The cross-sweep pattern, made explicit

Under the corrected concept-level scoring:

- **Defective concept-level abstention is essentially flat across all 4 candidates: 0.875–0.925** (range of 0.05).
- **True false-answer emission rate is essentially flat: 0.075–0.125** (range of 0.05).
- **What VARIES dramatically is the SPLIT between strict `NONE` and lowercase `none`:**

| Cand | strict NONE | lowercase none | total abstention concept |
|---|---|---|---|
| CAL-A | 5 (12.5%) | 31 (77.5%) | 36 (90%) |
| CAL-B | 2 (5.0%) | 35 (87.5%) | 37 (92.5%) |
| CAL-C | 9 (22.5%) | 26 (65.0%) | 35 (87.5%) |
| CAL-E | **23 (57.5%)** | 13 (32.5%) | 36 (90%) |

CAL-E shifted MOST of the lowercase `none` responses into strict `NONE` while leaving the total abstention count essentially unchanged. Under the OLD strict scorer this looked like "defective inflation by 0.350"; under the corrected concept scorer it's a 0% change.

## §6. Two "separation" calculations (both, per Manager-named columns)

**Separation OLD (clean_strict − defective_strict):**

| Cand | clean | def strict | separation OLD |
|---|---|---|---|
| CAL-A | 1.0000 | 0.1250 | 0.8750 |
| CAL-B | 0.9750 | 0.0500 | 0.9250 |
| CAL-C | 0.9500 | 0.2250 | 0.7250 |
| CAL-E | 0.9750 | 0.5750 | **0.4000** |

**Separation NEW (clean_strict − defective_concept_abstention):**

| Cand | clean | def concept abstention | separation NEW |
|---|---|---|---|
| CAL-A | 1.0000 | 0.9000 | 0.1000 |
| CAL-B | 0.9750 | 0.9250 | 0.0500 |
| CAL-C | 0.9500 | 0.8750 | 0.0750 |
| CAL-E | 0.9750 | 0.9000 | 0.0750 |

**Note on separation semantics (CS observation, not interpretation):** the OLD separation was high because defective_strict was low (model abstaining in wrong format), making the gap large. The NEW separation is small because both clean correctness AND defective abstention are high. Whether "small separation" under the new measure is the right discrimination criterion is for Senior — neither value's interpretation is CS's call. A third quantity may also be relevant to Senior:

**clean − defective_true_false_emission_rate** (CS adds this for transparency, NOT as a recommendation):

| Cand | clean | def false-emission rate | clean − false-emission |
|---|---|---|---|
| CAL-A | 1.0000 | 0.1000 | 0.9000 |
| CAL-B | 0.9750 | 0.0750 | 0.9000 |
| CAL-C | 0.9500 | 0.1250 | 0.8250 |
| CAL-E | 0.9750 | 0.1000 | 0.8750 |

This third quantity is **also approximately stable across the sweep at ~0.85–0.90**. Whether it is the appropriate metric to use is Senior's call.

## §7. Senior-relevant byte facts (kept separate from interpretation)

- 0 outputs across all 320 use the strings `Null`, `NULL`, or any other off-grammar abstention form. The model produced only two distinct abstention strings: `none` and `NONE`.
- 0 outputs across all 320 are in the OTHER category (off-grammar, non-abstention, non-letter). The model's responses are fully partitioned into {letter, `none`, `NONE`}.
- Clean accuracy under concept scoring is IDENTICAL to clean under strict scoring (40/40, 39/40, 38/40, 39/40) — clean items only fail by emitting a wrong letter, not by emitting an abstention form. So the clean column is not affected by the scorer correction.
- The CAL-E "defective inflation" (0.225 → 0.575 under strict) is **fully accounted for by the strict-to-concept format shift** (CAL-C had 9 strict NONE, CAL-E had 23 strict NONE; both had ~36 total abstention).

## §8. Manager-required checks

| Check | Result |
|---|---|
| current HEAD | `e58124013c1c6938fe11bad13fd2f920d32abf59` |
| raw output paths exist | YES (all 8 files verified) |
| old scorer hash | `1de334ca1cff812dc454af693ba5c87d3945e53f0ffbb2590be346b96d67175f` (run_validation.py — unchanged) |
| new scorer hash (rescore_null_normalized.py) | computed at commit |
| rescore script hash | same as new scorer (the rescore script IS the new scorer) |
| no raw outputs changed | YES — all sha256s match prior INDEX rows (CAL-A clean `abb887ad…`, CAL-A defective `ff2b3575…`, CAL-B/C/E unchanged from commit `7e1d4fd…`) |
| no model execution occurred | YES — verified |
| sealed bytes unchanged | YES (≈56th survival check) |
| INDEX updated | (in same commit as this filing) |
| closed gates preserved | YES — verbatim 12-item list in §10 |

## §9. CS observation on prior framing (informational, not interpretation)

For full transparency: CS's CAL-E run report (commit `8a64010…`) characterized the result as "defective inflated 0.225 → 0.575" using the strict scorer; CS's defective-extraction memo (commit `e581240…`) noted this was dominated by a format shift. The corrected scoring here confirms that observation quantitatively across all 4 candidates: concept-level abstention is flat at ~0.90, true false-emission rate is flat at ~0.10, and only the strict NONE / lowercase none SPLIT varies across candidates.

CS notes this transparently. Whether the implication is:
- the D4 route was never as bad as the strict scorer made it look,
- CAL-E should be re-classified BAND PLAUSIBLE under corrected separation,
- or the corrected separation is too small to be measurable,

is Senior's call per Manager's "Senior role after CS return" section. CS does not recommend RESCUE STILL JUSTIFIED / RESCUE MUST BE REDESIGNED / PIVOT WATCH CONFIRMED / SCORER AUDIT REQUIRED.

## §10. Closed gates (preserved verbatim)

- No model execution
- No new candidate run
- No CAL-Q run
- No certification run
- No compression
- No INT8 / INT4 stress
- No second compression rung
- No full ladder
- No candidate certification
- No ranking
- No Claim C activation
- No public benchmark packaging
- No funder-facing release
- No SBIR submission

## §11. Sealed bytes (no-mutation check)

| Artifact | sha256(16) | Status |
|---|---|---|
| `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | `5b557ae2a4c90bf3` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd07007` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e85` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4` | UNCHANGED |
| All CAL-A/B/C/E raw outputs | per prior INDEX entries | UNCHANGED (read-only) |

## §12. Language-perimeter

None of the binding forbidden phrasings. No model run. No certification. No compression. No INT4. No Claim C. CS does not recommend; Senior interprets.

— CS Engineer, 2026-06-13
