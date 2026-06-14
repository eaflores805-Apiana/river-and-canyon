# CS Implementability Review — Lane 1a′ Design Proposal v0.2

From: CS Engineer
To: Team Lead
Cc: New Senior Engineer, Senior Engineer, Contributor 5, Contributor 6, Manager
Date: 2026-06-11
Status: CS review COMPLETE; verdict below; no execution authorized

---

## 0. Document under review

| Field | Value |
|---|---|
| Title | Lane 1a′ Design Proposal — Corrected Reconnaissance Sweep With Pre-Lock Instrument Validation v0.2 |
| Author | New Senior Engineer (2026-06-11) |
| Source | `apiana-papers/C6_Proposal/LANE1A-PRIME-DESIGN-PROPOSAL-v0.2.md` |
| Local mirror | `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-DESIGN-PROPOSAL-v0.2.md` |
| sha256 (both) | `31e7b9b696b84b8f25eb68f1c49528c96b8ae948f75aee4183a94a90e97bd9e4` (`cmp` IDENTICAL) |
| Lens | Implementability and auditability (CS) |
| Routing | Team Lead filter PASS (memo of 2026-06-11) → CS implementability review (current step) → Manager design authorization |

---

## 1. CS Verdict

```text
PASS — implementable; route to Manager design-authorization review.
```

v0.2 is a clean revision. All 22 consolidated edits (E1–E22) and the
three additional structural items (no-positive-use block, packet-stage
concerns enumeration, survivor→non-eliminated-rung wording) land
correctly. The three CS-flagged v0.1 design-stage edits (DE-1, DE-2,
DE-3) are all addressed.

The proposal is now ready for Manager design-authorization review.

Implementation-stage concerns (carried forward, mostly already on the
v0.2 §10 list) and one new CS note (drift tolerance, IS-7) are
recorded under §5 below for the eventual packet stage. None of these
is a design-authorization blocker.

---

## 2. v0.1 → v0.2 edit-landing audit (CS verifications)

### 2a. My three v0.1 design-stage edits

| ID | v0.1 ask | v0.2 landing | CS status |
|---|---|---|---|
| **DE-1** | §5 commit to code-level enforcement of "blinded to queried-key" rule | §5 lines 92–98: Total-function definition (4 clauses) + Operation-equivalence consequence (§5 line 109) | **EFFECTIVELY ADDRESSED.** The structural undefinedness-is-impossible-by-definition language and the operation-equivalence consequence (must be removed or reclassified before lock; may not remain in the union envelope) together raise this from a wording protection to a code-level lock-time refusal. A5's oracle-case pre-flight covers the zero-self-match test on the synthetic ideal-retriever. CS endorses. |
| **DE-2** | §6 commit to code-level diagnostic-only enforcement of `scrambled_binding_retrieval` | §6 line 142: **"Mechanical rule: no elimination label may reference `scrambled_binding_retrieval`, directly or indirectly."** | **LANDED VERBATIM.** This is the load-bearing code-level boundary. CS endorses. |
| **DE-3** | §5 specify equality predicate for "exact queried key" | §5 line 93: **"the equality predicate is token-id-sequence equality after tokenizer canonicalization, unless CS proposes a stricter implementable rule"** | **LANDED VERBATIM.** And it leaves a clean CS-veto path. CS endorses; see IS-9 below. |

### 2b. The 22 consolidated edits (E1–E22)

CS spot-checked each edit against the document text:

