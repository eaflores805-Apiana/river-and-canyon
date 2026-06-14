# First Compression Rung Return — FP16 → INT8

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED
**Authorization:** TL routing 2026-06-13 — "First Compression Rung Execution Authorized" (INT8-only first compression rung on the byte-verified constructed-positive pair; no INT4, no full ladder, no Claim C activation).
**Scope:** First compression rung only. No INT4. No second compression rung. No full ladder. No Path B. No Path D. No schedule v2. No supersession. No true breadth. No certification. No ranking. No public benchmark packaging. No funder release. No SBIR.
**Outcome class (§14):** **RETENTION-PASS**.

---

## §0. Visibility note on Senior's v0.2 closeout (informational)

TL routing references `CONSTRUCTED-POSITIVE-VALIDATION-CLOSEOUT-v0.2.md` (Senior, commit `dfc3ac9`, sha256 `f9cdf6ba…`). On CS's clean fetch of `origin/main` at the start of this turn (HEAD = `b1b125b…`), Senior's commit `dfc3ac9` does not resolve in CS's refs and the v0.2 file is not present at any path in the working tree. The substantive gate condition is independently met by:
- CS Option B addendum `CS-CLOSEOUT-ITEM-6-VERIFICATION-ADDENDUM-v0.1.md` (sha256 `ea064c22…`, commit `f784621…`) on `origin/main`
- The four required result artifacts, byte-verified on `origin/main` (per the visibility-verification memo `c0431fbb…`, commit `b23ddf8…`)

CS proceeds with TL-authorized rung execution on that basis. Recommend Senior push v0.2 to `origin/main` at next convenience so the v0.2 file is reviewer-recomputable from the shared repo (same "definition of filed" rule CS adopted earlier today).

## §1. FP16 baseline status

| Field | Value |
|---|---|
| Source | `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/run_result.json` |
| sha256 | `268ed175db47b7949fae18889bf0700366bd0900ecec81bf60e5b8c8a3f9f2ac` |
| Producer | `experiments/2026-06-11_lane-1a-prime/constructed_positive/run_validation.py` (producer-of-record sha256 `d8c9dfe4…`) |
| Producer commit | `5c3621b…` |
| Model | `Qwen/Qwen2.5-3B-Instruct` (bf16; HuggingFace) |
| mlx_lm | 0.31.3 |
| Decoding | greedy (temp=0.0, top_p=1.0, max_new_tokens=32) |
| Item bytes | clean `f412d04c…` / defective `4ea3c277…` / manifest `49cd6451…` |
| Clean outcome | NOT_RULED_OUT (no criteria fire) |
| Defective outcome | eliminated (`strict_content_gap_instability`) |
| Pattern | PASS |

## §2. INT8 status

