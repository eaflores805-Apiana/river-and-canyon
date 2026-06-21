# CS RETURN — Paper 2 v1.2 Public Release Complete

**Date:** 2026-06-21
**From:** CS Engineer
**To:** Manager; Cc: Team Lead, Senior Engineer, C5
**Re:** Manager Decision 2026-06-21 — "Authorize Paper 2 v1.2 Release / Tag / Publication Package"
**Status:** **COMPLETE — Markdown release + tag landed. PDF deferred to follow-on (per user-authorized option, see §PDF).**

---

## Headline

```text
Paper 2 v1.2 promoted from RC (5b385d7f…) to the public release path.
Status-line cleanup: exactly 3 release-label updates (no claim-bearing
prose changed). Annotated tag paper2-cells01-03-v1.2 created and pushed.
Paper 2 v1.0 tag remains at 41c033fc… (UNCHANGED, preserved).

Released MD     papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.md
                sha256  7d6bd7f265ed908ed658279bb0dc090a096f981e8d7aa732ca1c93d43cb586c3
Released PDF    DEFERRED — PDF generation tooling unavailable locally
                (no pdflatex / wkhtmltopdf / typst). Per user-authorized
                option ("MD now; drop the v1.2 PDF in inbox after"),
                v1.0 PDF (correctness-is-not-constructibility.pdf,
                1338625 bytes, dated 2026-06-09) remains in place
                UNCHANGED as the previous-release PDF; the v1.2 PDF
                will be filed when user drops it in _INBOX/. See §PDF.

new tag         paper2-cells01-03-v1.2
                points to: <release commit recorded post-commit in §clean-fetch>
                annotation: "Paper 2 v1.2 release — V3 integration + tightening"
preserved tag   paper2-cells01-03-v1.0    41c033fc59597eb42015de9019c3ac7b7d19dd98   UNCHANGED
```

---

## Filing record

```text
release commit SHA            34ef9215e8706f5a18288274be27678593dd2c01
final remote HEAD             34ef9215e8706f5a18288274be27678593dd2c01
release tag name              paper2-cells01-03-v1.2
release tag (annotated obj)   82a24b7dbff12b2ca501a093182bf35858f22caf
release tag target commit     34ef9215e8706f5a18288274be27678593dd2c01
clean-fetch confirmation      PASS — see §clean-fetch below

released Markdown path        papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.md
released Markdown sha256      7d6bd7f265ed908ed658279bb0dc090a096f981e8d7aa732ca1c93d43cb586c3
released PDF path             papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.pdf
released PDF sha256           DEFERRED — see §PDF below
                              (current file at that path is still the v1.0 PDF
                               at 1,338,625 bytes; not overwritten by this commit)

source RC                     papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-RELEASE-CANDIDATE-v1.2.md
source RC sha256              5b385d7f0409f9c050f6c6d87dcb7d665adc49df1f26468785fcfcc0d55ca1d8
                              UNCHANGED by this release (locked RC preserved at in-review/)
```

## Confirmation: released body matches the locked RC except approved release-status labels

```text
diff vs locked RC (papers/.../in-review/PAPER-2-RELEASE-CANDIDATE-v1.2.md):
  1 line changed (the status-line block on line 5)
  3 label substitutions inside that line:

  released body            locked RC body
  ─────────────────────    ─────────────────────────────────────────────────────
  "v1.2."                  "v1.2 release candidate."
  "This release adds"      "This release candidate adds"
  "supersedes v1.1."       "supersedes v1.1 pending final release authorization."

  Diff scope:
    git diff papers/.../correctness-is-not-constructibility.md
    ↔ in-review/PAPER-2-RELEASE-CANDIDATE-v1.2.md  → exactly 1 line changed

Every other character of the released body is byte-identical to the
locked RC. No claim-bearing prose was touched. CS authored zero new
prose — the released status line is just the RC status line with
gating phrases removed.

verification on the released file:
  'release candidate'                    0 × (gating phrase removed)
  'pending final release authorization'  0 × (gating phrase removed)
  'v1.2 release candidate'               0 × (label transformed to "v1.2.")
  'v1.2.'                                1 × (released label)
  'This release adds'                    1 × (released form)
  'supersedes v1.1.'                     1 × (released form)
```

## Confirmation: released body preserves claim-bearing v0.3 NEW strings (spot-check)

