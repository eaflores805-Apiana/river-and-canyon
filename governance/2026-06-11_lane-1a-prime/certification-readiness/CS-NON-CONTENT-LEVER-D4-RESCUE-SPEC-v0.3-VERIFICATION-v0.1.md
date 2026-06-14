# CS Re-Verification — Non-Content-Lever D4 Rescue Spec v0.3 (CAL-Q)

**Author:** CS Engineer
**Date:** 2026-06-13
**Routed to:** Team Lead → Senior, Manager
**Status:** **PASS** — v0.3 fixes the v0.2 HOLD; all 16 Manager checks satisfied; CAL-Q v0.3 is ready for Manager decision on whether to authorize a narrow calibration-only run
**Authorization:** Manager 2026-06-13 — "CS Re-Verify CAL-Q v0.3" (model-free verification; NO execution)
**Artifact verified:** `NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.3.md` (sha256 `839249000bb1cb34d423534009d24682339e56c51ce393be45f5c03526a31a13`)

---

## §1. Identity + supersession

| Field | Value |
|---|---|
| Path | `governance/2026-06-11_lane-1a-prime/certification-readiness/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.3.md` |
| sha256 | `839249000bb1cb34d423534009d24682339e56c51ce393be45f5c03526a31a13` |
| Author | Senior Engineer |
| Self-anchor | `origin/main HEAD e2ad863` — **correct anchor** (the commit that landed v0.2 + CS HOLD verification; Senior fetched + drafted off the HOLD as designed) |
| v0.2 status | `d88cfef9…` — explicitly cited as superseded in v0.3 header; v0.2 file unchanged on disk at `certification-readiness/NON-CONTENT-LEVER-D4-RESCUE-SPEC-v0.2.md` |

