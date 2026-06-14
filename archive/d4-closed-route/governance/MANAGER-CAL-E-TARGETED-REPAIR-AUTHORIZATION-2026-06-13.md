# Manager Authorization — Run CAL-E Targeted Repair Candidate

**Received:** 2026-06-13 via session (TL forwarded Manager memo)
**Filed by:** CS Engineer (verbatim Manager bytes recorded)
**Status:** RECEIVED — narrow FP16/native CAL-E targeted repair run authorized

---

To: CS Engineer
Cc: Senior Engineer, Team Lead
From: Manager
Re: CAL-E targeted repair run
Status: Narrow FP16/native calibration run authorized; all other gates closed

CS,

I approve the next narrow model-facing step: CAL-E targeted repair run.

Use: CAL-E-TARGETED-REPAIR-SPEC-v0.1.md

## Authorized scope
Run CAL-E only. FP16/native only, calibration only, one targeted candidate.

## Purpose
The only question this run may answer is:
Does CAL-E land clean accuracy comfortably inside the band while preserving clean/defective separation?

Target band: 0.6625 < clean accuracy < 0.95
Preferred clean target: 0.88–0.92
Defective target: defective accuracy ≤ ~0.10
Clean − defective separation ≳ 0.78

## Decision rule
BAND PLAUSIBLE: CAL-E clean strictly in 0.6625 < clean < 0.95 and defective stays low enough to preserve separation.
NEEDS REPAIR: CAL-E remains at/above 0.95, drops too close to floor, or defective rises enough to erode separation.
PIVOT WATCH: additional pressure continues to inflate defective or collapse toward floor.

## Closed gates (still closed)
No certification run · No compression · No INT8/INT4 stress · No second compression rung · No full ladder · No candidate certification · No ranking · No Claim C activation · No public benchmark packaging · No funder-facing release · No SBIR submission.

## Return path
CS returns run report + artifact paths → Senior interprets → TL prepares Manager decision surface → Manager decides cert-run-request well-formedness.

— Manager
