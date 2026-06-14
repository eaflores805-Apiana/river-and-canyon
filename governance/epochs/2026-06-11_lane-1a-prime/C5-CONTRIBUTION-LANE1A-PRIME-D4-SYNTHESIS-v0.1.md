# C5 CONTRIBUTION — LANE1A-PRIME-D4-SYNTHESIS-AND-NEXT-QUESTIONS

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**Role in this memo (Manager §10):** adversarial review of overclaim paths · constructibility-risk guard · misuse / funder-language risk review
**For:** New Senior (synthesis lead) to merge into `LANE1A-PRIME-D4-SYNTHESIS-AND-NEXT-QUESTIONS-v0.1.md`
**To:** Team Lead → Manager · **Cc:** CS, Senior, New Senior
**Date:** 2026-06-11
**Status:** review-layer contribution, not the consolidated memo. **Authorizes nothing.** Working intent until CS commits the merged memo at a governance path with a SHA.

---

## 0. Scope discipline (what this contribution is, and is not)

```text
This IS the C5 layer: overclaim-path register, funder/misuse review, constructibility guard.
This is NOT: the synthesis memo, the current-state summary, the bounded-result section, the
  next-question map authoring, or the recommendation. Those are New Senior's (synthesis lead),
  with CS verification. I deliberately do not author them — authoring them from this seat is a
  role leak and is generation, not review.
I select no path, rank no paths, recommend no execution, populate no threshold, verify no hash.
```

I reviewed the Manager memo's already-specified required content (current state, bounded language, non-claim block, forbidden phrasings, next-question map). That content is disciplined; my findings below are the residual leak paths that survive *even that specification*, plus the two pieces this seat owns.

---

## A. Overclaim-path register (review of overclaim paths)

The accepted result is **NOT_RULED_OUT under a six-criterion set, including the candidate's own measured token prior**. That is strictly the strongest permitted reading and, per the Manager memo, may not be strengthened. The paths by which it gets strengthened anyway:

```text
OC1 — token-prior over-read (NEW with D4-B; highest-priority this round)
  Decay: "we also ruled out the candidate's token prior" -> "so it isn't a shortcut" ->
         "so it's genuine operation."
  Why wrong: D4-B ruled out the candidate's MEASURED token prior — one shortcut channel,
         instrumented and controlled. It did not rule out the space of shortcuts. "Not
         explained by this measured prior" is not "not explained by any prior," and is
         categorically not "not shortcut-driven" (a forbidden phrasing, §6).
  Containment: bounded line carries the exact qualifier "the declared shortcut battery OR
         the candidate's own measured token prior" as one closed clause; never compressed
         to "ruled out the token prior" standalone.

OC2 — progression-as-capability-ladder
  Decay: the §5 sequence (validated -> sealed -> first contact -> NOT_RULED_OUT ->
         TP-active -> NOT_RULED_OUT -> closed) reads, listed top to bottom, as ascending
         progress toward certification.
  Why wrong: it is a sequence of INSTRUMENT OPERATIONS and NON-ELIMINATIONS, not a capability
         ladder. Each NOT_RULED_OUT is a failure-to-eliminate, gap-shaped, fitting both the
         "genuine candidate" world and the "instrument/construction can't see the shortcut"
         world equally.
  Containment: label the progression explicitly as instrument-operation history; state that
         no step is a capability increment. Keeper: "Sealing binds an instrument state; it
         evaluates nothing."

OC3 — "twice NOT_RULED_OUT" -> "robustly survives"
  Decay: two NOT_RULED_OUTs in a row -> "the candidate keeps surviving" -> "robust" ->
         "validated candidate."
  Why wrong: D4-A (5-criterion, TP inactive) and D4-B (6-criterion, TP active) are two
         non-eliminations on the SAME narrow L01 surface, not independent stress survivals.
         Repetition of a double-negative is not accumulation of positive evidence.
  Containment: state that D4-A and D4-B do not aggregate into a strength claim; each is bounded
         to its own criterion set and neither rules in.

OC4 — verb leakage in the next-question map ("survive", "transfer", "hold")
  Decay: Path A "does the result SURVIVE broader extent", Path B "does it TRANSFER" — these
         verbs personify the candidate as surviving/holding under stress.
  Why wrong: the empirical question is whether the declared elimination criteria FIRE on
         L02–L08 / on a second model — not whether a candidate "survives." NOT_RULED_OUT is
         not a thing that survives; it is the absence of a fired criterion.
  Containment: phrase each path as "do the elimination criteria fire on <surface>?" rather
         than "does NOT_RULED_OUT survive <surface>?" (a wording edit for New Senior's map).

OC5 — Path D prerequisite-definition smuggling threshold work
  Decay: Path D ("what certifiable baseline is required before INT8/INT4") is answered by
         actually specifying a baseline -> which slides into candidate selection or threshold
         population under the label "defining the prerequisite."
  Why wrong: naming that a certifiable baseline is REQUIRED (doctrine: certification before
         retention) is not the same act as CONSTRUCTING or THRESHOLDING one. The first is
         in-scope synthesis; the second is a closed gate.
  Containment: Path D stays a question ("what would be required"), explicitly not an exercise
         that selects, ranks, or sets a number. Threshold/candidate gates remain closed.
```

Disposition on the Manager's required content: **PASS WITH TARGETED EDITS** — the edits are OC4 (verb phrasing in the next-question map) and explicit labels for OC1/OC2/OC3 in the bounded-result and progression sections. All wording/structure class; none changes the result.

---

## B. Misuse / funder-language risk review (Path C — the SBIR door)

Path C asks whether the evidence package is strong enough to consolidate into "a paper, internal report, or **funder-facing concept note** without further execution." A funder-facing concept note is the program's **highest future claim-risk surface**, because the funder-natural one-sentence compression of this entire program is the one claim three papers have refused.

