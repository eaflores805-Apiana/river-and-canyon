# Lane 1a Execution Packet v0.1 — Master Binding Document

From: CS Engineer
To: Team Lead
Cc: Senior Engineer, Manager
Date: 2026-06-10
Status: Step-3 production complete; all 22 unit tests pass; LOCK-RECORD sealed against listed hashes; awaiting Team Lead combined adversarial review

---

## 1. What this packet binds

This is the top-level governance document that binds together the
Lane 1a execution-packet artifacts produced under Manager Option A
authorization (2026-06-10). All artifacts are hash-recorded in
`experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` and are subject
to the "no edit after Team Lead lock-timestamp seal" rule.

Source design packet: `governance/2026-06-10_lane1a/DESIGN-PACKET-v0.3.md`
  sha256 `f1280a8563bbb48c5592c35c809be6c739859234cbf33b64a3786c6e5df67bab`

Source normative recipe: `governance/2026-06-10_lane1a/EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.2.md`

Lock record: `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md`
  sha256 `ecfdd743fb583c018953e71c22c8cb254ef6e14f00e66ed599ae45fe9630c416`

## 2. Artifact inventory (20 entries)

### 2.1 Governance documents (governance/2026-06-10_lane1a/)

| Artifact | Status |
|---|---|
| `DESIGN-PACKET-v0.3.md` | Senior; sha256 `f1280a85…` (filed at `e6cf3c1`) |
| `EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.2.md` | CS; this commit |
| `EXECUTION-PACKET-v0.1.md` (this document) | CS; this commit |

### 2.2 Locked execution artifacts (experiments/2026-06-10_lane-1a-sweep/)

| Artifact | sha256 | Role |
|---|---|---|
| `LOCK-RECORD.md` | `ecfdd743fb583c018953e71c22c8cb254ef6e14f00e66ed599ae45fe9630c416` | Master hash + B4 auth + sign-off |
| `classification_criteria.yaml` | `9b32fa1e84529efe078590e1ab9e448a246077fa85cb1492e88dad21eed09b93` | Source of truth: constants + rules |
| `manifest_generator.py` | `e2962139c2cd520e7e5c979830333e91523cdff3b196e1f475f31557f19c3d38` | Recipe-driven manifest builder |
| `prompt_template.md` | `1fa889ae8fede10d8b539a8f8672d4e68eedf67f8d0ce3592bbe9eb910df7cd1` | Locked prompt format |
| `scorer.py` | `c1aff994081829a6888338aea8dadab30bf622203dbb5f597cd7298cf8f27495` | Strict + content dual scoring |
| `dummy_policies.py` | `46a5b2349051b4e51059575d056068360fe990889c57cb11a4ba155afe9ad36c` | 5 declared offline policies |
| `runner_config.yaml` | `49401bf572d0491ab9f771fa3cce92edff6bd112c905f71372ca12eea4ca3bcc` | B1 v2 invocation flags |
| `lane1a_runner_wrapper.py` | `deff94c9f5fe7a8ead7c8a12c67110f5ae62370c1189415c2842a1110d0ae2b6` | Case B wrapper around B1 v2 |
| `analyzer.py` | `4c0087fa949883a772f608994f439132a195583a97035b7baff700230ba2144c` | Diagnostic axes + label assignment + outcome |
| `plotter.py` | `dca510667d52d1b5a281f4a5ca5597c2abb5a7cb4a1a25a59baa98e397a5834a` | 2 figure types; prohibitions enforced at code level |
| `artifact_tags.py` | `bb5d396eeee45d0e08ae987d487ea57579e12bf87efc2fe4e76896b505290f2f` | Tag injection at every write point |
| `audit_log.py` | `1c6578040dc3335b536453731c4cd0eb412ebea582c2eea38f3c6b39e57a90ed` | Append-only NDJSON writer |
| `fixed_outcome.md` | `bde3c8043dc058c7f357921bbc8623acecf8077922cd620e7a1b2220f1ef3217` | 3 byte-locked outcome statements |
| `exclusion_block.md` | `feb4b80cbc4b95be838fc39321086749c457ce3bfa745f0c57658ea5749318ce` | Verbatim §1.10 exclusion text |
| `schema/per_rung_record.schema.json` | `beb48aacf384cee21c29265802d320292544875e342e26cc3b1ef4b7959ae14c` | additionalProperties:false |
| `schema/sweep_record.schema.json` | `449aae9259ed9fe2f188818ae880c691f419e0b62b302e40fffb1e99cea678ec` | framework_version:"none" const |
| `AUDIT-LOG-FORMAT.md` | `29b418c6cb6601d1aab4b28eba8e538ef828900eef6a02a9d821b128abc6a465` | Event schema + B5 semantics |
| `test_lane1a_packet.py` | `4477a9940bda14beb5947724dd83a226b2a3a96d87c196399b8e70fa3da92f7a` | 22 unit tests; all pass |
| `NOVELTY-LEDGER.md` | `aad806a47bea04d7b16b77a0c1205a472b97ecbf7b5591b2a77b71f8ccb9f112` | Fork A bar on construction inputs |

