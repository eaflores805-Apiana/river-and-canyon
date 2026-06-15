# G6-RETROSPECTIVE-AUDIT-RESULT-v0.1

**Version:** v0.1. River and Canyon program. Result of the first model-free exercise of G6 — a retrospective desk audit of three standing refusals.
**Status:** MODEL-FREE DESK-AUDIT RESULT. Executed under the filed, pre-registered framing `G6-RETROSPECTIVE-AUDIT-FRAMING-v0.1` (commit 4442efd). It reads EXISTING raw outputs and applies the locked disposition rules; it runs no model, reopens no route, and authorizes nothing. Anchor: origin/main 4442efd.
**Method (locked, not chosen after seeing results):** disposition rules, channels, and the E3-not-E2 requirement are the framing's; the construct-validity semantic read stays human; design-target match counts as internal consistency, not general validation.
**Owner split:** Senior (auditor/drafter) → CS (verify cited paths + recompute the numeric re-derivations from the raw E3 files + confirm no execution/no reopen) → Team Lead (route) → Manager.

---

## Headline

```text
R1  D4 saturation refusal            → REFUSAL-CONFIRMED
R2  CAL-Q construct-validity refusal  → REFUSAL-CONFIRMED
R3  CAL-E elimination refusal         → REFUSAL-REVERSED (bounded — see boundary note)

The audit DISCRIMINATES: two refusals upheld, one scoring artifact reversed — and
the two "low defective score" cases (CAL-Q and CAL-E) were separated by item-level
raw evidence, not by their aggregates. This demonstrates INTERNAL G6 CONSISTENCY on
the spec's design-target cases. It does NOT demonstrate general G6 validity (§ caveat).
```

---

## R1 — D4 saturation refusal → REFUSAL-CONFIRMED

```text
GOVERNING ARTIFACT PATH(S):
  experiments/2026-06-11_lane-1a-prime/d4_a_pilot/candidate_outputs/ (80 answerable +
    16 null per-item raw files); candidate_predictions.json; the saturation arithmetic
    in BASELINE-GATE-DIAGNOSIS-v0.1 (window closes at clean_acc = 1.0).
RAW E3 EVIDENCE USED:
  the per-item raw output_text and prompt_user_text. I re-derived the gold for each
  answerable item FROM ITS PROMPT (parsing the key→value pairs and the query),
  independent of the original parser's parsed/label fields, and exact-matched the raw
  output_text. (E3, not E2.)  Provenance: candidate_predictions.json sha256 ba276b05…
INDEPENDENT CHANNEL DEPLOYED?
  YES — CH2 (a deterministic, objective re-derivation schema applied to raw outputs).
  CH1 (blind human reader) was NOT deployed; for an exact-match metric there is no
  reader-judgment latitude, so independence is carried by the rule's determinism, not
  by reader-blinding. Disclosed per the framing's interim-status rule.
DISPOSITION: REFUSAL-CONFIRMED.
RATIONALE:
  Independent re-score: answerable 80/80 exact-match correct = accuracy 1.0000; null
  16/16 abstained. The clean member sits AT ceiling (1.0). The sweep verdict classifies
  by clean accuracy (clean_acc ≥ ceiling − δ ⇒ CEILING/saturated), so at 1.0 there is
  no below-ceiling headroom for a retention drop to be measured. Refusing to certify
  D4 as a baseline was justified. (Human semantic read: a clean member at 1.0 cannot
  host a retention measurement — recorded as a human read, not automated.)
  Integrity note: my first re-score wrongly returned 0.85 because my prompt-parser
  mishandled MULTI-TOKEN keys (e.g. "44 3 -> l"); reading the raw prompt caught my own
  bug, and the corrected schema yields 80/80. The error and its correction are recorded
  because the re-derivation's value depends on it being genuinely independent, not a
  copy of the original scorer.
BOUNDARY NOTE:
  Auditing the D4 saturation refusal as EXISTING evidence does not reopen the D4 route
  (closed by Manager PIVOT; reopen Manager-only). No rerun; no execution.
```

## R2 — CAL-Q construct-validity refusal → REFUSAL-CONFIRMED

