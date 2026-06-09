# Cell02 Construction Proposal — Two-Hop Level 1

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Requested by:** Team Lead memo — "Cell02 Axis Decision — Position / Ordering Selected for Construction Proposal" 2026-06-08
**Status:** PROPOSAL ONLY — no construction authorized; Manager decision required before any generation

---

## 1. Selected axis

```text
Axis:         Position / ordering
Variable:     Context position of the target hop2 fact (T-hop2)
Manipulation: Eliminate the C_target-first ordering condition (T-hop2 at position 2)
              Replace with all-C_target-last (T-hop2 at position 6) for all 24 items
```

This is the single axis identified in CELL02-AXIS-DECISION-MEMO.md as the cleanest
causal candidate from Cell01.

---

## 2. Exact planned manipulation

### Cell01 ordering (reference)

```text
Design:           8+8+8 mixed ordering
Items 1-8:        C_target-first  — T-hop2 at context position 2  (hop1: 0/8 correct)
Items 9-16:       C_target-middle — T-hop2 at context position 4  (hop1: 6/8 correct)
Items 17-24:      C_target-last   — T-hop2 at context position 6  (hop1: 8/8 correct)

hop2 all groups:  8/8 correct (no ordering effect on B→C retrieval)
```

Within Cell01, a monotonic relationship holds between T-hop2 context position and hop1 pass rate:

```text
T-hop2 at position 6 → hop1: 8/8 (100%)
T-hop2 at position 4 → hop1: 6/8 (75%)
T-hop2 at position 2 → hop1: 0/8 (0%)
```

The C_target-first condition (position 2) accounts for the entire observed hop1 deficit.
The C_target-last condition (position 6) produced zero hop1 failures in Cell01.

Source: item-level JSON confirmed 2026-06-08 (RESULTS-TWOHOP-L1-cell01-1780912218.json).

### Cell02 proposed ordering

```text
Design:           All C_target-last
All 24 items:     T-hop2 at context position 6

Rationale:
  Eliminates the C_target-first condition entirely.
  All items constructed under the ordering condition that produced 0 hop1 failures in Cell01.
  Provides 24-item statistical power under a single ordering condition.
  Comparison to Cell01: does the hop1 pass rate increase when C_target-first is absent?

What changes:
  Context ordering — T-hop2 moves from {2,4,6} to all-6.
  Token pools — new 24 items require new token generation (same protocol; new BPE-Jaccard audit).

What does NOT change (see §3):
  Everything else.
```

### Why all-C_target-last rather than a mixed alternative

```text
Option A (proposed): 0+0+24 — all C_target-last
  Cleanest single-condition test.
  All 24 items under the zero-failure ordering condition from Cell01.
  No within-cell ordering variation to confound interpretation.
  Interpretation: any remaining hop1 failures are not attributable to C_target-first ordering.

Option B (alternative): 0+12+12 — C_target-middle and C_target-last, no C_target-first
  Preserves within-cell comparison across two non-failing ordering groups.
  Slightly more complex interpretation.
  Would require Manager choice between Option A and Option B; not both.

Option C (rejected): Keep 8+8+8 but shift all groups later
  C_target-first → C_target-middle; C_target-middle → C_target-last; new third group needed.
  Not a clean inversion — would require defining a new ordering condition.

Recommended for Manager decision: Option A (all C_target-last).
  Most interpretable against Cell01 C_target-last baseline.
  Simplest design consistent with one-axis constraint.
```

---

## 3. Frozen variables

The following must be identical between Cell01 and Cell02.
Any deviation requires a new axis designation and separate Manager authorization.

