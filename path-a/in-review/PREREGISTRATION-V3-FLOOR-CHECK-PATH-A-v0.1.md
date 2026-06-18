# PREREGISTRATION — V3 FLOOR CHECK (Path A) v0.1

**E. A. Flores**, Apiana AI, Inc. — June 17, 2026
*River and Canyon · Path A. Drafted by the Senior Engineer (lock-before-look). Routes for review and approval; SE locks nothing and authorizes no run.*

> **Framing.** V3 conforms *structurally* to the foreclose-all standard (byte-audit `c3f4e667…`, build verification `e9b7e349…`). **V3 is not certified.** This floor check is the empirical test of whether the substrate can operate under the foreclose-all standard at the locked load. **If V3 fails, substrate-infeasibility remains a valid outcome** — a real finding, never a license to loosen the floor.

## 1. Research question

```text
PRIMARY:  Does hop2 (the second hop, B -> C*) clear its reliability floor when queried in
          isolation under V3's same-depth-competitor competition?
```

This is the same question that foreclosed C0 (where hop2-isolated cleared its 0.75 floor only at the trivial K=1), now asked on a construction that forecloses every non-traversal route. The primary metric is **hop2-isolated retrieval**, reported against its floor. It is **not** a composite pass rate, and the result must not be collapsed into one (see §7–§11).

## 2. Locked construction source

```text
TARGET-CONSTRUCT-DEFINITION-v0.4         4b616afb919114ee…   (of-record; defines R1–R7 + outcome rules)
PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3 38e054601eda2ab6…  (V3 same-depth-competitor design)
PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4  c61a3256d26e0ed0…  (of-record; instrument byte-binding,
                                                              re-locked; supersedes v0.3 d9bd9b21…)
```

The foreclose-all standard and V3's seven properties are inherited from these locked sources; this prereg does not restate or modify them.

## 3. Build artifact inputs and digests (SE-verified at HEAD `703b3a3`)

```text
v3_item_generator.py        6a2ceee15442ebbd…   (realizes V3; verified PASS, build return e9b7e349…)
v3_conformance_runner.py    2a4408353e3713e3…
v3_token_pool.md            d5f3594ce42a9e55…
v3_direct_query_filler.md   7ff83ab82de13c7d…
v3_relation_balance.md      de45d2a9bb640177…
v3_seed_plan.md             f501f741f47faafd…
inspector.py (instrument)   cb4b0b60bd6dc2b5…   (matches v0.4 re-pin)
constants.py (instrument)   1d761c3d1c56e7ac…   (matches v0.4 re-pin; F=0.20, threshold=0.45)
```

The build was verified to realize V3, honor the locked values, be deterministic (two runs byte-identical; regenerated == committed items), and pass C1–C9 admissibility on the 8-item demonstration batch in real-run mode. **The build verified schema-level specs, not full prompt-realization or N=96 materialization** (§4, §5).

## 4. Prompt-realization requirements (the gap this prereg makes explicit)

The generated items are **schema-level construction specs** (the form the inspector consumes), **not prompts**. Before any run, the specs must be realized into concrete prompts for the four contexts, and that realization is itself an artifact to be checked:

```text
- four-context prompt realization: each item -> concrete prompt strings for
    composite (A -> ? via the full chain), hop1 (A -r1-> ?), hop2 (B -r2-> ?), direct_query (filler {W} holds {V})
- prompts must be length/format-matched across contexts (the four-context control rides on this)
- prompt realization must NOT introduce any cue absent from the spec (no leakage of C* or B into hop1/dq)
- a prompt-level conformance check must confirm the realized prompts preserve the spec's foreclose-all
  properties (no introduced shortcut, no terminal/answer collision, controls intact)
```

Prompt realization is **gated by Manager by-name authorization**; it is not performed by this prereg and was not performed by the build.

## 5. Planned N=96 materialization requirements

```text
- the 8-item batch is a DEMONSTRATION; the run requires the full N=96 materialized
- the generator's per-item prefix scheme generalizes to N=96 without schema change (verified), but
  all 96 must be generated and EACH must pass C1–C9 admissibility in real-run mode before any run
- position must cycle 1..p across the 96 as specified; seeds = item index; determinism re-verified on the 96
- N=96 chosen for comparability with the C0 scout (which ran 96 per cell)
```

## 6. Component floor definitions

