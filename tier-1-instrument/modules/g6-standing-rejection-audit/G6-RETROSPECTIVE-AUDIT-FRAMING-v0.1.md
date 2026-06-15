# G6-RETROSPECTIVE-AUDIT-FRAMING-v0.1

**Version:** v0.1. River and Canyon program. Framing for the first model-free exercise of G6 — a retrospective audit of standing refusals already on the record.
**Status:** MODEL-FREE FRAMING. Defines HOW the audit will classify existing refusals before it reads them; it implements no G6 software, runs nothing, and resolves nothing. It exercises G6 on existing refusals; it does not validate G6 generally. Anchor: origin/main cb4a254.
**Builds on (does not reopen):** `G6-STANDING-REJECTION-AUDIT-SPEC-v0.1` (CS-verified — the disposition logic, the E2/E3 independence mechanism, and the §4 channels are its, carried forward in meaning, not redefined here); `TIER-1-G6-ENTRY-FRAMING-v0.1` (filed — named this retrospective audit as the first model-free G6 step). The refusal records audited are read as EXISTING evidence; auditing them reopens none of their routes (D4 stays closed; CAL-Q stays parked).
**Owner split:** Senior (drafter) → CS (verify cited record paths exist, raw-output evidence is present, and nothing here implements software or authorizes a run) → Team Lead (route; keep separate from D4 reopening and Paper B) → Manager.

---

## §0. The distinction this framing holds (stated first)

```text
This retrospective audit CAN exercise G6 on existing refusals — run the disposition
  machinery on real records and produce CONFIRMED / REVERSED / QUARANTINED /
  INCONCLUSIVE / CIRCULARITY outcomes.
It CANNOT:
  - validate G6 generally (these three cases are the spec's own DESIGN TARGETS — see
    §11; passing on them is a consistency check, not external validation);
  - certify a baseline (it audits refusals; it builds no baseline);
  - produce stress evidence (no compression rung; the program is pre-stress).
```

## §1. The refusal records in scope

Three standing refusals, each already on the record with raw per-item evidence:

```text
R1  D4 SATURATION REFUSAL — the gate declined to certify the D4 candidate as a
    baseline. Mechanism: the D7 saturation guard (the pilot scored 80/80, accuracy
    1.0, NOT_RULED_OUT on the six elimination criteria but no headroom below ceiling
    for a retention drop). A refusal-to-certify on saturation grounds.
R2  CAL-Q CONSTRUCT-VALIDITY REFUSAL — the gate refused CAL-Q: the query-side
    manipulation collapsed abstention 0.92 → 0.00, an invalid construct. (Spec
    DESIGN TARGET: REFUSAL-CONFIRMED.)
R3  CAL-E ELIMINATION REFUSAL — CAL-E was eliminated in the Lane-1a sweep. (Spec
    DESIGN TARGET: REFUSAL-REVERSED — an aggregate-vs-item artifact: the elimination
    rested on a summary statistic that item-level inspection does not support.)
```

CAL-E is included because TL's condition is met: it is in the record with raw item-level evidence — **both** clean and defective per-item outputs plus a realized-match manifest — so the aggregate-vs-item reversal can be audited model-free.

## §2. The artifact paths that govern each refusal

```text
R1 D4:    experiments/2026-06-11_lane-1a-prime/d4_a_pilot/  (+ d4_b_pilot/) — raw
            per-item outputs; the D4 pilot t3 report (80/80, NOT_RULED_OUT); the
            Block-F saturation arithmetic recorded in BASELINE-GATE-DIAGNOSIS-v0.1
            (window closes at a=1.0).
R2 CAL-Q: finding-tracks/cal-q-format-sensitive-abstention/findings/
            CS-CAL-Q-RUN-REPORT-v0.1.md (+ the finding track) — raw per-item
            abstention behavior on key-absent items (0.92 → 0.00).
R3 CAL-E: experiments/2026-06-11_lane-1a-prime/certification_readiness/
            sweep_run_records/cal-e_run.json ;
            sweep_outputs/cal-e_clean_outputs.json , cal-e_defective_outputs.json ,
            cal-e_clean_member.json , cal-e_defective_member.json ,
            cal-e_realized_match_manifest.json — raw per-item clean+defective
            outputs and the manifest mapping which item is which.
```

## §3. The independent channel required for each audit (per the G6 spec §4)

A refusal is eligible for full REFUSAL-CONFIRMED only via an independent channel — one that does not have access to, and is not derived from, the read that produced the refusal. The spec's two channels:

```text
CH1  BLIND SECOND READER — a second reader classifies the raw per-item outputs (E3)
     WITHOUT seeing the gate's decision, the original labels, or the route.
CH2  PRE-REGISTERED SCHEMA APPLIED WITHOUT ROUTE KNOWLEDGE — a classification schema
     fixed BEFORE the outputs are seen, applied to raw outputs (E3) by someone/
     something with no knowledge of the gate's decision.
Both are deployable RETROSPECTIVELY and MODEL-FREE (they re-read existing raw
outputs; no new model run). Per-refusal:

R1 D4 (CONFIRMED target):  requires CH1 or CH2 — a blind re-score of the raw D4
     per-item outputs for correctness, yielding accuracy, blind to the "saturated"
     verdict. (Mechanical: the saturation claim is accuracy ≈ 1.0.)
R2 CAL-Q (CONFIRMED target):  requires CH1 or CH2 — a blind re-classification of the
     raw per-item abstention behavior on key-absent items, blind to the "construct
     collapse" verdict.
R3 CAL-E (REVERSED target):  the reversal path (aggregate-vs-item, spec Q2+Q3) is
     reachable WITHOUT a fresh independent channel — it re-examines the existing
     clean/defective items against the manifest. A channel is NOT required to
     REVERSE; it is required to CONFIRM. (This asymmetry is the point of §10.)
```

## §4. What raw-output / per-item evidence must be used (E3, not E2)

The audit re-classifies from **E3 — the raw model outputs — not E2, the original read's labels.** Using E2 (the labels the refusal was based on) would inherit the verdict the audit is meant to check; that is AUDIT-CIRCULARITY (§9), never a confirmation.

```text
R1 D4:    the raw per-item model responses in d4_a_pilot (+ d4_b) — re-scored for
          correctness by the channel, NOT the original NOT_RULED_OUT / saturated
          labels.
R2 CAL-Q: the raw per-item outputs on key-absent items — re-read for abstain/answer
          by the channel, NOT the original "collapse" label.
R3 CAL-E: the raw cal-e_clean_outputs / cal-e_defective_outputs item-by-item, joined
          on cal-e_realized_match_manifest — item-level agreement vs the aggregate
          statistic that drove the elimination, NOT the original elimination label.
```

## §5. What would count as REFUSAL-CONFIRMED

```text
An independent channel (§3 CH1/CH2), working from raw E3 outputs, independently
reproduces the basis for the refusal, and spec questions Q1–Q4 hold.
  R1 D4:    a blind re-score yields accuracy ≈ 1.0 (within a pre-set band) → no
            below-ceiling headroom → the saturation refusal was justified.
  R2 CAL-Q: a blind re-read finds abstention ≈ 0.00 on key-absent items (within a
            pre-set band) → the construct-collapse refusal was justified.
CONFIRMED is NOT reachable without an independent channel actually deployed; absent
one, the case is CIRCULARITY (§9), never a default CONFIRMED.
```

## §6. What would count as REFUSAL-REVERSED

```text
Item-level re-examination (Q2+Q3; no fresh channel required) shows the refusal
rested on a scoring/aggregate artifact NOT present in the raw item behavior → the
refusal is withdrawn and the reversal recorded.
  R3 CAL-E: joining clean/defective raw outputs on the manifest shows the aggregate
            statistic that drove elimination masks item-level agreement (or the
            "defect" is a scoring artifact) → the elimination was not item-grounded
            → REVERSED.
```

## §7. What would count as REFUSAL-QUARANTINED

```text
The refusal cannot be adjudicated because the record itself is procedurally
deficient — raw outputs missing, items unhashed, or a provenance break — even
though a refusal was recorded. The refusal is retained but non-driving; the
deficiency is named. (Distinct from CIRCULARITY: there, the evidence may exist but
no INDEPENDENT channel does. Here, the EVIDENCE is missing or untrustworthy.)
```

## §8. What would count as AUDIT-INCONCLUSIVE

```text
The audit RAN — an independent channel was applied — but the raw evidence does not
clearly confirm or reverse: e.g. a channel that partially disagrees, or re-derived
numbers that land in a borderline band (accuracy near but not at the saturation
threshold; abstention reduced but not collapsed). Reported as inconclusive; the
named remedy is a human semantic read (§10) and/or an additional channel. NOT
rounded to CONFIRMED or REVERSED.
```

## §9. What would count as AUDIT-CIRCULARITY

```text
NO mechanized-independent channel was available (§3) — the only basis for re-checking
the refusal is the original read's own labels (E2), with no raw E3 access and no
blind channel deployed. The audit cannot proceed without inheriting the verdict it
is meant to check → a LIMITED status, explicitly NOT a silent or default
confirmation. For the CONFIRMED-target cases (R1, R2), if no blind channel (CH1/CH2)
is deployed on the raw outputs, the honest output is CIRCULARITY (or, where Q2/Q3
mechanical re-derivation partially holds, a LIMITED status disclosed per the spec's
interim-status rule) — never CONFIRMED by assertion.
```

## §10. What remains human semantic judgment and must not be automated

