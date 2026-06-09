# Paper 2 Freeze/Tag Report

**Filed:** 2026-06-09  
**Prepared by:** CS Engineer  
**Status:** FINAL — responds to Team Lead memo, Paper 2 Freeze/Tag Authorization Request  
**Blocking issue:** One prerequisite unresolved before tag can be applied (see §2).

---

## §1 Tag Name

**Recommended tag name:** `paper2-cells01-03-v1.0`

---

## §2 Blocking Prerequisite — Manuscript Not in Repository

**The manuscript `paper2-correctness-is-not-constructibility-DRAFT.md` is not committed to the git repository.**

Current locations found (outside repo, outside CS scope):

| Path | sha256 (full) | Notes |
|---|---|---|
| `Main/roughdraftpaper2/PAPER2-correctness-is-not-constructibility-DRAFT.md` | `sha256:b68a9439fc3d162ba8041ec69da0fa1b164711e27db546f8f96ff718c067cd6d` | Has figures (fig1–fig4 embedded); appears to be the more complete version |
| `Papers/Apiana/files (20)/PAPER2-correctness-is-not-constructibility-DRAFT.md` | `sha256:51eafb1dd3d54fca2080ccdc0352dc39d66c2d8df4d24a69124932904ba8c1a4` | No figure references; earlier version |

The two files differ (diff confirmed). The roughdraftpaper2 version includes four figure references; the Papers/Apiana version does not.

**For the git freeze/tag to lock the manuscript, the canonical manuscript file must be committed to the repository before the tag is applied.** CS cannot commit files outside `tier0-run/` — this action belongs to the appropriate team member (Senior or Manager).

**CS recommendation:** Commit the `roughdraftpaper2` version as the canonical frozen manuscript, confirm the commit hash, then apply the tag. CS will confirm the tag once the commit is visible.

**If the manuscript is not to be committed to the repo:** The freeze/tag can still be applied to the current HEAD commit, but the tag will not include the manuscript. In that case, the freeze/tag report must note that the manuscript is externally held and must be verified via the hash above at any future audit.

---

## §3 Exact Manuscript File to Freeze

**Canonical file:** `PAPER2-correctness-is-not-constructibility-DRAFT.md`  
**Canonical version:** `roughdraftpaper2/` version — sha256:`b68a9439fc3d162ba8041ec69da0fa1b164711e27db546f8f96ff718c067cd6d`  
**Reason:** Contains figures fig1–fig4 and corresponding captions, which are absent from the Papers/Apiana version.

---

## §4 Artifact Directory Frozen

All Paper 2 artifact files reside in: `river-and-canyon-repo-FINAL/tier0-run/`

No artifact file has been modified since the recomputation was performed (2026-06-09). CS confirms all hashes below were verified directly from on-disk files during the recomputation session. No file was edited, renamed, or replaced.

---

## §5 Manifest Hashes

| Cell | File | sha256 (full 64-char) | Verified |
|---|---|---|---|
| Cell01 | `items_twohop_l1_cell01.json` | `sha256:00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28` | ✓ |
| Cell02 | `items_twohop_l1_cell02.json` | `sha256:b81d471616f8830fba76b99b9e1b04e23d3e4af13284c27627481ae89528f4c9` | ✓ |
| Cell03 | `items_twohop_l1_cell03.json` | `sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1` | ✓ |

---

## §6 Runner Hashes

| Cell | File | sha256 (full 64-char) | Verified |
|---|---|---|---|
| Cell01 | `runner_twohop_l1.py` | `sha256:f346e4f2cf93b881e129ba25bea469e2f6349ce1b6d430f8ddfb7269f3d0d7ce` | ✓ |
| Cell02 | `runner_twohop_l1_cell02.py` | `sha256:d14f6424340699785a8bdc12a8bb6c2b7cb33f96069de49e1fcb945bbc12b0fa` | ✓ |
| Cell03 | `runner_twohop_l1_cell03.py` | `sha256:f23d99dfefcf6d12378b97246c28f5488fed7c8f755145211f67f7f93ed804b2` | ✓ |

---

## §7 Scorer Hashes

| File | sha256 (full 64-char) | Used by | Verified |
|---|---|---|---|
| `scorer_twohop_l1.py` (current, post-amendment) | `sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde` | Cell03 | ✓ |
| `scorer_twohop_l1.py` (pre-amendment) | `sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd` | Cell01, Cell02 | **NOT SEPARATELY RECOVERABLE AS FILE** — hash confirmed via Cell01/Cell02 result JSON provenance blocks; amendment was additive-only to `compute_dummy_baseline_scores()`; `classify_output()` unchanged |

