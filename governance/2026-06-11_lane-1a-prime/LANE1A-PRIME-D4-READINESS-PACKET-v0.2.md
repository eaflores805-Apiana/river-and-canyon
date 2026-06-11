# Lane 1a' Prime — D4 Readiness / Authorization Packet (v0.2)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
D4 READINESS PREPARATION ONLY — NO D4 AUTHORIZATION REQUESTED OUTSIDE §20 BELOW
SEALED LOCK-RECORD v1.0 IS THE INSTRUMENT-STATE ANCHOR
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
D4 TOKEN-PRIOR AUTHORIZATION SLOT: PENDING / UNOPENED
```

*v0.2 (post NS + TL §1–§7 corrections): adds the explicit Manager
extent checkbox (Reading A vs Reading B); splits the Q2 token-prior
recommendation into NS GRANT vs CS DECLINE with full rationales for
both; pins `mlx_lm` to one exact version; confirms the unified
`d4_a_pilot/` output directory throughout; adds the Reading B
generator hash-pin section. All other sections from v0.1 carry
forward unchanged. Sealed LOCK-RECORD bytes UNCHANGED; D4 token-prior
authorization slot remains PENDING / UNOPENED.*

To: Manager (decision) · Cc: Team Lead, New Senior Engineer, Senior Engineer
From: CS Engineer
Date: 2026-06-11
Re: D4 readiness packet v0.2 per TL Cut-v0.2 direction

---

## §1. Sealed LOCK-RECORD path and sha256

| Field | Value |
|---|---|
| Path | `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` |
| sha256 | `51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935` |
| Status | SEALED · UNCHANGED at this filing |

## §2. Commit SHA for sealed instrument state

```text
sealing commit:     e69a7ad35e09581c9723565ed625c02a6b511147 (short e69a7ad)
TL-verified HEAD:   2b17ed9e77aaca64f96cdf9bf1542c0e06ede00c (short 2b17ed9)
current HEAD:       17f349eb5602afcdc6fea114d26c3f2056ee92c8 (short 17f349e)
```

## §3. Proposed model identity

```text
Family:         Qwen2.5
Variant:        Qwen2.5-3B-Instruct (instruction-tuned)
Architecture:   transformer decoder (3B parameter class)
Precision rung: bf16 (Apple Silicon / mlx native floating-point;
                supersedes the imprecise "FP16" wording in v0.1)
Tokenizer:      Qwen2 tokenizer (single tokenizer for the lane)
Provider:       Alibaba / Hugging Face hub
License:        per Hugging Face listing (Tongyi Qianwen License)
```

## §4. Model snapshot / provenance

```text
proposed model_snapshot_hash:
  abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20

reference: B1 v2 lock on main (merge commit 3cbfce5; locked 2026-06-10).
Same snapshot Paper 2's full regression reproduced bit-identically
(96/96 raw_output match under the locked runner).

staging precondition (filled at D4 execution authorization):
  - bf16 weights must be staged at a declared path before any D4-A
    inference runs.
  - tier0-run/ ships int4 and int8 packages only; the unquantized
    snapshot lives outside this repo.
```

## §5. Runner provenance

```text
proposed runner identity: lane1a_runner.py (NEW file; not yet authored)
proposed runner path:     experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py
authoring status:         NOT YET AUTHORED — gated behind Manager D4
                          execution authorization (§20).
runner sha256:            TBD at authoring; will be bound into the
                          D4-A execution_ledger and any future D4-A IVR.
```

Runner contract (per §5 of v0.1; unchanged in v0.2):
1. Call `analysis.verify_pre_flight_config` first; refuse on any
   lock-event hash mismatch.
2. Load sealed `pilot_manifests_L01.json` (and, under Reading B, also
   the freshly-generated L02..L08 manifests per §21 below).
3. Render prompts via the locked prompt template (sha256 to be bound).
4. Run inference via `mlx_lm` (version pinned in §7).
5. Parse outputs via `parse_model_output.py` into the validation
   harness's prediction shape.
6. Hand parsed predictions to `_build_measurements_for_predictions`
   and downstream T3/T4/IVR machinery.
7. Re-verify A6 against sealed `final_manifests_L01.json` (and L02..L08
   under Reading B).
8. Emit IVR + execution_ledger labeled SYNTHETIC / DIAGNOSTIC.

## §6. Quantization state

```text
proposed precision rung:  bf16 (unquantized)
quantization stress:      NONE (per Manager §4 recommendation; TL §3 carry)
INT8 / INT4 work:         OUT OF SCOPE for D4-A
```

## §7. Exact framework version pin (TL §5 correction)

```text
inference framework:      mlx_lm
authorized version pin:   0.19.3

