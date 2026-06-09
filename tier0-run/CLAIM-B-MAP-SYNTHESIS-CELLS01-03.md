# Claim B Map Synthesis — Two-Hop Level 1 — Cells01–03

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Per:** Team Lead memo "Authorized Task — Draft Cells01–03 Claim-B Map Synthesis" 2026-06-08
**Source basis:** Cell01/02/03 run packets, map entries, decomposition packet and review,
  EXPERIMENT_LOG.md
**Status:** REVISED 2026-06-08 (pass 4) — §7b symmetric non-identifiability added: pure
  last-position shortcut predicts 0/0/8 step (Group A 0/8, Group B 0/8, Group C 8/8);
  observed 1/6/8 monotone; Group B 6/8 correct with cd2 at last position rules out pure
  shortcut; non-identifiability is symmetric (gradient rules out clean tracing; Group B
  rules out pure shortcut); three-way confound documented (chain-tracing, partial shortcut,
  target-recency); warranted closing added. Evidence record, Paper 2 §4.3, and Fig 3 now
  aligned.
  Previous pass 3: composite-position corollary corrected; group-level table added; Group B
  not position-independent; Group A near-floor = strongest position-independent composite
  evidence; attribution correction.
  Previous pass 2: non_context_return umbrella-class definition + abstention asymmetry;
  endpoint-return / target_chain_wrong_neighbor cross-reference; Cell04 language adjusted.
  Previous pass 1: §5/§6 consistency; absolute-position row split; cd2@pos7 disclosure;
  neg_graph NULL group wording; answer-domain salience PARTIALLY WEAKENED.

---

## §1. Overview and Calibrated Framing

### Calibrated headline (Team Lead–approved)

```
Across Cells01–03, the Two-Hop Level 1 constructibility floor at 3B FP16 shows
recurring, classifiable endpoint-return, abstention, and chain-selection failures
rather than arbitrary failure. Cell03 weakens adjacency/proximity, C-rank, and
absolute position as sufficient explanations while leaving a chain-terminal /
answer-endpoint cue family unresolved.
```

### Three-cell summary

Three constructibility-boundary cells have been completed. All three are Branch 3:
Gate 2 FAIL on hop1 and composite; no cell is stress-eligible. All 288 outputs across
three cells are classified by the locked 8-class failure taxonomy. No new top-level
class was required.

```
Cell    Design                    hop1    hop2    composite  neg_graph  Branch
01      8+8+8 mixed-position      14/24   24/24   18/24      2/24       3
02      all-C_target-last         9/24    23/24   20/24      0/24       3
03      3-group balanced; adj.    6/24    23/24   15/24      6/24       3
        broken (gap=2) all items
```

hop2 is near-ceiling in all three cells (24/24, 23/24, 23/24). The task is not globally
infeasible: B→C single-hop retrieval is fully constructible at 3B FP16. The
constructibility floor is localized to hop1 and composite retrieval under full-chain
context conditions.

### Standing caveat (mandatory)

```
Gate 5 does not close target-token anchoring as a composite shortcut.
Composite ct-return is correct by construction and cannot be made ceiling-bearing
without turning the correct answer into a dummy failure.
Composite target-token anchoring remains tracked through §8 diagnostics, especially
hop1 failures returning ct.
```

---

## §2. Cell01–Cell03 Gate Table

```
Gate    Name                     Cell01          Cell02          Cell03
────────────────────────────────────────────────────────────────────────────────
Gate 0  Manifest schema          PASS            PASS            PASS
        24/24 validate_manifest  24/24           24/24           24/24

Gate 0.5 Token audit             PASS            PASS            PASS
        0 violations,            (reconciled     (run            (run
        j ≥ 0.40 all pairs       2026-06-08)     tokenizer)      tokenizer)

Gate 1  Format adherence
        hop1 FORMAT_PASS         24/24 PASS      24/24 PASS      24/24 PASS
        hop2 FORMAT_PASS         24/24 PASS      23/24 FAIL ★    24/24 PASS
        composite FORMAT_PASS    24/24 PASS      24/24 PASS      24/24 PASS
        neg_graph FORMAT_PASS    24/24 PASS      24/24 PASS      24/24 PASS
        Gate 1 result            PASS            FAIL ← (first)  PASS (first
                                                 1 FSF, i08      clean Gate 1)

Gate 2  FP16 pass rate                                           ← (first)
        hop1                     14/24 FAIL ←    9/24 FAIL       6/24 FAIL
        hop2                     24/24 PASS      23/24 [diag.]   23/24 PASS
        composite                18/24 FAIL      20/24 FAIL      15/24 FAIL
        neg_graph                N/A             N/A             N/A
        Gate 2 result            FAIL ← (first)  FAIL (diag.)    FAIL ← (first)

Gate 3  Op. fidelity (diag.)
        wrong_chain (≤ 3/24)     4/24 FAIL       4/24 FAIL       7/24 FAIL
        wrong_neighbor (≤ 3/24)  0/24 PASS       0/24 PASS       0/24 PASS
        stopped_short (≤ 3/24)   1/24 PASS       0/24 PASS       0/24 PASS
        Gate 3 result            FAIL (diag.)    FAIL (diag.)    FAIL (diag.)

Gate 4a Classifier reliability
        UNCLASSIFIED_OFF_FRAME   0/96 PASS       0/96 PASS       4/96 TRIGGERED
                                                                 (watch; hop1
                                                                  only; attribut.)
        Gate 4a result           PASS (diag.)    PASS (diag.)    TRIGGERED (diag.)

Gate 5  Dummy ceiling
        max_det (ceiling-bear.)  8/24 ≤ 9/24     0/24 ≤ 9/24     8/24 ≤ 9/24
        Gate 5 result            PASS            PASS*           PASS
                                                 (* coverage gap:
                                                  always_return_
                                                  second_C not
                                                  tested; closed
                                                  in Cell03)

Gate 6  Stress eligibility       NOT ELIGIBLE    NOT ELIGIBLE    NOT ELIGIBLE
────────────────────────────────────────────────────────────────────────────────

★ Cell02 Gate 1 failure: hop2 FORMAT_PASS 23/24 (item i08 — FORMAT_COMPLIANCE_LOSS;
  model reproduced full fact sentence; semantically correct; isolated, construction-
  orthogonal). See CELL02-HOP2-FSF-INSPECTION-TWOHOP-L1.md. Gate 2 metrics for
  Cell02 are diagnostic, not binding.

Cell03 scoring note: Cell03 used amended scorer sha256:b65c6803... (adds second_C,
  third_C ceiling-bearing + always_return_ct reference-only). Cell01/02 used
  sha256:060afad9... Cell01/02 gate dispositions are unchanged; amendment not
  retroactive to model outputs.
```

---

