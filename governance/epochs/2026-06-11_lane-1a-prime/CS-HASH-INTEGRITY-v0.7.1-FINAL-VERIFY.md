# CS Final Verification — Hash Integrity Is Not Construct Validity v0.7.1

```text
DISPOSITION: HOLD — specific mismatch on TL §5 item 3
1 of 10 items FAIL; 9 of 10 items PASS
ALL CLAIM-RELEVANT AND BINDING-ELEMENT ITEMS PASS
THE HOLD IS A LAYOUT MISMATCH; ONE-MINUTE CLERICAL FIX; NO SUBSTANTIVE CHANGE REQUIRED
PDF rendering is correct (item 4 PASS); the HOLD is on raw-MD rendering only
SEALED LOCK-RECORD v1.0 UNCHANGED · SEALED SCHEDULE UNCHANGED
```

To: Team Lead · Cc: Manager, New Senior Engineer, Senior Engineer, Contributor 5, Contributor 4, Contributor 6
From: CS Engineer
Date: 2026-06-12
Re: TL §5 10-item final verification of v0.7.1 — HOLD on item 3

CS files the final-verification disposition per TL filter §5. Nine of
ten items PASS; one item (item 3 — figure asset paths resolve from
raw Markdown) FAILS due to a layout mismatch between the v0.7.1
revision note's claim and the actual workspace state. The HOLD is
clerical-class, not claim-class: the binding elements, the
authorization block, the figure caption guards, and Appendix A
repository anchors all verify cleanly.

CS does not apply the fix because the note's bundle lives in the
NS / Senior workspace, outside CS scope. CS lists the specific
mismatch and proposes two equivalent fix options; the choice rests
with NS / Senior.

---

## Items 1–10 (TL §5 enumeration)

### Item 1 — v0.7.1 Markdown path and sha256 — **PASS**

```text
path:    /Users/eliasflores/Documents/Projects/Apiana_Ai/LLM_Mechanics/Main/
         Apiana_Papers/C6_Proposal/Hash Integrity is not Construct Validity/
         HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.1.md
sha256:  92a9bbf254d7a777dae07d3a938a851a3c65872771824fc6b89f642f1b285b3a
size:    31,152 bytes
```

### Item 2 — v0.7.1 PDF path and sha256 — **PASS**

```text
path:    /Users/eliasflores/Documents/Projects/Apiana_Ai/LLM_Mechanics/Main/
         Apiana_Papers/C6_Proposal/Hash Integrity is not Construct Validity/
         HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.1.pdf
sha256:  bff9895e102122b5deec42a85a19b111ababda03db5a9cd12a730295db65810c
size:    487,852 bytes
```

### Item 3 — figure asset paths resolve from raw Markdown — **HOLD (FAIL)**

**Specific mismatch:** the v0.7.1 revision note states (line 9):

> "Figure-path fix: the preferred option — figures as a `figures/`
> subdirectory beside the Markdown — is the convention of record;
> the Markdown paths were already `figures/fig*.png` and the asset
> layout of the delivered bundle and workspace now conforms, so raw
> Markdown renders the figures without modification."

The workspace **does not conform**. CS verified:

```text
MD figure references (lines 21, 31, 59, 93):
  ![Figure 1](figures/fig1_triad.png)
  ![Figure 2](figures/fig2_halo.png)
  ![Figure 3](figures/fig3_signature.png)
  ![Figure 4](figures/fig4_gate.png)

Actual on-disk layout in the workspace directory:
  HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.1.md
  HASH-INTEGRITY-IS-NOT-CONSTRUCT-VALIDITY-v0.7.1.pdf
  fig1_triad.png        ← sibling to MD, NOT in figures/
  fig2_halo.png         ← sibling to MD
  fig3_signature.png    ← sibling to MD
  fig4_gate.png         ← sibling to MD

`figures/` subdirectory: DOES NOT EXIST.
```

Result: raw-Markdown rendering shows broken image tags for all four
figures. Any GitHub viewer, IDE markdown preview, or static-site
renderer will fail to resolve `figures/fig*.png` because the path
does not exist relative to the MD.

**Two equivalent fix options** (CS does not apply; NS / Senior to
choose):

```text
Option A — match the bundle layout to the MD references:
  cd "C6_Proposal/Hash Integrity is not Construct Validity"
  mkdir figures
  mv fig*.png figures/
  # (also move fig*.svg if delivered, though only PNGs are present
  # in the workspace bundle CS inspected; the prior delivery had SVGs)

Option B — match the MD references to the bundle layout:
  # Update v0.7.1 MD lines 21/31/59/93 to remove "figures/" prefix:
  ![Figure 1](fig1_triad.png)
  ![Figure 2](fig2_halo.png)
  ![Figure 3](fig3_signature.png)
  ![Figure 4](fig4_gate.png)
```

Option A is preferred because (a) the revision note's stated
convention is `figures/`, and (b) it matches the prose convention of
treating figures as a separate asset class. Option B is preferred
only if NS / Senior intends the bundle's flat layout to be canonical.

