# C5 RETURN — Revised Paper 2 Integrated Manuscript Claim-Risk

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead · **Cc:** Senior, CS, New Senior, Manager
**Date:** 2026-06-19
**Object requested:** `PAPER-2-REVISED-MANUSCRIPT-DRAFT-v0.1`
**Status:** review return. Authorizes nothing.

---

## Verdict

```text
HOLD — ARTIFACT ACCESS. The integrated manuscript is not in this seat's reach, and an integrated
PAPER manuscript must be reviewed as actual bytes — the whole point of an integration review is to
catch interactions between old and new prose, which cannot be assessed from the delta and the
old manuscript separately.

Checked exhaustively this turn:
  - Fresh clone at HEAD aec03ffdb97349397c16805088fdd5ab0ed56621.
  - find . for *PAPER-2-REVISED* / *PAPER-2*MANUSCRIPT* / *REVISED*/*integrated* (paper/manuscript)
    → no integrated manuscript file.
  - path-a/in-review holds the V3 DELTA draft and an INTEGRATION-PLAN, but NOT the integrated
    manuscript.
  - papers/paper2-correctness-is-not-constructibility/ holds the EXISTING (pre-delta) Paper 2 —
    grep for V3/foreclose-all/hop1-stability returns ZERO, confirming it has not yet been
    integrated.
  - /mnt/user-data/uploads/ → only the Hash-Integrity files.
The integrated revised manuscript has not been filed to a readable path, nor pasted.
```

The HOLD lifts the instant the integrated manuscript is filed to a readable repo path (or pasted)
WITH a digest I can verify against.

## 0. Two things I CAN establish from bytes this turn (so the HOLD is not bare)

```text
(1) FIVE OF THE SIX WATCHPOINTS ARE ALREADY ADJUDICATED. The delta byte-review (976b1b09…,
    this session) cleared, at the sentence level, the exact phrases the TL re-lists:
      - "the persistence of the hop1 shortfall under it indicates the shortfall is not reducible
        to that route" — CLEARED (not-explained-by-the-foreclosed-route, not cause-isolated).
      - "the shortfall is stable across draws" — CLEARED (cross-materialization verdict unanimity,
        backed by the byte-verified HOP1-STABLE-INADMISSIBLE run; not a model property).
      - "foreclose-all redesign" — CLEARED (design-standard name, "conforms not certified-complete"
        stated verbatim).
      - "the baseline gate is shown binding and discriminating" — CLEARED (gate NON-VACUITY across
        two constructions, never general validation / certified baseline / positive result).
      - "second construction isolates the component-precondition failure" — CLEARED (it isolates
        the precondition failure FROM the position confound the first construction could not
        separate — an instrument/measurement statement, not a model-incapability claim).
    These clearances CARRY FORWARD to the integrated manuscript IF AND ONLY IF the integrated bytes
    contain these sentences unchanged. That is the byte-check when the object lands: confirm the
    five cleared sentences are byte-identical in the integrated manuscript, not silently reworded.

(2) THE SIXTH WATCHPOINT IS PRE-EXISTING PAPER 2 LANGUAGE, AND I VERIFIED IT AGAINST THE EXISTING
    BYTES. "natural next step into the stress phase" is NOT new V3 prose — it already exists in the
    published Paper 2 (correctness-is-not-constructibility.md line 440). I read its full context:
      "Single-hop retrieval (hop2) is the one query type that clears the gate at FP16; running it
       … through INT8/INT4 is the natural next step into the stress phase — BUT ONLY AFTER hop2 is
       itself certified shortcut-free … not merely near-ceiling, since by this paper's own argument
       accuracy does not establish constructibility. The first such rung should be framed as
       instrument-validation-under-stress … NOT as composition or seam evidence. … it remains
       gated …. No stress rung has yet been run on this construction."
    IN ITS EXISTING FORM THIS PHRASE IS SAFE: the "natural next step" is fully leashed — gated on a
    hop2-specific shortcut/position probe, explicitly framed as instrument-validation-not-seam, and
    closed with "remains gated / no stress rung run." The hedge holds in the existing manuscript.
    BYTE-CHECK when the integrated object lands: confirm the integration PRESERVED this leash. The
    risk is NOT the phrase itself (it is sound as written) — it is that integrating the V3 material,
    which now shows hop2 holding across SIX fresh materializations, could make "natural next step …
    stress hop2" read as MORE licensed (hop2 looks more robust now), eroding the "only after a hop2
    shortcut probe" gate. The delta already guards this ("strengthens the control but does not
    promote it"; §7 "not a green light to stress hop2"), so the integrated manuscript is safe IF it
    keeps BOTH the existing leash AND the delta's not-a-green-light language adjacent and intact.
```

