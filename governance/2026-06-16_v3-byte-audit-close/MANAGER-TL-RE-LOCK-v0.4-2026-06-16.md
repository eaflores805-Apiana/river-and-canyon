# Re-Lock Record — PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4

**To:** Senior Engineer, CS Engineer
**From:** Manager / Team Lead
**Subject:** Re-Lock of Corrected V3 Instrument Byte Binding
**Status:** RE-LOCKED OF RECORD
**Date:** June 16, 2026

Manager and Team Lead re-lock the corrected V3 preregistration binding:

```text
PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4
```

as the of-record successor to:

```text
PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3
sha256: d9bd9b219badd25901811ddfbb43b811a04750a77723f6a1f076c7dd641f091c
```

## Scope of re-lock

This re-lock applies only to the instrument byte-binding block.

The v0.4 binding patch re-pins:

```text
inspector.py:
  be50c08c… -> cb4b0b60bd6dc2b5…

constants.py:
  614d185d… -> 1d761c3d1c56e7ac…
```

Reason:

```text
Shared inspector.py / constants.py were patched additively for K-sweep sweep-mode.
Senior verified the V3 REAL-RUN path remains preserved.
CS confirmed this with a real-run parameter-deviation fixture PASS.
```

## Attestation

This re-lock changes no scientific content.

No values changed.
No thresholds changed.
No outcome rules changed.
No scoring categories changed.
No controls changed.
No stop-rules changed.
No forbidden interpretations changed.

The patch corrects stale byte bindings only.

## Boundaries

This re-lock does not authorize a build.
This re-lock does not authorize item generation.
This re-lock does not authorize prompt generation.
This re-lock does not authorize a model run.
This re-lock does not authorize compression.
This re-lock does not open Claim C.
This re-lock does not open Paper B.
This re-lock does not make a capability claim or mechanism claim.

The Path A FP16 K=5 FAIL remains closed and untouched.

## Route unlock

With v0.4 re-locked of-record, Senior is now cleared to draft the philosophy decision record:

```text
foreclose-all as the gate standard
V3 as the candidate vehicle
route: audit → build → floor-check
```

The philosophy record remains a decision artifact only. It will not authorize build or run by itself.

**Signed,**
Manager
Team Lead