| E# | Edit | Landing |
|---|---|---|
| E1 | Construction-failure language softened (§4) | ✓ "Lane 1a v1 did not establish that the construction was the failure; the primary identified failure was instrument-side — so the construction is carried forward as a working basis subject to the same revalidation as everything else, not as proven sound" |
| E2 | N=96 marked proposed-not-locked (§4) | ✓ "is carried as the current proposal, not as a locked design constant — final N, answerable/NULL split, and void budget must be confirmed during packet preparation and instrument validation" |
| E3 | Occupancy question reworded (§1) | ✓ "without ranking or positively supporting that region for candidate selection" |
| E4 | Operation-equivalent consequence (§5) | ✓ removed or reclassified before lock; may not remain in union envelope |
| E5 | `prefix_neighbor_confusion` total function (§5) | ✓ 4-clause definition |
| E6 | `copy_completion` outside union envelope (§5) | ✓ "outside the union envelope unless a separate pre-registered agreement-rate diagnostic is defined" |
| E7 | Envelope-inversion non-claim (§5) | ✓ low/non-saturated envelope is not evidence of candidate virtue |
| E8/E9 | `scrambled_binding_retrieval` strengthened + mechanical rule (§6) | ✓ "strictly diagnostic and non-eliminating ... no elimination label may reference scrambled_binding_retrieval, directly or indirectly" |
| E10 | Token-prior generations not design-authorized (§6) | ✓ "Design authorization does not authorize token-prior generations" |
| E11 | Baseline derived from shell visibility (§6) | ✓ derivation rule explicit |
| E12 | "Unconditioned" per standing taxonomy (§6) | ✓ "format-conditioned but binding-free" |
| E13 | K=0 outcome semantics tightened (§10) | ✓ "publishable" removed; "pre-registered substantive reconnaissance-negative finding for this task family at this scale, for this construction. It is not a Paper 3 certification verdict and not evidence of model incapability" — this also closes my v0.1 OW-1 |
| E14 | Non-eliminated-rung non-claim (§10) | ✓ "not promising, viable, candidate-ready, near-certifiable, or suitable for positive selection" |
| E15 | Symmetric finality (§10) | ✓ both K=0 and non-eliminated outcomes bounded against re-litigation in their respective directions |
| E16 | T4 pre-populated with three inherited open items (§8) | ✓ stratum semantics; outcome-chooser totality; SE interval method |
| E17 | B1-equivalent provenance enumerated (§2) | ✓ runner attestation; artifact hashes; append-only audit log; lock/access timestamps; sidecar records; model identity; prompt/config identity; raw output preservation; no wrapper-rewrite |
| E18 | Mixture oracle blend/components/verdict pre-declared (§5) | ✓ |
| E19 | A6 drift check (§5) | ✓ "must compare pilot and final per-policy scores and union-envelope scores and flag drift" |
| E20 | Offline pilot validation not authorized by this proposal (§8) | ✓ "This proposal defines offline pilot validation requirements but does not authorize pilot execution" |
| E21 | v1 numerics diagnostic-only (§2) | ✓ "Lane 1a v1 numeric levels may be referenced only as instrument-failure diagnosis" |
| E22 | §1 wording | ✓ (covered by E3) |

Additionally:
- **No-positive-use block (§10):** "no Lane 1a′ output — label, diagnostic, control number, validation result, or report — may be used as positive evidence for any model, construction, candidate, threshold, or certification purpose. Outputs rule out or they say nothing." ✓ Clean.
- **Packet-stage concerns enumerated (§10):** 7 items explicitly named, parking them for packet stage. ✓ This subsumes my v0.1 IS-1/IS-2/IS-3/IS-6.
- **Survivor → non-eliminated-rung wording (§10):** "unordered non-eliminated-set serialization, no rank fields or computations, fixed language, single-non-eliminated-rung sentence". ✓

All 22 edits landed; all three v0.1 design-stage edits effectively addressed.

---

## 3. Answers to the 10 review-focus items

### Item 1 — Can T1–T4 be implemented cleanly as written?

**YES.**

- **T1 (battery degeneracy audit):** Same schema as the addendum's appendix; `copy_completion` is now correctly outside the union envelope (cleaner; copy_completion measures per-item agreement, not accuracy, and would have falsely depressed an accuracy envelope). The four remaining envelope-policies (`pure_last_position`, `salient_endpoint`, `recency_excluding_target`, `prefix_neighbor_confusion`) are accuracy-comparable and union-compatible. The operation-equivalence consequence converts to a hard lock-time refusal (see IS-8 below).
- **T2 (control semantics specification):** Both controls fully specified at field level; the baseline-derivation rule is now explicit (E11).
- **T3 (ideal-witness / pass-region checklist):** Unchanged from v0.1 evaluation; structurally clean (joint pass region contains ideal corner by construction).
- **T4 (review-to-lock disposition table):** Now pre-populated with three inherited open items (E16), turning the founding incident's lesson — *Lane 1a v1's failure began with a filed must-fix that received no disposition* — into a structural defense for v0.2.

### Item 2 — Are the proposed controls buildable and auditable?

**YES.**

- **`unconditioned_token_prior`** — all six T2 fields populated; baseline derivation rule is explicit; the format-preserving-prompt-shell concrete spec is properly parked at packet stage (§10 item 1). Buildable; auditable via T2 conformance.
- **`scrambled_binding_retrieval`** — diagnostic-only and non-eliminating; the mechanical rule provides the code-level boundary; the analysis script must structurally refuse to read this control's output into any elimination-label computation path. Auditable via source-level grep of the elimination-label code paths.

