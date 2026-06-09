# RUN-SUMMARY-TEMPLATE-TWOHOP-L1.md

**Template version:** Stage 0 — 2026-06-07
**Usage:** Fill one copy per scored cell run. File as RESULTS-TWOHOP-L1-{cell_id}-{query_type}.md.
**Fields marked [FILL] must be completed before any run result is reported.**

---

## 1. Run identity

```
Date:              [FILL]
Cell ID:           [FILL]
Query type:        [FILL — hop1 | hop2 | composite | negative_graph | length_matched]
Model:             [FILL]
Precision:         [FILL — FP16 | INT8 | INT4]
Runner script:     [FILL]
Authorization:     [FILL — cite Manager memo date and subject]
Status:            [FILL — PASS | FAIL | UNINTERPRETABLE]
```

---

## 2. Gate results (ordered — a failed gate blocks all below)

```
Gate 0    Axis-control & manifest    [PASS | FAIL]
Gate 0.5  Token-construction audit   [PASS | FAIL]
Gate 1    Contract adherence         [PASS | FAIL]
Gate 2    FP16 baseline correctness  [PASS | FAIL — split: hop1=x/n hop2=x/n composite=x/n]
Gate 3    Operation fidelity         [PASS | FAIL — stopped_short=x shortcut=x wrong_chain_routing=x]
Gate 4a   Classifier reliability     [PASS | FAIL — unique_assignment_rate=x unclassified_rate=x]
Gate 4b   Failure-class separability [PASS | FAIL]
Gate 5    Control adequacy           [PASS | FAIL]
Gate 5.5  Baseline-stability confirm [N/A | PASS | FAIL — Manager-authorized only]
Gate 6    Stress eligibility         [ELIGIBLE | NOT ELIGIBLE]

First failed gate:    [FILL or NONE]
Blocking reason:      [FILL if any gate failed]
```

---

## 3. Provenance (all fields required in output artifact)

```
manifest_hash:              [FILL — sha256:...]
scorer_hash:                [FILL — sha256:...]
validator_hash:             [FILL — sha256:...]
runner_hash:                [FILL — sha256:...]
tokenizer_hash:             [FILL — sha256:...]
prompt_template_hash:       [FILL — sha256:...]
failure_taxonomy_version:   v1.0
model_tag_digest:           [FILL]
decoding_settings:          [FILL — temperature=x, max_tokens=x, sampler=...]
axis_configuration:         [FILL — which axes vary, which are frozen]
frozen_settings:            [FILL]
raw_output_path:            [FILL]
per_item_failure_label_path:[FILL]
unclassified_outputs_path:  [FILL]
```

---

## 4. Scoring breakdown

```
n_items:          [FILL]
pass_count:       [FILL]
pass_rate:        [FILL]
feasibility_gate: [FILL — ≥ x / n]
result:           [PASS | FAIL]

scaffold_class:
  SCAFFOLD_PRESENT: [FILL]
  SCAFFOLD_ABSENT:  [FILL]

format_class:
  FORMAT_PASS: [FILL]
  FORMAT_FAIL: [FILL]

failure_class distribution:
  correct:                       [FILL]
  format_scaffold_failure:       [FILL]
  non_context_return:            [FILL]
  correct_chain_stopped_short:   [FILL]
  anchor_echo:                   [FILL]
  wrong_chain_selection:         [FILL]
  target_chain_wrong_neighbor:   [FILL]
  UNCLASSIFIED_OFF_FRAME:        [FILL]
```

---

## 5. Dummy baseline results

```
Dummy                       Expected score    Feasibility gate    Pass/Fail
always_return_B_target      [FILL]            [FILL]              [FILL]
always_return_anchor_A      [FILL]            [FILL]              [FILL]
always_return_first_C       [FILL]            [FILL]              [FILL]
always_return_last_C        [FILL]            [FILL]              [FILL]
always_return_NULL          [FILL]            [FILL]              [FILL]
always_return_C_decoy_1     [FILL]            [FILL]              [FILL]
always_return_C_decoy_2     [FILL or N/A]     [FILL or N/A]       [FILL or N/A]
uniform_random_expected     [FILL]            N/A                 N/A

max_dummy_score:            [FILL]
feasibility_gate:           [FILL]
max_dummy < gate:           [FILL — OK | FAIL]
```

