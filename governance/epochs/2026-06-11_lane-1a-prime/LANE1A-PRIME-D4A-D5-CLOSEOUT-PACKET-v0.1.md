# Lane 1a' Prime — D4-A → D5 Close-Out Packet (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
D5 CLOSE-OUT PREPARATION ONLY — D5 ACCEPTANCE NOT REQUESTED HERE
SEALED LOCK-RECORD v1.0 UNCHANGED · D4-A OUTPUTS UNMUTATED
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
D4 TOKEN-PRIOR SLOT: PENDING / UNOPENED
```

To: Manager (decision) · Cc: Team Lead, New Senior Engineer, Senior Engineer
From: CS Engineer (joint package; NS counter-signature awaited per Manager §2)
Date: 2026-06-11
Re: Manager §2 9-item D5 close-out packet for D4-A

CS files the D5 close-out packet for the accepted D4-A pilot. The
packet records the D4-A result in the Manager-required bounded form,
preserves the full non-claim block, summarizes the named deviation
and the future-run emitter fix, and ends with a CS recommendation on
D5 acceptance. The packet does not request D5 acceptance; it furnishes
the evidence base for the Manager decision.

---

## §1. Execution summary

```text
Lane:                  Lane 1a' Prime
Decision phase:        D4-A minimal operational pilot
Authorization:         Manager 2026-06-11 (Q1 sweep + Q1.5 sweep_id +
                       Q1.6 model exec all authorized; Q2 token-prior
                       declined; Q3 extent L01 only / 96 records)
Execution date:        2026-06-11
sweep_id:              lane1a-prime-d4a-20260611-201722-ymbngp
Records:               96 (80 answerable + 16 NULL)
Inferences:            96/96 completed in 39.7 s
Runner:                lane1a_runner.py
Model:                 Qwen2.5-3B-Instruct (bf16, unquantized)
Precision:             bf16 (Apple Silicon / mlx native; no quantization)
mlx_lm:                0.31.3 (Manager Option A pin substitution from packet 0.19.3)
Decoding:              greedy (temperature 0; max_new_tokens 32; single pass)
TP criterion:          INACTIVE BY MANAGER DECISION (Q2 declined; reduced
                       criteria set permitted only because Manager named it)
Result:                NOT_RULED_OUT (no elimination label attached;
                       five active criteria all passed)
Named deviation:       report-emitter completeness defect — TP banner
                       absent from T1/T4/A6 JSONs at emit (banner-equivalent
                       fields present in execution_ledger, T3, IVR);
                       lifecycle CLOSED 2026-06-11
Future-run emitter fix: applied to runner (commit 5c60fbd); 5 unit tests
                       added; full suite 252 passed; fix applies only to
                       successor authorized runs
Sealed LOCK-RECORD:    v1.0 sha256 51e18fa9... UNCHANGED before, during,
                       and after the D4-A run; re-verified at this filing
