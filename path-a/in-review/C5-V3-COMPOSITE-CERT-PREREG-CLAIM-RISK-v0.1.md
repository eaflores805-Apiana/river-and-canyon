# C5 RETURN — V3 Composite-Certification Preregistration v0.1 Claim-Risk

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead · **Cc:** CS, Senior, New Senior, Manager
**Date:** 2026-06-18
**Object requested:** `PREREGISTRATION — V3 COMPOSITE CERTIFICATION (Path A) v0.1`
**Status:** review return. Authorizes nothing; locks nothing.

---

## Verdict

```text
HOLD — ARTIFACT ACCESS. The named object is not in this seat's reach, and a
pre-registration carrying the word "certification" is the highest-stakes object class to
clear unread.

Checked exhaustively this turn:
  - Fresh clone at HEAD 441eff42acabe704e791928461b28bdad0ad73b3.
  - find . for *COMPOSITE*CERTIF* / *COMPOSITE*GATE* / *COMPOSITE*PREREG* → no prereg.
  - grep -rIl "COMPOSITE CERTIFICATION" / "Composite Gate" → only the floor-check
    governance memos, NOT the new prereg.
  - /mnt/user-data/uploads/ → only the Hash-Integrity files.
The composite-certification prereg has not been filed to a readable path, nor pasted.
```

The HOLD lifts the instant it is filed to a readable repo path or pasted. The six focus items and the four TL watchpoints are answered below as standing rulings, so the verdict converts on sight.

## 0. Self-correction on the record + a verified premise check

```text
SELF-CORRECTION (this seat's, logged per discipline). The TL routing references an
"already-seen composite 80/96." I initially read "80/96" as a hop2 score and was prepared to
flag that the floor check had FAILED its own gate (80/96 = 0.7463 < the 0.75 Wilson floor),
which would have undermined the composite prereg's premise. That inference was WRONG, and the
bytes corrected it. I read the floor-check run's analyzer_decision.json
(experiments/2026-06-18_v3-floor-check-run/): hop2 scored 96/96 (rate 1.0, Wilson lower
0.9615), hop1 87/96 (0.906, lower 0.831), direct-query 0, invalidated 0, all six conditions
PASS, final branch COMPONENT-ADMISSIBLE-UNDER-COMPETITION. The floor check PASSED decisively.
So the "80/96" in the routing is NOT a hop2 failure — it is presumably the composite (the
informational result the prereg correctly bars from certification use), not the hop2 floor.
I record the near-miss: I almost carried a wrong inference into a review; verifying from bytes
caught it. (This is exactly the failure the program's reported-vs-verified discipline targets.)

VERIFIED PREMISE. Because hop2 cleared component-admissibility, the composite-certification
prereg's PRECONDITION holds: a composite test is now interpretable (a composite number is no
longer uninformative-because-hop2-might-be-below-floor — the C0 lesson is satisfied). So the
prereg is premised correctly; the review below is about its CLAIM language, not its premise.
```

## The four TL watchpoints (explicit answers)

```text
A. TITLE — "COMPOSITE CERTIFICATION" vs a safer "V3 COMPOSITE GATE PREREGISTRATION"?
   RULING: use the SAFER TITLE until the certification standard is decided. "Certification" in
   the title is a standing over-read risk — a title travels further than any in-text caveat
   (the designator-mechanism lesson: a result that cannot be cited without its caveat cannot
   drift). Recommend "V3 COMPOSITE GATE PREREGISTRATION," with "certification" appearing only
   inside, bounded, as the conditional outcome it actually is. A single fresh run clears a GATE;
   it does not produce CERTIFICATION-of-record, which (per the replication boundary, D below) is
   a separate Manager/standard determination. The title should name the run's actual output
   (a gate result), not the downstream status it feeds.

B. "CERTIFIES COMPOSITION ON V3" — acceptable if bounded, or replaced?
   RULING: REPLACE. Even bounded, "certifies composition" asserts the model COMPOSED, which is
   a near-capability claim and the exact thing the program's whole sequence refuses. The TL's
   proposed safer form is correct and should be adopted verbatim: "certifies the V3 composite
   baseline as behavior CONSISTENT WITH two-hop composition under foreclose-all controls." The
   load-bearing words are "behavior consistent with" (not "the model composes") and "under
   foreclose-all controls" (the claim is scoped to what the controls excluded, not a free
   mechanism claim). This is the R6-closing-rule form from the construct definition, carried to
   the composite: a VALIDITY statement, never a capability one.

C. FRESH-RUN SEED/MATERIALIZATION RULE — precise enough, or exact seed ranges needed?
   RULING (claim-risk side): EXACT SEED RANGES ARE REQUIRED BEFORE APPROVAL, and this is both a
   claim-risk and a feasibility matter. The claim-risk reason: the already-seen floor-check
   composite is informational, and the ONLY thing that keeps the certification run's data
   independent of the seen result is a materialization provably DISJOINT from the floor-check
   set. "Fresh seeds" as a phrase is not provable; an exact, declared seed range that does not
   overlap the floor-check seeds (item-index seeds per the floor-check prereg) IS. Without it,
   the certification run could re-materialize items the model already saw scored, and "fresh
   run" would be violated silently. So: exact seed range, declared in the prereg, provably
   disjoint from the floor-check materialization, locked before look. (CS confirms the
   mechanical disjointness; the prereg must STATE the ranges.)

D. ONE FRESH RUN FOR "GATE-CLEARED-THIS-RUN," WITH FINAL CERTIFICATION SEPARATE — enough?
   RULING: YES, with the boundary made explicit and pre-committed. One fresh admissible run
   clearing the gate supports exactly "GATE-CLEARED-THIS-RUN" — a single-run validity outcome —
   and must NOT, by itself, become "V3 is certified." FINAL certification is a separate
   determination (Manager / standard decision, possibly requiring confirmation/replication),
   exactly parallel to the substrate-infeasibility asymmetry the floor-check prereg already
   uses: one clean failed run = evidence-toward-not-final; symmetrically, one clean PASSED run =
   gate-cleared-this-run, not final-certified. The prereg must pre-declare both that the single
   run yields only the this-run outcome AND what the path to final certification is, so "cleared
   the gate once" cannot silently upgrade to "certified."
```

