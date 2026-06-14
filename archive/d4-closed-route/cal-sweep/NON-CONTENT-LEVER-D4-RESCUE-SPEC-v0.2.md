# NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.2

**Version:** v0.2. River and Canyon program. Certification-readiness submap, stage 3-rescue (corrected). **Supersedes v0.1** (d0bb0217), which is retained and marked superseded. v0.1's premise (avoid defective inflation) was voided by the NULL-normalized re-score; this version reframes the same query-side mechanism around the real blocker (clean saturation).
**Status:** model-free SPECIFICATION. Specifies; runs nothing; requests nothing. Anchored on origin/main HEAD 3b2c1b0.
**Authorization:** "Model-free redesign authorized; no execution authorized."
Owner/drafter: Senior Engineer · CS: verify model-free + closed-world query construction + content/decoy unchanged + scorer/reporting distinction preserved · Team Lead: routing · Manager: any later run authorization + rescue/pivot decision.

---

## 1. What changed from v0.1, and why (corrected interpretation preserved)

```text
v0.1 PREMISE (now VOID): "CAL-E showed catastrophic defective inflation (0.575);
  content levers are blocked; use a query-side lever to avoid inflating defective."
WHY VOID: the NULL-normalized re-score (cal-abce_rescore_summary.json, HEAD
  3b2c1b0) showed CAL-E's "defective inflation" was a case-sensitive-NULL scorer
  artifact (a none→NONE format shift), NOT false-answer leakage. Corrected:
    defective concept-level abstention: ~0.90 STABLE across CAL-A/B/C/E
    true false-emission:                ~0.10 STABLE, 0 out-of-context invention
    real discrimination:                ~0.825–0.900 STABLE, incl CAL-E
v0.2 PREMISE (corrected): the instrument's discrimination WORKS and is robust.
  D4 is NOT in PIVOT WATCH on defective discrimination. The live blocker is the
  ORIGINAL one — CLEAN SATURATION: every candidate's clean accuracy is ≥ 0.95, at
  or above the ceiling. The same query-side lever from v0.1 is retained, but its
  PURPOSE is now "pull clean off the ceiling," and we now KNOW (from the re-score)
  it will not break discrimination, because abstention is robust under hard
  constructs.
```

## 2. Corrected anchor facts (NULL-normalized, byte-read HEAD 3b2c1b0)

```text
  candidate   clean    def-abstention(concept)   true-false-emit
  CAL-A       1.000    0.900                      0.100
  CAL-B       0.975    0.925                      0.075
  CAL-C       0.950    0.875                      0.125
  CAL-E       0.975    0.900                      0.100
  TARGET BAND (clean):  0.6625 < clean < 0.95
  STATUS: ALL clean ≥ 0.95 → clean saturation is the live blocker.
  Discrimination (clean − false-emit) ~0.83–0.90 stable → NOT a blocker.
```

## 3. D4 status statement (per Manager requirement #2)

```text
D4 is NOT in PIVOT WATCH on defective discrimination. The corrected re-score
shows defective concept-level abstention stable ~0.90 and true false-emission
stable ~0.10 across all candidates, including CAL-E. The instrument distinguishes
clean from key-absent robustly, even as constructs harden. The route remains open
on the strength of working discrimination; the only unsolved problem is clean
saturation (§4).
```

## 4. The live blocker: clean saturation (per requirement #3)

```text
Clean accuracy will not come off the ceiling on the levers tried so far:
  - content levers (length/depth/near-miss) move clean WEAKLY and
    NON-MONOTONICALLY: CAL-C reached 0.950 at length 17, but CAL-E at length 21
    went back UP to 0.975. List length is not a reliable clean dial.
  - no candidate has placed clean strictly inside 0.6625 < clean < 0.95.
The redesign's whole job: find a lever that reliably pulls CLEAN down into the
band, with discrimination (now confirmed robust) maintained as a check.
```

## 5. Proposed lever: query-side difficulty (per requirements #4–#7)