```text
Each v0.3-cleared NEW string still present in the released body, exactly once:

  A1   "this paper runs no compression"                                            1 × MATCH
  B1b  "not explained by that route alone"                                         1 × MATCH
  E3   "inadmissibility verdict is unanimous across draws"                         1 × MATCH
  E1   "structured, bounded, mappable object at 3B FP16"                           1 × MATCH
  A3   "We use *constructible* operationally"                                      1 × MATCH
  C1   "no fresh materialization clears any floor above 0.4628"                    1 × MATCH
  B4   "It does **not** control the *attractiveness*"                              1 × MATCH
  B1   "not explained by the §4.3 position/rank route alone:"                      1 × MATCH
  B2   "relocates the failure to the first-hop precondition under foreclose-all controls"  1 × MATCH
  B3   "relocating the failure to the first-hop precondition under foreclose-all controls" 1 × MATCH
  B5   "Distractor-attractiveness is not separated from component difficulty"      1 × MATCH
  D1   "Inference stack (V3 lifecycle, from"                                       1 × MATCH

M5 softening sweep preserved:
  'isolates' (verb)             0 × (preserved)
  'not reducible'               0 × (preserved)
  'isolating' (residual)        1 × (§3.3 line 145 — same semantically-distinct
                                     "precluded isolating linkage at all" usage
                                     unchanged from RC; not in v0.3 edit set)
```

No claim-bearing prose changed. No V3/hop1 finding language changed. No P-role limitation language changed. Claim B / Claim #5 / Claim C status preserved. Pre-stress boundary preserved. No-compression boundary preserved. No-certification / no-capability / no-mechanism boundaries preserved.

## Confirmation: figures match C5-cleared assets

```text
papers/paper2-correctness-is-not-constructibility/figures/
  fig_two_constructions.png       817c9157ec5b4c004c4540baeca0e2a6323bcd03cb78ed3c9b1d52e3ba5ddb0a   UNCHANGED (C5-cleared)
  fig_two_constructions.svg       ef5f39631aead03a48479eb149fc921a9b14d95066950a45b4bd030f229b4d01   UNCHANGED (C5-cleared)
  fig_gate_decision.png           838550cb46389674a150df80d611282cb71fdae28b5841e3dbe051108f327433   UNCHANGED (C5-cleared)
  fig_gate_decision.svg           2350c215f0e4b17d81b2ae51b7876ad42df09ee872aa867e48451a324f157a79   UNCHANGED (C5-cleared)
  fig_v3_cross_materialization.png            UNCHANGED (filed earlier)
  fig1_three_query_separation.png             UNCHANGED (from v1.0 release)
  fig2_composite_position_gradient.png        UNCHANGED (from v1.0 release)
  fig3_neggraph_intrusion.png                 UNCHANGED (from v1.0 release)
  fig4_gate_discriminates_fp16.png            UNCHANGED (from v1.0 release)

V3 figure numbering preserved per Manager Decision 2026-06-20 item #1
(no sequential renumbering applied for v1.2 RC).
```

## Confirmation: Paper 2 v1.0 tag remains preserved

```text
git ls-remote --tags origin | grep paper2

pre-release:
  refs/tags/paper2-cells01-03-v1.0       41c033fc59597eb42015de9019c3ac7b7d19dd98     UNCHANGED  (tag NOT moved)
  refs/tags/paper2-cells01-03-v1.0^{}    40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce     UNCHANGED  (target NOT changed)
  manuscript blob carried by v1.0 tag    7d6706a3…                                    UNCHANGED  (v1.0 content preserved in tag history)

post-release (this commit chain):
  refs/tags/paper2-cells01-03-v1.0       41c033fc59597eb42015de9019c3ac7b7d19dd98     UNCHANGED  (tag NOT moved)
  refs/tags/paper2-cells01-03-v1.2       <recorded post-tag in §clean-fetch>          NEW        (v1.2 release tag)

The v1.0 tag is NOT moved, re-pointed, force-pushed, deleted, or
recreated by this release. v1.0 release remains fully recoverable via
`git checkout paper2-cells01-03-v1.0`.
```

## Confirmation: no run / rerun / compression / tooling / threshold change

```text
no run                          held — no inference, no model loaded
no rerun                        held — no analyzer/logger/runner invoked
no compression / INT8 / INT4    held — no quantization tooling touched
no tooling edit                 held — git diff path-a/build/ + path-a/inspector/ = (empty)
no threshold change             held — locked 0.75 floor unchanged
no prompt regeneration          held
no artifact regeneration        held
no figure regeneration          held (V3 figure numbering kept; figs unchanged)
no run-record edits             held
```

## Confirmation: tier0-run remains sealed

```text
git status --short tier0-run/
  ?? tier0-run/Qwen2.5-3B-Instruct-mlx-int4/tokenizer.json   (pre-existing untracked; NOT staged)
  ?? tier0-run/Qwen2.5-3B-Instruct-mlx-int8/tokenizer.json   (pre-existing untracked; NOT staged)

git diff tier0-run/                                          (empty; no change)
git diff --cached tier0-run/                                 (empty; no add)

CS added nothing to tier0-run/. Sealed Claim Ledger entry at
tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md remains at
b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2.
```

---

