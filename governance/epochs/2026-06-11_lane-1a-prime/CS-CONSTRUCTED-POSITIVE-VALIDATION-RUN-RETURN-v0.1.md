# CS Return — Constructed-Positive Validation Run

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED
**Authorization:** Manager 2026-06-13 — "Constructed-positive validation run: ACCEPT" (model-facing validation only; no quantization stress, INT8/INT4, Path B, Path D, schedule v2, certification, ranking, Claim C inference).
**Scope:** Single constructed-positive pair, single decoding pass per item, full T3 criteria battery applied where computable from the pair's structure.
**Disposition:** PASS — defective member eliminated; clean member not ruled out.
**Path A qualifier (TL §2 ruling option c):** This return concerns Path A (rung-uniform). No breadth, replication, seam, or Claim-C inference is asserted anywhere in this memo.

---

## §1. Run identity

| Field | Value |
|---|---|
| Run timestamp (UTC) | 2026-06-13T16:01:18Z |
| Model ID | Qwen/Qwen2.5-3B-Instruct |
| Precision | bf16 (mlx_lm 0.31.3) |
| Decoding | greedy (temp=0.0, top_p=1.0, max_new_tokens=32) |
| Items | 80 total (40 clean answerable + 40 defective answerable) |
| Inference wall time | 24.5 s (12.8 s clean + 11.7 s defective) |
| Model load time | 2.6 s |
| Hardware | local Apple-silicon, mlx_lm bf16 backend |

## §2. Pre-flight artifact-hash verification (PH5-4 pattern)

All sealed bytes checked at run start and at run end. **All UNCHANGED.**

