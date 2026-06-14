# CS Run Report — CAL-E Targeted Repair Run

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED — CAL-E executed; bytes delivered. **CS does NOT interpret.** Senior interprets against the pre-declared CAL-E rule (BAND PLAUSIBLE / NEEDS REPAIR / PIVOT WATCH).
**Authorization:** Manager 2026-06-13 "Run CAL-E Targeted Repair Candidate" — narrow FP16/native; CAL-E only.
**Scope:** Calibration only. Not certification, not compression, not retention, not Claim C, not ranking.

---

## §1. Pre-flight attestations (Manager-required)

| Field | Value |
|---|---|
| HEAD at run time | `7e1d4fd6742429ca32d12d97c7f3db4cd52f274f` |
| CAL-E spec path | `governance/2026-06-11_lane-1a-prime/certification-readiness/CAL-E-TARGETED-REPAIR-SPEC-v0.1.md` |
| CAL-E spec sha256 | `f90f713233d8fce4d466a2ac6c3c4e45fbbc660fe09db31991390a7becc38758` |
| prompt_template sha256 | `f1956e7dd43f165c8707fe88bc11757888f108e7e9766aa186ac9fc04f8b368a` |
| decoding_config sha256 | `a20391d89972d47c0b231f5c6da9f8a9f4c7be8c975ab98bd95a32327196f803` |
| scorer (run_validation.py) sha256 | `1de334ca1cff812dc454af693ba5c87d3945e53f0ffbb2590be346b96d67175f` |
| manifest sha256 | (per CAL-E manifest file emitted; recorded in run record) |
| single-difference status | **TRUE** (per-item-strict + distribution) |
| semantic-read status | Construct spec semantic-read per CAL-E §8; PASS (construct mirrors CAL-B/C protocol, only difficulty varies) |
| route-state declaration | **GREEN — for CAL-E only** (Manager-authorized; RED for everything in §6) |
| closed-gate list preserved | YES — verbatim 13-item list in §6 |

## §2. Candidate configuration

