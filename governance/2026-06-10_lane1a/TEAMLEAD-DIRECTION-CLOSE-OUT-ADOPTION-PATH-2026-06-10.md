# Team Lead Direction — Lane 1a Close-Out Adoption Path

From: Team Lead
To: CS Engineer, Senior Engineer, New Senior
Cc: Manager, Contributors
Date: 2026-06-10
Status: Filed; CS acknowledgement + action plan below

---

## Verbatim memo (key directions)

> 1. **Use v1.2 before adoption.** Senior prepares a v1.2 close-out
>    candidate incorporating the already-answered `separability_flag`
>    item. Record as: defaulted via coarse heuristic; effect on K=0
>    verdict none; effect on record non-trivial (column reads True but
>    represents heuristic proxy).
>
> 2. **File the missing review-chain provenance.** CS should request or
>    receive the outsider review and Contributor 5 precision-pass
>    materials. If full memos are available, file them in the Lane 1a
>    governance folder. If not, add a provenance note recording: which
>    review inputs produced the v1.1/v1.2 changes; where they reside;
>    who reviewed them; which close-out sections they affected.
>
> 3. **Preserve the scorer correction.** Dual-scoring distinction stays
>    intact. No retroactive rescoring.
>
> 4. **Accept R6 as a standing-rule candidate.** After adoption,
>    CS may add R6 to STANDING-REVIEW-DISCIPLINE.md (only after
>    adoption block signed and official close-out commit returned).
>
> 5. **Elevate the doctrine pair.** Stays in close-out, considered for
>    program principles list later. Do not describe Lane 1a as a
>    Paper 3 certifier false-reject rate — no certification gate was
>    exercised.
>
> 6. **Adoption path (in order):**
>    1. Senior prepares v1.2
>    2. CS confirms v1.2 resolves the open item
>    3. Team Lead reviews v1.2
>    4. Manager signs adoption block
>    5. CS commits official `CLOSE-OUT.md` and returns filename + sha256 + commit SHA
>    6. CS adds R6 to `STANDING-REVIEW-DISCIPLINE.md` in follow-on commit
>    7. Status: CLOSED-PENDING-ADOPTION → CLOSED-OF-RECORD
>
> 7. Non-authorizations (12 enumerated).
>
> 8. Prepare v1.2; close separability_flag record item; file or
>    provenance-pin missing review-chain inputs; return final adoption
>    candidate.
>
> — Team Lead

---

## CS acknowledgement and action plan

### Direction-by-direction:

**§1 v1.2 close-out candidate** — **Senior owns the draft** per §6 step 1.
CS does not prepare v1.2; CS verifies it resolves the
`separability_flag` open item when Senior delivers, per §6 step 2.

**§2 missing review-chain provenance** — **partially actionable now:**
CS has filed `INPUTS-PACKAGE-INSTRUMENT-VALIDATION-ADDENDUM-2026-06-10.md`
in this commit. That memo (a Senior-to-New-Senior handoff for a
separate Pre-Lock Instrument Validation Addendum drafting task)
**names** the review-chain materials Team Lead is asking about. The
full memos themselves are not in CS's hands. See §"Provenance trail
for v1.0 → v1.1 close-out changes" below for what CS has documented
and what is outstanding.

**§3 scorer correction preserved** — CONFIRMED. The L03 strict/content
gap (gap 0.162) remains the one genuine behavioral finding; no
retroactive rescoring. CS supports the rejection of its own original
"relaxed scorer" candidate revision.

**§4 R6 accepted as standing-rule candidate** — CS waits for adoption
block signature + official close-out commit before adding R6 to
`STANDING-REVIEW-DISCIPLINE.md`. R6 text from close-out v1.1 §10 is
ready to fold in verbatim.

**§5 doctrine pair elevation** — CONFIRMED. CS will not describe
Lane 1a as a Paper 3 certifier false-reject rate. The §8 M3
citation-scope guard is binding for any future M3/E1 discussion.

**§6 adoption path** — CS posture set:

```text
Step 1. Senior prepares v1.2                  PENDING SENIOR
Step 2. CS confirms v1.2 resolves open item   PENDING (after step 1)
Step 3. Team Lead reviews v1.2                PENDING (after step 2)
Step 4. Manager signs adoption block          PENDING (after step 3)
Step 5. CS commits official CLOSE-OUT.md
        and returns filename + sha256 + commit SHA   PENDING (after step 4)
Step 6. CS adds R6 to STANDING-REVIEW-DISCIPLINE
        in follow-on commit                          PENDING (after step 5)
Step 7. CLOSED-PENDING-ADOPTION → CLOSED-OF-RECORD   PENDING (after step 6)
```

**§7 non-authorizations** — all 12 in force.

---

## Provenance trail for v1.0 → v1.1 close-out changes

Per Team Lead §2, CS records the review-chain provenance that
produced the v1.0 → v1.1 changes:

### Materials CS has located in apiana-papers/Lane1a/ (now filed)

| Source | Repo location | sha256 |
|---|---|---|
| `INPUTS-PACKAGE-INSTRUMENT-VALIDATION-ADDENDUM.md` | `governance/2026-06-10_lane1a/INPUTS-PACKAGE-INSTRUMENT-VALIDATION-ADDENDUM-2026-06-10.md` | `3896fab1c8cd9c1f328e47e724c20e531ebc0a1a9064fdcb53ad064b905d5762` |

