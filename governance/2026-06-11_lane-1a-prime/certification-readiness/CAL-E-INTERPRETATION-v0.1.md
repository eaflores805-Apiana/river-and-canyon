# CAL-E-INTERPRETATION-v0.1

**Version:** v0.1. River and Canyon program. Certification-readiness submap, stage 3-repair-interp (Senior interpretation of executed CAL-E).
**Status:** model-free interpretation of CS's executed CAL-E run (commit 8a64010, HEAD-verified). Authorizes nothing. Anchored on origin/main HEAD 8a64010.
Owner/drafter: Senior Engineer · CS: executed the run (verified) · Team Lead: Manager decision surface · Manager: PIVOT-WATCH vs NEEDS-REPAIR decision.

---

## 1. Byte verification (recomputed, not trusted from the report)

```text
HEAD 8a64010e551180114a138574cda57d466ea5bd32 — MATCH to CS-expected.
CAL-E  cal-e_run.json  sha 74c3fa1f ✓  clean 0.9750  defective 0.5750
       separation 0.4000  single_diff_ok=True
Runner-bug note acknowledged: run_cal_e.py re-executed the A/B/C sweep on import;
CS restored prior records via git checkout and added a __main__ guard
(run_calibration_sweep.py → 85856aba). Outputs deterministic; prior records
(CAL-A/B/C) re-verified unchanged. No data loss.
```

## 2. CAL-E missed all three targets

```text
                          target        actual    result
  clean accuracy          0.88–0.92     0.9750    ABOVE band (back at CAL-B level)
  defective accuracy      ≤ 0.10        0.5750    ~5.75× target
  clean − defective sep   ≳ 0.78        0.4000    collapsed (worst of all candidates)
```

## 3. I have to own this: CAL-E's design hypothesis was FALSIFIED

The CAL-E spec rested on an explicit, load-bearing claim I made:

```text
CLAIMED (CAL-E spec §4): "length and deep-slot position increase the lookup
  burden for the clean item … while giving the defective (key-absent) item no
  additional way to appear answerable — so clean drops without defective rising."
  I leaned on length+depth precisely because I hypothesized they were the
  NON-defective-inflating lever.
WHAT THE BYTES SAY: from CAL-C to CAL-E, near-miss was held CONSTANT at 4. The
  only changes were length (17→21) and depth (10–15→13–18). Defective MORE THAN
  DOUBLED (0.225→0.575). Length+depth ALONE inflated defective.
VERDICT ON THE HYPOTHESIS: FALSIFIED. Length and depth do NOT load clean and
  defective symmetrically. They inflate defective. The premise CAL-E was built on
  is wrong, and the run proved it.
```

This is the program's discipline working as intended: a pre-declared, mechanistic
design claim met a run that could refute it, and it did. The honest record is
that my mechanism reasoning was wrong, not that the result is disappointing.

## 4. What the four-candidate picture now shows

```text
  cand  len slots   nm  clean  def    sep
  CAL-A   9  6–8    0  1.000  0.125  0.875
  CAL-B  13  8–11   2  0.975  0.050  0.925   ← best separation
  CAL-C  17  10–15  4  0.950  0.225  0.725
  CAL-E  21  13–18  4  0.975  0.575  0.400   ← worst separation
TWO structural readings, both unfavorable to the current lever set:
  (a) CLEAN is non-monotonic in length: 1.000 → 0.975 → 0.950 → 0.975. The
      "smooth descent" of the first three points did NOT continue; CAL-E at
      len 21 scored the SAME as CAL-B at len 13. The lever is not a reliable
      clean-accuracy dial.
  (b) DEFECTIVE rises with difficulty (length/depth AND near-miss both inflate
      it): 0.125 → 0.050 → 0.225 → 0.575. Every step that made the task harder
      (past CAL-B) made the key-absent item look MORE answerable, not less.
SEPARATION — the instrument's whole point — is BEST at CAL-B (0.925, the
near-ceiling point) and DEGRADES as difficulty rises. The levers that move clean
off the ceiling are the SAME levers that destroy clean/defective separation.
```

## 5. Mechanism reading (hypothesis, explicitly not asserted as established)

```text
Why would longer/deeper lists inflate DEFECTIVE (key-absent) accuracy? Plausible
mechanism: in a key-absent item, the correct behavior is abstention. A longer
list with a deep interior query gives the model MORE candidate values to grab and
emit as a confident (wrong) answer instead of abstaining. More decoy material →
more confident false answers → defective "looks answerable" → defective accuracy
rises. If this is right, difficulty-via-list-content is intrinsically
defective-inflating in this task family, because the same content that loads
clean lookup also supplies the defective item with false-answer material.
This is a HYPOTHESIS for the decision surface, not a finding. It would need its
own controlled test (e.g. vary length at FIXED near-miss and FIXED depth, reading
defective abstention rate) to establish.
```

## 6. The verdict against the pre-declared rule

The CAL-E spec §10 pre-declared three outcomes. Mapping the bytes:

```text
BAND PLAUSIBLE:  NOT MET. Clean (0.975) is above the band, and separation (0.400)
  fails the discrimination requirement (≳0.78) badly.
NEEDS REPAIR:    MET on its face — "defective rises enough to erode clean/
  defective separation (near-miss inflation recurs)." CAL-E triggers this.
PIVOT WATCH:     ALSO IMPLICATED — "additional pressure CONSISTENTLY causes
  defective inflation … across attempts." We now have TWO consecutive harder
  candidates (CAL-C, CAL-E) where added difficulty inflated defective and
  degraded separation. That is the beginning of a consistent pattern.
```

**Senior reading: this is NEEDS REPAIR tipping into PIVOT WATCH — and the
decision between them is the Manager's, but I will give my honest assessment.**

```text
The single-attempt view says NEEDS REPAIR (try a different lever). But the
two-attempt pattern (CAL-C and CAL-E both inflating defective as difficulty rose,
at the cost of separation) is exactly the PIVOT-WATCH signal the Manager named.
The deeper problem the data is surfacing: in THIS task family, the levers that
push clean off the ceiling (length, depth, near-miss) appear to be the SAME
levers that inflate defective and collapse separation. If clean-off-ceiling and
defective-low cannot be achieved together, the family cannot host a clean
off-ceiling discriminator — which is the structural-limit reading.
```

## 7. What I am NOT claiming (epistemic guardrails)

```text
- I am NOT declaring the structural limit proven. Two harder candidates is a
  pattern, not a proof. There exists at least one untried lever class (below).
- I am NOT reverting to "the band is plausible." CAL-E refutes the edge-case
  optimism of the prior interpretation: pushing past CAL-C did not find a clean
  in-band point with separation — it found worse separation.
- I am NOT blaming the run or the harness. The harness is correct; the run is
  byte-verified; CAL-A/B/C reproduced. The design premise was wrong.
```

## 8. The honest options (for the Manager decision surface)

```text
OPTION 1 — ONE more lever class, then decide (bounded NEEDS REPAIR):
  Every candidate so far varied length/depth/near-miss — all CONTENT levers, all
  now implicated in defective inflation. The untried class is NON-content
  difficulty: e.g. hold list content fixed but make the QUERY harder (indirect
  key reference, two-step lookup) so the CLEAN item is harder WITHOUT adding
  decoy values that help the defective item. If a non-content lever can drop
  clean to ~0.90 while keeping defective low, the band is reachable after all.
  This is ONE more model-free spec + (gated) run. Bounded: if it also inflates
  defective, that closes the question.
OPTION 2 — PIVOT to Tier 1 now (accept the structural reading):
  Two consecutive attempts show content-difficulty inflates defective in this
  family. If the Manager judges the pattern sufficient, the honest move is to
  stop pushing this family for a stress-retention baseline and pivot to Tier 1
  eval-validity auditing (Layer 1), which the whole arc has independently shown
  is real and defensible. A negative result — "this task family cannot host a
  clean off-ceiling discriminator on content levers" — is a publishable finding.
RECOMMENDATION: Option 1, ONCE, as the decisive test — because it isolates the
  one lever class not yet implicated, and its result is dispositive either way.
  If a non-content lever also fails to separate, PIVOT (Option 2) becomes the
  clearly-supported conclusion rather than a two-point inference.
```

## 9. Submap status after this interpretation

```text
SUBMAP: Certification-readiness / off-ceiling repair design — STILL OPEN, now at
  a NEEDS-REPAIR / PIVOT-WATCH decision point.
  stage 3-repair-interp (this): CAL-E missed all targets; design hypothesis
    FALSIFIED (length+depth inflate defective); separation collapsed.
  → Manager decides: Option 1 (one non-content-lever attempt, bounded) OR
    Option 2 (pivot to Tier 1 now).
  exit (A) band plausible:  NOT MET (CAL-E refuted the edge-case optimism)
  exit (B) too narrow/pivot: APPROACHING — two-attempt defective-inflation pattern
  exit (C) needs repair:    MET — but the repair must change LEVER CLASS, not add pressure
```

## 10. What remains closed

```text
No certification run · No compression · No INT8/INT4 · No second compression rung
· No candidate certification · No ranking · No Claim C activation · No public
benchmark packaging · No funder-facing release · No SBIR submission. This
interpretation is model-free; any further candidate (Option 1) is a model-free
spec whose run is separately gated.
```

---

## Note on method

I designed CAL-E on a mechanistic claim — that length/depth are the
non-defective-inflating lever — and the run falsified it directly (defective
doubled at constant near-miss). The correct response is to record the
falsification plainly, not to re-describe the miss as partial success or to
quietly lower the separation bar. The four-candidate picture now says something
the single CAL-C reading could not: the content levers that move clean off the
ceiling are the same ones that destroy discrimination. That is a real finding,
and it points either to one specific untried lever class or to an honest pivot.

— Senior Engineer
