# Claim B Map Entry — Two-Hop Level 1 Cell01

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Authorized by:** Team Lead memo — "Claim B Map Entry — Cell01 Filing Instructions" 2026-06-08
**Status:** FILED — constructibility-boundary point for Claim B; multi-axis classification
**Overlap section:** Filled from item-level JSON 2026-06-08 (tier0-run/RESULTS-TWOHOP-L1-cell01-1780912218.json)

---

## 1. Identity

```
Cell ID:             twohop_l1_cell01
Design:              3-chain, 7-fact, 8+8+8 ordering
                     3 chains per item: target + decoy_1 + decoy_2
                     7 facts per item
                     Ordering groups: items 1-8 C_target-first (T-hop2 at pos 2),
                       items 9-16 C_target-middle (T-hop2 at pos 4),
                       items 17-24 C_target-last (T-hop2 at pos 6)
n_items:             24 (per query type)

Model:               Qwen/Qwen2.5-3B-Instruct
Precision:           FP16
Model snapshot:      aa8e72537993ba99e69dfaafa59ed015b17504d1
```

### Valid run artifact

```
Path:    tier0-run/RESULTS-TWOHOP-L1-cell01-1780912218.json
Hash:    sha256:6de8b67c0267a65f088e7bccd68b3cd070c675938c71470dd97a5411daca6f47
Status:  VALID — Stage 1 FP16 result
Runner:  amended runner sha256:f346e4f2... (mlx_lm 0.19.3, chat-template applied)
```

### Voided run artifact

```
Path:    tier0-run/RESULTS-TWOHOP-L1-cell01-1780911140.json
Hash:    sha256:1adeb548d4e83bdb730f4c708d91a11f6506995e87d87a433ebbf16aa9fa0c8e
Status:  VOID — environment/runner incompatibility (mlx_lm 0.8.0, no chat template)
         May not be used as Stage 1 data or constructibility evidence.
```

### Tokenizer provenance

The FP16 run tokenizer sha256:c0382117… and the prior audit tokenizer sha256:3fd169731d… are
tokenizer-equivalent after normalization: vocabulary identical, normalized merges identical, and BPE
behavior empirically identical on the audited surfaces. BPE-Jaccard was re-audited under the actual
FP16 run tokenizer with 0 violations and 24/24 near-miss pairs meeting j ≥ 0.40.

```
Run tokenizer:   sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
                 (FP16 HuggingFace, snapshot aa8e7253...)
Audit tokenizer: sha256:3fd169731d2cbde95e10bf356d66d5997fd885dd8dbb6fb4684da3f23b2585d8
                 (INT4 MLX serialization — confirmed equivalent; see TOKENIZER-HASH-RECONCILIATION-TWOHOP-L1.md)
```

### Locked artifact hashes

```
scorer_hash:            sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd
runner_hash:            sha256:f346e4f2cf93b881e129ba25bea469e2f6349ce1b6d430f8ddfb7269f3d0d7ce
manifest_hash:          sha256:00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28
validator_hash:         sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
prompt_template_hash:   sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
failure_taxonomy:       v1.0
decoding:               temperature=0.0, max_tokens=16 (greedy, deterministic)
```

---

## 2. Gate Summary

