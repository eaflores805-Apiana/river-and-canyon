# Run Summary — Two-Hop Level 1 Cell03
## Standard Return Packet — Constructibility Run

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Status:** COMPLETE — AWAITING TEAM LEAD DISPOSITION
**Format:** Standard Return Packet Policy (Team Lead memo 2026-06-08)
**Per:** Manager / Team Lead memo — "Authorized — Execute One Cell03 FP16 Run Only" 2026-06-08

---

## 1. Run identity

```
cell_id:          twohop_l1_cell03
run_id:           RESULTS-TWOHOP-L1-cell03-1780948339
date:             2026-06-08
model:            Qwen/Qwen2.5-3B-Instruct
precision:        FP16
model_snapshot:   aa8e72537993ba99e69dfaafa59ed015b17504d1
n_items:          24
n_queries:        96 (24 items × 4 query types)
axis_under_test:  adjacency / proximity
design:           3-group balanced; neighbor fact interposed between target hop1
                  and hop2 in ALL 24 items; gap = 2 (adjacency broken).
                  Group A: ct first_C  pos 3 (items 1-8)
                  Group B: ct second_C pos 5 (items 9-16)
                  Group C: ct third_C/last_C pos 7 (items 17-24)
rng_seed:         20260615
authorized_scope: one FP16 run only — locked Cell03 construction packet
purpose:          attraction-cue mapping under broken adjacency and balanced
                  rank / position controls — characterization / re-baseline
```

---

## 2. Authorization boundary

```
Authorized:
  Load FP16 model (Qwen/Qwen2.5-3B-Instruct)
  Run locked Cell03 item set through locked runner
  Score outputs with locked scorer sha256:b65c6803...
  Produce raw and scored outputs
  Produce Run_Summary with mandatory §8 endpoint-intrusion diagnostics
  Update EXPERIMENT_LOG

Not authorized:
  INT8 run
  INT4 run
  rerun
  confirmation pass
  prompt repair
  Track B
  Claim C testing
  stress eligibility declaration
  Gate 3 endpoint-intrusion threshold lock
  mechanism claims
  seam claims
  compression claims
```

---

## 3. Provenance match table

Expected hashes from CELL03-CONSTRUCTION-PACKET.md and CELL03-PREP lock packet.
Observed hashes from run artifact provenance block
(RESULTS-TWOHOP-L1-cell03-1780948339.json).

```
Artifact           Expected hash                                                              Observed hash                                                              Status
Cell03 manifest    sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1   sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1   MATCH
Runner             sha256:f23d99dfefcf6d12378b97246c28f5488fed7c8f755145211f67f7f93ed804b2   sha256:f23d99dfefcf6d12378b97246c28f5488fed7c8f755145211f67f7f93ed804b2   MATCH
Prompt template    sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e   sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e   MATCH
Scorer             sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde   sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde   MATCH
Validator          sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b   sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b   MATCH
Tokenizer          sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539   sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539   MATCH
Model snapshot     aa8e72537993ba99e69dfaafa59ed015b17504d1                                  aa8e72537993ba99e69dfaafa59ed015b17504d1                                  MATCH
```

**All 7 artifacts: MATCH. No provenance deviations. Interpretation may proceed.**

Runner amendment note: mlx_lm API update required — `temp` kwarg removed;
replaced with `make_sampler(temp=0.0)` from mlx_lm.sample_utils; `stream_generate`
yields `GenerationResponse` objects (`.text` field). Decoding behavior unchanged:
greedy (temperature=0.0). Functionally equivalent to Cell02 runner.

---

## 4. Output artifacts

```
raw_output_json:    RESULTS-TWOHOP-L1-cell03-1780948339.json
raw_output_hash:    sha256:f29783622fb14caca1c2a5829da8b874836add5d111356ea42be1f7d4a7b73f7
scored_output_json: RESULTS-TWOHOP-L1-cell03-1780948339.json
scored_output_hash: sha256:f29783622fb14caca1c2a5829da8b874836add5d111356ea42be1f7d4a7b73f7

Note: raw output and scored output are the same artifact.
Scoring and §8 diagnostics are computed inline by the runner; the single JSON
contains raw_output, all scored fields (failure_class, is_correct, returned_token,
returned_role, scaffold_class, format_class, dummy_baselines), and
s8_diagnostics per result record.

run_summary:            RESULTS-TWOHOP-L1-cell03-ALL.md (this document)
experiment_log_entry:   EXPERIMENT_LOG.md (updated 2026-06-08, Cell03 section)
```

---

## 5. Gate table

