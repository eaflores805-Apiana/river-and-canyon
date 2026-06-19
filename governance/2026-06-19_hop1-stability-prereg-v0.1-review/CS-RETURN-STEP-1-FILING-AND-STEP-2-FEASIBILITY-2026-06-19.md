# CS RETURN — Hop1 Stability Prereg v0.1: Step 1 (PASS — Filed) + Step 2 (PASS — Feasible with notes)

**Date:** 2026-06-19
**From:** CS Engineer
**To:** Team Lead; Cc: Senior Engineer, C5, Manager
**Re:** TL ACTION 2026-06-19 — "File and Review Hop1 Stability Preregistration v0.1"
**Status:** **STEP 1 PASS — v0.1 filed. STEP 2 PASS — feasible with two implementation notes for the tooling-build action.**

---

## Record status

```text
artifact under review     path-a/in-review/PREREGISTRATION-HOP1-STABILITY-PATH-A-v0.1.md
                           sha256 71f00482e1d94bd7fb06a5068391a7977a4b71d9baac690b286511d29e052c26
authority                 TL ACTION 2026-06-19 ("File and Review Hop1 Stability
                           Preregistration v0.1")
Step 1 (filing)           PASS — v0.1 filed verbatim at TL-preferred path
Step 2 (feasibility)      PASS-with-notes — feasible as written; two minor
                           implementation clarifications recommended for the
                           subsequent tooling-build action (N1: realizer's
                           4-context default vs prereg's 2-context scope;
                           N2: §9 branch-priority order when multiple
                           conditions fire on the same set of blocks)
C5 lane                   parallel; not gated on CS
```

---

## Step 1 — Filing return fields (per TL ACTION)

```text
commit                       to be recorded in §3 once it lands
final remote HEAD            to be recorded in §3 once push completes
filed path                   path-a/in-review/PREREGISTRATION-HOP1-STABILITY-PATH-A-v0.1.md
                             (exactly TL's preferred path; the inbox source had the
                              same name, so no rename was applied at filing)
sha256 digest                71f00482e1d94bd7fb06a5068391a7977a4b71d9baac690b286511d29e052c26
clean-fetch confirmation     to be recorded in §3 after `git fetch origin` + per-file
                             verification

bytes match Senior v0.1 source            YES.
  Inbox source sha:                        71f00482e1d94bd7fb06a5068391a7977a4b71d9baac690b286511d29e052c26
  Filed destination sha (after cp):        71f00482e1d94bd7fb06a5068391a7977a4b71d9baac690b286511d29e052c26
                                                                                            ^ identical

confirmation C5 can access the object     YES via the standing review-track mechanism
                                           (path-a/in-review/README.md §Provenance +
                                            contributors clean-fetch path). C5 can
                                            `git fetch origin && git cat-file -p
                                            origin/main:path-a/in-review/PREREGISTRATION
                                            -HOP1-STABILITY-PATH-A-v0.1.md` for
                                            byte-identical Senior content.
```

---

## Step 2 — CS feasibility review

### Verdict: **PASS — executable as written, with two implementation notes for the tooling-build action**

The prereg is well-structured: bounded as a behavioral hop1-stability map (not a composite-gate rerun, certification, mechanism probe, or compression test); fresh disjoint seed range explicitly locked; anchors {001..096} and {097..192} correctly bounded as descriptive context (not fresh evidence); confirmatory hypothesis (P-role distractor landing) cleanly separated from descriptive secondary covariates; forbidden-interpretations carry forward from v0.4 / v0.2 verbatim; the two new tools are named for a separate TL/Manager tooling-build action.

CS notes two minor implementation clarifications that the tooling-build action should resolve. Neither is a HOLD blocker.

### 1. CS focus answers (the eight from TL ACTION)

#### 1.1 Seed ranges 193..768 — available, 3-digit, disjoint, mechanically realizable

**YES — confirmed by inspection of the wrapper + the per-item-prefix scheme.**

