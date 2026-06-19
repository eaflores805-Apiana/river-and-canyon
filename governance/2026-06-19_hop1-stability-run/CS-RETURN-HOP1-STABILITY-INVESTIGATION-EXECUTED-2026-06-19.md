# CS RETURN — Hop1 Stability Investigation EXECUTED

**Date:** 2026-06-19
**From:** CS Engineer
**To:** Manager; Cc: Team Lead, Senior Engineer, C5
**Re:** Manager by-name authorization 2026-06-19 — "Execute Hop1 Stability Investigation"
**Status:** **EXECUTED. Final branch: HOP1-STABLE-INADMISSIBLE.**

---

## Headline

```text
Final branch (per analyzer + N2 priority):  HOP1-STABLE-INADMISSIBLE

  All 6 fresh blocks F1..F6 (seeds 193..768; N=96 each; 576 total fresh items)
  fail the hop1 isolated lower-Wilson > 0.75 admissibility floor.

  hop2 control:        ALL 6 blocks clear (96/96 per block; lower Wilson 0.9615).
  C1-C9 admissibility: 576/576 PASS  (all_pass=True per block)
  prompt conformance:  576/576 PASS  (all_pass=True per block)
  invalidated count:   0 per block (threshold 10/96 not approached)

  → No CONSTRUCT-FAIL, no HOP2-CONTROL-FAIL. The hop1 stability question is
    cleanly answered on the fresh blocks.

PRIMARY covariate (predeclared §6 confirmatory hypothesis):
  predicted_is_P_role_distractor co-occurrence among wrong hop1 predictions:
  352 / 352 = 1.0000   (100% of wrong hop1 predictions landed on a "P" role
                        distractor — r1-SUBJECT of a relation-reusing
                        distractor chain.)
  The hypothesis suggested by the seen 097..192 anchor REPRODUCES UNANIMOUSLY
  on the FRESH blocks. Reported as descriptive co-occurrence per prereg §6;
  NOT a mechanism, binding, attention, or reasoning-failure claim (§11).
```

---

## Record status

```text
authority              Manager by-name authorization 2026-06-19
                       ("Execute Hop1 Stability Investigation")
package executed       PREREGISTRATION-HOP1-STABILITY-PATH-A-v0.1
                         (sha 71f00482e1d94bd7fb06a5068391a7977a4b71d9baac690b286511d29e052c26)
locked tooling         v3_hop1_stability_analyzer.py    31224f6f…  UNCHANGED
                       v3_hop1_covariate_logger.py      b9532490…  UNCHANGED
reused-tooling lock    wrapper cc07e5a2, generator 6a2ceee1, realizer
                       fb561fdc, conformance checker b8afa3f8, inspector
                       cb4b0b60, constants 1d761c3d — ALL UNCHANGED post-run
inference profile      FP16, greedy, Qwen2.5-3B-Instruct rev aa8e7253
                       1152 calls (576 items × 2 contexts)
                       912s inference time + 6s model load
N1.A discipline        rendered 4 contexts, executed ONLY hop1 + hop2;
                       analyzer + covariate logger structurally refuse
                       composite + dq even if present
N2 priority            CONSTRUCT-FAIL > HOP2-CONTROL-FAIL > stability branches;
                       documented in decision.json's branch_priority_order field
anchors                001..096 (87/96) and 097..192 (28/96) NOT entered into
                       the fresh stability branch decision — contextual only
```

---

## Per-block hop1 + hop2 rates and Wilson 95% CIs + floor verdicts

```text
block  range        hop1 k/n     hop1 rate   hop1 Wilson 95% CI     hop1 clears 0.75?   hop2 k/n     hop2 rate   hop2 Wilson 95% CI     hop2 clears 0.75?
F1     193..288     50/96        0.5208      [0.4220, 0.6180]       FAIL                96/96        1.0000      [0.9615, 1.0000]       CLEAR
F2     289..384     23/96        0.2396      [0.1653, 0.3339]       FAIL                96/96        1.0000      [0.9615, 1.0000]       CLEAR
F3     385..480     35/96        0.3646      [0.2752, 0.4643]       FAIL                96/96        1.0000      [0.9615, 1.0000]       CLEAR
F4     481..576     39/96        0.4062      [0.3135, 0.5063]       FAIL                96/96        1.0000      [0.9615, 1.0000]       CLEAR
F5     577..672     54/96        0.5625      [0.4628, 0.6574]       FAIL                96/96        1.0000      [0.9615, 1.0000]       CLEAR
F6     673..768     23/96        0.2396      [0.1653, 0.3339]       FAIL                96/96        1.0000      [0.9615, 1.0000]       CLEAR
```

