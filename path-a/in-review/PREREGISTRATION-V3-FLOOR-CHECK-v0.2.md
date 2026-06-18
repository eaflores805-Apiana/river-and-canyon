# PREREGISTRATION — V3 FLOOR CHECK (Path A) v0.2

**E. A. Flores**, Apiana AI, Inc. — June 17, 2026
*River and Canyon · Path A. Drafted by the Senior Engineer (lock-before-look). Revises v0.1 (`ceaa2e67…`) per TL ACTION after C5 HOLD — ARTIFACT ACCESS. Routes for review and approval; SE locks nothing and authorizes no run.*

> **Framing.** V3 conforms *structurally* to the foreclose-all standard (byte-audit `c3f4e667…`, build verification `e9b7e349…`). **V3 is not certified.** This floor check tests whether the substrate can operate under the foreclose-all standard at the locked load. **If V3 fails, that is evidence toward substrate-infeasibility under V3 — not, by one run, a final classification** (§10).

> **Staging note (edit 1).** This v0.2 is produced as canonical bytes with the SE digest below for **verbatim commit by CS** into a C5-readable in-review repo path (SE does not push to the repo). C5's next review must be against the committed bytes; a digest match to the SE digest confirms C5 reads exactly this draft. Access-confirmation follows CS's commit.

## 1. Research question

```text
PRIMARY:  Does hop2 (the second hop, B -> C*) clear its reliability floor when queried in
          isolation under V3's same-depth-competitor competition?
```

The primary metric is **hop2-isolated retrieval**, reported alone against its floor (§7). It is **not** a composite pass rate and must not be collapsed into one (§7–§11).

## 2. Locked construction source (current of-record; the v0.4 HOLD is resolved, not reopened — edit 7)

```text
TARGET-CONSTRUCT-DEFINITION-v0.4              4b616afb919114ee…   (of-record)
PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3     38e054601eda2ab6…   (V3 same-depth-competitor design)
PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4  c61a3256d26e0ed0226e46a60d9b701baddfe3006249db687f221aea57315955
                                              (CURRENT of-record; placeholder-fill corrective committed
                                               9ea16d1; supersedes v0.3 d9bd9b21…. This prereg binds to
                                               c61a3256. The resolved v0.4 byte-binding HOLD is NOT reopened.)
```

## 3. Build artifact inputs and digests (SE-verified at HEAD `703b3a3`; re-pinned instrument — edit 7)

```text
v3_item_generator.py        6a2ceee15442ebbd…       v3_relation_balance.md   de45d2a9bb640177…
v3_conformance_runner.py    2a4408353e3713e3…       v3_seed_plan.md          f501f741f47faafd…
v3_token_pool.md            d5f3594ce42a9e55…       v3_direct_query_filler.md 7ff83ab82de13c7d…
inspector.py  (instrument)  cb4b0b60bd6dc2b5…   ← current re-pinned binding (matches v0.4)
constants.py  (instrument)  1d761c3d1c56e7ac…   ← current re-pinned binding (matches v0.4; F=0.20, threshold=0.45)
```

Build verified (return `e9b7e349…`) to realize V3, honor locked values, be deterministic, and pass C1–C9 admissibility on the 8-item demonstration batch in real-run mode — **at the schema/spec level only** (§4–§6).

## 4. Prompt-realization requirements

The generated items are **schema-level construction specs**, not prompts. Before any run:

```text
- four-context prompt realization: each item -> concrete prompts for composite / hop1 / hop2 / direct_query
- prompts length/format-matched across contexts; no leakage of B or C* into hop1 / direct_query
- a prompt-level conformance check must confirm the realized prompts PRESERVE the foreclose-all properties
  (no introduced shortcut, no terminal/answer collision, controls intact)
```

Prompt realization is gated by Manager by-name authorization; not performed here.

## 5. Planned N=96 materialization requirements

```text
- the 8-item batch is a DEMONSTRATION; the run requires the full N=96 materialized
- the generator's per-item prefix scheme generalizes to N=96 without schema change (verified), but all 96
  must be generated and EACH must pass C1–C9 admissibility in real-run mode before any run
- position cycles 1..p across the 96; seeds = item index; determinism re-verified on the 96
- N=96 chosen for comparability with the C0 scout (96 per cell)
```

## 6. Component floor definitions