```
Gate 0    Axis-control & manifest          PASS
            24/24 validate_manifest; axis = single (token identity); 8+8+8 ordering;
            identical_context_hash verified; negative_graph path_exists=False confirmed

Gate 0.5  Token-construction audit         PASS (reconciled — see §1 tokenizer provenance)
            BPE round-trip: 0 failures
            Levenshtein violations: 0
            Trigram-Jaccard violations: 0
            BPE-Jaccard cross-chain C violations: 0
            Near-miss pairs: 24/24 j ≥ 0.40 confirmed under run tokenizer

Gate 1    Contract adherence               PASS
            hop1:          24/24 FORMAT_PASS
            hop2:          24/24 FORMAT_PASS
            composite:     24/24 FORMAT_PASS
            negative_graph: 24/24 FORMAT_PASS

Gate 2    FP16 baseline correctness        FAIL (first failed gate)
            hop1:      14/24 = 0.583   threshold ≥ 21/24   → FAIL
            hop2:      24/24 = 1.000   threshold ≥ 21/24   → PASS
            composite: 18/24 = 0.750   threshold ≥ 21/24   → FAIL
            [negative_graph not in G2; reported separately in §3 Axis A]

Gate 3    Operation fidelity               BLOCKED by Gate 2
            (computed diagnostic — not binding)
            stopped_short:    1/24   ceiling ≤ 3/24   → PASS
            shortcut_single:  0/24   ceiling ≤ 2/24   → PASS (structural guarantee)
            wrong_chain:      4/24   ceiling ≤ 3/24   → FAIL
            wrong_neighbor:   0/24   ceiling ≤ 3/24   → PASS
            anchor_echo:      0/24   ceiling ≤ 3/24   → PASS

Gate 4a   Classifier reliability           BLOCKED by Gate 2
            (computed) unique_assignment_rate = 1.000
            UNCLASSIFIED_OFF_FRAME = 0/96 = 0.000

Gate 5    Control adequacy                 BLOCKED by Gate 2
            (computed) max_dummy = 8/24 = 0.333 ≤ 9/24   → PASS
            composite (18) − max_dummy (8) = 10 ≥ 10     → PASS (minimum)

Gate 6    Stress eligibility               NOT ELIGIBLE
            Gate 2 failure; cell is not stress-eligible

First failed gate:    Gate 2
                      hop1 14/24 < 21/24; composite 18/24 < 21/24
Stress eligibility:   NOT ELIGIBLE
Track B:              BLOCKED
```

---

## 3. Per-Axis Classification

### Axis A — Contract / abstention behavior

```
Axis:             Contract / abstention behavior
Primary signal:   negative_graph null_return and endpoint-return behavior

Observed:
  negative_graph correct (NULL returned):  2/24 = 0.083  (items i04, i08; both C_target-first group)
  endpoint return:                        22/24 = 0.917
    wrong_chain_selection:   11/24  (returned decoy-chain endpoint)
    target_chain_wrong_neigh: 11/24 (returned hop1_B intermediate — the target chain B node)

  Gate 1: 24/24 FORMAT_PASS for negative_graph — format contract was followed
  Gate 2: not evaluated for negative_graph (not part of G2a/b/c)

Non-NULL returns by type:
  11 wrong_chain_selection: model returned C-position endpoint of a decoy chain
  11 target_chain_wrong_neigh: model returned the target chain's B-position node (intermediate)
    — the edge target_chain/hop2 was removed; model navigated only one hop

Summary label:    Abstention instability — endpoint-return prior dominant
                  Model follows format contract (ANSWER: prefix) but does not withhold
                  answer when the requested path is absent. Returns a reachable endpoint
                  (either via a decoy chain or via the surviving hop1 edge) in 22/24 cases.
                  Correct NULL behavior is present but rare: 2/24, concentrated in
                  C_target-first group (same items i04, i08 that show format stability on hop1
                  is irrelevant — hop1 i04 failed NULL, hop1 i08 failed wrong_neigh).
```

### Axis B — Content / distractor / chain-selection behavior

```
Axis:             Content / distractor / chain-selection behavior
Primary signal:   composite wrong_chain_selection; hop2 ceiling

Observed:
  hop2:       24/24 correct — B→C single-hop fully constructible
  composite:  18/24 correct
    wrong_chain_selection:          4/24  (returned decoy-chain C endpoint)
    correct_chain_stopped_short:    1/24  (returned target-chain B, not C)
    non_context_return:             1/24  (returned NULL)

  Gate 3 wrong-chain ceiling: 4/24 > 3/24 — exceeds ceiling
    This would fail Gate 3 independently if Gate 2 were passed.

Decoy selection detail:
  When wrong_chain_selection fires on composite, the model returns the endpoint of
  a decoy chain rather than the target chain endpoint. This is a content/distractor
  failure: the model selects the wrong chain, not the wrong node within the correct chain.
  hop2 24/24 confirms the model can retrieve B→C correctly when the chain is unambiguous.
  The wrong-chain failures occur when the full composite query (A→B→C) is presented with
  all three chains in context.

Summary label:    Partial constructibility — hop2 clean, composite distractor-sensitive
                  B→C retrieval is fully constructible at 3B FP16 (24/24).
                  Full A→B→C composite retrieval is not: 4/24 failures are classifiable
                  as wrong-chain selection, not wrong-node within correct chain.
                  The 4/24 rate exceeds the Gate 3 structural ceiling.
```

