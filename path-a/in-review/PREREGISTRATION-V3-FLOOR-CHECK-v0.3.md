# PREREGISTRATION — V3 FLOOR CHECK (Path A) v0.3

**E. A. Flores**, Apiana AI, Inc. — June 17, 2026
*River and Canyon · Path A. Drafted by the Senior Engineer (lock-before-look). Revises v0.2 (`a565e46b…`) per TL ACTION after CS feasibility HOLD ("feasible with required edits E1–E5"). Routes for CS re-review and C5 claim-risk; SE locks nothing and authorizes no run.*

> **Framing.** V3 conforms *structurally* to the foreclose-all standard (byte-audit `c3f4e667…`, build verification `e9b7e349…`). **V3 is not certified.** This floor check tests whether the substrate can operate under the standard at the locked load. **A single hop2-below-floor result is evidence toward substrate-infeasibility under V3, not a final classification** (§10).

> **Staging note.** v0.3 is produced as canonical bytes with the SE digest below for **verbatim commit by CS** into a C5-readable in-review repo path (SE does not push). A digest match confirms C5/CS review exactly this draft.

## 1. Research question

```text
PRIMARY:  Does hop2 (the second hop, B -> C*) clear its reliability floor when queried in
          isolation under V3's same-depth-competitor competition?
```

Primary metric: **hop2-isolated retrieval**, reported alone against its floor (§7), computed by the named analyzer (§E1). Not a composite pass rate; never collapsed (§7–§11).

## 2. Locked construction source (current of-record; v0.4 HOLD resolved, not reopened)

```text
TARGET-CONSTRUCT-DEFINITION-v0.4              4b616afb919114ee…
PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3     38e054601eda2ab6…
PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4  c61a3256d26e0ed0226e46a60d9b701baddfe3006249db687f221aea57315955
                                              (CURRENT of-record; placeholder corrective committed 9ea16d1;
                                               supersedes v0.3 d9bd9b21…. v0.4 byte-binding HOLD NOT reopened.)
```

## 3. Build artifact inputs and digests (SE-verified at HEAD `703b3a3`; re-pinned instrument)

```text
v3_item_generator.py        6a2ceee15442ebbd…       v3_relation_balance.md    de45d2a9bb640177…
v3_conformance_runner.py    2a4408353e3713e3…       v3_seed_plan.md           f501f741f47faafd…
v3_token_pool.md            d5f3594ce42a9e55…       v3_direct_query_filler.md 7ff83ab82de13c7d…
inspector.py  (instrument)  cb4b0b60bd6dc2b5…   ← re-pinned (matches v0.4)
constants.py  (instrument)  1d761c3d1c56e7ac…   ← re-pinned (matches v0.4; F=0.20, threshold=0.45)
```

Build verified (`e9b7e349…`) to realize V3, honor locked values, be deterministic, pass C1–C9 admissibility on the 8-item batch in real-run mode — **at the schema/spec level only** (§4–§6, §9 boundary).

## E1. Named analyzer / scorer (NEW — CS edit E1)

A single named, lockable analyzer computes all floor-check quantities and the final branch. It **scores already-produced model outputs**; it does **not** run a model.

```text
analyzer script path:  path-a/build/v3_floor_check_analyzer.py   (CS-produced)
analyzer intent:       deterministically compute the floor-check metrics and the final §9/§10 branch
                       from the per-context scored model outputs and the R6 invalidation log
analyzer inputs:       - per-context scored results for N=96: composite / hop1 / hop2 / direct_query
                       - materialized item ground truth (C*, B per locked construction)
                       - R6 invalidation log (item-level exclusions, §8)
analyzer outputs:      a single JSON report containing, AT MINIMUM:
                         - hop2-isolated retrieval rate
                         - hop2 Wilson 95% CI (lower bound is the decision input, §7)
                         - hop1-isolated retrieval rate
                         - hop1 Wilson 95% CI (lower bound is the decision input, §E4)
                         - direct-query C* count (point count, §E2)
                         - invalidated item count (§8)
                         - item-level exclusions (list)
                         - post-exclusion denominators and the resulting min-count thresholds (§E4)
                         - FINAL BRANCH under the §9 decision rule / §10 branches
analyzer sha256:       LOCKED AT APPROVAL. The analyzer's bytes must be fixed BEFORE the run (lock-before-
                       look on the scorer) so the scoring rule cannot be tuned to the data. CS produces it;
                       SE verifies it from bytes; TL/Manager lock its digest at approval.
```

