# Lane 1a′ Design-Packet Bundle (v0.3 — D2 package assembly)

*v0.3 changes (D2 package assembly):* re-bannered per Team Lead §6; design-side slots added for
IS-7 (pre-declared drift tolerance placeholder in the T1 A6 block), IS-8 (operation-equivalence
lock-time hard refusal noted as a code-level CS mechanism mirroring the I.4 consequence), and IS-9
(CS equality-predicate veto path reserved in I.4); cross-review record against CS-EP v0.2 /
LOCK-RECORD v0.2 added as Part IX; AL-INH-1/2 co-ownership confirmed (already in T4 since v0.2).
*v0.2 changes:*
*1. Clarified D2 references as future-review references only.*
*2. Added directory-name / sweep_id boundary.*
*3. Added CS co-ownership for INH-1 and INH-2.*
*4. Clarified Wilson as proposed, not selected.*

```text
DRAFT / REVIEW ONLY
D2 PACKAGE-ASSEMBLY ARTIFACT
NO D2 AUTHORIZATION GRANTED
NO EXECUTION AUTHORIZED
NO SWEEP_ID CREATED
NO MODEL RUNS
NO DATA GENERATED
NO VALIDATION OUTPUTS POPULATED
```

*New Senior Engineer, 2026-06-11. Per Team Lead D1 assignment. Contents: Part I — Design Packet
draft; Parts II–V — T1–T4 plans; Part VI — open issues and Manager decision points; Part VII —
interface questions for CS. Every result field in every table is intentionally empty. Route: Team
Lead filter → CS implementability alignment → Manager D2 review. D2 is not requested here.*

---

## Part I — Lane 1a′ Design Packet (draft)

**I.1 Doctrine and scope (verbatim, inherited).** Lane 1a′ may rule out; it may not rule in. No
survivor ranking; no positive candidate-selection inference; no threshold use; no certification
evidence; no Claim C activation. The occupancy question as D1-approved: *can a properly validated
reconnaissance sweep determine whether any region is not eliminated under pre-registered
negative-use diagnostics, without ranking or positively supporting that region for candidate
selection?* No-positive-use rule: outputs rule out or they say nothing.

**I.2 R6 inheritance screen (instantiated).** ADOPTED: the Pre-Lock Instrument Validation Addendum
in full (first applied instance — A1–A6, B1–B4, C1–C3, anti-tuning, E11 pilot-iteration retention,
E15 labels, E16 report non-claim); Lane 1a v0.3 doctrine, label vocabulary, schema constraints
(no rank/preference/best fields; `additionalProperties: false`; unordered non-eliminated-set
serialization in rung-ID order), plotting restrictions with code-level refusals, ladder-order
execution, no-re-execution rule with audit attempt counts, winner's-curse and consumption-side
rules, sidecar attestation; G1-open production rule; C2 review-enumeration rule; Path Conventions;
sibling-artifact cross-reference rule; production-path subprocess smoke rule. ADAPTED with
rationale: dummy battery (I.4), controls (I.5), abstention criterion (I.6). DECLINED: none.

**I.3 Task family, ladder, recipe.** Single-hop key→value retrieval, fresh synthetic manifests;
8-rung ladder L01–L08 over D ∈ {4,8,16} × K ∈ {low,high} × X ∈ {base,extended}; neutral IDs.
Construction carried as working basis, not proven sound (v1 established the instrument as the
primary identified failure, nothing more). N=96/rung (80/16) carried as proposal, not locked; final
N, split, and void budget confirmed at packet validation. Recipe: §13 v0.2 lineage plus declared
padding placement (prepended; real-pair block is the recency tail; policies compute over full
visible context), two-tier novelty (program-internal overlap = 0), per-item answer-slot recording,
deterministic seeds in the LOCK-RECORD. All constants are sweep parameters, never thresholds.

