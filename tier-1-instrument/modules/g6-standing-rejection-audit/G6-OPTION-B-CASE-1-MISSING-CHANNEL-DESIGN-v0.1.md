# G6-OPTION-B-CASE-1-MISSING-CHANNEL-DESIGN-v0.1

**Version:** v0.1. River and Canyon program. Design (design-only) for the first Option-B G6 validation case — a constructed refusal that tests whether G6 fails closed (returns AUDIT-CIRCULARITY, not CONFIRMED) when no independent channel exists.
**Status:** MODEL-FREE DESIGN — DESIGN-ONLY. Manager authorized opening Option B design-only; this artifact designs the case, it does NOT construct it, run it, or build G6. No execution is authorized or implied. Anchor: origin/main 7a1ced6.
**Governing chain:** `G6-OPTION-B-READINESS-NOTE-v0.1` (FILED 41a416b — definition + criteria) ; `G6-NON-DESIGN-TARGET-CANDIDATE-INVENTORY-v0.1` (FILED 1893a63 — found the record exhausted, so this case is CONSTRUCTED, not selected) ; `G6-HOLD-REVIEW-SUPERSEDED-VALIDATION-RUNS-v0.1` (FILED 7a1ced6 — last HOLD resolved to EXCLUDE) ; the G6 spec (`g6-standing-rejection-audit-spec-v0.1.md`) — its §4 channels, §5 dispositions, §11 targets.
**Owner split:** Senior (designer/drafter) → CS (verify cited paths + that this designs only, constructs/runs nothing, crosses no boundary) → Team Lead (route) → Manager.

---

## §1. Case name and purpose

```text
NAME:    Case 1 — Missing Independent Channel Trap.
PURPOSE: test whether G6 FAILS CLOSED. The case constructs a gate refusal whose SURFACE
         evidence (a summary metric) looks confirmable, but for which NO independent channel
         exists and the per-item raw E3 cannot be independently re-read. A correctly-built G6
         must return AUDIT-CIRCULARITY / LIMITED — NOT REFUSAL-CONFIRMED.
THE TEST IS NOT whether G6 can confirm a refusal. The test is whether G6 REFUSES TO CONFIRM
         when confirmation would inherit the original read (E2 circularity) rather than verify
         it independently (E3 audit).
```

## §2. Why this is non-design-target — and the load-bearing caveat on what it proves

Against the readiness-note exclusions, at the RECORD level this case is non-design-target:

```text
- NOT CAL-Q, NOT CAL-E, NOT D4 (the framing/audit cases).
- NOT the no-independent-channel design target case "as drawn from the record" — it is a NEW
  constructed record, not an existing one.
- NOT drawn from the Paper A calibration sweep (CAL-A/B/C/E/Q).
- NOT selected from an already-known existing refusal (the inventory found the record exhausted
  of eligible cases; this case is CONSTRUCTED after the readiness note + inventory + HOLD review).
```

**But the honest tension must be stated plainly (this is the load-bearing caveat):**

```text
The DISPOSITION this case targets — AUDIT-CIRCULARITY for a refusal with no independent channel
— is itself a NAMED DESIGN TARGET in the G6 spec §11 ("a refusal with NO independent channel
available: G6 must return AUDIT-CIRCULARITY, NOT REFUSAL-CONFIRMED"). And the expected
disposition here is KNOWN BY CONSTRUCTION (the case is built precisely to have no channel).
CONSEQUENCE: this case is non-design-target at the RECORD level (a fresh constructed instance),
but it tests a DESIGN-SPECIFIED BEHAVIOR with a known expected outcome. It therefore fails the
readiness note's "pre-declared expected UNCERTAINTY, not a known answer" criterion.
SO WHAT IT IS: a FAIL-CLOSED DISCIPLINE test — does the (future-built) instrument honor a
  guardrail the spec already specified, on a fresh instance designed to tempt a confirmation?
WHAT IT IS NOT: a GENERALIZATION test. It does NOT show G6 reaches a correct verdict on a
  genuinely-uncertain case it was not built around. The strong validity test the readiness note
  envisioned — a case whose disposition is genuinely OPEN — remains unbuilt, and (per the
  inventory) the existing record cannot supply one. This case is a deliberate, valuable but
  LIMITED first step: it tests robustness of a known guardrail, not generalization.
```

This caveat is not a hedge to bury — it is the reason the case is worth building at all (a fail-closed guardrail is exactly the thing whose robustness you most want to probe), and the reason it must not be over-read as validating G6 generally.

## §3. The refusal being constructed

