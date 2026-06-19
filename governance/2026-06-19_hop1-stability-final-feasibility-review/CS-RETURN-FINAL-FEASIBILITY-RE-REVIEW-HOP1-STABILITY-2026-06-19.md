# CS RETURN — Final Feasibility Re-Review (Hop1 Stability Package) — PASS

**Date:** 2026-06-19
**From:** CS Engineer
**To:** Team Lead, Manager; Cc: Senior Engineer, C5
**Re:** TL ACTION 2026-06-19 — "Final Feasibility Re-Review — Hop1 Stability Tooling Verified"
**Status:** **PASS — executable and mechanically lockable as written.**

---

## Record status

```text
authority             TL ACTION 2026-06-19 ("Final Feasibility Re-Review —
                      Hop1 Stability Tooling Verified")
package under review  PREREGISTRATION-HOP1-STABILITY-PATH-A-v0.1 (sha 71f00482…)
                      + verified Hop1 Stability tooling bytes
                      (analyzer 31224f6f…, covariate logger b9532490…)
verdict               PASS — no edits required; package is executable and
                      mechanically lockable as written
follow-on             ready for TL approval consideration → Manager by-name
                      RUN authorization (separate action; not requested here)
```

---

## Required checks — 10 / 10 PASS

### 1. Seeds 193..768 are mechanically realizable via the approved wrapper/generator path. — PASS

```text
verification           materialized all 576 items via the locked wrapper
                       cc07e5a2 (which calls underlying generator 6a2ceee1)
                       during the tooling-build verification step

evidence               path-a/build/build_verification/hop1_stability/items_193_768/
                       ls | wc -l → 576   (exactly 6 × 96)
                       first → item_193.json,   last → item_768.json

provenance check       item_193.json _build_provenance.item_index = 193
                       item_768.json _build_provenance.item_index = 768
                       item indexing is contiguous; no gaps in 193..768

wrapper invariant      cc07e5a2 enforces ≤999 cap; 768 < 999 → invariant holds
```

### 2. Six fresh blocks of N=96 are executable: F1..F6 (193..768). — PASS

```text
block boundary indices verified PRESENT in the materialized set:

  F1: 193..288   item_193.json PRESENT   item_288.json PRESENT
  F2: 289..384   item_289.json PRESENT   item_384.json PRESENT
  F3: 385..480   item_385.json PRESENT   item_480.json PRESENT
  F4: 481..576   item_481.json PRESENT   item_576.json PRESENT
  F5: 577..672   item_577.json PRESENT   item_672.json PRESENT
  F6: 673..768   item_673.json PRESENT   item_768.json PRESENT

  total items:   576 = 6 × 96   (matches prereg §5 exactly)

  disjoint from used ranges 001..192: yes (193 > 192).

block-id mapping in BOTH tools (analyzer + logger) uses
  block_id_for_index(item_index, start_index=193, block_size=96, n_blocks=6)
which is the same pure-function over both tools (verified at sha
31224f6f line 70 + sha b9532490 line 68; identical logic).
```

### 3. The 3-digit token-width constraint holds for all fresh blocks. — PASS

```text
per-item prefix scheme   i{NNN}_{ROLE}   (e.g., i193_C1, i768_B1)
                         3-digit index → 5-char prefix (i + 3 digits + _)
                         role tokens stay 6 or 7 chars total

empirical probe at lower boundary  item_193:
  prefix "i193_"   C_star width 7   (i193_C1 = 7 chars)
empirical probe at upper boundary  item_768:
  prefix "i768_"   width per role token:
    C_star = i768_C1   (7)
    B      = i768_B1   (7)
    T      = i768_T0   (7)
    r1     = i768_r1   (7)
    r2     = i768_r2   (7)
  ALL role tokens 6 or 7 chars   → True

result                   token-width invariant identical to ranges 001..192
                         across all six fresh blocks.
```

### 4. MAX_DELTA=8 remains valid. — PASS

