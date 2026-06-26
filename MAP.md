# Program Path Map

**Last updated:** 2026-06-25 (rev 5 — CS additions: Hop1 Stability Investigation EXECUTED → HOP1-STABLE-INADMISSIBLE (2026-06-19); Paper 2 V3-delta → v1.1-rc → **v1.2 PUBLIC RELEASE** + PDF (2026-06-19 → 06-21); Manager direction **open first bounded compression rung** (2026-06-21, packet prep only). YOU ARE HERE moved to the compression-rung standby. See rev-5 change-note at foot. Rev 4 traced the V3 lifecycle 2026-06-15 → 2026-06-19.)
**Re-sync rule:** if this and the record disagree, the record wins. Re-sync when a stage closes or a new branch opens. The `git log` is the authoritative timestamp for each commit.

A living overview of where the program has been, where it is, and where it ventured off. Coarse-grained: main stages, not every commit. The trunk reads top → bottom in time; branches show where the work split (closed routes, parked tracks, new directions).

For full per-route status see [`governance/standing/PROGRAM-CONTROL-LEDGER-v0.3.md`](governance/standing/PROGRAM-CONTROL-LEDGER-v0.3.md); for the route of record see [`PROGRAM-MAP-v2.0`](governance/standing/PROGRAM-MAP-v2.0.md); for the standard see [`NORTH-STAR-v1.2`](governance/standing/NORTH-STAR-v1.2.md). This is the path-and-branches view; those are the authoritative trackers.

---

## The trunk (top → bottom = progression in time)

