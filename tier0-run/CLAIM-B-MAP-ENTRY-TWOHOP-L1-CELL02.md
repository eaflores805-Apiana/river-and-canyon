# Claim B Map Entry — Two-Hop Level 1 Cell02

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Authorized by:** Team Lead memo — "Cell02 FP16 Return Packet — Provenance Match Table and Filing Clarification Required" 2026-06-08
**Status:** FILED — second constructibility-boundary point for Claim B; position/ordering axis test; Gate 1 FAIL / Gate 2 FAIL / Branch 3

---

## 1. Identity and artifact hashes

```
Cell ID:          twohop_l1_cell02
Design:           3-chain, 7-fact, all-C_target-last
                  3 chains per item: target + decoy_1 + decoy_2
                  7 facts per item
                  Ordering: all 24 items C_target-last (T-hop2 at context position 6)
                  decoy_chain_2 hop2 at position 7 (Gate 5 forced)
n_items:          24 (per query type)
Axis under test:  position / ordering (one-axis change from Cell01)
RNG seed:         20260610

Model:            Qwen/Qwen2.5-3B-Instruct
Precision:        FP16
Model snapshot:   aa8e72537993ba99e69dfaafa59ed015b17504d1
```

### Run artifact

```
Path:    tier0-run/RESULTS-TWOHOP-L1-cell02-1780933041.json
Hash:    sha256:47b5eaa9b954645ca2572fe20873a0255776f60f29b0a544d8c350dcddc181ca
Status:  VALID — Stage 1 FP16 result; Gate 1 FAIL / Gate 2 FAIL / Branch 3
Runner:  runner_twohop_l1_cell02.py sha256:d14f6424...
         (amended from Cell01 runner: ITEMS_PATH + AXIS_CONFIGURATION only)
```

### Tokenizer provenance

BPE-Jaccard audit performed under run tokenizer sha256:c0382117... (FP16 HuggingFace). No separate reconciliation required for Cell02 — audit was performed directly under the run tokenizer from the start.

```
Run tokenizer:  sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
                (FP16 HuggingFace, snapshot aa8e7253...)
                Same as Cell01 run tokenizer — confirmed unchanged.
```

---

## 2. Provenance match table

Expected hashes from CELL02-PREP-LOCK-PACKET-TWOHOP-L1.md. Observed hashes from run artifact provenance block.

```
Artifact           Expected hash                                                       Observed hash                                                       Status
Cell02 JSON        sha256:b81d471616f8830fba76b99b9e1b04e23d3e4af13284c27627481ae89528f4c9  sha256:b81d471616f8830fba76b99b9e1b04e23d3e4af13284c27627481ae89528f4c9  MATCH
Runner             sha256:d14f6424340699785a8bdc12a8bb6c2b7cb33f96069de49e1fcb945bbc12b0fa  sha256:d14f6424340699785a8bdc12a8bb6c2b7cb33f96069de49e1fcb945bbc12b0fa  MATCH
Prompt template    sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e  sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e  MATCH
Scorer             sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd  sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd  MATCH
Validator          sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b  sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b  MATCH
Tokenizer          sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539  sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539  MATCH
Model snapshot     aa8e72537993ba99e69dfaafa59ed015b17504d1                                aa8e72537993ba99e69dfaafa59ed015b17504d1                                MATCH
```

All 7 artifacts: **MATCH**. No provenance deviations.

---

## 3. Gate summary

```
Gate 0   Manifest schema         PASS    24/24 validate_manifest
Gate 0.5 Token construction      PASS    0 violations; 24/24 near-miss pairs j ≥ 0.40
                                         tokenizer sha256:c0382117...

OFFICIAL FIRST FAILED GATE:
Gate 1   Format adherence        FAIL    hop2 FORMAT_PASS 23/24 < 1.000
                                         (1 format_scaffold_failure — item i08)
                                         hop1/composite/neg_graph: FORMAT_PASS 24/24

Gate 2   FP16 pass rate          FAIL    (diagnostic — Gate 1 already failed)
  hop1:           9/24    threshold ≥ 21/24   FAIL
  hop2:           23/24   threshold ≥ 21/24   PASS  (Gate 1 contaminated)
  composite:      20/24   threshold ≥ 21/24   FAIL
  negative_graph: 0/24    (abstention contract)

Gate 3   Op. fidelity            BLOCKED by Gate 1 / Gate 2
  wrong_chain_routing: 4/24  (ceiling ≤ 3/24 — would fail independently)

Gate 5   Dummy ceiling           PASS*   max_det = 0/24 ≤ 9/24
                                         * positional-coverage gap: ct at pos 6 for all 24 items;
                                           always_return_second_C (= always_return_ct) = 24/24
                                           composite — not tested by current dummy set.
                                           See CELL02-GATE5-POSITIONAL-DUMMY-AUDIT.md.
Gate 6   Stress eligibility      NOT ELIGIBLE
Track B:                          BLOCKED

Branch:  3 — Gate 1 FAIL (first), Gate 2 FAIL (diagnostic), classifiable failures
Routing: Claim B dirty cell — second constructibility-boundary data point
```

