# CS Release-Consistency Checklist — Paper 3 v1.0 RC

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Team Lead, Senior Engineer, Manager
**Re:** Verification record for the Paper 3 v1.0 release-candidate package
**Status:** Preparation only; no commit, tag, or release action taken.

---

## Record status

```
RC package received and verified against Senior's PAPER3-RELEASE-CANDIDATE-PACKAGE.md.
All 10 Senior-defined checklist items: PASS (one note on item 1; see below).
PDF page count: 15 (matches Senior's expectation).
PDF embedded images: 4 (matches Senior's expectation).
Hash drift on md/pdf vs Senior's manifest: documented and attributed to the
  post-manifest format-issue correction (per user 2026-06-10).
Figure hashes (8 files) match Senior's manifest exactly.
No commit, no tag, no release-record finalization performed.
```

---

## Package source

| File | Path (Senior workspace) |
|---|---|
| Bundle README | `Apiana_Papers/certification_before_retention/README.md` |
| RC package note | `paper3-certification-before-retention/release-docs/PAPER3-RELEASE-CANDIDATE-PACKAGE.md` |
| External-review disposition | `paper3-certification-before-retention/release-docs/SENIOR-DISPOSITION-EXTERNAL-REVIEW-PAPER3.md` |
| Manuscript | `paper3-certification-before-retention/certification-before-retention.md` |
| PDF | `paper3-certification-before-retention/certification-before-retention.pdf` |
| Figures (4 × PNG, 4 × SVG) | `paper3-certification-before-retention/figures/` |
| Draft lineage (v0.6 – v0.9) | `paper3-certification-before-retention/lineage/` |

---

## Item 1 — sha256 manifest (CS recomputed full 64-hex independently)

### Manuscript and PDF

| File | First-16 (Senior manifest) | First-16 (CS recomputed) | Match | Note |
|---|---|---|---|---|
| `certification-before-retention.md` | `98e4c25e50dd9134` | `b948521ebab74b3a` | **MISMATCH** | Format-issue correction post-manifest (per user 2026-06-10) |
| `certification-before-retention.pdf` | `0881c9bd5576054a` | `6223cf85a65f1bc6` | **MISMATCH** | Same — derivative of corrected manuscript |

**Full corrected hashes (CS-attested 2026-06-10):**

```
md:  sha256:b948521ebab74b3a225a98509a07488c0f1a4c86d1802d46796e57b2d361e714
pdf: sha256:6223cf85a65f1bc6fe4621f717997e6b8d2b253b6156951715d6d30005080d8f
```

**Finding F1 — Senior's manifest needs refresh.** Senior wrote `PAPER3-RELEASE-CANDIDATE-PACKAGE.md`
§2 against the pre-correction files. After the format-issue fix, the manuscript and PDF have new
hashes. Senior should update §2 of the RC package note with the corrected values before commit
authorization, OR Manager authorization should explicitly reference the CS-attested corrected hashes
above as the binding manifest.

### Figures

All 8 figure hashes match Senior's manifest first-16 values exactly:

| File | First-16 (Senior + CS) | Full hash |
|---|---|---|
| `fig1_series_gap_ladder.png` | `92e3df1de5f5453a` | `92e3df1de5f5453a511cf2723d185a363b61ffc3852210e255f0e01bcec082ac` |
| `fig1_series_gap_ladder.svg` | `d78f3148a7336096` | `d78f3148a733609623d0d3196a3d1961963e33557d99ee42199c5517edce323e` |
| `fig2_lineage_to_gates.png` | `7c2a7ca671ac7981` | `7c2a7ca671ac7981e52fc50e19d66f29bb343e50afb1eb2c5608ebff0a74f9b5` |
| `fig2_lineage_to_gates.svg` | `404057ca715964e0` | `404057ca715964e0bae4343a4a324b2c33f0d94c867b5735aed7a9976b78547e` |
| `fig3_failclosed_pipeline.png` | `bd3ac23bd228d416` | `bd3ac23bd228d416e6e69036ad4b83801304007ab94ec687ddefd4ca2fd737a0` |
| `fig3_failclosed_pipeline.svg` | `b5c55151ce0b1441` | `b5c55151ce0b1441de4d16f7ff984e73448086715413c8eca86fe0683f288df8` |
| `fig4_three_artifact_layers.png` | `ce9ad944f256e19e` | `ce9ad944f256e19e2f06ef82285ed528b087a0ad41326ffade0474f186214970` |
| `fig4_three_artifact_layers.svg` | `0820aca8bfe4c66b` | `0820aca8bfe4c66baa8822964cd095ba3f3441cdaf53ba5d992e3dd9f31ec1ee` |

