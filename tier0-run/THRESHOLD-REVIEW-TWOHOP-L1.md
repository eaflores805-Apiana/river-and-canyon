# Threshold Proposal Review — CS Engineer Response

**Date:** 2026-06-07  
**Author:** CS Engineer  
**In response to:** Team Lead memo "Threshold Proposal Review — Narrow Technical Pass," 2026-06-07  
**Scope:** Technical review only. No thresholds approved. No runs authorized.

---

## Q1 — Gate-2 strictness: 0.80 vs 0.875

**Disposition: REVISE — raise to ≥ 0.875**

0.80 is not defensible. The reason it was proposed as 0.80 is essentially "avoid brittleness at the margin," but that rationale proves too much — any threshold can be loosened for the same reason. The right response to a difficult task is to redesign the cell until it clears 0.875, not to lower the gate.

Specific objections to 0.80:

1. **Paper 1 precedent.** Both feasibility screens (Exp8A, Exp8B) used ≥ 7/8 = 0.875 as the pass condition. That threshold was set on a simpler task (single-lookup, 5-fact context). A two-hop cell that cannot beat the single-lookup feasibility threshold has not established a floor — it has found a ceiling.

2. **The constructibility claim requires a clean FP16 baseline.** Claim B (mappability hypothesis) depends on FP16 being unambiguously above any plausible chance level. At 0.80 on a 2-choice composite task (uniform random = 0.50), the signal-to-chance ratio is 1.6:1. At 0.875 it is 1.75:1. The difference is small in absolute terms but meaningful for a gate whose purpose is to license further inference.

3. **A cell passing at 0.80–0.87 is a construction problem, not a threshold problem.** If a cell lands in that range at FP16, the correct action is to inspect the item manifest for structural defects (position anchoring, hop-shortcut paths, query ambiguity) and redesign, not to accept the cell.

**Proposed replacement:** ≥ 0.875 (≥ 17.5/20 → effectively ≥ 18/20 for integer counts at n=20)

---

## Q2 — Dummy ceiling / margin

**Disposition: REVISE — adopt two-condition rule**

The single-condition proposal (max_dummy ≤ 0.60) is insufficient. The problem: a cell with Gate-2 = 0.88 and max_dummy = 0.59 technically passes both the gate and the ceiling, but the gap (0.29) is just barely above the proposed margin, and a cell with Gate-2 = 0.875 and max_dummy = 0.60 fails only by one percentage point. The absolute ceiling and the margin need to be co-specified to be a coherent check.

**Proposed two-condition rule:**

```
Condition 1: max_dummy_score ≤ 0.55 (absolute ceiling)
Condition 2: Gate-2 pass rate − max_dummy_score ≥ 0.25 (minimum margin)

Both conditions must pass.
```

Rationale for the specific values:

- **Ceiling 0.55:** A well-constructed cell has uniform_random_expected = 0.50 (for 1-target + 1-decoy composite). Any dummy above 0.55 is 5 points above chance from a systematic cause — almost always a context-ordering artifact (target C consistently first or last). 0.55 provides a 5-point tolerance above chance without accepting gross ordering artifacts.

- **Margin 0.25:** With Gate-2 threshold at 0.875, the ceiling condition implies max_dummy ≤ 0.55, which gives minimum margin = 0.875 − 0.55 = 0.325. The margin condition is more binding for cells where Gate-2 passes at the minimum (0.875) with a modest dummy (e.g., 0.52 dummy is fine by the ceiling but margin = 0.355 passes). The margin condition catches the case where Gate-2 is marginal and the dummy is also moderately high: e.g., Gate-2 = 0.90, max_dummy = 0.64 — passes ceiling fails if ceiling is 0.60, but now fails margin too (gap = 0.26, just above margin). This is tighter when both are near their respective thresholds.

- In practice, for a well-constructed cell the margin will typically be ≥ 0.40. The margin condition is a floor protection, not an expected constraint.

---

## Q3 — Gate-3 denominators