```text
MAX_DELTA derivation     V3 construction uses positional/role-token slots
                         whose widths are bounded by the per-item-prefix
                         scheme. The wrapper cc07e5a2 enforces item_index
                         ≤ 999, which keeps the index portion to ≤ 3 digits
                         and the prefix to ≤ 5 chars (i + 3 + _). Combined
                         with the 1- or 2-char role suffix, role tokens
                         stay 6–7 chars, which is the regime in which
                         MAX_DELTA=8 was originally established and
                         validated on the V3 floor-check + composite-gate
                         runs.

cap check                768 ≤ 999    invariant holds across all 6 blocks.

cross-reference          carried verbatim through floor-check (001..096) and
                         composite-gate (097..192) approvals; the seed
                         widening to 193..768 stays within the same regime
                         (768 < 999), so MAX_DELTA=8 continues to apply
                         without re-derivation.
```

### 5. The analyzer implements all six required features. — PASS

```text
checked against path-a/build/v3_hop1_stability_analyzer.py (sha 31224f6f…):

  per-block hop1 rate                    line 188   hop1_rate = hop1_k / n
  per-block hop1 Wilson 95% CI           line 178 + wilson_ci() at line 59
                                            (returns hop1_wilson_lower / upper
                                             at lines 189-190)
  per-block hop2 control rate            line 193   hop2_rate = hop2_k / n
  per-block hop2 Wilson 95% CI           line 179 + wilson_ci() at line 59
                                            (returns hop2_wilson_lower / upper
                                             at lines 194-195)
  per-block floor verdicts               lines 191, 196   hop1_clears_floor
                                                          hop2_clears_floor
                                                          (Wilson lower > 0.75)
                                         line 200          block_construct_ok
                                                          (admissibility + conformance
                                                           + invalidated < 10)
  rate distribution                      lines 226-239   spread block with
                                                          min, max, range, mean
  between-block spread / variance        lines 226-239   variance, stddev
  final §9 branch                        lines 214-223   N2-priority selector
                                                          → decision["final_branch"]
                                         documented in decision["branch_priority_order"]
                                                          (= BRANCH_PRIORITY constant)
```

### 6. The covariate logger implements only the declared positional/structural covariates. — PASS

```text
checked against path-a/build/v3_hop1_covariate_logger.py (sha b9532490…):

PRIMARY (prereg §6) — confirmatory:
  predicted_is_P_role_distractor          line 172-173 + per_item field
                                          (predicted ∈ {d.head for d in decoy_chains})

SECONDARY (prereg §6) — descriptive co-occurrence:
  seed/index block                        block_id_for_index (line 68)
                                          per_item.block_id
  target B token (identity, width)        per_item.target_B_token / target_B_width
  predicted token (identity, role class)  per_item.predicted / predicted_role_class
  relation token identity (r1)            per_item.r1_identity
  relation position                       per_item.relation_position = 0 (constant)
  fact-line position of target hop1       per_item.fact_line_position_target_hop1 = 0
  prompt character count                  per_item.prompt_hop1_char_count
                                          (from realization summary if available)
  token-width class                       per_item.target_B_width
  competitor/distractor role class        per_item.competitor_distractor_role_class
                                          of the predicted token
  (and per_item.predicted_role_class which mechanically classifies into
    {C_star, B, T, r1, r2, post_C_star_relation, X_i_competitor,
     B_i_competitor, P_decoy_head, Q_decoy_bridge, S_decoy_answer,
     T_i_decoy_terminal, head_competitor_relation, tail_competitor_relation,
     filler_verb, free_form})

FORBIDDEN labels                          NONE emitted. Confirmed by reading
                                          all field names + the explicit
                                          summary.forbidden_labels_used field
                                          (logger output declares: "none —
                                          mechanism / binding / attention /
                                          reasoning failure / shortcut all
                                          forbidden per prereg §6 and never
                                          emitted").

no scope creep                            no covariate beyond the §6 set is
                                          computed or emitted.
```

### 7. N1 is resolved (render-4-execute-2). — PASS

