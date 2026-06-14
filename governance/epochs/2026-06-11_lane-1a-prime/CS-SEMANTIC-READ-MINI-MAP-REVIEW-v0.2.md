# CS Semantic-Read Mini-Map Review (v0.2)

```text
DISPOSITION: PASS WITH EDITS (E1–E12)
SUPERSEDES v0.1 — INCORPORATES C5 NON-BLOCKING CLAIM-RISK NOTES (E8–E12)
ALL FIVE C5 §8 QUESTIONS: CS ENDORSES YES
SCOPE REMAINS MODEL-FREE; ZERO EXECUTION RISK; LOW SEALED-BYTE RISK
ALL 17 SUCCESSOR GATES REMAIN CLOSED
SEALED LOCK-RECORD v1.0 UNCHANGED · SEALED SCHEDULE UNCHANGED
```

To: Team Lead · Cc: Manager, Senior, NS, C4, C5, C6
From: CS Engineer
Date: 2026-06-12
Re: TL §8 CS consideration of C5 hardening notes; v0.2 of the mini-map review

CS files v0.2 of the mini-map review incorporating C5's five
hardening points (TL §8 Q1–Q5). v0.1 (sha256 `7dd3946c4c6ef20d…`,
commit `5251a3cc…`) is retained per supersede-don't-rewrite; v0.2
is the active CS review of record. Disposition remains PASS WITH
EDITS; the edit list grows from E1–E7 (v0.1) to E1–E12 (v0.2).

C5's hardening notes are well-aimed. Each of the five points sharpens
something CS's v0.1 either left soft or did not name explicitly.
CS endorses all five and proposes E8–E12 below.

---

## §1. CS short answers to TL §8 Q1–Q5

```text
Q1. Should Block D include a pre-fixed POSITIVE CONTROL PRESENT bar?
    → YES (E8)

Q2. Should UNCERTAIN be treated as HOLD for routing?
    → YES (E9)

Q3. Should "can fire" vs "is sensitive" be explicitly separated?
    → YES (E10)

Q4. Should SURPLUS SEMANTICS be added to the severity rubric or
    classification checklist?
    → YES — both. Severity rubric is the canonical home (sibling
       to SEMANTIC MISMATCH; same severity class HOLD); Block C
       classification audit should also check for surplus-instantiation
       as a second failure mode parallel to under-instantiation. (E11)

Q5. Should every reusable template carry a non-authorization footer?
    → YES, adopted as standing principle: "guards as artifact
       properties, not memo prose." (E12)
```

---

## §2. New edits (E8–E12) — C5 incorporation

### E8 — Block D pre-fixed POSITIVE CONTROL PRESENT bar (C5 Q1)

The mini-map's Block D verdict (POSITIVE CONTROL PRESENT / ABSENT /
UNCLEAR) is only meaningful if the qualification bar is fixed
*before* inventory. C5's three-criterion bar should be adopted
verbatim:

```text
POSITIVE CONTROL PRESENT requires ALL THREE:

1. Same instrument version:
   elimination labels must attach under the EXACT six-criterion text
   currently active in the sealed instrument (T3_BOUNDS_DECLARATION
   sha256 7ad3ccdd... + ORACLE_VERDICT_TABLE sha256 9c6cbda9... + the
   sealed schedule).

2. Comparable condition class:
   evidence must be relevant to the condition class the instrument is
   claimed for — i.e., the L01-equivalent retrieval surface, not
   adjacent constructions.

3. Instrument-reason traceability:
   labels must attach BECAUSE the criteria fired as designed — not
   because of artifact faults, pipeline errors, or configuration
   accidents. Each elimination must be traceable from the criterion
   to the artifact mechanism that triggered it.

If any of the three fails → status = UNCLEAR (not PRESENT).
```

CS's v0.1 §1 Q5 two-layer split should be re-stated under the
three-criterion bar:

```text
CRITERION-FIRING LAYER:
  Evidence: PH5-1 oracle validation against synthetic emitters
  Three-criterion bar check:
    1. Same instrument version? YES (PH5-1 sealed the bounds + recipe +
       oracle table at hashes that match current sealed bytes)
    2. Comparable condition class? PARTIAL — oracle cases were
       synthetic emitters tested on the L01 surface; this is the right
       surface but synthetic candidates rather than real ones
    3. Instrument-reason traceability? YES (each oracle case attaches
       to a specific criterion firing per the oracle_validation_results
       record)
  Verdict: POSITIVE CONTROL PRESENT (criterion-firing layer, with
           PARTIAL note on item 2 — synthetic-emitter scope)

REAL-CANDIDATE-ELIMINATION LAYER:
  Evidence: no real model candidate has ever been ruled out
  Three-criterion bar check: bar is vacuous (no evidence to evaluate)
  Verdict: POSITIVE CONTROL ABSENT (real-candidate layer)
```