```
Gate    Name                        Status     Metric / threshold / result
──────────────────────────────────────────────────────────────────────────────
Gate 0  Manifest schema             PASS       validate_manifest: 24/24
                                               threshold: 24/24
                                               notes: carried from construction packet

Gate 0.5 Token construction audit  PASS       lev violations: 0
                                               trig violations: 0
                                               BPE-j violations (C-role): 0
                                               declared near-miss pairs j ≥ 0.40: 24/24
                                               tokenizer: sha256:c0382117...
                                               notes: carried from construction packet

Gate 1  Format adherence            PASS       hop1      FORMAT_PASS: 24/24 = 1.000  PASS
                                               hop2      FORMAT_PASS: 24/24 = 1.000  PASS
                                               composite FORMAT_PASS: 24/24 = 1.000  PASS
                                               neg_graph FORMAT_PASS: 24/24 = 1.000  PASS
                                               threshold: 1.000 per query type
                                               notes: 0 FSF across all 96 outputs.
                                               First clean Gate 1 across all three cells.

★ FIRST FAILED GATE:
Gate 2  FP16 pass rate              FAIL       hop1:      6/24 = 0.250  FAIL  ←
        (Gate 1 passes)                        hop2:     23/24 = 0.958  PASS
                                               composite: 15/24 = 0.625  FAIL  ←
                                               neg_graph:  6/24 = 0.250  N/A  (contract)
                                               threshold: ≥ 21/24 per query type
                                               notes: hop1 and composite independently fail
                                                 Gate 2. Branch 3.

Gate 3  Operation fidelity          FAIL       stopped_short:       0/24 = 0.000  PASS (≤ 3)
        (diagnostic — Gate 2        (diag.)    wrong_chain:         7/24 = 0.292  FAIL (> 3) ←
         already failed)                       wrong_neighbor:      0/24 = 0.000  PASS (≤ 3)
                                               anchor_echo:         0/24 = 0.000  PASS (≤ 3)
                                               UNCLASSIFIED(comp):  0/24 = 0.000  PASS
                                               denominator: composite FORMAT_PASS = 24
                                               threshold: each ceiling ≤ 3/24
                                               notes: wrong_chain_selection 7/24 exceeds
                                                 ceiling; would fail Gate 3 independently.
                                                 Blocked by Gate 2.
                                               §8 caveat: Gate 3 endpoint-intrusion threshold
                                                 not yet defined; option B guardrail in force.
                                                 composite wrong_neighbor = 0/24 (well within
                                                 existing ≤ 3/24 ceiling).

Gate 4a Classifier reliability      BLOCKED    UNCLASSIFIED_OFF_FRAME: 4/96 = 0.042 (hop1 only)
                                    (diag.)    watch trigger (> 0.02): TRIGGERED on hop1
                                               composite UNCLASSIFIED: 0/24 — taxonomy adequate
                                               notes: 4 UNCLASSIFIED on hop1; all filler or
                                                 A_decoy_2 tokens (ROLE_INERT_FILLER /
                                                 ROLE_OTHER_CONTEXT) — not a taxonomy gap.
                                                 Tokens are in-context but outside the 8 failure
                                                 classes (classifier returns these tokens but
                                                 the failure class is architecturally correct).
                                                 See §8 and §8a for detail.
                                                 Blocked by Gate 1/2.

Gate 4b Failure-class separability  BLOCKED    notes: requires Gate 2 PASS. Not computed.

Gate 5  Control adequacy            PASS       max_det (ceiling-bearing): 8/24 = 0.333 ≤ 9/24
                                               always_return_first_C:  8/24  (Group A = ct)
                                               always_return_second_C: 8/24  (Group B = ct)
                                               always_return_third_C:  8/24  (Group C = ct)
                                               always_return_last_C:   8/24  (Group C = ct)
                                               always_return_ct:      24/24  (ref only)
                                               always_return_NULL:     0/24  (ref only)
                                               Gate 2 composite (15) − max_det (8) = 7 < 10
                                               threshold: max_det ≤ 9/24
                                               notes: Gate 5 max_det ceiling PASS.
                                               NOTE: Gate 2 composite (15) − max_det (8) = 7,
                                               below the 10-item margin (Gate 2d). This is
                                               consistent with Gate 2 FAIL — the margin gate
                                               is only tested when Gate 2 accuracy passes.

Gate 5.5 Baseline-stability confirm N/A        notes: Manager-authorized only. Not applicable
                                               to this constructibility run.

Gate 6  Stress eligibility          NOT        requires Gate 2 PASS on hop1, hop2, composite.
                                    ELIGIBLE   notes: Gate 2 FAIL; cell is not stress-eligible.
                                               INT8 / INT4 / Track B not authorized.
                                               Gate 3 endpoint-intrusion threshold amendment
                                               additionally required before any future
                                               stress-eligibility declaration (guardrail, TL
                                               2026-06-08).
```

---

## 6. Query-type score table

```
query_type       pass_count   fail_count   FORMAT_PASS   dominant_failure_classes
hop1             6            18           24/24         non_context_return (7),
                                                         target_chain_wrong_neighbor (6),
                                                         UNCLASSIFIED_OFF_FRAME (4),
                                                         wrong_chain_selection (1)
hop2             23           1            24/24         wrong_chain_selection (1)
composite        15           9            24/24         wrong_chain_selection (7),
                                                         non_context_return (2)
negative_graph   6            18           24/24         wrong_chain_selection (12),
                                                         target_chain_wrong_neighbor (6)
```

