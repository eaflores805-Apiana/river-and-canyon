# CS RETURN — V3 Real-Run Parameter-Deviation Fixture (HOLD-Close, CS Half)

**Date:** 2026-06-16
**From:** CS Engineer
**To:** Team Lead; Cc: Senior Engineer, Manager
**Re:** TL ACTION 2026-06-16 — "Close V3 Instrument Byte-Audit HOLD Before Philosophy Decision Record" (CS deliverable)
**Status:** PASS — V3 real-run path remains fail-closed under patched inspector/constants

---

## Record status

```text
TL ACTION                  CS deliverable — "V3 real-run parameter-deviation
                            fixture under patched inspector"
purpose (from TL memo)      "Confirm V3 real-run mode still fail-closed REJECTs
                            a param deviation under the patched inspector"
verdict                    PASS
inspector under test       cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
constants under test       1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
                            (both = current HEAD, K-sweep-patched, matching the
                            two digests the SE binding patch re-pins to)
parallel SE action         PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4 binding
                            patch (filed in-review at commit 3f5f808; SE locks
                            nothing — routes to TL/Manager for re-lock)
this CS commit             dc3c3f75f0953e76c0bf0e147454104b08c819de
post-push remote HEAD      dc3c3f75f0953e76c0bf0e147454104b08c819de  (matches local)
```

---

## 1. What was built

A single synthetic admissibility fixture exercising V3's **REAL-RUN** path under the **patched** inspector/constants. The fixture is internally consistent (declared D matches actual depth-2 competitor count and matching `relation_balance`), so C1–C8 all pass; the failure isolates to **C9_manager_lock_binding** under a single, well-defined Manager-lock deviation.

```text
fixture id          path_a_fixture_10_v3_real_run_param_deviation_v0.1
mode                real-run (no `_fixture_mode`, no `_sweep_mode`)
deviation chosen    params.D = 4   (Manager-locked D_DEPTH_COMPETITORS = 5)
why D-deviation     D = 5 is V3's core foreclose-all binding (same-depth
                    competitors at the head). Different Manager-lock dimension
                    than fixture 07 (margin = 0.10), so the two fixtures
                    cover separate lock-axes. Spec drift kept internally
                    consistent (4 competitors + 4-entry relation_balance) so
                    that C5 / C6 do not co-fire and the test isolates to C9.
```

## 2. Result (inspector run)

```text
disposition                 REJECT
checks                      8 / 9 pass; 1 fail
sole failure                C9_manager_lock_binding
reason                      "real-run Manager-lock binding failed -- deviations
                             from Manager lock: ['params.D = 4 !=
                             Manager-locked D_DEPTH_COMPETITORS = 5']"
validation.mode             real-run
validation.ok               false
validation.missing          []
outcome                     LOCK_VIOLATION
_expected_disposition       REJECT
_expected_match             true
inspector_version           0.1
timestamp_utc               2026-06-17T06:00:42Z
```

The single failure is exactly the C9 fail-closed branch the patched constants.py declares: in real-run mode (spec lacks both `_fixture_mode` and `_sweep_mode`), `validate_manager_lock` returns `ok=false` on any deviation; `check_C9_manager_lock_binding` propagates that as REJECT with `mode="real-run"`. The sweep-mode branch is not reached. The fixture-mode branch is not reached.

## 3. Artifact paths (repo-relative, current HEAD)

```text
fixture spec    tier-1-instrument/modules/g6-standing-rejection-audit/evaluator/tests/fixtures/path_a/10_v3_real_run_param_deviation/construction_spec.json
fixture expected
                tier-1-instrument/modules/g6-standing-rejection-audit/evaluator/tests/fixtures/path_a/10_v3_real_run_param_deviation/expected.json
result          path-a/inspector/results/10_v3_real_run_param_deviation_inspection.json
```

## 4. sha256 of every artifact under test

```text
construction_spec.json   42cd53c4cb19124a810792d66c6e8391d688893b20f082acc6fb705f9f294aad
expected.json            cd068ef32e86a46fa8b2ffe35bf793dda5565722fecbf4f1943af0f6bc9289c5
inspection result JSON   5f09fe253b7c6195568f93b9c3b79e26b2b4f0e860834c83a750621dfedf4190
inspector.py             cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
constants.py             1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
```

The inspector + constants digests match the two digests the SE binding patch re-pins to (`PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4-binding-patch.md`, sha `bfb4404a…`).

