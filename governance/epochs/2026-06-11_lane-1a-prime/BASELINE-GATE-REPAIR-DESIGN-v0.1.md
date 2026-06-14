# BASELINE-GATE-REPAIR-DESIGN-v0.1

**Version:** v0.1. River and Canyon program. Repair design for the one open edge of the accepted Baseline Gate Diagnosis (Stage E).
**Status:** MODEL-FREE DESIGN ONLY. Specifies a certification-targeted off-ceiling construct in the D4 key→value family. It authorizes no execution, runs nothing, and resolves nothing. It advances the structural-limit risk to the GREEN boundary; it does not cross it. Anchor: origin/main 9f0b358.
**Builds on (does not reopen):** `BASELINE-GATE-DIAGNOSIS-v0.1` (CS-verified, Manager-accepted, recorded Stage E PASS). That diagnosis stands unchanged: primary FIXABLE DESIGN/CALIBRATION, secondary VALID REJECTION, one narrow STRUCTURAL-LIMIT risk not yet ruled out. This artifact takes up only that open edge.
**Owner split:** Senior (drafter) → CS (verify cited evidence/paths/numbers + that nothing claims resolution or authorizes a run) → Team Lead (route + route-state review) → Manager (decides whether to authorize a future certification run on this design — a separate GREEN decision this artifact does not request).

---

## §0. The distinction this artifact holds (stated first, because it governs everything below)

```text
This repair design CAN advance the structural-limit risk model-free:
  it specifies the construct whose certification WOULD test whether a certifiable
  off-ceiling baseline exists in this family.
This repair design CANNOT resolve the structural-limit risk model-free:
  resolution requires putting the construct through full D1–D7 CERTIFICATION as a
  structure — a model-facing run — which is RED and requires a separate,
  future Manager-authorized GREEN decision.
The artifact ends at a ready-to-certify DESIGN. It does not contain, simulate,
predict, or smuggle the test result.
```

## §1. The exact open edge (from the accepted diagnosis, restated not reinterpreted)

The diagnosis established that baseline-gate failures split into two understood mechanisms — saturation (D4, fixable) and elimination (the sweep, valid rejection) — and that the constructed-positive is an existence proof that an off-ceiling construct in this family is buildable. The single thing it left open, verbatim in substance:

```text
The constructed-positive cleared VALIDATION (it discriminates a planted defect:
defective eliminated via strict_content_gap_instability; clean member spared) —
but its clean member scored strict_accuracy 1.0 (40/40). So it proved
DISCRIMINATION; it did NOT demonstrate a clean operating point BELOW ceiling with
measurable headroom, put through full D1–D7 CERTIFICATION as a structure.
THE RISK: the off-ceiling certification window — above the shortcut floor
(0.6125 + margin) and below the saturation ceiling (−δ) — may be NARROW: constructs
made hard enough to escape saturation may collapse toward the shortcut floor,
leaving too little room to certify a baseline. If so, the family has a structural
limit. Untested at the certification level.
```

The repair design's entire job: specify a construct engineered to land its **clean operating point strictly inside that window**, so that a future certification run would either certify it (window wide enough → fixable confirmed) or fail to (window too narrow → structural limit confirmed, a legitimate narrowed result). Whether such a construct is achievable is precisely the open question; this design does not assume it is.

## §2. Target operating window (the numbers, byte-anchored to the diagnosis evidence)

```text
From the D4 shortcut-envelope audit (d4_a_pilot t1 battery; cited in the diagnosis):
  shortcut-floor union = 0.6125    shortcut cap = 0.8    room above cap = 0.1875

The D1–D7 certifiable window for the clean operating point a_clean:
        SHORTCUT FLOOR + MARGIN  <  a_clean  <  SATURATION CEILING − δ
  i.e.        0.6125 + m         <  a_clean  <        1.0 − δ

  where:
    m = the discrimination margin a certified baseline must sit above the shortcut
        floor (so a shortcut policy cannot reach the construct's score). The margin
        is set in the threshold-sheet/lock step; this design treats m as a declared
        parameter to be fixed at lock, NOT chosen here to flatter the window.
    δ = the minimum measurable retention drop the substrate must leave headroom for
        (the D7 saturation guard: a_clean must be far enough below ceiling that a
        post-stress drop of at least δ is observable). δ is likewise a declared
        gate parameter, not tuned here.

The constructed-positive sat at a_clean = 1.0 — ABOVE the window (saturated on the
clean member). The repair target is to move a_clean DOWN into the open interval
WITHOUT (a) crossing below floor+m (which would make it shortcut-passable /
eliminated) or (b) introducing a construct defect (which would make it a CAL-Q-style
invalid construct the gate rightly rejects). That two-sided constraint IS the
structural question made concrete.
```

