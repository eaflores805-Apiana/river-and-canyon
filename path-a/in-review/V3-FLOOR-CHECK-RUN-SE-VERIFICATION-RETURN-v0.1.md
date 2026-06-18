# V3 FLOOR-CHECK RUN — SE VERIFICATION RETURN

**To:** Team Lead **Cc:** CS Engineer, C5, Manager **From:** Senior Engineer **Re:** SE verification of the V3 floor-check run (CS step 6/7/8 return)
**E. A. Flores**, Apiana AI, Inc. — June 18, 2026 · *Verification only. Certifies nothing, authorizes nothing.*

## VERDICT: **PASS** — run independently verified from bytes; §10 branch **COMPONENT-ADMISSIBLE-UNDER-COMPETITION** confirmed.

I re-ran the analyzer on the committed scored outputs and obtained a **byte-identical decision** (`6a34f6dc…`); recomputed every §9 condition from the raw scored files; confirmed the result is real and honestly scored (not a vacuous perfect score); verified run integrity, the reported digests, the unchanged tooling, real-run mode, and the Manager by-name authorization. The bounding in §B is the important half of this return: a clean PASS here is **component-admissibility on one run**, not certification, composition, or capability.

## A. What I verified (from a fresh clone at HEAD `441eff42`)

**A1 — the result is real and honestly scored** (a perfect hop2 demands this check):

```text
- scored schema = {ground_truth, predicted, match}. I recomputed match := (ground_truth == predicted)
  for all 96×3 and found 0 disagreements with the stored match field — the scoring does not lie.
- hop2: 96/96. Predictions are 96 DISTINCT, item-specific tokens (i001_C1, i002_C1, …) — the model
  returned the correct unique C* per item, NOT a lucky constant. Not vacuous.
- hop1: 87/96 (varied; NOT perfect — so hop2's perfection is a real contrast, not a scoring artifact).
- direct_query: 0/96 — with the bridge fact withheld, the model produced OTHER tokens (i001_S1, i002_X1…),
  NEVER C*. So no direct-recall shortcut explains hop2.
- the hop2 prompt carries the full competitive load (same 22-line fact body: D=5 competitors + K=5 decoys),
  so 96/96 is genuinely hop2 UNDER COMPETITION, not a stripped-down probe.
```

**A2 — all six §9 conditions, independently recomputed:**

```text
(i)   hop2  96/96 = 1.000, Wilson95 lower 0.9615 > 0.75   CLEARS
(ii)  dq C* count 0  ≤ 19                                  PASS
(iii) hop1  87/96 = 0.906, Wilson95 lower 0.8313 > 0.75    CLEARS
(iv)  invalidated 0  < 10   (r6_log.json: 0 items with invalidators)   PASS
(v)   admissibility 96/96 PASS, real-run   (each C9_manager_lock_binding carries "mode":"real-run"
        against the Manager-locked values k=5,D=5,p=5,m_min=10,n=96,margin=0.25; F=0.20)   PASS
(vi)  prompt-realization conformance 96/96 PASS   PASS
```

**A3 — decision reproduces; digests match; tooling unchanged:**

```text
- re-ran the analyzer on the run's scored dir -> final_branch COMPONENT-ADMISSIBLE-UNDER-COMPETITION,
  decision JSON BYTE-IDENTICAL to the committed analyzer_decision.json (both 6a34f6dc…, = CS-reported)
- run_record.json, r6_log.json, analyzer_decision.json digests all MATCH CS-reported
- the four §T tooling digests are UNCHANGED pre+post (the "no tooling edit after data" attestation holds)
```

**A4 — run integrity + authorization:**

```text
- model: Qwen/Qwen2.5-3B-Instruct, revision aa8e7253… (program's locked snapshot), FP16, greedy (temp 0)
- 384 prompts; prompts_consumed_as_committed = true; prompt_regeneration_occurred = false (executed once)
- Manager BY-NAME authorization present and genuine: MANAGER-AUTHORIZATION-EXECUTE-V3-FLOOR-CHECK, AUTHORIZED
  for prereg v0.4, explicitly "not a composite certification run"
- CS final feasibility review: PASS, carrying the MAX_DELTA zero-margin caveat I raised
```

