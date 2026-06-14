# CS Run Report — CAL-Q v0.3 Calibration Pilot

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED — CAL-Q executed; four-way reporting delivered. **CS does NOT interpret.** Senior interprets against CAL-Q v0.3's pre-declared rule (BAND PLAUSIBLE / NEEDS REPAIR / PIVOT).
**Authorization:** Manager 2026-06-13 "Run CAL-Q v0.3 Calibration Pilot" — narrow FP16/native; CAL-Q only.
**Scope:** Calibration only. Not certification, not compression, not retention, not Claim C, not ranking.

---

## §1. Pre-flight (Manager-required)

| Field | Value |
|---|---|
| HEAD at run time | `c1bf3c76dd2af103666ba4c34b21cb2ab09a78a0` |
| CAL-Q v0.3 spec path | `governance/2026-06-11_lane-1a-prime/certification-readiness/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.3.md` |
| CAL-Q v0.3 spec sha256 | `839249000bb1cb34d423534009d24682339e56c51ce393be45f5c03526a31a13` |
| prompt_template sha256 | `f1956e7dd43f165c8707fe88bc11757888f108e7e9766aa186ac9fc04f8b368a` |
| decoding_config sha256 | `a20391d89972d47c0b231f5c6da9f8a9f4c7be8c975ab98bd95a32327196f803` |
| scorer (run_validation.py) sha256 | `1de334ca1cff812dc454af693ba5c87d3945e53f0ffbb2590be346b96d67175f` |
| rescore script (NULL-norm) sha256 | `bc0b48db88b7cf71e9518a8f15f48632b8388a058c3ea9663d7a98d561dfefc5` |
| Runner (`run_cal_q.py`) sha256 | `8acdf10556cd5535d2cfd9043481ea1b4b2138cd1ace6b78f03d8e41c67e81b2` |
| Manifest sha256 | `4de97d51f27f3146df890abcaa5efc04a23956b11e34d742dc9b54595b52102d` |
| semantic-read PASS | YES (CS v0.3 verification + per-construction confirmed mechanically: code A → queried_key in both members) |
| same-key identity (clean & defective) | YES — code A maps to `queried_key` in BOTH members for every item (verified by `same_key_identity_both_members` check) |
| single-difference feasibility | YES — verified by mechanical check; per-item invariant + queried_slot/slot_range/code_book/query_code all match between clean and defective per item |
| content load CAL-B-like | YES — list_len=13, slots=[8,9,10,11], near_miss=2, 40 items |
| decoy material unchanged | YES — same distractor density as CAL-B |
| query-side-only change | YES — only the in-prompt code book + indirect query added; list content otherwise CAL-B-like |
| four-way defective reporting active | YES — strict NONE + concept abstention + true false-emission + format artifact all in the run record |
| route-state | GREEN scoped to CAL-Q only (Manager-authorized) |
| closed-gate list preserved | YES — verbatim 12-item list in §5 |

## §2. CAL-Q v0.3 results (four-way + Manager-required output format)

| Field | Value |
|---|---|
| candidate_id | CAL-Q |
| spec_version | v0.3 |
| query_form | in_prompt_code_book |
| construction config | list_len=13, queried_slots=[8,9,10,11], near_miss_count=2, n_items=40, construction_seed=20260613006 |
| single_difference_ok | **TRUE** (all mechanical checks PASS) |
| **clean accuracy (strict and concept identical)** | **0.6500 (26/40)** |
| **defective strict NONE accuracy** (category 1) | **0.0000 (0/40)** |
| **defective concept-level abstention** (category 2 — authoritative) | **0.0000 (0/40)** |
| **defective true false-emission rate** (category 3) | **1.0000 (40/40)** |
| **defective format-abstention artifact** (category 4) | **0 lowercase `none`, 0 uppercase `NONE`** (no abstentions in either form) |
| **clean band position** vs `0.6625 < clean < 0.95` | **BELOW band** (0.6500 < 0.6625; just below the shortcut floor + margin) |
| raw clean outputs path | `experiments/.../sweep_outputs/cal-q_clean_outputs.json` (sha256 `f62a9bc060411e2d…`) |
| raw defective outputs path | `experiments/.../sweep_outputs/cal-q_defective_outputs.json` (sha256 `60a618a25f09feb2…`) |
| manifest path | `experiments/.../sweep_outputs/cal-q_realized_match_manifest.json` (sha256 `4de97d51f27f3146…`) |
| scorer path | `experiments/.../constructed_positive/run_validation.py` (sha256 `1de334ca…`) |
| rescore script path | `experiments/.../certification_readiness/rescore_null_normalized.py` (sha256 `bc0b48db…`) |
| run record JSON | `governance/.../sweep_run_records/cal-q_run.json` (sha256 `90de7fd0a20f650b…`) |

