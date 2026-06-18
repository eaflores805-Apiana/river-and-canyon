# CS FEASIBILITY RE-REVIEW — V3 Floor-Check Preregistration v0.3

**Date:** 2026-06-18
**From:** CS Engineer
**To:** Team Lead; Cc: Senior Engineer, C5, Manager
**Re:** TL ACTION 2026-06-18 — "Review Filed V3 Floor-Check Preregistration v0.3"
**Status:** **HOLD — feasible with required edits + one routing prerequisite**

---

## Record status

```text
artifact under review        path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.3.md
                              sha256 df82b34c4f96e085ea51b8e6e1a735849a39b108b321f79e30b9f20cffa19d5b
authority for review         TL ACTION 2026-06-18 ("Review Filed V3 Floor-Check Preregistration v0.3")
predecessor                  v0.1 CS HOLD (E1–E5) at governance/2026-06-18_v3-floor-check-prereg-review/
                              CS-FEASIBILITY-REVIEW-2026-06-18.md
verdict                      HOLD — feasible with required edits + one routing prerequisite

what v0.3 resolved (vs v0.1) E1 named analyzer (path + intent + I/O spec);
                              E2 DQ ceiling as exact point count (≤19/96 pass / ≥20/96 fail);
                              E3 R6 split (item-level exclude+log; set-level ≥10/96 fail);
                              E4 hop1 Wilson-lower>0.75 made parallel to hop2;
                              E5 length matching set to "character count + same template class"

what still HOLDs              F1 MAX DELTA tolerance still verbal ("predeclared"); needs numeric
                              F2 prompt-realizer + prompt-level conformance checker need
                                 analogous lockability treatment to the analyzer
                              F3 (ROUTING PREREQUISITE, not prereg defect): analyzer script
                                 does not exist; TL/Manager must separately authorize CS to
                                 build {analyzer, realizer, checker} before approval is possible

C5 lane                       independent; this review covers CS feasibility only.
```

---

## 1. Required CS focus answers (the five from TL ACTION)

### 1.1 Analyzer lockability — **CANNOT BE LOCKED YET** (routing prerequisite F3)

```text
CS-checked at HEAD 2f0f167e... (origin/main):

  $ ls path-a/build/v3_floor_check_analyzer.py
  ls: path-a/build/v3_floor_check_analyzer.py: No such file or directory

The script v0.3 §E1 names DOES NOT EXIST in the repo at HEAD.
```

This is not a defect in v0.3 — v0.3 correctly says the analyzer digest is "LOCKED AT APPROVAL" (§E1) and that "CS produces it; SE verifies it from bytes; TL/Manager lock its digest at approval." That sequence is correct. What v0.3 *cannot* do is make the script exist.

**Required artifact spec (CS-deliverable, when authorized):**

```text
path:               path-a/build/v3_floor_check_analyzer.py
intent:             deterministically compute floor-check metrics + §9/§10 branch
                    from per-context scored outputs + R6 log; no model code
implements:         the v0.3 §E1 spec verbatim (inputs / outputs / contract)
shape:              CLI tool: --scored-dir <dir of per-item per-context JSON>
                              --invalidation-log <R6 firing log path>
                              --ground-truth <materialized C* / B mapping>
                              --output <final decision JSON path>
                    exit 0 iff component-admissible-under-competition;
                    exit 1 iff null/substrate-infeasibility-evidence;
                    exit 2 iff construct-fail.
determinism:        pure function of inputs; no clock, no RNG, no env;
                    same inputs → byte-identical output JSON
lockable digest:    sha256 of the .py bytes, fixed at approval; recorded
                    in the v0.3 §16-style binding block alongside
                    inspector.py / constants.py / generator
```

**Routing prerequisite F3 (TL/Manager):** Before this prereg can be approved, the analyzer must exist, be SE-verified against the §E1 spec, and have its digest locked. The TL ACTION boundary "No analyzer creation yet unless separately authorized" puts the analyzer in the same posture the V3 build was in before TL/Manager ACTION 2026-06-17 ("Begin V3 Build Open Slots") — it requires its own ACTION. CS does not create artifacts without authorization; flagging the need.

### 1.2 Prompt length matching — **NOT EXECUTABLE AS WRITTEN** (required edit F1)

v0.3 §4 specifies the metric (character count) and the template-class rule, but leaves the tolerance verbal:

```text
"the residual character-count delta across the four contexts must be <= a predeclared MAX DELTA"
```

