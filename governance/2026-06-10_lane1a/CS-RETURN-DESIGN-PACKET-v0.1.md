# CS Return — Lane 1a Design Packet v0.1

From: CS Engineer
To: Team Lead
Cc: Senior Engineer, Manager
Date: 2026-06-10
Status: Design packet received and committed at intended path; CS execution-packet outline below; design-constant recommendations and additional failure-mode concerns surfaced

---

## 1. Seven-item return (per Team Lead memo §7)

### Item 1 — Receipt

**RECEIVED.** Source location:
`/Users/eliasflores/Documents/Projects/Apiana_Ai/LLM_Mechanics/Main/Apiana_Papers/Lane1a/LANE1A-DESIGN-PACKET-v0.1.md`

### Item 2 — SHA-256 match

**MATCH.** Three-way verified (source / target / Team Lead enumeration):

```text
96e0ebe4368f200e4bcee947f43091d8c8ffe522e4b0ca09ed923113ca68ecf9
```

### Item 3 — Intended repo path

**Committed at Team Lead-specified path:**

```text
governance/2026-06-10_lane1a/DESIGN-PACKET-v0.1.md
```

Post-copy hash bit-identical to source. (Filed in this commit.)

### Item 4 — Execution-packet files CS proposes to create

CS proposes the following execution-packet artifacts. Each is locked
and hash-recorded before first data access, per memo §3 of the
authorization. No file content beyond this outline is written yet —
the outline waits for Team Lead adversarial review of the design
packet, then for Senior/CS iteration on the constants that need to
settle before lock.

