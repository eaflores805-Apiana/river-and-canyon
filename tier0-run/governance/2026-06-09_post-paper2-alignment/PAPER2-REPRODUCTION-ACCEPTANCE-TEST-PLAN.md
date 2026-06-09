# Paper 2 Reproduction Acceptance Test Plan

**Filed:** 2026-06-09  
**Prepared by:** CS Engineer  
**Status:** FINAL — filed per Team Update 2026-06-09 directive  
**Purpose:** Define acceptance tests that the B1 harness must pass by re-deriving Paper 2 tables from locked artifacts. When all tests pass, the B1 harness is confirmed as the Paper 2 reproduction instrument.

---

## §1 Purpose and Scope

The B1 harness reproduction acceptance test is the validation gate for the B1 backfill. It answers:

> "Does the B1 runner, applied to the Cell01/02/03 locked manifests and scorer, reproduce all key numbers reported in Paper 2?"

Since the B1 harness is a provenance-hardening pass (new fields added; no scoring changes), all numeric outputs must be identical to the Paper 2 recomputation report (`PAPER2-RECOMPUTATION-REPORT.md`). Any numeric discrepancy indicates a B1 implementation error.

**Scope:** Cell01, Cell02, Cell03 — FP16 only. No stress runs. No new cells.

**Execution authorization:** Reproduction acceptance runs require Manager authorization. The B1 runner must be locked and hash-confirmed before any run.

---

## §2 Pre-Run Checklist

Before any B1 acceptance run, CS must confirm all of the following:

| Item | Requirement | Confirmed by |
|---|---|---|
| B1 runner hash locked | `EXPECTED_RUNNER_HASH` constant updated to B1 value; amendment lock note filed | CS |
| Scorer hash unchanged | B1 runner still locks scorer to sha256:b65c6803... for Cell03 | CS |
| Cell01/02 scorer note | Cell01 and Cell02 were originally run with scorer sha256:060afad9...; `classify_output()` is identical in both versions; numeric outputs are expected to match | CS (confirmed in PAPER2-RECOMPUTATION-REPORT.md §1) |
| Manifest hashes unchanged | All three manifest hashes match values embedded in original result JSONs | CS |
| Tokenizer hash | sha256:c0382117... — must match across all three cells | CS |
| Decoding settings | temperature=0.0, max_tokens=16 — unchanged | CS |
| Gate thresholds | Matches approved values in THRESHOLD-PROPOSAL-TWOHOP-L1.md Rev 2 | CS + Team Lead |
| B1 unit tests passing | All B1-T1 through B1-T10 pass | CS |
| Dry-run passes | B1 runner dry-run on all three cell manifests: no assertion failures | CS |
| Manager authorization | Explicit authorization to run B1 acceptance runs | Manager |

---

## §3 Acceptance Test Definitions

### AT-1: Per-cell accuracy counts

**Applies to:** Cell01, Cell02, Cell03 (separate runs)  
**Method:** Run B1 runner on each cell manifest. Read output JSON. Count `is_correct` by `query_type`.  
**Expected values (from PAPER2-RECOMPUTATION-REPORT.md §2):**

| Cell | hop1 | hop2 | composite | negative_graph |
|---|---|---|---|---|
| Cell01 | 14/24 | 24/24 | 18/24 | 2/24 |
| Cell02 | 9/24 | 23/24 | 20/24 | 0/24 |
| Cell03 | 6/24 | 23/24 | 15/24 | 6/24 |

**Pass condition:** All 12 counts match exactly.  
**Failure action:** If any count mismatches, halt. Investigate whether `classify_output()` was inadvertently changed or whether prompt rendering changed.

### AT-2: Failure taxonomy counts (Cell03)

**Applies to:** Cell03 only  
**Method:** Count `failure_class` across all 96 result records.  
**Expected values:**

| Class | Expected count |
|---|---|
| correct | 50 |
| wrong_chain_selection | 21 |
| non_context_return | 9 |
| target_chain_wrong_neighbor | 12 |
| UNCLASSIFIED_OFF_FRAME | 4 |
| **Total** | **96** |

**Pass condition:** All counts match exactly.

### AT-3: Cell03 composite group gradient

**Applies to:** Cell03 composite query type only  
**Method:** Filter composite results by item_id range. Count is_correct per group.  
**Expected values:**

| Group | Items | Expected correct |
|---|---|---|
| A | i01–i08 | 1/8 |
| B | i09–i16 | 6/8 |
| C | i17–i24 | 8/8 |

**Pass condition:** All three group counts match exactly.

### AT-4: Gate evaluation in output JSON

**Applies to:** All three cells  
**Method:** Read `gate_summary` field from B1 output JSON.  
**Expected values:**

| Cell | gate_1 | gate_2 | gate_5 | stress_eligible |
|---|---|---|---|---|
| Cell01 | PASS | FAIL | PASS | false |
| Cell02 | PASS | FAIL | PASS | false |
| Cell03 | PASS | FAIL | PASS | false |

**Pass condition:** All gate_summary entries match and stress_eligible = false for all three cells.  
**Note on Cell02 hop2 FSF:** Cell02 has one format_scaffold_failure in hop2. Gate 1 threshold is 0 FSF — this item has failure_class='format_scaffold_failure', not scaffold_class='SCAFFOLD_ABSENT'. Confirm gate_1 evaluation correctly reads scaffold_class, not failure_class.

