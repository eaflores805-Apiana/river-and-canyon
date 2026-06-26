# C5 RETURN — First Compression Rung Authorization Packet v0.2 Claim-Risk

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead / Manager · **Cc:** Senior, CS, New Senior
**Date:** 2026-06-21
**Object requested:** `FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.2.md`
**Declared digest:** `ae47c3c2c76be9594d81eff212633984f449a3e4ea9844c5ff56682455f2ffad`
**Status:** review return. Authorizes nothing; this is the highest-stakes claim surface in the program's history, and it is reviewed as such.

---

## Verdict

```text
HOLD — ARTIFACT ACCESS. The packet is not in this seat's reach. The TL note routes the packet to
C5 "once filed," but at the HEAD I can reach it is not yet filed — this is the routing-order
situation again (filing instruction issued, propagation not yet visible to review).

Checked exhaustively this turn:
  - Fresh clone at HEAD 3b336c697db7e8f510a1cfaaf215ba6e7cc4746b.
  - Suggested path governance/2026-06-21_first-compression-rung-direction/FIRST-COMPRESSION-RUNG-
    AUTHORIZATION-PACKET-v0.2.md → ABSENT.
  - Scanned every .md in the repo for the declared digest ae47c3c2… → NO match under any name.
  - The direction directory currently holds only the Manager direction and the CS ack; the packet
    is not there.
The authorization packet has not been filed to a readable path, nor pasted.
```

The HOLD lifts the instant the packet is filed to a readable repo path (or pasted) WITH its
digest — and the declared `ae47c3c2…` lets me confirm identity immediately on filing. The six
review items are pre-loaded below as standing standards, grounded in the governance bytes that
ARE filed and that I read this turn (the Manager direction, the CS ack, and the already-run
2026-06-15 FP16-INT8 result). **One of the six (item 5, adoption) is the subtle risk that makes
this packet different from a fresh-run authorization, and I flag it hardest.**

## 0. Why this HOLD matters more than the usual access-HOLD (the bytes I CAN read)

```text
This packet proposes the program's FIRST crossing from pre-stress to a compression rung. Every
prior review in this program's history has held the line "no INT8/INT4 rung has been run." The
governance context, which I read from filed bytes this turn, sets the boundary the packet must
honor — and the boundary is tight:

(a) MANAGER DIRECTION (filed, read): the rung is opened ONLY as "instrument-validation-under-
    stress." The run, if authorized, "may answer ONLY: Can the fail-closed instrument produce a
    valid FP16-to-INT8 stress-retention readout on the selected qualified target?" and may NOT
    answer whether compression damages composition, whether the seam exists, whether Claim C is
    supported, whether V3 is fixed, or whether M5 is resolved. No INT4. This is the exact frame
    the packet's claim language must stay inside.

(b) CS ACK (filed, read): reads the direction CORRECTLY as narrowly lifting the "no INT8" block
    FOR PACKET-AUTHORING SCOPE ONLY — the actual INT8 run "remains separately gated on the full
    chain (Senior draft → C5 claim-risk → CS feasibility → TL synthesis → Manager by-name run
    authorization)." So this review (C5 claim-risk on the packet) is the second gate in that
    chain; my PASS, if it comes, clears packet CLAIM LANGUAGE only and authorizes NO run.

(c) THE ALREADY-RUN 2026-06-15 FP16-INT8 RESULT (filed, read — this is the crux of item 5). The
    directory experiments/2026-06-15_minimal-fp16-int8-twohop-l1 contains an FP16-INT8 run that
    ALREADY EXECUTED. I verified it HAS a PREREGISTRATION.md (it was pre-registered), and its
    disposition is: retention/compression verdict INCONCLUSIVE (the baseline gate failed; no valid
    composition to stress); construction verdict NEGATIVE for Two-Hop L1 @ 3B (terminal-attraction
    mechanism); and the INT8 observation is "byte-identical same-error preservation — INT8
    reproduced a gate-failing baseline exactly. PRESERVED ERROR, NOT PRESERVED CAPABILITY." This
    run is closed with that disposition.
```

## 1. The subtle risk that makes this packet different — item 5, flagged hardest

