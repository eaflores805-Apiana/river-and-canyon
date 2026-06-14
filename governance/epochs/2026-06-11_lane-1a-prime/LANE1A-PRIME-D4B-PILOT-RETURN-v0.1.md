# Lane 1a' Prime — D4-B Pilot Return (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
D4-B L01 TOKEN-PRIOR-ACTIVE PILOT — EXECUTED 2026-06-11
SEALED LOCK-RECORD v1.0 UNCHANGED · D4-A RUN-OF-RECORD UNMUTATED
TP CRITERION ACTIVE BY MANAGER DECISION (Q4 authorized; unconditioned_token_prior)
ALL EMITTED REPORTS CARRY TP FIELDS (ACTIVE FORM)
```

To: Manager (decision) · Cc: Team Lead, New Senior Engineer, Senior Engineer
From: CS Engineer
Date: 2026-06-11
Re: Manager §8 24-item return — D4-B L01 token-prior-active pilot completion

D4-B executed under Manager D4-B authorization 2026-06-11 (all four
authorization boxes: model execution + sweep_id creation + L01 sweep +
token-prior generations by name; method
`unconditioned_token_prior` via no-bindings shell). Two-sweep
structure: candidate retrieval-shell + TP control no-bindings shell.

All Manager-required preconditions PASSED at runtime. The patched
TP-banner report emitter (commit `5c60fbd`) carried the symmetric
ACTIVE form across all six emission envelopes. Sealed LOCK-RECORD
unchanged; D4-A run-of-record unmutated.

**Outcome: NOT_RULED_OUT** under the active **six-criterion set**.
Reportable strictly per the non-claim block (§24): "not explained by
the declared shortcut battery."

---

## §1. sweep_id

```text
candidate sweep_id:   lane1a-prime-d4b-cand-20260611-220303-ueitv3
tp control sweep_id:  lane1a-prime-d4b-tp-20260611-220303-bt29ky
```

Both sweep_ids stamped into every D4-B artifact (`pre_flight_log.json`,
`execution_ledger.json`, per-record outputs under
`candidate_outputs/` and `tp_control_outputs/`).

## §2. Commit SHA

```text
HEAD at this filing (pre-commit of D4-B return):
  98d19be30efdfc6bc553f6d31ce3fa3771beda5b

(The commit SHA of this file is recorded after this file is committed.)
```

## §3. Model identity

```text
Family:    Qwen2.5
Variant:   Qwen2.5-3B-Instruct
Precision: bf16 (unquantized; mlx native)
```

(Same model as D4-A; no precision or family axis change.)

## §4. Model snapshot / revision hash

| field | value |
|---|---|
| Authorized canonical | `sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20` |
| Computed at runtime via B1 v2 routine | `sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20` |
| Match | **YES — exact** |

## §5. Local model hash / provenance

```text
HF snapshot directory:
  ~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/snapshots/
  aa8e72537993ba99e69dfaafa59ed015b17504d1/

