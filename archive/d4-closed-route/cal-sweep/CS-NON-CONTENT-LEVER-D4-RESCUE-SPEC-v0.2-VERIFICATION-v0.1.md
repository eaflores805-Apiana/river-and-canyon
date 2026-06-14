# CS Verification — Non-Content-Lever D4 Rescue Spec v0.2 (CAL-Q)

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** **HOLD** — one specific blocker on Manager check #8 (closed-world / no latent vocabulary clueing); recommended fix below
**Authorization:** Manager 2026-06-13 — "CS Verify CAL-Q v0.2 Design Spec" (model-free verification; NO execution)
**Artifact verified:** `NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.2.md` (sha256 `d88cfef937f7724cb1c1588bb08032181114ae5f999c0fadbf969cf378783630`)

---

## §1. Identity + supersession

| Field | Value |
|---|---|
| Path | `governance/2026-06-11_lane-1a-prime/certification-readiness/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.2.md` |
| sha256 | `d88cfef937f7724cb1c1588bb08032181114ae5f999c0fadbf969cf378783630` |
| Author | Senior Engineer |
| Self-anchor | `origin/main HEAD 3b2c1b0` (the NULL-normalized rescore commit) — **correct anchor** |
| v0.1 status | `d0bb0217a4e4de17…` — explicitly cited as superseded in v0.2 header; **v0.1 retained**, not overwritten (its file remains in the certification-readiness dir alongside v0.2) |

## §2. Manager's 14-item checklist — line-by-line

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Path / commit / sha256 recorded | **PASS** | This memo + INDEX |
| 2 | INDEX row updated | **PASS** | In this same commit |
| 3 | v0.1 retained, marked superseded, not overwritten | **PASS** | v0.2 header: "Supersedes v0.1 (d0bb0217), which is retained and marked superseded." v0.1 file still on disk at `certification-readiness/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.1.md` (sha256 unchanged) |
| 4 | Spec anchored to corrected re-score | **PASS** | v0.2 anchors to HEAD `3b2c1b0` (the rescore); §1 + §2 reproduce the corrected anchor facts (defective concept abstention ~0.90 stable; true false-emission ~0.10 stable) |
| 5 | Live blocker = clean saturation, not defective inflation | **PASS** | §3 D4-status statement: "D4 is NOT in PIVOT WATCH on defective discrimination." §4 explicit: "The live blocker: clean saturation." |
| 6 | Content held at CAL-B settings (list 13, slots 8–11, near-miss 2, same values/decoy) | **PASS** | §5 explicit: "built on CAL-B's content (len 13, slots 8–11, near-miss 2)... identical list values; no new near-miss values" |
| 7 | Only query form changes (direct → indirect-key) | **PASS** | §5: "ONLY the QUERY FORM changes (direct → indirect)" |
| **8** | **Strictly closed-world: no synonyms, no antonyms, no world facts, no riddles, no latent vocabulary clueing, all facts needed to resolve the key are in the prompt** | **HOLD** | See §3 below |
| 9 | Indirect query resolves to same key identity in both members | **PASS at spec level** (CRITICAL CHECK in §10 enforces this) | §5 closed-world clause + §10 CRITICAL CHECK |
| 10 | Single-difference invariant preserved | **PASS at spec level** | §10 explicit + drop-if-violated gate |
| 11 | Four-way defective reporting preserved (strict NONE / concept / true false-emit / format artifact) | **PASS** | §9 explicit, all four named, "concept-level scorer is authoritative; strict and the format split are reported alongside for transparency" |
| 12 | Decision rule pre-declared (BAND PLAUSIBLE / NEEDS REPAIR / PIVOT) | **PASS** | §12 explicit, all three branches defined; "Rule fixed now, before any run." |
| 13 | If later run, calibration-only | **PASS** | §14 explicit: "CALIBRATION-ONLY... no quantization, no stress arm, no certification, no compression" |
| 14 | No certification / compression / INT8/INT4 / ranking / Claim C language slipped in | **PASS** | §15 closed-gate list verbatim (12 items); grep for forbidden authorization phrasings: zero violations. The matches for "authorize" are all citing prior Manager direction or naming Manager's role for any later run — not slipped authorizations. |

## §3. The HOLD — Manager check #8 (closed-world / no latent vocabulary clueing)

Manager's check #8 is the strictest in the list: *"no synonyms, no antonyms, no world facts, no riddles, no latent vocabulary clueing, all facts needed to resolve the key are in the prompt."*

