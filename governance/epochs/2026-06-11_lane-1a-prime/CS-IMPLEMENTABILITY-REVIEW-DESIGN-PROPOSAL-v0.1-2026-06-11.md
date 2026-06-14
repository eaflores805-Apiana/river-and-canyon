# CS Implementability Review — Lane 1a′ Design Proposal v0.1

From: CS Engineer
To: Team Lead
Cc: New Senior Engineer, Senior Engineer, Contributor 5, Contributor 6, Manager
Date: 2026-06-11
Status: CS review COMPLETE; verdict below; no execution authorized

---

## 0. Document under review

| Field | Value |
|---|---|
| Title | Lane 1a′ Design Proposal — Corrected Reconnaissance Sweep With Pre-Lock Instrument Validation v0.1 |
| Author | New Senior Engineer (2026-06-11) |
| Source | `apiana-papers/C6_Proposal/LANE1A-PRIME-DESIGN-PROPOSAL-v0.1.md` |
| Local mirror | `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-DESIGN-PROPOSAL-v0.1.md` |
| sha256 (both) | `6d896499e96b11b5f064d8c985380a4a47422e214e8d928f91d43933213581ad` (`cmp` IDENTICAL) |
| Lens | Implementability and auditability (CS) |
| Routing | Team Lead filter → multi-lens review (Senior, CS, C5, C6) → Team Lead consolidates → potential revision → Manager design authorization |

---

## 1. CS Verdict

```text
PASS WITH TARGETED EDITS
```

The proposal is conceptually well-formed and structurally compliant with
the adopted Pre-Lock Instrument Validation Addendum. The three Lane 1a
v1 instrument defects are correctly diagnosed and addressed. The
required artifacts (T1–T4) are buildable; control semantics are
specified to the field level; pilot-manifest / oracle-case /
final-manifest / sidecar requirements all inherit cleanly from v1 +
addendum precedent.

Edits are recommended for three load-bearing implementability points
that v0.1 currently presents as wording rules (the addendum's own
protection-layer taxonomy ranks code > schema > wording; these three
points need to land at code-level at packet stage, and the design
proposal should commit to that now). None of the edits is
design-blocking — they are explicit hardenings of design intent.

---

## 2. Answers to the five all-reviewer questions

### Q1 — Does the proposal fix the three Lane 1a v1 instrument defects?

**YES.** Each fix is identified and tied to the standing addendum's enforcement triple.

| Defect | v1 mechanism | v0.1 fix | CS assessment |
|---|---|---|---|
| **A. Degenerate dummy battery / union-envelope saturation** | `target_recency` and `homogeneous_prefix_completion` reduced to self-match retrieval oracles → union envelope at 1.000 → every envelope-relative elimination fired unconditionally | (i) §5 design rule: *policy matching functions are blinded to exact queried-key identity*; (ii) `recency_excluding_target` replaces `target_recency`; (iii) `prefix_neighbor_confusion` replaces `homogeneous_prefix_completion`; (iv) addendum A2/A3/A5/A6 enforcement | Correctly diagnosed. Fix is structurally right. **DE-1 below** requests the design proposal commit to code-level enforcement of the "blinded" rule (currently presented as a wording rule). |
| **B. Mis-specified token-prior control** | v1 control measured retrieval under scrambled bindings, not token-prior emission | §6: two controls fully T2-specified pre-code: `unconditioned_token_prior` (key absent + values removed; format-preserving null-context shell) and `scrambled_binding_retrieval` (v1 retained under its honest name, **diagnostic-only and non-eliminating**) | Correctly diagnosed. Fix is well-formed. **DE-2 below** requests the design proposal commit to code-level enforcement of the diagnostic-only mark (the analysis script must structurally refuse to emit an elimination label from this control's output, parallel to how v1's verdict enum structurally cannot emit `passes_*`). |
| **C. Abstention criterion excluding ideal NULL** | v1 two-sided abstention band `[0.50, 0.95]` excluded perfect 1.000 NULL discipline | §7: ideal-witness specification declared/reviewed/locked before any pass-region checklist; two-condition criterion (NULL-floor + answerable-ceiling) whose joint pass region **contains the ideal corner by construction**; T3 5-Q check incl. "could a perfect model be eliminated" | Correctly diagnosed. Fix is **structural** (joint pass region contains ideal corner by construction). No code-level hardening edit required; this is the cleanest of the three fixes. |

