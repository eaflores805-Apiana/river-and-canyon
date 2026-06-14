# Per-Item Response Table — INT8 First Compression Rung

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED — derivative artifact (re-derivable from `int8_clean_outputs.json` + `int8_defective_outputs.json`)
**Source bytes:**
- INT8 clean raw outputs: `governance/2026-06-11_lane-1a-prime/first-compression-rung/int8_clean_outputs.json` (sha256 `abb887ad584101925a13e7e177114ac3c29b10f3b86b8d153f47a28ff9970708`)
- INT8 defective raw outputs: `governance/2026-06-11_lane-1a-prime/first-compression-rung/int8_defective_outputs.json` (sha256 `09747258fd2002e466270c095d5f49bcb4470017d602394d5d1d2a36a75a29e2`)

---

## Defective member (INT8) — 40 items

| rec | qkey | slot | gold | raw | s_kind | c_kind | s_corr | c_corr | s_abst | c_abst |
|---|---|---|---|---|---|---|---|---|---|---|
| CP-DEF-000 | 178 | 7 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-001 | 161 | 7 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-002 | 72 | 6 | null | 'f' | letter | letter_concept | n | n | n | n |
| CP-DEF-003 | 95 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-004 | 51 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-005 | 23 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-006 | 155 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-007 | 162 | 7 | null | 'NONE' | NONE | NONE_concept | Y | Y | Y | Y |
| CP-DEF-008 | 167 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-009 | 132 | 6 | null | 'NONE' | NONE | NONE_concept | Y | Y | Y | Y |
| CP-DEF-010 | 182 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-011 | 195 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-012 | 150 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| **CP-DEF-013** | 129 | 6 | null | **'NONE'** | **NONE** | NONE_concept | **Y** | Y | **Y** | Y |
| CP-DEF-014 | 40 | 7 | null | 'z' | letter | letter_concept | n | n | n | n |
| CP-DEF-015 | 29 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-016 | 134 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-017 | 79 | 8 | null | 'NONE' | NONE | NONE_concept | Y | Y | Y | Y |
| **CP-DEF-018** | 103 | 8 | null | **'h'** | **letter** | **letter_concept** | n | **n** | n | **n** |
| CP-DEF-019 | 189 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-020 | 48 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-021 | 149 | 8 | null | 'g' | letter | letter_concept | n | n | n | n |
| CP-DEF-022 | 66 | 8 | null | 'NONE' | NONE | NONE_concept | Y | Y | Y | Y |
| CP-DEF-023 | 84 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-024 | 140 | 7 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-025 | 63 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-026 | 77 | 7 | null | 'NONE' | NONE | NONE_concept | Y | Y | Y | Y |
| CP-DEF-027 | 110 | 8 | null | 'j' | letter | letter_concept | n | n | n | n |
| CP-DEF-028 | 185 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-029 | 64 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-030 | 168 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-031 | 193 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-032 | 111 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-033 | 61 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-034 | 166 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-035 | 86 | 7 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-036 | 127 | 7 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-037 | 154 | 7 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-038 | 93 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-039 | 125 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |

(Bolded rows are the two items where INT8 raw output differs from FP16; see §FP16-vs-INT8 diff table below.)

### Defective member (INT8) roll-up

| Statistic | INT8 | FP16 baseline | Δ |
|---|---|---|---|
| n | 40 | 40 | 0 |
| Raw output `none` (lowercase) | 29 | 31 | -2 |
| Raw output `NONE` (uppercase) | 6 | 5 | +1 |
| Raw output single lowercase letter | 5 | 4 | +1 |
| `strict_kind = NONE` | 6 | 5 | +1 |
| `strict_kind = letter` | 5 | 4 | +1 |
| `strict_kind = OTHER` (the lowercase `none`) | 29 | 31 | -2 |
| `content_kind = NONE_concept` | 35 | 36 | -1 |
| `content_kind = letter_concept` | 5 | 4 | +1 |
| Strict accuracy | 0.1500 | 0.1250 | +0.025 |
| Content accuracy | 0.8750 | 0.9000 | -0.025 |
| Strict abstention rate | 0.1500 | 0.1250 | +0.025 |
| Content abstention rate | 0.8750 | 0.9000 | -0.025 |
| (Content − strict) | **0.7250** | **0.7750** | -0.05 |
| NW-diff CI lower | **0.5292** | **0.5864** | -0.057 |
| GAP bound | 0.30 | 0.30 | — |
| GAP status | **FIRED** | **FIRED** | unchanged |
| CEIL CI lower | 0.0706 | 0.0546 | +0.016 |
| CEIL bound | 0.20 | 0.20 | — |
| CEIL status | NOT_FIRED | NOT_FIRED | unchanged |
| Defective outcome | **eliminated** (strict_content_gap_instability) | **eliminated** (strict_content_gap_instability) | **unchanged** |

---

## Clean member (INT8) — 40 items

**Note:** The INT8 clean raw outputs JSON has sha256 `abb887ad584101925a13e7e177114ac3c29b10f3b86b8d153f47a28ff9970708` — **byte-identical to the FP16 baseline clean outputs**. Under greedy decoding on the clean items, INT8 and FP16 produced the same 40 single-letter responses. The full table is omitted as redundant; refer to `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/PER-ITEM-RESPONSE-TABLE-v0.1.md` for the per-item rows.

| Statistic | INT8 | FP16 baseline | Δ |
|---|---|---|---|
| n | 40 | 40 | 0 |
| Strict accuracy | 1.0000 (40/40) | 1.0000 (40/40) | 0 |
| Content accuracy | 1.0000 (40/40) | 1.0000 (40/40) | 0 |
| Strict abstention rate | 0.0000 | 0.0000 | 0 |
| Content abstention rate | 0.0000 | 0.0000 | 0 |
| (Content − strict) | 0.0000 | 0.0000 | 0 |
| GAP status | NOT_FIRED | NOT_FIRED | unchanged |
| CEIL status | NOT_FIRED | NOT_FIRED | unchanged |
| Clean outcome | **NOT_RULED_OUT** | **NOT_RULED_OUT** | **unchanged** |

---

## FP16-vs-INT8 per-item differences (defective member)

Out of 40 defective items, INT8 and FP16 produced different raw outputs on exactly **2 items**:

| rec | qkey | slot | FP16 raw | FP16 strict / content | INT8 raw | INT8 strict / content | Direction |
|---|---|---|---|---|---|---|---|
| CP-DEF-013 | 129 | 6 | `none` | OTHER / NONE_concept | `NONE` | NONE / NONE_concept | format improvement: lowercase → uppercase (still abstaining; strict_correct flips n → Y; content unchanged) |
| CP-DEF-018 | 103 | 8 | `none` | OTHER / NONE_concept | `h` | letter / letter_concept | abstention loss: model abstained under FP16, hallucinated under INT8 (gold = null; both strict_correct and content_correct flip Y → n; content_abstained Y → n) |

Net population effect: +1 strict-correct (CP-DEF-013 format flip), −1 content-correct (CP-DEF-018 abstention loss). The 2 changes go in opposite directions on different items and do not move either population criterion across its bound.

Clean member: **0 items differ** (INT8 clean outputs byte-identical to FP16 clean outputs under greedy decoding).

---

— CS Engineer, 2026-06-13