This design does **not** assert the interval is non-empty. It specifies a construct intended to occupy it and the levers to attempt that; the certification run is what would reveal whether the interval can actually be occupied.

## §3. Construction levers (only those proven in the constructed-positive result)

The constructed-positive cleared validation off-ceiling using two difficulty levers; the repair design uses the same proven levers, now aimed at lowering clean accuracy into the window rather than only at producing discrimination:

```text
LEVER 1 — list length.  Constructed-positive used list_len 9 (vs the saturated D4
  pilot). Longer lists raise lookup difficulty. Repair use: tune list_len upward
  to pull a_clean down from ceiling — but only until just above floor+m.
LEVER 2 — queried-slot depth.  Constructed-positive queried deep slots (6–8).
  Deeper positions are harder. Repair use: distribute queried depth to set a_clean
  inside the window.
These are the ONLY levers carried, because they are the only ones with an
existence-proof behind them (the constructed-positive cleared validation with
them). No new lever class is introduced here; introducing untested levers would
re-open the very space the diagnosis closed.

LEVERS EXPLICITLY NOT USED (they would change the question, not answer it):
  - query-side reformulation / code-book aliasing — this is the CAL-Q lever that
    collapsed abstention 0.92→0.00; it produces an INVALID construct, not an
    off-ceiling valid one. Excluded.
  - any defect-introducing manipulation — would make the gate's rejection correct
    (valid rejection), not a test of the window. Excluded.
```

The design's difficulty must come from *more of the same legitimate task* (longer lists, deeper slots), never from changing what the task measures. That is the line between "harder valid construct" (what we want to test) and "invalid construct" (what the gate already correctly rejects).

## §4. D1–D7 certification requirements the design must eventually face

This construct is being designed to face full certification *as a structure* — not the lighter validation the constructed-positive passed. The design must be specified to meet, and be readable against, each gate:

```text
D1  baseline correctness — clean member answers the intended lookup correctly at
    its operating point (correctness, not just non-defectiveness).
D2  scorer validity — strict vs concept scoring audited; the lowercase/uppercase
    "none" parsing issue seen in the constructed-positive defective member
    (n_strict 5 vs n_content 36) must be resolved by a pre-declared scorer, so
    a_clean is not a parser artifact.
D3  construct validity — the clean member measures key→value lookup, not a
    shortcut; abstention behavior on key-absent items stable (the CAL-Q failure
    must not recur).
D4  off-ceiling operating point — a_clean strictly inside §2's window. THIS is the
    gate the constructed-positive did not face (it was at 1.0). The crux gate.
D5  same-error identity — provisions for checking, under future stress, that
    surviving items are the same ones, not coincidental re-scores (carried from
    Paper 1 discipline; specified now, exercised only under a future run).
D6  provenance / artifact lock — construct, calibration set, scorer, thresholds
    hash-anchored before any run; semantic-reads attached (§5).
D7  saturation guard — a_clean leaves ≥ δ headroom below ceiling (the gate D4
    failed). Satisfied by construction if D4-window placement holds.
```

D4 (off-ceiling placement) and D7 (saturation headroom) are the pair the prior construct never satisfied; they are the heart of what this design targets and what a certification run would test.

## §5. Semantic-read requirements before any future execution

Per the Hash Integrity standing note and the North Star's nine-field shown-read gate, before this design could ever be run it must carry — and a future readiness packet must present — the following, with the mechanical-rendering floor (actual bytes read, not summarized) and an owner signature:

```text
- nine-field shown-read for the construct artifact (path / commit / sha256 /
  claimed concept = "off-ceiling certifiable D4 baseline" / check performed /
  observed structure / required structure / surplus check / disposition);
- a shown-read confirming the construct INSTANTIATES the off-ceiling-in-window
  concept it is named for (hash-valid ≠ concept-valid — the standing discipline);
- the scorer and threshold-sheet (with m and δ fixed) shown-read before lock.
An unsigned or rendering-floor-failing read is not a completed read; absent it,
the design is HOLD regardless of how good the construction looks.
```

## §6. What evidence would support the design as READY for certification testing

```text
READY (model-free bar — all must hold, all design-side, no run):
  1. a concrete construct spec (list_len, slot-depth distribution, item count)
     with a DESIGN-PREDICTED a_clean placed strictly inside §2's window, and the
     prediction's basis stated (the constructed-positive lever evidence), labeled
     PREDICTED-not-measured;
  2. m and δ fixed as declared parameters (not chosen to widen the window);
  3. the D2 scorer ambiguity (strict/concept "none") resolved by a pre-declared
     scorer, so a_clean cannot be a parsing artifact;
  4. the §5 semantic-reads attached and signed;
  5. a pre-registered three-outcome rule for the eventual run (certifies /
     fails-low = collapses toward floor / fails-high = stays saturated), declared
     BEFORE the run so the certification result cannot be re-narrated after.
"Ready" means ready to be PROPOSED for a GREEN certification decision — not
authorized. It is the model-free finish line.
```

