# METHODOLOGY RECORD — How the Tests Got Their Shape

**Version:** v0.3. River and Canyon program. Internal methodology record. **Supersedes v0.2** (0f27f3e4), retained. v0.3 integrates Contributor 5 review with deliberate restraint: two corrections that close consistency gaps the record had against its own standards — (a) §9's standing rule promoted to an operationalized control with a trigger (§9a), since it was the only lesson left as prose while being the most load-bearing; (b) the 0.6625 band boundary given its derivation in §10, which the record had exempted from the provenance standard it holds everything else to. One forward control (the rejection audit) is LOGGED as a stub (§11) to be drafted in full when CAL-Q resolves — not elaborated now, per C5's own point that v0.3 should be triggered by a result, not by another round of reflection.
**What this is:** an honest account of *why the measurement instrument looks the way it does*, organized by the failures that forced each feature into existence. It is a record, not advocacy. Each entry is: here is a way an evaluation fooled us, here is the control that failure produced, here is what the control costs and when it is overkill. The features of the test are not design elegance; they are scar tissue from specific ways earlier versions got fooled.
**What this is NOT:** a claim of novelty. Whether this discipline is uncommon in the field is a separate question that requires a literature check, not an assertion from inside the program. This document establishes the internal record; the novelty question is downstream of it.
**Anchoring:** every episode below cites the artifacts and commits that are its evidence, so the record can be checked against bytes rather than memory. Read against origin/main HEAD e2ad863.
Owner: Manager · Senior drafts · maintained as failures accrue.

---

## 0. The one rule that generated all the others

Before the failures, the rule that made the program able to learn from them:

```text
"No mountain in the sentence."
If you cannot state a claim without the founding analogy (weights as carved
rock, activations as water), in the real system's own terms, you do not yet have
a claim. The analogy generates hunches; mechanism judges; experiments execute;
papers report only what the evidence earns.
```

Every control below is what happened when a hunch was stripped of the metaphor,
tested, and *failed* — and the failure was treated as information rather than
looked away from. The discipline is not "we designed good tests." It is "we kept
finding reasons not to trust a measurement, and built a control instead of
reporting the number anyway."

---

## 1. ORIGIN — the compositional seam, and the moment we turned around

**The question the program was built to answer.**

```text
Hunch (metaphor-stripped): compressing a model to INT4 might preserve simple
RETRIEVAL while breaking the LINKAGE between reasoning steps — a "compositional
seam." Component operations survive; the composite operation fails.
```

**The test built to catch it: Two-Hop Level-1.** (Evidence: `tier0-run/` —
`items_twohop_l1_cell01.json`, `RESULTS-TWOHOP-L1-cell0{1,2,3}-ALL.md`,
`CELL03-DECOMPOSITION-REVIEW.md`.)

```text
Each item is a set of chains A → B → C. The model is given A and must follow the
link TWICE (A→B, then B→C) to reach answer C. Decoy chains are mixed in with
look-alike objects, so the model cannot shortcut by grabbing a salient or nearby
object. Every object is role-tagged (anchor_A, hop1_B, answer_C,
distractor_chain_intermediate, distractor) so a wrong answer's SOURCE is legible.
Rationale: one hop is retrieval (easy). Two hops is composition — you must hold
the first lookup's result and use it as the key for the second. If a model does
each hop alone but fails the chain, the seam is real.
```

**The failure that set the program's entire direction.** The purpose-built
two-hop constructions kept failing their own baseline gates — the FP16 (clean,
uncompressed) model did not cleanly do the task the way the construction assumed.

**The control it produced — the program's foundational move:** *do not measure
the seam until you can prove you can measure a single hop cleanly.* Instead of
running the seam test, getting a number, and reporting it, the program turned
around and spent the bulk of its effort proving the **instrument itself** was
valid first. This is the origin of everything that follows. (The cell03
decomposition — `CELL03-DECOMPOSITION-REVIEW.md` — is the binding evidence that
the validity gate catches something real rather than blocking trivially.)

