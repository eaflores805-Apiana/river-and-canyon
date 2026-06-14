# PROGRAM-CONTROL-LEDGER-v0.1

**Version:** v0.1. River and Canyon program. Live route/branch control ledger.
**Status:** MODEL-FREE CONTROL ARTIFACT. A dashboard of the program's routes, their state, governing artifacts, and permitted next actions — assembled from origin/main at HEAD **`931b81a`** (read from bytes, not reconstructed). It records state; it changes none. Reopens no closed route, reinterprets no accepted diagnosis, authorizes no execution. Supersede by versioned replacement only; keep in sync with the record (if this and origin disagree, origin wins — re-sync).
**Owner:** Senior drafts · CS verifies repo-state (paths/commits exist + match) · Team Lead routes · Manager owns route decisions.
**Companions (the canonical sources this ledger points to, does not replace):** PROGRAM-MAP-v2.0 (the route/map of record), NORTH-STAR-v1.2 (the standard), PROGRAM-POSITION-v0.1 (the "you are here").

---

## Dashboard (at-a-glance: route → status)

```text
ROUTE                          STATUS                     OWNER
Program Map v2.0 / Reading C   ACTIVE (map of record)     Manager
North Star v1.2                ACTIVE (the standard)      Manager
Program Position v0.1          ACTIVE (live tracker)      Senior/CS
D4 certification-readiness      CLOSED (PIVOT)             Manager (reopen-only)
CAL-Q finding track             PARKED-ALIVE (secondary)   Senior
Baseline Gate Diagnosis         DONE (Stage E PASS)        accepted
Baseline Gate Repair Design     FILED (model-free endpoint) accepted
Tier 1 / G6                     ACTIVE-MODEL-FREE (next)   Senior→CS→TL→Mgr
Paper A                         RELEASED (instrument paper) Manager
Paper B                         DEFERRED (placeholder)     Manager (separate auth)
INT8-RUNG-1                     QUARANTINED (non-driving)   Manager
Hash Integrity / standing-notes FILED (standing note)      Manager
Repo structure / v0.5 doctrine  FILED (doctrine)           Senior→CS

ROUTE-STATE (global): YELLOW (model-free work proceeds) · RED (no execution).
```

## Global closed gates (apply to ALL routes unless a route notes an exception)

```text
No model execution · No new run · No certification run · No compression / INT8 /
INT4 · No second compression rung · No full ladder · No Claim C / seam activation ·
No Paper B activation · No D4 reopening (Manager-only) · No G6 software build /
implementation · No promotion of quarantined INT8-RUNG-1 · No public benchmark
packaging · No funder-facing release · No SBIR submission · No external release ·
No new research claims · Sealed bytes (experiments/, tier0-run/) DO NOT MOVE.
```

Per-route "Closed gates" below list only route-SPECIFIC closures beyond this global set.

---

## Route records (all 11 fields per route)

### 1. Program Map v2.0 / Reading C
```text
Status:            ACTIVE — the route/map of record.
Artifact of record: PROGRAM-MAP-v2.0.md
Current path:      governance/standing/PROGRAM-MAP-v2.0.md
Last commit:       6a4e604 (file) ; ledger HEAD 931b81a
Last Mgr decision: Reading C selected (on PROGRAM-MAP-RECONCILIATION-v0.1); v2.0
                   authored to execute it. Re-confirmed this session (stands).
Evidence location: governance/standing/PROGRAM-MAP-v2.0.md ;
                   reconciliation archived at archive/d4-closed-route/quarantine/
                   PROGRAM-MAP-RECONCILIATION-v0.1.md
Next permitted:    none required (stands). Supersede only by a new versioned map if
                   the Manager changes the route.
Closed gates:      route changes are Manager-only; no silent edits.
Open risk/watch:   none active.
Owner:             Manager (route authority); Senior drafts; CS verifies.
```

### 2. North Star v1.2
```text
Status:            ACTIVE — the standing standard.
Artifact of record: NORTH-STAR-v1.2.md (v1.1 retained, superseded)
Current path:      governance/standing/NORTH-STAR-v1.2.md
Last commit:       292b478 (filed) ; ledger HEAD 931b81a
Last Mgr decision: v1.2 supersession (method-as-basis §2 refinement, C5-integrated)
                   accepted + filed.
Evidence location: governance/standing/NORTH-STAR-v1.2.md ; companion
                   governance/standing/WHAT-KIND-OF-SMOOTHING-v0.2.md
Next permitted:    none required. Supersede-by-versioned-replacement only.
Closed gates:      Manager-owned; no silent edits.
Open risk/watch:   none active.
Owner:             Manager.
```

