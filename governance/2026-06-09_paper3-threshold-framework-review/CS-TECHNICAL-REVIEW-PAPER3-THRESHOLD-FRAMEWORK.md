# CS Technical Review — Paper 3 Threshold Framework

**Date:** 2026-06-09
**From:** CS Engineer
**To:** Team Lead, Senior Engineer, Manager
**Re:** CS technical review of *Paper 3 — Threshold Framework (draft)*, Senior Engineer planning deliverable
**Filed per:** Team Lead directive, 2026-06-09

---

## Record status

```
Framework review filed.
Candidate selection not yet made.
No runs authorized.
```

---

## Review scope

This review covers the candidate-agnostic Paper 3 threshold framework as a planning artifact. It does not select a candidate, set threshold values, or authorize any run. The framework defines six certification dimensions (D1–D6) and their decision rules; this review assesses them from a CS implementation and sequencing standpoint.

No design objections. The framework is structurally sound. The findings below are sequencing constraints and implementation notes, not corrections.

---

## CS findings

**Finding 1 — D6 depends on B1 runner-provenance-backed artifacts.**

D6 requires that the candidate's runner-provenance fields are backed, not asserted-only. The B1 harness hardening is the mechanism that produces those fields: `model_snapshot_hash`, `mlx_lm_version`, `python_version`, `precision_rung`, and `stress_eligible`. Paper 3 certification cannot advance to D6 review until B1 is implemented.

**Finding 2 — Paper 3 certification cannot clear D6 until B1 is implemented.**

This creates the following lane dependency:

```
B1 can proceed as implementation planning / hardening.
Paper 3 framework can proceed as governance / planning.
Candidate certification cannot clear D6 until B1 harness provenance fields exist.
Execution remains blocked.
```

B1 itself is currently blocked pending Manager code-change authorization. The sequencing is: Manager authorizes B1 → B1 implemented → D6 review becomes possible → candidate certification can proceed (under separate authorization). No step in this chain is currently unblocked past the B1 authorization gate.

**Finding 3 — D2 shortcut-battery architecture is partially pre-built.**

The scorer already implements ceiling-bearing rank-C dummies (`first_C`, `second_C`, `third_C`, `last_C`) and the reference-only `always_return_ct`. For a single-hop candidate, the D2 shortcut battery (position/last-slot, salient-endpoint attraction, copy-completion, homogeneous-prefix degeneration) maps onto constructions the program has already instrumented. The candidate-selection memo will determine which carry over and which require new dummy definitions, but the scoring architecture is in place and the dummy policy is established.

**Finding 4 — D3 dual-scoring instrument already exists.**

The strict-vs-content strict-scoring stability check (D3) is the program's existing dual scorer: `strict_format_score` + `content_slot_score`, locked in PREREGISTRATION-EXP4. No new scorer development is required for D3. The D3 per-candidate fields (strict and content scoring definitions, admissible gap, scaffold held fixed) are filled at instantiation using existing instrumentation.

**Finding 5 — hop2 cannot inherit standalone provenance from Two-Hop L1 result files; if selected, it must be re-run under B1-standard provenance.**

hop2 from Cells01–03 was near-ceiling as an internal gate-discrimination dimension (24/24, 23/24, 23/24 across cells), but it was run as part of the two-hop construction, not as a standalone single-hop candidate. Its result files carry no standalone provenance and would fail D6 as-is. If hop2 is selected as the Paper 3 candidate, it must be re-run under B1-standard provenance. The historical result files are not reusable as Paper 3 certification evidence.

**Finding 6 — Locks 1 and 4 remain intact.**

Lock 1 (certification is not a seam claim, Claim C remains blocked) and Lock 4 (certification is not authorization to run any compression rung) are consistent with the program's standing constraints. No dimension in this framework creates a path around either lock.

**Finding 7 — Claim C remains blocked.**

No outcome of Paper 3 — including a positive certification finding — bears on whether a compositional seam exists or activates Claim C. Confirmed.

**Finding 8 — No runs are authorized by the framework.**

This document and the Paper 3 framework it reviews authorize nothing. Candidate certification requires a candidate-selection memo (selecting the target and rationale), a per-candidate threshold sheet (filling the D1–D6 fields with pre-registered values), and separate Manager authorization before any run. None of those steps have occurred.

---

## Non-authorizations (carried forward)

```
new runs · re-runs · INT8 / INT4 execution · multi-model execution
Fork A reactivation · Claim C activation · Paper 3 execution
Paper 6 activation · artifact mutation · public benchmark packaging
```

---

## Sequencing summary

| Lane | Current state |
|---|---|
| B1 harness implementation | BLOCKED — pending Manager code-change authorization |
| Paper 3 framework (planning / governance) | OPEN — this filing advances it |
| Paper 3 candidate selection | DEFERRED — awaiting candidate-selection memo |
| Paper 3 D6 clearance | BLOCKED — requires B1 implementation |
| Paper 3 certification execution | BLOCKED — requires D6 clearance + Manager authorization |
| Claim C / seam | BLOCKED — no change |

---

— CS Engineer, 2026-06-09
