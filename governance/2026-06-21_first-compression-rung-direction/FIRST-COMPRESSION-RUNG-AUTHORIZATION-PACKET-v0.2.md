# FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.2 (DRAFT)

**From:** Senior Engineer (drafted; model-free; no run performed) → **Route:** Team Lead → C5 → **Manager (run authorization)**
**Status:** authorization packet for review. **No run begins from this packet.** SE prepares and verifies; SE does not authorize or execute. Execution, if authorized, is CS's on the real machine.
**Direction:** Manager — "Open the first compression rung as instrument-validation-under-stress."

> **The one question this rung may answer:** *Can the fail-closed instrument produce a valid FP16→INT8 stress-retention readout on the selected readout-eligible target (hop2)?* It may **not** answer whether compression damages composition, whether the seam exists, whether Claim C is supported, whether V3 is fixed, or whether M5 is resolved.

---

## v0.1 → v0.2 (this revision)

Revised per TL HOLD:
1. **Bounded the "qualified" language.** "shortcut-clean qualified capability," "qualified capability," and "qualified stress target" replaced with bounded wording — hop2 is *eligible for the narrow hop2-only FP16→INT8 readout under the existing baseline gate*, not certified as a general stress target.
2. **Added the explicit non-certification statement** (§2): "This does not certify hop2 as shortcut-free in general. It only permits a bounded FP16→INT8 readout on the locked n=8 target under the declared checks."
3. **Split the Manager decision into A / B / C** (§11), with adoption (A) and fresh-run (B) as **separate authorization types** — A is a provenance-review-gated adoption of existing bytes (no model run); B is a fresh run authorization.
4. **Added a C5 watchpoint** on whether "qualified/eligible" stays bounded and does not imply shortcut-freeness, robustness under quantization, or Claim-C suitability.

Unchanged (restated): no INT4; no composition / seam / Claim C claim; no M5 experiment; no V3 retry; no construction redesign; fail-closed treatment of hop1 and composite; the null-stress caveat.

---

## 0. The finding that shapes this packet (read first)

A minimal FP16/INT8 comparison on this exact target **already exists** — `experiments/2026-06-15_minimal-fp16-int8-twohop-l1/` — and its bytes decide the design:

```text
FP16 (n=8, greedy, max_tokens 16):   hop1 0/8 · hop2 8/8 · composite 1/8
INT8 (same):                          hop1 0/8 · hop2 8/8 · composite 1/8
byte-identity FP16 vs INT8:           IDENTICAL — 24/24 generations, match_rate 1.0
prior disposition:                    baseline_gate FAIL (hop1 component 0/8 < 0.5);
                                      compression_observation SAME_ERROR_IDENTITY;
                                      retention_compression_verdict INCONCLUSIVE
```

Two consequences, both load-bearing:

1. **Only one query type is eligible for a bounded readout.** hop2 (single-hop retrieval of the second relation, given the intermediate) is **8/8 at FP16** — it clears the baseline floor, which makes it *eligible for a narrow hop2-only FP16→INT8 readout under the existing baseline gate*, not certified as a general stress target. hop1 (first-hop component, 0/8) and composite (1/8) do **not** clear the gate; the gate fails closed on them. So the *only* target on which a valid retention readout can be produced is **hop2**.
2. **INT8 applies effectively null stress at this scale.** FP16 and INT8 produced byte-identical outputs across all 24 generations. So a fresh INT8 rung will almost certainly reproduce full retention on hop2 (8/8 → 8/8) **because INT8 does not perturb the model here**, not because the capability is "robust." This rung therefore validates the instrument's *mechanics* (can it produce a valid readout on the readout-eligible target), **not** retention decay. A readout of "full retention" here means "INT8 was too gentle to stress anything," and nothing more.

This is surfaced up front so the authorization decision is made knowing the likely outcome: **instrument-validation = achievable; retention-decay demonstration = not achievable with INT8 at 3B.** A meaningful decay test would need a harsher rung (INT4), which is **explicitly out of scope** here.