Additional locked files:

| File | sha256 (full 64-char) | Verified |
|---|---|---|
| `prompt_template_twohop_l1.txt` | `sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e` | ✓ |
| Tokenizer (Qwen2.5-3B-Instruct) | `sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539` | ✓ (reconciled in `TOKENIZER-HASH-RECONCILIATION-TWOHOP-L1.md`) |
| Validator | `sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b` | ✓ (embedded in all result JSONs) |

---

## §8 Result JSON Hashes

| Cell | File | sha256 (full 64-char) | Verified |
|---|---|---|---|
| Cell01 (valid) | `RESULTS-TWOHOP-L1-cell01-1780912218.json` | `sha256:6de8b67c0267a65f088e7bccd68b3cd070c675938c71470dd97a5411daca6f47` | ✓ |
| Cell02 | `RESULTS-TWOHOP-L1-cell02-1780933041.json` | `sha256:47b5eaa9b954645ca2572fe20873a0255776f60f29b0a544d8c350dcddc181ca` | ✓ |
| Cell03 | `RESULTS-TWOHOP-L1-cell03-1780948339.json` | `sha256:f29783622fb14caca1c2a5829da8b874836add5d111356ea42be1f7d4a7b73f7` | ✓ |

---

## §9 Summary File Hashes

| Cell | File | sha256 (full 64-char) |
|---|---|---|
| Cell01 | `RESULTS-TWOHOP-L1-cell01-ALL.md` | `sha256:696a1e0c078caf4c04051456aa40d536011f7ef82e1008ebc6f754fd3a7cc343` |
| Cell02 | `RESULTS-TWOHOP-L1-cell02-ALL.md` | `sha256:b4274643abb6de4807e53f572ba9416a4a40633c06a54ea4c55bae06bbf36a09` |
| Cell03 | `RESULTS-TWOHOP-L1-cell03-ALL.md` | `sha256:6c6c6dfc40e79c709b25544ec01cb581e26fc230c6a62aed50035b2161b45f61` |
| Synthesis | `CLAIM-B-MAP-SYNTHESIS-CELLS01-03.md` | Not re-hashed; covered by git tag `synthesis-cells01-03-pass4` at commit `49aa222` |

---

## §10 Voided-Run Exclusion List

| File | Reason | Status |
|---|---|---|
| `RESULTS-TWOHOP-L1-cell01-1780911140.json` | mlx_lm 0.8.0 + no chat template: 96/96 FORMAT_FAIL (all SCAFFOLD_PRESENT, all FORMAT_FAIL, 0 correct). Infrastructure failure, not a model behavior result. | Excluded from all Paper 2 tables and figures. File retained for audit trail. Noted in Appendix B of manuscript: "Voided run: Cell01 `1780911140.json` (mlx_lm 0.8.0 incompatibility, 96/96 FSF) — must not be cited." |

---

## §11 Known Unrecoverable Provenance Gaps

| Gap | Status |
|---|---|
| Pre-amendment scorer sha256:060afad9 not separately recoverable as standalone file | DOCUMENTED — hash artifact-backed via Cell01/Cell02 result JSON provenance blocks |
| Exp6/Exp7 runner/scorer/tokenizer hashes | NOT RECOVERABLE — documented in `PROVENANCE-GAP-DISPOSITION.md`; Paper 1 ships as DOCUMENTED GAP |
| Model snapshot hash (`aa8e7253…` cited in Appendix B) | NOT IN RUNNER PROVENANCE — B1 backfill will add `model_snapshot_hash` to future runs; value in Appendix B is asserted, not runner-provenance-backed in current artifact files |
| Cell01/Cell02 per-item intrusion-diagnostic fields | NOT PRESENT — Cell01/Cell02 runners predate §8 diagnostics (Cell03 only). Per-item positions are manifest-derived for Cell01/Cell02 |

---

## §12 Confirmation — No Cited Artifact Modified After Recomputation

**Confirmed.** All artifact files listed in §5–§9 above were read-only during the recomputation session (2026-06-09). No result JSON, manifest, runner, scorer, or summary file was edited, moved, renamed, or replaced. Hashes re-verified on-disk match the hashes embedded in each file's own provenance block and in the governance documents filed today.

