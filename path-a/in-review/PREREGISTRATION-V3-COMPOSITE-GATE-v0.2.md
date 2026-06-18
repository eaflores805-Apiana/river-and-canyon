# PREREGISTRATION — V3 COMPOSITE GATE (Path A) v0.2

**E. A. Flores**, Apiana AI, Inc. — June 18, 2026
*River and Canyon · Path A. Drafted by the Senior Engineer (lock-before-look). Revises v0.1 (`ee1ad41d…`, titled "V3 Composite Certification") per TL ACTION after C5 HOLD — ARTIFACT ACCESS + standing claim-risk rulings. Routes for filing and review; SE locks nothing and authorizes no run.*

> **Framing.** The V3 floor check established **component-admissibility-under-competition** for hop2 at the locked K=5 load (SE-verified, `03d2ead8…`). This prereg asks a **separate** empirical question: does the full two-hop **composite** clear a predeclared **gate** on a **fresh, disjoint** materialization? **A single fresh run may clear a gate; it does NOT produce certification-of-record by itself** (§7). The word *certification* appears below only as a **bounded conditional concept**, never as a result this run delivers on its own.

> **CRITICAL — lock-before-look.** The floor-check composite (80/96 = 0.833) is **informational and already seen**, and is **barred from use as composite-gate evidence** (§5). The gate is evaluated **only** on a **fresh run with seeds disjoint from the floor check** (§4), with the gate locked **before** the fresh composite is generated.

## 1. Component admissibility — VERIFIED PREMISE (precondition only; not re-litigated)

```text
From the V3 floor check (SE-verified; analyzer decision byte-identical 6a34f6dc…):
  hop2-isolated 96/96   (Wilson lower 0.9615 > 0.75)   CLEARS
  hop1-isolated 87/96   (Wilson lower 0.8313 > 0.75)   CLEARS
  direct-query C* count 0 ;  invalidated 0 ;  C1–C9 96/96 ;  prompt-conformance 96/96
  final branch: COMPONENT-ADMISSIBLE-UNDER-COMPETITION
```

This is carried **only** as the precondition that makes a composite-gate test **interpretable**. It is not re-opened. (It must be **re-confirmed on the fresh set** — §6 — since the fresh items are new data; it is not inherited.)

## 2. The composite-gate question (the new empirical question)

```text
PRIMARY:  On a FRESH N=96 materialization of the locked V3 construction with seeds DISJOINT from the floor
          check, does the full two-hop COMPOSITE clear the predeclared composite gate (§7), given that the
          components are admissible under competition?
```

## 3. Composite score interpretation (validity, not capability/mechanism)

```text
- CERTIFICATION-AS-CONCEPT (bounded): a cleared gate would "certify the V3 composite baseline as BEHAVIOR
  CONSISTENT WITH two-hop composition under foreclose-all controls." This is a VALIDITY statement about the
  baseline under controls — NOT a capability claim, NOT a mechanism claim, NOT "the model composes."
- CERTIFICATION METRIC (on the FRESH set): composite-correct rate = (# items whose composite context
  RETURNS THE CORRECT-CHAIN TARGET C* UNDER CONTROLS) / (post-exclusion denominator). We observe the output
  token and the cleared controls; we do NOT observe the model's internal path. A decoy-chain C does NOT count.
- Reported with its Wilson 95% CI; the lower bound is the gate input (§7). Reported alone; not collapsed.
```

## 4. Fresh-run seed ranges (exact; provable independence — C5 edit 4)

```text
FLOOR-CHECK SEEDS ALREADY USED (byte-confirmed from the run's construction_ids):  001 .. 096  (contiguous)
COMPOSITE-GATE SEEDS (this prereg, exact):                                         097 .. 192  (contiguous)
DISJOINTNESS RULE: the composite-gate seed set {097..192} MUST NOT overlap the floor-check set {001..096}.
  Disjointness makes the fresh run provably independent of the already-seen floor-check composite.

TOKEN-WIDTH CONSTRAINT (carry-forward of the MAX_DELTA=8 caveat): indices/seeds MUST remain <= 999 (3-digit
  prefix i{NNN}_), so the per-item role-token widths are UNCHANGED and the <=8-character prompt-length gate
  remains valid. {097..192} satisfies this. (A 4-digit index would widen the prefix and break MAX_DELTA=8.)
CS FEASIBILITY ITEM: generating indices 097..192 may require a generator start-index / seed-offset parameter;
  CS confirms (or adds it) at the tooling/feasibility step. The <=999 constraint is mandatory.
```

## 5. The already-seen composite is BARRED from gate use (C5 edit 5)

```text
The floor-check composite (80/96 = 0.833) is INFORMATIONAL ONLY and ALREADY SEEN.
It is BARRED from use as composite-gate evidence.
The composite gate is evaluated ONLY on the fresh, disjoint {097..192} materialization.
(The 0.833 may serve as a prior expectation in discussion; it is NOT a gate datum.)
```

## 6. Direct-query + control preservation, re-confirmed on the FRESH set (not inherited)

