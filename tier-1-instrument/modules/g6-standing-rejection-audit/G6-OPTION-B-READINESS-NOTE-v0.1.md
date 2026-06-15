# G6-OPTION-B-READINESS-NOTE-v0.1

**Version:** v0.1. River and Canyon program. Readiness note preparing the ground for a POSSIBLE future Option B decision — without opening Option B.
**Status:** MODEL-FREE READINESS NOTE. It defines what would count as a non-design-target G6 validation case and captures lessons from the first (closed) internal-consistency exercise. It does NOT open Option B, does NOT select or inventory any candidate case, and authorizes nothing. Anchor: origin/main 502a45f.
**Owner split:** Senior (drafter) → CS (verify cited filed-state + that no case is selected and no boundary is crossed) → Team Lead (route) → Manager (owns any future Option-B decision).
**Note on scope (per Manager):** the filed audit result, the ledger refresh, the closeout, and CS's raw-E3 verification are already satisfied and are NOT redone here; this note only prepares forward ground.

---

## §1. Current closed state (established; not re-litigated here)

```text
- G6 retrospective audit result FILED / CS PASS  (e6881f2, sha 4ce9b26d…).
- First internal G6 consistency exercise CLOSED  (closeout 502a45f, CS PASS).
- Live-state refresh FILED  (PROGRAM-CONTROL-LEDGER-v0.3, 2064ef3; coupled MAP.md bump done).
- Option A SELECTED and CLOSED.
- Option B NOT opened.
This note proceeds from that closed state; it changes none of it.
```

## §2. Definition of "non-design-target" for G6

```text
A refusal case counts as NON-DESIGN-TARGET only if it was NOT used to design, tune,
illustrate, or pre-load the G6 disposition logic — i.e., its expected disposition was
NOT an input to building, specifying, or worked-exampling G6.
Operative test: if knowing the case's outcome helped shape the gate, the spec, the
framing, or the disposition rules, the case is design-loaded and does NOT qualify.
A non-design-target case is one whose disposition the existing G6 machinery has never
been shown, tuned, or built to produce.
```

## §3. Exclusion rules (a candidate is DISQUALIFIED if it…)

```text
- is a NAMED design/validation target in the G6 spec. Per spec §11 these are:
    · CAL-Q  (construct collapse → expected REFUSAL-CONFIRMED),
    · CAL-E  (scorer artifact   → expected REFUSAL-REVERSED),
    · a refusal with NO independent channel → expected AUDIT-CIRCULARITY.
- was used in the retrospective audit FRAMING as an expected CONFIRMED / REVERSED case.
    The three audited refusals — D4 saturation, CAL-Q, CAL-E — are all design-loaded by
    use and are excluded.
- was already KNOWN to be a scoring artifact before selection (e.g. CAL-E, whose
    "NONE"/"none" case-sensitivity artifact was on record in the rescore summary).
- is selected BECAUSE its expected disposition is obvious (selecting for a foregone
    answer reproduces self-consistency, not a validity test).
- would require NEW MODEL EXECUTION under the current RED state (out of bounds; a
    non-design-target case must be auditable on existing evidence).
NOTE: this note lists only the EXCLUDED cases (restating the boundary). It does NOT
propose, name, or inventory any ELIGIBLE candidate — candidate inventory is a separate
future step (§7), not begun here.
```

## §4. Minimum eligibility criteria (a qualifying candidate MUST have…)

```text
- EXISTING RAW E3 OUTPUTS — per-item raw model outputs on record, so an independent
    channel can re-classify from raw outputs rather than inherit the original labels.
- CLEAR GOVERNING ARTIFACT PATHS — the refusal's record and evidence locatable and citable.
- ENOUGH PROVENANCE TO AVOID QUARANTINE — hashes / manifests sufficient that the record
    is not procedurally deficient (else the audit returns REFUSAL-QUARANTINED, not a test).
- AT LEAST ONE PLAUSIBLE INDEPENDENT CHANNEL — a deployable CH1 (blind reader of raw E3)
    or CH2 (pre-registered schema applied blind). Without one, a CONFIRMED-target case can
    only reach AUDIT-CIRCULARITY — which tests nothing new about generalization.
- A PRE-DECLARED EXPECTED UNCERTAINTY, NOT A KNOWN ANSWER — the expected disposition must
    be genuinely open before the audit runs. This is the criterion that makes the case a
    validity test rather than a re-run of self-consistency.
- NO NEED FOR MODEL EXECUTION — fully auditable model-free on existing bytes.
```

## §5. Lessons from the first G6 exercise (carried forward)