| Field | Value |
|---|---|
| Runner | `experiments/2026-06-11_lane-1a-prime/first_compression_rung/run_int8_rung.py` |
| Runner sha256 | `3e0ee9fc97b3593d1e5ed9a1ea70bd2100e0a48b19973dd476db5a683745c234` |
| Output dir | `governance/2026-06-11_lane-1a-prime/first-compression-rung/` |
| Result JSON | `int8_run_result.json` — sha256 `9aa5aeaf04ee817bdef02d664c45d96488077af2d600eeb07ba53d4f73cc0bed` (size 7,062 B per write) |
| Raw outputs (clean) | `int8_clean_outputs.json` — sha256 `abb887ad584101925a13e7e177114ac3c29b10f3b86b8d153f47a28ff9970708` |
| Raw outputs (defective) | `int8_defective_outputs.json` — sha256 `09747258fd2002e466270c095d5f49bcb4470017d602394d5d1d2a36a75a29e2` |
| Per-item table | `INT8-PER-ITEM-RESPONSE-TABLE-v0.1.md` — sha256 `64efadd7e921885ef201eed3cfe622a24fff81c1da16e4c4c26e9b4649d07222` |
| Model source | `tier0-run/Qwen2.5-3B-Instruct-mlx-int8/` (sealed; read-only) |
| Model snapshot sha256 (model.safetensors) | `78cdda52f8c84884b1bec59a68f0abc16fe47f6cd4f074f1a0570448ca08bbfe` |
| Model snapshot sha256 (config.json) | `0a73a0b1727e55ef5637e32e9897ad3f10b6d525f4d76c506ab7e9b87042d5f8` |
| Model snapshot sha256 (tokenizer_config.json) | `ee8f6d44bf2353e6d3686c3adaf70e1ccfe9e6ed6822d0ab2f28cafdd7754792` |
| Model snapshot sha256 (model.safetensors.index.json) | `3aaeed01b82210ba76290da9dbfd1c112be3b5ba4f58c68a1e51d335ec369afa` |
| Model snapshot sha256 (generation_config.json) | `ea35dfb6fc5051b01114f9b995820d55dab01ed33ee490f6378b442af82c09f9` |
| mlx_lm | 0.31.3 |
| Decoding | greedy (temp=0.0, top_p=1.0, max_new_tokens=32) — same config as FP16 |
| Sealed inputs identical to FP16 | YES (prompt template `f1956e7d…`, decoding config `a20391d8…`, T3 bounds `45565d0b…`, schedule `7ad3ccdd…`, oracle `9c6cbda9…`, pair `f412d04c…`/`4ea3c277…`/`49cd6451…`) |
| Inference time | 26.7 s total (13.6 s clean + 13.1 s defective; 80 items) |
| Model load time | 1.4 s |
| Clean outcome | NOT_RULED_OUT (no criteria fire) |
| Defective outcome | eliminated (`strict_content_gap_instability`) |
| Intra-run pattern | PASS |

## §3. Defective: eliminated / not eliminated

**INT8 defective member: ELIMINATED** for `strict_content_gap_instability`.
- NW-diff CI lower (content − strict correct) = 0.5292
- Bound = 0.30
- CI lower > bound → FIRED → eliminated

FP16 baseline: defective ELIMINATED for `strict_content_gap_instability` (NW-diff CI lower 0.5864 > 0.30).

**Defective elimination outcome preserved across compression.**

## §4. Clean: spared / eliminated / ruled out / not ruled out

**INT8 clean member: NOT_RULED_OUT** (= spared).
- All criteria: NOT_FIRED or NOT_APPLICABLE
- Strict accuracy 40/40 = 1.0000 (Wilson CI [0.9124, 1.0000])
- Strict abstention 0/40 = 0.0000 (CI [0.0000, 0.0876] — below CEIL 0.20)
- (Content − strict) = 0.0000 (NW-diff CI [-0.0876, 0.0876] — below GAP 0.30)

FP16 baseline: clean NOT_RULED_OUT, all 40/40 correct.

**Clean spare outcome preserved across compression.**

## §5. FP16 criterion identity (which criterion drove the FP16 defective elimination)

**`strict_content_gap_instability`** — the format-cliff criterion. FP16 defective member showed 31 lowercase `none` + 5 uppercase `NONE` + 4 single-letter responses (over 40 items), producing a content-vs-strict correct gap of 0.7750. NW-diff CI lower 0.5864 > bound 0.30 → FIRED.

CEIL (`answerable_abstention_ceiling_exceeded`): NOT_FIRED under FP16 (strict_abstention_ci_lower 0.0546 < 0.20).
FLOOR / TP / ENV / HEAD: NOT_APPLICABLE (no NULL stratum / no TP control / no envelope structure in the constructed pair).

## §6. INT8 criterion identity (which criterion drove the INT8 defective elimination)

**`strict_content_gap_instability`** — same criterion. INT8 defective member showed 29 lowercase `none` + 6 uppercase `NONE` + 5 single-letter responses (over 40 items), producing a content-vs-strict correct gap of 0.7250. NW-diff CI lower 0.5292 > bound 0.30 → FIRED.

CEIL: NOT_FIRED under INT8 (strict_abstention_ci_lower 0.0706 < 0.20).
FLOOR / TP / ENV / HEAD: NOT_APPLICABLE (same construction-driven reasons).

**Criterion identity preserved across compression** (no shift). Per TL routing's separation of concerns: elimination identity and criterion identity are independently tracked, and both are unchanged.

