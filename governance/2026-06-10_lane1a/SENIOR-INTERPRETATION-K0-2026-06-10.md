# Senior Interpretation — Lane 1a Sweep Result (K = 0)

From: Senior Engineer (outgoing seat; routed Senior → Team Lead per protocol)
To: Team Lead; Cc: CS Engineer, Manager, New Senior, Contributors · 2026-06-10
Method: all claims below verified against committed artifacts at `ec7390f` — sweep_record.json
(raw-bytes sha256 `f10f777c…` recomputed), prompt_template.md, manifest_generator.py,
dummy_policies.py, analyzer.py. No claim in this memo rests on the summary alone.

## 0. Headline

The labels fired mechanically correctly on the recorded values — **and for three of the four label
types, the recorded values are instrument tautologies, not model behavior.** The model's own behavior
in the same record is consistent with healthy retrieval. K=0 stands as the registered outcome; its
evidential content about the certification window is near zero; its evidential content about the sweep
instrument is large and specific.

## 1. (TL Q1) Are the labels consistent with the artifacts? Mechanically, yes

L01 arithmetic, from the record: strict .963 (SE .021), control .925 (SE .029) → |diff| .038 ≤
2·SE_diff = .072 → token-prior label fires. union_envelope 1.000 → strict ≤ 1.0 + 2·SE trivially →
envelope label fires. abstention_rate 1.000 ∉ [0.50, 0.95] → abstention label fires. headroom: .963 ≥
1 − 3(.021) = .937 → fires. Every label is a correct application of the locked rules. The problem is
upstream of the rules.

## 2. (TL Q2/Q5) Three instrument findings, each confirmed in code

**Finding A — two dummy policies are accidental oracles → envelope label is tautological.**
`homogeneous_prefix_completion` scans all in-context keys for the longest common prefix with the
queried key. On every answerable item, **the queried key itself is in the list** and matches itself at
full length → the policy returns the queried key's own value → correct on 100% of items, every rung,
by construction. `target_recency` (first-character match) oracles the same way on K=low, where the
recipe guarantees unique first letters — the only candidate is the queried key itself. Hence
max_dummy = union_envelope = 1.000 on all 8 rungs, and "indistinguishable from declared policy
envelope" fires on any result whatsoever. My requirement-8 acceptance gate (every policy yields
well-defined, *non-constant* predictions) passed both oracles — distinct predictions, all correct.
**The gate I specified has a missing dual: a battery that cannot fire is uninformative, and a battery
that always fires is a tautology. Both ends need generation-time ceilings.**

**Finding B — the control's gold is the post-scramble answer → token-prior label is tautological.**
manifest_generator.py, answerable_mirror branch, verbatim comment: *"After scrambling, the 'correct'
answer is whatever value is now at the queried key's position."* The control therefore scores
retrieval competence on a shuffled list — the same skill as the candidate condition — not
answer-without-signal. control_acc ≈ strict_acc everywhere (.76–.975) is the predicted signature, and
it is what the record shows. The design intent (gold = the *pre-scramble* target, so that matching
after scramble ≈ prior) was reinterpreted at implementation; §13 pinned the manifest recipe but never
pinned the control's scoring target line. That specification gap is mine as much as anyone's.

**Finding C — the abstention band penalizes perfection, and separability defaults to False.**
abstention_rate = 1.000 on all rungs means the model abstained on **16/16 NULL items, every rung** —
perfect contract compliance — while answering the answerable stratum (strict .71–.99). My §1.6 band
[0.50, 0.95] caps at 0.95, so the label fired *because the model was perfect*. (The Team Lead memo's
plain reading — "the model answered when it should abstain" — is inverted; the field is NULL-stratum
abstention, and 1.0 is ideal.) Secondary latent bug: analyzer reads
`raw_outputs.get("separability_flag", False)` — an unpopulated flag fires the label by default.
Fail-toward-labeling is the safe direction for negative use, but a label that can fire from absence
of computation is still an instrument defect.

## 3. (TL Q3) What the model actually did — the data under the tautologies

Strict accuracy degrades gradedly and sensibly: .963 → .825 → .713 across D = 4/8/16 at K-low;
.988 → .912 → .850 at K-high; extended context costs a little (.850/.887). NULL abstention perfect.
And one **genuine behavioral signal**: L03 (D=16, K-low) fired `strict_content_gap_instability` with
content − strict ≥ .15 at strict .713 — a format cliff at high distractor count, content preserved
while strict formatting degrades. That is a real, pre-registered, correctly-detected observation that
echoes the Paper 1 dual-scoring taxonomy, and it is the one elimination label in this sweep that
reflects model behavior.

## 4. (TL Q4) Limitations and the honest statement of result

The §5 scope limits all stand. Add one: **this sweep demonstrates the instrument's non-discrimination
at this design point, not the window's unoccupancy.** The registered statement "the certification
window … was unoccupied" is mechanically valid as the locked boolean's output and should be recorded
as such — accompanied in the same breath by the finding that three of its supporting label types were
tautological. Negative-use doctrine held throughout: over-elimination cannot promote anything, no
survivor set exists to leak into selection, and the governance design proved fail-safe in exactly the
direction it was built to fail.

## 5. (TL Q5) Recommended audit confirmations (read-only, cheap)

(a) CS prints the per-policy score breakdown per rung — prediction: homogeneous_prefix 1.0
everywhere; target_recency 1.0 on K-low rungs. (b) CS states separability_flag provenance (computed,
or defaulted-False). (c) Spot-check three raw NULL outputs to confirm "NULL" emissions back the 1.0.
(d) Confirm answer_pos_distribution per rung passed its ≤3σ check (field present; value unexamined).

## 6. Disposition recommendation (interpretation only; nothing authorized)

Record K=0 as the registered sweep outcome with this memo's findings attached as the post-run
instrument audit. The result is a **completed negative result about the instrument**, publishable in
the program's negative-result form, and it adds a third structural lesson to the family: G1 (delivery
must be tested), sibling cross-reference (agreement must be tested), and now **discrimination must be
tested** — a diagnostic battery needs both a can-fire floor and a cannot-always-fire ceiling, gated at
generation time. Any Lane 1a′ redesign — control gold pinned pre-scramble, policy-correctness ceiling,
two-sided abstention contract over both strata, band [0.50, 1.00], separability computed-or-absent —
is a **new packet under fresh Manager authorization**, exactly as §1.12 and the standing rules already
require. No such redesign is proposed or implied by this memo.

The sweep's *bookkeeping* deserves its sentence: 1,536/1,536 planned generations, zero anomalies, zero
re-executions, 32/32 sidecars, locked hashes end to end, 12.9 minutes. The provenance machine worked
perfectly. The measurement semantics inside it had three bugs, and the record it kept is exactly why
we can prove that.

— Senior Engineer
