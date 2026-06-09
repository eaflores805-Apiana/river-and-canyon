# Cell02 hop2 FORMAT_PASS Failure — Construction-Integrity Inspection

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Authorized by:** Team Lead memo — "Cell02 Filing Hold — Construction-Integrity Check Required" 2026-06-08
**Updated:** 2026-06-08 — taxonomy label updated to FORMAT_COMPLIANCE_LOSS per Team Lead memo "Cell02 Follow-Up — i08 Label Accepted; Gate 5 Positional-Dummy Audit Required"
**Status:** COMPLETE — classification: FORMAT_COMPLIANCE_LOSS (isolated, orthogonal format-only event)

---

## Purpose

Team Lead placed a filing hold on final Cell02 interpretive filing pending item-level inspection of the single hop2 FORMAT_PASS failure. The question under investigation:

```text
Was the single hop2 FORMAT_PASS failure in Cell02 caused by the Cell02
construction change, or was it an isolated single-item generation / formatting glitch?
```

This document records the 10-point inspection and the construction-integrity determination.

---

## 1. Item ID of the hop2 FORMAT_PASS failure

```text
item_id: twohop_l1_c02_i08
```

---

## 2. Raw hop2 output

```text
raw_output:         "ANSWER: ZBCDF maps to AJLAC."
scaffold_class:     SCAFFOLD_PRESENT  (ANSWER: prefix generated correctly)
format_class:       FORMAT_FAIL       (sentence form, not bare token)
returned_token:     null              (scorer could not extract a token)
is_correct:         false             (format failure; content not evaluated)
```

The model produced the scaffold prefix ("ANSWER:") correctly, then reproduced the text of context fact f06 verbatim ("ZBCDF maps to AJLAC.") rather than emitting only the answer token.

---

## 3. Expected hop2 answer

```text
expected_answer:  AJLAC
query_anchor:     ZBCDF  (the bt / hop1_B token for i08)

Target chain for i08:
  A_object: ZAYWZ (anchor_A)
  B_object: ZBCDF (hop1_B — also the hop2 query anchor)
  C_object: AJLAC (answer_C — the expected hop2 output)
```

AJLAC is present in the raw output ("ZBCDF maps to AJLAC."). The model had the correct semantic knowledge. The failure is format-only.

---

## 4. Context structure and rendering for i08

The i08 context is a standard 7-fact, 3-chain, all-C_target-last arrangement:

```text
pos 1  f01  ZDJTJ links to ZEXKH.      (dc1 hop1)
pos 2  f02  ZEXKH maps to DVRRO.       (dc1 hop2 — cd1 at pos 2)
pos 3  f03  ZGYJK links to ZHSNR.      (dc2 hop1)
pos 4  f04  ZFXHG holds AJLMA.         (neighbor fact — cn at pos 4)
pos 5  f05  ZAYWZ links to ZBCDF.      (target chain hop1 — bt at pos 5)
pos 6  f06  ZBCDF maps to AJLAC.       (target chain hop2 — ct at pos 6)
pos 7  f07  ZHSNR maps to PBKNW.       (dc2 hop2 — cd2 at pos 7)
```

The hop2 query anchor is ZBCDF. Fact f06 reads: "ZBCDF maps to AJLAC."

The model's output "ANSWER: ZBCDF maps to AJLAC." is a verbatim reproduction of fact f06's text after the scaffold prefix. Every hop2 query in Cell02 has this same structure: the query anchor (bt) appears as the subject of the hop2 fact in context. Item i08 is not structurally unusual.

Other i08 query results (confirming correct rendering):

```text
hop1:           ANSWER: ZBCDF       — correct, standard format
composite:      ANSWER: AJLAC       — correct, standard format
negative_graph: ANSWER: PBKNW       — FORMAT_PASS, wrong_chain_selection
```

All three other query types for i08 rendered and were processed in standard format. No rendering artifact is detectable.

---

## 5. Position/ordering group

```text
All 24 Cell02 items are C_target-last (T-hop2 at pos 6).
Item i08 is not in any distinct subgroup — it is part of the uniform all-C_target-last design.
Position/ordering group: C_target-last (same as all 24 items)
```

