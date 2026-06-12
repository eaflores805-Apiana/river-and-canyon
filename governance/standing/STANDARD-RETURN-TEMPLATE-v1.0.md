# Standard Return Template — v1.0

*CS-owned process artifact. Standing skeleton for CS return memos to TL and Manager. Adopted per Manager "Process Acceleration Protocols" notice (2026-06-12). Templates speed normal cases. Anything interesting exits the template.*

**Owner:** CS Engineer
**Last reviewed:** 2026-06-12
**Status:** v1.0 draft; awaiting TL filter under PROCESS-ACCELERATION-ADOPTION-MEMO. Forward-references SEVERITY-RUBRIC-v1.0 (TL) and VERIFICATION-PROTOCOL-v1.0 (NS) — those names are placeholders until they land.

---

## §A. Manager §14 process-artifact header

| Field | Value |
|---|---|
| **Path** | `governance/standing/STANDARD-RETURN-TEMPLATE-v1.0.md` |
| **sha256** | (recorded in CS delivery memo after this file commits) |
| **Owner** | CS Engineer |
| **Scope** | Routine CS return memos to TL and Manager (state verifications, G1 enumerations, filing returns, hash-precondition confirmations, no-execution attestations). |
| **What it standardizes** | The shape of a CS return memo for normal-case work: banner, header, enumerated direction-response items, standing carries, signature. Eliminates the prose CS rewrites in every return. |
| **What it does not authorize** | Nothing. This template authorizes no execution, no model load, no sweep_id creation, no token-prior generation, no public-facing claim, no successor gate opening, no severity reclassification, and does not substitute for Manager authorization, NS substance verification, TL filter, or C5 claim-risk review on documents that require them. |
| **Conditions that exit the template path** | See §G below ("Exit conditions"). When any exit condition applies, CS files a custom narrative memo, not this template. |

---

## §B. The standard return memo skeleton

A normal-case CS return memo follows this shape:

```markdown
# CS [Return-Type] — [Subject] (v0.1)

[Banner — see §C. Use the appropriate banner for this return's status.]

To: Team Lead · Cc: [as appropriate per the direction memo's To/Cc]
From: CS Engineer
Date: YYYY-MM-DD
Re: [Direction memo §reference] [N-item return] for [subject]

[One-paragraph opening. State the disposition (VERIFIED / HOLD / FILED / etc.).
State the §reference of the direction memo this responds to. State the
artifact filed or verified. No prose beyond what a future reader needs to
orient.]

---

## §1. [First enumerated item from the direction memo]

[Answer; include hash/path/sha256/confirmation as the direction requires.]

## §2. [Second enumerated item]

[Answer.]

... (one section per item the direction memo enumerated)

---

## §N. Standing carry (non-authorizations, verbatim)

This [return-type] does not authorize: [reference the standing carry hash
once that file exists; until then, enumerate per the direction memo's
prohibition list, which carries verbatim].

All successor gates remain CLOSED. [Other standing invariants:
sealed-record sha256 unchanged confirmation; token-prior slot status;
Claim C status.]

— CS Engineer, YYYY-MM-DD
```

The N enumerated sections mirror the direction memo's required-return items 1:1. CS does not add sections the direction did not ask for; CS does not skip sections the direction asked for. Each enumerated item gets exactly one §.

---

## §C. Banner conventions

Pick the banner that matches the return's disposition. Banners go inside a `text` code-fence at the top, after the title.

### VERIFIED disposition

```text
STATUS: VERIFIED — [SUBJECT] STATE-CONSISTENT AND MANAGER-READY
[Optional one-line finding note if a minor finding exists]
VERIFICATION-ONLY MEMO · AUTHORIZES NOTHING
NO MODEL · NO MODEL LOADED · NO SWEEP_ID · NO SWEEP EXECUTION
[Add any other standing carries the direction requires]
SEALED LOCK-RECORD vN UNCHANGED · [other artifact-status confirmations]
```

### HOLD disposition

```text
STATUS: HOLD — [SPECIFIC ISSUE]
HOLD UNTIL RESOLVED; SUCCESSOR EXECUTION REMAINS CLOSED
[Same standing carries as VERIFIED]
```

### FILED (delivery) disposition

```text
STATUS: [ARTIFACT] FILED — [BRIEF DESCRIPTION]
[Same standing carries]
```

If the disposition doesn't fit one of these three shapes, the return exits the template path. (See §G.)

---

## §D. Artifact / path / hash table convention

When a return enumerates artifacts (sealed-record verifications, run outputs, governance memos, etc.), use this table shape. Three columns minimum; add columns as the direction memo requires.

```markdown
| artifact | sha256 | match (run-of-record) |
|---|---|---|
| `path/relative/to/repo/root.json` | `<full sha256>` | ✓ |
```

Conventions:

- **Path column:** always relative to repo root, in backticks. Never absolute paths in a return.
- **sha256 column:** full 64-char hex. Use the truncated `…16…` form only in prose, never in the verification table.
- **Match column:** `✓` / `✗` / `(new)` / `(retained)`. One char. No prose.
- **When listing many artifacts:** group by purpose with a `### Subheader` for each group; one table per group.
- **When asserting "unchanged":** include the prior committed sha256 in the table AND state the prior-commit reference inline (e.g., "match run-of-record at commit `XXXXXXX`").