```text
The TL's item 5 ("adoption of the existing 2026-06-15 run clearly separated from fresh-run
authorization") is not a routine boundary check — it is THE claim-risk crux of this packet, and a
SUBTLER form of lock-after-look than a fresh run would present. The risk:

  A fresh-run authorization is a clean lock-before-look object: declare the metrics/thresholds/
  forbidden-interpretations, THEN run. The claim-risk surface is whether the pre-registration is
  honest. Adopting an ALREADY-RUN result as the "first compression rung" is different: the data
  already exist and their disposition is already known, so the risk is that the packet RE-READS a
  closed result beyond its locked disposition — turning "INT8 preserved a gate-FAILING baseline
  (inconclusive for retention)" into something that sounds like a positive first stress readout.

  This is admissible ONLY under tight conditions, and the packet must satisfy ALL of them:
    1. The 2026-06-15 run WAS pre-registered (verified: it has PREREGISTRATION.md) — so adoption
       is not retro-fitting a prereg onto an unplanned run. This condition is MET by the run; the
       packet must not claim more.
    2. The packet must carry that run's ACTUAL disposition forward unchanged: retention
       INCONCLUSIVE, construction NEGATIVE (terminal attraction), INT8 = preserved-error-not-
       preserved-capability. It may NOT re-interpret the byte-identical same-error preservation as
       "INT8 retains" or "hop2 survives" or any positive readout.
    3. Adoption and fresh-run authorization must be EXPLICITLY SEPARATED — the packet must not let
       "we already have an FP16-INT8 run" blur into "the first rung is therefore already passed."
       If the packet ADOPTS the 2026-06-15 result as the instrument-validation rung, the only
       claim-safe reading is "the instrument已 produced a valid readout on a gate-failing baseline,
       and the readout was "preserved error" — which validates the INSTRUMENT'S fail-closed
       behavior, NOT any capability retention." That is the instrument-validation framing the
       Manager authorized, and it is the ONLY thing that result can support.

  BYTE-CHECK on filing: does the packet adopt the 2026-06-15 run, propose a fresh run, or both?
  Whichever — is the adopted result's disposition carried forward UNCHANGED, and is adoption
  explicitly walled off from any "first rung passed" reading? The TL boundary "no adoption" in the
  closing boundaries list suggests the intended answer is that the packet must NOT adopt it as a
  pass — confirm the packet's language matches that boundary.
```

## 2. The six review items — standards pinned to the governance frame (adjudication deferred to packet bytes)

