# Oracle Expected-Verdict Declaration — NS-PROPOSED (for CS co-signature, then lock)

```text
DRAFT / REVIEW ONLY — D2 PHASE 5 PREREQUISITE
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
VERDICTS LOCKED BEFORE PRE-FLIGHT; NEVER DISCOVERED AFTER OBSERVATION
NO MODEL INVOKED · NO SWEEP_ID · NO SWEEP EXECUTION
```

*New Senior Engineer, 2026-06-11. The anti-tuning rule requires every oracle case's expected verdict
declared before pre-flight execution. This is the NS half of the joint declaration (Team Lead update
§11.4); it binds nothing until CS co-signs and the table is hashed into the validation packet.
Verdict vocabulary: **detect** (full instrument must eliminate, with the named primary label) ·
**pass** (full instrument must return NOT_RULED_OUT with no elimination label) ·
**flag-indeterminate** (declared boundary case; proximity flags expected). Where a verdict depends
on a [SWEEP-PARAMETER] bound, the dependency is stated and the verdict finalizes at the same
co-signature that fixes the bound — one lock event, no post-hoc choice.*

| oracle_case_id | oracle_case_type | behavior (synthetic, model-free) | expected_verdict | expected primary label / notes |
|---|---|---|---|---|
| ORC-01 | ideal retriever | gold on every answerable; contract abstention on every NULL; byte-exact format | **pass** | no elimination label; no proximity flag expected; B4 coherence pre-computed (NULL CI [0.806,1.000] above any floor ≤ 0.806) |
| ORC-02 | declared shortcut: pure_last_position | emits last visible pair's value on every item | **detect** | accuracy_indistinguishable_from_declared_policy_envelope (the case is inside the envelope by identity) |
| ORC-03 | declared shortcut: salient_endpoint | emits declared endpoint value | **detect** | envelope label, as ORC-02 |
| ORC-04 | declared shortcut: recency_excluding_target | emits most-recent non-target pair's value | **detect** | envelope label, as ORC-02 |
| ORC-05 | declared shortcut: prefix_neighbor_confusion | emits nearest prefix-neighbor's value (total-function rules) | **detect** | envelope label; no-match items emit declared no-match and score incorrect |
| ORC-06 | token-prior emitter | uniform draw over visible VALUE_POOL on every item | **detect** | accuracy_indistinguishable_from_token_prior (case accuracy ≈ control baseline ≈ 1/26; difference CI upper bound < margin); abstention-floor label also expected to attach (abstains nowhere) — multi-attach permitted, both named here |
| ORC-07 | universal answerer | answers a constant pool value on every item incl. NULL | **detect** | null_abstention_floor_unmet (abstention 0/16, CI ≈ [0, 0.194], upper bound below any floor ≥ 0.20); token-prior label may co-attach depending on constant's gold-coincidence — co-attachment permitted and recorded |
| ORC-08 | universal abstainer | contract abstention on every item incl. answerable | **detect** | answerable_abstention_ceiling_exceeded (abstention 80/80, CI lower ≈ 0.954 above any ceiling ≤ 0.95); headroom label may co-attach |
| ORC-09 | perfect NULL-on-NULL handler | exactly ORC-01 behavior; retained as the named guard for the v1 abstention-band failure | **pass** | the case the v1 instrument eliminated; its survival is the regression test for B3-malformed |
| ORC-10 | malformed-control case (semantic-separation guard) | follows rebinding perfectly: post-scramble-gold behavior presented as candidate | **pass** | must NOT attach accuracy_indistinguishable_from_token_prior (rebinding-following sits far above prior baseline); demonstrates the v1 mislabeling cannot recur; scrambled control remains non-referenced by any label — mechanically checked |
| ORC-11 | mixture oracle, shortcut-heavy | pre-declared blend: 0.75 of answerable items answered by pure_last_position, 0.25 gold; NULL per contract | **detect** | envelope label (blend accuracy dominated by in-envelope behavior); blend fraction 0.75 is itself [SWEEP-PARAMETER], locked with this table |
| ORC-12 | mixture oracle, retrieval-heavy | pre-declared blend: 0.25 shortcut, 0.75 gold; NULL per contract | **flag-indeterminate** | expected NOT_RULED_OUT with boundary_proximity_flag permitted on the envelope criterion (point estimate near margin, interval may straddle); the declared bracket: ORC-11 and ORC-12 sit on opposite sides of the envelope boundary by design |

**Full-instrument requirement (Contributor 6, accepted):** every case runs through the complete
pipeline to a final outcome; the packet records all eight fields per case
(`oracle_case_id … failure_interpretation_if_mismatch`). A mismatch on any case is a validation
failure with C1 disposition — the instrument is not lock-eligible while any expected-verdict row
mismatches unresolved.

**Dependencies to finalize at co-signature (one lock event):** the separation margin, envelope
margin, abstention floor and ceiling values [all SWEEP-PARAMETER]; ORC-06/07/08 verdict arithmetic
above assumes floor ≥ 0.20 and ceiling ≤ 0.95 — both comfortably inside any sane declaration, stated
here so the assumption is auditable rather than silent.

**Non-claim:** these cases validate the instrument on declared behaviors only. Passing the declared
battery does not rule out undeclared shortcuts or partial shortcut contribution; verdict matches are
lock-eligibility evidence, never candidate, capability, certification, or threshold evidence.

— New Senior Engineer (to CS for co-signature; to Team Lead for the lock event with bound values)
