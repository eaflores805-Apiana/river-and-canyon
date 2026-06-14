# Lane 1a′ D2 Packet-Stage Design Materials (v0.1)

```text
DRAFT / REVIEW ONLY
D2 PACKET-STAGE ARTIFACT (D2 APPROVED; D3/D4/D5 NOT APPROVED)
NO SWEEP EXECUTION AUTHORIZED
NO MODEL RUNS
NO NEW SWEEP_ID
NO TOKEN-PRIOR GENERATIONS (D4, BY NAME, ONLY)
DECLARATIONS POPULATED; NO VALIDATION RESULT FIELDS POPULATED BY THIS SEAT
```

*New Senior Engineer, 2026-06-11. Resolves or dispositions the eight OPEN-at-D2 items (Manager D2
authorization §2). Every numeric value below is a **[SWEEP-PARAMETER — NOT A THRESHOLD VALUE]**,
adjustable at review before lock, never after. Joint items are marked PROPOSED pending CS co-owner
sign-off. One boundary question is surfaced in §9 per the Manager's §3 mechanism.*

## 1. Prompt-shell visibility for `unconditioned_token_prior` — RESOLVED (proposal)

**Decision proposed: pool-visible shell.** The control prompt preserves the full format contract and
the instruction block, lists the declared value pool as the valid-answer set, omits the queried key,
and removes all bindings. **Rationale:** with the pool visible, the chance floor is defined and
non-degenerate — expected baseline = 1/|value_pool| (= 1/26 ≈ 0.038 [SWEEP-PARAMETER]) — so the
separation criterion has a real referent. The pool-invisible alternative drives the baseline toward
the model's open-vocabulary prior (≈ 0), which makes separation trivially large for any candidate
and the criterion tautological — exactly the ill-formed class T3 exists to screen out. T2's
`expected baseline` field is now derivable from declared semantics, not assumed, per E11.

## 2. T1 cap declarations and statistical rationale — DECLARED (pre-pilot, anti-tuning rule in force)

- **Per-policy cap: 0.50** [SWEEP-PARAMETER]. Rationale: intended structural hit-rates for the
  corrected battery are ≈ 1/(D+1) ∈ [0.06, 0.20] by construction; 0.50 sits ≥ 2.5× above the highest
  intended rate (margin against sampling variation at N=80, Wilson interval half-width ≈ 0.11 at
  p̂=0.5) and unambiguously below operation level (1.0). A policy at ≥ 0.50 is answering half the
  items: operationally entangled regardless of mechanism.
- **Union-envelope cap: 0.80** [SWEEP-PARAMETER]. Rationale: expected corrected-battery envelope is
  ≈ the sum of largely disjoint structural hit-rates (≲ 0.45); 0.80 preserves ≥ 0.20 declared
  measurement room below saturation — *a floor against a 1.000 envelope is no floor* — while not
  tripping on benign overlap.
- **IS-7 drift tolerance: |pilot − final| ≤ 0.05** per policy and for the envelope [SWEEP-PARAMETER];
  exceedance sets `drift_flag` and is a must-fix with C1 disposition before lock.
- Battery coverage minimum: ≥ 4 discriminative policies after classification (the corrected battery
  fields 4 envelope policies + `copy_completion` outside it).
Declared now, before any pilot exists — the anti-tuning rule timestamp is this document.

## 3. INH-1 per-diagnostic stratum semantics — PROPOSED DISPOSITION (joint: New Senior + CS)

| diagnostic | stratum | denominator |
|---|---|---|
| strict / content / gap | answerable | N_eff = 80 − void_answerable |
| policy floors, union envelope, envelope separation | answerable | N_eff (same items as candidate scoring) |
| token-prior control comparison | answerable-mirror controls | 80 − void_control |
| abstention floor | NULL | 16 − void_null |
| abstention ceiling | answerable | N_eff |
| measurement headroom | answerable | N_eff |
| void accounting | pooled 96 | N_declared |

