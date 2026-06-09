# Stage 1 Run Memo — Two-Hop Level 1
## Draft for Review

**Date:** 2026-06-08
**Author:** CS Engineer
**Status:** DRAFT — preparation complete 2026-06-08; Stage 1 Preparation Lock Packet submitted for Team Lead review. Not an authorization to execute.
**Track:** Track A — Constructibility Mapping
**Precision:** FP16 only
**Model:** Qwen2.5-3B-Instruct

---

## Authorization note

This document is a planning draft only. It describes what Stage 1 entails and what authorization is required before execution. No action described here is authorized by this document.

**This memo does NOT authorize:**

```
cell generation
model inference
Stage 1 execution
confirmation pass
7B pass
INT8 / INT4 stress
Track B
any run
```

---

## 1. Stage 1 purpose

Stage 1 is the first scored cell run under the locked Two-Hop Level 1 instrument. Its purpose is to establish a constructibility map at FP16: does the instrument produce interpretable, gate-passing results at baseline precision for a specific cell construction?

Stage 1 supports Claim B (mappability hypothesis): the constructibility floor is a stable, mappable object at 3B. Stage 1 does not test INT8/INT4 and does not generate Track B stress evidence.

A Stage 1 cell that passes all gates (Gate 0 through Gate 5, reaching Gate 6 = ELIGIBLE) licenses a Track B stress proposal. A Stage 1 cell that fails at any gate generates failure-anatomy evidence and guides construction revision.

---

## 2. Authorization chain (current state)

```
Stage 0 locked:               2026-06-07 (Team Lead)
Threshold set approved:       2026-06-08 (Manager)
BPE-Jaccard j ≥ 0.40:         LOCKED 2026-06-08 (Manager)
Gate 1 FORMAT_PASS = 1.000:   LOCKED 2026-06-08 (Manager)
shortcut_single_hop item:     CLOSED — no validator amendment required
All thresholds:               FULLY LOCKED — no threshold blockers remain
Stage 1 Run Memo:             Submitted for Team Lead final review
Stage 1 cell generation:      NOT AUTHORIZED
Stage 1 execution:            NOT AUTHORIZED — requires separate Manager authorization
```

Stage 1 execution requires, in order:

```
1. BPE-Jaccard j amendment (j ≥ 0.50 → j ≥ 0.40)   DONE — LOCKED 2026-06-08 (Manager)
2. Cell generation authorized (Manager decision)       DONE — Manager authorized 2026-06-08
3. Cell constructed and validated                      DONE (Rev 2) — items_twohop_l1_cell01.json
                                                              sha256:00a7adf8...  24/24 PASS
                                                              3-chain, 7-fact, 8+8+8 ordering
4. Runner script written and hashed                    DONE (Rev 2) — runner_twohop_l1.py
                                                              sha256:ed2fbdc3...
5. Prompt template written and hashed                  DONE — prompt_template_twohop_l1.txt
                                                              sha256:c8a81a29...
6. All Gate 0 / Gate 0.5 pre-run checks passed         DONE — Gate 0 PASS; Gate 0.5 PASS
                                                              (tokenizer hash accepted by
                                                              Team Lead 2026-06-08)
7. Explicit Manager authorization to execute           PENDING — revised lock packet submitted
                                                              to Team Lead 2026-06-08
```

---

## 3. Cell specification

### 3a. Size and structure

**Expected cell size:** n = 24 items

