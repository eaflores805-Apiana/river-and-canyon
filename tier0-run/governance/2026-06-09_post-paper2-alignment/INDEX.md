# Governance Filing Index — Post-Paper 2 Alignment

**Directory:** `tier0-run/governance/2026-06-09_post-paper2-alignment/`  
**Filed:** 2026-06-09  
**Filed by:** CS Engineer  
**Trigger:** Team Update — Post-Paper 2 Alignment and Routing (2026-06-09); Team Lead Required Clarifications memo (2026-06-09)

---

## Files in this directory

| File | Description | Version |
|---|---|---|
| `TEAM-UPDATE-POST-PAPER2-ALIGNMENT.md` | Governance record of Team Update memo; retraction disposition; correction requirements; CS deliverable status table | v1 |
| `PAPER2-RECOMPUTATION-CLOSE.md` | Formal recomputation close — all 9 confirmations; 12 per-cell accuracy counts; Cell03 group decomposition; neg_graph endpoint taxonomy (§8-level); Gate 5 max_det; voided-run exclusion; no mismatches | v1 |
| `PAPER2-CORRECTION-CONFIRMATION.md` | Confirmation of two Senior corrections; Cell02 label RESOLVED; §4.5 scope RESOLVED; value-check query on "(3,11,6)" routed to Senior | v1 |
| `FORK-A-CLARIFICATION-RETRACTION-NOTE.md` | **Stress retraction remains.** Plain answer + figure-by-figure table (8-column); 6-condition reactivation bar evaluation (conditions 2, 3, 5 not met); classification: historical artifact only; paper wording narrowing required ("Paper 2 construction") | v2 (supersedes v1) |
| `FREEZE-TAG-REPORT.md` | Complete freeze/tag record: all runner/scorer/manifest/tokenizer/validator/prompt/result hashes; voided-run exclusion list; unrecoverable hashes marked; Paper 2 tag prerequisites checklist | v2 (supersedes v1) |
| `B1-IMPLEMENTATION-PLAN.md` | File-level B1 plan: gap analysis, all required new fields (incl. quant_method, eligibility_reason_code, voided_run_log, comparison_table for stress); 14 unit tests; execution order; out-of-scope list | v2 (updated from v1) |
| `PAPER2-REPRODUCTION-ACCEPTANCE-TEST-PLAN.md` | 8 acceptance tests (AT-1 through AT-8) with exact expected values; pre-run checklist; protocol; disposition | v1 |
| `PAPER2-FREEZE-TAG-REPORT.md` | Freeze/tag report: tag name `paper2-cells01-03-v1.0`; all 11 hash tables verified on-disk; voided-run exclusion; 3 unrecoverable gaps; no artifacts modified; Appendix B verification with 2 issues flagged (Cell01 notation, stress wording); 5-item prerequisite checklist before tag application | v1 |
| `PAPER2-RECOMPUTATION-CLOSE.md` | Formal recomputation close — all 9 confirmations from Team Lead §2; 12 per-cell counts; neg_graph §8 taxonomy; Gate 5; voided-run confirmed excluded; no mismatches | v1 |
| `PAPER2-CORRECTION-CONFIRMATION.md` | Cell02 label correction RESOLVED; §4.5 scope RESOLVED; value-check query on "(3,11,6)" routed to Senior | v1 |

---

## Outstanding items requiring action by others

| Item | Owner | Status |
|---|---|---|
| Verify "(3, 11, 6)" triple against artifact hop1 table in `PAPER2-CORRECTION-CONFIRMATION.md` | Senior | PENDING |
| Accept two Paper 2 framing corrections | Senior | PENDING |
| Narrow Paper 2 no-stress sentence to "Paper 2 construction" | Senior | PENDING — per Fork A §4 wording consequence |
| Commit manuscript to repo before tag | Senior or Manager (outside CS scope) | **BLOCKING** |
| Correct Appendix B Cell01 notation (`7d…→00a7adf8` → `00a7adf8`) | Senior | **BLOCKING for camera-ready** |
| Correct Appendix B stress wording ("any task" → "this construction") | Senior | **BLOCKING for camera-ready** |
| Confirm or flag model snapshot `aa8e7253…` sourcing | Senior | PENDING |
| Authorize Paper 2 freeze tag | Manager | PENDING (after corrections) |
| Confirm B1 code-change authorization | Manager | PENDING |
| Confirm Gate 2 threshold values for B1 | Team Lead | PENDING |
| Update running map — Fork A stress retraction confirmed | Team Lead | PENDING — retraction confirmed, not reversed |
| B1 runner implementation | CS | BLOCKED (awaiting authorization) |
| B1 acceptance test run | CS | BLOCKED (awaiting B1 runner + authorization) |
