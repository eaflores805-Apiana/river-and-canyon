# Manager Authorization — Paper 3 v1.1 Remediation Scope

*Recorded by Senior Engineer from Manager approval given 2026-06-10, in response to the Team Lead
disposition on the Paper 3 v1.0 known-issues intake (§§8–9 of that memo). Intended path:
`governance/2026-06-10_paper3-v1.0-release/MANAGER-AUTHORIZATION-v1.1-SCOPE.md`. Authorizer:
E. A. Flores, Manager.*

## Decisions taken

1. **v1.1 remediation scope: AUTHORIZED**, exactly as Team-Lead-recommended — E1 (dual-mode D2 with the
   corrected mixtures-as-complete-accounts non-claim), E2 (D6 timestamp storage-side clarification),
   M1/M2 (satisfiability and D1×D7 window arithmetic), M3 (certifier operating-characteristics section,
   gate-provenance rows sourced from the documented record only), Q1 (`evaluation_mode` field), Q2
   (adapted disclaimer tightening preserving the three aligned non-claim blocks), G1 (governance
   transfer-correction commits).
2. **SYNTHETIC illustrative-number convention: APPROVED** for M1/M2 — every illustrative value
   SYNTHETIC-labeled, non-binding, not a threshold value, not a candidate sheet, not evidence.
3. **Confirmed:** this authorization includes **no** candidate selection, no candidate ranking, no
   threshold-sheet population or lock (beyond SYNTHETIC non-binding illustration), no certification
   evaluation, no runs of any kind, and no B1 v2.1 implementation. All execution gates remain closed.

## Implementation specification

The Team Lead feedback synthesis of 2026-06-10 sharpens the implementation instructions within this
same authorized scope (three-mode D2 with union envelope; explicit E2 storage mapping; Appendix-B
SYNTHETIC note with off-program values only; reporting_mode rename and guardrails; Q2 three-block
preservation; strengthened G1 transfer rule; new H3 framework-supersession rule; backlog 9 → 11–12).
The scope kind is unchanged: manuscript and schema-as-documented edits only.

## Scope boundary

This is manuscript remediation only. The remediation vehicle is `paper3-certification-protocol-v1.1`,
which follows the established release rail (draft → review → RC-is-final-text → tag) when ready. The
Paper 3 v1.0 tag and manuscript remain untouched; v1.0 remains the released version until v1.1 releases.

## Routing executed with this record

Committed together per the Team Lead's G1 disposition: this authorization;
`KNOWN-ISSUES-AND-DEFERRALS.md`; the v0.7 referee report and the Senior disposition of it (the
previously uncommitted external-review records); and the v1.0 external review.

— Recorded by Senior Engineer; authorized by E. A. Flores, Manager, 2026-06-10
