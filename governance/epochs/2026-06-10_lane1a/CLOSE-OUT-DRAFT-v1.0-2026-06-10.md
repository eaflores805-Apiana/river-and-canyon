# Lane 1a Close-Out — Document of Record

**Program:** River and Canyon · Apiana AI, Inc. · E. A. Flores, Manager
**Document class:** Governance close-out (archival)
**Prepared by:** Senior Engineer, at Manager request, from the Team Lead close-out draft of 2026-06-10
and the Senior and CS post-run interpretation memos. **Effective upon Team Lead and Manager adoption.**
**Intended path:** `governance/2026-06-10_lane1a/CLOSE-OUT.md`
**Date:** 2026-06-10

---

## 1. Identifiers

| Field | Value |
|---|---|
| Lane | 1a — pre-candidate occupancy / failure-map sweep (negative-use only) |
| Sweep ID | `lane-1a-2026-06-11` |
| Design packet | `governance/2026-06-10_lane1a/DESIGN-PACKET-v0.3.md`, sha256 `f1280a8563bbb48c5592c35c809be6c739859234cbf33b64a3786c6e5df67bab` |
| Execution commit | `ec7390f` |
| CS interpretation commit | `dd1c175` |
| Sweep record | `experiments/2026-06-10_lane-1a-sweep/sweep_record.json`, sha256 `f10f777c…` (Senior-recomputed from raw bytes) |
| Audit log | `experiments/2026-06-10_lane-1a-sweep/AUDIT-LOG.ndjson`, sha256 `cf02549b…` |
| Operative framework | `paper3-certification-protocol-v1.1` (Lane 1a is NOT a certification activity; `framework_version: "none"` in all sweep artifacts) |
| Artifact tags | `artifact_class: lane-1a-reconnaissance` · `certification_relevance: none` |
| Doctrine | Lane 1a may rule out; Lane 1a may not rule in. |

## 2. Result of record (two layers; both binding)

**Layer 1 — Mechanical verdict.** The locked classifier emitted **K = 0**: all 8 rungs carried at
least one elimination label under the pre-registered sweep classification. The locked fixed-outcome
statement, emitted verbatim by the analyzer's boolean rule:

> "The certification window, while logically nonempty, was unoccupied for this task family at this
> scale: every rung carried at least one elimination label under the pre-registered sweep
> classification."

The mechanical verdict stands. It is not relabeled, rescored, widened, or corrected after the fact.
The locked rules were the locked rules.

**Layer 2 — Controlling interpretation.** Post-run inspection of the committed code, raw outputs, and
per-policy diagnostics — performed independently by Senior (code-mechanism route) and CS
(quantified-score and raw-output route), converging on identical findings — established that **three
universal elimination labels were instrument-confounded.** Accordingly:

> Lane 1a v1 completed cleanly and emitted K=0 under locked rules. Post-run Senior and CS audits found
> that three universal elimination labels were instrument-confounded: the declared-policy envelope
> collapsed to 1.000 because two policies reduced to retrieval oracles; the token-prior control
> measured retrieval under scrambled bindings rather than prior emission; and the abstention criterion
> excluded perfect abstention. The K=0 verdict is therefore mechanically valid but cannot be used as
> substantive evidence of model failure, task-family non-viability, candidate certifiability, or
> certification-window occupancy. The sweep is archived as a **fail-closed instrument-discrimination
> finding**. All downstream gates remain closed.

## 3. Execution record

1,536 / 1,536 planned generations completed (768 candidate + 768 control); runner_started 32,
runner_completed 32, runner_anomaly 0, re-execution 0; analysis_completed 1; 9 plots; 32/32 sidecar
attestations; sweep duration 12.9 minutes; B1 v2 source unedited throughout; B1 v2.1 not created or
used. The run was not an operational failure; the provenance and audit machinery performed exactly as
designed, and the completeness of that record is what made the Layer-2 findings provable rather than
arguable.

## 4. Controlling instrument findings

### Finding A — The declared dummy-policy battery became degenerate (envelope label confounded)

`homogeneous_prefix_completion` selects the in-context key with the longest common prefix to the
queried key; on every answerable item the queried key is itself in the list and self-matches at full
length, so the policy returns the queried key's own value — a retrieval oracle. `target_recency`
(first-character match) oracles identically on K=low, where the recipe guarantees unique first
letters. CS quantification (L01; pattern holds on every rung): pure_last_position 13/80 (16.3%),
target_recency 80/80 (100%), salient_endpoint 13/80 (16.3%), copy_completion 0/80 (0%),
homogeneous_prefix_completion 80/80 (100%). Union envelope = **1.000 on every rung**, rendering the
classification inequality `strict ≤ envelope + 2·SE` automatically true for any candidate, perfect
retrievers included. The pre-lock acceptance gate (non-constant predictions, ≥3 distinct values)
passed both oracles: **non-constant ≠ non-degenerate.**

