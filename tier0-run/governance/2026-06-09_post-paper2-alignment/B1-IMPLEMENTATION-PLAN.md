# B1 File-Level Implementation Plan

**Filed:** 2026-06-09  
**Prepared by:** CS Engineer  
**Status:** FINAL — filed per Team Update 2026-06-09 directive  
**Purpose:** Detailed file-level plan for the B1 harness backfill. Scope: bounded validity-hardening per Team Update approval. No new cells. No new runs. No B or C claims.

---

## §1 Authorization Basis

From Team Update 2026-06-09:

> "B1 harness backfill: approved as bounded validity-hardening. Must include: model_snapshot_hash, mlx_lm_version, python_version, explicit precision_rung, gate_summary JSON, stress_eligible field, runtime fail-closed blocking, same-error identity analysis."

B1 is a hardening pass on the existing runner architecture. It does not introduce new cells, new items, new scoring axes, or new runs. Its sole purpose is to bring the runner provenance and output format up to the standard required for the Paper 2 reproduction acceptance test.

---

## §2 Scope

**In scope:**
- Add missing provenance fields to runner output (model_snapshot_hash, mlx_lm_version, python_version, explicit precision_rung)
- Add gate_summary JSON block to runner output
- Add stress_eligible field to runner output
- Add runtime fail-closed Gate 2 blocking (abort run if gate 2 would fail, per pre-registered thresholds)
- Add same-error identity analysis fields to per-item result records
- Verify all existing hash constants remain correct after changes
- Write unit tests for new fields

**Out of scope:**
- New manifests or items
- New scoring axes or failure classes
- New dummy baselines
- Any B or C claim
- Any new FP16 run
- Any stress (INT8/INT4) run

---

## §3 Gap Analysis — Current Runner vs. B1 Requirement

Reference runner: `runner_twohop_l1_cell03.py` (sha256:f23d99df...)

### Provenance block — current fields

```
manifest_hash, scorer_hash, validator_hash, runner_hash, tokenizer_hash,
prompt_template_hash, failure_taxonomy_version, model_id, decoding_settings,
axis_configuration, frozen_settings, run_timestamp
```

### B1 required additions to provenance block

| Field | Current state | B1 requirement |
|---|---|---|
| `mlx_lm_version` | Not present | Add: `import mlx_lm; mlx_lm.__version__` |
| `python_version` | Not present | Add: `import sys; sys.version` |
| `model_snapshot_hash` | Not present | Add: sha256 over sorted manifest of (relative path, file size, per-file sha256) for all model files in MODEL_DIR. Use the same method as `quant_model_manifest_hash` in Fork A runner |
| `precision_rung` | Implicit (FP16 by construction) | Add explicit string field: `"FP16"` for base runner; `"INT8"` / `"INT4"` for stress runner if/when built |
| `quant_method` | Not present | Add: for FP16 base runner, `"none"`; for stress runner, explicit string describing quantization method (e.g., `"mlx-lm bitsandbytes-style group-quantization, q_bits=8, q_group_size=64, dtype=bfloat16"` for INT8). Must match the description in the quant_config of the quantized model dir. Value is `"none"` for FP16; never omitted or null. |

### Output block — current state

```
{"provenance": {...}, "results": [...]}
```

### B1 required additions to output block

| Field | Current state | B1 requirement |
|---|---|---|
| `gate_summary` | Not present | Add top-level JSON object with per-gate pass/fail and threshold used (see §4.2) |
| `stress_eligible` | Not present | Add boolean field based on gate_summary evaluation |
| `eligibility_reason_code` | Not present | Add string field encoding the reason for stress_eligible value. For PASS: `"GATE2_PASS_HOP1_{n}_COMPOSITE_{n}"`. For FAIL: `"GATE2_FAIL_HOP1_{n}_BELOW_{threshold}"` or `"GATE2_FAIL_COMPOSITE_{n}_BELOW_{threshold}"` or `"GATE2_FAIL_BOTH"`. This gives machine-readable routing information without requiring the reader to parse the full gate_summary. |
| `voided_run_log` | Not present | Add list field. For FP16 base runner: records any items that were excluded from scoring due to infrastructure failures (e.g., empty output, tokenizer error). For stress runner: also records any FP16-reference items that are absent or hash-mismatched. Empty list `[]` when no voids. |
| `comparison_table` | Not present (stress runner only) | For stress runs only: add top-level structured comparison table showing per-precision-rung results in non-collapsing form. Each row is one rung (FP16, INT8, INT4). Columns: precision_rung, pass_count, failure_count, exact_output_agreement, single_failure_ids. Must NOT aggregate INT8 and INT4 into a combined summary row. Each rung is a separate, independently interpretable row. |

