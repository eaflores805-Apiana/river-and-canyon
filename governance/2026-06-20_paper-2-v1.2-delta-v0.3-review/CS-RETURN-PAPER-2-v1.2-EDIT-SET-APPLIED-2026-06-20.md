# CS RETURN — Paper 2 v1.2 Edit Set Applied

**Date:** 2026-06-20
**From:** CS Engineer
**To:** Team Lead, Manager; Cc: Senior Engineer, C5
**Re:** TL ACTION 2026-06-20 — "Apply C5-cleared v0.3 edit set to canonical Paper 2 RC body"
**Status:** **COMPLETE.**

---

## Headline

```text
All 15 v0.3-cleared edits applied mechanically to the v1.1 RC body bytes
(4e8a014a…). Result is a new file PAPER-2-RELEASE-CANDIDATE-v1.2.md.

  source v1.1 RC body              4e8a014ab8532136b41b231cd951f876d64f780eda87babd32cde9c3500cb633  UNCHANGED
  applied v1.2 manuscript         32056925d17253fbfa1e8b469d38f79c3f9a8fecd93db101177f01b8c513c6e7  NEW

All 15 OLD strings absent (0 occurrences each); all 15 NEW strings
present (exactly 1 occurrence each). The full softening sweep landed:
'isolates' (the verb form in the M5 cluster) goes from 2 → 0; 'not
reducible' goes from 2 → 0. The 1 remaining 'isolating' is in §3.3
line 145 ("precluded isolating linkage at all") — a semantically
distinct usage about isolating linkage as a component, NOT in the v0.3
edit set; per the Apply Rule ("Do not introduce wording outside the
cleared edit set"), it was correctly left unchanged.

Output file decision (CS judgment): created a NEW file
PAPER-2-RELEASE-CANDIDATE-v1.2.md instead of mutating v1.1 in place,
preserving the byte-frozen v1.1 RC at 4e8a014a (per the v0.3 delta's
own framing: "the frozen RC (4e8a014a) stays the RC until v1.2 clears
the chain"). The body status-line label inside the file is left
unchanged — per the v0.3 delta the status-line update is a Manager
call at RC-lock, not part of this mechanical-application pass.

No edits applied to Cluster F (figure assets) within the RC body — the
canonical RC body has no V3-1/V3-2/V3-3 figure markup blocks (those
exist only in the peer-review build at governance/.../PAPER-2-RC-v1.1-
PEER-REVIEW-BUILD.md and the SVG/PNG figure files themselves). The
v0.3 delta's F-1/F-2 edits applied to the figure block + SVG; those
SVGs are already filed at the C5-cleared digests (ef5f3963 + 2350c215;
PNG 817c9157 + 838550cb) — see filing return CS-RETURN-PAPER-2-v1.2-
DELTA-v0.3-ACCESS-HOLD-CURE-FILED-2026-06-20.md, commit 37082b0c.
```

---

## Filing record

```text
commit SHA                       (recorded post-commit in §clean-fetch)
final remote HEAD                (recorded post-commit in §clean-fetch)
clean-fetch confirmation         (recorded post-commit in §clean-fetch)
applied manuscript path          papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-RELEASE-CANDIDATE-v1.2.md
applied manuscript sha256        32056925d17253fbfa1e8b469d38f79c3f9a8fecd93db101177f01b8c513c6e7
source v1.1 RC body              papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-RELEASE-CANDIDATE-v1.1.md
source v1.1 RC sha256            4e8a014ab8532136b41b231cd951f876d64f780eda87babd32cde9c3500cb633
                                 (UNCHANGED; preserved for the audit trail)
source v0.3 edit set             papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-V1.2-TIGHTENING-AND-LIMITATIONS-DELTA-v0.3.md
source v0.3 sha256               e759b7edc86aaec4cbd0757eb2ad24ebee2bf33c6836a3feb84e32585b6c79b4
                                 (UNCHANGED; edit-spec retained)
```