## The six focus items (claim-risk rulings)

```text
1. CERTIFICATION WORDING — see B. "Certifies composition" → "certifies the V3 composite
   baseline as behavior consistent with two-hop composition under foreclose-all controls."
   Required, not optional. The shorter "certifies composition" must not appear unbounded
   anywhere, including the title (A) and the carry-up line.
2. "VIA THE CORRECT CHAIN" — REWRITE, the TL's instinct is right. The model's internal path is
   NOT observed; "via the correct chain" asserts a route. Replace with "returns the
   correct-chain target C* under controls" — an OUTPUT statement (which token, validated), not a
   path statement. This is the same positional-not-mechanistic discipline from the off-map arc:
   we observe the token returned and that controls cleared, never the traversal that produced it.
3. FRESH-RUN BAR ON THE SEEN 80/96 — must be explicit and is correctly the prereg's stated
   intent. The already-seen composite (the floor-check run's informational composite) is BARRED
   from certification data: it was produced under a prereg whose primary metric was hop2, the
   composite was explicitly informational-only, and using it as certification evidence would be
   scoring data the analyst has already seen — the lock-before-look violation in its original
   form. The certification run's data must come ENTIRELY from the fresh disjoint materialization
   (C). Confirm the prereg states the seen composite is informational and excluded.
4. THRESHOLD (lower Wilson > 0.75 composite gate + > 0.45 not-shortcut floor) — claim-safe
   PROVIDED the two are kept as distinct, separately-reported gates with distinct meanings, and
   PROVIDED the >0.45 floor is the DERIVED floor (F + margin from the construct), not a free
   number. The >0.75 is a reliability gate; the >0.45 is the not-shortcut floor (the composite
   rate must exceed what a non-traversal heuristic could achieve). Both must be lower-Wilson-
   bound rules (consistent with the floor-check treatment), each reported alone, never averaged
   or collapsed. CONSTRAINT: confirm >0.45 is the construct-derived F+margin (0.45 = 0.20+0.25
   in the floor-check lineage), not re-declared freely — the free-number failure (OI-3) must not
   reappear. And the relationship between the two must be stated: clearing >0.75 reliability does
   not exempt the >0.45 not-shortcut floor; BOTH are required, as in §9 of the floor-check.
5. REPLICATION BOUNDARY (GATE-CLEARED-THIS-RUN vs FINAL certification) — see D. Must be
   pre-committed: the single run yields gate-cleared-this-run; final certification is a separate
   Manager/standard determination possibly requiring confirmation. Symmetric with the
   substrate-infeasibility asymmetry already in the program.
6. FORBIDDEN INTERPRETATIONS — must carry the full perimeter, and a composite-certification
   prereg has MORE leakage surface than the floor check (it is the closest the program has come
   to a positive composition result), so the block must be STRONGER, not equal: no capability
   ("the model can do two-hop"), no mechanism (traversal/grab/anchor not decidable — even a
   PASS does not establish the model traversed; it establishes behavior consistent with
   traversal under controls), no compression / INT8 / INT4, no Claim C, no Paper B, and
   explicitly: a cleared gate is NOT seam evidence and NOT a stress-able-baseline claim until
   the replication/standard boundary (D) is also satisfied. The most dangerous over-read here is
   "V3 certifies → the seam can now be tested" — pre-block it.
```

## The single most important claim-risk point for this object