## 3. Test summary

```
Tests run:     22
Tests passed:  22
Tests failed:   0
```

Tests run via `python -m unittest test_lane1a_packet` from the
experiment directory.

Coverage:

- B1 gap sign (Senior unit test + below-threshold case)
- B2 inconclusive preempt (void / harness / missing-outputs)
- B5 survivor alphabetical ordering
- Outcome-statement determinism (STATEMENT_A/B/C)
- Plot prohibitions (each prohibited form raises `NotImplementedError`)
- Schema rejection of `rank`/`preference` fields
- Schema rejection of `framework_version != "none"`
- Recipe acceptance check (every declared dummy policy non-degenerate
  on every rung's generated manifest)
- Audit log append-only + total_attempts counting
- Artifact-tag override rejection
- Scorer strict-implies-content + void + abstain

## 4. Senior §3.B4 token-prior path resolution

**Option A selected by Manager 2026-06-10.** LOCK-RECORD carries the
exact authorization line:

```text
Token-prior control authorization: Manager-authorized Lane 1a token-prior control path
```

Generation plan under Option A:

```text
candidate_generations:           768
control_generations:             768
planned_generation_count:        1536
control_scoring_denominator:     80 (answerable-mirroring controls only)
NULL-mirroring control scoring:  descriptive-only
```

## 5. Case B wrapper — B1 v2 surface integrity

The wrapper (`lane1a_runner_wrapper.py`) invokes B1 v2's locked CLI
exclusively:

```text
B1 v2 runner: experiments/2026-06-09_b1-harness-v2/code/runner_b1_v2.py
B1 v2 lock:   merge 3cbfce57 (unchanged)
Invocation:
    --mode live
    --context paper2-reproduction
    --framework-version none
    --manifest <lane1a-manifest-path>
```

Lane 1a semantic tagging is applied at the wrapper layer:

- Output `context` field overridden to `"lane-1a-reconnaissance"`.
- Tags injected: `artifact_class: "lane-1a-reconnaissance"`,
  `certification_relevance: "none"`.
- Original B1 v2 `context` value preserved as
  `original_context_from_b1v2` for audit.

**B1 v2 source is NOT edited. B1 v2.1 has NOT been created or used.**

## 6. Six confirmations to Team Lead (anticipating combined review)

| # | Statement | Status |
|---|---|---|
| 1 | No first data access has occurred. | CONFIRMED — no model invocation; no live raw outputs |
| 2 | No model invocation. | CONFIRMED — `lane1a_runner_wrapper.py` script entry point runs only `preflight()`, which is gated by LOCK-RECORD; preflight not invoked here |
| 3 | B1 v2 source unedited. | CONFIRMED — `experiments/2026-06-09_b1-harness-v2/` not touched |
| 4 | B1 v2.1 not created or used. | CONFIRMED — no B1 v2.1 references in any produced artifact (grep clean) |
| 5 | Token-prior authorization represented in LOCK-RECORD. | CONFIRMED — verbatim Manager-authorized line present |
| 6 | All B1–B5 corrections applied in code. | CONFIRMED — unit-tested |

## 7. Sequence after this commit

```text
1. Team Lead adversarial review of:
   - DESIGN-PACKET-v0.3.md
   - EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.2.md
   - EXECUTION-PACKET-v0.1.md (this document)
   - All 18 artifacts under experiments/2026-06-10_lane-1a-sweep/
2. Team Lead appends RFC 3339 UTC lock timestamp to LOCK-RECORD.md.
3. Manager issues explicit first-data-access authorization memo.
4. CS preflight() reads LOCK-RECORD; validates token-prior auth and
   lock-timestamp ordering; emits `first_data_access` audit event.
5. CS invokes wrapper for each (rung_id, stratum) in ladder order;
   the wrapper enforces the no-re-execution rule via the audit log.
6. Analyzer aggregates per-rung scoring; assigns labels; computes K;
   emits fixed outcome statement.
7. Plotter produces the two allowed figures with mandatory footer.
8. EXPERIMENT_LOG.md gets a Lane 1a entry (sealed-section update).
9. CS final-report return to Manager.

This packet authorizes none of steps 4-9. Manager confirmation is the
gating event.
```

## 8. Non-authorizations carried forward

This packet does NOT authorize:

```text
first data access
Lane 1a execution
runner invocation against live sweep manifests
model calls
generation
candidate selection
candidate ranking
candidate shortlist
threshold-sheet population
threshold lock
certification evaluation
INT8 / INT4 stress-retention run
B1 v2.1 implementation
Claim C activation
Fork A reactivation
Paper 3 application beyond Lane 1a packet use
Paper 6 activation
public benchmark packaging
```

All work beyond Step-3 packet production remains closed.

— CS Engineer, 2026-06-10
