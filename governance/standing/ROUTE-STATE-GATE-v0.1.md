# ROUTE-STATE-GATE-v0.1

**Version:** v0.1. River and Canyon program. Phase-0 governance artifact (mini-map Stage C).
**Status:** model-free standing route-control rule. Defines the route-state declaration every future route memo must carry. Authorizes nothing itself; it constrains when execution may be authorized. Supersede by versioned replacement only.
Owner/drafter: Senior Engineer · CS: metadata / check hooks where possible · Team Lead: applies in routing · Manager: accepts; retains all execution authority.
Companion: NORTH-STAR-v1.1.md (the "when not to test" logic), PROGRAM-STAGE-MAP-v0.1.md (Phase 0).

## 1. Why this exists

The program executed a compression rung (INT8-RUNG-1) during a route-alignment pause — under route ambiguity — and had to quarantine the result. Semantic-read protects *artifact* validity; it does not protect *route* validity. This gate closes that gap: it makes the route's state an explicit, declared, checkable property of every route memo, so no run can happen while the route is ambiguous and have its status be discovered only afterward.

The rule, in one line:

```text
Every future route memo MUST declare a route state — GREEN / YELLOW / RED —
and no model-facing execution may proceed except under a declared GREEN.
```

## 2. The three states

### GREEN — execution may proceed (all conditions conjunctive)

```text
Execution of a model-facing step may proceed ONLY IF ALL hold:
  1. the Manager authorized THE NAMED STEP (not a general direction);
  2. the route map is RECONCILED (no Reading A/B/C ambiguity open — see the
     map-reconciliation artifact);
  3. artifact identities are FIXED (paths + commit SHAs + sha256 pinned, bytes
     verifiable from the shared remote on a clean fetch);
  4. semantic-read requirements are SATISFIED (nine-field shown-read with
     rendering floor, byte anchors, owner signature, disposition PASS for every
     load-bearing artifact);
  5. the action is NOT on the closed-gate list.
If any one of these is not true, the state is NOT GREEN.
```

GREEN is the only state under which a model touches anything. It is conjunctive by design: one missing condition drops the state.

### YELLOW — non-execution work may proceed

```text
Under YELLOW, the following MAY proceed:
  - design, specification, desk work;
  - verification, byte-recomputation, artifact-identity checks;
  - interpretation of existing results;
  - route and map reconciliation, governance drafting.
NO model-facing execution under YELLOW.
```

YELLOW is the program's normal working state for everything that is not a model run. Most Phase-0 and design work lives here.

### RED — nothing executes; hold

```text
The state is RED whenever ANY of these is present:
  - route ambiguity (the next step is not unambiguously authorized);
  - an active quarantine bearing on the step;
  - unresolved authorization (a prior local authorization without current
    route alignment — the exact INT8-RUNG-1 condition);
  - a map conflict (Reading A/B/C unresolved, or the active map superseded but
    not replaced);
  - missing bytes (a load-bearing artifact not verifiable from the shared remote);
  - an unresolved semantic-read (HOLD or UNCERTAIN on a load-bearing artifact);
  - a Manager pause.
Under RED: NO execution of any kind. Work that resolves the RED condition itself
(e.g. reconciling the map, fetching the missing bytes) may proceed and is the
path back to YELLOW/GREEN.
```

## 3. How the state is declared and used

```text
- Every route memo declares its state in a single line: ROUTE STATE: GREEN /
  YELLOW / RED, with the specific condition(s) that set it.
- A memo proposing model-facing execution MUST declare GREEN and enumerate how
  each of the five GREEN conditions is met. A GREEN declaration that does not
  enumerate the conditions is treated as YELLOW (incomplete).
- If conditions change mid-route (a quarantine opens, bytes go missing, the
  Manager pauses), the state DROPS to the most restrictive applicable state and
  any pending execution halts.
- The state is monotonic in restriction: when in doubt, the MORE restrictive
  state governs. Ambiguity resolves toward RED, not toward GREEN.
```

## 4. Relationship to the existing controls

```text
- It composes with semantic-read: semantic-read PASS is one of the five GREEN
  conditions (#4), not a substitute for the others. A clean semantic-read does
  NOT make the state GREEN by itself.
- It composes with the closed-gate list: an action on the closed-gate list is
  never GREEN regardless of the other four conditions (#5).
- It composes with the EXIT rule (North Star §9): F EMPTY (saturation) makes a
  retention measurement uninterpretable, which is a "not meaningful" condition —
  the run may be route-GREEN-eligible yet still should not run because the
  question is not ready. Route state governs PERMISSION; the EXIT rule governs
  MEANING. Both must clear.
```

## 5. Current program route state (as of this filing)

```text
ROUTE STATE: RED.
Setting conditions:
  - map conflict: the 2026-06-10 project map is in unresolved Reading A/B/C
    tension with the Lane-1a′ work (map reconciliation not yet accepted);
  - active quarantine: INT8-RUNG-1 quarantined pending governance reconciliation.
Consequence: no model-facing execution. The path back to YELLOW is completing
the map reconciliation (mini-map Stage D) and the route-state/quarantine closure;
the path to GREEN additionally requires a certified baseline and a Manager-
authorized named step — neither of which exists yet.
```

## 6. Done-when (Stage C completion)

```text
This gate is "filed" when:
  - it is byte-verifiable from the shared remote (CS commits + push-verifies);
  - the rule "every future route memo declares GREEN / YELLOW / RED" is adopted;
  - CS adds metadata/check hooks where possible (e.g. a required route-state
    field in route-memo templates).
```

## 7. No-authorization footer / closed gates

This route-state gate authorizes no execution. It is a control rule, not a permission. Closed throughout: no model-facing execution · no INT4 · no second compression rung · no full ladder · no Path B execution · no Path D execution · no schedule v2 supersession · no candidate certification · no ranking · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission. The gate's GREEN state is necessary but not sufficient for any execution — a Manager authorization of the named step is still required.

— Senior Engineer
