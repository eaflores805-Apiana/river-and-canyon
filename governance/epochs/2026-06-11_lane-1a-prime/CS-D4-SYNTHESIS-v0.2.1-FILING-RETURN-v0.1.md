# CS D4 Synthesis v0.2.1 — Filing Return (v0.1)

```text
STATUS: v0.2.1 FILED — E1, E2, E3 APPLIED EXACTLY
NO RESULT LANGUAGE CHANGED · BOUNDED INTERPRETATION PRESERVED
NO MODEL · NO SWEEP_ID · NO SWEEP EXECUTION · CLAIM C INACTIVE
ALL SUCCESSOR GATES CLOSED · SEALED LOCK-RECORD v1.0 UNCHANGED
```

To: Team Lead · Cc: New Senior Engineer, Contributor 5, Senior Engineer, Manager
From: CS Engineer
Date: 2026-06-11
Re: TL §7 10-item return — C5 wording edits E1–E3 applied to synthesis v0.2

CS has applied the three required C5 wording edits per TL direction
2026-06-11. File saved as v0.2.1 (patch-level; honest about being a
wording correction, not a substantive revision). v0.2 retained at its
locked sha256. The diff is exactly the four lines specified plus the
header note and the patch-attribution trailer.

---

## §1. Path

```text
governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-D4-SYNTHESIS-AND-NEXT-QUESTIONS-v0.2.1.md
```

v0.2 retained at:

```text
governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-D4-SYNTHESIS-AND-NEXT-QUESTIONS-v0.2.md
  sha256: 22bc922ba7c05a90f48d18ffeeff11e58de98eaab784ad980e244532b1db641a
  status: SUPERSEDED by v0.2.1 (C5 wording edits E1–E3) — retained per supersession discipline
```

## §2. Commit SHA

Recorded after this commit lands; reported in the CS delivery message.

## §3. sha256

```text
v0.2.1: 1900fc1fd24ede1121bbbdb496395fb6a5ad71e176e34dabe866e2015bcf7d6e
v0.2:   22bc922ba7c05a90f48d18ffeeff11e58de98eaab784ad980e244532b1db641a (unchanged)
```

## §4. Confirmation E1 applied

**CONFIRMED — exact.** §4 of v0.2.1 reads (relevant fragment):

> Everything beyond the easiest rung: whether **the declared elimination criteria fire across breadth** (L02–L08 ramp difficulty; L01 is the gentlest surface and a perfect score there is the *least* informative clean result the lane can produce); …

The parenthetical "L02–L08 ramp difficulty" is retained per TL §2.

## §5. Confirmation E2 applied

**CONFIRMED — exact.** §4 of v0.2.1 reads (relevant fragment):

> … whether **the declared elimination pattern replicates under transfer** (any model other than Qwen2.5-3B-Instruct bf16); …

The parenthetical "any model other than Qwen2.5-3B-Instruct bf16" is retained.

## §6. Confirmation E3 applied

**CONFIRMED — exact.** §7 Path A of v0.2.1 reads (relevant fragment):

> Prerequisites already in place: the eight-rung schedule is sealed; **the eight rung task instances are CS-confirmed buildable** inside the sealed record; the generator hash-pin requirement is documented from the D4 scope review.

The collision with the project's open constructibility question is now resolved by the explicit "task instances are buildable" language.

## §7. Confirmation: no result language changed

**CONFIRMED.** §2 of v0.2.1 is byte-identical to §2 of v0.2. The accepted bounded result language is preserved verbatim:

> The instrument did not attach any elimination label under the active six-criterion set.
> Accepted bounded interpretation: the result was not explained by the declared shortcut battery or by the candidate's own measured token prior.
> This is the strongest permitted interpretation. It may not be strengthened.

## §8. Confirmation: bounded interpretation preserved

**CONFIRMED.** The strongest-permitted-interpretation clause is intact. The forbidden phrasings list in §4 is intact. The OC1–OC5 register in §8 is intact. The funder-language guard in §9 is intact. The repetition guard in §5 is intact.

## §9. Confirmation: no successor execution occurred

**CONFIRMED.** This was a wording-edit pass. No runner invoked. No model loaded. No inference run. No artifact under `experiments/2026-06-11_lane-1a-prime/d4_*_pilot/` modified.

## §10. Confirmation: all successor gates remain closed

**CONFIRMED.** All successor gates from the standing list remain CLOSED: successor D4 execution; L02–L08 execution; additional token-prior generations; scrambled-binding generations; quantization stress; INT8 / INT4; candidate selection; ranking; threshold work; certification evaluation; stress-retention testing; Claim C activation; public benchmark packaging; funder-facing release; SBIR submission.

**Sealed LOCK-RECORD v1.0** sha256 `51e18fa9…` — UNCHANGED. **D4 token-prior authorization slot** — remains UNOPENED for any further use. **Claim C** — INACTIVE.

---

## §11. Diff verification (for the reviewer's convenience)

Five total changes from v0.2 to v0.2.1:

1. Title: `(v0.2)` → `(v0.2.1)`
2. New header line: italic patch-attribution paragraph (top of file)
3. §4 E1 wording (one line)
4. §4 E2 wording (one line)
5. §7 Path A E3 wording (one line)
6. Trailer: CS patch-attribution sign-off line

No other content differs. (Verified by `difflib.unified_diff` at filing time.)

## §12. Standing carry (non-authorizations, verbatim)

This filing return does not authorize: successor D4 execution; L02–L08 execution; additional token-prior generations; scrambled-binding generations; quantization stress; INT8 / INT4; candidate selection; ranking; threshold work; certification evaluation; stress-retention testing; Claim C activation; public benchmark packaging; funder-facing release; SBIR submission.

— CS Engineer, 2026-06-11