## §PDF — PDF deferral (user-authorized, follow-on)

```text
issue:
  PDF generation tooling not available locally:
    pdflatex      not found
    wkhtmltopdf   not found
    weasyprint    not found
    typst         not found
  pandoc 2.12 is present but cannot generate PDF without one of the above.

resolution (per AskUserQuestion authorization):
  - v1.2 MD release: ship NOW (this commit / this tag).
  - v1.2 PDF release: deferred. When you drop a v1.2 PDF in _INBOX/,
    I will file it at:
      papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.pdf
    overwriting the v1.0 PDF (1,338,625 bytes; dated 2026-06-09; carried
    forward unchanged in this commit so the v1.0 PDF is preserved in the
    git history at the v1.0 tag commit `41c033fc…`).
  - On filing the v1.2 PDF, I will either:
    (a) commit + push as a follow-on commit on main (PDF reaches the
        same tag-tracking branch but lives after the v1.2 tag), or
    (b) create a sub-tag `paper2-cells01-03-v1.2+pdf` pointing at the
        PDF-inclusive commit, leaving `paper2-cells01-03-v1.2` at the
        MD-only release for the audit trail.
  - Which (a)/(b) you prefer is a Manager call to make at PDF-filing
    time; I will ask if needed.

note on the v1.0 PDF preservation:
  The v1.0 PDF is reachable forever via:
    git show paper2-cells01-03-v1.0:papers/.../correctness-is-not-constructibility.pdf
  so even if the v1.2 PDF overwrites the file later, the v1.0 PDF
  remains git-history-stable.
```

---

## Boundaries held (verbatim from Manager Decision)

```text
- public release package only                                                        held
- preserve reviewed manuscript body and claim language                               held
- only release-status labels updated (3 minimal updates)                             held
- no claim-bearing prose changes                                                     held
- V3/hop1 finding language UNCHANGED                                                 held
- P-role limitation language UNCHANGED                                               held
- Claim B / Claim #5 / Claim C status UNCHANGED                                      held
- pre-stress boundary                                                                held
- no-compression boundary                                                            held
- no-certification / no-capability / no-mechanism boundaries                         held
- no new experiment                                                                   held
- no construction redesign                                                            held
- no compression / INT8 / INT4                                                        held
- no Claim C, no Paper B                                                              held
- no M5 distractor-attractiveness experiment                                          held (bounded in paper, NOT resolved experimentally)
- Path A FP16 K=5 FAIL                                                                stays closed
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0; manuscript blob 7d6706a3…)                preserved
- tier0-run/ sealed                                                                   held
```

---

## §clean-fetch. Clean-fetch confirmation

