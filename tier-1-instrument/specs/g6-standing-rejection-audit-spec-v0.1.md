# G6-STANDING-REJECTION-AUDIT-SPEC-v0.1

**Version:** v0.1. River and Canyon program. Tier 1 instrument — the first missing module (G6). 
**Goal:** turn the rejection-audit design from Paper A v1.0 (§5) and the Eval-Validity Gate Tool Spec v0.1 (G6) into a standing component.
**The component answers:** *When the gate says REFUSE, how do we know the refusal was justified?*
**Status:** MODEL-FREE SPECIFICATION. Authorizes no model execution and no software build. Paper A v1.0 and the Tool Spec v0.1 are the sources of truth; where this spec disagrees with either, they win. Anchored on origin/main HEAD cfa4ee6.
**Owner split:** Senior (drafter — model-free; preserve Paper A and Tool Spec boundaries) → CS (verify mechanized independence, output classes, no execution implication, consistency with Paper A / Tool Spec) → Team Lead (route as the first missing Tier-1 module; keep separate from CAL-Q diagnostics and Paper B) → Manager.

---

## 0. What this module is, and is not

```text
IS:  a STANDING component that audits every REFUSE decision the gate emits —
     turning the by-hand discipline of Paper A's two episodes into a repeatable
     procedure with a defined trigger, evidence, questions, and outputs.
IS:  the component whose absence makes Paper A's non-vacuousness claim "suggested
     by two worked episodes, not established by a standing mechanism." Building
     and exercising it is what would raise that claim to "established."
NOT: a built tool. This is the SPECIFICATION of the audit; no code is delivered.
NOT: an execution authorization. No run, rerun, or stress is approved here.
NOT: a way to manufacture confidence. Its central rule is that when independence
     is unavailable, it returns a LIMITED status — it does not confirm by default.
```

The reason this module is delicate: it is the instrument auditing its own "no." If it confirms refusals by re-running the same read that produced them, it launders a decision into a validation — exactly the circularity Paper A §5.1 (W1) identified. The whole point of a *standing* audit is that its independence is built in and mechanized, not assumed turn by turn.

## 1. Inherited constraints (binding; from Paper A v1.0 + Tool Spec v0.1)

```text
K1. The audit's confirming read must be MECHANIZED-INDEPENDENT of the read that
    produced the refusal (Paper A §5.1, Tool Spec C6/G6/EP6/FC7). Re-running the
    same per-item read is NOT independence.
K2. As specified without mechanized independence, the audit catches AGGREGATE-vs-
    ITEM disagreement (the CAL-E case) but NOT reading-standard miscalibration —
    and must say so in its output (Paper A §5.1 verbatim limit).
K3. The audit emits a STATUS, not a score, and FAILS CLOSED: when it cannot
    independently confirm, it returns a limited/quarantine status, never a silent
    pass (Tool Spec C1/C2).
K4. PER-ITEM BEFORE AGGREGATE: the audit reasons over inspectable items, not over
    a summary statistic (Tool Spec C4).
K5. SCOPE INHERITED: the audit's thresholds and "what counts as confirmation" are
    construction/model/task specific until independently justified (Tool Spec C5).
K6. The construct-validity SEMANTIC READ remains human (Tool Spec §8): the audit
    mechanizes INDEPENDENCE and BOOKKEEPING, not the judgement of meaning itself.
```

## 2. (Scope 1) What events trigger a rejection audit

```text
TRIGGER: every REFUSE decision emitted by the gate (Tool Spec G4 construct-validity
         refusals, and any future gate whose output is REFUSE).
ALSO AUDITABLE (configurable, recommended):
  - any decision flagged FC6 post-hoc-rule (a refusal under a rule chosen after
    seeing outputs is the highest-risk class);
  - any NEEDS-REPAIR or QUARANTINE that a reviewer escalates as a possible
    mis-refusal.
NOT triggered by: PASS decisions (a PASS is audited by the certification gates
         upstream, not by the rejection audit — the rejection audit exists to
         check the gate's "no," not its "yes").
STANDING, NOT SAMPLED: the audit runs on EVERY qualifying refusal as a matter of
         course — that is what makes it "standing" rather than the by-hand,
         author-chosen episodes of Paper A. (Paper A's limitation that the authors
         "also chose which episodes to report" is removed precisely by auditing all
         of them.)
```

## 3. (Scope 2) What evidence the audit receives

