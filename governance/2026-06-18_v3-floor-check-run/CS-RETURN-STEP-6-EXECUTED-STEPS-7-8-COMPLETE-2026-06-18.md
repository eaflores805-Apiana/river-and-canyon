# CS / Execution Return — V3 Floor Check Step 6 Complete (Steps 7 + 8 also executed)

**Date:** 2026-06-18
**From:** CS Engineer (executing role; same Claude Code instance as prior CS returns)
**To:** Manager; Cc: Team Lead, Senior Engineer, C5
**Re:** Manager + TL Start memo 2026-06-18 ("Start Step 6 — V3 Floor Check Model Execution")
**Status:** **STEP 6 EXECUTED. STEPS 7 + 8 COMPLETE. §10 BRANCH: COMPONENT-ADMISSIBLE-UNDER-COMPETITION.**

---

## Record status

```text
authority             Manager by-name authorization 2026-06-18 (Execute V3 Floor Check) +
                      Manager + TL Start memo 2026-06-18 (Start Step 6)
execution surface     Apple M2 Max host (same machine that produced the prior Path A FP16
                      K=5 FAIL run referenced throughout the program). The previous CS
                      return's "cannot execute" was incorrect — mlx_lm 0.31.3 was already
                      installed and Qwen2.5-3B-Instruct (FP16, locked revision sha
                      aa8e72537993ba99e69dfaafa59ed015b17504d1) was already cached at
                      ~/.cache/huggingface. Re-verified, confirmed, and executed.

step 6                COMPLETED — 384 prompts × greedy decoding × FP16 → scored outputs
step 7                COMPLETED — analyzer ran; §10 branch emitted
step 8                COMPLETED — this return memo

§10 final branch       COMPONENT-ADMISSIBLE-UNDER-COMPETITION
                      (all six §9 conditions PASS; clean executable construct; hop2 cleared
                      its 0.75 floor under V3 same-depth-competitor competition at the locked
                      K=5 load)

interpretation        per v0.4 §11 forbidden interpretations (carried verbatim in §6 below):
                      this OPENS the composite/certified-baseline question (separate prereg).
                      It is NOT certification, NOT a composition claim, NOT a capability claim,
                      NOT a mechanism claim. The empirical contrast with the C0 K=5 FAIL is
                      reported as data, not as a mechanism finding.
```

---

## 1. The §10 final branch (the substantive result)

```text
FINAL BRANCH: COMPONENT-ADMISSIBLE-UNDER-COMPETITION

§9 conditions (all six PASS):
  (i)   hop2 lower Wilson 95% > 0.75      0.9615 > 0.75   PASS  (k=96, n=96, rate=1.000)
  (ii)  dq C* count ≤ 19                  0 ≤ 19          PASS  (zero direct-recall events
                                                                  across all 96 items)
  (iii) hop1 lower Wilson 95% > 0.75      0.8313 > 0.75   PASS  (k=87, n=96, rate=0.906)
  (iv)  invalidated count < 10            0 < 10          PASS  (zero R6 firings)
  (v)   admissibility PASS all 96         true            PASS  (inspector C1–C9 96/96
                                                                  in real-run mode)
  (vi)  prompt-realization conformance    true            PASS  (checker 96/96 P1–P10 +
                                                                  §9(vi) gate)

clean_executable_construct: true     (= (ii) ∧ (iii) ∧ (iv) ∧ (v) ∧ (vi))
branch selector outcome:    clean_executable AND cond_i  →  COMPONENT-ADMISSIBLE-UNDER-COMPETITION

post-exclusion denominator: 96 (no exclusions; zero R6-invalidated items)
hop2 min_clearing_count:    81 (matches v0.4 §7 SE-verified figure)
hop1 min_clearing_count:    81 (matches v0.4 §E4 SE-verified figure)
```

**Composite context** (informational only; NOT a §9 condition; per v0.4 §11 interpreted only in light of hop2 admissibility):

```text
composite k/n:        80/96 = 0.833
composite Wilson 95%: [0.7463, 0.8947]
```

This is reported because the Manager required-return fields include "all artifact paths" and the composite scored JSONs exist; it is **NOT** a standalone certification claim per v0.4 §11 *"The composite result is NOT a standalone pass; interpreted only in light of hop2"* and *"hop2-clears is NOT certification and NOT a composition claim; it opens the composite question only."*

---

## 2. Required Manager-return fields

### Commit + push + clean-fetch

```text
step-6 inference + r6_log + analyzer commit   <to be recorded in §7 after push>
final remote HEAD                              <to be recorded in §7>
clean-fetch confirmation                       <to be recorded in §7>
```

### Scored output paths and hashes

```text
experiments/2026-06-18_v3-floor-check-run/scored/<item_NNN>/<context>.json
  96 items × 4 contexts = 384 files
  All per-item hashes recorded in updated manifest.json; representative:
    scored/item_001/composite.json (predicted i001_X1; not match)
    scored/item_001/hop1.json      (predicted i001_B1; MATCH)
    scored/item_001/hop2.json      (predicted i001_C1; MATCH)
    scored/item_001/direct_query.json (predicted i001_S1; not match)
```

