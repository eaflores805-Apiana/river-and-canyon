# Cell03 Axis Decision Memo — Two-Hop Level 1

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Requested by:** Team Lead memo — "Cell02 Filed — Interpretation and Recommended Next Axis" 2026-06-08
**Revised:** 2026-06-08 — per Team Lead memo "Cell02 Cue Relabel Accepted — Cell03 Requirements Before Construction Authorization"
**Status:** AXIS DECISION RECORDED — Cell03 construction NOT authorized by this memo

---

## Purpose

This memo records the axis decision for a prospective Cell03 under the Two-Hop Level 1 construction, revised to reflect the Cell02 cue relabel and the full pre-authorization requirements identified by the Gate 5 positional-dummy audit.

It documents:

```text
1. Cell02 relabel and cue accounting
2. Cell03 framing: attraction-cue mapping
3. Four confounded Cell02 cues
4. Axis options comparison
5. Dummy policy requirements before construction authorization
6. One-axis clarification and design principle
7. Design requirements
8. Pre-authorization requirements
9. Authorization boundary
```

This memo does not authorize Cell03 construction, model inference, or any run.

---

## 1. Cell02 relabel

The previous label `adjacency-driven endpoint attraction` is retired.

```text
Retired label:  adjacency-driven endpoint attraction
Correct label:  ct-anchoring; cue unresolved among
                adjacency / proximity,
                absolute position (ct fixed at pos 6, all 24 items),
                C-rank slot (ct fixed as second_C, all 24 items),
                answer-domain salience.
```

The behavioral observation is clean and stands:

```text
11/15 hop1 failures returned ct instead of bt.
```

But Cell02 confounded four potential cues simultaneously. All four were true of ct in every item:

```text
Cue 1 — Adjacency / proximity:
  Target chain hop1 at pos 5, hop2 at pos 6 — adjacent facts.
  ct is the object of the pos-6 fact.

Cue 2 — Absolute position:
  ct is at context position 6 for all 24 items.
  A model exploiting a fixed-position rule would return ct for every hop2 or composite query.

Cue 3 — C-rank slot:
  c_by_pos = [cd1(2), ct(6), cd2(7)] for all 24 items.
  ct is always second_C. A model returning the second C-endpoint by context rank
  would score 24/24 on composite.
  Gate 5 audit confirmed: always_return_second_C was not tested and would score 24/24.

Cue 4 — Answer-domain salience:
  ct is the correct composite answer for all 24 items.
  ct appears as the object of the only "maps to" fact with a subject that also anchors
  the composite and hop2 queries. It may be more semantically "answer-shaped" than
  cd1 or cd2 independent of its position or rank.
```

Cell02 does not — and cannot — distinguish which of these cues is load-bearing. The label "adjacency-driven" overclaims.

**Safe interpretation (required):**

```text
Cell02 strengthens the candidate convergence read that the Two-Hop Level 1 floor
may involve recurring salient endpoint-return behavior, but it does not establish
which cue drives that behavior.
```

Do not use: `confirmed`, `root cause`, `mechanism`, `adjacency-driven`.

---

## 2. Cell03 framing: attraction-cue mapping

Cell03 is not a generic third axis test.

Cell03 is an **attraction-cue mapping step**: it asks which cues, when disentangled, predict whether the model returns ct on hop1 queries.

```text
The Cell03 question:
  If adjacency / proximity between the target hop1 and hop2 facts is reduced —
  while ct's absolute position and C-rank are balanced across items rather than fixed —
  does ct-over-retrieval on hop1 decrease?

Interpretation under each outcome:
  ct-over-retrieval decreases:
    Adjacency / proximity is supported as a contributing cue.
    Position and C-rank were balanced, so they do not explain the decrease.

  ct-over-retrieval persists:
    Adjacency / proximity alone is not the load-bearing cue.
    Candidates shift to absolute position, C-rank, answer-domain salience,
    or a combination. Further axis separation required.
```

Cell03 is not a direct replication of Cell02 with one variable changed.

Cell03 re-baselines the adjacency question under corrected control coverage.

```text
Cell02 had cue confounds and an uncovered positional shortcut (second_C / ct).
Cell03 must correct both before the adjacency result is interpretable.
```

The Cell02-to-Cell03 comparison is honest only if stated as:

```text
Cell03 does not preserve Cell02's fixed-rank / fixed-position structure.
Cell03 re-baselines the adjacency question under corrected controls.
A drop in ct-over-retrieval in Cell03 vs. Cell02 does not by itself prove
adjacency was the cause in Cell02, because the controls changed.
```

---

## 3. Axis options

Three candidate axes remain. The preference ordering is unchanged; the framing is updated.

### Option A — Adjacency / proximity separation (RECOMMENDED)

```text
Tested axis: adjacency / proximity between target hop1 and hop2 facts

Proposed Cell02-to-Cell03 context arrangement change:
  Cell02:
    pos 4: neighbor fact (fl holds cn)
    pos 5: target chain hop1 (at→bt)      ← hop1 fact
    pos 6: target chain hop2 (bt→ct)      ← hop2 fact; ct here; adjacent to hop1

  Cell03:
    pos 4: target chain hop1 (at→bt)      ← hop1 fact moved one earlier
    pos 5: neighbor fact (fl holds cn)    ← inserted between target chain facts
    pos 6: target chain hop2 (bt→ct)      ← hop2 fact; ct stays at pos 6

NOTE: the simple neighbor-interposition above breaks adjacency but keeps ct at pos 6
and keeps ct as second_C — both Cell02 confounds persist.

REQUIRED DESIGN CORRECTION (per Team Lead memo 2026-06-08):
  Cell03 must BALANCE ct absolute position and C-rank across items, not hold them fixed.
  This means:
    (a) ct should not sit at the same absolute position in every item.
    (b) ct's C-rank (first / second / third by context position) should vary across items.
  This may require a mixed design (e.g., half items with ct as second_C, half as first_C
  or third_C) or a within-item arrangement where ct position varies by item.

  Balancing position and C-rank is treated as a mandatory control repair, not as
  the experimental axis. The experimental axis remains adjacency / proximity.
  The one-axis constraint is not violated: the axis under test is adjacency/proximity;
  the position/C-rank balance is a control requirement necessary to make Cell03
  interpretable against Cell02.

What this tests:
  With adjacency separated and position/C-rank balanced, does ct-over-retrieval on hop1
  drop relative to Cell02 (11/15)? If yes, adjacency/proximity is supported as a cue.
  If no, the cue is elsewhere.

One-axis constraint note:
  A design that balances position/C-rank will necessarily differ from Cell02 in more
  than one structural feature. This is acknowledged. The intent is:
    - Primary manipulation (tested axis): adjacency / proximity separation
    - Secondary adjustment (control repair): position/C-rank balance
  Both are required for a valid test. Manager authorization should explicitly cover
  the control-repair design change as part of the Cell03 construction scope.
```

### Option B — NULL / abstention calibration

```text
Reason not recommended first:
  Axis A (abstention) is 0/24 correct-NULL in both cells — already a clean floor.
  The cue-unresolved hop1 ct-anchoring signal is the stronger diagnostic to address.
  Modifying the prompt template is a larger instrument change.
  Defer unless Manager explicitly scopes a NULL-calibration test.
```

### Option C — Reduced wrong-chain pressure

```text
Reason not recommended first:
  Axis B (chain-selection) rate is stable at 4/24 across two cells.
  The ct-anchoring signal is more informative and more recently unresolved.
  Changing distractor geometry would modify context structure in ways that
  interact with the cue-confound analysis.
  Defer unless Manager explicitly authorizes.
```

---

## 4. Dummy policy requirements before construction authorization

**This is a pre-authorization requirement. Construction cannot proceed without it.**

### 4.1 Full-rank C coverage

The Cell02 Gate 5 audit identified a coverage gap: `always_return_second_C` (= `always_return_ct` in Cell02) was not tested and would score 24/24 on composite.

For Cell03 and all future ranked-C constructions, Gate 5 must include full-rank C coverage:

```text
always_return_first_C      (already in scorer)
always_return_second_C     (NEW — mandatory for Cell03)
always_return_third_C      (include if construction has 3+ C-endpoints)
always_return_last_C       (already in scorer)
always_return_ct           (NEW — mandatory for Cell03)
```

Cell03 has 3 C-endpoints (cd1, ct, cd2), so the full set is:
`first_C`, `second_C`, `third_C / last_C`, and `always_return_ct`.

### 4.2 always_return_ct

