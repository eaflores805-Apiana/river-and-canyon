# PREREGISTRATION — HOP1 STABILITY INVESTIGATION (Path A) v0.1

**E. A. Flores**, Apiana AI, Inc. — June 18, 2026
*River and Canyon · Path A. Drafted by the Senior Engineer (lock-before-look). A bounded behavioral stability investigation prompted by the verified hop1 contrast. Routes for review; SE locks nothing and authorizes no run.*

> **Scope.** This is **NOT** a composite-gate rerun, a certification attempt, a compression test, Claim C, Paper B, or a mechanism probe. It is a **narrow, behavioral** investigation of one question: does hop1 admissibility **vary across V3 materializations**, and along which **predeclared surface/structural** dimensions does hop1 correctness co-vary? All findings are **positional/structural**, never mechanistic.

## 1. Research question

```text
PRIMARY:  Does hop1-isolated admissibility (lower Wilson 95% > 0.75) vary MATERIALLY across fresh V3
          materializations (seed blocks) of the SAME locked construction?
SECONDARY (descriptive): If it varies, along which PREDECLARED surface/structural covariates does hop1
          correctness co-vary? (co-occurrence, not cause)
```

## 2. Prior facts (anchors — already seen; not fresh test data)

```text
floor-check    001..096:  hop1 87/96 = 0.906 (cleared 0.75)   hop2 96/96 = 1.000
composite-gate 097..192:  hop1 28/96 = 0.292 (FAILED 0.75)    hop2 96/96 = 1.000
Both verified from bytes. These are ANCHORS only (§4): reference points, NOT part of the fresh stability test.
Observation on the seen 097..192 data: wrong hop1 predictions landed on the "P" role token (the r1-subject
distractor). This is the SOURCE of the §6 PRIMARY covariate hypothesis — tested on FRESH blocks, not asserted
from the seen data.
```

## 3. Exact materialization plan

```text
- SAME locked V3 construction (definition v0.4; generator 6a2ceee1 via the ≤999-enforcing wrapper cc07e5a2).
- 6 FRESH blocks, N=96 each (576 fresh items). Per item: realize the HOP1 context (primary) and the HOP2
  context (control). dq/composite NOT run (out of scope; this is hop1 stability, not a gate).
- FP16, greedy (temp 0), Qwen2.5-3B-Instruct rev aa8e7253. Each prompt executed once; no regeneration.
- Justification for N=96/block: matches the two anchors EXACTLY -> directly comparable Wilson CIs and the
  same 0.75 floor verdict per block. Justification for 6 blocks: 6 fresh + 2 anchors = 8 materializations,
  enough to see whether the per-block floor verdict is unanimous or straddles, without an unbounded sweep.
  (Block count / N are a PROPOSAL; TL/Manager may size up or down. Up to ~8 blocks of 96 fit within ≤999.)
```

## 4. Existing outputs: anchors, not fresh evidence

```text
- The 001..096 and 097..192 hop1/hop2 results are used DESCRIPTIVELY as ANCHORS (plotted/tabulated for
  context alongside the fresh blocks). They are ALREADY SEEN.
- The STABILITY / INSTABILITY BRANCH (§9) is decided ONLY on the 6 FRESH blocks (lock-before-look). The
  anchors do not enter the branch decision; they contextualize it.
- The §6 PRIMARY covariate (P-role landing) was SUGGESTED by the seen 097..192 result; it is pre-declared
  here and CONFIRMED-OR-NOT on the FRESH blocks. The seen P-landing is NOT the evidence; the fresh blocks are.
```

## 5. Fresh seed ranges (declared before look)

```text
Block F1: 193..288     Block F2: 289..384     Block F3: 385..480
Block F4: 481..576     Block F5: 577..672     Block F6: 673..768
All indices are 3-digit (≤999) -> per-item token-prefix width unchanged -> MAX_DELTA=8 remains valid
(wrapper-enforced, §12 tooling). All disjoint from the used ranges {001..192}.
```

## 6. Surface/structural covariates to log (predeclared; positional only)

