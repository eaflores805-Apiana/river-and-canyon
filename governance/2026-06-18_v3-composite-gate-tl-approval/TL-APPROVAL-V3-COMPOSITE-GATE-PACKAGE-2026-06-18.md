# TL Approval — V3 Composite Gate Package

**To:** CS Engineer, Senior Engineer, C5
**From:** Team Lead
**Subject:** TL Approval of V3 Composite Gate Package
**Status:** TL APPROVED — pending Manager by-name run authorization

Team Lead approves the V3 Composite Gate package for Manager authorization consideration.

## Approved preregistration

```text
PREREGISTRATION — V3 COMPOSITE GATE (Path A) v0.2
sha256: df26dc65ac3dd76bb09fa84c4688b8835f49282e2a8f77ea4b94991308e57275
```

## Review status

```text
C5 claim-risk: PASS
CS feasibility: PASS
SE tooling verification: PASS
CS final feasibility: PASS
```

## Locked tooling digests

New tooling:

```text
v3_composite_gate_item_generator.py
sha256: cc07e5a2c49757e9171831af7944b5f7f8b1de235c7cb35cb18e48b06ce534a2

v3_composite_gate_analyzer.py
sha256: 3a3e954e1988ec3331d3e405bf2cbd90eae11d132d6ae9276cba10e1ca7e7c5f

v3_composite_error_logger.py
sha256: 2ed466281c949ca3a47843934c031b87e4d016b15d6d1db0ac83db6d4687c226
```

Reused unchanged:

```text
v3_item_generator.py
sha256: 6a2ceee15442ebbd1f6cc4bbbd14a76d1264af9904ad3e5d6062c1554f530c53

v3_prompt_realizer.py
sha256: fb561fdc526115da94c6137b739e8bb3b6adf30825d83f864cda713bc0750909

v3_prompt_conformance_checker.py
sha256: b8afa3f89dd7f375058500820bdf2bf58a46384d2283c8f2a31f1b8c92ad2b82

v3_neutral_token_pool.md
sha256: bc2020c2c4e1293f62c9f83a9b24a61f98c1ede35d5a071ee8cfd72a316ab0d9

inspector.py
sha256: cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9

constants.py
sha256: 1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd
```

## Binding caveat

`MAX_DELTA = 8` is approved only under the current scheme:

```text
current token-width scheme
current Manager-locked values
current relation-naming scheme
fresh composite-gate seed range 097..192
```

Any change to token width, seed range beyond the 3-digit constraint, construction shape, relation naming, or Manager-locked values reopens prompt-length conformance.

## Approved interpretation boundary

A successful run may yield only:

```text
GATE-CLEARED-THIS-RUN
```

and the allowed interpretation is:

```text
the V3 composite baseline shows behavior consistent with two-hop composition under foreclose-all controls on this run
```

It is not final certification.

It is not:

```text
the model composes
general two-hop capability
mechanism evidence
seam evidence
compression readiness
Claim C
Paper B
```

## Next gate

This TL approval does **not** authorize execution.

The next gate is separate Manager by-name authorization for the fresh V3 Composite Gate run:

```text
fresh seed range: 097..192
N = 96
FP16 only
Qwen2.5-3B-Instruct
greedy decoding
```

## Boundaries

No run begins without Manager authorization.
No compression.
No INT8.
No INT4.
No Claim C.
No Paper B.
No final certification claim.
No capability claim.
No mechanism claim.

The Path A FP16 K=5 FAIL remains closed.

**Signed,**
Team Lead
