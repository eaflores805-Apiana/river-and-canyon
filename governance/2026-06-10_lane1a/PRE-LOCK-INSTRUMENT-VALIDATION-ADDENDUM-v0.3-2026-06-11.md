# Pre-Lock Instrument Validation Addendum (v0.3) — Filed for CS Review

From: New Senior Engineer (drafted 2026-06-11, under Team Lead assignment of 2026-06-10)
To: Team Lead → Senior review → CS review → Manager adoption decision
Filed by: CS Engineer at the next step in the routing chain
Status: PROPOSED standing addendum; CS review filed at `CS-REVIEW-PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM-v0.3-2026-06-11.md`

---

## Routing record (corrected per Team Lead routing note 2026-06-11)

| Step | Status | Who |
|---|---|---|
| 1. New Senior drafts (this document) | DONE (v0.1 → v0.2 → v0.3) | New Senior |
| 2. Team Lead filter (v0.3) | **PASS** (per `TEAMLEAD-ROUTING-NOTE-PRE-LOCK-ADDENDUM-v0.3-2026-06-11.md`) | Team Lead |
| 3. Senior conceptual review (v0.3) | **IN FLIGHT** | Senior |
| 4. CS review (implementability + path + templates) | AWAITED (after Senior PASS) | CS |
| 5. Manager adoption decision | PENDING (final) | Manager |

Note: an earlier Senior review covered v0.1 → v0.2 (the v0.2 changelog records "the two required revisions from the Senior step-3 review"). The current Senior review is on v0.3.

---

## Provenance

The v0.3 draft is filed as received from the user 2026-06-11. CS has
not modified the substantive content; the addendum text below is the
review subject for the CS-side review filed in the companion memo.

(The verbatim addendum text follows in §1 onward exactly as provided
by New Senior; only this routing header is CS-added scaffolding.)

---

[ADDENDUM TEXT BEGINS — verbatim from New Senior v0.3]

# Pre-Lock Instrument Validation Addendum (v0.3)

*v0.3 changes:*
*1. Added classifier/certifier scope guard.*
*2. Softened positive retrieval wording.*
*3. Added standing-rule path confirmation as adoption condition.*
*4. Surfaced R6 in front matter.*
*5. Clarified diagnostic-only / non-eliminating rule consequence.*

## Battery Operating-Characteristic Validation and Criterion Well-Formedness for D2-Style Diagnostic Batteries

> **Before retention, certify the task. Before certification, validate the instrument.**
> Retention claims depend on certification. Certification depends on valid instruments. Valid
> instruments depend on pre-lock operating-characteristic checks.

*Proposed standing addendum — governance/template work only. Drafted by New Senior Engineer, 2026-06-11, under Team Lead assignment of 2026-06-10. v0.2 applies the two required revisions from the Senior step-3 review (frozen-term preservation via the ill-formed umbrella; §2 per-policy precision); no other content changed. Route: this draft → Team Lead filter → Senior
review → CS review → Manager adoption decision. It becomes a standing rule only at Manager adoption.
No execution, Lane 1a′ work, model run, data generation, candidate/threshold/certification work, B1
v2.1 work, or Paper 3 revision is authorized or implied. Proposed repo home:
`governance/standing/PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM.md` (and see §9 note on confirming the
standing-rules path convention). Subtitle reconciles the Team Lead's suggested form with the
inputs-package decided form; Team Lead filter picks if one is preferred.*

**Provenance.** Converts the Lane 1a close-out findings (Close-Out v1.1 §4 Findings A/B/C, §10
R1/R6) into standing requirements per the Manager structure memo and Team Lead C5-intake
formulation. Contributor 6's "Instrument Pre-Flight Hardening Packet" is merged as source input per
the Senior routing recommendation, with credit: the named oracle-case battery, the five-type control
taxonomy, and the pass-region checklist are Contributor 6's contributions. One document, templates as appendices (Manager smallness constraint); CS may split template files post-adoption. **This addendum also installs R6, the requirement-inheritance check, to prevent applicable prior-lane requirements from silently failing to transfer into new packets** — Lane 1a failed partly because a battery-validation requirement existed in the certification context and was not inherited into the reconnaissance lane (§8).