This replaces any "computed once from artifacts" language: the executable scorer is named and its digest is locked.

## 4. Prompt-realization requirements (length-matching metric specified — CS edit E5)

The generated items are **schema-level specs, not prompts**. Before any run:

```text
- four-context prompt realization: each item -> concrete prompts for composite / hop1 / hop2 / direct_query
- no leakage of B or C* into hop1 / direct_query

PROMPT LENGTH-MATCHING METRIC (E5; deterministic, CS-enforceable):
  PRIMARY metric = CHARACTER COUNT.
  RULE: within a four-context set, prompts must be the SAME TEMPLATE CLASS — identical surface template,
        differing only by role-token substitution — AND the residual character-count delta across the four
        contexts must be <= a predeclared MAX DELTA (SE-proposed; LOCKED AT APPROVAL).
  TOKEN COUNTS: reported DIAGNOSTICALLY ONLY, not gating. If token-count matching is ever made gating, the
        exact tokenizer + version/hash must be specified and locked; absent that, token counts do not gate.
- a prompt-level conformance check must confirm realized prompts PRESERVE the foreclose-all properties
  (no introduced shortcut, no terminal/answer collision, controls intact)
```

Prompt realization is gated by Manager by-name authorization; not performed here.

## 5. Planned N=96 materialization requirements

```text
- the 8-item batch is a DEMONSTRATION; the run requires the full N=96 materialized
- the generator's per-item prefix scheme generalizes to N=96 without schema change (verified); all 96 must
  be generated and EACH must pass C1–C9 admissibility in real-run mode before any run
- position cycles 1..p across the 96; seeds = item index; determinism re-verified on the 96
- N=96 chosen for comparability with the C0 scout (96 per cell)
```

## 6. Component floor definitions

```text
DERIVED COMPONENT (CHANCE) FLOOR (locked):  F = max(1/p,1/m,1/D) = 0.20
COMPOSITE SUCCESS THRESHOLD (locked):       F + margin = 0.45

COMPONENT RELIABILITY FLOOR (SE-proposed; LOCKED AT APPROVAL):
  hop1 floor = 0.75 and hop2 floor = 0.75 (chosen for comparability with the C0 scout).

DIRECT-QUERY CEILING — EXACT POINT-COUNT (E2):
  direct-query C* count <= 19/96  -> PASSES
  direct-query C* count >= 20/96  -> FAILS  (direct-recall shortcut; set-level invalidator, §8)
  THIS IS A POINT-COUNT CEILING, NOT A WILSON INTERVAL RULE. No Wilson-upper, Wilson-lower, or alternate
  interval interpretation applies to the direct-query ceiling.

INVALIDATED-FRACTION CEILING — set-level construct-validity gate (E3; SE-proposed; LOCKED AT APPROVAL):
  invalidated item count <= 9/96   -> tolerated (items excluded from numerator + logged, §8)
  invalidated item count >= 10/96  -> CONSTRUCT-FAIL / MIS-SPECIFIED for this run
```

## 7. Hop2 floor metric (PRIMARY) — Wilson strictness, bounded claim

```text
METRIC:   hop2-isolated retrieval rate = (# items where hop2 returns the correct C*) / (post-exclusion
          denominator, §8), C* per the locked construction, under V3 competition (D=5 competitors present).
DECISION INPUT (strict): lower bound of the Wilson 95% CI on the rate > 0.75.
MIN COUNT (full N=96, no exclusions): 81/96 clears (SE-verified: Wilson lower 0.7581 > 0.75; 80/96 = 0.7463
          does NOT clear). If exclusions reduce the denominator, the analyzer recomputes the exact Wilson
          rule on the post-exclusion denominator and reports the resulting minimum count (§E4).

WHAT CLEARING MEANS (and does NOT): a COMPONENT-ADMISSIBILITY result. NOT capability, NOT certification,
          NOT evidence of composition.
  REQUIRED INTERPRETATION: "If hop2 clears, it means only that second-hop retrieval is reliable enough
  under V3 competition to make a later composite test interpretable."

Reported ALONE with its own CI. NOT a composite pass rate, NOT averaged with hop1, NOT collapsed.
```

## 8. Control checks + R6 invalidator handling (single mechanically-final rule — CS edit E3)

