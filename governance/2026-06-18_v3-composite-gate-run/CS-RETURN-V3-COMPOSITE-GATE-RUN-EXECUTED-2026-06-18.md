# CS RETURN — V3 Composite Gate Run Executed (Final §7/§8 branch: PRECONDITION-FAIL)

**Date:** 2026-06-18
**From:** CS Engineer
**To:** Manager; Cc: Team Lead, Senior Engineer, C5
**Re:** Manager by-name authorization 2026-06-18 ("Authorization to Execute V3 Composite Gate Fresh Run")
**Status:** **RUN COMPLETE. FINAL §7/§8 BRANCH: PRECONDITION-FAIL.**

---

## Record status

```text
authority             Manager by-name authorization 2026-06-18 (V3 Composite Gate)
package               TL-approved (governance/2026-06-18_v3-composite-gate-tl-approval/
                      TL-APPROVAL-V3-COMPOSITE-GATE-PACKAGE-2026-06-18.md)
run scope             V3 Composite Gate, fresh seeds 097..192, N=96, FP16 greedy,
                      Qwen2.5-3B-Instruct revision aa8e72537993ba99e69dfaafa59ed015b17504d1
10-step sequence      ALL 10 STEPS EXECUTED in the authorized order
final §7/§8 branch    PRECONDITION-FAIL
                      (cond_c "preconditions hold on fresh set" fails because
                       hop1-isolated Wilson lower 0.2102 << 0.75 floor; gate not read)
interpretation        per v0.2 §8: "fresh set not on admissible ground; the
                      composite gate is NOT read. Examine / re-pre-register. NOT a
                      composite conclusion." No certification, no capability, no
                      mechanism, no Claim C, no Paper B claimed.
```

---

## 1. The §7/§8 final branch

```text
FINAL BRANCH: PRECONDITION-FAIL (analyzer exit code 2)

§7 conditions (5 of 5):
  (a) composite-correct lower Wilson > 0.75    0.5569 ≤ 0.75   FAILS
       (composite 63/96 = 0.6562; Wilson 95% [0.5569, 0.7436])
  (b) composite-correct lower Wilson > 0.45    0.5569 > 0.45   PASS
       (composite cleared the not-shortcut floor)
  (c) preconditions hold (hop2 + hop1 + dq)                   FAILS
       hop2 Wilson lower 0.9615 > 0.75                          PASS
       hop1 Wilson lower 0.2102 < 0.75                          FAILS  ← THE BLOCKER
       dq C* count 0 ≤ 19                                       PASS
  (d) construct clean (admissibility + conformance + invalidated)  PASS
       admissibility 96/96 real-run PASS                        PASS
       prompt-conformance 96/96 P1-P10 PASS                     PASS
       invalidated 0 < 10                                       PASS
  (e) error-structure non-pathological                          PASS
       composition_specific_success count: 0                    PASS

§8 routing: (c) fails → PRECONDITION-FAIL (priority over CONSTRUCT-FAIL)
            Composite gate NOT read.
            Composite result (63/96 = 0.6562) is INFORMATIONAL ONLY per v0.2 §8.
```

### Interpretation (per v0.2 §8, verbatim)

```text
"PRECONDITION-FAIL (components not admissible on the fresh set):
  hop2/hop1 below floor, or dq >= 20/96, on the FRESH items -> fresh set not on
  admissible ground; gate NOT read; examine / re-pre-register. NOT a composite
  conclusion."
```

The fresh set at indices 097..192 is **not on admissible ground** for the composite-gate question because the hop1-isolated retrieval rate (28/96 = 0.292) falls well below the 0.75 reliability floor. The composite gate is **NOT** read this run. The remedy per the prereg is to examine why hop1 failed and to re-pre-register a fresh run (which is a separate Manager-by-name authorization, not enabled here).

---

## 2. Required Manager-return fields

### Commit + final remote HEAD + clean-fetch confirmation

```text
commit                       <recorded in §11 after push>
final remote HEAD            <recorded in §11>
clean-fetch confirmation     <recorded in §11>
```

### Item materialization paths and hashes

