# Lane 1a Design Packet — Pre-Candidate Occupancy / Failure-Map Sweep (v0.3, consolidated)

**v0.2 → v0.3 changelog (per the consolidated conditions list, incoming+outgoing Senior):** B1
dead-rule fix — gap sign convention corrected to content − strict (the v0.1/v0.2 'strict − content'
rule could never fire, since strict-correct implies content-correct; authored by outgoing Senior,
caught by incoming Senior); B2 inconclusive-preempts rule; B3 control-scoring stratum pinned to the 80
answerable-mirroring controls; B4 token-prior authorization slot added to the LOCK-RECORD requirements
(resolves the standing unconditioned-token-prior lock by name at Manager confirmation); B5 pins
(survivor rung-ID-order unit test; total_attempts counts ALL generations, candidate + control = 1,536);
C1–C3 routed to the normative recipe (§13 of the CS execution packet, per intent-confirmation A2/A3).

**Convergence changelog (v0.1 → v0.2; all nine CS-return items adopted):** 5a SE_diff formula locked;
5b N_effective-for-headroom locked; 5c abstention_rate_se added; 5d extended-context = 2,048 tokens;
5e ladder top held at D=16; 5f no-re-execution rule added (new §1.12); 6a closed by 5f + total-attempt
audit counting; 6b outcome-statement choice rule locked as a boolean; 6c plotting prohibitions upgraded
to code-level assertions. The six §1.6 classification constants are unchanged (CS concurs). Constants
remain reviewer-adjustable BEFORE lock; never after.

