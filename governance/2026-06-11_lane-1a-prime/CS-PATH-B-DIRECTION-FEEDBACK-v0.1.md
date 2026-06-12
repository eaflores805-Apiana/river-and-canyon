# CS Path B Direction Feedback (v0.1)

```text
SCOPE: CS-LANE FEEDBACK ONLY · NO READINESS PACKET DRAFTED
NO EXECUTION REQUESTED · NO SEALED-BYTE CHANGE REQUESTED
ARTIFACT / PATH / MODEL / RUNNER / SEMANTIC-READ requirements enumerated for the Path B question
CS RECOMMENDATION ON PATH-CHOICE included as feedback only; Manager decides
SEALED LOCK-RECORD v1.0 UNCHANGED · SEALED SCHEDULE UNCHANGED
PATH A (rung-uniform) CLOSED · BREADTH UNTESTED UNDER CURRENT SEALED SCHEDULE
```

To: Team Lead · Cc: Manager, NS, Senior, C4, C5, C6
From: CS Engineer
Date: 2026-06-12
Re: TL §5 / §6 CS-scope feedback on proposed Path B direction

CS files feedback per TL request. The CS-scope task (§6 CS Engineer
prompt) is to identify likely artifact, path, model, runner, and
semantic-read requirements for a Path B readiness packet — without
drafting the packet. CS also offers brief answers to the §5 seven
generic questions through the CS lens, including a feedback-only
recommendation on path-choice; the path-choice decision rests with
Manager.

CS reads the proposed Path B question (§1) as: *does the Path A
(rung-uniform) L01-equivalent non-elimination pattern replicate
under a second model-facing condition?* — bounded follow-up, not
breadth, not certification, not compression. The §3 forbiddens
(does breadth work, L01–L08 breadth, task family viable, candidate
certified, constructibility, Claim C, quantization, INT8/INT4) are
the closed perimeter; Path B's epistemic envelope sits strictly
inside that perimeter.

---

## §1. Quick answers to the seven §5 questions (CS lens)

CS gives short answers; the role-specific prompt is addressed in §2.

**Q1. Is Path B the right next research direction?**
*CS recommends Path D first, then Consolidation, with Path B and
Option S deferred.* Path B is the only option of the four that
requires model-facing execution. Its epistemic ceiling is low
(adds at most one bounded-sentence outcome on the L01-equivalent
surface under one more condition; does not open any new question
that was not already framed). Path D (stress-prerequisite taxonomy)
and Consolidation (claim-ledger / Paper 3 implications) produce
real project value at zero execution risk and zero sealed-byte
risk. Option S costs the most but answers the only question whose
absence is structurally blocking (the breadth question).

**Q2. If Path B is worthwhile, what should the second condition be?**
CS does not propose a specific condition (Manager design choice).
The *least-confounded* second condition under the current seal is
**a second model snapshot of the same family at full precision**
(e.g., a different Qwen2.5 size at bf16). Family-change introduces
tokenizer / prompt-template / decoding-config confounds; size-only
keeps the instrument fixed and varies only the candidate.

**Q3. What would Path B establish if it returns cleanly?**
At most: *under the sealed rung-uniform schedule, the active
six-criterion instrument attached no elimination label to an
L01-equivalent surface repeated under one rung label for a second
model M2 distinct from Path A's model.* One additional bounded
sentence on the same surface. Per Manager close-out §11 forbiddens
list and the standing constraint on per-rung adjudication, the
two outcomes (Path A's and Path B's) do **not** aggregate into
generality, robustness, replication-in-the-strong-sense, or any
breadth- / certification- / capability-class claim.

**Q4. What would Path B not establish?**
Everything Manager close-out §6 forbids, plus: no generality
across models; no Claim C progress; no cross-rung structure (since
the schedule is still rung-uniform); no compression / INT8 / INT4
finding; no task-family viability; no candidate certification; no
public-benchmark-class result.

