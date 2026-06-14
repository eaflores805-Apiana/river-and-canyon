# CS Execution Packet — Draft v0.1 (text-form, for Senior intent confirmation)

From: CS Engineer
To: Senior Engineer
Cc: Team Lead, Manager
Date: 2026-06-10
Status: Architecture + interfaces + locked constants in text form; awaiting Senior confirmation that modifications preserve design intent BEFORE CS writes locked artifact files

---

## 0. Purpose of this document

This is the **architecture-and-interfaces text** for the Lane 1a
execution packet, incorporating all six accepted CS design-constant
recommendations and all three accepted failure-mode mitigations. It is
the surface Senior reviews to confirm "modifications preserve design
intent" (Team Lead §6 step 2). It is **not yet** locked. CS produces
the actual artifact files only after Senior confirms.

The constants below are presented in machine-readable form so the
classification logic is unambiguous when CS hand-writes it into code.

---

## 1. Artifact inventory and dependency graph

```text
[manifest_generator.py]
    ├─ writes → manifests/{L01..L08}.json + MANIFEST-HASHES.lock
    └─ depends on → manifest_generator.py source hash
                     + lane1a_constants.yaml
                     + dummy_policies.py (offline policy correctness on each item)

[prompt_template.md]
[scorer.py]
[dummy_policies.py]
[runner_config.yaml]
    └─ refers to → model snapshot pin
                   prompt_template hash, scorer hash, dummy_policies hash

[analyzer.py]
    ├─ reads → per-rung raw outputs (one JSON per item)
    └─ writes → per-rung records (per_rung_record.schema.json)
                + sweep_record.json (sweep_record.schema.json)

[plotter.py]
    └─ reads → sweep_record.json
    └─ writes → fig_diagnostic_points.{png,svg} (8 panels — 1 per diagnostic axis)
                + fig_rung_label_grid.{png,svg}

[audit_log.py]
    └─ appends to → AUDIT-LOG.ndjson

[artifact_tags.py]
    └─ called by → analyzer, plotter, audit_log writes

[fixed_outcome.md, exclusion_block.md]
    └─ inserted verbatim into sweep_record.json and figure footers

[LOCK-RECORD.md]
    └─ artifact_name → sha256 → lock_timestamp
    └─ MUST exist with all hashes BEFORE first data access
```

All artifacts live under `experiments/2026-06-10_lane-1a-sweep/`, plus
the schemas under `schema/` and the LOCK-RECORD in the directory root.
Governance documents (the design packet, this draft, the lock record
copy, the Manager confirmation memo when issued) live under
`governance/2026-06-10_lane1a/`.

---

## 2. Locked constants (all six accepted CS recommendations applied)

Stored in `classification_criteria.yaml` and read by `analyzer.py`.
Every constant carries the `SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true`
flag in its entry.

