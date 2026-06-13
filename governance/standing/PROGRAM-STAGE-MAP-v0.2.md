# PROGRAM STAGE MAP — From North Star To Practical Phases

**Version:** v0.2. River and Canyon program. Strategy / planning artifact.
**Status:** model-free planning document. Breaks the North Star into practical phases and milestones so the team does not lose the plan again. Authorizes no execution. **Revision note (v0.2):** updated to reflect the Manager's Reading C decision (PROGRAM-MAP-RECONCILIATION-v0.1) and to elevate Baseline Gate Diagnosis to the route hinge that gates Phase-1 readiness and any official compression route. Now governed by PROGRAM-MAP-v2.0. v0.1 retained, superseded. Companion to NORTH-STAR-v1.1.md; the North Star records the standard, this records the staged path to meeting it.

---

## 0. Purpose and how this relates to the North Star

The North Star answers "what must be true for this to be a real measurement tool?" This map answers "in what order do we make those things true, and how do we know when each is done?" It is phase-structured, not a task list of runs — each phase is defined by what becomes *true and enforced*, not by what gets executed.

Two rules carry over from the North Star and govern every phase here:

```text
- Ladder progression condition: no phase advance is authorized unless the prior
  phase's invariants are not merely DOCUMENTED but OPERATIONALLY ENFORCED in the
  mainline system.
- Claim/tier discipline: a phase may support only the claims and service tiers
  its evidence earns. No phase promises Tier 2 stress-retention measurement
  until an official, non-quarantined, certified-baseline compression rung exists.
```

---

## 1. The phases

### Phase 0 — Governance repair + baseline discipline

```text
Focus:
  semantic-read template (active, nine-field, rendering floor)
  route-state gate (unambiguous authorization before execution)
  quarantine handling (nonconforming runs labeled, not promoted)
  map reconciliation (the 2026-06-10 project map vs the 1a′ detour)
  no ambiguous-gate execution
Done when:
  North Star v1.1 accepted
  Program Stage Map accepted
  semantic-read template filed
  route-state rule filed
  INT8 quarantine complete
  CS verification complete
North Star ladder level: foundational (precondition to L-anything)
Grant relevance: foundational · near-term · high credibility
```

This phase is the direct response to the two route-discipline failures (Path A schedule mismatch; INT8-RUNG-1 under route ambiguity). It does not add measurement capability; it makes the existing capability *trustworthy and repeatable* by closing the route-level ambiguity that semantic-read alone does not cover.

### Phase 1 — Strengthen the ruler in one domain

```text
Focus:
  move from one planted defect class to MULTIPLE defect classes
  matched clean controls (spared, demonstrably)
  reproducible reports
  no quarantined-result dependence
  baseline gate diagnosis (see §1a)
Done when:
  L1 is achieved across multiple defect types in the current task family
  clean controls are spared
  reports are reproducible
  baseline gate failures are diagnosed as one of: valid rejections of bad
    constructs / fixable design-or-calibration problems / structural limits
  no official claim depends on the quarantined INT8 datum
North Star ladder level: L1 → L2
Grant relevance: strong candidate for near-term proposal
```

This is where the instrument stops being "fired once in one class" and becomes "fires across a defect taxonomy, in one domain, reproducibly." It deliberately stays inside the current task family — depth before breadth.

### 1a. Workstream — Baseline Gate Diagnosis (critical unknown, runs within Phase 1)

```text
Purpose: determine whether the program's repeated baseline-gate failures are
  - VALID REJECTIONS of bad constructs (good metrology — the gate working), or
  - FIXABLE design/calibration problems (the construct can be repaired), or
  - STRUCTURAL LIMITS (the ladder is harder / narrower than hoped).
```

This is a critical unknown, not a side note. The program's defining pattern to
date is that *every purpose-built construction failed its FP16 baseline gate.*
Two readings of that fact have very different consequences:

```text
- If the gate correctly rejects bad constructions, that is good metrology and
  the instrument is doing its job — Phase 1 proceeds by building constructs that
  pass.
- If the gate rejects almost everything usable, the UPPER LADDER (L2–L7) may be
  unreachable in practice, and the program's realistic ceiling is the
  methodology + validity-auditing layer, not the full predictive tool.
```