From: Senior Engineer · To: Team Lead (adversarial failure-mode review), CS Engineer (execution packet),
Manager (final pre-execution confirmation) · Authorization: Manager memo of 2026-06-10 ("Lane 1a
authorized for design and execution under stated constraints only"). Framework of record:
`paper3-certification-protocol-v1.1`.

**Doctrine restated as the packet's first constraint: Lane 1a may rule out; it may not rule in.**
This packet authorizes nothing by itself; first data access requires Team Lead failure-mode review of
this packet, the CS execution packet with locked hashes, and Manager execution confirmation (§3 of the
authorization). Artifact tags on every output: `artifact_class: lane-1a-reconnaissance`,
`certification_relevance: none`.

---

## 1. Pre-registration

**1.1 Model.** Qwen2.5-3B-Instruct, FP16, mlx_lm, deterministic decoding (greedy; temperature 0; seed
and decoding flags locked in the CS execution packet). Model snapshot identity runner-attested by B1 v2
at execution; expected content hash family per the instrument of record. No other model; no other
precision. (Multi-model and INT8/INT4 remain closed.)

**1.2 Task family.** Single-hop key→value retrieval over freshly constructed synthetic entity
manifests (hop2-class family). All manifests constructed new for this sweep under B1 v2 — no inherited
artifacts (Fork A bar applies). Items are strict-scored under the Paper 1 dual-scoring discipline
(strict + content recorded; strict is primary).

**1.3 Ladder (8 rungs, fixed order L01–L08; neutral IDs — naming may not encode quality).**
Axes: distractor count **D**, key confusability **K** (low = random keys; high = shared-prefix keys —
the homogeneous-prefix axis), context load **X** (base vs. extended padding to a declared token count).

| Rung | D | K | X |
|---|---|---|---|
| L01 | 4 | low | base |
| L02 | 8 | low | base |
| L03 | 16 | low | base |
| L04 | 4 | high | base |
| L05 | 8 | high | base |
| L06 | 16 | high | base |
| L07 | 8 | low | extended |
| L08 | 8 | high | extended |

**1.4 N.** N_declared = 96 items per rung; within each rung, 80 answerable + 16 NULL-condition items
(abstention diagnostics; descriptive only). Per-rung void budget: 5 items; a rung exceeding it is
labeled `inconclusive_not_actionable` (no renormalization). Each rung additionally carries a 96-prompt
token-prior control (same template, bindings scrambled/removed, format contract preserved). Compute
envelope: 8 × 96 × 2 = 1,536 deterministic generations at 3B FP16 — small by design.

**1.5 Diagnostic axes (construction-intrinsic only; computed per rung).**
(a) strict accuracy with binomial SE; (b) content accuracy and the strict−content gap;
(c) token-prior-control accuracy with SE — computed over the 80 answerable-mirroring controls only
(denominator 80 − void_count_control); the 16 NULL-mirroring controls are retained as descriptive
abstention-prior data and enter no accuracy statistic ("correct" is ill-defined for a scrambled-binding
NULL); (d) max single declared-dummy-policy score (offline);
(e) declared-policy union-envelope score (offline); (f) ceiling headroom: 1 − strict accuracy, with
the SE-based resolvability descriptor at N_effective; (g) NULL-stratum abstention rate and
abstention-vs-error separability (descriptive); (h) tokenization-boundary stability across the
declared permutation set (offline). Declared dummy-policy battery for (d)/(e): pure last-position,
target-recency, salient-endpoint, copy-completion, homogeneous-prefix completion — deterministic
implementations, computed offline from manifests, code hashed and locked pre-access.

**1.6 Classification criteria (sweep-internal decision rules; every constant below is
[SWEEP-CLASSIFICATION — NOT A THRESHOLD VALUE]; reviewers may adjust constants BEFORE lock, never
after).** Labels attach per rung; multiple labels may attach; rules are mechanical. Locked definitions:
SE_diff = sqrt(SE(strict)² + SE(control)²), each SE computed over its own effective N (answerable-stratum
N for strict; control N for control). For the headroom rule, N_effective = 80 − void_count_answerable
(NULL-stratum items and their voids do not enter strict-accuracy headroom). The per-rung void budget of
5 counts ALL voids (answerable + NULL); exceeding it labels the rung inconclusive_not_actionable.
- `accuracy_indistinguishable_from_token_prior`: strict − control ≤ 2·SE_diff.
- `accuracy_indistinguishable_from_declared_policy_envelope`: strict ≤ envelope + 2·SE.
- `insufficient_measurement_headroom`: strict ≥ 1 − 3·SE(p̂) at N_effective (a plausible drop would sit
  inside finite-N noise).
- `strict_content_gap_instability`: gap ≥ 0.15, where **gap := content_acc − strict_acc** (sign
  convention locked; strict-correct implies content-correct, so strict ≤ content always — the prior
  'strict − content' phrasing was a dead rule, corrected here). Unit test: content 0.90 / strict 0.70
  attaches the label.
- `abstention_contract_instability`: NULL-stratum abstention outside [0.50, 0.95] of NULL items, or
  NULL/error outputs not mechanically separable by the locked classifier.
- `inconclusive_not_actionable`: void budget exceeded, missing required outputs, or harness anomaly.
  **Preempt rule (B2):** these checks evaluate FIRST; if any fires, the rung's labels are exactly
  `["inconclusive_not_actionable"]` and no other classification rule is evaluated — an unmeasurable
  rung supports no elimination. Unit test included.
- `requires_further_investigation`: attached if and only if no other label attaches. Neutral; means
  only "not ruled out under this sweep." It is not promising, viable, candidate-ready, near-certifiable,
  or suitable for positive selection.

**1.7 Output schema (locked, hash-recorded pre-access).** Per-rung record:
`rung_id, manifest_hash, N_declared, N_effective, void_count, strict_acc, strict_acc_se, content_acc,
gap, control_acc, control_acc_se, max_dummy_score, union_envelope_score, headroom, abstention_rate, abstention_rate_se (NULL-stratum n=16 ⇒ SE ≈ 0.125 at p=0.5 — coarseness made visible),
separability_flag, tokenization_stability_flag, labels[], per_item_log_path (per-item records include answer_slot_index — position-policy predictions
are auditable only if the slot is in the record), raw_output_dir,
artifact_class (= lane-1a-reconnaissance), certification_relevance (= none)`. Sweep-level record:
model attestation, all script/schema/criteria hashes, lock timestamps, audit-log references, planned_generation_count and total_attempt_count (must be equal at sweep close — see §1.12), the fixed
outcome statement (one of §1.9, verbatim), and the §1.10 exclusion block (verbatim). Survivors are stored as an unordered set serialized in rung-ID order (unit-tested); the schema contains no rank, score-sort,
preference, or "best" field by construction.

**1.8 Plotting rules (locked).** Exactly two figure types: (i) per-rung diagnostic points — one panel
per diagnostic axis, rungs on the x-axis in ladder order L01–L08, unannotated, no lines connecting
points, no smoothing, no shaded regions, no reference lines except axis zero; (ii) a rung × label grid
of discrete categorical markers. Categorical palette only; no gradient colormaps; no sorting by any
statistic; no annotations beyond axis labels and the artifact-tag footer, which appears on every
figure. Prohibited forms are enforced at code level: plot.py raises NotImplementedError on any call path toward a prohibited form (schema/code-class protection, not prose). Prohibited by enumeration: heat maps,
contours, smoothed curves, fitted boundaries, threshold lines, certification bands, viability overlays,
promising-region annotations, ranked cluster plots.

**1.9 Fixed outcome language (verbatim; one statement is emitted; choice rule locked as code).**
Let K = |{ rung : labels(rung) = {requires_further_investigation} }|. Emit the unoccupied statement iff
K = 0; otherwise emit the survivor statement with that K. The rule lives in fixed_outcome.md and the
analyzer; no human chooses the sentence.
- *All rungs eliminated:* "The certification window, while logically nonempty, was unoccupied for this
  task family at this scale: every rung carried at least one elimination label under the pre-registered
  sweep classification."
- *Otherwise:* "K of 8 rungs were not ruled out under the pre-registered sweep classification and
  remain an unordered survivor set. Survivorship is neither ranking nor positive evidence; certification
  eligibility remains undetermined pending separately authorized candidate selection and certification."
- *Appended in all cases (winner's-curse / regression expectation, §9 of the authorization):* "Any
  construction examined after this sweep is expected to perform worse during fresh certification than
  during sweep exploration; regression from sweep behavior is not instrument failure and must not be
  used to tune thresholds."

**1.10 Exclusion language (verbatim, embedded in every sweep output).** "Lane 1a outputs are excluded
from threshold design, excluded from certification evidence, and excluded from the D6
historical-information allowance for threshold derivation. A later Candidate Selection Memo may cite
this sweep only for coarse elimination; it may not rank, prefer, shortlist, or positively justify any
construction from it. A later threshold-sheet process must attest: 'No statistic computed in Lane 1a
was copied into any threshold-sheet field, directly or by transformation.'"

**1.11 B1 v2 provenance capture plan.** All manifests generated and locked under B1 v2 with hashes;
runner-attested model identity; prompt-template, scorer, dummy-policy, analysis-script, and
plotting-script hashes recorded; raw outputs retained per item; audit-log timestamps captured. The LOCK-RECORD must carry the line `Token-prior control authorization: <explicit Manager citation |
offline fallback>` — the sweep's token-prior controls are model runs in the class the standing locks
name as "unconditioned token-prior runs," and that lock is resolved BY NAME inside the artifact the
Manager confirms; absent an explicit citation, the sweep falls back to offline dummy-policy controls
only and per-rung control generations are removed from the plan. Lock order (the execution-side
firewall analog): schema + classification criteria + analysis script +
plotting script hashed and recorded → Manager execution confirmation → first data access; the first
data-access timestamp must postdate the lock record. B1 v2.1 is not used and not authorized; all
Lane 1a enforcement in this packet is achieved with B1 v2 capabilities plus locked offline scripts.

**1.12 No-re-execution rule (CS 5f).** A rung labeled `inconclusive_not_actionable` is not re-run
within this sweep; any re-sweep of that rung requires fresh Manager authorization as a new packet. The
audit log records every generation attempt; at sweep close, total_attempt_count must equal planned_generation_count (8 rungs × 96 items × 2 conditions = 1,536 —
candidate AND control generations both count; semantics pinned in AUDIT-LOG-FORMAT.md), with zero
re-executions. This
closes selective re-execution as a backdoor selection channel (CS concern 6a).

## 2. Failure-mode review (the §10 battery, answered with shown search)

*Standing question applied: assume approval, disciplined implementation, and a downstream failure
anyway.* The most credible path: **the auditable tables (required) contain per-rung accuracies; a
future human reads them as a ranking and carries "L05 looked best" into candidate selection by
memory.** No schema can delete human memory. Structural blocks below reduce the channel; the residue
is honestly wording-class, with named enforcement.

1. *Reconnaissance → pre-selection.* Structural: unordered-set serialization, ladder-order-only
   presentation, no rank/preference fields, label-only conclusions, fixed outcome language. Residual
   (wording-class): reader-side ranking from tables — enforcement vehicle: the Candidate Selection Memo
   must justify any selection on construction-design grounds and may cite Lane 1a only for
   eliminations; Manager review of that memo is the audit point; the §1.10 attestation is the artifact.
2. *Diagnostic artifact → positive evidence.* Structural: artifact tags on every record and figure;
   exclusion block embedded in outputs; B1 v2.1 backlog includes rejecting lane-1a-tagged references in
   threshold sheets/gate summaries; interim enforcement: manual threshold review (named, owned).
3. *Unordered survivors → implicit ranking.* Structural: survivor set has no order field; plots never
   sort by statistic; the neutral label is binary-attached, not graded. Shown search: I checked the
   schema for any field that could smuggle order (timestamps? — per-rung evaluation timestamps could
   imply sequence-as-preference; mitigation adopted: rungs execute in ladder order by lock, so
   timestamps encode the pre-registered order and nothing else).
4. *Visual layout → "good region."* Structural: locked plotting scripts, enumerated prohibitions,
   categorical palette, no gradients, per-axis panels rather than composite "maps." Shown search:
   reviewed each allowed figure type for emergent-region risk — the rung × label grid could read as a
   "clean column" for a survivor rung; accepted with the artifact-tag footer and the fixed outcome
   language directly beneath the grid as the mitigation (the figure cannot be excerpted without the
   non-claim).
5. *Lane 1a → threshold contamination.* Structural: the §1.10 carve-out from D6's historical-information
   allowance (authorization-level rule); the attestation sentence as a required future threshold-sheet
   artifact; classification constants are sweep-internal and labeled NOT-A-THRESHOLD at every
   occurrence. Residual: a threshold author who has *read* the sweep cannot unread it — controlled by
   role separation at the future sheet (threshold author ≠ sweep analyst where staffing permits;
   recorded exception otherwise) plus the attestation.
6. *Descriptive label → gate verdict.* Structural: label names contain no gate identifiers; this packet
   deliberately omits any label→gate mapping table from sweep outputs (the mapping exists only in this
   design document, which is not a sweep output); fixed definitions are construction-intrinsic. Shown
   search: scanned label set, schema field names, file naming (neutral L01–L08), commit-message template
   ("lane-1a reconnaissance: locked-protocol sweep outputs; no certification relevance" — fixed), and
   the EXPERIMENT_LOG entry template (fixed wording, includes the exclusion block) for gate-shaped or
   quality-shaped vocabulary; none remains.

## 3. Design parameters — resolved at Senior/CS convergence (Team Lead may still adjust BEFORE lock)

(a) the six [SWEEP-CLASSIFICATION] constants stand unchanged (Senior proposed; CS concurs);
(b) NULL stratum stays 16/96, with its coarseness now explicit via abstention_rate_se;
(c) extended-context X = 2,048 tokens (CS 5d); (d) ladder top stays D=16 — a deeper sweep is a
separately authorized future packet (CS 5e). These are sweep-design choices with no certification
meaning; the Team Lead review may adjust any of them with rationale; the lock freezes them.

## 4. What follows this packet

CS execution packet (manifest generator, runner config, scorer, dummy-policy implementations, analysis
and plotting scripts — all hashed) → Team Lead adversarial review of both packets → Manager final
execution confirmation → locked-order execution → outputs under §1.7–§1.10 → EXPERIMENT_LOG entry →
the board returns to the Manager at the candidate-selection decision point, which remains closed.

— Senior Engineer, 2026-06-10
