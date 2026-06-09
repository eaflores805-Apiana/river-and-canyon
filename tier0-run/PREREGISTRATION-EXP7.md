# PREREGISTRATION-EXP7.md — Experiment 7: Primary Seam Test (Construction Repair)

**Status:** Pre-registered  
**Date:** 2026-06-06  
**Supersedes:** Exp6 (same hypothesis; construction artifacts repaired)  
**Depends on:** PREREGISTRATION-EXP6.md (task logic, G formula, scoring, outcome table — all unchanged)

---

## §0 Core statement

Experiment 7 repairs the two construction artifacts identified in Exp6 (RESULTS-EXP6.md §6) while preserving the seam-test logic in full. This is not a new hypothesis. It is a construction repair.

Changes from Exp6:
1. Distractor fact moved to the **front** of the context (was appended at the end).
2. S1 relation skeleton (`connects / leads / grants`) used for **all** SA items (S2 skeleton dropped for this batch).

Everything else — scaffold, scorer, G formula, diagnostic structure, outcome table, ordering constraint — is unchanged from PREREGISTRATION-EXP6.md and the locked elements in PREREGISTRATION-EXP4.md.

---

## §1 Hypothesis

Unchanged from PREREGISTRATION-EXP6.md §1.

Compositional seam claim: after INT4 quantization, the probability of correct composite answer drops more than the probability of correct component answers, relative to FP16 baseline. G_content(INT4) > 0 with CI lower bound > 0, calibration-invariant.

---

## §2 Instrument

Unchanged. Dual scorer locked in PREREGISTRATION-EXP4.md §3. Nine unit tests locked in PREREGISTRATION-EXP4.md §9. Runner: `run_tier0.py` as updated for Exp6 (PREREGISTRATION-EXP6.md §10). No runner changes required for Exp7.

---

## §3 Task families

Same counts as Exp6:

| Family | Role | Count | included_in_G |
|---|---|---|---|
| SA | Primary seam items | 8 | True |
| DE | Diagnostic echo controls | 4 | False |
| NC | Null control | 1 | False |
| AC | Atomic controls | 2 | False |
| **Total** | | **15** | |

---

## §4 G inclusion rules

Unchanged from PREREGISTRATION-EXP6.md §4.

G_content and G_strict are computed only over SA items (included_in_G=True). All DE, NC, and AC items are excluded from G in all cases.

Minimum for G computation: ≥6 stable SA items (§11). If fewer than 6 SA items survive the stability screen, report Outcome E and do not run INT8/INT4 sweep.

---

## §5 Context ordering rule (CHANGED from Exp6 — locked)

**The distractor fact MUST appear FIRST in the context, before the chain.**

Required format:

```
{DISTRACTOR_ENTITY} holds {BROAD_VALUE}. {A} connects to {B}. {B} leads to {C}. {C} grants {TERMINAL}.
```

Not:

```
{A} connects to {B}. {B} leads to {C}. {C} grants {TERMINAL}. {DISTRACTOR_ENTITY} holds {BROAD_VALUE}.
```

Rationale: Exp6 identified last-value anchoring as a construction artifact. Moving the distractor to the front places the chain terminal as the last token in context, directly inverting the artifact.

This rule applies to all SA items and to any DE-PI item with a distractor fact. DE-QE items (2-token context, no distractor fact in the chain) are unaffected.

---

## §6 Relation skeleton rule (CHANGED from Exp6 — locked)

**S1 skeleton only for all SA items in Exp7.**

```
S1: {A} connects to {B}. {B} leads to {C}. {C} grants {TERMINAL}.
    Component Q templates:
      "{A} connects to what?"
      "{B} leads to what?"
      "{C} grants what?"
```

The S2 skeleton (`routes / opens into / maps to`) is not used in Exp7. Reintroduction of verb variation is deferred to a later experiment after a clean stability gate is established.

Rationale: Exp6 showed that `opens into` triggers full-fact sentence reproduction on component prompts (FORMAT_COMPLIANCE_LOSS). `routes` caused a chain-jump failure. Eliminating S2 removes both compound-output and chain-jump artifacts for this batch.

This rule applies to all 8 SA items. DE items may use any short relation verb appropriate to their structure.

---

## §7 Token design rules

All token pools are refreshed for Exp7. No token from any Exp6 pool (PRIMARY_TERMINALS, BROAD_VALUES, INTERMEDIATES, DIAGNOSTIC_NODES, DISTRACTOR_ENTITIES) may be reused in Exp7.

Token design rules (unchanged from Exp6):

**PRIMARY_TERMINALS** (composite answer tokens, SA family):
- 8 tokens, one per SA item
- Single token, no space, all-caps
- 5–6 characters
- No English word embedded
- No natural antonym
- Chain-exclusive: each token appears only as the terminal of its designated SA chain and nowhere else in any Exp7 context

**BROAD_VALUES** (broad arm expected answers):
- One per SA, DE, NC, AC item (as needed by the broad arm)
- Not from PRIMARY_TERMINALS or INTERMEDIATES pools
- Same length / format rules as PRIMARY_TERMINALS

**INTERMEDIATES** (chain nodes, SA family):
- 3 per SA item (nodes A, B, C in the 3-hop/4-node chain)
- Never used as answer tokens
- Not from PRIMARY_TERMINALS or BROAD_VALUES pools
- No cross-item sharing

