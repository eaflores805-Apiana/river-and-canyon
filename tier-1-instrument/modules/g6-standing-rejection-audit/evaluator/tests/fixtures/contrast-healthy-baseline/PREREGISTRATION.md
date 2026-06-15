# SYNTHETIC FIXTURE — NOT A REAL RUN

> Hand-crafted contrast fixture used to prove `g6_evaluator_v0_2.py` is not a
> constant function. The fp16_raw_outputs.json + int8_raw_outputs.json in this
> directory contain synthetic generation records designed to DRIVE THE RULES to
> a different output than the real v0.1 run.

This file exists only so the evaluator's `preregistration_exists` check passes
when run against this directory. It records no real preregistration.

**Designed contrast properties:**
- FP16 hop1 high accuracy (≥ 0.50) → rule A passes
- No composite-correct items emit the same token across hop1 and composite → rule B passes
- INT8 differs from FP16 on some items → byte-identity = DIVERGENT

**Expected evaluator output (see expected.json in this directory):**
- baseline_gate.verdict       = PASS
- byte_identity.identity      = DIVERGENT
- construction_task_verdict   = OK
- compression_observation     = DIVERGENCE
- retention_compression_verdict = NO_DROP or DROP (not INCONCLUSIVE)

**Purpose (per TL ACTION 2026-06-15):** prove the evaluator emits different
outputs given different inputs — i.e., it is not just a formatter that prints
the known v0.1 conclusion regardless of input.
