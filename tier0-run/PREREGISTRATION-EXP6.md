# Pre-Registration — Experiment 6: Compositional Seam Test (Test 1, Clean Instrument)

**Locked:** 2026-06-06  
**Status:** LOCKED — do not edit after stability screen begins.

---

## 0. Core statement

> Experiment 6 is the first clean local adjudication of the compositional seam claim under Qwen2.5-1.5B, INT8/INT4 stress, forced `ANSWER: <value>` scaffold, neutral terminal tokens, explicit chain anchors, and echo/polarity/format confounds controlled.

This experiment directly tests Test 1 (the seam hypothesis):

> **Do composite multi-hop answers fail under quantization stress while the individual component hops remain correct?**

A true seam signal requires G_content(INT4) CI to exclude zero in the positive direction, driven by SA-family primary seam items, not by format, echo, polarity, or scorer artifacts.

---

## 1. Purpose

Experiments 3–5 established that:
- INT4 quantization degrades strict format compliance on this model and task family.
- The format cliff is scaffold-sensitive: a stronger forced-format instruction largely eliminates it.
- The Exp 3/4 seam signal dissolved under content rescoring — it was a format artifact.
- Three CONTENT_LOSS events appeared in Exp 5 under the new scaffold, including one composite failure with all components passing (FA2/narrow, structurally seam-like, single item, not statistically supported).

Experiment 6 applies the instrument to a purpose-built seam task family where:
- All confounds are controlled at the task-construction level (see §3).
- Format pressure is identical across composite and component arms.
- Terminal tokens are arbitrary, non-polar, and isolated to their chain.
- Echo behavior is estimated by explicit diagnostic controls.
- Null scoring is validated by an explicit negative control.

A clean null result in this experiment is locally meaningful: it means the seam pattern does not appear under this model, stress profile, and task design. A positive result requires item audit and forced-intermediate follow-up before any claim is made.

---

## 2. Model and stress profile

| Field | Value |
|---|---|
| Model | `Qwen/Qwen2.5-1.5B-Instruct` |
| INT8 quantization | In-place via `quantize_model` (group_size=64) |
| INT4 source | `mlx-community/Qwen2.5-1.5B-Instruct-4bit` |
| Hardware | Apple Silicon (MLX, macOS 15+) |
| Decoding | temperature=0.0 (greedy, deterministic) |
| Max tokens | 512 |
| Bit-depths swept | FP16, INT8, INT4 |

---

## 3. Task families — `tasks_exp6.py`

**Task file constructed before this pre-registration was locked.** Token taxonomy, relation skeletons, and item structure are fixed in `tasks_exp6.py`. No task edits are permitted after stability screen begins.

### 3.1 SA — Primary seam items (8 items, `included_in_G=True`)

3-hop / 4-node chains. Forced-format scaffold on all arms. Explicit first-node anchor in composite question. One 1-hop distractor fact per item (broad arm, stability-screen only).

**Relation skeletons (two pre-registered templates, 4 items each):**

```
S1: {A} connects to {B}. {B} leads to {C}. {C} grants {TERMINAL}.
    Composite Q: "Starting from {A}, what terminal value does the chain reach?"
    Hop Q1: "{A} connects to what?"
    Hop Q2: "{B} leads to what?"
    Hop Q3: "{C} grants what?"

S2: {A} routes to {B}. {B} opens into {C}. {C} maps to {TERMINAL}.
    Composite Q: "Starting from {A}, what terminal value does the chain reach?"
    Hop Q1: "{A} routes to what?"
    Hop Q2: "{B} opens into what?"
    Hop Q3: "{C} maps to what?"
```

**Token hygiene rules (locked at task-construction time):**

- PRIMARY_TERMINALS (`ZUNIP MAVOQ KELDA RIVOK TANEM GLAXU VOPAR DREXM`): each appears only as the composite terminal of its designated chain. Not in any other item's context string, not as an intermediate node, not as a broad arm answer, not in any distractor fact.
- BROAD_VALUES: expected answers for broad arms only. Never primary terminals or chain intermediates.
- INTERMEDIATES: chain nodes only. Never appear as answer tokens.
- No token has a natural antonym or obvious semantic polarity pair.

**What the composite question tests:**  
Can the model follow the chain from the explicit first node ({A}) to the terminal, given all three hop facts in context? Failure cannot be attributed to person-anchor lookup — the anchor is the chain's first node, named directly in the question.

