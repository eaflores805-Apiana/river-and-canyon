# Lane 1a' Prime — D4-B Readiness / Authorization Packet (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
D4-B READINESS PREPARATION ONLY — NO D4-B AUTHORIZATION REQUESTED OUTSIDE §20
SEALED LOCK-RECORD v1.0 UNCHANGED · D4-A RECORD UNMUTATED
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
D4 TOKEN-PRIOR SLOT: PENDING / UNOPENED (D4-B proposes opening it)
```

*v0.1 (post Manager D4-A acceptance + close-out direction 2026-06-11):
proposes the successor minimal operational pilot — L01 again, same
sealed instrument, **token-prior generations ACTIVE** as the empirical
question — under explicit Manager authorization. All other axes held
constant relative to D4-A (one model, bf16, single greedy pass, no
L02–L08, no quantization, no INT8/INT4, no Claim C). The TP-banner
emitter fix accepted by Manager at commit `5c60fbd` is the runner
baseline; D4-B emissions would carry the symmetric ACTIVE banner form
across every report.*

To: Manager (decision) · Cc: Team Lead, New Senior Engineer, Senior Engineer
From: CS Engineer (joint packet; NS counter-signature awaited)
Date: 2026-06-11
Re: Manager §4 successor D4 preparation per close-out direction

---

## §1. Purpose

Per Manager §5 (close-out direction memo) verbatim:

> D4-A already showed that L01 can run operationally under the sealed
> instrument with TP inactive. The cleanest next empirical question is
> whether the same narrow surface remains NOT_RULED_OUT when TP is
> active.

D4-B exists to answer that one question. It does not expand the
surface, the precision rung, or the criteria set beyond what D4-A
already crossed; it activates one criterion (TP) and re-runs the same
operational pilot.

## §2. Sealed LOCK-RECORD anchor (unchanged)

| field | value |
|---|---|
| Path | `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` |
| sha256 | `51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935` |
| Status | SEALED · UNCHANGED |

The sealed instrument anchors D4-B exactly as it anchored D4-A. No
supersession is requested or implied.

## §3. Proposed model identity (unchanged from D4-A)

```text
Family:         Qwen2.5
Variant:        Qwen2.5-3B-Instruct
Precision rung: bf16 (unquantized; mlx native)
Tokenizer:      Qwen2 tokenizer (single lane tokenizer)
```

Same model as D4-A. No model-family axis. No precision-axis change.

## §4. Proposed model snapshot / provenance (unchanged from D4-A)

```text
Canonical snapshot hash (runner-provenance-backed):
  sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20

Local HF cache revision:
  aa8e72537993ba99e69dfaafa59ed015b17504d1

Runtime verification:
  Runner replays B1 v2 compute_model_snapshot_hash routine.
  Aborts on any mismatch (per Manager §6 abort rule from D4-A authorization).
```

## §5. Proposed runner

| field | value |
|---|---|
| Runner path | `experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py` |
| Current sha256 (TP-banner future-run fix applied) | `1d6f7085c8ed6b5d4ebb023a008ccb1c8e1cf2d156bf32f0705870c9d11a31dc` |
| Manager-accepted future-run fix locus | `tp_banner_block` helper + propagation across 6 emission envelopes |

The runner already implements the symmetric Q2-authorized banner form
(see `test_tp_banner_block_q2_authorized_has_required_fields` and
`test_tp_banner_propagates_into_simulated_emission_envelopes`). Under
D4-B, the emitted banner would read:

```json
{
  "tp_criterion_status": "ACTIVE",
  "tp_inactivity_authority": "n/a (Manager authorized TP generations for this run)",
  "tp_generation_status": "RUN (authorized)",
  "tp_elimination_labels_enabled": true
}
```

Two D4-B-specific runner additions would need to be authored under
the D4-B execution authorization (NOT under this readiness packet):

```text
1. TP generation step:
   - Iterate the sealed L01 manifests under a TP-shell prompt (see §7).
   - Produce a per-record "control_token_prior" prediction.
   - Aggregate into a TP control accuracy distribution.