## Diff summary

```text
v1.1   633 lines
v1.2   636 lines  (+ 3 net lines — from A3 paragraph block + B5 bullet insert)

diff (v1.1 → v1.2):
  25 lines touched (mixed deletions / additions per line-level diff)
  15 distinct semantic edits, byte-faithful to v0.3 NEW strings
  every edit anchor was unique in the v1.1 body (verified pre-apply)
  every OLD string is absent (0 occurrences) post-apply
  every NEW string is present (exactly 1 occurrence) post-apply
```

## 15 edits applied — cluster + tag + line + OLD→NEW byte-match status

```text
A1   [CLAIM]   line  13    abstract opening: gate-as-deliverable + no-compression-first             APPLIED  match
B1b  [CLAIM]   line  17    abstract: "not reducible" → "not explained by that route alone"          APPLIED  match
E3   [EDIT]    line  17    abstract: "stable across draws" → "inadmissibility verdict unanimous"    APPLIED  match
E1   [EDIT]    line  76    "stable, mappable" → "structured, bounded, mappable"                     APPLIED  match
E2   [EDIT]    line 134    §3.2: "to be re-verified before submission" → "recomputed, listed"       APPLIED  match
A3   [CLAIM]   line 141    insert *constructible* operational definition before §3.3 heading        APPLIED  match
C1   [CLAIM]   line 147    §3.3: 0.75 floor — add local-threshold rationale + Wilson robustness     APPLIED  match
B4   [CLAIM]   line 149    §3.3: V3 design — enumerate what V3 controls + does NOT control          APPLIED  match
E4   [EDIT]    line 172    §4.1: append "construction-revision artifacts, not a trend" sentence     APPLIED  match
B1   [CLAIM]   line 291    §4.6: "not reducible to the §4.3 route" → "not explained by … alone"     APPLIED  match
B2   [CLAIM]   line 293    §4.6 result: "isolates" → "relocates … under foreclose-all controls"     APPLIED  match
A2+A4 [CLAIM]  line 332    §5: extend "two distinct ways" with asymmetry / contamination-exists     APPLIED  match
B3   [CLAIM]   line 332    §5: "isolating" → "relocating … under foreclose-all controls"            APPLIED  match
B5   [CLAIM]   line 379    §7: insert distractor-attractiveness bullet before "Behavioral only"     APPLIED  match
D1   [PROV]    line 592    Appendix B addendum: append inference stack versions                     APPLIED  match
```

## Confirmation: all [CLAIM] NEW strings match v0.3 exactly

```text
Of the 15 edits, 10 are [CLAIM]-tagged (A1, B1b, A3, C1, B4, B1, B2, A2+A4, B3, B5).
Each NEW string was applied verbatim from the v0.3 delta (sha e759b7ed…).

Spot-check verification (verbatim NEW substrings from v0.3 → present in v1.2 exactly once):

  A1   "this paper runs no compression"                                          1 × MATCH
  B1b  "not explained by that route alone"                                        1 × MATCH
  A3   "We use *constructible* operationally"                                     1 × MATCH
  A3   "Clause (iii) is what makes the V3 first-hop precondition decisive"        1 × MATCH
  C1   "no fresh materialization clears any floor above 0.4628"                   1 × MATCH
  C1   "the largest fresh-block Wilson lower bound is 0.4628"                     1 × MATCH
  B4   "It does **not** control the *attractiveness*"                             1 × MATCH
  B4   "whether that target's salience contributes to hop1 inadmissibility"       1 × MATCH
  B1   "not explained by the §4.3 position/rank route alone:"                     1 × MATCH
  B2   "relocates the failure to the first-hop precondition under foreclose-all controls"
                                                                                  1 × MATCH
  A2+A4 "They also differ in evidential weight"                                   1 × MATCH
  A2+A4 "contamination *exists* rather than that it is specifically positional"   1 × MATCH
  B3   "relocating the failure to the first-hop precondition under foreclose-all controls"
                                                                                  1 × MATCH
  B5   "Distractor-attractiveness is not separated from component difficulty"     1 × MATCH
  B5   "separating the two accounts — e.g., a variant that varies or removes the P-role distractor — is future work"
                                                                                  1 × MATCH
```

