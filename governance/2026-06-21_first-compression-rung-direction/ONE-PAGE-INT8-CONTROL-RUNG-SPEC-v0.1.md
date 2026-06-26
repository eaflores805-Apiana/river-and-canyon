# ONE-PAGE-INT8-CONTROL-RUNG-SPEC-v0.1 (DRAFT)

**From:** Senior Engineer (drafted; model-free; no run performed) → **Authorize:** Manager (by name)
**Date:** 2026-06-26
**Status:** control / calibration rung spec. **Authorizes nothing.** Deliberately short — this is a calibration record, **not** a Claim-C-class experiment and **not** a five-gate authorization packet. It is not iterated after the run.

---

## What this is

One minimal **FP16→INT8 control / calibration rung** to verify the machinery: that it runs FP16→INT8 cleanly, preserves raw outputs, scores correctly, records byte-identity, and **fails closed on unqualified targets**.

**What this is NOT:** not a Claim C experiment · not a seam test · not a composition result · not a robustness claim.

## Run scope

```text
Target     : the locked n=8 Two-Hop L1 set (twohop_l1_c03_i01..i08)
Conditions : FP16  vs  INT8
Decode     : greedy (temperature 0.0, max_tokens 16)
Inputs     : same prompts / items / scorer (pinned below)
Raw outputs: retained for BOTH conditions
Byte-check : FP16-vs-INT8 raw-output byte-identity computed and recorded (required)
```

## Query handling

```text
hop2       : readout-eligible for THIS bounded control only
hop1       : logged, fail-closed
composite  : logged, fail-closed
```

## Allowed result language — the result may say ONLY:

- The INT8 control rung produced a bounded hop2-only instrument-validation readout.
- INT8 produced no behavioral perturbation in this setup.
- The instrument preserved the fail-closed distinctions between readout-eligible and unqualified query types.

## Forbidden result language — do NOT write or imply:

- INT8 preserves reasoning · INT8 preserves capability
- The model is robust to quantization
- Composition survived compression
- The seam was tested
- Claim C moved · V3 is fixed · M5 is resolved
- INT4 would behave the same

## Artifacts to pin (the CS feasibility glance confirms these)

```text
prereg            sha256:3fb4dbd4d8daf19be31e95a395abe65175c5968cd3f1b6d50ac08e0bfd4bed03
scorer            sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde  (Cell03 scorer)
items_file        sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1
prompt_template   sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
FP16 model        Qwen/Qwen2.5-3B-Instruct  (HF cache)
INT8 target       tier0-run/Qwen2.5-3B-Instruct-mlx-int8   (mlx_lm 0.31.3)
```

CS glance = artifacts present · scorer pinned · paths correct · INT8 quantization target available. That is the only review this control needs.

## Governance shape (deliberately short)

- **No** five-gate claim-risk loop.
- **No** C5 review — *unless new claim language is introduced beyond the allowed-language list above.*
- **One** CS feasibility / provenance glance is sufficient (the four checks above).
- After this spec returns, the **Manager may authorize the run directly, by name.**
- **Do not iterate after the run.** Run it once, record the byte-identity, log the readout in the allowed language, stop.

## Boundaries (restated)

No INT4 · no composition claim · no seam claim · no Claim C · no M5 experiment · no V3 retry · no construction redesign. The Path A FP16 K=5 FAIL remains **closed**; the tier0-run remains sealed except for the read of the INT8 target.

## Authorization (not filled by this draft)

```text
Drafted ................ Senior Engineer — no run authorized by this draft
CS feasibility glance .. ____________________  (pending)
Manager run auth (name)  ____________________  (pending)   ← the run begins ONLY here
```

— Senior Engineer
