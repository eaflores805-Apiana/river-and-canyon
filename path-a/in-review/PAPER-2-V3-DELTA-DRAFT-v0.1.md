# PAPER-2-V3-DELTA-DRAFT-v0.1

**To:** Team Lead → C5 (claim-risk) → CS (provenance) → Manager **From:** Senior Engineer
**E. A. Flores**, Apiana AI, Inc. — June 19, 2026
*River and Canyon · Path A. A **delta draft** for Paper 2 (*Correctness Is Not Constructibility*): the new/changed text blocks that integrate the V3/hop1 constructibility finding as a second, independent construction. This is draft prose for review, **not** a final paper revision. Bounded language throughout. SE drafts; SE locks nothing and authorizes nothing.*

> Review route after this return: (1) C5 claim-risk; (2) CS provenance/digest feasibility; (3) TL synthesis; (4) Manager. Digests below are **placeholders pending CS independent recompute for the freeze/tag pass** (P2 Appendix B convention). Where a value is repo-verified this session, its short prefix is given and marked.

---

## 1. Revised abstract language

> *Replace the existing abstract body. Changes: "the demonstration" → "in two independent constructions"; add the V3 case; keep all pre-stress / no-generalization hedges.*

Behavioral stress metrology — measuring which capabilities a model retains under compression such as INT4 quantization — presumes a trustworthy full-precision baseline. Paper 1 argues that stress-retention is uninterpretable unless the FP16 baseline is clean, and specifies fail-closed gates that withhold a result otherwise. That argument leaves one thing unshown: that the baseline gate is ever binding rather than merely conservative. This paper supplies the demonstration in **two independent constructions within one model and one closed-world two-hop task family** (3B FP16).

In the first construction (Two-Hop Level-1, closed world), surface composite accuracy (15/24) appears to indicate partial competence. A per-group decomposition shows otherwise: composite correctness rises monotonically with the (co-varying) absolute-position / rank axis of the target endpoint — 1/8 at pos3, 6/8 at pos5, 8/8 at pos7, while a pure last-position shortcut predicts 0/0/8 — so surface correctness cannot be read as evidence of the intended two-hop operation. We are careful about the converse: we do not claim the model failed to perform it; we show the metric cannot distinguish the intended operation from shortcut-aligned correctness. We further find a component sub-task (hop1) below the constructibility floor, so linkage cannot be isolated at all in this construction; the baseline carries two independent defects, not one.

In a second, independent construction (a foreclose-all redesign, "V3") built specifically to remove the position/rank route exposed in the first, single-hop retrieval of the second relation (hop2) was admissible across **all six fresh materializations** tested (576/576), while the first hop (hop1) **did not clear its admissibility floor in any of the six**. Because the redesign was built to foreclose the position/rank route, the persistence of the hop1 shortfall under it indicates the shortfall is not reducible to that route; and because the six materializations were fresh and disjoint, the shortfall is stable across draws rather than a single-draw artifact. The composite gate was therefore not readable, and the composite question is unanswered, neither supported nor refuted. Among wrong hop1 predictions, outputs landed on a single in-context distractor class in all logged cases — a positional/structural co-occurrence, reported as such.

As an internal FP16 gate-discrimination control in both constructions, single-hop retrieval clears the gate while the multi-hop / first-hop precondition does not, so the gate discriminates rather than rejecting everything. The hop2 result is an internal FP16 gate-discrimination control, not a certified stress target; any future stress run on hop2 requires a hop2-specific shortcut/position probe. No compression rungs were run on either construction; we make no retention-under-stress claim. The contribution is a worked constructibility map across two constructions, illustrating why the gate must exist and withhold a superficially usable FP16 baseline. We do not claim this holds across all tasks, scales, or models; the second construction adds cross-materialization evidence within one model and task family, not generality beyond it.

---

## 2. New §3.3 text — *Second construction: foreclose-all V3*

> *Insert after §3.2 (Instrument). New subsection.*

**3.3 Second construction: foreclose-all V3.** The first construction (§3.1) left two routes by which surface correctness could be earned without the intended operation: a position/rank route (the §4.3 contamination) and a below-floor component (hop1) that precluded isolating linkage at all. §9 of an earlier draft identified the needed remedy as *different task geometry* that decouples position from rank and decouples decoy placement from target placement. The second construction, "V3," is that geometry, built as a foreclose-all redesign.

