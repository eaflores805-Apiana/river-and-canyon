# PATH-A-CANDIDATE-CONSTRUCTION-DESIGN-v0.1

**E. A. Flores**, Apiana AI, Inc. — June 15, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. Construction-design object (property level).*

## 0. Scope / negative-use

The first candidate construction under `TARGET-CONSTRUCT-DEFINITION-v0.2` (digest `f4462f2b…`). Specified **at property/schema level only**.

**Not in this object:** task items, concrete tokens, prompt templates, pre-registration, run request, compression rung, Claim C / Paper B language, model-capability or mechanism claims. Entities are placeholders (A, B, C\*, T, …); quantities are parameters (k, p, m), not values. Values are Manager decisions (§10).

**Negative-use.** A *candidate design*, not a built construction, not a certified baseline, not evidence of anything. CONDITIONAL_FEASIBLE upstream means "appears buildable"; this object proposes one such build for review, and it certifies and authorizes nothing. It is **not yet admissible** until CS feasibility and C5 claim-risk clear it against v0.2 §10.

## 1. Construction idea in one paragraph

Build closed-world chains over two relation types r1, r2, but make the queried two-hop target an **interior node of a longer presented chain**, not its endpoint. The target chain is `A —r1→ B —r2→ C* —(further edges)→ … → T`, where **C\* is the two-hop target from A and T is the chain's sink (salient terminal)**. Because the layout continues *past* C\* to T, C\* is never a terminal and T is always a wrong answer — which is exactly how terminal ≠ answer (R8.1) is realized without abandoning genuine two-hop structure: the queried composition is strictly `r2∘r1(A) = C*`, two hops, and the chain's extension is a pure layout device to put a non-C\* token in the salient terminal slot. Decoy chains of identical relational shape supply clutter; their sinks are decoy terminals (also wrong). Facts are presented in randomized order so C\*'s prompt-position varies across items, denying a fixed-position grab. Four separate, clutter-matched contexts (composite, hop1, hop2, direct-query) isolate the measurement from its own controls.

## 2. Entity / layout schema

- **Entities:** a closed-world pool partitioned into chains; all entities introduced in-context (no parametric recall required).
- **Relations:** two types r1, r2, shared across target and decoy chains so the chains are structurally indistinguishable except by their head.
- **Target chain (property):** `A —r1→ B —r2→ C* —rX→ … —rY→ T`, length ≥ 3 edges so that C\* (at depth 2 from A) is strictly interior and T (the sink) is at depth ≥ 3. The edges past C\* use relation types **outside** the queried {r1, r2} path so they cannot be mistaken for the composition path.
- **Decoy chains (clutter, k of them):** `P_i —r1→ Q_i —r2→ S_i —…→ T_i`, same shape; sinks T_i are decoy terminals. k is the declared clutter regime (R11; not lone-chain, R12.1).
- **Token roles per item (the known entity set the scorer uses):** {C\* (interior target), B (bridge), T (target sink/terminal), {T_i} (decoy terminals)}, all **pairwise-distinct** (R8.2).
- **Layout presentation:** facts shuffled; **C\* drawn from a declared set of p prompt-positions** (uniform), and the **target-terminal (T) position** is the declared experimental factor carried from the sweep (R11). The two position controls are distinct: C\*-position is *varied to defeat interior-position grab*; T-position is *the declared factor*.

## 3. Why terminal ≠ answer holds (R8.1)

- C\* is defined as an **interior** node: the presented chain continues past C\* to a deeper sink T, so C\* sits at no chain boundary.
- Every **salient terminal** in the layout — the target sink T and every decoy sink T_i — is, by construction, **not** C\* (admissibility checks token-disjointness, §9). So any terminal-grab lands on a wrong token (R2 or R4), and can never be misread as correct.
- The queried relation path is strictly two hops (`r1` then `r2`); the post-C\* edges use other relation types, so traversal that "overshoots" to T would require following a *different* relation than the query names — i.e., overshoot is not a two-hop-composition success, it is a terminal-grab.
- This is the "chain structure beyond a bare A→B→C" that v0.2 R8 anticipated; here the structure is *chain extension past the target*.

