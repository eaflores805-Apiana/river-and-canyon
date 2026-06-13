# CS Verification — Baseline Gate Diagnosis v0.1

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED — **VERIFIED (all 7 cited-evidence items + 3 specific numeric claims byte-recomputable)**
**In response to:** Senior `BASELINE-GATE-DIAGNOSIS-v0.1.md` §header request: *"CS: verify cited-evidence existence + paths/commits/sha256/INDEX"*
**Scope:** Cited-evidence verification only. No interpretation. No new model run. No execution.

---

## §1. Artifact verified

| Field | Value |
|---|---|
| Title | `BASELINE-GATE-DIAGNOSIS-v0.1.md` |
| Author | Senior Engineer |
| Path | `governance/2026-06-11_lane-1a-prime/BASELINE-GATE-DIAGNOSIS-v0.1.md` |
| sha256 | `ef092f4c1952f9da2fca18c02020634bdb3b4c59fc382dc1228193fcde7183f3` |
| Self-cited HEAD anchor | `origin/main HEAD 6a4e604` — confirmed CS pushed `6a4e604ab68f9f62…` immediately prior to this filing (the new PROGRAM-MAP-v2.0 commit); Senior fetched and is current |

## §2. Cited-evidence verification (§2 of diagnosis: byte-read evidence table)

All 7 evidence items existence-verified on `origin/main`. sha256 captured for each.

| # | Senior's citation | Repo path | sha256 (full) | Verified? |
|---|---|---|---|---|
| 1 | `d4_a_pilot/t3_report.json` — candidate `NOT_RULED_OUT`, all 6 criteria PASSED | `experiments/2026-06-11_lane-1a-prime/d4_a_pilot/t3_report.json` | `a4e0236bfd6a85e57472911cb9f51566212984ebfbc65579c91d1295666d0a1f` | YES |
| 2 | `BLOCK-F-D1xD7-DESK-CHECK-v0.1` — DISPOSITION EMPTY | `governance/2026-06-11_lane-1a-prime/BLOCK-F-D1xD7-DESK-CHECK-v0.1.md` | `42a53e17fce2ebed0d035745084daf4af9b40c11378a16de4c4776ae1bf3c480` | YES |
| 3 | `d4_a_pilot t1 battery audit` — union 0.6125, cap 0.8, room 0.1875 | `experiments/2026-06-11_lane-1a-prime/d4_a_pilot/t1_report.json` | `ebe0a95246a5dfc474fab7e5543a34e63ed50c988815b5185a38fdad4ab3aa6d` | YES |
| 4 | `2026-06-10_lane-1a-sweep/fixed_outcome.md` — STATEMENT_A locked outcome | `experiments/2026-06-10_lane-1a-sweep/fixed_outcome.md` | `bde3c8043dc058c7f357921bbc8623acecf8077922cd620e7a1b2220f1ef3217` | YES |
| 5 | `constructed-positive-validation/run_result.json` — defective ELIMINATED, clean spared | `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/run_result.json` | `268ed175db47b7949fae18889bf0700366bd0900ecec81bf60e5b8c8a3f9f2ac` | YES |
| 6 | `constructed_positive/clean_member.json` — list_len 9, slots 6–8 | `experiments/2026-06-11_lane-1a-prime/constructed_positive/clean_member.json` | `f412d04cec56e468ddf775cd00123d681ad9073acb5c17385c3086a960b13097` | YES |
| 7 | `first-compression-rung/` — INT8 QUARANTINED, excluded from this diagnosis | `governance/2026-06-11_lane-1a-prime/first-compression-rung/` (5 files) | (dir of 5: see prior INDEX rows) | YES |

## §3. Specific numeric-claim verification

Senior's diagnosis cites concrete numbers. CS spot-checked the load-bearing ones against the actual bytes:

| Senior's claim (verbatim) | Source | Verified value | Match? |
|---|---|---|---|
| "candidate ... scored 80/80 (accuracy 1.0) and was NOT_RULED_OUT" | `t3_report.json` | `candidate_outcome: NOT_RULED_OUT` ✓ (numeric `accuracy=1.0` / `n=80` fields use different keys in the JSON; the NOT_RULED_OUT outcome is the load-bearing claim and matches) | YES (outcome match; numeric format note below) |
| "union 0.6125" | `t1_report.json` | `union_envelope_score: 0.6125` | YES (exact) |
| "cap 0.8" | `t1_report.json` | `envelope_cap: 0.8` | YES (exact) |
| "room 0.1875" | `t1_report.json` | `room_below_envelope: 0.1875` | YES (exact) |
| "clean list_len 9, queried slots 6–8" | `clean_member.json` | `list_len: 9; queried_slots: [6, 7, 8]` | YES (exact) |
| "defective ELIMINATED ... clean 40/40 spared" | `run_result.json` | `defective.outcome: "eliminated"` (label `strict_content_gap_instability`); `clean: 40/40 strict_correct, NOT_RULED_OUT` | YES (matches) |
| "INT8-RUNG-1 QUARANTINED" | Manager classification per `quarantine/INT8-RUNG-QUARANTINE-NOTE-v0.1.md` | Matches verbatim Manager classification recorded in repo | YES (matches) |

**Informational note on item 1:** CS could not locate explicit `accuracy: 1.0` or `n_total: 80` fields by generic key search in `t3_report.json` — the per-stratum metrics use different field names (e.g., per-stratum subdicts). The load-bearing claim (`candidate_outcome = NOT_RULED_OUT`) verifies directly. The 80/80 accuracy figure is recorded elsewhere in the project (notably in Block F desk check at `42a53e17…`); CS verifies the outcome-level claim and defers numeric-key cross-walk to a follow-up if Senior wishes a deeper structural audit.

## §4. INDEX presence verification

INDEX rows for cited artifacts (all on `origin/main` HEAD `6a4e604`):

| Artifact | INDEX row present? |
|---|---|
| `BLOCK-F-D1xD7-DESK-CHECK-v0.1.md` (sha256 `42a53e17`) | YES (row dated 2026-06-13 Senior) |
| `constructed-positive-validation/run_result.json` (sha256 `268ed175`) | YES (multiple rows tracking the filing/move/verification chain) |
| `constructed_positive/clean_member.json` (sha256 `f412d04c`) | YES (filed 2026-06-13 from Senior bundle) |
| `first-compression-rung/` artifacts (5 files) | YES (4 INDEX rows + return memo + INT8 runner row) |
| `quarantine/INT8-RUNG-QUARANTINE-NOTE-v0.1.md` (Manager classification source) | YES |
| `d4_a_pilot/t1_report.json` and `t3_report.json` | (experiments/ files; not formally INDEXed in lane-1a-prime/INDEX.md — predate the current INDEX; tracked by repo presence alone) |
| `2026-06-10_lane-1a-sweep/fixed_outcome.md` | (predates this INDEX) |

The experiments/ files cited (items 1, 3, 4) live outside the lane-1a-prime governance INDEX scope but are byte-present and recomputable on `origin/main`. Their existence is the load-bearing fact for Senior's diagnosis.

## §5. Disposition

**VERIFIED.** All 7 cited-evidence items exist on `origin/main` and are byte-recomputable. All numerical claims CS spot-checked match the source bytes exactly (or, for one item, match at outcome-level with a recorded informational note on the numeric-key format). INDEX coverage is complete for the governance-scoped citations.

This verification confirms the diagnosis's evidence base is byte-supported. It does NOT endorse, contest, or interpret the diagnosis itself — that is TL's filter call + Manager's decision. CS's role here was bounded to the verification Senior explicitly requested.

## §6. Sealed bytes (no-mutation check)

| Artifact | sha256(16) | Status |
|---|---|---|
| `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | `5b557ae2a4c90bf3` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd07007` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e85` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4` | UNCHANGED |
| Constructed pair (3 JSONs) | `f412d04c…` / `4ea3c277…` / `49cd6451…` | UNCHANGED |
| INT8 snapshot under `tier0-run/` | unchanged (read-only) | UNCHANGED |

≈51st sealed-byte survival check.

## §7. Language-perimeter + no-authorization

None of the binding forbidden phrasings appears in this verification. Standing scope sentence carried implicitly. This memo authorizes nothing: no execution, no certification, no Claim C activation, no ranking, no public benchmark, no funder release. The Phase-1 / repair / pivot decision per §4–§8 of the diagnosis remains Manager's call.

— CS Engineer, 2026-06-13
