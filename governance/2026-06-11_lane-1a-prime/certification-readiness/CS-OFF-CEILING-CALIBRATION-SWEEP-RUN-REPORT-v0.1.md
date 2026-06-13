# CS Run Report — Off-Ceiling Calibration Sweep

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED — sweep executed; bytes returned. **CS does NOT interpret.** Senior runs the pre-registered verdict harness on the returned bytes.
**Authorization:** Manager 2026-06-13 "Run Off-Ceiling Calibration Sweep" + Manager direction "CS Execute Off-Ceiling Calibration Sweep" (filed at `MANAGER-OFF-CEILING-CALIBRATION-SWEEP-AUTHORIZATION-2026-06-13.md`).
**Scope:** Calibration only. Not certification, not compression, not retention, not Claim C, not ranking.

---

## §1. Pre-flight attestations (Manager-required)

| Field | Value |
|---|---|
| HEAD at run time | `d2014e5ce4932ac057cc80db875e844cf54ca398` (`origin/main`) |
| Sweep SPEC path | `governance/2026-06-11_lane-1a-prime/certification-readiness/OFF-CEILING-CALIBRATION-SWEEP-SPEC-v0.1.md` |
| Sweep SPEC sha256 | `18ac212fbc45e3d45d94fdfb21e507c081c21b38dd87fb3d34f2d7682f8049a0` |
| RUNSPEC path | `governance/2026-06-11_lane-1a-prime/certification-readiness/OFF-CEILING-CALIBRATION-SWEEP-RUNSPEC-v0.1.md` |
| RUNSPEC sha256 | `84ad4008f3e7900d635b3207d22895eee922584e1e858d2edaed7d13358dcae6` |
| Pre-registered harness | `experiments/2026-06-11_lane-1a-prime/certification_readiness/calibration_sweep_verdict.py` (sha256 `b5775c374669558f0eb844df2132a7dcc498963b00e0f1a0a96aa41b1f45792f`) |
| prompt_template sha256 | `f1956e7dd43f165c8707fe88bc11757888f108e7e9766aa186ac9fc04f8b368a` (same as validated baseline) |
| decoding_config sha256 | `a20391d89972d47c0b231f5c6da9f8a9f4c7be8c975ab98bd95a32327196f803` (same as validated baseline) |
| scorer (run_validation.py reused) sha256 | `1de334ca1cff812dc454af693ba5c87d3945e53f0ffbb2590be346b96d67175f` |
| Sweep runner | `experiments/2026-06-11_lane-1a-prime/certification_readiness/run_calibration_sweep.py` |
| Model ID | `Qwen/Qwen2.5-3B-Instruct` (validated baseline; FP16/native via mlx_lm 0.31.3) |
| Decoding | greedy, temp=0.0, max_new_tokens=32 |
| Route-state attestation | **GREEN — for THIS calibration step only** (Manager-authorized, narrow purpose; RED for everything in §4) |
| Closed-gate list preserved | YES — verbatim 13-item list in §4 below |
| Dropped candidates | CAL-D NOT CONSTRUCTED this run (optional per spec; not authorized as default; would require single-difference design re-check if requested) |

## §2. Candidate matrix executed