### Item 3 — Is `prefix_neighbor_confusion` deterministic enough for implementation?

**YES.** The 4-clause total-function definition makes it fully deterministic and total:

| Question | v0.2 §5 answer |
|---|---|
| Exact queried-key exclusion? | ✓ "exact queried-key self-match is excluded" |
| Equality predicate? | ✓ "token-id-sequence equality after tokenizer canonicalization, unless CS proposes a stricter implementable rule" |
| Tie-breaking? | ✓ "ties among shared-prefix neighbors resolve to the most recent neighbor in the visible context" |
| Declared no-match output? | ✓ "if no eligible shared-prefix neighbor exists (typical on K=low rungs), the policy emits a declared no-match output" |
| No-match / undefined contribution to envelope? | ✓ "undefined/no-match predictions score incorrect and contribute nothing to the union envelope unless separately declared as a diagnostic case — structural undefinedness on K=low is therefore impossible by definition, not by hope" |

All five sub-questions answered. CS reads the four clauses as a complete operational specification. CS proposes no stricter equality rule at this time (see IS-9 below).

### Item 4 — Is `copy_completion` correctly removed from the union-envelope mechanism?

**YES.** §5 moves `copy_completion` outside the envelope and explains why: "its detection mechanism is per-item agreement between candidate output and the copy pattern, not accuracy, so it does not sit as a low-accuracy policy inside an accuracy-union envelope." This is right: a copy-pattern-agreement metric is not comparable with the other policies' answerable-accuracy scores, and including it in the union would either inflate or depress the envelope depending on the candidate's distribution. The "unless a separate pre-registered agreement-rate diagnostic is defined" clause preserves the option to add a parallel agreement-rate envelope later if needed, but does not require it.

### Item 5 — Can final-manifest re-verification be implemented as stated?

**YES.** §5 A6 now explicitly requires:

```text
- per-policy caps re-checked on final manifests
- union-envelope cap re-checked on final manifests
- pilot vs final score drift flagged
```

Implementation contract for the packet stage:
1. After manifest lock, take `final_manifest_hash`.
2. Re-execute the locked policy battery against the final manifest records.
3. Recompute per-policy scores and union envelope.
4. Compute `drift_per_policy = abs(final_score - pilot_score)` and `drift_envelope = abs(final_envelope - pilot_envelope)`.
5. Compare against declared drift tolerance(s) (see IS-7 below — drift tolerance must be pre-declared per anti-tuning rule).
6. Emit re-verification block: `{final_manifest_hash, per_policy_caps_hold, envelope_cap_holds, drift_per_policy, drift_envelope, drift_within_tolerance: bool}`.

### Item 6 — Can mixture-oracle requirements be implemented?

**YES.** §5 mandates pre-declaration of:

```text
- blend fraction
- component behaviors
- expected verdict (detect | pass | flag-indeterminate)
```

…all locked before pre-flight execution. The commit-and-hash ceremony is parked at packet stage (§10 item 3) — CS reads this as a process-level concern, not a design-level concern, and will define the ceremony in the execution packet. Anti-tuning rule + E11 pilot-iteration retention prevent post-declaration mutation.

### Item 7 — Can `unconditioned_token_prior` be specified at packet stage without ambiguity?

**YES.** The packet-stage spec must populate:

| Spec field | v0.2 § | Implementation note |
|---|---|---|
| Shell visibility | §6 "declared prompt-shell visibility" | Packet defines exact shell template; CS proposes the template be hash-locked with the packet. |
| Value pool visibility | §6 "value pool" | Packet specifies whether the value pool is rendered in the shell. |
| Binding removal | §6 "queried key absent and value bindings removed" | Packet specifies the exact transform that removes bindings while preserving format. |
| Expected baseline / chance rate | §6 E11 derivation rule | Computed deterministically from the three above. |
| Scoring contract | §6 "gold value of the mirrored answerable item" | Packet specifies the mirroring rule. |

All five specifiable at packet stage without ambiguity. The §10 item 1 packet-stage concern names the exact-prompt-shell-content work explicitly.

### Item 8 — Are the Manager decision points D1–D5 clear and implementable?

**YES.** §12 enumerates five gates:

```text
D1 — Design authorization (this proposal)
D2 — Packet preparation authorization (design packet + CS execution packet,
     including offline pilot and oracle validation)
D3 — Instrument Validation Report acceptance (Team Lead review; sealed T1–T4)
D4 — Sweep execution authorization
     — by name include/decline unconditioned_token_prior generations under the
       standing token-prior gate (open by name, never by bundle)
     — bind to sealed LOCK-RECORD hash
     — follow G1-open and review-enumeration rules
D5 — Close-out acceptance with pre-registered outcome semantics per §10
```

"Each gate is independent; passing one authorizes nothing beyond it." — clean separation. CS reads each gate as implementable via the existing G1 delivery + LOCK-RECORD discipline. The "by name, never by bundle" routing at D4 is the load-bearing detail and is explicit.

### Item 9 — Are all non-authorizations preserved?

**YES.** §11 enumerates 14 items exhaustively. The new §10 "No positive use" block adds a stronger containment:

> *"no Lane 1a′ output — label, diagnostic, control number, validation result, or report — may be used as positive evidence for any model, construction, candidate, threshold, or certification purpose. Outputs rule out or they say nothing."*

CS endorses this as a meta-non-authorization that closes any residual interpretive gap.

### Item 10 — Hidden implementation risks before any execution packet exists?

**LOW.** v0.2 §10 enumerates 7 packet-stage concerns and 4 named residual risks (degenerate-mode, validation-as-tuning, token-prior gate, transfer/review-chain). All are bounded by existing standing rules (anti-tuning, E11 retention, G1-open production rule, sibling-artifact cross-reference rule, production-path subprocess smoke test rule).

