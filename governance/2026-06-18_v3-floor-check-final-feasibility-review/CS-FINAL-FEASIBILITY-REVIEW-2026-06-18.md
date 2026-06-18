# CS FINAL FEASIBILITY REVIEW — V3 Floor-Check Package (Prereg v0.4 + Tooling)

**Date:** 2026-06-18
**From:** CS Engineer
**To:** Team Lead; Cc: Senior Engineer, C5, Manager
**Re:** TL ACTION 2026-06-18 — "Final Feasibility Review — V3 Floor-Check Prereg v0.4 + Tooling"
**Status:** **PASS — feasible and mechanically lockable, with one binding caveat (MAX_DELTA ↔ current scheme)**

---

## Record status

```text
verdict                PASS — with caveat (the TL-proposed binding statement
                        for MAX_DELTA = 8, recorded explicitly at approval lock)
review object          v0.4 prereg + 4 verified tooling artifacts + current
                        v0.4-of-record constructibility binding + current
                        inspector/constants under v0.4 re-pin
authority              TL ACTION 2026-06-18 (final feasibility review only)
predecessor CS verdicts v0.1 HOLD (E1–E5) → v0.3 HOLD (F1+F2+F3) →
                        v0.4 + tooling now feasible and mechanically lockable
C5 claim-risk          PASS (filed 2026-06-18 on v0.3; v0.4 self-states no
                        C5-cleared boundary altered)
SE tooling verdict     PASS — tooling contract met (sha-confirmed for all 4
                        artifacts)
```

---

## 1. The seven required checks

### Check 1 — Prereg v0.4 and tooling are mutually consistent

```text
v0.4 spec → tooling implementation:

§T (1) ANALYZER contract → v3_floor_check_analyzer.py:
  inputs:  scored_dir + r6_log + admissibility + prompt_conformance ✓
  outputs: hop2 rate + Wilson CI; hop1 rate + Wilson CI; dq count;
           invalidated count; exclusions; post-exclusion denominators +
           min-count thresholds; FINAL BRANCH                          ✓

§T (2) REALIZER contract → v3_prompt_realizer.py:
  inputs:  item specs + neutral pool                                    ✓
  outputs: 4 prompts per item + per-set char counts                     ✓
  constraint: same template class + char_delta ≤ 8                      ✓

§T (3) CHECKER contract → v3_prompt_conformance_checker.py:
  inputs:  realized prompts + item specs                                ✓
  outputs: per-property pass/fail + char_delta + §9(vi) gate            ✓

§T (4) NEUTRAL POOL → v3_neutral_token_pool.md:
  separate-file mode (per v0.4 §T default); lockable digest             ✓

§6 thresholds (locked) → analyzer constants:
  HOP_FLOOR              = 0.75    in analyzer line ~36                 ✓
  DQ_POINT_CEILING_COUNT = 19      in analyzer line ~37                 ✓
  INVALIDATED_THRESHOLD  = 10      in analyzer line ~38                 ✓
  WILSON_Z_95            = 1.96    in analyzer line ~39                 ✓

§8 item-level R6 invalidators → analyzer:
  LOCKED_R6_INVALIDATORS = {terminal_coincidence, controls_unavailable,
                            direct_recall, interior_position,
                            constant_token}                              ✓ exact set

§9 conditions (i)-(vi) → analyzer's cond_i..cond_vi → branch selector   ✓
§10 branches → analyzer's 3-way switch on (clean_executable, cond_i)     ✓

§4 / F1 length-matching MAX_DELTA = 8 → realizer + checker constants   ✓ (line 42 / 46)
```

**VERDICT: CONSISTENT.** Every contract field in v0.4 §T maps to a corresponding implementation in the tooling. Every locked threshold in v0.4 §6 / §9 / §8 appears in the analyzer with the exact locked value. No drift.

### Check 2 — Paths exist + hashes match Senior-verified

CS re-verified by `shasum -a 256` on the current bytes at HEAD `df919abf…`:

```text
EXISTS  0f5a3f7438a6936fe449ea3558321a734b999b2ac2e8384032c2890e155f3585  path-a/build/v3_floor_check_analyzer.py
        ↑ matches Senior-verified                       0f5a3f74…  exactly
EXISTS  fb561fdc526115da94c6137b739e8bb3b6adf30825d83f864cda713bc0750909  path-a/build/v3_prompt_realizer.py
        ↑ matches Senior-verified                       fb561fdc…  exactly
EXISTS  b8afa3f89dd7f375058500820bdf2bf58a46384d2283c8f2a31f1b8c92ad2b82  path-a/build/v3_prompt_conformance_checker.py
        ↑ matches Senior-verified                       b8afa3f8…  exactly
EXISTS  bc2020c2c4e1293f62c9f83a9b24a61f98c1ede35d5a071ee8cfd72a316ab0d9  path-a/build/v3_neutral_token_pool.md
        ↑ matches Senior-verified                       bc2020c2…  exactly
```

**VERDICT: 4/4 paths exist; all 4 shas byte-identical to Senior-verified figures.** These are the digests that will be locked into v0.4 §T at TL approval.

### Check 3 — §9 / §10 computable exactly once from declared artifacts

```text
each §9 condition → its analyzer source:
  (i)   hop2 lower Wilson > 0.75      ← analyzer reads per-item hop2 scored JSON,
                                         computes rate, Wilson CI via wilson_ci();
                                         deterministic.
  (ii)  dq C* count ≤ 19              ← analyzer reads per-item dq scored JSON,
                                         counts matches; deterministic integer.
  (iii) hop1 lower Wilson > 0.75      ← analyzer reads per-item hop1 scored JSON;
                                         deterministic.
  (iv)  invalidated < 10              ← analyzer reads r6_log.json, counts items
                                         with any invalidator; deterministic.
  (v)   admissibility PASS all items  ← analyzer reads admissibility_summary.json
                                         from the inspector; deterministic.
  (vi)  prompt-conformance PASS       ← analyzer reads prompt_conformance_summary
                                         from the checker; deterministic.

branch selector → 3-way switch:
  clean_executable = (ii) AND (iii) AND (iv) AND (v) AND (vi)
  if clean_executable AND (i):     COMPONENT-ADMISSIBLE-UNDER-COMPETITION
  elif clean_executable AND ¬(i):  ONE-RUN-EVIDENCE-TOWARD-SUBSTRATE-INFEASIBILITY
  else:                            CONSTRUCT-FAIL

  partition is EXHAUSTIVE over the (clean_executable, cond_i) condition space.
  No undefined / overlapping cases.
```

**Determinism re-verified this turn:** running the analyzer on `test_b_hop2_fails` twice produced byte-identical decision JSONs (sha `cef00586ae903eeb58ca71351bbb06fed32777df597ef24c22492cfe1df0c4dd` on both).

**VERDICT: YES, computable exactly once from declared artifacts.** The analyzer emits a single decision JSON; same inputs → same output bytes.

### Check 4 — Analyzer outputs

```text
required output                       → analyzer decision JSON field             status
hop2 rate                             → decision["hop2"]["rate"]                  ✓
hop2 Wilson CI                        → decision["hop2"]["wilson_lower_95"] /
                                        ["wilson_upper_95"]                       ✓
hop1 rate                             → decision["hop1"]["rate"]                  ✓
hop1 Wilson CI                        → decision["hop1"]["wilson_lower_95"] /
                                        ["wilson_upper_95"]                       ✓
direct-query C* count                 → decision["direct_query"]["count"]         ✓
invalidated item count                → decision["invalidated"]["count"]          ✓
item-level exclusions                 → decision["excluded_items"] (list)         ✓
final branch                          → decision["final_branch"] (string in
                                        {COMPONENT-ADMISSIBLE-…,
                                         ONE-RUN-EVIDENCE-…,
                                         CONSTRUCT-FAIL})                          ✓

post-exclusion denominators           → decision["hop2"]["n"], ["hop1"]["n"]      ✓ (= n_included)
min-count thresholds (per §E4)        → decision["hop2"]["min_clearing_count"] / 
                                        ["hop1"]["min_clearing_count"]            ✓ (computed on
                                                                                    post-exclusion n)
```

