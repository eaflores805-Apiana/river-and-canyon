# PROGRAM-MAP-RECONCILIATION-v0.1

**Version:** v0.1. River and Canyon program. Phase-0 governance artifact (mini-map Stage D).
**Status:** model-free decision surface. Lays out how Lane 1a′ fits the 2026-06-10 project map and presents Readings A / B / C for the Manager to choose. Drafts the decision; does not make it. Authorizes nothing.
Owner/drafter: Senior Engineer · Team Lead: summarizes decision surface · Manager: chooses A / B / C · CS: verifies the filed map (Program Map v2) once the choice is made.

## 1. The question

```text
How does Lane 1a′ — the Semantic-Read Operationalization phase and the
constructed-positive arc, including the quarantined INT8-RUNG-1 — fit into the
project map of record (governance/passdown/2026-06-10_project-map.md)?
Until this is decided, the active route is ambiguous (route-state RED), and no
model-facing execution can be GREEN.
```

## 2. The map of record (lane structure, verbatim anchors)

```text
Lane 0  Paper 3 v1.1 (authorized, manuscript-only)
Lane 1  candidate selection (Manager gate)
Lane 1a feasibility sweep / reconnaissance (proposed, Manager-gated, UNDECIDED)
        doctrine: "Lane 1a may rule out; it may not rule in" — pre-candidate,
        negative-use-only, may not rank/recommend/certify/inform thresholds
Lane 2  threshold-sheet population + lock (Manager gate)
Lane 3  certification evaluation = Paper 4 (Manager gate)
Lane 4  FIRST COMPRESSION RUNG — INT8/INT4 on a CERTIFIED baseline (Manager gate)
Lane 5  deliberate clean-construction attempt (P1)
Lane 6  external validation
Far horizon: Claim C / compositional seam (hard-gated)
```

The structural fact: **the map places the first compression rung at Lane 4, behind Lane 3 certification, on a *certified* baseline.** Lanes 1, 2, 3 (candidate selection → threshold lock → certification) all precede any rung.

## 3. What actually happened (Lane 1a′, byte-anchored)

```text
- The Semantic-Read Operationalization phase ran a constructed-positive arc:
  design → P1/P2/P3 desk prerequisites → a CONSTRUCTED matched pair → a
  validation run (defective eliminated, clean spared, item 6 byte-verified) →
  then a first INT8 compression rung on that validated pair.
- The pair was VALIDATION-passed, NOT certified. Lane 3 certification never
  occurred in formalized form.
- The INT8 rung ran during a Team Lead route-alignment pause and is QUARANTINED
  (scientifically retainable, procedurally nonconforming).
```

So the executed rung does **not** occupy the map's Lane-4 slot: that slot is a rung on a *certified* baseline, and no certified baseline exists.

## 4. The three readings (decision surface; Senior does not choose)

### Reading A — the map was stale; 1a′ was a legitimate reconnaissance detour

```text
CLAIM: Lane 1a′ is a prime variant of the reconnaissance lane (Lane 1a), a
legitimate detour the map did not anticipate. The INT8 rung is a Lane-1a′
RECONNAISSANCE observation — consistent with "Lane 1a may rule out, may not rule
in" — categorically distinct from the Lane-4 certified rung.
CONSEQUENCE IF CHOSEN:
  - Build Program Map v2 that ADDS Lane 1a′ (the semantic-read operationalization
    + constructed-positive arc) to the lane structure, with Lane 4 unchanged as
    the later certified rung.
  - INT8-RUNG-1 remains reconnaissance-only; not promotable to Lane 4.
  - The next route proceeds toward a CERTIFIED baseline (the Lane 1→2→3 track)
    before any official Lane-4 rung.
TENSION TO ACKNOWLEDGE: Lane 1a doctrine is "negative-use only / may not rule
in." The constructed-positive arc did more than rule out — it built and validated
a positive control. Reading A must therefore treat 1a′ as a BROADER detour than
Lane 1a (instrument-construction + validation, not just elimination sweep), which
is a real extension of the map, not just an annotation.
```

### Reading B — the route drifted past Lanes 1–3

```text
CLAIM: momentum toward "first compression rung" skipped the map's ordering
(candidate selection → threshold lock → certification all precede any rung).
The 1a′ work, however valuable, ran ahead of its gates.
CONSEQUENCE IF CHOSEN:
  - Record the drift explicitly.
  - Return to the earliest unsatisfied lane (Lane 0 if Paper 3 v1.1 is still the
    live manuscript gate, else Lane 1 candidate selection) and proceed IN ORDER.
  - The 1a′ desk artifacts (semantic-read template, the P1/P2/P3 specs, the
    constructed pair) are retained as reusable instrument components but do not
    advance the lane sequence.
  - INT8-RUNG-1 stays quarantined; it preceded its gate and cannot substitute
    for a Lane-4 result.
TENSION TO ACKNOWLEDGE: this treats genuinely useful instrument work as
off-sequence. The work is not wasted (the components are reusable), but Reading B
is the most conservative reading and the slowest to a measurement.
```

### Reading C — the Manager defines a revised third route

```text
CLAIM: neither A nor B is quite right; the Manager specifies a new route that
takes what is true from each.
A PLAUSIBLE SHAPE (illustrative only — the Manager defines the actual route):
  - Accept 1a′ as a legitimate instrument-development phase (from A), AND
  - require the certification track (Lane 1→2→3) before any official rung (from
    B), AND
  - fold the Baseline Gate Diagnosis (mini-map Stage E) in as the gate that
    decides whether a certifiable baseline is even reachable — making the next
    route conditional on that diagnosis.
CONSEQUENCE IF CHOSEN: Program Map v2 is authored to the Manager's revised route.
```

## 5. What all three readings share (so the decision is safe either way)

```text
1. INT8-RUNG-1 is NOT promotable to official Lane-4 status under any reading.
   An official first-rung result requires a conforming run on a certified
   baseline. (This is invariant; the readings differ on route, not on this.)
2. The 1a′ instrument components (semantic-read template, P1/P2/P3, constructed
   pair) are retained and reusable under all readings.
3. No official Lane-4 rung happens before a CERTIFIED baseline exists.
4. The Baseline Gate Diagnosis (Stage E) is a real gate on whether a certified
   baseline is reachable at all — relevant under every reading.
```

Because the readings converge on these four points, the route stays disciplined no matter which the Manager picks; the choice affects the *map's shape and the next lane*, not whether the quarantined rung counts (it does not) or whether the components survive (they do).

## 6. The decision requested

```text
Manager selects: READING A / READING B / READING C (and if C, specifies the route).
On that choice:
  - Senior drafts PROGRAM MAP v2 to the selected reading (separate authorized step);
  - CS verifies the filed Program Map v2;
  - the active route ceases to be ambiguous → route-state can move from RED
    toward YELLOW/GREEN per ROUTE-STATE-GATE-v0.1.
```

## 7. Done-when (Stage D completion)

```text
PROGRAM MAP v2 is accepted AND the active route is no longer ambiguous.
(This artifact is the decision surface; Program Map v2 is the separate product
authored after the Manager chooses.)
```

## 8. No-authorization footer / closed gates

This reconciliation authorizes no execution and does not itself supersede the map (Program Map v2 is a separate authored step after the Manager's choice). Closed throughout: no model-facing execution · no INT4 · no second compression rung · no full ladder · no Path B execution · no Path D execution · no schedule v2 supersession · no candidate certification · no ranking · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission.

— Senior Engineer
