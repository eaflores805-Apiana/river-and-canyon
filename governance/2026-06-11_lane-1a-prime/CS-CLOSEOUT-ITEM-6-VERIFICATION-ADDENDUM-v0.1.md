# CS Addendum — Constructed-Positive Validation Closeout, Item 6 Reconciliation

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED (record-reconciliation addendum; awaits Senior confirmation of no interpretation change)
**In response to:** TL routing — "Closeout State Conflict; Item 6 Reconciliation Required" (2026-06-13), Option B
**Scope:** Record-state reconciliation only. No new model run, no compression rung, no INT8, no INT4, no Claim C activation, no result modification, no successor execution.

---

## §1. Referenced Senior document

| Field | Value |
|---|---|
| Title | `CONSTRUCTED-POSITIVE-VALIDATION-CLOSEOUT-v0.1.md` (Senior) |
| sha256 as named by TL routing | `5badf55b…` |
| Repo location | Not present in repo as of this addendum (workspace draft per TL routing context) |
| Item this addendum addresses | **Item 6 — `RESULT BYTES: NOT YET READABLE IN REPO`** |
| Other Senior items | Not addressed; this addendum is item-6-scoped only |

This addendum does not amend Senior's closeout v0.1. It records the present repo state for item 6 so Senior may issue v0.2 (or confirm no interpretation change) at Senior's discretion.

## §2. Why Senior's closeout v0.1 marked item 6 OPEN

Most-likely cause per TL routing: Senior drafted closeout v0.1 from a repo state that pre-dated CS's later result-byte filing commits. This is a governance-state mismatch only — not a validation failure and not a disagreement on result interpretation. CS independently reported earlier today that Senior's reported figures are byte-supported and the validation result remains PASS.

## §3. Repo state as of this addendum — item 6 is CLOSED

The validation result bytes ARE readable in the repo. Locations, sha256s, and the commits that filed them:

| Artifact | Path | sha256(64) | Size | Filing commit |
|---|---|---|---|---|
| Verdict | `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/run_result.json` | `268ed175db47b7949fae18889bf0700366bd0900ecec81bf60e5b8c8a3f9f2ac` | 6,570 B | `2b24375…` |
| Raw outputs — clean | `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/clean_outputs.json` | `abb887ad584101925a13e7e177114ac3c29b10f3b86b8d153f47a28ff9970708` | 16,339 B | `2b24375…` |
| Raw outputs — defective | `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/defective_outputs.json` | `ff2b35757d9f4536288dca59ab6bba07ad3d2482f1c2496bad44cd2eac631355` | 16,433 B | `2b24375…` |
| Per-item response table (derivative) | `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/PER-ITEM-RESPONSE-TABLE-v0.1.md` | `96a318cf1e7b4df041810403b29b6033b52b7969f087f6bef624f9c121949221` | (markdown) | `2b24375…` |
| Runner (OUTPUT_DIR retargeted) | `experiments/2026-06-11_lane-1a-prime/constructed_positive/run_validation.py` | `1de334ca1cff812dc454af693ba5c87d3945e53f0ffbb2590be346b96d67175f` | (Python) | `2b24375…` |
| CS filing return | `governance/2026-06-11_lane-1a-prime/CS-VALIDATION-RESULT-ARTIFACT-FILING-v0.1.md` | `a5ff6571f332189daacf6eca4595beb37d29491ebc24c62baa52ae9fdd113e38` | (markdown) | `2b24375…` |
| INDEX commit SHA fill | `governance/2026-06-11_lane-1a-prime/INDEX.md` | (updated) | — | `b289913…` |

INDEX rows for each of the above are present and visible at `governance/2026-06-11_lane-1a-prime/INDEX.md`. The corresponding "Last touched" footer in INDEX records the filing event.

## §4. Provenance of the result bytes (item-6 closure evidence)

The result bytes in §3 are byte-identical to the originals produced by the validation run that was executed earlier today. Specifically:

- **Producer:** `run_validation.py` at sha256 `d8c9dfe426f3475a…` (the OUTPUT_DIR-original version) — recorded in INDEX as SUPERSEDED-but-retained as the producer-of-record for these bytes.
- **Producer commit:** `5c3621b…` (initial validation run filing).
- **Move-only operation:** `git mv` of the three result JSONs from `experiments/2026-06-11_lane-1a-prime/constructed_positive/validation_run/` to `governance/2026-06-11_lane-1a-prime/constructed-positive-validation/` — verified by sha256 match between the originals from commit `5c3621b…` and the current files (sha256s in §3).
- **Filing commit:** `2b24375…` (governance-side filing of bytes + per-item derivative + filing return).
- **INDEX commit:** `b289913…` (commit-SHA fill for the §3 rows).

Both commits are on `main`.

## §5. Verdict bytes — what the filed `run_result.json` says

For Senior's convenience in producing v0.2 (Option A) if Senior wishes:

```text
overall_pattern:       "PASS"
clean_member.outcome:  "NOT_RULED_OUT"
clean_member.elimination_labels: []
defective_member.outcome: "eliminated"
defective_member.elimination_labels: ["strict_content_gap_instability"]
defective_member.criteria_outcomes.strict_content_gap_instability:
    status:              "FIRED"
    bound:               0.30
    comparison:          "nw_diff_ci_lower > bound"
    content_minus_strict: 0.7750
    nw_diff_ci_lower:     0.5864
    nw_diff_ci_upper:     0.8678
defective_member.criteria_outcomes.answerable_abstention_ceiling_exceeded:
    status:              "NOT_FIRED"
    bound:               0.20
    strict_abstention_ci_lower: 0.0546
    strict_abstention_rate:     0.1250
```

Per-item response table at sha256 `96a318cf…` documents the 31/5/4 split that drives GAP firing: 31 raw `none` (lowercase, content-correct / strict-broken) + 5 raw `NONE` (uppercase, strict-correct) + 4 single-letter hallucinations.

This is byte-identical to what CS already reported in `CS-CONSTRUCTED-POSITIVE-VALIDATION-RUN-RETURN-v0.1.md` (sha256 `1f8970605a829380…`).

## §6. No interpretation change asserted by this addendum

This addendum makes only one factual claim: as of repo state on `main` at INDEX update commit `b289913…`, item 6 of Senior's closeout v0.1 is closed by the byte-readability of the artifacts in §3.

This addendum:
- Does not amend Senior's closeout v0.1.
- Does not assert any change to Senior's interpretation of items 1–5 or 7+ of the closeout.
- Does not assert any change to the validation verdict (`PASS`), defective outcome (`eliminated`), clean outcome (`NOT_RULED_OUT`), or Layer-2 wording (`PRESENT for the constructed-positive condition class`).
- Does not authorize any compression rung, INT8 execution, INT4 execution, Claim C activation, or other successor work.

If Senior chooses Option A (file `CONSTRUCTED-POSITIVE-VALIDATION-CLOSEOUT-v0.2.md` updating item 6 to CLOSED with citations to §3 + §4 + §5), this addendum can be left in the record as the CS-side reconciliation co-sign and superseded by Senior's v0.2 record. If Senior chooses to confirm no interpretation change against this addendum without issuing v0.2, this addendum becomes the closure-of-record for item 6 only.

## §7. Required-final-state checklist (TL routing)

Per TL routing's required final state before the first compression rung:

| Required final-state line | Status per this addendum |
|---|---|
| Constructed-positive validation closeout: ACCEPTED / BYTE-VERIFIED | Item 6 byte-verified by this addendum; full closeout acceptance is Senior's to assert (this addendum only addresses item 6 of v0.1) |
| Item 6 result-byte status: **CLOSED** | **CLOSED** by commits `2b24375…` + `b289913…`; bytes at `governance/.../constructed-positive-validation/` |
| Validation result: PASS | PASS (per `run_result.json` `268ed175…`) — unchanged |
| Defective member: ELIMINATED | ELIMINATED (label `strict_content_gap_instability`) — unchanged |
| Clean member: NOT_RULED_OUT | NOT_RULED_OUT — unchanged |
| Layer-2: PRESENT for constructed-positive condition class | Senior interpretation per TL routing 2026-06-13; CS does not modify |
| Next eligible gate: first compression rung | Remains in Senior + Manager's hands; this addendum does not authorize any gate |

## §8. Sealed bytes (no-mutation check)

This addendum is record-reconciliation only and produces no run. Sealed bytes spot-checked at file time:

| Sealed artifact | sha256(16) | Status |
|---|---|---|
| `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | `5b557ae2a4c90bf3` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd07007` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e85` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4` | UNCHANGED |
| Constructed pair (3 JSONs) | `f412d04c…` / `4ea3c277…` / `49cd6451…` | UNCHANGED |
| Result bytes (3 JSONs) | `268ed175…` / `abb887ad…` / `ff2b3575…` | UNCHANGED (same bytes as commit `5c3621b…`; moved by `git mv`) |

≈46th sealed-byte survival check.

## §9. Language-perimeter self-check

None of the 22+ binding forbidden phrasings appears. Standing scope sentence carried: *"Breadth is untested under the current sealed schedule."* Path A (rung-uniform) is not invoked in this addendum.

## §10. Disposition

**Item 6 of `CONSTRUCTED-POSITIVE-VALIDATION-CLOSEOUT-v0.1.md` (Senior, sha256 `5badf55b…`) is closed by repo state at INDEX commit `b289913…`.** All byte anchors in §3 + §4 + §5 are independently verifiable from `main`. Awaiting Senior's choice of Option A (v0.2 supersession) or Option B confirmation (no interpretation change), per TL routing.

— CS Engineer, 2026-06-13
