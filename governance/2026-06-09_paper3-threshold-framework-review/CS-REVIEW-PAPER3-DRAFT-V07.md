# CS Technical Review — Paper 3 Draft v0.7

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Team Lead, Senior Engineer, Manager
**Re:** CS review of *Certification Before Retention* — Paper 3 draft v0.7
**Reviewed against:** v0.6 (last full CS review at `CS-REVIEW-PAPER3-DRAFT-V06.md`) and locked B1 v2 (merge `3cbfce5`, lock note `governance/2026-06-10_b1-harness-v2-merge-and-lock/B1-V2-LOCK-NOTE.md`)

---

## Record status

```
CS review filed.
v0.6 lock-blockers: remain resolved.
v0.7 is a substantial precision pass — tightens every gate, adds ~15 sheet fields.
B1-merge-vs-Paper-3-activation boundary explicitly reinforced.
One new minor spec/impl gap flagged (evidence_artifact_path field). Not blocking.
No candidate selected. No threshold values set. No runs authorized.
```

---

## Headline assessment

v0.7 is the kind of revision that pays off the first time a borderline case shows up. It promotes implicit conventions from v0.6 into explicit normative rules across every gate, adds a unified `## General decision rules` block in §5 (tie-equals-fail, voided-run handling, worst-case repeats, multi-role adjudication), and reinforces the lock-vs-activation boundary in bold:

> *"B1 merge locks infrastructure; B1 merge does not activate Paper 3."*

CS reads this as ready for the Team Lead readiness check. The new tightenings are well-targeted — they close ambiguities that would otherwise show up as governance friction at Paper 3 candidate authorization.

---

## Major v0.6 → v0.7 changes (named so they don't get missed)

