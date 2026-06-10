# CS Technical Review — Paper 3 v1.0 (Release Event)

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Team Lead, Senior Engineer, Manager
**Re:** CS review of *Certification Before Retention* — v1.0 (released)
**Reviewed against:** v0.9 (last full CS review at `CS-REVIEW-PAPER3-DRAFT-V09.md`)

---

## Record status

```
CS review filed.
v1.0 is a release pass on v0.9 content — no substantive D1-D7, §5, §6, or
Appendix changes.
v1.0 is the first lock-eligible framework version: paper3-certification-protocol-v1.0.
B1 v2.1 backlog item #5 (draft vs. released framework version naming check)
now has a concrete naming convention to enforce.
Persisting soft note on D6 §5/§7 cross-references closed as deliberate
(unchanged across six revisions).
CS recommendation: v1.0 accepted as released form from a CS standpoint.
No candidate selected. No threshold values set. No runs authorized.
```

---

## What changed v0.9 → v1.0

Per cadence rule, classified as editorial-only content with a governance-significant
release event.

**Content deltas (all editorial):**

1. Version bump in header: `v0.9` → `v1.0`.
2. Status block — "draft v0.9 for Team Lead review" removed; v1.0 ships with the
   protocol/methods-paper status only.
3. Framework version block — "draft framework identifier ... not yet lock-eligible"
   replaced with "stable identifier ... lock-eligible from the release tag onward."
4. §2 first paragraph — two sentences collapsed into one with a colon. Pure
   editorial smoothing.

**Unchanged (v0.9 carries forward as substantive review of record):**

- All seven gate definitions (D1–D7) including v0.9's anti-circular battery
  sensitivity, stratum saturation option, undeclared-emission-bias non-claim, etc.
- §5 general decision rules (tie-equals-fail, void rule, worst-case repeats,
  adjudication scope).
- §6 four-category interpretation structure (Success / Failure / Scientific /
  Non-claim per gate).
- Appendix A.1 threshold sheet (same fields, same organization).
- Appendix A.2 `gate_summary` schema (same 21 fields, including the v0.9 firewall
  status and D4 applicability additions).
- Appendix A.3 negative-certification report.
- All four figures.
- References (including the v0.9-resolved [3] body wording).

---

## The release event

v1.0 is the first **lock-eligible** framework version. Per the constraint Senior
added in v0.7+ and maintained through v0.8/v0.9:

> *"Threshold sheets lock only against a released framework version, not a draft
> identifier."*

v0.6 through v0.9 were explicitly draft identifiers (`paper3-certification-protocol-v0.x`)
and not lock-eligible. v1.0 is the first version against which a threshold sheet
*could* be locked — if and when Manager authorizes candidate selection.

To be clear: v1.0's lock-eligibility does **not** authorize candidate selection,
threshold-sheet creation, or certification evaluation. Those remain Manager-gated.
v1.0 is necessary for those steps to be possible; it is not sufficient on its own.

---

## Concrete implication for B1 v2.1 backlog

B1 v2.1 backlog item #5 — "Draft vs. released framework version naming check" — now
has a concrete naming convention to enforce.

**Proposed rule for B1 v2.1:**

- `framework_version` matching pattern `paper3-certification-protocol-v0.*` →
  treated as draft; B1 refuses to proceed (sheets locked against draft identifiers
  are invalid per Paper 3 §"Framework version").
- `framework_version` matching pattern `paper3-certification-protocol-v1.*` (or
  `v2.*`, etc.) → treated as released; B1 proceeds per the existing
  `validate_framework_version_agreement` flow.

This is a one-line addition to `validate_framework_version_agreement` in
`runner_b1_v2.py`. Scope as part of the B1 v2.1 "Paper 3 substrate completion"
change at first candidate authorization.

The other 8 B1 v2.1 backlog items from v0.7/v0.8/v0.9 are unchanged.

---

## Persisting soft note — now closed as deliberate

The D6 §5/§7 cross-references for historical-knowledge shading have been carried
as a CS soft note since v0.3. Senior had six revisions (v0.4 → v0.5 → v0.6 → v0.7
→ v0.8 → v0.9 → v1.0) to address and chose not to. Senior's call is now confirmed
by shipping v1.0 with the cross-references intact.

CS closes this finding as **deliberate Senior choice**, not an oversight. Will not
flag in future reviews.

---

## Adjacent release items (not in CS scope, but flagged for awareness)

A v1.0 release typically triggers additional governance work. These are
Senior/Manager calls, not CS-unilateral actions:

| Item | Likely owner | Status |
|---|---|---|
| Land manuscript in `papers/paper3-certification-before-retention/` | Senior | Open |
| File Paper 3 v1.0 release record (parallel to Paper 2 v1.0 `RELEASE-RECORD.md`) | Manager / Senior | Open |
| Tag the release commit (e.g., `paper3-v1.0`) | Manager | Open |
| Update root `README.md` / `STATUS.md` to reflect Paper 3 release | Senior / Manager | Open |
| Update onboarding `passdown letter` to note v1.0 ships | CS (next passdown) | Will be done at session close |

CS stands ready to support any of these on instruction.

---

## CS-side transparency

v1.0 was reviewed in full per the paper-revision cadence rule. Editorial pass
plus release event handled accordingly.

---

## Summary

| Surface | Status |
|---|---|
| Substantive content (D1–D7, §5, §6, Appendix A) | Unchanged from v0.9; v0.9 review of record |
| Framework version lock-eligibility | First-time **lock-eligible** at v1.0 |
| B1 v2.1 backlog item #5 (draft vs. released naming) | Concrete rule available; one-line addition |
| Persisting soft note (D6 §5/§7) | **Closed as deliberate**; will not re-flag |
| Cumulative B1 v2.1 backlog | 9 items, unchanged from v0.9 review |
| Consistency with locked B1 v2 | Clean |

**CS recommendation:** v1.0 is accepted as the released form of the Paper 3
framework from a CS standpoint. All v0.9-equivalent substantive surfaces remain
unchanged; the release event itself is the headline.

---

## Non-authorizations (carried forward)

```
candidate selection · threshold values · certification evaluation
new runs · re-runs beyond authorized reproduction validation
unconditioned token-prior runs · activation logging
INT8 / INT4 execution · multi-model execution
Fork A reactivation · Claim C activation
Paper 3 execution as an experiment · Paper 6 activation
public benchmark packaging · artifact mutation
```

---

— CS Engineer, 2026-06-10
