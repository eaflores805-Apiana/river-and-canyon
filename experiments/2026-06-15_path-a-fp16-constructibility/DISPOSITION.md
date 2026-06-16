# DISPOSITION — Path A FP16 Constructibility Run

**Outcome: FAIL** (per locked preregistration §14 MECE decision rule; dominant-signature branch).

This disposition is produced after the authorized Manager-by-name FP16 run completed and the locked Wilson 95% CI + decision rule were applied. Nothing in this disposition modifies the preregistration; per §17 stop-rule, no post-hoc change to construction / gate / scoring / invalidators / floor / threshold / dominance threshold / analysis unit.

## 1. Headline numbers

```text
n_items                          : 96   (locked Manager value)
n_generations                    : 384  (96 items × 4 contexts)

composite-query category breakdown (n=96):
  R1   (correct-composition cand.):  33   rate 0.3438
  R2   (target-terminal-grab)     :   4   rate 0.0417
  R3   (stopped-short)            :  11   rate 0.1146
  R4   (decoy-terminal-grab)      :   2   rate 0.0208
  R4b  (depth-competitor-grab)    :   0   rate 0.0000
  R5   (abstain)                  :   8   rate 0.0833
  R6cat (other)                   :  38   rate 0.3958

control pass rates:
  hop1                            : 0.740
  hop2                            : 0.677
  direct_query                    : 1.000

R1 candidates                    : 33
R1 validated (after R6 invalidators + R7 controls): 18
R1 validated rate                : 18 / 96 = 0.1875

Wilson 95% CI (two-sided):
  lower                          : 0.1220
  upper                          : 0.2770
  half-width                     : 0.0775
```

## 2. Decision rule application (per §14)

The MECE outcome rule:

```text
CERTIFY      lower CI > 0.45  AND  no dominant failure signature
FAIL         upper CI < 0.20  OR   any dominant failure signature
INCONCLUSIVE otherwise
```

**Result:** Wilson 95% CI = `[0.1220, 0.2770]`. Upper bound 0.2770 ≥ 0.20 and lower bound 0.1220 ≤ 0.45 — the CI alone would map to INCONCLUSIVE. **But three dominant failure signatures fire**, and the dominant-signature clause supersedes:

```text
control_floor_failure_hop1               (pass-rate 0.740 < 0.75 threshold)
control_floor_failure_hop2               (pass-rate 0.677 < 0.75 threshold)
other_rate_ceiling_breach_R6cat          (rate 0.3958  > 0.10 ceiling)
```

**OUTCOME: FAIL** via the dominant-signature branch.

## 3. Diagnoses (per §15 failure signatures)

### Control-floor failure (hop1 + hop2)

Per the prereg (definition v0.4 §11): "control-floor failure (controls not met → missing-fact, not composition)." The construction's per-item hop1 control fired correctly: the model returned the bridge B from the r1(A) query on only 71/96 items (74.0%); for hop2, it returned C* from r2(B) on only 65/96 items (67.7%). Both fall below the 0.75 control-floor threshold.

**What this means:** on a non-trivial fraction of items, the model could not even retrieve the BRIDGE FACT from a single-fact query (hop1) or the SECOND-HOP FACT given the bridge directly (hop2). Without component retrievability, composition cannot be credibly tested — the composition could not have used facts the model could not even read. The diagnosis per definition v0.4 is "missing-fact, not composition."

### Other-rate ceiling breach (R6cat = 39.6%)

The R6cat category (per definition v0.4 §2 + §15) is "any other token, incl. depth-1 competitor tokens, decoy interior nodes, or genuinely off-distribution/malformed." With **R4b separated** (depth-competitor-grabs counted distinctly; R4b = 0/96 = 0.000), R6cat now captures the residual: depth-1 competitor tokens (B_competitor_i), decoy chain interior nodes (decoy bridge + decoy answer), and any off-distribution output. The 0.10 ceiling fires at 0.3958 — nearly 40% of composite responses are off-category.

**What this means:** the model is emitting tokens that aren't C*, B, T, any decoy terminal, any X_i, or NULL. It's grasping for SOMETHING in the context but landing on entities the construction doesn't expect to be candidates (decoy interiors, competitor B-nodes, etc.). Per the prereg this signals the construction or scorer is mis-specified for what the model is actually doing.

## 4. Notable secondary observations