---

## 7. Failure-class breakdown

Counts per query type. Denominator = 24 per query type (96 total).

```
Failure class                   hop1   hop2   composite   negative_graph   total
──────────────────────────────────────────────────────────────────────────────────
correct                           6     23        15            6            50
format_scaffold_failure           0      0         0            0             0
non_context_return (NULL)         7      0         2            0             9
correct_chain_stopped_short       0      0         0            0             0
wrong_chain_selection             1      1         7           12            21
target_chain_wrong_neighbor       6      0         0            6            12
anchor_echo                       0      0         0            0             0
UNCLASSIFIED_OFF_FRAME            4      0         0            0             4
──────────────────────────────────────────────────────────────────────────────────
total                            24     24        24           24            96
```

**Notes:**
- hop1 NULL returns (7/24): non_context_return at NULL token (model abstained). Higher
  than Cell02 (3/24). Consistent with adjacency-broken items creating more hop1 ambiguity.
- hop1 ct-anchoring (6/24): all 6 target_chain_wrong_neighbor cases returned ct.
  See §8 for full breakdown.
- hop1 UNCLASSIFIED (4/24): tokens ZFWWT (i17, filler), ZFXFK (i21, filler?),
  ZFAHA (i22, filler?), ZGUPE (i10, A_decoy_2). All in-context tokens with roles
  ROLE_INERT_FILLER or ROLE_OTHER_CONTEXT — outside the 8 failure classes by design.
- hop2 failure (1/24): i09 returned LLIXH = cd2 (wrong_chain_selection). Isolated.
- composite wrong_chain (7/24): exceeds Gate 3 ceiling of 3/24. See §8 Axis B.
- negative_graph: 6/24 correct NULL, 18/24 endpoint intrusion.
  wrong_chain_selection (12) and target_chain_wrong_neighbor (6).
  See §8 Axis A and §8 endpoint-intrusion table for breakdown.
- UNCLASSIFIED total: 4/96 = 0.042 (all hop1; Gate 4a watch trigger on hop1).

---

## 8. Axis-specific diagnostics

### Axis A — Contract / abstention behavior

```
status:           FRAGILE — improved but below threshold
evidence:         negative_graph correct NULL: 6/24 (Cell02: 0/24; Cell03: +6)
                  Endpoint return (intrusion): 18/24
                  wrong_chain_selection: 12/24; target_chain_wrong_neighbor: 6/24
                  Group A: 3/8 intrusion (5/8 correct NULL)
                  Group B: 8/8 intrusion (0/8 correct NULL)
                  Group C: 7/8 intrusion (1/8 correct NULL)
label_confidence: HIGH for endpoint-intrusion classification
ambiguity_note:   Group A (ct=first_C, pos 3) has markedly better NULL-return
                  than Groups B and C. This asymmetry is notable given the
                  adjacency is equally broken in all groups. With hop2 removed,
                  Group A items have a 6-fact context; the target chain is
                  less prominent by absolute count. May suggest that fewer
                  remaining context facts reduce endpoint-attraction pressure.
                  Not interpretable as an axis result without further mapping.
```

### Axis B — Content / distractor / chain-selection behavior

```
status:           DEGRADED relative to Cell02
evidence:         composite wrong_chain_selection: 7/24 (Cell02: 4/24; increase)
                  Gate 3 ceiling: 3/24 — FAIL (7/24 > 3/24)
                  wrong_neighbor on composite: 0/24 (Gate 3 ceiling met)
                  hop2 wrong_chain: 1/24 (i09 — isolated)
label_confidence: HIGH for wrong_chain_selection classification
ambiguity_note:   wrong_chain_selection increased from 4/24 (Cell02) to 7/24.
                  Adjacency break may have made the target hop2 answer harder
                  to locate, increasing decoy chain selection pressure on composite.
                  This is consistent with adjacency providing a reliable positional
                  shortcut for composite: adjacent hop1/hop2 made the target chain
                  easier to trace. Removing adjacency degrades composite performance
                  more than hoped.
```

### Axis C — Adjacency / proximity behavior (primary axis)