---

## 1. Target task / item set

`experiments/2026-06-15_minimal-fp16-int8-twohop-l1/` — Two-Hop L1 matched-pair set, **n = 8**, greedy (temp 0.0, max_tokens 16). Query types scored per item: **hop1** (first-hop component), **hop2** (second-hop single-hop retrieval given the intermediate), **composite** (the full two-hop chain). Items file `sha256:7d5099cb…`, prompt template `sha256:c8a81a29…`.

**Selected readout-eligible target for the valid-readout question: `hop2` only** (eligible for the bounded hop2-only readout under the existing baseline gate; not certified as a general stress target). hop1 and composite are carried for the baseline gate and fail-closed accounting, not as readout targets.

## 2. Why hop2 is eligible for this bounded readout — and what that does NOT certify

```text
hop2 (single-hop retrieval): FP16 8/8 — clears the baseline floor; no format_fail, no anchor_echo,
                             no non_context, no stopped_short. This is the program's one ceiling-level,
                             clears the floor for the bounded hop2-only readout (consistent with V3 hop2 576/576) — eligible under the declared checks, not certified shortcut-free in general.
hop1 (component):            FP16 0/8 — NOT qualified (the program's central finding: first hop is not
                             constructible on this family).
composite (full chain):      FP16 1/8 — NOT qualified; gated out by the unmet hop1 precondition.
```

Eligibility here is deliberately narrow: hop2 is a **single-hop** retrieval, not a composition. It is eligible for the bounded hop2-only readout precisely because it is *not* the composite — it carries no unmet component precondition. Choosing hop2 is the disciplined consequence of the baseline gate, not a workaround of it.

**This does not certify hop2 as shortcut-free in general. It only permits a bounded FP16→INT8 readout on the locked n=8 target under the declared checks.** Eligibility is scoped to this run, this n=8 set, this gate — it is not robustness under quantization, not shortcut-freeness in general, and not suitability for Claim C.

## 3. FP16 baseline gate status (evaluated FIRST, before any INT8 is read)

Per the existing pre-registration §6 (FP16-BASELINE GATE evaluated first; pre-declared so it cannot be skipped after INT8 is seen):

```text
hop2:       PASS  — eligible (8/8, clears floor; FP16 raw outputs inspected for the Claim-B
                    position/anchor shortcut; hop2 is single-hop retrieval, not a chain, so the
                    composite shortcut signature does not apply).
hop1:       FAIL  — 0/8, below the 0.5 component-competence threshold.
composite:  FAIL  — 1/8; chain-following not established (prior disposition: same_token_across_queries).
```

**Fail-closed rule (binding):** if, on the run's FP16 outputs, hop2 does **not** clear the floor (e.g., a fresh draw degrades it) or its correctness is shown shortcut-aligned on inspection, the run **fails closed at the gate** and **no INT8 interpretation is produced** for any query type. The composite and hop1 are *already* gate-failures and remain fail-closed regardless of INT8.

## 4. INT8 stress plan

Run FP16 and INT8 on the same n=8 items, greedy, max_tokens 16, via the byte-locked scorer. Evaluate the FP16 baseline gate first (§3). If hop2 passes the gate, produce the **hop2 FP16→INT8 retention readout** (the permitted output). hop1 and composite remain fail-closed (no retention claim). Record raw outputs (E3 retained) and the FP16-vs-INT8 byte-identity check.

## 5. Exact model / quantization profile

```text
FP16 baseline:  Qwen/Qwen2.5-3B-Instruct, locked revision aa8e72537993ba99e69dfaafa59ed015b17504d1
                (HF cache), FP16, greedy (temp 0.0, max_tokens 16).
INT8 stress:    tier0-run/Qwen2.5-3B-Instruct-mlx-int8  (MLX INT8 quantization of the same revision),
                mlx_lm 0.31.3, greedy (temp 0.0, max_tokens 16).
Decode:         identical decode params across both arms (the only declared difference is the weight
                quantization). n = 8 matched items.
```