pre-run check:            the D4-A runner stamps the running mlx_lm
                          version at start; if the stamped version is
                          not exactly equal to the authorized pin
                          (0.19.3), the runner aborts before any model
                          load or inference (per readiness §13 hard
                          stop 4).

provenance reference (not the authorization pin):
  mlx_lm 0.19.3 → 0.31.3 has been verified-null for the locked Paper 2
  reproduction configuration (Team Lead 2026-06-10). The verified-null
  range is documented for traceability, but the AUTHORIZATION PIN is
  one exact version per TL §5 direction; CS proposes 0.19.3 as the
  canonical Paper 2 / B1 v2 lock baseline. Manager may substitute
  0.31.3 if preferred; either way, a single exact value will be in
  effect at D4-A execution.
```

## §8. Exact prompt / manifest / scoring paths and hashes (unchanged from v0.1)

### Manifests

L01 (sealed):

| artifact | path | sha256 |
|---|---|---|
| Pilot manifests | `experiments/.../validation/pilot_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |
| Final manifests | `experiments/.../validation/final_manifests_L01.json` | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` |

L02..L08 (under Reading B; would be generated at run time per §21):

| rung | proposed path |
|---|---|
| L02 | `experiments/.../d4_a_pilot/manifests/pilot_manifests_L02.json` (and `final_manifests_L02.json`) |
| L03 | `experiments/.../d4_a_pilot/manifests/pilot_manifests_L03.json` |
| L04..L08 | analogous per-rung paths |

### Prompt template / scoring

```text
prompt template path:  experiments/.../d4_runner/prompt_template_v1.json
                       NOT YET AUTHORED; sha256 TBD at authoring
parse module path:     experiments/.../d4_runner/parse_model_output.py
                       NOT YET AUTHORED; sha256 TBD at authoring
scorer (sealed code):  lane1a_prime/validation.py (sha256 bound in §21
                       under Reading B; sealed predictions consume this
                       file's current sha256 at HEAD `17f349e`)
tokenizer hash:        computed at D4 execution time from the staged
                       model's tokenizer files (single declared
                       tokenizer for the lane).
```

## §9. Proposed output directory (TL §6 alignment correction)

**Unified across this packet: `experiments/2026-06-11_lane-1a-prime/d4_a_pilot/`**

Any prior occurrence of `sweep_d4a/` in NS or CS materials is
superseded by `d4_a_pilot/`. CS confirms there is no
`sweep_d4a/` reference inside this v0.2 packet.

```text
experiments/2026-06-11_lane-1a-prime/d4_a_pilot/
  ├── manifests/                       (Reading B only; L02..L08 generated)
  ├── candidate_outputs/                (one JSON per manifest record)
  ├── candidate_predictions.json
  ├── pre_flight_log.json
  ├── t1_report.json
  ├── t3_report.json
  ├── t4_report.json
  ├── a6_re_verification.json
  ├── instrument_validation_report.md
  ├── execution_ledger.json
  └── prompt_template_used.json
```

Sealed `validation/` is NOT modified by D4-A under any reading.

## §10. Proposed sweep_id

```text
status:          NOT YET REQUESTED — Manager decision pending (§20 Q1).
proposed format: lane1a-prime-d4a-YYYYMMDD-HHMMSS-<random6>
example:         lane1a-prime-d4a-20260612-091500-a7b3c4
creation gate:   explicit Manager §20 authorization.
```

## §11. Whether model execution is requested

```text
At this readiness stage:  Model execution is REQUESTED for D4-A
                          (this is the point of the D4-A pilot).
Authorization status:     NOT YET AUTHORIZED (Manager §20).
Scope, if approved:       96 inferences (Reading A) OR 768 inferences
                          (Reading B) on the sealed manifest surface;
                          one deterministic-seed pass; no fan-out;
                          no multi-rung re-execution beyond the
                          Manager-chosen extent.
```

## §12. Whether sweep execution is requested

```text
At this readiness stage:  Sweep execution is REQUESTED for D4-A
                          (per readiness packet Q1; Manager §20).