```text
N1 requirement (TL ACTION verbatim):
  "render four contexts, execute only hop1 and hop2. Unexecuted
   composite/direct_query contexts must not enter scoring, covariate
   logging, branch computation, or claims."

analyzer enforcement (structural):
  - ALLOWED_CONTEXTS = {"hop1", "hop2"}                  (line 55)
  - OUT_OF_SCOPE_CONTEXTS = {"composite", "direct_query"} (line 56)
  - _load_hop1_hop2_only(scored_dir) (line 84) ONLY reads
      <item>/hop1.json and <item>/hop2.json; composite/dq files
      are NOT opened even if present in the scored dir
  - every decision JSON's "n1A_enforcement" field documents this
    (line 245-247) — verifiable in the analyzer output

covariate logger enforcement (structural):
  - build_log() (line 125) reads ONLY hop1.json (the PRIMARY context
    for the covariate analysis); composite/dq are NEVER read
  - no flag or arg enables them

cross-tool consistency:
  - both tools use the same item-index → block-id mapping
  - both refuse out-of-scope contexts mechanically (not by convention)

result:
  composite/direct_query contexts cannot enter scoring, covariate
  logging, branch computation, or claims via these tools — confirmed
  by both code inspection AND smoke-test evidence (no smoke-test
  scored set contained composite/dq files; the tools never reference
  them).
```

### 8. N2 is resolved (branch priority CONSTRUCT-FAIL > HOP2-CONTROL-FAIL > stability branches). — PASS

```text
N2 requirement (TL ACTION verbatim):
  1. CONSTRUCT-FAIL
  2. HOP2-CONTROL-FAIL
  3. HOP1-STABLE-ADMISSIBLE / HOP1-STABLE-INADMISSIBLE / HOP1-UNSTABLE

analyzer implementation:
  BRANCH_PRIORITY constant (lines 45-51) declares the order explicitly
  and is documented in every decision JSON's "branch_priority_order"
  field (line 244).

  Branch selector (lines 214-223, verbatim):
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

empirical confirmation (from tooling-build smoke tests):
  test_d (hop1 all clear + hop2 fail on block 3)
    → HOP2-CONTROL-FAIL fires, correctly overriding STABLE-ADMISSIBLE
  test_e (hop1 + hop2 all clear + admissibility fail on block 2)
    → CONSTRUCT-FAIL fires, correctly overriding STABLE-ADMISSIBLE

both higher-priority branches override the lower hop1 verdict, as
required.
```

### 9. All digests needed for TL approval are available and stable. — PASS

```text
Prereg artifact:
  PREREGISTRATION-HOP1-STABILITY-PATH-A-v0.1.md         71f00482e1d94bd7fb06a5068391a7977a4b71d9baac690b286511d29e052c26

Prereg §12 — REUSED UNCHANGED (digests locked from prior approvals):
  v3_composite_gate_item_generator.py (wrapper)          cc07e5a2c49757e9171831af7944b5f7f8b1de235c7cb35cb18e48b06ce534a2
  v3_item_generator.py (underlying)                       6a2ceee15442ebbd1f6cc4bbbd14a76d1264af9904ad3e5d6062c1554f530c53
  v3_prompt_realizer.py                                   fb561fdc526115da94c6137b739e8bb3b6adf30825d83f864cda713bc0750909
  v3_prompt_conformance_checker.py                        b8afa3f89dd7f375058500820bdf2bf58a46384d2283c8f2a31f1b8c92ad2b82

Prereg §12 — NEW (to be locked at TL approval; SE-verified):
  v3_hop1_stability_analyzer.py                           31224f6fe7b66d303924a40fa9307f3aded05f8ba73d4952f518c8deecd69f0f
  v3_hop1_covariate_logger.py                             b9532490f49970396cd9a14d926393450ede2e6a17c5374b2ac69d115f39953f

Dependency artifacts (auditable; not §12-listed but stable):
  path-a/inspector/inspector.py                           cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
  path-a/inspector/constants.py                           1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd

stability:
  - all 4 §12 reused digests are UNCHANGED from the prior approvals
    (V3 floor-check + V3 composite-gate; carried byte-faithful)
  - both new digests have been SE-verified PASS as of this re-review
  - all digests are present on origin/main and reproduce on clean fetch
    (governance/2026-06-19_hop1-stability-tooling-build/CS-RETURN-...
     §10 confirms the new digests; prior CS returns confirm the §12
     reused digests)

ready-for-TL-approval set: 6 digests (4 reused-unchanged + 2 new).
```

### 10. No hidden run, materialization for execution, prompt execution, model execution, compression, or claim expansion occurred. — PASS

