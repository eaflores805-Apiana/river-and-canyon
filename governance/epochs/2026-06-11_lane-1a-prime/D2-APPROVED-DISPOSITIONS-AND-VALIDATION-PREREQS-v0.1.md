# Lane 1a′ D2 Approved Dispositions & Validation Prerequisites (v0.1)

```text
DRAFT / REVIEW ONLY — D2 PACKET-STAGE ARTIFACT
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
CODE IMPLEMENTATION: CS-OWNED, IN FLIGHT — NONE HERE
NO MODEL INVOKED · NO SWEEP_ID · NO SWEEP EXECUTION · NO CANDIDATE/MODEL OUTPUTS
```

*New Senior Engineer, 2026-06-11. Consolidates the Manager/Team Lead-approved joint dispositions
into packet design text, and supplies the three design declarations that model-free validation
requires before any pilot executes: (A) the T3 comparison-rule declarations (Manager §5), (B) the
ideal-witness specification record (addendum E6: declared and reviewed before any checklist run),
(C) the Instrument Validation Report packet-stage form (empty; population authorized under the
confirmed model-free scope, by CS execution). Anti-tuning rule: every declaration here precedes any
pilot, oracle run, or manifest draw.*

## A. Approved dispositions — now packet design text (supersedes PROPOSED status)

A1. **INH-1:** stratum-specific N_effective default; pooled-96 limited to `distinct_outputs`,
`copy_completion` agreement, void accounting; type-level stratum enforcement; governance sentence
verbatim: *accuracy and abstention metrics are forbidden from cross-stratum aggregation; no declared
exception exists at packet stage; any future exception is a must-fix requiring C1 disposition.*

A2. **INH-2:** three-way totality `INCONCLUSIVE | ELIMINATED | NOT_RULED_OUT`;
`NOT_RULED_OUT` serializes `requires_further_investigation`, fires iff measurable and no
elimination label attached; `K = |{rung : outcome == NOT_RULED_OUT}|`; fixed language binds K to
"not ruled out"; evaluation-time INCONCLUSIVE triggers: void budget exceeded, required outputs
missing, harness anomaly (pilot-log, manifest-validation, and A6 failures are lock-blocking, never
rung outcomes); `boundary_proximity_flag` diagnostic-only, excluded from outcomes, K, and fixed
language; no elimination label, outcome, or statement may reference it.

A3. **Serialized elimination labels (the only wire/schema/sidecar/fixed-language forms):**
`accuracy_indistinguishable_from_token_prior` · `accuracy_indistinguishable_from_declared_policy_envelope`
· `insufficient_measurement_headroom` · `strict_content_gap_instability` ·
`null_abstention_floor_unmet` · `answerable_abstention_ceiling_exceeded`. No `fails` token in any
output artifact label.

A4. **INH-3:** Wilson without continuity correction; Newcombe–Wilson for differences; Jeffreys
fallback only; no Wald; single CI function with the source-level anti-Wald check.

A5. **Prompt shell:** VALUE_POOL visible, global, |26|, constant across rungs; token-id-sequence
lexicographic ordering under the packet's single declared tokenizer+canonicalization (same as the
`prefix_neighbor_confusion` equality predicate); queried key absent; bindings removed; baseline
1/26, empirically checked by the ideal-random-emitter oracle within IS-7 tolerance;
format-preserving per the accepted byte-identical definition with exactly one substitution;
`control_prompt_shell_hash` added to the LOCK-RECORD bound hashes.

## B. T3 comparison-rule declarations (Manager §5; declared pre-pilot)