All [CLAIM] NEW strings byte-match the v0.3 delta. No paraphrasing, no near-substitution, no rewording.

## Confirmation: corrected figures / SVG text match C5-cleared assets

```text
filed at HEAD 37082b0c (commit prior to this) and UNCHANGED by this commit:

  papers/paper2-correctness-is-not-constructibility/figures/
    fig_two_constructions.png     817c9157ec5b4c004c4540baeca0e2a6323bcd03cb78ed3c9b1d52e3ba5ddb0a   C5-cleared
    fig_two_constructions.svg     ef5f39631aead03a48479eb149fc921a9b14d95066950a45b4bd030f229b4d01   C5-cleared
    fig_gate_decision.png         838550cb46389674a150df80d611282cb71fdae28b5841e3dbe051108f327433   C5-cleared
    fig_gate_decision.svg         2350c215f0e4b17d81b2ae51b7876ad42df09ee872aa867e48451a324f157a79   C5-cleared

SVG softening (verified at filing): both SVGs grep-readable XML with
0 'isolates' / 0 'not reducible'; fig_two_constructions.svg carries
the softened 'relocates' framing.

The canonical RC body (v1.1 → v1.2) does NOT contain Figure V3-1/V3-2/V3-3
caption text. The v0.3 F-1/F-2 edits applied to the figure block /
provenance-doc / SVG bytes, which were filed in the prior commit. Nothing
in the body needs F-1/F-2 application.
```

## Confirmation: no unapproved prose changes

```text
- The 15 applied edits are 1-for-1 with the v0.3 cleared edit set.
- No string outside the v0.3 OLD/NEW pairs was modified.
- Verified: all 9 listed OLD strings absent post-apply (0 occurrences each).
- Verified: all 15 NEW strings present post-apply (exactly 1 occurrence each).
- Residual "isolating" hit (1 occurrence at §3.3 line 145, "precluded isolating
  linkage at all") was correctly LEFT INTACT — it is a semantically distinct
  usage about isolating linkage as a component, NOT the M5 "isolates the
  component-precondition failure" / "isolating the component-precondition
  failure" construct that v0.3 softened. Per the Apply Rule, no wording outside
  the cleared edit set was introduced or modified.
- DECISION items NOT applied (per v0.3 explicit Manager-deferral):
    * F1 figure numbering (Manager call)
    * E5 Cell02 placement (author judgment)
    * Status line ("v1.1 (revised draft … not released)" → release-candidate
       label; Manager call at RC-lock)
  The body version-line therefore still reads "v1.1 (revised draft — V3/hop1
  integration; pending C5 → CS → TL → Manager review; not released)" — this
  is deliberate; Manager retitles at RC-lock authorization.
```

## Confirmation: no release or tag occurred

```text
no release        held — no new public file, no published artifact, no
                  "release" status anywhere; the v1.2 file is filed under
                  .../in-review/ not at the released-paper path
no tag            held — no git tag created or moved; Paper 2 v1.0 tag
                  (paper2-cells01-03-v1.0 → 41c033fc59597eb42015de9019c3ac7b7d19dd98)
                  UNCHANGED
```

## Confirmation: no run / rerun / compression / tooling / threshold change

```text
no run                        held — no inference, no model loaded
no rerun                      held — no analyzer/logger/runner invoked
no compression / INT8 / INT4  held — no quantization tooling touched
no tooling edit               held — git diff path-a/build/ + path-a/inspector/ = (empty)
no threshold change           held — the 0.75 floor remains the locked value;
                                     C1 added a *robustness disclosure* about it
                                     (not a re-pick) per the v0.3 delta's own
                                     explicit framing ("the locked floor is NOT
                                     changed; this is a robustness disclosure")
no prompt regeneration        held
no artifact regeneration      held — figures unchanged from C5-cleared digests
no run-record edits           held
```

