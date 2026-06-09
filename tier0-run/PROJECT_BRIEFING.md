# PROJECT_BRIEFING.md — Cold-Start Briefing for Incoming Engineer

**Last updated:** 2026-06-07  
**Purpose:** Complete context document. Allows any engineer (or new AI instance) to resume work without prior conversation history. Read this before touching any file.

---

## 1. What this project is

We are running a controlled quantization study on Apple Silicon using MLX. The core question is:

> Does INT4 quantization break **compositional knowledge** more than **isolated component knowledge**?

The hypothesis is called the **seam claim**:

> After INT4 quantization, a model's ability to answer a composite multi-hop question degrades more than its ability to answer the individual hop components that make up that question.

If true, this suggests that the knowledge connecting facts across a chain — the "seam" — is stored in a way that is disproportionately fragile under compression.

This has not been proven. After seven experiments, the seam claim is **open and unadjudicated**. Every experiment so far has either hit a task construction problem or a format artifact before producing clean INT4 data.

---

## 2. Team roles

```
Manager:          Elias (user) — sets priorities, approves direction
Team Lead:        Elias (user) — experiment design, ledger, next-run instructions
Senior Engineer:  External reviewer — technical critique, catches design flaws
Contributors 1–5: Outside reads, objections, literature angles
CS Engineer:      Claude (AI) — executes runs, reports outputs, applies harness changes
```

Decision rule: Contributors advise. Senior Engineer critiques. CS Engineer runs. Team Lead recommends. Manager decides.

The CS Engineer does not make design decisions. The CS Engineer executes instructions exactly and holds on any ambiguity.

---

## 3. Research hypothesis (formal)

**Primary claim (Test 1 — seam):**

```
G_content(INT4) > 0, with CI lower bound > 0, calibration-invariant.

where:
  G_content(w) = R_component_content(w) − R_composite_content(w)
  R_component_content(w)  = mean(component content scores @ w) / mean(component content scores @ FP16)
                            over component checks with FP16 content = 1
  R_composite_content(w)  = narrow_content @ w / narrow_content @ FP16
                            over SA items with FP16 narrow_content = 1
  w = quantization rung (INT8 or INT4)
```

G_content > 0 means components degrade less than the composite under quantization — the seam is fragile.

**Calibration invariance requirement:** Two calibration runs (calib=code, calib=prose) must produce identical G_content rankings. The calibration label does not alter any prompt — it is a provenance tag only.

**Key rule (locked in PREREGISTRATION-EXP4.md):** A G_strict-only drop that does not appear under G_content scoring is a format artifact, not a seam signal.

---

## 4. Instrument

### 4.1 Dual scorer (locked in PREREGISTRATION-EXP4.md §3)

Two scorers run on every item:

**`strict_format_score(output, expected)`**
- Exact match after whitespace/case normalization
- Primary for format-compliance claims

**`content_slot_score(output, expected)`**
- Token-phrase matching of the expected value anywhere in output
- Primary for content/capability claims
- Avoids false positives where the value is a substring of an unrelated token

**`partial_content_score(output, expected)`**
- Fraction of expected value tokens found in output
- Diagnostic only — used for COMPOUND_NOUN_DROP detection

### 4.2 Failure taxonomy (locked in PREREGISTRATION-EXP4.md §4)

Priority order (first matching class wins):

```
PASS               strict=1
FORMAT_COMPLIANCE_LOSS  strict=0, content=1  (right answer, wrong format)
COMPOUND_NOUN_DROP      strict=0, content=0, partial>0  (part of multi-word answer present)
CONTENT_LOSS            strict=0, content=0, partial=0  (wrong answer entirely)
ROBUST_WRONG            cross-rung: content=0 at baseline AND all stressed rungs, same output
INPUT_ECHO_ERROR        DE items only: model returns the echo_wrong_value token
FLOOR_DIAGNOSTIC        DE items: FP16 content=0, excluded from echo-rate interpretation
```

### 4.3 Unit tests (locked in PREREGISTRATION-EXP4.md §9)

9 pre-registered cases. Run automatically before every model load:
```bash
python3 -c "from run_tier0 import run_unit_tests; run_unit_tests()"
```
If any unit test fails, do not proceed.

