# BASELINE-GATE-DIAGNOSIS-v0.1

**Version:** v0.1. River and Canyon program. Stage E (the route hinge per PROGRAM-MAP-v2.0 / Stage Map v0.2).
**Status:** model-free diagnosis. Classifies why purpose-built baselines fail the FP16 gate, from the actual gate-failure record read from bytes (origin/main HEAD 6a4e604). Authorizes no execution.
Owner/drafter: Senior Engineer · CS: verify cited-evidence existence + paths/commits/sha256/INDEX · Team Lead: Manager decision surface · Manager: decides Phase 1 / repair / pivot.

## 1. Executive summary

The baseline gate failures are **not one phenomenon — they split into two distinct mechanisms, and the split is the whole answer.** Read from the run bytes:

```text
- The D4 family did NOT fail the gate's elimination criteria — its candidate
  scored 80/80 (accuracy 1.0) and was NOT_RULED_OUT at t3 with all six criteria
  PASSED. It failed a DIFFERENT gate: the D7 saturation guard (Block F), because
  at accuracy 1.0 there is no room below the ceiling for any retention drop δ.
  Failure mode: SATURATION — the construct is too easy to host a measurement.
- The Lane-1a sweep (L01–L08) failed the gate's elimination criteria: its locked
  outcome is "the certification window, while logically nonempty, was UNOCCUPIED
  for this task family at this scale — every rung carried at least one
  elimination label." Failure mode: ELIMINATION — constructs caught by the
  shortcut/floor criteria the gate is built to catch.
- The constructed-positive pair PASSED validation (defective eliminated, clean
  spared) precisely because it was engineered OFF-ceiling (list_len 9, deep
  queried slots 6–8) — the inverse of the D4 saturation.
```