```text
PRIMARY (confirmatory — the hypothesis from the seen result):
  - predicted_is_P_role_distractor : is the hop1 prediction a "P" distractor (an r1-SUBJECT of a relation-
    reusing distractor chain) rather than the correct r1-OBJECT B? Tested for reproduction on fresh blocks.

SECONDARY (exploratory — logged + reported as DESCRIPTIVE co-occurrence, NOT confirmatory findings):
  - seed/index block            - target B token (identity, width)
  - predicted token (identity, role class)   - relation token identity (r1)
  - relation position           - fact-line position of the target hop1 triple
  - distance from the QUERY line - prompt character count
  - token-width class           - competitor/distractor role class of the predicted token

ALL covariates are deterministic, structural/positional. FORBIDDEN labels (not used anywhere): attention
failure, binding failure, reasoning failure, model chose shortcut, or any mechanistic attribution.
A covariate association is a CO-OCCURRENCE rate, never a cause.
```

## 7. Hop1 scoring rule

```text
hop1-isolated. match := (predicted == ground_truth), where ground_truth is the item's correct r1-object B
token. Exact token match. Greedy decode. Scored ONCE. (Identical to the rule used in the floor-check and
composite-gate runs, so the fresh blocks are directly comparable to the anchors.)
hop2 control scored the same way against the item's r2-object C* (per item).
```

## 8. Component floor rule

```text
Per block: hop1-isolated lower Wilson 95% > 0.75  ->  the block CLEARS (hop1 admissible on that block).
                                           otherwise ->  the block FAILS.
hop2 control per block: lower Wilson 95% > 0.75 expected (it cleared on both anchors). hop2 is a CONTROL
(§9 HOP2-CONTROL-FAIL): if hop2 falls below floor on a fresh block, the hop1 read on that block is confounded.
```

## 9. Null / stability / instability branches (decided on the 6 FRESH blocks)

```text
HOP1-STABLE-ADMISSIBLE      all 6 fresh blocks CLEAR the 0.75 floor -> hop1 admissibility is consistent
                            (and the seen 097..192 failure looks anomalous relative to the fresh map).
HOP1-STABLE-INADMISSIBLE    all 6 fresh blocks FAIL the 0.75 floor -> hop1 is consistently NOT admissible
                            (and the seen 001..096 clearing looks anomalous relative to the fresh map).
HOP1-UNSTABLE               the per-block floor verdict is NOT unanimous (>=1 clears AND >=1 fails) -> hop1
                            admissibility VARIES across materializations. (This is the operative meaning of
                            "material" variation: the admissibility verdict itself flips across blocks.)
                            -> then report which §6 covariates the per-item hop1 correctness co-varies with
                               (PRIMARY P-role read first; SECONDARY descriptive).
HOP2-CONTROL-FAIL           >=1 fresh block has hop2 below the 0.75 floor -> the hop1 read is confounded on
                            that block; investigate the materialization/run before drawing a hop1 conclusion.
CONSTRUCT-FAIL              C1–C9 admissibility, prompt-conformance, or invalidated-count (>=10/96 on a block)
                            fails -> the test is invalid on that block; fix and re-pre-register.

SECONDARY (descriptive, all branches): report the per-block hop1 rate distribution (min/max/spread) and a
simple between-block variance, alongside the two anchors, as the "stability map."
```

## 10. Stop rule

```text
- Fixed: 6 blocks x N=96, seeds 193..768, the §6 covariates, the §7 scoring, the §8 floor, and the §9
  branches are declared BEFORE the fresh run and computed ONCE.
- NO adding blocks until a desired pattern (stable/unstable) appears. NO post-hoc covariate fishing beyond
  the predeclared §6 set. The CONFIRMATORY P-role read (§6 PRIMARY) is reported SEPARATELY from the
  EXPLORATORY secondary covariates (which are flagged exploratory, not confirmed).
- NO re-running until a block clears/fails. A CONSTRUCT-FAIL block is remedied by a NEW pre-registration.
```

## 11. Forbidden interpretations

```text
- NOT a mechanism claim. Covariate associations are positional/structural CO-OCCURRENCE, never cause. No
  "attention/binding/reasoning failure," no "shortcut."
- NOT a capability claim. The model performs hop1 on SOME materializations (87/96 anchor); instability is not
  "the model cannot do hop1."
- NOT "the model cannot compose" — this is HOP1-ONLY, not the composite.
- NOT a composite-gate rerun, NOT certification, NOT compression readiness, NOT Claim C, NOT Paper B.
- The seen composite-gate (097..192) result is an ANCHOR, not fresh evidence; this prereg does not re-slice
  it as a claim.
- The C0 K=5 FAIL stays CLOSED; V3 ≠ C0; this prereg does not bear on it.
- Survival is not correctness; "not ruled out" is not "established."
```

