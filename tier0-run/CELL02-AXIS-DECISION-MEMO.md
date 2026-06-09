# Cell02 Axis Decision Memo — Two-Hop Level 1

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Requested by:** Team Lead memo — "Cell01 Claim B Map Entry Complete — Next Step Is Axis Decision, Not Rerun" 2026-06-08
**Status:** AXIS DECISION RECORDED — Cell02 construction NOT authorized by this memo

---

## Purpose

This memo records the axis decision for a prospective Cell02 under the Two-Hop Level 1 construction.

It documents:

```text
1. The Cell01 evidence supporting the provisional next axis
2. The competing axis options and the basis for preference ordering
3. The one-axis constraint
4. Design requirements a Cell02 position/ordering test must satisfy
5. Pre-authorization requirements before Cell02 can be constructed
6. Authorization boundary
```

This memo does not authorize Cell02 construction, model inference, or any run.

---

## 1. Cell01 evidence basis

### Axis C signal — Position / ordering (primary)

```text
hop1 by ordering group (source: CLAIM-B-MAP-ENTRY-TWOHOP-L1-CELL01.md §3 Axis C, §5):
  C_target-first  (items 1-8):   0/8  hop1 correct  (6 NULL + 2 target_chain_wrong_neighbor)
  C_target-middle (items 9-16):  6/8  hop1 correct  (1 NULL + 1 target_chain_wrong_neighbor)
  C_target-last   (items 17-24): 8/8  hop1 correct  (0 failures)

hop1 NULL failures by group (7 total):
  C_target-first:  6/7  (items i01, i02, i03, i04, i05, i07)
  C_target-middle: 1/7  (item i16)
  C_target-last:   0/7
```

C_target-first places the target hop2 fact (B→C) at context position 2 (the second fact in a
7-fact context). C_target-last places the same fact at position 6. The complete inversion of
hop1 pass rate (0/8 vs 8/8) between the two extreme ordering groups is the strongest structured
signal in Cell01.

hop2 was 24/24 correct across all three ordering groups — no ordering effect on hop2. The
position sensitivity is specific to hop1 retrieval.

### Axis B signal — Content / distractor / chain-selection (secondary)

```text
composite wrong_chain_selection: 4/24
  C_target-first:  3/4 (i01, i03, i07) — all overlap with hop1 NULL failures
  C_target-middle: 1/4 (i13)           — independent; hop1 correct

Behavioral divergence (item-level, from JSON):
  On overlapping items i01, i03, i07: hop1=NULL, composite=wrong_chain(distractor endpoint).
  If composite failure were strictly downstream of hop1 NULL, composite would return NULL.
  Instead composite selects a decoy chain endpoint — a different behavioral response.
```

Axis B fragility exists independently of Axis C (confirmed by i13), but the Cell01 composite
wrong_chain signal is entangled with the C_target-first cluster for 3/4 cases. Axis B cannot be
cleanly isolated from Axis C in Cell01.

### Axis A signal — Contract / abstention behavior (tertiary)

```text
negative_graph: 2/24 correct NULL
  Both correct NULL items (i04, i08) are in C_target-first group.
  Gate 1 passed 96/96 — format adherence clean.
  NULL-contract stability is poor and may also interact with ordering.
```

Axis A signal is real but may be confounded with Axis C: the two items that correctly withheld
(i04, i08) are both in C_target-first. Whether ordering affects abstention stability is not
separable from Cell01 alone.

### Summary of signal strength

```text
Axis C (position/ordering):     STRONGEST — near-complete failure cluster 8/8 in C_target-first,
                                 clean inversion 0/8 vs 8/8, not confounded with token identity
                                 beyond Cell01's own design

Axis B (chain-selection):       SECONDARY — 1/4 independent case (i13) confirms the signal exists
                                 outside positional confound; but 3/4 wrong_chain cases cluster
                                 with Axis C in C_target-first; cannot separate without Cell02

Axis A (abstention):            TERTIARY — 2/24 correct NULL may correlate with ordering;
                                 cannot separate from Axis C within Cell01
```

---

## 2. Axis options for Cell02