- **R4b = 0/96.** Depth-competitor-grab — the specific signature the same-depth-competitor design (D=5) was built to expose — did not fire even once. The model is NOT depth-selecting via the s/t/u/v/w competitor relations. So whatever's going on, it's not the depth-selection failure mode v0.2 of the design was built to catch. Good news for the depth-selection control's design; orthogonal to the failure modes that DID fire.
- **R2 + R4 = 6/96 = 6.3%.** Terminal-grab (target sink T + decoy sinks T_i combined) is RARE. The terminal ≠ answer move (R8.1) plus the same-depth-competitor design appears to have neutralized terminal attraction effectively, at least at this n.
- **Direct-query control passed 100% (96/96).** The model never produced C* with the bridge withheld — the direct A→C* recall route is empirically excluded. No R6c invalidations fired.
- **No constant-token across queries.** No R6e invalidations fired. The model is doing DIFFERENT things for different queries — not the i06-style flat heuristic.
- **R3 (stopped-short) = 11.5%.** A meaningful fraction of composite responses returned the BRIDGE token B instead of C*, suggesting the model traversed hop1 but failed to chain into hop2 on those items — consistent with the hop2-control-floor failure being a real composition-side issue, not just a scoring artifact.

## 5. What this run does NOT establish (per §18 forbidden interpretations)

- **NOT a refutation of "Qwen2.5-3B can do two-hop reasoning"** — that would be a capability claim, out of bounds. This is a **validity statement about elicited behavior under the declared construction at FP16, n=96**.
- **NOT a substrate-infeasibility candidate yet** — per §14 + definition v0.4 §8.5, a SINGLE failed admissible run does NOT fire §8.5. Substrate infeasibility is the **conjunction** of *admissible* constructions *repeatedly failing to certify*; we have one (1) failed admissible run.
- **NOT a license to loosen R8 / R6(c) / the threshold** to manufacture a pass on a re-run. Per §17 stop-rule, any re-run requires a NEW locked preregistration.
- **NOT Claim C / Paper B / capability / mechanism / compression / certified-baseline / product-funder claim.**

## 6. Per-position diagnostic (R6d layout-position post-hoc)

Per §12 + §6 (E3), per-C*-position breakdown is a layout diagnostic only — not a dominance cell. Reported here so an aggregate trend (if any) is visible alongside the global result.

```text
position_slot   n_items   R1_validated   R1_rate
      1          17           5          0.294
      2          22           7          0.318
      3          17           2          0.118
      4          17           0          0.000
      5          23           4          0.174
                ─────         ──
                 96          18  (= global R1_validated)
```

**Layout-position anomaly: position 4 cell has R1 = 0/17.** Positions 1 and 2 cluster around ~0.30; positions 3, 4, 5 fall to 0.118 / 0.000 / 0.174. With n_per_position ≈ 17–23, individual cells are underpowered for a formal test, but the position-4 zero is striking and would be the natural starting point for a future R6d post-hoc inspection. Per the prereg this is layout-diagnostic only — does not modify the global outcome (which is FAIL via the dominant-signature branch, regardless of position breakdown).

## 7. Stop-rule compliance (per §17)

- **No post-hoc change** to construction / gate / scoring / invalidators / floor / threshold / dominance threshold / analysis unit.
- **No re-run** of the same locked preregistration. The one authorized run produced this result; that's the end of this preregistration's run quota.
- **Any future re-run** requires a NEW locked preregistration per §17 (would need a different construction design, since loosening to manufacture a pass is never allowed).
- **Honest outcome reporting:** the FAIL is real and stands as the validity statement of this run. A construction that triggers control-floor failures and an R6cat-rate breach has not elicited composition under the declared exclusions — and that is exactly what the locked rule was built to declare.

## 8. Authority + boundaries

- **Authorized by:** TL ACTION 2026-06-15 ("Execute Locked Path A FP16 Constructibility Run") relaying Manager by-name authorization. Route GREEN for this single FP16 run only.
- **No compression run occurred** (FP16 only; no INT8, no INT4, no quantization rung loaded).
- **No retry, no second run.**
- **No post-hoc changes** to the locked preregistration or its derived rules.
- **Sealed bytes 4-of-4 byte-identical** (CS verified post-run).
- **Sealed-tree boundary preserved** (targeted git add only; tier0-run/ tokenizer.json files NOT staged).

— CS Engineer, 2026-06-16 (run timestamp UTC 2026-06-16T00:12:48Z; wall-clock 284s)
