# TARGET-CONSTRUCT-DEFINITION-v0.1

**E. A. Flores**, Apiana AI, Inc. — June 15, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. Gate-before-construction object.*

> **What this is.** A rule surface defining what counts as **"composing, not endpoint-grabbing,"** to be satisfied *before* anyone designs task items, writes prompts, sets a regime, or authorizes a run. It defines the bar a construction must clear to qualify as a certified-constructible FP16 baseline. **It certifies nothing, authorizes nothing, and is not a paper.**
>
> **Negative-use tag.** This object is a definition, not evidence. It is not evidence for a baseline, a model capability, a compression result, or Claim C. Citing it as evidence of any of those is a misuse.

---

## 0. Scope

In scope: response-category definitions, the validity gating of *correct-composition*, the admissibility conditions a construction must meet, the metric rule, and the slots that must be pre-declared before any run.

Out of scope (absent by instruction): task items, prompt set, run plan, pre-registration values, compression comparison, new sweep, model-execution request. Where a rule carries a construction-design consequence — notably terminal ≠ answer (R8) — the *property* is stated and the *realization* (chain length, layout, entity choice) is deferred to construction design. This object stops at the property line.

## 1. Substrate and notation

Closed-world, in-context two-hop relational composition: the facts are given in the prompt, then queried. Parametric recall is neither assumed nor required.

- Chain: head **A** —(r1)→ bridge **B** —(r2)→ target **C\*** (the correct composite answer).
- **Composite query** — apply r2∘r1 to A; correct response = C\*.
- **Component (control) queries** — hop1 = r1-of-A → B; hop2 = r2-of-B → C\*.
- **Terminal** — the salient endpoint entity of a presented chain (target or decoy): the token a recency/salience heuristic returns *without* following relations.
- **Decoy chains** — competing chains presented as clutter; their endpoints are **decoy terminals**.

## 2. Response categories (R1–R6) — the primary scorer

Every response is classified into exactly one category by a rule over the response token and the item's known entity set {C\*, B, target-terminal, decoy-terminals}. Categories are mutually exclusive and exhaustive.

- **R1 — correct-composition.** Response = C\*, **and** the item's controls pass (R7), **and** the exclusions (R6) are clear. Recorded as *behavior consistent with composition under controls* — never as proof the model composed (see R6 closing rule).
- **R2 — target-terminal-grab.** Response = the target chain's terminal. By construction (R8) this is a wrong answer. Positive evidence of terminal attraction on the target chain.
- **R3 — stopped-short.** Response = the intermediate B (hop1 result), not C\*. A partial traversal that halts at the bridge. Distinct from grabbing: hop1 landed, hop2-in-composition did not.
- **R4 — decoy-terminal-grab.** Response = a non-target chain's terminal. Wrong chain and wrong position; shows the salience pull is not even chain-localized.
- **R5 — abstain.** No entity commitment: refusal, "cannot determine," hedge, null, or empty. Not correct, but not a wrong-entity commitment either.
- **R6cat — other.** Any response matching none of the above (off-distribution token, malformed, an entity not present). A real bucket, not a dump: a high *other* rate is itself a signal the construction or scorer is mis-specified.

## 3. Validity gating of correct-composition

### R6 — what makes a composite-correct response INVALID as evidence of composition

A response equal to C\* does **not** count as R1 if any of the following hold; on any such item the response is reclassified as *uninterpretable / contaminated*, not as correct-composition:

- **(a) Terminal coincidence not excluded.** C\* equals, or is selectable as, any terminal present in the item (violates R8). If a salient-endpoint grab can produce C\*, R1 and terminal-grab are indistinguishable — the item is contaminated.
- **(b) Components not independently available.** The item's hop1/hop2 controls did not pass (R7). You cannot credit composing facts the model cannot retrieve.
- **(c) Direct A→C shortcut not excluded.** If C\* is predictable from A alone (initial→terminal association / co-occurrence), composite-correct may be one-hop direct recall, not two-hop traversal. The construction must make C\* not directly associable with A.
- **(d) Interior target independently guessable.** If C\* is the single most-salient/most-frequent candidate regardless of the relation path, a non-relational heuristic yields it without traversal.
- **(e) Underpowered.** A correct rate not distinguishable from the relevant heuristic/chance baseline (R11) is not evidence.

**Closing rule (the line we hold).** Even with (a)–(e) cleared, R1 is the *best-supported interpretation*, not a proof. Behavioral data cannot fully witness composition; some residual heuristic is always logically consistent with the right token. The construct's job is to **exclude the most-available shortcut (terminal-grab) by construction, gate on component availability, and name the residual** — yielding a **validity** statement ("behavior consistent with composition, under controls, with terminal-grab and direct-shortcut excluded"), never a **capability** statement about the model.

### R7 — controls required before composite success is interpretable

Per item, before any R1 on that item is interpretable:

- **hop1 control** — model returns B when asked r1-of-A directly (same closed-world context). The first fact is available.
- **hop2 control** — model returns C\* when asked r2-of-B directly (given B). The second fact is available. (Because terminal ≠ answer, hop2 targets the interior C\*, not a terminal.)
- Both controls are **validity floors, not capability claims.** Ceiling controls mean "components are retrievable, so a composite failure is a *composition* failure, not a missing-fact failure" — not "the model is good at retrieval."
- If either control fails for an item, R1 on that item is uninterpretable → excluded from the composition numerator and logged separately.
- Controls are reported **per item**, never collapsed into one pass/fail that hides which items had available components.

