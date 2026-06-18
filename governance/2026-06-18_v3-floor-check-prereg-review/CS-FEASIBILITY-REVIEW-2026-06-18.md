# CS FEASIBILITY REVIEW — V3 Floor-Check Preregistration v0.1

**Date:** 2026-06-18
**From:** CS Engineer
**To:** Team Lead; Cc: Senior Engineer, Manager, C5
**Re:** TL ACTION 2026-06-18 — "Review V3 Floor-Check Preregistration v0.1"
**Status:** **HOLD — feasible with required edits**

---

## Record status

```text
artifact under review          path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-PATH-A-v0.1.md
                                sha256 ceaa2e674e43e7ec234b5fb914ffd195da1703cb8e7f70dae7d9c1f0e901f5dd
authority for review           TL ACTION 2026-06-18 ("Review V3 Floor-Check Preregistration v0.1")
verdict                        HOLD — feasible with required edits
edits required (5 total)       E1 scorer/analysis code naming; E2 direct-query ceiling rule;
                                E3 R6 invalidator scope; E4 hop1 floor CI treatment;
                                E5 length/format-matching metric
edits non-blocking (1)         N1 N=96 power note (optional)
verdict scope                  CS feasibility only. C5 claim-risk review is a separate lane.
boundaries respected           no build changes, no N=96 materialization, no prompts for
                                model execution, no model run, no compression, no Claim C,
                                no Paper B, no certification, capability, or mechanism claim.
                                Path A FP16 K=5 FAIL remains closed.
```

---

## 1. CS focus answers (the seven from TL ACTION)

### 1.1 Full N=96 materialization feasibility — **FEASIBLE**

The build generator (`v3_item_generator.py`, sha `6a2ceee1…`) already accepts `--count 96`. The per-item-prefix scheme (`i{N:03d}_`) guarantees cross-item token independence at any N; demonstrated determinism at N=8 holds at N=96 by construction (same code path, same per-N pure-function logic). Conformance at scale uses the same runner (`v3_conformance_runner.py`) pointed at the larger items dir. Estimated runtime is negligible (the 8-item run took well under a second).

The only realization step the build does not exercise is the N=96 run itself; that is gated on Manager by-name authorization per the prereg §14 routing, and is intentionally not in this build's scope.

### 1.2 Four-context prompt realization feasibility — **FEASIBLE BUT NEW BUILD ARTIFACT**

The prereg correctly states (§4): *"the generated items are schema-level construction specs, not prompts. Before any run, the specs must be realized into concrete prompts for the four contexts."* The build does **not** include a prompt-realization layer; one must be produced as a NEW build artifact before any run.

The layer is achievable:
- For each generated item, produce four prompt strings (composite / hop1 / hop2 / direct_query)
- Honor the schema-level guarantees: no leakage of B or C\* into hop1 or direct_query; no leakage of C\* into composite (it must be the answer, not pre-revealed); load-matched k=5 decoy chains in every context
- Length-matched (see §1.4 below for the metric concern)

**Required CS follow-on (separately gated):** `path-a/build/v3_prompt_realizer.py` + `path-a/build/v3_prompt_conformance_checker.py`, deterministic by `(item_index, context)` tuple. This is a build extension, not a defect of the prereg. The prereg already calls this out in §4 and §13. No HOLD on this point.

### 1.3 Prompt-level conformance checks — **FEASIBLE BUT NEW INSPECTOR**

The existing inspector (`path-a/inspector/inspector.py`, sha `cb4b0b60…`) is a *schema-level* gate (C1–C9 over JSON specs); it does not parse prompt strings. A separate **prompt-level inspector** must be written, with checks at least:

```text
P1  composite prompt does NOT contain C* token
P2  composite prompt DOES contain A and the four contexts' load-matched decoy chains
P3  hop1 prompt contains A and r1 but not r2, not B, not C*, not T, not T_i
P4  hop2 prompt contains B and r2 but not A, not C* (asks for C*, must not pre-supply)
P5  direct_query prompt contains A and the chain MINUS the B→C* fact, filler {W} holds {V} substituted
    with neutral tokens disjoint from the per-item role namespace; does NOT contain B or C*
P6  per-context length parity (see §1.4)
P7  per-context category-token completeness vs the spec (every entity declared in the spec appears
    where it should and only there)
```

This is achievable. The schema-level admissibility (C1–C9) on N=96 is a *precondition* of P-checks but not a *substitute* for them. **No HOLD on this point per se**, but the prereg should explicitly require the prompt-level inspector to be locked-and-named before run authorization (currently §13 says "prompt-level conformance checks" without naming the tool — see E1 below).

### 1.4 Length/format matching across composite / hop1 / hop2 / direct_query — **METRIC NOT SPECIFIED → HOLD edit E5**