The governance documents filed today (this directory) are new files — they do not modify any cited Paper 2 artifact.

---

## §13 Appendix B Verification

**All 8-char hash prefixes verified against on-disk files. One notation issue found.**

| Appendix B entry | Expected prefix | On-disk prefix | Match? |
|---|---|---|---|
| Cell01 manifest | `00a7adf8` | `00a7adf8` | ✓ |
| Cell02 manifest | `b81d4716` | `b81d4716` | ✓ |
| Cell03 manifest | `7d5099cb` | `7d5099cb` | ✓ |
| Cell01 runner | `f346e4f2` | `f346e4f2` | ✓ |
| Cell02 runner | `d14f6424` | `d14f6424` | ✓ |
| Cell03 runner | `f23d99df` | `f23d99df` | ✓ |
| Cell01/02 scorer | `060afad9` | `060afad9` | ✓ (provenance-embedded; file not separately recoverable) |
| Cell03 scorer | `b65c6803` | `b65c6803` | ✓ |
| Cell01 result | `6de8b67c` | `6de8b67c` | ✓ |
| Cell02 result | `47b5eaa9` | `47b5eaa9` | ✓ |
| Cell03 result | `f29783622f` | `f29783622f` | ✓ |

**Notation issue — Cell01 manifest entry:** Appendix B reads `7d…→00a7adf8`. The prefix `7d…` does not match Cell01 manifest (`00a7adf8`); `7d5099cb` is the Cell03 manifest. The `→00a7adf8` portion is correct. The `7d…` appears to be an inadvertent paste or notation artifact from the Cell03 entry. The actual hash is confirmed as `00a7adf8`. **Senior should correct `7d…→00a7adf8` to `00a7adf8` before camera-ready.**

**Model snapshot hash (`aa8e7253…`):** Appendix B asserts model snapshot `aa8e7253…`. This value is not in runner provenance (B1 gap). CS cannot verify or refute this value from current artifact files. It should be flagged as asserted-only until B1 backfill adds `model_snapshot_hash` to runner provenance, or Senior provides the sourcing for this value.

**"No INT8/INT4 run exists for any task" (Appendix B last line of positive control note):** This must read "No compression rungs were run on this construction" per the Fork A clarification. The Appendix B sentence is currently the broader (incorrect) form. Senior must correct before camera-ready.

---

## §14 Governance Scope Preserved

The freeze/tag preserves all required Paper 2 governance boundaries:

| Boundary | Status in frozen artifact |
|---|---|
| No Claim C | ✓ — no compression stress run on Paper 2 construction |
| No seam claim | ✓ — seam hypothesis (Test 1) open and unadjudicated; not referenced in Paper 2 |
| No compression-retention claim | ✓ — Gate 2 FAIL all cells; no stress runs on Paper 2 construction |
| No assertion that hop2 is stress-ready | ✓ — hop2 described as FP16 gate-discrimination control; stress readiness pending certification |
| No Fork A stress evidence admitted | ✓ — Fork A retraction remains; no Fork A figures in Paper 2 |
| Correct stress wording | **REQUIRES CORRECTION** — Appendix B currently reads "No INT8/INT4 run exists for any task." Must be changed to "No compression rungs were run on this construction." (see §13) |

---

## §15 Tag Application — Pending

**CS is ready to apply the tag once the following are resolved:**

- [ ] Manuscript committed to repo by appropriate team member (outside CS scope)
- [ ] Appendix B notation issue corrected (`7d…→00a7adf8` → `00a7adf8`)
- [ ] Appendix B stress wording corrected ("any task" → "this construction")
- [ ] Model snapshot `aa8e7253…` source confirmed or flagged as asserted-only
- [ ] Manager authorization to apply tag received

**Tag command (CS will execute on authorization):**
```bash
cd river-and-canyon-repo-FINAL
git tag -a paper2-cells01-03-v1.0 -m "Paper 2 v1.0: Correctness Is Not Constructibility. Two-Hop L1 Cells01-03 FP16 instrument locked. Gate 2 FAIL all cells, Branch 3 all cells. No compression rungs on Paper 2 construction. Recomputation verified 2026-06-09 (CS Engineer). Governance cleared."
git push origin paper2-cells01-03-v1.0
```

CS will not execute this command until Manager authorization is received and all §15 prerequisites are checked.

---

— CS Engineer, 2026-06-09
