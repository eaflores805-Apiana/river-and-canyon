# PREREGISTRATION — V3 FLOOR CHECK (Path A) v0.4

**E. A. Flores**, Apiana AI, Inc. — June 17, 2026
*River and Canyon · Path A. Drafted by the Senior Engineer (lock-before-look). Revises v0.3 (`df82b34c…`) per TL ACTION after CS feasibility re-review HOLD ("feasible with required edits F1–F2 + one routing prerequisite F3"). C5 claim-risk PASSED on v0.3; this revision does not alter any C5-cleared claim boundary. Routes for CS re-review; SE locks nothing and authorizes no run.*

> **Framing.** V3 conforms *structurally* to the foreclose-all standard (byte-audit `c3f4e667…`, build verification `e9b7e349…`). **V3 is not certified.** This floor check tests whether the substrate can operate under the standard at the locked load. **A single hop2-below-floor result is evidence toward substrate-infeasibility under V3, not a final classification** (§10).

> **Staging note.** v0.4 is canonical bytes with the SE digest below for **verbatim commit by CS** into a C5-readable in-review repo path (SE does not push). Digest match confirms review of exactly this draft.

## 1. Research question

```text
PRIMARY:  Does hop2 (the second hop, B -> C*) clear its reliability floor when queried in
          isolation under V3's same-depth-competitor competition?
```

Primary metric: **hop2-isolated retrieval**, reported alone against its floor (§7), computed by the named analyzer (§T). Not a composite pass rate; never collapsed (§7–§11). *(C5-cleared — unchanged.)*

## 2. Locked construction source (current of-record; v0.4 binding HOLD resolved, not reopened)

```text
TARGET-CONSTRUCT-DEFINITION-v0.4              4b616afb919114ee…
PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3     38e054601eda2ab6…
PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4  c61a3256d26e0ed0226e46a60d9b701baddfe3006249db687f221aea57315955
                                              (CURRENT of-record; corrective committed 9ea16d1; supersedes
                                               v0.3 d9bd9b21…. Byte-binding HOLD NOT reopened.)
```

## 3. Build artifact inputs and digests (SE-verified at HEAD `703b3a3`; re-pinned instrument)

```text
v3_item_generator.py        6a2ceee15442ebbd…       v3_relation_balance.md    de45d2a9bb640177…
v3_conformance_runner.py    2a4408353e3713e3…       v3_seed_plan.md           f501f741f47faafd…
v3_token_pool.md            d5f3594ce42a9e55…       v3_direct_query_filler.md 7ff83ab82de13c7d…
inspector.py  (instrument)  cb4b0b60bd6dc2b5…   ← re-pinned (matches v0.4)
constants.py  (instrument)  1d761c3d1c56e7ac…   ← re-pinned (matches v0.4; F=0.20, threshold=0.45)
```

Build verified (`e9b7e349…`) to realize V3, honor locked values, be deterministic, pass C1–C9 admissibility on the 8-item batch in real-run mode — **at the schema/spec level only** (§4, §9 boundary).

## T. Floor-check tooling artifacts (NEW — CS edit F2; named + lock-at-approval; build is a SEPARATE gated action, F3)

All four artifacts are **named and lockable here but NOT built here** (§F3 routing). Each is produced by CS under a separate TL/Manager tooling-build authorization, SE-verified from bytes, and its sha256 **locked at approval before any run** (lock-before-look on the tooling).

