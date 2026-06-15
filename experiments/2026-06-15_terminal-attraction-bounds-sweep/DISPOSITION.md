# DISPOSITION — TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1

**Primary §8 reading: POSITION_EFFECT (with the unanticipated REVERSE-K direction flagged below).**

This disposition is written after applying the locked classifier and the §8 pre-declared readings to the 6-cell table. Nothing in this disposition was decided after looking at the model outputs; every threshold and reading was locked in the preregistration.

---

## 1. Headline — the 6-cell table

```text
                     PRIMARY            hop1     hop1     VALIDITY       composite   composite
cell        n        hop1 grab          abstain  correct  hop2 ctrl      correct     decoy-grab
                     (TARGET_TERMINAL_GRAB rate)                          (note flag)
─────────────────────────────────────────────────────────────────────────────────────────────
k1_EARLY    12        0.833              0.000    0.083    1.000          1.000*      —
k1_LATE     12        0.583              0.250    0.083    1.000          1.000*      —
k3_EARLY    12        0.083              0.167    0.333    1.000          0.333       0.667
k3_LATE     12        0.417              0.167    0.417    1.000          0.750       0.167
k5_EARLY    12        0.000              0.167    0.583    1.000          0.333       0.167
k5_LATE     12        0.167              0.167    0.583    1.000          0.667       0.000
─────────────────────────────────────────────────────────────────────────────────────────────
averages    72     k1=0.708, k3=0.250, k5=0.083  | EARLY=0.306, LATE=0.389

  * composite@k=1 distinguishability-limited (per §6) — at k=1 the only chain-
    terminal in the item IS the target's C, so composite-correct cannot be
    separated from a target-terminal grab. Reported, NOT counted as composition
    competence.
```

## 2. Validity floor — passed

```text
hop2 CORRECT rate = 1.000 in every cell.
  The model demonstrably performs single-fact "B maps to C" retrieval in
  every cell, EARLY and LATE, at k=1, 3, and 5. No cell is uninterpretable
  on the validity floor; the attraction meter is reading a real signal,
  not a model-not-functioning artifact.
```

## 3. The §8 reading

Computed against the pre-declared thresholds:

```text
SMOOTH SCALING (≥ +0.25 from k=1 to k=5, monotone-ish across both positions)
  hop1 grab rate at k=1 → k=5: 0.708 → 0.083 (Δ = −0.625).
  ✗ NOT HELD (and the direction is the REVERSE of what SMOOTH SCALING anticipated).

MAXED AT k=1 (≥0.50 at k=1 AND roughly flat across k)
  k=1 average = 0.708 ≥ 0.50 ✓ — but |k5 − k1| = 0.625, NOT flat.
  ✗ NOT HELD.

POSITION EFFECT (≥0.25 EARLY/LATE gap at any fixed k)
  position gaps by k:  k=1 → 0.25,  k=3 → 0.33,  k=5 → 0.17.
  ✓ HELD at k=1 and k=3 (≥0.25); at k=5 below the threshold.

FLAT / MIXED
  Not applicable — strong non-flat structure across k.
```

**§8 primary reading: POSITION_EFFECT.** Attraction is position-/recency-sensitive
on this construction at k=1 and k=3; the EARLY/LATE gap shrinks at k=5 as overall
attraction collapses.

## 4. The unanticipated dominant signal: REVERSE-K direction

The strongest pattern in the table is not in any §8 reading slot. Attraction
**decreases sharply with clutter**, not increases:

```text
average hop1 grab rate:  k=1: 0.708   k=3: 0.250   k=5: 0.083
```

And correspondingly, hop1 CORRECT rate **rises** with clutter:

```text
average hop1 correct:    k=1: 0.083   k=3: 0.375   k=5: 0.583
```

The §8 SMOOTH SCALING reading anticipated "more distractors → more attraction;
distractor salience is a designable lever." The observed direction is the
opposite: more competing chains → less terminal-grab → more correct intermediate
retrieval. Distractor count appears to act as an **anti-attractor lever** on
this construction, not a pro-attractor lever.

**Behavioral framing, per §9 (no mechanism claim):** *On this construction,
attraction is strongest when the target chain stands alone. Adding competing
chains reduces, rather than amplifies, the model's pull toward the target
chain's terminal.* This is a behavioral observation about the construction's
interaction with this model; it is NOT a claim about attention, architecture,
or training distribution.

## 5. Position effect — direction notes

