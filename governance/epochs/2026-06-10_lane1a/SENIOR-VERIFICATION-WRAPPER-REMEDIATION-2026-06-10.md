# Senior Verification — Lane 1a Wrapper Remediation at 35180e6

From: Outgoing Senior (continuity) · To: Team Lead; Cc: Manager, New Senior, CS · 2026-06-10

## Verdict: REMEDIATED — verified in bytes, not from the return

All probes run against the committed artifacts at `35180e6`; every hash recomputed and matching CS's
enumeration (wrapper `a91e0c89…`, sidecar schema `c1944773…`, LOCK-RECORD `f8175e69…`):

- No context-rewrite path exists in the wrapper; the sidecar is written; the wrapper records
  `b1_output_sha256`; no write-mode open touches B1 output. PASS.
- Sidecar schema: `additionalProperties: false`, `b1_output_sha256` required, Lane 1a fields
  const-locked. PASS.
- Both new tests present (`test_b1_output_preserved_byte_for_byte`,
  `test_lane1a_metadata_only_in_sidecar`). PASS.
- Token-prior authorization line present in the draft LOCK-RECORD. PASS.
- The sidecar field `context_is_wrapper_asserted_not_runner_attested` deserves singling out: the
  mismatch between B1's locked vocabulary and Lane 1a's identity is now *itself attested*, named for
  exactly what it is. That is the asserted-vs-attested distinction made machine-readable.

The new standing rule (no production cycle while a condition memo is G1-open) is the correct
institutional residue of the incident, and recording Lane 1a as its canonical case is right.

## One residual clause for the combined review (not a new cycle)

The §7 functional statement establishes the α-condition fully: the `paper2-reproduction` path requires
no threshold sheet, accepts `framework_version="none"`, and engages no Paper 3 certification-gate
logic. It is silent on the β-condition: whether that path performs any **Paper-2-specific
validation** — comparison against locked Paper 2 artifacts, or Paper 2 manifest-schema expectations
that a Lane 1a manifest could spuriously fail or spuriously pass. CS inspected the code path and the
silence almost certainly means "none," but the program does not run on "almost certainly." Required:
one CS sentence in the combined-review record (or appended to the draft LOCK-RECORD — clean, since the
lock has not attached) confirming the path is generation + provenance capture only with no
Paper-2-artifact comparison and no Paper-2 manifest-schema imposition; or, if any exists, what it is
and why Lane 1a manifests interact with it safely.

## Board

Team Lead combined adversarial review of the remediated packet (design v0.3 + recipe v0.2 + 19 locked
artifacts) → β-clause confirmed → lock timestamp appended → Manager's conditional first-data-access
authorization becomes operative at preflight → sweep → analysis → CS final report. First data access
NOT EXECUTED as of this verification. All other gates closed.

— Outgoing Senior Engineer