Baseline Gate Diagnosis is therefore a go/no-go input to the whole upper ladder,
and must be resolved within Phase 1 before Phase 2 (portability) is justified.
Under the Manager's Reading C decision (Program Map v2.0), it is elevated to the
ROUTE HINGE: it gates Phase-1 readiness AND any official compression route. If a
certifiable baseline is not reachable, the certification track and Lane 4 cannot
proceed, and the program's realistic value is the methodology + eval-validity
layer (Layer 1 / Tier 1).
It is itself model-free where possible (diagnosing WHY constructs fail from the
existing gate logic and the constructed-positive arc), escalating to authorized
runs only under separate Manager decision.

### Phase 2 — Portability

```text
Focus:
  same gate STRUCTURE across a second model family
  thresholds RE-JUSTIFIED (not assumed to transfer)
  no assumption that values port
North Star ladder level: L3
Grant relevance: extension / stretch aim only
```

Portability tests the claim that the gate structure is general while thresholds are local. Do not enter until Phase 1's invariants are enforced — scaling a not-yet-locked ruler buys faster confusion.

### Phase 3 — External usability

```text
Focus:
  third-party-readable report (the §7 schema, filled honestly)
  decision-useful output
  reproducible artifact bundle
North Star ladder level: L6
Grant relevance: long-term direction
```

### Phase 4 — Predictive / qualification value

```text
Focus:
  whether stress-retention readings predict deployment reliability
  better than ordinary benchmarks
North Star ladder level: L7
Grant relevance: long-term direction (the forward edge)
```

---

## 1b. Strategic layer split (read before funding or planning any of it)

The program is three layers stacked, and they must NOT be funded or promised as
one near-term deliverable. Each has a different maturity, value, and risk:

```text
LAYER 1 — Methodology layer.
  Papers 1–3, semantic-read, fail-closed rules, hash ≠ construct validity.
  STATUS: strongest, mostly BANKED. Real but modest if it remains only papers.
LAYER 2 — Tool layer (ladder L2–L6).
  A usable ruler: multiple defect classes, reproducible reports, portability,
  bounded automation.
  STATUS: highest PRACTICAL external value; partially begun (L1 in one class).
LAYER 3 — Predictive / qualification layer (ladder L7).
  Stress-retention predicts deployment reliability better than standard
  benchmarks.
  STATUS: biggest prize, furthest out, highest risk.
```

```text
STRATEGIC WARNING: Do NOT fund or plan all three as one near-term promise.
Layer 1 is bankable now; Layer 2 is the near-term build; Layer 3 is a long-term
bet contingent on the Baseline Gate Diagnosis (§1a) coming out favorably.
Conflating them is how a credible methodology program turns into an overclaim.
```

## 1c. Measurement Proof-of-Life and Kill Criteria

**The concern this section answers, stated plainly:** the control apparatus is
now more developed than the measurement apparatus. That does not mean the project
is wrong — the governance was built in response to real failures (Path A, the
INT8 routing ambiguity) and it works. But the next stretch must prove that
**governance enables measurement rather than replacing it.**

```text
CORE PRINCIPLE:
The project must demonstrate that its gates help valid measurement happen.
A gate system that only produces more gates is not sufficient.
Governance must be accountable to measurement.
```

This is not a weakening of governance. It is making governance answer to the
thing it exists to serve.

### The eight questions

```text
1. What real measurement would prove the apparatus can function?
   A CONFORMING certified-baseline compression rung (or equivalent conforming
   measurement): a run on a baseline that passed certification as a structure,
   executed under unambiguous route authorization, with the instrument
   eliminating planted defects and sparing matched clean controls — and the
   whole thing byte-verifiable and reproducible. That is the apparatus
   functioning end to end, not in pieces.
2. What is the shortest CONFORMING path to that measurement?
   Phase 0 closure (route-state rule + map reconciliation) → a certified
   baseline (the certification track the map places before any Lane-4 rung) →
   one conforming rung on it. No step skipped; the shortest path is still the
   ordered one, because an unordered shortcut produces another quarantine.
3. What blocks it today?
   - Phase 0 is not closed: the route-state rule and the map reconciliation
     (Reading A vs B on the 2026-06-10 project map) are open.
   - No certified baseline exists: every purpose-built construction has so far
     failed its FP16 baseline gate (the Baseline Gate Diagnosis unknown, §1a).
   - The only compression rung run to date is QUARANTINED (INT8-RUNG-1).
4. Which blockers can be resolved in the next 2–3 weeks?
   - Route-state rule: yes — it is model-free governance drafting.
   - Map reconciliation: yes — a Manager decision + a superseding map.
   - A certified baseline: UNKNOWN, and this is the crux — it depends on the
     Baseline Gate Diagnosis (§1a). If constructs can be calibrated to pass the
     gate, yes; if the gate is structurally rejecting everything usable, no.
   The honest 2–3-week deliverable is therefore EITHER a conforming measurement
   (if the baseline gate proves solvable) OR a precise blocker memo (if it does
   not) — see the bounded test below.
5. What counts as SUCCESS?  (see Continue, below)
6. What counts as PAUSE?    (see Pause, below)
7. What counts as PIVOT?    (see Pivot, below)
8. What counts as KILL / rescope?  (see Kill, below)
```

