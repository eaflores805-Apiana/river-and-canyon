# Manager / Team Lead Direction — Lane 1a v0.3 Acceptance and Token-Prior Authorization Path

From: Elias / Manager
To: CS Engineer
Cc: Senior Engineer, Team Lead
Date: 2026-06-10
Status: Filed; CS executes Step-3 production under this authorization

---

## Verbatim memo

> CS,
>
> Manager and Team Lead acknowledge the CS return filed at commit
> `e6cf3c1`. The Lane 1a design packet v0.3 is accepted as the current
> design packet of record.
>
> Reported design packet hash:
> `f1280a8563bbb48c5592c35c809be6c739859234cbf33b64a3786c6e5df67bab`
>
> ## 1. v0.3 supersession accepted
> v0.3 supersedes v0.1 for Step-3 production. B1–B5 corrections
> accepted and implemented directly in Step-3.
>
> ## 2. Token-prior path decision
> **Option A — token-prior control path authorized by name for Lane 1a.**
> candidate generations: 768; token-prior control generations: 768;
> total planned generations: 1,536. Authorization is narrow — Lane 1a
> only; not a general token-prior study; not candidate selection; not
> certification evaluation; not stress-retention; not B1 v2.1.
>
> ## 3. LOCK-RECORD requirement
> Must explicitly state:
> `Token-prior control authorization: Manager-authorized Lane 1a
> token-prior control path`
> plus `planned_generation_count = 1536`, `candidate_generation_count
> = 768`, `control_generation_count = 768`,
> `control_scoring_denominator = 80 answerable-mirroring controls per
> rung`, `NULL-mirroring controls = descriptive-only`.
>
> ## 4. Case B wrapper remains accepted
> CS may use `lane1a_runner_wrapper.py`; B1 v2 unedited; B1 v2.1
> unauthorized.
>
> ## 5. §13 recipe status
> Accepted with B3 amendment applied at Step-3 production time.
>
> ## 6. Step-3 production authorization
> CS authorized to produce + commit all execution-packet artifacts.
> Does NOT authorize: running sweep, model calls, generation, first
> data access.
>
> ## 7. Required Step-3 return
> Nine items: artifact list; sha256 per artifact; test summary;
> confirmation no first data access; confirmation no model invocation;
> confirmation B1 v2 not edited; confirmation B1 v2.1 not created/used;
> confirmation token-prior auth in LOCK-RECORD; any remaining concern.
>
> ## 8. First data access remains closed
> Requires: CS Step-3 complete + Senior/CS convergence + LOCK-RECORD
> with all hashes + Team Lead combined adversarial review + explicit
> Manager execution authorization (this memo does NOT satisfy item 5).
>
> ## 9. Non-authorizations (16 enumerated; all execution gates closed)
>
> ## 10. Disposition
> Design packet v0.3 accepted · B1–B5 accepted · Option A selected ·
> Case B wrapper accepted · Single-cycle Step-3 production authorized
> · First data access NOT authorized.
>
> — Elias / Manager

---

## CS acknowledgement and execution declaration

CS confirms:

1. **Single-cycle Step-3 production authorized.** CS proceeds.
2. **Option A token-prior path applied.** All 1,536 generations
   (768 candidate + 768 control) recorded as planned;
   control_scoring_denominator = 80 answerable-mirroring controls per
   rung; NULL-mirroring controls descriptive-only.
3. **LOCK-RECORD will carry the exact authorization line** verbatim
   from §3.
4. **Case B wrapper produced.** B1 v2 invoked only through its locked
   surface (`--mode live --context paper2-reproduction --framework-version
   none`); wrapper applies Lane 1a tagging at wrapper + schema layer.
5. **B1 v2 source unmodified.** B1 v2.1 not created and not used.
6. **All B1–B5 v0.3 corrections implemented in code.** Gap sign,
   inconclusive preempt, 80-denominator control scoring, B4 LOCK-RECORD
   line, B5 total_attempts = 1,536 and survivor-order unit test.
7. **First data access does NOT occur in this commit cycle.** No model
   invocation; no live sweep; no generation. LOCK-RECORD sign-off
   triggers Team Lead combined review next, not execution.

— CS Engineer, 2026-06-10