## 1. The integration-specific risk neither prior review could show (the reason this object needs its own read)

```text
The delta cleared in isolation; the existing Paper 2 is sound. Integration introduces a THIRD
thing neither review covered: INTERACTION between old and new prose. The specific risks to
byte-check when the manuscript lands:

A. CONTRADICTION / DOUBLE-COUNTING. The existing Paper 2 §9 already calls for "decouple position
   from rank … take a constructible task to stress." The V3 delta REALIZES that call (V3 IS the
   decoupled construction; its §9 revision reports the result). The integrated §9 must not read as
   if the call is still OPEN (it was answered by V3) NOR as if V3 fully closed it (it did not — the
   precondition was stable-inadmissible). The integrated future-work must state the call was
   realized AND returned a negative constructibility result, without either erasing the original
   framing or implying more closure than the run delivered.

B. THE "STRESS PHASE" PHRASE × THE NEW hop2 ROBUSTNESS (above). The single highest interaction
   risk: existing §9's "natural next step … stress hop2" now sits in a manuscript where §4.6 reports
   hop2 holding across six fresh materializations. Adjacent, these could read as "hop2 is now robust
   enough to stress." The leash must survive integration: confirm the integrated manuscript keeps
   "only after a hop2-specific shortcut/position probe" AND "not a green light to stress hop2" in
   force, and that the six-materialization hop2 result is still framed as an internal control, not
   evidence hop2 is stress-ready.

C. ABSTRACT × FULL-BODY CONSISTENCY. The delta's revised abstract was cleared standalone. Integrated,
   the abstract must not claim more than the integrated body delivers, and the body must not contain
   a claim the abstract's hedges don't cover. Byte-check the abstract against the integrated §§4.6/5/9.

D. CLAIM-COUNT CONSISTENCY. The existing Appendix A and the delta's Appendix A update must reconcile:
   Claim B strengthened (two constructions), Claim #5 still blocked-on-precondition, Claim C untouched.
   Confirm no double-entry or version-mismatch in the integrated ledger, and the "Claim B" vs forbidden
   "Paper B" distinction held.
```

## 2. The TL's twelve checks — status

```text
Checks 1–12 map to sentence-level judgments I made on the delta sections (cleared) PLUS the
existing Paper 2 sections (the abstract, §5, §7, §9, Appendix A as they stand pre-integration).
I CANNOT confirm any of them on the INTEGRATED manuscript without its bytes, because integration is
where a cleared delta sentence and a sound existing sentence can interact into an overclaim neither
had alone (§1). Every check is "carries forward IF the integrated bytes preserve the cleared
language AND the interactions A–D are clean." The two I will check hardest when the object lands:
check 5 (§5 does not convert gate non-vacuity into certification/positive composition — the
load-bearing contribution claim) and check 8 (§9 does not green-light compression/hop2-stress/
Claim-C/seam — the interaction-B risk).
```

## 3. The items the TL asked me to rule on — deferred to integrated bytes, with their standards

```text
- ABSTRACT SAFETY: the delta abstract cleared standalone (excerpt test passed). Integrated standard:
  it must remain excerpt-safe AND consistent with the integrated body (§1.C). Re-read word-by-word
  on filing.
- §3.3 / §4.6: cleared in the delta. Integrated standard: byte-identical, and §4.6's reference to the
  existing §4.2/§4.3 must resolve correctly in the integrated numbering (a dangling cross-reference is
  a provenance bug, not a claim bug, but a MIS-resolved one — pointing at the wrong section — could
  change meaning; check the cross-refs).
- §5 / §7 / §9: §5 must not convert non-vacuity to certification (check 5); §7's revised limitation
  ("Two constructions, one model and task family") must be present and not weaker than the existing
  limitation; §9 must keep the stress-phase leash (interaction B). Re-read on filing.
- APPENDIX A CLAIM-LEDGER: §1.D reconciliation. Claim #5 blocked, Claim C untouched, Claim B vs Paper
  B distinct, no double-entry.
- P-ROLE LEASH: cleared in the delta (352/352, positional/structural co-occurrence, witness-triple
  named). Integrated standard: byte-identical and not re-described elsewhere in the integrated body in
  looser terms. Check for any OTHER mention of the P-role landing in the integrated manuscript that
  might not carry the leash.
```

