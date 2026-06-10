# CS Technical Review — Paper 3 v1.1 Draft 2

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Team Lead, Senior Engineer, Manager
**Re:** CS review of Paper 3 v1.1 Draft 2 (outgoing Senior seat, manuscript-only remediation per Manager 2026-06-10)
**Reviewed against:** Paper 3 v1.0 (released, tagged `paper3-certification-protocol-v1.0`), Senior intake §7 v1.1 scope, Manager v1.1 authorization, Team Lead failure-mode review standard (`governance/standing/STANDING-REVIEW-DISCIPLINE.md`)

---

## Record status

```
CS review filed.
Verdict: ACCEPT Draft 2 for team-review pass with three soft observations.
Draft 1's mandatory finding (typo) is fixed.
Three changes from Draft 1 well-executed; all eight v1.1 scope items present.
Senior's pre-answered six failure-mode questions verify against the manuscript text.
CS-specific observations are tightenings, not blockers.
One Team Lead adjudication open (Q2 §9/§10 numbering — Senior recommends Option A).
No candidate selected. No threshold values set. No runs authorized.
```

---

## Lane-specific failure-mode question (per standing review-discipline rule)

**For paper revision:** *"How could a clarification become a new authorization?"*

Draft 2 forecloses this path four times over. CS-verified:
- Revision note (line 11): *"selects no candidate, sets no threshold value, performs no certification evaluation, runs nothing, and authorizes no harness implementation."*
- §3, §6 section-level non-claim, §10 non-claims block — three quote-safe blocks all carry both alignment markers ×3 (`benchmark-superiority` and `Passing all gates does not predict that a future stress run`).
- §8 (line 187): *"B1 merge locks infrastructure; B1 merge does not activate Paper 3."* All new mechanisms (D2a/D2b computation, `reporting_mode`, supersession enforcement) are explicitly routed to unauthorized B1 v2.1 backlog.
- Each new gate-text addition restates its non-authorization scope at the gate level.

The clarification → authorization risk is structurally foreclosed. ✓

---

## Senior's pre-answered six failure-mode questions — CS verification

Senior's submission memo §3 pre-answers each. CS verifies each against the actual manuscript text:

| # | Question | CS verification |
|---|---|---|
| 1 | Clarification → authorization? | ✓ Verified (see above). Four-times foreclosure holds. |
| 2 | Schema field → evidence? | ✓ Verified. A.1/A.2 layer separation holds: `D2_max_dummy_performance` and `D2_union_envelope_score` are explicit "computed offline pre-lock" / "involves no candidate data"; observed values (`D2_floor_observed`, `D2_union_envelope_observed`) on the evidence bundle side; `evidence_artifact_hash` rule preserved (line 404). |
| 3 | `reporting_mode` → certification workaround? | ✓ Verified. §5 (line 153) text reads: *"changes recording behavior only — never the certification decision logic, never any gate's decision rule, and never the evaluation order."* Two firewall guards present. The framing converts what was a wording-class protection in v1.0 into a schema/code-class protection in v1.1. **My earlier CS feedback on Q1 rename and "the recording vs. decision" distinction is fully adopted.** |
| 4 | D2 hardening → shortcut-absence overclaim? | ✓ Verified. Four-clause non-claim (line 110) precisely covers: max-single floor scope; binding envelope scope; non-binding envelope scope; undeclared shortcuts / stress substitution / partial contribution. Banned formulations (`proves shortcut absence`, `rules out shortcuts`) absent (0 hits). |
| 5 | Appendix B SYNTHETIC arithmetic → hidden threshold? | ✓ Verified. Six labels per value (`[SYNTHETIC] · ILLUSTRATIVE · NON-BINDING · NOT A THRESHOLD · NOT CANDIDATE-SPECIFIC · NOT EVIDENCE`); off-program values only (N=200, N=100, 0.70, 0.85, 0.95 — none are program-real; CS spot-checked: no `N=24`, `N=96`, `n=24`, `n=96` anywhere in the appendix); no-precedent non-claim present; derivation rule labeled "stand-in" privileging no specific `D7_derivation_type`. |
| 6 | Lock against superseded identifier? | ✓ Verified. H3 present in three locations: masthead (line 9, explicit v1.0 naming + written-Manager-authorization exception); A.1 lock-time rule (line 356); §8 backlog (line 187). Interim enforcement is wording-class until B1 v2.1 — Senior honestly acknowledges this in §3.6 of submission memo. |