| Surface | Substantive change |
|---|---|
| Status block | Now explicitly references B1 v2 active state and the lock-vs-activation distinction. |
| Framework version block | New constraint: *"threshold sheets lock only against a released framework version, not a draft identifier."* Explicit Manager C2 acknowledgment: B1 does not hardcode the manuscript version. |
| §1 | Inline citations to [3] and [4] added. [3] softened to "general decomposed-scoring discipline" (was "same separation principle") — partial address of my v0.6 wording question. |
| D1 | Tie-equals-fail rule cross-referenced to §5. |
| D2 | Explicit shortcut-prediction failure rule. New field: `D2_battery_code_hash` (battery itself is hashed and locked). Clean scoping: "D2 itself adjudicates through battery, not same-error identity alone." |
| D3 | New: strict-content gap distribution + confusion matrix archived. Stratum-level reporting (gap must pass in each declared stratum). |
| D4 | New: two-sided band (lower AND upper bound — prevents trivially-passing always-abstain or never-abstain). NULL classifier must be deterministic, versioned, hashed. |
| D5 | New: split into same-item-identity (manifest/item/prompt/scorer) vs. cross-candidate matching. |
| D6 | New: raw outputs retention required. Firewall scope refined (functional access triggers; admin reads don't). Timestamps must be UTC ISO-8601 AND harness-populated. |
| D7 | New: `D7_derivation_type` field. Deterministic vs. stochastic decoding noise source distinction. Inconclusive sensitivity fails closed. |
| §5 General decision rules (new block) | Tie-equals-fail; voided-run/missing-data rule; worst-case repeats; multi-role adjudication. |
| §5 closing | *"If no candidate passes the conjunction, the result is a mapped certification boundary, not evidence that the protocol is unusable."* Protects protocol value across negative runs. |
| §8 | Bold double-gate: B1 must supply provenance fields AND candidate must be Manager-authorized. *"B1 merge locks infrastructure; B1 merge does not activate Paper 3."* |
| Appendix A.1 | ~15 new threshold sheet fields. New statistical plan section (`statistical_plan`, `statistical_primary_test`, `statistical_CI_method`, `statistical_bootstrap_or_permutation_plan_if_applicable`, `minimum_N_rationale`). New env/decoding hashes (`decoding_settings_hash`, `container_or_environment_hash`, `dependency_manifest_ref`). Per-gate sub-fields expanded (D1 token-prior control; D2 battery code hash; D3 strict-content matrix + strata; D4 lower/upper band; D5 overlap metric; D7 derivation type). New: `baseline_repeat_count_and_aggregation_rule`. Renamed: `threshold_sheet_lock_timestamp` (was `threshold_sheet_timestamp`). |
| Appendix A.2 | Schema split: `evidence_artifact_path` (new) AND `evidence_artifact_hash`. Explicit short-circuit emission rule. |
| Threshold sheet hash spec | Now precise: SHA-256 over canonical JSON serialization with sorted keys, no whitespace. **Not** the hash of a Markdown rendering. |

---

## Consistency check with locked B1 v2

| Paper 3 v0.7 requirement | B1 v2 (merge `3cbfce5`) status |
|---|---|
| `framework_version` config-vs-sheet (no hardcoded literal) | ✓ Manager C2 satisfied; B1-T17 verifies with arbitrary version string |
| Harness-populated `first_candidate_data_access_timestamp` (UTC ISO-8601) | ✓ `now_utc_iso()` captured at manifest open |
| Threshold sheet content hash verified before content trust | ✓ Manager C3 satisfied; B1-T18 |
| Firewall: triggers on functional access (manifest open) | ✓ Implemented; B1-T21 (rejects prelock) / B1-T22 (passes postlock) |
| Threshold sheet content hash is over JSON, not Markdown | ✓ B1's `load_threshold_sheet` calls `json.loads`; canonical JSON expected |
| Per-item raw outputs retained | ✓ Per-item record carries `raw_output` |
| `framework_version` in every gate_record | ✓ `make_gate_record` propagates it |
| `threshold_sheet_hash` in every gate_record | ✓ `make_gate_record` propagates it |
| `analysis_script_hash` in every gate_record | ✓ `compute_analysis_script_hash` returns `sha256:in-runner` |
| `evidence_artifact_path` per gate_record | **Gap — see §"New spec/impl gap" below** |
| `D7_derivation_type` field | N/A — sheet-side; B1 reads from sheet |
| `D2_battery_code_hash` field | N/A — sheet-side; battery is candidate-specific |
| `baseline_repeat_count_and_aggregation_rule` | N/A — sheet-side; B1 reads from sheet |
| `decoding_settings_hash`, `container_or_environment_hash`, `dependency_manifest_ref` | N/A — sheet-side; B1 verifies against runtime where applicable |

Only one gap, flagged below.

---

## New spec/impl gap (minor, not blocking)

**v0.7 Appendix A.2 splits the evidence reference into two fields:**

```
evidence_artifact_path  # the specific table / JSON path / file that is the pass/fail evidence
evidence_artifact_hash  # hash of that artifact — NOT of the gate_summary file itself
```

B1 v2's `make_gate_record` produces `evidence_artifact_hash` but does not populate `evidence_artifact_path`. This is a small gap.

**Impact:** None at v0.7 readiness check. At Paper 3 candidate authorization, B1 will need a small addition (one parameter to `make_gate_record`; the gate-evaluation call sites pass the result-file path or JSON pointer).

**Not a Paper 3 lock blocker.** Flagged so the gap doesn't surprise anyone at Paper 3 candidate authorization. Suggest naming this "B1 v2.1 — gate_record evidence_artifact_path field" as a known follow-up; no work required until a Paper 3 candidate is authorized.

---

## Persisting items from v0.6 (still not blocking)

1. **D6 §5/§7 cross-references for historical-knowledge shading.** My soft note from v0.3 → v0.6 → v0.7 unchanged. Senior may have made a deliberate "see also" choice. Optional clarity item; not blocking.
2. **Reference [3] body still says "the same separation principle"** while §1 inline now says "general decomposed-scoring discipline." Senior softened the inline use (addressing my v0.6 question) but left the reference body. Minor inconsistency, possibly intentional preservation of canonical reference text. Not blocking.

---

## Open editorial item

- Formal NeurIPS proceedings pagination for [4]. Packaging detail; not in v0.7. Per Team Lead's prior summary, expected in a later patch or v0.8.

---

## CS-side transparency

v0.7 was reviewed in full per the paper-revision cadence rule. No visibility gap.

---

## CS recommendation

v0.7 is ready for Team Lead readiness check. The precision improvements address ambiguities I hadn't even named — the §5 general decision rules block in particular promotes implicit conventions into explicit normative rules, and the D4 two-sided band closes a real failure mode (degenerate-always-abstain or degenerate-never-abstain trivially passing the gate). The bold §8 lock-vs-activation statement is exactly the boundary CS wants reinforced.

The one spec/impl gap (`evidence_artifact_path`) is a B1 v2.1 follow-up item, not a Paper 3 lock issue.

---

## Summary for the Team Lead readiness check

| Surface | Status |
|---|---|
| v0.3/v0.6 CS lock blockers | All resolved (no regressions in v0.7) |
| Gate definitions (D1–D7) | Tightened across the board; well-targeted |
| §5 decision rules | New explicit block; promotes implicit → normative |
| Non-claims and locks | Unchanged; comprehensive |
| Appendix A.1 / A.2 / A.3 | A.1 substantially expanded (~15 new fields); A.2 schema split; A.3 unchanged |
| References [3] / [4] | Inline citations added in §1; [3] inline softened; reference bodies unchanged |
| Consistency with locked B1 v2 | Clean except one new minor gap (`evidence_artifact_path`); flagged as B1 v2.1 follow-up |
| Editorial pending | NeurIPS pagination for [4] — not blocking |
| Soft note | D6 §5/§7 cross-references still loose — not blocking |

**CS recommendation:** v0.7 is ready for Team Lead readiness check from a CS standpoint.

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
