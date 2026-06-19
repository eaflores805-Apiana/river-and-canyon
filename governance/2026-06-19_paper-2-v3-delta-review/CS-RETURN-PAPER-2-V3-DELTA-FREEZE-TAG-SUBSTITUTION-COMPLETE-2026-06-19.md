# CS RETURN — Paper 2 V3 Delta Freeze/Tag Substitution Complete

**Date:** 2026-06-19
**From:** CS Engineer
**To:** Manager; Cc: Team Lead, Senior Engineer, C5
**Re:** Manager Decision 2026-06-19 — "Claim Ledger Identifier and Paper 2 Freeze/Tag Substitution"
**Status:** **COMPLETE.**

---

## Headline

```text
2 authorized substitution passes applied — and ONLY those 2:

  Pass 1 (Appendix B): 9 placeholder lines → full sha256 (1-for-1; 9 lines)
  Pass 2 (Appendix A): 1 bracketed identifier → notes/CLAIM-LEDGER-v1.0.md (1 line)

Final diff: exactly 10 insertions / 10 deletions (balanced; no other prose
changed, no claim language touched).

New file created (per Manager identifier authorization):
  notes/CLAIM-LEDGER-v1.0.md
    — carries the V3 negative-finding row
    — claims A/B/C carried BY REFERENCE to the sealed tier0-run/ entry
      (sha b1687559…); CS authored no claim language
    — Claim #5 preserved as "blocked on a precondition"
    — Claim C preserved as untouched
    — program remains pre-stress
```

---

## Filing record

```text
substitution commit          (recorded post-commit in §clean-fetch)
final remote HEAD            (recorded post-commit in §clean-fetch)
clean-fetch confirmation     (recorded post-commit in §clean-fetch)
```

## Final Paper 2 V3 delta path + sha256

```text
path     path-a/in-review/PAPER-2-V3-DELTA-DRAFT-v0.1.md
sha256   ab52913c86b7745c4f2bfca0b242df77f010c82d874da34f7afa4a2b92364f99   (post-substitution)
prior    dcc94c1593ba310300cdf7df3e06c6033e2800d4edefb241fa0cfdc54a08cf7f   (C5-v0.2-BYTEREVIEW-reviewed
                                                                              bytes; preserved in git history
                                                                              at commit fed7de05bc41f0b8c2dc07bcd1f8f0f26df42c2f)
```

## New claim-ledger release path + sha256

```text
path     notes/CLAIM-LEDGER-v1.0.md
sha256   15f32e1a68620a9101d344514b7c2240a9a78969a564dd8fce589f86b32ea087
```

## Full Appendix B digest list as inserted

```text
V3 floor-check (anchor; seeds 001–096):
  decision    6a34f6dc9687e04d0bc58b1595b4c6e9555a59e4bb606e40e9aa72ddd2c048c5
              (COMPONENT-ADMISSIBLE-UNDER-COMPETITION)

V3 composite-gate run (anchor; fresh 097–192):
  run dir    experiments/2026-06-18_v3-composite-gate-run    HEAD 09030b18  (kept verbatim)
  decision   3924ff35087c5648a20101e463f2129d6d731a853c4b9f0e3d61a4ade6efe842
             (PRECONDITION-FAIL)

V3 hop1-stability run (six fresh 193–768):
  run dir   experiments/2026-06-19_hop1-stability-run    HEAD fe677158  (kept verbatim)
  decision.json                     8676530a97e4322f38cf8ded17710db32883c16a5b1b431e9af284dd9b4f8965
                                    (HOP1-STABLE-INADMISSIBLE; SE reproduced byte-identical)
  covariate_log.json                480f70d18f908a4dd89c8f5435cc122b61cfbf68e8fa006478fcfb8949049950
                                    (P-role 352/352 P_decoy_head)
  admissibility_summary.json        3763f736ff2dae8e2a90908a3787446d3e95c300062d02199107b6ebd85857e9
                                    (576/576 PASS)
  prompt_conformance_summary.json   b361b1d7b8bda061ad456dad0fe3cc82a81440277669f0fe651695ec0af92758
                                    (576/576 PASS)
  manifest.json                     2ad2015c5edc9d8c8a654a7f5b360d8c8b98983b3f85e4558ea29976bfc4a1bb
                                    (present; lists decision/covariate/run_record + scored)

Internal banked governance artifacts (unchanged in this pass; carried into
Appendix B as full sha256):
  V3-COMPOSITE-GATE-RUN-SE-VERIFICATION-RETURN-v0.1.md
                                    0eb0edcb6cc71632d41c58f2cd44ff802ba7beb173bf839bca4c50beecf88abd
  V3-FLOOR-CHECK-RUN-SE-VERIFICATION-RETURN-v0.1.md
                                    03d2ead80e830a8067c145e6516e20847fb0d2961a9ead85236ff696fe3d560f
  HOP1-STABILITY-FINDING-REPORT-v0.1.md            2969ec1a…   (already full at v0.1 filing — UNCHANGED)
  HOP1-STABILITY-RUN-SE-VERIFICATION-RETURN-v0.1   84a5716b…   (already full at v0.1 filing — UNCHANGED)

Model / profile (locked; unchanged in this pass):
  Qwen/Qwen2.5-3B-Instruct   revision aa8e72537993ba99e69dfaafa59ed015b17504d1   FP16   greedy (temp 0)

Threshold statement (unchanged in this pass):
  V3 admissibility floor = Wilson lower bound > 0.75
  K=5, P=5, M≥10, selection margin 0.25, derived structural floor F=0.20
  Thresholds are local to this construction/model/vocabulary/scoring/geometry (§7).
```

