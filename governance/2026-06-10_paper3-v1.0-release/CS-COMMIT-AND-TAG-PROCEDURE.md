# CS Commit and Tag Procedure — Paper 3 v1.0 RC

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Manager (authorization decision); Cc: Team Lead, Senior Engineer
**Re:** Proposed commit and tag procedure for Paper 3 v1.0 release
**Status:** Prepared and staged; no write actions taken. Awaits Manager release authorization.

---

## Record status

```
Procedure prepared for Manager review.
No write actions taken. No commit. No tag. No release record finalized.
Repo state at time of preparation: main @ 25f5acc (post-CS-V1.0-review commit).
Bundle source: certification_before_retention/paper3-certification-before-retention/
Two open findings from CS-RELEASE-CONSISTENCY-CHECKLIST: F1 (Senior manifest
refresh) and F2 (geometry check deferred). Neither blocks the procedure.
```

---

## Pre-execution state (verify before authorization)

```
git status: working tree clean (apart from environment-noise untracked files)
git branch: main
git log -1: 25f5acc  File CS review of Paper 3 v1.0 (release event)
paper3 slot in repo:  papers/  contains paper1 and paper2 only; no paper3 slot
Bundle source paths verified; sha256 hashes verified (see checklist F1 note)
```

---

## Proposed commit and tag plan

This is the **explicit fix** for the Paper 2 v1.0 release issue (where post-tag
status-label edits caused on-main vs tagged blob divergence). For Paper 3:

> The commit that adds the manuscript IS the commit that gets tagged. No post-tag
> edits to the manuscript file. The tagged blob and the on-main blob are identical
> from release tag forward.

### Step 1 — Stage all deliverables under `papers/paper3-certification-before-retention/`

Directory layout to create (parallels paper2 release structure):

```
papers/paper3-certification-before-retention/
  certification-before-retention.md
  certification-before-retention.pdf
  figures/
    fig1_series_gap_ladder.png
    fig1_series_gap_ladder.svg
    fig2_lineage_to_gates.png
    fig2_lineage_to_gates.svg
    fig3_failclosed_pipeline.png
    fig3_failclosed_pipeline.svg
    fig4_three_artifact_layers.png
    fig4_three_artifact_layers.svg
```

Source: copy from
`/Users/eliasflores/Documents/Projects/Apiana_Ai/LLM_Mechanics/Main/Apiana_Papers/certification_before_retention/paper3-certification-before-retention/`

(Lineage drafts and release-docs from the bundle are NOT copied into `papers/` —
they remain in the bundle as Senior's working archive. The release record in
`governance/` cites them by external path.)

### Step 2 — Pre-commit hash verification (CS attest)

Before staging, recompute hashes on the bundle source. Pass criteria:

```
md:  sha256:b948521ebab74b3a225a98509a07488c0f1a4c86d1802d46796e57b2d361e714
pdf: sha256:6223cf85a65f1bc6fe4621f717997e6b8d2b253b6156951715d6d30005080d8f
fig1.png: sha256:92e3df1de5f5453a511cf2723d185a363b61ffc3852210e255f0e01bcec082ac
fig1.svg: sha256:d78f3148a733609623d0d3196a3d1961963e33557d99ee42199c5517edce323e
fig2.png: sha256:7c2a7ca671ac7981e52fc50e19d66f29bb343e50afb1eb2c5608ebff0a74f9b5
fig2.svg: sha256:404057ca715964e0bae4343a4a324b2c33f0d94c867b5735aed7a9976b78547e
fig3.png: sha256:bd3ac23bd228d416e6e69036ad4b83801304007ab94ec687ddefd4ca2fd737a0
fig3.svg: sha256:b5c55151ce0b1441de4d16f7ff984e73448086715413c8eca86fe0683f288df8
fig4.png: sha256:ce9ad944f256e19e2f06ef82285ed528b087a0ad41326ffade0474f186214970
fig4.svg: sha256:0820aca8bfe4c66baa8822964cd095ba3f3441cdaf53ba5d992e3dd9f31ec1ee
```

If any hash drifts from these values at execution time, abort and re-verify.

### Step 3 — Commit

```bash
git add papers/paper3-certification-before-retention/
git commit -m "Paper 3 v1.0: release manuscript, PDF, and figures"
```

Proposed commit message body:

```
Lands Paper 3 v1.0 (Certification Before Retention) as the released form.

Framework identifier: paper3-certification-protocol-v1.0 (first lock-eligible
framework version per the manuscript's own framework-version rule).

This commit is the release commit. Per the Paper 2 lesson, the RC text IS the
final v1.0 text — no post-tag masthead flip. The blob that lands on main here
is the same blob that will be tagged.

Contents:
  certification-before-retention.md   sha256:b948521ebab74b3a225a98509a07488c0f1a4c86d1802d46796e57b2d361e714
  certification-before-retention.pdf  sha256:6223cf85a65f1bc6fe4621f717997e6b8d2b253b6156951715d6d30005080d8f
  figures/ (4 PNG + 4 SVG; hashes recorded in
            governance/2026-06-10_paper3-v1.0-release/CS-RELEASE-CONSISTENCY-CHECKLIST.md)

Authorization: Manager release authorization, 2026-06-10.
Reviews: governance/2026-06-09_paper3-threshold-framework-review/
  (v0.2, v0.3, v0.6, v0.7, v0.8, v0.9, v1.0; final CS review of record: v0.9
   for substance, v1.0 for release event)

Boundaries unchanged: candidate selection, threshold population, certification
evaluation, all stress lanes, Fork A, Claim C, Paper 3 application — all
remain blocked.

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Step 4 — Post-commit verification (before tag)

```bash
# Identify the commit SHA
RELEASE_COMMIT=$(git rev-parse HEAD)
echo "Release commit: $RELEASE_COMMIT"

