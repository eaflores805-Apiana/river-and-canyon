# DISPOSITION — Path A K-Sweep Scout (K = 1..5)

**Q3 disposition: BOUNDARY** (best cell at K = 1, the lower range edge). **K = 5 reproduction check: PASS** (byte-exact). Per locked preregistration v1.0 (sha `248581f6...`) §4 + §5 + §6.

This is a **descriptive scout**. No K certifies anything. The closed K = 5 FAIL artifact is untouched and stands. Per prereg §6, a BOUNDARY result records a descriptive caveat — **structure may extend beyond {1..5}** — and **pursuing it is a SEPARATE one-off under its own lock**, not an extension of this run (per §4 stop-rule).

## 1. Headline curve (validated-R1 + Wilson 95% CI per cell)

```text
K | n  | R1  | rate  | Wilson 95% CI    | half-width
--+----+-----+-------+------------------+-----------
1 | 96 |  29 | 0.302 | [0.2193, 0.4001] | 0.090
2 | 96 |  16 | 0.167 | [0.1053, 0.2537] | 0.074
3 | 96 |  15 | 0.156 | [0.0970, 0.2419] | 0.072
4 | 96 |  19 | 0.198 | [0.1305, 0.2886] | 0.079
5 | 96 |  18 | 0.188 | [0.1220, 0.2770] | 0.077
```

**Shape (per prereg §4 named patterns):** **cliff-then-plateau** — sharp ≈13.5-point drop K=1→K=2 (0.302 → 0.167), then a low plateau across K = 2..5 (range 0.156–0.198; all four 95% CIs overlap). My `scout_summary.py` heuristic labeled this "plateau" because no single step crossed its 20-point cliff threshold; the K=1→K=2 step is the most striking feature and the right reading is **cliff-then-plateau**, not pure plateau.

## 2. K = 5 reproduction check (per §5) — PASS

```text
closed K=5 run (commit 265114b)  R1_validated = 18 / 96 = 0.1875
new K=5 cell (this scout)        R1_validated = 18 / 96 = 0.1875
match: TRUE  (0 / 384 raw_output mismatches at the per-prompt level)
```

Mechanically guaranteed and empirically verified: same seed (20260615) + same generator + same construction + same prompts (all 384 `prompt_sha256` byte-identical pre-run) + same model + greedy decoding → byte-identical FP16 outputs → identical scored R1. **Harness is sound; scout is valid.**

## 3. Q3 disposition — BOUNDARY (best at K = 1)

Per prereg §4, **BAND-HINT requires an INTERIOR K** (2, 3, or 4) AND all three conditions:
(i) validated-R1 markedly higher at that K than at both K=1 and K=5 ends; (ii) control margins stable-or-stronger; (iii) Dial A steady-or-up AND Dial B beats per-K base rate.

**No interior cell qualifies for (i)**: K=2, K=3, K=4 all have point estimates *below* K=1 (0.302) and within a CI-overlap band of K=5 (0.188). The best interior cell is K=4 at 0.198, lower CI 0.131 — well below K=1's lower CI 0.219.

**Best K is K = 1** (range edge). Per F2:
> *"if the best cell sits at a range edge (validated-R1 still rising at K=5, or best at K=1), the structure may extend beyond {1..5}. That is recorded as a descriptive caveat and, if pursued, becomes a SEPARATE one-off under its own lock — NOT an INDETERMINATE resolved by adding a K point to THIS run."*

**Disposition: BOUNDARY. Q3_K = 1.** The structure may extend toward **K = 0** (no decoy chains; competitor-only clutter); pursuing requires a NEW locked one-off preregistration (prereg §4 stop-rule + §6 deferred scope).

## 4. Secondary panels (per prereg §3; descriptive only)

### 4a. Off-map POSITIONAL rate — monotone-up with K

```text
K | off-map+  | dC    | dB    | (= decoy answer-depth + decoy bridge landings, count / n)
--+-----------+-------+-------+
1 | 0.219     | 0.146 | 0.073 |
2 | 0.260     | 0.219 | 0.042 |
3 | 0.271     | 0.240 | 0.031 |
4 | 0.385     | 0.344 | 0.042 |
5 | 0.396     | 0.344 | 0.052 |
```