```yaml
# classification_criteria.yaml (Lane 1a v0.1 — DRAFT — not yet locked)

doctrine: "Lane 1a may rule out; Lane 1a may not rule in."
artifact_class: "lane-1a-reconnaissance"
certification_relevance: "none"

constants:
  # CS recommendation 5a (Team Lead 3.1): explicit SE_diff formula
  se_diff_formula:
    expression: "sqrt(SE(strict)^2 + SE(control)^2)"
    se_strict_denom: "N_s_eff = 80 - void_count_strict"
    se_control_denom: "N_c_eff = 96 - void_count_control"
    SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true

  token_prior_indistinguishability:
    rule: "strict_acc - control_acc <= 2 * SE_diff"
    SE_multiplier: 2
    SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true

  declared_policy_envelope_indistinguishability:
    rule: "strict_acc <= union_envelope_score + 2 * SE(strict_acc)"
    SE_multiplier: 2
    SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true

  # CS recommendation 5b (Team Lead 3.2): N_effective definition
  insufficient_measurement_headroom:
    rule: "strict_acc >= 1 - 3 * SE(strict_acc, N_effective)"
    SE_multiplier: 3
    N_effective: "80 - void_count_strict"
    SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true

  strict_content_gap_instability:
    rule: "(strict_acc - content_acc) >= 0.15"
    gap_threshold: 0.15
    SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true

  abstention_contract_instability:
    rule: "NULL_stratum_abstention_rate NOT IN [0.50, 0.95] OR NULL/error not mechanically separable"
    band_low: 0.50
    band_high: 0.95
    null_stratum_size: 16
    SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true

  void_budget:
    rule: "void_count > 5 -> inconclusive_not_actionable"
    threshold: 5
    SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true

  ladder:
    rungs:
      L01: { D: 4,  K: "low",  X: "base" }
      L02: { D: 8,  K: "low",  X: "base" }
      L03: { D: 16, K: "low",  X: "base" }   # CS rec 5e: keep D=16 as top
      L04: { D: 4,  K: "high", X: "base" }
      L05: { D: 8,  K: "high", X: "base" }
      L06: { D: 16, K: "high", X: "base" }
      L07: { D: 8,  K: "low",  X: "extended" }
      L08: { D: 8,  K: "high", X: "extended" }
    # CS recommendation 5d (Team Lead 3.4): extended-context token count
    extended_context_target_tokens: 2048
    SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true

  per_rung_N:
    declared_total: 96
    answerable: 80
    null_stratum: 16
    token_prior_control: 96
    SWEEP_CLASSIFICATION_NOT_A_THRESHOLD_VALUE: true

# CS recommendation 5f (Team Lead 3.6) + failure-mode 6a: no re-execution rule
re_execution_rule:
  policy: "no_re_execution_within_sweep"
  text: |
    A rung labeled inconclusive_not_actionable is not re-run within this
    sweep. A re-sweep on that rung requires fresh Manager authorization.
  total_attempts_logged: true   # audit log captures every execution attempt
```

---

## 3. Label assignment logic (code-level deterministic)

In `analyzer.py`, exactly one logical pass per rung. Pseudocode:

```python
def assign_labels(rung_record):
    labels = []

    # Token-prior indistinguishability
    se_strict   = sqrt(rung_record.strict_acc * (1 - rung_record.strict_acc) / rung_record.N_s_eff)
    se_control  = sqrt(rung_record.control_acc * (1 - rung_record.control_acc) / rung_record.N_c_eff)
    se_diff     = sqrt(se_strict**2 + se_control**2)
    if (rung_record.strict_acc - rung_record.control_acc) <= 2 * se_diff:
        labels.append("accuracy_indistinguishable_from_token_prior")

    # Declared-policy envelope indistinguishability
    if rung_record.strict_acc <= rung_record.union_envelope_score + 2 * se_strict:
        labels.append("accuracy_indistinguishable_from_declared_policy_envelope")

    # Insufficient measurement headroom
    if rung_record.strict_acc >= 1 - 3 * se_strict:   # SE recomputed at N_effective
        labels.append("insufficient_measurement_headroom")

    # Strict-content gap instability
    if (rung_record.strict_acc - rung_record.content_acc) >= 0.15:
        labels.append("strict_content_gap_instability")

    # Abstention contract instability
    null_rate = rung_record.abstention_rate
    if not (0.50 <= null_rate <= 0.95) or not rung_record.separability_flag:
        labels.append("abstention_contract_instability")

    # Void budget (precedence: this can attach independently)
    if rung_record.void_count > 5:
        labels.append("inconclusive_not_actionable")

    # Missing required outputs / harness anomaly
    if rung_record.harness_anomaly_flag:
        if "inconclusive_not_actionable" not in labels:
            labels.append("inconclusive_not_actionable")

    # Neutral label: attached iff and only if no other label attaches
    if len(labels) == 0:
        labels.append("requires_further_investigation")

    return sorted(labels)   # alphabetical, never by "quality"
```

Notes:

- Labels are **multi-attach** except `requires_further_investigation`,
  which is mutually exclusive with all others and means *only* "not
  ruled out under this sweep."