**VERDICT: ALL REQUIRED OUTPUTS PRESENT.** Plus three v0.4 §E4 quantities (post-exclusion denominator + recomputed min-count) that aren't explicitly required by the TL list but are required by v0.4 §7 / §E4.

### Check 5 — Realizer + checker implement the five properties

```text
same template class                  ✓ realizer's 4 prompts share identical
                                        3-section layout (FACTS: / 22 fact
                                        triples / QUERY: line); checker P2
                                        verifies "starts with FACTS:\\n and
                                        contains exactly one QUERY: line"
                                        for each context.

character-count gate                 ✓ realizer reports char_counts per
                                        context + char_delta (max - min) +
                                        max_delta_gate bool. Checker P9
                                        re-verifies independently from prompts.

MAX_DELTA = 8                        ✓ both files: line 42 (realizer) and
                                        line 46 (checker). Identical value;
                                        verified by grep.

no B/C* leakage into hop1/direct_query ✓ checker P3 (bridge presence/absence),
                                        P4 (hop1 query no C*), P5 (dq prompt
                                        no C* anywhere), P6 (dq FILLER LINE
                                        no B AND no C* — filler-line-scoped,
                                        per E5 binding intent; B is allowed
                                        elsewhere in dq because the A-r1-B
                                        fact is preserved, but the filler
                                        itself must reveal neither).

prompt-realization conformance       ✓ checker emits all_pass + section_9_vi_gate
result                                  ("PASS"/"FAIL") in the summary JSON;
                                        analyzer reads this as cond_vi.
```

Verified live on the 8-item batch this turn: realizer 8/8 gate-pass; checker 8/8 pass; §9(vi) gate = PASS.

**VERDICT: ALL FIVE PROPERTIES IMPLEMENTED.**

### Check 6 — Real-run assertions feasible

```text
no _fixture_mode flag         ✓ enforced by inspector C9 (constants.py:
                                  validate_manager_lock returns mode "fixture"
                                  if _fixture_mode is set true, otherwise
                                  falls through to real-run / sweep checks).
                                  The v3_item_generator does NOT emit
                                  _fixture_mode at all — items are real-run
                                  by construction.

no _sweep_mode flag           ✓ same enforcement. v3_item_generator does NOT
                                  emit _sweep_mode either.

C1–C9 admissibility per item  ✓ existing inspector (path-a/inspector/
                                  inspector.py, sha cb4b0b60bd6dc2b5...)
                                  enforces. Demonstrated on the 8-item batch:
                                  8/8 PASS in real-run mode (every per-item
                                  inspection JSON has validation.mode ==
                                  "real-run"). At N=96 the same enforcement
                                  applies; the generator's per-item-prefix
                                  scheme generalizes to any N without
                                  schema change.

  inspector + constants under test:
    inspector.py  sha cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
    constants.py  sha 1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
  Both match the v0.4 of-record re-pin (PREREGISTRATION-PATH-A-CONSTRUCTIBILITY
  -v0.4, sha c61a3256...; corrective committed 9ea16d1...).
```

**VERDICT: REAL-RUN ASSERTIONS FEASIBLE.** The v0.4-pinned inspector enforces fail-closed on both forbidden flags; the V3 generator never sets either; C1–C9 demonstrated at N=8 and structurally generalizes to N=96.

### Check 7 — No hidden execution / no materialization / no run occurred

