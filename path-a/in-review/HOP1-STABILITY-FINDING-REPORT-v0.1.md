# HOP1-STABILITY-FINDING-REPORT-v0.1

**To:** Team Lead (for Manager decision) **Cc:** CS Engineer, C5, Manager **From:** Senior Engineer
**E. A. Flores**, Apiana AI, Inc. — June 19, 2026
*River and Canyon · Path A. A finding of record and route-closeout note. Behavioral metrology only; positional/structural claims only. SE drafts; SE locks nothing and authorizes no run.*

> **What this is.** A banking of byte-verified results establishing that, under the current V3 construction at K=5 (FP16, greedy, Qwen2.5-3B-Instruct), **hop1-isolated admissibility does not reliably hold across fresh materializations**, which **blocks the composite-gate route as designed**. This is a **measurement / construct-stability finding** — it characterizes the V3 instrument's hop1 precondition, **not** the model's ability. Every number below was independently recomputed from repository bytes.

## 1. Prior route context

The committed route was: **foreclose-all gate standard → V3 conforming construction → floor-check → composite gate**. The composite gate carries **hop1 admissibility as a precondition** (the composite is interpretable only if the first hop is reliably retrievable under competition). The floor-check was the step intended to establish that precondition.

## 2. Floor-check result (anchor; seeds 001..096)

```text
hop1-isolated 87/96 = 0.906  (Wilson lower 0.8313 > 0.75)   CLEARS
hop2-isolated 96/96 = 1.000  (Wilson lower 0.9615 > 0.75)   CLEARS
direct-query 0/96 ; invalidated 0 ; C1–C9 96/96 ; conformance 96/96
final branch: COMPONENT-ADMISSIBLE-UNDER-COMPETITION   (SE-verified; decision 6a34f6dc…)
```

Read at the time, and still, as **component-admissibility on that one materialization** — never as certification or capability.

## 3. Composite-gate run — PRECONDITION-FAIL (fresh, disjoint; seeds 097..192)

The composite gate required a fresh, disjoint materialization (lock-before-look; the floor-check composite was already-seen and barred). On the fresh set:

```text
hop1-isolated 28/96 = 0.292  (Wilson lower 0.2102)   FAILS the 0.75 precondition floor
hop2-isolated 96/96 = 1.000  (Wilson lower 0.9615)   clears
final branch: PRECONDITION-FAIL  -> the composite gate was NOT read   (SE-verified; decision 3924ff35…)
Wrong hop1 predictions landed on the P-role distractor (68/68 of the wrong predictions).
```

The composite question was **not answered** (the gate was not read). hop1 failing on a fresh set — having cleared on the floor-check set — was the trigger for the stability investigation.

## 4. Hop1 stability result (six fresh blocks; seeds 193..768)

A pre-registered, lock-before-look stability map (six fresh blocks of N=96, same locked V3 construction, hop1 + hop2-control, FP16/greedy):

```text
 block    hop1       rate     hop2
 F1      50/96     0.5208    96/96
 F2      23/96     0.2396    96/96
 F3      35/96     0.3646    96/96
 F4      39/96     0.4062    96/96
 F5      54/96     0.5625    96/96
 F6      23/96     0.2396    96/96
 hop2 control: 576/576 (clears every block)
 final branch: HOP1-STABLE-INADMISSIBLE   (SE-verified; decision reproduced byte-identical)
```

All six fresh hop1 blocks **fail** the 0.75 floor (rates span 0.24–0.56; even the highest, F5 at 0.5625, has Wilson lower 0.4628 ≪ 0.75). hop2 **clears every block**. Scoring is honest (0 match-vs-(ground-truth) disagreements, 0 empty predictions); the raw model output token equals the parsed prediction, so the result is **real model behavior, not a scoring or parsing artifact**.

**Anchored across all eight materializations** (001..096, 097..192, F1–F6), hop1 cleared the floor in **exactly one** (the floor-check, 0.906); the other seven failed (0.24–0.41 on 097..192 and F2/F3/F4/F6, 0.52–0.56 on F1/F5). The floor-check clearing is **anomalous relative to the fresh map**.

## 5. P-role positional finding

The stability prereg pre-declared one **confirmatory** covariate (suggested by the composite-gate result, tested on fresh data): whether a wrong hop1 prediction lands on the **P-role distractor** — the r1-*subject* of a relation-reusing distractor chain `(P_i, r1, Q_i)` present in the facts, as opposed to the correct r1-*object* B.

```text
Among wrong hop1 predictions in the fresh stability blocks: 352/352 landed on the P-role distractor class.
```

The predeclared co-occurrence **reproduced on fresh blocks in all logged cases**. This is a **positional/structural co-occurrence**, recorded as data. No mechanism is claimed or implied.

## 6. Exact allowed interpretation