```text
seed range                  193 … 768  (6 contiguous blocks of 96)
max index                   768 ≤ 999 → 3-digit prefix preserved
                                       → MAX_DELTA = 8 binding holds
disjoint from used          {193..768} ∩ {001..192} = ∅ (193 > 192 — provable by interval)
mechanical realizability    wrapper v3_composite_gate_item_generator.py (sha cc07e5a2…)
                            accepts --start-index N + --count 96; one invocation
                            per block (F1..F6). The wrapper's ≤999 invariant
                            is structurally guarded; 6 blocks at 96 items each
                            fit comfortably (max index 768 < 999).
```

#### 1.2 Scale — 1,152 prompts feasible

**YES — well within the same execution envelope as the floor-check + composite-gate runs.**

```text
items                       576 (6 blocks × 96)
prompts (hop1 + hop2 only)  1,152 (2 contexts × 576 items)
inference time estimate     at the floor-check / composite-gate steady-state rate
                             of ~1.27 prompt/s on M2 Max + FP16 Qwen2.5-3B greedy:
                              1,152 × ~0.79 s ≈ 15 minutes inference
                              (+ ~10 s model load; ~30 s build prep × 6 blocks)
disk + I/O                   ~3,500 files across items + admissibility + prompts +
                             scored; aggregate ~few MB; comparable to two prior
                             runs combined; no environment concerns

  NOTE: see §1.3 below — the existing realizer renders ALL FOUR contexts per
  item, not just hop1+hop2. If reused unchanged, the actual rendered prompt
  count is 2,304 (4 × 576), of which 1,152 would be executed and the other
  1,152 simply unused. Either is feasible; this is the "implementation note
  N1" for the tooling-build action.
```

#### 1.3 Reused tooling — wrapper / generator / realizer / checker reused unchanged?

**4/4 reusable BYTES UNCHANGED with one implementation-note caveat (N1) on the realizer's default behavior.**

```text
wrapper       v3_composite_gate_item_generator.py    cc07e5a2…  REUSABLE — handles
                                                                 --start-index per block;
                                                                 ≤999 enforcement preserves
                                                                 MAX_DELTA=8
generator     v3_item_generator.py                   6a2ceee1…  REUSABLE — underlying,
                                                                 unchanged
realizer      v3_prompt_realizer.py                  fb561fdc…  REUSABLE-WITH-NOTE-N1:
                                                                 renders ALL FOUR contexts
                                                                 (composite/hop1/hop2/dq)
                                                                 unconditionally; prereg §3
                                                                 says "realize the HOP1
                                                                 context (primary) and the
                                                                 HOP2 context (control). dq/
                                                                 composite NOT run." See N1.
conformance   v3_prompt_conformance_checker.py        b8afa3f8…  REUSABLE — pure function of
                                                                 (specs, prompts); works on
                                                                 whichever subset of contexts
                                                                 is rendered
inspector     path-a/inspector/inspector.py           cb4b0b60…  REUSABLE — schema-level
constants     path-a/inspector/constants.py           1d761c3d…  REUSABLE — locked values
```

**Implementation note N1 (for the tooling-build action; NOT a feasibility blocker):**

The existing realizer's `realize_item()` returns a 4-context prompt set unconditionally; there is no `--contexts` flag. Prereg §3 specifies hop1+hop2 only. Three resolution paths, all bounded:

```text
N1.A   Accept "render all 4, execute only hop1+hop2": existing realizer reused
       UNCHANGED; 2,304 prompts are rendered but only 1,152 (hop1+hop2) are
       executed against the model. Inference cost goes from ~15 to ~30 minutes,
       still feasible. Cleanest at the tooling layer.

N1.B   Add a `--contexts` flag to v3_prompt_realizer.py (additive; default
       all-4 preserves existing behavior). Generator-style "additive patch":
       realizer digest changes (fb561fdc → new). v0.1 §12's "REUSED UNCHANGED"
       claim for the realizer would need a small textual update (rebind to the
       new sha at TL approval).

N1.C   Build a wrapper realizer v3_hop1_stability_prompt_realizer.py that
       imports realize_item() and writes only hop1+hop2 to disk. Underlying
       realizer unchanged; new wrapper digest locked alongside the analyzer
       and covariate logger.

CS does not recommend a specific option; Senior or the tooling-build ACTION
picks one. **N1.A is the smallest-touch option** and lets the existing
"REUSED UNCHANGED" claim stand literally; the cost is doubled inference
time, which is still under 30 minutes.

This is a clarification, not a blocker. The prereg is feasible under any of
the three options.
```

