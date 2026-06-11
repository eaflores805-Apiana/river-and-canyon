# Lane 1a' Prime — D4 Readiness / Authorization Packet (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
D4 READINESS PREPARATION ONLY — NO D4 AUTHORIZATION REQUESTED OUTSIDE §20 BELOW
SEALED LOCK-RECORD v1.0 IS THE INSTRUMENT-STATE ANCHOR
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
D4 TOKEN-PRIOR AUTHORIZATION SLOT: PENDING / UNOPENED
```

To: Manager (decision) · Cc: Team Lead, New Senior Engineer, Senior Engineer
From: CS Engineer
Date: 2026-06-11
Re: Manager-authorized D4 readiness packet preparation

This packet supports — but does not presume — a later Manager D4
decision. Per Manager §2 it preserves the two-question structure
(sweep execution authorization vs token-prior generations by-name
authorization) and per Manager §4 it proposes the narrow first
model-facing shape (D4-A: minimal model-facing pilot; no quantization
stress; no Claim C; no candidate certification). The explicit Manager
decision checklist is in §20.

The sealed Lane 1a' Prime LOCK-RECORD v1.0 is the immutable instrument
anchor for any D4 work. All twenty required items below carry the
sealed-state non-claim block as the operative constraint.

---

## §1. Sealed LOCK-RECORD path and sha256

| Field | Value |
|---|---|
| Path | `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` |
| sha256 | `51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935` |
| Status | SEALED (Manager-authorized 2026-06-11; TL-verified 24/24 bindings at commit `2b17ed9`) |

D4, if approved, would consume the sealed instrument by its committed
paths and hashes. The pre-flight refusal machinery
(`analysis.verify_pre_flight_config`) already enforces hash-precondition
checks against the three lock-event artifacts at runtime; the D4
runner would be required to invoke the same pre-flight before any
model interaction.

## §2. Commit SHA for sealed instrument state

```text
sealing commit:   e69a7ad35e09581c9723565ed625c02a6b511147 (short e69a7ad)
TL-verified HEAD: 2b17ed9e77aaca64f96cdf9bf1542c0e06ede00c (short 2b17ed9)
```

The TL-verified HEAD includes the live-refusal memo bound by the
sealed record (filed during the HOLD-closure round; Branch 1; bytes
matched bound hash exactly).

## §3. Proposed model identity

```text
Family:         Qwen2.5
Variant:        Qwen2.5-3B-Instruct (instruction-tuned)
Architecture:   transformer decoder (3B parameter class)
Tokenizer:      Qwen2 tokenizer (single tokenizer for the lane; see §7)
Provider:       Alibaba / Hugging Face hub
License:        per Hugging Face listing (Tongyi Qianwen License)
```

This is the same model family as the canonical Paper 2 / B1 v2 line.
Selecting it for the first D4-A pilot keeps Lane 1a' aligned with the
existing lab provenance baseline rather than introducing a model-family
axis at the same time as the first model-facing instrument step.

## §4. Model snapshot / provenance

```text
proposed model_snapshot_hash:
  abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20

reference: B1 v2 lock on main (merge commit 3cbfce5; locked 2026-06-10).
Same snapshot hash that Paper 2's full regression reproduced
bit-identically (96/96 raw_output match under the locked runner).

provisioning precondition (to fill at D4 execution authorization):
  - FP16 weights must be staged at a declared path before any D4-A
    inference runs.
  - tier0-run/ ships the int4 and int8 packages only; the FP16
    snapshot lives outside this repo. Staging is a precondition of
    D4 execution, not of this readiness packet.
```

## §5. Runner provenance

```text
proposed runner identity: lane1a_runner.py (new file; not yet authored)
proposed runner path:     experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py
authoring status:         NOT YET AUTHORED — authoring is gated behind
                          Manager D4 execution authorization. The runner
                          would be authored as a deliverable inside the
                          D4 execution work order if Manager approves.
