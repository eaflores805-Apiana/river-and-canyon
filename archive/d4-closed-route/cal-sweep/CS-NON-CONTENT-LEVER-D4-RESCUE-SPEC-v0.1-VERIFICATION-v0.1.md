# CS Verification — Non-Content-Lever D4 Rescue Spec (CAL-Q)

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** FILED — **PASS at design level; one construction-time flag on §9 single-difference feasibility**
**In response to:** Manager direction 2026-06-13 — "One Final Non-Content-Lever Attempt Before D4 Pivot" (CS instructions: verify spec for model-free, no-run-auth, single-difference feasibility, query-side-only changes, content load unchanged, defective answerability not increased).
**Artifact verified:** `NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1.md` (sha256 `d0bb0217a4e4de17f73faca30f0dfc037b25e52a6585a243e85c310f6cdc519f`)

---

## §1. Identity + pre-flight

| Field | Value |
|---|---|
| HEAD at verification | (this commit) |
| Spec path | `governance/2026-06-11_lane-1a-prime/certification-readiness/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1.md` |
| Spec sha256 | `d0bb0217a4e4de17f73faca30f0dfc037b25e52a6585a243e85c310f6cdc519f` |
| Author | Senior Engineer |
| Spec self-anchor | `origin/main HEAD 8a64010` (CAL-E run commit; spec was drafted before re-score) |
| Companion Senior interpretations also filed this turn | `CAL-E-INTERPRETATION-v0.1.md` (`4cafaedb…`), `CAL-E-DEFECTIVE-ERROR-ANALYSIS-v0.1.md` (`fc5569da…`), `CAL-ABCE-RESCORE-REINTERPRETATION-v0.1.md` (`8433e32f…`) |

## §2. Manager's CS verification checklist — line-by-line

| Manager-listed check | Result | Evidence |
|---|---|---|
| (a) spec remains model-free | **PASS** | §1 "specifies; runs nothing; requests nothing"; §13 closed gates verbatim; no mlx_lm/model-load language |
| (b) no run-authorization language slipped in | **PASS** | Grep for `authorize|approve|sanction|permit` near `execution/run/model-facing/sweep`: zero violations. The 2 matches are: (i) spec's own header citing Manager's prior model-free authorization, (ii) §header naming Manager's role for any later run authorization. Both are appropriate references, not authorizations. |
| (c) single-difference feasibility | **PASS at spec level, with construction-time flag — see §3 below** | §9 has the load-bearing CRITICAL CHECK that "the indirect description must pick out the same key IDENTITY in both members." Drop-if-violated gate explicit. |
| (d) lever changes only query-side difficulty | **PASS** | §4 explicitly holds CAL-B baseline content constant: list_len 13, slots 8–11, near-miss 2, vocabulary, values — all IDENTICAL. Only the query form changes (direct → indirect). |
| (e) content load / decoy material unchanged | **PASS** | §4 "list content / vocabulary / values: IDENTICAL — no new decoy material." §6 reiterates: "same list content as CAL-B's low-defective (0.05) baseline, no added decoy." |
| (f) defective answerability not increased by construction | **PASS at spec level** | §6 is the load-bearing argument: same content as the low-defective baseline; indirect step (if anything) makes false-answering HARDER (model must mis-resolve AND grab a decoy); DESIGN REJECTION CLAUSE if the indirect form adds answerability. §11 PIVOT branch fires if defective inflates. |

## §3. Construction-time flag on §9 single-difference feasibility

The spec is well-designed at the specification level. But the §9 critical check ("the indirect description must pick out the same key IDENTITY in both members") is non-trivial to satisfy depending on which class of indirect query is chosen at construction. CS flags this for the gated construction step, not as a failure of the spec.

**Concrete decomposition by indirect-query class:**

| Indirect-query class | Example | Resolution depends on... | Single-difference? |
|---|---|---|---|
| **List-content-dependent** (relational) | "key that comes immediately after key J" | the LIST contents (which key is adjacent to J) | **Risk of second difference.** In clean, J is adjacent to queried-key K. In defective, K is absent → some OTHER key is adjacent to J → the description resolves to a different identity in defective. The two members' lists differ on what's adjacent to J. |
| **List-content-dependent** (extrema) | "alphabetically-last key" / "key with longest value" | the LIST contents (ordering / value sets) | **Risk of second difference.** The "last" / "longest" key may be the queried-key in clean and a different key (the replacement) in defective. Resolution differs. |
| **List-content-INDEPENDENT** (arithmetic / external) | "value for key (138 + 7)" → resolves to integer 145 regardless of list | a property INDEPENDENT of the list (an arithmetic constant) | **Preserves single-difference cleanly.** Description resolves to the same integer key identity in both members. In clean it's present → model returns the value; in defective it's absent → model should abstain. |

