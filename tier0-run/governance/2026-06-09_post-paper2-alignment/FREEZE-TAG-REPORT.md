# Freeze/Tag Report — Paper 1 and Paper 2 Instrument of Record

**Filed:** 2026-06-09 (supersedes earlier version filed same date)  
**Prepared by:** CS Engineer  
**Status:** FINAL — responds to Team Lead memo §9  
**Purpose:** Complete freeze/tag record for Paper 1 and Paper 2 instruments of record, including voided-run exclusion list and unrecoverable hashes.

---

## §1 Repository

**Repository:** `https://github.com/eaflores805-Apiana/river-and-canyon`  
**Local path:** `river-and-canyon-repo-FINAL/`  
**Total commits (as of filing):** 56  
**Existing tag:** `synthesis-cells01-03-pass4` at commit `49aa22235f136e9aba7e12bcaaa15ca991ef137b`

---

## §2 Paper 1 Tag — Confirmed

**Tag name:** `synthesis-cells01-03-pass4`  
**Commit:** `49aa22235f136e9aba7e12bcaaa15ca991ef137b`  
**Date:** 2026-06-08  
**Tag message:** "Synthesis pass 4: symmetric non-identifiability, 0/0/8 step vs 1/6/8 monotone, three-way confound documented. Cells01-03 evidence record complete."  
**Status:** Valid. Permanent. No action required.

---

## §3 Paper 1 / Paper 2 Artifact Directory

All instrument files reside in `tier0-run/`. No artifact should be migrated, renamed, edited, or replaced by the B1 backfill.

---

## §4 Runner Files

| File | Cell | sha256 | Status |
|---|---|---|---|
| `runner_twohop_l1.py` | Cell01 | `sha256:f346e4f2cf93b881e129ba25bea469e2f6349ce1b6d430f8ddfb7269f3d0d7ce` | Frozen — hash embedded in Cell01 result JSON provenance |
| `runner_twohop_l1_cell02.py` | Cell02 | `sha256:d14f6424340699785a8bdc12a8bb6c2b7cb33f96069de49e1fcb945bbc12b0fa` | Frozen — hash embedded in Cell02 result JSON provenance |
| `runner_twohop_l1_cell03.py` | Cell03 | `sha256:f23d99dfefcf6d12378b97246c28f5488fed7c8f755145211f67f7f93ed804b2` | Frozen — hash embedded in Cell03 result JSON provenance |

---

## §5 Scorer Files

| File | sha256 | Used by | Status |
|---|---|---|---|
| `scorer_twohop_l1.py` (pre-amendment) | `sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd` | Cell01, Cell02 | **UNRECOVERABLE AS SEPARATE FILE** — hash embedded in Cell01/Cell02 result JSONs; current file is post-amendment. Amendment was additive-only (`compute_dummy_baseline_scores()` only; `classify_output()` unchanged). |
| `scorer_twohop_l1.py` (post-amendment, current) | `sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde` | Cell03 | Current file on disk; hash embedded in Cell03 result JSON provenance |

**Note on pre-amendment scorer:** The pre-amendment scorer (060afad9) is not separately recoverable as a standalone file. Its hash is artifact-backed via the Cell01/Cell02 result JSONs. The amendment scope is documented in `CELL03-SCORER-AMENDMENT-PLAN.md` §9: only `compute_dummy_baseline_scores()` was changed; `classify_output()`, `score_scaffold()`, `score_format()`, and all content scoring are identical between the two versions. Cell01/Cell02 outputs are not affected by the amendment and do not require rescoring.

---

## §6 Manifest Files

| File | Cell | sha256 | Status |
|---|---|---|---|
| `items_twohop_l1_cell01.json` | Cell01 | `sha256:00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28` | Frozen |
| `items_twohop_l1_cell02.json` | Cell02 | `sha256:b81d471616f8830fba76b99b9e1b04e23d3e4af13284c27627481ae89528f4c9` | Frozen |
| `items_twohop_l1_cell03.json` | Cell03 | `sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1` | Frozen |

---

## §7 Prompt Template

| File | sha256 | Status |
|---|---|---|
| `prompt_template_twohop_l1.txt` | `sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e` | Frozen — hash embedded in all three cell result JSON provenance blocks |

---

## §8 Tokenizer

| Tokenizer | sha256 | Status |
|---|---|---|
| Qwen2.5-3B-Instruct tokenizer (all cells) | `sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539` | Confirmed via `TOKENIZER-HASH-RECONCILIATION-TWOHOP-L1.md`; hash embedded in all three cell result JSON provenance blocks |

---

## §9 Validator

