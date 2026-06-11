# Lane 1a Lock Record — 2026-06-10 (Remediated: Sidecar Attestation Pattern)

Sweep ID: `lane-1a-2026-06-10`
Framework version (declared): `none`  *(Lane 1a is NOT a certification)*
Doctrine: *Lane 1a may rule out; Lane 1a may not rule in.*
Artifact class: `lane-1a-reconnaissance`
Certification relevance: `none`

Source design packet: `governance/2026-06-10_lane1a/DESIGN-PACKET-v0.3.md`
  sha256 `f1280a8563bbb48c5592c35c809be6c739859234cbf33b64a3786c6e5df67bab`

Source §13 normative manifest recipe: `governance/2026-06-10_lane1a/EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.2.md`

Senior remediation finding: `governance/2026-06-10_lane1a/SENIOR-FINDING-WRAPPER-REWRITE-2026-06-10.md`

Manager authorization memos:
  - `governance/2026-06-10_lane-1a-authorization/MANAGER-AUTHORIZATION.md` (lane opened)
  - `governance/2026-06-10_lane1a/MANAGER-DIRECTION-v0.3-OPTION-A-2026-06-10.md` (v0.3 + Option A)
  - `governance/2026-06-10_lane1a/MANAGER-AUTHORIZATION-FIRST-DATA-ACCESS-2026-06-10.md` (first data access, conditional)

## B4 — Token-prior control authorization (Manager 2026-06-10)

```text
Token-prior control authorization: Manager-authorized Lane 1a token-prior control path
```

## Generation plan (per Manager Option A)

```text
planned_generation_count = 1536
candidate_generation_count = 768
control_generation_count = 768
control_scoring_denominator = 80 answerable-mirroring controls per rung
NULL-mirroring controls = descriptive-only
```

## --context functional statement (Senior remediation §7)

The wrapper passes `--context paper2-reproduction` to B1 v2 because:

```text
B1 v2's locked argparse surface (merge 3cbfce57) accepts only
{paper2-reproduction, paper3-certification} as values for --context;
B1 v2 source must not be edited (B1 v2.1 is unauthorized).
```

Functionally, `--context paper2-reproduction` selects B1 v2's
post-generation code path that:

```text
- requires no threshold sheet;
- accepts framework_version="none";
- engages no Paper 3 certification-gate logic.
```

Lane 1a semantics are NOT carried by the B1 `context` field. The B1
output bytes are preserved unchanged by the wrapper. Lane 1a metadata
(artifact_class, certification_relevance, lane_1a_context,
context_is_wrapper_asserted_not_runner_attested,
context_functional_statement) lives only in a sidecar JSON written
alongside each B1 output. The sidecar records the B1 output's sha256
so an auditor can verify byte-for-byte preservation.

This is the sidecar-attestation pattern. The earlier rewrite pattern
(committed at `25613d3`) is superseded by this LOCK-RECORD; the
wrapper code is corrected; new unit tests prove byte preservation and
sidecar-only Lane 1a metadata; the sidecar schema is locked.

## Locked artifact hashes (post-remediation)

| Artifact | sha256 | Status |
|---|---|---|
| `classification_criteria.yaml` | `9b32fa1e84529efe078590e1ab9e448a246077fa85cb1492e88dad21eed09b93` | unchanged |
| `manifest_generator.py` | `e2962139c2cd520e7e5c979830333e91523cdff3b196e1f475f31557f19c3d38` | unchanged |
| `prompt_template.md` | `1fa889ae8fede10d8b539a8f8672d4e68eedf67f8d0ce3592bbe9eb910df7cd1` | unchanged |
| `scorer.py` | `c1aff994081829a6888338aea8dadab30bf622203dbb5f597cd7298cf8f27495` | unchanged |
| `dummy_policies.py` | `46a5b2349051b4e51059575d056068360fe990889c57cb11a4ba155afe9ad36c` | unchanged |
| `runner_config.yaml` | `49401bf572d0491ab9f771fa3cce92edff6bd112c905f71372ca12eea4ca3bcc` | unchanged |
| `lane1a_runner_wrapper.py` | `a91e0c89be9e4a7d330be0c4dab6b4c25541d5e97112832653b04b576fc95dc3` | **REMEDIATED — sidecar pattern** |
| `analyzer.py` | `4c0087fa949883a772f608994f439132a195583a97035b7baff700230ba2144c` | unchanged |
| `plotter.py` | `dca510667d52d1b5a281f4a5ca5597c2abb5a7cb4a1a25a59baa98e397a5834a` | unchanged |
| `artifact_tags.py` | `bb5d396eeee45d0e08ae987d487ea57579e12bf87efc2fe4e76896b505290f2f` | unchanged |
| `audit_log.py` | `1c6578040dc3335b536453731c4cd0eb412ebea582c2eea38f3c6b39e57a90ed` | unchanged |
| `fixed_outcome.md` | `bde3c8043dc058c7f357921bbc8623acecf8077922cd620e7a1b2220f1ef3217` | unchanged |
| `exclusion_block.md` | `feb4b80cbc4b95be838fc39321086749c457ce3bfa745f0c57658ea5749318ce` | unchanged |
| `schema/per_rung_record.schema.json` | `beb48aacf384cee21c29265802d320292544875e342e26cc3b1ef4b7959ae14c` | unchanged |
| `schema/sweep_record.schema.json` | `449aae9259ed9fe2f188818ae880c691f419e0b62b302e40fffb1e99cea678ec` | unchanged |
| `schema/lane1a_sidecar.schema.json` | `c1944773a5c686586bb39e553e803b6e2e66278ccbd7047e9000027e0a0502e1` | **NEW** |
| `AUDIT-LOG-FORMAT.md` | `29b418c6cb6601d1aab4b28eba8e538ef828900eef6a02a9d821b128abc6a465` | unchanged |
| `test_lane1a_packet.py` | `2697d69e2040722472d5cfb70df3042f67690164456c11b5b0c726fdfc73fa60` | **REMEDIATED — 3 new sidecar tests** |
| `NOVELTY-LEDGER.md` | `aad806a47bea04d7b16b77a0c1205a472b97ecbf7b5591b2a77b71f8ccb9f112` | unchanged |