**Uniform principle:** elimination requires the full confidence interval on the eliminating side.
Uncertainty resolves toward `NOT_RULED_OUT`, never toward elimination; data insufficiency resolves
toward `INCONCLUSIVE`. A point estimate on the eliminating side with a straddling interval does not
eliminate — it sets `boundary_proximity_flag` (this is the flag's principled definition: point
estimate beyond the criterion's bound while the interval straddles it).

| criterion (serialized label) | statistic | comparison rule [SWEEP-PARAMETER bounds] |
|---|---|---|
| accuracy_indistinguishable_from_token_prior | Newcombe–Wilson interval on (candidate − control) accuracy difference | eliminates iff difference-CI **upper bound** < declared separation margin |
| accuracy_indistinguishable_from_declared_policy_envelope | Newcombe–Wilson interval on (candidate − envelope) difference | eliminates iff difference-CI **upper bound** < declared envelope margin |
| insufficient_measurement_headroom | Wilson interval on available headroom proportion | eliminates iff headroom-CI **upper bound** < declared required headroom |
| strict_content_gap_instability | Newcombe–Wilson interval on (content − strict) gap | eliminates iff gap-CI **lower bound** > declared gap bound |
| null_abstention_floor_unmet | Wilson interval on NULL-stratum abstention rate (n=16 stratum) | eliminates iff abstention-CI **upper bound** < declared floor |
| answerable_abstention_ceiling_exceeded | Wilson interval on answerable-stratum abstention rate | eliminates iff abstention-CI **lower bound** > declared ceiling |

Ideal-witness coherence check (B4/T3, computable now): at the ideal corner the NULL abstention
interval is ≈ [0.806, 1.000]; for any declared floor ≤ 0.806 the upper bound (1.000) is never below
the floor, so the ideal witness cannot fire `null_abstention_floor_unmet`; symmetric arguments hold
for the ceiling (answerable abstention 0/80 → CI ≈ [0, 0.046]) and the gap (ideal gap 0). The
uniform principle therefore passes the perfect-model question by construction on every criterion.

## C. Ideal-witness specification record (addendum E6; for review with this document, then locked)

```json
{
  "ideal_witness_spec_version": "lane1a-prime-v1",
  "tokenizer_and_canonicalization": "<declared once for the packet; same as equality predicate>",
  "answerable_stratum": {
    "output": "<gold value for the item>",
    "format": "single-line answer per the locked template, byte-exact contract",
    "abstained": false
  },
  "null_stratum": {
    "output": "<the contract abstention string, byte-exact>",
    "format": "single-line answer per the locked template, byte-exact contract",
    "abstained": true
  },
  "expected_criterion_behavior": "passes every eliminative criterion; may fire only declared
                                  headroom-class diagnostics; never sets any elimination label"
}
```

## D. Instrument Validation Report — packet-stage form (empty; CS populates under confirmed scope)

Sections per the standing addendum §9, all result fields empty: D.1 T1 battery degeneracy audit
(per-policy/N_eff/classification/caps + envelope + A6 drift block with declared tolerance 0.05);
D.2 oracle-case verdict table (cases per Bundle Part II incl. mixture oracle — blend fraction,
component behaviors, expected_verdict columns to be declared by this seat + CS jointly *before*
pre-flight, then locked); D.3 T2 control-spec conformance fields; D.4 T3 checklist verdicts under
the §B comparison rules; D.5 T4 dispositions (INH rows now move ACCEPTED with this consolidation;
remaining packet findings tracked to zero open); D.6 pilot iteration log
(`pilot_iteration_count | failed_pilot_records_retained | reason_for_each_repilot |
changed_fields_between_pilots`); D.7 execution ledger (all nine Manager-§9 fields, template per D2
materials §9b); D.8 report-level non-claim, verbatim E16. Labeling on every artifact:
`SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION`.

## E. Confirmations (this seat, Manager §11 items 6–9)

No model was invoked. No sweep_id was created. No sweep execution occurred. No candidate/model
outputs were produced. This document is design declarations and empty forms only; the code
implementation summary and the populated execution ledger arrive from the CS side per the §7
division of ownership.

— New Senior Engineer (to Team Lead; cross-copy to CS for the joint expected-verdict declaration
before any oracle pre-flight)
