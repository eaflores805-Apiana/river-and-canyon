# PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.3

**E. A. Flores**, Apiana AI, Inc. — June 15, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. Construction-design object (property level).*

## 0. Scope / negative-use

Carry-forward of design v0.2 (`0e728d82…`) folding C5 required edits **E7/E8** after **PASS_WITH_REQUIRED_EDITS** (depth-selection closure accepted; the v0.1 HOLD and depth-selection axis are resolved and closed). Under `TARGET-CONSTRUCT-DEFINITION-v0.2` (`f4462f2b…`). Property/schema level only. A full v0.3 (not a side patch) because E8 adds a **binding admissibility property** that must live in the construction's admissibility and rejection surface in one place.

**Not in this object:** task items, concrete tokens, prompt templates, pre-registration, run request, compression rung, Claim C / Paper B language, capability or mechanism claims. Entities are placeholders; quantities are parameters (k, p, m, **D**), not values (§10).

**Negative-use.** A candidate design, not a built construction, not a certified baseline, not evidence. It is **not admissible** until CS feasibility and C5 claim-risk clear it. v0.1 was correct that it could not self-certify the residual channel; C5's HOLD confirmed the channel is real (depth-selection), and v0.2 exists to close it.

## 1. Construction idea in one paragraph

Keep the v0.1 interior-target move — `A —r1→ B —r2→ C* —(further edges)→ … → T`, so C\* is the two-hop target and T (the sink) is a non-C\* salient terminal — and **add same-depth competitors at the head** so that *structural depth alone cannot single out C\**. The head A fans out via **distinct relations** to several depth-1 nodes, each continuing to a distinct depth-2 node, so that **D nodes sit at structural depth 2 from A** and only following the *specific* relation path `r1 then r2` selects C\* among them. A depth-counting heuristic ("walk two edges from A") now lands on a *set* of D nodes and scores only 1/D; a layout-position heuristic still scores only 1/p (positions varied); a token-salience heuristic still scores only 1/m. The queried composition stays strictly two relation-typed hops — `r1(A)=B` is unique (A has exactly one r1-edge), `r2(B)=C*` is unique — so genuine two-hop structure is preserved; the competitors are off the r1→r2 path and a correct relation-following traversal rejects them by relation type, which is precisely the discrimination depth-selection cannot do.

## 2. Entity / layout schema

- **Target two-hop path:** `A —r1→ B —r2→ C* —rX→ … → T`. C\* interior (depth 2); T the target sink/terminal. The r1-edge from A is **unique** (so r1(A)=B is well-posed).
- **Same-depth competitor paths (the depth-selection control, E1):** A also emits edges via **other relations** `A —s1→ B2 —s2→ X2`, `A —t1→ B3 —t2→ X3`, … so that {C\*, X2, X3, …} all sit at **depth 2** from A (D total). The competitor relations {s·, t·, …} are **disjoint from {r1, r2}**, so they are off the queried path. Competitor depth-2 nodes (X·) are themselves **interior** (their paths continue), so the only **terminals** in the layout remain {T, decoy sinks T_i} — competitors do not occupy terminal slots.
- **Relation-balancing across competitors (E8 — binding admissibility property):** relation **frequency, order, and position** must be balanced across the target and competitor paths, so that **r1/r2 cannot be selected by salience alone**. No relation on the queried path may be made more frequent, earlier-ordered, or more positionally prominent than the competitor relations. This is what bounds the relation-identity route (route 4, §8) at the structural-depth floor 1/D rather than letting a relation-salience signal break the floor.
- **Decoy chains (chain-level clutter, k of them):** competing full chains with different heads; sinks T_i are decoy terminals. (Carried from v0.1.)
- **Known entity set the scorer uses:** {C\* (interior, depth-2, r1→r2 path), B (bridge), {X·} (depth-2 competitors), {B2,B3,…} (depth-1 competitors), T (target terminal), {T_i} (decoy terminals)} — pairwise-distinct (R8.2).
- **Layout presentation:** facts shuffled; C\*'s prompt-position drawn from p declared slots (retained only as a *layout diagnostic*, §6, E3); target-terminal position is the declared factor (R11).

