# FIRST-COMPRESSION-RUNG-SENIOR-INTERPRETATION-v0.1

**Version:** v0.1. River and Canyon program. Lane 1a′ / Semantic-Read Operationalization context.
**Status:** Senior verification + interpretation of the first compression rung. Reviews the INT8 result against bytes. Authorizes no successor execution. Records two governance gaps for reconciliation.
To: Team Lead · Cc: Manager, CS · From: Senior Engineer · Date: 2026-06-13.

## Q1. Can Senior fetch and recompute the rung artifacts from origin/main?

```text
YES. Fetched origin/main (HEAD 5f70a57c…). All rung artifacts present and recomputed:
  first-compression-rung/int8_run_result.json
  first-compression-rung/int8_clean_outputs.json
  first-compression-rung/int8_defective_outputs.json
  first-compression-rung/INT8-PER-ITEM-RESPONSE-TABLE-v0.1.md
  FIRST-COMPRESSION-RUNG-RETURN-v0.1.md
INT8 snapshot identity present in run_result metadata:
  int8 model.safetensors sha256 78cdda52… ; config/tokenizer hashes present.
fp16 baseline cross-reference present: fp16_baseline_run_result_sha256 268ed175…
  (matches the FP16 validation result I byte-verified in closeout v0.2).
```

## Q2. Does the reported INT8 result verify from bytes?

```text
YES, fully, including the two flips (which my first parser missed by reading the
wrong field — the output field is `raw_output`, not `output_text`; corrected).
Read from int8_run_result.json and the per-item output files:
  overall/intra_run_pattern: "PASS"
  INT8 defective: outcome "eliminated", label strict_content_gap_instability FIRED;
    n_strict_correct 6, n_content_correct 35
  INT8 clean: 40/40 strict, NOT_RULED_OUT
  FP16 baseline (for comparison): defective strict 5 / content 36; clean 40/40.
  Population criteria: only strict_content_gap_instability FIRED; all others
    NOT_FIRED or NOT_APPLICABLE — i.e. NO population criterion crosses its bound.
```

## Q3. Does the result support RETENTION-PASS?

```text
YES, on the bytes, with scope. The INT8 run preserves the FP16 validation
PATTERN: defective eliminated via the SAME criterion, clean spared. That is
what "retention of the validation behavior" means at this rung. RETENTION-PASS
is supportable AS SCOPED in Q7 — not as a general robustness claim.
```

## Q4. Same criterion at FP16 and INT8 — simplifies, or are the flips material?

Both, and they must be held together. The **criterion identity is the same** (strict_content_gap_instability fires at both FP16 and INT8), which is exactly the stability my validation interpretation §5 said a retention reading must look for — it tracks the *elimination*, and the elimination is criterion-stable across the rung. That simplifies the top-line reading: the instrument eliminates the defective member the same way before and after compression.

But the two flips are **material as texture, not as verdict**: they show the elimination is criterion-stable *despite* per-item output churn underneath it. The aggregate verdict is unchanged; two individual items moved. That is the correct level at which to record them — the verdict retained, the item-level behavior is not byte-frozen.

## Q5. Do the two defective flips matter?

They matter, in opposite directions, and the verified bytes show why:

```text
CP-DEF-013: raw_output "none" → "NONE"  (FP16 → INT8)
  A FORMAT IMPROVEMENT toward prompt-literal grammar. It moves the item from
  content-correct-but-strict-OTHER to strict-NONE — i.e. it ADDS a strict-correct
  (this is the 5→6 strict gain). Direction: the model's abstention got MORE
  prompt-literal under INT8 on this item.
CP-DEF-018: raw_output "none" → "h"  (FP16 → INT8)
  An ABSTENTION LOSS. The model stopped abstaining and emitted a letter ("h") —
  an ungrounded answer to an unanswerable item (this is the 36→35 content loss).
  Direction: on this item, INT8 produced a worse (confabulated) response.
NET at population level: the two flips are in OPPOSITE directions (one gains a
strict-correct, one loses a content-correct abstention), and NEITHER moves any
population criterion across its bound. The defective member remains eliminated
by the same criterion. So the flips matter for the HONEST TEXTURE of the result
(INT8 is not behaviorally identical to FP16 item-by-item) but do NOT change the
retention verdict.
```

The CP-DEF-018 abstention loss is the one worth flagging forward: it is exactly the kind of per-item degradation (abstention → confabulation) that, if it accumulated at scale or crossed the ceiling bound, would break retention. At n=40 it did not cross; it is a single item. But it is the signal to watch on any deeper rung — recorded, not alarmed.

