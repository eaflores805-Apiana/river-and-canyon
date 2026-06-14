# TIER-1-G6-ENTRY-FRAMING-v0.1

**Version:** v0.1. River and Canyon program. Entry framing for the transition into Tier 1 instrument work (the G6 standing rejection-audit path).
**Status:** MODEL-FREE FRAMING. Explains why the program now turns from carrying the D4 family toward certification into strengthening the Tier 1 eval-validity instrument. It authorizes no execution, no build, and resolves nothing. Anchor: origin/main 931b81a.
**Builds on (does not reopen):** the accepted Baseline Gate Diagnosis (Stage E, done); `BASELINE-GATE-REPAIR-DESIGN-v0.1` (filed, accepted as the model-free endpoint for the structural-limit edge); the existing `EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1` and `G6-STANDING-REJECTION-AUDIT-SPEC-v0.1` (both CS-verified; the sources of truth for the instrument and the G6 module). This framing names a path; it does not redraft those specs.
**Owner split:** Senior (drafter) → CS (verify consistency with the Tool Spec / G6 spec + that nothing here authorizes a build or run) → Team Lead (route as Tier-1 entry; keep separate from D4, CAL-Q diagnostics, and Paper B) → Manager.

---

## §0. The distinction this framing holds (stated first)

```text
Tier 1 / G6 work STRENGTHENS THE INSTRUMENT — it makes the gate's refusals
  auditable, so a refusal can be shown justified rather than asserted.
It does NOT:
  - resolve the structural-limit risk (that needs a future GREEN certification run);
  - certify a baseline (none is certified; none is claimed);
  - produce stress evidence (no compression rung has run; the program is pre-stress).
Strengthening how the instrument audits its refusals is a different axis from
measuring anything with it. This framing moves the program along the instrument
axis only.
```

## §1. Current accepted state (from the record, restated not reinterpreted)

```text
- PROGRAM-MAP-v2.0 / Reading C STANDS. The route is: foundation earned → Lane 1a′
  accepted (non-driving) → Baseline Gate Diagnosis (done) → [if a certifiable
  baseline is reachable] certification track → Lane 4 → long horizon.
- BASELINE GATE DIAGNOSIS is DONE (CS-verified, Manager-accepted, Stage E PASS):
  primary FIXABLE DESIGN/CALIBRATION + secondary VALID REJECTION, with one narrow
  STRUCTURAL-LIMIT risk not yet ruled out.
- BASELINE-GATE-REPAIR-DESIGN-v0.1 is FILED and accepted as the MODEL-FREE
  ENDPOINT for that structural-limit edge: it specifies the off-ceiling construct
  whose certification WOULD test the risk, and stops at the GREEN boundary.
- NO certification run is authorized. Execution is RED.
- D4 remains CLOSED unless the Manager explicitly reopens it. This framing does
  not reopen it; it turns to a different, model-free axis of work.
```

The repair design did the honest maximum on the D4/structural-limit edge: it carried that question as far as a model-free step can, to a ready-to-propose design. The next move on *that* edge would be a GREEN certification run, which is not authorized. So the program turns to the work that is available now and does not require execution: strengthening the Tier 1 instrument.

## §2. Why Tier 1 / G6 is the next model-free path

```text
1. The D4 pivot produced a VALUABLE NEGATIVE RESULT. The gate refused the family's
   purpose-built baselines — and the diagnosis showed those refusals were sound
   (saturation rightly guarded; shortcut-prone constructs rightly eliminated).
   That refusal behavior IS the instrument's contribution to date. Paper A's whole
   claim is that trustworthy refusal — "not safe to compare" — is the product.
2. THE INSTRUMENT MUST AUDIT ITS OWN REFUSALS. A gate that refuses is only as
   trustworthy as its ability to show a given refusal was justified rather than
   miscalibrated. Right now the program HAS standing refusals on the record (the
   D4 saturation refusal; the CAL-Q construct-validity refusal) but no standing
   MECHANISM that audits whether each was justified. That gap is exactly what G6
   names. The current moment makes it concrete: we have refusals to audit.
3. G6 IS THE FIRST MISSING MODULE, already named high-value. The Tool Spec
   implements G1–G5 (per Paper A §4.3) and SPECIFIES G6–G9; the G6 standing
   rejection-audit is the spec'd-but-unbuilt core (Paper A §6.3). Of the specified
   modules, G6 is the one whose absence most directly weakens the product claim
   ("trustworthy refusal"), because without it a refusal cannot be independently
   confirmed.
4. THIS PATH STRENGTHENS THE TOOL WITHOUT EXECUTION. Auditing refusals is a
   reading-and-design discipline over existing records and the gate's own logic —
   it needs no model run, no certification, no compression. It is genuinely
   model-free, which is why it is the right next direction under YELLOW.
```

## §3. What G6 should and should not do (consistent with the existing G6 spec)