In V3 each item presents a head entity that fans out, via *D = 5 distinct relations*, to five depth-2 competitor endpoints that all sit at the same structural depth; only following the queried relation through both hops selects the correct target C\*. Same-depth competitors remove a structural-depth selection cue, and distinct relations remove a single-relation recency cue; together with balanced placement they are intended to foreclose the position/rank/endpoint route that §4.3 exposed. Each item additionally carries *K = 5* relation-reusing distractor chains of the form (P\_i, r1, Q\_i), (Q\_i, r2, S\_i), whose r1-subject role token (the "P-role") is a designed wrong-selection target. The locked construction parameters are K = 5, P = 5, M ≥ 10 fan-in, selection margin 0.25, and a derived structural floor F = 0.20.

The admissibility criterion is fail-closed and stated as a strict floor: a query type is admissible on a materialization only if the Wilson lower bound of its accuracy exceeds **0.75**. V3 shares the *fail-closed gate layout* of §3.1–§3.2 but, consistent with §7, uses thresholds local to this construction, model scale, vocabulary, scoring contract, and task geometry. The composite query is gated behind hop1 admissibility: the two-hop result is read only if the first hop is itself admissible on that materialization.

To test stability rather than a single draw, V3 was materialized as six fresh, disjoint item sets (lock-before-look: metrics, floor, and stop-rule were fixed before scoring, and any already-seen materialization was barred from gate use). We emphasize the boundary on the construction itself: V3 *conforms* to the foreclose-all standard but is a committed design choice, not a construction proven to foreclose every conceivable route. All runs are 3B FP16, greedy decoding, on the single locked model revision recorded in Appendix B.

---

## 3. New §4.6 text — *Cross-materialization result under foreclose-all controls*

> *Insert after §4.5. New subsection. Table V3-1 (§4 of this delta) is referenced here.*

**4.6 Cross-materialization result under foreclose-all controls: hop2 admissible across six fresh materializations; hop1 stable-inadmissible.** Across the six fresh V3 materializations (Table V3-1), single-hop retrieval of the second relation held at ceiling on every materialization (576/576), clearing the 0.75 floor in all six. The first hop did not: its per-block accuracy ranged from 0.24 to 0.56, and its Wilson lower bound fell below 0.75 in every block, including the highest (F5, 0.5625, lower bound 0.4628). Stated in the program's bounded form:

> *Across the six fresh V3 materializations tested here, hop1 did not clear its admissibility floor in any block, while hop2 remained admissible in every block.*

Two earlier V3 materializations bound this result as descriptive anchors. An initial floor-check materialization (seeds 001–096) had cleared hop1 at 0.906; a fresh, disjoint composite-gate materialization (seeds 097–192) then returned hop1 at 0.292, failing the precondition, so the composite gate on that materialization was withheld (a fail-closed PRECONDITION-FAIL in the sense of §4.2). The six stability materializations were drawn fresh and disjoint from both. Across all eight V3 materializations tested to date, hop1 cleared its admissibility floor in exactly one — the initial floor-check — which is anomalous relative to the fresh map; we do not treat the lone clearing as the stable case. The methodological point is the one Paper 1 stages for: a precondition that cleared on a single (subsequently already-seen) materialization did not replicate on fresh disjoint draws, and requiring fresh runs — barring already-seen data from gate use — is what surfaced this.

Because the composite query is gated behind hop1 admissibility, and hop1 admissibility did not reliably hold, the composite gate was not readable on the fresh materializations. The composite question is therefore unanswered under this construction — neither supported nor refuted. This is a precondition-level outcome, not a composite result.

The hop1 shortfall here is not reducible to the §4.3 position/rank route: V3 was built to foreclose that route, and the shortfall persists under it across fresh draws. Among the wrong hop1 predictions in the fresh blocks, outputs landed on the P-role distractor class (the r1-subject role token of the relation-reusing distractor chains) in all logged cases (352/352). We report this strictly as a **positional/structural co-occurrence**: it identifies *where* wrong first-hop outputs landed in the item structure, not *why*. It is not a binding, attention, identity-resolution, or shortcut-mechanism claim; per the program's discipline, for this co-occurrence to become more than a landing fact it would require, in a future pre-registered study, a behavioral signature, a minimal intervention predicted to change the landing, and a falsification path.