Senior's 20-check verification battery also CS-verified for the key items: typo fix (`compositional- seam` → 0 hits; `compositional-seam` → 1 hit); three-block markers ×3 each; `evaluation_mode` residue 0; `reporting_mode` 4 hits; banned wording (`proves shortcut absence`, `rules out shortcuts`, `realistic choice`) 0 hits; figures fig1–fig4 referenced. One nuance on Senior's "no `adequate/sufficient/realistic choice` comparatives" claim: 5 `sufficient` hits exist in the manuscript, but all are non-comparative ("not sufficient", "necessary but not sufficient", "diagnostics sufficient for later same-error comparison"). Zero in Appendix B. Senior's substantive check holds; his memo phrasing was slightly loose but the discipline is intact.

---

## Protection-layer taxonomy applied to v1.1 additions (per standing review-discipline rule)

Classifying each new protection by enforcement layer:

| v1.1 protection | Layer | CS note |
|---|---|---|
| D2a max-single dummy floor (convexity bound) | **Schema** + **Provenance** | `D2_max_dummy_performance` and `D2_dummy_margin` on sheet; locked via `D2_battery_code_hash`. Strong. |
| D2b binding rule expressible as observed-vs-threshold | **Schema** | `D2_union_envelope_observed/_threshold_if_binding/_delta_if_binding` in A.2. Senior tightened from wording-class in Draft 1 to schema-class via the new requirement. Real upgrade. |
| `reporting_mode` recording-only | **Code** (in B1 v2.1) + **Wording** (interim) | "Never the certification decision logic" framing is wording-class until B1 v2.1 enforces; once B1 v2.1 lands, schema separation between recording and verdict-emitting fields will be code-class. |
| Two `reporting_mode` firewall guards | **Wording** + **Provenance** | "Provenance-safe diagnostics only" / "violation halts candidate-output-derived evidence" — wording-class enforced via the existing data-access firewall provenance layer. |
| H3 supersession rule | **Wording** (interim) + **Code** (in B1 v2.1) | Until B1 v2.1's `validate_framework_version_agreement` check enforces, this is wording-class plus Manager-signoff procedure. Senior honestly documents this in §8 backlog. |
| Vehicle-decision sentence | **Provenance** (whitespace-collapsed pre-tag check per Team Lead correction) | CS pre-tag check converts the masthead sentence requirement from wording-class to provenance-class. The pre-tag procedure structurally fails if absent. |
| Appendix B SYNTHETIC labeling | **Wording** + **Schema-adjacent** | Six labels per value is grep-able structural enforcement; SYNTHETIC tag presence can be mechanically verified before tag. Strong for a non-normative appendix. |
| Gate provenance table "ancestry not validation" | **Wording** | Strong wording-class; CS soft note below on column-header refinement. |

