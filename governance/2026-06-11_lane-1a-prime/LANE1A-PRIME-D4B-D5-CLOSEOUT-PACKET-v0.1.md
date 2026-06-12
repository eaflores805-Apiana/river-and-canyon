# Lane 1a' Prime — D4-B → D5 Close-Out Packet (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
D5-B CLOSE-OUT PREPARATION ONLY — D5-B ACCEPTANCE NOT REQUESTED HERE
SEALED LOCK-RECORD v1.0 UNCHANGED · D4-A AND D4-B RUN-OF-RECORD UNMUTATED
NO MODEL INVOKED · NO MODEL LOADED · NO NEW SWEEP_ID · NO SWEEP EXECUTION
NO ADDITIONAL TOKEN-PRIOR GENERATIONS
```

To: Manager (decision) · Cc: Team Lead, New Senior Engineer, Senior Engineer, Contributor 5
From: CS Engineer (joint packet; NS counter-signature awaited per Manager §2)
Date: 2026-06-11
Re: Manager §3 13-item D4-B → D5 close-out packet

CS files the D5-B close-out packet for the accepted D4-B pilot. The
packet records the D4-B result in the Manager-required bounded form,
preserves the full non-claim block, summarizes the active six-criterion
posture with the measured token-prior control, restates D4-B's
relationship to D4-A, references the to-be-filed constructibility-risk
note as an interpretation guard, and ends with a CS recommendation on
D5-B acceptance. The packet does not request D5-B acceptance; it
furnishes the evidence base for the Manager decision.

This packet leads — per Manager §4 — with the accepted bounded
language:

> **The instrument did not attach any elimination label under the
> active six-criterion set.**
>
> Accepted bounded interpretation:
> **The result was not explained by the declared shortcut battery or
> by the candidate's own measured token prior.**

This is the strongest permitted interpretation; CS does not strengthen
it.

---

## §1. Execution summary

```text
Lane:                  Lane 1a' Prime
Decision phase:        D4-B L01 token-prior-active pilot
Authorization:         Manager 2026-06-11 (all four Q boxes authorized:
                       model execution + sweep_id creation +
                       L01 sweep execution + token-prior generations
                       by name; method `unconditioned_token_prior`)
Execution date:        2026-06-11
Candidate sweep_id:    lane1a-prime-d4b-cand-20260611-220303-ueitv3
TP control sweep_id:   lane1a-prime-d4b-tp-20260611-220303-bt29ky
Records:               96 (80 answerable + 16 NULL), sealed L01 — read-only
Inferences:            192 total
                         96 candidate retrieval-shell (prompt_template_v1.json)
                         96 TP control no-bindings-shell (prompt_template_v1_tp.json)
Total elapsed:         61.4 s
Runner:                lane1a_runner_d4b.py
Model:                 Qwen2.5-3B-Instruct (bf16, unquantized)
Precision:             bf16 (mlx native)
mlx_lm:                0.31.3 (Option A pin substitution carried forward from D4-A)
Decoding:              greedy (temperature 0; max_new_tokens 32; single pass)
TP criterion:          ACTIVE BY MANAGER DECISION (Q4 authorized;
                       measured via unconditioned no-bindings shell;
                       NOT scrambled-binding)
TP-banner emitter fix: applied (D4-A future-run patch at commit 5c60fbd);
                       ACTIVE form propagated into all 6 emitted reports
Result:                NOT_RULED_OUT under the active six-criterion set
                       (attached_labels = [])
