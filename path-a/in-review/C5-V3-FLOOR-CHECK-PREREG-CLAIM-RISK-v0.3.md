# C5 RETURN — V3 Floor-Check Preregistration v0.3 Claim-Risk (re-review)

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead · **Cc:** CS, Senior, New Senior, Manager
**Date:** 2026-06-18
**Object:** `path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.3.md`
**Supersedes:** the v0.1 access-HOLD return (`acb11d60…`, retained).
**Status:** re-review return. Authorizes nothing; locks nothing.

---

## 0. Identity — verified from bytes by this seat

```text
Clone at HEAD 2f0f167e861af5e61469cfcc196cfe2e8fdee7d4.
sha256(PREREGISTRATION-V3-FLOOR-CHECK-v0.3.md)
  = df82b34c4f96e085ea51b8e6e1a735849a39b108b321f79e30b9f20cffa19d5b
  = declared digest, EXACT MATCH.
Access HOLD from v0.1: LIFTED. This is a verdict on the read bytes.
```

## 1. Verdict

```text
PASS — claim boundaries safe. All six prior claim-risk rulings are resolved in the bytes,
and the two quantitative claims the lock turns on (the Wilson floor minimum-count and the
direct-query/invalidated integer boundaries) were independently recomputed by this seat and
reproduce exactly. No claim-risk edits required. One verification dependency carried, not a
claim-risk edit (the instrument re-pin, §2 below), routed to CS.
```

This is the strongest pre-lock object in the Path A lineage. Every ruling landed at point of use, the strictness is in the protective direction throughout, and the validity/admissibility-not-certification line is held in the prereg's own decision rule and forbidden-interpretations block.

## 2. Resolution of the six prior rulings (each checked in bytes, not credited from the changelog)

```text
RULING 1 — R6 ITEM-LEVEL / SET-LEVEL SPLIT — RESOLVED (§8, CS edit E3).
  §8 states the single rule, two levels: item-level invalidator → EXCLUDE that item from the
  validated numerator + LOG (the five named non-circular invalidators); set-level → invalidated
  count ≥10/96 → CONSTRUCT-FAIL. This is exactly the split I required (exclude-an-item ≠
  fail-the-construct), and zero-tolerance is gone. BONUS catch I did not ask for but is correct:
  §8 explicitly states hop2-below-floor is NOT an item-level invalidator — it is the primary
  set-level outcome — closing a circularity (the primary metric invalidating its own items) I
  had not flagged. That is the drafter applying the discipline beyond the ruling. Fully resolved.

RULING 2 — DIRECT-QUERY EXACT COUNT BOUNDARY — RESOLVED (§6/E2).
  "direct-query C* count ≤ 19/96 PASSES; ≥ 20/96 FAILS … POINT-COUNT CEILING, NOT a Wilson
  interval rule." Exact integer boundary, one convention, explicitly not a CI rule (removing the
  ambiguity I flagged). I recomputed: 19/96 = 0.1979 ≤ 0.20, 20/96 = 0.2083 > 0.20 — unambiguous.
  Resolved.

RULING 3 — hop2 WILSON STRICTNESS BOUNDED AS COMPONENT-ADMISSIBILITY ONLY — RESOLVED (§7).
  §7 "WHAT CLEARING MEANS (and does NOT)": a COMPONENT-ADMISSIBILITY result, NOT capability,
  NOT certification, NOT composition; required interpretation quoted verbatim as "second-hop
  retrieval is reliable enough under V3 competition to make a later composite test
  interpretable." This is the exact bound I required, and it is the over-read I asked be guarded
  hardest — guarded correctly. The strictness (lower Wilson > 0.75) I recomputed: 81/96 clears
  (lower 0.7581), 80/96 does not (0.7463) — the §7 min-count is byte-correct. Resolved.

RULING 4 — ONE-RUN SUBSTRATE-INFEASIBILITY AS EVIDENCE-TOWARD, NOT FINAL — RESOLVED (§10, §11).
  §10 splits ONE-RUN EVIDENCE TOWARD (single run, "NOT, by itself, final proof") from FINAL
  CLASSIFICATION (requires REPEATED admissible failures), and states verbatim that a below-floor
  result is "NEVER a license to loosen the 0.75 floor, lower D, or tune until the number
  cooperates." §11 repeats "evidence TOWARD … not a final classification." This is the §8.5 /
  §17 repeated-failure language inherited, not weakly paraphrased — my verbatim-inheritance
  concern is met. Resolved.

RULING 5 — CLEAN CONSTRUCT CONTINGENT ON PROMPT-REALIZATION CONFORMANCE — RESOLVED (§4, §9).
  §9 makes prompt-realization conformance gate (vi) of the only "gate clears" outcome, and states
  the CLEAN-CONSTRUCT BOUNDARY: "clean at the SPEC level only until prompt-realization conformance
  passes; a spec-clean, prompt-unchecked construct is NOT eligible for a substrate conclusion."
  This is exactly the spec-execution-gap guard I required — the clean-construct claim is tied to
  realized bytes, not the spec. §4 adds the deterministic length-matching metric (character count,
  same template class, predeclared max delta; tokens diagnostic only) that makes the conformance
  check executable. Resolved.

RULING 6 — NO CERTIFICATION / CAPABILITY / MECHANISM / COMPOSITION OVERCLAIM — RESOLVED (§11).
  §11 forbidden-interpretations carries all four: hop2-clears is not certification and not
  composition; no mechanism claims (traversal/grab/anchor "not decidable here"); survival-is-not-
  correctness (C* counts only via the bridge with controls clearing); "not ruled out" is not
  "established." The full perimeter. Resolved.
```

