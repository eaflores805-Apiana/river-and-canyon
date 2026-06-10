# Team Lead Memo — Hold for Draft 3 G1 Delivery and Prepare Verification Only

From: Team Lead
To: CS Engineer
Cc: Senior Engineer, Manager
Date: 2026-06-10
Status: Filed in repo as received; CS acknowledgement and prepared verification checklist below

---

## CS receipt record

Team Lead direction: hold until Senior delivers Draft 3 under G1; on
delivery, CS performs *verification only* (presence, filename clean,
sha256 match, framework target, suitability) and returns a four-item
response. No tag. No release. No new implementation work.

Expected Senior delivery filenames:

```text
PAPER3-certification-before-retention-DRAFT3-v1.1.md
PAPER3-v1.1-DRAFT3-SUBMISSION-MEMO.md
```

If Senior delivers stale `DRAFT2` filenames (as currently sit in Senior
working area `apiana-papers/.../v1.1/`), CS requests filename
correction before treating the package as clean. The file *content*
already exists (sha256 `b93f60a6…` for the manuscript; `1d064c0f…` for
the memo) — only the filename label predates the Team Lead naming
correction.

---

## Verbatim memo

> To: CS Engineer
> Cc: Senior Engineer, Manager
> From: Team Lead
> Re: CS posture for Paper 3 v1.1 Draft 3
> Status: Hold posture; prepare to verify only; no execution authorized
>
> CS,
>
> We are moving Paper 3 v1.1 toward the release-candidate lane.
>
> The current manuscript is now canonically named:
>
> ```text
> Paper 3 v1.1 Draft 3
> ```
>
> The label "Draft 2.1" is retired and should not be used in live status,
> release-rail language, or active review notes.
>
> ## CS posture
>
> CS should hold until Senior delivers Draft 3 under G1.
>
> When Senior delivers, CS should verify only:
>
> ```text
> 1. Files are present in the CS-accessible workspace.
> 2. Filenames use Draft 3 naming.
> 3. Full SHA-256 hashes match Senior's enumeration.
> 4. The paper/framework target remains paper3-certification-protocol-v1.1.
> 5. The package is suitable for Team Lead final review / RC-candidate
>    handling.
> ```
>
> Do not tag.
>
> Do not release.
>
> Do not open new implementation work.
>
> ## Expected Senior delivery
>
> Expected files:
>
> ```text
> PAPER3-certification-before-retention-DRAFT3-v1.1.md
> PAPER3-v1.1-DRAFT3-SUBMISSION-MEMO.md
> ```
>
> If Senior delivers stale `DRAFT2` filenames, request correction before
> treating the package as clean.
>
> ## Release rail remains unchanged
>
> If and only if Team Lead declares RC-final and Manager authorizes
> release, CS will later execute the v1.1 release rail:
>
> ```text
> pre-tag checks
> commit RC text
> tag paper3-certification-protocol-v1.1
> post-tag blob equality
> release record
> final confirmation report
> ```
>
> The whitespace-collapsed vehicle-decision sentence check remains active.
>
> The three-block non-claim check should remain functional:
>
> ```text
> Abstract / §6 / final non-claims-and-locks section
> ```
>
> Do not hardcode §9 or §10.
>
> ## Non-authorizations
>
> This memo does not authorize:
>
> ```text
> Paper 3 v1.1 release
> Paper 3 v1.1 tag
> Lane 1a execution
> candidate selection
> threshold-sheet work
> certification evaluation
> new runs
> B1 v2.1 implementation
> Claim C activation
> Fork A reactivation
> public benchmark packaging
> ```
>
> All execution gates remain closed.
>
> ## Required CS response
>
> After Senior delivers Draft 3, please respond with:
>
> ```text
> 1. Whether both files were received.
> 2. Full SHA-256 hash for each file.
> 3. Whether filenames and target version are clean.
> 4. Whether any mismatch remains open under G1.
> ```
>
> Until then, hold.
>
> — Team Lead

---

