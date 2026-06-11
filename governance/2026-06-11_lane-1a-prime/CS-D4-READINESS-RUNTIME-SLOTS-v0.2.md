# CS D4 Readiness — Runtime / Provenance Slots (v0.2)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
D4 READINESS SLOT REVISION ONLY — NO D4 EXECUTION REQUESTED
SEALED LOCK-RECORD v1.0 UNCHANGED — D4 TOKEN-PRIOR SLOT: PENDING / UNOPENED
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
```

*v0.2 (post TL §5 + §6 + §7 corrections): exact-version `mlx_lm` pin
(replaces the "0.19.3 → 0.31.3 verified-null" range from v0.1);
unified `d4_a_pilot/` output directory naming throughout; Reading B
generator hash-pin added (cross-referenced from packet v0.2 §21).
All other slots from v0.1 carry forward unchanged.*

To: Team Lead · Cc: Manager, New Senior Engineer, Senior Engineer
From: CS Engineer
Date: 2026-06-11
Re: TL §9 14-item return — CS slot v0.2

---

## §1. Completed provenance/runtime table

### Model identity and snapshot (unchanged from v0.1)

| field | value |
|---|---|
| Model family | Qwen2.5 |
| Model variant | Qwen2.5-3B-Instruct |
| Precision rung | **bf16** |
| Canonical snapshot hash | `abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20` |
| Snapshot provenance | B1 v2 lock on `main` (merge commit `3cbfce5`; locked 2026-06-10) |
| Staging path | outside repo; runner verifies sha256 over staged weights at start |

### Inference framework — EXACT VERSION PIN (TL §5 correction)

| field | value |
|---|---|
| Framework | `mlx_lm` |
| **Authorized version pin (exact)** | **`0.19.3`** |
| Pre-run check | runner stamps the running `mlx_lm` version; if the stamped version is not exactly equal to `0.19.3`, the runner aborts before any model load or inference (readiness §13 hard stop 4) |
| Provenance note (not the pin) | mlx_lm 0.19.3 → 0.31.3 has been verified-null for the locked Paper 2 reproduction configuration (Team Lead 2026-06-10). The verified-null range is recorded for traceability; the authorization PIN is one exact value, per TL §5. Manager may substitute `0.31.3` at authorization; either way, a single exact value will be in effect. |

### Runner script

| field | value |
|---|---|
| Runner path | `experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py` |
| Authoring status | NOT YET AUTHORED — gated behind Manager D4 execution authorization |
| Runner sha256 | TBD at authoring |

### Decoding parameters (unchanged from v0.1)

```json
{
  "temperature": 0.0,
  "top_p": 1.0,
  "top_k": -1,
  "repetition_penalty": 1.0,
  "max_new_tokens": 32,
  "seed": 0,
  "chat_template_source": "tokenizer/chat_template.jinja",
  "stop_tokens": ["<|im_end|>", "<|endoftext|>"]
}
```

### Hardware / environment fingerprint plan (unchanged from v0.1)

10 ledger fields stamped at start: `hostname`, `os_release`,
`cpu_brand_string`, `chip_arch`, `python_version`, `mlx_lm_version`,
`mlx_core_version`, `sys.platform`, `random_module_seed`, `mlx_random_seed`.

### Manifest generation command + locked seed

```text
command:    python3 experiments/2026-06-11_lane-1a-prime/validation/run_validation.py
seed:       0 (locked at sealing event; ManifestRecipe(rung_id="L01", seed=0))
```

Under Reading B (per readiness packet v0.2 §21), per-rung manifest
generation for L02..L08 uses:

```text
command:    python3 -c "from lane1a_prime.validation import
              ManifestRecipe, construct_pilot_manifests
              for rung in ('L02','L03',...,'L08'):
                  recipe = ManifestRecipe(rung_id=rung, seed=0)
                  ... (full snippet in packet v0.2 §21)"
seed:       0 (identical across all rungs L01..L08)
generator path:   experiments/2026-06-11_lane-1a-prime/lane1a_prime/validation.py
generator sha256 at HEAD 17f349e:
                  db69519fe84396e7854f80460b41b60c7aeb1ef06948171b7fd91b4c1860bcac
