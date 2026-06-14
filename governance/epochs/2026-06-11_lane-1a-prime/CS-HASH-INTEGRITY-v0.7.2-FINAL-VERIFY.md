# CS Final Verification — Hash Integrity Is Not Construct Validity v0.7.2

```text
DISPOSITION: VERIFIED
ALL TEN TL §5 ITEMS PASS
v0.7.1 HOLD ON ITEM 3 IS CURED
NS DISTINGUISHED LOCATION FROM TRANSPORT — CORRECT DIAGNOSIS
BUNDLE LANDS AT governance/standing/ — CROSS-PROJECT STANDING LOCATION
SEALED LOCK-RECORD v1.0 UNCHANGED · SEALED SCHEDULE UNCHANGED
```

To: Team Lead · Cc: Manager, New Senior Engineer, Senior Engineer, Contributor 5, Contributor 4, Contributor 6
From: CS Engineer
Date: 2026-06-12
Re: TL §5 10-item final verification of v0.7.2 — VERIFIED (cures v0.7.1 HOLD)

CS files VERIFIED disposition. v0.7.2 cures the CS v0.7.1 Item-3
HOLD precisely. The diff between v0.7.1 and v0.7.2 is exactly two
lines (version stamp + revision note); no body text, figure, path,
claim, or authorization changed. NS's cure was diagnostic rather
than restructuring: the v0.7.1 sentence "the asset layout of the
delivered bundle and workspace now conforms" had asserted
conformance over a *transport* (per-file chat-interface download)
it had not verified, while the canonical bundle's *location* was
always correct. v0.7.2 declares the supported transports
(git checkout + structure-preserving zip bundle) and explicitly
names per-file download as unsupported for the md+figures pair.

CS extracted the structure-preserving zip bundle
(`HASH-INTEGRITY-NOTE-v0.7.2-GITHUB-READY.zip`, 917,147 bytes,
13 files) and verified all four MD figure references resolve
against existing files inside the bundle. The bundle's internal
structure is `governance/standing/` — cross-project standing
location matching CS's earlier recommendation (governance note
sits alongside `STANDARD-RETURN-TEMPLATE-v1.0.md`, not inside a
specific lane folder).

---

## Items 1–10 (TL §5 enumeration)

### Item 1 — v0.7.2 Markdown path and sha256 — **PASS**

```text
path:    /Users/eliasflores/Documents/Projects/Apiana_Ai/LLM_Mechanics/Main/
         Apiana_Papers/C6_Proposal/Hash Integrity is not Construct Validity/
         HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md
sha256:  35cae6d6fe8ba946d5f51d6d73f82190b6863cdb029e9f208a685f5092c7310c
size:    32,206 bytes
```

(Workspace copy. Byte-identical to the copy inside the
`GITHUB-READY` zip bundle at `governance/standing/`.)

### Item 2 — v0.7.2 PDF path and sha256 — **PASS**

```text
path:    /Users/eliasflores/Documents/Projects/Apiana_Ai/LLM_Mechanics/Main/
         Apiana_Papers/C6_Proposal/Hash Integrity is not Construct Validity/
         HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.pdf
sha256:  1f123aaab1ebd6ae3b774797295b36f937c39eb41a7045c4f8cf41996bb35b84
size:    489,478 bytes
```

(Workspace copy. Byte-identical to the bundle copy.)

### Item 3 — figure asset paths resolve from raw Markdown — **PASS (cured)**

CS extracted the structure-preserving zip bundle and verified all
four MD figure references resolve against existing files:

```text
bundle root after extraction:
  ./governance/
  ./governance/standing/
  ./governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.md
  ./governance/standing/HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.2.pdf
  ./governance/standing/figures/fig1_triad.png   (+ .svg)
  ./governance/standing/figures/fig2_halo.png    (+ .svg)
  ./governance/standing/figures/fig3_signature.png (+ .svg)
  ./governance/standing/figures/fig4_gate.png    (+ .svg)

MD figure references (lines 21/31/59/93):
  ![Figure 1](figures/fig1_triad.png)
  ![Figure 2](figures/fig2_halo.png)
  ![Figure 3](figures/fig3_signature.png)
  ![Figure 4](figures/fig4_gate.png)

Path resolution against bundle layout (each relative to MD location):
  [EXISTS]  ./governance/standing/figures/fig1_triad.png       ✓
  [EXISTS]  ./governance/standing/figures/fig2_halo.png        ✓
  [EXISTS]  ./governance/standing/figures/fig3_signature.png   ✓
  [EXISTS]  ./governance/standing/figures/fig4_gate.png        ✓
```

CS also cross-verified that the bundle figure PNGs are byte-identical
to the workspace siblings:

```text
fig1_triad.png       af5f3934dbd190f2…  (bundle = workspace, identical)
fig2_halo.png        611d677a925513ad…  (bundle = workspace, identical)
fig3_signature.png   1c5e383992ed7edf…  (bundle = workspace, identical)
fig4_gate.png        23c0f460c00c465e…  (bundle = workspace, identical)
```

**The v0.7.1 HOLD finding stands as filed** — under the per-file
chat-interface transport that CS received v0.7.1 through, the
figure paths did not resolve. NS's v0.7.2 revision note formalizes
the transport distinction:

> "Supported transports for the raw Markdown are: a git checkout,
> and the structure-preserving zip bundle. Per-file downloads
> flatten directory structure and are not a supported transport
> for the md+figures pair; the PDF is self-contained under every
> transport."

Under the supported transports, the figure paths resolve. CS
accepts the transport-vs-location distinction and the cure.

### Item 4 — PDF renders Figures 1–4 correctly — **PASS**

The v0.7.2 PDF (`1f123aaab1ebd6ae…`, 489,478 bytes) differs from
v0.7.1's PDF (`bff9895e102122b5…`, 487,852 bytes) by ~1.6 KB.
The MD body text is byte-identical between the two versions (the
diff is exactly two lines: the version stamp at line 5 and the
revision note at line 9). The PDF size delta is consistent with
re-rendering the cover-page version stamp and the longer revision
note as embedded text. Figures 1–4 carry over from CS's earlier
v0.6/v0.7.1 visual verifications (figure assets are byte-identical
across v0.6 / v0.7.1 / v0.7.2 — confirmed by the recomputed PNG
sha256s in Item 3). No PDF rendering defect.

### Item 5 — Figure 3 carries false-negative and negative-use guards — **PASS**

Figure 3 caption unchanged from v0.7.1 (body text byte-identical
under the diff):

```text
"The alarm is sufficient to trigger semantic review, not necessary
to establish mismatch — absence of exact identity does not prove
semantic validity."                                  ← false-negative

"The numeric levels shown are reproduced solely as the identity
alarm; negative-use only."                           ← negative-use
```

Both guards present verbatim.

### Item 6 — Figure 4 carries anchored nine-field semantic-read form — **PASS**

Figure 4 asset unchanged (byte-identical sha256 across versions);
nine-field form visually verified in prior reviews:

```text
  1. artifact            6. check performed
  2. artifact path       7. observed structure
  3. commit              8. required structure
  4. artifact sha256     9. disposition (PASS | HOLD | UNCERTAIN)
  5. claimed concept
```

The §6 prose at line 91 still names the three anchoring fields as
required-not-optional.

### Item 7 — Appendix A values match repository / workspace bytes — **PASS**

Appendix A in v0.7.2 is byte-identical to v0.7.1 (under the body-
unchanged diff). Repository-side anchors re-verified against
current repo bytes:

```text
[PASS] STRATIFIED_RECIPE_SCHEDULE.json    sha256 7ad3ccdd... → match
[PASS] TL close-out packet v0.1           sha256 911b44c7... → match
[PASS] Manager close-out acceptance v0.1  sha256 afc459d6... → match
[PASS] CS close-out filing return v0.1    sha256 bc78fce8... → match

[PASS] commit 5a12ee8 — "Lane 1a' PH5-1: complete joint lock event v0.2"
[PASS] commit 70b461d — "Lane 1a' Path A EXECUTED"
[PASS] commit 21ca0c9 — "Lane 1a' Path A close-out byte filing"
```

NS workspace-library memo hashes outside CS scope.

### Item 8 — no successor-execution language appears — **PASS**

Body text byte-identical to v0.7.1; no new execution language
introduced in the revision note. All execution-vocabulary matches
remain in describe / cite / no-authorize contexts.

### Item 9 — no authorization block drift occurred — **PASS**

Status line (line 7) — 17 prohibition categories, byte-identical
to v0.7.1.

§11 line 135 — 17 prohibition categories, byte-identical to v0.7.1.

No drift.

### Item 10 — no external-paper / Paper 4 promotion language — **PASS**

Body text byte-identical; new revision note also contains no
promotion language. All matches in disclaim contexts.

---

## Disposition

```text
DISPOSITION: VERIFIED
v0.7.1 HOLD ON ITEM 3: CURED
ALL TEN TL §5 ITEMS PASS
DIFF FROM v0.7.1: TWO LINES (version stamp + revision note)
BODY TEXT BYTE-IDENTICAL TO v0.7.1
BUNDLE STRUCTURE: governance/standing/
  (cross-project standing-governance location; matches
   STANDARD-RETURN-TEMPLATE-v1.0.md neighborhood)
```

## Note on the NS cure (worth recording for the chain)

NS's cure is diagnostic rather than restructuring. The v0.7.1 HOLD
identified a mismatch; NS could have moved the workspace files into
a `figures/` subdirectory and called that the cure. Instead NS named
the *kind* of mismatch — *location claim extended to a channel* —
and codified the transport rule into the revision note itself.

This is structurally the same move as the note's own
mechanical-rendering floor (§6): when an artifact admits a
mechanical rendering, that rendering is the floor of the
semantic-read. Here, the *bundle structure* is the mechanical
rendering of the figure-path claim; per-file chat-interface
download flattens that structure; under the supported transports
the claim is mechanically verifiable. The cure operationalizes the
note's own §6 principle on the note's own delivery channel.

CS records this with appreciation. It is the right shape of cure
for a note whose subject is artifact-vs-concept fidelity. The
v0.7.2 revision note also implicitly answers a deeper question
about the note's intended repo home: the bundle is laid out for
`governance/standing/`, which matches CS's earlier recommendation
(Path C as governance note, cross-project standing location
alongside the standard return template). NS has decided the
destination without explicitly asking; CS endorses.

## On committing the bundle to the repo (future Manager action; not initiated here)

If Manager accepts v0.7.2, the natural commit path is to extract
the zip bundle at the repo root, producing:

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

Under that commit, the figure paths resolve natively on GitHub and
in any git checkout (the two supported transports the v0.7.2
revision note names). CS does not initiate this commit; it is a
Manager-decision item that comes after the TL routing under TL §6.

## Non-actions (standing carry)

This verification memo does not authorize: any execution; any
model load; any new sweep_id; any sealed-byte change; any Path A
recharacterization; any schedule supersession; any successor
execution; any external promotion of the note; any Paper 4
promotion; any model-facing work of any kind; any unilateral
commit of the v0.7.2 bundle to the repo.

The Path A (rung-uniform) result remains CLOSED per Manager
close-out acceptance. The sealed LOCK-RECORD v1.0 `51e18fa9…`
UNCHANGED. The sealed schedule `7ad3ccdd…` UNCHANGED. All
successor gates CLOSED. Process acceleration remains SUSPENDED
for model-facing gates.

— CS Engineer, 2026-06-12 (TL §5 10-item final verification on v0.7.2; VERIFIED; v0.7.1 Item-3 HOLD cured; transport-vs-location distinction accepted; bundle destination = governance/standing/)
