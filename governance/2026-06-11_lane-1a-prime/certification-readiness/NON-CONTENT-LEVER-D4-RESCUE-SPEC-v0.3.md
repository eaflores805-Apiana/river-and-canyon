# NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.3

**Version:** v0.3. River and Canyon program. Certification-readiness submap, stage 3-rescue (closed-world repair). **Supersedes v0.2** (d88cfef9), which is retained and marked superseded. The v0.2 PREMISE (pull clean off ceiling, discrimination as confirm-check) is preserved unchanged; the only repair is replacing the §5 example query forms, which CS correctly HELD for violating the closed-world rule.
**Status:** model-free SPECIFICATION. Specifies; runs nothing; requests nothing. Anchored on origin/main HEAD e2ad863.
**Authorization:** "Model-free revision authorized; no execution authorized."
Owner/drafter: Senior Engineer · CS: re-verify against the prior HOLD (closed-world proof, same-key identity, content/decoy unchanged, query-side-only, single-difference, no run-auth, closed gates) · Team Lead: routing · Manager: any later run authorization + rescue/pivot decision.

---

## 0. What the CS HOLD caught, and the fix (precise)

```text
CS HELD v0.2 on Manager check #8 (closed-world). The v0.2 §5 example forms —
"value for the key immediately after key J" and "value for the alphabetically-
last key" — were wrong for TWO independent reasons:
  1. LATENT VOCABULARY: resolving "after" or "alphabetically-last" requires
     ordering/alphabet knowledge NOT stated in the prompt → violates check #8.
  2. LIST-CONTENT-DEPENDENT (the deeper bug): in the DEFECTIVE member the queried
     key is absent, so "the key immediately after J" or "the alphabetically-last
     key" resolves to a DIFFERENT key identity than in clean → violates the
     spec's own §10 CRITICAL CHECK (same key identity in both members) BY
     CONSTRUCTION. The v0.2 critical check would catch this and DROP CAL-Q,
     leaving no workable query class.
FIX (v0.3): replace the example forms with an IN-PROMPT CODE BOOK alias whose
resolution depends ONLY on facts explicitly in the prompt AND is INDEPENDENT of
which other list keys are present — so it resolves to the SAME integer key
identity in both members. The premise and all other v0.2 content are unchanged.
```

## 1. Premise (preserved from v0.2 — the corrected, NULL-normalized picture)

```text
D4 is NOT in PIVOT WATCH on defective discrimination. The NULL-normalized
re-score (HEAD 3b2c1b0) showed defective concept-level abstention stable ~0.90
and true false-emission stable ~0.10 across CAL-A/B/C/E (CAL-E's apparent
"inflation" was a case-sensitive-NULL scorer artifact). The instrument's
discrimination WORKS and is robust under harder constructs.
LIVE BLOCKER: clean saturation. Every candidate's clean accuracy is ≥ 0.95, at or
above the ceiling; content levers move it weakly and non-monotonically. The
redesign's job: a query-side lever that pulls CLEAN into 0.6625 < a < 0.95 while
discrimination (now confirmed robust) holds as a check.
```

## 2. Corrected anchor facts (NULL-normalized, byte-read)

```text
  candidate   clean    def-abstention(concept)   true-false-emit
  CAL-A       1.000    0.900                      0.100
  CAL-B       0.975    0.925                      0.075
  CAL-C       0.950    0.875                      0.125
  CAL-E       0.975    0.900                      0.100
  TARGET BAND (clean):  0.6625 < clean < 0.95   |  STATUS: all clean ≥ 0.95.
```

## 3. The repaired lever: in-prompt code-book alias resolution (the v0.3 fix)

The query-side difficulty is now added by an **in-prompt code book**: an explicit alias→key mapping stated in the prompt, so the model must decode the alias before looking up the value. **All facts needed to resolve the key are in the prompt; the resolution does not depend on any other list key.**

### Clean member form

```text
Use this code book:
  A = key_145
  B = key_027
  C = key_089

Key-value list:
  key_145 = <target_value>
  key_027 = <other_value>
  key_089 = <other_value>
  ... (CAL-B-like content: list_len 13, slots 8–11, near-miss 2)

Query:
  Return the value for the key assigned to code A.

Expected answer: <target_value>   (code A → key_145, present → its value)
```

### Defective member form (the single permitted difference)

