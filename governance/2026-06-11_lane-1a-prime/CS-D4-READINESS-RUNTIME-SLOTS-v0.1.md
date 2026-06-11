# CS D4 Readiness — Runtime / Provenance Slots (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
D4 READINESS SLOT COMPLETION ONLY — NO D4 EXECUTION REQUESTED
SEALED LOCK-RECORD v1.0 UNCHANGED — D4 TOKEN-PRIOR SLOT: PENDING / UNOPENED
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
```

To: Team Lead · Cc: Manager, New Senior Engineer, Senior Engineer
From: CS Engineer
Date: 2026-06-11
Re: TL §6 14-item return — CS provenance/runtime slot completion for the D4 readiness packet

CS completes the 13 runtime / provenance slots Team Lead identified as
open in `LANE1A-PRIME-D4-READINESS-PACKET-v0.1.md` (sha256
`48d93256c49940272339d8da83bc2e56b42abfc048c4eb7798953516d5e2d9ef`).
The 14-item return per TL §6 is consolidated below. No design change
is requested; this memo only fills the slots TL flagged.

One precision-label correction is adopted: **bf16** (TL §1) replaces
the imprecise "FP16" wording in the v0.1 packet. bf16 is the
Apple Silicon / mlx native floating-point representation for the
canonical Paper 2 / B1 v2 unquantized Qwen2.5-3B-Instruct snapshot.

---

## §1. Completed provenance/runtime table

### Model identity and snapshot

| field | value |
|---|---|
| Model family | Qwen2.5 |
| Model variant | Qwen2.5-3B-Instruct |
| Precision rung | **bf16** (per TL §1 correction; supersedes the "FP16" label in v0.1) |
| Local snapshot — model_snapshot_hash (canonical) | `abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20` |
| Local snapshot provenance | B1 v2 lock on `main` (merge commit `3cbfce5`; locked 2026-06-10). Same snapshot Paper 2's full regression reproduced bit-identically (96/96 raw_output match under the locked runner). |
| Snapshot staging path (proposed) | declared at D4 execution time; weights file outside the repo (Lane 1a' Prime sealed surface contains validation artifacts only; no model weights are committed to this repo) |
| Snapshot staging verification | runner computes file-level sha256 over the staged weights at start; refuses to proceed on mismatch (per readiness packet §13 hard stop 5) |

### Inference framework

| field | value |
|---|---|
| Framework | `mlx_lm` |
| Pinned version | declared in `pyproject.toml` / `requirements.txt` at D4 execution time; canonical line per B1 v2 PROVENANCE: `mlx_lm 0.19.3 → 0.31.3 verified-null for the locked Paper 2 reproduction configuration` (Team Lead 2026-06-10) |
| Version-drift policy | runner stamps `mlx_lm_version` into execution_ledger.json; any mismatch with the declared version at run start aborts (per readiness packet §13 hard stop 4) |

### Runner script

| field | value |
|---|---|
| Runner path (proposed) | `experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py` |
| Authoring status | **NOT YET AUTHORED.** Authoring is gated behind Manager D4 execution authorization (per readiness packet §5). |
| Runner sha256 | **TBD at D4 execution authorization.** Will be computed once authored, locked into the D4-A execution ledger and any future D4-A IVR. |
| Runner contract | (a) call `analysis.verify_pre_flight_config` first; (b) load sealed `pilot_manifests_L01.json` (sha256 `afe0e545…`); (c) render prompts via `prompt_template_v1.json`; (d) run inference via `mlx_lm`; (e) parse outputs via `parse_model_output.py`; (f) hand parsed predictions to the existing `_build_measurements_for_predictions` and downstream T3/T4/IVR machinery; (g) re-verify A6 against `final_manifests_L01.json`; (h) emit IVR + execution_ledger labeled SYNTHETIC / DIAGNOSTIC. |

### Decoding parameters (pinned in config)

| parameter | value | rationale |
|---|---|---|
| temperature | `0.0` | deterministic greedy decoding; single-pass requirement (no fan-out) |
| top_p | `1.0` | not in effect at temperature 0; pinned for record completeness |
| top_k | unrestricted (`-1` or framework default) | not in effect at temperature 0 |
| repetition_penalty | `1.0` (no penalty) | preserves token-prior baseline meaningfulness |
| max_new_tokens | `32` | single-value answer + small format margin; truncation = soft stop per §13.7 |
| seed | runner-stamped at start; pinned alongside decoding params in `decoding_config.json` (proposed path: `experiments/2026-06-11_lane-1a-prime/d4_runner/decoding_config.json`) | reproducibility under temperature 0 is decoding-deterministic, but the seed is logged for completeness |
| chat template | Qwen2.5 instruction-tuned chat template (from the locked tokenizer's `chat_template.jinja`) | matches the model's training-time format |
| stop tokens | runner default (EOS); plus declared answer-format terminator if used | per prompt template design |

### Hardware / environment fingerprint plan

```text
execution_ledger.json fields (runner stamps at start):
  - hostname
  - os_release            (e.g., "Darwin 25.5.0")
  - cpu_brand_string      (e.g., "Apple M-series")
  - chip_arch             (e.g., "arm64")
  - python_version
  - mlx_lm_version
  - mlx_core_version
  - sys.platform
  - random_module_seed    (Python random)
  - numpy_seed            (if numpy used)
  - mlx_random_seed       (if mlx random used)

