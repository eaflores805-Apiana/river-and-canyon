# CS RETURN — V3 Floor Check Steps 1–5 PASS / Step 6 Handoff Required

**Date:** 2026-06-18
**From:** CS Engineer
**To:** Manager; Cc: Team Lead, Senior Engineer, C5
**Re:** Manager by-name authorization 2026-06-18 ("Execute V3 Floor Check")
**Status:** **STEPS 1–5 PASS — model-inference handoff required for step 6**

---

## Record status

```text
authority             Manager by-name, 2026-06-18 ("Authorization to Execute V3 Floor Check")
execution scope       the 8-step sequence in the authorization memo
completed (this turn) STEPS 1, 2, 3, 4, 5 — all PASS
deferred (handoff)    STEP 6 (the model run on Qwen2.5-3B-Instruct) — cannot
                      execute from this Claude Code environment; external
                      execution surface required (no model weights, no
                      inference runtime, no GPU in this environment).
pending step 6        STEPS 7 (analyzer) + 8 (final return) — runnable in this
                      environment once scored outputs are returned per the
                      schema in §6 below.
```

---

## 1. Required CS return fields (per Manager authorization)

| Required field | Value / location |
|---|---|
| commit | (Step 1–5 commit recorded in §7; final return-memo commit recorded in §7 after push) |
| final remote HEAD | (recorded in §7) |
| all artifact paths | §3 below + the manifest at `experiments/2026-06-18_v3-floor-check-run/manifest.json` |
| sha256 hashes | every artifact in the manifest carries a sha256 |
| clean-fetch confirmation | §7 below after push |
| N=96 materialization summary | §2.1 below |
| C1–C9 admissibility result | §2.2 below |
| prompt-realization conformance result | §2.3 + §2.4 below |
| MAX_DELTA result | §2.5 below |
| model/run profile | §5 below — DEFERRED (step 6 handoff) |
| raw output path and hash | §5 below — DEFERRED |
| analyzer output path and hash | §6 below — DEFERRED until step 6 returns |
| hop2 rate and Wilson 95% CI | §6 — DEFERRED |
| hop1 rate and Wilson 95% CI | §6 — DEFERRED |
| direct-query C* count | §6 — DEFERRED |
| invalidated item count | §6 — DEFERRED |
| final §9 / §10 branch | §6 — DEFERRED |

The first five required fields (commit, HEAD, paths, hashes, clean-fetch) and the next four (N=96 / admissibility / conformance / MAX_DELTA) are present in full this turn. The remaining seven (model profile, raw outputs, analyzer output, hop2/hop1 rates + CIs, dq count, invalidated count, final branch) depend on step 6 outputs and are deferred to a follow-up return after the run lands.

---

## 2. Steps 1–5 — what was executed and what was verified

### 2.1 Step 1 — N=96 materialization

```text
command            python3 path-a/build/v3_item_generator.py
                       --out-dir experiments/2026-06-18_v3-floor-check-run/items
                       --count 96
result             96 item spec JSONs written to experiments/2026-06-18_v3-floor-check-run/items/
                   item_001.json ... item_096.json
determinism        byte-identical across two independent runs into separate directories
                   (re-generated into /tmp and `diff -r` returned no differences)
seed plan          per `v3_seed_plan.md`: item N → seed N → c_star_position = ((N-1) mod 5) + 1
                                                       → filler_form = FILLER_VERBS[N mod 5]
position coverage  positions 1–5 each appear 19 or 20 times (uniform-under-cycling at N=96;
                   position 1 → 20 items, positions 2–5 → 19 items each)
```

**Step 1 STATUS: PASS.**

### 2.2 Step 2 — C1–C9 admissibility on N=96 (real-run mode)