```text
GOVERNING ARTIFACT PATH(S):
  experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs/
    cal-q_defective_outputs.json , cal-q_clean_outputs.json ;
    sweep_run_records/cal-q_run.json (query_form = in_prompt_code_book);
    finding-tracks/cal-q-format-sensitive-abstention/ (the parked finding).
RAW E3 EVIDENCE USED:
  the per-item raw_output on the defective member (40 items, gold_value = null ⇒ correct
  behavior is ABSTAIN). I classified each raw output as abstention vs value-emission with
  a deterministic rule, independent of the original strict_correct/concept_correct labels.
  Provenance: cal-q_defective_outputs.json sha256 60a618a2…
INDEPENDENT CHANNEL DEPLOYED?
  YES — CH2 (deterministic abstain-vs-value classifier on raw outputs). The classification
  is objective here: the 40 outputs are real letter-values (a, n, b, y, h, z…) with ZERO
  none-forms, so there is no judgment latitude. CH1 not deployed (would add nothing for a
  zero-ambiguity case); disclosed.
DISPOSITION: REFUSAL-CONFIRMED.
RATIONALE:
  Independent re-derivation: defective-member abstention = 0/40 = 0.0000 (the model emitted
  a value on every item where it should have abstained; no "none"/"NONE" forms at all).
  Clean member re-derived at 26/40 = 0.65, matching the record. The code-book query form
  drives abstention to zero — the construct cannot measure abstention-discrimination.
  (Human semantic read: a query form under which the model NEVER abstains, even when it
  should, is construct-invalid for an abstention-discrimination instrument — recorded as a
  human read, per K6.) The refusal was justified.
  Critical separation: this is a GENUINE collapse, NOT a scoring artifact — contrast CAL-E
  (R3), whose "low" defective score IS a scoring artifact. The two were distinguished only
  by reading the raw item outputs (CAL-Q: 0 none-forms; CAL-E: 36 none-forms).
BOUNDARY NOTE:
  The audit reads the EXISTING CAL-Q outputs; it does NOT rerun CAL-Q (no rerun authorized).
  CAL-Q stays a parked finding track, not a D4 rescue. No execution.
```

## R3 — CAL-E elimination refusal → REFUSAL-REVERSED (bounded)

```text
GOVERNING ARTIFACT PATH(S):
  experiments/2026-06-11_lane-1a-prime/certification_readiness/sweep_outputs/
    cal-e_defective_outputs.json , cal-e_clean_outputs.json , cal-e_realized_match_manifest.json ;
    sweep_run_records/cal-e_run.json ; calibration_sweep_verdict.py (the pre-declared
    decision rule); cal-abce_rescore_summary.json (the record's own strict→concept rescore).
RAW E3 EVIDENCE USED:
  the per-item raw_output on the defective member (40 items, gold = null ⇒ abstain). I
  classified abstention CASE-INSENSITIVELY from raw outputs, independent of the original
  strict labels. Provenance: cal-e_defective_outputs.json sha256 9a85ff15…
INDEPENDENT CHANNEL DEPLOYED?
  Not required for a REVERSAL. Per the framing, reversal is reachable via item-level
  re-examination (Q2/Q3) without a fresh channel — and that is what was used.
DISPOSITION: REFUSAL-REVERSED, on the aggregate-vs-item point.
RATIONALE:
  The "defective member failed" reading rested on strict_accuracy 0.575 (23/40). Item-level
  inspection of the raw outputs shows the model actually ABSTAINED on 36/40 = 0.90 — it
  output "NONE" 23 times and "none" 13 times; the strict scorer was CASE-SENSITIVE and
  credited only the 23 uppercase forms, dropping 13 lowercase abstentions. So the apparent
  defective-member failure is a "NONE"/"none" scoring artifact, NOT present in the raw item
  behavior → the aggregate-driven reading is withdrawn. (My independent case-insensitive
  re-derivation, 36/40, matches the record's own rescore summary: n_strict_NONE 23,
  n_concept_abstention 36 — so this REVERSED disposition reproduces a correction the
  program had already made; the audit demonstrates G6 reaches the same item-grounded
  conclusion independently, which is the consistency check, not a new discovery.)
BOUNDARY NOTE (load-bearing — the reversal is bounded):
  Reversing the scoring artifact does NOT certify CAL-E. CAL-E was independently eliminated
  on a SEPARATE, valid ground: the sweep verdict classifies by CLEAN-member accuracy, and
  CAL-E's clean member is 0.975 = at/above the saturation boundary (CEILING). That
  ceiling-proximity elimination is untouched by the defective-member rescore and stands.
  So: the aggregate-vs-item artifact in the defective member is REVERSED; the overall
  non-certification of CAL-E is NOT reversed. The audit corrects the SCORING RECORD, not
  the disposition of CAL-E as a usable baseline.
```

