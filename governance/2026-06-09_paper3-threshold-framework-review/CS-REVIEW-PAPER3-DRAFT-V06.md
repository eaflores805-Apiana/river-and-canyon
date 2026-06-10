# CS Technical Review — Paper 3 Draft v0.6

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Team Lead, Senior Engineer, Manager
**Re:** CS review of *Certification Before Retention* — Paper 3 draft v0.6 ("first real draft")
**Reviewed against:** v0.3 (last full CS review at `CS-REVIEW-PAPER3-DRAFT-V03.md`) and locked B1 v2 (merge `3cbfce5`, lock note `B1-V2-LOCK-NOTE.md`)

---

## Record status

```
CS review filed.
v0.3 lock-blockers: resolved in v0.6.
v0.6 spec is consistent with locked B1 v2 implementation.
No new findings that should hold Team Lead readiness check.
No candidate selected. No threshold values set. No runs authorized.
```

---

## v0.3 lock-blocker disposition

| Finding | v0.6 status |
|---|---|
| Framework version undeclared | **RESOLVED.** New header block: *"Framework version: `paper3-certification-protocol-v0.6` ... a threshold sheet locks against exactly one framework version."* |
| Immutability "automatically rejected" overclaim | **RESOLVED.** A.1 Immutability now Option A wording: *"Locked threshold sheets must not be overwritten. Any attempted overwrite must be treated as a governance violation, rejected by review, and recorded in the governance archive when detected."* Policy statement, not tooling claim. |
| B1 plan scope expansion (not a paper-side item) | **Addressed by B1 v2 implementation** (merged `3cbfce5`). Out of paper scope. |
| Soft note: D6 §5/§7 cross-references are loose | **Carry-forward.** Still present in v0.6; Senior may have made a deliberate "see also" call. Not blocking. |

---

## New in v0.6 — references [3] and [4] completed

Both citations are well-scoped. The discipline is consistent with the program's
boundary posture (no Claim C, no inherited stress-retention claims):

**[3] Baxi (CDCT, arXiv:2512.17920).** Cited as adjacent prior art for decomposed
scoring, with explicit scope constraint:

> "CDCT concerns prompt-compression / instruction-following evaluation and is not
> evidence regarding INT8/INT4 weight quantization, compression-retention measurement,
> same-error identity, or failure taxonomy under numerical stress."

The principle (separating constraint compliance from semantic accuracy) is borrowed;
CDCT's experimental scope is not. This keeps the Paper 3 contribution distinct and
does not implicitly extend the program's seam-claim boundary.

**[4] Dutta et al. (Accuracy is Not All You Need, NeurIPS 2024 / arXiv:2407.09141).**
Cited as adjacent compression-evaluation prior art, with explicit non-inheritance:

> "Dutta et al. do not propose retention certification, same-error identity reporting,
> or a fail-closed baseline-admission contract; those are contributions of this series,
> not claims inherited from [4]."

Adjacency-not-inheritance framing. Strong epistemic discipline.

Both references prevent over-borrowing; both clearly mark the program's contribution
relative to prior art.

---

## Consistency check against locked B1 v2

| Paper 3 v0.6 requirement | B1 v2 (merge `3cbfce5`) delivers |
|---|---|
| `framework_version` field per gate (Appendix A.2) | ✓ Config-driven runner; Manager C2 validation via `validate_framework_version_agreement` |
| `threshold_sheet_content_hash` integrity (Appendix A.1) | ✓ `load_threshold_sheet` verifies hash BEFORE `json.loads` per Manager C3 |
| Data-access firewall (D6, A.1) | ✓ `enforce_data_access_firewall` with `FIREWALL_VIOLATION_DATA_ACCESS_PRELOCK`; B1-T21/T22 |
| Per-item structural proxies (D5) | ✓ `structural_proxies.py` module, 11 model-free proxies, deterministic (B1-T24); per-item schema slot in runner |
| Same-error identity logging (D2, §8) | ✓ Per-item `same_error_identity_key` field; B1-T07 |
| B1 must provide D6 substrate (§8 list) | ✓ All §8 substrate items delivered in `runner_b1_v2.py` |
| Per-gate A.2 schema (13 fields) | ✓ `make_gate_record` produces all 13 fields; B1-T19 |
| Locked-artifact hash registry (D6) | ✓ `verify_locked_artifacts` at boot; B1-T23 |

No spec/implementation drift. v0.6's substrate requirements match what B1 v2
already delivers.

---

## Carry-forward soft note (not blocking)

**D6 cross-references to §5 and §7 are still loose.** The final sentence of D6 cites
the §5 evaluation order and the §7 expiration rules as supporting controls for
"historical-knowledge shading." Neither §5 nor §7 directly addresses shading; they
function as "see also" breadcrumbs rather than load-bearing controls. Three other
controls cited in the same sentence (pre-lock review, signoffs, role separation) are
real and load-bearing.

Senior didn't address this in v0.3 → v0.6, which CS reads as a deliberate "see also"
choice. Not a blocker for the readiness check. Optional clarity item if Senior wishes
to either tighten the §5/§7 sections with explicit shading language or trim the
breadcrumb.

---

## Open editorial items (CS no concern)

Per Team Lead's v0.6 diff-scope summary, one item remains:

- Formal NeurIPS proceedings pagination for [4]. Packaging detail, not substantive.

---

## v0.3 → v0.6 visibility gap (CS-side, transparent)

CS did not review v0.4 (which closed the framework-version and immutability
blockers) or v0.5 (reference completion) in full text. Per the paper-revision
cadence rule established 2026-06-10, CS should have asked to see v0.4 specifically
when those CS-flagged items were closing, instead of inferring the form of the fix
from Team Lead's diff-scope summary. Verified now via v0.6 — both fixes match what
was flagged; no quality issue. Noting the gap so the cadence rule doesn't repeat the
same omission on the next revision series.

---

## Summary for the Team Lead readiness check

| Surface | Status |
|---|---|
| v0.3 CS lock blockers | All resolved |
| Gate definitions (D1–D7) | Unchanged from v0.3; no concerns |
| Non-claims and locks | Unchanged; comprehensive |
| Appendix A.1 / A.2 / A.3 | Unchanged from v0.3 except governance-fields immutability wording (resolved) |
| References [3]/[4] | Completed with strong scope discipline |
| Consistency with locked B1 v2 | Clean — no spec/impl drift |
| Editorial pending | NeurIPS pagination for [4] — not blocking |
| Soft note | D6 §5/§7 cross-references still loose — not blocking |

**CS recommendation:** v0.6 is ready for the Team Lead readiness check from a CS
standpoint. No CS-side blockers remain. The two open items are an editorial detail
([4] pagination) and a clarity-only soft note (D6 cross-references).

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