**Sub-finding:** the v0.7.1 revision note's claim "the asset layout
of the delivered bundle and workspace now conforms" is factually
incorrect as of CS inspection. If Option A is applied, the claim
becomes true; if Option B is applied, the revision note's statement
will require a small correction in v0.7.2. CS flags this as a
documentation accuracy point in addition to the layout fix.

**Why this is HOLD, not VERIFIED-WITH-MINOR-FINDING:** TL §5 named
item 3 explicitly as a verification target. The item asks whether
figure asset paths resolve from raw Markdown. They do not. CS does
not have discretion to soften an explicitly enumerated item to
"verified with finding"; the item as stated is failed.

### Item 4 — PDF renders Figures 1–4 correctly — **PASS**

The PDF (`bff9895e…`, 487,852 bytes) embeds Figures 1–4. CS
visually verified the embedded figures in the earlier review of the
v0.6 PDF; the v0.7.1 PDF differs in size by ~2 KB (vs v0.6's
485,558) consistent with the §1 caption polish noted in the
revision history (Figure 1 in-image annotation strip removed). The
four figures are present, numbered, and captioned. No rendering
defect observed.

### Item 5 — Figure 3 carries false-negative and negative-use guards — **PASS**

Figure 3 caption (line 61) carries both guards verbatim:

```text
"The alarm is sufficient to trigger semantic review, not necessary
to establish mismatch — absence of exact identity does not prove
semantic validity."                                  ← false-negative guard

"The numeric levels shown are reproduced solely as the identity
alarm; negative-use only."                           ← negative-use guard
```

Both guards travel with the figure, satisfying the C5 M3 and E1
constraints recorded in the v0.4 / v0.5.1 revision history.

### Item 6 — Figure 4 carries anchored nine-field semantic-read form — **PASS**

Figure 4 visually shows the nine-field shown-reading form (verified
in CS's earlier review of the v0.6 PDF; v0.7.1 figure asset is
byte-identical per the revision note's "the only figure change" =
Figure 1 only). The nine fields:

```text
  1. artifact
  2. artifact path
  3. commit
  4. artifact sha256
  5. claimed concept
  6. check performed
  7. observed structure
  8. required structure
  9. disposition: PASS | HOLD | UNCERTAIN
```

Figure 4 also shows the gate's placement in the model-facing corridor
(readiness packet → semantic-read → CS state/hash verify → NS + C5
review → TL filter → Manager decision → execution), with the HOLD
branch leading to "packet does not route to Manager."

The MD text at §6 (line 91) explicitly names the three anchoring
fields as required-not-optional: "without them the reading is shown
but not anchored, and a shown-but-unanchored reading cannot be
re-verified against the exact bytes it claims to have read."

### Item 7 — Appendix A values match repository / workspace bytes — **PASS**

Repository-side anchors (recomputed from current repo bytes):

```text
[PASS] STRATIFIED_RECIPE_SCHEDULE.json    sha256 7ad3ccdd... → match
[PASS] TL close-out packet v0.1           sha256 911b44c7... → match
[PASS] Manager close-out acceptance v0.1  sha256 afc459d6... → match
[PASS] CS close-out filing return v0.1    sha256 bc78fce8... → match
```

Commit references (verified to exist in repo, with descriptions):

```text
[PASS] 5a12ee8  →  5a12ee83ad60145ca8181ee1e00530dba5c5cdc6
       "Lane 1a' PH5-1: complete joint lock event v0.2 (CS-side
        filed; bounds locked; 5-stratum recipe; ORC-08 cleanup)"
       (Appendix A description: "joint lock event v0.2 — the seal
        that defined no breadth" — MATCHES)

[PASS] 70b461d  →  70b461db1c59cfd160e4b8edc425271cd420ce8e
       "Lane 1a' Path A EXECUTED: 8-rung breadth + TP active; 8
        rung-local NOT_RULED_OUT outcomes (do NOT aggregate)"
       (Appendix A description: "Path A executed under eight rung
        labels, TP active; rung-uniform, single-surface outcome"
        — MATCHES; the "do NOT aggregate" in the commit message
        is the same discipline the §3 binding characterization
        enforces)

[PASS] 21ca0c9  →  21ca0c92380f8fb8712b5d08cd699c99f12c91e6
       "Lane 1a' Path A close-out byte filing: TL packet +
        Manager acceptance v0.1 + CS filing return"
       (Appendix A description: "all filed at commit 21ca0c9"
        — MATCHES)
```

