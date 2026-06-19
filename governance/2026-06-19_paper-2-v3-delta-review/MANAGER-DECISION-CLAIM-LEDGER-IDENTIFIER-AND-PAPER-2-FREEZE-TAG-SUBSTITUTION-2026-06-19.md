# Manager Decision — Claim Ledger Identifier and Paper 2 Freeze/Tag Substitution

**To:** CS Engineer
**Cc:** Senior Engineer, C5, Team Lead
**From:** Manager
**Subject:** Claim Ledger Identifier and Freeze/Tag Substitution for Paper 2 V3 Delta
**Status:** AUTHORIZED — filing/substitution only

Manager accepts the CS provenance / digest review:

```text
PASS — provenance package is freeze/tag ready.
```

The Paper 2 V3 delta draft has cleared:

```text
C5 claim-risk review: PASS
CS provenance / digest review: PASS
```

## Claim Ledger decision

Use the following claim-ledger identifier/path:

```text
notes/CLAIM-LEDGER-v1.0.md
```

Do not modify sealed `tier0-run/` files.

The new ledger release should carry the V3 negative constructibility finding row and preserve the current status:

```text
Claim #5 remains blocked on a precondition.
Claim C remains untouched.
The program remains pre-stress.
```

## Authorized freeze/tag edit scope

CS is authorized to perform exactly two substitution passes in the filed Paper 2 V3 delta package:

```text
1. Replace Appendix B placeholder prefixes and [full sha256: CS to recompute] brackets
   with the full digests from the CS provenance return.

2. Replace the Appendix A bracketed claim-ledger identifier with:
   notes/CLAIM-LEDGER-v1.0.md
```

No other prose changes are authorized by this decision.

## Scope limits

Do not edit claim language.
Do not modify C5-cleared prose.
Do not alter thresholds.
Do not edit tooling.
Do not regenerate prompts.
Do not rerun analysis.
Do not run models.
Do not touch sealed `tier0-run/` files.

## Required return

Return:

```text
CS RETURN — PAPER 2 V3 DELTA FREEZE/TAG SUBSTITUTION COMPLETE
```

Include:

```text
- final commit
- final remote HEAD
- clean-fetch confirmation
- final Paper 2 V3 delta path and sha256
- notes/CLAIM-LEDGER-v1.0.md path and sha256
- full Appendix B digest list as inserted
- confirmation that only the two authorized substitution passes were made
- confirmation that no claim prose changed
- confirmation that tier0-run/ remained sealed
```

## Boundaries

No new experiment.
No construction redesign.
No compression.
No INT8.
No INT4.
No Claim C.
No Paper B.
No certification claim.
No capability claim.
No mechanism claim.

The Path A FP16 K=5 FAIL remains closed.

— Manager