Without a numeric MAX DELTA, the prompt-realizer cannot enforce it, the prompt-level conformance checker cannot verify it, and the §9(vi) clean-construct gate cannot evaluate it. **F1 — required edit.**

**CS-proposed exact numeric tolerance** (final value is SE/Manager to lock; CS proposes):

```text
MAX DELTA = 8 characters
  (interpreted: for any item set N, max over the four contexts of character-count
   MINUS min over the four contexts of character-count must be ≤ 8.)

WHY 8 (the chosen number, with rationale):
  - The four contexts share an identical surface template (§4 "same template class").
    The only character-count variation across contexts within an item is from:
      (a) the question text substituting a different role token (e.g., "A's r1"
          vs "B's r2"); per-item prefix tokens are uniform-width (e.g., "i007_A",
          "i007_B1", "i007_r1" all 6–7 chars); typical delta ≤2 chars.
      (b) the direct-query filler substitution: "neutral marks placeholder"
          replaces the withheld "i007_B1 r2 i007_C1" bridge fact; with a
          length-matched neutral pool (filler verbs already 5-letter — see
          v3_direct_query_filler.md), typical delta ≤4 chars.
    Cumulative worst-case delta from (a) + (b): ~6 chars.
    8 gives a 2-char safety margin without permitting a salience signal.
  - 8 chars is ~1–3% of typical four-context prompt length; below the
    threshold a model could reliably exploit as a context-routing signal.
  - The number is small enough to actually drive realizer/checker logic
    (i.e., the realizer fails fast if its templates drift; the checker
    catches small bugs early) without being unrealistically tight.

ALTERNATIVES SE could prefer (each defensible, each numeric):
  - 4 chars: very tight; demands carefully-matched neutral-token pool
  - 16 chars: comfortable; still small as a fraction of total prompt length

If SE prefers a different value, the value lockability is what matters; CS
flags only that the number must be a number, not a placeholder.
```

### 1.3 Analyzer digest — **WHAT MUST BE LOCKED BEFORE APPROVAL**

Per v0.3 §E1 + §13 + the spirit of the v0.4 byte-binding block, the digests that must be locked into the prereg (or a §16-style binding addendum) before TL approval are:

```text
REQUIRED LOCKED DIGESTS:

1. analyzer:                    path-a/build/v3_floor_check_analyzer.py
                                sha256: TBD (does not exist; F3)

2. prompt realizer:             path-a/build/v3_prompt_realizer.py
                                sha256: TBD (does not exist; F2 + F3)
                                v0.3 §4 mentions four-context prompt realization but does NOT
                                name a script. F2 — required edit: name it parallel to §E1.

3. prompt-level conformance     path-a/build/v3_prompt_conformance_checker.py
   checker:                     sha256: TBD (does not exist; F2 + F3)
                                v0.3 §4 mentions "prompt-level conformance check must confirm
                                realized prompts preserve foreclose-all properties" but does
                                NOT name a script. F2 — required edit: name it parallel to §E1.

4. neutral-token pool used by   path-a/build/v3_neutral_token_pool.json (or equivalent)
   direct-query filler          sha256: TBD (does not exist)
   substitution:                v0.3 inherits v3_direct_query_filler.md's "{W}/{V} substitution
                                downstream" guarantee but does NOT pin a concrete pool. This is
                                a minor F2 item — could be a const in the realizer.

ALREADY LOCKED (no edit needed):
  inspector.py     cb4b0b60bd6dc2b5... (matches v0.4 of-record re-pin)
  constants.py     1d761c3d1c56e7ac... (matches v0.4 of-record re-pin)
  generator        6a2ceee15442ebbd...
  conformance runner 2a4408353e3713e3...
  build design docs (4 files; v3_token_pool, v3_direct_query_filler, v3_relation_balance, v3_seed_plan)
```

v0.3 names exactly one of these four (the analyzer at §E1). **F2 — required edit:** treat the realizer, prompt-level checker, and neutral-token pool with the same lockability discipline as the analyzer — name the path, specify the I/O contract, declare the digest as "LOCKED AT APPROVAL."

### 1.4 Exact decision-rule computability — **YES, AFTER F1 + F2 + F3 ARE RESOLVED**

§9 conditions trace to artifacts as follows:

```text
(i)   hop2 lower Wilson > 0.75              ← analyzer (§E1) reads per-item hop2 scored
                                              outputs; computes rate + Wilson CI; lockable
(ii)  direct-query C* count ≤ 19/96         ← analyzer reads per-item dq scored outputs;
                                              point count; trivially mechanical
(iii) hop1 lower Wilson > 0.75              ← analyzer; symmetric to (i)
(iv)  invalidated count ≤ 9/96              ← analyzer reads R6 invalidation log; count
(v)   C1–C9 admissibility PASS on all 96    ← existing inspector (cb4b0b60...) outputs;
                                              N=96 inspector results aggregated by analyzer
(vi)  prompt-realization conformance PASS   ← prompt-level checker (TBD; F2) outputs;
                                              aggregated by analyzer

ANALYZER OUTPUT: a single JSON with each of (i)-(vi) computed once, plus the §9/§10 branch
                  selection deterministically derived from the six values.

REQUIRES (cannot compute before): F1 (numeric MAX DELTA — used in (vi) checker);
                                   F2 (named realizer + checker; otherwise (vi) has no source);
                                   F3 (artifacts must exist).

AFTER (with F1+F2+F3 resolved): YES, §9/§10 is computed exactly once from declared artifacts.
                                Each input is byte-locked (specs, prompts, scored outputs, R6 log,
                                inspector results, conformance results); analyzer is byte-locked
                                (LOCKED AT APPROVAL); output is a pure function of inputs.
```

§10 branches:

```text
ONE-RUN-EVIDENCE-TOWARD-SUBSTRATE-INFEASIBILITY — computable by analyzer when (ii)-(vi) PASS but (i) fails
FINAL-SUBSTRATE-INFEASIBILITY                     — explicitly DEFERRED to cross-run aggregation
                                                    in v0.3 §10 ("requires repeated admissible failures");
                                                    correctly NOT computable from one run; not in analyzer scope
CONSTRUCT-FAIL                                    — computable when any of {invalidated≥10/96, dq≥20/96,
                                                    hop1 below floor, admissibility fail, conformance fail}
COMPONENT-ADMISSIBLE-UNDER-COMPETITION            — computable when ALL of (i)-(vi) PASS

All §10 single-run branches are computable. The cross-run FINAL classification is correctly
out of scope for the analyzer; it would be computed by a later cross-run aggregator under
its own pre-registration.
```

### 1.5 No hidden execution — **CONFIRMED**

CS verified each of the three surfaces:

```text
REVIEW (this memo + TL ACTION):
  The TL ACTION explicitly forbids: "No build changes. No analyzer creation yet
  unless separately authorized. No N=96 materialization. No prompt generation for
  execution. No model run. No floor-check run. ..."
  This memo is a review-only deliverable; it produces no code, no specs, no prompts.
  CONFIRMED no hidden execution in the review surface.

FILING (yesterday's commit 2972b8c + today's earlier turn):
  The filing was a byte-identical copy of v0.3 from inbox to path-a/in-review/.
  Filing memo at governance/2026-06-18_v3-floor-check-prereg-v0.3-filing/
  CS-FILING-MEMO-V3-FLOOR-CHECK-V0.3-2026-06-18.md was filing-and-routing only.
  CONFIRMED no hidden execution in the filing surface.

PREREG (v0.3 bytes):
  §14 verbatim: "This preregistration authorizes: No build changes. No N=96
  materialization. No prompt generation for execution. No model run.
  No compression. No Claim C. No Paper B. No certification claim. No capability
  claim. No mechanism claim."
  §13 "Required artifacts (CS must produce before any run)" is a *prerequisite*
  list, not an authorization to produce them. CS reads §13 as: "before any run
  can be authorized, these artifacts must exist." It does NOT authorize CS to
  start producing them; that needs a separate Manager/TL ACTION (F3).
  CONFIRMED no hidden execution in the prereg surface.

The three surfaces are consistent: nothing in this routing turn (filing, review,
or v0.3 bytes themselves) authorizes execution of any kind.
```

---

## 2. Summary of required edits

