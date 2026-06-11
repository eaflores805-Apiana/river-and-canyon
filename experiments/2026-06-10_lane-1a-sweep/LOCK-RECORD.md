# Lane 1a Lock Record — 2026-06-10 (Path A.1 — MODEL_ID matches B1 v2)

Sweep ID: `lane-1a-2026-06-10`
Framework version (declared): `none`  *(Lane 1a is NOT a certification)*
Doctrine: *Lane 1a may rule out; Lane 1a may not rule in.*
Artifact class: `lane-1a-reconnaissance`
Certification relevance: `none`

Source design packet: `governance/2026-06-10_lane1a/DESIGN-PACKET-v0.3.md`
  sha256 `f1280a8563bbb48c5592c35c809be6c739859234cbf33b64a3786c6e5df67bab`

Source §13 normative manifest recipe: `governance/2026-06-10_lane1a/EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.2.md`

Senior remediation finding: `governance/2026-06-10_lane1a/SENIOR-FINDING-WRAPPER-REWRITE-2026-06-10.md`

CS deviation report (Step-3 architecture defect): `governance/2026-06-10_lane1a/CS-DEVIATION-REPORT-B1V2-MANIFEST-INTERFACE-2026-06-10.md`

Manager Path A direction: `governance/2026-06-10_lane1a/MANAGER-DIRECTION-PATH-A-2026-06-10.md`

Manager authorization memos:
  - `governance/2026-06-10_lane-1a-authorization/MANAGER-AUTHORIZATION.md` (lane opened)
  - `governance/2026-06-10_lane1a/MANAGER-DIRECTION-v0.3-OPTION-A-2026-06-10.md` (v0.3 + Option A)
  - `governance/2026-06-10_lane1a/MANAGER-AUTHORIZATION-FIRST-DATA-ACCESS-2026-06-10.md` (first data access, prior conditional)
  - `governance/2026-06-10_lane1a/MANAGER-REAUTHORIZATION-FIRST-DATA-ACCESS-2026-06-10.md` (re-issued against ef170fd7…; now superseded by Path A re-seal)

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

## Runner integration (Path A → Path A.1, Manager 2026-06-10)

**Root cause (Senior, Team Lead-approved one-sentence note):**

> B1 v2 validates against the Two-Hop L1 manifest schema.

**Wording (Manager-prescribed, applied verbatim):**

> Lane 1a uses a lane-specific runner that preserves B1 v2-compatible
> provenance conventions and locked model-loading dependencies, while
> leaving B1 v2 source unedited.

**Path A.1 model-identity correction (Manager 2026-06-10):**

> `lane1a_runner.MODEL_ID` must match B1 v2's MODEL_ID byte-for-byte:
> `"Qwen/Qwen2.5-3B-Instruct"`. Enforced by unit test
> `test_model_id_matches_b1v2`, which reads B1 v2 source directly and
> asserts equality with `lane1a_runner.MODEL_ID`. Any future drift in
> either side trips the test at CI time.

Concretely:

- The wrapper subprocesses `lane1a_runner.py` (NOT B1 v2's CLI).
- `lane1a_runner.py` uses `mlx_lm` directly (the shared dependency).
- `lane1a_runner.py` computes the model snapshot hash using the same
  algorithm B1 v2 uses (sha256 over a sorted manifest of
  (relative path, file size, per-file sha256)); the two records are
  comparable.
- `lane1a_runner.py` does NOT import any module from
  `experiments/2026-06-09_b1-harness-v2/`. Verified by unit test
  `test_no_b1v2_imports`.
- B1 v2 source remains unedited; B1 v2.1 is not created.
- This is not native B1 v2 execution and is not B1 v2.1.

## Locked artifact hashes (Path A)

| Artifact | sha256 | Status |
|---|---|---|
| `classification_criteria.yaml` | `9b32fa1e84529efe078590e1ab9e448a246077fa85cb1492e88dad21eed09b93` | unchanged |
| `manifest_generator.py` | `e2962139c2cd520e7e5c979830333e91523cdff3b196e1f475f31557f19c3d38` | unchanged |
| `prompt_template.md` | `1fa889ae8fede10d8b539a8f8672d4e68eedf67f8d0ce3592bbe9eb910df7cd1` | unchanged |
| `scorer.py` | `c1aff994081829a6888338aea8dadab30bf622203dbb5f597cd7298cf8f27495` | unchanged |
| `dummy_policies.py` | `46a5b2349051b4e51059575d056068360fe990889c57cb11a4ba155afe9ad36c` | unchanged |
| `runner_config.yaml` | `bbb4655e5789a0eb767a26b54d58dbe4bdc428f31469082dc0cc151d47596dc3` | **PATH A — b1v2 invocation block removed; runner: section added** |
| `lane1a_runner.py` | `4174039529e5820c4ff3904c6eff9c116cd0b1b7e963afb6a7c6d4e4d397f5a7` | **PATH A.1 — MODEL_ID corrected to `Qwen/Qwen2.5-3B-Instruct`** |
| `lane1a_runner_wrapper.py` | `4bed7fbdb938021638bda3908b7cbdb1e68e4dcc6305c7455b24df345cb444b1` | **PATH A — invokes lane1a_runner.py** |
| `analyzer.py` | `4c0087fa949883a772f608994f439132a195583a97035b7baff700230ba2144c` | unchanged |
| `plotter.py` | `dca510667d52d1b5a281f4a5ca5597c2abb5a7cb4a1a25a59baa98e397a5834a` | unchanged |
| `artifact_tags.py` | `bb5d396eeee45d0e08ae987d487ea57579e12bf87efc2fe4e76896b505290f2f` | unchanged |
| `audit_log.py` | `1c6578040dc3335b536453731c4cd0eb412ebea582c2eea38f3c6b39e57a90ed` | unchanged |
| `fixed_outcome.md` | `bde3c8043dc058c7f357921bbc8623acecf8077922cd620e7a1b2220f1ef3217` | unchanged |
| `exclusion_block.md` | `feb4b80cbc4b95be838fc39321086749c457ce3bfa745f0c57658ea5749318ce` | unchanged |
| `schema/per_rung_record.schema.json` | `beb48aacf384cee21c29265802d320292544875e342e26cc3b1ef4b7959ae14c` | unchanged |
| `schema/sweep_record.schema.json` | `449aae9259ed9fe2f188818ae880c691f419e0b62b302e40fffb1e99cea678ec` | unchanged |
| `schema/lane1a_sidecar.schema.json` | `23195986fe8bba1fa0754f9af1d9a80ce984e62f2056320d7ac9da281b4ac4aa` | **PATH A — runner_output fields** |
| `AUDIT-LOG-FORMAT.md` | `29b418c6cb6601d1aab4b28eba8e538ef828900eef6a02a9d821b128abc6a465` | unchanged |
| `test_lane1a_packet.py` | `8852c5171f92280cba320360b01bb1dc3e9539d4913a32cb7dc305dfa0602a5a` | **PATH A.1 — +1 test (test_model_id_matches_b1v2); 36/36 PASS** |
| `NOVELTY-LEDGER.md` | `aad806a47bea04d7b16b77a0c1205a472b97ecbf7b5591b2a77b71f8ccb9f112` | unchanged |

Total locked artifacts: 20 (was 19; lane1a_runner.py is the +1).

## Lock timestamp

```text
Lock timestamp: PENDING_TEAM_LEAD_REVIEW
```

**Reset to PENDING per Manager Path A.1 direction (`MANAGER-DIRECTION-
PATH-A1-MODEL-ID-2026-06-10.md` §6):** *"The prior Manager
authorization does not carry forward because the locked artifact set
and model identity changed."* The review chain must replay (Senior
intent-preservation + Team Lead combined re-review + Manager
reauthorization) against the Path A.1 LOCK-RECORD hash before CS may
finalize the timestamp.

