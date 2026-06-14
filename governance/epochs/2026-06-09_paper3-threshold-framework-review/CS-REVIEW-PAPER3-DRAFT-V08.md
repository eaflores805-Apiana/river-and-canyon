# CS Technical Review — Paper 3 Draft v0.8

**Date:** 2026-06-10
**From:** CS Engineer
**To:** Team Lead, Senior Engineer, Manager
**Re:** CS review of *Certification Before Retention* — Paper 3 draft v0.8
**Reviewed against:** v0.7 (last full CS review at `CS-REVIEW-PAPER3-DRAFT-V07.md`) and locked B1 v2 (merge `3cbfce5`)

---

## Record status

```
CS review filed.
v0.7 lock-blockers: remain resolved.
v0.8 is a focused precision pass — three governance-hardening additions
(D7 N_effective + void budget; §5 adjudication scope; D2 adversarial probes)
plus a three-layer artifact-separation cleanup in Appendix A.
Reference [4] NeurIPS pagination closed.
Four figures added.
Two new B1 v2.1 follow-up items (small; not blocking).
CS recommendation: v0.8 ready for Team Lead readiness check.
No candidate selected. No threshold values set. No runs authorized.
```

---

## Headline assessment

v0.8 is smaller in scope than v0.7 but lands three precisions that close real
loopholes. The two most important changes are governance-hardening:

1. **D7 N_effective + `max_voided_items` budget** — closes the "void to rescue
   marginal certification" loophole. Pre-registered void budget; fail-closed if
   exceeded; fail-closed if N_effective drops below sensitivity needs.
2. **§5 adjudication scope clause** — adjudication cannot modify pre-registered
   thresholds, cannot convert a failing gate into a pass. Preserves the
   fail-closed property under dispute.

Plus:

3. **D2 adversarial-probe requirement** — the battery must include at least one
   adversarial probe per shortcut family. Battery sensitivity is now demonstrable,
   not assumed.

CS recommendation: ready for Team Lead readiness check.

---

## Major v0.7 → v0.8 changes

### Governance hardening

**D7 N_effective and void budget.** Closes a real loophole. v0.7 said: "specify a
minimum detectable retention drop and show that the declared item count ... can
resolve it." v0.8 adds:

> *"D7 sensitivity is evaluated using **N_effective**, defined as N_declared
> minus voided items and missing required items. If voided or missing required
> items exceed the pre-registered `max_voided_items`, certification fails with
> `reason_code = void_budget_exceeded`; if N_effective no longer supports the
> pre-registered sensitivity calculation, D7 fails closed. This prevents a
> candidate from certifying at N_declared while silently evaluating at a smaller N."*

This is the kind of rule that is invisible if the protocol is never stressed but
load-bearing the first time a candidate is marginal. New threshold-sheet fields:
`max_voided_items` and `D7_N_effective_rule`.

**§5 adjudication scope.** Forecloses a back-door path:

> *"Adjudication resolves classification, evidence, and procedural disputes only.
> It may not modify any pre-registered threshold, margin, statistical test, or
> decision rule after candidate data is observed, and it may not convert a
> failing gate into a pass. Adjudication outcomes are fail-closed: an
> adjudication may void or fail a result, or require a new certification
> attempt, but may not rescue a failed gate."*

Without this clause, "borderline → adjudicate → pass" could undo the protocol's
discipline. v0.8 prevents this. §7 reinforces with a parallel statement.

**D2 adversarial probes.** Closes the "battery passed because items don't
trigger shortcuts" failure mode:

> *"The battery must include at least one adversarial probe per shortcut family,
> designed to elicit the shortcut if present; probe behavior must be recorded
> to demonstrate battery sensitivity."*

New threshold-sheet field: `D2_adversarial_probe_specs`. Sensitivity is now
demonstrable, not assumed.

### Architectural clarification — Appendix A three-layer separation

v0.8 explicitly separates pre-registration into three layers:

- **Threshold sheet** (A.1): pre-run commitments only.
- **`gate_summary` / evidence bundle** (A.2): post-run evidence.
- **Negative-certification report** (A.3): failure record.

Threshold-sheet path fields are now declared as *path patterns* (where things are
expected to live); actual paths are evidence-bundle outputs. Renamed fields in A.1
reflect this:

| v0.7 field | v0.8 field |
|---|---|
| `D2_per_item_contingency_table_path` | `D2_expected_contingency_table_artifact_path_pattern` |
| `D3_strict_content_gap_distribution` | `D3_expected_gap_distribution_artifact_path_pattern` |
| `D3_strict_content_confusion_matrix_path` | `D3_expected_confusion_matrix_artifact_path_pattern` |

The actual `_path` fields move to A.2's new "Evidence-bundle outputs (post-evaluation;
produced by the harness, not pre-registered)" section. Sound architecture — the
threshold sheet shouldn't carry post-run output paths.

### Per-item decision log schema (new in A.2)

v0.8 specifies a per-item decision log distinct from B1 v2's existing per-item
record. Fields include `D1_flag`, `D2_shortcut_verdicts`, `D3_strict_vs_content_delta`,
`D4_abstention_label`, `D5_difficulty_proxies`, plus per-item manifest/runner/scorer/
prompt hashes. See §"New B1 v2.1 follow-ups" below.

### Other v0.8 additions

- **D1 token-prior control construction specified.** v0.8 names two acceptable
  forms: null-context or scrambled-entity prompt-template variants, with the
  invariant "preserve format and output contract while removing task-relevant
  bindings." Closes the ambiguity about what counts as a valid control.
- **D6 firewall further refined.** New: *"Output-free validation of file existence,
  schema shape, or hash availability does not trigger the firewall."* Aligns with
  what B1 v2 already does at boot (`verify_locked_artifacts`).
- **Non-claims tightened.** New sentence in abstract, §6, and §9: *"Passing all
  gates does not predict that a future stress run will pass any stress-side
  precondition."* Stronger boundary; prevents over-reading certification as stress
  prediction.
- **Draft framework identifier not lock-eligible.** New constraint at the framework
  version block: *"`paper3-certification-protocol-v0.8` is **not yet lock-eligible**
  for threshold sheets; the released framework identifier becomes lock-eligible
  only at release."*
- **D5 standalone-vs-matched clarification.** v0.8 adds: standalone same-item
  certification may mark the matched-comparison subgate not applicable, but the
  identity check (manifest/item/prompt/scorer) remains required.
- **§3 fail-closed definition.** Defines the term canonically near first heavy use:
  *"defaulting to *not certified* unless every declared prerequisite is satisfied
  under the pre-registered decision rules."*

### Figures (1–4)

v0.8 adds four figures: series gap ladder (Fig 1), lineage→gates map (Fig 2),
fail-closed pipeline (Fig 3), three-artifact-layers (Fig 4). Files referenced as
`figures/fig*.png`. CS hasn't reviewed the image files; assuming they're in
Senior's working area pending publication packaging.

### Reference [4] NeurIPS pagination closed

The open editorial item from v0.6/v0.7 is resolved in v0.8:

> *"Advances in Neural Information Processing Systems 37 (NeurIPS 2024), Main
> Conference Track, 124347–124390. doi:10.52202/079017-3950."*

Also: author order corrected to `Dutta, A., Krishnan, S., Kwatra, N., and Ramjee, R.`
(Krishnan/Kwatra swapped vs. v0.7). Worth a quick verify-against-arXiv-or-proceedings
pass before final submission to confirm the corrected order matches the canonical
citation. Minor; Senior has presumably already done this.

---

## New B1 v2.1 follow-ups from v0.8 (not blocking)

| Item | Source | Disposition |
|---|---|---|
| `decoding_settings_hash` per gate record | v0.8 A.2 schema | One-line addition to `make_gate_record` at candidate authorization. |
| Per-item decision log (D1_flag, D2_verdicts, D3 delta, D4 label, D5 proxies) | v0.8 A.2 new section | Likely analysis-script layer over B1 v2's per-item output. Gate flags are candidate-specific (need threshold-sheet values), so unlikely to live in B1 v2 core. Worth scoping when a candidate is authorized — possibly a separate `analysis_b1_v2_paper3.py` script that consumes B1 output and emits the per-item decision log. |
| `N_effective` computation + `max_voided_items` enforcement | v0.8 D7 | Add to B1 gate evaluation logic at candidate authorization. Includes the `void_budget_exceeded` reason code. |
| Draft vs. released framework version naming check | v0.8 framework version block | Depends on Senior declaring release naming convention (e.g., release identifiers as `*-v1.0`). B1 can add a pattern check once convention is set. |

