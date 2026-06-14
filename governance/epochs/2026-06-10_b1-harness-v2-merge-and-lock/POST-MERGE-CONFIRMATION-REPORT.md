# CS Post-Merge Confirmation Report

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Elias / Manager (post-merge return); Cc: Team Lead, Senior Engineer
**Re:** B1 v2 merge execution and required confirmations
**Status:** Merge executed; lock note filed; all 7 required confirmations below.

---

## Record status

```
B1 v2 merged into main.
Merge commit: 3cbfce57d42536e8a5e1f35a92c931a03fe4e974
Branch tip absorbed: ff8466b2702205e9b9f95458cfe2d9023cb98ccb
Paper 2 v1.0 tag and released manuscript: unmoved; tag preserves frozen state.
Boundaries remain closed.
```

---

## Required CS return — 7 items

### 1. Merge commit SHA

```
3cbfce57d42536e8a5e1f35a92c931a03fe4e974
```

Merge type: `--no-ff` (explicit merge commit; preserves branch history).
Authorization basis: Manager memo "Manager Authorization — Merge B1 v2", 2026-06-10.

---

### 2. Branch content includes ff8466b2702205e9b9f95458cfe2d9023cb98ccb

**Confirmed.**

```
$ git merge-base --is-ancestor ff8466b2702205e9b9f95458cfe2d9023cb98ccb HEAD
  (returns true)

$ git log --oneline ff8466b -1
  ff8466b PROVENANCE.md mlx_lm canonical wording (Team Lead 2026-06-10)
```

`ff8466b` is the branch tip and is an ancestor of the merge commit `3cbfce5`.
The merge absorbs all five branch commits in their final state:

```
1aefc85  B1 v2 harness: initial implementation
e4322b0  B1 v2: smoke regression PASS
2d93ff1  B1 v2: full regression PASS
bdf8bb3  B1 v2 PROVENANCE: correct framing (Team Lead 2026-06-09)
ff8466b  PROVENANCE.md mlx_lm canonical wording (Team Lead 2026-06-10)
```

---

### 3. B1 v2 lock note

**Filed.** Path:

```
governance/2026-06-10_b1-harness-v2-merge-and-lock/B1-V2-LOCK-NOTE.md
```

The lock note records: merge identifiers, full locked-state hash set,
Addendum 01 §5 effectivity activation, Paper 3 substrate default posture, and
the explicit "what this merge does NOT do" boundary list.

---

### 4. EXPERIMENT_LOG update

**Filed.** Path:

```
tier0-run/EXPERIMENT_LOG.md (new "B1 v2 Lock — 2026-06-10" section)
```

Note on location: the seal on `tier0-run/` permits documentation updates to
existing files (memory: "tier0-run/ is SEALED (never add); existing files may
be updated for documentation"). EXPERIMENT_LOG.md is the program log; the
B1 v2 lock entry continues its established lineage. No new file added to
`tier0-run/`; no artifact modified.

Lock entry records: merge SHA, branch tip, locked runner hash, model snapshot
runner-provenance-backed hash, full and smoke regression artifact hashes,
test outcomes (26/26 offline + 96/96 bit-identical), Paper 2 v1.0 surface
status, Addendum 01 effectivity, Paper 3 substrate posture, and the
"what this lock does NOT do" boundary list.

---

### 5. Paper 2 v1.0 tag and released manuscript — not moved or altered

**Confirmed at merge time (post-merge state):**

```
Tag SHA:                 41c033fc59597eb42015de9019c3ac7b7d19dd98
Tagged commit SHA:       40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce
Tagged manuscript blob:  7d6706a346bb634bed6752ff147fd67e1ad2596f
```

All three values match `governance/2026-06-09_paper2-v1.0-release/RELEASE-RECORD.md`
exactly. Tag was not moved. Tagged commit and tagged manuscript blob are
preserved as frozen state.

**Honest note on on-main manuscript blob:** the current on-main manuscript
blob is `34ada312b96dd20138b3553e2a78a53ff0681b09`, which differs from the
tagged blob `7d6706a3...`. This difference is the documented v1.0 release
status-label update (commit `69df8be`, "Paper 2 v1.0 release: update status
label and archive governance") plus the PDF rebuild commit (`894140c`). Both
commits predate the B1 v2 work. The Paper 2 v1.0 RELEASE-RECORD.md §"Post-release
note" already documents this: *"PDF not rebuilt for v1.0 status update — .md
updated, PDF still reads 'Release candidate.'"*

**B1 v2 merge itself touched zero Paper 2 / tier0-run / governance files:**

```
$ git diff 5da0023..3cbfce5 --stat papers/ tier0-run/ governance/
  (empty — no changes to any of these)

$ git diff 5da0023..3cbfce5 --stat
  12 files changed, all under experiments/2026-06-09_b1-harness-v2/
```

The Paper 2 v1.0 tag, the tagged manuscript blob, and all tier0-run/ artifacts
are preserved unchanged by this merge.

---

### 6. Paper 3 substrate remains config-gated and disabled by default

**Confirmed.** Runner argparse defaults (from `runner_b1_v2.py` source, post-merge):

```
--mode               default="dry-run"
--context            default="paper2-reproduction"
--framework-version  default=FRAMEWORK_VERSION_NONE       (constant = "none")
--threshold-sheet    default=None
--expected-threshold-sheet-hash  default=None
```

Paper 3 substrate (D6 firewall enforcement, A.2 per-gate schema, threshold-sheet
hash verification, structural_proxies invocation) activates **only** when the
operator explicitly:

1. Passes `--context paper3-certification`, AND
2. Supplies `--threshold-sheet <path>`, AND
3. Supplies `--expected-threshold-sheet-hash <sha256:...>`.

With any of those absent, the runner operates in Paper 2 reproduction context
and Paper 3 substrate is dormant. Even when Paper 3 substrate is activated at
runtime, that activation is **not** authorization to apply Paper 3 certification;
certification application requires separate Manager authorization beyond this
merge.

---

### 7. No candidate threshold sheets, candidate outputs, or certification results

**Confirmed.** Post-merge sweep:

```
$ find experiments/ governance/ -type f \( \
    -name "*threshold-sheet*" -o -name "*threshold_sheet*" \
    -o -name "*certification-result*" -o -name "*candidate-output*" \
    -o -name "*certified-baseline*" \)
  (empty)

$ find experiments/ governance/ -type f \( -name "D[1-7]_*" -o -name "*_D[1-7]_*" \)
  (empty)
```

No candidate-specific files of any flavor were introduced by the merge. The
B1 v2 runner contains the *schema slot* for `structural_proxies` per-item, but
all merged result files carry empty `{}` for that slot (Paper 2 reproduction
context populates no candidate-specific structural proxies).

---

## Summary

All 7 confirmations satisfied. B1 v2 is now the active validity-harness
infrastructure on `main`. Addendum 01 §5 effectivity activates at this merge.
Paper 2 v1.0 release surface is preserved exactly. Paper 3 substrate is shipped
but inert by default and requires separate authorization to apply.

No further CS deliverables pending until next authorization arrives.

---

## Boundaries remain closed

```
candidate selection · threshold values · certification evaluation
new model runs · re-runs beyond authorized reproduction validation
unconditioned token-prior runs · activation logging
INT8 / INT4 execution · multi-model execution
Fork A reactivation · Claim C activation
Paper 3 execution as an experiment · Paper 6 activation
public benchmark packaging · artifact mutation
```

---

— CS Engineer, 2026-06-10
