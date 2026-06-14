# Paper 3 v1.0 Release Record

**Date:** 2026-06-10
**Paper:** *Certification Before Retention: A Fail-Closed Protocol for Qualifying a Single-Hop Baseline as a Strict-Correctness Retention Substrate*
**Tag:** `paper3-certification-protocol-v1.0`

---

## Tag identifiers

| Field | Value |
|---|---|
| Tag name | `paper3-certification-protocol-v1.0` |
| Tag object SHA | `6dbdcc1238a186af32baac076d3d82c92fd7c205` |
| Tagged commit SHA | `63d217216752f833b257d426665c872a21c5f422` |
| Tagged manuscript blob (git, 40-hex) | `798f7dceacf7ea05630009d80106a6dbff47b031` |
| Tagged manuscript content sha256 | `b948521ebab74b3a225a98509a07488c0f1a4c86d1802d46796e57b2d361e714` |

The tag name matches the lock-eligible framework identifier byte-for-byte
(`paper3-certification-protocol-v1.0`). Future threshold sheets can name the
released framework and the release tag with the same string in
`framework_version`.

---

## Paper 2 lesson incorporation — verified

Paper 2 v1.0 had post-tag manuscript edits (status-label flip in commit
`69df8be` and PDF rebuild in `894140c`) that produced on-main-vs-tagged blob
divergence. The lock note for Paper 2 documents this honestly but it complicated
the audit trail.

Paper 3 v1.0 explicitly avoided this. The RC text is the final v1.0 text; the
commit that landed the manuscript IS the commit that was tagged; no post-tag
edits to the manuscript file are authorized.

**Verification at release time:**

```
Tagged manuscript blob: 798f7dceacf7ea05630009d80106a6dbff47b031
Main manuscript blob:   798f7dceacf7ea05630009d80106a6dbff47b031
Match: YES — no divergence
```

---

## Manifest of released files (10 files, full 64-hex sha256)

```
papers/paper3-certification-before-retention/
  certification-before-retention.md
    sha256:b948521ebab74b3a225a98509a07488c0f1a4c86d1802d46796e57b2d361e714
  certification-before-retention.pdf
    sha256:6223cf85a65f1bc6fe4621f717997e6b8d2b253b6156951715d6d30005080d8f
  figures/fig1_series_gap_ladder.png
    sha256:92e3df1de5f5453a511cf2723d185a363b61ffc3852210e255f0e01bcec082ac
  figures/fig1_series_gap_ladder.svg
    sha256:d78f3148a733609623d0d3196a3d1961963e33557d99ee42199c5517edce323e
  figures/fig2_lineage_to_gates.png
    sha256:7c2a7ca671ac7981e52fc50e19d66f29bb343e50afb1eb2c5608ebff0a74f9b5
  figures/fig2_lineage_to_gates.svg
    sha256:404057ca715964e0bae4343a4a324b2c33f0d94c867b5735aed7a9976b78547e
  figures/fig3_failclosed_pipeline.png
    sha256:bd3ac23bd228d416e6e69036ad4b83801304007ab94ec687ddefd4ca2fd737a0
  figures/fig3_failclosed_pipeline.svg
    sha256:b5c55151ce0b1441de4d16f7ff984e73448086715413c8eca86fe0683f288df8
  figures/fig4_three_artifact_layers.png
    sha256:ce9ad944f256e19e2f06ef82285ed528b087a0ad41326ffade0474f186214970
  figures/fig4_three_artifact_layers.svg
    sha256:0820aca8bfe4c66baa8822964cd095ba3f3441cdaf53ba5d992e3dd9f31ec1ee
```

