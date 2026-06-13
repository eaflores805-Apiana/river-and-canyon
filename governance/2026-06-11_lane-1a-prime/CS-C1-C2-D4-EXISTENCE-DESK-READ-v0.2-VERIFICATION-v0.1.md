# CS Verification — C1/C2 D4 Existence-in-Principle Desk Read v0.2 (Senior's Surgical Correction)

```text
CS DISPOSITION: PASS (clean; no observations)
ALL 9 SUBSTANTIVE 10-ITEM CHECKS: PASS
ARTIFACT-SIDE DISPOSITION (Senior's): YES — unchanged from v0.1
v0.1 INFORMATIONAL OBSERVATION RESOLVED: 68 + 12 = 80 reconciles by recomputation
v0.1 SUPERSEDED BY v0.2 (retained per supersede-don't-rewrite)
SEALED LOCK-RECORD v1.0 UNCHANGED · SEALED SCHEDULE UNCHANGED
NO MODEL-FACING WORK · NO CONSTRUCTION · NO GENERATION
ALL 17 SUCCESSOR GATES CLOSED
```

To: Team Lead · Cc: Manager, Senior, NS, C4, C5, C6
From: CS Engineer
Date: 2026-06-13
Re: TL routing — C1/C2 D4 Existence-in-Principle Desk Read v0.2 verification

CS files the 10-item verification per TL routing. v0.2 was copied
byte-faithfully from the workspace into the lane governance
directory; v0.1 is marked SUPERSEDED in INDEX and retained per the
project's supersede-don't-rewrite convention.

All 9 substantive checks PASS. The v0.1 CS informational observation
(position counts summing to 68 vs answerable count 80) is **resolved**
by Senior's v0.2 surgical correction; CS confirms the new numeric
reconciliation totals correctly.

---

## §1. TL #1 — Filed path

```text
governance/2026-06-11_lane-1a-prime/C1-C2-D4-EXISTENCE-IN-PRINCIPLE-DESK-READ-v0.2.md
```

## §2. TL #2 — Commit

(Reported after this commit lands; populated in INDEX.)

## §3. TL #3 — sha256

```text
ca5567dc305454be0e06409effe9f101a58c44b1fd083ea9e2d45e6b0f7c9c7a  (9,524 bytes)

Byte-faithful copy from workspace (Apiana_Papers/Semantic-Read
Operationalization/) — workspace sha256 = repo sha256.

v0.1 retained at sha256 `e459251e6348fa90…` (8,416 bytes; commit
`b010b370…`) per supersede-don't-rewrite.
```

## §4. TL #4 — INDEX row present

```text
YES — v0.2 row added in this filing commit.
```

## §5. TL #5 — v0.1 marked superseded

```text
YES.
  Document-side: v0.2 line 5 explicitly states "v0.1 (`e459251e…`)
                  superseded" in the revision note.
  INDEX-side:    v0.1 INDEX row status updated to "SUPERSEDED by v0.2
                  (retained)" in this filing commit.
```

## §6. TL #6 — No-authorization footer carried

**YES.**

```text
§7 NON-AUTHORIZATION FOOTER (lines 126–130):
  "This desk read authorizes no constructed-positive generation, no
   seeded-defect exercise, no candidate generation, no model execution,
   no model loading, no sweep_id creation, no token-prior generations,
   no threshold setting, no candidate certification, no candidate
   selection, no ranking, no schedule v2 drafting, no schedule
   supersession, no Path B readiness or execution, no Path D execution,
   no quantization stress, no INT8/INT4, and no Claim C activation.

   It answers only whether C1/C2 existence-in-principle can be
   established from existing artifacts."

Footer text is identical to v0.1's §7 (the surgical correction did
not touch §7).
```

## §7. TL #7 — Full closed-gate list carried

```text
YES — §8 line 151 enumerates all 22 categories (identical to v0.1
and to Blocks E/F/G/template/precheck):

  no model-facing execution · no model loading · no sweep_id creation ·
  no token-prior generations · no constructed-positive generation ·
  no seeded-defect exercise · no surplus-signature validation ·
  no schedule v2 drafting · no schedule supersession ·
  no true breadth rerun · no Path B readiness or execution ·
  no Path D execution · no quantization stress · no INT8/INT4 ·
  no candidate selection · no ranking · no threshold work ·
  no certification evaluation · no Claim C activation ·
  no public benchmark packaging · no funder-facing release ·
  no SBIR submission

CS verdict: complete and standing.
```

## §8. TL #8 — Language-perimeter clean

**YES.**

```text
Forbidden positive over-reads (13):  ALL ABSENT
Forbidden negative over-reads (4):   ALL ABSENT
Path A references in body:           NONE
"saturated" language:                technical D7 term, not breadth claim
"Claim C" appearances:               2× — both in closed-gate negation
                                       (§7 footer + §8 closed-gate list)

The v0.2 correction added one sentence to §3 (line 71–73) introducing
"key uniqueness" as a controllable lever:

  "key uniqueness is ALSO an exposed dimension: the construction
   already contains both unique-key (68) and multi-occurrence-key (12)
   items, so key-ambiguity is a controllable lever as well."

CS perimeter check on the new sentence: no forbidden phrasing
introduced; "controllable lever" is a design-feasibility claim
(parallel to "list length" and "queried-key position" already in
§3); no breadth claim; no certification language. Clean.

The v0.2 correction added one sentence to §2 reconciling the count:

  "(The earlier v0.1 reported only the 68-item single-occurrence
   slots and omitted the 12-item multi-occurrence stratum.)"

CS perimeter check on this sentence: explicit reference to the v0.1
correction; no perimeter implications.
```