```text
Model:                  Qwen/Qwen2.5-3B-Instruct
Precision:              FP16
n_items:                24
n_query_types:          4 (hop1, hop2, composite, negative_graph)

Prompt template:        locked (sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e)
Scorer:                 locked (sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd)
Validator:              locked (sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b)
Runner:                 amended runner (sha256:f346e4f2...) or functionally identical successor

Relations:
  relation_hop1:        'links to'
  relation_hop2:        'maps to'
  relation_hold:        'holds'

Context length:         7 facts per item
Chains per item:        3 (target + decoy_1 + decoy_2)
Query wording:          locked template (same QUERY_TEXT dict)
negative_graph semantics: T-hop2 edge removed; valid_A_to_C_path_exists=False required
Dummy baseline rules:   same compute_dummy_baseline_scores() function (locked scorer)

Thresholds (locked):
  Gate 1 FORMAT_PASS:   1.000 per query type
  Gate 2 pass rate:     ≥ 21/24 per query type (hop1, hop2, composite)
  Gate 3 ceilings:      stopped_short ≤ 3/24; shortcut_single ≤ 2/24;
                        wrong_chain ≤ 3/24; wrong_neighbor ≤ 3/24; anchor_echo ≤ 3/24
  Dummy ceiling:        max_dummy ≤ 9/24; composite − max_dummy ≥ 0.40
  BPE-Jaccard:          j ≥ 0.40 under run tokenizer sha256:c0382117...
  Levenshtein:          k ≤ 2
  Trigram-Jaccard:      j ≥ 0.20

Token-construction constraints:
  Tokens must pass Gate 0.5 audit under sha256:c0382117... (FP16 run tokenizer).
  All near-miss declared pairs must satisfy j ≥ 0.40.
  BPE round-trip must pass for all C-role tokens.
  Token pools are new for Cell02 (Cell01 tokens are not reused).

Decoding:               temperature=0.0, max_tokens=16
Failure taxonomy:       v1.0 (FAILURE_TAXONOMY_VERSION unchanged)
```

---

## 4. Diagnostic predictions

The following decision rules are the interpretive framework for Cell02.
They are pre-registered here before any Cell02 items are generated or run.
No outcome is assumed.

### Primary prediction — position / ordering causal

```text
Trigger: hop1 NULL failure rate drops substantially relative to Cell01 C_target-first
         baseline; hop1 overall approaches or exceeds Gate 2 threshold (≥ 21/24)

Cell01 within-cell evidence:
  C_target-last hop1: 8/8 (100%) — zero failures at position 6

Expected result if position is causal:
  Cell02 hop1 (all C_target-last): ≥ 18-24/24
  Cell02 composite: likely improves proportionally (cell01 C_target-last composite: 7/8)
  hop2: expected 24/24 (was uniformly 8/8 across all groups in Cell01)

Interpretation:
  Ordering is a confirmed causal contributor to the hop1 deficit.
  The C_target-first condition (T-hop2 at position 2) is load-bearing for the Cell01 failure.
  This does not close the seam hypothesis; it constrains the Claim B floor.
```

### Position supported, chain-selection independent

```text
Trigger: hop1 improves to ≥ Gate 2 threshold, but composite wrong_chain_selection
         remains above Gate 3 ceiling (> 3/24)

Interpretation:
  hop1 positional instability and composite chain-selection fragility are separable.
  Removing the positional confound fixes hop1 but does not eliminate distractor pressure
  on composite. i13-type independent chain-selection fragility (hop1 correct, composite
  wrong_chain) may replicate.
  Next axis after Cell02 would be content / distractor geometry (Axis B).
```

### Position insufficient — content / distractor dominant

```text
Trigger: hop1 NULL failures persist despite ordering change; rate remains ≥ Cell01 overall
         (14/24 or worse)

Interpretation:
  The failure is not primarily driven by T-hop2 context position.
  Token identity, distractor geometry, or context-independent content factors dominate.
  Next axis should shift to content / distractor pressure (reduce decoy chains, change
  distractor placement, or add NULL-calibration instruction).
```

### Mixed outcome

```text
Trigger: hop1 improves but does not reach Gate 2 threshold; composite varies

Interpretation:
  Position is a partial contributor, not the sole causal factor.
  Both positional and content axes require further exploration.
  Record as mixed and do not assert a single causal conclusion.
```

### Null / no-improvement outcome

```text
Trigger: Cell02 shows no improvement over Cell01 on hop1 or composite;
         Gate 2 still fails

Interpretation:
  Position alone is insufficient. Cell02 would still be a dirty-cell result for Claim B.
  Consider NULL-calibration gate or capacity-control design as next alternative.
  Do not redesign Cell02 without separate Team Lead / Manager authorization.
```

### Full improvement outcome

```text
Trigger: hop1, hop2, and composite all reach Gate 2 threshold (≥ 21/24);
         Gate 1 FORMAT_PASS = 1.000; Gate 3 ceilings not exceeded

Interpretation:
  Cell01 was position-contaminated. Removing C_target-first restores constructibility.
  Cell02 would be stress-eligible (Gate 6 eligibility subject to Gate 3+ review).
  This is the most favorable outcome for Claim B.
  NOTE: stress eligibility would require separate Manager authorization before any INT8/INT4 run.
```