### Q2 — Does the proposal comply with the adopted Pre-Lock Instrument Validation Addendum?

**YES — strongly.** This is the addendum's first applied instance (proposal §3 states so explicitly).

| Addendum requirement | v0.1 coverage |
|---|---|
| A1 — Pilot-manifest battery run | §5 "all offline: pilot-manifest battery execution (A1)" |
| A2 — Per-policy degeneracy cap | §5 "per-policy accuracy caps declared pre-pilot with rationale (A2)" |
| A3 — Union-envelope cap | §5 "union-envelope cap with declared measurement room (A3)" |
| A4 — Policy classification | §5 "operation-equivalent / degenerate classification with coverage recomputation (A4)" |
| A5 — Oracle-case pre-flight | §5 full oracle-case list incl. synthetic ideal retriever, every declared policy, token-prior emitter, universal answerer, universal abstainer, NULL-on-NULL handler, malformed control, ≥1 mixture oracle with pre-declared expected_verdict |
| A6 — Final-manifest re-verification | §5 "final-manifest re-verification of all caps before lock (A6)" |
| B1 — Control semantic target locked before implementation | §6 full T2 field-level specification for both controls |
| B2 — Target taxonomy non-interchangeable | §6 "targets non-interchangeable by rule"; explicit reuse of taxonomy names |
| B3 — Ill-formed criterion classes (dead / tautological / malformed) | §7 "dead / tautological / malformed screens"; standing rule on decline-with-rationale |
| B4 — Ideal-witness / pass-region checklist | §7 explicit; ideal-witness locked before checklist; T3 5-Q applied incl. perfect-model-eliminable question |
| C1 — Review-to-lock disposition (T4) | §9 T4 row-schema referenced; §10 deferred-items inherit per E18 |
| C2 — Considered-memos enumeration | §10 explicit ("the installed C2 enumeration rule") |
| C3 / R6 — Requirement-inheritance check | §3 full R6 inheritance screen with adopt/adapt/decline-with-rationale categories populated |
| Containment + anti-tuning | §5/§8 anti-tuning explicit; E11 pilot-iteration retention explicit |
| Artifact labels (E15) | §8: SYNTHETIC for oracle/pilot artifacts; RECONNAISSANCE for sweep outputs |
| Report-level non-claim (E16) | §8 verbatim |
| Scope guard (instrument-only / classifier-not-certifier) | §2 verbatim from standing |

Compliance: complete.

### Q3 — Ambiguous terms, controls, labels, or decision points?

Three implementability-specific ambiguities that should be tightened
(none design-blocking):

1. **"Blinded to exact queried-key identity" (§5)** — the equality
   predicate for "exact queried key" is unspecified. Tokenizer-canonical
   form? Case-sensitive surface form? Hash-equal token-id sequence?
   The v1 incident hinged exactly on what "exact match" meant in
   practice. **DE-3 below** asks v0.1 to specify the predicate
   (CS proposes: token-id-sequence equality after tokenizer
   canonicalization, deferred to packet stage if v0.1 prefers to defer
   but the spec must be packet-level mandatory).

2. **"Format-preserving prompt shell" for `unconditioned_token_prior`
   (§6)** — what fields are preserved, what fields are stripped, and
   what produces the format? Not blocking for design proposal but the
   execution packet must specify. CS flags as implementation-stage
   concern (IS-1 below).

3. **"Real-pair block is the recency-relevant tail" (§4)** — the
   `recency_excluding_target` policy operates on the recency-relevant
   tail; the manifest schema must label the real-pair block boundary
   unambiguously so the policy can compute over the tail without
   reading the prepended padding. Implementation-stage; CS flags as
   IS-2 below.

Decision points D1–D5 (§12) are clearly enumerated and
non-overlapping; the explicit "by name, never by bundle" routing for
the standing token-prior gate at D4 is well-formed.

### Q4 — Hidden authorization leaks?

**NONE STRUCTURAL.** §11 enumerates the 14 standing non-authorizations
exhaustively (matching `STANDING-NON-AUTHORIZATIONS.md`). §10's
pre-registered outcome semantics is the only soft surface CS examined,
and on examination it is a containment statement, not an
authorization: it pre-commits how a K=0 result would be characterized
under sealed report (lane's substantive negative answer for this task
family at this scale; final for this construction; not grounds for
instrument re-litigation absent a documented new instrument defect).
The "publishable" connotation in that sentence is a wording matter for
Contributor 5 / Senior to weigh — CS flags it as **OW-1 below** but
does not treat it as an authorization leak.

