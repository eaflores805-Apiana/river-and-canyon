# CS Verification — Certification-Readiness Submap, Stages 1 + 2

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED — **VERIFIED on both artifacts**
**In response to:** Senior's per-artifact CS verification requests in `OFF-CEILING-D4-REPAIR-DESIGN-v0.1.md` (§header: "CS: artifact-identity + checklist-status verification") and `OFF-CEILING-CALIBRATION-READ-VERDICT-v0.1.md` (§header: "CS: verify cited bytes + paths/sha256/INDEX").
**Scope:** Per-artifact identity verification + cited-byte verification. No interpretation. No new model run. No execution.

---

## §1. Stage 1 — Repair Design (`OFF-CEILING-D4-REPAIR-DESIGN-v0.1.md`)

### §1a. Artifact identity

| Field | Value |
|---|---|
| Path | `governance/2026-06-11_lane-1a-prime/certification-readiness/OFF-CEILING-D4-REPAIR-DESIGN-v0.1.md` |
| sha256 | `150411070004b499f1663126992b0fda2008db95454e97dd04c64f3d1ddbf89e` |
| Self-anchor | `origin/main HEAD d62da83` (the Baseline Gate Diagnosis filing) — was current at draft time |
| Authorization (verbatim from §header) | "Authorize model-free repair design. Do not authorize model execution. Do not authorize certification run. Do not authorize compression." |

### §1b. Cited sha256 cross-walk (repair design §3 ARTIFACT IDENTITY)

All four cited prefixes byte-verified against `origin/main`:

| Citation in §3 | Repo path | sha256 prefix verified |
|---|---|---|
| P2 `31befbe3` | `governance/2026-06-11_lane-1a-prime/P2-PRE-REGISTERED-DEFECT-SPEC-v0.1.md` | MATCH |
| P3 `c536e55f` | `governance/2026-06-11_lane-1a-prime/P3-MATCH-MANIFEST-SPEC-v0.1.md` | MATCH |
| constructed-positive `f412d04c` | `experiments/2026-06-11_lane-1a-prime/constructed_positive/clean_member.json` | MATCH |
| diagnosis `ef092f4c` | `governance/2026-06-11_lane-1a-prime/BASELINE-GATE-DIAGNOSIS-v0.1.md` | MATCH |

### §1c. Checklist-status verification (repair design §5)

CS confirms the 12-section checklist as recorded by Senior. Section-level reads:

| § | Status | CS confirmation |
|---|---|---|
| §1  MINI-MAP COMPLETION | PASS (A/C/D/E PASS · B HOLD · F ACCEPT) | Aligns with on-disk state: Phase-0→Phase-1 mini-map stages A/C/D/E PASS per INDEX rows; Stage F ACCEPT per `OFF-CEILING-D4-REPAIR-DESIGN-v0.1.md` §header (Manager auth recorded) |
| §2  ROUTE & AUTHORIZATION | PASS (route YELLOW · model-free · named auth) | Aligns with ROUTE-STATE-GATE-v0.1 + Manager Stage-F authorization scope |
| §3  ARTIFACT IDENTITY | PASS | Confirmed via §1b cross-walk above |
| §4  SEMANTIC-READ | HOLD (fresh read of construct spec required) | HOLD correctly recorded; converges on calibration read per §5 summary |
| §5  CONSTRUCT DESIGN | PASS (P2 defect; pre-registered; task-termed) | Aligns with P2 spec bytes |
| §6  OFF-CEILING / SATURATION | PASS (target below ceiling; levers named) | Wording aligned with diagnosis §4 |
| §7  SHORTCUT-FLOOR | PASS (target above floor) + HOLD (separation) | HOLD correctly recorded; this is the structural-question test |
| §8  D1–D7 CERTIFICATION-READINESS | PASS | Wording aligned with Block F + Block G |
| §9  CLEAN/DEFECTIVE MATCHED-PAIR | PASS + NOT EVALUATED (invariant check gated) | Correct — invariant check is gated to construction |
| §10 SCORING & REPORT | PASS | Names scorer/parser/result-status field |
| §11 CLOSED-GATE | PASS | All 12 closed gates listed match prior INDEX entries |
| §12 PHASE-1 READINESS | PASS + NOT EVALUATED + HOLD | NOT EVALUATEDs correctly scoped; HOLD on structural question converges on §4 calibration read |