As in §4.1, hop2's admissibility is an internal FP16 gate-discrimination control, not a certified stress target; that it now holds across six fresh materializations strengthens the control but does not promote it, and any future stress run on hop2 still requires a hop2-specific shortcut/position probe. No compression rungs were run on this construction; we make no retention-under-stress claim. The result is that, across two independent constructions, the baseline gate is shown binding and discriminating — and that the second construction isolates the component-precondition failure from the position confound the first construction could not separate.

---

## 4. Table V3-1

> *Place in §4.6. Caption discipline mirrors Figure 1: distinct materializations, not an ordered stress variable.*

**Table V3-1. Foreclose-all V3, six fresh materializations (FP16, greedy).** Per-block first-hop (hop1) and second-hop (hop2) accuracy; hop1 Wilson lower bound against the 0.75 admissibility floor.

```text
 materialization   hop1        hop1 rate   hop1 Wilson lower (vs 0.75)   hop2
 F1 (193–288)      50/96        0.5208            0.4220   (fail)        96/96
 F2 (289–384)      23/96        0.2396            0.1653   (fail)        96/96
 F3 (385–480)      35/96        0.3646            0.2752   (fail)        96/96
 F4 (481–576)      39/96        0.4062            0.3135   (fail)        96/96
 F5 (577–672)      54/96        0.5625            0.4628   (fail)        96/96
 F6 (673–768)      23/96        0.2396            0.1653   (fail)        96/96
 total             224/576      —                 —                      576/576
```

*Caption.* Single-hop hop2 holds at ceiling on every materialization (576/576), clearing the 0.75 floor; hop1 fails the floor in all six. Materializations are distinct fresh, disjoint item sets, not an ordered stress variable; no fitted trend is implied. Counts, Wilson bounds, and the final branch (HOP1-STABLE-INADMISSIBLE) are attested from the locked run record and recomputed by CS for the freeze/tag pass (Appendix B).

---

## 5. Optional Figure V3-1 — recommendation

> *Recommendation, not required.*

A single panel plotting per-materialization hop1 rate (F1–F6) against the 0.75 floor line, with the two anchors (floor-check 001–096 = 0.906, cleared; composite-gate 097–192 = 0.292, failed) shown as separately marked points, would make "cleared in exactly one of eight" inspectable at a glance. **Recommendation: include only if space allows; Table V3-1 is sufficient on its own.** If included, the caption must carry the same discipline as Figure 1 — points are distinct materializations, not an ordered stress variable; the anchors are descriptive and not part of the stability branch — and the panel must not draw a trend line through the materializations.

---

## 6. §5 / §7 revision text (discussion and limitations)

> *§5/§7 additions and one revised limitation.*

**Add to the discussion (§5):** The two constructions fail the baseline in two distinct ways. The first earns a respectable surface composite score that dissolves into a position/rank-contaminated gradient, and separately carries a below-floor component; the second, built to foreclose that position/rank route, instead exposes a first-hop precondition that does not clear its floor and does not do so stably across fresh materializations. The gate is therefore shown binding and discriminating across two independent constructions, with the second isolating the component-precondition failure from the position confound the first could not separate. Neither construction yields a composite result: the first because its components are not constructible, the second because the first-hop precondition gating the composite is not met.

**Revise the "Single model, single construction family" limitation (§7) to read:** *Two constructions, one model and task family.* All results are 3B FP16 on a single closed-world two-hop task family; the second construction (V3) adds cross-materialization evidence across six fresh, disjoint draws. No generalization to other scales, architectures, or task families is claimed, and no compression rung was run on either construction. The single-hop controls (hop2) are query types within each construction, not separate tasks.

