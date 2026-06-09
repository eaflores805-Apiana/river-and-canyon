# Team Update — Post-Paper 2 Alignment and Routing

**Date:** 2026-06-09  
**From:** Team Lead  
**To:** Full team  
**Filed by:** CS Engineer (governance record)  
**Purpose:** Canonical governance record of the post-Paper 2 alignment memo. All CS deliverables referenced herein are filed in this directory.

---

## Approved Posture

- Paper 2 is draft-complete at v0.2. Two corrections required before external routing (see PAPER2-RECOMPUTATION-REPORT.md §5).
- Fork A stress figures are retracted pending CS artifact verification. CS verification complete (see FORK-A-CLARIFICATION-RETRACTION-NOTE.md). Figures confirmed artifact-backed; provenance gap below B1 standard disclosed.
- B1 harness backfill approved as bounded validity-hardening. No new cells, no new runs, no B or C claims.
- Post-Paper 2 roadmap: Track A (constructibility boundary map), Track B (blocked), Track C (deferred).

---

## CS Next Actions (per Team Update directive)

All five deliverables filed in this directory:

| Deliverable | File | Status |
|---|---|---|
| Paper 2 recomputation report | `PAPER2-RECOMPUTATION-REPORT.md` | FILED 2026-06-09 |
| Freeze/tag report | `FREEZE-TAG-REPORT.md` | FILED 2026-06-09 |
| Fork A clarification with retraction note | `FORK-A-CLARIFICATION-RETRACTION-NOTE.md` | FILED 2026-06-09 |
| B1 file-level implementation plan | `B1-IMPLEMENTATION-PLAN.md` | FILED 2026-06-09 |
| Paper 2 reproduction acceptance test plan | `PAPER2-REPRODUCTION-ACCEPTANCE-TEST-PLAN.md` | FILED 2026-06-09 |

---

## Fork A Retraction Status

**Original retraction:** "Fork A INT8 23/24, INT4 24/24, and n=8 8/8 stress figures are retracted and must not be reused unless CS verifies artifact-backed status."

**CS verification outcome:** All four figures artifact-backed and accurate. Same-error identity confirmed logged. Provenance gap identified: Fork A result files have empty `provenance: {}` block; metadata at top level; missing scorer_hash, manifest_hash, runner_hash, mlx_lm_version — below B1 standard. Figures may be reused subject to conditions in FORK-A-CLARIFICATION-RETRACTION-NOTE.md §5.

**Retraction disposition:** Resolved as VERIFIED WITH PROVENANCE CAVEAT. See FORK-A-CLARIFICATION-RETRACTION-NOTE.md for full terms.

---

## Paper 2 Corrections Required Before External Routing

1. **Cell02 "all-ct-last" label — FACTUAL ERROR.** ct is at context position 6 (not last). cd2 is at position 7 (last). Requires text correction in Paper 2. (Owner: Senior)
2. **"(3, 11, 6)" in §4.5 — AMBIGUITY.** Scope of the triple must be stated explicitly (hop1 only). (Owner: Senior to clarify and correct)

See PAPER2-RECOMPUTATION-REPORT.md §5 for full details.

---

## B1 Authorization

B1 backfill execution requires:
- Team Lead confirmation of Gate 2 threshold values
- Manager authorization for code changes (Team Update approves "bounded validity-hardening" — confirm this covers runner amendment)

See B1-IMPLEMENTATION-PLAN.md §7 for prerequisites checklist.

---

*Filed as governance record by CS Engineer, 2026-06-09*