```text
1. ANALYZER
   path:        path-a/build/v3_floor_check_analyzer.py
   intent:      deterministically compute the floor-check metrics and the §9/§10 final branch from
                per-context scored model outputs + the R6 invalidation log. SCORES outputs; runs no model.
   inputs:      per-context scored results (composite/hop1/hop2/direct_query, N=96); item ground truth;
                R6 invalidation log (item-level exclusions, §8)
   outputs:     single JSON: hop2 rate + Wilson 95% CI; hop1 rate + Wilson 95% CI; direct-query C* count;
                invalidated item count; item-level exclusions; post-exclusion denominators + min-count
                thresholds (§E4); FINAL BRANCH under §9/§10
   deterministic: pure function of inputs; no clock, randomness, or network
   sha256:      LOCKED AT APPROVAL

2. PROMPT REALIZER
   path:        path-a/build/v3_prompt_realizer.py
   intent:      render each schema-level item spec into four concrete prompts (composite/hop1/hop2/
                direct_query) under the §4 length-matching constraint (same template class, <= 8 char delta)
   inputs:      the N=96 item specs (schema-level); the neutral-token pool / filler resource (#4)
   outputs:     four prompt strings per item + per-set character counts (composite/hop1/hop2/direct_query)
   deterministic: pure function of (spec, seed); same spec -> byte-identical prompts; no clock/randomness/network
   sha256:      LOCKED AT APPROVAL

3. PROMPT CONFORMANCE CHECKER
   path:        path-a/build/v3_prompt_conformance_checker.py
   intent:      verify the realized prompts PRESERVE the foreclose-all properties (no B/C* leakage into
                hop1/direct_query; no terminal/answer collision; controls intact) AND that the four-context
                character-count delta <= 8 (the §4/F1 gate)
   inputs:      the realized prompts (per item, four contexts); item specs / ground truth
   outputs:     per-item conformance result (per-property pass/fail + char-delta); aggregate summary;
                pass/fail gate for "prompt-realization conformance" (§9 condition vi)
   deterministic: pure function of inputs; no clock/randomness/network
   sha256:      LOCKED AT APPROVAL

4. NEUTRAL-TOKEN POOL / FILLER RESOURCE
   path:        path-a/build/v3_neutral_token_pool.md
   intent:      the explicit, auditable pool of neutral connective/template material the realizer uses to
                render specs into prompts (distinct from, and building on — NOT replacing — the construction
                role-token pool v3_token_pool.md d5f3594c… and the direct-query filler v3_direct_query_filler.md
                7ff83ab8…)
   deterministic: a fixed resource; the realizer's output is a pure function of (spec, this pool)
   sha256:      LOCKED AT APPROVAL
   EMBEDDING NOTE: if the neutral pool is instead embedded as constants inside the realizer rather than a
                separate file, that must be stated explicitly and the REALIZER digest binds the pool (no
                separate file digest). Default here: a separate named file.
```

## 4. Prompt-realization requirements (length-matching = exact tolerance — CS edit F1)

The generated items are **schema-level specs, not prompts**. Before any run:

```text
- four-context prompt realization (by the realizer #2): each item -> concrete prompts for
  composite / hop1 / hop2 / direct_query; no leakage of B or C* into hop1 / direct_query

PROMPT LENGTH-MATCHING (F1; exact):
  Within each four-context item set, prompts must use the SAME TEMPLATE CLASS and the residual
  character-count delta across composite / hop1 / hop2 / direct_query must be <= 8 CHARACTERS.
  CHARACTER COUNT IS THE GATING LENGTH METRIC. TOKEN COUNTS ARE DIAGNOSTIC ONLY.
  (MAX_DELTA = 8 characters per four-context item set.)

- prompt-level conformance (by the checker #3) must confirm realized prompts preserve foreclose-all
  properties AND meet the <= 8 char delta, before the construct is called "clean" at the executable level (§9 vi).
```

**SE feasibility note (flagged, not a HOLD).** The same-template-class + ≤ 8-char constraint across the **composite** context (which references TWO relations: the r1→r2 nesting) and the **single-hop** contexts (which reference ONE relation) is a **non-trivial realizer target** — a natural-language composite query is structurally longer than a single-hop query, so holding the delta ≤ 8 characters likely requires a **length-controlled / fixed-slot query format** in the realizer. Whether MAX_DELTA = 8 is achievable is **validated at SE-verify-tool-bytes / CS-feasibility-re-review** (after the realizer exists), per §F3 routing. If it proves infeasible, the resolution is **realizer redesign or a TL/Manager tolerance decision at that gate — NOT loosening any C5-cleared claim boundary**. The value 8 is used as instructed; this note records the dependency so the right gate catches it.