```text
On the FRESH N=96 {097..192}, BEFORE the composite gate is read:
  - direct-query control: dq C* count <= 19/96 (no direct-recall on the fresh items) — point count.
  - hop2-isolated: lower Wilson 95% > 0.75 (component admissible on the fresh items).
  - hop1-isolated: lower Wilson 95% > 0.75.
  - C1–C9 admissibility: 96/96 PASS, real-run (fresh items).
  - prompt-realization conformance: 96/96 PASS, incl. the <=8 char delta (fresh prompts).
  - dominance: DOMINANT_RATE_THRESHOLD = 0.25 on the composite off-target mass (flagged, not pass/fail).
If any precondition fails on the fresh set -> PRECONDITION-FAIL (§8): gate NOT read; examine / re-pre-register.
```

## 7. Decision rule — two separate lower-Wilson gates + the this-run/final boundary (C5 edits 6, 7)

```text
TWO GATES, BOTH LOWER-WILSON, REPORTED SEPARATELY:
  PRIMARY RELIABILITY GATE:        composite-correct lower Wilson 95% > 0.75
                                   (the component reliability standard; SE-proposed, LOCKED AT APPROVAL)
  NECESSARY NOT-SHORTCUT FLOOR:    composite-correct lower Wilson 95% > 0.45
                                   0.45 is NOT free: it is INHERITED as F + margin = 0.20 + 0.25.
                                   A composite below this is achievable by foreclosed non-traversal routes;
                                   necessary, not sufficient.

GATE-CLEARED-THIS-RUN requires ALL of:
  (a) composite-correct lower Wilson 95% > 0.75   (primary reliability gate),
  (b) composite-correct lower Wilson 95% > 0.45   (necessary not-shortcut floor — reported separately),
  (c) preconditions hold on the fresh set (hop2 admissible, hop1 admissible, dq <= 19/96) — §6,
  (d) construct clean on the fresh set (C1–C9 96/96, conformance 96/96, invalidated <= 9/96),
  (e) error-structure non-pathological (composite "successes" are correct-chain target C* under controls) — §5/§9-logging.
  -> THEN: GATE-CLEARED-THIS-RUN.

THIS-RUN vs FINAL (precommitted boundary):
  GATE-CLEARED-THIS-RUN is the MOST this single fresh run can yield. It MUST NOT silently become FINAL
  certification. FINAL certification-of-record requires a SEPARATE Manager / standard decision and MAY
  require confirmation or replication. (SE recommends >= 1 confirmation run, mirroring the discipline that
  substrate-infeasibility requires REPEATED failures — strong claims in both directions cost > 1 run.)

THRESHOLD TRANSPARENCY: 0.75 is chosen on PRINCIPLE (the component reliability standard), NOT relative to the
  seen 0.833. The seen composite lower bound (0.7463) sits JUST BELOW 0.75, so the fresh-run result is
  GENUINELY UNCERTAIN — it may clear or may fail. The threshold is NOT set to guarantee a pass; failure (§8)
  is a real, valid outcome.
```

## 8. Failure / null branches

```text
COMPOSITE-DOES-NOT-CLEAR-THIS-RUN (clean construct, components admissible, gate not met):
  composite-correct lower Wilson <= 0.75 while (b)–(e) hold -> the composite is NOT reliable enough to clear
  the gate at this load on the fresh set. VALID outcome. NEVER a license to lower 0.75, change the
  construction, or tune to the data. (Clears 0.45 but not 0.75: "not explained by foreclosed shortcuts, but
  not reliably composing" — recorded as such.)

PRECONDITION-FAIL (components not admissible on the fresh set):
  hop2/hop1 below floor, or dq >= 20/96, on the FRESH items -> fresh set not on admissible ground; gate NOT
  read; examine / re-pre-register. NOT a composite conclusion.

CONSTRUCT-FAIL (invalid test):
  invalidated >= 10/96, OR C1–C9 fails, OR conformance fails, OR error-structure pathological (successes not
  correct-chain) -> the TEST is invalid. Fix and re-pre-register.
```

## 9. Same-error / wrong-address logging (composition-specific control)

```text
For every composite ERROR, log WHERE the output token lands and CO-OCCURRENCE (positional/structural; NOT mechanism):
  WHERE: correct chain wrong depth | DECOY chain depth-2 (off-map "right depth, wrong chain") | competitor | other
  CO-OCCURRENCE: error on an item whose hop2-isolated ALSO failed (inherited) vs whose hop2 SUCCEEDED
                 (composition-specific: components work but the chained output does not)
This is a CONTROL, not the primary metric, and does not change the §7 gate. Pathological patterns are FLAGGED
(e.g., "successes" not correct-chain -> CONSTRUCT-FAIL). WHY the model errs is NOT decidable here and NOT claimed.
```

## 10. Forbidden interpretations (strengthened — C5 edit 8)

