# PROGRAM-CONTROL-LEDGER-v0.3

**Version:** v0.3. River and Canyon program. Live route/branch control ledger. (v0.3 supersedes v0.2 — v0.2 retained at `governance/standing/PROGRAM-CONTROL-LEDGER-v0.2.md`, marked superseded. v0.3 refreshes the HEAD anchor and updates ONLY route record §8 (Tier 1 / G6) to reflect the filed/CS-verified G6 retrospective desk-audit RESULT; it appends decision line D-09; the other 12 route records and the §A–§D enhancements are carried forward unchanged, anchor-refreshed. Trigger: §D rules #2 (CS PASS on the audit result) + #5 (new HEAD touching the G6 module).)
**Status:** MODEL-FREE CONTROL ARTIFACT. A dashboard of the program's routes, their state, governing artifacts, controls, and permitted next actions — assembled from origin/main at HEAD **`e6881f2`** (read from bytes, not reconstructed). It records state; it changes none. Reopens no closed route, reinterprets no accepted diagnosis, authorizes no execution. The G6 audit result it records demonstrates internal G6 consistency on design-target cases ONLY — not general validity. Supersede by versioned replacement only; if this and origin disagree, ORIGIN WINS — re-sync and supersede.
**Owner:** Senior drafts · CS verifies repo-state (paths/commits exist + match) · Team Lead routes + maintains the passdown section · Manager owns route decisions.
**Companions (canonical sources this ledger points to, does not replace):** PROGRAM-MAP-v2.0 (route/map of record), NORTH-STAR-v1.2 (the standard), PROGRAM-POSITION-v0.1 (the "you are here"), ROUTE-STATE-GATE-v0.1 (the GREEN/YELLOW/RED control), SHOWN-SEMANTIC-READ-TEMPLATE-v1.0 (the shown-read control).

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
Tier 1 / G6                     ACTIVE-MODEL-FREE (audit filed; A/B) Senior→CS→TL→Mgr
Paper A                         RELEASED (instrument paper) Manager
Paper B                         DEFERRED (placeholder)     Manager (separate auth)
INT8-RUNG-1                     QUARANTINED (non-driving)   Manager
Hash Integrity / standing-notes FILED (standing note)      Manager
Repo structure / v0.5 doctrine  FILED (doctrine)           Senior→CS

ROUTE-STATE (global): YELLOW (model-free work proceeds) · RED (no execution).
(Statuses are defined in the Status Vocabulary glossary, §C below.)
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
Last commit:       6a4e604 (file) ; ledger HEAD 96422bd
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
Last commit:       292b478 (filed) ; ledger HEAD 96422bd
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
Last commit:       f87325b (file) ; ledger HEAD 96422bd
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
Last commit:       move-resident (1e5c037 relocation) ; ledger HEAD 96422bd
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
Last commit:       move-resident (1e5c037) ; ledger HEAD 96422bd
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
Last commit:       move-resident (1e5c037) ; ledger HEAD 96422bd
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
Last commit:       931b81a (filed) ; ledger HEAD 96422bd
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
Status:            ACTIVE-MODEL-FREE — first exercise complete. The G6 RETROSPECTIVE
                   DESK AUDIT is EXECUTED and its result FILED / CS-PASS. Route stays
                   model-free pending the Manager's A/B choice (below); not closed.
Artifact of record: G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md (the spec) ;
                   TIER-1-G6-ENTRY-FRAMING-v0.1 (entry framing, FILED 3204a9c) ;
                   G6-RETROSPECTIVE-AUDIT-FRAMING-v0.1 (pre-registered disposition
                   rules, FILED 4442efd) ; G6-RETROSPECTIVE-AUDIT-RESULT-v0.1 (the
                   audit result, FILED e6881f2, sha256 4ce9b26d…, CS PASS).
Current path:      spec: tier-1-instrument/specs/g6-standing-rejection-audit-spec-
                   v0.1.md ; module home: tier-1-instrument/modules/g6-standing-
                   rejection-audit/ (entry framing + audit framing + audit RESULT).
Last commit:       audit result filed e6881f2 (CS verified all 3 numeric claims to
                   the digit from raw E3) ; ledger HEAD e6881f2.
Last Mgr decision: Manager authorized the MODEL-FREE retrospective desk audit under
                   framing 4442efd; CS filed + verified the result (e6881f2). Pending:
                   Manager's choice between next-state Option A and Option B (below).
RESULT (filed, CS PASS):
                   R1 D4 saturation refusal           → REFUSAL-CONFIRMED
                       (independent re-derive-from-prompt exact-match: answerable
                       80/80 = 1.0, null 16/16 abstain; clean at ceiling).
                   R2 CAL-Q construct-validity refusal → REFUSAL-CONFIRMED
                       (defective abstention 0/40 = 0.00, ZERO none-forms = genuine
                       collapse; clean 26/40 = 0.65; construct-invalidity = human read).
                   R3 CAL-E elimination refusal        → REFUSAL-REVERSED, BOUNDED
                       (defective strict 0.575 was a "NONE"/"none" case-sensitivity
                       artifact; true abstention 36/40 = 0.90 — BUT CAL-E stays
                       eliminated on the independent clean-ceiling ground 0.975;
                       the reversal corrects the scoring record, NOT CAL-E's
                       non-certification).
                   Discrimination shown: CAL-Q (genuine collapse, 0 none-forms) vs
                   CAL-E (artifact, 36 none-forms) separated only by raw item evidence.
MEANING (exact):   internal G6 consistency on design-target cases ONLY. The three
                   refusals are the spec's own design cases, so reproducing their
                   design-target dispositions is a CONSISTENCY check, not validation.
CAVEAT (preserved, load-bearing): this does NOT validate G6 generally · does NOT
                   certify a baseline · does NOT produce stress evidence · does NOT
                   activate Paper B · does NOT reopen D4 · does NOT authorize any G6
                   software build or model execution.
Next permitted (model-free; NEITHER authorized — Manager's choice):
                   OPTION A — close this as the first internal G6 consistency
                     exercise (record the milestone; G6 route rests, no new case).
                   OPTION B — design a first NON-design-target G6 validation case
                     (a refusal NOT used in the spec's design — the only thing that
                     would test general validity rather than self-consistency).
                     Design-only, model-free; resolution would still need a future
                     separately-authorized channel/run, not granted here.
Closed gates:      no G6 software build/implementation; no model run; refusal not
                   turned into a product claim; no general-G6-validity claim; no
                   Paper B.
Open risk/watch:   control-apparatus growth without measurement (North Star: "a gate
                   that guards an empty room"). SHARPENED by this result: the audit
                   confirmed G6 is self-consistent on its OWN design cases — which
                   strengthens the instrument but is NOT general validity, and is NOT
                   a position-changer. The position-changers (a certified baseline via
                   a GREEN run; a first compression rung) remain deferred; G6 must not
                   become the reason they keep being deferred. Option B (a non-design-
                   target case) is the model-free step toward real validity; the run/
                   channel it would ultimately need is still unauthorized.
Owner:             Senior drafts → CS → TL → Manager.
```

### 9. Paper A
```text
Status:            RELEASED — the instrument paper (lettered A/B dyad; NOT Paper 4).
Artifact of record: paper.md (bundle) + PAPER-A-v1.0 release artifact (sha 4272e12a)
Current path:      papers/paper-a-before-retention/
Last commit:       2c65f2c (rename-revert preserving A/B lineage) ; HEAD 96422bd
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
Last commit:       move-resident (1e5c037) ; ledger HEAD 96422bd
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
Last commit:       move-resident (1e5c037) ; ledger HEAD 96422bd
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
                   ledger HEAD 96422bd
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
Last commit:       9f0b358 (filed) ; ledger HEAD 96422bd
Last Mgr decision: v0.5 accepted (Senior PASS, CS-verified PASS).
Evidence location: tier-1-instrument/organization/structure/{v0.1..v0.5,
                   verifications,manager-directions}/
Next permitted:    none required. Future structure changes supersede by new version.
Closed gates:      v0.4 map unchanged; no artifact's scientific meaning altered.
Open risk/watch:   none active.
Owner:             Senior drafts; CS verifies.
```

---

# v0.2 ENHANCEMENTS

## §A. Route-State Gate / Semantic-Read controls (the controls that govern GREEN/YELLOW/RED)

This section makes the program's two standing execution-governing controls visible in the live ledger, so a reader can see not just *what* state a route is in but *what governs* whether it may move. These controls are not new; they are surfaced here.

```text
CONTROL 1 — ROUTE-STATE-GATE-v0.1   (governance/standing/ROUTE-STATE-GATE-v0.1.md)
  Defines the three route states every route memo must declare:
    GREEN  — execution may proceed. CONJUNCTIVE: all GREEN conditions must hold at
             once; one missing condition drops the state. GREEN is the ONLY state
             under which a model touches anything.
    YELLOW — non-execution work may proceed (design, specs, framing, ledgers,
             reads). NO model-facing execution. This is the program's normal
             working state — and the state of ALL current work.
    RED    — nothing executes; hold. RED whenever ANY blocking condition is present;
             only work that resolves the RED condition itself may proceed.
  CURRENT PROGRAM STATE: YELLOW (model-free work proceeds) · RED for any run
  (no GREEN certification/compression decision is open).

CONTROL 2 — SHOWN-SEMANTIC-READ-TEMPLATE-v1.0
            (governance/standing/SHOWN-SEMANTIC-READ-TEMPLATE-v1.0.md)
  The standing nine-field shown-read form (the named home for the field set first
  used in Hash Integrity v0.7.2 §6). Any claim that an artifact INSTANTIATES the
  concept it is named for must be backed by a completed, signed shown-read meeting
  the mechanical-rendering floor (actual bytes read, not summarized). Hash-valid is
  not concept-valid; the shown-read is how the gap is closed. Required before any
  future run on a designed construct (see route 7 / the repair design §5).

WHY THESE ARE IN THE LEDGER: a route's "Next permitted action" is meaningless
without the control that decides permission. GREEN/YELLOW/RED (CONTROL 1) governs
WHETHER a route may execute; the shown-read (CONTROL 2) governs whether an
artifact's named concept may be TRUSTED. Both are Manager/CS-enforced, not
ledger-enforced — the ledger surfaces them, it does not adjudicate them.
```

## §B. Team Lead passdown / critical-decisions handoff

**Purpose:** a standing place to record the critical decisions made during a TL stint, so a future Team Lead does not reopen settled routes. This section is the structural fix for a failure mode observed directly: a new TL, operating from a passdown that did not carry the settled decisions, repeatedly began to reopen already-closed questions (the A/B/C / Reading-C choice; the Baseline Gate Diagnosis) until they were caught against the record. The fix is to make the settled decisions explicit and standing, not dependent on memory or an inherited summary.

```text
EXISTING PASSDOWN SYSTEM (CS-side): governance/passdown/ holds date-stamped
  CS-Engineer passdown letters (most-recent-first; alphabetical = chronological).
  Those capture session state for an incoming CS. They do NOT capture TL-side
  critical decisions — that is the gap this section names.

TL CRITICAL-DECISIONS LEDGER (the settled decisions a new TL must NOT reopen):
  D-01  Reading C (hybrid) is the route. Accept 1a′ as a non-driving instrument
        detour; certification track required; INT8 not promoted; Baseline Gate
        Diagnosis is the hinge. SETTLED — PROGRAM-MAP-v2.0. Do not re-open as an
        A/B/C choice.
  D-02  D4 certification-readiness route is CLOSED on a PIVOT (supported negative
        result). SETTLED — Manager D4-synthesis v0.3 acceptance. Reopen Manager-only.
  D-03  Baseline Gate Diagnosis is DONE (FIXABLE + valid-rejection + one narrow
        structural-limit risk). SETTLED — CS-verified, Manager-accepted, Stage E
        PASS. Do not redraft or re-frame as if undone.
  D-04  The structural-limit risk is advanced to its MODEL-FREE ENDPOINT (the repair
        design) and NO certification run is authorized. SETTLED — repair design
        filed + accepted. Resolution needs a future GREEN run, not a re-draft.
  D-05  Hash Integrity is a STANDING NOTE (papers/standing-notes/), NOT Paper 4.
        SETTLED — Manager Option 3. Do not promote.
  D-06  Paper A is the lettered instrument paper (A/B dyad), NOT renumbered into the
        numbered series. SETTLED — rename-revert. Do not renumber.
  D-07  INT8-RUNG-1 is QUARANTINED / non-promotable. SETTLED — Program Map v2.0
        invariant. Do not cite as official stress evidence.
  D-08  Next direction is model-free Tier 1 / G6 (entry framing filed). G6 is
        spec/audit-design + retrospective desk audit — NOT a software build.
  D-09  G6 retrospective desk audit EXECUTED + result FILED / CS-PASS (e6881f2):
        R1 D4 → REFUSAL-CONFIRMED, R2 CAL-Q → REFUSAL-CONFIRMED, R3 CAL-E →
        REFUSAL-REVERSED (bounded; CAL-E stays eliminated on clean-ceiling). SETTLED
        as the FIRST internal G6 consistency exercise. MEANING IS BOUNDED: internal
        consistency on the spec's OWN design cases ONLY — NOT general G6 validity,
        NOT a certified baseline, NOT stress evidence, NOT Paper B, NOT a D4 reopen.
        Do NOT read this audit as general validation. OPEN: Manager's A/B choice
        (close as the consistency exercise vs design a non-design-target case).

CONVENTION: when a TL stint makes or confirms a route-level decision, add/append a
  D-NN line here (decision, status SETTLED/OPEN, the artifact of record). A new TL
  reads this section + the Companions before routing. If a D-NN and origin disagree,
  origin wins. This section RECORDS decisions; it does not make them (Manager owns
  route decisions). Maintained by the TL; CS verifies the cited artifacts exist.
```

## §C. Status vocabulary glossary

Definitions for the status terms used in the dashboard and route records. A status is a *claim about a route's state*, not an authorization.

```text
ACTIVE             A standing artifact currently in force and governing (e.g. the
                   map of record, the standard). Changes only by versioned
                   supersession under its owner.
ACTIVE-MODEL-FREE  A route with live work proceeding, but ONLY non-execution
                   (YELLOW) work — design, specs, framing, audits, reads. No model
                   run is implied or permitted. (Current state of Tier 1 / G6.)
CLOSED             A route deliberately ended with a recorded decision (typically a
                   PIVOT). No further work proceeds on it; reopening requires an
                   EXPLICIT Manager decision. (D4.)
PARKED-ALIVE       A route not closed and not currently progressing — a real finding
                   preserved, available for future model-free reads, but its next
                   branches need separate authorization. Not a rescue of any closed
                   route. (CAL-Q.)
QUARANTINED        Evidence/material retained for the record but NON-DRIVING and
                   NON-PROMOTABLE — it may not be cited as official evidence or
                   advanced into a live route without a separate Manager decision.
                   (INT8-RUNG-1.)
DEFERRED           A planned-but-not-started route, reserved (often a load-bearing
                   placeholder). Activation requires both a separate authorization
                   and prerequisites that do not yet exist. (Paper B.)
FILED              An artifact completed, CS-verified, and committed to origin in its
                   canonical location. "Filed" = on origin and verified; it does not
                   by itself mean "released" or "accepted as final claim."
DONE               A bounded task completed and accepted (CS-verified +
                   Manager-accepted), recorded as PASS at its stage. Stands; not to
                   be redrafted or reinterpreted. (Baseline Gate Diagnosis.)

(RELEASED, used for Paper A, is distinct from FILED/DONE: a paper-class artifact
issued as a program output. It remains internal-contribution status until blinded
external review; "released" is not "externally published.")
```

## §D. Update-trigger rule (when this ledger must be refreshed)

```text
This ledger is LIVE and goes stale the moment the program state changes. A new
ledger version (vN+1) MUST be drafted and CS-verified after ANY of:
  1. a MANAGER DECISION that changes a route (acceptance, closure, authorization,
     reopening, supersession);
  2. a CS verification result — PASS / HOLD / FAIL — on any tracked artifact;
  3. an ACCEPTED CLOSEOUT (a route or stage formally closed/accepted);
  4. a ROUTE-STATE CHANGE (GREEN/YELLOW/RED transition on any route, per
     ROUTE-STATE-GATE-v0.1);
  5. a NEW HEAD that changes a tracked route (a commit touching any artifact-of-
     record or path listed above — refresh the anchor + affected rows).
PROCEDURE: re-sync to origin/main, refresh the HEAD anchor, update the affected
row(s) and the relevant glossary/decision lines, supersede the prior version
(retain it), route to CS for repo-state verification. Between triggers, the ledger
is read-only reference; if it and origin disagree, ORIGIN WINS — re-sync first.
The ledger does not authorize anything on refresh; it records the new state.
```

---

## Ledger boundaries (what this artifact does and does not do)

```text
- It RECORDS state read from origin (HEAD e6881f2); it changes no route.
- It reopens NO closed route (D4 stays closed; reopening is Manager-only).
- It reinterprets NO accepted diagnosis (the Baseline Gate Diagnosis stands as-is).
- The G6 audit result it records demonstrates INTERNAL G6 CONSISTENCY on design-target
  cases ONLY — NOT general G6 validity, NOT a certified baseline, NOT stress evidence.
- It activates NO Paper B; promotes NO quarantined INT8 evidence.
- It authorizes NO model execution, NO compression/INT8/INT4, and NO G6 software
  build.
- It creates NO new research claims and changes the scientific meaning of NO
  artifact.
- The enhancements (§A–§D) SURFACE existing controls and RECORD settled decisions;
  they enforce nothing the Manager/CS do not already enforce, and decide nothing.
- Where the ledger and origin disagree, ORIGIN WINS — re-sync and supersede.
v0.2 is retained at governance/standing/PROGRAM-CONTROL-LEDGER-v0.2.md (superseded).
```

*PROGRAM-CONTROL-LEDGER-v0.3 (TL ACTION; model-free; supersedes v0.2, v0.2 retained; anchor refreshed to origin/main HEAD e6881f2): carries forward v0.2's dashboard + global closed-gates + 12 unchanged route records + the §A–§D enhancements (anchor-refreshed), and updates ONLY route record §8 (Tier 1 / G6) to record the FILED / CS-PASS G6 retrospective desk-audit RESULT (e6881f2, sha 4ce9b26d): R1 D4 saturation → REFUSAL-CONFIRMED, R2 CAL-Q → REFUSAL-CONFIRMED, R3 CAL-E → REFUSAL-REVERSED (bounded — CAL-E stays eliminated on the independent clean-ceiling ground; the reversal corrects the scoring record, not the non-certification); discrimination shown (CAL-Q genuine collapse vs CAL-E scoring artifact). MEANING preserved exactly: internal G6 consistency on design-target cases ONLY. CAVEAT preserved: does NOT validate G6 generally / certify a baseline / produce stress evidence / activate Paper B / reopen D4 / authorize any G6 software build or model execution. Next-state options recorded WITHOUT authorizing either: Option A (close as the first internal consistency exercise) · Option B (design a first non-design-target validation case — the only model-free step toward general validity). Appends decision line D-09 (audit SETTLED as the first consistency exercise; bounded meaning; A/B open). Trigger: §D #2 (CS PASS) + #5 (new HEAD). Reopens nothing; reinterprets no diagnosis; promotes no INT8; activates no Paper B; authorizes no execution/compression/G6-build; claims no general validity; changes no scientific meaning. COUPLED FOLLOW-ONS for CS: bump MAP.md ledger pointer v0.2→v0.3 (line 8 + line 147); and PROGRAM-POSITION-v0.1 small refresh — add "[done] G6 retrospective audit (internal consistency on design-target cases; not general validity)" to clear the recorded lag. Routes to CS for repo-state verification. model-free.*
