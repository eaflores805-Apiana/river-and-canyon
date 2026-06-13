# P1-OFF-CEILING-CALIBRATION-DESK-RANGE-v0.1

**Version:** v0.1. River and Canyon program. Semantic-Read Operationalization phase (constructed-positive readiness, P1).
**Status:** model-free desk artifact. Proposes a calibration *direction and range* in qualitative terms; sets no threshold, runs no model, certifies nothing. Authorizes nothing.
Owner/drafter: Senior Engineer · CS: identity + guard verification · Team Lead: routing, ledger.
Ledger: SEMANTIC-READ-OPERATIONALIZATION-LEDGER-v0.2.1.md · INDEX is canonical artifact catalog.

## 1. Artifact identity

P1-OFF-CEILING-CALIBRATION-DESK-RANGE-v0.1.md — second of three desk prerequisites (P2→P1→P3). Specifies how the clean member of the constructed-positive could be made harder than the current D4 pilot without becoming defective, so it lands off the saturation ceiling.

## 2. Purpose

Specify, model-free, how the clean member could be made harder than current D4 (which saturates at 80/80) so it lands inside the resolvable window — using only the four already-exposed D4 levers, without setting any threshold value or certifying any candidate.

## 3. Claimed concept

> Increasing task load along the exposed D4 levers (list length, queried-key position, vocabulary, key uniqueness) moves the clean member's accuracy *downward from ceiling* in a controllable direction, and a range of load settings can be *proposed* at desk level such that the clean member is expected to sit off ceiling while remaining fully answerable (non-defective).

This is a directional/range claim, not a threshold. No accuracy value is set; the claim is about which way each lever pushes difficulty and that a proposable range exists.

## 4. The levers and their proposed direction (qualitative; no values set)

```text
list length:        the pilot uses 5 pairs. Increasing the number of pairs
                    raises retrieval load monotonically (more candidates to
                    scan, longer context). DIRECTION: more pairs → harder.
                    Proposed range: a band above the pilot's 5, left as a band
                    to be narrowed empirically under a future gated step.
queried-key position: the pilot concentrates at slot 3 (44/80) with tails at
                    1 and 5. Biasing the queried key toward interior/late
                    positions in longer lists raises difficulty (more
                    intervening pairs before the target). DIRECTION: deeper
                    position → harder.
key/value vocabulary: larger or more confusable token vocabularies raise
                    discrimination load. DIRECTION: larger/confusable → harder.
                    Held mild here to avoid introducing a second defect-like
                    confound; vocabulary is primarily a P3 match dimension.
key uniqueness:     the pilot already contains a 12/80 multi-occurrence-key
                    stratum. Multi-occurrence keys raise difficulty (the model
                    must resolve which pairing is queried). DIRECTION: more
                    ambiguity → harder — BUT this lever is constrained (§5),
                    because ambiguity can blur the clean/defective distinction.
```

## 5. Constraint: harder-but-still-clean (the non-defective boundary)

The calibration must raise difficulty without crossing into the P2 defect. The boundary is explicit:

```text
- the clean member's queried key must REMAIN PRESENT and uniquely answerable
  (P2's defect is key-absence; calibration must not approach key-absence).
- key-ambiguity (multi-occurrence) is therefore bounded: it may raise difficulty
  but must not render the queried key's value non-constructible, or it would
  collide with the P2 defect and destroy the single-difference design.
- preferred load levers are LENGTH and POSITION, which raise difficulty without
  touching constructibility; vocabulary and ambiguity are secondary and bounded.
```

So the proposed calibration favors length and position (orthogonal to the defect axis) and treats ambiguity as a constrained, optional lever.

## 6. Proposed range (desk-level, explicitly not a threshold)

```text
The off-ceiling target is the qualitative window  floor < a < ceiling − δ:
  - ABOVE the shortcut floor (union envelope 0.6125 in the pilot) by a
    resolvable margin, so the clean member is not confusable with shortcut
    behavior;
  - BELOW the saturation ceiling by resolvable room δ, so a defect-induced drop
    has somewhere to land.
The desk RANGE is therefore: load settings increased from the pilot along
length/position until the clean member is EXPECTED to leave ceiling but is still
EXPECTED to clear the shortcut floor with margin. Exact settings and the value
of δ are GATED — they require a model run to fix and are not set here.
This artifact proposes the SEARCH DIRECTION and the BAND, not a point.
```

## 7. Shown semantic-read of this artifact's own load-bearing claim

```text
1. artifact:            P1-OFF-CEILING-CALIBRATION-DESK-RANGE-v0.1.md
2. path:                semantic-read-operationalization/P1-OFF-CEILING-CALIBRATION-DESK-RANGE-v0.1.md
3. commit:              this filing (CS verifies)
4. sha256:              on filing (CS verifies)
5. claimed concept:     a proposable off-ceiling load RANGE exists using exposed
                        D4 levers, with the clean member staying non-defective.
6. check performed:     read each lever's difficulty direction against the D4
                        structure and pilot scores (5 pairs, slot distribution,
                        envelope 0.6125 / ceiling) from the C1/C2 desk read v0.2;
                        confirmed length and position raise difficulty without
                        touching constructibility, and that the non-defective
                        boundary (§5) keeps calibration disjoint from P2.
7. observed structure:  difficulty is monotone in length and position depth;
                        constructibility is independent of those two levers;
                        ambiguity touches constructibility and is therefore
                        bounded.
8. required structure:  a calibration proposal must raise difficulty, stay
                        non-defective (disjoint from P2), set no threshold, and
                        run no model.
9. surplus check:       ABSENT — no second concept introduced; the calibration
                        deliberately avoids the defect axis so it cannot smuggle
                        in a second difference.
10. disposition:        PASS — observed structure satisfies required structure,
                        as a directional/range proposal (not a value).
— non-authorization footer (below) —
```

## 8. Disposition

```text
DISPOSITION: PASS
```

A model-free off-ceiling calibration range is specifiable: length and position raise difficulty orthogonally to the P2 defect, a resolvable band between shortcut floor and saturation ceiling is the qualitative target, and no threshold is set. The exact settings and δ remain gated to a future model run.

## 9. No-authorization footer

This calibration desk-range authorizes no constructed-positive generation, no seeded-defect exercise, no candidate generation, no model execution, no model loading, no sweep_id creation, no token-prior generations, no threshold setting, no candidate certification, no candidate selection, no ranking, no schedule v2 drafting, no schedule supersession, no true breadth rerun, no Path B readiness or execution, no Path D execution, no quantization stress, no INT8/INT4, and no Claim C activation. It proposes a model-free calibration direction and range only; any threshold-fixing or model run requires separate Manager authorization.

## 10. Language-perimeter check

```text
language-perimeter clean: YES — no Path A result-citation; schedule-layer
framing only where alluded to; no breadth claim; no forbidden phrasings as
assertions; gated terms only in the closed-gate negation (§9).
```

Closed gates carried (full named list): no model-facing execution · no model loading · no sweep_id creation · no token-prior generations · no constructed-positive generation · no seeded-defect exercise · no surplus-signature validation · no schedule v2 drafting · no schedule supersession · no true breadth rerun · no Path B readiness or execution · no Path D execution · no quantization stress · no INT8/INT4 · no candidate selection · no ranking · no threshold work · no certification evaluation · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission.

— Senior Engineer