- The label list is sorted alphabetically (not by quality) before
  being written to the per-rung record.
- No label has a numeric "score." Survivor set membership is binary.

---

## 4. Outcome-statement deterministic rule (CS failure-mode 6b)

In `fixed_outcome.md` and enforced by `analyzer.py` after all rungs
classified:

```python
def emit_outcome(sweep_record):
    survivors = [
        r for r in sweep_record.rungs
        if r.labels == ["requires_further_investigation"]
    ]
    K = len(survivors)

    if K == 0:
        statement = STATEMENT_A_VERBATIM       # "The certification window, while logically nonempty, was unoccupied for this task family at this scale: every rung carried at least one elimination label under the pre-registered sweep classification."
    else:
        statement = STATEMENT_B_VERBATIM_WITH_K.format(K=K)   # "K of 8 rungs were not ruled out under the pre-registered sweep classification and remain an unordered survivor set. Survivorship is neither ranking nor positive evidence; certification eligibility remains undetermined pending separately authorized candidate selection and certification."

    statement += "\n\n" + STATEMENT_C_VERBATIM   # always-append: winner's-curse warning

    return statement
```

Three constants (`STATEMENT_A_VERBATIM`, `STATEMENT_B_VERBATIM_WITH_K`,
`STATEMENT_C_VERBATIM`) live in `fixed_outcome.md` byte-locked. The
code path **cannot** synthesize alternative wording — the templates are
the only strings emitted. CS will additionally write a unit test
asserting that no other string can be produced by `emit_outcome` under
any input.

---

## 5. Plot prohibition enforcement (CS failure-mode 6c)

In `plotter.py`, the prohibited forms become explicit refusals:

```python
class Lane1aPlotter:
    ALLOWED_FIGURE_TYPES = {
        "per_rung_diagnostic_points",     # 1 panel per diagnostic axis
        "rung_label_categorical_grid",    # rung × label categorical markers
    }

    def __init__(self):
        # Code-level refusals — assertion at every prohibited entry point.
        self.refusals = {
            "heatmap":                  "Prohibited per design packet §1.8",
            "contour":                  "Prohibited per design packet §1.8",
            "smoothed_curve":           "Prohibited per design packet §1.8",
            "fitted_boundary":          "Prohibited per design packet §1.8",
            "threshold_line":           "Prohibited per design packet §1.8",
            "certification_band":       "Prohibited per design packet §1.8",
            "viability_overlay":        "Prohibited per design packet §1.8",
            "promising_region":         "Prohibited per design packet §1.8",
            "ranked_cluster":           "Prohibited per design packet §1.8",
        }

    def draw(self, figure_type, **kwargs):
        if figure_type in self.refusals:
            raise NotImplementedError(
                f"{figure_type}: {self.refusals[figure_type]}"
            )
        if figure_type not in self.ALLOWED_FIGURE_TYPES:
            raise NotImplementedError(
                f"{figure_type}: not in ALLOWED_FIGURE_TYPES; "
                f"Lane 1a allows only {sorted(self.ALLOWED_FIGURE_TYPES)}"
            )
        # ... allowed-figure implementations ...

    def _draw_per_rung_diagnostic_points(self, axis, rungs):
        # x-axis: rung order L01..L08 (ladder order)
        # y-axis: the diagnostic axis value
        # markers only; no lines; no smoothing; no shaded regions
        # footer: artifact_tag block (mandatory; injected by artifact_tags.py)
        ...

    def _draw_rung_label_categorical_grid(self, sweep_record):
        # rows: labels (in alphabetical order)
        # cols: rungs L01..L08 (ladder order; NEVER sorted by statistic)
        # cells: discrete categorical marker (filled = label attached)
        # footer: artifact_tag block + fixed outcome statement
        ...
```

The plot footer is non-skippable: `plotter.py` calls
`artifact_tags.get_tag_footer()` at every `savefig`, which embeds the
two-tag pair plus the fixed-outcome statement plus a truncation of the
exclusion block. The figure cannot be saved without this footer.