## 4. Recommendation

```text
1. File the integrated manuscript to a readable path (or paste) WITH a digest. The HOLD lifts on
   sight and I perform the integrated sentence-level review — focused on the interactions (§1 A–D)
   that the delta and existing-manuscript reviews could not cover, plus confirmation that the five
   already-cleared watchpoint sentences and the existing stress-phase leash are byte-preserved.
2. The efficient path, given the delta is already cleared: the integration review is primarily a
   DIFF review — confirm the integrated manuscript = (existing Paper 2) + (cleared delta blocks) with
   NO other claim-bearing changes, and that the splice points (§1 A–D) don't create interactions. If
   CS or the SE can provide the integrated manuscript with the delta-insertion points marked, the
   review is faster and the interaction risks are easier to localize. Not required, but it targets the
   actual risk.
3. Do not advance to CS provenance review until claim-risk clears the integrated bytes — for an
   integrated manuscript headed toward release, "filed ≠ reviewed" remains most expensive.
Requires: the integrated manuscript + digest. Authorization implication: none.
```

## 5. Boundaries checked

```text
- No verdict on unread bytes: integrated manuscript confirmed absent from reach (clone at aec03ff,
  exhaustive find/grep, in-review holds delta+plan only, papers/ holds the pre-delta Paper 2,
  uploads) and HELD.
- The five watchpoint sentences already cleared in the delta byte-review (976b1b09…) carry forward
  CONTINGENT on byte-preservation; the sixth ("stress phase") verified SAFE in the existing Paper 2
  bytes, contingent on the integration preserving its leash.
- Integration-specific interaction risks (A–D) named as the reason this object needs its own read.
- No experiment, redesign, compression, INT8/INT4, Claim C, Paper B, certification, capability, or
  mechanism claim authorized or made. The K=5 FAIL stays closed.
```

---

**The one to carry up:** I cannot verdict the revised integrated Paper 2 manuscript because the object is not in my reach — cloned at HEAD `aec03ff`, and find/grep shows path-a/in-review holds only the V3 DELTA draft and an integration PLAN, while papers/ holds the EXISTING pre-delta Paper 2 (zero V3 content); the integrated manuscript is filed nowhere readable and is not in uploads, and the TL notice carries no digest. The access HOLD lifts the instant it is filed or pasted with a digest. Two things I established from bytes so the hold is not bare: first, FIVE of the six watchpoint phrases were already adjudicated and cleared at the sentence level in the delta byte-review this session ("not reducible to that route," "stable across draws," "foreclose-all redesign," "gate shown binding and discriminating," "second construction isolates the component-precondition failure") — these carry forward to the integrated manuscript ONLY IF the integrated bytes preserve those sentences unchanged, which is the byte-check on filing. Second, the sixth watchpoint, "natural next step into the stress phase," is NOT new V3 prose — it already exists in the published Paper 2 (line 440), and I read its full context: it is SAFE as written, fully leashed (gated on a hop2-specific shortcut/position probe, framed as instrument-validation-not-seam, closed with "remains gated / no stress rung run"). The reason this integrated object still needs its own read, which neither the delta review nor the existing manuscript could provide, is INTERACTION between old and new prose: the highest risk is that existing §9's "stress hop2 is the natural next step" now sits in a manuscript where the integrated §4.6 reports hop2 holding across six fresh materializations, which adjacent could read as "hop2 is now robust enough to stress" — so the byte-check must confirm the integration keeps BOTH the existing "only after a hop2 shortcut probe" leash AND the delta's "not a green light to stress hop2" language intact; plus three more splice-point interactions (the §9 future-work must show V3 REALIZED the original "decouple position from rank" call AND returned a negative result, without erasing the call or implying more closure than the run delivered; abstract-vs-integrated-body consistency on the excerpt test; and Appendix A ledger reconciliation with no double-entry and Claim B kept distinct from forbidden Paper B). The efficient path is a DIFF review: confirm integrated = existing Paper 2 + cleared delta blocks with no other claim-bearing changes and clean splice points; marked insertion points would localize the interaction risk. File the integrated manuscript with its digest and the review proceeds focused on those interactions; CS provenance review waits on this clearance, and the K=5 FAIL stays closed.

— Contributor 5
