# Senior Intent-Preservation Review — Lane 1a Path A Remediation (958062e)

From: Senior Engineer (outgoing seat; routed per onboarding protocol Senior → Team Lead)
To: Team Lead; Cc: CS Engineer, Manager, New Senior · 2026-06-10
Method: every claim below verified against fetched bytes at `958062e`; hashes recomputed.

## §5.1 — Design-intent preservation: **PASS** (all ten §2 checks)

1. Pre-candidate occupancy/failure-map sweep — intact: task family, ladder L01–L08, N=96 (80/16),
   diagnostic axes, classification labels, plotting restrictions, fixed outcome language all
   untouched by Path A (remediation scope was runner/wrapper/schema/tests/LOCK-RECORD only). PASS.
2. Rule-out-only doctrine — unchanged anywhere in the packet. PASS.
3. The lane-specific runner creates no selection/ranking/threshold/certification/stress surface: it
   is generation + provenance plumbing; schemas still reject rank/preference/best fields;
   `framework_version` still const `"none"`. PASS.
4. Manifest semantics preserved — the runner consumes Lane 1a manifests natively (7 new
   manifest-validation tests: good manifest accepted, malformed rejected). This is *better* than the
   prior plan, under which B1 v2 would have rejected every Lane 1a manifest against the Two-Hop L1
   schema. PASS.
5. No native-B1-execution claim remains; the LOCK-RECORD records the Path A architecture and the
   Manager decision; the design-packet B1-provenance language is recorded as superseded. PASS.
6. B1 v2 unedited — `runner_b1_v2.py` at `958062e` byte-identical to the pre-Path-A ref. The new
   runner imports nothing from the B1 tree (verified against the actual import statements; the
   docstring asserts the same boundary explicitly). It mirrors B1 v2's conventions — same `mlx_lm`
   dependency, same snapshot-hash format, same deterministic decoding defaults — by reimplementation,
   not by import. PASS.
7. B1 v2.1 not created, not used. PASS.
8. Sidecar attestation preserved and correctly renamed: `runner_output_sha256`, `runner_name =
   lane1a_runner.py`; byte-preservation and metadata-separation tests updated and passing;
   `additionalProperties: false` retained. PASS.
9. Planned count 1,536 intact in the LOCK-RECORD (768 candidate + 768 control). PASS.
10. First data access NOT AUTHORIZED and not executed: no audit-log writes; model loading is
    lazy-imported inside the generation path and CS attests no load occurred; preflight gates (lock
    timestamp ordering, no-re-execution) verified present in the wrapper. PASS.

LOCK-RECORD recomputes to `68edbdcd…` full-match. Model identity provenance: per-file sha256 snapshot
hashing mirroring B1 v2's `compute_model_snapshot_hash` — clean.

## §5.2 — Required fixes before combined review: **none blocking.** One one-line note

The LOCK-RECORD references the Path A decision but does not state the root cause inline (B1 v2
validates against the Two-Hop L1 manifest schema). The decision chain records it (Team Lead memo,
Manager selection); a future auditor reading the LOCK-RECORD alone would benefit from the single
sentence. Recommend adding at the next legitimate LOCK-RECORD touch — not worth a re-seal by itself.

## §5.3 — Scientific purpose: **preserved, and strengthened.**

Path A removed a latent falsifier: the prior architecture would have either rejected every manifest
(visible failure) or — worse — consumed them under Two-Hop expectations (silent semantic corruption).
The sweep now runs on a runner that understands its own manifests, with the same provenance
conventions, the same determinism, and the same attestation chain. The β-question this seat required
("state what --context functionally controls") is what surfaced the incompatibility; the escalation
path ("do not code around a functional mismatch") is what routed it to a Manager decision instead of a
workaround. The discipline worked end to end.

## §5.4 — Authorized scope: **unchanged.**

The runner adds execution capability under the same locks, not authority: same planned generations,
same gates, same preflight ordering, same consumption-side restrictions. Nothing Lane 1a may now do
was previously forbidden; nothing previously forbidden is now possible.

## §5.5 — Team Lead may proceed to final combined adversarial review: **yes.**

## §5.6 — First data access: **remains not authorized.** Confirmed in bytes and in posture.

— Senior Engineer
