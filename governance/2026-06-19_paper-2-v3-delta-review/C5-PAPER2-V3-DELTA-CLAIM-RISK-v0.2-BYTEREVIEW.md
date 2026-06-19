# C5 RETURN — Paper 2 V3 Delta Draft Claim-Risk (sentence-level byte review)

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead / Manager · **Cc:** Senior, CS, New Senior
**Date:** 2026-06-19
**Object:** `path-a/in-review/PAPER-2-V3-DELTA-DRAFT-v0.1.md`
**Supersedes:** the access-HOLD return (`405ebd96…`, retained).
**Status:** sentence-level review return. Authorizes nothing.

---

## 0. Identity + the precondition I flagged — both verified from bytes

```text
Clone at HEAD fed7de05bc41f0b8c2dc07bcd1f8f0f26df42c2f. Full packet now readable:
the delta draft, the SE verification return, the finding report, and the run directory.

THE PRECONDITION FROM MY ACCESS-HOLD IS RESOLVED — and I verified it, not credited it:
  experiments/2026-06-19_hop1-stability-run/decision.json final_branch = HOP1-STABLE-INADMISSIBLE.
  All SIX fresh blocks fail the hop1 floor (recomputed Wilson lowers, EXACT match to the run):
    F1 50/96 →0.4220  F2 23/96 →0.1653  F3 35/96 →0.2752
    F4 39/96 →0.3135  F5 54/96 →0.4628  F6 23/96 →0.1653   (all < 0.75)
  All six hop2 controls clear (96/96, lower 0.9615). Admissibility 576/576 PASS.
  P-role: covariate_log summary n_hop1_wrong = 352, primary_P_role_among_wrong = 352, rate 1.0.
So the delta is NOT asserting a result that does not exist — the largest exposure from my
access-HOLD is closed. The run ran, was SE-verified, and I reproduced its branch and its
P-role count from the bytes. The delta may now be reviewed as prose.
```

## 1. Verdict

```text
PASS — claim boundaries hold. This is the most disciplined claim-bearing draft the program has
produced. All four watchpoint phrases are bounded correctly at the sentence level, all ten TL
checks hold in the prose, the run behind it is byte-verified, and the P-role universal (352/352)
is accurate and correctly leashed. No claim-risk edits required. Two NON-blocking observations
for the freeze/tag pass (both already flagged in the draft itself), and one phrase I examined
hardest and am clearing with a note rather than an edit.
```

## 2. The four watchpoint phrases — each adjudicated at the sentence level

```text
WP1 "the hop1 shortfall is not reducible to the position/rank route" — CLEARS, bounded.
  §4.6 reads: "The hop1 shortfall here is not reducible to the §4.3 position/rank route: V3 was
  built to foreclose that route, and the shortfall persists under it across fresh draws." This
  meets my pre-loaded standard exactly: it reads as not-EXPLAINED-BY-that-named-route (the route
  was foreclosed by construction and the shortfall remains), NOT as "the cause is isolated" or
  "all routes are impossible." The sentence scopes to the one named, foreclosed route. The
  abstract's version ("indicates the shortfall is not reducible to that route") uses "indicates,"
  appropriately tentative. CLEARS.

WP2 "stable across draws" — CLEARS, bounded, and now backed by a verified run.
  The abstract reads "the shortfall is stable across draws rather than a single-draw artifact,"
  and §4.6 states it as "did not clear its admissibility floor in any block" across six fresh
  disjoint materializations. This meets the standard: "stable" = the cross-materialization
  VERDICT was unanimous (all six fail), a property of the construction's materializations, NOT
  "the model is stable." And the precondition I attached — the run must EXIST — is satisfied
  (§0). The draft never writes "the model is stable/unstable"; §10's checklist explicitly bars
  "the model is unstable." CLEARS.

WP3 "foreclose-all redesign" / "foreclose-all V3" — CLEARS, bounded.
  Used as the NAME of the design standard throughout (§3.3 title, abstract). The completeness
  guard is explicit and verbatim where it must be: §3.3 says "V3 conforms to the foreclose-all
  standard but is a committed design choice, not a construction proven to foreclose every
  conceivable route," and §10 checklist repeats "foreclose-all V3 = committed choice that
  conforms, NOT certified-complete." This is watchpoint 9 satisfied at the sentence level: the
  label is a design-standard name, never cashed out as "all routes foreclosed." CLEARS.

WP4 "gate is shown binding and discriminating across two independent constructions" — CLEARS,
  and this is the load-bearing contribution claim, so I examined it hardest. It appears in the
  abstract, §4.6, and §5. In every instance it is scoped to the gate's NON-VACUITY: the abstract
  frames the whole contribution as supplying "the demonstration [that the gate is binding rather
  than merely conservative]," and §4.6/§5 cash "binding and discriminating" as "single-hop clears
  the gate while the multi-hop/first-hop precondition does not, so the gate discriminates rather
  than rejecting everything" — i.e. the gate is shown to be able to FAIL on real constructions
  AND to distinguish admissible from inadmissible, across two of them. It does NOT imply (a)
  general validation (the abstract explicitly disclaims generality — "we do not claim this holds
  across all tasks, scales, or models"), (b) a certified baseline (the composite gate "was not
  readable," nothing passed), or (c) a positive composition result (composite "unanswered,
  neither supported nor refuted"). This is Paper 2's actual thesis — the gate catches real
  failures — extended to a second construction. CLEARS.
```