| Sealed artifact | sha256(64) | Status |
|---|---|---|
| `tier0-run/LOCK-RECORD.md` (Lane 1a' Prime predecessor) | `5b557ae2a4c90bf34d2c050dc2b713b0ae29c2dd4eeb1f54a4099b5fb6cd5869` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5` | UNCHANGED |
| `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39` | UNCHANGED |

Constructed pair inputs (file bytes unchanged from CS v0.2 filing):

| Artifact | sha256(64) |
|---|---|
| `constructed_positive/clean_member.json` | `f412d04cec56e468ddf775cd00123d681ad9073acb5c17385c3086a960b13097` |
| `constructed_positive/defective_member.json` | `4ea3c277eda4acbea5749a5c2f3fa9f0eec77b3ca6f386600f46ee0d213d9fe6` |
| `constructed_positive/realized_match_manifest.json` | `49cd64510fc8f9e3f54bf958f55dcbc0254b24eca2a389c19a9be1ab2f44b376` |

## §3. Run artifacts (this filing)

| Artifact | Path | sha256(64) | Size |
|---|---|---|---|
| Validation runner (source) | `experiments/2026-06-11_lane-1a-prime/constructed_positive/run_validation.py` | `d8c9dfe426f3475a60bad7a3881a86d3f39171297808287ed6d8c0ac77977dfc` | 19,396 B |
| Clean raw outputs | `experiments/2026-06-11_lane-1a-prime/constructed_positive/validation_run/clean_outputs.json` | `abb887ad584101925a13e7e177114ac3c29b10f3b86b8d153f47a28ff9970708` | 16,339 B |
| Defective raw outputs | `experiments/2026-06-11_lane-1a-prime/constructed_positive/validation_run/defective_outputs.json` | `ff2b35757d9f4536288dca59ab6bba07ad3d2482f1c2496bad44cd2eac631355` | 16,433 B |
| Run result (summary + criteria) | `experiments/2026-06-11_lane-1a-prime/constructed_positive/validation_run/run_result.json` | `268ed175db47b7949fae18889bf0700366bd0900ecec81bf60e5b8c8a3f9f2ac` | 6,570 B |

## §4. Scorer / gate identity

Same scoring logic and criteria as the sealed instrument (no threshold changes after results). The runner applies the prompt template's `expected_response_grammar` literally for strict scoring, and applies a case-insensitive concept read for content scoring — both required by the GAP criterion's measurement, which is `newcombe_wilson_difference_content_minus_strict`.

T3 bounds applied verbatim from `T3_BOUNDS_DECLARATION.json`:

| Criterion | Bound | Direction | Status this run |
|---|---|---|---|
| FLOOR — null_abstention_floor_unmet | 0.75 | floor | **N/A** (n_null = 0; no NULL stratum in constructed pair) |
| CEIL — answerable_abstention_ceiling_exceeded | 0.20 | ceiling | computed (Wilson on strict abstention) |
| TP — accuracy_indistinguishable_from_token_prior | 0.10 | difference | **N/A** (no TP control sub-run; not authorized) |
| ENV — accuracy_indistinguishable_from_declared_policy_envelope | 0.10 | difference | **N/A** (constructed pair does not carry the sealed 5-stratum disjoint envelope structure) |
| HEAD — insufficient_measurement_headroom | 0.15 | floor | **N/A** (derived from ENV) |
| GAP — strict_content_gap_instability | 0.30 | difference | computed (Newcombe-Wilson on content minus strict) |

The two computable criteria (CEIL, GAP) are both within the sealed scorer/gate logic; no logic was added or relaxed. The four N/A criteria are honest non-applicabilities given the constructed pair's structure and the authorization scope — not hidden suppressions.

## §5. Per-member results

### Clean member (40 answerable items)

| Metric | Value |
|---|---|
| Strict accuracy | 1.0000 (40/40); Wilson CI [0.9124, 1.0000] |
| Content accuracy | 1.0000 (40/40) |
| Strict abstention rate | 0.0000 (0/40); Wilson CI [0.0000, 0.0876] |
| Content abstention rate | 0.0000 (0/40) |
| Content − strict (correct) | 0.0000; NW-diff CI [-0.0876, 0.0876] |
| Letter responses (strict) | 40 |
| OTHER responses (strict) | 0 |

Criteria outcomes:
- CEIL: **NOT_FIRED** (strict_abstention_ci_lower 0.0000 < bound 0.20)
- GAP: **NOT_FIRED** (NW-diff CI lower -0.0876 < bound 0.30)
- FLOOR / TP / ENV / HEAD: N/A

**Outcome: NOT_RULED_OUT**. No elimination label attaches.

### Defective member (40 answerable items, defective stratum; queried key absent from listed pairs)

| Metric | Value |
|---|---|
| Strict accuracy | 0.1250 (5/40); Wilson CI [0.0546, 0.2611] |
| Content accuracy | 0.9000 (36/40) |
| Strict abstention rate | 0.1250 (5/40); Wilson CI [0.0546, 0.2611] |
| Content abstention rate | 0.9000 (36/40) |
| Content − strict (correct) | **0.7750**; NW-diff CI **[0.5864, 0.8678]** |
| Letter responses (strict) | 4 (raw outputs: `f`, `z`, `g`, `j`) |
| NONE responses (strict, exact uppercase) | 5 |
| OTHER responses (strict) | 31 — all raw `none` (lowercase) |

Criteria outcomes:
- CEIL: **NOT_FIRED** (strict_abstention_ci_lower 0.0546 < bound 0.20) — the model abstained correctly per the prompt's literal grammar on only 5/40 defective items, which by itself does not breach the strict-abstention ceiling.
- GAP: **FIRED** (NW-diff CI lower 0.5864 > bound 0.30) — at least 30% of answerable items are content-correct but format-broken; observed gap 0.7750 with CI lower 0.5864.
- FLOOR / TP / ENV / HEAD: N/A

**Outcome: ELIMINATED** for `strict_content_gap_instability`.

## §6. Overall pattern

**PASS** — Defective member eliminated under the sealed criteria battery; clean member not ruled out.

Per TL §required-return narrow framing: "Does the instrument eliminate the defective member and spare the clean member?" On this constructed pair, under the sealed prompt template, decoding configuration, and T3 bounds: **yes**. The route is GAP, not CEIL.

## §7. Substantive observation on the elimination route (not a claim, not a finding)

The defective member's responses split as follows on the abstention concept:

| Raw output | Count | Strict-grammar status | Content-grammar status |
|---|---|---|---|
| `NONE` (uppercase) | 5 | abstain (correct under spec) | abstain |
| `none` (lowercase) | 31 | OTHER (off-grammar) | abstain |
| single lowercase letter [`f`, `g`, `j`, `z`] | 4 | letter (hallucination, gold is null) | letter |

The model produced an abstention concept on 36/40 defective items but matched the prompt template's literal uppercase form on only 5/40. This is the source of the 0.7750 content-vs-strict gap that fires GAP.

If the model had matched the literal grammar on all 36 abstention-concept items, the CEIL criterion would have fired instead (strict abstention 36/40 = 0.90, Wilson CI lower 0.7660, well above the 0.20 bound). The defective member would be eliminated under either route. The criterion that fired in this run depends on the model's literal-vs-concept-level adherence to the spec — not on the sealed bounds.

This observation is reported for accurate interpretation. It is not a claim about model capability, format-discipline, headroom, or any other characteristic of the candidate. It is also not a claim that GAP and CEIL are interchangeable diagnostics in general; they are interchangeable only when the format-broken responses are themselves concept-correct abstentions, which is a contingent property of this specific run.

## §8. What this run does NOT support (binding language perimeter)

This validation run is **not** evidence for and shall not be cited as:
- model passed
- capability established
- not shortcut-driven
- candidate certified
- task family viable
- Claim C progressed
- seam evidence
- public benchmark result
- certification achieved
- breadth across rungs / L01–L08 breadth / 8/8 survived / eight rungs NOT_RULED_OUT
- full-surface NOT_RULED_OUT
- result replicated across rungs / robust across the schedule / consistent across all rungs
- Path A failed / the lane is broken / constructibility was answered negatively / task family shows no breadth
- task-family viability across the schedule

The carried scope sentence: **Breadth is untested under the current sealed schedule.**

This run reports a validation outcome on a single constructed pair under sealed instrument settings. Generalization beyond this pair is not supported by this run alone.

## §9. Open review items by ID (enumerated; per §9 consolidation rule)

Open items at the moment of this filing:
1. None routed to CS for response in this return.

If TL/Senior/Manager wish to route the §7 observation (lowercase-`none` GAP-vs-CEIL routing) as a methodological item — e.g., for inclusion in the Hash Integrity standing note's surplus-check examples, or for explicit treatment in the standing semantic-read template — CS is positioned to draft the relevant text on request. CS is not preempting that decision here.

## §10. Standing constraints honored

- `tier0-run/` SEALED: not modified, no files added.
- CS scope: only `tier0-run/` (read-only here, verified hash) and `experiments/`. Governance write is to `governance/2026-06-11_lane-1a-prime/` (this memo).
- Standing semantic-read template (SHOWN-SEMANTIC-READ-TEMPLATE-v1.0): not invoked for the run itself (the runner produces data, not a decision-bearing artifact); will be invoked if the run outputs are subsequently cited in a decision-bearing artifact.
- Hash Integrity standing note: surplus check on this memo — PRESENT. The memo does not claim that the sha256-verified pair, plus a PASS pattern via GAP, supports any of the perimeter-forbidden phrasings in §8. The artifact-layer assertion (these are the files run; these are the responses; these are the criteria outcomes) is the only claim made.
- §9 consolidation rule: open items enumerated by ID above (n=0 from this side).
- All 22 model-facing successor gates: untouched; no inference about successor models implied.
- TL §2 Path A attributive-shorthand ruling: applied (no breadth/replication/seam/Claim-C inference; "Path A" used only as the rung-uniform designator).

## §11. Pointers (relative paths within repo)

- Runner: `experiments/2026-06-11_lane-1a-prime/constructed_positive/run_validation.py`
- Run output dir: `experiments/2026-06-11_lane-1a-prime/constructed_positive/validation_run/`
  - `clean_outputs.json`
  - `defective_outputs.json`
  - `run_result.json`
- Constructed pair (unchanged inputs): `experiments/2026-06-11_lane-1a-prime/constructed_positive/{clean_member,defective_member,realized_match_manifest}.json`
- Sealed instrument bytes (unchanged): `experiments/2026-06-11_lane-1a-prime/validation/{STRATIFIED_RECIPE_SCHEDULE,ORACLE_VERDICT_TABLE,T3_BOUNDS_DECLARATION}.json`

## §12. Disposition

CS files this return as: **PASS pattern observed on the sealed instrument's six-criterion battery, under the constructed-positive pair, on Qwen2.5-3B-Instruct bf16 via mlx_lm 0.31.3, with greedy decoding.** Defective ELIMINATED via `strict_content_gap_instability`; clean NOT_RULED_OUT.

Awaiting TL routing as to whether (a) the §7 elimination-route observation should be promoted to a standing item, (b) Senior should desk-read this return, or (c) a second instance of the constructed pair under a different construction seed is appropriate as a same-instrument robustness check (which would still be a single-pair-class validation, not a breadth claim).

— CS Engineer, 2026-06-13