### Axis C — Position / ordering behavior

```
Axis:             Position / ordering behavior
Primary signal:   hop1 NULL failures concentrated in C_target-first ordering group

Observed:
  hop1 by ordering group:
    C_target-first  (items 1-8):   0/8  correct  (8/8 fail — 6 NULL, 2 wrong_neigh)
    C_target-middle (items 9-16):  6/8  correct  (2/8 fail — 1 wrong_neigh, 1 NULL)
    C_target-last   (items 17-24): 8/8  correct  (0 failures)

  The NULL failure mode is exclusively a C_target-first phenomenon:
    C_target-first:  6/6 hop1 NULL failures  (items i01, i02, i03, i04, i05, i07)
    C_target-middle: 1/1 hop1 NULL failure   (item i16)
    C_target-last:   0 hop1 NULL failures

  hop2 and composite show no ordering-group ceiling effect on correct count:
    hop2 24/24 correct uniformly across all three groups.
    Composite Group 1 (items 1-8): 4/8 correct.
    Composite Group 2 (items 9-16): 7/8 correct.
    Composite Group 3 (items 17-24): 7/8 correct.

Summary label:    Position / ordering sensitive — provisional (see §4 ambiguity note)
                  hop1 NULL failures cluster strongly in C_target-first.
                  C_target-first places the target hop2 fact at context position 2 (early).
                  Whether the causal factor is: (a) early placement of the hop2 answer
                  conflicting with hop1 retrieval, (b) positional distractor geometry, or
                  (c) interaction between token identity and ordering — is not resolvable
                  from Cell01 alone.
```

---

## 4. Per-Axis Label Confidence

### Axis A — Contract / abstention

```
Label:          Abstention instability / endpoint-return prior
Confidence:     Clean as behavioral description; interpretation contested

wrong_chain_selection (neg_graph):
  label_confidence: clean
  basis: scorer classified against C-role registry; returned token is decoy-chain endpoint
  interpretation: model selected reachable endpoint via decoy chain rather than withholding

target_chain_wrong_neigh (neg_graph):
  label_confidence: clean
  basis: returned token is target-chain B-position node (hop1_B role); hop2 edge removed;
         model navigated one surviving hop, not two
  interpretation: model followed the surviving hop1 edge and returned its object
                  rather than withholding for path absence

correct NULL (2/24):
  label_confidence: clean
  interpretation: model correctly withheld; items i04 and i08 (C_target-first group)
  ambiguity_note: why these two items produced correct NULL is not resolvable from
                  Cell01. Could reflect item-specific token geometry, context ordering,
                  or chance within a near-zero calibration.

Overall axis label:
  interpretation: ambiguous between:
    (a) abstention instability — model has poor NULL-contract adherence on this construction
    (b) endpoint-return prior — model defaults to returning a reachable endpoint when
        the queried path is absent
  These interpretations are not mutually exclusive. Both can be true simultaneously.
  No mechanism claim is licensed.

NULL-calibration carry-forward:
  Gate 1 passed 96/96 on format. Negative_graph showed only 2/24 correct NULL behavior.
  Format adherence and NULL-contract stability are separable. Future preflight revision
  should add a NULL / NO_LINK calibration gate or watch condition on negative_graph
  null_return rate. This note does not alter the Cell01 result; it records a ladder
  improvement for future cells.
```

