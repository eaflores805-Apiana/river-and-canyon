# PROPOSAL — Path A Constructibility Load-Sweep ("Is there a happy-medium K?")

**E. A. Flores**, Apiana AI, Inc. — June 16, 2026
*River and Canyon · Path A. Drafted by the Senior Engineer. Proposal draft for routing — not a locked pre-registration, not an authorization.*

> **What this is.** A proposal to run the Path A constructibility gate at **multiple clutter levels K**, to test whether there exists an interior load band where the construction elicits **certifiable two-hop composition** — a "happy medium" between *too-easy-to-be-meaningful* (low K, no composition stress) and *too-hard-to-retrieve-at-all* (high K, the observed K=5 floor).
>
> **What this is NOT.** Not the mechanism autopsy of the K=5 off-map mass (it does not separate traversal / grab / chain-anchor-inconsistency). Not a re-run of the closed FAIL (that run stays locked; this is a *new construction* under its *own* lock). Not an authorization — it routes Senior-draft → CS feasibility → C5 claim-risk → TL → **Manager authorizes by name**, like every run. Locking happens *after* the construction is built and the open parameters (§9) are set; **lock-before-look binds the run**.

---

## 1. The hypothesis (a shape claim — stated so we cannot fish for it)

The constructibility of two-hop composition on this substrate is hypothesized to be **non-monotone in load K**, with an interior optimum:

```text
low K   → task is trivial; little/no composition stress; "success" may be preserved
          non-composition, not composition (the Paper-1 trap, see §3)
high K  → substrate floor; single-fact retrieval already fails (K=5: hop1 0.74, hop2 0.68);
          the construction cannot certify
middle  → HYPOTHESIZED band where validated composition clears the certification bar
```

**This is a hypothesis about the *shape* of a curve, and shape claims are exactly where this program has twice drifted past its data.** The protocol is therefore pre-committed to *finding the shape*, including the outcome **"there is no K in range that certifies"** — which is a real, publishable substrate bound, not a failure of the sweep (§5). We do not assume the medium exists; we measure whether it does.

**No presumption about slope direction.** One dot (K=5) licenses no trend. Further, the program's own terminal-attraction bounds-sweep ran **reverse-K** (attraction *fell* with clutter, reported ≈ 0.708 → 0.083 as K went 1→5 — *C5-reported from the prior bounds-sweep; not byte-verified in this proposal's preparation; to be confirmed against that artifact before it is cited as load-bearing*). That precedent means "more clutter → more failure" is **not** a safe default on this substrate. The constructibility curve could ramp, cliff, plateau, or itself be reverse-K. The sweep presumes none of these.

## 2. Why this is the right question (constructibility, not autopsy)

Path A exists to produce a **certified-constructible FP16 baseline** — the precondition the seam waits on. The K=5 run failed to certify. "At what load, if any, can this substrate be made to show clean two-hop composition?" is precisely the constructibility question, it is on-mission, and it **answers the autopsy's one genuinely useful sub-question — does load drive the off-map rate? — as a descriptive byproduct**, without spending budget separating mechanisms on the dead K=5 dataset.

## 3. The locked metric (the single most important discipline)

The sweep is scored on the **per-item-validated, controls-gated R1** — genuine composition that survives the confound battery — **never** a raw "did-not-go-off-map" or "produced-an-answer" rate.

```text
At each K, per item, R1 counts ONLY IF:
  - composite output == C* (target answer), AND
  - R7 controls pass (hop1, hop2 retrievable on the correct chain), AND
  - no R6 invalidator fires (terminal-grab, depth-competitor, direct-recall,
    constant-token, control-floor)
Global per-K metric: validated-R1 rate + Wilson 95% CI (locked, per Path A).
```