**Q5. Load-bearing artifacts requiring semantic-read before routing.**
This is the CS-scope answer; see §2 below.

**Q6. Main failure modes / claim-risk traps.**
See §3 below.

**Q7. Path B vs Option S / Path D / Consolidation.**
*CS recommends* (in cost-benefit order): **Path D > Consolidation
> Path B > Option S** for the next move under the current posture.
Rationale in §4. This is feedback only; Manager decides.

---

## §2. Likely artifact, path, model, runner, and semantic-read requirements (the §6 CS task)

CS enumerates the requirements assuming the working interpretation
"second model snapshot on the same sealed instrument" (the
narrowest, least-bytes-touching reading of "second condition").
Other readings (different size, different prompt shell, different
decoding) shift requirements; CS flags those in §2.5.

### 2.1 Artifact requirements

```text
SEALED INSTRUMENT — REUSED VERBATIM, NO CHANGE
  STRATIFIED_RECIPE_SCHEDULE.json   7ad3ccdd...  (the rung-uniform schedule;
                                                  Path B uses ONE rung only;
                                                  the rung-uniformity is irrelevant
                                                  to a single-condition test)
  ORACLE_VERDICT_TABLE.json         9c6cbda9...
  T3_BOUNDS_DECLARATION.json        45565d0b...
  pilot_manifests_L01.json          afe0e545...  (96 records: 80 answerable + 16 NULL)
  final_manifests_L01.json          afe0e545...  (byte-equal under PH5-3)
  LOCK-RECORD v1.0                  51e18fa9...

NEW ARTIFACTS REQUIRED
  Second-model snapshot manifest    sha256 per B1 v2 routine
                                    (model_snapshot_hash distinct from Path A's
                                     abee745b... by construction)
  Second-model lineage record       (HF revision id, snapshot timestamp,
                                     declared family/size/precision)
  Path B runner                     proposed name: lane1a_runner_path_b.py
                                    (a parameterization of D4-A or D4-B runner;
                                     NO multi-rung loop)
  Path B preconditions JSON         analog of preconditions_path_a.json
  Path B run outputs                experiments/.../path_b_run/L01/
                                    (one rung directory only, not eight)
```

### 2.2 Path requirements

```text
Sealed instrument dir              experiments/2026-06-11_lane-1a-prime/validation/   (UNCHANGED, sealed-byte-protected)
Generator                          experiments/.../lane1a_prime/validation.py  db69519f...  (UNCHANGED)
Runner location                    experiments/.../d4_runner/lane1a_runner_path_b.py (proposed)
Preconditions location             experiments/.../d4_runner/preconditions_path_b.json (proposed)
Run outputs                        experiments/.../path_b_run/L01/                  (proposed; one rung)
```

### 2.3 Model requirements

```text
Path A model (reference, not reused as the Path B candidate):
  family:     Qwen2.5
  variant:    Qwen2.5-3B-Instruct
  precision:  bf16
  HF id:      Qwen/Qwen2.5-3B-Instruct
  snapshot:   abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20

Path B candidate (declared at packet time; CS does not select):
  family:     (Manager / NS decision — recommend Qwen2.5 family for minimal confound)
  variant:    (e.g., Qwen2.5-1.5B-Instruct or Qwen2.5-7B-Instruct, or another
               family if Manager prefers cross-family evidence; CS flags
               tokenizer + prompt-template + decoding-config confounds in §3)
  precision:  bf16 (full precision; INT8/INT4 closed by Manager)
  HF id:      (declared at packet time)
  snapshot:   (computed at preflight; MUST verify ≠ abee745b...)

Pin discipline:
  mlx_lm:     pin substituted per CS-D4A-MLX-LM-PIN-SUBSTITUTION (carried forward
              as 0.31.3 per B1 v2 verified-null lineage); same Option A pin
              substitution applies to Path B if mlx_lm is the runtime;
              if the second model requires a different runtime, that introduces
              a new instrument-class question that NS must address
              (potentially HOLD-class)
```