**Disposition: REJECT all Gate-3 ceilings until denominators are explicit and the shortcut_single_hop_rate mapping is resolved**

Two problems:

**Problem A — Denominators unspecified.** The proposal lists five rates but does not state what each rate is computed over. This is not a documentation gap; it directly determines whether the ceiling is binding or trivially satisfied.

Correct denominator for all five Gate-3 rates: **composite items with FORMAT_PASS**.

- "All items" is wrong: includes FORMAT_FAIL items that have no fidelity class. A cell with 40% FORMAT_FAIL would have artificially deflated rates, making all ceilings easy to pass.
- "Only failed items" is wrong: that is a conditional probability (given failure, what fraction is this class?), useful for failure anatomy analysis but not for a gate. It removes correct items from the denominator, inflating rates when correctness is high.
- "Only parseable outputs" is correct and equivalent to FORMAT_PASS for composite items.

Formally: for rate R corresponding to failure class FC,

```
R = count(composite, FORMAT_PASS, failure_class = FC) / count(composite, FORMAT_PASS)
```

Correct items (is_correct = True) contribute to the denominator but not the numerator. This is intentional.

**Problem B — shortcut_single_hop_rate has no failure class mapping.**

The Run Summary template (Section 6) lists `shortcut_single_hop_rate` as a Gate-3 fidelity metric. The proposal maps it to `non_context_return (shortcut variant)`. This mapping is incorrect.

`non_context_return` fires when a token is (a) not in the registry, or (b) NULL on a positive query. Neither of those is a "shortcut single-hop" in the intended sense. A single-hop shortcut on a composite query — where the model answers as if only hop1 were required — would fire as `correct_chain_stopped_short` (if it returns B_target) or as `anchor_echo` (if it returns A). There is no case in the current failure taxonomy where returning a single-hop answer on a composite query goes unclassified.

Before any ceiling is approved for shortcut_single_hop_rate, the following must be resolved:

1. What is the precise definition of "shortcut single-hop"?
2. Which failure class or combination of failure classes does it map to?
3. Is it a distinct Gate-3 diagnostic (e.g., shortcut = stopped_short + anchor_echo combined) or is it a renamed view of a single existing class?

Until this is resolved, the shortcut_single_hop_rate ceiling (≤ 0.10) cannot be approved. The other four ceilings can proceed once denominators are corrected.

**Revised Gate-3 ceiling table (denominator corrected, shortcut pending):**

| Metric | Failure class | Denominator | Proposed ceiling |
|---|---|---|---|
| stopped_short_rate | `correct_chain_stopped_short` | composite, FORMAT_PASS | ≤ 0.20 — see Q4 |
| shortcut_single_hop_rate | **UNDEFINED** | — | **BLOCKED** |
| wrong_chain_routing_rate | `wrong_chain_selection` | composite, FORMAT_PASS | see Q4 |
| wrong_neighbor_routing_rate | `target_chain_wrong_neighbor` | composite, FORMAT_PASS | ≤ 0.20 |
| anchor_echo_rate | `anchor_echo` | composite, FORMAT_PASS | ≤ 0.15 |

---

## Q4 — Wrong-chain ceiling

**Disposition: REVISE — lower from 0.30 to 0.20 for stress eligibility**

Addressing both framings:

**Rate over all composite items (gate metric):**  
0.30 is not compatible with stress eligibility. A cell with wrong-chain rate = 0.28 at FP16 has the model selecting the decoy chain on more than one in four composite queries at the *best* precision level. Under INT4 stress, this rate is expected to increase or change. The stress result would be: a noisy FP16 baseline plus a noisy INT4 result, with a difference that can't be interpreted cleanly. The purpose of Gate 3 is to ensure the FP16 cell is operationally clean before stress — 0.30 wrong-chain rate does not meet that bar.