## §3. Score Table Across Cells

```
query_type     Cell01      Cell02      Cell03      Trend
────────────────────────────────────────────────────────────
hop1           14/24       9/24        6/24        declining
hop2           24/24       23/24       23/24       near-ceiling stable
composite      18/24       20/24       15/24       non-monotone
neg_graph      2/24        0/24        6/24        low; Cell03 Group A
────────────────────────────────────────────────────────────
```

**hop1 trend (14 → 9 → 6):** Declining across cells. Each cell introduced a new
intervention targeting ct-anchoring (position change in Cell02; adjacency break in
Cell03). Both reduced correct hop1 (or changed the failure profile) without restoring
the floor. Cell03's Group A (0/8 hop1 correct) and Group C filler-return artifacts
contributed to the steeper Cell03 drop.

**hop2 near-ceiling (24/24, 23/24, 23/24):** Stable across design changes. B→C
single-hop retrieval is not the load-bearing failure axis. The Cell02 23/24 is
Gate-1-contaminated (1 FORMAT_COMPLIANCE_LOSS); semantically correct.

**composite non-monotone (18 → 20 → 15):** Cell02 slight improvement: all-C_target-last
places ct adjacent to hop2, which may help composite by making the target chain
terminal more proximal for the A→B→C query. Cell03 regression: breaking adjacency
increases wrong_chain selection (4 → 7) as the last-C-endpoint preference fires more
often when ct is not at the last position.

**neg_graph low (2, 0, 6):** Cell01 had 2/24 correct NULL, both in C_target-first group
(weakest hop1 group — consistent with reduced endpoint attraction when fewer chain facts
are prominent). Cell02 had 0/24. Cell03 improved to 6/24: 5 from Group A (5/8 correct
NULL — after hop2@pos3 removal, the target chain has only one visible fact, reducing
endpoint attraction pressure) and 1 from Group C (1/8 correct NULL). Group B remained
0/8 correct NULL (both decoy chains fully visible with C-endpoints). The 6/24 total is
not concentrated in one group; the group breakdown is A: 5/8, B: 0/8, C: 1/8. Overall,
abstention calibration remains fragile across all three cells.

---

## §4. Failure-Class Recurrence Table

Counts over 96 outputs per cell. Denominator = 96 (24 items × 4 query types).

```
Failure class              Cell01   Cell02   Cell03   All-3?
────────────────────────────────────────────────────────────────
correct                    58       52       50       —
format_scaffold_failure    0        1        0        NO  (Cell02 only)
non_context_return         8        3        9        YES ✓
correct_chain_stopped_short 1       0        0        NO  (Cell01 only)
wrong_chain_selection      15       28       21       YES ✓
target_chain_wrong_neighbor 14      12       12       YES ✓
anchor_echo                0        0        0        —
UNCLASSIFIED_OFF_FRAME     0        0        4        NO  (Cell03 only; attributed)
────────────────────────────────────────────────────────────────
total                      96       96       96
```

**Three failure classes recur across all three cells:**

1. **non_context_return (NULL)** — 8, 3, 9 total; primarily hop1. Model abstains
   rather than retrieving bt. Peaks in Cell01 (C_target-first group, 6/8 NULL) and
   Cell03 (Group A, 6/8 NULL — neighbor interposition after hop1 at pos1).

2. **wrong_chain_selection** — 15, 28, 21 total; primarily composite and neg_graph.
   Model selects a decoy chain C-endpoint rather than the target chain endpoint.
   Cell02 peak (28) reflects 23/24 neg_graph wrong_chain under all-C_target-last;
   decoy chains are fully represented and visible.

3. **target_chain_wrong_neighbor** — 14, 12, 12 total; primarily hop1 (ct-anchoring)
   and neg_graph (B-endpoint return in Cell03). Model returns the wrong node within
   the correct chain — ct instead of bt on hop1; bt instead of NULL on neg_graph.

**Behavioral description of the three-class core:**
The constructibility floor is not random. It maps onto three stable, classifiable
behavioral patterns: (1) abstention / chain-navigation failure on hop1 (NULL returns),
(2) chain-selection failure under multi-chain context (decoy endpoint selection), and
(3) chain-terminal / wrong-node return (ct-anchoring on hop1; B-terminal return on
neg_graph when chain is truncated).

**Classes absent or incident-level:**
- format_scaffold_failure (0, 1, 0): isolated FORMAT_COMPLIANCE_LOSS in Cell02/i08.
  Not a structural floor contributor.
- correct_chain_stopped_short (1, 0, 0): isolated Cell01/i22 stopped_short on
  composite. Not recurring.
- anchor_echo: 0 across all cells. No evidence of anchor-token dominance.
- UNCLASSIFIED_OFF_FRAME (0, 0, 4): Cell03 neighbor-proximity artifacts (3 filler
  returns from Group C + 1 A_decoy_2 return from Group B). Attributable to a single
  structural cause; not expanding the taxonomy.

---

## §5. Cue-Status Table

### Candidate cues entering Cell03

At the end of Cell02, four candidate cues were simultaneously confounded in ct:

```
Cue                    Definition                        Cell02 confounded?
─────────────────────────────────────────────────────────────────────────────
(a) Adjacency/proximity  hop2_fact immediately after hop1   YES (gap=1 all 24)
                         (gap=1; hop1@pos5, ct@pos6)
(b) Absolute position    ct fixed at context position 6     YES (pos 6 all 24)
                         for all 24 items
(c) C-rank slot          ct fixed as second_C               YES (second_C all 24)
                         for all 24 items
(d) Answer-domain        ct is the correct composite        YES (all 3 cells;
    salience             answer in all cells                 uncontrolled)
(d2) Chain-terminal      ct is the terminal node of the     YES (all 3 cells;
     endpoint            target chain in all cells          structural)
```

### Cell03 manipulation and results

Cell03 design:
- Broke adjacency in ALL 24 items: neighbor fact interposed between hop1 and hop2
  (gap=2 uniformly).
- Balanced absolute position: ct at pos3 (Group A, 8 items), pos5 (Group B, 8 items),
  pos7 (Group C, 8 items).
- Balanced C-rank: ct = first_C (Group A), second_C (Group B), third_C/last_C (Group C).
- Answer-domain salience: UNCONTROLLED (ct is always the correct composite answer).
- Chain-terminal role: UNCONTROLLED (ct is always the target chain terminal).

### Cue-status dispositions after Cell03

