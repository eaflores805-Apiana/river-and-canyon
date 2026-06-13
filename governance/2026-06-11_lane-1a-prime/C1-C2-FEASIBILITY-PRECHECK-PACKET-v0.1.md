# C1-C2-FEASIBILITY-PRECHECK-PACKET-v0.1

**Version:** v0.1. River and Canyon program. Semantic-Read Operationalization phase (Block E precondition work).
**Status:** model-free desk packet. Evaluates whether the two remaining Block E blockers are *checkable on paper*, not whether they pass. Constructs, generates, executes, and validates nothing. Authorizes nothing.
Owner/drafter: Senior Engineer · CS: artifact-identity + guard verification after return · Team Lead: routing, synthesis, ledger.
Ledger: SEMANTIC-READ-OPERATIONALIZATION-LEDGER-v0.2.1.md · INDEX is canonical artifact catalog.

## 0. The distinction this packet rests on

Block E returned CONDITIONAL on three preconditions. C3 (standing template unfiled) is now CLOSED — the template `SHOWN-SEMANTIC-READ-TEMPLATE-v1.0.md` is filed and verified. C1 and C2 remain OPEN. This packet does not try to *resolve* C1/C2; it asks the prior, cheaper question:

> Can C1 and C2 be evaluated cleanly on paper, model-free, before any constructed-positive proposal routes — and if not fully, what is the smallest next desk action?

"Checkable" and "true" are different questions. A blocker can be paper-checkable (we can decide it with artifacts in hand) or not (deciding it needs a model run, hence a gate). Sorting C1 and C2 into those bins is the whole job here.

## 1. C1 — off-ceiling feasibility: what it means without thresholds

C1 asks whether an off-ceiling clean candidate *can exist* in the relevant condition class. Stated without setting any threshold:

```text
C1 is the question of whether the condition class admits a clean candidate
whose accuracy sits strictly inside the resolvable window (above the shortcut
floor, below the saturation ceiling by resolvable room) rather than at the
ceiling — expressed as an existence question, not a target value.
```

What C1 is **not**: it is not "what accuracy should the candidate hit" (that is threshold work, closed). It is "does the class even contain a non-saturated clean point, or is this family structurally driven to ceiling?"

**Is C1 paper-checkable with existing artifacts?** Partially, and the partial line is sharp:
- *On paper now (model-free):* we can inspect whether the D4 family's saturation is a property of the *task construction* (item difficulty, answer availability, null fraction) or merely of the *one candidate scored*. The run-of-record artifacts (the schedule, the manifests, the per-policy envelope) carry the construction; a desk read can establish whether the construction *permits* a harder, non-saturated variant in principle.
- *Not on paper (would need a gate):* whether a specific constructed variant *actually* lands off-ceiling against a real model is an empirical fact that only a model run could settle — and that run is closed.

So C1 splits: the **existence-in-principle** sub-question is paper-checkable; the **realized-off-ceiling** sub-question is not.

## 2. C2 — matched-clean counterpart: what it requires structurally

C2 asks whether a matched clean counterpart can exist for a seeded-defect candidate. Structurally, a valid matched pair requires:

```text
- the two members differ in EXACTLY ONE controlled dimension — the seeded
  defect — and are matched on every other load-bearing dimension
  (length, position structure, null fraction, answer distribution,
  surface form), so a verdict difference isolates the defect.
- the match is itself shown by a semantic-read (the pair instantiates one
  controlled difference and no surplus), per the standing template.
```

**Is C2 paper-checkable with existing artifacts?** Largely yes, and more cleanly than C1:
- *On paper now:* whether a matched-pair *construction is definable* — whether the dimensions that must be matched can be enumerated and whether the existing schedule/manifest structure exposes them as controllable — is a desk question, answerable against the artifacts in hand. The Block C audit already showed these artifacts are instrument-components with readable structure.
- *Not on paper:* whether a *specific* seeded defect produces a verdict difference against a real model is empirical (gated). But C2 as a *design-existence* question — can such a pair be specified at all — is paper-checkable.

## 3. Existing artifacts vs new artifacts

```text
C1 existence-in-principle:  checkable against EXISTING artifacts (schedule,
   manifests, per-policy envelope, candidate summary). No new artifact needed
   for the paper sub-question.
C2 design-existence:        checkable against EXISTING artifacts (the same
   instrument-component set, read for controllable match dimensions). No new
   artifact needed for the paper sub-question.
Both realized sub-questions: would require a NEW constructed artifact AND a
   model run to settle — both gated, neither in scope here.
```

