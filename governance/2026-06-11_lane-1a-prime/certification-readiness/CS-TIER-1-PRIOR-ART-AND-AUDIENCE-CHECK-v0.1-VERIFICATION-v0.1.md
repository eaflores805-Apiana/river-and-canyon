# CS Verification — Tier-1 Prior-Art and Audience Check v0.1

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** **PARTIAL PASS** — closed gates / forbidden-language / overlap-risk language all clean; **citation metadata verification is partial (CS-environment limit); one load-bearing citation flagged for independent verification before any external use**
**In response to:** Manager direction 2026-06-13 "Tier 1 Prior-Art and Audience Check" — CS owner split: "Check source names, citation metadata, overlap-risk language, and closed gates. Flag unsupported claims or citation uncertainty."
**Artifact verified:** `TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK-v0.1.md` (sha256 `dbb3833c33e477444e12e74dfb3a1fb7a7412c2dfa7d9d476ca762f8646ba825`)

---

## §1. Verification scope

Per Manager's owner split, CS checks four things:

1. **Source names** — do the citations refer to real, identifiable prior work?
2. **Citation metadata** — venues, years, arXiv IDs reasonable?
3. **Overlap-risk language** — does the memo describe the program's distinction from prior work with appropriate hedging?
4. **Closed gates** — preserved verbatim?

Plus: flag unsupported claims or citation uncertainty.

Honest CS caveat upfront: **CS does not have reliable live-web-search access from this environment.** CS can place citations against well-known prior work where the field knowledge is in CS's training; CS cannot independently verify arXiv numbers, NeurIPS 2025 / TACL 2025 publication claims, or 2025-dated papers in general. Senior's §0 provenance note ("CS should verify the source metadata independently") acknowledges this need; this verification gives CS's best read with explicit confidence per row.

## §2. Closed gates — PASS

§14 contains the standard 12-item closed-gate list: no run · no D4 rescue · no CAL-Q rerun · no certification · no compression · no INT8/INT4 stress · no second compression rung · no full ladder · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission. Verbatim consistent with prior closed-gate convention. PASS.

## §3. Standard forbidden phrasings — PASS

Grep across the standard binding-forbidden phrasing list (model passed / capability established / seam evidence / claim C progressed / certified / compression-robust / "seam is false" / "models cannot abstain" / "all absence-defined tasks fail" / "no task family can host" / "D4 can never" / "compression fragility tested"). The only matches are in §11 where Senior cites the 6 Manager-listed CAL-Q forbidden claims as REJECTED ("We proved all absence-defined tasks fail." → one family, one model). Correct usage pattern; no assertion of any forbidden claim. PASS.

## §4. Manager's CAL-Q safe-claim wording — paraphrased, not violated

The Manager's verbatim CAL-Q safe-claim wording (about format-sensitive abstention coupled to retrieval difficulty) is not quoted verbatim in this memo, but §8 paraphrases it appropriately: "The program's CAL-Q finding — abstention collapsed when the code-book query raised difficulty — is a SMALL, SPECIFIC, SAME-DIRECTION echo (difficulty/format stress degrades abstention)." The paraphrase preserves both scopings (one family, format/difficulty trigger). No drift into the 6 forbidden CAL-Q claims. PASS.

## §5. Overlap-risk language — PASS

Senior uses appropriately scoped hedging throughout:

- §2: "PLAUSIBLY DISTINCTIVE" (not "uniquely ours")
- §4: "plausibly distinctive vs. the field-owned validity work" (not "novel")
- §5: explicit risk-tier per overlap ("HIGHEST RISK / HIGH RISK / MODERATE RISK")
- §11: forbidden positioning list expanded with specific prior-art reasons for each item
- §12: "defensible as a PAPER now (with honest scoping); it is NOT yet defensible as a PRODUCT (market unproven) or as a GENERAL method (one family)"
- §9: each audience entry includes "EVIDENCE NEEDED BEFORE PITCH" — concrete missing-evidence items, not aspirational claims

The overall posture is properly defensive on novelty. No instances of overclaiming novelty. PASS.

## §6. Citation metadata — PARTIAL VERIFICATION

CS places each cited source against known prior work:

| Citation | CS confidence | Note |
|---|---|---|
| **Geirhos et al. 2020 "Shortcut learning in deep neural networks", Nat. Mach. Intell.** | **HIGH (matches well-known prior work)** | Real, widely-cited foundational paper on shortcut learning |
| **Jacobs & Wallach measurement-modeling line** | **HIGH (matches well-known prior work)** | Abigail Jacobs & Hanna Wallach "Measurement and Fairness" (FAccT 2021) and related work |
| **Raji et al. 2021** (construct validity / audits) | **PLAUSIBLE-HIGH** | Inioluwa Deborah Raji has published on benchmarks and audits ("AI and the Everything in the Whole Wide World Benchmark", NeurIPS 2021 Datasets & Benchmarks) |
| **ZeroQuant-V2** (quantization) | **PLAUSIBLE-HIGH** | Microsoft DeepSpeed ZeroQuant series is real |
| **lm-eval "Lessons from the Trenches" 2024 (arXiv 2405.14782)** | **PLAUSIBLE — UNVERIFIED arXiv ID** | EleutherAI has published lm-eval-harness reflections; specific arXiv number cannot be confirmed by CS |
| **AbstentionBench (NeurIPS 2025)** | **UNVERIFIED — recent / specific venue claim** | Topic area (abstention benchmarking) is active; specific NeurIPS 2025 publication cannot be confirmed by CS |
| **"Know Your Limits" survey (TACL 2025)** | **UNVERIFIED** | Cannot confirm |
| **SelfAware (2023)** | **UNVERIFIED** | Plausible name (some abstention-related work uses this; CS cannot confirm the specific cite) |
| **"Quantization Meets Reasoning" (arXiv 2501.03035 / 2505.11574)** | **UNVERIFIED** | Cannot confirm specific arXiv IDs |
| **Freiesleben & Zezulka 2025** | **UNVERIFIED** | Cannot confirm |
| **ECBD 2024** | **UNVERIFIED** | Acronym unclear from CS position |
| **Bean et al. 2025 "Measuring what Matters" (arXiv 2511.04703; claimed 42 authors; 445-benchmark review + operational checklist)** | **UNVERIFIED — and load-bearing** | See §7 |

## §7. CRITICAL FLAG — Bean et al. 2025 (the load-bearing citation)

The memo's defensible novelty argument **hinges** on the distinction between (a) Bean 2025's operational checklist for benchmark construct validity and (b) the program's claim of fail-closed claim-blocking enforcement in the stress-retention setting. If Bean et al. 2025 (as described) does not exist or differs materially from the description, the memo's positioning collapses:

- If Bean is hallucinated or misdescribed → the program might still have the "construct-validity operationalization" claim with less constraint, but the entire §5 / §10 / §11 framing would need to be revisited.
- If Bean exists and matches the description → the memo's narrow positioning is honest and defensible.

**CS recommendation:** before ANY external use of this memo (paper draft, audience pitch, funder-facing slide), the Bean et al. 2025 citation should be independently verified:
- arXiv 2511.04703 — confirm or deny
- "Measuring what Matters" title — confirm or deny
- 445-benchmark review claim — confirm or deny
- 42-author count — confirm or deny
- operational checklist for construct validity in LLM benchmarks — confirm or deny

If any of these is wrong, Senior should issue v0.2 with corrected citation analysis. If all confirm, the memo's positioning stands as written.

This flag does NOT block internal use of the memo for strategic discussion (the broader argument — that the field has done extensive construct-validity work and the program's defensible delta is operational enforcement — is consistent with what's verifiable). It only blocks external claims that depend on the specific Bean distinction.

## §8. Unsupported claim audit

CS examined for claims unsupported by either cited prior work or the program's own on-disk evidence:

| Claim location | Claim | CS read |
|---|---|---|
| §1 / §4 | "fail-closed OPERATIONAL ENFORCEMENT before stress-retention claims" is the program's plausibly distinctive contribution | Supported by program's own on-disk evidence (the failure→control history: parser bug caught, lever-validity failure caught, D4 PIVOT under pre-declared rule) |
| §9 / Audience 1 | "current evidence is one synthetic family" | Supported — CAL-A through CAL-Q all one family |
| §9 / Audience 2 | "the program has NEVER run [a certified baseline → stress rung]; this is the missing proof" | Supported by program's on-disk record (PROGRAM-MAP-v2.0 places this at Lane 4; never reached) |
| §12 | "NOT yet defensible as a PRODUCT (market unproven) or as a GENERAL method (one family)" | Supported — no market evidence on disk; only one family tested |
| §13 | "RECOMMENDED IMMEDIATE NEXT (model-free): the §11 rejection-audit control draft (unblocked, bounded), then a positioning section that nails the Bean-2025 distinction" | Recommendation, not claim. Caveat: the Bean-2025 positioning sub-recommendation depends on §7's load-bearing citation flag resolving |

No unsupported claims flagged. The Bean-2025-dependent recommendation in §13 inherits the §7 flag.

## §9. Disposition

**PARTIAL PASS.**

- Closed gates: PASS
- Standard forbidden phrasings: PASS (only present as labeled rejections in §11)
- Manager CAL-Q safe wording: PASS (appropriately paraphrased)
- Overlap-risk language: PASS (consistently scoped)
- Citation metadata: PARTIAL — well-known prior work (Geirhos, Jacobs & Wallach, Raji, ZeroQuant) places confidently; 2025-dated papers and specific arXiv IDs cannot be independently verified by CS
- Bean et al. 2025: **HIGH-PRIORITY CITATION VERIFICATION FLAG** — load-bearing for the entire positioning; must be independently verified before any external use

CS does NOT decide:
- Whether to proceed with the §13 recommended ordering (Senior + TL + Manager)
- Whether the Tier-1 paper direction is the right near-term focus (Manager already approved hybrid; this memo confirms within that approval)
- How to resolve the Bean-2025 citation flag (Senior to verify the citation; CS just flags the need)

## §10. Sealed bytes + language perimeter

Sealed bytes UNCHANGED (≈64th survival check). No model run. No certification. No compression. No INT4. No Claim C. CS does not draft, interpret, or position; CS verifies what Manager asked CS to verify.

— CS Engineer, 2026-06-13