```text
no run                            confirmed — no model loaded, no
                                  inference performed during the tooling
                                  build; smoke-test scored sets are SYNTHETIC
no fresh materialization for execution
                                  confirmed — the 576 items at indices
                                  193..768 live under
                                  path-a/build/build_verification/hop1_stability/
                                  and are EXPLICITLY build-verification
                                  artifacts (their location and naming
                                  make this unambiguous); they are NOT
                                  run-prep. Any run-prep would go under
                                  a future experiments/<YYYY-MM-DD>_hop1-
                                  stability-run/ dir created only after
                                  Manager by-name authorization
no prompt execution               confirmed — no prompts rendered for
                                  this build (analyzer reads scored
                                  outputs, not prompts; covariate logger
                                  reads scored outputs + item specs)
no model execution                confirmed — neither tool imports any
                                  model framework (grep for transformers /
                                  torch / mlx / openai / anthropic / httpx /
                                  requests. / urllib / socket → zero matches)
no compression                    confirmed — no INT4, no INT8, no
                                  quantization tooling touched. Pre-existing
                                  untracked tier0-run/Qwen2.5-3B-Instruct-
                                  mlx-int{4,8}/tokenizer.json files appeared
                                  in working tree (NOT introduced by this
                                  work) and were NOT staged. tier0-run/
                                  remains sealed.
no claim expansion                confirmed — no Claim C, no Paper B, no
                                  certification claim, no capability claim,
                                  no mechanism claim, no composite-gate
                                  rerun, no Fork A reactivation, no public
                                  benchmark packaging, no Paper 6, no Paper
                                  3 execution as experiment; all standing
                                  non-authorizations honored. The seen
                                  097..192 composite-gate result is treated
                                  as an ANCHOR (§4) only and is not
                                  re-sliced as a fresh claim by this
                                  package.
```

---

## Verdict

```text
PASS — executable and mechanically lockable as written.

No edits required to either the prereg or the tooling. The package is
ready for TL approval consideration. Manager by-name RUN authorization
remains a separate action.
```

---

## Next route (per prereg §E and TL ACTION boundary)

```text
CS final feasibility re-review (THIS RETURN)
  → TL approval consideration
    → Manager by-name RUN authorization (separate action; not requested
       here; required before any fresh materialization or model execution)
        → CS execution (under Manager by-name authority only)
          → SE verification
```

---

## Standing non-authorizations (carried forward verbatim)

```text
- run                                       blocked
- fresh materialization for execution       blocked (build_verification
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
- tier0-run/ directory                      sealed; no new files added by CS

The Path A FP16 K=5 FAIL remains closed. V3 ≠ C0.
```

---

## §11. Clean-fetch confirmation

```text
verification procedure
  git clone --depth 1 https://github.com/eaflores805-Apiana/river-and-canyon clean
  cd clean
  git rev-parse HEAD
  shasum -a 256 governance/2026-06-19_hop1-stability-final-feasibility-review/TL-ACTION-CS-FINAL-FEASIBILITY-RE-REVIEW-HOP1-STABILITY-2026-06-19.md
  shasum -a 256 governance/2026-06-19_hop1-stability-final-feasibility-review/CS-RETURN-FINAL-FEASIBILITY-RE-REVIEW-HOP1-STABILITY-2026-06-19.md

results (clean-fetch from shared repo, 2026-06-19)
  remote HEAD                      5346f7fde6e71d71160310ca9a69220f3489037b   MATCH
  TL ACTION memo       sha256      3a52d6d521bede28bd347514b725087488986ea14fd1fc76ea5e5ba7946812e4   MATCH
  CS RETURN memo (pre-§11 append) sha256
                                   3bb6a160b70d4a3f4ffb540fff9dde68adc5037b4c7decb9fb64a0d71c97ead1   MATCH

verdict
  FILED. Both review-packet memos verify from the shared repo on clean
  fetch at HEAD 5346f7fde6e71d71160310ca9a69220f3489037b.

  The CS RETURN digest above is the pre-§11-append digest; this §11
  append + the §11-append commit will land in a follow-on commit whose
  digest is reported below.
```

---

— CS Engineer, 2026-06-19