## 4. Four-context control design (R7; isolation + load-matching)

Per item, four separate contexts, **each carrying the same clutter regime (k) and load as the composite** (load-matched), and **each a distinct context** so no control seeds C\* into the composite (isolation). Realization at property level:

- **composite context** — full target chain + k decoys; query `r2∘r1(A)`. The measured response.
- **hop1 context** — same clutter/load; query `r1(A)` → expect B. First fact available.
- **hop2 context** — same clutter/load; query `r2(B)` (B supplied) → expect C\*. Second fact available. *Run in its own context precisely because it surfaces C\*; it must not share a context with the composite.*
- **direct-query context** — same clutter/load **but with the bridge withheld** (§5); query the composite of A → must **fail** to produce C\*.

Order across the four contexts is counterbalanced and **logged as a factor**; the composite is never preceded in-context by a query that exposes C\*. **Cost: 4× generations per item** (accepted-pending-Manager, §10). Per-item, per-context **token + category logging** is emitted for G6 scoring and future same-error-identity comparison (§7, §9).

## 5. Direct-shortcut exclusion (R6c, OI-1)

Two parts, matching v0.2:

- **Design side (admissibility).** Entities are chosen so C\* is not directly associable with A: A and C\* do not co-occur as a named pair in any presented fact, and the pool avoids head→sink-2 regularities that would let A predict C\* without B. (This is a *property* the entity pool must satisfy; the concrete realization is item generation, deferred.)
- **Empirical side (control).** The **direct-query context** removes the linking fact(s) that make traversal possible (the `A—r1→B` edge, or `B—r2→C*` edge, withheld) and asks the composite. A model that still emits C\* did so by a non-traversal association → that item's composite R1 is **invalidated**. Because this runs in its own context, it does not contaminate the composite. The per-item direct-query result also *measures* the direct-association rate rather than assuming it is zero.

## 6. Interior-position salience control (R6d, OI-5)

- The risk this design itself introduces: once C\* is an interior token, a **fixed-position selection rule** ("always take the token at prompt-slot s," or "second-from-the-end," or a hub-node bias) could yield C\* without traversal — the next confound one level down from terminal-grab.
- **Control:** C\*'s prompt-position is **varied across items over p declared slots (uniform)**, so no constant-position rule tracks it. The scorer flags **interior-position-grab**: if an item's correct response is explained by a response-position that is constant while C\*'s actual position varies, R1 on that item is invalid (mechanically checkable from logged positions).
- This is named explicitly as the **residual risk to pressure-test** (§9, and the review ask below): the extended-chain device defeats terminal-grab but must be shown not to substitute an interior-position or "penultimate-node" salience that a heuristic can ride.

## 7. Multiclass scorer mapping (R1–R6cat; OI-2 constant-token)

Response classified by a pre-declared rule over the token and the known entity set:

| Category | Response token |
|---|---|
| **R1 correct-composition** | = C\* (interior target), controls pass, all invalidators clear |
| **R2 target-terminal-grab** | = T (target sink) |
| **R3 stopped-short** | = B (bridge) — error with diagnosis (hop2-in-composition failure), never partial credit |
| **R4 decoy-terminal-grab** | = some T_i (decoy sink) |
| **R5 abstain** | no entity commitment — on an answerable composite, a failure-to-elicit, not neutral |
| **R6cat other** | any other token (incl. a decoy interior node), or malformed |

**Cross-query constant-token invalidator (OI-2):** the four contexts yield four response tokens per item; if the token is **constant across composite / hop1 / hop2 / direct-query**, the model is emitting one token regardless of question (flat heuristic) → R1 invalid even if that token = C\* on the composite. (Re-imports G6 Rule B.) Distinguishability (R8.3) holds because C\*, B, T, {T_i} are distinct tokens and abstain/other are non-entity outcomes; a decoy interior node lands in *other* and a rising *other* rate trips the ceiling (R11).