## 5. Planned N=96 materialization requirements

```text
- the 8-item batch is a DEMONSTRATION; the run requires the full N=96 materialized (specs), each passing
  C1–C9 admissibility in real-run mode before any run
- position cycles 1..p across the 96; seeds = item index; determinism re-verified on the 96
- N=96 chosen for comparability with the C0 scout (96 per cell)
```

## 6. Component floor definitions *(C5-cleared — unchanged)*

```text
DERIVED COMPONENT (CHANCE) FLOOR (locked):  F = max(1/p,1/m,1/D) = 0.20
COMPOSITE SUCCESS THRESHOLD (locked):       F + margin = 0.45
COMPONENT RELIABILITY FLOOR (SE-proposed; LOCKED AT APPROVAL): hop1 = 0.75, hop2 = 0.75 (C0-comparable)

DIRECT-QUERY CEILING — EXACT POINT-COUNT:
  <= 19/96 PASSES; >= 20/96 FAILS (direct-recall shortcut; set-level invalidator). POINT-COUNT, NOT a Wilson rule.

INVALIDATED-FRACTION CEILING — set-level (SE-proposed; LOCKED AT APPROVAL):
  <= 9/96 tolerated (items excluded + logged, §8); >= 10/96 -> CONSTRUCT-FAIL / MIS-SPECIFIED for this run.
```

## 7. Hop2 floor metric (PRIMARY) *(C5-cleared — unchanged)*

```text
METRIC:   hop2-isolated retrieval = (# items hop2 returns correct C*) / (post-exclusion denominator, §8),
          under V3 competition (D=5 competitors present).
DECISION INPUT (strict): lower bound of Wilson 95% CI > 0.75.
MIN COUNT (full N=96): 81/96 clears (SE-verified: Wilson lower 0.7581 > 0.75; 80/96 = 0.7463 does NOT clear).
          Exclusions -> analyzer recomputes exact Wilson rule on the post-exclusion denominator (§E4).
WHAT CLEARING MEANS: a COMPONENT-ADMISSIBILITY result. NOT capability, NOT certification, NOT composition.
  REQUIRED INTERPRETATION: "If hop2 clears, it means only that second-hop retrieval is reliable enough
  under V3 competition to make a later composite test interpretable."
Reported ALONE with its own CI. NOT a composite pass rate, NOT averaged with hop1, NOT collapsed.
```

## 8. Control checks + R6 invalidator handling *(C5-cleared — unchanged)*

```text
R6 INVALIDATORS — single rule, two levels (NOT zero-tolerance):
  ITEM-LEVEL: if an item-level R6 invalidator fires, the item is EXCLUDED from the relevant validated
              numerator and LOGGED. Item-level R6 invalidators are EXACTLY the five non-circular ones:
              terminal-coincidence, controls-unavailable, direct-recall, interior-position, constant-token.
  SET-LEVEL:  invalidated count <= 9/96 tolerated; >= 10/96 -> CONSTRUCT-FAIL / MIS-SPECIFIED (§10).
  "BELOW-FLOOR": hop2-below-floor is NOT an item-level invalidator; it is the PRIMARY SET-LEVEL FLOOR
              OUTCOME (§7, §10). Item-level "below-floor" refers ONLY to construction-admissibility floor
              structure caught by C1–C9, never the hop2 retrieval outcome. The primary metric does not
              invalidate its own items.

OTHER CONTROLS (each reported separately; none collapsed):
  - hop1 floor:           lower Wilson 95% bound > 0.75 (§E4). Below floor -> CONSTRUCT problem.
  - direct-query control: dq C* count vs the 19/96 point ceiling (§6).
  - dominance control:    DOMINANT_RATE_THRESHOLD = 0.25 — a single competitor/decoy absorbing > 25% of the
                          off-target mass is flagged (fixed-shortcut signal), reported not pass/fail.
  - four-context load-matching: per the §4 character-count metric, verified by the checker (#3).
  - construction admissibility: C1–C9 inspector PASS in real-run mode for all N=96 (precondition, §5).
```

