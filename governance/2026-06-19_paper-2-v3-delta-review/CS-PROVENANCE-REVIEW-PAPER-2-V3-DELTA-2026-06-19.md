# CS RETURN — Provenance / Digest Review (Paper 2 V3 Delta Draft) — PASS

**Date:** 2026-06-19
**From:** CS Engineer
**To:** Team Lead, Manager; Cc: Senior Engineer, C5
**Re:** TL ACTION 2026-06-19 — "Provenance / Digest Review — Paper 2 V3 Delta Draft"
**Status:** **PASS — provenance package is freeze/tag ready.**

---

## Headline

```text
verdict           PASS — provenance package is freeze/tag ready.
                  Every Appendix B placeholder in the v0.1 delta draft resolves to a
                  full sha256 from locked bytes; both anchor decision-digest short
                  prefixes (6a34f6dc… , 3924ff35…) match in full; both SE-verification-
                  return short prefixes (0eb0edcb… , 03d2ead8…) match in full; the
                  hop1-stability run artifacts are present, complete, and byte-stable;
                  the final branch is HOP1-STABLE-INADMISSIBLE.

one carry-up      The Claim Ledger version identifier is a TL/Manager-decision question,
                  not a CS-blocker. Paper 2 §A points to "Claim Ledger v0.2"; this repo
                  carries the v0.1 working note + the sealed tier0-run/ constructibility-
                  floor entry (the Claim A/B/C carrier) but does not carry a file named
                  "v0.2" or "v0.3". See §13.

scope             Provenance / digests only. No claim language touched (C5 already
                  cleared prose at v0.2-BYTEREVIEW). No run, no regen, no threshold
                  change, no tooling edit.
```

---

## Repo HEAD + clean-fetch confirmation

```text
local HEAD                   (recorded post-commit in §X)
final remote HEAD            (recorded post-commit in §X)
clean-fetch confirmation     (recorded post-commit in §X)
```

(Per CS filing discipline: bytes verify from a clean fetch of the shared repo
before this return is treated as FILED. §X below records the values.)

---

## §1. Filed delta-draft path + sha256 — PASS

```text
path     path-a/in-review/PAPER-2-V3-DELTA-DRAFT-v0.1.md
sha256   dcc94c1593ba310300cdf7df3e06c6033e2800d4edefb241fa0cfdc54a08cf7f
status   readable + stable (no edits since the 2026-06-19 inbox-sweep filing
         at commit 8461e79de54432cc76570f0261738674707e4c13)
```

## §2. Hop1-stability run directory present — PASS

```text
path     experiments/2026-06-19_hop1-stability-run/
status   present; contains items_193_768 (576), prompts (2304), admissibility (576),
         scored (1152 contract + 1152 raw), 7 summary/decision/manifest JSONs,
         run_step_5.py + log, build_manifest.py — matches the manifest.json
         counts EXACTLY (manifest.counts.n_items=576, n_prompts_executed=1152,
         n_scored_contract=1152, n_blocks=6, n_per_block=96)
```

## §3. Run branch = HOP1-STABLE-INADMISSIBLE — PASS

```text
field                        value (from decision.json)
final_branch                 HOP1-STABLE-INADMISSIBLE
construct_fail_blocks        []           (admissibility + conformance 576/576 PASS)
hop2_control_fail_blocks     []           (hop2 96/96 every block; lower Wilson 0.9615)
hop1_clear_blocks            []
hop1_fail_blocks             [1, 2, 3, 4, 5, 6]
hop1_between_block_spread    min 0.2396  max 0.5625  range 0.3229  mean 0.3889
                             stddev 0.1245
branch_priority_order        ["CONSTRUCT-FAIL", "HOP2-CONTROL-FAIL",
                              "HOP1-STABLE-ADMISSIBLE",
                              "HOP1-STABLE-INADMISSIBLE",
                              "HOP1-UNSTABLE"]
```

## §4. Run manifest present + complete — PASS