---

## 1. Purpose

Prevent any future diagnostic battery, sweep classifier, control design, or certification-adjacent
instrument from being locked before it proves basic discriminative competence. A fail-closed
instrument has two error surfaces: it can be too permissive (falsely certifying dirty behavior — the
surface Paper 3 was built against) and it can be self-eliminating (falsely rejecting ideal
behavior — the surface Lane 1a demonstrated). Both are measurement failures. The governing rule this
addendum installs: **an instrument must demonstrate, before lock, that it can fire and that it
cannot always fire** — that it detects what it claims to detect and passes what it must pass.

## 2. Origin in the Lane 1a close-out

Lane 1a completed cleanly and emitted a mechanical K=0 under locked rules; that verdict stands
mechanically. Post-run audit showed the substantive interpretation was instrument-limited: three
universal elimination labels were driven by instrument-side artifacts — (1) two declared dummy policies reduced to retrieval oracles — `homogeneous_prefix_completion` scored 80/80 on every rung (self-match at full key length), and `target_recency` scored 80/80 on K=low rungs (unique first letters leave the queried key as the only first-character match); one oracle suffices for saturation, so the union envelope reached 1.000 on every rung;
(2) the token-prior control measured retrieval under scrambled bindings, not token-prior emission,
so candidate ≈ control was consistent with retrieval under both conditions, not with token-prior behavior (a diagnosis of the instrument, never a claim of candidate viability, certifiability, or positive model capability); (3) the abstention band `[0.50, 0.95]` excluded
ideal NULL discipline, firing on a perfect 1.000 abstention rate. The result was archived as a
fail-closed instrument-discrimination finding. **Citation scope (P4, binding on this document and
all descendants):** Lane 1a is cited only as a documented instrument-discrimination case study —
never as a certifier, model, occupancy, or threshold-supporting result; in particular, the `scrambled_binding_retrieval` reframing in §5 may not be used to retroactively reinterpret Lane 1a control numbers as a positive rebinding finding. **Classifier/certifier scope guard:** Lane 1a demonstrated a false-reject mechanism in a reconnaissance classifier. It did not measure the false-reject rate of any Paper 3 certification gate, and no formalized Paper 3 certification gate has yet been exercised — Lane 1a labels were sweep classifications, not Paper 3 certification-gate verdicts.

## 3. Definitions

- **Instrument:** a declared policy battery, classification-criterion set, control design, or any
  combination intended to be locked for diagnostic or certification-adjacent use.
- **Ideal witness:** the synthetic record of textbook-perfect behavior for the construction —
  perfect retrieval on answerable items, perfect format compliance, contract abstention on every
  NULL item.
- **Operation-equivalent policy:** a declared dummy policy whose pilot accuracy reaches the declared
  cap — it performs the operation rather than detecting its absence.
- **Degenerate policy:** constant, structurally undefined, or operation-equivalent on the
  construction; not a valid detector regardless of prediction-vector variation.
- **Malformed criterion (frozen, close-out v1.2):** a rule whose pass or non-elimination region excludes ideal behavior. The term is frozen narrowly and is not broadened here.
- **Ill-formed criterion classes (umbrella, this addendum):** *dead* (cannot fire), *tautological* (always fires), and *malformed* (excludes ideal) — full definitions §6.
- **Must-fix:** any review or validation finding that may affect execution, release, certification,
  or interpretation.
- **Enforcement triple:** vehicle, owner, audit artifact. A requirement lacking its triple is
  wording-class by the program's own standard ("a control is not structural because we describe it
  structurally"); every requirement below carries one.

## 4. Battery operating-characteristic validation (Section A)

**A-rule (standing, verbatim):**
> **Non-constant ≠ non-degenerate.**
> **A policy that scores 100% on answerable items is the operation, not evidence of the operation's
> absence.**

**A1 — Pilot-manifest battery run (execution, not inspection).** Before lock, every declared policy
is executed against pilot manifests generated by the locked construction recipe (policies are
deterministic and offline: no model, no candidate data, no gate). Recorded per policy: accuracy on
answerable items; accuracy on NULL/no-answer items where applicable; distinct-output count; full
prediction vector. Inspection is insufficient by documented demonstration: Lane 1a's control defect
was graded minor at spec time and proved load-bearing.
*Owner: Senior + CS. Artifact: per-policy score table + union-envelope summary (Appendix T1). Pass:
all A2–A4 conditions met. Lock consequence: packet may not lock until corrected or formally declined
by Manager with rationale.*