```text
PROGRAM TRUNK

[done · 2026-05-31 → 06-10]  Foundation  (empirical base + metrology tower)
│
│   Stage 0 / Tier 0 — the empirical foundation
│     Two-Hop Level-1 matched-pair instrument LOCKED
│       (lock packet self-dated 06-07; scorer amended 06-08; hashes locked)
│     Cells 01–03 evidence record committed 06-08 (49aa222, "synthesis pass 4")
│       Cell03 = the binding decomposition underneath Paper 2
│     tier0-run/   (now sealed — see "Sealed")
│
│   B1 v2 evaluation harness merged + locked (06-10, 65da66d)
│
│   Papers released — the metrology tower (method → first result → certification)
│     Paper 1 (method) · Paper 2 (first result; v1.0 06-09)
│     Paper 3 (certification protocol; v1.0 + v1.1 06-10, after external review)
│   Standing governance set (NORTH-STAR, PROGRAM-MAP, templates)
│
├── ↳ Standing-notes branch (parallel to the numbered tower)
│      └── Hash Integrity v0.7.2 — third discipline; NOT Paper 4
│             papers/standing-notes/
│
[done · 2026-06-10/11]  Lane 1a / 1a' validation
│   Sealed instrument; rung-uniform schedule caught
│   └── Path A (rung-uniform) closed:
│         "breadth untested under the sealed schedule"
│
[done · 2026-06-12]   Hash Integrity lifecycle accepted (governance discipline integrated)
│
[done · 2026-06-12/13]  Baseline Gate Diagnosis (D4 family)
│   Stage E PASS:
│     primary FIXABLE
│     secondary VALID REJECTION
│     one narrow STRUCTURAL-LIMIT risk left open
│
├── ✗ BLOCKED branch: D4 certification route
│      │   Closed by Manager PIVOT (2026-06-13)
│      │   No candidate cleared full CERTIFICATION off-ceiling. The constructed-
│      │   positive PASSED validation off-ceiling (clean 40/40 spared, defective
│      │   eliminated) — proving an off-ceiling construct is BUILDABLE — but its
│      │   clean member sat AT ceiling, so a below-ceiling certified operating
│      │   point was never demonstrated. That gap is the open structural-limit edge.
│      ├── archive/d4-closed-route/
│      ├── CAL-Q rescue attempt → converted to FINDING TRACK (not rescued)
│      │       finding-tracks/cal-q-format-sensitive-abstention/
│      └── INT8-RUNG-1 → QUARANTINED (non-driving)
│
[done · 2026-06-14]  Repo reorganization — whole-repo move executed + closeout accepted
│   13-phase plan (A–M); all hash checks PASS; sealed bytes UNCHANGED
│   Created the current layout this map describes
│   move records: tier-1-instrument/organization/move/  ·  closeout v1.0 accepted
│
[done · 2026-06-14]  Baseline Gate Repair Design v0.1
│   Model-free endpoint for the open structural-limit edge
│   Carries it to the GREEN boundary; does not cross
│   governance/epochs/2026-06-11_lane-1a-prime/BASELINE-GATE-REPAIR-DESIGN-v0.1.md
│
[done · 2026-06-14]  POST-PIVOT hybrid direction adopted: "instrument first, seam deferred"
│   Standard refined: NORTH-STAR v1.1 → v1.2 — method-as-basis reframe
│     (quantization = a basis of distinct probes, not a scalar bit-depth dial;
│      a failure becomes a coordinate, not a verdict)
│
├── ↳ Paper A — RELEASED (instrument paper)
│      │   Lettered A/B dyad — NOT a 4th metrology paper
│      │   Positioning section taken through external peer review (v0.7)
│      │   papers/paper-a-before-retention/
│      └── Paper B (stress paper) reserved as DEFERRED placeholder
│              paper-b/planning/   (empty by design — load-bearing slot for the dyad)
│
└── ↳ Tier 1 instrument architecture  (the active branch)
       │   tier-1-instrument/
       ├── Eval-Validity Gate Tool Spec v0.1   (CS PASS)
       └── G6 Standing Rejection-Audit Spec v0.1  (CS PASS)
              │   tier-1-instrument/modules/g6-standing-rejection-audit/
              ├── G6 Entry Framing v0.1 filed              (CS PASS)
              ├── G6 Retrospective Audit Framing v0.1     (CS PASS)
              ├── G6 Retrospective Audit RESULT v0.1      (CS PASS; design-target cases only; consistency, not validation)
              ├── G6 Internal Consistency Closeout v0.1   (Manager Option A; first exercise CLOSED)
              ├── G6 Option B Readiness Note v0.1         (definition + criteria; Option B not opened)
              ├── G6 Non-Design-Target Candidate Inventory v0.1   (Option C; record exhausted)
              ├── G6 HOLD Review Superseded Validation Runs v0.1+v0.2 (HOLD bucket → EXCLUDE)
              ├── G6 Option B Case 1 Missing-Channel Design v0.1  (Manager opened Option B design-only)
              ├── case-1-missing-channel/ — constructed Case 1 bundle (CS-built; channel-absent record)
              │     └── G6 Case 1 Manual Audit Result v0.1  (by-hand application of G6 rules)
              └── evaluator/                              (FIRST G6 SOFTWARE — minimal Case 1 evaluator; returned AUDIT-CIRCULARITY)

[done · 2026-06-14/15]  FIRST AUTHORIZED MODEL RUNS — instrument-side, NOT certification
│   experiments/2026-06-15_minimal-fp16-int8-twohop-l1/  (FP16↔INT8 byte-identical
│     on 24/24; VERDICT INCONCLUSIVE per pre-registered FP16-baseline gate)
│   experiments/2026-06-15_terminal-attraction-bounds-sweep/  (3×2 factorial, n=12/cell;
│     §8 reading POSITION_EFFECT; dominant signal REVERSE-K — attraction falls with clutter)
│
├── ↳ Finding track (parked) — Terminal Attraction
│      │   finding-tracks/terminal-attraction/
│      └── Senior-authored finding report v0.4 + 2 figures + PDF
│             (C5 PASS w/ I1+G1/G2 ; C6 prior-art PASS scoped diagnostic)
│
[done · 2026-06-15]  Path A K-Sweep Scout + FP16 Constructibility Run
│   Path A FP16 Constructibility Run — VERDICT FAIL via dominant-signature branch
│     (Manager-authorized FP16 only; no compression; no retry; no post-hoc changes)
│   K-Sweep scout K=1..5 outcome BOUNDARY (best at K=1 edge; K=5 reproduces FAIL byte-exact)
│   Cliff finding note v0.2: admissible-load set = {K=1}; component (hop2 in isolation)
│     INADMISSIBLE under competition on the existing construction; the 40% off-map is
│     the substrate ceiling for this construction, not a defect to engineer away
│   Construction Property Taxonomy v0.1: V3 (same-depth-competitor) named as the
│     conforming foreclose-all candidate; D1/D2 (tag / topic) violate R2/R3
│
[done · 2026-06-16/17]  V3 Instrument Byte-Audit HOLD → Re-Lock → Philosophy Decision
│   SE V3 byte-audit (return c3f4e667): of-record v0.3 prereg pinned STALE instrument
│     digests (the K-sweep additive sweep-mode patch had moved inspector/constants
│     under v0.3's binding); patch verified ADDITIVE; V3 real-run gate preserved
│   Senior v0.4 binding patch — re-pin inspector cb4b0b60 + constants 1d761c3d;
│     no values / thresholds / outcome rules / categories / controls / stop-rules changed
│   CS V3 real-run param-deviation fixture (10): PASS — addresses Senior G2 gap;
│     confirms patched inspector still fail-closed REJECTs a Manager-lock deviation
│   Manager + TL re-lock 2026-06-16; corrective 2026-06-17 (placeholder bytes bfb4404a
│     replaced with finalized filled bytes c61a3256; no scientific content changed)
│   ──
│   PHILOSOPHY DECISION RECORD v0.1 RATIFIED 2026-06-17 (path-a/of-record/)
│     Manager commits to FORECLOSE-ALL as Path A gate standard (a composition gate is
│       valid only if only traversal can select the answer)
│     MAKE-IDENTITY-EASY considered-and-rejected (introduces non-traversal tag/topic-
│       match route; weakens what the gate is supposed to measure)
│     V3 named as the current conforming CANDIDATE VEHICLE — NOT certified
│     Floor check remains the empirical question; substrate-infeasibility is a valid
│       outcome and is NEVER a license to loosen the standard
│
[done · 2026-06-17/18]  V3 Build Open Slots → Floor-Check → COMPONENT-ADMISSIBLE-UNDER-COMPETITION
│   Manager + TL ACTION 2026-06-17 "Begin V3 Build Open Slots"
│   path-a/build/   v3_item_generator + v3_prompt_realizer + v3_prompt_conformance_checker
│                   + v3_neutral_token_pool   (build verification 8/8 PASS,
│                                              deterministic, zero model imports)
│   Senior PASS on V3 build package (sha e9b7e349)
│   ──
│   V3 floor-check prereg ladder: v0.1 (CS HOLD E1-E5) → v0.3 (CS HOLD F1-F3) → v0.4
│     (CS final feasibility PASS-with-MAX_DELTA-caveat; C5 claim-risk PASS)
│   Floor-check tooling: v3_floor_check_analyzer + ancillary scripts (SE-verified)
│   V3 FLOOR-CHECK RUN executed 2026-06-18 — Qwen2.5-3B-Instruct revision
│     aa8e72537993ba99e69dfaafa59ed015b17504d1 (FP16, greedy, mlx_lm 0.31.3, M2 Max);
│     384 prompts × 96 items; experiments/2026-06-18_v3-floor-check-run/
│     §10 BRANCH: COMPONENT-ADMISSIBLE-UNDER-COMPETITION
│       hop2 96/96 (Wilson lower 0.9615 > 0.75)
│       hop1 87/96 (Wilson lower 0.8313 > 0.75)
│       dq C* count 0/96 (no direct-recall)
│       invalidated 0/96; admissibility 96/96; conformance 96/96; error-structure OK
│     Bounded as component-admissibility ONLY (per v0.4 §11 forbidden interpretations:
│       NOT certification, NOT "the model composes", NOT capability, NOT mechanism)
│     Senior PASS on run; analyzer decision reproduced byte-identical at 6a34f6dc
│
[done · 2026-06-18/19]  V3 Composite-Gate Lifecycle → PRECONDITION-FAIL
│   PREREGISTRATION V3 COMPOSITE GATE v0.2 (retitled from "Composite Certification"
│     per CS A1 + C5 rulings; bounded-validity wording, fresh disjoint seed range
│     097..192 mandated; MAX_DELTA=8 preserved by ≤999 3-digit invariant; two separate
│     lower-Wilson gates: primary > 0.75 reliability + necessary > 0.45 not-shortcut
│     floor; GATE-CLEARED-THIS-RUN ≠ FINAL certification; strengthened forbidden
│     interpretations — no seam / compression / capability / mechanism leakage)
│   Composite-gate tooling: v3_composite_gate_item_generator (WRAPPER — preserves
│     underlying v3_item_generator at sha 6a2ceee1 unchanged) +
│     v3_composite_gate_analyzer + v3_composite_error_logger; build verification
│     all 4 §8 branches exercised on synthetic scored sets
│   Senior PASS on tooling; CS final feasibility PASS (8/8 checks)
│   TL APPROVED 2026-06-18 (locked 3 new + 6 reused tooling digests + MAX_DELTA caveat
│     + interpretation boundary)
│   ──
│   V3 COMPOSITE-GATE RUN executed 2026-06-18 — fresh seeds 097..192 (byte-distinct
│     from floor-check 001..096; 0 shared role tokens by prefix-injection proof);
│     same model + decoding profile as the floor check;
│     experiments/2026-06-18_v3-composite-gate-run/
│     §8 BRANCH: PRECONDITION-FAIL (cond_c fails; composite gate NOT read)
│       hop1 28/96 (Wilson lower 0.2102 << 0.75 floor)   ← THE BLOCKER
│       hop2 96/96 (Wilson lower 0.9615); dq 0/96; invalidated 0; admissibility 96/96
│       composite 63/96 (Wilson lower 0.5569) — INFORMATIONAL ONLY; gate not read
│     STRIKING CONTRAST: hop1 swing 87/96 → 28/96 across the SAME construction at
│       different per-item indices (001..096 vs 097..192); every OTHER measured
│       property identical (hop2, dq, invalidated, admissibility, conformance,
│       MAX_DELTA all match). Mechanism NOT decidable from this run (per v0.2 §10).
│   Senior PASS on run; missing manifest filed 2026-06-19 per TL ACTION (lifecycle
│     closed as valid PRECONDITION-FAIL with full sha256 inventory)
│
[done · 2026-06-19]  Hop1 Stability Investigation → HOP1-STABLE-INADMISSIBLE
│   Separately pre-registered + TL-approved (NOT licensed by PRECONDITION-FAIL alone);
│     answers the candidate question "why does hop1 differ at 097..192 vs 001..096?"
│   experiments/2026-06-19_hop1-stability-run/  — 6 fresh blocks; P-role distractor
│     reproduces 100% on fresh items ⇒ hop1 is STABLY INADMISSIBLE on this construction,
│     not a seed/index artifact. Mechanism still not claimed.
│   Finding report v0.1 (path-a/in-review/HOP1-STABILITY-FINDING-REPORT-v0.1.md) fed the
│     Paper 2 V3-delta integration.
│
[done · 2026-06-19/21]  Paper 2 V3-delta → v1.2 PUBLIC RELEASE
│   V3-delta freeze/tag substitution + integrated revised manuscript → release candidate
│     (v1.1-rc1, body byte-identical to reviewed draft) → C5-cleared v0.3 tightening +
│     limitations delta → status-line cleanup (narrow Manager-authorized edit)
│   PAPER 2 v1.2 PUBLIC RELEASE 2026-06-21:
│     release commit 34ef9215; annotated tag paper2-cells01-03-v1.2 (obj 82a24b7d);
│     released Markdown sha256 7d6bd7f2… ; v1.2 PDF in follow-on commit cb977b54
│     (PDF lives after the tag by design)
│   Paper 2 v1.0 tag 41c033fc UNCHANGED (verified at release). §6/§9 now carry the hop2
│     single-lookup qualification language used by the compression-rung lane below.
│   governance/2026-06-21_paper-2-v1.2-public-release/
│
[direction · 2026-06-21; packet prep only, NO run authorized]  First Bounded Compression Rung
    Manager direction: open the first compression rung as INSTRUMENT-VALIDATION-UNDER-STRESS
      (FP16 → INT8 on a single qualified target). Blanket compression block NARROWLY
      LIFTED for INT8 authorization-packet authoring ONLY; INT4 stays blocked.
    Required next artifact: FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.1 (Senior lane).
      Run gated on: Senior draft → C5 → CS feasibility → TL → Manager by-name authorization.
    Bounded perimeter: "Can the fail-closed instrument produce a valid FP16→INT8 stress-
      retention readout on the selected qualified target?" — NOT seam / Claim C /
      composition / capability / mechanism. Fail-closed if FP16 baseline not qualified.
    NOT the first INT8 bytes: INT8-RUNG-1 (06-13, QUARANTINED) and the minimal FP16↔INT8
      run (06-15, INCONCLUSIVE per FP16-gate) are distinct and do not generalize the lift.
    governance/2026-06-21_first-compression-rung-direction/                          ◄── YOU ARE HERE
      CS ACKNOWLEDGED; standing by for the Senior packet draft.
```

