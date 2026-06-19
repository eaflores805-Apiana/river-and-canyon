# Claim Ledger — v1.0

**Released:** 2026-06-19
**Authority:** Manager Decision 2026-06-19 ("Claim Ledger Identifier and Paper 2 Freeze/Tag Substitution"). Identifier authorized as `notes/CLAIM-LEDGER-v1.0.md`.
**Carrier role:** organizing claim record for the Path A / V3 lifecycle; freeze/tag-carrying release for Paper 2 Appendix A.
**Filed by:** CS Engineer (filing only; CS authored no claim language).

**Predecessors (carried by reference, not modified):**

- `notes/claim-ledger-practice-note.md` — Claim Ledger v0.1 (working note; the convergence-audit framing).
- `tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md` — authoritative carrier of Claims A / B / C and the canonical gate ladder; **SEALED** per the standing tier0-run rule.
  - sha256: `b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2`
  - filed: 2026-06-07
- `papers/paper2-correctness-is-not-constructibility/correctness-is-not-constructibility.md` — Paper 2 (released v1.0; tag `paper2-cells01-03-v1.0`; manuscript blob `7d6706a3…`). The tag is **NOT** modified by this release.

This release **does not edit any claim language**. Where a claim's text is quoted below, it is verbatim from the predecessor identified by sha. Where this release adds new content, it is a **finding row** for the V3 lifecycle — a positional/structural / cross-materialization constructibility result, **not** a mechanism, capability, certification, compression, or seam claim.

---

## Claim A — the principle (analytic) — CARRIED BY REFERENCE; UNCHANGED

Canonical text: see `tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md` §"Claim A" verbatim (sha `b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2`).

**Status as of this release:** analytic; not falsifiable by Track A; holds whether or not any cell ever clears the floor. **Unchanged** by the V3 lifecycle.

## Claim B — the mappability hypothesis (empirical, falsifiable) — CARRIED BY REFERENCE; STATUS UPDATED

Canonical text: see `tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md` §"Claim B" verbatim (sha `b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2`).

**Status as of this release:** Paper 2 v1.0 reports Claim B as *mappable, not cleared* on one construction (Cells 01–03; position/rank-contaminated surface composite + below-floor hop1 component). The V3 lifecycle in this release adds a **second, independent construction** to Claim B's evidential base. Claim B remains **supported, not cleared** — mappability is reinforced across two distinct constructions, neither of which produced a clean cell.

## Claim C — linkage-under-compression (conditional; gated on B) — CARRIED BY REFERENCE; UNTOUCHED

Canonical text: see `tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md` §"Claim C" verbatim (sha `b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2`).

**Status as of this release:** **untouched.** Claim C is not testable until a Claim-B-cleared cell exists. No such cell has been produced in either construction. The V3 composite gate was not readable (precondition unmet); Claim C remains gated. **The program remains pre-stress.**

## Program Claim #5 — precision-demanding tasks retain less under quantization — UNCHANGED

**Status as of this release:** **blocked on a precondition.** Carried verbatim from Paper 2 v1.0 Appendix A. The V3 lifecycle **reinforces** the block (the V3 composite gate was likewise not readable) and **does not resolve it**.

---

## V3 negative-finding row (NEW; this release)

This row records that, under the V3 foreclose-all construction at 3B FP16 greedy, the first-hop admissibility precondition was **stable-inadmissible across six fresh disjoint materializations**, while the second hop held at ceiling — so the V3 composite gate was not readable on these materializations, and the V3 composite question is unanswered. The row carries the **positional / structural** finding for the constructibility map and explicitly **does not** carry a mechanism, capability, certification, or compression claim.

**Construction parameters (locked; carried from prereg v0.4):**

```text
D = 5 distinct relations to 5 same-depth depth-2 competitors (foreclose-all)
K = 5 relation-reusing distractor chains carrying the P-role token (r1-subject)
P = 5    M ≥ 10 fan-in    selection margin 0.25    derived structural floor F = 0.20
Indices ≤ 999 (3-digit per-item-prefix scheme; MAX_DELTA = 8 invariant)
```

**Materialization plan:**

```text
F1   193..288     fresh
F2   289..384     fresh
F3   385..480     fresh
F4   481..576     fresh
F5   577..672     fresh
F6   673..768     fresh
Anchors (not in branch decision):
  001..096   floor-check    COMPONENT-ADMISSIBLE-UNDER-COMPETITION
  097..192   composite-gate PRECONDITION-FAIL (hop1 28/96)
```

**Model / profile (locked):**

```text
Qwen/Qwen2.5-3B-Instruct    revision aa8e72537993ba99e69dfaafa59ed015b17504d1    FP16    greedy (temp 0)
```

