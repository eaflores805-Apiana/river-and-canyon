# Artifact Bundle — Index and Provenance Manifest

*Supplementary material for* **"Survival Is Not Correctness: A Staged, Fail-Closed Metrology Protocol
for Stress-Retention Evaluation."** This index catalogs the artifacts that accompany the manuscript,
records the provenance status of each, and identifies which run-artifact files must be attached from the
run environment. Provenance is reported as disclosed in the manuscript (§5.1, Appendix A): documented
gaps are stated rather than smoothed, and nothing here is reconstructed where the source artifact is
absent.

---

## A. Manuscript and figures (included; stable paths)

| File | Path | Description | Status |
|---|---|---|---|
| Manuscript (Markdown) | `survival-is-not-correctness.md` | Source manuscript | Included |
| Manuscript (PDF) | `survival-is-not-correctness.pdf` | Rendered manuscript (16 pp.) | Included |
| Figure 1 | `assets/fig_scorer.png` | Three-axis scoring of one output (§4) | Included |
| Figure 2 | `assets/fig_ladder.png` | Staged, fail-closed protocol; HALT at FP16 gate (§5) | Included |
| Figure 3 | `assets/fig_collapse.png` | Exp3 strict vs content interval (§7) — exact Exp3 CI values | Included |
| Figure 4 | `assets/fig_scaffold.png` | Exp5 strict-interval-vs-zero under a changed scaffold (§7) — **non-bar qualitative schematic, no numeric scale** | Included |
| Figure 5 | `assets/fig_discriminator.png` | Discriminator roadmap, *roadmap-not-result* (§9) | Included |

The PDF is built from the Markdown plus the five figure PNGs; all five PNGs are required to reproduce the
PDF.

---

## B. Data reproduced inline in the manuscript (no separate file required)

These artifacts are reproduced in full in the manuscript and need no supplementary navigation:

- **Dummy-baseline per-condition breakdown** — Appendix A, **Table A.1** (eight conditions; worst-case
  0.375 vs the 0.875 feasibility gate).
- **Exp8A → Exp8B paired transition matrix** — §7.1, **Table T4** (n=8; five stable, one rescued, one
  migrated, one destabilized).
- **Content/format scorer logic** — Appendix A scorer snippet (`FORMAT_PASS` regex, nine-class content
  priority, scaffold-detection rule, amendment history).
- **Bit-depth and decoding provenance** — §5.1, **Table P1** and **Table P2**.

---

## C. Known artifact hashes (verified present)

| Item | Hash | Source / scope |
|---|---|---|
| Exp7 manifest | `sha256:177c5f7f1fa39d902fafe4974e5d449f005e6200fe5101efb54b25186096f20e` | Artifact-backed (Exp7) |
| Scorer (`tasks_exp8.py`) | `sha256:4036b1ad0819be74e32521cea8f9117b503c6d9d79142969820175ecde95a1bc` | Dummy-baseline validation source (Table A.1), executed 2026-06-07 |

---

## D. Run-artifact files to attach from the run environment

The following are **data/source files held in the run environment**; they are not reproducible from the
manuscript and must be attached directly from their source. They are listed with stable target paths so
they slot into the bundle predictably. **None of these is generated here**; where a file does not exist or
a field was never recorded, the gap is documented in §E rather than filled.

| Target path | Contents | Availability |
|---|---|---|
| `artifacts/exp8a/raw_outputs.json` | Exp8A raw model outputs (incl. `L2_02 = "ANSWER: 0"`, `L2_03 = "ANSWER: 10"`, recorded `UNCLASSIFIED`) | To attach from run environment |
| `artifacts/exp8b/raw_outputs.json` | Exp8B raw model outputs (transition-matrix source) | To attach from run environment |
| `artifacts/exp6/raw_outputs.json` | Exp6 raw model outputs | To attach from run environment |
| `artifacts/exp7/raw_outputs.json` | Exp7 raw model outputs | To attach from run environment |
| `artifacts/manifests/` | Per-run manifest files | To attach from run environment (Exp7 manifest hash in §C; see §E for gaps) |
| `src/tasks_exp8.py` | Task construction + `validate_tasks()` + scorer | To attach from run environment (scorer hash in §C) |
| `logs/` | Supplementary run logs referenced by Appendix A, where they exist | To attach from run environment |

---

## E. Documented provenance gaps (not recoverable; disclosed)

Per the manuscript (§5.1, Appendix A), the following are documented gaps. Affected runs are **not**
presented as fully reproducible.

- **Exp6:** `tokenizer_hash`, `runner_hash`, `scorer_hash` were not stored and **cannot be recovered
  post-hoc**. Tokenizer identity is by model tag only; decoding (`temperature 0.0, max_tokens 512`) is
  reconstructed from runner source. Exp6 manifest hash is **not** artifact-backed.
- **Exp7:** `tokenizer_hash`, `runner_hash`, `scorer_hash` were not stored and **cannot be recovered
  post-hoc**. Decoding (`temperature 0.0, max_tokens 512`) is reconstructed from runner source. The
  **manifest hash is artifact-backed** (§C).
- **Exp8A (pre-amendment):** predates the locked three-axis scorer; the pre-amendment two-axis
  `scorer_hash` was not recorded and **cannot be recovered**, `scaffold_class` is **absent** from all
  items, and Exp8A was **not rescored**. Its decoding (`temperature 0.0, max_tokens 16`) **is**
  artifact-stored. Numeric items (`ANSWER: 0`, `ANSWER: 10`) retain the artifact label `UNCLASSIFIED`;
  the later `DEGENERATE_NONCONTEXT` / `RETURNED_NON_CONTEXT_TOKEN` classes postdate the run and were not
  applied to it.

---

## F. Naming and path stability

Bundle layout (stable):

```text
/  (bundle root)
├── survival-is-not-correctness.md
├── survival-is-not-correctness.pdf
├── assets/fig_scorer.png
├── assets/fig_ladder.png
├── assets/fig_collapse.png
├── assets/fig_scaffold.png
├── assets/fig_discriminator.png
├── artifact-bundle-index.md      (this file)
├── artifacts/                    (run-artifact files — §D, attach from source)
├── src/                          (task/scorer source — §D, attach from source)
└── logs/                         (run logs — §D, where they exist)
```

Manuscript and figure filenames are final and must not be renamed; references in the manuscript and in
this index assume these exact names. The `artifacts/`, `src/`, and `logs/` paths are reserved targets for
the run-environment files in §D.