### 4.4 Outcome table (locked in PREREGISTRATION-EXP6.md §11)

| Outcome | G_content CI | Calibration | NC | Meaning |
|---|---|---|---|---|
| A | lo > 0 | invariant | 0 | Seam signal — primary claim supported |
| B | CI includes 0 | — | 0 | Null result |
| C | hi < 0 | — | 0 | Inverse: component degrades faster than composite |
| D | G_strict signal, G_content flat | — | 0 | Format artifact; no seam signal |
| E | — | — | — | Task failure: <6 stable SA pairs at FP16 |
| F | lo > 0 | calibration-variant | 0 | Surprise content loss; not a clean seam signal |

---

## 5. Task structure (Exp 6–7 design)

Each task file contains 15 items in four families:

| Family | Role | Count | included_in_G |
|---|---|---|---|
| SA | Primary seam items (3-hop/4-node chains) | 8 | True |
| DE | Diagnostic echo controls | 4 | False |
| NC | Null control (scorer validation) | 1 | False |
| AC | Atomic controls (1-hop sanity checks) | 2 | False |

**SA item structure:**
- `narrow` arm: full chain traversal ("Starting from A, what terminal value does the chain reach?")
- `broad` arm: simple 1-hop lookup on the distractor fact ("X holds what?")
- `component_checks`: 3 individual hop questions (one per hop in the chain)

**SA context pattern (Exp 7 design — locked):**
```
DISTRACTOR_ENTITY holds BROAD_VALUE.
A connects to B. B leads to C. C grants TERMINAL.
DECOY_ENTITY marks DECOY_VALUE.
```
- Distractor fact is first (prevents first-position terminal anchoring)
- Decoy fact is last (prevents last-position terminal anchoring)
- Terminal is at position 8 of 10 ALL-CAPS tokens (neither first nor last)

**S1 skeleton (Exp 7 only):**
```
{A} connects to {B}. {B} leads to {C}. {C} grants {TERMINAL}.
Component Q templates: "{A} connects to what?"  "{B} leads to what?"  "{C} grants what?"
```

**DE items:**
- DE-QE (2 items): 1-hop, estimates question-entity echo rate
- DE-PI (2 items): 2-hop composite, estimates penultimate-intermediate echo rate
- Gate: if FP16 content=0, classify as FLOOR_DIAGNOSTIC, exclude from echo-rate interpretation

**NC item:**
- Expected answer token is absent from context
- If content_slot_score > 0 at any rung: HALT — scorer audit required

**AC items:**
- Two 1-hop facts per item; narrow and broad ask about different entities
- Decoy fact last (prevents last-value anchoring)

---

## 6. Experiment history

### Exp 1 (Tier 0A–0C) — Qwen2.5-7B, 3–5-hop tasks
Outcome: Flat / task ceiling. Model too capable for short chains at FP16; no degradation signal.

### Exp 2 — Qwen2.5-7B, 6–7-hop tasks
Outcome: Flat / local null. No seam signal.

### Exp 3 — Qwen2.5-1.5B, 6–7-hop tasks
Outcome: Apparent Outcome C (strict) — G_strict dropped at INT4. Rescored with content scorer: format artifact. The strict-only drop disappeared under content scoring.
**Lesson learned:** A strict-only drop is a format artifact, not a seam signal. This rule was locked into the pre-registration for all subsequent experiments.

### Exp 4 — Qwen2.5-1.5B, 6–7-hop tasks, dual scorer from the start
Outcome: Outcome C — calibration-invariant format cliff under dual scoring. G_strict still shows drop; G_content is flat. This confirmed the Exp 3 finding: the drop is format-compliance loss, not content loss.

### Exp 5 — Qwen2.5-1.5B, 6–7-hop tasks, forced-format instruction
Change: Stronger format instruction added ("Respond using only this exact format with nothing before or after: ANSWER:"). This was the Exp 5 scaffold, which became the standard for all subsequent experiments.
Outcome: G (format cliff disappears). G_strict CI includes zero. G_content CI includes zero.
**Key finding:** Format cliff was scaffold-sensitive — a stronger explicit instruction eliminated it. 3 CONTENT_LOSS items appeared at INT4 on different items than the format failures (not causally linked). Seam claim still open.

