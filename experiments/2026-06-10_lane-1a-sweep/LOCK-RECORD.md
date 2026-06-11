# Lane 1a Lock Record — 2026-06-10

Sweep ID: `lane-1a-2026-06-10`
Framework version (declared): `none`  *(Lane 1a is NOT a certification)*
Doctrine: *Lane 1a may rule out; Lane 1a may not rule in.*
Artifact class: `lane-1a-reconnaissance`
Certification relevance: `none`

Source design packet: `governance/2026-06-10_lane1a/DESIGN-PACKET-v0.3.md`
  sha256 `f1280a8563bbb48c5592c35c809be6c739859234cbf33b64a3786c6e5df67bab`

Source §13 normative manifest recipe: `governance/2026-06-10_lane1a/EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.2.md`

Manager authorization memos:
  - `governance/2026-06-10_lane-1a-authorization/MANAGER-AUTHORIZATION.md` (lane opened)
  - `governance/2026-06-10_lane1a/MANAGER-DIRECTION-v0.3-OPTION-A-2026-06-10.md` (v0.3 + Option A)

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

## Locked artifact hashes

| Artifact | sha256 |
|---|---|
| `classification_criteria.yaml` | `9b32fa1e84529efe078590e1ab9e448a246077fa85cb1492e88dad21eed09b93` |
| `manifest_generator.py` | `e2962139c2cd520e7e5c979830333e91523cdff3b196e1f475f31557f19c3d38` |
| `prompt_template.md` | `1fa889ae8fede10d8b539a8f8672d4e68eedf67f8d0ce3592bbe9eb910df7cd1` |
| `scorer.py` | `c1aff994081829a6888338aea8dadab30bf622203dbb5f597cd7298cf8f27495` |
| `dummy_policies.py` | `46a5b2349051b4e51059575d056068360fe990889c57cb11a4ba155afe9ad36c` |
| `runner_config.yaml` | `49401bf572d0491ab9f771fa3cce92edff6bd112c905f71372ca12eea4ca3bcc` |
| `lane1a_runner_wrapper.py` | `deff94c9f5fe7a8ead7c8a12c67110f5ae62370c1189415c2842a1110d0ae2b6` |
| `analyzer.py` | `4c0087fa949883a772f608994f439132a195583a97035b7baff700230ba2144c` |
| `plotter.py` | `dca510667d52d1b5a281f4a5ca5597c2abb5a7cb4a1a25a59baa98e397a5834a` |
| `artifact_tags.py` | `bb5d396eeee45d0e08ae987d487ea57579e12bf87efc2fe4e76896b505290f2f` |
| `audit_log.py` | `1c6578040dc3335b536453731c4cd0eb412ebea582c2eea38f3c6b39e57a90ed` |
| `fixed_outcome.md` | `bde3c8043dc058c7f357921bbc8623acecf8077922cd620e7a1b2220f1ef3217` |
| `exclusion_block.md` | `feb4b80cbc4b95be838fc39321086749c457ce3bfa745f0c57658ea5749318ce` |
| `schema/per_rung_record.schema.json` | `beb48aacf384cee21c29265802d320292544875e342e26cc3b1ef4b7959ae14c` |
| `schema/sweep_record.schema.json` | `449aae9259ed9fe2f188818ae880c691f419e0b62b302e40fffb1e99cea678ec` |
| `AUDIT-LOG-FORMAT.md` | `29b418c6cb6601d1aab4b28eba8e538ef828900eef6a02a9d821b128abc6a465` |
| `test_lane1a_packet.py` | `4477a9940bda14beb5947724dd83a226b2a3a96d87c196399b8e70fa3da92f7a` |
| `NOVELTY-LEDGER.md` | `aad806a47bea04d7b16b77a0c1205a472b97ecbf7b5591b2a77b71f8ccb9f112` |

## Lock timestamp

```text
Lock timestamp: PENDING_TEAM_LEAD_REVIEW
```

*(The lock timestamp is filled in by the Team Lead at the end of the
combined adversarial review. CS does not seal the timestamp before
review; the field reads `PENDING_TEAM_LEAD_REVIEW` until the Team Lead
appends a real RFC 3339 UTC value. Manager confirmation memo then
records the `first_data_access_timestamp` which MUST postdate this
lock timestamp.)*

## Unit-test verification (CS, 2026-06-10)

```text
Tests run:    22
Tests passed: 22
Tests failed:  0
Status:       OK
```

Key invariants verified by unit test:
- B1 — gap sign `content_acc - strict_acc`; Senior's test
  (content 0.90 / strict 0.70) attaches the label.
- B2 — inconclusive preempts: void_count>5 OR harness_anomaly OR
  missing_outputs → labels = `["inconclusive_not_actionable"]` only;
  no other label attaches.
- B5 — survivors serialized in alphabetical rung-ID order.
- Outcome-statement determinism: K=0 emits STATEMENT_A; K>0 emits
  STATEMENT_B with K substituted; STATEMENT_C always appended; no
  other string can be produced by `emit_outcome()`.
- Plot prohibitions: every form in `PROHIBITED_FIGURE_TYPES` raises
  `NotImplementedError` referencing §1.8.
- Schema rejection: per-rung schema rejects `rank` and `preference`
  fields under `additionalProperties:false`; sweep schema blocks
  `framework_version != "none"`.
- Recipe acceptance check: every declared dummy policy yields a
  non-degenerate prediction vector on every rung's generated manifest
  (≥ 3 distinct predictions per policy).
- Audit log: append-only; `total_attempts == count(runner_started)`.
- Artifact tagger: rejects override of `artifact_class` or
  `certification_relevance` to non-canonical values.
- Scorer: strict-implies-content; void detection; abstain detection.

## CS Engineer sign-off

```text
I certify that the artifact set above implements the Lane 1a design
packet v0.3 (sha256 f1280a85…) with the B-series corrections (B1, B2,
B3, B4 Option A, B5) applied. All 22 unit tests pass. No first data
access has occurred; no model has been invoked; no live sweep output
exists. B1 v2 source is unmodified; B1 v2.1 has not been created or
used. The Case B wrapper invokes B1 v2 exclusively through its locked
argparse surface.

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
- These require Team Lead adversarial review of design + execution
  packets followed by explicit Manager execution authorization.

## Audit anchors

- B1 v2 runner locked at merge `3cbfce57`; not modified by Lane 1a.
- Standing non-authorizations card: token-prior runs were blocked
  except by name; this LOCK-RECORD resolves the named exception for
  Lane 1a only.
- All execution gates other than Lane 1a packet preparation remain
  CLOSED.