---

## §E. G1 enumeration standard

A G1 enumeration is a CS-side delivery report that asserts: **the named files exist at the named paths with the named hashes.** It is the load-bearing CS attestation that downstream verification can rely on.

Required fields per G1 row:

1. Item number (matches the direction memo's required-return list).
2. Item description (one phrase, e.g., "commit SHA verified" or "v0.3 path").
3. Value — the actual hash, path, or short confirmation that the direction memo asked for.
4. Verification basis — how CS knows this is true (e.g., `Python hashlib.sha256()` over committed bytes; `git ls-tree` at HEAD; runtime stamp from a specific file).

Format options:
- **Inline** (preferred for short G1s, ≤5 items): each item is a numbered list entry with the value inline.
- **Table** (preferred for ≥6 items): two-column `# | item | value` table, plus a Verification-Basis subsection below.

A G1 enumeration is not complete until every item asked for has a row. Partial G1s exit the template path (see §G).

---

## §F. Test-log / assertion-status convention

When a return references test results, use this exact shape:

```markdown
Test suite: `pytest <path/to/test/dir>/`
Result: **N passed** (no failures, no errors, no warnings).
[Optional: list new tests added since the prior return and their purpose.]
```

If any test fails, the return exits the template path: CS files a custom memo with the failure detail. (See §G.)

For runtime assertions (e.g., a runner's pre-flight check), use:

```markdown
Runtime check: <name> (e.g., PH5-4 pre-flight; mlx_lm version check; snapshot hash match)
Result: PASSED / REFUSED / N/A
Stdout (verbatim, if relevant): `<one-line excerpt>`
```

Don't paraphrase runtime output. If the runtime check is multi-step, list each step's status separately.

---

## §G. Exit conditions (when CS does NOT use this template)

Manager §2 principle: *"Templates speed normal cases. Anything interesting exits the template."* The following conditions force CS to file a custom narrative memo instead of using this template:

| Exit condition | Why |
|---|---|
| Disposition is HOLD with a state mismatch, claim-boundary issue, or sealed-record issue | The HOLD reason needs full narrative explanation; template banners are not enough. |
| A SEVERITY-RUBRIC finding of NAMED DEVIATION, ABORT, or SUPERSESSION | These require the deviation-disposition lifecycle pattern; template is not the right shape. |
| A finding that the direction memo's required item cannot be produced (e.g., a hash doesn't match; an artifact doesn't exist) | The "answer" is itself a custom finding; template is misleading. |
| A first-of-kind event: new abort class, new deviation category, new claim-boundary discovery, new sealed-byte question | Patterns aren't yet known; writing custom is the only honest path. |
| Any return that touches the sealed LOCK-RECORD bytes | Sealed-byte returns are inherently load-bearing; template does not communicate the weight. |
| Any return that proposes opening a successor gate | Manager-facing gate-opening proposals require the readiness-packet format, not a return template. |
| Any return where the bounded result language must be revised, qualified, or expanded | Bounded language is C5-territory; CS should not author template-form responses on that axis. |
| Direction memo explicitly says "custom narrative return" or routes through C5 | Template is wrong shape by direction. |
| Any test failure, any unauthorized work detected, any artifact mutation detected | The finding needs full narrative; template is misleading. |

When in doubt, CS files a custom memo. The cost of an over-narrated return is small; the cost of a template-shaped return on a load-bearing finding is large.

---

## §H. Forward references (placeholder until referenced artifacts land)

- **SEVERITY-RUBRIC-v1.0** (TL deliverable): the §G exit conditions reference NAMED DEVIATION / ABORT / SUPERSESSION categories that the rubric defines. Once the rubric lands, §G updates to reference it by hash.
- **VERIFICATION-PROTOCOL-v1.0** (NS deliverable): the §B return skeleton's "verification basis" footnotes reference verification steps the protocol defines. Once the protocol lands, the template's §1-§N body shape may reference protocol steps by name (e.g., "VP-3 state-invariant check").
- **CLOSEOUT-TEMPLATE-v1.0** (NS deliverable): close-out returns are NOT covered by this template (they have their own shape per CLOSEOUT-TEMPLATE). This template covers state verifications, G1 returns, filing returns, and routine hash-precondition confirmations.
- **CLAIM-RISK-CHECKLIST-v1.0** (C5 deliverable): any return that touches claim language exits this template path (§G) and goes to C5 for review per the checklist.
- **STANDING-NON-AUTHORIZATIONS.md** (existing standing doc): the §N standing carry should eventually reference this canonical list by sha256 instead of re-enumerating prohibitions verbatim each time.

---

## §I. Adoption note

Once TL filters and Manager accepts this template (via `PROCESS-ACCELERATION-ADOPTION-MEMO`), CS direction memos may say:

> Return using `STANDARD-RETURN-TEMPLATE-v1.0`.

CS responds with a return memo following §B–§F. CS exits the template per §G if any exit condition applies. No template adoption changes the substantive requirements of any return — the direction memo still defines what must be answered; the template defines only the shape of the answer.

---

— CS Engineer, 2026-06-12 (draft for TL filter)