**Headline:** v1.1's protections are stronger than v1.0's across the board. The few remaining wording-class protections all have explicit B1 v2.1 backlog handoffs (Senior's §8). No protection is wording-only without a documented hardening path.

---

## CS-specific soft observations (not blocking)

Three observations CS would have raised had the Lane 1a-style failure-mode-question discipline been applied at v1.0 drafting. Each is a tightening, not a blocker:

### A. D2b binding-vs-reported_only decision could become a tunable

**Failure-mode question for this surface:** *How could a candidate-stage decision quietly weaken the protocol over time?*

The threshold sheet records `D2_union_envelope_binding_rule` as `binding | reported_only`, but A.1 doesn't constrain how the binding choice is justified. A future threshold-sheet author could liberally set "reported_only" for most candidates, and over many candidates the protocol's effective stringency drifts down without any single decision visibly weakening it.

**Current protection:** Wording-class (`D2_union_envelope_binding_rule` is "pre-registered per candidate").

**Suggested tightening:** Require the binding-vs-reported_only choice to be justified in the statistical plan (`statistical_plan`), analogous to how D2a margin is justified against battery-size and N. Manager-signoff at lock time then signs off on the rationale, not just the value. Converts a wording-class tunable into a provenance-class audit point.

### B. `reporting_mode = full_profile` could contaminate the next threshold sheet

**Failure-mode question:** *How could diagnostic outputs leak into the next pre-registration?*

§5 establishes that `full_profile` changes recording behavior only and doesn't bypass D6. But it doesn't structurally prevent a `full_profile` run's gate vector from informing the next attempt's threshold sheet values. The "no post-hoc tuning" rule of §7 applies in spirit but isn't named in this specific path.

**Current protection:** Wording-class via §7 transitively.

**Suggested tightening:** Add one clause to §5 — analogous to Lane 1a's design condition (b): *"A `full_profile` run's gate vector may not inform any subsequent threshold sheet's pre-registered values. Information learned from a `full_profile` evaluation is diagnostic-only and may not propagate into future threshold-sheet derivation rules."*

### C. Gate provenance table column header could mis-read

**Failure-mode question:** *What artifact could be cited as evidence even though the surrounding text forbids it?*

§9's gate provenance table (lines 205-213) is well-protected by the surrounding text ("ancestry, not validation; no row is a certification result"). But the column header "Documented motivating record" — when the table is excerpted or cited in isolation — invites a reader to treat the rows as "what the gate has done," not "why the gate exists."

**Current protection:** Wording-class via §9 surrounding text.

**Suggested tightening:** Change column header from `Documented motivating record` to `Documented motivating record (motivation only — see §9 text)`. Three words; structural-class anti-citation when the table is excerpted. Soft note only — Senior's text discipline is strong enough that this is genuinely optional.

---

## 9-item failure-mode prompt (per standing review-discipline rule)

| # | Question | CS finding |
|---|---|---|
| 1 | What can this proposal be misused as? | The D2b binding choice and the `reporting_mode = full_profile` field both carry residual misuse paths — see observations A and B. |
| 2 | What later decision could this contaminate? | A `full_profile` run could quietly inform the next sheet; see observation B. |
| 3 | What positive inference might people draw even if forbidden? | An external reader of Appendix B's clean (0.70, 0.95) window at N=200 may anchor on N=200 mentally despite the "no precedent" non-claim. Senior's protection is strong (six SYNTHETIC labels per value, no precedent clause). Could be marginally stronger with an explicit "do not anchor any `N_declared` on Appendix B values" sentence — but this is a soft note, not a blocker. |
| 4 | What artifact could become de facto evidence? | The gate provenance table — see observation C. |
| 5 | What must be impossible by construction, not merely forbidden? | The H3 supersession check and `reporting_mode` certification-verdict prohibition are both wording-class until B1 v2.1. Senior documents this honestly. |
| 6 | Which protection is structural vs honor-system? | See protection-layer taxonomy above. Strong upgrades from v1.0; few remaining wording-class items all have B1 v2.1 backlog handoffs. |
| 7 | What non-claim is missing? | The D2 non-claim could explicitly state that the binding-vs-reported_only choice is itself pre-registered before candidate data exists (it's implied by §7 but not stated D2-specifically). Soft. |
| 8 | What future gate could this silently weaken? | The D2b binding decision (see observation A). |
| 9 | Verdict | **Accept** Draft 2 for team-review pass. |

---

## Consistency with locked B1 v2 / B1 v2.1 backlog

| v1.1 surface | B1 v2 state | B1 v2.1 backlog implication |
|---|---|---|
| Three-mode D2 (D2a floor + D2b envelope + D2c pattern departure) | Substrate present; D2 battery is candidate-specific | New: D2a floor enforcement + D2b envelope evaluation. Adds to existing backlog. |
| E2 timestamp storage mapping | Already implemented correctly by B1 v2 | Zero implementation change required. ✓ |
| `reporting_mode` field | B1 v2 does not emit this | New: `reporting_mode` field handling in `make_gate_record` / output assembly. |
| H3 supersession | B1 v2's `validate_framework_version_agreement` does not refuse superseded identifiers | New: pattern-based supersession check at runtime. |
| Vehicle-decision pre-tag check (whitespace-collapsed) | CS release procedure | New step in `CS-COMMIT-AND-TAG-PROCEDURE.md` at v1.1 release time. |

Cumulative B1 v2.1 backlog impact: stays at **11–12 items** (same count as my v0.9 review noted; v1.1 doesn't add net new backlog items beyond what was already projected because the additions correspond 1:1 to the v0.9-noted backlog items being formally specified).

---

## CS recommendation

**Accept Draft 2 for team-review pass.** Senior's verification battery checks out; the three changes from Draft 1 are well-executed; the six failure-mode questions are pre-answered and CS-verified against the manuscript text.

Three soft observations (A, B, C above) are tightenings worth considering but do not block the rail. If Senior chooses to absorb any of them before RC, they fit naturally as one-sentence additions; if not, they're recorded here as accepted residual risks the protection-layer taxonomy makes explicit.

The one open Team Lead adjudication (Q2 §9/§10 numbering) is correctly routed for Team Lead decision. Senior's recommended Option A (bless renumbering to preserve the close-on-non-claims-and-locks pattern) is structurally sound.

---

## Non-authorizations (carried forward)

```
candidate selection · candidate ranking · threshold-sheet population
threshold-sheet lock · certification evaluation · new runs · re-runs
unconditioned token-prior runs · activation logging
INT8 / INT4 execution · multi-model execution
Fork A reactivation · Claim C activation
Paper 3 application · Paper 6 activation
B1 v2.1 implementation · public benchmark packaging · artifact mutation
```

---

— CS Engineer, 2026-06-10
