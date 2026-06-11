# Phase 5 Corrective Disposition Proposal (v0.1)

```text
DRAFT / REVIEW ONLY — JOINT CS / NEW SENIOR CORRECTIVE PROPOSAL (NS-drafted; CS co-signature required)
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION · NO CANDIDATE/MODEL OUTPUTS
LOCK-RECORD REMAINS PENDING · D3 NOT REQUESTED · D4/D5 NOT REQUESTED
```

*New Senior Engineer, 2026-06-11. Grounded in the Phase 5 artifacts read from repo bytes
(`experiments/2026-06-11_lane-1a-prime/validation/`: t1/t3/t4 reports, oracle results, execution
ledger). Headline: the Phase 5 result is a correct fail-closed outcome — A6 and the oracle pre-flight
each caught a real defect, which is the instrument validating the validation. One root cause
explains all three oracle findings; one separate root cause explains the drift.*

## Root-cause summary (before the eleven answers)

**RC-1 (oracle findings, all three):** Phase 5 evaluated a **reduced criteria set** — two of six
criteria (the abstention pair), with placeholder bounds (floor = ceiling = 0.5) and a comparison
direction differing from the declared §B rules. The envelope, token-prior-separation, headroom, and
gap criteria require [SWEEP-PARAMETER] bounds that were never fixed, because the **joint
expected-verdict + bounds lock event was never held** — the NS-proposed declaration (ORC-01…12)
explicitly binds nothing until CS co-signs, and Phase 5 ran on a CS-local verdict table instead.
Consequences, each now explained: (a) every non-abstaining shortcut oracle eliminated through
`null_abstention_floor_unmet` because the NULL floor was the only live eliminative path for such
cases — the broad outcomes were right, the explanation paths were an artifact of the missing
criteria; (b) `malformed_control` mismatched because the two tables disagree about its semantics
(CS expected ELIMINATED; the NS declaration defines it as the **semantic-separation pass-guard** —
a rebinding-follower that must NOT attach the token-prior label — expected NOT_RULED_OUT), and the
criteria that could even test the question weren't running; (c) the mixture case returned no
proximity flag because the envelope criterion that generates proximity flags did not exist in the
run.

**RC-2 (A6 drift):** structural hit-rates are currently **per-draw random variables**, not
construction constants. The recipe leaves gold-position placement to uniform chance, so
`pure_last_position`'s rate floats with the draw (pilot↔final drift 0.1375, ≈3σ of the binomial
sd at N=80); the envelope inherits it (0.10 > 0.05). A6 did exactly what it exists to do: it caught
that pilot-manifest validation does not transfer to final manifests under this recipe.

## The eleven answers

**Q1 — drift cause?** Policy-relevant *recipe instability* expressed through seed variance: the
recipe does not pin gold-position structure, so per-policy structural rates (and hence the envelope)
are draw-dependent. Not policy sensitivity (the policies are deterministic and behaved per spec —
prefix_neighbor drift 0.0), and not mere bad luck to be re-rolled.

**Q2 — keep tolerance 0.05?** **Yes.** With the recipe fix below, expected drift collapses to ≈ 0
and 0.05 becomes a comfortably enforceable bound rather than a statistically infeasible one.

**Q3 — why is this not post-hoc tuning?** No tolerance change is proposed — the declared 0.05
stands untouched. The correction is on the generating process, and the failed run is retained in
full per E11 (pilot_iteration_count increments; nothing erased).

**Q4 — make the recipe less drift-prone instead?** **Yes — this is the proposed correction.**
Stratified structural-feature assignment: the recipe declares, per rung, exact counts of items whose
gold sits at the last position, at the salient endpoint, in a prefix neighborhood, and at none of
these — a fixed schedule shuffled within strata. Structural hit-rates become construction constants
(identical for pilot and final by design); A6 then verifies implementation fidelity rather than
sampling luck. The schedule constants are recipe declarations [SWEEP-PARAMETER], fixed before the
re-run, hashed with the packet.

**Q5 — malformed_control correction?** Adopt the locked joint declaration as the single source of
verdict truth. Under it, `malformed_control` is ORC-10, the semantic-separation guard: behavior =
perfect rebinding-following presented as candidate; expected = NOT_RULED_OUT **with the explicit
required-absence check** that `accuracy_indistinguishable_from_token_prior` does not attach. Its
purpose is to prove the v1 mislabeling cannot recur. If CS additionally wants a case that *must*
eliminate through a non-abstention path, that is ORC-02…05's job under the full criteria set —
no new case type needed.