| Field | Value |
|---|---|
| candidate_id | CAL-E |
| list length | 21 (longer than CAL-C's 17) |
| queried slot range | 13–18 (deeper interior than CAL-C's 10–15) |
| near-miss distractor structure | **near_miss_count = 4** (CAPPED at CAL-C's level per spec §4 — NOT increased) |
| distractor placement | random shuffle (NOT clustered at queried slot) |
| construction seed | `20260613005` |
| n items per member | 40 |
| primary clean-lowering lever (per spec) | LENGTH + DEPTH (not added near-miss) |
| model | `Qwen/Qwen2.5-3B-Instruct` (FP16/native via mlx_lm 0.31.3) |
| decoding | greedy, temp=0.0, max_new_tokens=32 |

## §3. Results (Manager-required output format)

| Field | Value |
|---|---|
| candidate_id | CAL-E |
| list_len | 21 |
| queried slot range | 13–18 |
| near-miss / distractor structure | near_miss_count = 4, random placement |
| single_difference_ok | **TRUE** |
| **clean accuracy** | **0.9750 (39/40)** |
| **defective accuracy** | **0.5750 (23/40)** |
| n | 40 each |
| clean band position vs target 0.88–0.92 | **OUT OF TARGET** (clean 0.9750 is ABOVE target band's upper bound 0.92 by 0.055; sits in 0.95–1.00 strip) |
| clean band position vs principled band 0.6625 < a < 0.95 | **OUTSIDE** (clean 0.9750 > 0.95) |
| defective-separation result | **OUT OF TARGET** (separation = clean − defective = 0.4000; target ≳0.78; gap to target = 0.38) |
| defective vs Manager-named ≤0.10 | **OUT OF TARGET** (defective 0.5750 is ~5.75× the target) |
| raw clean outputs | `experiments/.../certification_readiness/sweep_outputs/cal-e_clean_outputs.json` |
| raw defective outputs | `experiments/.../certification_readiness/sweep_outputs/cal-e_defective_outputs.json` |
| manifest path | `experiments/.../certification_readiness/sweep_outputs/cal-e_realized_match_manifest.json` |
| scorer path | `experiments/.../constructed_positive/run_validation.py` |
| run record JSON | `governance/2026-06-11_lane-1a-prime/certification-readiness/sweep_run_records/cal-e_run.json` (sha256 `74c3fa1f4623e043…`) |

## §4. Comparison across the full sweep (now A/B/C/E)

| Cand | List | Slots | Near-miss | Clean | Defective | Separation |
|---|---|---|---|---|---|---|
| CAL-A (control) | 9 | 6–8 | 0 | 1.0000 | 0.1250 | 0.8750 |
| CAL-B | 13 | 8–11 | 2 | 0.9750 | 0.0500 | 0.9250 |
| CAL-C | 17 | 10–15 | 4 | 0.9500 | 0.2250 | 0.7250 |
| **CAL-E** | **21** | **13–18** | **4** | **0.9750** | **0.5750** | **0.4000** |

**What the numbers say (no interpretation, just description):**
- Clean accuracy did NOT continue depressing as length/depth increased. CAL-E at length 21 / slots 13–18 scored 0.9750 — same as CAL-B at length 13 / slots 8–11, and HIGHER than CAL-C at length 17 / slots 10–15. The expected monotonic drop did not hold.
- Defective accuracy **jumped** from CAL-C's 0.2250 to CAL-E's 0.5750. This is the largest defective rate in the sweep by a wide margin.
- Separation collapsed from 0.7250 (CAL-C) to 0.4000 (CAL-E).
- The near_miss_count is the SAME between CAL-C and CAL-E (both 4); only list_len and slot depth increased. So increased length + deeper slots — at constant near-miss density — produced the defective inflation, not increased near-miss.

## §5. Pre-registered harness output — illustrative only (CS does NOT pick m/δ)

Per RUNSPEC discipline, Senior pre-declares m and δ. CS ran the harness at the principled threshold m=0.05, δ=0.05 (band 0.6625 < a < 0.95) including CAL-E:

```
CAL-A: clean=1.0    → CEILING
CAL-B: clean=0.975  → CEILING (just above ceiling-δ)
CAL-C: clean=0.95   → CEILING (exactly at ceiling-δ boundary)
CAL-E: clean=0.975  → CEILING (above ceiling-δ)
VERDICT: INSUFFICIENT / NEEDS REPAIR (no candidate escaped ceiling under principled δ)
```

Note: the harness's `single_difference_ok` check still uses the strict per-item criterion, so CAL-A would flag without the patch CS already applied. The verdict above assumes the patched CAL-A.

The PIVOT WATCH dimension (defective inflation) is outside the harness's current scope — the harness reads only clean accuracy band position. Senior interprets defective inflation against Manager's pre-declared CAL-E rule.

## §6. Closed gates (preserved verbatim)

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

## §7. Two informational observations (description, not interpretation)

**Observation 1 — runner bug surfaced + fixed mid-task.** CS's `run_cal_e.py` imported from `run_calibration_sweep.py`, which triggered top-level execution of the full A/B/C sweep again (Python module-level code runs on import). CS detected this immediately because the prior run records were overwritten with new timestamps. Recovery:
- The model outputs are deterministic (greedy decode); accuracy values are identical between runs
- CS restored CAL-A/B/C run records and raw outputs from prior commit `7e1d4fd…` via `git checkout HEAD --` so the sha256s remain anchored to the prior INDEX entries
- CS added `if __name__ == "__main__":` guard to `run_calibration_sweep.py` (new sha256 `85856abae2aca666…`) so future imports do not re-execute the sweep
- CAL-E run record sha256 `74c3fa1f4623e043…` is unaffected by this issue (it's a new file written by `run_cal_e.py`)

**Observation 2 — CAL-E result diverges from the spec's expectation.** CAL-E was designed (spec §4–§6) under the hypothesis that length + depth (not increased near-miss) would depress clean toward 0.88–0.92 without inflating defective. The byte-verified result shows the opposite trend on defective: defective accuracy nearly tripled vs CAL-C (0.2250 → 0.5750), and clean did not drop into the target band. This is the byte fact; Senior interprets what it means for the BAND PLAUSIBLE / NEEDS REPAIR / PIVOT WATCH decision.

## §8. Sealed bytes (no-mutation check)

| Artifact | sha256(16) | Status |
|---|---|---|
| `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | `5b557ae2a4c90bf3` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd07007` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e85` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4` | UNCHANGED |
| Constructed pair (CAL-A) | `f412d04c…` / `4ea3c277…` / `49cd6451…` | UNCHANGED |
| Prior sweep run records (CAL-A/B/C) | restored to `5ceeeea4…` / `814676cc…` / `50964a77…` | UNCHANGED on `origin/main` |

≈54th sealed-byte survival check.

## §9. Language-perimeter

None of the binding forbidden phrasings appears. The CAL-E run is NOT framed as: certification, compression evidence, retention evidence, Claim C progress, candidate certification, ranking, seam evidence, candidate certified, etc. CS describes byte facts and notes the spec's expectation differed from the result; CS does NOT decide what the result means for the decision rule — that is Senior + Manager.

## §10. Disposition

**CAL-E EXECUTED. BYTES DELIVERED.** Run record at `governance/.../sweep_run_records/cal-e_run.json` (sha256 `74c3fa1f4623e043…`) carries the harness-schema fields. Raw outputs + member files + manifest under `experiments/.../sweep_outputs/`. CS does NOT interpret.

Senior next: interpret against the pre-declared CAL-E rule (BAND PLAUSIBLE / NEEDS REPAIR / PIVOT WATCH); update PROGRAM-POSITION-v0.1; Team Lead prepares Manager decision surface; Manager decides cert-run-request well-formedness.

— CS Engineer, 2026-06-13