## 3. The ten TL primary checks — each confirmed in the prose

```text
1. CONSTRUCTIBILITY/MEASUREMENT-VALIDITY FRAMING — holds. The contribution is "a worked
   constructibility map across two constructions, illustrating why the gate must exist." Framed
   as instrument/construction, not model.
2. PRE-STRESS — holds, stated repeatedly ("No compression rungs were run"; "the program remains
   PRE-STRESS"; §7 "No stress rung has yet been run on either construction").
3. NO COMPRESSION/INT8/INT4/CLAIM-C/SEAM/PAPER-B — holds. The seam-leak I flagged as the highest
   paper risk is explicitly closed: §8 "makes no statement on Claim C (the seam), which remains
   blocked," §7 "not a green light to stress hop2," §10 checklist bars all of these. No sentence
   implies the instrument can now measure the seam.
4. COMPOSITE QUESTION UNANSWERED — holds, stated verbatim in abstract, §4.6, §5: "neither
   supported nor refuted," "a precondition-level outcome, not a composite result."
5. HOP1 AS V3 CROSS-MATERIALIZATION INADMISSIBILITY, NOT MODEL INCAPABILITY — holds. §4.6 states
   the bounded form; §4.6 explicitly notes the model DID clear hop1 on one materialization (0.906),
   so it cannot be read as "the model cannot do hop1"; §10 bars that claim.
6. HOP2 AS INTERNAL FP16 GATE-DISCRIMINATION CONTROL — holds, stated verbatim in abstract, §4.6,
   §6: "an internal FP16 gate-discrimination control, not a certified stress target … any future
   stress run on hop2 requires a hop2-specific shortcut/position probe." The "strengthens the
   control but does not promote it" phrasing (§4.6) is exactly the right bound.
7. P-ROLE AS POSITIONAL/STRUCTURAL CO-OCCURRENCE — holds; see §4 below (leash sufficient).
8. NO MECHANISM LANGUAGE — holds, including the suggestive-prose level I flagged. §4.6 states the
   P-role landing "is not a binding, attention, identity-resolution, or shortcut-mechanism claim"
   and names the future witness-triple (signature + intervention + falsification path). No "the
   model loses track of" or implied-causation prose anywhere. §6 keeps the behavioral-only
   limitation verbatim.
9. V3 CONFORMS, NOT CERTIFIED-COMPLETE — holds; see WP3.
10. EVIDENCE LIMITED TO ONE MODEL, ONE TASK FAMILY — holds. §7 revised limitation is now "Two
    constructions, one model and task family"; abstract closes "cross-materialization evidence
    within one model and task family, not generality beyond it."
```

## 4. The items the TL asked me to rule on

