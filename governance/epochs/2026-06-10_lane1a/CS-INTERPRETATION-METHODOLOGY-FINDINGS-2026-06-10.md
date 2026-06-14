# CS Interpretation Memo — Lane 1a Sweep Result: Methodology Findings That Affect Interpretation

From: CS Engineer
To: Team Lead
Cc: Senior Engineer, Manager, New Senior Engineer, Contributors
Date: 2026-06-10
Status: Interpretation submitted; significant methodological findings surfaced; CS recommends sweep-design review BEFORE conclusions are recorded

---

## 0. Headline

The mechanical sweep ran cleanly (1,536/1,536; 0 anomalies). The K=0 verdict is mechanically valid against the pre-registered classification.

**But CS interpretation: three of the five elimination labels are firing for design-artifact reasons that are independent of the candidate's actual behavior.** A clean read of the raw outputs shows the model performs textbook retrieval (≥95% on most rungs; perfect NULL abstention) — yet the sweep eliminates it for reasons traceable to specific design choices in the dummy-policy battery, the control-stratum interpretation, and the abstention-band boundary.

CS recommends Team Lead/Senior review the methodology findings below before this K=0 result is recorded as a substantive observation about this model / task family / scale.

---

## 1. Answers to Team Lead's five questions

### Q1: Do the elimination labels appear consistent with the underlying artifacts and plots?

**Mechanically yes; substantively no on three of the five labels.** Each label trips on the pre-registered rule as written. But on substantive examination, three labels are firing because of design choices, not because of candidate behavior.

### Q2: Methodological considerations to document before any conclusion is recorded

Three substantive findings — see §2 below.

### Q3: Alternative interpretations consistent with the pre-registered analysis

Yes, two: (a) "this model is a near-ideal single-hop retriever on this task family at this scale, and the sweep design eliminates it for instrument-side reasons"; (b) "the sweep design exhibits the classic Lane 1a residual risk Senior flagged in design packet §2 — the audit tables are honest, but they cannot be cleanly read as candidate-behavior conclusions without acknowledging the construction-side facts in §2 of this memo."

### Q4: Limitations of this task family, scale, or sweep design

Several — see §3.

### Q5: Issues warranting additional output audit

Yes — see §4.

---

## 2. Substantive methodology findings (the important ones)

### Finding A — Two of five "dummy policies" achieve 100% accuracy on answerable items by construction

Quantified on L01's manifest (representative; the pattern holds on every rung):

| Dummy policy | Accuracy on L01 answerable items | Intended role | Actual behavior |
|---|---|---|---|
| `pure_last_position` | 13/80 (16.3%) | Last-token bias | Working as intended (~1/(D+1) chance) |
| `target_recency` | **80/80 (100%)** | Recency bias | **DEGENERATE** — predicts value of most-recently-mentioned key matching queried key's first character; since the queried key IS in the in-context list, it matches its own first character at its own position |
| `salient_endpoint` | 13/80 (16.3%) | Endpoint salience | Working as intended (≈ last position) |
| `copy_completion` | 0/80 (0.0%) | Copy bias | Working as intended (queried key ≠ value) |
| `homogeneous_prefix_completion` | **80/80 (100%)** | K=high shared-prefix shortcut | **DEGENERATE** — predicts value of in-context key sharing longest prefix with queried key; since the queried key IS in the list, the longest prefix match IS the queried key itself; returns its value |

The recipe acceptance check (§13 v0.2 §8) required "non-constant prediction vector with ≥ 3 distinct values." Both degenerate policies pass that check because their predictions vary across items (different items have different answer-position values). What the check did not require was "non-degenerate as a shortcut detector." Two policies are not detecting shortcuts — they are performing perfect retrieval.

**Consequences:**
- `max_dummy_score = 1.000` on every rung (one of the two degenerate policies is always at the max)
- `union_envelope_score = 1.000` on every rung (at least one of them is correct on every item)
- The candidate cannot exceed 1.000; therefore `strict_acc ≤ envelope + 2·SE` is **always true** → `accuracy_indistinguishable_from_declared_policy_envelope` **always fires**

This label is unrecoverable under the current dummy-policy battery — it would fire on any candidate that ran this sweep.

### Finding B — The control stratum measures retrieval under scrambled bindings, not token-prior baseline

The control prompts re-shuffle the value pool so the queried key (still in the in-context list) is now paired with a different value. Per `manifest_generator._make_item` for `stratum == "answerable_mirror"`:

```python
if bindings_scrambled:
    rng.shuffle(in_context_values)
# expected_answer = in_context_pairs[answer_pos][1]   # AFTER shuffle
```

A model that performs **proper retrieval** (look up queried key, return value at that position) will get the scrambled value correct — that is what `control_acc` measures. Sample evidence from L01/answerable_mirror item 0:

```text
queried_key:   "rjdyji"   (in the in-context list)
expected:      "echo"     (= value at queried_key's post-scramble position)
raw_output:    "echo"     ← model retrieved correctly
```

`control_acc` on L01 was 0.925 — the model retrieves correctly even on scrambled bindings. That is **evidence FOR proper retrieval**, not evidence of token-prior dependence.

**Consequences:**

- The rule `accuracy_indistinguishable_from_token_prior: strict − control ≤ 2·SE_diff` interprets candidate ≈ control as "candidate ≈ token-prior baseline."
- But what candidate ≈ control actually shows here is **candidate ≈ retrieval-under-different-bindings**, i.e., the model retrieves consistently regardless of which random bindings are present.
- A token-prior-only model would have `control_acc ≈ 1/|value_pool|` (random chance, ~3.8% with our 26-value pool). The observed `control_acc` of 0.76–0.98 is two orders of magnitude above token-prior chance.

The label is firing on **good retrieval behavior** because the control is not isolating the token-prior surface. To actually measure token-prior dependence, the control would need to remove the queried key from the in-context list (closer to the NULL stratum design), or scramble structure so retrieval cannot resolve, not just permute values.

### Finding C — The abstention band excludes ideal abstention discipline

Every rung's NULL-stratum `abstention_rate = 1.000`. From the raw outputs (L01 NULL sample):

```text
queried_key: "tkdtck" (NOT in in-context); expected "NULL"; raw_output "NULL"  ✓
queried_key: "mqebmq" (NOT in in-context); expected "NULL"; raw_output "NULL"  ✓
queried_key: "whvhdv" (NOT in in-context); expected "NULL"; raw_output "NULL"  ✓
```

The model is **perfectly abstaining on every NULL item across every rung**. This is the ideal outcome of the D4 abstention contract.

But the pre-registered rule is:

```
abstention_contract_instability:
  NULL_stratum_abstention_rate NOT IN [0.50, 0.95]   OR
  NULL/error not mechanically separable
```

Rate of 1.000 is outside the upper bound of [0.50, 0.95]. The label fires.

**The band's lower bound of 0.50 catches "model never abstains" (failure mode 1). The upper bound of 0.95 was presumably intended to catch "model over-abstains and answers nothing" (failure mode 2). But a model that ONLY abstains on NULL items and ALWAYS answers on answerable items — the textbook ideal — has rate 1.0 on NULL and rate ~0 on answerable. The band excludes the ideal corner.**

The label is firing on textbook-ideal behavior because the band's upper bound treats "abstains correctly 100% of the time" as a defect.

---

## 3. What the labels would say with the corrected dummy-policy battery (informational projection)