Same canonical Paper 2 / B1 v2 / D4-A snapshot. No re-staging.
```

## §6. Runner path and sha256

| field | value |
|---|---|
| Runner path | `experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner_d4b.py` |
| sha256 | `88504df4fbbf3a4ffc9e8a7371b31c32bd34bb61ff0c6e468a06be67c25ab42c` |

Supporting files:

| file | sha256 |
|---|---|
| `d4_runner/preconditions_d4b.json` | `e7376ac8e5c2faa1037b7afb3a6b44ca703bd0685299b2efd9116fbb93ccd0c0` |
| `d4_runner/prompt_template_v1.json` (candidate retrieval-shell) | `f1956e7dd43f165c8707fe88bc11757888f108e7e9766aa186ac9fc04f8b368a` |
| `d4_runner/prompt_template_v1_tp.json` (TP no-bindings shell) | `af55f9757005c6cd7c1baa1c77852d4a4bb596f185ceaccfb875ad29f3108615` |
| `d4_runner/decoding_config.json` | `a20391d89972d47c0b231f5c6da9f8a9f4c7be8c975ab98bd95a32327196f803` |
| `d4_runner/parse_model_output.py` | `fbdf989cdb8f258b7b2e18000835aafd9814a195b3eae0d73f540c08d35a1180` |

The D4-A patched runner (`lane1a_runner.py`, sha256 `1d6f7085…`) is the
source of the shared utilities (banner helper, snapshot routine,
pre-flight, sha helpers).

## §7. Framework version

```text
Active authorization pin: mlx_lm 0.31.3 (Option A carryforward from D4-A)
Actual installed:         mlx_lm 0.31.3
Match:                    YES (exact)
mlx companion:            mlx 0.31.2; mlx-metal 0.31.2
```

## §8. Decoding config

```json
{
  "temperature": 0.0,
  "top_p": 1.0,
  "top_k": -1,
  "repetition_penalty": 1.0,
  "max_new_tokens": 32,
  "seed": 0,
  "greedy": true
}
```

Same config used for both sweeps (candidate retrieval-shell + TP
no-bindings shell). One pass per record per sweep.

## §9. Output directory

```text
experiments/2026-06-11_lane-1a-prime/d4_b_pilot/
```

Sealed `validation/` not touched. `d4_a_pilot/` not touched.

## §10. Candidate manifest path and hash

| field | value |
|---|---|
| Pilot manifests | `experiments/2026-06-11_lane-1a-prime/validation/pilot_manifests_L01.json` |
| Pilot sha256 (verified runtime) | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| Final manifests | `experiments/2026-06-11_lane-1a-prime/validation/final_manifests_L01.json` |
| Final sha256 (verified runtime) | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |

Same sealed L01 manifests used by D4-A. Read-only.

## §11. TP control output paths and hashes

96 per-record TP control JSON files at
`experiments/2026-06-11_lane-1a-prime/d4_b_pilot/tp_control_outputs/`.

Consolidated TP control predictions:

| file | sha256 |
|---|---|
| `d4_b_pilot/tp_control_predictions.json` | `3bc7621c7b0bddf142f74b122e5f01259393e1bbb74850e2d741630cac110ee6` |

## §12. Raw candidate output paths and hashes

96 per-record candidate JSON files at
`experiments/2026-06-11_lane-1a-prime/d4_b_pilot/candidate_outputs/`.

Consolidated candidate predictions:

| file | sha256 |
|---|---|
| `d4_b_pilot/candidate_predictions.json` | `ba276b0539a4e7eed6662ea586c94aa0adc6a54ecaa92a0fd5c6540b3d170b76` |

(Note: this file has the same sha256 as the D4-A consolidated candidate
predictions; this is consistent with the model + decoding + manifests
being identical between D4-A and D4-B's candidate sweep — the prompt
template is identical and the model is deterministic at temp 0.)

## §13. Execution ledger path and hash

| field | value |
|---|---|
| Path | `experiments/2026-06-11_lane-1a-prime/d4_b_pilot/execution_ledger.json` |
| sha256 | `d8b8b7a9d75cf026ffd5320b504ed873c7400576291420e3f8cbfe5543df177e` |

The ledger carries the ACTIVE TP banner at the top level and embeds
both sweep_ids, the TP generation method
(`unconditioned_token_prior — no-bindings shell …`), explicit
"no scrambled-binding" confirmation, and the full provenance hash
collection.

## §14. Per-criterion result artifacts and hashes

| artifact | path | sha256 |
|---|---|---|
| T1 report (battery + A6 + candidate + TP summaries; ACTIVE banner) | `d4_b_pilot/t1_report.json` | `03b14a8e37a73f27ac95d703cc170c6aea2647ff8c8ea9cb090933c0d3d5ff59` |
| T3 report (6-criterion vs candidate; TP via measured control; ACTIVE banner) | `d4_b_pilot/t3_report.json` | `6a74ae78a96212edceb096965d9cc5e4d937d3e9fb20fd2322fdad766f57f662` |
| T4 report (INH-1..3 + PH5-1..5 + D4B rows; ACTIVE banner) | `d4_b_pilot/t4_report.json` | `ed723a8fc59baa6111a6d7df70216d50cc056f1bab0ae4e087cfb921eb2ba948` |
| A6 re-verification (ACTIVE banner) | `d4_b_pilot/a6_re_verification.json` | `3538412be4a58eb200009ef4073f9685a3b3c77a5ebfb117ec3b4e69b70991d3` |
| Pre-flight log (ACTIVE banner + run_header) | `d4_b_pilot/pre_flight_log.json` | `69575a72549cc66bb876599d588ff420787eb4b4fa8b79c684971241ede1310d` |
| IVR (D4-B addendum with ACTIVE banner block) | `d4_b_pilot/instrument_validation_report.md` | `70c26b2371e730cac7f3228c0ba8812baf2294833f524f47cc79f5f0783a60a5` |

### T3 per-criterion result table (vs candidate, six active criteria)

| criterion | outcome vs candidate |
|---|---|
| null_abstention_floor_unmet | PASSED |
| answerable_abstention_ceiling_exceeded | PASSED |
| **accuracy_indistinguishable_from_token_prior** | **PASSED (CI upper 0.998 > 0.10 locked margin; does not fire)** |
| accuracy_indistinguishable_from_declared_policy_envelope | PASSED |
| insufficient_measurement_headroom | PASSED |
| strict_content_gap_instability | PASSED |

### Attached elimination labels

```text
attached_labels: []
```

### Candidate per-stratum measurements

```text
n_answerable:               80
candidate_correct:          80
candidate_accuracy:         1.0000
candidate_abstained:        0
candidate_abstention_rate:  0.0000
n_null:                     16
candidate_null_abstained:   16
null_abstention_rate:       1.0000
candidate_parse_failures:   0
candidate_void_rate:        0.0000
```

### TP control (no-bindings shell) measurements

```text
n_answerable:               80
tp_control_correct:         1   (matches gold by chance under prior-only emission)
tp_control_accuracy:        0.0125
tp_control_abstained:       (recorded; not reproduced here)
tp_parse_failures:          0
tp_void_rate:               0.0000
```

### Outcome

```text
outcome: NOT_RULED_OUT under six active criteria
```

## §15. Candidate-vs-token-prior comparison artifacts and hashes

```text
candidate accuracy:            1.0000
tp control accuracy:           0.0125
point difference:              0.9875
Newcombe-Wilson CI on diff:    [0.9159, 0.9978]
locked TP margin:              0.10
TP criterion fires?            NO  (CI upper 0.9978 is NOT < 0.10)
```

This is the key D4-B measurement. The candidate is separated from its
own no-bindings-shell prior emission by a wide margin: the Wilson CI
on the accuracy difference is roughly `[0.92, 1.00]`, comfortably above
the locked 0.10 margin. The criterion's separation logic does NOT fire.

The comparison is materialized in:

| field | location |
|---|---|
| `candidate_vs_tp_comparison` block | `d4_b_pilot/execution_ledger.json` (top level) |
| `candidate_vs_tp_comparison` block | `d4_b_pilot/t3_report.json` (top level) |
| IVR D4-B addendum table | `d4_b_pilot/instrument_validation_report.md` |

(No separate "comparison artifact" file beyond these is emitted; the
comparison lives inside the standard report envelopes.)

## §16. Abort status

```text
abort_triggered: NO
abort_reason:    n/a
elapsed_seconds: 61.4
```

The two-sweep run completed all 192 inferences (96 candidate + 96 TP
control) without abort.

## §17. INCONCLUSIVE status

```text
rung_inconclusive: NO
candidate_void_rate: 0.0000 / 0.05 (budget)
tp_void_rate:        0.0000 / 0.05 (budget)
```

## §18. TP was ACTIVE by Manager decision

**CONFIRMED.** The TP banner ACTIVE form is carried at the top level of
every emitted report:

```json
{
  "tp_criterion_status": "ACTIVE",
  "tp_inactivity_authority": "n/a (Manager authorized TP generations for this run)",
  "tp_generation_status": "RUN (authorized)",
  "tp_elimination_labels_enabled": true
}
```

Authority reference (verbatim from `preconditions_d4b.json`):
`AUTHORIZED — Manager D4-B 2026-06-11 (unconditioned_token_prior method)`.

The TP criterion was evaluated using the MEASURED model TP control
(no-bindings shell), not the analytical 1/26 baseline. The T3 report
`candidate_vs_tp_comparison` block records the exact comparison
arithmetic and Newcombe-Wilson interval.

## §19. All reports carried TP fields

**CONFIRMED.** Verified by inspection at this filing:

| report | top-level `tp_banner` present | banner status |
|---|---|---|
| `pre_flight_log.json` | YES | ACTIVE (enabled=True) |
| `t1_report.json` | YES | ACTIVE (enabled=True) |
| `t3_report.json` | YES | ACTIVE (enabled=True) |
| `t4_report.json` | YES | ACTIVE (enabled=True) |
| `a6_re_verification.json` | YES | ACTIVE (enabled=True) |
| `execution_ledger.json` | YES | ACTIVE (enabled=True) |

All six reports carry all four required TP fields
(`tp_criterion_status`, `tp_inactivity_authority`,
`tp_generation_status`, `tp_elimination_labels_enabled`). The IVR
D4-B addendum additionally renders the four fields as a human-readable
block.

The TP-banner deviation from D4-A does not recur in D4-B — the
future-run emitter fix accepted by Manager at commit `5c60fbd` is now
running in production for this Q2-authorized successor.

## §20. No L02–L08 execution occurred

**CONFIRMED.** D4-B scope strictly L01 only. The two-sweep structure
operates on the same sealed L01 manifests (96 records). No `L02..L08`
manifests were generated; the Reading B generator pin (packet v0.2
§21) was not invoked. Execution ledger records:
`no_l02_l08_execution: "CONFIRMED"`.

## §21. No quantization occurred

**CONFIRMED.** bf16 (unquantized) throughout. Execution ledger:
`no_quantization: "CONFIRMED"`.

## §22. No INT8 / INT4 occurred

**CONFIRMED.** No INT8 / INT4 weights loaded. The runner pointed to
the bf16 HF cache snapshot only. Execution ledger:
`no_int8_or_int4: "CONFIRMED"`.

## §23. Sealed LOCK-RECORD v1.0 remained unchanged

**CONFIRMED.** Re-verified at this filing:

```text
governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md
  expected: 51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  actual:   51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  match:    True