## Q6. Does clean-output byte identity strengthen the clean-spared interpretation?

```text
YES, and it is verified: int8_clean_outputs.json is BYTE-IDENTICAL to the FP16
clean_outputs.json (both sha256 abb887ad…). The clean member produced exactly
the same outputs at INT8 as at FP16 — not just the same verdict, the same bytes.
This is a stronger form of "clean spared" than the defective side shows: the
clean member is not merely still-not-ruled-out, it is output-invariant under this
rung. Worth recording precisely because it contrasts with the defective side's
two flips — the compression perturbed defective item outputs but left clean item
outputs untouched, at this rung, at this scale.
```

## Q7. What exactly can be claimed?

```text
CLAIMABLE (scoped, byte-verified):
  "At the first compression rung (FP16 → INT8) on the validated constructed-
   positive pair, the constructed-positive validation behavior was retained: the
   defective member remained eliminated via the same criterion
   (strict_content_gap_instability), and the clean member remained not-ruled-out
   with byte-identical outputs. No population criterion crossed its bound.
   This is first-rung retention of constructed-positive validation behavior at INT8."
```

That is the suggested scope and I confirm it as the correct ceiling on the claim.

## Q8. What cannot be claimed?

```text
NOT claimable:
  - NOT INT4 (this rung is INT8 only)
  - NOT a full stress ladder (one rung)
  - NOT certification (the pair is validation-passed, not certified — Lane 3
    certification has not occurred; see the routing-reconciliation note below)
  - NOT general robustness (n=40, one constructed pair, one condition class)
  - NOT Claim C progress
  - NOT seam evidence
  - NOT compositional retention of anything beyond this constructed pair's
    single-difference behavior
This is a sensitivity-instrument-under-stress reading at one rung, on a
constructed positive, at 3B — exactly the framing Paper 2 §9 reserves for a
first compression rung: instrument-validation-under-stress, not composition
evidence.
```

## Q9. How should this fold into the route reconciliation?

This is the part that needs your and the Manager's decision, not my assertion — and it connects to the map question now open on the record.

```text
The result is SUPPORTING EVIDENCE; it should not, by itself, change the route.
Reason: the rung was executed under routing ambiguity (your freeze), AND it sits
in tension with the project map (governance/passdown/2026-06-10_project-map.md),
which places the first compression rung at LANE 4 — gated BEHIND Lane 3
certification (Paper 4) — i.e. on a CERTIFIED baseline. This rung ran on a
VALIDATION-passed pair, not a certified one. So either:
  (a) this is a Lane-1a′ reconnaissance rung (consistent with "Lane 1a may rule
      out"), distinct from the map's Lane-4 certified rung — in which case the
      map is stale and should be superseded to show the 1a′ detour and where
      this rung sits; OR
  (b) the route drifted past Lanes 1–3, in which case the rung's interpretation
      must carry that it preceded certification and cannot stand in for a
      Lane-4 result.
I cannot resolve (a) vs (b) from the record; it is a Manager/Team-Lead call about
what was decided. My recommendation: the data is kept (verified, RETENTION-PASS
as scoped), recorded as a Lane-1a′ reconnaissance rung under explicit "executed
under routing ambiguity" provenance, and the NEXT step is the route reconciliation
+ map supersession returning to Manager — NOT a successor rung. The result does
not earn an INT4 or a ladder; it earns a reconciled map.
```

## Governance gaps recorded

```text
GAP 1 — routing ambiguity (TL-recorded): the rung executed after a prior local
  authorization but during the TL route-alignment pause. Handling: data not
  discarded; quarantined as verified-but-routing-ambiguous; no successor until
  the Manager receives a reconciled route. I concur with this handling.
GAP 2 — my closeout v0.2 not visible to CS (CS-flagged): CONFIRMED and it is
  MINE to fix — CONSTRUCTED-POSITIVE-VALIDATION-CLOSEOUT-v0.2.md was filed to
  library/outputs but never pushed to the repo (the same unpushed-artifact gap
  CS hit with the result bytes, now on my side). I am filing it to the repo this
  turn so both seats see one history. The record cannot depend on each seat
  seeing a different history — agreed.
```

## Boundary

This interpretation authorizes no successor execution: no INT4, no second rung, no full ladder, no Path B, no Path D, no schedule v2, no certification, no ranking, no Claim C activation. It verifies the first rung from bytes, scopes the claim to first-rung INT8 retention of the constructed-positive validation behavior, records the two flips honestly, and refers the routing/map reconciliation to the Manager. All continuing prohibitions remain in force.

— Senior Engineer