Proposed revision: wrong-chain ceiling ≤ 0.20 for Gate-3 stress eligibility. A FP16 wrong-chain rate in the range 0.15–0.20 is interpretable (the decoy chain attracts ~1 in 5 to 7 composite queries). Above 0.20, the signal-to-noise ratio for Track B becomes insufficient to distinguish quantization effect from baseline noise.

**Wrong-chain share among failures (diagnostic metric only):**  
This is not an appropriate gate metric. The share among failures is: wrong_chain_selection / (total failures). It answers "what fraction of the model's errors are chain-routing errors?" This is valuable for understanding failure anatomy in Watch Conditions and per-item analysis, but it is denominator-incompatible with a gate: a cell with high correctness (5% failure rate) and all failures being wrong-chain would show 100% wrong-chain share — indicating a very clean cell, not a failure. Gates must be computed over all parseable outputs, not over failures only.

**Recommended wording addition:** include a note in the threshold document that wrong-chain rate in the range 0.15–0.20 at FP16 is a watch condition even when below the ceiling — it should be noted in the run summary and does not block advancement but warrants attention before Track B interpretation.

---

## Q5 — BPE-Jaccard blocking

**Disposition: APPROVE proposed value (j ≥ 0.50), CLARIFY blocking reason**

The proposal's statement that BPE-Jaccard is "blocked on locked tokenizer" is partially misleading and needs a wording correction.

**What Stage 0 correctly did not do:** Stage 0 was offline only — no model inference, no tokenizer calls, no `audit_round_trip()` execution. Stage 0 was correctly scoped to schema and scorer. Locking the tokenizer hash is a Gate-0 / Gate-0.5 requirement for actual runs, not a Stage 0 deliverable. There is no Stage 0 gap here.

**What is actually blocking BPE-Jaccard approval:** The proposed value j ≥ 0.50 is a reasonable starting point, but it is empirically uninspected. BPE tokenizers vary in how they segment 5-character uppercase identifiers — some may split CPQVX as a single token, others as 2–3 subword units. The value 0.50 was not derived from looking at actual BPE segmentations for this token pool; it was derived from first principles (midpoint of the overlap range). Before j = 0.50 is used as a construction constraint, the tokenizer must be locked and at least a sample of token-pool pairs must be inspected to verify that j = 0.50 places the boundary where intended.

**Required wording correction:** Replace "BLOCKED pending locked tokenizer" with: "Conditional on tokenizer lock; proposed value j ≥ 0.50 requires empirical inspection of BPE segmentations for the token pool before use as a construction constraint. Stage 0 was correctly scoped and this is not a Stage 0 gap."

---

## Q6 — Unique-assignment / UNCLASSIFIED pair

**Disposition: REVISE — tighten to ≤ 0.05 / ≥ 0.95**

The two thresholds are algebraically identical (unique_assignment_rate = 1 − UNCLASSIFIED_rate) and both are retained for reporting completeness. The question is whether 10% UNCLASSIFIED is defensible for a load-bearing gate.

It is not. Three reasons:

1. **Failure-class separability is the purpose of Gate 4b.** If 10% of outputs are UNCLASSIFIED at FP16, those outputs provide no signal to the separability analysis. For n=20 cells, 10% = 2 outputs. The separability analysis then operates over 18 data points, not 20. That is an acceptable loss if UNCLASSIFIED is truly random noise. But if UNCLASSIFIED outputs cluster (e.g., all from the same query type or context position), those 2 outputs may represent a systematic gap in the taxonomy that contaminates the full-cell interpretation.

2. **Stress comparison validity.** If UNCLASSIFIED rate increases under INT4 (a plausible outcome — novel outputs become more likely under quantization), the 10% FP16 UNCLASSIFIED baseline leaves only 10 percentage points of headroom before the increase becomes statistically significant. A 0.05 baseline leaves 15 percentage points — enough to distinguish a real increase from noise.

3. **The taxonomy was designed to be exhaustive.** 14/14 unit tests and 22/22 smoke tests covered all 7 named classes. A FP16 UNCLASSIFIED rate of 10% suggests the taxonomy has a gap that was not exposed in smoke testing. 5% (≈ 1 item in n=20) is a more appropriate operating tolerance.

