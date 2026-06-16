# PRE-REGISTRATION — Path A Load Scout, K = 1…5 (one-off, descriptive)

**E. A. Flores**, Apiana AI, Inc. — June 16, 2026
*River and Canyon · Path A. Drafted by the Senior Engineer. A single descriptive run — not a certification, not a project. Routes Senior-draft → TL approves → **Manager authorizes the run by name** → CS executes.*

> **What this is.** ONE run that sweeps clutter across **every integer K from 1 to 5** on the **existing construction**, to see how two things move with load: the **validated-R1 rate** and the **off-map positional rate**. The goal is to *see the effect* — does the failure grow, cliff, plateau, or fall as K climbs — and whether there's any hint of a "happy-medium" load worth a clean test later.
>
> **What this is NOT.** **Not a certification.** On the existing construction the six chains differ only by an arbitrary head token, so validated-R1 conflates *genuine composition* with *arbitrary-label-tracking*. Therefore **no K in this scout certifies a constructible baseline** — a band-hint is a *candidate K to certify later on a chain-identity-robust construction*, never a certified baseline (this is how the construction-validity constraint from CS/C4/C5 is honored: by **scoping the claim**, not by building a project first). Not a capability claim. Not a re-run of the closed K=5 FAIL — that artifact stays locked; the K=5 cell here **reproduces** it as an internal check. Not an authorization — the Manager authorizes the run by name.

---

## 1. The question (descriptive, by design)

```text
On the existing construction, across K ∈ {1, 2, 3, 4, 5}:
  Q1. How does validated-R1 move with K?  (rises / falls / cliffs / plateaus / non-monotone)
  Q2. How does the off-map POSITIONAL rate move with K?  (the "does more clutter →
      more wrong-address selection?" question, answered descriptively for THIS construction)
  Q3. Is there a hint of an interior band — a K where validated-R1 lifts while the
      confound margins stay strong — that would justify a clean certification test later?
```

No slope is presumed. One prior dot (K=5) licenses no trend, and the program's own terminal-attraction bounds-sweep ran **reverse-K** (reported ≈ 0.708→0.083 as K 1→5; *C5-reported, not yet byte-verified — to be confirmed before any load-bearing use*), so "more clutter → more failure" is not a safe default. The curve may ramp, cliff, plateau, fall, or be non-monotone. The scout measures the shape; it assumes none.

## 2. Run protocol (the instructions)

```text
CELLS:        K = 1, 2, 3, 4, 5   (five cells, one run)
CONSTRUCTION: the EXISTING construction (head-token-disambiguated chains), unchanged
ITEMS/CELL:   n = 96 (matches the locked K=5 run, for within-sweep comparability)
GENERATION:   per cell, generate the item set with K decoy chains under a DECLARED seed
              (seed family 20260615; per-cell seed recorded in the manifest), then
              materialize ground truth → items_materialized_K{k}.json (per-item entity sets);
              conformance-check each cell (target/decoy/competitor sets pairwise-distinct, R8).
CONTEXTS/ITEM: 4 — composite, hop1, hop2, direct-query  → 96 × 4 = 384 gens/cell
TOTAL:        5 × 384 = 1,920 generations  (CS estimate ≈ 25 min wall-clock, FP16; compute
              is not the constraint)
SCORER:       analyze.py — the PER-ITEM scorer (the one that produced the binding R1 in the
              K=5 run; NOT the single-representative-spec G6 path), run per cell. Emits
              per-item: composite/hop1/hop2/dq tokens, composite_category (R1–R6cat),
              controls_pass, invalidators, is_R1_candidate, is_R1_validated.
PROVENANCE:   one sweep manifest (RUN_MANIFEST_scout.json) with a per-cell block: commit hash,
              per-cell seed, per-cell artifact paths + digests. SE fetches each artifact and
              echoes a computed sha256 adjacent to the declared digest (reviewer-assertable).
CONSTANTS:    constants.py currently locks K=5 as a single value and inspector.py C9 enforces
              K-equality, which a sweep breaks in real-run mode. RESOLUTION FOR THIS ONE-OFF
              (CS, fast path): a per-cell locked spec that WAIVES C9-on-K-equality, with the
              K-list itself recorded as the locked object. (CS may instead implement a
              constants "sweep mode" if preferred long-term; either closes it. Small CS patch,
              pre-run.)
```

