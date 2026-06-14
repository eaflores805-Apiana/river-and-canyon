# CS Verification — CAL-Q Finding Diagnostic Plan v0.1

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior, Manager
**Status:** **PASS** — diagnostic separation clean; no D4 rescue implied; no execution authorization; per-item scorer control present in every branch; Manager safe-claim wording verbatim; closed gates intact; forbidden-language perimeter PASS
**In response to:** Owner split inside `CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1.md` §0/§11 — "CS verify the diagnostics are cleanly separated, do not reopen D4 rescue, imply no execution authorization."
**Artifact verified:** `governance/2026-06-11_lane-1a-prime/certification-readiness/CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1.md` (sha256 `0c2afbbc2218a2ba050a27a50ac0a6d2c5c51d8cbc42d8f8e262a7003f65a23e`)

Also filed this turn (separate item, separate scope): `papers/05_paper-a-before-retention/paper/paper.md` swapped from the v0.7-era source (sha256 `464a8889…`) to the v1.0 source (sha256 `4272e12a…`), resolving the CS flag from `CS-PAPER-A-GITHUB-BUNDLE-SWEEP-AND-VERIFICATION-v0.1.md` §3.

---

## §1. Plan anchor (informational)

Plan §0 anchors on `origin/main HEAD 3b7491b`. That was the HEAD when Senior drafted; the current HEAD (after the prior bundle-filing commit `55c9bc1`) has advanced one commit. The anchor is one commit stale but the plan's content is not affected by that commit (the bundle filing did not touch any D4 / CAL-Q artifact). Informational note only — no defect.

## §2. CS check #1 — D1 and D2 cleanly separated — PASS

The plan's §11 first check asks whether D1 (format-only) and D2 (difficulty-only) genuinely separate format and difficulty.

- **D1 §4 item 5 ("CLEAN-SIDE DIFFICULTY MOVEMENT: EXPECTED MINIMAL").** If clean accuracy drops materially, D1 has FAILED its design and is "void as a format-only test — re-design the form to be easier before interpreting." This is the right discipline: a confounded D1 cannot then be interpreted in either direction.
- **D2 §5 item 2 ("WHAT IS HELD FIXED: the direct-query FORMAT").** Format is fixed by construction. The §5 item 5 also makes clean-side movement REQUIRED (≤ 0.85) for D2 to be valid; if D2 can't induce clean-side movement under direct format, it is "INCONCLUSIVE-BY-CONSTRUCTION, not evidence either way." Right discipline again.
- **D1/D2 joint logic in §7.** The four indicative cells (D1 collapse + D2 preserved → format driver; D1 preserved + D2 collapse → difficulty driver; both preserved with CAL-Q still collapsed → combination; both collapse → multi-axis fragility) are correctly conditioned on each branch's design constraint holding. §7 explicitly states each cell is "a hypothesis the pattern would support, not a proof," and any branch that fails its own design constraint "is void rather than informative."

The branches are genuinely separated by enforced constraints, not by aspiration. **PASS.**

## §3. CS check #2 — no D4 rescue implied — PASS

The plan's §11 second check asks whether any branch (as written) constitutes or implies a D4 certification-readiness rescue.

- §0 explicit non-claim: "NOT: a D4 rescue. D4 is closed as a certification-readiness route and stays closed."
- §8 forbidden-claim list includes "D4 can never work" — handled as the SYMMETRIC forbidden claim (the plan also does not negatively foreclose D4; it preserves it as closed).
- §11 third bullet flags D3 specifically: "a gentle lever that preserved abstention would be a FINDING about the construct, and a candidate for future design work — it is not, by itself, a re-opened D4 route, and must not be packaged as one." Correct scoping.
- §9 ("Relationship to Paper A") preserves Paper A's primacy and explicitly says this track introduces no claim-safety issue for Paper A; if a CS or TL review finds any conflict, the conflict — not the diagnostic design — takes priority. Right deference order.

No branch is written in a way that, if executed and read positively, would constitute D4 re-opening. **PASS.**

## §4. CS check #3 — no execution authorization — PASS

The plan's §11 third check asks whether any execution authorization is stated or implied anywhere.

- §0 explicit non-claim: "NOT: an execution authorization. No run is approved by this document."
- §3 SCORER CONTROL: "every branch RUNS" → this is a future-tense conditional ("would run when executed under separate authorization"), not a present authorization. Read in §0 context, unambiguous.
- §4/§5/§6 each branch starts with "WHAT CHANGES" / "WHAT IS HELD FIXED" — these are *design specifications* for a hypothetical future run. No "we will run," "execute next," or "schedule for" language.
- §8 closing: "running them is a separate, future, authorized step."
- §10 closed-gate list (12 items) carries the standard verbatim closure (no model execution · no D4 rescue · no CAL-Q rerun · no certification · no compression · no INT8 / INT4 stress · no second compression rung · no full ladder · no Claim C activation · no public benchmark packaging · no funder-facing release · no SBIR submission).