### Exp 6 — Qwen2.5-1.5B, 3-hop/4-node seam design, first clean seam attempt
New design: shorter chains, neutral synthetic ALL-CAPS tokens, explicit anchor, SA-only G_content, DE/NC/AC diagnostics, forced-format scaffold from Exp 5, dual scorer from the start.
Stability screen outcome: 3/8 SA stable (SA2, SA3, SA7). Threshold not met. **Outcome E.**
**Construction artifacts found:**
1. Last-value distractor anchoring: distractor fact appended LAST in context. Model returned the distractor value instead of the chain terminal on a subset of items.
2. S2 verb compound-output: "opens into" caused the model to reproduce the full relation sentence on component checks instead of responding with a single token.

### Exp 7 — Qwen2.5-1.5B, construction repair of Exp6
Changes: distractor fact moved to FRONT of context; decoy fact added to END ("DECOY_ENTITY marks DECOY_VALUE."); S1 skeleton only (no S2).
Stability screen outcome: 3/8 SA stable (SA1, SA3, SA4). Threshold not met. **Outcome E.**
**Construction artifacts found (taxonomy corrected 2026-06-07 from provenance check):**
1. Pattern A — First-value anchoring (SA2): model returns the distractor broad value (first in context) on hop-1/2 component checks.
2. Pattern B — Last-context-position anchoring on decoy (SA6): model returns BROXN, the decoy_value (last sentence in context), on hop-1/2 checks. Terminal is NORVA — not returned. This is last-position anchoring on the decoy, not the terminal.
3. Pattern C — Terminal over-retrieval (SA8): flumb_nakvi check returns VEFLM (chain terminal) instead of NAKVI (expected intermediate). Last context value is WULFT (decoy) — not returned. Model over-traverses to the terminal.
4. Pattern D — Penultimate-node return on narrow (SA5, SA7): narrow original fails; narrow paraphrase passes. Model returns a mid-chain entity on the original phrasing.
**Key structural finding:** Hop-3 component checks always pass. Hops 1 and 2 are the unstable layer. Full 5-fact context (distractor + chain + decoy) creates anchoring noise for 1-hop retrieval at intermediate hops.

---

## 7. Current status (2026-06-07)

```
Experiment:     Exp8B (Branch F)
Status:         NOT FEASIBLE — Arm 2B locked, no further repair loop authorized
Pass count:     6/8 (threshold ≥7/8 not met)
Numeric OOC:    0 (Condition 2 met)
Stress sweep:   Not run
Seam claim:     Open, unadjudicated
Provenance:     Clean
Next direction: Requires Manager / Team Lead decision
```

**Exp8 / Exp8B summary:**
- Exp8 Arm 2 (n=8): 6/8 pass. Both failures at target_pos=2: numeric OOC returns ("0", "10"). NOT FEASIBLE.
- Exp8B Arm 2B (n=8): Same items, query wording changed. 6/8 pass. Numeric OOC eliminated (Condition 2 met). New failures: off-by-one positional anchoring at target_pos=2 (L2_03) and target_pos=3 (L2_04). NOT FEASIBLE.
- Exp8B is the final unconditional Arm 2 construction attempt. No Exp8C without explicit Manager / Team Lead decision.

**Decoding determinism (CLOSED — manuscript dependency):**
All Exp6, Exp7, Exp8, Exp8B runs: FP16, temp=0.0, greedy, single draw per item. Exp6/Exp7 max_tokens=512; Exp8/Exp8B max_tokens=16. No seed. Provenance gap: Exp6/Exp7 decoding settings in source code only, not stored in JSON artifacts.

---

## 8. File inventory