## 3. Locked metrics — declared BEFORE any cell is computed

**Primary (descriptive):**
```text
validated-R1 per cell = (composite == C*) AND hop1 retrievable AND hop2 retrievable AND
                        no invalidator fired   → rate + Wilson 95% CI.
  NOTE (the honesty mark, not a softening): on THIS construction "validated" means
  composition-CONDITIONAL-ON-label-tracking, because identifying the right chain requires
  the arbitrary head token. So the number is real and shortcut-resistant, but it is NOT
  pure-composition and does NOT certify (see §6). We still never use a raw rate — the
  validated metric is primary precisely because a raw "produced-something" rate peaks at
  trivial low K (Paper 1).
```

**Secondary (descriptive, reported alongside, never blended into the primary):**
```text
- OFF-MAP POSITIONAL RATE per cell = decoy answer-depth (dC) + decoy bridge (dB) landings.
  Labeled POSITIONAL — where tokens land vs K. NOT a mechanism-vs-K curve; it inherits the
  K=5 finding that the off-map mass is multi-mechanism (relation-keyed grab / chain-anchor
  inconsistency, not separable on this run). (F3 / CS#4 / C4.)
- TWO-DIAL DECOMPOSITION (C1, relabeled positional) per cell:
    Dial A = answer-depth landing rate  (fraction of outputs at depth-2 answer positions,
             target OR decoy)  — NOT "walk rate"; landing at answer-depth is not evidence of
             traversal (the run cannot see footsteps).
    Dial B = right-chain share among answer-depth landings (of those, fraction on the target
             chain), reported AGAINST the per-K base-rate expectation (wrong-chain share falls
             mechanically as K drops — fewer decoys — so a Dial-B "gain" must beat base rate,
             not merely fall).
- CROSS-QUERY CHAIN-MEMBERSHIP PATTERN per cell (the off-map record's instrument): does
  retrieval stay anchored to one chain across hop1/hop2/composite at this K — anchor-tracking
  / fixed / switching — gated on the component load-floor, reported as the PATTERN, NOT a
  consistency rate (the rate conflates real anchoring with fixed-target grabbing). This is the
  empirical "did the model HOLD chain identity at this load," distinct from any design property.
- CONTROL MARGINS per cell: terminal-grab rate, direct-query pass rate, depth-competitor
  (R4b) rate, control-floor headroom (hop1/hop2 retrieval). Recorded for the F1 read-flag.
```

## 4. Pre-declared read patterns, the null, and the stop-rule (lock-before-look)

A sweep invites fishing — re-gridding near an apparent peak until a band appears. Declared before any cell is computed:

```text
SHAPE PATTERNS (name the curve, chosen before look):
  ramp / cliff / plateau / interior-peak / reverse-K / flat.

BAND-HINT (what would make Q3 a "yes worth certifying later") — ALL of:
  (i)  validated-R1 markedly higher at some interior K than at the K=1 and K=5 ends;
  (ii) at that K, the CONTROL MARGINS are STABLE OR STRONGER, not weakest there — if the
       lift coincides with the K where confound separation is thinnest, it is a discrimination
       artifact, not a composition optimum (F1, C5 load-bearing: "a gate that opens because it
       went slack" — the validated-metric version of the mirage §3 already blocks for raw rates);
  (iii) Dial A (answer-depth landing) steady or up while Dial B (right-chain share) beats its
       per-K base rate — i.e. improvement is better chain selection, not the model ceasing to
       answer (C1 good-drop vs bad-drop).

THE NULL (forces "no band — file the curve"): validated-R1 flat or monotone across K with no
  interior lift meeting the band-hint conditions. Monotone-bad is a REAL descriptive result,
  not a failed scout.

BOUNDARY CASE (F2): if the best cell sits at a range edge (validated-R1 still rising at K=5,
  or best at K=1), the structure may extend beyond {1..5}. That is recorded as a descriptive
  caveat and, if pursued, becomes a SEPARATE one-off under its own lock — NOT an INDETERMINATE
  resolved by adding a K point to THIS run.

STOP-RULE: each cell is generated, run, and scored ONCE against these pre-declared patterns.
  No added K point after look, no re-slice of a cell, no new pattern defined post-hoc. Any
  extension is a fresh one-off pre-registration.
```

