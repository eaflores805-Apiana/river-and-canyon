# CS Technical Review — Paper 3 Draft v0.9

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Team Lead, Senior Engineer, Manager
**Re:** CS review of *Certification Before Retention* — Paper 3 draft v0.9
**Reviewed against:** v0.8 (last full CS review at `CS-REVIEW-PAPER3-DRAFT-V08.md`) and locked B1 v2 (merge `3cbfce5`)

---

## Record status

```
CS review filed.
v0.6 / v0.7 / v0.8 lock-blockers: all remain resolved.
v0.9 is a precision pass focused on §6 (interpretation rules rewritten),
A.1 (timestamp architectural fix), and A.2 (new firewall + D4 applicability
fields per gate).
My v0.6 wording question on reference [3] is fully resolved in v0.9.
Cumulative B1 v2.1 backlog now stands at 9 items — all deferrable; none
impact locked B1 v2.
CS recommendation: v0.9 ready for Team Lead readiness check.
No candidate selected. No threshold values set. No runs authorized.
```

---

## Headline assessment

v0.9 is a targeted precision pass. Three surfaces receive substantive work:

1. **§6 interpretation rules rewritten** to a four-category structure per gate
   (Success condition / Failure condition / Scientific interpretation /
   Explicit non-claim). This separates operational pass-fail from scientific
   inference and surfaces several non-claims that were implicit in v0.8.
2. **A.1 architectural fix** on the data-access timestamp problem. The actual
   timestamp can't exist at lock time, so v0.9 puts the *expected path* in the
   locked sheet; the actual timestamp lives in the evidence bundle.
3. **A.2 new fields** make the data-access firewall status and the D4
   applicability status explicit per gate record (both were implicit in v0.8).

Plus several smaller precisions (D2 anti-circular battery-sensitivity language,
D7 optional stratum saturation check, D1 undeclared-bias non-claim, §2 +
abstract acknowledging measurement requirements alongside lineage, independent
hash recomputation governance requirement).

**My v0.6 wording question on reference [3] is fully resolved in v0.9.** Both
the inline §1 use and the reference [3] body now read "decomposed-scoring
discipline" (was "the same separation principle" in v0.6–v0.8).

CS recommendation: ready for Team Lead readiness check.

---

## Major v0.8 → v0.9 changes

### §6 four-category interpretation rules

In v0.8 each gate had three short statements (Pass / Fail / Non-claim). In v0.9
each gate now has four labeled categories:

- *Success condition* — what passing means operationally
- *Failure condition* — what failing means operationally
- *Scientific interpretation* — what passing licenses in evidence/inference
- *Explicit non-claim* — what passing does NOT mean

This is a structural improvement. The four-category rewrite surfaces non-claims
that were implicit in v0.8:

- **D1.** Adds: *"...does not imply robustness to undeclared emission biases."*
- **D4.** Adds: *"a scoped-out D4 is not an actively tested NULL pass."* This
  closes a real ambiguity (v0.8 left scoped_out looking like a pass in
  gate_summary; the new A.2 `D4_applicability_status` field surfaces it
  explicitly).
- **D5.** Adds: *"does not establish end-to-end retention interpretability."*
  Strong boundary.
- **D7.** Failure conditions now enumerate every path: *"near-ceiling,
  underpowered, void-budget exceeded, or an inconclusive sensitivity
  calculation."*

### A.1 architectural fix: `first_candidate_data_access_timestamp_expected_path`

v0.8 listed `first_candidate_data_access_timestamp` as a threshold-sheet field.
But the actual timestamp can't exist at lock time — it comes after lock by
definition. Including it in the locked sheet would either prevent locking until
after the timestamp existed (impossible) or require updating the sheet after
creation (breaks immutability).

v0.9 fixes this cleanly: the threshold sheet records the *expected path* where
the access timestamp will be recorded; the actual timestamp lives in the
evidence bundle / `gate_summary`. New explanatory text:

> *"The threshold sheet records the lock timestamp and the expected location of
> the first-candidate-data-access record; the actual
> `first_candidate_data_access_timestamp` is harness-populated after lock and
> belongs to the evidence bundle / `gate_summary`, not to the locked
> threshold-sheet content hash."*

This separates pre-run commitments (locked, hashed) from post-run evidence
(harness-populated) cleanly. Sound architecture.

### A.2 new per-gate fields

v0.9 adds five new fields to `gate_summary`:

```
threshold_sheet_lock_timestamp
first_candidate_data_access_timestamp   # harness-populated after lock
data_access_firewall_status             # clear | violated
data_access_firewall_reason_code
D4_applicability_status                 # applicable | scoped_out
D4_scope_exclusion_reason
```

These surface what was previously implicit. The firewall status per gate makes
audit trivial; the D4 applicability fields end the ambiguity about whether a
scoped_out D4 is a pass or a non-evaluation.

### D2 anti-circular battery sensitivity (subtle but important)

v0.9 adds: *"Battery sensitivity is demonstrated against the pre-registered
deterministic shortcut implementations — dummy-policy outputs computed offline
— not inferred from the candidate's failure to exhibit the shortcut."*

This forecloses a circular validation path: you can't say "the battery is
sensitive because the candidate failed it" when the question is whether the
battery would catch the shortcut at all. v0.9 puts battery validation against
known shortcut outputs upstream of candidate evaluation. Subtle but important
precision.

### D7 optional stratum saturation check

v0.9 adds: *"The threshold sheet may additionally require per-item ceiling and
floor margins demonstrating that the baseline is not saturated at 0 or 1 on any
declared stratum."* Optional addition that closes a sub-loophole: aggregate
sensitivity might pass while individual strata are saturated.

### §2 + abstract alignment

v0.9 makes the gate motivation honest: *"motivated by the program's construction
lineage together with the measurement requirements that lineage exposed."*
This resolves an internal inconsistency in v0.8: Figure 2 caption said D1 and
D5 are measurement requirements (not single lineage artifacts), but the abstract
suggested all gates came from lineage. v0.9 aligns the two.

### A.1 independent hash recomputation requirement

New: *"The `threshold_sheet_content_hash` and the model-weight hash must be
independently recomputed by a second engineer, with both computation transcripts
archived under governance."*

Four-eyes review on the most load-bearing hashes. Governance process change,
not B1. Worth budgeting for when first candidate is authorized: someone other
than the threshold-sheet author must compute the hashes and archive the
transcripts.

### Reference [3] body wording resolved

| Version | Reference [3] body wording |
|---|---|
| v0.6–v0.8 | *"Paper 3 adapts the same separation principle to baseline certification..."* |
| v0.9 | *"Paper 3 adapts a related decomposed-scoring discipline to baseline certification..."* |

This fully addresses my v0.6 finding (carried through v0.7 and v0.8 as a
persisting soft note). Inline §1 and reference body now consistent.

### A.1 organization (pure cleanup)

Field list now grouped with labeled comments (`# — identity, environment,
instrument —`, etc.). No field changes; readability improvement.

### §5 worst-case repeats wording

Now explicitly: *"the pass/fail decision for every applicable gate uses the
worst-case result across repeats."* (Was implicitly so in v0.8.) Minor.

---

## Consistency check against locked B1 v2

All v0.9 surfaces compatible with B1 v2's current state. All new field
requirements deferrable to candidate authorization.