### Per-item result — current fields

```
item_id, query_type, prompt_rendered_hash, raw_output, failure_class,
scaffold_class, format_class, returned_token, returned_role, is_correct,
dummy_baselines, [§8 diagnostics]
```

### B1 required additions to per-item result

| Field | Current state | B1 requirement |
|---|---|---|
| `fp16_raw_output` | Not present in two-hop runner | Present in Fork A stress runner; add to base FP16 runner as self-reference (value = raw_output) for compatibility with stress comparison |
| `exact_output_match` | Not present | For FP16 base run: always True (self-reference); for stress run: compare to FP16 reference |
| `same_error_identity_key` | Not present | `f"{failure_class}|{scaffold_class}|{format_class}"` |

**Note on FP16 self-reference fields:** For the base FP16 runner, `fp16_raw_output = raw_output` and `exact_output_match = True` for all items. These fields exist for structural compatibility with the stress runner comparison workflow, not as meaningful comparison data. They should be documented as such in the runner header comment.

### Runtime fail-closed Gate 2 blocking

**Current state:** Gate 2 is evaluated post-hoc by reading the result file. There is no runtime blocker that prevents a run from completing if Gate 2 thresholds are not met.

**B1 requirement:** After all items are scored, before writing the output file, evaluate Gate 2. If Gate 2 fails: (1) write the result file with `stress_eligible: false` and `gate_summary` showing Gate 2 FAIL; (2) print a clear GATE 2 FAIL message; (3) do not suppress the output. The runner must not silently produce a result file that could be mistaken for a stress-eligible cell.

---

## §4 File-Level Changes

### 4.1 Primary file: `runner_twohop_l1_cell03.py`

The Cell03 runner will be the B1 reference implementation. Changes:

**Additions to `provenance` dict (lines ~405–418):**
```python
"mlx_lm_version":   mlx_lm.__version__,
"python_version":   sys.version,
"model_snapshot_hash": compute_model_snapshot_hash(model_dir),
"precision_rung":   "FP16",
```

**New helper function `compute_model_snapshot_hash(model_dir)`:**
- Enumerate all files in model_dir (sorted by relative path)
- Compute per-file sha256
- Build sorted manifest of (relative_path, file_size, sha256)
- Compute sha256 over the sorted manifest string
- Return `"sha256:{hex}"`
- This mirrors the `quant_model_manifest_hash` method from `stress_constructibility_3b.py`

**New function `evaluate_gates(results, axis_config)`:**
- Computes pass/fail for Gate 1 (FSF count), Gate 2 (hop1 and composite thresholds), Gate 5 (max_det threshold)
- Returns a dict: `{"gate_1": {"result": "PASS/FAIL", "fsf_count": n, "threshold": 0}, "gate_2": {...}, "gate_5": {...}}`
- Gate 2 thresholds must be defined as named constants in the runner header, not hardcoded inline

**Gate threshold constants (to be added to runner header):**
```python
GATE2_HOP1_THRESHOLD    = 20  # hop1 correct/24 required for PASS
GATE2_COMPOSITE_THRESHOLD = 20  # composite correct/24 required for PASS
GATE5_MAX_DET_THRESHOLD = 9   # max non-tautological dummy score must be < this
```

These values are pre-registered. They must match the values in `THRESHOLD-PROPOSAL-TWOHOP-L1.md` Rev 2 (approved 2026-06-08, BPE-Jaccard amendment applied).

**Additions to output block:**
```python
output = {
    "provenance":    provenance,
    "gate_summary":  evaluate_gates(all_results, AXIS_CONFIGURATION),
    "stress_eligible": gate_summary["gate_2"]["result"] == "PASS",
    "results":       all_results,
}
```

**Addition to per-item result:**
```python
result_record = {
    ...existing fields...,
    "fp16_raw_output":       raw_output,         # self-reference for FP16 base run
    "exact_output_match":    True,               # always True for FP16 base run
    "same_error_identity_key": f"{failure_class}|{scaffold_class}|{format_class}",
}
```

**Runtime fail-closed block (after all items scored, before file write):**
```python
gate_summary = evaluate_gates(all_results, AXIS_CONFIGURATION)
if gate_summary["gate_2"]["result"] == "FAIL":
    print("\n=== GATE 2 FAIL ===")
    print(f"  hop1:      {gate_summary['gate_2']['hop1_correct']}/24 (threshold {GATE2_HOP1_THRESHOLD})")
    print(f"  composite: {gate_summary['gate_2']['composite_correct']}/24 (threshold {GATE2_COMPOSITE_THRESHOLD})")
    print("  Cell is NOT stress-eligible. Result file will be written with stress_eligible=False.")
    print("  Do not proceed to stress runs.")
```