## 5. What the scout outputs

```text
- Two curves across K=1..5: validated-R1 (+CI) and off-map positional rate.
- The per-cell secondary panel: Dial A, Dial B-vs-base-rate, chain-membership pattern,
  control margins.
- A named shape (per §4) and a Q3 disposition: BAND-HINT (a candidate K to certify later) /
  NO BAND (file the curve) / BOUNDARY (structure may extend; separate one-off if pursued).
- A reproduction check: the K=5 cell should reproduce the locked FAIL (validated-R1 ≈ 18/96);
  if it does not, the harness is suspect and the scout is void pending diagnosis.
```

## 6. Ceiling — what this one-off does and does not establish

```text
DESCRIPTIVE ONLY. It shows how validated-R1 and the off-map positional rate move with K on
  THIS construction. It does NOT certify a constructible baseline at any K — validated-R1 here
  conflates composition with arbitrary-label-tracking. A BAND-HINT is a CANDIDATE K worth a
  clean certification test on a chain-identity-robust construction LATER; it is NOT itself a
  certified baseline, and must not be cited as one.
OFF-MAP-VS-K IS POSITIONAL, not a mechanism curve; it does not resolve the closed K=5 FAIL's
  mechanism question (relation-keyed grab vs chain-anchor inconsistency — not separable here).
NOT A CAPABILITY CLAIM. Results are per-construction, per-load, at n=96/cell. "The model
  can/can't compose" is out of bounds.
THE CLOSED K=5 FAIL IS UNTOUCHED. The K=5 cell reproduces it as an internal-validity check;
  the locked FAIL artifact is not modified, reopened, or superseded.
DEFERRED (explicitly out of scope of this one-off, triggered only by a BAND-HINT): a
  certification run on a chain-identity-robust construction. Execute the narrow scout now;
  the broad certification waits on a result that justifies the build.
```

## 7. Routing & authorization

```text
Senior drafts (this document) → TL approves the scout (direction + locked spec) → MANAGER
AUTHORIZES THE RUN BY NAME → CS patches constants/inspector for K-variation (§2) and executes
→ SE byte-verifies every emitted artifact (fetch + sha256 echoed adjacent) and recomputes the
headline validated-R1 and Wilson CI per cell independently → descriptive curves + dispositions
reported to TL / New Senior.

Lock-before-look binds the run: §3 metrics and §4 patterns/null/stop-rule are fixed before any
cell is computed. This pre-registration certifies nothing and authorizes nothing on its own;
the Manager authorizes the run by name.
```

---

**The one to carry up:** This is a **one-off descriptive load scout** — a single run sweeping **K = 1 through 5** on the **existing construction** to see how validated-R1 and the off-map positional rate move with clutter, answering "does the failure grow, cliff, plateau, or fall as K climbs, and is there a happy-medium hint." It is deliberately **not a certification and not a project**: on the head-token construction validated-R1 conflates composition with arbitrary-label-tracking, so **no K here certifies a baseline** — a band-hint is a *candidate K to certify later on a chain-identity-robust construction*, which is how the construction-validity constraint (CS/C4/C5) is honored, by scoping the claim rather than gating on a build. It keeps the metric discipline (validated-R1 primary, never a raw rate — Paper 1), reports the off-map curve as **positional** (not mechanism — CS#4/C4/C5-F3), folds C1's two-dial decomposition **relabeled positional and base-rate-baselined** (answer-depth landing rate, not "walk rate"), carries the **cross-query chain-membership pattern** as the per-cell empirical check that the model actually held chain identity at load, and requires that a band-hint show **control margins stable-or-stronger at the band K** (C5-F1, the validated-metric version of the mirage §3 blocks for raw rates). Lock-before-look binds with a **one-computation-per-cell** stop-rule and an explicit boundary-case branch (F2). The **K=5 cell reproduces the locked FAIL** as an internal check; the closed FAIL is untouched. Routing: Senior-draft → TL approves → **Manager authorizes the run by name** → CS patches K-variation + executes → SE byte-verifies. Certifies nothing; authorizes nothing on its own; the FAIL stays closed.

— Senior Engineer (drafting; routes Senior → TL approves → Manager-authorizes-by-name → CS executes → SE byte-verifies)
