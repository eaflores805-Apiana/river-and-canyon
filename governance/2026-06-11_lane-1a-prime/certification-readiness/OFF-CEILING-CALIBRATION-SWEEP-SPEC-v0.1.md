# OFF-CEILING-CALIBRATION-SWEEP-SPEC-v0.1

**Version:** v0.1. River and Canyon program. Certification-readiness submap, stage 2b (the calibration sweep specification).
**Status:** model-free SPECIFICATION. Designs a small candidate sweep that a later (separately authorized, gated) run could use to test whether a D4-family construct lands in the band. Specifies; runs nothing; requests nothing. Anchored on origin/main HEAD d86dec0b.
**Authorization:** "Model-free specification authorized; no execution authorized." Intent: make the next possible run request well-formed *later*, not request it now.
Owner/drafter: Senior Engineer · CS: verify paths/commit/sha256/source artifacts/INDEX + that the spec stays model-free and no run-authorization language slipped in · Team Lead: routing · Manager: any later run authorization.

---

## 1. Why this spec exists (anchored to the verdict)

The calibration-read verdict returned **C — INSUFFICIENT SPECIFICATION**: the existing record has **no off-ceiling clean data point**, so the band can be called neither plausible (A) nor too narrow (B) — only uncharacterized. This spec exists to design the smallest sweep that could supply those missing points.

```text
Byte-read anchors (HEAD d86dec0b):
  D4 saturation:                 clean accuracy 1.0  (80/80; 5-pair, shallow)
  constructed-positive clean:    clean accuracy 1.0  (n=40; list_len 9, slots 6–8)
  shortcut floor:                union_envelope 0.6125  (cap 0.8)
    constituents: pure_last_position 0.30, salient_endpoint 0.1625,
                  recency 0.15, prefix_neighbor 0.15, copy_completion 0.0
  constructed-positive scope:    "single-pair validation" — NOT a calibration sweep
TARGET WINDOW:  0.6125 + margin  <  accuracy  <  1.0 − δ
```

Both clean points on record sit on the ceiling wall; the sweep's job is to find whether any setting lands *inside* the window.

## 2. The difficulty levers (what the sweep varies)

```text
- list length:           more pairs → more lookup load → pressure DOWN from ceiling
- queried-slot depth:    deeper/interior slots → less endpoint-favored → DOWN
- distractor structure:  near-miss keys/values → more confusable → DOWN (but watch
                         it does not become a second difference vs the defect axis)
- answer position:       interior (not first/last) → defeats position shortcuts
- shortcut resistance:   construction must keep clean accuracy ABOVE the floor
                         policies (last-position, recency, salient-endpoint, copy)
The design tension (the structural question): length/depth/distractor push DOWN
toward the floor; staying above the floor pushes UP toward the ceiling. The sweep
is designed to reveal whether a setting exists where clean lands between them.
```

## 3. The candidate matrix (compact — designed to find the band, not to benchmark)

### Candidate A — control (constructed-positive-like)

```text
candidate ID:            CAL-A
list length:             9
queried slot range:      deep (6–8)
distractor structure:    baseline (as constructed-positive)
answer position:         interior
expected pressure:       SATURATED — reproduces the known 1.0 (anchor/control)
shortcut risks:          low; clean well above floor
semantic-read req:       nine-field read of the construct spec, owner-signed
pass/fail expectation:   clean ≈ 1.0 (CEILING) — expected to NOT be in band
reason included:         control point; confirms the sweep reproduces the known
                         saturated baseline before reading harder settings
what result means later: if CAL-A is NOT ~1.0, the harness/scoring differs from
                         the validated run → fix before trusting B/C/D
```

### Candidate B — moderate off-ceiling pressure

```text
candidate ID:            CAL-B
list length:             13
queried slot range:      deeper/interior (8–11)
distractor structure:    baseline + light near-key similarity
answer position:         interior
expected pressure:       MOVES OFF CEILING — first setting expected below 1.0
shortcut risks:          low–moderate; verify clean stays > 0.6125 + margin
semantic-read req:       nine-field read, owner-signed; single-difference check
pass/fail expectation:   clean expected in (0.6125+margin, 1.0−δ) OR just below
                         ceiling — the first real test of band occupancy
reason included:         the minimal step beyond the known saturated setting;
                         the cheapest possible off-ceiling data point
what result means later: clean in band → BAND PLAUSIBLE evidence begins;
                         clean still 1.0 → levers weaker than hoped, escalate to C;
                         clean ≤ floor → band collapse risk, escalate-with-caution
```

### Candidate C — stronger off-ceiling pressure

```text
candidate ID:            CAL-C
list length:             17
queried slot range:      deeper/interior (10–15)
distractor structure:    baseline + mild distractor pressure (near-miss keys)
answer position:         interior
expected pressure:       STRONG DOWN — risks approaching the shortcut floor
shortcut risks:          MODERATE — distractor pressure must not let a shortcut
                         policy account for the score; verify floor separation
semantic-read req:       nine-field read, owner-signed; single-difference check;
                         explicit shortcut-policy re-evaluation at this difficulty
pass/fail expectation:   clean expected lower than CAL-B; the test of whether
                         "hard enough to leave ceiling" still clears the floor
reason included:         probes the lower half of the band; the setting most
                         likely to reveal a floor-collapse if one exists
what result means later: clean in band → band has WIDTH (A and C both informative);
                         clean ≤ floor+margin → BAND TOO NARROW evidence (ceiling
                         escape and floor collapse cannot be separated on length/depth)
```