## Round-trips (ventured and came back — recorded for honesty)

```text
Paper A → paper4- rename ............. REVERTED (A/B dyad preserved)
Root docs → _meta/ ................... RESTORED to root (GitHub front-page semantics)
Hash Integrity location .............. governance/standing/ → papers/standing-notes/
                                        (Manager Option 3; NOT promoted to Paper 4)
tier0-run/ delete → restore .......... deleted 06-05 (75a2c27); restored 06-08 as part
                                        of the Cells01-03 evidence commit (49aa222);
                                        later 06-14 tokenizer-untrack revert (18c357d,
                                        sealed-tree scope-violation fix)
```

## Sealed (do not move)

```text
experiments/                                                   sealed-bytes territory
tier0-run/                                                     categorically sealed (Stage 0)
+ 4 sealed-byte files in experiments/2026-06-11_lane-1a-prime/validation/
  and experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md
```

## Where to look (bridge to the tree)

```text
Released papers ................. papers/
Tier 1 instrument architecture .. tier-1-instrument/
Finding tracks .................. finding-tracks/
Deferred (Paper B) .............. paper-b/planning/
Closed-route history ............ archive/d4-closed-route/
Standing governance ............. governance/standing/
                                  (PROGRAM-MAP · NORTH-STAR · POSITION · CONTROL-LEDGER)
Dated governance epochs ......... governance/epochs/
Run data (SEALED) ............... experiments/
Stage 0 instrument (SEALED) ..... tier0-run/  (Two-Hop Level-1 lock + Cells01-03)
Repo-level docs ................. README · STATUS · REVIEW · _meta/INDEX
```

