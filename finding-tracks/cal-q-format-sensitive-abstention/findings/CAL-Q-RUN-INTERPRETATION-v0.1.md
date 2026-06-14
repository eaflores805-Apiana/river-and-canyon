# CAL-Q-RUN-INTERPRETATION-v0.1

**Version:** v0.1. River and Canyon program. Certification-readiness submap, stage 3-rescue-run (Senior interpretation of the CAL-Q v0.3 calibration run).
**Status:** model-free interpretation of CS's byte-verified run (commit 4456d5a, HEAD-verified). No new run. Authorizes nothing. Anchored on origin/main HEAD 4456d5a.
Owner/drafter: Senior Engineer · CS: executed the run, delivered four-way bytes (verified) · Team Lead: Manager decision surface · Manager: the PIVOT decision this interpretation recommends.

---

## 1. The §9a sequencing control was applied (per the rule just written)

Before interpreting the aggregate, the per-item defective bytes were read — this
is exactly the moment §9a governs (a dramatic aggregate about to drive a route
decision). The read confirms the result is REAL, not a scorer artifact:

```text
All 40 defective items emitted an actual single-letter value (b, h, z, l, a, ...);
0 emitted any abstention form (no "none", no "NONE"). format_abstention_artifact
= 0.0 (no casing artifact this time). The model genuinely stopped abstaining.
(Contrast §7/CAL-E, where 13 "failures" were lowercase-none mis-scores. Here there
are zero — the collapse is the model's behavior, not the parser's.)
```

So unlike the CAL-E false alarm, this is not an artifact to be corrected away.
The discrimination collapse is real.

## 2. Byte-verified results (four-way, per spec §7)

```text
  metric                        CAL-Q     vs CAL-B (same content, direct query)
  clean concept accuracy        0.650     dropped 0.325 (0.975 → 0.650)
  defective strict NONE         0.000     dropped from 0.050
  defective concept abstention  0.000     COLLAPSED from 0.925
  defective true false-emission 1.000     ROSE from 0.075 (inverted)
  defective format artifact     0.000     no abstention in either form
```

```text
Full sweep (5 candidates):
  cand   query form   clean   def-abstention   false-emission
  CAL-A  direct       1.000   0.900            0.100
  CAL-B  direct       0.975   0.925            0.075
  CAL-C  direct       0.950   0.875            0.125
  CAL-E  direct       0.975   0.900            0.100
  CAL-Q  code book    0.650   0.000            1.000
```

## 3. Verdict against the pre-declared §8 rule: PIVOT

The rule was fixed before the run. All three BAND PLAUSIBLE criteria fail, and
the failure is specifically the PIVOT condition, not NEEDS REPAIR:

```text
BAND PLAUSIBLE (all three required):
  clean strictly in 0.6625 < clean < 0.95   → 0.650 < 0.6625 → BELOW band. FAIL.
  defective concept abstention stable ~0.90  → 0.000 → collapsed. FAIL.
  true false-emission low ~0.10              → 1.000 → inverted. FAIL.
→ NOT band-plausible.

PIVOT condition (pre-declared §8):
  "query-side difficulty ALSO fails to move clean off ceiling WITHOUT breaking
   discrimination — i.e. no lever (content OR query-side) places a clean in-band
   point with preserved discrimination."
  CAL-Q MOVED clean off the ceiling (0.975 → 0.650 — the first sub-ceiling clean
  point in the program's history) BUT broke discrimination completely
  (abstention 0.925 → 0.000). That is precisely the PIVOT condition: the lever
  cannot place a clean in-band point WITH discrimination preserved.
```

**Verdict: PIVOT.** This was the final D4 rescue attempt under a pre-declared
rule, and the rule resolves to PIVOT.

## 4. Why it broke — the mechanism (from the bytes, not the label)

This is the scientifically important part, and it is a genuine finding about the
construct, not just a failed calibration:

```text
The code-book decode step did NOT simply "add clean-side difficulty." It CHANGED
THE MODEL'S STRATEGY. Reading both members:
  - CLEAN: 26/40 correct. The 14 wrong clean items emit single-letter values
    (wrong values), same output mode as the defective side.
  - DEFECTIVE: 0/40 abstain; 40/40 emit a single letter — a value grabbed from
    the item rather than an abstention.
The model shifted from "look up the key; abstain if absent" to "decode and emit
SOME value," and it emits a value REGARDLESS of whether the key is present.
Clean: the emitted value is sometimes the right one (0.650). Defective: it should
abstain but emits anyway (abstention 0.000).
THE KEY INSIGHT: clean dropping to 0.650 and defective abstention dropping to
0.000 are THE SAME EFFECT, not two independent ones. The decode step did not load
"difficulty" onto an otherwise-intact lookup-and-abstain process; it displaced
the abstention behavior itself. Abstention and lookup were not separable under
this lever — loading the query collapsed the very behavior the instrument
measures.
```