```
status:           ct-ANCHORING PERSISTS; adjacency break does not eliminate it
evidence:         hop1 ct-anchoring: 6/24 (Cell02: 11/24 — reduced but not zero)
                  hop1 correct:      6/24 (Cell02: 9/24 — also decreased)
                  hop1 NULL:         7/24 (Cell02: 3/24 — increased)

  ct-anchoring distribution by C-rank (§8):
    Group A (ct first_C,  pos 3): 2/8 ct-anchored  (i01, i06)
    Group B (ct second_C, pos 5): 2/8 ct-anchored  (i13, i16)
    Group C (ct third_C,  pos 7): 2/8 ct-anchored  (i19, i23)
    UNIFORM: 2/8 per group regardless of C-rank or ct absolute position

  ct-anchoring positional pattern (§8 confirmed):
    All 6 ct-anchoring items: returned_abs_position = ct's position
    All 6: hop1_proximity = 2 (gap from hop1 to ct's position)
    All 6: hop2_proximity = 0 (ct is the hop2 fact endpoint)
    Pattern: model skips to hop2 endpoint despite interposed neighbor fact

label_confidence: HIGH — all 6 ct-anchoring cases confirmed by returned_token
                  matching ct from item metadata; hop1_proximity=2, hop2_proximity=0
                  for all 6 cases.

FINDING: ct-anchoring is reduced by broken adjacency (11 → 6) but not eliminated.
  ct-anchoring rate is UNIFORM across C-rank and ct absolute position (2/8 per group).
  This evidence is AGAINST C-rank or absolute-position alone being the primary driver:
  a rank-driven mechanism would predict higher ct-anchoring when ct is at rank 1 (first_C,
  most salient by position); the data shows no such gradient.
  A proximity-only mechanism would predict no ct-anchoring with gap=2; the data refutes this.
  Residual candidate cues: answer-domain salience (ct is correct composite answer) remains
  uncontrolled. See §10 for interpretation boundary.
```

---

## 8a. Comparison-integrity caveat

```
Cell03 is the first cell with clean Gate 1 (0 FSF). Cross-cell comparison to Cell01
(Gate 1 contaminated by format boundary evidence — 1 FSF on composite) and Cell02
(Gate 1 FAIL — 1 FSF on hop2) should be read with that caveat.

Cell02 content metrics (hop1 ct-anchoring=11/24, composite=20/24) were downstream
of a Gate 1 failure. Cell03 provides the first clean baseline for content metrics
without a Gate 1 confound.

Runner API amendment note: the mlx_lm sampler API changed between Cell02 and Cell03
(temp kwarg → make_sampler; stream_generate yields GenerationResponse). The amendment
is functionally equivalent (greedy decoding, temperature=0.0). The amendment is
documented in the runner and in this packet. Decoding behavior is identical.
```

---

## 9. Prior-cell comparison

```
Metric              Cell01      Cell02      Cell03      Direction
─────────────────────────────────────────────────────────────────
hop1 correct        14/24       9/24        6/24        ↓ decreasing
hop2 correct        24/24       23/24*      23/24       stable
composite correct   18/24       20/24       15/24       non-monotone (↑Cell02, ↓Cell03)
neg_graph correct   2/24        0/24        6/24        non-monotone (↑Cell03)
Gate 1              PASS*       FAIL        PASS        (Cell01 1 FSF on composite; Cell02 1 FSF on hop2)
Gate 2              FAIL        FAIL        FAIL        consistent
Branch              3           3           3           consistent
─────────────────────────────────────────────────────────────────
hop1 ct-anchoring   N/A         11/24       6/24        ↓ reduced but not zero
composite wrong_chain 4/24      4/24        7/24        ↑ increased in Cell03
neg_graph intrusion N/A         24/24       18/24       ↓ reduced
```

*Cell02 hop2: 23/24 FORMAT_PASS; the 1 FSF item had correct semantic answer.

Key cross-cell observation:
- hop1 accuracy has declined monotonically across cells (14 → 9 → 6).
  Breaking adjacency increased NULL-return rate (3 → 7) while ct-anchoring decreased
  (11 → 6). Adjacency break degraded hop1 performance overall.
- Composite accuracy is non-monotone: Cell02 (20/24) improved over Cell01 (18/24)
  under all-C_target-last, but Cell03 (15/24) degraded under broken adjacency +
  balanced layout. Adjacency appears to have been a shortcut that helped composite.
- ct-anchoring uniformity across C-rank (2/8 per group) is the key new finding:
  rank and absolute position are not sufficient to explain the residual anchoring.

---

## 10. Branch routing

```
Branch: 3

Gate 2 FAIL (hop1=6/24, composite=15/24 below ≥21/24 threshold)
Gate 1 PASS (first clean Gate 1 across all three cells)

Branch 3 consequences:
  Cell is NOT stress-eligible.
  No INT8, INT4, or Track B authorized.
  No stress-eligibility declaration.
  Cell03 is a Claim B floor-mapping / characterization boundary point.
```

---

## 11. Safe interpretation

Per Team Lead authorization:

```
Cell03 measures residual ct-attraction under broken adjacency (gap=2) and
balanced rank / position controls.

Findings:
  1. ct-anchoring on hop1 is present at 6/24 under broken adjacency.
     This is reduced from Cell02 (11/24) but not zero.
     Adjacency break is insufficient to eliminate ct-anchoring.

  2. ct-anchoring rate is uniform across C-rank groups (2/8 per group:
     first_C, second_C, third_C/last_C). C-rank is not a discriminating
     predictor of ct-anchoring in Cell03.

  3. All 6 ct-anchoring items: returned_abs_position = ct's absolute position,
     hop1_proximity = 2, hop2_proximity = 0. The model skips hop1→hop2 despite
     the interposed neighbor fact.

  4. hop1 overall accuracy decreased (9/24 → 6/24) with broken adjacency.
     NULL-returns increased (3/24 → 7/24). Breaking adjacency introduced
     more abstention without eliminating endpoint attraction.

  5. Composite accuracy decreased (20/24 → 15/24) under broken adjacency.
     wrong_chain_selection increased (4/24 → 7/24). Adjacency appears to
     have aided composite chain-tracing.

  6. negative_graph NULL-return improved (0/24 → 6/24) but remains fragile
     (18/24 endpoint intrusion). Group A (ct first_C) had markedly better
     NULL-return (5/8) than Groups B and C (0/8 and 1/8).
```