**Keep verbatim (the V3 material inherits these):** the *Behavioral only — no mechanistic claim* limitation; the *Thresholds are local; the gate layout is not the thresholds* limitation. **Add to the behavioral-only limitation:** the P-role landing of §4.6 is a positional/structural co-occurrence and is governed by the same rule — it generates a future target, not a mechanism. **Add to the abstention note:** the over-abstention on hop1 observed in §4.6's wrong predictions is consistent with the NULL-calibration instability already flagged; it remains future work, not explained here.

---

## 7. §9 future-work revision text

> *Revise/extend §9.*

The earlier §9 called for *different task geometry* that decouples position from rank — the construction realized here as V3 (§3.3). Its result reframes the linkage-constructibility question rather than closing it: with the position/rank route foreclosed, the first-hop precondition was stable-inadmissible across six fresh materializations, so a constructible linkage baseline is not yet in hand under this construction. The most direct next measurement remains unchanged and remains gated: take a *demonstrably constructible* single-lookup task through actual compression as instrument-validation-under-stress — not composition or seam evidence — and only after that task is itself certified shortcut-free (a task-specific shortcut/position probe), since by this paper's own argument accuracy does not establish constructibility. The V3 result is not a green light to stress hop2 or any other component; whether a linkage task can be made constructible enough to carry a composite measurement at all is the open program question, and it remains gated. No stress rung has yet been run on either construction.

---

## 8. Appendix A — claim-ledger update language

> *Replace the Appendix A linkage paragraph.*

This paper reports **Claim B** (constructibility floor mappable, not cleared) and now supports it with **two independent constructions**: the position-contaminated, below-floor first construction, and the foreclose-all V3 construction in which the first-hop precondition is stable-inadmissible across six fresh materializations while the second hop holds. It continues to update program **Claim #5** (precision-demanding tasks retain less under quantization) to **blocked on a precondition** — the V3 result reinforces this block and does not resolve it. It makes **no statement on Claim C** (the seam), which remains blocked. The V3 finding is recorded as the program's first data-trigger ledger update (a protocol run); see Claim Ledger [version to be set to the release carrying the V3 negative-finding row — CS/TL to confirm the identifier].

---

## 9. Appendix B — provenance / digest placeholders

> *Add to Appendix B in its existing form: full sha256, attested from the locked files, **independently recomputed by CS for the freeze/tag pass.** Short prefixes marked "repo-verified this session" were recomputed by SE during verification; CS must still recompute full digests for the freeze/tag.*

```text
Repository: github.com/eaflores805-Apiana/river-and-canyon

V3 floor-check (anchor; seeds 001–096):
  decision  6a34f6dc…                         [full sha256: CS to recompute]   (COMPONENT-ADMISSIBLE-UNDER-COMPETITION)

V3 composite-gate run (anchor; fresh 097–192):
  run dir   experiments/2026-06-18_v3-composite-gate-run   HEAD 09030b18
  decision  3924ff35…                         [full sha256: CS to recompute]   (PRECONDITION-FAIL)

V3 hop1-stability run (six fresh 193–768):
  run dir   experiments/2026-06-19_hop1-stability-run      HEAD fe677158
  decision.json           [full sha256: CS to recompute]   (HOP1-STABLE-INADMISSIBLE; SE reproduced byte-identical)
  covariate_log.json      [full sha256: CS to recompute]   (P-role 352/352 P_decoy_head)
  admissibility_summary.json   [full sha256: CS to recompute]   (576/576 PASS)
  prompt_conformance_summary.json [full sha256: CS to recompute]   (576/576 PASS)
  manifest.json           [full sha256: CS to recompute]   (present; lists decision/covariate/run_record + scored)

Model / profile (locked):
  Qwen/Qwen2.5-3B-Instruct   revision aa8e72537993ba99e69dfaafa59ed015b17504d1   FP16   greedy (temp 0)

Internal banked governance artifacts (SE-draft bytes; canonical filing is the CS commit of the same bytes):
  HOP1-STABILITY-FINDING-REPORT-v0.1.md          2969ec1a5ce830c2b77c974ad23b163e4cb1dca6a518800a555f5a159f6efb33  (full; SE)
  HOP1-STABILITY-RUN-SE-VERIFICATION-RETURN-v0.1 84a5716b4f202a9337495100064d8e5f466ff8baf3e76bb16b4d221de05285b9  (full; SE)
  V3-COMPOSITE-GATE-RUN-SE-VERIFICATION-RETURN   0eb0edcb…   [full sha256: CS to recompute]
  V3-FLOOR-CHECK-RUN-SE-VERIFICATION-RETURN      03d2ead8…   [full sha256: CS to recompute]

Threshold statement (state explicitly in Appendix B): V3 admissibility floor = Wilson lower bound > 0.75;
locked construction values K=5, P=5, M>=10, selection margin 0.25, derived structural floor F=0.20.
Thresholds are local to this construction/model/vocabulary/scoring/geometry (§7).
```

