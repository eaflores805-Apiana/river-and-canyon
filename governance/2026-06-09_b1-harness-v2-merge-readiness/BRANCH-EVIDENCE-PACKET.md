# B1 v2 Branch Evidence Packet

**Date:** 2026-06-09
**From:** CS Engineer
**To:** Manager (merge decision support); Cc: Team Lead, Senior Engineer
**Re:** Detailed evidence supporting the B1 v2 merge-ready note
**Status:** Evidence packet filed alongside `B1-V2-MERGE-READY-NOTE.md` (this directory)

---

## Record status

```
Evidence packet filed.
Branch: b1-harness-v2 at bdf8bb3 (PROVENANCE wording correction)
Branch history below; all four commits pushed to origin.
No runs authorized.
```

---

## Branch commit history

```
bdf8bb3  B1 v2 PROVENANCE: correct framing per Team Lead 2026-06-09 status correction
2d93ff1  B1 v2: full regression PASS — 96/96 raw_output bit-identical to Paper 2 v1.0
e4322b0  B1 v2: smoke regression PASS — i01 bit-identical to Paper 2 reference
1aefc85  B1 v2 harness: initial implementation (24/24 unit tests passing)
```

Net change vs. main: 13 files changed, +10,764 / -0 (the 139-line apparent deletion
in `git diff main..b1-harness-v2` is the scaling-discussion file added to main after
the branch was cut; merge will preserve both sets of changes — no conflict).

---

## Authorization chain

```
Manager / Team Lead memo, 2026-06-09:
  "B1 v2 implementation is authorized as bounded validity-harness infrastructure."

Senior conditions C1, C2, C3: enumerated in the Manager authorization memo and
each verified on branch (see B1-V2-MERGE-READY-NOTE §"Senior conditions").

Team Lead corrected status, 2026-06-09: snapshot wording corrected from "retired"
to "runner-provenance-backed via behavioral bit-identity; snapshot-ID assertion
corroborated, historically asserted." Applied in commit bdf8bb3.
```

---

## File-by-file evidence

### code/runner_b1_v2.py (`sha256:7f5efdcbf8a5...`)

Single configurable runner supporting two operational contexts via `--context`
flag. Provenance, gate evaluation, and per-item record assembly all populated.
Boot sequence:

1. Verify locked artifact hashes (`verify_locked_artifacts`, D6 substrate).
2. (Paper 3 context only) Load threshold sheet with hash verified before
   `json.loads` (`load_threshold_sheet`, Senior C3).
3. (Paper 3 context only) Validate `framework_version` config-vs-sheet
   agreement with no hardcoded literal (`validate_framework_version_agreement`,
   Senior C2).
4. Capture `first_candidate_data_access_timestamp` (D6 firewall substrate).
5. (Paper 3 context only) Enforce data-access firewall
   (`enforce_data_access_firewall`).
6. Load and validate manifest.
7. (Live mode) Load model, compute snapshot hash, verify tokenizer hash.
8. (Live mode) Inference loop with per-item record assembly.
9. Gate evaluation with Paper 3 A.2 schema-compliant per-gate records.
10. Stress eligibility determination, runtime fail-closed block.
11. Output assembly and write.

### code/structural_proxies.py (`sha256:96dd1e0ddfbc...`)

D5 substrate. 11 deterministic, model-free proxy functions:
`token_length`, `context_window_utilization`, `graph_distance`, `number_of_hops`,
`number_of_keys`, `nesting_depth`, `distractor_count`, `distractor_entropy`,
`answer_position_distribution`, `token_prefix_overlap`, `null_non_null_balance`.

Functions are pure (B1-T24 verifies determinism across repeated calls).

No candidate-specific calling convention — Paper 3 candidate's
`D5_structural_difficulty_proxies` field will declare which proxies are computed
when a candidate is eventually authorized.

### code/test_b1_harness.py (`sha256:e81c11c9aab8...`)

26 tests total: 24 B1-coded (B1-T01 → B1-T24) plus 2 Paper 2 sanity tests. Tests
run offline; no model load. Coverage:

```
B1-T01  mlx_lm_version slot present in provenance
B1-T02  python_version populated from sys.version
B1-T03  model_snapshot_hash returns sha256:... format
B1-T04  precision_rung == "FP16" for FP16 base run
B1-T05  gate_summary has gate_1, gate_2, gate_5 keys
B1-T06  stress_eligible False when Gate 2 fails
B1-T07  same_error_identity_key format = "{fc}|{sc}|{fc}"
B1-T08  exact_output_match True for FP16 base run
B1-T09  compute_model_snapshot_hash deterministic
B1-T10  runtime fail-closed prints STRESS-ELIGIBILITY FAIL
B1-T11  eligibility_reason_code FAIL pattern
B1-T12  eligibility_reason_code PASS pattern
B1-T13  voided_run_log present and empty for clean run
B1-T14  quant_method == "none" for FP16 base run
B1-T15  analysis_script_hash present, starts with sha256:
B1-T16  first_candidate_data_access_timestamp is ISO-8601 UTC
B1-T17  framework_version config-vs-sheet (NOT hardcoded literal) [Senior C2]
B1-T18  threshold-sheet hash verified BEFORE trust [Senior C3]
B1-T19  gate_record has all 13 A.2 schema fields
B1-T20  short_circuit field set correctly
B1-T21  firewall rejects pre-lock data access
B1-T22  firewall passes when access postdates lock
B1-T23  hash registry rejects mismatched artifacts
B1-T24  structural_proxies functions are deterministic
```