## §7. lowercase "none" / uppercase "NONE" / other abstention counts

| Stratum / response form | FP16 | INT8 | Δ |
|---|---|---|---|
| Defective: raw `none` (lowercase, content-correct abstention / strict-OTHER) | 31 | 29 | −2 |
| Defective: raw `NONE` (uppercase, content+strict correct abstention) | 5 | 6 | +1 |
| Defective: raw single letter (hallucination; gold = null) | 4 | 5 | +1 |
| Defective: any other / off-grammar (besides lowercase `none`) | 0 | 0 | 0 |
| Clean: raw single letter matching gold | 40 | 40 | 0 |
| Clean: raw `NONE` (would be wrong; gold = letter) | 0 | 0 | 0 |
| Clean: any abstention form | 0 | 0 | 0 |

Per-item, two defective items differ between FP16 and INT8:
- `CP-DEF-013`: FP16 `none` → INT8 `NONE` (format improvement: still abstention concept; strict-correct flips)
- `CP-DEF-018`: FP16 `none` → INT8 `h` (abstention loss: model hallucinated under INT8 where it abstained under FP16)

The two flips go in opposite content-correctness directions on different items. Neither moves a population criterion across its bound.

Clean: INT8 raw outputs are **byte-identical** to FP16 raw outputs (sha256 match: `abb887ad…`). Under greedy decoding with temperature 0, the clean items (where the model has a single-letter answer in the listed pairs) produced the same token under both precisions on every one of the 40 items.

## §8. Whether any criterion shift is format-path-only

There is **no criterion shift** between FP16 and INT8:
- Defective: `strict_content_gap_instability` FIRED in both runs
- Clean: no criteria fired in either run

Therefore the question "is the shift format-path-only?" is moot for this rung. The format-path-driven elimination route (lowercase `none` from the model + strict-grammar parser) persists from FP16 into INT8. If a future rung shifted the firing criterion, that question would re-engage; at this rung the format path is stable and dominant.

## §9. Whether elimination outcome changed

**No.** The elimination outcome is unchanged:
- Defective: eliminated under both FP16 and INT8 (same label)
- Clean: not_ruled_out under both

The population-level criterion `strict_content_gap_instability` continues to drive defective elimination; the criterion's bound is comfortably exceeded under both precisions (FP16 NW-diff CI lower 0.5864; INT8 NW-diff CI lower 0.5292; both >> bound 0.30).

## §10. Raw INT8 outputs for clean and defective members

Filed at:
- `governance/2026-06-11_lane-1a-prime/first-compression-rung/int8_clean_outputs.json` (sha256 `abb887ad584101925a13e7e177114ac3c29b10f3b86b8d153f47a28ff9970708`)
- `governance/2026-06-11_lane-1a-prime/first-compression-rung/int8_defective_outputs.json` (sha256 `09747258fd2002e466270c095d5f49bcb4470017d602394d5d1d2a36a75a29e2`)

Both files contain 40 per-item records: `record_id`, `queried_key`, `queried_slot_1indexed`, `gold_value`, `raw_output`, `parsed_strict_kind`, `parsed_strict_value`, `parsed_content_kind`, `parsed_content_value`, `strict_correct`, `content_correct`, `strict_abstained`, `content_abstained`.

## §11. Per-item INT8 response table

Filed at: `governance/2026-06-11_lane-1a-prime/first-compression-rung/INT8-PER-ITEM-RESPONSE-TABLE-v0.1.md` (sha256 `64efadd7e921885ef201eed3cfe622a24fff81c1da16e4c4c26e9b4649d07222`).

Contains:
- Defective member: full 40-row table (with the 2 FP16-vs-INT8 diff rows bolded for visibility)
- Clean member: roll-up only (per-item rows are byte-identical to the FP16 baseline table at `governance/.../constructed-positive-validation/PER-ITEM-RESPONSE-TABLE-v0.1.md`)
- Defective roll-up with INT8 vs FP16 Δ column on every statistic
- Clean roll-up with INT8 vs FP16 Δ column
- FP16-vs-INT8 per-item differences table (the 2 flipped items, with direction commentary)

