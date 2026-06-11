# Continuity Finding — Lane 1a Wrapper Implements the Rejected Output-Rewrite (Review-Blocking)

From: Outgoing Senior (continuity advisor, §4 trigger: CS mismatch / artifact-routing problem)
To: Team Lead · Cc: Manager, New Senior, CS Engineer · 2026-06-10
Status: Review-blocking input to the pending combined review. Nothing is locked; no data accessed;
the finding lands at exactly the gate built to catch it.

## 1. Finding

The committed `lane1a_runner_wrapper.py` at `25613d3`
(`experiments/2026-06-10_lane-1a-sweep/`, sha256 verified = CS-enumerated `deff94c9…`) **rewrites the
`context` field of B1 v2's output JSON** to `lane-1a-reconnaissance`. Verified by direct fetch and
source probe: assignment to the output's context key present; no sidecar implementation anywhere in
the Lane 1a tree; no hash-of-B1-output recorded by the wrapper; LOCK-RECORD lists no sidecar schema
artifact; and the **required `--context` functional statement is absent** from both the LOCK-RECORD
and the CS step-3 return.

This is the pattern the Senior step-3 response memo rejected and replaced: a wrapper must never mutate
a runner-emitted field. A rewritten output is no longer what the runner attested — it converts
runner-attested provenance into wrapper-asserted provenance silently, which defeats the reason the
authorization mandates B1 capture at all.

## 2. Root cause — and it is not CS error

The correcting memo (`SENIOR-RESPONSE-LANE1A-STEP3.md`) was **SEND-marked but never commit-confirmed:
a G1-open item at production time** (flagged as such in the onboarding acknowledgment). CS built in
good faith from the last spec they verifiably had — their own draft, whose "honest override" line was
never countermanded in any artifact that reached them. Intent is not delivery; G1 said so, and this is
that rule firing again, now on the instruction channel itself. CS's discipline inside what they built
was excellent: B1 v2 untouched, B-series corrections in, tests passing, lock timestamp left open.

## 3. Required remediation (before the combined review can pass)

1. **Wrapper revision (sidecar pattern):** B1 output preserved byte-verbatim; wrapper records
   sha256 of the emitted output; writes `lane1a_context_sidecar.json` per invocation (true context,
   artifact tags, hash of the annotated output, locked-surface constraint note, audit-log ref);
   analyzer consumes the pair. No write path may touch B1-emitted bytes.
2. **Sidecar schema** joins the artifact list (`additionalProperties: false`, `framework_version`
   const "none", like its siblings).
3. **New unit test:** wrapper processes a fixture B1 output; assert emitted bytes hash-identical
   before and after wrapper processing (the attestation-preservation test — the test that would have
   caught this class).
4. **The `--context` functional statement** (what `--context paper2-reproduction` controls inside
   B1 v2: labeling/routing only, or functional validation). Still required, still absent. If
   functional: escalate to Manager as a named decision; do not code around.
5. **LOCK-RECORD regenerated** with new hashes — clean, because the record is `status: draft` until
   Manager confirmation (the pin exists for exactly this moment). Token-prior line: retain, and at
   Manager confirmation fill the explicit citation (the current "Manager-authorized … path" wording
   asserts authorization without citing it).
6. **Process fix for the checklist:** production cycles may not start while any Senior condition memo
   affecting them is G1-open. Commit-confirm the instruction channel first. (Recommend adding to the
   combined-review checklist permanently.)

## 4. What is not wrong

No gate crossed: first data access never occurred, no model loaded, lock timestamp pending, B1 v2
locked and unedited, B1 v2.1 untouched. Design packet v0.3 and recipe v0.2 are committed (those G1
items closed). The architecture around the one flaw is sound and tested. This is a one-artifact
revision plus one missing statement, caught pre-lock by the review structure operating as designed.

— Outgoing Senior Engineer
