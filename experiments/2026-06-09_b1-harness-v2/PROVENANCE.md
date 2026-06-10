# PROVENANCE — B1 Harness v2

**Filed:** 2026-06-09

## Locked file hashes (this directory)

```
code/runner_b1_v2.py            sha256:f5be33b34f59925b48e674293ae8d05f894639c49d188b98ddff01bbed00d981
code/structural_proxies.py      sha256:96dd1e0ddfbc27ab34b908a0b6d881738b7d8bb8ee28c90cdca28ebbea49626a
code/test_b1_harness.py         sha256:e81c11c9aab8fd26219a9161dd230aa681f39f2c573aed573f1e9215e644e37c
code/paper2_regression.py       sha256:f9d92350133efbcf9d8ce90438b6b835086d7e83197797e5e91b60d22a6b7248
```

## Inherited file hashes (copies from tier0-run/, hash-verified)

```
code/scorer_twohop_l1.py        sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde
code/tasks_twohop_l1.py         sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
code/prompt_template_twohop_l1.txt
                                sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
manifest/items_twohop_l1_cell03.json
                                sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1
```

All four inherited hashes match the Paper 2 v1.0 Appendix B values. tier0-run/ originals
are untouched. The runner verifies these hashes against the expected values at boot
(`verify_locked_artifacts`).

## Software environment

| Component | Version |
|---|---|
| OS | macOS / Darwin 25.5.0 |
| Python | 3.13.3 |
| mlx_lm (at implementation) | 0.31.3 |
| mlx_lm (Paper 2 lock) | 0.19.3 |

**Version drift note (RETIRED 2026-06-09):** Paper 2 v1.0 was produced with mlx_lm 0.19.3.
The current environment runs 0.31.3. Cross-version drift was a recorded concern at
implementation. The full Paper 2 regression (`paper2_regression.py --mode full`,
2026-06-09) found **96/96 raw_output records bit-identical** to the Paper 2 v1.0
reference (`RESULTS-TWOHOP-L1-cell03-1780948339.json`, sha256 f29783622f...). All gate
decisions matched. The version-drift caveat is therefore retired: mlx_lm 0.19.3 and
0.31.3 produce bit-identical inference for Qwen2.5-3B-Instruct under deterministic
greedy decoding (temp=0.0, max_tokens=16).

## Model snapshot status

| Field | Value |
|---|---|
| model_id | `Qwen/Qwen2.5-3B-Instruct` |
| HuggingFace snapshot (cached) | `aa8e72537993ba99e69dfaafa59ed015b17504d1` |
| Snapshot status | **Asserted only** at this filing; runner-provenance backing produced when `paper2_regression.py --mode live` executes and records `model_snapshot_hash` (computed by `compute_model_snapshot_hash` over the snapshot directory). |
| Locked tokenizer hash | `sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539` |

The Paper 2 v1.0 release record documented the model snapshot as asserted-only with
runner-provenance backing deferred to B1. B1 v2 implements the backing mechanism;
backing is produced on the first live run.

## Authorization chain

```
Manager / Team Lead 2026-06-09:
  "B1 v2 implementation is authorized as bounded validity-harness infrastructure."

Senior conditions C1, C2, C3 incorporated in:
  - code/paper2_regression.py (C1: real regression test)
  - code/runner_b1_v2.py validate_framework_version_agreement (C2: config-vs-sheet)
  - code/runner_b1_v2.py load_threshold_sheet (C3: hash verify before trust)
```

## Test status (updated 2026-06-09 after full regression)

```
B1 unit tests (B1-T1 through B1-T24):    24/24 PASS
Paper 2 regression sanity tests:          2/2 PASS
Subtotal (offline):                       26/26 PASS

Dry-run end-to-end (Paper 2 context):     PASS
Smoke regression (i01 × 4 query types):   PASS (4/4 raw_output bit-identical)
Full regression (96 records):             PASS
  raw_output bit-identical:               96/96
  failure_class match:                    96/96
  is_correct match:                       96/96
  gate decisions match Paper 2 v1.0:      all 7 checks PASS
  v1 shape preservation:                  7/7 checks PASS
  Result artifact: results/RESULTS-B1V2-REGRESSION-full-cell03-1781070929.json
  Output hash:    sha256:c9114c192dbaafc66d85babf6dacc62b9df8e4ffb87886fb868c875a202893f8
```

## Model snapshot — runner-provenance backed (2026-06-09)

| Field | Value |
|---|---|
| HuggingFace snapshot dir | `aa8e72537993ba99e69dfaafa59ed015b17504d1` |
| Computed runner-provenance `model_snapshot_hash` | `sha256:abee745b7dfe399d9254dbcdea5e3e3...` |
| Status at filing | Asserted only |
| Status after full regression | **Runner-provenance-backed** — the asserted-only flag on the model snapshot in the Paper 2 v1.0 release record can be retired |

— CS Engineer, 2026-06-09