#### 1.4 New tooling — `v3_hop1_stability_analyzer.py` + `v3_hop1_covariate_logger.py` feasible

**YES — both feasible as deterministic pure-function scripts.**

```text
v3_hop1_stability_analyzer.py
  intent (per §9):
    - per-block hop1 + hop2 correct rate + Wilson 95% CI
    - per-block 0.75 floor verdict (CLEARS/FAILS)
    - between-block branch selector (STABLE-ADMISSIBLE / STABLE-INADMISSIBLE /
      UNSTABLE / HOP2-CONTROL-FAIL / CONSTRUCT-FAIL)
    - per-block rate distribution + between-block spread (descriptive)
    - reads covariate log from v3_hop1_covariate_logger
  scale:    ~200 lines; same template as v3_composite_gate_analyzer.py
  contract: pure function; no model imports; deterministic
  digest:   LOCKED AT APPROVAL

v3_hop1_covariate_logger.py
  intent (per §6):
    - PRIMARY: predicted_is_P_role_distractor flag per item (predicted ∈ {d.head
      for d in spec.decoy_chains}; the "P" tokens)
    - SECONDARY descriptive: block, target B, predicted (identity + role class),
      r1 identity, relation position, fact-line position, distance-from-QUERY,
      prompt char count, token-width class, distractor role class
  scale:    ~200 lines; same template as build_r6_log.py + extra columns
  contract: pure function; no model imports; deterministic
  digest:   LOCKED AT APPROVAL
```

All inputs (item specs + scored hop1/hop2 outputs) are already produced by the
existing tools at known schemas. Both new tools follow the established floor-
check / composite-gate tooling pattern. **FEASIBLE.**

#### 1.5 Scoring — hop1 + hop2 exact-match computable

**YES — already implemented and verified.**

```text
Per the established run_step_6.py pattern (executed for both prior runs):
  predicted = first identifier-like token from the model's response, regex
              [A-Za-z][\w]* via _extract_predicted()
  match     = (predicted == ground_truth)
  ground_truth(hop1) = spec.target.B   (the r1-object)
  ground_truth(hop2) = spec.target.C_star  (the r2-object)

Same scoring rule as floor-check + composite-gate runs → fresh blocks are
directly comparable to the anchors at the score level. Mechanical and
deterministic.
```

#### 1.6 Covariates — mechanically extractable

**YES — all PRIMARY + 10 SECONDARY covariates from spec/prompts/scored.**

```text
PRIMARY (confirmatory):
  predicted_is_P_role_distractor    predicted ∈ {d.head for d in spec.decoy_chains}
                                    (the P_1..P_5 tokens; mechanically determinable)

SECONDARY (descriptive):
  seed/index block                  ((item_index - 1) // 96) + offset (deterministic)
  target B token                    spec.target.B (and its char width)
  predicted (identity, role class)  scored.predicted + match against role-token namespaces:
                                    {C_star, B, T, T_i_*, X_*, B_competitor_*, decoy P/Q/S,
                                     neutral pool, otherwise = "free-form"}
  relation token identity (r1)      spec.target.r1
  relation position                 always slot 0 in head_relations (constant per scheme)
  fact-line position of target hop1 always index 0 in the realizer's fact list (constant)
  distance from QUERY line          number of fact lines or character distance (computable
                                    from prompt text)
  prompt char count                 len(prompt) (already recorded in realization_summary)
  token-width class                 char width of role tokens; bucketed (e.g., {6, 7})
  competitor/distractor role class  match against {X_i, B_i, P_i, Q_i, S_i, T_i, ...} sets

All covariates are POSITIONAL/STRUCTURAL functions of (spec, prompt, scored output).
No covariate references mechanism (attention, binding, reasoning, shortcut) —
per §6 the forbidden labels are explicitly excluded from the logger.
```

