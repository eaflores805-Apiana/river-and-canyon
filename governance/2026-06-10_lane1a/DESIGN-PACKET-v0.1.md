# Lane 1a Design Packet — Pre-Candidate Occupancy / Failure-Map Sweep (v0.1, for review)

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
(c) token-prior-control accuracy with SE; (d) max single declared-dummy-policy score (offline);
(e) declared-policy union-envelope score (offline); (f) ceiling headroom: 1 − strict accuracy, with
the SE-based resolvability descriptor at N_effective; (g) NULL-stratum abstention rate and
abstention-vs-error separability (descriptive); (h) tokenization-boundary stability across the
declared permutation set (offline). Declared dummy-policy battery for (d)/(e): pure last-position,
target-recency, salient-endpoint, copy-completion, homogeneous-prefix completion — deterministic
implementations, computed offline from manifests, code hashed and locked pre-access.

**1.6 Classification criteria (sweep-internal decision rules; every constant below is
[SWEEP-CLASSIFICATION — NOT A THRESHOLD VALUE]; reviewers may adjust constants BEFORE lock, never
after).** Labels attach per rung; multiple labels may attach; rules are mechanical:
- `accuracy_indistinguishable_from_token_prior`: strict − control ≤ 2·SE_diff.
- `accuracy_indistinguishable_from_declared_policy_envelope`: strict ≤ envelope + 2·SE.
- `insufficient_measurement_headroom`: strict ≥ 1 − 3·SE(p̂) at N_effective (a plausible drop would sit
  inside finite-N noise).
- `strict_content_gap_instability`: strict−content gap ≥ 0.15.
- `abstention_contract_instability`: NULL-stratum abstention outside [0.50, 0.95] of NULL items, or
  NULL/error outputs not mechanically separable by the locked classifier.
- `inconclusive_not_actionable`: void budget exceeded, missing required outputs, or harness anomaly.
- `requires_further_investigation`: attached if and only if no other label attaches. Neutral; means
  only "not ruled out under this sweep." It is not promising, viable, candidate-ready, near-certifiable,
  or suitable for positive selection.

**1.7 Output schema (locked, hash-recorded pre-access).** Per-rung record:
`rung_id, manifest_hash, N_declared, N_effective, void_count, strict_acc, strict_acc_se, content_acc,
gap, control_acc, control_acc_se, max_dummy_score, union_envelope_score, headroom, abstention_rate,
separability_flag, tokenization_stability_flag, labels[], per_item_log_path, raw_output_dir,
artifact_class (= lane-1a-reconnaissance), certification_relevance (= none)`. Sweep-level record:
model attestation, all script/schema/criteria hashes, lock timestamps, audit-log references, the fixed
outcome statement (one of §1.9, verbatim), and the §1.10 exclusion block (verbatim). Survivors are
stored as an unordered set serialized in rung-ID order; the schema contains no rank, score-sort,
preference, or "best" field by construction.

**1.8 Plotting rules (locked).** Exactly two figure types: (i) per-rung diagnostic points — one panel
per diagnostic axis, rungs on the x-axis in ladder order L01–L08, unannotated, no lines connecting
points, no smoothing, no shaded regions, no reference lines except axis zero; (ii) a rung × label grid
of discrete categorical markers. Categorical palette only; no gradient colormaps; no sorting by any
statistic; no annotations beyond axis labels and the artifact-tag footer, which appears on every
figure. Prohibited forms per the authorization §6 are prohibited here by enumeration: heat maps,
contours, smoothed curves, fitted boundaries, threshold lines, certification bands, viability overlays,
promising-region annotations, ranked cluster plots.

**1.9 Fixed outcome language (verbatim; one statement is emitted, chosen mechanically).**
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
plotting-script hashes recorded; raw outputs retained per item; audit-log timestamps captured. Lock
order (the execution-side firewall analog): schema + classification criteria + analysis script +
plotting script hashed and recorded → Manager execution confirmation → first data access; the first
data-access timestamp must postdate the lock record. B1 v2.1 is not used and not authorized; all
Lane 1a enforcement in this packet is achieved with B1 v2 capabilities plus locked offline scripts.

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

## 3. Open design parameters for review (decide BEFORE lock; never after)

(a) the six [SWEEP-CLASSIFICATION] constants in §1.6 (2·SE, 3·SE, 0.15 gap, abstention band, void
budget 5); (b) NULL-stratum size (16/96); (c) extended-context token count for X=extended; (d) whether
L03/L06 (D=16) warrant a larger distractor step. These are sweep-design choices with no certification
meaning; reviewers may adjust with rationale; the lock freezes them.

## 4. What follows this packet

CS execution packet (manifest generator, runner config, scorer, dummy-policy implementations, analysis
and plotting scripts — all hashed) → Team Lead adversarial review of both packets → Manager final
execution confirmation → locked-order execution → outputs under §1.7–§1.10 → EXPERIMENT_LOG entry →
the board returns to the Manager at the candidate-selection decision point, which remains closed.

— Senior Engineer, 2026-06-10
