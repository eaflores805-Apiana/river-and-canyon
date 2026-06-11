# Lane 1a Lock Record — 2026-06-11 (Path E.1 — new sweep_id; explicit subprocess interpreter)

Sweep ID: `lane-1a-2026-06-11`
Framework version (declared): `none`  *(Lane 1a is NOT a certification)*
Doctrine: *Lane 1a may rule out; Lane 1a may not rule in.*
Artifact class: `lane-1a-reconnaissance`
Certification relevance: `none`

Source design packet: `governance/2026-06-10_lane1a/DESIGN-PACKET-v0.3.md`
  sha256 `f1280a8563bbb48c5592c35c809be6c739859234cbf33b64a3786c6e5df67bab`

Source §13 normative manifest recipe: `governance/2026-06-10_lane1a/EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.2.md`

Manager Path E.1 direction: `governance/2026-06-10_lane1a/MANAGER-DIRECTION-PATH-E1-RUNTIME-ENV-2026-06-10.md`

Prior sweep attempt (archived as `instrument_failure_before_model_load`):
  - sweep_id `lane-1a-2026-06-10`
  - LOCK-RECORD hash at finalization: `270078a0…`
  - 31 runner_started events; 30 runner_anomaly; 0 generations
  - Audit log preserved in this directory at `AUDIT-LOG-2026-06-10-INSTRUMENT-FAILURE.ndjson`
  - Driver stderr/stdout preserved at `_sweep_st{err,out}-2026-06-10-INSTRUMENT-FAILURE.log`

## B4 — Token-prior control authorization (Manager 2026-06-10)

```text
Token-prior control authorization: Manager-authorized Lane 1a token-prior control path
```

(Token-prior authorization carries forward from prior Manager memos
— the Manager decision was substantive, not bound to the prior
sweep_id. Reconfirmation expected at first-data-access reauthorization
against this new sweep_id.)

## Generation plan (per Manager Option A)

```text
planned_generation_count = 1536
candidate_generation_count = 768
control_generation_count = 768
control_scoring_denominator = 80 answerable-mirroring controls per rung
NULL-mirroring controls = descriptive-only
```

## Runner integration (Path E.1, Manager 2026-06-10)

**Root cause (Senior, Team Lead-approved one-sentence note, carried forward from Path A.1):**

> B1 v2 validates against the Two-Hop L1 manifest schema.

**Root cause (Path E.1, new):**

> `sys.executable` in the wrapper context resolved to `/opt/anaconda3/bin/python`
> with `mlx_lm 0.19.3`, which does not expose `make_sampler` from
> `mlx_lm.sample_utils`. The fix pins the production subprocess to an
> explicit Python interpreter and adds a smoke test that verifies the
> import surface succeeds before first data access.

**Wording (Manager-prescribed, applied verbatim):**

> Lane 1a uses a lane-specific runner that preserves B1 v2-compatible
> provenance conventions and locked model-loading dependencies, while
> leaving B1 v2 source unedited.

**Production subprocess interpreter (Path E.1; explicit):**

