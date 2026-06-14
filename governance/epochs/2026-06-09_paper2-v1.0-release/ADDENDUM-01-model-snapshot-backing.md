# Addendum 01 to Paper 2 v1.0 Release Record — Model-Snapshot Provenance Reclassification

*Senior Engineer. Filed as an addendum; the v1.0 release record itself is not mutated. Intended path:
`governance/2026-06-09_paper2-v1.0-release/ADDENDUM-01-model-snapshot-backing.md`.*

**Date:** 2026-06-09
**Basis:** B1 v2 full Paper 2 regression (branch `b1-harness-v2`, latest commit
`2d93ff11de82bbfb8d3e5940eb1b73a6767bd229`); CS final report 2026-06-09; PROVENANCE.md of
`experiments/2026-06-09_b1-harness-v2/`.

## 1. What the release record said

The Paper 2 v1.0 release record carried the model snapshot as **asserted-only**: the HuggingFace
snapshot directory `aa8e72537993ba99e69dfaafa59ed015b17504d1` was recorded as asserted by the runner
environment without runner-provenance backing, with backing deferred to B1.

## 2. What B1 v2 produced

The B1 v2 full regression (96 inferences, Paper 2 reproduction context, deterministic decoding,
mlx_lm 0.31.3) produced, CS-attested:

- a runner-computed content hash over the model snapshot directory,
  `model_snapshot_hash = sha256:abee745b7dfe399d9254dbcdea5e3e3902aa95d71a31989b7b720b7ac9907b20`
  *(full 64-character value CS-attested 2026-06-09; matches the regression result file under
  `experiments/2026-06-09_b1-harness-v2/results/` at commit `2d93ff11…`)*; and
- **96/96 raw_output records bit-identical** to the Paper 2 v1.0 locked Cell03 results, with all gate
  decisions matching and v1 output shape preserved (7/7).

## 3. Reclassification — stated precisely

The two identifiers are different kinds and back different statements; the reclassification keeps them
distinct:

- **Backed (new):** the weights used in the B1 v2 regression carry runner-attested content hash
  `sha256:abee745b…`, and those weights reproduce the Paper 2 v1.0 results bit-identically (96/96).
  The material provenance question — *which weights produced the Paper 2 numbers* — is therefore now
  **runner-provenance-backed via behavioral identity**: the results are tied to content-hash-attested
  weights.
- **Still asserted (historical):** that the Paper 2 run's snapshot directory was HuggingFace snapshot
  `aa8e7253…`. No retroactive proof of the 2026 run directory's identity is possible; that assertion is
  now **corroborated** by the bit-identity result but is not converted into a backed claim.

**Status change:** model-snapshot provenance: *asserted-only (backing deferred to B1)* →
**runner-provenance-backed via behavioral bit-identity; snapshot-ID assertion corroborated,
historically asserted.**

## 4. Side result recorded with it

mlx_lm 0.19.3 → 0.31.3 was **verified-null for the locked Paper 2 reproduction configuration**: same
model, tokenizer, prompt path, scorer, manifest, deterministic decoding, and reproduction surface.
The 96/96 bit-identical reproduction is the evidence. Version drift remains a provenance variable
for any changed configuration.

*Editorial correction 2026-06-10 (CS, per Team Lead 2026-06-10 wording standardization):* this
section originally used "retired" wording. Replaced with the canonical phrasing above. No claim,
hash, or scientific content changed; only the wording standard.

## 5. Effectivity

This addendum takes effect for the release record when B1 v2 is merged and locked (runner amendment
lock note + EXPERIMENT_LOG update, per CS's pending list). Until merge, it stands as the prepared
reclassification, contingent on no change to the regression artifacts between the reported commit and
the lock.

## 6. Not changed by this addendum

Paper 2 v1.0 content (md/pdf), the freeze tag `paper2-cells01-03-v1.0`, all tier0-run/ artifacts, the
13/13 Appendix B hash set, and every standing lock and non-authorization. No candidate selection, no
threshold values, no runs beyond the already-reported regression, no Claim C / seam / retention claim.

— Senior Engineer