All 26 tests PASS on commit bdf8bb3. Reproducible with:
```
cd experiments/2026-06-09_b1-harness-v2/code
python3 test_b1_harness.py
```

### code/paper2_regression.py (`sha256:86d6fe53279e...`)

Senior C1 deliverable. Two modes:

**`--mode smoke`**: 1 item × 4 query types (twohop_l1_c03_i01). Validates model
loads, mlx_lm functional, single inference completes, v1 shape preserved. Run
2026-06-09: PASS, with 4/4 raw_output bit-identical to Paper 2 reference for i01.

**`--mode full`**: all 24 items × 4 query types (96 inferences). Validates v1 shape
preservation AND gate decision bit-identity against Paper 2 v1.0 ground truth.
Run 2026-06-09: PASS, with 96/96 raw_output bit-identical, all gate decisions
matching, v1 shape 7/7 PASS.

Reference loaded with hash verification:
- Path: `tier0-run/RESULTS-TWOHOP-L1-cell03-1780948339.json`
- Expected: `sha256:f29783622fb14caca1c2a5829da8b874836add5d111356ea42be1f7d4a7b73f7`
- Status: matched

### Inherited foundation files (bit-identical copies; runtime hash-verified)

| File | Hash | Source |
|---|---|---|
| `code/scorer_twohop_l1.py` | `sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde` | tier0-run/ |
| `code/tasks_twohop_l1.py` | `sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b` | tier0-run/ |
| `code/prompt_template_twohop_l1.txt` | `sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e` | tier0-run/ |
| `manifest/items_twohop_l1_cell03.json` | `sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1` | tier0-run/ |

All four match Paper 2 v1.0 Appendix B values. tier0-run/ originals untouched
(seal preserved).

---

## Regression result artifacts

```
experiments/2026-06-09_b1-harness-v2/results/RESULTS-B1V2-REGRESSION-smoke-cell03-1781070595.json
  Hash:     sha256:7cc17649a7a20d3bf99c7c9517fe8604a9a537a6cb3baf734d78ff0e71058f39
  Records:  4 (item i01, 4 query types)
  Result:   4/4 raw_output bit-identical to Paper 2 reference

experiments/2026-06-09_b1-harness-v2/results/RESULTS-B1V2-REGRESSION-full-cell03-1781070929.json
  Hash:     sha256:c9114c192dbaafc66d85babf6dacc62b9df8e4ffb87886fb868c875a202893f8
  Records:  96 (all 24 items × 4 query types)
  Result:   96/96 raw_output bit-identical to Paper 2 reference
  Gates:    All 7 gate-decision checks match Paper 2 v1.0 ground truth
```

Both artifacts carry the runner-provenance-backed model_snapshot_hash
`sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20`.

---

## Software environment at evidence collection

```
OS:                Darwin 25.5.0 (macOS, Apple Silicon)
Python:            3.13.3
mlx_lm:            0.31.3
Model:             Qwen/Qwen2.5-3B-Instruct
Snapshot dir ID:   aa8e72537993ba99e69dfaafa59ed015b17504d1
                   (HuggingFace cache; matches Paper 2 v1.0 historical assertion)
Decoding:          greedy, temp=0.0, max_tokens=16 (matches Paper 2 v1.0 lock)
```

Cross-version bit-identity (0.19.3 → 0.31.3) verified within this scope only; not
generalized to other models, decoding configurations, or future mlx_lm versions.

---

## What this packet does NOT include

By design — these are separate or downstream items:

- **B1 v2 lock note.** Pending; filed after Manager merges.
- **EXPERIMENT_LOG update.** Pending; filed after Manager merges.
- **Paper 2 release-record addendum.** Senior-authored; awaiting CS inlining of the
  full 64-character snapshot hash at commit time. Separate item per Team Lead status
  board.
- **Any candidate-specific certification artifact.** No candidate selected.
- **Any threshold sheet.** None locked.
- **Any stress run.** None authorized.

---

## Non-authorizations (carried forward)

```
candidate selection · threshold values · certification evaluation
new runs · re-runs beyond authorized reproduction validation
unconditioned token-prior runs · activation logging
INT8 / INT4 execution · multi-model execution
Fork A reactivation · Claim C activation
Paper 3 execution as an experiment · Paper 6 activation
public benchmark packaging · artifact mutation
```

---

— CS Engineer, 2026-06-09