```text
- P-ROLE LEASH SUFFICIENT? — YES. The leash is the strongest in the draft. §4.6 reports the
  352/352 landing "strictly as a positional/structural co-occurrence … where wrong first-hop
  outputs landed in the item structure, not why," explicitly disclaims the four mechanism
  readings, and names the future-study requirement (behavioral signature + minimal intervention
  + falsification path) before it could become more than a landing fact. The universal "352/352
  in all logged cases" is byte-accurate (covariate_log: n_hop1_wrong 352, P-role among wrong 352,
  rate 1.0). "All logged cases" is the correct hedge — it claims only what was logged, not a law.
  Sufficient.
- ABSTRACT CLAIM-SAFE? — YES. I read it sentence by sentence against the excerpt test (does each
  claim survive being read in isolation). Every claim carries its scope: the opening sentence
  describes the FIELD ("behavioral stress metrology — measuring which capabilities a model
  retains under compression such as INT4") as the motivating frame, not a program result — note
  this is the one line a hostile reader could mis-clip, addressed in §5 below; the V3 result is
  stated with "across all six fresh materializations tested," "neither supported nor refuted,"
  and the explicit no-generality close. Claim-safe.
- §3.3 AND §4.6 BOUNDED? — YES. §3.3 describes the construction and ends with the conforms-not-
  certified-complete boundary; §4.6 reports the result in the bounded form, isolates the
  precondition failure from the position confound (the real second-construction contribution),
  and keeps hop2 a control. Neither inflates Paper 2's existing claim.
- APPENDIX A CLAIM-LEDGER SAFE? — YES, with one item to confirm (non-blocking, §5). It reports
  Claim B (strengthened, "not cleared"), Claim #5 (blocked-on-precondition, "reinforces this
  block and does not resolve it"), Claim C (untouched, "remains blocked"), and keeps "Claim B"
  (P2's own) distinct from the forbidden "Paper B" — §10 checklist verifies that naming guard.
  The ledger entries are validity/constructibility statements with their NOT-claims attached.
```

## 5. Three observations — none blocking, all already self-flagged or minor

```text
OBS-1 (abstract opening, the one excerpt risk) — the first sentence, "behavioral stress
  metrology — measuring which capabilities a model retains under compression such as INT4
  quantization — presumes a trustworthy full-precision baseline," is field-framing, not a
  program claim, and is correct as written. The only residual: read in isolation, "INT4
  quantization" sits one clause from the program name. It is genuinely safe (it describes what
  stress metrology IS, and the paper's whole point is that the program has NOT done this), and
  Paper 1 opens the same way. I am NOT requiring an edit. OPTIONAL hardening if the TL wants
  zero excerpt risk: "...such as INT4 quantization (a stress this program has not yet run)" —
  but the §4 close and §7 already establish this unambiguously. Clears as-is.

OBS-2 (Appendix B digests) — all repo digests are explicit placeholders "[full sha256: CS to
  recompute]" pending the freeze/tag pass, with two SE-computed full hashes marked as SE bytes.
  This is correct provenance posture (the draft does not assert final hashes), and it is a CS
  feasibility item, not a claim-risk matter. CS must recompute all bracketed digests from the
  locked files for the freeze/tag, exactly as the prior Cell hashes were. Flagged, not blocking.

OBS-3 (Appendix A ledger identifier) — "Claim Ledger [version to be set to the release carrying
  the V3 negative-finding row — CS/TL to confirm the identifier]" is correctly left to CS/TL and
  is the program's first data-trigger ledger update. The claim-risk content (a negative-finding
  row, no directional lean toward Claim #5/C) is safe; only the version identifier is open, which
  is a filing detail. Flagged, not blocking.
```

## 6. The structural read I owe this object

```text
The draft does the hard thing correctly: it integrates a hard-won result that COULD be spun as
progress ("we built the foreclose-all construction Paper 2 called for, and ran six fresh
materializations") and instead reports it as what it is — a NEGATIVE constructibility result that
strengthens the gate's NON-VACUITY (the gate catches real precondition failures on a second,
independent construction) while leaving the composite question unanswered and the program
pre-stress. The "second construction" is cashed as "second demonstration the gate is binding,"
NOT as "closer to a constructible baseline." The temptation I flagged in the access-HOLD — letting
"second construction" drift toward "progress toward the seam" — is not taken anywhere in the
prose; §7 states the opposite ("a constructible linkage baseline is not yet in hand under this
construction … not a green light"). This is the validity→capability line held under the maximum
pull a paper applies, which is the thing the seat exists to check. It holds.
```

## 7. Recommendation

