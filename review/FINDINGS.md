# River and Canyon — Full Review Findings

*Prepared by Claude (Anthropic), June 2026. Covers: complete repository audit, literature verification, novelty assessment, technical setup, and strategic recommendations. All section numbers are stable; add findings to them rather than creating new files.*

---

## 1. What This Repository Is

A **bounded behavioral metrology workflow** for evaluating LLM capability under quantization stress. It consists of:

1. Two essays building and stress-testing a physical analogy for transformer mechanics (the "river and canyon" model).
2. A proposed matched-pair experimental design for measuring capability retention under bit-depth reduction.
3. A runnable Python harness (MLX/Apple Silicon) for executing that experiment.
4. A claim-governance layer — a ledger, boundary diagrams, and explicit epistemic limits — that separates behavioral evidence from mechanistic claims.

**Zero empirical data has been collected.** The harness is verified-valid, the model is downloaded, and the task stubs exist — but `tasks.py` contains only 2 worked examples (P01, P02) out of a needed ~20-40 pairs. Running the experiment is the single open action.

---

## 2. Repository Map

```
river-and-canyon-repo-FINAL/
├── README.md                           — entry point; reading order
├── STATUS.md                           — live status of all pieces; most honest self-assessment
├── REVIEW.md                           — one-document project overview
│
├── the-river-and-the-canyon/
│   ├── the-river-and-the-canyon.md     — full paper; Part I builds the analogy, Part II breaks it
│   ├── the-river-and-the-canyon-lean.md — 90-line condensed version; start here
│   └── no-mountain-in-the-sentence.md  — method essay: state the claim without the analogy
│
├── what-kind-of-water/
│   └── what-kind-of-water.md           — companion paper; provenance × fragility two-axis model
│
├── notes/
│   ├── fragility-probe-protocol.md     — full experimental design with 6 confound guards
│   ├── IMPLICATIONS-SUMMARY.md         — 13 Tier-A implications scored on 5 axes
│   ├── literature-notes.md             — 4-round search; claims shrank to synthesis-not-discovery
│   ├── inference-ranking.md            — 5 independent rankings converging on same substance order
│   ├── analogy-as-scaffold.md          — three registers: analogy / mechanism / measurement
│   ├── capability-under-load.md        — speculative: capacity ≠ usable structure
│   ├── claim-ledger-practice-note.md   — control sheet: every claim sorted by evidential status
│   ├── open-question-uneven-support.md — parked open question; reach ≠ validity
│   └── carved-path-pattern-list.md     — raw material for above; not a finding
│
├── diagrams/
│   ├── README.md                       — six governance figures described
│   ├── lineage.{html,png}              — what the analogy generated and what unequally survived
│   ├── boundary.{html,png}             — what the method can and cannot decide (table form)
│   ├── venn.{html,png}                 — Method / Evaluation / Mechanism boundary (spatial)
│   ├── gap-map.{html,png}              — unexplored areas by field
│   ├── decision.{html,png}             — what each Tier 0 outcome means (pre-registered)
│   └── status.{html,png}              — what promotes a claim
│
├── tier0-run/
│   ├── run_tier0.py                    — Python harness; patched and verified valid
│   ├── tasks.py                        — CRITICAL: only 2 of ~20 pairs written
│   ├── task_design.md                  — 4-cell design grid; 20 blank pair slots
│   ├── DIAGNOSTIC-ADDENDUM.md          — Tier-1 diagnostics (seam + robust-wrong tests)
│   └── RESULTS-INTAKE-TEMPLATE.md      — pre-registered blank run slot
│
└── review/
    └── FINDINGS.md                     — this document
```

---

## 3. Literature Verification — Claim-by-Claim

### 3.1 Fragility axis: precision-demanding capabilities degrade more under quantization
**Verdict: ESTABLISHED by the field.** Not a novel claim.

Key papers confirm near-verbatim:
- **arXiv 2505.11574** (Li et al., "Quantization Meets Reasoning"): post-training quantization disproportionately affects mathematical reasoning; mild impact on general language. Recovery possible with ~500 task-specific examples.
- **arXiv 2504.04823** ("Quantization Hurts Reasoning?"): systematic study across DeepSeek-R1-Distilled and Llama families (1.5B–70B). Disentangles capability into **memorization** (fragile) vs. **utilization** (robust). Goes further mechanistically than this framework.
- **arXiv 2606.00206** (Meta FAIR): compression can preserve aggregate performance while disproportionately degrading harder capabilities. Most affects high-entropy "thinking" tokens. Names this an *emerging thread*.
- **arXiv 2501.03035**: up to 32.39% accuracy degradation on Llama-3 under AWQ/GPTQ, concentrated in numerical computation and reasoning planning.

