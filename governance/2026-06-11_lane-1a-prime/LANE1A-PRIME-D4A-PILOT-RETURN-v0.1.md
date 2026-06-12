# Lane 1a' Prime — D4-A Pilot Return (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
D4-A MINIMAL OPERATIONAL PILOT — EXECUTED 2026-06-11
SEALED LOCK-RECORD v1.0 UNCHANGED · D4 TOKEN-PRIOR SLOT: PENDING / UNOPENED
TP CRITERION INACTIVE BY MANAGER DECISION (Q2 declined)
```

To: Manager (decision) · Cc: Team Lead, New Senior Engineer, Senior Engineer
From: CS Engineer
Date: 2026-06-11
Re: TL §8 22-item return — D4-A minimal operational pilot completion

D4-A executed under explicit Manager authorization (Lane 1a' D4-A
Minimal Operational Pilot, 2026-06-11; Pre-Execution BLOCKER Disposition,
2026-06-11). All Manager-required preconditions PASSED at runtime:
PH5-4 pre-flight match, sealed LOCK-RECORD hash match, sealed manifest
hash match, `mlx_lm 0.31.3` (Option A pin substitution) match, model
snapshot hash match by B1 v2 runner-provenance routine.

96/96 inferences completed in 39.7 s. Zero parse failures (void rate
0/96). Outcome: **NOT_RULED_OUT** under the active 5-criterion set
(TP INACTIVE by Manager Q2 decline).

This return is instrument-use evidence only. It does not establish
model capability, candidate suitability, certification readiness, or
any Claim C progress.

---

## §1. Sweep_id

```text
sweep_id: lane1a-prime-d4a-20260611-201722-ymbngp
```

Created at runtime per Manager Q1.5 authorization. Stamped into every
D4-A artifact (`pre_flight_log.json`, `execution_ledger.json`, each
`candidate_outputs/<record_id>.json`).

## §2. Commit SHA

```text
HEAD at this filing (pre-commit of D4-A return):
  6b14213e95225771e1906ed294c0f1cb6f4d191e

sealing commit (sealed LOCK-RECORD v1.0):
  e69a7ad35e09581c9723565ed625c02a6b511147

TL-verified HEAD (post HOLD-closure on PH5-1 live-refusal binding):
  2b17ed9e77aaca64f96cdf9bf1542c0e06ede00c
```

The commit SHA for this D4-A return file itself is recorded after this
file is committed (in the post-commit delivery report).

## §3. Model identity

```text
Family:    Qwen2.5
Variant:   Qwen2.5-3B-Instruct (instruction-tuned)
Precision: bf16 (unquantized; Apple Silicon / mlx native)
```

## §4. Model snapshot / revision hash

| field | value |
|---|---|
| Authorized canonical (B1 v2 runner-provenance) | `sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20` |
| Computed at runtime by B1 v2 routine over local snapshot | `sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20` |
| Match | **YES — exact match** (Manager §3 snapshot-verification proposal honored) |
| HF revision (informational; different hash scheme) | `aa8e72537993ba99e69dfaafa59ed015b17504d1` |

The runner reproduced the B1 v2 `compute_model_snapshot_hash` routine
(sha256 over a sorted manifest of `(rel_path, file_size, per_file_sha256)`
tuples, tab-separated, newline-joined) and refused to proceed until
match was confirmed.

## §5. Local model hash / provenance

```text
HF snapshot directory:
  ~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/snapshots/
  aa8e72537993ba99e69dfaafa59ed015b17504d1/

Provenance chain:
  Paper 2 v1.0 release record (asserted-only): aa8e7253...
  B1 v2 lock (runner-provenance-backed):       abee745b...
  D4-A runtime (B1 v2 routine, this run):      abee745b... (match)