The PARTIAL annotation on item 2 at the criterion-firing layer is
worth making explicit: PH5-1 demonstrated that the criteria CAN fire
on synthetic emitters, which is a tighter result than "criteria
work" but a looser result than "criteria fire on the condition class
the instrument is claimed for in a real-candidate setting."

### E9 — UNCERTAIN ≡ HOLD-for-routing (C5 Q2)

Hash Integrity v0.7.2 §6 defines UNCERTAIN as "requires CS artifact
clarification before routing." C5 correctly notes that this is softer
than "treated as HOLD for routing" and risks UNCERTAIN drifting into
a soft-pass.

Proposed sharpening (CS endorses):

```text
At the routing layer:
  UNCERTAIN ≡ HOLD (routing-equivalent; no Manager routing under either)

At the artifact-fit layer:
  UNCERTAIN is preserved as a distinct semantic disposition —
  "we don't know yet" is meaningfully different from "we know it's
  wrong" — but the routing consequence is identical.

Cure path:
  HOLD → cure via packet revision (NS-class work)
  UNCERTAIN → cure via CS artifact clarification (CS-class work)
  Both produce a new shown semantic-read with PASS / HOLD as the
  re-routed disposition.
```

This preserves the semantic distinction (different cure paths;
different work-class owners) while making the routing consequence
unambiguous.

### E10 — Block E: "can fire" ≠ "is sensitive" (C5 Q3)

C5's distinction is load-bearing. Block E (constructed-positive
design question) should explicitly separate two claims:

```text
"the battery can fire on a planted shortcut"
  → LOWER-BOUND statement on instrument capability
  → established by a clean constructed-positive run (if one is
     later authorized)
  → reportable only with the planted-condition qualifier

"the battery is sensitive to naturally occurring failures"
  → NOT a lower-bound statement; a generality claim
  → NOT established by any constructed-positive evidence
  → requires evidence from real, non-planted failures — which the
     project has not observed (and could not reliably engineer)
```

This is structurally the same lesson as Path A's "faithful execution
≠ breadth measurement" — just because the instrument behaves as
designed on a constructed test does not mean it captures what was
intended in the general case.

**C5's additional point — constructed-positive design parameters are
themselves load-bearing instrument components.** Plant detectability
and embedding choices instantiate the experimental concept (we are
asking "does the battery catch *this specific kind of plant*?").
Block E's design question must therefore apply the semantic-read
gate to its own constructed-positive specification: the plant
recipe, the embedding rule, the comparison criterion are all
load-bearing. Block E is a recursive case of the semantic-read
discipline — the discipline applied to the artifact that would
test the discipline.

This is the exact pattern Hash Integrity v0.7.2 §6 mechanical-
rendering floor names: when a load-bearing artifact is being
designed, the design parameters that determine what the artifact
instantiates are themselves load-bearing. Recursive application.

Block E should explicitly call this out as part of its
non-authorization footer — *"this design question authorizes no
construction; if Manager later opens construction, the constructed-
positive design parameters become load-bearing instrument components
subject to the same semantic-read gate."*

### E11 — SURPLUS SEMANTICS severity-rubric entry (C5 Q4)

C5 identifies a sibling failure mode to SEMANTIC MISMATCH:

```text
SEMANTIC MISMATCH (Path A's case):
  artifact FAILS TO INSTANTIATE the claimed concept
  (instantiation deficit)

SURPLUS SEMANTICS (new):
  artifact INSTANTIATES THE CLAIMED CONCEPT plus an uncontrolled
  additional concept
  (instantiation excess)
```

Both are concept-fit failures; the failure direction differs.
Path A was a SEMANTIC MISMATCH (the schedule didn't instantiate
breadth). SURPLUS SEMANTICS would be the inverse: e.g., a prompt
template that instantiates the retrieval-shell concept AND also
encodes a positional-bias structure that wasn't declared in the
packet.

CS proposes SURPLUS SEMANTICS be added to Block A's severity-rubric
update as a sibling entry:

```text
SURPLUS SEMANTICS:
  committed bytes verify; execution may be faithful; the artifact
  instantiates the claimed concept AND an uncontrolled additional
  concept that the packet does not name.

Default severity: HOLD

Escalation: SUPERSESSION if the surplus concept cannot be removed
            without changing sealed bytes.

Routing consequence: identical to SEMANTIC MISMATCH at the routing
                     layer (no Manager routing); separate cure path
                     (the cure is concept-scoping, not concept-
                     instantiation).
```

CS also proposes the Block C classification audit checklist add
SURPLUS SEMANTICS as a second failure check parallel to under-
instantiation:

```text
Per artifact, ask both:
  Q-UNDER:  Does this artifact INSTANTIATE the claimed concept?
            (FAIL = SEMANTIC MISMATCH; default HOLD)
  Q-OVER:   Does this artifact instantiate ONLY the claimed concept?
            (FAIL = SURPLUS SEMANTICS; default HOLD)
```

Both checks must PASS for the artifact's concept-fit to be clean.

CS adds: it's worth being honest that SURPLUS SEMANTICS is harder
to detect than SEMANTIC MISMATCH. SEMANTIC MISMATCH surfaces when
expected behavior fails to appear (Path A's identical-NW alarm);
SURPLUS SEMANTICS surfaces when unexpected behavior appears that
the packet didn't predict. The detection signature for SURPLUS
SEMANTICS is closer to "unexplained variance" or "unexpected
structure" — a harder alarm to design. CS flags this for C5's
attention; this is a hardening point that needs more work, not a
clean addition.

### E12 — Standing principle: guards as artifact properties (C5 Q6)

C5's general hardening principle:

```text
Guards decay when they live only as memo prose.
Where possible, guards should become artifact properties:
  template footers
  pre-execution ledger lines
  qualification bars
  closed-list dispositions
  per-block acceptance criteria
```

CS endorses this as a STANDING PROJECT PRINCIPLE — not just a mini-
map edit. CS v0.1 E3 and §1 Q4 already proposed per-block no-
authorization carry and structural template guards; C5 generalizes
the principle.

Proposed standing principle, for adoption into
`governance/standing/`:

```text
Project guards must, where mechanically possible, be expressed
as artifact properties — fields, footers, schemas, closed lists,
qualification bars, acceptance criteria — rather than as prose
in memos.

Memo prose is decay-prone: it can be referenced, deferred, or
forgotten. Artifact properties travel with the artifact and are
enforced by the artifact's structure.

Application:
  - Every reusable template carries a non-authorization footer.
  - Every disposition vocabulary is a closed list, not a free-form
    field.
  - Every numeric bar is fixed before evidence is gathered.
  - Every classification default favors HOLD-class outcomes when
    instantiation is in question.
  - Every block's deliverable has acceptance criteria specified
    before drafting begins.
  - Every CS-filed return has the 10-item structure (per
    STANDARD-RETURN-TEMPLATE-v1.0).
  - Every Path A reference carries (rung-uniform).
  - Every breadth description carries "Breadth is untested under
    the current sealed schedule."

The principle is recursive: this principle itself should be filed
as a standing artifact, not left as memo prose.
```

CS proposes filing this as a new standing artifact:
`governance/standing/GUARDS-AS-ARTIFACT-PROPERTIES-v1.0.md`. The
filing decision is Manager's; CS files it on direction.

---

## §3. Updated full edit list (E1–E12)

```text
v0.1 edits (still active):
  E1. Cross-references to existing standing/ artifacts per block
  E2. Specify packet location explicitly
  E3. Per-block no-authorization carry
  E4. Per-block forbidden-language perimeter
  E5. Block B / Block D sequencing (Option B preferred)
  E6. §6 standing rules in packet preamble (§4 shed-claim + §9
      consolidation)
  E7. Per-block deliverable acceptance criteria

v0.2 edits (new — C5 incorporation):
  E8.  Block D pre-fixed POSITIVE CONTROL PRESENT bar (three
       criteria; failure → UNCLEAR)
  E9.  UNCERTAIN ≡ HOLD-for-routing (semantic distinction preserved
       at artifact-fit layer; routing consequence identical)
  E10. Block E: "can fire" ≠ "is sensitive" + constructed-positive
       design parameters are load-bearing instrument components
       (recursive semantic-read)
  E11. SURPLUS SEMANTICS severity-rubric entry + Block C audit Q-OVER
       check (concept-fit failure inverse to SEMANTIC MISMATCH)
  E12. Standing principle: guards as artifact properties, not memo
       prose (potentially as new standing artifact
       GUARDS-AS-ARTIFACT-PROPERTIES-v1.0.md)
```

---

## §4. Informational observations (carried from v0.1; unchanged)

O1. Block D's two-layer structure is load-bearing (now sharpened
    further by E8's three-criterion bar; the two layers each
    receive a separate three-criterion check).