## §7. What would force HOLD before any run

```text
HOLD (do not advance toward a run) if any of:
  - the design cannot specify a construct with a credibly in-window predicted
    a_clean using ONLY the proven levers (i.e. every in-window attempt either
    stays saturated or is predicted to fall toward the floor) — this is itself a
    NARROWED STRUCTURAL-LIMIT FINDING (model-free), and a legitimate result to
    report, NOT a failure to force through;
  - m or δ would have to be set unusually small purely to make the window appear
    non-empty (gaming the gate);
  - the only way to lower a_clean is a lever outside §3 (i.e. a construct change
    that risks invalidity) — excluded;
  - the semantic-reads cannot be completed or signed.
A HOLD here is informative: "the off-ceiling window may be too narrow even by
design" is the structural-limit risk realizing at the DESIGN stage, which sharply
redirects toward Tier 1 — and that is a valid, recordable outcome per the
diagnosis §8 pivot criteria.
```

## §8. The future GREEN route required to actually resolve the risk

```text
Resolution is NOT in this artifact. It requires, in order, each a separate gate:
  1. Manager authorizes a certification RUN on this design (GREEN execution
     decision — not requested here);
  2. CS executes the run on the certified, artifact-locked construct;
  3. the run is read against the pre-registered three-outcome rule (§6.5):
       - CERTIFIES in-window  → the off-ceiling window is occupiable; the
         structural-limit risk is RULED OUT for this family/scale (fixable
         confirmed); the certification track can proceed toward Lane 4.
       - FAILS-LOW (collapses toward floor) → the window is too narrow; STRUCTURAL
         LIMIT confirmed for this family/scale; pivot to Tier 1 is supported.
       - FAILS-HIGH (stays saturated) → the levers were insufficient; re-design,
         not a structural verdict.
Only step 3 resolves the risk. Until then the risk remains OPEN, exactly as the
accepted diagnosis records it. This design moves the program from "risk open,
no test designed" to "risk open, test designed and ready to propose" — which is
the most a model-free step can do.
```

## §9. What remains closed under this design (carried from the diagnosis; unchanged)

```text
- The accepted Baseline Gate Diagnosis is NOT reopened or reinterpreted.
- No claim that the structural-limit risk is resolved.
- No claim that a certifiable baseline exists (only that a construct is designed
  to test whether one can).
- No model execution. No certification evaluation. No certification run.
- No compression / INT8 / INT4. No second compression rung. No full ladder.
- No G6 implementation. No Paper B activation. No D4 reopening.
- No promotion of quarantined INT8-RUNG-1 evidence (excluded from this design as
  it was from the diagnosis).
- No analogy used as evidence; the construct is specified in model/task/artifact
  terms only.
- No new research claims. No public benchmark packaging, funder-facing release,
  or SBIR submission.
Route state: YELLOW (this design is model-free). Execution: RED (no run authorized).
```

This is model-free design only. It specifies the construct that would carry the structural-limit question up to the GREEN boundary — a certification-targeted, off-ceiling D4-family baseline aimed strictly inside the D1–D7 window, built on the constructed-positive's proven levers, with the certification requirements, semantic-reads, and pre-registered outcome rule it must satisfy. It advances the open edge; it does not resolve it. Resolution waits on a separate, future Manager-authorized GREEN certification run.

---

*BASELINE-GATE-REPAIR-DESIGN-v0.1 (TL ACTION; model-free design for the one open edge of the accepted Stage-E diagnosis): specifies a certification-targeted off-ceiling D4-family construct intended to place its CLEAN operating point strictly inside the D1–D7 window (above shortcut floor 0.6125+margin, below saturation ceiling−δ) — the placement the constructed-positive (clean member at 1.0, saturated) did not achieve. Uses ONLY the constructed-positive's proven levers (list length, queried-slot depth); explicitly excludes the CAL-Q query-side/aliasing lever and any defect-introducing manipulation. Defines the target window (byte-anchored: union 0.6125, cap 0.8), the D1–D7 requirements (D4 off-ceiling + D7 headroom are the crux the prior construct skipped), the nine-field semantic-read prerequisites, the model-free READY bar, the HOLD conditions (incl. "in-window construct not specifiable with proven levers" = a narrowed structural-limit finding), and the future GREEN route (Manager-authorized certification run with a pre-registered three-outcome rule) that alone resolves the risk. Holds the CAN-advance / CANNOT-resolve distinction throughout. Does not reopen or reinterpret the diagnosis; claims no resolution; authorizes nothing. model-free.*