### Axis B — Content / distractor / chain-selection

```
Label:          Partial constructibility — hop2 clean, composite distractor-sensitive
Confidence:     Clean (role-based classification)

hop2 (24/24 correct):
  label_confidence: clean
  basis: 24/24 FORMAT_PASS, 24/24 correct — B→C retrieval is constructible

composite wrong_chain_selection (4/24):
  label_confidence: clean
  basis: scorer classified against C-role registry; returned token role is
         distractor_chain_endpoint (decoy C) not answer_C (target C)
  interpretation: model selected a decoy chain's endpoint over the target chain endpoint
                  when both were present in context with the same hop2 relation verb

composite stopped_short (1/24, item i22):
  label_confidence: clean
  basis: returned token role is hop1_B (target chain B); correct answer is answer_C
  interpretation: model traversed only the first hop (A→B), stopped before B→C

composite non_context_return (1/24, item i04):
  label_confidence: clean (NULL returned; contract adherent)
  interpretation: model withheld on composite query for item i04 — same item where
                  NULL was also returned on hop1 and correct NULL on negative_graph

ambiguity_note:
  The 4/24 wrong-chain rate exceeds Gate 3 ceiling (3/24). This is a classifiable
  excess, not an ambiguous boundary. The label is clean. The interpretation of WHY
  the model selects decoy chains on composite when hop2 is fully clean — is not
  resolvable from Cell01 alone (see §5 overlap analysis).
```

### Axis C — Position / ordering

```
Label:          Position / ordering sensitive — provisional
Confidence:     Clean as observational claim; contested as causal interpretation

hop1 NULL clustering:
  label_confidence: clean as returned NULL token
  interpretation: contested / ambiguous
  ambiguity_note:
    The NULL returns are concentrated in C_target-first (items 1-8: 0/8 hop1 correct).
    Three candidate explanations, not distinguishable from Cell01:
      (a) Positional: early placement of the target hop2 answer (at context pos 2)
          interferes with hop1 retrieval — model sees the hop2 answer early and
          returns NULL for hop1 rather than the hop1_B intermediate.
      (b) Token-positional interaction: C_target-first tokens may coincidentally share
          properties that cause retrieval difficulty beyond ordering alone.
      (c) Abstention triggered by ordering geometry: model's hop1 retrieval is
          destabilized when the chain terminal is in early context position.
    Cell01 cannot distinguish these. A clean next-axis test would invert or isolate
    the C_target-first condition while holding token identities and distractor geometry
    constant.

hop1 wrong_neigh (3 items: i06, i08, i15):
  label_confidence: clean
  basis: returned token role is target_neighbor_decoy; not NULL
  note: i06 and i08 are in C_target-first group (non-NULL failure mode for that group);
        i15 is C_target-middle. These are a different failure mode than NULL returns —
        model retrieved a related but incorrect token rather than withholding.
```

---

## 5. Failure Overlap — hop1 vs composite

**Source:** Item-level JSON confirmed 2026-06-08 from tier0-run/RESULTS-TWOHOP-L1-cell01-1780912218.json.
All failure classes, tokens, and roles are from the actual scorer output, not inferred from counts.

### Item-level overlap table

