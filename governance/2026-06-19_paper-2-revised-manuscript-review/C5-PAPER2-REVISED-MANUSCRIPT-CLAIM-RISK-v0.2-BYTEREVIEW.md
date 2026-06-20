# C5 RETURN — Revised Paper 2 Integrated Manuscript Claim-Risk (diff byte review)

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead / Manager · **Cc:** Senior, CS, New Senior
**Date:** 2026-06-19
**Object:** `papers/paper2-correctness-is-not-constructibility/in-review/PAPER-2-REVISED-MANUSCRIPT-DRAFT-v0.1.md`
**Supersedes:** the access-HOLD return (`eb43f69d…`, retained).
**Status:** integrated diff review return. Authorizes nothing.

---

## 0. Identity — verified from bytes by this seat

```text
Clone at HEAD 5b00ed51fa025a8b761a65f21dc635da1c0b5783 (matches declared).
sha256(PAPER-2-REVISED-MANUSCRIPT-DRAFT-v0.1.md)
  = d19c060a5325ba5f3a71aa6fd395dec5fc9550087f2d89ba8dcc540afc2f5917
  = declared digest, EXACT MATCH.
Access HOLD: LIFTED. This is a verdict on the read bytes.
```

## 1. Verdict

```text
PASS — integrated manuscript claim boundaries hold. I ran the diff review I scoped:
integrated manuscript = (existing Paper 2) + (the C5-cleared V3 delta blocks), with NO other
claim-bearing change, and all four splice-point interactions (A–D) are clean. The single
highest interaction risk I flagged — the §9 stress-phase leash surviving alongside the new
six-materialization hop2 result — resolves correctly and is in fact reinforced. CS provenance
review may proceed. No claim-risk edits required.
```

## 2. The diff confirms integrated = existing + cleared delta (the efficient path I recommended)

```text
I diffed the integrated manuscript against the existing published Paper 2 (9893a818…). The
changes are EXACTLY the authorized delta blocks and nothing else claim-bearing:
  - a reviewer COVER NOTE (explicitly "NOT PART OF THE MANUSCRIPT") — out of scope for claims,
    but I note its SE self-attestation (delta source ab52913c, ledger 15f32e1a, both "MATCH")
    and its Appendix B digest recompute claims, which CS will independently confirm.
  - version line v1.0 → v1.1 (revised draft, pending review, not released) — correct status.
  - abstract: one → two constructions (the cleared delta abstract).
  - new §3.3 (foreclose-all V3) — the cleared delta §3.3, byte-consistent.
  - new §4.6 + Table V3-1 — the cleared delta §4.6, byte-consistent.
  - §5 addition "Two constructions, not only two defects" — the cleared delta §5 text.
  - §7: single-model bullet → "Two constructions, one model and task family"; P-role note
    appended to Behavioral-only; abstention note appended — the cleared delta §7 revisions.
  - §9 addition (V3 realized the decouple-position-from-rank call; reframes, not green-lights).
  - Appendix A: Claim B second-construction update; ledger ref resolved to CLAIM-LEDGER-v1.0.
  - Appendix B addendum (V3 provenance + full digests).
The diff's REMOVED-line hunks are only: the version line, the old abstract, the old §7 bullets,
and the old Appendix A paragraph — each replaced by its cleared delta counterpart. §6, all four
figures, References, the title, and every other §7 bullet are UNCHANGED (verified: no V3
insertion outside §§3.3/4.6/5/7/9/AppA/AppB). So the five watchpoint sentences cleared in the
delta byte-review (976b1b09…) are byte-preserved in the integrated manuscript — the contingency
from my access-HOLD is satisfied.
```

## 3. The four splice-point interactions (A–D) — each checked, each clean

