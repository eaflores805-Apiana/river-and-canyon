# Program Path Map

**Last updated:** 2026-06-14 (CS housekeeping)
**Re-sync rule:** if this and the record disagree, the record wins. Re-sync when a stage closes or a new branch opens. The `git log` is the authoritative timestamp for each commit.

A living overview of where the program has been, where it is, and where it ventured off. Coarse-grained: main stages, not every commit. The trunk reads top → bottom in time; branches show where the work split (closed routes, parked tracks, new directions).

For full per-route status see [`governance/standing/PROGRAM-CONTROL-LEDGER-v0.1.md`](governance/standing/PROGRAM-CONTROL-LEDGER-v0.1.md); for the route of record see [`PROGRAM-MAP-v2.0`](governance/standing/PROGRAM-MAP-v2.0.md); for the standard see [`NORTH-STAR-v1.2`](governance/standing/NORTH-STAR-v1.2.md). This is the path-and-branches view; those are the authoritative trackers.

---

## The trunk (top → bottom = progression in time)

```text
PROGRAM TRUNK

[done · 2026-06-09]  Foundation
│   Papers 1, 2, 3 released — the metrology tower
│   (method → first result → certification protocol)
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
│      │   No candidate cleared the gate off-ceiling cleanly
│      ├── archive/d4-closed-route/
│      ├── CAL-Q rescue attempt → converted to FINDING TRACK (not rescued)
│      │       finding-tracks/cal-q-format-sensitive-abstention/
│      └── INT8-RUNG-1 → QUARANTINED (non-driving)
│
[done · 2026-06-14]  Baseline Gate Repair Design v0.1
│   Model-free endpoint for the open structural-limit edge
│   Carries it to the GREEN boundary; does not cross
│   governance/epochs/2026-06-11_lane-1a-prime/BASELINE-GATE-REPAIR-DESIGN-v0.1.md
│
[done · 2026-06-14]  POST-PIVOT hybrid direction adopted: "instrument first, seam deferred"
│
├── ↳ Paper A — RELEASED (instrument paper)
│      │   Lettered A/B dyad — NOT a 4th metrology paper
│      │   papers/paper-a-before-retention/
│      └── Paper B (stress paper) reserved as DEFERRED placeholder
│              paper-b/planning/   (empty by design — load-bearing slot for the dyad)
│
└── ↳ Tier 1 instrument architecture  (the active branch)
       │   tier-1-instrument/
       ├── Eval-Validity Gate Tool Spec v0.1   (CS PASS)
       └── G6 Standing Rejection-Audit Spec v0.1  (CS PASS)
              │
              ├── G6 Entry Framing v0.1 filed  (CS PASS)        ◄── YOU ARE HERE
              │
              └── [next · model-free] Retrospective audit of standing refusals
                  (D4 saturation, CAL-Q) against G6 spec's validation targets
```

## Round-trips (ventured and came back — recorded for honesty)

```text
Paper A → paper4- rename ............. REVERTED (A/B dyad preserved)
Root docs → _meta/ ................... RESTORED to root (GitHub front-page semantics)
Hash Integrity location .............. governance/standing/ → papers/standing-notes/
                                        (Manager Option 3; NOT promoted to Paper 4)
```

## Sealed (do not move)

```text
experiments/                                                   sealed-bytes territory
tier0-run/                                                     categorically sealed
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
Model weights (SEALED) .......... tier0-run/
Repo-level docs ................. README · STATUS · REVIEW · _meta/INDEX
```

## Boundaries

```text
- Records state; changes none.
- Reopens no closed route (D4 stays closed; reopening is Manager-only).
- Reinterprets no accepted diagnosis.
- Authorizes no model execution / certification run / compression / build.
- Creates no new research claims; changes the scientific meaning of no artifact.
- Sealed bytes do not move.
```

---

*Living map. CS housekeeping. Re-sync when a stage closes, a new branch opens, or a routing decision changes a tracked branch's status. For frozen per-route detail with the 11-field schema, see `governance/standing/PROGRAM-CONTROL-LEDGER-v0.1.md` — this map is the at-a-glance view; the ledger is the deeper read.*
