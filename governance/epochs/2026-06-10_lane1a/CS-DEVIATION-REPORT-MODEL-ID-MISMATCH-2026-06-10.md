# CS Deviation Report — MODEL_ID Discrepancy Between lane1a_runner.py and B1 v2 (PRE-EXECUTION, NO FIRST DATA ACCESS)

From: CS Engineer
To: Elias / Manager
Cc: Team Lead, Senior Engineer
Date: 2026-06-10
Status: Execution STOPPED at second deviation discovery; no model load; no first data access; Manager direction required

---

## 0. TL;DR

```text
Manager reauthorization received and acknowledged.
LOCK-RECORD touch executed (note + timestamp); post-touch hash:
  88a2a16d889e171e039ed17d477d1cfb96fe2d0ccda6059f0c7bd76c7f2a2025
Lock timestamp finalized: 2026-06-11T02:38:46Z.
Preflight items 1-16: 16/16 PASS.
mlx_lm availability check: OK (mlx_lm 0.31.3).
Model cache inspection: only "Qwen/Qwen2.5-3B-Instruct" is cached.

DEVIATION DISCOVERED:
  B1 v2 MODEL_ID:           "Qwen/Qwen2.5-3B-Instruct"        (cached)
  lane1a_runner MODEL_ID:   "mlx-community/Qwen2.5-3B-Instruct-bf16"
                            (NOT cached; would trigger fresh download
                            of a DIFFERENT model variant)

First data access:       NOT EXECUTED (deviation discovered before invoke)
Model load:              DID NOT OCCUR
AUDIT-LOG.ndjson:        absent (no runner_started events written)
B1 v2 source:            UNEDITED
B1 v2.1:                 NOT CREATED OR USED
Locked artifacts:        UNMODIFIED
```

## 1. The deviation

CS inspected B1 v2's MODEL_ID after preflight PASS:

```python
# experiments/2026-06-09_b1-harness-v2/code/runner_b1_v2.py:92
MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"
```

And the value CS hard-coded in lane1a_runner.py during Path A
production:

```python
# experiments/2026-06-10_lane-1a-sweep/lane1a_runner.py:50
MODEL_ID = "mlx-community/Qwen2.5-3B-Instruct-bf16"
```

The Manager-prescribed wording for Path A is:

> Lane 1a uses a lane-specific runner that preserves B1 v2-compatible
> provenance conventions and locked model-loading dependencies, while
> leaving B1 v2 source unedited.

The "locked model-loading dependencies" interpretation is two-fold:
- **mlx_lm** (the Python package) — same dependency. ✓
- **MODEL_ID** (the specific model the runner loads) — DIVERGED.

Invoking lane1a_runner.py with the current MODEL_ID would either:

- Trigger `mlx_lm.load("mlx-community/Qwen2.5-3B-Instruct-bf16")` to
  download ~6GB of a DIFFERENT model variant (the mlx-community
  pre-converted version). The recorded model snapshot hash would
  then be the mlx-community variant's hash, NOT a value comparable
  to B1 v2's recorded snapshot hash for Paper 2 reproduction.
- Or fail with a network/download error in offline-only environments.

Either outcome breaks the spirit of "B1 v2-compatible provenance
conventions": the snapshot-hash *algorithm* matches B1 v2's, but the
*model the algorithm is applied to* differs from the one B1 v2
attested in Paper 2.

## 2. Why this was not caught earlier

CS Path A production defaulted to the mlx-community variant because
that is the canonical mlx_lm distribution path for Qwen models in
the public mlx ecosystem. CS did not cross-reference B1 v2's locked
MODEL_ID line, which was the authoritative source of truth.

The Path A unit tests verified:
- `test_no_b1v2_imports` — passed (no source imports).
- `test_compute_model_snapshot_hash_signature` — passed on a synthetic
  directory; did NOT exercise the actual MODEL_ID against a cached
  model.

A "MODEL_ID matches B1 v2's MODEL_ID" test would have caught this.
CS did not write that test in Path A production.