2. T3 evaluation with TP ACTIVE:
   - Use the measured TP control distribution (instead of the
     analytical 1/26 baseline used in D4-A's TP-INACTIVE evaluation)
     in the Newcombe-Wilson difference computation for the
     accuracy_indistinguishable_from_token_prior criterion.
   - Apply the locked T3 bound 0.10 verbatim.
   - If the difference CI upper bound < 0.10, attach the TP label and
     the candidate is ELIMINATED.
```

## §6. Quantization state (unchanged from D4-A)

```text
proposed precision rung:  bf16 (unquantized)
quantization stress:      NONE
INT8 / INT4:              OUT OF SCOPE
```

## §7. Token-prior generation method (proposed; subject to Manager review)

**The TP measurement method must not be scrambled-binding** (Manager
§6 of close-out direction memo prohibits scrambled-binding generations
in this lane until separately named). CS proposes the following
NO-BINDINGS SHELL:

```text
TP shell description:
  Use the same prompt template (prompt_template_v1.json) but render
  the pair list as EMPTY. The model receives:
    System: <same as D4-A>
    User:   "Pairs:\n\nQuery: <queried_key>"
  The model has no pair context to retrieve from, so any non-NONE
  response is a prior-only emission over the visible VALUE_POOL.

Why this is NOT "scrambled-binding":
  No bindings are scrambled; no bindings exist in the prompt at all.
  The shell strictly mirrors what an ORC-06 token_prior_emitter
  oracle does in the synthetic harness: emit a value with no
  retrieval substrate.

What it measures:
  The candidate's prior-only distribution over VALUE_POOL given the
  D4-A prompt structure, queried key, and decoding parameters. The
  expected control accuracy under perfect uniformity over the 26
  values is 1/26 ≈ 0.038.

How it is used in the TP criterion:
  TP control accuracy = (TP-shell correct predictions) / n_answerable
  Candidate accuracy   = (D4-A-style retrieval-shell correct) / n_answerable
  Newcombe-Wilson CI on (candidate − control); fires iff CI upper < 0.10.

Sweep_id:
  Distinct sweep_id for the TP-shell sweep (proposed format:
  lane1a-prime-d4b-tp-YYYYMMDD-HHMMSS-<random6>).
  The candidate retrieval-shell sweep uses its own sweep_id
  (proposed: lane1a-prime-d4b-cand-YYYYMMDD-HHMMSS-<random6>).
  Both sweep_ids recorded in the execution_ledger.
```

If Manager prefers a different TP shell (e.g., a different masking
approach), CS implements the Manager-specified method. The "no-bindings
shell" above is a proposal, not an assertion.

## §8. Other axes (unchanged from D4-A)

| axis | D4-A | D4-B (proposed) |
|---|---|---|
| Extent | L01 only / 96 records | **L01 only / 96 records (same)** |
| Pre-flight refusal | PH5-4 + sealed LOCK-RECORD + manifest hash + version pin + snapshot hash | **same six-way check** |
| mlx_lm pin | 0.31.3 (Manager Option A substitution from packet 0.19.3) | **0.31.3 (carry the Option A substitution forward; provenance reference preserved)** |
| Decoding | greedy; temp 0; max_new_tokens 32; seed 0 | **same** |
| Stopping rules | 5 hard stops + 2 soft stops | **same** |
| Abort rules | 6 categories with retention discipline | **same** |
| INCONCLUSIVE handling | per sealed INH-2; 5% void budget | **same** |
| Output dir | `d4_a_pilot/` | **`d4_b_pilot/`** (parallel; sealed `validation/` untouched) |
| TP banner | INACTIVE form (D4-A; named deviation; closed) | **ACTIVE form, symmetric** (per the accepted future-run fix) |

## §9. D4-B execution constraints (would carry forward from D4-A)

```text
sealed LOCK-RECORD v1.0 unchanged
D4-B L01-only extent
approved model identity and snapshot
approved exact framework pin (0.31.3, per Option A carryforward)
approved runner/provenance controls
approved output directory (d4_b_pilot/)
approved sweep_id format
one pass per shell (candidate + TP control = two single-pass sweeps,
  same extent, distinct sweep_ids)
no retries
no adaptive continuation
no added items
abort on pre-flight hash refusal
abort on A6 drift exceedance
abort on schema validation failure
abort on artifact hash mismatch
abort on runner/model identity mismatch
abort on unhandled exception
```

## §10. Expected D4-B artifacts (under d4_b_pilot/)

```text
experiments/2026-06-11_lane-1a-prime/d4_b_pilot/
  ├── candidate_outputs/             (96 retrieval-shell outputs)
  ├── tp_control_outputs/            (96 no-bindings-shell outputs)
  ├── candidate_predictions.json
  ├── tp_control_predictions.json
  ├── pre_flight_log.json            (with ACTIVE TP banner)
  ├── t1_report.json                 (with ACTIVE TP banner)
  ├── t3_report.json                 (with ACTIVE TP banner; TP criterion
                                      now evaluated against measured control)
  ├── t4_report.json                 (with ACTIVE TP banner; D4B rows added)
  ├── a6_re_verification.json        (with ACTIVE TP banner)
  ├── instrument_validation_report.md (with ACTIVE TP banner block)
  └── execution_ledger.json          (with ACTIVE TP banner; both sweep_ids;
                                      tp_generation_status: RUN (authorized);
                                      tp_elimination_labels_enabled: true)
```

All artifacts SYNTHETIC / DIAGNOSTIC labeled.

## §11. Non-claim block (Manager § verbatim, carries to D4-B)

> D4-B, if approved, would be an instrument-use step, not a capability
> claim.
>
> D4-B would not establish: model capability, model incapability,
> task-family viability, candidate suitability, certification
> readiness, retention-under-compression, Claim C progress, seam
> evidence, or public benchmark status.
>
> D4-B does not authorize: D5 close-out (D5 prep is a separate
> deliverable); quantization stress; INT8 / INT4; stress-retention
> testing; candidate selection; ranking; threshold work; certification
> evaluation; Claim C activation; public benchmark packaging.
>
> The instrument may rule out; it may not rule in.
>
> Passing the declared battery is reportable only as "not explained
> by the declared shortcut battery," never as "not shortcut-driven."
>
> We have improved the ruler; we are only beginning to touch the
> territory.

### What a D4-B NOT_RULED_OUT result would mean

```text
"The instrument did not attach any elimination label under the active
SIX-criterion set (including the now-measured TP control)."

This is a strictly stronger statement than the D4-A bounded result,
because TP is no longer inactive. It would establish:
  - The candidate's retrieval-shell accuracy is separated from its
    no-bindings prior emission by more than the locked 0.10 margin
    (otherwise TP fires).
  - The other four active criteria continue to pass.

It would still NOT establish: model capability, task-family viability,
certification readiness, retention-under-compression, Claim C, seam
evidence, or public benchmark status. The bounded language above
remains binding.
```

### What a D4-B ELIMINATED result would mean

```text
"The instrument attached an elimination label under the active
six-criterion set."

This would establish only that, on the L01 surface and under this
specific candidate / model / scale / construction / shell, the
instrument fired one or more eliminative criteria. It would NOT
establish: model incapability across the task family; that the
candidate is incapable in general; or that the instrument's threshold
is correctly calibrated for any other surface.

It would also activate the constructibility-risk carryforward
discussion (Contributor 5 + NS deliverable) more concretely: a
non-certification at D4-B is one of three possible explanations
(miscalibration / gate defect / genuine barrier).
```

## §12. Successor-gate status (unchanged from D5 close-out)

| gate | status |
|---|---|
| D5 acceptance (D4-A close-out) | Manager decision pending; D5 packet filed (CS) |
| Constructibility-risk note | Contributor 5 + NS deliverable; awaiting their filing |
| D4-B execution | NOT REQUESTED outside §20 below |
| L02–L08 execution | NOT REQUESTED |
| Quantization stress / INT8 / INT4 | NOT REQUESTED |
| Stress-retention testing | NOT REQUESTED |
| Candidate selection / ranking | NOT REQUESTED |
| Threshold work / certification | NOT REQUESTED |
| Claim C activation | NOT REQUESTED |
| Public benchmark packaging | NOT REQUESTED |

---

## §20. Manager D4-B Decision Requested (4-way split per Manager §4)

```text
Manager D4-B Decision Requested:

[ ] authorize model execution
[ ] decline model execution

[ ] authorize sweep_id creation
[ ] decline sweep_id creation

[ ] authorize L01 sweep execution
[ ] decline L01 sweep execution

[ ] authorize token-prior generations by name
[ ] decline token-prior generations
```

### CS recommendation (Manager not bound)

```text
[X] authorize model execution
[ ] decline model execution

[X] authorize sweep_id creation
[ ] decline sweep_id creation

[X] authorize L01 sweep execution
[ ] decline L01 sweep execution

[X] authorize token-prior generations by name
[ ] decline token-prior generations
```

Rationale: this is the narrow successor empirical question Manager
identified in §5 of the close-out direction memo. Authorizing all four
permissions for D4-B at L01 only honors the "cleanest next empirical
question" framing. Manager may approve any subset (or none).

### Partial-approval handling

```text
If Q4 (token-prior generations) is APPROVED but Q1-Q3 are not, D4-B
cannot run — model execution + sweep + sweep_id are all required to
produce the TP control sweep.

If Q1-Q3 are APPROVED but Q4 is DECLINED, the run would be a literal
re-run of D4-A under the patched runner (now banner-correct) but with
TP still INACTIVE — CS would proceed only if Manager explicitly
intends this; otherwise CS would file a clarification request, since
a D4-A re-run is a different experiment than the D4-B that this
packet proposes.

CS recommends the all-four-authorize path or all-four-decline; the
mixed paths are flagged for Manager awareness.
```

---

## Appendix A — Reading order for D4-B review

1. This packet (§1–§20).
2. `LANE1A-PRIME-D4A-PILOT-RETURN-v0.1.md` (sha256 `0b230e03…`) for the
   D4-A run record this packet builds on.
3. `LANE1A-PRIME-D4A-D5-CLOSEOUT-PACKET-v0.1.md` (filed alongside this
   packet) for the D4-A close-out posture.
4. `LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` (sha256 `51e18fa9…`) for
   the sealed instrument anchor.
5. `CS-D4A-TP-BANNER-DEVIATION-ACK-AND-FIX-PLAN-v0.1.md` for the
   runner fix that D4-B's emissions would inherit.
6. `CONSTRUCTIBILITY-RISK-CARRYFORWARD-NOTE-v0.1.md` — Contributor 5 +
   NS deliverable (when filed) for the constructibility framing.

## Appendix B — Standing carry (non-authorizations, verbatim)

This D4-B readiness packet does not authorize: D4-B execution; D5
acceptance; L02–L08 execution; scrambled-binding generations;
quantization stress; INT8 / INT4; stress-retention testing; candidate
selection; ranking; threshold work; certification evaluation; Claim C
activation; public benchmark packaging.

All model-touching and sweep-execution gates remain CLOSED until
Manager separately approves them by name via §20.

**D4 token-prior authorization slot: PENDING / UNOPENED** (D4-B
proposes opening it; Manager decides).

— CS Engineer, 2026-06-11