```text
R6 INVALIDATORS — single rule, two levels (NOT zero-tolerance):
  ITEM-LEVEL:  if an item-level R6 invalidator fires, that item is EXCLUDED from the relevant validated
               numerator and LOGGED. The item-level R6 invalidators are EXACTLY the five non-circular ones:
                 terminal-coincidence, controls-unavailable, direct-recall, interior-position, constant-token.
  SET-LEVEL:   invalidated item count <= 9/96 tolerated; >= 10/96 -> CONSTRUCT-FAIL / MIS-SPECIFIED (§10).

  "BELOW-FLOOR" CLARIFICATION (avoid circularity, E3): hop2-below-floor is NOT an item-level R6 invalidator.
  Hop2-below-floor is the PRIMARY SET-LEVEL FLOOR OUTCOME (§7, §10). Any item-level "below-floor" notion
  refers ONLY to construction-admissibility floor structure caught by C1–C9 at admissibility time, never to
  the hop2 retrieval outcome. The primary metric does not invalidate its own items.

OTHER CONTROLS (each reported separately; none collapsed into the primary):
  - hop1 floor:           hop1-isolated, lower Wilson 95% bound > 0.75 (§E4). Below floor -> CONSTRUCT problem.
  - direct-query control: dq C* count vs the 19/96 point ceiling (§6/E2).
  - dominance control:    DOMINANT_RATE_THRESHOLD = 0.25 — a single competitor/decoy absorbing > 25% of the
                          off-target mass is flagged (fixed-shortcut signal), reported not pass/fail.
  - four-context load-matching: per the §4 character-count metric, verified at prompt realization.
  - construction admissibility: C1–C9 inspector PASS in real-run mode for all N=96 (precondition, §5).
```

## E4. hop1 floor CI treatment (explicit, parallel to hop2 — CS edit E4)

```text
hop1 clears floor IFF lower Wilson 95% bound > 0.75 (same rule as hop2).
MECHANICAL NOTE (SE-verified): at N=96, 81/96 is the MINIMUM count that clears this rule
  (Wilson lower 0.7581 > 0.75; 80/96 = 0.7463 does NOT clear).
POST-EXCLUSION: if item-level invalidation reduces the denominator below 96, the analyzer (§E1) computes the
  EXACT Wilson rule on the post-exclusion denominator and reports the resulting minimum-count threshold for
  that denominator. The 81/96 figure is the full-N reference, not a hardcoded count.
```

## 9. Decision rule (computed once by the named analyzer; clean construct scoped to spec + prompts)

```text
COMPONENT-ADMISSIBLE-UNDER-COMPETITION (the only "gate clears" outcome) requires ALL of:
  (i)   hop2-isolated lower Wilson 95% bound > 0.75,
  (ii)  direct-query C* count <= 19/96 (point count),
  (iii) hop1-isolated lower Wilson 95% bound > 0.75,
  (iv)  invalidated item count <= 9/96 (set-level construct validity),
  (v)   C1–C9 admissibility PASS for all materialized items, AND
  (vi)  PROMPT-REALIZATION CONFORMANCE PASS (the construct is "clean" at the EXECUTABLE level).
  -> THEN: component admissible under competition on V3. OPENS — does not answer — the composite /
     certified-baseline question (separate prereg). NOT certification.

CLEAN-CONSTRUCT BOUNDARY: clean at the SPEC level only until prompt-realization conformance passes (vi). A
  spec-clean, prompt-unchecked construct is NOT eligible for a substrate conclusion.

The composite, if computed, is interpreted ONLY in light of hop2 admissibility (a composite number with hop2
below floor is uninformative — the C0 lesson).
```

## 10. Null / fail / substrate-infeasibility branches (repeated-failure discipline)

```text
ONE-RUN EVIDENCE TOWARD SUBSTRATE-INFEASIBILITY (single-run outcome — NOT final):
  hop2-isolated does NOT clear 0.75 while (ii)–(vi) hold (clean executable construct) -> this run is EVIDENCE
  TOWARD substrate-infeasibility under V3 at the locked load. NOT, by itself, final proof.

FINAL SUBSTRATE-INFEASIBILITY CLASSIFICATION (requires REPEATED admissible failures):
  Made only after repeated hop2-below-floor results across admissible runs (clean construct each time), per
  the constructibility framework's repeated-failure discipline. One clean failed run does NOT become an
  overstrong final claim, and a below-floor result is NEVER a license to loosen the 0.75 floor, lower D, or
  tune until the number cooperates.

CONSTRUCT-FAIL (NOT a substrate result, at any count):
  invalidated count >= 10/96, OR direct-query count >= 20/96, OR hop1 below floor, OR C1–C9 admissibility
  fails, OR prompt-realization conformance fails -> the TEST is invalid, not the substrate. Fix the construct
  and re-pre-register; draw NO substrate conclusion.
```