```text
DERIVED COMPONENT FLOOR (locked in constants.py):
  F = max(1/p, 1/m, 1/D) = max(1/5, 1/10, 1/5) = 0.20   — the rate a non-traversal route achieves by
                                                           construction (depth/salience/position all 1/D-class)
COMPOSITE SUCCESS THRESHOLD (locked):
  F + margin = 0.20 + 0.25 = 0.45                        — a composite at/below this is not evidence of traversal

COMPONENT RELIABILITY FLOOR (pre-declared here; LOCKED AT APPROVAL):
  hop1 floor = 0.75   and   hop2 floor = 0.75
  Rationale: a component that succeeds in isolation less than ~3/4 of the time is too unreliable for a
  composite failure to be attributable to COMPOSITION rather than to component fragility. 0.75 is chosen
  for DIRECT COMPARABILITY with the C0 scout, which used the same hop2 floor. (SE proposes 0.75; the value
  is locked by TL/Manager at approval, not by SE.)

DIRECT-QUERY CEILING (pre-declared; LOCKED AT APPROVAL):
  direct_query retrieval of C* must be AT OR BELOW F = 0.20 (i.e., at/below chance). Above the ceiling =
  a direct-recall shortcut (R6 invalidator) — the model is producing C* without traversing the bridge.
```

The reliability floor (0.75) and the derived/chance floor (0.20) measure **different things** and are kept separate: 0.75 asks "does the component *work*"; 0.20 is "what chance/non-traversal achieves." The PRIMARY question (§7) is the reliability question.

## 7. Hop2 floor metric (PRIMARY)

```text
METRIC:   hop2-isolated retrieval rate = (# items where the hop2 context returns the correct C*) / N,
          with C* defined by the locked construction (B -r2-> C*), scored against the materialized
          ground truth, under the V3 competition structure (D=5 same-depth competitors present).
INTERVAL: Wilson 95% CI on the rate.
DECISION INPUT: hop2-isolated rate vs the 0.75 floor (lower CI bound vs floor handled in §9).
NOT: a composite pass rate. NOT averaged with hop1. NOT collapsed with the composite. Reported alone,
     as its own number, with its own CI.
```

## 8. Control checks (each reported separately; none collapsed)

```text
- hop1 floor:           hop1-isolated retrieval (A -r1-> B) vs 0.75. If hop1 is below floor, the item set
                        is broken (the easy direct lookup fails) — a CONSTRUCT problem, not a substrate result.
- direct-query control: dq retrieval of C* vs the 0.20 ceiling. Above ceiling -> direct-recall invalidator.
- dominance control:    DOMINANT_RATE_THRESHOLD = 0.25 — if a single competitor/decoy absorbs > 25% of the
                        off-target mass, the error is concentrated (a fixed-shortcut signal), flagged not pass/fail.
- four-context load-matching: composite/hop1/hop2/dq must be load-matched per the construction; verified at
                        prompt realization (§4).
- R6 invalidators:      terminal-coincidence, controls-unavailable, direct-recall, interior-position,
                        constant-token, below-floor. ANY firing invalidates the construct for that item.
- construction admissibility: C1–C9 inspector PASS in real-run mode for all N=96 (precondition, §5).
```

## 9. Decision rule (computed once, after the run, against these pre-declared conditions)

```text
COMPONENT-ADMISSIBLE-UNDER-COMPETITION  (the only "gate clears" outcome) requires ALL of:
  (i)   hop2-isolated rate clears the 0.75 floor (lower Wilson bound > 0.75 floor — strict),
  (ii)  direct_query at/below the 0.20 ceiling (no direct-recall shortcut),
  (iii) hop1-isolated clears the 0.75 floor (the component chain is retrievable),
  (iv)  no R6 invalidator fires at the set level,
  (v)   C1–C9 admissibility PASS for all materialized items.
  -> THEN: the component operation is admissible under competition on V3. This OPENS — does not answer —
     the composite/certified-baseline question (a SEPARATE prereg). It is NOT certification.

ANY condition unmet -> route to the matching branch in §10. The composite, if computed, is interpreted
ONLY in light of hop2 admissibility (a composite number with hop2 below floor is uninformative — the C0 lesson).
```

## 10. Null / fail / substrate-infeasibility branches

