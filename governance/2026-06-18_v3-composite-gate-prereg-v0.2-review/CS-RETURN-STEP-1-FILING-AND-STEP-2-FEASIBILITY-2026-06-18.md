# CS RETURN — V3 Composite Gate Prereg v0.2: Step 1 (PASS — Filed) + Step 2 (PASS — Feasible with notes)

**Date:** 2026-06-18
**From:** CS Engineer
**To:** Team Lead; Cc: Senior Engineer, C5, Manager
**Re:** TL ACTION 2026-06-18 — "File and Review V3 Composite Gate Prereg v0.2"
**Status:** **STEP 1 PASS — v0.2 filed. STEP 2 PASS — feasible with implementation notes (no edits required).**

---

## Record status

```text
artifact under review        path-a/in-review/PREREGISTRATION-V3-COMPOSITE-GATE-v0.2.md
                              sha256 df26dc65ac3dd76bb09fa84c4688b8835f49282e2a8f77ea4b94991308e57275
authority                    TL ACTION 2026-06-18 ("File and Review V3 Composite
                              Gate Prereg v0.2")
predecessor                  v0.1 sha ee1ad41d… ("V3 Composite Certification" title;
                              CS feasibility HOLD on E1; C5 access HOLD)
Step 1 (filing)              PASS — v0.2 filed verbatim at TL-specified path
Step 2 (feasibility)         PASS-with-notes — feasible as written; the §4 "CS
                              FEASIBILITY ITEM" (generator-start-index) is structurally
                              correct as routed (handled at the tooling-build step,
                              same pattern as floor-check v0.4's unbuilt tools)
C5 lane (parallel)           v0.1 C5 review and v0.2 C5 review both ARTIFACT-ACCESS
                              HOLDs; both files now on origin/main; C5 can re-review
                              with byte access on the next cycle
```

---

## Step 1 — Filing return fields (per TL ACTION)

```text
commit                       to be recorded in §3 once it lands
final remote HEAD            to be recorded in §3 once push completes
filed path                   path-a/in-review/PREREGISTRATION-V3-COMPOSITE-GATE-v0.2.md
                             (exactly the TL-specified path; inbox source was named
                              PREREGISTRATION-V3-COMPOSITE-GATE-PATH-A-v0.2.md; the
                              "-PATH-A-" infix is dropped at filing per TL's destination
                              path, consistent with v0.2/v0.3/v0.4 naming convention)
sha256 digest                df26dc65ac3dd76bb09fa84c4688b8835f49282e2a8f77ea4b94991308e57275
clean-fetch confirmation     to be recorded in §3 after `git fetch origin` + per-file
                             verification

bytes match Senior v0.2 source           YES.
  Inbox source sha:                       df26dc65ac3dd76bb09fa84c4688b8835f49282e2a8f77ea4b94991308e57275
  Filed destination sha (after cp):       df26dc65ac3dd76bb09fa84c4688b8835f49282e2a8f77ea4b94991308e57275
                                                                                          ^ identical
  No scientific content edited at filing; rename only.

confirmation C5 can access the object    YES via the standing review-track mechanism
                                          (path-a/in-review/README.md §"Provenance" +
                                          contributors clean-fetch path). The two C5
                                          reviews that returned ARTIFACT-ACCESS HOLDs
                                          (v0.1 access + v0.2 filing-not-yet-propagated)
                                          can both be re-reviewed once this commit
                                          propagates to origin/main — the bytes will
                                          reproduce from origin via `git cat-file -p
                                          origin/main:<path>`, which is C5's access
                                          mechanism.
```

---

## Step 2 — CS feasibility review

### Verdict: **PASS — executable as written**

The §4 "CS FEASIBILITY ITEM" (generator-start-index support) is **structurally correctly routed** as an item for the subsequent tooling-build action — the same pattern the program already accepted for the floor-check v0.4 prereg, where the four tooling artifacts (analyzer, realizer, checker, neutral pool) were NAMED in §T with `sha256: LOCKED AT APPROVAL` but did not yet exist; CS built them under a separate TL/Manager ACTION 2026-06-17 ("Begin V3 Build Open Slots"), and §T was locked at TL approval thereafter.

