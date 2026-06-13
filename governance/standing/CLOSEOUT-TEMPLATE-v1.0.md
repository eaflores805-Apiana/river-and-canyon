# CLOSEOUT-TEMPLATE v1.0

```text
PROCESS ARTIFACT — STANDARDIZES CLOSE-OUT PACKET STRUCTURE ONLY
AUTHORIZES NOTHING; CLOSE-OUT ACCEPTANCE REMAINS A MANAGER DECISION (or a pre-authorized
acceptance under CONDITIONAL-LIFECYCLE-AUTHORIZATION-PATTERN where the Manager granted it)
```

*Owner: New Senior Engineer (with CS artifacts). Scope: D5-class close-out packets for completed
run lifecycles. Codified from the accepted D5 and D5-B packets.*

## Required masthead

Status banner (preparation-only; acceptance is separate) · the lifecycle's accepted bounded
result, verbatim, leading · "strongest permitted interpretation / may not be strengthened" ·
no-successor confirmations line.

## Required sections, in order

```text
S1  Execution summary — sweep_id(s), model identity computed=authorized, framework
    pin chain, decoding hash, extent, pass discipline, runner file + hash, aborts
    (count and disposition).
S2  Verified artifact basis — BY REFERENCE to the NS verification memo (path + hash);
    do not restate the enumeration; the verification memo is incorporated whole.
S3  Result summary — per-criterion outcomes; attached_labels; outcome term; every
    number traceable to verified bytes.
S4  Control summary (where controls ran) — measured values, descriptive comparison
    to analytical expectation, the control guard verbatim (control artifacts only;
    not candidate evidence; not threshold material; not reusable outside the locked
    comparison).
S5  Comparison summary — locked rule, locked margin, the verifier's independent
    recomputation cited as the evidentiary basis.
S6  Bounded result language — accepted sentence + interpretation, nowhere
    strengthened.
S7  Deviations and notations — every named deviation with lifecycle state; every
    notation with rubric class; "none" is written, not implied.
S8  No-mutation confirmation — the diff-by-construction statement for all prior
    closed lifecycles.
S9  Non-claim block — standing does-not-establish list, forbidden phrasings,
    standing framing, verbatim.
S10 Guards by reference — constructibility-risk note (three branches, third
    first-class, not presumed) and any lifecycle-specific guards.
S11 Successor-gate status — all gates enumerated closed unless separately
    authorized by name.
S12 Recommendation — whether close-out may be accepted, with the one-sentence
    basis; the recommendation closes a record and authorizes nothing.
S13 Confirmations — no successor execution / sweep_id / model execution / TP
    generations / quantization / Claim C activation, as applicable.
```

## Template-exit conditions

A close-out exits this template (bespoke packet, full prose) if the lifecycle contains: an abort ·
an INCONCLUSIVE outcome · a criterion firing requiring interpretation · an unresolved deviation ·
a sealed-record or supersession event · any claim-language question C5 has not already cleared.
Clean lifecycles only.

## What this template does not do

Does not accept anything; does not compress the bounded language; does not let S2's by-reference
form substitute for the verification having actually occurred; does not apply to synthesis,
readiness, or proposal documents (those remain bespoke).

— New Senior Engineer