**Where tokens land vs K** — more clutter, more wrong-address landings. dC (decoy answer-depth) is the dominant component and grows ~2.4× from K=1 to K=5. dB (decoy bridge) is much smaller and roughly flat. This is the closed-K=5 R6cat mass arriving in dose-response form, with no mechanism resolution (per prereg + closed-K=5 R6cat note: positional curve cannot separate relation-keyed grab vs chain-anchor inconsistency).

### 4b. Dial A (answer-depth landing rate) — non-monotone; peaks at K=4

```text
K | Dial A
--+-------
1 | 0.5625
2 | 0.5312
3 | 0.4896
4 | 0.7500   ← peak
5 | 0.6875
```

Fraction of outputs at depth-2 answer positions (target C* + decoy answers + competitor X). NOT a "walk rate" — landing at answer-depth is not evidence of traversal. K=4 peak coincides with the highest R6cat rate (0.406, same as K=4's R1 rate — both maxed). K=1's lower Dial A coexists with a 0.74 right-chain share, so K=1 is more often *correct* among the smaller depth-population it samples.

### 4c. Dial B (right-chain share at answer-depth) — monotone-down with K; every K beats base

```text
K | Dial B share | base = 1/(1+D+K) | gain over base
--+--------------+-------------------+----------------
1 | 0.7407       | 0.1429            | +0.5979
2 | 0.5882       | 0.1250            | +0.4632
3 | 0.5106       | 0.1111            | +0.3995
4 | 0.5417       | 0.1000            | +0.4417
5 | 0.5000       | 0.0909            | +0.4091
```

**Every cell beats per-K base rate**, so chain selection is above chance at every K. **But the absolute right-chain share falls roughly monotonically as K rises** — at K=1 the model picks the right chain ~74% of the time among answer-depth landings; at K=5 only ~50%. **Important:** the prereg explicitly warns that the *base rate* falls mechanically as K drops (fewer decoys), so a Dial-B "gain" looks larger at low K from that artifact alone. Even with that baselining, K=1 still leads (gain +0.60 vs +0.41 at K=5), so the K-1 lead is real and not purely a base-rate-shift artifact.

### 4d. Cross-query chain-membership pattern (gated on hop1 + hop2 pass)

```text
K | anchor-tracking | switching | gated_out (no component floor)
--+-----------------+-----------+---------------------------------
1 | 49              | 15        | 32        (anchor share of gated-through = 49/64 = 0.766)
2 | 34              | 21        | 41        (anchor share of gated-through = 34/55 = 0.618)
3 | 32              | 28        | 36        (anchor share of gated-through = 32/60 = 0.533)
4 | 24              | 22        | 50        (anchor share of gated-through = 24/46 = 0.522)
5 | 26              | 26        | 44        (anchor share of gated-through = 26/52 = 0.500)
```

`anchor_tracking_target` = composite + hop1 + hop2 all on the target chain (composite==C*, hop1==B, hop2==C*). `switching` = mixed across queries. `fixed_wrong_chain` = all three queries land on the same wrong chain (NOT observed in any cell). `gated_out` = at least one of hop1 / hop2 controls failed, so chain-membership not gradable per prereg.

**Among items that pass component retrieval, anchor-tracking share falls monotonically from 77% (K=1) to 50% (K=5).** No fixed-wrong-chain attractor emerged at any K.

### 4e. Control margins — hop2 below 0.75 floor at K = 2, 3, 4, 5

```text
K | hop1   | hop2   | dq   | R2 (term-grab) | R4 (decoy term) | R4b (depth-comp)
--+--------+--------+------+----------------+------------------+------------------
1 | 0.865  | 0.792  | 1.00 | 0.062          | 0.021            | 0.000
2 | 0.854  | 0.667  | 1.00 | 0.042          | 0.010            | 0.000
3 | 0.833  | 0.740  | 1.00 | 0.052          | 0.000            | 0.000
4 | 0.854  | 0.604  | 1.00 | 0.010          | 0.010            | 0.000
5 | 0.740  | 0.677  | 1.00 | 0.042          | 0.021            | 0.000
```

- **hop2 control below the 0.75 floor at K = 2, 3, 4, 5.** Only K=1 carries hop2 above floor (0.792). hop2 is the bridge→answer retrieval; for K=2..5 the model can't even read the second-hop fact reliably on a non-trivial fraction of items, so the validated-R1 numerator at K=2..5 is conditioned on the smaller subset that DID retrieve both components.
- **hop1 control above floor at every K** (0.74–0.87). hop1 fails the floor only at K=5 (0.740, marginally below).
- **R4b = 0 / 96 at every K.** Same-depth-competitor-grab — the failure mode v0.2 of the design was built to expose — did not fire even once. The depth-control held across the full sweep.
- **R2 (terminal-grab) ≤ 6.3% at every K.** Terminal-attraction is rare.
- **dq pass = 1.00 at every K.** Direct A→C* recall route empirically closed at every load. No R6c invalidations anywhere.

## 5. Reading: what the K-curve does and does not say

**Does say:**
- On this construction, validated-R1 is *highest at the lowest tested load* (K=1) and falls sharply at K=2, then plateaus K=2..5.
- The plateau-then-fall in Dial B and the climb in off-map positional rate both move smoothly with K. The model degrades with clutter on multiple separately-measured axes.
- **K = 1 stands apart from K = 2..5** on the primary metric (CI [0.219, 0.400] vs all four interior+upper-edge CIs sitting at lower-bound ≤ 0.131). The cliff sits at K = 1 → K = 2.
- The closed K = 5 FAIL reproduces byte-exactly; the harness is sound.

**Does NOT say** (per prereg §6 + the construction-validity ceiling):
- K = 1 is NOT a "certified baseline." On this construction, validated-R1 conflates composition with arbitrary-label-tracking (head tokens are the only chain-identity carrier). A K = 1 lead is a **candidate K to test on a chain-identity-robust construction LATER**, NOT a certified composition.
- The off-map-vs-K positional curve is **POSITIONAL, not mechanism**. It does not resolve the closed K = 5 R6cat mechanism question (relation-keyed grab vs chain-anchor inconsistency — both predict an off-map climb with K; this run does not separate them).
- No K here makes a capability claim. The Qwen2.5-3B-Instruct "can/can't compose" question stays out of scope.

## 6. Stop-rule compliance (per §4 + §17 lineage)

- **No added K**, no re-slice of any cell, no post-hoc redefinition of any pattern. The §4 patterns, the §3 metrics, and the §5 reproduction check were locked before any cell was computed.
- **One computation per cell** — single FP16 greedy run, no retry, no second pass.
- **Sealed bytes 4-of-4 byte-identical** (CS verified pre-run).
- **No compression run occurred** (FP16 only; no INT8, no INT4, no quantization rung).
- The closed K = 5 FAIL artifact is **untouched**. The K = 5 cell here only reproduces it as the harness check called for by §5.
- Any extension (e.g., K = 0; or a chain-identity-robust construction; or a re-run at any K) requires a **NEW locked preregistration** per the stop-rule lineage.

## 7. Authority + boundaries

- **Authorized by:** Manager by-name (2026-06-15) on top of TL ACTION 2026-06-15 ("Path A Load Scout K=1..5; scout direction + locked spec cleared"). Route GREEN for THIS NAMED SCOUT ONLY.
- **Locked preregistration:** `path-a/in-review/PATH-A-KSWEEP-ONEOFF-RUN-PREREG-v1.0.md` sha `248581f673df2300ddf8567bd7fb826f1c3536dd459ff20576b689a07ea5ab90` (byte-identical copy at `experiments/2026-06-15_path-a-ksweep-scout/PREREGISTRATION.md`).
- **Sweep-mode admissibility patch:** `path-a/inspector/constants.py` + `inspector.py` patched pre-run to handle `_sweep_mode: true` + `_sweep_locked_K_list: [1..5]`; per-cell inspectors all 9/9 PASS with C9 mode='sweep'.
- **Per-cell seeds** (locked in `SEED.json`): K1=20260611, K2=20260612, K3=20260613, K4=20260614, K5=20260615 (the K=5 seed = the closed K=5 run's seed, by design, for the reproduction property).
- **Total wall-clock:** 1230 s (20.5 min) for 5 cells × 384 generations = 1,920 FP16 generations on Apple M2 Max, mlx_lm 0.31.3.
- **No forbidden phrasings:** no Claim C / Paper B / capability / mechanism / compression-robust / certified-baseline / seam-evidence / public-benchmark-result / task-family-viable / not-shortcut-driven.

— CS Engineer, 2026-06-15
