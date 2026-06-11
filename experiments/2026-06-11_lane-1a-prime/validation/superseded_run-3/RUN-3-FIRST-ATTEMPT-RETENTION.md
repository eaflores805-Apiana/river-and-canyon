# Run-3 First-Attempt Retention Block (E11 / PH5-5)

```text
SYNTHETIC / DIAGNOSTIC -- NON-BINDING -- NOT FOR THRESHOLD DERIVATION
RUN-3 FIRST ATTEMPT SUPERSEDED -- RETAINED PER E11 DISCIPLINE
NO MODEL INVOKED · NO SWEEP_ID CREATED · NO SWEEP EXECUTION
```

*CS Engineer, 2026-06-11.*

## Status

The first execution of the corrective run-3 (under the PH5-1 PASS
authorization) is **superseded**, **retained**, and **not erased**. A
CS-side construction bug in `construct_pilot_manifests` (stratum
`gold_in_prefix_neighborhood`) produced an envelope of 0.4875 (39/80)
rather than the deterministic constant 0.60 (48/80) declared in the
PH5-1 lock event. The bug was discovered by CS during run-3 result
verification; the corrected execution (run-3 final; current outputs at
`validation/`) is the canonical authorized run-3 reported to Team Lead.

This retention block honors E11 / PH5-5 discipline: failed pilot
records retained, reason recorded, changed fields enumerated.

## pilot_iteration_count

**4** at this retention filing (run-1, run-2, run-3 attempt 1, run-3
attempt 2). The canonical authorized run-3 = attempt 2 (current
`validation/` outputs).

## reason_for_re-pilot (run-3 attempt 1 → run-3 attempt 2)

Construction-bug discovery: the `gold_in_prefix_neighborhood` stratum
in `construct_pilot_manifests` assigned a random `value_token_ids` to
the prefix-sharing neighbor pair. Per the locked schedule, that
neighbor's value must equal gold so that the
`prefix_neighbor_confusion` shortcut hits the designated stratum at
12/80 = 0.15 by construction.

The bug's symptom was measured at run-3 attempt 1's t1 report:

```text
prefix_neighbor_confusion  answerable  0/80 = 0.0000   (expected 12/80 = 0.15)
salient_endpoint           answerable 15/80 = 0.1875   (expected 12/80 = 0.15;
                                                       3 incidental hits)
recency_excluding_target   answerable 12/80 = 0.1500   ✓
pure_last_position         answerable 24/80 = 0.3000   ✓
union envelope             39/80 = 0.4875              (expected 48/80 = 0.60)
```

The 12-item undercount on `prefix_neighbor_confusion` reduced the
union by 12; the 3 incidental hits on `salient_endpoint` did not
re-enter the union because they coincided with `pure_last_position`
hits on the `gold_at_last_position` stratum (item-disjoint overlap).
Net envelope deficit: 9 items (48 → 39).

Anti-tuning quarantine: this bug discovery is a CS construction
correction, not a bound or verdict change. No locked artifact mutates;
no T3 bound moves; no verdict-table row moves; no recipe schedule
constant moves. The fix is to `construct_pilot_manifests` in
`lane1a_prime/validation.py` only.

## failed_pilot_records_retained

All eight run-3 attempt-1 outputs are preserved in this directory:

| file | sha256 |
|---|---|
| `pilot_manifests_L01.json` | `70aa5e3bed0f54366accdd9a4983e2375319d71a76a0f17a9130035e5d883e79` |
| `final_manifests_L01.json` | `70aa5e3bed0f54366accdd9a4983e2375319d71a76a0f17a9130035e5d883e79` |
| `oracle_validation_results.json` | `92e290f02f3e0e2b11b260fe2c52f0f69509c624502d38b7764d409f3803455f` |
| `t1_report.json` | `d8729b7266f0922d7121edf1b620abcbceff8f09f18b3e614c12149e183dcfd3` |
| `t3_report.json` | `ca6e627cceaa9c70b47e343378d5a29d7511069801733e7190aea59280e843f4` |
| `t4_report.json` | `104ff3d64a05f0228e53a17ae404586bf421716ad5503ed0c62345dca4a44782` |
| `instrument_validation_report.md` | `0e3b5ecfcb4d47d4a6976ee1632b457c8c396fa452a68b9c32ef1d6388e35e2f` |
| `execution_ledger.json` | `558b58a97ede03178ac051ab72446645f0f47c48ff9a306cb43b61883538d6a9` |

Notable: run-3 attempt 1 still produced 12/12 oracle overall_matched
and A6 drift within tolerance — the label-set matching survived the
envelope undercount because the oracle expected-verdicts hold under
the reduced envelope (lower envelope → larger candidate-envelope
difference for shortcuts → ENV still fires; no required-label gets
disabled; no required-absent gets falsely attached). The bug
manifested only at the T1 per-policy / envelope level, which is the
correct discrimination layer for catching it.

## changed_fields_between_pilots (attempt 1 → attempt 2)

| field | attempt 1 | attempt 2 |
|---|---|---|
| `construct_pilot_manifests` stratum 3 neighbor value | random `VALUE_POOL` draw | `gold_token` (set equal to queried_key's binding) |
| stratum 3 slot layout | mixed insertion: `[neighbor, …distractors, queried, …distractors]` (neighbor at position 0) | explicit 5-slot: `[distractor, neighbor, queried, distractor, distractor]` (neighbor at position 1; non-edge) |
| stratum 3 position-4 value | random | forced `non_gold_token` (≠ gold) |
| envelope (measured) | 0.4875 (39/80) | 0.6125 (49/80, vs deterministic 0.60 with one incidental) |
| `prefix_neighbor_confusion` hit-rate | 0/80 | 12/80 |
| `salient_endpoint` hit-rate | 15/80 | 13/80 |
| `pure_last_position` hit-rate | 24/80 | 24/80 (unchanged) |
| `recency_excluding_target` hit-rate | 12/80 | 12/80 (unchanged) |
| `validation.py` sha256 | (pre-fix) | `db69519fe84396e7854f80460b41b60c7aeb1ef06948171b7fd91b4c1860bcac` |
| no locked artifact mutates | (true) | (true) — same three sha256s |

## Relationship to run-1 and run-2 retention

`validation/superseded_run-1/`, `validation/superseded_run-2/`, and
`validation/superseded_run-3/` stand side by side. Their distinct
reasons (run-1: reduced criteria + unlocked verdicts + unstratified
recipe + A6 drift; run-2: provisional bounds + 4-stratum recipe;
run-3 attempt 1: prefix-neighbor stratum construction bug) are
cumulative and auditable.

## Non-claim

This retention block records a CS-discovered construction bug under
the standing E11 / PH5-5 discipline. It does not constitute corrective
re-run re-authorization (the run-3 TL authorization stands; the bug
fix is a CS implementation correction within that authorization), nor
candidate evidence, nor capability evidence, nor certification
evidence, nor threshold support. LOCK-RECORD remains PENDING.

— CS Engineer, 2026-06-11