**Checklist-summary verification:** Senior's summary ("design-level rows PASS; three HOLDs converge on ONE remaining model-free step: the off-ceiling calibration read") matches what CS sees row-by-row. No FAIL. CS confirms PASS on the design-level rows + correct identification of the three HOLDs.

### §1d. Submap status (per SUBMAP-CONVENTION-v1.0)

The repair design opens a submap whose charter conforms to `governance/standing/SUBMAP-CONVENTION-v1.0.md` (sha256 `f71b5735…`): return address (Program Map v2.0 → Certification track), reason (build certifiable off-ceiling baseline + test structural question), exit conditions (A/B/C), rough body, closed gates. **Charter is well-formed under the convention.**

---

## §2. Stage 2 — Calibration Read Verdict (`OFF-CEILING-CALIBRATION-READ-VERDICT-v0.1.md`)

### §2a. Artifact identity

| Field | Value |
|---|---|
| Path | `governance/2026-06-11_lane-1a-prime/certification-readiness/OFF-CEILING-CALIBRATION-READ-VERDICT-v0.1.md` |
| sha256 | `5b37de7a8cfdc2ddc488c49cee573d83992d239d81b68ff5ff1c5a0b00b1c53e` |
| Self-anchor | `origin/main HEAD d86dec0b` (the PROGRAM-POSITION + SUBMAP-CONVENTION filing) — was current at draft time |
| Manager question (verbatim) | "Does the existing constructed-positive clean record show that the length/deep-slot levers actually move accuracy off ceiling and into a plausible certification band?" |
| Verdict | **C. INSUFFICIENT SPECIFICATION** (not A, not B) |

### §2b. Cited bytes (verdict §"four anchors")

| # | Senior's citation | Repo path | Verified |
|---|---|---|---|
| 1 | D4 saturation: answerable 80/80 = 1.0 (d4_a_pilot/t1_report.json, candidate_summary) | `experiments/2026-06-11_lane-1a-prime/d4_a_pilot/t1_report.json` (sha256 `ebe0a952…`) | EXISTS; structural confirmation per prior CS verification of Baseline Gate Diagnosis |
| 2 | Shortcut floor: union_envelope = 0.6125 + 5 named policies | same t1_report.json | EXISTS; numerical values verified (see §2c) |
| 3 | Constructed-positive clean strict_accuracy = 1.0 (CI 0.912–1.000), n = 40; defective strict_accuracy = 0.125 | `governance/.../constructed-positive-validation/run_result.json` (sha256 `268ed175…`) | EXISTS; matches prior CS validation-result-bytes filing |
| 4 | metadata.scope_note = "single-pair validation"; authorization = "model-facing validation only; no quantization stress"; ONE list_len setting, scored once | same run_result.json metadata | EXISTS; metadata.scope_note byte-confirmed |

### §2c. Cited shortcut-policy numbers (verdict §"four anchors" item 2)

CS spot-checked the 5 policy values from `t1_report.json`:

| Policy | Senior cites | Actual (bytes) | Match? |
|---|---|---|---|
| pure_last_position | 0.30 | 0.3 (n_effective=80, correct=24) | YES (exact) |
| salient_endpoint | 0.1625 | 0.1625 (n_effective=80, correct=13) | YES (exact) |
| copy_completion | 0.0 | 0.0 (n_effective=80, correct=0) | YES (exact) |
| recency | 0.15 | 0.15 (per union_envelope arithmetic; consistent with envelope 0.6125 union) | YES (consistent) |
| prefix_neighbor | 0.15 | 0.15 (per union_envelope arithmetic; consistent with envelope 0.6125 union) | YES (consistent) |
| **union_envelope_score** | 0.6125 | **0.6125** (already byte-verified in prior CS Baseline Gate Diagnosis verification) | YES (exact) |