**FEASIBLE.**

#### 1.7 Branches mechanically computable

**YES — deterministic between-block synthesis on top of per-block verdicts.**

```text
per-block compute (each F1..F6):
  hop1_lower_wilson > 0.75  →  block CLEARS (else FAILS)
  hop2_lower_wilson > 0.75  →  hop2 admissible on block (else flagged for confound)
  C1-C9 96/96 + conformance 96/96 + invalidated < 10  →  construct clean

between-block branch (deterministic):
  CONSTRUCT-FAIL          IF any block fails C1-C9 OR conformance OR invalidated ≥10
  HOP2-CONTROL-FAIL       IF any block has hop2 below 0.75 (confound flag)
  STABLE-ADMISSIBLE       IF all 6 blocks CLEAR hop1 (and the above two checks pass)
  STABLE-INADMISSIBLE     IF all 6 blocks FAIL hop1 (and CONSTRUCT-FAIL + HOP2 are OK)
  UNSTABLE                IF at least one CLEARS and at least one FAILS

Each is a deterministic predicate on per-block scored outputs + admissibility +
conformance + invalidated counts. Mechanically computable; deterministic.
```

**Implementation note N2 (for the tooling-build action; NOT a blocker):**

The prereg §9 does not explicitly state a **priority order** among the five branches when multiple trigger conditions fire on the same set of blocks (e.g., one block has hop2 below floor AND another block has hop1 unanimity failing). The analyzer needs a precise priority order. CS proposes:

```text
1. CONSTRUCT-FAIL (any block with C1-C9 / conformance / invalidated fail) — highest priority
2. HOP2-CONTROL-FAIL (any block with hop2 below floor) — confound flag
3. STABLE-ADMISSIBLE / STABLE-INADMISSIBLE / UNSTABLE — based on per-block hop1
   verdicts, only meaningful when (1) and (2) pass

Rationale: CONSTRUCT-FAIL means the block's data is invalid, so a stability
verdict on it would be meaningless; HOP2-CONTROL-FAIL means the hop1 read is
confounded; the stability test only runs on blocks that pass both checks.
```

Senior may want to lock this priority order in v0.2, or delegate to the
analyzer's documented behavior at tooling-build time. CS notes that the
prereg as written DOES support the above priority by reasonable reading;
it just isn't explicit.

#### 1.8 No hidden execution

**CONFIRMED — §E + §12 explicit.**

```text
§E verbatim: "This preregistration authorizes:
  No run.  No fresh materialization yet.  No prompt generation for execution.
  No tooling creation.  No composite-gate retry.  No prompt edits to existing
  runs.  No post-hoc slicing of the composite-gate result as a claim.  No
  compression / INT8 / INT4.  No Claim C.  No Paper B.  No certification.
  No capability claim.  No mechanism claim."

§12 explicit: new tools "built under a SEPARATE TL/Manager tooling-build
action; SE-verified; digests LOCKED AT APPROVAL"

This filing turn (CS review + C5 review on bytes) is review-only.
```

### 2. TL watchpoint answers (the four)

#### A. Is 6 fresh blocks the right fixed size?

**CS recommendation: 6 is appropriate.** Rationale:

```text
- 6 fresh + 2 anchors = 8 materializations: enough resolution to detect
  unanimity vs straddle without an unbounded sweep.
- Inference cost at FP16/M2 Max steady-state (~1.27 prompt/s) is ~15 min for
  1,152 prompts (or ~30 min if all 4 contexts rendered+executed per N1.A).
  Manageable.
- Spread metrics (between-block variance) work better with 6 than with 4
  (smaller samples give noisier between-block spread estimates).
- The prereg explicitly says "Block count / N are a PROPOSAL; TL/Manager may
  size up or down. Up to ~8 blocks of 96 fit within ≤999." Sizing flexibility
  is built in.

If TL/Manager prefers smaller: 4 blocks still permits the unanimity test
(STABLE / UNSTABLE branches still work at 4) but reduces between-block-spread
precision. CS does not recommend reducing below 4.
```