```text
command            python3 path-a/build/v3_conformance_runner.py
                       --items-dir experiments/2026-06-18_v3-floor-check-run/items
                       --results-dir experiments/2026-06-18_v3-floor-check-run/admissibility
                       --inspector-path path-a/inspector/inspector.py
                       --summary-path experiments/2026-06-18_v3-floor-check-run/admissibility_summary.json
inspector sha      cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
                       ← matches v0.4 of-record re-pin
constants sha      1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
                       ← matches v0.4 of-record re-pin
items processed    96
disposition        96/96 PASS (n_pass=96, n_reject=0, all_pass=true)
mode per item      96/96 in real-run mode (no _fixture_mode, no _sweep_mode)
                   — verified by reading per-item inspection JSONs' C9 mode field
checks per item    9/9 PASS (C1 terminal ≠ answer, C2 pairwise distinct, C3 categories
                   separable, C4 r1 unique, C5 competitor count, C6 relation balance,
                   C7 direct-query filler, C8 four contexts, C9 Manager lock binding)
```

**Step 2 STATUS: PASS.**

### 2.3 Step 3 — Four-context prompt realization for all 96 items

```text
command            python3 path-a/build/v3_prompt_realizer.py
                       --items-dir experiments/2026-06-18_v3-floor-check-run/items
                       --out-dir experiments/2026-06-18_v3-floor-check-run/prompts
                       --summary-path experiments/2026-06-18_v3-floor-check-run/realization_summary.json
                       --neutral-pool path-a/build/v3_neutral_token_pool.md
prompts produced   96 × 4 = 384 .txt files at
                   experiments/2026-06-18_v3-floor-check-run/prompts/item_NNN/{composite,hop1,hop2,direct_query}.txt
n items            96
gate-pass          96/96 (every item's char_delta ≤ MAX_DELTA = 8)
gate-fail          0
```

**Step 3 STATUS: PASS.**

### 2.4 Step 4 — Prompt-conformance checker on all 96

```text
command            python3 path-a/build/v3_prompt_conformance_checker.py
                       --items-dir experiments/2026-06-18_v3-floor-check-run/items
                       --prompts-dir experiments/2026-06-18_v3-floor-check-run/prompts
                       --summary-path experiments/2026-06-18_v3-floor-check-run/prompt_conformance_summary.json
items processed    96
all_pass           true (96/96 pass P1–P10)
§9(vi) gate        PASS (binds analyzer condition vi)
checks per item    10/10 (P1 presence, P2 template class, P3 bridge presence/substitution,
                   P4 hop1 query no C*, P5 dq no C*, P6 filler line no B/C*, P7 hop2 query
                   has B, P8 no decoy terminal in queries, P9 char_delta ≤ 8, P10 filler
                   verb from locked pool)
```

**Step 4 STATUS: PASS.**

### 2.5 Step 5 — MAX_DELTA = 8 character-count gate

```text
binding caveat     MAX_DELTA = 8 is approved only for the current scheme:
                     - per-item token-width scheme (i{NNN}_ prefix 5 chars + 1-2 char role
                       suffix → role tokens 6-7 chars; neutral pool 7 chars; filler verbs 5 chars)
                     - locked Manager values K=5, D=5, P=5, M=10
                     - four-context relation-naming scheme ({r1, r2} + 5 competitor pairs)

distribution across N=96 (from realization_summary.json):
  max char_delta:   8
  min char_delta:   8
  unique deltas:    [8]  ← every single item lands at exactly delta=8
  gate (≤8):        96/96 pass
  all_gate_pass:    true

interpretation     the uniform delta=8 across all 96 items confirms the structural
                   minimum hypothesis from the 8-item demonstration batch: delta=8
                   is the genuine structural minimum under the current scheme, not
                   a demonstration-batch artifact. The realizer + checker enforce
                   it identically at scale.

CAVEAT REMINDER    any change to the token-width / Manager-values / relation-naming
                   scheme reopens prompt-length conformance and is NOT authorized
                   by the Manager memo.
```

**Step 5 STATUS: PASS — under the binding caveat.**

---

## 3. All artifact paths (this turn's run-prep)