### 3. Program Position v0.1
```text
Status:            ACTIVE — live position tracker ("you are here").
Artifact of record: PROGRAM-POSITION-v0.1.md
Current path:      governance/standing/PROGRAM-POSITION-v0.1.md
Last commit:       f87325b (file) ; ledger HEAD 931b81a
Last Mgr decision: tracks the accepted state; updated when a stage closes.
Evidence location: governance/standing/PROGRAM-POSITION-v0.1.md
Next permitted:    update as stages close (records "[done] Baseline Gate Diagnosis").
                   NOTE: may lag recent closes (repair design, G6 entry); a refresh
                   is a model-free housekeeping option.
Closed gates:      reflects, does not decide.
Open risk/watch:   staleness vs the record (re-sync before relying on it).
Owner:             Senior maintains; CS verifies.
```

### 4. D4 certification-readiness route
```text
Status:            CLOSED — PIVOT (a supported negative result).
Artifact of record: the D4 synthesis + Baseline Gate Diagnosis (see route 6).
Current path:      archive/d4-closed-route/ (historical evidence)
Last commit:       move-resident (1e5c037 relocation) ; ledger HEAD 931b81a
Last Mgr decision: D4 SYNTHESIS v0.3 ACCEPTED (MANAGER-D4-SYNTHESIS-v0.3-ACCEPTANCE
                   -2026-06-11) — route closed on PIVOT; no further D4 repair.
Evidence location: archive/d4-closed-route/{governance,cal-sweep,quarantine,
                   constructed-positive-validation,reference-imagery}/
Next permitted:    none. CLOSED unless the Manager EXPLICITLY reopens.
Closed gates:      no D4 rescue; no off-ceiling repair beyond the filed design;
                   reopening is Manager-only.
Open risk/watch:   the structural-limit edge (tracked under routes 6 + 7), not D4
                   itself.
Owner:             Manager (reopen-only).
```

### 5. CAL-Q finding track
```text
Status:            PARKED-ALIVE — secondary finding (format-sensitive abstention).
Artifact of record: cal-q-finding-diagnostic-plan-v0.1.md
Current path:      finding-tracks/cal-q-format-sensitive-abstention/
Last commit:       move-resident (1e5c037) ; ledger HEAD 931b81a
Last Mgr decision: preserved as a FINDING TRACK (explicitly NOT a D4 rescue).
Evidence location: finding-tracks/cal-q-format-sensitive-abstention/{findings,
                   verifications}/ (run report, interpretation, finding writeup)
Next permitted:    none authorized; the diagnostic plan's branches require separate
                   authorization. Available as a future model-free read.
Closed gates:      no CAL-Q rerun; not a D4 rescue; safe claim preserved verbatim.
Open risk/watch:   claim scope — the safe finding must not inflate into a general
                   abstention claim.
Owner:             Senior.
```

### 6. Baseline Gate Diagnosis
```text
Status:            DONE — Stage E PASS (CS-verified, Manager-accepted).
Artifact of record: BASELINE-GATE-DIAGNOSIS-v0.1.md
Current path:      governance/epochs/2026-06-11_lane-1a-prime/BASELINE-GATE-
                   DIAGNOSIS-v0.1.md
Last commit:       move-resident (1e5c037) ; ledger HEAD 931b81a
Last Mgr decision: accepted on the D4 synthesis v0.3 (Stage E recorded PASS in
                   PROGRAM-POSITION).
Evidence location: same epoch dir (CS verification + the cited run bytes in
                   archive/d4-closed-route/ + experiments/2026-06-11_lane-1a-prime/)
Next permitted:    none — stands. Do NOT redraft or reinterpret. Its one open edge
                   is carried by route 7.
Closed gates:      diagnosis not reopened/reinterpreted.
Open risk/watch:   the one narrow STRUCTURAL-LIMIT risk it left open (→ route 7).
Owner:             accepted (no active owner action).
```

