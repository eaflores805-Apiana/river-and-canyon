# V3 FLOOR-CHECK TOOLING VERIFICATION — SE RETURN

**To:** Team Lead **Cc:** CS Engineer, C5, Manager **From:** Senior Engineer **Re:** TL ACTION 2026-06-18 (Verify V3 Floor-Check Tooling)
**E. A. Flores**, Apiana AI, Inc. — June 18, 2026 · *Verification only (YELLOW). No run. Certifies nothing.*

## VERDICT: **PASS** (tooling contract met) — with the MAX_DELTA=8 zero-margin **surfaced for TL** (§watch)

All four tools implement the v0.4 §T contract, are deterministic, enforce the correct thresholds and branches, and execute no model. The one item requiring a TL judgment is the zero-margin prompt-length result (§watch): it is **stable and reflects the structural minimum**, but it has **no headroom** and the ≤8 gate is a **drift-tripwire, not an independent length-comparability validation**. I recommend proceeding to CS feasibility final review **provided the lock records that the ≤8 tolerance is bound to the current token-width scheme** (§watch).

## 1. Files inspected + hashes recomputed (SE, clone at HEAD `df919ab`)

```text
v3_floor_check_analyzer.py         0f5a3f7438a6936f…   matches CS-reported  ✓
v3_prompt_realizer.py              fb561fdc526115da…   matches CS-reported  ✓
v3_prompt_conformance_checker.py   b8afa3f89dd7f375…   matches CS-reported  ✓
v3_neutral_token_pool.md           bc2020c2c4e1293f…   matches CS-reported  ✓
```

## 2. Commands run

```text
git fetch && checkout origin/main (HEAD df919ab)
python3 v3_prompt_realizer.py --items-dir items --out-dir … --summary-path …      (twice — determinism)
python3 v3_prompt_conformance_checker.py --items-dir items --prompts-dir … …       (twice — determinism)
python3 v3_floor_check_analyzer.py --scored-dir … --r6-log … --admissibility … --prompt-conformance … --output …
   (twice on a fixed synthetic input — determinism; plus 3 synthetic N=96 cases — branch tests)
import of analyzer.wilson_ci for the threshold tests; sha256sum; diff
```

## 3. Task-by-task

**(1) Each tool implements the v0.4 §T contract — VERIFIED** (paths, intent, inputs, outputs, deterministic behavior all match §T for analyzer / realizer / checker / neutral-pool).

**(2) Analyzer — VERIFIED** (by reading + synthetic-input execution):

```text
- computes hop1/hop2 retrieval rates + Wilson 95% CIs                                     ✓
- reports post-exclusion denominators (n_included) + min-clearing-count per denominator   ✓
- direct-query rule: count <= 19 passes, >= 20 fails (point count)                          ✓
- invalidated rule: n_excluded < 10 tolerated (>=10 -> construct-fail)                       ✓
- emits §9/§10 final_branch                                                                  ✓
- no model / network imports                                                                 ✓
BRANCH TESTS (synthetic N=96):
  hop2 85/96, dq 5, clean      -> COMPONENT-ADMISSIBLE-UNDER-COMPETITION              (correct)
  hop2 70/96, dq 5, clean      -> ONE-RUN-EVIDENCE-TOWARD-SUBSTRATE-INFEASIBILITY     (correct)
  hop2 85/96, dq 25            -> CONSTRUCT-FAIL                                       (correct)
  (FINAL substrate-infeasibility correctly OUT OF SCOPE for a single run — matches v0.4 §10.)
```

**(3) Prompt realizer — VERIFIED**: renders four prompts per item (per-item subdir: composite/hop1/hop2/direct_query); consumes the neutral pool; **deterministic (two runs byte-identical)**; MAX_DELTA=8 character-count gate present; does not generate N=96 or execute prompts (no model imports).

**(4) Prompt conformance checker — VERIFIED**: implements P1–P9 — including **no C\* leakage into hop1 (P4) or direct_query (P5)**, the substituted filler reveals neither B nor C\* (P6), same-template-class invariant (P2), and **character-count delta ≤ 8 (P9)**; **deterministic (two runs byte-identical)**; passes on the demo (all_pass=True, 8/8); no model imports.

**(5) Neutral-token pool — VERIFIED**: a fixed, auditable markdown resource; documents the 6–7-char prefixed role-token width scheme and the filler-width parity rationale; consumed by the realizer (or, per §T option B, the embedded defaults are bound by the realizer digest). Bound either way.

**(6) Determinism — VERIFIED**: realizer prompts byte-identical across two runs; checker output byte-identical; analyzer decision JSON byte-identical on fixed input.