## E4. hop1 floor CI treatment *(C5-cleared — unchanged)*

```text
hop1 clears IFF lower Wilson 95% bound > 0.75. At N=96, 81/96 is the minimum count (SE-verified; 80/96 fails).
Exclusions -> analyzer computes the exact Wilson rule on the post-exclusion denominator and reports the
resulting minimum count. 81/96 is the full-N reference, not a hardcoded count.
```

## 9. Decision rule *(C5-cleared — unchanged; clean construct contingent on prompt-realization conformance)*

```text
COMPONENT-ADMISSIBLE-UNDER-COMPETITION (the only "gate clears" outcome) requires ALL of:
  (i)   hop2-isolated lower Wilson 95% bound > 0.75,
  (ii)  direct-query C* count <= 19/96 (point count),
  (iii) hop1-isolated lower Wilson 95% bound > 0.75,
  (iv)  invalidated item count <= 9/96,
  (v)   C1–C9 admissibility PASS for all materialized items, AND
  (vi)  PROMPT-REALIZATION CONFORMANCE PASS (checker #3): foreclose-all properties preserved AND <= 8 char delta.
  -> THEN: component admissible under competition on V3. OPENS — does not answer — the composite /
     certified-baseline question (separate prereg). NOT certification.

CLEAN-CONSTRUCT BOUNDARY: clean at the SPEC level only until prompt-realization conformance passes (vi). A
  spec-clean, prompt-unchecked construct is NOT eligible for a substrate conclusion.
The composite, if computed, is interpreted ONLY in light of hop2 admissibility (the C0 lesson).
```

## 10. Null / fail / substrate-infeasibility branches *(C5-cleared — unchanged)*

```text
ONE-RUN EVIDENCE TOWARD SUBSTRATE-INFEASIBILITY (single-run outcome — NOT final):
  hop2 does NOT clear 0.75 while (ii)–(vi) hold (clean executable construct) -> this run is EVIDENCE TOWARD
  substrate-infeasibility under V3 at the locked load. NOT, by itself, final proof.
FINAL SUBSTRATE-INFEASIBILITY CLASSIFICATION (requires REPEATED admissible failures):
  Made only after repeated hop2-below-floor results across admissible runs (clean construct each time), per
  the constructibility framework's repeated-failure discipline. One clean failed run does NOT become a final
  claim; a below-floor result is NEVER a license to loosen the 0.75 floor, lower D, or tune to the data.
CONSTRUCT-FAIL (NOT a substrate result, at any count):
  invalidated >= 10/96, OR dq count >= 20/96, OR hop1 below floor, OR C1–C9 admissibility fails, OR prompt-
  realization conformance fails -> the TEST is invalid, not the substrate. Fix the construct and re-pre-register.
```

## 11. Forbidden interpretations *(C5-cleared — unchanged)*

```text
- hop2-below-floor is NOT "V3 is a bad construction"; V3 is verified-conformant. It is a substrate finding
  (one-run evidence, §10), not an instrument defect.
- hop2-clears is NOT certification and NOT a composition claim; it opens the composite question only.
- The composite result is NOT a standalone pass; interpreted only in light of hop2.
- NO mechanism claims (traversal vs grab vs anchor not decidable here).
- Survival is not correctness: C* counts only if it is the RIGHT C* via the bridge, controls clearing, no invalidator.
- "Not ruled out" is not "established." A single clean failed run is evidence TOWARD substrate-infeasibility, not final.
```

## 12. Stop rule *(C5-cleared — unchanged; analyzer/tooling digests fixed before run)*

```text
- N fixed at 96. Floors (0.75; 0.20; 19/96 dq; 9/96 invalidated; 0.45 composite), the §9 rule, and the §T
  tooling digests (analyzer/realizer/checker/neutral-pool) are fixed BEFORE the run and computed/applied ONCE.
- NO post-hoc floor adjustment, NO slicing, NO re-running until it passes, NO tooling edit after data.
- An invalid construct (§10 construct-fail) is remedied by a NEW pre-registration.
- FINAL substrate-infeasibility is a separate determination across repeated admissible runs, not this single run.
```