---

## Required caveat — what this audit does and does not demonstrate

```text
DEMONSTRATES: INTERNAL G6 CONSISTENCY on design-target cases. Run on the raw E3 evidence,
  G6's disposition logic produces the spec's design-target outcomes (CAL-Q ⇒ CONFIRMED,
  CAL-E ⇒ REVERSED) and a sound CONFIRMED on the added D4 saturation case — and it
  DISCRIMINATES (it did not stamp everything the same; it separated CAL-Q's genuine
  collapse from CAL-E's scoring artifact using raw item evidence).
DOES NOT DEMONSTRATE (default position held): general G6 validity. These three refusals
  are the spec's own design cases; reproducing their design-target dispositions is a
  CONSISTENCY check, not external validation. A strong validity test needs NEW refusals
  not used in the spec's design. Nothing here is a claim that G6 works generally, that any
  baseline is certified, or that any stress evidence exists.
INDEPENDENCE HONESTY: for the two CONFIRMED cases the metric is objective (exact-match;
  value-vs-none with zero ambiguous items), so the deployed channel is a deterministic
  schema (CH2) whose result a non-blind auditor cannot bias; a blind human reader (CH1)
  was not deployed and, for these zero-latitude metrics, would add little — but its absence
  is disclosed, not hidden.
```

## Boundaries (held)

```text
- No G6 software implemented (desk audit only).   - No D4 reopening (D4 read as existing
- No model execution. No new runs.                  evidence; route stays closed, Manager-only).
- No certification evaluation.                     - No CAL-Q rerun (existing outputs read).
- No compression / INT8 / INT4.                    - No refusal turned into a product claim.
- No Paper B activation.                           - No claim G6 works generally.
- No new research claims.    Route state: YELLOW (model-free). Execution: RED.
```

This is a model-free desk-audit result. Under the locked framing, the three standing refusals disposition as CONFIRMED (D4 saturation, independently re-derived 80/80 = 1.0), CONFIRMED (CAL-Q, abstention genuinely 0/40 = 0.00), and REVERSED-bounded (CAL-E, a "NONE"/"none" case-sensitivity artifact in the defective member, reversed — while CAL-E's clean-ceiling elimination stands). The exercise demonstrates internal G6 consistency and discrimination on the spec's design-target cases; it does not validate G6 generally, certify a baseline, or produce stress evidence.

---

*G6-RETROSPECTIVE-AUDIT-RESULT-v0.1 (TL AUTHORIZED; model-free desk audit under framing 4442efd): R1 D4 saturation → REFUSAL-CONFIRMED (independent CH2 re-derive-from-prompt exact-match: answerable 80/80 = 1.0, null 16/16 abstain; clean member at ceiling; self-caught multi-token-key parser bug recorded). R2 CAL-Q → REFUSAL-CONFIRMED (independent CH2: defective abstention 0/40 = 0.00, ZERO none-forms = genuine collapse; clean 26/40 = 0.65; construct-invalidity = human semantic read per K6). R3 CAL-E → REFUSAL-REVERSED bounded (Q2/Q3 item inspection: defective strict 0.575/23 was a NONE/none case-sensitivity artifact, true abstention 36/40 = 0.90, reproduces the record's own rescore; BUT CAL-E stays eliminated on the independent clean-member ceiling ground 0.975 — reversal corrects the scoring record, not CAL-E's non-certification). Each with governing paths, raw E3 evidence + provenance sha256, channel-deployed status, rationale, boundary note. Discrimination shown (CAL-Q genuine vs CAL-E artifact, separated by raw item evidence). Caveat held: INTERNAL CONSISTENCY on design-target cases only, NOT general G6 validity; independence honesty disclosed (objective metrics, CH2 deterministic, CH1 not deployed). Boundaries: no software/exec/run/cert/compression/PaperB/D4-reopen/CAL-Q-rerun/product-claim/general-validity/new-claims. model-free.*