```

## §2. Verified artifact list and hashes

### D4-A run outputs (UNMUTATED; sha256 re-verified at this filing)

| artifact | sha256 |
|---|---|
| `d4_a_pilot/pilot_manifests_*` (sealed; consumed read-only) | `afe0e545c318132a5821e6d02ba3f41093c05ce7a2623a120d0088e03b29b09f` (pilot and final identical, sealed) |
| `d4_a_pilot/pre_flight_log.json` | `ebda4737c9c97c752475f8d44e582f28eca8c3fc10c907fdb7d5c16bc493281d` |
| `d4_a_pilot/candidate_predictions.json` | `ba276b0539a4e7eed6662ea586c94aa0adc6a54ecaa92a0fd5c6540b3d170b76` |
| `d4_a_pilot/t1_report.json` | `ebe0a95246a5dfc474fab7e5543a34e63ed50c988815b5185a38fdad4ab3aa6d` |
| `d4_a_pilot/t3_report.json` | `a4e0236bfd6a85e57472911cb9f51566212984ebfbc65579c91d1295666d0a1f` |
| `d4_a_pilot/t4_report.json` | `6d265d25d1bd6852afa34fc1eb95680395fc82e1b993698a584f81a23fd29067` |
| `d4_a_pilot/a6_re_verification.json` | `3c2e09b18e609e4fd2ab8513d6af6f74a55c13a19f98d56d217ed763c7d771ab` |
| `d4_a_pilot/execution_ledger.json` | `f75db02c3080939fb60a6be9a22d3010b5c1e26ffec35b1a43acd7a5ebd08a0f` |
| `d4_a_pilot/instrument_validation_report.md` | `7510c06a6dcddf09c8fe17c6fb3bf2993d351d4306ed3c7cb624f0225b449c42` |
| `d4_a_pilot/candidate_outputs/*` (96 files) | individual sha256 per file; aggregate set unchanged since commit `2cc0c1f` |

### Runner & supporting files (D4-A run-of-record)

| artifact | sha256 (run-of-record) |
|---|---|
| `d4_runner/lane1a_runner.py` | `5beba944f91fee64ab58e659d13af603f25a420ffce671e3b223204abbe59e60` |
| `d4_runner/parse_model_output.py` | `fbdf989cdb8f258b7b2e18000835aafd9814a195b3eae0d73f540c08d35a1180` |
| `d4_runner/preconditions.json` | `d3ad098c8d67ab765622f2d3ae6a768c18de40e71db54e1dba3a2c848cf7c9ba` |
| `d4_runner/decoding_config.json` | `a20391d89972d47c0b231f5c6da9f8a9f4c7be8c975ab98bd95a32327196f803` |
| `d4_runner/prompt_template_v1.json` | `f1956e7dd43f165c8707fe88bc11757888f108e7e9766aa186ac9fc04f8b368a` |

(Note: the runner file was subsequently patched for the future-run TP-banner fix; current `lane1a_runner.py` sha256 is `1d6f7085c8ed6b5d4ebb023a008ccb1c8e1cf2d156bf32f0705870c9d11a31dc`. The D4-A execution_ledger `runner_hash` field permanently records the run-of-record sha256 `5beba944…`; the patch does NOT mutate the run record.)

### Lock-event anchors (UNCHANGED)

| artifact | sha256 |
|---|---|
| `LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` | `51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935` |
| `ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5` |
| `T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39` |
| `STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5` |

### Governance memos (D4-A track)

| memo | sha256 |
|---|---|
| `MANAGER-D3-AUTHORIZATION-2026-06-11.md` | `802439a712149afd51f46e32c0889bb9cf8c3f725c76c215ced35bc25bcc7c9e` |
| `MANAGER-LOCK-RECORD-SEALING-AUTHORIZATION-2026-06-11.md` | `fbc34b12a366e2c5f9a46bf2db80b1e24fddb8998a9b1b88bfac6a841a066562` |
| `LANE1A-PRIME-D4-READINESS-PACKET-v0.2.md` | `cb0b0c5ed9b2f6e64b3bad521f9e54aa2cb121d4b366cdf010f0ba6e3c2ab6bd` |
| `CS-D4-READINESS-RUNTIME-SLOTS-v0.2.md` | `c2e85e9f73ed3db91a4a739c9c27bb80e049468bae7b0a2ca19fa49b0fd9973d` |
| `CS-D4A-PRE-EXECUTION-BLOCKERS-v0.1.md` | `3ad93907c5038d8db287b5a76275fd88fb851c31f1b2bec1d0594bf54dae8a99` |
| `CS-D4A-MLX-LM-PIN-SUBSTITUTION-2026-06-11.md` | `cb7f210b14ee2d7e4f05f2b56fa1f409d5420a0f8107377cf9a2de3f59e3ede2` |
| `LANE1A-PRIME-D4A-PILOT-RETURN-v0.1.md` | `0b230e036be984a24c610cafaa9bdc3e6a11ed6053f8ba58a4f0547251916979` |
| `CS-D4A-TP-BANNER-DEVIATION-ACK-AND-FIX-PLAN-v0.1.md` | `4beeefb37e988430f3456ca90913214547c318c46ae5230aef631e731c4df00e` |

Verification method: sha256 over each path's bytes via Python
`hashlib.sha256().hexdigest()`. All re-computed at this filing match
the committed values.

## §3. Bounded result language (Manager §2 verbatim)

> The instrument did not attach any elimination label under the
> active five-criterion set.

Accepted interpretation:

> not explained by the declared shortcut battery

Forbidden interpretations (verbatim Manager §5 of acceptance memo):

```text
model passed
capability established
not shortcut-driven
candidate certified
task family viable
Claim C progressed
seam evidence
public benchmark result
```

This language binds D4-A in this packet, in the D4-A IVR, in the D4-A
pilot return, and in any future governance memo that references the
D4-A result.

### D4-A objective data (factual; presented under the bounded language above)

| stratum / measure | value |
|---|---|
| n_answerable | 80 |
| answerable_correct | 80 |
| answerable_accuracy | 1.0000 |
| answerable_abstained | 0 |
| answerable_abstention_rate | 0.0000 |
| n_null | 16 |
| null_abstained | 16 |
| null_abstention_rate | 1.0000 |
| parse_failures | 0 |
| void_rate | 0.0000 |
| attached_labels | (empty) |
| outcome | NOT_RULED_OUT |

| criterion | result vs candidate |
|---|---|
| null_abstention_floor_unmet | PASSED |
| answerable_abstention_ceiling_exceeded | PASSED |
| **accuracy_indistinguishable_from_token_prior** | **INACTIVE BY MANAGER DECISION** |
| accuracy_indistinguishable_from_declared_policy_envelope | PASSED |
| insufficient_measurement_headroom | PASSED |
| strict_content_gap_instability | PASSED |

The reduced criteria set was permitted ONLY because Manager named the
Q2 token-prior decline — containment of the run-1 failure mode is
preserved.

## §4. Named deviation summary

```text
Deviation class:     report-emitter completeness defect
Locus:               T1, T4, A6 JSON emissions lacked TP inactive-by-decision banner
Manager disposition: accepted with named deviation (no HOLD)
                     verbatim: "D4-A result accepted with named deviation"
Authoritative records that DID carry banner-equivalent fields:
                     execution_ledger, T3 report, IVR
No-post-hoc-mutation rule:
                     Manager §3 of TP-banner deviation disposition
                     verbatim: "No post-hoc mutation of run outputs authorized"
Closure:             Manager 2026-06-11 — TP-banner deviation lifecycle CLOSED
Closure commit:      5c60fbd2c26962f11766ec93b06572b03f16aea8 (runner patch +
                     test + ack memo)
```

The deviation is carried visibly here and in `LANE1A-PRIME-D4A-PILOT-RETURN-v0.1.md`
as the operative form of "named deviation." No retroactive normalization
of D4-A outputs occurred. The D4-A run record stands exactly as emitted.

## §5. Future-run emitter fix summary

```text
Fix surface:         experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py
Patched sha256:      1d6f7085c8ed6b5d4ebb023a008ccb1c8e1cf2d156bf32f0705870c9d11a31dc
                     (current at HEAD; differs from D4-A run-of-record
                     runner sha256 5beba944... by intent — the run-of-record
                     ledger is immutable)
Helper:              tp_banner_block(token_prior_authorized, authority_ref)
Required fields:     tp_criterion_status
                     tp_inactivity_authority
                     tp_generation_status
                     tp_elimination_labels_enabled
Propagation surface: pre_flight_log, t1_report, t3_report, t4_report,
                     a6_re_verification, execution_ledger
                     (banner embedded at TOP LEVEL of each)
Symmetric case:      Q2-authorized future runs emit the symmetric ACTIVE
                     banner form (tp_criterion_status=ACTIVE; labels enabled)
Test file:           experiments/2026-06-11_lane-1a-prime/tests/test_d4_runner_tp_banner.py
                     sha256 d4ac402427a14e6c6eac3a9cec1d0c1451978b4437b245c45135412f74095c7e
Tests added:         5
Test result:         5/5 PASS within full suite 252 PASS
Scope:               fix applies only to FUTURE authorized D4 runs
                     (Manager §4 of TP-banner deviation acceptance)
```

## §6. No-output-mutation confirmation

**CONFIRMED.** Verification method (decisive, per NS verification memo):

```text
git diff --name-only 2cc0c1f..5c60fbd

Result: exactly three files changed —
  experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py
  experiments/2026-06-11_lane-1a-prime/tests/test_d4_runner_tp_banner.py
  governance/2026-06-11_lane-1a-prime/CS-D4A-TP-BANNER-DEVIATION-ACK-AND-FIX-PLAN-v0.1.md

Not one file under experiments/2026-06-11_lane-1a-prime/d4_a_pilot/
was touched. Therefore every D4-A output (96 raw outputs,
pre_flight_log, candidate_predictions, T1/T3/T4 reports,
a6_re_verification, execution_ledger, IVR) is unchanged not merely by
re-hash but by the absence of any commit touching it.
```

Additionally, at the time of THIS packet filing, CS re-verified each of
the 6 D4-A artifact sha256s above against the bytes on disk: all match
verbatim. Re-verified the sealed LOCK-RECORD sha256: matches.

## §7. Non-claim block (Manager §10 / §6 verbatim carry)

> D4-A is an instrument-use step, not a capability claim.
>
> D4-A does not establish: model capability, model incapability,
> task-family viability, candidate suitability, certification
> readiness, retention-under-compression, Claim C progress, seam
> evidence, or public benchmark status.
>
> D4-A does not authorize: D5 close-out (this packet only prepares it),
> quantization stress, INT8 / INT4, stress-retention testing, candidate
> selection, ranking, threshold work, certification evaluation,
> Claim C activation, or public benchmark packaging.
>
> The instrument may rule out; it may not rule in.
>
> Passing the declared battery is reportable only as **"not explained
> by the declared shortcut battery,"** never as "not shortcut-driven."
>
> We have improved the ruler; we are only beginning to touch the
> territory.

## §8. Successor-gate status

| gate | status |
|---|---|
| D5 acceptance | NOT REQUESTED HERE (this packet prepares; Manager decides) |
| Successor D4 execution (e.g., D4-B with TP active) | NOT REQUESTED — see successor readiness packet `LANE1A-PRIME-D4B-READINESS-PACKET-v0.1.md` (filed separately) |
| L02–L08 execution | NOT REQUESTED |
| Token-prior generations | NOT REQUESTED HERE (any future authorization is a separate Manager decision; readiness packet for D4-B carries the Q2 request explicitly per §4 of Manager direction) |
| Quantization stress / INT8 / INT4 | NOT REQUESTED |
| Stress-retention testing | NOT REQUESTED |
| Candidate selection / ranking | NOT REQUESTED |
| Threshold work / certification evaluation | NOT REQUESTED |
| Claim C activation | NOT REQUESTED |
| Public benchmark packaging | NOT REQUESTED |
| **D4 token-prior authorization slot** | **PENDING / UNOPENED** |
| Sealed LOCK-RECORD v1.0 | UNCHANGED |

All successor execution gates remain CLOSED until Manager separately
approves them by name.

## §9. CS recommendation on D5 close-out acceptance

CS recommendation: **D5 close-out for D4-A MAY BE ACCEPTED** under the
bounded result language and the named-deviation discipline already on
record.

### Rationale (presented under the non-claim block)

1. **Substantive integrity of the run is preserved.** All
   Manager-required preconditions PASSED at runtime (PH5-4 lock-event
   hashes, sealed LOCK-RECORD hash, sealed manifest hashes, mlx_lm
   version match, model snapshot hash match via the B1 v2
   runner-provenance routine). No unauthorized execution occurred at
   any point.

2. **The named deviation is contained.** The TP-banner emission gap on
   T1/T4/A6 JSONs is documented, dispositioned by Manager as
   "report-emitter completeness defect (not a HOLD)," ack-ed by CS,
   fixed forward in the runner with test coverage, and the lifecycle
   is CLOSED. The deviation is visible in the record, not buried.

3. **No-post-hoc-mutation rule has been honored.** The D4-A run record
   stands exactly as emitted; the future-run fix touches no D4-A
   artifact. NS independently verified this by `git diff --name-only`.

4. **The bounded result language is binding.** The D4-A result is
   carried forward only as "not explained by the declared shortcut
   battery" — no overreach into capability, certification, viability,
   stress-retention, Claim C, seam, or benchmark.

5. **The sealed instrument is preserved.** The sealed LOCK-RECORD v1.0
   is byte-identical to its sealing-event state. Any future
   authorized D4 successor run can anchor against the same sealed
   surface.

6. **Constructibility-risk carryforward** (per Manager §3 of the
   close-out direction memo) is being prepared by Contributor 5 + NS
   as the next deliverable in sequence. That note preserves the
   first-class outcome possibility of "genuine constructibility
   barrier at model/task/scale" and is referenced by this close-out
   packet as a companion artifact.

CS does not request D5 acceptance. The recommendation above is offered
under the standard CS-recommend / NS-counter / TL-filter / Manager-decide
governance chain.

### What D5 acceptance would NOT establish

```text
Not model capability.
Not model incapability.
Not task-family viability.
Not candidate suitability.
Not certification readiness.
Not retention-under-compression.
Not Claim C progress.
Not seam evidence.
Not public benchmark status.
Not authorization for any successor model-facing work.
```

D5 acceptance would establish that the D4-A operational pilot's
documentation and disposition trail are complete on the lane's terms.
It is a procedural close-out, not an evidentiary uplift.

---

## Appendix A — Reading order for D5 review

1. This packet (§1–§9) for the consolidated close-out view.
2. `LANE1A-PRIME-D4A-PILOT-RETURN-v0.1.md` (sha256 `0b230e03…`) for the
   D4-A run record's 22-item return.
3. `CS-D4A-TP-BANNER-DEVIATION-ACK-AND-FIX-PLAN-v0.1.md` (sha256
   `4beeefb3…`) for the deviation lifecycle.
4. `LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` (sha256 `51e18fa9…`) for
   the sealed instrument anchor.
5. `CONSTRUCTIBILITY-RISK-CARRYFORWARD-NOTE-v0.1.md` — to be filed by
   Contributor 5 + NS per Manager §3.
6. `LANE1A-PRIME-D4B-READINESS-PACKET-v0.1.md` — successor preparation
   only (CS files separately per Manager §4).

## Appendix B — Standing carry (non-authorizations, verbatim)

This D5 close-out packet does not authorize: D5 acceptance; successor
D4 execution; L02–L08 execution; token-prior model generations;
scrambled-binding model generations; quantization stress; INT8 / INT4;
candidate selection; ranking; threshold work; certification
evaluation; stress-retention testing; Claim C activation; public
benchmark packaging.

All successor model-facing gates remain CLOSED until Manager
separately approves them by name.

**D4 token-prior authorization slot: PENDING / UNOPENED.**

— CS Engineer, 2026-06-11
