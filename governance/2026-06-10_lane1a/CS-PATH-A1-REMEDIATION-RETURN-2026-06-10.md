# CS Path A.1 Remediation Return — MODEL_ID Matches B1 v2

From: CS Engineer
To: Elias / Manager
Cc: Team Lead, Senior Engineer, New Senior Engineer
Date: 2026-06-10
Status: Path A.1 remediation complete; 36/36 unit tests pass; LOCK-RECORD re-sealed with `PENDING_TEAM_LEAD_REVIEW`; standing review-discipline rule added; awaiting Senior intent-preservation + Team Lead combined re-review + Manager re-reauthorization

---

## 0. TL;DR

```text
Path A.1 authorized:               Manager direction 2026-06-10
MODEL_ID corrected:                mlx-community/Qwen2.5-3B-Instruct-bf16
                                   -> Qwen/Qwen2.5-3B-Instruct
                                   (byte-for-byte match with B1 v2)
New unit test:                     test_model_id_matches_b1v2
                                   - reads B1 v2 source directly
                                   - asserts byte-equality with lane1a_runner.MODEL_ID
                                   - PASSES
Standing rule added:               sibling-artifact cross-reference test rule
                                   (Manager §4 accepted CS proposal)
Tests:                             36/36 PASS (35 prior + 1 new)
LOCK-RECORD re-sealed:             5a3fbdf80607582e2f2d5a7d61369a1dde04bc3318597230d2de13341cd16d11
                                   Lock timestamp = PENDING_TEAM_LEAD_REVIEW
                                   (prior authorization does not carry forward)
First data access:                 NOT EXECUTED
Model load:                        DID NOT OCCUR
B1 v2 source:                      UNEDITED
B1 v2.1:                           NOT CREATED OR USED
```

## 1. Twelve-item CS return (per Manager memo §5)

### 1. Complete changed artifact list

| # | Path | Change |
|---|---|---|
| 1 | `experiments/2026-06-10_lane-1a-sweep/lane1a_runner.py` | MODEL_ID one-line change: `mlx-community/Qwen2.5-3B-Instruct-bf16` → `Qwen/Qwen2.5-3B-Instruct` |
| 2 | `experiments/2026-06-10_lane-1a-sweep/test_lane1a_packet.py` | added `test_model_id_matches_b1v2` (reads B1 v2 source; asserts byte equality); added `import re` |
| 3 | `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | re-sealed: new hashes for above two; Path A.1 model-identity correction section; reset Lock timestamp to `PENDING_TEAM_LEAD_REVIEW`; supersession note for prior touched state |
| 4 | `governance/standing/STANDING-REVIEW-DISCIPLINE.md` | NEW SECTION: *"Additional rule — sibling-artifact cross-reference tests"* with the canonical example |
| 5 | `governance/2026-06-10_lane1a/MANAGER-DIRECTION-PATH-A1-MODEL-ID-2026-06-10.md` | NEW (verbatim Manager memo + CS acknowledgement) |
| 6 | `governance/2026-06-10_lane1a/CS-PATH-A1-REMEDIATION-RETURN-2026-06-10.md` | NEW (this memo) |

### 2. Full sha256 hash for every changed artifact

```text
lane1a_runner.py                4174039529e5820c4ff3904c6eff9c116cd0b1b7e963afb6a7c6d4e4d397f5a7
test_lane1a_packet.py           8852c5171f92280cba320360b01bb1dc3e9539d4913a32cb7dc305dfa0602a5a
LOCK-RECORD.md                  5a3fbdf80607582e2f2d5a7d61369a1dde04bc3318597230d2de13341cd16d11
STANDING-REVIEW-DISCIPLINE.md   (re-hashed at commit time; new section appended)
MANAGER-DIRECTION-PATH-A1-...   (governance file; not a locked artifact)
CS-PATH-A1-REMEDIATION-RETURN   (governance file; not a locked artifact)
```

All 18 other locked artifacts (the 20 minus lane1a_runner and test) are
unchanged. Verified by re-hashing every locked artifact against the
LOCK-RECORD table.

### 3. Updated LOCK-RECORD hash

```text
Path A.1 LOCK-RECORD.md sha256: 5a3fbdf80607582e2f2d5a7d61369a1dde04bc3318597230d2de13341cd16d11
Lock timestamp:                 PENDING_TEAM_LEAD_REVIEW
```

Supersedes:
- Path A LOCK-RECORD `68edbdcd…` (sealed; PENDING)
- Path A post-touch `88a2a16d…` (timestamp `2026-06-11T02:38:46Z` — superseded because the locked artifact set changed)

### 4. Test summary

```text
Test runner:    python -m unittest test_lane1a_packet
Tests run:      36   (35 prior + 1 new test_model_id_matches_b1v2)
Tests passed:   36
Tests failed:    0
Wall time:      0.281s
```

The new test (`test_model_id_matches_b1v2`):

- Locates B1 v2 source at `experiments/2026-06-09_b1-harness-v2/code/runner_b1_v2.py`.
- Reads the file directly (no import).
- Extracts B1 v2's `MODEL_ID` value via regex.
- Asserts byte-equality with `lane1a_runner.MODEL_ID`.
- The assertion message names both values explicitly so any future
  drift is debuggable from the test output alone.

### 5. Confirmation that `test_model_id_matches_b1v2` passes

**CONFIRMED.** Verified:

```text
B1 v2 MODEL_ID:           'Qwen/Qwen2.5-3B-Instruct'
lane1a_runner MODEL_ID:   'Qwen/Qwen2.5-3B-Instruct'
match:                    True
```

The test's regex `^MODEL_ID\s*=\s*"([^"]+)"` extracts B1 v2's value
from line 92 of `runner_b1_v2.py`. The extracted value is
byte-identical to `lane1a_runner.MODEL_ID` (line 50 of
`lane1a_runner.py`).