```text
Definition:
  For each item and query type, always_return_ct returns the target chain's C_object
  (ct) regardless of query type or expected answer.

  score(item, query_type) = 1.0 if ct == expected_answer(item, query_type) else 0.0

Expected scores under correct construction:
  hop1:           0/n  (expected answer is bt, not ct)
  hop2:           n/n  (expected answer is ct — trivially correct)
  composite:      n/n  (expected answer is ct — trivially correct)
  negative_graph: 0/n  (expected answer is NULL)

Gate 5 relevance:
  For composite, always_return_ct = n/n. If included, this dummy would fail Gate 5
  (n/n > ceiling) for composite under standard constructions.
  This is expected and intentional: it quantifies the "always return the right token"
  upper bound. The composite ct-predictability is not a shortcut in isolation; it
  reveals whether the model's composite correct rate exceeds what chance or positional
  rules explain.
  Gate 5 ceiling policy for always_return_ct must be explicitly scoped before use.
  Proposed: always_return_ct is recorded for reference only and excluded from the
  max_det ceiling calculation. Its function is to anchor the diagnostic, not to fail Gate 5.
```

### 4.3 always_return_answer_shaped (proposed operational definition)

```text
Purpose:
  Test whether the model is exploiting answer-domain salience — returning tokens that
  are structurally or syntactically "answer-like" in the context, independent of
  fixed token identity or fixed rank position.

Operational definition (proposed):
  always_return_answer_shaped(item, query_type) returns the in-context token that
  appears as the object of the MOST RECENTLY SEEN relation fact whose relation type
  matches the query's expected relation type, where:
    - hop1 expected relation:     "links to" (returns the bt-type object of the last
                                   "links to" fact seen before the query anchor)
    - hop2 / composite expected:  "maps to" (returns the ct-type object of the last
                                   "maps to" fact with the query anchor as subject)
    - negative_graph:              NULL (no valid relation chain; answer-shaped = NULL)

Under current two-hop construction:
  hop1:           returns bt (same as always_return_B_target — not independently informative)
  hop2:           returns ct (same as always_return_ct for the target chain)
  composite:      returns ct (same as always_return_ct)
  negative_graph: returns NULL (same as always_return_NULL)

  always_return_answer_shaped ≡ existing dummies under current construction.

Why include it anyway:
  The dummy becomes informative in future constructions where:
  (a) Multiple "maps to" facts compete for the same anchor
  (b) The relation type varies across items
  (c) The answer-shaped token differs structurally from the pure ct/bt by-construction label
  For Cell03, include it explicitly to close the answer-domain salience hypothesis formally,
  even if numerically equivalent to always_return_ct on composite.

  Required pre-condition: scorer must implement this dummy explicitly.
  It may not remain informal. A proposed implementation must be reviewed before
  the scorer is amended (new scorer hash required).

Status: PROPOSED — definition must be reviewed and confirmed before scorer amendment.
        Scorer amendment requires Manager authorization and new hash lock.
```

---

## 5. One-axis clarification and design principle

```text
The Cell03 experimental axis is: adjacency / proximity between target chain hop1 and hop2 facts.

The required control repair (balancing ct absolute position and C-rank across items)
is NOT the tested axis. It is a structural correction that makes the adjacency test
interpretable.

The one-axis rule still applies to the experimental manipulation:
  Only adjacency / proximity changes as the tested variable.
  All locked instrument constants (scorer, validator, prompt template, decoding,
  thresholds, relations, chain count) are unchanged.

The control repair (position / C-rank balance) changes the specific values of item
metadata but not the construction protocol or the instrument.

Authorization scope: Manager authorization for Cell03 must explicitly cover both:
  (a) The adjacency/proximity manipulation (tested axis)
  (b) The position/C-rank balance requirement (control repair)
  and must authorize the scorer amendment required by the new dummy set.
```

---

## 6. Design requirements for Cell03

The following are design preconditions, not a construction authorization.