§8's "A Validation Report PASS authorizes nothing; it is a
precondition for requesting execution authorization, not a substitute
for it" is the explicit non-authorization. CS endorses.

### Q5 — Disposition

```text
PASS WITH TARGETED EDITS
```

Rationale: the proposal correctly fixes all three v1 defects, complies
with the standing addendum at section-by-section depth, and routes
itself through the addendum's full T1–T4 + A1–A6 + B1–B4 + C1–C3 +
R6 chain before any future lock. The recommended edits ask v0.1 to
commit at design-stage to code-level enforcement for three protections
currently presented at wording level; the protection-layer taxonomy in
the standing review-discipline rule treats wording as the weakest
layer, so naming these now hardens the design.

---

## 3. Edits classification

### 3a. Design-blocking edits

**NONE.**

### 3b. Targeted design-stage edits (recommended; not blocking)

| ID | Edit | Rationale |
|---|---|---|
| **DE-1** | In §5, after the "blinded to exact queried-key identity" sentence, add a one-sentence commitment to packet-stage CODE-level enforcement (proposed: *"At packet stage this rule is enforced structurally: policies receive the manifest record via an interface that does not expose the exact queried-key identity to the matching function, and CS includes a unit test asserting each policy scores 0 on the synthetic ideal-retriever oracle's answerable items where retrieval would self-match."*) | Per the protection-layer taxonomy (`STANDING-REVIEW-DISCIPLINE.md`), wording-only protection is the weakest layer. The v1 failure was a wording-vs-code mismatch. Naming the code-level enforcement here closes that mismatch at design stage. |
| **DE-2** | In §6, after the `scrambled_binding_retrieval` "Failure interpretation: informs interpretation only" sentence, add a one-sentence commitment to packet-stage CODE-level enforcement (proposed: *"At packet stage this control is structurally diagnostic-only: the analysis script's elimination-label emission path takes no input from this control's output, enforced by a typed boundary parallel to the v1 verdict enum that admits no `passes_*` value."*) | Same protection-layer reasoning. The diagnostic-only mark is the load-bearing protection for B-correction; structural enforcement at packet stage prevents drift back to v1's confusion. |
| **DE-3** | In §5, add a half-sentence specifying the equality predicate for "queried key exclusion" in `recency_excluding_target` and `prefix_neighbor_confusion` (proposed: *"key equality is token-id-sequence equality after tokenizer canonicalization; the equality predicate is locked in the execution packet."*) | v1's failure rested on what "exact match" meant in token space; specifying the predicate at design stage prevents the same ambiguity from resurfacing as an implementation choice later. |

### 3c. Implementation-stage concerns (for the future execution packet — no edits to v0.1)

| ID | Concern | Notes |
|---|---|---|
| **IS-1** | `unconditioned_token_prior` "format-preserving prompt shell" — concrete prompt-template specification, what fields are preserved vs stripped, how `value bindings removed` is rendered | Must be specified at execution-packet stage with a worked example. |
| **IS-2** | Manifest schema must label real-pair-block boundaries (start/end indices or a `real_pair_block_span` field) so `recency_excluding_target` computes over the recency-relevant tail unambiguously and policies cannot accidentally read the prepended padding | A schema-level constraint enforces the §4 "policies compute over the full visible context" + recency-tail design. |
| **IS-3** | Mixture oracle expected_verdict commit-and-hash mechanism — the fraction and the verdict (detect / pass / flag-indeterminate) must be locked and hashed BEFORE pre-flight | The addendum mandates pre-execution lock; the execution packet must specify the commit ceremony so the anti-tuning rule is enforceable. |
| **IS-4** | `unconditioned_token_prior` requires model generations at sweep time and touches the standing token-prior Manager gate — the execution packet must route this gate authorization "by name, never by bundle" at D4, as §10 risk (iii) and §12 D4 already direct | CS flag for the packet-prep step: the packet must not bundle the token-prior control authorization with the broader sweep authorization. |
| **IS-5** | The `recency_excluding_target` and `prefix_neighbor_confusion` policies require a deterministic neighbor-selection rule when multiple candidates tie (e.g., two prefix-neighbors at equal prefix length); the tie-break rule must be locked in the execution packet | Implementation hygiene; not design-blocking. |
| **IS-6** | Pilot iteration logging (E11) on first applied instance — CS will implement the four fields (`pilot_iteration_count; failed_pilot_records_retained; reason_for_each_repilot; changed_fields_between_pilots`) as schema-validated fields in the Instrument Validation Report; the schema lives in `governance/standing/templates/` per PA-3 from the addendum adoption | Coordinates with the post-adoption PA-3 work. |