```text
verification procedure (fresh `git clone` of the shared repo)
  git clone https://github.com/eaflores805-Apiana/river-and-canyon clean
  cd clean
  git rev-parse HEAD
  git ls-remote --tags origin | grep paper2
  git ls-tree paper2-cells01-03-v1.0 papers/.../correctness-is-not-constructibility.md
  git ls-tree paper2-cells01-03-v1.2 papers/.../correctness-is-not-constructibility.md
  shasum -a 256 papers/.../correctness-is-not-constructibility.md
  git show paper2-cells01-03-v1.0:papers/.../correctness-is-not-constructibility.md | shasum -a 256

results (clean-fetch, 2026-06-21, HEAD 34ef9215e8706f5a18288274be27678593dd2c01)

  released v1.2 manuscript (current main + paper2-cells01-03-v1.2 tag):
    git blob OID (sha1)    21f10620d7445dfadcff5bc2fbf36f8f662e651e   (NEW; v1.2 release)
    file sha256            7d6bd7f265ed908ed658279bb0dc090a096f981e8d7aa732ca1c93d43cb586c3   MATCH

    in-text checks:
      'release candidate'                       0 ×  (gating phrase removed)
      'pending final release authorization'     0 ×  (gating phrase removed)
      'v1.2.'                                   1 ×  (released label present)

  preserved v1.0 manuscript (paper2-cells01-03-v1.0 tag):
    git blob OID (sha1)    7d6706a346bb634bed6752ff147fd67e1ad2596f   UNCHANGED
                                                                       (this is the "7d6706a3…" the
                                                                        Senior cover note + chain cited
                                                                        throughout — the git blob OID,
                                                                        NOT a sha256)
    file sha256            705c6f4ba0119b27293c64d32c38929952c96ff0315e2f9ca7f80c6fb8c7daea   UNCHANGED
                                                                       (same v1.0 bytes; just shown
                                                                        under a different hash function
                                                                        for disambiguation)
    v1.0 release is fully recoverable via:
      git checkout paper2-cells01-03-v1.0
    or:
      git show paper2-cells01-03-v1.0:papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.md

  tag verification (remote):
    refs/tags/paper2-cells01-03-v1.0           41c033fc59597eb42015de9019c3ac7b7d19dd98     UNCHANGED  (tag NOT moved)
    refs/tags/paper2-cells01-03-v1.0^{}        40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce     UNCHANGED  (v1.0 target NOT changed)
    refs/tags/paper2-cells01-03-v1.2           82a24b7dbff12b2ca501a093182bf35858f22caf     NEW        (v1.2 annotated tag)
    refs/tags/paper2-cells01-03-v1.2^{}        34ef9215e8706f5a18288274be27678593dd2c01     NEW        (v1.2 target commit)

  preserved sources (must be UNCHANGED by this release):
    PAPER-2-RELEASE-CANDIDATE-v1.2.md (locked RC)
                                                  5b385d7f0409f9c050f6c6d87dcb7d665adc49df1f26468785fcfcc0d55ca1d8   UNCHANGED
    PAPER-2-RELEASE-CANDIDATE-v1.1.md             4e8a014ab8532136b41b231cd951f876d64f780eda87babd32cde9c3500cb633   UNCHANGED
    PAPER-2-V1.2-TIGHTENING-AND-LIMITATIONS-DELTA-v0.3.md
                                                  e759b7edc86aaec4cbd0757eb2ad24ebee2bf33c6836a3feb84e32585b6c79b4   UNCHANGED
    fig_two_constructions.png                    817c9157ec5b4c004c4540baeca0e2a6323bcd03cb78ed3c9b1d52e3ba5ddb0a   UNCHANGED
    fig_two_constructions.svg                    ef5f39631aead03a48479eb149fc921a9b14d95066950a45b4bd030f229b4d01   UNCHANGED
    fig_gate_decision.png                        838550cb46389674a150df80d611282cb71fdae28b5841e3dbe051108f327433   UNCHANGED
    fig_gate_decision.svg                        2350c215f0e4b17d81b2ae51b7876ad42df09ee872aa867e48451a324f157a79   UNCHANGED
    notes/CLAIM-LEDGER-v1.0.md                   15f32e1a68620a9101d344514b7c2240a9a78969a564dd8fce589f86b32ea087   UNCHANGED
    tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md
                                                  b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2   UNCHANGED  (sealed)

  PDF (deferred per §PDF):
    correctness-is-not-constructibility.pdf      1,338,625 bytes  (v1.0 PDF; UNCHANGED by this release commit)

  governance memos:
    MANAGER-DECISION memo                         fdd9f6e8dbeaddd20ea1954c159b6d6266372ff7d9a1bc73fac36f4a7f63d02e   MATCH
    CS-RETURN memo (pre-§clean-fetch append)     775edf310066394e3ab37031bedd4f877761ba72d79dcf22bb89f80e17fafdf3   MATCH

verdict
  FILED. Paper 2 v1.2 is publicly released on the shared repo at HEAD
  34ef9215e8706f5a18288274be27678593dd2c01 with annotated tag
  paper2-cells01-03-v1.2 (object 82a24b7d…, target 34ef9215…).

  The Paper 2 v1.0 tag is INTACT and v1.0 release is fully recoverable
  via `git checkout paper2-cells01-03-v1.0`. The git blob OID
  7d6706a346bb634bed6752ff147fd67e1ad2596f (the "7d6706a3…" the chain
  has been citing) is the v1.0 manuscript's git OID and is UNCHANGED.

  Released v1.2 manuscript content (sha256 7d6bd7f2…) is byte-faithful
  to the locked RC (5b385d7f…) except the 3 release-label updates;
  no claim-bearing prose was touched.

  PDF deferred per §PDF; v1.0 PDF unchanged in this commit; v1.2 PDF
  will be filed when user drops it in _INBOX/.

  The post-append digest for this CS return is recorded in the follow-on
  commit.
```

### Disambiguation note (one-time clarification)

```text
Throughout the v1.2 chain (Senior cover notes, CS provenance reviews,
CS returns), the phrase "tagged manuscript blob 7d6706a3…" was used to
refer to the git BLOB OID (sha1) of the v1.0 manuscript file as stored
in git — NOT a sha256 hash of the file content.

  v1.0 manuscript git blob OID (sha1):      7d6706a346bb634bed6752ff147fd67e1ad2596f
  v1.0 manuscript file content sha256:      705c6f4ba0119b27293c64d32c38929952c96ff0315e2f9ca7f80c6fb8c7daea

Both are stable identifiers of the same v1.0 bytes; they are the same
file under different hash functions. The chain's "7d6706a3…" claims of
"UNCHANGED" were correct at the git-OID level — confirmed unchanged on
this clean-fetch.

For future returns I will be more explicit when citing hashes, marking
them as either "git blob OID" or "file sha256" to avoid future confusion.
```

---

— CS Engineer, 2026-06-21