### 2.4 Runner requirements

```text
Base:                      derived from lane1a_runner.py (D4-A) or
                           lane1a_runner_d4b.py (D4-B with TP active)
Structure:                 SINGLE-CONDITION (not multi-rung)
  - no rung-loop scaffolding from lane1a_runner_path_a.py
  - one candidate sweep at L01
  - if TP active: one TP control sweep at L01 (parallel to candidate)
Inputs:                    sealed L01 manifests (path A's, byte-identical)
Pre-flight hash refusal:   armed for all sealed artifacts (7ad3ccdd... +
                           9c6cbda9... + 45565d0b... + afe0e545... + 51e18fa9...)
Sealed-byte protection:    inventory-snapshot validation/ before + after;
                           abort on any change (reuses Path A's sealed-dir
                           protection mechanism)
Model snapshot:            computed via B1 v2 routine; must match the
                           authorized_model_snapshot_hash declared in
                           preconditions_path_b.json
Provenance stamping:       sweep_id, runner sha256, runtime version, decoding
                           config, candidate model identity (all per Manager §8
                           Path A return shape)
TP-banner discipline:      fix-forward applies — every report-class artifact
                           must carry the TP banner per Manager Hash Integrity
                           close-out §8 / Manager Path A HOLD §7
Adjudication:              single rung; bounded sentence; NO aggregation with
                           Path A's bounded sentence
Outputs:                   t3_report, t4_report, a6_re_verification, execution_ledger,
                           candidate_predictions, (if TP: tp_control_predictions
                           + candidate_vs_tp_comparison), instrument_validation_report
                           — all with TP-banner fields populated
```

### 2.5 Semantic-read requirements (the load-bearing artifacts)

This is the new gate. Per Manager Hash Integrity close-out §8, NS
must include a shown semantic-read in the Path B readiness packet
covering each load-bearing artifact. CS enumerates the artifacts
CS expects to be subject to semantic-read, and CS's expected
disposition outcome at the artifact-fit level (CS does not perform
the semantic-read itself — NS owns that; CS lists the inputs).

```text
Artifact                            Concept claimed in packet                       CS expected disposition (input to NS)
──────────────────────────────────  ──────────────────────────────────────────────  ────────────────────────────────────────
STRATIFIED_RECIPE_SCHEDULE.json     "a single L01-equivalent surface"               PASS (the rung-uniform schedule
  7ad3ccdd...                       (Path B uses one rung only; the schedule's       trivially instantiates one surface;
                                     rung-uniformity is not a defect for this        the Path A drift was claiming EIGHT
                                     concept)                                        distinct surfaces, which it could not
                                                                                     instantiate. Path B claims ONE.)

pilot_manifests_L01.json            "96 L01-equivalent records used as the          PASS (mechanically rendered: 96
final_manifests_L01.json              candidate's test surface"                       records, byte-equal pilot=final, recipe
  afe0e545...                                                                        hash matches sealed)

Second model snapshot               "a second model distinct from Path A's          NS to perform: verify
                                     Qwen2.5-3B-Instruct abee745b... by              model_snapshot_hash ≠ abee745b... by
                                     declared family/size/precision"                 B1 v2 routine; verify declared
                                                                                     family/size/precision matches packet
                                                                                     declaration; HOLD if the snapshot is
                                                                                     not actually distinct or doesn't match
                                                                                     declaration

Path B runner                       "single-condition L01 execution; NO              NS to perform: read the runner; confirm
  lane1a_runner_path_b.py             multi-condition aggregation"                    NO multi-rung loop, NO repeated-label
                                                                                     scaffolding, NO aggregation logic across
                                                                                     conditions; HOLD if any of those appear

Prompt shell (template_v1)          "the same retrieval-shell used by Path A         PASS if unchanged; HOLD if any prompt
                                     so the candidate's measurement is               text differs from Path A's
                                     comparable to Path A's"

Decoding config                     "greedy, temperature=0, same as Path A           PASS if unchanged; HOLD if any decoding
                                     so deterministic measurement is preserved"      parameter differs

Six-criterion set + TP status       "same six-criterion adjudication used by         PASS if criterion definitions and TP
                                     Path A so the bounded outcome is                status are unchanged from Path A; HOLD
                                     directly comparable"                            if any criterion definition or TP
                                                                                     decision differs

Comparison framework                "single-condition bounded sentence, NOT          NS to perform: read the comparison
                                     aggregation with Path A's bounded               artifact schema; confirm it produces
                                     sentence"                                       ONE bounded sentence for Path B's
                                                                                     condition, NOT a "Path A vs Path B"
                                                                                     aggregation; HOLD if the comparison
                                                                                     artifact implies aggregation
```