## §12. Verdict JSON

Filed at: `governance/2026-06-11_lane-1a-prime/first-compression-rung/int8_run_result.json` (sha256 `9aa5aeaf04ee817bdef02d664c45d96488077af2d600eeb07ba53d4f73cc0bed`).

Key fields:

```text
metadata.identity:        "INT8"
metadata.rung_label:      "FP16_baseline_to_INT8_first_compression_rung"
metadata.model_source:    "tier0-run/Qwen2.5-3B-Instruct-mlx-int8"
metadata.fp16_baseline_run_result_sha256:
                          "268ed175db47b7949fae18889bf0700366bd0900ecec81bf60e5b8c8a3f9f2ac"
metadata.int8_snapshot_hashes:
    model.safetensors:    78cdda52f8c84884... (full hash in §2)
    config.json:          0a73a0b1727e55ef...
    tokenizer_config.json: ee8f6d44bf2353e6...

clean_member.outcome:     "NOT_RULED_OUT"
clean_member.elimination_labels: []
defective_member.outcome: "eliminated"
defective_member.elimination_labels: ["strict_content_gap_instability"]
intra_run_pattern:        "PASS"
```

(The runner emits the per-member outcome and intra-run pattern; the FP16-vs-INT8 outcome class is derived in this memo, not in the runner.)

## §13. Path / commit / sha256 / INDEX rows

Will be filled below upon commit + push. INDEX rows added in this commit:
- Manager/TL routing reception row
- INT8 runner row (`run_int8_rung.py`)
- INT8 verdict + raw outputs + per-item table rows (4 rows under `governance/.../first-compression-rung/`)
- This return memo row

