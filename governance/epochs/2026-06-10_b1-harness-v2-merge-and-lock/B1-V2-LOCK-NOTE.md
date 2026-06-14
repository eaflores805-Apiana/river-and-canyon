# B1 v2 Lock Note

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Manager (post-merge return); Cc: Team Lead, Senior Engineer
**Re:** B1 v2 harness locked on main; Addendum 01 §5 effectivity activated
**Status:** Locked. Infrastructure only. No protocol authorized.

---

## Record status

```
B1 v2 merged into main: 3cbfce57d42536e8a5e1f35a92c931a03fe4e974
Branch tip merged:      ff8466b2702205e9b9f95458cfe2d9023cb98ccb
Paper 2 v1.0 tag:        unmoved (41c033fc...)
Paper 2 release blob:    unaltered by merge
Addendum 01 §5 effectivity: now active
Boundaries:              all still closed
```

---

## Merge identifiers

| Item | Value |
|---|---|
| Merge commit SHA (`main`) | `3cbfce57d42536e8a5e1f35a92c931a03fe4e974` |
| Merge type | `--no-ff` (explicit merge commit; branch history preserved) |
| Branch merged | `b1-harness-v2` |
| Branch tip at merge | `ff8466b2702205e9b9f95458cfe2d9023cb98ccb` |
| Authorization | Elias / Manager, 2026-06-10 — "Authorization to merge B1 v2 ... Authorized." |

Branch commit lineage absorbed by the merge:

```
1aefc85  B1 v2 harness: initial implementation (24/24 unit tests passing)
e4322b0  B1 v2: smoke regression PASS — i01 bit-identical to Paper 2 reference
2d93ff1  B1 v2: full regression PASS — 96/96 raw_output bit-identical to Paper 2 v1.0
bdf8bb3  B1 v2 PROVENANCE: correct framing per Team Lead 2026-06-09 status correction
ff8466b  PROVENANCE.md mlx_lm canonical wording (Team Lead 2026-06-10)
```

All five commits are now reachable from `main`.

---

## Locked-state hashes (effective at merge)

| Artifact | Hash |
|---|---|
| `experiments/2026-06-09_b1-harness-v2/code/runner_b1_v2.py` | `sha256:7f5efdcbf8a51a9368ee1868be7bcb734fb4ceeedbe580f29f9ff2ac87f90fe6` |
| `experiments/2026-06-09_b1-harness-v2/code/structural_proxies.py` | `sha256:96dd1e0ddfbc27ab34b908a0b6d881738b7d8bb8ee28c90cdca28ebbea49626a` |
| `experiments/2026-06-09_b1-harness-v2/code/test_b1_harness.py` | `sha256:e81c11c9aab8fd26219a9161dd230aa681f39f2c573aed573f1e9215e644e37c` |
| `experiments/2026-06-09_b1-harness-v2/code/paper2_regression.py` | `sha256:86d6fe53279ebba214f4c04f462568c631836243b5521c278e529b3f938dc5ee` |
| `experiments/2026-06-09_b1-harness-v2/code/scorer_twohop_l1.py` | `sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde` (bit-identical to tier0-run/) |
| `experiments/2026-06-09_b1-harness-v2/code/tasks_twohop_l1.py` | `sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b` (bit-identical to tier0-run/) |
| `experiments/2026-06-09_b1-harness-v2/code/prompt_template_twohop_l1.txt` | `sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e` (bit-identical to tier0-run/) |
| `experiments/2026-06-09_b1-harness-v2/manifest/items_twohop_l1_cell03.json` | `sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1` (bit-identical to tier0-run/) |
| Full Paper 2 regression artifact | `sha256:c9114c192dbaafc66d85babf6dacc62b9df8e4ffb87886fb868c875a202893f8` |
| Smoke regression artifact | `sha256:7cc17649a7a20d3bf99c7c9517fe8604a9a537a6cb3baf734d78ff0e71058f39` |
| **Model snapshot (runner-provenance-backed)** | **`sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20`** |