## 12. Required artifacts + tooling

```text
ARTIFACTS PRODUCED BY THE RUN: fresh items {193..768} (6 blocks); hop1 + hop2 prompts; scored results;
  per-block table (hop1/hop2 rate + Wilson + floor verdict); covariate table; stability decision JSON;
  run record (profile, seeds, once); run manifest (all artifact hashes).

REUSED UNCHANGED (digests locked): generator wrapper cc07e5a2 (≤999-enforcing; --start-index per block),
  underlying generator 6a2ceee1, realizer fb561fdc, conformance checker b8afa3f8.
NEW (named; built under a SEPARATE TL/Manager tooling-build action; SE-verified; digests LOCKED AT APPROVAL):
  path-a/build/v3_hop1_stability_analyzer.py
     intent: per-block hop1/hop2 correct rate + Wilson CI + 0.75 floor verdict; the §9 between-block branch
             (unanimity test); per-block rate distribution + between-block spread; reads the covariate log.
             Scores outputs; runs no model. deterministic; sha256 LOCKED AT APPROVAL.
  path-a/build/v3_hop1_covariate_logger.py
     intent: emit the §6 covariates per item (PRIMARY P-role flag + SECONDARY structural fields) from the
             item specs + scored hop1 results. Positional/structural only. deterministic; sha256 LOCKED AT APPROVAL.
```

## E. Execution boundary + routing

```text
This preregistration authorizes:
  No run.  No fresh materialization yet.  No prompt generation for execution.  No tooling creation.  No
  composite-gate retry.  No prompt edits to existing runs.  No post-hoc slicing of the composite-gate result
  as a claim.  No compression / INT8 / INT4.  No Claim C.  No Paper B.  No certification.  No capability
  claim.  No mechanism claim.

ROUTING (no step may be skipped):
  Senior draft (v0.1)
   -> CS files to a readable in-review path
   -> C5 claim-risk review (actual bytes)
   -> CS feasibility review
   -> TL approval consideration
   -> (separate TL/Manager TOOLING-BUILD action for the two new tools -> SE verifies tool bytes)
   -> Manager by-name RUN authorization (only if approved; fresh blocks; real-run; locked digests)
   -> CS execution
   -> SE verification

The Path A FP16 K=5 FAIL remains closed and untouched. SE drafts this prereg; SE locks nothing.
```

---

**The one to carry up:** A bounded, behavioral hop1-stability map — **not** a composite-gate rerun, certification, compression, or mechanism probe. **Question:** does hop1 admissibility (lower Wilson > 0.75) vary across fresh V3 materializations, and along which **predeclared positional/structural** covariates does hop1 correctness co-vary. **Design:** 6 fresh blocks of N=96 (seeds **193..768**, all 3-digit so MAX_DELTA=8 holds, disjoint from the used 001..192), same locked construction, **hop1 + hop2-control** only, FP16 greedy, once. The two known points (001..096 = 87/96, 097..192 = 28/96) are **anchors only**; the branch is decided on the **fresh** blocks (lock-before-look). **Primary metric:** per-block hop1 floor verdict; **stability = unanimity** of that verdict across the 6 blocks (UNSTABLE if it straddles). **Covariates:** one **confirmatory** (the P-role-distractor landing, suggested by the seen result, tested fresh) + the rest **exploratory/descriptive** (guarding against covariate fishing). **Branches:** STABLE-ADMISSIBLE / STABLE-INADMISSIBLE / UNSTABLE / HOP2-CONTROL-FAIL / CONSTRUCT-FAIL. **Forbidden:** mechanism, capability, "can't compose," certification, compression, Claim C, Paper B, composite-gate rerun, C0 reopening; covariate associations are co-occurrence, never cause. Two new tools (stability analyzer + covariate logger) named, built under a **separate** TL/Manager action; wrapper/realizer/checker reused unchanged. Authorizes no run, materialization, or tooling. Routes per TL's block. FP16 K=5 FAIL closed.

— Senior Engineer (hop1 stability prereg v0.1; routes for CS filing, C5 claim-risk, CS feasibility)
