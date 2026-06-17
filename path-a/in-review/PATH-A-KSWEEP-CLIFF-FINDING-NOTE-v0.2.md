# PATH-A K-SWEEP — CLIFF FINDING NOTE (positional, mechanism-free) v0.2

**E. A. Flores**, Apiana AI, Inc. — June 16, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. Descriptive finding from the verified scout (repo HEAD `3cfdc3f`). Records what the bytes show; asserts no mechanism. Supersedes v0.1 (`ee5ed1ef…`), retained.*

> **v0.2 revision note.** Adds the hop2-isolated floor column (SE-recomputed from repo bytes this session) and the foreclosure it implies — the admissible-load set on this construction is {K=1}, so there is no non-trivial operating point to tune toward. The causal clause from the discussion ("because chain identity rests on an arbitrary token") is **kept out of the body** and demoted to a labeled next-hypothesis footer: the bytes establish the foreclosure, not its cause. No prior finding changed.

## 0. What this note is

A claim-safe record of what the K=1…5 load scout produced, stated **positionally** and **before any hypothesis about why**. Mechanism is unspecified throughout the body. Certifies nothing, authorizes nothing, and does not reopen the closed K=5 FAIL (which it reproduces).

## 1. The finding (all columns SE-recomputed from repo bytes at HEAD `3cfdc3f`, this session)

```text
K   validated-R1   Wilson 95% CI        off-map positional   hop2-ISOLATED pass   vs floor 0.75
                                        rate (dC + dB)       (the component op)
1   29/96 = 0.302  [0.219, 0.400]       0.219                76/96 = 0.792        ABOVE  (only cell)
2   16/96 = 0.167  [0.105, 0.254]       0.260                64/96 = 0.667        below
3   15/96 = 0.156  [0.097, 0.242]       0.271                71/96 = 0.740        below
4   19/96 = 0.198  [0.131, 0.289]       0.385                58/96 = 0.604        below
5   18/96 = 0.188  [0.122, 0.277]       0.396                65/96 = 0.677        below   (reproduces closed FAIL byte-exact)
```

Three positional facts, each verified independently from the per-cell scored artifacts:

1. **Validated-R1 cliffs from K=1 to K=2 and then plateaus** (0.302 → 0.167, then a flat 0.156–0.198 band with all four Wilson intervals overlapping).
2. **The off-map positional rate climbs monotonically** across K=1…5 (0.219 → 0.396): answers land at the *right depth* in the *wrong chain*, at a rate rising with the number of competing chains.
3. **The component operation (hop2, queried in isolation) clears its own 0.75 floor only at K=1** (0.792). Under competition (K≥2) hop2 is sub-floor at every level (0.667 / 0.740 / 0.604 / 0.677).

## 2. What this finding is NOT (the containment — read before interpreting)

```text
- NOT "detail drift" / "the model dropped a detail mid-traversal." Those are PROCESS claims. The
  bytes are POSITIONAL: the answer lands at the right depth in a wrong chain. The run cannot separate
  (a) traversal / (b) relation-keyed grab / (c) chain-anchor inconsistency. Mechanism unspecified.

- NOT a "threshold" or a "complexity boundary being crossed." K=1 and K=2 are ADJACENT integers with
  nothing measured between them. Jump-then-plateau is EQUALLY consistent with the duller null: K=1 is
  the TRIVIAL EDGE (one distractor), K>=2 is simply this construction's regime. No trigger established.

- K VARIES COMPETITORS, NOT HOPS. Every cell is the SAME two-hop task. The variable across K=1->2 is
  "one competing decoy chain -> two," not "more reasoning steps."

- NO SLOPE OR SHAPE PRESUMED. The program's terminal-attraction bounds-sweep ran REVERSE-K (terminal-
  grab FELL with clutter, 0.708 -> 0.250 -> 0.083, byte-verified) — standing proof that clutter-related
  rates on this substrate do not move the way intuition expects. The off-map climb is recorded, not explained.
```

## 3. The foreclosure (claim-safe — what the floor column implies)