If `target_recency` and `homogeneous_prefix_completion` were re-implemented as **non-retrieval-equivalent shortcuts** (e.g., predicting value of the key that shares the queried key's *prefix-class structure* but is NOT the queried key itself), the projected envelope on this model would be substantially below 1.000 on K=low rungs and around the shortcut-correlation rate on K=high rungs. The candidate's strict_acc of 0.71–0.99 would then need to be compared against an envelope of, say, 0.20–0.40 (random-chance regime), which would NOT fire `accuracy_indistinguishable_from_declared_policy_envelope` on any rung.

This is a projection, not a measurement. CS records it as an "alternative interpretation consistent with the pre-registered analysis structure" per Team Lead Q3.

---

## 4. Audit items worth checking

### Audit A — Format compliance on the strict-content gap

Sample L01/answerable item 2:

```text
queried_key: "dsvpvm"; expected: "juliet"; raw_output: "dsvpvm: juliet"
```

The model emits *"<queried_key>: <value>"* on some items instead of just *"<value>"*. The scorer marks this `content=True` (juliet appears as substring) but `strict=False` (no exact match). This explains the gap that fires `strict_content_gap_instability` on L03.

This is a **format-following defect**, not a retrieval defect. The model knew the answer but expressed it in a richer format than the prompt template specified. With a relaxed scorer (e.g., trailing-token grab after final colon), this gap would close substantially.

CS recommends: the gap label is honest for the current locked scorer, but Senior/Team Lead should note that the underlying retrieval is correct on most "gap" items.

### Audit B — answer_pos_distribution was not populated

The per-rung records carry `answer_pos_distribution: {bin_counts: [], bin_count_total: 0, max_deviation_sigma: 0.0}` — the analyzer driver did not populate it. The recipe required a histogram + 3σ deviation check on per-rung answer-slot positions. Lack of population means the position-distribution sanity check was not actually run on the sweep outputs (it ran on the *manifests* at generation time per `manifest_generator.recipe_acceptance_check_rung`, which is different).

Not blocking for the K=0 verdict (the sanity check is about position uniformity, not classification), but the audit record is incomplete here.

### Audit C — `union_envelope_score = 1.000` flagged but accepted

The audit log shows `analysis_completed` event with no warning about envelope=1.000. CS recommends the analyzer be extended to emit a warning when `union_envelope = 1.000` because that condition strictly disables the envelope check as a discriminator.

---

## 5. What CS interprets as the substantive result (separate from the elimination labels)

Reading the raw outputs directly, the model — Qwen2.5-3B-Instruct, FP16, deterministic — exhibits the following on this task family at this scale:

```text
- Single-hop key→value retrieval works:                  ~71-99% strict accuracy across rungs
- Retrieval is stable under random-binding permutation:   ~76-98% control accuracy
- NULL detection (queried key absent → abstain):          100% across every rung
- Format compliance is imperfect:                          some answers emit "key: value"
                                                           instead of just "value"
                                                           (≈ 16% gap on L03)
- Performance degrades with distractor count D:           L01(D=4) 0.96, L03(D=16) 0.71
                                                           on K=low
                                                           L04(D=4) 0.99, L06(D=16) 0.85
                                                           on K=high
- K=high (shared-prefix) is HARDER than K=low only at D=16: small effect
- Extended context (X=ext) is comparable to base:          L07 ≈ L02; L08 ≈ L05
```

These observations are reading the audit-table content directly. They do NOT depend on the elimination labels (which fired for design-side reasons enumerated above).

**Whether this candidate constitutes a "certifiable baseline" under a corrected dummy-policy battery + corrected control interpretation + corrected abstention band is a question that the current sweep, as instrumented, did not answer.** What the current sweep answers is the K=0 verdict against the pre-registered classification rules — which CS marks as a valid mechanical outcome that the team should examine before treating it as a candidate-behavior conclusion.

---

## 6. CS recommendation

CS records the K=0 mechanical verdict as filed (it is the honest output of the locked analyzer against the locked classification rules running on the locked sweep outputs).

CS recommends that — before this K=0 result is recorded as a substantive observation about the candidate or about the model's certifiability —  the team consider whether:

1. The dummy-policy battery should be re-specified to exclude shortcuts that degenerate to "perfect retrieval" on items where the queried key is in the in-context list.
2. The control stratum should be re-specified to actually isolate token-prior surface (perhaps by removing the queried key from the in-context list AND scrambling bindings).
3. The abstention band's upper bound should be widened or removed (the ideal-abstainer is at 1.0).
4. The scorer should be relaxed to allow `"<queried_key>: <value>"` format if that becomes the model's natural output format.

Each of these is **outside the scope of this sweep** — they are sweep-design decisions for Senior and Team Lead, not CS implementation choices. CS surfaces them because Team Lead's Q1 (label consistency with artifacts) requires it.

If the team accepts that the current sweep design produces a K=0 verdict that conflates "candidate is poorly behaved" with "sweep design has tautological elements," then a follow-up sweep with a corrected design — under fresh Manager authorization, new sweep_id, replayed review chain — would produce a more discriminating measurement.

If the team accepts the K=0 verdict as the substantive Lane 1a finding regardless, CS notes that the Lane 1a doctrine of *negative-use only* is preserved either way: the K=0 verdict cannot be used to certify any candidate or set any threshold. No certification action follows from this sweep regardless of interpretation.

## 7. CS posture

Lane 1a outputs remain negative-use only. No statistic from this sweep may be copied into a threshold-sheet field. No survivor exists to be selected. CS does not advocate for any of the four follow-up changes above as authorized work — they are surfaced because Team Lead asked for an interpretation.

The mechanical sweep is complete. CS interprets the K=0 verdict as a sweep-design outcome that does not yet support substantive conclusions about the candidate's certifiability without methodological revision.

— CS Engineer, 2026-06-10
