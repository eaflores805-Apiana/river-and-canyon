# PREREGISTRATION — V3 COMPOSITE CERTIFICATION (Path A) v0.1

**E. A. Flores**, Apiana AI, Inc. — June 18, 2026
*River and Canyon · Path A. Drafted by the Senior Engineer (lock-before-look). Routes for review and approval; SE locks nothing and authorizes no run.*

> **Framing.** The V3 floor check established **component-admissibility-under-competition** for hop2 at the locked K=5 load (SE-verified, return `03d2ead8…`). This prereg asks the **next, separate** empirical question: does the full two-hop **composite** clear a predeclared **certification** gate? A cleared gate would certify composition **on this construction, at this load, with this model — and nothing more** (§9). **A composite that does not clear is a valid outcome**, never a license to lower the gate.

> **CRITICAL — lock-before-look (read first).** The floor-check run already computed the composite (80/96 = 0.833) **as informational**. That data is **already seen**. A certification gate evaluated against *that same data* would be declared *after* the result is known — **not** lock-before-look. Therefore **certification requires a FRESH run** (new seeds, same locked V3 construction, N=96), with the gate locked **before** the fresh composite is generated. The seen 0.833 is a prior expectation only; it is **not** certification data (§3).

## 1. Component admissibility — ALREADY ESTABLISHED (a precondition, not re-litigated here)

```text
From the V3 floor check (SE-verified, byte-identical analyzer decision 6a34f6dc…):
  hop2-isolated 96/96 = 1.000, Wilson lower 0.9615 > 0.75   -> CLEARS (admissible under competition)
  hop1-isolated 87/96 = 0.906, Wilson lower 0.8313 > 0.75   -> CLEARS
  direct-query C* count 0  (no direct-recall shortcut); invalidated 0; admissibility 96/96; conformance 96/96
This is a PRECONDITION carried into certification. It is NOT re-opened or re-argued here. (It must,
however, be RE-CONFIRMED on the FRESH certification set — §6 — since the fresh items are new data.)
```

## 2. The certification question (the NEW empirical question)

```text
PRIMARY:  On a FRESH N=96 materialization of the locked V3 construction, does the full two-hop COMPOSITE
          (A -r1-> B -r2-> C*) clear the predeclared composite-certification gate (§7), given that the
          components are admissible under competition?
```

The composite test presents the whole problem (find the r2 of the r1 of A). Certification asks whether the model produces the correct C\* **via the correct chain** reliably enough — with foreclosed non-traversal routes (V3 design), controlled direct-recall (dq), and admissible components — to certify two-hop composition on this construction.

## 3. Composite score interpretation (and why the seen composite is NOT certification data)

```text
- The floor-check composite (80/96 = 0.833, Wilson95 [0.7463, 0.8947]) is INFORMATIONAL and ALREADY SEEN.
  It is NOT the certification datum. Using it as certification would violate lock-before-look (gate set
  after result known). It serves ONLY as a prior expectation (~0.83).
- CERTIFICATION METRIC (on the FRESH set): composite-correct rate = (# items whose composite context returns
  the correct target C* VIA THE CORRECT CHAIN) / (post-exclusion denominator). Scored against the fresh
  materialized ground truth (the target chain's C*; a decoy-chain C does NOT count as correct).
- Reported with its Wilson 95% CI. The lower bound is the gate input (§7). NOT collapsed with the components.
```

## 4. Invalidator handling (same item/set rules as the floor check)

```text
ITEM-LEVEL R6: if an item-level R6 invalidator fires (the five non-circular ones: terminal-coincidence,
  controls-unavailable, direct-recall, interior-position, constant-token), the item is EXCLUDED from the
  validated numerator and LOGGED.
SET-LEVEL R6: invalidated count <= 9/96 tolerated; >= 10/96 -> CONSTRUCT-FAIL / MIS-SPECIFIED (§8).
"BELOW-GATE" CLARIFICATION (avoid circularity): composite-below-gate is NOT an item-level invalidator; it is
  the PRIMARY composite OUTCOME (§7/§8). The primary metric does not invalidate its own items. Item-level
  "below-floor" refers only to construction-admissibility caught by C1–C9.
```

