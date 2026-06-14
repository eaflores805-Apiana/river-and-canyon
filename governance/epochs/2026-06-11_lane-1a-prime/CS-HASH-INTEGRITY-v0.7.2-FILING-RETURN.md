# CS Filing Return — Hash Integrity v0.7.2 Bundle Filed to governance/standing/

```text
MANAGER §2 FILING AUTHORIZATION EXECUTED
BUNDLE LANDED AT governance/standing/ — 10 FILES (MD + PDF + 4 PNG + 4 SVG)
ALL FIGURE PATHS RESOLVE NATIVELY IN GIT CHECKOUT
PDF SELF-CONTAINED · MD SELF-CONTAINED WITH figures/ SUBDIR PRESENT
NO SUCCESSOR EXECUTION · ALL SUCCESSOR GATES CLOSED
SEALED LOCK-RECORD v1.0 UNCHANGED · SEALED SCHEDULE UNCHANGED
```

To: Manager · Cc: Team Lead, New Senior Engineer, Senior Engineer, Contributor 4, Contributor 5, Contributor 6
From: CS Engineer
Date: 2026-06-12
Re: Manager §8 filing return — Hash Integrity v0.7.2 bundle filed to governance/standing/

CS files the §8 return per Manager acceptance memo (2026-06-12).
The GitHub-ready zip bundle was extracted at the repo root,
landing 10 files under `governance/standing/` per Manager §2.
All MD figure references resolve against the bundle's `figures/`
subdirectory; the PDF is self-contained.

---

## §1 — Commit SHA

(Reported after this commit lands; populated in the CS delivery
message and INDEX row.)

Prior CS verification commits (the chain that produced this filing):
```text
38a28fd7  CS v0.7.1 final-verify (HOLD on Item 3)
ded4d4ef  CS v0.7.2 final-verify (VERIFIED — HOLD cured)
THIS      CS v0.7.2 filing return (Manager §2 authorization executed)
```

## §2 — Filed file paths

Ten files landed under `governance/standing/`:

```text
governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md
governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.pdf
governance/standing/figures/fig1_triad.png
governance/standing/figures/fig1_triad.svg
governance/standing/figures/fig2_halo.png
governance/standing/figures/fig2_halo.svg
governance/standing/figures/fig3_signature.png
governance/standing/figures/fig3_signature.svg
governance/standing/figures/fig4_gate.png
governance/standing/figures/fig4_gate.svg
```

**Minor typo flag (informational, not blocking):** Manager §2's
file enumeration line 6 reads `governance/standing/fig2_halo.svg`
without the `figures/` prefix. CS filed `fig2_halo.svg` at the
correct location (`governance/standing/figures/fig2_halo.svg`)
matching the zip bundle's canonical structure and the other seven
figure assets. CS reads §2 line 6 as a transcription typo, not an
intentional layout deviation, given (a) the other three SVGs are
listed under `figures/` and (b) the zip itself places all eight
assets under `figures/`. If Manager intended an exception for
`fig2_halo.svg` specifically, CS will move it on direction.

## §3 — sha256 values (all 10 files)

```text
35cae6d6fe8ba946d5f51d6d73f82190b6863cdb029e9f208a685f5092c7310c  governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md
1f123aaab1ebd6ae3b774797295b36f937c39eb41a7045c4f8cf41996bb35b84  governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.pdf
af5f3934dbd190f23e1bba99e5008faac5fdcf27d074bef2b6ff580b8feccc76  governance/standing/figures/fig1_triad.png
2eb5519a4db7a60befa22c09ad76c0ae442dda620d41b692f5e5d147eec6df4f  governance/standing/figures/fig1_triad.svg
611d677a925513ad42365fafde5005a7b79e995654120fce96c062e4a0d0f2a3  governance/standing/figures/fig2_halo.png
40c1546d758fdcb392326af5461889d2cbd29feedffb6f56772086dff4cf1930  governance/standing/figures/fig2_halo.svg
1c5e383992ed7edf241b9106bef49e84a58c8a7c84da2e19254d845d51656c04  governance/standing/figures/fig3_signature.png
0ffa8f7febfe0287f52f477fc716d575380d469dbbec4e05910e70991c4497c1  governance/standing/figures/fig3_signature.svg
23c0f460c00c465ea1a82959dc0874a75f198ec178e9a257d4d979d001000f23  governance/standing/figures/fig4_gate.png
7040999830c37a9cec81226783f672a959fb02528389fe53b15c626f7d9120b4  governance/standing/figures/fig4_gate.svg
```