## 3. Why terminal ≠ answer holds (R8.1)

Unchanged from v0.1 and reinforced: C\* is interior (chain continues to T); every terminal (T, T_i) is ≠ C\* by token-disjointness; the post-C\* and competitor edges use relations outside {r1, r2}, so overshoot or wrong-relation walks are not two-hop-composition successes. Competitor depth-2 nodes are also interior, so the terminal slots are occupied only by {T, T_i}.

## 4. Four-context control design (R7; E4 language corrected)

Per item, four contexts, **each under matched, isolated conditions** — same clutter/load (k, D competitors present), **separate context** so no control seeds C\* into the composite. The claim is **"components retrievable under matched isolated conditions"** (E4), **not** "available in the same context":

- **composite** — full layout; query `r2∘r1(A)`. Measured response.
- **hop1** — matched isolated; query `r1(A)` → B.
- **hop2** — matched isolated; query `r2(B)` (B supplied) → C\*. Run in its own context *because* it surfaces C\*.
- **direct-query** — matched isolated, **bridge withheld** (§5); composite of A → must fail to produce C\*.

Order across contexts counterbalanced and logged; the composite is never preceded in-context by a query exposing C\*. **4× generation cost** (Manager decision, §10). Per-item, per-context token + category logging for G6 scoring and future same-error-identity.

## 5. Direct-shortcut exclusion (R6c; E5 filler specified)

- **Design side (admissibility):** entities chosen so C\* is not directly associable with A (no A–C\* co-occurrence; no head→depth-2 regularity), and — now — **relation-balancing (E8, §2): no head→relation regularity and no relation frequency/order/position salience** that lets the model infer which depth-2 node is the r1→r2 one without following relations.
- **Empirical side (control):** the direct-query context withholds the linking fact and asks the composite. **The withheld fact is replaced by neutral, length-matched filler that contains neither B nor C\*** (E5), so the context length/structure matches the composite while providing no traversal path and no exposure of B or C\*. A model still emitting C\* did so by non-traversal association → that item's composite R1 is invalidated; the rate is measured, not assumed.

## 6. Structural-depth and interior-position controls (E1, E3)

**Structural-depth control (E1 — the core fix).** Depth-2-from-A is made **non-unique** by the same-depth competitors (§2): D nodes share depth 2, and only relation-following (`r1` then `r2`, specifically) selects C\* among them. A fixed-depth heuristic ("return the depth-2 node") is therefore **insufficient** by construction — it underdetermines C\* and scores 1/D. This is what makes *depth alone insufficient* while keeping the target path a genuine two relation-typed hops.

**Interior-position is a diagnostic, not a depth control (E3).** v0.1's prompt-position variation controls *layout-position* salience only. **Post-hoc layout-position correlation does NOT control structural depth** — depth is a graph property invariant to fact-order, so shuffling cannot touch a depth-selection heuristic. Position-variation is therefore retained **only as a layout diagnostic** (does the response track prompt-slot?), and structural depth is controlled separately and primarily by the same-depth competitors above. Conflating the two was the v0.1 error C5 caught.

## 7. Multiclass scorer mapping (R1–R6cat) and a coupled definition note

| Category | Response token |
|---|---|
| **R1 correct-composition** | = C\* (depth-2, r1→r2 path), controls pass, invalidators clear |
| **R2 target-terminal-grab** | = T |
| **R3 stopped-short** | = B (bridge on the r1 path) — error with diagnosis, never partial credit |
| **R4 decoy-terminal-grab** | = some T_i |
| **R5 abstain** | no commitment — failure-to-elicit on an answerable composite |
| **R6cat other** | any other token, incl. depth-2 competitors {X·} and depth-1 competitors {B·} |

Cross-query constant-token invalidator (OI-2) applies across the four contexts as in v0.1.