```text
DERIVED COMPONENT (CHANCE) FLOOR (locked in constants.py):
  F = max(1/p, 1/m, 1/D) = max(1/5, 1/10, 1/5) = 0.20    — what a non-traversal route achieves by construction
COMPOSITE SUCCESS THRESHOLD (locked):
  F + margin = 0.20 + 0.25 = 0.45

COMPONENT RELIABILITY FLOOR (SE-proposed; LOCKED AT APPROVAL):
  hop1 floor = 0.75   and   hop2 floor = 0.75
  Rationale: a component succeeding in isolation < ~3/4 of the time is too unreliable for a composite
  failure to be attributable to COMPOSITION rather than component fragility. 0.75 chosen for direct
  comparability with the C0 scout. (SE proposes; TL/Manager lock the value.)

DIRECT-QUERY CEILING — EXACT N=96 COUNT (edit 3):
  direct-query C* count <= 19/96  -> PASSES the ceiling (at/below the 0.20 chance floor)
  direct-query C* count >= 20/96  -> FAILS the ceiling -> direct-recall shortcut (R6 invalidator at set level)

INVALIDATED-FRACTION CEILING — set-level construct-validity gate (edit 2; SE-proposed, LOCKED AT APPROVAL):
  invalidated item count <= 9/96   -> tolerated (items excluded from numerator, logged; see §8)
  invalidated item count >= 10/96  -> construct deemed MIS-SPECIFIED / construct-fail for this run
  Rationale: a construct producing > ~10% invalid items is not cleanly measuring what it claims. (SE
  proposes 10%; TL/Manager lock the value.)
```

The reliability floor (0.75, "does the component work") and the chance floor (0.20, "what a shortcut gets") measure different things and are kept separate.

## 7. Hop2 floor metric (PRIMARY) — Wilson strictness, bounded claim (edit 4)

```text
METRIC:   hop2-isolated retrieval rate = (# items where the hop2 context returns the correct C*) /
          (# items NOT excluded by item-level invalidation, §8), C* per the locked construction,
          under the V3 competition structure (D=5 same-depth competitors present).
DECISION INPUT (kept strict): lower bound of the Wilson 95% CI on the rate > 0.75.

WHAT CLEARING MEANS (and does NOT mean):
  Clearing the hop2 floor is a COMPONENT-ADMISSIBILITY result. It is NOT a capability claim, NOT a
  certification result, and NOT evidence of composition.
  REQUIRED INTERPRETATION: "If hop2 clears, it means only that second-hop retrieval is reliable enough
  under V3 competition to make a later composite test interpretable."

Reported ALONE, with its own CI. NOT a composite pass rate, NOT averaged with hop1, NOT collapsed.
```

## 8. Control checks + R6 invalidator handling (item-level / set-level split — edit 2)

```text
R6 INVALIDATORS — handled at two levels (NOT zero-tolerance):
  ITEM-LEVEL:  if an R6 invalidator (terminal-coincidence, controls-unavailable, direct-recall,
               interior-position, constant-token, below-floor) fires on an item, that ITEM is EXCLUDED
               from the validated numerator and logged separately. One invalidated item does NOT fail
               the construct.
  SET-LEVEL:   if the invalidated fraction exceeds the §6 ceiling (>= 10/96), the construct is deemed
               mis-specified / construct-fail for this run (§10 construct-fail).

OTHER CONTROLS (each reported separately; none collapsed into the primary):
  - hop1 floor:           hop1-isolated retrieval (A -r1-> B) vs 0.75. Below floor -> CONSTRUCT problem.
  - direct-query control: dq C* count vs the 19/96 ceiling (§6). >= 20/96 -> direct-recall (set-level invalidator).
  - dominance control:    DOMINANT_RATE_THRESHOLD = 0.25 — a single competitor/decoy absorbing > 25% of the
                          off-target mass is flagged (fixed-shortcut signal), reported not pass/fail.
  - four-context load-matching: verified at prompt realization (§4).
  - construction admissibility: C1–C9 inspector PASS in real-run mode for all N=96 (precondition, §5).
```

## 9. Decision rule (computed once; "clean construct" scoped to spec + realized prompts — edit 6)

```text
COMPONENT-ADMISSIBLE-UNDER-COMPETITION (the only "gate clears" outcome) requires ALL of:
  (i)   hop2-isolated lower Wilson 95% bound > 0.75,
  (ii)  direct-query C* count <= 19/96 (no direct-recall shortcut),
  (iii) hop1-isolated clears its 0.75 floor,
  (iv)  invalidated fraction <= 9/96 (set-level construct validity, §8),
  (v)   C1–C9 admissibility PASS for all materialized items, AND
  (vi)  PROMPT-REALIZATION CONFORMANCE PASS (the construct is "clean" at the EXECUTABLE level, not merely
        the spec level — see boundary below).
  -> THEN: the component operation is admissible under competition on V3. This OPENS — does not answer —
     the composite / certified-baseline question (a SEPARATE prereg). It is NOT certification.

CLEAN-CONSTRUCT BOUNDARY (edit 6):
  The construct is "clean" at the SPEC level only until prompt-realization conformance passes. The
  EXECUTABLE construct is not called clean until the rendered prompts are checked (vi). A spec-clean,
  prompt-unchecked construct is NOT eligible for a substrate conclusion.

The composite, if computed, is interpreted ONLY in light of hop2 admissibility (a composite number with
hop2 below floor is uninformative — the C0 lesson).
```

## 10. Null / fail / substrate-infeasibility branches (repeated-failure discipline — edit 5)

