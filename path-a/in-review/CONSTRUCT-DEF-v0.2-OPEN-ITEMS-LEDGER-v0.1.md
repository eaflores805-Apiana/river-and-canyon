# CONSTRUCT-DEFINITION v0.2 — OPEN-ITEMS LEDGER (issuance v0.1)

**E. A. Flores**, Apiana AI, Inc. — June 15, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. Review-tracking object.*

> **Naming.** "v0.2" refers to the next version of `TARGET-CONSTRUCT-DEFINITION` (the construct-definition document). "Ledger issuance v0.1" is the first cut of *this* tracking object. There is no separate "ledger v0.2."
>
> **What this is.** A by-ID enumeration of every open review item owed to the construct definition's v0.2 consolidation, with source, severity, and disposition. **It enumerates the edits; it does not make them.** The consolidation is a single pass, held for the feasibility verdict (see §2).
>
> **What this is not / negative-use.** Not v0.2 (the edits are not applied). Not a claim, not evidence, not a certification. Certifies nothing, authorizes nothing. The Claim Ledger has **not** advanced — no run has produced data; Claim C remains blocked behind the certified-constructible baseline this gate defines.

---

## 0. Binding references

- **Object under revision:** `TARGET-CONSTRUCT-DEFINITION-v0.1.md`, SE-computed digest `a33ea5640ccfc09f2b8ba480beb76c734614a7286d764bc8881b3bab1247c0bf` (CS to confirm at bind).
- **Reviews consolidated here (5):** Contributor 4 (assessment); Senior Engineer (pass 1 — six items); Senior Engineer (pass 2 — three holes + three tightenings); Contributor 5 (claim-risk — F1–F3 + N1–N2); CS Engineer (implementation/scoring — five items + closing).
- **Status of reviews:** closed. No further review input is required; adding a sixth pass would be over-production. The failure modes are found, not open.

## 1. Severity key

- **MUST-FIX** — soundness or integrity defect; blocks elevation of the object to definition-of-record.
- **ADDITION** — new clause or structural section; high priority, not a soundness block.
- **TIGHTENING** — clarity/consistency; fold in but non-blocking.
- **SCOPE-HELD** — correctly raised, but its fix is construction/feasibility design and must **not** be folded into the gate object.

## 2. The dependency gate (why consolidation is held)

Every reviewer converged independently on one structural question, now in its sharpest form:

> **Does a closed-world two-hop construction exist that yields C\* *only* by traversal — not terminal-grab (R8), not direct A→C\* recall (OI-1), not interior-position salience (OI-5), not control-induced recency (OI-6) — with a *derivable* non-trivial success threshold (OI-3), while remaining a genuine two-hop task?**

This is not a clause; it is the gate the gate rests on. The feasibility verdict **reshapes** v0.2, it does not merely add to it:

- **Feasible →** v0.2 hardens into a buildable gate; the items below tighten it.
- **Infeasible →** v0.2's headline becomes the **substrate-infeasibility finding** (OI-4): the gate is honest, complete, and unbuildable — itself a first-class result, reached before any item is written.

Therefore the consolidation runs **after** feasibility reports, in a single pass. Routing to the decision layer comes after that, carrying all five reviews **and** the feasibility verdict — not the definition alone.

## 3. Open items (enumerated by ID)

### MUST-FIX

- **OI-1 · R6(c) refactor — direct-shortcut: split into admissibility property + a per-item direct-query control.**
  Source: C5 F1 (unsound as a §9 checklist property — "C\* associable with A" is a property of the *model*, not visible in item layout) + CS-1 (mis-placed in §3 per-item scoring). Fix: (a) construction property → §4/§9 (items built so C\* is not directly associable with A); (b) a **pre-declared per-item direct-query control**, parallel to R7 — query A→C\* with the bridge withheld and confirm the model *cannot* produce C\* that way — in the R11 block and the §9 checklist as a reportable control. Without it, "R1 = behavior consistent with composition" is unsound: direct recall yields C\*, passes R8 (C\* is not a terminal), passes the R7 controls, and lands in R1.

- **OI-2 · R11 failure signatures — add the cross-query constant-token disqualifier.**
  Source: CS-2. Fix: if the response token is constant across hop1 / hop2 / composite for the same item, that **invalidates R1** on that item. Per-query scoring otherwise *dismembers* the i06 pattern (one token answering every query reads as partial composition — R2 on hop1, R1 on hop2, R1 on composite). Re-imports G6's Rule B, which the multiclass scorer otherwise loses.

- **OI-3 · R11 success threshold — derive it, don't declare it freely.**
  Source: CS-3 (pairs with C5 F3). Fix: the success threshold is "R1 rate > terminal-grab chance floor + pre-declared margin," where the chance floor is a function of R8 + R11.k (number of terminals / clutter). A freely-declared number lets a pre-registration set a bar not pinned to the actual heuristic floor — a route to manufacturing a pass by lowering the bar.

### ADDITION

- **OI-4 · NEW clause — pre-commit substrate-infeasibility as a first-class result.**
  Source: C5 F3. Fix: the object must pre-commit that *admissible-but-failing-to-certify across constructions* is itself a finding (substrate infeasibility), **not** a license to loosen R8 / R6(c) / the threshold. Per program doctrine, a gate that never opens on linkage is observationally identical to a miscalibrated one until one construction clears it — so the integrity guard is to pre-commit that the gate may correctly never open. Highest-priority non-clause addition.

- **OI-5 · R6(f) NEW — interior-position coincidence exclusion.**
  Source: Senior pass 2, hole 1. Fix: moving C\* off the terminal to satisfy R8.1 places C\* at an interior slot; if that slot is independently salient, an interior-position heuristic yields C\* without traversal. Add an exclusion tied to the slot C\* occupies once moved off the terminal. Same non-terminal-route family as OI-1.