---

## 5. Gate expectations

Cell02 must clear gates in order. A failed gate blocks all subsequent stress claims.

```text
Gate 0    Axis-control & manifest
  Required: 24/24 validate_manifest PASS
  Cell02 axis: single (token identities vary across items; all C_target-last ordering)
  identical_context_hash: must be present and verified on all items
  negative_graph path_exists=False: must be confirmed on all items

Gate 0.5  Token-construction audit
  Required: BPE round-trip 0 failures; Lev ≤ 2 violations 0; trigram-Jaccard violations 0
  BPE-Jaccard under sha256:c0382117...: 0 cross-chain C violations; all near-miss pairs j ≥ 0.40
  All token construction must be audited before any model inference.

Gate 1    Contract adherence
  Required: FORMAT_PASS = 1.000 per query type (all 4)
  If Gate 1 fails, result is a runner/environment issue, not a model-behavior finding.
  Chat template (Qwen2.5-Instruct format) must be applied as in Cell01 amended runner.

Gate 2    FP16 baseline correctness
  Required for stress eligibility: ≥ 21/24 per query type (hop1, hop2, composite)
  Primary diagnostic gate for the position / ordering hypothesis.
  If hop1 reaches ≥ 21/24 and composite reaches ≥ 21/24: Gate 2 PASS → stress eligible
    (subject to Gates 3-5).
  If hop1 fails again: position hypothesis weakened or refuted; no stress eligibility.

Gate 3+   Operation fidelity, classifier reliability, control adequacy
  Evaluated only if Gate 2 passes.
  wrong_chain ceiling ≤ 3/24 applies to composite.
  Dummy baseline ceiling max_dummy ≤ 9/24 applies.
  UNCLASSIFIED ceiling ≤ 0.05 applies.

Gate 6    Stress eligibility
  NOT ELIGIBLE by default; becomes discussable only if Gates 0-5 all pass.
  Stress eligibility for Cell02 requires separate Manager authorization even if
  all gates pass.
```

---

## 6. Artifact requirements

The following artifacts are required before any Cell02 model inference.
All are offline — no model inference during preparation.

```text
A1  Cell02 item JSON
    Path: tier0-run/items_twohop_l1_cell02.json (proposed path)
    Required: 24 items, all C_target-last ordering
    Validation: 24/24 validate_manifest PASS
    Hash: sha256 to be recorded at generation time

A2  Gate 0.5 token-construction audit
    Run under sha256:c0382117... (FP16 run tokenizer)
    Required: 0 round-trip failures; 0 cross-chain C violations; all declared near-miss
    pairs j ≥ 0.40; all Levenshtein near-miss pairs k ≤ 2; trigram-Jaccard j ≥ 0.20
    Audit artifact: BPE-JACCARD-INSPECTION-TWOHOP-L1-CELL02.md (proposed)

A3  Dummy baseline verification
    Offline computation from item JSON (no model inference)
    Required: max_dummy ≤ 9/24; dummy structure consistent with locked scorer

A4  Runner dry-run
    python runner_twohop_l1.py --dry-run (amended runner sha256:f346e4f2... or successor)
    Required: all provenance hash checks PASS; manifest 24/24 PASS; chat-template OK
    No model inference performed.

A5  Stage 1 Preparation Lock Packet for Cell02
    Documents items_hash, runner_hash, scorer_hash, validator_hash, prompt_template_hash,
    tokenizer_hash (sha256:c0382117...), threshold set, axis specification
    Required before any Stage 1 execution authorization request

A6  No-model-inference confirmation
    Explicit statement in lock packet that all A1-A5 artifacts were produced without
    model inference.
```

---

## 7. Claim boundaries

Cell02 is a position / ordering axis test under the Two-Hop Level 1 construction.
The following claims are forbidden regardless of Cell02 outcome.

```text
No stress result from Cell02 unless Gate 6 explicitly determined eligible.
No INT8 or INT4 result. No compression result.
No seam result. The seam hypothesis (INT4 causes composite-vs-component degradation)
  requires a stress-eligible clean cell. Cell02 tests constructibility, not quantization.
No mechanism claim. Cell02 cannot establish why position/ordering affects hop1 retrieval.
No general capability claim. Cell02 is one construction. hop1 failure or pass on Cell02
  does not generalize to other task designs, context lengths, or model families.
No Track B result. Track B is not authorized.
No Claim C test. Claim C requires a stress-eligible clean cell; Cell02 must first
  establish stress eligibility.
No cross-cell comparison claim without explicit authorization.
  If Cell02 passes and Cell01 failed, the safe statement is: under the all-C_target-last
  construction, the cell reached the constructibility floor; under the 8+8+8 mixed
  construction including C_target-first, it did not.
```

