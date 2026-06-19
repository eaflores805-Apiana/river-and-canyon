# PAPER-2-V3-INTEGRATION-PLAN-v0.1

**To:** Team Lead (for Manager/TL review) **Cc:** CS Engineer, C5, Manager **From:** Senior Engineer
**E. A. Flores**, Apiana AI, Inc. — June 19, 2026
*River and Canyon · Path A. An integration plan for Paper 2 — where the V3/hop1 finding enters, what language is allowed, what to revise, what stays forbidden. This does NOT rewrite the paper. SE drafts; SE locks nothing and authorizes nothing.*

> Grounded in a byte-read of `correctnessisnotconstructibility.pdf` (P2, v1.0, 14 pp): §3.1 construction / §3.2 instrument; §4.1–§4.5 results (Figures 1–4); §5/§7 discussion + limitations; §8 related work; §9 future work; §10 conclusion; Appendix A claim-ledger linkage; Appendix B artifacts/provenance. Where I name P2's current content, I read it.

## 0. What P2 currently is (so the plan attaches correctly)

P2 supplies **one** worked demonstration that the FP16 baseline gate is *binding, not merely conservative*: a **Two-Hop Level-1 closed-world construction** (Cells 01–03, 3B FP16) carrying **two independent defects** — **Defect 1**, a component hop (hop1) **below the constructibility floor** (Cell03 6/24), which "precludes any isolated linkage claim from this lineage"; and **Defect 2**, surface composite correctness **position/rank-contaminated** (Cell03 1/8 → 6/8 → 8/8 by endpoint position; all seven wrong_chain returns = the last-position decoy `cd2@pos7`). Single-hop hop2 is near-ceiling (24/24, 23/24, 23/24) as an **internal FP16 gate-discrimination control — explicitly not a certified stress target.** Figures 1–4 carry these. P2 **already owns "Claim B"** (constructibility floor mappable, not cleared), **already updates program Claim #5 to "blocked on a precondition,"** and **makes no statement on Claim C (the seam, blocked)** — see Claim Ledger v0.2. P2 §9 future-work **already calls for** "different task geometry … decouple position from rank … decouple decoy placement from target placement."

**The V3 case is the construction P2 §9 asked for, and a second, independent demonstration of Claim B.** The foreclose-all V3 redesign closes the position/rank route that produced Defect 2 — and the result is that, with that route foreclosed, the **hop1 precondition still fails, now stably across six fresh materializations**, while hop2 holds. That isolates the hop1-constructibility shortfall *away from* the position confound and adds a **cross-materialization** dimension P2's single-draw case does not have.

---

## 1. WHERE the V3/hop1 finding enters Paper 2

```text
§3.3  (NEW) "Second construction: foreclose-all V3"  — parallels §3.1.
      Describe V3: head fans out via D=5 DISTINCT relations to same-depth (depth-2) competitor nodes so only
      relation-following selects the target C*, plus K=5 relation-reusing P-distractor decoy chains; locked
      values (K=5, P=5, M>=10, margin=0.25, derived floor F=0.20, admissibility floor 0.75 Wilson-lower).
      State plainly: V3 was built to FORECLOSE the position/rank route that produced Defect 2 in §3.1's
      construction (the decouple-position-from-rank geometry §9 called for). State the boundary: V3 CONFORMS to
      the foreclose-all standard; it is a committed design CHOICE, not a certified-complete construction.

§4.6  (NEW) "Cross-materialization result under foreclose-all controls: hop2 admissible across six fresh
      materializations; hop1 stable-inadmissible"  — the home of the finding. Contains Table V3-1 (per-block),
      the anchor/eight-materialization framing, the composite-gate PRECONDITION-FAIL, and the P-role
      co-occurrence with its leash. Mirror §4.1's caption discipline on any figure.

§5 / §7  (REVISE) One paragraph tying Case 1 + Case 2: Case 1 shows surface composite != constructibility via
      position contamination AND a below-floor component; Case 2 shows that FORECLOSING the position route does
      not rescue constructibility — the hop1 precondition fails, and does so STABLY across fresh draws. "Two
      independent constructions within the same model and closed-world two-hop task family; two distinct routes
      to a constructibility failure." Extend §7's existing hedges (do not weaken them — see §5 below).

Abstract  (REVISE) From "supplies the demonstration … one small, closed-world 3B construction" to two
      independent constructions; add the V3 result in bounded form (allowed sentences in §2 below).

Appendix A  (REVISE) Claim-ledger linkage: the V3 case is a SECOND demonstration of Claim B; Claim #5 stays
      "blocked on a precondition"; no statement on Claim C. Bump the cited ledger version to the one carrying
      the V3 negative finding row (the program's first data-trigger ledger update).

Appendix B  (ADD) V3 run artifacts/provenance in P2's existing full-sha256, attested + CS-recomputed-for-
      freeze/tag form (§4 below).
```

