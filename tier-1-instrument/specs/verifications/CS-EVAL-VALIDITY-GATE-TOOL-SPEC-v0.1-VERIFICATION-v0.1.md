# CS Verification — Eval-Validity Gate Tool Spec v0.1

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior, Manager
**In response to:** `MANAGER-DIRECTION-EVAL-VALIDITY-GATE-TOOL-SPEC-VERIFICATION-2026-06-14.md` (Manager direction, this turn)
**Artifact verified:** `governance/2026-06-11_lane-1a-prime/certification-readiness/EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1.md` (sha256 `fc0bee3fff93c970289e5d45335b8470da532bbb7f4410a46723b36c77f0fa36`)

---

## §0. Verdict (Manager's return format)

```text
PASS:
  Tool spec faithfully translates Paper A and is safe to route as Tier 1 architecture.
```

The spec preserves the implemented-vs-specified distinction exactly, holds the human-semantic-read line where Paper A holds it, operationalizes the C6 mechanized-independence requirement in three places beyond restatement, defines route decisions as `{PASS, NEEDS-REPAIR, QUARANTINE, REFUSE}` with no bare score emitted, keeps QUARANTINE distinct from REFUSE, and asserts no claim from the forbidden list. No blockers; no corrections required.

---

## §1. Anchor and sealed-bytes posture