```text
- E3 RAW EVIDENCE CHANGES THE OUTCOME. Re-deriving from raw outputs — not the producing
    read's labels — materially altered scores: a multi-token-key parser slip read 0.85
    before correction to the true 1.0 (D4); a case-sensitivity artifact read 0.575 before
    correction to the true 0.90 abstention (CAL-E). The raw read, not the label, decided.
- AGGREGATE SCORES CAN HIDE ITEM-LEVEL CAUSES. CAL-E's strict 0.575 concealed 36/40
    correct abstentions ("NONE" 23 + "none" 13); only item inspection surfaced the cause.
- CONFIRMED AND REVERSED HAVE ASYMMETRIC CHANNEL NEEDS. REFUSAL-CONFIRMED requires a
    deployed independent channel; REFUSAL-REVERSED via an aggregate-vs-item artifact is
    reachable by item-level re-examination (Q2/Q3) without a fresh channel.
- DETERMINISTIC CH2 CAN WORK FOR ZERO-LATITUDE METRICS — BUT MUST DISCLOSE LIMITS. For
    objective metrics (exact-match; value-vs-none with no ambiguous items) a deterministic
    schema's result a non-blind auditor cannot bias; a blind human reader (CH1) was not
    deployed and its absence was disclosed, not hidden.
- DESIGN-TARGET SUCCESS IS INTERNAL CONSISTENCY, NOT GENERAL VALIDITY. Reproducing the
    spec's own design-target dispositions shows the machinery runs and is self-consistent;
    it does not show it generalizes.
- CAL-Q vs CAL-E SHOWED WHY RAW ITEM INSPECTION MATTERS. Both had a "low" defective score,
    for OPPOSITE reasons — CAL-Q a genuine collapse (0 none-forms), CAL-E a scoring artifact
    (36 none-forms). Nothing but the raw item evidence separated them.
```

## §6. What Option B would and would not test

```text
WOULD (if opened and run on a qualifying case):
  - test whether G6 GENERALIZES beyond its design cases — whether the disposition logic
    reaches a correct, pre-uncertain verdict on a refusal it was never built around.
WOULD NOT:
  - validate G6 generally by itself (one non-design-target case is one case, not a class);
  - certify a baseline;
  - produce stress evidence (the program remains pre-stress).
And: resolving a CONFIRMED-target candidate at full strength would still need an
independent channel deployed; anything beyond model-free desk work remains unauthorized.
```

## §7. Recommended next decision surface (a clean future choice for the Manager)

```text
Present the Manager with three options — WITHOUT a recommendation among them and WITHOUT
selecting any case:
  (a) KEEP OPTION B PARKED — no further G6 work now; the closed exercise stands.
  (b) OPEN OPTION B, DESIGN-ONLY — authorize model-free DESIGN of a non-design-target
      validation case against §§2–4 (no execution; resolution still needs a separately
      authorized channel later).
  (c) REQUEST A CANDIDATE INVENTORY FIRST — a separate model-free pass that lists
      refusals on record meeting §§3–4, with provenance, BEFORE deciding (a) vs (b).
This note prepares that surface; it does not choose, and it does not begin (b) or (c).
```

## §8. Boundaries (held)

```text
- Option B NOT opened.                  - No certification authorized.
- No non-design-target case selected.   - No compression authorized.
- No audit execution authorized.        - No Paper B activation.
- No software build authorized.         - No D4 reopening.
- No model execution authorized.        - No general G6 validity claim.
- No product / funder-facing claim.     Route state: YELLOW (model-free). Execution: RED.
```

This is a model-free readiness note. It defines a non-design-target G6 validation case (§2), its exclusion rules (§3, grounded in the spec's §11 named targets and the framing's used cases) and minimum eligibility criteria (§4), carries forward the lessons of the first exercise (§5), bounds what Option B would and would not test (§6), and lays out a clean future decision surface (§7). It opens no option, selects no case, inventories no candidate, and authorizes nothing; D4 stays closed, CAL-Q is not rerun, Paper B stays deferred, and no general-validity or funder-facing claim is made.

---

*G6-OPTION-B-READINESS-NOTE-v0.1 (TL ACTION; model-free; prepares ground for a possible future Option B WITHOUT opening it): §1 closed state established (result e6881f2, closeout 502a45f, ledger v0.3 2064ef3; Option A closed, B not opened) — not re-litigated per Manager. §2 non-design-target definition (a case whose expected disposition was NOT an input to building/specifying/exampling G6). §3 exclusion rules grounded in spec §11 named targets (CAL-Q→CONFIRMED, CAL-E→REVERSED, no-channel→CIRCULARITY) + framing-used cases (D4/CAL-Q/CAL-E) + known-artifact (CAL-E) + obvious-answer + needs-execution; lists ONLY excluded cases, inventories no eligible candidate. §4 minimum eligibility (existing raw E3; clear paths; provenance vs quarantine; ≥1 plausible independent channel; pre-declared expected UNCERTAINTY not a known answer; no execution). §5 six lessons carried forward (E3 changes outcome; aggregates hide item causes; CONFIRMED/REVERSED asymmetric channel needs; deterministic CH2 for zero-latitude metrics w/ disclosed limits; design-target success = internal consistency not general validity; CAL-Q-vs-CAL-E raw inspection). §6 Option B would test generalization but would NOT validate generally/certify baseline/produce stress. §7 decision surface (keep parked / open design-only / request candidate inventory) — no recommendation, no selection. Opens no option; selects no case; authorizes nothing; D4 closed; CAL-Q not rerun; Paper B deferred; no general-validity or funder claim. model-free.*
