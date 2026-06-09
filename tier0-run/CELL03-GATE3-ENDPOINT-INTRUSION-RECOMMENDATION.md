# Cell03 Gate 3 Endpoint-Intrusion Threshold — CS Recommendation

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**In response to:** Team Lead memo — "Cell03 Scorer Re-lock Packet — Team Lead Disposition" §6, 2026-06-08
**Status:** RECOMMENDATION ONLY — no threshold is amended or authorized by this document

---

## Recommendation: Option B

**Defer the Gate 3 endpoint-intrusion threshold amendment.**

Proceed with Cell03 construction under the existing locked Gate 3 thresholds, with §8
endpoint-intrusion diagnostics as mandatory non-blocking diagnostics.

---

## Rationale

### 1. Gate 3 is a composite-quality stress-eligibility gate — not a hop1 failure gate

The locked Gate 3 thresholds (all five ceilings) apply to composite FORMAT_PASS items only.
This scope is intentional: Gate 3 determines whether the FP16 composite signal is clean enough
to support Track B stress interpretation. It is not designed to gate hop1 failure behavior.

Adding a hop1 ct-anchoring ceiling to Gate 3 would conflate two structurally different quality
dimensions:

```text
Gate 3 (existing):
  Composite operation fidelity — is the composite signal clean for stress?
  Denominator: composite FORMAT_PASS items.

Proposed endpoint-intrusion gate:
  Hop1 failure mode rate — how often does the model return ct on hop1?
  Denominator: hop1 FORMAT_PASS items.
```

Combining these under the same gate number creates ambiguity about what Gate 3 failure means.
Option A should either redefine Gate 3 scope explicitly or create a new gate number. Either
requires full threshold proposal cycle under the locked protocol.

### 2. The §8 framework is the correct home for ct-anchoring

The Gate 5 / §8 split (confirmed by Senior, accepted by Team Lead) was established precisely
to separate high-score shortcuts (Gate 5) and composite-quality gates (Gate 3) from low-score
failure diagnostics (§8). ct-anchoring on hop1 is explicitly §8:

```text
ct-anchoring on hop1:
  Model returns ct when bt is expected.
  score = 0.0 on hop1 by construction (ct ≠ bt).
  This is a low-score failure diagnostic — §8, not Gate 3 or Gate 5.
```

A hop1 endpoint-intrusion ceiling in Gate 3 would move a §8 diagnostic into the gate ladder
without a principled basis for the threshold value.

### 3. The threshold value has no empirical basis before Cell03 runs

Any Gate 3 endpoint-intrusion ceiling would require a specific number (e.g., ≤ k/24 wrong_neighbor
on hop1). Cell02 produced 11/24 ct-anchoring on hop1. But Cell02 had four confounded cues;
Cell03 is specifically designed to disentangle them. The right endpoint-intrusion rate for a
balanced-C-rank, separated-adjacency cell is unknown before Cell03 produces data.

Setting the ceiling at ≤ 3/24 (by analogy with the composite wrong_neighbor ceiling) would
apply a composite-domain calibration to a different query type, without validation.

Setting it at any higher value (e.g., ≤ 11/24, derived from Cell02) would be post-hoc
threshold calibration: the ceiling would be set to pass Cell02 rather than established
independently.

There is currently no defensible value to file. Option A would require either an underpowered
prior estimate or a placeholder, both of which are weaker than the existing §8 diagnostic
architecture.

### 4. Cell03's experimental purpose conflicts with making ct-anchoring a gate condition

Cell03 is an attraction-cue mapping step. Its primary measured variable is whether
ct-anchoring on hop1 changes relative to Cell02 under separated adjacency and balanced C-rank.

If ct-anchoring rate is a Gate 3 condition, then:

```text
High ct-anchoring → Gate 3 FAIL → cell is not stress-eligible.
```

But a Cell03 with high ct-anchoring would be a scientifically informative result: it would
tell us that adjacency/proximity separation does not reduce endpoint intrusion, pointing toward
absolute position, C-rank, or answer-domain salience as the load-bearing cue. Under Option A,
this finding would fail Gate 3 and block advancement — not because the cell is poorly
constructed, but because the experimental manipulation produced its expected range of outcomes.