**Note on i08/hop2 FORMAT_COMPLIANCE_LOSS:** Raw output `'ANSWER: ZBCDF maps to AJLAC.'` — model reproduced the full fact sentence after the ANSWER scaffold. AJLAC (correct ct for i08) was present in the output; the strict bare-token contract was violated. Classified as FORMAT_COMPLIANCE_LOSS: isolated, orthogonal format-only event. No construction-linked cause identified. See CELL02-HOP2-FSF-INSPECTION-TWOHOP-L1.md.

---

## 4. Per-axis classification

### Axis A — Contract / abstention behavior

```
Query type:        negative_graph
Correct NULL:      0/24
Endpoint return:   23/24 wrong_chain_selection + 1/24 target_chain_wrong_neighbor
                   (i20 returned anchor_A = ZBATA, not a C-endpoint)

Status: Same structural pattern as Cell01 (0/24 correct NULL; 2/24 in Cell01 also
        clustered in C_target-first which is absent in Cell02).
        NULL-calibration fragility persists regardless of ordering condition.
        No improvement in abstention behavior under all-C_target-last.

Label confidence:  HIGH — 0/24 correct NULL is a clean floor measurement.
                   No ambiguity in classification.
```

### Axis B — Content / distractor / chain-selection

```
Composite query:
  Correct:               20/24
  wrong_chain_selection: 4/24   (items i01, i12, i15, i21)
  wrong_chain_routing_rate: 4/24 (ceiling ≤ 3/24 — Gate 3 FAIL diagnostic)

hop2 (pure chain-following, no selection required):
  Correct:               23/24  (1 FSF on i08)
  hop2 is structurally clean — no selection pressure, single visible answer.

Composite wrong_chain_selection in Cell02 (4/24) matches Cell01 (4/24) exactly.
The chain-selection fragility rate is stable across the two cells despite the
ordering change. Axis B appears ordering-independent at this sample size.

Note on composite/hop1 overlap in Cell02:
  i01: hop1 NULL, composite wrong_chain
  i12: hop1 target_chain_wrong_neighbor, composite wrong_chain (same token: UDNSZ = ct12 returned as wrong_chain for composite)
  i15: hop1 NULL, composite wrong_chain
  i21: hop1 correct, composite wrong_chain (independent — no hop1 failure)

3/4 composite failures co-occur with hop1 failures (same pattern as Cell01).
i21 remains an independent chain-selection failure independent of hop1.

Label confidence:  MEDIUM for i12 composite failure.
  i12 hop1 returned ct12 (target_chain_wrong_neighbor) and composite also returned ct12
  rotated from another item (UDNSZ). The two failures involve different tokens but both
  are C-endpoints, consistent with ct-anchoring operating on both query types.
```

### Axis C — Position / ordering

```
hop1 results:
  Correct:                      9/24
  target_chain_wrong_neighbor:  11/15 failures — model returns ct instead of bt
  non_context_return (NULL):    3/15 failures
  wrong_chain_selection:        1/15 failures

hop2 results:
  Correct:                      23/24  (1 FSF on i08 — format, not knowledge)
  hop2 nearly ceiling — target hop2 facts at position 6 are reliably retrieved.

DOMINANT NEW FAILURE — hop1 target_chain_wrong_neighbor (11/15 = 73%):
  All 11 cases: model returned ct (the C_target / hop2 answer at position 6)
  for hop1 queries (which expect bt at position 5).
  Label: ct-anchoring; cue unresolved.
  In Cell02, ct was simultaneously adjacent to the hop1 fact, fixed at absolute
  position 6, fixed as second_C for all 24 items, and the correct composite answer.
  All four candidate cues are confounded. "Adjacency-driven" is retired.
  Safe read: Cell02 strengthens the candidate convergence read that the floor may
  involve recurring salient endpoint-return behavior; it does not identify the cue.

Position/ordering hypothesis result: NOT SUPPORTED
  See §6 for full comparison and safe interpretation.
```

---

## 4a. Comparison-integrity caveat

