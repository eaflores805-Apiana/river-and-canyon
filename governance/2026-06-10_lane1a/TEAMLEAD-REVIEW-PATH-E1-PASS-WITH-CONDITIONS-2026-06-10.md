# Team Lead Re-Review — Lane 1a Path E.1 Runtime Remediation (PASS WITH CONDITIONS)

From: Team Lead
To: CS Engineer
Cc: Senior Engineer, Manager, New Senior Engineer
Date: 2026-06-10
Status: Re-review PASS; two clarifications required before Manager reauthorization

---

## Verbatim memo (key points)

> Senior Path E.1 review: PASS (design + execution-environment).
> Team Lead combined re-review: PASS.
>
> **Item 1.** New sweep_id `lane-1a-2026-06-11` regenerates the entire
> item population. CS must clarify whether Lane 1a uses:
>
> - **Option A** — manifests pre-generated now, with acceptance results
>   and hashes recorded before lock, OR
> - **Option B** — manifests generated at sweep start, with acceptance
>   checks as generation-time gates audit-logged before first model call.
>
> No re-seal required if recorded in CS return or lock-finalization memo.
> Manager reauthorization should not proceed until CS states which
> applies.
>
> **Item 2.** Test suite skipped 1 test for missing `jsonschema`.
> Execution-blocking if any locked runtime artifact uses jsonschema. CS
> must either:
>
> - **A.** Add jsonschema to the production subprocess smoke test, OR
> - **B.** State and prove that runtime record validation does not depend
>   on jsonschema.
>
> A schema-class protection cannot silently degrade to wording-class
> because the validation library is absent.
>
> **§4 standing rule interpretation:** the production-path smoke test
> must verify all required runtime dependencies of the locked execution
> set, not only mlx_lm.
>
> — Team Lead

---

## CS response

### Item 1 — Manifest population evidence: **OPTION A**

Manifests are **pre-generated NOW** (regenerated during the Path E.1
remediation cycle, immediately after `SWEEP_ID` was updated). The
pre-generation evidence is on disk in the experiment directory:

```text
experiments/2026-06-10_lane-1a-sweep/manifests/
  L01.json   sha256 808bf4e81865c7be586521b0b9e23b5269ef8dc0465799def2855c9189f346a9
  L02.json   sha256 00bfa0fcdb74e2858bf711e9436593e33c410fb174406c1d3fda7220922dc95b
  L03.json   sha256 dea1a74ec3929f0808e574516894c667899192212b609e6f2bd261c7d2409004
  L04.json   sha256 e340380326f6ead1d90696e3412b6248c85e6c9ba8625cf4dd9ec8f854f5b3c2
  L05.json   sha256 999404cd503bfbbfdaadaf2445db6766fadad6f89aa4fc6b7954fb242e65b45a
  L06.json   sha256 0f09a00c1f111a2f87d38322eb1b975a93e3a2388fdcd0134b18baf095cbcfe4
  L07.json   sha256 0aa90da2aa4da6be2e724e38a654923a129ad2efebb4ad554e5e67c3bb639e1b
  L08.json   sha256 7b68db9c84b538e653aa0cd06ab39e06232ce23f5d3abaf7a9d7370f26247aec

  MANIFEST-HASHES.lock                — the per-rung sha256 list (above)
  RECIPE-ACCEPTANCE-CHECK-RESULTS.json — per-rung acceptance:
                                          L01..L08 all_pass=true
```

The 8 manifest hashes are **also embedded verbatim in LOCK-RECORD.md
§"Manifest hashes"** so the audit-time signature is fixed at lock
time, not at sweep start. The seed (`111550783468268645`, from
`sha256("lane-1a-2026-06-11")[:8]`) is recorded in
`RECIPE-ACCEPTANCE-CHECK-RESULTS.json`.

**At sweep time, the wrapper does not regenerate.** Each
`invoke_runner()` call reads `manifests/<rung_id>.json` from disk; if
that file's content differs from the pre-locked hash, an auditor
would catch the divergence by re-hashing against MANIFEST-HASHES.lock.

**Generation-time gates** (per `§13 recipe v0.2 §8` and
`manifest_generator.recipe_acceptance_check_rung`) were exercised
during the pre-generation step: all 8 rungs PASSED the recipe
acceptance check (every declared dummy policy produces a non-degenerate
prediction vector with ≥3 distinct predictions). These results are
recorded in `RECIPE-ACCEPTANCE-CHECK-RESULTS.json`. The wrapper does
not re-run the gates at sweep time; the lock-time gate result is the
binding evidence.

### Item 2 — Runtime dependency on jsonschema: **OPTION B**

CS verifies that **no locked runtime artifact imports `jsonschema`.**
Direct grep across every locked runtime file:

| Artifact | Imports `jsonschema`? |
|---|---|
| `classification_criteria.yaml` | no (YAML data file) |
| `manifest_generator.py` | no |
| `prompt_template.md` | no (data) |
| `scorer.py` | no |
| `dummy_policies.py` | no |
| `runner_config.yaml` | no (YAML data file) |
| `lane1a_runner.py` | **no** — line 90 is a comment: *"Lane 1a manifest schema validator (lightweight; no jsonschema dep)."* The runner uses its own in-process validator `validate_lane1a_manifest()` |
| `lane1a_runner_wrapper.py` | no |
| `analyzer.py` | no |
| `plotter.py` | no |
| `artifact_tags.py` | no |
| `audit_log.py` | no |
| `fixed_outcome.md` | no (data) |
| `exclusion_block.md` | no (data) |
| `AUDIT-LOG-FORMAT.md` | no (documentation) |
| `NOVELTY-LEDGER.md` | no (documentation) |
| schemas | no (data files, themselves the contracts) |

