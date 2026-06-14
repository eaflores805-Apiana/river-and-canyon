# CS Verification — G6 Standing Rejection-Audit Spec v0.1

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior, Manager
**In response to:** `MANAGER-DIRECTION-G6-STANDING-REJECTION-AUDIT-SPEC-VERIFICATION-2026-06-14.md` (Manager direction, this turn)
**Artifact verified:** `governance/2026-06-11_lane-1a-prime/certification-readiness/G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md` (sha256 `2b4cedf8c7f748b1a9cc8718db2bc568b4491ec33704a2823601172e59696033`)

---

## §0. Verdict (Manager's return format)

```text
PASS:
  G6 spec correctly defines a standing rejection-audit component and is safe to
  route as the first missing Tier 1 module.
```

The spec defines a non-circular procedure for auditing the gate's REFUSE decisions: mechanized independence is required (via at least one of three named channels) before any REFUSAL-CONFIRMED is emitted; the absence of an independent channel deterministically routes to AUDIT-CIRCULARITY; Paper A's four audit questions are carried forward with the Q1-vs-Q2/Q3 catches distinction preserved; the human/mechanized boundary keeps construct-validity judgement on the human side; validation targets (CAL-Q / CAL-E / no-channel) are framed as future-build targets only. No blockers; no corrections required.

---

## §1. Anchor and sealed-bytes posture