### 7. Baseline Gate Repair Design
```text
Status:            FILED — accepted as the MODEL-FREE ENDPOINT for the structural-
                   limit edge (carries it to the GREEN boundary; does not resolve).
Artifact of record: BASELINE-GATE-REPAIR-DESIGN-v0.1.md
Current path:      governance/epochs/2026-06-11_lane-1a-prime/BASELINE-GATE-REPAIR-
                   DESIGN-v0.1.md
Last commit:       931b81a (filed) ; ledger HEAD 931b81a
Last Mgr decision: accepted as filed model-free endpoint; NO certification run
                   authorized.
Evidence location: same artifact (byte-anchored to constructed-positive closeout +
                   diagnosis evidence: window union 0.6125, cap 0.8, ceiling−δ)
Next permitted:    none model-free remaining on this edge. RESOLUTION requires a
                   FUTURE Manager-authorized GREEN certification run (not requested).
Closed gates:      no resolution claimed; no certified baseline claimed; no run.
Open risk/watch:   whether the off-ceiling D1–D7 window is wide enough to certify —
                   UNRESOLVABLE model-free; needs the gated run.
Owner:             Manager (holds the GREEN decision).
```

### 8. Tier 1 / G6 (standing rejection-audit)
```text
Status:            ACTIVE-MODEL-FREE — the current next direction.
Artifact of record: G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md (the spec) ;
                   TIER-1-G6-ENTRY-FRAMING-v0.1 (entry framing — FILED at 3204a9c).
Current path:      spec: tier-1-instrument/specs/g6-standing-rejection-audit-spec-
                   v0.1.md ; module home: tier-1-instrument/modules/g6-standing-
                   rejection-audit/ ; entry framing: tier-1-instrument/modules/g6-standing-
                   rejection-audit/TIER-1-G6-ENTRY-FRAMING-v0.1.md.
Last commit:       spec move-resident (1e5c037) ; entry framing filed at 3204a9c ; ledger HEAD 931b81a
Last Mgr decision: Manager directed model-free Tier 1 / G6 work as the next path;
                   G6 spec already CS-verified.
Evidence location: tier-1-instrument/specs/ (spec + verifications) ; Tool Spec
                   (eval-validity-gate-tool-spec-v0.1.md) is the parent architecture.
Next permitted:    model-free G6 work — e.g. a RETROSPECTIVE audit of the standing
                   refusals on record (D4 saturation, CAL-Q) against the spec's
                   validation targets. NOT a build.
Closed gates:      no G6 software build/implementation; no model run; refusal not
                   turned into a product claim; no Paper B.
Open risk/watch:   control-apparatus growth without measurement (North Star: "a gate
                   that guards an empty room") — G6 must not become the reason a
                   future certified baseline + rung keeps being deferred.
Owner:             Senior drafts → CS → TL → Manager.
```

### 9. Paper A
```text
Status:            RELEASED — the instrument paper (lettered A/B dyad; NOT Paper 4).
Artifact of record: paper.md (bundle) + PAPER-A-v1.0 release artifact (sha 4272e12a)
Current path:      papers/paper-a-before-retention/
Last commit:       2c65f2c (rename-revert preserving A/B lineage) ; HEAD 931b81a
Last Mgr decision: released; the paper4- rename was reverted to preserve the A/B
                   lineage (Manager-aware).
Evidence location: papers/paper-a-before-retention/{paper,sections,figures,
                   supplement,revisions,governance}/
Next permitted:    optional future venue submission (separate Manager decision);
                   STANDING PRE-SUBMISSION GATE: §2.1 citations need independent
                   second-reader confirmation before outside sharing.
Closed gates:      not renumbered into the numbered series; no external release
                   without the pre-submission gate cleared.
Open risk/watch:   "publishable" is internal-contribution status only until blinded
                   review (funder-language perimeter).
Owner:             Manager.
```

### 10. Paper B
```text
Status:            DEFERRED — placeholder only (the future stress paper, dyad's B).
Artifact of record: none (reserved slot).
Current path:      paper-b/planning/ (stub README; emptiness is load-bearing)
Last commit:       move-resident (1e5c037) ; ledger HEAD 931b81a
Last Mgr decision: deferred; "No Paper B activation" standing gate.
Evidence location: none — no Paper B artifacts exist.
Next permitted:    none. Activation requires a separate Manager authorization AND a
                   certified-baseline stress result that does not yet exist.
Closed gates:      no Paper B activation; the empty slot must not be filled as a
                   substitute for the certified stress experiment.
Open risk/watch:   premature activation; the dyad's B must remain lettered (not
                   renumbered "paper5-").
Owner:             Manager (separate auth).
```

