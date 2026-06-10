# Paper 3 v1.0 — Known-Issues Intake and Deferral Record (Erratum-Class Routing)

*Senior Engineer, 2026-06-10. Filed under the Team Lead closure's erratum clause ("no further Paper 3
protocol review unless an erratum-class defect is discovered"). Intended path:
`governance/2026-06-10_paper3-v1.0-release/KNOWN-ISSUES-AND-DEFERRALS.md`. The v1.0 tag and manuscript
are not modified by this record; the remediation vehicle is a future v1.1 revision under separate
authorization. To be committed together with the previously uncommitted external-review records
(REFEREE-REPORT-v0.7.md, SENIOR-DISPOSITION.md) at `governance/2026-06-10_paper3-external-review/`.*

## 0. Safety position

No live exposure exists: candidate selection, threshold population/lock, certification evaluation, and
all runs remain Manager-locked. No threshold sheet can lock against v1.0 before these items are
dispositioned, because no threshold sheet can lock at all without authorizations that have not been
given. This record converts known-but-underdocumented items into ledger entries; it does not create new
risk and it removes the silent-deferral state.

## 1. Erratum-class (fix required in v1.1, before any first threshold-sheet lock)

**E1 — D2 mixture gap.** Pattern-departure against pure shortcut nulls does not bound mixtures of
declared policies; a blend departs from every pure prediction while remaining substantially
shortcut-driven — the unidentifiable interior Paper 2 itself mapped. The v1.0 non-claim ("rules out
only the declared battery") does not unambiguously cover declared-policy blends. *Remediation:*
dual-mode D2 — Paper 1 Table-D performance floor (exceed max-dummy by pre-registered margin; bounds
all blends of declared policies) plus the existing pattern departure — with a battery-size/N margin
calibration note. Protocol change → framework identifier increments at v1.1. Requires no run.
*Status: previously dispositioned ADOPT (Senior disposition of the v0.7 referee report); decision now
formally requested of Team Lead + Manager.*

**E2 — D6 timestamp wording ambiguity.** D6's sentence "Both `threshold_sheet_lock_timestamp` and
`first_candidate_data_access_timestamp` must be UTC ISO-8601 and harness-populated" does not state
storage sides and can be read as sheet-side for both, contradicting A.1/A.2 (lock timestamp sheet-side;
access timestamp evidence-side). The firewall cannot carry ambiguity. *Remediation:* one clause in D6
("recorded on the threshold sheet and in the evidence bundle respectively, per A.1/A.2"). *Status: new
finding; Senior considered the sentence at v0.9 and judged it acceptable — that judgment is withdrawn.*

## 2. Major (v1.1 scope, with E1)

**M1 — Satisfiability undemonstrated** and **M2 — D1×D7 squeeze unquantified.** One remediation: a
half-page of derivation-type arithmetic showing the certification window is nonempty at realistic N
(illustrative, SYNTHETIC-labeled, non-binding), optionally extended to a full worked example.
*Gate: Manager sign-off on the illustrative-numbers labeling convention (brushes the no-threshold-values
lock); previously dispositioned ADOPT, gated — decision now formally requested.*

**M3 — Certifier operating characteristics unstated.** False-certify routes (mixtures pre-E1,
outside-battery shortcuts) and false-reject routes (margin strictness × battery size at small N) are
not discussed; nothing states what would validate the certifier. *Remediation:* gate-provenance
(ancestral-firing) table built strictly from the documented record, plus the plain statement that no
formalized gate has yet been exercised. *Previously dispositioned ADOPT with sourcing discipline.*

## 3. Moderate (v1.1 scope)

**Q1 — evaluation_mode field** (`short_circuit | full_profile`): full gate vectors substantiate the
mapped-boundary fallback. *Previously dispositioned ADOPT.*
**Q2 — Disclaimer repetition**, which worsened at v0.8/v0.9 because the three-aligned-blocks
quote-safety rule (Contributor 5, ledger-locked) required adding the new stress-side sentence to all
three blocks. *Remediation requires Team Lead adjudication of consolidation vs. quote-safety —
previously dispositioned ADAPT; decision now formally requested.*

## 4. Program-level bounds (recorded; not Paper 3 defects)

**P1 — No linkage construction has ever cleared a baseline gate**; "linkage is hard" vs. "gate
miscalibrated for linkage" is non-identifiable until one passes (the constructibility-sweep protocol is
the standing future-work answer). **P2 — Zero compression rungs have ever run**; the first stress sweep
is a first-light event, and D2 explicitly does not certify against stress-side shortcut substitution.
**P3 — Single-team validation only**; external adversarial review is the unfaced test; public release
and any external submission path are the remediation direction.

