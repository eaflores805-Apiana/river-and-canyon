# CS Technical Review — Paper 3 Draft v0.3

**Date:** 2026-06-09
**From:** CS Engineer
**To:** Team Lead, Senior Engineer, Manager
**Re:** CS review of *Certification Before Retention* — Paper 3 draft v0.3
**Reviewed against:** `CS-REVIEW-PAPER3-DRAFT-V02.md` (this directory) and the underlying program constraints

---

## Record status

```
CS review filed.
No candidate selected. No threshold values set. No runs authorized.
```

---

## v0.2 finding disposition

| v0.2 finding | v0.3 disposition |
|---|---|
| §10 dead link in D7 footnote | RESOLVED — replaced with "stress-side validation concern outside the scope of this protocol and requires separate authorization" |
| Framework version undeclared | NOT ADDRESSED — see v0.3 carry-forward below |
| B1 plan undersized | NOT ADDRESSED (intentionally — not a Paper 3 lock condition); scope further expanded in v0.3 — see v0.3 finding 3 below |

**Bonus fix (not flagged in v0.2):** §4 intro cross-reference corrected from "(§6, Appendix A.1)" to "(§7, Appendix A.1)" — pre-registration material lives in §7. Clean.

---

## v0.3 Finding 1 (carry-forward) — Framework version still undeclared

**Source:** Appendix A.2 `framework_version` field; Appendix A.1 `framework_version` governance field.

The manuscript status line declares "draft v0.3" (a revision identifier for the manuscript itself), but no value is assigned to the `framework_version` field that every `gate_summary` record and every threshold sheet must populate. If Senior's intent is to assign the version string at final lock — and drafts are deliberately version-free — that policy should be stated explicitly in the manuscript. Otherwise the framework version is a real lock condition: a threshold sheet cannot be locked against an unnamed framework.

**Required resolution before lock:** Either (a) declare a draft framework version (e.g. `paper3-threshold-framework-v0.3-draft`), or (b) add a short note that `framework_version` is assigned at final lock and drafts do not populate it. Either resolves the question.

---

## v0.3 Finding 2 (new) — Immutability claim asserts an enforcement mechanism that does not yet exist

**Source:** Appendix A.1, Immutability clause.

**Text:** *"Any edit to a locked threshold sheet creates a new version with a new hash. Overwrites are prohibited; any attempt to overwrite a locked threshold sheet is automatically rejected and logged in governance."*

**Issue:** This is a claim about an enforcement mechanism. The current repository state has no such mechanism — git permits arbitrary file modification, there is no pre-commit hook checking threshold-sheet hashes against an archived registry, and there is no read-only protection on files in `governance/`. As stated, "automatically rejected and logged in governance" is aspirational rather than operational.

**Two ways to resolve:**

1. **Soften the language** to match current capability: *"Overwrites are prohibited as a matter of governance. Any detected overwrite invalidates the certification and must be recorded."* This is a policy statement, not an enforcement claim.

2. **Build the enforcement mechanism.** A practical implementation would be a pre-commit hook (or a governance check script) that maintains a registry of locked threshold-sheet hashes and rejects commits that change a registered file. This is CS-implementable but is a new deliverable: scope, code, registry format, and governance-archive integration all need to be defined.

**Recommended path:** Option 1 for the v0.3 → v1.0 lock pass, with option 2 deferred as a separate CS scoping memo when a candidate certification actually approaches. Building the enforcement mechanism in advance of any real threshold-sheet lock is premature.

This is a CS-side deliverable either way; flagged here so the choice is made deliberately.

---

## v0.3 Finding 3 (continuation of v0.2 finding 2) — B1 plan revision scope expanded

**Source:** §8 B1 deliverables list; Appendix A.1 `D7_baseline_noise_model_or_derivation_rule`.

v0.3 makes two changes that further expand the B1 revision scope beyond what was flagged in v0.2:

- **New B1 deliverable:** *"data-access timestamp capture sufficient to enforce the Appendix A.1 data-access firewall."* This is a behavioral requirement on the harness: the runner must record when it first reads candidate-evaluation data, distinguishable from when it reads configuration or documentation. Implementing this cleanly requires the harness to distinguish "candidate data" (per the v0.3 D6 definition) from other reads.
- **Field rename:** v0.2 `D7_baseline_noise_estimate` → v0.3 `D7_baseline_noise_model_or_derivation_rule`. More precise (allows either a stated noise model or a derivation rule like bootstrap from per-item logs) but means B1 must produce per-item logs adequate for either form, not just a summary estimate.

**Updated B1 revision scope (cumulative v0.2 + v0.3):**