## 3. Independent arithmetic verification (the lock-bearing numbers)

```text
Recomputed, not credited from "SE-verified":
  hop2/hop1 floor (lower Wilson 95% > 0.75 at N=96):
    81/96 → lower 0.7581 CLEARS;  80/96 → lower 0.7463 does NOT.  ✓ matches §7/§E4.
  direct-query point ceiling: 19/96 = 0.1979 (pass), 20/96 = 0.2083 (fail). ✓ exact integer.
  invalidated-fraction ceiling: 9/96 tolerated, 10/96 construct-fail. ✓ exact integer.
The post-exclusion handling (§E4: analyzer recomputes the exact Wilson minimum on the reduced
denominator; 81/96 is the full-N reference, not a hardcoded count) is the correct treatment —
it does not freeze a count that would be wrong if items are excluded.
```

## 4. The one carried dependency (verification, not a claim-risk edit — route to CS)

```text
INSTRUMENT RE-PIN — appears RESOLVED in the bytes; CS to confirm. My v0.1 return flagged that
the SE's V3 byte-audit was a HOLD because the of-record prereg pinned a stale inspector digest
(be50c08c) after the K-sweep patch drifted it. v0.3 §3 now pins inspector.py = cb4b0b60 and
constants.py = 1d761c3d, both annotated "re-pinned (matches v0.4)." This is the corrected
digest from the SE audit (cb4b0b60 was the SE-recomputed value), so the stale-binding problem
is addressed in the bytes. CS feasibility should CONFIRM these re-pinned digests against the
actual instrument bytes at HEAD (CS owns hash verification), and confirm the v0.4 binding
(c61a3256…, "placeholder corrective 9ea16d1") is itself resolved — §2 says the v0.4 byte-binding
HOLD is "NOT reopened," which is a routing statement, so CS should confirm it was actually closed
upstream, not merely deferred. This is a CS verification item; from the claim-risk side the
prereg correctly pins corrected digests rather than the stale ones, which is what I required.
```

## 5. What this seat is NOT ruling on (CS's lane)