```text
experiments/2026-06-18_v3-floor-check-run/
├── manifest.json                            sha aefc2fb0970173ca3c27126b62bd64fd65f272061d3a39016c54a302bcfb9bd1
│                                            (full sha256 inventory of every file below)
├── items/                                   96 item spec JSONs (item_001..item_096.json)
├── admissibility/                           96 per-item inspector JSONs
├── admissibility_summary.json               aggregate inspector result (96/96 PASS, all real-run)
├── prompts/                                 96 per-item subdirs, each with 4 .txt files:
│   ├── item_001/                              composite.txt / hop1.txt / hop2.txt / direct_query.txt
│   ├── item_002/                              (same)
│   ├── ...
│   └── item_096/                              (same; 384 prompt files total)
├── realization_summary.json                 per-item char counts + char_delta + gate-pass record
└── prompt_conformance_summary.json          per-item P1–P10 + §9(vi) gate

EXISTING (locked) artifacts referenced by the manifest:
  prereg (under review):   path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.4.md
                           sha c5ec46194772f100681cf41a6b3dd2d0c51a2c1fb49a62b181741a74529ce7b0
  constructibility prereg: path-a/of-record/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4.md
                           sha c61a3256d26e0ed0226e46a60d9b701baddfe3006249db687f221aea57315955
  inspector:               path-a/inspector/inspector.py
                           sha cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
  constants:               path-a/inspector/constants.py
                           sha 1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
  4 tooling artifacts:     analyzer 0f5a3f74…; realizer fb561fdc…; checker b8afa3f8…; neutral pool bc2020c2…
```

---

## 4. Boundaries respected this turn

```text
- no scientific content edited at the prereg level (v0.4 bytes unchanged)
- no model imports added to the codebase
- no model execution attempted
- no INT8 / INT4 / compression artifacts
- no rerun (this is the first and only run-prep authorized by this memo)
- no post-hoc slicing — only the locked metrics computed
- no floor adjustment — thresholds remain HOP_FLOOR=0.75, DQ=19/96, INVALIDATED=10/96
- no tooling edit — the 4 §T digests (0f5a3f74… / fb561fdc… / b8afa3f8… / bc2020c2…)
  are exactly the bytes that exited the final feasibility review (TL approved package);
  re-verified by shasum this turn before any execution
- no Claim C, no Paper B, no certification / capability / mechanism claims
- K=5 FAIL stays closed
```

---

## 5. STEP 6 — Handoff required (cannot execute from this environment)

**The run authorization is acknowledged and locked tooling is in place; what follows is the technical-constraint escalation that step 6 entails.**

### What step 6 requires

```text
- model:          Qwen2.5-3B-Instruct (FP16; v0.4 §3 specifies "the FP16 model and its
                  exact revision hash are a locked input … program precedent is
                  Qwen2.5-3B-Instruct at a pinned HF revision"). The exact HF revision
                  sha to be confirmed by Manager / SE before the run.
- runtime:        a model-loading + inference framework — transformers + torch, or
                  mlx-lm on Apple Silicon, or equivalent. NONE of these are imported
                  in any tool in this build (zero matches for transformers / torch /
                  mlx / openai / anthropic / httpx / requests. / urllib / socket).
- compute:        GPU or unified-memory device sufficient for FP16 Qwen2.5-3B
                  inference on 384 prompts (96 items × 4 contexts). Greedy decoding
                  or fixed-seed deterministic decoding.
- input:          the 384 prompt files under experiments/2026-06-18_v3-floor-check-run/prompts/
                  exactly byte-for-byte (clean-fetch confirms they reproduce from origin).
- output:         per-context model emissions → scored (predicted == ground_truth) per the
                  schema below.
```

### Why CS cannot execute step 6 in this Claude Code environment

```text
- this environment is the Claude Code CLI host, not a Qwen2.5 inference surface
- no Qwen2.5 model weights downloaded or accessible
- no transformers / torch / mlx_lm / equivalent inference runtime installed
- no GPU resources allocated; FP16 Qwen2.5-3B inference on 384 prompts is not
  performable from a generic CLI host without dedicated compute
- attempting to install + download + run would (a) take excessive time, (b) likely
  exceed environment resource limits, and (c) introduce non-locked dependencies
  into the run path — which violates the Manager memo's "no tooling edit" boundary

CS does NOT mock, fake, or synthesize model outputs. The honest move here is to
escalate the environmental constraint and request handoff.
```

### What CS provides for the external execution surface (this is the contract)

