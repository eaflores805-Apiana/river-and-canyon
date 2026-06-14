# MANAGER-DECISION-VENUE-OPTION-2-v0.1

**Version:** v0.1. River and Canyon program. Decision record. Ratifies the venue-category decision surfaced in VENUE-DECISION-MEMO-PAPER-A-v0.1 (4f399b8e).
**Status:** DECISION (Manager). Model-free. Fixes the contribution category for Paper A before submission polish. Anchored on origin/main HEAD bbec2e5. Authorizes nothing.
Routing: Manager (decision) → Team Lead (route into strategic record + paper surface) → Senior (apply framing to abstract/submission) → CS (n/a).

---

## The decision

```text
RATIFIED: Paper A is an INSTRUMENT / MEASUREMENT / EXPERIENCE paper (Option 2).
  NOT a full methods paper (Option 1).
```

## What the two options would have claimed

```text
Option 1 — full methods paper:
  "Here is a new general method, validated broadly."
  REJECTED: the evidence does not support it. The program has one task family, one
  model (Qwen2.5-3B, FP16), no compression rung, and no external demonstration. A
  general-method claim would overclaim on every one of those axes.

Option 2 — instrument / measurement / experience paper (RATIFIED):
  "We built and exercised a fail-closed validity instrument, and it caught an
   invalid baseline before a retention claim could be made — shown through a worked
   case, with honest limits and a roadmap to broader validation."
  This is what the draft (PAPER-A-DRAFT-v0.4) is already built as.
```

## Why Option 2 (Manager rationale)

```text
- It matches the evidence exactly: one family, one model, pre-stress, N=1 worked
  refusal on the authors' own baseline (§6.2's bounded-non-vacuousness limit).
- It does NOT weaken the paper. It protects it from overclaiming. The strength of
  this work is its honesty; a general-method frame would put the paper at war with
  its own scope section and hand a reviewer the easiest possible rejection.
- It is consistent with the external peer review ("a credible measurement/experience
  contribution"; "reject as a full methods submission" at current evidence) and with
  the prior instrument-first decision (MANAGER-DECISION-PAPER-A-NOW, Option C).
- The right framing is the demonstration, not the method:
    WRONG: "We have a complete new method for stress-retention evaluation."
    RIGHT: "We built and exercised a fail-closed validity instrument, and it caught
            an invalid baseline before a retention claim could be made."
```

## Binding framing rules this sets (for the abstract review pass and submission)

```text
1. The contribution is the INSTRUMENT + the WORKED REFUSAL, not a validated method.
   The abstract should foreground the gate and the refusal, not "we present a method."
2. Keep "staged, fail-closed protocol" as description, but do not let it read as a
   general-method claim. The title ("The Gate That Refused Its Authors") already
   leans instrument/demonstration — keep the abstract consistent with the title.
3. All scope limits stay in the body, unsoftened: one family, one model, pre-stress,
   own-baseline-only non-vacuousness.
4. Target venues: measurement / evaluation / experience tracks and eval-validity /
   benchmarking workshops — NOT a top-tier novel-methods track.
5. The D1-D7 material stays as §4 architecture-with-status; no separate methods
   section implying uniform validation is added.
6. The negative-result form is retained: if the external demonstration and the stress
   rung are not completed, the work remains a protocol with a worked example, scoped
   accordingly, and is not promoted past that.
```

## What this decision does NOT do

```text
- It does not authorize any run. Paper B's external demonstration and stress rung
  remain execution-gated to a separate future Manager authorization.
- It does not pick the specific venue; it fixes the CATEGORY. The specific
  track/venue is a later choice consistent with rule 4.
- It does not require re-drafting v0.4's body. v0.4 is already built as Option 2; the
  decision mainly governs the abstract's framing and the eventual cover/submission
  language.
```

## Consequence for current work

```text
- The abstract review pass (the immediate next model-free step) now has a fixed
  target: align the abstract to the instrument/demonstration framing (rule 1-2).
- Paper A's status is unchanged otherwise: complete draft (v0.4), pending abstract
  review, standing citation re-verification, and supplement assembly. All model-free.
- Paper B remains planned, not started; its runs need separate authorization.
```

## Closed gates (unchanged)

```text
No new run · No D4 rescue · No CAL-Q rerun · No certification · No compression · No
INT8/INT4 stress · No second compression rung · No full ladder · No Claim C
activation · No public benchmark packaging · No funder-facing release · No SBIR
submission. Model-free.
```

— Manager decision, recorded by Senior Engineer