```text
ITEM 1 — "qualified"/"eligible" stays bounded to the narrow hop2-only FP16→INT8 readout.
  STANDARD: every use of "qualified"/"eligible"/"stress-eligible" in the packet must be scoped to
  "this specific target clears the FP16 baseline gate well enough to carry THIS hop2-only FP16→
  INT8 instrument-validation readout" — NOT "hop2 is qualified" in any general sense, NOT
  "composition is qualified." The Manager frame is a single qualified target for a single readout.
  BYTE-CHECK: no unscoped "qualified" that reads as a capability property.

ITEM 2 — packet avoids implying hop2 is certified shortcut-free.
  STANDARD: this is the paper's own §6/§9 leash, now load-bearing for a RUN. The paper states
  hop2's admission rests on FP16 accuracy + inapplicability of the §4.3 contamination, NOT a hop2-
  specific shortcut probe, and that "certifying hop2's own shortcut-freeness is a precondition for
  any future stress rung on it." The packet MUST carry that: hop2 is the target BECAUSE it clears
  the FP16 gate, but the packet must NOT assert hop2 is shortcut-free/certified. If the packet
  treats hop2 as a stress target WITHOUT either (a) including the hop2-specific shortcut/position
  probe the paper requires, or (b) explicitly scoping the rung as instrument-validation that does
  NOT presume hop2 shortcut-freeness — that is a claim-risk HOLD. BYTE-CHECK: no "hop2 is
  shortcut-free/certified"; the shortcut-freeness precondition is either satisfied or explicitly
  deferred-and-not-presumed.

ITEM 3 — packet avoids implying hop2 is robust under quantization.
  STANDARD: the paper states the FP16 control "does NOT establish that hop2 is robust under
  quantization" and any "retains under compression" reading "is unsupported by the current
  artifacts." The packet is the FIRST thing that could violate this by proposing the actual INT8
  run. It must frame the run as ASKING whether the instrument produces a valid readout, NOT as
  expecting/asserting hop2 robustness. And critically (item 6) the OUTCOME framing must not
  pre-judge: a "pass" means "the instrument produced a valid readout," not "hop2 is robust."
  BYTE-CHECK: no "hop2 robust under INT8" as premise or anticipated conclusion.

ITEM 4 — packet avoids Claim C / seam / composition implications.
  STANDARD: the Manager direction is explicit — NOT a seam test, NOT Claim C, NOT a composition
  claim. hop2 is a SINGLE-HOP retrieval; a FP16→INT8 readout on it says nothing about composition
  by construction. The packet must keep Claim C "untouched/blocked" and must not let "first
  compression rung" read as "first seam measurement." BYTE-CHECK: Claim C explicitly untouched;
  no composition/seam language; the single-hop nature of the target stated as what walls it off
  from composition.

ITEM 5 — adoption of the 2026-06-15 run clearly separated from fresh-run authorization.
  STANDARD: §1 above — the crux. Adoption admissible only if the run's prereg status (MET) and its
  unchanged disposition (retention INCONCLUSIVE, INT8 = preserved-error) are both honored, and
  adoption is explicitly walled from any "rung already passed" reading. The TL boundary list says
  "no adoption" — so the safest packet either proposes a FRESH run under fresh prereg, or cites
  the 2026-06-15 run ONLY as instrument-validation precedent (the instrument produced a valid
  readout on a gate-failing baseline) without adopting it as the authorized rung. BYTE-CHECK:
  adoption vs fresh is unambiguous; if adopted, disposition carried forward unchanged; "no
  adoption" boundary respected.

ITEM 6 — INT8 null-stress stated as instrument-validation only, not retention robustness.
  STANDARD: the 2026-06-15 INT8 result (byte-identical same-error preservation of a gate-failing
  baseline) is the "null-stress" reference. Its ONLY claim-safe reading is that the INSTRUMENT
  behaved correctly (it produced a valid readout and that readout was "preserved error") — which
  validates the fail-closed instrument, NOT capability retention. The packet must state this as
  instrument-validation, NEVER as "INT8 is robust" or "the model retains under INT8." This is the
  exact "no 'INT8 robust' from byte-identity" standing rule from the 2026-06-15 disposition.
  BYTE-CHECK: null-stress framed as instrument-validation; the preserved-error-not-preserved-
  capability distinction explicit.
```

## 3. The boundary the packet sits inside (for the record)

```text
Per the Manager direction, CS ack, and the TL boundary list, ALL of these remain CLOSED and the
packet must not cross any of them: no run begins (this is packet-authoring + claim-risk only); no
adoption as a pass; no INT4; no composition / seam / Claim C claim; no M5 distractor-attractiveness
experiment; no V3 composite-gate retry; no construction redesign; no certified baseline; no
capability claim; no mechanism claim. The Path A FP16 K=5 FAIL stays closed. My eventual PASS, if
the packet earns it, clears the packet's CLAIM LANGUAGE for the next gate (CS feasibility) and
authorizes NO run — run authorization is the Manager's by-name step at the end of the chain.
```

## 4. Recommendation

```text
1. File the packet to a readable path (or paste) WITH its digest (declared ae47c3c2… — I will
   confirm identity on sight). The HOLD lifts and I perform the claim-risk review against the six
   standards, with item 5 (adoption-vs-fresh) and item 2 (hop2 shortcut-freeness not presumed) as
   the two I will scrutinize hardest, since those are where a first-rung packet most easily
   overclaims.
2. The single most important question for the bytes: does the packet keep the rung as
   instrument-validation answering ONLY "can the instrument produce a valid readout," with the
   2026-06-15 INT8 result's "preserved error, not preserved capability" disposition carried
   forward unchanged — or does any language drift toward "hop2 robust / composes / first seam
   readout"? The former is claim-safe; the latter is a HOLD.
3. This review does not advance to CS feasibility until claim-risk clears the packet bytes. For
   the program's first stress-rung object, "filed ≠ cleared" is the most expensive it has ever
   been — a claim-language drift here is what would let "pre-stress" silently become "seam-
   started."
Requires: the packet + digest. Authorization implication: none — claim-risk is gate 2 of 5; run
authorization is the Manager's by-name step.
```