---

## 12. Forbidden interpretations

```
NOT PERMITTED by this document:

  Cell03 proves adjacency caused Cell02 ct-anchoring behavior.
    [No adjacent/non-adjacent within-cell contrast exists. Both Cell02
     and Cell03 are between-cell comparisons with multiple confounded
     changes. A causal adjacency claim requires a within-cell or
     single-variable cell design.]

  Cell03 establishes a mechanism for ct-anchoring.
    [Answer-domain salience (ct is correct composite answer) remains
     uncontrolled. Absolute-position gradient was not observed
     (2/8 uniform), but this does not rule out absolute position as a
     contributing factor. No mechanism claim is warranted.]

  Cell03 establishes stress eligibility.
    [Gate 2 FAIL. Cell is not stress-eligible under any reading.]

  Cell03 proves adjacency did not matter.
    [ct-anchoring rate decreased (11 → 6) which is consistent with
     adjacency being one contributing cue among several. The reduction
     is not zero, and the reduction itself is not established as
     adjacency-causal without additional controls.]

  Cell03 results generalize beyond Qwen2.5-3B-Instruct FP16.
    [Single model, single precision, single cell.]

  §8 ct-anchoring uniformity across groups proves rank does not matter.
    [Uniformity across 3 groups of 8 items each is evidence against rank
     being the sole driver. It does not rule out rank as a partial contributor
     or interaction term in a multi-variable causal model.]
```

---

## 13. Recommended next action

Per Cell03 characterization findings, the primary residual candidate cues are:

```
1. Answer-domain salience (uncontrolled in all three cells):
   ct is always the correct composite answer. This may create a general
   answer-shaped token preference independent of position, rank, or adjacency.
   Controlling this would require a non-standard task redesign.

2. Adjacency vs absolute position partial attribution:
   Cell03 broke adjacency uniformly but also changed absolute positions.
   Group A: ct at pos 3 (not pos 6); Group B: ct at pos 5; Group C: ct at pos 7.
   The uniform 2/8 ct-anchoring across groups suggests position alone is not
   the primary predictor. A within-cell adjacent vs non-adjacent contrast at
   fixed absolute position would be a cleaner test.
```

Suggested next cell axis for Team Lead / Manager consideration:

```
Option X (within-cell adjacent vs non-adjacent contrast):
  Half of Cell04 items: target hop1 adjacent to hop2 (gap=1)
  Other half: target hop1 separated by neighbor (gap=2, as in Cell03)
  Fixed ct absolute position across both halves.
  This would isolate adjacency vs absolute-position in a single cell.

Option Y (answer-domain salience probe):
  Use a cell design where ct is NOT the correct composite answer for some items
  (e.g., swap expected composite answer to a decoy under controlled conditions).
  Requires task-design amendment — may be out of scope for constructibility tier.
```

Both options require Team Lead / Manager authorization. No further Cell04 construction
is authorized by this document.

---

## 14. No-extra-run statement

```
One FP16 run only was authorized and executed.

No rerun was performed.
No INT8 run was performed.
No INT4 run was performed.
No confirmation pass was performed.
No prompt repair was performed.
No track B was executed.
No stress-eligibility declaration was made.
No Gate 3 endpoint-intrusion threshold was locked.
No mechanism claim is made.

Authorization is consumed. The next run (if any) requires separate authorization.
```

---

## §8 Endpoint-Intrusion Diagnostics — Full Table

Mandatory per Team Lead standing requirement.
All 24 items reported for hop1 and negative_graph query types.
Composite and hop2 §8 tables follow.

### §8 Table 1 — hop1 (all 24 items)

