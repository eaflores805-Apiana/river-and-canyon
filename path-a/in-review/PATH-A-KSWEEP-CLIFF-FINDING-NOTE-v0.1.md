# PATH-A K-SWEEP — CLIFF FINDING NOTE (positional, mechanism-free) v0.1

**E. A. Flores**, Apiana AI, Inc. — June 16, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. Descriptive finding from the verified scout (repo HEAD `3cfdc3f`). Records what the bytes show; asserts no mechanism.*

## 0. What this note is

A claim-safe record of the one finding the K=1…5 load scout produced, stated **positionally** and **before any hypothesis about why**. The cliff is the finding now; what causes it is a separate, unresolved question that this note deliberately does not contaminate the record with. Mechanism is unspecified throughout. This note certifies nothing, authorizes nothing, and does not reopen the closed K=5 FAIL (which it reproduces).

## 1. The finding (SE-recomputed from repo bytes)

```text
K   validated-R1   Wilson 95% CI          off-map positional rate (decoy answer-depth + decoy bridge)
1   29/96 = 0.302  [0.219, 0.400]         0.219
2   16/96 = 0.167  [0.105, 0.254]         0.260
3   15/96 = 0.156  [0.097, 0.242]         0.271
4   19/96 = 0.198  [0.131, 0.289]         0.385
5   18/96 = 0.188  [0.122, 0.277]         0.396   (reproduces the closed FAIL byte-exact: 384-key join, prompts + outputs identical)
```

Two positional facts, both verified independently from the per-cell scored artifacts this session:

1. **Validated-R1 cliffs from K=1 to K=2 and then plateaus.** K=1 sits at 0.302; K=2 drops to 0.167 (~13.5 points); K=2…5 are a flat band (0.156–0.198) with all four Wilson intervals overlapping.
2. **The off-map positional rate climbs monotonically across K=1…5** (0.219 → 0.396): answers land at the *right depth* in the *wrong chain*, at a rate that rises with the number of competing chains.

## 2. What this finding is NOT (the containment — read before interpreting)

```text
- NOT "detail drift," and NOT "the model dropped a detail mid-traversal." Those are PROCESS claims.
  The bytes are POSITIONAL: the answer lands at the correct depth in a wrong chain. We do not know
  whether the model traversed-and-dropped, grabbed-by-relation, or anchor-drifted — the run cannot
  separate (a) traversal / (b) relation-keyed grab / (c) chain-anchor inconsistency. Mechanism is
  unspecified, by the limits of the instrument.

- NOT a "threshold" or a "complexity boundary being crossed." K=1 and K=2 are ADJACENT integers with
  nothing measured between them. A jump-then-plateau is EQUALLY consistent with the duller null:
  K=1 is the TRIVIAL EDGE (one distractor — almost nothing to get wrong), and K>=2 is simply this
  construction's operating regime. No trigger, no boundary-crossing is established. The dull null is
  the leading reading until something rules it out (see §3).

- K VARIES COMPETITORS, NOT HOPS. Every cell is the SAME two-hop task. The variable that changes
  K=1 -> K=2 is "one competing decoy chain -> two," not "more reasoning steps." Any description in
  terms of "extra hops" is wrong about the variable.

- NO SLOPE OR SHAPE IS PRESUMED in either direction. The program's own terminal-attraction
  bounds-sweep ran REVERSE-K (terminal-grab FELL with clutter, 0.708 -> 0.250 -> 0.083, now
  byte-verified), which is standing proof that clutter-related rates on this substrate do not move
  the way intuition expects. So neither "rises with load" nor "thresholds at K=2" is a safe default;
  the off-map rate's climb is recorded as observed, not explained.
```

## 3. The leading interpretation (stated as the default, not a conclusion)

The most parsimonious reading of the cliff is the **dull null**: K=1 is trivial (one decoy, the task is too easy to fail much), and K≥2 is what the construction does once there is real competing material — a flat FAIL-band. On this reading there is no "trigger" and no threshold to explain; the apparent cliff is the trivial edge falling away. This is consistent with the corroborating control evidence (hop2 retrieval is below the 0.75 floor at every K except K=1), which says the substrate is under the retrieval floor across the plateau, not that something switches on at K=2.

Whether instead there is genuine threshold structure is **not decidable from two adjacent points**, and is left open. Discriminating "diffuse plateau" from "structured subset" is the subject of a separate, pre-declared probe (see the consistency-probe pre-declaration) — which must be locked before the existing data is re-sliced, because re-cutting committed data after seeing the cliff is analytical fishing unless the cut is pre-committed.

## 4. Status

```text
- Positional finding, mechanism-free, descriptive. From the verified scout at HEAD 3cfdc3f.
- The closed K=5 FAIL stands; this note reproduces it as the scout's internal check, does not reopen it.
- Certifies nothing, advances no mechanism claim, authorizes nothing.
- Routes Senior-draft -> TL/New Senior (record); the "why" question is deferred to the pre-declared
  consistency probe, which locks before any new analytical cut.
```

— Senior Engineer (descriptive finding; routes for record)
