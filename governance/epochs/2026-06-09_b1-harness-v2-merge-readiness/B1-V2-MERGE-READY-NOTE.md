# B1 v2 Merge-Ready Note

**Date:** 2026-06-09
**From:** CS Engineer
**To:** Manager (merge decision); Cc: Team Lead, Senior Engineer
**Re:** B1 v2 feature branch `b1-harness-v2` ready for merge consideration
**Status:** Merge readiness reported. Merge decision pending Manager.

---

## Record status

```
Merge-ready notice filed.
Branch: b1-harness-v2 (4 commits ahead of main; +10,764 / -0 net lines)
Last commit on branch: bdf8bb3 (PROVENANCE wording correction per Team Lead 2026-06-09)
Awaiting: Manager merge decision.
No candidate selected. No threshold values set. No runs authorized by this filing.
```

---

## Headline status

**B1 v2 is implementation-complete on the feature branch but is not yet merged, locked,
or released as the active harness state.** Merging brings the harness infrastructure
into main alongside its evidence record (full Paper 2 regression artifact, smoke
artifact, PROVENANCE.md with corroborated snapshot backing). Merging does **not**
activate Paper 3, select a candidate, set thresholds, or authorize any run.

---

## Branch contents (10 new files)

Under `experiments/2026-06-09_b1-harness-v2/`:

| Path | Role |
|---|---|
| `README.md` | What the directory is, layout deviation rationale, quick-start |
| `PROVENANCE.md` | Locked hashes, software environment, model snapshot, test status |
| `code/runner_b1_v2.py` | Single configurable runner (paper2-reproduction / paper3-certification contexts) |
| `code/structural_proxies.py` | D5 substrate — 11 model-free proxies, deterministic |
| `code/test_b1_harness.py` | 24 B1 unit tests + 2 Paper 2 sanity tests |
| `code/paper2_regression.py` | Senior C1 deliverable: real regression test (smoke / full modes) |
| `code/scorer_twohop_l1.py` | Bit-identical copy of tier0-run/ original |
| `code/tasks_twohop_l1.py` | Bit-identical copy of tier0-run/ original |
| `code/prompt_template_twohop_l1.txt` | Bit-identical copy of tier0-run/ original |
| `manifest/items_twohop_l1_cell03.json` | Bit-identical copy of tier0-run/ Cell03 manifest |
| `results/RESULTS-B1V2-REGRESSION-smoke-cell03-1781070595.json` | Smoke regression artifact (i01, 4 query types) |
| `results/RESULTS-B1V2-REGRESSION-full-cell03-1781070929.json` | Full regression artifact (24 items, 96 records) |

The four "inherited" copies match tier0-run/ originals byte-for-byte and are
hash-verified at runner boot (`verify_locked_artifacts`). tier0-run/ is untouched.

---

## Test status (final on branch)

```
B1 unit tests (B1-T01 → B1-T24):              24/24 PASS
Paper 2 reproduction sanity tests:             2/2 PASS
Offline subtotal:                             26/26 PASS

Dry-run end-to-end (Paper 2 context):         PASS
Smoke regression (i01 × 4 query types live):  PASS (4/4 raw_output bit-identical)
Full regression (all 24 items × 4 QT = 96):   PASS
  raw_output bit-identical to Paper 2:        96/96
  failure_class match:                        96/96
  is_correct match:                           96/96
  hop1_correct:                                6/24  (Paper 2 v1.0 ground truth: 6/24)
  hop2_correct:                               23/24  (Paper 2 v1.0 ground truth: 23/24)
  composite_correct:                          15/24  (Paper 2 v1.0 ground truth: 15/24)
  neg_graph_correct:                           6/24  (Paper 2 v1.0 ground truth: 6/24)
  gate_1 status:                              pass   (matches Paper 2 v1.0)
  gate_2 status:                              fail   (matches Paper 2 v1.0)
  stress_eligible:                            False  (matches Paper 2 v1.0)
  v1 output shape preservation checks:        7/7    PASS
```

---

## Senior conditions — verification status

| Condition | Verification | Status |
|---|---|---|
| C1 — Paper 2 regression protection (real regression test, v1-shape preserved, gate decisions bit-identical) | `paper2_regression.py --mode full` reports 96/96 bit-identity and 7/7 shape preservation; full artifact committed | **Satisfied** |
| C2 — `framework_version` config-driven, not hardcoded; validated against locked threshold sheet | `runner_b1_v2.py validate_framework_version_agreement`; B1-T17 tests with arbitrary non-paper3 string (`"arbitrary-test-framework-v9.9"`) | **Satisfied** |
| C3 — Threshold-sheet hash verified BEFORE trusting content | `runner_b1_v2.py load_threshold_sheet` reads bytes, computes hash, raises `ThresholdSheetError` before `json.loads`; B1-T18 verifies | **Satisfied** |

---

## Notable hashes

| Item | Hash |
|---|---|
| Runner (final) | `sha256:7f5efdcbf8a51a9368ee1868be7bcb734fb4ceeedbe580f29f9ff2ac87f90fe6` |
| Structural proxies module | `sha256:96dd1e0ddfbc27ab34b908a0b6d881738b7d8bb8ee28c90cdca28ebbea49626a` |
| Test suite | `sha256:e81c11c9aab8fd26219a9161dd230aa681f39f2c573aed573f1e9215e644e37c` |
| Regression script (final) | `sha256:86d6fe53279ebba214f4c04f462568c631836243b5521c278e529b3f938dc5ee` |
| Full regression output | `sha256:c9114c192dbaafc66d85babf6dacc62b9df8e4ffb87886fb868c875a202893f8` |
| **Model snapshot (runner-provenance-backed)** | **`sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20`** |

The model_snapshot_hash above is the runner-provenance backing of the historically
asserted Paper 2 v1.0 snapshot ID `aa8e72537993ba99e69dfaafa59ed015b17504d1`. Per
Team Lead correction 2026-06-09: this is corroboration of the historical assertion
via behavioral bit-identity, not replacement of the historical asserted-only record.

---

## What merge does (and does not) do

**Merge brings into main:**
- The B1 v2 harness infrastructure as the working substrate for Paper 2 reproduction
  and (when Manager separately authorizes) Paper 3 certification application.
- The full and smoke regression artifacts as the evidence record.
- PROVENANCE.md with the snapshot runner-provenance backing recorded.

**Merge does not:**
- Activate Paper 3 certification or select any candidate.
- Set any threshold value or lock any threshold sheet.
- Authorize any new run, re-run, INT8/INT4 execution, or multi-model execution.
- Modify any tier0-run/ artifact, Paper 2 v1.0 tag, or released Paper 2 manuscript.
- Reactivate Fork A, activate Claim C, or unblock any standing boundary.
- Constitute the Paper 2 release-record addendum commit — that is a separate item
  (see `PAPER2-RELEASE-RECORD-ADDENDUM-01.md`, awaiting Senior's content with CS
  inlining the full 64-character snapshot hash at commit time).

---

## Adjacent CS deliverables (not in this filing)

| Deliverable | Status | Trigger |
|---|---|---|
| B1 v2 merge-ready note (this file) | **Filed** | Now |
| Branch evidence packet | **Filed** | Now (sibling file in this directory) |
| B1 v2 lock note | Pending | Post-merge |
| EXPERIMENT_LOG update | Pending | Post-merge |
| Full hash inlined into PAPER2-RELEASE-RECORD-ADDENDUM-01.md | Pending | When Senior's addendum text reaches CS |

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
