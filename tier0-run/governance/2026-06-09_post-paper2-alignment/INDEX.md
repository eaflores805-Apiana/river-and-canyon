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

## Item disposition — 2026-06-09

All items from the initial outstanding list were resolved before or during the Paper 2 v1.0 release cycle. Final dispositions:

| Item | Owner | Final Status |
|---|---|---|
| Verify "(3, 11, 6)" triple against artifact hop1 table | Senior | RESOLVED — confirmed as hop1 scope; §4.5 qualifier added |
| Accept two Paper 2 framing corrections | Senior | RESOLVED — Cell02 ct-pos label corrected; §4.5 scope qualified |
| Narrow Paper 2 no-stress sentence to "Paper 2 construction" | Senior | RESOLVED — wording updated before tag |
| Commit manuscript to repo before tag | Manager | RESOLVED — manuscript committed; tag `paper2-cells01-03-v1.0` executed on commit `40c0cd5a` |
| Correct Appendix B Cell01 notation | Senior | RESOLVED — 13/13 hash table corrected; manuscript blob `7d6706a3…` tagged |
| Correct Appendix B stress wording | Senior | RESOLVED — wording scoped to this construction before tag |
| Confirm model snapshot `aa8e7253…` sourcing | Senior | RESOLVED — asserted-only; runner-provenance backing deferred to B1 (disclosed in release record) |
| Authorize Paper 2 freeze tag | Manager | RESOLVED — tag authorized and executed 2026-06-09 |
| Confirm B1 code-change authorization | Manager | **OPEN — B1 harness BLOCKED pending Manager authorization** |
| Confirm Gate 2 threshold values for B1 | Team Lead | RESOLVED — Gate 2 thresholds confirmed |
| Update running map — Fork A stress retraction confirmed | Team Lead | RESOLVED — retraction remains in force; not reversed |
| B1 runner implementation | CS | **BLOCKED — awaiting Manager code-change authorization** |
| B1 acceptance test run | CS | **BLOCKED — awaiting B1 runner + authorization** |

**Single remaining open item:** B1 harness implementation — blocked on Manager code-change authorization.

Plan: `B1-IMPLEMENTATION-PLAN.md` in this directory.  
Next authorized planning lanes: B1 harness hardening + Paper 3 threshold framework design (no runs).