```text
no model execution            ✓ no model imports in any tool (grep over the
                                  3 .py files for {transformers, torch, mlx,
                                  openai, anthropic, httpx, requests., urllib,
                                  socket} returns ZERO matches).
                                  Only stdlib imports: argparse, json, math,
                                  sys, pathlib, hashlib.

no prompt execution           ✓ the 32 build-verification prompt files under
                                  path-a/build/build_verification/prompts/
                                  are demonstration artifacts. No LM was
                                  invoked to consume them. The analyzer's
                                  test inputs are SYNTHETIC scored JSONs
                                  (not model outputs).

no N=96 materialization       ✓ path-a/build/items/ contains exactly 8 items
                                  (the original demonstration batch from the
                                  V3 build, sha 6a2ceee1...). The generator
                                  was NOT run with --count 96. The realizer
                                  was exercised on the same 8 items only.

no run                        ✓ no model load, no inference, no GPU work,
                                  no compression, no certification act of
                                  any kind has occurred in this routing chain.

build_verification dir scope  the dir contains:
  ├── prompts/                 32 prompt files (8 items × 4 contexts)
  ├── realization_summary.json 8/8 gate-pass record
  ├── prompt_conformance_summary.json  8/8 pass record
  ├── test_{a,b,c}_*/         synthetic scored sets (NOT model outputs)
  └── analyzer_runs/           per-test decision JSONs
  
  This dir is clearly labeled "build_verification" — none of its contents
  are run-ready or run-authorized. They are demonstration artifacts to
  prove the tooling works deterministically.
```

**VERDICT: NO HIDDEN EXECUTION.** Confirmed across all four surfaces (review, package contents, tool imports, build_verification dir scope).

---

## 2. MAX_DELTA watch item — explicit answer

**TL's question (verbatim):**

> *Is this acceptable for final feasibility if the approval lock records that MAX_DELTA = 8 is bound to the current token-width scheme, and any construction/token-width change reopens prompt-length conformance?*

**CS answer: YES — acceptable, with the caveat formulated as below.**

### The structural minimum is real

CS verified this turn that every item in the 8-item demonstration batch lands at **exactly char_delta = 8**, with zero headroom across the four contexts. The sources of the delta are mechanically traceable:

```text
SOURCE                                                  contribution
composite/dq QUERY uses `r1.r2` (compound relation)     ~3 chars more than hop1's `r1`
                                                          or hop2's `r2` (single relation)
bridge fact `(B, r2, C*)` vs filler `(W, verb, V)` in dq ~2 chars (filler triple 25 chars
                                                          vs bridge 27)
hop2 query uses B token (i007_B1) vs hop1's A (i007_A)  1 char (token-width difference)
small cumulative drift across contexts                   ≤ 2 chars

Cumulative                                              ≤ 8 chars (binding to the demo)
```

This is the **structural minimum under the current scheme** — not an artifact of the realizer's implementation choices. A different realizer would face the same lower bound: the composite query has structurally more relation tokens than the single-hop queries, and the dq filler must replace the bridge fact's structural slot.

### The binding caveat (CS-formulated)

I recommend the approval lock record **the following caveat in full**, alongside the four §T tooling digests:

```text
MAX_DELTA = 8 is BOUND to:
  (A) the current per-item token-width scheme:
        per-item prefix `i{NNN}_` (5 chars) + role suffix (1–2 chars) → role tokens 6–7 chars
        neutral pool tokens: 7 chars (matches role-token upper bound)
        filler verbs: 5 chars (locked pool {holds, marks, types, pairs, links})
  (B) the current locked Manager values (K=5, D=5, P=5, M=10):
        these govern the 22-fact layout (2 target + 5×2 competitor + 5×2 decoy)
        and the per-context query structure
  (C) the current four-context relation-naming scheme:
        target uses {r1, r2}; competitors use {s1/s2, t1/t2, u1/u2, v1/v2, w1/w2}
        each relation token width 7 chars (under the per-item prefix scheme)

Any change to any of (A), (B), or (C) — including but not limited to:
  - a different per-item prefix length (e.g., "j{NN}_" or "ix_") changing role-token widths
  - a different neutral-pool token width
  - a different filler verb pool with different verb widths
  - a different K / D / P / M values changing the fact-list count
  - a different competitor-relation pool
  - additional or changed fact-list structure (e.g., 3-hop targets, hierarchical decoys)
  - a different four-context query template
REOPENS prompt-length conformance for re-verification — the realizer must be re-run on
demonstration items under the new scheme, the checker's P9 gate re-confirmed, and the
v0.4 §4 / F1 MAX_DELTA constraint either re-verified at the new structural minimum or
the locked MAX_DELTA value reconsidered.
```