### AT-5: Provenance block completeness

**Applies to:** All three cells  
**Method:** Read `provenance` block from B1 output JSON. Check all required fields are present and non-null.  
**Required fields:**

```
manifest_hash, scorer_hash, validator_hash, runner_hash, tokenizer_hash,
prompt_template_hash, failure_taxonomy_version, model_id, decoding_settings,
axis_configuration, frozen_settings, run_timestamp,
mlx_lm_version, python_version, model_snapshot_hash, precision_rung
```

**Pass condition:** All fields present. No field is None or empty string.

### AT-6: Hash lock verification

**Applies to:** All three cells  
**Method:** Read `provenance.scorer_hash`, `provenance.manifest_hash`, `provenance.runner_hash`, `provenance.tokenizer_hash` from B1 output JSON. Compare to expected values.

| Cell | scorer_hash | manifest_hash | runner_hash | tokenizer_hash |
|---|---|---|---|---|
| Cell01 | sha256:060afad9... | sha256:00a7adf8... | sha256:[B1 runner hash] | sha256:c0382117... |
| Cell02 | sha256:060afad9... | sha256:b81d4716... | sha256:[B1 runner hash] | sha256:c0382117... |
| Cell03 | sha256:b65c6803... | sha256:7d5099cb... | sha256:[B1 runner hash] | sha256:c0382117... |

**Note:** B1 runner hash is TBD until B1 runner is finalized. The runner_hash field in Cell01/02 B1 runs will be the B1 runner hash, not the original runner hashes. This is expected — B1 is a new runner version.

**Pass condition:** scorer_hash and manifest_hash match expected values exactly. tokenizer_hash matches for all three cells. runner_hash is consistent with the B1 runner file hash.

### AT-7: Same-error identity fields present

**Applies to:** All three cells (all 96 items per cell)  
**Method:** Check all per-item result records contain `same_error_identity_key`, `fp16_raw_output`, `exact_output_match`.

**Pass condition:**  
- All 96 records per cell have `same_error_identity_key` field.  
- `same_error_identity_key` format: `"{failure_class}|{scaffold_class}|{format_class}"`  
- `exact_output_match = True` for all items (FP16 base run self-reference).  
- `fp16_raw_output == raw_output` for all items (FP16 base run self-reference).

### AT-8: Dummy baseline counts (Gate 5 reference)

**Applies to:** Cell03 composite results  
**Method:** Sum dummy baseline scores across all 24 composite items.

| Dummy | Expected score | Type |
|---|---|---|
| always_return_first_C | 8/24 | ceiling-bearing |
| always_return_second_C | 8/24 | ceiling-bearing |
| always_return_third_C | 8/24 | ceiling-bearing |
| always_return_last_C | 8/24 | ceiling-bearing |
| always_return_ct | 24/24 | reference-only |
| always_return_NULL | 0/24 | reference-only |

**Pass condition:** All six dummy scores match. Gate 5 max_det (excluding reference-only) = 8/24 < 9/24 threshold.

---

## §4 Acceptance Run Protocol

1. **Lock B1 runner** — confirm hash, file amendment lock note
2. **Dry-run all three cells** — `--dry-run` flag; no model inference; confirm no assertion failures
3. **Run Cell01** — live run; save output JSON with timestamp
4. **Run Cell02** — live run; save output JSON with timestamp
5. **Run Cell03** — live run; save output JSON with timestamp
6. **Run AT-1 through AT-8** against all three output JSONs
7. **File acceptance test results** as `PAPER2-REPRODUCTION-ACCEPTANCE-RESULTS.md` in this governance directory
8. **Report to Senior** with pass/fail summary and full hash table

---

## §5 Acceptance Criteria Summary

The B1 harness passes reproduction acceptance when:

- AT-1: All 12 per-cell accuracy counts match ✓
- AT-2: Cell03 taxonomy counts 96/96 match ✓
- AT-3: Cell03 composite group gradient 1/6/8 confirmed ✓
- AT-4: Gate summaries match (Gate 2 FAIL all cells, stress_eligible=false all cells) ✓
- AT-5: All provenance fields present ✓
- AT-6: Hash locks verified ✓
- AT-7: Same-error identity fields present and correct ✓
- AT-8: Dummy baseline scores match ✓

A single AT failure is a blocking failure. No partial acceptance.

---

## §6 Disposition After Acceptance

When all ATs pass:
- CS files `PAPER2-REPRODUCTION-ACCEPTANCE-RESULTS.md` with per-test results and all output file hashes
- CS reports to Senior: "B1 harness confirmed as Paper 2 reproduction instrument"
- Senior confirms release-consistency for Paper 2 (based on PAPER2-RECOMPUTATION-REPORT.md + acceptance results)
- Manager authorizes Paper 2 freeze tag (see FREEZE-TAG-REPORT.md §4)

If any AT fails:
- CS investigates, identifies root cause, files a bug note in this governance directory
- B1 changes revised
- All ATs re-run from scratch (not just the failing test)

---

— CS Engineer, 2026-06-09
