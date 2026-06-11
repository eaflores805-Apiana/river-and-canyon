# Lane 1a Fixed Outcome Statements (verbatim; byte-locked)
#
# The analyzer emits one of {STATEMENT_A, STATEMENT_B} per the K-rule
# below, then appends STATEMENT_C. No human chooses the sentence;
# `analyzer.py` references these strings exactly.

## Selection rule (locked)

```text
K = | { rung_id in {L01..L08} : labels(rung_id) == ["requires_further_investigation"] } |

if K == 0:
    emit STATEMENT_A
else:
    emit STATEMENT_B with K
always_append STATEMENT_C
```

The condition `labels(rung_id) == ["requires_further_investigation"]`
requires *exact* equality with a single-element list. Multi-attach
labels do not satisfy this; `inconclusive_not_actionable` alone does
not satisfy this. The neutral label is mutually exclusive with all
others by the B2 preempt rule and the requires_further_investigation
attach rule.

## STATEMENT_A (verbatim — emit iff K == 0)

```text
The certification window, while logically nonempty, was unoccupied for this task family at this scale: every rung carried at least one elimination label under the pre-registered sweep classification.
```

## STATEMENT_B (verbatim — emit iff K > 0; substitute the K value)

```text
{K} of 8 rungs were not ruled out under the pre-registered sweep classification and remain an unordered survivor set. Survivorship is neither ranking nor positive evidence; certification eligibility remains undetermined pending separately authorized candidate selection and certification.
```

## STATEMENT_C (verbatim — appended always)

```text
Any construction examined after this sweep is expected to perform worse during fresh certification than during sweep exploration; regression from sweep behavior is not instrument failure and must not be used to tune thresholds.
```

## Implementation note

`analyzer.py` MUST emit byte-for-byte one of these three strings
(STATEMENT_B with `{K}` substituted by the integer value). The unit
test `test_lane1a_packet.py::test_outcome_statement_determinism`
asserts that no other string can be produced under any combination of
inputs to `emit_outcome()`.
