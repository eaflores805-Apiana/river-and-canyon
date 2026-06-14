# Per-Item Response Table — Constructed-Positive Validation Run

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED — derivative artifact (re-derivable from `clean_outputs.json` + `defective_outputs.json`)
**Source bytes:**
- Clean raw outputs: `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/clean_outputs.json` (sha256 `abb887ad584101925a13e7e177114ac3c29b10f3b86b8d153f47a28ff9970708`)
- Defective raw outputs: `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/defective_outputs.json` (sha256 `ff2b35757d9f4536288dca59ab6bba07ad3d2482f1c2496bad44cd2eac631355`)

This is a derivative artifact built from the raw output JSONs (per TL §required-return item 3). The raw JSONs are authoritative; this table is for human readability.

---

## Legend

| Column | Meaning |
|---|---|
| `rec` | record_id (per item, byte-identical between clean and defective at same index) |
| `qkey` | queried_key (the key whose value the model was asked to return) |
| `slot` | 1-indexed position of queried_key in the listed pairs (if present); for defective, the slot the key WOULD occupy if present (it isn't) |
| `gold` | gold answer; `null` for defective member (queried key absent from pairs) |
| `raw` | model's raw output (greedy decode, first line, trailing punctuation stripped) |
| `s_kind` | strict parsed kind: `letter` (single [a-z]) / `NONE` (exact uppercase) / `OTHER` (off-grammar) |
| `c_kind` | content parsed kind: `letter_concept` (any single letter, either case) / `NONE_concept` (any case of "none") / `OTHER` |
| `s_corr` | strict_correct: Y/n |
| `c_corr` | content_correct: Y/n |
| `s_abst` | strict_abstained: Y/n |
| `c_abst` | content_abstained: Y/n |

---

## Defective member — 40 items (queried key absent from pairs; gold = null; abstention is the correct content response)

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
| CP-DEF-013 | 129 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-014 | 40 | 7 | null | 'z' | letter | letter_concept | n | n | n | n |
| CP-DEF-015 | 29 | 6 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-016 | 134 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
| CP-DEF-017 | 79 | 8 | null | 'NONE' | NONE | NONE_concept | Y | Y | Y | Y |
| CP-DEF-018 | 103 | 8 | null | 'none' | OTHER | NONE_concept | n | Y | n | Y |
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

### Defective member roll-up (computed from above)

| Statistic | Count | Fraction |
|---|---|---|
| Total items | 40 | 1.000 |
| Raw output = `none` (lowercase) | **31** | **0.775** |
| Raw output = `NONE` (uppercase) | **5** | **0.125** |
| Raw output = single lowercase letter (`f`, `g`, `j`, `z`) | **4** | **0.100** |
| `strict_kind = NONE` (exact uppercase) | 5 | 0.125 |
| `strict_kind = letter` | 4 | 0.100 |
| `strict_kind = OTHER` (the 31 `none` lowercase) | 31 | 0.775 |
| `content_kind = NONE_concept` (any case of "none") | **36** | **0.900** |
| `content_kind = letter_concept` | 4 | 0.100 |
| Strict correct (gold = null → exact `NONE` required) | 5 | 0.125 |
| Content correct (gold = null → any case of NONE counts) | 36 | 0.900 |
| Strict abstained | 5 | 0.125 |
| Content abstained | 36 | 0.900 |
| (Content − strict) correct | — | **0.775** |

This per-item table is the evidence base for §7 of `CS-CONSTRUCTED-POSITIVE-VALIDATION-RUN-RETURN-v0.1.md` and for the GAP criterion firing in `run_result.json`.

---

## Clean member — 40 items (queried key present; gold = lowercase letter)

| rec | qkey | slot | gold | raw | s_kind | c_kind | s_corr | c_corr | s_abst | c_abst |
|---|---|---|---|---|---|---|---|---|---|---|
| CP-CLEAN-000 | 145 | 7 | f | 'f' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-001 | 24 | 7 | t | 't' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-002 | 116 | 6 | x | 'x' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-003 | 54 | 6 | m | 'm' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-004 | 85 | 6 | p | 'p' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-005 | 116 | 8 | p | 'p' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-006 | 87 | 8 | d | 'd' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-007 | 80 | 7 | c | 'c' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-008 | 33 | 8 | l | 'l' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-009 | 144 | 6 | h | 'h' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-010 | 186 | 6 | x | 'x' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-011 | 144 | 8 | i | 'i' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-012 | 10 | 6 | f | 'f' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-013 | 25 | 6 | r | 'r' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-014 | 141 | 7 | l | 'l' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-015 | 75 | 6 | v | 'v' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-016 | 36 | 8 | f | 'f' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-017 | 181 | 8 | n | 'n' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-018 | 171 | 8 | b | 'b' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-019 | 80 | 8 | d | 'd' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-020 | 21 | 8 | t | 't' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-021 | 38 | 8 | l | 'l' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-022 | 175 | 8 | t | 't' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-023 | 178 | 8 | s | 's' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-024 | 185 | 7 | n | 'n' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-025 | 10 | 6 | u | 'u' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-026 | 156 | 7 | p | 'p' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-027 | 34 | 8 | u | 'u' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-028 | 66 | 6 | q | 'q' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-029 | 178 | 8 | g | 'g' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-030 | 85 | 6 | v | 'v' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-031 | 27 | 6 | c | 'c' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-032 | 40 | 6 | p | 'p' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-033 | 155 | 8 | l | 'l' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-034 | 133 | 6 | t | 't' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-035 | 159 | 7 | d | 'd' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-036 | 88 | 7 | s | 's' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-037 | 82 | 7 | d | 'd' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-038 | 27 | 6 | y | 'y' | letter | letter_concept | Y | Y | n | n |
| CP-CLEAN-039 | 89 | 8 | p | 'p' | letter | letter_concept | Y | Y | n | n |

### Clean member roll-up

| Statistic | Count | Fraction |
|---|---|---|
| Total items | 40 | 1.000 |
| Raw output exactly matches gold (single letter) | 40 | 1.000 |
| Strict correct | 40 | 1.000 |
| Content correct | 40 | 1.000 |
| Strict abstained | 0 | 0.000 |
| Content abstained | 0 | 0.000 |
| (Content − strict) correct | — | 0.000 |

---

## Re-derivability

This table can be regenerated from the raw output JSONs with a one-line Python expression. The raw JSONs are the byte-of-record; this markdown is a human-readable rendering.

```python
import json
items = json.load(open('defective_outputs.json'))
rows = [(o['record_id'], o['queried_key'], o['queried_slot_1indexed'],
         o['gold_value'], o['raw_output'],
         o['parsed_strict_kind'], o['parsed_content_kind'],
         o['strict_correct'], o['content_correct'],
         o['strict_abstained'], o['content_abstained']) for o in items]
```

— CS Engineer, 2026-06-13