**Chain-type symmetry:** Each SA item's component checks cover exactly the 3 hops in its composite. No additional hops. No missing hops.

### 3.2 DE — Diagnostic echo controls (4 items, `included_in_G=False`)

Estimate the rate of intermediate-token echo under the forced-format scaffold and quantization stress. Not seam evidence.

- **DE-QE (2 items):** 1-hop question; echo risk = model outputs the question subject instead of the correct value.
- **DE-PI (2 items):** 2-hop composite; echo risk = model outputs the penultimate chain node instead of the terminal.

### 3.3 NC — Null control (1 item, `included_in_G=False`)

Scorer/null validation. Expected value absent from context at all rungs. Failure is the correct result. See §8 for halt condition.

### 3.4 AC — Atomic controls (2 items, `included_in_G=False`)

1-hop person→value sanity checks. Verify basic 1-hop retrieval is functional at each quantization rung.

---

## 4. Inclusion and exclusion rules

### 4.1 Items included in G_content / G_strict

```
INCLUDED:  SA-family primary seam items (SA1–SA8)

EXCLUDED:  DE echo diagnostics
           NC null control
           AC atomic controls
           broad arms (all families)
           forced-intermediate follow-ups (§12)
```

Broad arm is stability-screen only. It does not enter G computation for or against the seam claim.

### 4.2 Per-item eligibility for G computation

An SA item is eligible for G_content at a given stress rung w only if:

```
FP16 composite content_slot_score = 1
FP16 all component content_slot_score = 1
FP16 stability screen classification = STABLE
```

If any FP16 condition fails: exclude the item from G. No partial credit. No "nearly passed."

**Minimum eligible count:** ≥ 6 stable substantive SA pairs required to proceed to stress sweep. If fewer than 6 SA items are STABLE after the screen, report Outcome E (task construction failure) and do not run INT8/INT4.

---

## 5. Scoring hierarchy — unchanged from Exp 4/5

Scorer is not modified. All 9 pre-registered unit tests from PREREGISTRATION-EXP4.md §9 must pass before any run.

| Metric | Primary use |
|---|---|
| `content_slot_score` | Content/capability claims — PRIMARY for seam readout |
| `strict_format_score` | Format-compliance claims only |
| `partial_content_score` | COMPOUND_NOUN_DROP diagnostic only |

**Hierarchy rule (locked):** content_slot_score is the primary readout for seam claims. G_strict movement without G_content movement is a format artifact, not a seam signal.

**Failure taxonomy (locked from PREREGISTRATION-EXP4.md):**  
PASS > FORMAT_COMPLIANCE_LOSS > COMPOUND_NOUN_DROP > CONTENT_LOSS > ROBUST_WRONG

Additional classification for Exp 6 diagnostics:

| Class | Condition |
|---|---|
| INPUT_ECHO_ERROR | DE item: output contains echo_wrong_value and not expected value |
| FLOOR_DIAGNOSTIC | DE item: FP16 content = 0 (excluded from echo-rate interpretation) |
| NULL_CONTROL / EXPECTED_FLOOR | NC1: content = 0 (correct behavior) |

---

## 6. G_content formula (LOCKED)

```
G_content(w) = R_component_content(w) − R_composite_content(w)
```

Where:

```
R_composite_content(w)
  = mean( content_slot_score(composite, item, w) )
    over eligible SA items

R_component_content(w)
  = mean( mean( content_slot_score(comp_i, item, w) ) for each comp_i )
    over eligible SA items
```

Bootstrap CI: 1000 iterations, seed=0, on the mean G_content across eligible pairs.

**Sign convention:** Positive G_content means components retain content at higher rate than composites. This is the seam direction. Negative G_content means composites outperform components (not the seam direction).

**G_strict(w)** computed identically but using `strict_format_score`. Primary for format-compliance tracking only.

---

## 7. Diagnostic echo rules (LOCKED)

DE-QE and DE-PI items estimate whether input-echo behavior is active under the forced-format scaffold at each stress rung. They are never seam evidence.

**Inclusion gate:** A DE item enters echo-rate interpretation only if FP16 content passes (`content_slot_score = 1`). If FP16 content fails, classify as FLOOR_DIAGNOSTIC and exclude from echo-rate interpretation.

**Echo classification:** If a DE item's output at any rung contains the item's `echo_wrong_value` and does not contain the expected value: classify as INPUT_ECHO_ERROR.