### 11. INT8-RUNG-1
```text
Status:            QUARANTINED — scientifically retainable, procedurally
                   nonconforming, NON-DRIVING.
Artifact of record: first-compression-rung records + Senior interpretation.
Current path:      governance/epochs/2026-06-11_lane-1a-prime/first-compression-rung/
Last commit:       move-resident (1e5c037) ; ledger HEAD 931b81a
Last Mgr decision: classified quarantined/non-promotable (Program Map v2.0 invariant
                   1); routed as Lane-1a-prime HISTORY (NOT D4, NOT Paper B).
Evidence location: same dir (int8_run_result.json, per-item tables) +
                   experiments/2026-06-11_lane-1a-prime/ (bytes)
Next permitted:    none. Stays quarantined throughout. Not promotable to Lane 4.
Closed gates:      no promotion to official stress evidence; not Lane-4-eligible;
                   not Paper B seed without a separate Manager decision.
Open risk/watch:   accidental citation as official stress evidence — must not happen.
Owner:             Manager.
```

### 12. Hash Integrity / standing-notes
```text
Status:            FILED — standing governance note (Option 3 sub-tree); NOT Paper 4.
Artifact of record: HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2 (md+pdf)
Current path:      papers/standing-notes/hash-integrity-is-not-construct-validity-
                   v0.7.2/
Last commit:       fd9f653 (Option 3 filing) ; later README path fix 2187432 ;
                   ledger HEAD 931b81a
Last Mgr decision: Option 3 accepted (papers/standing-notes/ sub-tree); preserves
                   "not Paper 4" via the sub-dir name.
Evidence location: papers/standing-notes/.../ (md, pdf, figures) ; relocation note
                   at tier-1-instrument/organization/HASH-INTEGRITY-RELOCATION-NOTE-
                   2026-06-14.md
Next permitted:    none required (settled).
Closed gates:      not promoted to Paper 4; scientific meaning unchanged by the move.
Open risk/watch:   none active (a stale-pointer cleanup was handled at 2187432).
Owner:             Manager.
```

### 13. Repo structure / v0.5 doctrine
```text
Status:            FILED — additive doctrine on the CS-passed v0.4 map.
Artifact of record: TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.5.md (v0.1–v0.4 retained)
Current path:      tier-1-instrument/organization/structure/v0.5.md
Last commit:       9f0b358 (filed) ; ledger HEAD 931b81a
Last Mgr decision: v0.5 accepted (Senior PASS, CS-verified PASS).
Evidence location: tier-1-instrument/organization/structure/{v0.1..v0.5,
                   verifications,manager-directions}/
Next permitted:    none required. Future structure changes supersede by new version.
Closed gates:      v0.4 map unchanged; no artifact's scientific meaning altered.
Open risk/watch:   none active.
Owner:             Senior drafts; CS verifies.
```

---

## Ledger boundaries (what this artifact does and does not do)

```text
- It RECORDS state read from origin (HEAD 931b81a); it changes no route.
- It reopens NO closed route (D4 stays closed; reopening is Manager-only).
- It reinterprets NO accepted diagnosis (the Baseline Gate Diagnosis stands as-is).
- It activates NO Paper B; promotes NO quarantined INT8 evidence.
- It authorizes NO model execution and NO G6 implementation.
- It creates NO new research claims.
- Where the ledger and origin disagree, ORIGIN WINS — re-sync and supersede.
NOTE (CS update at filing time, per TL tactical authorization): the Tier 1 / G6
ENTRY FRAMING was filed at commit 3204a9c immediately before this ledger;
row 8 now reflects that filed state. The ledger HEAD anchor (931b81a) is one
commit stale at filing of this ledger; current HEAD at filing = 3204a9c
(entry framing) + the ledger's own filing commit. Per the ledger's own re-sync
rule: origin wins; the next ledger version would refresh the HEAD anchor.
```

*PROGRAM-CONTROL-LEDGER-v0.1 (TL ACTION; model-free live control artifact at origin/main HEAD 931b81a): a dashboard + 13 per-route records (Program Map v2.0/Reading C, North Star v1.2, Program Position, D4 closed-pivot, CAL-Q parked, Baseline Gate Diagnosis done, Repair Design filed-endpoint, Tier 1/G6 active-model-free, Paper A released, Paper B deferred, INT8-RUNG-1 quarantined, Hash Integrity filed, v0.5 doctrine filed), each carrying all 11 requested fields (route/status/artifact-of-record/path/last-commit/last-Manager-decision/evidence/next-permitted/closed-gates/open-risk/owner). Paths + commits read from bytes, not reconstructed. Global closed-gate set factored out; per-route closures are route-specific. Reopens nothing; reinterprets no diagnosis; authorizes nothing; honestly flags the one drafted-not-yet-filed item (G6 entry framing). Route state YELLOW/RED. model-free.*
