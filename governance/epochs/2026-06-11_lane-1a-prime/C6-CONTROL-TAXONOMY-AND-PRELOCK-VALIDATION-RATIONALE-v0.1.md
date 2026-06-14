# C6 Control Taxonomy and Pre-Lock Instrument Validation Rationale (v0.1)

```text
INTERNAL TECHNICAL CONSOLIDATION — NOT A PAPER, NOT A CLAIM-LEDGER PROMOTION
NO EXECUTION AUTHORIZED · NO MODEL INVOKED · NO SWEEP_ID CREATED
```

*New Senior Engineer, 2026-06-11, at Team Lead request. Governing distinction throughout:
**instrument validation ≠ model evaluation.** C6 is an instrument-validity framework. It asks
whether the ruler can distinguish retrieval-like behavior from its alternatives. It does not yet ask
whether the model has the target capability.*

## 1. Background: Lane 1a v1 failure mode

Lane 1a v1 executed cleanly and emitted a mechanical K=0 under locked rules. Post-run audit showed
the verdict was instrument-limited: three universal elimination labels were driven by the
instrument, not the behavior under test. (1) Two declared dummy policies degenerated into retrieval
oracles via self-match — `homogeneous_prefix_completion` on every rung, `target_recency` on K=low
rungs — saturating the union envelope at 1.000, and a floor against a 1.000 envelope is no floor.
(2) The control labeled token-prior in fact measured retrieval under scrambled bindings — a valid
control with a different semantic target, so candidate ≈ control was consistent with retrieval, not
with prior-driven emission, and the elimination label measured the mislabeling. (3) The abstention
band [0.50, 0.95] excluded perfect 1.000 NULL abstention: the criterion eliminated the ideal
witness. The run was archived as a fail-closed instrument-discrimination finding. It is cited here
solely in that capacity, and no v1 numeric level is evidence for Lane 1a′ viability, model
capability, task-family suitability, or candidate readiness.

## 2. Problem: retention and occupancy cannot be interpreted with an unvalidated instrument

The program's dependency chain runs: retention claims depend on certification; certification
depends on valid instruments; valid instruments depend on pre-lock operating-characteristic checks.
A fail-closed instrument has two error surfaces — too permissive (false certification: preserved
error read as preserved capability) and self-eliminating (false rejection: ideal behavior read as
failure). Paper 1 addressed the first surface; Lane 1a v1 demonstrated the second. An occupancy
question answered by an instrument that has not demonstrated both **can-fire** and
**cannot-always-fire** behavior is not answered: K=0 from a saturated envelope is a statement about
the envelope. Hence the standing rule adopted at
`governance/standing/PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM.md`: before retention, certify the
task; before certification, validate the instrument.

## 3. C6 contribution: the five-way control taxonomy