**Implication for Paper 2:** The fragility axis is a synthesis, not a discovery. The contribution is the framing and the cleaner measurement design (matched-pair, same-context, same-prompt-length) that controls the task-difficulty confound cross-benchmark comparisons carry.

**One overclaim to fix:** Any suggestion that "CoT length stays stable at moderate quantization, so CoT improves robustness" is not supported. arXiv 2606.00206 found the *opposite* in key cases — quantization most affects high-entropy thinking tokens. The correct statement: CoT-style outputs are among the *more* fragile under compression, not more robust.

---

### 3.2 Provenance effects: training composition shapes capability and robustness
**Verdict: SUBSTANTIALLY ESTABLISHED.** Controlled comparison already run.

- **arXiv 2409.04556**: trains on interleaved NL+code **holding total data volume constant** — a clean causal design. Higher code proportion improves compositional/structured-output tasks and math; harms syntax-sensitive and real-world-knowledge tasks. This is the controlled provenance comparison, done.
- **arXiv 2509.21499**: parallel NL vs. code instruction datasets, five model families, 3,331 fine-tuning experiments. Models more vulnerable to structural than semantic perturbation, especially on math and code.

**Implication:** This framework independently converged on a question the field has already answered with controls. Its role is synthesis. The specific narrow corner that may remain open: whether provenance predicts *quantization-retention* specifically (vs. perturbation-robustness in general). Not enough to build weight on.

---

### 3.3 Two-axis model (provenance × fragility)
**Verdict: ORIGINAL FRAMING.** A genuine structural contribution.

No paper reviewed organizes the space as a two-dimensional grid with provenance on one axis and fragility on the other. The field studied both variables independently; this framework's contribution is the cross-product and the geometric interpretation that makes it tractable for experimental design. This is not a mechanical discovery — it is an organizational lens, and it is a real one.

---

### 3.4 Retention blind-spot: a model that is merely robust-at-being-wrong scores as robust
**Verdict: REAL AND UNDERAPPRECIATED.** The most defensible operational contribution.

The logic is analytic, not empirical: a retention metric (score_stressed / score_baseline) equals 1.0 whether the model got it right in both conditions or wrong in both. Without correctness + same-error identity logging, aggregate retention certifies the wrong thing. No paper found explicitly addresses this as a reporting requirement. The contribution is the *operational guard* — forcing these columns into the output rather than letting them hide inside an aggregate.

This is the strongest claim in the repository. It is self-evident once stated, but no framework reviewed enforces it.

---

### 3.5 Metric asymmetry as confound: scoring broad with tolerant judge + narrow with exact manufactures the gap
**Verdict: REAL AND IMPORTANT.**

The experimental design literature acknowledges scoring consistency as a control, but the specific argument here — that using a *lenient judge for the broad arm and exact-match for the narrow arm* will always produce ΔR > 0 regardless of whether any real effect exists — is stated more precisely here than in the papers reviewed. This is the single most important confound guard in the protocol and it is correctly identified.

---

### 3.6 Qualification question: does retention under stress predict deployment reliability better than peak accuracy?
**Verdict: GENUINELY OPEN narrow question.**

The *concept* of reliability-style evaluation is active. What the literature search did **not** clearly find: the specific competing-predictors test — retention-under-compression vs. peak accuracy, as rival predictors of reliability, across a panel of models. This is the framework's honest forward edge. Its value does not depend on originality: a stress metric that predicts field failure is useful whether or not anyone proposed it first.

---

### 3.7 Physical analogy (river / canyon / water)
**Verdict: TEACHING TOOL, not a mechanism claim.**

The analogy is not evaluated as a research claim — it is a scaffold for intuition. The papers say this explicitly and spend significant space stress-testing the analogy to find where it breaks. This is correctly handled.

---

### 3.8 Claim governance layer (claim ledger + boundary diagrams)
**Verdict: GENUINE PROCESS CONTRIBUTION.**

A pre-registered claim ledger that sorts every major assertion by evidential status, combined with governance diagrams that block mechanism claims from behavioral measurement, is a packaging contribution. The *underlying principles* (construct validity, preregistration, model-card discipline) are not novel. The *applied combination* — enforced through a visual diagram set with a pre-registered decision matrix — is distinctive, especially for a solo research project.

---

## 4. Novel Contributions — Ranked by Value