**Q6 — eliminate, inconclusive, or not ruled out under the reduced set?** The question dissolves:
the reduced set is itself the defect. Under the **full** criteria set, expected = NOT_RULED_OUT with
the required-absence check (above). No oracle expectation should ever be defined relative to a
reduced criteria set.

**Q7 — why NULL-floor explanations?** Because the floor was the only criterion capable of
eliminating a non-abstaining case in the reduced run (RC-1a). Under the full set, shortcut emitters
attach `accuracy_indistinguishable_from_declared_policy_envelope` as the required label, with the
abstention-floor label as a *permitted and expected co-attachment* (a pure emitter genuinely never
abstains) — multi-attach was always the declared design; what was missing was the primary path.

**Q8 — verdict-only matching sufficient?** **No — this run is the proof.** Five detect-cases
"matched" on verdict while eliminating through an unintended label, and verdict-only matching
declared success. Corrective rule, to be locked into the oracle harness: each case declares
`required_labels` (must attach), `permitted_co_labels` (may attach), and where applicable
`required_absent_labels` (must not attach); a case passes only if outcome AND label-set conditions
hold. CS implements this as the match predicate; the NS declaration is updated to carry all three
fields per case.

**Q9 — full Phase 5 re-run?** **Yes**, under: (i) the full six-criterion T3 set with the §B
comparison rules (uniform principle: elimination requires the whole interval on the eliminating
side) and bounds fixed at the lock event; (ii) the co-signed twelve-case verdict table with
label-set matching; (iii) the stratified recipe; (iv) A6 at 0.05; (v) full-instrument oracle
validation with the eight-field record. One added precondition, encoding the process lesson:
**pre-flight refuses to run unless the co-signed verdict-table hash and bounds hash are present in
the validation config** — the same pattern as PacketLockRefused, so the lock event becomes
mechanically unskippable rather than procedurally remembered.

**Q10 — files changed?** Recipe/generator (stratified schedule + constants); T3 criteria config
(six criteria, §B comparison enums, declared bounds); oracle case definitions + the joint verdict
table (label-set fields added); oracle harness match predicate; validation config (verdict/bounds
hash preconditions); re-generated pilot + final manifests; re-populated T1/T3/T4 result fields;
IVR draft updated. Phases 1–4 acceptance is not reopened: schemas, typed boundaries, outcome model,
intervals, runner/wrapper/lock-packet machinery all stand — the changes are config, recipe, case
declarations, and one match-predicate function.

**Q11 — superseded outputs?** Phase 5 run-1 T1 per-policy/envelope results, A6 block, T3
evaluations, oracle results, and execution ledger are **superseded and retained**: per E11 they
remain in the IVR as `failed_pilot_records_retained` with `reason_for_each_repilot` =
(reduced-criteria run; unlocked verdict table; unstratified recipe; A6 drift exceedance) and
`changed_fields_between_pilots` enumerated per Q10. A passing final battery erases nothing.

## Anti-tuning attestation

The declared A6 tolerance (0.05), the per-policy cap (0.50), the envelope cap (0.80), and the §B
comparison rules are unchanged by this proposal. The single criteria-bound set is being declared
*for the first time* at the lock event, not adjusted; the run-1 numbers above are quarantined from
that declaration (bounds are derived from the declarations' pre-registered rationales, not from
run-1 outcomes), and run-1's retention in the IVR makes any later tuning visible by construction.

## Process disposition (T4 rows added)

PH5-1: joint verdict/bounds lock event held before any re-run — owner NS+CS, must-fix.
PH5-2: label-set match predicate — owner CS, must-fix. PH5-3: stratified recipe — owner CS
(NS review), must-fix. PH5-4: pre-flight hash precondition — owner CS, must-fix. PH5-5: run-1
retention block in IVR — owner CS, must-fix. All five enter T4 as OPEN with this proposal.

## Confirmations

No model was invoked. No model was loaded. No sweep_id was created. No sweep execution occurred.
No candidate/model outputs were produced. LOCK-RECORD remains PENDING. D3 is not requested; D4/D5
are not requested.

— New Senior Engineer (NS-drafted; routed to CS for co-signature, then Team Lead)