- **OI-6 · R7 rewrite — isolation + load-matching + token logging (three sub-parts).**
  Sources: C5 F2 (isolation), Senior pass 2 hole 3 (clutter-matching), Senior pass 2 hole 2 (logging). Fix: (a) **control/composite isolation** — controls must not surface C\* as a recent token to the composite (separate contexts, or counterbalanced order logged, or composite-first with controls as post-hoc checks on a frozen response); (b) **clutter-matching** — controls run under the *same* clutter regime as the composite, not in an easier lone-chain condition; (c) **per-item token-level logging** — retain the response token and category per item in a form supporting same-error-identity comparison at a future compression rung. Note: (a) and (b) may pull against each other in realization — that is feasibility's problem; the object states both properties.

- **OI-7 · R8.1 ↔ R6(a) — name the consequence of overlap.**
  Source: CS-4. Fix: R8.1 (admissibility) and R6(a) (per-item invalidation) overlap; belt-and-suspenders is fine, but if R6(a) ever fires it means the construction silently breached R8.1 at admissibility — so the gate must **reject the whole construction, not just the item.**

- **OI-8 · §9 — rejected-construction disposition.**
  Source: CS-5 (ties to OI-10). Fix: §9 is currently binary (admissible / not) and silent on what happens to a *rejected* construction. Name the declared disposition (archive / iterate / abandon) and who decides, under role-separation.

### TIGHTENING

- **OI-9 · R6 closing rule — give the validity/capability asymmetry a positive shape.**
  Sources: CS closing + C4-2. Fix: name what a capability claim *would* require (mechanistic intervention; cross-construction generalization) so the ceiling is load-bearing, not apologetic; add "never a claim about internal process." Guards against the drift where "couldn't witness it behaviorally" becomes "so call it capability."

- **OI-10 · R6 — name the evaluator.**
  Source: Senior pass 2, tightening 6. Fix: R6 exclusions must be mechanically computable from logged fields where possible (token identity, position, control pass/fail); any judgment-based exclusion flagged as such and adjudicated under role-separation. An unread rule passes every check not pointed at it.

- **OI-11 · R11 — *other*-rate ceiling.**
  Source: Senior pass 2, tightening 4. Fix: pre-declare an *other*-rate ceiling above which the construction is deemed mis-specified (value set at construction time; existence required now). A "signal" with no declared trigger is wording-class.

- **OI-12 · §2 / §9 — abstention consistency.**
  Sources: CS N2 + Senior pass 2 tightening 5. Fix: align R5's §2 framing (reads neutral) with R11's failure-signature treatment (R5-dominant → composition-failure on an answerable composite); confirm §9 treats an abstention-dominated construction as failing-to-elicit, not "clean because no wrong commitments."

- **OI-13 · N1 — delineate R6(c) / R6(d) / R11.**
  Source: C5 N1. Fix: state the relationship explicitly — R6(c) = associable-with-A (a different shortcut); R6(d) = salient-regardless-of-path (construction property); R11 = the quantitative heuristic floor R1 must beat. Largely absorbed by OI-1 + OI-3; keep for clarity.

- **OI-14 · R3 — sharpen to error-with-diagnosis.**
  Source: C4-1. Fix: R3 (stopped-short) reads unambiguously as an *error* with diagnostic value (hop2-in-composition failure), never partial credit. Partial credit would smuggle a graded metric back in.

- **OI-15 · R11 — G6-scorability cross-reference.**
  Source: C4-3 (reinforced by OI-2). Fix: any run under this definition must be scorable by the G6 evaluator (or its successor). The two objects are complementary — this defines the admissible construct; G6 operationalizes the gate.

### SCOPE-HELD (do NOT fold into the object)

- **OI-16 · R8.3 operationalization — deferred to feasibility/design.**
  Source: C4-4. Concrete token-space guidance for keeping R3/R5 distinguishable is construction design. R8.3 states the property; its realization belongs to feasibility/design, not the gate object. Folding it in would tip the gate into the task design it is meant to precede.

## 4. Do-not-drift (endorsed as-is; consolidation must preserve)

Every reviewer confirmed these are correct; the consolidation must **not** weaken them while folding in the above:

- **R8** (terminal ≠ answer) as the load-bearing, inadmissible-by-inspection property, realization deferred.
- **R6 closing rule** — R1 is the best-supported interpretation, not proof; a validity statement, never a capability statement. (OI-9 *strengthens* this; it must not dilute it.)
- **R9 / R10** — multiclass scorer primary, binary accuracy non-gating (the metric prior baselines passed under by coincidence).
- **R12.2** — a fall in terminal-grab is not composition; certification requires R1 to *rise*, not R2 to *fall*.
- **Three-outcome lock** — certify / inconclusive / fail with a pre-declared inconclusive band; fail-closed.

## 5. Status and seat

- Reviews: **closed** (C4, Senior ×2, C5, CS). Nothing to add.
- v0.2 consolidation: **owed**, single pass, Senior Engineer to run. **Held for the feasibility verdict** (§2), which reshapes the output.
- Routing to decision layer: **after** feasibility, carrying all five reviews + the feasibility verdict. Elevation to definition-of-record is the Manager's / Team Lead's call, not the Senior Engineer's.
- Seat: the Senior Engineer drafted v0.1 (OI-1 and OI-2 are logged as drafter's errors — a soundness hole and a scoring hole), holds this ledger, and runs the consolidation. The Senior Engineer does not declare v0.2 of-record and does not route it upward.

*Issuance v0.1. Enumerates 16 open items + 5 do-not-drift invariants across 5 reviews. Performs no edits; certifies nothing; authorizes nothing.*
