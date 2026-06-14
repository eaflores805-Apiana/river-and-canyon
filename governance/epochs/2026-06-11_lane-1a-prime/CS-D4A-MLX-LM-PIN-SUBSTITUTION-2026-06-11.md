# CS D4-A mlx_lm Pin Substitution (Manager Option A binding)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
SUPPLEMENTAL BINDING ONLY — BINDS MANAGER OPTION A DISPOSITION TO RUNNER
SEALED LOCK-RECORD v1.0 UNCHANGED · D4 TOKEN-PRIOR SLOT: PENDING / UNOPENED
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
```

To: Team Lead · Cc: Manager, New Senior Engineer, Senior Engineer
From: CS Engineer
Date: 2026-06-11
Re: Binding of Manager Option A disposition (mlx_lm pin substitution to 0.31.3)

Per Manager D4-A pre-execution blocker disposition §1, Option A is
**approved**: the authorized framework pin for D4-A is substituted to
**`mlx_lm 0.31.3`**. The prior `0.19.3` value is preserved as
provenance, not as the active run pin.

This memo binds the substitution to the runner authoring step.

---

## §1. Active D4-A framework pin (post-disposition)

| field | value |
|---|---|
| Active authorization pin | **`mlx_lm 0.31.3`** |
| Prior packet pin (provenance only) | `mlx_lm 0.19.3` |
| Verified-null lineage | B1 v2 PROVENANCE 2026-06-10: `0.19.3 → 0.31.3 verified-null for the locked Paper 2 reproduction configuration` |
| Manager authorization for substitution | `Manager Disposition — D4-A Pre-Execution BLOCKER` (2026-06-11) §1 |
| Manager rejection of pip install | Manager §2 — Option B (install 0.19.3) DECLINED |

## §2. Runner contract under the active pin

The D4-A runner uses `0.31.3` as the active authorization pin. The
runner's pre-flight version check refuses to proceed if the running
`mlx_lm` version is not exactly equal to `0.31.3`.

The runner's `preconditions.json` carries:

```json
{
  "authorized_mlx_lm_version": "0.31.3",
  "mlx_lm_version_substitution_authority": "MANAGER-DISPOSITION-D4A-PRE-EXECUTION-BLOCKER-2026-06-11 §1 (Option A)",
  "prior_packet_pin_provenance": "0.19.3 (preserved per Manager §1; not the active pin)",
  "verified_null_lineage": "B1 v2 PROVENANCE 2026-06-10: 0.19.3 → 0.31.3 verified-null for Paper 2 reproduction config"
}
```

## §3. Snapshot-verification routine (Manager §3 approved)

```text
Runner load_model() calls compute_model_snapshot_hash(snapshot_dir),
implementing the B1 v2 routine (sha256 over a sorted manifest of
(relative_path, file_size, per-file_sha256)).

If the computed hash equals
  sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20
the runner proceeds.

If not, the runner aborts and a separate BLOCKER is filed.
```

CS verified at this filing time that the local HF cache
(`~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/
snapshots/aa8e72537993ba99e69dfaafa59ed015b17504d1/`) produces the
canonical hash `abee745b…` under this routine. The runner's runtime
check will re-derive this in-process; this filing-time computation is
recorded for provenance only and is not a substitute for the runtime
check.

## §4. Standing confirmations

- Sealed LOCK-RECORD v1.0 sha256 `51e18fa9…` — UNCHANGED.
- D4 token-prior authorization slot: PENDING / UNOPENED.
- No model invoked. No model loaded. No sweep_id created. No sweep
  execution occurred.

## §5. Standing carry (non-authorizations, verbatim)

This supplemental memo does not authorize: D5 close-out; L02–L08
execution; token-prior model generations; scrambled-binding model
generations; quantization stress; INT8 / INT4; candidate selection;
ranking; threshold work; certification evaluation; stress-retention
testing; Claim C activation; public benchmark packaging.

All model-touching and sweep-execution gates outside the
Manager-authorized D4-A scope remain CLOSED.

— CS Engineer, 2026-06-11