**Proposed revision:**
```
unique_assignment_rate ≥ 0.95
UNCLASSIFIED / OFF-FRAME ceiling ≤ 0.05
```

**Watch condition:** UNCLASSIFIED rate > 0.02 (not a gate fail) triggers mandatory manual inspection and clustering assessment in Watch Conditions. If a cluster is identified, it is a candidate for taxonomy expansion before any Track B interpretation.

---

## Q7 — Stage 1 readiness

**Disposition: REVISE FIRST, then route to Manager**

Three items block routing in the current state:

**Blocker 1 — Gate-3 denominators unresolved (Q3).** All five Gate-3 ceilings reference undefined denominators. No Gate-3 ceiling is currently approvable. This is fixable with one pass of explicit denominator language.

**Blocker 2 — shortcut_single_hop_rate mapping undefined (Q3).** The failure class that populates this rate is not identified. Until the definition is resolved, the ceiling (≤ 0.10) cannot be approved. If shortcut_single_hop_rate is just another name for a combination of existing classes (e.g., stopped_short + anchor_echo), that must be stated. If it requires a new diagnostic, that must be stated too.

**Blocker 3 — wrong-chain ceiling too permissive (Q4).** 0.30 is not compatible with a constructibility floor claim. Needs revision to 0.20 before routing.

The following items are not blockers — they are straightforward revisions that can be incorporated in the same pass:

- Gate-2 from 0.80 → 0.875
- Dummy: add two-condition rule (ceiling 0.55, margin 0.25)
- BPE-Jaccard: wording correction (not a structural change)
- UNCLASSIFIED ceiling from 0.10 → 0.05

**Recommendation:** CS Engineer will incorporate all revisions into a revised THRESHOLD-PROPOSAL-TWOHOP-L1.md. Team Lead should confirm the shortcut_single_hop_rate definition before revision is filed — that is the only item that requires Team Lead input rather than CS action. Once definition is confirmed, revision can be filed and routed to Manager.

---

## Summary

| # | Threshold | Disposition | Revised value |
|---|---|---|---|
| 1 | Gate-2 FP16 pass rate | REVISE | ≥ 0.875 |
| 2 | Dummy ceiling | REVISE | max_dummy ≤ 0.55 AND margin ≥ 0.25 |
| 3 | Near-miss Levenshtein k | APPROVE (Manager approval still required) | k ≤ 2 |
| 4 | BPE-Jaccard j | APPROVE value, REVISE wording | j ≥ 0.50 (conditional on empirical inspection) |
| 5 | Trigram-Jaccard j | APPROVE | j ≥ 0.20 |
| 6 | Length-matched ±x | APPROVE | ± 10 tokens |
| 7 | Unique-assignment reliability | REVISE | ≥ 0.95 |
| 8 | UNCLASSIFIED ceiling | REVISE | ≤ 0.05 |
| 9a | Stopped-short ceiling | APPROVE value (denominator correction required) | ≤ 0.20, denominator = composite FORMAT_PASS |
| 9b | Shortcut single-hop ceiling | **BLOCKED** — failure class undefined | — |
| 9c | Wrong-chain ceiling | REVISE + denominator correction | ≤ 0.20, denominator = composite FORMAT_PASS |
| 9d | Wrong-neighbor ceiling | APPROVE value (denominator correction required) | ≤ 0.20, denominator = composite FORMAT_PASS |
| 9e | Anchor-echo ceiling | APPROVE value (denominator correction required) | ≤ 0.15, denominator = composite FORMAT_PASS |

**Final recommendation: REVISE FIRST**

Three blockers must be resolved before routing to Manager. One blocker (shortcut_single_hop_rate definition) requires Team Lead input. Two blockers (denominators, wrong-chain ceiling) are CS actions. Estimated one-pass revision once shortcut definition is confirmed.

— CS Engineer