```text
COST OF THIS CONTROL: enormous. The program is, in its official sequence, still
PRE-STRESS — it has not yet run a certified compression rung. Months went into
validating the ruler instead of taking the headline measurement.
WHEN IT WOULD BE OVERKILL: if the goal were a quick directional signal rather
than a trustworthy one. For a throwaway exploration, this control is too
expensive. It earns its cost only when the number has to be defensible.
```

---

## 2. Survival is not correctness

**The failure.** A model could score well on a retention test *while being
secretly broken* — the test preserved the model's ERROR and counted it as
preserved capability. A high "retention" number can mean "the model is reliably
wrong in the same way," not "the model still works." (Evidence: Paper 1,
`survivalisnotcorrectness.pdf`; merged at commit 89c66de.)

**The control.** Staged, fail-closed scoring: a retention score is not trusted
until a verified clean baseline establishes what "correct" even was. Survival of
a behavior under stress is necessary but not sufficient; the behavior must also
have been *correct* at baseline, or its survival is the survival of an error.

```text
COST: you cannot report a retention number from the stressed run alone; you must
first certify the clean baseline, which is extra work and can fail.
OVERKILL WHEN: never, if the retention claim is load-bearing. This is the
cheapest of the controls relative to the error it prevents (reporting preserved
error as preserved skill).
```

---

## 3. Correctness is not constructibility (salient-endpoint attraction)

**Plain setup.** "Can the model do the lookup?" and "did the model get the right
answer?" are not the same question — a model can produce the right answer for the
wrong reason. This section is about the second masquerading as the first.

**The failure.** A model could score well on a baseline *by cheating with a
shortcut* — grabbing the last item, the most salient item, a recent or nearby
value — instead of actually performing the intended operation. A high clean
score did not prove the model did the task; it might have exploited a positional
cue. (Evidence: Paper 2, `correctnessisnotconstructibility.pdf`; Claim B.)

**The failure's signature, which kept recurring.** "Salient-endpoint /
chain-terminal attraction" reappeared *one level deeper* every time it was
patched. Fix the obvious endpoint cue, and a subtler positional shortcut took its
place. This is why it became the actual Claim-B finding rather than a nuisance —
it is a structural confound, not a one-off bug.

**The control.** The shortcut floor: a construct's score must beat what any
enumerated cheap policy (last-position, salient-endpoint, recency,
prefix-neighbor, copy-completion) could achieve, by a margin, or it does not
count. Plus deep interior answer positions and matched decoys, specifically to
deny the shortcuts. (These features in CAL-A–CAL-Q are direct descendants:
deep slots and near-miss distractors exist *because of this failure*.)

```text
COST: constructs must be built off-ceiling and shortcut-resistant, which is
hard and which most purpose-built constructs FAIL (see §5).
OVERKILL WHEN: if you have independent proof the model isn't using positional
cues. Absent that proof, the floor is mandatory — the cue keeps coming back.
```

---

## 4. Hash integrity is not construct validity