This is a second instance of the same pattern as the prior deviation
(B1 v2 manifest interface incompatibility): both arose because CS's
Step-3 / Path A unit tests covered Python-logic invariants on
synthetic inputs but did not cross-reference the actual B1 v2 source
file values.

## 3. State of every other preflight + readiness check

Recorded for completeness (all PASS aside from the deviation):

| # | Check | Result |
|---|---|---|
| 1 | Lock timestamp finalized | PASS (`2026-06-11T02:38:46Z`) |
| 2 | First-data-access > lock timestamp | PASS |
| 3 | All 20 locked artifact hashes match LOCK-RECORD | PASS |
| 4 | B1 v2 source unedited | PASS |
| 5 | B1 v2.1 absent | PASS |
| 6 | lane1a_runner.py is active runner | PASS |
| 7 | No native B1 v2 execution claim | PASS |
| 8 | lane1a_runner validates Lane 1a manifest schema | PASS (all 8 generated manifests validate) |
| 9 | Sidecar pattern active | PASS |
| 10 | Byte preservation (unit-tested) | PASS |
| 11 | Metadata only in sidecar (unit-tested) | PASS |
| 12 | artifact_class const | PASS |
| 13 | certification_relevance const | PASS |
| 14 | framework_version const | PASS |
| 15 | planned_generation_count = 1,536 | PASS |
| 16 | No prior runner_started events | PASS |
| (extra) | mlx_lm importable | PASS (0.31.3) |
| (extra) | MODEL_ID matches B1 v2 MODEL_ID | **FAIL** (`mlx-community/Qwen2.5-3B-Instruct-bf16` ≠ `Qwen/Qwen2.5-3B-Instruct`) |

The literal 16-item Manager preflight passes; the MODEL_ID check is
implicit in the "B1 v2-compatible provenance conventions" spec and was
not literally enumerated by Manager. CS is stopping execution at the
spirit-of-the-spec violation rather than proceeding to first data
access with mismatched MODEL_ID.

## 4. Available remediation paths

### Path A.1 — Fix MODEL_ID in lane1a_runner.py to match B1 v2

Single-line edit in lane1a_runner.py:

```python
MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"   # matches B1 v2 byte-for-byte
```

**Cost:** one-line code change; new lane1a_runner.py sha256; LOCK-RECORD
re-seal; one new unit test (`test_model_id_matches_b1v2`); review
chain replay (Senior intent-preservation + Team Lead + Manager
re-reauthorization).

**Risk:** none beyond the time cost of replaying the review chain.

### Path A.2 — Proceed with current MODEL_ID

Accept that lane1a_runner.py uses the mlx-community variant; record the
divergent snapshot hash in provenance; document the divergence in
LOCK-RECORD and the post-run return. Future cross-comparisons with
Paper 2's recorded model snapshot hash would need an explicit
"different variant" note.

**Cost:** trigger ~6GB download (10-30 minutes) on first invocation;
permanent provenance divergence from B1 v2's recorded value.

**Risk:** Lane 1a outputs are no longer directly comparable to B1 v2
under a clean "same model" claim. The Manager-prescribed wording is
strained.

**CS does NOT recommend Path A.2.** The integration cost of one review
chain replay is dwarfed by the long-term cost of permanent provenance
divergence.

### Path A.3 — Edit B1 v2 to match

NOT AUTHORIZED. B1 v2 is locked at merge `3cbfce57`; B1 v2.1 is
unauthorized. Off the table.

### CS recommendation

**Path A.1** — fix MODEL_ID in lane1a_runner.py to match B1 v2's
`"Qwen/Qwen2.5-3B-Instruct"`; add a unit test that asserts the match;
re-seal LOCK-RECORD; replay Senior + Team Lead + Manager review chain.

If Manager approves Path A.1, the remediation is:
1. Edit lane1a_runner.py line 50 to `MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"`.
2. Add `test_model_id_matches_b1v2` to test_lane1a_packet.py.
3. Re-hash lane1a_runner.py + test_lane1a_packet.py.
4. Re-seal LOCK-RECORD with the new hashes.
5. Senior intent-preservation review (re-verify all prior PASS items
   plus the new MODEL_ID alignment).