## 6. Scorer and validator hashes (to be re-verified at run time)

```text
scorer_twohop_l1.py        sha256: b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde
smoke_test_twohop_l1.py    sha256: 58749ca88ab69e0fc6cf34cfb3417ee57f42c1ebe13c5c7cfd384726182c3989
prompt_template            sha256: c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
items_file                 sha256: 7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1
existing PREREGISTRATION    sha256: 3fb4dbd4d8daf19be31e95a395abe65175c5968cd3f1b6d50ac08e0bfd4bed03
```

The scorer is the byte-locked Cell03 scorer (`b65c6803`). Any change to scorer, prompt, or items voids the gate and requires re-lock before authorization.

## 7. Pass / fail / uninterpretable branches (instrument-validation framing)

```text
PASS (instrument validated on the readout-eligible target):
   FP16 hop2 clears the baseline gate (§3), AND the INT8 hop2 readout is produced, AND all validity
   guards hold (format, prompt-conformance, decode determinism). The instrument has produced a VALID
   FP16→INT8 retention readout on the readout-eligible target. The readout VALUE (likely full retention given
   the prior byte-identity) is reported as-is, with the §0 null-stress caveat attached.

FAIL-CLOSED (instrument correctly withholds):
   FP16 hop2 does not clear the gate, OR a validity guard trips before INT8 is interpretable, OR the
   gate machinery fails to withhold on the unqualified hop1/composite. No INT8 retention claim is made.
   (Note: hop1 and composite are already fail-closed; this is the expected, correct behavior, and it is
   itself evidence the instrument fails closed under stress.)

UNINTERPRETABLE:
   A readout is produced but a declared validity guard is ambiguous (e.g., partial decode, near-floor
   hop2 on a fresh draw, byte-identity check inconclusive). Withhold and report the ambiguity; do not
   force a verdict.
```

## 8. Forbidden interpretations (binding on any writeup)

```text
A valid hop2 readout — including full retention — does NOT support, and may not be written as:
  - "compression is lossless / preserves capability" (general)         - Claim C progress
  - "INT4 would behave the same" (extrapolation across bit-depth)       - Paper B activation
  - "composition is preserved under compression"                        - "the seam does not exist"
  - "the model is robust to quantization"                               - "V3 is fixed" / "M5 resolved"
  - "the baseline / task family is certified or viable"                 - capability / mechanism claim
  - "the model passed" / product- or funder-facing result
Null-stress (FP16≡INT8 byte-identity) says nothing about any harsher compression. The readout speaks
ONLY to: the instrument produced a valid FP16→INT8 readout on a single readout-eligible single-hop target,
at 3B, on n=8, under INT8-MLX, once.
```

## 9. Artifact and provenance requirements

```text
- Locked model revision + INT8 path recorded; mlx_lm version; node/platform manifest.
- FP16 + INT8 raw outputs retained (E3); FP16 + INT8 scored counts; per-item table.
- FP16-vs-INT8 byte-identity check recorded (match rate, diff examples).
- scorer / prompt / items / pre-reg sha256 re-verified at run time and recorded in a MANIFEST.json.
- Disposition JSON with the pre-declared verdict keys; expected-match check.
- All under experiments/<date>_first-compression-rung/ ; sha256 manifest; nothing overwrites sealed bytes.
```

## 10. Stop conditions

```text
- Baseline gate fails (hop2 does not clear the floor on the run's FP16 outputs) -> STOP, fail closed, no INT8 readout.
- Any scorer/prompt/items/pre-reg hash mismatch at run time           -> STOP, re-lock required.
- Validity guard trips (decode nondeterminism, format collapse)       -> STOP, mark uninterpretable.
- Any attempt to read INT8 on hop1/composite as a retention result    -> STOP (those are fail-closed).
- Scope creep toward INT4 / composite / seam / Claim C / V3 / M5      -> STOP (out of scope).
```

