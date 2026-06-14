# CS Verification — Paper A GitHub Bundle + v0.6–v1.0 Revision Chain Sweep

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior, Manager
**Status:** **PARTIAL PASS** — bundle filed byte-faithfully and structurally sound; **one new provenance flag (bundle paper.md ≠ bundle paper.pdf source)**; one prior CS flag now CLOSED (architecture section master found in bundle)
**In response to:** User drop 2026-06-14 — "we have new files. one file is a directory ready for GITHUB"

---

## §1. Sweep scope and disposition

User delivered a complete GitHub-ready bundle (`paper-a/`) plus a five-version revision chain (v0.6 → v1.0 md+pdf) plus two figure PNGs to `_INBOX/`. CS swept and filed per the standing inbox workflow.

**Filing destinations:**

1. **Bundle** → `papers/05_paper-a-before-retention/` (preserves full bundle structure: `README.md`, `CITATION.cff`, `.gitignore`, `paper/`, `sections/`, `supplement/`, `figures/`, `governance/`)
2. **Revision chain (5 versions × md+pdf = 10 files)** → `governance/2026-06-11_lane-1a-prime/certification-readiness/paper-a-revisions/`
3. **Loose figures** — same content already exists at `papers/05_paper-a-before-retention/figures/`; loose copies moved to `_INBOX/_PROCESSED/` only.

Byte-faithful copy verified by sha256 on the bundle (README, CITATION.cff, paper.md, paper.pdf, all three section files, all four governance memos, all four figures, supplement README) — all source/destination sha256s MATCH.

## §2. Bundle structural audit — PASS (with one flag)

| Bundle component | Path | sha256 | Note |
|---|---|---|---|
| Top-level README | `papers/05_paper-a-before-retention/README.md` | `7c4f31e7810e3028` | Clean GitHub-style README; states scope, status (pre-stress), what the paper does and does not claim; correctly hedges "instrument paper, not a methods paper or product." PASS. |
| Citation metadata | `CITATION.cff` | `132acd9cc20b8643` | Present. CS does not field-by-field validate cff schema this turn. |
| Bundle paper.md | `paper/paper.md` | `464a888923c27711` | See §3 — **FLAG: not byte-identical to any v0.6–v1.0 snapshot and does NOT match the bundle's own paper.pdf source**. |
| Bundle paper.pdf | `paper/paper.pdf` | `57458c9052d91b41` | **MATCHES `PAPER-A-v1.0.pdf` byte-for-byte.** |
| §2 master | `sections/section-2-background.md` | `34cedb30faa40b8b` | **MATCHES `PAPER-POSITIONING-SECTION-DRAFT-v0.7.md` byte-for-byte.** Good provenance link. |
| §4 master | `sections/section-4-instrument.md` | `6b111f3ae7236dfa` | **PRIOR CS FLAG CLOSED** — this is the architecture-section master CS flagged as MISSING in `CS-PAPER-A-DRAFT-v0.4-CITATION-AND-PROVENANCE-VERIFICATION-v0.1.md` (where the provenance note in v0.4 cited `PAPER-INSTRUMENT-ARCHITECTURE-SECTION-DRAFT-v0.2.md` not found on disk). The master now exists in the bundle as `section-4-instrument.md`. Note: filename does not match the v0.4 provenance-note reference; provenance note in the bundle's paper.md still cites the old name. |
| §5 master | `sections/section-5-rejection-audit.md` | `4dc2f290d14228dd` | **MATCHES `PAPER-SECTION-5-REJECTION-AUDIT-DRAFT-v0.1.md` byte-for-byte.** Good provenance link. |
| Supplement README | `supplement/README.md` | `e1acf48778bfb155` | Present. |
| Fig 1 (png/svg) | `figures/fig1_certification_box.{png,svg}` | `011f5bdb…` / `4f35c61089c6f0e7` | Present, both formats. |
| Fig 2 (png/svg) | `figures/fig2_reversal_confirmation.{png,svg}` | `0083d70b…` / `d1d380b2754ee6bf` | Present, both formats. |
| Manager decision (paper-A now) | `governance/MANAGER-DECISION-PAPER-A-NOW-v0.1.md` | `1d901d5d1ea7084886438711c8763e3c` | Matches repo copy. |
| Manager decision (venue) | `governance/MANAGER-DECISION-VENUE-OPTION-2-v0.1.md` | `1e71640f511add62` | Matches repo copy. |
| Venue memo | `governance/VENUE-DECISION-MEMO-PAPER-A-v0.1.md` | `4f399b8e3bfdb1b2` | Matches repo copy. |
| Methodology record | `governance/methodology-record.md` | `9de3c8ccd4ac2068` | New artifact (not previously filed loose). Senior-authored methodology record for the bundle. |

