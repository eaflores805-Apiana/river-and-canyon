# Manager Authorization — Run Off-Ceiling Calibration Sweep

**Received:** 2026-06-13 via session (TL forwarded Manager memo)
**Filed by:** CS Engineer (verbatim Manager bytes recorded for the project record)
**Status:** RECEIVED — narrow model-facing calibration sweep authorized
**Submap:** Certification-Readiness, Stage 3 (sweep execution)

---

To: CS Engineer, Senior Engineer
Cc: Team Lead
From: Manager
Re: Off-ceiling calibration sweep
Status: Narrow model-facing calibration sweep authorized

Team,

I approve the next step:

```text
OFF-CEILING CALIBRATION SWEEP
```

This approval is narrow.

## Authorized scope

Run the calibration sweep specified in:

```text
OFF-CEILING-CALIBRATION-SWEEP-SPEC-v0.1.md
```

Authorized candidates:

```text
CAL-A
CAL-B
CAL-C
```

CAL-D is authorized **only if** the single-difference check passes. If CAL-D introduces a second difference or confound, drop it.

## Purpose

The only question this run is allowed to answer is:

```text
Does a D4-family construct land inside the off-ceiling certification band?
```

Target band:

```text
0.6125 + margin < clean accuracy < 1.0 − delta
```

The sweep should determine whether the band is:

```text
BAND PLAUSIBLE
BAND TOO NARROW
INSUFFICIENT / NEEDS REPAIR
```

## What this does not authorize

This does **not** authorize:

```text
certification run
compression
INT8 / INT4 stress
second compression rung
candidate certification
ranking
Claim C activation
public benchmark packaging
funder-facing release
SBIR submission
```

## Required CS controls

Before execution, CS must confirm:

```text
current HEAD
spec path
spec sha256
candidate matrix
prompt/template hashes
scorer hash
manifest hash
single-difference status for each candidate
route-state declaration
closed-gate list preserved
```

## Required output

Return a compact run report with:

```text
candidate ID
clean accuracy
defective accuracy, if applicable
shortcut-floor comparison
ceiling comparison
band verdict
raw output path
manifest path
scorer path
sha256s
notes / blockers
```

## Required interpretation

Do not interpret this as certification.

Do not interpret this as compression evidence.

Do not interpret this as Claim C evidence.

This is only a calibration sweep to decide whether a later certification-run request is well-formed.

## Decision rule

```text
If at least one clean candidate lands below ceiling and above shortcut floor + margin:
  BAND PLAUSIBLE

If every candidate that escapes ceiling collapses to or below shortcut floor + margin:
  BAND TOO NARROW

If artifacts, matching, or single-difference checks fail:
  INSUFFICIENT / NEEDS REPAIR
```

## After run

Senior interprets the run against the pre-declared decision rule.

Team Lead prepares the Manager decision surface.

Manager decides whether to authorize a later certification-run request.

— Manager