### 6. Confirmation that lane1a_runner.py uses `Qwen/Qwen2.5-3B-Instruct`

**CONFIRMED.** Direct file inspection:

```python
# experiments/2026-06-10_lane-1a-sweep/lane1a_runner.py:50
MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"   # Path A.1 (Manager 2026-06-10): matches B1 v2 byte-for-byte
```

### 7. Confirmation that no first data access occurred

**CONFIRMED.** No `lane1a_runner_wrapper.py preflight()` invocation
(the lock timestamp is PENDING, so preflight would refuse). No
`lane1a_runner_wrapper.py invoke_runner()` invocation. No
`lane1a_runner.py` standalone invocation.

### 8. Confirmation that no model load occurred

**CONFIRMED.** `mlx_lm.load(MODEL_ID)` not called in this session.

### 9. Confirmation that no live outputs were produced

**CONFIRMED.** `experiments/2026-06-10_lane-1a-sweep/raw/` does not
exist. `AUDIT-LOG.ndjson` does not exist. The only outputs present are
the 8 deterministic Lane 1a manifests + recipe acceptance check
results + manifest hashes lock, all from prior (no-model-call)
`manifest_generator.py main()` invocation.

### 10. Confirmation that B1 v2 was not edited

**CONFIRMED.** `git diff experiments/2026-06-09_b1-harness-v2/`
returns empty. B1 v2 remains at merge `3cbfce57`. The
`test_model_id_matches_b1v2` test reads B1 v2 source READ-ONLY (via
`Path.read_text()`); does not import or modify.

### 11. Confirmation that B1 v2.1 was not created or used

**CONFIRMED.** No file named for B1 v2.1. No code path references B1
v2.1 features.

### 12. Any remaining deviation or concern

**None known.**

CS exercised the standing review-discipline rule against the Path A.1
changes:

- Verified the canonical examples called out in §4 of Manager memo —
  schema field names (per_rung schema, sweep schema, sidecar schema
  all const-locked); CLI constants (validate_only + required argparse
  args); mode names (not on B1 v2 — Path A's whole point); context
  names (not on B1 v2 — Path A's whole point); framework-version
  behavior (const `"none"`); artifact tags (const-locked).
- The MODEL_ID test is the canonical example of the new rule applied.
- CS is preparing similar cross-reference assertions for any future
  artifact integrations.

## 2. Standing review-discipline rule addition (Manager §4 accepted)

`governance/standing/STANDING-REVIEW-DISCIPLINE.md` now carries:

> **CS production of any artifact that integrates with a locked
> sibling artifact must include a unit test that cross-references
> concrete values against the sibling artifact's source.**

With the eight Manager-enumerated categories (MODEL_IDs, schema field
names, required manifest fields, CLI constants, mode names, context
names, framework-version behavior, artifact tags, provenance fields)
and the canonical example
(`test_model_id_matches_b1v2` reads `runner_b1_v2.py` via regex
extraction).

This rule complements the prior G1-open production rule:

| Rule | Catches |
|---|---|
| No production while G1-open condition memo affects it | wrapper-rewrite pattern defect (Senior correction memo G1-open at production) |
| Sibling-artifact cross-reference unit test | MODEL_ID drift; manifest-schema shape drift; CLI flag drift; etc. |

## 3. Review sequence remaining (per Manager memo §6)

```text
1. CS Path A.1 remediation — COMPLETE (this commit)
2. Senior intent-preservation review (design + provenance) — PENDING
3. Team Lead combined adversarial re-review — PENDING
4. CS lock-finalization touch (timestamp + any newly-approved notes) — PENDING
5. Manager reauthorization against final LOCK-RECORD hash — PENDING
6. CS preflight (now including test_model_id_matches_b1v2 in the
   implicit invariant set) — PENDING
7. CS execute the sweep — PENDING
```

The prior Manager authorization does NOT carry forward because the
locked artifact set and model identity changed.

## 4. Current state

```text
Path A.1 remediation:                COMPLETE
MODEL_ID:                            Qwen/Qwen2.5-3B-Instruct (matches B1 v2)
test_model_id_matches_b1v2:          PASSES
Tests:                               36/36 PASS
Standing rule addition:              FILED
LOCK-RECORD:                         5a3fbdf8... (PENDING_TEAM_LEAD_REVIEW)
B1 v2 source:                        UNEDITED
B1 v2.1:                             NOT CREATED OR USED
First data access:                   NOT EXECUTED
All non-Lane-1a execution gates:     CLOSED
```

CS posture: **HOLD for Senior intent-preservation review + Team Lead
combined adversarial re-review + Manager re-reauthorization.**

— CS Engineer, 2026-06-10