**A2 — Per-policy degeneracy cap.** Each battery declares, before pilot execution and with
rationale, a cap on single-policy accuracy. A policy at or above cap is classified
operation-equivalent: *a dummy policy that scores at or near ideal-behavior level is not a valid
shortcut detector unless explicitly re-declared as a positive oracle rather than a negative dummy.*
Cap values are packet-specific declarations; this addendum sets requirements, never values.
*Owner: Senior (declaration) + CS (measurement). Artifact: declared-caps block in the validation
report. Pass: no policy exceeds cap while still classified as a dummy. Lock consequence: as A1.*

**A3 — Union-envelope cap.** The declared-policy union envelope on pilot manifests must leave
declared measurement room. **A floor against a 1.000 envelope is no floor** (close-out, verbatim):
an envelope at saturation makes every envelope-relative elimination fire unconditionally on any
possible candidate.
*Owner: Senior + CS. Artifact: union-envelope summary in T1. Pass: envelope below declared cap.
Lock consequence: as A1.*

**A4 — Policy classification.** Post-pilot, every policy is classified
`discriminative | operation_equivalent | degenerate_constant | structurally_undefined`; only
`discriminative` policies count toward declared battery-coverage minima; a battery falling below
coverage after classification fails validation and is redesigned and re-piloted before lock.
*Owner: Senior. Artifact: classification column in T1. Pass: coverage minimum met by discriminative
policies alone. Lock consequence: as A1.*

**A5 — Oracle-case discrimination pre-flight** (Contributor 6, Component 1). The instrument is run,
pre-lock, against synthetic or oracle-coded cases representing at minimum: ideal retriever; each
declared shortcut policy; token-prior / surface-bias emitter; universal answerer; universal
abstainer; perfect NULL-on-NULL handler; one malformed-control case. Required outcomes: the
instrument must not eliminate the ideal retriever; must detect each declared shortcut where
expected; must distinguish token-prior emission from retrieval; must treat perfect NULL-on-NULL
behavior as valid unless the declared task states otherwise. **Non-claim (verbatim concept, C6):
passing this pre-flight does not validate the instrument generally; it shows only that the
instrument is not obviously self-eliminating or non-discriminating on declared oracle cases.**
*Owner: CS (execution) + Senior (case declarations). Artifact: oracle-case verdict table in the
validation report. Pass: every declared expected-verdict matches. Lock consequence: as A1.*

## 5. Control semantics specification (Section B, part 1)

**B1 — Semantic target locked before implementation.** Every control declares, before any code is
written, all of: `control_name; semantic_target; behavior it isolates; behavior it must not reward;
bindings handling (preserved | scrambled | removed | replaced); scoring target; expected
chance/baseline rate; expected ideal-model behavior; expected shortcut-model behavior; failure
interpretation; non-claim`. The code implements the declared target — it does not define the target
after the fact.
*Owner: Senior (spec) + CS (conformance). Artifact: control-spec sheet (Appendix T2), locked and
hashed with the packet. Pass: every field populated pre-implementation; pilot behavior consistent
with declared target. Lock consequence: as A1.*

**B2 — Target taxonomy (Contributor 6, Component 3; non-interchangeable by rule).**
`unconditioned_token_prior` (surface emission bias without task-relevant bindings) ·
`scrambled_binding_retrieval` (whether the model follows new bindings after rebinding) ·
`null_context_control` (behavior when task-relevant context is absent) · `copy_surface_control`
(whether surface span copying solves the item) · `dummy_policy_control` (whether a declared
non-operational policy explains performance). The four reference targets — original-token,
post-scramble-token, null-context, frequency-baseline — are **not interchangeable**; Lane 1a's
control was a well-formed instance of the second taxon mislabeled as the first, which is exactly why
the declaration precedes the code. (P4 scope from §2 applies to any use of this taxonomy against
Lane 1a numbers.)