```text
WHY THIS MATTERS BEYOND CAL-Q:
A valid difficulty lever must lower clean accuracy while LEAVING THE MEASURED
BEHAVIOR (key-presence discrimination) INTACT. The code-book lever fails this not
by being too strong but by being the WRONG KIND: it makes the task hard in a way
that changes WHICH behavior the model runs, so the harder task is no longer
measuring the same thing. This is a construct-validity failure of the lever, of
exactly the family this program studies — the lever moved the number by changing
the construct, not by stressing it.
```

## 5. What the full sweep now establishes

```text
- CONTENT levers (CAL-A/B/C/E): move clean weakly and non-monotonically; cannot
  place clean below the ceiling at all (all ≥ 0.95). Discrimination intact (~0.90)
  but no off-ceiling point.
- QUERY-SIDE lever (CAL-Q): DOES move clean below the ceiling (first time) but
  destroys discrimination by changing the model's strategy.
- TOGETHER: neither lever class can place a clean point strictly inside the band
  WITH discrimination preserved. Content can't move clean; query-side moves clean
  but breaks the measured behavior. The two failure modes are complementary, and
  between them they cover the available lever space for this task family.
```

This is the supported negative result the pre-registered rule was built to earn.
It is NOT a two-point inference: both lever classes have now been tried under
declared rules, and both fail for distinct, understood reasons.

## 6. Recommendation: PIVOT to Tier 1 (honest, supported, and a real product)

```text
The honest next move is the one the Manager pre-framed: stop pursuing D4
certification-readiness as the path to a stress-retention baseline, and pivot to
Tier 1 eval-validity auditing.
Basis:
  - The pre-declared rule resolves to PIVOT on the run's own bytes.
  - The negative result is publishable: "in this synthetic key-value lookup
    family, no available difficulty lever — content or query-side — places a clean
    FP16 baseline strictly off-ceiling while preserving key-presence
    discrimination." That is a real, scoped finding about the limits of
    constructing a calibrated baseline in this family.
  - Tier 1 / Layer 1 (eval-validity auditing) is independently demonstrated by
    the program's own work: survival≠correctness, correctness≠constructibility,
    hash≠construct-validity, the saturation/elimination diagnosis, the parser-bug
    catch, and now the CAL-Q lever-validity failure are all eval-validity findings.
    The instrument that the program built IS the deliverable.
```

## 7. What this does NOT establish (epistemic guardrails)

```text
- It does NOT prove the compositional seam does or does not exist. The program
  never reached a certified compression rung; the seam question is UNANSWERED, not
  answered negatively. The pivot is away from THIS BASELINE-CONSTRUCTION PATH, not
  a verdict on the seam.
- It does NOT prove no baseline is constructible in ANY task family — only that
  this synthetic key-value family resists it across the levers tried. A different
  task family might host a calibrated baseline; that is a future question.
- It does NOT mean CAL-Q was a wasted attempt. It produced the program's first
  sub-ceiling clean point AND a clean mechanistic account of why query-side
  difficulty breaks discrimination — both are findings.
- The PIVOT is a route decision for the Manager, not a Senior authorization. This
  interpretation recommends; the Manager decides.
```

## 8. The strategic question this forces (flagged, per C5)

```text
The CAL-Q result sharpens the two-norths question C5 raised. If the program's
real deliverable is the INSTRUMENT (eval-validity methodology), then this PIVOT
does not diminish the program — it CLOSES the D4 question cleanly (the baseline
path is exhausted under declared rules) and frees effort for Tier 1, which the
work already supports. If the real deliverable was always the COMPRESSION result
(the seam), then this is a genuine setback that leaves the headline question
unreached. The Manager should state which, because it determines whether this
PIVOT reads as "a question closed and a product confirmed" or "the main goal
deferred again." Either way, D4-as-baseline-path is settled by these bytes.
```

## 9. Submap status after this interpretation

```text
SUBMAP: Certification-readiness / off-ceiling repair design — READY TO CLOSE on a
  PIVOT outcome (pending Manager decision).
  stage 3-rescue-run (this): CAL-Q v0.3 moved clean off ceiling (first ever) but
    collapsed discrimination by changing the model's strategy (decode-and-emit
    displacing lookup-and-abstain). All 3 BAND PLAUSIBLE criteria fail; the
    pre-declared PIVOT condition is met.
  → recommended: Manager authorizes the pivot to Tier 1 eval-validity auditing;
    the submap closes with a supported negative result; the rejection-audit
    control (methodology record §11 stub) should be drafted in full now, since
    CAL-Q has resolved and a PIVOT is itself a rejection that control governs.
  exit taken (B) PIVOT: both lever classes tried under declared rules; both fail
    for distinct understood reasons; the negative result is the earned outcome.
```

## 10. What remains closed

```text
No model execution beyond this completed calibration read · No certification run ·
No compression · No INT8/INT4 stress · No second compression rung · No full ladder
· No candidate certification · No ranking · No Claim C activation · No public
benchmark packaging · No funder-facing release · No SBIR submission. This
interpretation is model-free (a read of the completed run's bytes).
```

---

## Note on method (the symmetry worth marking)