## 11. Forbidden interpretations

```text
- hop2-below-floor is NOT "V3 is a bad construction"; V3 is verified-conformant. It is a substrate finding
  (one-run evidence, §10), not an instrument defect.
- hop2-clears is NOT certification and NOT a composition claim; it opens the composite question only.
- The composite result is NOT a standalone pass; interpreted only in light of hop2.
- NO mechanism claims (traversal vs grab vs anchor not decidable here).
- Survival is not correctness: C* counts only if it is the RIGHT C* via the bridge, controls clearing, no invalidator.
- "Not ruled out" is not "established."
- A single clean failed run is evidence TOWARD substrate-infeasibility, not a final classification.
```

## 12. Stop rule

```text
- N fixed at 96. Floors (0.75 reliability; 0.20 chance; 19/96 dq point ceiling; 9/96 invalidated ceiling;
  0.45 composite threshold), the §9 rule, and the §E1 analyzer digest are fixed BEFORE the run and computed ONCE.
- NO post-hoc floor adjustment, NO slicing, NO re-running until it passes, NO analyzer edit after data.
- An invalid construct (§10 construct-fail) is remedied by a NEW pre-registration.
- FINAL substrate-infeasibility is a separate determination across repeated admissible runs, not this single run.
```

## 13. Required artifacts (CS must produce before any run)

```text
- full N=96 item materialization (specs), each passing C1–C9 admissibility in real-run mode
- four-context prompt realization (composite / hop1 / hop2 / direct_query), per the §4 character-count metric
- prompt-level conformance checks confirming realized prompts preserve foreclose-all properties
- the named analyzer v3_floor_check_analyzer.py (§E1), digest locked at approval, SE-verified from bytes
- clean-fetchable artifact hashes (sha256) for all items, prompts, per-context conformance results, analyzer
- fixture-mode / real-run assertions: run executes in REAL-RUN mode (no _fixture_mode, no _sweep_mode),
  asserted in the run record and confirmed by the inspector per item
```

## 14. Execution boundary (preserved)

```text
This preregistration authorizes:
  No build changes.  No N=96 materialization.  No prompt generation for execution.  No model run.
  No compression.  No Claim C.  No Paper B.  No certification claim.  No capability claim.  No mechanism claim.

Routing (no step may be skipped):
  SE draft -> CS feasibility re-review -> C5 claim-risk review -> TL approval
     -> Manager by-name authorization -> CS execution -> SE verification

At run time, Manager by-name authorization is required, with the §13 real-run assertion in force and the
§E1 analyzer digest locked. The Path A FP16 K=5 FAIL remains closed. SE drafts; SE locks nothing.
```

---

**The one to carry up:** v0.3 resolves CS E1–E5. **(E1)** A named, lockable analyzer `v3_floor_check_analyzer.py` computes hop2/hop1 rates + Wilson CIs, dq count, invalidated count, item exclusions, and the final branch — its digest **locked at approval** (lock-before-look on the scorer); it scores outputs, runs no model. **(E2)** The direct-query ceiling is an **exact point-count (≤19/96 pass, ≥20/96 fail), explicitly not a Wilson rule**. **(E3)** R6 is a single rule — item-level exclude+log (the five non-circular invalidators), set-level ≥10/96 → construct-fail — and **hop2-below-floor is explicitly NOT an item-level invalidator** (it is the primary set-level outcome; no circularity). **(E4)** hop1 is parallel to hop2 (lower Wilson > 0.75; **81/96 minimum at full N**, SE-verified; analyzer recomputes on the post-exclusion denominator). **(E5)** Prompt length-matching is **character count + same template class within a predeclared max delta**, token counts diagnostic only. All v0.2 improvements preserved (v0.4 binding `c61a3256…`, instrument `cb4b0b60`/`1d761c3d`, dq point boundary, R6 item/set split, hop2-clearing-as-component-admissibility-only, one-clean-failed-run = evidence-toward-not-final, clean-construct contingent on prompt-realization conformance). hop2 remains the standalone primary metric. Authorizes no run, no materialization, no prompt generation, no model execution; routes SE-draft → CS feasibility re-review → C5 claim-risk → TL approval → Manager by-name authorization → CS execution → SE verification. FAIL closed. CS to commit these bytes verbatim to a C5-readable in-review path; digest below.

— Senior Engineer (floor-check prereg v0.3; routes for CS feasibility re-review and C5 claim-risk)
