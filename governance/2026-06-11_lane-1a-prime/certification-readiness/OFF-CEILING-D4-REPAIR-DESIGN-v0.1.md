# OFF-CEILING-D4-REPAIR-DESIGN-v0.1

**Version:** v0.1. River and Canyon program. Certification-readiness submap (opened on Manager Stage-F ACCEPT, scoped: model-free repair design only).
**Status:** model-free DESIGN. Specifies an off-ceiling D4 construct targeting the certification window; constructs, generates, runs, and certifies nothing. Authorizes nothing. Anchored on origin/main HEAD d62da83.
**Authorization (verbatim scope):** "Authorize model-free repair design. Do not authorize model execution. Do not authorize certification run. Do not authorize compression."
Owner/drafter: Senior Engineer · CS: artifact-identity + checklist-status verification · Team Lead: routing · Manager: any later certification-run authorization.

---

## Submap charter (per SUBMAP-CONVENTION-v1.0)

```text
SUBMAP: Certification-readiness / off-ceiling repair design
  Parent node:    Program Map v2.0 → Certification track (Lanes 1–3)
  Why:            build a certifiable off-ceiling D4 construct AND test the
                  open structural question (is the off-ceiling window wide
                  enough to certify?) from the Baseline Gate Diagnosis.
  Exit condition: (A) a repair design that places a construct in the window and
                      passes the 12-section checklist → a certification-run
                      request becomes well-formed (separate Manager auth); OR
                  (B) the window proves too narrow on paper → PIVOT to Tier 1; OR
                  (C) no construct placeable + no second family → STOP.
  Rough plan:     repair design (this artifact) → checklist PASS → (gated)
                  certification-run request.
  Touch / closed: model-free design only. No execution / INT4 / rung /
                  certification run / compression.
  Status: OPEN (this artifact is the first stage).
```

---

## 1. The target window (stated directly, per Manager requirement)

```text
        shortcut floor + margin  <  target accuracy  <  ceiling − delta
Concrete, from byte-read evidence (Baseline Gate Diagnosis, origin/main):
  shortcut floor  = union envelope 0.6125  (D4 t1 battery: pure_last_position
                    0.30, salient_endpoint 0.1625, recency 0.15,
                    prefix_neighbor 0.15, copy_completion 0.0)
  ceiling         = 1.0   (D4 saturated here — the failure to escape)
  margin (m)      = a resolvable separation above the floor (set at the gated
                    calibration step; design names it, does not fix a value)
  delta (δ)       = the retention drop of interest the rung must later resolve
                    (set at the gated step)
  TARGET BAND:    0.6125 + m  <  a  <  1.0 − δ
The design's entire job is to place a D4-family construct's clean-member
accuracy inside this band — above the shortcut floor with resolvable margin,
below the saturation ceiling with resolvable room.
```

## 2. The repair strategy (how it escapes both failure modes)

The Baseline Gate Diagnosis found two failure mechanisms. This design must escape both at once:

```text
ESCAPE SATURATION (the D4 failure): raise difficulty along the proven off-ceiling
  levers so the clean member lands below ceiling. Levers (from the constructed-
  positive, which cleared validation off-ceiling at list_len 9, slots 6–8):
    - list length: longer than the D4 pilot's 5 pairs;
    - queried-key position: biased to deep/interior slots;
    - (bounded) key-ambiguity, only if it does not approach the defect axis.
ESCAPE SHORTCUT ELIMINATION (the Lane-1a failure): keep the clean member's
  accuracy ABOVE the shortcut envelope by a resolvable margin, so no shortcut
  policy (last-position / salient-endpoint / recency / prefix-neighbor / copy)
  can account for the score. The construct must be solvable by genuine lookup
  and NOT by any enumerated shortcut.
THE TENSION (this is the structural question): raising difficulty pushes
  accuracy DOWN toward the shortcut floor; staying above the floor pushes it UP
  toward saturation. The design must show a band exists where both hold. If the
  levers cannot separate "hard enough to escape ceiling" from "still above the
  floor," the window is too narrow → exit (B).
```

## 3. The construct (design-level specification, no values fixed)

```text
TASK FAMILY: D4 key→value lookup (unchanged — depth before breadth).
CLEAN MEMBER: a lookup set calibrated to the §1 band —
  - list length raised from 5 toward the off-ceiling regime;
  - queried key present, uniquely answerable, biased to deep slots;
  - difficulty set so expected accuracy sits in 0.6125+m .. 1.0−δ (gated calibration).
DEFECTIVE MEMBER: identical construction except the single pre-registered defect
  (P2: queried key absent from pairs → value not constructible), surface still
  answerable-looking. Matched on all load-bearing dims (P3).
This reuses the P2 defect spec and P3 match manifest (existing instrument
components) — the repair is in the CALIBRATION (the off-ceiling band), not in
the defect or the matching.
```

## 4. The structural-question test (what this design resolves on paper)

```text
The design answers, model-free, BEFORE any run:
  Q: Does a calibration exist (on the named levers) that is expected to place the
     clean member in 0.6125+m < a < 1.0−δ?
  - If YES on paper (the levers can plausibly hit the band): the structural risk
    is NOT realized at the design level; a certification-run request becomes
    well-formed (exit A) — the run then EMPIRICALLY confirms or refutes.
  - If NO on paper (the levers cannot separate floor-escape from ceiling-escape):
    the window is too narrow; PIVOT to Tier 1 (exit B) — delivered for free,
    without a run.
This is the design's load-bearing contribution: it converts "is the window wide
enough?" from an unknown into a paper determination that EITHER licenses a gated
run OR forces a pivot.
```

