# TL Approval — Hop1 Stability Investigation Package

**To:** CS Engineer, Senior Engineer, C5
**From:** Team Lead
**Subject:** TL Approval of Hop1 Stability Investigation Package
**Status:** TL APPROVED — pending Manager by-name run authorization

Team Lead approves the Hop1 Stability Investigation package for Manager authorization consideration.

## Approved preregistration

```text
PREREGISTRATION — HOP1 STABILITY INVESTIGATION (Path A) v0.1
sha256: 71f00482e1d94bd7fb06a5068391a7977a4b71d9baac690b286511d29e052c26
```

## Review status

```text
C5 claim-risk: PASS
CS feasibility: PASS
CS tooling build: PASS
SE tooling verification: PASS
CS final feasibility: PASS
```

## Locked tooling digests

```text
v3_hop1_stability_analyzer.py
sha256: 31224f6fe7b66d303924a40fa9307f3aded05f8ba73d4952f518c8deecd69f0f

v3_hop1_covariate_logger.py
sha256: b9532490f49970396cd9a14d926393450ede2e6a17c5374b2ac69d115f39953f
```

Reused tooling remains unchanged and locked as previously verified.

## Approved run design

The approved investigation is:

```text
6 fresh blocks × N=96
seeds 193..768
hop1 + hop2-control contexts only
FP16
greedy decoding
Qwen2.5-3B-Instruct
```

Fresh blocks:

```text
F1: 193..288
F2: 289..384
F3: 385..480
F4: 481..576
F5: 577..672
F6: 673..768
```

## Approved interpretation boundary

This study may report only:

```text
cross-block hop1 materialization-admissibility
```

It may not report:

```text
model stability
general hop1 capability
mechanism
binding / attention / reasoning failure
composite-gate result
certification
compression readiness
Claim C
Paper B
```

The P-role covariate is a fresh-tested co-occurrence hypothesis only. Secondary covariates are exploratory/descriptive only.

## Branch priority

The analyzer priority is approved as:

```text
1. CONSTRUCT-FAIL
2. HOP2-CONTROL-FAIL
3. HOP1-STABLE-ADMISSIBLE / HOP1-STABLE-INADMISSIBLE / HOP1-UNSTABLE
```

## Next gate

This TL approval does **not** authorize execution.

The next gate is separate Manager by-name authorization for the Hop1 Stability Investigation run.

## Boundaries

No run begins without Manager authorization.
No composite-gate retry.
No compression.
No INT8.
No INT4.
No Claim C.
No Paper B.
No certification claim.
No capability claim.
No mechanism claim.

The Path A FP16 K=5 FAIL remains closed.

**Signed,**
Team Lead
