# Non-Authorization + Consumption-Side Exclusion Language v0.1 — Lane 1a′

```text
DRAFT / REVIEW ONLY
D1 PACKET-PREPARATION ARTIFACT
NO EXECUTION AUTHORIZED
NO SWEEP_ID CREATED
NO MODEL RUNS
NO DATA GENERATED
NO VALIDATION OUTPUTS POPULATED
```

From: CS Engineer
To: Team Lead, New Senior Engineer
Cc: Senior Engineer, Contributor 5, Contributor 6, Manager
Date: 2026-06-11
Re: Non-authorization + consumption-side exclusion language for Lane 1a′ packet
Status: DRAFT v0.1; verbatim blocks from authorized sources; this artifact installs nothing

---

## 1. Scope

This document carries the verbatim non-authorization and
consumption-side exclusion language that will sit, byte-for-byte, in
the Lane 1a′ packet at lock. The text here is **pulled from authorized
sources** (the adopted Pre-Lock Instrument Validation Addendum; v0.2
proposal §10 and §11; `STANDING-NON-AUTHORIZATIONS.md`) — CS does not
invent containment text. This document is the canonical place where
the Lane 1a′ packet aggregates that language.

Per New Senior D1 ack item 8: *"Non-authorization and consumption-side
exclusion language (verbatim blocks from the v0.2 proposal and the
standing addendum)."*

CS confirms: nothing in this document is novel containment language;
every block is sourced and quoted to its origin.

Authority: D1 design authorization (Manager memo of 2026-06-11; commit
`d80ad4b`); Team Lead direction of 2026-06-11.

## 2. Standing non-authorizations (block A)

**Verbatim from `STANDING-NON-AUTHORIZATIONS.md` (sha256 `d2711b8b…`):**

> Canonical list of lanes that are blocked across the program. Every
> CS memo, every governance filing, and every implementation decision
> must respect this list. Items move OFF this list only by explicit
> Manager authorization filed in `governance/`.
>
> | Blocked lane | Why it's blocked |
> |---|---|
> | candidate selection | Paper 3 candidate-selection memo has not been issued. No certification attempt can proceed without it. Manager-gated. |
> | threshold values | Per Paper 3 §7, thresholds must be pre-registered before any candidate evaluation; no post-hoc tuning permitted. Locking values before candidate selection is the wrong order. |
> | certification evaluation | Requires both candidate selection AND a locked, hash-verified threshold sheet. Neither exists. |
> | new model runs | All work to date uses one model (`Qwen/Qwen2.5-3B-Instruct`, snapshot `aa8e7253...`). Any new model run requires fresh authorization. |
> | re-runs beyond authorized reproduction validation | Paper 2 reproduction (`paper2_regression.py`) is the only authorized validity-check rerun. Anything else needs new authorization. |
> | unconditioned token-prior runs | D1 token-prior control may require a preflight run; that run is **not** pre-authorized by Paper 3 — it requires separate Manager authorization at candidate-selection time. |
> | activation logging | Activation-outlier telemetry was classified as stress-side validation, not baseline certification. Beyond B1 v2 scope. Requires harness extension and separate authorization. |
> | INT8 / INT4 execution | Stress runs. Blocked until a stress-eligible baseline exists. No Two-Hop L1 cell cleared Gate 2; no other candidate certified. |
> | multi-model execution | Single-model is the program's current scope. Multi-model is part of the scaling discussion item (filed 2026-06-09); not authorized. |
> | Fork A reactivation | Fork A artifacts fail the reactivation bar (provenance below B1 standard; result files have empty `provenance: {}` blocks). Cannot be admitted as live evidence regardless of figures. |
> | Claim C activation | The seam/linkage claim. Compositional-seam existence is the program's deliberately blocked claim. Stays blocked across all metrology work, including Paper 3 certification. |
> | Paper 3 execution as an experiment | Paper 3 is a methods/protocol paper. Applying the protocol (selecting a candidate, running certification) is a separate downstream paper requiring separate authorization. |
> | Paper 6 activation | Paper 6 is not in active scope. Listed as a backstop against premature scope expansion. |
> | public benchmark packaging | Tooling and distribution posture is an open team-discussion item (`governance/2026-06-09_scaling-discussion-item/`). Not authorized as a deliverable. |
> | artifact mutation | Locked artifacts (manifests, scorers, runners, result JSONs, tagged manuscripts, locked threshold sheets) must not be edited in place. Any change creates a new artifact with a new hash; corrections file as superseding commits, not history rewrites. |

**Recent partial movement (carried verbatim):**