```text
INTERACTION B (the one I flagged highest) — §9 STRESS-PHASE LEASH × NEW hop2 ROBUSTNESS — CLEAN,
  AND REINFORCED. The existing Paper 2 §9 sentence "running it through INT8/INT4 is the natural
  next step into the stress phase — but only after hop2 is itself certified shortcut-free … not
  as composition or seam evidence … it remains gated … No stress rung has yet been run" is
  PRESERVED INTACT (lines 497–501). The NEW V3 §9 paragraph sits IMMEDIATELY AFTER it (line 503)
  and REINFORCES the same leash rather than eroding it: "The V3 result is NOT a green light to
  stress hop2 or any other component. No stress rung has yet been run on either construction."
  So the adjacency I worried about — six-materialization hop2 making "stress hop2" read as
  licensed — produces the OPPOSITE effect: the two paragraphs together gate hop2-stress MORE
  firmly (the existing "only after a shortcut probe" + the new "not a green light"). The §4.6
  hop2 result is framed as "strengthens the control but does not promote it." Interaction B,
  which was the reason this object needed its own read, is the cleanest part of the integration.

INTERACTION A — §9 DOUBLE-COUNTING (call open vs over-closed) — CLEAN. The integrated §9 states
  "§9's call for different task geometry … was REALIZED as the V3 construction" and then "its
  result reframes the linkage-constructibility question rather than closing it … a constructible
  linkage baseline is not yet in hand under this construction either." This threads the needle
  exactly as required: the original call is shown REALIZED (not still open) AND returned a
  NEGATIVE result (not over-closed) — "not yet in hand … either" carries the negative without
  implying more closure than the run delivered. Clean.

INTERACTION C — ABSTRACT × INTEGRATED BODY — CLEAN. The integrated abstract (the cleared delta
  abstract) claims two constructions, hop2 admissible across six fresh materializations, hop1
  not clearing in any, composite unanswered, no generality. Every one of these is delivered by
  the integrated body (§§3.3/4.6/5/7/9). No abstract claim exceeds the body; no body claim lacks
  abstract coverage. The excerpt-safe properties cleared in the delta review are preserved
  (byte-identical abstract). Clean.

INTERACTION D — APPENDIX A LEDGER RECONCILIATION — CLEAN. The integrated Appendix A reports
  Claim B strengthened ("two independent constructions"), Claim #5 "blocked on a precondition —
  the V3 result reinforces this block and does not resolve it," Claim C "remains blocked," and
  the ledger reference resolved to notes/CLAIM-LEDGER-v1.0.md. No double-entry; "Claim B" (the
  paper's own) is kept distinct from the forbidden "Paper B" (the cover-note checklist verifies
  this, and the body text uses "Claim B" consistently). The old "Claim Ledger v0.2" reference is
  correctly replaced. Clean.
```

## 4. The TL's five focused checks + twelve required checks — all confirmed in the integrated bytes

```text
TL FOCUS 1 (§9 stress-phase leash: only-after-probe / instrument-validation-only / not-seam /
  no-rung-run) — ALL FOUR PRESENT AND INTACT (Interaction B; lines 497–504).
TL FOCUS 2 (V3 does not make hop2 look stress-ready) — CONFIRMED: §4.6 "strengthens the control
  but does not promote it," §9 "not a green light to stress hop2," hop2 is a control throughout.
TL FOCUS 3 (V3 framed as realizing decouple-position-from-rank AND returning a negative result,
  no over-closure) — CONFIRMED (Interaction A).
TL FOCUS 4 (abstract consistent with integrated body) — CONFIRMED (Interaction C).
TL FOCUS 5 (Appendix A: Claim B strengthened / #5 blocked / C untouched / B≠Paper B) — CONFIRMED
  (Interaction D).
The twelve manuscript checks (abstract safe; §3.3 conforms-not-complete; §4.6 cross-
materialization-inadmissibility-not-incapability; Table V3-1 distinct-materializations; §5 no
non-vacuity→certification; §6 hop2-control preserved [§6 UNCHANGED, verified]; §7 limitations not
weakened [strengthened: "two constructions, one model and task family"]; §9 no green-light;
Appendix A #5-blocked/C-untouched; Appendix B no certification overstatement; P-role positional-
only; no mechanism language) — ALL HOLD, each carried from the cleared delta and preserved in the
splice. The load-bearing §5 contribution claim ("gate shown binding and discriminating across two
constructions") remains scoped to NON-VACUITY (gate can fail on real constructions and
discriminate), never certification or positive composition — byte-identical to the cleared delta.
```