## 5. Governance finding and closure (the deferral gap)

**G1 — The v0.7 external-review disposition was never committed** (404 at intended path, verified
2026-06-10) and the four decisions it carried were never taken on the record; Paper 3 released with
those majors open and undocumented in-repo. Root cause: the Senior-workspace→repo transfer failure mode
(second occurrence; first was the Addendum 01 hunt). *Closure:* this record, the referee report, and
the original disposition commit together; the decisions in §§1–3 are hereby formally requested of
Manager and Team Lead; and the transfer rule is restated for the record — a SEND-TO-CS marker is not
delivery; delivery is a confirmed commit SHA.

## 6. Requested decisions

1. Manager: accept erratum-class routing and authorize v1.1 scope = {E1, E2, M1+M2, M3, Q1, Q2-as-
   adjudicated}. (Scope authorization only — no candidate, no thresholds, no runs.)
2. Manager: labeling-convention sign-off for SYNTHETIC illustrative numbers (gates M1+M2).
3. Team Lead: accept dual-mode D2 as a protocol revision (E1).
4. Team Lead: adjudicate disclaimer consolidation vs. the three-block quote-safety rule (Q2).

Until decided, the project holds exactly as the closure memo left it; all execution gates remain closed.

## 7. Remediation annex — refined v1.1 scope (per Team Lead feedback synthesis, 2026-06-10)

*This annex supersedes the earlier solution mapping. The Manager's 2026-06-10 authorization stands; the
synthesis sharpens implementation instructions within the same manuscript-only scope. Manuscript-only
includes schema-as-documented edits; it excludes B1 implementation, candidate artifacts, threshold
sheets, certification outputs, run scripts, model outputs, and benchmark packaging.*

- **E1 — D2 mixture/selector hardening (three-mode):**
  **D2a** max-single dummy floor — exceed the maximum performance of any declared dummy policy by a
  pre-registered margin, same item set / scoring / aggregation as the candidate evaluation (bounds
  item-independent convex mixtures of declared policies as complete accounts).
  **D2b** declared-policy union envelope — an item is envelope-correct if *any* declared policy answers
  it correctly; the envelope is always reported; whether it is binding is pre-registered per candidate
  (when binding, excludes item-conditional selectors over the declared battery as complete accounts).
  **D2c** existing pattern-departure test, per-shortcut, pre-registered margins.
  **Non-claim (verbatim per synthesis):** the max-single floor excludes item-independent convex
  mixtures of declared dummy policies as complete accounts; the union envelope, when made binding,
  excludes item-conditional selectors over the declared battery as complete accounts; if reported but
  not binding, conditional-selector explanations are not excluded; in all cases D2 does not rule out
  undeclared shortcuts, shortcut substitution under stress, or partial/contributory shortcut use within
  otherwise operation-dominant behavior. Never: "D2 proves shortcut absence / rules out shortcuts /
  proves operation-only behavior."
  **Schema (documented):** A.1 `D2_dummy_policy_set`, `D2_max_dummy_performance`, `D2_dummy_margin`,
  `D2_union_envelope_score`, `D2_union_envelope_binding_rule`, `D2_pattern_departure_margins`; A.2
  `D2_floor_observed/threshold/delta`, `D2_union_envelope_observed/threshold_if_binding/delta_if_binding`.

