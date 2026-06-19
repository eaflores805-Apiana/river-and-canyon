# C5 RETURN — Paper 2 V3 Delta Draft Claim-Risk

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead · **Cc:** Senior, CS, New Senior, Manager
**Date:** 2026-06-19
**Object requested:** `PAPER-2-V3-DELTA-DRAFT-v0.1`
**Status:** review return. Authorizes nothing.

---

## Verdict

```text
HOLD — ARTIFACT ACCESS. The named object is not in this seat's reach, and a PAPER DELTA is the
highest-stakes claim-risk surface in the program — it must not be cleared unread, and unlike a
prereg it cannot even be partially adjudicated from structure, because claim-risk in prose
lives at the SENTENCE and PHRASE level and I have no sentences.

Checked exhaustively this turn:
  - Fresh clone at HEAD 539a530f63593cecfdfb38262c2dbac445223585.
  - find . for *PAPER-2-V3-DELTA* / *PAPER*2*DELTA* / *PAPER-2*V3* → no file.
  - The papers/ tree holds the EXISTING Paper 2 (papers/paper2-correctness-is-not-
    constructibility) but NOT a V3 delta draft.
  - grep -rIl for the four watchpoint phrases ("stable across draws," "foreclose-all
    redesign," "gate is shown binding," "hop1 shortfall is not reducible…") → ZERO matches
    anywhere in the tree. The draft's distinctive language is nowhere in the repo.
  - The TL notice provides no path and no digest.
  - /mnt/user-data/uploads/ → only the Hash-Integrity files.
The delta draft has not been filed to a readable path, nor pasted/uploaded.
```

The HOLD lifts the instant the draft is filed to a readable repo path (or pasted) WITH a digest
I can verify against.

## 0. Why this object cannot be pre-adjudicated the way a prereg can

```text
For prior unreadable prereg objects, I pre-loaded substantive RULINGS because a prereg's claim
safety is largely STRUCTURAL — thresholds, decision rules, outcome partitions — which can be
reasoned about from the locked discipline before the bytes arrive. A PAPER DELTA is different in
kind: its claim safety lives in the EXACT WORDING of specific sentences, the caveats that do or
do not travel attached to each claim, and what an external reader takes from a phrase STRIPPED of
the governance context. The TL's own watchpoints make this concrete — they quote four phrases and
ask whether each is "tightly bounded." Tight-boundedness is not a structural property; it is a
property of the sentence and its neighbors. I cannot rule "tightly bounded ✓/✗" on a phrase I
cannot see. So below I pre-load the STANDARD each watchpoint phrase must meet (so the drafter and
the eventual review share the bar), but I explicitly DEFER the adjudication itself to the bytes.
This is the honest limit of the seat without the object: I can state the test; I cannot score it.
```

## The four watchpoint phrases — the STANDARD each must meet (adjudication deferred to bytes)

```text
"the hop1 shortfall is not reducible to the position/rank route"
  STANDARD: acceptable ONLY if it reads as "not EXPLAINED BY the position/rank route as
  measured/controlled" — i.e. the position/rank confound was excluded and the shortfall
  remains. It must NOT read as "the shortfall has been reduced to its true cause" or "all
  non-intended routes are excluded." The program's foreclose-all design forecloses a NAMED SET
  of routes; "not reducible to position/rank" can only mean that ONE named route does not
  account for it, never that the residual is therefore the intended operation or that all
  alternatives are impossible. BYTE-CHECK: does the sentence scope to the named, measured route,
  or does it imply the cause has been isolated? The phrase "not reducible" is doing the most
  work and is the highest sentence-level risk of the four.

"stable across draws"
  STANDARD: acceptable ONLY as "the per-block admissibility VERDICT was unanimous across the
  fresh materialization draws" (the hop1-stability prereg's exact, bounded meaning) — a
  cross-materialization property of the CONSTRUCTION, never "the model is stable." And only if
  the stability run has actually RUN and cleared; if the delta is written before that result
  exists, "stable across draws" is a claim from a run that hasn't happened. BYTE-CHECK: (a) is
  "stable" bound to cross-draw verdict unanimity, not a model property; (b) does the evidence
  for it EXIST yet (has the hop1-stability run executed), or is the draft pre-writing a result?
  This second check is critical — I have not seen a hop1-stability RUN result, only its prereg.

"foreclose-all redesign"
  STANDARD: acceptable as a description of the DESIGN STANDARD V3 conforms to (it forecloses the
  named set of non-traversal routes by construction), NEVER as "V3 forecloses ALL possible
  routes" or "V3 is certified-complete." This is watchpoint 9 verbatim: conforming to the
  foreclose-all standard ≠ certified-complete. BYTE-CHECK: is "foreclose-all" the NAME of the
  design standard (safe) or a claim that all routes are foreclosed (overclaim)? The hyphenated
  term is fine as a label; the surrounding sentence must not cash it out as a completeness claim.

"gate is shown binding and discriminating across two independent constructions"
  STANDARD: this is the load-bearing contribution claim and the one most likely to overreach.
  "Binding and discriminating across two constructions" is acceptable ONLY as: the gate
  attached a non-vacuous verdict (it can fail, and did, on real constructions — C0 and V3) and
  distinguished admissible from inadmissible cases, ACROSS two constructions. It must NOT imply:
  (a) the gate is VALIDATED in general (two is not all); (b) a certified baseline exists (the
  gate binding is about the INSTRUMENT's non-vacuity, not about a construction PASSING); (c) the
  composite question is answered (the "two constructions" are about hop1/floor admissibility,
  not composite certification). BYTE-CHECK: confirm "two independent constructions" refers to
  the gate's DEMONSTRATED NON-VACUITY (Paper 2's actual thesis — the gate catches real
  failures), not to a positive composition result; and confirm "two" is not generalized to "the
  gate is established."
```

