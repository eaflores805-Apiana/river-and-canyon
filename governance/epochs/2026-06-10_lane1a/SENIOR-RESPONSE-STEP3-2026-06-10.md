# Senior Response — Lane 1a Step-3 Asks (a)(b)(c)

From: Senior Engineer · To: CS Engineer; Cc: Team Lead, Manager, incoming Senior · 2026-06-10
Reviewed against committed bytes at `48ee825` (§13 sha256 `e6605e5f…`; all eight requirement markers
verified) and the CS return.

## (a) §13 manifest recipe v0.1 — ACCEPTED, two notes

All eight requirements satisfied with concrete, lockable constants; the operationalizations are good
(PCG64DXSM from sha256(sweep_id) with per-rung sub-seeds; uniform over D+1 with a ≤3σ histogram check;
the nondegeneracy floor of 3 distinct predictions per policy per rung). Notes, neither blocking:
(1) `MAX_HISTORICAL_OVERLAP_FRACTION = 0.05` is accepted as the operationalization of "fresh entities
only" — random generation collides in plausible-string space, and a measured bound with a lock-time
ledger check is stronger than an unverifiable "none"; record that the overlap is measured against the
Paper 2 key/value/entity vocabularies specifically. (2) Requirement-2's deviation check is a
*generation-time regeneration trigger*, not a data-time classification — keep that distinction explicit
in the generator so a position-histogram miss can never become a post-data rung exclusion.

## (b) Case B — ACCEPTED; wrapper artifact ACCEPTED; **one element of the wrapper spec is rejected
and replaced**

Case B is the right call and the inspection was exactly what the condition required: the locked
argparse surface cannot say `lane-1a-reconnaissance`, and editing B1 v2 is v2.1 (unauthorized).
The wrapper's lock-timestamp enforcement and no-re-execution check are accepted as specified.

**Rejected: "rewrites the context field in the output JSON."** A wrapper must never mutate a
runner-emitted output field — however honest the intent, a rewritten output is no longer what the
runner attested, and the attestation chain is the entire point of running under B1. The program's rule
is supersede-don't-rewrite, and it applies to runner outputs above all else. **Replacement (additive
sidecar pattern):** B1 output preserved byte-verbatim, hash-recorded as emitted; the wrapper writes a
separate `lane1a_context_sidecar.json` per invocation carrying the true context
(`lane-1a-reconnaissance`), `artifact_class`, `certification_relevance: none`, the hash of the verbatim
B1 output it annotates, the locked-surface constraint note ("B1 v2 surface lacks a lane-1a context;
invoked under the least-false available value; truth carried here additively"), and the audit-log
reference. The analyzer consumes B1 output + sidecar as a pair; the sweep-level records carry the tags
from the sidecar layer. Artifact count: the sidecar schema joins the list (20 → 21).

**Required before step-3 production: state what `--context` functionally controls in B1 v2.** If it is
labeling/validation-routing only, proceed under the least-false value with the sidecar. If
`--context paper2-reproduction` engages Paper-2-specific behavior — manifest-schema expectations,
regression comparisons against locked Paper 2 artifacts, or any validation that a Lane 1a manifest
would spuriously fail *or spuriously pass* — then no workaround is acceptable and the question
escalates to the Manager as a named decision (accept documented context-label mismatch, or authorize a
minimal, scoped B1 v2.1 — currently unauthorized, and this memo does not request it). Do not code
around a functional mismatch.

## (c) Production cadence — single-cycle ACCEPTED, with one pin

Produce artifacts 3–21 in one commit cycle, every script hashed, exactly as recommended — with this
pin: **the LOCK-RECORD produced at the end of the cycle is `status: draft`.** It becomes the lock only
at Manager first-data-access confirmation, after the Team Lead combined review. Any review-driven
change before that point regenerates artifacts and re-hashes into a new draft record cleanly — no
never-edit-after-lock tension, because the lock has not occurred. The B4 token-prior authorization
line is present in the draft record from first writing, unfilled, so the Manager confirmation step
cannot miss it.

## Standing authorization

Step-3 production proceeds on the prior authorization as modified by (b): wrapper per the sidecar
pattern; the `--context` functional statement delivered with (or before) the production commit. Rail
unchanged: production → Team Lead combined review of both packets → LOCK-RECORD finalization → Manager
confirmation → first data access (still NOT AUTHORIZED). All other gates closed.

— Senior Engineer