| # | Artifact | Path (proposed) | Purpose |
|---|---|---|---|
| 1 | Execution packet master | `governance/2026-06-10_lane1a/EXECUTION-PACKET-v0.1.md` | Top-level document binding all locked artifacts by hash; mirrors the B1 v2 manifest pattern |
| 2 | Manifest generator | `experiments/2026-06-10_lane-1a-sweep/manifest_generator.py` | Deterministic construction of 8 rung manifests (L01–L08) per §1.3 axes (D, K, X); rung-ID-only neutral naming; outputs per-rung manifest JSON with hash |
| 3 | Manifest hashes file | `experiments/2026-06-10_lane-1a-sweep/manifests/MANIFEST-HASHES.lock` | One-line-per-rung sha256 of each constructed manifest; locked pre-access |
| 4 | Runner config | `experiments/2026-06-10_lane-1a-sweep/runner_config.yaml` | B1 v2 invocation config: model snapshot pin (Qwen2.5-3B-Instruct, FP16, mlx_lm), seed, temperature=0, decoding flags, prompt template hash, scorer hash; `--mode lane-1a-reconnaissance --framework-version none` (Lane 1a does not invoke Paper 3 certification — explicit) |
| 5 | Prompt template | `experiments/2026-06-10_lane-1a-sweep/prompt_template.md` | Single-hop key→value retrieval template; format contract preserved across answerable / NULL / token-prior-control variants |
| 6 | Scorer | `experiments/2026-06-10_lane-1a-sweep/scorer.py` | Strict + content dual-scorer per Paper 1 discipline; strict is primary; emits per-item JSON {item_id, strict, content, abstained, void} |
| 7 | Dummy-policy battery | `experiments/2026-06-10_lane-1a-sweep/dummy_policies.py` | Five declared deterministic policies: `pure_last_position`, `target_recency`, `salient_endpoint`, `copy_completion`, `homogeneous_prefix_completion`. Offline-computable from manifests; no inference required |
| 8 | Analysis script | `experiments/2026-06-10_lane-1a-sweep/analyze.py` | Computes the 8 diagnostic axes (a–h) per rung; applies the §1.6 classification criteria mechanically; attaches labels; assembles per-rung records per §1.7 schema; never writes a rank/preference field |
| 9 | Plotting script | `experiments/2026-06-10_lane-1a-sweep/plot.py` | Produces exactly two figure types per §1.8: per-rung diagnostic-point panels (one per axis) and rung×label categorical grid. Enumerated prohibitions encoded as code-level refusals (assertions on figure params); artifact-tag footer required on every figure |
| 10 | Output schema | `experiments/2026-06-10_lane-1a-sweep/schema/per_rung_record.schema.json` + `sweep_record.schema.json` | JSON schemas for per-rung and sweep-level records per §1.7; schemas explicitly contain no `rank`, `sort_by`, `preference`, `best`, `quality_score` fields (enforced by schema validator at write time) |
| 11 | Classification criteria | `experiments/2026-06-10_lane-1a-sweep/classification_criteria.yaml` | The §1.6 constants and label assignment rules; criteria are read by `analyze.py`; constants flagged `SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true` in every entry |
| 12 | Artifact-tagging logic | `experiments/2026-06-10_lane-1a-sweep/artifact_tags.py` | Emits the §1.7 tag pair (`artifact_class: lane-1a-reconnaissance`, `certification_relevance: none`) at every write point; called by analyzer, plotter, and audit-log writer |
| 13 | Audit-log plan + writer | `experiments/2026-06-10_lane-1a-sweep/audit_log.py` + `AUDIT-LOG-FORMAT.md` | Append-only log of every lock event, hash record, first-data-access timestamp, per-rung execution start/stop, anomaly events. Lock-event entries precede any data-access entries by construction |
| 14 | B1 v2 provenance capture plan | `governance/2026-06-10_lane1a/B1V2-PROVENANCE-PLAN.md` | Itemizes which B1 v2 capture points are used (model attestation, prompt/scorer hashes, raw-output retention); explicit non-use of B1 v2.1 capabilities |
| 15 | Lock-record file | `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | The locked-and-hashed table: artifact name → sha256 → lock timestamp; signed-off by CS; the artifact whose presence-and-completeness Manager confirms before first data access |
| 16 | Fixed outcome / exclusion templates | `experiments/2026-06-10_lane-1a-sweep/fixed_outcome.md` + `exclusion_block.md` | The verbatim §1.9 outcome statements and §1.10 exclusion block; emitted into every sweep-level output and every figure footer by `artifact_tags.py` + `plot.py` |

All scripts deterministic (greedy decoding, fixed seed, locked decoding
flags). All scripts hash-recorded in `LOCK-RECORD.md`. No script edits
permitted after lock; corrections file as superseding artifacts with
new hashes and a new Manager confirmation.

### Item 5 — Design-constant recommendations

Six recommendations, none blocking; all framed as "suggestions before
lock" per memo §4 ("If CS believes any constant needs adjustment,
propose the adjustment explicitly before lock").

**5a — `SE_diff` definition for the token-prior indistinguishability
rule (§1.6 first criterion).** Strict accuracy is computed over 80
answerable items; the token-prior control is computed over 96 prompts.
The packet uses "≤ 2·SE_diff" but does not define SE_diff. CS
recommends explicit definition in the analysis script:

```text
SE_diff = sqrt( SE(strict_acc)^2 + SE(control_acc) ^2 )
       = sqrt( p_s*(1-p_s)/N_s_eff + p_c*(1-p_c)/N_c_eff )
