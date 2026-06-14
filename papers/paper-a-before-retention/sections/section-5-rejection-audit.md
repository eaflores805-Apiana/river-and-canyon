# PAPER-SECTION-5-REJECTION-AUDIT-DRAFT-v0.1

**Version:** v0.1. River and Canyon program. DRAFT of §5 (Rejection Audit) for Paper A — the first paper section built as substance rather than framing in this drafting pass. Companion to §2 (positioning) and §3 (instrument architecture). **Status:** model-free draft of academic prose, written in Paper 1's house style (read from /mnt/project/survivalisnotcorrectness.pdf: declarative cadence, "what it does not license" boundary discipline, tables that separate kinds of object). This section converts the highest-value SPECIFIED-BUT-UNBUILT module (§3.4) into a specified control with a worked evidentiary spine. It does not require a model run: it is built on the already-on-disk CAL-E and CAL-Q records. Anchored on origin/main HEAD 0f7e9a7. Authorizes nothing; model-free; pre-stress. **Evidence anchors (byte-verified this turn):** CAL-E defective strict_OLD=0.575 (apparent collapse) → item read: abstention_forms {NONE:23, none:13}, true false-emission 0.10, concept abstention 0.90 — a refusal-eligible aggregate that item-level reading REVERSED. CAL-Q defective abstention 0.000, false-emission 1.000, format_abstention_artifact size 0.0 — a refusal that item-level reading CONFIRMED. The symmetry is the section's spine. Owner/drafter: Senior Engineer · CS: verify the CAL-E/CAL-Q numbers and the audit-procedure claims against artifacts · Team Lead: route into paper draft surface · Manager: scope.

---

## DRAFTING NOTES (internal — not part of the paper)

```text
WHY THIS SECTION, WHY NOW: an external review and the program's own methodology
record both name the rejection audit as REQUIRED before the non-vacuousness claim of
§2.4/§3 holds — a fail-closed instrument with nine documented reasons to refuse and
no guard against its own conservatism is only half-validated. Prior drafting passes
hardened the framing (§2, seven rounds) while this — substance — stayed a stub. This
section is the deliberate correction: build the work, not the argument for it.
THE SPINE: the CAL-E/CAL-Q contrast is a natural over-rejection control already on
disk. CAL-E is a refusal-eligible aggregate that per-item reading REVERSED (the
"failure" was mostly a parser artifact). CAL-Q is a refusal that per-item reading
CONFIRMED. The same procedure applied to both — and the audit is precisely the
discipline that the procedure must fire on REFUSALS, not only acceptances, so the one
time a refusal would be wrong gets caught.
HONESTY BOUND: this section SPECIFIES the audit and demonstrates its necessity on two
real cases; it does NOT claim the audit is implemented as a standing automated
component (it is not — see §5.4). The claim is "specified, motivated by a worked
reversal, and required" — not "built and validated across many cases."
STYLE: Paper 1 voice — declarative key sentences; state what each check does and what
it does NOT license; separate kinds of object.
```

---

## 5. The Rejection Audit: Auditing the Instrument's Own Refusals

### 5.1 Why a fail-closed instrument must audit its refusals

A fail-closed instrument is designed to refuse. The protocol of §3 carries many reasons to withhold a result — an uncertified baseline, a saturated clean score, a failed shortcut floor, a scorer artifact, a collapsed construct, an unsealed provenance trail, a nonconforming route. This is the intended behaviour. It is also a latent failure mode: an instrument with many reasons to refuse and no guard against its own conservatism can refuse a valid construct as readily as an invalid one, and a gate that refuses everything is as useless for measurement as one that refuses nothing. Over-acceptance — passing an invalid baseline — is the failure the rest of the protocol is built to prevent. Over-rejection — refusing a valid one — is the symmetric failure, and it is the one a fail-closed design is structurally most prone to, because every gate is oriented toward refusal and none, by default, toward checking that a refusal was warranted.