**Admissibility floor:** Wilson lower bound > 0.75 (component); CONSTRUCT-FAIL > HOP2-CONTROL-FAIL > stability branches.

**Result (analyzer decision, this release):**

```text
final_branch               HOP1-STABLE-INADMISSIBLE
construct_fail_blocks      []        (C1–C9 admissibility 576/576 PASS; prompt conformance 576/576 PASS)
hop2_control_fail_blocks   []        (hop2 96/96 every block; Wilson lower 0.9615)
hop1_clear_blocks          []
hop1_fail_blocks           [1, 2, 3, 4, 5, 6]

  block   range        hop1 k/n   hop1 rate   hop1 Wilson lower (vs 0.75)   hop2 k/n
  F1      193..288     50/96      0.5208      0.4220   (fail)               96/96
  F2      289..384     23/96      0.2396      0.1653   (fail)               96/96
  F3      385..480     35/96      0.3646      0.2752   (fail)               96/96
  F4      481..576     39/96      0.4062      0.3135   (fail)               96/96
  F5      577..672     54/96      0.5625      0.4628   (fail)               96/96
  F6      673..768     23/96      0.2396      0.1653   (fail)               96/96
  total                224/576    —           —                             576/576

hop1 between-block spread:  min 0.2396  max 0.5625  range 0.3229  mean 0.3889  stddev 0.1245
```

**Positional / structural co-occurrence (per prereg §6; descriptive, never causal):**

```text
predicted_is_P_role_distractor among WRONG hop1 predictions   352 / 352 = 1.0000

  Reading: 100% of wrong hop1 predictions landed on the P-role distractor
  (the r1-subject role token of a relation-reusing distractor chain), reproduced
  unanimously on the six fresh blocks. This is a landing fact, not a mechanism.
  Per the discipline of this ledger, for this co-occurrence to become more than a
  landing fact, a future pre-registered study would require a behavioral signature,
  a minimal intervention predicted to change the landing, and a falsification path.
```

**Authoritative byte-stable carriers (SHA-256 from the locked files; CS-recomputed 2026-06-19):**

```text
experiments/2026-06-19_hop1-stability-run/
  decision.json                     8676530a97e4322f38cf8ded17710db32883c16a5b1b431e9af284dd9b4f8965
  covariate_log.json                480f70d18f908a4dd89c8f5435cc122b61cfbf68e8fa006478fcfb8949049950
  admissibility_summary.json        3763f736ff2dae8e2a90908a3787446d3e95c300062d02199107b6ebd85857e9
  prompt_conformance_summary.json   b361b1d7b8bda061ad456dad0fe3cc82a81440277669f0fe651695ec0af92758
  run_record.json                   11756a53a9158e8687faab1da1a05d89cf77db7a74403e7d34b7a95d4c5e6702
  manifest.json                     2ad2015c5edc9d8c8a654a7f5b360d8c8b98983b3f85e4558ea29976bfc4a1bb

experiments/2026-06-18_v3-floor-check-run/
  analyzer_decision.json            6a34f6dc9687e04d0bc58b1595b4c6e9555a59e4bb606e40e9aa72ddd2c048c5
                                    (anchor; COMPONENT-ADMISSIBLE-UNDER-COMPETITION)

experiments/2026-06-18_v3-composite-gate-run/
  analyzer_decision.json            3924ff35087c5648a20101e463f2129d6d731a853c4b9f0e3d61a4ade6efe842
                                    (anchor; PRECONDITION-FAIL)

Locked tooling (unchanged across the V3 lifecycle):
  v3_hop1_stability_analyzer.py     31224f6fe7b66d303924a40fa9307f3aded05f8ba73d4952f518c8deecd69f0f
  v3_hop1_covariate_logger.py       b9532490f49970396cd9a14d926393450ede2e6a17c5374b2ac69d115f39953f
  v3_composite_gate_item_generator  cc07e5a2c49757e9171831af7944b5f7f8b1de235c7cb35cb18e48b06ce534a2  (wrapper)
  v3_item_generator.py              6a2ceee15442ebbd1f6cc4bbbd14a76d1264af9904ad3e5d6062c1554f530c53  (underlying)
  v3_prompt_realizer.py             fb561fdc526115da94c6137b739e8bb3b6adf30825d83f864cda713bc0750909
  v3_prompt_conformance_checker.py  b8afa3f89dd7f375058500820bdf2bf58a46384d2283c8f2a31f1b8c92ad2b82
  path-a/inspector/inspector.py     cb4b0b60bd6dc2b5f1d7ee6c4eaf3fc274cbb10254b5a548c637c84ca27348a9
  path-a/inspector/constants.py     1d761c3d1c56e7aca9ef32a3f8b05c310e2aa5f35c6d91e67fd7fd81468915dd

SE verification returns of record (byte-stable):
  V3-FLOOR-CHECK-RUN-SE-VERIFICATION-RETURN-v0.1.md
                                    03d2ead80e830a8067c145e6516e20847fb0d2961a9ead85236ff696fe3d560f
  V3-COMPOSITE-GATE-RUN-SE-VERIFICATION-RETURN-v0.1.md
                                    0eb0edcb6cc71632d41c58f2cd44ff802ba7beb173bf839bca4c50beecf88abd
  HOP1-STABILITY-RUN-SE-VERIFICATION-RETURN-v0.1.md
                                    84a5716b4f202a9337495100064d8e5f466ff8baf3e76bb16b4d221de05285b9
  HOP1-STABILITY-FINDING-REPORT-v0.1.md
                                    2969ec1a5ce830c2b77c974ad23b163e4cb1dca6a518800a555f5a159f6efb33
```

