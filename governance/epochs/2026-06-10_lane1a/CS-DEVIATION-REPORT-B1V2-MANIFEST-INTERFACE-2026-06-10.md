# CS Deviation Report — B1 v2 Manifest Interface Incompatibility (PRE-EXECUTION, NO FIRST DATA ACCESS)

From: CS Engineer
To: Elias / Manager
Cc: Team Lead, Senior Engineer
Date: 2026-06-10
Status: Execution STOPPED at deviation discovery; no model load; no first data access; Manager direction required

---

## 0. TL;DR

```text
Manager reauthorization received and acknowledged.
Preflight items 1–13:   PASSED (all 13).
Manifests generated:    8/8 (deterministic; recipe acceptance check
                              passed on every rung; no model call).
B1 v2 manifest interface check: FAIL.
First data access:      NOT EXECUTED (deviation discovered pre-invocation).
Model load:             DID NOT OCCUR.
AUDIT-LOG.ndjson:       still absent (no runner_started events written).
B1 v2 source:           still unedited.
B1 v2.1:                still not present.
```

Per Manager memo §2 ("If any preflight check fails, CS must stop and
report") and §4 item 14 ("Any failure, anomaly, or deviation") — CS
stops execution and files this deviation report before any first data
access.

## 1. What was discovered

The Step-3 production assumed B1 v2 could serve as a generic
deterministic runner for any manifest passed via `--manifest`. That
assumption is incorrect.

**Concrete evidence (read-only inspection):**

| Check | Outcome |
|---|---|
| B1 v2 expected manifest type (`validate_manifest(items: list)` at `tasks_twohop_l1.py:282`) | flat list of items |
| Each item validated by `validate_item()` against a Two-Hop L1 schema with required fields: `item_id`, `chains`, `object_roles`, `queries`, `context`, `positive_sufficiency_exclusion`, `same_context_controls`, `negative_graph_control`, `dummy_baselines`, `cue_balance`, `axis_note`, `axis_note_detail` | Two-Hop L1-specific |
| My Lane 1a manifest shape | nested dict: `{rung_id, rung_spec, items: {answerable: [...], null: [...]}, controls: {answerable_mirror: [...], null_mirror: [...]}, ...}` |
| Each Lane 1a item shape | `{item_id, stratum, in_context_pairs, queried_key, expected_answer, answer_slot_index}` |

The wrapper's subprocess call:

```python
cmd = [sys.executable, str(B1V2_RUNNER), "--mode", "live",
       "--context", "paper2-reproduction", "--framework-version", "none",
       "--manifest", str(manifest_path), ...]
```

would invoke B1 v2, which would execute:

```python
manifest_path = Path(args.manifest)
items = json.loads(manifest_path.read_text())   # gets a dict, not a list
validation = validate_manifest(items)            # iterates dict keys; calls validate_item on strings
```

The B1 v2 process would either crash on the `for item in items:` line
(if `items` is a dict, the iteration yields string keys; `validate_item`
would then fail to call `.get("item_id", ...)` on a string), OR
report `pass_count=0 / total=N_keys` and continue into a no-op
inference path — neither outcome produces meaningful Lane 1a output.

## 2. Why this was not caught earlier

The Step-3 unit test suite (25/25 pass) covers:

- The wrapper's *logic* on synthetic B1-shaped outputs (the
  `_stage_fake_b1_output` test helper writes a small JSON with a
  `context` field; the wrapper byte-preservation and sidecar-only
  tests verify the wrapper's behavior **given** a B1-shaped output).
- It does NOT subprocess the real B1 v2 runner against a Lane 1a
  manifest — that would have been first data access (model load).

The Senior wrapper-rewrite finding caught the attestation pattern.
The B1 v2 manifest-interface mismatch is a separate, earlier
architecture defect: the design packet §1.11 wrote that "all
manifests generated and locked under B1 v2 with hashes" without
specifying that B1 v2's `--manifest` interface is Two-Hop L1 schema-
specific. CS Step-3 production took §1.11 to mean B1 v2 is generic,
which it is not.

This is consistent with the new standing rule "no production cycle
may begin while any condition memo affecting it is G1-open" — there
was an implicit assumption (B1 v2 is generic) that was never
G1-confirmed.

## 3. What this means for the locked artifacts

The current Step-3 artifact set is **structurally correct except at
the B1 v2 invocation boundary**. Specifically:

- Manifest generator, schemas, classification criteria, scorer, dummy
  policies, analyzer, plotter, audit log, sidecar schema, all 25 unit
  tests — all good.
- `lane1a_runner_wrapper.py` `invoke_b1v2()` — needs to invoke a
  Lane-1a-compatible runner instead of B1 v2's Two-Hop L1 runner.
- `runner_config.yaml` — its `b1v2.invocation` block describes flags
  that B1 v2 accepts at the argparse level, but the manifest will not
  validate. The config is wrong about the integration path.
- LOCK-RECORD — locks correct hashes against a wrapper that cannot
  actually invoke production successfully.

## 4. Available remediation paths

CS lists options for Manager / Team Lead / Senior decision. CS does
not act on any of them without authorization.

### Path A — New Lane 1a-specific runner using B1 v2's locked dependencies

Build a new runner (`lane1a_runner.py`) under `experiments/2026-06-10_lane-1a-sweep/`
that:
- Imports `mlx_lm` and the model snapshot pin EXACTLY as B1 v2 does
  (via reading B1 v2's locked module functions, not by editing B1 v2).
- Loads the model via the same routine B1 v2 uses (preserves model
  attestation hash).
- Iterates Lane 1a manifest items and calls `stream_generate()` with
  the locked prompt template, locked decoding flags, locked seed.
- Writes a per-item raw output JSON in the format the analyzer
  already expects.
- The wrapper then calls this runner via subprocess (no B1 v2 CLI
  invocation at all).

**Cost:** ~150 lines of Python; preserves Lane 1a manifest semantics;
preserves model attestation via shared dependency; requires NO edit
to B1 v2 source. **B1 v2.1 not implicated** — this is a separate
sweep runner, not a harness modification.

**Risk:** the model load and decoding code must mirror B1 v2's
behavior exactly; if Senior's later confirmation finds drift, the
sweep would need re-running.

### Path B — Manifest adapter into Two-Hop L1 schema

Write a `lane1a_to_twohop_l1_adapter.py` that translates a Lane 1a
manifest into a "look-alike" Two-Hop L1 manifest with synthetic
chains/queries/etc. Pass the adapted manifest to B1 v2.

**Cost:** moderate; requires inventing dummy field values that satisfy
B1 v2's validator without changing the underlying semantics.

**Risk:** B1 v2 also applies Two-Hop L1 scoring and Two-Hop L1-specific
gate logic. The resulting outputs would carry Two-Hop L1 scoring
artifacts that downstream Lane 1a analyzer would need to strip. This
is the "honest override" anti-pattern at the manifest level — the
output would be wrapper-asserted Two-Hop L1, not Lane 1a-attested.

**CS does NOT recommend Path B.** It violates the spirit of the
sidecar attestation remediation.

### Path C — Edit B1 v2 to accept a Lane 1a manifest schema

NOT AUTHORIZED. B1 v2 is locked at merge `3cbfce57`; B1 v2.1 is
unauthorized. This option is off the table by standing rule.

### Path D — Abandon Lane 1a as designed and redesign as Two-Hop L1

Use Two-Hop L1 cells as the substrate Lane 1a sweeps over. Out of
scope of the current design packet v0.3; would require Senior
re-design.

### CS recommendation

**Path A** is the cleanest. It builds a small runner that preserves
the design intent of "model attestation via the locked B1 v2 stack"
without requiring B1 v2 to consume a non-Two-Hop-L1 manifest. The
new runner becomes one more locked artifact in the Lane 1a packet
(with its own sha256 in LOCK-RECORD).

If Manager approves Path A, the remediation is a step-3 supplement
that:
1. Adds `experiments/2026-06-10_lane-1a-sweep/lane1a_runner.py` (new locked artifact).
2. Updates `lane1a_runner_wrapper.py` to subprocess the new runner
   instead of B1 v2 CLI (small change; preserves sidecar pattern; B1
   v2 source still untouched).
3. Updates `runner_config.yaml` to remove the misleading `b1v2.invocation`
   block.
4. Adds unit tests covering: deterministic generation on synthetic
   manifests; model attestation hash recording; sidecar pattern over
   the new runner's outputs.
5. Re-seals LOCK-RECORD with new hashes.
6. Team Lead combined-review pass on the supplement.
7. Manager re-reauthorization.
8. Preflight + sweep.

## 5. State of every memo §5 return item (deviation point, partial)

Per Manager memo §4, the 14-item post-run return — but execution did
not occur. CS reports state for each item:

| # | Item | State |
|---|---|---|
| 1 | First-data-access timestamp | NOT RECORDED (no first data access) |
| 2 | Confirmation that first data access postdated lock timestamp | n/a |
| 3 | Preflight result | items 1–13 all PASS in the limited interpretation; item-3 expected-vs-actual hash table 19/19 match |
| 4 | Final audit log | `AUDIT-LOG.ndjson` absent; no `runner_started` events |
| 5 | Per-rung result records | none generated |
| 6 | Sweep-level record | none generated |
| 7 | Output artifact hashes | manifests generated and hash-locked; output records were never produced |
| 8 | Test / validation summary | 25/25 unit tests pass; recipe acceptance check pass on all 8 rungs |
| 9 | No re-execution occurred | confirmed (no execution at all) |
| 10 | B1 v2 not edited | confirmed (`git diff` clean) |
| 11 | B1 v2.1 not used | confirmed |
| 12 | Fixed outcome statement emitted | n/a (no execution) |
| 13 | Inconclusive_not_actionable rungs | n/a |
| 14 | **Any failure, anomaly, or deviation** | **THIS REPORT. B1 v2 manifest interface incompatibility discovered pre-invocation.** |

## 6. Recipe-acceptance check result (informational; was generated)

CS generated the 8 Lane 1a manifests under `experiments/2026-06-10_lane-1a-sweep/manifests/`.
This step is offline/deterministic; no model call. The
`RECIPE-ACCEPTANCE-CHECK-RESULTS.json` records all 8 rungs as
`all_pass: true` (every declared dummy policy yields a non-degenerate
prediction vector on every rung's manifest). The 8 manifest hashes
are recorded at `manifests/MANIFEST-HASHES.lock`:

```text
L01: c6d03b1371b3d90b9825ae57ca3e14b71cef0e989028df327aa09f78d1a4e826
L02: fd33a357f46f74c88196e5d4e1694965df5fce6a82ae1dd2a3822fec31c50c7b
L03: 3e3d83fc465fd05a906c33c1732624a959fd3d3bfad09458249314c24bffd5f4
L04: 60398e0382bf890991801ff3f56446d085f7f065699a80fe0d956328e5f9a62b
L05: 3e5feffedb4ac1e62ac951658bc4915e1801b8535a0aafc8bf29c7a21c68730b
L06: 5ec535048c85a2eb42c4f39db6eed62d768a7d53a6b66a76411815a30bd34fc4
L07: f3ef0850288cca765ebb3c27909d86c6a78cd0b7973ea461bf33c3bf0abc9241
L08: b3a83757bb500cb7ae2155294f79cdb2e01ebe84f863df044366dc2bc6cf8001
```

Manifest generator seed: `15532313055991926420` (deterministic from
`sha256("lane-1a-2026-06-10")[0:8]`).

## 7. Open question for Manager / Team Lead / Senior

**Which remediation path should CS pursue?**

CS recommends Path A (new Lane 1a-specific runner using B1 v2's locked
model-loading dependencies). CS will not begin building any
remediation until Manager indicates a path.

## 8. Standing posture

```text
Manager reauthorization issued:        ACKNOWLEDGED
Preflight items 1-13:                  PASSED
Manifest generation:                   COMPLETE (no model call)
B1 v2 manifest interface verification: FAILED (incompatibility found)
First data access:                     NOT EXECUTED
Model load:                            DID NOT OCCUR
Lane 1a sweep:                         NOT EXECUTED
B1 v2 unedited; B1 v2.1 unused:        CONFIRMED
LOCK-RECORD hash (ef170fd7…):          UNCHANGED
Locked artifact hashes:                ALL 19 UNCHANGED
All execution gates:                   CLOSED
```

CS posture: **STOPPED at deviation discovery, awaiting Manager
direction on remediation path.**

— CS Engineer, 2026-06-10