| Cand | List len | Slot range | Near-miss | Source | n | single_difference_ok |
|---|---|---|---|---|---|---|
| CAL-A | 9 | 6–8 | 0 (baseline) | **reused** existing constructed-positive bytes (`f412d04c…` / `4ea3c277…` / `49cd6451…`) | 40 | YES (per original manifest's distribution-level PASS; see §6 note) |
| CAL-B | 13 | 8–11 | 2 | **constructed fresh** (seed `20260613001`) | 40 | YES (per-item-strict + distribution) |
| CAL-C | 17 | 10–15 | 4 | **constructed fresh** (seed `20260613002`) | 40 | YES (per-item-strict + distribution) |
| CAL-D | — | — | — | NOT RUN | — | n/a |

## §3. Raw results per candidate (Manager-required output format)

### CAL-A — control (expected SATURATION; reproduces validated baseline)

| Field | Value |
|---|---|
| candidate_id | CAL-A |
| list_len | 9 |
| queried slot range | 6–8 |
| distractor structure | baseline (no near-miss) |
| single_difference_ok | TRUE (per original manifest's distribution-level PASS) |
| clean accuracy | **1.0000** (40/40) |
| defective accuracy | 0.1250 (5/40) |
| n | 40 each |
| shortcut-floor comparison | clean 1.0000 >> 0.6125+m for any m≥0 — well above floor |
| ceiling comparison | clean 1.0000 = ceiling — AT CEILING (no headroom) |
| raw clean outputs | `experiments/.../certification_readiness/sweep_outputs/cal-a_clean_outputs.json` (sha256 below) |
| raw defective outputs | `experiments/.../certification_readiness/sweep_outputs/cal-a_defective_outputs.json` (sha256 below) |
| manifest path | `experiments/2026-06-11_lane-1a-prime/constructed_positive/realized_match_manifest.json` (sha256 `49cd64510fc8f9e3…`) |
| scorer path | `experiments/2026-06-11_lane-1a-prime/constructed_positive/run_validation.py` (sha256 `1de334ca1cff812d…`) |
| run record JSON | `governance/2026-06-11_lane-1a-prime/certification-readiness/sweep_run_records/cal-a_run.json` (sha256 `5ceeeea467442082…`) |
| notes | Reproduces the known validated 1.0 baseline. Control sanity check: PASS. |

### CAL-B — moderate off-ceiling pressure

| Field | Value |
|---|---|
| candidate_id | CAL-B |
| list_len | 13 |
| queried slot range | 8–11 |
| distractor structure | baseline + 2 near-miss keys (within ±5 of queried key) |
| single_difference_ok | TRUE (per-item-strict + distribution) |
| clean accuracy | **0.9750** (39/40) |
| defective accuracy | 0.0500 (2/40) |
| n | 40 each |
| shortcut-floor comparison | clean 0.9750 >> 0.6125+m for any m<0.35 — well above floor |
| ceiling comparison | clean 0.9750 < 1.0 — **OFF CEILING** (by 0.025; first off-ceiling clean data point in the record) |
| raw clean outputs | `experiments/.../sweep_outputs/cal-b_clean_outputs.json` |
| raw defective outputs | `experiments/.../sweep_outputs/cal-b_defective_outputs.json` |
| manifest path | `experiments/.../sweep_outputs/cal-b_realized_match_manifest.json` |
| scorer path | `experiments/2026-06-11_lane-1a-prime/constructed_positive/run_validation.py` |
| run record JSON | `governance/.../sweep_run_records/cal-b_run.json` (sha256 `814676cc7775b4b2…`) |
| notes | First setting that escaped saturation. Defective collapse (2/40) indicates the gate is firing on the defect strongly. |

### CAL-C — stronger off-ceiling pressure

| Field | Value |
|---|---|
| candidate_id | CAL-C |
| list_len | 17 |
| queried slot range | 10–15 |
| distractor structure | baseline + 4 near-miss keys |
| single_difference_ok | TRUE (per-item-strict + distribution) |
| clean accuracy | **0.9500** (38/40) |
| defective accuracy | 0.2250 (9/40) |
| n | 40 each |
| shortcut-floor comparison | clean 0.9500 >> 0.6125+m for any m<0.33 — well above floor |
| ceiling comparison | clean 0.9500 < 1.0 — **OFF CEILING** (by 0.050; deeper off-ceiling than CAL-B) |
| raw clean outputs | `experiments/.../sweep_outputs/cal-c_clean_outputs.json` |
| raw defective outputs | `experiments/.../sweep_outputs/cal-c_defective_outputs.json` |
| manifest path | `experiments/.../sweep_outputs/cal-c_realized_match_manifest.json` |
| scorer path | `experiments/2026-06-11_lane-1a-prime/constructed_positive/run_validation.py` |
| run record JSON | `governance/.../sweep_run_records/cal-c_run.json` (sha256 `50964a77cf646e8e…`) |
| notes | Stronger pressure pushed deeper off ceiling. Defective higher than CAL-B (0.225 vs 0.05) — more distractor near-miss may be confusing the defect-detection path; Senior to interpret. |

### Run output file hashes (governance side)

| Run record | sha256 (full) |
|---|---|
| `cal-a_run.json` | `5ceeeea4674420823fd2e912ed9fe04f6330e798370f202c2e16760e930fbba6` |
| `cal-b_run.json` | `814676cc7775b4b26ce1a898e91caa06fa7940e85819be54cdebcbbe83da241a` |
| `cal-c_run.json` | `50964a77cf646e8ef9344c702e7fb7116b6b5dd7ffae3ed35a8714fab17840ed` |

## §4. Closed gates (preserved verbatim per Manager memo + RUNSPEC §4)

The following remain CLOSED — this calibration sweep authorizes nothing further:

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
- No follow-on D4 cell execution
- No model-facing work beyond this sweep

## §5. Pre-registered harness output — for transparency, NOT for interpretation

CS ran the pre-registered `calibration_sweep_verdict.py` harness on the three run records for transparency only. The verdict is δ-sensitive (and m-sensitive); Senior selects the final m/δ values per the pre-declared rule. Two illustrative runs:

**With margin=0.05, delta=0.05** (band: 0.6625 < a < 0.95):
```
CAL-A: clean=1.0    → CEILING
CAL-B: clean=0.975  → CEILING (just above ceiling-δ)
CAL-C: clean=0.95   → CEILING (exactly at ceiling-δ; harness uses strict <)
VERDICT: INSUFFICIENT / NEEDS REPAIR
REASON:  no candidate escaped the ceiling under this δ
```

**With margin=0.05, delta=0.02** (band: 0.6625 < a < 0.98):
```
CAL-A: clean=1.0    → CEILING
CAL-B: clean=0.975  → IN_BAND
CAL-C: clean=0.95   → IN_BAND
VERDICT: BAND PLAUSIBLE
REASON:  in-band candidate(s) [(CAL-B, 0.975), (CAL-C, 0.95)]
```

**CS does not pick m/δ.** Senior pre-declares them and runs the harness; that result is the authoritative verdict.

## §6. Single-difference note on CAL-A

CS's `run_calibration_sweep.py` ran a per-item-strict single-difference check (same queried_key + same slot per item index between clean and defective). The fresh CAL-B and CAL-C candidates were constructed to meet that stricter criterion and pass it.

CAL-A uses the existing constructed-positive bytes (sha256 `f412d04c…` clean, `4ea3c277…` defective). Those were originally matched at the **distribution level** (per their `realized_match_manifest.json`'s `held_constant` list: `list_len`, `queried_slot_distribution`, `key_value_vocabulary_family`, `token_length_profile`, `null_answerable_stratum`, `surface_format`, `item_count`, `scoring_harness`). The original manifest declares `single_difference_invariant_check: PASS` under that distribution-level convention — that is the convention under which the validation passed and the closeout was accepted.

CS's stricter per-item check is NOT the original criterion; it is a stricter check CS added for the fresh constructors. CAL-A passes the original distribution-level check (the convention of record) and fails the new stricter check. CS records `single_difference_ok=TRUE` for CAL-A per the original manifest's declared PASS, with this note for full transparency. CAL-B and CAL-C pass both criteria.

## §7. Substantive observation (informational, not interpretation)

The CS analytical read offered earlier in this session ("plausible band exists; not demonstrated; every byte-verified accuracy was 1.0") is now updated by the bytes from this sweep:

- The off-ceiling levers (length / deep slot / near-miss distractors) **do** move clean accuracy off ceiling on this candidate. CAL-B 0.975 and CAL-C 0.95 are the first off-ceiling clean data points in the record.
- The first-order question of the verdict has resolved from "uncharacterized" toward characterizable, **provided** Senior's chosen δ value places at least one of CAL-B/CAL-C strictly below ceiling-δ.
- Whether this is BAND PLAUSIBLE or INSUFFICIENT depends entirely on δ. The bytes do not pick δ.
- This observation does not interpret the verdict. It only states what the new bytes say relative to the prior CS analytical read.

## §8. Sealed bytes (no-mutation check)

| Artifact | sha256(16) | Status |
|---|---|---|
| `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | `5b557ae2a4c90bf3` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd07007` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e85` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4` | UNCHANGED |
| Constructed pair (CAL-A; 3 JSONs) | `f412d04c…` / `4ea3c277…` / `49cd6451…` | UNCHANGED |

≈53rd sealed-byte survival check.

## §9. Language-perimeter

None of the binding forbidden phrasings appears. The sweep result is NOT framed as: certification, compression evidence, retention evidence, Claim C progress, candidate certification, ranking, seam evidence, robust to compression, candidate certified, etc. The substantive observation in §7 is bounded to "the bytes show off-ceiling data points exist now."

## §10. Disposition

**SWEEP EXECUTED. BYTES DELIVERED.** Three per-candidate run records (`cal-a_run.json` + `cal-b_run.json` + `cal-c_run.json`) under `governance/2026-06-11_lane-1a-prime/certification-readiness/sweep_run_records/` carry the schema the pre-registered harness consumes. Raw outputs + member files + manifests under `experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs/`. CS does NOT interpret.

Senior next: run `calibration_sweep_verdict.py` with pre-declared margin and delta values → emit band verdict (BAND PLAUSIBLE / TOO NARROW / INSUFFICIENT) → update PROGRAM-POSITION-v0.1 with verdict → Team Lead prepares Manager decision surface.

— CS Engineer, 2026-06-13