## 6. Ideal-witness / malformed-criterion check (Section B, part 2)

**B3 — Ill-formed criterion classes.** Three named classes, screened jointly by B4: **dead** — the rule cannot fire under the construction's scoring identities (the gap-sign incident: `strict − content ≥ 0.15` where strict-correct implies content-correct); **tautological** — the rule always fires regardless of candidate behavior (any label referenced to a 1.000 envelope); and **malformed** — per the close-out v1.2 frozen definition, kept narrow and verbatim: *a criterion whose pass or non-elimination region excludes ideal behavior* (the abstention-band incident).
Motivating example, kept: *a rule that excludes 1.000 correct NULL abstention is not merely
conservative; it excludes the ideal witness.*

**B4 — Ideal-witness check (pre-lock, every gate, label, or classification rule).** For each
criterion: define ideal behavior for its stratum; verify the pass/non-elimination region includes
that ideal point; then answer the five-question checklist (Contributor 6, Component 4): (1) what is
ideal behavior for this stratum? (2) does the pass or non-elimination region include it? (3) does
the rule confuse ideal behavior with universal or degenerate behavior? (4) does the rule separately
test answerable and NULL strata where needed? (5) **could a perfect model be eliminated by this
rule?** B4 screens for all three B3 classes. Required rule: *any rule that eliminates ideal behavior must be revised or explicitly scoped as diagnostic-only and non-eliminating;* dead and tautological rules are corrected before lock in all cases. A diagnostic-only rule may inform interpretation but may not produce an elimination label unless separately justified and locked — a malformed eliminator does not survive merely by being renamed diagnostic. The only legitimate exception class is declared at spec
time with written justification: measurement-resolution criteria (e.g. insufficient headroom) that
intentionally fire on a saturated pilot score — the D1×D7 squeeze, observed empirically at Lane 1a's
near-ceiling rungs as the M1/M2 arithmetic predicts.
*Owner: Senior. Artifact: pass-region checklist (Appendix T3), one row per criterion, in the
validation report. Pass: every criterion includes its ideal point, or carries the diagnostic-only
mark, or carries the declared headroom-class justification. Lock consequence: as A1.*

## 7. Review-to-lock disposition table (Section C, part 1)

**C1 — Every must-fix is dispositioned before lock.** Each must-fix receives exactly one disposition:
`incorporated | declined with rationale | deferred with rationale and owner | superseded by stronger
control`. No must-fix disappears silently between review and lock. Canonical incident: the warning
that predicted the abstention-band defect was filed pre-lock without disposition; the band locked
and fired on the ideal witness.
*Owner: Team Lead (table acceptance) + Senior (population). Artifact: disposition table (Appendix
T4) with fields `review_item_id; reviewer; risk_class; summary; disposition; rationale; owner;
commit_or_file_reference; blocking_status`. Pass: zero must-fix rows without disposition. Lock
consequence: lock blocked while any row is open.*

**C2 — Delivery rule (standing, restated as lock-input rule).** *SEND-TO-CS is intent. Delivery is
a confirmed commit SHA at the intended path in the target repository; for release-affecting or
execution-affecting artifacts, delivery also requires filename and hash or blob identifier.* A
review that closes a gate enumerates, by hash, the condition memos it considered; any
review-in-flight is confirmed delivered-or-withdrawn before a PASS is recorded — a memo no one knows
exists cannot hold a gate.
*Owner: gate-closing reviewer. Artifact: considered-memos enumeration inside the PASS record. Pass:
enumeration present and complete. Lock consequence: PASS invalid without it.*

## 8. Requirement-inheritance check (R6)

**C3 — R6 (verbatim):**
> *Requirement-inheritance check: every new packet review screens prior-lane requirements for
> portability; an applicable requirement is adopted, adapted with rationale, or declined with
> rationale — never silently un-inherited.*