The audit receives the refusal's full evidence packet (Tool Spec §5) plus the materials needed for an independent read:

```text
E1. THE REFUSAL RECORD: which gate fired, the pre-declared rule it applied, and
    whether that rule was pre-declared or post-hoc (Tool Spec EP3).
E2. THE PER-ITEM TABLE the refusal was based on: each item's input, raw output,
    strict score, concept score, four-way absence classification (Tool Spec EP2).
E3. THE RAW MODEL OUTPUTS (not the producing read's labels): so an independent
    channel can re-classify from raw outputs rather than inherit the original
    read's verdicts.
E4. PROVENANCE BLOCK: model id+precision, item-set hash, scorer hash, run-record
    hashes (Tool Spec EP4) — so the audit is traceable.
E5. THE INDEPENDENCE CHANNEL (§4): whichever of blind-second-reader / pre-
    registered-schema / external-labels is available for this audit. If NONE is
    available, that absence is itself recorded and forces a limited status (§6).
```

Critically (K1): E3 — raw outputs, not the original read's labels — is what makes an independent re-classification possible. An audit handed only E2 (the original labels) could not be independent; it would inherit the verdict it is meant to check.

## 4. (Scope 3) What counts as mechanized independence

Independence is mechanized when the confirming classification is produced by a channel that does **not** have access to, and is not derived from, the read that produced the refusal. At least one of the following must be specified for a refusal to be eligible for full confirmation:

```text
CH1. BLIND SECOND READER
     A second human reader classifies the raw per-item outputs (E3) WITHOUT seeing
     the gate's decision, the original reader's labels, or the route. Independence
     mechanism: blinding. Catches: reading-standard miscalibration (two readers
     applying the standard disagree) AND aggregate-vs-item disagreement.
CH2. PRE-REGISTERED OUTPUT-CLASSIFICATION SCHEMA, APPLIED WITHOUT ROUTE KNOWLEDGE
     A classification schema fixed BEFORE the outputs were seen, applied to raw
     outputs (E3) by someone/something with no knowledge of the gate's decision.
     Independence mechanism: the rule predates and is blind to the decision.
     Catches: reading-standard drift (the schema, not the original reader, decides).
CH3. EXTERNAL GROUND-TRUTH LABELS
     Labels from a source independent of the gate (e.g. a separately constructed
     answer key, a different annotation effort). Independence mechanism: provenance
     external to the instrument. Catches: both error classes, strongest where
     available.
```

```text
NOT mechanized independence (explicitly insufficient):
  - re-running the SAME per-item read that produced the refusal (K1 — the
    circularity);
  - the same reader re-classifying with knowledge of their own prior verdict;
  - a schema written AFTER seeing the outputs (post-hoc; no better than the
    original read);
  - an automated proxy that pattern-matches the original read's heuristic (it
    re-applies the same standard by other means).
```

The number of channels is configurable, but **zero channels available ⇒ the audit cannot fully confirm** (§6, the limited status).

## 5. (Scope 4) What questions the audit asks

Paper A's four audit questions, carried forward verbatim in meaning, each now assigned to a channel where mechanization matters:

```text
Q1. WAS THE REFUSAL CORRECT?
    Does an INDEPENDENT read (CH1/CH2/CH3 — not the producing read) confirm the
    defect the gate fired on? This is the question K1/K2 are about: answerable with
    full force ONLY via an independent channel.
Q2. COULD THE REFUSAL BE A SCORING ARTIFACT?
    Could the signal the gate refused on be produced by the scorer rather than the
    model? (The strict-vs-concept / four-way check, Tool Spec G2/G3, asked of the
    refusal.) This is what reversed CAL-E.
Q3. DO PER-ITEM READS CONFIRM IT?
    Is the refusal grounded in inspectable items (E2/E3), not a summary statistic?
    The audit requires the items.
Q4. WAS THE RULE PRE-DECLARED?
    Was the refusal under a rule fixed before the outputs were seen (evidence), or
    chosen after (post-hoc tuning, recorded as weakened — Tool Spec FC6)?
```

```text
Mapping questions to what they can catch:
  - Q2 + Q3 are answerable WITHOUT a fresh independent channel (they re-examine the
    existing scoring and items) — they catch the AGGREGATE-vs-ITEM artifact (CAL-E).
  - Q1 with full force REQUIRES an independent channel (§4) — only then can the
    audit catch READING-STANDARD MISCALIBRATION, not just aggregate-vs-item
    disagreement (K2).
This mapping is why "no independent channel" yields a LIMITED status: Q2/Q3 can
still run, but Q1 cannot be answered at full strength.
```

