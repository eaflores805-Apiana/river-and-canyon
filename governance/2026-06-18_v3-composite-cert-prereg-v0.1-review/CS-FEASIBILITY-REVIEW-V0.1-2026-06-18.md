# CS FEASIBILITY REVIEW — V3 Composite-Certification Preregistration v0.1

**Date:** 2026-06-18
**From:** CS Engineer
**To:** Team Lead; Cc: Senior Engineer, C5, Manager
**Re:** TL ACTION 2026-06-18 — "Route V3 Composite-Certification Prereg v0.1 for Review"
**Status:** **HOLD — feasible with one required edit (E1: fresh-seed/materialization rule)**

---

## Record status

```text
artifact under review        path-a/in-review/PREREGISTRATION-V3-COMPOSITE-CERTIFICATION-v0.1.md
                              sha256 ee1ad41d7b1b7b025adda1afe469bad22c75a274b4c5b65e76d9cf266aebb32c
authority for review         TL ACTION 2026-06-18 ("Route V3 Composite-Certification
                              Prereg v0.1 for Review")
verdict                      HOLD — feasible with one required edit (E1)
edits required               E1  fresh-seed/materialization rule must specify HOW fresh
                                  items are generated; the existing generator currently
                                  cannot produce fresh items without an additive parameter
edits recommended (non-blocking)
                             A1  title-vs-§7-branch consistency (TL watchpoint A — recommend
                                  CS feasibility-side)
verdict scope                CS feasibility only. C5 claim-risk is a separate lane.
C5-lane items                B (wording "certifies composition") — CS notes feasibility
                              implications but defers verdict to C5
```

---

## 1. CS focus answers (the seven from TL ACTION)

### 1.1 Fresh-run materialization — **NOT EXECUTABLE AS WRITTEN** (E1)

The prereg §6 + §T say items will be re-generated "with FRESH seeds for the new N=96" while the generator is "REUSED UNCHANGED." This is internally inconsistent: the current generator's main() iterates `for n in range(1, args.count + 1)`, so calling `--count 96` again would produce **byte-identical** items to the floor-check (per-item prefix `i{N:03d}_` is keyed on the index 1..96).

CS-verified by grep of the current generator (sha `6a2ceee1…`):

```text
$ grep -E "add_argument|--start-index" path-a/build/v3_item_generator.py
    p.add_argument("--out-dir", type=Path, required=True, ...)
    p.add_argument("--count", type=int, default=8, ...)
    p.add_argument("--verbose", action="store_true", ...)
```

No `--start-index` (or equivalent) parameter. The generator currently has no way to produce items 97..192 (or any other fresh range) without modification.