| New requirement | Source |
|---|---|
| Per-gate `gate_summary` schema (A.2) | A.2 |
| `evidence_artifact_hash` per gate | A.2 |
| `short_circuit` boolean per gate | A.2 |
| `framework_version` per gate | A.2 |
| `threshold_sheet_hash` per gate | A.2 |
| `analysis_script_hash` as D6 provenance field | §4 D6, A.1 |
| `first_candidate_data_access_timestamp` | §4 D6, A.1 |
| Per-item outcome logs supporting `D7_baseline_noise_model_or_derivation_rule` | §4 D7, §8 |
| D2 per-item contingency tables | §8 |
| D5 structural-proxy computation from manifest JSON | §4 D5, §8 |
| **NEW v0.3:** Data-access timestamp capture sufficient to enforce A.1 firewall | §8 |

**Disposition:** Same as v0.2 — not a Paper 3 lock condition. When Manager authorizes B1, CS revises the B1 plan to absorb this full requirement set before writing any code.

---

## v0.3 Finding 4 (soft) — D6 cross-references to §5 and §7 are loose

**Source:** §4 D6, final sentence.

**Text:** *"Historical-knowledge shading is controlled by pre-lock threshold-sheet review, Manager/Senior/CS signoff, and role separation between threshold author, candidate constructor, and evaluator (Appendix A.1; see also the §5 evaluation order and the §7 expiration rules)."*

**Issue:** Three of the four controls cited are real and load-bearing: pre-lock review, signoffs, role separation. The fourth — the cross-reference to §5 and §7 — is loose. §5 covers gate evaluation order (D6 precheck first); §7 covers expiration on artifact changes. Neither section directly addresses historical-knowledge shading. A reader who follows the breadcrumb to §5 or §7 looking for shading-control text will not find it.

**Soft suggestion:** Either trim the cross-reference (the three listed controls are already sufficient), or add a short sentence in §5 and §7 explicitly linking each to historical-knowledge shading control. Not a blocker; clarity-only.

---

## v0.3 strengthenings (noted for completeness)

These are not findings — they are improvements I want to record so the v0.3 review has the same shape as the v0.2 review:

- **D6 "candidate data" definition.** Prevents false-positive firewall triggers by clarifying that historical/published information about the construction does not constitute "candidate data." This is a real protocol strengthening — without it, a strict reading of the firewall could disqualify any threshold-setter who had read prior work on the candidate.
- **D7 wording refinement.** "Baseline-noise estimate" → "baseline-noise model or derivation rule" is more precise; admits either a specified noise model or a derivation rule (e.g., bootstrap from per-item outcomes).
- **§6 stress-side preconditions made explicit.** v0.3 enumerates the stress-side preconditions in the section-level non-claim ("identical rung application, item-level same-error logging under stress, and a drop exceeding the pre-registered sensitivity floor"), matching the §3 phrasing. Consistency.
- **Role-separation hardening.** "Should not" → "must not, except by recorded Manager approval." Real tightening, CS-implementable through the A.1 signoff fields.
- **A.2 naming clarification.** The parenthetical noting that `threshold_sheet_hash` (A.2), `locked_threshold_sheet_hash` (A.3), and `threshold_sheet_content_hash` (A.1) denote the same value resolves a real naming ambiguity that could otherwise produce inconsistent records.

---

## Summary of required actions before lock

| # | Item | Owner | Blocking lock? |
|---|---|---|---|
| 1 | Resolve framework version question (declare or note "set at lock") | Senior | Yes — required by A.1 / A.2 schema |
| 2 | Decide A.1 immutability language: soften, or build enforcement | Senior (policy) / CS (build, if chosen) | Yes — current text claims a non-existent mechanism |
| 3 | Tighten or trim D6 cross-references to §5 and §7 | Senior | No — clarity only |
| 4 | Revise B1 plan to reflect full cumulative requirement set | CS (when B1 authorized) | No — B1 precedes any application, not Paper 3 lock |

---

## No design objections

The fail-closed conjunction, evaluation order (D6 precheck first), data-access firewall, candidate-data definition, role-separation hardening, negative-certification result form, and non-claims section are all consistent with program constraints. Locks 1 and 4 hold. Claim C remains blocked. The protocol is well-formed.

---

## Non-authorizations (carried forward)

```
new runs · re-runs · unconditioned-prior runs · activation logging runs
INT8 / INT4 execution · candidate selection · threshold values
Fork A reactivation · Claim C activation · Paper 3 execution
artifact mutation · public benchmark packaging
```

---

— CS Engineer, 2026-06-09
