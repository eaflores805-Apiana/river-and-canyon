# Release Note — Final Package

**Paper:** *Survival Is Not Correctness: A Staged, Fail-Closed Metrology Protocol for Stress-Retention
Evaluation* (subtitle: *Lessons from a blocked seam-under-quantization test*).
**Status:** Manager-approved final. Internal "production lock candidate" status label removed from the
manuscript for external submission. Length: 16 pages.

---

## What is included (this package)

| Item | File | Notes |
|---|---|---|
| Final manuscript (Markdown) | `survival-is-not-correctness.md` | Source of record |
| Final manuscript (PDF) | `survival-is-not-correctness.pdf` | Rendered; title/figures/captions/tables/references/appendices render-checked |
| Figures (×5) | `assets/fig_scorer.png`, `assets/fig_ladder.png`, `assets/fig_collapse.png`, `assets/fig_scaffold.png`, `assets/fig_discriminator.png` | Required to rebuild the PDF; Figure 4 is a non-bar qualitative schematic |
| Artifact bundle index | `artifact-bundle-index.md` | Provenance manifest + stable paths + the run-artifact files to attach from source |

---

## Render check (PDF)

Confirmed rendering: title and subtitle; external-facing front-matter note; abstract and the
"What we do not claim" box; Figures 1–5 (visually verified, Figure 4 non-bar schematic); Tables P1, P2,
D, T4, A.1; the claim ledger; §§1–12; Appendix A (artifact record, scorer snippet, Table A.1) and
Appendix B (prior-art perimeter); and the References (four full citations, verbatim).

---

## Claims and discipline state (as approved)

- Claims match evidence. Same-error identity is **specified and operationalized**, not established as
  having adjudicated a compression-retention result.
- **No seam result** is claimed; no compositional-seam existence/non-existence claim.
- **No Track 2 result** is included; **no Track 3** material is introduced.
- **No mechanism** claim; **no general quantization-robustness** claim.
- Documented provenance gaps are **disclosed** (Exp6/Exp7 and pre-amendment Exp8A are not presented as
  fully reproducible); Exp7 manifest hash and Exp8A decoding are artifact-backed.
- Full bibliography integrated **verbatim** (Dutta et al. 2024 — *Accuracy is Not All You Need*, NeurIPS
  2024; Liu et al. 2024 — TACL; Kurtic et al. 2025 — ACL; Li et al. 2025 — arXiv:2505.11574). Earlier Li
  arXiv:2501.03035 not cited as independent support. Cautious novelty wording maintained (not "no prior
  work does this").
- Dummy-baseline decomposition is **inline** (Appendix A, Table A.1). Artifact availability and
  reproducibility notes are **external-facing** (no internal team-process language).

---

## Outstanding packaging dependency (not produced here)

One item remains before the bundle is complete, and it is outside what can be generated from the
manuscript side: the **run-artifact files** must be attached from the run environment as listed in
`artifact-bundle-index.md` §D —

- per-run raw output packets (`artifacts/<run>/raw_outputs.json`),
- per-run manifest files (`artifacts/manifests/`),
- task/scorer source (`src/tasks_exp8.py`),
- supplementary run logs (`logs/`), where they exist.

These are data/source files, not derivable from the manuscript; known hashes for the scorer and the Exp7
manifest are recorded in the index (§C), and the not-recoverable gaps are documented (§E). Once these
files are attached at their reserved paths, the bundle in the index is complete.

---

## Handoff

No further scientific edits are authorized. Maintained invariants: same-error identity = specified and
operationalized; validated components are ready to reuse; the full instrument has not produced a clean
seam measurement; documented provenance gaps remain visible. Ready for archive/submission handoff pending
attachment of the run-artifact files above.