Safe interpretation form for a position-causal Cell02 result (placeholder — to be filled
after actual run):

```text
Under the locked Two-Hop Level 1 construction at 3B FP16 with all-C_target-last ordering,
Cell02 [reached / did not reach] the constructibility floor. [Summary of gate results.]
The Cell01 C_target-first deficit [was / was not] replicated in Cell02. The position /
ordering manipulation [is / is not] sufficient to explain the Cell01 hop1 failure pattern.
```

---

## 8. Carry-forward watch items from Cell01

The following Cell01 observations are recorded as watch items for Cell02.
They are not the selected axis and must not be acted on in Cell02 design.

```text
Negative_graph endpoint-return behavior:
  Cell01: 2/24 correct NULL; 22/24 endpoint return.
  Cell02 watch: does endpoint-return rate change under all-C_target-last?
  Note: no change to prompt or NULL-calibration instruction is authorized for Cell02.
  If the rate changes, record for future NULL-calibration axis consideration.

Per-item distractor preference:
  Cell01: all 4 composite wrong_chain failures returned the same token on both composite
  and negative_graph.
  Cell02 watch: does consistent per-item distractor preference persist with new tokens?

C-endpoint over-retrieval on hop1:
  Cell01: i06, i08, i15 returned target chain answer_C (= hop2 correct answer) on hop1 query.
  Cell02 watch: does this pattern appear with all-C_target-last? Prediction: less likely
  if C_target-first context position 2 was the trigger. If it appears in C_target-last
  items, it is not purely positional.

B-node anchoring / stopped-short:
  Cell01 i22: consistently returned hop1_B across hop1 (correct), composite (stopped_short),
  and negative_graph (wrong_neighbor).
  Cell02 watch: does stopped_short appear in Cell02? If yes, is it associated with a
  specific item pattern?
```

These are diagnostic observations only. No Cell02 design change is authorized to address them.

---

## 9. Manager decision required

```text
Decision requested:
  Authorize Cell02 construction under the following specification:
    Axis:       Position / ordering
    Design:     All C_target-last (T-hop2 at context position 6, all 24 items)
    [OR]        Mixed C_target-middle + C_target-last (Option B)
    Frozen:     All Cell01 locked constants (scorer, validator, prompt, thresholds, model)
    n_items:    24
    Precision:  FP16

Options for Manager decision:
  A. Authorize Option A (all C_target-last, 24 items) — recommended
  B. Authorize Option B (0+12+12: C_target-middle + C_target-last, 12 items each)
  C. Reject proposal — return to axis selection
  D. Request modifications — specify changes and return proposal for revision

If authorized:
  Next step: item generation, token construction, Gate 0.5 audit (all offline).
  Stage 1 execution requires separate Manager authorization after Stage 0 lock.
```

---

## Authorization boundary

```text
This proposal authorizes:
  documentation of the proposed construction
  analysis of Cell01 result
  diagnostic prediction pre-registration

This proposal does NOT authorize:
  Cell02 item generation
  token pool construction
  model inference
  Cell01 rerun
  runner or scorer modification
  threshold changes
  7B, INT8, INT4, Track B
  any run
```

**Cell02 construction requires explicit Manager authorization.**

---

## 10. Key files referenced

```text
RESULTS-TWOHOP-L1-cell01-1780912218.json  — Cell01 item-level result (source for §2 data)
CLAIM-B-MAP-ENTRY-TWOHOP-L1-CELL01.md    — Cell01 multi-axis map entry (Axes A/B/C)
CELL02-AXIS-DECISION-MEMO.md             — Axis decision rationale and one-axis constraint
STAGE0-INSTRUMENT-LOCK-PACKET.md         — Locked Stage 0 instruments (scorer/validator)
STAGE1-PREP-LOCK-PACKET-TWOHOP-L1.md    — Locked Stage 1 preparation (runner/tokenizer)
THRESHOLD-PROPOSAL-TWOHOP-L1.md         — Revision 2 thresholds (all thresholds frozen)
```

---

**Proposal complete. Awaiting Manager authorization before any Cell02 construction begins.**

— CS Engineer, 2026-06-08
