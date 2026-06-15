# PREREGISTRATION — MINIMAL-FP16-INT8-TWOHOP-L1-v0.1

**Locked BEFORE any results are seen.** River and Canyon program. This pre-registration declares the task, conditions, metrics, and verdict rules for the program's first real model run, so the result can come back NO_DROP, DROP, or INCONCLUSIVE and be reported honestly either way. It runs no model and contains no results.
**Status / boundary:** Senior-drafted (model-free). EXECUTION IS NOT PERFORMED HERE and is not mine to perform — the run is CS's, on the real machine, and ONLY after the Manager explicitly authorizes this specific named run (Route GREEN). Until then this document is the locked pre-registration, nothing more. Classified as an **exploratory Tier-1 observation, NOT Lane 4 certification evidence** unless the Manager separately classifies it.
**Run name:** MINIMAL-FP16-INT8-TWOHOP-L1-v0.1. **Run dir (to be created at execution):** `experiments/2026-06-15_minimal-fp16-int8-twohop-l1/`.

---

## 1. Model and weight paths

```text
Model:        Qwen2.5-3B-Instruct (program baseline; Paper A / Cell03).
FP16 weights: Qwen/Qwen2.5-3B-Instruct  (HF cache) — loader mlx_lm.load("Qwen/Qwen2.5-3B-Instruct")
INT8 weights: tier0-run/Qwen2.5-3B-Instruct-mlx-int8/  — loader mlx_lm.load("tier0-run/Qwen2.5-3B-Instruct-mlx-int8")
Runtime:      mlx_lm 0.31.3 (version recorded in manifest). Both smoke-tested as loading + generating.
```

## 2. Task and prompt source

```text
Task:    Two-Hop Constructibility Level-1, matched-pair.
Scorer:  tier0-run/scorer_twohop_l1.py (deterministic; byte-locked under Cell03 — read-only, not modified).
Prompts: tasks_twohop_l1.py item set (the established Two-Hop L1 prompts); same prompts, both conditions.
Query types scored per item: hop1 (component), hop2 (composite), length_matched (control).
Per-item classification (scorer's own categories): correct · non_context_return · correct_chain_stopped_short
  (composite-only — the "did hop1 but not hop2" seam signature) · anchor_echo · format pass/fail.
```

## 3. Sample size

```text
n = 8 (smallest viable; program convention "FP16 feasibility, n=8 only"). Coarse by design — see §7.
```

## 4. Decoding parameters

```text
Greedy / deterministic: temperature = 0.0, max_tokens = 16 (matching the existing constructibility check).
Identical decoding for both conditions. Same prompts, same order, same seed-free greedy path.
```

## 5. Metrics (pre-declared — computed identically for both conditions)

```text
M1  FP16 accuracy        = count(correct) / n, overall AND broken out by query type (hop1 / hop2 / length_matched).
M2  INT8 accuracy        = same, both conditions side by side.
M3  item-level difference = per-item FP16→INT8 classification transition (which items changed category, how).
M4  matched-pair difference = composite (hop2) correctness vs component (hop1) correctness, per condition; and
      specifically whether INT8 loses hop2 while retaining hop1 — tracked via the correct_chain_stopped_short
      (composite-only) rate. This is the seam-shaped quantity, reported as an observation, not a claim.
M5  raw E3 retained      = full per-item raw model outputs for BOTH conditions written to disk (fp16_raw_outputs.json,
      int8_raw_outputs.json), plus tokenizer audit + per-file sha256 manifest.
```

## 6. Verdict labels — pre-declared thresholds (coarse for n=8; chosen NOW, before looking)