*Supported archival reading:* candidate accuracy did not exceed the declared-policy union envelope
under the locked rule, but the envelope was 1.000 because two declared policies reduced to retrieval
oracles; the label is instrument-confounded and supports no substantive shortcut interpretation.
*Unsupported readings (do not use):* "declared dummy policies explained candidate accuracy"; "the
candidate failed D2"; "the model was relying on shortcuts."

### Finding B — The token-prior control measured retrieval under scrambled bindings (token-prior label confounded)

The control's expected answer was assigned **post-scramble** (manifest_generator.py,
`answerable_mirror` branch, verbatim code comment: "After scrambling, the 'correct' answer is whatever
value is now at the queried key's position."). The control therefore scored retrieval on a shuffled
list — the same skill as the candidate condition — not answer-without-signal. Observed control
accuracy 0.76–0.98 across rungs versus a ≈3.8% chance floor for the 26-value pool; CS raw-output
example: queried_key `rjdyji`, expected `echo` (post-scramble), raw output `echo` — correct lookup.

*Supported archival reading:* the control condition measured retrieval under a changed binding
assignment rather than token-prior emission; the token-prior indistinguishability label is
instrument-confounded and supports no conclusion that candidate behavior was driven by token priors.
*Unsupported readings (do not use):* "the model tracked token-prior probabilities"; "the model was not
retrieving"; "correctness was explained by token priors."

### Finding C — The abstention band excluded ideal abstention (abstention label confounded)

Observed abstention_rate = **1.000 on every rung**: the model emitted `NULL` on 16/16 NULL items per
rung (CS raw-output spot-checks confirm literal `NULL` emissions) while answering the answerable
stratum (strict 0.71–0.99). The locked band [0.50, 0.95] excludes 1.000, so
`abstention_contract_instability` fired **because behavior was perfect**. Secondary latent defect
recorded: the analyzer reads `raw_outputs.get("separability_flag", False)` — an unpopulated flag fires
the label by default (fail-toward-labeling: the safe direction, but a label fireable from absence of
computation is an instrument defect).

*Supported archival reading:* the model produced perfect NULL abstention under the observed NULL
items; the locked criterion excluded 1.000; the label is instrument-confounded and cannot be
interpreted as abstention failure. *Unsupported readings (do not use):* "the model failed NULL
abstention"; "the model answered when it should abstain"; "the abstention contract was behaviorally
unstable."

## 5. Surviving behavior-informative observations (negative-use boundaries apply)

**5.1 — L03 strict/content format gap (real).** L03 (D=16, K=low) fired
`strict_content_gap_instability` with gap = 0.162 (content − strict; B1 sign convention): the model
sometimes emitted a `key: value` pattern where the contract requires value-only output — content
preserved, strict contract violated. This is a genuine, pre-registered, correctly-detected
**format-cliff observation**, continuous with the Paper 1 dual-scoring taxonomy. **The strict scorer
is not to be relaxed after the fact to absorb this behavior**; relaxation would erase the sweep's one
genuine behavioral finding by definition.

**5.2 — Measurement-headroom limitation on L01/L04/L05 (real).** `insufficient_measurement_headroom`
on these rungs is a level-based finding, not a confounded comparison: near-ceiling performance leaves
those rungs without resolution to detect plausible degradation at N_eff ≈ 80 — the D7-class lesson.
This is a measurement-design observation; it is **not convertible into a positive capability claim.**

**5.3 — Residual rung status.** L01/L04/L05: real headroom limitation plus confounded universal
labels. L03: real format gap plus confounded universal labels. L02/L06/L07/L08: unresolved under
corrected instruments. **No rung becomes a survivor; K = 0 stands; the substantive reason for K = 0 is
instrument discrimination, not model or family non-viability.**

## 6. Numeric diagnostics — retention and boundary

Per-rung levels (strict ≈ 0.71–0.99; control ≈ 0.76–0.98; NULL detection 1.00; visible D/K
sensitivity) are retained **as instrument-diagnosis evidence only**: they explain why the labels fired
and why the surface reading was revised. They may not be used to claim the candidate is good or
certifiable, that the family is viable, that thresholds can be set, or that a candidate can be
selected. Any table reproducing per-rung levels must carry, adjacent:

> "These numeric diagnostics are negative-use only. They are included to diagnose instrument behavior
> and may not be copied into a threshold sheet, candidate-selection memo, certification report, or
> future rung-selection rationale."

## 7. Non-claims

