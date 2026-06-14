# Lane 1a′ Design Proposal — Corrected Reconnaissance Sweep With Pre-Lock Instrument Validation (v0.2)

*v0.1 → v0.2 changelog (consolidated five-reviewer round, 22 required edits):* occupancy question
reworded to exclude positive-selection implication (E3); construction-failure language softened (E1);
N=96 marked proposed-not-locked (E2); operation-equivalent consequence (E4); `prefix_neighbor_confusion`
made a total function (E5); `copy_completion` moved outside the union envelope as an output-pattern
diagnostic (E6); envelope-inversion non-claim (E7); `scrambled_binding_retrieval` non-claim strengthened
+ mechanical prohibition (E8–E9); token-prior generations explicitly not design-authorized (E10);
baseline derived from shell visibility (E11); "unconditioned" defined per standing taxonomy (E12);
K=0 outcome semantics tightened (E13); non-eliminated-rung non-claim (E14); symmetric finality (E15);
T4 pre-populated with three inherited open items (E16); B1-equivalent provenance enumerated (E17);
mixture-oracle blend/components/verdict pre-declared (E18); A6 drift check (E19); offline pilot
validation not authorized by this proposal (E20); v1 numerics diagnostic-only (E21); §1 wording (E22).
Plus: seven packet-stage concerns carried forward; "no positive use" block added after §10;
survivor→non-eliminated-rung wording where practical.*

*New Senior Engineer, 2026-06-11. Team Lead drafting assignment of 2026-06-11. Design proposal only:
no execution, no model runs, no data generation, no implementation, no new sweep_id. Route: this
draft → Team Lead filter → Senior advisory if needed → CS implementability review → Manager design
authorization. Status sentence, per assignment §5: **Lane 1a′ is a proposed corrected reconnaissance
design.** Nothing more is claimed.*

> **Before retention, certify the task. Before certification, validate the instrument.**

## 1. Purpose and scope

Return to the original Lane 1a question with a corrected instrument: *Can a properly validated reconnaissance sweep determine whether any region is not eliminated under pre-registered negative-use diagnostics, without ranking or positively supporting that region for candidate selection?* Lane 1a v1 did not answer it — the instrument over-eliminated
(three universal labels driven by instrument-side artifacts), so K=0 stood mechanically while the
occupancy question stayed open. Lane 1a′ keeps everything v1 proved sound — the doctrine, the
governance chain, the fail-closed containment that let an instrument failure burn nothing
downstream — and applies the now-standing Pre-Lock Instrument Validation Addendum to the instrument design (`governance/standing/`, commit `e76e7f8`). Doctrine unchanged and verbatim: **Lane 1a′
may rule out; it may not rule in.** All v1 negative-use, label, plotting, serialization,
no-re-execution, sidecar-attestation, and consumption-side rules are inherited intact.

## 2. Lessons inherited from Lane 1a v1

**Instrument lessons (the three failures, each corrected in §§5–7):** (A) two dummy policies
degenerated into retrieval oracles via self-match, saturating the union envelope at 1.000 —
*non-constant ≠ non-degenerate; a policy that scores 100% on answerable items is the operation, not
evidence of the operation's absence;* and *a floor against a 1.000 envelope is no floor.* (B) the
"token-prior" control actually measured retrieval under scrambled bindings — control semantic
targets are not interchangeable and must be locked before code. (C) the abstention band excluded
ideal NULL discipline — a rule whose pass region excludes ideal behavior is malformed.
**Architecture lessons (kept):** the standalone generation runner with B1-equivalent provenance discipline — enumerated and checkable, not asserted: runner attestation; artifact hashes; append-only audit log; lock/access timestamps; sidecar records; model identity; prompt/config identity; raw output preservation; no wrapper-rewrite of runner-attested outputs — and sidecar attestation (B1 v2 cannot consume this manifest family — established, not
re-litigated); the interface-contract / production-path smoke test; the G1-open production rule;
ladder-order execution; append-only audit; locked plotting with code-level refusals.
**Scope guard (standing, verbatim):** Lane 1a demonstrated a false-reject mechanism in a
reconnaissance classifier. It did not measure the false-reject rate of any Paper 3 certification
gate, and no formalized Paper 3 certification gate has yet been exercised. Lane 1a v1 numeric levels may be referenced only as instrument-failure diagnosis; they may not be used as evidence for Lane 1a′ viability, model capability, task-family suitability, or candidate readiness.