```text
hop1 between-block spread:
  min                                  0.2396 (F2, F6)
  max                                  0.5625 (F5)
  range                                0.3229     (32.3 pp)
  mean                                 0.3889
  variance                             0.0155
  stddev                               0.1245     (12.5 pp)

hop2 between-block spread:
  uniform 96/96 across all 6 blocks    (no variation; control behaved as
                                        the prereg expected — both anchors
                                        cleared 96/96 as well)

hop1 stability map (anchors + fresh, descriptive):
  001..096   anchor   87/96 = 0.9062   (seen; cleared 0.75)
  097..192   anchor   28/96 = 0.2917   (seen; FAILED 0.75)
  F1..F6     fresh    rates above; 0/6 clear 0.75
  → final branch HOP1-STABLE-INADMISSIBLE on the FRESH blocks; the seen
    001..096 clearing now looks anomalous relative to the fresh map of 6 blocks
    that ALL fail, while the seen 097..192 failure aligns with the fresh map.
    (Reported per prereg §9 verbatim: "STABLE-INADMISSIBLE: all 6 fresh blocks
     FAIL the 0.75 floor → hop1 is consistently NOT admissible, and the seen
     001..096 clearing looks anomalous relative to the fresh map.")
```

## Final branch and N2-priority computation

```text
construct_fail_blocks                 []      (admissibility 576/576 pass;
                                                conformance 576/576 pass;
                                                invalidated 0/block — well
                                                below the 10/block threshold)
hop2_control_fail_blocks              []      (all 6 blocks clear hop2 floor)
hop1_clear_blocks                     []      (no fresh block clears hop1
                                                Wilson lower > 0.75)
hop1_fail_blocks                      [1, 2, 3, 4, 5, 6]
                                              (all 6 blocks fail hop1 floor)

→ N2-priority selector lands on:    HOP1-STABLE-INADMISSIBLE
  (§9 verbatim: "all 6 fresh blocks FAIL the 0.75 floor →
   hop1 is consistently NOT admissible (and the seen 001..096
   clearing looks anomalous relative to the fresh map)")
```

## P-role co-occurrence result (PRIMARY covariate, prereg §6)

```text
n_hop1_match                                    224 / 576
n_hop1_wrong                                    352 / 576
predicted_is_P_role_distractor (total)         352 / 576   (61.1% of all items)
predicted_is_P_role_distractor among WRONG     352 / 352   = 1.0000 (100%)

interpretation (per prereg §6 + §11 verbatim):
  - The confirmatory hypothesis from the seen 097..192 result (wrong hop1
    predictions landing on the "P" role token — the r1-SUBJECT of a
    relation-reusing distractor chain — rather than the correct r1-OBJECT B)
    REPRODUCES UNANIMOUSLY on the fresh blocks.
  - This is reported as POSITIONAL CO-OCCURRENCE per §6, never cause; the
    forbidden mechanism / binding / attention / reasoning-failure / shortcut
    labels are NOT used.
```

## Exploratory covariate summary (SECONDARY, prereg §6 — descriptive only)

```text
predicted_role_class distribution (across all 576 items):
  P_decoy_head:                                352   (61.1% — all wrong predictions)
  B:                                           224   (38.9% — all correct predictions)

predicted_role_class among WRONG predictions:
  P_decoy_head:                                352  / 352  (100% of wrongs)
  (no other role class observed among wrong predictions)

target_B_width_distribution:
  width 7                                      576 / 576  (uniform; consistent
                                                with the i{NNN}_X scheme on
                                                3-digit indices — every target
                                                B token is i{NNN}_B1, width 7)

relation_position                              0 (constant; r1 at slot 0 — no
                                                positional variation present)
fact_line_position_target_hop1                 0 (constant; target hop1 triple at
                                                position 0 — no positional
                                                variation present)
prompt_hop1_char_count                         logged per item from
                                                realization_summary.json (576
                                                values); descriptive only

EXPLORATORY NOTE (per §10 stop rule):
  - The PRIMARY P-role read is the confirmatory finding (100% reproduction
    on fresh blocks).
  - All SECONDARY covariates are DESCRIPTIVE distributions only; they are NOT
    confirmatory findings, and no causal claim follows from their distributions.
  - No post-hoc covariate fishing has been performed: only the predeclared §6
    set was logged; no new covariate is computed or reported here beyond §6.
```