**Why this is non-negotiable for a happy-medium search (Paper 1 — "survival is not correctness").** A raw not-off-map rate will look *best at low K*, because low K is trivial — but that "success" is preserved non-composition, a confound-satisfied metric. A happy medium defined on a raw rate is a mirage: it finds the K where the task is too easy to fail, not the K where composition works. The medium is only real if measured by a number a shortcut cannot satisfy. This is the trap most likely to fire precisely *because* the medium-search wants a comfortable peak.

## 4. Construction-validity precondition (a hard gate, not a nicety)

The sweep **must run on a construction where chain identity is robustly recoverable** — semantic/ distinguishable head anchors, fewer or non-identical competitors, reduced relation-sharing — **not** the current construction, where six structurally-identical chains are told apart only by an arbitrary synthetic head token.

```text
Reason (C5, byte-confirmed this arc): on the current construction the SOLE disambiguator is
an arbitrary head token among identical structures. A K-sweep on it measures how
LABEL-TRACKING degrades with K, NOT how COMPOSITION degrades with K. A "happy medium" found
there could be "the K where arbitrary-token-tracking is just barely manageable" — the wrong
quantity. Construct-validity must be fixed FIRST or the curve is about the wrong thing.
```

**This is not a separate cost.** The chain-identity-robust construction *is the same next construction the seam needs anyway.* So the sweep is not a detour: it is **"build the next certifiable construction and characterize its composition-vs-K as you go."** The autopsy's only useful question folds into the productive path.

## 5. Three-outcome decision rule (MECE; pre-declared BEFORE any data)

```text
BAND FOUND       — ∃ K in range where validated-R1 lower CI > success threshold AND no
                   dominant failure signature → a usable certifiable load band exists.
                   (This K becomes the candidate certified-constructible baseline.)
NO USABLE K      — validated-R1 fails the certification bar at ALL tested K (upper CI < floor
                   or a dominant signature at every cell) → no load in range certifies. A real,
                   publishable substrate/task bound; NOT a sweep failure.
INDETERMINATE    — neither cleanly holds (e.g., CIs straddle at the best cells) → INCONCLUSIVE;
                   resolution requires a FRESH pre-declared question (more cells / larger n),
                   never a post-hoc cut on this data.
```

The certification bar is the Path A gate (lower CI > success threshold, no dominant failure signature), now evaluated **per K**.

## 6. Lock-before-look — extended to the sweep (CS discipline; sweeps are especially prone)

A sweep is the *most* fishing-prone design: nothing stops adding a K point near an apparent peak until a medium appears. Before any cell is computed, pre-declare:

```text
(i)   the curve PATTERNS that lean each §5 outcome (ramp / cliff / plateau / interior-peak /
      reverse-K / flat-bad), referencing the validated-R1-vs-K shape — declared, not chosen
      after look;
(ii)  the NULL that forces "no usable K, file the bound" (validated-R1 below bar at all cells);
(iii) a ONE-COMPUTATION-PER-CELL STOP-RULE — each K is run and scored ONCE against the
      pre-declared patterns; NO adding a K point after seeing results to chase a peak, NO
      re-slicing a cell. A second pass (new K points, finer grid) is a FRESH locked
      pre-registration, exactly as a re-run requires a fresh lock.
```

## 7. Confound guards carried from the program (per cell, at every K)

```text
- Full R6/R7 control battery per item at each K (the validated-R1 gating of §3).
- Component load-floor gate: composition is uninterpretable on items where the components
  are not retrievable at all on that item; clear the floor before crediting/discrediting.
- Metric-symmetry / Paper-1 guard: validated metric only (§3).
- Same locked thresholds across all cells (or justified per-cell, declared in advance) —
  threshold values are construction/load-specific until justified; structure is portable.
```

## 8. Ceiling — what the sweep does and does not establish