The rejection audit is the control for over-rejection. Its claim is narrow and symmetric: the same per-item discipline the protocol applies before accepting a result must also be applied before *trusting a refusal*. A refusal is a decision with consequences — it removes a candidate baseline, it can trigger a route pivot, it can end a measurement line — and a decision with consequences must itself be auditable. The audit does not weaken the fail-closed posture; it completes it, by making the refusals as accountable as the acceptances.

### 5.2 The audit procedure

For any refusal the instrument issues, the rejection audit asks four questions before the refusal is treated as sound. The questions are not a softening of the gate; they are the evidence a refusal must survive to be load-bearing.

```text
R1. Is the refusal supported by a per-item read, or only by an aggregate?
    A refusal driven by an aggregate alone is provisional until the items are read.
R2. Could the refusal be a scoring artifact rather than a construct failure?
    The same strict-versus-concept and format-artifact checks that guard acceptance
    must be run on the refused case, because a parser that mis-scores a correct
    output produces a false refusal exactly as it produces a false acceptance.
R3. Do the per-item reads confirm the refusal, or reverse it?
    The read either substantiates the refusal (the defect is real) or overturns it
    (the apparent defect was an artifact). Both outcomes are recorded.
R4. Was the decision rule pre-declared, or fitted after seeing the result?
    A refusal under a pre-registered rule is sound; a refusal under a rule chosen
    after the aggregate was seen is post-hoc and is flagged as such.
```

What the audit does **not** license: it does not convert a refusal into an acceptance on appeal, and it does not permit a refused baseline to be used for a claim once any defect is confirmed. It changes one thing only — whether a refusal is treated as established or as provisional-pending-read. Its output is not "accept or reject" but "this refusal is confirmed by item-level evidence" or "this refusal is not yet supported and must be read before it is acted on."

### 5.3 The audit demonstrated on two real refusals: reversal and confirmation

The audit's necessity is not hypothetical. The program's own development contains two refusal-eligible cases that the audit procedure would govern, and they resolve in *opposite directions* — which is exactly why the audit cannot be skipped: an instrument that always confirmed its refusals, or always reversed them, would not need an audit, but one whose refusals are sometimes right and sometimes artifacts does.

**CAL-E — a refusal the audit would have REVERSED.** On the defective (key-absent) items, the strict scorer reported an accuracy of 0.575, an aggregate that on its face looks like a discrimination failure and would license a refusal of the baseline. Applying the audit: R1 (read the items) and R2 (check for a scoring artifact) together overturn it. The per-item read showed that of the apparent failures, the dominant cause was a case-sensitive parser scoring a lowercase abstention (`none`) as a wrong answer: the observed abstention forms were `NONE` (23, scored correct) and `none` (13, mis-scored wrong), with only 4 genuine false-emissions. The construct-level abstention was in fact 0.90, not the strict 0.575, and the true false-emission rate was 0.10. The refusal-eligible aggregate was mostly a scoring artifact. A pipeline that acted on the aggregate without the audit would have refused (or pivoted on) a baseline whose apparent defect was an artifact of the scorer, not a property of the model — a *false refusal*. The audit's R1–R2 catch exactly this.

**CAL-Q — a refusal the audit CONFIRMS.** On the CAL-Q defective items, the aggregate again looked like a discrimination failure: abstention 0.000, false-emission 1.000. Applying the same audit: R1 (read the items) and R2 (check for a scoring artifact) this time *substantiate* the refusal. The per-item read confirmed that all forty key-absent outputs were genuine single-character value emissions — the format-abstention artifact fraction was 0.0, with no abstention of any form concealed in the outputs — so the collapse was a real change in the model's behaviour, not a parser miss. The refusal stands. The same procedure that reversed CAL-E confirms CAL-Q.

The two cases together are the argument for the audit. The identical aggregate signature — defective accuracy that looks like collapse — meant *opposite* things in the two cases, and only the per-item audit distinguished them. Without R1–R2, CAL-E would have produced a false refusal and CAL-Q a true one, and the instrument would have had no way to tell which was which. With the audit, the reversal and the confirmation are both grounded in item-level evidence, and the refusal is sound in exactly the case where it is warranted.