| Rank | Contribution | Why it matters |
|---|---|---|
| 1 | **Correctness + same-error identity guard** | Operational: forces retention evaluation to log what survived. No reviewed framework enforces this. Self-evident once stated; not enforced in practice. |
| 2 | **Metric symmetry as confound guard** | Methodological: identifies the exact mechanism by which a fair-seeming experiment manufactures the gap. Precise, actionable. |
| 3 | **Qualification question** (retention vs. accuracy as predictors) | Scientific: a clean head-to-head test not clearly found in the literature. Valuable regardless of originality. |
| 4 | **Two-axis framework** (provenance × fragility) | Organizational: original cross-product framing that the field hasn't used for experimental design, even if both axes are individually studied. |
| 5 | **Matched-pair, same-context design with component verification** | Methodological: controls the task-difficulty confound that cross-benchmark comparisons carry. Cleaner than prior instrument designs. |
| 6 | **Pre-registered claim governance** (ledger + decision matrix) | Process: makes it harder to misread a behavioral result as a mechanistic claim. Distinctive packaging. |
| 7 | **Physical analogy and synthesis** | Communication: organizes an emerging finding under a vivid framework for a non-specialist audience. Teaching value is real; mechanism value is zero. |

**Bottom line:** Items 1 and 2 are the strongest because their value is analytic and does not depend on running data. Items 3–5 become valuable once the experiment runs. Items 6–7 are positioning.

---

## 5. Technical Setup — What Was Done This Session

### 5.1 Environment

**Hardware:** Apple M2 Max, 32GB unified memory. Adequate for Qwen2.5-7B at FP16 (~14GB) with room for OS.

**Why Ollama models (qwen3:14b, phi3) don't work:** Ollama distributes pre-quantized GGUF files. These are already at INT4/INT8 — there is no FP16 baseline to compute retention from. A bit-depth sweep requires the model in HuggingFace format, loaded fresh at each bit-depth via `mlx-lm`.

### 5.2 Installation and model download

```bash
pip install mlx-lm numpy
# model downloaded to ~/.cache/huggingface/hub/models--Qwen--Qwen2.5-7B-Instruct/
# ~14.3GB, 4 safetensors shards — download confirmed complete
```

**Model:** `Qwen/Qwen2.5-7B-Instruct` — instruction-tuned, chat template present, well-studied, good reasoning performance. Appropriate for this probe.

### 5.3 Harness patches applied to `tier0-run/run_tier0.py`

**Patch 1 — mlx-lm 0.31.3 API change (required)**

In mlx-lm ≥ 0.31.x, `quantize_model` requires the model config dict as a second positional argument. The original scaffold called `quantize_model(model, group_size=64, bits=bits)` which fails.

Fix: use `load(model_repo, return_config=True)` and pass config forward:
```python
def load_at_bits(model_repo: str, bits: int):
    model, tokenizer, config = load(model_repo, return_config=True)
    if bits == 16:
        return model, tokenizer
    group_size = 64
    quantize_model(model, config, group_size=group_size, bits=bits)
    return model, tokenizer
```

**Patch 2 — component_checks support (required for seam-fragility diagnostics)**

Added per-hop verification loop inside the main run, plus a component competence summary in the output JSON. This enables the seam-fragility flag: "composite degraded while all component hops passed — seam candidate."

Key additions:
- `raw.setdefault(pid, {..., "components": {}})` — initialize components dict per pair
- Loop over `pair.get("component_checks", [])` — verify each hop independently
- `comp_summary` block — aggregate component data, flag seam candidates
- `summary["component_competence"] = comp_summary` — include in JSON output

Both patches are in place. The harness is ready to run once `tasks.py` is filled.

---

## 6. The Tier 0 Experimental Design

### 6.1 The core hypothesis

> Compositional tasks degrade more under quantization than atomic tasks **after controlling for component competence** — i.e. the composite fails while the individual hops still work.

A composite that fails because the model doesn't know an intermediate fact is a data problem, not a precision problem. The seam hypothesis requires the components to be verified passing before the composite failure counts.

### 6.2 Four-cell design grid

| Cell | Structure | Support | What it probes |
|---|---|---|---|
| 1 | Atomic | High-shortcut | Stable-wrong / robust-wrong probe |
| 2 | Atomic | Low-shortcut | Clean retention control (boring but essential) |
| 3 | Compositional | High-support | Familiar composition without rarity confound |
| 4 | Compositional | Low-support | **Core ΔR stress target** |

The live comparison is Cell 4 vs Cell 3 (or matched atomic). Cells 1 and 2 supply anchors.