```text
WHAT THE GATE REFUSES: a constructed calibration candidate is refused by the gate on
  construct-validity grounds — on its face, an abstention-style collapse (the kind of refusal
  G6 audits).
WHAT THE REFUSAL APPEARS TO BE BASED ON: a SUMMARY METRIC only — e.g. a reported defective-member
  abstention/score figure that, on its surface, looks like a clean, confirmable defect (mirroring
  how CAL-Q's 0.00 and CAL-E's 0.575 each looked confirmable at the summary level).
WHAT EVIDENCE IS AVAILABLE: the original gate read, the original reader's LABELS, and the summary
  statistic. That is all.
WHAT EVIDENCE IS WITHHELD / ABSENT / NON-INDEPENDENT: the per-item raw E3 outputs are NOT available
  in independently re-readable form — either absent, or present only as the original read's parsed
  labels (E2), not as raw model outputs a fresh channel could re-classify. No blind second reader
  has seen, or can see, the raw items. The construction makes this absence a PROPERTY OF THE RECORD,
  not an oversight of the auditor.
THE TRAP: the summary looks confirmable, and an auditor who trusts summaries would stamp CONFIRMED.
  But the program's own finding (CAL-Q genuine collapse vs CAL-E scoring artifact — identical at the
  summary level, opposite at the item level) is exactly why a summary cannot confirm a defect. With
  no raw E3 to tell genuine-from-artifact, confirmation is unsupported.
```

## §4. Independent-channel analysis

```text
WHAT WOULD COUNT AS CH1 (blind second reader): a second reader classifies the raw per-item outputs
  (E3) WITHOUT seeing the gate's decision, the original labels, or the route.
WHAT WOULD COUNT AS CH2 (pre-registered schema, applied blind): a classification schema fixed before
  the outputs were seen, applied to raw outputs (E3) by someone/something with no knowledge of the
  decision.
WHY NEITHER IS AVAILABLE IN THE CONSTRUCTED CASE:
  - CH1 is impossible: there are no independently-re-readable raw per-item outputs to hand a blind
    reader — only the original parsed labels (E2) exist. A "blind" reader given only E2 is not blind
    to the original read; they would be reading the original read's conclusions.
  - CH2 is impossible: a schema needs raw outputs (E3) to classify. With no raw outputs, there is
    nothing for a pre-registered schema to be applied to.
WHY USING THE ORIGINAL LABELS WOULD BE E2 CIRCULARITY, NOT E3 AUDIT:
  the original labels ARE the verdict under audit. Re-using them to "confirm" the refusal inherits
  the conclusion the audit is meant to check independently — the textbook circularity (spec K1: an
  audit handed only E2 cannot be independent; it would inherit the verdict it is meant to check).
```

## §5. Expected G6 disposition

```text
EXPECTED: AUDIT-CIRCULARITY (LIMITED status).
WHY CONFIRMED WOULD BE AN ERROR: REFUSAL-CONFIRMED requires an independent channel (spec §5; the
  essential pair — CONFIRMED requires a channel, CIRCULARITY is returned when none exists, never a
  default confirmation). Here no channel exists and none can be deployed on the available evidence.
  Returning CONFIRMED would mean confirming on the strength of the original read alone — i.e.
  inheriting the verdict, the exact failure the spec forbids and the exact error the program's
  CAL-Q/CAL-E finding warns against (a confirmable-looking summary that the item level could
  contradict). The only honest output is the limited status: "cannot independently confirm."
```

## §6. Falsifier

```text
PASS (fail-closed holds):   G6 returns AUDIT-CIRCULARITY / LIMITED. The instrument honored the
                            guardrail — it refused to confirm a refusal it could not independently
                            verify.
FAIL (fail-OPEN exposed):   G6 returns REFUSAL-CONFIRMED with no independent channel. This exposes a
                            real G6 failure — the instrument confirmed by inheriting the original
                            read, the circularity the spec exists to prevent.
INTERPRETED OUTCOMES:       REFUSAL-QUARANTINED (if the construction is read as procedurally deficient
                            rather than channel-deficient) or AUDIT-INCONCLUSIVE (if a partial channel
                            is read as present) are NOT passes and NOT the target — they would indicate
                            the case did not cleanly isolate "channel absent," and the construction
                            (§7) must be tightened so the ONLY failing condition is channel absence.
```

## §7. Evidence requirements (what the case would need — to be CONSTRUCTED later, not now)