**I.4 Diagnostic battery (corrected; full text per D1-approved v0.2 §5).** Standing rule verbatim:
**Non-constant ≠ non-degenerate. A policy that scores 100% on answerable items is the operation,
not evidence of the operation's absence.** Definition-layer rule: policy matching functions are
blinded to exact queried-key identity. Battery: `pure_last_position`; `salient_endpoint`;
`recency_excluding_target`; `prefix_neighbor_confusion` with the total-function definition
(self-match excluded via token-id-sequence equality after tokenizer canonicalization unless CS proposes stricter — IS-9: CS retains a reserved veto/stricter-rule path on this predicate through packet review; most-recent-neighbor tie-break; declared no-match output scoring incorrect and
outside the envelope; K=low undefinedness impossible by definition); `copy_completion` **outside
the union envelope** as a candidate-output-pattern (agreement-rate) diagnostic unless a separate
pre-registered diagnostic is defined. Operation-equivalence consequence: a negative dummy that
becomes operation-equivalent on pilot or final manifests is removed or reclassified as a positive
oracle before lock; it may not remain in the union envelope. (IS-8: CS implements this as a lock-time hard refusal at code level — a battery containing an operation-equivalent policy cannot seal.) Envelope-inversion non-claim carried
verbatim (a quiet battery is evidence about the battery and manifest geometry, not candidate
virtue).

**I.5 Controls (full specs in Part III).** `unconditioned_token_prior` — format-conditioned but
binding-free per the standing taxonomy; baseline derived from declared prompt-shell visibility,
value pool, and scoring contract, never assumed. `scrambled_binding_retrieval` — strictly
diagnostic and non-eliminating; **no elimination label may reference it, directly or indirectly**
(mechanical rule, schema-enforced at packet stage). Design authorization does not authorize
token-prior generations; they remain closed until Manager opens them by name at D4.

**I.6 Abstention / ideal witness.** Ideal-witness specification locked before any checklist run
(record format in Part IV): perfect retrieval on answerable, contract abstention on NULL, strict
format throughout. Criterion form: two separately pre-registered one-sided conditions (NULL-stratum
abstention ≥ declared floor; answerable-stratum abstention ≤ declared ceiling); the ideal corner
(1.0 / 0.0) is inside the pass region by construction; perfect NULL abstention is never labeled
unstable. All criteria pass the T3 screens (dead / tautological / malformed; B4-Q5 with the
headroom-exception-only No rule); Manager decline-with-rationale cannot preserve an ill-formed
criterion in an active eliminative path.

**I.7 Label vocabulary, outputs, plotting.** Inherited from v1 v0.3 unchanged: the seven
descriptive labels (with criteria re-derived per I.4–I.6 and the corrected referents); inconclusive
preempts; equality survivor predicate; fixed outcome language including the single-non-eliminated-
rung sentence; two figure types only, manifest-ID ordering, categorical markers, code-level
prohibition refusals; artifact tags `RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION`
on sweep outputs and `SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION` on oracle/pilot
artifacts. Outcome semantics per v0.2 §10 verbatim (reconnaissance-negative finding; non-eliminated
non-claims; symmetric finality).

**I.8 Provenance (enumerated, auditable).** Runner attestation; artifact hashes; append-only audit
log; lock/access timestamps; sidecar records; model identity; prompt/config identity; raw-output
preservation; **no wrapper-rewrite of runner-attested outputs.** Standalone generation runner
(B1 v2 untouched and unused — established); interface-contract test and production-path subprocess
smoke test required in the CS execution packet before any lock.

---

## Part II — T1 Battery Degeneracy Audit Plan (draft; result fields empty)

Declarations to be fixed pre-pilot with rationale (anti-tuning rule applies): per-policy accuracy
cap (per battery, value TBD at packet stage with statistical rationale); union-envelope cap with
declared measurement room; classification rules
(`discriminative | operation_equivalent | degenerate_constant | structurally_undefined`); battery
coverage minimum over discriminative policies only. Audit table (empty):
`policy | answerable_acc | null_acc | distinct_outputs | classification | declared_cap |
cap_exceeded | disposition` per rung-class, plus
`union_envelope_score | envelope_cap | room_below_envelope`, plus the **A6 drift block**: `pilot_score vs final_manifest_score per policy | envelope_pilot vs envelope_final | drift_flag | declared_drift_tolerance (IS-7: pre-declared at packet stage with rationale, before any pilot — empty here)`.
Oracle pre-flight case list (expected_verdict column empty until declared, then locked pre-flight):
synthetic ideal retriever; each declared policy; token-prior emitter; universal answerer; universal
abstainer; NULL-on-NULL handler; one malformed control; **mixture oracle** (blend fraction,
component behaviors, expected verdict all pre-declared). Pilot iteration log fields per E11.

