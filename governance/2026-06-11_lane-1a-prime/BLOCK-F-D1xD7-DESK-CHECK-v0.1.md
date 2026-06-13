# BLOCK-F-D1xD7-DESK-CHECK-v0.1

**Version:** v0.1. River and Canyon program. Semantic-Read Operationalization phase, Block F.
**Status:** model-free desk-check return; quarantined math; all numeric values [NON-PRECEDENTIAL]; authorizes nothing.
Owner: Senior Engineer · CS role: artifact/path/hash verification · Team Lead: synthesize + ledger entry.
Ledger: SEMANTIC-READ-OPERATIONALIZATION-LEDGER-v0.2.1.md · INDEX is canonical artifact catalog.

## 0. Question

Is the D1–D7 certification window logically nonempty for the D4 family at 3B FP16, under known constraints? Desk arithmetic only — no thresholds set, no certification performed, no model run, no candidate selected. Block F owns all math in this phase; this artifact is separate and is never merged into the rubric or template files.

## 1. Inputs (shown from run-of-record bytes, not memory)

Read from `experiments/2026-06-11_lane-1a-prime/d4_a_pilot/` and `d4_b_pilot/` t1/t3 reports at origin/main:

```text
D4-A candidate (t1 candidate_summary):
  n_answerable = 80 · answerable_correct = 80 · answerable_accuracy = 1.0
  n_null = 16 · null_abstention_rate = 1.0 · void_rate = 0.0
  candidate_outcome (t3) = NOT_RULED_OUT
D4-B candidate: identical candidate_summary (80/80; 16/16 null abstain);
  candidate_outcome = NOT_RULED_OUT
D4-B TP control (t1 tp_control_summary):
  tp_control_correct = 1 / 80 · tp_control_accuracy = 0.0125 · abstention 0.475
shortcut-policy envelope (both cells, t1):
  union_envelope_score = 0.6125 · envelope_cap = 0.8 · room_below_envelope = 0.1875
  per-policy answerable accuracies: pure_last_position 0.30 · salient_endpoint 0.1625 ·
    recency_excluding_target 0.15 · prefix_neighbor_confusion 0.15 · copy_completion 0.0
  all four non-trivial policies classified "discriminative"
```

These are the bytes of record. CS to confirm path/commit/sha256 on filing.

## 2. The window, in constraint-structure form (inequalities only; no thresholds set)

A certifiable measurement substrate must place candidate accuracy `a` in a window bounded below by the shortcut/floor structure and above by the saturation guard:

```text
floor(D1, D2)  <  a  <  saturation_ceiling(D7)

where, as inequalities (NOT threshold values):
  D2 (shortcut resistance): a must exceed the shortcut envelope by a
     resolvable margin →  a  >  union_envelope_score + m_resolve
  D7 (saturation guard):    a must sit below the ceiling by enough room to
     resolve a retention drop of interest δ →  a  <  ceiling − δ
  D1 (emission-bias control): TP-control accuracy must sit at/near its
     analytical prior (low), establishing the control channel measures
     native bias, not capability → satisfied in structure (see §3)
  feasibility condition (window nonempty):
     union_envelope_score + m_resolve  <  ceiling − δ
```

The dependency ordering: D1 (control channel valid) and D2 (shortcut envelope known) must hold *before* D7's ceiling is meaningful; D7's room-below requirement is what a retention measurement later consumes.

## 3. Reading the D4 family against the structure

```text
D2 side — shortcut envelope is known and bounded:
  union_envelope_score = 0.6125 [NON-PRECEDENTIAL], cap 0.8, room_below 0.1875.
  The four shortcut policies are discriminative but none approaches candidate
  accuracy. So the LOWER bound of the window is established and is well below 1.0.

D1 side — control channel reads as designed:
  D4-B TP control = 0.0125 [NON-PRECEDENTIAL], near its analytical prior;
  this is control-channel evidence only (per ledger E14), and it satisfies the
  D1 STRUCTURE (the bias channel measures bias), not any sensitivity claim.

D7 side — THIS IS WHERE THE WINDOW CLOSES:
  candidate answerable_accuracy = 1.0 (80/80) [NON-PRECEDENTIAL].
  The saturation guard requires  a < ceiling − δ  for some retention drop δ > 0
  that the instrument must later resolve. At a = 1.0 there is ZERO room above:
  ceiling − δ < 1.0 for any δ > 0, so the upper-bound inequality
  a < ceiling − δ  is VIOLATED for every positive δ.
```

