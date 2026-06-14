# EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1

**Version:** v0.1. River and Canyon program. Track: Eval-Validity Gate Tool Spec (Tier 1 instrument). 
**Goal:** convert Paper A ("Before Retention: A Fail-Closed Validity Gate for LLM Stress-Retention Evaluation," v1.0) into a reusable protocol / tool architecture.
**Status:** MODEL-FREE SPECIFICATION. This document specifies an architecture; it authorizes no model execution and builds no software. Paper A v1.0 is the source of truth; where this spec and Paper A disagree, Paper A wins. Anchored on origin/main HEAD 55c9bc1.
**Owner split (proposed):** Senior (drafter — keep the automated/human-read line identical to Paper A's implemented/specified split) → CS (verify no spec element overstates what Paper A demonstrated, and no execution is implied) → Team Lead (route as a Tier-1 instrument artifact, separate from the CAL-Q finding track and from Paper B) → Manager.

---

## 0. What this spec is, and is not

```text
IS:  an architecture that turns Paper A's worked gate into a reusable protocol.
IS:  a precise statement of what is automatable vs what needs a human semantic read.
IS:  faithful to Paper A's central discipline — a gate whose output is a ROUTE
     DECISION, not a score, and which FAILS CLOSED.
NOT: a built tool. No code is delivered or implied.
NOT: a claim that the gate is validated. Paper A establishes it on ONE family /
     ONE model / N=2 episodes / pre-stress; this spec inherits exactly that scope.
NOT: an execution authorization, a benchmark, or a product. Those are downstream
     and separately gated.
```

The spec's value is precisely that it draws the automated-vs-human line *honestly*. That line is not an engineering convenience — it is Paper A's implemented/specified split (§4.3) rendered as an architecture. Blurring it would undo the paper's discipline, so it is held as a hard constraint throughout (§8).

## 1. Carried forward from Paper A v1.0 (binding constraints)

```text
C1. OUTPUT IS A ROUTE DECISION, NOT A SCORE.
    The gate emits one of {pass, needs-repair, quarantine, refuse} plus an
    evidence packet — never a bare retention number.
C2. FAIL CLOSED.
    Absence of demonstrated construct validity at the baseline yields a logged
    REFUSAL, not a pass-by-default and not a retention number.
C3. THE BASELINE IS THE OBJECT.
    The gate certifies whether the BASELINE measures the intended construct,
    BEFORE any retention/stress comparison. It is prior to certifying the
    measurement process (the empty-certificate argument, Paper A §1.3/§6.4).
C4. PER-ITEM BEFORE AGGREGATE.
    No route decision rests on a summary statistic alone; the per-item read and
    the scorer audit gate every decision (Paper A §3, the CAL-E/CAL-Q lesson).
C5. SCOPE IS INHERITED, NOT EXPANDED.
    Thresholds, bins, and "what counts as a defect" are construction/model/task
    specific until independently justified. The architecture is portable; the
    numbers are not (Paper A's gate-portability caveat).
C6. MECHANIZED INDEPENDENCE IS REQUIRED FOR THE AUDIT (Paper A §5.1, W1 fix).
    A rejection audit whose "independent read" is the SAME per-item read that
    produced the refusal is circular. Independence must be mechanized (blind
    second reader / pre-registered schema applied without knowledge of the route
    / external labels). Absent that, the audit catches aggregate-vs-item
    disagreement but NOT reading-standard miscalibration — and the tool must say so.
```

## 2. Inputs

The gate operates on a **baseline submission**: everything needed to decide whether a proposed baseline measures the intended construct. Required inputs:

```text
IN1. CONSTRUCT DECLARATION
     - the intended capability in the real system's own terms (no analogy —
       the "No Mountain in the Sentence" rule);
     - the operational definition of a CORRECT response and of a legitimate
       ABSTENTION / absence response.
IN2. ITEM SET + KEYS
     - the evaluation items, each labelled present/absent (or the task's
       analogue of answerable/unanswerable), with ground-truth values;
     - enough per-item structure that a per-item read is possible (C4).
IN3. MODEL OUTPUTS
     - raw per-item model outputs on the item set (NOT pre-scored), so the
       scorer audit (G2) can be applied by the gate rather than trusted.
IN4. SCORER DEFINITION
     - the scoring function(s) to be audited: at minimum a strict scorer and a
       concept-level scorer, so strict-vs-concept divergence is measurable.
IN5. PRE-DECLARED RULES
     - the decision thresholds and the route rules, declared BEFORE outputs are
       inspected (C4/C5); a rule chosen after seeing outputs is logged as
       post-hoc and weakens the decision (mirrors Paper A §5.1 Q4).
IN6. PROVENANCE METADATA
     - model id + precision, item-set hash, scorer-version hash, run record
       hashes — so every downstream decision is traceable (G5).
IN7. (FUTURE) INDEPENDENCE CHANNEL
     - for the standing audit (G6): a blind-second-reader interface, a
       pre-registered classification schema, or external labels. SPECIFIED,
       not yet available (see §8).
```

Missing or unhashable required inputs (IN1–IN6) are themselves a **fail-closed condition**: the gate cannot certify a baseline it cannot inspect, and returns `quarantine: insufficient-input` rather than proceeding.

## 3. Gates (the ordered checks)

The gate is an ordered set of checks. The first five are **implemented and exercised in Paper A**; the remaining are **specified but unbuilt** and are marked as such (the split is binding — §8). Order matters: a failure at an earlier gate short-circuits to a route decision without running later gates.

```text
G1. BASELINE CERTIFICATION GATE                                   [IMPLEMENTED]
    Is the clean baseline off-ceiling enough to leave retention headroom, and
    does it perform the intended task at all? A ceiling baseline cannot serve as
    a retention substrate (Paper A §3.1). 
    -> ceiling/floor or non-performing baseline => not a valid substrate.

G2. STRICT-VERSUS-CONCEPT SCORER AUDIT                            [IMPLEMENTED]
    Does the decision survive both a strict and a concept-level scorer, or is the
    apparent signal a scorer artifact? (The CAL-E reversal: an aggregate "failure"
    that the per-item/concept read overturned.)
    -> strict/concept divergence => flag scorer artifact before any other reading.

G3. FOUR-WAY REPORTING OF ABSENCE-DEFINED BEHAVIOR               [IMPLEMENTED]
    On absence-defined items, classify each output four ways: correct-abstention /
    false-emission / format-artifact-abstention / genuine-value-emission. (This is
    what distinguished CAL-Q's real collapse from a parser miss.)
    -> resolves whether an abstention "collapse" is real or a counting artifact.

G4. CONSTRUCT-VALIDITY GATE                                       [IMPLEMENTED]
    Does the baseline still measure the intended construct, per item? The check
    that refused CAL-Q: surface score real, construct collapsed (abstention 0.00).
    -> construct collapse => REFUSE, even if the surface/clean number looks usable.

G5. PROVENANCE AND ROUTE CONTROL                                 [IMPLEMENTED]
    Are inputs artifact-locked and hashed, and is the route decision admitted only
    via protocol compliance (non-conforming runs quarantined, not allowed to shape
    claims)?
    -> unhashed / non-conforming => quarantine.

--- boundary: everything below is SPECIFIED BUT UNBUILT (Paper A §4.3) ---

G6. STANDING REJECTION AUDIT (with mechanized independence)        [SPECIFIED]
    For every refusal, the four audit questions (Paper A §5.1): was it correct;
    could it be a scoring artifact; do per-item reads confirm it; was the rule
    pre-declared? CRITICALLY (C6): the confirming read must be MECHANIZED-
    INDEPENDENT of the read that produced the refusal, or the audit is circular.
    Status: NO run artifact exists; this is the highest-value remaining build.
    Until built+exercised, the tool's "non-vacuousness" is SUGGESTED, not established.

G7. SAME-ERROR IDENTITY                                            [SPECIFIED]
    Under stress, is a "retained" behavior the SAME operation, or a different
    operation yielding the same answer? Specified; no implementation.

G8. CROSS-FAMILY / CROSS-MODEL GENERALITY                         [SPECIFIED]
    Does the gate behave consistently across task families and models? Specified;
    Paper A is one family / one model only.

G9. FULL STRESS-RETENTION PIPELINE                                [SPECIFIED]
    The end-to-end path the instrument is ultimately for: certified baseline ->
    executed compression rung -> retention interpreted against it. PRE-STRESS;
    no rung has run; requires separate authorization.
```

## 4. Outputs (the route decisions)

The gate emits exactly one route decision per baseline submission, plus the evidence packet (§5). No bare score is ever emitted (C1).

```text
PASS          The baseline is certified to measure the intended construct and is
              off-ceiling enough to serve as a retention substrate. A retention
              comparison MAY proceed. (Note: in Paper A's family, NO candidate
              reached PASS — the certifiable region was unoccupied. PASS is
              defined here; it has not been observed.)
NEEDS-REPAIR  A specific, named defect is present but plausibly fixable (e.g.
              ceiling saturation that a difficulty lever might address). The packet
              names what to change; the resubmitted baseline re-enters at G1.
QUARANTINE    The submission cannot be cleanly adjudicated — missing/unhashed
              inputs, non-conforming run, or scorer artifact unresolved (G2/G5).
              The baseline is held OUT of any claim until the issue is resolved.
REFUSE        The baseline's construct has demonstrably collapsed (G4): the surface
              score may look usable, but per-item reads show it no longer measures
              the intended capability. NOT safe to compare. Logged with evidence.
```

## 5. Evidence packet (emitted with every decision)

Every route decision ships with a packet that makes the decision auditable and reproducible. Minimum contents:

```text
EP1. DECISION + the gate that produced it (which of G1-G9 fired, in order).
EP2. PER-ITEM TABLE: each item's input, output, strict score, concept score,
     and four-way absence classification (G3) where applicable.
EP3. THE PRE-DECLARED RULE that was applied, with a flag if any rule was post-hoc.
EP4. PROVENANCE BLOCK: model id+precision, item-set hash, scorer hash, run-record
     hashes (IN6) — so the decision is traceable to locked artifacts.
EP5. SCOPE STAMP: "evidence about the instrument, not the model," plus the
     family/model the decision is scoped to (C5).
EP6. (FOR REFUSALS) THE AUDIT RESULT once G6 exists: confirmed / reversed, and BY
     WHAT INDEPENDENT CHANNEL. Until G6 is built, the packet states explicitly
     that the refusal rests on the per-item read WITHOUT mechanized-independent
     confirmation (honest interim status, per C6).
```

## 6. Failure classes (what can go wrong, and how it routes)

The tool distinguishes failure *of the baseline* from failure *of the submission* from failure *of the instrument itself*:

```text
FC1. BASELINE-AT-CEILING            -> NEEDS-REPAIR (no retention headroom; G1).
FC2. CONSTRUCT-COLLAPSE             -> REFUSE (surface ok, construct gone; G4).
FC3. SCORER-ARTIFACT                -> resolve via G2/G3; if the "defect" is a
                                       scoring artifact, do NOT refuse — the
                                       CAL-E lesson (an apparent failure reversed).
FC4. INSUFFICIENT/UNHASHED INPUT    -> QUARANTINE (cannot certify what it can't
                                       inspect; §2).
FC5. NON-CONFORMING RUN             -> QUARANTINE (provenance/route violation; G5).
FC6. POST-HOC RULE                  -> decision still emitted, but flagged as
                                       weakened evidence (rule chosen after data).
FC7. AUDIT-CIRCULARITY (instrument) -> if a refusal's only confirmation is the same
                                       read that produced it, the tool must DECLINE
                                       to call the refusal independently confirmed
                                       (C6) — a failure mode of the TOOL, surfaced
                                       honestly, not hidden.
FC8. OUT-OF-SCOPE GENERALIZATION    -> the tool refuses to extend a decision beyond
                                       the family/model it was run on (C5); reported
                                       as "not adjudicated here," not as a pass.
```

## 7. Quarantine rules

```text
QR1. Quarantined submissions are HELD OUT of every claim until the blocking issue
     (FC4/FC5, or an unresolved FC3) is resolved; they do not pass by default and
     do not silently expire into a pass.
QR2. A quarantine is logged with its cause and the exact missing/failing input, so
     resolution is checkable.
QR3. Resolving a quarantine re-enters the submission at the gate that quarantined it
     (not at the end) — the earlier gates must still hold.
QR4. Quarantine is NOT refusal: it means "cannot yet adjudicate," not "construct
     collapsed." The two are reported distinctly (a reader must not read a
     provenance gap as a construct failure, or vice versa).
```

## 8. What is automated vs what requires a human semantic read

This is the spec's load-bearing section, and it is identical to Paper A's implemented/specified split (§4.3). The line is drawn by one test: **can the check be made without a human judging meaning?** Counting, hashing, threshold comparison, and format classification can be automated. Judging *whether an output means what the construct intended* cannot — yet — and the tool must not pretend otherwise.

```text
AUTOMATABLE (mechanical — counting, comparison, hashing, format-matching):
  - G1 ceiling/floor detection (threshold comparison on clean accuracy).
  - G2 strict-vs-concept DIVERGENCE detection (run both scorers, compare) — note:
       FLAGGING divergence is automatable; ADJUDICATING which scorer is right may
       need a human read (below).
  - G3 four-way tallying ONCE the per-item labels exist (counting).
  - G5 provenance/hash checks and conformance gating (mechanical).
  - EP1-EP5 packet assembly (mechanical once the reads exist).
  - QR1-QR3 quarantine bookkeeping (mechanical).

REQUIRES HUMAN SEMANTIC READ (judging meaning — NOT yet automatable):
  - G4 construct-validity judgement: deciding that an output is a genuine value
       emission rather than a legitimate response in disguise — the read that
       distinguished CAL-Q's real collapse. This is the per-item semantic read
       at the heart of Paper A, and it is human.
  - G2 ADJUDICATION (not just flagging): when strict and concept diverge, deciding
       which reflects the construct (the CAL-E call) is a semantic judgement.
  - The CONSTRUCT DECLARATION itself (IN1): stating the capability in the system's
       own terms is a human act ("No Mountain in the Sentence").
  - G6's INDEPENDENT confirming read: even when mechanized via a schema, designing
       the schema and the blind-reading protocol is human; the point of C6 is that
       this independence cannot be faked by re-running the same automated read.

SPECIFIED-BUT-UNBUILT (no automation AND no exercised manual procedure yet):
  - G6 standing rejection audit, G7 same-error identity, G8 cross-family generality,
    G9 full stress pipeline. These are architecture, not capability. The tool's
    honest status is: the automatable mechanical layer plus a HUMAN per-item
    semantic read implement G1-G5 on one family; G6-G9 are specified.
```

The single most important honesty constraint: **the construct-validity judgement (G4) and the audit's independent read (G6) are human semantic reads, not automated gates.** A version of this tool that quietly automates G4 — by, say, pattern-matching "looks like a value" — would be exactly the kind of shortcut baseline the gate exists to refuse. The tool must keep the semantic read human until an independently-justified automation is demonstrated, and must label any automated proxy as a proxy.

## 9. Relationship to the rest of the program

```text
- PAPER A is the source of truth and is complete (on GitHub, v1.0). This spec adds
  no claim to it; it re-expresses its architecture and inherits its scope exactly.
- The first BUILD this spec motivates is G6 (the standing rejection audit with
  mechanized independence) — the same component Paper A §6.3 and all three external
  reviews named as the highest-value remaining work. Building it would turn the
  tool's non-vacuousness from "suggested" to "demonstrated." It is MODEL-FREE.
- CAL-Q FINDING TRACK stays alive but secondary: its diagnostics (D1/D2/D3) are
  future research about abstention transfer, not part of this Tier-1 spec.
- D4 rescue: CLOSED. PAPER B stress rung (G9): later, separately authorized.
- The SEAM (Claim C): open, deferred. Nothing here activates it.
```

## 10. Boundary (closed gates — unchanged)

```text
No model execution.       No second compression rung.
No new run.               No full ladder.
No D4 rescue.             No Claim C activation.
No CAL-Q rerun.           No public benchmark packaging.
No certification run.     No funder-facing release.
No compression.           No SBIR submission.
No INT8 / INT4 stress.    No software build (this is a spec, not a tool).
```

This is specification only. Paper A is the source of truth. The next buildable increment it points at is G6, model-free, separately scoped.

## 11. For CS verification (what to check)

```text
- That NO gate in §3 claims more than Paper A demonstrated: G1-G5 marked
  implemented, G6-G9 marked specified, and the boundary line drawn exactly at
  Paper A's §4.3 split.
- That §8's automated-vs-human line matches that split — in particular, that G4
  (construct-validity judgement) and G6's independent read are on the HUMAN side,
  not quietly automated.
- That the mechanized-independence requirement (C6) is preserved and that the spec
  nowhere implies the audit can confirm a refusal by re-running the same read.
- That no execution, run, build, or benchmark is authorized or implied; that the
  closed gates (§10) are intact; and that the spec is scoped to one family/one
  model exactly as Paper A is (C5).
```

— Senior Engineer