CS records two implementation-stage concerns NEW to v0.2 (not in §10's list):

- **IS-7** (new) — A6 drift tolerance must be pre-declared per anti-tuning rule (see §3 Item 5).
- **IS-8** (new) — Operation-equivalence consequence requires lock-time hard refusal at code level, not just wording (see §5 below for full note).
- **IS-9** (new) — Equality-predicate veto path: CS proposes no stricter rule at this time; reserves the right at packet stage if tokenizer edge cases (e.g., unicode-normalization boundaries) surface.

None of the three rises to design-blocking.

---

## 4. Answers to the 7 specific checks

### Check 1 — v0.2 proposal path and sha256

```text
Source:      apiana-papers/C6_Proposal/LANE1A-PRIME-DESIGN-PROPOSAL-v0.2.md
Mirror:      governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-DESIGN-PROPOSAL-v0.2.md
sha256:      31e7b9b696b84b8f25eb68f1c49528c96b8ae948f75aee4183a94a90e97bd9e4
cmp:         IDENTICAL
```

### Check 2 — Folder follows adopted Path Conventions?

**YES.** `governance/2026-06-11_lane-1a-prime/` is lane-specific governance under `governance/<date>_<lane>/`, matching the standing rule installed at the addendum adoption. No other path option applies — Lane 1a′ is a proposed lane distinct from Lane 1a v1, so it requires its own folder.

### Check 3 — Can design proceed to Manager design-authorization, or is v0.3 needed?

**Design can proceed to Manager design-authorization.** No v0.3 required for CS lens. (Other lenses may differ; CS speaks only to implementability and auditability.)

### Check 4 — Any design-stage language leaving room for accidental execution authorization?

**NO.** Belt-and-suspenders containment:

- §1 status sentence: "Lane 1a′ is a proposed corrected reconnaissance design. Nothing more is claimed."
- §6: "Design authorization does not authorize token-prior generations."
- §8: "This proposal defines offline pilot validation requirements but does not authorize pilot execution; pilot validation requires later packet-stage authorization (§12 D2)."
- §8: "A Validation Report PASS authorizes nothing; it is a precondition for requesting execution authorization, not a substitute for it."
- §10 No-positive-use block: "Outputs rule out or they say nothing."
- §11: 14 non-authorizations enumerated.
- §12: 5 independent gates; "passing one authorizes nothing beyond it."

CS finds no surface that could be misread as authorizing execution.

### Check 5 — Offline pilot validation clearly deferred to packet-stage authorization?

**YES.** §8 explicit: "This proposal defines offline pilot validation requirements but does not authorize pilot execution; pilot validation requires later packet-stage authorization (§12 D2)."

### Check 6 — Token-prior control requires separate Manager-named authorization at D4?

**YES.** Two anchors:

- §6: "Design authorization does not authorize token-prior generations. Token-prior generations remain closed until Manager opens them by name at the sweep execution gate (§12 D4)."
- §12 D4: "by name include or decline the `unconditioned_token_prior` control generations under the standing token-prior gate (open by name, never by bundle)."

CS endorses; the routing is explicit and matches the standing token-prior gate discipline.

### Check 7 — Lane 1a v1 numeric levels quarantined as instrument-failure diagnosis only?

**YES.** §2: "Lane 1a v1 numeric levels may be referenced only as instrument-failure diagnosis; they may not be used as evidence for Lane 1a′ viability, model capability, task-family suitability, or candidate readiness." Combined with the §1 scope-guard inheritance and the §10 no-positive-use block, the v1 numerics are tightly quarantined.

---

## 5. Edits classification

### 5a. Design-authorization blockers

**NONE.**

### 5b. Packet-stage implementation concerns

The 7 items already enumerated in v0.2 §10 (prompt shell; manifest-schema labeling; mixture-oracle ceremony; A6 mechanics; ideal-witness record format; pilot-iteration logging schema/template location; validation artifact labels and exclusion in evidence bundle) are correctly parked there. CS adds three CS-side notes for the packet stage:

| ID | Concern | Rationale | Owner |
|---|---|---|---|
| **IS-7** | A6 drift tolerance must be pre-declared per anti-tuning rule | v0.2 §5 mandates drift flagging but does not specify the tolerance; per anti-tuning, the tolerance must be locked before pilot execution and is itself subject to T4 disposition if changed | Senior (declaration) + CS (verification) at packet stage |
| **IS-8** | Operation-equivalence consequence requires lock-time hard refusal at code level | v0.2 §5 mandates removal/reclassification of operation-equivalent policies before lock; CS implementation flag: the lock script must structurally refuse to proceed if any negative-battery policy is classified operation-equivalent, rather than relying on reviewer attestation | CS at execution-packet stage |
| **IS-9** | Equality-predicate stricter-rule veto path | v0.2 §5 leaves "unless CS proposes a stricter implementable rule" as a CS veto path; CS proposes no stricter rule at this time but reserves the option at packet stage if tokenizer edge cases (e.g., unicode-normalization boundaries) surface | CS at execution-packet stage |

Together with v0.2's seven enumerated packet-stage concerns, these complete the CS-side punch list for the eventual D2 packet preparation.

### 5c. Optional wording improvements

**NONE.** v0.1's OW-1 ("publishable" connotation in §10) is closed by E13. v0.1's OW-2 was nice-to-have; the §3 R6 screen reads cleanly as-is and CS does not press the optional naming.

---

## 6. Boundaries preserved

```text
No execution authorized.
No new sweep_id.
No model runs.
No data generation.
No execution packet.
No offline pilot execution.
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

This review proposes nothing executable. All execution gates remain CLOSED.

---

## 7. CS posture

```text
Lane 1a' Design Proposal v0.2:

  Source bytes verified (cmp IDENTICAL with C6_Proposal source).
  22 consolidated edits + 3 structural additions: ALL LANDED.
  v0.1 design-stage edits (DE-1, DE-2, DE-3): ALL ADDRESSED.
  Pre-Lock Instrument Validation Addendum compliance: complete
                                                      (first applied
                                                       instance).
  Three v1 instrument defects: each correctly diagnosed and addressed,
                                with structural protections at the
                                code/definition layer.
  T1-T4 implementability: clean (copy_completion correctly moved
                                  outside envelope; T4 pre-populated
                                  with three inherited open items).
  Manager decision points D1-D5: clear and implementable; each gate
                                  independent; token-prior gate
                                  named at D4.

  Design-authorization blockers:   NONE
  Packet-stage concerns:           7 v0.2-enumerated + 3 CS notes
                                    (IS-7 drift tolerance;
                                     IS-8 lock-time refusal;
                                     IS-9 equality-predicate veto)
  Optional wording improvements:   NONE

CS verdict:                        PASS — implementable; route to
                                    Manager design-authorization
                                    review.

Next:                              Manager design-authorization
                                    decision (D1).
CS holds for:                      Manager D1 decision.
On Manager D1 authorization:       CS prepares execution packet at
                                    D2 packet-preparation stage,
                                    incorporating the 7 + 3 packet-
                                    stage concerns into the packet
                                    spec.

Lane 1a close-out v1.2:            CLOSED-PENDING-ADOPTION
                                    (parallel track; Senior owns
                                     v1.2 draft; R6 cross-reference
                                     to the installed standing rule)
All execution gates:               CLOSED
```

— CS Engineer, 2026-06-11