```text
THE FORBIDDEN FUNDER SENTENCE (and its relatives):
  "a tool that measures whether quantization breaks composition"
  "detects the compositional seam" / "a quantization safety tool" /
  "certifies models for deployment" / "predicts deployment reliability" /
  "validated on Qwen2.5" (a funder reads "validated" as model-validated; it is
   INSTRUMENT-validated — the word inverts on contact with a funder audience).
WHY: these are the seam-tool / retention-predicts-reliability claims. The program has
  NOT measured a seam, NOT certified a candidate, NOT shown retention predicts reliability,
  and has run NO quantization. A concept note implying any of these overclaims against the
  program's own record.
```

What a funder-facing artifact **may** truthfully say (the §7a-aligned safe framing — stated so this review is not purely prohibitive):

```text
- The deliverable to date is a measurement DISCIPLINE: a fail-closed behavioral
  stress-metrology instrument that, for a given result, can rule out a declared battery of
  shortcut explanations (including a candidate's own measured token prior), and that has
  been validated, sealed, and shown to run under first model contact without falsely
  eliminating a narrow L01 surface.
- The contribution is a disclosure contract: a retention result must say what retained.
  That is real, packageable, and does NOT require the seam claim.
```

Hard constraints any funder/outside artifact must satisfy, to be raised BEFORE Path C is chosen, not after:

```text
F-1  M3 keeper survives funder prose verbatim: "no formalized certification gate has yet
     been exercised."
F-2  No claim is made that the instrument measures, detects, or predicts a compositional
     seam, model capability, or deployment reliability.
F-3  "validated/sealed" is qualified in-line as instrument-state, never model-state.
F-4  The closed benchmark-packaging gate and the closed SBIR-submission gate are NOT
     end-run by a "concept note" — a concept note is itself inside those gates and needs
     separate Manager authorization.
F-5  Aggregate/boundary level only; no per-run identified detail (no laundering of D4-A/B
     internals into an external narrative).
```

Note: the choice to pursue Path C at all is a Manager decision; this review does not recommend for or against it. It states the perimeter any Path-C artifact must clear.

---

## C. Constructibility-risk guard (integration)

Per Manager §7, the constructibility-risk carryforward note is referenced here as an interpretation guard and travels with this memo: `CONSTRUCTIBILITY-RISK-CARRYFORWARD-NOTE-v0.1.md` (C5 draft, pending CS commit). Load-bearing lines restated so the synthesis memo carries them even if read standalone:

```text
- D4-B L01 NOT_RULED_OUT does not prove a full candidate can certify; does not prove
  task-family viability across L01–L08; does not prove model capability; is not
  stress-retention evidence; is not Claim C progress.
- Any future non-certification stays a first-class three-way open set:
    (1) threshold miscalibration  (2) gate-design defect
    (3) genuine constructibility barrier at this model/task/scale.
  The third is a RESULT OF RECORD, not a program failure; none of the three is
  pre-registered as the expected outcome; non-certification is gap-shaped until a control
  separates the three.
- NOT_RULED_OUT is the absence of an elimination, not the presence of a certification. No
  certification gate has been exercised.
```

---

## D. Provenance and seat limits

```text
- All "validated / sealed / LOCK-RECORD v1.0 unchanged" assertions rest on hashes this seat
  did not compute; reported by the chain, require CS re-confirmation. No SHA asserted verified.
- The memo names the model as Qwen2.5-3B-Instruct (Path B). C5 takes the model identity as
  chain-reported working context, not independently verified.
- D4-A/D4-B execution and lifecycle-closed states are chain-reported; C5 has not seen the
  underlying authorizations or artifacts and does not assert them as record.
- The named TP-banner deviation, the emitter fix, and D5/D5-B closures live in the CS
  packets; this contribution does not restate or adjudicate them.
```

---

## E. Disposition

```text
Disposition on Manager-specified required content: PASS WITH TARGETED EDITS (OC1–OC5; all
  wording/structure class).
This contribution: route to New Senior to merge into the synthesis memo; then Team Lead;
  then Manager. Requires CS commit (path + SHA) to become record.
Requires CS verification: yes (LOCK-RECORD hashes; commit of merged memo).
Authorization implication: none. Selects no path, recommends no execution.
```

---

**The one to carry up:** D4-B's accepted result is **NOT_RULED_OUT under six criteria including the candidate's own measured token prior**, and the single new over-read this round is the token-prior one — "we ruled out the token prior" decaying into "not a shortcut" and then "genuine," when all that holds is *not explained by this one measured prior channel*, which the memo's own forbidden-phrasing list already bars from becoming "not shortcut-driven." Two NOT_RULED_OUTs on the same narrow L01 surface do not aggregate into strength; the §5 progression is instrument-operation history, not a capability ladder. The highest-leverage risk in the next-question map is **Path C**: a funder-facing concept note is the program's highest claim-risk surface because the funder-natural compression of the whole program — "a tool that measures whether quantization breaks composition" — is exactly the seam-tool claim three papers refused, so any Path-C artifact must clear a fixed perimeter *before* it is chosen (M3's "no formalized certification gate has yet been exercised" survives verbatim; no seam/capability/reliability claim; "validated" qualified as instrument-state; the closed benchmark-packaging and SBIR gates not end-run by calling it a "concept note"; aggregate-level only). The honest funder-safe framing does exist — a fail-closed measurement discipline and a retention-disclosure contract — and it does not require the seam claim, which is the point. I authored none of New Senior's synthesis sections by design, selected no path, and verified no hash; every sealed/validated assertion remains CS-owned.

— Contributor 5