Three options are possible. Only one axis may change from Cell01.

### Option 1 — Position / ordering inversion (RECOMMENDED)

```text
Change: context ordering only
  Convert C_target-first items (T-hop2 at position 2) to a different position group
  while holding token identities, distractor geometry, and chain structure constant.

Design intent:
  If C_target-first ordering is the causal factor, items that failed hop1 in Cell01
  should show improved hop1 under a different ordering condition.
  If failures persist regardless of ordering, the causal factor is not ordering —
  it is something else about those specific items (token identity, distractor geometry).

Test form:
  Option 1a — All C_target-last: replace the 8+8+8 mixed design with a single
    ordering group placing the target hop2 fact at the last or near-last context position
    for all 24 items. Clean comparison: does hop1 reach the constructibility floor
    when C_target-first is eliminated?

  Option 1b — C_target-first inverted to C_target-last for the failing group:
    Regenerate the Cell01 token constructions for items 1-8 with C_target-last ordering
    instead of C_target-first, while using the same relation structure, distractor geometry,
    and equivalent token construction protocol. Matched comparison across groups.

Axis constraint satisfied:
  Token construction protocol: UNCHANGED
  Distractor geometry (3-chain, 7-fact): UNCHANGED
  Relation structure (hop1='links to', hop2='maps to'): UNCHANGED
  Prompt template: UNCHANGED
  Scorer / validator: UNCHANGED
  Only context ordering changes.
```

### Option 2 — Content / distractor pressure isolation

```text
Change: distractor chain geometry only (e.g., reduce from 2 decoy chains to 1)
  Hold ordering at 8+8+8 (same as Cell01).

What it would test:
  Whether composite wrong_chain_selection rate drops when decoy chain pressure decreases.
  Would address the i13-type independent chain-selection fragility.

Reason not recommended first:
  Axis B signal in Cell01 is entangled with Axis C for 3/4 cases. Testing Axis B without
  first isolating Axis C leaves the primary positional confound unresolved.
  If Cell02 tested Axis B and failed, it would not clarify whether the ordering effect
  is the load-bearing explanatory variable.
  Ordering is cleaner because the null expectation under the test is well-defined:
  if ordering is the causal factor, inverting it should restore hop1.
  
Recommendation: defer to Option 1 unless Manager explicitly authorizes Axis B first.
```

### Option 3 — NULL-contract calibration isolation

```text
Change: add an explicit NULL-contract instruction to the prompt
  Hold ordering and distractor geometry at Cell01 baseline.

What it would test:
  Whether negative_graph null_return rate improves with a stronger abstention instruction.
  Related to the NULL-calibration carry-forward note in the map entry.

Reason not recommended first:
  Axis A (abstention) is the weakest primary signal in Cell01 for Claim B mapping.
  2/24 correct NULL is below a meaningful signal threshold.
  Testing abstention before resolving the ordering confound would not advance the
  Claim B floor-mapping goal. Additionally, modifying the prompt template requires
  a separate locked template and is a larger change than context ordering.

Recommendation: defer unless Manager explicitly scopes a NULL-calibration test.
```

---

## 3. One-axis constraint

```text
Cell02 must change exactly one axis from Cell01.

This constraint is non-negotiable absent explicit Manager authorization for an
interaction test. Changing multiple axes simultaneously makes it impossible to
attribute any outcome difference to a single variable.

Permitted changes for a position/ordering Cell02:
  Context ordering (which fact appears at which position): YES
  Token construction (new tokens following same protocol): YES — required if new items generated;
    same BPE-Jaccard audit applies; new tokens must pass Gate 0.5 under run tokenizer
  Number of chains per item (3): NO — locked at Cell01 baseline
  Context length (7 facts): NO — locked
  Relations ('links to', 'maps to'): NO — locked
  Prompt template: NO — locked (sha256:c8a81a29...)
  Scorer: NO — locked (sha256:060afad9...)
  Validator: NO — locked (sha256:bcc26ca0...)
  BPE-Jaccard threshold (j ≥ 0.40): NO — locked
  Query types: NO — locked (hop1, hop2, composite, negative_graph)
  Decoding (temperature=0.0, max_tokens=16): NO — locked

Note on new token generation:
  If Cell02 uses new token pools (required if new items are generated rather than reordering
  Cell01 items), those tokens must pass the same Gate 0.5 audit under the run tokenizer
  sha256:c0382117.... The audit protocol is fixed; only the token set changes.
```

