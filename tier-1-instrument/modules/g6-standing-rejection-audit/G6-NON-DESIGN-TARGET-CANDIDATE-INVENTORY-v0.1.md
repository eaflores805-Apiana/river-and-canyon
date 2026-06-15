# G6-NON-DESIGN-TARGET-CANDIDATE-INVENTORY-v0.1

**Version:** v0.1. River and Canyon program. Inventory of refusal cases already on record, screened against the filed non-design-target definition — to identify whether any existing refusal is eligible for a FUTURE Option B design decision.
**Status:** MODEL-FREE INVENTORY (Manager selected Option C — "request a candidate inventory first"). It screens existing cases; it does NOT open Option B, does NOT select a candidate, and authorizes nothing. Anchor: origin/main 41a416b.
**Governing readiness note:** `tier-1-instrument/modules/g6-standing-rejection-audit/G6-OPTION-B-READINESS-NOTE-v0.1.md` (FILED 41a416b) — the non-design-target definition (§2), exclusion rules (§3), and minimum eligibility criteria (§4) screened against here are its.
**Owner split:** Senior (inventory/drafter) → CS (verify cited record paths exist + that no case is selected and no boundary crossed) → Team Lead (route) → Manager (owns any future Option-B decision).

---

## §1. Method

Each case surveyed on record returns exactly one disposition:

```text
ELIGIBLE-CANDIDATE  appears to satisfy the non-design-target definition AND the
                    minimum eligibility criteria.
EXCLUDE             fails the non-design-target definition or an exclusion rule.
HOLD                may qualify, but available information is insufficient to decide
                    without further model-free path/provenance review.
```

Screened against the readiness note's criteria (per case): used to design/tune/illustrate/pre-load G6? · named in the G6 spec as a design/validation target? · used in the retrospective audit framing? · expected disposition known before selection? · expected answer too obvious? · requires new model execution? · existing raw E3 outputs? · governing artifact paths clear? · provenance sufficient to avoid quarantine? · ≥1 independent channel plausible? · expected uncertainty genuinely open?

**This inventory SCREENS cases; it does not SELECT one.** Listing a case as ELIGIBLE-CANDIDATE (none here) would be a screening result, not a selection — selection is a separate, future, Manager-owned act.

## §2. Candidate inventory table

```text
CASE                          DISPOSITION       PRIMARY BASIS
--------------------------------------------------------------------------------------
CAL-Q                         EXCLUDE           spec design target (→CONFIRMED); framing R2
CAL-E                         EXCLUDE           spec design target (→REVERSED); framing R3;
                                                known scoring artifact
D4 saturation                 EXCLUDE           framing R1; clean-ceiling; disposition known
no-independent-channel case   EXCLUDE           spec §11 design target (→CIRCULARITY)
CAL-A                         EXCLUDE           Paper A instrument sweep + cal-abce rescore;
                                                clean 1.000 = obvious ceiling
CAL-B                         EXCLUDE           Paper A instrument sweep + cal-abce rescore;
                                                clean 0.975 = obvious ceiling
CAL-C                         EXCLUDE           Paper A instrument sweep + cal-abce rescore;
                                                clean 0.950 = at/near boundary
2026-06-10 lane-1a-sweep      EXCLUDE           labeled INSTRUMENT-FAILURE; no valid per-item
                                                refusal outputs; instrument-development evidence
b1-harness-v2                 EXCLUDE           harness/instrument validation, not a gate refusal
INT8-RUNG-1                   EXCLUDE           QUARANTINED (non-promotable); not a gate refusal
superseded validation runs    HOLD              retention-validation runs (not gate refusals),
  (superseded_run-1/2/3)                        superseded; eligibility needs path/provenance review
--------------------------------------------------------------------------------------
ELIGIBLE-CANDIDATE count: 0      EXCLUDE: 10 (case-groups)      HOLD: 1 (case-group)
```

## §3. Per-candidate rationale (short)

