# CS RETURN — Paper 2 v1.2 RC Status-Line Cleanup Complete

**Date:** 2026-06-20
**From:** CS Engineer
**To:** Manager; Cc: Team Lead, Senior Engineer, C5
**Re:** Manager Decision 2026-06-20 — "Narrow status-line cleanup on Paper 2 v1.2 RC"
**Status:** **COMPLETE.**

---

## Headline

```text
Status-line block replaced with the Manager-supplied verbatim text.
Diff: exactly 1 insertion / 3 deletions (the old 3-wrapped-line status
block collapsed to the new 1-line block). No other prose changed.

  v1.2 pre-cleanup sha256    32056925d17253fbfa1e8b469d38f79c3f9a8fecd93db101177f01b8c513c6e7
  v1.2 post-cleanup sha256   5b385d7f0409f9c050f6c6d87dcb7d665adc49df1f26468785fcfcc0d55ca1d8
```

---

## Filing record

```text
commit SHA                  (recorded post-commit in §clean-fetch)
final remote HEAD           (recorded post-commit in §clean-fetch)
clean-fetch confirmation    (recorded post-commit in §clean-fetch)

final v1.2 RC path          papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-RELEASE-CANDIDATE-v1.2.md
final v1.2 RC sha256        5b385d7f0409f9c050f6c6d87dcb7d665adc49df1f26468785fcfcc0d55ca1d8
```

## Confirmation: only the status line changed

```text
git diff --stat papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-RELEASE-CANDIDATE-v1.2.md
  1 file changed, 1 insertion(+), 3 deletions(-)

unified diff:
  -**v1.1 (revised draft — V3/hop1 integration; pending C5 → CS → TL → Manager review; not released).** River and Canyon program. Companion to *Survival Is Not Correctness: A
  -Staged, Fail-Closed Metrology Protocol for Stress-Retention Evaluation* (Paper 1). Experimental values and
  -artifact hashes are attested from the locked run records and listed in Appendix B; CS independently recomputed them for the freeze/tag pass. This revision adds a second, independent construction (foreclose-all V3; §3.3, §4.6) and integrates the V3/hop1 constructibility finding; it supersedes v1.0 pending review.
  +v1.2 release candidate. River and Canyon program. Companion to Survival Is Not Correctness: A Staged, Fail-Closed Metrology Protocol for Stress-Retention Evaluation (Paper 1). Experimental values and artifact hashes are attested from the locked run records and listed in Appendix B; CS independently recomputed them for the freeze/tag pass. This release candidate adds a second, independent construction (foreclose-all V3; §3.3, §4.6), integrates the V3/hop1 constructibility finding, and supersedes v1.1 pending final release authorization.

scope check:
  the only lines touched are the status-line block; no other character
  in the manuscript file was modified. Verified:
    "v1.1 (revised draft"          0 occurrences  (gone)
    "v1.2 release candidate"       1 occurrence    (present, verbatim)
  line count:  636 → 634   (-2 from the 3-wrapped-line→1-line collapse)
```

