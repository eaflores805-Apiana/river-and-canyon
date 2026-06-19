# HOP1-STABILITY TOOLING VERIFICATION — SE RETURN

**To:** Team Lead **Cc:** CS Engineer, C5, Manager **From:** Senior Engineer **Re:** TL ACTION (Verify Hop1 Stability Tooling)
**E. A. Flores**, Apiana AI, Inc. — June 19, 2026 · *Verification only (YELLOW). No run. Certifies nothing.*

## VERDICT: **PASS** — Hop1 Stability tooling verified from bytes.

Both tools implement the hop1-stability prereg contract; all five §9 branches reproduce; the N1 (hop1+hop2-only) and N2 (branch priority) resolutions are enforced — N1 confirmed behaviorally and N2 demonstrated by the two cases where it changes the verdict; everything is deterministic and model-free.

## 1. Files inspected + hashes recomputed (clone at HEAD `fc673971`)

```text
v3_hop1_stability_analyzer.py   31224f6f…   matches CS-reported  ✓
v3_hop1_covariate_logger.py     b9532490…   matches CS-reported  ✓
```

## 2. Commands run

```text
git fetch && checkout fc673971
python3 v3_hop1_stability_analyzer.py  --scored-dir … --items-dir … --admissibility … --prompt-conformance …
        --start-index 1 --block-size 96 --n-blocks 3 --output …   (5 synthetic branch cases; +twice for determinism)
python3 v3_hop1_covariate_logger.py    --scored-dir … --items-dir … --start-index 1 --block-size 96 --n-blocks 3 …
        (+ twice for determinism)
N1.A injection test (composite/dq added to a scored dir); sha256sum; diff; import + mechanism-label scan; git show --stat HEAD
```

## 3. Task-by-task

```text
(1) §9 BRANCHES — all five present: HOP1-STABLE-ADMISSIBLE / HOP1-STABLE-INADMISSIBLE / HOP1-UNSTABLE /
    HOP2-CONTROL-FAIL / CONSTRUCT-FAIL.
(2) ANALYZER COMPUTES — per-block hop1 rate + Wilson 95% CI + 0.75 floor verdict; per-block hop2 control rate
    + Wilson CI; rate distribution; between-block spread (n_blocks/min/max/range/variance); final branch. ✓
(3) COVARIATE LOGGER — emits ONLY the declared positional/structural covariates: predicted_is_P_role_distractor
    (predicted ∈ decoy-chain heads = the confirmatory hypothesis), seed_block, target_B_token, predicted_token
    + predicted_role_class, relation identity, relation_position (constant 0 per scheme), fact_line_position
    (constant 0), distance-from-query, prompt_char_count, token_width_class, competitor/distractor role class. ✓
(4) NO MECHANISM LABELS — "attention/binding/reasoning failure/shortcut" appear ONLY inside forbidden-list
    fields ("forbidden_labels", "forbidden_labels_used":"none") that DECLARE the prohibition and report none
    used. No mechanistic attribution is applied anywhere. ✓
(5) N1 (render-4-execute-2) — ALLOWED_CONTEXTS={hop1,hop2}; OUT_OF_SCOPE={composite,direct_query}; the loader
    reads only hop1+hop2 even if composite/dq are present. BEHAVIORALLY CONFIRMED: injecting composite.json +
    direct_query.json into the scored dir left the branch UNCHANGED (HOP1-UNSTABLE → HOP1-UNSTABLE). So
    unexecuted composite/dq cannot enter scoring, covariate logging, branch computation, or claims. ✓
(6) N2 PRIORITY — CONSTRUCT-FAIL > HOP2-CONTROL-FAIL > stability. DEMONSTRATED where it changes the verdict:
      case D (hop1 all-clear, but block-2 hop2 below floor)  -> HOP2-CONTROL-FAIL  (not STABLE-ADMISSIBLE)
      case E (hop1 mixed=UNSTABLE, but block-2 adm fails)     -> CONSTRUCT-FAIL     (not HOP1-UNSTABLE)         ✓
(7) BRANCH COVERAGE 5/5:
      all blocks hop1 clear                 -> HOP1-STABLE-ADMISSIBLE
      all blocks hop1 fail                  -> HOP1-STABLE-INADMISSIBLE
      blocks straddle (clear+fail)          -> HOP1-UNSTABLE
      a block hop2 below floor              -> HOP2-CONTROL-FAIL
      a block admissibility fails           -> CONSTRUCT-FAIL                                                   ✓
(8) DETERMINISM — analyzer + covariate logger each BYTE-IDENTICAL across two runs on fixed inputs.            ✓
(9) IMPORT / EXECUTION BOUNDARY — no torch/mlx/transformers/openai/anthropic/requests/urllib/http/subprocess;
    no model execution, no prompt execution, no fresh materialization. Pure scoring/classification.            ✓
(10) UNTRACKED TIER0 FILES — the build commit NOTES (no action) two pre-existing untracked tier0-run/
     tokenizer.json files that were NOT staged; git show --stat HEAD touches no tier0/tokenizer files. They do
     not affect this tooling build.                                                                            ✓
```

## 4. N1 / N2 verification (summary)

```text
N1.A: hop1+hop2-only is both CODE-ENFORCED (ALLOWED_CONTEXTS) and BEHAVIORALLY VERIFIED (composite/dq injection
      changed nothing). render-4-execute-2 holds: the realizer may render four contexts, but only hop1+hop2 are
      scored/logged/branched; the out-of-scope two cannot enter any output or claim.
N2:   priority order CONSTRUCT-FAIL > HOP2-CONTROL-FAIL > {stability} is enforced and demonstrated on the two
      cases (D, E) where the higher-priority branch overrides what the stability verdict alone would say.
```

## 5. Discrepancies / blockers

```text
None. (Note, out of scope: tracked tier0-run int4/int8 tokenizer_config.json files pre-exist in the repo,
untouched by this build. If ever intended for a compression rung, that is a separate pre-registration; flagged
for awareness only — it does not bear on this tooling or this verification, and the program remains pre-stress.)
```

## 6. Recommended next route

```text
PASS -> proceed per the hop1-stability prereg routing:
  CS files the prereg to a readable in-review path -> C5 claim-risk review -> CS feasibility review -> TL
  approval consideration -> Manager by-name RUN authorization (only if approved) -> CS execution -> SE verification.
The tooling is verified; the fresh 6-block run remains gated and is NOT authorized by this verification.
```

## 7. Boundary

```text
- Verification only. No run, no fresh materialization for execution, no prompt execution, no model execution,
  no composite-gate retry, no compression, no INT8/INT4, no Claim C, no Paper B, no certification claim, no
  capability claim, no mechanism claim.
- The Path A FP16 K=5 FAIL remains closed and untouched. SE verifies; SE authorizes nothing.
```

— Senior Engineer (hop1-stability tooling verification; PASS)