The pre-declared POSITION_EFFECT reading is content-free about direction. From
the data:

```text
k=1: EARLY (0.833) > LATE (0.583)   — attraction stronger when target hop2 sits early
k=3: EARLY (0.083) < LATE (0.417)   — attraction stronger when target hop2 sits late
k=5: EARLY (0.000) < LATE (0.167)   — same direction as k=3, smaller absolute gap
```

The position-effect **direction flips** between k=1 and k≥3. At k=1 (single
chain) the target terminal pulls more when seen early; at k≥3 (multiple chains)
the target terminal pulls more when seen late. Behavioral observation only; no
mechanism claim.

## 6. Composite — a separate behavioral pattern worth recording

```text
composite CORRECT rate:    k=1: 1.000* (flagged)   k=3: 0.542 (avg)   k=5: 0.500 (avg)
composite DECOY_GRAB rate: k=1: 0.000 (n/a, no decoys)  k=3: 0.417   k=5: 0.083
composite STOPPED_SHORT:   ~0 in all cells (rare on this construction)
```

At k=3, composite gets the right answer half the time and grabs a decoy
terminal in 0.417 of items — a meaningful decoy-grab rate that does NOT
appear at k=5 (where the model abstains more or makes other errors). The
k=3 cell is where chain confusion appears to be highest. This is noted as
an observation in the §6 seam-context slot, not as evidence about Claim C
or the seam itself.

## 7. Provenance closures (the two v0.1 gaps the prereg required this run to fix)

```text
1. items_materialized.json was committed BEFORE the model run (in commit
   81c2779, sha 92fea7fe...). The run reads those committed bytes, not a
   regenerated set. The manifest binds the same sha. v0.1 gap closed.

2. FP16 weight provenance is recorded in MANIFEST.json:
     HF revision  aa8e72537993ba99e69dfaafa59ed015b17504d1
     shard 1 sha  67347b23...   shard 2 sha  a40d941d...
   v0.1 gap closed.
```

## 8. Pre-declared limits (§10) — apply unchanged

```text
- n = 12/cell; resolution ~0.083 per item. The REVERSE-K direction (0.708 → 0.083)
  has Δ = 0.625 across k — far above the resolution; the trend is robust to this
  resolution. The POSITION_EFFECT direction-flip between k=1 and k≥3 is at the
  resolution boundary at k=5 (0.17 gap), well above at k=3 (0.33 gap).
- One model, one synthetic task family, FP16, behavioral characterization only.
  Results hold for THIS construction on Qwen2.5-3B; they do not generalize without
  separately-authorized work.
- Behavioral metrology: this measures what the model does, never why.
```

## 9. §9 forbidden interpretations — all held

```text
NOT claimed:
  - Claim C progressed
  - compositional seam demonstrated / Paper B activated
  - any compression or compression-robustness claim
  - certified-baseline claim
  - "we found the prompt fix"
  - "Qwen2.5 can / cannot do two-hop reasoning"
  - mechanism (attention / architecture / training distribution)
  - "designable lever" without the decay-guards
  - any product- or funder-facing result
```

## 10. Open decision (§8 decision point — Manager-owned, NOT made here)

```text
Per §8 the Manager evaluates the table against the readings and chooses among:
  (a) BANK and move on — bounds characterized, return to G6.
  (b) DESIGN a powered follow-up under separate authorization.
  (c) SUBSTRATE CONCLUSION — if attraction is not distractor-count-driven and
      not position-defeatable, the seam likely needs a different task family.

CS observation (per §10's substrate-viability framing): the data argues against
the "distractor-count salience" hypothesis as the mechanism behind terminal
attraction on this construction. The strongest pull is at k=1; adding chains
reduces it. The position-defeat possibility is partial (gap flips direction
between k=1 and k≥3, attenuates at k=5). Whether (c) substrate-conclusion is
the honest read is the Manager's call; nothing here forces or implies it.

§14 stop-rule: one sweep, evaluated, done. No second sweep without re-authorization.
```

## 11. Authority + sealed bytes

```text
Authority:   TL ACTION 2026-06-14 + Manager "authorize TERMINAL-ATTRACTION-
             BOUNDS-SWEEP-v0.1" (Route GREEN for this named run only).
Sealed bytes: 4-of-4 byte-identical post-run.
Sealed-tree: preserved (targeted git add only).
```

— CS Engineer, 2026-06-15 (run timestamp UTC 2026-06-15T09:06:50Z)
