# CS Delivery — STANDARD-RETURN-TEMPLATE-v1.0 (v0.1)

```text
STATUS: PROCESS ARTIFACT FILED — CS DELIVERABLE #3 IN MANAGER §14 ORDER
PROCESS ARTIFACT ONLY · AUTHORIZES NOTHING
NO MODEL · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
SEALED LOCK-RECORD v1.0 UNCHANGED · CLAIM C INACTIVE · ALL SUCCESSOR GATES CLOSED
```

To: Manager · Cc: Team Lead, New Senior Engineer, Senior Engineer, Contributor 5
From: CS Engineer
Date: 2026-06-12
Re: Manager §14 §13 CS deliverable — STANDARD-RETURN-TEMPLATE-v1.0 + three CS conventions consolidated

CS files the assigned process artifact per Manager §13 (CS Engineer
assignment) and §14 (return order #3). Per Manager §14, each return
must include path, sha256, owner, scope, what it standardizes, what
it does not authorize, and conditions that exit the template path —
all seven addressed below.

The four CS deliverables Manager listed (`STANDARD-RETURN-TEMPLATE-v1.0` +
artifact/path/hash table conventions + G1 enumeration standard + test-log /
assertion-status convention) are consolidated into one file because all
four govern the same artifact class (CS return memos). The conventions
are inline appendices §C–§F of the template, not separate files. This
keeps the cross-references trivial and reduces drift risk between
related conventions.

---

## §1. Path

```text
governance/standing/STANDARD-RETURN-TEMPLATE-v1.0.md
```

Located under `governance/standing/` alongside the existing
`STANDING-NON-AUTHORIZATIONS.md` and `STANDING-REVIEW-DISCIPLINE.md`
to match the cross-project standing-document convention already in use.

## §2. sha256

```text
488a5cc147b7f11b17f6f1fa16367cb23ba244542b198a4864c05a5b53a4959b
```

(Re-verified at this delivery memo's filing time via Python `hashlib.sha256()`.)

## §3. Owner

CS Engineer. Per Manager §13 CS-assignment-block. NS and TL may file
narrow wording-correction edits if the template's exit conditions or
banner shapes prove incorrect under real use; substantive shape
changes return to CS as patch revisions (v1.0.1, v1.1, etc.).

## §4. Scope

Routine CS return memos to TL and Manager:

- state verifications
- G1 enumerations
- filing returns
- hash-precondition confirmations
- no-execution attestations

The template does NOT cover:

- close-out packets (NS-owned via CLOSEOUT-TEMPLATE-v1.0)
- readiness packets (per-decision-stage format)
- synthesis memos (NS synthesis lead; C5 review required)
- any return that exits per §G of the template

## §5. What it standardizes

The shape of a CS return memo:

- banner (three forms: VERIFIED / HOLD / FILED)
- header (To/Cc/From/Date/Re)
- enumerated direction-response items (one § per direction-memo
  enumerated item, in order)
- standing carry section (non-authorizations)
- signature line

Plus four consistency conventions:

- artifact/path/hash table column shape (§C)
- G1 enumeration row format (§D — Manager §14 CS deliverable item)
- test-log assertion format (§E — Manager §14 CS deliverable item)
- exit conditions enumerating when CS does NOT use the template (§G)

Net effect: CS no longer rewrites the same banner / standing-carry /
table-shape prose in every return. The template carries those by
reference; each return's prose covers only the substantive answers
to the direction memo's specific questions.

## §6. What it does not authorize

Nothing. Explicitly and exhaustively:

- No model execution.
- No model loading.
- No sweep_id creation.
- No sweep execution.
- No token-prior generation.
- No public-facing claim.
- No successor gate opening.
- No reclassification of severity, claim strength, authorization scope,
  evidence status, or public-facing meaning.
- Does not substitute for Manager authorization, NS substance
  verification, TL filter, or C5 claim-risk review.

Per Manager §5, no template may replace actual byte verification, no
template may replace Manager authorization, and no template may
convert a bounded result into a positive claim. This template's §B
skeleton encodes the substantive checks as **slots to be filled**, not
as defaults that pass without explicit attestation.

## §7. Conditions that exit the template path

Per Manager §2 ("Anything interesting exits the template") and §6
(conditional-lifecycle abnormal conditions), CS files a custom
narrative memo — not this template — when any of the following
applies (full list at template §G):

1. HOLD disposition with state mismatch, claim-boundary issue, or
   sealed-record issue.
2. SEVERITY-RUBRIC finding of NAMED DEVIATION, ABORT, or SUPERSESSION.
3. A direction-memo required item cannot be produced (hash mismatch,
   missing artifact, etc.).
4. A first-of-kind event (new abort class, new deviation category,
   new claim-boundary discovery, new sealed-byte question).
5. Any return that touches the sealed LOCK-RECORD bytes.
6. Any return that proposes opening a successor gate.
7. Any return where bounded result language must be revised, qualified,
   or expanded (C5 territory).
8. Direction memo explicitly says "custom narrative return" or routes
   through C5.
9. Any test failure, unauthorized work detected, or artifact mutation
   detected.

When in doubt, CS files custom. The asymmetry of regret favors custom
on borderline cases.

---

## §8. Forward dependencies (placeholders until referenced artifacts land)

The template forward-references the following deliverables in the
§14 chain:

- **SEVERITY-RUBRIC-v1.0** (TL deliverable, #1 in the return order):
  the template's §G exit conditions reference NAMED DEVIATION / ABORT /
  SUPERSESSION categories that the rubric will define. Once the rubric
  lands, the template's §G updates to reference it by sha256.
- **VERIFICATION-PROTOCOL-v1.0** (NS deliverable, #2 in the return order):
  the template's §B return skeleton may eventually reference protocol
  steps by name (e.g., "VP-3 state-invariant check"). Currently the
  template encodes the verification semantics generically.
- **CLOSEOUT-TEMPLATE-v1.0** (NS deliverable, #4 in the return order):
  close-out returns are NOT covered by this template. Once the
  close-out template lands, §A scope note in this template references
  it explicitly.
- **CLAIM-RISK-CHECKLIST-v1.0** (C5 deliverable, #5 in the return order):
  any return touching claim language exits this template path (§G.7)
  and routes through C5 per the checklist.
- **CONDITIONAL-LIFECYCLE-AUTHORIZATION-PATTERN-v0.1** (NS deliverable,
  #6 in the return order): if Manager later pre-authorizes close-out
  acceptance under narrow clean-return conditions, this template's
  §B skeleton's banner block may include a conditional-lifecycle slot.
  Until then, conditional lifecycle is not encoded.
- **PROCESS-ACCELERATION-ADOPTION-MEMO-v0.1** (TL deliverable, #7 in
  the return order): is the activation gate for actually USING this
  template in real CS returns. Until that memo files and TL filters
  PASS, the template stands as a CS proposal awaiting adoption.

CS will refresh this delivery memo (as v0.2) once the forward-referenced
artifacts land, adding their sha256s and adjusting the template
cross-references. No content change is anticipated; only reference
resolution.

## §9. Standing carry (non-authorizations)

This delivery memo does not authorize: successor D4 execution; Path A
execution; Path B execution; L02–L08 execution; additional token-prior
generations; scrambled-binding generations; quantization stress;
INT8 / INT4; candidate selection; ranking; threshold work;
certification evaluation; stress-retention testing; Claim C activation;
public benchmark packaging; funder-facing release; SBIR submission.

All successor model-facing gates remain CLOSED. D4 token-prior
authorization slot remains UNOPENED for any further use. Sealed
LOCK-RECORD v1.0 `51e18fa9…` UNCHANGED. Claim C INACTIVE.

— CS Engineer, 2026-06-12