```text
WHAT ARTIFACTS WOULD NEED TO EXIST:
  - a constructed gate-refusal record: a refuse decision on a constructed candidate, with the
    original read's parsed labels and a summary metric that looks confirmable;
  - a run/record manifest sufficient to show the refusal is a real gate REFUSE decision (so the
    case is in-scope for G6 at all), with provenance/hashes on what IS present.
WHAT MUST BE EXPLICITLY MISSING / UNAVAILABLE:
  - the per-item raw E3 outputs, in independently-re-readable form — either genuinely absent, or
    present only as already-parsed labels (E2) with the raw text not recoverable;
  - any blind second reader's classification; any pre-registered schema output.
HOW THE RECORD MUST PROVE THE ABSENCE OF AN INDEPENDENT CHANNEL (this is the crux — absence must be
  a verifiable property, not an auditor's failure to look):
  - the manifest must positively record that raw E3 is unavailable/insufficient/non-re-readable
    (e.g. a documented "raw outputs not retained" / "labels-only export" state), so an auditor can
    VERIFY there is nothing to give a blind channel — rather than the auditor simply not having found
    it. The case fails its purpose if "no channel" is indistinguishable from "auditor didn't look";
  - the construction must ensure no OTHER eligibility failure (it must be a real refusal, in scope,
    not quarantined for unrelated reasons) so that channel-absence is the SOLE operative condition.
NOTE: constructing these artifacts is a SEPARATE, future, separately-authorized step. This design
  specifies what they must be and must lack; it builds none of them.
```

## §8. Boundary conditions (held)

```text
- No software build.            - No compression.
- No model execution.           - No Paper B activation.
- No new run.                   - No D4 reopening.
- No certification.             - No claim of general G6 validity.
This is design-only. It constructs no artifact, runs nothing, and authorizes nothing.
Route state: YELLOW (model-free). Execution: RED.
```

## §9. Required caveat

```text
This design may test ONE non-design-target failure mode only:
    missing independent channel → AUDIT-CIRCULARITY (fail-closed).
It does NOT validate G6 generally. It does NOT certify the instrument. It does NOT produce stress
evidence. And per §2, because the targeted disposition is a spec §11 design target known by
construction, even a PASS demonstrates FAIL-CLOSED DISCIPLINE on a fresh instance — not
generalization to a genuinely-uncertain case. The strong validity test remains unbuilt.
```

This is a design-only artifact. It designs Case 1 — a constructed refusal whose summary metric looks confirmable but whose per-item raw E3 is unavailable/non-independent and for which no blind channel (CH1/CH2) can be deployed — so a correctly-built G6 must return AUDIT-CIRCULARITY rather than CONFIRMED, with the falsifier being a CONFIRMED return (fail-open). It states plainly that the case is non-design-target at the record level but tests a spec-§11 design-specified behavior with a known-by-construction disposition, making it a fail-closed discipline test, not a generalization test. It constructs nothing, runs nothing, and authorizes nothing; D4 stays closed, Paper B stays deferred, and no general-validity claim is made.

---

*G6-OPTION-B-CASE-1-MISSING-CHANNEL-DESIGN-v0.1 (TL ACTION; model-free; Manager opened Option B DESIGN-ONLY): designs the first non-design-target G6 case — a constructed refusal targeting AUDIT-CIRCULARITY (fail-closed test). §1 name/purpose (test G6 refuses to confirm when no independent channel exists; not whether it can confirm). §2 non-design-target at the RECORD level (new constructed record; not CAL-Q/E/D4, not Paper-A sweep, not from the exhausted inventory) WITH the load-bearing caveat: AUDIT-CIRCULARITY is a spec §11 design target and the disposition is known by construction → this is a FAIL-CLOSED DISCIPLINE test, NOT a generalization test; the strong validity test remains unbuilt. §3 the constructed refusal (summary metric looks confirmable — mirroring CAL-Q 0.00 / CAL-E 0.575 — but per-item raw E3 withheld/non-independent; the trap is that summaries can't tell genuine-from-artifact, per the program's own CAL-Q-vs-CAL-E finding). §4 channel analysis (CH1/CH2 both impossible with no raw E3; using labels = E2 circularity per spec K1). §5 expected AUDIT-CIRCULARITY (CONFIRMED would inherit the original read = the forbidden circularity). §6 falsifier (CONFIRMED without a channel = fail-open G6 failure; AUDIT-CIRCULARITY = pass; QUARANTINED/INCONCLUSIVE = case not cleanly isolated). §7 evidence requirements (a real in-scope refusal with labels+summary present; raw E3 + blind channel explicitly absent; absence must be a VERIFIABLE record property, not auditor's-failure-to-look; construction is a separate future authorized step). §8 boundaries; §9 caveat (one failure mode only; not general validity/cert/stress; PASS = fail-closed discipline not generalization). Designs only; constructs/runs/authorizes nothing; reopens no D4; claims no general validity. model-free.*