## 2. EXACT claim language allowed (bounded; quotable as-is)

```text
PRIMARY (the sanctioned route statement — use verbatim):
  "Across the six fresh V3 materializations tested here, hop1 did not clear its admissibility floor in any
   block, while hop2 remained admissible in every block."

SUPPORTING (all bounded; behavior-of-the-construction, not capability):
  "In a second, independent construction (foreclose-all V3) at 3B FP16, hop2 was admissible across all six
   fresh materializations (576/576), while hop1 did not clear its 0.75 admissibility floor in any of the six."
  "Because the foreclose-all construction was built to remove the position/rank route exposed in the first
   construction, the persistence of the hop1 shortfall under it shows the shortfall is not reducible to that
   route."
  "Across all eight materializations tested to date, hop1 cleared its admissibility floor in exactly one; that
   single clearing is anomalous relative to the fresh map."
  "The composite gate was not readable because the hop1 precondition was not met; the composite question is
   unanswered, neither supported nor refuted."

P-ROLE (positional/structural ONLY — see §7 of P2's own discipline; use verbatim):
  "Among wrong hop1 predictions in the fresh blocks, outputs landed on the P-role distractor class in all
   logged cases."

STANDING DISCLAIMERS to carry into §4.6 (re-use P2's own wording where it exists):
  - hop2 admissibility here is an internal FP16 gate-discrimination control, NOT a certified stress target;
    any future stress run on hop2 requires a hop2-specific shortcut/position probe.
  - No compression rungs were run on this construction; no retention-under-stress claim is made; pre-stress.
  - V3 conforms to the foreclose-all standard but is not certified; the composite gate was not read, so no
    "gate cleared" claim arises for it.
```

## 3. FIGURES / TABLES needed

```text
Table V3-1 (MANDATORY) — Per-block hop1 / hop2 under foreclose-all V3 (six fresh materializations):
  block | hop1 | rate | hop1 Wilson lower | hop2
   F1   50/96  0.5208      0.4220          96/96
   F2   23/96  0.2396      0.1653          96/96
   F3   35/96  0.3646      0.2752          96/96
   F4   39/96  0.4062      0.3135          96/96
   F5   54/96  0.5625      0.4628          96/96
   F6   23/96  0.2396      0.1653          96/96
   total hop1 224/576 ; hop2 576/576 ; all six hop1 blocks fail the 0.75 floor.
  Caption discipline (mirror P2 Figure 1): blocks are DISTINCT fresh materializations, not an ordered stress
  variable; no fitted trend.

Figure V3-1 (OPTIONAL) — Per-block hop1 rate with the 0.75 floor line, plus the two anchors (floor-check
  001..096 = 0.906 [cleared], composite-gate 097..192 = 0.292 [failed]) marked as anomalous/with-context.
  Same caption discipline; anchors labeled descriptive, not part of the branch.

Table V3-2 (OPTIONAL) — Eight-materialization summary: 001..096 (0.906, clear) | 097..192 (0.292, fail) |
  F1..F6 (fail) — to make "cleared in exactly one" inspectable.

P-role landing (one-line table or inline): wrong hop1 predictions by landing class — P_decoy_head 352, other 0
  (= 352/352). Tagged "positional/structural co-occurrence; no mechanism."
```

Keep it tight: P2 already has four figures. Table V3-1 is required; Figure V3-1 and Table V3-2 are optional supplements; the P-role line should not become its own figure.

