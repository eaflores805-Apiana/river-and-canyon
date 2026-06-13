# SHOWN-SEMANTIC-READ-TEMPLATE-v1.0

**Version:** v1.0. River and Canyon program. Standing, model-free template artifact.
**Status:** standing process piece (Block B), adopted lane-local, promotable to `governance/standing/` by earned use. This is a blank form + instructions; it makes no claim and authorizes nothing. Supersedes the practice of borrowing the Hash Integrity v0.7.2 §6 form (the field set is identical; this is the named standing home for it).

## 0. What this template is for

Before a load-bearing artifact is relied on in a model-facing packet, this form must be completed for it. Its single purpose, in plain terms:

> Do not just prove the file exists. **Show that the committed artifact makes the claimed concept true.**

A hash proves bytes. This form proves correspondence between bytes and concept. The two are different, and the gap between them is where Path A occurred.

## 1. The core question

Every completed read answers one question explicitly:

> **Which committed artifact makes the claimed concept true — and does it make only that concept true?**

"Which committed artifact" must resolve to a specific path + commit + sha256. "Makes the claimed concept true" must be shown by exhibiting the artifact's observed structure against the structure the concept requires. "Only that concept" is the surplus check.

## 2. The form (ten fields)

Complete every field. A field left blank is not a PASS; it is at most UNCERTAIN, which for a decision-bearing artifact routes as HOLD (§3).

```text
1. artifact            — the name of the artifact being read
2. path                — repository path
3. commit              — commit at which the artifact is read
4. sha256              — full sha256 of the artifact bytes, recomputed at read time
5. claimed concept     — the concept/contrast/condition/operation the routing
                         packet claims this artifact instantiates, quoted from
                         the packet or the artifact's own declaration
6. check performed     — what was actually inspected to test the claim
                         (fields read, values compared, structure walked) —
                         shown, not asserted
7. observed structure  — what the artifact actually contains, in its own terms
8. required structure  — what the claimed concept REQUIRES the artifact to
                         contain for the claim to be true
9. surplus check       — does the artifact instantiate ONLY the claimed concept,
                         or also an uncontrolled additional concept?
                         allowed values: PRESENT / ABSENT / NOT EVALUATED / N/A
                         · NOT EVALUATED is legal only when surplus is explicitly
                           outside the declared scope of this read
                         · N/A is legal only when the property does not apply to
                           this artifact class (per the property→applicable-class
                           matrix; mark N/A, do not mark missing)
10. disposition        — PASS / HOLD / UNCERTAIN (see §3)
```

The binding comparison is field 7 against field 8: **observed structure must satisfy required structure.** If it does not, the concept is claimed but not instantiated — a SEMANTIC MISMATCH — and the disposition is HOLD.

## 3. Disposition vocabulary

```text
PASS       — observed structure satisfies required structure; surplus check is
             ABSENT (or legally NOT EVALUATED / N/A); the artifact makes the
             claimed concept true and only that concept.
HOLD       — SEMANTIC MISMATCH (field 7 does not satisfy field 8) OR
             SURPLUS SEMANTICS (surplus check PRESENT). The affected readiness
             claim is blocked until corrected, superseded, or explicitly scoped
             out by Manager decision.
UNCERTAIN  — the read could not establish PASS or HOLD (missing field, ambiguous
             structure, unavailable bytes).
```

**For decision-bearing artifacts, UNCERTAIN routes as HOLD.** UNCERTAIN may be recorded as a classification state, but it cannot function as PASS for a readiness claim. (A decision-bearing artifact is one whose output can be mistaken for authorization, evidence, routing status, or acceptance status.)

## 4. Load-bearing artifact note (the default-flip)

Do not assume "configuration" files are inert. The following classes are routinely **instrument-components** — they carry concepts the measurement depends on — and must be read, not waved through:

```text
schedules · manifests · generators · scorer rules · comparison schemas ·
stress specifications · calibration artifacts · templates
```

The Block C audit found every audited Lane 1a′ artifact in these classes classified INSTRUMENT-COMPONENT, zero inert-config. Default each such artifact to INSTRUMENT-COMPONENT and require a read to demote it, not the reverse.

## 5. Language-perimeter guard

Any read or packet citing the program's findings must keep the perimeter clean:

```text
- Path A must be cited as "Path A (rung-uniform)".
- Breadth remains untested under the current sealed schedule;
  the result is a schedule-layer finding.
- Do NOT use phrasings implying: breadth passed · 8/8 survived ·
  replication across rungs · seam evidence · candidate certification ·
  Claim C progress · task family viable.
```

A read whose prose breaches this perimeter is HOLD on the perimeter regardless of its field content.

## 6. No-authorization footer (carried by every completed read)

A PASS on this template means only that artifact/concept correspondence has been shown for the stated claim.

It does not authorize execution, construction, model loading, stress testing, gate opening, certification, candidate selection, threshold work, schedule supersession, or model-facing readiness.

## 7. Worked field-skeleton (blank, for copying)

```text
1. artifact:
2. path:
3. commit:
4. sha256:
5. claimed concept:
6. check performed:
7. observed structure:
8. required structure:
9. surplus check:       PRESENT / ABSENT / NOT EVALUATED / N/A
10. disposition:        PASS / HOLD / UNCERTAIN  (UNCERTAIN → HOLD if decision-bearing)
— no-authorization footer (§6) —
```

## 8. This artifact's own status

This template is a standing form. It authorizes nothing and asserts no finding. It does not authorize: model-facing execution, model loading, sweep_id creation, token-prior generations, constructed-positive generation, seeded-defect exercise, surplus-signature validation, schedule v2 drafting, schedule supersession, true breadth rerun, Path B readiness or execution, Path D execution, quantization stress, INT8/INT4, candidate selection, ranking, threshold work, certification evaluation, Claim C activation, public benchmark packaging, funder-facing release, or SBIR submission.

— Senior Engineer
