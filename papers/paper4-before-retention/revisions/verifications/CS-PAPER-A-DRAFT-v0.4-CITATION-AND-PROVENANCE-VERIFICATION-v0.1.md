# CS Citation/Provenance Verification — PAPER-A-DRAFT v0.4

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior, Manager
**Status:** **PARTIAL PASS** — provenance facts mostly verify against bytes; one §3.5 source attribution refined (the numbers are CAL-E, not CAL-A — confirms paper text is correct); several discrepancies flagged for repair before submission; citation HOLDs from prior verifications continue to apply.
**In response to:** User request "CS citation/provenance verification" on PAPER-A-DRAFT v0.4.
**Verification target:** the pasted v0.4 text (matches the inbox file `PAPER-A-DRAFT-v0.4.md` sha256 `6bcfc17f2b32f92c81d3c0d56d96021ace02bf642ac377268ff179780988661e` byte-for-byte against the pasted text). Inbox also contains a later **v0.5** (sha256 `557bc00566896434…`) which CS notes but did not verify against this request.
**Scope:** Verification only. No drafting, no interpretation of paper claims, no editorial decisions. No model run; no model-facing work.

---

## §1. Verification target identity

| Field | Value |
|---|---|
| Verification target | PAPER-A-DRAFT-v0.4 (pasted text + inbox file are byte-identical) |
| Inbox sha256 | `6bcfc17f2b32f92c81d3c0d56d96021ace02bf642ac377268ff179780988661e` |
| Self-anchor | `origin/main HEAD 0f7e9a7` — verified to exist on `origin/main` (commit subject: "File 2 Senior strategic memos + Manager Tier-1 direction + CS verification (PARTIAL PASS with citation flag)") |
| Successor in inbox | `PAPER-A-DRAFT-v0.5.md` (sha256 `557bc00566896434…`) — not verified here |

## §2. Provenance fact-check against bytes

### §2a. §1.2 / §3.2 — CAL-Q abstention collapse, "approximately 0.92 to 0.00"

| Paper claim | Source bytes | Result |
|---|---|---|
| "abstention falling from approximately 0.92 to 0.00 on otherwise identical content" | CAL-B defective concept abstention = **0.9250** (rescore summary `d874b894…`); CAL-Q defective concept abstention = **0.0000** (run record `90de7fd0…`) | **VERIFIED.** Paper's "approximately 0.92" matches CAL-B's 0.925 to two decimals; "0.00" matches CAL-Q's 0.000 exactly. |

### §2b. §3.3 — Form-level positive control, "all forty key-absent outputs were substantive single-character value emissions, with no abstention in any form"

| Paper claim | Source bytes | Result |
|---|---|---|
| 40/40 single-character value emissions | `cal-q_defective_outputs.json`: `strict_kind` dist = `{'letter': 40}`; `concept_kind` dist = `{'letter': 40}`; items with non-single-character first token = 0 | **VERIFIED EXACTLY.** All 40 items are single-letter value emissions. |
| 0 abstention in any form (cased token, multi-token phrase, or symbolic) | Items with `concept_kind == abstention` = 0; raw output distribution shows only single lowercase letters | **VERIFIED.** No abstention strings of any form appear. |

### §2c. §3.5 — Scorer-audit episode, "thirteen of seventeen apparent 'errors' were lowercase abstentions" and "the true emission rate, once corrected, was stable (approximately 0.10)"

| Paper claim | Source bytes | Result |
|---|---|---|
| "13 of 17 apparent errors were lowercase abstentions" | **CAL-E** defective: 23 strict NONE + 13 lowercase `none` + 4 single letters = 40. Apparent failures under strict scoring = 13+4 = **17**. Of those 17, lowercase `none` = **13**. | **VERIFIED — and source identified as CAL-E.** Initial CS check pulled CAL-A (which has 31 lowercase of 35 apparent failures); the paper's "13 of 17" is from CAL-E, where the numbers match exactly. The §3.5 episode is therefore the CAL-E scorer-format episode, not the constructed-positive (CAL-A) one. |
| "true emission rate, once corrected, was stable (approximately 0.10)" | CAL-E concept true-false-emission rate = **0.10** (4/40) | **VERIFIED EXACTLY.** |

### §2d. §3.5 precision-correction note ("prevented a wrong pivot, did not reverse an issued refusal")