## 6. (Scope 5) What outputs the audit can emit

```text
REFUSAL-CONFIRMED     An independent channel (§4) confirms the defect; Q1-Q4 hold.
                      The refusal was justified. (Design target for CAL-Q: construct
                      collapse confirmed by an independent read of raw outputs.)
REFUSAL-REVERSED      The audit shows the refusal was a scoring/aggregate artifact
                      (Q2/Q3): the baseline was in fact valid. The refusal is
                      withdrawn and the event recorded. (Design target for CAL-E:
                      the apparent failure the per-item read overturned.)
REFUSAL-QUARANTINED   The refusal cannot be adjudicated — missing items, unhashed
                      provenance, or an unresolved scorer question. Held out of any
                      claim until resolved; re-enters the audit when the gap is closed.
AUDIT-INCONCLUSIVE    The audit ran but the evidence does not clearly confirm or
                      reverse (e.g. intermediate per-item results, or an independent
                      channel that partially disagrees). Reported as inconclusive,
                      NOT forced to confirm or reverse.
AUDIT-CIRCULARITY     NO mechanized-independent channel was available (§4), so the
                      refusal cannot be INDEPENDENTLY confirmed. Q2/Q3 may still be
                      reported, but Q1 is explicitly marked unanswerable-at-full-
                      strength. This is the LIMITED status (K3): the audit declines
                      to call the refusal independently confirmed, and says why.
                      (This is FC7 from the Tool Spec, realized as an output class.)
```

Names may be revised; the meanings are binding. The essential pair is **REFUSAL-CONFIRMED requires an independent channel**, and **AUDIT-CIRCULARITY is what is returned when none exists** — never a silent or default confirmation.

## 7. (Scope 6) What happens when the refusal is confirmed

```text
On REFUSAL-CONFIRMED:
  - the REFUSE route decision stands; the baseline is recorded as not-safe-to-
    compare for the stated, independently-confirmed reason;
  - the confirming channel and its result are written to the evidence packet (§9);
  - the confirmation contributes to the instrument's standing record of audited
    refusals — the accumulating evidence that the gate's "no" tracks real defects
    (this is the record that, over many confirmed refusals, would move non-vacuous-
    ness from "suggested" to "established" — K-claim).
  - NOTE: a confirmed refusal is still scoped to its family/model (K5); it is not
    generalized.
```

## 8. (Scope 7 + 8) What happens when the refusal is reversed, and when inconclusive

```text
On REFUSAL-REVERSED:
  - the REFUSE decision is WITHDRAWN; the baseline is returned to the gate for
    re-routing (it may now PASS / NEEDS-REPAIR depending on the corrected reading);
  - the reversal is recorded as an instrument event: the gate's rule produced a
    wrong refusal, and the audit caught it. The producing RULE is flagged for
    review (a reversal is evidence the reading standard or scorer needs correction).
  - reversals are first-class data, not embarrassments: a gate whose audit reverses
    some refusals is demonstrably not calibrated to refuse-by-default (Paper A's
    bidirectional point, now standing rather than by-hand). Recording reversals is
    what keeps the confirmed refusals credible.

On AUDIT-INCONCLUSIVE:
  - the REFUSE decision is HELD (it does not flip to pass on inconclusive evidence —
    fail-closed, K3), but it is marked as not-independently-confirmed and routed for
    a human semantic read (§10) and/or acquisition of an independent channel;
  - inconclusive is recorded as inconclusive — not quietly rounded to confirmed.
```

## 9. (Scope 9) What gets recorded in the evidence packet

Extending Tool Spec EP1–EP6, every audit writes an audit record:

```text
AR1. AUDIT OUTPUT CLASS (§6) and the refusal it audited (link to the refusal's
     own packet).
AR2. WHICH CHANNEL was used (CH1/CH2/CH3) or, if none, an explicit "no independent
     channel available" note that justifies an AUDIT-CIRCULARITY output.
AR3. THE FOUR QUESTIONS Q1-Q4 with their per-question results, including which were
     answerable at full strength and which were limited by channel availability (§5).
AR4. FOR REVERSALS: the producing rule flagged for review, and the corrected reading.
AR5. PROVENANCE: hashes of the raw outputs, the independent channel's labels (if
     any), and the audit's own decision rule (pre-declared).
AR6. SCOPE STAMP: the family/model the audit is scoped to; "evidence about the
     instrument, not the model" (Tool Spec EP5).
AR7. INTERIM-STATUS DISCLOSURE (until independent channels are routinely available):
     an explicit statement, per Tool Spec EP6, of whether the refusal rests on a
     read WITH or WITHOUT mechanized-independent confirmation.
```