**The failure.** Matching bytes (a file's hash verifying) proves the *artifact
was transmitted intact* — it does NOT prove the artifact instantiates the concept
it claims to. A perfectly transmitted test can be a perfectly transmitted *wrong*
test. (Evidence: the Hash-Integrity standing note.)

**The control.** The semantic-read: a nine-field shown-read (artifact / path /
commit / sha256 / claimed concept / check performed / observed structure /
required structure / surplus check), with a mechanical-rendering floor (the
actual bytes are read, not summarized from memory) and an owner signature.
Disposed PASS / HOLD / UNCERTAIN, with UNCERTAIN routing to HOLD for anything
decision-bearing.

```text
COST: every load-bearing artifact needs a human to actually read its bytes and
sign. Slow, and it cannot be automated (a script may prepare the read but may
not perform the judgment).
OVERKILL WHEN: for clerical artifacts with no decision weight. The control is
scoped to load-bearing artifacts precisely so it is not applied everywhere.
```

---

## 5. The baseline gate failures split into two mechanisms (saturation vs elimination)

**Plain setup.** When a test keeps "failing," the instinct is to assume one
problem and one fix. Here, two different failures wore the same surface
appearance, and the fix for one was the opposite of the fix for the other.

**The failure (a subtle one — reading the gate failures wrong).** "Every
purpose-built construction fails its baseline gate" sounds like one problem. It
was two, and conflating them was itself an error. (Evidence:
`BASELINE-GATE-DIAGNOSIS-v0.1.md`, read from the D4 pilot reports and the
Lane-1a sweep `fixed_outcome.md`.)

```text
SATURATION (the D4 family): the candidate scored 80/80 = 1.0 and PASSED the
  elimination criteria — but at accuracy 1.0 there is no room below the ceiling
  for a stress drop to be measurable. Failure = the construct is too EASY, not
  invalid. FIXABLE by calibration.
ELIMINATION (the Lane-1a sweep): every rung carried a shortcut-elimination label
  — the gate correctly catching shortcut-prone constructs. VALID REJECTION; the
  gate doing its job.
```

**The control.** Diagnose *why* a gate fails before acting on it — classify each
failure as valid-rejection / fixable / structural-limit / unresolved, from the
per-item bytes, not from the aggregate. The fix for saturation (make it harder)
is the opposite of the fix for elimination (the construct was correctly rejected;
don't "fix" it). Acting without the diagnosis applies the wrong fix.

```text
COST: a whole diagnostic stage before you may repair a construct.
OVERKILL WHEN: if all your failures are visibly the same mechanism. Here they
weren't, and the cost was justified by the constructed-positive's success — which
came precisely from building OFF-ceiling once saturation was identified as the
problem (Evidence: `constructed-positive-validation/`, clean 1.0 / defective 0.125).
```

---

## 6. A validation pass is not calibration evidence

*This is one of the program's most recurring subtle errors, and it directly
explains why even a "successful" validation (the constructed-positive PASSED) did
NOT automatically produce a usable measurement band. It deserves the same weight
as §2 and §3, with which it shares a family resemblance: a result meaning
something other than what its label suggests.*

**The failure.** The constructed-positive PASSED validation (it discriminated:
clean 1.0 vs defective 0.125) — and that PASS *looked like* progress toward a
measurable band. It was not. "Discriminates at one off-ceiling setting" and
"sits in the measurable band with headroom" are different properties. The clean
member was still at 1.0 (the ceiling); validation success said nothing about
whether the difficulty levers could place it BELOW the ceiling.

**The control.** Keep the question precise: a validation PASS answers "does the
instrument fire?" It does not answer the calibration question "is there room to
measure a drop?" Reading the actual clean accuracy (still 1.0) — not the PASS
label — is what caught this. (Evidence: the calibration-read verdict returned
INSUFFICIENT SPECIFICATION precisely because no off-ceiling clean data point
existed yet, despite the validation PASS.)

```text
COST: a "passing" result does not let you advance; you must check it answers the
question you're actually asking.
OVERKILL WHEN: never, if the two questions are genuinely distinct — which here
they were. This is the same family of error as §2 (a number meaning something
other than what it appears to mean).
```

---

## 7. The parser bug — a scary aggregate that was a scoring artifact

**The failure (the clearest case, and the most recent).** A construct (CAL-E)
appeared to show the model "being fooled by content" — emitting answers when it
should abstain — at a rate of 0.575, which looked like a serious discrimination
failure and triggered a possible pivot away from the whole task family.

**What the bytes actually showed.** The model was correctly abstaining by writing
"none" (lowercase). The scorer's NULL parser only accepted "NONE" (uppercase) and
scored lowercase "none" as a wrong answer. (Evidence:
`CAL-E-DEFECTIVE-ERROR-ANALYSIS-v0.1.md`, then the independent re-score
`cal-abce_rescore_summary.json`.)

```text
Of 40 key-absent items: 23 emitted "NONE" (scored correct), 13 emitted "none"
(scored WRONG — the bug), 4 emitted an actual stray value (the real, small
leakage). The model abstained 36/40 = 90% of the time. The "0.575 inflation" was
mostly a case-sensitivity parser artifact, NOT the model being fooled. Corrected,
defective discrimination was ~0.90 and STABLE across every candidate.
```

**The control.** Read per-item outputs, never trust the aggregate. The bug was
invisible in the summary number (0.575) and obvious in the raw responses (rows of
"none"). Two people read the bytes independently and reached the identical
correction. The standing rule this hardened: **read the items, not the
aggregate** — and report defective behavior in four explicit forms (strict,
concept-level, true-emission, format-artifact) so the same artifact can never
again hide in a single number.

```text
COST: someone must read individual model outputs, every time, even when the
aggregate looks clean — especially when it looks clean.
OVERKILL WHEN: never demonstrated to be. This is the second time in the program
a clean-looking aggregate hid a measurement artifact (§6 was the first). The
cost of reading items has been repaid both times.
```

---

## 8. Procedurally-nonconforming evidence must be quarantined, not laundered

**The failure (a governance failure, not a measurement one).** A compression run
(INT8-RUNG-1) was executed during a routing pause — under ambiguous
authorization. The data looked scientifically usable. The temptation was to
promote it into the official sequence because the number was good.

**The control.** Quarantine: the run was labeled "scientifically retainable,
procedurally nonconforming, pending governance reconciliation" and explicitly
barred from becoming load-bearing for any official claim. A future official
result requires a conforming, authorized run. (Evidence: the INT8 quarantine
suite — quarantine note, route-reconciliation memo, consolidation note.) The
structural fix was the route-state gate (GREEN/YELLOW/RED) so a run cannot again
happen under ambiguity without that being a declared, visible state.

```text
COST: usable-looking data is set aside and cannot be cited. Painful.
OVERKILL WHEN: if provenance genuinely doesn't matter for the claim. For any
claim that has to be trusted, laundering nonconforming evidence destroys the one
asset the program has — that its refusals can be trusted.
```

---

## 9. The pattern across all of them — stated as a standing rule

Every control in this record exists for the same reason, and the reason is worth
stating not as a reflection but as an operating rule the program holds going
forward:

```text
STANDING RULE:
Every control in this record exists because an aggregate number or a passing
label was allowed to stand in for a mechanistic reading until it was forced open.
The discipline is NOT "we design good tests." It is "we treat appealing
aggregates as PROVISIONAL until the per-item bytes and provenance have been read
AND the alternative explanation has been ruled out."
```

The features of the tests — deep slots, matched decoys, shortcut floors,
abstention checks, semantic-reads, per-item reading, quarantine, the off-ceiling
band — are not a design. They are the accumulated residue of being wrong and
catching it. None was foreseen; each was forced. The standing rule is what makes
the next one catchable too.

**Why this is worth recording.** Not because it is novel (unverified), and not
as advocacy. Because right now this discipline is transmitted largely by *shared
experience* — the team grasps it quickly because they lived the failures. Shared
experience does not survive turnover. This record is the backup: the controls,
with the failures that justify them, so the method can be re-derived from the
evidence rather than re-learned by re-failing.

**The honest open question this record does not settle.** Whether this
failure-to-control discipline is genuinely uncommon in the field — and therefore
worth a field-facing methods paper — requires a literature check against
published work on shortcut learning, construct validity in evaluation,
pre-registration, and evaluation reproducibility. That check is the next document
if this one warrants a successor. This record stands on its institutional-memory
value alone, which does not depend on the novelty question's answer.

---

## 9a. The sequencing control (the standing rule, operationalized)

The §9 rule is the most load-bearing lesson in this record — it is the one that
bit the program twice (§6 validation-vs-calibration, §7 the parser bug). Every
other lesson here became an operational control with a trigger, a cost, and an
overkill condition; this one was, until now, the only one left as a reflection.
The program's own bar (a rule must be *operational, not aspirational*) requires
it to have a trigger. Here it is.

```text
SEQUENCING CONTROL (trigger):
No aggregate number may initiate a route change, a pivot discussion, or a design
decision until a per-item read of the N most decision-relevant items has been
logged. Aggregates may INFORM; they may not MOVE. A memo proposing any route/
pivot/design change must attest that the per-item read happened and cite what it
found, or the proposal is not GREEN-eligible.
```

```text
COST: every decision-bearing aggregate incurs a per-item read before it can drive
anything — latency on exactly the moments that feel most urgent (a scary number
invites immediate reaction; this control forbids the reaction until the bytes are
read).
OVERKILL WHEN: for aggregates that inform but do not drive (a number cited for
context, not used to change course). The control is scoped to aggregates that
would MOVE a decision, not all aggregates.
ENFORCEMENT LIMIT (stated honestly): this is a control on PROCESS BEHAVIOR, not a
code gate. Nothing mechanically prevents a decision from being made on an unread
aggregate; the control works only if route/pivot/design memos actually attest the
per-item read, and if reviewers hold that attestation as a GREEN precondition. It
is as strong as the team's adherence, no stronger. It is recorded here so the
adherence has a written standard to point to.
WOULD HAVE CAUGHT: the D4 near-pivot (§7) AT SOURCE. The 0.575 aggregate was
about to drive a pivot discussion; under this control, the per-item read (which
showed the model abstaining ~90%, the number a scorer artifact) would have been
mandatory BEFORE the pivot was entertained — catching it at the start instead of
one step from the cliff.
```

## 10. Current Implications — where the instrument stands today (per C4)

This record explains how the controls came to exist. This section says where they
stand *now*, so it serves as a reference for someone joining or for deciding what
to prioritize. (State as of HEAD c1bf3c7.)

### Which controls are mature and load-bearing

```text
- Survival≠correctness, correctness≠constructibility, hash≠construct-validity
  (§2,§3,§4): MATURE. Released as Papers 1–3 + the Hash-Integrity note. These are
  banked and true independent of how the compression question resolves.
- The semantic-read (§4) and quarantine + route-state discipline (§8): MATURE and
  in active daily use — every load-bearing artifact is read and signed; every
  route memo declares GREEN/YELLOW/RED. The CAL-Q v0.2→v0.3 cycle is a live
  instance: a closed-world violation was caught at design verification and fixed
  before any model time was spent.
- Per-item reading over aggregates (§7,§9): MATURE as a rule, and it has paid out
  twice (the validation-vs-calibration confusion §6, and the parser bug §7).
```

### Which controls are still being stress-tested

```text
- The off-ceiling band + saturation/elimination diagnosis (§5,§6): ACTIVE. The
  D4 calibration work is the current proving ground. The instrument's
  DISCRIMINATION is confirmed robust (defective abstention ~0.90, stable, zero
  out-of-context invention across CAL-A/B/C/E after the §7 scorer correction).
  What is NOT yet shown is that a construct can be placed in the measurable band
  (clean strictly in 0.6625–0.95) — every candidate's clean accuracy is still
  ≥0.95, at or above the ceiling.
  [BAND DERIVATION, per the provenance standard this record holds everything else
  to: the lower bound 0.6625 = shortcut floor 0.6125 + 0.05 margin. The shortcut
  floor 0.6125 is the union_envelope score from the D4 t1 shortcut battery (the
  best score any enumerated cheap policy achieved). The upper bound 0.95 =
  ceiling 1.0 − 0.05 (a noise-floor margin at n=40). Both margins are 0.05, chosen
  on n=40 noise-floor grounds, not asserted. The record should not exempt its own
  threshold from the derivation it requires of every other load-bearing number.]
```

### The active constraint on forward progress

```text
THE BLOCKER IS CLEAN SATURATION, NOT DISCRIMINATION.
The model does the lookup too well — clean accuracy will not come off the ceiling
on the levers tried so far. Content levers (length/depth/near-miss) move it weakly
and non-monotonically. The live test is CAL-Q v0.3 (CS-verified PASS, awaiting a
narrow calibration-only run authorization): an in-prompt code-book query lever
that adds clean-side difficulty without touching list content. Whether it pulls
clean into the band with discrimination intact is the open question on which D4
viability turns.
```

### The velocity cost this record implies (honest)

```text
The governance layer that makes these controls trustworthy is SLOW. The program
is, in its official sequence, still PRE-STRESS: no certified compression rung has
run, after substantial effort. Each control adds a gate; each gate adds latency.
This is the deliberate trade the North Star and kill-criteria encode — fewer,
slower, more defensible results over more, faster, less trustworthy ones. The
record implies a standing question the team must keep asking: is the next control
buying enough validity to justify its velocity cost, or is it governance for its
own sake? (The proof-of-life / kill criteria exist precisely to force that
question — a gate system that only produces more gates is a failure mode this
program names explicitly.)
```

### What the record implies for the next design move

```text
- D4 is NOT to be abandoned on discrimination grounds — that fear (PIVOT WATCH)
  was a scorer artifact, now corrected. Abandoning now would repeat the §7 error.
- The next move is the CAL-Q v0.3 calibration run (if authorized): a dispositive
  test of whether a query-side lever solves clean saturation.
- If it does: D4 yields its first well-formed certification-run request — the
  program's first step from PRE-STRESS toward an actual stress measurement.
- If it does not: the pivot to Tier 1 eval-validity auditing is honest and
  supported (both content AND query-side levers will have been tried), and the
  methodology layer (Papers 1–3 + this record) is itself the defensible product.
- Either way, the band question must be settled by READING THE CLEAN BYTES of the
  run, not the pass/fail label — the §6 lesson, applied to the very next result.
```

## 11. LOGGED STUB — the rejection audit (to be drafted in full when CAL-Q resolves)

*This is a deliberately unfinished entry. It records the single most valuable
forward observation from the C5 review so it is not lost, while honoring C5's own
point that this record's next full revision should be triggered by a RESULT (the
CAL-Q v0.3 calibration run resolving), not by another round of reflection. Do not
elaborate this into a polished §-entry now; draft it in full when the run lands.*

```text
THE BLIND SPOT (structural, not yet controlled):
Eight of the nine failure→control episodes in this record (§2–§6, §8, and the
discrimination half of §5) are controls against trusting a number that looks
GOOD — false comfort. Only §7 points the other way: the parser bug made
discrimination look WORSE than it was (0.575 vs the real ~0.90), and the
program's response to that false ALARM was to nearly abandon a whole task family.

As the control stack grows, the dominant residual risk QUIETLY FLIPS:
  early: the main danger is "we trusted a bad number"          (heavily defended)
  later: the main danger is "we killed a good construct on a bad signal"  (undefended)
The record has nine reasons to reject and almost nothing to second-guess a
rejection. §7 is the first near-miss of exactly this type.

THE SYMMETRIC CONTROL (to be specified in full later): a REJECTION AUDIT —
every HOLD, every killed construct, every "this family can't host it" gets the
same "was the rejection itself an artifact?" scrutiny applied to passes;
periodically re-opened, not left buried. The control stack is currently
asymmetric (distrust-good-numbers only); this is the missing other half.

WHY DEFERRED, NOT DROPPED: the full control needs a trigger / cost / overkill in
the shape of the rest of the record, AND it should be informed by how CAL-Q
resolves (a CAL-Q PIVOT would itself be a rejection that this control would later
audit — so the run is live evidence for how to specify the audit). Drafting it
now, before that, would be the exact "let the appealing thing (writing) move you
before the bytes are read" error the record warns against.
```

## Appendix — episode-to-evidence index

```text
§1 two-hop seam origin    tier0-run/items_twohop_l1_cell01.json,
                          RESULTS-TWOHOP-L1-cell0{1,2,3}-ALL.md,
                          CELL03-DECOMPOSITION-REVIEW.md
§2 survival≠correctness   survivalisnotcorrectness.pdf (Paper 1; commit 89c66de)
§3 correctness≠construct  correctnessisnotconstructibility.pdf (Paper 2; Claim B)
§4 hash≠construct validity Hash-Integrity standing note; semantic-read template
§5 saturation vs elimination BASELINE-GATE-DIAGNOSIS-v0.1.md;
                          constructed-positive-validation/run_result.json
§6 validation≠calibration calibration-read verdict (INSUFFICIENT SPECIFICATION)
§7 parser-bug artifact    CAL-E-DEFECTIVE-ERROR-ANALYSIS-v0.1.md;
                          cal-abce_rescore_summary.json
§8 quarantine discipline  INT8 quarantine suite; ROUTE-STATE-GATE-v0.1.md
```

— Senior Engineer
