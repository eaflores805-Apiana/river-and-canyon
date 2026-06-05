# Fragility Probe — Standalone Abstract

*A portable, methods-facing summary of the fragility-probe protocol. This version carries none of the companion-paper framing; it is intended to let the protocol travel to quantization, compression, and evaluation researchers on its own terms. The full protocol, with its tier structure and companion context, is in `fragility-probe-protocol.md`.*

---

This protocol specifies a controlled, pre-registered evaluation design for testing whether precision demand predicts differential retention under numerical stress. It asks whether behaviors requiring exact state preservation, variable binding, or step-wise symbolic execution retain less of their full-precision performance than matched behaviors that tolerate multiple acceptable outputs, when both are evaluated under the same quantization recipe.

The design uses a within-model bit-depth sweep on matched task pairs drawn from the same source material. Each pair differs primarily in precision demand while holding domain, length, and prompt structure approximately constant. Retention is measured relative to each task's own FP16/BF16 baseline. To prevent metric artifacts, both halves of each pair are scored under comparable strictness using canonical structured formats such as checklists, JSON fields, entity-slot accuracy, constrained multiple choice, or predefined rubrics, rather than tolerant semantic scoring versus exact-match scoring.

The protocol includes broad–broad and narrow–narrow negative controls, scorer-sensitivity checks, and a pre-declared three-outcome decision rule that distinguishes real retention gaps from scoring artifacts or task-pair confounds. Every run reports its full stress profile, including quantization format and method, weights-only versus weights-plus-activations, bit-depth ladder, calibration file hash, and calibration distribution.

The protocol tests whether retention under numerical stress provides information about behavioral stability that peak full-precision accuracy alone does not. It is intended as a portable baseline measurement tool for quantization robustness, compression evaluation, and capability-fragility research.

---

*Status: proposed evaluation design, not yet run. The design is coherent and the controls are specified; its predictive value — whether stress-retention forecasts deployment-relevant failure better than peak accuracy — is unvalidated until executed. Written by E. A. Flores, Apiana AI, Inc.*