Spec §0 anchors on `origin/main HEAD cfa4ee6` — current at draft time (matches my most recent push). Sealed bytes UNCHANGED (≈70th survival check):

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`) UNCHANGED.

## §2. Required checks (Manager §"Required checks", items 1–10)

| # | Check | Spec evidence | Verdict |
|---|---|---|---|
| 1 | G6 is described as specified, not built | §0: "NOT: a built tool. This is the SPECIFICATION of the audit; no code is delivered." §0: "Building and exercising it is what would raise that claim to 'established.'" §11: "These are validation targets for a FUTURE build; this spec runs nothing and asserts no result." | **PASS** |
| 2 | The spec authorizes no model execution | §0: "Authorizes no model execution and no software build." §12 first entry: "No model execution." | **PASS** |
| 3 | The spec authorizes no software build | §0 explicit. §12 last entry: "No software build." §11: "When G6 is eventually built (separate authorization)…" | **PASS** |
| 4 | The spec does not reopen D4 | §12: "No D4 rescue." Spec is purely an audit-design artifact; no path back to a D4 candidate baseline. | **PASS** |
| 5 | The spec does not authorize a CAL-Q rerun | §12: "No CAL-Q rerun." §11 frames CAL-Q strictly as a validation target for a FUTURE G6 build, not as a re-execution request. | **PASS** |
| 6 | No certification / compression / INT8/INT4 stress / second rung / full ladder / Claim C | §12 enumerates all six verbatim. | **PASS** |
| 7 | Paper A v1.0 remains the source of truth | §0: "Paper A v1.0 and the Tool Spec v0.1 are the sources of truth; where this spec disagrees with either, they win." §1 K1/K2 cite Paper A §5.1 explicitly. | **PASS** |
| 8 | Tool Spec v0.1 remains the architecture reference | §0 names Tool Spec as co-source of truth. §1 K1-K6 explicitly cite Tool Spec C1/C2/C4/C5/C6 and §8. §2/§3 anchor triggers and inputs to Tool Spec G4/EP1-EP6. | **PASS** |
| 9 | No claim the rejection audit has been exercised as a standing module | §0: "the by-hand discipline of Paper A's two episodes"; "the component whose absence makes Paper A's non-vacuousness claim 'suggested by two worked episodes, not established by a standing mechanism.'" §2 "STANDING, NOT SAMPLED" is forward-looking ("the audit runs on EVERY qualifying refusal as a matter of course — that is what makes it 'standing' rather than the by-hand…episodes of Paper A"). §11 explicit: "this spec runs nothing." | **PASS** |
| 10 | No claim of general non-vacuousness beyond two worked episodes | §0 quotes the verbatim Paper A v0.9 W2 downgrade. §7: "the accumulating evidence … is the record that, over many confirmed refusals, WOULD move non-vacuousness from 'suggested' to 'established'" (future-conditional). §11: "would be the first evidence that moves non-vacuousness from 'suggested by two episodes' to 'demonstrated by a standing mechanism'" (also future-conditional). | **PASS** |

All ten numbered checks: **PASS.**

## §3. Mechanized independence check (Manager §"Mechanized independence check") — load-bearing

Manager's load-bearing rule: "A refusal cannot be independently confirmed by rerunning the same read that produced the refusal."

K1 in spec §1: "The audit's confirming read must be MECHANIZED-INDEPENDENT of the read that produced the refusal (Paper A §5.1, Tool Spec C6/G6/EP6/FC7). Re-running the same per-item read is NOT independence." Verbatim preservation.

Manager's required independent-channel options (at least one before full confirmation):

| Manager-required channel | Spec §4 channel | Match |
|---|---|---|
| blind second reader | CH1 BLIND SECOND READER ("classifies the raw per-item outputs (E3) WITHOUT seeing the gate's decision, the original reader's labels, or the route") | **Match** |
| pre-registered output-classification schema applied without route knowledge | CH2 PRE-REGISTERED OUTPUT-CLASSIFICATION SCHEMA, APPLIED WITHOUT ROUTE KNOWLEDGE ("fixed BEFORE the outputs were seen, applied to raw outputs (E3) by someone/something with no knowledge of the gate's decision") | **Verbatim match** |
| external ground-truth labels | CH3 EXTERNAL GROUND-TRUTH LABELS ("Labels from a source independent of the gate") | **Match** |

Manager's required explicitly-insufficient list:

| Manager-required insufficient | Spec §4 "NOT mechanized independence" entry | Match |
|---|---|---|
| same reader re-reading with knowledge of prior verdict | "the same reader re-classifying with knowledge of their own prior verdict" | **Match** |
| same per-item read rerun | "re-running the SAME per-item read that produced the refusal (K1 — the circularity)" | **Match** |
| post-hoc schema written after seeing outputs | "a schema written AFTER seeing the outputs (post-hoc; no better than the original read)" | **Match** |
| automated proxy that merely repeats the original read's heuristic | "an automated proxy that pattern-matches the original read's heuristic (it re-applies the same standard by other means)" | **Match** |

Four-for-four on insufficient list. Three-for-three on independent-channel list.

§4 closing rule: "zero channels available ⇒ the audit cannot fully confirm (§6, the limited status)." Fail-closed on missing channel is enforced architecturally. **PASS.**

## §4. Output-class check (Manager §"Output-class check")

| Manager-required output | Spec §6 output | Match |
|---|---|---|
| REFUSAL-CONFIRMED | REFUSAL-CONFIRMED | **Exact** |
| REFUSAL-REVERSED | REFUSAL-REVERSED | **Exact** |
| REFUSAL-QUARANTINED | REFUSAL-QUARANTINED | **Exact** |
| AUDIT-INCONCLUSIVE | AUDIT-INCONCLUSIVE | **Exact** |
| AUDIT-CIRCULARITY | AUDIT-CIRCULARITY | **Exact** |

Five-for-five exact name match (no naming-drift adjudication needed).

Manager-required especially-verify items:

- **REFUSAL-CONFIRMED requires an independent channel.** Spec §6 REFUSAL-CONFIRMED definition: "An independent channel (§4) confirms the defect; Q1-Q4 hold." §6 closing: "The essential pair is **REFUSAL-CONFIRMED requires an independent channel**, and **AUDIT-CIRCULARITY is what is returned when none exists** — never a silent or default confirmation." **PASS.**
- **AUDIT-CIRCULARITY is returned when no independent channel is available.** §6 AUDIT-CIRCULARITY definition: "NO mechanized-independent channel was available (§4), so the refusal cannot be INDEPENDENTLY confirmed. … This is the LIMITED status (K3): the audit declines to call the refusal independently confirmed, and says why. (This is FC7 from the Tool Spec, realized as an output class.)" **PASS.**
- **No independent channel means no full confirmation.** §6 closing rule above. §4 closing: "zero channels available ⇒ the audit cannot fully confirm." K3 in §1: "FAILS CLOSED: when it cannot independently confirm, it returns a limited/quarantine status, never a silent pass." **PASS.**

## §5. Audit-question check (Manager §"Audit-question check")

Manager-required Q1–Q4: was the refusal correct / could it be a scoring artifact / do per-item reads confirm it / was the rule pre-declared.

Spec §5 Q1: "WAS THE REFUSAL CORRECT?" Q2: "COULD THE REFUSAL BE A SCORING ARTIFACT?" Q3: "DO PER-ITEM READS CONFIRM IT?" Q4: "WAS THE RULE PRE-DECLARED?" **Four-for-four exact match.**

Manager's required distinction:
- Q2/Q3 can catch aggregate-vs-item disagreement.
- Q1 with mechanized independence is required to catch reading-standard miscalibration.

Spec §5 closing mapping block: "Q2 + Q3 are answerable WITHOUT a fresh independent channel (they re-examine the existing scoring and items) — they catch the AGGREGATE-vs-ITEM artifact (CAL-E). Q1 with full force REQUIRES an independent channel (§4) — only then can the audit catch READING-STANDARD MISCALIBRATION, not just aggregate-vs-item disagreement (K2). This mapping is why 'no independent channel' yields a LIMITED status: Q2/Q3 can still run, but Q1 cannot be answered at full strength." **Verbatim match to Manager's required distinction. PASS.**

## §6. Human semantic-read boundary (Manager §"Human semantic-read boundary")

Manager-required mechanized side: triggering audits / assembling records / comparing independent labels / emitting audit status / enforcing fail-closed routing.

Spec §10 MECHANIZED side:
- "triggering the audit on every refusal (§2);"
- "assembling the evidence (§3) and the audit record (§9);"
- "comparing the independent channel's labels to the original read and computing agreement/disagreement;"
- "emitting the output class per the decision rule (§6) and enforcing fail-closed on missing channels."

Five Manager items map onto these four bullets (Manager's "assembling records" + "comparing independent labels" + "emitting audit status" + "enforcing fail-closed routing" all present; "triggering audits" matches bullet 1). **Full coverage.**

Manager-required human-semantic-read side: construct-validity judgment / designing independent schemas / blind reading protocols / adjudicating inconclusive cases.

Spec §10 HUMAN side:
- "THE CONSTRUCT-VALIDITY JUDGEMENT ITSELF (Tool Spec §8, K6) … A blind second reader (CH1) is still a HUMAN read; a pre-registered schema (CH2) was authored by a human; external labels (CH3) were annotated by humans."
- "DESIGNING THE INDEPENDENCE CHANNEL: writing the blind-reading protocol or the pre-registered schema is a human design act."
- "ADJUDICATING AUDIT-INCONCLUSIVE cases: when an independent channel partially disagrees, resolving it is a human semantic read."

Four-for-four match (Manager's "designing independent schemas" and "blind reading protocols" both map to "DESIGNING THE INDEPENDENCE CHANNEL").

Manager's most important check: "The spec must not imply that G6 removes human judgment of meaning. It should only mechanize independence and bookkeeping."

Spec §10 closing: "mechanizing the audit means mechanizing the INDEPENDENCE and the bookkeeping — never the semantic judgement of meaning. An audit that automated the construct-validity judgement would re-introduce the very shortcut the gate exists to refuse." **Verbatim alignment to Manager intent. PASS.**

## §7. Evidence-packet check (Manager §"Evidence-packet check")

| Manager-required content | Spec §9 entry | Match |
|---|---|---|
| audit output class | AR1 ("AUDIT OUTPUT CLASS (§6)") | **Match** |
| link to the refusal being audited | AR1 ("…and the refusal it audited (link to the refusal's own packet)") | **Match** |
| independence channel used, or explicit no-channel note | AR2 ("WHICH CHANNEL was used (CH1/CH2/CH3) or, if none, an explicit 'no independent channel available' note that justifies an AUDIT-CIRCULARITY output") | **Verbatim match** |
| answers to Q1–Q4 | AR3 ("THE FOUR QUESTIONS Q1-Q4 with their per-question results, including which were answerable at full strength and which were limited by channel availability") | **Match** |
| reversal details if applicable | AR4 ("FOR REVERSALS: the producing rule flagged for review, and the corrected reading") | **Match** |
| provenance / hashes | AR5 ("PROVENANCE: hashes of the raw outputs, the independent channel's labels (if any), and the audit's own decision rule (pre-declared)") | **Match** |
| scope stamp | AR6 ("SCOPE STAMP: the family/model the audit is scoped to") | **Match** |
| interim-status disclosure where independence is absent | AR7 ("INTERIM-STATUS DISCLOSURE (until independent channels are routinely available): an explicit statement, per Tool Spec EP6, of whether the refusal rests on a read WITH or WITHOUT mechanized-independent confirmation") | **Verbatim match** |

Eight-for-eight required contents present. **PASS.**

## §8. Validation-target check (Manager §"Validation-target check")

Manager's permitted pattern: validation targets framed as future-build only, with the three target pairs (CAL-Q → REFUSAL-CONFIRMED / CAL-E → REFUSAL-REVERSED / no channel → AUDIT-CIRCULARITY).

Spec §11: "When G6 is eventually built (separate authorization), it should reproduce Paper A's two by-hand verdicts as a standing procedure:
- CAL-Q … should return REFUSAL-CONFIRMED.
- CAL-E … should return REFUSAL-REVERSED.
- A refusal with NO independent channel available: G6 must return AUDIT-CIRCULARITY (limited status), NOT REFUSAL-CONFIRMED.
These are validation targets for a FUTURE build; this spec runs nothing and asserts no result."

All three Manager-permitted target pairs present; explicit "FUTURE build" framing; explicit "this spec runs nothing and asserts no result." **PASS.**

## §9. Scope boundary (Manager §"Scope boundary")

Manager-forbidden generalizations and spec evidence none are made:

| Forbidden generalization | Spec evidence the generalization is NOT made |
|---|---|
| proof the model cannot abstain | No spec element. §7 explicitly: "a confirmed refusal is still scoped to its family/model (K5); it is not generalized." |
| proof D4 can never work | §12: "No D4 rescue." Spec is silent on D4 viability beyond what is closed. |
| proof all absence-defined tasks fail | No spec element. K5 inheritance + §7 scope-stamp ban on generalization. |
| proof the seam is false | No spec element. §9 (of Tool Spec) reference inherited: "The SEAM (Claim C): open, deferred. Nothing here activates it." |
| proof compression fragility has been tested | §12: "No compression / No INT8 / INT4 stress / No second compression rung." |
| proof the gate works generally | §0 NOT: "a way to manufacture confidence." K5 SCOPE INHERITED. §6 LIMITED status semantics. |

Six-for-six forbidden generalizations NOT made.

Additional standard forbidden-phrasings grep ("model passed" / "capability established" / "candidate certified" / "task family viable" / "Claim C progressed" / "seam evidence" / "public benchmark result" / "certification achieved" / "compression-robust"): **zero matches.** **PASS.**

## §10. Closed-gates perimeter (Manager §"Boundary")

| Manager-required closure | Spec §12 entry | Match |
|---|---|---|
| No model execution | No model execution | **Match** |
| No new run | No new run | **Match** |
| No D4 rescue | No D4 rescue | **Match** |
| No CAL-Q rerun | No CAL-Q rerun | **Match** |
| No certification run | No certification run | **Match** |
| No compression | No compression | **Match** |
| No INT8 / INT4 stress | No INT8 / INT4 stress | **Match** |
| No second compression rung | No second compression rung | **Match** |
| No full ladder | No full ladder | **Match** |
| No Claim C activation | No Claim C activation | **Match** |
| No public benchmark packaging | No public benchmark packaging | **Match** |
| No funder-facing release | No funder-facing release | **Match** |
| No SBIR submission | No SBIR submission | **Match** |
| No software build | No software build | **Match** |

**14-for-14 verbatim match. PASS.**

## §11. Final verdict

```text
PASS:
  G6 spec correctly defines a standing rejection-audit component and is safe to
  route as the first missing Tier 1 module.
```

No blockers. No corrections requested. The spec is filable as the first missing Tier-1 module specification, model-free, with mechanized independence preserved as the load-bearing constraint, REFUSAL-CONFIRMED gated on an independent channel, AUDIT-CIRCULARITY enforced as the no-channel status, Paper A's four audit questions preserved with the Q1-vs-Q2/Q3 catch distinction intact, the human-semantic-read boundary preserved, and validation targets framed strictly as future-build.

CS does NOT decide:
- Whether to authorize a G6 BUILD (Manager only; the spec correctly names the build as separately-authorized future work).
- Which independence channel (CH1/CH2/CH3) the eventual build should implement first (Senior + Manager; the spec deliberately leaves this as a build-time design call).
- Whether the spec should be re-located to a dedicated `tier-1-instrument/` subdir (TL/Manager organization call; current location in `certification-readiness/` co-locates with related specs but does not misclassify).
- Whether v0.1 is the right increment to share with external collaborators (Manager).

— CS Engineer, 2026-06-14