> Python interpreter: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`
> Expected mlx_lm version: `0.31.3`
>
> Cross-referenced by unit test `test_interpreter_path_matches_config`
> (asserts `lane1a_runner_wrapper.PRODUCTION_PYTHON` byte-equals
> `runner_config.yaml production.python_interpreter`) and
> `test_expected_mlx_lm_version_matches_config`. Verified at preflight
> time by `test_production_subprocess_smoke` (spawns the production
> subprocess; verifies import success; verifies mlx_lm version).

## Locked artifact hashes (Path E.1)

| Artifact | sha256 | Status |
|---|---|---|
| `classification_criteria.yaml` | `9b32fa1e84529efe078590e1ab9e448a246077fa85cb1492e88dad21eed09b93` | unchanged |
| `manifest_generator.py` | `8b480243e828ffb3a642625000165751aed5322f6c52b01238d8f3dd58e02efa` | **PATH E.1 — SWEEP_ID changed** |
| `prompt_template.md` | `1fa889ae8fede10d8b539a8f8672d4e68eedf67f8d0ce3592bbe9eb910df7cd1` | unchanged |
| `scorer.py` | `c1aff994081829a6888338aea8dadab30bf622203dbb5f597cd7298cf8f27495` | unchanged |
| `dummy_policies.py` | `46a5b2349051b4e51059575d056068360fe990889c57cb11a4ba155afe9ad36c` | unchanged |
| `runner_config.yaml` | `be22cce51475a55b7440d9755f14f30f3a82977fc1a331d75f385470319b6a92` | **PATH E.1 — sweep_id + production: section** |
| `lane1a_runner.py` | `4174039529e5820c4ff3904c6eff9c116cd0b1b7e963afb6a7c6d4e4d397f5a7` | unchanged |
| `lane1a_runner_wrapper.py` | `e3ab78f134073d67e337ebc1fe9ab0b87b3f4fb7ed1761031d70f3b94c349314` | **PATH E.1 — PRODUCTION_PYTHON constant; subprocess uses it; smoke test added; preflight runs smoke test** |
| `analyzer.py` | `4c0087fa949883a772f608994f439132a195583a97035b7baff700230ba2144c` | unchanged |
| `plotter.py` | `dca510667d52d1b5a281f4a5ca5597c2abb5a7cb4a1a25a59baa98e397a5834a` | unchanged |
| `artifact_tags.py` | `bb5d396eeee45d0e08ae987d487ea57579e12bf87efc2fe4e76896b505290f2f` | unchanged |
| `audit_log.py` | `1c6578040dc3335b536453731c4cd0eb412ebea582c2eea38f3c6b39e57a90ed` | unchanged |
| `fixed_outcome.md` | `bde3c8043dc058c7f357921bbc8623acecf8077922cd620e7a1b2220f1ef3217` | unchanged |
| `exclusion_block.md` | `feb4b80cbc4b95be838fc39321086749c457ce3bfa745f0c57658ea5749318ce` | unchanged |
| `schema/per_rung_record.schema.json` | `beb48aacf384cee21c29265802d320292544875e342e26cc3b1ef4b7959ae14c` | unchanged |
| `schema/sweep_record.schema.json` | `acef5719a3394d8c3581c51b4548dc1e13577a0214962d8965f312a3edd73910` | **PATH E.1 — sweep_id const updated** |
| `schema/lane1a_sidecar.schema.json` | `23195986fe8bba1fa0754f9af1d9a80ce984e62f2056320d7ac9da281b4ac4aa` | unchanged |
| `AUDIT-LOG-FORMAT.md` | `29b418c6cb6601d1aab4b28eba8e538ef828900eef6a02a9d821b128abc6a465` | unchanged |
| `test_lane1a_packet.py` | `6f30f01f5a87fe56996e0a08dfa621a0c09144a4ca3177194a225bb85cfb33cd` | **PATH E.1 — TestPathE1ProductionSubprocess class (4 new tests)** |
| `NOVELTY-LEDGER.md` | `aad806a47bea04d7b16b77a0c1205a472b97ecbf7b5591b2a77b71f8ccb9f112` | unchanged |

Total locked artifacts: 20.

## Manifest hashes (regenerated under new sweep_id seed)

```text
seed = sha256("lane-1a-2026-06-11")[:8] = 111550783468268645