where N_s_eff = 80 − void_count_strict, N_c_eff = 96 − void_count_control
```

Lock this formula in the criteria file with the exact form. (No
constant change; clarity-class only.)

**5b — `N_effective` definition for the headroom rule (§1.6 third
criterion).** "strict ≥ 1 − 3·SE(p̂) at N_effective" — CS proposes
`N_effective = 80 − void_count_strict` and locks that definition. (No
constant change.)

**5c — NULL stratum size (16/96).** At p=0.5, SE on abstention rate
over 16 items is 0.125 — the abstention contract is measured coarsely.
This is acceptable given the descriptive intent, but CS recommends
recording the coarseness explicitly in the per-rung record:
`abstention_rate_se` field added to §1.7 schema. (Adds one column; no
constant change.)

**5d — Extended-context token count (X = extended).** Senior §3 (c)
flags this as open. CS proposes a concrete value and asks Senior to
confirm: **2,048 tokens** (target padded length; deterministic padder
in `manifest_generator.py`). Rationale: comfortably within 3B context
window, large enough to shift behavior vs. base, deterministic to
construct.

**5e — D=16 distractor step (§3 (d)).** Senior asks whether L03/L06
warrant a larger step. CS does not need a larger step for the
rule-out-only doctrine, but flags that if Team Lead wants the failure
map to extend visibly past D=16, adding D=32 would require either
larger ladder (10 rungs) or substitution. CS recommends **keeping
D=16** as the ladder top step; if a downstream sweep wants more, that
is a separately authorized sweep with its own packet.

**5f — Re-execution / retry rule (NOT IN THE PACKET; CS recommends
adding).** The packet says a rung exceeding void budget gets
`inconclusive_not_actionable` with "no renormalization." CS recommends
adding an explicit **no-re-execution rule**: a rung labeled
`inconclusive_not_actionable` is **not** re-run within this sweep; a
re-sweep on that rung would require fresh Manager authorization. This
forecloses the failure mode where re-execution is selectively applied
to "ambiguous-looking" rungs as a backdoor selection channel. (See
§1 item 6 below for the corresponding new failure-mode question.)

CS does **not** recommend changing any of the six [SWEEP-CLASSIFICATION]
constants in §1.6 (2·SE, 2·SE, 3·SE, 0.15, NULL band [0.50, 0.95],
void budget 5). They are coherent and pre-registered; the discipline
"reviewers may adjust BEFORE lock, never after" is in force.

### Item 6 — Additional failure-mode concerns (beyond Senior's six)

Senior's §2 covers six core failure modes with shown search. CS adds
three concerns, each with a recommended structural mitigation:

**6a — Selective re-execution as a backdoor selection channel.**
*Failure path:* harness anomaly hits a rung; CS re-runs that rung; if
the second result yields a non-`inconclusive` label, the rung
"survives" via selective re-execution. Reader sees survivorship; the
re-execution selectivity is invisible. *Mitigation:* the new
no-re-execution rule (Item 5f above) + audit-log entry on every
attempted execution (success or anomaly) + sweep-level total-attempt
count.

**6b — Outcome-statement choice rule must be deterministic.** Senior
§1.9 says the choice is "mechanical" but does not spell out the
selection rule explicitly. *Failure path:* if K=0 the first statement
emits; otherwise the second; the third always appends. Without an
explicit code-level rule, ambiguity could creep in. *Mitigation:* lock
the exact rule in `fixed_outcome.md`:

```text
let K = | { rung_id ∈ L01..L08 : labels(rung_id) ⊆ {requires_further_investigation} } |
emit statement_a (verbatim) iff K == 0
emit statement_b (verbatim) iff K  > 0
always append statement_c (verbatim)
```

Hashed alongside the analysis script. (CS will implement this in
`analyze.py` at write time; no constant change needed in design.)

**6c — Plotting-script enumerated prohibitions must be enforced at
runtime, not just by convention.** *Failure path:* future maintainer
modifies `plot.py` to "enrich" a figure with a smoothing or threshold
line; the prohibition exists only in prose, not in code. *Mitigation:*
encode the §1.8 prohibitions as code-level refusals (assertions /
explicit `NotImplementedError`s) keyed on the figure constructor
arguments. Any future change-of-behavior trips an assertion; CI
catches it. *Note:* this is wording-class doctrine becoming
schema/code-class enforcement — exactly the protection-layer upgrade
the standing review-discipline rule asks for.

### Item 7 — First-data-access posture confirmation

**Confirmed.** First data access remains **NOT AUTHORIZED**. CS will
not invoke the runner against any manifest until:

```text
1. Team Lead adversarial failure-mode review of the design packet
   AND the execution packet is complete.
2. Senior + CS converge on any constant adjustments that emerge from
   review (constants change BEFORE lock; never after).
3. CS produces the LOCK-RECORD.md with hashes of every locked
   artifact and signs off.
