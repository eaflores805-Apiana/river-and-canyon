# Lane 1a Novelty Ledger (locked; per §13 recipe §6)

This ledger enumerates construction inputs that are FORBIDDEN as
sources for Lane 1a manifest construction. The Fork A bar applies to
inputs, not only to artifacts.

`manifest_generator.py` computes a `construction_inputs_hash` (sha256
of the union of value pool + K=low alphabet + K=high common-prefix-
family alphabet + NULL-decoy alphabet) and verifies overlap with the
items below does not exceed `MAX_HISTORICAL_OVERLAP_FRACTION = 0.05`.

## Forbidden source pools

### From the program record

- Paper 2 Cell01 / Cell02 / Cell03 manifests, items, entities, keys,
  values.
- Two-Hop L1 program manifests.
- Fork A artifacts (all): manifests, prompts, scorers, entity vocab.
- Any historical `paper2-reproduction` or `paper3-certification`
  artifact admitted to a release record.

### From external sources

- MMLU, HumanEval, MATH, GSM8K, ARC, BIG-Bench, HELM benchmarks.
- Any external dataset under `tier0-run/` that pre-dates this sweep.

## Lane 1a constructive vocabulary (declared NEW for this sweep)

The constructive vocabulary used by Lane 1a is generated fresh from
the per-rung seeds and the K-axis rules in `classification_criteria.yaml`.
The base alphabets are:

- **K=low alphabet:** lowercase Latin a-z (declared in YAML).
- **K=high common prefix:** drawn deterministically per rung from
  3-letter combinations of lowercase Latin (17,576 possibilities).
- **Suffixes:** drawn deterministically per rung.
- **Value pool:** declared in `classification_criteria.yaml` (the
  value pool is `["alpha","bravo","charlie","delta","echo","foxtrot",
  "golf","hotel","india","juliet","kilo","lima","mike","november",
  "oscar","papa","quebec","romeo","sierra","tango","uniform","victor",
  "whiskey","xray","yankee","zulu"]` — the NATO phonetic alphabet,
  uniform string format, no numeric content, used fresh for Lane 1a;
  not used in prior program artifacts).

## Lock-time verification

At lock time, `manifest_generator.py` performs:

1. Compute `construction_inputs_hash = sha256(value_pool || k_low_alphabet || k_high_common_prefix_pool || null_decoy_pool)`.
2. Read prior-program construction-input inventory (from this ledger).
3. Compute overlap fraction = |constructive_vocab ∩ prior_program_inputs| / |constructive_vocab|.
4. If overlap > 0.05, regenerate constructive vocabulary under a new seed and re-check, BEFORE lock.

Post-lock, this check is not re-run; the recorded
`construction_inputs_hash` in LOCK-RECORD.md is the audit anchor.

## Locked
Additions to this ledger are permitted (it records facts about prior work, not Lane 1a state).
Edits to the Lane 1a constructive vocabulary list above are prohibited after LOCK-RECORD seal.