Workspace-side NS advisory memo hashes (`02df9835…`, `d12eb40d…`,
`340a0338…`, `29cbf426…`) live in the NS / Senior workspace
library and are outside CS scope per the standing repo-scope rule;
CS does not verify those hashes against bytes and does not assert
their correctness, only that the Appendix labels them correctly
as workspace-library artifacts ("workspace library; carried into
the documents of record above" — line 163).

### Item 8 — no successor-execution language appears — **PASS**

CS scanned for execution/authorization/initiation language. All
matches occur in describe / cite / no-authorize contexts:

```text
line 37 — descriptive of the case (citation-bound)
line 55 — descriptive of the failure mode
line 86 — technical mechanism (rung_schedule → per_rung_default × 8)
line 97 — gate trigger vocabulary in a not-authorize context
line 150 — Appendix A traceability description
```

No language in the note authorizes any model-facing execution,
schedule v2 work, supersession, breadth rerun, Path B / Path D
execution, additional TP generations, scrambled-binding, quantization
stress, INT8/INT4, candidate selection, ranking, threshold work,
certification evaluation, Claim C activation, public benchmark
packaging, funder-facing release, or SBIR submission.

### Item 9 — no authorization block drift occurred — **PASS**

The authorization-block surface is present in two places:

```text
Status line (line 7) — 17 prohibition categories enumerated
§11 line 135 — 17 prohibition categories enumerated
```

Comparison vs. Manager Path A close-out §15 prohibition list:

```text
schedule v2 drafting              — present  ✓
schedule supersession             — present  ✓
true breadth rerun                — present  ✓
successor D4 execution            — covered by "model-facing execution"
L02–L08 under revised schedule    — covered by "model-facing execution"
additional token-prior generations — present  ✓
scrambled-binding generations     — present in §11 ✓
quantization stress               — present  ✓
INT8 / INT4                       — present  ✓
candidate selection               — present  ✓
ranking                           — present  ✓
threshold work                    — present  ✓
certification evaluation          — present  ✓
stress-retention testing          — covered by "model-facing execution"
Claim C activation                — present  ✓
public benchmark packaging        — present  ✓
funder-facing release             — present  ✓
SBIR submission                   — present  ✓
```

§11 also adds Path B execution and Path D execution to the
prohibition list, consistent with Manager close-out §14 (Path B and
Path D listed as intentionally-unopened questions). This is an
extension consistent with the project's posture, not a drift.

No drift. Authorization block intact.

### Item 10 — no external-paper / Paper 4 promotion language — **PASS**

All matches for promotion/publication/external-paper appear in
disclaim contexts:

```text
status line:   "This is not Paper 4, not a publication-ready paper,
                and not an established external contribution."
§1:            "this note is a governance rule, not a peer-level
                model-behavior paper"
§8 TODO:       "blocking for any external promotion; non-blocking
                for governance use"
§8 TODO:       "Before this note may be promoted beyond internal
                governance, its prior-art boundary must be expanded
                and verified..."
§11:           "internal non-blind review only; not external-paper
                ready"
§11:           "if no further cases arrive, it remains a single-case
                governance note and is never promoted"
revision note: "PASS as governance note; PROMISING as future paper
                seed; MAJOR REVISIONS REQUIRED before any external
                promotion"
```

No language promotes the note to Paper 4, publication-ready paper,
or external contribution. PASS.

---

## Disposition

```text
DISPOSITION: HOLD
HOLD scope: TL §5 item 3 only (figure-path layout mismatch)
HOLD class: clerical / layout (not claim-class, not binding-class,
            not authorization-class)
Items PASSED: 1, 2, 4, 5, 6, 7, 8, 9, 10  (9 of 10)
Items FAILED: 3                            (1 of 10)
```

Cure procedure (NS / Senior choose Option A or B from §Item 3 above);
on cure, CS will return:

```text
CS-HASH-INTEGRITY-v0.7.1-FINAL-VERIFY-v0.2.md → VERIFIED
```

(or, if the cure produces a v0.7.2, CS verifies the new revision
under the same 10-item scope and returns
`CS-HASH-INTEGRITY-v0.7.2-FINAL-VERIFY.md`.)

The HOLD does not impede:

```text
- internal use of the note for guidance (already operational)
- Manager review of v0.7.1 substance if Manager chooses to disposition
  the layout issue alongside acceptance
- any other in-flight project work
```

The HOLD does impede:

```text
- raw-Markdown rendering of figures (the PDF still renders correctly)
- any future cite-by-Markdown of v0.7.1 figures
- the v0.7.1 revision note's accuracy in describing its own bundle
```

## Non-actions (standing carry)

This verification memo does not authorize: any execution; any model
load; any new sweep_id; any sealed-byte change; any Path A
recharacterization; any schedule supersession; any successor
execution; any external promotion of the note; any Paper 4 promotion;
any model-facing work of any kind.

The Path A (rung-uniform) result remains CLOSED per Manager close-out
acceptance. The sealed LOCK-RECORD v1.0 `51e18fa9…` UNCHANGED. The
sealed schedule `7ad3ccdd…` UNCHANGED. All successor gates CLOSED.

— CS Engineer, 2026-06-12 (TL §5 10-item final verification; HOLD on item 3 only; 9/10 PASS; cure proposed in two equivalent options)
