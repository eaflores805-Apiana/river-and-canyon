# C5 CLAIM-RISK RECORD — The FP16 Off-Map Mass: Combined Team Position

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead → New Senior (synthesis lead) → Manager · **Cc:** C4, C6, CS, Senior
**Date:** 2026-06-16
**Version:** v0.2 (supersedes v0.1 `c0914399…6436`, retained)
**Re:** complete claim-risk record of the combined position (C5 + C4 + C6 + CS) on the Path A FP16 off-map mass, for folding into the of-record synthesis
**Status:** claim-risk record. Model-free. Changes no verdict, authorizes no run, makes no mechanism claim. **Not the of-record synthesis** — that is the New Senior's / Team Lead's to assemble; this is C5's contribution to it, authored from the claim-risk seat so the synthesis carries an independent check rather than being graded by its own author.

> **v0.2 revision note.** Folds two CS contributions, both adopted because each contributes (one is a correction to v0.1, not merely an addition): **(1)** lock-before-look applies to the model-free rung-1 audit itself — §5 pre-commitment broadened from a consistency threshold to a full pre-declared stop-rule, lean-pattern, and null (§5, §6). **(2) Correction to v0.1:** cross-query chain-membership consistency is NOT a clean (c)-detector as v0.1 implied — high consistency is produced both by (a) coherent traversal and by a fixed-target (b) grab, so the consistency *rate* conflates them in (a)'s favor; the matrix discriminates only via its per-query chain-identity *pattern* (anchor-tracking vs fixed-chain). §4 characterization and §5 disciplines corrected accordingly. Per CS, both are sharpenings of what C6's requirements already implied; nothing else is added, as the space is worked over and further additions would be motion, not signal.

> **Authorship boundary (why this document is scoped as it is).** A complete of-record synthesis is a synthesis-seat deliverable. C5 is the adversarial-foresight seat; a synthesis authored AND claim-risk-reviewed by C5 would have no independent check — the same structural defect the off-map memo routed around by separating the Senior's drafting from the adjudication of his own approach. This record therefore states the combined position completely and labels every claim by its support level, but it is input to the of-record document, not the document itself.

---

## 1. The settled finding (positional; behavioral; not in question)

The Path A FP16 constructibility run (commit `265114b`) remains a **locked FAIL** via the dominant-signature branch. Nothing here reopens it. The finding that is settled — independently reproduced from the committed bytes by two seats — is **positional only**:

```text
Of 96 composite responses, 38 fell into R6cat ("off-map"). All 38 are on-page
decoy-chain entities:
  33/38  at decoy ANSWER-depth positions (depth-2, wrong chain)
   5/38  at decoy BRIDGE positions (depth-1, wrong chain)
   0/38  novel tokens (not in the item)
   0/38  format-variants of the correct target answer

The engineered confounds stayed quiet: target-terminal-grab 4%, depth-competitor
(R4b) 0/96, direct-recall 0, constant-token 0. Single-fact retrieval was already
unreliable under the clutter: hop1 control 0.74, hop2 control 0.68.
```

The claim-safe statement, and the only one the tokens license:

> **The FP16 off-map mass is structured: all R6cat outputs are on-page decoy-chain entities, mostly at decoy answer-depth positions — right answer-type, wrong address.** This is *where the tokens sat*, not *what process produced them*. It is per-construction, at this load, n=1, and not a capability claim.

This positional finding **is the product.** Everything in §§2–4 is hypothesis about the mechanism behind it, and the mechanism question is open.

## 2. The hypothesis space (corrected — two mechanisms, one shared observable)

The original decomposition was too narrow:

```text
(a) wrong-chain traversal     — the model followed decoy-r1 → decoy-r2 from a decoy head
(b) positional/salience grab  — the model grabbed a decoy-C node by depth/position/salience
```

The combined review added one genuinely missing mechanism and corrected one apparent one:

```text
(c) observable chain-anchor inconsistency  [C5/C4, relabeled per C6]
    Under shared-relation clutter, the model does not maintain a stable binding between
    the queried anchor A and its originating chain; it surfaces some relation-shaped
    fact-pair without holding the target-chain identity across queries. The decoy-C token
    is the residue of unstable anchoring, not a completed wrong-chain traversal or a
    consistent positional rule.
    NOTE ON NAMING: stated as "observable chain-anchor inconsistency" — a behavioral
    property (does retrieval stay within one chain across queries?) — NOT "binding failure,"
    which would assert an internal mechanism the seat does not claim. This relabel (C6) is
    a deliberate tightening and is adopted.
```

**On C6's proposed (d) "answer-role prior / right type, wrong address":** this is **not a fourth mechanism.** It is the observable OUTPUT SIGNATURE that (b) and (c) BOTH produce — a relation-keyed grab lands an answer-depth node on a wrong chain ("right role, wrong address"), and chain-anchor inconsistency surfaces an answer-shaped entity without chain identity ("right role, wrong address"). Listing (d) as a peer cell double-counts the space: it implies four separable mechanisms when there are **two live mechanisms ((b), (c)) plus one shared observable that neither uniquely owns.** (d) is correctly recorded as the *name for the settled positional finding* (§1), not as a competing hypothesis. Enumerating it as a cell would invite a study mis-designed to sort items into four bins.

**The corrected hypothesis space, stated honestly:**

```text
TWO live mechanisms:
  (b) relation-signature-keyed grab
  (c) observable chain-anchor inconsistency
ONE shared output signature they both produce, which the current run cannot use to
  separate them:
  answer-role-correct, address-wrong  (= C6's "(d)", = §1's settled finding)
(a) wrong-chain traversal remains logically possible but is the LEAST supported (see §3).
None is proven.
```

## 3. What the data supports — and the two over-reads that must stay blocked

**Supports (c) being a live hypothesis** (not (c) winning):

```text
- Target hop2 control = 0.677. Retrieval is fragile EVEN WHEN B is handed to the model
  directly on the CORRECT chain — no wrong-chain choice involved. This is the strongest
  single point: it weakens (a) AND (b) as COMPLETE accounts, because both presume a
  competence the target-chain control already shows is intermittent.
- The 38 tokens are clean on-page decoy depth-2 entities (0 novel, 0 format-variant),
  consistent with "surfaced some r1→r2-shaped pair" as much as with any cleaner story.
```

**Two over-reads, corrected and to stay blocked** (both originally offered in (c)'s favor; flagged hardest precisely because they flatter the reviewers' own hypothesis):

```text
OVER-READ 1 — "R4b = 0/96 weakens (b)."  IT DOES NOT.
  R4b=0 refutes only the crude "grab ANY depth-2 node" version. Decoy-C nodes sit on
  chains SHARING the target's r1/r2 relations; the suppressed competitors (X_i) sit on
  chains with DISJOINT relations. R4b=0 says the model ignored the relation-MISMATCHED
  chains — which is equally consistent with, and arguably SUPPORTS, a sharper
  relation-signature-keyed (b): the model grabs answer-depth nodes from relation-MATCHING
  chains specifically. R4b=0 weakens a crude (b); it does not weaken the live (b).

OVER-READ 2 — "Direct-query 100% pass shows clean low-load composition."  IT DOES NOT.
  Direct-query is a NEGATIVE control: it confirms the direct A→C* recall shortcut was
  ABSENT (the route is empirically closed). That is the OPPOSITE of "the model composes
  cleanly at low load." The low-load-capability claim would need a low-load COMPOSITE
  test, which this run does not contain.
```

**The honest state, therefore:**

> The data is **consistent with** observable chain-anchor inconsistency, and **cannot separate** it from relation-keyed grabbing or from the shared answer-role signature. It is **not** "the data leans (c)." Calling it "leans (c)" would license designing the next study to *confirm* chain-anchor inconsistency — the prejudged-result entry point the lock-before-look discipline exists to block. (c) is a **live missing hypothesis, not the winning one.**

## 4. Why the obvious next experiment is under-specified

