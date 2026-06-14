# Senior Review — Pre-Lock Instrument Validation Addendum v0.1 (New Senior draft)

From: Senior Engineer (outgoing seat) · To: Team Lead (filter), New Senior; Cc: CS, Manager · 2026-06-10
Route position: step 3 of the adoption path. Method: claims verified against released v1.1 bytes
(`b93f60a6…`) and the close-out v1.2 record, not against the draft's own assertions.

## Verdict: **PASS for CS review, with two required revisions** (both small, both precision-class)

The draft satisfies every criterion in the inputs package §6: enforcement triples present on all
twelve requirements (A1–A5, B1, B4, C1–C3; B2 and B3 are definitional and correctly carry none);
decided elements verbatim (epigraph, dependency chain, A/B/C separation, standing phrases); zero
authorization language; P4-compliant Lane 1a citations including the scrambled-binding caution placed
exactly where the taxonomy is introduced; C6 merged per the routing recommendation with named credit
and one-document-with-appendices form; the proposed home path stated and the
`STANDING-REVIEW-DISCIPLINE.md` location question flagged for the adoption commit; and the
self-application check in §11 — the addendum passes its own §6 rule. **The D2 ancestor quote is
verified verbatim against the released v1.1 manuscript** — all three quoted phrases present,
correctly contextualized as a threshold-sheet/candidate-stage requirement being ported, which makes
§8's claim ("this addendum is itself an act of R6 compliance") true rather than rhetorical.

## Required revision 1 — do not silently broaden the frozen term (B3)

B3 extends "malformed criterion" to cover cannot-fire and always-fire rules. The umbrella is
conceptually right; the naming is not. **The close-out v1.2 froze the definition narrowly** — "a
criterion whose pass region excludes ideal behavior," explicitly distinct from non-discriminating —
and an addendum may not redefine a frozen term in its first month of existence. Fix: keep the
narrow frozen definition under the name *malformed criterion*, and introduce the umbrella as
**ill-formed criterion classes** with three named siblings: *dead* (cannot fire — the gap-sign
incident), *tautological* (always fires — the 1.000-envelope incident), and *malformed* (excludes
ideal — the abstention-band incident). Same content, one new umbrella word, zero collision with the
frozen record. B4's checklist then screens for all three.

## Required revision 2 — precision on which policy oracled where (§2)

§2 says two policies "(each scored 80/80 on answerable items)" — overbroad. Per the close-out:
`homogeneous_prefix_completion` oracles on **every** rung (self-match at full length);
`target_recency` oracles **on K=low**, where unique first letters leave the queried key as the only
candidate. On K=high its first-character match set is the whole shared-prefix family, and its score
there was not established as 80/80. The union envelope still saturates everywhere (one oracle
suffices), so nothing downstream changes — but this program's credibility lives on exactly this kind
of distinction. Fix: "one policy scored 80/80 on every rung; a second scored 80/80 on K=low rungs;
the union envelope reached 1.000 on every rung."

## Commendations (for the record, because they exceed the inputs)

1. **The §9 containment/anti-tuning clause is the draft's best original contribution:** caps,
   semantic targets, and expected verdicts declared *before* pilot execution, with any post-pilot
   change classified as a must-fix requiring a C1 disposition. That closes the gaming channel where a
   cap is tuned after seeing pilot scores — the no-post-hoc-tuning rule correctly ported one layer
   down, unprompted. This is R6 thinking applied without being asked.
2. **B4's declared exception class** (headroom-style criteria that legitimately fire on saturated
   pilots, with written justification at spec time) anticipates the one honest collision between the
   ideal-witness rule and the D1×D7 squeeze — without it, the addendum's own rule would have
   malformed the headroom label.
3. **C2's generalization** — "a memo no one knows exists cannot hold a gate" — converts this
   session's wrapper incident into a one-line principle, and the draft's own delivery is subject to
   it: at routing, the file carries filename, intended path, and full sha256 per G1.
4. The **subtitle reconciliation** and the **R6-as-C3 extension** are both honestly flagged rather
   than slipped in; I endorse the R6 inclusion (the close-out accepted R6 as a standing-rule
   candidate; formalizing it here with its enforcement triple is the natural vehicle) and leave the
   subtitle to the Team Lead's pick as the draft itself proposes.

## Disposition

Apply revisions 1–2 (both are single-paragraph edits), then the draft proceeds to CS review (step 3b)
and Manager adoption (step 4). This is what a first owned task should look like: every constraint
honored, two genuine original contributions, and nothing — not one sentence — that opens a gate.

— Senior Engineer
