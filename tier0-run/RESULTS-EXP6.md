# RESULTS-EXP6.md — Experiment 6: Primary Seam Test (Stability Gate)

**Status:** Outcome E — stability gate failed / threshold not met  
**Date:** 2026-06-06  
**Pre-registration:** PREREGISTRATION-EXP6.md (locked 2026-06-06)  
**Stability screen log:** stability_screen_1780771434.json  
**Model:** Qwen/Qwen2.5-1.5B-Instruct (FP16 only — stress sweep not run)  
**Tasks file:** tasks_exp6.py (15 items: SA1–SA8, DE1–DE4, NC1, AC1–AC2)

---

## 1. Run metadata

| Field | Value |
|---|---|
| Model | Qwen/Qwen2.5-1.5B-Instruct |
| Quantization rungs run | FP16 only (stability gate; stress sweep blocked) |
| Task file | tasks_exp6.py |
| Screen output | stability_screen_1780771434.json |
| Screen date | 2026-06-06 |
| Pre-registered threshold | ≥6 stable SA (included_in_G=True) pairs |

---

## 2. Pre-registered threshold

Per PREREGISTRATION-EXP6.md §9:

> Stability screen threshold: ≥6 STABLE SA pairs (included_in_G=True).  
> If fewer than 6 SA items are STABLE: report Outcome E (task failure). Do not proceed to INT8/INT4 sweep.

---

## 3. Outcome: E — threshold not met

**Stable SA items (included_in_G=True): 3 / 8**

Threshold: 6. Gate failed. Stress sweep not run.

This is a **task-construction finding**, not a model-capability finding and not a seam result.

Exp6 does not adjudicate the seam claim. The stability gate failed before stress testing. The result is a task-construction finding: the current SA design contains context-order and verb-template artifacts. Seam claim remains open, with no movement.

No inference about quantization sensitivity, seam fragility, or G_content is licensed from Exp6 data.

---

## 4. Stable SA items

| Item | Classification | Skeleton | Note |
|---|---|---|---|
| SA2 | STABLE | S1 | NEXAL distractor; all components pass |
| SA3 | STABLE | S1 | RUBYX distractor; all components pass |
| SA7 | STABLE | S1 | DRUMN distractor; all components pass |

All three stable SA items use the S1 relation skeleton (connects / leads / grants).

---

## 5. Item classifications

### Primary seam items (SA family, 8 items)

| Item | Skeleton | Classification | Narrow orig | Narrow para | Failure pattern |
|---|---|---|---|---|---|
| SA1 | S1 | FLOOR | 0.00 | 1.00 | Last-value anchor (original only); paraphrase recovers |
| SA2 | S1 | STABLE | 1.00 | 1.00 | — |
| SA3 | S1 | STABLE | 1.00 | 1.00 | — |
| SA4 | S2 | FLOOR | 0.00 | 0.00 | Last-value anchor (both phrasings) |
| SA5 | S2 | COMP_FAIL | 1.00 | 1.00 | comp[torpx_clavb]: full-fact reproduction |
| SA6 | S2 | COMP_FAIL | 1.00 | 1.00 | comp[zarot_flobn]: chain-jump to terminal |
| SA7 | S1 | STABLE | 1.00 | 1.00 | — |
| SA8 | S2 | FLOOR | 0.00 | 0.00 | Last-value anchor (both phrasings) |

### Diagnostic / control items (DE, NC, AC — excluded from G)

| Item | Classification | Note |
|---|---|---|
| DE1 | STABLE | QE echo eligible at FP16 |
| DE2 | STABLE | QE echo eligible at FP16 |
| DE3 | FLOOR | Last-value anchor; FLOOR_DIAGNOSTIC; excluded from echo-rate read |
| DE4 | FLOOR | Last-value anchor (original); paraphrase recovers; FLOOR_DIAGNOSTIC |
| NC1 | FLOOR | Expected — null control behaves correctly; scorer validated |
| AC1 | FLOOR | Last-value anchor in two-fact atomic context |
| AC2 | STABLE | Single-fact pair; no anchoring |

---

## 6. Construction artifact analysis

Two distinct construction artifacts / behavioral failure patterns are observed at FP16 before stress testing begins.

### Artifact 1: Last-value distractor anchoring

In every SA item, the distractor fact (`ENTITY holds VALUE`) was appended at the END of the context:

```
AXFOB connects to TUNNB. TUNNB leads to ALCV5. ALCV5 grants ZUNIP. GATEP holds BRIFQ.
                                                                    ^^^^^^^^^^^^^^^^^
```

A subset of items return the distractor value regardless of what the narrow question asks. The model anchors on the last value in context rather than traversing the chain.

