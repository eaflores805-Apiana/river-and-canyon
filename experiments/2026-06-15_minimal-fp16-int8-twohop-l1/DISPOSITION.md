# DISPOSITION — MINIMAL-FP16-INT8-TWOHOP-L1-v0.1

**Verdict: INCONCLUSIVE.**
**Reason: FP16-BASELINE GATE failed (§6 pre-declared rule). The matched-pair difference is therefore uninterpretable on the larger question, but a clean factual observation is reportable separately (see §3 below).**

This disposition is written **after** running both conditions per the locked
preregistration, applying the §6 gate **first**, and following the §8 forbidden-
interpretations list. Nothing in this disposition was decided after looking at INT8.

---

## 1. Headline numbers (factual; reported as-is)

```text
n                                    = 8 items (twohop_l1_c03_i01..i08)
Decoding                             = greedy, temp=0.0, max_tokens=16
Conditions                           = FP16 (HF cache) + INT8 (tier0-run MLX)

FP16  hop1=0/8   hop2=8/8   composite=1/8   total=9/24
INT8  hop1=0/8   hop2=8/8   composite=1/8   total=9/24

Matched-pair difference              = 0 / 24 items disagree
Raw-output byte-identity (FP16↔INT8) = 24 / 24 generations identical
```

## 2. FP16-BASELINE GATE — outcome: **CONTAMINATED → INCONCLUSIVE**

The preregistration §6 declared **before any run** that the FP16 baseline
must be inspected for the Claim-B position/anchor shortcut **before** any
INT8 interpretation. Inspection of the FP16 raw E3 found these signatures:

```text
(a) hop1 = 0 / 8 correct.
    The first-hop query "{anchor} links to what?" expects the B token.
    The model returns NULL 6/8 times and, on 2 items (i01, i06), returns
    the COMPOSITE (C) token directly — skipping the first hop entirely.
    A model that cannot do the single-hop A→B retrieval cannot be doing
    genuine two-hop A→B→C composition.

(b) The one composite-correct (i06) is NOT chain-following.
    For item i06, the model emitted "YHIJZ" for ALL THREE query types
    (hop1, hop2, composite). The same token appears regardless of what
    is asked. That is pattern-matching the hop2 fact ("ZBUTS maps to
    YHIJZ") and emitting its tail when the prompt's anchor is anywhere
    in the target chain — not chain-traversal. This is exactly the
    "composite-correct that on inspection is position-reading not
    chain-following" signature §6 names.

(c) The 8 hop2 "corrects" are legitimate but not load-bearing.
    The hop2 query "{anchor} maps to what?" is a single-fact lookup
    against one fact ("B maps to C") in the context. 8/8 correctness
    here measures single-fact retrieval, NOT chain composition. These
    correct answers are not shortcut-contaminated; they are also not
    evidence of two-hop reasoning.
```

Per §6, the gate disposition is: **FP16 baseline contaminated; matched-pair
difference is UNINTERPRETABLE for the larger compositional question.**

## 3. Factual observation worth recording (separate from the verdict)

```text
On these 8 items, with greedy decoding (temp=0.0, max_tokens=16), the INT8
MLX-quantized Qwen2.5-3B-Instruct produced raw outputs BYTE-IDENTICAL to the
FP16 baseline for all 24 generations.

That observation is genuinely informative about INT8≡FP16 behavior at this
scale, this task, this decoding setting — and only that. It is NOT a claim
about compression robustness in any larger sense (§7, §8).
```

## 4. What this run does NOT mean (carried verbatim from §8)

```text
This result is NOT:
  - Claim C progress
  - Paper B activation
  - a general compression-robustness claim
  - a certified-baseline claim — the baseline IS contaminated by this run's
    own gate
  - the task family is viable
  - the model "passed" / capability established / "not shortcut-driven"
  - a product- or funder-facing result
  - Lane 4 official compression evidence (this is Tier-1 exploratory)
```

## 5. What the next move could be (NOT authorized here)

Two paths a future Manager decision could take, neither authorized by this
disposition:

```text
- Tighten the baseline: revise the prompt / query phrasing / item selection so
  the FP16 baseline can do single-hop retrieval reliably (otherwise INT8 vs FP16
  comparisons remain uninterpretable on the chain-composition question).
- Treat INT8≡FP16 byte-identity as a SEPARATE inquiry, scoped narrowly: under
  what conditions does INT8 stop matching FP16 (larger n; different tasks;
  non-greedy decoding)? A finding-track-style scope, with strict claim limits.

Both would need new pre-registration; neither is implied here.
```

## 6. Boundaries held (§7-§8)

```text
- No Claim C / Paper B / general compression / certified-baseline / task-family /
  "passed" / product-funder claim made.
- Tier-1 exploratory; NOT Lane 4 unless Manager separately classifies.
- Raw E3 retained for both conditions (fp16_raw_outputs.json, int8_raw_outputs.json).
- Sealed bytes 4-of-4 byte-identical; sealed tree not touched.
- Authority: TL ACTION 2026-06-14 + Manager "authorize MINIMAL-FP16-INT8-TWOHOP-L1-v0.1".
```

— CS Engineer, 2026-06-14 (run timestamp UTC 2026-06-15T06:52)
