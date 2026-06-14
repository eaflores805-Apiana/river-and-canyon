# OFF-CEILING-CALIBRATION-READ-VERDICT-v0.1

**Version:** v0.1. River and Canyon program. Certification-readiness submap, stage 2 (the off-ceiling calibration read).
**Status:** model-free calibration read. Answers the Manager's narrow graded question from bytes. Authorizes nothing. Anchored on origin/main HEAD d86dec0b.
**Question (verbatim):** "Does the existing constructed-positive clean record show that the length/deep-slot levers actually move accuracy off ceiling and into a plausible certification band?"
Owner/drafter: Senior Engineer · CS: verify cited bytes + paths/sha256/INDEX · Team Lead: Manager decision surface · Manager: decides repair / pivot / well-formed cert-run request.

---

## VERDICT

```text
C. INSUFFICIENT SPECIFICATION
```

Not A (band plausible): no construct on record sits in the band — both data points are pinned at the ceiling.
Not B (band too narrow): we cannot show the band is *narrow*, because we have no data point off the ceiling at all. "Narrow" is itself an unsupported claim on this record.
**C is the honest verdict: the existing record does not contain the evidence needed to characterize the band, because the levers were never swept — only one off-ceiling setting was run, and it saturated.**

---

## The four anchors (byte-read, HEAD d86dec0b)

```text
1. D4 saturation:            answerable 80/80 = 1.0
                             (experiments/.../d4_a_pilot/t1_report.json, candidate_summary)
2. Shortcut floor:           union_envelope = 0.6125
                             (same t1_report; policies: pure_last_position 0.30,
                              salient_endpoint 0.1625, recency 0.15,
                              prefix_neighbor 0.15, copy_completion 0.0)
3. Constructed-positive clean: strict_accuracy = 1.0 (CI 0.912–1.000), n = 40
                             defective strict_accuracy = 0.125
                             (governance/.../constructed-positive-validation/run_result.json)
4. Record scope:             metadata.scope_note = "single-pair validation";
                             authorization = "model-facing validation only;
                             no quantization stress"; ONE list_len setting, scored once.
```

## Why C and not B (the decisive point)

```text
The target band is:   shortcut floor + margin  <  a  <  ceiling − δ
                      i.e.  0.6125 + margin  <  a  <  1.0 − δ
The record gives TWO clean accuracy points, and BOTH are on the upper wall:
    D4 pilot (5 pairs, shallow):       a = 1.0   ← ceiling
    constructed-positive (9, deep):    a = 1.0   ← ceiling
A band's WIDTH cannot be characterized from two points that lie on the same wall.
To call the band "too narrow" (B) you would need at least one off-ceiling point
showing accuracy landing near the floor when difficulty rises. To call it
"plausible" (A) you would need a point landing inside the band. The record has
NEITHER. It has no off-ceiling clean data point. Therefore the specification of
the band is INSUFFICIENT — not narrow, not plausible: uncharacterized.
```

## What the constructed-positive record IS and ISN'T

```text
IS:  a VALIDATION result. It shows the instrument DISCRIMINATES — clean 1.0 vs
     defective 0.125 is a clean firing, and it passed validation correctly.
     scope_note confirms: "single-pair validation."
ISN'T: a calibration sweep. It does not show where clean accuracy goes as
     length/depth increase, because only one setting was run. "Discriminates at
     one off-ceiling setting" and "sits in the certification band" are different
     properties; this record establishes the first, not the second.
KEY READING (the one that changes the answer): the length/deep-slot levers were
     NOT shown to move clean accuracy off ceiling. At list_len 9 with deep slots
     6–8, clean is still 1.0 (CI lower 0.912). The single jump from 5→9 pairs did
     not depress clean accuracy below the ceiling at all. So the levers, AT THE
     ONE SETTING TRIED, did not reach the band — and there is no second setting
     to establish a trend.
```

## Answer to the decision the Manager actually asked for

```text
"Is a later certification-run request well-formed on paper, or do we need to
 repair/pivot first?"
→ NOT well-formed on paper yet. A certification-run request requires a construct
  specified to land in 0.6125+margin < a < 1.0−δ. The record contains no such
  construct and no evidence the named levers can produce one. We need to REPAIR
  (a model-free calibration sweep) before a cert-run request is well-formed.
→ This is NOT yet a PIVOT trigger. Pivot (exit B) requires showing the band is
  too narrow; we have not shown that — we have shown the band is uncharacterized.
  Pivoting now would be as unsupported as running now.
```

## Recommended next action (model-free, no run)

```text
REPAIR via a model-free calibration SWEEP SPECIFICATION: specify a small set of
constructs across the difficulty levers (e.g. list_len 9 / 13 / 17+, varying
queried-slot depth and distractor structure) designed to find a setting where
clean accuracy is EXPECTED to land below 1.0 — ideally inside the band. This is
a design/specification artifact; it commits no run. It converts "is there a
band?" from unanswerable-on-this-record into a sweep whose later (separately
authorized) execution would answer it.
The calibration read CANNOT be closed to A or B from the existing record. It can
only be closed by a record that includes off-ceiling clean data points — which
requires the sweep to be specified now and (separately, later, gated) run.
```

## Submap status after this read

```text
SUBMAP: Certification-readiness / off-ceiling repair design — STILL OPEN.
  exit (A) band plausible → cert-run request well-formed:  NOT MET (no in-band point)
  exit (B) band too narrow → PIVOT to Tier 1:              NOT MET (band uncharacterized, not narrow)
  exit (C) no band + no second family → STOP:              NOT MET
  → The read returns C (insufficient specification). The submap does not close;
    it requires the calibration sweep specification as its next model-free stage.
```

## What remains closed

```text
No model execution · No certification run · No compression · No INT4 · No second
compression rung · No full ladder · No candidate certification · No ranking · No
Claim C activation · No public benchmark packaging · No funder-facing release ·
No SBIR submission. This verdict is model-free; the calibration sweep it
recommends is a specification (model-free); the sweep's execution is separately
gated and NOT authorized here.
```

---

## Note on method (the irony this program watches for)

Last turn, before reading the run_result bytes, the constructed-positive's "PASS"
looked like progress toward a band. Reading the actual number (clean still 1.0 at
the harder setting, single-pair scope) changed the verdict from an implied "band
looks reachable" to "band uncharacterized." This is exactly the failure the
program's discipline exists to catch — treating a validation PASS as
calibration evidence it is not. The verdict is anchored to bytes for that reason.

— Senior Engineer
