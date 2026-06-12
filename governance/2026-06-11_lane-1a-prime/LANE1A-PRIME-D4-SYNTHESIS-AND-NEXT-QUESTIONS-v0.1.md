# Lane 1a' Prime — D4 Synthesis and Next-Questions Memo (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
SYNTHESIS PREPARATION ONLY — NO EXECUTION AUTHORIZATION REQUESTED
SEALED LOCK-RECORD v1.0 UNCHANGED · D4-A AND D4-B RUN-OF-RECORD UNMUTATED
D4-A AND D4-B LIFECYCLES CLOSED · D4 TOKEN-PRIOR SLOT REMAINS UNOPENED FOR ANY FURTHER USE
NO MODEL INVOKED · NO MODEL LOADED · NO NEW SWEEP_ID · NO SWEEP EXECUTION
NO ADDITIONAL TOKEN-PRIOR GENERATIONS · NO QUANTIZATION · CLAIM C INACTIVE
```

To: Manager (decision context) · Cc: Team Lead, Senior Engineer
From: New Senior Engineer (synthesis lead) · CS Engineer (verification scaffolding) · Contributor 5 (adversarial review)
Date: 2026-06-11
Re: Manager-authorized post-D4 synthesis per the "D4 Synthesis and Next-Questions Memo" direction

This memo consolidates the closed D4-A and D4-B lifecycles into a
single bounded interpretation record and maps the next empirical
choices Manager may consider. It authorizes nothing. It strengthens
nothing. Per Manager §4 the strongest permitted bounded interpretation
is carried verbatim and is not exceeded.

**Role attribution (per Manager §10):** NS is the synthesis lead and
owns the claim-boundary discipline and the next-question map; CS owns
the artifact/state verification, path/hash references, and the
no-execution confirmations; Contributor 5 owns the adversarial review
of overclaim paths and the funder-language risk review. This v0.1
filing presents the CS-side scaffolding in full and a CS-drafted text
covering the substantive sections, pending NS finalization and C5
adversarial pass.

---

## §1. Purpose

The lane has reached a natural pause point. The instrument has been
validated. The instrument has been sealed. The instrument has now
been driven against a real model twice — once under a reduced
five-criterion set (Q2 declined) and once under the full
six-criterion set with measured token-prior control. Both runs
returned NOT_RULED_OUT and both lifecycles have been formally closed
by Manager.

Before any successor gate is considered, the team needs a single
record that:

1. Freezes what D4-A and D4-B did and did not establish;
2. States the strongest permitted bounded interpretation, verbatim,
   without strengthening it;
3. Maps the next empirical choices available, with what each would
   test and what each would still not establish;
4. Carries the constructibility-risk guard as binding interpretation
   context for any future decision.

This memo is that record.

## §2. Current state (verified)

```text
D4-A:
  L01-only operational pilot
  TP INACTIVE by Manager decision (Q2 declined; reduced criteria set
                                   permitted only because Manager named it)
  active FIVE-criterion set
  outcome: NOT_RULED_OUT (attached_labels = [])
  named TP-banner emitter completeness deviation → CLOSED;
                                                   future-run fix accepted
  D4-A lifecycle: CLOSED through D5 close-out (Manager-accepted 2026-06-11)

D4-B:
  L01-only operational pilot
  TP ACTIVE by Manager decision (Q4 authorized;
                                  unconditioned_token_prior method;
                                  no-bindings shell; NOT scrambled-binding)
  measured token-prior control: 1/80 = 0.0125 (descriptively near analytical 1/26)
  active SIX-criterion set
  candidate accuracy: 80/80 = 1.0000
  candidate-control difference: 0.9875
  Newcombe-Wilson CI on difference: [0.9159, 0.9978]
  locked TP margin: 0.10  →  TP criterion did NOT fire (CI upper >> margin)
  outcome: NOT_RULED_OUT (attached_labels = [])
  TP-banner emitter fix from D4-A: exercised successfully (ACTIVE form
                                                            in all 6 reports)
  D4-B lifecycle: CLOSED through D5-B close-out (Manager-accepted 2026-06-11)