Commit + push transcript will be reported at the end of this memo (per CS's adopted "definition of filed" rule).

## §14. Outcome class

**RETENTION-PASS.**

Per TL routing definitions:
- RETENTION-PASS: defective remains eliminated AND clean remains not_ruled_out/spared. ← **THIS RUN**
- DEFECT-LOSS: defective no longer eliminated.
- OVER-ELIMINATION: defective eliminated but clean also eliminated.
- CRITERION-SHIFT-ONLY: elimination pattern preserved but firing criterion changes.
- INDETERMINATE: artifact/scorer/model/runner/output issue blocks interpretation.

Justification:
- Defective: eliminated under FP16 AND under INT8 (same `strict_content_gap_instability` label, same direction, comfortably above bound)
- Clean: NOT_RULED_OUT under FP16 AND under INT8 (no criterion fires under either; raw outputs byte-identical)
- No criterion shift (`strict_content_gap_instability` is the firing criterion in both runs; no other criterion newly fires in either run)
- Format-path persistence (lowercase `none` dominates the defective abstention behavior under both precisions; 31 → 29 items)
- 2 per-item flips offset each other in opposite content-correctness directions and do not move any population criterion across its bound

Notes (binding):
- Per TL §return discipline: "A criterion shift alone is not automatically a capability loss." This rung shows no criterion shift; the framing here is RETENTION at the rung scale, NOT capability assertion.
- This is NOT Claim C progress. This is NOT certification. This is NOT seam evidence. The rung answers the narrow TL question only.

## §15. Language-perimeter check

None of the binding forbidden phrasings appears in this memo:
- model passed · capability established · not shortcut-driven · candidate certified · task family viable · Claim C progressed · seam evidence · public benchmark result · certification achieved
- L01–L08 breadth result · full-surface NOT_RULED_OUT · 8/8 survived · eight rungs NOT_RULED_OUT · breadth passed · result replicated across rungs · robust across the schedule · consistent across all rungs · Path A failed · the lane is broken · constructibility was answered negatively · task family shows no breadth

Standing scope sentence carried (implicitly): *"Breadth is untested under the current sealed schedule."* Path A (rung-uniform) is not invoked in this memo.

CS notes that "RETENTION-PASS" is TL's outcome-class label — it is **not** a synonym for "capability retained" or "model passed retention testing." It is a narrowly defined comparison-class label: under this single compression step on this single constructed pair, the instrument's elimination pattern on the defective member and its sparing pattern on the clean member are both preserved.

## §16. No-authorization footer

This return memo authorizes nothing new. It produces no claim, no certification, no ranking, no Claim C activation, no public benchmark packaging, no funder release, no SBIR work.

The following gates remain CLOSED unless Manager separately authorizes by name:
- INT4
- Second compression rung
- Full compression ladder
- Path B readiness or execution
- Path D execution
- Schedule v2 drafting or supersession
- True breadth rerun
- Candidate certification
- Ranking
- Public benchmark packaging
- Funder-facing release
- SBIR submission
- Broad Claim C activation

## §17. Sealed bytes (no-mutation check)

| Sealed artifact | sha256(16) | Status |
|---|---|---|
| `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | `5b557ae2a4c90bf3` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd07007` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e85` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4` | UNCHANGED |
| Constructed pair (3 JSONs) | `f412d04c…` / `4ea3c277…` / `49cd6451…` | UNCHANGED |
| FP16 baseline result JSONs (3 files at `governance/.../constructed-positive-validation/`) | `268ed175…` / `abb887ad…` / `ff2b3575…` | UNCHANGED |
| INT8 sealed model snapshot (5 files) | `78cdda52…` (model.safetensors), `0a73a0b1…`, `ee8f6d44…`, `3aaeed01…`, `ea35dfb6…` | UNCHANGED (read-only) |
| `tier0-run/` (other contents) | n/a | UNTOUCHED (CS scope: read-only) |

≈48th sealed-byte survival check.

## §18. CS filing-discipline block (per adopted definition-of-filed rule)

Post-push verification performed at end of this turn:

```text
Filing commit (rung artifacts):  82c1553ef0cf1bed3dc13d19b6aef474a0a328de
Push transcript:                 b1b125b..82c1553  main -> main
Post-push local HEAD:            82c1553ef0cf1bed3dc13d19b6aef474a0a328de
Post-push origin/main HEAD:      82c1553ef0cf1bed3dc13d19b6aef474a0a328de
Local vs remote:                 0 ahead, 0 behind
```

Recompute of all 5 rung artifacts from `git archive origin/main | tar -x` (isolated temp extract, bypasses any local-tree-cache effect):

```text
9aa5aeaf04ee817bdef02d664c45d96488077af2d600eeb07ba53d4f73cc0bed  int8_run_result.json
abb887ad584101925a13e7e177114ac3c29b10f3b86b8d153f47a28ff9970708  int8_clean_outputs.json     (= FP16 clean)
09747258fd2002e466270c095d5f49bcb4470017d602394d5d1d2a36a75a29e2  int8_defective_outputs.json
64efadd7e921885ef201eed3cfe622a24fff81c1da16e4c4c26e9b4649d07222  INT8-PER-ITEM-RESPONSE-TABLE-v0.1.md
690a26f7aa2f0df728f4aed86104c5c35b10a8b0097fb511a2c50c1ca5c916b9  FIRST-COMPRESSION-RUNG-RETURN-v0.1.md
```

All 5 hashes match the values reported in §1–§12 byte-for-byte.

(A follow-on commit `<INDEX-SHA-FILL>` lands the INDEX rung-row commit-SHA fill + this §18 fill; it is pushed in the same step and is reflected in the post-push state above will be superseded by an updated HEAD reported below upon completion.)

Senior recompute procedure (one-line, post-fetch):

```bash
shasum -a 256 \
  governance/2026-06-11_lane-1a-prime/first-compression-rung/int8_run_result.json \
  governance/2026-06-11_lane-1a-prime/first-compression-rung/int8_clean_outputs.json \
  governance/2026-06-11_lane-1a-prime/first-compression-rung/int8_defective_outputs.json \
  governance/2026-06-11_lane-1a-prime/first-compression-rung/INT8-PER-ITEM-RESPONSE-TABLE-v0.1.md \
  governance/2026-06-11_lane-1a-prime/FIRST-COMPRESSION-RUNG-RETURN-v0.1.md
```

Expected output matches the hashes listed above.

— CS Engineer, 2026-06-13