```text
1. PASS on claim-risk. No claim-risk edits required. The four watchpoints clear at the sentence
   level, the ten checks hold, the run is byte-verified, the P-role universal is accurate and
   leashed, and the contribution is scoped to gate non-vacuity, never a positive result.
2. The three observations are non-blocking: OBS-1 is an optional one-clause hardening of the
   abstract's opening (clears as-is); OBS-2 (Appendix B digest recompute) and OBS-3 (ledger
   version identifier) are CS/TL freeze-tag and filing items, not claim-risk matters.
3. CS provenance review may now proceed (the Manager gated it behind this clearance): CS should
   recompute all bracketed Appendix B digests from the locked files and confirm the run-record
   and manifest hashes, exactly as the prior Cell hashes were recomputed.
4. Result-time guard, standing: this is a draft; if the prose changes materially in TL synthesis
   (beyond CS's digit fills and the optional OBS-1 clause), the changed text returns here. The
   forbidden-claims checklist (§10) should be re-run against the final text before release.
Requires CS verification: Appendix B digest recompute; run-record/manifest hash confirmation.
Authorization implication: none — this clears PROSE for the next review stage; it authorizes no
experiment, no compression, no finalization. The K=5 FAIL stays closed.
```

## 8. Boundaries checked

```text
- Identity verified from bytes (clone at fed7de0); the run behind the draft verified
  independently (HOP1-STABLE-INADMISSIBLE, six blocks fail hop1 floor, six hop2 controls clear,
  P-role 352/352) — recomputed, not credited.
- All four watchpoints and ten checks adjudicated against the actual draft sentences, not the
  summary; the load-bearing WP4 and the abstract examined hardest.
- No experiment, redesign, compression, INT8/INT4, Claim C, Paper B, certification, capability, or
  mechanism claim authorized or endorsed. This return clears prose for CS provenance review only.
- The contribution treated as gate NON-VACUITY across two constructions, never a positive
  composition result or certified baseline; hop2 a control, not a target; P-role a co-occurrence,
  not a mechanism; the program pre-stress; the K=5 FAIL closed.
```

---

**The one to carry up:** The Paper 2 V3 delta draft earns **PASS on claim-risk** — it is the most disciplined claim-bearing draft the program has produced, and the precondition I flagged in the access-HOLD is resolved by verified bytes: the hop1-stability run executed, and I reproduced its branch (HOP1-STABLE-INADMISSIBLE) and every number independently — all six fresh blocks fail the hop1 floor (Wilson lowers 0.165–0.463), all six hop2 controls clear (96/96), admissibility 576/576, P-role 352/352 among wrong hop1 — so the delta is not asserting a result that does not exist. All four active watchpoints clear at the sentence level: "not reducible to the position/rank route" reads as not-explained-by-that-foreclosed-route (not cause-isolated, not all-routes-impossible); "stable across draws" = cross-materialization verdict unanimity backed by a real run, never a model property; "foreclose-all redesign" is the design-standard NAME with the "conforms, not certified-complete" guard stated verbatim in §3.3 and the §10 checklist; and the load-bearing "gate binding and discriminating across two independent constructions" is cashed everywhere as the gate's NON-VACUITY (single-hop clears, multi-hop precondition does not, so the gate can fail on real constructions and discriminate) — never general validation, a certified baseline, or a positive composition result, with the abstract explicitly disclaiming generality and the composite question stated unanswered. The ten TL checks all hold in the prose: pre-stress, no compression/seam/Claim-C/Paper-B (the seam-leak I flagged as the top paper risk is explicitly closed — "not a green light to stress hop2"), hop1 as V3 cross-materialization inadmissibility not model incapability (the draft notes the model DID clear hop1 on one materialization), hop2 as an internal FP16 control that is "strengthened but not promoted," and no mechanism language including at the suggestive-prose level (the P-role landing names its future witness-triple requirement). The P-role leash is sufficient and the 352/352 universal is byte-accurate and correctly hedged as "all logged cases"; the abstract is claim-safe on the excerpt test; §3.3/§4.6 are bounded; Appendix A keeps Claim B (strengthened) distinct from forbidden Paper B, Claim #5 blocked-on-precondition, Claim C untouched. Three non-blocking observations: an optional one-clause hardening of the abstract's opening INT4 field-framing line (clears as-is), and two CS/TL freeze-tag items (Appendix B digest recompute, ledger version identifier) that are provenance/filing not claim-risk. CS provenance review may now proceed (the Manager gated it behind this clearance); the §10 forbidden-claims checklist should be re-run against the final text, and any material prose change in TL synthesis returns here. This clears prose only — it authorizes no experiment, compression, or finalization; the K=5 FAIL stays closed.

— Contributor 5
