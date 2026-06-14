# CONSTRUCTED-POSITIVE-PROPOSAL-PACKET-v0.1

**Version:** v0.1. River and Canyon program. Semantic-Read Operationalization phase.
**Status:** model-free PROPOSAL packet. Specifies a constructed-positive *design*; constructs, generates, validates, and runs nothing. Authorizes nothing. Routing this packet, if accepted, authorizes only a separate future construction/generation decision — not construction itself.
Owner/drafter: Senior Engineer · CS: artifact-identity + guard verification after return · Team Lead: routing, synthesis, ledger.
Ledger: SEMANTIC-READ-OPERATIONALIZATION-LEDGER-v0.2.1.md · INDEX is canonical artifact catalog.

## 0. What this packet proposes

The C1/C2 desk read (v0.2, CS-verified) established that the D4 family's construction permits a non-saturated clean variant and a one-dimension-matched pair to be specified in principle, via four exposed levers: **list length, queried-key position, key/value vocabulary, key uniqueness/ambiguity.** This packet proposes a *design* that uses those levers to build a positive control capable of testing real-candidate elimination. It specifies the design; it does not build it. Every realization step stays gated (§9).

The design must satisfy the demonstration requirement from Block E: a real-candidate positive control succeeds only if (a) a defective candidate is eliminated, (b) the elimination is attributable to the pre-registered defect, and (c) a matched clean candidate is **not** eliminated — the contrast that separates "can fire" from "is sensitive."

## 1. Proposed off-ceiling design strategy

The D4 pilot saturates at 80/80 because its settings are easy (5 short pairs, unique keys, a model that solves them all). The proposed strategy moves the *clean* member off ceiling by increasing task load along the exposed levers, at design level only (no target values set — that is gated threshold work):

```text
- increase list length beyond the pilot's 5 pairs, raising retrieval load;
- bias queried-key position toward the harder interior/late slots rather than
  the easy distribution; position is already an exposed, varied dimension;
- optionally introduce key-ambiguity (the multi-occurrence stratum the desk
  read found at 12/80) as a controlled difficulty source.
Goal (qualitative): place the clean member's accuracy strictly inside the
resolvable window  floor < a < ceiling − δ  rather than at the ceiling, so a
defect-induced drop has room to be observed. Whether any specific setting
realizes off-ceiling is the gated empirical question.
```

## 2. Proposed matched clean/defective pair structure

```text
The pair is two candidate sets generated from the SAME construction settings,
differing in exactly one controlled dimension:
  CLEAN member:     non-saturated lookup as in §1; the queried key is present
                    and unambiguously answerable.
  DEFECTIVE member: identical in every load-bearing dimension EXCEPT the single
                    seeded defect (§4); designed so a correct instrument should
                    eliminate it while leaving the clean member standing.
Both members carry identical list length, position distribution, vocabulary
family, null fraction, and surface format. The ONLY intended difference is the
defect axis.
```

## 3. Load-bearing dimensions to hold constant

For a verdict difference to isolate the defect, the pair must match on every dimension that could otherwise explain a difference:

```text
- list length (pairs per item)
- queried-key position distribution
- key/value vocabulary family and token-length profile
- null/answerable stratum fractions
- surface format ("N -> token" rendering, whitespace, query phrasing)
- item count and scoring harness
Any unmatched load-bearing dimension is a confound that would let a verdict
difference be attributed to something other than the defect — a FAILED pair
by design, regardless of how the verdict falls.
```

## 4. Single controlled defect / difference

```text
The defect is ONE pre-registered, semantically-named corruption of the
answerability of the defective member — e.g. the queried key's value is made
unrecoverable from the listed pairs (the answer is not constructible from the
context) while the surface form still looks answerable.
The defect must be:
  - singular (one controlled axis; no surplus second difference);
  - pre-registered (named before any construction, with the ground on which
    the instrument SHOULD eliminate it stated in advance);
  - stated in the task's own terms (no analogy standing in for the mechanism).
A correct instrument eliminates the defective member BECAUSE the answer is not
constructible, and leaves the clean member standing BECAUSE its answer is.
```

## 5. Required shown semantic-reads before any future use

Each of the following is an instrument-component (per the Block C default-flip) and must pass a `SHOWN-SEMANTIC-READ-TEMPLATE-v1.0` read BEFORE any construction or use:

```text
- the clean-member specification (claims: non-saturated, answerable, no surplus)
- the defective-member specification (claims: one defect, matched otherwise)
- the defect definition (claims: singular, pre-registered, real-terms)
- the match manifest (claims: all load-bearing dimensions held constant)
- the off-ceiling calibration setting (claims: lands in the resolvable window)
- the elimination ground (claims: why a correct instrument catches the defect)
None may be trusted on its name. A read that cannot show observed structure
satisfying required structure is HOLD — this is the Path A guard applied to the
positive control's own parts.
```

## 6. How the proposal avoids D4 saturation