```text
path                              experiments/2026-06-19_hop1-stability-run/manifest.json
sha256                            2ad2015c5edc9d8c8a654a7f5b360d8c8b98983b3f85e4558ea29976bfc4a1bb
manifest.run_id                   v3-hop1-stability-2026-06-19
manifest.final_branch             HOP1-STABLE-INADMISSIBLE
manifest.counts.n_items           576
manifest.counts.n_admissibility   576
manifest.counts.n_prompts_rendered 2304
manifest.counts.n_prompts_executed 1152
manifest.counts.n_scored_contract  1152
manifest.counts.n_blocks          6
manifest.counts.n_per_block       96
manifest.items                    576 entries (each with sha256)
manifest.prompts                  2304 entries (each with sha256)
manifest.admissibility            576 entries (each with sha256)
manifest.scored                   2304 entries (each with sha256)
manifest.hop1_stability_tooling   analyzer 31224f6f…, covariate logger b9532490…
manifest.reused_tooling_unchanged wrapper cc07e5a2, generator 6a2ceee1, realizer
                                  fb561fdc, conformance checker b8afa3f8,
                                  conformance runner, neutral pool
manifest.instrument               inspector cb4b0b60, constants 1d761c3d
manifest.run_record               run_record.json sha 11756a53…
manifest.decision                 decision.json sha 8676530a…
manifest.covariate_log            covariate_log.json sha 480f70d1…
```

## §5. decision.json digest (recomputed from locked bytes) — PASS

```text
path     experiments/2026-06-19_hop1-stability-run/decision.json
sha256   8676530a97e4322f38cf8ded17710db32883c16a5b1b431e9af284dd9b4f8965
```

## §6. covariate_log.json digest (recomputed from locked bytes) — PASS

```text
path     experiments/2026-06-19_hop1-stability-run/covariate_log.json
sha256   480f70d18f908a4dd89c8f5435cc122b61cfbf68e8fa006478fcfb8949049950
content  summary.primary_P_role_distractor_count        352
         summary.primary_P_role_among_wrong_count       352
         summary.primary_P_role_among_wrong_rate        1.0
         summary.n_hop1_match                           224
         summary.n_hop1_wrong                           352
```

## §7. admissibility_summary.json digest (recomputed from locked bytes) — PASS

```text
path     experiments/2026-06-19_hop1-stability-run/admissibility_summary.json
sha256   3763f736ff2dae8e2a90908a3787446d3e95c300062d02199107b6ebd85857e9
content  n_items 576  n_pass 576  n_reject 0  all_pass True
```

## §8. prompt_conformance_summary.json digest (recomputed from locked bytes) — PASS

```text
path     experiments/2026-06-19_hop1-stability-run/prompt_conformance_summary.json
sha256   b361b1d7b8bda061ad456dad0fe3cc82a81440277669f0fe651695ec0af92758
content  n_items 576  n_pass 576  all_pass True  §9(vi) PASS
```

## §9. run_record.json digest (recomputed from locked bytes) — PASS

```text
path     experiments/2026-06-19_hop1-stability-run/run_record.json
sha256   11756a53a9158e8687faab1da1a05d89cf77db7a74403e7d34b7a95d4c5e6702
content  model_name              Qwen/Qwen2.5-3B-Instruct
         model_revision_sha      aa8e72537993ba99e69dfaafa59ed015b17504d1
         precision               FP16
         decoding                greedy (temp=0.0)
         n_items                 576
         n_contexts_per_item     2 (hop1, hop2)   (composite + direct_query rendered,
                                                    NOT executed — N1.A discipline)
         n_prompts_total         1152
         inference_time_s        911.7
         model_load_time_s       6.0
```

## §10. V3 floor-check decision digest (recomputed) — PASS

```text
path     experiments/2026-06-18_v3-floor-check-run/analyzer_decision.json
sha256   6a34f6dc9687e04d0bc58b1595b4c6e9555a59e4bb606e40e9aa72ddd2c048c5
draft-listed prefix    6a34f6dc…    MATCH (first 8 hex)
draft-listed branch    COMPONENT-ADMISSIBLE-UNDER-COMPETITION  (consistent with the v0.1
                                                                  delta's anchor descriptions)
```

## §11. V3 composite-gate decision digest (recomputed) — PASS

```text
path     experiments/2026-06-18_v3-composite-gate-run/analyzer_decision.json
sha256   3924ff35087c5648a20101e463f2129d6d731a853c4b9f0e3d61a4ade6efe842
draft-listed prefix    3924ff35…    MATCH (first 8 hex)
draft-listed branch    PRECONDITION-FAIL                       (consistent with the v0.1
                                                                  delta's anchor descriptions)
draft-listed HEAD      09030b18                                (composite-gate run dir at
                                                                  09030b18 — historical;
                                                                  current HEAD is post-run)
```

## §12. Paper 2 Appendix B placeholders → full sha256 values (CS recompute) — PASS

For drop-in into the Appendix B block of the v0.1 delta draft (§9 of the draft), the
complete sha256 values are:

```text
V3 floor-check (anchor; seeds 001–096):
  decision.json                                6a34f6dc9687e04d0bc58b1595b4c6e9555a59e4bb606e40e9aa72ddd2c048c5
                                               (final_branch: COMPONENT-ADMISSIBLE-UNDER-COMPETITION)

V3 composite-gate run (anchor; fresh 097–192):
  run dir   experiments/2026-06-18_v3-composite-gate-run
  decision.json                                3924ff35087c5648a20101e463f2129d6d731a853c4b9f0e3d61a4ade6efe842
                                               (final_branch: PRECONDITION-FAIL)

V3 hop1-stability run (six fresh 193–768):
  run dir   experiments/2026-06-19_hop1-stability-run
  decision.json                                8676530a97e4322f38cf8ded17710db32883c16a5b1b431e9af284dd9b4f8965
                                                (HOP1-STABLE-INADMISSIBLE)
  covariate_log.json                           480f70d18f908a4dd89c8f5435cc122b61cfbf68e8fa006478fcfb8949049950
                                                (P-role 352/352 P_decoy_head)
  admissibility_summary.json                   3763f736ff2dae8e2a90908a3787446d3e95c300062d02199107b6ebd85857e9
                                                (576/576 PASS)
  prompt_conformance_summary.json              b361b1d7b8bda061ad456dad0fe3cc82a81440277669f0fe651695ec0af92758
                                                (576/576 PASS)
  manifest.json                                2ad2015c5edc9d8c8a654a7f5b360d8c8b98983b3f85e4558ea29976bfc4a1bb
                                                (present; lists decision/covariate/
                                                 run_record + per-item items/prompts/
                                                 admissibility/scored arrays)
  run_record.json                              11756a53a9158e8687faab1da1a05d89cf77db7a74403e7d34b7a95d4c5e6702
                                                (Qwen2.5-3B-Instruct rev aa8e7253, FP16,
                                                 greedy, 1152 calls)

Model / profile (locked):
  Qwen/Qwen2.5-3B-Instruct   revision aa8e72537993ba99e69dfaafa59ed015b17504d1
  FP16   greedy (temp 0)                       (verified from run_record.json bytes)

Internal banked governance artifacts (filed at path-a/in-review/, byte-faithful with the
SE-supplied originals):
  HOP1-STABILITY-FINDING-REPORT-v0.1.md            2969ec1a5ce830c2b77c974ad23b163e4cb1dca6a518800a555f5a159f6efb33
  HOP1-STABILITY-RUN-SE-VERIFICATION-RETURN-v0.1.md
    (filed at governance/2026-06-19_hop1-stability-run/)
                                                   84a5716b4f202a9337495100064d8e5f466ff8baf3e76bb16b4d221de05285b9
  V3-COMPOSITE-GATE-RUN-SE-VERIFICATION-RETURN-v0.1.md
    (filed at path-a/in-review/)
                                                   0eb0edcb6cc71632d41c58f2cd44ff802ba7beb173bf839bca4c50beecf88abd
                                                   draft-listed prefix 0eb0edcb…    MATCH
  V3-FLOOR-CHECK-RUN-SE-VERIFICATION-RETURN-v0.1.md
    (filed at path-a/in-review/)
                                                   03d2ead80e830a8067c145e6516e20847fb0d2961a9ead85236ff696fe3d560f
                                                   draft-listed prefix 03d2ead8…    MATCH

Threshold statement (state explicitly in Appendix B, verbatim from prereg):
  V3 admissibility floor = Wilson lower bound > 0.75; locked construction values
  K=5, P=5, M>=10, selection margin 0.25, derived structural floor F=0.20.
  Thresholds are local to this construction/model/vocabulary/scoring/geometry (§7).
```

