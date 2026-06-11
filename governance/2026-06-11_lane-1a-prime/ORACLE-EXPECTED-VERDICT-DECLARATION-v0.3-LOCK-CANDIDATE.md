# Oracle Expected-Verdict Declaration v0.3 — LOCK CANDIDATE

*v0.3 (lock candidate): applies the Team Lead §4 pre-lock cleanup — HEAD dropped from ORC-08
permitted_co_labels (under corrected HEAD semantics, HEAD is envelope-derived and does not attach to
a candidate-behavior case). Incorporates the co-signed ORC-10 tightened wording. T3 bounds locked
per the co-signed bounds set (FLOOR 0.75, CEIL 0.20, TP 0.10, ENV 0.10, HEAD 0.15, GAP 0.30); blend
values locked at 0.75/0.25 per ORC-11/12. No other change from co-signed v0.2.*

*v0.2 (post Phase 5 run-1 corrective): every case now carries the four label-set fields required by
the Team Lead filter §4 — `expected_outcome · required_labels · permitted_co_labels ·
required_absent_labels` — and a case passes only if outcome AND label-set conditions hold
(verdict-only matching is retired; run-1 is the documented reason). Label abbreviations: TP =
accuracy_indistinguishable_from_token_prior; ENV = accuracy_indistinguishable_from_declared_policy_envelope;
HEAD = insufficient_measurement_headroom; GAP = strict_content_gap_instability; FLOOR =
null_abstention_floor_unmet; CEIL = answerable_abstention_ceiling_exceeded. Verdict expectations are
defined against the FULL six-criterion set only — no expectation is ever defined relative to a
reduced criteria set.*

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

| oracle_case_id | type / behavior | expected_outcome | required_labels | permitted_co_labels | required_absent_labels |
|---|---|---|---|---|---|
| ORC-01 | ideal retriever: gold + contract abstention + byte-exact format | NOT_RULED_OUT | — | — | TP, ENV, HEAD, GAP, FLOOR, CEIL (all six) |
| ORC-02 | pure_last_position emitter | ELIMINATED | ENV | FLOOR, TP | — |
| ORC-03 | salient_endpoint emitter | ELIMINATED | ENV | FLOOR, TP | — |
| ORC-04 | recency_excluding_target emitter | ELIMINATED | ENV | FLOOR, TP | — |
| ORC-05 | prefix_neighbor_confusion emitter (total-function; no-match → declared no-match, incorrect) | ELIMINATED | ENV | FLOOR, TP | — |
| ORC-06 | token-prior emitter: uniform over visible pool | ELIMINATED | TP | FLOOR, ENV | — |
| ORC-07 | universal answerer: constant pool value everywhere incl. NULL | ELIMINATED | FLOOR | TP, ENV | — |
| ORC-08 | universal abstainer: contract abstention everywhere incl. answerable | ELIMINATED | CEIL | TP, ENV | — |
| ORC-09 | perfect NULL-on-NULL handler (v1 abstention-band regression guard) | NOT_RULED_OUT | — | — | all six (as ORC-01) |
| ORC-10 | malformed-control / semantic-separation guard: perfect rebinding-follower as candidate | NOT_RULED_OUT | — | — (boundary_proximity_flags permitted diagnostically; excluded from the match predicate entirely — no proximity flag may appear in any clause, elimination path, K, or fixed language) | **TP (the defining check)** |
| ORC-11 | mixture, shortcut-heavy: 0.75 pure_last_position / 0.25 gold; NULL per contract [blend = SWEEP-PARAMETER] | ELIMINATED | ENV | — | FLOOR, CEIL |
| ORC-12 | mixture, retrieval-heavy: 0.25 shortcut / 0.75 gold; NULL per contract | NOT_RULED_OUT | — | boundary_proximity_flag on ENV criterion expected-permitted | TP, FLOOR, CEIL |

**Full-instrument requirement (Contributor 6, accepted):** every case runs through the complete
pipeline to a final outcome; the packet records all eight fields per case
(`oracle_case_id … failure_interpretation_if_mismatch`). A case passes only if BOTH hold: the full-instrument outcome equals `expected_outcome`, AND every `required_labels` entry attached, no `required_absent_labels` entry attached, and any other attachment is within `permitted_co_labels`. A mismatch on any case is a validation failure with C1 disposition — the instrument is not lock-eligible while any row mismatches unresolved. Pre-flight refuses to run unless this table's co-signed hash and the bounds hash are present in the validation config (PH5-4).

**Dependencies to finalize at co-signature (one lock event):** the separation margin, envelope
margin, abstention floor and ceiling values [all SWEEP-PARAMETER]; ORC-06/07/08 verdict arithmetic
above assumes floor ≥ 0.20 and ceiling ≤ 0.95 — both comfortably inside any sane declaration, stated
here so the assumption is auditable rather than silent.

**Non-claim:** these cases validate the instrument on declared behaviors only. Passing the declared
battery does not rule out undeclared shortcuts or partial shortcut contribution; verdict matches are
lock-eligibility evidence, never candidate, capability, certification, or threshold evidence.

— New Senior Engineer (to CS for co-signature; to Team Lead for the lock event with bound values)
