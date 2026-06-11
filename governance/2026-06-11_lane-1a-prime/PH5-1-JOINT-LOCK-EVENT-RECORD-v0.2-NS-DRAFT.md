# PH5-1 Joint Lock-Event Record (v0.2 — NS side complete; CS slots open)

*v0.2: §3 revised per the stratified-recipe blocker adjudication (item-label disjointness accepted;
geometric impossibility of policy-hit disjointness on record; pure_last_position expected constant
corrected to 0.30). No other section changed; no verdict, bound, blend, or policy definition moves.*

```text
JOINT LOCK-EVENT RECORD — Lane 1a′ corrective Phase 5 prerequisites
NO CORRECTIVE RUN-3 UNTIL THIS RECORD IS FILED AND TEAM LEAD PASSES IT
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION · LOCK-RECORD PENDING
```

*Assembled in parallel per the Team Lead ordering memo: NS items final below; CS items are
structured slots that CS completes with paths/hashes/implementation confirmations; then joint
review, co-signature, Team Lead filter, and only then corrective run-3 under the approved model-free
D2 boundary.*

## 1. Oracle verdict table (NS final)

- Document: `ORACLE-EXPECTED-VERDICT-DECLARATION-v0.3-LOCK-CANDIDATE.md`
- NS-side sha256: `0e01ce2c374a05db80bdcefbcc925e5c24ed1566589dbc934fb56ac8e865c375`
- Contents at lock: twelve cases (ORC-01…12); four label-set fields per case; four-clause match
  predicate (outcome_matched · required_labels_present · required_absent_labels_absent ·
  only_required_or_permitted_attached); ORC-10 tightened wording incorporated; blends locked at
  0.75/0.25.
- **Repo path and committed sha256:** [CS SLOT]

## 2. T3 bounds declaration (NS final; co-signed values)

```text
FLOOR (null_abstention_floor_unmet):                 0.75   fires iff NULL-abstention CI upper < 0.75
CEIL  (answerable_abstention_ceiling_exceeded):      0.20   fires iff answerable-abstention CI lower > 0.20
TP_margin (accuracy_indistinguishable_from_token_prior):     0.10   fires iff (cand − control) CI upper < 0.10
ENV_margin (accuracy_indistinguishable_from_declared_policy_envelope): 0.10   fires iff (cand − envelope) CI upper < 0.10
HEAD (insufficient_measurement_headroom):            0.15   fires iff (1 − envelope) CI upper < 0.15
                                                      [declared B4 headroom-class exception]
GAP  (strict_content_gap_instability):               0.30   fires iff (content − strict) CI lower > 0.30
```

Comparison framework: uniform principle — elimination requires the full interval on the eliminating
side; straddle with point estimate beyond the bound sets `boundary_proximity_flag` (diagnostic-only);
data insufficiency → INCONCLUSIVE. Intervals: Wilson without continuity correction; Newcombe–Wilson
for differences; single CI function; anti-Wald source check. All six criteria active — no deferred
bounds; no criterion inactive. Every value [SWEEP-PARAMETER]; anti-tuning quarantine on record (all
rationales construction-derived; no run-1/run-2 statistic in any rationale).
- **Bounds artifact repo path and committed sha256:** [CS SLOT]

## 3. Stratified recipe schedule constants (NS final; CS implementability confirmed at co-signature)

```text
Per rung, answerable stratum (80): gold_at_last_position 12 · gold_at_salient_endpoint 12 ·
gold_in_prefix_neighborhood 12 · gold_recency_adjacent 12 · no_structural_feature 32
NULL stratum: 16 (contract abstention). Strata disjoint by construction; assignment shuffled
within strata by the locked seed; identical schedule for pilot and final manifests.
Disjointness semantics (per the blocker adjudication, which governs): **the schedule is
item-label-disjoint, not fully policy-hit-disjoint** — full policy-hit disjointness between
pure_last_position and any recency-adjacent construction is geometrically unconstructible (every
recency-adjacent hit co-occurs with a pure_last_position hit, both target placements). The union
envelope remains 48/80 = 0.60 by intended item-label construction. Deterministic per-policy
constants: pure_last_position 24/80 = 0.30 (its 12 + the 12 recency co-hits; below the 0.50 cap);
salient_endpoint, recency_excluding_target, prefix_neighbor_confusion 12/80 = 0.15 each. The
eliminative machinery is union-based and overlap-insensitive, so the instrument's intended
semantics — not merely the envelope number — are preserved. Expected A6 drift 0.00 under faithful
implementation (declared tolerance 0.05 unchanged).
```
- **Schedule artifact repo path and committed sha256:** [CS SLOT]
- Per-rung-class adjustment for K=low prefix-neighborhood constructibility, if CS requires:
  [CS SLOT — none assumed; any adjustment is recorded here before signature, not after]

## 4. ORC-08 cleanup confirmation (NS)

Applied in the v0.3 lock candidate: HEAD removed from ORC-08 `permitted_co_labels`
(now `TP, ENV`), per the corrected envelope-derived HEAD semantics. Verified by direct row
inspection; the v0.3 hash above includes this change.

## 5–6. Signatures

- **NS signature:** New Senior Engineer, 2026-06-11 — signs items 1–4 and 9–14 as final on the
  design side, conditional only on CS slot completion matching the NS-side hashes above.
- **CS signature:** [CS SLOT — signs paths, hashes, config precondition, refusal check]

## 7. Validation-config hash precondition (CS implements; NS text final)

The validation config carries three required fields: `oracle_table_sha256`, `t3_bounds_sha256`,
`recipe_schedule_sha256`. Each must be present and must match the committed artifact byte-for-byte.
- **Config path and field confirmation:** [CS SLOT]

## 8. Pre-flight refusal confirmation (CS)

Pre-flight mechanically refuses to run if any of the three hashes is absent or mismatched
(PacketLockRefused pattern; PH5-4). Any post-lock change to any bound, count, blend, or verdict is
a C1 must-fix.
- **Refusal-check implementation + test reference:** [CS SLOT]

## 9. Run-1 / run-2 supersession record (NS language final; CS paths)

Phase 5 run-1 and run-2 are **superseded and retained** per addendum E11: `superseded_run-1/` and
`superseded_run-2/` paths preserve all artifacts with hashes; the IVR retention block carries
`failed_pilot_records_retained`, `reason_for_each_repilot` (run-1: reduced-criteria run; unlocked
verdict table; unstratified recipe; A6 drift exceedance — run-2: [CS records run-2's documented
reasons]), and `changed_fields_between_pilots`. A passing run-3 erases nothing; run-1 and run-2
remain auditable forever, and their numeric levels are quarantined from all bound rationales.
- **Retention paths and hashes:** [CS SLOT]

## 10–14. Confirmations (NS side; CS re-confirms at signature)

No model was invoked. No model was loaded. No sweep_id was created. No sweep execution occurred.
LOCK-RECORD remains PENDING. Corrective run-3 is not requested by this record; it proceeds only
after Team Lead filters and passes the filed record.

**Boundary and non-claim text (NS final, carried into the record):** all run-3 artifacts are
`SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION`; they determine instrument
lock-eligibility only; instrument validation ≠ model evaluation; Lane 1a′ may rule out and may not
rule in; passing the declared battery does not rule out undeclared shortcuts or partial shortcut
contribution — permitted phrasing "not explained by the declared shortcut battery," forbidden
phrasing "not shortcut-driven."

— New Senior Engineer (NS side filed; to CS for slot completion and co-signature; then Team Lead)