```
Cue                       Cell03 result                 Disposition
────────────────────────────────────────────────────────────────────────────
(a) Adjacency/proximity   hop1 ct-anchoring:            WEAKENED — not eliminated.
                          11/24 → 6/24. Breaking         Adjacency contributes but
                          adjacency reduces ct-           is not sufficient alone.
                          anchoring but does not
                          eliminate it. Residual
                          6/24 persists under gap=2.

(b1) Absolute position    hop1 ct-anchoring: 2/8 per    WEAKENED — not sufficient
     (hop1 ct-anchoring)  group (Group A pos3: 2;        for hop1 ct-anchoring.
                          Group B pos5: 2; Group C       ct-anchoring is uniform
                          pos7: 2). Position-invariant.  across ct at pos3/pos5/pos7.
                                                         Scope: hop1 only.

(b2) Absolute position /  composite wrong_chain: ALL     ACTIVE — construction-fixed
     last-position        7 returns = cd2@pos7.          regularity in Groups A and B.
     (composite           cd2 is construction-fixed at   Cell03 balances target chain
     wrong_chain)         pos7 in Groups A and B.        ct position/C-rank but does
                          Group C: cd2 at pos4, ct at    NOT independently balance
                          pos7 → model returns ct         decoy-chain endpoint
                          correctly (8/8).               positions. The last-C/
                                                         cd2@pos7 preference is
                                                         behaviorally active but
                                                         cannot be fully separated
                                                         from the construction-fixed
                                                         decoy placement in this cell.

(c) C-rank slot           hop1 ct-anchoring: 2/8 per    WEAKENED — not sufficient
                          group (first_C: 2; second_C:   for hop1 ct-anchoring.
                          2; third_C: 2). Rank-          ct-anchoring is uniform
                          invariant.                     across all three C-rank
                                                         positions. Scope: hop1 only.

(d) Answer-domain         ct absent from neg_graph       PARTIALLY WEAKENED.
    salience              context; 0/18 intrusions        0/18 neg_graph intrusions
                          returned ct. On hop1, ct        returned ct. This weakens
                          present: 6/24 returned ct.     answer-domain salience as a
                                                         context-independent attractor:
                                                         the model does not return ct
                                                         abstractly when ct is not
                                                         visible. The residual
                                                         question — whether hop1
                                                         ct-anchoring (when ct IS
                                                         visible) is driven by ct's
                                                         answer-role or chain-terminal
                                                         role — remains unresolved
                                                         within the current design.
                                                         Cannot separate from (d2)
                                                         without task redesign.

(d2) Chain-terminal       ct is always target chain      UNRESOLVED — structural in
     endpoint             terminal in all 3 cells.       all current cells. ct does
                          Cannot be disentangled from    two jobs: correct composite
                          (d) without constructing        answer AND chain terminal.
                          items where the composite       The answer-role vs chain-
                          answer is NOT the chain         terminal distinction remains
                          terminal.                       unresolved in the current L1
                                                         design. A future design could
                                                         attempt to address it, but
                                                         Cell04 is not authorized and
                                                         may require a different task
                                                         geometry.
```

### Residual cue family

The surviving unresolved candidate is the **chain-terminal / answer-endpoint cue family**:
ct simultaneously (a) terminates the target chain and (b) is the correct composite
answer. Answer-domain salience as a context-independent attractor is weakened by the
neg_graph evidence (0/18 ct returns when ct is absent); the model cannot return ct when
it is not visible. The residual is: when ct IS visible (hop1 queries), the 6/24
ct-anchoring rate cannot be attributed to either role alone — both chain-terminal role
and visible-token answer-role are simultaneously satisfied. Cell03 cannot separate them.

The calibrated label for the residual: **endpoint-return / chain-terminal-answer attraction.**

**Construction regularity note (composite):** The composite wrong_chain pattern (cd2@pos7,
all 7 returns) is concentrated at a construction-fixed position. Cell03 balances the
target chain ct position across groups but does not balance decoy-chain endpoint
positions. cd2 is fixed at pos7 in Groups A and B. The behavioral last-C preference is
real and classifiable, but its independence from the cd2@pos7 construction regularity
cannot be confirmed within this cell. This is disclosed as a residual construction
regularity, not a disqualification: composite wrong_chain remains valid
constructibility-boundary evidence.

---

## §6. §8 Endpoint-Intrusion Summary Across Cells

### §6.1 Hop1 ct-anchoring (target_chain_wrong_neighbor on hop1)

**Labeling cross-reference:** The §8 diagnostic term "endpoint-return" (or
"ct-anchoring") describes the observed behavior: model returned a chain endpoint
(ct) where a chain intermediate (bt) was requested. The §4 taxonomy class for this
specific case is `target_chain_wrong_neighbor` — model returned the wrong node
within the correct chain. These are not separate classes: "endpoint-return" is a
behavioral description; `target_chain_wrong_neighbor` is the scorer classification.

```
Cell    hop1 ct-anchoring   Conditions                    Notes
─────────────────────────────────────────────────────────────────────────────
Cell01  3/24                Mixed positions (pos2/4/6);    Only in C_target-first
                             no neighbor interposition      (i06, i08) and
                                                           C_target-middle (i15).
                                                           All 3 returned ct.

Cell02  11/24               All adjacency (gap=1);         73% of hop1 failures.
                             ct at pos6 (second_C);         All 11: hop1@pos5,
                             all 4 cues confounded          ct@pos6, adjacent.

Cell03  6/24                Adjacency broken (gap=2);      Uniform 2/8 per group:
                             ct balanced pos3/5/7;          Group A (ct=first_C): 2
                             C-rank balanced 1st/2nd/3rd    Group B (ct=second_C): 2
                                                           Group C (ct=third_C): 2
```

**Cross-cell pattern:** ct-anchoring rate peaked when all four cues were confounded
(Cell02: 11/24), was attenuated by breaking adjacency and balancing controls (Cell03:
6/24), but was not eliminated. The residual 2/8 per group is rank-invariant and
position-invariant, pointing to the chain-terminal / answer-endpoint cue family as
the remaining driver.

### §6.2 Negative_graph endpoint intrusion

```
Cell    correct NULL   intrusion   dominant intrusion type
─────────────────────────────────────────────────────────────────────────────
Cell01  2/24 (0.083)   22/24       wrong_chain (11) + target_wrong_neigh (11)
                                   Mixed C-endpoint and B-endpoint returns.
                                   C_target-first group produced both correct NULLs.

Cell02  0/24 (0.000)   24/24       wrong_chain (23) + target_wrong_neigh (1)
                                   Near-total C-endpoint intrusion.
                                   ct absent from context; decoy C-endpoints visible.

Cell03  6/24 (0.250)   18/24       wrong_chain (12) + target_wrong_neigh (6)
                                   Group breakdown:
                                     Group A: 5/8 NULL (best); 3/8 C-endpoint intrusion
                                     Group B: 0/8 NULL; 8/8 intrusion
                                     Group C: 1/8 NULL; 7/8 intrusion (5 B-endpoint)
```