Authorization status:     NOT YET AUTHORIZED.
Scope, if approved:       single sweep over the chosen extent
                          (Reading A or Reading B); one pass per
                          record; no multi-temperature fan-out; no
                          multi-seed retry; no quantization sweep.
```

## §13. Stopping rules (unchanged from v0.1)

```text
hard stops (always applied):
  1. PH5-4 pre-flight refusal — any lock-event hash mismatch aborts
     before any inference.
  2. Manifest schema validation refusal — any non-conformant record
     aborts.
  3. Tokenizer mismatch refusal — runner's tokenizer hash must equal
     the locked tokenizer hash; mismatch aborts.
  4. mlx_lm version mismatch refusal — actual version must equal the
     authorized pin (§7); mismatch aborts.
  5. Model snapshot hash mismatch refusal — actual weights sha256 must
     equal the declared snapshot hash; mismatch aborts.
  6. (Reading B only) Generator hash mismatch refusal — lane1a_prime/
     validation.py sha256 at generation time must equal the authorized
     generator pin (§21); mismatch aborts before L02..L08 generation.
  7. (Reading B only) Per-rung manifest hash mismatch refusal — any
     post-generation manifest sha256 must equal the value computed
     at generation and recorded in the execution_ledger; mismatch on a
     later re-load aborts.

soft stops (recorded; do not abort):
  8. Per-record inference timeout (proposed 60 seconds); record
     INCONCLUSIVE per §15; contributes to the void budget.
  9. Output token count exceeding declared maximum (proposed 32);
     truncated; recorded as void with reason.

completion criteria:
  - All records in the chosen extent have a recorded output (real or
    INCONCLUSIVE).
  - Pre-flight log, A6 re-verification, T1/T3/T4 reports, IVR, and
    execution ledger all written.
```

## §14. Abort rules (unchanged from v0.1; expanded for Reading B)

```text
abort triggers (terminate the run; emit abort ledger; preserve partial
artifacts under d4_a_pilot/aborted_<timestamp>/):

  1. ValidationPreFlightRefused (PH5-4).
  2. ManifestSchemaValidationError.
  3. ModelLoadFailure (snapshot hash mismatch, missing weights, mlx_lm
     import error).
  4. TokenizerMismatch.
  5. Cumulative void budget exceeded (> 5% of records INCONCLUSIVE).
  6. Harness anomaly (uncaught exception; A6 drift exceedance).
  7. (Reading B only) Generator hash mismatch at L02..L08 generation
     time, or per-rung manifest hash inconsistency between generation
     and any later re-load.

abort-record discipline (per E11 / PH5-5 carryover):
  - Aborted runs are RETAINED, not erased.
  - Aborted runs CANNOT be promoted to "successful" D4-A.
  - Any re-attempt requires a new sweep_id; no reuse of an aborted
    sweep_id.
```

## §15. INCONCLUSIVE handling (unchanged from v0.1)

Per sealed INH-2: `INCONCLUSIVE | ELIMINATED | NOT_RULED_OUT` totality.

```text
record-level INCONCLUSIVE triggers:
  - inference timeout
  - output truncation past declared limit
  - parse failure
  - single-record manifest-validation failure

rung-level INCONCLUSIVE triggers:
  - void budget exceeded (> 5%)
  - harness anomaly
  - pre-flight refusal at start

INCONCLUSIVE != ELIMINATED. Per sealed INH-2 K-counter rules,
INCONCLUSIVE rungs are excluded from K. Uncertainty never eliminates;
insufficiency never resolves by retry.
```

## §16. Expected artifacts (unchanged from v0.1)

```text
under experiments/2026-06-11_lane-1a-prime/d4_a_pilot/:
  manifests/                       (Reading B only)
  candidate_outputs/<record_id>.json
  candidate_predictions.json
  pre_flight_log.json
  t1_report.json
  t3_report.json
  t4_report.json
  a6_re_verification.json
  instrument_validation_report.md
  execution_ledger.json
  prompt_template_used.json
```

All artifacts SYNTHETIC / DIAGNOSTIC labeled.

## §17. Post-run verification requirements (unchanged from v0.1)

10 required checks per v0.1 §17. Reading B adds two checks:

```text
11. (Reading B) Generator sha256 in execution_ledger matches the
    authorized pin (§21).
12. (Reading B) Per-rung manifest hashes in execution_ledger are
    self-consistent (manifests at the recorded paths re-hash to the
    recorded values).
