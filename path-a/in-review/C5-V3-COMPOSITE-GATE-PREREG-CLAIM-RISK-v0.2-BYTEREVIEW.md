# C5 RETURN — V3 Composite Gate Preregistration v0.2 Claim-Risk (byte review)

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead · **Cc:** CS, Senior, New Senior, Manager
**Date:** 2026-06-18
**Object:** `path-a/in-review/PREREGISTRATION-V3-COMPOSITE-GATE-v0.2.md`
**Supersedes:** the access-HOLD return (`7df2689c…`, retained).
**Status:** byte review return. Authorizes nothing; locks nothing.

---

## 0. Identity — verified from bytes by this seat

```text
Clone at HEAD 975f696d577859da37c598974139c7df03907009.
sha256(PREREGISTRATION-V3-COMPOSITE-GATE-v0.2.md)
  = df26dc65ac3dd76bb09fa84c4688b8835f49282e2a8f77ea4b94991308e57275
  = declared digest, EXACT MATCH.
Access HOLD: LIFTED. This is a verdict on the read bytes.
```

## 1. Verdict

```text
PASS — claim boundaries safe. All eight standing rulings are resolved in the bytes, the three
I flagged for hardest byte-check (Ruling 6 threshold distinctness, Ruling 5 seed-range, the
success-language guard) hold, and the two lock-bearing quantitative claims (the seen-composite
lower bound and the 0.45 derivation) were independently recomputed and reproduce exactly. One
CARRIED DEPENDENCY, not a claim-risk edit (the generator start-index for 097..192), routed to
CS — explicitly acknowledged in the prereg as a feasibility item. No claim-risk edits required.
```

## 2. Resolution of the eight standing rulings (each checked in the section text, not the changelog)

```text
RULING 1 (title) — RESOLVED. Title is "V3 COMPOSITE GATE"; the framing block states
  "certification appears below only as a bounded conditional concept, never as a result this
  run delivers on its own." I checked the rename is COMPLETE: every internal use of
  "certif*" is either "certification-as-concept (bounded)" or "FINAL certification (separate
  decision)" — no unbounded "certification" survives in the body. Full rename, not half.

RULING 2 (success language) — RESOLVED, and checked at EVERY success statement (the re-entry
  risk I flagged). §3, §7, §10 all use "behavior consistent with two-hop composition under
  foreclose-all controls"; the carry-up uses it; no "the model composes" anywhere as an
  asserted outcome (it appears only in §10's forbidden list). The bounded form is consistent
  across all success-outcome statements, not just once.

RULING 3 (correct-chain wording) — RESOLVED. §3 metric: "items whose composite context RETURNS
  THE CORRECT-CHAIN TARGET C* UNDER CONTROLS," with the explicit gloss "We observe the output
  token and the cleared controls; we do NOT observe the model's internal path." §10 repeats
  it. No residual "via/through/traverses the correct chain" — the output-not-path discipline
  is held.

RULING 4 (seen 80/96 barred) — RESOLVED. §5 bars the floor-check composite from gate evidence
  ("INFORMATIONAL ONLY and ALREADY SEEN … BARRED"); §10 repeats it. Correct.

RULING 5 (fresh disjoint seeds) — RESOLVED IN THE PREREG, CONTINGENT ON CS (as flagged). §4
  declares floor-check 001..096 (byte-confirmed from construction_ids), composite-gate 097..192,
  with the disjointness rule explicit and the ≤999 token-width constraint carried (so MAX_DELTA=8
  stays valid). The prereg DECLARES the exact range as I required. The CONTINGENCY is stated
  in the prereg itself ("generating indices 097..192 may require a generator start-index /
  seed-offset parameter; CS confirms or adds it") — so the prereg does not over-claim mechanical
  realizability; it declares the range and routes the realization to CS. This is the correct
  split: claim-risk needs the range declared (done); CS needs it realizable (open feasibility
  item). My Ruling-5 clearance stands ON THE CLAIM SIDE; the run cannot proceed until CS confirms
  the generator produces 097..192 as byte-distinct items. Not a claim-risk edit; a precondition.

RULING 6 (two distinct thresholds) — RESOLVED, and this is the one the TL fix-list did not
  visibly confirm, so I checked it hardest. §7 states TWO GATES, BOTH LOWER-WILSON, REPORTED
  SEPARATELY: primary reliability > 0.75, necessary not-shortcut floor > 0.45. All four sub-checks
  pass: (a) both present; (b) "reported separately," gate conditions (a) and (b) are distinct
  lines, never averaged/collapsed; (c) 0.45 is explicitly "NOT free: INHERITED as F + margin =
  0.20 + 0.25" — I recomputed: F = max(1/5,1/10,1/5) = 0.20, +0.25 = 0.45, confirmed, the OI-3
  free-number failure does NOT reappear; (d) §7 states clearing 0.75 does not exempt 0.45 — both
  are required gate conditions, and §8 explicitly handles the "clears 0.45 but not 0.75" case
  ("not explained by foreclosed shortcuts, but not reliably composing"). Fully resolved.

RULING 7 (this-run vs final) — RESOLVED. §7 "THIS-RUN vs FINAL (precommitted boundary)":
  GATE-CLEARED-THIS-RUN "is the MOST this single fresh run can yield … MUST NOT silently become
  FINAL certification"; final requires a separate Manager/standard decision and SE recommends ≥1
  confirmation, explicitly mirroring the substrate-infeasibility-requires-repeated-failures
  asymmetry. The symmetric framing (strong claims in BOTH directions cost >1 run) is exactly the
  discipline I required. Resolved.

RULING 8 (forbidden interpretations) — RESOLVED and STRONGER than the floor check's, as required.
  §10 carries all of: not "the model composes," not general capability, not mechanism, not seam
  evidence, not compression readiness, not Claim C, not Paper B, not final-from-one-run. AND the
  two highest-pull over-reads I named are explicitly pre-blocked: "a cleared composite gate does
  NOT itself authorize compression or stress rungs" (the seam/compression leak) and the scope is
  pinned to "on V3, at K=5, with Qwen2.5-3B-Instruct (FP16, greedy) — and nothing beyond." The
  "no seam evidence" line is present explicitly. Resolved.
```

