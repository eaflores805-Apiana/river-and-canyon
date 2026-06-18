# C5 RETURN — V3 Composite Gate Preregistration v0.2 Claim-Risk

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead · **Cc:** CS, Senior, New Senior, Manager
**Date:** 2026-06-18
**Object requested:** `PREREGISTRATION — V3 COMPOSITE GATE (Path A) v0.2`
**Status:** review return. Authorizes nothing; locks nothing.

---

## Verdict

```text
HOLD — ARTIFACT ACCESS (filing-not-yet-propagated variant).

This is a routing-order situation, not the usual "filed somewhere unreadable": the TL notice
instructs CS to FILE v0.2 and, in the same notice, asks C5 to REVIEW it — but the filing step
is upstream of the review step, and the bytes are not on the remote I can fetch.

Checked this turn:
  - Fresh clone at HEAD 294847d16506a9680f758f3dab3960a7e0944592.
  - find . for *COMPOSITE-GATE* / *COMPOSITE*GATE*v0.2* → no file.
  - in-review currently holds only PREREGISTRATION-V3-COMPOSITE-CERTIFICATION-v0.1.md
    (the prior-title v0.1); the v0.2 composite-GATE rename is not yet committed at this HEAD.
  - The TL notice carries NO digest for v0.2, so even were a copy located there is nothing to
    verify identity against.
  - /mnt/user-data/uploads/ → only the Hash-Integrity files.
```

A pre-registration is lock-before-look, and one carrying gate/certification semantics is the
highest-stakes object to clear unread — so the HOLD stands. It lifts the instant CS's filing
lands at the readable path WITH a digest in the filing return (the TL's CS-action block already
requires CS to return the sha256 + clean-fetch confirmation; I verify against that). The eight
standing rulings are mapped to the TL-described fixes below and pre-loaded, so the verdict
converts to PASS on sight IF the bytes match the description.

## 0. Important scope note — I am confirming a DESCRIPTION, not the bytes

```text
The TL notice ENUMERATES what v0.2 changed. I can confirm that the DESCRIBED changes, IF
present in the bytes as described, resolve my eight standing rulings — but a description of a
fix is not the fix, and this seat does not clear a claim boundary on a changelog. Every line
below is "resolved IF the bytes match"; the actual PASS waits on the filed object. This is the
same discipline that caught the wrong "80/96 = hop2 failure" inference last turn: the bytes,
not the summary, decide.
```

## Rulings-to-fixes mapping (TL-described; each marked for byte-confirmation)

```text
RULING 1 (title) — TL says: retitled "Composite Certification" → "Composite Gate."
  IF the title and all in-text self-references read "Composite Gate," resolved. BYTE-CHECK: the
  RENAME must be complete — not just the title line, but every internal "certification" that
  should now read "gate," or a half-rename leaves "certification" language live in the body.

RULING 2 (success language) — TL says: "certifies composition" → bounded validity language.
  IF the success language reads "behavior consistent with two-hop composition under
  foreclose-all controls" (not "the model composes"), resolved. BYTE-CHECK: confirm the bounded
  form appears at EVERY success-outcome statement (§9 decision rule, the outcome labels, the
  carry-up line), not only once — the over-read re-enters wherever the short form survives.

RULING 3 ("via the correct chain") — TL says: replaced with "returns the correct-chain target
  C* under controls." IF so, resolved (output statement, not path claim). BYTE-CHECK: confirm
  no residual "via/through/traverses the correct chain" phrasing elsewhere.

RULING 4 (seen 80/96 barred) — TL says: the already-seen floor-check composite is barred from
  gate use. IF the prereg states the floor-check composite is informational-only and excluded
  from gate data, resolved. (Verified context: the floor-check composite is the "80/96" — last
  turn I confirmed from the run bytes that hop2 was 96/96 and the composite was the informational
  result; barring it from gate data is correct.)

RULING 5 (fresh disjoint seeds) — TL says: floor-check 001..096, composite-gate 097..192.
  THIS IS THE ONE I FLAG FOR THE HARDEST BYTE-CHECK (see §1 below). At the description level the
  ranges are disjoint (097..192 ∩ 001..096 = ∅). BYTE-CHECK required: that the prereg DECLARES
  097..192 as an exact locked range AND that this is mechanically realizable (CS's feasibility
  item 2 flags the generator may have lacked --start-index — if it can't start at 097, the
  declared range is aspirational, and "fresh disjoint" is not yet provable). Claim-risk needs
  the range DECLARED; CS needs it MECHANICALLY TRUE; both before lock.

RULING 6 (two distinct thresholds) — TL summary does NOT explicitly confirm the 0.75 reliability
  gate and 0.45 not-shortcut floor are kept DISTINCT and separately-reported. BYTE-CHECK
  REQUIRED: confirm (a) both are present, (b) reported separately and never averaged/collapsed,
  (c) 0.45 is the construct-DERIVED F+margin (0.20+0.25), not a re-declared free number (the
  OI-3 free-number failure must not reappear), and (d) the prereg states clearing 0.75 does NOT
  exempt the 0.45 floor — BOTH required. This is the one ruling the TL's fix-list does not
  visibly address, so it is the most likely to be under-resolved.

RULING 7 (gate-cleared-this-run ≠ final certification) — TL says: separates GATE-CLEARED-THIS-RUN
  from FINAL certification. IF the prereg pre-commits that one clean PASS yields only
  gate-cleared-this-run and names the separate path to final certification, resolved. BYTE-CHECK:
  confirm the single-run outcome CANNOT be read as final-certified anywhere, symmetric with the
  one-clean-fail "evidence-toward-not-final" asymmetry.

RULING 8 (forbidden interpretations) — TL says: strengthened — no capability, mechanism, seam
  evidence, compression readiness, Claim C, Paper B. IF the block carries all of these AND
  explicitly pre-blocks "cleared gate → seam can be tested" (the single most dangerous over-read
  for this object, per my prior return), resolved. BYTE-CHECK: confirm "no seam evidence" is
  present explicitly, since a composite PASS is the closest the program comes to a positive
  result and the seam-leak is the highest-pull misread.
```