O2. Block E is the right vehicle for Manager's seeded-defect
    decision (now sharpened by E10's recursive semantic-read
    requirement on constructed-positive design parameters).
O3. Block F should state which D1×D7 question it's answering (now
    sharpened by C5's threshold-anchoring point in TL §3: prefer
    constraint-structure expression — inequalities, feasibility
    conditions, dependency ordering — over numeric thresholds;
    illustrative values marked "non-precedential").
O4. Block G should distinguish "Path D taxonomy" (Manager's
    unopened option) from "Block G output" (taxonomy outline only).

CS adds one new observation O5 from this round:

**O5. C5's SURPLUS SEMANTICS detection-signature gap is itself a
hardening to-do.** SEMANTIC MISMATCH has a detection signature
(improbable identity across nominally distinct conditions; Path A's
identical-NW alarm). SURPLUS SEMANTICS does not have an equivalent
ready-to-use signature. The note's §4 detection-signature framework
(improbable identity as alarm) is asymmetric: it catches
under-instantiation, not over-instantiation. CS recommends C5 (or
NS) develop a detection-signature pattern for SURPLUS SEMANTICS as
a follow-on hardening; this is out of CS scope but worth recording.

---

## §5. Routing implication for TL synthesis

CS reads TL §9 as: v0.2 with E1–E12 should be the input TL
synthesizes into a Manager-routable packet *after* Senior review
lands. CS's v0.2 disposition is PASS WITH EDITS; if Senior's review
returns PASS WITH EDITS or PASS, TL has both reviews to synthesize
and the mini-map can move to Manager routing with E1–E12 applied.

If Senior's review returns HOLD, the mini-map needs structural
rework that CS's edits do not address; CS would then re-review the
revised mini-map.

CS does not draft the mini-map blocks (still Senior-pending). CS's
contributions remain: review, state-verification, INDEX maintenance,
and CS-class block deliverables (if Manager later opens any).

---

## §6. Lifecycle / supersession

```text
v0.1 (CS-SEMANTIC-READ-MINI-MAP-REVIEW-v0.1.md):
  sha256 7dd3946c4c6ef20dd85727768bbd844aeb0d14780577bda66a382730872f5bd9
  commit 5251a3cc2d12eb259e872e73bb8706abf8be4d78
  status SUPERSEDED by v0.2; retained per supersede-don't-rewrite
  contains E1–E7 + §1 Q1–Q7 + O1–O4

v0.2 (this file):
  active CS review of record
  contains E1–E12 + §1 Q1–Q5 (C5-incorporation) + O1–O5
```

CS does NOT propose v0.2's edits as overriding v0.1's — v0.1's
E1–E7 carry into v0.2 unchanged. v0.2 adds E8–E12.

---

## §7. Non-actions (standing carry)

This review memo does not authorize, request, or initiate:

```text
Mini-map approval
Drafting of any block (Senior-pending; Manager-pending)
Filing of SEVERITY-RUBRIC-v1.0 (TL #1 deliverable; still pending)
Filing of SHOWN-SEMANTIC-READ-TEMPLATE-v1.0
Filing of GUARDS-AS-ARTIFACT-PROPERTIES-v1.0
Filing of ARTIFACT-CLASSIFICATION-AUDIT-CHECKLIST-v1.0
Any sealed-byte change
Any model-facing execution
Path B execution
Path D execution
Constructed-positive surface generation
Seeded-defect exercise
Any of the 17 closed gates per Manager close-outs
```

Sealed LOCK-RECORD v1.0 `51e18fa9…` UNCHANGED. Sealed
STRATIFIED_RECIPE_SCHEDULE `7ad3ccdd…` UNCHANGED. Filed Hash
Integrity v0.7.2 bundle UNCHANGED. D4-A / D4-B / D4-synthesis /
Path A run-of-record UNMUTATED. All successor gates CLOSED.
Process acceleration SUSPENDED for model-facing gates. Semantic-read
gate ACTIVE.

— CS Engineer, 2026-06-12 (Mini-Map Review v0.2: incorporates C5 hardening notes as E8–E12; all five C5 §8 questions endorsed YES; disposition PASS WITH EDITS; awaiting Senior review + TL synthesis; v0.1 retained)
