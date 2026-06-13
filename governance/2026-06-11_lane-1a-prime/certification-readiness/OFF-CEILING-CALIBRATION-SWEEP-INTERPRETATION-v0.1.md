# OFF-CEILING-CALIBRATION-SWEEP-INTERPRETATION-v0.1

**Version:** v0.1. River and Canyon program. Certification-readiness submap, stage 3-interp (Senior interpretation of the executed sweep).
**Status:** model-free interpretation of CS's executed run (commit 7e1d4fd, HEAD-verified). Senior pre-declares m/δ on principled grounds and runs the pre-registered harness. Authorizes nothing. Anchored on origin/main HEAD 7e1d4fd.
Owner/drafter: Senior Engineer · CS: executed the run (verified) · Team Lead: Manager decision surface · Manager: cert-run-request decision.

---

## 1. Byte verification (recomputed, not trusted from the report)

```text
HEAD 7e1d4fd6742429ca32d12d97c7f3db4cd52f274f — MATCH to CS-expected.
CAL-A  cal-a_run.json  sha 5ceeeea4 ✓  clean 1.000  defective 0.125  single_diff_ok
CAL-B  cal-b_run.json  sha 814676cc ✓  clean 0.975  defective 0.050  single_diff_ok
CAL-C  cal-c_run.json  sha 50964a77 ✓  clean 0.950  defective 0.225  single_diff_ok
All three single-difference-OK. CAL-A reproduces the validated 1.0 (harness
consistent with prior runs).
```

## 2. The headline result (what changed from the prior reading)

```text
The off-ceiling levers WORK. Clean accuracy moved off the ceiling monotonically:
    CAL-A (len 9, no distractor)        1.000   ceiling (control, as expected)
    CAL-B (len 13, slots 8–11, 2 nm)    0.975   off ceiling by 0.025
    CAL-C (len 17, slots 10–15, 4 nm)   0.950   off ceiling by 0.050
CAL-B and CAL-C are the FIRST off-ceiling clean data points in the program's
entire record. The prior calibration read returned C precisely because no such
point existed; now two do. The length/deep-slot/near-miss levers demonstrably
depress clean accuracy below ceiling without collapsing it to the shortcut floor
(0.6125) — both points sit far above the floor.
```

## 3. Principled pre-declaration of m and δ (reasoned from meaning, BEFORE the verdict)

CS correctly did NOT pick δ. The protocol assigns it to Senior, pre-declared. I declare from what the parameters *mean*, not from which verdict they produce:

```text
m (margin above shortcut floor 0.6125):
  Purpose: a clean score must not be explainable by any shortcut policy. The
  separation should exceed sampling noise (1 item = 0.025 at n=40).
  DECLARE m = 0.05 (two items). floor+margin = 0.6625.
  All candidates (0.95–1.0) clear this by a wide margin → m is NOT the binding
  constraint; the verdict is not decided here.

δ (room below ceiling a LATER stress rung needs to show a measurable drop):
  Purpose: the headroom a future compression rung needs so a real retention
  decrease is distinguishable from sampling jitter. At n=40, 1 item = 0.025; a
  *meaningful* measurable drop should be at least ~2 items.
  DECLARE δ = 0.05. ceiling−δ = 0.95.
  I explicitly do NOT lower δ to 0.02 to pull CAL-C into the band: a δ below one
  item (0.025) would call a sub-noise drop "measurable," which is choosing the
  parameter to manufacture a PLAUSIBLE verdict — the exact failure this program
  forbids. δ is set on the noise floor, before seeing the result it yields.
```

## 4. The verdict (pre-registered harness, principled parameters)

```text
band: 0.6625 < clean_acc < 0.95   (m=0.05, δ=0.05)
  CAL-A 1.000 → at/above ceiling−δ
  CAL-B 0.975 → at/above ceiling−δ
  CAL-C 0.950 → exactly at ceiling−δ (excluded by strict <)
VERDICT (principled δ=0.05):  INSUFFICIENT / NEEDS REPAIR
```

## 5. The honest nuance — this is NOT the prior "saturated" INSUFFICIENT

The harness reason-string ("no candidate escaped the ceiling") fires on the
strict-`<` boundary, and I will not let that phrasing overstate the case:

```text
- The prior INSUFFICIENT (calibration read) meant: levers did not move accuracy
  off ceiling AT ALL (every point pinned at 1.0). That is NOT this situation.
- This INSUFFICIENT means: the levers DID move accuracy off ceiling (to 0.975,
  0.950), but the best off-ceiling point (CAL-C, 0.950) leaves headroom of
  exactly 0.05 — equal to the minimum resolvable δ — so there is no STRICT room
  beyond the minimum a later rung would need. It is a boundary result, not a
  saturation result.
```

