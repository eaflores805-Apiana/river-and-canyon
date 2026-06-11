# Inputs Package — Pre-Lock Instrument Validation Addendum (for New Senior)

From: Outgoing Senior (continuity) · To: New Senior, via Team Lead · Cc: CS, Manager · 2026-06-10
Purpose: everything needed to draft your first owned task, in one place. Nothing here adds
requirements beyond the Team Lead's instruction; it only locates sources and pins decided elements.

## 1. The task (Team Lead instruction, verbatim — this is your scope)

> "Draft a governance addendum titled 'Pre-Lock Instrument Validation Addendum.' Its purpose is to
> convert the Lane 1a instrument-discrimination findings into standing pre-lock requirements. Do not
> authorize execution, redesign Lane 1a, revise Paper 3, or propose new experiments. Focus only on
> required validation checks before any diagnostic battery or criterion can be locked."

## 2. Decided elements (do not re-litigate; incorporate verbatim)

- **Title:** Pre-Lock Instrument Validation Addendum. **Subtitle:** Battery Operating-Characteristic
  Validation for D2-Style Diagnostic Batteries.
- **Epigraph:** "Before retention, certify the task. Before certification, validate the instrument."
  (Manager; with the dependency chain: retention claims depend on certification; certification depends
  on valid instruments; valid instruments depend on pre-lock operating-characteristic checks.)
- **Structure:** exactly A / B / C as the Team Lead specified — A. Battery validation
  (pilot-manifest execution; per-policy accuracy cap; union-envelope cap; operation-equivalent /
  degenerate policy classification; "non-constant ≠ non-degenerate"); B. Criterion well-formedness
  (ideal witness passes every criterion it should; malformed-criterion definition; control semantic
  target declared at spec time; no criterion excludes ideal behavior without explicit justification);
  C. Lock process (every must-fix dispositioned before lock: incorporated / declined-with-rationale /
  deferred-with-owner; no silent carry-through). These are different failure surfaces; keep them
  separated.
- **Status on delivery:** *proposed standing addendum* — it becomes a standing rule only at Manager
  adoption (step 4 of the route). Released Paper 3 v1.1 is not touched; any later manuscript
  incorporation is a separately authorized scope decision.

## 3. Source materials (cite these; do not reconstruct from memory)

1. **Lane 1a Close-Out v1.1** (freeze candidate, sha256 `38e5f69f…`): §4 Findings A/B/C with code
   citations and supported/unsupported readings; §9 structural-rule family + doctrine pair; §10
   R1 (Pre-lock Instrument Validation Suite — your section A/B in embryo, accepted by Team Lead) and
   R6 (requirement-inheritance check); §8 P4 citation-scope guard.
2. **Team Lead C5-intake memo:** the three-component suite formulation (positive controls / ideal
   witness / degeneracy caps); malformed-criterion definition; P1–P4 record pins.
3. **Manager structure memo:** the seven-item spec your A/B/C reorganizes; the
   sensitivity-vs-specificity framing; the naming decision.
4. **Contributor memo (Lane 1a accounting):** the inheritance finding ("the cure already existed in
   v1.0's D2 battery-sensitivity text" — quote the v1.0/v1.1 D2 requirement as the addendum's ported
   ancestor, which makes your document an act of R6 compliance, worth saying explicitly); the floor
   precondition, verbatim keeper: "a floor against a 1.000 envelope is no floor."
5. **Standing rule family** for the framing paragraph: G1 (delivery must be tested), sibling
   cross-reference (agreement), production-path smoke (environment), battery discrimination
   (this addendum's subject) — your document is the fourth rule's formalization.
6. **Review-discipline standard:** every requirement you write must carry the enforcement triple —
   vehicle, owner, audit artifact — or it is wording-class by the program's own definition. ("A
   control is not structural because we describe it structurally.")

## 4. Boundaries (violating any of these is the review's first check)

No execution authorized or implied; no Lane 1a′ proposal; no Paper 3 v1.1 edits; Lane 1a cited only
per the P4 scope ("documented instrument-discrimination case study — never a certifier, model,
occupancy, or threshold-supporting result"); G1 applies to your delivery (enumerate filename, intended
path, full sha256); the route is fixed: you draft → Team Lead filters → Senior + CS review → Manager
adoption decision.

## 5. Two practical notes from this seat

(a) **Name your document's home.** Propose the intended repo path inside the addendum itself — and
flag to CS that `STANDING-REVIEW-DISCIPLINE.md`'s path was never confirmed in any return (open since
the Path A.1 review); your addendum is the natural occasion to resolve where standing rules live.
(b) **Verification habit:** when you verify your own draft's claims against repo artifacts, use
whitespace-flexible matching — soft-wrapped sources break exact-string anchors. This seat hit that
trap three times this session; consider the lesson inherited.

## 6. What the step-3 review will check (so you can pre-check)

Enforcement triple on every A/B/C requirement; the decided elements present verbatim; no authorization
language anywhere; P4-compliant Lane 1a citations; consistency with close-out R1/R6 (your document
supersedes neither — it formalizes them); the v1.0 D2 ancestor quoted; and the boundary that perfect
behavior passes (your section B is itself screened by its own ideal-witness rule: a well-formed
addendum's requirements must be satisfiable by an ideal instrument).

Good first task. It's the program's newest rule, and it should carry its newest seat's name.

— Outgoing Senior Engineer
