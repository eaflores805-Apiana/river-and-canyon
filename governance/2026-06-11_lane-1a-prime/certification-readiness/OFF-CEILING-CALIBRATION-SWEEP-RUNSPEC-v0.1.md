# OFF-CEILING-CALIBRATION-SWEEP-RUNSPEC-v0.1

**Version:** v0.1. River and Canyon program. Certification-readiness submap, stage 3 (run specification for the authorized sweep).
**Status:** model-free RUN SPECIFICATION + handoff. Defines exactly what CS executes for the Manager-authorized calibration sweep and how the result is interpreted. Senior does not execute (see §0). Anchored on origin/main HEAD d86dec0b.
**Authorization:** Manager "Run Off-Ceiling Calibration Sweep" — narrow, candidates CAL-A/B/C, CAL-D only if single-difference passes.
Owner/drafter: Senior Engineer · Executor: **CS Engineer** (model environment) · Interpreter: Senior (post-run, against the pre-registered harness) · Manager: later cert-run-request decision.

---

## 0. Why Senior is not the executor (stated plainly)

The authorization is addressed to CS Engineer first, and the owner split assigns Senior **"interprets the run against the pre-declared decision rule,"** which is a post-run step. Separately, the Senior drafting environment is firewalled to package registries only — no model weights, no MLX, no Qwen2.5-3B — so it **cannot** run the model, and fabricating a run would be the exact manufactured-measurement failure this program exists to prevent. Therefore this artifact is the **executable contract CS runs**, plus the **pre-registered harness** (`calibration_sweep_verdict.py`) that makes the later interpretation mechanical. CS runs; Senior interprets the returned bytes.

## 1. Pre-flight controls (CS confirms BEFORE execution — Manager-required)

```text
current HEAD:               record git rev-parse origin/main at run time
spec path:                  OFF-CEILING-CALIBRATION-SWEEP-SPEC-v0.1.md
spec sha256:                18ac212f… (recompute from the filed bytes)
candidate matrix:           CAL-A (len 9, slots 6–8), CAL-B (len 13, slots 8–11),
                            CAL-C (len 17, slots 10–15), CAL-D (optional)
prompt/template hashes:     reuse the validated run's prompt_template_sha256
                            (f1956e7d…) and decoding_config_sha256 (a20391d8…)
scorer hash:                reuse the validated run's scorer; record its sha256
manifest hash:              record realized_match_manifest sha256 per candidate
single-difference status:   computed per candidate (CAL-D dropped if it fails)
route-state declaration:    GREEN for THIS named step (Manager authorized; map
                            reconciled; identities fixed; semantic-read PASS;
                            calibration sweep not on the closed-gate list) —
                            GREEN scoped to calibration only, RED for everything in §4
closed-gate list preserved: §4 below, unchanged
```

## 2. Member construction (per candidate, reusing validated components)

```text
For each of CAL-A/B/C (and CAL-D iff single-difference holds):
  1. Generate a CLEAN member: list_len + queried-slot-depth + distractor per the
     §3 matrix of the SWEEP-SPEC; queried key present, uniquely answerable,
     interior answer position.
  2. Generate a DEFECTIVE member: identical construction EXCEPT the single
     pre-registered defect (P2: queried key absent → value not constructible).
  3. Build the realized_match_manifest; run the SINGLE-DIFFERENCE check:
       clean and defective differ ONLY in the permitted defect, matched on
       length / position / vocab / null-rate / format / count / scorer.
     If a candidate fails this (esp. CAL-D's stronger distractor introducing a
     second axis): DROP that candidate; record single_difference_ok=false.
  4. Nine-field semantic-read (owner-signed) of each candidate's construct spec.
Reuse: the P2 defect spec and P3 matching discipline are unchanged; only the
calibration (length/depth/distractor) varies across candidates.
```

## 3. Execution (per surviving candidate)