The v0.2 spec's §5 example indirect-query forms violate this constraint:

| Example form (verbatim from §5) | Problem |
|---|---|
| `"what is the value for the key immediately after key J?"` | Resolution requires the model to know what "after" means (list-position ordering or numeric ordering). The ordering operation itself is latent vocabulary / language modeling, not a fact stated in the prompt. Also: in defective, the queried-key is replaced, so what comes "immediately after J" is a DIFFERENT key (the replacement), which causes the description to resolve to a DIFFERENT key identity in defective → violates §10 CRITICAL CHECK by construction. |
| `"what is the value for the alphabetically-last key?"` | Resolution requires knowing the alphabet (latent vocabulary clueing). Also: the alphabetically-last key in clean (likely the queried-key) is NOT the alphabetically-last key in defective (the queried-key is absent), so the description resolves to a DIFFERENT key identity → violates §10 CRITICAL CHECK. |

Both example forms have TWO problems:
1. They use latent vocabulary/ordering knowledge (alphabet, "after" relation) that is not explicitly in the prompt → violates Manager's check #8.
2. They are list-content-DEPENDENT, so the resolved key identity differs across members (because the queried-key is absent in defective) → violates the spec's own §10 CRITICAL CHECK.

The spec's own internal logic catches problem #2 (the CRITICAL CHECK drops CAL-Q if the description resolves differently across members). But the examples invite the construction step to attempt these forms first, fail the CRITICAL CHECK mechanically, and DROP CAL-Q — leaving the spec without a workable indirect-query class.

**Closed-world + single-difference + non-trivial-difficulty is satisfiable**, but the §5 examples are the wrong forms for it. A workable class:

> **In-prompt code book (one workable form, CS proposes only as an example).** Prefix the prompt with an explicit mapping: `"Use this code book: A maps to 145, B maps to 27, C maps to 89, ..."`. The query becomes: `"What is the value for the key that maps from code A?"` The model must perform the decode step (`A → 145`) using ONLY the in-prompt codebook (closed-world ✓), then look up 145 in the list. The decoded integer (145) is the queried-key; it is PRESENT in clean and ABSENT in defective regardless of which other keys appear in the list (single-difference ✓). The decode step adds genuine difficulty without depending on latent vocabulary (alphabet/ordering) ✓.

Other workable classes may exist (e.g., explicit-in-prompt arithmetic where the model must compute the queried-key as the sum of two numbers stated in the prompt). The unifying constraint is that the description's resolution must depend ONLY on facts explicitly in the prompt AND be independent of which other list keys are present (so the description resolves to the same integer key identity in both members).

## §4. Recommended fix

**Senior should revise §5 to either:**

(a) Replace the example forms ("immediately after key J", "alphabetically-last key") with at least one example of a list-content-INDEPENDENT, fully-closed-world indirect form (e.g., the in-prompt code book pattern in §3 above, or explicit-in-prompt arithmetic);

OR

(b) Remove the example forms and explicitly state that the construction-step semantic-read must pick an indirect form satisfying BOTH:
- Manager's closed-world check #8 (all facts needed in the prompt; no latent vocabulary clueing);
- The §10 CRITICAL CHECK (resolution independent of which other list keys are present);

and rely on the construction step's drop-if-violated gate as the only enforcement.

Option (a) is cleaner because it removes the misleading examples + gives the construction step a concrete starting point. Option (b) is acceptable if Senior prefers to leave the form-selection fully to construction.

A v0.3 revision addressing this is the minimum fix CS sees. The rest of v0.2 is solid — premise correction is right, four-way reporting is right, decision rule is right, all other checks PASS.

## §5. CS disposition

**HOLD** on v0.2 pending revision to remove the closed-world-violating example forms in §5. All other 13 Manager checks PASS.

CS does NOT decide:
- Whether the HOLD can be addressed by a Senior note in v0.2 itself (replacing the §5 examples) or requires a v0.3
- Whether Manager wishes to accept v0.2 as-is on the grounds that the §10 CRITICAL CHECK + drop-if-violated gate already enforces the right thing, treating the §5 examples as illustrative-only

Both are within Senior + Manager's purview. CS surfaces the technical mismatch; the response shape is governance.

## §6. Sealed bytes + language perimeter

All sealed bytes UNCHANGED (≈58th survival check). No model run. No certification. No compression. No INT4. No Claim C. The 12-item §15 closed-gate list of v0.2 is preserved verbatim from the prior closed-gate convention.

— CS Engineer, 2026-06-13