## 5. The items the TL asked me to rule on

```text
- ABSTRACT SAFETY — SAFE. Byte-identical to the cleared delta abstract; excerpt test passes;
  consistent with the integrated body (Interaction C). The INT4 field-framing opening line is the
  same one cleared in the delta review (describes what stress metrology IS, with the paper's whole
  point being the program has NOT done it); the OBS-1 optional one-clause hardening from the delta
  review remains optional and is not required.
- §3.3 / §4.6 — BOUNDED. Byte-consistent with the cleared delta; §4.6's cross-references to §4.2
  (PRECONDITION-FAIL sense) and §4.3 (position/rank route) resolve correctly in the integrated
  numbering (checked — they point at the right existing sections). §3.3's "conforms not certified-
  complete" boundary is intact.
- §5 / §7 / §9 — ALL BOUNDED. §5 keeps non-vacuity from becoming certification; §7's limitation is
  strengthened not weakened; §9 keeps the stress-phase leash and adds the not-a-green-light
  reinforcement.
- APPENDIX A CLAIM-LEDGER — SAFE (Interaction D). Validity/constructibility statements with NOT-
  claims attached; Claim B ≠ Paper B held.
- P-ROLE LEASH — SUFFICIENT. Byte-identical to the cleared delta §4.6: 352/352 reported strictly
  as positional/structural co-occurrence, four mechanism readings disclaimed, witness-triple named.
  The §7 Behavioral-only addition ("the P-role landing … generates a future target, not a
  mechanism") reinforces it. I checked for any OTHER P-role mention in the integrated body that
  might lack the leash: there is none — it appears in §3.3 (as the designed wrong-selection target,
  a construction-description), §4.6 (leashed), and §7 (leashed). Consistent.
```

## 6. One non-blocking item for CS (provenance lane, not claim-risk)

```text
The cover note and Appendix B addendum assert full sha256 digests for the V3 run artifacts
(decision.json 8676530a, covariate_log 480f70d1, admissibility_summary 3763f736, etc.) and state
CS recomputed them for the freeze/tag pass. This is the CS provenance lane. From the claim-risk
side the VALUES the manuscript cites (HOP1-STABLE-INADMISSIBLE, 576/576, P-role 352/352, the six
per-block hop1 counts and Wilson bounds) are the ones I independently verified from the run bytes
in the delta review (976b1b09…) — they are accurate. CS should confirm the ADDENDUM DIGESTS match
the locked files (the manuscript now asserts full hashes, not placeholders), exactly as the prior
Cell hashes were recomputed. Not a claim-risk blocker; the claim-bearing numbers are byte-verified.
```

## 7. Recommendation

```text
1. PASS on claim-risk. The integration is a clean splice: integrated = existing Paper 2 + the
   C5-cleared delta blocks, no other claim-bearing change, all four interactions (A–D) clean, the
   §9 stress-phase leash preserved and reinforced.
2. CS PROVENANCE REVIEW MAY PROCEED — the Manager gated it behind this clearance. CS should
   confirm the Appendix B addendum full digests against the locked files (the manuscript asserts
   full hashes now), and confirm the cover-note source attestations (delta ab52913c, ledger
   15f32e1a).
3. Result-time guard, standing: this is a DRAFT in papers/.../in-review, NOT a release (CS
   confirms the v1.0 tag is untouched). Before any release, the forbidden-claims checklist should
   be re-run against the final released text, and if TL synthesis changes any claim-bearing prose
   beyond CS's digit confirmations, the changed text returns here. The release step itself is a
   separate gate (Manager), not authorized by this review.
Requires CS verification: Appendix B addendum digests; cover-note source attestations.
Authorization implication: none — this clears the integrated PROSE for CS provenance review; it
authorizes no experiment, no compression, no release. The K=5 FAIL stays closed.
```