**Key finding (Cell03):** 0/18 intrusions returned ct. ct is contained in the hop2_fact
which is removed for neg_graph; ct is therefore absent from context. The intrusion
pattern is NOT ct-specific / NOT answer-domain-salience driven. Intrusions return the
last-visible C-endpoint (10/18) or the target B-endpoint when hop2 is removed and bt
is the last visible target-chain token (6/18, Group C). This is pure
endpoint-emission / chain-terminal behavior.

Implication for §6.1: hop1 ct-anchoring requires ct to be visible in context (ct is in
hop2_fact which IS present on hop1 queries). The convergence of ct-anchoring on hop1
(where ct is visible) with 0 ct returns on neg_graph (where ct is absent) confirms
that the residual ct-anchoring is token-visibility-dependent, not driven by abstract
answer-domain salience decoupled from token presence.

### §6.3 Composite wrong_chain

```
Cell    wrong_chain   Token returned              Position pattern
───────────────────────────────────────────────────────────────────────────
Cell01  4/24          decoy C-endpoints           3/4 in C_target-first;
                      (various)                   consistent per-item distractor token
                                                 across composite and neg_graph

Cell02  4/24          decoy C-endpoints           ct at pos6 (not last); cd2 at pos7
                      cd2 (pos7) dominant?        (last). Same 4/24 rate as Cell01.

Cell03  7/24          cd2 at pos7 exclusively     ALL 7 returns: cd2 at position 7.
                                                 Last-position / last-C preference.
                                                 Gradient: Group A 5/8 wrong, Group B
                                                 2/8, Group C 0/8 — exactly matches ct
                                                 distance from last position.
```

**Cross-cell pattern:** Composite wrong_chain rate has been stable to increasing
(4, 4, 7). The Cell01/02 rate (4/24) appears to reflect a structural floor for
this token pool geometry. Cell03 increase to 7/24 is explained by the balanced design
placing ct at non-last positions for 16 items (Groups A/B), where the last-C-endpoint
preference fires wrong (cd2 at pos7 instead of ct at pos3 or pos5). In Group C
(ct=last), the same preference fires correctly (8/8 composite correct). Not new
fragility — same last-C mechanism, more adversarial layout.

**Construction-fixed disclosure (cd2@pos7):** In Cell03 Groups A and B, cd2 is at
pos7 by construction — it is the last context fact for those groups. Cell03 balances
the target chain ct position and C-rank across groups but does not independently
balance decoy-chain endpoint positions. Therefore, composite wrong_chain in Cell03
reflects a last-C / cd2@pos7 pattern that cannot be fully separated from the
construction-fixed decoy placement. The behavioral last-position preference is
classifiable and supported by the Group C contrast (cd2 moves to pos4 in Group C;
ct is at pos7; model returns ct correctly), but the independence of the preference
from the specific cd2@pos7 geometry cannot be confirmed within this cell. This is
a residual construction regularity, not a disqualification of the wrong_chain
finding as constructibility-boundary evidence.

---

## §7. Cell03 Decomposition Summaries

### §7a. Hop1 Failure Decomposition

```
Group   correct   NULL    ct-anchored   UNCLASSIFIED   wrong_chain
A       0/8       6       2             0              0
B       4/8       0       2             1              1
C       2/8       1       2             3              0
total   6/24      7       6             4              1
```

**Group A complete failure (0/8):** The neighbor fact is interposed immediately after
hop1 at pos1 (pos1: hop1, pos2: neighbor, pos3: hop2/ct). With no prior context to
ground the query, 6/8 items returned NULL (abstention) and 2/8 returned ct (skipped
to pos3). Group A is catastrophically disrupted by having the neighbor interposed
between hop1 and its only neighboring target-chain token before the decoy chains.

**Group C filler-return artifacts (3/8 UNCLASSIFIED):** Neighbor fact at pos6 is
immediately adjacent to hop1 at pos5. Three Group C items returned the filler token
(fl, left side of `fl holds cn`). Model treats the neighbor line as a chain
continuation and returns its subject token. A neighbor-proximity artifact.

**ct-anchoring (2/8 per group, uniform):** All 6 ct-anchored returns are in pairs
across groups, regardless of ct's position (pos3, pos5, pos7) or C-rank. This is the
key evidence against position or C-rank as sufficient drivers of ct-anchoring.

**No cn returns:** Zero hop1 failures returned the neighbor token (cn) itself.
The 3 UNCLASSIFIED Group C returns retrieved fl (the left-side subject of the
neighbor line), not cn (the right-side object).

**Hop1 failure taxonomy mapping (§4 classes):**

```
Hop1 decomposition         Count   §4 taxonomy class                Notes
─────────────────────────────────────────────────────────────────────────────────
NULL (non_context_return)  7       non_context_return               All 7 are
                                                                    correct-class
                                                                    classifications:
                                                                    model returned
                                                                    NULL on a
                                                                    positive query.

ct-anchored                6       target_chain_wrong_neighbor      Returned ct
  (returned ct)                    (model returned the wrong        (answer_C role)
                                   node within the target chain:    instead of bt
                                   ct instead of bt)                (hop1_B role).

UNCLASSIFIED               4       UNCLASSIFIED_OFF_FRAME           Returned in-context
  (3 filler fl,                    (tokens with ROLE_INERT_         tokens whose roles
   1 ad2 ZGUPE)                    FILLER or ROLE_OTHER_CONTEXT     are not addressed
                                   — outside the 8 classification   by the 8 rules.
                                   rules by design)                 All 4 attributable;
                                                                    no taxonomy gap.

wrong-chain                1       wrong_chain_selection            i10 returned ad2
  (returned ad2)                   (model returned a decoy chain    (ROLE_OTHER_CONTEXT
                                   token rather than the target)    for decoy_chain_2
                                                                    A-object).
─────────────────────────────────────────────────────────────────────────────────
total failures             18      (correct = 6; all 24 accounted)
```

All 18 hop1 failures map cleanly onto existing §4 top-level taxonomy classes.
No output falls outside the taxonomy. The 4 UNCLASSIFIED_OFF_FRAME cases are
architecturally correct placements, not taxonomy gaps: the classifier returns these
tokens but the correct structural label is that they are in-context tokens with roles
not addressed by the 8 classification rules.

**non_context_return umbrella-class definition:** In this taxonomy, `non_context_return`
is an umbrella class for responses that are not in-context endpoint tokens as expected
by the query. For interpretive clarity, this synthesis sub-tags two conceptually
distinct subtypes:

```
non_context_return sub-tags:
  NULL / abstention (7 hop1 instances; 2 composite instances across 3 cells):
    Model returns NULL or NO_LINK. On hop1 and composite, this is incorrect abstention.
    On negative_graph, NULL is the correct response. The 7 hop1 NULL returns in Cell03
    are incorrect abstention: the model withholds when it should retrieve bt.

  off-context-token / UNCLASSIFIED_OFF_FRAME (4 Cell03 hop1 instances):
    Model returns an in-context token with a role outside the 8 classification rules.
    This is a separate top-level taxonomy class (class 8), NOT a subtype of
    non_context_return. Included here for conceptual contrast only.
```