Contributor 6's proposal supplied three things the program adopted with credit. Conceptually: the
symmetric statement of the two error surfaces ("a ruler must not only refuse false positives; it
must also avoid being shaped so badly that it rejects the ideal case"). Operationally: the named
oracle-case battery (ideal retriever, declared shortcuts, token-prior emitter, universal answerer,
universal abstainer, NULL-on-NULL handler, malformed control — later extended with the mixture
oracle) and the five-question pass-region checklist. Structurally: the **five-type control
taxonomy** with the rule that semantic targets are locked before implementation, because the v1
defect was precisely a control whose code defined its meaning after the fact. The taxonomy's load-
bearing property is **non-interchangeability**: original-token targets, post-scramble-token
targets, null-context targets, and frequency-baseline targets answer different questions, and
substituting one for another silently changes what an elimination label means.

## 4. The five control/task categories

**4.1 `unconditioned_token_prior`** — semantic target: surface emission bias without task-relevant
bindings. Isolates: what the model emits when retrieval cannot resolve. Must not reward: retrieval
of any in-context binding. Binding handling: queried key absent, value bindings removed,
format-preserving shell ("unconditioned" = format-conditioned but binding-free, per the standing
taxonomy). Expected ideal behavior: at-chance correctness (or contract abstention, recorded
descriptively). Expected shortcut behavior: above-chance via surface/frequency bias. Failure
interpretation: candidate ≈ control separation below the declared margin is consistent with
prior-driven correctness. Lane 1a′ status: implemented as the approved pool-visible shell —
VALUE_POOL visible, global, |26|; baseline 1/26 derived from declared semantics and empirically
checked by the ideal-random-emitter oracle within drift tolerance; model generations remain closed
until D4 opens them by name. Non-claim: measures emission bias on this construction only; supports
no capability claim.

**4.2 `scrambled_binding_retrieval`** — semantic target: whether the model follows new bindings
after rebinding. Isolates: current-binding-following vs. stale-binding return. Must not reward:
prior-favored or stale values. Binding handling: queried key present, values re-shuffled,
post-scramble gold. Expected ideal behavior: high post-scramble correctness. Expected shortcut
behavior: stale or prior-favored values. Failure interpretation: informs interpretation only. Lane
1a′ status: retained under its honest name as a **strictly diagnostic, non-eliminating** control;
the mechanical rule — no elimination label may reference it, directly or indirectly — is
schema-enforced; generations closed until D4. Non-claim: its existence does not reinterpret or
rehabilitate any Lane 1a v1 control result; it supports no claim of retrieval capability,
viability, suitability, certifiability, or threshold readiness.

**4.3 `null_context_control`** — semantic target: behavior when task-relevant context is absent.
Isolates: the model's no-evidence default (answering vs. abstaining). Must not reward: confident
answering without evidence. Binding handling: context removed or task-irrelevant. Expected ideal
behavior: contract abstention. Expected shortcut behavior: fluent confident answering. Failure
interpretation: over-answering under absent context. Lane 1a′ status: **not separately
instantiated**; its function is covered by two existing structures — the NULL stratum (16
items/rung whose correct operation is abstention, with the floor/ceiling criterion pair whose pass
region contains the ideal corner by construction) and the unconditioned shell (which is a
null-binding prompt). A standalone null-context control is a documented future option, not a gap:
the taxonomy requires the *function* be covered and honestly named, not that all five be separately
built. Non-claim: NULL-stratum behavior is contract compliance on this construction, not an
abstention-capability claim.

**4.4 `copy_surface_control`** — semantic target: whether surface span copying can solve the item.
Isolates: copy/echo resolution. Must not reward: genuine retrieval (it must detect copying, not
perform lookup). Binding handling: bindings preserved; the policy operates on surface form only.
Expected ideal behavior: agreement with the copy pattern at structural-coincidence rates only.
Expected shortcut behavior: high agreement. Failure interpretation: candidate outputs explainable
by copying. Lane 1a′ status: implemented as `copy_completion`, deliberately **outside the
accuracy-union envelope** — it is an agreement-rate diagnostic (per-item agreement between
candidate output and the copy pattern), because a low-accuracy policy inside an accuracy envelope
detects nothing. Non-claim: agreement is descriptive; non-agreement is not a cleanliness
certificate.

**4.5 `dummy_policy_control`** — semantic target: whether a declared non-operational policy
explains performance. Isolates: structural shortcuts (position, recency, prefix-neighborhood).
Must not reward: the target operation — this is the category where v1 failed, so Lane 1a′ adds the
definition-layer rule: **policy matching functions are blinded to exact queried-key identity**.
Expected ideal behavior: candidate accuracy separated above the policy envelope. Expected shortcut
behavior: candidate within the envelope. Failure interpretation:
`accuracy_indistinguishable_from_declared_policy_envelope`. Lane 1a′ status: the corrected
four-policy envelope battery (`pure_last_position`, `salient_endpoint`,
`recency_excluding_target`, `prefix_neighbor_confusion` as a total function) under per-policy cap
0.50, envelope cap 0.80, operation-equivalence reclassification with lock-time hard refusal
(IS-8), and A6 final-manifest re-verification with drift tolerance 0.05 — all
[SWEEP-PARAMETER] declarations made pre-pilot. Standing rule, verbatim: **non-constant ≠
non-degenerate; a policy that scores 100% on answerable items is the operation, not evidence of the
operation's absence.** Non-claim: a quiet battery is evidence about the battery and manifest
geometry, not candidate virtue.

## 5. Why each category tests a different failure explanation

Each control eliminates one alternative explanation for retrieval-shaped output: the token-prior
control asks *would it have said this anyway* (priors); the scrambled control asks *is it reading
the current bindings or remembering old ones* (staleness); the null-context function asks *does it
answer when there is nothing to read* (over-answering); the copy control asks *is the answer just
the question's surface again* (echo); the dummy battery asks *does a position/recency/neighbor rule
produce the same answers* (structure). These are not substitutable because their reference targets
differ — v1's incident was exactly a category-4.2 measurement wearing a category-4.1 name, and the
elimination logic inherited the wrong meaning. One construction can cover a category's function
(4.3), but no artifact may carry a category name whose declared semantic target its code does not
implement.

## 6. How Lane 1a′ implements the taxonomy

The taxonomy enters Lane 1a′ at three layers. **Specification:** every control carries the full T2
field set, locked before code; the two model-touching controls are declared with their eliminative
status fixed (token-prior: referenced by one criterion; scrambled: referenced by none, mechanically).
**Schema:** the descriptive serialized labels are the only wire vocabulary; the
no-reference-to-scrambled rule and the no-`passes_*` rule are enforced at type/schema level with
source-level checks. **Outcome semantics:** three-way totality (INCONCLUSIVE | ELIMINATED |
NOT_RULED_OUT) with the equality predicate and K bound to "not ruled out"; the uniform comparison
principle — elimination requires the full confidence interval on the eliminating side; uncertainty
resolves toward NOT_RULED_OUT, never toward elimination — with `boundary_proximity_flag` as the
diagnostic-only record of straddling cases.

## 7. Pre-lock validation role: ideal witness, oracle cases, mixture oracle, dummy policies

The pre-lock stack answers four questions before anything is trusted. The **ideal witness** answers
*can a perfect model survive this instrument* — the specification is declared and locked before any
checklist, and the T3 screens (dead / tautological / malformed) plus the computable coherence check
(at the ideal NULL corner, Wilson [0.806, 1.000] can never sit below a sane floor) make
self-elimination structurally impossible rather than hoped-against. The **oracle cases** answer
*does each detector fire where it must and stay quiet where it must* — can-fire and
cannot-always-fire demonstrated on declared cases with `expected_verdict` locked before pre-flight.
The **mixture oracle** answers *does the instrument behave sensibly on blended behavior* — real
candidates are not pure cases, and its blend fraction, components, and expected verdict are
declared before execution. The **dummy-policy audit** answers *did any detector become the
operation* — pilot execution, caps, classification, and final-manifest re-verification. Passing all
four shows lock-eligibility on declared cases only — the E16 non-claim — never general validity.

## 8. Governance boundaries and non-claims

C6 does not currently establish: model capability; model incapability; candidate viability;
threshold readiness; certification readiness; retention under compression; Claim C; a seam; a
public benchmark claim. **Lane 1a′ may rule out. Lane 1a′ may not rule in.** All validation
artifacts are `SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION`, usable only to
determine lock-eligibility; a Validation Report PASS is pre-lock adequacy on declared cases,
pilots, and required checks only — not candidate evidence, not general field validity, not
certification evidence, not threshold support. The classifier/certifier boundary stands: Lane 1a v1
demonstrated a false-reject mechanism in a reconnaissance classifier; it did not measure the
false-reject rate of any Paper 3 certification gate, and no formalized Paper 3 certification gate
has yet been exercised.

## 9. Current implementation status under D2

C6 proposal: absorbed into the Lane 1a′ instrument-validation stack (with credit, per the Senior
routing recommendation). D2: approved. Joint dispositions (INH-1/2/3, prompt shell): approved.
Code implementation: CS-owned, in flight. Model-free validation: authorized under D2 boundaries
with the execution-ledger requirement. Model runs: not authorized. Sweep execution: not authorized.
sweep_id: not created. D3 / D4 / D5: not approved. Evidence-discipline separation maintained:
adopted governance (the standing addendum) ≠ design declarations (caps, comparison rules, specs —
made, not yet exercised) ≠ model-free validation artifacts (authorized, not yet produced) ≠ future
model execution (D4, closed) ≠ future compression-stress evidence (not in this lane at all).

## 10. Open questions before D3 / D4

(1) Joint expected-verdict declaration for every oracle case including the mixture oracle — locked
before any pre-flight executes. (2) Whether the declared caps (0.50 / 0.80 / drift 0.05) survive
pilot contact — any post-pilot change is a must-fix with C1 disposition. (3) The packet's single
tokenizer+canonicalization identity, declared by name and version in T1. (4) LOCK-RECORD v0.3
extension (`control_prompt_shell_hash`) concurrence. (5) T3 criterion bound values
[SWEEP-PARAMETER] at packet lock. (6) The D4 decision itself: token-prior generations opened by
name, never by bundle — the only model-touching question this framework will eventually pose.

---

**Source documents:** Lane 1a Close-Out v1.1/v1.2 (findings A/B/C); C6 proposal ("Instrument
Pre-Flight Hardening Packet"); Senior routing recommendation; Pre-Lock Instrument Validation
Addendum (adopted, `e76e7f8`, sha256 `124f6046…`); Lane 1a′ Design Proposal v0.2 (D1-approved);
D1/D2 design-packet bundles v0.2/v0.3; CS-PROPOSED-DISPOSITIONS (`acf73a3`); NS co-review; the
Manager/Team Lead joint-disposition approval; D2 Approved Dispositions & Validation Prerequisites
v0.1.

**Non-claim block:** this write-up is an internal consolidation of instrument-validity reasoning.
It contains no model evidence, no candidate evidence, no occupancy evidence, no retention evidence,
and supports no claim beyond the documented governance and design record it cites.

**Confirmations:** no execution occurred; no model was invoked; no sweep_id was created.

— New Senior Engineer
