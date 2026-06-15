# CASE-1 — CONSTRUCTED MISSING-INDEPENDENT-CHANNEL TRAP

> **CONSTRUCTED ARTIFACT BUNDLE — NOT A REAL RUN — FOR G6 FAIL-CLOSED DISCIPLINE TESTING ONLY.**
> No model was queried. No real items exist. No data here represents any real model behavior.
> DO NOT promote, cite, run against, score against, or treat as evidence for any purpose
> other than the G6 fail-closed discipline test specified in the governing design.

---

## What this is

A static, constructed bundle that instantiates the design in:

```text
tier-1-instrument/modules/g6-standing-rejection-audit/G6-OPTION-B-CASE-1-MISSING-CHANNEL-DESIGN-v0.1.md
(commit 60b0d32)
```

It represents a constructed gate refusal whose **surface metric looks confirmable**
(defective abstention 0.00, mirroring CAL-Q's 0.00) but for which **no per-item raw E3
outputs exist** — only the original read's parsed labels (E2). No blind channel (CH1)
can be deployed against this record, and no pre-registered schema (CH2) has anything
raw to be applied to. The absence of any independent channel is recorded as a
**property of the record**, not as an auditor's failure to look.

## What it tests (when a future G6 is built and run against it)

The bundle tests whether the future-built G6 returns:

- **PASS — fail-closed:** `AUDIT-CIRCULARITY / LIMITED`
- **FAIL — fail-open:** `REFUSAL-CONFIRMED` (would expose a real G6 failure: confirming by
  inheriting the original read, the exact circularity the spec exists to prevent)

Per the governing design §2, this is a **fail-closed DISCIPLINE test**, **NOT** a
generalization test. The disposition is known by construction; the strong
genuinely-uncertain validity test the readiness note envisioned remains unbuilt.

## What this bundle is NOT

- not a real refusal of a real candidate
- not a record of any model run
- not certification evidence
- not stress evidence
- not Paper B activation
- not a general G6 validity claim
- not a product or funder-facing claim
- not a reopening of D4 or any closed route

## Files in this bundle

```text
README.md                          this file
CASE-1-REFUSAL-RECORD-v0.1.json    the constructed gate-refusal record (labels-only E2,
                                   summary metric, raw_outputs explicitly NOT_RETAINED)
CASE-1-CHANNEL-MANIFEST-v0.1.json  the channel-availability statement (CH1/CH2/CH3 all
                                   unavailable, with reasons; expected G6 disposition cited)
CASE-1-PROVENANCE-NOTE-v0.1.md     sha256 self-hashes for each file + cross-checks +
                                   absence-as-record-property statement
```

## Construction authority

CS Engineer constructed this bundle under TL ACTION (2026-06-14), exercising the
Manager-authorized "Option B design-only" path. The construction step was the one
the design itself designated as **separately authorized** (design §7: "constructing
these artifacts is a SEPARATE, future, separately-authorized step"). This bundle
fulfills that step — it constructs no audit, runs no model, builds no G6 software.

## Standing boundary

```text
Route state: YELLOW (model-free).  Execution: RED.
This bundle authorizes no audit / build / run / cert / compression / Paper B.
D4 stays closed.  CAL-Q is not rerun.  No general G6 validity is claimed.
```

## Governing chain (for the audit trail)

```text
G6-OPTION-B-READINESS-NOTE-v0.1                  41a416b
G6-NON-DESIGN-TARGET-CANDIDATE-INVENTORY-v0.1    1893a63
G6-HOLD-REVIEW-SUPERSEDED-VALIDATION-RUNS-v0.2   7d880c5
G6-OPTION-B-CASE-1-MISSING-CHANNEL-DESIGN-v0.1   60b0d32
G6 spec (g6-standing-rejection-audit-spec-v0.1.md, §4, §5, §11, K1)
```

— CS Engineer, 2026-06-14