```

## §18. Non-claim block (Manager §5 / TL §3 verbatim)

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

## §19. Explicit statements (unchanged from v0.1)

### §19.A — D4 does not activate Claim C

D4-A would establish NONE of: candidate identity, threshold sheet,
stress-test, certification scope. D4-A is an instrument-use step that
checks whether the sealed instrument can drive a real model without
breaking governance, logging, abstention handling, shortcut labeling,
or output discipline.

### §19.B — D4 does not authorize stress-retention testing unless separately named

Stress-retention testing — INT8 / INT4 retention, temperature fan-out,
multi-seed — is OUT OF SCOPE for D4-A. It requires a separate Manager
authorization that names the stress axis explicitly.

If Q2 is declined (per §20.Q2 below), an additional rule binds:

```text
TP criterion inactive by Manager decision.
Run header and every report must state this.
Elimination labels referencing TP cannot fire.
The reduced criteria set is permitted only because Manager chose it
by name.
```

This containment rule is necessary so that the run-1 failure mode
(reduced criteria set without naming) cannot recur under a Q2-decline
D4-A.

---

## §20. Manager D4 Decision Requested (split per TL §2, §3, §4)

### Q1 — Sweep execution authorization

```text
Manager D4 Q1 — sweep execution:

[ ] authorize sweep execution
[ ] decline sweep execution
```

Recommendation (CS, unchanged from v0.1): **authorize sweep execution**
to enable the D4-A pilot. Manager not bound.

### Q1.5 — Sweep_id creation (Q1 supporting authorization)

```text
[ ] authorize sweep_id creation
[ ] decline sweep_id creation
```

Recommendation (CS): **authorize sweep_id creation** if Q1 is granted;
the sweep_id is the provenance carrier for all D4-A artifacts.

### Q1.6 — Model execution (Q1 supporting authorization)

```text
[ ] authorize model execution
[ ] decline model execution
```

Recommendation (CS): **authorize model execution** if Q1 is granted;
D4-A is by definition a model-facing step.

### Q2 — Token-prior generations by-name authorization (TL §4 split correction)

```text
Manager D4 Q2 — token-prior generations:

New Senior recommendation:  GRANT

NS rationale:
  the criterion's separation logic presumes the measured model prior;
  a skewed lexical prior under the format shell can exceed the
  analytical 1/26 without retrieval, weakening exactly the control
  ORC-10 exists to protect.

CS recommendation:          DECLINE for D4-A

CS rationale:
  analytical baseline is sufficient for a governance pilot whose
  purpose is operational, not measurement. D4-A is an instrument-use
  pilot; measured-prior generation belongs in a later measurement
  campaign that names that step explicitly.

Manager decision:

[ ] authorize token-prior generations by name
[ ] decline token-prior generations
```

**If declined** (the CS recommendation):

```text
TP criterion inactive by Manager decision.
Run header must state this verbatim.
Every report (T1, T3, T4, IVR, execution_ledger) must state this.
Elimination labels referencing TP cannot fire.
The reduced criteria set is permitted only because Manager chose it
by name (containment of the run-1 failure mode).
```

**If authorized**:

```text
Token-prior generations would be run before candidate generation,
using a scrambled-binding shell that elicits prior-only behavior; the
measured prior would replace the analytical 1/26 baseline in the TP
difference computation. The runner would record the prior-generation
sweep_id (distinct from the candidate sweep_id) and the prior
predictions in the execution_ledger.
```

### Q3 — D4-A extent decision (TL §3 correction)

```text
Manager D4 Q3 — D4-A extent:

[ ] L01 only / 96 records
    sealed manifests as-is
    no additional rung materialization
    candidate run: 96 inferences
    no generator hash-pin needed (sealed manifests have hash-bound paths)

[ ] L01–L08 / 768 records
    L01 manifests from the sealed surface
    L02–L08 manifests generated at run time from the sealed recipe and
    locked seed
    requires generator hash-pin in the authorization (§21)
    requires per-rung manifest hashes computed at generation and
    written to the execution ledger (§21)
    candidate run: 768 inferences