**Abstention asymmetry thread:** These two sub-tags define opposite failure modes that
must not be collapsed. hop1 shows incorrect abstention (7 NULL returns — model abstains
when it should retrieve bt). neg_graph shows failure to abstain (18 intrusions — model
emits an endpoint when it should return NULL). The model both over-abstains on hop1 and
under-abstains on neg_graph. This abstention asymmetry is a live characterization thread
and should be preserved in any Claim B Track A framing.

### §7b. Composite Wrong_Chain Decomposition

All 7 composite wrong_chain returns = cd2 at context position 7 (last position in
Groups A and B):

```
item_id            group   ct_rank    returned   ret_pos   ct_pos
i01, i02, i03,     A       first_C    cd2         7         3
i05, i08
i09, i11           B       second_C   cd2         7         5
```

Composite accuracy gradient: Group C 8/8 → Group B 6/8 → Group A 1/8.

This is a last-position / last-C preference on composite. When ct is at the last
context position (Group C), the preference fires correctly. When ct is not at the
last position (Groups A/B), it fires wrong (returns cd2 at pos7 instead). No
Group C wrong_chain. No B-endpoint wrong_chain. Single-mechanism failure.

**Group-level composite correctness (pass 3 correction):**

```
Group   composite correct   ct position
A       1/8                 pos3 (first_C)
B       6/8                 pos5 (second_C)
C       8/8                 pos7 (third_C / last_C)
total   15/24
```

**Composite-position corollary:** Composite correctness increases monotonically with ct
absolute position: Group A 1/8 at ct@pos3, Group B 6/8 at ct@pos5, Group C 8/8 at
ct@pos7. This is a monotone gradient consistent with last-position pull — as ct approaches
the last context position, composite correctness rises. Group C 8/8 cannot be distinguished
from last-C shortcut survival (ct IS at pos7). Group B 6/8 is mid-gradient and likewise
consistent with partial last-position shortcut survival — it is not clean position-independent
chain-tracing evidence.

Therefore, the surface composite score of 15/24 should not be read as 15/24 clean chain
tracing. Some correct composite outputs are consistent with positional shortcut survival.
The strongest position-independent composite evidence is Group A, where ct is farthest from
last position and composite correctness is near floor (1/8 correct; 5/8 wrong_chain to
cd2@pos7). Group A's near-floor rate confirms that when the last-position shortcut does not
coincide with ct, composite retrieval largely fails.

This strengthens Claim B rather than weakening it: the constructibility floor is structured
and position-governed, and correctness alone does not establish that the intended operation
was performed.

**Pure-shortcut prediction vs observed (pass 4):** A pure last-position shortcut (always
return the token at context position 7) predicts a step function across groups:

```
Group   pure-shortcut prediction   pos7 token   predicted correct
A       return cd2 (pos7)          cd2           0/8
B       return cd2 (pos7)          cd2           0/8
C       return ct  (pos7)          ct            8/8
                                                 ────
                                   predicted:    0/0/8 step
                                   observed:     1/6/8 monotone
```

Group B's 6 correct returns — ct at pos5, cd2 still at last position — are exactly what
a pure last-position shortcut cannot produce. The pure shortcut is ruled out by the
Group B result.

**Symmetric non-identifiability:** The non-identifiability runs in both directions. The
monotone gradient and Group A near-floor rule out reading 15/24 as clean chain-tracing.
Group B 6/8 correct despite cd2 occupying last position rules out pure positional shortcut.
The instrument cannot separate the three residual explanations for the Group B result:
(1) genuine chain-tracing, (2) partial last-position shortcut active on some items but
not others, or (3) target-recency — ct at pos5 being accessible by recency rather than
by chain-following. These three are not distinguishable within the current cell design.

Warranted closing: correctness does not establish that the intended operation was
performed — nor does the gradient establish that it was not.

### §7c. Negative_Graph Endpoint-Intrusion Decomposition

**0/18 ct returns:** ct is in the hop2_fact which is removed for neg_graph. ct is
absent from the rendered context. The intrusion pattern is NOT ct-specific.

```
Intrusion type            count   mechanism
C-endpoint (decoy)        10/18   9/10 = last-visible C-endpoint in truncated context
Target B-endpoint (bt)    6/18    Group C: hop2 removed → bt@pos5 is last target token;
                                  model follows hop1 to bt rather than returning NULL
B-decoy intermediate      2/18    Group B: near decoy chain material at pos6
```

Group asymmetry after hop2 removal:
- Group A: target chain has 1 visible fact (hop1@pos1); decoy chains visible at
  pos4–7; 5/8 NULL (low endpoint-attraction pressure with sparse target chain).
- Group B: both decoy chains fully visible with C-endpoints; 0/8 NULL (model always
  emits an endpoint when full chains are present).
- Group C: hop2@pos7 removed; bt@pos5 is the last visible target-chain token; 5/8
  returned bt (model follows hop1 → bt, chain-terminal emission for the surviving hop).

---

## §8. Taxonomy Saturation Assessment

```
Cell    n_outputs   UNCLASSIFIED_OFF_FRAME   rate    watch trigger (> 2%)
──────────────────────────────────────────────────────────────────────────────
Cell01  96          0                        0.000   NO
Cell02  96          0                        0.000   NO
Cell03  96          4 (hop1 only)            0.042   YES (hop1; attributable)

Three-cell total: 288 outputs; 4 UNCLASSIFIED (1.4%)
```

All 4 Cell03 UNCLASSIFIED cases are attributed to a single structural cause:
neighbor-proximity artifact on hop1 Group C (3 filler returns from Group C items
where neighbor immediately follows hop1 at pos5) and 1 A_decoy_2 return from Group B
(i10, isolated). No second structural cause, no pattern in other query types, no
spread to composite or negative_graph.

**Taxonomy saturation conclusion:**

The existing 8-class taxonomy is adequate for the three-cell evidence base. No new
top-level class was required. The three core recurring classes (non_context_return,
wrong_chain_selection, target_chain_wrong_neighbor) cover the constructibility floor
consistently across all three cells with no residual ambiguity at the class level.

The failure surface is not expanding. UNCLASSIFIED_OFF_FRAME is at 1.4% over 288
outputs, with all cases attributable. The taxonomy supports a stable, mappable
characterization of the Claim B floor.

If Cell04 is pursued, neighbor-proximity artifacts (if they recur) may warrant a
sub-category annotation under UNCLASSIFIED_OFF_FRAME, but would not require a new
top-level class.