```text
G6 SHOULD:
  - audit STANDING REJECTIONS / refusals — when the gate returns REFUSE, produce a
    disposition on whether the refusal was justified (the spec's outputs:
    CONFIRMED / REVERSED / QUARANTINED / INCONCLUSIVE / AUDIT-CIRCULARITY);
  - PREVENT CIRCULAR SELF-APPROVAL — an audit that re-runs the same read that
    produced the refusal is not independent; it inherits the verdict it is meant to
    check. The spec's mechanism: an independent channel must re-classify from the
    RAW per-item outputs (E3), not from the original read's labels (E2);
  - PRESERVE INDEPENDENT REVIEW CHANNELS — at least one of: a blind second human
    reader, a pre-registered schema, or externally-sourced labels. Zero channels
    available ⇒ the audit returns a LIMITED status (AUDIT-CIRCULARITY), never a
    silent confirmation. (The construct-validity semantic read stays HUMAN — Tool
    Spec §8 / G6 K6; G6 does not automate that judgment.)

G6 SHOULD NOT:
  - BECOME A MODEL RUN — G6 is an audit over existing refusal records and gate
    logic; it does not call a model, run inference, or execute anything;
  - TURN REFUSAL INTO A PRODUCT CLAIM — confirming a refusal was justified is an
    internal validity statement, NOT a market/funder claim and NOT "the gate works
    generally" (thresholds remain construction/model/task-specific until
    independently justified — Tool Spec C5 / G6 K-note);
  - ACTIVATE PAPER B — G6 strengthens the instrument; it is not the stress
    experiment, does not require a certified baseline, and does not touch the
    seam.
```

A useful first model-free G6 step (named, not authorized here — a later routed memo would scope it): apply the G6 audit framework *retrospectively* to the refusals already on the record — the D4 saturation refusal and the CAL-Q refusal — as a desk exercise against the spec's validation targets (CAL-Q ⇒ expected CONFIRMED; CAL-E ⇒ expected REVERSED; no-channel ⇒ AUDIT-CIRCULARITY). That exercises the audit on real refusals without any execution, and tests whether the spec's design actually discriminates justified from unjustified refusals.

## §4. The honest tension this framing must name (per the North Star's own warning)

The North Star is explicit, and this framing would be dishonest to omit it: *"a tool whose refusals never lead to valid measurement is not yet a usable measurement tool... If the control apparatus grows while the measurement apparatus does not, the program has built a gate that guards an empty room. Governance is accountable to measurement, not a replacement for it."*

```text
G6 is CONTROL-APPARATUS work. It is the right model-free next step, AND it adds to
the control side of the ledger while the measurement side (a certified baseline, a
stress rung) stays gated. That is acceptable HERE because:
  - the measurement side is RED by Manager decision, not by neglect — the repair
    design carried it to the GREEN boundary and stopped correctly;
  - G6 closes a NAMED weakness in the product the program actually has (refusal),
    not a speculative one;
  - the retrospective audit (§3) produces a real result on real refusals.
But the standing caveat travels with this work: G6 strengthening is NOT a
substitute for ever measuring. The program should remain clear-eyed that the move
that changes its epistemic position is still a future certified baseline + an
authorized rung — and G6 must not become the reason that move keeps being deferred.
This framing names the tension so it is chosen with eyes open, not drifted into.
```

## §5. What remains closed

```text
- No certification run.            - No Claim C / seam activation.
- No model execution.              - No external release.
- No compression / INT8 / INT4.    - No G6 software build / implementation
- No second compression rung.        (G6 work here is model-free spec/audit-design
- No full ladder.                    + retrospective desk audit; NOT a build).
- No Paper B activation.           - No public benchmark packaging / funder-facing
- No D4 reopening (Manager-only).    release / SBIR.
- No promotion of quarantined INT8-RUNG-1.   - No turning refusal into a product claim.
- No analogy used as evidence.
Route state: YELLOW (model-free). Execution: RED.
```

This is model-free framing only. It explains why the program now moves from the closed D4 / repair-design path onto the Tier 1 instrument axis — specifically the G6 standing rejection-audit, the first missing module, whose job is to make the gate's refusals auditable and non-circular. It strengthens the instrument; it does not resolve the structural-limit risk, certify a baseline, or produce stress evidence — and it carries the North Star's standing reminder that control work must remain accountable to eventual measurement, not a substitute for it.

---

*TIER-1-G6-ENTRY-FRAMING-v0.1 (TL ACTION; model-free entry framing for the Tier 1 / G6 transition): §1 current accepted state (Reading C stands; diagnosis done; repair design filed as model-free endpoint; no cert run; D4 closed unless Manager reopens); §2 why Tier 1/G6 is next (D4 pivot = valuable negative result; the instrument must audit its own refusals; G6 = first missing module, the spec'd-but-unbuilt core of the product claim; strengthens the tool without execution); §3 what G6 should do (audit standing rejections; prevent circular self-approval via raw-output independent channel; preserve independent channels; construct-validity read stays human) and should NOT do (become a model run; turn refusal into a product claim; activate Paper B) — consistent with the existing CS-verified G6 spec; names a model-free first step (retrospective audit of the D4 and CAL-Q refusals against the spec's validation targets); §4 the honest North-Star tension (G6 is control-apparatus work; governance accountable to measurement; G6 must not become the reason measurement stays deferred); §5 closed gates. Holds the STRENGTHENS-not-RESOLVES distinction throughout. Reopens nothing; claims no resolution, no certified baseline, no stress evidence; authorizes nothing. model-free.*