```text
F1  (PREREG EDIT) Replace "predeclared MAX DELTA" in §4 with an exact numeric
    tolerance. CS proposes MAX DELTA = 8 characters per item-set; SE / Manager
    to lock the value. Rationale recorded in §1.2 above.

F2  (PREREG EDIT) Name path-a/build/v3_prompt_realizer.py and
    path-a/build/v3_prompt_conformance_checker.py (and the neutral-token pool
    if separate from the realizer) with the same lockability discipline as the
    analyzer in §E1 — path + intent + I/O contract + "sha256 LOCKED AT APPROVAL."

F3  (ROUTING PREREQUISITE, NOT A PREREG DEFECT) TL/Manager must separately
    authorize CS to build the analyzer + realizer + prompt-level checker, in
    the same posture as TL/Manager ACTION 2026-06-17 ("Begin V3 Build Open
    Slots") authorized the construction-build effort. Without that ACTION, CS
    cannot produce the artifacts whose digests v0.3 requires locked. The
    artifacts must exist before TL approval is possible.
```

All three are achievable without altering the foreclose-all standard, V3 schema, build artifacts, locked Manager values, instrument bytes (`cb4b0b60…` / `1d761c3d…`), or any §9/§10 floor/threshold/branch wording. F1 and F2 are text edits to v0.3 (yielding a v0.4-of-the-floor-check-prereg, not the v0.4 of the constructibility prereg). F3 is a routing-step authorization, parallel to how the V3 build itself was authorized.

## 3. What this verdict means — and does not mean

```text
HOLD does NOT mean:
  - the prereg is poorly drafted (it's not; v0.3 substantively addresses E1–E5
    and improves the v0.2 intermediate substantially)
  - V3 is no longer the candidate vehicle (it remains the conforming candidate)
  - any boundary moved (no run is closer to authorized than yesterday)
  - the foreclose-all standard, V3 schema, instrument, locked values, or
    §9/§10 floor/threshold/branch logic need to change (they don't)

HOLD DOES mean:
  - one numeric tolerance and two named scripts are needed for v0.3 to be
    mechanically lockable
  - the three CS-deliverable artifacts (analyzer + realizer + checker) must
    exist and be SE-verified before TL approval can issue
  - those artifacts require a separate "Begin Floor-Check Tooling Build"
    ACTION (analogous to the V3 build ACTION) — CS does not produce them
    unilaterally
  - C5 claim-risk review proceeds in parallel; not gated on this CS verdict
```

## 4. Clean-fetch confirmation

Performed after the commit landed; `git fetch origin` immediately preceded the verification. Each file's local sha256 compared against `git cat-file -p origin/main:<path> | sha256sum`.

```text
commit                       641956cdc2bcbb34fe773b6a66e82ddf3c7754a5
push                         2f0f167..641956c  main -> main
origin/main HEAD             641956cdc2bcbb34fe773b6a66e82ddf3c7754a5
local       HEAD             641956cdc2bcbb34fe773b6a66e82ddf3c7754a5   (match)

per-file verification (origin/main bytes → local bytes):

MATCH  df82b34c4f96e085ea51b8e6e1a735849a39b108b321f79e30b9f20cffa19d5b
       path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.3.md
                   ↑ the artifact under review; bytes intact (no edits)
MATCH  b48c8b42bd87bd98047c50ef99a2d44448e1b7fc2210a7eb078e89b0bc11b8ba
       governance/2026-06-18_v3-floor-check-prereg-v0.3-filing/TL-ACTION-REVIEW-FILED-V0.3-2026-06-18.md
MATCH  0afa3cbcd746e55093dbb99334f9b388b9567f847c1a99c72221834a93d179e6
       governance/2026-06-18_v3-floor-check-prereg-v0.3-filing/CS-FEASIBILITY-RE-REVIEW-V0.3-2026-06-18.md
                   ↑ this file, immediately PRIOR to the §4 commit;
                     the §4 commit's own sha will be cross-verified on next sweep
```

All 3 listed artifacts reproduce byte-exact from the shared repository on a clean fetch. **CS feasibility re-review FILED.**

---

— CS Engineer, 2026-06-18 (clean-fetch appendix)

---

## Non-authorizations (carried forward)

```text
- build changes                       blocked (per TL ACTION this turn)
- analyzer creation                   blocked (per TL ACTION; separate ACTION required)
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
- candidate selection, threshold values, certification evaluation,
  multi-model, Fork A reactivation, public benchmark packaging,
  artifact mutation                   all carried per standing card

Protected surfaces:
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc...) +
  tagged manuscript blob (7d6706a3...): never moved.
- tier0-run/ directory: sealed; no new files.

V3 conformance to the foreclose-all standard ≠ V3 certification.
The floor check remains the empirical question and is not enabled
by this review. The Path A FP16 K=5 FAIL remains closed.
```

---

— CS Engineer, 2026-06-18
