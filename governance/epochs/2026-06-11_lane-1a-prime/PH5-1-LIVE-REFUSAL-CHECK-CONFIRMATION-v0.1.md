# PH5-1 Live Refusal-Check Confirmation (v0.1)

```text
SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
PH5-1 FINAL PRE-RUN GATE — LIVE-CHECK ARTIFACT
NO MODEL INVOKED · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
NO CORRECTIVE RUN-3 EXECUTION · LOCK-RECORD PENDING
```

To: Team Lead · Cc: New Senior Engineer, Senior Engineer, Manager
From: CS Engineer · 2026-06-11
Re: TL §6 final pre-run gate — live exercise of the PH5-4 refusal machinery

CS exercised `verify_pre_flight_config` against the three required
failure modes in a single Python invocation. The pre-flight refusal
machinery is live: it refuses on the two negative modes, passes on the
positive mode, and the script halted immediately after the positive
mode without invoking `run_full_instrument_oracle_validation` or any
downstream validation step. Corrective run-3 was not executed.

---

## §1. Commit SHA

```text
HEAD: 5a12ee83ad60145ca8181ee1e00530dba5c5cdc6
short: 5a12ee8
```

This is the PH5-1 PASS state per Team Lead disposition (this memo
introduces no further commits prior to the live check; an optional
follow-up commit may file this confirmation memo itself).

## §2. Test commands / invocation description

A single Python `python3` invocation (no pytest harness) exercised
three independent calls to `verify_pre_flight_config` against
distinct `ValidationPreFlightConfig` instances. The script imported
only `lane1a_prime.analysis.{ValidationPreFlightConfig,
ValidationPreFlightRefused, verify_pre_flight_config}` — no validation,
oracle, manifest, policy, scoring, A6, or reporting module was loaded.
No model module was imported. No filesystem write.

```python
from lane1a_prime.analysis import (
    ValidationPreFlightConfig,
    ValidationPreFlightRefused,
    verify_pre_flight_config,
)

# Locked artifacts (committed at HEAD = 5a12ee8):
LOCKED_ORACLE = repo / "validation" / "ORACLE_VERDICT_TABLE.json"
LOCKED_BOUNDS = repo / "validation" / "T3_BOUNDS_DECLARATION.json"
LOCKED_RECIPE = repo / "validation" / "STRATIFIED_RECIPE_SCHEDULE.json"
ORACLE_HASH = "9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5"
BOUNDS_HASH = "45565d0b46c05da4f7d5c13956ac3a6331cc0748dfba4546f8f1d6cc46addd39"
RECIPE_HASH = "7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5"

# Check 1: missing required artifact (oracle path → non-existent)
# Check 2: mismatched hash (oracle hash → 64 zeros)
# Check 3: all three correct → silent return; script halts immediately
```

After Check 3 returned, the script printed a `HALT:` line and
terminated. No code path downstream of `verify_pre_flight_config` was
taken.

## §3. Missing-hash refusal result

```text
=== Check 1: missing required artifact ===
REFUSED: PH5-4 refusal: required lock-event artifact missing: oracle
verdict table at /tmp/__does_not_exist_ovt.json
```

Exception type: `lane1a_prime.analysis.ValidationPreFlightRefused`.
Raised from `verify_pre_flight_config` before any sha256 computation
on the present artifacts.

**Result:** REFUSED as required.

## §4. Mismatched-hash refusal result

```text
=== Check 2: mismatched hash ===
REFUSED: PH5-4 refusal: oracle verdict table hash mismatch: declared
0000000000000000000000000000000000000000000000000000000000000000;
actual on disk 9c6cbda9eb5b6e850b88451529bb989dee6355ce145c31d1fca5d7b0f3a7fba5
```

Exception type: `lane1a_prime.analysis.ValidationPreFlightRefused`.
Raised after computing the on-disk sha256 of the present oracle verdict
table and detecting the declared-vs-actual mismatch. The error message
includes both hashes for audit reconstructibility.

**Result:** REFUSED as required.

## §5. All-correct-hashes pre-flight result

