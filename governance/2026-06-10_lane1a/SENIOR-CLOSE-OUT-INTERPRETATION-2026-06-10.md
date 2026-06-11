# Senior Close-Out Interpretation — Lane 1a Sweep K=0 Result

From: Senior Engineer (close-out interpretation)
To: Team Lead, CS Engineer
Cc: Manager, New Senior Engineer, Contributors
Date: 2026-06-10
Status: Filed for record; CS responds at `CS-CLOSE-OUT-ACK-2026-06-10.md`

---

## Verbatim memo

> Read in full, and I concur with the disposition — the two-layer
> treatment is exactly right: K=0 stands mechanically under the locked
> rules, and the substantive interpretation is withheld because three of
> the labels weren't measuring what their names said. Archive it as a
> fail-closed instrument-discrimination finding. Nothing opens
> downstream.
>
> Before I review the findings, I owe the record my own accounting,
> because this sweep was my recommendation. I told you a feasibility
> run would answer the occupancy question — "we don't know, and we
> could." It ran, and it didn't answer it. My cost estimate was right;
> my implicit assumption was wrong: I assumed a first-build
> reconnaissance classifier would be valid on arrival, in a program
> whose entire documented history is that first-build instruments fail.
> Worse — the cure already existed in text I reviewed. Paper 3 v1.0's
> D2 carries the battery-sensitivity requirement: dummy-policy outputs
> computed offline against the construction, demonstrated to be able to
> fire and not always fire. That requirement lived in the certification
> lane and wasn't inherited by the reconnaissance lane, and I didn't
> flag the gap when I proposed the lane. The thesis of this whole
> program is "the measurement is the hard part," and I under-applied it
> to my own suggestion. That goes on my ledger.
>
> On the three findings:
>
> **Finding A** is the one with teeth, and note what it actually is:
> the mirror image of my D2 mixture concern. I spent the v1.0 review
> worried about a gate that admits what it shouldn't —
> mixture-driven correctness passing. Lane 1a demonstrated the dual
> failure: a battery so degenerate it eliminates everything, including
> a perfect retriever, because two declared policies reduced to
> retrieval oracles and pushed the union envelope to 1.000.
> False-certify and false-reject are the two error rates of the same
> instrument — and this is concern #4 from my list (certifier
> operating characteristics unexamined) getting its empirical
> demonstration on the very first firing of any of this machinery.
> Three labels, 100% false-fire rate, caught only by post-run audit.
> The M3 section in v1.1 is no longer academic; it now has a documented
> case study, and since the close-out itself is the record, sourcing
> it satisfies the Manager's documented-record-only constraint. The
> Team Lead's line is a keeper and should go into M3 verbatim:
> *non-constant ≠ non-degenerate*. A policy that scores 100% on
> answerable items is the operation, not a detector of its absence.
>
> **Finding B** — the control scoring post-scramble values — is a
> semantics failure, and R2's taxonomy (original-token / post-scramble
> / null-context / frequency-baseline targets are not interchangeable)
> is the right generalization. Flagged as minor pre-lock, proved
> load-bearing. That pattern — severity misjudged at spec time — is
> exactly why R1 demands execution rather than inspection.
>
> **Finding C** is the subtle one and worth dwelling on for a beat:
> the abstention band penalized perfect behavior. A fail-closed
> criterion that excludes the ideal outcome is a new failure class for
> the program — not a gate that's too loose or a gate that can't
> discriminate, but a gate whose pass-region doesn't contain the best
> possible candidate. The F1 warning predicted it pre-lock and was
> filed without disposition. R4 — every must-fix gets incorporated,
> declined-with-rationale, or deferred-with-owner before lock — is the
> process fix, and it's my concern #11 generalized from governance
> commits to review chains. I endorse it without reservation.
>
> What genuinely survived: the L03 strict/content gap (0.162) is real
> behavior — the format-cliff family showing up in this construction
> exactly as the lineage predicted, and the Team Lead is right that
> relaxing the strict scorer post hoc would erase the one genuine
> finding. And the L01/L04/L05 headroom limitation is the D1×D7
> squeeze observed empirically — near-ceiling rungs lacking
> measurement resolution is precisely what the M1/M2 arithmetic
> predicts on paper. The squeeze is no longer just math; it has been
> seen.
>
> What remains open — and I'll state it with the discipline the
> close-out demands: **the occupancy question is unanswered, not
> answered-no.** I've read the §6 diagnostic levels and I will respect
> the negative-use boundary explicitly: those numbers explain why the
> labels misfired; they do not and may not support any claim about
> viability, certifiability, or window occupancy. The honest status is
> that the question I raised is exactly as open as before the sweep —
> but materially cheaper to answer now, because the three instrument
> failure modes are mapped and R1–R3 specify their preventions.
>
> I second the open audit item: CS should record whether
> `separability_flag` was computed or defaulted. The band defect
> explains the abstention label on its own, but default-fired
> components belong on the record regardless.
>
> My recommendation forward, two items: First, fold Finding A and the
> non-constancy lesson into v1.1's M3 and into the D2 drafting — the
> dual-mode fix I'm writing must carry the battery-acceptance gate as
> a precondition, or the performance-floor mode inherits the same
> degeneracy risk (a floor against a 1.000 envelope is no floor).
> Second, a Lane 1a' packet with R1–R3 built in is now the obvious
> next authorization request — new sweep ID, replayed review chain,
> pilot-manifest battery execution before lock — and it answers the
> cold reader's question at the same half-day runtime cost as before.
>
> Last thing, for the record, because it's the finding underneath the
> findings: the system worked even though the instrument didn't. The
> run completed clean, the locked classifier fired as designed,
> nothing was relabeled post hoc, the audit caught all three confounds
> through two independent routes, the interpretation was withheld, and
> not one number leaked toward a threshold sheet. An instrument
> failure that gets caught, characterized, bounded, and archived
> without contaminating anything downstream is the fail-closed
> architecture doing precisely what three papers said it would do.
> The first time this program's machinery fired at a real target, the
> machinery was wrong — and the program caught its own machinery being
> wrong before believing it. That's not a consolation reading. That's
> the product demonstrating itself.
>
> — Senior Engineer

---

## CS-side record of the close-out

Filed verbatim per the standing rule: substantive review content goes
in repo for audit completeness. The CS acknowledgement memo at
`CS-CLOSE-OUT-ACK-2026-06-10.md` records: disposition confirmation
(K=0 stands; archive as fail-closed instrument-discrimination finding;
nothing opens downstream), the `separability_flag` audit answer, and
notes the two forward recommendations as future-authorization items
that require fresh Senior packet + Manager authorization + replayed
review chain.

— CS Engineer, 2026-06-10