```

The runner would:
1. Call `analysis.verify_pre_flight_config` against the three
   lock-event artifact sha256s as the first action; refuse to proceed
   on any mismatch.
2. Load the sealed `pilot_manifests_L01.json` (sha256 `afe0e545…`).
3. Construct prompts from manifests via a single declared prompt
   template (see §7).
4. Run inference via `mlx_lm` (the same path used by Paper 2 / B1 v2).
5. Parse model outputs into the validation harness's prediction shape
   (`SimulatedPrediction` analogue or a new `CandidatePrediction` shape).
6. Hand predictions to the existing `_build_measurements_for_predictions`
   and the T3 / T4 / IVR machinery in `lane1a_prime/validation.py`.
7. Re-verify A6 against the sealed `final_manifests_L01.json` (sha256
   `afe0e545…`).
8. Emit the D4-A IVR + execution_ledger labeled
   `SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION`
   carried verbatim from the sealed non-claim block.

The runner's sha256 would be recorded in the D4-A execution ledger and
in any D4-A completion summary.

## §6. Quantization state

```text
proposed precision rung:  FP16 (unquantized)
quantization stress:      NONE (per Manager §4 recommendation)
INT8 / INT4 work:         OUT OF SCOPE for D4-A; would require a
                          separate authorization
```

This aligns with the canonical Paper 2 / B1 v2 baseline and avoids
introducing a quantization axis at the first model-facing step. If the
team later wishes to add INT8 / INT4, that is a separate (post-D4-A)
decision.

## §7. Exact prompt / manifest / scoring paths and hashes

### Manifests (sealed; bound by LOCK-RECORD §4)

| artifact | path | sha256 |
|---|---|---|
| Pilot manifests | `experiments/2026-06-11_lane-1a-prime/validation/pilot_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| Final manifests | `experiments/2026-06-11_lane-1a-prime/validation/final_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| Schema | `experiments/2026-06-11_lane-1a-prime/schemas/manifest_schema.yaml` | (existing; bind at D4 execution time) |

Pilot and final share sha256 by construction (PH5-3 identical-seed
property).

### Prompt template

```text
status:                      NOT YET AUTHORED — gated behind D4
                             execution authorization
proposed prompt template path:
  experiments/2026-06-11_lane-1a-prime/d4_runner/prompt_template_v1.json
content shape (proposed):    single declared Jinja-style or string-format
                             template that renders a manifest's
                             {context_block, queried_key, response prefix}
                             into a single-line prompt string per the
                             locked instruction-tuned message format
                             (Qwen2.5 chat template).
locking discipline:          template sha256 would be bound into the
                             D4-A execution ledger and into any future
                             D4-A IVR; any post-lock change is a
                             must-fix requiring C1 disposition.
```

### Scoring

| component | path | sha256 |
|---|---|---|
| Predict-shape (model output → prediction) | NOT YET AUTHORED — gated behind D4 authorization; proposed path `experiments/2026-06-11_lane-1a-prime/d4_runner/parse_model_output.py` | n/a |
| Measurement / criterion code (already sealed) | `experiments/2026-06-11_lane-1a-prime/lane1a_prime/validation.py` (sha256 to bind at D4 execution time; current local sha256 in working tree differs from the sealing-time commit and will be re-pinned at D4 execution) | (re-pin at D4 time) |
| T3 bound loader (already sealed) | `experiments/2026-06-11_lane-1a-prime/lane1a_prime/analysis.py` sha256 `3f83ac57d59f30818d12888ce0d364c78d3226475ab1ca4dd098c0cc99c55969` | bound |

Tokenizer:
```text
single declared tokenizer for the lane: Qwen2 tokenizer (matches the
proposed model snapshot in §3/§4).
tokenizer hash: to be computed and bound at D4 execution authorization
                from the FP16 model snapshot's tokenizer files.