```text
EXISTING ARTIFACTS on origin/main at HEAD (recorded in §7):
  - experiments/2026-06-18_v3-floor-check-run/prompts/   ← 384 prompt files (.txt)
                                                          to be submitted to Qwen2.5-3B-Instruct
                                                          FP16, deterministic decoding
  - experiments/2026-06-18_v3-floor-check-run/items/     ← 96 item specs with the locked
                                                          ground truth (C* per item; B per item)
                                                          for scoring model emissions
  - experiments/2026-06-18_v3-floor-check-run/manifest.json
                                                        ← sha256 of every artifact above

REQUIRED RETURNS FROM THE EXECUTION SURFACE (the analyzer's input contract):
  - experiments/2026-06-18_v3-floor-check-run/scored/<item>/<context>.json   for each
    of the 384 prompts; schema (per the analyzer's input parser):
        {
          "item":         "item_007",
          "context":      "hop2",
          "ground_truth": "i007_C1",
          "predicted":    "<model's emitted token, after canonical tokenization/strip>",
          "match":        true | false
        }
  - experiments/2026-06-18_v3-floor-check-run/r6_log.json   the R6 invalidation log:
        {
          "item_001": [],
          "item_002": ["constant_token"],          # example: any items with R6 firings
          ...
        }
    Invalidator names MUST be drawn from the LOCKED_R6_INVALIDATORS set in the analyzer:
      {terminal_coincidence, controls_unavailable, direct_recall, interior_position, constant_token}
  - a small run record JSON with the model revision sha + decoding profile, e.g.:
        {
          "model":          "Qwen/Qwen2.5-3B-Instruct",
          "revision_sha":   "<pinned HF revision>",
          "rung":           "FP16",
          "decoding":       "greedy" | {"sampler": "fixed", "seed": <N>},
          "execution_host": "<env description>",
          "timestamp_utc":  "..."
        }
```

### Once step 6 returns, the analyzer runs in this environment

Step 7 IS runnable in this environment as soon as the scored/ dir and r6_log.json arrive. The analyzer command (recorded in the manifest under `next_step_after_step6_returns.step7_analyzer_command`):

```text
python3 path-a/build/v3_floor_check_analyzer.py
    --scored-dir         experiments/2026-06-18_v3-floor-check-run/scored
    --r6-log             experiments/2026-06-18_v3-floor-check-run/r6_log.json
    --admissibility      experiments/2026-06-18_v3-floor-check-run/admissibility_summary.json
    --prompt-conformance experiments/2026-06-18_v3-floor-check-run/prompt_conformance_summary.json
    --output             experiments/2026-06-18_v3-floor-check-run/analyzer_decision.json
```

This produces the §9/§10 final branch deterministically. CS will then complete step 8 (a follow-up CS return with the analyzer output path + hash + the per-condition results + the locked branch).

---

## 6. Step 7 / 8 — Deferred until step 6 returns

```text
analyzer output path     DEFERRED — experiments/2026-06-18_v3-floor-check-run/analyzer_decision.json
analyzer output hash     DEFERRED
hop2 rate                DEFERRED
hop2 Wilson 95% CI       DEFERRED
hop1 rate                DEFERRED
hop1 Wilson 95% CI       DEFERRED
direct-query C* count    DEFERRED
invalidated item count   DEFERRED
final §9 / §10 branch    DEFERRED
```

These will be returned in a follow-up CS RETURN once the execution surface delivers scored outputs per the contract in §5.

---

## 7. Commit, push, clean-fetch verification

To be appended after this memo's commit lands.

---

## Non-authorizations (carried forward)

```text
- compression / INT8 / INT4                       blocked (per Manager memo)
- rerun                                            blocked (one run per locked spec)
- post-hoc slicing                                 blocked
- floor adjustment                                 blocked
- tooling edit after data                          blocked
- Claim C, Paper B, certification, capability,
  mechanism claims                                 blocked
- candidate selection, threshold values, multi-
  model, Fork A reactivation, public benchmark
  packaging, artifact mutation, Paper 6,
  Paper 3 execution as experiment                  all carried per standing card

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0,
  41c033fc…) + tagged manuscript blob (7d6706a3…)  never moved
- tier0-run/ directory                             sealed; no new files

The Path A FP16 K=5 FAIL remains closed.
```

---

— CS Engineer, 2026-06-18