**Interpretation:**
```
If INT4 INPUT_ECHO_ERROR on DE-QE item(s):
  QE-type echo is active at INT4 under this scaffold.
  Flag any SA component-check failures where the failed output matches the
  question subject. These failures may be echo-driven, not seam-driven.

If INT4 INPUT_ECHO_ERROR on DE-PI item(s):
  PI-type echo is active at INT4.
  Flag any SA composite failures where the failed output matches a chain
  intermediate rather than the terminal. These may be chain-truncation echo.

If DE items pass at INT4:
  Echo confound not demonstrated as active in this run.
  Does not prove echo is absent; shows it did not fire on these items.
```

Echo item failures reduce confidence in SA composite failures that share the same error pattern. They do not independently support or oppose the seam claim.

---

## 8. Null-control rule (LOCKED)

NC1 validates that `content_slot_score` returns 0 when the expected token is absent from context.

**Expected behavior at every rung:** content = 0, strict = 0.

**Halt condition:**
```
If NC1 content_slot_score = 1 at any rung:
  STOP.
  Do not interpret any Exp 6 results until scorer or model-hallucination
  audit is complete. The scorer may be returning false content credit,
  or the model may be hallucinating a reserved token.
```

NC1 is not a model failure. It is a guardrail. Its EXPECTED_FLOOR classification is correct behavior, not a miss.

---

## 9. Stability screen gate

Same protocol as Exp 3 (`run_stability_screen.py`), run with Exp 5/6 forced-format paraphrase strings:

```
PARAPHRASE_FROM: "Respond using only this exact format with nothing before or after: ANSWER:"
PARAPHRASE_TO:   "Your entire response must be exactly this and nothing else: ANSWER:"
```

**STABLE** classification requires:
- narrow original = 1.0 (content_slot_score ≥ 0.5 would be ambiguous; exact match enforced via `score_exact`)
- narrow paraphrase = 1.0
- all component checks ≥ 0.5
- broad ≥ 0.5

**Classifications:** STABLE, BOUNDARY, COMP_FAIL, BROAD_FAIL, FLOOR — as in Exp 3.

**DE items:** included in stability screen to verify FP16 behavior. If FLOOR at FP16 (original narrow fails): classify as FLOOR_DIAGNOSTIC, exclude from echo-rate interpretation at all rungs. DE items proceed to stress sweep regardless of stability classification.

**NC1:** expected to FLOOR on narrow arm (correct behavior). Not subject to standard stability thresholds. Broad arm tests TURVL (present in context) — expected to PASS.

**AC items:** standard stability thresholds apply. Exclusion of AC does not affect G computation (AC is not included in G).

**Minimum gate:** ≥ 6 STABLE SA items. If fewer: report Outcome E. Do not run INT8/INT4.

---

## 10. Runner changes required before stress sweep

The following changes to `run_tier0.py` must be made and verified before the INT8/INT4 sweep:

```
1. Respect included_in_G field:
   G_content and G_strict computed only over items with included_in_G=True.
   All other items scored and logged but excluded from G metrics.

2. Respect diagnostic_gate field:
   DE items: if FP16 content_slot_score < 1, mark as FLOOR_DIAGNOSTIC
   in output; exclude from echo-rate summary.

3. NC1 flag condition:
   If NC1 content_slot_score = 1 at any rung, emit a hard-stop warning
   and halt before writing results. Do not silently continue.

4. Echo-rate summary:
   For each DE item that passes the diagnostic gate, report whether
   INT4 output contains echo_wrong_value. Compute:
     QE_echo_rate = INPUT_ECHO_ERRORs / eligible DE-QE items
     PI_echo_rate = INPUT_ECHO_ERRORs / eligible DE-PI items

5. Per-item raw output logging:
   Emit for each item/arm/rung/calibration:
     {pid, arm, rung, calib, strict, content, partial, failure_class,
      output (truncated to 400 chars), expected, timestamp}

6. Source/provenance fields in result JSON:
   {model, model_4bit, tasks, calib, bits_swept, run_timestamp,
    unit_tests_passed: true/false}

7. Broad arm excluded from G:
   Broad arm scores logged but not included in R_composite_content
   or R_component_content.
```

**Scorer is not modified.** The 9 pre-registered unit tests gate each run as before.

---

## 11. Outcome table (LOCKED)