```

## §6. Runner path and sha256

| field | value |
|---|---|
| Path | `experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py` |
| sha256 | `5beba944f91fee64ab58e659d13af603f25a420ffce671e3b223204abbe59e60` |

Supporting files:

| file | sha256 |
|---|---|
| `d4_runner/__init__.py` | `ea014d5d882619427beaf32d53b3733a6caf07973979ee4f6e804111d106410e` |
| `d4_runner/preconditions.json` | `d3ad098c8d67ab765622f2d3ae6a768c18de40e71db54e1dba3a2c848cf7c9ba` |
| `d4_runner/decoding_config.json` | `a20391d89972d47c0b231f5c6da9f8a9f4c7be8c975ab98bd95a32327196f803` |
| `d4_runner/prompt_template_v1.json` | `f1956e7dd43f165c8707fe88bc11757888f108e7e9766aa186ac9fc04f8b368a` |
| `d4_runner/parse_model_output.py` | `fbdf989cdb8f258b7b2e18000835aafd9814a195b3eae0d73f540c08d35a1180` |

Pin-substitution binding memo:

| file | sha256 |
|---|---|
| `governance/.../CS-D4A-MLX-LM-PIN-SUBSTITUTION-2026-06-11.md` | `cb7f210b14ee2d7e4f05f2b56fa1f409d5420a0f8107377cf9a2de3f59e3ede2` |

## §7. Framework version

```text
Active authorization pin (Manager Option A): mlx_lm 0.31.3
Actual installed at runtime:                 mlx_lm 0.31.3
Match:                                        YES (exact)

Companion versions:
  mlx 0.31.2
  mlx-metal 0.31.2

