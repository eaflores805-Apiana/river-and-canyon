# CS Technical Review — Paper 3 Draft v0.2

**Date:** 2026-06-09
**From:** CS Engineer
**To:** Team Lead, Senior Engineer, Manager
**Re:** CS review of *Certification Before Retention* — Paper 3 draft v0.2
**Reviewed against:** `CS-TECHNICAL-REVIEW-PAPER3-THRESHOLD-FRAMEWORK.md` and
`CS-CLASSIFICATION-PAPER3-METROLOGY-SAFEGUARDS.md` (this directory)

---

## Record status

```
CS review filed.
No candidate selected. No threshold values set. No runs authorized.
```

---

## Prior CS classification consistency check

All four items from `CS-CLASSIFICATION-PAPER3-METROLOGY-SAFEGUARDS.md` are correctly
incorporated in v0.2:

| Item | My classification | Incorporation in v0.2 |
|---|---|---|
| D1 token-prior control | A — main framework | ✓ D1 requires token-prior / dummy-policy control; execution requires separate authorization |
| D3 tokenization-boundary guard | A — main framework | ✓ D3 explicitly requires tokenization-boundary check across declared permutations |
| D5 structural-only proxies | A — main framework + C (B1) | ✓ D5 explicitly bars model-accuracy-based proxies; structural proxies listed; B1 named as computation path in §8 |
| D6/activation telemetry | D — stress-side validation | ✓ D7 footnote correctly defers to stress-side; not a certification gate |

No design objections. The fail-closed conjunction, evaluation order (D6 precheck first),
data-access firewall, negative-certification result form, and non-claims section are all
consistent with program constraints. Locks 1 and 4 hold. Claim C remains blocked.

---

## Finding 1 — §10 forward reference is a dead link

**Location:** §4, D7 gate definition, parenthetical footnote.

**Text:** *"Activation-outlier telemetry — kurtosis, hidden-state outlier rates, residual-stream
peak-to-mean — is not a baseline-certification requirement and is not part of D6 or D7; it is
a stress-side concern noted in §10."*

**Issue:** The paper has no §10. Sections run §1–§9, then Appendix A. The reference destination
does not exist in v0.2.

**Required resolution before lock:** Either (a) add §10 covering stress-side validation
considerations including activation-outlier telemetry, or (b) change the reference to an existing
location or remove it. Resolution is Senior's call; this is a manuscript integrity issue, not a
CS implementation issue.

---

## Finding 2 — B1 plan is now undersized relative to Paper 3 requirements

**Source:** §4 (D5, D6, D7), §8, Appendix A.1 (threshold sheet fields), Appendix A.2
(gate_summary schema).

Paper 3 v0.2 introduces requirements that are not covered by the current B1 plan
(filed at `tier0-run/governance/2026-06-09_post-paper2-alignment/B1-IMPLEMENTATION-PLAN.md`).
The current plan specifies a `gate_summary` JSON block and `stress_eligible` boolean.
The new requirements are:

| New requirement | Source in Paper 3 | In current B1 plan? |
|---|---|---|
| Per-gate `gate_summary` schema with all A.2 fields | Appendix A.2 | Partial — block exists; per-gate schema not specified |
| `evidence_artifact_hash` per gate | A.2 | No |
| `short_circuit` boolean per gate | A.2 | No |
| `framework_version` per gate | A.2 | No |
| `threshold_sheet_hash` per gate | A.2 | No |
| `analysis_script_hash` (D6 provenance field) | §4 D6, A.1 | No |
| `first_candidate_data_access_timestamp` (D6 firewall) | §4 D6 firewall, A.1 | No |
| `baseline_noise_estimate` (D7 power calculation input) | §4 D7, §8 | No |
| D2 per-item contingency tables | §8 | No |
| D5 structural-proxy computation from manifest JSON | §4 D5, §8 | No — B1 plan predates D5 structural-only requirement |

**Impact:** The B1 plan needs a revision pass before implementation begins to absorb these
requirements. This is not a blocker on Paper 3 v0.2 review — the paper correctly treats B1 as
a precondition and does not set implementation details. But when B1 authorization is granted,
the implementation scope must match Paper 3's requirements, not the older plan.

**Action required:** When Manager authorizes B1, CS will revise the B1 plan to reflect these
fields before writing any code.

---

## Finding 3 — Framework version needs to be declared and archived

**Source:** Appendix A.2, `framework_version` field.

Every `gate_summary` record requires a `framework_version` field. The paper doesn't declare
what version string this draft constitutes, and no governance artifact currently tracks Paper 3
framework version history.

**Impact:** A threshold sheet cannot be locked against this framework until the version is
declared. If two threshold sheets were created against different framework drafts, there would
be no way to tell them apart from the `gate_summary` alone.

**Suggested resolution:**
- Declare this draft `paper3-threshold-framework-v0.2` (matching the manuscript status line).
- At final lock, assign a stable version string (e.g. `paper3-threshold-framework-v1.0`) and
  archive a hash of the locked framework document in governance.
- Resolution is Senior's call for the version naming; governance archiving is a CS deliverable
  at lock time.

---

## No-issue items (confirmed clean)

- **D7 (new gate):** The addition of D7 (retention-measurement sensitivity / power floor) is
  consistent with the program's lineage (near-ceiling sensitivity risk) and with the CS
  classification framework. D7 correctly scopes to detectability, not existence of a drop.
- **Evaluation order:** D6 precheck first is correct. Provenance failure should short-circuit
  before interpretive gates are evaluated.
- **Data-access firewall:** The automatic *not certified* consequence for any gate-computation
  or candidate-output inspection before threshold-sheet lock is a strong, CS-implementable
  rule. B1 records `first_candidate_data_access_timestamp` to enforce it.
- **Negative certification as result of record:** Consistent with Paper 2's framing.
  "Not certified" is a constructibility-boundary outcome, not a failed experiment.
- **Non-claims and locks:** Exhaustive and consistent. No path opened toward Claim C, no
  candidate selected, no run authorized.
- **References [3] and [4]:** Correctly marked as requiring bibliographic completion before
  external submission. No assertion made here.

---

## Summary of required actions before lock

| # | Item | Owner | Blocking lock? |
|---|---|---|---|
| 1 | Resolve §10 dead link in D7 footnote | Senior | Yes — manuscript integrity |
| 2 | Declare framework version string | Senior | Yes — required by A.2 schema |
| 3 | Revise B1 plan to reflect new Paper 3 requirements | CS (when B1 authorized) | No — B1 is a precondition, not a Paper 3 lock condition |

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
