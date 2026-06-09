# Fork A Clarification and Retraction Note

**Filed:** 2026-06-09 (supersedes earlier version filed same date)  
**Prepared by:** CS Engineer  
**Status:** FINAL — responds to Team Lead memo §4–§7  
**Purpose:** Plain-answer retraction status for each Fork A figure; figure-by-figure table; reactivation bar evaluation; paper wording consequence.

---

## §1 Plain Answer — Fork A INT8/INT4 Retraction Status

**Direct answer to Team Lead memo §4:**

> Are the Fork A INT8/INT4 stress numbers now un-retracted and artifact-backed?

**The stress retraction remains.**

All four figures are artifact-backed (the result files exist, the numbers are accurate, same-error identity is logged). However, the INT8 and INT4 stress figures do **not** meet the reactivation bar conditions required to treat them as interpretable retention evidence. Specifically, conditions 2, 3, and 5 of the six-condition reactivation bar are not met (see §3).

**Figure-by-figure retraction status:**

| Figure | Retraction status |
|---|---|
| 8/8 FP16 n=8 pilot | **HISTORICAL ONLY** — not retracted (FP16; no stress claim); not stress-eligible under canonical gate ladder |
| 24/24 FP16 n=24 | **HISTORICAL ONLY** — not retracted (FP16; no stress claim); not certified constructible under canonical gate ladder |
| 23/24 INT8 n=24 | **STRESS RETRACTION REMAINS** — artifact exists and is accurate; reactivation bar conditions 2, 3, 5 not met |
| 24/24 INT4 n=24 | **STRESS RETRACTION REMAINS** — artifact exists and is accurate; reactivation bar conditions 2, 3, 5 not met |

---

## §2 Figure-by-Figure Table

| Figure | Precision / condition | Task / construction | Artifact exists? | Artifact path / hash | Same-error identity available? | FP16 baseline certified constructible (canonical gate ladder)? | Stress rung pre-registered? | Status |
|---|---|---|---|---|---|---|---|---|
| 8/8 | FP16, n=8 pilot | Synthetic Key-Value Selection Constructibility (Fork A, manifest_family=L3) | **YES** | `fp16_constructibility_3b_1780865740.json` — hash not in provenance block; file exists | Not applicable (FP16 run; no stressed comparison) | **NO** — Fork A used pass/fail pilot system, not Gate 0–6 ladder | Not applicable (FP16) | **Historical only** |
| 24/24 | FP16, n=24 baseline | Same construction | **YES** | `fp16_constructibility_3b_n24_1780867214.json` — hash not in provenance block; file exists | Not applicable (FP16 run) | **NO** — same as above | Not applicable (FP16) | **Historical only** |
| 23/24 | INT8, n=24 | Same construction | **YES** | `stress_constructibility_3b_int8_1780870164.json` — `provenance: null`; metadata at top level; file exists; exact_output_agreement=0.9583 | **YES** — per-item `fp16_raw_output`, `exact_output_match`, `same_error_identity_key` present; `failure_class_transition` logged; 1 failure: L3_15 (UNCLASSIFIED\|None\|None) | **NO** — FP16 baseline not certified constructible under canonical gate ladder | **NO** — authorization was Manager decision 2026-06-07; no preregistration document | **Stress retraction remains** |
| 24/24 | INT4, n=24 | Same construction | **YES** | `stress_constructibility_3b_int4_1780872258.json` — `provenance: null`; metadata at top level; file exists; exact_output_agreement=1.0 | **YES** — per-item fields present; exact_output_agreement=1.0; failure_class_transition=[] | **NO** — same as INT8 | **NO** — same as INT8 | **Stress retraction remains** |

---

## §3 Reactivation Bar — Six-Condition Evaluation

Per Team Lead memo §6. Each condition evaluated against the INT8/INT4 stress runs.

| Condition | Requirement | INT8/INT4 status | Met? |
|---|---|---|---|
| 1 | Artifact-backed | Result files exist; numbers confirmed accurate | **YES** |
| 2 | Produced under locked instrument or traceably equivalent | Fork A runner (`stress_constructibility_3b.py`) predates two-hop harness. `provenance` field is `null` — not an empty dict, fully absent. scorer_hash, manifest_hash, runner_hash, tokenizer_hash not embedded in provenance architecture. Metadata present at top level (model_id, bits, decoding, authorization_note) but instrument is not traceable to locked hashes in the two-hop sense | **DOES NOT MEET** |
| 3 | Tied to certified-constructible FP16 baseline | FP16 n=24 baseline exists (24/24). However, this baseline was not evaluated against the canonical 10-gate ladder (Gate 0 through Gate 6). Fork A used its own pass/fail system: n=8 pilot → n=24 expansion. No gate_summary, no stress_eligible field, no Gate 2 threshold evaluation in the FP16 result file | **DOES NOT MEET** |
| 4 | Compatible with same-error identity reporting | fp16_raw_output, exact_output_match, same_error_identity_key present per-item in INT8/INT4 result files | **YES** |
| 5 | Governed by pre-registered stress-rung conditions | Authorization is documented (authorization_note: "INT8 authorized by Manager 2026-06-07"). No preregistration document exists for Fork A stress rungs. No pre-registered outcome→reading map for the stress runs. No pre-registered gate thresholds for stress eligibility | **DOES NOT MEET** |
| 6 | Free from reliance on asserted-not-run, stale, or unauditable summaries | Result files are directly inspectable. All counts recomputed from artifacts | **YES** |

**Three of six conditions not met (conditions 2, 3, 5).**

**Classification per Team Lead memo §6:**

> "historical artifact only, not interpretable retention evidence"

This classification applies to the INT8 23/24 and INT4 24/24 stress figures. The FP16 figures (8/8 and 24/24) are not stress claims and are not subject to this classification, but they also cannot be described as "certified constructible" under the canonical gate ladder.

---

## §4 Paper Wording Consequence

Per Team Lead memo §7: Fork A artifacts exist. CS must specify which artifact family they belong to.

**Fork A artifact family:** Separate Fork A track — distinct from the Paper 2 two-hop L1 construction.

Evidence from artifact metadata:
- `track: "Synthetic Key-Value Selection Constructibility"` (top-level field in both FP16 and stress result files)
- `manifest_family: "L3"` (Fork A L3 synthetic manifest, distinct from the two-hop L1 manifest family)
- `model_id: "Qwen/Qwen2.5-3B-Instruct"` (same model, but different task family)

Fork A does **not** belong to the Paper 2 two-hop L1 construction family. The Paper 2 construction is the two-hop L1 cells (Cell01/02/03), which use `manifest_family` structured as `items_twohop_l1_cell0{n}.json`.

**Wording consequence for Senior:**

The current sentence "No compression rungs were run on any task" is factually incorrect — Fork A INT8 and INT4 runs were executed on the Synthetic Key-Value Selection Constructibility construction.

The accurate narrowed sentence is:

> "No compression rungs were run on the Paper 2 construction."

CS does not recommend wording beyond this factual narrowing. All further framing decisions belong to Senior.

---

## §5 What Remains Held

Per Team Lead memo §10, the following remain unchanged until the governance record is updated:

- Running map: Fork A INT8/INT4 figures remain retracted (stress retraction confirmed, not reversed)
- Paper 2 no-stress language: narrowed to "Paper 2 construction" per §4 above
- No Fork A reactivation as live retention evidence
- No update to Contributor 5 leakage-review question based on Fork A stress figures

---

— CS Engineer, 2026-06-09