## Part III — T2 Control Semantics Specification Plan (draft)

Two spec sheets, all declaration fields drafted (these are design declarations, not validation
outputs); conformance/result fields empty:

| field | unconditioned_token_prior | scrambled_binding_retrieval |
|---|---|---|
| semantic_target | surface emission bias without task-relevant bindings | binding-following after rebinding |
| isolates | what the model emits when retrieval cannot resolve | whether current bindings are followed |
| must_not_reward | retrieval of any in-context binding | stale/prior-favored value return |
| binding handling | queried key absent; value bindings removed; format-preserving shell | key present; values re-shuffled; post-scramble gold |
| scoring target | gold value of mirrored answerable item | post-scramble gold |
| expected baseline | derived from declared shell visibility / value pool / scoring contract (≈1/\|pool\| only if pool visible; declared, never assumed) | n/a (diagnostic) |
| expected ideal behavior | at-chance correctness or contract abstention (descriptive) | high correctness |
| expected shortcut behavior | above-chance via surface/frequency bias only | stale or prior-favored values |
| failure interpretation | candidate≈control consistent with prior-driven correctness (descriptive margin) | informs interpretation only |
| eliminative status | referenced by elimination criteria per T3 | **none — mechanical rule: no elimination label may reference it, directly or indirectly** |
| non-claim | measures emission bias on this construction only; no capability claim | strictly diagnostic; no capability/viability/suitability/certifiability/threshold claim; does not rehabilitate any v1 result |
| "unconditioned" definition | format-conditioned but binding-free (standing taxonomy) | — |

Open declaration carried to Part VI: exact prompt-shell content (value-pool visibility decision
drives the baseline derivation).

## Part IV — T3 Ideal-Witness / Pass-Region Checklist Plan (draft)

Ideal-witness record format: per-stratum synthetic record
`{stratum, item_id, output, format_compliant: true, abstained: per contract}` — answerable: gold
value, strict format; NULL: contract abstention string. Checklist (verdict columns empty), one row
per planned criterion: token-prior separation; envelope rule (corrected battery); measurement
headroom (**declared headroom-class exception — fires on saturated witness by design,
justification slot**); strict−content gap (sign pinned: content − strict); abstention floor;
abstention ceiling; RFI; inconclusive. Columns: `criterion | stratum | ideal_behavior |
ideal_in_pass_region | confuses_ideal_with_universal | strata_separated |
perfect_model_eliminable (must be No unless declared headroom exception) | ill_formed_class_screen
(dead / tautological / malformed) | disposition`.

## Part V — T4 Review-to-Lock Disposition Table (live draft)

| review_item_id | reviewer | risk_class | summary | disposition | rationale | owner | blocking_status |
|---|---|---|---|---|---|---|---|
| INH-1 | inherited (v1 close-out) | semantics | Per-diagnostic stratum semantics: which diagnostics compute over 96/80/16; which use per-stratum N_effective | OPEN | entered per E16 pre-population | New Senior + CS | must resolve before lock |
| INH-2 | inherited (v1 close-out) | totality | Outcome-chooser totality: non-eliminated predicate, RFI-only behavior, inconclusive class, fixed language | OPEN | entered per E16 | New Senior + CS | must resolve before lock |
| INH-3 | inherited (v1 close-out) | statistics | SE interval method: Wilson / Jeffreys / other — never silently Wald | OPEN | entered per E16 | New Senior + CS | must resolve before lock |
| (packet findings) | — | — | rows added as reviews arrive | — | — | — | — |