All 4 short-prefix placeholders in the draft (`6a34f6dc…`, `3924ff35…`, `0eb0edcb…`,
`03d2ead8…`) and all 5 "[full sha256: CS to recompute]" placeholders are now
resolved to full sha256 values from the locked files. Both SE-supplied full-form
digests (the two SE-banked governance artifacts in the draft's §9 list) reproduce
exactly from the filed copies.

## §13. Claim-ledger version / path carrying the V3 negative-finding row — CARRY-UP

```text
Paper 2 manuscript (papers/paper2-correctness-is-not-constructibility/
correctness-is-not-constructibility.md, §Appendix A line 467) cites:
  "Claim Ledger v0.2."

Repo-local claim-ledger artifacts present:
  notes/claim-ledger-practice-note.md        v0.1  (working note; sha tbd at need)
  notes/claim-ledger-practice-note.pdf       v0.1  (pdf render)
  tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md
                                              b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2
                                              (the Claim A/B/C carrier; "Filed: 2026-06-07";
                                               SEALED per tier0-run rule — CS adds nothing
                                               here)

GAP (TL/Manager-decision-class, not a CS-blocker):
  The exact file named "Claim Ledger v0.2" cited by Paper 2 is NOT present at any
  version-resolvable path in this repo. The substantive Claim A/B/C carrier
  (sealed tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md) is present and is what
  v0.2 was understood to wrap, but the v0.2 version label is not bound to a file.

  The delta-draft's Appendix A says:
    "See Claim Ledger [version to be set to the release carrying the V3 negative-
    finding row — CS/TL to confirm the identifier]."

  CS recommendation (for TL/Manager decision):
    - the V3 negative-finding row (HOP1-STABLE-INADMISSIBLE on 6 fresh
      materializations; hop2 576/576; P-role 352/352 co-occurrence; composite-gate
      not readable) should land in a NEW versioned claim-ledger release:
        Option A:  v0.3 of the working-note lineage at notes/claim-ledger-*.md
        Option B:  a new versioned file (e.g., notes/CLAIM-LEDGER-v1.0.md)
                   that explicitly carries the V3 row and supersedes v0.2 +
                   the Constructibility-Floor entry by reference
    - either way, tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md must remain
      sealed and unmodified per the standing tier0-run rule; the V3 row's
      authoritative carrier therefore lives OUTSIDE tier0-run/
    - the delta's Appendix A bracketed identifier should be set to the chosen
      version after TL/Manager picks one (this is the single content-edit the
      delta needs from the freeze/tag pass beyond placeholder→full digest
      substitution)

This is the ONE remaining freeze/tag question on the package; it is a TL/Manager
identifier choice + a one-line edit, NOT a provenance failure.
```

---

## What does NOT need to change in the delta draft

```text
- claim language                  C5 cleared v0.2-BYTEREVIEW (sentence-level
                                  byte review); CS does not touch prose
- numbers in §4.6 + Table V3-1    every number cross-checks against the run record
                                  byte-for-byte (224/576, 352/576, per-block 50/23/
                                  35/39/54/23 over 96, hop2 576/576, Wilson lowers
                                  exactly as drafted)
- thresholds                      0.75 floor; K=5 P=5 M>=10 margin 0.25 F=0.20
                                  matches the prereg + tooling-build records
- anchor framing                  001..096 = COMPONENT-ADMISSIBLE-UNDER-COMPETITION
                                  (hop1 87/96), 097..192 = PRECONDITION-FAIL
                                  (hop1 28/96) — both decision digests verify
- locked tooling                  analyzer 31224f6f, logger b9532490, wrapper
                                  cc07e5a2, generator 6a2ceee1, realizer fb561fdc,
                                  conformance checker b8afa3f8, inspector cb4b0b60,
                                  constants 1d761c3d — ALL UNCHANGED
- model/precision/decoding        Qwen/Qwen2.5-3B-Instruct rev aa8e7253, FP16, greedy
                                  — verified from run_record bytes
```

## What the delta draft DOES need from the freeze/tag pass

```text
- Substitute placeholder short prefixes + bracketed "[full sha256: CS to recompute]"
  with the full sha256 values in §12 above (CS-supplied; pure substitution).
- Fill the Appendix A bracketed claim-ledger identifier (TL/Manager decision per §13).
- That is the entire edit scope. Nothing else.
```

---

## Scope held (carried verbatim from the TL ACTION)

```text
- this is NOT a claim-risk review (C5 cleared prose)        held
- did NOT edit claim language                                held
- did NOT run models                                          held
- did NOT regenerate prompts                                  held
- did NOT rerun analysis (digest recompute only)              held
- did NOT change thresholds                                   held
- did NOT alter tooling                                       held
- no new experiment, no construction redesign                 held
- no compression / INT8 / INT4                                held
- no Claim C, no Paper B                                      held
- no certification claim, capability claim, mechanism claim   held
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc…)        untouched
- tier0-run/ sealed; no files added (the 2 pre-existing
  untracked tokenizer.json files there remain unstaged)       held
- Path A FP16 K=5 FAIL                                        stays closed
- V3 ≠ C0                                                     not equated
```

---

## §X. Clean-fetch confirmation

To be appended after this return commits and pushes.

---

— CS Engineer, 2026-06-19