### 6.3 The one rule that governs task design

> **All Tier 0 tasks are closed-world.** The relevant facts live inside the prompt. No uncontrolled world knowledge.

A multi-hop chain using real-world entities conflates four failure modes: broken chain logic, unknown entity, unknown relation, ambiguous wording. Closed-world prompts eliminate all of these. Every fact supplied, every binding explicit, every expected answer deterministic.

### 6.4 Execution order

```
Phase 0: Smoke test (3-5 pairs at FP16 only)
  — confirms format parsing, scoring, and JSON output fire correctly
  — do not look at ΔR until full set is locked

Phase 1: Code-calibration run (--calib code)
  — FP16, INT8, INT4 on the full pair set

Phase 2: Prose-calibration run (--calib prose)
  — same pair set, different calibration hash

Gate: Compare rung rankings across calibration sets
  — the fragility signal counts only if pair ranking by ΔR is invariant
  — if ranking flips, the result is calibration-sensitive, not capability-sensitive
```

### 6.5 Outcome classification (pre-registered)

| Outcome | What it means |
|---|---|
| A: ΔR > 0, CI excludes 0, invariant across calibrations | Real signal; report with component verification data |
| B: ΔR > 0, CI includes 0, or ranking reverses across calibrations | Metric artifact or calibration sensitivity; do not report as positive |
| C: ΔR ≈ 0, robust-wrong flags also absent | Local null; does not retire the correctness/same-error requirement |
| Negative ΔR | Broad tasks degrading more than narrow; inspect scoring and pair matching |

Pre-declared thresholds: **ΔR > 0.15** and **same-error rate > 0.7** as review triggers (not proof). With 20 items, crossing them is smoke-test evidence worth a larger controlled look.

### 6.6 What `tasks.py` needs

Currently: 2 of ~20+ pairs (P01: temporal ordering, P02: arithmetic).

Each pair requires:
- `id`, `source_note`
- `narrow` arm: prompt + `score_type: "exact"` + `answer`
- `broad` arm: prompt + `score_type: "checklist"` + `required_facts`
- `counterexample` (optional but strongly recommended): the shortcut-trap version
- `component_checks` (required for Cell 3 and 4 pairs): one dict per hop with `prompt`, scoring, and `hop` label

**Minimum viable run: 20 pairs across all four cells, including at least 1 broad-broad and 1 narrow-narrow negative control.**

**Suggested domain breakdown (20 pairs):**
- Cell 1 (atomic + shortcut): 4 pairs — negation traps, position-bias, lexical-overlap NLI
- Cell 2 (atomic + clean): 4 pairs — closed-world lookup, single-step arithmetic
- Cell 3 (compositional + high-support): 4 pairs — familiar 2-hop chains (supplied facts)
- Cell 4 (compositional + low-support): 6 pairs — synthetic 2-3 hop, unusual constraints, distractors
- Negative controls: 2 pairs — broad-broad and narrow-narrow (must show no within-pair gap)

---

## 7. Current State: What's Ready vs. What's Missing

| Item | Status |
|---|---|
| Hardware | Ready (M2 Max 32GB) |
| mlx-lm installed | Ready |
| Model downloaded | Ready (`Qwen/Qwen2.5-7B-Instruct`, ~14.3GB) |
| `run_tier0.py` harness | Ready (both patches applied) |
| `tasks.py` — P01, P02 | Written (2 pairs) |
| `tasks.py` — remaining 18+ pairs | **NOT WRITTEN — blocking** |
| Smoke test | Not yet run |
| Phase 1 (code calibration) | Not yet run |
| Phase 2 (prose calibration) | Not yet run |
| RESULTS-INTAKE-TEMPLATE.md | Pre-registered blank, waiting for first numbers |

---

## 8. How to Run

```bash
cd "/Users/eliasflores/Documents/Projects/Apiana_Ai/LLM_Mechanics/final/files (14)/river-and-canyon-repo-FINAL/tier0-run"

# Smoke test (FP16 only, just the 2 existing pairs)
python run_tier0.py \
  --model Qwen/Qwen2.5-7B-Instruct \
  --bits 16 \
  --calib code \
  --max-tokens 256

# Full code-calibration run (after tasks.py is filled)
python run_tier0.py \
  --model Qwen/Qwen2.5-7B-Instruct \
  --bits 16 8 4 \
  --calib code

# Full prose-calibration run
python run_tier0.py \
  --model Qwen/Qwen2.5-7B-Instruct \
  --bits 16 8 4 \
  --calib prose

# Results land in: results_code_<timestamp>.json, results_prose_<timestamp>.json
```