**Reads against the existing Claims (per this row only):**

```text
Claim A          unchanged — the row IS evidence that the floor is mapped here,
                 not that the floor is crossed; A holds regardless.
Claim B          supported (not cleared) — second independent construction
                 reinforcing mappability; the second hop is at ceiling across
                 six fresh materializations while the first hop is stable-
                 inadmissible, so this construction is mapped, not crossed.
Claim C          UNTOUCHED — the V3 composite gate was not readable; nothing
                 about compression is read here; Claim C stays gated.
Claim #5         REINFORCED as "blocked on a precondition" — not resolved;
                 the V3 lifecycle adds a second precondition-failure data
                 point to the existing block; the program remains pre-stress.
```

**Non-claims of this row (explicit; carried verbatim from the V3 delta draft §10):**

```text
- NOT "the model cannot do hop1."                  (V3 states a per-construction admissibility result.)
- NOT "the model cannot compose."                  (Composite question is unanswered, not refuted.)
- NOT "the model is unstable."                     (Result is about the V3 construct's precondition.)
- NOT a binding / attention / reasoning failure.   (No mechanism is named anywhere.)
- NOT a shortcut-mechanism claim.                  (P-role is positional / structural co-occurrence only.)
- NOT compression readiness.                       (Pre-stress; no rung run.)
- NOT a statement on Claim C (the seam).           (Remains blocked; untouched.)
- NOT a certification claim.                       (Nothing certified; composite gate not even read.)
- NOT a capability claim.                          (All statements are about the construction's behavior.)
- NOT a mechanism claim.                           (Behavioral-only limitation inherited.)
- NOT cross-model / cross-scale / cross-task generality.  (Cross-materialization within one model and task family only.)
```

---

## Required measurement rule — canonical gate ladder (unchanged)

Canonical text: see `tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md` §"Required measurement rule — canonical gate ladder" verbatim (sha `b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2`).

The V3 construction is bound to that ladder. The V3 negative-finding row above is a **Gate 2** result (FP16 baseline correctness — hop1 component) for the V3 construction: hop1 fails Gate 2 across all six fresh materializations, which blocks every gate below it for that construction.

## Non-claims (canonical) — unchanged

Canonical text: see `tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md` §"Non-claims" verbatim (sha `b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2`).

## Safe claim language — unchanged

Canonical text: see `tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md` §"Safe claim language" verbatim (sha `b16875590ca060b857bf577fd5862eae9adb05b60c7fbdda1d0d5f1318bb55b2`).

The V3 row above is phrased to comply: *under this frozen V3 construction, at this model size, under these gates, the first-hop component did not reach interpretability across six fresh materializations.*

---

## Provenance + filing

- **Released** by CS Engineer on 2026-06-19 per Manager Decision 2026-06-19 ("Claim Ledger Identifier and Paper 2 Freeze/Tag Substitution"). Identifier authorized as `notes/CLAIM-LEDGER-v1.0.md`.
- **Filed simultaneously with** the Paper 2 V3 delta freeze/tag substitution pass (Appendix A bracketed identifier → `notes/CLAIM-LEDGER-v1.0.md`; Appendix B placeholder digests → full sha256). Those substitutions are in the same commit.
- **`tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md` is NOT modified** by this release. It remains sealed per the standing tier0-run rule; all references above are read-only citations by sha.
- **Paper 2 v1.0 tag (`paper2-cells01-03-v1.0`; manuscript blob `7d6706a3…`) is NOT modified** by this release.
- **No new experiment is implied** by this release. No prereg is modified. No tooling digest is modified. No threshold is modified.
- **CS authored no claim language.** All claim text in this release is carried by reference to its canonical home and cited by sha. CS's authorship in this file is limited to: (i) the V3 negative-finding row's empirical record (numbers, digests, byte-stable carriers); (ii) the framing of *which existing claims this row reads against*; (iii) the provenance section.

— CS Engineer, 2026-06-19
