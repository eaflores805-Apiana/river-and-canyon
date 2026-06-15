# TARGET-CONSTRUCT-DEFINITION-v0.4

**E. A. Flores**, Apiana AI, Inc. — June 15, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. Gate-before-construction object.*

> **What this is.** A rule surface defining what counts as **"composing, not endpoint-grabbing,"** to be satisfied *before* anyone designs task items, writes prompts, sets a regime, or authorizes a run. It defines the bar a construction must clear to qualify as a certified-constructible FP16 baseline. **It certifies nothing, authorizes nothing, and is not a paper.**
>
> **Negative-use tag.** This object is a definition, not evidence. It is not evidence for a baseline, a model capability, a compression result, or Claim C. Citing it as evidence of any of those is a misuse.
>
> **Consolidation note.** v0.2 folds 16 open items (ledger `CONSTRUCT-DEF-v0.2-OPEN-ITEMS-LEDGER-v0.1`) from five reviews (C4, Senior ×2, C5, CS) in a single pass, shaped by the CS feasibility verdict below. Two of the folded items (OI-1, OI-2) correct soundness/scoring defects in v0.1, logged as drafter's errors.
>
> **v0.3 patch note.** v0.3 is a **narrow patch** carrying the routed **E7** item from `PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3`: it adds a named diagnostic category **R4b (depth-competitor-grab)** so depth-selection responses do not fall into generic *other* and inflate it with the wrong diagnosis. The patch **only** adds this diagnostic split and its dependent edits (failure signatures, other-rate ceiling, G6-scorability, admissibility). No do-not-weaken invariant is changed.
>
> **v0.4 patch note.** v0.4 is a **narrow pre-prereg patch** with exactly two changes: (1) it **promotes the dominance threshold (0.25) from scorer code into the definition**, declared with the failure signatures and qualified by a pre-declared analysis unit; and (2) it adds a **real-run fixture-mode guard** (an authorization/pre-registration requirement that a real-run spec assert `_fixture_mode` absent/false). No other rule changed; all do-not-alter invariants preserved byte-for-byte.

## Feasibility status (carried, not resolved)

CS feasibility verdict: **CONDITIONAL_FEASIBLE.** This means only that the construct **appears operationalizable without violating its own gate, provided the conditions below are carried.** It does **not** mean the construct is built, will certify when run, or is authorized to run. *"Appears buildable; whether it certifies when run remains unknown."* The substrate-infeasibility branch (§8.5) therefore does **not** fire at this stage; it remains pre-registered as a possibility.

Conditions carried into v0.2 (each maps to an open item below):

- The direct A→C\* shortcut is excludable via a per-item **direct-query control** (OI-1).
- The cross-query **constant-token** invalidator is operationalizable and made explicit (OI-2).
- The success threshold is **derived from the heuristic floor + margin**, not freely declared (OI-3).
- Interior-position salience is handled by **varying C\*'s position across items** (OI-5).
- Control isolation **and** load-matching coexist via **separate clutter-matched contexts** — composite, hop1, hop2, direct-query — **at a 4× generation cost** (OI-6).
- An R8 breach is a **construction-level rejection**, not item cleanup (OI-7).
- Rejected constructions are **structurally logged** (OI-8).
- **Computable** and **judgment** exclusions are separated (OI-10).
- The **other-rate ceiling** is declared and enforceable (OI-11).
- Future runs must be **scorable by G6** or its successor (OI-15).

---

## 0. Scope

In scope: response-category definitions, the validity gating of *correct-composition*, the controls, the admissibility conditions, the metric rule, the pre-run declarations, and the outcome branches.

Out of scope (absent by instruction): task items, concrete tokens, prompt templates, run plan, pre-registration values, compression comparison, Paper B / Claim C claims, model-execution request. Where a rule carries a construction-design consequence — terminal ≠ answer (R8), interior-position handling (R6f), control realization (R7) — the *property* is stated and the *realization* is deferred to construction design. CONDITIONAL_FEASIBLE means feasibility confirmed these properties are realizable; it does not import the realizations here.

## 1. Substrate and notation

Closed-world, in-context two-hop relational composition: facts are given in the prompt, then queried. Parametric recall is neither assumed nor required.

