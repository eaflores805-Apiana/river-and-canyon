# PROVENANCE-GAP-DISPOSITION.md

**Date:** 2026-06-07
**Owner:** CS Engineer
**Purpose:** Final provenance gap disposition for Paper 1 v1.0 lock
**Requested by:** Elias, Manager (memo: "Final provenance-gap disposition needed for Paper 1 v1.0")

---

## Artifact inspection basis

All dispositions below are based on direct JSON artifact inspection performed 2026-06-07.
No reruns were performed. No missing artifacts were reconstructed as original provenance.

| Artifact | Top-level keys confirmed present |
|---|---|
| `stability_screen_1780771434.json` (Exp6) | `model`, `tasks`, `results` — no hash or decoding fields |
| `stability_screen_1780776502.json` (Exp7) | `model`, `tasks`, `tasks_manifest_hash`, `fresh_generation`, `screen_timestamp`, `results` |
| `fp16_screen_exp8_arm2_1780781863.json` (Exp8A) | `manifest_hash`, `decoding` present; scorer/tokenizer/runner hashes absent; item keys lack `scaffold_class` |

---

## Disposition table

### Exp6

| Gap | Disposition | Artifact path / hash | Recommended manuscript wording |
|---|---|---|---|
| tokenizer_hash absent | NOT RECOVERABLE | — | "Tokenizer hash was not stored in the Exp6 result artifact. Tokenizer identity is established by model tag only (Qwen/Qwen2.5-1.5B-Instruct)." |
| runner_hash absent | NOT RECOVERABLE | — | "Runner hash was not stored in the Exp6 result artifact and cannot be recovered post-hoc. Runner identity is established by source inspection of `run_stability_screen.py` only." |
| scorer_hash absent | NOT RECOVERABLE | — | "Scorer hash was not stored in the Exp6 result artifact and cannot be recovered post-hoc." |
| decoding settings not in artifact | SHIP AS DOCUMENTED GAP | `run_stability_screen.py` (current hash: `sha256:4588bc7e98fc78906b093b7707304ef5e4b53ba2268de28c29ea68dd8157d647`); `--max-tokens` default=512, `temp=0.0` hardcoded via `make_sampler` | "Decoding settings (temperature=0.0, max_tokens=512) for Exp6 were reconstructed from source inspection of `run_stability_screen.py` and are not stored in the result JSON artifact." |

---

### Exp7

| Gap | Disposition | Artifact path / hash | Recommended manuscript wording |
|---|---|---|---|
| tokenizer_hash absent | NOT RECOVERABLE | — | "Tokenizer hash was not stored in the Exp7 result artifact. Tokenizer identity is established by model tag only (Qwen/Qwen2.5-1.5B-Instruct)." |
| runner_hash absent | NOT RECOVERABLE | — | "Runner hash was not stored in the Exp7 result artifact and cannot be recovered post-hoc. Runner identity is established by source inspection of `run_stability_screen.py` only." |
| scorer_hash absent | NOT RECOVERABLE | — | "Scorer hash was not stored in the Exp7 result artifact and cannot be recovered post-hoc." |
| decoding settings not in artifact | SHIP AS DOCUMENTED GAP | `run_stability_screen.py` (same source as Exp6) | "Decoding settings (temperature=0.0, max_tokens=512) for Exp7 were reconstructed from source inspection of `run_stability_screen.py` and are not stored in the result JSON artifact." |

**Note:** Exp7 manifest hash IS present in the artifact: `sha256:177c5f7f1fa39d902fafe4974e5d449f005e6200fe5101efb54b25186096f20e`. This is the only hash field present.

---

### Exp8A

| Gap | Disposition | Artifact path / hash | Recommended manuscript wording |
|---|---|---|---|
| scorer_hash absent (pre-amendment) | NOT RECOVERABLE | — | "Exp8A ran before the three-axis scorer (`tasks_exp8.py`, `sha256:4036b1ad...`) was locked. The pre-amendment two-axis scorer used at run time is not the currently locked scorer; its hash was not recorded and cannot be recovered post-hoc." |
| scaffold_class absent from items | NOT RECOVERABLE | — | "Exp8A ran before the scaffold axis was added to the scorer. `scaffold_class` is absent from all Exp8A result items. Exp8A was not rescored under the amended scorer." |
| Numeric failures (L2_02, L2_03) as UNCLASSIFIED | SHIP AS DOCUMENTED GAP | `fp16_screen_exp8_arm2_1780781863.json` — confirmed: both items carry `content_class: UNCLASSIFIED` | "Items L2_02 (raw=`ANSWER: 0`) and L2_03 (raw=`ANSWER: 10`) are classified as UNCLASSIFIED in the Exp8A artifact. The class RETURNED_NON_CONTEXT_TOKEN was introduced in a subsequent scorer amendment; Exp8A was not rescored. Manuscripts citing item-level failure classes for Exp8A must use artifact values (UNCLASSIFIED)." |

---

## Summary by disposition type

```
RECOVERED:              0 items

NOT RECOVERABLE:        7 items
  Exp6:   tokenizer_hash, runner_hash, scorer_hash
  Exp7:   tokenizer_hash, runner_hash, scorer_hash
  Exp8A:  scorer_hash (pre-amendment), scaffold_class

SHIP AS DOCUMENTED GAP: 3 items
  Exp6:   decoding settings (values known from source, not from artifact)
  Exp7:   decoding settings (values known from source, not from artifact)
  Exp8A:  numeric failures — UNCLASSIFIED in artifact; RETURNED_NON_CONTEXT_TOKEN
          is post-hoc documentation only; artifact value governs
```

---

## Correction to APPENDIX-ARTIFACT-PACKET.md

During this inspection, a discrepancy was identified and corrected in APPENDIX-ARTIFACT-PACKET.md:

**Exp8A decoding settings are artifact-backed, not source-reconstructed.**

The Exp8A JSON artifact contains `"decoding": {"temperature": 0.0, "max_tokens": 16}` at the top level. This was confirmed by direct inspection on 2026-06-07. The APPENDIX-ARTIFACT-PACKET.md reproducibility table has been updated to mark Exp8A and Exp8B decoding as `*(artifact-backed)*`, consistent with the `*(from source)*` qualifier used for Exp6/Exp7. The Exp8A artifact gaps block has been updated to explicitly note that decoding is NOT a gap for Exp8A.

Prior references in documentation or memory that described "Exp8A decoding from source" are incorrect. The artifact value governs.

---

## Guidance for Senior

The seven NOT RECOVERABLE items are genuinely unrecoverable. No additional retrieval action changes these dispositions. The paper should say "documented provenance gap" for all seven.

The three SHIP AS DOCUMENTED GAP items have known values. Manuscript must be explicit:
- Exp6/Exp7 decoding: cite as "reconstructed from source inspection of `run_stability_screen.py`"
- Exp8A numeric failures: cite artifact values (UNCLASSIFIED), not post-hoc reclassification

Exp8A and Exp8B decoding settings are artifact-backed and may be cited without qualification.

---

## Files

```
PROVENANCE-GAP-DISPOSITION.md              — this file
APPENDIX-ARTIFACT-PACKET.md               — corrected (Exp8A decoding qualifier + gap note)
fp16_screen_exp8_arm2_1780781863.json     — Exp8A artifact (decoding confirmed present)
stability_screen_1780771434.json          — Exp6 artifact (decoding confirmed absent)
stability_screen_1780776502.json          — Exp7 artifact (decoding confirmed absent)
run_stability_screen.py                   — Exp6/Exp7 decoding source (current hash above)
```