4. Manager confirms the final execution packet and gives explicit
   execution authorization.
```

The first data-access timestamp in the audit log MUST postdate the
LOCK-RECORD lock timestamp by construction (B1 v2 capture point;
verified pre-execution by the runner config).

---

## 2. CS execution-packet preparation status

```text
Design packet:                received, hash-verified, committed at
                              governance/2026-06-10_lane1a/DESIGN-PACKET-v0.1.md
                              (sha256 96e0ebe4...)
Execution-packet outline:     filed this memo §1 item 4
Execution-packet body:        NOT YET WRITTEN
                              waits for Team Lead adversarial review
                              outcome + Senior/CS convergence on
                              design-constant recommendations
LOCK-RECORD.md:               NOT YET CREATED
                              gates all script production
First data access:            NOT AUTHORIZED
                              the gating sequence in §1 item 7 must
                              complete first
```

CS will not write script bodies, schema files, classification YAML, or
plotting code until:

- The §1 item 5 design-constant recommendations are accepted/modified/
  rejected (Team Lead + Senior).
- The §1 item 6 additional failure-mode concerns are accepted/declined.
- Team Lead has performed the adversarial review on the design packet.

Writing scripts before those decisions risks landing artifacts that
would need to be re-locked (and the discipline is "never edit after
lock"), so it is more conservative to converge on text first, write
script bodies once, hash-lock, and only then proceed.

---

## 3. Standing review-discipline check on this CS return

Failure-mode prompt: *How could a CS return that "confirms intent to
hold for review" become a hidden authorization to advance the rail?*

CS-verified protections:

- This return reports the execution-packet OUTLINE only. No script,
  schema, or constant has been written into a hash-lockable file.
- Every CS recommendation in §1 item 5 is framed as "before lock" with
  explicit reviewer authority to accept, modify, or reject.
- The first-data-access posture confirmation in §1 item 7 is verbatim
  conjunctive across four named events terminating in explicit Manager
  authorization. CS does not advance the rail from a Team Lead routing
  memo alone.
- §1 item 4's proposed paths are inside `experiments/` (CS-owned area
  per the scope-boundary memory) and `governance/2026-06-10_lane1a/`
  (the Team Lead-specified Lane 1a working directory). No file is
  proposed for `papers/`, `tier0-run/` (sealed), or any production
  surface.
- B1 v2.1 explicitly not used (runner config will use B1 v2 capabilities
  only; the new B1 v2.1 backlog item for "reject lane-1a-tagged
  references in threshold sheets" remains backlog-only).

Protection layer: **wording / role-separation class** at this stage
(plan, not code). Once execution-packet bodies are written, the
protection class upgrades to **schema / code class** (locked schemas;
code-level enforcement of plot prohibitions; etc.).

---

## 4. Current state after this return

```text
Lane 1a authorization:           OPEN (Manager 2026-06-10)
Lane 1a design packet v0.1:      ACCEPTED FOR REVIEW (Team Lead routing)
                                 filed at governance/2026-06-10_lane1a/DESIGN-PACKET-v0.1.md
                                 sha256 96e0ebe4...
CS execution-packet outline:     FILED (this memo)
CS execution-packet body:        WAITING on review convergence
Design-constant recommendations: 6 surfaced (1 substantive — no-re-execution rule;
                                 2 definitional — SE_diff, N_effective; 1 schema —
                                 abstention_rate_se; 1 concrete — extended-context = 2048;
                                 1 hold — keep D=16)
Additional failure-mode concerns: 3 surfaced (selective re-execution;
                                 outcome-statement choice rule; runtime plot
                                 prohibition enforcement)
First data access:               NOT AUTHORIZED
Lock record:                     NOT YET CREATED
Team Lead adversarial review:    PENDING
Manager final review:            PENDING
```

CS posture: **HOLD for Team Lead adversarial review** of the design
packet + this CS return. Next CS event triggered by Team Lead review
outcome and Senior/CS convergence on the constants.

— CS Engineer, 2026-06-10