- Chain: head **A** —(r1)→ bridge **B** —(r2)→ target **C\*** (the correct composite answer), with **C\* at a non-terminal position** (R8.1) and **its position varied across items** (R11, OI-5).
- **Composite query** — apply r2∘r1 to A; correct response = C\*.
- **Component (control) queries** — hop1 = r1-of-A → B; hop2 = r2-of-B → C\*.
- **Direct-query control** — query C\* from A with the bridge **withheld** (or the composite relation named directly); a model that returns C\* here did so **without** traversal.
- **Terminal** — the salient endpoint entity of a presented chain (target or decoy): the token a recency/salience heuristic returns *without* following relations.
- **Decoy chains** — competing chains presented as clutter; their endpoints are **decoy terminals**.

## 2. Response categories (R1–R6cat, with R4b) — the primary scorer

Every response is classified into exactly one category by a pre-declared rule over the response token and the item's known entity set {C\*, B, target-terminal, decoy-terminals, depth-2 competitors {X_i}}, fixed before any run.

- **R1 — correct-composition.** Response = C\*, **and** the item's controls pass (R7), **and** the invalidators (R6) are all clear. Recorded as *behavior consistent with traversal under controls* — never as proof the model composed (R6 closing rule).
- **R2 — target-terminal-grab.** Response = the target chain's terminal. By construction (R8) a wrong answer. Positive evidence of terminal attraction on the target chain.
- **R3 — stopped-short.** Response = the intermediate B (hop1 result), not C\*. **An error, not partial credit** — diagnostic of hop2-in-composition failure (hop1 landed, the second hop in the composite did not). It is never scored as partial success; doing so would reintroduce a graded metric.
- **R4 — decoy-terminal-grab.** Response = a non-target chain's terminal. Wrong chain and wrong position; the salience pull is not even chain-localized.
- **R4b — depth-competitor-grab.** Response = some X_i, a **same-depth competitor node at depth 2 from A reached by a relation path other than r1→r2** (off the queried path). A wrong answer, and a **distinct diagnostic category — not a sub-type of R4** (R4 is a decoy *terminal*; R4b is a same-depth interior node at the right structural depth but the wrong relation path). Diagnostic meaning: **depth-selection / wrong-depth-2 competitor** — the model selected by structural depth without relation-following. It is the positive observable signature of the depth-selection heuristic that the same-depth competitors (and the 1/D floor) are built to expose.
- **R5 — abstain.** No entity commitment: refusal, "cannot determine," hedge, null, or empty. Not a wrong-entity commitment — **but not neutral**: on an answerable composite (C\* derivable, controls pass), abstention **is a failure to compose**, and an abstention-dominated construction is a failure-to-elicit (R11, §8.3), not "clean because no wrong commitments."
- **R6cat — other.** Any response matching none of the above (off-distribution token, malformed, entity not present). **Depth-2 competitor tokens {X_i} are NOT *other* — they are R4b**, so *other* now excludes the depth-selection signal. A real bucket: a high *other* rate (above the R11 ceiling) signals genuine construction/scorer mis-specification (off-distribution/malformed) — **not** depth-selection, which is now diagnosed by R4b.

## 3. Validity gating of correct-composition

### R6 — invalidators: what makes a composite-correct response INVALID as evidence of composition

A response equal to C\* does **not** count as R1 if any invalidator holds. The six invalidators, with their delineation (OI-13) and their computable/judgment status (OI-10):

- **(a) Terminal coincidence.** Response = C\* equals a terminal present in the item. Under R8.1 admissibility this is impossible; **if it ever fires at scoring, the construction silently breached R8.1 and is rejected as a whole** (§8.4, OI-7) — not item cleanup. *Mechanically computable* (token identity vs known terminal set).
- **(b) Components not available.** The item's hop1/hop2 controls did not pass (R7). You cannot credit composing facts the model cannot retrieve. *Mechanically computable* (logged control pass/fail).
- **(c) Direct A→C\* shortcut.** A latent A→C\* association produces C\* without traversal. This is **two parts**: a *construction property* — items built so C\* is not directly associable with A (enforced at admissibility, §4/§10) — and an *empirical confirmation* — the **direct-query control** (R7) must show the model **cannot** produce C\* from A with the bridge withheld. If the direct-query control passes (model produces C\*), R1 on that item is invalid. *Empirical side mechanically computable* (logged direct-query result); *design side enforced at admissibility*.
- **(d) Interior-position salience.** Once C\* sits at a non-terminal interior slot (R8.1), a fixed-position selection rule could yield C\* without traversal. Mitigated by **varying C\*'s position across items** (R11, OI-5): if correct responses are explained by a constant response-position while C\*'s actual position varies, R1 is invalid (interior-position-grab). *Mechanically computable* given logged positions. Distinct from (c): (c) is association-with-A; (d) is salience-of-the-slot.
- **(e) Cross-query constant-token.** If the response token is **constant across the item's hop1 / hop2 / composite / direct-query** queries, the model is emitting one token regardless of question — a flat heuristic, not composition — and R1 on that item is invalid even if that token equals C\* on the composite. *Mechanically computable* (token equality across the item's queries). This re-imports the G6 Rule B discriminator (the i06 "same token for every query" pattern), which per-query scoring would otherwise dismember into apparent partial composition.
- **(f) Underpowered / below heuristic floor.** An R1 rate not distinguishable from the derived heuristic floor (R11, the quantitative version of the salience baselines above) is not evidence. *Mechanically computable* given the derived floor.