Each item must contain:
- 1 target chain (A → B → C)
- ≥ 1 decoy chain (A' → B' → C'), distinct from target
- 1 planted target_neighbor_decoy (near-miss of C_target, Levenshtein ≤ 2)
- Inert filler facts as needed for context length management
- All 4 required query types: hop1, hop2, composite, negative_graph

### 3b. Token pool requirements

All token-pool identifiers (A, B, C objects and decoys) must satisfy the following before cell finalization:

```
1. BPE round-trip: audit_round_trip() = True for all unique tokens
   (requires tokenizer loaded, no model inference)
2. Levenshtein: no accidental near-misses (unintended pair with edit distance ≤ 2)
3. Trigram-Jaccard: no accidental pair with j ≥ 0.20 except declared near-miss
4. BPE-Jaccard: no accidental cross-chain C-role pair with j ≥ 0.40
   (pending amendment approval)
5. Cross-chain C-role tokens must be drawn from distinct letter families to avoid
   BPE subword collision (see BPE-JACCARD-INSPECTION-TWOHOP-L1.md)
```

### 3c. Item storage

Stage 1 items must be stored in a separate file from `tasks_twohop_l1.py`. The locked validator file must not be amended to add items.

Proposed structure:

```
items_twohop_l1_cell01.json   — item list (JSON), hash separately as manifest_hash
tasks_twohop_l1.py            — validator (locked hash unchanged)
```

The runner loads items from the JSON file and validates them via the locked `validate_manifest()` before any inference is run.

### 3d. Positive sufficiency requirement

Each composite item must declare:

```json
"positive_sufficiency_exclusion": {
  "composite_requires_hop1": true,
  "composite_requires_hop2": true,
  "answer_from_hop1_alone_possible": false,
  "answer_from_hop2_alone_possible": false,
  "validation_method": "manifest_structure"
}
```

The validator rejects items where this is violated. Shortcut_single_hop_rate should be 0 for a validated cell.

---

## 4. Pre-run checklist

All items must be completed and confirmed in writing before any scored run. This checklist maps to the gate sequence.

**Gate 0 — Axis-control and manifest**

```
[x] All 24 items pass validate_manifest() with zero errors
[x] Axis configuration documented: token identities vary; 8+8+8 ordering
    (C_target-first items 1-8, C_target-middle items 9-16, C_target-last items 17-24)
[x] Frozen settings documented:
    relation_hop1='links to'; relation_hop2='maps to'; relation_hold='holds'
    context_length=7 facts; chains_per_item=3 (target + decoy_1 + decoy_2)
    query_phrasing=template; instruction_prefix=prompt_template_twohop_l1.txt
[x] identical_context_hash verified for all same-context control sets
[x] negative_graph_control path verification: valid_A_to_C_path_exists = False
    confirmed by structural inspection (not model inference)
[x] manifest_hash recorded: sha256:00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28
[x] validator_hash confirmed: sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b

Gate 0: PASS
```

**Gate 0.5 — Token-construction audit**

```
[x] BPE round-trip verified for all unique token-pool identifiers (216 tokens)
[x] Levenshtein scan: 0 violations (23,220 pairs audited)
[x] Trigram-Jaccard scan: 0 violations
[x] BPE-Jaccard scan: 0 cross-chain C-pair violations (≥ 0.40)
[x] target_neighbor_decoy confirmed: edit_distance(decoy, C_target) ≤ 2
    AND trigram_jaccard(decoy, C_target) ≥ 0.20
    AND bpe_jaccard(decoy, C_target) ≥ 0.40
[x] tokenizer_hash — ACCEPTED by Team Lead 2026-06-08:
    FP16 HuggingFace: sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
    Note: differs from local int4/int8 hash sha256:3fd169731... (JSON format only;
    vocabulary and normalized merges IDENTICAL)

Gate 0.5: PASS
```

**Provenance assembly (before any model call)**

```
[x] manifest_hash:             sha256:00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28
[x] validator_hash:            sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
[x] scorer_hash:               sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd
                               (amended 2026-06-08 — Option D: line 229 backward-compatible
                               fact_role fix; 22/22 smoke tests, 14/14 unit tests PASS)
[x] runner_hash:               sha256:ed2fbdc3e21375060f15a0645da111c24db890b840d9be476ee24d8bb06c5aaf
[x] tokenizer_hash:            sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
                               (FP16 — accepted by Team Lead 2026-06-08)
[x] prompt_template_hash:      sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
[ ] model_tag_digest:          sha256 of model weights or HuggingFace model card hash (at run time)
[x] decoding_settings:         temperature=0.0, max_tokens=16
[x] failure_taxonomy_version:  v1.0
```

---

## 5. Run specification

**Model:** Qwen2.5-3B-Instruct (FP16)
**Precision:** FP16 only. No INT8 or INT4 in Stage 1.
**Decoding:** temperature=0.0, max_tokens=16 (greedy, deterministic)
  — consistent with Fork A and Exp8A/Exp8B; no change proposed
**Query types to score:** hop1, hop2, composite, negative_graph
  — length_matched is a control, not a primary scored type

**Runner script (not yet written):** The runner must:
1. Load items from items JSON and validate via `validate_manifest()`
2. Compute and record all provenance hashes before the first model call
3. Render each prompt using the locked prompt template; record `prompt_rendered_hash` per item
4. For each item × query type: call model, record raw output, score via `classify_output()`
5. Compute all Run Summary fields (gates, scoring breakdown, dummy baselines, fidelity rates)
6. Write output artifact (JSON) and this Run Summary (MD) to disk
7. Record runner hash in output artifact

**Prompt template (not yet written):** Must specify:
- Instruction prefix (including explicit format instruction: `ANSWER: <TOKEN>` contract)
- Context block rendering order
- Query rendering per query type
- No information about token roles may appear in the prompt

---

## 6. Gate sequence

Gates are evaluated in order. A failed gate blocks all gates below it.

```
Gate 0    Axis-control and manifest
          Pass: all 24 items validate clean; axis configuration documented;
          negative_graph path absence confirmed
          Fail: any item fails validate_manifest(), or axis undocumented

Gate 0.5  Token-construction audit
          Pass: all token-pool checks pass; all provenance hashes assembled
          Fail: any accidental near-miss detected, or BPE round-trip fails,
          or tokenizer hash not confirmed

Gate 1    Contract adherence (FORMAT_PASS rate)
          Pass: FORMAT_PASS = 1.000 per query type (stress eligibility threshold)
          — LOCKED 2026-06-08 (Manager)
          Clarifications (Manager 2026-06-08):
            • NULL / NO_LINK returned under negative_graph contract = FORMAT_PASS
              (format adherence, not correctness)
            • Correctness excluded from Gate 1 denominator
            • Gate 1 evaluated per query type; no cross-type pooling
          Fail: any FORMAT_FAIL at FP16 routes to Branch 2 (format boundary evidence)

Gate 2    FP16 baseline correctness
          Pass: hop1 ≥ 21/24 AND hop2 ≥ 21/24 AND composite ≥ 21/24
          Fail: any query type < 21/24 correct

Gate 3    Operation fidelity (composite only, FORMAT_PASS denominator)
          Pass: all five rates below approved ceilings
            stopped_short     ≤ 3/24
            shortcut_single_hop ≤ 2/24
            wrong_chain       ≤ 3/24
            wrong_neighbor    ≤ 3/24
            anchor_echo       ≤ 3/24
          Fail: any ceiling exceeded

Gate 4a   Classifier reliability
          Pass: UNCLASSIFIED_OFF_FRAME rate ≤ 0.05; unique assignment = 1.000 for FORMAT_PASS
          Watch condition: UNCLASSIFIED > 0.02 triggers mandatory manual inspection

Gate 4b   Failure-class separability
          Pass: failure class distribution is interpretable; no ceiling exceeded
          Fail: failure distribution is degenerate or dominated by UNCLASSIFIED

Gate 5    Control adequacy
          Pass:
            length_matched token_count within ± 10 prompt tokens
            same-context hop1/hop2/composite pass rates internally consistent
            identical_context_hash verified for same-context controls
            negative_graph null_return_rate documented
            dummy check: max_dummy ≤ 9/24 AND Gate-2 composite − max_dummy ≥ 10/24
          Fail: any control check fails

Gate 5.5  Baseline-stability confirmation
          N/A for Stage 1 unless Manager-authorized separately

Gate 6    Stress eligibility
          ELIGIBLE: all gates 0–5 pass
          NOT ELIGIBLE: any gate failed
```

**Gate 1 note:** FORMAT_PASS = 1.000 per query type — LOCKED 2026-06-08 (Manager). NULL / NO_LINK under negative_graph contract = FORMAT_PASS. Correctness excluded. Per query type; no pooling.

---

## 7. Branch routing

```
Branch 1 — all gates pass (Gate 6 = ELIGIBLE)
  Action: prepare Track B stress proposal for Manager authorization
  Note: clean-cell handoff statement required (per RUN-SUMMARY-TEMPLATE §12)

Branch 2 — Gate 1 fails (contract / scaffold failure)
  Action: record boundary evidence; inspect prompt template and token pool
  Note: format failures at FP16 are a construction or prompt problem, not a model problem

Branch 3 — Gate 2 or Gate 3 fails (content / distractor / operation failure)
  Action: route to salience / attraction floor evidence; inspect failure class distribution
  Note: Gate 2 fail = constructibility not established; report item-level anatomy before redesign

Branch 4 — Gate 5 fails (control failure)
  Action: construction invalid; redesign required; do not attempt stress
  Note: negative_graph path not clean, or context hash mismatch = manifest construction error

Branch 5 — Gates 2–3 pass but Gate 6 = NOT ELIGIBLE for another reason
  Action: local null for this cell; report and consult Team Lead

Branch 6 — components (hop1/hop2) pass Gate 2 but composite fails Gate 2
  Action: composite-only drop signal; candidate for linkage-specific stress proposal
  Note: must also pass Gates 3–5 before stress proposal is licensed
```

---

## 8. Output artifact requirements

Every scored run must produce both artifacts before results are reported:

**A. Raw output JSON** — one object per item × query type, containing:

```json
{
  "item_id":                 "...",
  "query_type":              "...",
  "prompt_rendered_hash":    "sha256:...",
  "raw_output":              "...",
  "failure_class":           "...",
  "scaffold_class":          "...",
  "format_class":            "...",
  "returned_token":          "...",
  "returned_role":           "...",
  "is_correct":              true/false
}
```

Provenance block (once per file):

```json
{
  "manifest_hash":             "sha256:...",
  "scorer_hash":               "sha256:...",
  "validator_hash":            "sha256:...",
  "runner_hash":               "sha256:...",
  "tokenizer_hash":            "sha256:...",
  "prompt_template_hash":      "sha256:...",
  "failure_taxonomy_version":  "v1.0",
  "model_tag_digest":          "...",
  "decoding_settings":         {"temperature": 0.0, "max_tokens": 16},
  "axis_configuration":        "...",
  "frozen_settings":           "..."
}
```

**B. Run Summary** — one filled copy of `RUN-SUMMARY-TEMPLATE-TWOHOP-L1.md` per query type, filed as `RESULTS-TWOHOP-L1-{cell_id}-{query_type}.md`.

---

## 9. Open items before execution

The following must be resolved before Stage 1 execution is authorized. None is CS-actionable alone; all require Team Lead and/or Manager input.

| # | Item | Status | Blocking | Routing |
|---|---|---|---|---|
| 1 | BPE-Jaccard j amendment (0.50 → 0.40) | **LOCKED 2026-06-08 (Manager)** | — resolved | No action required |
| 2 | Gate 1 FORMAT_PASS threshold (1.000) | **LOCKED 2026-06-08 (Manager)** | — resolved | No action required |
| 3 | shortcut_single_hop validator flag | **CLOSED** — coverage confirmed in canonical locked artifact `tier0-run/tasks_twohop_l1.py`, `sha256:bcc26ca0...`; `validate_positive_sufficiency()` line 201, all three checks present; no Stage 0 Amendment A required. *Provenance note: prior conflicting inspection referenced non-canonical path `stage0/validator.py`; canonical artifact reconciliation resolved the discrepancy (Team Lead disposition 2026-06-08).* | None | No action required |
| 4 | Cell generation authorization | **DONE — Manager authorized 2026-06-08** | — resolved | No action required |
| 5 | Runner script construction and lock | **DONE (Rev 2) — runner_twohop_l1.py, sha256:ed2fbdc3...** | — resolved | No action required |
| 6 | Prompt template construction and lock | **DONE — prompt_template_twohop_l1.txt, sha256:c8a81a29...** | — resolved | No action required |
| 7 | FP16 tokenizer hash | **CLOSED — accepted by Team Lead 2026-06-08.** sha256:c0382117... (format difference from local hash only; vocabulary and merges identical) | Gate 0.5 PASS | No action required |
| 8 | Scorer fact_role mismatch (Option D) | **CLOSED — scorer amended 2026-06-08** (backward-compatible; smoke/unit tests PASS). New hash sha256:060afad9... | — resolved | No action required |
| 9 | Cell regeneration — 3-chain design (Option B) | **CLOSED — items regenerated 2026-06-08.** sha256:00a7adf8...; 24/24 PASS; first_C=last_C=8/24 ≤ 9/24; Gate 5 PASS | — resolved | No action required |

---

## 10. Forbidden claims

The following claims are forbidden regardless of Stage 1 result (from CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md):

```
the seam exists / does not exist
quantization breaks reasoning
INT4 is harmful or harmless
this model cannot do two-hop linkage
a constructibility boundary is a capability boundary
a composite drop is linkage degradation without failure-class separability
behavioral evidence implies mechanism
```

Safe form: *Under this frozen construction, at this model size, under these gates, the task did or did not reach interpretability.*

---

## 11. Files (current state)

**Locked Stage 0 files:**

```
tasks_twohop_l1.py              sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
scorer_twohop_l1.py             sha256:6921e58059e3ef4806c1ae75f73a9670f4a02962bff2eb27fd2da77bad82c473
smoke_test_twohop_l1.py         sha256:58749ca88ab69e0fc6cf34cfb3417ee57f42c1ebe13c5c7cfd384726182c3989
RUN-SUMMARY-TEMPLATE-TWOHOP-L1.md
STAGE0-INSTRUMENT-LOCK-PACKET.md
```

**Approved threshold documents:**

```
THRESHOLD-PROPOSAL-TWOHOP-L1.md     Revision 2 — APPROVED 2026-06-08 (BPE-Jaccard amendment pending)
THRESHOLD-REVIEW-TWOHOP-L1.md       CS Engineer review response
BPE-JACCARD-INSPECTION-TWOHOP-L1.md tokenizer inspection — amendment required
```

**Stage 0 amended instrument (2026-06-08):**

```
scorer_twohop_l1.py   sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd
  (Option D amendment: line 229 fact_role recognition; backward-compatible;
   prior hash sha256:6921e580...; 22/22 smoke tests PASS; 14/14 unit tests PASS)
```

**Stage 1 preparation artifacts (Rev 2 — 2026-06-08):**

```
items_twohop_l1_cell01.json       sha256:00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28
                                  (3-chain, 7-fact, 8+8+8 ordering; 24/24 PASS)
runner_twohop_l1.py               sha256:ed2fbdc3e21375060f15a0645da111c24db890b840d9be476ee24d8bb06c5aaf
prompt_template_twohop_l1.txt     sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
generate_cell01.py                One-time generation script (not locked; RNG seed 20260608)
STAGE1-PREP-LOCK-PACKET-TWOHOP-L1.md   Revised lock packet (Rev 2) — submitted for Team Lead review
```

**Not yet authorized (requires Manager authorization after Team Lead review):**

```
RESULTS-TWOHOP-L1-*.md           Run summaries (NOT AUTHORIZED — no inference authorized)
```

— CS Engineer
