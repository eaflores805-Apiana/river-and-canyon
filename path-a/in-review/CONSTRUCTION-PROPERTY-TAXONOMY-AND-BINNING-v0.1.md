# CONSTRUCTION-PROPERTY-TAXONOMY-AND-BINNING-v0.1

**E. A. Flores**, Apiana AI, Inc. — June 16, 2026
*River and Canyon · Path A. Prepared by the Senior Engineer. Analytic comparison object.*

## 0. Scope / negative-use

Gathers the candidate construction approaches now in play, derives a property set (split into **required** gate-soundness properties and **desirable** properties), and bins the candidates by property profile — to inform the **construction-philosophy decision**, which is the Manager's and team's, not this object's. This is analysis, not a build, a certification, or an authorization. It certifies nothing, advances no claim, and selects no construction.

**One discipline declared up front.** "Fixes chain identity" / "makes binding easy" is deliberately **NOT** a required property. Treating it as a virtue presumes the K=5 failure was caused by chain-anchor instability (mechanism (c)) — which the combined-position record explicitly recorded as *consistent-with, not established* (the data could equally reflect (b) relation-keyed grab or (a) traversal; the run could not separate them). So the matrix scores **how** a candidate addresses the measured failure — forecloses every non-traversal route, vs. bets on one mechanism — never whether it flatters the chain-identity story.

## 1. Candidates gathered

```text
C0  EXISTING head-token construction        the closed K=5 FAIL — included as reference/baseline
V3  SAME-DEPTH-COMPETITOR design (v0.3)      the reviewed candidate: foreclose ALL non-traversal routes
D1  EXPLICIT CHAIN-IDENTITY TAGS             prefix each fact with a chain tag
D2  SEMANTICALLY-DISTINCT CHAINS             each chain a different domain/story
D3  STAGED / GATED                           verify binding (or list facts) before scoring composition
D4  VARIABLE IDENTITY STRENGTH               vary how chain membership is signaled, as an experimental knob
D5  HIERARCHICAL / GROUPED TOPOLOGY          nested/sectioned facts instead of flat parallel chains
```

## 2. Property set (derived; required vs desirable)

**REQUIRED — gate-soundness. A construction failing any of these cannot be a valid two-hop composition gate.** (Sourced from prereg v0.3, design v0.3, and the open-items "do-not-drift" invariants.)

```text
R1  TERMINAL ≠ ANSWER          C* interior; no terminal occupies the answer slot.            [R8.1]
R2  TRAVERSAL-ONLY SELECTION   NO non-traversal route (depth / layout-position / token-
                               salience / relation-identity / direct A→C* recall) selects
                               C* above a derived floor. THE core gate property.            [design §1/§6/§8]
R3  DERIVED FLOOR              success threshold pinned to the construction's own parameters
                               (F = max(1/p,1/m,1/D) + margin), not freely declared.         [OI-3, prereg §4]
R4  GENUINE TWO-HOP            r1(A)=B and r2(B)=C* unique and well-posed; a composition
                               task, not a lookup.                                           [design §1/§2]
R5  FOUR-CONTEXT CONTROL       composite/hop1/hop2/direct-query runnable under matched
                               isolated load.                                                [R7, prereg §6]
R6  MECHANICAL ADMISSIBILITY   an inspector can accept/reject it before scoring.             [prereg §7, C1–C9]
R7  INFEASIBILITY-COMPATIBLE   a failure is interpretable and never forces loosening the
                               gate; repeated admissible failure = substrate-infeasibility.  [prereg §17]
```

**DESIRABLE — improve the instrument; not soundness gates.**

```text
W1  MECHANISM-AGNOSTIC         validity does not depend on which mechanism caused K=5
                               ((a)/(b)/(c)); forecloses all routes rather than betting on one.
W2  BINDING OBSERVABLE         chain-binding success measurable separately, before scoring
                               composition (the cross-query chain-membership instrument).
W3  IDENTITY-STRENGTH VARIABLE chain-identity signal strength deliberately variable →
                               discriminating power to TEST whether (c) is real.
W4  SINGLE-PASS                measures unscaffolded two-hop composition (no pre-step that
                               does the binding for the model — that is a different task).
W5  LOAD-TUNABLE               clutter / competitor count are knobs (sweepable).
W6  NO NEW CONFOUND            introduces no NEW non-traversal shortcut (tag-match, topic-
                               match, section-match) that itself then needs controlling.
W7  BUILDABLE / CHEAP          synthetic-token-realizable at reasonable cost.
```

## 3. Required-property matrix

✓ meets · ~ partial/conditional · ✗ fails/violates · — not-applicable (overlay, not a construction)

