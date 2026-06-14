# BLOCK-E-CONSTRUCTED-POSITIVE-DESIGN-QUESTION-v0.1

**Version:** v0.1. River and Canyon program. Semantic-Read Operationalization phase, Block E.
**Status:** model-free DESIGN QUESTION only. Specifies what a constructed-positive *would need to be*; generates, executes, validates, and constructs nothing. Authorizes nothing.
Owner/drafter: Senior Engineer · CS: implementation-feasibility + artifact-identity feedback after return · Team Lead: routing, synthesis, ledger.
Ledger: SEMANTIC-READ-OPERATIONALIZATION-LEDGER-v0.2.1.md · INDEX is canonical artifact catalog.

## 0. The question

Block D established that criterion-firing evidence exists in synthetic/oracle scope while **real-candidate elimination evidence is absent** in the model-facing condition class. That asymmetry makes one question well-posed and worth designing against:

> What would a constructed positive control have to *be* — as an artifact, with what properties — to demonstrate that the instrument can eliminate a *real candidate* it should eliminate, in the condition class we care about, without that demonstration being confounded by saturation, shortcut survival, or control-channel masquerade?

This block answers that at the level of design requirements only. It is the qualitative bridge between the EMPTY window Block F found and any future proposal to build something.

## 1. What real-candidate firing would need to demonstrate

A real-candidate positive control must show the instrument attaching an **elimination** verdict to a candidate that (a) is a genuine model-facing output, not a synthetic oracle stub, and (b) *should* be eliminated on a known, pre-registered ground. The demonstration succeeds only if all three hold:

```text
1. the candidate is eliminated (verdict fires), AND
2. the elimination is attributable to the pre-registered defect the
   candidate was designed to carry — not to an unrelated failure, AND
3. a matched non-defective candidate in the same condition class is
   NOT eliminated (the contrast that proves the verdict discriminates).
```

Without (3) the design proves only that the instrument can reject *something*, not that it discriminates the defect from its absence — which is the gap between "can fire" and "is sensitive" that Block G names and the E10 guard forbids collapsing.

## 2. What artifact class would carry it

The constructed-positive is an **instrument-component artifact** (per the Block C default-flip, not inert config): a *seeded-defect candidate specification* plus its *matched clean counterpart*, both under the same sealed schedule structure, both carrying a shown semantic-read of the concept each instantiates. It is not a new model, not a new task family, not a schedule change. It is a matched candidate pair designed so the instrument's verdict on the pair is informative regardless of which way it falls.

## 3. Semantic-read properties to check before any future use

Before such an artifact could ever be used (a separate, gated step), its shown semantic-read must establish:

```text
- claimed concept: the pair instantiates exactly one controlled
  difference — the seeded defect — and nothing else (no surplus).
- the defect is the KIND the instrument claims to detect, stated in
  the real system's own terms (no analogy standing in for the mechanism).
- the clean counterpart is matched on every load-bearing dimension
  except the defect (length, position structure, null fraction,
  answer distribution) — so a verdict difference isolates the defect.
- the pair sits OFF the saturation ceiling (see §4).
- identity/error tracking is possible: same-item correspondence between
  defective and clean members, so a verdict difference is the same
  capability discriminated, not two different error sets.
```

## 4. How the design avoids the Block F saturation problem

This is the binding constraint and the design's hardest requirement. Block F found the D4 family EMPTY because it scores at ceiling (80/80) — no room for a downward signal. A constructed positive must therefore be specified to operate **inside the resolvable window** `floor < a < ceiling − δ`, not at it:

```text
- the candidate pair must be calibrated (at DESIGN level — values left to a
  future, gated step) so the clean member sits below the saturation ceiling
  with resolvable room, and the defective member is expected to fall to a
  distinguishable lower band.
- the design must state the off-ceiling target as a load-bearing semantic-read
  parameter — i.e. "this artifact is only valid if the clean member is
  non-saturated" is part of what the read checks, not an afterthought.
- a pair that saturates is, by this design rule, a FAILED constructed positive
  regardless of whether the verdict fired — because saturation makes the
  verdict uninterpretable (Block G failure-class: saturation masking).
```

This is the precise inversion of the D4 problem: D4 failed certification *because* it was at ceiling; the constructed positive is defined as the thing engineered to live where D4 cannot.

## 5. How the design distinguishes the three firing types

The whole value of the design is keeping three things that look alike apart:

```text
synthetic/oracle criterion-firing  — the verdict fires on an oracle STUB
   (what Block D Layer-1 already shows; 12/12). Establishes the code path
   works on designed inputs. NOT real-candidate evidence.
real-candidate elimination          — the verdict fires on a genuine
   model-facing candidate carrying a pre-registered defect, AND the matched
   clean candidate is not eliminated. This is the gap Block E targets.
control-channel elimination         — the verdict fires on a no-bindings
   shell designed to fail (the TP control; D4-B 0.0125). Measures the control
   machinery, not a candidate. Per E14, non-upgradeable; the design must
   never let a control-channel firing be read as real-candidate evidence.
```

The design's discrimination test: a constructed positive is only real-candidate evidence if its firing survives removal of both the oracle-stub interpretation (it's a real generated candidate) and the control-channel interpretation (it has real bindings, not a designed-to-fail shell).

## 6. Disposition

```text
DISPOSITION: CONDITIONAL
```

A coherent constructed-positive design path **does** exist at the design level — §§1–5 specify it without contradiction — but it depends on missing preconditions that must be resolved before any proposal could route:

```text
C1. the off-ceiling calibration (§4) is specified as a requirement but its
    feasibility against a real model is unverified — it depends on whether a
    non-saturated clean candidate in this condition class can be constructed
    at all, which is itself a (gated) empirical question.
C2. the matched-pair construction (§3) requires a clean counterpart matched on
    all load-bearing dimensions; whether such a match exists for the seeded
    defect is unverified at design time.
C3. the Block B standing semantic-read template is not yet filed; the recursive
    semantic-reads this design requires (§3) should run against the standing
    template, not a borrowed §6 form, before any construction.
```

CONDITIONAL, not FEASIBLE, because FEASIBLE would assert the path is coherent *and* its preconditions met; C1–C3 are real and unmet. CONDITIONAL, not INFEASIBLE, because the path is not incoherent — it is well-defined and blocked only on resolvable preconditions. This is the honest reading: the design question has a good answer, and that answer names what must be true before the answer can be used.

## 7. What remains blocked even if a future design were FEASIBLE

```text
- generating the constructed positive (no constructed-positive generation)
- seeding the defect (no seeded-defect exercise)
- validating any surplus signature (no surplus-signature validation)
- running any model (no model execution / loading)
- any threshold, certification, candidate selection, or ranking
- Claim C activation
Everything in §§1–5 is a SPECIFICATION of an artifact, not the artifact.
Building it is a separate Manager authorization.
```

## 8. Plant-parameter list (each flagged for its own recursive semantic-read)

```text
- the seeded defect's identity and mechanism      → semantic-read required
- the matched-clean counterpart's match dimensions → semantic-read required
- the off-ceiling calibration target               → semantic-read required
- the elimination ground (why the defect should be caught) → semantic-read required
- the discrimination contrast (clean-not-eliminated) → semantic-read required
```

Each is a place where a concept could be claimed but not instantiated — the Path A failure mode — so none may be trusted on its name; each requires a shown read before any future use. "can fire" ≠ "is sensitive."

## 9. Non-authorization footer

NON-AUTHORIZATION FOOTER — BLOCK E

This design authorizes no constructed-positive generation, no seeded-defect exercise, no surplus-signature validation, no model execution, no suite execution, no threshold setting, no candidate certification, no candidate selection, no schedule v2 drafting, no quantization stress, no INT8/INT4, and no Claim C activation.

It is a design question only. Any future construction, generation, validation, or execution requires separate Manager authorization.

## 10. Required-return checklist

```text
1. artifact: BLOCK-E-CONSTRUCTED-POSITIVE-DESIGN-QUESTION-v0.1.md
2. disposition: CONDITIONAL (path coherent; preconditions C1–C3 unmet) §6
3. path/commit/sha256: on filing (CS verifies)
4. INDEX row: added this filing
5. non-authorization block carried: YES §9
6. language-perimeter clean: YES — Path A cited only as "(rung-uniform)" /
   schedule-layer finding; no breadth claim; no forbidden phrasings; firing
   types kept distinct; "Claim C" appears only in the closed-gate negation
```

Closed gates carried (full named list): no model-facing execution · no model loading · no sweep_id creation · no token-prior generations · no constructed-positive generation · no seeded-defect exercise · no surplus-signature validation · no schedule v2 drafting · no schedule supersession · no true breadth rerun · no Path B readiness or execution · no Path D execution · no quantization stress · no INT8/INT4 · no candidate selection · no ranking · no threshold work · no certification evaluation · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission.

— Senior Engineer