Total locked artifacts: 19 (was 18; sidecar schema is the +1).

## Lock timestamp

```text
Lock timestamp: 2026-06-11T02:06:36Z
```

Team Lead appended this RFC 3339 UTC timestamp upon completion of the
combined adversarial review (PASS) of design packet v0.3 + this
remediated execution packet, filed at
`governance/2026-06-10_lane1a/TEAMLEAD-COMBINED-REVIEW-PASS-2026-06-10.md`.

The `first_data_access_timestamp` recorded by the wrapper at sweep
time MUST postdate this lock timestamp. `lane1a_runner_wrapper.py
preflight()` enforces this comparison.

**First data access remains NOT AUTHORIZED until Manager reauthorizes
against the remediated packet (Team Lead memo §7).** The lock
timestamp is finalized; the gate is now waiting on Manager
reauthorization, not on the lock timestamp.

## Unit-test verification (CS, 2026-06-10, post-remediation)

```text
Tests run:    25  (22 prior + 3 new sidecar tests)
Tests passed: 25
Tests failed:  0
Status:       OK
```

New sidecar tests (Senior remediation §5, §6):
- `test_b1_output_preserved_byte_for_byte`:
    verifies the wrapper does NOT modify the B1 output file.
    Before/after byte-equality and sha256-equality both asserted.
- `test_lane1a_metadata_only_in_sidecar`:
    verifies the B1 output JSON contains no Lane 1a fields
    (`artifact_class`, `certification_relevance`, `lane_1a_context`,
    `original_context_from_b1v2`) and the sidecar carries them.
- `test_sidecar_validates_against_schema`:
    verifies the sidecar passes `jsonschema` validation against
    `schema/lane1a_sidecar.schema.json`.

All prior invariants still verified (B1 gap sign, B2 preempt, B5
survivor ordering, outcome determinism, plot prohibitions, schema
rejection, recipe acceptance, audit-log append-only, tag override,
scorer rules, dummy-policy non-degeneracy).

## CS Engineer sign-off (REMEDIATED)

```text
I certify that the artifact set above implements the Lane 1a design
packet v0.3 (sha256 f1280a85...) with the B-series corrections
(B1, B2, B3, B4 Option A, B5) applied AND the Senior remediation
(sidecar-attestation pattern; B1 output preserved byte-for-byte; Lane
1a metadata only in the sidecar).

All 25 unit tests pass. No first data access has occurred; no model
has been invoked; no live sweep output exists. B1 v2 source is
unmodified; B1 v2.1 has not been created or used. The Case B wrapper
invokes B1 v2 exclusively through its locked argparse surface and
does NOT mutate the B1 output.

The earlier rewrite-pattern wrapper (committed at 25613d3,
sha256 deff94c9...) is SUPERSEDED by this LOCK-RECORD and replaced
with the sidecar-pattern wrapper at sha256 a91e0c89.... The earlier
artifact remains in git history as historical audit trail.

This record is sealed against the listed hashes. No edit to any
listed artifact is permitted after Team Lead appends the lock
timestamp; corrections require a new sweep packet with a new lock
record.

— CS Engineer, 2026-06-10
```

## What this record does NOT do

- It does NOT authorize first data access.
- It does NOT authorize model invocation.
- It does NOT authorize the sweep to execute.
- These require Team Lead adversarial review of the remediated
  packet followed by explicit Manager execution authorization.

## Audit anchors

- B1 v2 runner locked at merge `3cbfce57`; not modified by Lane 1a.
- Senior remediation finding (2026-06-10): wrapper rewrite pattern
  rejected; sidecar attestation pattern adopted.
- Standing non-authorizations card: token-prior runs were blocked
  except by name; this LOCK-RECORD resolves the named exception for
  Lane 1a only.
- New permanent production rule (standing review-discipline): no
  production cycle may begin while any G1-open condition memo
  affects it.
- All execution gates other than Lane 1a packet preparation remain
  CLOSED.