## The standards for the TL's ten primary checks (each a byte-check on the filed draft)

```text
1. CONSTRUCTIBILITY/MEASUREMENT-VALIDITY FRAMING — the V3/hop1 finding must be framed as about
   the INSTRUMENT and the CONSTRUCTION's measurability, not about the model. This is Paper 2's
   actual contribution (correctness ≠ constructibility); the delta must extend that, not drift
   to a model-behavior claim.
2. PRE-STRESS — the draft must state the program is still pre-stress (no certified stressable
   baseline exists). If the delta implies V3 is a stress-ready baseline, HOLD.
3. NO COMPRESSION/INT8/INT4/CLAIM-C/SEAM/PAPER-B — none may be implied. The seam-leak is the
   one to watch hardest in a PAPER (it travels furthest): a paper sentence implying "the
   instrument can now measure the seam" is the funder-natural overclaim the three papers refused.
4. COMPOSITE QUESTION UNANSWERED — the draft must state the composite is not certified/answered;
   the V3 finding is about hop1/floor admissibility, upstream of composite certification.
5. HOP1 FAILURE AS V3 CROSS-MATERIALIZATION INADMISSIBILITY, NOT MODEL INCAPABILITY — the exact
   bound from the stability prereg: "hop1 not admissible across V3 materializations," never "the
   model cannot do hop1." (And contingent on the stability run having produced this — check 2 above.)
6. HOP2 AS INTERNAL FP16 GATE-DISCRIMINATION CONTROL, NOT CERTIFIED STRESS TARGET — hop2 is the
   control that makes a hop1/composite read interpretable, never itself a certified target.
7. P-ROLE AS POSITIONAL/STRUCTURAL CO-OCCURRENCE — see the P-role leash section below.
8. NO MECHANISM LANGUAGE — no binding, attention, reasoning-failure, shortcut-mechanism,
   identity-resolution-mechanism, or causal explanation. In a paper this includes SUGGESTIVE
   mechanism framing, not just explicit labels — "the model loses track of…" is mechanism in
   prose clothing. BYTE-CHECK at the sentence level for implied causation.
9. V3 CONFORMS TO FORECLOSE-ALL STANDARD, NOT CERTIFIED-COMPLETE — see the watchpoint phrase.
10. EVIDENCE LIMITED TO ONE MODEL, ONE CLOSED-WORLD TWO-HOP TASK FAMILY — the generalization
    boundary must be explicit: Qwen2.5-3B, FP16, greedy, one synthetic key-value family. No
    cross-model or cross-family generality claimed.
```

## The specific items the TL asked me to rule on — all DEFERRED to bytes, with their standards

```text
- WHETHER THE P-ROLE LEASH IS SUFFICIENT: cannot rule without the sentences. STANDARD: P-role
  must appear ONLY as a positional/structural CO-OCCURRENCE rate (where the wrong hop1 prediction
  landed), explicitly NOT a cause, NOT a mechanism, and — if the hop1-stability run hasn't
  produced the fresh-block P-role result — NOT stated as a confirmed pattern (it is a
  hypothesis-tested-on-fresh-data per the prereg, and the paper cannot assert a result the run
  hasn't yielded). "Sufficient leash" = co-occurrence framing + no causal verb + result actually
  exists. I check all three against the bytes.
- WHETHER THE ABSTRACT REMAINS CLAIM-SAFE: cannot rule without the abstract. The abstract is the
  HIGHEST-RISK sentence-for-sentence text in any paper — it is what gets read and quoted in
  isolation. STANDARD: every claim in it must survive being read with zero surrounding context
  (the excerpt test), must carry no capability/mechanism/seam/certification implication, and must
  scope to the one-model/one-family boundary. I read it word by word when it exists.
- WHETHER §3.3 AND §4.6 REMAIN BOUNDED: cannot rule without those sections. STANDARD: each must
  hold whatever bounded claim Paper 2 already makes and not let the V3 delta inflate it; the V3
  material is a SECOND independent construction demonstrating the gate's non-vacuity, not a
  strengthening toward a positive composition result.
- WHETHER APPENDIX A CLAIM-LEDGER LANGUAGE IS SAFE: cannot rule without the ledger entries.
  STANDARD: the ledger is where claims are stated most baldly (stripped of hedging prose), so it
  is where overclaim is easiest to spot AND most dangerous — each entry must be a validity/
  constructibility statement with its evidence scope and its NOT-claims attached, never a
  capability or seam entry. I check each entry against its evidence.
```