```text
LEVER (retained from v0.1, re-purposed): indirect-key query. Query the key
  INDIRECTLY via a description that uniquely identifies it from the SAME list,
  adding a clean-side resolution step:
    e.g. "what is the value for the key immediately after key J?"
         "what is the value for the alphabetically-last key?"
HELD FIXED (requirements #5, #6, #7):
  - content load:   UNCHANGED — built on CAL-B's content (len 13, slots 8–11,
                    near-miss 2): the setting with clean 0.975 and the cleanest
                    discrimination. No length/depth/near-miss escalation.
  - decoy material: UNCHANGED — identical list values; no new near-miss values.
  - closed-world:   the indirect description resolves to exactly one key that is
                    PRESENT in the clean member and ABSENT in the defective member;
                    no open-ended or out-of-list reference. The query is
                    answerable in-context for clean, correctly null for defective.
ONLY the QUERY FORM changes (direct → indirect). The difficulty lives in the
QUESTION, not the LIST.
```

## 6. How the lever pressures CLEAN (the corrected target)

```text
The clean item becomes a two-step task: resolve the description → identify the
key → read its value. The added resolution step is genuine clean-side difficulty
expected to pull clean DOWN from CAL-B's 0.975 into the band (0.6625–0.95),
WITHOUT adding list content. Because it is query-side, it does not depend on the
unreliable list-length dial (§4) — it adds difficulty directly to the lookup the
clean item must perform.
```

## 7. Why discrimination should HOLD (now a confirm-check, not the central worry)

```text
The re-score established that the model's key-absent discrimination is robust
(~0.90 abstention, ~0.10 emission, 0 invention) even under harder constructs.
The indirect query does not change this:
  - the defective item's list is identical to CAL-B (defective abstention there
    was ~0.925); no new decoy material is added.
  - an indirect query resolving to an ABSENT key gives the defective item no new
    answer material; correct behavior remains abstention.
  - if anything, the indirect step raises the bar for false-answering (the model
    must mis-resolve AND grab a value).
So discrimination is expected to stay in its established stable range. This is now
a CONFIRM-IT-HOLDS check, demoted from v0.1's central concern.
```

## 8. Clean target (primary success metric)

```text
PRIMARY: clean strict/concept accuracy in 0.6625 < a < 0.95 (target ~0.88–0.92,
  strict interior). This is THE success metric for v0.2.
Basis: CAL-B (direct query, same content) = clean 0.975. The added query-side
  resolution step is expected to depress clean by ~0.05–0.09 into the band.
  EXPECTATION for a later (gated) run, not a measured value.
```

## 9. Defective reporting (per requirement #8 — four-way, explicit)

```text
A later (gated) CAL-Q run must report defective behavior in ALL FOUR forms, to
prevent the v0.1-era artifact from recurring:
  1. strict NONE accuracy        (uppercase-NONE only — the OLD strict scorer)
  2. concept-level abstention    (none + NONE, case-insensitive — the TRUE rate)
  3. true false-emission rate    (model emits an actual value when it should abstain)
  4. format-abstention artifact  (the none-vs-NONE split — the size of the
                                  format shift, reported explicitly so it is never
                                  again mistaken for leakage)
The NULL-normalized (concept-level) scorer is authoritative; strict and the
format split are reported alongside for transparency.
```

## 10. Single-difference preservation

```text
- Clean and defective CAL-Q members differ in EXACTLY the pre-registered defect
  (the indirect-resolved queried key absent in the defective member), matched on
  length (13), slots (8–11), vocabulary, near-miss (2), null-rate, format, count,
  scorer, AND query form (both get the SAME indirect query).
- The indirect query is a SHARED property of both members; not a second difference.
- CRITICAL CHECK: the indirect description must resolve to the same key IDENTITY
  in both members (present in clean, absent in defective). If it resolves
  differently, DROP CAL-Q (do not run as a confound).
- Checked mechanically at construction (gated step).
```

## 11. Semantic-read requirements

```text
- Nine-field shown-read (owner-signed) of the CAL-Q v0.2 construct spec before
  any construction is trusted, disposed PASS (UNCERTAIN→HOLD).
- The read must confirm: (a) content/decoy IDENTICAL to CAL-B; (b) ONLY query
  form changed; (c) closed-world resolution to the same key identity in both
  members; (d) the four-way defective reporting (§9) is wired in.
```

## 12. Pre-declared decision rule (per Manager pass condition, before any run)

