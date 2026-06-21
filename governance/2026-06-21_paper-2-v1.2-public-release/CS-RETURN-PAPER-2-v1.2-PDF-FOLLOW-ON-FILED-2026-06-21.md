# CS RETURN — Paper 2 v1.2 PDF Follow-On Filed

**Date:** 2026-06-21
**From:** CS Engineer
**To:** Manager; Cc: Team Lead, Senior Engineer, C5
**Re:** Follow-on to v1.2 public release — v1.2 PDF arrival in inbox
**Status:** **COMPLETE — PDF filed; v1.2 release now MD + PDF parity.**

---

## Headline

```text
v1.2 PDF filed at the released path. Inbox bundle contained:
  - the v1.2 PDF (NEW canonical artifact)                  sha256 16b9538647…   (817,223 B)
  - redundant copies of already-released artifacts        (MD + 4 figures — all match repo bytes)
  - bundle helpers (tar.gz + SHA256SUMS)                   (archived without filing)

The 4 inbox PNG figures (fig1–fig4) are byte-identical to the figures
already in the repo (verified). The inbox MD matches the released v1.2
MD (7d6bd7f2…). Only the PDF needed filing.

Tag policy: no new tag created. The v1.2 tag (paper2-cells01-03-v1.2)
stays at the MD-only release commit 34ef9215; the PDF arrives as a
follow-on commit on main. Per my prior CS return §PDF, the alternative
(sub-tag paper2-cells01-03-v1.2+pdf) was offered; user did not pick,
so CS went with the simpler follow-on-commit option. If Manager wants
a sub-tag for the PDF-inclusive commit, ask and I'll create it.
```

---

## Filing record

```text
filing commit                 (recorded post-commit in §clean-fetch)
final remote HEAD             (recorded post-commit in §clean-fetch)
clean-fetch confirmation      (recorded post-commit in §clean-fetch)

released PDF path             papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.pdf
released PDF sha256           16b9538647b12dc0079f5d901170887ffc398bd0714066d11e834ea4eedc10ec
                              (NEW v1.2 PDF; 817,223 bytes)

v1.2 tag                      paper2-cells01-03-v1.2 → 34ef9215e8706f5a18288274be27678593dd2c01
                              UNCHANGED (NOT moved). Tag still points at the MD-only release.
                              The PDF lives on main AFTER this tag (follow-on commit).
```

## Disclosure: PDF lineage in git history (3 distinct PDF blobs preserved)

```text
v1.0 tag PDF (paper2-cells01-03-v1.0):
  git blob OID (sha1)         5dbfc023edd8f3108d643e27e9091c166d6e0d2f
  file sha256                 1d4eae36152b15836377737e1c64494ab73ebd53a27887b45fc02f7c733dd87e
  size                        1,338,680 bytes
  reachable                   git show paper2-cells01-03-v1.0:papers/.../correctness-is-not-constructibility.pdf

v1.0 PDF rebuild on trunk (commit 894140c "Paper 2 v1.0: rebuild PDF with v1.0 masthead",
post-v1.0 tag, pre-v1.2):
  git blob OID (sha1)         0ae930d0b112f5f9f023e3226e0f1c8328417e58
  file sha256                 6e855e4b4b8acee9a08f5d9c49fcd774aa383f91f25f7f4f73b06bb83bb7aa92
  size                        1,338,625 bytes
  reachable                   git show 894140c:papers/.../correctness-is-not-constructibility.pdf
                              (this is the PDF that was sitting on trunk pre-today, NOT the
                               tag-carried v1.0 PDF; both are v1.0-era and both preserved by git)

v1.2 PDF (this filing, on main; follow-on to v1.2 MD release):
  git blob OID (sha1)         (NEW — captured at commit time)
  file sha256                 16b9538647b12dc0079f5d901170887ffc398bd0714066d11e834ea4eedc10ec
  size                        817,223 bytes  (smaller than v1.0 PDF — different layout/build)
  reachable                   on main HEAD; v1.2 tag does NOT include this commit
```

Both v1.0-era PDFs (`5dbfc023…` and `0ae930d0…`) remain in git history. The current trunk PDF is now the v1.2 PDF. No v1.0 PDF was destroyed.

## Confirmation: only the PDF changed

```text
git diff --stat
  papers/.../correctness-is-not-constructibility.pdf  (binary, +817223 bytes / -1338625 bytes)

verified UNCHANGED in this commit:
  papers/.../correctness-is-not-constructibility.md (v1.2 release MD)      7d6bd7f265ed…   UNCHANGED
  papers/.../in-review/PAPER-2-RELEASE-CANDIDATE-v1.2.md (locked RC)       5b385d7f0409…   UNCHANGED
  papers/.../in-review/PAPER-2-RELEASE-CANDIDATE-v1.1.md (byte-frozen)     4e8a014ab853…   UNCHANGED
  papers/.../in-review/PAPER-2-V1.2-TIGHTENING-...DELTA-v0.3.md             e759b7edc86a…   UNCHANGED
  papers/.../figures/* (all 9 figures: V3 + v1.0 series)                    all UNCHANGED   (4 verified vs SE bundle = match)
  notes/CLAIM-LEDGER-v1.0.md                                                15f32e1a6862…   UNCHANGED
  tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md                          b16875590ca0…   UNCHANGED (sealed)

verified UNCHANGED on remote tags:
  paper2-cells01-03-v1.0      41c033fc59597eb42015de9019c3ac7b7d19dd98     UNCHANGED  (tag NOT moved)
  paper2-cells01-03-v1.2      82a24b7dbff12b2ca501a093182bf35858f22caf     UNCHANGED  (tag NOT moved;
                                                                                       PDF arrives AFTER
                                                                                       this tag on main)
```

## Confirmation: bundle helpers archived; no claim-bearing artifact filed beyond the PDF

```text
archived to _INBOX/_PROCESSED/2026-06-21/ (NOT filed in repo):
  PAPER-2-v1.2-FINAL.tar.gz                                                       (bundle helper)
  SHA256SUMS.txt                                                                  (sha manifest helper)
  correctness-is-not-constructibility.md                                          (redundant; matches released MD byte-for-byte)
  correctness-is-not-constructibility.pdf                                          (after filing — also archived)
  fig1_three_query_separation.png, fig2_*, fig3_*, fig4_*                          (redundant; match repo figs byte-for-byte)

per the standing inbox-workflow archive rule for non-canonical /
redundant artifacts. Inbox top-level: empty.
```

## Boundaries held

```text
- only the PDF was filed (no other file changed by this commit)              held
- v1.2 MD release (7d6bd7f2…) UNCHANGED                                       held
- v1.2 tag (paper2-cells01-03-v1.2 → 34ef9215…) UNCHANGED                     held
- v1.0 tag (paper2-cells01-03-v1.0 → 41c033fc…) UNCHANGED                     held
- v1.0-era PDFs preserved in git history (2 blobs reachable)                 held
- no claim-bearing prose changed (PDF is rendering of already-released MD)   held
- no run / rerun / compression / tooling / threshold change                  held
- tier0-run/ sealed                                                          held
- no new tag created (option B from prior CS return §PDF deferred; if
  Manager wants paper2-cells01-03-v1.2+pdf sub-tag, just ask)                held
- Path A FP16 K=5 FAIL                                                       stays closed
```

---

## §clean-fetch. Clean-fetch confirmation

To be appended after this commit + push.

---

— CS Engineer, 2026-06-21