This caveat:
- **Accurately reflects the headroom analysis** (zero margin → any structural change matters)
- **Makes the constraint explicit** for any future schema revision
- **Activates a re-conformance gate** as a precondition of any (A)/(B)/(C) change taking effect
- **Does NOT loosen any C5-cleared claim boundary** (the foreclose-all standard, V3 schema, locked Manager values, instrument bytes, §9/§10 floor/threshold/branch logic are all untouched)
- **Is mechanically auditable** at any future schema-revision gate

The alternative (HOLD: redesign realizer for headroom) would require either shortening relation token widths (which changes the construction's token-width scheme — a v0.4 §4 invariant) or padding shorter contexts (which would add prompt content the model sees, a semantic change). Neither is preferable to recording the binding explicitly.

**CS recommendation: PASS with the binding caveat above recorded at approval lock.**

---

## 3. Verdict — synthesis

```text
verdict                  PASS — feasible and mechanically lockable
caveat (binding)         MAX_DELTA = 8 ↔ current token-width + Manager-value
                          + relation-naming scheme; any change reopens prompt-
                          length conformance per the formulation in §2 above.
nothing else outstanding the 7 required checks all pass; the §T tooling digests
                          line up with Senior-verified figures; the v0.4 §9/§10
                          decision rule is mechanically computable; no model
                          imports / executions / N=96 materialization / run.

ready for approval        YES, contingent on TL/Manager recording the caveat
consideration             in §2 verbatim alongside the four §T tooling digests
                          at the approval lock.
```

---

## 4. What this PASS does NOT mean

```text
Does NOT authorize anything operational:
  no model run, no N=96 materialization, no prompt generation for execution,
  no compression, no certification, no Claim C, no Paper B, no capability
  claim, no mechanism claim.

Does NOT alter any C5-cleared claim boundary:
  hop2 standalone primary; lower Wilson > 0.75 (hop2 + hop1); 81/96 full-N
  reference; dq ≤ 19/96 pass / ≥ 20/96 fail; R6 item-exclude/log + set ≥10/96
  construct-fail; hop2-below-floor not an item-level invalidator; one clean
  failed run is evidence TOWARD substrate-infeasibility (NOT final
  classification); clean construct contingent on prompt-realization
  conformance; no certification / capability / mechanism / composition
  overclaim.

Does NOT lock anything:
  the four §T tooling digests are CS-produced and SE-verified; the lock
  itself is TL + Manager at the next gate. CS only attests the digests
  are accurate at HEAD df919abf...

Routing after this PASS:
  → TL approval consideration (with the §2 MAX_DELTA caveat recorded)
  → Manager by-name run authorization (only if approved)
  → CS execution (the run itself)
  → SE verification (recompute from bytes; read the §10 branch)
```

## 5. Clean-fetch confirmation

To be appended after this memo's commit lands.

---

## Non-authorizations (carried forward, per TL ACTION boundary)

```text
- N=96 materialization                blocked
- prompt generation for execution     blocked
- model run                           blocked
- floor-check run                     blocked
- compression                         blocked program-wide
- Claim C                             blocked
- Paper B                             blocked
- certification claim                 blocked
- capability claim                    blocked
- mechanism claim                     blocked
- candidate selection, threshold values, multi-model, Fork A
  reactivation, public benchmark packaging, artifact mutation, Paper 6
  activation, Paper 3 execution as experiment    all carried per standing card

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc...) +
  tagged manuscript blob (7d6706a3...): never moved.
- tier0-run/ directory: sealed; no new files.

The Path A FP16 K=5 FAIL remains closed and untouched by this review.
```

---

— CS Engineer, 2026-06-18