Until the timestamp is finalized, `lane1a_runner_wrapper.py
preflight()` refuses to invoke (the `PENDING_TEAM_LEAD_REVIEW`
sentinel triggers `FirstDataAccessGateError`).

The earlier timestamp `2026-06-11T02:38:46Z` and post-touch hash
`88a2a16d…` are superseded by this re-seal; they are preserved in git
history for audit.

## Unit-test verification (CS, 2026-06-10, post-Path-A.1)

```text
Tests run:    36   (+1 vs Path A: test_model_id_matches_b1v2)
Tests passed: 36
Tests failed:  0
Status:       OK
```

Breakdown:
- 22 prior invariants (B1 gap sign; B2 preempt; B5 ordering; outcome
  determinism; plot prohibitions; schema rejection; recipe acceptance;
  audit log; tag override; scorer; dummy policies).
- 3 updated sidecar tests (runner_output byte preservation;
  lane1a_metadata only in sidecar; sidecar validates against the new
  schema with `runner_output_*` and `runner_name = lane1a_runner.py`
  fields).
- 7 new lane1a_runner manifest-validation tests (good manifest accepted;
  missing top-level key rejected; wrong artifact_class rejected; wrong
  certification_relevance rejected; invalid stratum rejected; missing
  item field rejected; **all 8 actual generated Lane 1a manifests pass
  lane1a_runner.validate_lane1a_manifest**).
- 3 new lane1a_runner provenance tests (no B1 v2 imports; B1 v2-
  compatible compute_model_snapshot_hash signature; decoding settings
  locked).

## CS Engineer sign-off (PATH A REMEDIATED)

```text
I certify that the artifact set above implements the Lane 1a design
packet v0.3 (sha256 f1280a85…) with:
  - all B-series corrections (B1 / B2 / B3 / B4 Option A / B5),
  - the Senior remediation (sidecar-attestation pattern; runner output
    preserved byte-for-byte; Lane 1a metadata only in sidecar), and
  - the Path A remediation (lane1a_runner.py; B1 v2-compatible
    provenance conventions; B1 v2 source unedited; B1 v2.1 not created
    or used).

All 35 unit tests pass. No first data access has occurred; no model
has been invoked; no live sweep output exists. B1 v2 source is
unmodified; B1 v2.1 has not been created or used. The wrapper
subprocesses lane1a_runner.py and writes a sidecar JSON alongside
each runner output; runner output bytes are preserved unchanged.

The packet does not claim native B1 v2 execution. The Manager-
prescribed wording ("Lane 1a uses a lane-specific runner that
preserves B1 v2-compatible provenance conventions and locked
model-loading dependencies, while leaving B1 v2 source unedited") is
applied verbatim in LOCK-RECORD, runner_config.yaml, the wrapper's
CONTEXT_FUNCTIONAL_STATEMENT, every sidecar's
context_functional_statement, and the CS remediation return.

The earlier wrapper sha256 a91e0c89… (sidecar over B1 v2 CLI) is
SUPERSEDED by the Path A wrapper sha256 4bed7fbd… (sidecar over
lane1a_runner.py). The earlier artifact remains in git history as
historical audit trail. The earlier LOCK-RECORD sha256 ef170fd7… is
superseded by the Path A LOCK-RECORD sha256 (computed post-seal).

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
- These require Team Lead adversarial review of the Path A
  remediated packet followed by explicit Manager reauthorization.

## Audit anchors

- B1 v2 runner locked at merge `3cbfce57`; not modified by Lane 1a
  in any cycle.
- Senior remediation finding (2026-06-10): wrapper rewrite pattern
  rejected; sidecar attestation pattern adopted.
- CS deviation discovery (2026-06-10): B1 v2 manifest-interface
  incompatibility; remediated by Path A (lane1a_runner.py).
- Standing non-authorizations card: token-prior runs were blocked
  except by name; this LOCK-RECORD resolves the named exception for
  Lane 1a only.
- Standing review-discipline rule: no production cycle may begin
  while any G1-open condition memo affects it.
- All execution gates other than Lane 1a packet preparation remain
  CLOSED.
