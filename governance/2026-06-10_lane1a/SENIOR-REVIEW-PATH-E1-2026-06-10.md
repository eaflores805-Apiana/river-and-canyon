# Senior Review — Lane 1a Path E.1 Runtime Remediation (08fc847)

From: Senior Engineer (outgoing seat; routed Senior → Team Lead)
To: Team Lead; Cc: CS Engineer, Manager, New Senior · 2026-06-10
Method: verified against fetched bytes at `08fc847`; LOCK-RECORD recomputes to `969e1e31…` full-match.

## §5.1 — Design-intent preservation: **PASS** (all twelve §2 checks)

sweep_id `lane-1a-2026-06-11` carries the identical design (packet v0.3 referenced by hash
`f1280a85…` in the LOCK-RECORD; doctrine, artifact class, framework "none" all restated); the prior
attempt is archived as `instrument_failure_before_model_load` — correctly classified: zero
generations occurred, so this is an instrument fault, not a rung re-execution, and the fresh sweep_id
plus fresh Manager reauthorization is the clean path (§1.12's no-re-execution rule governs post-data
attempts and is not implicated); PRODUCTION_PYTHON is the explicit framework path; mlx_lm 0.31.3
explicit; the smoke test spawns the pinned interpreter itself and verifies import + version; MODEL_ID
remains `Qwen/Qwen2.5-3B-Instruct`; runner remains lane-specific; B1 v2 byte-identical to the
pre-Path-A reference; no v2.1 artifact; sidecar intact with no rewrite path; 1,536 planned with the
token-prior line present; first data access not executed and not authorized. The single
`sys.executable` occurrence in the wrapper is a comment explaining why it must NOT be used — the
anti-pattern is documented at the site of temptation.

## §5.2 — Execution-environment intent preservation: **PASS**, with two named items

The remediation honors the principle behind it: the environment a subprocess actually resolves is a
*claim about the world*, and Path E.1 converts it from an assumption into a tested fact recorded in
the lock chain.

**Item 1 — manifest population evidence (one sentence, at re-review).** The seed derives from
sha256(sweep_id), so the new sweep_id regenerates the *entire item population*. The LOCK-RECORD notes
the regeneration but does not state where the v0.3 generation-time gates — recipe acceptance
(dummy-policy nondegeneracy per rung), position-histogram ≤3σ, tokenization stability, novelty-ledger
overlap — are evidenced for the lane-1a-2026-06-11 population. Both timings are legitimate under
v0.3: (a) manifests pre-generated now, acceptance results + hashes recorded before lock; or (b)
manifests generated at sweep start with acceptance checks as generation-time gates whose results
enter the audit log before the first model call. CS states which, in one sentence, at re-review.

**Item 2 — dependency-verification completeness (before execution).** Tests report "1 jsonschema
skip" (`skipTest("jsonschema not installed")`). If any locked artifact imports `jsonschema` at
runtime — schema validation of sidecars/records — then the production smoke test must verify it
exactly as it verifies mlx_lm; a validator that silently can't run is a schema-class protection
demoted to wording-class at execution time. Either add jsonschema (and any other runtime import of
the locked set) to the smoke test's verified dependencies, or state that record validation is
enforced by a non-jsonschema mechanism. The rule §3 already implies this: "verifies required
dependency versions" should mean *all* of them.

## §3 standing rule: **CONFIRMED appropriate**

It is the third leg of a now-coherent family: G1 tests *delivery*, the sibling cross-reference rule
tests *agreement*, and the production-path smoke test tests *environment*. All three share one form —
a claim about the world must be verified in the world's own terms before anything locks against it.
Enforcement triple present (vehicle: smoke test in the suite; owner: CS at production; audit
artifact: interpreter path + versions recorded). With Item 2 adopted, the rule's "required dependency
versions" clause is read as exhaustive over the locked set's runtime imports.

## §5.3 — Required fixes: Items 1 and 2 above (one sentence; one smoke-test extension). Neither
blocks re-review; Item 2 blocks execution.
## §5.4 — Team Lead may proceed to combined adversarial re-review: **yes.**
## §5.5 — First data access: **remains not authorized.** Confirmed.

— Senior Engineer