CS unit tests will verify:
- Every prohibited figure type raises `NotImplementedError` with a
  message naming the design-packet section.
- Every allowed figure type emits the artifact-tag footer.
- The categorical grid is plotted in ladder order (L01..L08), not in
  any order derived from a statistic.

---

## 6. Per-rung record schema (locked, hash-recorded)

In `schema/per_rung_record.schema.json` (JSON Schema draft 2020-12):

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Lane 1a per-rung record",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "rung_id", "manifest_hash", "N_declared", "N_effective",
    "void_count", "strict_acc", "strict_acc_se",
    "content_acc", "gap",
    "control_acc", "control_acc_se",
    "max_dummy_score", "union_envelope_score",
    "headroom",
    "abstention_rate", "abstention_rate_se",
    "separability_flag", "tokenization_stability_flag",
    "harness_anomaly_flag",
    "labels", "per_item_log_path", "raw_output_dir",
    "artifact_class", "certification_relevance"
  ],
  "properties": {
    "rung_id": { "enum": ["L01","L02","L03","L04","L05","L06","L07","L08"] },
    "manifest_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "N_declared": { "const": 96 },
    "N_effective": { "type": "integer", "minimum": 0, "maximum": 96 },
    "void_count": { "type": "integer", "minimum": 0 },

    "strict_acc": { "type": "number", "minimum": 0, "maximum": 1 },
    "strict_acc_se": { "type": "number", "minimum": 0 },
    "content_acc": { "type": "number", "minimum": 0, "maximum": 1 },
    "gap": { "type": "number" },
    "control_acc": { "type": "number", "minimum": 0, "maximum": 1 },
    "control_acc_se": { "type": "number", "minimum": 0 },
    "max_dummy_score": { "type": "number", "minimum": 0, "maximum": 1 },
    "union_envelope_score": { "type": "number", "minimum": 0, "maximum": 1 },
    "headroom": { "type": "number" },

    "abstention_rate": { "type": "number", "minimum": 0, "maximum": 1 },
    "abstention_rate_se": { "type": "number", "minimum": 0 },   /* CS rec 5c */
    "separability_flag": { "type": "boolean" },
    "tokenization_stability_flag": { "type": "boolean" },
    "harness_anomaly_flag": { "type": "boolean" },

    "labels": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "enum": [
          "accuracy_indistinguishable_from_token_prior",
          "accuracy_indistinguishable_from_declared_policy_envelope",
          "insufficient_measurement_headroom",
          "strict_content_gap_instability",
          "abstention_contract_instability",
          "inconclusive_not_actionable",
          "requires_further_investigation"
        ]
      }
    },

    "per_item_log_path": { "type": "string" },
    "raw_output_dir": { "type": "string" },

    "artifact_class": { "const": "lane-1a-reconnaissance" },
    "certification_relevance": { "const": "none" }
  }
}
```

**Schema-level protections (note the absence):** there is **no** field
named `rank`, `sort_by`, `preference`, `best`, `quality_score`,
`recommended`, or any synonym. `additionalProperties: false` means any
attempt to write such a field at JSON-validate time raises a
SchemaValidationError. This is the schema/code-class enforcement of
the doctrine.

---

## 7. Sweep-level record schema (locked, hash-recorded)

In `schema/sweep_record.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Lane 1a sweep record",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "sweep_id", "framework_version", "model_attestation",
    "lock_record_hash", "classification_criteria_hash",
    "manifest_generator_hash", "scorer_hash",
    "dummy_policies_hash", "analyzer_hash", "plotter_hash",
    "prompt_template_hash", "runner_config_hash",
    "lock_timestamp", "first_data_access_timestamp",
    "sweep_complete_timestamp", "total_attempts",
    "rungs", "survivors", "K",
    "fixed_outcome_statement", "exclusion_block",
    "artifact_class", "certification_relevance"
  ],
  "properties": {
    "sweep_id": { "const": "lane-1a-2026-06-10" },
    "framework_version": { "const": "none" },
    "model_attestation": { "type": "object" },
    "lock_record_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "classification_criteria_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "manifest_generator_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "scorer_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "dummy_policies_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "analyzer_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "plotter_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "prompt_template_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "runner_config_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },

    "lock_timestamp": { "type": "string", "format": "date-time" },
    "first_data_access_timestamp": { "type": "string", "format": "date-time" },
    "sweep_complete_timestamp": { "type": "string", "format": "date-time" },
    "total_attempts": { "type": "integer", "minimum": 8 },

    "rungs": {
      "type": "array",
      "items": { "$ref": "per_rung_record.schema.json" },
      "minItems": 8,
      "maxItems": 8
    },

    "survivors": {
      "type": "array",
      "uniqueItems": true,
      "items": { "enum": ["L01","L02","L03","L04","L05","L06","L07","L08"] }
    },
    "K": { "type": "integer", "minimum": 0, "maximum": 8 },

    "fixed_outcome_statement": { "type": "string" },
    "exclusion_block":         { "type": "string" },

    "artifact_class":          { "const": "lane-1a-reconnaissance" },
    "certification_relevance": { "const": "none" }
  }
}
```

Three protections worth calling out:

- **`framework_version: "none"`** is a `const`. The Lane 1a sweep
  cannot accidentally name itself `paper3-certification-protocol-v1.1`
  in a way that would let a future tool confuse it with certification.
- **`survivors` enum** restricts to rung IDs only — no scores, no
  preference fields.
- **`first_data_access_timestamp` MUST postdate `lock_timestamp`** —
  this is enforced by `runner_config.yaml` at runtime, and the
  analyzer additionally asserts `first_data_access_timestamp >
  lock_timestamp` before writing the sweep record.

---

## 8. Audit log format (CS failure-mode 6a / total-attempt count)

In `AUDIT-LOG-FORMAT.md` + `audit_log.py`:

NDJSON, append-only. Each line is one event. Field schema:

```json
{
  "ts": "RFC 3339 with milliseconds",
  "event": "lock_record | manifest_generated | runner_started | runner_completed | runner_anomaly | analysis_started | analysis_completed | plot_generated | sweep_complete",
  "rung_id": "L01..L08 or null",
  "attempt_id": "integer (1..N)",
  "details": { "artifact_class": "lane-1a-reconnaissance", ... }
}
```

`runner_started` and `runner_anomaly` together let CS reconstruct
`total_attempts` by summing all `event == "runner_started"` entries.
`runner_completed` indicates a clean execution; `runner_anomaly`
indicates the rung is destined for `inconclusive_not_actionable` and
no re-execution is permitted within this sweep.

The audit log is the artifact whose append-only-ness lets a future
auditor distinguish *"one attempt per rung"* from *"selective
re-execution after seeing a result."*

---

## 9. Lock-record format

In `LOCK-RECORD.md`:

```text
# Lane 1a Lock Record — 2026-06-10