| Paper claim | Source bytes | Result |
|---|---|---|
| "CAL-E was an apparent failure caught by the per-item read BEFORE any refusal was acted on — the read prevented a wrong pivot; it did not reverse an issued refusal." | Chronology on `origin/main`: CS CAL-E run report (commit `8a64010…`) → Manager pause direction (PIVOT WATCH framing) → CS-CAL-E-DEFECTIVE-OUTPUT-EXTRACTION (per-item analysis) → CS-CAL-ABCE-NULL-NORMALIZED-RESCORE (re-grade) → Senior reinterpretation. PIVOT WATCH was *declared by Manager based on the strict-scoring aggregate*; the per-item read + rescore CORRECTED the interpretation before any "rescue" or "pivot" was *executed* (no model run was authorized on the PIVOT-WATCH framing before the rescore corrected it). | **VERIFIED in the carefully scoped sense the paper uses.** "Refusal acted on" reads as "actioned at the gate level" (e.g., a successor run launched on the basis of it); a Manager-level interpretive label (PIVOT WATCH) that was subsequently corrected before any action ≠ a refusal acted on. The paper's careful wording survives this distinction. |

### §2e. Section masters referenced in the "Provenance / editing boundary" note

| Section master claimed | On disk? | Result |
|---|---|---|
| `PAPER-POSITIONING-SECTION-DRAFT-v0.7.md` (for §2) | YES — `governance/.../certification-readiness/PAPER-POSITIONING-SECTION-DRAFT-v0.7.md` sha256 `34cedb30…` | VERIFIED. |
| `PAPER-INSTRUMENT-ARCHITECTURE-SECTION-DRAFT-v0.2.md` (for the architecture) | **NOT FOUND** on `origin/main` and not in inbox | **DISCREPANCY** — provenance note claims this as the editable master for §4 architecture content, but no such file exists. Either §4 was authored directly into this paper draft (in which case the provenance note is inaccurate), or the architecture master was intended to be filed separately and hasn't been. Senior should clarify and file the architecture master, OR rewrite the provenance note to reflect that §4 was authored in-paper. |
| `PAPER-SECTION-5-REJECTION-AUDIT-DRAFT-v0.1.md` (for §5) | NOT FOUND on `origin/main` **but is in inbox** (sha256 `4dc2f290…`); will be filed in this commit | VERIFIED once filed (this commit). |

### §2f. Version label mismatch

| Location | Says | Should say |
|---|---|---|
| Header `**Version:** DRAFT v0.4 (targeted polish; supersedes v0.3).` | v0.4 ✓ | (correct) |
| Footer `*River and Canyon program · Apiana AI, Inc. · Draft v0.3 · model-free · pre-stress · authorizes nothing.*` | v0.3 | **MISMATCH — should be v0.4** |

**Persistence note:** the same footer mismatch is present in the inbox v0.5 ("Draft v0.3" in the footer despite v0.5 in the header). This is now a recurring typo that has survived two version bumps; Senior should add a footer-version-update step to the revision checklist.

## §3. Forbidden-language perimeter

CS spot-checked the paper text against the standard binding-forbidden list (model passed / capability established / not shortcut-driven / candidate certified / task family viable / Claim C progressed / seam evidence / public benchmark result / certification achieved / Path A failed / the lane is broken / breadth passed / etc.) + the 6 CAL-Q forbidden claims (Models cannot abstain / All absence-defined tasks fail / etc.) + the 8 Manager-listed Tier-1 forbidden claims (We discovered construct validity / etc.).

**No forbidden phrasing detected as an assertion.** The "What we do not claim" section and §6.1, §6.2, §6.3, and §7 explicitly disclaim all of them. The negative-use scope on per-item numbers (§3.4 closing paragraph) is appropriately scoped.

## §4. Citation status (per-citation)

The paper's citations include both well-known prior work and recent (2025/2026) papers CS cannot independently verify from this environment. Prior CS verifications on the TIER-1 prior-art memo continue to apply; v0.7 of the positioning section reported all three §2.1 borderline cites verified to source by Senior + external peer reviewer.