## 5. Same-error / wrong-address logging (composition-specific control)

```text
For every composite ERROR (wrong or absent C*), log:
  WHERE IT LANDS:
    - correct chain, wrong depth (e.g., returns B, or the terminal)        }
    - DECOY chain, depth-2 (an off-map "right depth, wrong chain" C)        }  characterized, reported
    - a competitor / other token                                            }
  CO-OCCURRENCE:
    - does the composite error occur on an item whose hop2-isolated ALSO failed (INHERITED component
      failure) or whose hop2 SUCCEEDED (COMPOSITION-SPECIFIC failure — the components work but the chain
      does not)?
PURPOSE: this is a CONTROL on the certification, not the primary metric. It does not change the §7 gate.
  But pathological patterns are FLAGGED, e.g.:
    - if composite "successes" are not correct-chain (coincidental C*), certification is invalid;
    - heavy DECOY-depth-2 landing among errors is the off-map signature (recorded as data, not mechanism).
NOTE: characterization is POSITIONAL/structural. WHY the model errs (traversal vs grab vs anchor) is NOT
  decidable here and is NOT claimed.
```

## 6. Direct-query and control preservation (on the FRESH set — not assumed from the prior run)

```text
On the FRESH N=96, BEFORE the composite gate is read, re-confirm (the components must be admissible on the
NEW items, not inherited from the floor-check run):
  - direct-query control: dq C* count <= 19/96 (no direct-recall on the fresh items) — point count.
  - hop2-isolated: lower Wilson 95% > 0.75 (component still admissible under competition on fresh items).
  - hop1-isolated: lower Wilson 95% > 0.75.
  - C1–C9 admissibility: 96/96 PASS in real-run mode (fresh items).
  - prompt-realization conformance: 96/96 PASS, including the <= 8 char delta (fresh prompts).
  - dominance control: DOMINANT_RATE_THRESHOLD = 0.25 on the composite off-target mass (flagged, not pass/fail).
If any precondition fails on the fresh set -> PRECONDITION-FAIL (§8): the fresh set is not on admissible
ground; the composite gate is NOT read, and the cause is examined (re-materialize / re-pre-register).
```

## 7. Decision rule (computed once by the named certification analyzer, on the FRESH run)

```text
COMPOSITE-CERTIFICATION-GATE-CLEARED (this run) requires ALL of:
  (a) PRIMARY reliability bar: composite-correct lower Wilson 95% > 0.75
       (the SAME strict reliability standard the components were held to; SE-proposed, LOCKED AT APPROVAL);
  (b) NECESSARY not-shortcut floor: composite-correct lower Wilson 95% > 0.45 (= F + margin)
       (a composite below this is achievable by foreclosed non-traversal routes; necessary, not sufficient);
  (c) PRECONDITIONS hold on the fresh set: hop2 admissible, hop1 admissible, dq <= 19/96 (§6);
  (d) CONSTRUCT clean on the fresh set: C1–C9 96/96, prompt-conformance 96/96, invalidated <= 9/96;
  (e) ERROR-STRUCTURE non-pathological: composite "successes" are correct-chain (§5).
  -> THEN: the composite clears the certification gate ON THIS RUN. (Whether FINAL certification requires
     replication is a Manager/standard decision — see §9; SE recommends at least one confirmation.)

THRESHOLD TRANSPARENCY (lock-before-look honesty): 0.75 is chosen on PRINCIPLE (the component reliability
standard), NOT relative to the seen 0.833. The seen composite's lower bound (0.7463) sits JUST BELOW 0.75,
so the fresh-run result is GENUINELY UNCERTAIN — it may clear or may fail. The threshold is NOT set to
guarantee a pass, and a failure (§8) is a real, valid outcome.
```