```text
items dir          experiments/2026-06-18_v3-composite-gate-run/items/
                   96 spec JSON files at item_097.json … item_192.json
generator          v3_composite_gate_item_generator.py (sha cc07e5a2…; wrapper)
disjointness       byte-distinct from floor-check {001..096} (verified live this
                   turn: `diff item_097.json floor-check/item_007.json` → distinct;
                   0 shared role tokens between sets per prefix-injection proof)
```

### Prompt paths and hashes

```text
prompts dir        experiments/2026-06-18_v3-composite-gate-run/prompts/
                   384 prompt files at item_NNN/{composite,hop1,hop2,direct_query}.txt
realizer           v3_prompt_realizer.py (sha fb561fdc…; UNCHANGED)
MAX_DELTA result   96/96 gate-pass at delta=8 exactly (unique deltas: [8])
```

### Admissibility summary

```text
path                 experiments/2026-06-18_v3-composite-gate-run/admissibility_summary.json
sha256               4449ccdda9ef2094c16c841d0a4bf9c71ec1feebe07d716894b49e83d4da4030
result               96/96 PASS in real-run mode (every item C9.mode == "real-run";
                     all 9 checks pass per item)
inspector            cb4b0b60… (UNCHANGED)
constants            1d761c3d… (UNCHANGED)
```

### Prompt-conformance summary

```text
path                 experiments/2026-06-18_v3-composite-gate-run/prompt_conformance_summary.json
sha256               4e9402e4bec2a0c989281546dc44af830556330c674bf902edd8d1f53c28af0a
result               96/96 PASS P1-P10; §9(vi) gate: PASS
checker              b8afa3f8… (UNCHANGED)
```

### Model / run profile

```text
model_name             Qwen/Qwen2.5-3B-Instruct
model_revision_sha     aa8e72537993ba99e69dfaafa59ed015b17504d1   (program's locked snapshot,
                                                                   same as the floor-check run)
precision              FP16 (mlx_lm default for non-quantized Qwen2.5)
decoding               greedy (temp=0.0 / argmax sampler)
max_new_tokens         24
inference runtime      mlx_lm 0.31.3 / transformers 5.10.2 / torch 2.7.1 / Python 3.13.3
host                   Apple M2 Max
model_load_time_s      9.3
inference_time_s       302.5 (5 min 3 s)
n_prompts_total        384 (executed exactly once; no retries; no recomputations)
prompts_consumed_as_committed     true
prompt_regeneration_occurred      false
inference script       reused experiments/2026-06-18_v3-floor-check-run/run_step_6.py
                       (the floor-check inference script; pure model-input → model-output
                        function; no floor-check-specific logic; scope-text generic)
```

### Raw / scored output paths and hashes

```text
scored dir              experiments/2026-06-18_v3-composite-gate-run/scored/
                        96 per-item subdirs × 4 contexts = 384 scored JSONs
                        schema: {item, context, ground_truth, predicted, match}
                        (.raw.json debug copies were used during inference and
                         then stripped; the analyzer reads only the contract
                         JSONs, not the raw debug copies)
```

### r6_log.json

```text
path                   experiments/2026-06-18_v3-composite-gate-run/r6_log.json
sha256                 646bf4cffd9904b3287304ee410b2dd50c67973bcec6bed42333a8bfad04c415
content                {item_097: [], …, item_192: []}   (no R6 firings)
fired count            direct_recall: 0 / 96   (no item had dq.match=True)
                       constant_token: 0 / 96   (no uniform-wrong-cross-query token)
                       other 3 invalidators not mechanically determinable from this
                       snapshot (terminal_coincidence / controls_unavailable /
                       interior_position) — documented in build_r6_log.py
```

### error_log.json

```text
path                   experiments/2026-06-18_v3-composite-gate-run/error_log.json
sha256                 3a89243bd44cbeed991de664b25e72cd984dc1435e0beda466ffcb1c7f616274
items                  96
composite match count  63
composite error count  33
composition_specific_success_count   0
pathological_error_structure         false
landed token distribution            correct: 63, decoy_chain_depth_2: 1, competitor_or_other: 32
cooccurrence distribution            fully_correct: 63, composition_specific: 33
                                      (no inherited_component_failure because hop2 = 96/96
                                       so no hop2 failures co-occurred; no
                                       composition_specific_success because no item had
                                       composite=T AND hop2=F)
```