No execution authorization is stated or implied. **PASS.**

## §5. CS check #4 — per-item scorer control in every branch — PASS

The plan's §11 fourth check asks whether every branch carries the per-item scorer control (so a future apparent collapse is confirmed-or-reversed before interpretation, per CAL-E/CAL-Q).

- §3 SCORER CONTROL is defined globally: "every branch runs the four-way report (strict / concept / true-false-emission / format-artifact) so an apparent collapse is confirmed real (as in CAL-Q) or reversed as an artifact (as in CAL-E) before it is interpreted."
- D1 / D2 / D3 each use the §3 ABSTENTION PRESERVED / COLLAPSE / INTERMEDIATE definitions, which by §3 construction carry the scorer-audit dependency.
- §3's HELD-FIXED BASELINE clause keeps each branch read against the SAME direct-query clean baseline and SAME content set, so a scorer artifact in one branch cannot be hidden by a baseline shift.

The four-way reporting schema is invoked in every branch by reference to §3. **PASS.**

## §6. Manager safe-claim wording — verbatim PASS

The plan's §8 reproduces Manager's verbatim CAL-Q safe-claim wording (binding):

> *In the D4 key-value family, direct-query defective abstention was robust across content-lever variants, but did not transfer to the code-book query format. The first query-side lever that produced meaningful clean difficulty also collapsed defective abstention to zero. This suggests abstention behavior in this construct is format-sensitive and may be coupled to retrieval difficulty.*

Whitespace-normalized comparison: **VERBATIM MATCH** to the Manager wording on record. The §8 forbidden-claim list (6 items: "Models cannot abstain" / "All absence-defined tasks fail" / "D4 can never work" / "The seam is false" / "Compression fragility has been tested" / "The mechanism is already established") matches the standing CAL-Q forbidden-claims register. **PASS.**

## §7. Standard forbidden-phrasings perimeter — PASS

Grep across the plan for the standard binding-forbidden phrasings (model passed / capability established / candidate certified / task family viable / Claim C progressed / seam evidence / public benchmark result / certification achieved / compression-robust / not shortcut-driven). **No matches.** Where the closely-related phrases appear (§8 forbidden-claim list), they are correctly framed as REJECTED uses, not as assertions.

Path A (rung-uniform) standing scope sentence and binding characterization are not load-bearing for this artifact (different lane); not expected, not flagged for absence.

## §8. Closed gates — PASS

§10 carries the standard 12-item closed-gate list verbatim. Consistent with the post-D4 / post-Path A standing closure. **PASS.**

## §9. Sealed bytes + posture

Sealed bytes UNCHANGED. ≈68th survival check.

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`) UNCHANGED.

No model run. No certification. No compression. All 12 closed gates intact.

## §10. Disposition

**PASS.** The diagnostic plan is model-free, cleanly separates the three candidate drivers (format / difficulty / combination + a gentle-query control), introduces no D4 rescue path, implies no execution authorization, preserves Paper A's primacy, carries the per-item scorer control in every branch, and reproduces Manager's safe-claim wording verbatim. It is filable as a finding-track planning artifact.

CS does NOT decide:
- Whether the plan's design constraints are *technically achievable* (e.g., whether D1's "rephrased-but-equivalent query that adds no difficulty" exists for this construct; whether D2 can induce clean-side movement under direct format where D4 content levers could not — the plan itself flags this as D2's design challenge in §7 risk note inside §5). These are Senior + Manager design judgments.
- Whether to authorize any future execution of any branch (Manager only; closed by §10).
- Whether D3 should be ordered before or after D1/D2 (Manager).
- Whether the diagnostic-plan track is the right next thing for the Manager's hybrid "instrument first, seam deferred" direction, or whether the standing rejection-audit BUILD (named in `PAPER-A v1.0 §6.3` as the recommended next model-free increment) should come first (Manager).

## §11. Companion item — bundle paper.md swap

Independent of the CAL-Q plan verification: the user also re-delivered the `paper-a/` bundle with a single file changed (`paper/paper.md` swapped from sha256 `464a8889…` to `4272e12a…` = `PAPER-A-v1.0.md` byte-identical). Bundle now self-consistent: paper.md and paper.pdf are a matched v1.0 pair. **The CS flag from `CS-PAPER-A-GITHUB-BUNDLE-SWEEP-AND-VERIFICATION-v0.1.md` §3 is CLOSED.** All other 17 bundle files unchanged this turn.

— CS Engineer, 2026-06-14