This memo is an Outgoing-Senior-to-New-Senior handoff for a separate
task (drafting a Pre-Lock Instrument Validation Addendum). It is
**not the C5-intake / Manager structure / Contributor memos** per se,
but its §3 explicitly enumerates those source materials by name.

### Materials referenced by close-out v1.1 changelog and INPUTS-PACKAGE §3 but NOT in CS hands

CS does not have standalone copies of:

| Referenced material | First mention in repo | Where the reference says it resides |
|---|---|---|
| **Team Lead C5-intake memo** | `CLOSE-OUT-DRAFT-v1.1-FREEZE-CANDIDATE-2026-06-10.md` changelog: *"Contributor 5 precision pass"*; `INPUTS-PACKAGE` §3 item 2 | INPUTS-PACKAGE describes content: "the three-component suite formulation (positive controls / ideal witness / degeneracy caps); malformed-criterion definition; P1–P4 record pins." Source location not stated. |
| **Manager structure memo** | `INPUTS-PACKAGE` §3 item 3 | "the seven-item spec your A/B/C reorganizes; the sensitivity-vs-specificity framing; the naming decision." Source location not stated. |
| **Contributor memo (Lane 1a accounting)** | `INPUTS-PACKAGE` §3 item 4; close-out v1.1 changelog: *"outsider review"* | "the inheritance finding … 'the cure already existed in v1.0's D2 battery-sensitivity text'"; verbatim keeper "a floor against a 1.000 envelope is no floor." Source location not stated. |

### Effect of each referenced material on close-out v1.0 → v1.1 sections

Inferred from the close-out v1.1 changelog plus internal cross-references:

| Section affected | Change | Source review input |
|---|---|---|
| §1 framework sequence (P1, pinned) | New paragraph: Paper 3 v1.1 released before Lane 1a authorization | Contributor 5 / outsider precision pass |
| §2 "five independent vantage points" sentence | Added attestation that Senior + CS + contributor + Team Lead + outsider converge | Contributor 5 / outsider precision pass |
| §4C malformed-criterion class named | "the program's newly named failure class: a criterion whose pass region excludes ideal behavior" | Team Lead C5-intake (per INPUTS-PACKAGE §3 item 2) |
| §5.3 residual rung map pinned (P2) | Tightened L01/L04/L05 / L03 / L02/L06/L07/L08 wording | Contributor 5 precision pass |
| §6 capability-language guard (P3) | "archival language stays at witness level — 'the criterion excluded ideal behavior' — never candidate-positive" | Contributor 5 precision pass |
| §7 certifier/classifier scope correction | "Lane 1a demonstrated a false-reject mechanism in a reconnaissance classifier whose structures are gate-analogous — it did not demonstrate a Paper 3 certifier false-reject" | Contributor 5 precision pass |
| §8 M3 citation-scope guard (P4) | "Lane 1a may be cited in future M3/E1 discussion only as a documented instrument-discrimination case study" | Contributor 5 precision pass |
| §9 doctrine pair on program ledger | "a valid ruler must not be too permissive; a valid ruler must also not be self-eliminating" | Outsider review (per close-out v1.1 changelog reference) |
| §9 requirement-inheritance lesson | "the cure for Finding A existed verbatim in v1.0's D2 battery-sensitivity text" | Contributor memo (Lane 1a accounting) — per INPUTS-PACKAGE §3 item 4 |
| §10 R1 unified Pre-lock Instrument Validation Suite | Three components: positive controls + ideal witness + degeneracy caps | Team Lead C5-intake |
| §10 R6 NEW — Requirement-inheritance check | Cross-lane requirement portability rule | Contributor memo (Lane 1a accounting) + Outsider review consensus |
| §11 audit items "open: separability_flag" | left open for CS to answer | Senior |

### Open question to Manager

**Do the C5-intake / Manager structure / Contributor memos exist as
standalone artifacts that CS should file?**

If yes, please indicate the source location and CS will copy them
into `governance/2026-06-10_lane1a/` under appropriate names with
three-way hash verification.

If no — i.e., they were conveyed informally through review meetings
or working-area drafts that don't have stable hashes — the table
above stands as the provenance note Team Lead §2 asked for, and CS
considers the §2 item closed via this filing.

**This provenance question does NOT block Senior's v1.2 drafting**
(which is independent and proceeds whenever Senior is ready). It
blocks only the audit-trail completeness for the v1.0 → v1.1
transition.

---

## CS posture

```text
Lane 1a:                              CLOSED-PENDING-ADOPTION
Senior v1.2 close-out candidate:      AWAITED
separability_flag answer:             ready to fold in (defaulted via
                                       coarse heuristic; no effect on
                                       K=0 verdict; non-trivial effect on
                                       record)
R6 standing-rule addition:            text ready; CS waits for adoption
                                       signature before commit
Provenance trail for v1.0 → v1.1:    documented in §"Provenance trail"
                                       above; manager response on
                                       standalone-memo availability
                                       awaited
v1.1 freeze candidate:                in repo as
                                       CLOSE-OUT-DRAFT-v1.1-FREEZE-CANDIDATE
                                       (will be superseded by v1.2)
Official CLOSE-OUT.md:                NOT yet at intended path
                                       (per Senior's own §12 text:
                                       waits for adoption block signature)
All non-Lane-1a execution gates:      CLOSED
```

**CS posture: HOLD for (a) Manager response on standalone-memo
availability, (b) Senior v1.2 draft, (c) Team Lead review of v1.2,
(d) Manager adoption signature.**

— CS Engineer, 2026-06-10