```
run_tier0.py                      — Main harness. Dual scorer, unit tests, G computation,
                                    DE echo diagnostic, NC halt, provenance fields.

run_stability_screen.py           — FP16 stability screen. Runs each item twice (original +
                                    paraphrase prompt). Dual scoring, timestamps, manifest hash.

tasks_exp6.py                     — Exp6 task file (15 items). Has construction defects.
                                    Do not use for stress sweep.

tasks_exp7.py                     — Exp7 task file (15 items). Has construction defects.
tasks_exp7_stable.py              — Auto-generated. STABLE items from Exp7 screen (SA1/SA3/SA4
                                    + DE/AC controls). Do NOT use for stress sweep.

tasks_exp8.py                     — Exp8 Arm 2 task file (n=8). Three-axis scorer.
                                    26-check validator. Manifest hash (approved):
                                    sha256:14129d0bfe2cae1c3e4d817a8423eaf5513665741c04f1d388ac8da34a9074de

tasks_exp8b.py                    — Exp8B Arm 2B task file (n=8). Exact Exp8A items,
                                    Exp8B query wording only. 32-check validator (6 extra
                                    reuse-verification checks). Manifest hash (approved):
                                    sha256:695b1ac90aa0745765f9785435f527757a248f4ad27a85ce8f249230610ec56e

fp16_screen_exp8_arm2.py          — Exp8 Arm 2 FP16 runner.
fp16_screen_exp8b.py              — Exp8B Arm 2B FP16 runner.

fp16_screen_exp8_arm2_1780781863.json  — Exp8 Arm 2 raw outputs. 6/8 pass. NOT FEASIBLE.
fp16_screen_exp8b_1780789038.json      — Exp8B Arm 2B raw outputs. 6/8 pass. NOT FEASIBLE.

stability_screen_1780771434.json  — Exp6 stability screen results.
stability_screen_1780776502.json  — Exp7 stability screen results. Full provenance.
stability_screen_exp6_log.txt     — Console log from Exp6 stability screen.
stability_screen_exp7_log.txt     — Console log from Exp7 stability screen.

PREREGISTRATION-EXP4.md          — Scorer definitions, failure taxonomy, unit tests. LOCKED.
PREREGISTRATION-EXP5.md          — Forced-format scaffold spec. LOCKED.
PREREGISTRATION-EXP6.md          — Exp6 seam design, G formula, outcome table. LOCKED.
PREREGISTRATION-EXP7.md          — Exp7 construction repair spec. LOCKED.

RESULTS-EXP2.md                   — Exp2 results. Flat/local null.
RESULTS-EXP3.md                   — Exp3 results. Format artifact discovery.
RESULTS-EXP4.md                   — Exp4 results. Dual scorer validation, Outcome C.
RESULTS-EXP5.md                   — Exp5 results. Outcome G, cliff disappears.
RESULTS-EXP6.md                   — Exp6 results. Outcome E. Construction artifact analysis.
RESULTS-EXP8-ARM2-FEASIBILITY.md  — Exp8 Arm 2 full results. Three-axis scoring. NOT FEASIBLE.
RESULTS-EXP8B.md                  — Exp8B full results. Wording comparison, bit-stability. NOT FEASIBLE.

EXPERIMENT_LOG.md                 — Single unified log. All experiments Tier0 through Exp8B.
                                    Includes master ledger, claim status, decoding provenance.
                                    Primary reference document. Keep this up to date.

regression_check_exp3.py          — Offline rescore validation tool (Exp3 outputs).
tasks_exp3.py / tasks_exp2.py     — Earlier task definitions (reference only).
```

---

## 9. How to run

### Verify scorer unit tests
```bash
python3 -c "from run_tier0 import run_unit_tests; run_unit_tests()"
```

### Validate a task file
```bash
python3 tasks_exp7.py
# Prints pass/fail for all 11 static checks + manifest hash.
```

### Verify manifest hash before any run
```bash
python3 -c "
import hashlib
from pathlib import Path
h = hashlib.sha256(Path('tasks_exp7.py').read_bytes()).hexdigest()
print(f'sha256:{h}')
"
# Compare to approved hash before proceeding.
```

### Run FP16 stability screen
```bash
python3 run_stability_screen.py \
  --model Qwen/Qwen2.5-1.5B-Instruct \
  --tasks tasks_exp7 \
  --model-4bit mlx-community/Qwen2.5-1.5B-Instruct-4bit \
  --out-tasks tasks_exp7_stable.py
```

### Run stress sweep (Calibration A — only after Team Lead approval and ≥6 stable SA)
```bash
python3 run_tier0.py \
  --model Qwen/Qwen2.5-1.5B-Instruct \
  --bits 16 8 4 \
  --calib code \
  --tasks tasks_exp7_stable \
  --model-4bit mlx-community/Qwen2.5-1.5B-Instruct-4bit
```

