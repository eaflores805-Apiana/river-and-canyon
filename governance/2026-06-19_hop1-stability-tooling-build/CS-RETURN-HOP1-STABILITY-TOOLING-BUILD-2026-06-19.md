# CS RETURN — Hop1 Stability Tooling Built (PASS)

**Date:** 2026-06-19
**From:** CS Engineer
**To:** Team Lead, Manager; Cc: Senior Engineer, C5
**Re:** Manager + TL ACTION 2026-06-19 — "Begin Hop1 Stability Tooling Build"
**Status:** **PASS — Hop1 Stability tooling built for SE verification.**

---

## Record status

```text
authority           Manager + TL ACTION 2026-06-19 ("Begin Hop1 Stability
                    Tooling Build")
build verdict       PASS — both tools built, deterministic, model-free
N1 resolution       N1.A enforced — analyzer reads ONLY hop1 + hop2;
                    composite + direct_query are out of scope; mechanical
                    refusal documented in the analyzer's _load_hop1_hop2_only()
N2 resolution       branch priority implemented + documented in the
                    analyzer's output: 1) CONSTRUCT-FAIL >
                    2) HOP2-CONTROL-FAIL > 3) HOP1-STABLE-ADMISSIBLE /
                    HOP1-STABLE-INADMISSIBLE / HOP1-UNSTABLE
branch coverage     all 5 §9 branches exercised in synthetic smoke tests;
                    each fires correctly under the N2 priority
ready for SE        YES
```

---

## 1. Paths

```text
NEW TOOLING ARTIFACTS (digests to be SE-verified + locked at TL approval):
  path-a/build/v3_hop1_stability_analyzer.py
  path-a/build/v3_hop1_covariate_logger.py

BUILD-VERIFICATION ARTIFACTS (build only; not run-authorized):
  path-a/build/build_verification/hop1_stability/
    items_193_768/                 576 V3 spec JSONs (6 blocks × 96 items;
                                    materialized via the locked wrapper at
                                    cc07e5a2... — underlying generator UNCHANGED)
    test_a_stable_admissible/      synthetic scored set + summaries + decision
    test_b_stable_inadmissible/    synthetic scored set + summaries + decision
    test_c_unstable/               synthetic scored set + summaries + decision
                                    + covariate_log.json (covariate logger run on this set)
    test_d_hop2_control_fail/      synthetic scored set + summaries + decision
    test_e_construct_fail/         synthetic scored set + summaries + decision
                                    (per-block admissibility override on block 2)
```

## 2. Commit + final remote HEAD + clean-fetch confirmation

```text
build commit                <recorded in §10 after push>
final remote HEAD           <recorded in §10>
clean-fetch confirmation    <recorded in §10>
```

## 3. sha256 digests for each new tool

```text
v3_hop1_stability_analyzer.py    31224f6fe7b66d303924a40fa9307f3aded05f8ba73d4952f518c8deecd69f0f
v3_hop1_covariate_logger.py      b9532490f49970396cd9a14d926393450ede2e6a17c5374b2ac69d115f39953f

These are the two digests to be SE-verified and locked into the prereg v0.1 §12
binding block at TL approval.
```

For reference, all six v0.1 §12 reused-tool digests are UNCHANGED post-build:

```text
v3_composite_gate_item_generator.py (wrapper)    cc07e5a2...    UNCHANGED
v3_item_generator.py (underlying)                 6a2ceee1...    UNCHANGED
v3_prompt_realizer.py                              fb561fdc...    UNCHANGED
v3_prompt_conformance_checker.py                   b8afa3f8...    UNCHANGED
inspector.py                                      cb4b0b60...    UNCHANGED
constants.py                                      1d761c3d...    UNCHANGED
```

## 4. Deterministic behavior summary

```text
ANALYZER (v3_hop1_stability_analyzer.py):
  pure function of (scored, items, admissibility, prompt_conformance,
  start_index, block_size, n_blocks). No clock, no RNG, no environment,
  no network. Verified: re-run on test_c_unstable inputs → byte-identical
  decision JSON (sha 4c7a8196... matches across two independent runs).

COVARIATE LOGGER (v3_hop1_covariate_logger.py):
  pure function of (scored, items, optional realization_summary,
  start_index, block_size, n_blocks). No clock, no RNG, no environment,
  no network. Verified: re-run on test_c_unstable → byte-identical
  output JSON.

IMPORTS PER TOOL:
  analyzer: argparse, json, math, sys, pathlib   (stdlib only)
  logger:   argparse, json, re, sys, collections, pathlib   (stdlib only)
```