## §9. TL #9 — Disposition present

```text
YES.

§5 lines 102–104:
  "YES — the D4 condition-class construction permits a non-saturated
   clean variant (C1) and a one-dimension-matched pair (C2) to be
   specified in principle, on the evidence of existing artifacts."

Vocabulary: YES / NO / INDETERMINATE (same as v0.1). Disposition
unchanged from v0.1 per Senior's revision note line 5: "Disposition
unchanged (YES); the correction strengthens the finding (one more
exposed dimension)."
```

## §10. TL #10 — CS verification disposition

```text
DISPOSITION: PASS (clean — no informational observations)
```

All 9 substantive 10-item checks satisfied.

The v0.1 CS informational observation — that §2 position counts
(12+44+12=68) summed to less than the answerable item count (80) —
is **resolved** by Senior's v0.2 surgical correction. CS confirms:

```text
v0.2 reconciliation:
  single-occurrence queried key: 68 items (slot1=12 + slot3=44 + slot5=12)
  multi-occurrence queried key:  12 items
  sum:                            68 + 12 = 80 answerable items ✓

Reconciles cleanly. The 12 missing items in v0.1's enumeration are
a distinct "multi-occurrence-key" stratum where the queried key
appears in more than one pair (e.g. "44 -> 120" and "44 -> 3" both
present, so no single positional slot applies). CS notes this is a
different stratum than CS had hypothesized in the v0.1 observation
(CS had guessed the missing 12 were the recency_adjacent stratum
at slot 4); Senior's actual recomputation from bytes identified the
correct stratum (queried-key multi-occurrence, orthogonal to the
positional axis).

The v0.1 observation is closed. CS does not record a new observation
on v0.2.
```

CS endorses TL's read that the correction *strengthens* the finding:
the construction is now shown to expose **four** controllable
dimensions, not three (list length, queried-key position, key/value
vocabulary, **key uniqueness/ambiguity**). Adding one more lever for
a window-placed construction is design-favorable, not design-
foreclosing. The YES disposition is reinforced, not weakened.

---

## §11. Block E precondition status update (unchanged from v0.1 verification)

```text
Block E precondition C1 (off-ceiling calibration feasibility):
  paper-checkable sub-question:  YES IN PRINCIPLE (this desk read,
                                  now strengthened by the additional
                                  key-uniqueness lever per v0.2)
  realized sub-question:          still gated
  overall:                        existence-in-principle ESTABLISHED;
                                  realized part still OPEN

Block E precondition C2 (matched-clean counterpart existence):
  paper-checkable sub-question:  YES IN PRINCIPLE
  realized sub-question:          still gated
  overall:                        existence-in-principle ESTABLISHED;
                                  realized part still OPEN

Block E precondition C3 (standing semantic-read template filed):
  CLOSED

Block E disposition:               stays CONDITIONAL.
```

Natural next ask per Senior §6 is unchanged: a constructed-positive
PROPOSAL under separate Manager authorization, carrying the realized
sub-questions as its gated content.

---

## §12. State invariants (≈38th sealed-byte survival check)

```text
Sealed LOCK-RECORD v1.0    sha256 51e18fa9f45379a3...  UNCHANGED
Sealed STRATIFIED_RECIPE   sha256 7ad3ccddecd07007...  UNCHANGED
Sealed ORACLE_VERDICT      sha256 9c6cbda9eb5b6e85...  UNCHANGED
Sealed T3_BOUNDS           sha256 45565d0b46c05da4...  UNCHANGED
Sealed L01 manifests       sha256 afe0e545c318132a...  UNCHANGED
Filed Hash Integrity v0.7.2 bundle                       UNCHANGED
SHOWN-SEMANTIC-READ-TEMPLATE-v1.0 sha256 2f07c55d...    UNCHANGED
D4-A / D4-B / D4-synthesis / Path A run-of-record       UNMUTATED
Block C / D / E / F / G + Ledger + C1/C2 precheck        UNMUTATED
v0.1 desk read                                           UNMUTATED (retained
                                                          as superseded
                                                          per discipline)
```

---

## §13. Non-actions (standing carry — TL verbatim)

This verification + filing return does not authorize, request, or
initiate:

```text
model-facing execution
model loading
sweep_id creation
token-prior generations
constructed-positive generation
seeded-defect exercise
surplus-signature validation
schedule v2 drafting
schedule supersession
true breadth rerun
Path B readiness or execution
Path D execution
quantization stress
INT8 / INT4
candidate selection
ranking
threshold work
certification evaluation
Claim C activation
public benchmark packaging
funder-facing release
SBIR submission

TL §scope-specific non-actions:
construction of a variant
generation of a candidate
running a model
setting thresholds
certifying anything
selecting candidates
opening stress testing
```

Standing constraints carry. Process acceleration SUSPENDED for
model-facing gates. Semantic-read gate ACTIVE.

— CS Engineer, 2026-06-13 (C1/C2 D4 Existence-in-Principle Desk Read v0.2 verification: 9 of 9 substantive checks PASS; clean — no informational observations; v0.1 CS observation RESOLVED by Senior's surgical correction (68 + 12 = 80 reconciles via multi-occurrence-key stratum, orthogonal to positional axis); v0.1 marked SUPERSEDED in INDEX and retained per discipline; YES disposition unchanged and strengthened by the additional controllable dimension; Block E preconditions C1 + C2 existence-in-principle reaffirmed; Block E stays CONDITIONAL; ≈38th sealed-byte survival check passed)
