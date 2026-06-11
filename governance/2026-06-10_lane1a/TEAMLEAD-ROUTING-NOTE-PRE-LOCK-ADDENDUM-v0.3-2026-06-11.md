# Team Lead Routing Note — Pre-Lock Instrument Validation Addendum v0.3

From: Team Lead
To: Senior Engineer
Cc: New Senior Engineer, CS Engineer, Manager
Date: 2026-06-11
Status: Filed; Team Lead filter PASS; Senior conceptual review in flight; CS HOLDS for Senior PASS

---

## Verbatim memo

> ## 1. Review context
> This addendum converts the Lane 1a instrument-discrimination
> findings into proposed standing governance requirements.
> The draft is not an execution packet, not a Lane 1a′ design, not a
> Paper 3 revision, not an authorization request for model/data
> activity. Governance/template work only.
>
> ## 2. Confirmed v0.3 changes (5 items per addendum front matter)
> [classifier/certifier scope guard; softened positive retrieval
> wording; standing-rule path confirmation as adoption condition;
> R6 surfaced in front matter; diagnostic-only / non-eliminating
> rule consequence clarified]
>
> ## 3. Requested Senior review focus (7 items)
> [classifier/certifier scope guard sufficiency; Lane 1a not as
> Paper 3 certifier result; dead/tautological/malformed scoping;
> battery operating-characteristic strength; R6 fidelity to the
> Lane 1a inheritance failure; enforcement triple adequacy; no
> language risking positive model/candidate claims]
>
> ## 4. Boundaries (verbatim)
> No execution authorized: Lane 1a′; new sweep_id; model runs; new
> data generation; candidate selection; ranking; threshold-sheet
> work; certification evaluation; stress-retention testing;
> B1 v2.1; Paper 3 revision; Claim C; Fork A; Paper 6; public
> benchmark packaging.
>
> ## 5. Expected Senior review outcome (one of):
> PASS — route to CS review;
> PASS with targeted edits — specify exact edits;
> HOLD — specify blocking conceptual issue.
>
> If Senior PASSes, **the next route is CS review for
> implementability, artifact path, template usability, and
> standing-rule path convention.**
>
> — Team Lead

---

## CS acknowledgement and corrected posture

### Routing correction

Earlier in this commit cycle CS placed the addendum at the CS-review
step. That was premature — Team Lead's routing note clarifies:

```text
Team Lead filter:       PASS
Next:                   Senior conceptual review  (CURRENT STEP)
After Senior PASS:      CS review (implementability + artifact path +
                                   template usability + standing-rule
                                   path convention)
Finally:                Manager adoption decision
```

CS is **not** the immediate next reviewer; Senior is. CS holds for
Senior's conceptual-review outcome before issuing CS review.

The routing record in
`governance/2026-06-10_lane1a/PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM-v0.3-2026-06-11.md`
has been updated to reflect this.

### CS-readiness preparation (preliminary, non-binding)

To make CS's eventual review faster when it arrives, CS records two
pre-verification findings that the CS review can incorporate if/when
Senior PASSes:

**Pre-verification 1 — §8 R6 Paper 3 D2 quote: VERIFIED present in
released v1.1 manuscript.**

The addendum's §8 cites Paper 3 v1.1 §D2 as carrying the
battery-sensitivity ancestor of the Pre-Lock Instrument Validation
requirements:

> *"Battery sensitivity is demonstrated against the pre-registered
> deterministic shortcut implementations — dummy-policy outputs
> computed offline — not inferred from the candidate's failure to
> exhibit the shortcut."*

CS verified by direct grep of
`papers/paper3-certification-before-retention/certification-before-retention.md`
at the v1.1 release tag: the sentence appears verbatim at line 108
of the released manuscript. The R6 inheritance claim is factually
correct: this requirement DID exist in released text and DID not
inherit into the reconnaissance lane. The addendum is itself an act
of R6 compliance, as it states.

**Pre-verification 2 — §9 adoption condition (standing-rule path
convention): CONVENTION EXISTS; PROPOSED PATH IS CONSISTENT.**

The addendum's §9 says: *"before adoption, CS must confirm the
committed standing-rule path convention and the intended home for
this addendum. This addendum proposes `governance/standing/`; the
convention — including the never-confirmed committed path of
`STANDING-REVIEW-DISCIPLINE.md` — is resolved in the adoption commit,
not left open in the adopted text."*

CS confirms:

| Existing standing-rule artifact | Repo path |
|---|---|
| `STANDING-REVIEW-DISCIPLINE.md` | `governance/standing/STANDING-REVIEW-DISCIPLINE.md` (sha256 `fa3142e9…`) |
| `STANDING-NON-AUTHORIZATIONS.md` | `governance/standing/STANDING-NON-AUTHORIZATIONS.md` |

The convention is: **lane-specific governance lives under
`governance/<date>_<lane>/`; cross-lane standing rules live under
`governance/standing/`.** This convention has been operating since
the standing rules were first filed, but the addendum is right that
it has never been formally written down as a rule. CS recommends
adoption commit include a one-sentence path-convention codification
(e.g., in `STANDING-REVIEW-DISCIPLINE.md` or a new
`STANDING-PATH-CONVENTIONS.md`).

The proposed path
`governance/standing/PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM.md` is
consistent with this convention. CS endorses the placement.

### Things CS will look at in its actual review (after Senior PASS)

For the record, here is the checklist CS will work through when CS
review is the active step:

| Item | What CS will verify |
|---|---|
| **Implementability** | Every requirement has a clear vehicle, owner, and audit artifact (the "enforcement triple"). Every requirement specifies what produces "PASS" determinable from artifacts CS can build. The "Lock consequence" language is operationally clear. |
| **Artifact path** | The proposed `governance/standing/` home matches the convention. The adoption commit codifies the convention itself (above). |
| **Template usability** | Appendix T1/T2/T3/T4 skeletons translate cleanly to executable artifacts (YAML schema, JSON schema, or markdown templates). CS can produce a working `validation_report_skeleton.{yaml,md}` post-adoption. |
| **Standing-rule path convention** | Confirmed established (per Pre-verification 2 above). |
| **R6 install coherence** | R6 is being installed via two paths simultaneously: (a) close-out v1.2 §10 (per Team Lead direction §4); (b) this addendum §8. The two carry identical R6 text. CS will install R6 in `STANDING-REVIEW-DISCIPLINE.md` once via whichever adoption commits first; the second adoption references the existing R6 rather than re-installing. |
| **Cross-reference with prior CS-filed standing rules** | No conflict expected with G1-open production rule, sibling-artifact cross-reference rule, or production-path subprocess smoke test rule; the new addendum complements all three. |

CS will NOT issue these as a substantive PASS / HOLD verdict until
Senior's conceptual review completes and routes the document to CS.

### Boundary acknowledged

This routing note authorizes nothing beyond Senior conceptual review
of v0.3. CS preserves all 14 non-authorizations enumerated in §4 of
Team Lead's routing note. No execution, no Lane 1a′ work, no Paper 3
revision, no model/data activity.

## CS posture

```text
Team Lead filter of v0.3:                PASS
Senior conceptual review:                IN FLIGHT (current step)
CS review:                               HOLDS for Senior PASS
CS pre-verification of factual claims:   §8 D2 quote VERIFIED;
                                          §9 path convention CONFIRMED
CS readiness for actual review:          checklist documented above
Manager adoption decision:               PENDING (final step)

Lane 1a close-out:                       CLOSED-PENDING-ADOPTION
                                          (parallel work; Senior owns v1.2 draft)
All non-Lane-1a execution gates:         CLOSED
```

— CS Engineer, 2026-06-11