# Verify committed blob hashes match bundle source
git cat-file blob HEAD:papers/paper3-certification-before-retention/certification-before-retention.md | shasum -a 256
# Expected: b948521ebab74b3a225a98509a07488c0f1a4c86d1802d46796e57b2d361e714

# Verify the git blob SHA of the committed manuscript
git ls-tree HEAD papers/paper3-certification-before-retention/certification-before-retention.md
# Record the blob SHA (40-hex git blob hash) for the release record
```

### Step 5 — Tag

Proposed tag name (Senior's recommendation, per RC package §4):

```
paper3-certification-protocol-v1.0
```

Rationale: tag matches the lock-eligible framework identifier byte-for-byte, so a
threshold sheet's `framework_version` field names the tag exactly.

Alternative if Manager prefers the paper2-style form:

```
paper3-protocol-v1.0
```

(Manuscript identifier `paper3-certification-protocol-v1.0` still governs
lock-eligibility regardless of tag name choice.)

```bash
# Annotated tag (recommended for release tags)
git tag -a paper3-certification-protocol-v1.0 -m "Paper 3 v1.0 release"
# OR
git tag -a paper3-protocol-v1.0 -m "Paper 3 v1.0 release"
```

### Step 6 — Post-tag verification (re-confirm no divergence)

```bash
TAG_NAME=paper3-certification-protocol-v1.0
echo "=== Tag identifiers ==="
echo "tag object SHA:  $(git rev-parse $TAG_NAME)"
echo "tagged commit:   $(git rev-parse $TAG_NAME^{commit})"
echo "tagged blob:     $(git ls-tree $TAG_NAME papers/paper3-certification-before-retention/certification-before-retention.md | awk '{print $3}')"
echo ""
echo "=== On-main blob (should match tagged blob exactly) ==="
echo "main blob:       $(git ls-tree HEAD papers/paper3-certification-before-retention/certification-before-retention.md | awk '{print $3}')"
echo ""
echo "Match check (tagged blob == on-main blob): pass if both lines above are identical SHAs"
```

**Pass criterion:** tagged blob SHA == on-main blob SHA. (This is the explicit fix
for Paper 2's post-tag divergence; passing this check confirms the fix worked.)

### Step 7 — Push commit and tag

```bash
git push                    # push the release commit
git push origin $TAG_NAME   # push the tag explicitly
```

### Step 8 — File release record

CS writes the release record at:

```
governance/2026-06-10_paper3-v1.0-release/RELEASE-RECORD.md
```

(parallel to Paper 2's `governance/2026-06-09_paper2-v1.0-release/RELEASE-RECORD.md`)

Contents:
- Tag identifiers table (tag SHA, tagged commit SHA, tagged manuscript blob SHA)
- All 8 figure hashes
- All 10 checklist results (referencing this checklist file)
- Authorization chain
- Standing boundaries (carried forward)
- CS-Senior-Manager signoffs

### Step 9 — Update auxiliary docs (post-release)

- `tier0-run/EXPERIMENT_LOG.md`: append "Paper 3 v1.0 Release — 2026-06-10" entry
  (consistent with the seal carve-out for documentation updates)
- `governance/passdown/2026-06-10_passdown-letter.md` (or a new dated letter):
  refresh "Paper 3" lane to RELEASED
- Memory file `llm_mechanics_experiments.md`: refresh state

### Step 10 — Return CS post-release confirmation report

Mirrored on the Paper 2 post-merge confirmation report. CS returns:

```
1. release commit SHA
2. tag object SHA
3. tagged commit SHA
4. tagged manuscript blob SHA
5. confirmation tag blob == main blob (no divergence)
6. confirmation Senior C1/C3 patterns preserved (lock-before-data-access ordering)
7. confirmation no candidate / threshold / run authorized by release
8. confirmation all 10 CS-RELEASE-CONSISTENCY-CHECKLIST items still PASS post-commit
9. release-record file path
```

---

## Open findings and disposition (from CS-RELEASE-CONSISTENCY-CHECKLIST)

| ID | Finding | Disposition |
|---|---|---|
| F1 | Senior's RC manifest §2 has pre-correction md/pdf hashes; needs refresh | Recommend: Senior refresh manifest §2 with the post-correction hashes (or Manager authorization references the CS-attested corrected hashes in this procedure as binding). Either path lets the commit proceed. |
| F2 | `fitz` geometry check for right-margin overflow not performed | Recommend Senior visual confirmation of the PDF in lieu of programmatic check. If Manager wants the strict `fitz` check, defer commit until check completes. |

Neither F1 nor F2 is a content blocker.

---

## What this procedure does NOT do

- Does not select a candidate or set any threshold value.
- Does not authorize any run, re-run, INT8/INT4 execution, or multi-model
  execution.
- Does not introduce any candidate threshold sheet or certification result.
- Does not modify `tier0-run/` artifacts (post-release `EXPERIMENT_LOG.md`
  update is documentation-only per the established seal carve-out).
- Does not modify Paper 2's v1.0 release surface.
- Does not reactivate Fork A or activate Claim C.

---

## Non-authorizations (carried forward)

```
candidate selection · threshold values · certification evaluation
new runs · re-runs beyond authorized reproduction validation
unconditioned token-prior runs · activation logging
INT8 / INT4 execution · multi-model execution
Fork A reactivation · Claim C activation
Paper 3 execution as an experiment · Paper 6 activation
public benchmark packaging · artifact mutation
```

---

— CS Engineer, 2026-06-10