### Locked auxiliary outputs (run_record + r6_log + analyzer)

```text
experiments/2026-06-18_v3-floor-check-run/run_record.json
  sha256 49128678e4384dc62197165b739439f2a598278ab74c8424648d0b5bb733dfe0
experiments/2026-06-18_v3-floor-check-run/r6_log.json
  sha256 935e386382d1cd61e0d568408de76629969b9d71db8358af20cfe74008f17471
experiments/2026-06-18_v3-floor-check-run/analyzer_decision.json
  sha256 6a34f6dc9687e04d0bc58b1595b4c6e9555a59e4bb606e40e9aa72ddd2c048c5
```

### Auxiliary execution artifacts (build-side scripts retained for audit)

```text
experiments/2026-06-18_v3-floor-check-run/run_step_6.py
  sha256 92514808d50b9a1985e904dbcb46ee41d5d85eff53061786998983231f660eb6
experiments/2026-06-18_v3-floor-check-run/build_r6_log.py
  sha256 b861a977907282a1d42bc7c9d1288e798e802ddca465ab8d5d433bc23e80cd17
experiments/2026-06-18_v3-floor-check-run/run_step_6.log
  sha256 9323945cbc888e7e3e85d76010196401460219eb0665cb5dd53b27605aa823e8
```

### Model / run profile (from run_record.json)

```text
model_name             Qwen/Qwen2.5-3B-Instruct
model_revision_sha     aa8e72537993ba99e69dfaafa59ed015b17504d1
                       (matches the program's locked snapshot referenced
                        throughout — same revision the prior Path A FP16
                        K=5 FAIL was run against)
precision              FP16 (mlx_lm default for non-quantized Qwen2.5)
decoding               greedy (temp=0.0 / argmax sampler)
max_new_tokens         24
execution_host         (recorded in run_record.json; M2 Max)
runtime
  python               3.13.3
  mlx_lm               0.31.3        (matches the v0.4 binding's mlx_lm 0.19.3 → 0.31.3
                                       verified-null statement)
  transformers         5.10.2
  torch                2.7.1
model_load_time_s      5.8
inference_time_s       303.1  (5 min 3 s)
n_items                96
n_contexts_per_item    4
n_prompts_total        384
timestamp_utc          (recorded in run_record.json)
operator               CS Engineer (Claude Code; M2 Max host)
```

### Confirmation 384 prompts were executed exactly once

```text
YES. run_record.json field n_prompts_total = 384.
     run_step_6.log shows progress 384/384 with one PASS per prompt (no retries,
     no recomputations, no parallel duplicate runs).
     Scored output dir has exactly 96 subdirs × 4 .json files = 384 (verified by
     `find scored -name '*.json' | wc -l` returning 384).
```

### Confirmation no prompt edits or regeneration occurred

```text
YES. run_record.json fields:
  prompts_consumed_as_committed:   true
  prompt_regeneration_occurred:    false
The realizer (v3_prompt_realizer.py, sha fb561fdc...) was NOT invoked from
the step-6 script. Prompts were read from experiments/2026-06-18_v3-floor-
check-run/prompts/ as committed bytes; each `<prompt>.txt` was opened with
`Path.read_text()` and passed verbatim to the chat template + model call.
Re-verified post-run: the 384 prompt files have unchanged sha256s against
the manifest (no edits during execution; checked via the analyzer's
clean-fetch path).
```

---

## 3. R6 invalidation log (build_r6_log.py methodology)

The R6 log was computed honestly from the scored outputs. Only the two invalidators that are **mechanically determinable** from the scored snapshot were fired:

```text
direct_recall    fires on item N iff scored[N]["direct_query"].match == True.
                 Fired count this run: 0/96   (model never produced C* under bridge withheld;
                                                consistent with the dq ceiling cond_ii)
constant_token   fires on item N iff all four contexts emit the SAME predicted token AND that
                 token is NOT equal to any of the four locked ground truths.
                 Fired count this run: 0/96   (no item exhibited uniform-wrong cross-query
                                                tokens)
```

The three other invalidators (`terminal_coincidence`, `controls_unavailable`, `interior_position`) were **NOT fired** by build_r6_log.py — they require diagnostic analysis beyond the scored-output snapshot alone (interior_position needs per-item layout-position evidence; controls_unavailable depends on per-item hop1/hop2 retrieval failure which is captured by §9 conditions iii/i directly; terminal_coincidence overlaps with admissibility already gated at the inspector C1 layer). This is recorded honestly in `build_r6_log.py` docstring.

Set-level cond (iv): `invalidated count ≤ 9` → 0 ≤ 9 → **PASS**.

---

## 4. Per-context aggregate (informational; per v0.4 §11 reported separately, not collapsed)