**DIAGNOSTIC_NODES** (DE items):
- Separate pool from SA INTERMEDIATES
- No cross-contamination with SA pools

---

## §8 G formula

Unchanged from PREREGISTRATION-EXP6.md §6 and PREREGISTRATION-EXP4.md.

```
G_content(w) = R_component_content(w) − R_composite_content(w)
G_strict(w)  = R_component_strict(w)  − R_composite_strict(w)

where:
  w = quantization rung (e.g. INT8 or INT4)
  R_component_content(w)  = mean(content_score @ w) / mean(content_score @ FP16)
                            over component checks of SA items with FP16 content=1
  R_composite_content(w)  = narrow_content @ w / narrow_content @ FP16
                            over SA items with FP16 narrow_content=1
```

Bootstrap CI: 1000 iterations, seed=0, percentile method (2.5, 97.5).

Primary seam claim requires G_content CI lower bound > 0 at INT4, calibration-invariant (Calibration A and B yield identical G_content ranking).

G_strict is reported for format-compliance analysis. A G_strict-only signal that does not appear in G_content is a format artifact, not a seam signal (rule locked in PREREGISTRATION-EXP4.md).

---

## §9 DE echo diagnostic

Unchanged from PREREGISTRATION-EXP6.md §7.

DE-QE items estimate question-entity echo rate (1-hop; echo risk = model outputs the anchor entity rather than the target).

DE-PI items estimate penultimate-intermediate echo rate (2-hop composite; echo risk = model outputs the penultimate node rather than the terminal).

Diagnostic gate: if an item's FP16 narrow content score < 1, classify as FLOOR_DIAGNOSTIC and exclude from echo-rate interpretation. Do not use FLOOR_DIAGNOSTIC items to estimate echo behavior.

Echo rates reported separately for QE and PI types at INT4. INPUT_ECHO_ERROR assigned by runner when: model output contains echo_wrong_value (case-insensitive) AND content=0 at the scored rung.

---

## §10 NC halt condition

Unchanged from PREREGISTRATION-EXP6.md §8.

NC1's narrow arm expected token is absent from NC1's context. If content_slot_score returns > 0 for NC1 narrow at any rung, halt immediately — scorer or model-hallucination audit required. Do not continue the sweep.

---

## §11 Stability screen gate

Pre-registered threshold: **≥6 STABLE SA items** (included_in_G=True) before proceeding to INT8/INT4 sweep.

Stability criteria (unchanged from Exp6):
- narrow/original = 1.0
- narrow/paraphrase = 1.0 (paraphrase: replace `_FMT` with `_FMT_PARA`)
- all component checks ≥ 0.5 (original prompt only)
- broad arm ≥ 0.5 (original prompt only)

If n_stable_SA < 6: report Outcome E (task failure). Do not run stress sweep.

DE items go through the stability screen (classification is logged) but are not counted toward the SA threshold. NC1 is expected to FLOOR; NC1 FLOOR does not count against the threshold.

---

## §12 Outcome table

Unchanged from PREREGISTRATION-EXP6.md §11. Outcomes are determined by G_content at INT4, calibration-invariance, and NC/DE behavior.

| Outcome | G_content CI | Calibration | NC | Meaning |
|---|---|---|---|---|
| A | lo > 0 | invariant | 0 | Seam signal — primary claim supported |
| B | CI includes 0 | — | 0 | Null result |
| C | hi < 0 | — | 0 | Inverse: component degrades faster than composite |
| D | G_strict signal, G_content flat | — | 0 | Format artifact; no seam signal |
| E | — | — | — | Task failure: <6 stable SA pairs at FP16 |
| F | lo > 0 | calibration-variant | 0 | Surprise content loss; not a clean seam signal |

If NC content > 0 at any rung: halt (scorer audit). Outcome not assigned.

---

## §13 Forced-intermediate follow-up

Unchanged from PREREGISTRATION-EXP6.md §12.

Trigger condition: for any SA item at a stressed rung, composite content fails (< 0.5) AND all component checks pass (≥ 0.5).

If triggered: run forced-intermediate prompt (reveal intermediate nodes explicitly; ask only for terminal). Log separately. Do not add to G computation. Used as post-hoc diagnostic only.

---

## §14 Calibration arms

Two calibration labels: `code` (Calibration A) and `prose` (Calibration B). Label does not alter any prompt. Both calibrations must produce bit-identical results (same model, same temperature=0, same prompts). G_content rankings must be identical across both calibrations for Outcome A to be declared.

Run Calibration A first. Archive JSON. Run Calibration B. Compare G_content rankings before writing RESULTS-EXP7.md.

---

## §15 Ordering constraint (locked)

```
PREREGISTRATION-EXP7.md (this document, locked before task construction)
  → tasks_exp7.py (constructed to satisfy §5, §6, §7)
  → verify runner unit tests (python3 -c "from run_tier0 import run_unit_tests; run_unit_tests()")
  → FP16 stability screen (run_stability_screen.py --tasks tasks_exp7 ...)
  → if ≥6 SA stable: tasks_exp7_stable.py written
  → Calibration A (--calib code)
  → Calibration B (--calib prose)
  → forced-intermediate follow-up if trigger condition fires
  → RESULTS-EXP7.md
```

No INT8/INT4 sweep before stability gate confirmed. No results written before both calibrations complete.