```text
DR1 — Tested axis:
  Adjacency / proximity between target chain hop1 and hop2 facts is the tested axis.
  Some non-target inert fact must be interposed between the two target chain facts.

DR2 — Control repair — position balance:
  ct must not be fixed at the same absolute context position for all n items.
  Design must specify how ct position varies across items and confirm the variation
  is not a systematic pattern that introduces a new confound.

DR3 — Control repair — C-rank balance:
  ct's ordinal rank among C-endpoints (first_C, second_C, etc.) must not be uniform
  across all n items. At minimum, ct should appear as first_C in some items and
  second_C or last_C in others. The specific balance strategy must be documented.

DR4 — Dummy policy:
  Gate 5 must include: always_return_first_C, always_return_second_C,
  always_return_ct, always_return_last_C, and always_return_answer_shaped (once
  the scorer amendment is authorized and hashed).
  always_return_ct is excluded from max_det ceiling calculation (reference only).

DR5 — Scorer amendment:
  A scorer amendment is required to add full-rank C dummies.
  Requires Manager authorization and new scorer hash.
  No cell construction or run may use an unamended scorer for Cell03.

DR6 — Token audit:
  Full Gate 0.5 BPE-Jaccard audit required under run tokenizer sha256:c0382117...
  New token pools under same protocol.

DR7 — Manifest validation:
  24/24 validate_manifest must pass before any run.

DR8 — Runner dry-run:
  Cell03 runner must pass --dry-run before any live inference.

DR9 — Stage 0 lock:
  A Cell03 Stage 0 lock packet is required before inference.

DR10 — Claim B scope:
  Cell03 is a Claim B attraction-cue mapping step only. No stress, INT8/INT4,
  Track B, or Claim C testing is authorized.
```

---

## 7. Pre-authorization requirements

Before Cell03 can be constructed or run, the following must occur in order:

```text
0. Dummy policy confirmation
   CS proposes always_return_answer_shaped operational definition (filed above, §4.3).
   Team Lead and Senior confirm or revise.
   This step must precede scorer amendment.

1. Scorer amendment authorized by Manager
   New dummies added: always_return_second_C, always_return_ct, always_return_answer_shaped.
   New scorer hash locked.

2. Manager authorization for Cell03 construction
   Must explicitly cover: adjacency manipulation (tested axis) + position/C-rank
   balance (control repair) + scorer amendment scope.

3. Cell03 design specification reviewed and accepted by Team Lead
   Must specify: context arrangement per position-balance strategy, how C-rank varies,
   how adjacency is broken, how position/C-rank balance is achieved, n_items, RNG seed.

4. Token construction and Gate 0.5 audit (offline)
   New pools under sha256:c0382117...; all near-miss pairs j ≥ 0.40.

5. Cell03 Stage 0 lock
   All instrument hashes confirmed. Smoke test passing.

6. Threshold review
   Current thresholds apply unless Manager authorizes revision.

7. Stage 1 preparation lock for Cell03
   Amended runner with Cell03-specific constants; dry-run PASS.

8. Manager authorization for Cell03 Stage 1 execution
   Separate from construction authorization.
```

---

## 8. Authorization boundary

```text
This memo authorizes:
  axis decision recording
  cue-confound documentation
  dummy policy proposal
  design requirements documentation
  pre-authorization requirements documentation

This memo does NOT authorize:
  Cell03 construction
  item generation
  token pool creation
  scorer amendment
  model inference
  Cell02 rerun
  confirmation pass
  7B, INT8, INT4, Track B
  Cell03 Stage 0 or Stage 1 work
  any change to locked Cell02 artifacts
  any change to locked Stage 0 instrument artifacts
```

---

## 9. Disposition record

```text
Cell02 disposition (final — Team Lead 2026-06-08):
  VALID FP16 constructibility-boundary point for Claim B.
  Cue label: ct-anchoring / cue unresolved (four confounded cues; "adjacency-driven" retired).
  Gate 5: PASS* with positional-coverage gap (always_return_second_C not tested;
    would score 24/24 composite; Cell03 dummy policy must close this gap).
  i08/hop2: FORMAT_COMPLIANCE_LOSS (isolated, orthogonal format-only event).

Cell03 status:
  NOT AUTHORIZED — pending dummy policy confirmation, scorer amendment,
  and Manager authorization covering tested axis + control repair + scorer change.

Claim B map state:
  Two dirty cells. Failures are structured and classifiable.
  ct-anchoring pattern replicated at 11/15 (Cell02) with cue unresolved.
  No stress-eligible cell. Track B BLOCKED.
  Cell03 purpose: attraction-cue mapping under corrected control coverage.
```

---

**Axis decision recorded. Cell03 requires scorer amendment, dummy policy confirmation, and Manager authorization before construction.**

— CS Engineer, 2026-06-08