---

## 6. Operation fidelity diagnostics (Gate 3 — composite queries only)

```
stopped_short_rate:              [FILL]    threshold: [FILL]    [PASS | FAIL]
shortcut_single_hop_rate:        [FILL]    threshold: [FILL]    [PASS | FAIL]
wrong_chain_routing_rate:        [FILL]    threshold: [FILL]    [PASS | FAIL]
wrong_neighbor_routing_rate:     [FILL]    threshold: [FILL]    [PASS | FAIL]
anchor_echo_rate:                [FILL]    threshold: [FILL]    [PASS | FAIL]
```

---

## 7. Control adequacy (Gate 5)

```
length_matched_control:
  token_count_delta:    [FILL]    tolerance: ±[FILL]    [PASS | FAIL]
  control_pass_rate:    [FILL]

same_context_controls:
  hop1_pass_rate:       [FILL]
  hop2_pass_rate:       [FILL]
  composite_pass_rate:  [FILL]
  identical_context_hash verified: [YES | NO]

negative_graph_control:
  null_return_rate:     [FILL]
  forced_endpoint_rate: [FILL]    [PASS | FAIL]
  path_traversal_verified_clean: [YES | NO]

dummy_ceiling_check:    [PASS | FAIL — max_dummy < gate]
```

---

## 8. Watch conditions

```
Novel failure classes this cell:    [FILL — list or NONE]
Novel class trend (saturation):     [FILL — saturating | still expanding | unknown]
UNCLASSIFIED_OFF_FRAME rate:        [FILL]    ceiling: [FILL]    [OK | WARNING]
UNCLASSIFIED clustering observed:   [YES — describe | NO]
```

---

## 9. Per-item failure summary

```
item_id    query_type    returned_token    returned_role    failure_class    is_correct
[FILL]     [FILL]        [FILL]            [FILL]           [FILL]           [FILL]
...
```

Per-item prompt_rendered_hash must be present in the raw output artifact (not required in this summary).

---

## 10. Branch routing

```
Applicable branch:      [FILL — Branch 1 | 2 | 3 | 4 | 5 | 6]
Branch description:     [FILL]
Next action:            [FILL]
Manager authorization required: [YES | NO]
```

Branch reference:
```
Branch 1 — clean cell: recommend targeted INT8/INT4 stress for Manager authorization
Branch 2 — contract/scaffold failure: record boundary evidence
Branch 3 — content/distractor/position failure: route to salience/attraction floor evidence
Branch 4 — control failure: construction invalid, redesign required
Branch 5 — clean FP16, stress, no gap: local null
Branch 6 — components survive, composite drops: candidate linkage-specific stress signal
```

---

## 11. Scope boundary

```
This result applies only to:
  Task:       frozen cell construction [FILL — cell_id]
  Query type: [FILL]
  Context:    [FILL — fact count, token count]
  Prompt:     locked (prompt_template_hash above)
  Tokenizer:  locked (tokenizer_hash above)
  Scorer:     locked (scorer_hash above, FAILURE_TAXONOMY_VERSION=v1.0)
  Decoding:   [FILL]
  Model:      [FILL]
  Precision:  [FILL]

This result does not generalize to:
  other cells
  other query types
  other context orderings
  other model sizes
  other precision levels
  natural-language tasks
```

---

## 12. Clean-cell handoff statement (required if Gate 6 = ELIGIBLE)

```
This cell is clean only with respect to the tested axes: contract adherence,
operation fidelity, failure-class separability, length-matched controls,
same-context controls, and the specified wording/token-construction settings.

It is not clean generally.

If Track B breaks under stress, the first suspect is an unmapped or frozen axis,
not INT4.
```

---

## 13. Forbidden claims

The following claims are forbidden regardless of result:

```
the seam exists / does not exist
quantization breaks reasoning
INT4 is harmful or harmless
this model cannot do two-hop linkage
a constructibility boundary is a capability boundary
a composite drop is linkage degradation without failure-class separability
behavioral evidence implies mechanism
```

Safe form: *Under this frozen construction, at this model size, under these gates,
the task did or did not reach interpretability.*

---

## 14. Authorization chain

```
[FILL — list all prior authorization steps leading to this run, in order]
```

---

## 15. Files

```
[FILL — list raw output JSON, this summary, manifest, scorer, runner]
```
