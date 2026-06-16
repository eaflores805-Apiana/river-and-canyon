# OPEN QUESTION FOR TEAM INPUT — The FP16 Off-Map Mass

**E. A. Flores**, Apiana AI, Inc. — June 16, 2026
*River and Canyon · Path A. Drafted by the Senior Engineer; routed by the Manager.*
**To:** C4 · New Senior · CS Engineer · C5 · C6 · Team Lead

> **Status.** A problem statement circulated for **independent input**. This is **not** an authorization request, **not** a proposal to ratify, and **not** a request to confirm a conclusion. The FP16 constructibility run FAIL (commit `265114b`) is closed and unchanged; nothing here reopens it.
>
> **Why this memo is structured the way it is.** We want genuine reads, not agreement. The most useful thing you can return is a reason the framing below is *wrong* — a better decomposition of the question, an explanation we're not considering, or a case that this isn't worth pursuing at all. Those returns are weighted **higher**, not lower. If you find yourself supplying the answer you think we want, that is the failure mode this memo exists to avoid.

---

## 1. What we observe (measured; positional; not in question)

Stated deliberately in positional terms — *where the tokens sit* — with no mechanism implied:

- The FP16 run FAILED (locked, via the dominant-signature branch).
- 40% (38/96) of composite responses were off-map ("R6cat").
- All 38 are **on-page decoy-chain entities**: 33 sit at decoy **answer-positions** (depth-2, wrong chain), 5 at decoy **bridge** positions; **0** are novel tokens; **0** are format-variants of the correct answer. Reproduced independently by two seats from the committed bytes.
- The engineered confounds stayed quiet (terminal-grab 4%, depth-competitor 0/96, direct-recall 0, constant-token 0). Single-fact retrieval was unreliable under the clutter (hop1 0.74, hop2 0.68).
- This is **per-construction-at-this-load**, **n=1**, **not** a capability claim.

That much is settled. Everything below is not.

## 2. The open question — *including whether this is the right question*

We have been decomposing it as: **when the model emits a decoy answer-position token, did it (a) *traverse* the decoy chain, or (b) *grab* the node by position/depth/salience?** The current run cannot separate these — the decoy chains were never independently queried, so both mechanisms produce the identical token with the identical address.

**But that decomposition is our choice, and it is on the table to be challenged.** Genuinely open, and we are not pre-committed to any of these:

- Is (a)-vs-(b) the right way to carve this, or is there a better decomposition?
- Is there an explanation for the off-map mass that we are not considering at all?
- Is *"why the 40%"* even the question worth asking — or is the positional finding (§1) already the useful product, with the mechanism question a time sink?

## 3. One candidate approach — offered for critique, **not** for adoption

> **Authorship disclosure:** this path was developed primarily by the Senior Engineer, who has a stake in it. Weight accordingly. It is presented so you can attack it, not so you can approve it. We may be wrong about its value, its ordering, or its premises.

A free → cheap → expensive ladder:

1. **Byte-only analyses on existing data** (no run): do the 38 grabs cluster by *proximity* to the target answer, by *position*, or by *relation-signature overlap*? Do they persist on the same item's other queries? — narrows the space at zero cost.
2. **A characterization sweep** (vary load *k*, decoy count *D*, relation overlap, position): *maps* the phenomenon. Descriptive, light ceremony, time-expensive. Would report the **validated, controls-gated** metric (per Paper 1, *survival is not correctness*), not a retention/survival score.
3. **A locked decoy-control study** (query the decoy chains with their own hop1/hop2/direct-query battery): the only design that begins to separate (a)/(b). Heavy lock-before-look. **Asymmetric ceiling** — it is better at *acquitting* traversal (decoy-components-not-retrievable but grabbed → leans grab) than at *convicting* it (retrievable-on-demand does not prove the grab *was* a traversal). Even a clean result is a *lean*, never "the model composes."

We think this is reasonable. We are not asking you to agree.

## 4. What we are asking (open prompts, not a checklist to endorse)

Return your independent read. These are prompts to provoke thought, not statements to ratify:

- **Is the question posed right?** If not, how would you pose it?
- **What explanation are we not considering?** What would a mechanism other than (a)/(b) look like?
- **Would you pursue this at all** — given n=1, per-construction, and a closed FAIL? What is the opportunity cost against the program's other open work?
- **If you would pursue it, how** — and what specifically would convince you the question is *answered* (or *unanswerable*)?
- **Where does our §3 approach inherit an assumption we haven't flagged?** Where would it confound itself?

## 5. What this is not

- Not an authorization request. Any run is the Manager's call, by name, on a locked pre-registration — this memo is upstream of that.
- Not a request to confirm a conclusion. If the honest read is "you are chasing a non-finding, file §1 and move on," that is the single most valuable return.
- Not a reopening of the FAIL, which stands.

---

*Routing note: returns go to the Team Lead for synthesis. The drafting seat (Senior) will not adjudicate the returns to its own approach — that synthesis is the New Senior's / Team Lead's, precisely because the Senior has the stake disclosed in §3. Authorization of any resulting study remains the Manager's, by name. This memo certifies nothing and authorizes nothing.*

— Senior Engineer (drafting)