Canonical incident: the cure for Finding A already existed in released text. Paper 3's D2 carries
the battery-sensitivity ancestor — battery sensitivity *"demonstrated against the pre-registered
deterministic shortcut implementations — dummy-policy outputs computed offline — not inferred from
the candidate's failure to exhibit the shortcut"* (released v1.1, tag
`paper3-certification-protocol-v1.1`; present in v1.0 ancestry). That requirement lived in the
certification lane and was not inherited by the reconnaissance lane. This addendum is itself an act
of R6 compliance: it ports and completes that ancestor (sensitivity alone is shown insufficient
without the operation-equivalence and envelope caps).
*Owner: packet reviewer. Artifact: inheritance-screen section in every future packet review. Pass:
every applicable prior-lane requirement carries adopt/adapt/decline with rationale. Lock
consequence: review incomplete without it.*

## 9. Required artifacts (consolidated)

One **Instrument Validation Report** per packet, locked and hashed with the packet, containing:
T1 per-policy score table + union-envelope summary + classification + declared caps (A1–A4); the
oracle-case verdict table (A5); T2 control-spec sheets (B1–B2); T3 pass-region checklist (B3–B4);
T4 review-to-lock disposition table (C1); the considered-memos enumeration (C2); the
inheritance screen (C3). Template skeletons are Appendices T1–T4 of this addendum (one document,
per the smallness constraint; CS may split into standalone template files post-adoption).
**Containment:** pilot manifests and all validation outputs inherit the program's negative-use
discipline in full — excluded from sweep statistics, threshold design, certification evidence, and
the D6 historical-information allowance — and the anti-tuning rule applies: caps, semantic targets,
and expected verdicts are declared *before* pilot execution; any post-pilot change to them is itself
a must-fix requiring a C1 disposition.
**Adoption condition (path):** before adoption, CS must confirm the committed standing-rule path convention and the intended home for this addendum. This addendum proposes `governance/standing/`; the convention — including the never-confirmed committed path of `STANDING-REVIEW-DISCIPLINE.md` — is resolved in the adoption commit, not left open in the adopted text.

## 10. Non-authorizations

This addendum authorizes nothing. Specifically not: Lane 1a′ execution or new sweep_id; ladder
construction; model runs, re-runs, or new data generation; unconditioned token-prior runs; candidate
selection, ranking, or shortlisting; threshold-sheet population or lock; certification evaluation;
INT8/INT4 or stress-retention work; activation logging; multi-model execution; B1 v2.1
implementation; Paper 3 revision (any later incorporation into M3, D2 drafting, or a revised
manuscript is a separately authorized decision); Claim C activation; Fork A reactivation; Paper 6
activation; public benchmark packaging. All execution gates remain closed.

## 11. Adoption status

PROPOSED. Becomes standing only at Manager adoption (route step 5). Self-application check, per the
review standard: this addendum's own requirements were screened against its §6 rule — an ideal
instrument satisfies every requirement here (each has a non-empty pass region containing correct
instrument behavior), and each requirement carries its enforcement triple. Governing lesson, kept
from the source proposal: *a ruler must not only refuse false positives; it must also avoid being
shaped so badly that it rejects the ideal case.*

---

### Appendix T1 — Battery degeneracy audit (skeleton)
`policy_name | answerable_acc | null_acc | distinct_outputs | classification | declared_cap |
cap_exceeded | disposition` + `union_envelope_score | envelope_cap | room_below_envelope`

### Appendix T2 — Control semantics spec (skeleton)
`control_name | semantic_target | isolates | must_not_reward | bindings (preserved/scrambled/
removed/replaced) | scoring_target | expected_chance_rate | expected_ideal_behavior |
expected_shortcut_behavior | failure_interpretation | non_claim | implemented_by | conformance_check`

### Appendix T3 — Ideal-behavior pass-region checklist (skeleton)
`criterion | stratum | ideal_behavior | ideal_in_pass_region (Y/N) | confuses_ideal_with_universal
(Y/N) | strata_separated (Y/N) | perfect_model_eliminable (Y/N) | disposition (pass | revised |
diagnostic_only | justified_headroom_class)`

### Appendix T4 — Review-to-lock disposition table (skeleton)
`review_item_id | reviewer | risk_class | summary | disposition (incorporated | declined_with_
rationale | deferred_with_rationale_and_owner | superseded_by_stronger_control) | rationale | owner
| commit_or_file_reference | blocking_status`

— New Senior Engineer (to Team Lead for filter; then Senior review → CS review → Manager adoption)

[ADDENDUM TEXT ENDS]