There is no positional subgroup distinction in Cell02 against which i08 can be compared.

---

## 6. Adjacency condition

```text
Cell02 adjacency condition (all 24 items):
  Target chain hop1 fact at pos 5 (bt at pos 5)
  Target chain hop2 fact at pos 6 (ct at pos 6)
  These two facts are adjacent in all 24 Cell02 items.

Item i08 participates in the same adjacency condition as all other Cell02 items.
The hop2 FSF on i08 is not linked to a distinguishing adjacency configuration.
```

---

## 7. Co-failures on the same item

```text
hop1:           correct (returned ZBCDF = bt)                   — no failure
hop2:           format_scaffold_failure (FORMAT_FAIL)           — the failure under investigation
composite:      correct (returned AJLAC = ct)                   — no failure
negative_graph: wrong_chain_selection (returned PBKNW = cd2)    — standard failure class
```

i08 has no unusual pattern of co-failures. hop1 and composite are both correct. The negative_graph wrong_chain_selection is the most common failure class in Cell02 (23/24 negative_graph items failed this way). Item i08 exhibits no cross-query failure concentration that would indicate a construction anomaly.

---

## 8. Token-construction and near-miss properties

### AJLAC / AJLMA near-miss pair

```text
AJLAC (answer_C / ct for i08):      bpe = ['AJ', 'L', 'AC']
AJLMA (target_neighbor_decoy / cn): bpe = ['AJ', 'L', 'MA']

Levenshtein(AJLAC, AJLMA) = 2  (within k ≤ 2 near-miss threshold)
bjac(AJLAC, AJLMA)         = 0.50  (above j ≥ 0.40 threshold)
tjac:                           (not computed here — covered by Phase 1 audit)

Status: VALID declared near-miss pair
  This pair is in the declared set {(ct, cn)} from Phase 1 of generate_cell02.py.
  The pair was selected by the greedy algorithm precisely because it satisfies
  lv ≤ 2, bjac ≥ 0.40, tjac ≥ 0.20.
  The Phase 4 token-pool audit correctly excludes declared ct-cn pairs from
  violation reporting (as designed — these are intentional near-miss pairs).
  Gate 0.5 result is valid: 0 violations.
```

**Important note on bjac computation:**
The `bjac` function in `generate_cell02.py` computes Jaccard over the SET of BPE subword strings, not over BPE token IDs. For AJLAC/AJLMA:
```
bpe('AJLAC') → ['AJ', 'L', 'AC'] → set {'AJ', 'L', 'AC'}
bpe('AJLMA') → ['AJ', 'L', 'MA'] → set {'AJ', 'L', 'MA'}
intersection: {'AJ', 'L'} = 2 elements
union:        {'AJ', 'L', 'AC', 'MA'} = 4 elements
bjac = 2/4 = 0.50
```
A computation based on HuggingFace token IDs would produce 0.333 (incorrect for this context). The generation script's own bjac function confirms j=0.50 ≥ 0.40.

### bt token (ZBCDF) BPE structure

```text
ZBCDF: bpe = ['Z', 'BC', 'DF']  (3 subwords)
```

ZBCDF has the same 3-subword structure as most bt tokens (ZBOJB, ZBSMS, ZBATA, ZBIKR also have 3 subwords). No unusual BPE fragmentation.

### Token-identity summary

No BPE anomaly is detected for i08's tokens. The ct-cn pair is a valid declared near-miss pair with bjac=0.50. Gate 0.5 is confirmed clean.

---

## 9. Prompt / template / rendering difference

```text
hop1 query for i08:           FORMAT_PASS (ANSWER: ZBCDF — correct terse output)
composite query for i08:      FORMAT_PASS (ANSWER: AJLAC — correct terse output)
negative_graph query for i08: FORMAT_PASS (ANSWER: PBKNW — correct terse, wrong content)

hop2 query for i08:           FORMAT_FAIL (ANSWER: ZBCDF maps to AJLAC. — verbatim fact)
```