## §3. Full-sweep comparison (now including CAL-Q)

| Cand | Query form | List | Slots | Near-miss | Clean (concept) | Defective abstention (concept) | True false-emission |
|---|---|---|---|---|---|---|---|
| CAL-A | direct | 9 | 6–8 | 0 | 1.0000 | 0.9000 | 0.1000 |
| CAL-B | direct | 13 | 8–11 | 2 | 0.9750 | 0.9250 | 0.0750 |
| CAL-C | direct | 17 | 10–15 | 4 | 0.9500 | 0.8750 | 0.1250 |
| CAL-E | direct | 21 | 13–18 | 4 | 0.9750 | 0.9000 | 0.1000 |
| **CAL-Q** | **in-prompt code book** | **13** | **8–11** | **2** | **0.6500** | **0.0000** | **1.0000** |

## §4. What the bytes show (CS describes, does NOT interpret)

For full transparency on what changed between CAL-Q and the prior CAL-A/B/C/E sweep, with NO interpretive call:

- **Clean accuracy dropped** from CAL-B's 0.975 (same content settings as CAL-Q) to 0.6500 — a drop of 0.325. The code-book decode step is genuinely harder for the model.
- **Defective concept-level abstention dropped** from CAL-B's 0.925 (same content settings) to 0.0000 — a drop of 0.925. The model never abstained on any defective item.
- **Defective true false-emission rose** from CAL-B's 0.075 to 1.0000 — the model emitted a letter on every defective item.
- **Format-abstention artifact disappeared**: prior candidates had `none` (lowercase) as the dominant abstention form (CAL-B: 35/40 lowercase, CAL-A: 31/40 lowercase). CAL-Q has 0/40 in either form — the model produced NO abstentions at all.
- **Clean accuracy of 0.6500 sits BELOW the band** (target was 0.6625 < a < 0.95). The drop went past the target into the floor-region.

For sanity, all three Manager pre-declared decision-rule criteria for BAND PLAUSIBLE:
- ✗ "clean lands strictly inside 0.6625 < clean < 0.95" — FAILS (0.6500 < 0.6625)
- ✗ "concept-level defective abstention remains stable around prior ~0.90 range" — FAILS (collapsed to 0.0000)
- ✗ "true false-emission remains low around prior ~0.10 range" — FAILS (rose to 1.0000)

The NEEDS REPAIR criterion ("clean drops too close to the shortcut floor, or defective concept-level abstention degrades materially") and the PIVOT criterion ("query-side difficulty ALSO fails to move clean off ceiling without breaking discrimination") both look applicable to the bytes — but **CS does NOT decide which branch Senior selects**.

## §5. Closed gates (preserved verbatim)

- No model execution (beyond this authorized CAL-Q run)
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

## §6. Notes / blockers

- **No blockers.** Run executed successfully; bytes recorded; four-way reporting wired in per spec §7.
- **Sample prompt format** (per spec §3, in run output): code book section + key-value list section + indirect query section. The model received exactly the format Senior specified.
- **Construction seed**: `20260613006` (CAL-Q-specific; distinct from CAL-B's `20260613001` to avoid byte collisions).
- **Single-difference verified mechanically** by per-item check + same-key identity check. All 40 items pass.
- **Senior interpretation pending** — Senior reads four-way report against the v0.3 pre-declared rule (§8 of the spec) and emits one of: BAND PLAUSIBLE / NEEDS REPAIR / PIVOT.

## §7. Sealed bytes (no-mutation check)

| Artifact | sha256(16) | Status |
|---|---|---|
| `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | `5b557ae2a4c90bf3` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd07007` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e85` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4` | UNCHANGED |
| Constructed pair + prior sweep records | per existing INDEX | UNCHANGED |

≈60th sealed-byte survival check.

## §8. Language perimeter + no-authorization

None of the binding forbidden phrasings. No certification. No compression. No INT4. No Claim C. CS does NOT decide BAND PLAUSIBLE / NEEDS REPAIR / PIVOT — Senior + Manager's call.

— CS Engineer, 2026-06-13