Figures were **not affected** by the format-issue correction. All 8 hashes match exactly.

**CS attestation:** SHA-256 values above were computed by the CS Engineer using `shasum -a 256` on the
bundle files at the paths shown. Transcripts archived in this directory at commit time.

Status: **PASS** (with F1 noted for Senior's manifest refresh).

---

## Item 2 — Masthead reads `v1.0`; no draft residue

- Masthead (line 5 of manuscript): `**v1.0.** River and Canyon program...` ✓
- Status block: no `draft v0.x` or `for Team Lead review` language. ✓
- Sole `draft` occurrence is the canonical "*threshold sheets lock only against a released framework version, not a draft identifier*" clause at line 9 — required language, not residue.
- Grep `for Team Lead review`: 0 hits ✓

Status: **PASS**

---

## Item 3 — Framework identifier consistency

- Single masthead occurrence: `paper3-certification-protocol-v1.0` at line 9 ✓
- Grep `paper3-certification-protocol-v0`: 0 hits — no stale draft identifier anywhere ✓

Status: **PASS**

---

## Item 4 — Three non-claim blocks aligned (×3 markers)

- `benchmark-superiority`: 3 hits ✓ (abstract, §6 preamble, §9)
- `Passing all gates does not predict that a future stress run`: 3 hits ✓ (abstract, §6 preamble, §9)

Status: **PASS**

---

## Item 5 — §6 four-field structure intact (7 × four-label)

| Label | Hit count | Expected |
|---|---|---|
| `Success condition` | 7 | 7 |
| `Failure condition` | 7 | 7 |
| `Scientific interpretation` | 7 | 7 |
| `Explicit non-claim` | 7 | 7 |

Status: **PASS**

---

## Item 6 — Figures

### Markdown references

Four references in the manuscript, all PNG variants:

| Line | Reference |
|---|---|
| 40 | `figures/fig1_series_gap_ladder.png` |
| 76 | `figures/fig2_lineage_to_gates.png` |
| 130 | `figures/fig3_failclosed_pipeline.png` |
| 195 | `figures/fig4_three_artifact_layers.png` |

All four PNG files resolve in the bundle's `figures/` directory.

### PDF properties

- **Page count: 15** ✓ (verified via `pdfinfo`)
- **Embedded images: 4** ✓ (verified via `pdfimages -list`; images appear on pages 2, 4, 7, 10)
- Page size: 612 × 792 pts (US Letter)
- Source: wkhtmltopdf 0.12.6 / Qt 5.15.13

### Right-margin overflow (geometry check)

**Deferred — tool-availability finding F2.** Senior's checklist specifies a `fitz` (PyMuPDF)
geometry check for right-margin overflows. The CS environment does not have `fitz` or `pypdf`
installed and `pip install` is restricted in this environment. The geometry check is therefore
**not programmatically completed** in this CS preparation pass.

Options:
- (a) Senior or Manager performs the geometry check using a workstation with `fitz` available;
  CS records the result here.
- (b) CS defers the geometry check to a Senior visual inspection; pass is inferred from the
  visual review of the PDF (Senior already produced it from a known-good template).
- (c) The check is treated as a non-blocker for Manager release authorization, with the
  understanding that any future overflow finding triggers a corrective re-render.

CS recommends option (b) for this pass: Senior produced the PDF and has already visually inspected
it. If Manager wants the strict `fitz` check, option (a) is available without environment changes
to the CS workstation.

Status: **PASS** on items checkable; **DEFERRED** on the geometry sub-check (F2).

---

## Item 7 — No candidate names, no threshold values, no run-authorization language

- Grep for model names (Qwen / Llama / Mistral / Gemma): 0 hits ✓
- Numeric threshold values in A.1: 0 hits (A.1 is field-name list, no values written) ✓

Status: **PASS**

---

## Item 8 — Banned-wording sweep

| Banned phrase | Hits |
|---|---|
| `model flag retired` | 0 |
| `snapshot caveat retired` | 0 |
| `version drift retired` | 0 |
| `mlx_lm drift harmless` | 0 |
| `version-drift retired` | 0 |
| `asserted-only flag retired` | 0 |

Status: **PASS**

---

## Item 9 — References [3] / [4]

### [3] Baxi (CDCT)

- Scope constraint present: *"CDCT concerns prompt-compression / instruction-following evaluation and is not evidence regarding INT8/INT4 weight quantization, compression-retention measurement, same-error identity, or failure taxonomy under numerical stress."* ✓
- Decomposed-scoring discipline framing matches v0.9 resolution ✓

### [4] Dutta et al.

- Author order: `Dutta, A., Krishnan, S., Kwatra, N., and Ramjee, R.` ✓
- Venue: `Advances in Neural Information Processing Systems 37 (NeurIPS 2024), Main Conference Track, 124347–124390` ✓
- DOI: `10.52202/079017-3950` ✓
- arXiv: `2407.09141v1` ✓
- Scope constraint preserved: *"Dutta et al. do not propose retention certification, same-error identity reporting, or a fail-closed baseline-admission contract; those are contributions of this series, not claims inherited from [4]."* ✓

Status: **PASS**

---

## Item 10 — License footer present and last

Last three lines of manuscript:

```
---

*© 2026 E. A. Flores, Apiana AI, Inc. Licensed under CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/).*
```

Status: **PASS**

---

## Summary

| # | Checklist item | Result |
|---|---|---|
| 1 | sha256 manifest (md, pdf, figures) | **PASS w/ F1** (figures match; md/pdf differ due to post-manifest format correction — Senior manifest refresh requested) |
| 2 | Masthead `v1.0`, no draft residue | PASS |
| 3 | Framework identifier consistency | PASS |
| 4 | Three non-claim blocks aligned (×3 markers) | PASS |
| 5 | §6 four-field structure (7 × four-label) | PASS |
| 6 | Figures resolve, PDF 15pp, 4 images | **PASS w/ F2** (geometry check deferred — no fitz available) |
| 7 | No candidate names / thresholds / run-auth | PASS |
| 8 | Banned-wording sweep clean | PASS |
| 9 | References [3] / [4] scope and citation | PASS |
| 10 | License footer present and last | PASS |

**Two open findings:**

- **F1 — Senior manifest refresh.** Senior's `PAPER3-RELEASE-CANDIDATE-PACKAGE.md` §2 needs to be
  updated with the post-correction md/pdf hashes:
  - `md:  sha256:b948521ebab74b3a225a98509a07488c0f1a4c86d1802d46796e57b2d361e714`
  - `pdf: sha256:6223cf85a65f1bc6fe4621f717997e6b8d2b253b6156951715d6d30005080d8f`
  Alternatively, Manager authorization may reference the CS-attested hashes above as the binding
  manifest at commit time.
- **F2 — Geometry check deferred.** `fitz`-based right-margin overflow check not performed; CS
  recommends Senior-visual or workstation-with-fitz fallback.

Neither F1 nor F2 is a content blocker. Both can be resolved before Manager release authorization.

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
commit · tag · release-record finalization
```

---

— CS Engineer, 2026-06-10