#### B. Is "stability = unanimous floor verdict across fresh blocks" claim-safe and mechanically clear?

**YES — both.**

```text
mechanically clear   each block has a deterministic boolean floor verdict
                     (Wilson lower > 0.75). The unanimity test is just
                     AND(all CLEAR) / AND(all FAIL) / otherwise UNSTABLE.
                     No fuzzy thresholds; no judgment calls.

claim-safe           "stability" here means "the per-block floor verdict is
                     consistent across materializations." This is a positional/
                     structural fact about admissibility — NOT a claim about
                     model reasoning or capability (per §11: "NOT a capability
                     claim. The model performs hop1 on SOME materializations
                     (87/96 anchor); instability is not 'the model cannot do
                     hop1.'"). The branch language correctly stays at the
                     materialization level.
```

#### C. Is the P-role confirmatory hypothesis stated narrowly enough?

**YES.**

```text
- The hypothesis is exactly one mechanical predicate: predicted_is_P_role_distractor
  (predicted ∈ decoy_chain heads {P_1, ..., P_5}). No ambiguity.
- The prereg distinguishes SOURCE from EVIDENCE: "Observation on the seen
  097..192 data: wrong hop1 predictions landed on the 'P' role token … This is
  the SOURCE of the §6 PRIMARY covariate hypothesis — tested on FRESH blocks,
  not asserted from the seen data" (§2) and "The §6 PRIMARY covariate (P-role
  landing) was SUGGESTED by the seen 097..192 result; it is pre-declared here
  and CONFIRMED-OR-NOT on the FRESH blocks. The seen P-landing is NOT the
  evidence; the fresh blocks are." (§4)
- This is correctly a confirmatory hypothesis (suggested by seen data, tested
  on fresh data), not a fishing-driven claim. The reporting framing in §10
  also requires reporting "the CONFIRMATORY P-role read (§6 PRIMARY) SEPARATELY
  from the EXPLORATORY secondary covariates" — preventing inadvertent fishing.
```

#### D. Is hop2-control failure handled safely?

**YES.**

```text
§9 HOP2-CONTROL-FAIL: "≥1 fresh block has hop2 below the 0.75 floor → the hop1
read is confounded on that block; investigate the materialization/run before
drawing a hop1 conclusion."

This:
- DOES bound the failure as a confound flag on the affected block, not a
  broader "the model can't do hop2" claim.
- DOES NOT turn the investigation into a wider component-stability study
  (the prereg's scope is still hop1 stability; hop2 is the CONTROL).
- DOES require investigation BEFORE drawing a conclusion — preventing a
  hasty "hop2 broken on block X" finding.

The prereg correctly handles hop2 control failure as a flag, not as a
new claim surface. Safe.
```

---

## 3. Required edits / notes

```text
N1 (TOOLING-BUILD ACTION NOTE, NON-BLOCKING)
   Existing realizer renders all 4 contexts; prereg §3 specifies hop1+hop2 only.
   Tooling-build action picks one of: N1.A accept render-4-execute-2 (existing
   realizer reused unchanged); N1.B additive --contexts flag (realizer digest
   changes); N1.C wrapper realizer (new lockable digest, underlying unchanged).
   CS does not recommend a specific option; N1.A is the smallest-touch option.

N2 (TOOLING-BUILD ACTION NOTE, NON-BLOCKING)
   §9 branch priority order is not explicit when multiple trigger conditions
   fire. CS proposes priority: (1) CONSTRUCT-FAIL > (2) HOP2-CONTROL-FAIL >
   (3) STABLE-ADMISSIBLE / STABLE-INADMISSIBLE / UNSTABLE. Senior may lock
   the priority in v0.2 or delegate to analyzer's documented behavior at
   tooling-build time.

Neither note is a HOLD blocker. The prereg is feasible-as-written under
either resolution path for both notes.
```