### analyzer_decision.json

```text
path                   experiments/2026-06-18_v3-composite-gate-run/analyzer_decision.json
sha256                 3924ff35087c5648a20101e463f2129d6d731a853c4b9f0e3d61a4ade6efe842
determinism            re-run analyzer on same inputs → byte-identical decision
                       (sha unchanged across two independent runs)
final_branch           PRECONDITION-FAIL
analyzer_version       v0.1
```

### Composite-correct rate and Wilson 95% CI

```text
composite k / n        63 / 96
rate                   0.6562
Wilson 95% CI          [0.5569, 0.7436]
condition (a) (lower > 0.75):  FAILS   (0.5569 ≤ 0.75)
condition (b) (lower > 0.45):  PASS    (0.5569 > 0.45)
                                       (composite cleared the not-shortcut floor;
                                        sub-message: "not explained by foreclosed
                                        shortcuts, but not reliably composing"
                                        — BUT this sub-message DOES NOT FIRE
                                        because the §8 routing puts the result
                                        on PRECONDITION-FAIL, NOT on
                                        COMPOSITE-DOES-NOT-CLEAR-THIS-RUN)
informational only     per v0.2 §8 the composite gate is NOT read when (c)
                       fails; the composite result is informational and is
                       NOT a composite-gate conclusion.
```

### 0.75 reliability gate result

```text
composite Wilson lower 0.5569 < 0.75    FAILS  (informational — gate not read)
                                                because preconditions failed
```

### 0.45 not-shortcut floor result

```text
composite Wilson lower 0.5569 > 0.45    PASS   (informational — gate not read)
                                                composite is above the chance floor
                                                F+margin = 0.45 (which would mean
                                                "not explained by foreclosed
                                                shortcuts" IF the preconditions
                                                had held — but they didn't, so
                                                the composite result remains
                                                informational only)
```

### hop1 / hop2 / direct-query precondition results

```text
hop2 k / n              96 / 96 = 1.000
hop2 Wilson 95% lower   0.9615 > 0.75 floor                     PASSES
hop2 precondition       PASS

hop1 k / n              28 / 96 = 0.2917
hop1 Wilson 95% lower   0.2102 < 0.75 floor                     FAILS   ← THE BLOCKER
hop1 Wilson 95%         [0.2102, 0.3892]
hop1 precondition       FAILS — this is the cause of PRECONDITION-FAIL

direct-query k          0 / 96 = 0.000
direct-query count      0 ≤ 19 ceiling                          PASSES
direct-query precondition  PASS
                        (no direct-recall observed; model never produced C* under
                         bridge withheld; consistent with the no-direct-recall
                         design goal — same behavior as the floor-check run)
```

### Invalidated item count

```text
invalidated count       0 / 96
threshold               < 10
construct_pass          PASS (well under the 10/96 set-level construct-fail line)
                        Item-level R6 invalidators that fired this run:
                          direct_recall:   0 (no dq matches → no item-level fire)
                          constant_token:  0 (no uniform-wrong-cross-context token)
                          (other 3 invalidators not mechanically determinable from
                           the scored snapshot alone)
```

### Final §7 / §8 branch

```text
**PRECONDITION-FAIL**

Cause:                 cond_c fails — hop1 below floor on the fresh set
Composite gate         NOT read (per v0.2 §8 priority routing: precondition-fail
                       takes precedence over construct-fail and over the
                       composite-gate evaluation)
Composite informational     63/96 = 0.6562, Wilson [0.5569, 0.7436] — NOT a
                            composite-gate conclusion
Remedy per v0.2 §8     "Examine / re-pre-register. NOT a composite conclusion."
                       This requires a NEW pre-registration (Senior draft) and a
                       FRESH Manager by-name authorization. The remedy is NOT
                       authorized by this memo's authorization.
```