| Validator | sha256 | Status |
|---|---|---|
| validate_tasks() (all cells) | `sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b` | Hash embedded in all three cell result JSON provenance blocks |

---

## §10 Raw Result Files

| File | Cell | sha256 | Status |
|---|---|---|---|
| `RESULTS-TWOHOP-L1-cell01-1780912218.json` | Cell01 (valid) | `sha256:6de8b67c0267a65f088e7bccd68b3cd070c675938c71470dd97a5411daca6f47` | Frozen — instrument of record |
| `RESULTS-TWOHOP-L1-cell02-1780933041.json` | Cell02 | `sha256:47b5eaa9b954645ca2572fe20873a0255776f60f29b0a544d8c350dcddc181ca` | Frozen — instrument of record |
| `RESULTS-TWOHOP-L1-cell03-1780948339.json` | Cell03 | `sha256:f29783622fb14caca1c2a5829da8b874836add5d111356ea42be1f7d4a7b73f7` | Frozen — instrument of record |

---

## §11 Summary Files

| File | Cell | Status |
|---|---|---|
| `RESULTS-TWOHOP-L1-cell01-ALL.md` | Cell01 | Frozen — 14-section Standard Return Packet |
| `RESULTS-TWOHOP-L1-cell02-ALL.md` | Cell02 | Frozen — 14-section Standard Return Packet |
| `RESULTS-TWOHOP-L1-cell03-ALL.md` | Cell03 | Frozen — 14-section Standard Return Packet |
| `CLAIM-B-MAP-SYNTHESIS-CELLS01-03.md` | All | Frozen — pass 4 synthesis; tagged `synthesis-cells01-03-pass4` |

---

## §12 Voided-Run Exclusion List

| File | Reason voided | Disposition |
|---|---|---|
| `RESULTS-TWOHOP-L1-cell01-1780911140.json` | mlx_lm 0.8.0 environment + no chat template applied: 96/96 FORMAT_FAIL (all SCAFFOLD_PRESENT, all FORMAT_FAIL, 0 correct). Run is structurally corrupt — failure is an infrastructure failure, not a model behavior signal. | Excluded from all Paper 1/2 counts and tables. File retained on disk for audit trail. Hash not listed as instrument-of-record. Documented in `RUNNER-AMENDMENT-LOCK-NOTE-TWOHOP-L1.md`. |

No other voided runs in the Paper 1/2 instrument.

---

## §13 Known Provenance Gaps

| Artifact | Gap | Status |
|---|---|---|
| Fork A result files (`fp16_constructibility_3b_*.json`, `stress_constructibility_3b_*.json`) | `provenance` field is `null` or absent; scorer_hash, manifest_hash, runner_hash, tokenizer_hash not embedded in provenance architecture; metadata present at top level only | DOCUMENTED — not part of Paper 1/2 two-hop L1 instrument; classified as historical only (see `FORK-A-CLARIFICATION-RETRACTION-NOTE.md`) |
| `scorer_twohop_l1.py` pre-amendment (sha256:060afad9) | Separate file not separately recoverable | UNRECOVERABLE AS FILE — hash artifact-backed via Cell01/Cell02 result JSONs; amendment scope fully documented |
| Exp6/Exp7 runner/scorer/tokenizer hashes | Decoding confirmed from source; no tokenizer/runner/scorer hashes in result JSONs | NOT RECOVERABLE — documented in `PROVENANCE-GAP-DISPOSITION.md`; Paper 1 ships as DOCUMENTED GAP |

---

## §14 Paper 2 Freeze Tag — Pending

**Recommended tag name:** `paper2-cells01-03-v1.0`  
**Status:** BLOCKED until (1) two Paper 2 corrections accepted by Senior; (2) Manager authorizes tag.

**Tag command (requires Manager authorization before execution):**
```bash
git tag -a paper2-cells01-03-v1.0 -m "Paper 2 v1.0: Two-Hop L1 Constructibility Boundary Map, Cells01-03. Gate 2 FAIL all cells, Branch 3 all cells. No compression rungs on Paper 2 construction. Recomputation verified 2026-06-09 (CS Engineer). Two framing corrections from v0.2 peer review incorporated."
git push origin paper2-cells01-03-v1.0
```

**Prerequisite checklist:**
- [ ] Cell02 "ct-last" label correction accepted by Senior
- [ ] §4.5 "(3, 11, 6)" value verified by Senior against artifact table
- [ ] Paper 2 no-stress sentence narrowed to "Paper 2 construction" per Fork A disposition
- [ ] Manager authorizes tag
- [ ] Final Paper 2 version committed to repository

---

— CS Engineer, 2026-06-09