ordering rule: token-id-sequence lexicographic under the packet's
               single declared tokenizer + canonicalization (per
               the sealed Lane 1a' design declaration A5).
```

## §8. Proposed output directory

```text
experiments/2026-06-11_lane-1a-prime/d4_a_pilot/
  ├── candidate_outputs/        (one JSON per manifest record)
  ├── candidate_predictions.json (parsed predictions)
  ├── pre_flight_log.json       (PH5-4 pre-flight result)
  ├── t1_report.json            (battery degeneracy audit vs candidate)
  ├── t3_report.json            (6-criterion checklist vs candidate)
  ├── t4_report.json            (review-to-lock disposition)
  ├── a6_re_verification.json   (drift block)
  ├── instrument_validation_report.md
  ├── execution_ledger.json
  └── prompt_template_used.json (the exact template + sha256)
```

D4-A artifacts would NOT be co-mingled with the sealed instrument
artifacts at `validation/`. The sealed `validation/` directory remains
immutable; D4-A writes only into `d4_a_pilot/`.

## §9. Proposed sweep_id, if requested

```text
proposed sweep_id format:    lane1a-prime-d4a-YYYYMMDD-HHMMSS-<random6>
example:                     lane1a-prime-d4a-20260612-091500-a7b3c4
creation gate:               Manager authorization (per D4 question 1
                             checklist in §20)
authorization status:        NOT REQUESTED at this readiness stage;
                             Manager decision pending
```

The sweep_id, if created, would be stamped into every D4-A output
record, into the execution ledger, and into the D4-A completion
summary. It would NOT be created during readiness preparation.

## §10. Whether model execution is requested

```text
At this readiness stage:  Model execution is REQUESTED for D4-A
                          (this is the entire point of the D4-A pilot —
                          the first model-facing step against the sealed
                          instrument).

Authorization status:     NOT YET AUTHORIZED. Per Manager §6, model
                          execution remains closed until Manager
                          separately approves. The §20 decision
                          checklist preserves the choice.

Scope, if approved:       96 inferences (80 answerable + 16 NULL) on
                          rung L01 only. No multi-rung sweep. No batch
                          re-runs. One deterministic-seed run.
```

## §11. Whether sweep execution is requested

```text
At this readiness stage:  Sweep execution is REQUESTED for D4-A
                          (per Manager §2 D4 question 1; the §20
                          decision checklist preserves the choice).

Authorization status:     NOT YET AUTHORIZED.

Scope, if approved:       Single sweep over the 96 sealed L01 manifests.
                          One pass per record. No multi-temperature
                          fan-out. No multi-rung extension. No
                          re-execution under varied conditions in this
                          packet — varied conditions would be a separate
                          decision.
```

## §12. Whether token-prior generations are requested by name

```text
At this readiness stage:  Token-prior generations are NOT REQUESTED
                          for D4-A.

Rationale:                The sealed T3 bound for
                          accuracy_indistinguishable_from_token_prior
                          (TP_margin = 0.10) compares candidate accuracy
                          against an ANALYTICAL control baseline
                          (1/26 ≈ 0.038, derived from shell construction:
                          uniform visible VALUE_POOL of size 26, queried
                          key absent, bindings removed). The analytical
                          baseline does NOT require any model
                          generation. The token-prior emitter oracle
                          case (ORC-06) in the sealed validation used
                          predict_token_prior_emitter (synthetic) as a
                          uniform-pool draw for label-set verification;
                          for the real-model D4-A pilot, the analytical
                          baseline suffices.

Authorization status:     NOT REQUESTED at this readiness stage;
                          token-prior authorization slot remains
                          PENDING / UNOPENED per the sealed LOCK-RECORD.

If later requested:       Would require Manager by-name authorization
                          per Manager §2 D4 question 2 AND a separate
                          packet justifying the need for model-derived
                          token-prior generations over the analytical
                          baseline.
```

## §13. Stopping rules

```text
hard stops (always applied):
  1. PH5-4 pre-flight refusal — any lock-event hash mismatch aborts the
     run before any inference.
  2. Manifest schema validation refusal — any non-conformant record
     aborts the run.
  3. Tokenizer mismatch refusal — the runner's tokenizer hash must
     equal the locked tokenizer hash; mismatch aborts.
  4. mlx_lm version mismatch refusal — declared version mismatch aborts.
  5. Model snapshot hash mismatch refusal — actual model weights sha256
     must equal the declared snapshot hash; mismatch aborts.

soft stops (recorded; do not abort the run):
  6. Per-record inference timeout (proposed 60 seconds per inference);
     record marked INCONCLUSIVE per §15 and contributes to the void
     budget.
  7. Output token count exceeding declared maximum (proposed 32 tokens);
     truncated; recorded as void with reason logged.

completion criteria:
  - All 96 records have a recorded output (real or INCONCLUSIVE).
  - Pre-flight, A6 re-verification, T1/T3/T4 reports, IVR, and ledger
    all written.
```

## §14. Abort rules

```text
abort triggers (terminate the run; emit abort ledger; preserve partial
artifacts under d4_a_pilot/aborted_<timestamp>/):

  1. ValidationPreFlightRefused (PH5-4) — abort before any inference.
  2. ManifestSchemaValidationError — abort before any inference.
  3. ModelLoadFailure (snapshot hash mismatch, missing weights file,
     mlx_lm import error) — abort before any inference.
  4. TokenizerMismatch — abort before any inference.
  5. Cumulative void budget exceeded (proposed: > 5% of records
     INCONCLUSIVE) — abort partway through; preserve completed records.
  6. Harness anomaly (uncaught exception in the runner or measurement
     code; manifest hash drift between pilot and final beyond the 0.05
     A6 tolerance computed live) — abort; preserve partial state.

abort-record discipline:
  - Aborted runs are RETAINED, not erased (E11 / PH5-5 carryover).
  - Aborted runs CANNOT be promoted to a "successful" D4-A; they are
    failed pilots with a retention record and a documented abort cause.
  - Any subsequent re-attempt requires a new sweep_id (no reuse of an
    aborted sweep_id).
```

## §15. INCONCLUSIVE handling

Per the sealed INH-2 (A2) totality `INCONCLUSIVE | ELIMINATED | NOT_RULED_OUT`:

```text
record-level INCONCLUSIVE triggers:
  - per-record inference timeout (soft stop §13.6)
  - output truncation past declared limit (soft stop §13.7)
  - parse failure: model output cannot be mapped to a value token by
    the §7 parser
  - manifest-validation failure on a single record (logged; record
    INCONCLUSIVE; run continues unless cumulative budget exceeded)

rung-level INCONCLUSIVE triggers:
  - void budget exceeded (cumulative INCONCLUSIVE > 5% of records;
    rung outcome INCONCLUSIVE; abort per §14.5)
  - harness anomaly (rung outcome INCONCLUSIVE; abort per §14.6)
  - pre-flight refusal at start (rung outcome INCONCLUSIVE; abort
    per §14.1)

INCONCLUSIVE != ELIMINATED. INCONCLUSIVE means "instrument cannot
reach a determination at this rung under these manifests"; it is
neither a pass nor a fail. Per sealed INH-2 K-counter rules,
INCONCLUSIVE rungs are excluded from K.

void budget reporting:
  - per-record void category logged in t1_report.json
  - cumulative void rate reported in the IVR
  - if void rate > 5%, the IVR carries "rung outcome: INCONCLUSIVE"
    and the run is aborted (per §14.5).
```

## §16. Expected artifacts

```text
under experiments/2026-06-11_lane-1a-prime/d4_a_pilot/:

  candidate_outputs/<record_id>.json
    raw model output per record; includes: record_id, prompt sha256,
    output_token_ids, output_string, generation_metadata
    (latency_ms, tokens_generated, finish_reason)

  candidate_predictions.json
    list of parsed predictions per record; shape mirrors
    SimulatedPrediction for downstream pipeline compatibility

  pre_flight_log.json
    PH5-4 result; declared vs actual hashes; PASS or REFUSAL with
    reason

  t1_report.json
    battery degeneracy audit (candidate vs locked battery);
    per-policy scores (candidate, not battery; battery uses sealed
    synthetic policies); A6 drift block

  t3_report.json
    6-criterion checklist applied to the candidate's measured values
    against the locked bounds (FLOOR 0.75, CEIL 0.20, TP 0.10, ENV 0.10,
    HEAD 0.15, GAP 0.30)

  t4_report.json
    review-to-lock disposition: INH-1/2/3 incorporated; PH5-1..5
    incorporated; D4-A new rows for runner/prompt/tokenizer/snapshot
    bindings

  a6_re_verification.json
    pilot-vs-final drift block (expected 0.00 under faithful
    identical-seed property; flagged drifts list)

  instrument_validation_report.md
    D4-A IVR; same §9 sections as the sealed run-3 IVR + a new
    "Candidate identity and provenance" section + the sealed
    non-claim block carried verbatim

  execution_ledger.json
    9 fields including no_model_invoked → REPLACED with model_invoked
    field (since D4-A invokes a model); the field carries the
    sweep_id, model_snapshot_hash, mlx_lm_version, tokenizer_hash,
    runner_hash, prompt_template_hash, scorer_hash for full
    provenance reconstruction

  prompt_template_used.json
    exact template used; sha256 for binding into the IVR
```

All D4-A artifacts would be SYNTHETIC / DIAGNOSTIC — NON-BINDING —
NOT FOR THRESHOLD DERIVATION labeled.

## §17. Post-run verification requirements

```text
required immediately after run completion (before any "success" claim):

  1. Pre-flight log must show PASS for all three lock-event hashes.
  2. A6 drift must be ≤ 0.05 on every component AND on the envelope
     (per IS-7 declared tolerance; per sealed PH5-3 should be 0.00
     by construction).
  3. Sweep_id in execution_ledger.json must match the Manager-authorized
     sweep_id from §20 (if approved).
  4. Model snapshot hash in execution_ledger.json must match the
     declared snapshot hash from §4.
  5. Mlx_lm version in execution_ledger.json must match the version
     stamped at the start of the run.
  6. Tokenizer hash in execution_ledger.json must match the locked
     tokenizer hash from §7.
  7. Runner hash must match the post-authoring runner sha256.
  8. Prompt template hash must match the locked template sha256.
  9. Void rate must be ≤ 5% (else rung INCONCLUSIVE and the result is
     not lock-eligible).
  10. No required artifact under §16 may be missing.

If all ten post-run checks pass:
  - The D4-A IVR may be filed as a candidate for D4-A acceptance review.
  - Acceptance is a separate Manager decision (this readiness packet
    does not pre-commit to acceptance).

If any post-run check fails:
  - Run is RETAINED under E11 / PH5-5 at d4_a_pilot/superseded_<id>/.
  - Reason for the failure is documented.
  - No "passing" results may be reported.
```

## §18. Non-claim block

Per Manager §5 verbatim:

> D4, if later approved, would be an instrument-use step, not a
> capability claim.
>
> It would not establish model capability, model incapability,
> task-family viability, candidate suitability, certification
> readiness, retention-under-compression, Claim C progress, seam
> evidence, or public benchmark status.
>
> The instrument may rule out; it may not rule in.
>
> Passing the declared battery is reportable only as "not explained
> by the declared shortcut battery," never as "not shortcut-driven."
>
> We have improved the ruler; we have not yet mapped the territory.

This non-claim block governs every D4-A artifact, every IVR section,
every execution-ledger field, every post-run report, and every
reference made to D4-A in any subsequent governance memo.

## §19. Explicit statements

### §19.A — D4 does not activate Claim C

```text
Claim C activation requires a separate Manager decision under the
Paper 3 certification protocol, with: a stress-eligible baseline; a
declared scope_of_certification; the threshold sheet locked; a sealed
candidate identity bound by all relevant provenance hashes; and the
retention-under-compression result accepted by Manager.

D4-A would establish NONE of these. Specifically:
  - D4-A does NOT make the model a candidate.
  - D4-A does NOT lock a threshold sheet.
  - D4-A does NOT stress-test under quantization.
  - D4-A does NOT certify the model for any scope.
  - D4-A does NOT advance Claim C.

D4-A is an instrument-use step. It checks whether the sealed
instrument can be driven against a real model without breaking
governance, logging, abstention handling, shortcut labeling, or
output discipline.
```

### §19.B — D4 does not authorize stress-retention testing unless separately named

```text
Stress-retention testing — running the sealed instrument against
quantized variants (INT8 / INT4) of the same model, or running it
under sampling temperature variation, or running it across multiple
random seeds — is OUT OF SCOPE for D4-A.

Stress-retention testing requires a separate Manager authorization
that names the stress axis explicitly (e.g., "INT8 retention",
"INT4 retention", "temperature-fan-out retention").

D4-A is one model, one precision (FP16), one seed, one pass. Nothing
more.
```

---

## §20. Manager D4 Decision Requested

```text
Manager D4 Decision Requested:

[ ] authorize sweep execution
[ ] decline sweep execution

[ ] authorize token-prior generations by name
[ ] decline token-prior generations

[ ] authorize sweep_id creation
[ ] decline sweep_id creation

[ ] authorize model execution
[ ] decline model execution
```

### CS recommendation (Manager not bound by it)

```text
Recommended D4-A first model-facing shape:

  [X] authorize sweep execution         — needed to drive 96 inferences
                                           against the sealed manifests
  [ ] decline sweep execution

  [ ] authorize token-prior generations by name
  [X] decline token-prior generations   — analytical 1/26 baseline
                                           suffices per §12 rationale;
                                           preserve token-prior slot as
                                           PENDING / UNOPENED for now

  [X] authorize sweep_id creation       — needed for provenance stamping
                                           per §9 / §16 / §17
  [ ] decline sweep_id creation

  [X] authorize model execution         — the entire point of D4-A;
                                           one model, FP16, one pass
  [ ] decline model execution
```

If Manager approves this recommended shape (or any subset), the next
deliverable from CS would be the D4-A execution packet authoring work:
the runner, the prompt template, the parse-model-output module, the
test coverage, and the pre-execution sanity check — all under explicit
Manager D4 execution authorization. CS would NOT initiate any of that
authoring under this readiness packet alone; this readiness packet is
preparation only.

If Manager declines any or all of the four authorizations, CS would
stand down on the corresponding work items. Manager may approve one,
both halves of one, all four, or none.

---

## Appendix A — Reading order for D4 review

1. Start here: **this packet (§1–§20)** for the consolidated proposal.
2. `LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` (sha256 `51e18fa9…`)
   for the immutable sealed instrument state.
3. `MANAGER-LOCK-RECORD-SEALING-AUTHORIZATION-2026-06-11.md`
   (sha256 `fbc34b12…`) for the upstream sealing authority.
4. `MANAGER-D3-AUTHORIZATION-2026-06-11.md` (sha256 `802439a7…`)
   for the upstream D3 acceptance.
5. `PH5-1-JOINT-LOCK-EVENT-RECORD-v0.2.md` (sha256 `264cc47e…`)
   for the locked T3 bounds, the locked recipe schedule, and the
   ORC-08 / ORC-10 wording.
6. `PHASE5-v0.2-CORRECTIVE-RUN3-COMPLETION-SUMMARY.md`
   (sha256 `9655b8c5…`) for the run-3 results that the sealed
   record binds.

## Appendix B — Standing carry (non-authorizations, verbatim)

This D4 readiness packet does not authorize: D4 sweep authorization;
D5 close-out; model runs; model loading; new sweep_id; sweep
execution; token-prior model generations; scrambled-binding model
generations; candidate/model outputs; candidate selection; ranking;
threshold work; certification evaluation; stress-retention testing;
Claim C activation; public benchmark packaging.

All model-touching and sweep-execution gates remain CLOSED until
Manager separately approves them by name via §20.

**D4 token-prior authorization slot: PENDING / UNOPENED.**

— CS Engineer, 2026-06-11