## 4. Admissibility — terminal ≠ answer (R8)

The load-bearing structural requirement. A construction is **inadmissible by inspection** unless:

- **R8.1** — the correct composite answer C\* is **not** any terminal present in the item (not the target chain's terminal, not any decoy terminal); every salient endpoint maps to a *wrong* answer, so any terminal-grab is scoreable as an error (R2/R4) and can never be misread as correct.
- **R8.2** — C\*, B, the target-terminal, and all decoy-terminals are **pairwise-distinct tokens** (no aliasing), so every response maps to exactly one category in R1–R6cat.
- **R8.3** — the construction admits all six categories as distinguishable outcomes; if any two categories cannot be separated in the output, the construct is unmeasurable and the construction is rejected.

R8 is *why* prior baselines were unmeasurable: when a terminal-grab can produce the correct answer, R1 and R2 collapse and the gate cannot open on linkage. Realizing R8 may require chain structure beyond a bare A→B→C (e.g., the two-hop target placed at a non-terminal position) — but the specific realization is construction design and is **out of scope here**. This object asserts only the property.

## 5. Metric rule (R9, R10)

- **R9 — binary accuracy cannot be the primary metric.** Binary correct/incorrect collapses the distinctions that carry the signal: it lumps R1 with terminal-coincidence-correct (when not excluded) and merges R2/R3/R4/R5 into one "wrong" bucket, erasing the diagnostic difference between *didn't traverse* (grab) and *traversed one hop* (stopped-short). Binary accuracy is also the metric under which prior baselines passed via terminal coincidence. The failure mode is invisible to it by construction.
- **R10 — the R1–R6cat multiclass scorer is primary.** Category boundaries are fixed before any run (lock-before-look). Binary accuracy may exist only as a derived summary and must never gate interpretation.

## 6. Pre-declaration required before any run (R11)

Locked before look, as a single pre-registered block (values set at construction/pre-registration time, not here):

- **k / clutter regime** — number of competing chains and how clutter is set, justified against the sweep (R12): not lone-chain/minimal.
- **target-terminal position** — early/late, declared, since position gates the effect and direction flips with k.
- **n / power rationale** — sample size and the calculation behind it; n must distinguish the R1 rate from the relevant heuristic baseline (the terminal-grab chance rate), not a probe-sized n.
- **success threshold** — the pre-declared R1 rate (controls passing, R6 exclusions clear) that would count as "this construction elicits composition," i.e., qualifies as a certified-constructible baseline. A number, before the run.
- **inconclusive threshold** — the band that neither certifies nor refutes, declared so *inconclusive* is a pre-committed outcome, not a retrospective hedge.
- **failure signatures** — the pre-declared patterns that mean the gate failed, each mapped to a diagnosis: R2 dominant (target-terminal attraction), R4 dominant (cross-chain salience), R3 dominant (hop2-in-composition failure), R5 dominant (abstention regime), control floor not met (missing-fact, not composition), or R1 indistinguishable from terminal coincidence (R8 breach / contamination).
- **three-outcome decision rule** — certify / inconclusive / fail, mapping the thresholds above to a disposition, declared in advance.

## 7. Constraints carried from the terminal-attraction sweep (R12)

- **R12.1** — lone-chain / minimal constructions can *maximize* endpoint attraction; minimal is the dirtiest baseline, not the cleanest. → R11 (declare a clutter regime, not minimal).
- **R12.2** — clutter can *reduce* target-terminal attraction, but a fall in grabbing is **not** a fix and **not** composition; certification requires R1 to *rise*, not merely R2 to fall.
- **R12.3** — composition does **not** auto-recover when component retrieval improves; passing controls (R7) is necessary, not sufficient (R6b).
- **R12.4** — the k5_LATE-type cell is a **candidate** regime only, never an assumed-clean baseline; it must clear this definition like any other.
- **R12.5** — hop2 control at ceiling is a **validity floor, not a capability claim** (R7).

## 8. Boundaries

This object does not claim, and must not be read to claim: Claim C progress; Paper B activation; a certified baseline (it defines the bar; it does not meet it); compression evidence; any model capability; any mechanism / attention / architecture / training-distribution explanation; that terminal attraction is solved; or that Qwen2.5-3B can or cannot do two-hop reasoning. The strongest statement this rule surface ever licenses downstream is a **validity** statement about elicited behavior under declared conditions.

## 9. Admissibility checklist (the usable gate)

A candidate construction is **admissible for pre-registration** iff all hold; any failure rejects it by inspection, before any items or prompts are written:

1. C\* is not any present terminal (R8.1).
2. C\*, B, target-terminal, decoy-terminals are pairwise-distinct (R8.2).
3. All six categories (R1–R6cat) are separable in the output (R8.3).
4. Per-item hop1 and hop2 controls are defined and reportable (R7).
5. C\* is not directly associable with A; not independently guessable (R6c, R6d).
6. The primary metric is the multiclass scorer; binary accuracy is not gating (R9, R10).
7. The R11 block (k, position, n+power, success/inconclusive thresholds, failure signatures, decision rule) is fully pre-declared and locked before look.
8. The clutter regime is declared and is not lone-chain/minimal (R12.1).

A construction passing this checklist is *admissible to test*. Whether it then *certifies* a baseline depends on the run clearing the pre-declared success threshold — which this object does not and cannot decide.

---

*Status: v0.1, gate-before-construction. Held at property level; construction/task design deferred. Ready for claim-risk review (Contributor 5) and feasibility review. Certifies nothing; authorizes nothing.*
