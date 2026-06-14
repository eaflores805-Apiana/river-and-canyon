# C1-C2-D4-EXISTENCE-IN-PRINCIPLE-DESK-READ-v0.1

**Version:** v0.1. River and Canyon program. Semantic-Read Operationalization phase (Block E precondition work).
**Status:** model-free desk read of existing D4 artifacts only. Inspects bytes; specifies, generates, runs nothing. Authorizes nothing.
Owner: CS Engineer (artifact inspection support) · Drafter: Senior Engineer · Team Lead: routing, synthesis, ledger.
Ledger: SEMANTIC-READ-OPERATIONALIZATION-LEDGER-v0.2.1.md · INDEX is canonical artifact catalog.

## 0. Question

Does the D4 condition-class construction PERMIT a non-saturated clean variant (C1) and a one-dimension-matched pair (C2) to be SPECIFIED in principle — yes/no — by inspecting existing artifacts only? This is the paper-checkable existence-in-principle sub-question routed by the Team Lead; the realized sub-questions remain gated and out of scope.

## 1. Artifacts inspected (existing bytes only)

```text
experiments/2026-06-11_lane-1a-prime/d4_a_pilot/t1_report.json
  — per_policy_scores, union_envelope_score, candidate_summary
experiments/2026-06-11_lane-1a-prime/d4_a_pilot/candidate_outputs/*.json
  — 96 item files (80 answerable, 16 null); item structure read directly
```

No model was run; no item was generated; the read is of committed bytes.

## 2. Shown evidence — the D4 item structure

Read directly from a candidate item (`L01-000-answerable.json`), the D4 task is a **single-hop key→value lookup**:

```text
prompt structure (verbatim shape):
  Pairs:
    194 -> q
    107 -> p
    10  -> m
    66  -> z
    98  -> j
  Query: 98          (gold = the value paired with the queried key, here "j")
```

Measured across the 80 answerable items (shown):

```text
- pairs per item:        exactly 5 (range 5–5; uniform)
- queried-key position:  distributed across slots {1, 3, 5}
                         (position counts: slot1=12, slot3=44, slot5=12)
- candidate accuracy:    80/80 = 1.0  (saturated)
- shortcut envelope:     union 0.6125, cap 0.8 — every shortcut policy
                         (pure_last_position 0.30, salient_endpoint 0.1625,
                         recency 0.15, prefix_neighbor 0.15, copy 0.0)
                         scores far below the candidate; floor is healthy
                         and well-separated
```

The construction therefore exposes its difficulty dimensions explicitly: **list length** (number of pairs), **queried-key position** (where in the list the target sits), and **key/value vocabulary**. The saturation at 80/80 is a property of *how easy these settings currently are* (5 pairs, short lists, a model that solves them all), not of anything that hides the tunable dimensions.

## 3. C1 read — is a non-saturated clean variant definable in principle?

**Yes, in principle.** The construction parameterizes difficulty along dimensions that are visible in the bytes and are not fixed by the task's definition:

```text
- list length is currently 5 and uniform; the construction admits longer
  lists, which is the canonical lever for moving a lookup task off ceiling.
- queried-key position is already varied (slots 1/3/5); position is an
  exposed, controllable dimension.
- the shortcut envelope is well below ceiling, so there is room between the
  shortcut floor and the saturation ceiling for a clean variant to occupy
  WITHOUT colliding with shortcut behavior.
```

So the *specification* of a harder, non-saturated clean variant is definable from the existing construction's own parameters. Whether a specific variant *realizes* off-ceiling against a real model is the gated sub-question (§6).

## 4. C2 read — is a one-dimension-matched pair definable in principle?

**Yes, in principle.** A matched pair requires two members differing in exactly one controlled dimension and matched on all others. The construction exposes the dimensions needed to define both the match and the single difference:

```text
matchable dimensions visible in the bytes:
  - list length (currently uniform at 5 → trivially matchable)
  - queried-key position (an explicit, controllable slot)
  - key/value token vocabulary and surface form (uniform "N -> token" format)
  - null fraction (16/96, a controllable stratum already present)
one-dimension difference candidates (the "seeded defect" axis):
  - the construction's uniform format means a single controlled perturbation
    (e.g. a position change, or a single altered pair) is specifiable while
    holding every other listed dimension constant.
```

Because the format is uniform and its dimensions are enumerable from the bytes, a pair that differs in one dimension and matches on the rest is *specifiable* in principle. Realization against a model remains gated.

## 5. Disposition

```text
YES — the D4 condition-class construction permits a non-saturated clean
variant (C1) and a one-dimension-matched pair (C2) to be specified in
principle, on the evidence of existing artifacts.
```

The family is **not** structurally saturated in a way that forecloses specification: saturation is a property of the current easy settings, while the difficulty and matching dimensions are exposed and controllable in the construction itself. This is therefore not a "do not drive this family" finding — it is the opposite: the family's own structure contains the levers a window-placed construction would use.

## 6. What remains gated before realization (YES path, required content #6)

```text
- generating any variant or pair               (no constructed-positive generation)
- seeding any defect                            (no seeded-defect exercise)
- running any variant against a model           (no model execution / loading)
- confirming a variant actually lands off-ceiling (empirical; requires a run)
- confirming a pair actually yields a discriminating verdict (empirical; requires a run)
- any threshold, certification, selection, ranking
Each future variant/pair specification is itself an instrument-component and
must pass a shown semantic-read (SHOWN-SEMANTIC-READ-TEMPLATE-v1.0) BEFORE use.
```

The existence-in-principle answer (YES) advances C1 and C2 to the edge of the gate. It does not cross it. The natural next ask is a constructed-positive **proposal** (separate Manager authorization), which would carry the realized sub-questions as its gated content.

## 7. No-authorization footer

NON-AUTHORIZATION FOOTER

This desk read authorizes no constructed-positive generation, no seeded-defect exercise, no candidate generation, no model execution, no model loading, no sweep_id creation, no token-prior generations, no threshold setting, no candidate certification, no candidate selection, no ranking, no schedule v2 drafting, no schedule supersession, no Path B readiness or execution, no Path D execution, no quantization stress, no INT8/INT4, and no Claim C activation.

It answers only whether C1/C2 existence-in-principle can be established from existing artifacts.

## 8. Required-return checklist

```text
1. Artifact list inspected: §1
2. Shown evidence from existing bytes: §2 (item structure, position spread,
   envelope separation — all read, not asserted)
3. C1 read (non-saturated clean variant definable in principle): YES §3
4. C2 read (one-dimension-matched pair definable in principle): YES §4
5. Disposition: YES §5
6. If YES, what remains gated: §6
7. If NO (n/a — disposition is YES)
8. If INDETERMINATE (n/a — disposition is YES)
9. No-authorization footer: §7
10. Language-perimeter clean: YES — D4 referred to as a condition-class /
    single-hop lookup in its own terms; no Path A breadth claim; no forbidden
    phrasings; "Claim C" appears only in the closed-gate negation
11. path / commit / sha256 / INDEX row: on filing (CS verifies)
```

Closed gates carried (full named list): no model-facing execution · no model loading · no sweep_id creation · no token-prior generations · no constructed-positive generation · no seeded-defect exercise · no surplus-signature validation · no schedule v2 drafting · no schedule supersession · no true breadth rerun · no Path B readiness or execution · no Path D execution · no quantization stress · no INT8/INT4 · no candidate selection · no ranking · no threshold work · no certification evaluation · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission.

— Senior Engineer