```text
model:     Qwen/Qwen2.5-3B-Instruct  (the validated model_id)
decoding:  the validated decoding_config (greedy/seeded as the prior run)
for each candidate:
  - score the CLEAN member  → strict_accuracy, n
  - score the DEFECTIVE member → strict_accuracy, n
  - write a run-output JSON in the schema the harness consumes (§5):
      {candidate_id, clean_member.summary.strict_accuracy,
       defective_member.summary.strict_accuracy, single_difference_ok,
       manifest_sha256, scorer_sha256, prompt_template_sha256, raw_output_path}
NO quantization. NO INT8/INT4. FP16/native only. This is a CLEAN-baseline
calibration sweep — there is no stress arm.
```

## 4. Closed gates (unchanged; CS must preserve)

```text
No certification run · No compression · No INT8/INT4 stress · No second
compression rung · No candidate certification · No ranking · No Claim C
activation · No public benchmark packaging · No funder-facing release · No SBIR
submission. The authorization is calibration-only: the run may answer ONLY
"does a clean construct land in the band?" — nothing about stress, retention, or
composition.
```

## 5. Interpretation (Senior, post-run, via the PRE-REGISTERED harness)

The verdict is computed mechanically by `calibration_sweep_verdict.py` (filed
alongside, logic self-tested), so it cannot drift to fit a hope:

```text
python3 calibration_sweep_verdict.py \
    --floor 0.6125 --ceiling 1.0 \
    --margin <m> --delta <δ>          # m, δ PRE-DECLARED before the run
    --run CAL-A:<path> --run CAL-B:<path> --run CAL-C:<path> [--run CAL-D:<path>]
```

Pre-declared decision rule (the harness enforces it verbatim):

```text
BAND PLAUSIBLE:            ≥1 clean candidate lands strictly in (0.6125+m, 1.0−δ).
BAND TOO NARROW:           every ceiling-escaping candidate collapses to/below
                           floor+margin (levers can't separate the two).
INSUFFICIENT/NEEDS REPAIR: single-difference fails for an authorized candidate,
                           OR no candidate escapes the ceiling at all (→ specify
                           harder settings; do NOT pivot — uncharacterized ≠ narrow).
```

Note the harness keeps the C-verdict discipline: "no candidate escaped the
ceiling" returns INSUFFICIENT (needs harder settings), NOT "too narrow" —
because uncharacterized is still not the same as narrow.

## 6. Required run report (CS returns; Manager-required fields)

```text
per candidate: candidate ID · clean accuracy · defective accuracy ·
  shortcut-floor comparison (vs 0.6125+m) · ceiling comparison (vs 1.0−δ) ·
  band verdict (per harness) · raw output path · manifest path · scorer path ·
  sha256s · notes/blockers
plus: HEAD at run time · single_difference_ok per candidate · route-state GREEN
  attestation · closed-gate-preserved attestation.
```

## 7. After run (owner split)

```text
CS:        runs §1–§3, returns the §6 report (does NOT interpret).
Senior:    runs §5 harness on the returned bytes; states the band verdict against
           the pre-declared rule; updates the position tracker.
Team Lead: prepares the Manager decision surface.
Manager:   decides whether a later CERTIFICATION-RUN request is well-formed.
```

---

## Submap status after this run spec

```text
SUBMAP: Certification-readiness / off-ceiling repair design — STILL OPEN.
  stage 1   repair design               FILED
  stage 2   calibration read → C        FILED
  stage 2b  sweep spec                   FILED
  stage 3   run spec + harness (this)    FILED — ready for CS execution
  stage 3-run  CS executes the sweep     PENDING CS (authorized; GREEN for calibration)
  stage 3-interp Senior reads result     PENDING the run bytes
  stage 4   (gated) cert-run request      NOT EVALUATED
Closing condition: the harness verdict on the real run → BAND PLAUSIBLE
(cert-run request becomes well-formed) / TOO NARROW (pivot to Tier 1) /
INSUFFICIENT (specify harder settings, re-run).
```

— Senior Engineer