### The bounded proof-of-life test

```text
Within a short, bounded window, the program must produce ONE of:

A. A CONFORMING certified-baseline rung (or equivalent conforming measurement),
   IF all prerequisites are actually ready; OR

B. A PRECISE BLOCKER MEMO showing exactly why such a conforming measurement is
   not yet possible, what must change, and whether the blocker is solvable.

Outcome B counts as progress ONLY if it NARROWS the blocker — names the specific
prerequisite, the specific reason, and a solvable/unsolvable determination. A
generic "more governance needed" answer does NOT count and is itself a warning
sign that the program is becoming the gate-that-guards-an-empty-room.
```

The asymmetry is deliberate: outcome A is the apparatus working; outcome B is
acceptable only as a *sharpened* understanding of why it cannot yet work. Either
advances; neither is "produce more governance."

### Continue / Pause / Pivot / Kill

```text
CONTINUE if:
  - governance removes a NAMED blocker (not a vague "tightening");
  - the stage produces a reusable TOOL component (not only a rule);
  - the next measurement becomes more CONCRETE, not more abstract;
  - the project moves up the North Star ladder OR hardens a named ladder
    prerequisite into operational enforcement.
```

```text
PAUSE if:
  - route state is ambiguous;
  - artifact visibility is not shared across seats (the "filed but invisible" gap);
  - semantic-read or route-state checks are incomplete;
  - a proposed run is possible but not yet MEANINGFUL (infrastructure-ready is
    not question-ready).
```

```text
PIVOT if:
  - the same blocker recurs repeatedly WITHOUT becoming easier to resolve;
  - baseline gates reject nearly all usable candidates (a §1a "structural" finding);
  - the project can produce governance artifacts but not conforming measurements;
  - the practical value is clearer as an EVAL-VALIDITY AUDIT tool (Tier 1 /
    methodology layer) than as a stress-retention tool (Tier 2 / tool layer).
  A pivot here is not failure — it is recognizing the program's real product is
  Layer 1 + Tier 1, which is genuinely valuable and defensible today.
```

```text
KILL / radically rescope if, after a bounded period:
  - the program produces ONLY governance artifacts and no conforming
    measurement, no reusable tool component, and no sharply narrowed blocker;
  - the measurement ladder cannot advance beyond the one constructed-positive
    condition class already achieved;
  - baseline gate failures appear STRUCTURAL rather than diagnosable or fixable;
  - the tool cannot be made efficient enough to test across models without
    manual governance overload.
```

This is disciplined project management, not defeatism. A program that cannot
state its own kill criteria cannot be trusted to stop when it should — and a
measurement program that never stops to check whether it still measures anything
is exactly the failure mode this section exists to prevent. The kill criteria are
the proof that the program is honest about its own value.

### What this section commits the program to

```text
The next reporting period is judged not by "how much governance was produced"
but by which of the bounded-test outcomes (A or B) was reached, and whether the
Continue conditions held. Governance that removes a named blocker continues;
governance that only produces more governance triggers Pause, Pivot, or — at the
bound — Kill/rescope.
```

## 2. Program stage map (table)

