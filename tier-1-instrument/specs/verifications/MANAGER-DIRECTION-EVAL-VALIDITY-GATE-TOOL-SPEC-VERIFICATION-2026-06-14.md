# Manager Direction — CS Verification of Eval-Validity Gate Tool Spec v0.1

**Received:** 2026-06-14 via session
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — model-free verification requested from CS; no execution authorized.

---

To: CS Engineer
Cc: Senior Engineer, Team Lead
From: Manager
Re: Verification of `EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1.md`
Status: Model-free verification requested; no execution authorized

CS,

Please verify the new Tier 1 tool-spec artifact:

```text
EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1.md
```

This artifact converts Paper A into a reusable protocol / tool architecture. Paper A v1.0 remains the source of truth. If the tool spec and Paper A disagree, Paper A wins.

## Verification purpose

Please verify that the spec faithfully translates Paper A without overstating what has been demonstrated.

The core question:

```text
Does the spec preserve the distinction between:
  implemented / exercised gates
and
  specified but unbuilt gates?
```

## Required checks

Please verify:

```text
1. Paper A remains the source of truth.
2. The spec authorizes no model execution.
3. The spec authorizes no software build.
4. The spec does not reopen D4.
5. The spec does not activate CAL-Q rerun, certification, compression, INT8/INT4 stress, second rung, full ladder, or Claim C.
6. G1–G5 are the only gates marked implemented / exercised.
7. G6–G9 are marked specified but unbuilt.
8. G1–G5 do not claim more than Paper A demonstrated.
9. G6 standing rejection audit is not treated as already built.
10. G7 same-error identity is not treated as already implemented.
11. G8 cross-family / cross-model generality is not treated as demonstrated.
12. G9 full stress-retention pipeline is not treated as executed.
```

## Automated vs. human-read boundary

Please pay special attention to §8.

Verify that the spec keeps this boundary intact:

```text
Automatable:
  counting
  hashing
  threshold comparisons
  strict-vs-concept divergence flagging
  packet assembly
  quarantine bookkeeping

Requires human semantic read:
  construct-validity judgment
  scorer divergence adjudication
  construct declaration
  independent rejection-audit read
```

The most important check:

```text
G4 construct-validity judgment must remain human-semantic-read dependent.
G6 rejection-audit confirmation must require mechanized independence.
```

The spec must not imply that construct validity can be safely automated by pattern matching.

## Mechanized independence check

Please verify that the C6 requirement is preserved:

```text
A rejection audit cannot confirm a refusal by simply rerunning the same read that produced the refusal.
```

The spec should require one of:

```text
blind second reader
pre-registered output-classification schema applied without route knowledge
external ground-truth labels
```

If this is weakened or missing, return HOLD.

## Output schema check

Please verify that the route decisions are correctly defined as:

```text
PASS
NEEDS-REPAIR
QUARANTINE
REFUSE
```

And that no bare score is emitted as the final output.

Also verify that every decision includes an evidence packet:

```text
decision + firing gate
per-item table
pre-declared rule
provenance block
scope stamp
audit result for refusals once G6 exists
```

## Quarantine check

Please verify that quarantine remains distinct from refusal:

```text
QUARANTINE:
  cannot yet adjudicate

REFUSE:
  construct has demonstrably collapsed
```

The spec must not allow quarantined evidence to support claims.

## Claim boundary

Please verify that the spec does not claim:

```text
a finished tool
a validated general method
a product
a market-validated standard
compression fragility
a seam result
cross-family generality
an executed stress-retention pipeline
```

## Return format

Please return one of:

```text
PASS:
  Tool spec faithfully translates Paper A and is safe to route as Tier 1 architecture.

HOLD:
  Specific issue must be fixed before routing.

FAIL:
  Spec materially overstates what Paper A demonstrated or implies unauthorized execution/build.
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

The goal is to turn Paper A into a reusable Tier 1 architecture while preserving Paper A's honesty.

This is the bridge from paper to tool — not the tool itself.

— Manager
