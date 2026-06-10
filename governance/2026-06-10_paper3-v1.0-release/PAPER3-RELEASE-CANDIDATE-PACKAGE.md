# Paper 3 — Release-Candidate Package (v1.0-rc)

*Senior Engineer, 2026-06-10. Prepared per Team Lead final readiness summary (review converged, route to
release). Commit and tag are gated on the Manager's release authorization — nothing in this package is
to land on main before that decision.*

## 1. Package contents

| File (Senior workspace) | Repo path on commit |
|---|---|
| `PAPER3-certification-before-retention-RC-v1.0.md` | `papers/paper3-certification-before-retention/certification-before-retention.md` |
| `certification-before-retention-RC-v1.0.pdf` | `papers/paper3-certification-before-retention/certification-before-retention.pdf` |
| `figures/` (4 × PNG + 4 × SVG) | already committed; unchanged by this RC |

RC deltas from reviewed v0.9 (all procedural, none substantive): masthead `Draft v0.9` → `v1.0`; status
line's draft-review clause removed; framework identifier `paper3-certification-protocol-v0.9` →
`paper3-certification-protocol-v1.0` with release semantics ("lock-eligible from the release tag
onward" replacing the draft not-lock-eligible clause); Team Lead's optional §2 smoothing applied
verbatim. Everything else is content-identical to reviewed v0.9; the source was additionally reflowed to Paper 2's soft-wrapped paragraph convention (whitespace-collapsed text verified byte-identical pre/post reflow).

Design note (lesson from Paper 2's release): this RC *is* the final v1.0 text. On authorization, CS
commits these files and tags that commit — no post-tag masthead flip, so the tagged blob and the on-main
blob are identical at release.

## 2. sha256 manifest (first 16 hex; CS to recompute full values independently)

```
md : b948521ebab74b3a   PAPER3-certification-before-retention-RC-v1.0.md
pdf: 6223cf85a65f1bc6   certification-before-retention-RC-v1.0.pdf
png: 92e3df1de5f5453a   fig1_series_gap_ladder.png
png: 7c2a7ca671ac7981   fig2_lineage_to_gates.png
png: bd3ac23bd228d416   fig3_failclosed_pipeline.png
png: ce9ad944f256e19e   fig4_three_artifact_layers.png
svg: d78f3148a7336096   fig1_series_gap_ladder.svg
svg: 404057ca715964e0   fig2_lineage_to_gates.svg
svg: b5c55151ce0b1441   fig3_failclosed_pipeline.svg
svg: 0820aca8bfe4c66b   fig4_three_artifact_layers.svg
```

## 3. CS release-consistency verification checklist (10 points)

1. File hashes match §2 (recomputed independently, full 64-hex, per the manuscript's own two-person
   hash discipline; transcript archived under governance).
2. Masthead reads `v1.0`; no `draft`/`Draft v0.x`/`for Team Lead review` residue anywhere in md or pdf.
3. Framework identifier `paper3-certification-protocol-v1.0` consistent between masthead and the A.1/A.2
   field descriptions; no stale `v0.x` identifier anywhere.
4. Three non-claim blocks (abstract, §6 preamble, §9) aligned: both union markers present ×3
   ("benchmark-superiority"; "Passing all gates does not predict that a future stress run…").
5. §6 four-field structure intact: 7 × {Success condition, Failure condition, Scientific
   interpretation, Explicit non-claim}.
6. Figures: md references exactly `figures/fig1…fig4` PNGs; all four resolve in the repo; PDF embeds
   4 images; PDF page count 15; zero right-margin overflows (fitz geometry check).
7. No candidate names, no threshold values, no run-authorization language (grep: candidate names list
   empty; numeric thresholds absent from A.1 value positions).
8. Banned-wording grep clean: "model flag retired", "snapshot caveat retired", "version drift retired",
   "mlx_lm drift harmless".
9. References: [3]/[4] scope constraints present; [4] = Dutta, Krishnan, Kwatra, Ramjee with NeurIPS 37
   Main Conference Track, 124347–124390, doi:10.52202/079017-3950.
10. License footer present and last: *© 2026 E. A. Flores, Apiana AI, Inc. … CC BY-NC 4.0 (URL).*

## 4. Proposed release mechanics (for Manager decision)

- Proposed tag: `paper3-certification-protocol-v1.0` (matches the lock-eligible framework identifier —
  a threshold sheet's `framework_version` then names the tag exactly; Manager/CS may prefer the
  paper2-style form `paper3-protocol-v1.0`, in which case the manuscript identifier still governs
  lock-eligibility and the tag is the release act).
- Sequence on authorization: (1) CS commits md + pdf (figures unchanged), (2) CS runs the §3 checklist
  against the committed blobs, (3) CS tags the verified commit, (4) Senior performs the release-record
  confirmation against the tag, (5) release record filed in
  `governance/2026-06-10_paper3-v1.0-release/` with hashes, checklist transcript, and the review-arc
  citation (v0.6→v0.9 memos + external-review disposition reference).

## 5. Standing boundaries (unchanged by this package)

Release of the protocol paper authorizes nothing downstream: no candidate selection, no threshold
population or lock, no certification evaluation, no runs of any kind, no Fork A reactivation, no Claim
C activity, no benchmark packaging. B1 v2.1 backlog items are candidate-stage future work, separately
gated. The released identifier's lock-eligibility is a *precondition* future work may use, not an
authorization.

— Senior Engineer