```

**Reading A recommendation (CS, unchanged from v0.1):** L01 only.
Rationale: first model-facing pilot should be one-rung minimal to
fail-fast on runner / prompt / parser / tokenizer / mlx_lm issues
before committing 768 inferences.

**Reading B note (NS / TL):** L01–L08 is within the sealed declarative
instrument state per the TL SCOPE-B confirmation; no sealed-byte
supersession is required to choose Reading B. The choice is operational
(96 vs 768 inferences) and provenance-pinning (§21 below applies under
Reading B).

Manager chooses the extent by name; no default assumption.

### CS overall recommendation summary

```text
Q1   sweep execution:                  authorize
Q1.5 sweep_id creation:                authorize
Q1.6 model execution:                  authorize
Q2   token-prior generations:          decline
Q3   D4-A extent:                      L01 only (Reading A)
```

Manager not bound; may approve any combination above (or decline all).

---

## §21. Reading B generator hash-pin (TL §7 correction)

If Manager chooses Reading B (Q3 second checkbox), the following
generator pin is in effect for D4-A:

```text
Generator path:              experiments/2026-06-11_lane-1a-prime/lane1a_prime/validation.py
Generator sha256 at HEAD 17f349e:
                              db69519fe84396e7854f80460b41b60c7aeb1ef06948171b7fd91b4c1860bcac

Generation function:         construct_pilot_manifests(recipe)
                              from lane1a_prime.validation

Generation command (per rung):
  python3 -c "
  import json
  from pathlib import Path
  from lane1a_prime.validation import ManifestRecipe, construct_pilot_manifests
  for rung in ('L02','L03','L04','L05','L06','L07','L08'):
      recipe = ManifestRecipe(rung_id=rung, seed=0)
      pilot = construct_pilot_manifests(recipe)
      out_p = Path(f'.../d4_a_pilot/manifests/pilot_manifests_{rung}.json')
      out_p.write_text(json.dumps(pilot))
      # final manifests are byte-identical under the identical-seed
      # property (PH5-3); we materialize a second copy for the A6
      # re-verification API.
      out_f = Path(f'.../d4_a_pilot/manifests/final_manifests_{rung}.json')
      out_f.write_text(json.dumps(construct_pilot_manifests(recipe)))
  "

Locked seed:                 seed=0 (per the sealed recipe; identical
                             across all rungs L01..L08)

Per-rung manifest hashes:    TO BE COMPUTED AT GENERATION TIME by the
                             runner and written to the execution ledger
                             with one line per rung in the form
                               pilot_manifests_L02.json: <sha256>
                               final_manifests_L02.json: <sha256>
                               ...
                             Pilot and final sha256 per rung are
                             expected equal (PH5-3 identical-seed
                             property); any mismatch aborts per §13 hard
                             stop 7.

Generator-state invariant:   the runner aborts before any L02..L08
                             generation if the on-disk
                             lane1a_prime/validation.py sha256 does not
                             equal the authorized generator pin
                             (db69519f...). This prevents silent drift
                             between authorization and execution.

Generator post-generation discipline:
  - Generated manifests live under d4_a_pilot/manifests/, not under
    the sealed validation/ directory.
  - Generated manifests are NOT promoted to the sealed surface unless
    a separate authorization (a sealing extension event) is filed.
  - Per-rung sha256s become part of the D4-A execution_ledger and any
    D4-A IVR; they are NOT part of the sealed LOCK-RECORD v1.0.
```

Under Reading A, §21 is inactive; only L01 (already sealed) is in
scope and no generator pin is needed.

---

## Appendix A — Reading order for D4 review (unchanged from v0.1)

1. Start here: this packet (§1–§21).
2. `LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` (`51e18fa9…`)
3. `MANAGER-LOCK-RECORD-SEALING-AUTHORIZATION-2026-06-11.md` (`fbc34b12…`)
4. `MANAGER-D3-AUTHORIZATION-2026-06-11.md` (`802439a7…`)
5. `PH5-1-JOINT-LOCK-EVENT-RECORD-v0.2.md` (`264cc47e…`)
6. `PHASE5-v0.2-CORRECTIVE-RUN3-COMPLETION-SUMMARY.md` (`9655b8c5…`)

## Appendix B — Standing carry (non-authorizations, verbatim)

This v0.2 readiness packet does not authorize: D4 sweep authorization;
D5 close-out; model runs; model loading; new sweep_id; sweep
execution; token-prior model generations; scrambled-binding model
generations; candidate/model outputs; candidate selection; ranking;
threshold work; certification evaluation; stress-retention testing;
Claim C activation; public benchmark packaging.

All model-touching and sweep-execution gates remain CLOSED until
Manager separately approves them by name via §20.

**D4 token-prior authorization slot: PENDING / UNOPENED.**

— CS Engineer, 2026-06-11