## 1. The one byte-check to prioritize when the object lands — seed-range provability

```text
Ruling 5 is the load-bearing one because it is where claim-risk and feasibility intersect. The
"fresh run" claim — the thing that makes the gate's data independent of the already-seen
composite — is only as good as the disjointness being MECHANICALLY TRUE, not just declared.
The TL notice asks CS (feasibility item 2) to confirm whether v3_item_generator.py now supports
--start-index, because a prior CS review found it lacked one. If the generator cannot actually
start materialization at index 097, then "composite-gate seeds 097..192" is a declared intention
the tooling cannot execute, and the fresh-disjoint guarantee fails silently. So my Ruling-5
clearance is explicitly CONTINGENT on CS confirming the generator can produce 097..192 as
byte-distinct items — claim-risk needs the range declared in the prereg; CS needs it realizable;
neither alone is sufficient. This is the same "hashes/declarations bind concepts only if the
bytes back them" lesson: a declared disjoint seed range that the generator can't realize is a
concept without its bytes.
```

## 2. The standing critical guard (carried, unchanged)

```text
A composite-gate PASS would be the program's FIRST positive composition-consistent result after
a long chain of negatives — the moment of maximum temptation to overclaim. Every ruling above is
a guard on that pull. The byte-check must confirm that even a clean PASS yields ONLY "the V3
composite baseline shows behavior consistent with two-hop composition under foreclose-all
controls, gate-cleared this run" — scoped, single-run, not capability, not mechanism, not seam
evidence, not final certification. If the filed v0.2's success language says more than that
anywhere, that is the validity→capability step the program exists to refuse, and it is a HOLD
regardless of how many other rulings are resolved.
```

## Recommendation

```text
1. CS files v0.2 at the readable path and returns the sha256 + clean-fetch confirmation (the TL
   notice already requires this). On that filing, this HOLD lifts and I review the actual bytes.
2. On review, the priorities are: Ruling 6 (the two-threshold distinctness the TL fix-list does
   not visibly confirm), Ruling 5 + §1 (seed-range declared AND CS-confirmed realizable), and the
   §2 success-language guard (no over-read at any success statement). If those three hold in the
   bytes and Rulings 1–4,7,8 match the description, this converts to PASS.
3. Do not lock until claim-risk clears the actual bytes AND CS confirms the generator can realize
   097..192 (Ruling 5 is not provable on description alone).
Requires CS verification: the filing + digest; the generator --start-index / 097..192
realizability; the two new tooling artifacts' lockability. Authorization implication: none.
```

## Boundaries checked

```text
- No verdict on unread bytes: v0.2 confirmed not-yet-at-readable-HEAD (clone at 294847d;
  in-review holds only the v0.1 certification-titled draft) and HELD; the rulings-to-fixes
  mapping is explicitly a DESCRIPTION confirmation, not a byte clearance, with every line marked
  byte-check-required.
- No run, materialization, prompt generation, tooling creation, compression, INT8/INT4, Claim C,
  or Paper B authorized or proposed. This return sets no threshold and recommends no path.
- Certification/gate treated as a bounded validity outcome, never capability; single-run bounded
  as gate-cleared-this-run; the seam-leak flagged as the priority over-read; the K=5 FAIL stays
  closed.
```

---

**The one to carry up:** I cannot verdict the V3 composite gate prereg v0.2 because its bytes are not yet at a readable HEAD — this is a routing-order situation (the TL notice asks CS to FILE v0.2 and asks C5 to REVIEW it in the same notice, but the filing is upstream and hasn't propagated; the clone at `294847d` still shows only the v0.1 certification-titled draft in-review), and the notice carries no digest to verify against regardless. The access HOLD lifts the instant CS's filing lands at the path with the sha256 the TL notice already requires. I can confirm the TL-DESCRIBED changes map onto my eight standing rulings, but a changelog is not the bytes — so every mapping is "resolved IF the bytes match," and three need the hardest byte-checks when the object lands: Ruling 6 (the 0.75 reliability gate and 0.45 not-shortcut floor kept distinct, separately reported, with 0.45 confirmed as the construct-derived F+margin not a free number — the one ruling the TL fix-list does NOT visibly confirm, so most likely under-resolved); Ruling 5 (the declared disjoint seeds 097..192 vs floor-check 001..096 are disjoint as described, BUT the clearance is contingent on CS confirming v3_item_generator.py can actually start at index 097 — a prior CS review found it lacked --start-index, and a declared range the generator can't realize is "fresh disjoint" in name only); and the standing success-language guard (a composite PASS would be the program's first positive composition-consistent result, the moment of maximum temptation, so the bytes must show even a clean PASS yields only a scoped single-run validity statement — never the model composes, the seam is open, or final certification, with "no seam evidence" explicitly in the forbidden block). File v0.2 with its digest and the verdict converts on sight; do not lock until claim-risk clears the actual bytes and CS confirms 097..192 is mechanically realizable.

— Contributor 5