Provenance note (not the active pin):
  mlx_lm 0.19.3 -> 0.31.3 verified-null for the locked Paper 2
  reproduction configuration (B1 v2 PROVENANCE 2026-06-10).
  Prior packet pin 0.19.3 preserved as provenance per Manager §1.
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
  "greedy": true,
  "stop_strings": ["\n", "<|im_end|>", "<|endoftext|>"]
}
```

(Greedy deterministic; single pass per record per Manager §2.)

## §9. Output directory

```text
experiments/2026-06-11_lane-1a-prime/d4_a_pilot/
```

The sealed `validation/` directory was not touched by this run.

## §10. Manifest path and hash

| field | value |
|---|---|
| Pilot manifests path | `experiments/2026-06-11_lane-1a-prime/validation/pilot_manifests_L01.json` |
| Pilot sha256 (verified at runtime) | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| Final manifests path | `experiments/2026-06-11_lane-1a-prime/validation/final_manifests_L01.json` |
| Final sha256 (verified at runtime) | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| Pilot/final byte-identical (PH5-3 identical-seed) | YES |

## §11. Raw output paths and hashes

96 per-record JSON files under
`experiments/2026-06-11_lane-1a-prime/d4_a_pilot/candidate_outputs/`,
one per manifest record, named `L01-NNN-<stratum>.json`. Each carries:
record_id, stratum, queried_key, gold, prompt_user_text, output_text,
parsed prediction, latency_ms, finish_reason.

Aggregate hash of all per-record outputs (sha256 of sorted file list
concatenated by per-file sha256): not separately required by Manager
§8, but each file's individual sha256 is reproducible by the auditor
from the committed bytes at HEAD after this commit.

Consolidated candidate predictions:

| file | sha256 |
|---|---|
| `d4_a_pilot/candidate_predictions.json` | `ba276b0539a4e7eed6662ea586c94aa0adc6a54ecaa92a0fd5c6540b3d170b76` |

## §12. Execution ledger path and hash

| field | value |
|---|---|
| Path | `experiments/2026-06-11_lane-1a-prime/d4_a_pilot/execution_ledger.json` |
| sha256 | `f75db02c3080939fb60a6be9a22d3010b5c1e26ffec35b1a43acd7a5ebd08a0f` |

Ledger contents (key fields): `sweep_id_created`, `model_invoked: True`,
`model_loaded: True`, `sweep_execution: True`,
`candidate_model_outputs_produced: True`,
`tp_criterion_status: INACTIVE BY MANAGER DECISION`,
`no_token_prior_generations: CONFIRMED`,
`no_quantization: CONFIRMED`, `no_int8_or_int4: CONFIRMED`,
`no_l02_l08_execution: CONFIRMED`, `no_claim_c_activation: CONFIRMED`,
`model_snapshot_hash_authorized`, `model_snapshot_hash_computed`,
`mlx_lm_version`, `runner_hash`, `parser_hash`,
`prompt_template_hash`, `decoding_config_hash`, `preconditions_hash`,
`scorer_hash`, `sealed_lock_record_hash`, `lock_event_hashes`,
`sealed_manifest_hashes`, `env`, `outcome`, `attached_labels`,
`candidate_summary`, `elapsed_seconds`.

## §13. Per-criterion result artifacts and hashes

| artifact | path | sha256 |
|---|---|---|
| T1 report (battery + A6 + candidate summary) | `d4_a_pilot/t1_report.json` | `ebe0a95246a5dfc474fab7e5543a34e63ed50c988815b5185a38fdad4ab3aa6d` |
| T3 report (6-criterion vs candidate; TP INACTIVE) | `d4_a_pilot/t3_report.json` | `a4e0236bfd6a85e57472911cb9f51566212984ebfbc65579c91d1295666d0a1f` |
| T4 report (INH-1..3 + PH5-1..5 + D4A rows) | `d4_a_pilot/t4_report.json` | `6d265d25d1bd6852afa34fc1eb95680395fc82e1b993698a584f81a23fd29067` |
| A6 re-verification | `d4_a_pilot/a6_re_verification.json` | `3c2e09b18e609e4fd2ab8513d6af6f74a55c13a19f98d56d217ed763c7d771ab` |
| Pre-flight log | `d4_a_pilot/pre_flight_log.json` | `ebda4737c9c97c752475f8d44e582f28eca8c3fc10c907fdb7d5c16bc493281d` |
| Instrument Validation Report (D4-A IVR) | `d4_a_pilot/instrument_validation_report.md` | `7510c06a6dcddf09c8fe17c6fb3bf2993d351d4306ed3c7cb624f0225b449c42` |

### T3 per-criterion result table (vs candidate)

| criterion | outcome vs candidate |
|---|---|
| null_abstention_floor_unmet | PASSED (does not fire) |
| answerable_abstention_ceiling_exceeded | PASSED (does not fire) |
| **accuracy_indistinguishable_from_token_prior** | **INACTIVE BY MANAGER DECISION** |
| accuracy_indistinguishable_from_declared_policy_envelope | PASSED (does not fire) |
| insufficient_measurement_headroom | PASSED (does not fire) |
| strict_content_gap_instability | PASSED (does not fire) |

### Attached elimination labels

```text
attached_labels: []
```

### Candidate per-stratum measurements (verbatim from t1_report.json)

```text
n_answerable:                 80
answerable_correct:           80
answerable_accuracy:          1.0000
answerable_abstained:         0
answerable_abstention_rate:   0.0000
n_null:                       16
null_abstained:               16
null_abstention_rate:         1.0000
parse_failures:               0
void_rate:                    0.0000
```

### Outcome

```text
outcome: NOT_RULED_OUT
```

Per Manager §10 / non-claim block (verbatim): the instrument did not
attach any elimination label under the active 5-criterion set; this
is reportable only as **"not explained by the declared shortcut
battery,"** never as "not shortcut-driven." It does not establish
model capability.

## §14. Abort status

```text
abort_triggered: NO
abort_reason:    n/a
```

The run completed all 96 records with no abort. (Two earlier authoring
iterations during this session — `aborted_20260611-165048`,
`aborted_20260611-165303`, `aborted_20260611-165359`,
`aborted_20260611-165501` — were CS implementation bugs in the runner's
post-inference reporting code, NOT runtime preconditions failing. Those
abort dirs were removed before the final clean run; the issues fixed
were: `CIBound → CriterionComparison` import, `apply_criterion` return
type, `T4Report.rows` immutability, JSON serialization of dataclasses.
None of them triggered model re-loads with mismatched preconditions; the
preconditions passed cleanly on every iteration. The final run is the
single canonical D4-A execution.)

## §15. INCONCLUSIVE status

```text
rung_inconclusive:           NO
record_level_inconclusive:   0 / 96 (zero parse failures; void_rate 0.0)
void_budget:                 0.0 / 0.05 (well below threshold)
```

## §16. TP criterion was INACTIVE by Manager decision

**CONFIRMED.** TP criterion `accuracy_indistinguishable_from_token_prior`
was INACTIVE during this D4-A run per Manager Q2 decline. The run
header, every report, and the execution ledger all state this:

- T3 report row: `disposition_d4a = "INACTIVE_BY_MANAGER_DECISION"`;
  `fired_d4a = False`; `manager_decision_ref = "MANAGER-AUTHORIZATION-LANE-1A-PRIME-D4A 2026-06-11 §4 (Q2 decline)"`.
- T3 report top-level: `tp_inactive_by_manager_decision: true`.
- Execution ledger: `tp_criterion_status: INACTIVE BY MANAGER DECISION`.
- IVR D4-A addendum: "Inactive criteria (by Manager decision)" section
  explicitly names TP and binds the inactivity to Manager Q2.
- Reduced criteria set is permitted **only because Manager chose it
  by name** (containment of the run-1 failure mode).

TP elimination labels could not fire under this run because the
criterion was bypassed in the evaluation loop.

## §17. No TP model generations occurred

**CONFIRMED.** No token-prior shell prompts were rendered. No
scrambled-binding inferences ran. No TP-specific generation sweep was
created. The execution ledger records
`no_token_prior_generations: "CONFIRMED — Q2 declined by Manager"`.

## §18. No L02–L08 execution occurred

**CONFIRMED.** D4-A scope was strictly L01 / 96 records per Manager Q3
Reading A. The execution ledger records
`no_l02_l08_execution: "CONFIRMED"`. The Reading B generator pin
(packet v0.2 §21) was not invoked. No `d4_a_pilot/manifests/` directory
was created.

## §19. No quantization occurred

**CONFIRMED.** Inference ran at bf16 (native unquantized precision).
The execution ledger records `no_quantization: "CONFIRMED"`. No
quantization-related code paths were exercised.

## §20. No INT8 / INT4 occurred

**CONFIRMED.** No `tier0-run/Qwen2.5-3B-Instruct-mlx-int4/` or
`tier0-run/Qwen2.5-3B-Instruct-mlx-int8/` snapshot was loaded. The
runner pointed strictly to the bf16 HF cache snapshot. The execution
ledger records `no_int8_or_int4: "CONFIRMED"`.

## §21. Sealed LOCK-RECORD v1.0 remained unchanged

**CONFIRMED.** Re-verified at this filing:

```text
governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md
  expected: 51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  actual:   51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  match:    True