```
item  group            hop1_fc / tok          composite_fc / tok         neg_graph_fc / tok     h1_fail  co_fail  overlap
i01   C_target-first   non_context_return/NULL  wrong_chain_sel/FSLIY    wrong_chain_sel/FSLIY  YES      YES      YES
i02   C_target-first   non_context_return/NULL  correct/DBKSD            wrong_chain_sel/UEBLS  YES      NO       —
i03   C_target-first   non_context_return/NULL  wrong_chain_sel/HGKLW    wrong_chain_sel/HGKLW  YES      YES      YES
i04   C_target-first   non_context_return/NULL  non_context_ret/NULL     correct/NULL           YES      YES      YES
i05   C_target-first   non_context_return/NULL  correct/BAGCR            wrong_chain_sel/PLFBI  YES      NO       —
i06   C_target-first   target_wrong_neigh/XFCPN correct/XFCPN           wrong_chain_sel/QDBJV  YES      NO       —
i07   C_target-first   non_context_return/NULL  wrong_chain_sel/SVHZX    wrong_chain_sel/SVHZX  YES      YES      YES
i08   C_target-first   target_wrong_neigh/YXPPV correct/YXPPV           correct/NULL           YES      NO       —
i09   C_target-middle  correct/ZBUIE            correct/FSLIY            target_wrong_neigh/ZBUIE NO     NO       —
i10   C_target-middle  correct/ZBNBZ            correct/UEBLS            target_wrong_neigh/ZBNBZ NO     NO       —
i11   C_target-middle  correct/ZBRAL            correct/HUCAX            target_wrong_neigh/ZBRAL NO     NO       —
i12   C_target-middle  correct/ZBFSG            correct/PLZEG            wrong_chain_sel/QYQYP  NO      NO       —
i13   C_target-middle  correct/ZBBDR            wrong_chain_sel/BAGCR    wrong_chain_sel/BAGCR  NO      YES      NO (independent)
i14   C_target-middle  correct/ZBCXB            correct/QDBJV            target_wrong_neigh/ZBCXB NO    NO       —
i15   C_target-middle  target_wrong_neigh/SVHZX correct/SVHZX           wrong_chain_sel/GTJWG  YES     NO       —
i16   C_target-middle  non_context_return/NULL  correct/BKMVE            wrong_chain_sel/YXPPV  YES     NO       —
i17   C_target-last    correct/ZBKYX            correct/DNXUT            target_wrong_neigh/ZBKYX NO    NO       —
i18   C_target-last    correct/ZBAMV            correct/PZUPT            target_wrong_neigh/ZBAMV NO    NO       —
i19   C_target-last    correct/ZBGQC            correct/HGKLW            target_wrong_neigh/ZBGQC NO    NO       —
i20   C_target-last    correct/ZBOVW            correct/QYQYP            target_wrong_neigh/ZBOVW NO    NO       —
i21   C_target-last    correct/ZBMFK            correct/PLFBI            target_wrong_neigh/ZBMFK NO    NO       —
i22   C_target-last    correct/ZBLNF            stopped_short/ZBLNF      target_wrong_neigh/ZBLNF NO   YES      NO (independent)
i23   C_target-last    correct/ZBVLS            correct/DFHLZ            target_wrong_neigh/ZBVLS NO    NO       —
i24   C_target-last    correct/ZBDGA            correct/JEMZC            wrong_chain_sel/BKMVE  NO      NO       —

Roles confirmed from JSON:
  non_context_return tokens: all NULL / null_no_link role
  wrong_chain_selection tokens: all distractor_chain_endpoint role
  target_chain_wrong_neighbor tokens: all answer_C role (hop1 queries i06/i08/i15) or hop1_B role (neg_graph)
  stopped_short token i22: ZBLNF / hop1_B role
```

### Q1 — Of the 6 composite failures, how many also failed hop1?

```
4 of 6 composite failures also failed hop1.

  i01: hop1=NULL(non_context_return)  composite=FSLIY(wrong_chain_selection)  — overlap
  i03: hop1=NULL(non_context_return)  composite=HGKLW(wrong_chain_selection)  — overlap
  i04: hop1=NULL(non_context_return)  composite=NULL(non_context_return)       — overlap
  i07: hop1=NULL(non_context_return)  composite=SVHZX(wrong_chain_selection)  — overlap
  i13: hop1=ZBBDR(correct)            composite=BAGCR(wrong_chain_selection)   — independent
  i22: hop1=ZBLNF(correct)            composite=ZBLNF(stopped_short)           — independent
```

### Q2 — Of the 4 composite wrong_chain failures, how many also failed hop1?

