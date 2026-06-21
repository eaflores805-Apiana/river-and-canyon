# CS Acknowledgment — First Bounded Compression Rung Direction

**Date:** 2026-06-21
**From:** CS Engineer
**To:** Manager, Team Lead; Cc: Senior Engineer, C5
**Re:** Manager Direction 2026-06-21 — "Open First Bounded Compression Rung"
**Status:** **ACKNOWLEDGED. Standing by for Senior draft of the authorization packet.**

---

## Acknowledgment

Manager direction received and filed byte-faithful at:

```text
governance/2026-06-21_first-compression-rung-direction/
  MANAGER-DIRECTION-OPEN-FIRST-BOUNDED-COMPRESSION-RUNG-2026-06-21.md
```

CS reads the direction as:

```text
- Authorize PREPARATION of FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.1.
- Do NOT authorize a run.
- Narrowly lift the "no INT8" block for the authorization-packet authoring
  scope; the actual INT8 run remains separately gated on the full chain
  (Senior draft → C5 claim-risk → CS feasibility → TL synthesis →
   Manager by-name run authorization).
- "No INT4" stays in place.
- "No composition / seam / Claim C claim" stays.
- "No M5 distractor-attractiveness experiment" stays.
- "No V3 composite-gate retry" stays.
- "No construction redesign" stays.
- Path A FP16 K=5 FAIL stays closed.
- Existing fail-closed gate semantics apply: if FP16 baseline is not
  qualified, the run must fail closed before INT8 interpretation.
```

## Program-state note (carry-up for transparency)

The standing card has carried `No compression / INT8 / INT4` as a blanket
block throughout the Path A / V3 lifecycle. This Manager direction
narrowly lifts that block for the **first INT8 rung as instrument-
validation-under-stress**, on a single qualified target, with the
existing fail-closed gates intact.

CS reads this as:

```text
- compression block: narrowly LIFTED for INT8 instrument-validation
  on the qualified target, packet-authoring scope only (the run itself
  still requires Manager by-name authorization)
- INT4: still BLOCKED
- composition / seam / Claim C / capability / mechanism claims:
  still BLOCKED
- M5 distractor-attractiveness experiment: still BLOCKED
- V3 composite-gate retry: still BLOCKED
- construction redesign: still BLOCKED
- Path A FP16 K=5 FAIL: stays closed
- the bounded interpretation perimeter: "Can the fail-closed instrument
  produce a valid FP16-to-INT8 stress-retention readout on the selected
  qualified target?" — and nothing else
```

This is a material program-state change and CS notes it explicitly for
the audit trail. If CS has misread the scope (e.g., the block-lift is
narrower than CS infers, or the INT4 boundary applies differently than
read), please correct.

## CS posture going forward

```text
- CS will NOT draft FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.1.
  Authoring the packet is Senior's lane per the standing routing
  (Senior drafts; SE locks nothing; routes for C5 + CS + TL + Manager).
- CS WILL stand by to:
    * Inbox-sweep when Senior drops the packet
    * File the packet byte-faithful to path-a/in-review/
       (or wherever Senior's cover note directs)
    * Run the standard CS feasibility / provenance review on the packet
       (target attestation, baseline-gate status, scorer/validator hash
        recompute, paths reachable, fail-closed branches checked)
    * Hold against the narrowed forbidden-interpretations list above
- CS WILL NOT execute the run, materialize fresh items for execution,
  render prompts for execution, load any quantization tooling, or touch
  INT8 inference until a separate Manager by-name run-authorization
  memo lands.
```

## Qualifying-target candidate (for Senior's awareness; CS does not pre-decide)

