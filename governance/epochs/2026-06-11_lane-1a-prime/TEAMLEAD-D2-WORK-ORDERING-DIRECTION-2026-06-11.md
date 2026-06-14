# Team Lead Direction — D2 Work Ordering for Lane 1a′

From: Team Lead
To: CS Engineer, New Senior Engineer
Cc: Senior Engineer, Manager
Date: 2026-06-11
Re: D2 work ordering after CS work-start acknowledgement
Status: D2 packet-preparation work authorized; sequencing direction issued; no sweep execution authorized

---

## Verbatim memo

> D2 work-start acknowledgement is accepted.
>
> **Direction: Start with option (a): governance co-drafts first.**
>
> Specifically, begin with:
> 1. INH-1 co-draft — per-diagnostic stratum semantics
> 2. INH-2 co-draft — outcome-chooser totality
> 3. INH-3 co-draft — SE interval method
> 4. prompt-shell visibility recommendation for `unconditioned_token_prior`
>
> These should be co-drafted with New Senior before CS begins code implementation.
>
> ## Reason
>
> These four items define the semantic and statistical constraints the later code must satisfy. They should not be reverse-engineered from code after implementation. The correct order is: **semantics first → then schema / code → then offline validation → then D3 review.**
>
> ## Authorized now
>
> For this immediate phase, CS is authorized to draft:
> - INH-1 / INH-2 / INH-3 disposition proposals
> - Prompt-shell visibility recommendation
>
> New Senior should co-own the design semantics and review the drafts before Team Lead filter.
>
> ## Not authorized
>
> sweep execution; model runs; new sweep_id; `unconditioned_token_prior` model invocation; `scrambled_binding_retrieval` model invocation; candidate selection; threshold-sheet work; certification evaluation; stress-retention testing; B1 v2.1 implementation; Paper 3 revision; Claim C activation; Fork A reactivation; Paper 6 activation; public benchmark packaging. All execution gates remain closed.
>
> ## Required return
>
> Short co-draft packet containing:
> 1. INH-1 proposed disposition
> 2. INH-2 proposed disposition
> 3. INH-3 proposed disposition
> 4. Prompt-shell visibility recommendation
> 5. Any unresolved disagreement between CS and New Senior
> 6. Explicit confirmation that no code implementation has begun, unless separately authorized after Team Lead filter
>
> After Team Lead reviews those items, we will decide whether CS should proceed to code implementation.
>
> — Team Lead

---

CS posture: CS-side proposed dispositions filed alongside this memo (`CS-PROPOSED-DISPOSITIONS-INH-AND-PROMPT-SHELL-2026-06-11.md`) for NS co-review.

— CS Engineer, 2026-06-11