```

### Output directory — UNIFIED NAMING (TL §6 correction)

```text
experiments/2026-06-11_lane-1a-prime/d4_a_pilot/
```

CS confirms there is NO `sweep_d4a/` reference in this v0.2 memo or in
the packet v0.2. If any prior NS or CS material used `sweep_d4a/`, it
is superseded by `d4_a_pilot/`.

## §2. All paths and sha256 hashes

### Sealed instrument anchors (UNCHANGED at this filing)

| path | sha256 |
|---|---|
| `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` | `51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935` |
| `experiments/.../validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5` |
| `experiments/.../validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39` |
| `experiments/.../validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5` |
| `experiments/.../validation/pilot_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| `experiments/.../validation/final_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |

### Generator pin (Reading B; TL §7 correction)

| field | value |
|---|---|
| Generator path | `experiments/2026-06-11_lane-1a-prime/lane1a_prime/validation.py` |
| Generator sha256 at HEAD `17f349e` | `db69519fe84396e7854f80460b41b60c7aeb1ef06948171b7fd91b4c1860bcac` |
| Locked seed | `0` |
| Generation command | per readiness packet v0.2 §21 (multi-rung loop) |
| Per-rung manifest hashes | TO BE COMPUTED AT GENERATION TIME; written to D4-A execution ledger |

Under Reading A, the generator pin is inactive (sealed L01 manifests
are consumed as-is from the sealed paths).

### D4 readiness packet v0.2

| path | sha256 |
|---|---|
| `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-D4-READINESS-PACKET-v0.2.md` | (computed at commit time; in CS delivery report) |

## §3. Proposed sweep_id

```text
status:          NOT YET REQUESTED — Manager decision pending (packet
                 v0.2 §20 Q1).
proposed format: lane1a-prime-d4a-YYYYMMDD-HHMMSS-<random6>
```

## §4. Proposed output directory

```text
experiments/2026-06-11_lane-1a-prime/d4_a_pilot/
```

(Unified everywhere per TL §6.)

## §5. Model identity and snapshot

Qwen2.5-3B-Instruct, bf16; snapshot
`abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20`.

## §6. Runner identity and hash

`experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py`;
NOT YET AUTHORED; sha256 TBD at authoring.

## §7. Decoding config

Per §1 above (consolidated). Written to
`experiments/2026-06-11_lane-1a-prime/d4_runner/decoding_config.json`
at authoring time.

## §8. Manifest generation command + seed

```text
L01 (sealed): python3 experiments/.../validation/run_validation.py
              seed=0; outputs sha256 afe0e545...

L02..L08 (Reading B; generated at run time):
              Python snippet per packet v0.2 §21; seed=0; generator
              pin db69519f... ; per-rung manifest sha256s recorded at
              generation time.
```

## §9. Confirmation: sealed LOCK-RECORD remains unchanged

**CONFIRMED.** Re-verified at this filing:

```text
governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md
  expected: 51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  actual:   51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  match:    True
```

## §10. Confirmation: no model invoked

**CONFIRMED.**

## §11. Confirmation: no model loaded

**CONFIRMED.**

## §12. Confirmation: no sweep_id created

**CONFIRMED.**

## §13. Confirmation: no sweep execution occurred

**CONFIRMED.**

## §14. Confirmation: D4 token-prior slot remains PENDING / UNOPENED

**CONFIRMED.** The sealed LOCK-RECORD v1.0 declares the slot
PENDING / UNOPENED; this v0.2 slot memo does not open it. CS
recommendation in packet v0.2 §20 Q2 is DECLINE (preserving the slot
in its sealed state). NS recommendation is GRANT. Manager chooses.

---

## Appendix A — Standing carry (non-authorizations, verbatim)

This v0.2 slot memo does not authorize: D4 sweep execution; D5
close-out; model runs; model loading; new sweep_id; sweep execution;
token-prior model generations; scrambled-binding model generations;
candidate/model outputs; candidate selection; ranking; threshold work;
certification evaluation; stress-retention testing; Claim C activation;
public benchmark packaging.

All model-touching and sweep-execution gates remain CLOSED.

**D4 token-prior authorization slot: PENDING / UNOPENED.**

— CS Engineer, 2026-06-11