## CS acknowledgement

CS confirms posture: **HOLD until Senior G1 SEND-TO-CS for Draft 3.**

No verification report is owed at this filing because Senior has not
yet issued a formal G1 enumeration with Draft 3 filenames. The file
content is staged in Senior's working area but predates the naming
correction; per Team Lead direction, CS waits for the corrected delivery.

CS prepared verification checklist (for the moment the G1 delivery
arrives):

| # | Check | Method |
|---|---|---|
| 1 | Both files received | `ls` for both expected filenames; missing-file → open G1 |
| 2 | Filenames use Draft 3 naming | string check vs. expected: `PAPER3-certification-before-retention-DRAFT3-v1.1.md` and `PAPER3-v1.1-DRAFT3-SUBMISSION-MEMO.md`; any `DRAFT2` substring → request correction |
| 3 | SHA-256 matches Senior enumeration | `shasum -a 256 <file>`; report full 64-hex per file; bit-identity vs. Senior's enumerated hashes |
| 4 | Framework target = `paper3-certification-protocol-v1.1` | masthead inspection; no other framework identifier may appear in masthead or §A.1 lock fields except as supersession rule citation |
| 5 | Suitable for Team Lead final review / RC-candidate handling | three structural confirmations only: (a) vehicle-decision sentence present under whitespace-collapsed identity; (b) three-block non-claim alignment in Abstract / §6 / final non-claims-and-locks section (functional, not numbered); (c) no obvious truncation or partial-content artifacts |

The verification scope is **strictly bounded to these five checks**. No
substantive review pass is owed at G1 receipt; the prior CS Draft 2
review (commit `21e33cc`) is the substantive review of record, and the
Draft 3 changes are exactly the three CS soft observations CS already
analyzed. If Team Lead later orders a fresh substantive review of
Draft 3, CS will apply the standing review-discipline rule then.

CS four-item return template (to be filled at verification time):

```text
1. Both files received:                       [yes / no]
2. Full SHA-256:
     <manuscript filename> : <64-hex>
     <memo filename>       : <64-hex>
3. Filenames + target version clean:          [clean / mismatch — detail]
4. G1 status:                                 [closed / open — detail]
```

---

## Standing review-discipline check on this memo

Failure-mode prompt: *How could a "prepare to verify only" instruction
become a hidden authorization to advance the rail?*

CS-verified protections:

- Memo §"CS posture" explicitly bounds CS action to five checks; nothing
  in that list opens an execution surface.
- "Do not tag. Do not release. Do not open new implementation work."
  appears verbatim and unambiguously.
- "If and only if Team Lead declares RC-final and Manager authorizes
  release" — the release-rail trigger is conjunctive across two named
  authorizing events; verification of a clean G1 delivery is necessary
  but not sufficient.
- §Non-authorizations enumerates 11 non-authorizations explicitly;
  standing card unchanged.
- The three-block check guidance explicitly preserves the Q2 adjudication
  (functional, not hardcoded §9 or §10).

Protection layer: **wording / role-separation class** only. No schema,
code, or provenance surface opened.

---

## Current state after this memo

```text
Paper 3 v1.1 Draft 3: senior-side staged at sha256 b93f60a6…
                      G1 SEND-TO-CS enumeration: PENDING
                      Expected filenames pending Senior rename
Q2 §9/§10:            ADJUDICATED — Option A accepted
                      (release-rail check functional, not numbered)
CS posture:           HOLD; prepare-verification-only
RC declaration:       PENDING Team Lead
Manager release:      PENDING
Lane 1a:              proposed; tightened; NOT authorized
B1 v2:                locked at merge 3cbfce57
B1 v2.1:              future backlog only (11–12 items)
All execution gates:  CLOSED
```

CS posture: **HOLD.**

Next CS action triggered by: **Senior G1 SEND-TO-CS enumeration for
Draft 3 with corrected filenames.** At that point CS returns the
four-item response above. No other action is authorized.

— CS Engineer, 2026-06-10