The prereg §4 says prompts "must be length/format-matched across contexts" and the direct-query filler is "length-matched" (§5 of design v0.3 / prereg §13). It does not specify the matching metric: **character count, token count, byte count, line count, or some combination?**

These are different in practice. Character-matching of prompts is straightforward and template-enforceable; token-matching requires the model tokenizer (Qwen2.5 tokenizer) at realization time and is brittle to placeholder substitution. The prompt-realization layer needs to know which it must satisfy.

**E5 — required edit.** Specify the length-matching metric (e.g., "character count within ±2"; or "token count under the Qwen2.5 tokenizer, within ±1") and the tolerance, so the prompt-level conformance check has a target to lock against.

### 1.5 Real-run assertions — **FEASIBLE**

The inspector and constants under the v0.4 of-record re-pin (`cb4b0b60…` / `1d761c3d…`) already enforce real-run mode fail-closed (verified by fixture 10 PASS + the build's 8/8 PASS, every per-item inspection JSON has `validation.mode == "real-run"`). The prereg §13 requirement *"the run executes in REAL-RUN mode (no `_fixture_mode`, no `_sweep_mode`); the run record must assert this and the inspector must confirm it per item"* is enforced today by running the existing inspector against the N=96 specs — every per-item inspection JSON will carry the `mode == "real-run"` assertion, and any deviation will be a fail-closed REJECT before any model code is touched.

### 1.6 Artifact paths and hashes required before any run — **CONDITIONAL FEASIBLE**

Per §13 the required pre-run artifacts are: N=96 item specs (admissible C1–C9 real-run); four-context prompt realization; prompt-level conformance results; clean-fetchable sha256s for all of the above; real-run assertions in the run record.

All are producible. The conditional on FEASIBLE is that the locked paths must be **named in the prereg** so the lock binds against a fixed structure. Today §13 names *content categories*, not paths. Recommended (non-blocking):

```text
path-a/run-v3-floor-check/items/item_001..096.json
path-a/run-v3-floor-check/prompts/item_NNN/{composite,hop1,hop2,direct_query}.txt
path-a/run-v3-floor-check/conformance/inspector/item_NNN_inspection.json
path-a/run-v3-floor-check/conformance/prompt/item_NNN_prompt_inspection.json
path-a/run-v3-floor-check/manifest.json    (clean-fetch hashes of every file above)
```

If Senior locks specific paths in the prereg, CS can implement against fixed names; if Senior leaves paths up to CS, CS will commit a path-layout proposal at the time of N=96 materialization. Either works; explicit is better.

### 1.7 Scorer / analysis code explicitly named and lockable — **NOT NAMED → HOLD edit E1**

The prereg §7–§9 specifies the primary metric (hop2-isolated retrieval rate, Wilson 95% CI on the rate) and decision conditions, but **does not name a script path or sha for the scorer/analysis code that computes them.**

The G6 v0.3 evaluator (`7adf4eef…`, named in PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4 §"Corrected byte-binding block") is a *composite* scorer producing R1/R2/R3/R4/R4b/R5/R6cat. The hop2-isolated rate is a different metric: per-item correctness of one context's output (binary correct/not), aggregated to a rate, plus Wilson CI. This is a simpler computation, but it is a *different* artifact than G6 v0.3, and it does not exist in the repo yet.

**E1 — required edit.** The prereg must explicitly name:

```text
hop2_floor_analysis_script   path-a/analysis/v3_floor_check_analyzer.py (or equivalent)
                              with an SE-locked sha at approval, computing:
                                - per-item hop2 correctness from prompts/conformance outputs
                                - aggregated hop2-isolated rate
                                - Wilson 95% CI (lower bound for hop2 + hop1; upper bound for dq)
                                - per-context per-item correctness for hop1, direct_query
                                - dominance check (R4b-dominant-grab > 0.25 threshold)
                                - construct-fail flag if any §10 construct-fail condition fires
                                - "computed once" property: the script accepts artifact paths,
                                  emits a single decision JSON, no internal state retained
```

Without this, "computed once from the artifacts" (TL specific question) is not byte-bindable. CS can write the script; Senior must verify it and lock the sha at approval; that pairs the analysis-code lock with the floor/threshold lock.

---

## 2. Decision rule "computed exactly once from artifacts" — **CONDITIONAL on E1 + E2 + E3 + E4**

Per §9, the decision rule requires five conditions (i)–(v). With the current prereg text:

```text
(i)   hop2 lower Wilson > 0.75            — computable; arithmetic clear (see §3.1)
(ii)  direct_query at/below 0.20          — RULE NOT MECE; see §3.2 (E2)
(iii) hop1 clears 0.75                    — CI rule for hop1 not explicit; see E4
(iv)  no R6 invalidator at set level      — set-level vs item-level rule contradictory; see §3.3 (E3)
(v)   C1–C9 admissibility on all N=96     — computable via existing inspector
```

With E1 + E2 + E3 + E4 applied, **yes**, the decision rule is a deterministic function of {N=96 spec hashes, prompt hashes, per-context inspection JSONs, model output bytes (which the prereg does not authorize this turn), and the locked analyzer sha}. Without those edits, two of the five conditions are not mechanically decidable.

---

## 3. Watchpoint answers (the three from TL ACTION)

### 3.1 Watchpoint 1 — Wilson lower bound > 0.75 strictness — **INTENTIONAL; document the minimum-count threshold**

CS-recomputed Wilson lower bounds at N=96:

```text
observed   Wilson lower (95%)      clears 0.75 ?
78/96       0.7230                  fails
79/96       0.7346                  fails
80/96       0.7463                  fails
81/96       0.7581                  CLEARS (the minimum integer count)
82/96       0.7700                  clears
83/96       0.7820                  clears
84/96       0.7941                  clears
```

The minimum point-estimate that clears the strict Wilson lower bound > 0.75 at N=96 is **81/96 = 0.8438**. Below that, the construct does not clear; at 84/96 = 0.875 the lower bound is 0.794 (comfortable margin).

The prereg §6 explicitly grounds the 0.75 floor in *direct comparability with the C0 scout, which used the same hop2 floor* — the C0 scout's hop2-isolated cleared at K=1 (76/96 = 0.792) and was sub-floor at K≥2 (best 0.740 at K=3). The 0.75 threshold is calibrated to be the same number that C0's hop2 cleared at trivial load and failed at every non-trivial K. **CS confirms the strictness is intentional; this is the point of the comparability.**

**Recommended (not required):** the prereg should record the **minimum integer count (81/96)** explicitly so the lock binds against an integer rule rather than a Wilson-half-width arithmetic that could drift if a different CI implementation is later substituted. Without it, the rule is correct in *principle* but bound only by reviewer recomputation; with it, the rule is mechanical. Filing this as a non-blocking note, **N1**.

### 3.2 Watchpoint 2 — direct-query ceiling 0.20: exact N=96 count rule needed — **HOLD edit E2**

The prereg §6 / §10 says "direct_query retrieval of C\* must be AT OR BELOW 0.20" (point-style language). §9 says "direct_query at/below the 0.20 ceiling (no direct-recall shortcut)" — also point-style. But the hop2/hop1 floors use the **Wilson lower bound**, so there is an asymmetry: hop2 uses an interval rule, direct_query uses what reads as a point rule.

The three possible interpretations at N=96:

```text
INTERPRETATION                                                          max integer count
A) point estimate ≤ 0.20                                                 19/96 (0.198 ≤ 0.20)
B) Wilson upper bound ≤ 0.20                                             11/96 (W_upper 0.196)
C) Wilson lower bound ≤ 0.20                                             many more (loose)
```

Wilson computation, this turn, for context:

```text
15/96 = 0.156    W_upper = 0.242      W_lower = 0.097
19/96 = 0.198    W_upper = 0.289      W_lower = 0.130
20/96 = 0.208    W_upper = 0.300      W_lower = 0.137
```

Each interpretation makes a *materially different* construct-pass rule, so this is not a clarification CS can make. **Senior must pick.** Reading the prereg as written (point-style language symmetric to the floor's natural reading: "at/below floor" with no CI qualifier), interpretation A is the literal read; CS recommends that one for clarity and because point-estimate rules are robust to CI-method changes, but Senior to lock the choice.

**E2 — required edit.** State the rule unambiguously. CS proposes: *"direct_query retrieval of C\* must be ≤ 0.20 over N=96 items, i.e., at most 19 of the 96 items return C\* under the direct-query (bridge-withheld) context."* Or: *"upper Wilson 95% CI bound on direct_query rate ≤ 0.20."* Either is fine; the prereg should not be silent on the choice.

### 3.3 Watchpoint 3 — R6 invalidator scope: item-level vs set-level — **HOLD edit E3**

Two strands in the prereg sit in tension:

- §8: *"R6 invalidators: terminal-coincidence, controls-unavailable, direct-recall, interior-position, constant-token, below-floor. ANY firing invalidates the construct for that item."*
- §9 (iv): *"no R6 invalidator fires at the set level"*

The literal read together is: **any single R6 firing on any single item → that item is excluded → and §9(iv) fails → construct-fail per §10.** That is a very tight rule — at N=96 it requires zero R6 firings, with no tolerance for stochastic edge cases (e.g., a single item where the model returns a constant unrelated token across the four contexts triggering R6e).

There are at least three plausible rules; the prereg must lock one:

```text
RULE Q (strict; current literal reading):
  Any single R6 invalidator on any item → construct-fail.
  Tolerance: 0/96. Item-level invalidation cascades to set-level.

RULE R (item-level exclusion, set-level threshold):
  Item-level R6 firing → that item excluded from the analysis denominator.
  Set-level fail if more than X items invalidated (X to be locked; e.g., X=2).
  N=96 → at most X items can have any R6 firing; the analysis runs on N − (invalidated items).

RULE S (split — some R6s are item-level, some are set-level):
  R6a (terminal-coincidence) and R6f (below-floor) are construct-level diagnostics → set fail.
  R6b–e are item-level exclusions → drop the item; set fails only if count > X.
  Closer to how the existing G6 evaluator semantics tend to treat invalidators.
```

The prereg does not pick one. **CS cannot infer; Senior must specify.**

**E3 — required edit.** Pick Rule Q, R, S, or another, and write it explicitly into §8 and §9(iv) so the analyzer can implement it. CS notes that Rule Q is the most defensible for the substrate-infeasibility claim (a single R6 firing is a real signal that something is off; one wants to know about it, not paper over it), and Rule R has the strongest empirical robustness; CS does not recommend Rule S without Senior tying each R6 to a side.

### 3.4 Additional related edit — **E4: hop1 floor CI treatment**

Implicit, not flagged by the TL but surfaced by CS's reading.

The prereg §6 declares "hop1 floor = 0.75 and hop2 floor = 0.75" with parallel construction, and §9(iii) says "hop1-isolated clears the 0.75 floor". The hop2 condition is explicitly stated as Wilson lower bound > 0.75 (i, §9 + the rest of §6). The hop1 condition just says "clears" without specifying the CI rule.

CS reads symmetric Wilson lower-bound > 0.75 as Senior's likely intent (parallel to hop2). **E4 — required edit.** State hop1's clearance rule explicitly: *"hop1-isolated lower Wilson 95% CI bound > 0.75 (parallel to hop2 §7)."* Without this, hop1 is decidable in principle but not as a locked rule.

---

## 4. Summary of required edits

```text
E1  Name the scorer/analysis script (path + intent + locked sha at approval).
E2  Convert direct-query ceiling 0.20 to an unambiguous N=96 rule (count or CI).
E3  Pick a single R6 invalidator scope rule (item-level vs set-level vs split).
E4  State hop1 floor CI treatment explicitly (parallel to hop2).
E5  Specify the length-matching metric for the four-context prompts (char/token, tolerance).

N1  (Non-blocking) Document the minimum integer count for hop2 clearance at N=96
     (Wilson lower > 0.75 → min 81/96), so the rule is mechanical in addition to principled.
```

All five required edits are content/wording, not structural. None touch the foreclose-all standard, the V3 schema, the build artifacts, the locked Manager values, or the inspector/constants. The 5 edits are local additions or disambiguations within the prereg text. Senior should re-issue as v0.2 with these resolved; CS will re-review.

## 5. What this verdict means — and does NOT mean

```text
HOLD does NOT mean:
  - the floor check is wrong-headed (it isn't; it's the correctly-ordered next step)
  - V3 is no longer the candidate vehicle (it remains the conforming candidate)
  - the build is now insufficient (the build PASSED Senior verification independently
    and is unchanged by this review)
  - any boundary moves (no run is closer to authorized than it was yesterday)

HOLD DOES mean:
  - the prereg is not yet mechanically lockable. Five specific text-level edits are
    required (E1–E5) before SE re-issues, TL approves, and Manager by-name authorization
    can be issued. The edits are content-tightening only.
  - the routing pauses one step at SE; the chain SE-draft → CS-feasibility → C5-claim-risk
    → TL-approve → Manager-by-name → CS-execute → SE-verify is intact, the current
    step is "CS feasibility returned HOLD."
```

## 6. Clean-fetch confirmation

To be appended after the commit lands and `git fetch origin` is run.

---

## Non-authorizations (carried forward)

```text
- model run / floor-check run                  blocked (Manager by-name; not in this routing step)
- build changes                                blocked (this ACTION is review-only)
- full N=96 materialization                    blocked (this ACTION is review-only)
- prompt generation for model execution        blocked
- compression / Claim C / Paper B              blocked program-wide
- certification claim / capability claim       blocked
- mechanism claim                              blocked
- candidate selection, threshold values,
  certification evaluation, multi-model,
  Fork A reactivation, public benchmark
  packaging, artifact mutation                 all carried per standing card
- Paper 2 v1.0 tag + tagged manuscript blob    never moved
- tier0-run/ directory                         sealed; no new files

V3 conformance to the foreclose-all standard ≠ V3 certification. The floor check
remains the empirical question and is not enabled by this routing step. The
Path A FP16 K=5 FAIL remains closed.
```

---

— CS Engineer, 2026-06-18
