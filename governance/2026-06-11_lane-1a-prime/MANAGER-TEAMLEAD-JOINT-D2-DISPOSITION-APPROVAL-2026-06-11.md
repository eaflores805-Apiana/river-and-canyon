# Manager / Team Lead Joint Update — D2 Disposition Set Approved

From: Team Lead (Manager-approved)
To: New Senior Engineer, CS Engineer
Cc: Senior Engineer, Manager
Date: 2026-06-11
Re: Lane 1a′ D2 joint disposition set approved; code implementation authorized under D2 boundaries; model-free validation scope confirmed
Status: Joint semantic disposition set approved; code implementation authorized under D2; model-free validation scope confirmed; model/sweep execution gates remain closed

---

## Verbatim memo (substantive content)

> Manager has reviewed the joint D2 disposition set and approves the current direction.
>
> Team Lead disposition: **PASS**. Manager disposition: **Approved**.
>
> ## 1. Approved joint dispositions
>
> INH-1; INH-2; INH-3; prompt-shell visibility for `unconditioned_token_prior`.
>
> ## 2. INH-1 accepted
>
> Default: stratum-specific N_effective; cross-stratum aggregation requires explicit declaration. Pooled-N=96 diagnostics limited to: `distinct_outputs`, `copy_completion` agreement, `void accounting`. Governance sentence: *"Accuracy and abstention metrics are forbidden from cross-stratum aggregation. No declared exception exists at packet stage; any future exception is a must-fix requiring C1 disposition."*
>
> ## 3. INH-2 accepted
>
> Outcome model: `INCONCLUSIVE | ELIMINATED | NOT_RULED_OUT`.
> - ELIMINATED carries one or more attached descriptive elimination labels.
> - NOT_RULED_OUT serializes the inherited label string `requires_further_investigation`; fires iff the rung is measurable and no elimination label attached.
> - K = |{rung : outcome == NOT_RULED_OUT}|.
> - `boundary_proximity_flag` is diagnostic-only; excluded from outcome / K / fixed language; reported only in diagnostics / sidecar context; no elimination label, outcome, or fixed statement may reference it.
>
> ## 4. Accepted serialized elimination labels
>
> Descriptive strings only:
> - `accuracy_indistinguishable_from_token_prior`
> - `accuracy_indistinguishable_from_declared_policy_envelope`
> - `insufficient_measurement_headroom`
> - `strict_content_gap_instability`
> - `null_abstention_floor_unmet`
> - `answerable_abstention_ceiling_exceeded`
>
> No `fails` token in any output artifact label. Internal enum names remain CS choice; serialized values must be descriptive.
>
> ## 5. INH-3 accepted
>
> Wilson without continuity correction; Newcombe-Wilson hybrid for differences; Jeffreys fallback only; no Wald; single CI function; source-level anti-Wald check. Before lock, each T3 criterion must declare whether it compares point estimate / CI lower bound / CI upper bound / difference interval against its declared floor or ceiling.
>
> ## 6. Prompt-shell visibility accepted
>
> VALUE_POOL visible, global, |VALUE_POOL|=26, constant across rungs, lexicographic by token-id sequence, queried key absent, value bindings removed, baseline = 1/|VALUE_POOL|. Format-preserving: locked header, instruction block, format contract, and Q/A scaffold byte-identical to answerable prompt; exactly one substitution (key-value-pairs block → Available values flat list); queried key absent from Q scaffold.
>
> ## 7. Code implementation authorization under D2
>
> CS may now begin code implementation under D2. Authorized: runner source; wrapper source; schemas; policy modules; control modules; A6 machinery; lock_packet machinery; tests; dry-run interface checks; non-executing packet infrastructure.
>
> **Writing source code is authorized. Invoking source code against a model is not authorized.**
>
> ## 8. Model-free validation scope (Manager confirms)
>
> D2 authorizes model-free instrument validation work required by the Pre-Lock Instrument Validation Addendum.
>
> Authorized: pilot manifest construction; deterministic dummy-policy execution against pilot manifests; oracle-case pre-flight against synthetic/oracle records; A6 final-manifest re-verification; T1–T4 validation result-field population; Instrument Validation Report preparation.
>
> Artifacts labeled `SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION`. May be used only to determine instrument lock-eligibility. May NOT be used for candidate selection / ranking / threshold derivation / certification / retention claims / model capability claims / Claim C.
>
> ## 9. Execution ledger required
>
> First model-free validation return must include:
> - `what_was_generated`
> - `what_was_computed`
> - `files_created`
> - `artifact_hashes`
> - confirmation no model was invoked
> - confirmation no sweep_id was created
> - confirmation no sweep execution occurred
> - confirmation no candidate/model outputs were produced
> - confirmation all outputs are validation-only and non-binding
>
> ## 10. Still not authorized
>
> Model runs; sweep execution; new sweep_id; `unconditioned_token_prior` model generations; `scrambled_binding_retrieval` model generations; candidate selection; ranking; threshold-sheet work; certification evaluation; stress-retention testing; B1 v2.1 implementation; Paper 3 revision; Claim C activation; Fork A reactivation; Paper 6 activation; public benchmark packaging; D3 acceptance; D4 sweep authorization; D5 close-out acceptance.
>
> ## 11. Required return
>
> Code implementation summary; updated packet artifacts; model-free validation execution ledger; T1–T4 validation packet materials; Instrument Validation Report draft or packet-stage form; four confirmations (no model invoked; no sweep_id; no sweep execution; no candidate/model outputs).
>
> ## 12. Team Lead final direction
>
> **Proceed with D2 code implementation and model-free validation work under the boundaries above. Do not invoke any model. Do not create a sweep_id. Do not execute the sweep. Do not open D3, D4, or D5.**
>
> — Team Lead (Manager-approved)

---

CS posture: D2 implementation work-start acknowledgement filed alongside this memo.

— CS Engineer, 2026-06-11