### Run Calibration B (after Calibration A is archived)
```bash
python3 run_tier0.py \
  --model Qwen/Qwen2.5-1.5B-Instruct \
  --bits 16 8 4 \
  --calib prose \
  --tasks tasks_exp7_stable \
  --model-4bit mlx-community/Qwen2.5-1.5B-Instruct-4bit
```

---

## 10. Pre-registered ordering constraint

For any experiment, the ordering is locked:

```
Pre-registration (locked before task construction)
  → Task file written to satisfy pre-registration rules
  → Static validation (python3 tasks_expN.py) — must pass
  → Manifest hash verified and approved by Team Lead
  → Scorer unit tests (run_unit_tests()) — must pass
  → FP16 stability screen
  → Team Lead approval to proceed
  → If ≥6 stable SA: Calibration A (calib=code)
  → Calibration B (calib=prose)
  → Forced-intermediate follow-up if trigger condition fires
  → RESULTS-EXPn.md written
```

**Never run INT8/INT4 before the stability gate passes and Team Lead explicitly approves.**

---

## 11. Key design rules (all locked)

1. **Dual scoring always.** Every item scored with both strict_format_score and content_slot_score. G_content is the primary metric for seam claims.

2. **A strict-only drop is a format artifact.** If G_strict drops but G_content does not, it is not a seam signal.

3. **G computed over SA items only.** included_in_G=True for SA family only. DE, NC, AC are always excluded from G.

4. **NC halt condition.** If NC1 content > 0 at any rung, stop immediately. The scorer found the absent token — something is wrong.

5. **Calibration invariance required for Outcome A.** Both calib=code and calib=prose must produce identical G_content rankings.

6. **Forced-intermediate is post-hoc diagnostic only.** Trigger: composite content fails AND all component checks pass at stressed rung. Does not enter primary G computation.

7. **Scaffold standard.** All prompts use: `"Respond using only this exact format with nothing before or after: ANSWER: <value>"`. Paraphrase arm uses: `"Your entire response must be exactly this and nothing else: ANSWER: <value>"`.

8. **Token design rules.** All answer tokens: 5–6 chars, all-caps, no English word embedded, no natural antonym, single token, no space. All pools (PRIMARY_TERMINALS, BROAD_VALUES, INTERMEDIATES, DECOY_VALUES) must be disjoint.

9. **Static validation before every run.** The task file must contain validate_tasks() and all checks must pass. Manifest hash must match the Team Lead-approved hash.

10. **Do not salvage partial results.** If stability gate fails (Outcome E), do not run stress sweep on the stable subset. Do not treat partial results as evidence about the seam.

---

## 12. What happened to the seam claim

After nine experiments (Tier0 A/B/C, Exp2–8B):

- Exp 1–2: Task ceiling (model too capable or wrong task family).
- Exp 3–4: Format artifact discovered and resolved. Dual scorer locked.
- Exp 5: Scaffold sensitivity resolved. Forced-format instruction established as standard.
- Exp 6: First clean seam design. Stability gate caught last-value distractor anchoring and S2 verb compound-output before INT4 ran.
- Exp 7: Construction repair. Composite question stabilized for SA1/SA3/SA4. Component checks unstable at hops 1–2 due to anchoring on decoy (Pattern B) and terminal over-retrieval (Pattern C).
- Exp 8 Arm 2: Load-matched single-lookup feasibility screen. 6/8. Numeric OOC returns ("0", "10") at target_pos=2. NOT FEASIBLE.
- Exp 8B Arm 2B: Single-variable wording test on Exp8A items. 6/8. Numeric OOC eliminated. New off-by-one positional anchoring failures. NOT FEASIBLE. Branch F locked.

**The seam has not been tested.** The instrument is sound. No experiment has yet passed the stability gate with ≥6 stable SA items and run the full stress sweep. The G_content formula, dual scorer, and outcome table are ready. Task construction and feasibility screening have been the blocking constraint across all nine experiments.

**Scorer class registry (locked):** 9 content classes. RETURNED_NON_CONTEXT_TOKEN is flat (no subclasses). Near-miss / token-fidelity distinctions are post-hoc diagnostic annotations for the manuscript, not scorer subclasses. CHECK_23 asserts exactly 9 classes.