**Routed open item (E7 — depth-competitor diagnostic).** Under the current six categories, a **depth-competitor-grab** (response = some X·) lands in *other*. This closes the confound for certification (depth-selection scores ≤ 1/D < threshold, §8) but conflates a *diagnostic* signal (the model depth-selected) with generic off-distribution noise — so **a working depth control could inflate *other* with the wrong diagnosis** and trip the other-rate ceiling spuriously. **Required, routed:** *depth-competitor-grab must become a named diagnostic category, or a definition-level split, in `TARGET-CONSTRUCT-DEFINITION` v0.3, **before the other-rate ceiling is locked.*** This is an explicit open item for the definition owner / Manager + C5 — not a unilateral scorer change here. The confound is closed by §2 + §8 regardless; the ceiling cannot be locked until the split lands.

## 8. Heuristic floor derivation (E2 — structural-depth term added)

The derived heuristic floor F is the **best R1 rate any single non-traversal heuristic achieves**:

- **terminal-grab floor** — C\* ∉ terminals (R8.1) → **0**.
- **direct-query floor** — measured (§5); clean subset excludes items above it → **≈ 0**.
- **interior/layout-position floor** — fixed-position pick with C\* over p positions → **1/p** (layout diagnostic).
- **token-pick floor** — frequency/salience pick among m equal-salience candidates → **1/m**.
- **structural-depth floor (NEW, E2)** — fixed-depth pick among D depth-2 nodes → **1/D**.

**F = max(0, ≈0, 1/p, 1/m, 1/D) = max(1/p, 1/m, 1/D).** Success threshold = F + margin (E2; OI-3), fully derived from (p, m, D). Design implication: **larger D (and p, m) drive F down** and make a passing R1 rate more stringent; with same-depth competitors, 1/D may be the **binding** term, so D is a primary rigor knob. A *combined* heuristic (e.g., depth ∧ position) is a testable residual (§ residual risks); the floor takes the strongest single route, and combination is a hypothesis, not a free assumption. **Relation-identity (route 4), once relation frequency/order/position are balanced (§2, §5, §9, E8), has no salience signal to exploit and is bounded by the structural-depth floor 1/D — it adds no new term, so F = max(1/p, 1/m, 1/D) is unchanged.** Without that balancing the route would break the floor (toward 1), which is exactly why relation-balancing is a binding admissibility property, not a tuning choice.

## 9. Rejection conditions (R8 breach; OI-7/OI-8)

At admissibility (mechanical over the schema): C\* ∈ terminals? → reject. C\* aliased with B, any X·, T, or any T_i? → reject. Any category pair not separable? → reject. Entity pool permits A–C\* association **or a head→relation regularity** that singles out the r1→r2 depth-2 node without relation-following? → reject (R6c, extended for depth). A r1-edge from A that is **not unique** (so r1(A) is ambiguous)? → reject (would make the composite ill-posed). Relation **frequency, order, or position not balanced** across target and competitor paths (a relation-salience signal that could select r1/r2 without relation-following)? → reject (R6c / E8; route 4 uncontrolled). At scoring: R6(a) firing → whole-construction rejection. All rejections structurally logged with the breached condition; disposition declared under role-separation.

## 10. Open Manager decisions (values; not set here)

- **k / clutter** (chain-level decoys), **D** (number of same-depth competitors — primary new knob; drives 1/D), **p** (C\*-position slots, diagnostic), **m** (equal-salience candidates).
- **position regime** — target-terminal position factor.
- **n / power** — powered against F = max(1/p, 1/m, 1/D).
- **margin** — success threshold = F + margin.
- **acceptable 4× generation cost** — accept, or direct a cheaper trade (weakens a control; advised against).
- **depth-competitor split (E7 — routed, pre-lock)** — `TARGET-CONSTRUCT-DEFINITION` v0.3 must add a depth-competitor diagnostic category/split **before the other-rate ceiling is locked** (§7); a required routed item for the definition owner / Manager + C5, **not a free Manager value**.

## 11. Boundaries

No items, prompts, pre-registration, run, compression, certified baseline, Claim C, Paper B, capability claim, mechanism claim. CONDITIONAL_FEASIBLE upstream is *appears buildable*, not built or will-certify.

**Forbidden justifications (E6).** The framing **"a depth-2 heuristic approximates traversal"** — or any claim that depth-selection is near-enough to composition to excuse it — **may not be used as justification**. Depth-selection is a **non-traversal route to be excluded** (priced into F as 1/D and controlled by same-depth competitors), not a behavior to be excused as proto-composition. Treating it as "approximate traversal" would reintroduce exactly the false-positive the gate exists to prevent.