```
3 of 4 composite wrong_chain failures also failed hop1.

  i01: hop1=NULL  composite=FSLIY(distractor_chain_endpoint)  — overlap
  i03: hop1=NULL  composite=HGKLW(distractor_chain_endpoint)  — overlap
  i07: hop1=NULL  composite=SVHZX(distractor_chain_endpoint)  — overlap
  i13: hop1=ZBBDR(correct hop1_B)  composite=BAGCR(distractor_chain_endpoint)  — independent

Behavioral divergence confirmed from JSON:
  On all three overlapping wrong_chain items (i01, i03, i07):
    hop1 returns NULL (non_context_return — abstention)
    composite returns a distractor_chain_endpoint (wrong_chain_selection — active selection)
  The failure class differs between hop1 and composite on every overlapping wrong_chain item.
  Strict downstream causation would predict composite=NULL if hop1=NULL.
  Instead composite selects a decoy chain endpoint, indicating the composite query triggers
  a different behavioral response than the hop1 query under the same positional geometry.
```

### Q3 — Do composite wrong_chain failures cluster in the same positional group as hop1 NULL failures?

```
YES — 3 of 4 composite wrong_chain failures and 6 of 7 hop1 NULL failures are in C_target-first.

  Composite wrong_chain failures by group:
    C_target-first  (items 1-8):  i01, i03, i07  — 3 of 4
    C_target-middle (items 9-16): i13            — 1 of 4
    C_target-last   (items 17-24): none

  hop1 NULL failures by group:
    C_target-first  (items 1-8):  i01, i02, i03, i04, i05, i07  — 6 of 7
    C_target-middle (items 9-16): i16                            — 1 of 7
    C_target-last   (items 17-24): none

  i13 is the lone exception: composite wrong_chain in C_target-middle with hop1 correct.
  Chain-selection fragility is not exclusively a C_target-first phenomenon.

  Additional clustering note (consistent distractor token across composite and neg_graph):
    For all 4 wrong_chain composite failures, the same distractor token is returned on
    both composite and negative_graph:
      i01: composite=FSLIY  neg_graph=FSLIY  (match)
      i03: composite=HGKLW  neg_graph=HGKLW  (match)
      i07: composite=SVHZX  neg_graph=SVHZX  (match)
      i13: composite=BAGCR  neg_graph=BAGCR   (match)
    The model has a consistent per-item distractor preference that is stable across
    query types. This is consistent with role-based chain selection (not random noise):
    each item's returned wrong token is a real in-context distractor_chain_endpoint.
```

### Q4 — Are composite failures best explained as downstream of hop1 weakness, independent chain-selection fragility, position/ordering sensitivity, or mixed?