## 3. Requirement-inheritance screen under R6

Per the installed R6 (STANDING-REVIEW-DISCIPLINE.md): prior-lane requirements screened for
portability — **Adopted:** the entire Pre-Lock Instrument Validation Addendum (A1–A6, B1–B4, C1–C3,
containment/anti-tuning, labeling, report non-claim) — mandatory as standing governance, and this
lane is its first applied instance; Paper 3 D2 battery-sensitivity ancestor (already completed by
the addendum); Lane 1a v0.3 design doctrine, label vocabulary, output schema constraints, plotting
restrictions, winner's-curse and consumption-side rules; the no-re-execution rule with audit
attempt counts; G1 delivery and review-enumeration rules. **Adapted with rationale:** the v1 dummy
battery (two policies redefined, §5) and the v1 control set (renamed and split, §6) and the
abstention criterion (re-formed, §7). **Declined with rationale:** none — no applicable prior-lane
requirement is dropped.

## 4. Proposed task family and rung structure

Inherited from v0.3 with revalidation. Lane 1a v1 did not establish that the construction was the failure; the primary identified failure was instrument-side — so the construction is carried forward as a working basis subject to the same revalidation as everything else, not as proven sound: single-hop
key→value retrieval over freshly constructed synthetic entity manifests; the 8-rung ladder L01–L08
over distractor count **D** ∈ {4, 8, 16} × key confusability **K** ∈ {low, high} × context load
**X** ∈ {base, extended}; neutral rung IDs; N=96/rung (80 answerable + 16 NULL) is carried as the current proposal, not as a locked design constant — final N, answerable/NULL split, and void budget must be confirmed during packet preparation and instrument validation; per-rung void budget; manifest recipe per §13 v0.2 **plus** the
declared padding placement (padding prepended; the real-pair block is the recency-relevant tail;
policies compute over the full visible context) and the two-tier novelty rule (program-internal
overlap tolerance exactly zero). All recipe constants remain sweep parameters, never thresholds.

## 5. Diagnostic battery design (correction A)

Standing rule, verbatim:

> **Non-constant ≠ non-degenerate.**
> **A policy that scores 100% on answerable items is the operation, not evidence of the operation's
> absence.**

Design rule installed at the definition layer: **policy matching functions are blinded to exact
queried-key identity** — a declared shortcut models what a model might do *instead of* retrieval,
so no policy may resolve the target by self-match. The proposed battery:
- `pure_last_position` — value of the last visible pair (unchanged; behaved correctly in v1).
- `salient_endpoint` — value at the declared salient endpoint (unchanged).
- `copy_completion` — a candidate-output-pattern diagnostic **outside the union envelope** unless a separate pre-registered agreement-rate diagnostic is defined: its detection mechanism is per-item agreement between candidate output and the copy pattern, not accuracy, so it does not sit as a low-accuracy policy inside an accuracy-union envelope.
- `recency_excluding_target` — **replaces** `target_recency`: value of the most recently listed
  pair *excluding the exact queried key*; models recency bias without the self-match oracle.