```text
=== Check 3: all-correct hashes ===
PASSED: verify_pre_flight_config returned silently
HALT: not invoking run_full_instrument_oracle_validation; not constructing manifests;
      not running policy battery; not running A6; not running oracle validation;
      not assembling reports; corrective run-3 NOT executed.
```

`verify_pre_flight_config` returned `None`; no exception. The three
on-disk sha256s matched the three declared hashes:

| artifact | declared | on-disk | match |
|---|---|---|---|
| oracle verdict table | `9c6cbda9…` | `9c6cbda9…` | ✓ |
| T3 bounds declaration | `45565d0b…` | `45565d0b…` | ✓ |
| stratified recipe schedule | `7ad3ccdd…` | `7ad3ccdd…` | ✓ |

The script then halted at the point immediately after pre-flight return
and before any model-free validation execution. No
`construct_pilot_manifests`, `apply_policy_battery`, `compute_union_envelope`,
`a6_final_manifest_reverification`, `run_full_instrument_oracle_validation`,
`populate_t1_report`, `populate_t3_report`, `populate_t4_report`,
`assemble_instrument_validation_report`, or `emit_execution_ledger`
call was made.

**Result:** PASSED to the point immediately before model-free validation
execution, as TL §6 step 6 requires.

## §6. Confirmation: corrective run-3 did not execute

**CONFIRMED.** No manifest was constructed. No policy battery executed.
No A6 check ran. No oracle case ran. No T1, T3, T4 report, IVR, or
execution ledger was written. No file under
`experiments/2026-06-11_lane-1a-prime/validation/` was created or
modified by this exercise. The script wrote zero files; it produced
stdout only.

## §7. Confirmation: no model invoked

**CONFIRMED.** No model invocation occurred. The only imports were
`ValidationPreFlightConfig`, `ValidationPreFlightRefused`, and
`verify_pre_flight_config` from `lane1a_prime.analysis`. No
`mlx_lm`, no `from_pretrained`, no `load_model`, no inference call,
and no model-bearing module path was touched.

## §8. Confirmation: no model loaded

**CONFIRMED.** No model file or weights were loaded. The
analysis module path imported is entirely model-free
(source-level guarantee at `lane1a_prime.analysis` sha256
`3f83ac57d59f30818d12888ce0d364c78d3226475ab1ca4dd098c0cc99c55969`;
test coverage `test_validation_source_no_model_imports` and
`test_oracle_cases_source_no_model_imports`).

## §9. Confirmation: no sweep_id created

**CONFIRMED.** No sweep configuration generated, referenced, or stored.
No identifier of any kind was emitted.

## §10. Confirmation: no sweep execution

**CONFIRMED.** No batched or distributed candidate generation initiated.
The validation harness has not been re-executed since the run-2
supersession. The corrective run-3 remains gated behind Team Lead
acknowledgement of this live refusal-check confirmation per TL §7.

## §11. Confirmation: LOCK-RECORD remains PENDING

**CONFIRMED.** LOCK-RECORD remains PENDING. The PH5-1 joint lock-event
record v0.2 has Team Lead PASS (TL §10); the live refusal-check
machinery is now confirmed live; corrective run-3 is conditionally
authorized after Team Lead acknowledgement of this memo per TL §7.

Until acknowledgement, no run-3 execution. All downstream gates remain
CLOSED: D3 acceptance; D4 sweep authorization; D5 close-out; model
runs; model loading; new sweep_id; sweep execution; token-prior model
generations; scrambled-binding model generations; candidate/model
outputs; candidate selection; ranking; threshold work; certification
evaluation; stress-retention testing; Claim C activation; public
benchmark packaging.

---

## Appendix — Reproducibility note

The live check was a single deterministic Python invocation that read
the three lock-event artifacts at the paths declared in the joint
record. Any auditor at HEAD = `5a12ee8` may reproduce the three
results by running an equivalent script; the three on-disk sha256s
match the declared hashes byte-for-byte, the two negative paths raise
`ValidationPreFlightRefused`, and the positive path returns silently.

— CS Engineer, 2026-06-11