| v0.9 surface | B1 v2 status |
|---|---|
| `framework_version` config-vs-sheet | ✓ Manager C2; B1-T17 |
| Harness-populated access timestamp (now in gate_summary per v0.9) | ✓ captured; needs propagation to per-gate record at B1 v2.1 |
| Threshold sheet content hash verified before content trust | ✓ Manager C3; B1-T18 |
| Firewall: triggers on functional access | ✓ B1-T21/T22 |
| Output-free firewall exemption | ✓ Aligns with `verify_locked_artifacts` |
| `threshold_sheet_content_hash` over canonical JSON | ✓ `load_threshold_sheet` calls `json.loads` |
| Per-item raw outputs retained | ✓ Per-item record carries `raw_output` |
| `framework_version` / `threshold_sheet_hash` / `analysis_script_hash` per gate | ✓ propagated |
| `evidence_artifact_path` per gate (v0.7) | **B1 v2.1** |
| `decoding_settings_hash` per gate (v0.8) | **B1 v2.1** |
| Per-item decision log schema (v0.8) | **B1 v2.1** — analysis-script layer |
| `N_effective` + `max_voided_items` (v0.8) | **B1 v2.1** |
| Draft framework version naming check (v0.8) | **B1 v2.1** — depends on Senior naming convention |
| `threshold_sheet_lock_timestamp` per gate (v0.9 NEW) | **B1 v2.1** |
| `first_candidate_data_access_timestamp` per gate (v0.9 NEW) | **B1 v2.1** — currently in provenance; needs per-gate propagation |
| `data_access_firewall_status` + reason_code per gate (v0.9 NEW) | **B1 v2.1** |
| `D4_applicability_status` + scope_exclusion_reason per gate (v0.9 NEW) | **B1 v2.1** |

---

## B1 v2.1 cumulative backlog (9 items)

All deferrable to first Paper 3 candidate authorization. Suggest scoping as one
*"B1 v2.1 — Paper 3 substrate completion"* change rather than piecemeal:

| # | Item | Source |
|---|---|---|
| 1 | `evidence_artifact_path` per gate record | v0.7 A.2 |
| 2 | `decoding_settings_hash` per gate record | v0.8 A.2 |
| 3 | Per-item decision log schema (D1–D5 flags per item) | v0.8 A.2 |
| 4 | `N_effective` + `max_voided_items` enforcement | v0.8 D7 |
| 5 | Draft vs. released framework version naming check | v0.8 header |
| 6 | `threshold_sheet_lock_timestamp` per gate record | v0.9 A.2 |
| 7 | `first_candidate_data_access_timestamp` per gate record | v0.9 A.2 |
| 8 | `data_access_firewall_status` + reason_code per gate | v0.9 A.2 |
| 9 | `D4_applicability_status` + scope_exclusion_reason per gate | v0.9 A.2 |

Estimated effort: ~half-day for items 1, 2, 6, 7, 8, 9 (one-to-three-line
additions to `make_gate_record`); ~one-to-two-day for items 3 and 4 (gate
evaluation logic + analysis-script layer); item 5 depends on Senior's release
naming convention. No work begins until first Paper 3 candidate is authorized.

---

## Persisting items

**Only one remaining:** D6 §5/§7 cross-references for historical-knowledge
shading. Soft note from v0.3 → v0.9 unchanged. Senior's call. Not blocking.

(The reference [3] wording inconsistency from v0.6 is **resolved** in v0.9 — see
above.)

---

## CS-side transparency

v0.9 was reviewed in full per the paper-revision cadence rule. No visibility gap.

---

## Summary table

| Surface | Status |
|---|---|
| v0.3 / v0.6 / v0.7 / v0.8 CS lock blockers | All resolved; no regressions |
| §6 interpretation rules | Rewritten to four-category structure; non-claims tightened |
| A.1 timestamp architecture | Fixed (expected path in sheet; actual timestamp in evidence) |
| A.2 new per-gate fields (firewall status, D4 applicability) | Add; surface what was implicit |
| D2 anti-circular battery sensitivity | Added |
| D7 optional stratum saturation check | Added |
| §2 + abstract lineage/measurement alignment | Fixed |
| Independent hash recomputation | Added (governance) |
| Reference [3] body wording | Resolved (v0.6 finding closed) |
| A.1 field organization | Improved (labeled comments) |
| Consistency with locked B1 v2 | Clean; 9 B1 v2.1 follow-ups in backlog |
| Persisting soft notes | D6 §5/§7 cross-references only |

**CS recommendation:** v0.9 is ready for Team Lead readiness check from a CS
standpoint.

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