**New runner hash:** After all changes, compute new sha256 of the amended file. Update `EXPECTED_RUNNER_HASH` constant accordingly. This is the B1 runner hash.

### 4.2 New file: `runner_twohop_l1_b1.py`

If the amendment to `runner_twohop_l1_cell03.py` cannot be done cleanly (e.g., if hash-locked constants make in-place amendment impractical), a new file `runner_twohop_l1_b1.py` will be created as the B1 reference runner. It will be identical to `runner_twohop_l1_cell03.py` except for the changes described in §4.1.

**Decision rule:** Amend in place if the only constant that changes is `EXPECTED_RUNNER_HASH`. Create a new file if any other locked constant (EXPECTED_SCORER_HASH, EXPECTED_MANIFEST_HASH) would need to change for structural reasons.

### 4.3 Unit test additions

The following tests must be added to the test suite (currently in scorer unit test block):

| Test ID | Test | Pass condition |
|---|---|---|
| B1-T1 | provenance block contains mlx_lm_version | Field present and non-empty |
| B1-T2 | provenance block contains python_version | Field present and non-empty |
| B1-T3 | provenance block contains model_snapshot_hash | Field starts with "sha256:" |
| B1-T4 | provenance block contains precision_rung | Field == "FP16" |
| B1-T5 | gate_summary block present in output | Field is dict with gate_1, gate_2, gate_5 keys |
| B1-T6 | stress_eligible is False when Gate 2 FAIL | Computed correctly from gate_summary |
| B1-T7 | per-item same_error_identity_key format | Matches `f"{failure_class}|{scaffold_class}|{format_class}"` |
| B1-T8 | per-item exact_output_match is True for FP16 base run | All items True |
| B1-T9 | compute_model_snapshot_hash is deterministic | Two calls on same dir return same hash |
| B1-T10 | runtime blocker prints GATE 2 FAIL message | Mock items; confirm output message |
| B1-T11 | eligibility_reason_code format — FAIL case | Mock Gate 2 FAIL; confirm code matches `GATE2_FAIL_*` pattern |
| B1-T12 | eligibility_reason_code format — PASS case | Mock Gate 2 PASS; confirm code matches `GATE2_PASS_*` pattern |
| B1-T13 | voided_run_log is present and empty for clean run | All items score normally; voided_run_log == [] |
| B1-T14 | quant_method is "none" for FP16 base run | Field present and equals "none" |

### 4.4 Lock note

After B1 runner is complete and all B1 tests pass:
- Compute sha256 of B1 runner file
- File a runner amendment lock note (similar to `RUNNER-AMENDMENT-LOCK-NOTE-TWOHOP-L1.md`)
- Update `EXPERIMENT_LOG.md` with B1 runner hash
- Tag the commit: `b1-harness-lock-v1.0` (after Manager authorization)

---

## §5 Execution Order

1. Confirm Gate 2 threshold constants from `THRESHOLD-PROPOSAL-TWOHOP-L1.md` Rev 2 — verify exact values
2. Implement `compute_model_snapshot_hash()` helper — test in isolation
3. Implement `evaluate_gates()` function — test against Cell03 result JSON (expected: Gate 2 FAIL, Gate 5 PASS)
4. Amend provenance dict
5. Amend per-item result record (same_error_identity_key, fp16_raw_output, exact_output_match)
6. Amend output block (gate_summary, stress_eligible)
7. Add runtime fail-closed block
8. Run all unit tests (B1-T1 through B1-T10 + all prior regression tests)
9. Compute new runner hash; update `EXPECTED_RUNNER_HASH`
10. Run dry-run pass on Cell03 items to confirm no crashes
11. File runner amendment lock note
12. Update EXPERIMENT_LOG.md

---

## §6 What B1 Does NOT Change

- `scorer_twohop_l1.py` — not amended (no scorer change authorized under B1)
- All manifest files (`items_twohop_l1_cell0*.json`) — not amended
- All result JSON files — not amended or rewritten
- All RESULTS-ALL markdown files — not amended
- Gate thresholds — not changed (must match approved values)
- Failure taxonomy — not changed

---

## §7 Prerequisites for B1 Execution

- [ ] Team Lead confirms Gate 2 threshold values (from THRESHOLD-PROPOSAL-TWOHOP-L1.md Rev 2)
- [ ] Manager authorizes B1 backfill execution (Team Update 2026-06-09 approves "bounded validity-hardening" — confirm this covers code changes)
- [ ] Paper 2 reproduction acceptance test plan (filed separately) reviewed — B1 must satisfy all test plan requirements

---

— CS Engineer, 2026-06-09