δ-sensitivity, shown honestly (the verdict turns on δ ≈ 0.045):

```text
  δ ≥ 0.05   → INSUFFICIENT   (CAL-C at/above band top 0.95)
  δ = 0.04   → BAND PLAUSIBLE  (CAL-C 0.95 < band top 0.96)
  δ ≤ 0.04   → BAND PLAUSIBLE  (CAL-B and CAL-C both in band)
```

So at the principled noise-floor δ (0.05), the band is **not yet** demonstrated
with strict measurable headroom; a marginally smaller δ would flip it. The
honest reading is: **the band is essentially at the edge of resolvability at
n=40 — the levers reach its doorstep but do not yet clear it with room to spare.**

## 6. What this means (and does not)

```text
NOT "band too narrow" (no pivot): the levers demonstrably work and produce
  off-ceiling points well above the floor. "Too narrow" would require showing
  ceiling-escape forces floor-collapse; the opposite happened (0.95, 0.975 are
  nowhere near 0.6125). A Tier-1 pivot is NOT supported.
NOT "band plausible" at the principled δ: CAL-C's 0.05 headroom equals the
  minimum resolvable drop, leaving no strict room beyond the minimum. A
  certification-run request is NOT yet well-formed with strict measurable headroom.
THE ACTUAL FINDING: the band is at the edge of resolvability at n=40. One modest
  step would settle it — either push one candidate further off ceiling (a harder
  setting: longer list / deeper slots / more near-miss, landing ~0.88–0.92, which
  clears δ=0.05 strictly), OR increase n so the noise floor (and thus the
  principled δ) shrinks below 0.05 and CAL-C's existing 0.05 headroom becomes
  strictly resolvable.
```

## 7. Recommended next action (model-free)

```text
REPAIR via a SMALL targeted extension, not a pivot:
  Option 1 (harder setting): specify one additional candidate (CAL-E: len ~21,
    slots deeper, near-miss 5–6) expected to land clean ~0.88–0.92 — comfortably
    inside 0.6625 < a < 0.95 with strict headroom. One construct, one run.
  Option 2 (more power): re-run CAL-C at larger n (e.g. n=160) so the resolvable
    δ falls to ~0.0125 (1 item) and CAL-C's 0.05 headroom clears it strictly.
  Either resolves the boundary cleanly. Option 1 is the smaller lift and also
  strengthens the band's interior (a point at 0.90 plus CAL-B at 0.975 brackets
  a real interval). Recommend Option 1, with Option 2 as fallback.
This is a model-free specification step; any run is separately gated.
```

## 8. Defective-accuracy note (CS flagged; Senior interprets)

```text
Defective accuracy is non-monotonic: 0.125 (A) → 0.050 (B) → 0.225 (C). CAL-C's
higher defective rate plausibly reflects its stronger near-miss distractors:
near-miss values can occasionally make the defective (key-absent) item look
answerable, lifting defective "accuracy." This is a WATCH ITEM for the repair
step — if near-miss pressure inflates defective scores, the clean/defective
separation (the instrument's whole point) erodes. CAL-E (Option 1) should be
checked for clean-defective separation, not just clean off-ceiling placement.
This does not affect the band verdict (which is about CLEAN accuracy) but it
bears on whether a harder construct stays a valid discriminator.
```

## 9. Submap status after this interpretation

```text
SUBMAP: Certification-readiness / off-ceiling repair design — STILL OPEN.
  stage 3-interp (this): verdict INSUFFICIENT at principled δ=0.05, but
    "edge-of-resolvability," NOT saturation and NOT too-narrow.
  → next model-free stage: specify CAL-E (Option 1) [or n-increase (Option 2)].
  exit (A) band plausible → cert-run request well-formed:  NOT YET (edge case)
  exit (B) band too narrow → pivot:                        NOT MET (levers work)
  exit (C) insufficient → repair:                          THIS — small targeted extension
```

## 10. What remains closed

```text
No certification run · No compression · No INT8/INT4 · No second compression rung
· No candidate certification · No ranking · No Claim C activation · No public
benchmark packaging · No funder-facing release · No SBIR submission. This
interpretation is model-free; the recommended CAL-E specification is model-free;
its run is separately gated.
```

---

## Note on method

The verdict was δ-sensitive and CS handed the choice to Senior. The disciplined
move was to fix δ on the n=40 noise floor (0.05) BEFORE running the harness, and
to refuse the available smaller δ (0.02) that would have produced the more
satisfying PLAUSIBLE verdict. The result — INSUFFICIENT-but-at-the-edge — is less
clean than "plausible," and is the honest reading precisely because it was not
chosen to be satisfying. The band is real-adjacent; one small step settles it.

— Senior Engineer