A candidate at the saturation ceiling cannot host a *downward* retention measurement, because there is no measurable room for accuracy to fall into that the instrument could resolve as a drop rather than as noise. This is exactly the condition D7 exists to refuse.

## 4. Disposition

```text
DISPOSITION: EMPTY (for the D4 family as it currently scores), under the
illustrative constraints stated. [NON-PRECEDENTIAL]
```

The window is empty not because the constraints are mis-set but because the only surface in hand scores at ceiling (80/80). The D2 floor is healthy and the D1 control channel reads correctly; the D7 saturation guard is the binding constraint, and it binds hard at a = 1.0.

Restated without the analogy, in the family's own terms: *the D4 surface is solved to the measurement's resolution, so it has no headroom for a compression-induced drop to be observed; certifying it as a retention substrate would certify a ruler with no scale below its current reading.*

## 5. What this does and does not establish

```text
Establishes (desk-level, non-precedential):
  - the certification corridor is EMPTY for the D4 family at its current 80/80
    score; the binding constraint is D7 saturation, not D2 shortcut leakage.
  - therefore a constructed-positive / window-placed variant that pulls
    candidate accuracy OFF ceiling into (floor, ceiling−δ) is the structural
    prerequisite for any future certification attempt on this family.

Does NOT establish:
  - any threshold value (none set; δ, ceiling, m_resolve left as symbols)
  - that an off-ceiling variant WILL certify (that is a future attempt, gated)
  - any model-behavior claim, sensitivity claim, or Claim C progress
  - any authorization to construct, generate, or run anything
```

## 6. Feeds (execution sequencing, not authorization)

Per the proposal, Block F output feeds Block E's design space. This EMPTY disposition is the premise Block E must design against: any constructed-positive proposal must specify how it moves accuracy off the saturation ceiling into the resolvable window, and must carry that target as a load-bearing, semantic-read design parameter. Block E remains sequenced after Block D and this Block F, and remains drafting-only.

## 7. Non-authorization footer

NON-AUTHORIZATION FOOTER — BLOCK F
This desk-check does not authorize threshold setting, threshold anchoring, candidate certification, candidate selection, model execution, stress testing, INT8 / INT4, or Claim C activation. All illustrative values are [NON-PRECEDENTIAL]. The artifact is separate and is never merged into rubric or template files.

## 8. Required-return checklist

```text
1. D1×D7 desk-check result: §2–§3
2. Disposition: EMPTY (D4 family at 80/80; binding constraint D7 saturation) §4
3. Assumptions stated: §2 (inequality form; δ, ceiling, m_resolve symbolic) §1 (input bytes)
4. Non-precedential status: stated throughout; §7 footer
5. Full non-authorization / prohibition block carried: §7 + program closed-gate list below
6. Language-perimeter clean: YES — no Path A citation in this artifact (none needed);
   no breadth language; no forbidden phrasings; D4 outcomes referred to as
   NOT_RULED_OUT per binding language; TP result as control-channel only
7. Path / commit / sha256 / INDEX reference: on filing (CS verifies)
```

Closed gates carried (full named list): no model-facing execution · no model loading · no sweep_id creation · no token-prior generations · no constructed-positive generation · no seeded-defect exercise · no surplus-signature validation · no schedule v2 drafting · no schedule supersession · no true breadth rerun · no Path B readiness or execution · no Path D execution · no quantization stress · no INT8/INT4 · no candidate selection · no ranking · no threshold work · no certification evaluation · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission.

— Senior Engineer