Note (per Manager 2026-06-10 release authorization §"The release record should
note"): *"The package note uses shortened manifest display values; full 64-hex
SHA-256 verification transcripts are recorded in the CS release-consistency
checklist. The corrected manuscript/PDF hashes were independently recomputed by
Senior and CS and matched."*

---

## Pre-release verification chain

### CS release-consistency checklist (2026-06-10)

10 Senior-defined items, all PASS:

| # | Item | Result |
|---|---|---|
| 1 | sha256 manifest (10 files) | PASS (CS-attested full 64-hex; figures match Senior manifest; md/pdf hashes drifted due to post-manifest format-issue correction, resolved via Senior manifest refresh) |
| 2 | Masthead `v1.0`, no draft residue | PASS |
| 3 | Framework identifier `paper3-certification-protocol-v1.0` consistency | PASS |
| 4 | Three non-claim blocks aligned (×3 union markers) | PASS |
| 5 | §6 four-field structure (7 × four-label) | PASS |
| 6 | Figures resolve, PDF 15pp, 4 embedded images | PASS |
| 7 | No candidate names / thresholds / run-authorization | PASS |
| 8 | Banned-wording sweep clean | PASS |
| 9 | References [3] / [4] scope and full citation | PASS |
| 10 | License footer present and last | PASS |

Full transcript: `CS-RELEASE-CONSISTENCY-CHECKLIST.md` (this directory).

### Senior dispositions on findings

| Finding | Disposition | Outcome |
|---|---|---|
| F1 — hash drift on md/pdf | Senior refreshed `PAPER3-RELEASE-CANDIDATE-PACKAGE.md` §2 with corrected first-16 values | CLEARED. CS-attested full 64-hex values match Senior recomputation character-for-character. |
| F2 — PDF geometry check | Senior performed programmatic `fitz` geometry verification AND visual 15-page PDF confirmation (consistent margins, no edge-touching, all four figures properly scaled, appendix code blocks within margins, no clipping, license footer closes page 15 correctly) | CLEARED. Zero overflows. |

---

## Authorization chain

```
Manager / Elias, 2026-06-10:
  "Manager authorization is granted to execute the prepared Paper 3 v1.0
   release procedure. Authorized tag name: paper3-certification-protocol-v1.0."

Team Lead, 2026-06-10:
  - Recommended tag `paper3-certification-protocol-v1.0` (endorsed by Senior).
  - Confirmed F1 cleared (Senior manifest refresh; CS attestation matched).
  - Confirmed F2 cleared (Senior fitz + visual confirmation).
  - Accepted CS release procedure in principle.

Senior Engineer, 2026-06-10:
  - Delivered RC package + final v1.0 manuscript and PDF.
  - Refreshed package manifest §2 (F1 disposition).
  - Performed programmatic + visual geometry check (F2 disposition).
  - Endorsed `paper3-certification-protocol-v1.0` as tag name.

CS Engineer, 2026-06-10:
  - Filed release-consistency checklist (10 items PASS).
  - Filed commit/tag procedure.
  - Filed release-confirmation report (pre-release).
  - Filed Senior's refreshed package note in governance.
  - Executed 10-step release procedure on Manager authorization.
```

---

## Review arc — full lineage

CS reviews of v0.2 through v1.0 filed in
`governance/2026-06-09_paper3-threshold-framework-review/`:

| File | Coverage |
|---|---|
| `CS-TECHNICAL-REVIEW-PAPER3-THRESHOLD-FRAMEWORK.md` | Senior's planning framework |
| `CS-CLASSIFICATION-PAPER3-METROLOGY-SAFEGUARDS.md` | 4 metrology safeguard items |
| `CS-REVIEW-PAPER3-DRAFT-V02.md` | v0.2 review (2 lock blockers flagged) |
| `CS-REVIEW-PAPER3-DRAFT-V03.md` | v0.3 review |
| `CS-REVIEW-PAPER3-DRAFT-V06.md` | v0.6 review (first real draft) |
| `CS-REVIEW-PAPER3-DRAFT-V07.md` | v0.7 review |
| `CS-REVIEW-PAPER3-DRAFT-V08.md` | v0.8 review |
| `CS-REVIEW-PAPER3-DRAFT-V09.md` | v0.9 review (substantive review of record) |
| `CS-REVIEW-PAPER3-V1.0.md` | v1.0 release event review |

External-review disposition (Senior-authored) archived in Senior bundle at
`Apiana_Papers/certification_before_retention/paper3-certification-before-retention/release-docs/SENIOR-DISPOSITION-EXTERNAL-REVIEW-PAPER3.md`.

Reviewed drafts (v0.6 – v0.9) archived in Senior bundle at
`Apiana_Papers/certification_before_retention/paper3-certification-before-retention/lineage/`.

---

## Release sequence executed

```
1. Stage: papers/paper3-certification-before-retention/ created with manuscript,
   PDF, and 8 figures (4 PNG + 4 SVG).
2. Pre-commit hash verify: ALL 10 files match CS-attested values.
3. Commit: 63d217216752f833b257d426665c872a21c5f422 on main.
4. Post-commit verify: manuscript blob (798f7dce...) content sha256 matches
   expected (b948521e...).
5. Tag: paper3-certification-protocol-v1.0 (annotated; tag object
   6dbdcc1238a186af32baac076d3d82c92fd7c205).
6. Post-tag blob-equality check: tagged blob 798f7dce... == main blob 798f7dce...
   → PASS (Paper 2 lesson fix verified).
7. Push: commit pushed to main; tag pushed to origin.
8. This release record filed.
9. Auxiliary docs updates: EXPERIMENT_LOG.md + memory (this commit).
10. Final confirmation report: this directory.
```

---

## Authorized release actions (this release)

```
✓ Land Paper 3 v1.0 manuscript and PDF at papers/paper3-certification-before-retention/
✓ Land 4 PNG + 4 SVG figures under papers/paper3-certification-before-retention/figures/
✓ Tag the release commit as paper3-certification-protocol-v1.0
✓ File this release record
✓ Update tier0-run/EXPERIMENT_LOG.md (documentation only; per seal carve-out)
✓ Update memory state for next CS session
```

---

## Follow-up items (not in this commit; tracked)

| Item | Owner | Status |
|---|---|---|
| Root doc refresh (README.md, REVIEW.md, STATUS.md) to reflect Paper 3 release | User (taking direct ownership 2026-06-10) | In progress outside this CS commit. Not blocking the release tag. |
| Refresh passdown letter to reflect Paper 3 release | CS | Pending; will land in passdown directory at session close |
| B1 v2.1 backlog now has concrete naming rule (`*-v0.*` draft, `*-v1.*+` released) | CS, at first candidate authorization | Future work; not authorized |

---

## Non-authorizations (carried forward)

This release does NOT authorize:

```
candidate selection · threshold-sheet population · threshold-sheet lock
certification evaluation · new runs · re-runs
INT8 / INT4 execution · multi-model execution
unconditioned token-prior runs · activation logging
Fork A reactivation · Claim C activation
Paper 3 application as an experiment · Paper 6 activation
B1 v2.1 implementation · public benchmark packaging · artifact mutation
```

Lock-eligibility of `paper3-certification-protocol-v1.0` is now a precondition
that future work may use, not an authorization.

---

— CS Engineer, 2026-06-10
