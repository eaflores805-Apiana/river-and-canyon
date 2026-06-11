# New Senior Stratified-Recipe Blocker Adjudication (v0.1)

```text
DRAFT / REVIEW ONLY — PH5-1 BLOCKER ADJUDICATION
NO EXECUTION OCCURRED · NO MODEL INVOKED · NO SWEEP_ID CREATED · LOCK-RECORD PENDING
CORRECTIVE RUN-3 REMAINS GATED UNTIL THE REVISED JOINT RECORD PASSES TEAM LEAD FILTER
```

To: Team Lead, CS Engineer · Cc: Senior Engineer, Manager · From: New Senior Engineer · 2026-06-11

## 1. Decision

**Item-label disjointness is sufficient — Option A — and is also the only constructible option.**
CS's construction is accepted. This is not a concession to implementation convenience; policy-hit
disjointness between `pure_last_position` and any recency-adjacent construction is **geometrically
unconstructible** under this task, shown by exhaustive case analysis (verified by computation,
session record):

For `recency_excluding_target` to hit, the most recent non-target pair must carry gold's value
(deliberate duplication — under per-manifest value uniqueness no non-target pair's own value equals
gold). There are exactly two placements of the target pair, and both co-hit: (Case 1) target not at
last position → the most recent non-target pair *is* the last pair → the duplication puts gold's
value at the last position → `pure_last_position` hits. (Case 2) target at last position →
`pure_last_position` hits via the target's own value → the second-to-last duplication makes recency
hit too. Every recency-adjacent hit therefore co-occurs with a `pure_last_position` hit. Demanding
policy-hit disjointness (Option B) is demanding the impossible; achieving it by redefining the
policy (Option C, e.g. a pure "second-to-last value" proxy) would change a co-signed control's
declared semantic target to solve a problem the instrument does not have — rejected as heavier than
the disease.

## 2. Why this preserves the instrument's intended semantics (not merely the envelope number)

The Team Lead's key question, answered directly: **the semantics survive because the eliminative
machinery is union-based and overlap-insensitive.** The envelope criterion asks whether candidate
accuracy is explainable by *the set of items any declared policy resolves* — a union, unchanged by
co-hits. The per-policy caps ask whether any single policy approaches operation level — 0.30 is a
deterministic constant comfortably under 0.50. The co-hits themselves are not artifact: a
recency-biased model and a position-biased model genuinely make the same prediction on those items;
the overlap is real structure in the shortcut space, and the recipe now represents it honestly
instead of pretending the explanations are separable where they are not. Nothing the instrument
computes — envelope, caps, classification, A6, any criterion — depends on hit-disjointness.

## 3–4. Expected values under the accepted construction (all deterministic constants)

```text
union envelope:              48/80 = 0.60   (item-label construction; unchanged)
pure_last_position:          24/80 = 0.30   (its 12 + the 12 recency co-hits; < cap 0.50)
salient_endpoint:            12/80 = 0.15
recency_excluding_target:    12/80 = 0.15
prefix_neighbor_confusion:   12/80 = 0.15
expected A6 drift:           0.00 under faithful implementation (all rates remain
                             construction constants; identical pilot/final schedule)
```

Oracle-verdict stability re-verified by computation under pure_last = 0.30: ORC-02 (cand−env CI
[−0.434, −0.146], fires) ELIMINATED ✓; ORC-11 (blend acc 0.475, CI [−0.271, +0.029], fires)
ELIMINATED ✓; ORC-12 (blend acc 0.825, CI [+0.085, +0.354], does not fire) NOT_RULED_OUT ✓ — with
the lower bound now straddling the 0.10 margin, so a `boundary_proximity_flag` on the ENV criterion
is *expected-permitted* for ORC-12, exactly as the locked table already states. **No verdict, label
set, or bound changes.** One honest note for the record: the per-policy cap margin on
`pure_last_position` halves (0.30 vs 0.50, formerly 0.15 vs 0.50) — still ample, and the cap value
does not move.

## 5. Required changes before run-3 (text only; no locked artifact mutates post-lock because none is locked yet)

(a) Joint lock-event record §3 (NS-owned text, unsigned by CS, my signature conditional —
revising now is pre-lock and clean): the schedule paragraph replaces "per-policy structural rate
0.15" with the table above and adds, verbatim per the Team Lead instruction: *the schedule is
item-label-disjoint, not fully policy-hit-disjoint; the union envelope remains 48/80 = 0.60 by
intended item-label construction; pure_last_position is expected to measure 24/80 = 0.30 under the
accepted construction; 0.30 remains below the per-policy cap of 0.50* — plus the impossibility
rationale by reference to this adjudication. (b) The lock-event package §2 rationale is superseded
on the "0.15 exactly each" claim by this adjudication (supersede-don't-rewrite; the package remains
in the library marked accordingly). (c) No change to: verdict table v0.3, bounds, blends, policy
definitions, schemas, or any Phase 1–4 artifact. (d) CS's A6 expectation table updates
pure_last_position's expected constant to 0.30.

## 6. Anti-tuning statement

The change is geometry-forced and was discovered before run-3 by the lock-event process working as
designed; no value moves toward any outcome. The envelope (0.60), every cap (0.50/0.80), every
bound, every blend, and every verdict are unchanged; the only revision is the *description* of a
rate the construction itself determines. The corrected rate (0.30) is a derived constant, not a
chosen parameter, and it is declared here before any run-3 artifact exists.

## 7. May CS proceed?

**Yes.** Upon applying §5(a)–(d), CS may finalize the joint lock-event record (slots + signature);
my conditional signature extends to the revised §3 text as specified here. The record then goes to
Team Lead filter; run-3 remains gated until that PASS, per standing direction.

## 8–11. Confirmations

No execution occurred. No model was invoked. No sweep_id was created. LOCK-RECORD remains PENDING.

— New Senior Engineer