```text
Two runs, two dramatic aggregates, two opposite outcomes — and the §9a control
(read the per-item bytes before the aggregate moves a decision) was right both
times. At CAL-E, the bytes REVERSED the aggregate (the "collapse" was a scorer
artifact; do not pivot). At CAL-Q, the bytes CONFIRMED the aggregate (the collapse
is real; pivot). The control is not "distrust bad-looking numbers" — it is "read
the bytes, then let them decide, whichever way they point." CAL-Q is the case
where reading the bytes confirmed the rejection rather than overturning it — which
is exactly why the rejection-audit control (§11) matters: most of the time the
bytes will confirm, but the discipline must be applied even when the answer is
"yes, really pivot," so that the one time it would have been wrong is caught.
```

— Senior Engineer


---

## Reconciliation note — CS byte-read converges on PIVOT and sharpens the mechanism (HEAD 4456d5a)

CS's independent byte-read (CS-CAL-Q-RUN-REPORT) reaches the same PIVOT verdict
and adds a sharper, verified account of the mechanism that this interpretation
adopts and credits.

### The sharper mechanism (CS): abstention is FORMAT-COUPLED, not capability-resident

```text
CS's framing, verified against the bytes: the model has two skills on opposite
sides of a prompt-format boundary.
  - Under DIRECT queries (CAL-A/B/C/E): abstention is robust ~0.90, false-emission
    low ~0.10 — on identical content.
  - Under the INDIRECT code-book query (CAL-Q): abstention collapses to 0.000 — on
    the SAME CAL-B content. Only the query FORMAT changed.
VERIFICATION: CAL-B (direct) def-abstention 0.925 vs CAL-Q (code-book) 0.000, same
content, query form the only difference. The "I can't find the key → abstain"
pathway is COUPLED to the direct-query training distribution. Step outside that
format and the abstention discipline does not transfer.
This is a more precise statement of §4's "the lever changed the model's strategy":
the strategy that changed is abstention, and it changed because abstention is
format-bound to the direct-query basin, not a format-independent capability.
```

### The asterisk this puts on a PRIOR claim (the program's discipline requires marking it)

```text
The rescore reinterpretation (CAL-ABCE-RESCORE-REINTERPRETATION-v0.1, 8433e32f)
claimed "the instrument distinguishes clean from key-absent ROBUSTLY, even as
constructs harden." CAL-Q sharpens that claim and requires an asterisk:
  AS WRITTEN:   discrimination is robust under harder constructs.
  CORRECTED:    discrimination is robust under harder constructs *within the
                direct-query format*. It is FORMAT-SCOPED, not capability-scoped.
                CAL-Q shows the robustness did not survive a query-format change.
This is NOT a reversal of the rescore (the CAL-A/B/C/E numbers stand; CAL-E was
still a scorer artifact). It is a sharpening of WHAT the rescore was measuring:
direct-query discrimination, which is real but narrower than "discrimination"
unqualified. The prior claim should be read with this scope from now on.
(This is itself an instance of the §9-family lesson: a robust-looking result
meant something slightly narrower than its label, and the boundary was found by
the next probe.)
```

### The narrow exit CS flags (honest assessment)

```text
CS names one reasonable narrow exit: the code book may be UNIQUELY HOSTILE (a
prompt structure far outside Qwen's training distribution), and a DIFFERENT
closed-world non-content lever — e.g. a "confirm-then-return" form ("first
confirm K is in the list, then return its value") — might add clean-side
difficulty while keeping abstention in a format closer to the direct-query basin.
HONEST ASSESSMENT of this exit:
  - It is scientifically reasonable. CAL-Q tested ONE query-side lever; "query-side
    breaks discrimination" is really "the code-book lever breaks discrimination,"
    and a gentler lever might not.
  - BUT two things weigh against taking it now: (1) the Manager named CAL-Q as the
    FINAL bounded rescue, and CAL-Q consumed that slot; trying again requires the
    Manager to re-authorize or to accept that "final" was provisional. (2) The
    format-coupling finding gives a MECHANISTIC reason to expect ANY format change
    to risk the same collapse — confirm-then-return is also outside the direct-query
    basin, so the prior is that it too may move abstention. It is not obviously
    safer; it is a different bet on the same coupling.
  - RECOMMENDATION: do not fold this exit into the PIVOT decision silently. Put it
    to the Manager explicitly as a named option — "PIVOT now, OR authorize ONE more
    non-content lever (confirm-then-return) against the format-coupling prior" — and
    let the Manager decide whether the 'final' framing holds. The bytes support
    PIVOT under the rule as written; the exit is a Manager-authorization question,
    not a Senior reinterpretation of the rule.
```

### Net

```text
The PIVOT verdict stands on the rule as written. CS's mechanism (format-coupled
abstention) is adopted as the precise account of WHY, and it sharpens a prior
claim (direct-query-scoped discrimination) that should now carry that scope. The
one open decision is the Manager's: accept the PIVOT, or re-authorize one final
gentler lever against a mechanistic prior that it may fail the same way. Either
way, the format-coupling finding is the real scientific result of CAL-Q.
```