---

## Artifact inventory (paths + key digests)

### Run-level summaries

```text
realization_summary.json                      sha 4ec37a6ab97230d67f62a2d9d2863c2e27eeb83bba5ab53b4e0af62d22ba5e5a
admissibility_summary.json                    sha 3763f736ff2dae8e2a90908a3787446d3e95c300062d02199107b6ebd85857e9
prompt_conformance_summary.json               sha b361b1d7b8bda061ad456dad0fe3cc82a81440277669f0fe651695ec0af92758
run_record.json                               sha 11756a53a9158e8687faab1da1a05d89cf77db7a74403e7d34b7a95d4c5e6702
covariate_log.json                            sha 480f70d18f908a4dd89c8f5435cc122b61cfbf68e8fa006478fcfb8949049950
decision.json                                 sha 8676530a97e4322f38cf8ded17710db32883c16a5b1b431e9af284dd9b4f8965
manifest.json                                 sha 2ad2015c5edc9d8c8a654a7f5b360d8c8b98983b3f85e4558ea29976bfc4a1bb

all paths under experiments/2026-06-19_hop1-stability-run/
```

### Auxiliary scripts (consumed unchanged after data)

```text
run_step_5.py        (hop1+hop2-only inference runner)        sha 4a61a92514bcd139f2d0ccd7c7e39e5d4183d730dcc550a23e4a2097e13716f0
run_step_5.log       (inference progress log)                  sha 12bf3a3d2b917210a770aad453ce2f76ef79a75822bf1cbe529080a0834ef4ba
build_manifest.py    (read-only inventory script)              sha 0d6bd8541b9b6bb7152b555a97fddb9b14ba83f0f68b06773769c385ea0badb9
```

### Bulk-artifact directory rollup hashes

Sha256 of the concatenation of (relative_path \0 file_bytes \0) for every file
in each subtree, sorted by relative path — a single byte-stable handle per
subtree, suitable for cross-engineer reproduction checks:

```text
items_193_768/       files=576   rollup_sha256=3d1ecdf0ba3d095780e3c0eaaf416dfb58417a89623fff91c9b46bff9ebc5fe8
prompts/             files=2304  rollup_sha256=b0c2b07ff54ae85f0d66fef22f81aaa373aa7205c07ebdd6f4ce74bd56c16eaa
admissibility/       files=576   rollup_sha256=c6b95e71402b3b9c6d4a1d6fded02ffb748e2fd053248f1fe43601bc5560ae34
scored/              files=2304  rollup_sha256=af7411c72c0e7a43e7d038d9172d6eac27e9d6a3ffd00867adc3f1f585797e10
```

The per-file sha256 inventory for these subtrees is in `manifest.json`
(items, prompts, admissibility, scored arrays).

### Locked tooling digests (UNCHANGED before, during, after the run)

```text
path-a/build/v3_hop1_stability_analyzer.py            sha 31224f6fe7b66d303924a40fa9307f3aded05f8ba73d4952f518c8deecd69f0f
path-a/build/v3_hop1_covariate_logger.py              sha b9532490f49970396cd9a14d926393450ede2e6a17c5374b2ac69d115f39953f

path-a/build/v3_composite_gate_item_generator.py      sha cc07e5a2c49757e9171831af7944b5f7f8b1de235c7cb35cb18e48b06ce534a2
path-a/build/v3_item_generator.py                     sha 6a2ceee15442ebbd1f6cc4bbbd14a76d1264af9904ad3e5d6062c1554f530c53
path-a/build/v3_prompt_realizer.py                    sha fb561fdc526115da94c6137b739e8bb3b6adf30825d83f864cda713bc0750909
path-a/build/v3_prompt_conformance_checker.py         sha b8afa3f89dd7f375058500820bdf2bf58a46384d2283c8f2a31f1b8c92ad2b82
path-a/inspector/inspector.py                         sha cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
path-a/inspector/constants.py                         sha 1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
```

---

## Boundaries held at filing (verbatim from Manager memo + standing card)