Sealed LOCK-RECORD v1.0: UNCHANGED (≈13 survival checks across the
                                     full D3 → sealing → D4-A → D4-A
                                     deviation lifecycle → D4-B → D5-B
                                     chain)
D4 token-prior authorization slot: was authorized for D4-B ONLY;
                                    remains UNOPENED for any further use
Successor model-facing gates:       all CLOSED
```

## §3. Bounded result language (Manager §4 verbatim — strongest permitted)

> **The instrument did not attach any elimination label under the
> active six-criterion set.**
>
> Accepted bounded interpretation:
> **The result was not explained by the declared shortcut battery or
> by the candidate's own measured token prior.**

```text
This is the strongest permitted interpretation.
It may not be strengthened.
```

The D4-A result is carried under its own narrower form (five-criterion
set; TP inactive by Manager decision):

> The D4-A result is that, under the active five-criterion L01 pilot
> with TP inactive by Manager decision, the instrument did not attach
> an elimination label.

This narrower form does not subsume D4-B's, and D4-B's does not
override D4-A's. They are two separate, closed records.

## §4. Progression summary (Manager §5)

```text
validated instrument
    →
sealed instrument
    →
D4-A first model contact (L01; TP inactive)
    →
D4-A five-criterion NOT_RULED_OUT
    →
D4-B token-prior-active model contact (L01; TP active)
    →
D4-B six-criterion NOT_RULED_OUT
    →
closed D4-A and D4-B lifecycles
```

This progression is NOT a certification, NOT a capability proof, and
NOT Claim C progress. It is a sequence of bounded instrument-use
events, each verified and recordable on the lane's own terms.

The single substantive empirical addition between D4-A and D4-B is the
measured token-prior control. The measured prior behaved like a prior
(0.0125, descriptively near the analytical 1/26 baseline of 0.038),
and the candidate's separation from it (`[0.9159, 0.9978]`) is well
above the locked TP margin (0.10) — so the criterion did not fire.
That is one additional declared-class explanation that has been ruled
out, and only that.

## §5. Non-claim block (Manager §6 verbatim)

D4-A and D4-B do NOT establish:

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

Forbidden phrasings (binding for all future references to D4-A or
D4-B, in this memo and in any downstream artifact):

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
> (and — for the D4-B result — additionally "not explained by the
> candidate's own measured token prior").
>
> Never reportable as "not shortcut-driven."
>
> We have improved the ruler; we are only beginning to touch the
> territory.

## §6. Constructibility-risk guard (Manager §7 — binding for §7 next-questions)

Attached: `CONSTRUCTIBILITY-RISK-CARRYFORWARD-NOTE-v0.1.md`
(sha256 `ff8426897034753d8a23b92ff7fe588d76ea49ef9a75a8c41c0a79ee44c6aad7`;
NS-finalized; Contributor 5 precursor draft also in repo as
`CONSTRUCTIBILITY-RISK-CARRYFORWARD-NOTE-v0.1-CONTRIBUTOR5-DRAFT.md`
sha256 `088fe5a27af7bf4d5443230a72fecd597df425f89ab3c43619e24cf0c5219d6e`).

Binding interpretation guard carried verbatim into this synthesis:

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

Future non-certification outcomes — including K=0, INCONCLUSIVE, or
failure-to-certify under any path — must remain interpretable across
three branches, none privileged in advance:

```text
1. threshold miscalibration  — gate arithmetic directionally right but
                                numerically too tight or too loose
2. gate-design defect        — gate logic measures the wrong axis or
                                admits/excludes the wrong behavior
3. genuine constructibility  — the task family at the tested
   barrier at model/task/      model/scale may not produce behavior
   scale                       that can clear the certification window
```

**The third branch is a first-class outcome.** It is not an
embarrassment, and it is not an automatic reason to loosen gates.
The constructibility-risk note carries this point in full.

## §7. Next-question map (Manager §8)

The following paths are available to Manager consideration. None is
authorized by this memo. Each entry states the empirical question the
path tests and what the path still would not establish.

### Path A — L01–L08 with TP active

```text
Question tested:
  Does the D4-B six-criterion NOT_RULED_OUT result survive broader
  extent across the full sealed surface (L01–L08, 768 records)?

