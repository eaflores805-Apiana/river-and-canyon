# Standing Review Discipline — Failure-Mode Review Prompt

*Team Lead 2026-06-10. Process update for future reviews. Standing rule — applies to every review of a lane, protocol change, governance rule, or experimental proposal going forward. Not an authorization; only a methodology.*

---

## The rule, in one line

> *"Do not ask reviewers only whether they agree. Ask reviewers how the proposal fails if everyone is trying to do the right thing."*

This applies to every CS review, every Senior review, every Contributor review of a new lane, protocol change, governance rule, or experimental proposal.

## What it replaces

Earlier review prompts often took the form *"Is this useful and safe?"* — which invites endorsement or rejection but does not force the reviewer to look for the specific leak. The Lane 1a discussion exposed how that framing under-recruits the catch we want: reconnaissance data quietly becoming candidate-selection pressure; clarifications becoming new authorizations; implementation details changing scientific claims.

The Lane 1a case in concrete form:
- Original question (too broad): *"Is this lane useful and safe?"*
- Better question (the one Contributor 4 effectively answered): *"Assume Lane 1a is well-intentioned and still contaminates candidate selection or threshold design. How does that happen?"*

That sharper framing should be the default going forward.

---

## The 9-item failure-mode review prompt

For every new lane, protocol change, governance rule, or experimental proposal, the reviewer should be asked to answer:

```
1. What can this proposal be misused as?
2. What later decision could this contaminate?
3. What positive inference might people draw even if the proposal forbids it?
4. What artifact, schema field, figure, table, or label could become de facto evidence?
5. What must be made impossible by construction, not merely forbidden by wording?
6. Which protection is structural, and which protection is only an honor-system rule?
7. What non-claim is missing?
8. What future gate could this silently weaken?
9. Should the proposal be: accepted, accepted only with constraints, parked, or rejected?
```

This is the default review prompt for risk-bearing design changes.

---

## Lane-specific failure-mode questions

The review prompt should be tailored to the lane's likely failure mode:

| Lane / proposal | Failure-mode question to ask |
|---|---|
| Lane 1a | How could reconnaissance become pre-selection, threshold tuning, or certification rehearsal? |
| Paper 3 v1.1 | How could a clarification become a new authorization? |
| B1 v2.1 | How could an implementation detail change the scientific claim? |
| Candidate Selection Memo | How could prior knowledge bias candidate choice before thresholds are locked? |
| Threshold-sheet lock | How could historical information or sweep outputs leak into threshold values? |
| Certification evaluation | How could a diagnostic profile be mistaken for a certification verdict? |
| Stress-retention run | How could retention be confused with correctness again? |

Reviewers should ask the lane-specific question first, then run the 9-item general prompt.

---

## Protection-layer taxonomy

Reviewers should explicitly classify each proposed protection by where its enforcement lives. The taxonomy, in increasing strength:

```
protected by wording          (weakest — depends on memory and discipline)
protected by role separation  (procedural; depends on enforcement)
protected by schema           (output type or field cannot represent the violation)
protected by code             (analysis script structurally cannot emit the violation)
protected by provenance       (artifact hashes / firewall make tampering detectable)
protected by Manager gate     (cannot proceed without explicit authorization)
```

If a protection is *only* by wording, reviewers should say so. The fix is usually to convert wording-only protections to a stronger layer: encode the forbidden state as unrepresentable in the schema, make the analysis script structurally refuse to emit it, or hash-lock the relevant artifact.

Examples of strong structural protections already in the program:

- **Schema:** Lane 1a verdict enum may contain only `clearly_fails_D*` and `requires_further_investigation` — no `passes_*` value exists; positive-selection cannot be emitted.
- **Code:** Plot style file locked; "promising region" rendering cannot be produced.
- **Provenance:** Threshold-sheet content hash verified before content trust (Senior C3); analysis script hash locked at sweep authorization.
- **Manager gate:** Framework-version supersession check (H3) refuses superseded identifiers at runtime.

---

## The Lane 1a lesson, distilled

```
Lane 1a may rule out.
Lane 1a may not rule in.
```

That distinction emerged because reviewers were eventually asked what the lane could *become* in practice, not merely what it was *intended* to be.

The same pattern applies everywhere: **a proposal's stated intent is not enough; we need to ask what its artifacts will do after they exist.**

---

## How CS applies this rule going forward

Every CS review of a substantive proposal carries:

1. The lane-specific failure-mode question at the top.
2. The 9-item prompt answered explicitly.
3. The protection-layer taxonomy applied to each protective rule in the proposal — noting which are wording-only and recommending structural alternatives.
4. A standard verdict (accept / accept-with-constraints / park / reject) per §1 item 9.

This applies to: paper revision reviews, lane authorization reviews, B1 plan reviews, governance-rule reviews. Editorial-only revisions stay light per the existing paper-revision cadence rule.

---

## Process status

Team Lead will include the failure-mode prompt section in future review packets for: Paper 3 v1.1, Lane 1a, Candidate Selection Memo, B1 v2.1, threshold-sheet design, certification evaluation, and stress-retention execution. CS adopts the rule unilaterally for its own review filings starting now.

---

## Non-authorizations (carried forward)

This standing rule does not authorize any execution lane. See `governance/standing/STANDING-NON-AUTHORIZATIONS.md` for the full canonical list.

---

— Team Lead authored 2026-06-10; CS filed 2026-06-10
