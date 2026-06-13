# VERIFICATION-PROTOCOL v1.0

```text
PROCESS ARTIFACT — STANDARDIZES VERIFICATION STRUCTURE ONLY
AUTHORIZES NOTHING: no execution, no model, no sweep_id, no TP generations, no claims
TEMPLATES SPEED NORMAL CASES. ANYTHING INTERESTING EXITS THE TEMPLATE.
```

*Owner: New Senior Engineer. Scope: all byte-verification requests and performances in Lane 1a′
Prime and successor work. Codified from the D4-A / D4-B arc as actually performed.*

## 1. Invocation

A Team Lead memo may invoke this protocol in one line — "Verify per VERIFICATION-PROTOCOL-v1.0,
profile <P>, commit <SHA>" — plus only the run-specific items (authorized constraints, expected
sweep_ids, any special audits). The protocol supplies the rest.

## 2. Standing verification battery (every invocation)

```text
V1  Pull clean; verify reported commit SHA is HEAD or named ancestor.
V2  Recompute sha256 of every path+hash pair in the return memo (G1 enumeration);
    report N/N. Any miss = HOLD.
V3  Recompute sealed LOCK-RECORD v1.0; must equal 51e18fa9…1935 byte-identical.
V4  No-mutation by construction: git diff <prior-accepted>..<verified> --name-only;
    any touch to a closed lifecycle's artifact tree = HOLD. The diff list is the
    evidence; per-file re-hashing is corroboration, not substitute.
V5  Constraint audit from the execution ledger against the authorization memo,
    item by item (extent, model identity computed=authorized, framework pin,
    decoding hash, pass/retry discipline, prohibited-work absence).
V6  Per-run runner provenance: ledger runner_hash must match a committed runner
    file introduced in or before the run commit; each run its own runner file.
V7  Emitter-field audit: all four TP fields present in symmetric form in EVERY
    emitted report (pre-flight, t1, t3, t4, A6, ledger, IVR). Absence = HOLD
    (grace spent as of D4-B).
V8  Independent recomputation of every decision-bearing statistic from raw counts
    under the locked rule (e.g., Wilson / Newcombe–Wilson intervals, margins).
    Matching the ledger to reported precision is required; the verifier's
    arithmetic, not the report, is the evidence.
V9  Language audit: no forbidden phrasing outside prohibition/non-claim context;
    bounded sentence present in accepted or equivalent form (equivalence must be
    stated and shown, not assumed).
V10 Unauthorized-work sweep: no artifacts outside the authorized output tree;
    no undeclared sweep_ids; no model/quantization/threshold/Claim C residue.
```

## 3. Verifier conduct rules

Read committed bytes before trusting any summary, including this seat's own prior summaries.
Flat-string checks are screening only — every check-string failure is chased to the committed
line before being reported; false alarms (line-wraps, italics/blockquote markers, field-name
variants, wrong-file comparisons) are recorded honestly in the return, never silently dropped.
Verification of a correction applies the same battery to the correction's own factual claims.

## 4. Outcomes

**VERIFIED** — all battery items pass; minor notations (below deviation bar) may ride along,
classified per SEVERITY-RUBRIC-v1.0. **HOLD** — any battery miss; names the specific mismatch and
the one action that clears it; HOLD is a good outcome and is never softened to a notation to keep
a chain clean. There is no third outcome.

## 5. Template-exit conditions (mandatory)

Any of the following exits this protocol into bespoke handling with full fresh memos: HOLD ·
named deviation · abort · INCONCLUSIVE · criterion firing requiring interpretation · artifact or
path/hash mismatch · unexpected output distribution · claim-boundary issue · sealed-record issue ·
runner/provenance issue · unauthorized work · anything the verifier judges interesting. Exit is
one-way for that lifecycle stage; re-entry requires Team Lead direction.

## 6. What this protocol does not do

It does not replace byte verification with assertion; does not replace Manager authorization;
does not classify severities (rubric's job); does not accept results (Manager's); does not touch
result language (bounded forms and non-claim blocks bind unchanged).

— New Senior Engineer