Any new artifact introduced later (a candidate-pair specification) would itself need a shown semantic-read against the standing template **before** any use — the default-flip applies; a pair spec is an instrument-component, not inert config. This is required consideration #5, answered: yes, a future new artifact reads first.

## 4. Can the precheck be model-free? Where does authorization enter?

```text
The PRECHECK (this packet, and the paper sub-questions it identifies):
   fully model-free. No model, no run, no generation.
The RESOLUTION of C1/C2's realized sub-questions:
   not model-free — requires constructing a candidate (gated:
   no constructed-positive generation) and running it (gated:
   no model execution). Manager authorization required BEFORE that point.
```

So the boundary is clean: the desk can carry C1/C2 up to "existence-in-principle established or refuted," and no further without a gate.

## 5. Why filing the template closed C3 only, not C1 or C2

Required consideration #8, stated plainly: C3 was a *process-artifact* gap — the standing form did not exist, so it could be closed by *drafting the form*, which is pure desk work. C1 and C2 are *empirical-existence* questions about the task class and a candidate pair — their full resolution depends on facts about how a real model behaves on real constructed inputs, which a document cannot supply. Filing a template creates a tool; it does not create a non-saturated candidate or a matched pair. C3 was closeable by writing; C1/C2 are not. Conflating them would be the "no mountain in the sentence" error — treating an empirical question as if it were a documentation task because both wore the label "precondition."

## 6. Disposition

```text
DISPOSITION: CONDITIONAL
```

The precheck itself is FEASIBLE as desk work — both C1 and C2 have paper-checkable sub-questions answerable against existing artifacts model-free. But the *overall* C1/C2 resolution is CONDITIONAL, because each splits into a paper-checkable existence-in-principle part (in scope, model-free) and a realized part that requires construction + a model run (gated, out of scope). The honest disposition is CONDITIONAL: the desk can advance C1/C2 to "is a non-saturated clean point / matched pair definable in principle?" and must stop at the gate before "does it realize against a model?"

## 7. Smallest next desk action (recommendation only)

```text
A single model-free desk read, against existing artifacts only:
  "Does the D4 condition-class construction PERMIT a non-saturated clean
   variant and a one-dimension-matched pair to be SPECIFIED — yes/no — by
   inspecting the schedule, manifests, and per-policy envelope already in hand?"
If yes  → C1/C2 existence-in-principle is established on paper; a
          constructed-positive PROPOSAL (separate Manager authorization)
          becomes the next ask, carrying the realized sub-questions as its
          gated content.
If no   → the family is structurally saturated; the design must change class
          or the route reconsiders — a "do not drive this family" finding,
          delivered on paper for free.
This action creates no artifact requiring construction; it is a read of
existing bytes and returns a yes/no with shown evidence.
```

## 8. No-authorization footer

This feasibility-precheck authorizes no constructed-positive generation, no seeded-defect exercise, no candidate generation, no model execution, no model loading, no sweep_id creation, no token-prior generations, no threshold setting, no candidate certification, no candidate selection, no ranking, no schedule v2 drafting, no schedule supersession, no true breadth rerun, no Path B readiness or execution, no Path D execution, no quantization stress, no INT8/INT4, no Claim C activation, no public benchmark packaging, no funder-facing release, no SBIR submission. It is a desk evaluation of checkability only; any construction, generation, or model run requires separate Manager authorization.

## 9. Required-return checklist

```text
1. artifact: C1-C2-FEASIBILITY-PRECHECK-PACKET-v0.1.md
2. disposition: CONDITIONAL (precheck FEASIBLE as desk work; C1/C2 each split
   into paper-checkable existence-in-principle + gated realized sub-question) §6
3. path/commit/sha256: on filing (CS verifies)
4. INDEX row: added this filing
5. no-authorization footer carried: YES §8
6. language-perimeter clean: YES — Path A cited as "(rung-uniform)" /
   schedule-layer finding; breadth-untested framing used; no forbidden
   phrasings; "Claim C" appears only in the closed-gate negation
```

Closed gates carried (full named list): no model-facing execution · no model loading · no sweep_id creation · no token-prior generations · no constructed-positive generation · no seeded-defect exercise · no surplus-signature validation · no schedule v2 drafting · no schedule supersession · no true breadth rerun · no Path B readiness or execution · no Path D execution · no quantization stress · no INT8/INT4 · no candidate selection · no ranking · no threshold work · no certification evaluation · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission.

— Senior Engineer