---

## 11. Manager decision options (separated — adoption is NOT a run authorization)

These are distinct authorizations and must not be bundled. **No run is authorized by this packet.**

**Option A — Adopt the existing 2026-06-15 result (adoption authorization; no model run).**
Adopt the existing `2026-06-15_minimal-fp16-int8-twohop-l1` hop2 FP16→INT8 result as the instrument-validation readout, **conditional on a CS provenance review** confirming the existing run artifacts meet this packet's artifact requirements (§9): pre-reg `3fb4dbd4`, scorer `b65c6803`, items `7d5099cb`, prompt `c8a81a29`, FP16+INT8 raw/scored retained, byte-identity recorded. This authorizes *adoption of existing bytes after provenance review* — no model is run. Likely readout: hop2 full retention, null stress.

**Option B — Authorize a fresh hop2-only rung (run authorization).**
Authorize CS to execute a fresh FP16→INT8 rung on the locked n=8 target, hop2-only readout, per §3–§10, on the real machine. This authorizes *a new run*. Likely outcome: full retention with null stress (INT8 byte-identical at 3B). Buys clean provenance, not new information.

**Option C — Hold.** Do neither now.

**Adoption (A) and fresh-run (B) are separate authorization types.** A is a provenance-review-gated adoption of existing bytes (CS reviews; no model runs). B is a run authorization (CS runs the model). Authorizing A does **not** authorize B, and authorizing B does **not** authorize A. The Manager may choose A, B, or C.

## C5 watchpoint

C5 should specifically review whether this packet's use of "qualified"/"eligible" stays **bounded to the narrow hop2 readout** and does **not** imply hop2 is certified shortcut-free, robust under quantization, or suitable for Claim C. The binding statement is in §2: eligibility is scoped to this run, this n=8 set, this gate — it is not a general capability claim. The fail-closed treatment of hop1 and composite, and the null-stress caveat, must remain intact.

---

## Boundary

```text
This packet PREPARES a run-authorization decision. No run begins from this packet or the Manager's
direction alone — execution requires the Manager's explicit "authorize run," and is CS's to perform on
the real machine. SE drafted this; SE authorizes nothing, runs nothing, and seals/moves no bytes.

Scope locks (inherited + restated): NO INT4. NO composition / seam / Claim C claim. NO M5
distractor-attractiveness experiment. NO V3 composite-gate retry. NO construction redesign. If the
baseline is not qualified, the run fails closed before any INT8 interpretation. The Path A FP16 K=5
FAIL remains closed; the tier0-run remains sealed.
```

## The one to carry up

The honest shape of this first rung: the **only readout-eligible target is hop2** (single-hop retrieval, 8/8 FP16), so that is the one place a valid FP16→INT8 readout can be produced — and the prior 2026-06-15 bytes show **INT8 is byte-identical to FP16 at this scale**, so the readout will almost certainly be *full retention with null stress*. That **validates the instrument** (it can produce a valid readout on the readout-eligible target and fails closed on the unqualified composite/hop1) but **demonstrates no retention decay** — INT8 simply does not perturb a 3B model on this task. So the decision splits cleanly (see §11): **adopt** the existing 2026-06-15 hop2 result as the instrument-validation readout (subject to CS provenance review), **authorize a fresh** hop2-only rung for clean provenance (likely null stress), or **hold**. The strategic point stands: a *meaningful* stress-retention test — one where the instrument could actually show decay — needs a harsher rung than INT8, which this direction explicitly forecloses. Either way the instrument-validation question can be answered; the compression-effect question cannot, and must not be written as if it could.

— Senior Engineer (first compression rung authorization packet v0.1; for TL → C5 → Manager)
