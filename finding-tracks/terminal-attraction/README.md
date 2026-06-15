# Terminal Attraction — Finding Track

Behavioral characterization of a recurring failure mode in this program's closed-world
fact-chain constructions: when asked for an *intermediate* (B) or a *composition* (A→C),
the model tends to return a chain-*terminal* token or abstain rather than perform the
requested hop. Bounded by a single FP16-only clutter×position sweep on Qwen2.5-3B.

**NOT** a paper, **NOT** Lane 4 evidence, **NOT** a compression / capability / seam claim.
Behavioral metrology only. Parked beside the CAL-Q finding track. Authorizes nothing.
The next build of record remains G6.

## Contents

- `TERMINAL-ATTRACTION-BOUNDS-SWEEP-FINDING-REPORT-v0.4.md` — Senior-authored finding-track report.
  - C5 claim-risk review: PASS with interpretation constraint I1 + language guards G1/G2.
  - C6 prior-art review: PASS scoped as diagnostic subtype.
  - Anchor: run commit `f560b26` (sweep), pre-registration lock `81c2779`.
- `TERMINAL-ATTRACTION-BOUNDS-SWEEP-FINDING-REPORT-v0.4.pdf` — typeset version.
- `terminal-attraction-sweep-fig1.png` — response rates by clutter × position.
- `terminal-attraction-sweep-fig2.png` — full 6-cell rate grid.

## Headline (with the load-bearing nuance)

- **Dominant signal: reverse-K (unanticipated; flagged per §10).** hop1 target-terminal grab
  rate falls steeply with clutter (k=1: 0.708 → k=5: 0.083) while intermediate retrieval
  recovers (hop1 correct: 0.083 → 0.583). Distractor count acts as an **anti-attractor lever**
  on this construction — *demonstrated directional effect, NOT sufficient, NOT a repair, NOT
  valid below the distinguishability floor.*
- **Direction robust, magnitude metric-dependent (C5 I1).** Both the primary metric and the
  attraction-inclusive metric fall k=1→k=5; the entire divergence sits in **k3_EARLY** where
  5 wrong-chain (decoy) terminal grabs are themselves a form of attraction.
- **Composition does not track the component's recovery.** hop1 correct rises with k; composite
  correct stays roughly flat (~0.5) at k≥3 and is position-gated (LATE > EARLY).
- **Substrate viability finding (conditional):** terminal attraction is **not** an irreducible
  substrate property — it is salience-sensitive and clutter-reducible — but composition
  remains confounded. **k5_LATE** identified as a candidate regime for a *future powered test*,
  not as a constructible baseline.
- **Validity floor passed:** hop2 control = 1.000 in every one of the 6 cells.

## Provenance (the v0.1-run gaps Senior flagged were closed by this run)

- Materialized items committed BEFORE the model run (commit `81c2779`, sha `92fea7fe…`).
- FP16 weight provenance pinned: HF revision `aa8e72537993ba99e69dfaafa59ed015b17504d1`,
  per-shard sha256s in the run's MANIFEST.json.

## Boundaries (carried)

```text
- no compression evidence of any kind (FP16-only)
- no Claim C progress / no Paper B activation
- no certified baseline / no "prompt fix" / no constructible composition baseline
- no model-capability claim ("Qwen2.5-3B can/cannot do X")
- no mechanism / architecture / training-distribution claim
- "anti-attractor lever" never restated as "clutter fixes attraction"
- hop2 = 1.000 is the validity FLOOR, not a capability result
- no product / funder-facing result
```

## Stop-rule

One sweep. Six cells. Evaluated. No second sweep, no added knob, no n increase without
fresh Manager authorization. The §8 decision (bank / powered follow-up / substrate
conclusion) is the Manager's; the Senior Engineer's recommendation is to **bank the finding**
and keep G6 the next build.

## CS observation (informational)

The finding report's §1 figure-provenance lines cite `.svg` versions of both figures
(`3f3f6991…`, `1353a378…`); these `.svg` files were not in the inbox and are not in this
directory. Only `.png` versions are filed. The `.png` shas verify byte-perfect against the
shas Senior cites in §1. If the `.svg` versions are needed for typesetting, they can be
added in a later filing — non-blocking for this finding-track filing.