## 5. Commit, push, clean-fetch verification

```text
fixture commit (local)     dc3c3f75f0953e76c0bf0e147454104b08c819de
fixture commit (origin)    dc3c3f75f0953e76c0bf0e147454104b08c819de
                            (verified via `git ls-remote origin main`
                             immediately post-push; SHAs match)
parent (pre-fixture)       3f5f8084e0836ae92459073f232e26eb42b10b37
                            (the sweep that filed the SE binding patch +
                             cliff v0.2 + V3 byte-audit return)
remote URL                 https://github.com/eaflores805-Apiana/river-and-canyon
```

Clean-fetch reproducibility verification is appended at the foot of this memo, performed against `git fetch origin` immediately before claiming FILED.

## 6. Coverage matrix — real-run vs sweep, before vs after the K-sweep patch

```text
                                  inspector           result               status
fixture 07  margin = 0.10        be50c08c… (pre)     REJECT (C9)          historical
                                                                          (pre-patch
                                                                          real-run REJECT)
fixture 08  K=3 in sweep list    cb4b0b60… (post)    PASS                 sweep-mode
fixture 09  K=8 not in list      cb4b0b60… (post)    REJECT (C9 sweep)    sweep-mode
fixture 10  D = 4 (THIS)         cb4b0b60… (post)    REJECT (C9 real-run) post-patch
                                                                          real-run REJECT
```

The matrix is intentionally narrow. Fixture 10 is the **one** missing real-run rejection case under the patched inspector that the SE byte-audit flagged as Gap G2. No other lock-axis is exercised here; the property under test is that the patch did **not** loosen the real-run fail-closed binding, demonstrated on a Manager-lock dimension distinct from the historical fixture 07 case.

## 7. What this fixture does NOT establish

```text
- Does NOT re-lock the prereg (CS does not lock; TL/Manager re-lock).
- Does NOT validate V3's substantive properties (R1-R7) beyond the C9
  binding — that was Senior's byte-audit (`c3f4e667…`), not this fixture.
- Does NOT cover every possible parameter deviation. The C9 branch is
  exercised on D; the analogous proof for p / m / margin / k under the
  patched inspector is left to the existing fixture 07 (margin) plus
  the structural design of `validate_manager_lock` (one fail-closed code
  path; deviation on any of {p, D, m, margin, k} routes through the same
  REJECT branch).
- Does NOT authorize a model run, item generation, prompt generation,
  build, compression, or any downstream action.
- Does NOT advance Claim C, Paper B, or any capability / mechanism claim.
- Does NOT touch the closed K=5 FAIL.
```

## 8. Routing

```text
1. SE binding-patch (filed in-review at commit 3f5f808, sha bfb4404a…)
2. CS fixture PASS return (THIS memo, commit dc3c3f7 + memo commit)
3. TL / Manager re-lock the corrected V3 prereg binding of-record
4. ONLY THEN may Senior draft the philosophy decision record
```

Both parallel HOLD-closure actions (SE binding patch + CS fixture PASS) are now on disk and on origin/main. CS holds for TL/Manager re-lock decision; no further CS action required on this lifecycle absent fresh ACTION.

---

## Non-authorizations (carried forward)

```text
- candidate selection: blocked (no Paper 3 candidate-selection memo).
- threshold values: blocked (pre-registered, not freely tunable).
- certification evaluation: blocked (no candidate, no locked sheet).
- new model runs: blocked (single-model scope; any new run = fresh authorization).
- re-runs beyond authorized reproduction validation: blocked.
- INT8 / INT4 execution: blocked (no stress-eligible baseline).
- multi-model execution: blocked.
- Fork A reactivation: blocked permanently.
- Claim C activation: blocked.
- Paper 3 execution as an experiment: blocked.
- Paper 6 activation: blocked.
- public benchmark packaging: blocked.
- artifact mutation: locked artifacts must not be edited in place; corrections
  file as superseding commits.

Two specific protected surfaces remain:
- Paper 2 v1.0 tag (`paper2-cells01-03-v1.0`, SHA 41c033fc…) and tagged
  manuscript blob (7d6706a3…): never moved.
- `tier0-run/` directory: sealed; no new files.

V3 prereg of-record remains at v0.3 (not at v0.4) until TL/Manager re-lock.
The Path A FP16 K=5 FAIL remains closed and untouched by this filing.
```

---

— CS Engineer, 2026-06-16