Rule carried verbatim: no must-fix disappears silently; deferred items enter the next packet's R6
screen — deferral is routing, not burial.

## Part VI — Open issues / Manager decision points

**All references to D2 identify future review locations only. This D1 bundle does not request D2
authorization.**

1. **Prompt-shell visibility for `unconditioned_token_prior`** (drives baseline derivation; D2
   review item; recommendation to be co-drafted with CS).
2. **Cap values and statistical rationale for T1** (declared at packet stage pre-pilot; D2 reviews
   the declarations, not results).
3. **INH-1/2/3 dispositions** (proposals to accompany the D2 return; for INH-3, Wilson is a proposal for review, not a selected interval method under D1).
4. **D4 token-prior gate** (carried; opened by name at sweep-execution authorization only).
5. **Mixture-oracle commit-and-hash ceremony**, A6 mechanics, ideal-witness record format
   finalization, pilot-log template location, evidence-bundle exclusion labels — the seven v0.2
   packet-stage concerns, all assigned Part-II–IV homes above, none blocking D1 work.

## Part VII — Interface questions for CS

1. Runner: confirm the standalone-runner skeleton exposes a no-model **assembly dry-run** (real
   manifests → rendered prompts → template-conformance check) so the interface-contract test runs
   pre-lock without any generation.
2. Schema: confirm sidecar + per-rung schemas can enforce the mechanical
   no-elimination-references-scrambled-control rule by construction (enum/reference validation),
   not by review.
3. Equality predicate: does CS propose a stricter implementable rule than token-id-sequence
   equality for `prefix_neighbor_confusion` self-match exclusion?
4. `copy_completion` agreement-rate diagnostic: per-item agreement field placement (per-item log
   vs. gate record) — CS preference?
5. LOCK-RECORD structure: confirm slots for the D4 by-name token-prior resolution, the sealed-hash
   binding, and the C2 considered-memos enumeration.
6. Path Conventions: intended experiment directory name under the convention (no sweep_id is
   created by naming a directory in a draft — confirm CS agrees on that reading or proposes deferring the name to D2). **Any proposed directory name is provisional until D2 or later. No directory name may create or imply a sweep_id under D1.**

## Part VIII — Cross-review record (design side vs. CS v0.2 skeletons)

Per the CS Interface Alignment Response v0.2 (repo, `47c744d`): every design-packet row maps ALIGNED
to a named CS mechanism — I.4 ↔ CS-EP §6 PolicyInputView code-level blinding + §8 A6 drift + §9 IS-8
refusal; I.5 ↔ CS-EP §7 typed boundary + Layer-2 schema enforcement of the
no-elimination-references-scrambled-control rule; I.6 ↔ CS-EP §15 zero-self-match / B4 pass-region
test class; I.7 ↔ §12 label-emission invariant; I.8 ↔ §2 identical nine-item provenance enumeration;
T1 ↔ §8 `a6_final_manifest_reverification` + IS-7; T2 ↔ §7; T3 ↔ §15 reserved test class; T4 ↔
LOCK-RECORD §2 `r6_inheritance_screen` + addendum C1 row schema; Part VI ↔ CS-EP §16 cross-reference
map. AL-Q1/Q2-schema/Q4/Q5-opt land in CS-EP v0.2 and LOCK-RECORD v0.2 (CS-owned); AL-INH-1/2
co-ownership is reflected in Part V. OPT-1/2/3 remain optional and non-blocking unless elevated.

## Part IX — Non-authorizations (full, unshortened)

This bundle does not authorize: new sweep_id; offline pilot execution; oracle pre-flight execution;
model runs; data generation; execution packet execution; candidate selection; candidate ranking;
threshold-sheet work; certification evaluation; stress-retention testing; B1 v2.1 implementation;
Paper 3 revision; Claim C activation; Fork A reactivation; Paper 6 activation; public benchmark
packaging. All execution gates remain closed.

— New Senior Engineer (to Team Lead for filter; CS in parallel; D2 not requested)