| Outcome | Definition | Action |
|---|---|---|
| **A — seam signal** | G_content(INT4) CI excludes zero (positive direction); SA items drive it; composites fail content while components pass; not explained by echo, format, polarity, scorer, or FP16 floor | Item audit required. Forced-intermediate follow-up (§12) required before any claim promotion. |
| **B — local null** | G_content flat (CI includes zero); no repeated composite-fail/components-pass pattern across SA items | Seam locally unsupported under this model, task design, and stress profile. Log as null, specify conditions. |
| **C — echo artifact** | Apparent composite failures dominated by INPUT_ECHO_ERROR; DE echo controls fire at INT4 | No seam claim movement. Echo confound active. Redesign anchor or question format. |
| **D — format artifact** | G_strict CI excludes zero; G_content CI includes zero | Format issue, not seam. Consistent with Exp 4 finding. |
| **E — task construction failure** | < 6 SA items stable at FP16; or NC1 fails scorer validation; or SA components broadly fail at baseline | No claim movement. Diagnose and redesign before rerun. |
| **F — surprise content loss** | Content loss appears broadly across both components and composites; G_content ambiguous or flat | Audit before interpretation. Do not attribute to seam without item-level analysis. |

**Calibration-invariance gate:** Results count only if G_content and G_strict rankings are invariant under calib=code and calib=prose. Same limitation as Exp 4/5: bit-identical results expected since calib label does not alter prompts. Invariance confirms no calibration-label artifact; does not provide independent replication across different prompt distributions.

**Kill conditions for Outcome A promotion:**
- G_content CI includes zero
- G_content direction flips across calibrations
- Echo or format artifact explains composite failures before forced-intermediate follow-up is complete
- Item audit reveals < 2 clean seam-structured items driving the signal

---

## 12. Forced-intermediate follow-up rule (LOCKED)

Forced-intermediate follow-up is a secondary diagnostic. It is triggered only after the primary stress sweep completes, and only for items meeting the trigger condition. It is excluded from primary G_content / G_strict computation.

**Trigger condition:**
```
SA item: composite content_slot_score = 0 at stressed rung
AND
SA item: all component content_slot_score = 1 at same rung
```

**Follow-up procedure:**
Supply the correct value at the penultimate hop as a prefix, then ask the terminal question:

```
Context: [same as item's context]
Intermediate: The value at [penultimate_node] is [penultimate_node_answer].
Question: [same composite question]
Format: [same _FMT]
```

**Interpretation:**
```
If follow-up content = 1 (recovery):
  Composite failure is localized to chain-following from scratch.
  Supplying the intermediate enables correct completion.
  Candidate handoff/seam diagnostic strengthened.

If follow-up content = 0 (no recovery):
  Failure is not cleanly localized to the chain handoff.
  Audit required before interpretation.

If trigger never fires (no composite fail + all components pass at same rung):
  Forced-intermediate follow-up is not run.
  Log: FORCED_INTERMEDIATE_NOT_TRIGGERED.
```

---

## 13. Claim-status consequences

**Primary seam claim (Test 1):**  
Promoted to Outcome A only if all of the following hold:
- G_content(INT4) CI excludes zero, positive direction, calibration-invariant
- SA items drive the signal; item audit confirms composite-fail/component-pass structure in ≥ 2 independent items
- Echo diagnostic items do not explain the composite failures
- Forced-intermediate follow-up runs and supports the handoff interpretation
- NC1 passes scorer validation at all rungs

Absent all of these: claim remains open but locally unsupported.

**Format-degradation finding (Test 2, from Exp 4/5):**  
Resolved as scaffold-sensitive. G_strict movement without G_content movement in Exp 6 would replicate this finding but does not constitute a new seam claim.

**Composite seam hypothesis note:**  
One or two SA items showing composite-fail/component-pass is diagnostic only. Aggregate G_content CI must exclude zero before any seam claim movement. Single items are logged as candidates, not claim evidence.

---

## 14. Ordering constraint

```
1. tasks_exp6.py constructed                           ← DONE
2. PREREGISTRATION-EXP6.md locked                      ← you are here
3. run_tier0.py updated (§10 runner changes)
4. Scorer unit tests verified (9 pre-registered cases)
5. FP16 stability screen run on tasks_exp6
6. tasks_exp6_stable.py auto-generated
7. Calibration A run (calib=code)
8. Calibration B run (calib=prose) after A is archived
9. Forced-intermediate follow-up if triggered (§12)
10. Results recorded in RESULTS-EXP6.md
```

Do not run the stress sweep before the runner changes (§10) are verified. Do not run INT8/INT4 before ≥ 6 SA items pass the FP16 stability screen.