This matches B1 v2 PROVENANCE.md conventions and is the same fingerprint
shape used in the locked Paper 2 reproduction harness.
```

### Manifest generation command + locked seed

```text
command:    python3 experiments/2026-06-11_lane-1a-prime/validation/run_validation.py
seed:       0 (the locked seed per the sealed ManifestRecipe;
             ManifestRecipe(rung_id="L01", seed=0) generates the
             96-record manifests bound by the sealed LOCK-RECORD)
pre-flight: PH5-4 hash verification runs as the first action; aborts
             on any lock-event hash mismatch.
```

The command above produces `pilot_manifests_L01.json` and
`final_manifests_L01.json` byte-identical to the sealed-bound sha256
`afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f`
(PH5-3 identical-seed property).

### Output directory

```text
experiments/2026-06-11_lane-1a-prime/d4_a_pilot/
```

Confirmed per readiness packet §8. Will be created at D4 execution
time; does NOT mutate `validation/` (which remains the sealed
instrument surface).

## §2. All paths and sha256 hashes

### Sealed instrument anchors (unchanged at current HEAD)

| path | sha256 (re-verified at this filing; commit `16dfc90`) |
|---|---|
| `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` | `51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935` |
| `experiments/.../validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5` |
| `experiments/.../validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39` |
| `experiments/.../validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5` |
| `experiments/.../validation/pilot_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| `experiments/.../validation/final_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |

### D4 readiness packet (unchanged)

| path | sha256 |
|---|---|
| `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-D4-READINESS-PACKET-v0.1.md` | `48d93256c49940272339d8da83bc2e56b42abfc048c4eb7798953516d5e2d9ef` |

### Proposed model / runtime (not yet materialized in the repo)

| artifact | path | sha256 |
|---|---|---|
| Model weights | (outside repo; staged at D4 execution time) | `abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20` (canonical snapshot hash) |
| Tokenizer files | (same as snapshot) | computed at D4 execution time over the locked tokenizer files |
| Runner | `experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py` | TBD at authoring |
| Prompt template | `experiments/2026-06-11_lane-1a-prime/d4_runner/prompt_template_v1.json` | TBD at authoring |
| Parser | `experiments/2026-06-11_lane-1a-prime/d4_runner/parse_model_output.py` | TBD at authoring |
| Decoding config | `experiments/2026-06-11_lane-1a-prime/d4_runner/decoding_config.json` | TBD at authoring (carries §1 decoding parameters) |

## §3. Proposed sweep_id, or explicit no-sweep_id request

```text
status:          NOT YET REQUESTED — Manager decision pending (per
                 readiness packet §20 Q1 / sweep_id checkbox).

proposed format: lane1a-prime-d4a-YYYYMMDD-HHMMSS-<random6>
example:         lane1a-prime-d4a-20260612-091500-a7b3c4

creation gate:   explicit Manager authorization (§20 Q1 third item).
authorization status at this filing: NOT YET AUTHORIZED.
```

CS does not request sweep_id creation in this slot-completion memo.
Sweep_id creation, if approved by Manager, would happen at D4 execution
start by the runner. The runner would stamp the sweep_id into the
execution_ledger and every per-record output before any inference runs.

## §4. Proposed output directory

```text
experiments/2026-06-11_lane-1a-prime/d4_a_pilot/
```

Confirmed (re-stated from §1). Sealed `validation/` directory is **not
modified by D4-A**; the sealed surface remains immutable.

## §5. Model identity and snapshot

| field | value |
|---|---|
| identity | Qwen2.5-3B-Instruct (bf16) |
| canonical snapshot hash | `abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20` |
| provenance lineage | B1 v2 lock on `main` (merge commit `3cbfce5`); same snapshot Paper 2's full regression reproduced bit-identically (96/96) under the locked runner |
| staging location | outside repo; runner verifies sha256 over the staged weights at start; refuses on mismatch |

## §6. Runner identity and hash

| field | value |
|---|---|
| runner identity | `lane1a_runner.py` (Lane 1a' Prime D4-A runner) |
| proposed path | `experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py` |
| authoring status | NOT YET AUTHORED — gated behind Manager D4 execution authorization |
| sha256 | TBD at authoring |

Authoring would be CS's deliverable inside the D4 execution work order
if Manager approves the §20 checklist. CS will not author the runner
under this slot-completion memo alone.

## §7. Decoding config

Per §1 above (consolidated here for the slot checklist):

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

The config would be written to
`experiments/2026-06-11_lane-1a-prime/d4_runner/decoding_config.json`
at runner-authoring time; its sha256 would be bound into the D4-A
execution ledger.

## §8. Manifest generation command + seed (re-stated for slot checklist)

```text
command: python3 experiments/2026-06-11_lane-1a-prime/validation/run_validation.py
seed:    0 (locked at sealing event; ManifestRecipe(rung_id="L01", seed=0))
output:  pilot_manifests_L01.json (sha256 afe0e545...)
         final_manifests_L01.json (sha256 afe0e545...)
         pilot == final by construction (PH5-3 identical-seed property)