```text
- no composite-gate retry                                              held
- no compression / INT8 / INT4                                         held
- no Claim C, Paper B                                                  held
- no certification claim, capability claim, mechanism claim            held
- no rerun until a preferred branch appears                            held
- no post-hoc covariate fishing (only §6 set logged)                   held
- no prompt edits after execution                                      held
- no tooling edits after data (all 8 digests UNCHANGED post-run)       held
- N1.A: composite + dq RENDERED but NEVER executed by run_step_5      held
- anchors 001..096 / 097..192 NOT entered into branch decision         held
- tier0-run/ sealed; no new files added by CS                          held (the
  two pre-existing untracked tokenizer.json files in tier0-run/ remain
  unstaged; CS Engineer adds nothing to tier0-run/)
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc…) untouched       held
- Path A FP16 K=5 FAIL                                                 stays closed
- V3 ≠ C0                                                              not equated
```

## Interpretation boundary (carried verbatim from Manager memo)

```text
This run reports ONLY:
  cross-block hop1 materialization-admissibility

It does NOT report:
  model stability, general hop1 capability, mechanism, binding failure,
  attention failure, reasoning failure, shortcut claim, composite-gate
  result, certification, compression readiness, Claim C, Paper B.

The P-role covariate result (100% reproduction on the fresh blocks) is
positional CO-OCCURRENCE per prereg §6, never cause.
```

---

## Commit + final remote HEAD + clean-fetch confirmation

```text
run commit                  2c20e960bf9b68393810f9ba269ca28710f0aac5
final remote HEAD           2c20e960bf9b68393810f9ba269ca28710f0aac5
                            (origin/main, github.com/eaflores805-Apiana/
                             river-and-canyon; 5,770 files staged including
                             576 items + 2,304 prompts + 576 admissibility
                             + 2,304 scored + 10 summary/script files +
                             2 governance memos; previous HEAD 85eb76c
                             fast-forward)

clean-fetch verification (from a fresh `git clone --depth 1` of the
shared repo at HEAD 2c20e960…):

  decision.json                       8676530a97e4322f38cf8ded17710db32883c16a5b1b431e9af284dd9b4f8965   MATCH
  covariate_log.json                  480f70d18f908a4dd89c8f5435cc122b61cfbf68e8fa006478fcfb8949049950   MATCH
  run_record.json                     11756a53a9158e8687faab1da1a05d89cf77db7a74403e7d34b7a95d4c5e6702   MATCH
  manifest.json                       2ad2015c5edc9d8c8a654a7f5b360d8c8b98983b3f85e4558ea29976bfc4a1bb   MATCH
  realization_summary.json            4ec37a6ab97230d67f62a2d9d2863c2e27eeb83bba5ab53b4e0af62d22ba5e5a   MATCH
  admissibility_summary.json          3763f736ff2dae8e2a90908a3787446d3e95c300062d02199107b6ebd85857e9   MATCH
  prompt_conformance_summary.json     b361b1d7b8bda061ad456dad0fe3cc82a81440277669f0fe651695ec0af92758   MATCH

  v3_hop1_stability_analyzer.py       31224f6fe7b66d303924a40fa9307f3aded05f8ba73d4952f518c8deecd69f0f   UNCHANGED
  v3_hop1_covariate_logger.py         b9532490f49970396cd9a14d926393450ede2e6a17c5374b2ac69d115f39953f   UNCHANGED

  items_193_768/                      576 files     PRESENT (count MATCH)
  prompts/   (*.txt)                  2,304 files   PRESENT (count MATCH; 4 × 576)
  admissibility/                      576 files     PRESENT (count MATCH)
  scored/    (hop[12].json)           1,152 files   PRESENT (count MATCH; 2 × 576)

  governance/2026-06-19_hop1-stability-run/
    MANAGER-BY-NAME-AUTHORIZATION-EXECUTE-HOP1-STABILITY-INVESTIGATION-2026-06-19.md   PRESENT
    CS-RETURN-HOP1-STABILITY-INVESTIGATION-EXECUTED-2026-06-19.md                      PRESENT
                                                                                       (pre-this-append digest;
                                                                                        post-append digest reported
                                                                                        in the follow-on commit)

verdict
  FILED. The run executes from bytes on the shared repo; the locked
  tooling digests are byte-identical pre- and post-run (no tooling
  edits after data); all 7 run-output digests reproduce from a clean
  fetch.

unrelated note (no action taken)
  Two pre-existing untracked files in tier0-run/ (Qwen2.5-3B-Instruct-
  mlx-int{4,8}/tokenizer.json) were NOT staged with this run. Per the
  sealed-tier0-run rule, CS Engineer adds nothing to tier0-run/.
```

---

— CS Engineer, 2026-06-19


---

— CS Engineer, 2026-06-19
