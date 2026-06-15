# G6-HOLD-REVIEW-SUPERSEDED-VALIDATION-RUNS-v0.2

**Version:** v0.2. River and Canyon program. Narrow review of the single HOLD bucket from the filed candidate inventory — the three superseded validation runs — against the filed non-design-target definition and eligibility criteria. (v0.2 supersedes v0.1 — v0.1 retained at `tier-1-instrument/modules/g6-standing-rejection-audit/G6-HOLD-REVIEW-SUPERSEDED-VALIDATION-RUNS-v0.1.md`, marked superseded. v0.2 corrects ONE precision overgeneralization flagged in CS verification — see the Correction note; the dispositions are UNCHANGED.)
**Status:** MODEL-FREE HOLD REVIEW (Manager selected the narrow HOLD-review path). It reads existing artifacts and classifies; it opens no option, selects no candidate, runs nothing, authorizes nothing. Anchor: origin/main 7a1ced6.
**Correction note (v0.2):** v0.1's §2 row-5 parenthetical and §4 read-method note overgeneralized "oracle cases carry a pre-declared expected_verdict" to all three runs. Verified: only run-1's oracle carries expected_verdict (9/9 cases); run-2 and run-3 oracles do NOT (0/12 each — the oracle schema changed across iterations). The EXCLUDE disposition for run-2/run-3 is UNAFFECTED — it rests on check 5's documented SUPERSESSION reason (CS-verified verbatim) and on checks 1/2/6/7/8, not on the oracle field. This was an unverified generalization on my part (I checked run-1's oracle and extrapolated); it is corrected here.
**Governing artifact:** `tier-1-instrument/modules/g6-standing-rejection-audit/G6-NON-DESIGN-TARGET-CANDIDATE-INVENTORY-v0.1.md` (FILED 1893a63) — this review resolves its one HOLD row.
**Definition/criteria source:** `G6-OPTION-B-READINESS-NOTE-v0.1` (FILED 41a416b).
**Owner split:** Senior (reviewer/drafter) → CS (verify cited paths + the zero-raw-E3 finding + that no boundary is crossed) → Team Lead (route) → Manager.

---

## §1. What the HOLD bucket is

The three superseded runs under `experiments/2026-06-11_lane-1a-prime/validation/`:

```text
superseded_run-1   RUN-1-RETENTION.md + t1/t3/t4_report.json + oracle_validation_results.json
                   + pilot_manifests_L01.json + execution_ledger.json
superseded_run-2   RUN-2-RETENTION.md + (same report set) + final_manifests + instrument_validation_report.md
superseded_run-3   RUN-3-FIRST-ATTEMPT-RETENTION.md + (same report set) + instrument_validation_report.md
```

All three are marked, in their own retention headers, **"SYNTHETIC / DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION"** and **SUPERSEDED**, retained per E11 / PH5-5 discipline.

## §2. Screen (the 8 required checks, applied to each run from the bytes)

```text
CHECK                                         run-1      run-2      run-3
-----------------------------------------------------------------------------------------
1. Gate REFUSE decision (vs retention only)?  NO         NO         NO     (validation/retention
                                                                            material; the t4
                                                                            "disposition" field is
                                                                            REVIEW-ITEM tracking,
                                                                            and oracle_validation is
                                                                            INSTRUMENT-ORACLE checking
                                                                            — neither is a construct-
                                                                            validity gate refusal)
2. Complete per-item raw E3 outputs present?  NO (0)     NO (0)     NO (0)  (output_text/raw_output
                                                                            occurrences = 0 across
                                                                            t3/t4/oracle in all three)
3. Provenanced/hashed enough vs quarantine?   REPORTS    REPORTS    REPORTS (artifact-level hashes +
                                              only       only       only    E11 retention exist, but
                                                                            of validation REPORTS, not
                                                                            of any raw model outputs)
4. Design-loaded for G6 specifically?         no(*)      no(*)      no(*)   (Phase-5 instrument
                                                                            validation, not a G6 design
                                                                            target — but moot: fails 1/2)
5. Expected disposition known before select?  YES        YES        YES    (each SUPERSEDED for a
                                                                            documented reason — see §3;
                                                                            run-1 oracle ALSO carries a
                                                                            pre-declared expected_verdict
                                                                            [9/9]; run-2/3 oracles do not
                                                                            [0/12] — they rest on the §3
                                                                            supersession reason)
6. ≥1 independent channel plausible?          NO         NO         NO     (nothing to re-classify
                                                                            without raw E3)
7. Expected uncertainty genuinely open?       NO         NO         NO     (superseded for known
                                                                            reasons; verdicts pre-declared)
8. Would reviewing require model execution?   YES to get raw E3         (the raw outputs are NOT
                                              (→ EXCLUDE under RED)       retained; producing them
                                                                          would mean re-running)
-----------------------------------------------------------------------------------------
DISPOSITION                                   EXCLUDE    EXCLUDE    EXCLUDE
```