## 13. Required artifacts (CS must produce before any run)

```text
- the four §T tooling artifacts (analyzer / realizer / checker / neutral-token pool), digests locked at
  approval, SE-verified from bytes
- full N=96 item materialization (specs), each passing C1–C9 admissibility in real-run mode
- four-context prompt realization (by the realizer), meeting the §4 <= 8 char delta
- prompt-level conformance results (by the checker), gating §9 (vi)
- clean-fetchable artifact hashes (sha256) for tooling, items, prompts, per-context conformance, analyzer output
- fixture-mode / real-run assertions: run executes in REAL-RUN mode (no _fixture_mode, no _sweep_mode),
  asserted in the run record and confirmed by the inspector per item
```

## 14. Execution boundary + routing (F3: tooling-build is a separate gated action)

```text
This preregistration authorizes:
  No build changes.  No analyzer creation.  No prompt realizer creation.  No prompt conformance checker
  creation.  No N=96 materialization.  No prompt generation for execution.  No model run.  No compression.
  No Claim C.  No Paper B.  No certification claim.  No capability claim.  No mechanism claim.

ROUTING (F3; no step may be skipped):
  Senior v0.4 draft
   -> TL/Manager TOOLING-BUILD authorization        (separate action; this prereg does NOT authorize it)
   -> CS builds analyzer / realizer / checker / neutral-token resource
   -> SE verifies tool bytes                          (digests for the §T lock)
   -> CS feasibility re-review
   -> TL approval
   -> Manager by-name RUN authorization               (the run gate; §13 real-run assertion in force)
   -> CS execution
   -> SE verification

The tooling artifacts (§T) are REQUIRED BEFORE APPROVAL and must be produced under the separate TL/Manager
tooling-build action above — NOT built inside this prereg. The Path A FP16 K=5 FAIL remains closed. SE drafts; SE locks nothing.
```

---

**The one to carry up:** v0.4 resolves CS F1–F3 without touching any C5-cleared boundary. **(F1)** Prompt length-matching is now exact: **same template class, residual character-count delta ≤ 8 characters across the four contexts; character count gates, token counts diagnostic only** — with an SE feasibility note that holding ≤8 chars across the 2-relation composite and 1-relation single-hop contexts is a non-trivial realizer target, validated at the post-realizer feasibility gate, and if infeasible resolved by realizer redesign or a TL/Manager tolerance call, never by loosening claim boundaries. **(F2)** All four tooling artifacts are named and lock-at-approval: analyzer `v3_floor_check_analyzer.py`, prompt realizer `v3_prompt_realizer.py`, prompt conformance checker `v3_prompt_conformance_checker.py`, neutral-token pool `v3_neutral_token_pool.md` (separate file by default; if embedded, the realizer digest binds it) — each with path/intent/inputs/outputs/deterministic-behavior/sha256-locked. **(F3)** The tooling build is a **separate TL/Manager-gated action**, not authorized here; routing is Senior-draft → TL/Manager tooling-build authorization → CS builds → SE verifies tool bytes → CS feasibility re-review → TL approval → Manager by-name run authorization → CS execution → SE verification. **C5-cleared boundaries preserved verbatim:** hop2 standalone primary; lower Wilson > 0.75 (hop2 and hop1); 81/96 full-N; dq ≤19/96 pass / ≥20/96 fail; R6 item-exclude/log + set ≥10/96 construct-fail; hop2-below-floor not an item-level invalidator; one run = evidence toward substrate-infeasibility, not final; clean construct contingent on prompt-realization conformance; no certification/capability/mechanism/composition overclaim. Authorizes no build, no tooling creation, no materialization, no prompt generation, no model run. FAIL closed. CS to commit these bytes verbatim to a C5-readable in-review path; digest below.

— Senior Engineer (floor-check prereg v0.4; routes for CS feasibility re-review)