```
Cell02 content metrics are diagnostic downstream of a Gate 1 failure.
Comparisons to Cell01 should be read with that caveat.

Construction-integrity check (CELL02-HOP2-FSF-INSPECTION-TWOHOP-L1.md, 2026-06-08):
  The single hop2 FSF (item i08) has been classified as FORMAT_COMPLIANCE_LOSS
  (isolated, orthogonal format-only event; model demonstrably knew the answer).
  No construction defect was found. Gate 0.5 is confirmed valid.
  The "position/ordering NOT SUPPORTED" conclusion and the ct-anchoring / cue-unresolved
  finding (11/15 hop1 wrong_neighbor) are unaffected.
  This caveat is preserved per filing instructions regardless of classification outcome.
```

---

## 5. Cell02 vs Cell01 comparison

### Raw scores

```
Query type      Cell01 (24 items)   Cell01 C_target-last subgroup (8)   Cell02 (24 items, all-last)
hop1            14/24 (0.583)       8/8  (1.000)                        9/24  (0.375)
hop2            24/24 (1.000)       8/8  (1.000)                        23/24 (0.958) — 1 FSF
composite       18/24 (0.750)       7/8  (0.875)                        20/24 (0.833)
negative_graph  2/24  (0.083)       —                                   0/24  (0.000)
```

### Failure class comparison

```
Failure class                Cell01 hop1 failures    Cell02 hop1 failures
non_context_return (NULL)    6                       3
target_chain_wrong_neighbor  2                       11
wrong_chain_selection        2                       1

Primary Cell01 failure:  NULL (6/10)
Primary Cell02 failure:  target_chain_wrong_neighbor (11/15)
```

The failure profile shifted substantially. Cell01's dominant hop1 failure was NULL-return (especially in the C_target-first group). Cell02's dominant hop1 failure is ct-anchoring (returning ct instead of bt — 11/15 failures). The cue driving ct-anchoring is unresolved in Cell02.

### Composite wrong_chain stability

```
Cell01 composite wrong_chain: 4/24 (i01, i03, i07, i13)
Cell02 composite wrong_chain: 4/24 (i01, i12, i15, i21)
```

Identical rate across cells despite axis change. Axis B (chain-selection fragility) appears stable and ordering-independent.

---

## 6. Position/ordering hypothesis result

```
Hypothesis (pre-registered in CELL02-CONSTRUCTION-PROPOSAL-TWOHOP-L1.md):
  If position/ordering is the primary causal factor for Cell01 hop1 fragility,
  then all-C_target-last should produce hop1 near 24/24.

Result: NOT SUPPORTED.
  Cell02 hop1 = 9/24 — regression from Cell01 overall (14/24) and far below
  Cell01 C_target-last subgroup (8/8).

Safe interpretation:
  This specific all-C_target-last manipulation did not support the
  position/ordering hypothesis as a sufficient explanation of Cell01.
  The Cell01 C_target-last success (8/8) appears item-specific or
  interaction-dependent rather than purely ordering-causal.
  Moving all items to C_target-last did not restore the hop1 floor.

What this does NOT establish:
  This does not establish that position is irrelevant. It establishes that
  this particular manipulation (all-C_target-last with new token identities)
  was not a sufficient intervention to improve hop1.
  The token-identity interaction with context arrangement may be the
  load-bearing variable that Cell01's subgroup analysis could not isolate.

Dominant new signal:
  ct-anchoring; cue unresolved:
  11/15 hop1 failures returned ct (position 6) instead of bt (position 5).
  Four cues were simultaneously true of ct in all 24 items: adjacency/proximity,
  absolute position (pos 6), C-rank slot (second_C), and answer-domain salience.
  Which cue is load-bearing cannot be determined from Cell02 alone.
  This is a new failure pattern not prominently observed in Cell01.
```

---

## 7. Label confidence / ambiguity notes