```text
BAND PLAUSIBLE:
  clean lands STRICTLY inside 0.6625 < clean < 0.95 AND concept-level defective
  abstention remains stable around the prior ~0.90 range WHILE true false-emission
  remains low (~0.10). → the query-side lever pulled clean off the ceiling with
  discrimination intact → a certification-run request becomes well-formed
  (separate Manager auth + GREEN).
NEEDS REPAIR:
  clean remains at/above 0.95 (lever too weak), OR clean drops too far toward the
  shortcut floor (too strong), OR defective concept-level abstention degrades
  materially (discrimination breaks). → adjust the query-side difficulty if a
  specific non-handwavy adjustment is identified.
PIVOT:
  query-side difficulty ALSO fails to move clean off the ceiling without breaking
  discrimination — i.e. no lever (content OR query-side) places a clean in-band
  point with preserved discrimination. → the honest end of D4 certification-
  readiness; pivot to Tier 1 eval-validity auditing. Accumulated result is a
  publishable negative finding; Tier 1 / Layer 1 is independently demonstrated.
Rule fixed now, before any run.
```

## 13. Checklist (status fields: PASS / FAIL / HOLD / NOT EVALUATED)

```text
route state                    YELLOW (model-free) ....................... PASS
artifact identity              sources anchored: rescore summary d874b894,
                               reinterpretation 8433e32f, CAL-B run record,
                               HEAD 3b2c1b0 .............................. PASS
supersedes v0.1                v0.1 d0bb0217 cited + marked superseded .... PASS
corrected interpretation preserved §1–§2 carry the NULL-normalized picture . PASS
D4-not-PIVOT-WATCH statement   §3 ........................................ PASS
clean-saturation as live blocker §4 ...................................... PASS
query-side lever                §5, indirect-key query .................... PASS
content load unchanged          built on CAL-B; no escalation ............ PASS
decoy material unchanged        identical list values .................... PASS
closed-world query construction resolves to same key identity, in-list .... PASS
clean target primary            §8, 0.6625–0.95 .......................... PASS
four-way defective reporting    §9 (strict / concept / false-emit / artifact) PASS
single-difference preservation  §10, shared query, drop-if-violated ....... PASS
semantic-read                   §11 reads at gated construction ........... HOLD
pre-declared decision rule      §12 PLAUSIBLE/NEEDS-REPAIR/PIVOT ........... PASS
calibration-only if run         §14 ...................................... PASS
closed-gate preservation        §15 ...................................... PASS
```

```text
SUMMARY: design-level rows PASS. One HOLD (semantic-read) is correct — the
nine-field reads happen at the (gated) construction step. No FAIL. The four-way
defective reporting (§9) is the v0.2 addition that makes the format artifact
impossible to mistake for leakage again.
```

## 14. Calibration-only (per requirement #9)

```text
If a CAL-Q run is later authorized, it is CALIBRATION-ONLY: it may answer ONLY
"does the query-side lever place clean in-band while discrimination holds?" — it
is FP16/native, no quantization, no stress arm, no certification, no compression.
```

## 15. Closed gates

```text
No model execution · No CAL-Q run · No certification run · No compression · No
INT8/INT4 stress · No second compression rung · No full ladder · No candidate
certification · No ranking · No Claim C activation · No public benchmark
packaging · No funder-facing release · No SBIR submission. This spec is
model-free. CAL-Q is executed only under separate Manager authorization +
route-state GREEN; nothing here grants it.
```

---

## Submap status after this spec

```text
SUBMAP: Certification-readiness / off-ceiling repair design — STILL OPEN.
  stage 3-rescue v0.2 (this): CAL-Q reframed around clean saturation (the real
    blocker); discrimination confirmed robust → demoted to a confirm-check;
    query-side lever retained for the CORRECTED reason.
  → next: (gated) CAL-Q run → §12 verdict (BAND PLAUSIBLE / NEEDS REPAIR / PIVOT).
  This remains the test of whether ANY lever (now query-side, after content
  levers proved weak/non-monotonic) can place clean in-band with discrimination
  intact. If it can: D4 viable. If it cannot: honest pivot to Tier 1.
```

— Senior Engineer
