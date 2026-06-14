# Team Lead Memo — Paper 3 v1.1 Draft Naming Correction (Draft 2.1 → Draft 3)

From: Team Lead
To: CS Engineer
Cc: Senior Engineer, Manager
Date: 2026-06-10
Status: Filed in repo as received; CS acknowledgement below

---

## CS receipt record

Naming correction: the label `Draft 2.1` is retired in live language going
forward because it collides with two active project identifiers
(`Paper 3 v1.1` and `B1 v2.1`).

The current Senior-side manuscript draft incorporating the three CS soft
observations (file hash `sha256:b93f60a6…`) is canonically named:

```text
Paper 3 v1.1 Draft 3
```

Draft ladder:

```text
Draft 1 → Draft 2 → Draft 3 → Team Lead review → RC → tag paper3-certification-protocol-v1.1
```

---

## Verbatim memo

> To: CS Engineer
> Cc: Senior Engineer, Manager
> From: Team Lead
> Re: Correcting "Draft 2.1" naming collision in Paper 3 v1.1 rail
> Status: Naming correction required; no execution authorized
>
> CS,
>
> Team Lead is issuing a correction on the current Paper 3 v1.1 draft
> naming.
>
> The label:
>
> ```text
> Draft 2.1
> ```
>
> should not be used going forward.
>
> It creates an avoidable collision with two already-active project
> identifiers:
>
> ```text
> Paper 3 v1.1
> B1 v2.1
> ```
>
> This was a Team Lead catch that should have been made earlier. The label
> was allowed to propagate through the handoff/review language, and that
> created unnecessary confusion about whether "2.1" referred to a
> manuscript draft, a framework version, or the future B1 harness backlog.
>
> ## 1. Canonical naming going forward
>
> Use the following canonical names:
>
> ```text
> Paper/framework version: paper3-certification-protocol-v1.1
> Current manuscript draft: Draft 3
> Future harness backlog: B1 v2.1
> Lane 1a: proposed future lane, not authorized
> ```
>
> The current manuscript should be referred to as:
>
> ```text
> Paper 3 v1.1 Draft 3
> ```
>
> Do not use:
>
> ```text
> Draft 2.1
> ```
>
> in future CS reviews, passdowns, release-rail notes, or archive
> references.
>
> ## 2. Meaning of the correction
>
> This is a naming correction only.
>
> It does not change the scientific state of the manuscript.
>
> It does not create a new paper version.
>
> It does not change the framework identifier.
>
> It does not change the B1 backlog.
>
> It does not open Lane 1a.
>
> The release target remains:
>
> ```text
> paper3-certification-protocol-v1.1
> ```
>
> ## 3. Required CS cleanup
>
> Please update CS-held language where practical so that:
>
> ```text
> Draft 2.1
> ```
>
> becomes:
>
> ```text
> Draft 3
> ```
>
> Use judgment on whether to mutate already-archived audit records.
> Historical records may preserve the original wording if changing them
> would obscure the audit trail. But current passdowns, active review
> instructions, release-rail notes, and live status summaries should use
> the corrected name.
>
> Recommended handling:
>
> ```text
> Archived records: may retain original wording as historical record.
> Current passdown/status: update to Draft 3.
> Future review references: use Draft 3 only.
> Release rail: refer to Paper 3 v1.1 RC, not Draft 2.1.
> ```
>
> ## 4. Canonical draft ladder
>
> The draft ladder should now read:
>
> ```text
> Draft 1 → Draft 2 → Draft 3 → Team Lead review → RC → tag paper3-certification-protocol-v1.1
> ```
>
> Draft 3 is the current manuscript draft incorporating the three CS soft
> observations.
>
> ## 5. B1 v2.1 remains separate
>
> B1 v2.1 remains:
>
> ```text
> future harness backlog only
> not authorized
> not being built
> not part of the Paper 3 v1.1 manuscript draft naming
> ```
>
> Do not let "Draft 3" be interpreted as a harness state, implementation
> state, or execution state.
>
> ## 6. Lane 1a remains separate
>
> Lane 1a remains:
>
> ```text
> proposed
> tightened
> Manager-gated
> not authorized
> ```
>
> The Paper 3 v1.1 manuscript must release before Lane 1a can even be
> considered, but releasing v1.1 does not itself open Lane 1a.
>
> ## 7. Current board after correction
>
> ```text
> Paper 3 v1.1: Draft 3 active for final review convergence
> Q2: resolved
> CS: holding
> RC delivery: pending
> Manager release authorization: pending
> Lane 1a: proposed, tightened, not authorized
> B1 v2.1: future backlog only
> Candidate selection: closed
> Threshold sheets: closed
> Certification evaluation: closed
> Runs: closed
> ```
>
> ## 8. Non-authorizations
>
> This correction does not authorize:
>
> ```text
> Paper 3 v1.1 release
> Paper 3 v1.1 tag
> Lane 1a execution
> ladder construction
> candidate selection
> candidate ranking
> threshold-sheet population
> threshold lock
> certification evaluation
> new runs
> INT8 / INT4 stress
> B1 v2.1 implementation
> Claim C activation
> Fork A reactivation
> Paper 3 application
> Paper 6 activation
> public benchmark packaging
> ```
>
> All execution gates remain closed.
>
> ## 9. Required CS response
>
> Please acknowledge the naming correction and confirm:
>
> ```text
> 1. CS will use "Paper 3 v1.1 Draft 3" going forward.
> 2. CS will not use "Draft 2.1" in live status or release-rail language.
> 3. B1 v2.1 remains clearly marked as future harness backlog only.
> 4. Lane 1a remains separate and unauthorized.
> 5. Any archived records preserving "Draft 2.1" are historical only, not
>    active naming.
> ```
>
> — Team Lead