## Boundaries

```text
- Records state; changes none.
- Reopens no closed route (D4 stays closed; reopening is Manager-only).
- Reinterprets no accepted diagnosis.
- Authorizes no model execution / certification run / compression / build.
- Creates no new research claims; changes the scientific meaning of no artifact.
- Sealed bytes do not move. Surfacing Stage 0 / tier0-run on this map is a
  historical reference only — tier0-run stays sealed; Stage 0 stays CLOSED/locked.
```

---

*Living map. Re-sync when a stage closes, a new branch opens, or a routing decision changes a tracked branch's status. For frozen per-route detail with the 11-field schema, see `governance/standing/PROGRAM-CONTROL-LEDGER-v0.3.md` — this map is the at-a-glance view; the ledger is the deeper read.*

*Change-note (rev 2, Senior content revision; verified against the record with CS):*
*— ADDED Stage 0 / Tier 0 as the foundational trunk node (Two-Hop Level-1 matched-pair instrument lock, packet self-dated 06-07 / scorer amended 06-08; Cells01-03 evidence committed 06-08, 49aa222) — previously invisible except as "sealed."*
*— ADDED the repo reorganization (whole-repo move) as a 06-14 trunk stage (execution all-hash-PASS, sealed bytes unchanged, closeout v1.0 accepted) — previously present only as the "root docs restored" consequence.*
*— CORRECTED the D4 off-ceiling line: "No candidate cleared the gate off-ceiling cleanly" → the constructed-positive PASSED validation off-ceiling (clean 40/40 spared, defective eliminated), but its clean member sat at ceiling, so a below-ceiling certified operating point was never demonstrated (= the open structural-limit edge). The old line understated the constructed-positive and mis-stated why the edge is open.*
*— CORRECTED foundation dating: 06-09 → span 05-31 → 06-10 (initial commits 05-31; Paper 2 v1.0 06-09; Paper 3 v1.0 + v1.1 and B1 v2 lock 06-10).*
*— NOTED the NORTH-STAR v1.1 → v1.2 method-as-basis reframe (a conceptual shift, not just a version bump) and that Paper A's positioning section went through external peer review (v0.7).*
*— ADDED the tier0-run delete (06-05, 75a2c27) → restore (06-08, 49aa222) round-trip + the 06-14 tokenizer-untrack revert (18c357d) to Round-trips.*
*— Ledger pointer LEFT at v0.1 (v0.2 not yet on origin; bump when filed). Records state only; reopens nothing; unseals nothing; changes no scientific meaning.*