## Changelog v0.1 → v0.2 (by C5 edit)

- **E1 — resolved.** Same-depth competitor nodes added (§1, §2, §6): D nodes at depth 2, only relation-following selects C\*; depth alone insufficient by construction.
- **E2 — resolved.** Structural-depth floor 1/D added to F (§8); F = max(1/p, 1/m, 1/D).
- **E3 — resolved.** §6 states post-hoc layout-position correlation does NOT control structural depth; position-variation demoted to a layout diagnostic only.
- **E4 — resolved.** §4 control claim revised to "components retrievable under matched isolated conditions," not "available in the same context."
- **E5 — resolved.** §5 direct-query filler specified as neutral, length-matched, containing neither B nor C\*.
- **E6 — resolved.** §11 forbids "depth-2 heuristic approximates traversal" as justification.

**Preserved from v0.1:** interior-target / terminal ≠ answer (R8), four-context isolation + load-matching, direct-shortcut control, constant-token invalidator, multiclass mapping, derived-floor + margin discipline, rejection/logging.

## Changelog v0.2 → v0.3 (C5 E7/E8)

- **E7 — carried.** Depth-competitor diagnostic promoted from a flagged recommendation to an **explicit routed open item** (§7, §10): a named diagnostic category / definition-level split is **required before the other-rate ceiling is locked**, because a working depth control could inflate *other* with the wrong diagnosis.
- **E8 — carried.** Relation-identity heuristic promoted from residual risk to a **binding admissibility property** (§2, §5, §9): relation frequency, order, and position must be balanced across competitors so r1/r2 cannot be selected by salience alone. This bounds the relation-identity route (route 4) at the structural-depth floor 1/D; **F = max(1/p, 1/m, 1/D) is unchanged.**

**Do-not-weaken invariants preserved (per memo):** terminal ≠ answer (R8.1); direct-query control (§5); same-depth competitor design (§2, §6); F = max(1/p, 1/m, 1/D) (§8); four-context isolation (§4); validity-not-capability boundary (§11); substrate-infeasibility branch (definition v0.2 §8.5; residual). **No items, prompts, pre-registration, or run were added.**

## Residual risks (the next level down)

**Named non-traversal routes to C\*, status:** (1) **terminal-grab — closed** (R8.1, interior target); (2) **direct A→C\* recall — controlled** (direct-query control, §5); (3) **structural-depth selection — closed** (same-depth competitors, 1/D, §6/§8); (4) **relation-identity heuristic — now controlled** (relation-balancing admissibility property, §2/§5/§9, E8; bounded at 1/D). What remains genuinely residual: **(a) combined heuristics** — depth ∧ position ∧ relation in conjunction could exceed any single-route floor; F prices the strongest *single* route, and combination is a testable residual, not yet priced. **(b) the recurrence itself** — if each closed channel keeps birthing another that cannot be driven below a meaningful floor, that is the **substrate-infeasibility signal** (definition v0.2 §8.5) accumulating; this iteration is evidence on whether the gate is satisfiable, and it must **not** be answered by loosening the gate. Neither is closed here; both are the next-round targets, surfaced before any item is written.

---

**C5 artifact access (routing correction).** Per the memo, transmitting byte-exact artifacts + digests to C5 is **CS's action**, not the Senior Engineer's. I have supplied the exact SE-computed digests to enable it: definition v0.2 `f4462f2b…`, design v0.1 `9e90fbc5…`, and design v0.2 below. **SE cannot confirm C5 received the bytes — CS must return that confirmation.** Per the memo, C5 should not be asked for a design-specific verdict without byte access; design v0.2's re-review is gated on CS's transmission.

*Status: design v0.3, property level. Construction design only; no items, prompts, values, or run. Depth-selection closed (v0.2, C5-accepted); E7/E8 carried (depth-competitor diagnostic routed pre-lock; relation-identity now a binding admissibility property). Certifies nothing; authorizes nothing. Ready for Manager value selection.*