## 8. Heuristic floor derivation (OI-3; four named floors)

The derived heuristic floor F is the **best R1 rate any single non-traversal heuristic can achieve in this layout**:

- **terminal-grab floor** — P(terminal-grab = C\*). Since C\* ∉ terminals (R8.1), **= 0**.
- **direct-query floor** — the measured rate the model produces C\* with the bridge withheld (§5). On the retained (clean) subset, items above this are excluded, driving the direct-association contribution to **≈ 0** (measured, not assumed).
- **interior-position floor** — P(a fixed-position pick = C\*) with C\* uniform over p positions, **= 1/p**.
- **token-pick floor** — P(a frequency/salience pick = C\*) with m equal-salience interior candidates, **= 1/m**.

**F = max(0, ≈0, 1/p, 1/m) = max(1/p, 1/m)** — fully derived from construction parameters (p, m), per OI-3. Design implication: **larger p and m drive F down**, making a passing R1 rate more stringent and more meaningful; the construction should maximize both within feasibility. (If a *combined* heuristic is hypothesized, the floor is still the strongest single available route; combination is itself a testable claim, not a free assumption.)

## 9. Rejection conditions (R8 breach; OI-7, OI-8)

Checked **at admissibility, before any item is written** (mechanical over the schema's entity set):

- C\* ∈ {any sink/terminal in any presented chain}? → **reject construction** (R8.1 breach).
- C\* aliased with B, T, or any T_i? → reject (R8.2 breach).
- Any two of {C\*, B, T, {T_i}} share a token, or any category pair not separable? → reject (R8.3 breach).
- Entity pool permits a direct A→C\* pair or head→sink-2 regularity? → reject (R6c design side).

**At scoring:** if R6(a) (terminal coincidence: response = C\* = a terminal) ever fires, a breach slipped through → the **whole construction is rejected**, not the item (OI-7). Every rejection is **structurally logged** with the breached condition; disposition (archive / iterate / abandon) is a declared routing decision under role-separation (OI-8), not limbo.

## 10. Open Manager decisions (values; not set here)

- **k / clutter** — number of decoy chains (regime; not lone-chain).
- **position regime** — p (number of distinct C\*-positions) and the target-terminal (T) position factor.
- **n / power** — sample size, powered to distinguish the R1 rate from F = max(1/p, 1/m).
- **margin** — the pre-declared margin above F defining success threshold = F + margin.
- **acceptable 4× generation cost** — accept the four-context cost, or direct a cheaper trade-off (which would weaken isolation or load-matching — advised against).
- **m** — number of equal-salience interior candidates (drives the token-pick floor); a design/Manager joint parameter.

## 11. Boundaries

No run, no items, no prompts, no compression, no certified baseline, no Claim C, no Paper B, no model-capability claim, no mechanism claim. CONDITIONAL_FEASIBLE upstream is *appears buildable*, not built or will-certify. The strongest downstream statement this design supports, once built and run, is a **validity** statement about elicited behavior under declared conditions — and only if it clears its derived gate, which this object does not decide.

---

**Residual risk flagged for review (the one to pressure-test).** This design defeats terminal-grab (the confound that killed nine constructions) by moving C\* to an interior node — but per the program's recurring pattern, *the fix for one confound tends to birth the next one a level down*. Here the candidate new channel is **interior-position / penultimate-node salience** (§6): the very act of placing C\* off the terminal puts it at an interior slot that a position- or hub-biased heuristic might ride. §6's position-variation control and the interior-position-grab invalidator are the proposed defense, and the derived floor (§8) prices it in via 1/p — but whether the defense is *sufficient* on this substrate is exactly the question CS feasibility and C5 claim-risk should attack, not something this draft can self-certify. If interior-position salience cannot be controlled below a meaningful floor, this construction fails its own gate, and that — surfaced now, before items — is the honest outcome.

*Status: design v0.1, property level. Construction design only; no items, prompts, values, or run. Certifies nothing; authorizes nothing. Ready for CS feasibility and C5 claim-risk review against v0.2 §10.*
