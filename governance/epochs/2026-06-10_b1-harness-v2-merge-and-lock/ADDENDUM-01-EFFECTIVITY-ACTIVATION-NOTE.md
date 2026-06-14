# Addendum 01 Effectivity Activation Note

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Elias / Manager (item 8 of post-merge return); Cc: Team Lead, Senior Engineer
**Re:** Explicit confirmation that ADDENDUM-01-model-snapshot-backing.md is now effective under its own §5 effectivity clause
**Status:** Effectivity active. No artifact modified to produce activation; activation is self-gating.

---

## Record status

```
Addendum 01 §5 conditions: both met as of this filing.
Addendum 01 effectivity: ACTIVE for the Paper 2 v1.0 release record.
Paper 2 v1.0 tag and manuscript: unmoved/unaltered.
Boundaries: all still closed.
```

---

## What the §5 effectivity clause says

`governance/2026-06-09_paper2-v1.0-release/ADDENDUM-01-model-snapshot-backing.md` §5:

> *"This addendum takes effect for the release record when B1 v2 is merged and locked
> (runner amendment lock note + EXPERIMENT_LOG update, per CS's pending list). Until
> merge, it stands as the prepared reclassification, contingent on no change to the
> regression artifacts between the reported commit and the lock."*

The clause is **self-gating**: effectivity is conditional on (a) merge AND (b) lock,
and triggers automatically when both conditions hold. No human action toggles
activation; the activation timestamp is the moment both gates close.

---

## Both gates are closed

### Gate (a) — B1 v2 merged

```
Merge commit SHA:   3cbfce57d42536e8a5e1f35a92c931a03fe4e974
Merge type:         --no-ff
Branch absorbed:    b1-harness-v2 (tip ff8466b2702205e9b9f95458cfe2d9023cb98ccb)
Authorization:      Elias / Manager memo "Authorization to merge B1 v2", 2026-06-10
Pushed:             origin/main, post-merge state confirmed
```

### Gate (b) — B1 v2 locked

Per §5 specifically: "runner amendment lock note + EXPERIMENT_LOG update". Both
filed in companion commit `65da66d`:

```
Lock note:          governance/2026-06-10_b1-harness-v2-merge-and-lock/B1-V2-LOCK-NOTE.md
EXPERIMENT_LOG:     tier0-run/EXPERIMENT_LOG.md (new "B1 v2 Lock — 2026-06-10" section)
Companion commit:   65da66d0b307ec25926f38e0c9117ca92019577b
```

---

## Contingency clause check (also from §5)

> *"... contingent on no change to the regression artifacts between the reported
> commit and the lock."*

The §5 contingency requires that the regression artifacts referenced in the
addendum (the result files behind the 96/96 bit-identical reproduction) remain
unchanged between the reported commit (`2d93ff11`) and the lock.

**Verification (post-merge):**

```
Full regression artifact:
  Path:  experiments/2026-06-09_b1-harness-v2/results/RESULTS-B1V2-REGRESSION-full-cell03-1781070929.json
  Hash:  sha256:c9114c192dbaafc66d85babf6dacc62b9df8e4ffb87886fb868c875a202893f8
  Same hash as reported at branch commit 2d93ff11: YES (file content unchanged
    through bdf8bb3 wording-only commit, ff8466b wording-only commit, and the
    --no-ff merge into main)

Smoke regression artifact:
  Path:  experiments/2026-06-09_b1-harness-v2/results/RESULTS-B1V2-REGRESSION-smoke-cell03-1781070595.json
  Hash:  sha256:7cc17649a7a20d3bf99c7c9517fe8604a9a537a6cb3baf734d78ff0e71058f39
  Same hash as reported at branch commit e4322b0: YES
```

The §5 contingency is satisfied — regression artifacts are bit-identical to their
reported state. Effectivity is therefore unconditionally activated.

---

## What "effective" means for the Paper 2 v1.0 release record

Per the Manager-accepted wording (2026-06-10 authorization), Paper 2 v1.0
model-snapshot status is now formally recorded as:

> historically asserted in v1.0;
> subsequently corroborated by B1 runner-provenance-backed bit-identity reproduction;
> release-record addendum committed;
> Paper 2 tag/manuscript unchanged.

Per the same authorization, the mlx_lm version-drift status is formally recorded as:

> mlx_lm 0.19.3 → 0.31.3 was verified-null for the locked Paper 2 reproduction
> configuration: same model, tokenizer, prompt path, scorer, manifest,
> deterministic decoding, and reproduction surface. Version drift remains a
> provenance variable for any changed configuration.

These are the canonical formulations to use when referencing the Paper 2 v1.0
model-snapshot status and mlx_lm version-drift status from this point forward.

---

## What activation does NOT change

- Paper 2 v1.0 tag `paper2-cells01-03-v1.0` is **unmoved** (`41c033fc...`).
- Tagged commit `40c0cd5a...` is **unchanged**.
- Tagged manuscript blob `7d6706a3...` is **preserved in the tag**.
- The Paper 2 v1.0 RELEASE-RECORD.md itself is **not mutated** — the addendum is a
  sibling file by design.
- All tier0-run/ artifacts are **untouched**.
- All Appendix B hashes remain valid.

The activation is a governance-state change to the release record's *associated
provenance accounting*, not a modification to the release artifact itself.

---

## Boundaries remain closed

Activation of Addendum 01 effectivity does not authorize:

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