---

## 4. Design requirements for a position/ordering Cell02

The following requirements must be satisfied. They are design preconditions, not a construction authorization.

```text
DR1 — Single-axis change:
  The only difference from Cell01 must be context ordering.
  All locked construction constants (relations, context length, chain count, prompt,
  scorer, validator, thresholds) must carry over unchanged.

DR2 — Ordering specification:
  The target hop2 fact position must be explicitly specified as an axis variable.
  Acceptable forms: all C_target-last; all C_target-middle; inverted group (C_target-first
  items from Cell01 reconstructed at C_target-last position). The specific form requires
  Manager approval.

DR3 — New token audit:
  If new token pools are generated for Cell02, the full Gate 0.5 audit must be re-run
  under sha256:c0382117... (the FP16 run tokenizer). The prior Cell01 audit result does
  not carry over to new token pools.

DR4 — Manifest validation:
  24/24 validate_manifest must pass before any run.

DR5 — Runner dry-run:
  The amended runner (sha256:f346e4f2...) or a successor must pass --dry-run before
  any live inference.

DR6 — Stage 0 lock:
  A new Stage 0 lock packet is required for Cell02 before any inference.
  Cell01 Stage 0 artifacts do not cover a new cell.

DR7 — Claim B scope:
  Cell02 is a Claim B axis test only. It does not authorize stress testing (INT8/INT4),
  Track B, or Claim C evaluation.
```

---

## 5. Pre-authorization requirements

Before Cell02 can be constructed or run, the following must occur in order:

```text
1. Manager authorization for Cell02 construction
   Required before any item generation, token construction, or manifest build.

2. Cell02 design specification reviewed and accepted by Team Lead
   Must specify: ordering variant (Option 1a vs 1b), n_items, token construction protocol,
   and how the one-axis constraint is enforced.

3. Token construction and Gate 0.5 audit (offline only)
   New token pools generated; BPE-Jaccard audit run under sha256:c0382117...;
   all near-miss pairs confirmed j ≥ 0.40.

4. Cell02 Stage 0 lock
   Manifest schema, scorer, and validator hashes confirmed for Cell02.
   Smoke test passing.

5. Threshold review
   Current thresholds (Gate-2 ≥ 21/24, etc.) apply unless Manager authorizes revision.
   No threshold changes authorized for Cell02 absent separate approval.

6. Stage 1 preparation lock for Cell02
   Runner amended if needed; dry-run PASS; authorization boundary confirmed.

7. Manager authorization for Cell02 Stage 1 execution
   Separate from construction authorization.
```

---

## 6. Authorization boundary

```text
This memo authorizes:
  axis decision recording
  design requirements documentation
  pre-authorization requirements documentation

This memo does NOT authorize:
  Cell02 construction
  item generation
  token pool creation
  model inference
  Cell01 rerun
  confirmation pass
  7B, INT8, INT4, Track B
  Cell02 Stage 0 or Stage 1 work
  any change to locked Cell01 artifacts
```

---

## 7. Disposition record

```text
Cell01 disposition (final):
  VALID FP16 constructibility-boundary result for Claim B
  Accepted by Team Lead 2026-06-08
  Multi-axis map entry filed: CLAIM-B-MAP-ENTRY-TWOHOP-L1-CELL01.md
  Tokenizer reconciliation: COMPLETE
  Gate 0.5: CLOSED

Provisional next axis (not authorized):
  Position / ordering — invert or isolate C_target-first ordering condition
  while holding distractor geometry constant

One-axis rule:
  Cell02 changes only one axis absent explicit Manager authorization for interaction test

Cell02 status:
  NOT AUTHORIZED — pending Manager authorization per pre-authorization requirements above
```

---

**Axis decision recorded. Cell02 construction requires separate Manager authorization.**

— CS Engineer, 2026-06-08