**(7) Threshold behavior — VERIFIED** (analyzer's own Wilson, z=1.96):

```text
80/96  Wilson lower 0.7463  -> does NOT clear 0.75   ✓
81/96  Wilson lower 0.7581  -> clears 0.75            ✓ (matches the prereg 81/96 note)
N=8 smoke: even 8/8 -> Wilson lower 0.6756 -> does NOT clear 0.75  ✓ (strict floor correctly fails small N)
post-exclusion min counts computed (N=95->80, N=90->76, N=88->74)  ✓
```

## 4. Import / model-execution check

```text
No torch / mlx / transformers / openai / anthropic / requests / urllib / http in ANY of the four artifacts.
The analyzer and checker are pure computation; the realizer is pure string rendering. None executes a model
or a prompt. (The analyzer SCORES already-produced outputs; it does not produce them.)
```

## 5. MAX_DELTA = 8 assessment (the watch item)

**Fact (from bytes):** every demo item produces `char_delta = exactly 8` — composite 653, hop1 645, hop2 646, direct_query 651 — **identical across all 8 items** (the tokens are width-controlled, so the counts do not vary by seed). The gate ≤8 passes with **zero margin**.

**Cause (verified):** the composite query references **both** relation tokens (`{r1}.{r2}`, where r1/r2 are ~7-char prefixed tokens like `i001_r1`) while the single-hop queries reference **one**. The irreducible difference ≈ one relation-token width + 1 (dot) ≈ 8 characters. The fact bodies are identical across composite/hop1/hop2; direct_query substitutes one length-comparable filler triple (2-char delta on that line, within the 8 set by the query). The neutral-pool doc states the pool was sized "to meet the MAX_DELTA = 8 constraint."

**Assessment:**

```text
- 8 ~= the STRUCTURAL MINIMUM for a genuine two-relation-vs-one-relation query contrast under the current
  6-7 char prefixed-token scheme. It is STABLE (not random per-item), and the realizer is NOT padding-to-
  match (it leaves the natural difference rather than inflating the shorter prompts). The tolerance equals
  the structural floor.

- CONCERN (a) — ZERO HEADROOM / BRITTLENESS. The gate passes at exactly the boundary, so it is tightly bound
  to the current token-width scheme (6-7 char prefix; N<=999). Any change that lengthens relation tokens
  (e.g., a 4-digit prefix at N>=1000, or wider role suffixes) would push the composite-vs-hop delta > 8 and
  FAIL the gate. RECOMMENDATION: the lock should explicitly record that the <=8 tolerance is calibrated to
  THIS token-width scheme, and that any construction/token change re-opens the delta check (and possibly the
  tolerance). This is a lock-scope caveat, not a defect.

- CONCERN (b) — LIMITED DISCRIMINATING POWER. Because 8 ~= the structural minimum, the <=8 gate CANNOT fail
  for the inherent composite-vs-hop asymmetry; it can only catch ADDED, avoidable length differences (e.g.,
  realizer verbosity drift). So it is a DRIFT-TRIPWIRE, not an independent validation of length-comparability.
  The contexts are length-comparable by the realizer's structural DESIGN, not by passing this gate. TL should
  read the gate as guarding against drift from that design, not as proving the design.

- SUBSTANTIVELY, the length-matching GOAL is WELL-SERVED: 645-653 is a ~1.2% spread on ~650 characters — the
  four contexts are tightly length-comparable, so prompt length is not a meaningful confound. The zero-margin
  is a property of the GATE CALIBRATION, not a sign the contexts are poorly matched.
```

**Disposition on the watch item:** per TL, I did **not** change the tolerance. I assess the zero-margin as **acceptable to proceed**, *conditioned on* the lock recording concern (a) (the tolerance is bound to the current token scheme; construction/token changes re-open the delta). The accept-vs-mitigate judgment is **TL's** — I am surfacing the property and its two concerns, not deciding it.

## 6. Recommendation

**Recommend CS feasibility final review next**, with the §5 lock-scope caveat carried forward. The tooling is contract-correct, deterministic, threshold-correct, and model-free; the only open judgment is the zero-margin (a TL call), and it does not block CS feasibility re-review.

## 7. Boundary

```text
- Verification only (YELLOW). No N=96 materialization, no prompt generation for execution, no model run, no
  floor-check run, no compression, no Claim C, no Paper B, no certification/capability/mechanism claim.
- The Path A FP16 K=5 FAIL remains closed and untouched. SE verifies; SE authorizes nothing.
```

— Senior Engineer (tooling verification; PASS with zero-margin surfaced)
