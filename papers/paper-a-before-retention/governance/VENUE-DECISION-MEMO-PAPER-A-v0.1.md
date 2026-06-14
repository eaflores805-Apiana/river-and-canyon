# VENUE-DECISION-MEMO-PAPER-A-v0.1

**Version:** v0.1. River and Canyon program. Decision-surface memo for the Manager.
**Status:** model-free. Surfaces a venue-category decision that the v0.3 restructure made implicitly and that should be ratified explicitly. Anchored on origin/main HEAD 0f7e9a7. Authorizes nothing.
Routing: Senior (surfaces) → Team Lead (route) → Manager (decision).

---

## Why this memo exists

The v0.3 restructure of Paper A (PAPER-A-DRAFT-v0.3, "The Gate That Refused Its Authors") made a venue-category choice without it being decided as such. Specifically: it folded the D1–D7 protocol specification into §4 as architecture-with-status (each gate labelled implemented-and-exercised or specified-but-unbuilt) rather than presenting it as a standalone methods protocol. That structural choice commits the paper to one lane. The choice is, in Senior's judgement, the right one — but a venue-category decision should be ratified by the Manager, not defaulted into by a drafting move.

## The decision

```text
Confirm the venue/contribution category for Paper A:
  LANE 1 (what v0.3 is built as): instrument / measurement / experience contribution.
    Claim = "a fail-closed validity-gate architecture, a coherent implemented subset,
    and a worked refusal demonstration, scoped to one family / one model / pre-stress."
    The gate set is architecture-with-status; non-vacuousness rests on the worked
    refusal; scope and the own-baseline limitation are stated in the body.
  LANE 2 (what v0.3 is NOT built as): novel-method contribution.
    Claim = "a new method, validated." This lane would require the D1–D7 spec as a
    methods protocol with per-gate validation, an external demonstration, and ideally
    a stress rung — i.e. much of Paper B's content folded forward.
```

## Why Lane 1 is the right call (Senior's recommendation, for ratification)

```text
- It matches the evidence. The program is pre-stress with N=1 worked refusal on the
  authors' own baseline (the §6.2 bounded-non-vacuousness limitation). Lane 1 claims
  exactly that; Lane 2 would over-claim.
- It matches the external peer review, which judged the work "a credible
  measurement/experience contribution once §4.1-4.3 are addressed" and "reject as a
  full methods submission" in its current evidentiary state.
- It matches the Manager's prior instrument-first decision (MANAGER-DECISION-PAPER-A-
  NOW, Option C): Paper A is the instrument paper; Paper B is the
  carried-through-stress paper.
- It resolves the framing tension a reviewer flagged: "narrow and complementary"
  (which §2.3 must say to survive the certification-prior-art reviewer) sits badly
  under a method-flavoured title/claim, but sits correctly under an instrument-paper
  claim. The new title ("The Gate That Refused Its Authors") already leans
  instrument/demonstration, not method — so Lane 1 makes the title and the claim
  consistent.
```

## What ratifying Lane 1 changes downstream

```text
- The abstract's review pass should align it to the instrument-paper framing: it
  currently opens "We present a staged, fail-closed protocol," which leans method.
  Lane 1 would keep the protocol description but foreground the gate + the worked
  refusal as the contribution, not a validated method.
- Target venues become measurement/evaluation/experience tracks (and workshops on
  eval validity / benchmarking), not a top-tier novel-methods track.
- The D1–D7 material stays as §4 architecture-with-status; no separate methods
  section is added (unless a target venue specifically wants one, in which case it
  must carry the per-gate evidential-grain labelling, not imply uniform validation).
- Paper B inherits the novel-method ambitions: the external demonstration + stress
  rung are what would, in time, support a stronger methods claim.
```

## What this memo does not decide

```text
- It does not authorize any run. Paper B's external demonstration and stress rung
  remain execution-gated to a separate future Manager authorization.
- It does not finalize the venue (the specific track/venue is a later choice); it
  fixes the CATEGORY (instrument/measurement/experience vs novel-method), which is
  what the draft's structure depends on.
```

## Requested action

```text
A one-line ratification: "Lane 1 confirmed (instrument/measurement/experience)" — or
a direction to re-aim Paper A toward Lane 2, which would require folding Paper B
content forward and is inconsistent with the pre-stress status and the instrument-
first decision. Senior recommends Lane 1.
```

## Closed gates (unchanged)

```text
No new run · No D4 rescue · No CAL-Q rerun · No certification · No compression · No
INT8/INT4 stress · No second compression rung · No full ladder · No Claim C
activation · No public benchmark packaging · No funder-facing release · No SBIR
submission. Model-free.
```

— Senior Engineer
