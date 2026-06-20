# CS Step 1 — Inbox Filing Sweep (PASS — 7 artifacts filed byte-faithful)

**Date:** 2026-06-20
**From:** CS Engineer
**To:** Team Lead, Manager; Cc: Senior Engineer, C5
**Re:** Inbox sweep 2026-06-20 — peer-review build + byte-frozen RC + v1.2 tightening delta + 3 V3 figures
**Status:** **FILED.** *(Filing only. No review advanced. CS provenance pass will queue only after C5 substantive re-review clears v1.2 per Senior's routing.)*

---

## What was filed (7 artifacts; all byte-faithful)

```text
papers/paper2-correctness-is-not-constructibility/in-review/
  PAPER-2-RELEASE-CANDIDATE-v1.1.md                       sha 4e8a014ab8532136b41b231cd951f876d64f780eda87babd32cde9c3500cb633
    — Senior's byte-frozen RC body. This is the file the v1.2 delta
      explicitly bases on (delta header: "Base: papers/paper2-…/in-review/
      PAPER-2-RELEASE-CANDIDATE-v1.1.md body, sha256 4e8a014a…").
      CANONICAL RC for the v1.2 chain.

  PAPER-2-V1.2-TIGHTENING-AND-LIMITATIONS-DELTA-v0.1.md   sha 643b01a62b6a13bf134d5376baa80be93a5687a11ed82cd91e2471fc1346dacf
    — Senior's edit-spec consolidating three reviews (C4 accept w/ minor
      tightening; C5 external referee accept w/ minor revisions; TL
      PASS w/ minor RC edits). Tagged [CLAIM]/[EDIT]/[PROV]/[DECISION].
      Routes: C5 substantive re-review → CS provenance → TL synthesis
      → Manager (RC-lock). The headline edit is M5 (distractor-
      attractiveness): "isolates the component-precondition failure"
      → "relocates … under foreclose-all controls" (appears 2× in the
      RC body; both occurrences must soften).

papers/paper2-correctness-is-not-constructibility/figures/
  fig_two_constructions.png                                sha dc167d6ca71e24ad98c38d4f05d2cde31bd983798a0028c2d1784467c388d49b
  fig_gate_decision.png                                    sha e88265a7f0213728d3f7d1545267275876c3aaaddfbe5066a46d2b70d0ef183e
  fig_v3_cross_materialization.png                         sha 4d29aabbf828fbd354924fa98b30d5d2bb6c35aeb2f9ff630b541f03230aea63
    — V3 lifecycle figures used by the peer-review build (Figure V3-1,
      V3-2, V3-3). Placed in the existing figures/ subtree alongside
      fig1_three_query_separation.png .. fig4_gate_discriminates_fp16.png.

governance/2026-06-20_paper-2-rc-v1.1-peer-review/
  PAPER-2-RC-v1.1-PEER-REVIEW-BUILD.md                    sha 4ae42161eb7ec39498b240181d31c32da2860d9c8957c300bc4cc2af8a5811f3
  PAPER-2-RC-v1.1-PEER-REVIEW-BUILD.pdf                   sha c3f578645fcaeb2642de1d743a459b89cd1e11c8c8fe199431c8a43594dfa0f7
    — The peer-review build of the RC (manuscript body + 3 V3 figure
      callouts inlined). PDF is what reviewers saw. Stored in
      governance/ for the review record (NOT in in-review/, since it
      is a review-build, not the byte-frozen RC).
  CS-STEP-1-FILING-SWEEP-2026-06-20.md
    — This filing record.
```

All 7 digests verified byte-identical to the inbox sources before the sources were moved to `_INBOX/_PROCESSED/2026-06-20/`. Inbox top-level: empty.

## Peer-review build vs canonical RC — verified byte-relationship

```text
PAPER-2-RELEASE-CANDIDATE-v1.1.md (canonical, 4e8a014a…)   633 lines
PAPER-2-RC-v1.1-PEER-REVIEW.md     (review build, 4ae42161…) 645 lines

diff:  the peer-review build adds exactly 12 lines to the canonical RC
       — 3 blocks of figure markup, one per V3 figure:

  after line 307 of the RC:
    + (blank)
    + (blank)
    + ![Foreclose-all V3 cross-materialization](figures/fig_v3_cross_materialization.png)
    + (blank)
    + **Figure V3-1.** …
    + (blank)
    + ![Fail-closed gate decision](figures/fig_gate_decision.png)
  after line 308:
    + **Figure V3-2.** …
  after line 333:
    + ![Two constructions, two failure modes](figures/fig_two_constructions.png)
    + (blank)
    + **Figure V3-3.** …
    + (blank)

  No other text or caption was added; no claim language was altered;
  no figure was replaced. The peer-review PDF rendered these markup
  blocks against the now-filed figure PNGs.

  → the peer-review build CAN be regenerated from canonical RC bytes
     + the three figure additions; the figure files are now at the
     paths the markup references.
```

---

## Disclosed: RC-naming reconciliation (CS judgment call → superseded)

```text
prior CS filing (2026-06-19, commit 6a588eaf):
  papers/paper2-correctness-is-not-constructibility/release-candidate/
    PAPER-2-RELEASE-CANDIDATE-v1.1-rc1.md     sha 2bc5cb73c3378550f05b65873a5f3a7d4174f31426905a5faa668471dd7f6527

Senior's byte-frozen RC (today's filing):
  papers/paper2-correctness-is-not-constructibility/in-review/
    PAPER-2-RELEASE-CANDIDATE-v1.1.md         sha 4e8a014ab8532136b41b231cd951f876d64f780eda87babd32cde9c3500cb633

byte-relationship between the two RC files:
  CS file (2bc5cb73…)  = tail -n +34 of the reviewed-draft source
                          = 634 lines, starting with a leading blank,
                            then # Correctness Is Not Constructibility…
  Senior file (4e8a014a…) = same body content, but WITHOUT the leading
                            blank line
                          = 633 lines, starting directly with # Correctness…
  diff: exactly one byte (the leading "\n" present in CS file, absent
        in Senior file)

resolution:
  - The v1.2 delta + the peer-review build chain anchor on Senior's
    bytes (4e8a014a…), at Senior's path (in-review/), under Senior's
    filename (PAPER-2-RELEASE-CANDIDATE-v1.1.md — no "-rc1" suffix).
  - Senior's file is therefore THE canonical RC for the v1.2 chain.
  - CS's earlier RC file is a superseded historical artifact — same
    manuscript content, byte-different by exactly the leading blank,
    at a non-canonical path/name.

CS recommendation (TL/Manager-decision-class, NOT a CS-blocker):
  - The CS file (release-candidate/PAPER-2-RELEASE-CANDIDATE-v1.1-rc1.md)
    should be deleted to avoid future ambiguity about which is the
    canonical RC. CS will not delete it without explicit authorization;
    flagging here for TL/Manager review.
  - Alternative: leave it as a historical artifact and rely on this
    filing record + the v1.2 delta's explicit "Base: …4e8a014a…"
    line to disambiguate.

what this is NOT:
  - NOT a data discrepancy. Both files preserve identical manuscript
    body content; the byte-diff is purely a leading whitespace artifact
    of two valid "preserve body after BEGIN REVISED MANUSCRIPT marker"
    interpretations.
  - NOT a provenance failure. CS's release-candidate-prep return
    (commit 8960138; 2026-06-19) explicitly disclosed the literal
    "tail -n +34" preservation rule used.
  - NOT a claim-prose change. No prose was altered in either file.
```

---

## Routing implications surfaced by this filing

```text
1. v1.2 tightening delta requires SUBSTANTIVE C5 RE-REVIEW (next step).
   Per Senior's routing in the v1.2 header:
     SE drafts → C5 claim-risk (substantive) → CS provenance → Team Lead
     synthesis → Manager (RC-lock)
   The delta itself states: "the substantive C5 re-review is REQUIRED
   (A1–A4, B1–B5, C1 touch claim-bearing sentences); it is not a 'quick
   check.'"

2. CS provenance pass on v1.2 is NOT advanced. CS will queue provenance
   review only after C5 returns PASS on v1.2.

3. The frozen RC stays the RC until v1.2 clears the chain. Per Senior:
   "The frozen RC (4e8a014a) stays the RC until v1.2 clears the chain.
    Filing/committing is CS's lane."

4. The 3 V3 figures are now reachable at the paths the peer-review
   build references (figures/fig_two_constructions.png, etc.). If
   Manager later chooses Option B sequential renumbering (per delta F1
   / TL #4), the figures may need to be relabeled (file rename only;
   no new data, no new run).

5. The headline edit cluster is M5 (distractor-attractiveness). Two RC
   sentences contain "isolates the component-precondition failure"
   (§4.6 + §5); both must soften per the delta. This is a CLAIM-bearing
   edit and triggers the substantive C5 re-review.
```

## What CS did NOT do

```text
- did NOT review claim content of any artifact (this is filing, not review)
- did NOT mutate any inbox byte
- did NOT advance CS provenance pass on v1.2 (gated on C5 substantive re-review)
- did NOT apply any v1.2 edit to the canonical RC (frozen RC stays the RC)
- did NOT modify Paper 2 v1.0 tag (paper2-cells01-03-v1.0, 41c033fc…) — UNTOUCHED
- did NOT modify released paper file on trunk (correctness-is-not-…md, 9893a818…) — UNCHANGED
- did NOT touch tier0-run/ — sealed (2 pre-existing untracked tokenizer.json files NOT staged)
- did NOT delete the prior release-candidate/PAPER-2-RELEASE-CANDIDATE-v1.1-rc1.md
   (TL/Manager-decision-class; flagged above)
- did NOT regenerate figures, edit prose, run models, change thresholds,
   edit tooling, or modify thresholds
```

---

## Boundaries held (verbatim from the standing card + v1.2 delta boundary)

```text
- no new experiment                                                           held
- no run / rerun                                                              held
- no compression / INT8 / INT4                                                held
- no Claim C, no Paper B                                                      held
- no certification claim, no capability claim, no mechanism claim             held
- no threshold change                                                         held
- no tooling edit                                                             held
- no figure regeneration                                                      held
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0; manuscript blob 7d6706a3…)        UNTOUCHED
- released paper file on trunk (9893a818…)                                    UNCHANGED
- Claim Ledger v1.0 (15f32e1a…) UNCHANGED; tier0-run/ entry (b1687559…)       UNCHANGED
- Path A FP16 K=5 FAIL                                                        stays closed
- V3 ≠ C0                                                                     not equated
```

---

## §clean-fetch. Clean-fetch confirmation

```text
verification procedure (fresh `git clone --depth 1` of the shared repo)
  git clone --depth 1 https://github.com/eaflores805-Apiana/river-and-canyon clean
  cd clean
  git rev-parse HEAD
  shasum -a 256  papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-RELEASE-CANDIDATE-v1.1.md
                 papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-V1.2-TIGHTENING-AND-LIMITATIONS-DELTA-v0.1.md
                 papers/paper2-correctness-is-not-constructibility/figures/fig_{two_constructions,gate_decision,v3_cross_materialization}.png
                 governance/2026-06-20_paper-2-rc-v1.1-peer-review/PAPER-2-RC-v1.1-PEER-REVIEW-BUILD.{md,pdf}
                 governance/2026-06-20_paper-2-rc-v1.1-peer-review/CS-STEP-1-FILING-SWEEP-2026-06-20.md
                 papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.md
                 papers/paper2-correctness-is-not-constructibility/release-candidate/PAPER-2-RELEASE-CANDIDATE-v1.1-rc1.md
                 notes/CLAIM-LEDGER-v1.0.md
                 tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md
  git ls-remote --tags origin | grep paper2

results (clean-fetch, 2026-06-20, HEAD cb3885d2a0791d01f2ed91038a0fea497b54dbb4)

  filed in this sweep:
    PAPER-2-RELEASE-CANDIDATE-v1.1.md                          4e8a014ab8532136b41b231cd951f876d64f780eda87babd32cde9c3500cb633   MATCH
    PAPER-2-V1.2-TIGHTENING-AND-LIMITATIONS-DELTA-v0.1.md      643b01a62b6a13bf134d5376baa80be93a5687a11ed82cd91e2471fc1346dacf   MATCH
    fig_two_constructions.png                                  dc167d6ca71e24ad98c38d4f05d2cde31bd983798a0028c2d1784467c388d49b   MATCH
    fig_gate_decision.png                                      e88265a7f0213728d3f7d1545267275876c3aaaddfbe5066a46d2b70d0ef183e   MATCH
    fig_v3_cross_materialization.png                           4d29aabbf828fbd354924fa98b30d5d2bb6c35aeb2f9ff630b541f03230aea63   MATCH
    PAPER-2-RC-v1.1-PEER-REVIEW-BUILD.md                       4ae42161eb7ec39498b240181d31c32da2860d9c8957c300bc4cc2af8a5811f3   MATCH
    PAPER-2-RC-v1.1-PEER-REVIEW-BUILD.pdf                      c3f578645fcaeb2642de1d743a459b89cd1e11c8c8fe199431c8a43594dfa0f7   MATCH
    CS-STEP-1-FILING-SWEEP-2026-06-20.md (pre-§clean-fetch)     3ed892d88f48740c9d3e5e31dcf1c547ea3aa81e262b9a7df82fb419c3ea6104   MATCH

  protected surfaces (must be unchanged by this sweep):
    released paper file on trunk                               9893a8184cc1e92458eee6eedb521b0e3c78b95623f458a8d2b1150b2724e1e1   UNCHANGED
    prior CS RC file (release-candidate/...rc1.md)             2bc5cb73c3378550f05b65873a5f3a7d4174f31426905a5faa668471dd7f6527   UNCHANGED  (superseded; flagged for TL/Manager cleanup decision)
    notes/CLAIM-LEDGER-v1.0.md                                 15f32e1a68620a9101d344514b7c2240a9a78969a564dd8fce589f86b32ea087   UNCHANGED
    tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md           b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2   UNCHANGED

  paper 2 v1.0 tag (must remain intact):
    refs/tags/paper2-cells01-03-v1.0                           41c033fc59597eb42015de9019c3ac7b7d19dd98                           UNCHANGED  (tag NOT moved)
    refs/tags/paper2-cells01-03-v1.0^{}                        40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce                           UNCHANGED  (tag-target NOT changed)

verdict
  FILED. All 7 inbox artifacts + this CS filing record reproduce byte-
  for-byte from the shared repo on clean fetch at HEAD cb3885d2…. All
  protected surfaces (released paper, prior RC, ledger v1.0, sealed
  ledger entry, Paper 2 v1.0 tag) are unchanged by this sweep. tier0-run/
  remained sealed (no add/modify; pre-existing untracked tokenizer.json
  files remain unstaged).

  Routing: v1.2 delta now reachable at the path Senior referenced for
  the C5 substantive re-review pass. CS provenance pass is NOT advanced
  (gated on C5).

  The post-append digest for this CS return is recorded in the follow-on
  commit.
```

---

— CS Engineer, 2026-06-20