```text
"Across the six fresh V3 materializations tested here, hop1 did not clear its admissibility floor in any
 block, while hop2 remained admissible in every block."

"Among wrong hop1 predictions in the fresh blocks, outputs landed on the P-role distractor class in all
 logged cases."
```

Both are positional / structural statements about behavior under the V3 controls.

## 7. Forbidden interpretations

```text
This finding is NOT, and must not be written as, any of:
  the model cannot do hop1 | the model cannot compose | the model is unstable | binding failure |
  attention failure | reasoning failure | shortcut mechanism | compression readiness | Claim C |
  Paper B | certification.
The model performed hop1 at 0.906 on the floor-check materialization; "inadmissible across the fresh blocks"
is a statement about the V3 construct's precondition stability under these controls, NOT about the model's
capability. The C0 K=5 FAIL stays CLOSED; V3 ≠ C0. Survival is not correctness; "not ruled out" is not "established."
```

## 8. Route consequence

```text
The current V3 composite-gate route is BLOCKED AS DESIGNED.
  - The composite gate requires hop1 admissibility as a precondition.
  - Fresh materializations show hop1 admissibility does NOT reliably hold (stable-inadmissible across six
    fresh blocks; the lone clearing, on the floor-check set, is anomalous).
  - Therefore the composite gate is NOT reliably testable under the current V3 design.
This is a precondition-level block, not a composite result: the composite question remains unanswered, neither
supported nor refuted.
```

## 9. Options for Manager decision

Presented neutrally for the Manager (Elias). **No rerun-until-pass path is offered** — drawing fresh seeds until hop1 happens to clear is excluded by the program's discipline and by the stable-inadmissible result.

```text
A. CLOSE the current V3 composite route and BANK this finding.
   - Records the verified result of record; stops the composite line under the current design.
   - Lowest cost. Leaves the construction-design question and the papers as separate later choices.
   - The finding stands on its own as a measurement / construct-stability result.

B. OPEN a new construction-design question focused on hop1 admissibility under V3-like controls.
   - A fresh, separately pre-registered DESIGN effort: can a V3-like construction be built whose hop1
     precondition is stably admissible across materializations (without importing a non-traversal route)?
   - Higher cost; productive; only worthwhile if a stably-admissible hop1 construction is plausibly reachable.
   - This is design work, NOT a rerun of the current construction or gate.

C. PAUSE Path A and PACKAGE the constructibility findings for the papers.
   - Banks the accumulated measurement-validity results (survival≠correctness; correctness≠constructibility;
     certification-before-retention; lock-before-look catching hop1 non-replication; the P-role positional
     regularity) as the contribution to date.
   - Productive; consolidates what the discipline has earned rather than opening new construction work now.

(SE perspective, non-binding: A is a prerequisite framing for either B or C — the finding is banked regardless;
 B vs C is a priorities question for the Manager. The program's contribution to date is the measurement
 discipline itself, which both B and C build on in different directions. The choice is the Manager's.)
```

## Boundary

```text
- Finding record only. No rerun, no prompt edits, no regeneration, no post-hoc slicing, no threshold change,
  no tooling edit, no composite-gate retry, no compression, no INT8/INT4, no Claim C, no Paper B, no
  certification claim, no capability claim, no mechanism claim.
- The program remains PRE-STRESS (FP16); nothing here bears on compression / INT4.
- The Path A FP16 K=5 FAIL remains closed and untouched. SE drafts this finding; SE locks nothing and
  authorizes nothing. The decision among A/B/C is the Manager's.
```

---

**The one to carry up:** Under V3 at K=5 (FP16, greedy, Qwen2.5-3B-Instruct), **hop1-isolated admissibility is stable-inadmissible across six fresh materializations** (rates 0.24–0.56, all below the 0.75 floor), while **hop2 clears every block** (576/576) — verified byte-for-byte, real model behavior, not an artifact. Across all eight materializations to date, hop1 cleared the floor in **exactly one** (the floor-check, 0.906), which is **anomalous relative to the fresh map**. Among wrong hop1 predictions, outputs landed on the **P-role distractor in all logged cases (352/352)** — a positional/structural co-occurrence, no mechanism. **Consequence:** the V3 composite gate is **blocked as designed** — its hop1 precondition does not reliably hold, so the gate is not reliably testable; the composite question remains unanswered. This is a **measurement / construct-stability finding about V3, not a statement about the model** (it did hop1 at 0.906 on one materialization). **Manager decision:** (A) close + bank, (B) open a new hop1-admissibility construction-design question, or (C) pause Path A and package the constructibility findings for the papers — no rerun-until-pass. Still pre-stress; C0 K=5 FAIL closed. SE drafts; SE authorizes nothing.

— Senior Engineer (hop1-stability finding & route-closeout; routes for Manager decision)