## Confirmation: only the two authorized substitution passes were made

```text
diff scope (git diff path-a/in-review/PAPER-2-V3-DELTA-DRAFT-v0.1.md):

  1 file changed, 10 insertions(+), 10 deletions(-)
  perfectly balanced — strict 1-for-1 line replacement; no insertions beyond
  the substitution lines themselves

lines touched, by category:

  Pass 1 (Appendix B):  9 lines
    - line 122  decision  6a34f6dc…                       → full sha256
    - line 126  decision  3924ff35…                       → full sha256
    - line 130  decision.json           [CS to recompute] → full sha256
    - line 131  covariate_log.json      [CS to recompute] → full sha256
    - line 132  admissibility_summary.json   [CS to recompute] → full sha256
    - line 133  prompt_conformance_summary.json [CS to recompute] → full sha256
    - line 134  manifest.json           [CS to recompute] → full sha256
    - line 142  V3-COMPOSITE-GATE-RUN-SE-VERIFICATION-RETURN   0eb0edcb…   [CS to recompute]  → full sha256
    - line 143  V3-FLOOR-CHECK-RUN-SE-VERIFICATION-RETURN      03d2ead8…   [CS to recompute]  → full sha256

  Pass 2 (Appendix A):  1 line
    - line 110  "Claim Ledger [version to be set ... — CS/TL to confirm the identifier]"
                → "Claim Ledger `notes/CLAIM-LEDGER-v1.0.md`"

  Total: 10 lines authorized; 10 lines changed; 0 other lines touched.

intermediate slip + correction (full disclosure):
  My first pass also added a NEW run_record.json line in the hop1-stability
  Appendix B block. Per Manager memo ("No other prose changes are authorized
  by this decision"), I reverted that addition before commit. The final diff
  contains only the 10 strictly-1-for-1 substitutions above.
```

## Confirmation: no claim prose changed

```text
- C5-cleared prose (everything outside the 10 substituted lines)        UNCHANGED
- abstract revision (§1)                                                 UNCHANGED
- §3.3 second-construction text                                          UNCHANGED
- §4.6 cross-materialization result text                                 UNCHANGED
- Table V3-1 + caption                                                   UNCHANGED
- §5/§7 discussion + limitations revisions                               UNCHANGED
- §9 future-work revision                                                UNCHANGED
- §10 forbidden-claims checklist                                         UNCHANGED
- Boundaries footer                                                      UNCHANGED
- "The one to carry up" closing paragraph                                UNCHANGED
- Appendix A: only the bracketed identifier replaced; the rest of the
  paragraph (the substantive Claim B / Claim #5 / Claim C language)     UNCHANGED
- Appendix B: only placeholder digests replaced with full sha256; all
  surrounding labels, parenthetical descriptors, threshold statement,
  model/profile line                                                     UNCHANGED
```

The only "new" content in the package is `notes/CLAIM-LEDGER-v1.0.md`, which was
explicitly authorized by Manager Decision 2026-06-19. That file carries Claims
A/B/C BY REFERENCE to the sealed `tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md`
(sha `b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2`); CS
authored no claim language in that file either — only the V3 negative-finding row
(empirical record + digests + reads-against-claims), which is the row Manager
authorized.

## Confirmation: tier0-run/ remained sealed

```text
git status tier0-run/  (pre- and post-substitution)
  ?? tier0-run/Qwen2.5-3B-Instruct-mlx-int4/tokenizer.json   (pre-existing untracked; NOT staged)
  ?? tier0-run/Qwen2.5-3B-Instruct-mlx-int8/tokenizer.json   (pre-existing untracked; NOT staged)

git ls-files tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md  → tracked at sha b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2
git diff   tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md  → (empty; no change)

No file under tier0-run/ was added, modified, deleted, or staged by this pass.
```

## Confirmation: Paper 2 v1.0 tag untouched

```text
git show paper2-cells01-03-v1.0 --stat
  tag paper2-cells01-03-v1.0
  Tagger: Elias Flores
  Date:   Tue Jun 9 18:54:31 2026 -0700
  Paper 2 freeze/tag — Correctness Is Not Constructibility

  (manuscript blob 7d6706a3… — UNCHANGED; tag NOT moved)
```

---

## Scope held (verbatim from Manager memo)

```text
- did NOT edit claim language                          held
- did NOT modify C5-cleared prose                      held
- did NOT alter thresholds                             held
- did NOT edit tooling                                 held
- did NOT regenerate prompts                           held
- did NOT rerun analysis                               held
- did NOT run models                                   held
- did NOT touch sealed tier0-run/ files                held
- no new experiment / construction redesign            held
- no compression / INT8 / INT4                         held
- no Claim C, no Paper B                               held
- no certification claim, capability claim,
  mechanism claim                                      held
- Path A FP16 K=5 FAIL                                 stays closed
```

---

## §clean-fetch. Clean-fetch confirmation

To be appended after this return commits and pushes.

---

— CS Engineer, 2026-06-19