What this path WOULD potentially add:
  - Coverage of seven additional rungs beyond L01
  - More statistical room on the per-criterion CIs
  - Whether the candidate's L01 separation from its measured prior
    holds at deeper or differently-constructed rungs
  - Whether the active six-criterion set fires anywhere on the surface

What this path WOULD still NOT establish:
  - Model capability
  - Task-family viability beyond the sealed surface
  - Certification readiness
  - Retention under compression
  - Claim C progress
  - Transferability to a different model

Preconditions before opening:
  - Manager authorization (separate from this memo)
  - Reading B generator pin (Lane 1a' D4 readiness packet v0.2 §21):
    generator path + sha256, locked seed, per-rung manifest hashes
    written at generation time
  - Each rung's pilot and final manifest sha256 captured in the
    execution ledger
  - The team's acceptance that even a clean Path-A NOT_RULED_OUT
    remains bounded instrument use, not a capability claim
```

### Path B — second model, L01 with TP active

```text
Question tested:
  Does the L01 six-criterion NOT_RULED_OUT result transfer beyond
  Qwen2.5-3B-Instruct?

What this path WOULD potentially add:
  - One axis of model-family / model-scale variation
  - Empirical evidence on whether the lane's instrument behaves
    similarly when driven by a different candidate
  - Coverage of one of the three "scaling axes" flagged in the
    project memory (model family / model scale)

What this path WOULD still NOT establish:
  - Model capability (in either the original or the second model)
  - Task-family viability
  - Certification readiness
  - Retention under compression
  - Claim C progress
  - Cross-construction transfer (the construction stays Lane 1a')

Preconditions before opening:
  - Manager authorization (separate from this memo)
  - Second model identity declared by name + snapshot hash
  - mlx_lm version pin (or framework substitution) declared explicitly
  - Tokenizer hash bound (different model = different tokenizer)
  - Runner adapted to the second model's chat template
  - Acceptance that any cross-model comparison is a separate
    governance unit (no implicit shared-instrument certification)
```

### Path C — stop and write

```text
Question tested:
  Is the completed instrument-validation and first-contact evidence
  package strong enough to consolidate into a paper, internal report,
  or funder-facing concept note WITHOUT FURTHER EXECUTION?

What this path WOULD potentially add:
  - Portable evidence base for the lane's instrument-validity
    discipline (sealed instrument + fail-closed pre-flight + TP-banner
    discipline + 12/12 oracle match + bounded-language framework)
  - Documented exemplar of the river-and-canyon governance pattern
  - Decision-record example of a named-deviation lifecycle CLOSED
    cleanly without post-hoc mutation
  - Demonstration of the negative-result-form discipline (NOT_RULED_OUT
    as a bounded form, not a positive claim)

What this path WOULD still NOT establish:
  - Model capability or any positive evidence claim
  - Candidate certification
  - Task-family viability
  - Retention under compression
  - Claim C progress
  - Public benchmark status

Preconditions before opening:
  - Manager authorization for the specific writing target (paper,
    internal report, concept note) — each target has different
    boundary and audience implications
  - Senior Engineer paper-ownership (if a paper is the target)
  - Verbatim carry of all forbidden phrasings into the target
    document; verbatim carry of the bounded result language; verbatim
    carry of the constructibility-risk guard
  - Adversarial review for funder-language risk (Contributor 5)
```

### Path D — future stress-retention only after certification prerequisites

```text
Question tested (only as a structural inquiry; not opened):
  What additional certifiable baseline would be required before
  INT8 / INT4 or other compression stress is allowed?

What this path WOULD potentially establish (only after prerequisites):
  - Retention under compression as a downstream finding, IF a
    certifiable baseline exists first

What this path explicitly DOES NOT do now:
  - Quantization stress is NOT opened
  - INT8 / INT4 is NOT opened
  - This entry is a structural reminder that stress-retention work
    cannot precede a certifiable baseline; it is not a request to
    proceed
  - Per the constructibility-risk note §5: "Only after a clean
    certifiable baseline exists should stress-retention claims become
    live."

Preconditions before any opening:
  - A certifiable baseline exists (which D4-A and D4-B did not
    establish; bounded result language is explicit on this)
  - Threshold sheet locked
  - Scope_of_certification declared
  - Per-precision-rung run authorization by name from Manager
  - All forbidden phrasings preserved with the quantization axis
```

## §8. CS recommendation section (Manager §9 — phrased as future Manager decision)

Per Manager §9, the recommendation in this memo is offered as
**evaluation input for a future Manager decision**, not as an
authorization request.

### Default posture to evaluate

```text
Do not open quantization stress yet.
Do not activate Claim C.
Do not open L02–L08 until the team accepts the constructibility-risk
  guard and decides whether breadth (Path A) or replication (Path B)
  is the higher-value next uncertainty.
```

### CS-side recommendation (not an authorization request)

If Manager seeks a single CS recommendation among Paths A–D, CS
recommends **Path C** as the cleanest next default. Rationale:

```text
1. Path C carries the lowest execution risk (none) and preserves the
   sealed instrument's immutability indefinitely.

2. Path C creates portable evidence of the lane's instrument-validity
   discipline, named-deviation handling, and bounded-language
   framework — contributions that are valuable in themselves, separate
   from any capability question.

3. Path C does not preempt Path A or Path B. After consolidation, the
   team can still elect to open L02–L08 or a second-model run with a
   stronger position; Path C may even strengthen the framing.

4. Path C honors the constructibility-risk guard most directly: it
   does not assume that further L01 / L02–L08 / transfer execution will
   produce a different kind of evidence than what already exists.
```

CS recognizes that Paths A and B add empirical leverage if breadth or
replication is the higher-value next uncertainty for the program.
Between Paths A and B, CS would suggest **B (replication on a second
model)** is likely more informative per execution: L01 has been deeply
exercised under one model in two distinct criterion configurations,
and Path B addresses a different empirical axis (model family / scale)
that L01-extent does not. This is a future Manager decision, not a CS
authorization request.

CS explicitly does not recommend Path D in any form now. The
constructibility-risk guard's §5 statement
("Only after a clean certifiable baseline exists should
stress-retention claims become live") is binding and unmet.

## §9. CS contribution — Verification scaffolding (Manager §10 CS role)

### §9.1 Sealed LOCK-RECORD v1.0 — survival check

```text
governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md
  expected: 51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  actual:   51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935
  match:    True (this synthesis re-verification is the ≈14th)
```

### §9.2 D4-A run-of-record artifacts — UNMUTATED

| artifact | sha256 (run-of-record) |
|---|---|
| `d4_a_pilot/pre_flight_log.json` | `ebda4737c9c97c752475f8d44e582f28eca8c3fc10c907fdb7d5c16bc493281d` |
| `d4_a_pilot/candidate_predictions.json` | `ba276b0539a4e7eed6662ea586c94aa0adc6a54ecaa92a0fd5c6540b3d170b76` |
| `d4_a_pilot/t1_report.json` | `ebe0a95246a5dfc474fab7e5543a34e63ed50c988815b5185a38fdad4ab3aa6d` |
| `d4_a_pilot/t3_report.json` | `a4e0236bfd6a85e57472911cb9f51566212984ebfbc65579c91d1295666d0a1f` |
| `d4_a_pilot/t4_report.json` | `6d265d25d1bd6852afa34fc1eb95680395fc82e1b993698a584f81a23fd29067` |
| `d4_a_pilot/a6_re_verification.json` | `3c2e09b18e609e4fd2ab8513d6af6f74a55c13a19f98d56d217ed763c7d771ab` |
| `d4_a_pilot/execution_ledger.json` | `f75db02c3080939fb60a6be9a22d3010b5c1e26ffec35b1a43acd7a5ebd08a0f` |
| `d4_a_pilot/instrument_validation_report.md` | `7510c06a6dcddf09c8fe17c6fb3bf2993d351d4306ed3c7cb624f0225b449c42` |

### §9.3 D4-B run-of-record artifacts — UNMUTATED

| artifact | sha256 (run-of-record) |
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

### §9.4 Closed-lifecycle governance memos

| memo | sha256 |
|---|---|
| `MANAGER-D3-AUTHORIZATION-2026-06-11.md` | `802439a712149afd51f46e32c0889bb9cf8c3f725c76c215ced35bc25bcc7c9e` |
| `MANAGER-LOCK-RECORD-SEALING-AUTHORIZATION-2026-06-11.md` | `fbc34b12a366e2c5f9a46bf2db80b1e24fddb8998a9b1b88bfac6a841a066562` |
| `LANE1A-PRIME-D4A-PILOT-RETURN-v0.1.md` | `0b230e036be984a24c610cafaa9bdc3e6a11ed6053f8ba58a4f0547251916979` |
| `CS-D4A-TP-BANNER-DEVIATION-ACK-AND-FIX-PLAN-v0.1.md` | `4beeefb37e988430f3456ca90913214547c318c46ae5230aef631e731c4df00e` |
| `LANE1A-PRIME-D4A-D5-CLOSEOUT-PACKET-v0.1.md` | `12463cdfa9c557aaceb1a69a1c2016d4211d9d831ab13afb5d51120a5c21e981` |
| `LANE1A-PRIME-D4B-READINESS-PACKET-v0.1.md` | `899392696834dfec7a010022aaab700d41fa5caf79e13b2031b193785ef31f54` |
| `LANE1A-PRIME-D4B-PILOT-RETURN-v0.1.md` | `626a7effe5546bd87ff71902a4bfaa56913029ba4219562a915c9d542b793ab9` |
| `LANE1A-PRIME-D4B-D5-CLOSEOUT-PACKET-v0.1.md` | `20ca240148e2fdaf77dfc9aa273f226ed77daad74916bbb0c3cca8663430d415` |
| `NEW-SENIOR-CS-D5-D4B-PACKET-VERIFICATION-v0.1.md` | `2df9ebf11dc58f0df9bb6119a6d69490dbb322e72e4c776f5e5b4bd81b9b6000` |
| `CONSTRUCTIBILITY-RISK-CARRYFORWARD-NOTE-v0.1.md` | `ff8426897034753d8a23b92ff7fe588d76ea49ef9a75a8c41c0a79ee44c6aad7` |

### §9.5 Lock-event anchors (UNCHANGED throughout)

| artifact | sha256 |
|---|---|
| `LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` | `51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935` |
| `ORACLE_VERDICT_TABLE.json` | `9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5` |
| `T3_BOUNDS_DECLARATION.json` | `45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39` |
| `STRATIFIED_RECIPE_SCHEDULE.json` | `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5` |

All hashes above re-verified at this synthesis filing.

---

## §10. Manager §11 12-item return

| # | item | value |
|---|---|---|
| 1 | commit SHA (this synthesis) | recorded in CS delivery report after commit lands |
| 2 | path | `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-D4-SYNTHESIS-AND-NEXT-QUESTIONS-v0.1.md` |
| 3 | sha256 (this synthesis) | recorded in CS delivery report after commit lands |
| 4 | verification basis | Python `hashlib.sha256()` over committed bytes for all §9 entries; independent NS verification on file for D4-A (per `NEW-SENIOR-D4A-PILOT-BYTE-VERIFICATION-v0.1.md`) and D4-B (per `NEW-SENIOR-D4B-PILOT-BYTE-VERIFICATION-v0.1.md`); NS verification of D5 (D4-A) + D4-B readiness packets per `NEW-SENIOR-CS-D5-D4B-PACKET-VERIFICATION-v0.1.md` |
| 5 | D4-A and D4-B bounded language preserved | **CONFIRMED.** §3 carries the D4-B bounded form verbatim and the D4-A bounded form in its narrower five-criterion shape; no strengthening; non-claim block in §5 carries Manager-forbidden phrasings verbatim |
| 6 | no successor execution occurred | **CONFIRMED.** This memo is preparation only. No runner invoked. No model loaded. No inference run. |
| 7 | no new sweep_id was created | **CONFIRMED.** |
| 8 | no additional model execution occurred | **CONFIRMED.** |
| 9 | no additional token-prior generations occurred | **CONFIRMED.** The D4-B token-prior authorization (Q4) was for D4-B only and the slot is recorded as remaining UNOPENED for any further use. |
| 10 | no quantization or stress testing occurred | **CONFIRMED.** No `tier0-run/Qwen2.5-3B-Instruct-mlx-int{4,8}/` artifact loaded; no quantization stress; no stress-retention testing. |
| 11 | Claim C remains inactive | **CONFIRMED.** Claim C is not activated and is not requested. |
| 12 | all successor gates remain closed | **CONFIRMED.** Per §13 below and per Manager §12 enumeration. |

---

## §11. Outstanding deliverables and counter-signature requests

```text
NS finalization:    NS is the synthesis lead per Manager §10. This v0.1
                    presents a CS-drafted text with full Manager-required
                    sections; NS may finalize the substantive sections
                    (§1–§8) and the next-question map (§7) under
                    synthesis-lead authority.

C5 adversarial:     Contributor 5 is named for adversarial review of
                    overclaim paths, misuse / funder-language risk
                    review, and the constructibility-risk guard. v0.1
                    incorporates the C5-precursor / NS-finalized
                    constructibility-risk note verbatim in §6 and the
                    binding interpretation guard. C5 may add an
                    adversarial pass on §7's next-question map and
                    §8's recommendation.

CS scaffolding:     The verification scaffolding in §9, the no-execution
                    confirmations in §10, and the non-authorization
                    carry in §13 are CS-side complete at v0.1.
```

This v0.1 may be carried into a v1.0 by NS finalization + C5
adversarial pass; or it may be revised in place if NS prefers. CS does
not pre-empt either choice; CS files v0.1 as the scaffolding skeleton
and the substantive draft that NS and C5 may revise.

## §12. Reading order for any future Manager decision based on this synthesis

1. This memo (§1–§13) for the consolidated bounded view.
2. `CONSTRUCTIBILITY-RISK-CARRYFORWARD-NOTE-v0.1.md` (sha256
   `ff842689…`) for the interpretation guard.
3. `LANE1A-PRIME-D4A-D5-CLOSEOUT-PACKET-v0.1.md` (sha256 `12463cdf…`)
   for the D4-A close-out record.
4. `LANE1A-PRIME-D4B-D5-CLOSEOUT-PACKET-v0.1.md` (sha256 `20ca2401…`)
   for the D4-B close-out record.
5. `LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` (sha256 `51e18fa9…`) for
   the sealed instrument anchor.
6. The two NS byte-verification memos (`NEW-SENIOR-D4A-PILOT-…`,
   `NEW-SENIOR-D4B-PILOT-…`) for the independent G1 enumerations.
7. `NEW-SENIOR-CS-D5-D4B-PACKET-VERIFICATION-v0.1.md` (sha256
   `2df9ebf1…`) for the cross-packet readiness verification.

## §13. Standing carry (non-authorizations, verbatim)

This synthesis memo does not authorize: successor D4 execution;
L02–L08 execution; additional token-prior generations;
scrambled-binding generations; quantization stress; INT8 / INT4;
candidate selection; ranking; threshold work; certification
evaluation; stress-retention testing; Claim C activation; public
benchmark packaging.

All successor model-facing gates remain CLOSED until Manager
separately approves them by name.

**D4 token-prior authorization slot:** was authorized for D4-B only;
**remains UNOPENED for any further use.** Any future TP authorization
is a separate Manager decision.

**Sealed LOCK-RECORD v1.0** `51e18fa9…`: UNCHANGED.

**Claim C:** INACTIVE.

— New Senior Engineer (synthesis lead — finalization pending)
— CS Engineer (verification scaffolding complete; 2026-06-11)
— Contributor 5 (adversarial review pending)