**Exclusion adjudication (OI-10).** Invalidators (a), (b), (d), (e), (f) and the empirical side of (c) are **mechanically computable from logged fields** and must be applied by the scorer, not by hand. The *design* side of (c) and (d) is enforced at admissibility. The only residual **judgment** calls — chiefly **R6cat (other) adjudication** for ambiguous or malformed tokens (is a near-miss a typo'd C\* or genuinely off-distribution?) — must be **flagged as judgment and adjudicated under the program's role-separation**, never silently resolved by the scorer. An unread rule passes every check not pointed at it; R6's reader is named here (the scorer for computable exclusions; the adjudicating seat for judgment ones).

**Closing rule (the line we hold).** Even with all invalidators cleared, R1 is the *best-supported interpretation, never a proof.* Behavioral data cannot fully witness composition; some residual heuristic is always logically consistent with the right token. The construct's job is to exclude the available shortcuts by construction and control, gate on component availability, and name the residual — yielding a **validity statement** ("behavior consistent with traversal, under controls, with terminal-grab, direct-recall, interior-position, and constant-token routes excluded"), **never a claim about internal process.** A **capability** claim would additionally require what this construction does not and cannot provide: **mechanistic intervention** (showing the traversal computation is the cause) and **cross-construction generalization** (the behavior surviving across independent constructions and substrates). Absent those, the ceiling is a validity statement about elicited behavior under declared conditions — stated positively so the asymmetry has a shape, not just a negation.

### R7 — controls (rewritten: isolation + load-matching + logging)

Per item, before any R1 on that item is interpretable, four queries are run, **each in its own context** (OI-6):

- **hop1 control** — model returns B when asked r1-of-A. First fact available.
- **hop2 control** — model returns C\* when asked r2-of-B (given B). Second fact available. (Because terminal ≠ answer, hop2 targets the interior C\*, not a terminal.)
- **direct-query control** — model is asked for C\* from A with the bridge withheld; it must **fail** to produce C\* (OI-1, R6c). A pass here invalidates R1 for that item.
- **composite** — the measured query.

Control design constraints (OI-6, CONDITIONAL_FEASIBLE):

- **Isolation.** Controls run in **separate contexts** from the composite, so that asking a control (especially hop2, which surfaces C\*) does **not** seed C\* as a recently-attended token in the composite context. The composite must not be contaminated by prior controls. (v0.1's "same closed-world context" was the contamination; corrected here.)
- **Load-matching.** Each control runs under the **same clutter/load regime** as the composite (R11.k), so "components available" is established in the *same* condition composition is tested in — not an easier lone-chain condition.
- **Cost.** Isolation + load-matching means composite / hop1 / hop2 / direct-query are four separate clutter-matched contexts per item: a **4× generation cost**, accepted as the price of uncontaminated, load-matched controls (Manager resourcing decision, §11).
- **Per-item token-level logging.** The response token and its category are retained **per item, per query**, in a form supporting **same-error-identity comparison at a future compression rung** (OI-6) — so that a later "is the FP16 error the same as the INT4 error?" question is answerable without reconstruction.
- Controls are **validity floors, not capability claims** (R12.5); reported **per item**, never collapsed into one pass/fail.

## 4. Admissibility — terminal ≠ answer (R8)

The load-bearing structural requirement, checked **by inspection before any item is written**. A construction is **inadmissible** unless:

- **R8.1** — C\* is **not** any terminal present in the item (target or decoy); every salient endpoint maps to a *wrong* answer, so any terminal-grab is scoreable as an error (R2/R4) and can never be misread as correct.
- **R8.2** — C\*, B, target-terminal, all decoy-terminals, **and all depth-2 competitor tokens {X_i}** are **pairwise-distinct tokens** (no aliasing), so every response maps to exactly one category (including a clean separation of R4b from R6cat). *(Extended in v0.3 to cover {X_i}; this strengthens, not weakens, the same-depth competitor design.)*
- **R8.3** — all seven categories (R1, R2, R3, R4, R4b, R5, R6cat) are **distinguishable outcomes**; if any two cannot be separated in the output, the construct is unmeasurable. Feasibility confirmed this is operationalizable (C\*-position variation and separate contexts keep R3/R5 distinguishable in practice; distinct {X_i} tokens keep R4b distinguishable from R6cat); the **specific token-space realization remains construction-design and is not folded in here** (OI-16, scope-held).

**Breach handling (OI-7).** R8.1 is enforced at admissibility. If invalidator R6(a) (terminal coincidence) ever fires at scoring, it means the construction breached R8.1 silently → the **whole construction is rejected** (§8.4), not the single item.

R8 is *why* prior baselines were unmeasurable: when a terminal-grab can produce the correct answer, R1 and R2 collapse and the gate cannot open on linkage. Realization (chain structure placing the two-hop target off-terminal) is construction design, out of scope; the object asserts only the property.

## 5. Metric rule (R9, R10)

- **R9 — binary accuracy cannot be the primary metric.** It lumps R1 with any uncaught coincidence-correct and merges R2/R3/R4/R5 into one "wrong" bucket, erasing the diagnostic difference between *didn't traverse* and *traversed one hop*. It is the metric under which prior baselines passed via coincidence. The failure mode is invisible to it by construction.
- **R10 — the R1–R6cat multiclass scorer is primary.** Category boundaries fixed before any run (lock-before-look). Binary accuracy may exist only as a derived summary and **must never gate interpretation.**

## 6. Pre-run declaration required before any run (R11)

Locked before look, as a single pre-registered block (values set at construction/pre-registration time, not here):

- **k / clutter regime** — number of competing chains and how clutter is set; not lone-chain/minimal (R12.1).
- **target-terminal position** — declared (position gates the effect; direction flips with k).
- **C\* position-variation rule** — how C\*'s interior position is varied across items, so a fixed-position heuristic cannot track it (R6d, OI-5).
- **n / power rationale** — sample size and the calculation; n must distinguish the R1 rate from the derived heuristic floor, not a probe-sized n.
- **derived heuristic floor** — the rate at which the strongest available non-traversal heuristic would produce C\* by chance, **derived from R8 + k + the candidate/terminal counts** (not assumed). (OI-3)
- **success threshold = floor + margin** — the pre-declared margin above the derived floor that counts as "this construction elicits composition." **Derived, not a free number** (OI-3); a low bar cannot be declared into a pass.
- **inconclusive band** — the band that neither certifies nor refutes; pre-committed so *inconclusive* is an outcome, not a retrospective hedge.
- **failure signatures** — patterns meaning the gate failed, each mapped to a diagnosis. **A failure category is "dominant" when its rate is ≥ 0.25 over the pre-declared analysis unit** (the dominance threshold, promoted from scorer code into the definition in v0.4). **Dominance is evaluated over the pre-declared analysis unit: global run, declared cell/regime, or both. If both are used, per-cell/regime dominance is primary for diagnosing localized construction failure; global dominance is secondary summary.** (For Path A, the exact analysis unit is left to the pre-registration unless already fixed.) The signatures: R2 dominant (target-terminal attraction); R4 dominant (cross-chain salience); **R4b dominant (depth-selection regime → right structural depth, wrong relation path; R4b-dominant with R1 ≈ 1/D confirms depth-selection)**; R3 dominant (hop2-in-composition failure); **R5 dominant (abstention regime → failure-to-elicit, OI-12)**; **cross-query constant-token prevalent (flat heuristic, OI-2)**; **direct-query shortcut prevalent (R6c invalidated the R1 candidates → direct-recall route active)**; control-floor failure (controls not met → missing-fact, not composition); other-rate-ceiling breach (the separately-declared other-rate ceiling exceeded → construction/scorer mis-specified); R1 indistinguishable from the derived floor. The rate-based "dominant"/"prevalent" signatures use the 0.25 threshold; **control-floor failure and other-rate-ceiling breach apply their own declared criteria** (the control pass/fail test, and the declared other-rate ceiling — a value distinct from 0.25), not the dominance threshold.
- **other-rate ceiling** — a declared, enforceable ceiling above which the construction is deemed mis-specified (OI-11). Value set at construction time; existence required now. **The ceiling now excludes depth-competitor grabs (counted as R4b, not *other*), so a high *other* rate signals genuine off-distribution/malformed mis-specification — not depth-selection, which has its own R4b signature (E7).**
- **G6-scorability** — the run must be scorable by the G6 evaluator or its successor; the seven categories (R1–R6cat **incl. R4b**) and R6 invalidators are defined to be G6-operable (OI-15). **R4b is mechanically computable: the depth-2 competitor tokens {X_i} are known per item, so a response equal to some X_i is classified R4b by token match, distinctly from R6cat.** This object defines the admissible construct; G6 operationalizes the gate.
- **decision rule** — maps the thresholds to the §8 outcome branches, declared in advance.

## 7. Constraints carried from the terminal-attraction sweep (R12)

- **R12.1** — lone-chain / minimal constructions *maximize* endpoint attraction; minimal is the dirtiest baseline. → R11 (declare clutter, not minimal).
- **R12.2** — clutter can *reduce* target-terminal attraction, but a fall in grabbing is **not** a fix and **not** composition; certification requires **R1 to rise**, not merely R2 to fall.
- **R12.3** — composition does **not** auto-recover when component retrieval improves; passing controls (R7) is necessary, not sufficient (R6b).
- **R12.4** — the k5_LATE-type cell is a **candidate** regime only, never an assumed-clean baseline; it must clear this definition like any other.
- **R12.5** — hop2 control at ceiling is a **validity floor, not a capability claim**.

## 8. Outcome branches

The decision rule (R11) maps a run's results to exactly one of five pre-committed outcomes:

- **8.1 CERTIFY** — R1 rate ≥ success threshold (= derived floor + margin), controls pass, all invalidators clear, no failure signature dominant. The construction **qualifies as** a certified-constructible FP16 baseline. *This object defines the bar; a run decides; certification is not asserted here.*
- **8.2 INCONCLUSIVE** — R1 rate in the declared inconclusive band; neither certifies nor refutes.
- **8.3 FAIL** — a failure signature dominant (R2/R4 terminal attraction, R3 hop2-in-composition failure, R5 abstention-regime, constant-token, direct-query shortcut, control-floor failure, other-rate-ceiling breach) or R1 below floor+margin. **"Dominant" means a category rate ≥ 0.25 over the pre-declared analysis unit (R11).** The construction failed its gate; the dominant signature is the diagnosis.
- **8.4 REJECTED-CONSTRUCTION** — an admissibility breach detected at scoring (R6(a) terminal coincidence fires, token aliasing, or categories not separable). The construction is **rejected as a whole** and the rejection — with its breached condition — is **structurally logged** (OI-8); disposition (archive / iterate / abandon) is a declared routing decision under role-separation, not limbo.
- **8.5 SUBSTRATE-INFEASIBILITY CANDIDATE** — if **admissible** constructions (not rejected ones) **repeatedly fail to certify**, this becomes a first-class finding candidate: the conjunction of exclusions may be unsatisfiable on this substrate. **Pre-committed here as a possibility (OI-4); it does NOT fire at this stage** (the feasibility verdict is CONDITIONAL_FEASIBLE). It is **never** a license to loosen R8 / R6(c) / the threshold to manufacture a pass — a gate that never opens on linkage is observationally identical to a miscalibrated one until one construction clears it, and the integrity guard is to pre-commit that the gate may correctly never open.

## 9. Boundaries

This object does not claim, and must not be read to claim: Claim C progress; Paper B activation; a certified baseline (it defines the bar; it does not meet it); compression evidence; any model capability; any mechanism / attention / architecture / training-distribution explanation; that terminal attraction is solved; or that Qwen2.5-3B can or cannot do two-hop reasoning. CONDITIONAL_FEASIBLE means *appears buildable*, not *built* or *will certify*. The strongest statement this rule surface licenses downstream is a **validity** statement about elicited behavior under declared conditions.

## 10. Admissibility checklist (the usable gate)

A candidate construction is **admissible for pre-registration** iff all hold; any failure rejects it by inspection, before any items or prompts are written:

1. C\* is not any present terminal (R8.1); R6(a) firing at scoring = whole-construction rejection (OI-7).
2. C\*, B, target-terminal, decoy-terminals are pairwise-distinct (R8.2).
3. All seven categories (R1, R2, R3, R4, R4b, R5, R6cat) are separable in the output, with depth-2 competitor tokens {X_i} distinct so R4b separates cleanly from R6cat (R8.2, R8.3).
4. Per-item hop1, hop2, **and direct-query** controls are defined and reportable, in **separate clutter-matched contexts**, composite uncontaminated by prior controls (R7).
5. C\* is not directly associable with A (design side, R6c) **and** the direct-query control is in place (empirical side); C\*'s position is varied across items (R6d, OI-5).
6. The primary metric is the multiclass scorer; binary accuracy is not gating (R9, R10).
7. The R11 block is fully pre-declared and locked: k, position, **C\* position-variation rule**, n+power, **derived heuristic floor**, **success threshold = floor+margin**, inconclusive band, failure signatures (incl. constant-token and abstention-dominant; **dominance threshold = 0.25 over the pre-declared analysis unit**), **other-rate ceiling**, **G6-scorability**, decision rule.
8. The clutter regime is declared and not lone-chain/minimal (R12.1).
9. Per-item, per-query **token-level logging** for same-error-identity is in place (OI-6).
10. A **rejected-construction disposition** path is declared (OI-8).
11. **Real-run fixture-mode guard (v0.4).** Any real-run construction spec must assert `_fixture_mode` is absent or false. A spec with `_fixture_mode: true` is **inadmissible for real-run pre-registration** and must be treated only as a software fixture. *(Authorization / pre-registration guard — it prevents a real run from bypassing Manager-lock enforcement by self-declaring fixture mode. It is not a software-logic claim: the software already fails closed in real-run mode and exempts fixtures; this rule binds the pre-registration to never present a real construction as a fixture.)*

A construction passing this checklist is *admissible to test*. Whether it then *certifies* depends on the run clearing the derived success threshold — which this object does not and cannot decide.

## 11. Changelog v0.1 → v0.2 (by open-item ID)

**Must-fix (soundness/scoring):**
- **OI-1 — resolved.** R6(c) split into an admissibility design-property (§4/§10) + a per-item **direct-query control** (R7, §1). No longer an unverifiable scoring filter. *(Corrects a v0.1 drafter's error.)*
- **OI-2 — resolved.** **Cross-query constant-token** invalidator added (R6e), made explicit, and added to R11 failure signatures; re-imports G6 Rule B. *(Corrects a v0.1 scoring gap.)*
- **OI-3 — resolved.** Success threshold now **derived from heuristic floor + margin** (R11); floor derived from R8 + k. Free-number declaration removed.

**Additions:**
- **OI-4 — resolved.** Substrate-infeasibility added as a pre-committed outcome (§8.5); explicitly does not fire now; explicitly not a license to loosen the gate.
- **OI-5 — resolved.** Interior-position salience invalidator added (R6d) + **C\* position-variation rule** in R11.
- **OI-6 — resolved.** R7 rewritten: isolation (separate contexts) + load-matching + per-item token logging; 4× generation cost recorded.
- **OI-7 — resolved.** R8 breach → whole-construction rejection (R6a, §4, §8.4).
- **OI-8 — resolved.** Rejected-construction disposition structurally logged (§8.4, checklist #10).

**Tightenings:**
- **OI-9 — resolved.** R6 closing rule given positive shape (capability would require mechanistic intervention + cross-construction generalization) + "never a claim about internal process."
- **OI-10 — resolved.** Computable vs judgment exclusions separated (R6 adjudication paragraph).
- **OI-11 — resolved.** Other-rate ceiling declared and enforceable (R11, R6cat).
- **OI-12 — resolved.** R5 §2 framing aligned with R11 (abstention-dominant = failure-to-elicit).
- **OI-13 — resolved.** R6(c)/(d)/floor delineated (R6 entries).
- **OI-14 — resolved.** R3 sharpened to error-with-diagnosis, never partial credit (§2).
- **OI-15 — resolved.** G6-scorability required (R11).

**Scope-held:**
- **OI-16 — held.** R8.3 token-space realization remains construction-design; feasibility confirmed operationalizable; not folded into the object.

**Do-not-drift invariants preserved:** R8 (terminal ≠ answer, inspection), R6 closing rule (validity not capability — *strengthened* by OI-9, not diluted), R9/R10 (multiclass primary, binary non-gating), R12.2 (R1 must rise, not R2 fall), and the lock-before-look outcome rule (now five branches, §8).

**OI resolution summary:** 15 of 16 resolved-and-folded; 1 (OI-16) scope-held by design. None deferred unaddressed.

## Changelog v0.2 → v0.3 (routed E7 diagnostic split)

- **E7 — carried.** Added **R4b (depth-competitor-grab)** as a named diagnostic category: response = some X_i, a same-depth competitor at depth 2 from A off the queried r1→r2 path; diagnosis *depth-selection / wrong-depth-2 competitor*. Dependent edits, all narrow: §2 category list and known entity set (add {X_i}); §2 R6cat (depth-2 competitors are R4b, not *other*); R8.2 (pairwise-distinctness extended to {X_i} — a strengthening); R8.3 and checklist #3 (six → seven categories); R11 failure signatures (R4b-dominant → depth-selection regime; R4b-dominant + R1 ≈ 1/D confirms depth-selection); R11 other-rate ceiling (now excludes R4b, so a high *other* rate means genuine mis-specification, not depth-selection); R11 G6-scorability (R4b mechanically computable from known {X_i}).
- **Purpose served.** A working depth-selection control would otherwise inflate *other* with depth-competitor grabs and trip the other-rate ceiling with the wrong diagnosis. R4b separates the depth-selection signal from generic *other*, so the ceiling measures genuine mis-specification and depth-selection is diagnosed where it belongs.

**Patch scope confirmation:** v0.3 **only** adds the R4b diagnostic split and its dependent edits. **No do-not-weaken invariant changed:** terminal ≠ answer (R8.1); direct-query control; same-depth competitor design (R8.2 *strengthened* to cover {X_i}, not weakened); F = max(1/p, 1/m, 1/D) (untouched — R4b is a diagnostic category, not a floor term); relation-balancing admissibility property; four-context isolation; validity-not-capability boundary; substrate-infeasibility branch (§8.5). No items, prompts, pre-registration, run, compression, or Claim C / Paper B language added.

## Changelog v0.3 → v0.4 (dominance threshold + real-run fixture-mode guard)

- **Patch 1 — dominance threshold promoted into the definition (R11, §8.3, checklist #7).** Exact wording: *"A failure category is 'dominant' when its rate is ≥ 0.25 over the pre-declared analysis unit."* Applied to the rate-based failure signatures (R2/R4/R4b/R3/R5 dominant; cross-query constant-token prevalent; direct-query shortcut prevalent), with control-floor failure and other-rate-ceiling breach keeping their own declared criteria. Analysis-unit clarification added: *"Dominance is evaluated over the pre-declared analysis unit: global run, declared cell/regime, or both. If both are used, per-cell/regime dominance is primary for diagnosing localized construction failure; global dominance is secondary summary."* For Path A, the exact analysis unit is left to the pre-registration unless already fixed. This closes the v0.3-prior provenance flag (the 0.25 threshold was a scorer-code constant, not declared with the signatures it governs).
- **Patch 2 — real-run fixture-mode guard (checklist #11).** Exact wording: *"Any real-run construction spec must assert `_fixture_mode` is absent or false. A spec with `_fixture_mode: true` is inadmissible for real-run pre-registration and must be treated only as a software fixture."* This is an authorization/pre-registration guard, not a software-logic claim; it prevents a real run from bypassing Manager-lock enforcement by self-declaring fixture mode (the external guarantee named in the value-lock-patch review).

**Confirmation — no other rule changed.** The two patches above are the only substantive edits. Preserved byte-for-byte (do-not-alter): R4b diagnostic split; terminal ≠ answer; direct-query control; relation-balancing admissibility; F = max(1/p, 1/m, 1/D); success threshold = F + margin; Manager-approved values; four-context isolation; validity-not-capability boundary; substrate-infeasibility branch. No items, prompts, pre-registration, run request, compression, or Claim C / Paper B language added.

---

*Status: v0.4, gate-before-construction. v0.2 consolidated from five reviews under CONDITIONAL_FEASIBLE; v0.3 carried the E7 R4b split; v0.4 promotes the dominance threshold (0.25, analysis-unit-qualified) into the definition and adds the real-run fixture-mode guard. Held at property level; construction/task design and pre-registration values deferred. Certifies nothing; authorizes nothing. Ready for pre-registration shell.*