### 3d. Optional wording improvements

| ID | Suggestion | Notes |
|---|---|---|
| **OW-1** | §10 "publishable, final for this construction" — consider tightening "publishable" to "available as the lane's substantive negative finding under sealed report" to remove any connotation that publication is implied | Strict wording matter; CS defers to Senior / Contributor 5 review under their lenses. Non-blocking. |
| **OW-2** | §3 R6 screen reads cleanly but could name each of the three production rules (G1-open, sibling-artifact, subprocess smoke test) explicitly under "Adopted" to demonstrate full R6 enforcement | Nice-to-have; current "G1 delivery and review-enumeration rules" reference covers it implicitly. |

---

## 4. Implementability checks against the addendum

### T1 — Battery degeneracy audit

Implementable. CS implementation note: the new policies
(`recency_excluding_target`, `prefix_neighbor_confusion`) require a
`queried_key_token_ids` field in the manifest for the exclusion test;
both are deterministic post-policy-lock; CS unit tests can verify the
zero-self-match property on the synthetic ideal-retriever oracle.

### T2 — Control semantics specification

Implementable. Both controls have every field populated. CS will hash
both T2 sheets with the packet at lock per addendum B1. Conformance
check at pilot is straightforward (declared targets are testable).

### T3 — Ideal-witness / pass-region checklist

Implementable, and structurally clean. The §7 "joint pass region
contains the ideal corner by construction" is the right protection
layer (code rather than wording). The 5-Q checklist applied; the
malformed/dead/tautological screens are explicit.

### T4 — Review-to-lock disposition table

Implementable; identical schema to the adoption-package E21 instance.
CS already has the schema operational from the addendum adoption.

### Pilot manifests, oracle cases, final-manifest re-verification, sidecar

- **Pilot manifests**: inherited recipe from §13 v0.2 + padding placement + novelty rule; drawable from the locked recipe; deterministic.
- **Oracle cases**: A5 list is concrete; mixture oracle is the one new construct, well-specified at design level (IS-3 covers the execution-packet commit ceremony).
- **Final-manifest re-verification**: A6 is implementable as a re-run of the policy battery against the locked manifest; fast (no model required); deterministic.
- **Sidecar attestation**: inherited from Lane 1a v1 packet; established pattern; CS production-path subprocess smoke test rule continues to apply at packet stage.

All satisfiable at packet stage under inherited v1 infrastructure plus the addendum's pre-lock validation discipline.

---

## 5. Boundaries preserved

```text
No execution authorized.
No new sweep_id.
No model runs.
No data generation.
No execution packet.
No pilot execution.
No candidate selection.
No candidate ranking.
No threshold-sheet work.
No certification evaluation.
No stress-retention testing.
No B1 v2.1 implementation.
No Paper 3 revision.
No Claim C activation.
No Fork A reactivation.
No Paper 6 activation.
No public benchmark packaging.
```

This review proposes nothing executable. If Manager later authorizes
Lane 1a′ packet preparation (D2), that authorization comes by name
and not by bundle.

---

## 6. CS posture

```text
Lane 1a' Design Proposal v0.1:

  Source bytes verified (cmp IDENTICAL with C6_Proposal source).
  R6 inheritance screen present and populated.
  Pre-Lock Instrument Validation Addendum compliance: complete.
  Three v1 instrument defects: each correctly diagnosed and addressed.
  T1-T4 implementability: clean.

  Design-blocking edits:           NONE
  Targeted design-stage edits:     DE-1, DE-2, DE-3 (load-bearing
                                    code-level commitments)
  Implementation-stage concerns:   IS-1 through IS-6 (for execution
                                    packet stage; non-blocking now)
  Optional wording improvements:   OW-1, OW-2

CS verdict:                        PASS WITH TARGETED EDITS

Next:                              Team Lead binning + consolidated
                                    revision request to New Senior
                                    if needed; CS holds for revised
                                    draft if one is issued.

All execution gates:               CLOSED
```

— CS Engineer, 2026-06-11