All four queries used the same prompt template (sha256:c8a81a29...) with the same rendering logic. Three of four query types produced standard-format outputs. The hop2 output is the only non-standard output.

The hop2 query anchor is ZBCDF. The context fact f06 reads "ZBCDF maps to AJLAC." The model produced the ANSWER: scaffold correctly, then reproduced f06's text verbatim. This is a verbatim sentence reproduction pattern: the model completed "ANSWER: " with the full context sentence whose subject matches the query anchor, rather than extracting the endpoint token.

No rendering difference, template error, or prompt construction issue is detectable. The other 23 hop2 queries — all with identical prompt structure (anchor = bt, fact at pos 6 = "bt maps to ct") — produced standard-format responses.

---

## 10. Classification

```text
Classification: FORMAT_COMPLIANCE_LOSS
  (isolated, orthogonal format-only event — not construction-linked)

Taxonomy label (per Team Lead memo 2026-06-08):
  i08/hop2 is classified as FORMAT_COMPLIANCE_LOSS: the correct answer AJLAC was
  present, but the model reproduced the full fact sentence after the ANSWER scaffold,
  violating the strict bare-token contract. This is treated as an isolated format-only
  event, not a construction-linked side effect.

Scorer class (unchanged): format_scaffold_failure
Human-readable taxonomy class: FORMAT_COMPLIANCE_LOSS

Mechanism:
  At temperature=0.0 (greedy decoding), the hop2 query for i08 followed a generation
  path that reproduced the text of context fact f06 ("ZBCDF maps to AJLAC.") verbatim
  after the ANSWER: scaffold. The model's highest-probability continuation for
  "ANSWER: " given this specific item's context happened to be the full sentence
  form, not the bare endpoint token. Content was present; format contract was violated.

Evidence for isolated, orthogonal event:
  - 23/24 other hop2 items with identical context structure produced standard format
  - i08 hop1 and composite both produced correct terse outputs
  - The correct answer (AJLAC) is present in the raw output
  - No BPE anomaly, no rendering difference, no template error detected
  - No construction feature unique to i08 explains the failure

Evidence against construction-linked:
  - All 24 items have the same hop2 query structure (anchor = bt; fact at pos 6 = "bt maps to ct")
  - The neighbor near-miss (AJLAC/AJLMA) is a valid declared pair; it did not cause the failure
  - hop1 and composite returned correct tokens for i08, confirming the item's construction is functional
  - Gate 0.5 is valid (0 violations confirmed under correct bjac implementation)

Classification confidence: HIGH
  The isolation (1/24) with functional hop1/composite outputs and no detectable construction
  difference is strong evidence for a generation-path artifact rather than a construction defect.
```

---

## 11. Construction-integrity determination

```text
Gate 0.5: VALID — 0 violations confirmed (bjac implementation uses BPE subword strings)
Cell02 manifest: VALID — all 7 provenance hashes match
hop2 FSF: ISOLATED GENERATION GLITCH — not construction-linked

Impact on Cell02 comparisons:
  The "position/ordering NOT SUPPORTED" conclusion stands.
  Cell02 content metrics (hop1 9/24, composite 20/24) remain valid as diagnostic
  downstream of Gate 1.
  The adjacency-driven endpoint attraction finding (11/15 hop1 target_chain_wrong_neighbor)
  is unaffected by the hop2 FSF on i08.
  The comparison-integrity caveat required by Team Lead is preserved per filing instructions.

Filing hold: RESOLVED — classification is isolated noise, not construction-linked.
```

---

## 12. Authorization boundary

```text
This document authorizes:
  construction-integrity inspection and classification

This document does NOT authorize:
  rerun
  confirmation pass
  Cell03 construction
  prompt repair
  model inference
  7B, INT8, INT4, Track B
  any amendment to locked Cell02 artifacts beyond the required caveat notes
```

---

**Construction-integrity inspection complete.**
**Classification: FORMAT_COMPLIANCE_LOSS (isolated, orthogonal) — Cell02 i08 filing hold resolved.**

— CS Engineer, 2026-06-08
