# Manager / Team Lead Direction — Lane 1a MODEL_ID Remediation (Path A.1)

From: Elias / Manager
To: CS Engineer
Cc: Senior Engineer, Team Lead, New Senior Engineer
Date: 2026-06-10
Status: Path A.1 selected; CS executing remediation; first data access NOT authorized

---

## Verbatim memo

> CS,
>
> Manager and Team Lead acknowledge the deviation report at commit
> `4f26368`. CS correctly stopped at deviation discovery.
>
> ## 1. Finding accepted (release/execution-blocking)
>
> B1 v2 MODEL_ID is `Qwen/Qwen2.5-3B-Instruct`; lane1a_runner MODEL_ID is
> `mlx-community/Qwen2.5-3B-Instruct-bf16`. Not acceptable. Manager
> does not authorize a different model identity.
>
> ## 2. Remediation decision: **Path A.1** — fix MODEL_ID in
> `lane1a_runner.py` to `"Qwen/Qwen2.5-3B-Instruct"`.
>
> Do not proceed with `mlx-community/Qwen2.5-3B-Instruct-bf16`. Do not
> trigger a download of a different distribution variant. Do not accept
> provenance divergence. Do not edit B1 v2.
>
> ## 3. Authorized remediation work
>
> (1) update MODEL_ID to `Qwen/Qwen2.5-3B-Instruct`;
> (2) add unit test `test_model_id_matches_b1v2`;
> (3) cross-reference MODEL_ID against B1 v2 source;
> (4) re-run test suite;
> (5) re-seal LOCK-RECORD;
> (6) return remediation report with hashes.
>
> ## 4. Standing rule addition accepted
>
> > *CS production of any artifact that integrates with a locked sibling
> > artifact must include a unit test that cross-references concrete
> > values against the sibling artifact's source.*
>
> Applies to MODEL_IDs, schema field names, required manifest fields,
> CLI constants, mode/context names, framework-version behavior,
> artifact tags, provenance fields.
>
> Add to standing review discipline. Lane 1a manifest-interface
> deviation and MODEL_ID deviation are canonical examples.
>
> ## 5. Required CS return (12 items)
>
> [list with hashes, test_model_id_matches_b1v2 PASS confirmation,
> MODEL_ID exact-value confirmation, no first-data-access / no
> model-load / no live outputs / no B1 v2 edit / no B1 v2.1 / any
> remaining concern.]
>
> ## 6. Review sequence after remediation
>
> CS return → Senior confirms design + provenance intent → Team Lead
> combined re-review → CS lock-finalization → Manager reauthorization
> → CS preflight → CS execute. **Prior Manager authorization does NOT
> carry forward.**
>
> ## 7. Non-authorizations [15 enumerated; all in force]
>
> ## 8. Disposition
>
> Path A.1 selected. MODEL_ID must match B1 v2 exactly. B1 v2 unedited.
> B1 v2.1 unauthorized. First data access NOT AUTHORIZED.
>
> — Elias / Manager

---

## CS acknowledgement and execution declaration

CS confirms:

1. **Path A.1 authorized; CS proceeds.** Single-line MODEL_ID change in
   `lane1a_runner.py`; new `test_model_id_matches_b1v2` unit test;
   re-sealed LOCK-RECORD with `Lock timestamp: PENDING_TEAM_LEAD_REVIEW`
   (because the prior authorization does not carry forward).
2. **MODEL_ID will be `"Qwen/Qwen2.5-3B-Instruct"`** verbatim — read
   directly from B1 v2 source by the unit test for ongoing cross-
   reference verification.
3. **Standing review-discipline addition will be filed** at
   `governance/standing/STANDING-REVIEW-DISCIPLINE.md` in this commit.
   The new rule names the eight categories Manager enumerated
   (MODEL_IDs, schema field names, required manifest fields, CLI
   constants, mode names, context names, framework-version behavior,
   artifact tags, provenance fields).
4. **No first data access this commit.** No model load. No live
   outputs. No `AUDIT-LOG.ndjson` writes.
5. **B1 v2 source remains unedited.** No imports added; only a
   read-only cross-reference in the unit test.
6. **B1 v2.1 not created or used.**

— CS Engineer, 2026-06-10
