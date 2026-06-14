# CAL-ABCE-RESCORE-REINTERPRETATION-v0.1

**Version:** v0.1. River and Canyon program. Certification-readiness submap, stage 3-rescore-interp (Senior reinterpretation of the NULL-normalized re-score).
**Status:** model-free interpretation of CS's corrected re-score (commit 3b2c1b0, HEAD-verified). No new run. Authorizes nothing. Anchored on origin/main HEAD 3b2c1b0.
Owner/drafter: Senior Engineer · CS: re-scored existing outputs (verified) · Team Lead: Manager decision surface · Manager: rescue/redesign/pivot decision.

---

## 1. Byte verification

```text
HEAD 3b2c1b09b79a59db3fec7a971f06989229a85dc7 — MATCH to CS-expected.
cal-abce_rescore_summary.json  sha d874b894 ✓
Re-score is a re-grade of EXISTING raw outputs under a case-insensitive NULL
parser; no new model run (sealed-bytes survival check intact).
```

## 2. The corrected picture (NULL-normalized, byte-read)

```text
  cand   clean   def-abstention   true-false-emit   REAL discrimination
                  (concept)        (model emits a    (clean − false-emit)
                                    value, wrongly)
  CAL-A  1.000    0.900            0.100             0.900
  CAL-B  0.975    0.925            0.075             0.900
  CAL-C  0.950    0.875            0.125             0.825
  CAL-E  0.975    0.900            0.100             0.875
```

Three facts, all stable across candidates:

```text
1. Defective concept-level abstention is FLAT ~0.90 (range 0.875–0.925). The
   model correctly recognizes "no answer exists" ~90% of the time, regardless of
   how hard the construct is.
2. True false-emission (the model emits a value when it should abstain) is FLAT
   and LOW ~0.10 (range 0.075–0.125), with ZERO out-of-context invention across
   all 320 outputs — the worst case is occasionally copying an in-context value.
3. REAL discrimination (clean-correct minus defective-false-emission) is HIGH
   and STABLE ~0.825–0.900 across ALL candidates, INCLUDING CAL-E.
```

## 3. What this resolves: PIVOT WATCH is LIFTED (it was an artifact)

```text
CAL-E triggered PIVOT WATCH on the claim that "defective inflated to 0.575,
separation collapsed to 0.400, content levers are blocked." The corrected
re-score shows that claim was an artifact of the case-sensitive NULL scorer:
  - CAL-E's defective concept-abstention is 0.900 — IDENTICAL to CAL-A.
  - CAL-E's true false-emission is 0.100 — same low, stable rate as every candidate.
  - CAL-E's REAL discrimination is 0.875 — essentially the same as CAL-A's 0.900.
There was NO defective collapse and NO content-driven leakage. The model
discriminates clean from key-absent EQUALLY WELL at CAL-E (length 21, deep slots,
4 near-miss) as at CAL-A (the easy control). The instrument's discrimination —
its whole purpose — WORKS, and works robustly as difficulty rises.
```

**Verdict: PIVOT WATCH CONFIRMED is REJECTED.** The defective successes did not
reveal a general non-discrimination problem; they revealed a scorer bug, now
fixed. There is no discrimination-failure reason to abandon D4.

## 4. What this does NOT resolve: the clean-off-ceiling problem reverts

I will not let the good news overstate itself. Correcting the scorer fixed the
*defective* scare; it did nothing to the *clean* numbers, which were never
affected by the NULL bug:

```text
  band question (m=δ=0.05): is clean strictly in 0.6625 < a < 0.95?
  CAL-A 1.000  AT/ABOVE ceiling
  CAL-B 0.975  AT/ABOVE ceiling
  CAL-C 0.950  AT/ABOVE ceiling (boundary)
  CAL-E 0.975  AT/ABOVE ceiling
EVERY candidate's clean accuracy is still ≥ 0.95 — at or above the saturation
ceiling. The original problem — getting clean accuracy strictly BELOW the ceiling
with measurable room — is exactly where it was BEFORE the CAL-E detour. We are
back to the real open question, minus the false alarm.
```

So the situation is genuinely better than the PIVOT-WATCH reading, but NOT solved:

```text
GONE:      the defective-inflation problem (was an artifact). Content levers are
           NOT blocked — they never inflated true defective behavior. The fear
           that drove PIVOT WATCH is removed.
REMAINS:   clean accuracy will not come off the ceiling. CAL-C reached 0.950
           (the boundary) at length 17; CAL-E at length 21 went back UP to 0.975
           (clean is non-monotonic — the levers are not a reliable clean dial).
           This is a SATURATION problem, the program's original Stage-E finding,
           not a discrimination problem.
```

## 5. The Manager's output categories — the call

```text
NOT "PIVOT WATCH CONFIRMED": rejected — discrimination is excellent and stable;
  the inflation was an artifact.
NOT "SCORER AUDIT REQUIRED": that audit is DONE (this re-score is its product).
The call is between RESCUE STILL JUSTIFIED and RESCUE MUST BE REDESIGNED:
```

```text
RESCUE STILL JUSTIFIED — but REDESIGNED around the RIGHT problem.
```

Reasoning:

```text
- The rescue is still justified because the blocker is NOT a structural
  discrimination failure (which would force a pivot). The instrument works. The
  only unsolved problem is clean saturation — a difficulty-calibration problem,
  which is solvable in principle.
- BUT the planned CAL-Q rescue (non-content / indirect-key query) was designed to
  fix the DEFECTIVE-inflation problem — which turned out not to be real. Its
  premise is void. CAL-Q as specified solves a non-problem.
- The redesign must target the ACTUAL problem: clean is stuck at/above 0.95 and
  the content levers (length/depth/near-miss) move it only weakly and
  NON-MONOTONICALLY (0.950 at len17, back to 0.975 at len21). The question is no
  longer "does hardening inflate defective?" (no) but "what lever reliably pulls
  CLEAN down into 0.6625–0.95 with room to spare?"
```

## 6. Recommended next action (model-free)

```text
REDESIGN the rescue around clean-saturation, not defective-inflation:
  The non-content query-side lever (indirect-key query) is STILL a good idea —
  but now for a DIFFERENT and CORRECT reason: it adds genuine clean-side
  difficulty (a resolution step) that should pull clean DOWN off the ceiling,
  and we now KNOW (from this re-score) that it will NOT hurt defective
  discrimination, because the model's abstention is robust (~0.90) and emission
  is low (~0.10) even under harder constructs. So CAL-Q's MECHANISM is still
  promising; its STATED PURPOSE must be rewritten from "avoid defective inflation"
  to "pull clean off the ceiling while discrimination (now confirmed robust) holds."
  CONCRETELY: re-issue CAL-Q with (a) the corrected premise, (b) clean target
  0.6625–0.95 as the primary success metric, (c) defective discrimination
  demoted to a confirm-it-stays-robust check rather than the central worry.
  Also worth one explicit note: clean's non-monotonicity (len17→21 went UP) means
  list-length is an unreliable clean dial; the query-side lever is preferable
  precisely because it adds difficulty without depending on list mechanics.
```

## 7. The Manager's seven (carried) questions — updated answers

```text
1. Defective successes real or scorer artifacts? → ARTIFACTS (now proven by the
   re-score): defective abstention is ~0.90 across all candidates.
2. Successful defective outputs from salient positions? → N/A; they are
   abstentions. The 4 emissions are in-context letters, 0 invention.
3. From near-miss/distractor material? → 1 of 4 near-miss, 3 other-in-context.
   Too few to characterize; not a content-leakage pattern.
4. Random plausible values? → no out-of-context invention at all.
5. D4-specific / scorer-specific / follows us? → the artifact was SCORER-specific
   (fixed). The residual is a CLEAN-SATURATION issue that is D4-task-specific.
6. Does the non-content query rescue still make sense? → YES, but for the
   corrected reason (pull clean off ceiling), not the original (avoid defective
   inflation). Redesign the premise.
7. Proceed / redesign / cancel-and-pivot? → REDESIGN (not cancel). The pivot is
   not warranted: discrimination works; only clean saturation remains.
```

## 8. What I am NOT claiming (epistemic guardrails)

```text
- I am NOT claiming the band is now reachable. Clean is still pinned ≥0.95; no
  candidate has landed clean in-band. The redesigned CAL-Q must still
  DEMONSTRATE (in a later gated run) that a query-side lever pulls clean down.
- I am NOT claiming content levers are good — they move clean weakly and
  non-monotonically. I am claiming they are not DISQUALIFIED by defective
  inflation (that was the artifact).
- I am NOT reversing the discipline: the corrected numbers are good news about
  the INSTRUMENT (it discriminates), not yet good news about the MEASUREMENT
  (clean still saturates).
- PIVOT remains a live future outcome IF the redesigned clean-targeted lever also
  fails to move clean off the ceiling. This re-score removes the FALSE reason to
  pivot; it does not remove the real test still ahead.
```

## 9. Submap status after this reinterpretation

```text
SUBMAP: Certification-readiness / off-ceiling repair design — STILL OPEN.
  stage 3-rescore-interp (this): PIVOT WATCH lifted (defective inflation was a
    scorer artifact); discrimination confirmed robust ~0.90; clean-saturation is
    the real, reverted open problem.
  → next model-free step: REDESIGN CAL-Q around clean-saturation (corrected
    premise; clean target 0.6625–0.95 primary; discrimination as confirm-check).
  The CAL-Q spec (d0bb0217) is NOT void as a mechanism but its premise is
    rewritten; supersede with a corrected version before any gated run.
  exit (A) band plausible:  not yet — clean still ≥0.95
  exit (B) pivot:           NOT warranted now (discrimination works); remains a
                            future outcome only if clean-targeted levers also fail
  exit (C) redesign/repair: THIS — redesign around the right problem
```

## 10. What remains closed

```text
No model execution · No new candidate run · No certification run · No compression
· No INT8/INT4 stress · No second compression rung · No full ladder · No candidate
certification · No ranking · No Claim C activation · No public benchmark
packaging · No funder-facing release · No SBIR submission. This interpretation is
model-free; the recommended CAL-Q redesign is a model-free spec; its run is
separately gated.
```

---

## Note on method

This re-score is the program's discipline paying off in the clearest possible
way: a scary aggregate (defective 0.575, "separation collapsed") was traced to a
case-sensitive parser, corrected, and re-read — and the corrected numbers show
the instrument was working all along. The honest balance: that is real good news
about the instrument's discrimination, and it removes a FALSE reason to abandon
D4 — but it returns us to the genuine, unsolved clean-saturation problem, which
the next (redesigned) attempt must actually crack. Good news about the ruler;
the measurement is still pending.

— Senior Engineer