CS notes that the mechanical-rendering floor (Manager Hash Integrity
close-out §8 / note §6) applies: where a load-bearing artifact admits
a mechanical rendering, that rendering is the floor of the
semantic-read. For Path B, *every* artifact above except prose-class
items admits a mechanical rendering. The runner can be read; the
model snapshot can be hashed; the criterion set can be rendered;
the comparison framework can be schema-validated.

CS will perform path/hash state-verification at the appropriate
gate (per the reinstated original gate-by-gate discipline), separate
from NS's semantic-read.

---

## §3. Main failure modes and claim-risk traps (CS-scope)

CS lists the failure modes where CS would expect to intervene
during pre-routing or pre-flight, and the language-class traps that
C5 should evaluate independently (CS flags only; C5 owns claim-risk).

### 3.1 Execution-class failure modes (CS pre-flight territory)

```text
F1. Second-model snapshot ≠ declared identity.
    Risk: a different model is loaded than the packet claims.
    Guard: B1 v2 model_snapshot_hash check at pre-flight; abort
           on mismatch.

F2. Runner contains residual multi-rung scaffolding.
    Risk: the Path A runner was the obvious starting template;
          if the rung-loop is not removed, Path B inadvertently
          re-runs Path A's structure on a new model — a Path A
          replay, not a Path B test.
    Guard: NS semantic-read of the runner; CS state-verification
           of runner sha256 against authorized hash.

F3. Sealed-byte mutation.
    Risk: any write to validation/ aborts the instrument.
    Guard: sealed-dir inventory snapshot before + after, per
           Path A's mechanism.

F4. TP-banner gap on any decision-bearing artifact.
    Risk: Manager Hash Integrity close-out §8 fix-forward — any
          future decision-bearing artifact missing TP banner
          fields is presumptively HOLD.
    Guard: every emitter (t3, t4, a6, candidate_predictions,
           tp_control_predictions if active, candidate_vs_tp_comparison)
           must carry TP banner fields; CS unit-tests at packet
           review.

F5. Per-rung adjudication discipline.
    Risk: Path B is one condition; if Path B is later compared
          to Path A by aggregation ("two clean non-eliminations"),
          this becomes the same class of error Manager close-out
          §11 (Path A) explicitly forbids.
    Guard: the comparison framework must produce ONE bounded
           sentence per condition; CS notes this is identical
           in shape to the Path A per-rung adjudication discipline
           and the per-rung adjudication discipline carries.
```

### 3.2 Claim-risk traps (CS flags; C5 evaluates)