## §2. Manager's 16-item checklist — line-by-line

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Path / commit / sha256 recorded | **PASS** | This memo + INDEX |
| 2 | INDEX row updated | **PASS** | Same commit |
| 3 | v0.2 retained, marked superseded, not overwritten | **PASS** | v0.3 header: "Supersedes v0.2 (d88cfef9), which is retained and marked superseded." v0.2 sha256 unchanged on disk (`d88cfef9…`). |
| 4 | Prior closed-world HOLD resolved | **PASS** | §0 "What the CS HOLD caught, and the fix" cites both reasons CS HELD on (latent vocabulary + list-content-dependence) and §3 fix uses in-prompt code book that is BOTH closed-world AND list-content-independent. |
| 5 | Clue fully defined inside the prompt | **PASS** | §3 example: "Use this code book: A = key_145, B = key_027, C = key_089". The mapping is in the prompt itself; no external lookup. |
| 6 | No synonym/antonym/alphabetic ordering/world fact/riddle/latent vocab clue | **PASS** | The decode step is a LITERAL alias lookup (A → key_145 from an in-prompt mapping). No alphabet, no "after" relation, no out-of-prompt knowledge. Grep for the v0.2 violating forms ("alphabetically-last", "immediately after key") finds them ONLY in §0 where Senior cites them as the rejected forms; they do not appear as new examples. |
| 7 | Code A resolves to same key identity in clean and defective | **PASS** | §3 explicit: "A = key_145" in BOTH members' identical code books. Resolution depends only on the in-prompt mapping (closed-world), not on other list keys (content-independent). §9 reiterates: "code A → key_145 in both members independent of list content." |
| 8 | Key present in clean, absent in defective | **PASS** | §3 clean form: "key_145 is present"; defective form: "key_145 is absent from the key-value list ← the permitted defect" |
| 9 | Content load CAL-B-like + unchanged (list 13, slots 8–11, near-miss 2) | **PASS** | §3 "(CAL-B-like content: list_len 13, slots 8–11, near-miss 2)"; §4 #5 explicit. |
| 10 | Decoy material unchanged | **PASS** | §4 #5: "Content list + decoy material CAL-B-like, unchanged except permitted defect"; §6: "no new decoy material" |
| 11 | Only query-side code-book step changes | **PASS** | §3 closing rationale: "the decode step (A → key_145, then look up) adds genuine clean-side difficulty WITHOUT touching list content or decoy material"; §4 #6 explicit. |
| 12 | Single-difference feasibility preserved | **PASS** | §9 explicit + CRITICAL CHECK "now satisfiable by construction" (vs v0.2's not-satisfiable-by-construction). The same key identity (key_145) is referenced by A in both members; the only difference is its presence/absence in the list. |
| 13 | Four-way defective reporting preserved | **PASS** | §7 verbatim from v0.2: strict NONE / concept abstention (authoritative) / true false-emission rate / format-abstention artifact. |
| 14 | Decision rule pre-declared (BAND PLAUSIBLE / NEEDS REPAIR / PIVOT) | **PASS** | §8 explicit, all three branches defined; "Rule fixed now, before any run." |
| 15 | No run-authorization language slipped in | **PASS** | Grep confirms only legitimate self-citations: header "Model-free revision authorized; no execution authorized" + role-naming "Manager: any later run authorization." Zero slipped authorizations. Zero closed-gate-violation phrases. |
| 16 | Closed gates preserved | **PASS** | §13 verbatim 12-item list (no execution / no CAL-Q run / no certification / no compression / no INT8 / INT4 / no second rung / no full ladder / no certification / no ranking / no Claim C / no public benchmark / no funder release / no SBIR). |

## §3. Resolution of the prior HOLD

CS's v0.2 HOLD identified the §5 example forms as failing Manager check #8 for two compounding reasons:
1. They used latent vocabulary/ordering knowledge (alphabet, "after" relation) → violated closed-world
2. They were list-content-dependent → resolved to different key identities in clean vs defective → would fail §10 CRITICAL CHECK by construction

**v0.3 fix is precise.** §0 explicitly cites both reasons and §3 replaces the example forms with an in-prompt code book pattern (matching exactly the workable example CS proposed in its v0.2 HOLD §3). The code book is fully in-prompt (closed-world), and code A maps to a specific integer key identity (`key_145`) regardless of which other keys are in the list (content-independent). Both members get the same code book and the same query; the only difference is whether `key_145` is in the list.

The same-key-identity invariant that v0.2 could only enforce via a drop-if-violated gate is now SATISFIABLE BY CONSTRUCTION — the construction step does not need to "find a workable form"; the spec hands it one that meets both Manager check #8 AND §10 CRITICAL CHECK.

## §4. CS disposition

**PASS.** CAL-Q v0.3 is ready for Manager decision on whether to authorize a narrow calibration-only run.

All 16 Manager checks satisfied at spec level. The v0.2 HOLD is cleanly resolved. The premise (clean saturation = live blocker; defective discrimination = confirm-check) preserved from v0.2. The four-way defective reporting (§7) and pre-declared decision rule (§8) preserved. Closed-gate list (§13) preserved verbatim.

The one HOLD that remains in v0.3's own internal checklist (semantic-read at §10) is appropriately scoped to the (gated) construction step and is not a CS verification blocker — it is the standard gate that semantic-reads happen when constructs are materialized, not when specs are written.

## §5. What CS does NOT decide

- Whether to authorize a CAL-Q run (Manager's call)
- Whether to authorize it now vs deferring (Manager's call)
- Whether the run should use a single-decode form or multi-layer alias (per §5 of v0.3: single-decode is the starting point; multi-layer is a tuning option Senior may need at construction; CS does not pre-judge)

CS surfaces that v0.3 is technically sound and the prior HOLD is resolved.

## §6. Sealed bytes + language perimeter

All sealed bytes UNCHANGED (≈59th survival check). No model run. No certification. No compression. No INT4. No Claim C. The 12-item §13 closed-gate list is preserved verbatim.

— CS Engineer, 2026-06-13