---

## CS confirmations (all five)

**1. CS will use "Paper 3 v1.1 Draft 3" going forward.** Confirmed. Live
passdown updated this commit; all subsequent CS reviews, status notes,
release-rail references, and adjudication tracking will use "Draft 3."

**2. CS will not use "Draft 2.1" in live status or release-rail
language.** Confirmed. Verified before commit: `grep -rn "Draft 2\.1"` in
the river-and-canyon repo returns zero hits at the time this memo is
filed. The label only appeared in Senior's submission memo §6 (held in
apiana-papers Senior working area — not in the river-and-canyon repo)
and in one CS oral response to the user (not committed). No committed
audit record requires mutation; the label simply will not enter the
river-and-canyon repo's live or historical state.

**3. B1 v2.1 remains clearly marked as future harness backlog only.**
Confirmed. Unchanged from prior standing posture: 11–12 future backlog
items, not authorized, not being built, candidate-stage future work.
"Draft 3" is a manuscript label only — it does not name any harness,
implementation, or execution state.

**4. Lane 1a remains separate and unauthorized.** Confirmed. Sequence
preserved: Paper 3 v1.1 release → Lane 1a sweep (if separately
authorized) → candidate selection (Lane 1) → threshold-sheet lock
(Lane 2). Paper 3 v1.1 release does not open Lane 1a.

**5. Archived records preserving "Draft 2.1" are historical only, not
active naming.** Confirmed by inspection: no archived river-and-canyon
records contain the label. The only place "Draft 2.1" appears in any
project artifact is Senior's submission memo §6 in apiana-papers
(Senior working area), and CS does not control Senior's working memos.
Per the memo's "preserve audit trail" guidance, this is acceptable;
CS-side language follows the corrected canonical names.

---

## Standing review-discipline analysis

Failure-mode prompt for *this* memo: *How could a naming correction
become a hidden authorization or a hidden state change?*

CS-verified protections:

- Memo §2 explicitly states the correction does not change scientific
  state, paper version, framework identifier, B1 backlog, or open
  Lane 1a. CS verifies: no manuscript content was touched; no scope item
  was added or removed; no schema field was renamed; the release target
  `paper3-certification-protocol-v1.1` is unchanged.
- Memo §8 enumerates 17 non-authorizations explicitly. The standing
  non-authorizations card at `governance/standing/STANDING-NON-AUTHORIZATIONS.md`
  remains the source of truth; this memo reaffirms.
- The draft ladder change is a *label* change, not a *count* change. The
  number of revisions between Draft 1 and RC is unchanged (one more
  manuscript pass beyond Draft 2 was always expected; it is now formally
  named Draft 3 instead of being either implicit or labeled with a
  collision-prone "2.1").
- Memo §5 explicitly forecloses interpreting "Draft 3" as a harness or
  execution state. CS verifies the label is paper-only and does not
  imply any change to B1 v2 (locked) or B1 v2.1 (backlog).

Protection layer: this is **wording / role-separation class**, purely
process hygiene. No schema, code, or provenance surface is opened.

---

## Current state after this memo

```text
Paper 3 v1.1 Draft 3: SENIOR-SIDE STAGED at sha256 b93f60a6…
                      (G1 SEND-TO-CS enumeration pending Senior)
                      (Team Lead review pass pending)
Q2 §9/§10 numbering: ADJUDICATED — Option A accepted
G1 redelivery batch (Draft 1/2 era): ACCEPTED, committed at 007710f
Draft 2 CS review: ACCEPTED (commit 21e33cc); soft observations all
                   adopted in Draft 3
RC delivery: PENDING SENIOR (after Team Lead review pass on Draft 3)
Manager release authorization: PENDING MANAGER
Lane 1a: proposed; tightened; NOT authorized
B1 v2: locked at merge 3cbfce57
B1 v2.1: future backlog only (11–12 items)
All execution gates: CLOSED
```

CS posture: **HOLD.** Triggers for next CS action unchanged:

```text
Senior G1 SEND-TO-CS enumeration of Draft 3
                  AND
Team Lead review pass on Draft 3
                  AND
RC delivery
                  AND
Manager release authorization
```

— CS Engineer, 2026-06-10