---

## §9. Synthesis Questions

### Q1. What failure classes recur across Cells01–03?

Three failure classes are non-zero in all three cells:

```
1. non_context_return (NULL):
   Cell01: 8/96   Cell02: 3/96   Cell03: 9/96
   Primary locus: hop1 (model abstains rather than retrieving bt).
   Driver: context geometry that disrupts hop1 retrieval (C_target-first NULL
   clustering in Cell01; Group A NULL concentration in Cell03 under neighbor
   interposition at pos1/pos2).

2. wrong_chain_selection:
   Cell01: 15/96  Cell02: 28/96  Cell03: 21/96
   Primary locus: composite (decoy C-endpoint selection) and neg_graph
   (endpoint-emission on truncated context).
   Driver: last-C-endpoint preference under multi-chain context (Cell03 confirmed
   single-mechanism: all 7 composite wrong_chain = cd2 at pos7).

3. target_chain_wrong_neighbor:
   Cell01: 14/96  Cell02: 12/96  Cell03: 12/96
   Primary locus: hop1 (ct-anchoring — model returns ct instead of bt) and
   neg_graph (B-endpoint emission when hop2 removed).
   Driver on hop1: chain-terminal / answer-endpoint cue family (residual after
   adjacency, position, and C-rank are individually weakened). Driver on neg_graph:
   chain-terminal emission of the surviving hop (bt when ct is removed).
```

These three classes define the stable constructibility floor for Two-Hop Level 1
at 3B FP16 under the current construction family.

---

### Q2. Which cues have been weakened as sufficient explanations?

**Position/ordering hypothesis (Cell02): REJECTED as a sufficient recovery lever.**
All-C_target-last manipulation did not restore hop1 floor. Cell01's C_target-last
subgroup (8/8) was item-specific or interaction-dependent, not a pure ordering effect.
Clarification: position/ordering is rejected as a sufficient explanation for the
observed constructibility floor across Cells01–03, not rejected as a factor that can
shape specific failure modes. The Cell03 composite gradient (Group A 1/8 → Group B
6/8 → Group C 8/8 correct composite) demonstrates that absolute position actively
shapes composite wrong_chain rates — position/ordering influences how the last-C
preference fires, even though manipulating ordering did not resolve the floor.

**Absolute position (Cell03): WEAKENED as sufficient — scoped to hop1 ct-anchoring.**
For hop1 ct-anchoring: 2/8 per group across ct at pos3, pos5, and pos7. Absolute
position alone does not determine whether hop1 ct-anchoring fires.
Note: absolute position / last-position IS active for composite wrong_chain (cd2@pos7
all 7 returns — see §5 row b2 and §6.3). The weakening applies specifically to hop1
ct-anchoring, not to the composite failure surface.

**C-rank slot (Cell03): WEAKENED as sufficient — scoped to hop1 ct-anchoring.**
For hop1 ct-anchoring: 2/8 per group across first_C, second_C, and third_C.
C-rank position alone does not determine whether hop1 ct-anchoring fires.

**Adjacency/proximity (Cell03): WEAKENED but contributing.**
Breaking adjacency (gap=2, neighbor interposed) reduced ct-anchoring from 11/24 to
6/24. Not eliminated. Adjacency is a contributing factor — closer proximity increases
ct-anchoring rate — but breaking it is not sufficient to eliminate the behavior.

---

### Q3. Which cues remain confounded or unresolved?

**Chain-terminal / answer-endpoint cue family: UNRESOLVED.**

