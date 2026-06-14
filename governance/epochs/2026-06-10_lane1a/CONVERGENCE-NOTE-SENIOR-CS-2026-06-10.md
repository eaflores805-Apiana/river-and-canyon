# Convergence Note — Lane 1a K=0 Interpretations (Senior × CS)

From: Senior Engineer (outgoing seat; routed Senior → Team Lead)
To: Team Lead; Cc: CS Engineer, Manager, New Senior, Contributors · 2026-06-10

## 1. Convergence — two independent routes, one conclusion

The Senior interpretation (code-mechanism route) and the CS interpretation at `dd1c175`
(quantified-scores and raw-output route) were produced independently and agree on every substantive
point: labels mechanically valid; three of the labels tautological for instrument-side reasons; model
behavior textbook. The evidence now interlocks: I located the causes in code (the self-match in
`homogeneous_prefix_completion`; the verbatim post-scramble comment in the control branch; the §1.6
band cap), and CS quantified the effects in data (target_recency and homogeneous_prefix at 80/80 on
every rung while the honest policies sit near position-chance; control items retrieved correctly
against post-scramble gold; three raw NULL outputs literally emitting "NULL"). Prediction and
measurement match exactly — including the 13/80 ≈ chance scores for the policies that were working as
intended. This is what a correct diagnosis looks like from two directions.

## 2. One caution on the revision sketch: do not relax the strict scorer

CS's list of candidate revisions is right on three of four items (corrected dummy battery, corrected
control gold, widened abstention band). The fourth — "relaxed scorer for 'key: value' format" — should
NOT be adopted. The L03 format cliff (gap 0.162; model emitting `key: value` where the contract says
value-only) is the **one genuine behavioral finding of this sweep**, and it exists precisely because
the dual-scoring discipline separates strict-format compliance from content correctness. Relaxing
strict to absorb the format deviation dissolves the finding by definition — the Paper 1 lesson in
reverse. Any Lane 1a′ keeps the dual scorer as-is; the gap label was the instrument *working*.

## 3. Consolidated audit items and dispositions

(a) Per-policy score table — DONE (CS, finding A quantification). (b) Raw NULL spot-check — DONE (CS,
3/3 "NULL"). (c) `separability_flag` provenance — OPEN: analyzer reads
`raw_outputs.get("separability_flag", False)`; CS to state whether it was computed or defaulted for
this sweep (one sentence; the abstention label fired on the band either way, but a default-fired
component should be on the record). (d) `answer_pos_distribution` not populated — CONFIRMED by CS as
an analyzer-driver omission; position uniformity for the lane-1a-2026-06-11 population therefore
rests on generator code plus seed determinism rather than a recorded histogram. Fully recoverable
offline: the manifests are bit-reproducible from the locked seed, so the histogram can be computed
read-only at any time without touching the sweep. Record as a bookkeeping gap, not an evidence gap.
(e) CS's proposed analyzer warning at union_envelope = 1.000 — ENDORSED, generalized: that warning is
the analysis-time face of the same rule whose generation-time face is the policy-correctness ceiling.
Both belong in any future packet's spec: **a diagnostic battery needs a can-fire floor and a
cannot-always-fire ceiling, checked at generation time and warned at analysis time.**

## 4. Recommended record (interpretation only; nothing authorized)

Record, together, as the Lane 1a result of record: (1) the K=0 mechanical outcome with its locked
fixed-outcome statement; (2) both interpretation memos and this convergence note as the post-run
instrument audit; (3) the statement that the sweep constitutes a completed negative result **about the
instrument's discrimination at this design point**, with the L03 format cliff as its one behavioral
observation; (4) the lessons entry — delivery must be tested (G1), agreement must be tested (sibling
cross-reference), environment must be tested (production-path smoke), and now **discrimination must be
tested** (two-sided battery gates). Lane 1a doctrine held end to end: negative-use only, no survivor,
no leak, fail-safe in the built direction. Any Lane 1a′ is a new packet, fresh authorization, new
sweep_id, full review chain — exactly as CS's memo also states. Neither memo advocates it; both make
it cheap to do correctly if the Manager ever wants it.

— Senior Engineer