```

The runner verified this hash as a precondition before any model load.
Same hash holds post-run.

**Additionally, D4-A artifacts UNCHANGED (no post-hoc mutation):**
- `d4_a_pilot/t1_report.json` — `ebe0a952…` match
- `d4_a_pilot/t3_report.json` — `a4e0236b…` match
- `d4_a_pilot/execution_ledger.json` — `f75db02c…` match

## §24. Non-claim block (Manager §10 verbatim)

> D4-B is an instrument-use step, not a capability claim. Even if
> D4-B returns NOT_RULED_OUT under six active criteria, it remains
> instrument use, not a capability claim.
>
> D4-B does not establish: model capability, model incapability,
> task-family viability, candidate suitability, certification
> readiness, retention-under-compression, Claim C progress, seam
> evidence, or public benchmark status.
>
> D4-B does not authorize: L02–L08 execution; scrambled-binding
> generations beyond the approved D4-B scope; quantization stress;
> INT8 / INT4; candidate selection; ranking; threshold work;
> certification evaluation; stress-retention testing; Claim C
> activation; public benchmark packaging.
>
> The instrument may rule out; it may not rule in.
>
> Passing the declared battery is reportable only as **"not explained
> by the declared shortcut battery,"** never as "not shortcut-driven."
>
> We have improved the ruler; we are only beginning to touch the
> territory.

---

## Appendix A — Why D4-B's NOT_RULED_OUT is a strictly stronger statement than D4-A's

D4-A returned NOT_RULED_OUT under a **five-criterion set** (TP
INACTIVE by Manager decision; reduced criteria permitted only because
Manager named the decline).

D4-B returns NOT_RULED_OUT under a **six-criterion set** (TP ACTIVE;
measured against the candidate's own no-bindings prior emission).

The added criterion (TP) provides the strongest single-pass test of
whether the candidate's high accuracy is explainable by prior-only
emission. The candidate's measured prior accuracy is 0.0125 (1/80) —
near the analytical 1/26 baseline — while the candidate's
retrieval-shell accuracy is 1.0000. The Newcombe-Wilson interval on
the difference is `[0.9159, 0.9978]`, comfortably outside the locked
0.10 margin.

This means: D4-B's NOT_RULED_OUT is "not explained by the declared
shortcut battery AND not explained by the candidate's measured prior."
Both halves are necessary for D4-B's NOT_RULED_OUT to hold.

This is still **not** a capability claim. The instrument has ruled
out a single class of explanation (declared shortcuts + measured
prior); it has not established candidate capability, certification,
or any positive evidence claim. The bounded language remains binding.

## Appendix B — Required Manager verification path (Manager §9)

```text
1. New Senior performs full G1 byte verification.
2. New Senior recomputes all artifact hashes.
3. New Senior confirms sealed LOCK-RECORD v1.0 unchanged.
4. New Senior audits D4-B constraints from the execution ledger.
5. New Senior confirms TP active by Manager decision.
6. New Senior confirms all reports carried TP fields.
7. New Senior confirms no unauthorized work occurred.
8. Team Lead filters the result.
9. Manager reviews the result.
```

CS does not claim citability for this result. It is filed for the
above verification chain.

## Appendix C — Standing carry (non-authorizations, verbatim)

This D4-B pilot return does not authorize: L02–L08 execution;
scrambled-binding generations beyond the approved D4-B scope;
quantization stress; INT8 / INT4; candidate selection; ranking;
threshold work; certification evaluation; stress-retention testing;
Claim C activation; public benchmark packaging.

All model-touching and sweep-execution gates outside the D4-B scope
remain CLOSED.

**D4 token-prior authorization slot:** authorized by Manager for D4-B
only; remains UNOPENED for any other use; any future TP authorization
is a separate Manager decision.

— CS Engineer, 2026-06-11