The spec's §4 example list ("comes immediately after key J", "alphabetically-last key", "value-side constraint") leans toward list-content-dependent forms. If the construction step picks one of those forms, the §9 CRITICAL CHECK is likely to fail mechanically (the resolved key identity will differ across members because the lists differ on the queried-slot key by design).

The arithmetic / external-reference form (e.g., "value for key X+Y" where X and Y are constants such that X+Y equals the queried-key as an integer) resolves to the same integer key identity in both members without depending on list content — and is consistent with the spec's intent of changing ONLY the query side.

**CS recommendation (not interpretation; a construction guardrail):** when CAL-Q is materialized at the gated construction step (after Manager authorizes a run), the construct spec's semantic-read should explicitly confirm:

- The chosen indirect-query class has list-content-INDEPENDENT resolution
- The same indirect description, applied to both members' lists, resolves to the same integer key identity (present in clean, absent in defective)
- The §9 CRITICAL CHECK passes mechanically by construction, not by hope

If the construction step cannot find a list-content-independent form that pressures clean difficulty, CAL-Q is DROPPED per the spec's own gate (same as CAL-D). That is the spec's correct behavior; CS just flags the dependency for awareness.

## §4. Companion Senior artifacts also filed this turn (CS notes them; does NOT interpret)

| Artifact | sha256 | Senior's role |
|---|---|---|
| `CAL-E-INTERPRETATION-v0.1.md` | `4cafaedb7e96b799c1608127f25e2bdff37a0bcc9c972d0849b625364cd400cf` | Senior accepted CAL-E falsified the length+depth hypothesis at the CAL-E commit |
| `CAL-E-DEFECTIVE-ERROR-ANALYSIS-v0.1.md` | `fc5569da1fcb3b9251da7011c37469a86f460cad504c847ff849abf545fd1623` | Senior's classification per Manager's pause direction; identifies format-shift artifact |
| `CAL-ABCE-RESCORE-REINTERPRETATION-v0.1.md` | `8433e32f5f56d390d2ff35262dab7a579889bf0de54203e68b512021d5d72e06` | Senior's reinterpretation under CS's NULL-normalized re-score (commit `3b2c1b0…`); confirms abstention concept flat at ~0.90 across A/B/C/E |
| `PROGRAM-POSITION-v0.1.md` | `77c300fe221808f05893cb9c7fce6da21dd75977ff97942b040099dbce5a5a83` (was `2a7fb7df…`) | In-place living-tracker update reflecting current PIVOT WATCH state and CAL-Q delivery |

CS notes the rescue spec was drafted BEFORE Senior's rescore reinterpretation (spec anchors to `8a64010`; rescore happened at `3b2c1b0`; reinterpretation at `8433e32f` notes the rescore changed the picture). Senior may want to revisit whether CAL-Q is still the right next step given the corrected scores (concept-level abstention flat at ~0.90, true false-emission flat at ~0.10 across CAL-A/B/C/E) — but that revisit is Senior's call, not CS's.

## §5. Disposition

**PASS at design level.** All 6 of Manager's CS verification checks are satisfied at the specification level:
- Model-free ✓
- No run-authorization language ✓
- Single-difference feasibility ✓ (with construction-time flag in §3 about indirect-query class selection)
- Query-side only difficulty ✓
- Content load / decoy material unchanged ✓
- Defective answerability not increased by construction ✓

CS does **not** decide:
- Whether to authorize the CAL-Q run (Manager's call)
- Whether CAL-Q is still the right next step given the rescore reinterpretation (Senior's call)
- Whether RESCUE STILL JUSTIFIED / RESCUE MUST BE REDESIGNED / PIVOT WATCH CONFIRMED / SCORER AUDIT REQUIRED (Senior's call per Manager's required output categories)

CS flags one construction-time dependency (§3) so that when/if Manager authorizes a CAL-Q run, the construction step picks a list-content-independent indirect-query form to ensure §9 single-difference holds mechanically by construction.

## §6. Sealed bytes + language perimeter

All sealed bytes UNCHANGED (≈57th survival check). No model run. No certification. No compression. No Claim C. The 12-item closed-gate list (§13 of the rescue spec) preserved verbatim.

— CS Engineer, 2026-06-13