## Confirmation: Paper 2 v1.0 tag remains UNTOUCHED

```text
git ls-remote --tags origin | grep paper2
  refs/tags/paper2-cells01-03-v1.0    41c033fc59597eb42015de9019c3ac7b7d19dd98     UNCHANGED  (tag NOT moved)
  refs/tags/paper2-cells01-03-v1.0^{} 40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce     UNCHANGED  (tag-target NOT changed)
  tagged manuscript blob             7d6706a3…                                    UNCHANGED
  released paper file on trunk       9893a8184cc1e92458eee6eedb521b0e3c78b95623f458a8d2b1150b2724e1e1  UNCHANGED  (NOT overwritten)
```

## Confirmation: tier0-run remains sealed

```text
git status --short tier0-run/
  ?? tier0-run/Qwen2.5-3B-Instruct-mlx-int4/tokenizer.json   (pre-existing untracked; NOT staged)
  ?? tier0-run/Qwen2.5-3B-Instruct-mlx-int8/tokenizer.json   (pre-existing untracked; NOT staged)

git diff tier0-run/                                          (empty; no change)
git diff --cached tier0-run/                                 (empty; no add)

CS added nothing to tier0-run/. The sealed Claim Ledger entry at
tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md remains at
b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2.
```

---

## Boundaries held (verbatim from TL ACTION)

```text
- mechanical application only                                                        held
- no release                                                                         held
- no tag                                                                              held
- no new experiment                                                                   held
- no construction redesign                                                            held
- no compression / INT8 / INT4                                                        held
- no Claim C, no Paper B                                                              held
- no certification claim, capability claim, mechanism claim                           held
- Path A FP16 K=5 FAIL                                                                stays closed
- v1.1 RC body byte-frozen at 4e8a014a                                                preserved (NOT mutated)
- v0.3 edit-spec at e759b7ed                                                          preserved (NOT mutated)
- tier0-run/ sealed                                                                   held
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0; manuscript blob 7d6706a3…)                untouched
- released paper file on trunk (9893a818…)                                            unchanged
- Claim Ledger v1.0 (15f32e1a…)                                                       unchanged
```

---

## Note on file-path / version-label choices (CS judgment, for TL transparency)

The TL ACTION specified "applied manuscript path" (singular) without naming
v1.2 vs v1.1.md. CS chose:

- **NEW file** at `.../in-review/PAPER-2-RELEASE-CANDIDATE-v1.2.md`, NOT
  in-place mutation of v1.1.md. This preserves the byte-frozen v1.1 RC
  (4e8a014a…) intact, consistent with the v0.3 delta's own framing ("the
  frozen RC (4e8a014a) stays the RC until v1.2 clears the chain"). v1.1
  remains as a historical reference; v1.2 is the new post-application
  artifact.
- **Body version-line UNCHANGED** (still reads "v1.1 (revised draft …
  pending C5 → CS → TL → Manager review; not released)"). The v0.3 delta
  explicitly defers the status-line update to Manager at RC-lock ("The
  final version identifier for the post-delta artifact is the Manager's
  call"); applying a status-line change here would exceed the cleared
  edit set.

If TL/Manager prefer in-place v1.1 mutation (overwriting 4e8a014a…) or a
different filename or body-version-line update, that is a one-shot
correction (CS can apply a tag move + filename rename or revert v1.1 →
4e8a014a + redo as in-place) — flagging the choice openly for Manager
to redirect if needed.

---

## §clean-fetch. Clean-fetch confirmation

To be appended after this return commits and pushes.

---

— CS Engineer, 2026-06-20