---

## 3. Empirical contrast (data; NOT mechanism claim per v0.2 §10)

For the record, in numbers only:

```text
                                       floor-check       composite-gate
                                       {001..096}        {097..192}
hop2-isolated                          96/96 = 1.000     96/96 = 1.000     identical
hop1-isolated                          87/96 = 0.906     28/96 = 0.292     ↓ 58 percentage points
composite                              80/96 = 0.833     63/96 = 0.656     ↓ 18 percentage points
direct-query (C*)                       0/96 = 0.000      0/96 = 0.000     identical
invalidated                             0/96              0/96             identical
admissibility (C1-C9)                  96/96 PASS        96/96 PASS        identical
prompt conformance (P1-P10)            96/96 PASS        96/96 PASS        identical
MAX_DELTA (per item)                    delta = 8         delta = 8        identical
```

The notable difference is **hop1 dropping from 87/96 to 28/96** while EVERY OTHER measured property is identical (hop2, dq, invalidated, admissibility, conformance, MAX_DELTA all match). The only difference between the two runs at the construction level is the per-item index (001..096 vs 097..192).

**Mechanism is NOT decidable from this run** (per v0.2 §10: "NO mechanism claims (traversal vs grab vs anchor not decidable here)"). The hop1 swing is **DATA**; the WHY is the next, separately gated question and **NOT** claimed here.

Some hypothesis space (not asserted as findings; recorded as candidate questions for a separately-authorized future analysis):

```text
- tokenization sensitivity: Qwen2.5's BPE may tokenize "i007_A" and "i097_A"
  differently in ways that affect hop1 retrieval
- prefix-range effect: the model may treat 2-digit-significant-decimals (007)
  differently from 3-digit (097, 192) in some way
- statistical fluctuation: extremely unlikely given the magnitude (87/96 vs 28/96
  is far outside any plausible sampling variance for the same task)
- something else mechanical-but-not-mechanism: a property of the construction
  realization that varies with the index range

NONE of these are claimed as findings. They are recorded as the candidate
questions the §8-required "examine" step might address under a separately
authorized analysis.
```

---

## 4. Forbidden interpretations (carried verbatim from v0.2 §10)

```text
The result PRECONDITION-FAIL must NOT be read as ANY of:
  - "the model composes"                              (NOT EVEN EVALUATED — gate not read)
  - general two-hop capability                        (no)
  - a mechanism claim                                 (no — hop1 swing has no mechanism here)
  - seam evidence                                     (no)
  - compression readiness                             (no — FP16 only authorized)
  - Claim C                                           (no)
  - Paper B                                           (no)
  - FINAL certification from one run                  (no — and this isn't even a cleared run)

A PRECONDITION-FAIL outcome IS:
  - a valid §8 routing outcome                        (yes — the prereg's safety rule fired)
  - data that the fresh set isn't on admissible       (yes — hop1 below floor on 097..192)
  - a flag for examine / re-pre-register              (yes — the remedy per v0.2 §8)

ALSO:
  - The C0 K=5 FAIL stays CLOSED; V3 ≠ C0; this run does not bear on it.
  - Survival is not correctness; "not ruled out" is not "established."
  - GATE-CLEARED-THIS-RUN is NOT the result of this run (the gate wasn't read).
```

---

## 5. What's open vs blocked after this result

```text
OPEN (separately gated; not authorized by this run):
  - Re-pre-registration of a fresh composite-gate run (Senior draft → CS feasibility
     → C5 claim-risk → TL approval → SEPARATE Manager by-name authorization). The
     re-pre-registration might:
       (a) choose a different fresh seed range (would need to verify hop1 admissibility
            on the new range as part of preconditions)
       (b) include a hop1-investigation pre-run (separately preregistered) to
            understand WHY hop1 differs between {001..096} and {097..192}
       (c) extend the construct's analysis surface (e.g., index-range robustness)

BLOCKED (carried per Manager memo + standing card):
  no rerun of this prereg
  no compression / INT8 / INT4
  no post-hoc slicing (we report only the locked metrics)
  no prompt edits after generation
  no floor adjustment ("never a license to lower 0.75")
  no tooling edit after data
  no Claim C, Paper B, final certification, capability, or mechanism claims
  K=5 FAIL stays closed (V3 ≠ C0)
```