## 8. Failure / null branches

```text
COMPOSITE-DOES-NOT-CERTIFY-THIS-RUN (clean construct, components admissible, gate not cleared):
  composite-correct lower Wilson <= 0.75 while (b)–(e) hold -> the composite is NOT reliable enough to
  certify two-hop composition at this load. A VALID outcome. NEVER a license to lower the 0.75 bar, change
  the construction, or tune to the data. (If it clears 0.45 but not 0.75: "not explained by foreclosed
  shortcuts, but not reliably composing" — recorded as such.)

PRECONDITION-FAIL (components not admissible on the fresh set):
  hop2 or hop1 below floor, or dq >= 20/96, on the FRESH items -> the fresh set is not on admissible ground;
  the composite gate is NOT read. Examine (re-materialize / re-pre-register). NOT a composite conclusion.

CONSTRUCT-FAIL (invalid test, not a substrate/composition result):
  invalidated >= 10/96, OR C1–C9 admissibility fails, OR prompt-conformance fails, OR error-structure is
  pathological (successes not correct-chain) -> the TEST is invalid. Fix and re-pre-register.
```

## 9. Forbidden interpretations

```text
- Even a CLEARED gate certifies COMPOSITION on V3, at K=5, with Qwen2.5-3B-Instruct (FP16, greedy) — and
  NOTHING beyond that. NOT general composition capability, NOT mechanism, NOT compression-survival, NOT
  Claim C, NOT Paper B.
- A single cleared run = GATE-CLEARED-THIS-RUN. Whether FINAL certification requires replication is a
  Manager/standard decision. SE RECOMMENDS at least one confirmation run (or a pre-registered robustness
  condition) before "certified" is called FINAL — mirroring the program's discipline that substrate-
  infeasibility requires REPEATED failures. Strong claims in both directions require more than one run.
- The floor-check composite (0.833) is INFORMATIONAL / already-seen and is NOT certification data.
- NO reuse of the floor-check run as certification (it was a component-admissibility run; certification is
  a fresh, separately-gated run).
- NO mechanism claim (the §5 error structure is positional/data, not "why").
- Survival is not correctness: a composite "success" counts only if it is the correct C* via the correct
  chain, controls clearing, no invalidator. "Not ruled out" is not "established."
- The C0 K=5 FAIL stays CLOSED; V3 ≠ C0; this prereg does not bear on it.
```

## 10. Stop rule

```text
- N fixed at 96 (FRESH materialization, new seeds). The gate, the thresholds (0.75 primary, 0.45 floor),
  the §6 preconditions, the §7 rule, and the certification-analyzer digest are fixed BEFORE the fresh run
  and computed ONCE.
- NO post-hoc threshold adjustment, NO slicing, NO re-running until it passes, NO tooling edit after data.
- A construct-fail (§8) is remedied by a NEW pre-registration, not a re-analysis.
- FINAL certification (vs gate-cleared-this-run) is a separate determination per §9, not this single run.
```

## T. Tooling (named; new tooling built under a SEPARATE TL/Manager action; existing tooling reused unchanged)