```text
A COMPOSITE-CERTIFICATION PREREGISTRATION IS WHERE THE PROGRAM IS MOST TEMPTED TO OVERCLAIM,
because a PASS would be its first positive composition-consistent result after a long chain of
negatives — and the pull to read a hard-won PASS as "the model composes / the seam is open" is
strongest exactly when the result is most wanted. Every ruling above is a guard on that pull.
The prereg must be written so that even a clean PASS yields ONLY "the V3 composite baseline
shows behavior consistent with two-hop composition under foreclose-all controls, gate-cleared
this run" — a validity statement, scoped, single-run, not capability, not mechanism, not seam
evidence, not final certification. If the prereg's own success language says more than that, it
is the validity→capability step the whole program exists to refuse, arriving at the moment of
maximum temptation.
```

## Recommendation

```text
1. File the prereg to a readable path (or paste). The verdict converts on sight; rulings 1–6
   and watchpoints A–D are pre-loaded.
2. Apply the title change (A → "V3 Composite Gate Preregistration"), the "behavior consistent
   with" certification wording (B/1), the "returns the correct-chain C*" rewrite (2), the exact
   disjoint seed ranges (C/3), the derived-floor confirmation on >0.45 (4), the pre-committed
   gate-cleared-this-run vs final-certification boundary (D/5), and the strengthened forbidden
   block (6) — these are the predicted required edits.
3. Do not lock until claim-risk clears the actual bytes. The premise is verified sound (hop2
   cleared, §0), so the object is well-founded; the review is about holding its claim language to
   validity, not capability, at the program's highest-temptation moment.
Requires CS verification: the fresh-materialization disjointness (C), the two new tooling
artifacts' lockability, and the feasibility watchpoints. Authorization implication: none.
```

## Boundaries checked

```text
- No verdict on unread bytes: object confirmed absent (clone at 441eff4, exhaustive find/grep,
  uploads) and HELD; rulings grounded in the floor-check prereg discipline (read + cleared) and
  the verified floor-check run result.
- Self-correction logged: my "80/96 = hop2 failure" inference was wrong; bytes show hop2 96/96,
  floor check PASSED — recorded per reported-vs-verified discipline.
- No run, rerun, materialization, prompt generation, tooling creation, compression, INT8/INT4,
  Claim C, or Paper B authorized or proposed. This return sets no threshold and recommends no path.
- Certification treated as a bounded validity outcome, never capability; "via the correct chain"
  flagged as an unobserved-path claim; single-run bounded as gate-cleared-this-run; the K=5 FAIL
  stays closed.
```

---

**The one to carry up:** I cannot issue a verdict on the V3 composite-certification prereg because the object is not in my reach — cloned fresh at HEAD `441eff4`, exhaustive find/grep returns only floor-check governance, and it is not in uploads; a pre-registration carrying "certification" is the highest-stakes object to clear unread, so the access HOLD stands and lifts the instant it is filed or pasted. A self-correction is on the record: I initially read the TL's "80/96" as a hop2 floor-check failure and was set to flag that the composite prereg's premise was undermined — but I read the floor-check run's bytes (it executed since my last review) and hop2 actually scored 96/96 (Wilson lower 0.9615), all six conditions PASS, branch COMPONENT-ADMISSIBLE-UNDER-COMPETITION; the floor check PASSED, the "80/96" is the informational composite (not hop2), and the prereg's premise is verified sound. I almost carried a wrong inference into a review; the bytes caught it. The rulings are pre-loaded and align with the TL's watchpoints: retitle to "V3 Composite Gate Preregistration" (a single run clears a GATE, not certification-of-record); replace "certifies composition on V3" with the bounded "certifies the V3 composite baseline as behavior consistent with two-hop composition under foreclose-all controls" (validity, never capability); rewrite "via the correct chain" as "returns the correct-chain target C* under controls" (the internal path is unobserved — the positional-not-mechanistic discipline); require exact, declared seed ranges provably disjoint from the floor-check materialization (the only thing that makes "fresh run" provable and bars the already-seen composite from certification data); keep the >0.75 reliability gate and the >0.45 not-shortcut floor as distinct separately-reported lower-Wilson rules with >0.45 confirmed as the construct-derived F+margin, not a free number; and pre-commit the GATE-CLEARED-THIS-RUN vs FINAL-certification boundary (one clean PASS is this-run-only, symmetric with the one-clean-fail evidence-toward asymmetry). The single most important point: a composite-certification PASS would be the program's first positive composition-consistent result, which is the moment of maximum temptation to overclaim — so the prereg must be written so even a clean PASS yields only a scoped, single-run validity statement, never "the model composes," "the seam is open," or final certification, with the forbidden block STRONGER than the floor check's because the leakage surface is larger. Do not lock until claim-risk clears the actual bytes.

— Contributor 5