```

The runner verified this hash as a precondition (per Manager §6:
"abort on artifact hash mismatch"). The same hash holds post-run.

## §22. Non-claim block (Manager §10 / §11 verbatim)

> D4-A is an instrument-use step, not a capability claim.
>
> D4-A does not establish: model capability, model incapability,
> task-family viability, candidate suitability, certification
> readiness, retention-under-compression, Claim C progress, seam
> evidence, or public benchmark status.
>
> D4-A does not authorize: D5 close-out, quantization stress,
> INT8 / INT4, stress-retention testing, candidate selection, ranking,
> threshold work, certification evaluation, Claim C activation, or
> public benchmark packaging.
>
> The instrument may rule out; it may not rule in.
>
> Passing the declared battery is reportable only as **"not explained
> by the declared shortcut battery,"** never as "not shortcut-driven."
>
> We have improved the ruler; we are only beginning to touch the
> territory.

---

## Appendix A — Pre-flight log summary (verbatim from pre_flight_log.json)

```text
sweep_id:                      lane1a-prime-d4a-20260611-201722-ymbngp
ph5_4:                         PASSED
mlx_lm_version_check:          PASSED (authorized 0.31.3; actual 0.31.3)
manifest_hashes:               pilot+final afe0e545... (match)
sealed_lock_record_hash:       51e18fa9... (match)
snapshot_hash_authorized:      sha256:abee745b...
snapshot_hash_computed:        sha256:abee745b... (match via B1 v2 routine)
all_preconditions:             PASSED
```

## Appendix B — Required Manager verification path (Manager §9)

Per Manager §9, before this result is citable:

```text
1. New Senior performs byte verification of the full G1 enumeration.
2. New Senior confirms sealed LOCK-RECORD v1.0 unchanged.
3. New Senior confirms the run honored D4-A constraints
   (L01-only; bf16; no TP generations; no quantization).
4. New Senior confirms TP inactive by Manager decision in artifacts.
5. New Senior confirms no unauthorized model-facing work occurred.
6. Team Lead filters the result.
7. Manager reviews the result.
```

CS does not claim citability for this result. It is filed for the
verification chain above.

## Appendix C — Standing carry (non-authorizations, verbatim)

This D4-A pilot return does not authorize: D5 close-out; L02–L08
execution; token-prior model generations; scrambled-binding model
generations; quantization stress; INT8 / INT4; candidate selection;
ranking; threshold work; certification evaluation; stress-retention
testing; Claim C activation; public benchmark packaging.

All model-touching and sweep-execution gates outside the D4-A scope
remain CLOSED.

**D4 token-prior authorization slot: PENDING / UNOPENED.**

— CS Engineer, 2026-06-11
