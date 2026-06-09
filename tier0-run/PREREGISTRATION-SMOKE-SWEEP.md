# Pre-Registration: Tier 0 Smoke Sweep

*Locked before results. Do not modify after the run starts.*
*Date: 2026-06-06*

---

## Run type

Tier 0 smoke sweep — pipeline behavior check under bit-depth stress.
Not the final Tier 0 result. Five pairs is enough to answer one question:

> Does the harness produce interpretable retention and error-identity output across bit depths?

---

## Eligible pairs

| Pair | Cell | FP16 narrow baseline | Status |
|---|---|---|---|
| P02R | compositional_low_support | 1.0 | eligible for ΔR |
| P03 | compositional_low_support | 1.0 | eligible for ΔR |
| P04 | compositional_low_support | 1.0 | eligible for ΔR |
| P05 | atomic_low_shortcut (clean control) | 1.0 | eligible for ΔR |
| P06 | atomic_high_shortcut (shortcut probe) | 1.0 | eligible for ΔR |

## Excluded from ΔR

| Pair | Reason |
|---|---|
| P01R | FP16 narrow baseline = 0. Both component hops pass; composite fails before stress. Classification: **baseline seam failure / capability floor**. Not compression-fragility. Sits in diagnostic section only. Do not include in ΔR denominator. |

---

## Run configuration

```
Model:               Qwen/Qwen2.5-7B-Instruct
Bit depths:          16, 8, 4
Quantization source: each rung loaded fresh from original FP16 weights (no cascading)
Calibration label:   code
Decoding:            temperature = 0.0 (deterministic)
Max tokens:          256
```

---

## Primary predictions (declared before results)

1. **Compositional arms (P02R, P03, P04 narrow) will degrade more than their matched broad arms under INT8 and INT4.**
2. **Atomic clean control (P05) will remain stable across all rungs.** If P05 fails, the instrument is leaking — not signal.
3. **P06 narrow may flip under INT4.** If it does and the error matches the label-shortcut answer, that is a robust-wrong candidate. If it stays correct, the shortcut probe simply did not trigger under this stress level.

---

## Outcome classification (pre-declared)

| Pattern | Classification |
|---|---|
| All valid pairs stay correct through INT4 | Good pipeline / no signal. Tasks may be too easy or model robust at this stress level. Expand task set before claiming anything. |
| Compositional narrow degrades, broad/atomic controls stable | Useful signal. Justifies expanding to 20+ pairs. Do not overclaim from 5 pairs. |
| Atomic clean control (P05) fails | Bad instrument. Stop. Repair scoring, format, or quantization setup before scaling. |
| Components pass, composite flips under INT4 | Seam pattern. The interesting diagnostic. Record which pairs and which rungs. |
| P06 narrow flips to shortcut answer under compression | Robust-wrong candidate. Flag and expand. |

---

## What this sweep cannot support

- Any claim about compression-fragility in general (5 pairs, one model, one calibration set)
- Any claim about provenance effects (no provenance contrast in this set)
- Any retention number as a "result" rather than a calibration check
- Comparison across calibration sets (only one calibration run)

---

## What comes next if sweep succeeds

1. Expand `tasks.py` to 20+ pairs covering all four cells
2. Run code calibration on full set
3. Run prose calibration on full set
4. Compare rung rankings across calibration sets (invariance gate)
5. Fill RESULTS-INTAKE-TEMPLATE.md

*Locked: E. A. Flores, Apiana AI, Inc., 2026-06-06*