```text
            R1      R2          R3      R4      R5      R6      R7
          term≠   travrsl-    derived  2-hop   4-ctx   mech.   infeas-
          answer  only        floor            ctrl    admis   compat
C0  exist   ✓       ✗           ~        ✓       ✓       ✓        ✓     ← failed R2 (label-track/depth route)
V3  v0.3    ✓       ✓           ✓        ✓       ✓       ✓        ✓     ← engineered against all 7
D1  tags    ~       ✗           ✗        ✓       ✓       ~        ✓     ← tag-match defeats R2/R3
D2  semant  ~       ✗           ✗        ✓       ✓       ~        ✓     ← topic-match defeats R2/R3
D3  staged  —       —           —        —       ✓       —        ✓     ← overlay, not a construction
D4  id-var  —       —           —        —       —       —        ✓     ← probe/variable, not a construction
D5  hier    ~       ~           ~        ✓       ~       ~        ✓     ← under-specified; group-match risk on R2
```

**Reading:** only **V3** currently meets all seven required properties — because it was designed against them and went through the review (E1–E8, OI-1…16) that derived them. **D1/D2 actively violate the two most important** (R2 traversal-only, R3 derived-floor): a chain tag or a distinct topic is a *non-traversal* way to pick the right chain, so "success" would measure tag/topic-matching, not composition — the Paper-1 mirage in new dress, and exactly the recurrence the v0.3 design's residual-risks section warns against. **C0** fails R2 (the label-tracking route the scout exposed). **D3/D4 are mostly "—"** because they are not constructions at all (see §5).

## 4. Desirable-property matrix

```text
            W1      W2       W3       W4       W5      W6      W7
          mech-   binding  id-str   single-  load-   no-new  build-
          agnost  observ   variable pass     tunable confnd  able
C0  exist   ✗       ~        ✗        ✓        ✓       ~        ✓
V3  v0.3    ✓       ~        ✗        ✓        ✓       ✓        ~
D1  tags    ✗       ✓        ✓        ✓        ✓       ✗        ✓
D2  semant  ✗       ~        ~        ✓        ✓       ✗        ~
D3  staged  ~       ✓        —        ~        —       ~        ✓     ← two-stage variant fails W4 (scaffolds)
D4  id-var  ✓       ~        ✓        ✓        ✓       ~        ✓     ← the only TEST of the mechanism (W3)
D5  hier    ~       ~        ~        ✓        ~       ~        ~
```