**Diagnosis (headline):** the failures are predominantly **FIXABLE DESIGN / CALIBRATION** for the saturation arm (D4 saturated because the pilot settings were easy, and the constructed-positive proves an off-ceiling variant is buildable), and **VALID REJECTION** for the elimination arm (the sweep's eliminations are the gate correctly catching shortcut-prone constructs). There is a **STRUCTURAL-LIMIT risk that is not yet ruled out** and is the one thing to watch. It is **not** UNRESOLVED in the disqualifying sense — the blocker is narrowed to a specific, testable question (§7).

## 2. Evidence table (byte-read, origin/main 6a4e604)

```text
construct / run         | what the gate did                    | mechanism      | source bytes
------------------------|--------------------------------------|----------------|----------------------------------
D4-A pilot (t3)         | candidate 80/80 (acc 1.0),           | SATURATION     | d4_a_pilot/t3_report.json
                        |   NOT_RULED_OUT, all 6 criteria PASS |   (not elim)   |   candidate_outcome=NOT_RULED_OUT
D4-A / D4-B (Block F)   | DISPOSITION EMPTY: a<ceiling−δ       | SATURATION     | BLOCK-F-D1xD7-DESK-CHECK-v0.1
                        |   impossible at a=1.0; window closes |                |   (desk arithmetic on run bytes)
D4 shortcut envelope    | union 0.6125, cap 0.8, room 0.1875   | (floor healthy)| d4_a_pilot t1 battery audit
                        |   — floor is well-separated, fine    |                |
Lane-1a sweep L01–L08   | "certification window UNOCCUPIED for | ELIMINATION    | 2026-06-10_lane-1a-sweep/
                        |   this task family — every rung      |   (valid catch)|   fixed_outcome.md STATEMENT_A
                        |   carried ≥1 elimination label"      |                |   (locked outcome)
constructed-positive    | defective ELIMINATED (same          | PASS           | constructed-positive-validation/
  (FP16 validation)     |   criterion), clean 40/40 spared     |   (off-ceiling | run_result.json (byte-verified
                        |   — the gate FIRED correctly         |    by design)  |   in closeout v0.2)
constructed-positive    | clean list_len 9, queried slots 6–8  | (off-ceiling   | constructed_positive/
  design                |   — built to avoid D4 saturation     |   construction)|   clean_member.json
INT8-RUNG-1             | QUARANTINED — non-driving background | (excluded from | first-compression-rung/
                        |   only, per Manager classification   |  this diagnosis)|  (not official evidence)
```

## 3. Failure-class bins

```text
BIN 1 — SATURATION (too easy): D4 family.
  The candidate solves the task at 1.0, so there is no headroom for a retention
  drop. The gate (D7) correctly refuses to certify a substrate on which no
  downward measurement is interpretable. This is the gate working — but the
  CONSTRUCT is the problem, and it is fixable (make it harder without making it
  defective; the constructed-positive shows how).
BIN 2 — ELIMINATION (shortcut-prone / floor-colliding): Lane-1a sweep L01–L08.
  Every rung carried an elimination label under the pre-registered criteria.
  This is the gate correctly rejecting constructs that a shortcut policy could
  pass — VALID REJECTION, good metrology.
BIN 3 — PASS (off-ceiling, matched): the constructed-positive.
  The one construct deliberately built off-ceiling cleared validation. It is the
  existence proof that a usable construct in this family is buildable.
```

## 4. Diagnosis

```text
PRIMARY: FIXABLE DESIGN / CALIBRATION  (with a VALID-REJECTION component).
```

Reasoning, tied to the bins:

- The most prominent failure (D4, BIN 1) is **saturation, not a bad construct caught by the gate** — and saturation is the most fixable failure there is: lower the difficulty ceiling by lengthening lists / deepening positions, exactly the levers the constructed-positive used. The constructed-positive (BIN 3) is the existence proof that the fix works: it cleared the gate by being off-ceiling.
- The sweep failures (BIN 2) are **VALID REJECTION** — the gate catching shortcut-prone constructs is the gate doing its job, and counts as evidence the metrology discipline is sound, not evidence the family is broken.
- Therefore the gate is **not blocking usable measurement out of miscalibration** — it blocked D4 because D4 was too easy (fixable) and blocked the sweep rungs because they were shortcut-prone (correct). Neither is "the gate is wrong."

**The STRUCTURAL-LIMIT risk that remains (not ruled out):** the constructed-positive cleared *validation* (it discriminates a planted defect) but has **not** been put through the full **D1–D7 certification** as a structure, off-ceiling, at a measurable operating point. It is possible that the off-ceiling window (above the shortcut floor 0.6125+margin, below the saturation ceiling−δ) is **narrow** — that constructs hard enough to escape saturation tend to fall toward the shortcut floor, leaving little room in between. If that window proves too narrow to certify, the family has a structural limit. This is the one open question, and it is **narrow and testable** (§7) — which is why the overall diagnosis is FIXABLE-with-a-watch, not UNRESOLVED.

## 5. Required questions — answered

```text
1. Which gates keep failing?
   TWO different gates, not one: D7 saturation (D4) and the elimination criteria
   (sweep). They are distinct mechanisms; conflating them was the confusion.
2. Which task families/constructions failed?
   D4 key→value lookup (saturated); Lane-1a sweep rungs L01–L08 (eliminated).
   The constructed-positive (same lookup family, off-ceiling) passed validation.
3. Recurring the same way or changing form?
   Two stable forms: saturation (D4) and elimination (sweep). The constructed-
   positive shows the saturation form is escapable by design. The forms are not
   worsening; they are now understood and separable.
4. Do failures look like GOOD rejections of invalid constructs?
   The sweep eliminations: YES (valid rejection). The D4 saturation: it is a
   good rejection of an UNINTERPRETABLE substrate, but D4 is not "invalid" — it
   is too easy, which is a design problem, not a bad construct.
5. Fixable by design/calibration?
   YES for the saturation arm — demonstrated by the off-ceiling constructed
   positive. The lever is difficulty calibration (length/position) without
   crossing into defectiveness.
6. Structural limits in the current family?
   NOT RULED OUT, narrowed to one question: is the off-ceiling certification
   window (floor+margin < a < ceiling−δ) wide enough to certify a baseline? If
   the family collapses toward the shortcut floor when made hard enough to
   escape saturation, that is structural. Untested at the certification level.
7. Shortest path to a clean CERTIFIED baseline, if one exists?
   Take the off-ceiling constructed-positive design (proven to discriminate and
   to avoid saturation) and run it through the full D1–D7 certification as a
   structure — NOT just validation — at a calibrated off-ceiling operating point.
   That is the shortest path AND simultaneously the test of the §6 structural
   question. (Design/calibration is model-free; the certification run is gated.)
8. What would make Phase 1 readiness possible?
   A certified (not merely validated) off-ceiling baseline in this family, plus
   a second defect class beyond the single key-absence defect (Phase 1's
   multi-defect-class target). Readiness does not require the structural question
   fully closed first — it requires a credible repair design to test.
9. What would force a pivot to Tier 1 eval-validity auditing?
   If the off-ceiling certification window proves too narrow to certify ANY
   construct in this family — i.e. the §6 structural risk realizes — then
   stress-retention measurement (Tier 2) is blocked, and the program's defensible
   product is Tier 1 (eval-validity auditing) + the methodology layer, which the
   gate failures themselves demonstrate is real and valuable.
```

## 6. Recommended next action

```text
Authorize a model-free REPAIR DESIGN: a certification-targeted off-ceiling
construct for the D4 family, built on the constructed-positive's proven levers
(length/position calibration), specified to sit in the D1–D7 window
(floor+margin < a < ceiling−δ), with its semantic-reads. This design both (a) is
the shortest path to a certified baseline and (b) is the direct test of the
structural-limit question. It remains design-only; the certification run that
would resolve the structural question is separately gated.
Do NOT pivot yet: the evidence does not support a structural-limit conclusion —
it supports "fixable, with one narrow structural risk to test."
```

## 7. What would count as proof-of-life (per Stage Map §1c)

```text
EITHER: a model-free repair-design artifact that credibly places a D4-family
  construct in the D1–D7 off-ceiling window (a concrete, narrowed step toward a
  certifiable baseline — not "more governance"); OR
  a precise finding that the window is provably too narrow (a NARROWED structural
  blocker, which also counts as progress because it sharply redirects to Tier 1).
A generic "needs more work" answer does NOT count. This diagnosis itself narrows
the blocker from "baselines keep failing, unknown why" to "two known mechanisms;
saturation is fixable and proven escapable; one narrow structural question
remains — is the off-ceiling window wide enough to certify?"
```

## 8. What would count as pivot / stop

```text
PIVOT to Tier 1 if: a repair-design attempt shows the off-ceiling window in this
  family is too narrow to certify (constructs hard enough to escape saturation
  collapse toward the shortcut floor). Then the realistic product is eval-validity
  auditing + methodology, and that is a legitimate, defensible outcome — not a
  failure.
STOP / radically rescope if: repeated repair-design attempts cannot place ANY
  construct in the window AND no second task family is available — i.e. the
  measurement ladder cannot advance beyond the one constructed-positive condition
  class. Per Stage Map §1c, that is the kill condition; this diagnosis does NOT
  meet it (a repair path exists and is untested).
```

## 9. What remains closed

```text
No model execution · No INT4 · No second compression rung · No full ladder · No
Path B execution · No Path D execution · No schedule v2 supersession · No
candidate certification · No ranking · No Claim C activation · No public
benchmark packaging · No funder-facing release · No SBIR submission. This
diagnosis is model-free; the repair design it recommends is also model-free; the
certification run that would resolve the structural question is separately gated.
```

— Senior Engineer