Affected SA items: SA1 (partial — original only), SA4 (full), SA8 (full).  
Affected DE items: DE3 (full), DE4 (partial).  
Affected AC items: AC1 (two-fact context, model returns FRALP's value for NIRA question).

Specific outputs:
- SA4 narrow (both phrasings): `ANSWER: KOLVR` — KOLVR is the distractor (`TUVOX holds KOLVR.`), not the terminal RIVOK
- SA8 narrow (both phrasings): `ANSWER: GRUXV` — GRUXV is the distractor (`NEXOV holds GRUXV.`), not the terminal DREXM
- SA1 narrow (original): `ANSWER: BRIFQ` — BRIFQ is the distractor (`GATEP holds BRIFQ.`), not the terminal ZUNIP

SA1's paraphrase instruction (`"Your entire response must be exactly this and nothing else: ANSWER:"`) breaks the anchor and the model returns the correct terminal. This indicates the anchoring is sensitive to exact prompt wording, not a hard capability floor. SA4 and SA8 show anchoring under both phrasings — the anchoring is stronger when the chain terminal and distractor value are phonologically similar in position (both appear once, near each other in context).

The 3 stable SA items (SA2, SA3, SA7) avoid this pattern. Their distractor entities and values do not appear to compete with the chain terminal for last-position salience, but more likely the instability is primarily a context-ordering artifact: distractor appended last makes it the most recent token in context at inference time.

This artifact is directly attributable to context ordering. It is not evidence about model capability or quantization sensitivity.

### Artifact 2: S2 verb compound-output on component prompts

The S2 skeleton uses `opens into` as a relation verb. On component prompts of the form:

```
TORPX opens into what?
```

the model reproduces the full relation fact sentence rather than the target token:

```
Output: 'TORPX opens into CLAVB.'
Expected: 'ANSWER: CLAVB'
```

The model knows the correct hop target (CLAVB is present in the output) but does not follow the format instruction for this verb. This is a FORMAT_COMPLIANCE_LOSS on the component arm, not CONTENT_LOSS. The component check scores 0 regardless of whether the model knows the fact.

Affected: SA5/comp[torpx_clavb].

The underlying cause appears to be that `opens into` forms a fluent verb phrase that the model treats as a fill-in-the-blank sentence template (`"X opens into ___."`) rather than a standalone question requiring a formatted response. The S1 verbs (`connects`, `leads`, `grants`) are more economical and do not trigger this behavior.

### Supplemental observation: chain-jump on first-hop component (SA6)

SA6/comp[zarot_flobn] asks `"ZAROT routes to what?"` — expected `ANSWER: FLOBN`. The model returns `ANSWER: GLAXU` (the chain terminal). The model traverses the full chain from the first-hop anchor rather than stopping at the first hop.

Notably, SA6's narrow arm (full chain traversal from ZAROT) passes with score 1.00. The component check (1-hop from ZAROT) fails because the model does too much, not too little. This inversion — composite passes, component fails — is distinct from both artifacts above. It is noted here as a supplemental observation. It does not constitute a seam finding and no causal interpretation is pre-registered.

---

## 7. Claim-status consequences

The pre-registration did its job. It blocked a dirty run.

The stability screen caught two construction defects before they could produce spurious INT4 findings:
- Last-value anchoring would have inflated INT4 FLOOR rates with items that were already FLOOR at FP16.
- S2 component failures would have produced COMP_FAIL classifications that could not be distinguished from seam-related component degradation.

**Seam claim (Test 1):** Open. No movement. Six experiments in, the claim has not been adjudicated because the task set has not yet passed a clean stability gate.

**Format-degradation finding (Exp 4→5):** Resolved and stable. Not affected by Exp6 result.

---

## 8. Exp7 redesign requirements

Exp7 is a **construction repair** of Exp6. The seam-test logic is unchanged. The two identified artifacts are repaired.

**Fix 1 — Distractor fact to context front:**

```
GATEP holds BRIFQ. AXFOB connects to TUNNB. TUNNB leads to ALCV5. ALCV5 grants ZUNIP.
```

not:

```
AXFOB connects to TUNNB. TUNNB leads to ALCV5. ALCV5 grants ZUNIP. GATEP holds BRIFQ.
```

The distractor appears before the chain. The chain terminal is the last value in context. This directly inverts the context-ordering artifact.

**Fix 2 — S1 skeleton only:**

Use only `connects / leads / grants` across all 8 SA items. Do not reintroduce the S2 skeleton (`routes / opens into / maps to`) in Exp7. Verb variation is a later concern; a clean stability gate takes priority.

**Unchanged from Exp6:**
- Forced-format instruction (Exp5 scaffold: `"Respond using only this exact format with nothing before or after: ANSWER:"`)
- Neutral terminal token design (5–6 char, all-caps, no English embedding, no antonym, single token, no space)
- Explicit first-node anchor in composite question
- SA-only G_content formula and G_strict formula (locked in PREREGISTRATION-EXP4.md)
- DE/NC/AC diagnostic structure and counts (4/1/2)
- Dual scorer, 9 pre-registered unit tests
- Outcome table

**Token pools:** All pools refreshed for Exp7. No reuse of Exp6 token assignments.
