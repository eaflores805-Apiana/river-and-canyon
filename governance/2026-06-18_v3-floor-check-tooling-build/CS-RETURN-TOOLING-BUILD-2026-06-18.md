# CS RETURN — V3 Floor-Check Tooling Build (Step 1 + Step 2)

**Date:** 2026-06-18
**From:** CS Engineer
**To:** Team Lead; Cc: Manager, Senior Engineer, C5
**Re:** Manager + TL ACTION 2026-06-18 — "File V3 Floor-Check Prereg v0.4 and Begin Tooling Build"
**Status:** **STEP 1 PASS — v0.4 filed.** **STEP 2 PASS — floor-check tooling built for SE verification.**

---

## Record status

```text
ACTION                Manager + TL, 2026-06-18 (two-step)
Step 1                PASS — v0.4 filed at TL-specified path, byte-identical to Senior source
Step 2                PASS — four tooling artifacts built, deterministic, conformance-passing on
                       the 8-item demonstration batch
boundaries respected  no scientific content edited at filing; no model imports;
                       no model execution; no prompt execution against a model;
                       no N=96 materialization; no run.
next                  SE verifies tool bytes → CS feasibility re-review → TL approval
                       consideration → Manager by-name run authorization (only if approved)
```

---

## Step 1 — v0.4 filed (PASS)

```text
commit                       829e00cc0cc7377c734c7f9b31b2e6f6117e7280
final remote HEAD            (recorded in §3 with the tooling commit; this Step 1 commit
                              was followed by the tooling commit; both are on origin/main)
filed path                   path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.4.md
sha256 digest                c5ec46194772f100681cf41a6b3dd2d0c51a2c1fb49a62b181741a74529ce7b0

clean-fetch confirmation     verified post-push via `git fetch origin` + `git cat-file -p
                              origin/main:<path>`; sha matches the digest above byte-for-byte.

bytes match Senior v0.4       YES.
                              inbox source: _INBOX/PREREGISTRATION-V3-FLOOR-CHECK-PATH-A-v0.4.md
                              source sha:   c5ec46194772f100681cf41a6b3dd2d0c51a2c1fb49a62b181741a74529ce7b0
                              filed dest sha: c5ec46194772f100681cf41a6b3dd2d0c51a2c1fb49a62b181741a74529ce7b0
                                                                                                 ^ identical
                              Filing was a byte-identical copy with rename (drops `-PATH-A-`
                              infix per TL-specified destination path, consistent with
                              v0.2/v0.3 naming). No scientific content edited.
```