## 4. EVIDENCE / digests cited (Appendix B additions)

Add in P2's existing Appendix B form (full sha256, attested from locked files, **independently recomputed by CS for the freeze/tag pass**):

```text
REPO-VERIFIED (load-bearing; recompute for freeze/tag):
  Repository: github.com/eaflores805-Apiana/river-and-canyon
  Hop1-stability run:   experiments/2026-06-19_hop1-stability-run   HEAD fe677158
     decision.json      (HOP1-STABLE-INADMISSIBLE; reproduced byte-identical)
     covariate_log.json (P-role 352/352 P_decoy_head)
     admissibility_summary.json 576/576 PASS ; prompt_conformance_summary.json 576/576 PASS ; manifest present
  Composite-gate run:   experiments/2026-06-18_v3-composite-gate-run  HEAD 09030b18
     decision 3924ff35  (PRECONDITION-FAIL; hop1 28/96, hop2 96/96)
  Floor-check:          decision 6a34f6dc  (COMPONENT-ADMISSIBLE-UNDER-COMPETITION; hop2 96/96, hop1 87/96)
  Model/profile:        Qwen/Qwen2.5-3B-Instruct rev aa8e7253, FP16, greedy
  (List full sha256 for each cited file, as P2 Appendix B does for the Cell artifacts.)

INTERNAL BANKED ARTIFACTS (SE-draft bytes; canonical filing is the CS commit of the same bytes):
  HOP1-STABILITY-FINDING-REPORT-v0.1.md            2969ec1a5ce830c2b77c974ad23b163e4cb1dca6a518800a555f5a159f6efb33
  HOP1-STABILITY-RUN-SE-VERIFICATION-RETURN-v0.1   84a5716b4f202a9337495100064d8e5f466ff8baf3e76bb16b4d221de05285b9
  V3-COMPOSITE-GATE-RUN-SE-VERIFICATION-RETURN     0eb0edcb…
  V3-FLOOR-CHECK-RUN-SE-VERIFICATION-RETURN        03d2ead8…

EXPLICIT THRESHOLD STATEMENT for §4.6: state the admissibility floor (0.75 Wilson lower bound) and the locked
  values (K=5, P=5, M>=10, margin=0.25, derived F=0.20) so the V3 "floor" is defined and not conflated with the
  §4.1 per-cell /24 floor language. Note (consistent with §7) thresholds are local to construction/model/
  vocabulary/scoring/geometry.
```

## 5. EXISTING Paper 2 language to revise

```text
Abstract:
  - "This paper supplies the demonstration" -> "...in two independent constructions."
  - "diagnostic case evidence from one small, closed-world 3B construction" -> "...from two constructions
    within one model and closed-world two-hop family," with the second adding foreclose-all controls and
    cross-materialization evidence. KEEP "we do not claim this holds across all tasks or models."

§7 Limitations — "Single model, single construction family":
  - REVISE to: results now span TWO constructions within the same model (3B FP16) and the same closed-world
    two-hop family; the V3 construction adds CROSS-MATERIALIZATION evidence (six fresh disjoint draws). STILL no
    generalization to other scales, architectures, or task families; still no compression rung. (Strengthen the
    cross-materialization point WITHOUT widening the model/task claim.)
  - Keep "Behavioral only / no mechanistic claim" and "Thresholds are local" verbatim; the V3 section inherits
    both.

§9 Future work:
  - NOTE that V3 IS the "decouple position from rank / different task geometry" construction §9 called for, and
    that its result REFRAMES the linkage-constructibility question: even with the position route foreclosed, the
    hop1 precondition was stable-inadmissible across fresh materializations, so a constructible linkage baseline
    is not yet in hand. The "take a constructible task to stress" direction is unchanged and still gated; this
    is NOT a green light to stress hop2 or anything else.

§10 Conclusion:
  - OPTIONAL: add that the gate's binding/discriminating character is now shown across two independent
    constructions, the second isolating the component-precondition failure from the position confound.

Appendix A — claim-ledger linkage:
  - The V3 case is a SECOND demonstration supporting Claim B (constructibility floor mappable, not cleared);
    Claim #5 REMAINS "blocked on a precondition" (not resolved); NO statement on Claim C. Bump the cited ledger
    version to the one carrying the V3 negative finding row.

DO NOT:
  - change the title; - weaken any "behavioral only / no mechanism / single model / thresholds local" hedge
    (extend, never relax); - recast hop2's role from "internal FP16 gate-discrimination control" to anything
    stronger.
```