```text
CAL-Q  — the spec's explicit design target for REFUSAL-CONFIRMED and framing R2. Design-
         loaded by definition; its disposition is the design intent. EXCLUDE.
CAL-E  — the spec's explicit design target for REFUSAL-REVERSED, framing R3, and a case whose
         "NONE"/"none" scoring artifact was on record before any selection. EXCLUDE.
D4 saturation — framing R1; eliminated on the clean-ceiling rule (clean 1.0); audited already;
         disposition known and obvious. EXCLUDE.
no-independent-channel case — the spec §11 design target for AUDIT-CIRCULARITY. EXCLUDE.
CAL-A / CAL-B / CAL-C — the other members of the SAME calibration sweep that Paper A states
         "exercised this gate directly"; all appear in Paper A's certification-box figure and
         instrument section, and all are in the cal-abce rescore that revealed the aggregate-vs-
         item artifact underlying G6's REVERSED disposition logic. Design-loaded by illustration
         AND by shaping the disposition logic. Their clean accuracies (1.000 / 0.975 / 0.950)
         also make the expected disposition obvious (saturation/ceiling, like D4/CAL-E). EXCLUDE.
2026-06-10 lane-1a-sweep — the predecessor sweep, explicitly recorded as an INSTRUMENT FAILURE
         (audit log + stderr both name "INSTRUMENT-FAILURE"; LOCK-RECORD finalized). An instrument
         failure yields no VALID gate-refusal cases with clean per-item raw E3, and it is itself
         instrument-development evidence that shaped the staged metrology. EXCLUDE.
b1-harness-v2 — a harness/baseline validation (PROVENANCE + manifest + results), i.e. instrument
         infrastructure, not a gate REFUSE decision on a candidate. EXCLUDE.
INT8-RUNG-1 — quarantined, non-promotable evidence (a compression rung), not a construct-validity
         gate refusal; promoting/citing it is separately barred. EXCLUDE.
superseded validation runs — retention-validation runs (RUN-*-RETENTION), superseded by a final
         run, that fed the (DONE) baseline-gate diagnosis. They are not obviously gate REFUSE
         decisions, and a desk read cannot confirm whether any contains a clean, non-design-loaded,
         genuinely-uncertain refusal with complete raw E3. HOLD (see §5).
```

## §4. Exclusion table (design-loaded / ineligible cases)

```text
CASE                        EXCLUSION RULE TRIGGERED (readiness note §3)
--------------------------------------------------------------------------------------
CAL-Q                       named spec design target; used in framing; disposition known
CAL-E                       named spec design target; used in framing; known scoring artifact
D4 saturation               used in framing; disposition known; expected answer obvious
no-independent-channel      named spec §11 design target
CAL-A                       design-loaded (Paper A instrument sweep + cal-abce rescore); obvious
CAL-B                       design-loaded (Paper A instrument sweep + cal-abce rescore); obvious
CAL-C                       design-loaded (Paper A instrument sweep + cal-abce rescore)
2026-06-10 lane-1a-sweep    instrument-development evidence; no valid per-item refusal outputs
b1-harness-v2               instrument infrastructure, not a refusal case
INT8-RUNG-1                 quarantined / non-promotable; not a gate refusal
--------------------------------------------------------------------------------------
The four TL-required exclusions (CAL-Q, CAL-E, D4 saturation, no-independent-channel)
are present and explicitly excluded.
```

## §5. HOLD table (needs further model-free path/provenance review)

```text
CASE                         WHAT REVIEW WOULD RESOLVE THE HOLD
--------------------------------------------------------------------------------------
superseded validation runs   A model-free path/provenance read to determine: (1) whether any
  (superseded_run-1/2/3 in    superseded run contains a GATE REFUSE decision (vs only a retention
  .../lane-1a-prime/          measurement); (2) whether complete per-item raw E3 outputs are
  validation/)                present and hashed (provenance vs quarantine); (3) whether it is
                              design-loaded for G6 specifically vs only for the (DONE) baseline-gate
                              diagnosis; (4) whether its expected disposition is genuinely open.
                              Until reviewed, it can be neither admitted nor excluded honestly.
--------------------------------------------------------------------------------------
HOLD does NOT mean eligible. It means undetermined pending review — not begun here.
```