## 5. Branch-coverage test results

5 synthetic test scenarios over 576 items (6 blocks × 96), one per §9 branch:

```text
test                              hop1 per block       hop2 per block       expected branch              observed
test_a_stable_admissible         [96,96,96,96,96,96]  [96,96,96,96,96,96]   HOP1-STABLE-ADMISSIBLE       MATCH (exit 0)
test_b_stable_inadmissible       [0,0,0,0,0,0]        [96,96,96,96,96,96]   HOP1-STABLE-INADMISSIBLE     MATCH (exit 1)
test_c_unstable                  [96,96,96,0,0,0]     [96,96,96,96,96,96]   HOP1-UNSTABLE                MATCH (exit 2)
test_d_hop2_control_fail         [96,96,96,96,96,96]  [96,96,30,96,96,96]   HOP2-CONTROL-FAIL            MATCH (exit 3)
test_e_construct_fail            [96,96,96,96,96,96]  [96,96,96,96,96,96]   CONSTRUCT-FAIL               MATCH (exit 4)
                                                                              (adm.all_pass=false on block 2;
                                                                               invalidated_count=12 ≥ 10)
```

Exit codes match the documented mapping in the analyzer's `main()`. All 5 §9
branches fire correctly under the **N2 priority**:

```text
The TWO higher-priority branches correctly OVERRIDE the hop1 stability verdict:
  test_d: hop1 is all-clear (would otherwise be STABLE-ADMISSIBLE), but hop2
          control fails on block 3 → HOP2-CONTROL-FAIL fires (correct override).
  test_e: hop1 + hop2 are all-clear (would otherwise be STABLE-ADMISSIBLE),
          but admissibility fails on block 2 → CONSTRUCT-FAIL fires (correct
          override).
```

Per-test artifacts (scored sets + summaries + decisions; plus covariate_log.json
on test_c) committed under `path-a/build/build_verification/hop1_stability/`
for SE byte-level audit.

## 6. Confirmation N1 is resolved (N1.A enforced)

```text
N1.A REQUIREMENT (from TL ACTION verbatim):
  "render four contexts, execute only hop1 and hop2.
   Unexecuted composite/direct_query contexts must not enter scoring,
   covariate logging, branch computation, or claims."

IMPLEMENTATION:
  v3_hop1_stability_analyzer.py:
    ALLOWED_CONTEXTS = {"hop1", "hop2"}   (module constant)
    OUT_OF_SCOPE_CONTEXTS = {"composite", "direct_query"}
    _load_hop1_hop2_only() reads ONLY scored/<item>/{hop1,hop2}.json;
    composite/dq files are ignored even if present.
    Analyzer output's "n1A_enforcement" field documents this in every
    decision JSON.

  v3_hop1_covariate_logger.py:
    build_log() reads ONLY scored/<item>/hop1.json (the PRIMARY context
    for covariate analysis); composite/dq are NEVER read.

ENFORCEMENT: structural (the tools cannot opt into reading composite/dq;
no flag or arg enables it). Documented in tool docstrings + output JSONs.

CS recommends downstream inference (if/when the run is authorized) also
honors N1.A by either skipping composite/dq prompt execution OR rendering
them and labeling outputs as out-of-scope at the inference step. The
analyzer enforces N1.A structurally regardless of upstream decisions.
```

## 7. Confirmation N2 priority is implemented