Sealed LOCK-RECORD:    v1.0 sha256 51e18fa9... UNCHANGED throughout
D4-A record:           UNMUTATED (verified by commit-diff construction)
```

## §2. Verified artifact list and hashes

### D4-B run outputs (UNMUTATED; sha256 re-verified at this filing)

| artifact | sha256 |
|---|---|
| `d4_b_pilot/pre_flight_log.json` | `69575a72549cc66bb876599d588ff420787eb4b4fa8b79c684971241ede1310d` |
| `d4_b_pilot/candidate_predictions.json` | `ba276b0539a4e7eed6662ea586c94aa0adc6a54ecaa92a0fd5c6540b3d170b76` |
| `d4_b_pilot/tp_control_predictions.json` | `3bc7621c7b0bddf142f74b122e5f01259393e1bbb74850e2d741630cac110ee6` |
| `d4_b_pilot/t1_report.json` | `03b14a8e37a73f27ac95d703cc170c6aea2647ff8c8ea9cb090933c0d3d5ff59` |
| `d4_b_pilot/t3_report.json` | `6a74ae78a96212edceb096965d9cc5e4d937d3e9fb20fd2322fdad766f57f662` |
| `d4_b_pilot/t4_report.json` | `ed723a8fc59baa6111a6d7df70216d50cc056f1bab0ae4e087cfb921eb2ba948` |
| `d4_b_pilot/a6_re_verification.json` | `3538412be4a58eb200009ef4073f9685a3b3c77a5ebfb117ec3b4e69b70991d3` |
| `d4_b_pilot/execution_ledger.json` | `d8b8b7a9d75cf026ffd5320b504ed873c7400576291420e3f8cbfe5543df177e` |
| `d4_b_pilot/instrument_validation_report.md` | `70c26b2371e730cac7f3228c0ba8812baf2294833f524f47cc79f5f0783a60a5` |
| `d4_b_pilot/candidate_outputs/*` (96 files) | per-file sha256s on disk; unchanged since commit `9b0e0ee` |
| `d4_b_pilot/tp_control_outputs/*` (96 files) | per-file sha256s on disk; unchanged since commit `9b0e0ee` |

### Runner & supporting files (D4-B run-of-record)

| artifact | sha256 |
|---|---|
| `d4_runner/lane1a_runner_d4b.py` | `88504df4fbbf3a4ffc9e8a7371b31c32bd34bb61ff0c6e468a06be67c25ab42c` |
| `d4_runner/preconditions_d4b.json` | `e7376ac8e5c2faa1037b7afb3a6b44ca703bd0685299b2efd9116fbb93ccd0c0` |
| `d4_runner/prompt_template_v1.json` (candidate retrieval-shell) | `f1956e7dd43f165c8707fe88bc11757888f108e7e9766aa186ac9fc04f8b368a` |
| `d4_runner/prompt_template_v1_tp.json` (TP no-bindings shell) | `af55f9757005c6cd7c1baa1c77852d4a4bb596f185ceaccfb875ad29f3108615` |
| `d4_runner/decoding_config.json` | `a20391d89972d47c0b231f5c6da9f8a9f4c7be8c975ab98bd95a32327196f803` |
| `d4_runner/parse_model_output.py` | `fbdf989cdb8f258b7b2e18000835aafd9814a195b3eae0d73f540c08d35a1180` |

(The D4-A patched runner `lane1a_runner.py` sha256 `1d6f7085…`
provides shared utilities by import; it is not the D4-B run-of-record
runner.)

### Lock-event anchors (UNCHANGED)

| artifact | sha256 |
|---|---|
| `LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` | `51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935` |
| `ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5` |
| `T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39` |
| `STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5` |

### Governance memos (D4-B track)

| memo | sha256 |
|---|---|
| `LANE1A-PRIME-D4B-READINESS-PACKET-v0.1.md` | `899392696834dfec7a010022aaab700d41fa5caf79e13b2031b193785ef31f54` |
| `LANE1A-PRIME-D4B-PILOT-RETURN-v0.1.md` | `626a7effe5546bd87ff71902a4bfaa56913029ba4219562a915c9d542b793ab9` |

Verification basis: sha256 computed over each path's bytes via Python
`hashlib.sha256().hexdigest()`. All hashes above re-verified at this
filing match the committed values. Independent NS verification of the
D4-B G1 enumeration (17/17) is on record in the NS byte-verification
memo for D4-B.

## §3. Active six-criterion result summary

| criterion | bound | comparison | outcome vs candidate |
|---|---|---|---|
| null_abstention_floor_unmet | 0.75 | CI upper < bound | PASSED |
| answerable_abstention_ceiling_exceeded | 0.20 | CI lower > bound | PASSED |
| **accuracy_indistinguishable_from_token_prior** | **0.10** | **NW difference CI upper < bound** | **PASSED (TP active; measured)** |
| accuracy_indistinguishable_from_declared_policy_envelope | 0.10 | NW difference CI upper < bound | PASSED |
| insufficient_measurement_headroom | 0.15 | CI upper on (1−envelope) < bound | PASSED |
| strict_content_gap_instability | 0.30 | NW difference CI lower > bound | PASSED |

Ideal witness in pass region: True. No `boundary_proximity_flag` fired.
`attached_labels: []`. `outcome: NOT_RULED_OUT under the active
six-criterion set.`

The TP criterion was evaluated against the MEASURED model
unconditioned token prior (not the analytical 1/26 baseline used in
D4-A's TP-INACTIVE evaluation). The locked TP margin (0.10) and the
locked Newcombe-Wilson difference rule were applied verbatim.

### D4-B objective data (factual; presented under the bounded language §6)

| stratum / measure | value |
|---|---|
| n_answerable | 80 |
| candidate_correct | 80 |
| candidate_accuracy | 1.0000 |
| candidate_abstained | 0 |
| candidate_abstention_rate | 0.0000 |
| n_null | 16 |
| candidate_null_abstained | 16 |
| candidate_null_abstention_rate | 1.0000 |
| candidate_parse_failures | 0 |
| candidate_void_rate | 0.0000 |

## §4. Token-prior control summary

| measure | value |
|---|---|
| TP control method | `unconditioned_token_prior` — no-bindings shell (same prompt template structure with empty pair list); **NOT scrambled-binding** |
| TP control records | 96 (same sealed L01 manifests; same answerable/NULL stratification) |
| n_answerable | 80 |
| tp_control_correct | 1 |
| tp_control_accuracy | 0.0125 |
| analytical 1/26 baseline (reference) | ≈ 0.0385 |
| tp_control_parse_failures | 0 |
| tp_control_void_rate | 0.0000 |
| TP control descriptive note | The measured prior accuracy (0.0125) is below and near the analytical 1/26 baseline; the measured prior behaved like a prior, as the pre-registered expectation predicted. This is descriptive only, not a finding. |

### Token-prior control language (Manager §6 verbatim, carried verbatim per NS recommendation)

```text
Token-prior generations were authorized by name for D4-B only.
Token-prior outputs are control artifacts only.
Token-prior outputs are not candidate evidence.
Token-prior outputs are not threshold material.
Token-prior outputs are not reusable outside this lane's locked comparison.
```

This guard sentence binds the use of D4-B TP control outputs. They
were used exclusively inside the locked TP criterion's
Newcombe-Wilson difference computation. They are not reused, not
exported, not promoted to candidate data, and not carried into any
threshold-sheet, certification, or benchmark posture.

## §5. Candidate-vs-token-prior comparison summary

```text
candidate accuracy:            1.0000
TP control accuracy:           0.0125
point difference:              0.9875
Newcombe-Wilson CI on diff:    [0.9159, 0.9978]
locked TP margin:              0.10
TP criterion comparison rule:  fires iff CI upper < locked margin
                                (NW difference upper < 0.10)
TP criterion fires?            NO  (0.9978 is NOT < 0.10)
```

Independent NS recomputation (NS D4-B byte-verification memo): matched
CS's ledger values to full reported precision (`0.9159444…`,
`0.9977900…`). The comparison rule and the margin are both verbatim
the locked T3 declarations bound in the sealed LOCK-RECORD; nothing
was tuned.

The comparison block is materialized in:

| field | location |
|---|---|
| `candidate_vs_tp_comparison` block | `d4_b_pilot/execution_ledger.json` (top level) |
| `candidate_vs_tp_comparison` block | `d4_b_pilot/t3_report.json` (top level) |
| IVR D4-B addendum table | `d4_b_pilot/instrument_validation_report.md` |

## §6. Bounded result language (Manager §4 verbatim)

> **The instrument did not attach any elimination label under the
> active six-criterion set.**
>
> Accepted bounded interpretation:
> **The result was not explained by the declared shortcut battery or
> by the candidate's own measured token prior.**

This is the strongest permitted interpretation. CS does not strengthen
it.

## §7. Non-claim block (Manager §7 verbatim)

D4-B does NOT establish:

```text
model capability
model incapability
candidate certification
task-family viability
certification readiness
retention-under-compression
Claim C progress
seam evidence
public benchmark status
```

Forbidden phrasings (binding for all future references to the D4-B
result, in this packet and any downstream artifact):

```text
model passed
capability established
not shortcut-driven
candidate certified
task family viable
Claim C progressed
seam evidence
public benchmark result
certification achieved
```

Standing framing remains:

> The instrument may rule out; it may not rule in.
>
> Reportable only as "not explained by the declared shortcut battery"
> (and — TP being active and measured — "not explained by the
> candidate's own measured token prior").
>
> Never reportable as "not shortcut-driven."
>
> We have improved the ruler; we are only beginning to touch the
> territory.

## §8. Comparison to D4-A (Manager §8 verbatim posture)

```text
D4-A:  NOT_RULED_OUT under the active FIVE-criterion L01 instrument,
       TP INACTIVE by Manager decision (Q2 declined; reduced criteria
       set permitted only because Manager named it).

D4-B:  NOT_RULED_OUT under the active SIX-criterion L01 instrument,
       TP ACTIVE and measured (Q4 authorized;
       unconditioned_token_prior method via no-bindings shell).
```

D4-B is **stronger than D4-A in the narrow instrument sense** because
the measured token-prior control was active. The criterion's
separation logic applied the locked Newcombe-Wilson rule to candidate
vs measured prior; the CI upper on the difference (0.9978) is well
above the locked 0.10 margin, so TP does not fire.

**D4-B remains bounded instrument use, not a capability claim.** The
added strength is "+1 criterion ruled out" relative to D4-A; it is
not capability evidence, certification evidence, or any
positive-uplift claim.

## §9. Unauthorized-work audit (decisive, by construction)

```text
git diff --name-only 98d19be..9b0e0ee
  Result: changes confined to —
    experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner_d4b.py
    experiments/2026-06-11_lane-1a-prime/d4_runner/preconditions_d4b.json
    experiments/2026-06-11_lane-1a-prime/d4_runner/prompt_template_v1_tp.json
    experiments/2026-06-11_lane-1a-prime/d4_b_pilot/  (new directory)
    governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-D4B-PILOT-RETURN-v0.1.md

  Files NOT touched between 98d19be and 9b0e0ee:
    experiments/2026-06-11_lane-1a-prime/d4_a_pilot/*  (D4-A run-of-record)
    experiments/2026-06-11_lane-1a-prime/validation/*  (sealed surface)
    experiments/2026-06-11_lane-1a-prime/d4_runner/lane1a_runner.py
      (D4-A patched runner; unchanged — D4-B has its own runner file)
    governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md
```

Additionally at THIS filing time, CS re-hashed the sealed
LOCK-RECORD and the D4-A artifacts; all match their pre-D4-B values.
Independent NS verification confirms this (NS D4-B byte-verification
memo §10 constraint audit, §13 unauthorized-work audit).

**Confirmed clean:** no L02–L08 manifests generated, no quantization
work, no INT8/INT4 weights loaded, no scrambled-binding generations,
no threshold work, no certification evaluation, no candidate
selection, no ranking, no Claim C activation, no benchmark packaging.

## §10. Sealed LOCK-RECORD unchanged confirmation

**CONFIRMED.** Re-verified at this filing:

```text
governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md
  expected: 51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  actual:   51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  match:    True
```

Survival checks at this point: sealed during sealing event, byte-verified
under TL HOLD-closure, re-verified under D3 review, re-verified under
D4-A authorization, re-verified at D4-A run start, re-verified at D4-A
pilot return, re-verified through TP-banner deviation lifecycle,
re-verified at D5 (D4-A) close-out, re-verified at D4-B run start,
re-verified at D4-B pilot return, NS-verified through D4-B G1 — and
now re-verified again at D5-B close-out filing.

## §11. D4-A record unchanged confirmation

**CONFIRMED.** Per Manager §9, all D4-A artifacts remain unmutated.
Re-verified at this filing:

| D4-A artifact | sha256 (re-verified) | match to D4-A run-of-record |
|---|---|---|
| `d4_a_pilot/t1_report.json` | `ebe0a95246a5dfc474fab7e5543a34e63ed50c988815b5185a38fdad4ab3aa6d` | YES |
| `d4_a_pilot/t3_report.json` | `a4e0236bfd6a85e57472911cb9f51566212984ebfbc65579c91d1295666d0a1f` | YES |
| `d4_a_pilot/t4_report.json` | `6d265d25d1bd6852afa34fc1eb95680395fc82e1b993698a584f81a23fd29067` | YES |
| `d4_a_pilot/a6_re_verification.json` | `3c2e09b18e609e4fd2ab8513d6af6f74a55c13a19f98d56d217ed763c7d771ab` | YES |
| `d4_a_pilot/execution_ledger.json` | `f75db02c3080939fb60a6be9a22d3010b5c1e26ffec35b1a43acd7a5ebd08a0f` | YES |
| `d4_a_pilot/instrument_validation_report.md` | `7510c06a6dcddf09c8fe17c6fb3bf2993d351d4306ed3c7cb624f0225b449c42` | YES |
| `d4_a_pilot/pre_flight_log.json` | (per `LANE1A-PRIME-D4A-PILOT-RETURN-v0.1.md` §13) | YES |
| `d4_a_pilot/candidate_predictions.json` | (per same memo) | YES |
| `d4_a_pilot/candidate_outputs/*` (96 files) | per-file sha256s on disk | YES |

The D4-A TP-banner named deviation remains visibly part of the D4-A
record. It was acknowledged in
`CS-D4A-TP-BANNER-DEVIATION-ACK-AND-FIX-PLAN-v0.1.md` (sha256
`4beeefb37e988430f3456ca90913214547c318c46ae5230aef631e731c4df00e`),
dispositioned by Manager as accepted-with-named-deviation, and CLOSED
in lifecycle. The fix that resolved it for future runs (commit
`5c60fbd`) was successfully exercised in D4-B — every D4-B emitted
report carries the TP banner in symmetric ACTIVE form. The deviation
did not recur.

## §12. Constructibility-risk note (interpretation guard)

Per Manager §3 (in the D4-A close-out direction memo) and §10 (here),
the constructibility-risk carryforward note is a Contributor 5 + NS
deliverable:

```text
File:      CONSTRUCTIBILITY-RISK-CARRYFORWARD-NOTE-v0.1.md
Owner:     Contributor 5 + New Senior Engineer
Status:    AWAITING C5 + NS AUTHORING (CS does not file)
Referenced from: LANE1A-PRIME-D4A-D5-CLOSEOUT-PACKET-v0.1.md
                 LANE1A-PRIME-D4B-READINESS-PACKET-v0.1.md
                 (this packet)
```

The interpretation guard the note is intended to preserve carries
verbatim into this close-out packet so that no D5-B reader can infer
beyond bounds:

> D4-B L01 NOT_RULED_OUT does not prove that a full candidate can
> certify.
>
> It does not prove task-family viability across L01–L08.
>
> It does not prove model capability.
>
> It is not stress-retention evidence.
>
> It is not Claim C progress.

Future non-certification outcomes must remain interpretable across the
following three possibilities, none of which is dispositively
established by any single D4 instrument run:

```text
1. threshold miscalibration
2. gate-design defect
3. genuine constructibility barrier at model/task/scale
```

The third possibility — a genuine barrier — must remain a first-class
outcome under any future interpretation of non-certification. D4-B's
NOT_RULED_OUT under L01 is consistent with all three explanations
applied to any future L02–L08 or other-surface run; it does not
preempt any of them.

(When Contributor 5 + NS file the formal note, its sha256 and path
will be referenced from any successor close-out packet alongside this
verbatim interpretation guard.)

## §13. Successor-gate status (Manager §11 verbatim)

All successor gates remain **CLOSED** unless separately authorized by
Manager:

| gate | status |
|---|---|
| D5-B acceptance (this packet's decision request) | Manager decision pending; this packet prepares |
| D4-C or any successor D4 execution | NOT REQUESTED |
| L02–L08 execution | NOT REQUESTED |
| Additional token-prior generations | NOT REQUESTED (D4-B's authorization was for D4-B only) |
| Scrambled-binding generations | NOT REQUESTED — and the lane-wide prohibition remains in force |
| Quantization stress / INT8 / INT4 | NOT REQUESTED |
| Stress-retention testing | NOT REQUESTED |
| Candidate selection / ranking | NOT REQUESTED |
| Threshold work | NOT REQUESTED |
| Certification evaluation | NOT REQUESTED |
| Claim C activation | NOT REQUESTED |
| Public benchmark packaging | NOT REQUESTED |
| **D4 token-prior authorization slot** | authorized for D4-B only; remains UNOPENED for any other use |
| Sealed LOCK-RECORD v1.0 | UNCHANGED |

## §14. CS recommendation on D5-B close-out acceptance

CS recommendation: **D5-B close-out for D4-B MAY BE ACCEPTED** under
the bounded result language, the active-six-criterion posture, the
verified measured TP control, the unmutated-record discipline, and
the standing non-claim block.

### Rationale (presented under the non-claim block and the bounded language)

1. **Substantive integrity of the D4-B run is preserved.** All
   Manager-required preconditions PASSED at runtime (PH5-4 lock-event
   hashes, sealed LOCK-RECORD hash, sealed manifest hashes, mlx_lm
   version match, model snapshot hash via B1 v2 runner-provenance
   routine). No unauthorized execution occurred at any point during
   D4-B or in its close-out preparation.

2. **The TP criterion was evaluated honestly under the locked rule.**
   The criterion's separation logic applied the locked
   Newcombe-Wilson difference rule against the measured control with
   the locked margin (0.10). Independent NS arithmetic recomputation
   matched CS values to full precision. The measured prior behaved
   like a prior (0.0125 ≈ near analytical 1/26), and the candidate's
   separation from it (CI `[0.9159, 0.9978]`) is well above the locked
   margin.

3. **The TP-banner deviation from D4-A did not recur.** The
   future-run emitter fix (commit `5c60fbd`) was exercised
   successfully under the Q2-authorized path. All six D4-B emitted
   reports carry the symmetric ACTIVE TP banner form.

4. **No-mutation discipline is preserved across BOTH prior records.**
   The sealed LOCK-RECORD v1.0 is byte-identical to its sealing-event
   state. The D4-A run-of-record is byte-identical to its acceptance
   state. The D4-B run-of-record is byte-identical to its filing
   state. Verified at every successor transition, including this one.

5. **The bounded result language is binding.** The D4-B result is
   carried forward only as Manager's accepted bounded form — no
   overreach into capability, certification, viability,
   stress-retention, Claim C, seam, or benchmark.

6. **The constructibility-risk interpretation guard is preserved.**
   D4-B's NOT_RULED_OUT does not prove certifiability, task-family
   viability across L01–L08, model capability, stress-retention, or
   Claim C progress; it remains consistent with all three
   constructibility-risk possibilities (threshold miscalibration /
   gate-design defect / genuine barrier).

CS does not request D5-B acceptance. The recommendation above is
offered under the standard CS-recommend / NS-counter / TL-filter /
Manager-decide governance chain.

### What D5-B acceptance would NOT establish

```text
Not model capability.
Not model incapability.
Not task-family viability.
Not candidate certification.
Not certification readiness.
Not retention-under-compression.
Not Claim C progress.
Not seam evidence.
Not public benchmark status.
Not authorization for any successor model-facing work.
```

D5-B acceptance would establish that the D4-B operational pilot's
documentation and disposition trail are complete on the lane's terms,
fixing the D4-B record as a finished auditable unit. It is a
procedural close-out, not an evidentiary uplift.

---

## Appendix A — Reading order for D5-B review

1. This packet (§1–§14).
2. `LANE1A-PRIME-D4B-PILOT-RETURN-v0.1.md` (sha256 `626a7eff…`) for the
   D4-B run record's 24-item return.
3. NS D4-B byte-verification memo (NS-side filed) for the independent
   17/17 G1 enumeration and the candidate-vs-control arithmetic
   recomputation.
4. `LANE1A-PRIME-D4B-READINESS-PACKET-v0.1.md` (sha256 `89939269…`)
   for the readiness scope D4-B operated under.
5. `LANE1A-PRIME-D4A-D5-CLOSEOUT-PACKET-v0.1.md` (sha256 `12463cdf…`)
   for the predecessor close-out packet pattern (D4-A → D5 close-out
   accepted by Manager).
6. `LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` (sha256 `51e18fa9…`) for
   the sealed instrument anchor.
7. `CONSTRUCTIBILITY-RISK-CARRYFORWARD-NOTE-v0.1.md` — to be filed by
   Contributor 5 + NS per Manager direction.

## Appendix B — Standing carry (non-authorizations, verbatim)

This D5-B close-out packet does not authorize: D5-B acceptance;
successor D4 execution; L02–L08 execution; additional token-prior
generations; scrambled-binding generations; quantization stress;
INT8 / INT4; candidate selection; ranking; threshold work;
certification evaluation; stress-retention testing; Claim C
activation; public benchmark packaging.

All successor model-facing gates remain CLOSED until Manager
separately approves them by name.

**D4 token-prior authorization slot:** authorized by Manager for D4-B
only; remains UNOPENED for any other use.

— CS Engineer, 2026-06-11