## 6. Claims still forbidden (carry the full list)

```text
None of the following may appear in the V3 material or anywhere it touches:
  the model cannot do hop1 | the model cannot compose | the model is unstable | binding failure |
  attention failure | reasoning failure | shortcut mechanism | compression readiness | Claim C |
  Paper B | certification | seam evidence.
Construct-specific additions:
  - NO statement on Claim C (the seam) — it remains blocked; the V3 case does not touch it.
  - NO resolution or advance of Claim #5 — it stays "blocked on a precondition"; pre-stress.
  - The P-role landing is positional/structural co-occurrence ONLY — never binding/attention/identity/shortcut
    mechanism; for it to become more it would need (in a FUTURE study) a behavioral signature, a minimal
    intervention, and a falsification path.
  - NO cross-MODEL / cross-SCALE / cross-TASK-FAMILY generality. V3 adds cross-MATERIALIZATION evidence within
    ONE model and ONE task family — nothing wider.
  - The foreclose-all design is a committed CHOICE that CONFORMS; it is NOT certified-complete. Do not imply the
    construction is proven to foreclose every route.
  - Per-block connecting lines (if any figure draws them) are visual guides across distinct materializations —
    NOT a fitted trend or ordered stress variable.
NAMING DISCIPLINE (do not conflate):
  - "Claim B" = P2's OWN claim (constructibility floor mappable, not cleared) — ALLOWED, and strengthened here.
  - "Paper B" = FORBIDDEN. These are different tokens; keep them distinct.
```

## Manager / TL boundary

```text
- This is an INTEGRATION PLAN, not the paper section. The actual §3.3/§4.6 prose, the figures, the Appendix B
  full-sha256 list, and the claim-ledger row are SEPARATE drafting tasks, each due the same claim-risk review.
- The Appendix B V3 digests must be independently recomputed by CS for the freeze/tag pass (P2's standing
  convention), exactly as the existing 13/13 Cell hashes were.
- This plan recommends NO immediate experiment. Whether to (A) package and pause Path A or (B) later attempt
  one bounded hop1-safe construction-design question remains a Manager decision, best taken after the packaged
  Paper 2 material exists.
```

## Required return

```text
PASS — Paper 2 V3 integration plan drafted for Manager/TL review.
```

## Boundaries

```text
No new experiment. No construction redesign. No prompt edits. No post-hoc slicing. No threshold adjustment.
No tooling edit. No compression. No INT8. No INT4. No Claim C. No Paper B. No certification claim. No
capability claim. No mechanism claim. The program remains PRE-STRESS; the carving analogy stays a target-
generator, never a mechanism. The Path A FP16 K=5 FAIL remains closed. SE drafts this plan; SE locks nothing
and authorizes nothing.
```

---

**The one to carry up:** The V3/hop1 finding enters **Paper 2** as a **second, independent construction** (new §3.3 + §4.6), and it is the construction P2's own §9 future-work called for — *decouple position from rank*. Its force is precise: the foreclose-all redesign that removed the position/rank route (Defect 2) **still shows the hop1 precondition failing, now stably across six fresh materializations** while hop2 holds (576/576) — so the hop1-constructibility shortfall is **not reducible to the position confound**, and the gate is shown binding/discriminating across **two** independent constructions. It is a **second demonstration of P2's existing Claim B**; Claim #5 **stays blocked-on-precondition**; Claim C is **untouched**; the program stays **pre-stress**. The P-role landing rides in as positional co-occurrence on the tightest leash. Revisions extend P2's hedges (cross-materialization within one model/task family — no wider) and never relax them. This plan does not write the section and recommends no experiment; A (pause) vs B (one bounded design attempt, later) remains the Manager's call.

— Senior Engineer (Paper 2 V3 integration plan; routes for Manager/TL review)