*Change-note (rev 3, CS additions, 2026-06-15):*
*— EXPANDED the G6 module home (under Tier 1) to enumerate the full Case 1 / Option B workflow: entry framing, audit framing, audit RESULT, internal-consistency closeout, Option B readiness note, non-design-target candidate inventory, HOLD review (v0.1+v0.2), Case 1 design, the constructed `case-1-missing-channel/` bundle + G6 Case 1 Manual Audit Result, and the FIRST G6 SOFTWARE (`evaluator/`, returned AUDIT-CIRCULARITY).*
*— ADDED the two FIRST AUTHORIZED MODEL RUNS as a new trunk stage (2026-06-14/15): the minimal FP16↔INT8 run (byte-identical 24/24; INCONCLUSIVE per pre-registered FP16-baseline gate) and the TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1 (3×2 factorial, 216 generations, primary §8 reading POSITION_EFFECT, dominant signal REVERSE-K). These are the first model-facing events of the program; classified instrument-side, NOT certification / NOT Lane 4.*
*— ADDED the Terminal Attraction finding track (`finding-tracks/terminal-attraction/`) as a branch — Senior-authored finding report v0.4 + 2 figures + PDF, parked beside the CAL-Q finding track. C5 PASS w/ I1+G1/G2 carried; C6 prior-art PASS scoped diagnostic.*
*— UPDATED "YOU ARE HERE" to the finding-track branch; the next build of record remains G6 (per finding-report §8 Senior recommendation: bank the finding; do not reorder against G6).*
*— Records state only; reopens nothing; unseals nothing; authorizes nothing; changes no scientific meaning. Sealed bytes 4-of-4 byte-identical at filing time. PROGRAM-POSITION-v0.1 / PROGRAM-MAP-v2.0 / PROGRAM-CONTROL-LEDGER-v0.3 NOT updated this turn (Senior/Manager-maintained; awaiting Senior draft for any control-ledger v0.4 reflecting the two named runs).*