6. Team Lead combined adversarial review.
7. Manager reauthorization against the new LOCK-RECORD hash.
8. CS performs lock-finalization touch (timestamp + Manager-approved
   notes).
9. CS preflight (now including the MODEL_ID match check).
10. CS sweep.

## 5. State of every Manager §6 return item (deviation point, partial)

| # | Item | State |
|---|---|---|
| 1 | Final post-touch LOCK-RECORD hash | `88a2a16d…` (recorded; now superseded by the Path A.1 remediation if approved) |
| 2 | Lock timestamp | `2026-06-11T02:38:46Z` (recorded; supersession applies if remediation) |
| 3 | First-data-access timestamp | NOT RECORDED (no first data access) |
| 4 | Confirmation that first data access postdated lock | n/a |
| 5 | Preflight result | 16/16 PASS on Manager's literal list; one CS-side spirit-of-spec deviation surfaced |
| 6 | Final audit log | `AUDIT-LOG.ndjson` absent; no `runner_started` events |
| 7 | Per-rung result records | none generated |
| 8 | Sweep-level record | none generated |
| 9 | Output artifact hashes | manifests already hash-locked at prior commit; raw outputs not generated |
| 10 | Test / validation summary | 35/35 unit tests pass; manifest recipe acceptance pass all rungs |
| 11 | No re-execution occurred | confirmed (no execution at all) |
| 12 | B1 v2 not edited | confirmed (`git diff` clean) |
| 13 | B1 v2.1 not used | confirmed |
| 14 | Fixed outcome statement emitted | n/a (no execution) |
| 15 | Inconclusive_not_actionable rungs | n/a |
| 16 | **Any failure, anomaly, or deviation** | **THIS REPORT. MODEL_ID discrepancy with B1 v2.** |

## 6. Standing review-discipline check

Failure-mode prompt: *How did this pass three review gates (Senior PASS,
Team Lead PASS, CS Path A return) without being caught?*

CS-verified explanation:

- CS did not write a unit test for MODEL_ID alignment in Path A.
- Senior's intent-preservation check verified the architectural
  invariants (no B1 v2 imports; B1 v2-compatible compute_model_snapshot_hash
  algorithm); did not byte-compare MODEL_ID strings.
- Team Lead's combined review accepted Senior's confirmation.
- All three reviewers reasonably assumed "B1 v2-compatible
  model-loading dependencies" implied "same model" — CS's
  implementation interpreted "dependencies" narrowly to mean
  "mlx_lm" only.

**Structural fix going forward:** the new permanent production rule
"no production cycle may begin while any G1-open condition memo
affects it" is necessary but not sufficient. CS should additionally
add a hard rule:

> CS production of any artifact that integrates with a locked sibling
> artifact must include a unit test that cross-references concrete
> values (constants, MODEL_IDs, schema field names) against the
> sibling artifact's source.

CS will propose this addition to the standing review-discipline rule
if Manager / Team Lead concur.

## 7. Standing posture

```text
LOCK-RECORD touch:                        EXECUTED (single authorized touch)
Lock timestamp finalized:                 2026-06-11T02:38:46Z
Post-touch LOCK-RECORD hash:              88a2a16d… (recorded)
Preflight (Manager's literal 16 items):   16/16 PASS
mlx_lm availability:                      PASS (0.31.3)
MODEL_ID match with B1 v2:                FAIL (CS-recommended Path A.1 fix)
First data access:                        NOT EXECUTED
Model load:                               DID NOT OCCUR
B1 v2 unedited; B1 v2.1 unused:           CONFIRMED
All locked artifacts:                     UNMODIFIED
All execution gates:                      CLOSED
```

CS posture: **STOPPED at second deviation discovery, awaiting Manager
direction on Path A.1 vs Path A.2** (CS recommends Path A.1).

— CS Engineer, 2026-06-10