**Reading:** the desirable column splits the field by philosophy. **V3** scores on mechanism-agnostic + no-new-confound + single-pass + load-tunable, but only *partial* on binding-observable (it can carry the chain-membership log, but doesn't make binding a separate gate) and is *not* identity-strength-variable (it deliberately keeps chains structurally similar to force traversal). **D1** scores on binding-observable and identity-strength-variable but **fails no-new-confound** — its strength and its fatal flaw are the same feature. **D4 is special:** it is the only candidate that scores on W3 in a way that *tests* the mechanism the others *assume* — vary the identity signal, hold facts fixed, watch the off-map rate; large movement supports (c), small movement points to (b), which tags would not fix.

## 5. Binning — two cuts, and the structural finding

**Cut 1 — by KIND. The "five directions" are not five competing constructions.**

```text
CONSTRUCTION TOPOLOGIES (a thing you build):     C0, V3, D2, D5
SIGNAL OVERLAY (a cue you add to a construction): D1  (tags)
MEASUREMENT / PROBE OVERLAYS (a thing you DO to a construction):  D3 (staged binding metric), D4 (identity-strength sweep)
```

This is the first real finding: **D3 and D4 (and arguably D1) are orthogonal to the construction choice — they ride on top of whatever construction you pick.** So the actual construction decision is among the *topologies* (C0 dead, V3, D2, D5), and D1/D3/D4 are things you layer onto the chosen one. Comparing "tags vs same-depth-competitors" as if they were rival constructions is a category error; tags are a *signal* you could add to V3 (and shouldn't, per W6).

**Cut 2 — by PHILOSOPHY. This is the load-bearing axis.**

```text
FORECLOSE-ALL-ROUTES  (mechanism-agnostic):   V3
MAKE-IDENTITY-EASY    (assumes (c) is the cause): D1, D2, and D5's grouping cues
TEST-THE-MECHANISM    (assumes nothing; discriminates): D4 (+ D3 as the binding observable)
```

The divider is whether you **bet on a mechanism** or **foreclose all of them**. V3 needs no commitment about why K=5 failed — it closes depth, position, salience, relation-identity, and direct-recall simultaneously, so it is valid whether the cause was (b) or (c). D1/D2 *bet* the cause was (c) and optimize for it — which is both an overclaim (we never established (c)) and *less robust* if the cause was actually (b), since tags/topics do nothing about a relation-keyed grab.

## 6. The target profile, and what approaches it

**Target profile** = all 7 required + the desirable ones that matter most for a sound, interpretable, sweepable gate: **W1 mechanism-agnostic, W6 no-new-confound, W2 binding-observable, W4 single-pass, W5 load-tunable**, plus **W3 identity-strength-variable as a separable probe** (so the mechanism can be tested, not assumed).

No single candidate hits the whole target — but a **combination does, and it is the "more comprehensive" construction the binning points to:**

```text
  V3            as the CONSTRUCTION         → R1–R7 + W1 + W4 + W5 + W6  (the foreclose-all spine)
+ D3-metric     as a BINDING OVERLAY        → closes W2 (V3's one partial): measure chain-binding
                                              success as a separate reportable metric BEFORE scoring
                                              composition — the single-pass variant, NOT the two-stage
                                              scaffold (which would forfeit W4)
+ D4            as a MECHANISM PROBE         → closes W3: a matched weak-vs-strong-identity arm on the
                                              SAME facts, to TEST whether (c) was ever the cause —
                                              retroactively validating or refuting the entire premise
                                              the chain-identity directions assumed
  ────────────────────────────────────────
  EXPLICITLY NOT D1 / D2 as the construction → they fail W6 and violate R2/R3 (tag/topic-match route)
```

The binning's payoff: the right next object is **not** "pick one of five directions." It is **V3 as the construction, with staged binding-measurement and an identity-strength probe layered on** — which gives a mechanism-agnostic gate that *also* carries the instrumentation to test the chain-identity hypothesis the directions doc took for granted. That is strictly more comprehensive than any single direction, and it does not buy comprehensiveness by importing a new confound.

## 7. Caveats (the honest perimeter)

```text
- THE REQUIRED SET ENCODES A PHILOSOPHY. R1–R7 are derived from the EXISTING gate philosophy
  (foreclose-all-routes; validity-not-capability; single-pass). If the team deliberately chose a
  DIFFERENT philosophy — e.g. "scaffolded composition is an acceptable target" — then D3's two-stage
  variant stops failing W4 and bins differently, and the whole matrix shifts. The property set is a
  CHOICE, and that choice is the Manager's / team's, not this object's. The binning is conditional on it.
- "FIXES IDENTITY" IS NOT A REQUIREMENT, BY CONSTRUCTION (§0). Scoring it as a virtue would presume
  mechanism (c). The matrix rewards foreclosing all routes (mechanism-agnostic), not betting on (c).
- THIS IS ANALYSIS, NOT A DECISION OR A BUILD. No construction is selected, no items written, no run
  authorized. The construction-philosophy call routes to the Manager / team.
- PROVENANCE. V3's property claims (the ✓'s in its row) are read from the construction-design v0.3 and
  pre-registration v0.3 bytes; they are NOT a full audit — the referenced instrument digests (inspector,
  evaluator, constants, definition v0.4) were relayed, not SE-recomputed, and definition v0.4 was not
  read in full. A V3 column that must be load-bearing should get that audit first.
- D5 IS UNDER-SPECIFIED. Its row is mostly "~" because the hierarchical topology has not been designed
  to the property level; it is a hypothesis worth its own design pass, not a ready candidate.
```

---

**The one to carry up:** Gathering the candidates and binning them by property yields two findings the ad-hoc comparison hid. **First, the "five directions" are not five rival constructions** — only two are construction topologies (semantic-distinct D2, hierarchical D5; the existing C0 is the dead one), one is a signal overlay (tags D1), and two are measurement/probe overlays (staged binding D3, identity-strength sweep D4) that ride on top of *whatever* construction is chosen. **Second, the real axis is philosophy: foreclose-all-routes (mechanism-agnostic — the v0.3 design) vs. make-identity-easy (which assumes the unproven chain-identity mechanism and, worse, reintroduces a tag/topic-matching shortcut that defeats the traversal-only and derived-floor requirements).** Against a required-property set derived from the existing gate, only the v0.3 same-depth-competitor design meets all seven; D1/D2 violate the two most important. The target profile is best approached not by any single direction but by a **combination — v0.3 as the construction, a staged binding-measurement overlay (single-pass variant) to make binding observable, and an identity-strength probe to TEST rather than assume the chain-identity mechanism** — which is strictly more comprehensive than any direction and imports no new confound. Caveat the binding constraint: the required set encodes a gate-philosophy choice that is the Manager's/team's to make, and the v0.3 property row is read from the design+prereg, not a full instrument audit. Analysis only; selects nothing; authorizes nothing; the FAIL stays closed.

— Senior Engineer (analytic input; routes to Manager / team for the construction-philosophy decision)
