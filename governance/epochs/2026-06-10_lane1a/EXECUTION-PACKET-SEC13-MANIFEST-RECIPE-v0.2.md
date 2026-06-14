# Execution Packet §13 — Normative Manifest Construction Recipe (v0.2; B3 amendment applied)

From: CS Engineer
Date: 2026-06-10
Status: v0.2 supersedes v0.1 for Step-3 production; B3 control-prompt-stratum amendment incorporated; all other v0.1 content holds verbatim

---

## 0. Diff vs. v0.1

Single substantive change relative to v0.1: a §12 amendment documenting
that each rung's 96-prompt token-prior control is partitioned into 80
**answerable-mirror** controls (one per answerable item) and 16
**NULL-mirror** controls (one per NULL item). The recipe still
generates 96 controls per rung; downstream scoring uses only the 80
answerable-mirror partition for `control_acc` and `control_acc_se`
(B3 from design packet v0.3). The NULL-mirror controls are retained as
descriptive abstention-prior data and enter no accuracy statistic.

This is a tagging amendment, not a construction-rule change. The §1–§11
content of v0.1 holds verbatim; §10 is updated to reference §12.

## 1.–11. (unchanged)

See `EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.1.md` at commit `48ee825`
for §1 (determinism), §2 (uniform answer-slot position), §3 (K-axis
low/high definitions), §4 (type-matched distractors), §5 (NULL items),
§6 (fresh entities / novelty ledger), §7 (tokenization stability),
§8 (recipe acceptance check), §9 (lock-blocking summary),
§10 (`manifest_generator.py` outputs — superseded by §10 below), and
§11 (open question — closed at intent confirmation).

## 10. What `manifest_generator.py` will produce (REVISED for B3)

Per-rung manifest JSON now contains TWO parallel item lists:

```text
items = {
  "answerable":  [ 80 items: queried_key in in_context_keys ],
  "null":        [ 16 items: queried_key NOT in in_context_keys ]
}

controls = {
  "answerable_mirror": [ 80 items: scrambled bindings, queried_key in in_context_keys (token-prior null for answerable stratum) ],
  "null_mirror":       [ 16 items: scrambled bindings, queried_key NOT in in_context_keys (descriptive abstention-prior) ]
}
```

Each control item carries `control_class: "answerable_mirror"` or
`control_class: "null_mirror"` so the analyzer can partition without
re-deriving from item-IDs.

Outputs (per rung):

- `manifests/{L01..L08}.json` — full manifest with both partitions
- `manifests/MANIFEST-HASHES.lock` — one-line-per-rung sha256
- `manifests/RECIPE-ACCEPTANCE-CHECK-RESULTS.json` — per-rung
  acceptance record (recipe-§8 dummy-policy non-degeneracy verified on
  the 80 answerable items)
- `manifests/NOVELTY-LEDGER-CHECK.md` — confirmation that construction
  inputs cleared the novelty-ledger check at lock time

## 12. B3 amendment — control-prompt-stratum tagging (NEW in v0.2)

**Statement.** The token-prior control set has 96 prompts per rung
(matching N_declared = 96 = 80 answerable + 16 NULL by parallel
construction). However, *scoring* uses only the 80 answerable-mirror
prompts.

**Construction.** For each rung, the manifest generator produces 96
control prompts in two strata:

1. **80 `answerable_mirror` controls.** One per answerable item.
   Construction: identical prompt template, identical format
   contract, identical in-context-list length (D+1 entries), but the
   key→value bindings are deterministically scrambled (each key in
   the in-context list is paired with a different value drawn from
   the value pool, never matching the original binding). The queried
   key remains in the in-context list (so a token-prior model would
   "answer correctly" by chance proportional to value-pool overlap).
   This control measures the token-prior baseline for the answerable
   stratum.
2. **16 `null_mirror` controls.** One per NULL item. Construction:
   same scrambling; the queried key remains absent from the
   in-context list. Descriptive only: a scrambled-binding NULL has no
   well-defined "correct" answer (the model should abstain, but the
   "correct" abstention rate under scrambling is ill-defined and not
   used by any classification rule). Retained as abstention-prior
   data to feed `abstention_rate_se` characterization.

**Scoring.** `control_acc` and `control_acc_se` are computed over the
80 answerable-mirror controls only:

```python
control_acc      = sum(strict_correct(item) for item in answerable_mirror) / 80
N_c_eff          = 80 - void_count_control_answerable_mirror
control_acc_se   = sqrt(control_acc * (1 - control_acc) / N_c_eff)
```

The 16 `null_mirror` controls are NOT entered into `control_acc`,
`control_acc_se`, or `SE_diff`. They are recorded in the per-rung
raw-output directory and appear in the audit log, but they do not
affect any classification rule.

**Void budget.** Per design packet v0.3 §1.6, the per-rung void
budget of 5 counts ALL voids (answerable + NULL + both control strata).
A rung whose total void count > 5 attaches
`inconclusive_not_actionable` and (by B2 preempt) no other label.

**Generation count.** Per rung: 80 answerable + 16 NULL + 80
answerable_mirror + 16 null_mirror = 192 generations. Across 8 rungs:
1,536 — matching B5's `planned_generation_count` under Path A (Option A
authorization).

## 13. (renumbered from v0.1's §11) Open question — closed at intent confirmation

CS has no remaining open question against the recipe; Senior intent
confirmation §3 closed the recipe-design surface.

---

— CS Engineer, 2026-06-10
