# Program Path Map

**Last updated:** 2026-06-15 (rev 3 — CS additions after first authorized model runs + Terminal Attraction finding-track filing. See change-note at foot.)
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
│             (C5 PASS w/ I1+G1/G2 ; C6 prior-art PASS scoped diagnostic)        ◄── YOU ARE HERE
│
[next · per Senior post-run breakdown v0.2 + finding report §8 recommendation]
    Bank the terminal-attraction finding; keep G6 the next build of record.
    Two model runs done; instrument-first stance preserved; no reorder against G6.
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
