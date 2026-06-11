# Standing Review Discipline — Failure-Mode Review Prompt

*Team Lead 2026-06-10. Process update for future reviews. Standing rule — applies to every review of a lane, protocol change, governance rule, or experimental proposal going forward. Not an authorization; only a methodology.*

---

## The rule, in one line

> *"Do not ask reviewers only whether they agree. Ask reviewers how the proposal fails if everyone is trying to do the right thing."*

This applies to every CS review, every Senior review, every Contributor review of a new lane, protocol change, governance rule, or experimental proposal.

## What it replaces

Earlier review prompts often took the form *"Is this useful and safe?"* — which invites endorsement or rejection but does not force the reviewer to look for the specific leak. The Lane 1a discussion exposed how that framing under-recruits the catch we want: reconnaissance data quietly becoming candidate-selection pressure; clarifications becoming new authorizations; implementation details changing scientific claims.

The Lane 1a case in concrete form:
- Original question (too broad): *"Is this lane useful and safe?"*
- Better question (the one Contributor 4 effectively answered): *"Assume Lane 1a is well-intentioned and still contaminates candidate selection or threshold design. How does that happen?"*

That sharper framing should be the default going forward.

---

## The 9-item failure-mode review prompt

For every new lane, protocol change, governance rule, or experimental proposal, the reviewer should be asked to answer:

```
1. What can this proposal be misused as?
2. What later decision could this contaminate?
3. What positive inference might people draw even if the proposal forbids it?
4. What artifact, schema field, figure, table, or label could become de facto evidence?
5. What must be made impossible by construction, not merely forbidden by wording?
6. Which protection is structural, and which protection is only an honor-system rule?
7. What non-claim is missing?
8. What future gate could this silently weaken?
9. Should the proposal be: accepted, accepted only with constraints, parked, or rejected?
```

This is the default review prompt for risk-bearing design changes.

---

## Lane-specific failure-mode questions

The review prompt should be tailored to the lane's likely failure mode:

| Lane / proposal | Failure-mode question to ask |
|---|---|
| Lane 1a | How could reconnaissance become pre-selection, threshold tuning, or certification rehearsal? |
| Paper 3 v1.1 | How could a clarification become a new authorization? |
| B1 v2.1 | How could an implementation detail change the scientific claim? |
| Candidate Selection Memo | How could prior knowledge bias candidate choice before thresholds are locked? |
| Threshold-sheet lock | How could historical information or sweep outputs leak into threshold values? |
| Certification evaluation | How could a diagnostic profile be mistaken for a certification verdict? |
| Stress-retention run | How could retention be confused with correctness again? |

Reviewers should ask the lane-specific question first, then run the 9-item general prompt.

---

## Protection-layer taxonomy

Reviewers should explicitly classify each proposed protection by where its enforcement lives. The taxonomy, in increasing strength:

```
protected by wording          (weakest — depends on memory and discipline)
protected by role separation  (procedural; depends on enforcement)
protected by schema           (output type or field cannot represent the violation)
protected by code             (analysis script structurally cannot emit the violation)
protected by provenance       (artifact hashes / firewall make tampering detectable)
protected by Manager gate     (cannot proceed without explicit authorization)
```

If a protection is *only* by wording, reviewers should say so. The fix is usually to convert wording-only protections to a stronger layer: encode the forbidden state as unrepresentable in the schema, make the analysis script structurally refuse to emit it, or hash-lock the relevant artifact.

Examples of strong structural protections already in the program:

- **Schema:** Lane 1a verdict enum may contain only `clearly_fails_D*` and `requires_further_investigation` — no `passes_*` value exists; positive-selection cannot be emitted.
- **Code:** Plot style file locked; "promising region" rendering cannot be produced.
- **Provenance:** Threshold-sheet content hash verified before content trust (Senior C3); analysis script hash locked at sweep authorization.
- **Manager gate:** Framework-version supersession check (H3) refuses superseded identifiers at runtime.

---

## The Lane 1a lesson, distilled

```
Lane 1a may rule out.
Lane 1a may not rule in.
```

That distinction emerged because reviewers were eventually asked what the lane could *become* in practice, not merely what it was *intended* to be.