```
High confidence labels:
  target_chain_wrong_neighbor on hop1: unambiguous — returned token is ct (confirmed
    from item metadata), distinct from bt, well-defined failure class.
  non_context_return (NULL): unambiguous — model returned NULL on a positive graph query.
  hop2 correct (23/24): clean; the 1 FSF is format, not knowledge.
  negative_graph 0/24: clean floor measurement.

Medium confidence:
  i08/hop2 FORMAT_COMPLIANCE_LOSS: correct answer AJLAC present in output; model reproduced
    the full fact sentence after the ANSWER scaffold, violating the bare-token contract.
    Classified as isolated, orthogonal format-only event. See CELL02-HOP2-FSF-INSPECTION.
  i12/composite wrong_chain: composite returned a C-endpoint from a different item's
    ct rotation. Hard to attribute cleanly to distractor pressure vs. ct-anchoring.

Ambiguity note — ct-anchoring cue is unresolved:
  The 11/15 hop1 target_chain_wrong_neighbor pattern cannot be attributed to a single cue.
  In Cell02, four candidate cues were simultaneously true of ct for all 24 items:
    (a) Adjacency / proximity: hop1 at pos 5, hop2 at pos 6 — adjacent
    (b) Absolute position: ct fixed at pos 6 for all items
    (c) C-rank slot: ct fixed as second_C for all items
        (Gate 5 audit: always_return_second_C = 24/24 composite — not tested in run)
    (d) Answer-domain salience: ct is the composite correct answer
  Cell03 is required to break these confounds before attribution is attempted.

NULL-calibration carry-forward:
  0/24 correct NULL on negative_graph. Same structural fragility as Cell01.
  Ordering change had no effect on abstention calibration.
  Axis A remains an open question requiring separate manipulation.
```

---

## 8. Safe interpretation

```
Cell02 is a valid dirty-cell constructibility-boundary data point for Claim B.

What is established:
  1. Two-hop retrieval with 7 facts / 3 chains / FP16 / Qwen2.5-3B-Instruct
     does not reach constructibility floor at n=24 under all-C_target-last ordering.
  2. hop2 retrieval is near-ceiling (23/24) — the target hop2 fact at position 6
     is reliably found. hop2 fragility is not a structural property of this task.
  3. The all-C_target-last ordering exposes a distinct failure mode:
     ct-anchoring on hop1 queries (11/15 failures return ct instead of bt).
     The cue driving this pattern is unresolved; four candidate cues were confounded.
     Cell02 strengthens the candidate convergence read that the floor may involve
     recurring salient endpoint-return behavior; it does not identify the cue.
  4. Composite wrong_chain_selection rate (4/24) is stable across cells —
     suggesting Axis B fragility is ordering-independent.
     NOTE: composite (20/24) does not exclude the always_return_second_C shortcut —
     this shortcut was not tested (Gate 5 coverage gap). See §3 Gate summary.
  5. NULL-calibration (Axis A) is unchanged by ordering — 0/24 correct NULL in both cells.
  6. The position/ordering hypothesis (Axis C) is not supported as a sufficient
     explanation of Cell01 hop1 fragility.

What is NOT established:
  See §9.
```

---

## 9. Forbidden interpretations

```
This result DOES NOT support:
  - Position/ordering is the primary causal factor for hop1 fragility
  - All-C_target-last ordering improves hop1 performance
  - Cell02 failure mechanism is the same as Cell01
  - Cell01's C_target-last subgroup (8/8) was a reliable ordering effect
  - Any mechanism, seam, compression, or Claim A/C conclusions
  - Stress eligibility (Gate 2 FAIL)
  - INT8/INT4 comparisons
  - That cell-level token identities are a controlled variable between cells
  - That adjacency is the identified or confirmed cue for ct-anchoring
    (cue is unresolved across adjacency, absolute position, C-rank, and answer-domain salience)
  - That composite (20/24) excludes a return-second_C / return-ct positional shortcut
    (Gate 5 coverage gap; shortcut not tested)
```

---

## 10. Recommended next-axis implication

Cell03 is the attraction-cue mapping step. See CELL03-AXIS-DECISION-MEMO.md for full requirements.

```
Cell03 framing (per Team Lead memo 2026-06-08):
  Cell03 is attraction-cue mapping, not a generic adjacency test.
  The tested axis is adjacency / proximity between target chain hop1 and hop2 facts.
  Cell03 must balance ct absolute position and C-rank across items — not hold them fixed.
  Cell03 re-baselines the adjacency question under corrected controls.

Pre-authorization requirements for Cell03 (not authorized by this entry):
  1. Scorer amendment: add full-rank C dummies (second_C, always_return_ct,
     always_return_answer_shaped). Requires Manager authorization and new scorer hash.
  2. Position/C-rank balance design confirmed by Team Lead.
  3. Manager authorization for construction and scorer amendment.

Current state:
  Axis C (position/ordering) — NOT SUPPORTED as sufficient explanation.
  ct-anchoring cue — UNRESOLVED across four candidate dimensions.
  Gate 5 — PASS* for current dummies; always_return_second_C gap must be closed in Cell03.
  Axis B (chain-selection) — stable at 4/24 across both cells.
  Axis A (abstention) — unchanged by ordering (0/24 both cells).
```

---

**Cell02 map entry complete. Second dirty-cell constructibility-boundary point filed for Claim B.**

— CS Engineer, 2026-06-08