Sweep ID: lane-1a-2026-06-10
Framework version (declared): none  (Lane 1a is NOT a certification)
Doctrine: "Lane 1a may rule out; Lane 1a may not rule in."

| Artifact | sha256 | lock_timestamp |
|---|---|---|
| classification_criteria.yaml | <64-hex> | <RFC3339> |
| manifest_generator.py        | <64-hex> | <RFC3339> |
| prompt_template.md           | <64-hex> | <RFC3339> |
| scorer.py                    | <64-hex> | <RFC3339> |
| dummy_policies.py            | <64-hex> | <RFC3339> |
| runner_config.yaml           | <64-hex> | <RFC3339> |
| analyzer.py                  | <64-hex> | <RFC3339> |
| plotter.py                   | <64-hex> | <RFC3339> |
| artifact_tags.py             | <64-hex> | <RFC3339> |
| audit_log.py                 | <64-hex> | <RFC3339> |
| fixed_outcome.md             | <64-hex> | <RFC3339> |
| exclusion_block.md           | <64-hex> | <RFC3339> |
| per_rung_record.schema.json  | <64-hex> | <RFC3339> |
| sweep_record.schema.json     | <64-hex> | <RFC3339> |

CS sign-off: <CS engineer attestation block>
First-data-access-timestamp constraint: > max(lock_timestamp)
B1 v2.1: NOT USED
```

The lock record is what Manager confirms before authorizing first data
access (Team Lead §7 step 3 + step 5). After this record is sealed,
**no edit to any listed artifact** is permitted — corrections go via a
new lock record on a separately-authorized re-sweep.

---

## 10. Notable interlock with B1 v2 provenance

The runner config uses B1 v2 capabilities only. Specifically:

- `--mode lane-1a-reconnaissance` (a Lane-1a-specific mode that does
  not run any Paper 3 certification gate)
- `--framework-version none` (Lane 1a is not framework-locked; the
  sweep record records `framework_version: "none"` as a `const`)
- Model snapshot pin via runner-attestation (B1 v2 captures the
  model identity hash at execution time)
- Prompt template, scorer, and dummy-policies hashes embedded in the
  runner config; B1 v2 validates these against the lock record at
  startup

B1 v2.1 capabilities (e.g., supersession-rule enforcement, lane-1a-
tagged-reference rejection in threshold sheets) are **not used and
not authorized**. The Lane 1a enforcement in this packet is
schema/code-class against B1 v2 + locked offline scripts.

---

## 11. Six failure-mode mitigations (combined Senior §2 + CS additions)

| # | Failure path | Structural mitigation (Senior §2 + CS) | Residual / enforcement vehicle |
|---|---|---|---|
| 1 | Reconnaissance → pre-selection | Unordered-set serialization; ladder-order-only presentation; no rank/preference/best fields in schema; label-only conclusions; fixed outcome language | Candidate Selection Memo's required justification on construction-design grounds; Manager review of that memo; §1.10 exclusion attestation |
| 2 | Diagnostic artifact → positive evidence | `artifact_class: lane-1a-reconnaissance` + `certification_relevance: none` on every record and figure; exclusion block embedded in outputs; figure footer non-skippable | B1 v2.1 backlog: reject lane-1a-tagged references in threshold sheets; interim: manual threshold review |
| 3 | Unordered survivors → implicit ranking | Survivor set has no order field; plots never sort by statistic; neutral label binary-attached; timestamps encode pre-registered ladder order only | Schema validator (`additionalProperties: false`) blocks injection of order fields |
| 4 | Visual layout → "good region" | Locked plotting scripts; enumerated prohibitions encoded as `NotImplementedError`; categorical palette; per-axis panels not composite "maps"; artifact-tag footer + fixed outcome statement directly beneath grid | Figures cannot be excerpted without the non-claim — footer is non-skippable |
| 5 | Lane 1a → threshold contamination | §1.10 carve-out from D6 historical-information allowance; required attestation; classification constants tagged NOT-A-THRESHOLD at every occurrence | Role separation at the future threshold sheet (author ≠ analyst where staffing permits; recorded exception otherwise); attestation as artifact |
| 6 | Descriptive label → gate verdict | Label names contain no gate identifiers; label→gate mapping is absent from sweep outputs; commit-message template fixed; EXPERIMENT_LOG entry template fixed | Audit-log review at sweep completion can scan for any label drift |
| 7 *(CS 6a)* | Selective re-execution → backdoor selection | No-re-execution rule encoded in runner config; audit log captures every attempt (success + anomaly); sweep-level `total_attempts` exposed in schema | A re-sweep requires fresh Manager authorization with its own lock record |
| 8 *(CS 6b)* | Outcome-statement discretion | Three byte-locked statements in `fixed_outcome.md`; deterministic selection rule; unit test asserts no alternative string can be emitted | Schema requires `fixed_outcome_statement` field; mismatch raises validation error |
| 9 *(CS 6c)* | Plot prohibition drift | `NotImplementedError` per prohibited form; unit tests assert each prohibition raises; `ALLOWED_FIGURE_TYPES` enumerated | Future maintainer cannot silently add a heatmap — CI catches the test failure |

---

## 12. What CS will write after Senior confirmation

Once Senior confirms this draft preserves design intent, CS will create:

| Path | Status |
|---|---|
| `experiments/2026-06-10_lane-1a-sweep/manifest_generator.py` | new |
| `experiments/2026-06-10_lane-1a-sweep/prompt_template.md` | new |
| `experiments/2026-06-10_lane-1a-sweep/scorer.py` | new |
| `experiments/2026-06-10_lane-1a-sweep/dummy_policies.py` | new |
| `experiments/2026-06-10_lane-1a-sweep/runner_config.yaml` | new |
| `experiments/2026-06-10_lane-1a-sweep/analyzer.py` | new |
| `experiments/2026-06-10_lane-1a-sweep/plotter.py` | new |
| `experiments/2026-06-10_lane-1a-sweep/artifact_tags.py` | new |
| `experiments/2026-06-10_lane-1a-sweep/audit_log.py` | new |
| `experiments/2026-06-10_lane-1a-sweep/fixed_outcome.md` | new |
| `experiments/2026-06-10_lane-1a-sweep/exclusion_block.md` | new |
| `experiments/2026-06-10_lane-1a-sweep/classification_criteria.yaml` | new |
| `experiments/2026-06-10_lane-1a-sweep/schema/per_rung_record.schema.json` | new |
| `experiments/2026-06-10_lane-1a-sweep/schema/sweep_record.schema.json` | new |
| `experiments/2026-06-10_lane-1a-sweep/AUDIT-LOG-FORMAT.md` | new |
| `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` | new (filled in after CS sign-off) |
| `experiments/2026-06-10_lane-1a-sweep/test_lane1a_packet.py` | new (unit tests for outcome determinism, plot prohibitions, schema rejection of order fields) |
| `governance/2026-06-10_lane1a/EXECUTION-PACKET-v0.1.md` | new (master document binding all locked hashes) |

All hash-locked in `LOCK-RECORD.md`. No file is committed without its
sha256 entered in the lock record. The CS sign-off block in
`LOCK-RECORD.md` is the artifact Manager confirms.

---

## 13. Open question for Senior

CS believes the architecture preserves design intent on all six
constants and all three additional failure-mode mitigations. **One
clarification CS would value before locking script bodies:**

- **Manifest construction:** Senior §1.2 says "single-hop key→value
  retrieval over freshly constructed synthetic entity manifests
  (hop2-class family)." CS will implement the manifest generator
  using a deterministic synthetic-entity construction analogous to
  the Two-Hop L1 cell manifests (in spirit), but parameterized for
  Lane 1a (D distractors, K low/high confusability, X base/extended).
  **Is there a specific manifest-construction recipe Senior wants CS
  to follow, or should CS produce a CS-internal recipe in the
  manifest_generator.py file's docstring for Senior to review at
  lock time?**

If Senior has no preference, CS will document the recipe in the
docstring and bring it to lock-time review as a normal
construction-detail decision.

---

## 14. Current state at end of draft

```text
Design packet v0.1:                ACCEPTED (Team Lead 2026-06-10)
CS 6 design-constant recommendations: ACCEPTED (Team Lead 3.1–3.6)
CS 3 failure-mode mitigations:     ACCEPTED (Team Lead 4.1–4.3)
CS execution-packet DRAFT (text):  FILED (this document)
Senior intent-preservation review:  PENDING
CS execution-packet v0.1 (files):  WAITING on Senior confirmation
LOCK-RECORD:                       NOT CREATED
Team Lead combined review:         PENDING
Manager first-data-access auth:    PENDING
First data access:                 NOT AUTHORIZED
```

CS posture: **HOLD for Senior intent-preservation confirmation.** Next
CS event triggered by Senior confirming this draft (or routing back
with adjustments).

— CS Engineer, 2026-06-10