```text
The five CS feasibility watchpoints (analyzer lockability + path existence, length-matching
executability, analyzer digest, exact-once computability, no-hidden-execution) are CS's. One
claim-risk touch-point, already noted under Ruling 5: the §4 length-matching metric is BOTH a
feasibility item AND the spec-execution-gap guard — CS's conformance check is part of what makes
the clean-construct claim safe, so the two reviews meet there. The analyzer (§E1) being named but
not-yet-produced (digest "LOCKED AT APPROVAL") is the correct lock-before-look posture for a
scorer (its bytes fixed before the run so the rule can't be tuned to data); whether the analyzer
path exists and is lockable is CS's PASS/HOLD call, not mine.
```

## 6. Recommendation

```text
1. PASS on claim-risk. No claim-risk edits required; all six rulings resolved in bytes, lock-
   bearing arithmetic independently confirmed.
2. The instrument re-pin (§4) and the analyzer lockability (§5) are CS feasibility items; this
   PASS is on claim framing and boundaries, and is independent of CS's feasibility verdict — both
   must clear before TL approval and Manager authorization.
3. At lock: the analyzer digest (§E1), the SE-proposed LOCKED-AT-APPROVAL values (hop1/hop2 floor
   0.75, prompt max-delta, the §6 ceilings), and the §9 decision rule are fixed before the run and
   computed once. Confirm none drift between approval and run — the same byte-discipline that
   caught the inspector stale-pin applies to these at-approval locks.
4. No further C5 round required on the claim-risk axis — stop-rule declared. If the prereg changes
   materially before lock (not just CS's feasibility edits), it returns here.
Requires CS verification: the re-pinned instrument digests, the v0.4 binding closure, and the
five feasibility watchpoints. Authorization implication: none — no lock, no materialization, no run.
```

## 7. Boundaries checked

```text
- Identity verified from bytes (clone at 2f0f167; digest exact match).
- All six prior rulings checked against the actual section text, not the changelog.
- The two lock-bearing quantitative claims recomputed independently, not credited from "SE-verified."
- No lock authorized — this PASS is on claim framing; lock still requires CS feasibility + TL + Manager.
- No items, prompts, materialization, run, compression, certification, Claim C, or Paper B authorized.
- hop2 floor treated as component-admissibility throughout; substrate-infeasibility held to repeated-
  failure; mechanism/composition/capability forbidden; the K=5 FAIL stays closed.
```

---

**The one to carry up:** v0.3 is identity-verified from bytes (clone at `2f0f167`, digest exact) and earns **PASS on claim-risk** — all six prior rulings are resolved in the actual section text, not merely credited: the R6 rule now splits item-level (exclude that item from the numerator + log, the five non-circular invalidators) from set-level (≥10/96 → construct-fail), with zero-tolerance gone and a bonus closure I had not flagged (hop2-below-floor explicitly is NOT an item-level invalidator, so the primary metric cannot invalidate its own items); the direct-query ceiling is an exact integer point-count (≤19/96 pass, ≥20 fail, explicitly not a Wilson rule); the hop2 Wilson strictness is bounded verbatim as a component-ADMISSIBILITY result ("reliable enough to make a later composite test interpretable"), never certification or composition; one-run substrate-infeasibility is split from final classification with the "never a license to loosen the floor" language inherited verbatim; the clean-construct claim is gated on prompt-realization conformance (the spec-execution gap) and tied to realized bytes; and the §11 forbidden-interpretations block carries the full no-certification/capability/mechanism/composition perimeter. I independently recomputed the lock-bearing numbers rather than crediting the "SE-verified" annotation: 81/96 clears the lower-Wilson>0.75 floor (0.7581) and 80/96 does not (0.7463), and the integer ceilings are unambiguous — all confirmed. One carried dependency, a CS verification item not a claim-risk edit: §3 now re-pins the instrument digests (inspector cb4b0b60, constants 1d761c3d) to the corrected values from the SE byte-audit, resolving the stale-pin I flagged in v0.1 — CS should confirm these against the instrument bytes and confirm the v0.4 binding was actually closed upstream rather than only deferred. This PASS is on claim framing and is independent of CS's feasibility verdict; both must clear before TL approval and Manager by-name authorization, and nothing here authorizes a lock or a run. The K=5 FAIL stays closed.

— Contributor 5