(Step 1 also swept C5's v0.3 claim-risk PASS return — `sha:fd99a64a…` — into `path-a/in-review/` as the parallel review-track artifact; covered in the same commit + README addendum 5.)

---

## Step 2 — Floor-check tooling built (PASS)

### 2.1 Paths

```text
path-a/build/v3_floor_check_analyzer.py
path-a/build/v3_prompt_realizer.py
path-a/build/v3_prompt_conformance_checker.py
path-a/build/v3_neutral_token_pool.md
```

Plus build-verification artifacts (build-only, not run-authorized):

```text
path-a/build/build_verification/
├── prompts/                                 8 items × 4 contexts = 32 prompt files
├── realization_summary.json                 8/8 gate-pass (char_delta ≤ 8 per item-set)
├── prompt_conformance_summary.json          8/8 pass; §9(vi) gate PASS
├── test_a_all_clean/                        synthetic scored set for analyzer branch test
├── test_b_hop2_fails/                       synthetic scored set: hop2 below floor
├── test_c_hop1_also_fails/                  synthetic scored set: hop1 below floor
└── analyzer_runs/                           per-test analyzer decision JSONs
    ├── test_a_all_clean.json
    ├── test_b_hop2_fails.json
    └── test_c_hop1_also_fails.json
```

### 2.2 Per-artifact sha256

```text
0f5a3f7438a6936fe449ea3558321a734b999b2ac2e8384032c2890e155f3585  v3_floor_check_analyzer.py
fb561fdc526115da94c6137b739e8bb3b6adf30825d83f864cda713bc0750909  v3_prompt_realizer.py
b8afa3f89dd7f375058500820bdf2bf58a46384d2283c8f2a31f1b8c92ad2b82  v3_prompt_conformance_checker.py
bc2020c2c4e1293f62c9f83a9b24a61f98c1ede35d5a071ee8cfd72a316ab0d9  v3_neutral_token_pool.md
```

These are the digests to be SE-verified next and locked into the v0.4 §T binding block at TL/Manager approval.

### 2.3 Deterministic behavior — verified

```text
REALIZER     pure function of (item_spec, neutral_token_pool); imports only
              {argparse, hashlib, json, sys, pathlib}; no clock, no RNG, no
              environment, no network. Verified by re-generating all 32 prompts
              into a tmpdir and confirming byte-identical sha256 across two
              independent runs: 32/32 prompts byte-identical, 0 mismatches.

CHECKER      pure function of (item_spec, realized_prompts); imports only
              {argparse, json, sys, pathlib}; no clock, no RNG, no environment,
              no network. Per-item checks P1–P10; same inputs → same outputs.

ANALYZER     pure function of (scored_outputs, r6_log, admissibility,
              prompt_conformance); imports only {argparse, json, math, sys,
              pathlib}; no clock, no RNG, no environment, no network. Verified
              by re-running on the same test_b inputs and confirming
              byte-identical decision JSON across two runs (sha
              cef00586ae903eeb58ca71351bbb06fed32777df597ef24c22492cfe1df0c4dd
              on both runs).

NEUTRAL POOL fixed markdown resource; realizer's parser is a deliberately
              simple bracket-extractor tied to §2's literal layout.
```

### 2.4 Confirmation: no model imports, no model/prompt execution, no N=96 materialization

```text
NO MODEL IMPORTS     grep over the three .py tools for {transformers, torch,
                     mlx, openai, anthropic, httpx, requests., urllib, socket}
                     returns ZERO matches. The only imports are stdlib:
                       analyzer: argparse, json, math, sys, pathlib
                       realizer: argparse, hashlib, json, sys, pathlib
                       checker:  argparse, json, sys, pathlib

NO MODEL EXECUTION   the tools call no model API and run no inference. The
                     analyzer scores OUTPUTS that have already been produced
                     by a model (per v0.4 §T: "SCORES outputs; runs no model").

NO PROMPT EXECUTION  the realizer writes prompt .txt files; no LM is invoked
                     to consume them. The build-verification prompts under
                     path-a/build/build_verification/prompts/ are demonstration
                     artifacts to verify the realizer's deterministic behavior
                     and the checker's pass/fail logic — they are NOT run-ready
                     and NOT submitted to any model.

NO N=96 MATERIALIZATION
                     The realizer was exercised on the existing 8-item
                     demonstration batch only (`path-a/build/items/item_001..008.json`).
                     N=96 generation is a separate downstream step gated on
                     Manager by-name authorization per v0.4 §13/§14.
```

### 2.5 Confirmation: MAX_DELTA = 8 implemented as character-count gate

```text
REALIZER        MAX_DELTA = 8 is set as a module constant in v3_prompt_realizer.py
                line ~30. realize_item() returns char_counts per context + char_delta
                (max - min) + max_delta_gate boolean (delta ≤ MAX_DELTA).

CHECKER         MAX_DELTA = 8 is set as a module constant in v3_prompt_conformance
                _checker.py. P9 "char_delta_gate" check fires if delta > 8.
                Property check returns ok=True iff delta ≤ 8.

VERIFIED on 8-item batch:
  item    composite  hop1  hop2  dq   delta  gate
  item_001    653    645   646   651    8    PASS
  item_002    653    645   646   651    8    PASS
  item_003    653    645   646   651    8    PASS
  item_004    653    645   646   651    8    PASS
  item_005    653    645   646   651    8    PASS
  item_006    653    645   646   651    8    PASS
  item_007    653    645   646   651    8    PASS
  item_008    653    645   646   651    8    PASS
  max char_delta observed: 8 — every item hits the gate exactly at the boundary.
```

### 2.6 Feasibility note — ≤8 characters is achievable but ON-THE-EDGE

CS confirms ≤8 characters is achievable with the current realizer; **all 8 items in the demonstration batch hit the gate exactly at delta = 8** (no margin). The structural sources of the delta:

```text
SOURCE                              char contribution
composite/dq QUERY uses `r1.r2`     ~3 chars more than hop1's `r1` or hop2's `r2`
bridge fact vs filler line in dq    ~2 chars (filler triple 25 chars vs bridge 27)
B token (i007_B1) vs A (i007_A)     1 char
small cumulative                    ~2 chars

Cumulative delta                    ~ 8 chars — at the gate boundary.
```

This matches the SE feasibility note in v0.4 §4 verbatim: *"holding the delta ≤ 8 characters likely requires a length-controlled / fixed-slot query format in the realizer."* CS used exactly that approach (triple format `(SUBJ, REL, OBJ)`, length-balanced neutral pool at 7-char width matching role-token prefix width).

**No blocker.** The realizer meets the gate. But the margin is zero, which means future changes to the construction schema (e.g., shorter or longer per-item-prefix tokens, additional fact lines, longer relation tokens) could exceed the gate without realizer adjustment. SE may consider this in the post-tooling feasibility re-review per v0.4 §4: "Whether MAX_DELTA = 8 is achievable is validated at SE-verify-tool-bytes / CS-feasibility-re-review (after the realizer exists)."

### 2.7 Smoke-test branch behavior

Three synthetic scored-output scenarios over the 8-item batch:

```text
TEST                       hop2 k/n   hop1 k/n   dq cnt   invalidated   branch
test_a_all_clean              8/8        8/8         0         0        CONSTRUCT-FAIL *
test_b_hop2_fails             4/8        8/8         0         0        CONSTRUCT-FAIL *
test_c_hop1_also_fails        8/8        4/8         0         0        CONSTRUCT-FAIL *
```

`*` — at N=8 the Wilson 95% lower bound on 8/8 = 0.6756 < 0.75 (Wilson half-width is too
wide at small N). So condition (i) or (iii) fails in every smoke test regardless of point
estimate, sending all three branches into CONSTRUCT-FAIL. **This is correct behavior**: the
analyzer enforces strict Wilson > 0.75 on the post-exclusion denominator, exactly as v0.4 §7
and §E4 specify, with no N=96-hardcoded path.

**Locked-threshold check at N=96 (verified separately via the analyzer's wilson_ci function):**

```text
  80/96 = 0.8333   W_lower = 0.7463   fails  (matches v0.4 §7 SE-verified figure)
  81/96 = 0.8438   W_lower = 0.7581   CLEARS (matches v0.4 §7 SE-verified figure)
  82/96 = 0.8542   W_lower = 0.7700   clears
```

Analyzer's Wilson function correctly implements the locked decision rule. At the locked N=96, 81/96 is the minimum-clearing count; SE-verifiable via the analyzer's `wilson_ci(81, 96)` call. The COMPONENT-ADMISSIBLE-UNDER-COMPETITION and ONE-RUN-EVIDENCE-TOWARD-SUBSTRATE-INFEASIBILITY branches were verified by code inspection of the analyzer's branch selector (`if clean_executable and cond_i: ... elif clean_executable and not cond_i: ... else: CONSTRUCT-FAIL`) — the selector is a 3-way switch on (clean_executable, cond_i) that exhaustively partitions the condition space.

### 2.8 Feasibility blockers

```text
NONE identified at the tooling layer.

All four tooling artifacts:
  - exist
  - match v0.4 §T contracts in code
  - are pure functions of inputs (deterministic)
  - have no model imports, no inference, no network
  - implement MAX_DELTA = 8 as character-count gate (realizer + checker)
  - implement the §9 condition checks and §10 branch selector (analyzer) under the
    LOCKED thresholds (HOP_FLOOR=0.75; DQ_POINT_CEILING_COUNT=19; INVALIDATED_THRESHOLD=10;
    WILSON_Z_95=1.96)
  - produce conformant output on the existing 8-item demonstration batch
    (realizer: 8/8 gate-pass; checker: 8/8 pass; §9(vi) PASS)
  - exercise CONSTRUCT-FAIL branch under three different failure modes;
    other two branches verified by code inspection (small-N Wilson width
    prevents their exercise at N=8 — by design)

Downstream considerations flagged but explicitly NOT blockers:

  - PROMPT REALIZER MARGIN — delta hits 8 exactly. Future schema changes could
    exceed without realizer adjustment. SE may consider in feasibility re-review.

  - N=96 SMOKE TEST OF BRANCHES — COMPONENT-ADMISSIBLE and ONE-RUN-EVIDENCE
    branches can only be exercised at N where strict Wilson > 0.75 is reachable
    (~ N ≥ 30 with high point estimate). The full-run validation happens at
    Manager-authorized N=96, downstream. Branch selector code is trivial and
    inspected; no defect.

  - ANALYZER INPUT SCHEMA — the analyzer expects per-context scored JSON files
    with fields {item, context, ground_truth, predicted, match}. The downstream
    scorer (between the model and the analyzer) is not built in this ACTION;
    it's a separate downstream component. The analyzer's input schema is the
    interface; CS recommends this schema be SE-verified as part of the tool-bytes
    review.
```

### 2.9 Ready for Senior verification

```text
READY: YES.

Senior may verify from bytes by:
  (a) reading the three .py tools and the neutral pool .md, confirming each
      implements the v0.4 §T contract verbatim;
  (b) re-running v3_prompt_realizer.py on path-a/build/items and confirming
      byte-identical output to the committed path-a/build/build_verification/
      prompts/ (determinism check; see §2.3);
  (c) re-running v3_prompt_conformance_checker.py and confirming 8/8 pass;
  (d) re-running v3_floor_check_analyzer.py on the three synthetic test
      scenarios and confirming the recorded branch verdicts;
  (e) inspecting wilson_ci() in the analyzer and confirming wilson_ci(81, 96)
      returns 0.7581 (matches v0.4 §7);
  (f) confirming no model imports / no model execution / no prompt execution
      via stdlib-only-imports check (§2.4).

After SE verifies, the next step in the routing chain is CS feasibility
re-review (per the original v0.4 §14 / §F3 routing).

CS holds for SE verification + next ACTION.
```

## 3. Commit + push + clean-fetch verification

```text
Step 1 commit                829e00cc0cc7377c734c7f9b31b2e6f6117e7280
                              (sweep of v0.4 + C5 PASS into path-a/in-review/)

Step 2 commit                to be recorded after the tooling commit lands
                              (this memo + tooling files)

final remote HEAD            (to be recorded in §4 after push)

clean-fetch                  to be appended in §4 after `git fetch origin`
                              + per-file sha256 verification against origin
                              bytes
```

## 4. Clean-fetch confirmation

Performed after the Step 2 commit landed; `git fetch origin` immediately preceded the verification. Each file's local sha256 was compared against `git cat-file -p origin/main:<path> | sha256sum`.

```text
Step 1 commit                829e00cc0cc7377c734c7f9b31b2e6f6117e7280
Step 2 commit                6d2ba00f317566900a9e1deb1a9b4a9498d4f562
final remote HEAD            6d2ba00f317566900a9e1deb1a9b4a9498d4f562
local       HEAD             6d2ba00f317566900a9e1deb1a9b4a9498d4f562   (match)

per-file verification (origin/main bytes → local bytes):

TOOLING ARTIFACTS (the four §T digests to be SE-verified and locked at approval):
MATCH  0f5a3f7438a6936fe449ea3558321a734b999b2ac2e8384032c2890e155f3585
       path-a/build/v3_floor_check_analyzer.py
MATCH  fb561fdc526115da94c6137b739e8bb3b6adf30825d83f864cda713bc0750909
       path-a/build/v3_prompt_realizer.py
MATCH  b8afa3f89dd7f375058500820bdf2bf58a46384d2283c8f2a31f1b8c92ad2b82
       path-a/build/v3_prompt_conformance_checker.py
MATCH  bc2020c2c4e1293f62c9f83a9b24a61f98c1ede35d5a071ee8cfd72a316ab0d9
       path-a/build/v3_neutral_token_pool.md

BUILD-VERIFICATION SUMMARIES (8-item demonstration batch):
MATCH  b010faffd9e8da9ac976fee6ed9dacf5e4f7298d33ede7df125aeabbf46409f1
       path-a/build/build_verification/realization_summary.json
MATCH  259410a302df889a997e1edbf1abb6fd9a709ed975b5701fa1c5ea7838d8ca9d
       path-a/build/build_verification/prompt_conformance_summary.json

V0.4 PREREG (under review; bytes intact, no edits):
MATCH  c5ec46194772f100681cf41a6b3dd2d0c51a2c1fb49a62b181741a74529ce7b0
       path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.4.md
MATCH  fd99a64aa70df42c49a190a39bc316f2cf4cbff40b8dd36d8b8b456102210f92
       path-a/in-review/C5-V3-FLOOR-CHECK-PREREG-CLAIM-RISK-v0.3.md

GOVERNANCE:
MATCH  bd42b4100a7ca203273c4e28ae825e7ddc6930b6fa1575ebaa8187f82b0d5211
       governance/2026-06-18_v3-floor-check-tooling-build/TL-MANAGER-ACTION-FILE-V0.4-AND-BUILD-TOOLING-2026-06-18.md
MATCH  65d0a03e3e7990656fe071f1d436b8c21c0bdf28eb23826048271b20980702a1
       governance/2026-06-18_v3-floor-check-tooling-build/CS-RETURN-TOOLING-BUILD-2026-06-18.md
                   ↑ this file, PRIOR to the §4 commit (the §4 commit's own
                     sha will be cross-verified on the next sweep)
```

All 10 listed key artifacts (the four tooling files, two build-verification summaries, two in-review prereg/review files, two governance memos) reproduce byte-exact from the shared repository on a clean fetch. The four §T tooling digests are exactly the digests to be SE-verified next and locked into v0.4's binding block at TL/Manager approval. **Floor-check tooling FILED. Ready for SE verification.**

---

— CS Engineer, 2026-06-18 (clean-fetch appendix)

---

## Non-authorizations (carried forward)

```text
- N=96 materialization                blocked (per ACTION)
- prompt generation for execution     blocked
- model run                           blocked
- floor-check run                     blocked
- compression                         blocked program-wide
- Claim C                             blocked
- Paper B                             blocked
- certification claim                 blocked
- capability claim                    blocked
- mechanism claim                     blocked
- candidate selection, threshold values, certification evaluation,
  multi-model, Fork A reactivation, public benchmark packaging,
  artifact mutation                   all carried per standing card

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc...) +
  tagged manuscript blob (7d6706a3...): never moved.
- tier0-run/ directory: sealed; no new files.

The Path A FP16 K=5 FAIL remains closed.
```

---

— CS Engineer, 2026-06-18