## 10. (Scope 10) What remains human-semantic-read dependent

```text
HUMAN (not mechanized by this spec):
  - THE CONSTRUCT-VALIDITY JUDGEMENT ITSELF (Tool Spec §8, K6): deciding that an
    output is a genuine value-emission rather than a legitimate response in
    disguise. The audit mechanizes the INDEPENDENCE of a second such judgement
    (blinding, pre-registration, external provenance) — it does not remove the
    judgement of meaning. A blind second reader (CH1) is still a HUMAN read; a
    pre-registered schema (CH2) was authored by a human; external labels (CH3) were
    annotated by humans.
  - DESIGNING THE INDEPENDENCE CHANNEL: writing the blind-reading protocol or the
    pre-registered schema is a human design act (and is the first real task of the
    eventual G6 BUILD, not something this spec solves).
  - ADJUDICATING AUDIT-INCONCLUSIVE cases: when an independent channel partially
    disagrees, resolving it is a human semantic read.

MECHANIZED (bookkeeping, routing, comparison — automatable):
  - triggering the audit on every refusal (§2);
  - assembling the evidence (§3) and the audit record (§9);
  - comparing the independent channel's labels to the original read and computing
    agreement/disagreement;
  - emitting the output class per the decision rule (§6) and enforcing fail-closed
    on missing channels.
```

The load-bearing honesty constraint, identical to Paper A and the Tool Spec: **mechanizing the audit means mechanizing the INDEPENDENCE and the bookkeeping — never the semantic judgement of meaning.** An audit that automated the construct-validity judgement would re-introduce the very shortcut the gate exists to refuse.

## 11. Design validation targets (how a future build would be checked — NOT run here)

When G6 is eventually built (separate authorization), it should reproduce Paper A's two by-hand verdicts as a standing procedure:

```text
- CAL-Q (construct collapse, abstention 0.00, confirmed by the form-level positive
  control): a correctly-built G6 with an independent channel should return
  REFUSAL-CONFIRMED.
- CAL-E (apparent failure that was a scorer artifact, 0.575 -> 0.90 on the per-item
  read): a correctly-built G6 should return REFUSAL-REVERSED.
- A refusal with NO independent channel available: G6 must return AUDIT-CIRCULARITY
  (limited status), NOT REFUSAL-CONFIRMED.
These are validation targets for a FUTURE build; this spec runs nothing and asserts
no result. Reproducing them would be the first evidence that moves non-vacuousness
from "suggested by two episodes" to "demonstrated by a standing mechanism."
```

## 12. Boundary (closed gates — unchanged)

```text
No model execution.       No second compression rung.
No new run.               No full ladder.
No D4 rescue.             No Claim C activation.
No CAL-Q rerun.           No public benchmark packaging.
No certification run.     No funder-facing release.
No compression.           No SBIR submission.
No INT8 / INT4 stress.    No software build.
```

This is specification only. Paper A and the Tool Spec are the sources of truth. A G6 BUILD — including the independence-channel design — is a separate, future, separately-authorized step.

## 13. For CS verification (what to check)

```text
- MECHANIZED INDEPENDENCE: that §4 specifies at least one real independent channel,
  that re-running the same read is explicitly excluded (K1), and that "no channel
  available" forces AUDIT-CIRCULARITY (not a default confirmation).
- OUTPUT CLASSES: that the five outputs (§6) are clearly defined and that
  REFUSAL-CONFIRMED is gated on an independent channel while AUDIT-CIRCULARITY is
  the no-channel status.
- NO EXECUTION IMPLICATION: that §11's validation targets are marked future-build,
  not run here; that the closed gates (§12) are intact; no software build implied.
- CONSISTENCY WITH PAPER A / TOOL SPEC: that the four questions (§5) match Paper A
  §5.1; that the human/mechanized line (§10) matches Tool Spec §8 (construct-
  validity judgement stays human); that K2's catches/misses limit is preserved.
- SCOPE: that confirmed refusals are not generalized beyond their family/model (K5).
```

— Senior Engineer