Nothing else computes over pooled 96. Per-stratum N_eff is recorded per rung in the per-rung record.

## 4. INH-2 outcome-chooser totality — PROPOSED DISPOSITION (joint: New Senior + CS)

Fixed evaluation precedence: (1) `inconclusive_not_actionable` — preempts, exclusive, rung excluded
from K and reported separately; (2) elimination labels — multi-attach, each per its locked rule;
(3) `requires_further_investigation` — attaches iff measurable and no elimination label attached.
Non-eliminated predicate: `labels(rung) == {requires_further_investigation}` (equality, not subset).
Outcome chooser: `K = |{rung : labels(rung) == {RFI}}|`; exactly one fixed statement emits — the K=0
reconnaissance-negative statement, or the K≥1 unordered statement with the single-non-eliminated-rung
sentence appended iff K=1 among evaluable rungs. **Totality obligation:** every rung maps to exactly
one of {inconclusive, eliminated, non-eliminated}; CS encodes this as a unit-tested exhaustiveness
property, not a convention.

## 5. INH-3 SE interval method — PROPOSED (joint: New Senior + CS; not selected until packet review)

**Wilson score intervals** for all binomial proportions; **Newcombe–Wilson hybrid** for differences
(the token-prior separation criterion). Rationale: small strata (NULL n=16) and boundary proportions
make Wald degenerate — at the ideal corner (NULL abstention p̂ = 1.0) Wald SE = 0, which would have
re-created the v1 pathology in interval form; Wilson is boundary-correct at these N. Jeffreys is the
named fallback if CS implementability review prefers it. Never silently Wald — and never loudly
Wald either.

## 6. D4 token-prior gate — CARRIED (no change)

Token-prior generations remain closed; opened by Manager **by name** at D4 only; the LOCK-RECORD
slot stands. This document populates the control's *declarations*; it generates nothing.

## 7. OPT-2 — DISPOSITIONED non-blocking

Remains in the CS optional register, not elevated by either owner; available for elevation at Team
Lead/CS discretion per the assembly memo.

## 8. Remaining register items — DISPOSITIONED

AL-Q1 / AL-Q2-schema / AL-Q4 landed in CS-EP v0.2 (CS-confirmed); AL-Q5-opt remains a Team Lead
preference on the LOCK-RECORD sub-block; AL-INH-1/2 co-ownership is exercised by §§3–4 above;
IS-7 now carries the declared tolerance (§2); IS-8 cross-referenced in the design packet (lock-time
hard refusal); IS-9 veto path remains reserved to CS through packet review; OPT-1/3 non-blocking.

## 9. Boundary question surfaced per Manager §3 (before any offline validation executes)

The D2 non-authorization list omits *offline pilot execution*, *oracle pre-flight execution*, and
*manifest generation* — three categories the assembly-stage memo explicitly banned — while §1.2
authorizes "populating T1–T4 as appropriate" and §6.6 anticipates a Validation Report "draft or
completed packet-stage form." The coherent reading: **D2 opens model-free validation work** (pilot
manifest construction; deterministic dummy-policy execution; oracle pre-flight of the instrument
against synthetic records) while keeping every model-touching category closed. Per §3's own
mechanism, we proceed on declarations now and request **explicit confirmation of that reading**
before CS executes any offline pilot or oracle pre-flight. If confirmed, the only remaining
execution-side categories stay: model runs (closed), token-prior generations (D4 by name), sweep
(D4). If not confirmed, T1/T3 result fields remain empty into D3 and the Validation Report returns
as a draft form. Nothing model-free has been executed by this seat either way.

## 10. Confirmations (Manager §6 items 10–12, this seat)

Executed under D2 by this seat: document preparation only. No sweep execution occurred. No model
runs. No sweep_id was created. No token-prior generations. No validation **result** fields were
populated — §§1–5 populate *declarations* (caps, semantics, methods, rationale), which the standing
addendum requires to exist before any validation executes.

— New Senior Engineer (to Team Lead + CS for cross-review; D3 not requested)