The replacement text is byte-faithful to the Manager-supplied paragraph — no formatting added (no bold/asterisks around "v1.2 release candidate"; no italics around the companion paper's title), no formatting removed. CS authored zero characters of new prose in this pass — the entire NEW string was supplied verbatim by Manager.

## Confirmation: all claim-bearing v0.3 NEW strings remain unchanged

```text
spot-check (each v0.3-cleared NEW string still present exactly once, no drift):

  A1   "this paper runs no compression"                                          1 × MATCH
  B1b  "not explained by that route alone"                                       1 × MATCH
  E3   "inadmissibility verdict is unanimous across draws"                       1 × MATCH (in abstract)
  E1   "structured, bounded, mappable object at 3B FP16"                         1 × MATCH
  A3   "We use *constructible* operationally"                                    1 × MATCH
  C1   "no fresh materialization clears any floor above 0.4628"                  1 × MATCH
  B4   "It does **not** control the *attractiveness*"                            1 × MATCH
  B1   "not explained by the §4.3 position/rank route alone:"                    1 × MATCH
  B2   "relocates the failure to the first-hop precondition under foreclose-all controls"  1 × MATCH
  A2+A4 "They also differ in evidential weight"                                  1 × MATCH
  B3   "relocating the failure to the first-hop precondition under foreclose-all controls" 1 × MATCH
  B5   "Distractor-attractiveness is not separated from component difficulty"    1 × MATCH
  D1   "Inference stack (V3 lifecycle, from"                                     1 × MATCH

residual M5 softening sweep also unchanged:
  'isolates' (verb form):     0 occurrences  (unchanged from post-v0.3 state)
  'not reducible':            0 occurrences  (unchanged from post-v0.3 state)
  'isolating' (residual):     1 occurrence   (still at §3.3 line 145
                                              "precluded isolating linkage at all" —
                                              the same semantically-distinct usage
                                              correctly left intact in the prior
                                              edit-apply pass; not in v0.3 edit set)
```

No claim-bearing string was touched by this status-line cleanup.

## Confirmation: figures unchanged

```text
papers/paper2-correctness-is-not-constructibility/figures/
  fig_two_constructions.png    817c9157ec5b4c004c4540baeca0e2a6323bcd03cb78ed3c9b1d52e3ba5ddb0a   UNCHANGED  (C5-cleared)
  fig_two_constructions.svg    ef5f39631aead03a48479eb149fc921a9b14d95066950a45b4bd030f229b4d01   UNCHANGED  (C5-cleared)
  fig_gate_decision.png        838550cb46389674a150df80d611282cb71fdae28b5841e3dbe051108f327433   UNCHANGED  (C5-cleared)
  fig_gate_decision.svg        2350c215f0e4b17d81b2ae51b7876ad42df09ee872aa867e48451a324f157a79   UNCHANGED  (C5-cleared)
  (fig_v3_cross_materialization.png from prior batch also UNCHANGED;
   fig1–fig4 from released v1.0 also UNCHANGED)

V3 figure numbering preserved per Manager Decision item #1 ("Keep V3
figure numbering for this RC"). No figure relabel or regeneration.
```

## Confirmation: no release or tag occurred

```text
no release    held — the file stays under .../in-review/, not at the released-paper path
no tag        held — no git tag created or moved
              Paper 2 v1.0 tag (paper2-cells01-03-v1.0):
                refs/tags/paper2-cells01-03-v1.0    41c033fc59597eb42015de9019c3ac7b7d19dd98   UNCHANGED  (tag NOT moved)
                refs/tags/paper2-cells01-03-v1.0^{} 40c0cd5a974b8bb10e7d3fe2a794b43efcd30fce   UNCHANGED  (target NOT changed)
              tagged manuscript blob 7d6706a3…                                                UNCHANGED
              released paper file on trunk (correctness-is-not-…md)  9893a818…                UNCHANGED  (NOT overwritten)
```

The body of the manuscript now reads "v1.2 release candidate" but this is the manuscript's own label, not a published release — the file lives under `.../in-review/`, no release commit/tag has been created, and "pending final release authorization" stays in the new status line as the explicit gating phrase.

## Confirmation: no run / rerun / compression / tooling / threshold change

```text
no run                          held — no inference, no model loaded
no rerun                        held — no analyzer/logger/runner invoked
no compression / INT8 / INT4    held — no quantization tooling touched
no tooling edit                 held — git diff path-a/build/ + path-a/inspector/ = (empty)
no threshold change             held — the locked 0.75 floor is unchanged;
                                       C1's robustness disclosure (added in the prior
                                       edit-apply pass) is unchanged here
no prompt regeneration          held
no artifact regeneration        held
no run-record edits             held
```

---

## Preserved sources verification

```text
papers/paper2-correctness-is-not-constructibility/
  in-review/
    PAPER-2-RELEASE-CANDIDATE-v1.1.md                        4e8a014a…   UNCHANGED  (byte-frozen)
    PAPER-2-V1.2-TIGHTENING-AND-LIMITATIONS-DELTA-v0.3.md    e759b7ed…   UNCHANGED  (edit-spec)
  correctness-is-not-constructibility.md                     9893a818…   UNCHANGED  (released v1.0)
notes/CLAIM-LEDGER-v1.0.md                                   15f32e1a…   UNCHANGED
tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md             b1687559…   UNCHANGED  (sealed; CS adds nothing)
```

---

## Boundaries held (verbatim from Manager Decision)

```text
- status-line edit only                                                       held
- no other prose changes                                                      held
- no release                                                                  held
- no tag                                                                       held
- no new experiment                                                            held
- no construction redesign                                                     held
- no compression / INT8 / INT4                                                 held
- no Claim C, no Paper B                                                       held
- no certification claim, capability claim, mechanism claim                    held
- Path A FP16 K=5 FAIL                                                         stays closed
- V3 figure numbering kept (Manager item #1)                                   held
- Cell02 placement kept in main text (Manager item #2)                         held
- new-file policy preserving v1.1 unchanged (Manager item #3)                  held
- tier0-run/ sealed                                                            held
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0; manuscript blob 7d6706a3…)         untouched
```

---

## §clean-fetch. Clean-fetch confirmation

To be appended after this return commits and pushes.

---

— CS Engineer, 2026-06-20