Filed MD + PDF sha256s match the v0.7.2 workspace copies and the
v0.7.2 CS verification record (`ded4d4ef…`). PNG sha256s match the
v0.7.1 / v0.7.2 reviews. SVG sha256s are recorded for the first time
in repo bytes; they are the source assets for the rendered PNGs.

## §4 — Confirmation that all figure paths resolve

The MD's four figure references (lines 21, 31, 59, 93) resolve
against the bundle's `figures/` subdirectory relative to the MD's
repo location:

```text
MD lives at:  governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md
MD refers to: figures/fig1_triad.png       → governance/standing/figures/fig1_triad.png       [EXISTS]
              figures/fig2_halo.png        → governance/standing/figures/fig2_halo.png        [EXISTS]
              figures/fig3_signature.png   → governance/standing/figures/fig3_signature.png   [EXISTS]
              figures/fig4_gate.png        → governance/standing/figures/fig4_gate.png        [EXISTS]
```

CS performed the resolution check by walking each MD `figures/*.png`
reference and verifying file existence at the resolved repo path.
All four resolve.

This is the cure plane the v0.7.2 revision note named: under git
checkout (one of the two supported transports), directory structure
is preserved and the relative paths resolve natively.

## §5 — Confirmation that the PDF is self-contained

The PDF `HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.pdf`
(`1f123aaab1ebd6ae…`, 489,478 bytes) embeds Figures 1–4. The PDF
does not depend on the `figures/` subdirectory or any sibling
asset to render. Per the v0.7.2 revision note: *"the PDF is
self-contained under every transport."* CS confirms this is
mechanically true: the PDF file alone is sufficient for the
reader to see the figures.

## §6 — Confirmation that no successor execution occurred

CS confirms: **no successor execution was authorized or performed**
as part of this filing. The Manager acceptance memo §7 lists 17
prohibited categories explicitly; the filing event:

```text
- did NOT load any model
- did NOT initiate any sweep_id
- did NOT alter any sealed byte
- did NOT execute any rung
- did NOT generate any token-prior
- did NOT touch quantization / INT8 / INT4
- did NOT touch the validation/ sealed directory
- did NOT touch d4_a_pilot/ or d4_b_pilot/ or path_a_run/
- did NOT touch any sealed schedule or LOCK-RECORD
- did NOT touch any Path A run-of-record artifact
- did NOT trigger Path B / Path D / Option S
- did NOT enable seeded-defect exercise
```

The filing is a pure governance-record action: ten new files written
under `governance/standing/`; no other repo state changed in this
commit other than INDEX.md.

## §7 — Confirmation that all successor gates remain closed

CS confirms: **all successor gates remain CLOSED.** The Manager §7
prohibition list and the standing constraints in the lane INDEX
are preserved verbatim:

```text
schedule v2 drafting              — CLOSED
schedule supersession             — CLOSED
true breadth rerun                — CLOSED
Path B execution                  — CLOSED
Path D execution                  — CLOSED
seeded-defect exercise            — CLOSED (recorded in note §8 as
                                            future possible validation;
                                            not authorized by this filing)
additional token-prior generations — CLOSED
quantization stress               — CLOSED
INT8 / INT4                       — CLOSED
candidate selection               — CLOSED
ranking                           — CLOSED
threshold work                    — CLOSED
certification evaluation          — CLOSED
Claim C activation                — CLOSED
public benchmark packaging        — CLOSED
funder-facing release             — CLOSED
SBIR submission                   — CLOSED
```

