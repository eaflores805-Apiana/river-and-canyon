# CONDITIONAL-LIFECYCLE-AUTHORIZATION-PATTERN v0.1

```text
PROCESS ARTIFACT — A PATTERN THE MANAGER MAY GRANT; THIS DOCUMENT GRANTS NOTHING
NEVER AUTHORIZES A SUCCESSOR RUN · NEVER SKIPS VERIFICATION OR FILTER · ANY ABNORMALITY
BREAKS THE CHAIN AND RETURNS TO MANAGER
```

*Owner: New Senior Engineer. Scope: optional per-lifecycle grant collapsing post-run
acceptance round-trips for clean returns only. Drafted at v0.1 for chain review; adoption is a
Manager decision.*

## 1. What the pattern is

At run-authorization time, the Manager may add one clause to the authorization memo:

> *Conditional close-out acceptance granted for this lifecycle: if the post-run chain returns
> clean per §2, the D5-class close-out prepared under CLOSEOUT-TEMPLATE-v1.0 is accepted without
> a further Manager round. Any §3 condition voids this grant for the lifecycle.*

The grant is per-lifecycle, named in the authorization, and recorded as a Manager decision in the
INDEX at grant time. Absent the clause, the full round-trip sequence applies unchanged.

## 2. The clean-return chain (every element required)

```text
C1  NS verification returns VERIFIED under VERIFICATION-PROTOCOL-v1.0
C2  no HOLD occurred anywhere in the lifecycle
C3  no named deviation occurred
C4  no abort occurred
C5  no INCONCLUSIVE result occurred
C6  no criterion firing requires interpretation (criteria firing exactly as
    pre-registered with unambiguous rung-local reading does not by itself break
    the chain ONLY if the Manager's grant explicitly said so; default: any
    firing breaks the chain)
C7  no unauthorized work detected
C8  no claim-language issue appears (C5 seat raises none)
C9  Team Lead filter is PASS without edits
C10 close-out packet conforms to CLOSEOUT-TEMPLATE-v1.0 with no template-exit
    condition met
```

All ten or nothing. The chain is conjunctive; no element substitutes for another.

## 3. Chain-break conditions (any one voids the grant)

HOLD · deviation · abort · INCONCLUSIVE · criterion firing requiring interpretation · artifact
mismatch · path/hash mismatch · unauthorized execution · unexpected output distribution ·
claim-boundary issue · public-facing language issue · sealed-record issue · runner/provenance
issue · TL filter edits · template exit · any seat's stated discomfort. On break: the lifecycle
reverts to the full sequence from the break point; the break and its reason are INDEXed; reverting
is not a sanction — it is the pattern working.

## 4. What the pattern never does

Never authorizes a successor run (conditional sequencing is explicitly not approved — Manager
notice §7). Never pre-accepts a result whose verification has not yet occurred — the grant
pre-accepts the *acceptance step*, contingent on verification actually returning clean; it does
not pre-accept the verification. Never compresses bounded language, never waives C5 review where
C5 review is mandatory, never moves any authority between seats. The Manager may revoke a
standing grant at any time before the chain completes.

## 5. Expected saving, honestly stated

For a clean lifecycle: the post-run sequence collapses from approximately four Manager/TL
round-trips (accept result → direct close-out → review close-out → accept close-out) to one
(filter PASS lands; acceptance is already standing). For any non-clean lifecycle: zero saving by
design — the interesting cases get the full process they deserve.

## 6. Worked check against the record

Applied retroactively (illustration only, no retroactive effect): D4-B would have qualified —
VERIFIED, no HOLD, no deviation, no abort, clean filter — collapsing its post-run arc. D4-A would
NOT have qualified — the TP-banner named deviation breaks at C3 — and would correctly have
received the full sequence it actually got. The pattern's worth lives precisely in that asymmetry.

— New Senior Engineer (to chain review; adoption is the Manager's)