Directly, and as a design invariant rather than an afterthought: the clean member is *defined* as non-saturated — "lands in the resolvable window" is a load-bearing claim its semantic-read must establish (§5), and a clean member that saturates is a FAILED construction regardless of any verdict (Block G failure-class: saturation masking). This inverts the D4 pilot's defect: D4 failed certification *because* it was at ceiling; the proposed clean member is the artifact engineered to live where D4 could not. Block F's EMPTY window is the premise this design exists to escape.

## 7. How the proposal distinguishes the three firing types

```text
oracle/synthetic criterion-firing — verdict fires on a designed oracle STUB.
  Already shown (Block D Layer-1, 12/12). The proposed pair is NOT a stub: it
  is a real generated candidate set, so a firing here is not oracle-firing.
control-channel elimination — verdict fires on a no-bindings shell designed to
  fail (the TP control, D4-B 0.0125, non-upgradeable per E14). The defective
  member is NOT a designed-to-fail shell: it has real bindings and differs from
  the clean member by one defect only, so its elimination is not control-channel.
real-candidate elimination — verdict fires on the DEFECTIVE member AND spares
  the matched CLEAN member. This is the only outcome the design counts as
  real-candidate evidence, and it is well-defined precisely because the pair
  rules out the other two interpretations by construction.
Discrimination test: the design yields real-candidate evidence only if the
defective-member firing survives removal of both the oracle-stub reading (it is
a real candidate) and the control-channel reading (it has real bindings), AND
the clean member is not also eliminated.
```

## 8. Disposition

```text
DISPOSITION: CONDITIONAL
```

A coherent constructed-positive design path exists and is specified above without contradiction — so this is not NOT-READY. But it is not yet PROPOSAL-READY in the strong sense of "route to Manager for construction authorization with nothing further to resolve," because three prerequisites remain that are design-resolvable but not yet resolved:

```text
P1. off-ceiling calibration is specified as a requirement but no calibration
    setting has been desk-derived even at design level; the smallest next desk
    action (a model-free derivation of candidate load settings expected to land
    off ceiling, stated as a range, no model run) would clear it.
P2. the defect's pre-registration is specified in form but not yet written as a
    concrete, named defect with its elimination ground; this is a desk artifact
    that must exist and pass its own semantic-read before construction.
P3. the match manifest (the list of held-constant dimensions with their
    intended values) is specified in kind but not yet instantiated as a
    checkable document.
```

CONDITIONAL is the honest reading: the design is coherent and the path is real, and what remains are named, model-free, desk-resolvable prerequisites — not empirical unknowns and not incoherence. Clearing P1–P3 (all desk work, all gated short of construction) would move this to PROPOSAL-READY.

Note on routing semantics, for the Manager's decision: even a PROPOSAL-READY disposition would authorize only a *construction decision*, never construction. CONDITIONAL means the team should clear P1–P3 on paper first, then route a v0.2 as PROPOSAL-READY.

## 9. What remains gated even if the proposal is accepted

```text
- generating the clean or defective member         (no constructed-positive generation)
- seeding the defect                               (no seeded-defect exercise)
- any candidate generation                         (no candidate generation)
- running any member against a model               (no model execution / loading)
- confirming off-ceiling realization               (empirical; gated)
- confirming the verdict discriminates             (empirical; gated)
- any threshold, certification, selection, ranking, surplus-signature validation
- schedule v2, supersession, Path B/D, quantization, INT8/INT4, Claim C activation
Acceptance of this PROPOSAL authorizes, at most, the next desk steps (P1–P3)
and a subsequent separate construction-authorization decision. It never
authorizes construction itself.
```

## 10. Non-authorization footer

NON-AUTHORIZATION FOOTER

This proposal packet authorizes no constructed-positive generation, no seeded-defect exercise, no candidate generation, no model execution, no model loading, no sweep_id creation, no token-prior generations, no threshold setting, no candidate certification, no candidate selection, no ranking, no schedule v2 drafting, no schedule supersession, no true breadth rerun, no Path B readiness or execution, no Path D execution, no quantization stress, no INT8/INT4, and no Claim C activation.

It is a proposal packet only. Any construction, generation, validation, or model run requires separate Manager authorization.

## 11. Required-return checklist

```text
1. artifact: CONSTRUCTED-POSITIVE-PROPOSAL-PACKET-v0.1.md
2. disposition: CONDITIONAL (path coherent; desk prerequisites P1–P3 unresolved) §8
3. path/commit/sha256: on filing (CS verifies)
4. INDEX row: added this filing
5. no-authorization footer carried: YES §10
6. language-perimeter clean: YES — Path A cited as "(rung-uniform)" /
   schedule-layer finding only; no breadth claim; no forbidden phrasings present anywhere as assertions;
   run-readiness language avoided; the only mentions of gated terms are in
   closed-gate negations
```

Closed gates carried (full named list): no model-facing execution · no model loading · no sweep_id creation · no token-prior generations · no constructed-positive generation · no seeded-defect exercise · no surplus-signature validation · no schedule v2 drafting · no schedule supersession · no true breadth rerun · no Path B readiness or execution · no Path D execution · no quantization stress · no INT8/INT4 · no candidate selection · no ranking · no threshold work · no certification evaluation · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission.

— Senior Engineer