```text
Use this code book:
  A = key_145          ← IDENTICAL code book
  B = key_027
  C = key_089

Key-value list:
  key_027 = <other_value>
  key_089 = <other_value>
  key_145 is absent from the key-value list      ← the permitted defect
  ... (otherwise CAL-B-like, identical to clean except key_145 absent)

Query:
  Return the value for the key assigned to code A.      ← IDENTICAL query

Expected answer: NULL   (code A → key_145, absent → not constructible → abstain)
```

**Why this satisfies closed-world + same-key-identity:**

```text
- Code A maps to key_145 via the IN-PROMPT code book in BOTH members. The
  resolution A → key_145 uses ONLY a fact stated in the prompt (closed-world ✓),
  with no ordering, alphabet, synonym, antonym, world fact, or riddle (#2 ✓).
- key_145 is the resolved key identity in BOTH members regardless of which other
  keys appear — it does NOT depend on list content. So the query resolves to the
  SAME key identity in clean and defective (same-key ✓, fixing the v0.2 bug).
- key_145 is PRESENT in clean and ABSENT in defective — the single permitted
  difference (#4 ✓).
- The decode step (A → key_145, then look up) adds genuine clean-side difficulty
  WITHOUT touching list content or decoy material (#5, #6 ✓).
```

## 4. Requirements satisfied (Manager's eight, mapped)

```text
1. Clue fully defined inside the prompt:    code book A=key_145 etc. is in-prompt. ✓
2. No synonym/antonym/ordering/world-fact/riddle/latent-vocab clue:
   resolution is a literal in-prompt alias lookup; none of these used. ✓
3. Code/alias resolves to same key identity in clean and defective:
   A → key_145 in both, content-independent. ✓
4. Key present in clean, absent in defective:  key_145 present / absent. ✓
5. Content list + decoy material CAL-B-like, unchanged except permitted defect:
   list_len 13, slots 8–11, near-miss 2; only key_145 presence differs. ✓
6. Query-side step adds difficulty only through closed-world alias resolution:
   the decode A → key_145 is the only added step; no list change. ✓
7. Four-way defective reporting preserved (see §7). ✓
8. Decision rule BAND PLAUSIBLE / NEEDS REPAIR / PIVOT preserved (see §8). ✓
```

## 5. How the lever pressures CLEAN (the corrected target)

```text
The clean item becomes a two-step task: decode the alias (A → key_145) using the
in-prompt code book, THEN look up key_145's value. The added decode step is
genuine clean-side difficulty expected to pull clean DOWN from CAL-B's 0.975 into
the band (0.6625–0.95), WITHOUT adding list content. Because difficulty lives in
the alias-resolution (the QUESTION), not the list, it does not depend on the
unreliable list-length dial.
Multiple alias layers (A → B → key_145) could tune the difficulty up if a single
decode proves too weak — but each layer must remain a literal in-prompt mapping
(still closed-world). The single-decode form is the starting point.
```

## 6. Why discrimination should HOLD (confirm-check, preserved from v0.2)

```text
The re-score established robust key-absent discrimination (~0.90 abstention,
~0.10 emission, 0 invention) under harder constructs. The code-book step does not
change this:
  - the defective list is identical to CAL-B except key_145 is absent; no new
    decoy material.
  - code A resolves to key_145 (absent in defective) → no answer material; correct
    behavior remains abstention.
  - the decode step raises the bar for false-answering (the model must mis-decode
    AND grab a value).
Discrimination is expected to stay in its established stable range — a
CONFIRM-IT-HOLDS check, not the central concern.
```

## 7. Four-way defective reporting (preserved from v0.2, per requirement #7)

```text
A later (gated) CAL-Q run must report defective behavior in ALL FOUR forms:
  1. strict NONE accuracy        (uppercase-NONE only — the OLD strict scorer)
  2. concept-level abstention    (none + NONE, case-insensitive — the TRUE rate; authoritative)
  3. true false-emission rate    (model emits an actual value when it should abstain)
  4. format-abstention artifact  (the none-vs-NONE split, reported explicitly so
                                  the v0.1-era artifact can never recur unnoticed)
```

## 8. Pre-declared decision rule (preserved from v0.2, per requirement #8)