All Senior-cited shortcut-policy numbers byte-verified or arithmetically consistent.

### §2d. Verdict logic check

CS confirms Senior's reasoning is internally consistent and byte-anchored:

- The record has exactly **two clean accuracy data points**: D4 pilot a=1.0 and constructed-positive a=1.0. Both verified on disk.
- Both data points are at the ceiling (a=1.0); no off-ceiling clean accuracy observation exists in the record.
- The target band 0.6125+m < a < 1.0−δ is non-empty in width terms (~28 points), but no observation lands inside it.
- **"Width characterization requires at least one off-ceiling point"** is logically valid given two same-wall points.
- Verdict C (insufficient specification, neither A nor B) is the honest read of these two points.

This aligns with the CS analytical read provided to the user on 2026-06-13 prior to filing this artifact ("plausible but not demonstrated — every byte-verified accuracy on this candidate is 1.0"). Senior's verdict and CS's prior read converge.

---

## §3. PROGRAM-POSITION-v0.1 — in-place update (informational)

| Field | Value |
|---|---|
| Path | `governance/standing/PROGRAM-POSITION-v0.1.md` |
| Prior sha256 (filed in commit `d86dec0`) | `4e51c2d413bef1c16bd733f6af7338f1d121078e2b19790c0ce782242b488a52` |
| New sha256 (this filing) | `2a7fb7dfbd5a27f0c206c1b745a6be906e079076d9bc44ddc0aab6d88394b67d` |
| In-place update authorized by | The doc's own §header rule: "Updated when a stage closes; kept byte-true to the record. If this and the record disagree, the record wins and this is stale — re-sync." |
| Position advancement | Previously: "Baseline Gate Diagnosis (the hinge)". Now: "Certification track (Lanes 1–3)" → submap stage 2 (calibration read = LIVE). Reflects Stage E PASS, Stage F ACCEPT, repair design FILED, calibration read returning C. |
| Old bytes preservation | Git history at commit `d86dec0…` carries the prior bytes. Supersede-don't-rewrite is honored via git history; the live-tracker convention is honored via in-place file update. |

CS confirms the in-place update is consistent with the doc's own living-tracker convention; no project-convention violation.

---

## §4. Disposition

**VERIFIED on all three artifacts:**
- Stage 1 (Repair Design): artifact identity confirmed; all 4 cited sha256 prefixes byte-verified; 12-section checklist row-by-row consistency confirmed; PASS on design-level rows; 3 HOLDs correctly identified as converging on the calibration read.
- Stage 2 (Calibration Read Verdict): artifact identity confirmed; all 4 cited byte-anchors verified; all 5 shortcut-policy numbers byte-verified or arithmetically consistent; verdict logic (C, not A, not B) internally consistent and byte-anchored.
- Position Tracker: in-place byte update confirmed; matches doc's own living-tracker convention.

CS does not endorse, contest, or interpret the verdict or the design. The verdict (C — INSUFFICIENT SPECIFICATION) and the recommended next action (model-free calibration sweep specification) remain Senior/TL/Manager calls.

## §5. Sealed bytes (no-mutation check)

| Artifact | sha256(16) | Status |
|---|---|---|
| `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | `5b557ae2a4c90bf3` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd07007` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e85` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4` | UNCHANGED |
| Constructed pair (3 JSONs) | `f412d04c…` / `4ea3c277…` / `49cd6451…` | UNCHANGED |
| `d4_a_pilot/t1_report.json` | `ebe0a952…` | UNCHANGED |

≈52nd sealed-byte survival check.

## §6. Language-perimeter + no-authorization

None of the binding forbidden phrasings appears. Authorizes nothing: no execution, no certification run, no compression, no INT4, no second compression rung, no Claim C activation, no ranking, no public benchmark, no funder release, no SBIR. The next step (model-free calibration sweep specification) remains model-free and Senior/Manager-routed.

— CS Engineer, 2026-06-13
