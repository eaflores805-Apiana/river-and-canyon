# Senior Disposition — External Referee Report on Paper 3 v0.7

*Senior Engineer. Responds to the external-perspective referee report received 2026-06-10 ("take with a
grain of salt" — Manager). Item-by-item disposition for Team Lead routing. Nothing here is implemented;
this memo proposes a v0.8 scope for Team Lead/Manager decision. No execution, candidate selection, or
threshold authorization is implied.*

## Overall verdict on the review

Substantively strong. The two structural attacks it names (satisfiability undemonstrated; D1×D7
squeeze unexamined) are real, fixable without any run, and the worked-example fix is the highest-value
single addition available to this paper. One technical finding (D2 mixture gap) is a genuine protocol
defect. Three items conflict with standing governance and need adjudication rather than adoption.

## Item-by-item

**Major 1 — satisfiability / worked synthetic example. ADOPT, gated.** A fabricated candidate with
clearly-labeled, non-binding illustrative values traced through all seven gates (one full pass, one D7
fail at small N), with filled-in threshold-sheet and gate_summary exhibits. No run, no candidate, no
authorization touched. **Governance gate:** illustrative numbers sit near the "no threshold values"
lock; requires explicit Manager sign-off on the labeling convention before any number is written.
Proposed convention: every illustrative value carries a SYNTHETIC marker; the section opens and closes
with a non-binding declaration; no value may coincide with any later pre-registered value without a new
derivation.

**Major 2 — D1×D7 squeeze subsection. ADOPT.** Name the tension; show the window arithmetic at two N
values (derivation-type-dependent, illustrative, non-binding). Senior will derive the numbers from the
declared derivation types, not transcribe the reviewer's (whose ≈5-flips/≈20-pt figures are plausible
but unchecked). Doubles as the Major-1 satisfiability argument.

**Major 3 — D2 dual-mode (performance floor + pattern departure). ADOPT — protocol change.** The
mixture gap is real: pattern-departure alone certifies the unidentifiable interior Paper 2 mapped; the
max-dummy performance floor bounds mixtures of declared policies. Also adopt the battery-size/N margin
calibration sentence. **This changes a gate's decision rule:** framework version increments; Team Lead
review required; the "rules out only the declared battery" non-claim becomes "the declared battery and
mixtures thereof."

**Major 4 — `evaluation_mode: short_circuit | full_profile`. ADOPT.** One pre-registered field;
certification stays conjunction-based; full-profile mode records the complete gate vector so the
"mapped certification boundary" fallback is substantiated. D6 remains first in either mode.

**Major 5 — gate-provenance (ancestral-firing) table + certifier error-rate discussion. ADOPT, with
sourcing discipline.** Every row must be rebuilt from the documented program record (claim ledger,
experiment logs, Paper 1/2 artifacts); the reviewer's specific attributions are NOT adopted on memory.
Include the plain statement that no formalized gate (margins, null models, locked battery code) has yet
been exercised. Add the false-certify / false-reject routes and what would validate the certifier
(future gate-level binding demonstrations).

**Major 6 — consolidate authorization disclaimers. ADAPT, needs Team Lead adjudication.** The
repetition is real (five materially identical statements; firewall taxonomy duplicated). But the three
aligned non-claim blocks are a ledger-locked Contributor-5 requirement (quote-safety: any one block
yields the full boundary). Proposed middle path: full canonical block in the new §2 (scope) and the
status line; one-line pointers elsewhere; firewall taxonomy lives once in Appendix A, referenced from
the application section. Team Lead must explicitly release or amend the alignment requirement before
this lands.

**Restructure (§1–§9 + appendices). ADAPT.** The proposed order is better for an external reader:
thesis-scope first, gates self-contained (merging current §4+§6 into uniform four-field blocks),
worked example as its own section, certifier-limits section, operational matter consolidated.
Senior supports it as the v0.8 skeleton, subject to: (a) the Major-6 adjudication above; (b) preserving
every ledger-locked wording (canonical snapshot/mlx_lm phrases are unaffected; non-claim union content
unchanged, placement consolidated); (c) the gate set, scope asymmetry, negative-certification posture,
and Claim C containment are untouched — this is reorganization plus two new sections, not reopening.

**Minors.** Online/offline gate annotation in the ordering table: ADOPT. "Substrate" one-sentence
definition: ADOPT. §7 expiration ambiguity (schema-compatible bugfix vs schema-version bump): ADOPT —
propose "certification expires on any change to the recorded `B1_harness_schema_version`; a harness
change that does not alter the schema version does not expire certification but must be recorded."
MSA / gauge-R&R positioning: ADOPT IN PRINCIPLE — the genealogy is honest and strengthens novelty
(D7 as precision-to-tolerance), but citations must be real, verified sources added by Senior with the
same discipline as [3]/[4]; no entry is written until verified. Reference-list thinness for external
release: acknowledged; handled at the positioning pass.

## Governance flags (decisions required before v0.8 begins)

1. Manager: authorize the worked synthetic example under the SYNTHETIC labeling convention (Major 1).
2. Team Lead: accept dual-mode D2 as a protocol revision (framework version increment) (Major 3).
3. Team Lead: adjudicate non-claim consolidation vs the Contributor-5 alignment requirement (Major 6).
4. Team Lead: accept the restructure skeleton as the v0.8 scope, or narrow it.

## What this disposition does not do

It implements nothing; selects no candidate; sets no threshold value (illustrative-value authorization
is explicitly deferred to Manager); authorizes no run; reopens no released artifact; and changes no
ledger-locked wording. v0.7 remains the manuscript of record until the Team Lead scopes v0.8.

— Senior Engineer, 2026-06-10