A decoy-control study that only asks **"can the model retrieve the decoy chain's components on demand?"** is confounded by (c): degraded decoy retrieval is *expected* under chain-anchor inconsistency for the same load reason target retrieval degraded (hop2 = 0.68 on the target). So "decoy components not retrievable → leans grab" would **misread chain-anchor inconsistency as a grab** — converting a (c)-vs-(b) question into a spurious grab-vs-traverse result.

The instrument that avoids this (C4's measure, C6-sharpened, CS-corrected, adopted):

```text
CROSS-QUERY CHAIN-MEMBERSHIP CONSISTENCY — on the same item, do the model's hop1, hop2,
composite (and, in a future decoy-control study, decoy-query) retrievals stay anchored to
ONE chain identity, or drift across chains?

CORRECTION (CS) — the consistency RATE alone is NOT a clean (c)-detector, and v0.1 wrongly
implied it was. High cross-query consistency is produced by TWO different things:
  - (a) coherent wrong-chain traversal (the model follows one wrong chain across queries), AND
  - a FIXED-TARGET (b) grab (the model always grabs from the SAME salient wrong chain,
    by a non-traversal rule, which is also perfectly consistent in its wrongness).
So "high consistency" CONFLATES (a) with a fixed (b), IN (a)'s FAVOR — the same
metric-satisfied-by-a-confound shape this thread keeps catching. A consistency rate cannot
separate stable anchoring from consistent grabbing.

WHAT ACTUALLY DISCRIMINATES — the per-query CHAIN-IDENTITY PATTERN, which the matrix
(§5 (ii) requirement) records by showing WHICH chain was selected per query:
  - selected chain TRACKS THE QUERY ANCHOR's chain across queries → leans real anchoring
    (and is the only pattern under which an (a)-style reading is even available)
  - selected chain is FIXED regardless of which anchor is queried → leans a non-traversal
    grab from a salient chain (b), NOT traversal — even though it reads as high consistency
  - selected chain SWITCHES per query → chain-anchor inconsistency (c)
The matrix's STRUCTURE is therefore the discriminator, not a richer report format; the
discriminating signal is the pattern (anchor-tracking vs fixed vs switching), never the
consistency rate.
```

## 5. The instrument plan (model-free; the agreed rung 1)

The combined position's next step is **model-free** and builds on existing data. Two components:

**(i) The Entity Address Map** — deterministic metadata from `items_materialized.json`, no model run, no re-score. For every entity token, record (C6's field set):

```text
item_id · entity_token · chain_id · chain_type · role · depth · relation_signature ·
fact_line_index · prompt_position · position_band · query_anchor_position ·
distance_from_query_anchor · distance_from_target_answer · same_chain_as_target ·
same_depth_as_answer · same_relation_signature_as_target
```

Each output then classified positionally: target-consistent · same-decoy-consistent · decoy-switching · role-only/answer-depth-only · relation-signature-matched-wrong-chain · position/proximity-matched · off-frame · abstention.

**CLAIM-RISK CONSTRAINT ON THE MAP (load-bearing, carried from the prior review):** the map is a **deterministic function of (token, layout); it reads outputs.** Two mechanisms that emit the same token at the same position have the same address — so the map **cannot separate (a)/(b)/(c); it describes, it does not adjudicate.** Its subtype field names must be **positional in surface form** (`position_shares_target_relation_labels`), **never mechanistic** (`followed_same_relation_path`) — a precise-looking mechanistic field name is the program's false-confidence-from-precision failure recurring at the naming layer, harder to catch because the precision makes the slide feel earned. The map is the **filing system** for a future separator experiment, not the separator.

**(ii) Three instrument disciplines (C6, CS-corrected, adopted)** that gate interpretation of any consistency measure:

```text
1. COMPONENT LOAD-FLOOR GATE (the most important): a chain-consistency measure is
   uninterpretable on an item until you establish the components were retrievable AT ALL
   on that item. Low consistency is just low retrieval until the floor is cleared. This
   is the (c)-vs-noise floor.
2. CHAIN-CONSISTENCY MATRIX — its structure IS the discriminator (CS), not merely
   non-binary scoring. Beyond avoiding the Paper-1 binary-collapse, the matrix records
   per-item WHICH chain was selected per query, which is the ONLY thing that separates
   fixed-target grabbing (high consistency, but a non-traversal (b) — selected chain fixed
   regardless of anchor) from real anchoring (selected chain tracks the query anchor) from
   switching ((c)). A binary or rate-only score CONFLATES the first two in (a)'s favor (§4
   correction). The matrix must therefore expose the chain-identity pattern, not a
   consistency count.
3. TRACK QUERY-ANCHOR POSITION, not only output-token position — or anchor-proximity
   effects cannot be told from output-proximity effects. (Also required so the matrix can
   test whether the selected chain TRACKS the queried anchor — requirement 2's discriminator.)
```

**Pre-commitment requirement — LOCK-BEFORE-LOOK ON THE AUDIT ITSELF (CS, broadened from v0.1):** the rung-1 audit is byte-only but is locked in the **same sense the pre-registration was**, because analytical fishing in existing data is the same prejudged-result failure as experimental fishing — and "free to recompute" makes it MORE prone, not less, since nothing stops re-slicing until a pattern appears. Before the matrix is computed, pre-declare:

```text
(i)   the matrix PATTERN that would lean (a) traversal-confusion vs (b) non-traversal-grab
      vs (c) chain-anchor inconsistency — referencing patterns (anchor-tracking / fixed /
      switching), NOT consistency cells or rates (§4 correction);
(ii)  the NULL pattern that would force "file §1 and move on" (the positional finding is
      the product and no mechanism lean is supported);
(iii) a ONE-COMPUTATION STOP-RULE — the matrix is computed once against the pre-declared
      patterns; no re-slicing, no added cut, no new pattern defined after look. A second
      pass requires a fresh pre-declared question, exactly as a re-run requires a fresh
      locked prereg.
```

## 6. Opportunity-cost read (the honest recommendation)

```text
§1 (the positional finding) IS the product. The mechanism question is worth AT MOST the
model-free rung-1 audit above, on a closed FAIL — and rung 1 should be framed to test
"is this construction well-posed and is chain-anchoring stable?" not the (a)/(b) clustering
it cannot resolve. If chain-anchoring is unstable under load (or the construction is
under-specified — six structurally-identical chains distinguishable only by an arbitrary
synthetic head token), then heavier rungs on THIS construction measure the construction,
not the model, and the higher-value move is a NEW well-posed construction that makes chain
identity robustly recoverable BEFORE traversal is asked about at all.

The genuinely prior question — which only the Manager can settle — is the goal: is the
objective still a STRESS-ABLE CERTIFIED BASELINE for the seam (→ build the next construction),
or has it become CHARACTERIZING this model's behavior as a finding in itself (→ pursue the
mechanism)? The program's three papers, gate, and prereg discipline were all built on the
former. The two paths are different; the choice should be made explicitly, not defaulted
into by the momentum of a free→cheap→expensive ladder (which structurally de-emphasizes the
"file §1 and stop" option — the honest top level is two choices, stop vs investigate, and
only the second has a ladder).
```

## 7. Boundaries — what must not be claimed (the perimeter)

```text
MUST NOT be claimed from any of this:
  - the model traversed decoy chains
  - the model composed on the wrong chain
  - the model has a (proven) binding failure   [even "binding failure" as a mechanism term
                                                 is out; "observable chain-anchor
                                                 inconsistency" is the behavioral form]
  - the model can / cannot do two-hop composition
  - Claim C progress · Paper B activation · compression evidence · task-family viability
  - the locked FAIL changes (it does not)

ALLOWED (the product):
  - "The FP16 off-map mass is structured: all R6cat outputs are on-page decoy-chain
    entities, mostly at decoy answer-depth positions (right answer-type, wrong address).
    This motivates a model-free entity-address and chain-membership audit to determine
    which observable layout relations predict those outputs."

STANDING:
  - mechanism is out of bounds (behavioral metrology; the method reads behavior, not weights)
  - n=1; substrate-infeasibility does not fire (requires repeated admissible failure)
  - any model-facing study is a NEW lock-before-look prereg, Senior+Manager, never a retrofit
    or a loosened re-run; the separator experiment must be able to come back "grab" or it is
    not a separator
```

## 8. Combined bottom line

```text
SETTLED:    The off-map mass is structured wrong-address selection under load — right
            answer-type, wrong chain. Positional, behavioral, reproduced from bytes.
HYPOTHESES: Two live mechanisms — relation-keyed grab (b), observable chain-anchor
            inconsistency (c) — plus one shared output signature (right-role/wrong-address)
            the current run cannot separate them by. Wrong-chain traversal (a) is least
            supported. None proven.
BLOCKED:    "leans (c)" (the data is consistent with (c), not leaning to it); R4b=0 ruling
            out relation-keyed grab; direct-query 100% as low-load-capability evidence;
            "(d)" as a fourth mechanism (it is the shared observable).
NEXT:       A model-free entity-address map + cross-query chain-membership consistency rule,
            gated on a component load-floor, LOCKED BEFORE LOOK (pre-declared lean-patterns,
            null, and a one-computation stop-rule — analytical fishing is the same failure as
            experimental fishing), with the matrix's per-query CHAIN-IDENTITY PATTERN as the
            discriminator (anchor-tracking vs fixed vs switching — the consistency RATE alone
            conflates real anchoring with fixed-target grabbing in (a)'s favor), and strictly
            positional field names. The map files; it does not adjudicate.
PRIOR:      Whether to pursue mechanism at all vs build the next certifiable construction is
            the Manager's goal-call, made explicitly.
CEILING:    Mechanism is out of bounds; the FAIL stands; nothing here authorizes a run.
```

---

**The one to carry up:** This is the complete claim-risk record of the combined position (v0.2, folding CS's two contributions), authored from the C5 seat as input to the of-record synthesis (which is the New Senior's to assemble — a synthesis authored and reviewed by the same seat has no independent check). The settled product is positional and reproduced from bytes: the FP16 off-map mass is structured wrong-address selection — all 38 R6cat outputs are on-page decoy-chain entities, mostly at decoy answer-depth positions, right answer-type wrong address. The corrected hypothesis space is two live mechanisms (relation-keyed grab; observable chain-anchor inconsistency — the latter relabeled from "binding failure" to keep it behavioral) plus one shared output signature that neither uniquely owns and the current run cannot separate them by; C6's proposed "(d)" is that shared signature, not a fourth mechanism, and listing it as a peer cell double-counts the space. Three over-reads stay blocked — "leans (c)" (the data is consistent with (c), not leaning to it), R4b=0 ruling out relation-keyed grab (it refutes only a crude version and is consistent with a sharper relation-keyed grab), and direct-query 100% as low-load-capability evidence (it is a negative control showing the shortcut is absent). Two CS corrections are folded: the model-free rung-1 audit is itself LOCK-BEFORE-LOOK — pre-declared lean-patterns, a null that forces "file §1 and stop," and a one-computation stop-rule, because analytical fishing in existing data is the same prejudged-result failure as experimental fishing and "free to recompute" makes it more prone; and cross-query chain-membership consistency is NOT a clean detector by rate — high consistency is produced both by coherent traversal AND by a fixed-target grab, so the matrix's per-query CHAIN-IDENTITY PATTERN (anchor-tracking vs fixed vs switching) is the discriminator, not the consistency rate, which conflates them in (a)'s favor. The agreed next step remains model-free: an entity-address map plus the locked consistency rule, gated on a component load-floor, with strictly positional field names — the map files the data, it does not adjudicate mechanism, because it reads outputs and identical outputs have identical addresses. The prior question is the Manager's goal-call: a stress-able certified baseline for the seam (build the next construction) versus characterizing this model's behavior as a finding (pursue mechanism), the program's history pointing at the former. Mechanism stays out of bounds, the FAIL stands, nothing here authorizes a run.

— Contributor 5