## B. What this result IS and is NOT (the bounding — read before interpreting)

```text
WHAT IT IS:
  On V3 (the foreclose-all, same-depth-competitor construction), with D=5 competitors present in the prompt,
  the model retrieved the correct item-specific C* in the hop2-isolated context 96/96, with no direct-recall
  shortcut (dq 0/96), hop1 also clearing, and a clean construct (admissibility + prompt-conformance + 0
  invalidated). => the component operation (hop2) is ADMISSIBLE UNDER COMPETITION on V3.

WHAT IT IS NOT (per v0.4 §11, verbatim discipline):
  - NOT certification. NOT a composition claim. NOT a capability claim.
  - hop2-clears means ONLY that second-hop retrieval is reliable enough under V3 competition to make a
    later COMPOSITE test interpretable. It OPENS the composite/certified-baseline question (separate prereg).
  - ONE clean PASSED run = component-admissibility — the exact mirror of v0.4 §10's "one clean FAILED run =
    evidence toward substrate-infeasibility." It does NOT establish certification of any kind.
  - The COMPOSITE result (80/96 = 0.833, Wilson95 [0.7463, 0.8947]) is INFORMATIONAL ONLY, NOT a standalone
    pass, interpreted only in light of hop2. Even though 0.833 exceeds the 0.45 composite threshold, §11
    forbids reading it as "the model composes"; certification is a separate, pre-registered question.
  - NO mechanism claim. The V3-vs-C0 asymmetry (below) is DATA; WHY is not decidable from this run.
  - The C0 K=5 FAIL stays CLOSED. V3 ≠ C0; this run does not reopen, overturn, or bear on that FAIL.
```

## C. Empirical contrast (data, not mechanism)

```text
C0 at K=5:  hop2-isolated 65/96 = 0.677  (sub-floor — the K-sweep cliff finding, SE-verified earlier)
V3 at K=5:  hop2-isolated 96/96 = 1.000  (clears the 0.75 strict floor — this run, SE-verified)
Recorded as data. The magnitude is large; the cause is NOT a claim this run can make.
```

## D. Instrument observation (measured, not overclaimed)

```text
This is the FIRST time the composition gate has CLEARED on a multi-hop construction. The standing concern was
"a gate that never opens is observationally identical to a miscalibrated gate." With C0 FAILING the gate
(hop2 sub-floor) and V3 CLEARING it (hop2 clears), the gate now demonstrably DISCRIMINATES between
constructions — an instrument-validity gain. Bounded honestly: one clearing shows the gate CAN open on a
clean construction; it does not, by itself, establish full calibration, and it establishes nothing about
composition. It removes the "always-fails" failure mode; it does not certify anything.

Also noted as DATA for a future bounded look (not a claim): hop2-isolated (1.000) exceeds the composite
(0.833) — the model retrieves the second hop in isolation more reliably than it completes the full two-hop
composite. That gap is exactly the composite/certification question, which is a separate prereg.
```

## E. Zero-margin MAX_DELTA (carry-forward of my tooling caveat)

```text
The ≤8-character prompt-length gate passed 96/96 (zero margin, as flagged). CS final feasibility carried the
caveat. My lock-scope note stands for FUTURE constructions: the ≤8 tolerance is calibrated to the current
6-7 char prefixed-token scheme; any token/construction change re-opens the delta check. Not a defect in this run.
```

## F. What's open vs blocked

```text
OPEN (each separately gated; NOT authorized by this run or this verification):
  - composite-certification prereg (V3 two-hop composition; hop2-admissibility now a precondition)
  - multi-construction comparison
  - stress / compression rungs (their own pre-registration; the program remains pre-stress)

BLOCKED (standing): compression / INT8 / INT4 / rerun / prompt edits / regeneration / slicing / floor
  adjustment / tooling edit / Claim C / Paper B / certification / capability / mechanism. K=5 FAIL closed.
```

## G. Boundary

```text
- Verification only. This return certifies nothing and authorizes nothing.
- The Path A FP16 K=5 FAIL remains closed and untouched. SE verifies; SE authorizes nothing.
- The result is component-admissibility on one run; certification is a separate, pre-registered question.
```

— Senior Engineer (run verification; PASS — component-admissibility confirmed, bounded)