Only `test_lane1a_packet.py` imports `jsonschema`, and only in tests
that explicitly `self.skipTest("jsonschema not installed")` if it's
absent. The one skipped test (`test_per_rung_schema_rejects_rank_field`)
verifies that an extra `rank` field IS rejected by
`additionalProperties: false`. That's a test-time contract verification,
not a runtime validation.

### Non-jsonschema enforcement mechanism (Team Lead Item 5)

Lane 1a runtime protection is **code-class**, not jsonschema-class:

| Surface | Runtime enforcement |
|---|---|
| Lane 1a manifest shape | `lane1a_runner.validate_lane1a_manifest()` — Python-level field/type/enum checks; raises `ManifestValidationError` on malformed input; unit-tested by 5 negative cases + all 8 generated manifests |
| `artifact_class` / `certification_relevance` tags | `artifact_tags.tag()` — rejects override of either field to non-canonical values; raises `ValueError`; unit-tested by `TestArtifactTagsRejectOverride` |
| Audit log events | `audit_log.AuditLogWriter.emit()` — `VALID_EVENTS` and `VALID_STRATA` enum-checks; raises `ValueError` on unknown event/stratum |
| LOCK-RECORD token-prior authorization | `lane1a_runner_wrapper._validate_lock_record()` — regex parse + exact-string match against authorized literal |
| Lock-timestamp ordering | `lane1a_runner_wrapper._validate_first_data_access_ordering()` — sentinel check + RFC 3339 lexicographic comparison |
| Production subprocess interpreter / mlx_lm version | `lane1a_runner_wrapper.production_subprocess_smoke_test()` — spawns subprocess; verifies import surface + version |
| Manifest hash integrity at sweep time | implicit: each invoke reads the on-disk manifest; any auditor can re-hash against `MANIFEST-HASHES.lock` to detect tampering |

**There is no surface on which the JSON Schemas are the SOLE enforcement
mechanism at runtime.** Every protection is backed by at least one
code-class check or by hash verification.

### Schema-class protection clarification

The three JSON Schemas
(`per_rung_record.schema.json`, `sweep_record.schema.json`,
`lane1a_sidecar.schema.json`) function as:

1. **Contract documentation** — readable specifications of the record
   shape; consumed by any external auditor or future certification
   pipeline.
2. **Test-time enforcement** — the test suite validates representative
   records against the schemas (via `jsonschema` when installed; skipped
   gracefully otherwise) to confirm `additionalProperties: false`
   rejects forbidden fields like `rank` / `preference` / `best` and
   that `framework_version != "none"` is rejected.
3. **Production-write commitment** — the analyzer, wrapper, and runner
   write records whose Python-level construction mirrors the schemas
   field-by-field. The code paths producing these records do not
   construct rank/preference/best fields; the schemas would catch it
   if they did.

Lane 1a does not currently re-validate records against the schemas at
runtime. If future work wants jsonschema-backed runtime validation,
that is a future lock cycle (would require: new analyzer.py /
wrapper.py / runner.py with `jsonschema.validate()` calls; jsonschema
added to the production smoke test; new LOCK-RECORD; replay review
chain). CS will surface that recommendation when warranted; for the
current sweep, the code-class enforcement above stands.

### Item 4 — Standing-rule interpretation (Team Lead §4)

CS accepts Senior's framing:

> *"The production-path smoke test must verify all required runtime
> dependencies of the locked execution set, not only mlx_lm."*

The current smoke test verifies `mlx_lm` + `make_sampler` because
those are the **only third-party runtime dependencies** of the locked
execution set. `numpy`, `subprocess`, `pathlib`, `json`, `hashlib`,
`datetime`, `re` are stdlib (no probe needed). `lane1a_runner.py`
imports `artifact_tags` and `dummy_policies` (siblings, already
hash-locked).

If a future production change adds a runtime dependency, the smoke
test gets a new probe in the same cycle. CS will reflect this in
`STANDING-REVIEW-DISCIPLINE.md` if Manager and Team Lead concur with
the following sentence:

> *"The smoke test's probe list must be kept current with the locked
> execution set's third-party runtime imports; adding or removing a
> runtime import triggers a corresponding smoke-test update in the
> same lock cycle."*

If Team Lead approves, CS files this clarification at the next
legitimate STANDING-REVIEW-DISCIPLINE.md touch.

### Item 6 — First data access confirmation

**CONFIRMED.** First data access remains NOT AUTHORIZED. CS has not
invoked `preflight()` against the new LOCK-RECORD. No model load.
No `AUDIT-LOG.ndjson` (only the archived
`AUDIT-LOG-2026-06-10-INSTRUMENT-FAILURE.ndjson` from the prior
sweep_id).

## CS posture

**HOLD for Manager first-data-access reauthorization against
LOCK-RECORD `969e1e31…`.** No re-seal performed (Team Lead §2 made
clear no re-seal is required if Item 1 / Item 2 are addressed in a
return memo). All 20 inner artifact hashes unchanged. All 40 unit
tests still PASS (re-run not re-required since no artifact modified;
result holds since commit `08fc847`).

## Summary

| Item | Resolution |
|---|---|
| 1. Manifest evidence timing | **Option A** — pre-generated NOW; hashes in LOCK-RECORD + MANIFEST-HASHES.lock; acceptance in RECIPE-ACCEPTANCE-CHECK-RESULTS.json (all 8 PASS) |
| 2. jsonschema runtime use | **Option B** — no locked runtime artifact imports jsonschema; runtime enforcement is code-class via 7 enumerated mechanisms |
| 4. Standing rule interpretation | Accepted; CS proposes one-sentence clarification at next STANDING file touch |
| 6. First data access | NOT AUTHORIZED; confirmed |

— CS Engineer, 2026-06-10