| Phase | Goal | NS ladder | Deliverables | Success criteria | Difficulty | Risk | Grant relevance | What remains gated |
|---|---|---|---|---|---|---|---|---|
| **0** | Governance repair + baseline discipline | foundational | North Star v1.1; Stage Map; semantic-read template; route-state rule; INT8 quarantine suite; map reconciliation | All filed + CS-verified; no ambiguous-gate execution possible; route-state gate active | Low–moderate (process, not science) | Low; main risk is treating it as "done on paper" vs enforced | Foundational · near-term · high credibility | All model-facing execution; INT4; second rung; certification; Claim C |
| **1** | Strengthen the ruler in one domain | L1 → L2 | Multi-defect-class constructed positives; matched clean controls; reproducible report instances | Multiple defect types caught; clean spared; reports reproducible; no quarantined-datum dependence | Moderate | Over-eliminating clean controls; defect classes that smuggle a second difference | Strong candidate for near-term proposal | Cross-model work; thresholds-as-general; stress on uncertified baselines |
| **2** | Portability | L3 | Second-model-family runs under the same gate structure; re-justified threshold sheets | Structure ports; thresholds independently justified per model; no value-transfer assumption | High | Assuming thresholds transfer; confusing structure-portability with value-portability | Extension / stretch aim | INT4 ladder; certification claims across models; any general-robustness claim |
| **3** | External usability | L6 | Third-party-readable report; reproducible artifact bundle | A non-author reproduces a result and acts on the report | High | Report that looks decision-useful but hides validity caveats | Long-term direction | Qualification/predictive claims; Tier 3 |
| **4** | Predictive / qualification value | L7 | Evidence on whether retention predicts deployment reliability vs aggregate benchmarks | A defensible predictive comparison, claim-scoped | Highest | The hardest claim to make honestly; easiest to overclaim | Long-term direction (forward edge) | Everything not yet earned; the strongest claims the program could ever make |

---

## 3. Grant-scope recommendation

```text
For a near-term grant, propose PHASE 0 + PHASE 1.
At most include PHASE 2 as an extension or stretch aim.
Reference PHASES 3–4 as long-term direction only.
Do NOT promise Tier 2 stress-retention measurement until an official
certified-baseline compression rung exists in the non-quarantined sequence.
Do NOT promise L7 predictive value in a near-term grant unless resourcing,
timeline, AND baseline-gate solvability (§1a) are explicitly addressed.
```

The fundable near-term story is honest and strong on its own terms: *we built a validity instrument for behavioral evals, demonstrated it fires on planted defects and spares clean controls, and are hardening it across a defect taxonomy with the route/artifact discipline that prevents false confidence.* That is Phase 0 + Phase 1, and it does not require a single overclaim.

---

## 4. How recent failures become design lessons (the honest framing)

```text
We discovered route-control and artifact-validity weaknesses.
We quarantined nonconforming evidence instead of laundering it.
We are building those lessons into the measurement system.
```

Concretely, each failure became a Phase-0 invariant:

```text
- Path A schedule mismatch        → the semantic-read gate (artifact validity,
                                      nine-field, rendering floor).
- INT8-RUNG-1 under route ambiguity → the route-state gate (unambiguous
                                      authorization before execution) + the
                                      quarantine-handling rule.
- "filed but not visible" gaps      → filed-means-bytes-verify-from-the-shared-
                                      remote, enforced at read time (fetch-first).
```

These are not embarrassments to manage; they are the reason the tool's refusals can be trusted. A measurement system that has never caught itself is one that has never been stressed.

---

## 5. Where the program is on this map, right now

```text
Phase 0: IN PROGRESS. North Star v1.1 and this Stage Map are drafted (pending
  acceptance + CS verification). Semantic-read template filed. INT8 quarantine
  suite filed and byte-matched. Route-state rule and map reconciliation REMAIN
  the open Phase-0 items — the map reconciliation (Reading A vs B for the
  2026-06-10 project map) is the specific unresolved decision blocking Phase-0
  completion.
Phases 1–4: NOT STARTED. Correctly gated behind Phase 0.
Honest status: pre-stress in the official sequence; the instrument is the
  contribution to date; happy but not satisfied.
Reading C accepted (Manager): Lane 1a′ is an accepted instrument-development
  detour; INT8-RUNG-1 stays quarantined and non-driving; the certification track
  remains required; Baseline Gate Diagnosis is the hinge. Program Map v2.0 is the
  map of record (superseding 2026-06-10). The map-reconciliation Phase-0 item is
  thus CLOSED; the route-state rule is filed (Stage C). Remaining Phase-0 / next:
  Baseline Gate Diagnosis (Stage E).
Proof-of-life standing (per §1c): the program is at the point where the bounded
  test applies — the next deliverable must be EITHER a conforming measurement
  (if the baseline gate proves solvable once Phase 0 closes) OR a precise,
  narrowed blocker memo. "More governance" is no longer a sufficient output. The
  control apparatus is ahead of the measurement apparatus, and the next stretch
  must close that gap or sharply explain why it cannot.
```

---

## Boundary

This map authorizes no execution. Closed: no model-facing execution · no INT4 · no second compression rung · no full ladder · no Path B execution · no Path D execution · no schedule v2 supersession · no candidate certification · no ranking · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission. It is a planning artifact; phase advances require the prior phase's invariants operationally enforced and separate Manager authorization.

— Senior Engineer