Making the experimental outcome variable a gate condition inverts the measurement logic.

### 5. §8 diagnostics already required as standing mandate

Team Lead standing requirement (from CELL03-SCORER-AMENDMENT-PLAN.md §5) mandates §8 diagnostics
in all Cell03 run summaries:

```text
hop1 expected bt, returned ct
negative_graph expected NULL, returned endpoint
returned ct vs returned other C endpoint
returned B endpoint vs returned C endpoint
absolute position of returned endpoint
C-rank of returned endpoint
adjacency/proximity of returned endpoint
```

These diagnostics produce the endpoint-intrusion record that Option A's gate would try to
bound. The §8 record is required and complete; it simply is not a gate condition.

---

## What Option B requires

For Option B to be implemented cleanly, the following must be explicit in the Cell03 runner
and run summary:

```text
1. §8 endpoint-intrusion diagnostics are MANDATORY, not optional.
   The run summary must include all seven §8 items above regardless of ct-anchoring rate.

2. §8 results are NON-BLOCKING.
   Any ct-anchoring rate is a valid Cell03 result and does not fail any gate.
   A high rate is a finding that informs Cell04+ axis selection, not a construction failure.

3. The standing caveat is mandatory in all Cell03 documents:
   Gate 5 does not close target-token anchoring as a composite shortcut.
   Composite ct-return is correct by construction and cannot be made ceiling-bearing.
   Composite target-token anchoring is tracked through §8 diagnostics, especially
   hop1 failures returning ct.

4. Wrong_neighbor ceiling on composite (≤ 3/24) remains binding under existing Gate 3.
   This covers cases where the model returns the wrong target-chain neighbor on composite —
   a distinct diagnostic from hop1 ct-anchoring.
```

---

## What Option A would require (deferred)

If Team Lead / Manager later decides Option A should proceed:

```text
1. Define the threshold value independently (not derived from Cell02 data post-hoc).
   Requires justification: theoretical baseline, analogy to existing ceilings,
   or empirical basis from Cell03 data (which means Option A cannot precede Cell03).

2. Identify the denominator.
   Hop1 FORMAT_PASS items? Hop1 attempted items? Composite FORMAT_PASS?

3. Define the numerator.
   target_chain_wrong_neighbor on hop1 only?
   Or all wrong_neighbor cases where the returned token = ct specifically?
   The scorer does not currently distinguish "wrong_neighbor where returned = ct"
   from other wrong_neighbor cases. A sub-type diagnostic would require a scorer
   amendment (new hash, Manager authorization).

4. Determine the gate number.
   Gate 3b? Gate 3a-hop1? A new Gate 6?
   This is a naming and sequencing decision requiring Team Lead input.

5. Full threshold proposal cycle: CS draft → CS review → Team Lead → Manager authorization.
   This is another authorization cycle before Cell03 construction.
```

Option A, properly implemented, adds material delay and requires an empirical basis that does
not exist until after at least one Cell03 run. It is not executable before Cell03 without
accepting an underpowered or post-hoc threshold.

---

## Summary

```text
Recommendation:      Option B — defer Gate 3 endpoint-intrusion amendment
Rationale:           Gate 3 is composite-only; §8 is the correct architectural home;
                     no defensible threshold value exists pre-Cell03;
                     making the experimental outcome variable a gate condition is
                     methodologically inverted.

What Option B requires:
  §8 endpoint-intrusion diagnostics mandatory and non-blocking in Cell03 runner/summary
  Standing caveat mandatory in all Cell03 documents
  Composite wrong_neighbor Gate 3 ceiling (≤ 3/24) remains binding (unchanged)

What remains blocked:
  Cell03 construction — awaiting Team Lead / Manager disposition on this recommendation
  Option A — deferred pending empirical basis and separate authorization cycle
```

**Recommendation filed. Awaiting Team Lead / Manager disposition before Cell03 construction is authorized.**

— CS Engineer, 2026-06-08