In all three cells, ct simultaneously plays two roles:
  (a) the terminal endpoint of the target chain (structural — ct is always C_object
      of the target chain's hop2_fact)
  (b) the correct composite answer (definitional — composite query expects ct)

These two roles are inseparable in the current cell design. Cell03 cannot determine
whether the residual 6/24 ct-anchoring is driven by:
  - ct's role as chain terminal (model emits chain endpoints)
  - ct's role as the answer token (answer-domain salience)
  - both simultaneously

The neg_graph evidence (0/18 ct returns when ct is absent from context) confirms
that ct-anchoring requires ct to be visible. It does not resolve whether the
attraction is to the chain-terminal position or the answer-token identity, because
both are always co-present on hop1 queries.

**Token-identity interaction: RESIDUAL UNCERTAINTY.**
Individual token properties may interact with context geometry. The rotation design
(C_DECOYS_1 = +8 rotation, C_DECOYS_2 = +16 rotation) means each item's ct appears
as a decoy in other items — a controlled near-miss structure. No token-construction
violation was found (Gate 0.5 PASS all cells). Token-identity effects, if present,
would operate within the confines of the verified token pool.

---

### Q4. Does the floor appear mappable or still expanding?

**The floor appears increasingly mappable.**

Evidence:
- 288 outputs across 3 cells; all classified; no taxonomy expansion required.
- Three core failure classes are consistent and behaviorally describable across all cells.
- Each cell has added a cue-disentanglement result (position/ordering NOT SUPPORTED in
  Cell02; adjacency/position/C-rank weakened but chain-terminal/answer-endpoint residual
  in Cell03).
- The residual failure pattern (6/24 ct-anchoring, last-C-endpoint preference, abstention
  under reduced chain density) is structurally explicable.

**The floor is not fully mapped:**
- The chain-terminal / answer-endpoint cue family remains unresolved.
- The residual 6/24 ct-anchoring under broken adjacency + balanced controls is a
  stable measurement but its cue attribution is incomplete.
- A future design (not currently authorized) could target cue separation, but would
  require a different task geometry and is not guaranteed to resolve the attribution.

**Interim mappability statement:**
The floor appears mappable in the sense that it maps onto a finite, stable, classifiable
failure surface rather than expanding arbitrarily. The failure surface is not arbitrary —
it is structurally coherent and theoretically interpretable as endpoint-return / chain-
terminal-answer attraction. The open question is cue attribution within that family,
not whether the floor is classifiable.

---

### Q5. Is Claim B now a Track A paper candidate?

**Provisional YES — Claim B supports Track A framing at the three-cell level.**

The three-cell evidence base supports the following Track A claim:

```
Two-Hop Level 1 constructibility at 3B FP16 (Qwen2.5-3B-Instruct) shows a recurring,
classifiable failure floor rather than arbitrary failure. Under progressively
strengthened positional controls:
  - hop2 retrieval is near-ceiling across all cells (24/24, 23/24, 23/24), establishing
    that B→C single-hop retrieval is constructible at this scale.
  - hop1 and composite retrieval do not reach the constructibility threshold (≥21/24)
    in any cell.
  - The dominant failure patterns (NULL abstention on hop1, wrong-chain selection on
    composite, ct-anchoring on hop1) recur across cells with a stable failure taxonomy.
  - Three individual cue hypotheses have been sequentially weakened: position/ordering
    (Cell02), absolute position (Cell03), C-rank slot (Cell03), adjacency/proximity
    (Cell03 partially). A chain-terminal / answer-endpoint cue family remains as the
    unresolved residual.
  - endpoint-return behavior persists under corrected positional controls.
```

Claim B as currently stated (candidate convergence framing, not mechanism claim) is
supportable from the three-cell evidence base. Cell04 would strengthen but not unlock
the claim — the core finding (recurring classifiable floor; endpoint-return behavior
persists under corrected controls) is established.

**What Claim B currently supports (Track A draft language):**

```
SUPPORTED:
  endpoint-return behavior persists under corrected positional controls
  failure surface appears increasingly mappable
  answer-domain salience remains a candidate subcue (unresolved, not refuted)
  chain-terminal / answer-endpoint cue family remains unresolved

NOT SUPPORTED:
  answer-domain salience proven or isolated
  mechanism established
  adjacency/proximity is the causal cue
  any mechanism beyond observational pattern description
  Claim C tested (no stress-eligible cell)
  Track B (compression not measured)
```

---

### Q6. What exact question would Cell04 answer that the synthesis cannot?

**Cell04 target question:**

"Does ct-anchoring on hop1 persist when the correct composite answer is NOT also the
terminal endpoint of the target chain?"

This requires constructing items in which the hop2_fact terminates at a node that is
NOT ct — i.e., the correct composite answer (the thing the A→B→C query asks for) is
at a non-terminal position, while a different token occupies the chain-terminal
position. Under this design, a model driven by chain-terminal emission (endpoint-return
regardless of answer-domain salience) would return the chain terminal (wrong answer),
while a model driven by answer-domain salience would return ct (correct answer).

**What Cell04 would establish:**
- If ct-anchoring on hop1 disappears when ct is not the chain terminal: answer-domain
  salience is the driver; the model is tracking the answer token, not the chain endpoint.
- If ct-anchoring on hop1 persists even when ct is not at the chain terminal:
  the model is tracking some property of ct independent of its endpoint role.
- If the terminal token (not ct) is returned on hop1: chain-terminal emission is the
  driver.

**What Cell04 cannot establish:**
- Mechanism (behavioral evidence cannot establish mechanism)
- Generalization beyond this task construction family
- Claim C (stress eligibility requires Gate 2 PASS, which a Cell04 construction
  optimized for cue separation may or may not achieve)

**Design requirement for Cell04:**
A new task structure is required in which the hop2 terminal (C-endpoint) is not the
target of the composite query — for example, a three-hop chain where the composite
answer is the B-intermediate and the C-endpoint is not queried, or a modified design
where the query asks for a specific non-terminal node. This is a substantive task
redesign that requires separate Team Lead / Manager authorization and design review.

**Is Cell04 a prerequisite for Track A Claim B?**
No. A future cue-separation design would strengthen and sharpen Claim B but is not
required for the core finding. The current provisional Claim B framing
(endpoint-return / chain-terminal-answer attraction; three cues weakened; residual
family unresolved) is supportable without it. Such a design, if authorized and
successfully executed, could convert the residual from "unresolved" to "attributed"
— but this is not guaranteed, as the answer-role vs chain-terminal separation
requires a task geometry that does not yet exist in this pipeline.

---

## §10. Paper-Candidate Assessment

### Claim B Track A framing

```
Candidate paper headline:
  "Endpoint-Return and Chain-Terminal-Answer Attraction at the Two-Hop Level 1
   Constructibility Floor in 3B FP16 Language Models"

Evidence base (three cells):
  - 3 FP16 runs × n=24 items × 4 query types = 288 scored outputs
  - All Branch 3 (constructibility-boundary); no stress-eligible cell
  - Locked scorer, locked tokenizer, locked prompt, deterministic greedy decoding
  - Full provenance chain: 7-artifact hash match per cell
  - Sequential cue disentanglement across 3 cells

Supported findings for Track A:
  1. hop2 near-ceiling (23-24/24 across cells): B→C single-hop retrieval is
     constructible at 3B FP16 under this construction family.
  2. hop1 and composite persistently below floor: the two-hop chain is not fully
     constructible across any of the three cell designs.
  3. Three-class stable failure surface: non_context_return, wrong_chain_selection,
     target_chain_wrong_neighbor recur across all cells; taxonomy is not expanding.
  4. Sequential cue weakening: position/ordering rejected as sufficient (Cell02);
     absolute position, C-rank slot, and adjacency/proximity weakened as sufficient
     (Cell03); chain-terminal/answer-endpoint family identified as residual.
  5. ct-anchoring uniformity: 2/8 per group in Cell03 (rank-invariant and
     position-invariant), providing the cue-disentanglement finding.
  6. neg_graph endpoint-emission: NOT ct-specific; 0/18 intrusions returned ct;
     pure endpoint-emission behavior under truncated context.
```

### Current framing constraints

```
Required language:
  "chain-terminal / answer-endpoint cue family remains unresolved"
  "endpoint-return behavior persists under corrected positional controls"
  "answer-domain salience remains a candidate subcue"
  "failure surface appears increasingly mappable"

Not permitted:
  "answer-domain salience proven"
  "mechanism established"
  "linkage impossible"
  "Track B unlocked"
  "Claim C tested"
  "compression stress measured"
```

### Stress-eligibility path (for reference — not authorized)

A stress-eligible cell (Gate 6) requires Gate 2 PASS on hop1, hop2, and composite
(≥21/24 each). No current cell reaches this threshold. Cell04 — if designed to target
cue separation rather than maximum accuracy — may also not produce a stress-eligible
cell. A separate clean-cell design (optimized for Gate 2 passage rather than cue
mapping) would be needed for Track B entry. Neither is currently authorized.

---

## §11. Cell04 Decision Section

### Option 1 — Stop at three cells and file Claim B

**Rationale:** The three-cell evidence base supports the provisional Claim B headline
and enables Track A framing. The residual unresolved cue (chain-terminal/answer-
endpoint) is documented as the open question, not a gap that invalidates the finding.
The paper can be filed with the framing that three cues are weakened and one family
remains unresolved, with Cell04 identified as future work.

**Supports:**
- Claim B Track A candidate (provisional framing, as stated in §10)
- Timely closure of the Track A filing
- No additional construction/execution burden

**Does not support:**
- Resolution of the chain-terminal / answer-domain salience split
- Definitively attributing the residual 6/24 ct-anchoring to a specific cue

### Option 2 — Pursue a future design to separate answer-role from chain-terminal role

**Rationale:** A new cue-separation cell could test whether ct-anchoring is driven by
ct's role as the composite answer or its role as the chain terminal endpoint. A
positive result (ct-anchoring disappears when ct is not the chain terminal) would
convert the residual from "unresolved" to "attributed to answer-domain salience." A
negative result (ct-anchoring persists regardless) would implicate chain-terminal
emission as the primary driver. Neither outcome is guaranteed.

**Cell04 is not authorized.** This option requires authorization from Team Lead and
Manager, a new task geometry that does not yet exist in this pipeline, and a full
construction / review cycle. It is presented here as a potential next step only.

**Cell04 design requirements (informational — not authorized):**
- New task structure in which the correct composite answer is NOT the terminal
  C-endpoint of the target chain
- This requires substantive task redesign (not a one-axis cell change within the
  current Two-Hop L1 design)
- Full construction pipeline: new generation script, manifest, validation, scorer
  compatibility check, Stage 0 review, FP16 authorization
- Standing precondition: Gate 3 endpoint-intrusion threshold amendment before any
  future stress-eligibility declaration (Team Lead governance guardrail, 2026-06-08)

**Would produce:**
- The cue attribution finding the three-cell synthesis cannot deliver
- A fourth data point in the Claim B floor map
- Potentially a more precise Track A headline

**Would not produce (without separate authorization):**
- Stress eligibility (requires Gate 2 PASS)
- Mechanism claims (behavioral evidence cannot establish mechanism)
- Track B entry (requires stress-eligible cell)

### Manager decision basis

```
To stop (Option 1):
  Three cells support provisional Claim B headline.
  Residual unresolved cue is documented and theoretically interpretable.
  Cell04 is identified as future work, not a gap in the current claim.

To continue (Option 2):
  The chain-terminal / answer-domain salience split is the core open question.
  Cell04 provides targeted cue attribution that would strengthen Claim B.
  Requires new task design, construction pipeline, and authorization cycle.
  Not a continuation of the current cell series — a new design class.
```

---

## §12. Standing Caveat

```
Gate 5 does not close target-token anchoring as a composite shortcut.
Composite ct-return is correct by construction and cannot be made ceiling-bearing
without turning the correct answer into a dummy failure.
Composite target-token anchoring remains tracked through §8 diagnostics, especially
hop1 failures returning ct.
```

---

## §13. Authorization Boundary

This synthesis drafting is authorized per Team Lead memo 2026-06-08.

**Not authorized by this synthesis or any artifact filed to date:**

```
new model inference of any kind
rerun of any cell
confirmation pass
FP16 repeat of any cell
7B model
INT8 or INT4 runs
Cell04 construction or execution
Track B (compression / stress)
Claim C testing
stress eligibility declaration
Gate 3 threshold lock
mechanism claims
seam claims
attribution beyond observational pattern description
```

The Gate 3 endpoint-intrusion threshold amendment remains a precondition for any
future stress-eligibility declaration (Team Lead governance guardrail, 2026-06-08).
Must define: failure class, query type, denominator, numeric ceiling, Gate 3 effect.

---

## §14. No-Inference Statement

No model inference was performed in preparing this synthesis. All data is from:

```
RESULTS-TWOHOP-L1-cell01-1780912218.json   (sha256:6de8b67c...)
RESULTS-TWOHOP-L1-cell02-1780933041.json   (sha256:47b5eaa9...)
RESULTS-TWOHOP-L1-cell03-1780948339.json   (sha256:f29783622f...)
```

These are the locked, hash-verified run artifacts for the three authorized FP16 runs.
No additional scoring, no output modification, no rerun.

---

## Appendix A — Cross-Cell Per-Item Ct-Anchoring Summary (hop1)

```
Cell01 ct-anchoring on hop1 (target_chain_wrong_neighbor, 3 items):
  i06  C_target-first   ct at pos2   returned ct (XFCPN)   hop1_proximity = 1
  i08  C_target-first   ct at pos2   returned ct (YXPPV)   hop1_proximity = 1
  i15  C_target-middle  ct at pos4   returned ct (SVHZX)   hop1_proximity = 2
  (Cell01 runner did not include §8 diagnostics; positions derived from manifest)

Cell02 ct-anchoring on hop1 (target_chain_wrong_neighbor, 11 items):
  i02, i04, i06, i07, i11, i12, i13, i17, i18, i22, i24
  All: ct at pos6 (second_C); hop1 at pos5; hop1_proximity = 1 (adjacent)
  (Cell02 runner did not include §8 diagnostics)

Cell03 ct-anchoring on hop1 (target_chain_wrong_neighbor, 6 items):
  i01  Group A  ct at pos3 (first_C)   returned ct   hop1_proximity = 2
  i06  Group A  ct at pos3 (first_C)   returned ct   hop1_proximity = 2
  i09  Group B  ct at pos5 (second_C)  returned ct   hop1_proximity = 2
  i14  Group B  ct at pos5 (second_C)  returned ct   hop1_proximity = 2
  i17  Group C  ct at pos7 (third_C)   returned ct   hop1_proximity = 2
  i18  Group C  ct at pos7 (third_C)   returned ct   hop1_proximity = 2
  (All Cell03 ct-anchoring: hop1_proximity = 2 uniformly — adjacency broken for all)
```

---

## Appendix B — Source Artifact Index

```
Cell01 run:          RESULTS-TWOHOP-L1-cell01-1780912218.json   sha256:6de8b67c...
Cell01 run summary:  RESULTS-TWOHOP-L1-cell01-ALL.md
Cell01 map entry:    CLAIM-B-MAP-ENTRY-TWOHOP-L1-CELL01.md

Cell02 run:          RESULTS-TWOHOP-L1-cell02-1780933041.json   sha256:47b5eaa9...
Cell02 run summary:  RESULTS-TWOHOP-L1-cell02-ALL.md
Cell02 map entry:    CLAIM-B-MAP-ENTRY-TWOHOP-L1-CELL02.md

Cell03 run:          RESULTS-TWOHOP-L1-cell03-1780948339.json   sha256:f29783622f...
Cell03 run summary:  RESULTS-TWOHOP-L1-cell03-ALL.md
Cell03 decomposition: CELL03-DECOMPOSITION-PACKET.md
Cell03 decomp review: CELL03-DECOMPOSITION-REVIEW.md

Scorer (Cell01/02):  scorer_twohop_l1.py   sha256:060afad9...
Scorer (Cell03):     scorer_twohop_l1.py   sha256:b65c6803...
Validator:           tasks_twohop_l1.py    sha256:bcc26ca0...
Tokenizer:           sha256:c0382117...    (all three cells)
Prompt template:     sha256:c8a81a29...    (all three cells)
Model snapshot:      aa8e72537993ba99e69dfaafa59ed015b17504d1  (all three cells)
```

---

**Synthesis filed. No model inference was performed. Awaiting Team Lead disposition.**

— CS Engineer, 2026-06-08