```text
NULL (hop2 at/below floor, clean construct):
  hop2-isolated does NOT clear 0.75 while (ii)–(v) hold -> the substrate cannot reliably perform hop2 under
  V3 competition at the locked load. This is the SUBSTRATE-INFEASIBILITY outcome.

SUBSTRATE-INFEASIBILITY (the honest finding):
  A hop2-below-floor result with a clean construct (controls clear, no invalidators, admissibility passes) is
  a VALID finding: even with every non-traversal route foreclosed and a verified-conformant construction, the
  substrate does not do the second hop under competition. This is the STRONGER version of the C0 result and is
  NEVER a license to loosen the 0.75 floor, lower D, or otherwise tune until the number cooperates.

CONSTRUCT-FAIL (NOT a substrate result):
  If an R6 invalidator fires, OR direct_query exceeds its ceiling, OR hop1 is below floor, OR admissibility
  fails for any item -> the TEST is invalid, not the substrate. Fix the construct and re-pre-register; do NOT
  draw a substrate conclusion from an invalid construct.
```

## 11. Forbidden interpretations

```text
- A hop2-below-floor result is NOT "V3 is a bad construction." V3 is verified-conformant; a below-floor
  result is a SUBSTRATE finding about the model, not a defect in the instrument.
- A hop2-clears-floor result is NOT certification and NOT a composition claim. It means only that the
  component is admissible under competition — it opens the composite question, nothing more.
- The composite result is NOT reported as a standalone pass. It is interpreted only in light of hop2.
- NO mechanism claims (why hop2 succeeds or fails — traversal vs grab vs anchor — is not decidable here).
- Survival is not correctness: producing C* is not a pass unless it is the RIGHT C* via the bridge with
  controls clearing and no invalidator.
- "Not ruled out" is not "established"; absence of an invalidator is not evidence of composition.
```

## 12. Stop rule

```text
- N is fixed at 96. The floors (0.75 reliability; 0.20 chance/ceiling; 0.45 composite threshold) and the
  §9 decision rule are fixed BEFORE the run and computed ONCE.
- NO post-hoc floor adjustment. NO slicing for a "better" sub-condition. NO re-running until it passes.
- A single pre-declared run produces a single disposition per §9/§10. If the construct is invalid (§10
  construct-fail), the remedy is a NEW pre-registration, not a re-analysis of this run.
```

## 13. Required artifacts (CS must produce before any run)

```text
- full N=96 item materialization (specs), each passing C1–C9 admissibility in real-run mode
- four-context prompt realization (composite / hop1 / hop2 / direct_query), length/format-matched
- prompt-level conformance checks confirming the realized prompts preserve foreclose-all properties
- clean-fetchable artifact hashes (sha256) for all items, prompts, and per-context conformance results
- fixture-mode / real-run assertions: the run executes in REAL-RUN mode (no _fixture_mode, no _sweep_mode);
  the run record must assert this and the inspector must confirm it per item
```

## 14. Execution boundary

```text
- This preregistration authorizes NO run. It does not authorize build changes, full N=96 materialization,
  prompt generation for model execution, model loading, inference, the floor-check run, compression,
  certification, Claim C, Paper B, capability claim, or mechanism claim.
- Routing (no step may be skipped):
    SE draft -> CS feasibility review -> C5 claim-risk review -> TL approval
       -> Manager by-name authorization -> CS execution -> SE verification
- At run time, Manager by-name authorization is required, with the §13 real-run assertion in force.
- The Path A FP16 K=5 FAIL remains closed and untouched. SE drafts this prereg; SE locks nothing.
```

---

**The one to carry up:** This locks the next empirical question — *does hop2 clear its reliability floor under V3 competition?* — with hop2-isolated retrieval as the **primary metric, reported alone against a 0.75 floor (chosen for comparability with the C0 scout), never collapsed into a composite pass**. hop1, direct-query, dominance, invalidators, and C1–C9 admissibility are separate controls. The only "gate clears" outcome is **component-admissible-under-competition** (hop2 clears, dq below chance, hop1 clears, no invalidators, admissibility passes) — which *opens* the composite/certification question, and is **not** itself certification. A hop2-below-floor result with a clean construct is **substrate-infeasibility** — a valid, stronger-than-C0 finding, never a license to loosen the floor. The build verified schema-level specs only; before any run CS must produce full N=96 materialization, four-context prompt realization, prompt-level conformance checks, clean-fetchable hashes, and real-run assertions. This prereg authorizes no run; it routes SE-draft → CS feasibility → C5 claim-risk → TL approval → Manager by-name authorization → CS execution → SE verification, no step skipped. FAIL stays closed.

— Senior Engineer (floor-check prereg draft; routes for review and approval)