```text
C-T1. "Two clean non-eliminations" read as generality or
      replication-in-the-strong-sense.
      The two bounded sentences (Path A's, Path B's) do NOT
      aggregate. Standing per-rung adjudication discipline carries
      directly into per-condition adjudication discipline.

C-T2. Second-model selection AFTER seeing Path A outputs.
      Manager Path A HOLD §9: "Path A outputs are negative-use
      for v2 schedule design." CS reads this as extending to
      Path B model selection: the second-model choice should be
      made on construction-intrinsic grounds (size, family,
      precision), not on observed-behavior grounds. If the second
      model is picked to maximize the chance of non-elimination,
      that is adversarial selection and the result is contaminated.

C-T3. "Path B replicated Path A" as proof of construct validity.
      A clean Path B outcome would only show that the L01-equivalent
      surface remains bounded under one more model. That is NOT
      evidence that the surface IS what Path A's label claimed —
      the same semantic-mismatch hazard from Path A applies to
      Path B's label too. The label "Path B" must not drift
      toward "second-model breadth" or "cross-model generality."

C-T4. Sliding from "second model" to "small panel of models."
      Path B is ONE condition. If a single Path B leads to "let's
      do three more for a panel," the project has slid back into
      the same lifecycle-acceleration posture Manager Path A
      suspension §3 closed. Any "follow-on of Path B" requires
      a separate Manager decision.

C-T5. Standing scope sentence omission.
      Per Manager Path A close-out §10 and Hash Integrity §3,
      the sentence "Breadth is untested under the current sealed
      schedule." must travel with any description of breadth,
      rungs, L01–L08, or Path A under the current seal. A Path B
      packet that describes Path B without this sentence is a
      C5-class HOLD.

C-T6. The figure rule.
      The Manager Path A close-out §12 "one surface = one row"
      rule binds. Path B is also one surface. Any future figure
      should not pair Path A (rung-uniform) and Path B (single-
      surface) on an axis that implies they are sample points on
      a generality dimension. They are two bounded sentences
      about two configurations, not two samples from a population.
```

---

## §4. Path B vs Option S / Path D / Consolidation — CS feedback ordering

CS offers a feedback-only path-choice recommendation. Manager decides.

```text
PATH D (stress-prerequisite taxonomy)
  Execution risk:        ZERO (documentation work; no model load)
  Sealed-byte risk:      ZERO
  Semantic-read load:    NONE for Path D itself; Path D produces the
                         taxonomy that PRECEDES any future stress work
  Epistemic value:       HIGH for project posture — names what
                         "stress-prerequisite" requires before any
                         stress-retention measurement could be valid;
                         clarifies what Paper 3 (Certification Before
                         Retention) does and does not cover; cleanly
                         downstream of the Hash Integrity discipline.
  CS recommendation:     OPEN FIRST. Lowest-risk, highest-clarification.

CONSOLIDATION (claim-ledger / Paper 3 implication updates only)
  Execution risk:        ZERO
  Sealed-byte risk:      ZERO
  Semantic-read load:    NONE
  Epistemic value:       MEDIUM — keeps the claim-ledger current with
                         the three-discipline result; integrates the
                         Hash Integrity semantic-read gate into Paper 3's
                         D1–D7 corridor (per the note's D0 recommendation);
                         keeps the project's external surface (papers)
                         coherent with internal discipline (governance).
  CS recommendation:     OPEN SECOND. Cleans up after the Hash Integrity
                         landing.

PATH B (second-condition replication of L01-equivalent non-elimination)
  Execution risk:        MEDIUM (model-facing execution; new runner;
                         new model snapshot; pre-flight + sealed-dir
                         protection required)
  Sealed-byte risk:      LOW (no sealed bytes change; instrument
                         reused verbatim) but the closed-gate posture
                         needs an explicit re-opening for ANY
                         model-facing execution
  Semantic-read load:    MEDIUM — multiple load-bearing artifacts
                         (§2.5) require shown semantic-read
  Epistemic value:       LOW — adds at most one bounded sentence on
                         the L01-equivalent surface under one more
                         model; does not open any new question; does
                         not change any closed gate
  CS recommendation:     OPEN ONLY IF the project has a specific
                         reason to want a second-model bounded
                         sentence (e.g., paper-writing or claim-ledger
                         reasons). Otherwise defer until after Path D
                         + Consolidation.

OPTION S (schedule-v2 supersession design preparation only)
  Execution risk:        HIGH eventually (a v2 schedule, if completed,
                         would lead to a true breadth run requiring
                         a fresh PH5-1-class joint lock event)
  Sealed-byte risk:      HIGH (supersession by construction touches
                         sealed bytes — the existing schedule
                         7ad3ccdd... would be retained but the project
                         would commit to producing a sealed v2)
  Semantic-read load:    HIGH — every per-rung structural axis (D, K, X
                         per D2 design proposal v0.2) needs semantic-read
                         against its instantiating bytes
  Epistemic value:       HIGHEST among the four — answers the question
                         whose absence is currently the structural
                         block: "is breadth a measurable property under
                         a properly-defined schedule?" Path A showed it
                         cannot be asked under the current seal.
  CS recommendation:     DEFER until Path D + Consolidation have
                         landed; then Manager has the framing to
                         decide whether the breadth question is worth
                         supersession-class work. Option S is the
                         right move IF the project commits to pursuing
                         breadth; the project may equally choose
                         "breadth remains untested" as a permanent
                         posture (Manager Path A close-out §7
                         Option N temporarily adopted).
```