(*) Not G6-design-loaded specifically, but this does not rescue eligibility — each run fails checks 1, 2, 5, 6, 7, and 8 independently.

## §3. Per-run disposition + rationale

```text
RUN-1  → EXCLUDE.
  Phase-5 run-1 validation artifacts, SUPERSEDED by the corrective Phase-5 v0.2 re-run
  (run-1's failure modes are the documented reason; retained, not erased). It carries
  instrument-validation/retention material — an oracle-validation table (ideal-retriever
  oracle cases with pre-declared expected verdicts) and a review-item disposition table —
  NOT a construct-validity gate REFUSE decision. No per-item raw E3 outputs are present
  (0 occurrences). Expected disposition known (superseded). No channel possible without raw
  outputs. EXCLUDE.

RUN-2  → EXCLUDE.
  Corrective-pipeline run-2, SUPERSEDED as a PREMATURE EXECUTION (run before the required
  PH5-1 joint lock; reason_for_re-pilot records null_abstention_floor_unmet, floor raised
  0.50 → 0.75). Same material class (validation/retention), same absence of per-item raw E3
  (0), same known disposition. Not a gate refusal. EXCLUDE.

RUN-3 (first attempt)  → EXCLUDE.
  SUPERSEDED due to a CS-side construction bug in construct_pilot_manifests (a stratum
  construction defect); retained with the changed fields enumerated. Same material class,
  same absence of per-item raw E3 (0), same known disposition (a construction bug, not an
  open question). Not a gate refusal. EXCLUDE.
```

## §4. Evidence paths used

```text
- experiments/2026-06-11_lane-1a-prime/validation/superseded_run-1/  (RUN-1-RETENTION.md;
    t3_report.json; t4_report.json [rows = review-item dispositions]; oracle_validation_results.json
    [9 oracle cases, pre-declared expected_verdict]; execution_ledger.json; pilot_manifests_L01.json)
- experiments/2026-06-11_lane-1a-prime/validation/superseded_run-2/  (RUN-2-RETENTION.md;
    same report set; instrument_validation_report.md; final_manifests_L01.json)
- experiments/2026-06-11_lane-1a-prime/validation/superseded_run-3/  (RUN-3-FIRST-ATTEMPT-RETENTION.md;
    same report set; instrument_validation_report.md)
Read method: per-item raw-output presence counted by output_text/raw_output occurrences in
each report (all 0); the t4 "disposition" field inspected and found to be REVIEW-ITEM tracking
(review_item_id / blocking_status), not a gate decision; oracle_validation inspected and found
to be instrument-oracle checking (run-1's 9 cases carry pre-declared expected verdicts; run-2/run-3's
12 cases each carry none — their EXCLUDE rests on the supersession reason, not the oracle field).
```

## §5. Provenance status

```text
Artifact-level provenance EXISTS (E11 / PH5-5 retention discipline; hashed validation reports,
e.g. instrument_validation_report sha256 122780d5…). But it is provenance of SUPERSEDED
VALIDATION REPORTS, not of raw per-item model outputs. The eligibility criterion that fails is
not "insufficiently hashed" — it is "no raw E3 outputs exist to provenance or re-classify."
Sealed/retained bytes are not moved or altered by this review.
```