---

## 6. Commit, push, clean-fetch verification

Performed after the run-commit landed; `git fetch origin` immediately preceded the verification.

```text
commit                       d92c73a075e6d4821e1b41141a7b71ef9e388a6a   (970 files; 49064 insertions)
push                         86fea7c..d92c73a  main -> main
origin/main HEAD             d92c73a075e6d4821e1b41141a7b71ef9e388a6a
local       HEAD             d92c73a075e6d4821e1b41141a7b71ef9e388a6a   (match)

per-file verification (origin/main bytes → local bytes):

RUN ARTIFACTS:
MATCH  experiments/2026-06-18_v3-composite-gate-run/analyzer_decision.json
        (3924ff35…; the final §7/§8 branch JSON)
MATCH  experiments/2026-06-18_v3-composite-gate-run/run_record.json
MATCH  experiments/2026-06-18_v3-composite-gate-run/r6_log.json
MATCH  experiments/2026-06-18_v3-composite-gate-run/error_log.json
MATCH  experiments/2026-06-18_v3-composite-gate-run/admissibility_summary.json
MATCH  experiments/2026-06-18_v3-composite-gate-run/prompt_conformance_summary.json
MATCH  experiments/2026-06-18_v3-composite-gate-run/scored/item_097/composite.json
        (endpoint check; 95 more items × 4 contexts = 380 more scored JSONs
         also on origin/main per the commit log)
MATCH  experiments/2026-06-18_v3-composite-gate-run/scored/item_192/hop1.json

LOCKED TOOLING — UNCHANGED through the run (the "no tooling edit after data" attestation):
MATCH  path-a/build/v3_composite_gate_analyzer.py             (3a3e954e…)
MATCH  path-a/build/v3_composite_error_logger.py              (2ed46628…)
MATCH  path-a/build/v3_composite_gate_item_generator.py       (cc07e5a2…)

GOVERNANCE (this turn):
MATCH  governance/2026-06-18_v3-composite-gate-run/MANAGER-AUTHORIZATION-V3-COMPOSITE-GATE-RUN-2026-06-18.md
MATCH  governance/2026-06-18_v3-composite-gate-run/CS-RETURN-V3-COMPOSITE-GATE-RUN-EXECUTED-2026-06-18.md
        (this file, PRIOR to the §6 commit; cross-verifies on the next sweep)
```

All 13 listed key artifacts reproduce byte-exact from the shared repository on a clean fetch. The full 970-file commit (96 items + 96 admissibility + 384 prompts + 384 scored + 4 summary JSONs + 3 analysis JSONs + run_record + run_step_6.log + 2 governance memos) is on origin/main at HEAD `d92c73a…`.

**V3 Composite Gate run FILED. Final §7/§8 branch: PRECONDITION-FAIL.**

---

— CS Engineer, 2026-06-18 (clean-fetch appendix)

---

## Non-authorizations (carried verbatim from the Manager memo + standing card)

```text
- compression / INT8 / INT4                blocked
- rerun                                    blocked (one run per locked spec)
- prompt edits after generation            blocked
- post-hoc slicing                         blocked
- floor adjustment                         blocked
- tooling edit after data                  blocked (the 9 §T-locked digests verified
                                                    UNCHANGED post-run)
- Claim C, Paper B                         blocked
- final certification claim                blocked
- general capability claim                 blocked
- mechanism claim                          blocked
- seam evidence claim                      blocked
- candidate selection, threshold values, multi-model, Fork A reactivation,
  public benchmark packaging, artifact mutation, Paper 6, Paper 3 execution
  as experiment                            all carried per standing card

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc…) + tagged manuscript
  blob (7d6706a3…)                        never moved
- tier0-run/ directory                     sealed; no new files

The Path A FP16 K=5 FAIL remains closed.
```

---

— CS Engineer, 2026-06-18