## 4. What this PASS does NOT mean

```text
Does NOT authorize anything operational:
  no run; no fresh materialization; no prompt generation for execution;
  no tooling creation (the 2 new tools require separate TL/Manager
  tooling-build action); no compression; no Claim C / Paper B /
  certification / capability / mechanism claims.

Does NOT alter any boundary established by prior reviews:
  - V3 composite-gate PRECONDITION-FAIL stands as a valid outcome
  - The hop1 swing 87/96 → 28/96 is the recorded data; mechanism not
    decidable from prior runs
  - V3 ≠ C0; K=5 FAIL stays closed

Does NOT make any of the forbidden claims:
  per §11 the hop1 stability investigation is bounded as positional/
  structural; covariate associations are co-occurrence, never cause;
  no mechanism, no capability, no certification, no composition claim.
```

## 5. Clean-fetch confirmation

Performed after the commit landed; `git fetch origin` immediately preceded the verification.

```text
commit                       b757f4d64a9f1c97dde7e9647d21edaa98957f90
push                         9744e0e..b757f4d  main -> main
origin/main HEAD             b757f4d64a9f1c97dde7e9647d21edaa98957f90
local       HEAD             b757f4d64a9f1c97dde7e9647d21edaa98957f90   (match)

per-file verification (origin/main bytes → local bytes):

MATCH  path-a/in-review/PREREGISTRATION-HOP1-STABILITY-PATH-A-v0.1.md
       (71f00482…; matches TL-cited Senior source byte-for-byte)
MATCH  path-a/in-review/C5-V3-COMPOSITE-GATE-PREREG-CLAIM-RISK-v0.2-BYTEREVIEW.md
       (9d042b6d…; C5 PASS on v0.2 bytes)
MATCH  path-a/in-review/V3-COMPOSITE-GATE-RUN-SE-VERIFICATION-RETURN-v0.1.md
       (0eb0edcb…; SE PASS on PRECONDITION-FAIL run)
MATCH  path-a/in-review/V3-COMPOSITE-GATE-TOOLING-VERIFICATION-SE-RETURN-v0.1.md
       (c97f98b0…; SE PASS on composite-gate tooling)
MATCH  path-a/in-review/README.md
MATCH  governance/2026-06-19_hop1-stability-prereg-v0.1-review/TL-ACTION-FILE-AND-REVIEW-HOP1-STABILITY-V0.1-2026-06-19.md
MATCH  governance/2026-06-19_hop1-stability-prereg-v0.1-review/CS-RETURN-STEP-1-FILING-AND-STEP-2-FEASIBILITY-2026-06-19.md
       (this file, PRIOR to the §5 commit)
```

All 7 listed artifacts reproduce byte-exact from the shared repository on a clean fetch. **CS Step 1 (filing) + Step 2 (feasibility PASS-with-notes) FILED.**

---

— CS Engineer, 2026-06-19 (clean-fetch appendix)

---

## Non-authorizations (carried forward)

```text
- run                                      blocked
- fresh materialization                    blocked
- prompt generation                        blocked
- tooling creation                         blocked (2 new tools require SEPARATE
                                                    TL/Manager tooling-build ACTION)
- composite-gate retry                     blocked
- compression / INT8 / INT4                blocked
- Claim C, Paper B                         blocked
- certification claim                      blocked
- capability claim, mechanism claim        blocked
- candidate selection, threshold values, multi-model, Fork A reactivation,
  public benchmark packaging, artifact mutation, Paper 6, Paper 3 execution
  as experiment                            all carried per standing card

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc…) + tagged manuscript
  blob (7d6706a3…)                         never moved
- tier0-run/ directory                     sealed; no new files

The Path A FP16 K=5 FAIL remains closed. V3 ≠ C0.
```

---

— CS Engineer, 2026-06-19
