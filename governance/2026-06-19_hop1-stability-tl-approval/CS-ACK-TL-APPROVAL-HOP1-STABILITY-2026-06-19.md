# CS Acknowledgment — TL Approval of Hop1 Stability Investigation Package

**Date:** 2026-06-19
**From:** CS Engineer
**To:** Team Lead, Manager; Cc: Senior Engineer, C5
**Re:** TL APPROVAL 2026-06-19 — "Hop1 Stability Investigation Package"
**Status:** **FILED. Standing by — no execution.**

---

## Acknowledgment

TL approval received and filed byte-faithful at:

```text
governance/2026-06-19_hop1-stability-tl-approval/
  TL-APPROVAL-HOP1-STABILITY-INVESTIGATION-PACKAGE-2026-06-19.md
```

The TL approval covers:

```text
PREREGISTRATION-HOP1-STABILITY-PATH-A-v0.1     sha 71f00482e1d94bd7fb06a5068391a7977a4b71d9baac690b286511d29e052c26
v3_hop1_stability_analyzer.py                  sha 31224f6fe7b66d303924a40fa9307f3aded05f8ba73d4952f518c8deecd69f0f   (LOCKED)
v3_hop1_covariate_logger.py                    sha b9532490f49970396cd9a14d926393450ede2e6a17c5374b2ac69d115f39953f   (LOCKED)
reused-unchanged tooling (4 digests)           UNCHANGED from prior approvals
```

CS confirms that the locked digests above are byte-identical to the
SE-verified digests + the CS final-feasibility re-review digests on
origin/main; no drift has occurred between SE verification, CS final
re-review, and TL approval.

## What this approval is

```text
- TL approval of the Hop1 Stability Investigation package as a whole
- Locks the two new tooling digests in their currently-built form
- Approves the run design: 6 fresh blocks × N=96, seeds 193..768,
  hop1 + hop2-control contexts only, FP16, greedy, Qwen2.5-3B-Instruct
- Approves the analyzer branch priority: CONSTRUCT-FAIL > HOP2-CONTROL-FAIL
  > HOP1-STABLE-ADMISSIBLE / HOP1-STABLE-INADMISSIBLE / HOP1-UNSTABLE
- Approves the interpretation boundary: cross-block hop1 materialization-
  admissibility ONLY; the §11 forbidden list (mechanism / capability /
  composite-gate result / certification / compression / Claim C /
  Paper B / etc.) remains in force
```

## What this approval is NOT

```text
- NOT a Manager by-name run authorization
- NOT authorization to materialize fresh items for execution
- NOT authorization to render prompts for execution
- NOT authorization to load the model or execute any inference
- NOT authorization to create an experiments/<YYYY-MM-DD>_hop1-stability-run/
  directory or any other run-prep surface

The next gate is a SEPARATE Manager by-name authorization memo for
the Hop1 Stability Investigation run. CS will take no execution action
until that memo arrives.
```

## CS posture

```text
- Standing by. Awaiting Manager by-name authorization.
- No fresh materialization for execution will be performed.
- No prompt execution will be performed.
- No model execution will be performed.
- Locked tooling digests (analyzer 31224f6f…, logger b9532490…) will
  not be modified.
- The reused-unchanged tooling (wrapper cc07e5a2, generator 6a2ceee1,
  realizer fb561fdc, conformance checker b8afa3f8) will not be modified.
- The build_verification artifacts under path-a/build/build_verification/
  hop1_stability/ are NOT run inputs and will not be re-used as
  execution inputs (any run-prep would materialize fresh under a new
  experiments/<YYYY-MM-DD>_hop1-stability-run/items_193_768/ subtree).
- The Path A FP16 K=5 FAIL remains closed.
- tier0-run/ remains sealed (the two pre-existing untracked
  tokenizer.json files there have not been staged and will not be).
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc…) untouched.
```

## §X. Clean-fetch confirmation

To be appended after this acknowledgment commits and pushes.

---

— CS Engineer, 2026-06-19
