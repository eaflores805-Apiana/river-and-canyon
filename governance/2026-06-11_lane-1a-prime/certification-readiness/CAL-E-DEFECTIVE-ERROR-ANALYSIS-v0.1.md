# CAL-E-DEFECTIVE-ERROR-ANALYSIS-v0.1

**Version:** v0.1. River and Canyon program. Certification-readiness submap, stage 3-diagnostic (CAL-E defective error analysis).
**Status:** model-free analysis of EXISTING CAL-E outputs (no new run). Reads the actual defective per-item outputs from bytes and classifies them. Authorizes nothing. Anchored on origin/main HEAD 72356eb.
Owner/drafter: Senior Engineer (classification + interpretation) · CS: extracted/labels observable output-source relationships · Team Lead: Manager decision surface · Manager: rescue/redesign/pivot/scorer-audit decision.

---

## 1. Headline finding (this changes the CAL-E verdict)

**CAL-E's apparent "defective inflation to 0.575" is largely a parser case-sensitivity artifact, not false-answer leakage.** Read from the defective per-item bytes:

```text
Of the 40 CAL-E defective (key-absent) items:
  - 23 emitted raw "NONE" (uppercase) → scored strict_correct=True (abstained)
  - 13 emitted raw "none" (lowercase) → scored strict_correct=FALSE, parsed_kind=OTHER
        despite being the SAME abstention intent (a casing parser bug)
  - 4  emitted an actual stray value ("y","a","l","x") → genuine non-abstention
TRUE behavior: the model abstained on 36/40 = 90% of key-absent items.
It emitted a real false value on only 4/40 = 10%.
The reported defective "accuracy" 0.575 counts ONLY uppercase NONE; the 13
lowercase-none abstentions were mis-scored as failures, DEFLATING the measured
abstention rate and creating the appearance of inflation.
```

## 2. Evidence table (CS-extracted, byte-read; Senior bins)

```text
record_id        gold   raw_output   parsed_kind  strict_correct  → BIN
CAL-E-DEF-000    null   "NONE"       NONE         True            correct abstention
CAL-E-DEF-001    null   "none"       OTHER        False           SCORER/PARSER ARTIFACT
CAL-E-DEF-003    null   "y"          letter       False           true false-emission
CAL-E-DEF-004    null   "a"          letter       False           true false-emission
CAL-E-DEF-011    null   "l"          letter       False           true false-emission
CAL-E-DEF-012    null   "x"          letter       False           true false-emission
CAL-E-DEF-008/010/016/018/019/020/021/022/025/027/028/032
                 null   "none"       OTHER        False           SCORER/PARSER ARTIFACT (×13 total)
... 23× raw "NONE" → True (correct abstention)
SUMMARY: 23 correct (NONE) · 13 parser-artifact (none) · 4 true emission (letters).
scorer accepted (correct) = 23; scorer rejected = 17, of which 13 are
abstentions mis-rejected on casing and only 4 are genuine emissions.
```

## 3. Bin classification (the Manager's six bins)

```text
SCORER_LENIENCY:             0  (NO over-acceptance; all 23 "correct" are true NONE)
FALSE_ANSWER_MATERIAL:       4  (the only genuine stray values — single letters
                                "y","a","l","x"; the real, small leakage)
POSITION_ENDPOINT_SHORTCUT:  0  observed (the 4 emissions are single letters, not
                                obviously first/last/salient values — see §5 caveat)
QUERY_TEMPLATE_ARTIFACT:     0  (no template-induced answerability seen)
ABSTENTION_FAILURE_NON_NULL: 4  (same 4 — model failed to abstain and emitted a value)
SCORER/PARSER_ARTIFACT:     13  (raw "none" lowercase scored as OTHER/wrong — the
                                DOMINANT bin, and the cause of the apparent inflation)
OTHER_UNCLASSIFIED:          0
```

The dominant bin is **SCORER/PARSER_ARTIFACT (13/17 of the "failures")** — a case-sensitivity bug in NULL parsing, not a model discrimination failure.

## 4. The artifact contaminates the whole sweep (re-reading all candidates)

```text
                 reported    NONE-casing   TRUE false-      corrected true
  candidate      def "acc"   artifacts     emission rate    abstention rate
  CAL-A          0.125       31            0.100 (4/40)     0.900
  CAL-B          0.050       35            0.075 (3/40)     0.925
  CAL-C          0.225       26            0.125 (5/40)     0.875
  CAL-E          0.575       13            0.100 (4/40)     0.900
```