### Candidate D — optional stronger distractor (only if single-difference holds)

```text
candidate ID:            CAL-D (OPTIONAL)
list length:             17
queried slot range:      deeper/interior (10–15)
distractor structure:    stronger distractor variant
answer position:         interior
expected pressure:       STRONGEST DOWN
shortcut risks:          HIGHEST — included ONLY IF the stronger distractor keeps
                         the clean/defective pair single-difference (distractor is
                         a SHARED property of both members, not a second axis vs
                         the defect). If it cannot be made single-difference, CAL-D
                         is DROPPED — not run as a confound.
semantic-read req:       nine-field read; single-difference check is the GATE on
                         whether CAL-D exists at all
pass/fail expectation:   only meaningful if single-difference preserved
reason included:         reserve probe for the band's lower edge if A–C leave it
                         ambiguous; explicitly optional to avoid overbuilding
what result means later: same band/floor reading as CAL-C, at higher pressure;
                         OR dropped if it would introduce a second difference
```

### Matrix summary

```text
CAL-A  len 9   slots 6–8    baseline distractor     → expect CEILING (control)
CAL-B  len 13  slots 8–11   light similarity        → expect OFF-CEILING (first band test)
CAL-C  len 17  slots 10–15  mild distractor         → expect STRONG DOWN (floor-collapse test)
CAL-D  len 17  slots 10–15  stronger distractor*    → optional, *single-difference-gated
```

## 4. The decision rule (pre-declared, before any run)

```text
BAND PLAUSIBLE if:
  at least one candidate (most likely CAL-B or CAL-C) is EXPECTED to land below
  ceiling (< 1.0 − δ) while remaining above the shortcut floor + margin
  (> 0.6125 + margin). One clean in-band point flips the verdict from C to a
  plausible-A footing and makes a later certification-run request well-formed.
BAND TOO NARROW if:
  the design analysis (or later the sweep itself) shows the levers cannot separate
  ceiling escape from shortcut-floor collapse — i.e. every setting that leaves the
  ceiling also falls to/below the floor+margin. This is the structural-limit
  finding → PIVOT to Tier 1 (a legitimate, publishable negative result).
INSUFFICIENT SPECIFICATION if:
  the sweep design itself still lacks the structure to judge the band — e.g. a
  candidate cannot be made single-difference, or the levers are underspecified.
  Then refine the spec; do not run.
```

This rule is fixed now, before any run is requested, so a later result cannot be reinterpreted to fit a hope.

## 5. Checklist (status fields: PASS / FAIL / HOLD / NOT EVALUATED)

```text
route state                  YELLOW (model-free) ........................ PASS
artifact identity            sources anchored: D4 t1 (d4_a_pilot), constructed-
                             positive clean f412d04c, verdict 5b37de7a; HEAD
                             d86dec0b .................................... PASS
semantic-read                each candidate carries a nine-field read req;
                             reads themselves performed at the (gated) run ... HOLD
candidate matrix completeness 4 candidates with all 10 required fields ..... PASS
off-ceiling pressure         each candidate's expected pressure direction stated PASS
shortcut-floor protection    floor (0.6125) + margin named as the lower bound
                             each candidate must clear; CAL-C/D flagged for
                             floor-collapse risk ......................... PASS
single-difference preservation matched-pair single-difference required; CAL-D
                             gated on it (dropped if violated) ........... PASS (CAL-D conditional)
closed-gate preservation     no execution/certification/compression invoked  PASS
later decision rule          BAND PLAUSIBLE / TOO NARROW / INSUFFICIENT
                             pre-declared (§4) ........................... PASS
```

```text
SUMMARY: design-level rows PASS. The one HOLD (semantic-read) is correct — the
nine-field reads are performed when the construct specs are materialized at a
later gated step, not in this paper spec. No FAIL. No NOT-EVALUATED gaps in the
spec's own scope.
```

## 6. What this spec does and does not do

```text
DOES: define the candidate settings, their expected pressure, their shortcut
  risks, and the pre-declared meaning of each later outcome — so that IF a run is
  later authorized, it is well-formed and its result is interpretable in advance.
DOES NOT: request a run, authorize a run, select a candidate as "the" baseline,
  rank candidates, or certify anything. It is the "what we would test" the
  Manager asked for — not the test.
```

## 7. What remains closed

```text
No model execution · No certification run · No compression · No INT4 · No second
compression rung · No full ladder · No candidate certification · No ranking · No
Claim C activation · No public benchmark packaging · No funder-facing release ·
No SBIR submission. This spec is model-free. The sweep it designs is executed
only under separate Manager authorization + route-state GREEN; nothing here
grants that.
```

---

## Submap status after this spec

```text
SUBMAP: Certification-readiness / off-ceiling repair design — STILL OPEN.
  stage 1   repair design                        FILED
  stage 2   calibration read → verdict C         FILED
  stage 2b  calibration sweep SPEC (this)         FILED
  stage 3   (gated) sweep run → band read         NOT EVALUATED (needs Manager auth + GREEN)
  stage 4   (gated) certification-run request      NOT EVALUATED
Closing condition unchanged: a band read (from a later authorized sweep) returns
PLAUSIBLE → cert-run request well-formed; TOO NARROW → pivot to Tier 1.
```

— Senior Engineer