**E1 — required edit.** The prereg must lock the fresh-item generation scheme explicitly. CS proposes three concrete options (the choice is Senior's; CS only flags that the rule must be made mechanical):

```text
OPTION A  Add `--start-index N` parameter to v3_item_generator.py
          (small additive change; doesn't alter existing real-run behavior
           at start-index 1; generator digest changes from 6a2ceee1... to
           a new value; prereg §T re-locks the new digest at approval).
          Then prereg locks: "fresh certification items generated with
          --start-index 97 --count 96, producing item_097..item_192."
          Per-item prefix scheme i{NNN}_ generalizes naturally to 097..192;
          no cross-set token collision possible by the existing prefix
          discipline (per v3_token_pool.md §3 disjointness proof).

OPTION B  Specify a DIFFERENT per-item prefix scheme for certification items
          (e.g., `c{NNN}_` for certification vs `i{NNN}_` for floor check).
          Requires a generator parameter `--prefix-char c` plus a small
          patch to the per-item prefix function. Same lockability discipline.

OPTION C  Wrap the existing generator with a small `v3_certification_item_
          generator.py` script that calls the existing `generate_item()`
          function directly with item_indices 97..192. The wrapper digest
          locks at approval; the underlying generator remains UNCHANGED
          (sha 6a2ceee1... unchanged). Most consistent with the "REUSED
          UNCHANGED" claim in §T, but adds a new lockable artifact.

ANY OF THE THREE works. CS does not recommend a specific option; Senior to lock
the choice and the prereg §T to record both:
  - the exact fresh-item index range / prefix scheme used
  - the (possibly updated) generator digest, or the new wrapper script's digest

Without E1 resolved, "fresh seeds" is wishful: the only mechanical effect of
`--count 96` on the unchanged generator is to regenerate items 1..96 byte-
identical to the floor-check, which would violate lock-before-look.
```

### 1.2 Reused tooling — **5/6 reusable unchanged; 1 needs E1 resolution**

```text
realizer         v3_prompt_realizer.py                fb561fdc...  REUSABLE — pure
                                                                    function of (spec, pool)
checker          v3_prompt_conformance_checker.py     b8afa3f8...  REUSABLE — pure
                                                                    function of (specs, prompts)
neutral pool     v3_neutral_token_pool.md             bc2020c2...  REUSABLE — fixed resource
inspector        path-a/inspector/inspector.py        cb4b0b60...  REUSABLE — schema-level
constants        path-a/inspector/constants.py        1d761c3d...  REUSABLE — locked values
generator        v3_item_generator.py                 6a2ceee1...  REUSABLE *iff E1 resolved*
                                                                   (currently cannot produce
                                                                    fresh items; see §1.1)
```

The realizer's per-item-prefix scheme (`i{N:03d}_`) generalizes naturally to N>96 by construction (token namespace `i\d{3}_\w+` is infinite), so the realizer and downstream tools require no changes. The conformance, inspector, constants, and pool are all index-agnostic.

### 1.3 New tooling — **FEASIBLE**

Both new tools are feasible as deterministic, model-free, pure-function CLI scripts following the existing `v3_floor_check_analyzer.py` template.

```text
v3_composite_certification_analyzer.py
  inputs   --scored-dir          (the FRESH N=96 scored outputs)
           --items-dir           (fresh item specs with ground truth)
           --r6-log              (R6 invalidation log, fresh set)
           --admissibility       (inspector summary, fresh set)
           --prompt-conformance  (checker summary, fresh set)
           --error-log           (from v3_composite_error_logger.py, see below)
           --output              (decision JSON path)
  outputs  composite k/n + rate + Wilson 95% CI;
           re-confirmed precondition status (hop2, hop1, dq, admissibility, conformance);
           gate conditions (a) lower Wilson > 0.75, (b) lower Wilson > 0.45;
           §7/§8 branch selector → one of
             GATE-CLEARED-THIS-RUN
             COMPOSITE-DOES-NOT-CERTIFY-THIS-RUN
                (sub-message if 0.45 < lower Wilson ≤ 0.75:
                 "not explained by foreclosed shortcuts, but not reliably composing")
             PRECONDITION-FAIL
             CONSTRUCT-FAIL  (incl. pathological error-structure flag)
  contract pure function of inputs; no clock, no RNG, no environment, no network;
           same inputs → byte-identical output JSON.
  digest   LOCKED AT APPROVAL.

v3_composite_error_logger.py
  inputs   --scored-dir, --items-dir
  outputs  error_structure_log.json with per-item:
             composite_match (bool); composite_predicted; ground_truth;
             error_class ∈ {correct, correct_chain_wrong_depth, decoy_chain_depth_2,
                             competitor_or_other_token};
             cooccurrence ∈ {inherited_component_failure, composition_specific, n/a};
           plus aggregate counts feeding the §5 pathological-structure check
           (success-not-correct-chain count + composition-specific failure count).
  contract pure function of inputs; no clock, no RNG.
  digest   LOCKED AT APPROVAL.
```

Both are reasonably-sized scripts (~150-250 lines each) following the patterns I already established for `v3_floor_check_analyzer.py` and `build_r6_log.py`. **FEASIBLE.**

### 1.4 Analyzer lockability — **CONTRACT IS CLEAR; DIGEST LOCKABLE**

Required inputs, outputs, digest locks, branch computation are all specified in §1.3 above and §7/§8 of the prereg. The branch logic is a deterministic 4-way switch on three predicates (preconditions_ok, gate_a, gate_b) plus the pathological-error-structure flag from the error logger.

Lockability conditions:
- Both new scripts must exist with SE-verified bytes before approval (same routing as the floor-check tooling F3 prerequisite — separate tooling-build action gated by TL/Manager).
- Each script's sha256 locked at TL/Manager approval, recorded into v0.2's §T binding block.
- Error logger digest is a dependency of the analyzer (analyzer reads error_log produced by logger), so both must be locked together.

**FEASIBLE.**

### 1.5 Error-structure logging — **MECHANICALLY COMPUTABLE**

All three error classes and the co-occurrence partition are deterministic functions of (scored outputs, item specs, ground truth):

```text
ERROR CLASSES (for any composite-error item N):
  correct_chain_wrong_depth     iff predicted ∈ {spec.target.B, spec.target.T}
                                (the bridge token or the target chain's terminal)
  decoy_chain_depth_2           iff predicted ∈ {d.answer for d in spec.decoy_chains}
                                (one of the 5 decoy answers S_i — right-depth, wrong-chain)
  competitor_or_other_token     otherwise
                                (X_i depth-2 competitors, B_i depth-1 competitors,
                                 decoy heads/bridges/terminals, or any free-form token)

CO-OCCURRENCE (for any composite-error item N):
  inherited_component_failure   iff scored[N]["hop2"].match == False
                                (the component itself failed on this item; composite
                                 failure inherited)
  composition_specific          iff scored[N]["hop2"].match == True
                                (the component works on this item but the chain doesn't
                                 — the composition-specific signature)

PATHOLOGICAL-ERROR-STRUCTURE FLAG (for the analyzer):
  pathological  iff among items where scored[N]["composite"].match == True, the
                predicted == C* is "coincidental" rather than "via the correct chain"
                — operationally, this would require an additional signal beyond exact
                string match. The single exact-string-match condition (predicted ==
                spec.target.C_star) already implies the correct chain's C* by design
                (decoy answers S_i and competitor X_i are distinct strings per the
                token-pool disjointness in v3_token_pool.md §3). So the pathological
                flag is mechanically computable as ALWAYS FALSE under the existing
                token-pool design — unless Senior intends a stricter check (e.g.,
                composite-success items where the SAME item's hop2 also failed,
                suggesting the C* emission was not via traversal).
```

CS recommendation (non-blocking note): the pathological check's operational definition would benefit from one more sentence in §5 of the prereg making it explicit that exact-string match against `spec.target.C_star` IS the "via the correct chain" check (mechanical), since decoy-answer and competitor tokens are namespace-disjoint by construction. Senior's call whether to add a cross-context coincidence check (item where composite.match=True but hop2.match=False) as an additional pathological flag — that's a different content question.

**FEASIBLE.**

### 1.6 Fresh preconditions — **MECHANICALLY RECOMPUTABLE on the fresh set**

All six §6 preconditions (hop1, hop2, dq, C1–C9, prompt-conformance, invalidators) are recomputed by tools that already exist and work on any item set:

```text
hop1, hop2, dq scored          from the fresh inference run's scored outputs
                               (analyzer reads, computes rate + Wilson)
C1–C9 admissibility            v3_conformance_runner.py on the fresh items (96 results)
prompt-realization conformance v3_prompt_conformance_checker.py on the fresh prompts
invalidators                   build_r6_log.py (existing) on the fresh scored outputs
dominance                      computed by v3_composite_certification_analyzer.py from
                               the off-target mass distribution
                               (DOMINANT_RATE_THRESHOLD = 0.25; same constant as the
                                floor-check, flagged not pass/fail per §6)
```

**FEASIBLE** — assuming E1 resolves the fresh-item generation question (§1.1) so there ARE fresh items to recompute against.

### 1.7 No hidden execution — **CONFIRMED**

```text
prereg §E verbatim:
  "This preregistration authorizes:
     No new run.  No rerun.  No fresh materialization yet.  No prompt generation
     for execution.  No model run.  No compression / INT8 / INT4.  No prompt
     edits.  No floor adjustment.  No tooling edit after data.
     No Claim C.  No Paper B.  No certification claim
     (certification only if the §7 gate clears on the fresh run).
     No capability claim.  No mechanism claim."

prereg §T verbatim:
  "NEW (named here; built under a SEPARATE TL/Manager tooling-build action;
   SE-verified; digest LOCKED AT APPROVAL): [two new tools]"

This routing turn (CS review + C5 review) is review-only. The tooling build,
materialization, prompts, model run, and compression are all explicitly NOT
authorized by this artifact — each requires a separately gated downstream action.
```

**CONFIRMED — no hidden execution.**

---

## 2. TL watchpoint answers (the four)

### A. Title — "composite certification" vs "V3 Composite Gate Preregistration"?

There's a real tension between the title and §7/§9: the title says "CERTIFICATION" but the §7 branch is `GATE-CLEARED-THIS-RUN` (explicitly NOT final certification per §9: "Whether FINAL certification requires replication is a Manager/standard decision"). The artifact's operational ceiling is gate-cleared-this-run; the title is one step stronger.

**CS recommendation (A1, non-blocking edit):** match the title to the §7 branch name:

```text
PREFERRED:  "PREREGISTRATION — V3 COMPOSITE GATE (Path A) v0.1"
ALTERNATE:  "PREREGISTRATION — V3 COMPOSITE CERTIFICATION GATE (Path A) v0.1"
            (keeps the "certification" wording but qualifies it as "gate")
ACCEPTABLE: keep "V3 COMPOSITE CERTIFICATION" if §9's
            "single cleared run = GATE-CLEARED-THIS-RUN, not FINAL certification"
            is restated in the title's subtitle line so the operational level
            is visible at the artifact's masthead.
```

Feasibility implication: minimal — wording change at the prereg layer doesn't affect tooling. The §7 analyzer branch name (`GATE-CLEARED-THIS-RUN`) is already the conservative wording at the code layer.

### B. "Certifies composition on V3" wording — acceptable bounded, or replace?

**This is primarily a C5-lane question; CS defers verdict.** From a feasibility standpoint, CS notes:
- The §9 wording is *"Even a CLEARED gate certifies COMPOSITION on V3, at K=5, with Qwen2.5-3B-Instruct (FP16, greedy) — and NOTHING beyond that."* The bounds are precise (construction + load + model + precision + decoding).
- The analyzer's branch label is `GATE-CLEARED-THIS-RUN` — no analyzer output literally says "certifies composition." So the wording question affects prose only, not any tool output.
- If C5 wants a tighter form (e.g., TL's proposed *"certifies the V3 composite baseline as behavior consistent with two-hop composition under foreclose-all controls"*), the edit is to §9 only and does not affect tooling.

**Feasibility-side: NO BLOCKER**, whatever C5 decides. C5 has primary jurisdiction.

### C. Fresh-run seed/materialization rule — precise enough, or needs exact seed ranges?

**NOT PRECISE ENOUGH.** This is the same concern as E1 (§1.1 above). CS feasibility requires:
- A specific fresh-item generation rule (which generator parameter / index range / prefix scheme — see E1 options A/B/C)
- That rule locked into the prereg before approval
- The generator's (possibly updated) digest re-locked at approval

Without an exact rule, the §6 "FRESH N=96" requirement cannot be mechanically enforced. **The prereg needs an exact seed range / prefix scheme / generator-parameter binding before TL approval can be safely issued.**

### D. One fresh run enough for "gate-cleared-this-run," final certification separate?

**YES — this is structurally correct as written.** The prereg §9 explicitly states:

```text
"A single cleared run = GATE-CLEARED-THIS-RUN. Whether FINAL certification
 requires replication is a Manager/standard decision. SE RECOMMENDS at least
 one confirmation run (or a pre-registered robustness condition) before
 'certified' is called FINAL — mirroring the program's discipline that
 substrate-infeasibility requires REPEATED failures."
```

This **mirrors** the §10/§11 discipline from the floor-check prereg:
- Substrate-infeasibility (negative): requires REPEATED admissible failures
- Composite certification (positive): SE recommends at least one CONFIRMATION run

Symmetric, defensible, and the operational ceiling of THIS prereg is correctly bounded at gate-cleared-this-run. FINAL certification is a downstream Manager/standard decision. Feasibility OK; no edit needed on this point.

---

## 3. Summary of required edits

```text
E1  (PREREG EDIT, BLOCKING) Lock the fresh-item generation scheme explicitly.
    Three concrete options sketched in §1.1 (A: --start-index param on the
    generator; B: different per-item prefix scheme; C: wrapper script). Senior
    picks one and the prereg §T records the chosen scheme + the (possibly
    updated) generator/wrapper digest. Without this, "fresh seeds" cannot be
    mechanically enforced and the §6 "FRESH N=96" requirement is wishful.

A1  (PREREG EDIT, NON-BLOCKING) Title-vs-§7-branch consistency — current title
    "COMPOSITE CERTIFICATION" is one step stronger than the §7 operational
    outcome "GATE-CLEARED-THIS-RUN." CS recommends matching the title to the
    operational branch (e.g., "V3 COMPOSITE GATE PREREGISTRATION") or adding
    a masthead subtitle preserving the gate-vs-final distinction. Wording
    change only; no tooling impact. Senior judgment.

B1  (DEFERRED TO C5 LANE) "Certifies composition on V3" wording — bounded
    correctly in §9 but the unbounded form ripples through the prereg's prose.
    C5's primary jurisdiction; CS notes the wording does NOT appear in any
    tool output (analyzer branch is `GATE-CLEARED-THIS-RUN`).
```

CS does NOT recommend FAIL — the prereg is well-structured, the lock-before-look discipline is correctly enforced, the floor-check composite is correctly barred from certification use, the gate threshold transparency is honest, the failure branches are MECE, and the forbidden-interpretations carry forward from v0.4 cleanly. E1 is a single concrete edit that makes the fresh-run requirement mechanical.

---

## 4. What this verdict does NOT mean

```text
Does NOT mean the prereg is poorly drafted — it is well-structured and
the lock-before-look framing is exemplary.

Does NOT bar the C5 claim-risk review from proceeding in parallel — C5 should
review the v0.1 bytes immediately; CS's E1 edit is mechanical and does not
affect the claim wording C5 evaluates.

Does NOT authorize anything operational — no run, no tooling build, no
materialization, no prompts for execution, no compression, no Claim C, no
Paper B, no certification, capability, or mechanism claims.

Does NOT block the V3 floor-check result (COMPONENT-ADMISSIBLE-UNDER-COMPETITION,
SE-confirmed) — that result stands as the precondition this prereg carries
forward, regardless of this verdict.

Does NOT reopen the K=5 FAIL — V3 ≠ C0; this prereg does not bear on it.
```

## 5. Clean-fetch confirmation

Performed after the commit landed; `git fetch origin` immediately preceded the verification. Each file's local sha256 compared against `git cat-file -p origin/main:<path> | sha256sum`.

```text
commit                       c7cb2f0dac8c740288c3d2e51a8eecb9bc65ca33
push                         441eff4..c7cb2f0  main -> main
origin/main HEAD             c7cb2f0dac8c740288c3d2e51a8eecb9bc65ca33
local       HEAD             c7cb2f0dac8c740288c3d2e51a8eecb9bc65ca33   (match)

per-file verification (origin/main bytes → local bytes):

MATCH  path-a/in-review/PREREGISTRATION-V3-COMPOSITE-CERTIFICATION-v0.1.md
       (ee1ad41d…; the artifact under review)
MATCH  path-a/in-review/V3-FLOOR-CHECK-RUN-SE-VERIFICATION-RETURN-v0.1.md
       (03d2ead8…; SE PASS on the floor-check run)
MATCH  path-a/in-review/V3-FLOOR-CHECK-TOOLING-VERIFICATION-SE-RETURN-v0.1.md
       (232270f1…; SE PASS on the floor-check tooling)
MATCH  governance/2026-06-18_v3-composite-cert-prereg-v0.1-review/TL-ACTION-ROUTE-V3-COMPOSITE-CERT-PREREG-V0.1-2026-06-18.md
MATCH  governance/2026-06-18_v3-composite-cert-prereg-v0.1-review/CS-FEASIBILITY-REVIEW-V0.1-2026-06-18.md
                                (this file, PRIOR to the §5 commit; the §5 commit's
                                 own sha will be cross-verified on the next sweep)
```

All 5 listed artifacts reproduce byte-exact from the shared repository on a clean fetch. **CS feasibility review FILED.**

---

— CS Engineer, 2026-06-18 (clean-fetch appendix)

---

## Non-authorizations (carried forward, per TL ACTION boundary)

```text
- new run / rerun                    blocked
- fresh materialization              blocked (this ACTION is review only)
- prompt generation for execution    blocked
- tooling creation                   blocked (the two new tools require a separate
                                              TL/Manager tooling-build action)
- compression / INT8 / INT4          blocked
- Claim C, Paper B                   blocked
- certification claim                blocked (until §7 gate clears on a fresh run)
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