```text
ESTABLISHES:   whether a load band exists where THIS construction certifies genuine two-hop
               composition (constructibility); and, descriptively, how the off-map rate moves
               with K (the autopsy byproduct).
DOES NOT:      separate the K=5 off-map mechanisms (a)/(b)/(c) — that needs a separator study,
               not a sweep.
NOT A CAPABILITY CLAIM: "the model can/can't do two-hop" is out of bounds; results are
               per-construction, per-load, at the tested n. A BAND FOUND means THIS construction
               certifies at that K, not that the model "can compose"; NO USABLE K means THIS
               construction/family does not certify in range, not that the model "cannot."
SUBSTRATE-INFEASIBILITY: fires only under the repeated-admissible-failure rule; a NO-USABLE-K
               result on one swept family is evidence toward, not proof of, infeasibility.
```

## 9. Open design decisions — flagged for routing, not pre-decided here

```text
A. CONSTRUCTION (the gating decision): existing head-token construction vs the new
   chain-identity-robust construction. SE RECOMMENDATION: the new construction — the
   existing one inherits the construct-validity confound (§4) and would measure
   label-tracking-vs-K. This is a design + build decision (CS feasibility + construction build).
B. K RANGE: enough points to resolve shape (ramp/cliff/plateau/interior-peak/reverse-K).
   SE starting suggestion: K ∈ {1, 2, 3, 5, 7} — K=1 as the trivial-floor anchor, K=5 as the
   known prior point re-measured on the NEW construction, interior points to expose any band.
   Exact grid is a feasibility/compute call.
C. PER-CELL n: powered for a Wilson CI tight enough to clear/miss the bar decisively at each K.
D. THRESHOLDS: inherit the Path A locked values (success threshold, floor, dominance,
   other-rate, control-floor) or re-derive for the new construction — declared before lock.
E. COMPUTE BUDGET: a sweep is several runs (≈ |K| × the single-run cost). Manager resourcing.
```

## 10. Boundaries

```text
- NEW locked pre-registration on a NEW construction; the K=5 FAIL stays closed and untouched
  (this is not a re-run; §17 satisfied by the new construction + new lock).
- Manager authorizes the run by name; locking is CS; the run is several authorized executions.
- Lock-before-look binds the run: §5 outcomes, §6 patterns/null/stop-rule pre-declared,
  metric (§3) and construction-validity (§4) fixed, before any cell is computed.
- This proposal certifies nothing and authorizes nothing. It defines the question, the locked
  metric, the decision rule, the preconditions, and the open decisions — for routing.
```

---

**The one to carry up:** This proposes a **constructibility load-sweep** — run the Path A certification gate at multiple clutter levels K to test whether a **happy-medium band** exists where the construction certifies genuine two-hop composition, between trivial-low-K and the observed high-K retrieval floor. It is locked on the **validated, controls-gated R1**, never a raw rate (Paper 1: a raw rate peaks at trivial low K and finds a mirage medium). It is gated on **construction-validity first** — the sweep must run on a chain-identity-robust construction, not the current head-token-only one, or it measures label-tracking-vs-K rather than composition-vs-K; and that construction is the *same* one the seam needs, so the sweep folds the autopsy's one useful question (does load drive this?) into the productive path rather than spending budget on the closed FAIL. It pre-declares **three MECE outcomes** (band found / no usable K / indeterminate), with "no usable K" a real publishable substrate bound, and it extends **lock-before-look to the sweep** (pre-declared curve patterns, the null, and a one-computation-per-cell stop-rule, because sweeps are the most fishing-prone design). It presumes **no slope direction** — one dot licenses no trend, and the program's own reverse-K bounds-sweep precedent (reported, to be byte-verified) shows positive slope is not a safe default. Ceiling: it establishes constructibility (a certifiable load band, or its absence) and describes the off-map-rate-vs-K byproduct, but does not separate the K=5 mechanisms and is not a capability claim. It is a NEW locked pre-registration on a NEW construction, Manager-authorized by name; the K=5 FAIL stays closed; this proposal authorizes nothing.

— Senior Engineer (drafting; routes Senior → CS feasibility → C5 claim-risk → TL → Manager-by-name)
