# CS Classification — Paper 3 Metrology Safeguards

**Date:** 2026-06-09
**From:** CS Engineer
**To:** Team Lead, Senior Engineer, Manager
**Re:** Classification of four proposed Paper 3 metrology safeguards
**Filed per:** Team Lead directive, 2026-06-09
**Parent record:** `CS-TECHNICAL-REVIEW-PAPER3-THRESHOLD-FRAMEWORK.md` (this directory)

---

## Record status

```
Classification filed.
No candidate selected. No threshold values set. No runs authorized.
```

---

## Classification codes

```
A  Paper 3 main-framework requirement
B  Appendix A threshold-sheet field
C  B1 harness implementation requirement
D  Stress-side validation requirement, not baseline certification
E  Future work / out of scope for Paper 3
```

---

## Item 1 — D1: Unconditioned token-prior control

**Concern:** A flat random chance baseline may be inadequate when target entities have unequal native token priors.

**Classification: A — Paper 3 main-framework requirement**

**Rationale:** The current D1 language requires clearing "chance and dummy-policy baselines" but does not explicitly require a token-prior control. Without this, a threshold sheet could satisfy D1 with uniform chance alone and silently pass a candidate whose correct answers are partially explained by native emission bias. Elevating this to the framework level ensures no threshold sheet can skip it.

**Implementation burden:** MEDIUM. Computing native emission probability for target tokens requires either (a) tokenizer vocabulary frequency analysis (feasible offline, limited accuracy) or (b) running the model on a neutral / task-free context to measure unconditional output distributions. Option (b) is a constrained preflight run — it requires Manager authorization before it can be executed. This is not a zero-cost offline operation in general.

**Recommended placement:**
- D1 framework text: add "the floor must also clear an unconditioned token-prior control or equivalent dummy-policy baseline that accounts for native emission bias."
- Appendix A threshold sheet: specifies the control method chosen (vocabulary-based estimate vs. preflight run), the target-entity token set, and the measured or estimated prior values.
- Preflight run (if required): separately authorized; not opened by this filing.

---

## Item 2 — D3: Tokenization-boundary invariance guard

**Concern:** Entity swaps, distractor shuffling, or positional perturbations may change BPE token boundaries, creating hidden format or load artifacts not captured by strict-vs-content scoring.

**Classification: A — Paper 3 main-framework requirement**

**Rationale:** The program already has an established tokenization audit mechanism: tokenizer hash verification, BPE-Jaccard inspection, and Gate 0.5 (near-miss pair validation). Making this an explicit D3 requirement in the framework ensures it is applied to every Paper 3 candidate and cannot be treated as optional. The specific audit results belong in the threshold sheet, but the requirement to perform the audit is framework-level.

**Implementation burden:** LOW. The tokenizer audit tooling is already in the program:
- `BPE-JACCARD-INSPECTION-TWOHOP-L1.md` and the offline inspection script establish the method.
- Tokenizer hash reconciliation protocol is documented.
- This is an offline pre-run step — no authorized model run required.

**Recommended placement:**
- D3 framework text: add "target entities, keys, and format indicators must have tokenization-invariant boundaries across all declared permutations, verified by an offline tokenizer audit before the candidate run."
- Appendix A threshold sheet: records the tokenizer hash, the audit artifact, and the zero-violation confirmation for the candidate's token set.

---

## Item 3 — D5: Structural-only difficulty proxies

**Concern:** Difficulty proxies must not be based on model accuracy or observed failures, which would be circular.

**Classification: A — Paper 3 main-framework requirement (B1 is the implementation path)**

**Rationale:** D5 currently specifies "difficulty proxies" without constraining them to structural metadata. Without an explicit exclusion, model-accuracy-based proxies (which encode the outcome being measured as an input to the matching criterion) are not barred. The principle "proxies must be structural" is a framework rule, not a threshold-sheet choice.

The implementation path is B1: B1 can compute the relevant structural proxies deterministically from the manifest JSON without any model run. Candidate fields include: token length, graph distance, number of hops, number of distractors, token-prefix overlap, context-window utilization. These are all computable from item metadata alone.

**Implementation burden:**
- Framework text change: LOW.
- B1 manifest computation: LOW-MEDIUM. The manifest already contains the structural metadata. B1 adds a `difficulty_metadata` block to `gate_summary` with these fields computed at run time. No new manifest fields required; no model output accessed.

**Recommended placement:**
- D5 framework text: add "Difficulty proxies must be computed from item metadata only (structural proxies). Proxies derived from model outputs, observed accuracy, or failure rates are not admissible."
- B1 harness: add `difficulty_metadata` to `gate_summary`, computed from manifest fields at run time.
- Appendix A threshold sheet: lists the specific structural proxies used for this candidate and the match tolerance.

---

## Item 4 — D6 / numerical stress eligibility: Activation outlier telemetry

**Concern:** A baseline can be behaviorally clean at FP16 but numerically fragile under integer quantization due to activation outliers or extreme residual-stream scaling.

**Classification: D — Stress-side validation requirement, not baseline certification**

**Rationale:** Activation outlier metrics (kurtosis, peak-to-mean ratio, equivalent) are only interpretable as fragility indicators in comparison across precision rungs. FP16 baseline values alone do not establish fragility — a high-kurtosis activation at FP16 may survive INT8 intact; a low-kurtosis activation may not. The comparison requires INT8/INT4 runs, which are stress runs. This item does not belong in baseline certification (D6); it belongs in stress-side validation, which is downstream of any authorized compression run.

**MLX feasibility:** In the current `mlx_lm` environment, per-layer activation statistics are not exposed through the standard generation API. Recording kurtosis or peak-to-mean ratio would require custom forward-pass hooks into the model's residual stream — a substantial harness extension well beyond B1 scope. This is not implementable within the B1 plan as currently specified.

**Implementation burden:** HIGH, and not addressable within the current harness scope. Deferred.

**Recommended placement:**
- Not a D6 field. D6 is provenance and reproducibility of the baseline; numerical fragility prediction is a separate question.
- Not a new certification gate for Paper 3. It cannot be evaluated without running stress rungs.
- If pursued: a separate stress-side validation design, scoped and authorized after a certified baseline exists and a compression run is authorized. Out of Paper 3 scope.

---

## Summary table

| Item | Classification | Burden | Requires authorized run? |
|---|---|---|---|
| D1 — Token-prior control | A — main framework | MEDIUM | Possible (preflight run option) |
| D3 — Tokenization-boundary guard | A — main framework | LOW | No (offline audit) |
| D5 — Structural-only proxies | A — main framework + C (B1) | LOW | No (manifest-only) |
| D6 — Activation outlier telemetry | D — stress-side validation | HIGH (out of scope) | Yes (requires stress runs) |

---

## Non-authorizations (carried forward)

```
new runs · preflight runs · unconditioned-prior runs · activation logging runs
INT8 / INT4 execution · candidate selection · threshold values
Fork A reactivation · Claim C activation · Paper 3 execution
artifact mutation · public benchmark packaging
```

---

— CS Engineer, 2026-06-09