**CS feasibility note for review:** all repo digests must be recomputed from the locked files for the freeze/tag pass exactly as the existing 13/13 Cell hashes were; the four bracketed repo entries above are placeholders for that recompute, not asserted final hashes.

---

## 10. Explicit forbidden-claims checklist

> *Run this against the drafted blocks before C5 review; every box must hold.*

```text
[ ] No "the model cannot do hop1."                  (V3 states a per-construction admissibility result.)
[ ] No "the model cannot compose."                  (Composite question is unanswered, not refuted.)
[ ] No "the model is unstable."                     (Result is about the V3 construct's precondition.)
[ ] No binding / attention / reasoning failure.     (No mechanism is named anywhere.)
[ ] No shortcut-mechanism claim.                    (P-role is positional/structural co-occurrence only.)
[ ] No compression-readiness claim.                 (Pre-stress; no rung run.)
[ ] No statement on Claim C (the seam).             (Remains blocked; untouched.)
[ ] Claim #5 stays "blocked on a precondition."     (Reinforced, not resolved.)
[ ] No certification claim.                          (Nothing is certified; composite gate not even read.)
[ ] No capability claim.                             (All statements are about the construction's behavior.)
[ ] No mechanism claim.                              (Behavioral-only limitation inherited.)
[ ] No cross-model / cross-scale / cross-task generality.   (Cross-materialization within one model/family only.)
[ ] Foreclose-all V3 = committed choice that conforms, NOT certified-complete.
[ ] Per-block table/figure = distinct materializations, NOT an ordered stress variable / fitted trend.
[ ] Naming: "Claim B" (P2's own, strengthened) is NOT "Paper B" (forbidden) — kept distinct.
[ ] hop2 = internal FP16 gate-discrimination control, NOT a certified stress target.
[ ] The sanctioned route statement is used verbatim where the headline is stated.
```

---

## Boundaries

```text
This is a delta DRAFT for review (C5 -> CS -> TL -> Manager), not a final paper revision and not a filing.
No new experiment. No construction redesign. No prompt edits. No post-hoc slicing. No threshold adjustment.
No tooling edit. No compression. No INT8. No INT4. No Claim C. No Paper B. No certification claim. No
capability claim. No mechanism claim. The program remains PRE-STRESS; the carving analogy stays a target-
generator, never a mechanism. The Path A FP16 K=5 FAIL remains closed. SE drafts; SE locks nothing and
authorizes nothing. Appendix B digests are placeholders pending CS recompute for the freeze/tag pass.
```

---

**The one to carry up:** This delta draft adds the V3/hop1 finding to Paper 2 as a **second, independent construction** — the foreclose-all redesign that P2's own §9 called for — written in P2's voice and bounded throughout: hop2 admissible across six fresh materializations (576/576), hop1 not clearing its 0.75 floor in any of the six, the composite gate therefore not readable and the composite question unanswered, the hop1 shortfall **not reducible to the position/rank route** the redesign foreclosed, and the P-role landing reported strictly as positional/structural co-occurrence. It **strengthens Claim B**, keeps **Claim #5 blocked-on-precondition**, leaves **Claim C untouched**, and keeps the program **pre-stress**. Revisions extend P2's hedges (two constructions, one model/family, cross-materialization only) and never relax them; hop2 stays an internal FP16 control. Appendix B digests are placeholders for the CS freeze/tag recompute. Next: C5 claim-risk → CS provenance → TL synthesis → Manager. SE drafts; SE authorizes nothing; no experiment is recommended.

— Senior Engineer (Paper 2 V3 delta draft; for the C5 → CS → TL → Manager review chain)