```text
Per the spec K6 / Tool Spec §8: the CONSTRUCT-VALIDITY SEMANTIC READ stays human.
The audit may MECHANIZE the independence channel (blind re-classification of raw
outputs) and the mechanical re-derivations (accuracy, abstention rate, item
agreement). It must NOT automate the JUDGMENT of what that behavior MEANS for
construct validity — e.g. whether abstention-collapse reflects genuine construct
invalidity versus an artifact of the manipulation; whether a saturated score
reflects a real ceiling versus an easy task that could be made harder. The
disposition's mechanical inputs are auditable; its semantic interpretation is a
human read, recorded as such.
```

## §11. The honest caveat — two levels of circularity, and the retrospective asymmetry

This is the framing's load-bearing honesty, and the reason §0 holds:

```text
LEVEL 1 — per-audit circularity. Handled by the disposition scheme: re-using E2
  labels instead of E3 raw outputs returns AUDIT-CIRCULARITY (§9), not a pass. The
  E3 requirement (§4) is the guard.

LEVEL 2 — META circularity (the one to state plainly). These three refusals ARE the
  G6 spec's own design cases: CAL-Q is the explicit DESIGN TARGET for CONFIRMED,
  CAL-E the explicit DESIGN TARGET for REVERSED. So even a clean run — each case
  returning its design-target disposition through a proper E3 channel — demonstrates
  that the machinery RUNS and is INTERNALLY CONSISTENT on the cases it was built for.
  It is a WEAK test of GENERAL validity precisely because the cases were design
  INPUTS. A strong validity test needs NEW refusals not used in the spec's design.
  The audit therefore STRENGTHENS confidence that G6 is implementable and
  self-consistent; it does NOT validate G6 generally — and the design-target match
  must be recorded as CONSISTENCY, not external confirmation.

RETROSPECTIVE ASYMMETRY (a structural finding to pre-declare). REVERSAL (CAL-E) is
  cleanly reachable retrospectively via Q2/Q3 with no fresh channel. CONFIRMATION
  (D4, CAL-Q) requires a blind channel (CH1/CH2) deployed on the existing raw
  outputs — achievable model-free, but ONLY if actually deployed. Pre-declaring this
  prevents the audit from rubber-stamping a CONFIRMED it cannot independently
  support: a CONFIRMED-target case with no deployed channel is CIRCULARITY/LIMITED,
  not CONFIRMED.
```

**Pre-registration (the discipline this framing exists to enforce):** the disposition rules in §§5–9, the channel requirement in §3, the E3 requirement in §4, and the asymmetry in §11 are declared NOW, before the audit reads the records and produces verdicts — so the classification is a pre-registration, not a post-hoc story fitted to what the records turn out to show.

## §12. What remains closed (boundaries)

```text
- No G6 software implementation — this is framing + a desk-audit method, not a build.
- No model execution. No new runs. No certification evaluation.
- No compression / INT8 / INT4. No Paper B activation. No D4 reopening (auditing the
  D4 saturation refusal as existing evidence does NOT reopen the D4 route).
- No CAL-Q rerun (the audit reads the EXISTING CAL-Q outputs).
- No turning a refusal into a product claim; no claim that G6 works generally
  (§11); no new research claims.
Route state: YELLOW (model-free). Execution: RED.
```

This is model-free framing only. It defines the disposition rules, channels, and evidence for a retrospective audit of three standing refusals (D4 saturation, CAL-Q, CAL-E) before that audit reads them — and states plainly that the audit can EXERCISE G6 on existing refusals but cannot validate G6 generally, certify a baseline, or produce stress evidence, with the design-target match recorded as consistency rather than confirmation.

---

*G6-RETROSPECTIVE-AUDIT-FRAMING-v0.1 (TL ACTION; model-free; first exercise of G6): §1 three refusal records in scope (D4 saturation; CAL-Q construct-validity = CONFIRMED design target; CAL-E elimination = REVERSED design target, included because in-record with raw clean+defective item outputs + manifest); §2 governing artifact paths; §3 the §4 independent channels (CH1 blind reader / CH2 pre-registered schema), deployable retrospectively + model-free, with the per-case requirement; §4 E3-not-E2 raw-evidence requirement; §§5–9 the five dispositions specialized to these cases (REFUSAL-CONFIRMED requires a deployed independent channel; REFUSAL-REVERSED reachable via Q2/Q3 without one; QUARANTINED = deficient record; INCONCLUSIVE = channel ran but ambiguous; AUDIT-CIRCULARITY = no independent channel, never a default confirm); §10 the construct-validity semantic read stays human (K6); §11 the honest caveat — Level-1 per-audit circularity (guarded by E3) + Level-2 meta circularity (these are the spec's design targets, so a pass is consistency not external validation) + the retrospective confirm/reverse asymmetry; pre-registration declared before the audit reads the records. Holds CAN-exercise / CANNOT-validate-generally throughout. Implements no software; authorizes no execution/run/certification/compression; reopens no D4; reruns no CAL-Q; claims no general G6 validity; creates no new claims. model-free.*
