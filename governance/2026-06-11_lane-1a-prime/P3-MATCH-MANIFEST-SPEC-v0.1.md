# P3-MATCH-MANIFEST-SPEC-v0.1

**Version:** v0.1. River and Canyon program. Semantic-Read Operationalization phase (constructed-positive readiness, P3).
**Status:** model-free desk artifact. Specifies a match manifest; constructs and generates nothing. Authorizes nothing.
Owner/drafter: Senior Engineer · CS: identity + guard verification · Team Lead: routing, ledger.
Ledger: SEMANTIC-READ-OPERATIONALIZATION-LEDGER-v0.2.1.md · INDEX is canonical artifact catalog.

## 1. Artifact identity

P3-MATCH-MANIFEST-SPEC-v0.1.md — third of three desk prerequisites (P2→P1→P3). Instantiated last because it references both the defect (P2) and the calibration setting (P1). States what must be identical between the clean and defective members so the only difference is the P2 defect.

## 2. Purpose

State what must be held identical between the clean member and the defective member so that the **only** difference between them is the single P2 defect (queried key's value not constructible). Any unmatched load-bearing dimension would be a confound that lets a future verdict difference be attributed to something other than the defect.

## 3. Claimed concept

> For every load-bearing dimension except the P2 defect axis, the clean and defective members are constructed from identical settings, so a verdict difference between them isolates the defect.

## 4. The match manifest (dimensions held constant)

Each dimension below must be identical across the pair, at the P1-proposed off-ceiling load setting:

```text
dimension                  held-constant requirement
-------------------------  ----------------------------------------------------
list length                same number of pairs per item (P1 off-ceiling band),
                           identical between members
queried-key position dist  same distribution of where the queried key sits;
                           the defective member's "queried key" slot structure
                           mirrors the clean member's (the difference is
                           PRESENCE of the value, not position)
key/value vocabulary family same token vocabulary and sampling for keys and
                           values across both members
token-length profile       same key/value token-length distribution; no length
                           tell that distinguishes defective from clean
null/answerable stratum     same fraction of null vs answerable items; the
                           defect lives inside the answerable stratum, not by
                           shifting stratum proportions
surface format             identical rendering ("N -> token", whitespace, Query
                           line phrasing); no formatting tell
item count                 same N per member, so scoring power is matched
scoring harness            identical scorer, parser, and abstention handling
                           applied to both members
```

## 5. The single permitted difference

```text
PERMITTED difference (exactly one):
  the P2 defect — in the defective member, the queried key is ABSENT from the
  listed pairs (value not constructible); in the clean member, the queried key
  is PRESENT and uniquely answerable.
EVERYTHING ELSE in §4 is identical.
```

This is the design's whole validity: matched on §4, differing only on §5, a future verdict difference (defective eliminated, clean spared) isolates the defect — which is the real-candidate-elimination evidence the constructed positive exists to produce.

## 6. Interaction checks with P1 and P2 (consistency)

```text
- vs P2: the defect axis (§5) is exactly P2's single defect; no second defect
  is introduced by any §4 dimension.
- vs P1: the off-ceiling calibration (length, position) is applied IDENTICALLY
  to both members, so calibration raises difficulty without becoming a
  difference between them. P1's bounded-ambiguity caution is honored: key
  uniqueness is a §4 held-constant dimension here (both members same), so
  ambiguity is not a lurking second difference.
- the manifest is internally consistent with both prior artifacts; no dimension
  in §4 collides with the defect or the calibration.
```

## 7. Shown semantic-read of this artifact's own load-bearing claim

```text
1. artifact:            P3-MATCH-MANIFEST-SPEC-v0.1.md
2. path:                semantic-read-operationalization/P3-MATCH-MANIFEST-SPEC-v0.1.md
3. commit:              this filing (CS verifies)
4. sha256:              on filing (CS verifies)
5. claimed concept:     every load-bearing dimension except the P2 defect is
                        held identical across the pair, so a verdict difference
                        isolates the defect.
6. check performed:     enumerated the load-bearing dimensions from the D4 item
                        structure (C1/C2 desk read v0.2) and the constructed-
                        positive proposal's §3 list; confirmed each is present in
                        §4 as held-constant; confirmed the only permitted
                        difference (§5) is exactly P2's defect and nothing else;
                        cross-checked against P1 so calibration applies equally.
7. observed structure:  §4 covers all eight load-bearing dimensions named in the
                        routing plus scorer/parser; §5 admits exactly one
                        difference; §6 shows no collision with P1/P2.
8. required structure:  a match manifest must hold ALL load-bearing dimensions
                        constant and admit exactly ONE difference (the defect).
9. surplus check:       ABSENT — no uncontrolled second difference; the manifest
                        is exhaustive over the named dimensions and closes the
                        confound surface.
10. disposition:        PASS — observed structure satisfies required structure.
— non-authorization footer (below) —
```

## 8. Disposition

```text
DISPOSITION: PASS
```

The match manifest holds every load-bearing dimension constant, admits exactly one difference (the P2 defect), and is consistent with P1's calibration and P2's defect. It is a desk specification only.

## 9. No-authorization footer

This match manifest spec authorizes no constructed-positive generation, no seeded-defect exercise, no candidate generation, no model execution, no model loading, no sweep_id creation, no token-prior generations, no threshold setting, no candidate certification, no candidate selection, no ranking, no schedule v2 drafting, no schedule supersession, no true breadth rerun, no Path B readiness or execution, no Path D execution, no quantization stress, no INT8/INT4, and no Claim C activation. It specifies a match manifest in writing only; any construction or model run requires separate Manager authorization.

## 10. Language-perimeter check

```text
language-perimeter clean: YES — no Path A result-citation; schedule-layer
framing only where alluded to; no breadth claim; no forbidden phrasings as
assertions; gated terms only in the closed-gate negation (§9).
```

Closed gates carried (full named list): no model-facing execution · no model loading · no sweep_id creation · no token-prior generations · no constructed-positive generation · no seeded-defect exercise · no surplus-signature validation · no schedule v2 drafting · no schedule supersession · no true breadth rerun · no Path B readiness or execution · no Path D execution · no quantization stress · no INT8/INT4 · no candidate selection · no ranking · no threshold work · no certification evaluation · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission.

— Senior Engineer