This close-out does not claim any of: model retrieval failure; model retrieval certification; model
certifiability; substantive task-family non-viability or viability; that single-hop KV retrieval is
easy or impossible; substantive occupancy or unoccupancy of the certification window; support for or
falsification of Claim C; successful application of Paper 3; that any D1/D2/D4 certification gate
fired. **The sweep exercised Lane 1a classifications, not Paper 3 certification gates.** Substantive
certifiability interpretation is withheld.

## 8. Governance posture

Lane 1a outputs remain negative-use only (`artifact_class: lane-1a-reconnaissance`,
`certification_relevance: none`). No statistic from this sweep may be copied into a threshold-sheet
field, directly or by transformation. No output may be used to rank rungs, select or prefer
candidates, populate or lock thresholds, certify a model, support retention claims or Claim C,
reactivate Fork A, activate Paper 6, or package a public benchmark. All non-Lane-1a execution gates
remain closed. The over-elimination failure mode realized here is the direction the lane was designed
to fail toward: nothing was promoted, no survivor set exists, nothing leaked into selection.

## 9. Review-to-lock accountability (process record, not person-failure record)

Three issues were predicted or partly visible before lock: the unsplit abstention band (warned,
not incorporated); the underdeclared control scoring target (flagged minor; proved load-bearing); and
dummy-battery degeneracy (missed — no review layer required executing the battery against a pilot
manifest before lock). **Durable lesson:** specification-level review of a diagnostic battery is
insufficient; the battery must be executed against a pilot manifest before lock to verify that it can
fire and cannot always fire. This joins the program's structural-rule family: **G1 — delivery must be
tested; sibling cross-reference — agreement must be tested; production-path smoke — environment must
be tested; battery discrimination — discrimination must be tested.**

## 10. Design requirements for any Lane 1a′ (lessons only; nothing authorized)

**R1 — Battery acceptance gate.** Pre-lock, every dummy policy computed offline against a pilot
manifest; acceptance requires per-policy accuracy below a declared cap, union-envelope below a
declared cap, and evidence each policy is wrong somewhere the correct operation is right. Non-constant
≠ non-degenerate. Analyzer hardening: `union_envelope ≥ 0.999` is a hard warning / fail-closed
discriminator condition.
**R2 — Control semantics declared at spec time.** Original-token target, post-scramble target,
null-context target, and token-frequency baseline are not interchangeable; a true token-prior control
must remove binding-recoverable signal while preserving the surface distribution. Post-scramble
scoring is a second retrieval task.
**R3 — Abstention rule split.** Separate NULL-stratum floor, answerable-stratum cap, and
NULL-vs-answerable separability; perfect NULL abstention is not penalized absent explicit
justification.
**R4 — Review-to-lock disposition table.** Every review must-fix carries an explicit disposition
(incorporated / declined with rationale / deferred with rationale and risk owner) before Manager lock
confirmation.
**R5 — Analyzer completeness and evidence-bundle hygiene.** `answer_pos_distribution` populated;
per-rung numeric tables carry the adjacent exclusion block; figure metadata carries artifact class and
certification relevance; no output implies least-bad-rung ranking.

Any Lane 1a′ requires a new design packet, new sweep_id, new lock manifest, replayed review chain, and
explicit Manager authorization. **No such authorization is granted by this close-out.**

## 11. Audit items

**Accepted bookkeeping gap:** `answer_pos_distribution` unpopulated in per-rung records
(analyzer-driver omission). Disposition: bookkeeping gap, not an evidence gap — the manifest
population is bit-reproducible from the locked seed and generator, so the histogram is recoverable
read-only at any time; recorded so future readers understand position-uniformity was not directly
surfaced in the sweep record. **Open item:** `separability_flag` provenance — CS records whether the
flag was computed or defaulted via `raw_outputs.get("separability_flag", False)`. This does not alter
the abstention diagnosis (the band defect alone explains the label) but default-fired components
belong on the record.

## 12. Final disposition

| Item | Status |
|---|---|
| Lane 1a execution | Complete and clean |
| Mechanical verdict | K = 0 under locked rules |
| Substantive certifiability interpretation | Withheld |
| Primary recorded result | Fail-closed instrument-discrimination finding |
| Surviving real observations | L03 strict/content format gap; L01/L04/L05 measurement-headroom limitation |
| Downstream authorization | None |

**Adoption block:** Team Lead ________ · Manager (E. A. Flores) ________ · Date ________
Upon adoption, CS commits this document at the intended path under G1 enumeration (filename, full
sha256 computed at routing, commit SHA returned), and the Lane 1a lane is closed of record.

— Prepared by Senior Engineer, 2026-06-10