Two things follow:

```text
(a) The reported defective "accuracy" is dominated by how many abstentions the
    model happened to render as uppercase vs lowercase NONE — which VARIES run to
    run (31, 35, 26, 13 lowercase-none mis-scores). That variation, NOT
    false-answer leakage, drives the reported 0.125→0.05→0.225→0.575 swing.
(b) The TRUE false-emission rate (model emits a stray value when it should
    abstain) is STABLE at ~0.075–0.125 across ALL FOUR candidates, INCLUDING
    CAL-E. CAL-E did not actually emit more false answers than CAL-A/B/C.
```

So the prior CAL-E interpretation's central claim — "length+depth inflated
defective, separation collapsed, content levers blocked" — was **reading a
parser artifact as a model behavior.** The model's actual key-absent
discrimination is roughly constant across all candidates. (Note: the run
record's `separation = clean_correct − defective_correct_abstention` = 0.4 for
CAL-E inherits the same artifact, because the defective term is the deflated
abstention count.)

## 5. The Manager's seven questions — answered

```text
1. Are CAL-E defective successes real under the scorer, or scorer artifacts?
   The 23 "successes" are REAL abstentions (raw NONE). The 17 "failures" are
   mostly ARTIFACTS: 13 are real abstentions mis-scored on casing; only 4 are
   genuine emissions. So the "failures" are largely scorer artifacts.
2. Are successful defective outputs mostly from salient positions?
   N/A — the "successes" are abstentions (NONE), not emitted values. The 4 true
   emissions are single letters; with n=4 no position pattern is establishable.
3. Mostly from near-miss / distractor material?
   Cannot be claimed: only 4 true emissions, single letters. CS labeling did not
   tie them conclusively to near-miss values. Too few to characterize.
4. Mostly random plausible values from context?
   Only 4 emissions total; insufficient to call random-plausible vs anything else.
5. D4-specific, scorer-specific, or follows us to another family?
   The DOMINANT effect is SCORER-SPECIFIC (NULL casing parser), which would
   follow ANY task family using this scorer — and is trivially fixable. The
   residual true-emission rate (~0.10) is small and stable, not a D4 collapse.
6. Does the planned non-content query rescue still make sense?
   The PREMISE for the rescue (CAL-E showed catastrophic defective inflation) is
   now substantially weakened — the inflation was mostly a parser artifact. The
   rescue may not be NEEDED to fix a defective problem that is ~0.10 and stable.
   But see §6: the scorer must be fixed and the sweep re-scored FIRST.
7. Should the final D4 rescue proceed, be redesigned, or pivot?
   NEITHER proceed-as-planned NOR pivot yet: FIX THE SCORER and RE-SCORE the
   existing CAL-A/B/C/E outputs first. The rescue decision should be made against
   CORRECTED numbers, not artifact-contaminated ones.
```

## 6. Verdict (Manager's output categories)

```text
SCORER AUDIT REQUIRED.
```

```text
The apparent CAL-E defective failures are dominated (13 of 17) by a NULL
case-sensitivity parser bug: raw "none" is scored OTHER/wrong while "NONE" is
scored as correct abstention. This contaminates the defective "accuracy" of
EVERY candidate and is the main driver of the reported CAL-E "inflation." Per the
Manager's own rule ("if the defective successes are scorer artifacts, we fix the
scorer"), scorer correction must happen before any further task design or the
final rescue.
```

This is not a pivot and not a green light: it is a **prerequisite correction**.
The honest sequence:

```text
1. Fix the scorer: NULL parsing must accept case-insensitive "none"/"NONE"
   (and document the exact normalization). Model-free code fix + re-score of the
   EXISTING outputs (no new model run needed — the raw outputs are on disk).
2. Re-score CAL-A/B/C/E from their existing raw outputs under the corrected
   scorer → get corrected clean accuracy, corrected defective abstention, and a
   properly-defined discrimination (clean-correct vs true false-emission).
3. THEN re-decide: with corrected numbers, the true picture appears to be
   clean ~0.95–1.0 and true false-emission ~0.10 stable — which may mean the
   band/separation question looks very different (and possibly more favorable)
   than the artifact-contaminated reading suggested.
```

## 7. What I got wrong (owning it, second time in this arc)