```text
A cleared gate, or any result of this run, must NOT be read as ANY of:
  - "the model composes"
  - general two-hop capability
  - a mechanism claim
  - seam evidence
  - compression readiness
  - Claim C
  - Paper B
  - FINAL certification from one run
ALSO:
  - A cleared composite gate does NOT itself authorize compression or stress rungs.
  - A cleared gate certifies ONLY "the V3 composite baseline as behavior consistent with two-hop composition
    under foreclose-all controls," on V3, at K=5, with Qwen2.5-3B-Instruct (FP16, greedy) — and nothing beyond.
  - The floor-check composite (0.833) is informational/already-seen, NOT gate evidence; no reuse of the
    floor-check run as the gate.
  - Survival is not correctness; "not ruled out" is not "established."
  - The C0 K=5 FAIL stays CLOSED; V3 ≠ C0; this prereg does not bear on it.
```

## 11. Stop rule

```text
- N fixed at 96 (FRESH materialization, seeds 097..192). The two gates (0.75 / 0.45), the §6 preconditions,
  the §7 rule, the this-run/final boundary, and the gate-analyzer digest are fixed BEFORE the fresh run and
  computed ONCE.
- NO post-hoc threshold adjustment, NO slicing, NO re-running until it passes, NO tooling edit after data.
- A construct-fail (§8) is remedied by a NEW pre-registration.
- FINAL certification is a SEPARATE determination (§7), not this single run.
```

## T. Tooling (named; new tooling built under a SEPARATE TL/Manager action; existing tooling reused unchanged)

```text
REUSED UNCHANGED (digests already locked; re-used on the fresh {097..192} set):
  v3_item_generator.py 6a2ceee1… (re-run with seeds 097..192; CS confirms start-index support, §4)
  v3_prompt_realizer.py fb561fdc… · v3_prompt_conformance_checker.py b8afa3f8… · v3_neutral_token_pool.md bc2020c2…
  inspector.py cb4b0b60… / constants.py 1d761c3d…
NEW (named; built under a SEPARATE TL/Manager tooling-build action; SE-verified; digest LOCKED AT APPROVAL):
  path-a/build/v3_composite_gate_analyzer.py
     intent: compute composite-correct rate + Wilson CI; evaluate the §7 two-gate rule; re-confirm §6
             preconditions; apply §4-seed/§8 invalidator rules; emit the §7/§8 branch (GATE-CLEARED-THIS-RUN /
             COMPOSITE-DOES-NOT-CLEAR / PRECONDITION-FAIL / CONSTRUCT-FAIL). Scores outputs; runs no model.
     deterministic; sha256 LOCKED AT APPROVAL.
  path-a/build/v3_composite_error_logger.py
     intent: produce the §9 same-error / wrong-address characterization. deterministic; sha256 LOCKED AT APPROVAL.
```

## E. Execution boundary + routing

```text
This preregistration authorizes:
  No new run.  No fresh materialization yet.  No prompt generation.  No tooling creation.  No compression /
  INT8 / INT4.  No Claim C.  No Paper B.  No certification claim (only GATE-CLEARED-THIS-RUN if the §7 gate
  clears on the fresh run; FINAL certification is a separate decision).  No capability claim.  No mechanism claim.

ROUTING (no step may be skipped):
  Senior draft (v0.2)
   -> CS files v0.2 to a readable in-review path
   -> C5 reviews actual bytes
   -> CS feasibility review
   -> TL approval consideration
   -> (separate TL/Manager TOOLING-BUILD action for the two new tools -> SE verifies tool bytes)
   -> Manager by-name RUN authorization (only if approved later; fresh run; real-run; locked digests)
   -> CS execution
   -> SE verification

The Path A FP16 K=5 FAIL remains closed and untouched. SE drafts this prereg; SE locks nothing.
```

---

**The one to carry up:** v0.2 is retitled **V3 COMPOSITE GATE** ("certification" only as a bounded conditional inside, never the title) and folds all C5/TL rulings. A cleared gate would **"certify the V3 composite baseline as behavior consistent with two-hop composition under foreclose-all controls"** — a **validity** statement, not "the model composes," not capability, not mechanism. The metric counts items that **return the correct-chain target C\* under controls** (output token + cleared controls observed; internal path not observed). The gate runs on a **fresh, disjoint materialization, seeds 097..192** (floor-check used 001..096, byte-confirmed; disjointness gives provable independence; indices kept ≤999 so the MAX_DELTA=8 token-width gate stays valid). The floor-check composite (0.833) is **barred** from gate use. **Two separate lower-Wilson gates:** primary reliability **> 0.75**, necessary not-shortcut floor **> 0.45** (inherited F+margin), reported separately. **GATE-CLEARED-THIS-RUN ≠ FINAL certification** — a single pass cannot silently become final; final needs a separate Manager/standard decision and SE recommends ≥1 confirmation. **Forbidden (strengthened):** the model composes / general two-hop capability / mechanism / seam evidence / compression readiness / Claim C / Paper B / final-from-one-run — and **a cleared gate does not authorize compression or stress rungs**. Verified floor-check premise carried only as the interpretability precondition. Two new tools named, built under a **separate** TL/Manager action; realizer/checker/pool/generator reused unchanged. Authorizes no run, materialization, tooling, compression, or certification. Routes per TL's next-route block. FP16 K=5 FAIL closed.

— Senior Engineer (composite-gate prereg v0.2; routes for CS filing, C5 byte review, CS feasibility)