```text
Paper 2 v1.2 §6 + §9 name single-hop retrieval (hop2) as the one query
type that clears the FP16 gate ("the natural first candidate for any
future stress run, but no compression rung has been run on this
construction"). §9 explicitly notes: "the first such rung should be
framed as instrument-validation-under-stress on a constructible
single-lookup task, not as composition or seam evidence."

Paper 2 v1.2 §6 also bounds this carefully: "hop2's status rests on
near-ceiling FP16 accuracy together with the fact that the multi-hop
position/endpoint contamination of §4.3 does not apply to a single
B→C lookup — not on a separate hop2-specific shortcut probe. By the
same accuracy-is-not-constructibility logic this paper argues,
certifying hop2's own shortcut-freeness is a precondition for any
future stress rung on it (§9), and we do not pre-suppose it here."

So the Senior packet will need to either:
  (a) Argue why hop2 is already qualified enough for instrument-
       validation-under-stress (vs. capability-under-stress),
       leveraging the §6 / §9 distinction;
  OR
  (b) Specify a hop2-specific shortcut/position probe as a precondition
       step before INT8;
  OR
  (c) Pick a different qualified target if one exists ("already-prepared,
       smoke-tested target" in the Manager direction suggests one is in
       hand — Senior to identify).

CS does not adjudicate this; flagging for Senior's awareness while
drafting.
```

## Tooling / provenance posture (pre-emptive notes for the packet review)

```text
Anticipated CS feasibility-review checks (when the packet arrives):

  1. target identity + path + sha256
  2. FP16 baseline-gate status from the locked record (cross-check
     against locked artifact hashes; the v1.2 Appendix B addendum
     digests are stable on origin/main from the v1.2 release commit
     34ef9215)
  3. INT8 quantization tooling: specify quantization library/version
     (mlx_lm K-quant? bitsandbytes? AWQ? GPTQ? Other?); CS will need
     deterministic hashes for the quantization step itself
  4. scorer + validator hashes (almost certainly already-locked
     V3 tooling for V3-derived targets, or original cell scorers for
     Cell01-03-derived targets); CS will recompute from bytes
  5. pass / fail / uninterpretable branches: ensure each branch is
     mechanically decidable; ensure "uninterpretable" exists as a
     first-class branch (so a borderline result doesn't get promoted)
  6. forbidden-interpretations list: ensure it forecloses Claim C,
     composition, seam, capability, mechanism, M5-resolution, V3-
     reopening, INT4 promotion, etc.
  7. stop conditions: ensure pre-stated; no post-hoc threshold tuning
  8. artifact / provenance requirements: ensure CS recompute path
     exists for all hashes the packet asserts

If the packet is missing any of the above, CS will return HOLD with a
specific gap list; no PASS without all items.
```

## Boundaries held (verbatim, narrowed-as-stated)

```text
- no run begins from this direction alone                                          held
- no INT4                                                                          held
- no composition / seam / Claim C claim                                            held
- no M5 distractor-attractiveness experiment                                       held
- no V3 composite-gate retry                                                       held
- no construction redesign                                                         held
- Path A FP16 K=5 FAIL                                                             stays closed
- Paper 2 v1.0 tag (paper2-cells01-03-v1.0; 41c033fc59597eb42015de9019c3ac7b7d19dd98)   preserved
- Paper 2 v1.2 tag (paper2-cells01-03-v1.2; 34ef9215e8706f5a18288274be27678593dd2c01)   preserved
- v1.2 PDF on trunk at sha256 16b9538647…                                          carried (from the v1.2 PDF follow-on commit)
- v1.2 RC locked at in-review/PAPER-2-RELEASE-CANDIDATE-v1.2.md (5b385d7f…)        preserved
- notes/CLAIM-LEDGER-v1.0.md (15f32e1a…)                                           UNCHANGED
- tier0-run/CLAIM-LEDGER-CONSTRUCTIBILITY-FLOOR.md (b1687559…)                     UNCHANGED (sealed)
```

CS authored zero claim language in this acknowledgment. The "qualifying-
target candidate" section above is informational reading of the v1.2
manuscript Senior already wrote — no new claim is introduced by CS.

---

— CS Engineer, 2026-06-21