## The one structural point I CAN make without the bytes

```text
A PAPER is the object where the program's standing "validity is not capability" line faces its
hardest test, because a paper's job is to state a CONTRIBUTION, and the pull is to make the
contribution sound as strong as possible for external readers. The delta integrates V3 as a
"second independent construction" — and the safe version of that contribution is precise and
worth stating plainly: Paper 2's thesis is that the gate is NON-VACUOUS (it catches real
constructibility failures), and a second construction (V3) that the gate also correctly handles
STRENGTHENS THE NON-VACUITY CLAIM — the gate catches failures on two independent constructions,
not one. That is a real, defensible contribution and it is ENTIRELY an instrument claim. The
failure mode is letting "second construction" drift into "progress toward a positive result" —
toward "we're getting closer to a constructible baseline / the seam." The delta is safe if it
says "the gate is demonstrated non-vacuous across two constructions" and unsafe if it says
anything that reads as "V3 is closer to passing." I cannot tell which it says without the bytes;
this is the axis to check hardest when it arrives.
```

## Recommendation

```text
1. File the delta draft to a readable repo path (or paste) WITH a digest. The HOLD lifts on
   sight and I perform the actual sentence-level review — which for a paper is the whole job.
2. CRITICAL PRECONDITION I flag now: confirm the hop1-stability RUN has actually executed and
   produced results before the delta asserts "stable across draws" or a fresh-block P-role
   pattern. I have reviewed the hop1-stability PREREG (PASS) but have seen NO hop1-stability RUN
   RESULT. A paper delta that states cross-draw stability or a confirmed P-role landing as
   findings, when the run that would produce them has not been authorized or executed, is
   asserting results that do not yet exist — the single largest claim-risk exposure for this
   object, and it is independent of wording. If the delta is written ahead of the run, that is a
   FAIL-shaped problem regardless of how carefully the phrases are bounded.
3. Do not advance to CS provenance review until claim-risk clears the actual bytes — for a paper,
   "filed ≠ reviewed" is most expensive of all, because the output is public and permanent.
Requires: the filed draft + digest; confirmation the hop1-stability run results exist (precond. 2).
Authorization implication: none.
```

## Boundaries checked

```text
- No verdict on unread bytes: object confirmed absent from reach (clone at 539a530, exhaustive
  find/grep incl. all four watchpoint phrases returning zero, papers/ tree, uploads) and HELD.
- Unlike prior prereg holds, NO substantive sentence-level rulings pre-loaded — only the STANDARD
  each phrase/section must meet — because prose claim-risk cannot be adjudicated from structure.
- Flagged the precondition (hop1-stability RUN results must exist before the delta asserts
  cross-draw stability or a confirmed P-role pattern) as the object's largest exposure, independent
  of wording.
- No experiment, redesign, compression, INT8/INT4, Claim C, Paper B, certification, capability, or
  mechanism claim authorized or made. The K=5 FAIL stays closed.
```

---

**The one to carry up:** I cannot verdict the Paper 2 V3 delta draft because the object is not in my reach — cloned fresh at HEAD `539a530`, and find/grep for the filename and for all four watchpoint phrases ("stable across draws," "foreclose-all redesign," "gate is shown binding," "hop1 shortfall is not reducible…") return ZERO matches anywhere in the tree; the papers/ directory holds the existing Paper 2 but no V3 delta, the TL notice gives no path or digest, and it is not in uploads. The access HOLD lifts the instant it is filed or pasted with a digest. This object differs from prior unreadable preregs in a way worth stating: a prereg's claim safety is structural (thresholds, decision rules) and can be pre-adjudicated; a PAPER delta's claim safety lives in exact wording, the caveats that travel attached to each phrase, and what an external reader takes from a sentence stripped of governance context — so I can pre-load the STANDARD each watchpoint phrase must meet ("not reducible to position/rank" = not-explained-by-that-named-route, never cause-isolated or all-routes-impossible; "stable across draws" = cross-materialization verdict unanimity, never a model property; "foreclose-all redesign" = the design-standard name, never certified-complete; "gate binding and discriminating across two constructions" = the gate's demonstrated NON-VACUITY on two independent constructions, never general validation or a positive composition result or a certified baseline) but I cannot SCORE any of them, the abstract, §3.3, §4.6, or the Appendix A ledger without the sentences, and scoring them is the whole job on a paper. The single largest exposure, independent of wording and flagged now: I have reviewed the hop1-stability PREREG (PASS) but have seen NO hop1-stability RUN RESULT, so a delta that asserts "stable across draws" or a confirmed fresh-block P-role landing as findings would be stating results from a run that has not been shown to exist — a FAIL-shaped problem no amount of careful phrasing fixes. File the draft with its digest and confirm the stability-run results exist; until then this holds, and a paper is the object where "filed ≠ reviewed" is most expensive because the output is public and permanent.

— Contributor 5
