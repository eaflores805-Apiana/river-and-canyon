# CS Correction Report — Wording Standardization Pre-Merge

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Team Lead (response to urgent correction memo 2026-06-10); Cc: Senior Engineer, Manager
**Re:** Required wording standardization across Paper 2 addendum and B1 v2 PROVENANCE.md
**Status:** Corrections complete on both surfaces; merge authorization remains a Manager decision

---

## Record status

```
Corrections committed and pushed on both main and b1-harness-v2.
Paper 2 v1.0 tag and manuscript: verified unmoved/unedited.
Stale-wording sweep: clean (two meta-references to the correction itself; not stale propagation).
Merge authorization: still paused, pending this confirmation.
No runs, candidate, or thresholds authorized.
```

---

## 1. Addendum file path

`governance/2026-06-09_paper2-v1.0-release/ADDENDUM-01-model-snapshot-backing.md`

(Filename per Senior's intended-path header. Team Lead status board referred to it as
`PAPER2-RELEASE-RECORD-ADDENDUM-01.md`; flag remains open if rename desired.)

---

## 2. Commit SHA containing the corrected addendum

`531ba869f256ea39ce81895e2e9f7457a422149a` (branch `main`)

This commit replaces §4 of the addendum with canonical mlx_lm wording. History was
not rewritten — the original commit `5cbcd66` remains in the log, and `531ba86` is
the superseding correction filed as a new governance commit per Team Lead instruction.

---

## 3. Full 64-character model content hash present in addendum

**Confirmed.** §2 of the addendum contains:

```
sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20
```

The full 64-character hex string is verbatim from Senior's delivered text. CS verified
bit-identity against the regression result file
`experiments/2026-06-09_b1-harness-v2/results/RESULTS-B1V2-REGRESSION-full-cell03-1781070929.json`
at commit `2d93ff11de82bbfb8d3e5940eb1b73a6767bd229` on branch `b1-harness-v2`.

---

## 4. Snapshot wording is canonical

**Confirmed.** §3 of the addendum reads:

```
runner-provenance-backed via behavioral bit-identity; snapshot-ID assertion
corroborated, historically asserted.
```

Verbatim from Senior's text; matches Team Lead's required canonical wording.

---

## 5. mlx_lm wording is canonical

**Confirmed.** §4 of the addendum (post-correction in commit `531ba86`) reads:

```
mlx_lm 0.19.3 → 0.31.3 was verified-null for the locked Paper 2 reproduction
configuration: same model, tokenizer, prompt path, scorer, manifest, deterministic
decoding, and reproduction surface. The 96/96 bit-identical reproduction is the
evidence. Version drift remains a provenance variable for any changed configuration.
```

Matches Team Lead's required canonical wording. Broad "retired" wording removed.

---

## 6. PROVENANCE.md correction — path and commit SHA

**Path:** `experiments/2026-06-09_b1-harness-v2/PROVENANCE.md` (branch `b1-harness-v2`)

**Commit SHA:** `ff8466b2702205e9b9f95458cfe2d9023cb98ccb` (branch `b1-harness-v2`)

The mlx_lm version-drift paragraph (lines 41–47 post-edit) now reads verbatim:

```
Version drift note — verified-null for locked Paper 2 reproduction configuration.
Paper 2 ran under mlx_lm 0.19.3; B1 v2 regression ran under mlx_lm 0.31.3. The 96/96
bit-identical reproduction (paper2_regression.py --mode full, 2026-06-09; reference
RESULTS-TWOHOP-L1-cell03-1780948339.json, sha256 f29783622f...) verifies null drift
for the locked Paper 2 reproduction configuration only: same model, tokenizer, prompt
path, scorer, manifest, deterministic decoding, and reproduction surface. Version
drift remains a provenance variable for any changed configuration.
```

The snapshot wording in PROVENANCE.md (§"Model snapshot — runner-provenance backing
recorded") was already brought to canonical form in earlier commit `bdf8bb3` (Team
Lead 2026-06-09 correction). No additional edit needed there.

---

## 7. Stale-wording sweep result

Scope: every `.md` and `.py` file under `experiments/` and `governance/` on both
`main` and `b1-harness-v2`.

Search patterns (case-insensitive):
- `version-drift retired`, `version drift retired`
- `version-drift caveat retired`, `version-drift caveat is retired`
- `model flag retired`, `snapshot caveat retired`, `asserted-only flag retired`
- `mlx_lm drift is harmless`
- broader: `drift.*retired`, `caveat is retired`, `caveat .* therefore retired`

**Result on `b1-harness-v2`:** no hits. Branch is clean.

**Result on `main`:** no hits on the banned phrases. Two meta-references to the word
"retired" remain, both documenting the correction (not propagating stale wording):

| File | Line | Context |
|---|---|---|
| `governance/2026-06-09_paper2-v1.0-release/ADDENDUM-01-model-snapshot-backing.md` | 55 | CS editorial-correction note: *"this section originally used 'retired' wording. Replaced with the canonical phrasing above."* |
| `governance/2026-06-09_b1-harness-v2-merge-readiness/BRANCH-EVIDENCE-PACKET.md` | 46 | Paraphrasing Team Lead 2026-06-09 status correction: *"snapshot wording corrected from 'retired' to 'runner-provenance-backed via behavioral bit-identity...'"* |

Both are quoted in the context of describing the correction itself, not propagating
the stale wording. CS reads both as compliant with Team Lead's intent; flag for
Team Lead if they should be rephrased.

---

## 8. Paper 2 v1.0 tag and manuscript — not moved, not edited

**Tag verification:**

```
git rev-parse paper2-cells01-03-v1.0          → 41c033fc59597eb42015de9019c3ac7b7d19dd98
git cat-file -t paper2-cells01-03-v1.0        → tag
Tagged commit                                  → 40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce
Tagged manuscript blob                         → 7d6706a346bb634bed6752ff147fd67e1ad2596f
```

All three values match the Paper 2 v1.0 RELEASE-RECORD.md exactly:

```
RELEASE-RECORD.md §"Tag identifiers" — recorded values:
  Tag SHA                : 41c033fc59597eb42015de9019c3ac7b7d19dd98
  Commit SHA tagged      : 40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce
  Tagged manuscript blob : 7d6706a346bb634bed6752ff147fd67e1ad2596f
```

**Confirmed:** the Paper 2 v1.0 tag was not moved. The released manuscript blob was
not rewritten. No tier0-run/ files were modified. The 13/13 Appendix B hash set is
intact (no commits to tier0-run/ since the v1.0 release).

---

## Summary

Both wording surfaces — the Paper 2 addendum (`531ba86` on main) and the B1 v2
PROVENANCE.md (`ff8466b` on b1-harness-v2) — now carry Team Lead's canonical
wording for both the snapshot reclassification and the mlx_lm version-drift note.
No banned phrases propagate. The Paper 2 v1.0 release surface is unchanged. Merge
authorization remains a Manager decision; CS's pre-merge wording standardization
is complete.

---

## Boundaries remain closed

```
B1 merge · candidate selection · threshold values · certification evaluation
new model runs · re-runs beyond authorized reproduction validation
unconditioned token-prior runs · activation logging
INT8 / INT4 execution · multi-model execution
Fork A reactivation · Claim C activation
Paper 3 execution as an experiment · Paper 6 activation
public benchmark packaging · artifact mutation
```

---

— CS Engineer, 2026-06-10
