# Manager Direction — CS Verification of G6 Standing Rejection-Audit Spec

**Received:** 2026-06-14 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — model-free verification requested from CS; no execution or software build authorized.

---

To: CS Engineer
Cc: Senior Engineer, Team Lead
From: Manager
Re: Verification of `G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md`
Status: Model-free verification requested; no execution or software build authorized

CS,

Please verify the new G6 specification:

```text
G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md
```

This artifact specifies the first missing Tier 1 module from the Eval-Validity Gate architecture:

```text
G6 — Standing Rejection Audit
```

Paper A v1.0 and `EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1.md` remain the sources of truth. If the G6 spec disagrees with either, Paper A and the Tool Spec win.

## Verification purpose

The purpose of this verification is to confirm that G6 correctly specifies how the instrument audits its own refusals.

The core question:

```text
When the gate says REFUSE, does the G6 spec define a non-circular way to determine whether that refusal was justified?
```

## Required checks

Please verify:

```text
1. G6 is described as specified, not built.
2. The spec authorizes no model execution.
3. The spec authorizes no software build.
4. The spec does not reopen D4.
5. The spec does not authorize a CAL-Q rerun.
6. The spec does not authorize certification, compression, INT8/INT4 stress, second rung, full ladder, or Claim C.
7. Paper A v1.0 remains the source of truth.
8. Tool Spec v0.1 remains the architecture reference.
9. The spec does not claim the rejection audit has already been exercised as a standing module.
10. The spec does not claim general non-vacuousness beyond the two worked episodes.
```

## Mechanized independence check

This is the load-bearing check.

Please verify that the spec preserves the following rule:

```text
A refusal cannot be independently confirmed by rerunning the same read that produced the refusal.
```

The spec must require at least one mechanized-independent channel before returning full confirmation:

```text
blind second reader
pre-registered output-classification schema applied without route knowledge
external ground-truth labels
```

Please verify that the following are explicitly insufficient:

```text
same reader re-reading with knowledge of prior verdict
same per-item read rerun
post-hoc schema written after seeing outputs
automated proxy that merely repeats the original read's heuristic
```

If this independence requirement is weakened or missing, return HOLD.

## Output-class check

Please verify that G6 defines clear audit outputs, including:

```text
REFUSAL-CONFIRMED
REFUSAL-REVERSED
REFUSAL-QUARANTINED
AUDIT-INCONCLUSIVE
AUDIT-CIRCULARITY
```

The exact names may differ only if the meanings remain clear.

Verify especially:

```text
REFUSAL-CONFIRMED requires an independent channel.
AUDIT-CIRCULARITY is returned when no independent channel is available.
No independent channel means no full confirmation.
```

## Audit-question check

Please verify that the spec carries forward Paper A's four audit questions:

```text
1. Was the refusal correct?
2. Could the refusal be a scoring artifact?
3. Do per-item reads confirm it?
4. Was the rule pre-declared?
```

Also verify that the spec correctly distinguishes:

```text
Q2/Q3:
  can catch aggregate-vs-item disagreement.

Q1 with mechanized independence:
  is required to catch reading-standard miscalibration.
```

## Human semantic-read boundary

Please verify that the spec does not automate construct-validity judgment.

The spec must preserve the boundary:

```text
Mechanized:
  triggering audits
  assembling records
  comparing independent labels
  emitting audit status
  enforcing fail-closed routing

Human semantic-read dependent:
  construct-validity judgment
  designing independent schemas / blind reading protocols
  adjudicating inconclusive cases
```

The spec must not imply that G6 removes human judgment of meaning. It should only mechanize independence and bookkeeping.

## Evidence-packet check

Please verify that the audit record includes:

```text
audit output class
link to the refusal being audited
independence channel used, or explicit no-channel note
answers to Q1–Q4
reversal details if applicable
provenance / hashes
scope stamp
interim-status disclosure where independence is absent
```

## Validation-target check

Please verify that any references to CAL-Q and CAL-E are framed as future validation targets only.

The spec may state:

```text
A future G6 build should reproduce:
  CAL-Q → REFUSAL-CONFIRMED
  CAL-E → REFUSAL-REVERSED
  no independent channel → AUDIT-CIRCULARITY
```

But it must not imply that these validation targets are being run now.

## Scope boundary

Please verify that confirmed refusals remain scoped to their family/model.

The spec must not generalize a confirmed refusal into:

```text
proof the model cannot abstain
proof D4 can never work
proof all absence-defined tasks fail
proof the seam is false
proof compression fragility has been tested
proof the gate works generally
```

## Return format

Please return one of:

```text
PASS:
  G6 spec correctly defines a standing rejection-audit component and is safe to route as the first missing Tier 1 module.

HOLD:
  Specific issue must be fixed before routing.

FAIL:
  Spec materially violates Paper A / Tool Spec boundaries, weakens mechanized independence, or implies unauthorized execution/build.
```

If HOLD or FAIL, include the exact blocker and proposed correction.

## Boundary

Closed:

```text
No model execution.
No new run.
No D4 rescue.
No CAL-Q rerun.
No certification run.
No compression.
No INT8 / INT4 stress.
No second compression rung.
No full ladder.
No Claim C activation.
No public benchmark packaging.
No funder-facing release.
No SBIR submission.
No software build.
```

## Intent

The Eval-Validity Gate must be able to check its own "no."

G6 is the first missing module because trusted refusal is only valuable if refusals themselves can be audited without circularity.

This verification ensures the specification preserves that discipline before routing.

— Manager
