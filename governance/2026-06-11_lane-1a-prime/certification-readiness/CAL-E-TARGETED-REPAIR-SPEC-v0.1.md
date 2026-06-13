# CAL-E-TARGETED-REPAIR-SPEC-v0.1

**Version:** v0.1. River and Canyon program. Certification-readiness submap, stage 3-repair (CAL-E targeted repair specification).
**Status:** model-free SPECIFICATION of one targeted candidate. Specifies; runs nothing; requests nothing. Anchored on origin/main HEAD 7e1d4fd.
**Authorization:** "Model-free specification authorized; no execution authorized." Intent: one targeted construct to settle the edge case CAL-C created — not a new broad design phase.
Owner/drafter: Senior Engineer · CS: verify paths/commit/sha256/source artifacts/INDEX + that the spec stays model-free, no run-authorization language · Team Lead: routing · Manager: any later run authorization.

---

## 1. Executive summary

The calibration sweep showed the off-ceiling levers work (clean 1.000 → 0.975 → 0.950), but at the principled threshold (m=0.05, δ=0.05; band 0.6625 < a < 0.95) CAL-C landed *exactly* on the upper boundary (0.950), leaving no strict measurable headroom — verdict INSUFFICIENT, edge-of-resolvability. CAL-E is **one** construct designed to land clean accuracy at **0.88–0.92**, comfortably inside the band with strict headroom, **while preserving clean/defective separation** — the central constraint, because CAL-C's defective accuracy rose to 0.225 and that trend must not continue. CAL-E applies the difficulty levers *selectively*: the ones that depress clean lookup load without making key-absent (defective) items look answerable.

## 2. Anchor facts (byte-read, HEAD 7e1d4fd)

```text
                 list  slots    near-miss   clean    defective
  CAL-A (control)  9   6–8       0           1.000    0.125
  CAL-B            13  8–11      2           0.975    0.050
  CAL-C            17  10–15     4           0.950    0.225   ← defective inflation
  shortcut floor (union envelope): 0.6125
  principled band (m=δ=0.05):      0.6625 < clean < 0.95
  CAL-E clean target:              0.88–0.92  (strict interior)
Two readings from the trend:
  - clean responds smoothly to length+depth+near-miss (monotone down).
  - defective is NON-monotone (0.125→0.05→0.225); the jump at CAL-C tracks its
    jump to 4 near-miss distractors — the leading hypothesis is that near-miss
    VALUES make some key-absent items look answerable, inflating defective.
```

## 3. Why CAL-E is needed

```text
- To settle the edge case: CAL-C at exactly 0.95 does not clear δ=0.05 strictly;
  a point at ~0.90 does (0.6625 < 0.90 < 0.95 with room on both sides), and with
  CAL-B (0.975) it brackets a real interior interval, making the band's
  occupancy unambiguous at the principled threshold.
- To do it WITHOUT the CAL-C side effect: simply pushing harder (more near-miss)
  risks driving defective accuracy up further, eroding the clean/defective
  separation that is the instrument's entire purpose. CAL-E must lower clean via
  levers that do NOT inflate defective.
```

## 4. Proposed CAL-E construct settings

The design lowers clean lookup difficulty primarily through **length and depth** (which load genuine lookup without offering the defective item a false answer), and holds **near-miss distractors at or below CAL-C's level on the DEFECTIVE member**, applying any added distractor pressure in a way that is single-difference-shared and value-safe:

```text
candidate ID:        CAL-E
list length:         21        (longer than CAL-C's 17 → more lookup load → clean down)
queried slot range:  13–18     (deeper interior than CAL-C → less endpoint-favored)
answer position:     interior  (never first/last → defeats position shortcuts)
near-miss distractors (KEY side): up to 4 (NOT increased beyond CAL-C) —
                     near-miss KEYS may be added (they pressure clean lookup) but
                     near-miss VALUES that could satisfy a key-absent defective
                     item are CAPPED at CAL-C's level or reduced.
distractor placement: near-miss keys distributed across the list, NOT clustered
                     at the queried slot (clustering is what most inflates
                     defective false-answerability).
primary clean-lowering lever: LENGTH + DEPTH (21 / slots 13–18), not added
                     near-miss — because length/depth load lookup symmetrically
                     for clean and defective, whereas near-miss values
                     asymmetrically help the defective item look answerable.
```

Rationale for leaning on length/depth over near-miss: length and deep-slot
position increase the lookup burden for the *clean* item (driving its accuracy
toward 0.90) while giving the *defective* (key-absent) item no additional way to
appear answerable — so clean drops without defective rising. Near-miss *values*
are the lever implicated in CAL-C's defective inflation, so CAL-E does not push
that lever further.

## 5. Expected clean accuracy target

```text
TARGET: clean strict_accuracy in 0.88–0.92 (strict interior of 0.6625 < a < 0.95).
Basis: clean fell ~0.025 per CAL step (1.000 → 0.975 → 0.950) driven mainly by
length/depth. Extending length 17→21 and slots to 13–18 is expected to add a
further ~0.03–0.07 of lookup difficulty, landing clean ≈ 0.88–0.92. This is an
EXPECTATION for a later (gated) run to confirm, not a measured value.
```

## 6. Expected defective behavior

```text
TARGET: defective strict_accuracy LOW (≤ ~0.10, i.e. at or below CAL-A/CAL-B
level, NOT CAL-C's 0.225). The construct is designed so the key-absent item has
no near-miss VALUE that satisfies it and no clustered distractor at the queried
slot. If the (later, gated) run shows defective rising toward CAL-C's 0.225
again, that is a NEEDS-REPAIR / PIVOT-WATCH signal (see §10), not a pass —
because clean/defective separation is the instrument's purpose.
SEPARATION REQUIREMENT: clean − defective must remain large (target ≳ 0.78, i.e.
clean ~0.90 vs defective ~0.10). A high clean with an inflated defective is NOT
a usable certification baseline.
```