## §6. Recommendation to Manager

```text
PRIMARY: NO ELIGIBLE CANDIDATES FOUND in the current record.
  The calibration sweep that produced the program's refusal cases (CAL-A/B/C/E/Q) is
  design-loaded — it is Paper A's instrument demonstration and the source of both the G6
  design targets and the aggregate-vs-item insight G6's disposition logic encodes. The only
  non-CAL records are instrument failures / infrastructure (EXCLUDE) or superseded retention
  runs (HOLD). No existing refusal clearly satisfies the non-design-target definition AND the
  eligibility criteria.

SECONDARY (if the Manager wishes to pursue Option B despite the above):
  FURTHER INVENTORY NEEDED on the single HOLD case-group (the superseded validation runs),
  per §5 — a model-free path/provenance review. If that review also comes up empty, the honest
  implication is that a genuine non-design-target G6 validity test would require a NEW refusal
  case, not an existing one. (This matches spec §11: reproducing the design targets is the first
  non-vacuousness evidence; demonstrating GENERALIZATION needs cases the instrument was not built
  around — which the current record does not contain.)

NOTHING IS SELECTED. This is a screening result and a recommendation surface; the choice
  among "accept PRIMARY (no eligible; keep Option B parked or seek a new case later)" and
  "authorize the SECONDARY HOLD review" is the Manager's, and is not made or implied here.
```

## §7. Boundaries (held)

```text
- Option B NOT opened.                   - No certification authorized.
- No candidate SELECTED (count 0; and    - No compression authorized.
  no HOLD case admitted).                - No Paper B activation.
- No audit execution authorized.         - No D4 reopening (D4 read as existing record).
- No software build authorized.          - No general G6 validity claim.
- No model execution authorized.         - No product / funder-facing claim.
Route state: YELLOW (model-free). Execution: RED.
```

This is a model-free inventory. It screens every refusal and refusal-adjacent case on record against the filed non-design-target definition and eligibility criteria, excludes the design-loaded calibration sweep (CAL-A/B/C/E/Q — Paper A's instrument demonstration and the basis of G6's disposition logic) and the non-CAL instrument-failure/infrastructure/quarantined records, holds the superseded validation runs pending path/provenance review, and finds NO eligible non-design-target candidate in the current record. It selects nothing, opens no option, and authorizes nothing; D4 stays closed, CAL-Q is not rerun, Paper B stays deferred, and no general-validity or funder-facing claim is made.

---

*G6-NON-DESIGN-TARGET-CANDIDATE-INVENTORY-v0.1 (TL ACTION; model-free; Manager Option C): screens all on-record refusal/refusal-adjacent cases against the filed readiness-note definition (41a416b). §2 inventory table: EXCLUDE×10 case-groups, HOLD×1, ELIGIBLE×0. EXCLUDE — CAL-Q/CAL-E/D4/no-channel (TL-required four: spec design targets + framing-used), CAL-A/B/C (design-loaded: Paper A instrument sweep "exercised this gate directly" + cal-abce rescore that shaped G6's REVERSED logic; clean 1.000/0.975/0.950 = obvious), 2026-06-10 sweep (INSTRUMENT-FAILURE, no valid per-item refusals), b1-harness-v2 (infrastructure), INT8-RUNG-1 (quarantined, not a gate refusal). HOLD — superseded validation runs (retention runs, not gate refusals; eligibility needs path/provenance review per §5). §3 per-candidate rationale; §4 exclusion table (four required exclusions present); §5 HOLD table (what review resolves it); §6 recommendation: NO ELIGIBLE CANDIDATES FOUND (primary) + further HOLD review needed if pursuing Option B + a genuine non-design-target test likely needs a NEW refusal (matches spec §11). Selects nothing; opens no option; authorizes no audit/build/run/cert/compression/Paper B; reopens no D4; claims no general validity; no funder claim. model-free.*