Spec §0 anchors on `origin/main HEAD 55c9bc1`. After the prior batch-1 commit (`d291bca`, paper.md swap + CAL-Q plan + CS verification) the anchor is one commit stale; no anchor-load-bearing content has shifted. Sealed bytes UNCHANGED (≈69th survival check):

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`) UNCHANGED.

## §2. Required checks (Manager §"Required checks", items 1–12)

| # | Check | Spec evidence | Verdict |
|---|---|---|---|
| 1 | Paper A remains the source of truth | §0: "Paper A v1.0 is the source of truth; where this spec and Paper A disagree, Paper A wins." §9 first bullet repeats the deference. | **PASS** |
| 2 | The spec authorizes no model execution | §0: "MODEL-FREE SPECIFICATION. This document … authorizes no model execution." §10 first entry: "No model execution." | **PASS** |
| 3 | The spec authorizes no software build | §0: "… and builds no software." §10 last entry: "No software build (this is a spec, not a tool)." §3 G6 description: "Until built+exercised, the tool's 'non-vacuousness' is SUGGESTED, not established." (Frames G6 explicitly as not-yet-built.) | **PASS** |
| 4 | The spec does not reopen D4 | §10: "No D4 rescue." §9: "D4 rescue: CLOSED." No spec element introduces a candidate alternative D4 baseline or invites a D4 rerun. | **PASS** |
| 5 | The spec does not activate CAL-Q rerun / certification / compression / INT8/INT4 stress / second rung / full ladder / Claim C | §10 enumerates all seven verbatim. §9: "CAL-Q FINDING TRACK stays alive but secondary"; "PAPER B stress rung (G9): later, separately authorized"; "The SEAM (Claim C): open, deferred. Nothing here activates it." | **PASS** |
| 6 | G1–G5 are the only gates marked implemented / exercised | §3 explicit: G1 `[IMPLEMENTED]`, G2 `[IMPLEMENTED]`, G3 `[IMPLEMENTED]`, G4 `[IMPLEMENTED]`, G5 `[IMPLEMENTED]`. §3 boundary line: `--- boundary: everything below is SPECIFIED BUT UNBUILT (Paper A §4.3) ---`. | **PASS** |
| 7 | G6–G9 are marked specified but unbuilt | §3 explicit: G6 `[SPECIFIED]`, G7 `[SPECIFIED]`, G8 `[SPECIFIED]`, G9 `[SPECIFIED]`. §8 third group enumerates all four under "SPECIFIED-BUT-UNBUILT (no automation AND no exercised manual procedure yet)." | **PASS** |
| 8 | G1–G5 do not claim more than Paper A demonstrated | Each G1–G5 description points to the specific Paper A v1.0 evidence it operationalizes: G1↔§3.1 (off-ceiling baseline + CAL-A/B/C/E ceiling cases); G2↔§3.5 (CAL-E reversal); G3↔§3.3/§3.5 (form-level control + four-way correction); G4↔§3.2/§3.4 (CAL-Q refusal under pre-declared rule); G5↔artifact-locking discipline (LOCK-RECORD, D5/D5-B, provenance throughout). No overstatement: each gate is described in terms Paper A already evidences. | **PASS** |
| 9 | G6 standing rejection audit is not treated as already built | §3 G6 marked `[SPECIFIED]`; descriptor: "Status: NO run artifact exists; this is the highest-value remaining build. Until built+exercised, the tool's 'non-vacuousness' is SUGGESTED, not established." §5 EP6: until G6 is built, evidence packet "states explicitly that the refusal rests on the per-item read WITHOUT mechanized-independent confirmation (honest interim status, per C6)." | **PASS** |
| 10 | G7 same-error identity is not treated as already implemented | §3 G7 marked `[SPECIFIED]`; descriptor: "Specified; no implementation." | **PASS** |
| 11 | G8 cross-family / cross-model generality is not treated as demonstrated | §3 G8 marked `[SPECIFIED]`; descriptor: "Specified; Paper A is one family / one model only." §1 C5: "Scope is inherited, not expanded … the architecture is portable; the numbers are not." §6 FC8: "OUT-OF-SCOPE GENERALIZATION → the tool refuses to extend a decision beyond the family/model it was run on." | **PASS** |
| 12 | G9 full stress-retention pipeline is not treated as executed | §3 G9 marked `[SPECIFIED]`; descriptor: "PRE-STRESS; no rung has run; requires separate authorization." §9: "PAPER B stress rung (G9): later, separately authorized." §10 closes: "No compression / No INT8 / INT4 stress / No second compression rung / No full ladder." | **PASS** |

All twelve numbered checks: **PASS.**

## §3. Automated vs. human-read boundary (Manager §"Automated vs. human-read boundary")

Manager's required automatable side: counting, hashing, threshold comparisons, strict-vs-concept divergence flagging, packet assembly, quarantine bookkeeping.
Spec §8 AUTOMATABLE side enumerates: G1 ceiling/floor detection (threshold comparison), G2 strict-vs-concept *divergence flagging* (Manager language exactly), G3 four-way tallying (counting), G5 provenance/hash checks (hashing + comparison), EP1–EP5 packet assembly, QR1–QR3 quarantine bookkeeping. **Match.**

Manager's required human-semantic-read side: construct-validity judgment, scorer divergence adjudication, construct declaration, independent rejection-audit read.
Spec §8 REQUIRES HUMAN SEMANTIC READ side enumerates: G4 construct-validity judgement (the per-item semantic read), G2 *adjudication* (deciding which of strict/concept reflects the construct when they diverge — Manager's "scorer divergence adjudication" exactly), construct declaration IN1 ("No Mountain in the Sentence"), G6's independent confirming read. **Match.**

The most important Manager check — "G4 construct-validity judgment must remain human-semantic-read dependent; G6 rejection-audit confirmation must require mechanized independence" — is the spec's stated load-bearing constraint, called out by name at §8's close: "the construct-validity judgement (G4) and the audit's independent read (G6) are human semantic reads, not automated gates. A version of this tool that quietly automates G4 — by, say, pattern-matching 'looks like a value' — would be exactly the kind of shortcut baseline the gate exists to refuse." **PASS.**

## §4. Mechanized independence check (Manager §"Mechanized independence check")

Manager's required rule: "A rejection audit cannot confirm a refusal by simply rerunning the same read that produced the refusal."

C6 is stated verbatim from Paper A v1.0 §5.1 W1 fix in spec §1, and operationalized in three additional places:

1. **§3 G6 description:** "CRITICALLY (C6): the confirming read must be MECHANIZED-INDEPENDENT of the read that produced the refusal, or the audit is circular."
2. **§5 EP6:** "Until G6 is built, the packet states explicitly that the refusal rests on the per-item read WITHOUT mechanized-independent confirmation (honest interim status, per C6)."
3. **§6 FC7:** "if a refusal's only confirmation is the same read that produced it, the tool must DECLINE to call the refusal independently confirmed (C6) — a failure mode of the TOOL, surfaced honestly, not hidden."

Manager's required independence-channel options: blind second reader / pre-registered output-classification schema applied without route knowledge / external ground-truth labels.

Spec §1 C6 enumerates: "blind second reader / pre-registered schema applied without knowledge of the route / external labels." **Verbatim match across all three channels.**

Spec §2 IN7 additionally specifies the future independence-channel input requirement: "for the standing audit (G6): a blind-second-reader interface, a pre-registered classification schema, or external labels. SPECIFIED, not yet available." **PASS.**

## §5. Output schema check (Manager §"Output schema check")

Manager-required route decisions: `PASS / NEEDS-REPAIR / QUARANTINE / REFUSE`.
Spec §4 enumerates exactly these four, with no fifth and no bare-score option. **Match.**

Manager: "no bare score is emitted as the final output."
Spec §1 C1: "OUTPUT IS A ROUTE DECISION, NOT A SCORE. The gate emits one of {pass, needs-repair, quarantine, refuse} plus an evidence packet — never a bare retention number." §4: "No bare score is ever emitted (C1)." **PASS.**

Manager-required evidence-packet contents: decision + firing gate / per-item table / pre-declared rule / provenance block / scope stamp / audit result for refusals once G6 exists.
Spec §5: EP1 decision + which gate fired, EP2 per-item table (input/output/strict/concept/four-way), EP3 the pre-declared rule (with post-hoc flag), EP4 provenance block (model id+precision, item-set hash, scorer hash, run-record hashes), EP5 scope stamp ("evidence about the instrument, not the model"), EP6 audit result for refusals once G6 exists. **Six-for-six match.** PASS.

Spec §4 carries the honest disclosure: "in Paper A's family, NO candidate reached PASS — the certifiable region was unoccupied. PASS is defined here; it has not been observed." This is a positive correctness signal — the spec defines `PASS` without asserting any baseline has achieved it.

## §6. Quarantine check (Manager §"Quarantine check")

Manager-required distinction: QUARANTINE = cannot yet adjudicate; REFUSE = construct has demonstrably collapsed.

Spec §4 QUARANTINE: "The submission cannot be cleanly adjudicated — missing/unhashed inputs, non-conforming run, or scorer artifact unresolved." Spec §4 REFUSE: "The baseline's construct has demonstrably collapsed (G4): the surface score may look usable, but per-item reads show it no longer measures the intended capability."

Spec §7 QR4 is explicit: "Quarantine is NOT refusal: it means 'cannot yet adjudicate,' not 'construct collapsed.' The two are reported distinctly (a reader must not read a provenance gap as a construct failure, or vice versa)." **Verbatim distinction match.**

Manager: "The spec must not allow quarantined evidence to support claims."
Spec §7 QR1: "Quarantined submissions are HELD OUT of every claim until the blocking issue (FC4/FC5, or an unresolved FC3) is resolved; they do not pass by default and do not silently expire into a pass." **PASS.**

## §7. Claim boundary (Manager §"Claim boundary")

Forbidden claims and spec evidence:

| Forbidden claim | Spec evidence the claim is NOT made |
|---|---|
| a finished tool | §0 NOT: "a built tool. No code is delivered or implied." §10: "No software build (this is a spec, not a tool)." |
| a validated general method | §0 NOT: "a claim that the gate is validated. Paper A establishes it on ONE family / ONE model / N=2 episodes / pre-stress; this spec inherits exactly that scope." §1 C5 "scope is inherited, not expanded." |
| a product | §0 NOT: "an execution authorization, a benchmark, or a product. Those are downstream and separately gated." |
| a market-validated standard | No spec element invokes market / users / customers / benchmark adoption. |
| compression fragility | §10: "No compression / No INT8 / INT4 stress / No second compression rung." §9: "PAPER B stress rung (G9): later, separately authorized." |
| a seam result | §9: "The SEAM (Claim C): open, deferred. Nothing here activates it." §10: "No Claim C activation." |
| cross-family generality | §3 G8 SPECIFIED; §1 C5; §6 FC8 explicit out-of-scope refusal. |
| an executed stress-retention pipeline | §3 G9 SPECIFIED ("PRE-STRESS; no rung has run; requires separate authorization"). |

**Eight-for-eight: no forbidden claim is made.** Additional standard-forbidden-phrasing grep ("model passed" / "capability established" / "candidate certified" / "task family viable" / "Claim C progressed" / "seam evidence" / "public benchmark result" / "certification achieved" / "compression-robust"): zero matches. **PASS.**

## §8. Closed-gates perimeter (Manager §"Boundary")

Spec §10 list: "No model execution / No new run / No D4 rescue / No CAL-Q rerun / No certification run / No compression / No INT8 / INT4 stress / No second compression rung / No full ladder / No Claim C activation / No public benchmark packaging / No funder-facing release / No SBIR submission / No software build."

Cross-check against Manager's "Boundary" list: every one of Manager's 14 entries appears in spec §10. **One-to-one match. PASS.**

## §9. Final verdict

```text
PASS:
  Tool spec faithfully translates Paper A and is safe to route as Tier 1 architecture.
```

No blockers. No corrections requested. The spec is filable as a Tier-1 instrument planning artifact, model-free, with the implemented/specified split preserved exactly and the human-read invariant for G4 and G6 preserved as the spec's most important honesty constraint.

CS does NOT decide:
- Whether to authorize a G6 BUILD (Manager; the spec correctly names G6 as the highest-value next increment but requests no authorization).
- Whether the spec deserves a dedicated `governance/2026-06-11_lane-1a-prime/tier-1-instrument/` subdir or stays co-located in `certification-readiness/` (TL/Manager organization call).
- Whether v0.1 is the right increment to share with external collaborators or to base a build proposal on (Manager).
- Whether IN7 (the standing audit's independence channel) should be specified further now (Senior + Manager).

— CS Engineer, 2026-06-14