- `prefix_neighbor_confusion` — **replaces** `homogeneous_prefix_completion`: value of the nearest
  shared-prefix *neighbor*, queried key excluded; models exactly the K=high confusion shortcut the axis exists to probe (answering with a confusable
neighbor's value). Total-function definition: (1) exact queried-key self-match is excluded; the
equality predicate is token-id-sequence equality after tokenizer canonicalization, unless CS proposes
a stricter implementable rule; (2) ties among shared-prefix neighbors resolve to the most recent
neighbor in the visible context; (3) if no eligible shared-prefix neighbor exists (typical on K=low
rungs), the policy emits a declared no-match output; (4) undefined/no-match predictions score
incorrect and contribute nothing to the union envelope unless separately declared as a diagnostic
case — structural undefinedness on K=low is therefore impossible by definition, not by hope.
Validation per the standing addendum, all offline: pilot-manifest battery execution (A1);
per-policy accuracy caps declared pre-pilot with rationale (A2); union-envelope cap with declared
measurement room (A3); operation-equivalent / degenerate classification with coverage recomputation
(A4); oracle-case pre-flight including the **synthetic ideal retriever**, every declared policy, a
token-prior emitter, universal answerer, universal abstainer, NULL-on-NULL handler, one malformed
control, and **at least one mixture oracle** (operation-correct behavior blended with declared
shortcut behavior at a pre-declared fraction; expected verdict — detect, pass, or
flag-indeterminate — locked before pre-flight) (A5 + E5/E17) — the mixture oracle pre-declares its blend fraction, its component behaviors, and
its expected verdict before pre-flight execution; **final-manifest re-verification of all caps
before lock** (A6), which must compare pilot and final per-policy scores and union-envelope scores
and flag drift. **Operation-equivalence consequence:** if any declared negative dummy policy becomes
operation-equivalent on pilot or final manifests, it must be removed from the negative battery or
reclassified as a positive oracle before lock; it may not remain in the union envelope.
**Envelope-inversion non-claim:** a quiet declared-policy battery is evidence about the declared
battery and manifest geometry, not evidence of candidate virtue. A low or non-saturated union
envelope may not be used to claim shortcut resistance, model capability, task-family viability,
candidate suitability, certification readiness, or threshold readiness. Offline validation execution only — none of this authorizes model
execution, candidate evaluation, certification evaluation, or data generation.

## 6. Control semantics design (correction B)

Two controls, each fully specified per T2 before any code, targets non-interchangeable by rule:

**`unconditioned_token_prior`** — semantic_target: surface emission bias without task-relevant
bindings. Isolates: what the model emits when retrieval cannot resolve. Must not reward: retrieval
of any in-context binding. Binding handling: queried key **absent** and value bindings **removed**
(format-preserving prompt shell; closer to null-context than to rebinding). Scoring target: gold
value of the mirrored answerable item. Expected baseline: derived from the declared prompt-shell visibility, value pool, and scoring contract — if the value pool remains visible in the shell, chance may approximate 1/|value_pool|; if values are removed or real-word priors dominate, the expected baseline must be declared from the actual control semantics rather than assumed. Here, "unconditioned" follows the standing taxonomy: format-conditioned but binding-free, without task-relevant bindings. Expected
ideal-model behavior: at-chance correctness (or contract abstention, recorded descriptively).
Expected shortcut-model behavior: above-chance only via surface/frequency bias. Failure
interpretation: candidate-vs-control separation below the pre-registered descriptive margin is
consistent with prior-driven correctness. Non-claim: measures emission bias on this construction
only; supports no capability claim.

**`scrambled_binding_retrieval`** — retained from v1 under its honest name, **diagnostic-only and
non-eliminating**: semantic_target: whether the model follows new bindings after rebinding. Binding
handling: queried key present, values re-shuffled, post-scramble gold. Expected ideal behavior:
high correctness (follows current bindings). Expected shortcut behavior: returns stale or
prior-favored values. Failure interpretation: informs interpretation only; produces, influences,
and triggers no elimination label. Non-claim: `scrambled_binding_retrieval` is strictly diagnostic and non-eliminating. Its outputs
may inform interpretation, but they produce no elimination label and support no claim of retrieval
capability, task-family viability, candidate suitability, certifiability, or threshold readiness;
per the standing taxonomy sentence, this control's existence does not reinterpret or rehabilitate
any Lane 1a v1 control result. **Mechanical rule: no elimination label may reference
`scrambled_binding_retrieval`, directly or indirectly.**

**Design authorization does not authorize token-prior generations.** Token-prior generations remain closed until Manager opens them by name at the sweep execution gate (§12 D4). The v1 defect is structurally unrepeatable here: no label may reference a control whose declared
semantic_target differs from the label's name, checked at T2 review before implementation.

## 7. Abstention and NULL-contract design (correction C)

**Ideal-witness specification (declared, reviewed, and locked before any pass-region checklist):**
ideal answerable behavior — correct value, strict format contract (single-line answer per the
locked template); ideal NULL behavior — the contract abstention string, same format; abstention
behavior — abstain on every NULL item, answer on every answerable item. **Criterion re-form:** the
v1 two-sided band is replaced by two separately evaluated, separately pre-registered conditions
whose joint pass region **contains the ideal corner (NULL abstention 1.0, answerable abstention
0.0) by construction**: (i) NULL-stratum abstention at or above a declared floor (catches
never-abstains); (ii) answerable-stratum abstention at or below a declared ceiling (catches
over-abstention). Perfect NULL abstention is never labeled unstable. Every criterion in the packet
passes the T3 checklist — including question 5, *could a perfect model be eliminated by this rule?*
(answer must be No unless the rule is the declared measurement-resolution/headroom exception) — and
the dead / tautological / malformed screens, with the standing rule that Manager
decline-with-rationale cannot preserve an ill-formed criterion in an active eliminative path.

## 8. Instrument validation plan

Sequence (all offline, all pre-lock, per the standing addendum): pilot manifests drawn under the
locked recipe → A1 battery execution → A2/A3 cap checks → A4 classification → A5 oracle pre-flight
with locked `expected_verdict` per case → B1/B2 control-spec review (T2) → ideal-witness lock → B4
pass-region checklist (T3) → C1 dispositions of every must-fix (T4) → A6 final-manifest
re-verification → Instrument Validation Report sealed with the packet. Pilot iteration logging per
E11 (every failed pilot retained; a passing final battery erases nothing); anti-tuning rule in
force (caps, targets, and expected verdicts declared before pilot execution; post-pilot changes are
must-fix events); artifact labels per E15 (`SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION`
on oracle/pilot artifacts; `RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION` on sweep
outputs). Report-level non-claim per E16 verbatim. **T4 pre-population (inherited open items):** the
initial Lane 1a′ T4 table must include, for disposition before lock: (1) per-diagnostic stratum
semantics — which diagnostics compute over 96 / 80 / 16, and which use per-stratum N_effective;
(2) outcome-chooser totality — survivor predicate, RFI-only behavior, inconclusive class, and fixed
language; (3) SE interval method — Wilson, Jeffreys, or other, never silently Wald. The lane whose
founding incident was a filed must-fix with no disposition does not begin by silently inheriting
unresolved items. **This proposal defines offline pilot validation requirements but does not authorize pilot execution; pilot validation requires later packet-stage authorization (§12 D2). A Validation Report PASS authorizes nothing; it is a precondition for requesting execution authorization, not a substitute for it.**

## 9. Required artifacts (T1–T4; defined here, executed never under this proposal)

T1 — Battery degeneracy audit (per-policy scores incl. NULL stratum, distinct outputs,
classification, caps, envelope, final-manifest re-verification block). T2 — Control semantics
specification (full field set for both §6 controls). T3 — Ideal-witness / pass-region checklist
(one row per criterion; ill-formed-class screens). T4 — Review-to-lock disposition table (every
must-fix: incorporated / declined-with-rationale / deferred-with-rationale-and-owner /
superseded-by-stronger-control; deferred items enter the next packet's R6 screen). **All four are
required before any future lock or execution and are sealed in the Instrument Validation Report.**

## 10. Failure-mode review (standing question applied)

*Assume approval, disciplined implementation, and a downstream failure anyway.* The most credible
residual path: the corrected battery passes validation, the sweep runs, and **K=0 fires again — this
time under a validated instrument — and the team treats it as the same non-result as v1**, leaving
the lane in a loop; or its dual, a non-eliminated set emerges and non-elimination quietly hardens into pre-selection. Pre-registered outcome semantics close both sides. **K=0 side:** under a sealed Validation Report,
a K=0 outcome constitutes the lane's pre-registered substantive reconnaissance-negative finding for
this task family at this scale, for this construction. It is not a Paper 3 certification verdict and
not evidence of model incapability. **Non-eliminated side:** a non-eliminated rung is not promising,
viable, candidate-ready, near-certifiable, or suitable for positive selection. **Symmetric
finality:** a validated K=0 outcome is not relitigated into instrument failure absent a documented
new instrument defect; a non-eliminated outcome is not relitigated into positive selection, ranking,
candidate readiness, or certification evidence absent separately authorized downstream processes.
The pre-selection side additionally inherits v1's full structural set (unordered non-eliminated-set
serialization, no rank fields or computations, fixed language, single-non-eliminated-rung sentence,
consumption-side attestation). Remaining named risks: (i) the corrected
policies could still harbor an undeclared degenerate mode — mitigated by the mixture oracle, the
pilot execution requirement, and A6; residual honestly nonzero and bounded by validation rather
than hope; (ii) validation-as-tuning — blocked by the anti-tuning rule and E11 retention; (iii) the
`unconditioned_token_prior` control requires model generations at sweep time and touches the
standing token-prior Manager gate — named as a §12 decision point so it is opened by name, never by
bundle; (iv) transfer/review-chain failures — covered by the installed C2 enumeration rule and the
G1-open production rule, both of which this lane's chain must satisfy at every gate-closing review.

**No positive use (standing for this lane):** no Lane 1a′ output — label, diagnostic, control
number, validation result, or report — may be used as positive evidence for any model, construction,
candidate, threshold, or certification purpose. Outputs rule out or they say nothing.

**Packet-stage concerns carried forward (not v0.2 blockers):** (1) exact prompt-shell content for
`unconditioned_token_prior`; (2) concrete manifest-schema labeling of the real-pair-block boundary;
(3) mixture-oracle commit-and-hash ceremony; (4) exact mechanics of A6 final-manifest
re-verification; (5) synthetic ideal-witness record format; (6) pilot-iteration logging
schema/template location; (7) validation artifact labels and threshold/certification exclusion in
the evidence bundle.

## 11. Execution non-authorizations

This proposal authorizes nothing: no new sweep_id, no model runs, no data generation, no execution
packet, no pilot execution (itself authorized at the packet stage, offline), no candidate selection
or ranking, no threshold-sheet work, no certification evaluation, no stress-retention testing, no
B1 v2.1 implementation, no Paper 3 revision, no Claim C activation, no Fork A reactivation, no
Paper 6 activation, no public benchmark packaging. All execution gates remain closed. Per
assignment §5, this proposal does not claim that Lane 1a′ will find a survivor, that the task
family is viable, that the model is capable or incapable, that certification is near, or that
threshold or retention work is authorized.

## 12. Manager decision points

D1 — Design authorization (this proposal, after Team Lead filter and CS implementability review).
D2 — Packet preparation authorization (design packet + CS execution packet, including offline pilot
and oracle validation under the standing addendum). D3 — Instrument Validation Report acceptance
(Team Lead review; sealed T1–T4). D4 — Sweep execution authorization. Design authorization (D1) does not authorize token-prior generations; they remain closed until this gate, which must **by name** include or decline the `unconditioned_token_prior` control generations under the standing
token-prior gate (open by name, never by bundle), bind to the sealed LOCK-RECORD hash, and follow
the G1-open and review-enumeration rules. D5 — Close-out acceptance with pre-registered outcome
semantics per §10. Each gate is independent; passing one authorizes nothing beyond it.

— New Senior Engineer (to Team Lead for filter; G1 enumeration accompanies delivery)