```text
- The component operation (hop2 in isolation) is ADMISSIBLE (clears its 0.75 floor) only at K=1.
  Under genuine competition (K>=2) it is INADMISSIBLE at every level.
- Therefore the ADMISSIBLE-LOAD SET on this construction is {K=1}. And {K=1} is the trivial cell —
  one distractor, nothing real to compose against — so it is not a valid composition gate.
- THEREFORE there is NO non-trivial operating point on this construction. "Shift complexity to raise K
  and drop the off-map" presumes a knob exists that preserves the gate; the floor data shows there is
  none here: the only load where the component is admissible is the trivial one, and the only way to
  create headroom at K>1 would be to make the chains easier to separate — which imports a non-traversal
  route (tag/topic-match) and changes the question (R2/R3), i.e. loosening the gate.
- THEREFORE the 40% off-map is the instrument CORRECTLY REPORTING that this substrate cannot perform
  hop2 under competition on this construction. It is the SUBSTRATE CEILING for this construction, not a
  defect to engineer away. The honest output is to REPORT the ceiling, not tune toward it.
```

This is a stronger statement than "the scout found no band": it says **why** there is no band — the component operation is inadmissible under any real competition here — rather than merely that none was found. What this note does **not** assert is *why* the component is inadmissible (see footer).

## 4. Leading interpretation (the default, not a conclusion)

The most parsimonious reading of the cliff is the **dull null**: K=1 is trivial, and K≥2 is what the construction does once there is real competing material — a flat FAIL-band. The hop2-isolated floor column **is** the corroboration: the substrate is under the component-retrieval floor across the whole plateau, which says the component simply doesn't hold under competition here — not that something switches on at K=2. No "trigger" is required to explain the cliff. Whether there is genuine threshold structure instead is not decidable from two adjacent points and is left open (and is the subject of the separately-pre-declared consistency probe, which locks before any re-slice of this data).

## 5. The forward question (correctly pointed, correctly bounded)

```text
Re-run the component-floor check on the V3 (foreclose-all) construction — one that does NOT rest chain
identity on an arbitrary token. Does hop2 clear its floor under competition there?
  YES -> a real operating point exists; the composition gate becomes runnable at that K.
  NO  -> substrate-infeasibility accumulating (the recurrence V3's own residual-risks section pre-flagged);
         the honest output is the ceiling, NOT a third construction.
This is a NEW RUN under its own pre-registration and Manager by-name authorization — NOT a slice of this
data — and it sits downstream of: the construction-philosophy decision, the V3 instrument byte-audit, and
the V3 build. It is the correctly-ordered next step, not a step available today.
```

## 6. Status

```text
- Positional finding, mechanism-free, descriptive. All columns SE-recomputed from repo bytes at HEAD 3cfdc3f.
- The closed K=5 FAIL stands; this note reproduces it as the scout's internal check, does not reopen it.
- Certifies nothing, advances no mechanism claim, authorizes nothing.
- Routes Senior-draft -> TL / New Senior (record).
```

---

**NEXT-HYPOTHESIS — NOT A FINDING (explicitly labeled, kept out of the body above):**
*One plausible cause of the hop2 fragility under competition is that this construction rests chain identity on an arbitrary head token, so adding competitors degrades component retrieval itself. The floor data establishes the foreclosure (hop2 inadmissible under competition → admissible-load set {K=1}); it does **NOT** establish this cause. "Arbitrary-token chain identity causes the fragility" is a hypothesis, testable only by the V3 floor check (§5) — where the construction does not rest identity on an arbitrary token — not by anything in this dataset. It is recorded here as a next-hypothesis so it is not lost, and is firewalled from the note's claim surface so the note ships no uncertified mechanism.*

— Senior Engineer (descriptive finding; routes for record)

---

## Changelog v0.1 → v0.2

```text
ADDED   §1 hop2-isolated floor column (76/96=0.792 at K=1, ABOVE 0.75; 0.667/0.740/0.604/0.677 at
        K=2-5, all below), SE-recomputed from repo bytes this session, same provenance standard as
        the cliff column (per the provenance catch: the floor series is SE-recomputed-and-relayed,
        now stamped as such, not stated as ambient fact).
ADDED   §3 foreclosure — admissible-load set {K=1}; component inadmissible under competition; no
        non-trivial operating point; "raise K to drop the off-map" has no gate-preserving knob on
        this construction; the 40% is the substrate ceiling, not a defect to tune away. Stated
        claim-safe (no causal clause).
MOVED   the "because chain identity rests on an arbitrary token" causal clause OUT of the body and
        into a labeled NEXT-HYPOTHESIS footer (bytes establish the foreclosure, not its cause).
UNCHANGED  the cliff and off-map facts (§1); the not-detail-drift / not-threshold / competitors-not-
        hops / no-slope containment (§2); the dull-null leading interpretation (§4); mechanism
        unspecified in the body; no-certification / no-authorization scope.
```