- **E2 — D6 timestamp storage (explicit mapping, no "respectively"):**
  `threshold_sheet_lock_timestamp` is stored on the locked threshold sheet and may be echoed in the
  evidence bundle; `first_candidate_data_access_timestamp` is stored in the evidence bundle from the B1
  audit-log source of record and is not part of the locked threshold-sheet content hash. A.1 carries
  the lock timestamp + `first_candidate_data_access_record_expected_path`; A.2 carries the access
  timestamp + `data_access_firewall_status` + `data_access_firewall_reason_code`.

- **M1/M2 — non-normative synthetic satisfiability note:** new **Appendix B — [SYNTHETIC] Illustrative
  Satisfiability Note, Non-Normative**. Labels on the section, every example, every number:
  [SYNTHETIC] · ILLUSTRATIVE · NON-BINDING · NOT A THRESHOLD · NOT CANDIDATE-SPECIFIC · NOT EVIDENCE.
  **Symbolic or off-program values only (e.g. N_illustrative, N=100, N=200) — never program-real values
  such as N=24 or N=96.** Required non-claim: a nonempty synthetic window does not demonstrate
  feasibility for any real candidate, model, scale, or construction, and must not be cited as precedent
  for threshold derivation.

- **M3 — certifier-limits section:** false-certify routes, false-reject routes, what would validate the
  certifier, gate-provenance/ancestral-firing table sourced only from documented records, and the
  statement that no formalized gate has yet been exercised. Required non-claims: the section describes
  known routes, does not claim the gate set has been validated against them, and is not itself a
  validation; no table row is a certification result. **Banned:** empirical false-certify/false-reject
  rates, ROC curves, confidence intervals, retroactive gate-firing claims ("Cell03 would have failed
  D2"). The lineage motivates gates; it does not validate the certifier.

- **Q1 — `reporting_mode` (renamed from evaluation_mode):** `short_circuit | full_profile`; changes
  recording behavior only, never the certification decision logic. full_profile is diagnostic-only: no
  certification verdict, no bypass of D1–D7 decision rules, D6 remains the hard precheck. Firewall
  guard: if D6 fails for provenance incompleteness after authorized data exists, full_profile may emit
  only provenance-safe diagnostics; if D6 fails for a data-access/firewall violation, no further
  candidate-output-derived gate evidence may be computed.

- **Q2 — quote-safe non-claims:** Abstract / §6 / §9 blocks preserved; editorial tightening permitted
  only if every substantive non-claim survives in all three; no block may be replaced by a
  cross-reference; internal clause-to-block checklist to be used at drafting.

- **H3 — framework supersession (new):** only the latest released framework identifier is lock-eligible
  by default; draft identifiers are refused; superseded released identifiers are refused by default
  unless Manager explicitly authorizes an older released identifier in writing for a specified purpose.
  Lands in the v1.1 masthead framework block, the Appendix A framework_version rule, and the B1 v2.1
  backlog note. (Prevents a future sheet locking against v1.0 once v1.1 exists.)

- **B1 v2.1 backlog:** updated 9 → 11–12 items, adding D2 floor/union-envelope enforcement,
  reporting_mode handling, and the latest-released-supersession check (12 if supersession is counted
  separately from the existing framework-version check). Classification unchanged: candidate-stage
  future work, not a v1.1 blocker, not authorized.

## 8. G1 — strengthened transfer rule and open status

Rule (Team-Lead-final wording): **"SEND-TO-CS is intent. Delivery is a confirmed commit SHA at the
intended repo path in the target repository."** For release-affecting review artifacts, delivery
requires confirmed commit SHA, intended repo path, filename, and hash or blob identifier where
applicable; multi-file SEND-TO-CS markers must enumerate all intended files and destinations; partial
delivery remains open until every enumerated file is committed at its intended path.

**G1 status: OPEN** until CS confirms commit SHAs for the enumerated external-review and governance
files. This record's filing is part of the remediation, not its closure.

— Senior Engineer