```text
FP16-BASELINE GATE (evaluated FIRST — the diligence this run genuinely needs):
  Inspect the FP16 raw E3, not only the score. The program's own Claim B established that an FP16 baseline can
  score "correct" via a POSITION / ANCHOR shortcut rather than genuine two-hop operation. If the FP16 baseline's
  correct answers show shortcut signatures (anchor_echo, non_context_return passing for the wrong reason, or
  hop2-correct that on inspection is position-reading not chain-following), then the FP16 baseline is NOT a valid
  measurement floor → the matched-pair difference is UNINTERPRETABLE → verdict = INCONCLUSIVE, and the run reports
  the baseline contamination as its finding. This gate is pre-declared so it cannot be skipped after INT8 is seen.

IF the FP16 baseline passes its raw-output check, then:
  NO_DROP       INT8 correct-count ≥ FP16 correct-count − 1 (within one item) AND no composite-specific
                degradation (correct_chain_stopped_short on hop2 does NOT increase under INT8).
  DROP          INT8 correct-count ≤ FP16 correct-count − 2 (≥ 0.25 absolute) OR composite-specific degradation
                appears (correct_chain_stopped_short / hop2 failures increase under INT8 while hop1 holds) — the
                seam signature, reported as an observation on these 8 items.
  INCONCLUSIVE  anything between the above; ties; or FP16-baseline-gate failure (above).
```

## 7. Pre-declared limits on what this run can mean

```text
- n = 8 → 1 item = 0.125. Resolution is coarse; a one-item move is near the noise of the instrument.
- This is the program's FIRST real observation — one model, one task, one compression step, eight items. It is an
  OBSERVATION, not a powered test. Whatever the verdict, it holds for THESE 8 items under THIS setup — it does not
  establish a general property of the model, the task family, or quantization.
```

## 8. Forbidden interpretations (pre-declared; binding on the result writeup)

```text
The result must NOT be reported as, or used to claim:
  - Claim C progressed / a compositional seam demonstrated
  - Paper B activated
  - a general compression-robustness claim
  - a certified-baseline claim (no baseline is certified; this is exploratory)
  - the task family is viable / the model "passed" / capability established / "not shortcut-driven"
  - any product- or funder-facing result
The honest output is: two accuracies, their item-level and matched-pair differences, the FP16-baseline-gate
disposition, and one of {NO_DROP, DROP, INCONCLUSIVE} on these 8 items — nothing about what it means for the
larger question.
```

## 9. Execution order (for CS, after Manager authorization — NOT performed here)

```text
1. Create the run dir; commit THIS pre-registration first (locked before any run).
2. [Manager authorizes "authorize run" → Route GREEN.]
3. Run FP16 condition → write fp16_raw_outputs.json (raw E3).
4. Run INT8 condition → write int8_raw_outputs.json (raw E3).
5. Score both with scorer_twohop_l1.py → per-condition + matched-pair score JSON.
6. Evaluate the FP16-baseline gate (§6) from the FP16 raw outputs.
7. Manifest: sha256 every input + output; record mlx_lm version, prompt/scorer hashes, decoding params, machine id.
8. Disposition: apply §6 rules → {NO_DROP, DROP, INCONCLUSIVE}; report per §8.
Boundaries held throughout: no Lane 4 classification, no certification, no Claim C/Paper B, no sealed-byte movement
(new dated dir only), no product/funder claim.
```

---

*PREREGISTRATION — MINIMAL-FP16-INT8-TWOHOP-L1-v0.1 (Senior-drafted; model-free; the before-you-look LOCK for the program's first real run): Qwen2.5-3B-Instruct, FP16 (HF cache) vs INT8 (tier0-run MLX), Two-Hop L1 matched-pair via the byte-locked scorer_twohop_l1.py, n=8, greedy (temp 0.0 / max_tokens 16). Metrics M1–M5 (FP16 acc, INT8 acc by query type, item-level diff, matched-pair composite-vs-component diff incl. the correct_chain_stopped_short seam quantity, raw E3 retained). Verdict thresholds pre-declared: FP16-BASELINE GATE FIRST (inspect FP16 raw outputs for the Claim-B position/anchor shortcut — contaminated baseline ⇒ INCONCLUSIVE), then NO_DROP / DROP / INCONCLUSIVE with explicit n=8-coarse numeric rules. §7 limits (n=8 = 0.125/item; a first OBSERVATION not a powered test; no general property). §8 forbidden interpretations (no Claim C / Paper B / general compression / certified baseline / task-family-viable / "passed" / product-funder). §9 execution order for CS AFTER Manager authorization. EXECUTION NOT PERFORMED HERE and not Senior's to perform — the run is CS's, on the real machine, only on the Manager's explicit "authorize run"; this document runs no model and reports no results. Exploratory Tier-1, NOT Lane 4. No sealed-byte movement.*