```
MIXED / UNRESOLVED — multiple patterns present; no single explanation accounts for all failures.

Pattern 1 — Behavioral divergence in overlapping C_target-first items (i01, i03, i07):
  hop1=NULL(non_context_return), composite=wrong_chain(distractor_chain_endpoint).
  Both queries fail on these items, and all are in C_target-first.
  However: the failure class differs. A strict downstream account predicts composite=NULL
  (same abstention as hop1). Composite instead selects a decoy chain endpoint.
  Interpretation: C_target-first geometry disrupts both queries, but disrupts them differently.
  hop1 → abstention; composite → decoy-chain selection.
  These are independent behavioral responses to a shared positional context, not propagation.
  Downstream causation: inconsistent with behavioral divergence. Positional sensitivity: consistent.

Pattern 2 — Consistent abstention (i04):
  hop1=NULL, composite=NULL — failure class is identical.
  neg_graph=NULL(correct) — model correctly withholds when asked on neg_graph.
  i04 is the one item where downstream-consistent behavior holds: both queries return NULL.
  This is the only composite failure where the failure class matches hop1.

Pattern 3 — Independent chain-selection fragility (i13):
  hop1=correct(ZBBDR hop1_B). composite=wrong_chain(BAGCR distractor_chain_endpoint).
  No hop1 weakness. No positional confound (C_target-middle).
  Pure chain-selection failure: model retrieved correct hop1 intermediate but selected
  the wrong chain endpoint for the composite query.
  neg_graph also returns BAGCR — consistent distractor preference for i13 regardless of
  composite vs neg_graph query type.

Pattern 4 — Stopped-short failure (i22):
  hop1=correct(ZBLNF hop1_B). composite=stopped_short(ZBLNF hop1_B). neg_graph=wrong_neigh(ZBLNF).
  All three queries return the same token ZBLNF (the hop1_B intermediate).
  hop1 is correct because ZBLNF is the hop1 answer. Composite is wrong because ZBLNF is
  not the hop2 answer (BNEQN is). neg_graph is wrong because ZBLNF is the surviving hop1_B
  node, not NULL.
  The model has learned ZBLNF as the dominant salient token for i22's chain and returns it
  consistently. Composite failure is independent of hop1 strength — it reflects inability
  to advance past the B intermediate, not inability to find it.

Interpretive key applied:
  "Most composite failures also failed hop1" (4/6):
    → Downstream signal present — but behavioral divergence on i01/i03/i07 argues against
      strict downstream causation.
  "Most composite wrong_chain passed hop1" is NOT true (only 1/4):
    → "At least partly independent" is partially supported only by i13.
  "Failures cluster in C_target-first":
    → Supports position/ordering as the recommended next axis.
  "Failures cluster by distractor geometry":
    → Distractor token is consistent per item (same token on composite and neg_graph),
      suggesting per-item distractor geometry contributes — but cannot be separated from
      positional geometry within Cell01.

Conclusion:
  The overlapping failures (i01, i03, i04, i07) share C_target-first geometry but show
  divergent behavioral responses (NULL vs wrong_chain). The independent failures (i13, i22)
  confirm that composite fragility exists outside the positional confound.
  The data supports: MIXED — position/ordering sensitivity and independent chain-selection
  fragility both present; cannot be separated from Cell01 alone.
  Recommended next axis is position/ordering (§8) on the basis of the C_target-first
  clustering signal, not on the basis of a resolved causal claim.

Additional item-level observations (not interpretive claims):

  C-endpoint over-retrieval on hop1 (items i06, i08, i15):
    These three target_chain_wrong_neighbor hop1 failures all returned the target chain's
    C endpoint (answer_C role) instead of the expected B intermediate (hop1_B role).
    The returned token is identical to the correct hop2 answer for each item:
      i06: hop1 returns XFCPN (answer_C) = hop2 correct answer = composite correct answer
      i08: hop1 returns YXPPV (answer_C) = hop2 correct answer = composite correct answer
      i15: hop1 returns SVHZX (answer_C) = hop2 correct answer = composite correct answer
    The model retrieved the correct chain but the wrong node — returning the chain endpoint
    (C) rather than the queried intermediate (B). hop2 and composite are correct on all
    three items because C is the correct answer for those queries.
    This is a structural observation, not a mechanism claim.
```

---

## 6. Safe Interpretation

Under the locked Two-Hop Level 1 construction at 3B FP16, Cell01 did not reach the constructibility
floor. The failure was structured and classifiable: hop2 cleared, hop1 and composite failed Gate 2,
negative-graph abstention was unstable, wrong-chain selection exceeded the Gate 3 ceiling, and
UNCLASSIFIED remained zero. Cell01 is a dirty-cell boundary point for Claim B, not a test of Claim C.

```
Specific safe statements:

  hop2 (B→C): Fully constructible at 3B FP16 under this construction (24/24).

  hop1 (A→B): Not constructible at 3B FP16 under this construction (14/24).
    Failure is structured: NULL returns concentrate in C_target-first ordering group;
    8/8 C_target-first items fail hop1. C_target-last 8/8 items pass hop1.
    The positional pattern is an observation, not a mechanism claim.

  composite (A→B→C): Not constructible at 3B FP16 under this construction (18/24).
    Dominant failure: wrong_chain_selection 4/24, exceeding Gate 3 ceiling.
    Mixed overlap with hop1 failures (4/6 overlap items) and independent failures (2/6).

  negative_graph: Abstention unstable (2/24 correct NULL).
    Format contract satisfied (24/24 FORMAT_PASS); NULL-contract not satisfied.
    Endpoint-return dominant: 22/24 return a reachable endpoint.
    Gate 1 passes; abstention stability is not measured by Gate 1.

  Claim B applicability:
    Cell01 confirms the existence of a dirty cell with classifiable failures at 3B FP16.
    Zero UNCLASSIFIED_OFF_FRAME supports that the failure taxonomy covers the observed
    failure surface on this construction.
    Cell01 does NOT support Claim C (stress eligibility) or any compression claim.
```