*Change-note (rev 4, CS additions, 2026-06-19):*
*— EXTENDED the trunk with the V3 program lifecycle 2026-06-15 → 2026-06-19, previously absent. Five new trunk nodes added in time order: (a) Path A K-Sweep scout + FP16 constructibility run (2026-06-15) producing the cliff-finding-v0.2 foreclosure that pointed the program at V3; (b) V3 instrument byte-audit HOLD → re-lock at v0.4 (Senior c3f4e667 → Manager+TL re-lock 06-16 → corrective 06-17 placeholder→finalized bfb4404a→c61a3256) → Philosophy Decision Record v0.1 RATIFIED 2026-06-17 committing FORECLOSE-ALL as Path A gate standard with V3 as conforming candidate vehicle; (c) V3 Build Open Slots realized (4 deliverables; 8/8 build verification PASS) → V3 FLOOR-CHECK RUN 2026-06-18 → §10 COMPONENT-ADMISSIBLE-UNDER-COMPETITION (hop2 96/96, hop1 87/96, dq 0/96; bounded as component-admissibility ONLY); (d) V3 COMPOSITE-GATE prereg v0.2 (retitled from "Composite Certification") → 3 new tools built (wrapper preserves underlying generator unchanged) → TL APPROVED → COMPOSITE-GATE RUN 2026-06-18 → §8 PRECONDITION-FAIL with the striking hop1 swing 87/96 → 28/96 across the same construction at different per-item index ranges; (e) missing manifest filed 2026-06-19 (lifecycle closed). YOU ARE HERE moved from the Terminal Attraction finding-track branch to the composite-gate close.*
*— REMOVED the rev-3 "next: bank Terminal Attraction; keep G6 the next build of record" pointer — superseded by the actual events. Terminal Attraction remains a parked finding track (not abandoned, just not the focal active surface). G6 (tier-1 instrument architecture) remains a parallel discipline; its trunk node from rev 3 stays intact above. The V3 lifecycle became the focal active surface from the philosophy decision (2026-06-17) onward.*
*— ADDED a candidate-question annotation for the OPEN hop1 stability investigation (why does hop1 differ at 097..192 vs 001..096?). Recorded as a candidate question NOT licensed for execution by the PRECONDITION-FAIL outcome alone; would need its own pre-registration + Manager/TL authorization.*
*— Records state only; reopens no closed route; unseals no sealed bytes; authorizes no run/build/compression/claim; changes no scientific meaning. PROGRAM-POSITION / PROGRAM-MAP / PROGRAM-CONTROL-LEDGER not updated this turn (Senior/Manager-maintained; this map is the at-a-glance view, the ledger is the deeper read). K=5 FAIL remains closed; V3 ≠ C0; neither the COMPONENT-ADMISSIBLE nor the PRECONDITION-FAIL outcome bears on it.*