```text
BAND PLAUSIBLE:
  clean lands STRICTLY inside 0.6625 < clean < 0.95 AND concept-level defective
  abstention remains stable around the prior ~0.90 range WHILE true false-emission
  remains low (~0.10). → query-side lever pulled clean off the ceiling with
  discrimination intact → a certification-run request becomes well-formed
  (separate Manager auth + GREEN).
NEEDS REPAIR:
  clean remains at/above 0.95 (decode too weak — add an alias layer), OR clean
  drops too far toward the shortcut floor (too strong), OR defective concept-level
  abstention degrades materially (discrimination breaks).
PIVOT:
  closed-world query-side difficulty ALSO fails to move clean off the ceiling
  without breaking discrimination — i.e. no lever (content OR query-side) places a
  clean in-band point with preserved discrimination. → honest end of D4
  certification-readiness; pivot to Tier 1 eval-validity auditing (publishable
  negative finding; Tier 1 / Layer 1 independently demonstrated).
Rule fixed now, before any run.
```

## 9. Single-difference preservation

```text
- Clean and defective CAL-Q members differ in EXACTLY the pre-registered defect
  (key_145 — the code-A-resolved key — absent in the defective member), matched on
  the code book (identical), list_len (13), slots (8–11), vocabulary, near-miss
  (2), null-rate, format, count, scorer, AND query (identical: "value for the key
  assigned to code A").
- The code book and query are SHARED, identical properties of both members; not a
  second difference.
- CRITICAL CHECK (now satisfiable by construction): code A → key_145 in both
  members independent of list content, so the description provably resolves to the
  same key identity. (This is exactly what the v0.2 forms failed.) Still
  mechanically re-checked at construction; if any chosen form resolves
  differently across members, DROP it.
```

## 10. Semantic-read requirements

```text
- Nine-field shown-read (owner-signed) of the v0.3 construct spec before
  construction, disposed PASS (UNCERTAIN→HOLD).
- The read must confirm: (a) the code book is fully in-prompt; (b) code A resolves
  to the same fixed key identity in both members, content-independent; (c) content/
  decoy IDENTICAL to CAL-B except the permitted defect; (d) four-way defective
  reporting (§7) is wired in.
```

## 11. Checklist (status fields: PASS / FAIL / HOLD / NOT EVALUATED)

```text
route state                    YELLOW (model-free) ....................... PASS
artifact identity              sources anchored: v0.2 d88cfef9, CS HOLD
                               verification, rescore d874b894, HEAD e2ad863 . PASS
supersedes v0.2                v0.2 d88cfef9 cited + marked superseded ..... PASS
closed-world repair (the HOLD) in-prompt code book; no latent vocab ......... PASS
same-key identity both members A → key_145 content-independent .............. PASS
content load unchanged         CAL-B content; only key_145 presence differs . PASS
decoy material unchanged       identical near-miss/values ................... PASS
query-side-only change         only the code-book decode added .............. PASS
clean target primary           0.6625–0.95 .................................. PASS
four-way defective reporting   §7 ........................................... PASS
single-difference preservation §9, code book + query shared, drop-if-violated  PASS
semantic-read                  §10 reads at gated construction .............. HOLD
pre-declared decision rule     §8 PLAUSIBLE/NEEDS-REPAIR/PIVOT ............... PASS
calibration-only if run        §12 .......................................... PASS
closed-gate preservation       §13 .......................................... PASS
```

```text
SUMMARY: design-level rows PASS, INCLUDING the closed-world repair that was the
v0.2 HOLD. One HOLD (semantic-read) is correct — the nine-field reads happen at
the (gated) construction step. No FAIL.
```

## 12. Calibration-only (preserved)

```text
If a CAL-Q run is later authorized, it is CALIBRATION-ONLY: it may answer ONLY
"does the code-book query-side lever place clean in-band while discrimination
holds?" — FP16/native, no quantization, no stress arm, no certification, no
compression.
```

## 13. Closed gates

```text
No model execution · No CAL-Q run · No certification run · No compression · No
INT8/INT4 stress · No second compression rung · No full ladder · No candidate
certification · No ranking · No Claim C activation · No public benchmark
packaging · No funder-facing release · No SBIR submission. This spec is
model-free. CAL-Q is executed only under separate Manager authorization +
route-state GREEN; nothing here grants it.
```

---

## Submap status after this spec

```text
SUBMAP: Certification-readiness / off-ceiling repair design — STILL OPEN.
  stage 3-rescue v0.3 (this): closed-world HOLD repaired (in-prompt code-book
    alias replaces the latent-vocabulary example forms); premise + all other v0.2
    content preserved.
  → next: CS re-verification against the prior HOLD; then (gated) CAL-Q run → §8 verdict.
  This remains the test of whether a closed-world query-side lever can place clean
  in-band with discrimination intact. If it can: D4 viable. If not: honest pivot.
```

— Senior Engineer