CS does NOT require pre-build resolution as an edit to v0.2. CS does require, per §1.1 below, that the §T binding be **updated at the tooling-build step** to reflect either (A) the new generator sha if patched, or (C) a new wrapper-script entry if that approach is chosen — analogous to the v0.4 §16 byte-binding re-lock.

### 1. CS focus answers (the seven from TL ACTION)

#### 1.1 Fresh materialization — can the current generator produce 097..192?

**At the current sha (`6a2ceee1…`): NO.** CS re-verified (matches prior review): the generator's `main()` iterates `for n in range(1, args.count + 1)`, so `--count 96` always produces items 1..96 byte-identical to the floor-check. There is no `--start-index` parameter.

**At a patched / wrapped generator: YES.** v0.2 §4 explicitly names this as a "CS FEASIBILITY ITEM" to be resolved at the tooling-build step. Three options (sketched in CS's prior v0.1 review, carried forward):

```text
OPTION A   Patch v3_item_generator.py to add a `--start-index N` parameter (additive;
           default 1 preserves existing behavior; no behavior change at start-index=1).
           Generator digest CHANGES from 6a2ceee1... to a new value; §T binding must
           be re-locked at the tooling-build step.

OPTION C   Build a new wrapper v3_composite_gate_item_generator.py that calls the
           underlying `generate_item()` function directly for indices 097..192.
           Generator sha 6a2ceee1... stays unchanged (§T's "REUSED UNCHANGED" line is
           literally true); a NEW entry is added under §T's NEW section for the wrapper.
```

CS does NOT recommend a specific option; Senior + tooling-build action picks one. Both are mechanically achievable; both are bounded; both fit the program's established lockable-digest discipline.

#### 1.2 Generator support — start-index exists or must be added?

**Must be added** (per §1.1). Re-grep:

```text
$ grep -E "add_argument|--start-index" path-a/build/v3_item_generator.py
    p.add_argument("--out-dir", type=Path, required=True, ...)
    p.add_argument("--count", type=int, default=8, ...)
    p.add_argument("--verbose", action="store_true", ...)
```

No `--start-index`. The patch is small (~10 lines) and additive — does not alter existing behavior at the default start-index of 1.

#### 1.3 Disjointness — does 097..192 produce byte-distinct items/prompts from 001..096?

**YES — mechanically provable** by the per-item-prefix scheme.

```text
Per v3_token_pool.md §3 + the generator's _item_prefix(N) = f"i{N:03d}_":
  - item index 7 → prefix "i007_" → role tokens i007_A, i007_B1, i007_C1, ...
  - item index 107 → prefix "i107_" → role tokens i107_A, i107_B1, i107_C1, ...
  - Different prefixes → different role-token strings → different specs → different prompts.

For ANY N ∈ {097..192} and M ∈ {001..096}:
  N ≠ M → string "i{N:03d}_" ≠ string "i{M:03d}_" → cross-set token disjoint.

Proof of byte-distinctness extends through:
  - item specs (different role tokens throughout the spec JSON)
  - prompts (the role tokens appear in fact triples and queries)
  - admissibility results (per-item ids differ)
  - scored outputs (per-item dirs differ)

The disjointness is structural, not statistical. Provable by the deterministic
prefix scheme.
```

#### 1.4 MAX_DELTA — does 097..192 preserve the 3-digit token-width scheme?

**YES — preserved.** Per v0.2 §4 (mandatory ≤999 constraint):

```text
Max index in {097..192}:  192
String representation:    "192"
Digit width:              3
Prefix:                   "i192_"
Prefix width:             5 chars (i + 3 digits + _)
Role token widths:        identical to floor-check (i007_A is 6 chars; i192_A is 6 chars;
                          i007_B1 is 7 chars; i192_B1 is 7 chars; etc.)

→ MAX_DELTA=8 binding (current token-width scheme) is UNAFFECTED by the index range.

If indices crossed 999, the prefix would widen to 4 digits ("i1000_"), all role tokens
would grow by 1 char, the bridge fact width would change, and the MAX_DELTA gate would
need re-validation. v0.2 §4 explicitly locks the ≤999 constraint to prevent this.
The {097..192} range satisfies it with substantial margin (max 192 « 999).
```

This is **mechanically guaranteed** and does not require re-running the prompt-conformance check on the fresh set to validate (though that check WILL re-run on the fresh items per v0.2 §6 — it just isn't expected to fail on MAX_DELTA grounds).

#### 1.5 New tools — feasibility of `v3_composite_gate_analyzer.py` + `v3_composite_error_logger.py`?

**FEASIBLE.** Both follow the established template from `v3_floor_check_analyzer.py` + `build_r6_log.py` + `v3_conformance_runner.py`.

```text
v3_composite_gate_analyzer.py
  CONTRACT (per v0.2 §T):
    inputs    --scored-dir (fresh N=96 scored outputs)
              --items-dir (fresh item specs with ground truth)
              --r6-log (R6 invalidation log, fresh set)
              --admissibility (inspector summary, fresh set)
              --prompt-conformance (checker summary, fresh set)
              --error-log (from v3_composite_error_logger.py)
              --output (decision JSON path)
    outputs   composite-correct k/n + rate + Wilson 95% CI;
              re-confirmed precondition status (hop2, hop1, dq, admissibility,
              conformance) per v0.2 §6;
              two gates per v0.2 §7: (a) lower-Wilson > 0.75 reliability,
                                     (b) lower-Wilson > 0.45 not-shortcut floor;
              §7/§8 branch: GATE-CLEARED-THIS-RUN /
                            COMPOSITE-DOES-NOT-CLEAR-THIS-RUN /
                            PRECONDITION-FAIL /
                            CONSTRUCT-FAIL
              this-run/final boundary attestation
    contract  pure function of inputs; no clock, no RNG, no environment, no
              network; same inputs → byte-identical output JSON.
    digest    LOCKED AT APPROVAL.

v3_composite_error_logger.py
  CONTRACT (per v0.2 §9):
    inputs    --scored-dir, --items-dir
    outputs   per-item error characterization (WHERE landed: correct-chain
              wrong-depth / decoy-chain depth-2 / competitor / other) and
              CO-OCCURRENCE (inherited-component-failure / composition-specific);
              pathological-error-structure flag for §7(e)
    contract  pure function of inputs; deterministic.
    digest    LOCKED AT APPROVAL.
```

Both are ~150-250 lines each, achievable. Both inputs/outputs are mechanically computable from the fresh scored set + item specs. Both lockable as additive artifacts.

#### 1.6 Reused tools — realizer/checker/pool/inspector/constants reused unchanged after §1.1 resolution?

**YES — 5/5 reusable.**

```text
realizer       v3_prompt_realizer.py            fb561fdc...  pure function of (spec, pool);
                                                              works on any item indices
checker        v3_prompt_conformance_checker.py b8afa3f8...  pure function of (specs, prompts);
                                                              works on any item indices
neutral pool   v3_neutral_token_pool.md         bc2020c2...  fixed resource; index-agnostic
inspector      path-a/inspector/inspector.py    cb4b0b60...  schema-level; works on any item
constants      path-a/inspector/constants.py    1d761c3d...  locked values; index-agnostic
```

All five are index-agnostic by construction. The per-item-prefix scheme generalizes to any 3-digit index N ∈ [1..999] without any tool change. v0.2 §T's "REUSED UNCHANGED" claim is **literally true** for these five. (The sixth — generator — is the §4 "CS FEASIBILITY ITEM" handled per §1.1.)

#### 1.7 No hidden execution — does v0.2 authorize anything?

**CONFIRMED — NO.** v0.2 §E verbatim:

```text
"This preregistration authorizes:
   No new run.  No fresh materialization yet.  No prompt generation.  No tooling
   creation.  No compression / INT8 / INT4.  No Claim C.  No Paper B.  No
   certification claim (only GATE-CLEARED-THIS-RUN if the §7 gate clears on the
   fresh run; FINAL certification is a separate decision).  No capability claim.
   No mechanism claim."
```

The two new tools are explicitly "built under a SEPARATE TL/Manager tooling-build action" (§T). The fresh materialization is explicitly downstream of Manager by-name run authorization (§E routing).

This filing turn (CS review + C5 review on bytes) is review-only.

### 2. Routing recommendation

```text
The §4 "CS FEASIBILITY ITEM" (generator-start-index) is correctly scoped as a
tooling-build deliverable. CS recommends the following routing be preserved
into the next TL/Manager tooling-build action (mirroring TL/Manager ACTION
2026-06-17 "Begin V3 Build Open Slots"):

  Senior v0.2 (filed; this turn) → CS feasibility PASS (this memo)
   → C5 claim-risk re-review (now byte-accessible post-push)
   → TL approval consideration (with §4 generator-patch noted as tooling-build
      deliverable + §T binding to be updated at tooling-build step)
   → Manager + TL "Begin V3 Composite-Gate Tooling Build" ACTION authorizing CS
      to build the two new tools (analyzer + error logger) AND resolve the
      generator-start-index need (either Option A patch or Option C wrapper —
      Senior or tooling-build ACTION specifies)
   → CS builds; SE verifies tool bytes; §T binding re-locked with new/added digests
   → CS feasibility re-review against locked bytes
   → Manager by-name RUN authorization (fresh N=96 {097..192} certification run)
   → CS execution → SE verification
```

### 3. Commit + push + clean-fetch verification

To be appended after this memo's commit lands.

### 4. Side-bar — addressing the two C5 ARTIFACT-ACCESS HOLDs

```text
C5 v0.1 review (sha 07050ecc…)   VERDICT: HOLD — ARTIFACT ACCESS
                                  Filed at path-a/in-review/. Superseded by C5 v0.2
                                  attempt; will not be re-attempted on v0.1 because
                                  v0.2 supersedes the artifact.

C5 v0.2 review (sha 7df2689c…)   VERDICT: HOLD — ARTIFACT ACCESS (filing-not-yet-
                                  propagated variant)
                                  C5 reviewed before v0.2 propagated to origin.
                                  This commit (referenced in §3) puts v0.2 (sha
                                  df26dc65…) on origin/main. C5 can re-review
                                  with `git fetch origin && git cat-file -p
                                  origin/main:path-a/in-review/PREREGISTRATION-V3-
                                  COMPOSITE-GATE-v0.2.md` and will receive
                                  byte-identical Senior content.

CS does not preempt C5's substantive review; both reviews are filed as version
trail and C5 holds the claim-risk lane on the byte-accessible v0.2.
```

---

## Non-authorizations (carried forward, per TL ACTION boundary)

```text
- new run / rerun                    blocked
- fresh materialization              blocked (this ACTION is filing/review only)
- prompt generation                  blocked
- tooling creation                   blocked (generator patch + 2 new tools require a
                                              SEPARATE TL/Manager tooling-build ACTION)
- compression / INT8 / INT4          blocked
- Claim C, Paper B                   blocked
- certification claim                blocked (only GATE-CLEARED-THIS-RUN if §7 gate
                                              clears; FINAL is a separate decision)
- capability claim, mechanism claim  blocked
- candidate selection, threshold values, multi-model, Fork A reactivation,
  public benchmark packaging, artifact mutation, Paper 6, Paper 3 execution
  as experiment                      all carried per standing card

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc…) + tagged manuscript
  blob (7d6706a3…)                   never moved
- tier0-run/ directory               sealed; no new files

The Path A FP16 K=5 FAIL remains closed.
```

---

— CS Engineer, 2026-06-18
