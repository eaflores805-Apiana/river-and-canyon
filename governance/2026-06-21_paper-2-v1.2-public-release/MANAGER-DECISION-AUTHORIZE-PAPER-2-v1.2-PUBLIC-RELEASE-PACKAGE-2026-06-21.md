# Manager Decision — Authorize Paper 2 v1.2 Public Release Package

**To:** CS Engineer, Senior Engineer
**Cc:** C5, Team Lead
**From:** Manager
**Subject:** Authorize Paper 2 v1.2 Release / Tag / Publication Package
**Status:** AUTHORIZED — PUBLIC RELEASE PACKAGE ONLY

Manager approves public release packaging for:

```text
Paper 2 v1.2 — Correctness Is Not Constructibility
```

## Release-candidate artifact of record

```text
Path:
papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-RELEASE-CANDIDATE-v1.2.md

sha256:
5b385d7f0409f9c050f6c6d87dcb7d665adc49df1f26468785fcfcc0d55ca1d8

Remote HEAD verified:
cd3190ae0472ab1650cfbfaaeced58935ba7578b
```

## Basis for release authorization

The release candidate has cleared:

```text
C5 claim-risk review
CS provenance / digest review
CS mechanical apply verification
Manager RC lock
SE final byte verification
```

Senior verified:

```text
- locked artifact path present
- sha256 matches exactly
- corrected v0.3 softening present
- old stronger remnants absent
- corrected figure assets match
- embedded SVG text softened
```

## Authorized release-package actions

CS may now prepare the public release package by:

```text
1. Promoting the locked v1.2 RC manuscript to the public Paper 2 release path.
2. Preserving the reviewed manuscript body and claim language.
3. Updating only release-status labels required for public release.
4. Generating / filing release artifacts as needed, including Markdown and PDF if standard for this repo.
5. Creating the release tag for Paper 2 v1.2.
6. Returning final release paths, digests, and tag information.
```

## Required release constraints

Do not change claim-bearing prose.

Do not alter:

```text
- V3/hop1 finding language
- P-role limitation language
- Claim B / Claim #5 / Claim C status
- pre-stress boundary
- no-compression boundary
- no-certification / no-capability / no-mechanism boundaries
```

If any claim-bearing prose changes, return to C5 before release.

## Required CS return

Return:

```text
CS RETURN — PAPER 2 v1.2 PUBLIC RELEASE COMPLETE
```

Include:

```text
- release commit SHA
- final remote HEAD
- release tag name and commit
- released Markdown path and sha256
- released PDF path and sha256, if generated
- confirmation the released body matches the locked RC except approved release-status labels
- confirmation figures match C5-cleared assets
- confirmation Paper 2 v1.0 tag remains preserved
- confirmation no run / rerun / compression / tooling / threshold change occurred
- confirmation tier0-run remains sealed
```

## Boundaries

This release authorization does **not** authorize:

```text
new experiment
construction redesign
compression
INT8 / INT4
Claim C
Paper B
certification claim
capability claim
mechanism claim
M5 distractor-attractiveness experiment
```

M5 remains bounded in the paper, not experimentally resolved.

The Path A FP16 K=5 FAIL remains closed.

— Manager