## 5. Boundaries checked

```text
- No verdict on unread bytes: packet confirmed absent from reach (clone at 3b336c69; suggested
  path empty; declared digest matches no file under any name; direction dir holds only direction +
  ack) and HELD.
- The six review standards pinned to the FILED governance bytes I read this turn (Manager
  direction = instrument-validation-only frame; CS ack = run still fully gated; 2026-06-15 run =
  pre-registered, disposition retention-INCONCLUSIVE / INT8-preserved-error).
- Item 5 (adoption) flagged as the subtle lock-after-look risk that distinguishes this from a
  fresh-run packet, with the admissibility conditions named.
- No run, adoption, INT4, composition/seam/Claim C claim, M5 experiment, V3 retry, redesign,
  certification, capability, or mechanism claim authorized or endorsed. This is claim-risk gate 2
  of 5; run authorization is the Manager's by-name step. The K=5 FAIL stays closed.
```

---

**The one to carry up:** I cannot verdict the first-compression-rung authorization packet because it is not in my reach — cloned at HEAD `3b336c69`, the suggested governance path is empty, the declared digest `ae47c3c2…` matches no file under any name, and the direction directory currently holds only the Manager direction and the CS ack; the packet has not propagated. The access HOLD lifts the instant it is filed or pasted with its digest, which I can confirm on sight. This is the program's FIRST crossing from pre-stress to a compression rung — the highest-stakes claim surface in its history — so I read the filed governance context to ground the six rulings: the Manager direction opens the rung ONLY as "instrument-validation-under-stress" answering ONLY "can the fail-closed instrument produce a valid FP16→INT8 readout on the qualified target," explicitly NOT seam/Claim C/composition/V3-fixed/M5-resolved and no INT4; the CS ack correctly reads this as narrowly lifting the "no INT8" block for PACKET-AUTHORING ONLY, with the actual run still fully gated through the five-step chain (my claim-risk review is gate 2 of 5, and clears packet CLAIM LANGUAGE only — it authorizes no run). The subtle risk that makes this packet different from a fresh-run authorization, and which I flag hardest, is the TL's item 5: the "2026-06-15 minimal FP16-INT8" run the packet may ADOPT already executed, and I verified from its bytes that it WAS pre-registered (has PREREGISTRATION.md) and is closed with the disposition retention/compression INCONCLUSIVE (baseline gate failed, no valid composition to stress), construction NEGATIVE (terminal-attraction mechanism), and INT8 = "byte-identical same-error preservation — preserved error, NOT preserved capability." Adopting an already-run result as the "first rung" is a subtler lock-after-look than a fresh run, admissible ONLY if that prereg status and that exact disposition are carried forward unchanged and adoption is explicitly walled from any "first rung passed" reading — and the TL's own boundary list says "no adoption," so the claim-safe packet either proposes a fresh run under fresh prereg or cites the 2026-06-15 result only as instrument-validation precedent (the instrument produced a valid readout on a gate-failing baseline, which validates the INSTRUMENT, not capability retention) without adopting it as the authorized rung. The other five standards: "qualified/eligible" must stay bounded to the narrow hop2-only FP16→INT8 readout (not hop2-as-capability); the packet must not imply hop2 is certified shortcut-free (the paper's §9 makes a hop2-specific shortcut probe a precondition for any stress rung on it — so the packet must either include that probe or explicitly not presume shortcut-freeness); must not imply hop2 is robust under quantization (the run ASKS whether the instrument produces a valid readout, and a "pass" means exactly that, not "hop2 robust"); must keep Claim C/seam/composition untouched (hop2 is single-hop, which by construction says nothing about composition); and must state the INT8 null-stress as instrument-validation only, never "INT8 robust" from byte-identity. File the packet with its digest and the review proceeds, with item 5 (adoption-vs-fresh) and item 2 (hop2 shortcut-freeness not presumed) scrutinized hardest; CS feasibility waits on this clearance; no run begins from anything here; and the K=5 FAIL stays closed.

— Contributor 5
