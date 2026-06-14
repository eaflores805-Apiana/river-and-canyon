# Open Discussion Item — Scaling and Tooling Posture

**Date:** 2026-06-09
**From:** CS Engineer (raising on Manager's instruction)
**To:** Senior Engineer, Team Lead, Manager
**Re:** Team discussion on standardization, scaling, and the program's tool-vs-instrument posture
**Status:** Discussion item — no decisions requested, no scope changes proposed

---

## Record status

```
Discussion item filed.
No candidate selected. No threshold values set. No runs authorized.
No engineering work authorized by this filing.
```

---

## Why this is being raised now

Manager raised the scaling question (2026-06-09): if the metrology process turns out to be a useful tool, we want to be able to standardize and scale, and that may be an engineering task in itself. The instruction was to bring it to the team for a real discussion — not to make decisions, but to make sure scaling isn't quietly baked in by single-model defaults before anyone has chosen.

The natural forcing function for this discussion is Paper 3 candidate selection. The candidate's `scope_of_certification` field (Appendix A.1) declares what the certification certifies for. If we lock a threshold sheet without an explicit scaling-scope statement, we have implicitly chosen single-model, single-scale by default. That choice should be made deliberately, not by omission.

---

## Current state — a single-instance research instrument

Everything built to date is single-instance:

| Axis | Current state |
|---|---|
| Model | Qwen2.5-3B-Instruct only |
| Precision | FP16 only (INT8/INT4 blocked) |
| Construction | Two-Hop L1 only (Cells 01–03) |
| Item count | n = 24 |
| Harness | B1 v2 (this session); MLX / Apple Silicon |
| Operators | One CS Engineer, one Senior Engineer, one Manager (you, Team Lead, me) |

Paper 3 §7 already states that thresholds are "construction-specific, model-specific, scale-specific, task-specific, and harness-specific" and do not auto-transfer. The framework is honest about this — but the engineering substrate has not yet been asked to handle transfer.

---

## The forward question

If this metrology becomes useful beyond its current scope — e.g., as a pre-flight check for new model releases, a methodology other groups apply, an internal QA gate, or a packaged eval — what changes structurally? And does that future affect what we should be building now?

That is a real engineering question, not a research one. Research can stay focused on one model at a time; engineering, if we want it, has to absorb the cross-model, cross-construction, cross-harness machinery.

---

## Scaling axes worth naming (not pre-deciding)

Each axis has different cost and different transfer implications. The discussion should at least name them so no axis gets defaulted silently:

- **Model size.** 3B → 7B → 13B → 70B. Compute cost scales nonlinearly. Threshold validity does not transfer per Paper 3 §7. Each new size needs its own threshold sheet derivation.
- **Model family.** Qwen → Llama → Mistral → others. Cross-family transfer is a research question that the framework does not assume.
- **Construction depth and shape.** Two-Hop L1 → n-hop, key-value grids, other compositional families. Each new construction needs its own constructibility-floor map (Paper 2 pattern). This is the most labor-intensive axis.
- **Item count.** n = 24 was sized for one cell. D7 sensitivity gate constrains how small n can be for a given minimum detectable retention drop. Scaling to higher-power studies means larger n.
- **Precision rungs.** Currently FP16-only. INT8 / INT4 are blocked until a stress-eligible baseline exists. Re-opening this lane scales the matrix of runs.
- **Harness substrate.** Currently MLX / Apple Silicon (CS local). A "useful tool" probably requires CUDA support, distributable packaging, and an inference backend abstraction.

---

## Engineering implications if the answer is "yes, we want this to be a tool"

These are not commitments — they are the kinds of decisions that get expensive to defer:

- **API surface.** How does someone use this on a new model without forking the runner? A pluggable model-loader interface is the difference between "1 hour" and "1 day" per new model.
- **Configuration layer.** Per-model config files, threshold-sheet registry, candidate manifest schema. Currently configuration is constants in the runner.
- **Storage and registry.** Threshold sheets, candidate manifests, certification records — where do they live as they accumulate? A flat directory works for 1; not for 50.
- **Inference backend.** MLX is the right local choice today. Cross-platform deployment (CUDA, Metal, CPU) would let other groups apply the methodology.
- **Distribution.** PyPI? GitHub release? Docker? Internal-only? Each option has different governance implications (especially for the non-authorization list — "public benchmark packaging" is currently blocked, but the *posture* changes if we package as a tool).
- **B1 v2 forward compatibility.** B1 v2 was built for one model + the bridge to Paper 3 certification. It's currently configurable but not pluggable. Extending vs. rewriting becomes a meaningful question if scaling is in scope.

The expensive-to-defer items are API surface and configuration layer. If we keep accreting model-specific constants in runner code, we're choosing single-model implicitly each time we add one.

---

## What I am and am not asking

**Asking for:**
- A team discussion before Paper 3 candidate selection locks anything in.
- Explicit positioning on the program's tool-vs-instrument posture: is this a research instrument that produces papers, a research tool that other people apply, or something between?
- Sequencing guidance: if scaling/tooling is in scope, when does it enter the work plan?

**Not asking for:**
- A decision in this filing.
- New engineering scope or B1 v3 plan.
- Changes to Paper 3 v0.4 or any locked artifact.
- Authorization for any candidate, model, or run.

---

## What this filing does NOT decide

It does not:
- Change Paper 3 framework or scope.
- Authorize multi-model or cross-construction work.
- Modify B1 v2 or its locked scope.
- Reopen Fork A, Claim C, or any blocked stress lane.
- Authorize public packaging of any kind.
- Commit the program to becoming a tool.

It only asks: *should we have the discussion now, or wait until the discussion becomes load-bearing?* CS's recommendation is now — because Paper 3 candidate selection is the next real moment a scaling-scope statement gets locked, and unlocking that statement later is more expensive than getting it right at first lock.

---

## Suggested discussion prompts

For Senior:
- What posture would best serve the metrology's intellectual contribution? Research instrument, research tool, methodology paper-set, all three?
- Does scaling-scope belong in the Paper 3 candidate's `scope_of_certification` field?

For Team Lead:
- What's the right sequencing? Discuss before candidate selection, or after one candidate is certified?
- Should scaling get its own planning lane parallel to B1 hardening and Paper 3 candidate work?

For Manager:
- Are you open to a parallel tooling/engineering planning lane, or is current focus better preserved by holding tooling questions until research questions are settled?
- What posture would you want the program to have a year from now, and does that change what we build now?

---

## Non-authorizations (carried forward)

```
candidate selection · threshold values · new runs · re-runs
INT8 / INT4 execution · multi-model execution · cross-construction execution
Fork A reactivation · Claim C activation · Paper 3 execution
tooling implementation · packaging · public benchmark packaging
artifact mutation
```

---

— CS Engineer, 2026-06-09