The same pattern applies everywhere: **a proposal's stated intent is not enough; we need to ask what its artifacts will do after they exist.**

---

## How CS applies this rule going forward

Every CS review of a substantive proposal carries:

1. The lane-specific failure-mode question at the top.
2. The 9-item prompt answered explicitly.
3. The protection-layer taxonomy applied to each protective rule in the proposal — noting which are wording-only and recommending structural alternatives.
4. A standard verdict (accept / accept-with-constraints / park / reject) per §1 item 9.

This applies to: paper revision reviews, lane authorization reviews, B1 plan reviews, governance-rule reviews. Editorial-only revisions stay light per the existing paper-revision cadence rule.

---

## Process status

Team Lead will include the failure-mode prompt section in future review packets for: Paper 3 v1.1, Lane 1a, Candidate Selection Memo, B1 v2.1, threshold-sheet design, certification evaluation, and stress-retention execution. CS adopts the rule unilaterally for its own review filings starting now.

---

## Additional rule — production cycle vs. G1-open condition memos (added 2026-06-10)

*Manager / Elias 2026-06-10 (routing Senior finding on Lane 1a Step-3 wrapper). Permanent production rule for any work package that has multiple condition memos in flight.*

> **No production cycle may begin while any condition memo affecting that production cycle is G1-open.**

A production cycle includes (but is not limited to) writing locked artifacts, hash-recording in a lock record, or any work whose semantic depends on the resolution of a still-in-flight instruction.

This applies to:

- Senior correction memos
- Team Lead conditions
- Manager constraints
- CS implementation notes that alter artifact semantics

A production cycle may proceed only after the relevant condition memos are either:

- **committed at intended path** (CS verifies on disk before starting),
- **hash-confirmed** (the SEND-marked content's sha256 matches the on-disk copy),
- **explicitly superseded** by a later authoritative memo, or
- **explicitly ruled out of scope** by Team Lead or Manager.

If a condition memo is SEND-marked but not commit-confirmed, the production cycle does not start. CS reports the G1-open state and waits.

**Why this rule exists.** It was added after Senior surfaced a Lane 1a Step-3 wrapper defect (`SENIOR-FINDING-WRAPPER-REWRITE-2026-06-10.md`): Senior's correction memo specifying the sidecar-attestation pattern was SEND-marked but G1-open at production time, so CS built from the prior confirmed spec, which still permitted "honest override" — the rejected pattern. Zero damage occurred because the LOCK-RECORD was still PENDING and no first data access happened; the rule prevents recurrence.

**Implication for CS.** CS reads memo channels with the same discipline as artifact channels: SEND-TO-CS is intent; delivery is confirmed commit SHA at intended path. This rule extends that discipline to *correction* memos, not only to artifact deliveries.

---

## Additional rule — sibling-artifact cross-reference tests (added 2026-06-10, Manager / Path A.1 acceptance)

*Manager / Elias 2026-06-10 (Path A.1 direction, accepting CS standing-rule proposal). Permanent production rule for any artifact that integrates with a locked sibling artifact.*

> **CS production of any artifact that integrates with a locked sibling artifact must include a unit test that cross-references concrete values against the sibling artifact's source.**

Applies to:

- `MODEL_ID`s
- schema field names
- required manifest fields
- CLI constants (argparse choices, default values)
- mode names
- context names
- framework-version behavior
- artifact tags (`artifact_class`, `certification_relevance`, etc.)
- provenance fields

The test must read the sibling artifact's source file directly (not import it; not depend on the sibling being importable) and assert byte-for-byte equality with the corresponding value in the new artifact.

**Why this rule exists.** Lane 1a Step-3 production exposed two CS-side specification defects that survived three review gates (Senior intent-preservation PASS, Team Lead combined-review PASS, CS Path A return) because Path A unit tests covered Python-logic invariants on synthetic inputs but did not cross-reference concrete values against B1 v2's source:

- The B1 v2 manifest-interface deviation (Lane 1a nested dict vs. Two-Hop L1 flat list) would have been caught by a schema-shape cross-reference test on `validate_manifest`.
- The `MODEL_ID` deviation (`mlx-community/Qwen2.5-3B-Instruct-bf16` vs. `Qwen/Qwen2.5-3B-Instruct`) is caught by `test_model_id_matches_b1v2`, which reads B1 v2 source directly.

**Canonical examples for this rule:**

- `experiments/2026-06-10_lane-1a-sweep/test_lane1a_packet.py::TestLane1aRunnerProvenance::test_model_id_matches_b1v2` — reads `experiments/2026-06-09_b1-harness-v2/code/runner_b1_v2.py`, extracts `MODEL_ID` via regex, asserts equality with `lane1a_runner.MODEL_ID`. Any future drift on either side trips CI.

**Implication for CS.** The new rule complements the prior G1-open production rule (no production while condition memos are G1-open). Together they require:

- Conditions arriving via memo channel: committed at intended path; hash-confirmed; explicitly superseded; or explicitly ruled out of scope.
- Conditions arriving via existing locked artifact: unit-tested against the locked artifact's source.

Both rules apply to every production cycle going forward.

---

## Additional rule — production-path subprocess smoke test (added 2026-06-10, Manager / Path E.1 acceptance)

*Manager / Elias 2026-06-10 (Path E.1 direction, accepting CS standing-rule proposal). Permanent production rule for any artifact that invokes a subprocess.*

> **Any artifact that invokes a subprocess in production must include a production-path smoke test that spawns that subprocess exactly as production will, verifies import success, verifies required dependency versions, and records the interpreter path.**

Same-process import checks are not sufficient. They test the test runner's environment, not the production subprocess environment.

The test must:

- Spawn the subprocess using the EXACT interpreter resolution the production wrapper uses (not `sys.executable` if production uses a pinned path).
- Verify the runner module's import surface succeeds in that subprocess (the production wrapper must not be able to invoke the runner only to have it crash at import time).
- Verify required dependency versions match the locked expected values (e.g., `mlx_lm.__version__`).
- Record the interpreter path so any future drift is traceable.

**Why this rule exists.** The third Lane 1a deviation surfaced because `sys.executable` in the production environment resolved to a Python interpreter (anaconda Python 3.10) whose `mlx_lm` was version 0.19.3 — an older release without the `make_sampler` symbol the runner imports. The runtime mlx_lm version was not cross-referenced against B1 v2's documented runtime environment. The wrapper's subprocess invocation produced 31 `ImportError` events before any model load, consuming 31 (rung, stratum) attempts under the no-re-execution rule. The new rule converts the implicit assumption "the host has the right Python" into a tested, locked production invariant.

**Canonical example.**

`experiments/2026-06-10_lane-1a-sweep/test_lane1a_packet.py::TestPathE1ProductionSubprocess`:

- `test_interpreter_path_matches_config` — cross-references `wrapper.PRODUCTION_PYTHON` against `runner_config.yaml production.python_interpreter`.
- `test_expected_mlx_lm_version_matches_config` — cross-references the expected mlx_lm version.
- `test_production_subprocess_smoke` — spawns the production subprocess; runs `import mlx_lm; from mlx_lm.sample_utils import make_sampler; print(mlx_lm.__version__)`; verifies the version equals expected.
- `test_wrapper_does_not_use_sys_executable_for_subprocess` — source-level grep asserts the wrapper's subprocess argv[0] is `PRODUCTION_PYTHON`, not `sys.executable`.

**Three production rules now in force.**

| Rule | Catches |
|---|---|
| No production while G1-open condition memo affects it | wrapper-rewrite pattern defect |
| Sibling-artifact cross-reference unit test | source-side drift (MODEL_IDs, schema shapes, CLI flags) |
| Production-path subprocess smoke test | environment-side drift (interpreter paths, dependency versions, import surface availability) |

Together they cover memo-channel, source-code-channel, and runtime-environment-channel discipline.

---

## Non-authorizations (carried forward)

This standing rule does not authorize any execution lane. See `governance/standing/STANDING-NON-AUTHORIZATIONS.md` for the full canonical list.

---

— Team Lead authored 2026-06-10; CS filed 2026-06-10; Manager production-rule addendum 2026-06-10; Manager sibling-artifact cross-reference rule addendum 2026-06-10; Manager production-path subprocess smoke test rule addendum 2026-06-10