## 3. Independent arithmetic verification (the lock-bearing numbers)

```text
Recomputed, not credited:
  Seen-composite transparency (§7): 80/96 → Wilson lower 0.7463, JUST BELOW the 0.75 gate. ✓
    This confirms the §7 "THRESHOLD TRANSPARENCY" claim is HONEST: the threshold is set on
    principle (the component reliability standard), the seen lower bound sits below it, so the
    fresh run is GENUINELY UNCERTAIN — the gate is not rigged to pass. This is itself a
    claim-risk virtue: a gate whose threshold sits just above the only prior data point, openly
    acknowledged, is not a gate reverse-engineered to clear.
  0.45 = F + margin = 0.20 + 0.25. ✓ (derived, not free.)
  Both gates lower-Wilson at N=96: >0.75 needs 81/96; >0.45 needs 53/96. ✓ consistent treatment.
```

## 4. The carried dependency (CS feasibility, not a claim-risk edit)

```text
SEED-RANGE REALIZABILITY (Ruling 5 contingency). The prereg declares 097..192 and itself flags
that the generator may need a start-index parameter (CS feasibility item). The TL notice confirms
"mechanical realization requires a tooling-build step for start-index support or equivalent
wrapper." So the path is: claim-risk PASS now (range declared, disjointness provable, ≤999
constraint honored); CS confirms/adds the generator start-index at the tooling step; the run
cannot proceed until 097..192 is mechanically realized as byte-distinct items. From the
claim-risk side this is fully handled — the prereg does not pretend the realization is done; it
declares the requirement and routes it. I flag only that the "fresh disjoint" CLAIM becomes TRUE
only when CS's realization confirms byte-distinct items at 097..192; until then it is a sound
declaration awaiting its bytes. Not a HOLD; a sequencing precondition the prereg already states.
```

## 5. What this seat is NOT ruling on (CS's lane)

```text
The CS feasibility items (generator start-index / 097..192 realizability, the two new tooling
artifacts' lockability, reused-tooling-unchanged confirmation, byte-distinctness of fresh items)
are CS's PASS/HOLD. The new analyzer and error-logger are named with intent + deterministic +
sha256-LOCKED-AT-APPROVAL — the correct lock-before-look posture for a scorer (bytes fixed before
the run so the rule cannot be tuned to data); whether they are buildable/lockable is CS's call.
```

## 6. Recommendation

