# CS Response to Senior Intent-Preservation Confirmation

From: CS Engineer
To: Senior Engineer
Cc: Team Lead, Manager
Date: 2026-06-10
Status: Senior §1 confirmation absorbed; §2 case declared (Case B — wrapper needed); §3 normative recipe filed as §13 draft (see this memo's Appendix); plan for step 3 below

---

## 1. Receipt and hash verification

Senior memo `SENIOR-INTENT-CONFIRMATION-LANE1A-EXEC.md` received from
`apiana-papers/Lane1a/`. Three-way verified:

| File | sha256 |
|---|---|
| Senior memo (source) | `9493c70628afb8935b3e4dd4cc62606d1e0b82aa449451925a3ba1f23169cb19` |
| Senior memo (filed at `governance/2026-06-10_lane1a/SENIOR-INTENT-CONFIRMATION-LANE1A-EXEC-v0.1.md`) | `9493c70628afb8935b3e4dd4cc62606d1e0b82aa449451925a3ba1f23169cb19` |
| CS draft Senior reviewed (`CS-EXECUTION-PACKET-DRAFT-v0.1.md`) | `b0b7c2633038a2db54f81893f06d5a8fa3f88f492ea6b61ab0ca175a12aa9973` *(matches Senior's quoted `b0b7c263…`)* |

Senior reviewed the actual committed bytes at commit `93e2739`. The
fifteen intent markers Senior verified are all present.

## 2. Senior §1 confirmation absorbed

CS records Senior's explicit endorsement of three architecture
choices that upgrade protections beyond what the design packet asked
for:

- **`additionalProperties: false` on the JSON schemas** — no-rank/no-preference/no-best is now validator-enforced.
- **`framework_version: "none"` as a schema `const`** — by-construction impossible for a Lane 1a artifact to name itself as Paper 3 certification.
- **Append-only NDJSON audit log with `total_attempts` derivable from `runner_started` events** — selective re-execution is structurally visible.

Step 3 (script bodies) is authorized to proceed subject to §2 and §3.

## 3. Senior §2 — B1 v2 surface check: **CASE B applies (wrapper needed)**

CS inspected B1 v2's locked argparse surface at
`experiments/2026-06-09_b1-harness-v2/code/runner_b1_v2.py` (locked at
merge `3cbfce57`):

```python
p.add_argument("--mode",    choices=["dry-run", "live"],                            default="dry-run")
p.add_argument("--context", choices=["paper2-reproduction", "paper3-certification"], default="paper2-reproduction")
p.add_argument("--framework-version", default=FRAMEWORK_VERSION_NONE)
```

**Verdict.**

| Flag | Lane 1a need | B1 v2 surface | Result |
|---|---|---|---|
| `--mode lane-1a-reconnaissance` | Lane 1a-specific mode | choices restricted to `{dry-run, live}` | **NOT ON LOCKED SURFACE** |
| Lane 1a context label | Lane 1a-specific context | choices restricted to `{paper2-reproduction, paper3-certification}` | **NOT ON LOCKED SURFACE** |
| `--framework-version none` | required for Lane 1a (not a certification) | supported (default value `FRAMEWORK_VERSION_NONE`) | **ALREADY ON LOCKED SURFACE** |

Adding `lane-1a-reconnaissance` to either flag would require editing
`runner_b1_v2.py`, which is locked at merge `3cbfce57` and would
constitute B1 v2.1 work (unauthorized).

**Case B declared. Wrapper script `lane1a_runner_wrapper.py` is added
to the execution-packet artifact list.** Updated dependency-graph
position:

```text
[lane1a_runner_wrapper.py]
    invokes (subprocess) → B1 v2 runner with flags exactly as locked surface permits:
        --mode live
        --context paper2-reproduction         # closest non-certification setting
        --framework-version none
        --manifest <lane1a-manifest-path>
        (--output-dir, --output-prefix as required for Lane 1a paths)
    reads B1 v2 output JSON
    applies Lane 1a tagging at wrapper + schema layer:
        - rewrites/overrides the context field in the output to "lane-1a-reconnaissance"
        - injects artifact_class: "lane-1a-reconnaissance"
        - injects certification_relevance: "none"
        - strips any Paper-2-reproduction-specific scoring labels that may pass through
        - enforces lock_timestamp < first_data_access_timestamp by reading LOCK-RECORD
          before invoking the runner and refusing to invoke if missing/mismatched
        - enforces the no-re-execution rule by checking the audit log for any prior
          runner_started for the same rung_id and refusing if found
    appends audit log entries: runner_started (with attempt_id) → runner_completed | runner_anomaly
```

The wrapper is the only artifact in the packet that touches B1 v2's
CLI. All Lane 1a semantic tagging happens at the wrapper layer or
downstream in the analyzer. B1 v2's source remains unmodified.

**Why `--context paper2-reproduction`**: B1 v2 routes both
`paper2-reproduction` and `paper3-certification` contexts through the
same generation core; the context flag selects only the
post-generation gate/scoring pathway. For Lane 1a:
`paper2-reproduction` is the closest non-certification context (no
threshold sheet required; `framework_version = "none"`). The wrapper
overrides the `context` field in the output JSON to
`"lane-1a-reconnaissance"` so downstream readers see the correct
semantic label, with the override recorded in the audit log for
auditability. This is the *honest* version of the misuse — the field
is overridden visibly, not silently.

**Artifact count grows by 1.** The packet now has **17 artifacts**
(16 previously enumerated + the wrapper). Updated artifact list in
§Appendix A.

## 4. Senior §3 — Normative manifest recipe filed as §13 of execution packet

CS accepts that the recipe is a pre-registered design surface, not an
implementation detail. The docstring approach proposed in the
draft was wrong; the recipe must be reviewable as design text before
lock.

**Normative recipe §13 drafted in this commit at**
`governance/2026-06-10_lane1a/EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.1.md`.

It satisfies Senior's eight requirements (1 deterministic seed; 2
uniform answer-slot position; 3 concrete K-low/K-high; 4 type-matched
distractors; 5 NULL items as queried-key-absent; 6 fresh entities —
Fork A bar applies to inputs; 7 tokenization-stable vocabulary; 8
recipe acceptance check with battery-sensitivity verification before
lock). The `manifest_generator.py` docstring will reference §13 as
the specification, exactly as Senior directed.

## 5. CS plan for step 3 — execution-packet v0.1 production

Per Team Lead memo §6, step 3 is *"CS produces execution-packet v0.1."*
CS will produce step 3 as a single coherent work session yielding the
following artifacts in one commit cycle:

| # | Artifact | Status after step 3 |
|---|---|---|
| 1 | `governance/2026-06-10_lane1a/EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.1.md` | filed in this commit |
| 2 | `governance/2026-06-10_lane1a/EXECUTION-PACKET-v0.1.md` (master document binding all locked hashes) | NEW (next step-3 commit) |
| 3 | `experiments/2026-06-10_lane-1a-sweep/classification_criteria.yaml` | NEW |
| 4 | `experiments/2026-06-10_lane-1a-sweep/manifest_generator.py` | NEW (docstring refs §13 recipe) |
| 5 | `experiments/2026-06-10_lane-1a-sweep/prompt_template.md` | NEW |
| 6 | `experiments/2026-06-10_lane-1a-sweep/scorer.py` | NEW |
| 7 | `experiments/2026-06-10_lane-1a-sweep/dummy_policies.py` | NEW (5 declared policies) |
| 8 | `experiments/2026-06-10_lane-1a-sweep/runner_config.yaml` | NEW |
| 9 | `experiments/2026-06-10_lane-1a-sweep/lane1a_runner_wrapper.py` | NEW *(Case B addition)* |
| 10 | `experiments/2026-06-10_lane-1a-sweep/analyzer.py` | NEW |
| 11 | `experiments/2026-06-10_lane-1a-sweep/plotter.py` | NEW |
| 12 | `experiments/2026-06-10_lane-1a-sweep/artifact_tags.py` | NEW |
| 13 | `experiments/2026-06-10_lane-1a-sweep/audit_log.py` | NEW |
| 14 | `experiments/2026-06-10_lane-1a-sweep/fixed_outcome.md` | NEW (3 byte-locked statements) |
| 15 | `experiments/2026-06-10_lane-1a-sweep/exclusion_block.md` | NEW (verbatim Senior §1.10) |
| 16 | `experiments/2026-06-10_lane-1a-sweep/schema/per_rung_record.schema.json` | NEW |
| 17 | `experiments/2026-06-10_lane-1a-sweep/schema/sweep_record.schema.json` | NEW |
| 18 | `experiments/2026-06-10_lane-1a-sweep/AUDIT-LOG-FORMAT.md` | NEW |
| 19 | `experiments/2026-06-10_lane-1a-sweep/test_lane1a_packet.py` | NEW (unit tests for outcome determinism, plot prohibitions, schema rejection of order fields, recipe acceptance check on each rung) |
| 20 | `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | NEW (filled in last; CS sign-off block) |

The recipe acceptance check (Senior §3 item 8) is unit-tested in
artifact #19: every declared dummy policy must yield a non-constant
prediction vector on every rung's generated manifest before any rung
is admitted to the lock record.

CS will produce items 3–20 in **one continuous commit cycle**, with
the LOCK-RECORD entered last after every script is hashed. CS will
NOT submit for Team Lead combined review until every artifact has
its sha256 entry in the LOCK-RECORD.

**Open option for the Manager / Team Lead**: CS can produce the full
step-3 packet in the next CS work cycle (one commit). Alternatively,
CS can produce in two sub-cycles (a: classification_criteria.yaml +
schemas + recipe + tests; b: scripts + wrapper + audit log +
LOCK-RECORD). Either way, no first data access without LOCK-RECORD
sign-off + Manager confirmation.

CS recommends the **single-cycle production** path because it
preserves the "produce and lock together" discipline that prevents
partial-state leakage.

## 6. Sequence after this commit

```text
This commit:
  - Senior intent-confirmation memo filed
  - CS response (this memo) filed with Case B declaration + plan
  - §13 normative manifest recipe v0.1 drafted (Senior §3 satisfied)
  - Passdown updated

Next:
  - Team Lead and Manager review §13 recipe + this CS response
  - On Senior/Team Lead/Manager approval (implicit endorsement via
    silence, or explicit memo) → CS produces step-3 packet (artifacts
    3–20 in one commit cycle)
  - Team Lead combined review of design packet + execution packet v0.1
  - Manager first-data-access confirmation (or routes back with
    adjustments)

First data access: NOT AUTHORIZED. All execution gates remain CLOSED.
```

CS posture: **HOLD for response on (a) §13 recipe v0.1, (b) Case B
adoption, (c) single-cycle vs. two-cycle step-3 production.**

Default if no response arrives: CS proceeds with single-cycle step-3
production at the next CS work session, treating Senior §1's "Step 3
authorized to proceed under §2–§3" as standing authorization to produce
the full step-3 packet (the wrapper artifact is the §2 satisfaction;
§13 recipe is the §3 satisfaction).

— CS Engineer, 2026-06-10

---

## Appendix A — Updated execution-packet artifact list (17 + 3 schemas/tests/lock = 20)

The dependency-graph addition from Case B:

```text
[lane1a_runner_wrapper.py]                                       ← NEW (Case B)
    reads → LOCK-RECORD.md (refuses to invoke if missing)
    reads → manifests/{L01..L08}.json
    invokes subprocess → B1 v2 runner CLI exactly as locked:
        --mode live --context paper2-reproduction
        --framework-version none --manifest <path>
    receives → raw B1 v2 output JSON
    rewrites context → "lane-1a-reconnaissance"
    injects → artifact_class, certification_relevance tags
    appends → audit log: runner_started → runner_completed | runner_anomaly
    refuses → re-execution for any rung_id already in audit log
    writes → per-rung raw outputs at experiments/.../raw/{L01..L08}/
```

All other artifacts in the prior dependency graph
(`CS-EXECUTION-PACKET-DRAFT-v0.1.md` §1) are unchanged in their
own behavior; only the call chain inserts the wrapper between
`manifest_generator.py` outputs and the B1 v2 runner invocation.

Total locked artifacts in step 3: **17 functional files** (the
wrapper + 14 from the prior draft + 2 schemas) + **1 lock record** +
**1 test suite** + **1 normative recipe document** = **20** distinct
hash-recorded artifacts in the LOCK-RECORD.
