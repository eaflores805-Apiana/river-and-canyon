# PROGRAM-POSITION-v0.1 — YOU ARE HERE

**Version:** v0.1. River and Canyon program. The single live position tracker.
**Status:** the one document that answers "where are we right now?" Updated when a stage closes; kept byte-true to the record (anchor: origin/main 6a4e604). If this and the record disagree, the record wins and this is stale — re-sync.
Maintained by Senior; verified by CS.

---

## ▶ RIGHT NOW

```text
MAIN MAP:   Program Map v2.0  →  node: "Baseline Gate Diagnosis (the hinge)"
SUBMAP:     Phase-0 → Phase-1 readiness mini-map
ON STAGE:   F — Phase-1 readiness decision   ← THE LIVE STEP
WAITING ON: Manager (ACCEPT / RETURN / PIVOT)
ROUTE STATE: YELLOW (model-free work proceeds) · RED (no model execution)
```

**In one sentence:** every model-free stage up to the baseline diagnosis is done; we are waiting on the Manager's Phase-1 readiness decision, which is the gate that would authorize the off-ceiling repair design.

---

## The main map (Program Map v2.0) — which node we're at

```text
[done]  Foundation / earned (Papers 1–3, Hash Integrity note, North Star,
        Stage Map, Route-State Gate, quarantine discipline)
[done]  Lane 1a′ accepted as instrument-development detour (INT8-RUNG-1 quarantined)
[HERE]  Baseline Gate Diagnosis — the hinge   ◀── current main-map node
[next]  Certification track (Lanes 1–3)  — only if the hinge says "reachable"
[gated] Lane 4 — official compression on a certified baseline
[horizon] portability · external usability · predictive/qualification · Claim C
```

---

## The live submap — the Phase-0→Phase-1 mini-map, as a checklist

```text
A  Strategy docs verification     PASS
B  INT8 quarantine package        HOLD   (filed + byte-matched; Manager acceptance tracking open)
C  Route-state gate               PASS
D  Map reconciliation             PASS   (Reading C; Program Map v2.0 is map of record)
E  Baseline Gate Diagnosis        PASS   (FIXABLE + one narrow structural risk)
F  Phase-1 readiness decision     LIVE   ◀── we are here; Manager decision
```

```text
What closes this submap: F resolves to ACCEPT / RETURN / PIVOT.
  ACCEPT → opens the next submap (certification-readiness / repair design)
  RETURN → names a blocker to fix, stay in this submap
  PIVOT  → redirect to Tier 1 eval-validity auditing
What it returns to the main map: a decided route at the BGD hinge.
```

---

## What the last closed stage (E) handed us

```text
The baseline gate failures split into two mechanisms:
  - D4 = SATURATION (too easy; passed t3 but no measurement headroom) — FIXABLE
  - Lane-1a sweep = ELIMINATION (shortcut-prone; gate correctly caught) — VALID
The constructed-positive passed validation by being off-ceiling = existence proof.
Diagnosis: FIXABLE + valid-rejection, with ONE narrow structural risk untested —
  is the off-ceiling window (floor 0.6125+margin < a < 1.0−δ) wide enough to certify?
Recommended next: a model-free off-ceiling repair design (shortest path to a
  certified baseline AND the test of that structural question) — GATED on F.
```

---

## The next submap (opens only if F = ACCEPT) — pre-charter

```text
SUBMAP: Certification-readiness / off-ceiling repair design
  Parent node:    Program Map v2.0 → Certification track (Lanes 1–3)
  Why:            build a certifiable off-ceiling baseline + test the structural-window question
  Exit condition: (A) a repair design that places a construct in the window and
                      passes the 12-section checklist → certification-run request
                      becomes well-formed; OR
                  (B) the window proves too narrow → PIVOT to Tier 1; OR
                  (C) no construct placeable + no second family → STOP
  Rough plan:     repair design → checklist PASS → (gated) certification-run request
  Touch / closed: model-free design only; no execution / INT4 / rung / certification run
```

This charter is written but NOT OPEN — it opens the moment the Manager accepts Stage F. (Convention: SUBMAP-CONVENTION-v1.0. Checklist form: REPAIR-DESIGN-CHECKLIST-INSTRUMENT-v0.1.)

---

## How to read this document

```text
- ▶ RIGHT NOW is the answer to "what step are we on." Start there.
- The two checklists below it show the main-map node and the submap stage.
- When a stage closes, update its status here FIRST, then everything else.
- If this disagrees with the record (origin/main), the record wins — re-sync.
```

— Senior Engineer