```text
Summary of the two governed cases (byte-verified):
  CASE    aggregate (defective)         audit outcome    refusal status
  CAL-E   strict accuracy 0.575         REVERSED (R1,R2) false refusal averted
          -> read: abstention 0.90,     the apparent     (defect was a parser
             true FE 0.10, forms        defect was a      artifact, not the model)
             NONE:23 / none:13          scoring artifact
  CAL-Q   abstention 0.000, FE 1.000    CONFIRMED (R1,R2) refusal sound
          -> read: 40/40 genuine        the defect is     (construct genuinely
             single-char emissions,     real              collapsed)
             format-artifact 0.0
```

### 5.4 Status and what this section does not claim

The rejection audit is, at the time of writing, **specified and demonstrated as necessary, not implemented as a standing automated component.** What exists on disk is the procedure (R1–R4), and two real cases (CAL-E, CAL-Q) on which the procedure's necessity is shown — one reversal, one confirmation, both grounded in per-item reads that were actually performed. What does not yet exist is an automated audit that runs R1–R4 over every refusal the instrument issues and emits a logged audit record; the per-item reads in §5.3 were performed by hand, and the section's honesty rests on that being stated plainly. We therefore claim that the audit is *required* (a fail-closed instrument is only half-validated without it), *specified* (R1–R4), and *shown necessary on two real refusals that resolve oppositely* — and we do not claim it is a built, automated, broadly-validated component. Implementing R1–R4 as a standing control, and exercising it across more than the two cases here, are stated as required next work; the design is model-free, and the implementation does not depend on a compression rung.

This section also completes a symmetry in the paper's own argument. §3 demonstrates that the instrument refuses a baseline that surface metrics passed (the non-vacuousness of the gate on the *acceptance* side); §5 specifies how the instrument checks that its refusals are themselves warranted (the *rejection* side). An instrument that only demonstrated the first would be open to the objection that it refuses too readily; specifying the audit, and showing it would have reversed a real refusal (CAL-E) as well as confirmed one (CAL-Q), is the answer to that objection.

---

## POST-DRAFT REVIEW (internal)

```text
INTEGRITY CHECK — does the section claim only what is built/shown?
  - Procedure R1-R4: specified. OK.
  - CAL-E reversal: byte-verified (strict 0.575, forms NONE:23/none:13, concept 0.90,
    true FE 0.10). Stated as a refusal the audit REVERSES. OK.
  - CAL-Q confirmation: byte-verified (abstention 0.000, FE 1.000, format-artifact 0.0,
    40/40 genuine). Stated as a refusal the audit CONFIRMS. OK.
  - §5.4 states plainly: specified + shown-necessary, NOT implemented/automated/broadly
    validated; per-item reads were BY HAND. The over-claim trap (presenting a designed
    control as a built one) is explicitly avoided. OK.
ADDRESSES THE REVIEWER: this converts the highest-value SPECIFIED module into real
  section content with a worked, byte-verified spine — "build the work, not the
  argument for it." It does NOT pretend the audit is automated.
STYLE: Paper 1 cadence (declarative; "what it does not license"; a table separating
  the two governed cases). Matches house voice.
RESIDUAL / OPEN:
  - §5 should eventually cite the §4 D1-D7 spec for where R2's strict-vs-concept and
    format-artifact checks are defined (currently §4 is a stub — this is the next build).
  - the two-case basis is N=2; the section says so. More cases strengthen it; none are
    required to make the necessity argument, which turns on the OPPOSITE resolutions.
```

---

## Closed gates

```text
No new run · No D4 rescue · No CAL-Q rerun · No certification · No compression · No
INT8/INT4 stress · No second compression rung · No full ladder · No Claim C
activation · No public benchmark packaging · No funder-facing release · No SBIR
submission. This is a model-free draft of a paper section, built on existing on-disk
records (CAL-E, CAL-Q). No run was performed or is implied.
```

— Senior Engineer