*Change-note (rev 5, CS additions, 2026-06-25):*
*— RESOLVED the rev-4 OPEN candidate-question block: the hop1 stability investigation was separately pre-registered, TL-approved, and EXECUTED 2026-06-19 → HOP1-STABLE-INADMISSIBLE (6 fresh blocks; P-role distractor reproduces 100% on fresh ⇒ stable inadmissibility on this construction, not a seed/index artifact; mechanism still not claimed). Added as a `[done]` trunk node.*
*— ADDED the Paper 2 V3-delta → v1.1-rc → v1.2 PUBLIC RELEASE + PDF trunk node (2026-06-19 → 06-21): release commit 34ef9215; tag paper2-cells01-03-v1.2 (obj 82a24b7d); released Markdown sha256 7d6bd7f2…; PDF follow-on cb977b54. Paper 2 v1.0 tag 41c033fc verified UNCHANGED at release.*
*— ADDED the First Bounded Compression Rung direction (2026-06-21) as a `[direction]` node (packet prep only; INT8 packet-authoring lift; INT4 still blocked; run gated on the full chain; fail-closed perimeter). Noted INT8-RUNG-1 (06-13 QUARANTINED) and the minimal FP16↔INT8 run (06-15 INCONCLUSIVE) as distinct prior INT8 touches that do not generalize the lift.*
*— MOVED YOU ARE HERE from the composite-gate close to the compression-rung standby (CS acknowledged; awaiting the Senior packet draft).*
*— Records state only; reopens no closed route; unseals no sealed bytes; authorizes no run/build/compression/claim; changes no scientific meaning. Companion CS-lane updates this turn: refreshed passdown (governance/passdown/2026-06-25_passdown-letter.md) + standing-card revision (INT8 packet-authoring lift, INT8/INT4 split, v1.2 + Paper 3 tags added to protected surfaces). Root docs STATUS/README/REVIEW left user-owned (unchanged). K=5 FAIL remains closed.*