CS's net recommendation: **Path D → Consolidation → (decide whether
to do Path B or Option S based on what those clarifications expose).**

CS's caveat: this is a CS-scope path-choice feedback. The strategic
value of any of these options depends on factors outside CS's
visibility (paper-writing schedule, funder-facing commitments,
research-program timing). CS's path-ordering is a defensible
cost-benefit read; the actual choice is Manager's.

---

## §5. What CS would commit to if Path B is opened (no commitment now)

If Manager opens Path B, CS would:

```text
- Author lane1a_runner_path_b.py as a single-condition variant of
  lane1a_runner_d4b.py (TP-active variant; single sweep, no rung loop)
- Author preconditions_path_b.json analog of preconditions_path_a.json
- Coordinate with NS on the shown semantic-read for the
  second-model snapshot and the runner
- Perform path/hash state-verification on the readiness packet
  per the original gate-by-gate discipline
- Maintain the sealed-dir protection mechanism (inventory snapshot
  before + after)
- Emit all TP-banner fields per the close-out §8 fix-forward
- File the run return per a Manager §8-equivalent return schema
- Maintain INDEX rows for every CS-authored deliverable
```

CS does not draft any of these now. CS commits to authoring them
only on Manager direction.

---

## §6. Non-actions (standing carry)

This feedback memo does not authorize, request, or initiate:

```text
Path B readiness packet drafting
Path B execution
model loading
sweep_id creation
sealed-byte change
schedule v2 drafting or supersession
true breadth rerun
Path D execution (Path D as proposed is documentation; CS does not
   initiate even that without Manager direction)
seeded-defect exercise
additional token-prior generations
scrambled-binding generations
quantization stress
INT8 / INT4
candidate selection
ranking
threshold work
certification evaluation
Claim C activation
public benchmark packaging
funder-facing release
SBIR submission
```

Sealed LOCK-RECORD v1.0 `51e18fa9…` UNCHANGED. Sealed
STRATIFIED_RECIPE_SCHEDULE `7ad3ccdd…` UNCHANGED. Filed Hash
Integrity v0.7.2 bundle UNCHANGED. D4-A / D4-B / D4-synthesis /
Path A run-of-record UNMUTATED. All successor gates CLOSED.
Process acceleration SUSPENDED for model-facing gates. Semantic-read
gate ACTIVE for all model-facing readiness packets.

— CS Engineer, 2026-06-12 (Path B direction feedback only; CS-scope artifact/path/model/runner/semantic-read requirements enumerated; CS path-choice recommendation: Path D first, then Consolidation, with Path B and Option S deferred; Manager decides)