```
item_id             grp  ct_rank         fc                              ret_tok   ct      ct_vs_C           b_vs_c              abs_pos  c_rank  h1prox  h2prox
twohop_l1_c03_i01   A    first_C         target_chain_wrong_neighbor     LLIXH     LLIXH   ct                C_target_endpoint   3        1       2       0
twohop_l1_c03_i02   A    first_C         non_context_return              NULL      RPHBK   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i03   A    first_C         non_context_return              NULL      HXPVQ   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i04   A    first_C         non_context_return              NULL      CZFUR   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i05   A    first_C         non_context_return              NULL      RJJZO   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i06   A    first_C         target_chain_wrong_neighbor     YHIJZ     YHIJZ   ct                C_target_endpoint   3        1       2       0
twohop_l1_c03_i07   A    first_C         non_context_return              NULL      OUFOK   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i08   A    first_C         non_context_return              NULL      CLZMW   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i09   B    second_C        wrong_chain_selection           ZHGLB     YJKBM   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i10   B    second_C        UNCLASSIFIED_OFF_FRAME          ZGUPE     GCGMX   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i11   B    second_C        correct                         ZBEVL     RIMFB   not_C             B_endpoint          3        N/A     0       2
twohop_l1_c03_i12   B    second_C        correct                         ZBLAR     KRNJK   not_C             B_endpoint          3        N/A     0       2
twohop_l1_c03_i13   B    second_C        target_chain_wrong_neighbor     ZTPUT     ZTPUT   ct                C_target_endpoint   5        2       2       0
twohop_l1_c03_i14   B    second_C        correct                         ZBGPC     MDUJI   not_C             B_endpoint          3        N/A     0       2
twohop_l1_c03_i15   B    second_C        correct                         ZBNHK     AYKRS   not_C             B_endpoint          3        N/A     0       2
twohop_l1_c03_i16   B    second_C        target_chain_wrong_neighbor     AARQW     AARQW   ct                C_target_endpoint   5        2       2       0
twohop_l1_c03_i17   C    third_C_last_C  UNCLASSIFIED_OFF_FRAME          ZFWWT     LRPTZ   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i18   C    third_C_last_C  non_context_return              NULL      EFSCG   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i19   C    third_C_last_C  target_chain_wrong_neighbor     YNVBT     YNVBT   ct                C_target_endpoint   7        3       2       0
twohop_l1_c03_i20   C    third_C_last_C  correct                         ZBPQV     DYLYG   not_C             B_endpoint          5        N/A     0       2
twohop_l1_c03_i21   C    third_C_last_C  UNCLASSIFIED_OFF_FRAME          ZFXFK     VOTRJ   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i22   C    third_C_last_C  UNCLASSIFIED_OFF_FRAME          ZFAHA     GYKXD   not_C             other               N/A      N/A     N/A     N/A
twohop_l1_c03_i23   C    third_C_last_C  target_chain_wrong_neighbor     AQRJC     AQRJC   ct                C_target_endpoint   7        3       2       0
twohop_l1_c03_i24   C    third_C_last_C  correct                         ZBXRT     LDFVJ   not_C             B_endpoint          5        N/A     0       2
```

**§8 hop1 summary:**

```
hop1 FORMAT_PASS:          24/24
hop1 correct:              6/24
hop1 ct-anchored:          6/24  (all target_chain_wrong_neighbor; all returned ct)
hop1 NULL:                 7/24  (non_context_return)
hop1 wrong_chain:          1/24
hop1 UNCLASSIFIED:         4/24  (in-context non-chain-role tokens)

ct-anchoring by group:
  Group A (first_C,  ct pos 3):  2/8  (i01 abs_pos=3 c_rank=1; i06 abs_pos=3 c_rank=1)
  Group B (second_C, ct pos 5):  2/8  (i13 abs_pos=5 c_rank=2; i16 abs_pos=5 c_rank=2)
  Group C (third_C,  ct pos 7):  2/8  (i19 abs_pos=7 c_rank=3; i23 abs_pos=7 c_rank=3)
  UNIFORM 2/8 across all C-ranks and absolute positions.
  All ct-anchoring items: hop1_proximity=2, hop2_proximity=0.
  Model skips to hop2 endpoint despite neighbor interposed at gap distance 1 before hop2.
```

### §8 Table 2 — negative_graph (all 24 items)

```
item_id             grp  fc                              ret_tok   neg_intrusion  role                           abs_pos  ct_vs_C
twohop_l1_c03_i01   A    correct                         NULL      False          null_no_link                   N/A      not_C
twohop_l1_c03_i02   A    wrong_chain_selection           EFSCG     True           distractor_chain_endpoint      7        other_C
twohop_l1_c03_i03   A    correct                         NULL      False          null_no_link                   N/A      not_C
twohop_l1_c03_i04   A    correct                         NULL      False          null_no_link                   N/A      not_C
twohop_l1_c03_i05   A    wrong_chain_selection           ZTPUT     True           distractor_chain_endpoint      5        other_C
twohop_l1_c03_i06   A    correct                         NULL      False          null_no_link                   N/A      not_C
twohop_l1_c03_i07   A    correct                         NULL      False          null_no_link                   N/A      not_C
twohop_l1_c03_i08   A    wrong_chain_selection           LDFVJ     True           distractor_chain_endpoint      7        other_C
twohop_l1_c03_i09   B    wrong_chain_selection           LLIXH     True           distractor_chain_endpoint      7        other_C
twohop_l1_c03_i10   B    wrong_chain_selection           RPHBK     True           distractor_chain_endpoint      7        other_C
twohop_l1_c03_i11   B    wrong_chain_selection           HXPVQ     True           distractor_chain_endpoint      7        other_C
twohop_l1_c03_i12   B    wrong_chain_selection           CZFUR     True           distractor_chain_endpoint      7        other_C
twohop_l1_c03_i13   B    target_chain_wrong_neighbor     ZBMXF     True           hop1_B                         3        not_C
twohop_l1_c03_i14   B    wrong_chain_selection           ZHAEI     True           distractor_chain_intermediate  N/A      not_C
twohop_l1_c03_i15   B    wrong_chain_selection           ZHQBK     True           distractor_chain_intermediate  N/A      not_C
twohop_l1_c03_i16   B    wrong_chain_selection           CLZMW     True           distractor_chain_endpoint      7        other_C
twohop_l1_c03_i17   C    wrong_chain_selection           YJKBM     True           distractor_chain_endpoint      4        other_C
twohop_l1_c03_i18   C    correct                         NULL      False          null_no_link                   N/A      not_C
twohop_l1_c03_i19   C    target_chain_wrong_neighbor     ZBZCI     True           hop1_B                         5        not_C
twohop_l1_c03_i20   C    target_chain_wrong_neighbor     ZBPQV     True           hop1_B                         5        not_C
twohop_l1_c03_i21   C    target_chain_wrong_neighbor     ZBCOG     True           hop1_B                         5        not_C
twohop_l1_c03_i22   C    wrong_chain_selection           MDUJI     True           distractor_chain_endpoint      4        other_C
twohop_l1_c03_i23   C    target_chain_wrong_neighbor     ZBFYY     True           hop1_B                         5        not_C
twohop_l1_c03_i24   C    target_chain_wrong_neighbor     ZBXRT     True           hop1_B                         5        not_C
```