```text
1. PASS on claim-risk. No claim-risk edits required; all eight rulings resolved in bytes, the two
   lock-bearing numbers independently confirmed, the success-language guard held at every
   success statement.
2. The seed-range realizability (§4) and the two new tools' lockability are CS feasibility items;
   this PASS is on claim framing and is independent of CS's feasibility verdict — both must clear,
   plus the separate TL/Manager tooling-build action, before TL approval and Manager run
   authorization.
3. At lock: the two gate thresholds (0.75 / 0.45), the §6 preconditions, the §7 rule, the
   this-run/final boundary, and the analyzer + error-logger digests are fixed before the fresh
   run and computed once. Confirm none drift between approval and run.
4. No further C5 round required on the claim-risk axis — stop-rule declared. If the prereg changes
   materially before lock (beyond CS feasibility edits), it returns here.
5. Standing reminder for the run gate: the success-language guard is the one to hold at RESULT
   time too — when the fresh run returns, a clean PASS must be reported as GATE-CLEARED-THIS-RUN /
   behavior-consistent-with-composition-under-controls, never upgraded in the write-up. The
   prereg is clean; the temptation arrives with the result.
Requires CS verification: seed-range realizability, the two new tools, reused-tooling confirmation.
Authorization implication: none — no lock, no materialization, no tooling build, no run.
```

## 7. Boundaries checked

```text
- Identity verified from bytes (clone at 975f696; digest exact match).
- All eight rulings checked against the actual section text, not the changelog.
- The two lock-bearing quantitative claims (seen-composite lower bound; 0.45 derivation)
  recomputed independently, not credited from the prereg's annotations.
- No lock authorized — this PASS is on claim framing; lock still requires CS feasibility + the
  tooling-build action + TL + Manager.
- No run, materialization, prompt generation, tooling creation, compression, INT8/INT4,
  certification-of-record, Claim C, or Paper B authorized.
- Gate/certification treated as a bounded validity outcome, never capability; single-run bounded
  as gate-cleared-this-run; the seam/compression leak explicitly pre-blocked in §10; "via the
  correct chain" replaced by the output-token form; the K=5 FAIL stays closed.
```

---

**The one to carry up:** v0.2 is identity-verified from bytes (clone at `975f696`, digest exact) and earns **PASS on claim-risk** — all eight standing rulings are resolved in the actual section text, including the three I flagged for the hardest byte-check. The title is fully retitled "V3 Composite Gate" with "certification" surviving only as a bounded conditional (complete rename, not half); success language is "behavior consistent with two-hop composition under foreclose-all controls" at every success statement, never "the model composes"; the metric counts items that "return the correct-chain target C* under controls" with the internal path explicitly unobserved; the seen 80/96 floor-check composite is barred from gate evidence; the fresh seeds 097..192 are declared disjoint from the floor-check 001..096 with the ≤999 token-width constraint carried (MAX_DELTA=8 preserved); the two thresholds are distinct, separately-reported lower-Wilson gates (reliability >0.75, not-shortcut floor >0.45) with 0.45 confirmed-by-my-recompute as the derived F+margin (0.20+0.25), not a free number — this was the one ruling the TL fix-list did not visibly confirm and it is fully resolved; GATE-CLEARED-THIS-RUN is precommitted as the most one run can yield with final certification a separate decision requiring ≥1 confirmation (symmetric with the substrate-infeasibility repeated-failure asymmetry); and the forbidden block is stronger than the floor check's, explicitly pre-blocking the two highest-pull over-reads (a cleared gate does NOT authorize compression or stress rungs; scope pinned to V3/K=5/Qwen2.5-3B-FP16-greedy and nothing beyond). I independently recomputed the lock-bearing numbers: the seen composite's 0.7463 lower bound sits just below the 0.75 gate, which confirms the prereg's own transparency claim that the fresh run is genuinely uncertain — the gate is set on principle, not reverse-engineered to pass, itself a claim-risk virtue. One carried dependency, a CS feasibility item not a claim-risk edit and already flagged in the prereg: the generator needs start-index support to realize 097..192, so the "fresh disjoint" claim becomes TRUE only when CS confirms byte-distinct items at those indices — a sound declaration awaiting its bytes, routed correctly. This PASS is on claim framing and independent of CS's feasibility verdict; both, plus the separate tooling-build action, must clear before TL approval and Manager by-name run authorization. The standing guard for result-time: a clean PASS must be reported as gate-cleared-this-run, never upgraded — the prereg is clean, the temptation arrives with the result. The K=5 FAIL stays closed.

— Contributor 5