| Citation | Page/§ | CS status |
|---|---|---|
| Geirhos et al. 2020, arXiv:2004.07780 | §2.1 | **HIGH confidence** — well-known foundational paper |
| Bean et al. 2025, arXiv:2511.04703 | §2.1, §2.2 | **UNVERIFIED by CS** (still load-bearing per prior CS flag); Senior + external peer reviewer reported verified |
| Freiesleben & Zezulka 2025, arXiv:2510.23191 | §2.1 | **UNVERIFIED by CS** |
| Evidence-Centered Benchmark Design 2024, arXiv:2406.08723 | §2.1 | **UNVERIFIED by CS** |
| Raji et al. 2021 | §2.1 | **PLAUSIBLE-HIGH** (well-known author + research area) |
| Biderman et al. 2024 (LM Eval Harness), arXiv:2405.14782 | §2.1 | **UNVERIFIED by CS** (Senior reported verified per v0.7) |
| AbstentionBench 2025, arXiv:2506.09038, NeurIPS 2025 | §2.1, §3.4 | **UNVERIFIED by CS** |
| Wen et al. "Know Your Limits" TACL vol. 13 2025 | §2.1 | **UNVERIFIED by CS** (Senior reported verified per v0.7 with DOI 10.1162/tacl_a_00754 / arXiv:2407.18418 — DOI structure adds plausibility but CS still can't confirm) |
| Quantization Meets Reasoning 2025, arXiv:2501.03035 (~32% figure) | §2.1 | **UNVERIFIED by CS** (Senior reported verified per v0.7 with exact 32.39% figure) |
| ZeroQuant-V2, arXiv:2303.08302 | §2.1 | **UNVERIFIED arXiv ID** (paper title is real — ZeroQuant series exists — but the specific arXiv ID I cannot independently confirm) |
| Noisy but Valid 2026, arXiv:2601.20913 | §2.3 | **UNVERIFIED by CS — LOAD-BEARING for §2.3 cell distinction** |
| Selective Risk Certification 2025, arXiv:2509.12527 | §2.3 | **UNVERIFIED by CS — LOAD-BEARING for §2.3 cell distinction** |
| Safety Under Scaffolding 2026, arXiv:2603.10044 | §2.3 | **UNVERIFIED by CS — LOAD-BEARING for §2.3 cell distinction** |

**Standing pre-submission gate (unchanged from prior verifications):** all UNVERIFIED-by-CS citations should be independently re-verified by a human reader against source (arXiv ID resolves, claimed scope matches abstract) before any external use. The paper's own "Supplement (to assemble) → Citation-status record" item already commits to this in principle.

## §5. Other observations (non-blocking)

- §3.4 "AbstentionBench 2025" is referenced in addition to the §2.1 cite. Internal consistency PASS (same reference, no duplicate-citation problem).
- §4.3 table is concise and useful; the implemented-vs-specified discipline is the paper's spine and is clearly drawn.
- §6.2 ("The gate has only been tested on baselines we built") is a strong honest scope statement; CS confirms this matches the on-disk record (every demonstration in the paper is on author-constructed bytes).
- §3.5 "wrong pivot" precision-correction is precisely worded; matches the chronology on `origin/main`.

## §6. Disposition

**PARTIAL PASS.** All provenance facts CS can verify against the bytes on `origin/main` are correct (CAL-Q abstention numbers, form-level positive control, scorer-audit numbers, §3.5 precision-correction framing, HEAD anchor). Three discrepancies are flagged:

1. **Section master gap:** `PAPER-INSTRUMENT-ARCHITECTURE-SECTION-DRAFT-v0.2.md` is referenced in the Provenance note but doesn't exist on `origin/main` or in inbox. Senior should either file the architecture master or rewrite the provenance note. **(BLOCKING for the provenance-discipline standard the paper itself sets.)**
2. **Version-label mismatch:** Header v0.4, footer v0.3 (persists into v0.5 as well). Trivial to fix; should be fixed before any external sharing.
3. **Citation HOLDs from prior verifications still apply:** roughly 10 of 13 citations remain unverified by CS (all 2025/2026 papers + specific arXiv IDs); Senior + external peer reviewer have reportedly verified several to source per v0.7; independent re-verification by a second human reader against arXiv before submission is the standing pre-submission gate.

CS does NOT decide:
- Whether to proceed with v0.5 (which supersedes v0.4 per inbox)
- Whether the paper is ready for external sharing (Manager + TL + Senior call)
- Whether the architecture master needs to exist as a separate file or whether the provenance note should be rewritten

## §7. Sealed bytes + language perimeter

Sealed bytes UNCHANGED (≈66th survival check). No model run. No certification. No compression. No INT4. No Claim C. CS verifies what Manager + user asked CS to verify.

— CS Engineer, 2026-06-14