```text
ONE-RUN EVIDENCE TOWARD SUBSTRATE-INFEASIBILITY (the single-run outcome — NOT a final classification):
  hop2-isolated does NOT clear 0.75 while (ii)–(vi) hold (clean executable construct) -> this run is
  EVIDENCE TOWARD substrate-infeasibility under V3 at the locked load. It is NOT, by itself, final proof.

FINAL SUBSTRATE-INFEASIBILITY CLASSIFICATION (requires repeated admissible failures):
  A FINAL substrate-infeasibility classification for V3 is made only after REPEATED hop2-below-floor
  results across admissible runs (clean construct each time), per the constructibility framework's
  repeated-failure discipline. One clean failed run does NOT become an overstrong final claim, and a
  below-floor result is NEVER a license to loosen the 0.75 floor, lower D, or tune until the number cooperates.

CONSTRUCT-FAIL (NOT a substrate result, at any count):
  If invalidated fraction >= 10/96, OR direct-query count >= 20/96, OR hop1 below floor, OR C1–C9
  admissibility fails, OR prompt-realization conformance fails -> the TEST is invalid, not the substrate.
  Fix the construct and re-pre-register; draw NO substrate conclusion from an invalid construct.
```

## 11. Forbidden interpretations

```text
- A hop2-below-floor result is NOT "V3 is a bad construction." V3 is verified-conformant; a below-floor
  result is a substrate finding (one-run evidence, §10), not an instrument defect.
- A hop2-clears result is NOT certification and NOT a composition claim. It opens the composite question only.
- The composite result is NOT reported as a standalone pass; interpreted only in light of hop2.
- NO mechanism claims (traversal vs grab vs anchor is not decidable here).
- Survival is not correctness: producing C* counts only if it is the RIGHT C* via the bridge, controls
  clearing, no invalidator.
- "Not ruled out" is not "established"; absence of an invalidator is not evidence of composition.
- A single clean failed run is evidence TOWARD substrate-infeasibility, not a final classification (§10).
```

## 12. Stop rule

```text
- N fixed at 96. Floors (0.75 reliability; 0.20 chance; 19/96 dq ceiling; 9/96 invalidated ceiling; 0.45
  composite threshold) and the §9 decision rule are fixed BEFORE the run and computed ONCE.
- NO post-hoc floor adjustment, NO slicing for a "better" sub-condition, NO re-running until it passes.
- An invalid construct (§10 construct-fail) is remedied by a NEW pre-registration, not a re-analysis.
- A FINAL substrate-infeasibility classification is a separate determination across repeated admissible
  runs (§10), not a claim from this single run.
```

## 13. Required artifacts (CS must produce before any run)

```text
- full N=96 item materialization (specs), each passing C1–C9 admissibility in real-run mode
- four-context prompt realization (composite / hop1 / hop2 / direct_query), length/format-matched
- prompt-level conformance checks confirming the realized prompts preserve foreclose-all properties
- clean-fetchable artifact hashes (sha256) for all items, prompts, and per-context conformance results
- fixture-mode / real-run assertions: run executes in REAL-RUN mode (no _fixture_mode, no _sweep_mode),
  asserted in the run record and confirmed by the inspector per item
```

## 14. Execution boundary (preserved — edit 8)

```text
This preregistration authorizes:
  No model run.
  No full N=96 materialization.
  No prompt generation for execution.
  No compression.
  No Claim C.
  No Paper B.
  No certification claim.
  No capability claim.
  No mechanism claim.

Routing (no step may be skipped):
  SE draft -> CS feasibility review -> C5 claim-risk review -> TL approval
     -> Manager by-name authorization -> CS execution -> SE verification

At run time, Manager by-name authorization is required, with the §13 real-run assertion in force.
The Path A FP16 K=5 FAIL remains closed and untouched. SE drafts this prereg; SE locks nothing.
```

---

**The one to carry up:** v0.2 incorporates all C5/TL edits. hop2-isolated retrieval remains the **primary metric, reported alone against a 0.75 reliability floor with a strict lower-Wilson-bound rule**, explicitly bounded as a **component-admissibility floor — not capability, not certification, not composition** (clearing means only that hop2 is reliable enough to make a later composite test interpretable). R6 invalidators are handled **item-level (exclude + log) and set-level (≥10/96 invalidated → construct-fail)** — **not** zero-tolerance. The direct-query ceiling is an **exact count (≤19/96 pass, ≥20/96 fail)**. A single hop2-below-floor result on a clean construct is **one-run evidence toward substrate-infeasibility, not a final classification** (final requires repeated admissible failures). "Clean construct" is **scoped to spec + realized prompts** — prompt-realization conformance is required (§9 vi) before the executable construct is called clean. Provenance binds to the **current of-record v0.4 `c61a3256…`** and re-pinned instrument `cb4b0b60`/`1d761c3d`; the resolved v0.4 HOLD is not reopened. The prereg authorizes no run, no materialization, no prompt generation, no model execution; routes SE-draft → CS feasibility → C5 claim-risk → TL approval → Manager by-name authorization → CS execution → SE verification. FAIL stays closed. CS to commit these bytes verbatim into a C5-readable in-review path; digest below.

— Senior Engineer (floor-check prereg v0.2; routes for C5 claim-risk and CS feasibility)