```text
context          k/n        rate     Wilson 95% lower    Wilson 95% upper    floor / rule       result
composite        80/96      0.833    0.7463              0.8947              N/A (informational; per v0.4 §11)
hop1             87/96      0.906    0.8313              0.9499              floor 0.75 strict  CLEARS
hop2             96/96      1.000    0.9615              1.0000              floor 0.75 strict  CLEARS
direct_query     0/96       0.000    n/a                 n/a                 ceiling 19/96 pt   PASSES (count = 0)
```

Reported separately. **Composite is NOT averaged with hop1/hop2; not interpreted as a standalone pass.** The composite-vs-hop2 contrast (0.833 vs 1.000) shows that even under V3's foreclose-all design, two-hop composition in the composite context loses some items the hop2-alone retrieval cleanly handles — that asymmetry is **data**, not a mechanism finding.

---

## 5. Empirical contrast (data point; NOT a mechanism claim)

For the record, in numbers only:

```text
construction           K     hop2-isolated retrieval     §10 outcome
C0 (existing)          1     76/96 = 0.792               (cliff edge; not a foreclose-all gate)
C0 (existing)          5     65/96 = 0.677               sub-floor — substrate-infeasibility evidence
                                                          per K-sweep cliff finding v0.2
V3 (this run)          5     96/96 = 1.000               clears 0.75 strict; component-admissible
```

Per v0.4 §11 forbidden interpretations:
- This data **does not** establish that V3's design choices CAUSED hop2 to clear (that's a mechanism claim; not authorized).
- This data **does not** establish that the model COMPOSED two-hop (composite is 0.833, not 1.0; and even at 1.0 hop2 alone is component admissibility, not composition).
- This data **does** open the door — under separately gated authorization — to a composite-certification prereg that could measure two-hop composition with hop2 admissibility now established as a precondition.

---

## 6. Forbidden interpretations (carried verbatim from v0.4 §11)

```text
- hop2-below-floor is NOT "V3 is a bad construction"; V3 is verified-conformant. It is a
  substrate finding (one-run evidence, §10), not an instrument defect.
- hop2-clears is NOT certification and NOT a composition claim; it opens the composite
  question only.
- The composite result is NOT a standalone pass; interpreted only in light of hop2.
- NO mechanism claims (traversal vs grab vs anchor not decidable here).
- Survival is not correctness: C* counts only if it is the RIGHT C* via the bridge,
  controls clearing, no invalidator.
- "Not ruled out" is not "established."
- A single clean failed run is evidence TOWARD substrate-infeasibility, not a final classification.
```

This run is the **mirror image** of the "single clean failed run" clause: a single clean passed run is COMPONENT-ADMISSIBILITY evidence — it OPENS the composite question, does NOT establish certification of any kind.

---

## 7. Commit + push + clean-fetch verification

To be appended after the commit lands.

---

## Non-authorizations (carried forward verbatim from the Manager memo + standing card)

```text
- compression / INT8 / INT4              blocked
- rerun                                  blocked (one run per locked spec)
- prompt edits                           blocked
- prompt regeneration                    blocked
- post-hoc slicing                       blocked
- floor adjustment                       blocked
- tooling edit after data                blocked  (the 4 §T tooling digests are unchanged
                                                    through this run — verified pre + post)
- Claim C                                blocked
- Paper B                                blocked
- certification claim                    blocked
- capability claim                       blocked
- mechanism claim                        blocked
- candidate selection, threshold values, certification evaluation, multi-model,
  Fork A reactivation, public benchmark packaging, artifact mutation               all carried per standing card

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc…) + tagged manuscript blob   never moved
- tier0-run/ directory                                                             sealed; no new files

The Path A FP16 K=5 FAIL remains closed.
```

---

## Routing posture after this return

```text
This run closes the V3 floor-check lifecycle that began with Senior's first floor-check
prereg draft (v0.1, 2026-06-18) and was iterated through:
  v0.1 → CS feasibility HOLD (E1–E5)
  v0.2 → intermediate
  v0.3 → CS feasibility HOLD (F1+F2+F3) + C5 claim-risk PASS
  v0.4 → CS final feasibility PASS-with-caveat + C5 confirm-transfer PASS
        + SE tooling PASS + TL approval + Manager by-name authorization
  Steps 1–5 → prep PASS
  Step 6 → executed COMPONENT-ADMISSIBLE-UNDER-COMPETITION
  Steps 7+8 → analyzer ran; this return

WHAT IS NOW OPEN (downstream of this result, but each its own separately-gated lane):
  - Composite-certification prereg (would test two-hop composition under V3, NOT yet drafted)
  - Multi-construction comparison (V3 vs other foreclose-all candidates) (not authorized)
  - Stress / compression rungs (would need their own pre-registration; NOT authorized)

WHAT IS NOT OPEN:
  - Any of the standing-card non-authorizations above
  - Certification of V3 (this run was component admissibility only)
  - Capability or mechanism claims of any kind
  - Claim C, Paper B
  - The K=5 FAIL itself (which stays closed; this run does not "reopen" it because V3 is a
    DIFFERENT construction, and the K=5 FAIL was specifically C0 at K=5)
```

---

— CS Engineer, 2026-06-18