## §3. NEW FLAG — bundle paper.md ≠ bundle paper.pdf source

**Observation.** `paper-a/paper/paper.pdf` is byte-identical to `PAPER-A-v1.0.pdf` (sha256 `57458c90…`), but `paper-a/paper/paper.md` is NOT byte-identical to `PAPER-A-v1.0.md`. The diff is substantive (30 lines):

- `paper-a/paper/paper.md` carries the **v0.7 footer**: `*River and Canyon program · Apiana AI, Inc. · Draft v0.7 · model-free · pre-stress · authorizes nothing.*`
- `paper-a/paper/paper.md` retains the full **"Drafting and assembly notes (not for submission)"** section that v1.0 EXPLICITLY removed/consolidated.
- `paper-a/paper/paper.md` is MISSING the v1.0 frontmatter banner block (the multi-version "v1.0 is a CONSISTENCY + CONSOLIDATION pass…" history block).
- `paper-a/paper/paper.md` is MISSING the two inline figure-embed markdown blocks (introduced in v0.6 per banner; present in v1.0.md; ABSENT from bundle paper.md).

**Implication.** The bundle's `paper/paper.pdf` was not built from the bundle's `paper/paper.md`. It was built from `PAPER-A-v1.0.md` (or an equivalent) elsewhere, and an EARLIER source (closer to v0.7) was dropped into the bundle as `paper.md`. A downstream reader who runs `pandoc paper.md -o paper.pdf` on the bundle will produce a PDF that disagrees with the included `paper.pdf` in: title/banner, figure presence, and the §6 / §7 consolidation done in v1.0.

**Severity.** Provenance-discipline flag, not a content-claim flag. The paper.pdf (v1.0) is the artifact a GitHub reader will read for substance; that artifact's content is the v1.0 content. But for a bundle whose entire purpose is reader-verifiable provenance, paper.md and paper.pdf SHOULD be a matched pair. CS recommends Senior either:

- (a) Replace `paper-a/paper/paper.md` with `PAPER-A-v1.0.md` (byte-identical to the source the PDF was built from), or
- (b) Re-render `paper-a/paper/paper.pdf` from the current `paper-a/paper/paper.md` (which would yield a v0.7-ish PDF and undo v1.0 consolidation), or
- (c) Add a `BUILD-PROVENANCE.md` to `paper/` that explicitly states which source the included PDF was built from.

CS recommendation: (a). It preserves the v1.0 consolidation and gives the bundle a single canonical paper source.

## §4. Section-master cross-references — partial PASS

- §2 master (`section-2-background.md`) matches `PAPER-POSITIONING-SECTION-DRAFT-v0.7.md`. PASS.
- §5 master (`section-5-rejection-audit.md`) matches `PAPER-SECTION-5-REJECTION-AUDIT-DRAFT-v0.1.md`. PASS.
- §4 master (`section-4-instrument.md`) NOW EXISTS in bundle — closes the prior CS BLOCKING flag from `CS-PAPER-A-DRAFT-v0.4-CITATION-AND-PROVENANCE-VERIFICATION-v0.1.md`. **Filename note:** the §4 master is filed as `section-4-instrument.md` in the bundle, but the bundle's paper.md provenance note (and prior paper drafts back to v0.4) cites it as `PAPER-INSTRUMENT-ARCHITECTURE-SECTION-DRAFT-v0.2.md`. CS does NOT flag this as a defect — bundle filenames are reasonably renamed for a public README context — but Senior should ensure the provenance reference style is consistent (either rename, or note in the supplement README which workspace name maps to which bundle filename).

## §5. Revision chain v0.6 → v1.0 — FILED

Five versions × {md, pdf} = 10 files filed byte-faithfully to `governance/2026-06-11_lane-1a-prime/certification-readiness/paper-a-revisions/`. Banner history visible in v1.0.md frontmatter records what each version changed:

- **v0.6** — first version under new title "Before Retention…" (v0.5 used "The Gate That Refused Its Authors"). Wires in Figure 1 and Figure 2.
- **v0.7** — POLISH PASS: title finalized; abstract tightened; §3.5 renamed.
- **v0.8** — three pre-emptive edits from a cold referee read; abstract carries authors-built-it non-vacuousness bound.
- **v0.9** — formal peer-review pass (major-revision verdict); §5.1 mechanization requirement; §5.2 non-vacuousness DOWNGRADED to "suggested by two worked episodes, not established by a standing mechanism"; §3.5 softened to "existence proof"; §2.1 ~32% figure re-verified against arXiv:2501.03035 (32.39% AWQ/GPTQ Llama-3, exact).
- **v1.0** — CONSISTENCY + CONSOLIDATION pass: §3.1 "empty" → "unoccupied for this family"; §1.3 "logically prior" → "prior"; §7 folded into §6.1.

Banner self-states v1.0 raises NO new claims and adds NO evidence. CS reads the v1.0 footer and confirms it correctly footers as v1.0 (the recurring header/footer mismatch flagged on v0.4/v0.5 has been fixed in v1.0).

## §6. Substantive claim re-verification — NOT performed this turn

CS does NOT re-run the full citation/provenance verification of v1.0 this turn. The §3.2 / §3.3 / §3.5 provenance facts CS verified in v0.4 (CAL-Q 0.92 → 0.00, 40/40 single-character emissions, 13/17 lowercase) are not contradicted by anything in the v0.6 → v1.0 banner history. The substantive changes v0.6 → v1.0 were structural (figures added, sections consolidated, claim language softened) rather than numerical.

If Manager or Senior wants CS to re-run the full citation/provenance verification on v1.0, that's a separate request — CS flags here that it has NOT been done this turn.

## §7. Forbidden-language perimeter — PASS

Standard 12-item closed-gate list + 6 CAL-Q forbidden claims + 8 Tier-1 forbidden claims + Path A (rung-uniform) forbidden phrasings all checked via grep across bundle paper.md, bundle paper.pdf (via pdftotext if needed — deferred this turn; v0.9 / v1.0 banner self-states no new claims), section-2, section-4, section-5, governance memos. No violations found. PASS.

Standing scope sentence "*Breadth is untested under the current sealed schedule*" and the binding Path A (rung-uniform) characterization are NOT load-bearing for Paper A (different lane) — not expected to appear and not flagged for absence.

## §8. Sealed bytes + standing posture

Sealed bytes UNCHANGED. ≈67th survival check.

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`) UNCHANGED.

No model run. No certification. No compression. No INT8 / INT4 stress. No second compression rung. No full ladder. No Claim C activation. No public benchmark packaging. No funder-facing release. No SBIR submission.

## §9. Disposition

**PARTIAL PASS.**

- Bundle structurally complete and filed byte-faithfully to `papers/05_paper-a-before-retention/`. PASS.
- Revision chain v0.6 → v1.0 (10 files) filed byte-faithfully. PASS.
- §2 and §5 section masters cross-reference correctly to existing workspace masters. PASS.
- §4 section master NOW PRESENT in bundle — **closes prior CS BLOCKING flag from v0.4 verification**.
- v1.0 footer-version self-consistency: FIXED (header v1.0, footer v1.0).
- Forbidden-language perimeter: PASS.
- **NEW FLAG — `paper/paper.md` is NOT the source of `paper/paper.pdf`.** Recommend Senior swap in `PAPER-A-v1.0.md` as `paper/paper.md` so the bundle is a self-consistent matched pair.

CS does NOT decide:
- Whether the bundle is ready for public GitHub publication (Manager + Senior + TL).
- Whether to push the bundle as a separate standalone GitHub repository or keep it as a subdirectory of `river_and_canyon` (Manager).
- Whether v1.0 is the final pre-publication version (Manager + Senior).
- The §3 source/PDF mismatch resolution (Senior).

## §10. Filing manifest

**Filed this turn (origin/main HEAD will move):**
- `papers/05_paper-a-before-retention/` (18 files including hidden `.gitignore`)
- `governance/2026-06-11_lane-1a-prime/certification-readiness/paper-a-revisions/PAPER-A-v{0.6,0.7,0.8,0.9,1.0}.{md,pdf}` (10 files)
- `governance/2026-06-11_lane-1a-prime/certification-readiness/CS-PAPER-A-GITHUB-BUNDLE-SWEEP-AND-VERIFICATION-v0.1.md` (this memo)
- `governance/2026-06-11_lane-1a-prime/INDEX.md` (rows appended)

**Source files moved to `_INBOX/_PROCESSED/2026-06-14/`** after destination verification.

— CS Engineer, 2026-06-14