> **Lane 1a (pre-candidate occupancy / failure-map sweep)** — moved
> from FULLY BLOCKED to PACKET PREPARATION AUTHORIZED per
> `governance/2026-06-10_lane-1a-authorization/MANAGER-AUTHORIZATION.md`.
> First data access remains **NOT AUTHORIZED** until the final
> execution packet passes Team Lead adversarial review AND Manager
> confirms execution start. Lane 1a is **negative-use only** ("may
> rule out; may not rule in") — survivorship is not authorization,
> ranking, or positive evidence. All Lane 1a outputs must carry
> `artifact_class: lane-1a-reconnaissance` /
> `certification_relevance: none` and are excluded from threshold
> design and certification evidence. Consumption-side rule: a later
> threshold sheet must attest no Lane 1a statistic was copied or
> transformed in.

**Lane 1a′ extension of the carve-out (CS reading):** Lane 1a′ is the
corrected reconnaissance design tracked under the v0.2 proposal;
the same "PACKET PREPARATION AUTHORIZED, FIRST DATA ACCESS NOT
AUTHORIZED" posture applies. All Lane 1a′ outputs carry
`artifact_class: lane-1a-prime-reconnaissance` /
`certification_relevance: none` and are excluded from threshold
design and certification evidence under the same consumption-side
attestation requirement.

## 3. Lane 1a′ packet non-authorization block (block B)

**Verbatim from Lane 1a′ Design Proposal v0.2 §11 (sha256 `31e7b9b6…`):**

> This proposal authorizes nothing: no new sweep_id, no model runs,
> no data generation, no execution packet, no pilot execution (itself
> authorized at the packet stage, offline), no candidate selection
> or ranking, no threshold-sheet work, no certification evaluation,
> no stress-retention testing, no B1 v2.1 implementation, no Paper 3
> revision, no Claim C activation, no Fork A reactivation, no Paper 6
> activation, no public benchmark packaging. All execution gates
> remain closed. Per assignment §5, this proposal does not claim
> that Lane 1a′ will find a survivor, that the task family is viable,
> that the model is capable or incapable, that certification is near,
> or that threshold or retention work is authorized.

## 4. No-positive-use block (block C)

**Verbatim from Lane 1a′ Design Proposal v0.2 §10:**

> **No positive use (standing for this lane):** no Lane 1a′ output —
> label, diagnostic, control number, validation result, or report —
> may be used as positive evidence for any model, construction,
> candidate, threshold, or certification purpose. Outputs rule out
> or they say nothing.

## 5. Consumption-side exclusion (block D)

**Inherited from v1 + Standing-non-authorizations + addendum:**

> A later threshold sheet must attest that no Lane 1a′ statistic was
> copied or transformed in. The threshold sheet's locked content must
> declare, per field:
>
>   1. The source of the field's value;
>   2. That the source is not a Lane 1a′ output, diagnostic, control
>      number, validation result, or report;
>   3. That no transformation chain leads back to a Lane 1a′ output.
>
> The attestation is a structural field of the threshold sheet, not a
> review-time annotation.

> The certification evidence bundle must exclude every Lane 1a′
> artifact by `artifact_class`. The bundle-emission code structurally
> filters by `artifact_class != "lane-1a-prime-reconnaissance"` AND
> `certification_relevance != "none"`; the filter is a code-level
> refusal, not a reviewer attestation. (Per CS Execution-Packet
> Proposal v0.1 §12: artifact label emission is a typed-boundary
> interface invariant.)

## 6. Artifact label requirements (block E15 verbatim)

**Verbatim from adopted addendum E15 (sha256 `124f6046…`):**

> oracle/pilot/canary artifacts carry `SYNTHETIC — NON-BINDING — NOT
> FOR THRESHOLD DERIVATION`; diagnostic sweep artifacts carry
> `DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION` or
> `RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION` —
> real outputs are never mislabeled synthetic, and no labeled
> artifact is threshold or certification evidence.

**Lane 1a′ label assignment (CS):**

| Artifact class | Label |
|---|---|
| Oracle cases (A5 pre-flight, synthetic) | `SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION` |
| Pilot manifests | `SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION` |
| Canary records | `SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION` |
| Sweep outputs (final manifests, runner-attested) | `RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION` |
| Validation report (sealed) | `RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION` |

Label emission is enforced at code level (CS Execution-Packet
Proposal v0.1 §12).

## 7. Report-level non-claim (E16 verbatim)

**Verbatim from adopted addendum E16 (sha256 `124f6046…`):**

> a Validation Report PASS means pre-lock adequacy on declared cases,
> pilots, and required checks only. It is not candidate evidence,
> not general field validity, not certification evidence, and not
> threshold support.

**Lane 1a′ extension (verbatim from v0.2 §8):**

> A Validation Report PASS authorizes nothing; it is a precondition
> for requesting execution authorization, not a substitute for it.

## 8. Evidence-bundle exclusion

The Lane 1a′ Validation Report and all Lane 1a′ artifacts (oracle
cases, pilots, sweep outputs, T1–T4 tables, audit log, LOCK-RECORD)
are excluded from any certification evidence bundle. The exclusion is
implemented at code level via the artifact-label classification
filter (block 5 above + CS Execution-Packet Proposal §12).

The certification evidence bundle's emission code includes the
following invariant:

```python
def emit_certification_evidence_bundle(...) -> EvidenceBundle:
    """
    INVARIANT: filter out any artifact whose artifact_label is one of:
      SYNTHETIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
      RECONNAISSANCE — NON-BINDING — NOT FOR THRESHOLD DERIVATION
      DIAGNOSTIC — NON-BINDING — NOT FOR THRESHOLD DERIVATION
    
    These artifacts are not certification evidence by code-level
    refusal; the filter is not a reviewer attestation.
    """
```

(This block is a forward declaration of behavior the certification
evidence bundle's emitter must obey when it is later authorized; it
does not authorize emission of any evidence bundle now.)

## 9. Threshold-sheet exclusion

The threshold sheet (when later authorized) must include an
attestation field per block 5 above:

```yaml
threshold_sheet:
  per_field_source_attestation:
    - field_name: <field>
      source: <source artifact identifier>
      source_artifact_class: <source artifact class>
      not_lane_1a_prime: true        # attestation
      transformation_chain_clean: true  # attestation
```

Per `STANDING-NON-AUTHORIZATIONS.md`, threshold-sheet work is itself
blocked under standing governance and is unblocked only by a
separate Manager authorization. This block is a forward declaration
of behavior the threshold sheet's emitter must obey when it is later
authorized.

## 10. Scope-guard (instrument-only) — verbatim addendum §1

**Verbatim from adopted addendum §1 (sha256 `124f6046…`):**

> **Instrument-only scope guard:** This addendum defines
> instrument-validation requirements for diagnostic batteries and
> controls only. Compliance with these requirements is necessary for
> instrument credibility but does not constitute, imply, or authorize
> candidate certification. Certification criteria remain separately
> governed and require Manager authorization.

**Verbatim from v0.2 §2 P4 citation scope:**

> Lane 1a is cited solely as a documented case of instrument failure
> in a reconnaissance classifier. It may not be used to support any
> claim regarding model capability, task-family viability, positive
> retrieval performance, or Paper 3 certification-gate behavior. No
> Lane 1a label or statistic may be reinterpreted as evidence of
> successful single-hop retrieval.

> **Classifier/certifier scope guard:** Lane 1a demonstrated a
> false-reject mechanism in a reconnaissance classifier. It did not
> measure the false-reject rate of any Paper 3 certification gate,
> and no formalized Paper 3 certification gate has yet been exercised
> — Lane 1a labels were sweep classifications, not Paper 3
> certification-gate verdicts.

> Lane 1a v1 numeric levels may be referenced only as
> instrument-failure diagnosis; they may not be used as evidence for
> Lane 1a′ viability, model capability, task-family suitability, or
> candidate readiness.

## 11. R6 inheritance (forward to future packets)

Per adopted addendum §8 R6, this section's content carries forward
into the R6 inheritance screen of any future packet that integrates
with Lane 1a′ outputs (e.g., a follow-on reconnaissance lane, a
candidate-selection memo authoring process, a threshold-sheet
preparation process).

The R6 screen of every such future packet must:

- screen this section's non-authorizations, no-positive-use rule,
  consumption-side exclusion, artifact labels, report-level
  non-claim, and scope-guard text;
- mark each as `adopted` / `adapted with rationale` / `declined with
  rationale`;
- never silently un-inherit.

CS reads the standard R6 disposition for Lane 1a′ outputs in any
future packet as: **all eleven blocks here are `adopted` by
default; any `adapted` or `declined` requires explicit rationale.**

## 12. CS sign-off

```text
Document status:                  DRAFT v0.1
D1 packet-preparation artifact:   YES
Execution authorized:             NO
sweep_id created:                 NO
Model runs:                       NO
Data generated:                   NO
Validation outputs populated:     NO

Verbatim source attribution:
  Block A (§2):   STANDING-NON-AUTHORIZATIONS.md (sha256 d2711b8b...)
  Block B (§3):   v0.2 §11
                  (governance/2026-06-11_lane-1a-prime/
                   LANE1A-PRIME-DESIGN-PROPOSAL-v0.2.md;
                   sha256 31e7b9b6...)
  Block C (§4):   v0.2 §10 no-positive-use
  Block D (§5):   v1 + Standing-non-authorizations + addendum
  E15 (§6):       adopted addendum E15
                  (governance/standing/
                   PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM.md;
                   sha256 124f6046...)
  E16 (§7):       adopted addendum E16
  Scope-guard (§10): adopted addendum §1 + v0.2 §2

Next:                             cross-review with New Senior
                                   design packet + T1-T4 plans;
                                   refine label-class language at
                                   T2/T3 review;
                                   joint return to Manager at D2 gate

Eleven blocks all sourced; no novel containment text introduced.
```

— CS Engineer, 2026-06-11