```

D4-A would NOT re-generate manifests; it would consume the sealed
manifest files at the sealed paths and refuse to proceed if their
sha256s do not match.

## §9. Confirmation: sealed LOCK-RECORD remains unchanged

**CONFIRMED.** Re-verified at this filing by Python sha256:

```text
governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md
  expected: 51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  actual:   51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  match:    True
```

All other sealed-bound artifacts also re-verified at this filing (6/6
pass per the verification table in §2). Sealed instrument state is
byte-identical to the TL-verified state at commit `2b17ed9`.

## §10. Confirmation: no model invoked

**CONFIRMED.** No model was invoked during the assembly of this slot
completion memo, during the readiness packet authoring, or during any
upstream step of the Lane 1a' Prime D1→D2→D3→sealing chain.

## §11. Confirmation: no model loaded

**CONFIRMED.** No model has been loaded into memory at any point.
Source-level model-freeness enforced by `test_validation_source_no_model_imports`
and `test_oracle_cases_source_no_model_imports`.

## §12. Confirmation: no sweep_id was created

**CONFIRMED.** No sweep_id has been created. The §3 format proposal is
a string template only; no identifier was emitted.

## §13. Confirmation: no sweep execution occurred

**CONFIRMED.** No sweep execution occurred. No batched or distributed
candidate generation has been initiated.

## §14. Confirmation: D4 token-prior authorization slot remains PENDING / UNOPENED

**CONFIRMED.** The sealed LOCK-RECORD v1.0 declares the slot PENDING /
UNOPENED; this slot-completion memo does NOT open it. CS recommendation
in the readiness packet §20 was DECLINE on token-prior generations
(analytical 1/26 baseline suffices); the slot remains in its sealed
PENDING / UNOPENED state.

---

## §15. One narrow clarification request to Team Lead

TL §1 referenced "Single pass over the sealed 768-item surface." The
sealed manifest artifacts at the time of D3 acceptance and sealing
cover **rung L01 only** (96 records: 80 answerable + 16 NULL). The
8-rung schedule (L01–L08) is in the locked recipe (768 records if all
rungs were materialized) but only L01 manifests are currently in the
sealed surface.

The v0.1 readiness packet §10/§11 proposed D4-A as a single pass over
the sealed L01 surface (96 records). Two readings of TL §1 are
possible:

```text
Reading A: D4-A is L01 only (96 records), per the v0.1 packet; TL §1
"768-item surface" is a forward framing of the full lane scope (not a
correction to D4-A's scope).

Reading B: D4-A should cover all 8 rungs (768 records). This would
require manifest generation for L02..L08 under the locked recipe + a
new sealing extension to bind those manifests by sha256 before D4-A
could run them.
```

CS's working assumption is **Reading A** (96 records on L01 only) per
the v0.1 packet and the TL "DESIGN SIDE: PASS" disposition. If TL
intended Reading B, CS will need to:

- generate manifests for L02..L08 under the sealed recipe (CS-doable
  under the existing D2 model-free boundary);
- file a supplemental binding memo extending the sealed surface from
  L01-only to L01..L08 (this is a supersession-equivalent event that
  would require fresh Manager authorization, since the sealed
  LOCK-RECORD currently binds L01 manifests only);
- then propose D4-A at 768 items.

CS prefers Reading A for the first model-facing pilot (one rung, fail
fast, one model, one pass); Reading B is available if TL/Manager
prefer the broader first pilot. No design change is required for
Reading A. CS does not act on this clarification within the
slot-completion scope; the readiness packet's §20 checklist binds to
the L01 reading until TL or Manager indicates otherwise.

---

## Appendix A — Standing carry (non-authorizations, verbatim)

This slot-completion memo does not authorize: D4 sweep execution;
D5 close-out; model runs; model loading; new sweep_id; sweep
execution; token-prior model generations; scrambled-binding model
generations; candidate/model outputs; candidate selection; ranking;
threshold work; certification evaluation; stress-retention testing;
Claim C activation; public benchmark packaging.

All model-touching and sweep-execution gates remain CLOSED until
Manager separately approves them by name via the readiness packet
§20 checklist.

**D4 token-prior authorization slot: PENDING / UNOPENED.**

— CS Engineer, 2026-06-11