**§8 negative_graph summary:**

```
neg_graph FORMAT_PASS:          24/24
neg_graph correct NULL:          6/24
neg_graph endpoint intrusion:   18/24

  wrong_chain_selection (C_endpoint):  12/18 — returned decoy C (last decoy at pos 7
                                         in most cases; Group C items i17/i22 returned
                                         decoy at pos 4)
  target_chain_wrong_neighbor (B_endpoint): 6/18 — returned hop1_B token
    All 6: B_endpoint (hop1_B role); Group C items i19, i20, i21, i23, i24 +
           Group B item i13. With hop2 fact removed, model may follow hop1 link
           and return the B_target rather than attempting the second hop.
    Note: i13 (Group B) and Groups C i19-i24 are notable — B_endpoint returned
    on negative_graph is a distinct failure mode from C_endpoint return.

Group breakdown:
  Group A: 5/8 correct NULL, 3/8 intrusion  (3 wrong_chain C_endpoint)
  Group B: 0/8 correct NULL, 8/8 intrusion  (7 wrong_chain + 1 B_endpoint)
  Group C: 1/8 correct NULL, 7/8 intrusion  (2 wrong_chain + 5 B_endpoint)
  Group asymmetry is marked — Group A best, B worst (0/8 correct NULL).
```

### §8 Table 3 — composite (all 24 items, FORMAT_PASS)

```
item_id             fc                              is_correct  ret_tok   ct_vs_C    b_vs_c
twohop_l1_c03_i01   wrong_chain_selection           False       LRPTZ     other_C    C_decoy_endpoint
twohop_l1_c03_i02   wrong_chain_selection           False       EFSCG     other_C    C_decoy_endpoint
twohop_l1_c03_i03   wrong_chain_selection           False       YNVBT     other_C    C_decoy_endpoint
twohop_l1_c03_i04   non_context_return              False       NULL      not_C      other
twohop_l1_c03_i05   wrong_chain_selection           False       VOTRJ     other_C    C_decoy_endpoint
twohop_l1_c03_i06   correct                         True        YHIJZ     ct         C_target_endpoint
twohop_l1_c03_i07   non_context_return              False       NULL      not_C      other
twohop_l1_c03_i08   wrong_chain_selection           False       LDFVJ     other_C    C_decoy_endpoint
twohop_l1_c03_i09   wrong_chain_selection           False       LLIXH     other_C    C_decoy_endpoint
twohop_l1_c03_i10   correct                         True        GCGMX     ct         C_target_endpoint
twohop_l1_c03_i11   wrong_chain_selection           False       HXPVQ     other_C    C_decoy_endpoint
twohop_l1_c03_i12   correct                         True        KRNJK     ct         C_target_endpoint
twohop_l1_c03_i13   correct                         True        ZTPUT     ct         C_target_endpoint
twohop_l1_c03_i14   correct                         True        MDUJI     ct         C_target_endpoint
twohop_l1_c03_i15   correct                         True        AYKRS     ct         C_target_endpoint
twohop_l1_c03_i16   correct                         True        AARQW     ct         C_target_endpoint
twohop_l1_c03_i17   correct                         True        LRPTZ     ct         C_target_endpoint
twohop_l1_c03_i18   correct                         True        EFSCG     ct         C_target_endpoint
twohop_l1_c03_i19   correct                         True        YNVBT     ct         C_target_endpoint
twohop_l1_c03_i20   correct                         True        DYLYG     ct         C_target_endpoint
twohop_l1_c03_i21   correct                         True        VOTRJ     ct         C_target_endpoint
twohop_l1_c03_i22   correct                         True        GYKXD     ct         C_target_endpoint
twohop_l1_c03_i23   correct                         True        AQRJC     ct         C_target_endpoint
twohop_l1_c03_i24   correct                         True        LDFVJ     ct         C_target_endpoint
```