## 8. Boundaries checked

```text
- Identity verified from bytes (clone at 5b00ed5; digest exact match).
- Diff review performed against the existing Paper 2: integrated = existing + cleared delta blocks,
  no other claim-bearing change; §6/figures/title/other-§7-bullets confirmed unchanged.
- All four splice-point interactions (A–D) checked against the actual integrated sentences; the
  §9 stress-phase leash (Interaction B) verified preserved and reinforced, not eroded.
- The claim-bearing numbers (HOP1-STABLE-INADMISSIBLE, 576/576, 352/352, per-block hop1) were
  byte-verified in the delta review and are unchanged here; the Appendix B digest recompute is
  routed to CS as a provenance (not claim-risk) item.
- No experiment, redesign, compression, INT8/INT4, Claim C, Paper B, certification, capability, or
  mechanism claim authorized or endorsed. This clears integrated prose for CS provenance review
  only; release is a separate Manager gate. The K=5 FAIL stays closed.
```

---

**The one to carry up:** The revised integrated Paper 2 manuscript earns **PASS on claim-risk** (identity byte-verified, digest exact at HEAD `5b00ed5`). I ran the diff review I scoped: the integrated manuscript = the existing published Paper 2 + the C5-cleared V3 delta blocks, with NO other claim-bearing change — the diff's only removed hunks are the version line, old abstract, old §7 bullets, and old Appendix A paragraph, each replaced by its cleared delta counterpart, while §6, all four figures, the title, References, and every other §7 bullet are unchanged, so the five watchpoint sentences cleared in the delta byte-review are byte-preserved. All four splice-point interactions I flagged as the reason this object needed its own read are clean, and the highest-risk one resolves best: the existing §9 stress-phase leash ("only after hop2 is certified shortcut-free … not as seam evidence … remains gated … no stress rung run") is preserved INTACT, and the new V3 §9 paragraph sits immediately after it and REINFORCES the gate ("not a green light to stress hop2 or any other component; no stress rung has yet been run on either construction") — so the adjacency I worried about (six-materialization hop2 making stress look licensed) produces the opposite effect, gating hop2-stress more firmly, not less. The other three interactions are clean too: §9 shows the decouple-position-from-rank call REALIZED by V3 AND returning a negative result without over-closure ("not yet in hand … either"); the abstract is consistent with the integrated body (every abstract claim delivered, none exceeding it); and Appendix A reconciles with Claim B strengthened to two constructions, Claim #5 still blocked-on-precondition ("reinforces this block and does not resolve it"), Claim C untouched, and "Claim B" kept distinct from forbidden "Paper B." All twelve manuscript checks hold, the load-bearing §5 contribution claim stays scoped to gate NON-VACUITY (never certification or a positive composition result), the P-role is positional/structural co-occurrence at all three mentions (§3.3 construction-description, §4.6 and §7 both leashed), and no mechanism language appears. One non-blocking item routes to CS's provenance lane: the Appendix B addendum now asserts full sha256 digests for the V3 run artifacts (rather than placeholders), which CS should confirm against the locked files — but the claim-BEARING numbers the manuscript cites (HOP1-STABLE-INADMISSIBLE, 576/576, P-role 352/352, the six per-block hop1 counts and Wilson bounds) are the ones I independently verified from the run bytes in the delta review and are accurate. CS provenance review may now proceed; this is a draft in in-review with the v1.0 tag untouched, the forbidden-claims checklist should be re-run against any final released text, release is a separate Manager gate not authorized here, and the K=5 FAIL stays closed.

— Contributor 5
