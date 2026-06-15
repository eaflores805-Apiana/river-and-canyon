# CASE-1 — PROVENANCE NOTE (v0.1)

> CONSTRUCTED ARTIFACT — provenance note for the Case 1 Missing-Channel Trap bundle.
> Documents what this bundle is, what it provably lacks (per the design's crux), and
> the sha256 self-hashes of its constructed files so an auditor can verify integrity.

---

## 1. What this provenance note establishes

The Case 1 artifact bundle was constructed by CS Engineer on **2026-06-14**, under
**TL ACTION** (Manager opened Option B design-only; this construction is the
separately-authorized step the design itself named at §7). The bundle instantiates:

```text
G6-OPTION-B-CASE-1-MISSING-CHANNEL-DESIGN-v0.1
path:   tier-1-instrument/modules/g6-standing-rejection-audit/G6-OPTION-B-CASE-1-MISSING-CHANNEL-DESIGN-v0.1.md
commit: 60b0d32
```

No model was queried; no real data is contained; no audit was performed; no G6
software was built; no run, certification, compression, or stress was executed.
Sealed bytes were not touched (this bundle lives outside `experiments/`).

## 2. The crux the design required this note to satisfy

Per design §7:

> "the manifest must positively record that raw E3 is unavailable/insufficient/non-re-readable
> (e.g. a documented 'raw outputs not retained' / 'labels-only export' state), so an auditor can
> VERIFY there is nothing to give a blind channel — rather than the auditor simply not having found
> it. The case fails its purpose if 'no channel' is indistinguishable from 'auditor didn't look'."

This bundle satisfies the crux in **four positively-recorded places**:

```text
1. CASE-1-REFUSAL-RECORD-v0.1.json → original_read.raw_outputs       = "NOT_RETAINED — labels-only export by construction"
2. CASE-1-REFUSAL-RECORD-v0.1.json → original_read.raw_outputs_retained = false
3. CASE-1-REFUSAL-RECORD-v0.1.json → raw_E3_status.available         = false (with verifiability checklist)
4. CASE-1-CHANNEL-MANIFEST-v0.1.json → CH1 / CH2 / CH3 .available    = false (with reason for each)
```

An auditor who is told "go test G6 against Case 1" can read those four fields directly
and confirm "no independent channel" is a **property of the record**, not a failure
to look. The bundle directory also contains **no** file matching raw-output / E3 /
blind-reader / schema-output patterns — verifiable by `ls`.

## 3. Scope-isolation assertion (the second design requirement: channel-absence as the SOLE operative failing condition)

Per design §7: "the construction must ensure no OTHER eligibility failure (it must be a
real refusal, in scope, not quarantined for unrelated reasons) so that channel-absence is
the SOLE operative condition."

CS-enumerated isolation checks (all recorded in the refusal record's `scope_isolation_check`):

```text
✓ is_real_gate_refusal_in_form          = true   (gate_decision = REFUSE on construct-validity grounds)
✓ is_in_g6_audit_scope                  = true   (construct-validity gate refusals are exactly G6's audit scope)
✗ is_quarantined_for_unrelated_reasons  = false  (record is well-formed; provenance complete for what IS present)
✓ summary_metric_well_formed            = true   (numeric, recognizable, mirrors CAL-Q surface)
✓ labels_well_formed                    = true   (40 labels, all "answered_not_abstained", explicit item_ids)
✗ introduces_unrelated_defects          = false  (no malformed fields, no double defects, no procedural anomalies)
  sole_operative_failure_condition      = "no_independent_channel_available"
```

The only failing eligibility condition in this constructed record is the one the
design targets: **no independent channel available**. Any other interpretation
(QUARANTINED / INCONCLUSIVE) by a future G6 would indicate the case is not cleanly
isolated and the construction must be tightened — that outcome would be informative
about either the case (revise this bundle) or G6's discrimination (a separate, useful
finding).

## 4. sha256 self-hashes (constructed bundle files, on disk at construction time)

```text
README.md                          3271e30569882a2e021b6ac250a9e02c2072a6a226e8ea3e3296f78417f1814a
CASE-1-REFUSAL-RECORD-v0.1.json    c66d8bb7c9b474deaf9f3a7ce834ffb58382151b4e885c71b52b619106544b93
CASE-1-CHANNEL-MANIFEST-v0.1.json  9cb91dc168f50aeeae638586c7bcb75ad4b73c98319f77c95be7f7d0258b8a0e
```

(This provenance note's own sha256 will be recorded by the filing commit's tree
hash; it is not self-referenced here to avoid the chicken-and-egg problem.)

## 5. Cross-checks an auditor should perform before treating this bundle as the Case 1 instance

```text
[ ] Verify each file's on-disk sha256 matches the value in §4.
[ ] Open CASE-1-REFUSAL-RECORD-v0.1.json; confirm the four positively-recorded
    raw-E3-absence fields cited in §2.
[ ] Open CASE-1-CHANNEL-MANIFEST-v0.1.json; confirm CH1/CH2/CH3 all .available=false
    with the cited spec §4 line references.
[ ] `ls` this directory; confirm no raw-output / E3 / blind-reader / schema-output
    file exists.
[ ] Confirm the governing-chain commits (41a416b / 1893a63 / 7d880c5 / 60b0d32)
    exist in `git log` and match the artifacts named in the refusal record.
[ ] Confirm the G6 spec citations (§5 line 181, §11 line 278, K1 line 87, §4 lines
    95 + 101) match the bytes of `tier-1-instrument/specs/g6-standing-rejection-audit-spec-v0.1.md`.
```

## 6. What this bundle does NOT do

- does NOT execute any audit (the audit step is separate and not authorized here)
- does NOT build any G6 software
- does NOT run any model
- does NOT certify a baseline
- does NOT produce stress evidence
- does NOT activate Paper B
- does NOT reopen D4
- does NOT claim general G6 validity
- does NOT create any product or funder-facing claim
- does NOT modify any sealed bytes

## 7. Construction authority + audit trail

```text
Authority:    TL ACTION 2026-06-14 ("Construct Case 1 Artifact Bundle or Return HOLD")
Constructor:  CS Engineer (this was a CS construction step, not a Senior drafting step)
Designer:     Senior (G6-OPTION-B-CASE-1-MISSING-CHANNEL-DESIGN-v0.1 @ 60b0d32)
Filer:        CS Engineer (this filing)
Owner:        Manager (Option B design-only path is Manager-authorized)
Route state:  YELLOW (model-free).  Execution: RED.
```

— CS Engineer, 2026-06-14