L01: 808bf4e81865c7be586521b0b9e23b5269ef8dc0465799def2855c9189f346a9
L02: 00bfa0fcdb74e2858bf711e9436593e33c410fb174406c1d3fda7220922dc95b
L03: dea1a74ec3929f0808e574516894c667899192212b609e6f2bd261c7d2409004
L04: e340380326f6ead1d90696e3412b6248c85e6c9ba8625cf4dd9ec8f854f5b3c2
L05: 999404cd503bfbbfdaadaf2445db6766fadad6f89aa4fc6b7954fb242e65b45a
L06: 0f09a00c1f111a2f87d38322eb1b975a93e3a2388fdcd0134b18baf095cbcfe4
L07: 0aa90da2aa4da6be2e724e38a654923a129ad2efebb4ad554e5e67c3bb639e1b
L08: 7b68db9c84b538e653aa0cd06ab39e06232ce23f5d3abaf7a9d7370f26247aec
```

Manifests are regenerated outputs, not locked artifacts; they recompute
bit-identically from the manifest_generator.py + classification_criteria.yaml
+ sweep_id inputs. The lock applies to the inputs.

## Lock timestamp

```text
Lock timestamp: 2026-06-11T03:37:50Z
```

CS appended this RFC 3339 UTC timestamp under Manager Path E.1
reauthorization authority (`MANAGER-REAUTHORIZATION-PATH-E1-FIRST-DATA-
ACCESS-2026-06-10.md` §3) after Senior Path E.1 intent-preservation
PASS + Team Lead Path E.1 combined re-review PASS with both conditions
resolved without re-seal.

The `first_data_access_timestamp` recorded by the wrapper at sweep
time MUST postdate this lock timestamp.
`lane1a_runner_wrapper.py preflight()` enforces this comparison.

## Unit-test verification (CS, 2026-06-10, post-Path-E.1)

```text
Tests run:    40   (36 prior + 4 new Path E.1 tests)
Tests passed: 40 (1 skipped: jsonschema not installed for one sidecar test)
Tests failed:  0
Status:       OK
```

New Path E.1 tests (`TestPathE1ProductionSubprocess`):
- `test_interpreter_path_matches_config` — cross-references
  `wrapper.PRODUCTION_PYTHON` against `runner_config.yaml`
- `test_expected_mlx_lm_version_matches_config` — cross-references
  `wrapper.EXPECTED_MLX_LM_VERSION` against `runner_config.yaml`
- `test_production_subprocess_smoke` — spawns the production
  subprocess; verifies `from mlx_lm.sample_utils import make_sampler`
  succeeds; verifies `mlx_lm.__version__` equals expected; would have
  caught the prior instrument failure
- `test_wrapper_does_not_use_sys_executable_for_subprocess` —
  source-level grep asserts the wrapper's subprocess argv[0] is
  `PRODUCTION_PYTHON`, not `sys.executable`

## CS Engineer sign-off (PATH E.1)

```text
I certify that the artifact set above implements the Lane 1a design
packet v0.3 (sha256 f1280a85...) with all B-series corrections, the
Senior sidecar remediation, Path A (lane-specific runner), Path A.1
(MODEL_ID matches B1 v2), and the Path E.1 fix (explicit production
subprocess interpreter + smoke test).

All 40 unit tests pass. No first data access has occurred in this
remediation cycle; the production subprocess smoke test ran successfully
(verified mlx_lm 0.31.3 importable in the pinned Python 3.13).

B1 v2 source is unmodified; B1 v2.1 has not been created or used. The
wrapper subprocesses lane1a_runner.py via the EXPLICIT Python
interpreter path; sys.executable is no longer used for subprocess
invocation in the production path.

The prior sweep_id (lane-1a-2026-06-10) is archived as
instrument_failure_before_model_load; its audit log is preserved as
AUDIT-LOG-2026-06-10-INSTRUMENT-FAILURE.ndjson alongside the driver
stderr/stdout. The new sweep_id (lane-1a-2026-06-11) starts with no
prior runner_started events; the wrapper's no-re-execution check on a
fresh AUDIT-LOG.ndjson (not yet created) will allow each (rung_id,
stratum) one attempt.

This record is sealed against the listed hashes. No edit to any listed
artifact is permitted after Team Lead appends the lock timestamp;
corrections require a new sweep packet with a new lock record.

— CS Engineer, 2026-06-10
```

## What this record does NOT do

- It does NOT authorize first data access.
- It does NOT authorize model invocation.
- It does NOT authorize the sweep to execute.
- These require Team Lead adversarial review of the Path E.1
  remediated packet followed by explicit Manager reauthorization.

## Audit anchors

- B1 v2 runner locked at merge `3cbfce57`; not modified by Lane 1a in
  any cycle.
- Senior wrapper-rewrite finding (2026-06-10): closed by sidecar pattern.
- CS deviation 1 — B1 v2 manifest-interface (2026-06-10): closed by Path A.
- CS deviation 2 — MODEL_ID mismatch (2026-06-10): closed by Path A.1.
- CS deviation 3 — runtime environment / mlx_lm import (2026-06-10):
  closed by Path E.1 (this record).
- Standing non-authorizations card: token-prior runs were blocked
  except by name; this LOCK-RECORD carries forward the named exception
  for Lane 1a only.
- Standing review-discipline rules in force:
  - G1-open production rule
  - sibling-artifact cross-reference unit test rule
  - production-path subprocess smoke test rule (added with this Path E.1
    cycle)
- All execution gates other than Lane 1a packet preparation remain
  CLOSED.