## §6. Final summary

```text
ELIGIBLE-CANDIDATE: 0
EXCLUDE:            3   (superseded_run-1, superseded_run-2, superseded_run-3)
REMAINING HOLD:     0
The HOLD bucket is FULLY RESOLVED — to EXCLUDE, on independent grounds (no gate refusal; no
per-item raw E3; known disposition; no plausible channel; raw E3 only obtainable by re-running).

CONSEQUENCE FOR THE INVENTORY: the candidate inventory's PRIMARY finding now stands firm —
NO eligible non-design-target candidate exists in the current record, and its last uncertain
bucket resolves to EXCLUDE. The honest implication (inventory §6, spec §11) is confirmed: a
genuine non-design-target G6 validity test would require a NEW refusal case, not an existing
one. This review does not recommend constructing one; it reports that the record is exhausted.
```

## §7. Boundaries (held)

```text
- Option B NOT opened.                    - No certification authorized.
- No candidate selected (count 0).        - No compression authorized.
- No audit execution authorized.          - No Paper B activation.
- No software build authorized.           - No D4 reopening.
- No model execution authorized           - No general G6 validity claim.
  (and none performed; reports read only).- No product / funder-facing claim.
Route state: YELLOW (model-free). Execution: RED.
```

This is a model-free HOLD review. Reading the three superseded validation runs from the bytes, each is a superseded Phase-5 instrument-validation/retention pilot — not a construct-validity gate refusal — with no per-item raw E3 outputs and a known supersession disposition; obtaining raw E3 would require re-running, barred under RED. All three are EXCLUDE; the HOLD bucket resolves to ELIGIBLE 0 / EXCLUDE 3 / remaining HOLD 0, confirming the inventory's no-eligible-candidate finding and the implication that a real non-design-target test would need a new refusal. It selects nothing, opens no option, and authorizes nothing; D4 stays closed, Paper B stays deferred, and no general-validity or funder-facing claim is made.

---

*G6-HOLD-REVIEW-SUPERSEDED-VALIDATION-RUNS-v0.2 (TL ACTION; model-free; Manager narrow HOLD-review path; supersedes v0.1, v0.1 retained; corrects one precision overgeneralization per CS verification — dispositions UNCHANGED): resolves the candidate inventory's single HOLD row (1893a63). Reads the 3 superseded Phase-5 validation runs from the bytes against the 8 required checks. FINDING (all three EXCLUDE): (1) NO gate REFUSE decision — they carry instrument-validation/retention material (the t4 "disposition" field is review-item tracking; oracle_validation is instrument-oracle checking — run-1's oracle carries pre-declared expected verdicts [9/9], run-2/run-3's do not [0/12]), not construct-validity refusals; (2) NO per-item raw E3 (output_text/raw_output = 0 across t3/t4/oracle in all three); (5) known dispositions — run-1 superseded by corrective v0.2 re-run, run-2 superseded as premature execution (null_abstention_floor_unmet 0.50→0.75), run-3 superseded by a construct_pilot_manifests construction bug; (6/7) no plausible channel / no genuine uncertainty; (8) raw E3 only obtainable by re-running = execution, barred under RED. Provenance exists for the validation REPORTS but not for any raw model outputs. SUMMARY: ELIGIBLE 0 / EXCLUDE 3 / remaining HOLD 0 — bucket fully resolved; confirms the inventory's NO-eligible-candidate finding + the implication a genuine non-design-target test needs a NEW refusal (spec §11). v0.2 correction: the oracle expected_verdict property holds only for run-1 (verified 9/9; run-2/3 are 0/12); run-2/3 EXCLUDE rests on their supersession reasons, unaffected. Selects nothing; opens no option; runs nothing; authorizes no audit/build/run/cert/compression/Paper B; reopens no D4; claims no general validity; no funder claim. Sealed bytes untouched. model-free.*