```
composite correct:         15/24
composite wrong_chain:     7/24  (all: returned other_C = C_decoy endpoint)
composite non_context:     2/24  (i04, i07 returned NULL)
composite ct-anchoring:    0/24  (no hop1-hop2 shortcut via ct on composite)

Note: composite ct-return (15/24) is correct by construction. Composite ct-return
  is NOT ct-anchoring — it is the correct answer. This is the reference-only
  always_return_ct behavior (24/24 on composite by definition).
  Standing caveat applies: Gate 5 does not close target-token anchoring as a
  composite shortcut.
```

---

## Standing Caveat

```
Gate 5 does not close target-token anchoring as a composite shortcut.
Composite ct-return is correct by construction and cannot be made
ceiling-bearing without turning the correct answer into a dummy failure.
Composite target-token anchoring remains tracked through §8 diagnostics,
especially hop1 failures returning ct.
```

---

## Appendix A — Per-item failure table (composite summary)

```
item_id             hop1              hop2              composite         neg_graph
twohop_l1_c03_i01   wrong_nbr(ct)     correct           wrong_chain(cd)   correct(NULL)
twohop_l1_c03_i02   non_ctx(NULL)     correct           wrong_chain(cd)   wrong_chain(cd)
twohop_l1_c03_i03   non_ctx(NULL)     correct           wrong_chain(cd)   correct(NULL)
twohop_l1_c03_i04   non_ctx(NULL)     correct           non_ctx(NULL)     correct(NULL)
twohop_l1_c03_i05   non_ctx(NULL)     correct           wrong_chain(cd)   wrong_chain(cd)
twohop_l1_c03_i06   wrong_nbr(ct)     correct           correct           correct(NULL)
twohop_l1_c03_i07   non_ctx(NULL)     correct           non_ctx(NULL)     correct(NULL)
twohop_l1_c03_i08   non_ctx(NULL)     correct           wrong_chain(cd)   wrong_chain(cd)
twohop_l1_c03_i09   wrong_chain       wrong_chain(cd)   wrong_chain(cd)   wrong_chain(cd)
twohop_l1_c03_i10   unclass           correct           correct           wrong_chain(cd)
twohop_l1_c03_i11   correct           correct           wrong_chain(cd)   wrong_chain(cd)
twohop_l1_c03_i12   correct           correct           correct           wrong_chain(cd)
twohop_l1_c03_i13   wrong_nbr(ct)     correct           correct           wrong_nbr(B)
twohop_l1_c03_i14   correct           correct           correct           wrong_chain(cd)
twohop_l1_c03_i15   correct           correct           correct           wrong_chain(cd)
twohop_l1_c03_i16   wrong_nbr(ct)     correct           correct           wrong_chain(cd)
twohop_l1_c03_i17   unclass           correct           correct           wrong_chain(cd)
twohop_l1_c03_i18   non_ctx(NULL)     correct           correct           correct(NULL)
twohop_l1_c03_i19   wrong_nbr(ct)     correct           correct           wrong_nbr(B)
twohop_l1_c03_i20   correct           correct           correct           wrong_nbr(B)
twohop_l1_c03_i21   unclass           correct           correct           wrong_nbr(B)
twohop_l1_c03_i22   unclass           correct           correct           wrong_chain(cd)
twohop_l1_c03_i23   wrong_nbr(ct)     correct           correct           wrong_nbr(B)
twohop_l1_c03_i24   correct           correct           correct           wrong_nbr(B)
```

Legend: ct=ct-anchoring, cd=decoy chain C endpoint, B=hop1_B endpoint, NULL=non_context_return

---

## Appendix B — Authorization chain

```
Claim B / Constructibility Floor — Track A
  Manager / Team Lead: "Authorized — Execute One Cell03 FP16 Run Only" 2026-06-08
  Manager / Team Lead: "Authorized — Construct Cell03 Manifest Only" 2026-06-08
  Senior: Stage 0 lock review PASS (CELL03-STAGE0-LOCK-REVIEW.md, 2026-06-08)
  Manager: scorer re-lock (sha256:b65c6803...) — 2026-06-08
  Manager: Stage 0 instruments locked (STAGE0-INSTRUMENT-LOCK-PACKET.md) — 2026-06-07
  Manager: Gate thresholds locked (THRESHOLD-PROPOSAL-TWOHOP-L1.md Rev 2) — 2026-06-08
  Manager: BPE-Jaccard j ≥ 0.40 amendment locked — 2026-06-08
  Manager: Gate 1 FORMAT_PASS = 1.000 locked — 2026-06-08
```

---

**Construction packet filed. One FP16 run executed. No further runs authorized.**

— CS Engineer, 2026-06-08