Process acceleration remains SUSPENDED for model-facing gates.
Original gate-by-gate discipline remains REINSTATED. Semantic-read
of load-bearing artifacts is now part of the required pre-routing
discipline for any model-facing readiness packet, per Manager §3
and §6 and the now-filed governance note.

## §8 — State invariants (≈29th survival check)

```text
Sealed LOCK-RECORD v1.0  sha256 51e18fa9... UNCHANGED
Sealed schedule          sha256 7ad3ccdd... UNCHANGED
ORACLE_VERDICT_TABLE     sha256 9c6cbda9... UNCHANGED
T3_BOUNDS_DECLARATION    sha256 45565d0b... UNCHANGED
L01 manifests            sha256 afe0e545... UNCHANGED
D4-A run-of-record       UNMUTATED
D4-B run-of-record       UNMUTATED
D4 synthesis v0.3        sha256 674c98c8... UNMUTATED
Path A run-of-record     UNMUTATED · CLOSED as Path A (rung-uniform)
```

CS recomputed the LOCK-RECORD and sealed-schedule hashes
immediately before filing this return; both match. No sealed byte
moved during the filing event.

## §9 — Lifecycle status per Manager §9

```text
Hash Integrity v0.7.2: ACCEPTED  ← Manager 2026-06-12
Filing in governance/standing/:   FILED THIS RETURN
Lifecycle:                        CLOSING (pending Manager close-confirmation
                                  if any is required; CS reads §9 "close after
                                  CS filing return" as authorization to mark
                                  the lifecycle closed in INDEX upon this
                                  return's filing)
All successor gates:              CLOSED
```

CS marks the v0.7.2 lifecycle as CLOSED in INDEX upon this return's
landing. If Manager intends an additional explicit close-confirmation
memo, CS will await it and adjust the INDEX status accordingly.

## §10 — Cross-references

```text
Manager acceptance memo (this filing's authorizer):
  "Manager Acceptance — Hash Integrity v0.7.2 Standing Governance Note"
  received 2026-06-12; not filed as a separate mirror per the project's
  established practice for short acceptance memos; cited here verbatim
  by date and by the §1 / §2 / §7 / §8 / §9 structure.

Driving CS verification chain:
  CS-HASH-INTEGRITY-v0.7.1-FINAL-VERIFY.md  sha256 0d346de6...  commit 38a28fd7
    (HOLD on Item 3 — figure-path layout under per-file transport)
  CS-HASH-INTEGRITY-v0.7.2-FINAL-VERIFY.md  sha256 0f197606...  commit ded4d4ef
    (VERIFIED — HOLD cured; all 10 TL §5 items PASS)

Filed bundle:
  governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md
  governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.pdf
  governance/standing/figures/  (4 PNG + 4 SVG)
```

## Non-actions (standing carry)

This filing return does not authorize: any model-facing execution;
any model load; any new sweep_id; any sealed-byte change; any Path A
recharacterization; any schedule supersession; any successor
execution; any external promotion of the note (the note remains a
standing governance / methodological / claim-ledger-support
artifact); any Paper 4 promotion; any seeded-defect exercise; any
model-facing work of any kind.

The Path A (rung-uniform) result remains CLOSED. The sealed
LOCK-RECORD v1.0 `51e18fa9…` UNCHANGED. The sealed schedule
`7ad3ccdd…` UNCHANGED. All successor gates CLOSED. Process
acceleration remains SUSPENDED for model-facing gates. Original
gate-by-gate discipline remains REINSTATED. Semantic-read of
load-bearing artifacts is now standing pre-routing discipline.

— CS Engineer, 2026-06-12 (Manager §2 filing authorization executed; 10 files landed at governance/standing/; all four figure paths resolve in repo; PDF self-contained; v0.7.2 lifecycle CLOSING per §9)