---

## 7. Forbidden Interpretations

```
No stress result.
  Gate 2 fails. Cell is not stress-eligible. No INT8 or INT4 result is licensed from Cell01.

No INT8 or INT4 result.
  No quantization run was performed. No compression result.

No seam result.
  Cell01 tests FP16 constructibility only. The seam hypothesis (INT4 causes composite-vs-component
  degradation) cannot be evaluated from a single FP16 run.

No compression result.
  No bit-depth comparison was performed.

No mechanism claim.
  The positional clustering of hop1 failures is an observational finding.
  It does not imply a causal mechanism. The causes of positional sensitivity are not
  resolvable from Cell01.

No Track B result.
  Track B is blocked. No Track B authorization exists.

No Claim C test.
  Claim C requires a stress-eligible clean cell. Cell01 is not clean.

No claim that 3B cannot do two-hop linkage generally.
  Cell01 is one frozen construction. hop2 24/24 demonstrates two-hop retrieval is
  present at the B→C level. hop1 and composite failures are construction- and
  ordering-specific observations, not general capability claims.

No claim that the positional pattern is causal.
  Clustering in C_target-first is a correlation within Cell01. It does not establish
  that ordering caused the failures or that a different ordering would produce different
  results. This is a provisional label pending a targeted next-axis test.
```

---

## 8. Recommended Next Axis

**Provisional recommendation — not an authorization.**

```
Axis:           Position / ordering
Rationale:      The most structured signal in Cell01 is the hop1 NULL failure concentration
                in C_target-first (8/8 items fail hop1; 0/8 in C_target-last).
                The distractor geometry, token identities, and relation structure are
                confounded with ordering in Cell01. A dedicated position test would
                isolate the ordering variable.

Proposed test:  Invert or isolate the C_target-first ordering condition while holding
                distractor geometry, token identities, and relation structure constant.
                A matched cell that places the target hop2 fact at a late context position
                (C_target-last equivalent) for the items that failed hop1 in Cell01 would
                provide direct evidence on whether ordering is the separable causal factor.

One-axis rule:  Cell02 should change only one axis unless Manager explicitly authorizes
                an interaction test. Changing both ordering AND distractor geometry in the
                same cell would make it impossible to attribute any outcome difference to
                either variable.
```

**Authorization boundary:**

```
This map entry does not authorize Cell02 construction.
Any new cell requires separate Manager authorization.
The recommended next axis is a provisional record only.
```

---

## Authorization chain (Cell01)

```
1. Stage 0 closure — Team Lead, 2026-06-07
2. Threshold proposal review — Team Lead, 2026-06-08
3. Stage 1 preparation authorization — Manager, 2026-06-08
4. FP16 tokenizer acceptance + scorer/cell amendment — Team Lead, 2026-06-08
5. Stage 1 Preparation Lock Packet Rev 2 accepted — Team Lead, 2026-06-08
6. FP16 Stage 1 Execution Authorization — Manager, 2026-06-08
7. FP16 Stage 1 Run Escalation + Runner Amendment Authorization (Option R1) — Manager, 2026-06-08
8. Branch 3 accepted / tokenizer reconciliation requested — Team Lead, 2026-06-08
9. Tokenizer reconciliation complete — CS Engineer, 2026-06-08
10. Claim B Map Entry Filing Instructions — Team Lead, 2026-06-08
```

---

**Cell01 filed as Claim B constructibility-boundary point. No further execution authorized under this filing.**

— CS Engineer, 2026-06-08