## 5. The 12-section checklist (per REPAIR-DESIGN-CHECKLIST-INSTRUMENT-v0.1)

Status fields: PASS / FAIL / HOLD / NOT EVALUATED.

```text
§1  MINI-MAP COMPLETION
    A PASS · B HOLD · C PASS · D PASS · E PASS · F ACCEPT (this authorization) → PASS
§2  ROUTE & AUTHORIZATION
    route state declared: YELLOW (model-free) ......................... PASS
    step is model-free: design-only, no run .......................... PASS
    named-step authorization: Manager "authorize model-free repair design" PASS
    action not on closed-gate list: design-only permitted ............ PASS
§3  ARTIFACT IDENTITY
    inputs path/commit/sha256 anchored (P2 31befbe3, P3 c536e55f,
      constructed-positive f412d04c, diagnosis ef092f4c) ............. PASS
    bytes verify on clean fetch (origin/main d62da83) ................ PASS
§4  SEMANTIC-READ
    nine-field reads of load-bearing inputs ......................... HOLD (this design
      reuses already-read P2/P3/constructed-positive; fresh reads of THIS design's
      construct spec are required before any construction — owner-signed)
§5  CONSTRUCT DESIGN
    single permitted defect (P2 key-absence) ......................... PASS
    defect pre-registered + task-termed .............................. PASS
§6  OFF-CEILING / SATURATION
    target below ceiling (a < 1.0−δ) stated .......................... PASS
    difficulty levers named (length/position) ........................ PASS
    saturation = failed design, stated .............................. PASS
§7  SHORTCUT-FLOOR
    target above floor+margin (a > 0.6125+m) stated .................. PASS
    shortcut policies enumerated ..................................... PASS
    floor separated from window ...................................... HOLD (separation
      is the structural question; PASS on paper requires the §4 calibration read)
§8  D1–D7 CERTIFICATION-READINESS
    D1/D2/D7 prerequisites named ..................................... PASS
    window stated explicitly (§1) .................................... PASS
    certification ≠ validation (targets full D1–D7) .................. PASS
§9  CLEAN/DEFECTIVE MATCHED-PAIR
    matched on load-bearing dims (P3) ................................ PASS
    one permitted difference ......................................... PASS
    single-difference invariant (checked at construction, gated) ..... NOT EVALUATED
§10 SCORING & REPORT
    scorer/parser fixed; North Star §7 report form; result-status field PASS (design names them)
§11 CLOSED-GATE
    no execution / INT4 / rung / certification / compression ......... PASS (all closed)
§12 PHASE-1 READINESS
    certified off-ceiling baseline ................................... NOT EVALUATED (this design is the precursor)
    second defect class .............................................. NOT EVALUATED (Phase-1 scope)
    no quarantined dependence ........................................ PASS (no INT8 reliance)
    structural question addressed .................................... HOLD (this design addresses it; §4 read closes it)
```

```text
CHECKLIST SUMMARY: the design-level rows PASS. The three HOLDs (§4 fresh
semantic-read of the construct spec; §7 floor-separation; §12 structural
question) all converge on ONE remaining model-free step: the off-ceiling
calibration read that determines whether a band 0.6125+m < a < 1.0−δ is
plausibly reachable on the named levers. No FAIL. The NOT EVALUATED rows are
correctly out of scope (they need construction/a run/Phase-1).
```

## 6. Exact condition that would allow a later certification-run REQUEST

```text
A certification-run request becomes WELL-FORMED (still requiring separate Manager
authorization + route-state GREEN) when the three §5 HOLDs clear to PASS:
  - §4: owner-signed nine-field read of the construct spec;
  - §7: the calibration read shows floor-separation is achievable (band exists);
  - §12: the structural question is answered YES-on-paper.
At that point exit (A) is reached. This design does not grant the request; it
defines when it is well-formed.
```

## 7. Exact condition that would force repair / pivot / stop

```text
REPAIR (iterate this design) if: the calibration read shows the band is reachable
  only with a fragile margin — tighten the levers and re-read.
PIVOT to Tier 1 if: the calibration read shows NO band exists (floor-escape and
  ceiling-escape cannot be separated on the named levers) — the window is
  structurally too narrow; Tier 1 eval-validity auditing is the defensible
  product (exit B). Not a failure.
STOP / rescope if: no band on any lever AND no second task family available
  (exit C; the Stage Map §1c kill condition).
```

## 8. What remains closed

```text
No model execution · No INT4 · No second compression rung · No full ladder · No
candidate certification · No certification run · No compression · No ranking · No
Claim C activation · No public benchmark packaging · No funder-facing release ·
No SBIR submission. This design is model-free; the calibration read that closes
the §5 HOLDs is also model-free; the certification run that would empirically
confirm the band is separately gated and NOT authorized here.
```

---

## Submap close-out (partial — this artifact is stage 1 of the submap)

```text
CLOSE-OUT: Certification-readiness / off-ceiling repair design — PARTIAL
  Outcome:   repair design filed; design-level checklist PASS; 3 HOLDs converge
             on one model-free calibration read.
  Returns:   to the parent map — a repair design that, pending the calibration
             read, either licenses a gated certification-run request (A) or
             forces a Tier-1 pivot (B).
  Traces to: Program Map v2.0 → Certification track. Submap stays OPEN until the
             calibration read resolves the structural question.
```

— Senior Engineer