```text
The CAL-E interpretation (v0.1) read the defective number 0.575 as "the model
emitting more false answers as content scaled," and built the content-levers-
blocked / PIVOT-WATCH conclusion on it. Reading the per-item bytes shows that was
wrong: the model abstained 90% of the time; the 0.575 was mostly a casing parser
artifact. I diagnosed a model behavior from an aggregate number without reading
the per-item outputs — the exact failure this program exists to prevent, and the
exact diagnostic the Manager correctly ordered before spending the rescue. The
lesson (again): read the items, not the aggregate.
```

## 8. What this does NOT establish (epistemic guardrails)

```text
- It does NOT prove the band is reachable. It removes a contaminating artifact;
  the corrected re-score is still pending and must be computed before any claim.
- It does NOT clear the 4 true emissions. ~0.10 false-emission is real and
  should be tracked, just not mistaken for a 0.575 collapse.
- It does NOT authorize the rescue OR the pivot. It redirects to a scorer fix +
  re-score, after which the rescue/pivot decision is made on clean numbers.
- The n=4 true emissions are too few to characterize by source (position/near-
  miss/random); no mechanism claim is made about them.
```

## 9. Submap status after this analysis

```text
SUBMAP: Certification-readiness / off-ceiling repair design — STILL OPEN; the
  final rescue is PAUSED pending scorer correction.
  stage 3-diagnostic (this): CAL-E defective "inflation" is mostly a NULL-casing
    parser artifact; true discrimination ~stable across candidates.
  → next model-free step: FIX SCORER (case-insensitive NULL) + RE-SCORE existing
    CAL-A/B/C/E raw outputs; re-decide rescue/pivot on corrected numbers.
  The CAL-Q non-content rescue spec (d0bb0217) remains filed but its PREMISE is
    under revision — do not run it until the corrected sweep numbers are in.
```

## 10. What remains closed

```text
No model execution · No new candidate · No certification run · No compression ·
No INT8/INT4 stress · No second compression rung · No full ladder · No candidate
certification · No ranking · No Claim C activation · No public benchmark
packaging · No funder-facing release · No SBIR submission. This analysis is
model-free (a read of existing outputs); the recommended scorer fix + re-score
is also model-free (no new model run — raw outputs are on disk).
```

— Senior Engineer


---

## Reconciliation note — independent CS extraction converges (HEAD e581240)

CS's independent byte extraction (CS-CAL-E-DEFECTIVE-OUTPUT-EXTRACTION-v0.1,
cal-e_defective_error_table.json 99e342bd) reaches the IDENTICAL reading reached
in §1–§4 above, derived separately:

```text
  23 NONE strict-abstain · 13 lowercase-none (concept abstention, scorer-rejected)
  · 4 letter emissions · 36/40 = 0.90 abstention-in-concept · constant ~0.90 across A/B/C/E.
```

Two refinements CS's source-labeling ADDS to this analysis:

```text
1. OF THE 4 TRUE EMISSIONS: 0 are pure invention (out-of-context). CS labels
   them 1 near-miss-distractor value + 3 other-in-context values. The model never
   fabricated a value absent from the list — even its 4 genuine non-abstentions
   grabbed something present in context. This STRENGTHENS the no-real-leakage
   reading: there is no evidence of the model inventing answers for key-absent
   items; the worst case is occasionally copying an in-context value (~0.10),
   stable across candidates.
   → Bin update: the 4 FALSE_ANSWER_MATERIAL / ABSTENTION_FAILURE_NON_NULL items
     are confirmed in-context copies (1 near-miss, 3 other-in-context), 0 invention.
2. CS frames the dominant effect precisely as a FORMAT SHIFT in abstention
   (none → NONE) as the construct hardens: CAL-A 5 strict / 31 off-grammar (12.5%
   in-grammar) → CAL-E 23 strict / 13 off-grammar (57.5% in-grammar). The strict
   scorer reads this format shift as rising "defective accuracy." This is the same
   parser/casing artifact identified in §1, expressed as the model's abstention
   FORMAT migrating toward the scorer-accepted token as difficulty rises.
```

Neither refinement changes the verdict (SCORER AUDIT REQUIRED) or the recommended
sequence (fix case-insensitive NULL → re-score existing outputs → re-decide). They
strengthen it: the convergent, independent reading plus "0 invention" makes the
"the apparent inflation is a scoring/format artifact, not leakage" conclusion
robust. The corrected re-score remains the prerequisite before any rescue/pivot call.