```text
REUSED UNCHANGED (digests already locked; re-used on the fresh set):
  v3_prompt_realizer.py            fb561fdc…   v3_prompt_conformance_checker.py  b8afa3f8…
  v3_neutral_token_pool.md         bc2020c2…   inspector.py cb4b0b60… / constants.py 1d761c3d…
  v3_item_generator.py             6a2ceee1…   (re-run with FRESH seeds for the new N=96)

NEW (named here; built under a SEPARATE TL/Manager tooling-build action; SE-verified; digest LOCKED AT APPROVAL):
  path-a/build/v3_composite_certification_analyzer.py
     intent:   compute composite-correct rate + Wilson CI, evaluate the §7 gate, re-confirm §6 preconditions,
               apply §4 invalidator rules, emit the §7/§8 branch. Scores outputs; runs no model.
     inputs:   per-context scored results (composite/hop1/hop2/direct_query) for the FRESH N=96; ground truth;
               R6 log; admissibility + prompt-conformance summaries; the §5 error-structure log.
     outputs:  single JSON: composite-correct rate + Wilson CI; gate conditions (a)-(e); precondition re-confirm;
               final branch (GATE-CLEARED-THIS-RUN / COMPOSITE-DOES-NOT-CERTIFY / PRECONDITION-FAIL / CONSTRUCT-FAIL).
     deterministic; sha256 LOCKED AT APPROVAL.
  path-a/build/v3_composite_error_logger.py
     intent:   produce the §5 same-error / wrong-address characterization (where errors land; inherited vs
               composition-specific) from the scored composite + hop1/hop2 results + ground truth.
     deterministic; sha256 LOCKED AT APPROVAL.
```

## E. Execution boundary + routing

```text
This preregistration authorizes:
  No new run.  No rerun.  No fresh materialization yet.  No prompt generation for execution.  No model run.
  No compression / INT8 / INT4.  No prompt edits.  No floor adjustment.  No tooling edit after data.
  No Claim C.  No Paper B.  No certification claim (certification only if the §7 gate clears on the fresh run).
  No capability claim.  No mechanism claim.

ROUTING (no step may be skipped):
  Senior draft
   -> CS feasibility review
   -> C5 claim-risk review
   -> TL approval
   -> (separate TL/Manager TOOLING-BUILD action for the two new analyzers -> SE verifies tool bytes)
   -> Manager by-name RUN authorization (fresh certification run; real-run assertion; locked digests)
   -> CS execution
   -> SE verification

The Path A FP16 K=5 FAIL remains closed and untouched. SE drafts this prereg; SE locks nothing.
```

---

**The one to carry up:** This locks the composite-certification question as a **fresh, separately-gated run** — because the floor-check composite (0.833) is **already-seen and cannot be certification data** (lock-before-look). Component-admissibility (hop2/hop1 clear, dq controlled) is a **precondition carried from the floor check** and must be **re-confirmed on the fresh set**, not inherited. **Primary metric:** composite-correct rate (correct C\* via the correct chain), reported alone with its Wilson CI. **Certification gate (proposed, locked at approval):** composite-correct lower Wilson 95% **> 0.75** (the component reliability standard) — with a necessary **> 0.45** not-shortcut floor, the §6 preconditions holding on the fresh set, a clean construct, and **non-pathological error structure** (§5 same-error/wrong-address logging). **Transparency:** 0.75 is chosen on principle, not relative to the seen 0.833 whose lower bound (0.7463) sits just below it — so the result is genuinely uncertain and **a failure is a valid outcome**. **Failure branches:** composite-does-not-certify-this-run (clean, gate not cleared — valid, not a license to lower the bar), precondition-fail, construct-fail. **Forbidden:** even a cleared gate certifies composition **on V3, at K=5, with this model only** — not capability, mechanism, compression, Claim C, or Paper B; a single cleared run is **gate-cleared-this-run**, and SE recommends **at least one confirmation** before FINAL certification (mirroring substrate-infeasibility's repeated-failure requirement); no reuse of the floor-check as certification. New tooling (a composite-certification analyzer + an error-structure logger) is **named and built under a separate TL/Manager action**; the realizer/checker/neutral-pool are **reused unchanged**. Authorizes no run, no materialization, no tooling creation. Routes SE-draft → CS feasibility → C5 claim-risk → TL approval → (tooling-build + SE tool verification) → Manager by-name run authorization → CS execution → SE verification. FP16 K=5 FAIL closed.

— Senior Engineer (composite-certification prereg v0.1; routes for CS feasibility and C5 claim-risk)