---

## Addendum 01 effectivity activation

`governance/2026-06-09_paper2-v1.0-release/ADDENDUM-01-model-snapshot-backing.md`
contains a §5 clause: *"This addendum takes effect for the release record when B1
v2 is merged and locked."*

Both conditions are met at this commit:
- B1 v2 merged: yes (this commit `3cbfce5`).
- B1 v2 locked: yes (this lock note filed; merge-commit, branch-tip, and full
  hash set recorded above).

The addendum is therefore now **active** for the Paper 2 v1.0 release record. The
model-snapshot status of the v1.0 release is recorded as:

> historically asserted in v1.0;
> subsequently corroborated by B1 runner-provenance-backed bit-identity reproduction;
> release-record addendum committed;
> Paper 2 tag/manuscript unchanged.

(Verbatim from Manager 2026-06-10 authorization memo §"Accepted Paper 2 model
snapshot status".)

The mlx_lm version-drift status is recorded as:

> mlx_lm 0.19.3 → 0.31.3 was verified-null for the locked Paper 2 reproduction
> configuration: same model, tokenizer, prompt path, scorer, manifest,
> deterministic decoding, and reproduction surface. Version drift remains a
> provenance variable for any changed configuration.

(Verbatim from Manager 2026-06-10 authorization memo §"Accepted mlx_lm
version-drift status".)

---

## Paper 3 substrate posture at lock

The B1 v2 runner ships Paper 3 substrate (D6 firewall, A.2 gate_summary schema,
threshold-sheet hash verification, structural_proxies module). It is **config-gated
and disabled by default**:

```
runner_b1_v2.py argparse defaults (from runner source):

  --mode               default="dry-run"
  --context            default="paper2-reproduction"
  --framework-version  default=FRAMEWORK_VERSION_NONE  ("none")
  --threshold-sheet    default=None
  --expected-threshold-sheet-hash  default=None
```

Paper 3 substrate activates only when the operator explicitly passes
`--context paper3-certification` AND provides a locked threshold sheet. Even then,
**activating Paper 3 substrate at runtime is not the same as authorization to apply
Paper 3 certification.** Per all standing memos and the §"Boundaries" block of
this filing, certification application requires separate Manager authorization
beyond the merge.

---

## What this merge does NOT do

- Does not activate Paper 3 certification.
- Does not select a candidate.
- Does not set any threshold value.
- Does not lock any threshold sheet.
- Does not authorize any new model run, re-run, INT8/INT4 execution, or multi-model
  execution.
- Does not introduce any candidate threshold sheet, candidate output, or
  certification result.
- Does not modify any tier0-run/ artifact.
- Does not modify, move, or rewrite the Paper 2 v1.0 tag or released manuscript.
- Does not reactivate Fork A, activate Claim C, or unblock any standing boundary.

---

## CS open board after lock

| Deliverable | Status |
|---|---|
| B1 v2 merge-ready note | Filed (pre-merge) |
| Branch evidence packet | Filed (pre-merge) |
| Paper 2 addendum (full hash + canonical wording) | Filed and corrected (pre-merge) |
| Wording correction report | Filed (pre-merge) |
| **B1 v2 lock note (this file)** | **Filed (post-merge)** |
| EXPERIMENT_LOG.md update | Filed in companion commit |
| Post-merge confirmation report | Filed in companion commit |

No further CS deliverables pending until next authorization arrives.

---

## Boundaries remain closed

```
candidate selection · threshold values · certification evaluation
new model runs · re-runs beyond authorized reproduction validation
unconditioned token-prior runs · activation logging
INT8 / INT4 execution · multi-model execution
Fork A reactivation · Claim C activation
Paper 3 execution as an experiment · Paper 6 activation
public benchmark packaging · artifact mutation
```

---

— CS Engineer, 2026-06-10
