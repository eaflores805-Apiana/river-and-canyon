# NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1

**Version:** v0.1. River and Canyon program. Certification-readiness submap, stage 3-rescue (final bounded D4 rescue attempt).
**Status:** model-free SPECIFICATION of one non-content-lever candidate. Specifies; runs nothing; requests nothing. This is the FINAL D4 rescue attempt unless the result cleanly identifies a new specific non-handwavy repair. Anchored on origin/main HEAD 8a64010.
**Authorization:** "one final bounded model-free repair attempt, and only because it changes lever class." Non-content difficulty only.
Owner/drafter: Senior Engineer · CS: verify model-free + that the lever changes only query-side difficulty (content/decoy unchanged, defective answerability not increased) · Team Lead: routing · Manager: any later run authorization + the pivot decision.

---

## 1. Executive summary

CAL-E falsified the hypothesis that content levers (length/depth) could lower clean accuracy without inflating defective. At constant near-miss, length+depth alone more than doubled defective (0.225→0.575) and collapsed separation to 0.400. Every content lever is now implicated. This spec proposes the one untried lever class — **non-content difficulty via an indirect-key query** — that makes the *clean* lookup harder by adding a query-side resolution step, **while leaving the list content (and thus the defective/key-absent item's decoy material) completely unchanged.** The design's load-bearing claim is that an indirect query pressures clean without giving the key-absent item any new false-answer material — the exact failure mode CAL-E revealed. Candidate ID: **CAL-Q** (Q for query-side).

## 2. CAL-E falsification summary (byte-read, HEAD 8a64010)

```text
  cand  len slots   nm  clean  def    sep
  CAL-A   9  6–8    0  1.000  0.125  0.875
  CAL-B  13  8–11   2  0.975  0.050  0.925
  CAL-C  17  10–15  4  0.950  0.225  0.725
  CAL-E  21  13–18  4  0.975  0.575  0.400
CAL-C → CAL-E: near-miss held CONSTANT at 4; only length (17→21) and depth
changed; defective MORE THAN DOUBLED (0.225→0.575). Length+depth are NOT the
non-defective-inflating lever I claimed — they inflate defective. Separation is
best at the near-ceiling point (CAL-B 0.925) and degrades as content difficulty
rises.
```

## 3. Why content levers are now blocked

```text
The mechanism the data supports: in a key-ABSENT (defective) item, correct
behavior is abstention. Content difficulty — longer lists, deeper slots, more
near-miss values — works by adding MORE list material. But more list material is
exactly MORE DECOY for the key-absent item: more candidate values to grab and
emit as a confident wrong answer instead of abstaining. So every content lever
that loads clean lookup ALSO supplies the defective item with false-answer
material → defective inflates → separation collapses. Content difficulty is
intrinsically defective-inflating in this task family. It is blocked.
```

## 4. Proposed non-content lever (CAL-Q)

```text
LEVER: indirect-key query. Instead of querying the key DIRECTLY
  ("what is the value for key K?"), query it INDIRECTLY via a description that
  uniquely identifies K from the SAME list, with NO change to list content:
    e.g. "what is the value for the key that comes immediately after key J?"
         "what is the value for the alphabetically-last key?"
         "what is the value for the key whose value is the longest?" (value-side
            constraint, still resolving to one existing key)
HELD FIXED (this is the whole point):
  - list length:        UNCHANGED from a low-inflation baseline (CAL-B's len 13)
  - queried-slot depth: UNCHANGED
  - near-miss count:    UNCHANGED (CAL-B's 2, the low-defective setting)
  - list content / vocabulary / values: IDENTICAL — no new decoy material
ONLY the QUERY FORM changes: direct → indirect. The clean item must now perform
an extra resolution step (identify which key the description picks out, THEN look
up its value). The defective item's list is identical; no decoy is added.
BASELINE CHOICE: CAL-Q is built on CAL-B's content settings (len 13, slots 8–11,
near-miss 2) — the setting with the BEST separation (0.925) and LOW defective
(0.050) — and adds ONLY the query-side step. This isolates the non-content lever.
```

## 5. How the lever pressures clean accuracy

```text
The clean item, previously a one-step lookup (find K → read value), becomes a
two-step task (resolve the description → find the identified key → read value).
The extra resolution step is genuine difficulty that depresses clean accuracy
WITHOUT adding list material. Expected effect: clean drops from CAL-B's 0.975
toward the band (target 0.88–0.92) purely from the added query-side step.
This is difficulty that lives in the QUESTION, not the LIST.
```

## 6. Why it should NOT inflate defective accuracy

```text
This is the load-bearing argument and the reason the lever is authorized:
  - The defective item is key-ABSENT: the queried key (however specified) is not
    in the list, so its value is not constructible; correct behavior = abstain.
  - An INDIRECT query that resolves to an absent key gives the defective item NO
    new answer material: the list content is identical to the low-defective
    CAL-B baseline (near-miss 2), so there is no MORE decoy than the setting that
    produced defective 0.050.
  - The indirect step, if anything, makes false-answering HARDER for the
    defective item: to emit a confident wrong answer, the model must both
    mis-resolve the description AND grab a decoy value — a higher bar than direct
    decoy-grabbing.
DESIGN REJECTION CLAUSE (per Manager): if the chosen indirect form would make
the defective item MORE answerable — e.g. an indirect description that
accidentally points at a PRESENT key in the defective member, or that adds
content — it is REJECTED at the design stage. The indirect query must resolve to
the SAME (absent, in defective) key identity, changing only the query form.
```

## 7. Clean target

```text
clean strict_accuracy in 0.88–0.92 (strict interior of 0.6625 < a < 0.95).
Basis: CAL-B (direct query, same content) scored clean 0.975. The added
query-side resolution step is expected to depress clean by ~0.05–0.09 into the
band. EXPECTATION for a later (gated) run, not a measured value.
```

## 8. Defective target

```text
defective strict_accuracy ≤ ~0.10 (at or below CAL-B's 0.050), since list content
is identical to CAL-B and the indirect step does not add decoy material.
Separation requirement: clean − defective ≳ 0.78 (target clean ~0.90 vs
defective ~0.05–0.10). If defective rises materially above CAL-B's 0.050, the
non-content lever has FAILED its purpose → PIVOT (see §11).
```

## 9. Single-difference preservation

```text
- Clean and defective CAL-Q members differ in EXACTLY the pre-registered defect
  (P2: the queried key — as resolved by the indirect description — is absent in
  the defective member), matched on length (13), slots (8–11), vocabulary,
  near-miss (2), null-rate, format, count, scorer, AND query form (both members
  get the SAME indirect query; the only difference is key presence/absence).
- The indirect query is a SHARED property of both members. It is not a second
  difference. The defect remains the single difference.
- CRITICAL CHECK: the indirect description must pick out the same key IDENTITY in
  both members (present in clean, absent in defective). If the description
  resolves differently across members, that is a second difference → DROP CAL-Q,
  do not run as a confound (same gate as CAL-D/CAL-E).
- Single-difference is checked mechanically at construction (gated step).
```

## 10. Semantic-read requirements

```text
- Nine-field shown-read (owner-signed) of the CAL-Q construct spec before any
  construction is trusted: artifact / path / commit / sha256 / claimed concept /
  check performed / observed structure / required structure / surplus check,
  disposed PASS (UNCERTAIN→HOLD).
- The read must explicitly confirm the three load-bearing claims: (a) list
  content is IDENTICAL to the CAL-B baseline (no added decoy); (b) ONLY the query
  form changed (direct→indirect); (c) the indirect description resolves to the
  same key identity in both members (single-difference holds).
```

## 11. Pre-declared decision rule (before any run)

```text
BAND PLAUSIBLE:
  CAL-Q clean lands STRICTLY inside 0.6625 < a < 0.95 (target 0.88–0.92) AND
  defective stays ≤ ~0.10 with separation ≳ 0.78. A non-content lever has created
  an in-band clean point with preserved discrimination → the D4 route is viable
  → a certification-run request becomes well-formed (separate Manager auth + GREEN).
NEEDS REPAIR:
  clean remains at/above 0.95 (the query step was too weak), OR clean drops too
  close to the shortcut floor (too strong), OR defective rises enough to erode
  separation. → only revisit if a SPECIFIC non-handwavy adjustment is identified;
  otherwise this collapses into PIVOT.
PIVOT:
  the non-content lever ALSO inflates defective, OR fails to create a clean
  in-band point. Per the Manager's framing, this is the honest end of D4
  certification-readiness: stop pursuing this family for a stress-retention
  baseline and pivot to Tier 1 eval-validity auditing. The accumulated result —
  "neither content nor query-side levers can place a clean off-ceiling point with
  preserved discrimination in this task family" — is a publishable negative
  finding, and Tier 1 / Layer 1 is independently demonstrated and defensible.
This is the FINAL D4 rescue attempt unless the result cleanly identifies a new,
specific, non-handwavy repair. The rule is fixed now, before any run.
```

## 12. Checklist (status fields: PASS / FAIL / HOLD / NOT EVALUATED)

```text
route state                   YELLOW (model-free) ....................... PASS
artifact identity             sources anchored: CAL-A/B/C/E run records,
                              CAL-E interpretation 4cafaedb, HEAD 8a64010 . PASS
CAL-E run record + interp cited per §2 ................................... PASS
semantic-read                 §10 reads required at the (gated) construction  HOLD
proposed non-content lever    indirect-key query, fully specified ......... PASS
lever changes ONLY query-side content/decoy held = CAL-B; only query form .. PASS
defective-answerability guard indirect resolves to same absent key; no added
                              decoy; reject-if-more-answerable clause ...... PASS
clean target                  0.88–0.92 strict interior, with basis ....... PASS
defective target              ≤~0.10 + separation ≳0.78 .................... PASS
single-difference preservation indirect query SHARED; same key identity both
                              members; drop-if-violated gate .............. PASS
later decision rule           PLAUSIBLE / NEEDS REPAIR / PIVOT pre-declared  PASS
closed-gate preservation      §13; no execution/cert/compression invoked ... PASS
```

```text
SUMMARY: design-level rows PASS. One HOLD (semantic-read) is correct — the
nine-field reads happen when CAL-Q is materialized at a later gated step. No
FAIL. The defective-answerability guard (content held = CAL-B; only query form
changes; reject if the indirect form adds answerability) is the design feature
that directly targets CAL-E's falsified failure mode.
```

## 13. Closed gates

```text
No model execution · No certification run · No compression · No INT8/INT4 stress
· No second compression rung · No full ladder · No candidate certification · No
ranking · No Claim C activation · No public benchmark packaging · No funder-facing
release · No SBIR submission. This spec is model-free. CAL-Q is executed only
under separate Manager authorization + route-state GREEN; nothing here grants it.
```

---

## Submap status after this spec

```text
SUBMAP: Certification-readiness / off-ceiling repair design — STILL OPEN, at the
  FINAL D4 rescue attempt.
  stage 3-rescue (this): non-content lever (CAL-Q, indirect-key query on CAL-B
    content) specified; designed to pressure clean without inflating defective.
  → next: (gated) CAL-Q run → §11 verdict.
  exit (A) band plausible:  reachable IFF CAL-Q lands clean in-band with separation
  exit (B) pivot:           the Manager-framed honest end if CAL-Q fails like CAL-E
  This is the dispositive test: query-side is the one lever class not yet implicated.
```

— Senior Engineer