```text
N2 PRIORITY (from TL ACTION verbatim):
  1. CONSTRUCT-FAIL
  2. HOP2-CONTROL-FAIL
  3. HOP1 stability branches:
     - HOP1-STABLE-ADMISSIBLE
     - HOP1-STABLE-INADMISSIBLE
     - HOP1-UNSTABLE

IMPLEMENTATION:
  v3_hop1_stability_analyzer.py:
    BRANCH_PRIORITY = [
        "CONSTRUCT-FAIL",
        "HOP2-CONTROL-FAIL",
        "HOP1-STABLE-ADMISSIBLE",
        "HOP1-STABLE-INADMISSIBLE",
        "HOP1-UNSTABLE",
    ]   (module constant; documented in every decision JSON's
         "branch_priority_order" field)

    Branch selector logic (verbatim):
      if construct_fail_blocks:
          branch = "CONSTRUCT-FAIL"
      elif hop2_control_fail_blocks:
          branch = "HOP2-CONTROL-FAIL"
      elif hop1_clear_set and not hop1_fail_set:
          branch = "HOP1-STABLE-ADMISSIBLE"
      elif hop1_fail_set and not hop1_clear_set:
          branch = "HOP1-STABLE-INADMISSIBLE"
      else:
          branch = "HOP1-UNSTABLE"

EMPIRICAL VERIFICATION:
  test_d (hop1 all clear + hop2 fail on one block) → HOP2-CONTROL-FAIL
  test_e (hop1 + hop2 all clear + adm fail on one block) → CONSTRUCT-FAIL
  Both correctly override the otherwise-STABLE-ADMISSIBLE hop1 verdict.
```

## 8. Confirmation no model imports / no model execution

```text
NO MODEL IMPORTS
  grep -lE "transformers|torch|mlx|openai|anthropic|httpx|requests.|urllib|socket"
       path-a/build/v3_hop1_stability_analyzer.py
       path-a/build/v3_hop1_covariate_logger.py
  → zero matches.
  Imports per tool (stdlib only):
    analyzer:        argparse, json, math, sys, pathlib
    covariate logger: argparse, json, re, sys, collections, pathlib

NO MODEL EXECUTION
  Neither tool calls any model API or runs inference. The analyzer scores
  outputs that have already been produced by a model — per prereg v0.1 §12:
  "Scores outputs; runs no model." The covariate logger reads scored
  outputs + item specs — never invokes a model.
```

## 9. Confirmation no run / no materialization-for-execution / no prompt execution

```text
NO RUN
  No model loaded; no inference performed; no prompts submitted to any
  LM by this build. The smoke-test scored outputs under
  path-a/build/build_verification/hop1_stability/test_{a..e}/scored/
  are SYNTHETIC (constructed by a build-verification script that assigns
  match=True/False per offset within each block, with predicted strings
  chosen from the item's existing role-token namespace) — NOT model outputs.

NO MATERIALIZATION-FOR-EXECUTION
  576 items at indices 193..768 were materialized via the wrapper to
  exercise the per-block grouping logic of both tools. These items live
  under path-a/build/build_verification/hop1_stability/items_193_768/
  and are EXPLICITLY build-verification artifacts (not run-prep). The
  actual fresh-run materialization (if/when authorized) would go under
  a future experiments/<YYYY-MM-DD>_hop1-stability-run/ dir.

NO PROMPT EXECUTION
  No prompt files were rendered for this build. (Prompt rendering is
  not needed for analyzer/logger smoke tests — the analyzer reads scored
  outputs, not prompts; the covariate logger reads scored outputs +
  item specs.) If/when the run is authorized, prompt rendering would
  proceed via the existing realizer per N1.A — but that is downstream
  of Manager by-name run authorization, not this tooling-build action.
```

## 10. Clean-fetch confirmation

To be appended after the build commit lands.

---

## Non-authorizations (carried forward, per TL ACTION boundary)

```text
- run                                       blocked
- fresh materialization for execution       blocked (the build_verification
                                                     items are NOT for execution)
- prompt execution                          blocked
- model execution                           blocked
- composite-gate retry                      blocked
- compression / INT8 / INT4                 blocked
- Claim C, Paper B                          blocked
- certification claim                       blocked
- capability claim, mechanism claim         blocked
- candidate selection, threshold values, multi-model, Fork A reactivation,
  public benchmark packaging, artifact mutation, Paper 6, Paper 3 execution
  as experiment                             all carried per standing card

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc…) + tagged manuscript
  blob (7d6706a3…)                          never moved
- tier0-run/ directory                      sealed; no new files

The Path A FP16 K=5 FAIL remains closed. V3 ≠ C0.
```

---

— CS Engineer, 2026-06-19
