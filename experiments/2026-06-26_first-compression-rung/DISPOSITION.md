# Disposition — Minimal INT8 Control Rung (2026-06-26)

**Governing object:** `ONE-PAGE-INT8-CONTROL-RUNG-SPEC-v0.1` (sha256 `8b1a2f14…`)
**Authorization:** Manager Decision 2026-06-26 — "Authorize Minimal INT8 Control Rung" (by name).
**Class:** control / calibration rung. **Not** a Claim-C experiment, seam test, composition result, or robustness claim.
**Run dir:** `experiments/2026-06-26_first-compression-rung/`

---

## What was run

One minimal FP16→INT8 control rung on the locked n=8 Two-Hop L1 target (`twohop_l1_c03_i01..i08`), greedy (temp 0.0, max_tokens 16), same prompts/items/scorer for both arms, executed with a byte-identical copy of the locked 2026-06-15 runner. Raw outputs retained for both conditions; FP16-vs-INT8 byte-identity computed.

## Result (measured)

```text
                  hop1     hop2     composite
FP16              0/8      8/8      1/8
INT8              0/8      8/8      1/8

FP16-vs-INT8 raw-output byte-identity: 24/24 generations identical (match_rate 1.0000; zero mismatches)
chat-prompt sha identical across arms:  yes (same prompts)
```

## Readout (allowed control-rung language only)

- The INT8 control rung produced a bounded **hop2-only instrument-validation readout**.
- INT8 produced **no behavioral perturbation in this setup** (FP16 and INT8 generations byte-identical, 24/24).
- The instrument **preserved the fail-closed distinctions** between the readout-eligible query type (hop2) and the unqualified query types (hop1 0/8 and composite 1/8, both logged fail-closed).

## Carried forward unchanged (from the 2026-06-15 disposition)

The hop2 outputs are **single-fact retrieval, NOT chain composition** — legitimate but not load-bearing, and not evidence of two-hop reasoning. The FP16-baseline gate on this target is **CONTAMINATED → INCONCLUSIVE**; this control rung does **not** certify a baseline. Byte-identity is informative about INT8≡FP16 behavior *at this scale, this task, this decoding setting — and only that.*

## What this run does NOT support (forbidden interpretations, restated)

Not: INT8 preserves reasoning · INT8 preserves capability · robust to quantization · composition survived compression · seam tested · Claim C moved · V3 fixed · M5 resolved · INT4 would behave the same. No INT4 was run; no construction redesign occurred; no Claim C / seam / composition claim is made.

— CS Engineer, 2026-06-26