**Memory note:** Each fresh load of the model at a new bit-depth requires ~14GB (FP16) or ~4GB (INT4). The harness deletes each loaded model (`del model, tokenizer`) before loading the next. Total run on all three bit-depths: ~1-2 hours depending on pair count and token limits.

---

## 9. What Needs to Be Done Before Submission

### 9.1 Fix the CoT overclaim
Any language suggesting "CoT is more robust under quantization" needs to be corrected. The Meta FAIR paper (arXiv 2606.00206) found quantization most affects high-entropy thinking tokens — the opposite direction. The correct positioning: CoT-style extended reasoning is among the *more* fragile outputs under compression.

### 9.2 Fill tasks.py
This is the experiment. The quality of the result depends entirely on the quality of the pairs. Bad pairs produce clean-looking false results. Good pairs produce interpretable ones. The design grid and the four rules in `tasks.py` are the guide.

### 9.3 Run the smoke test
3-5 pairs at FP16 only. Confirm: does the model follow the prompt format? Does `score_exact` hit? Does `score_checklist` hit? Does the JSON output look right? Fix any format issues before scaling.

### 9.4 Run both calibration sets
Lock `tasks.py` before looking at ΔR numbers. The pre-registration only counts if the scoring rubric and pair definitions don't change after seeing results.

### 9.5 Fill RESULTS-INTAKE-TEMPLATE.md
The template has a pre-registered blank run slot. Fill it with real numbers and classify the outcome (A / B / C / flat) per the decision matrix.

---

## 10. Strategic Recommendations

### 10.1 What to claim, and how
The project's honest positioning:

> "We present a measurement protocol for behavioral capability evaluation under quantization stress. The protocol's contribution is not finding a new failure mode — quantization fragility is established — but rather enforcing a reporting contract that makes stable-wrong behavior visible: correctness and same-error identity are logged jointly with retention so that a model that is merely robust-at-being-wrong cannot score as robust."

This is defensible, precise, and distinct from adjacent work.

### 10.2 Publication path
The **qualification question** (retention vs. accuracy as rival predictors of deployment reliability) is the strongest forward edge. A follow-up study that:
1. Runs the Tier 0 matched-pair protocol on 3-5 models across the quantization ladder
2. Correlates retention scores (not just accuracy) against a deployment-reliability benchmark
3. Tests whether retention adds predictive value beyond accuracy alone

...would be an arXiv-publishable result in the current robustness/reliability evaluation space. It does not require the physical analogy at all — it is a clean engineering question.

**Near-term:** The current repository, once Tier 0 runs, is a working paper / technical report. It is suitable for arXiv as a methods/protocols contribution (not an empirical result). Submit to arXiv cs.LG or cs.CL after Tier 0 completes.

### 10.3 How to use the analogy
The river-and-canyon analogy is a communication asset. It makes the ideas accessible to non-specialists. It should be in talks, blog posts, and introductory framing — not in the mechanistic claims sections of papers. The "no mountain in the sentence" rule is the right discipline: state every empirical claim without the analogy, then use the analogy to motivate the reader's intuition.

### 10.4 Career positioning (defense / AI context)
The project demonstrates:
- Metrological discipline: pre-registration, confound identification, symmetric scoring
- Experimental design: matched-pair within-subject design with bootstrap CIs
- Systems thinking: the two-axis framework organizes a multi-variable space cleanly
- Epistemic honesty: the claims shrank through four literature search rounds and the project kept going

These are signal qualities for defense AI / AI safety / AI evaluation roles where rigorous, bounded claims matter more than high-impact demo results.

---

## 11. Session Summary

This review session covered:

1. Full directory read of the repository (all 50+ files)
2. Four-round literature search confirming fragility established, provenance established, qualification question open
3. Assessment that items 1-2 in the novelty ranking (correctness guard + metric symmetry guard) are the strongest contributions
4. Identification of the CoT overclaim requiring a fix
5. Diagnosis that Ollama GGUF models are incompatible with the experiment (pre-quantized, no FP16 baseline)
6. Installation of `mlx-lm`, download of `Qwen/Qwen2.5-7B-Instruct` (~14.3GB)
7. Two patches to `run_tier0.py`: (a) mlx-lm 0.31.3 API fix for `quantize_model`, (b) component_checks support for seam-fragility diagnostics
8. This document

**The single blocking action is filling `tasks.py`.** Everything else is ready.

---

*E. A. Flores, Apiana AI, Inc. | Review session: June 2026*