Plus carried forward from v0.7 review:

| Item | Source | Disposition |
|---|---|---|
| `evidence_artifact_path` per gate record | v0.7 A.2 schema | One-line addition to `make_gate_record` at candidate authorization. |

CS notes these in the B1 v2.1 backlog. All are deferrable; none impact the
locked B1 v2 state.

---

## Consistency check against locked B1 v2

| v0.8 surface | B1 v2 status |
|---|---|
| `framework_version` config-vs-sheet (no hardcoded literal) | ✓ Manager C2; B1-T17 |
| Harness-populated `first_candidate_data_access_timestamp` (UTC ISO-8601) | ✓ `now_utc_iso()` at manifest open |
| Threshold sheet content hash verified before content trust | ✓ Manager C3; B1-T18 |
| Firewall: triggers on functional access (manifest open) | ✓ B1-T21/T22 |
| Output-free firewall exemption (D6 v0.8 refinement) | ✓ Aligns with `verify_locked_artifacts` (hash-only check) |
| Threshold sheet content hash over JSON (not Markdown) | ✓ `load_threshold_sheet` calls `json.loads` |
| Per-item raw outputs retained | ✓ Per-item record carries `raw_output` |
| `framework_version` / `threshold_sheet_hash` / `analysis_script_hash` per gate | ✓ `make_gate_record` propagates |
| `decoding_settings_hash` per gate (NEW in v0.8) | **B1 v2.1** — small addition |
| `evidence_artifact_path` per gate (carried from v0.7) | **B1 v2.1** — small addition |
| Per-item decision log (D1–D5 flags per item) | **B1 v2.1** — analysis-script layer; candidate-specific |
| `N_effective` + `max_voided_items` enforcement | **B1 v2.1** — gate evaluation logic; candidate-specific |

No regressions; no v0.8 surface conflicts with B1 v2; all new spec needs map to
small B1 v2.1 patches at candidate authorization.

---

## Persisting items (still not blocking, same as v0.7)

1. **D6 §5/§7 cross-references for historical-knowledge shading.** Soft note
   from v0.3 → v0.8 unchanged. Senior's call.
2. **Reference [3] body still says "the same separation principle"** while §1
   inline says "general decomposed-scoring discipline." Minor inconsistency
   carried from v0.7. Possibly intentional preservation of canonical reference text.

---

## CS-side transparency

v0.8 was reviewed in full per the paper-revision cadence rule. No visibility gap.

---

## CS recommendation

v0.8 is ready for Team Lead readiness check from a CS standpoint.

The three governance-hardening precisions (D7 N_effective, §5 adjudication scope,
D2 adversarial probes) are well-targeted. The three-layer artifact separation in
Appendix A is sound architecture. The four B1 v2.1 follow-up items are small and
deferrable.

---

## Summary table

| Surface | Status |
|---|---|
| v0.3 / v0.6 / v0.7 CS lock blockers | All resolved; no regressions |
| §5 General decision rules + adjudication scope | Strengthened (adjudication may not rescue failed gates) |
| D2 adversarial-probe requirement | New; closes "battery insensitive" failure mode |
| D7 N_effective + void budget | New; closes "void to rescue" loophole |
| Appendix A three-layer separation | New; sound architecture |
| Reference [4] NeurIPS pagination | Closed |
| Figures 1–4 | Added (image files not reviewed by CS) |
| Non-claims | Tightened (no stress-side prediction from cert pass) |
| Draft framework identifier lock-eligibility | New; prohibits locking against drafts |
| Consistency with locked B1 v2 | Clean; 4 B1 v2.1 follow-ups (all deferrable) |
| Persisting soft notes | D6 §5/§7 cross-references; [3] inline/body wording inconsistency |

**CS recommendation:** v0.8 is ready for Team Lead readiness check from a CS
standpoint.

---

## Non-authorizations (carried forward)

```
candidate selection · threshold values · certification evaluation
new runs · re-runs beyond authorized reproduction validation
unconditioned token-prior runs · activation logging
INT8 / INT4 execution · multi-model execution
Fork A reactivation · Claim C activation
Paper 3 execution as an experiment · Paper 6 activation
public benchmark packaging · artifact mutation
```

---

— CS Engineer, 2026-06-10