## 7. Shortcut-floor protection

```text
- Clean target 0.88–0.92 sits FAR above the shortcut floor 0.6125 (and above
  floor+margin 0.6625) — no shortcut policy (last-position 0.30, salient-endpoint
  0.1625, recency 0.15, prefix-neighbor 0.15, copy 0.0) can account for ~0.90.
- Interior answer position + deep slots specifically defeat last-position and
  salient-endpoint shortcuts.
- The (later) run must re-evaluate the shortcut envelope at CAL-E's difficulty
  and confirm clean stays above floor+margin; the design intent is a wide gap.
```

## 8. Single-difference preservation

```text
- Clean and defective CAL-E members differ in EXACTLY the pre-registered defect
  (P2: queried key absent → value not constructible), matched on length (21),
  slot range (13–18), vocabulary, null-rate, format, count, and scorer.
- Any near-miss distractor structure is a SHARED property of both members (same
  distractors in clean and defective), so it is not a second difference.
- The single-difference invariant is checked mechanically at construction
  (gated step); if CAL-E cannot be built single-difference, it is DROPPED, not
  run as a confound (same gate that governed CAL-D).
```

## 9. Semantic-read requirements

```text
- Nine-field shown-read (owner-signed) of the CAL-E construct spec before any
  construction is trusted: artifact / path / commit / sha256 / claimed concept /
  check performed / observed structure / required structure / surplus check,
  disposed PASS (UNCERTAIN→HOLD).
- The read must explicitly confirm: (a) length/depth are the primary clean-
  lowering levers; (b) near-miss VALUES are not increased beyond CAL-C; (c)
  single-difference holds. These three are the design's load-bearing claims.
```

## 10. Pre-declared decision rule (before any run)

```text
BAND PLAUSIBLE:
  CAL-E clean lands STRICTLY inside 0.6625 < a < 0.95 (target 0.88–0.92) AND
  defective stays low enough to preserve discrimination (clean − defective ≳ 0.78,
  defective ≤ ~0.10). One such point, with CAL-B, brackets the band's interior →
  a certification-run request becomes well-formed (separate Manager auth + GREEN).
NEEDS REPAIR:
  CAL-E remains at/above 0.95 (levers underpowered), OR drops too close to the
  shortcut floor (over-pressured), OR defective rises enough to erode clean/
  defective separation (near-miss inflation recurs). → specify a further adjusted
  candidate; do not pivot on a single signal.
PIVOT WATCH:
  Additional pressure CONSISTENTLY causes defective inflation or shortcut-floor
  collapse across attempts — i.e. there is no setting that lands clean in-band
  while keeping defective low. That would indicate the task family cannot host a
  clean off-ceiling discriminator → Tier-1 pivot becomes the honest reading.
This rule is fixed now, before any run, so a later result cannot be reinterpreted.
```

## 11. Checklist (status fields: PASS / FAIL / HOLD / NOT EVALUATED)

```text
route state                  YELLOW (model-free) ........................ PASS
artifact identity            sources anchored: CAL-A/B/C run records
                             (5ceeeea4/814676cc/50964a77), interpretation
                             e666c2e4, HEAD 7e1d4fd ...................... PASS
semantic-read                §9 reads required at the (gated) construction step  HOLD
construct settings complete  list/slots/position/near-miss/placement all stated  PASS
expected clean target        0.88–0.92, with basis ....................... PASS
expected defective behavior  ≤~0.10 + separation requirement ≳0.78 stated  PASS
off-ceiling pressure         length/depth as primary lever, stated ....... PASS
shortcut-floor protection    target far above floor+margin; re-eval named  PASS
single-difference preservation shared distractors; drop-if-violated gate .. PASS
defective-inflation guard    near-miss VALUES capped; placement de-clustered PASS
later decision rule          PLAUSIBLE / NEEDS REPAIR / PIVOT WATCH pre-declared PASS
closed-gate preservation     §12; no execution/cert/compression invoked ... PASS
```

```text
SUMMARY: design-level rows PASS. One HOLD (semantic-read) is correct — the
nine-field reads happen when the CAL-E construct is materialized at a later
gated step, not in this paper spec. No FAIL. The defective-inflation guard is
the addition that distinguishes CAL-E from "just push harder."
```

## 12. Closed gates

```text
No model execution · No certification run · No compression · No INT8/INT4 stress
· No second compression rung · No full ladder · No candidate certification · No
ranking · No Claim C activation · No public benchmark packaging · No funder-facing
release · No SBIR submission. This spec is model-free. CAL-E is executed only
under separate Manager authorization + route-state GREEN; nothing here grants it.
```

---

## Submap status after this spec

```text
SUBMAP: Certification-readiness / off-ceiling repair design — STILL OPEN.
  stage 3-interp   sweep interpretation (verdict INSUFFICIENT, edge)  FILED
  stage 3-repair   CAL-E targeted repair spec (this)                   FILED
  stage 3-repair-run  (gated) CAL-E run                                NOT EVALUATED
  stage 4          (gated) certification-run request                    NOT EVALUATED
Closing condition: a CAL-E run (later, authorized) lands clean in-band with
preserved discrimination → cert-run request well-formed; OR triggers NEEDS
REPAIR / PIVOT WATCH per §10.
```

— Senior Engineer
