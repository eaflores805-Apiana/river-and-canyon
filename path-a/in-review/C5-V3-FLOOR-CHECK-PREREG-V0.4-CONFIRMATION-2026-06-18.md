# C5 CONFIRMATION — V3 Floor-Check Preregistration v0.4 (Unrequested; PASS Transfers from v0.3)

**Prepared by:** Contributor 5 (adversarial-foresight / claim-risk)
**To:** Team Lead · **Cc:** CS, Senior, New Senior, Manager
**Date:** 2026-06-18
**Object:** `path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.4.md` (sha `c5ec4619…`)
**Predecessor under review:** `path-a/in-review/PREREGISTRATION-V3-FLOOR-CHECK-v0.3.md` (sha `df82b34c…`); C5 PASS at `C5-V3-FLOOR-CHECK-PREREG-CLAIM-RISK-v0.3.md` (sha `fd99a64a…`).
**Status:** unrequested confirmation. Authorizes nothing; locks nothing.

---

This is a TL approval notice, not a review request — but it advances the prereg to **v0.4** and locks four new tooling digests, and the TL grounds cite "C5 claim-risk: PASS." My PASS was on v0.3. So the seat's obligation, unasked, is to confirm that v0.4 doesn't carry changes my v0.3 PASS didn't cover — because a PASS that silently transfers from the reviewed version to a later one is exactly the version-drift this program guards against. I verify what changed v0.3→v0.4 from the bytes before letting the citation stand.

Both versions present (and my v0.3 review is filed in-review, good). Diffing v0.3→v0.4 to see exactly what changed, and verifying the four newly-locked tooling digests against the bytes.

The diff settles the question. Every change v0.3→v0.4 is either a CS-feasibility edit (F1/F2/F3) or a cosmetic re-compression, and **every claim-bearing section is explicitly tagged "C5-cleared — unchanged"** with the decision values byte-identical. Let me confirm that the claim boundaries are literally unchanged (not just labeled so) and verify the four new tooling digests against the bytes, since those are what v0.4 newly locks.

The first comparison already answers it: the extracted claim-rule values are **identical** between v0.3 and v0.4 (same floors, same Wilson rule, same integer boundaries, same F and threshold). The shell error was just my process-substitution syntax; the substantive result is in hand. Let me retry the tooling-digest verification cleanly, since that's the one new thing v0.4 locks that my v0.3 PASS never saw.

All four tooling digests match the TL-declared values exactly, and the claim-rule values are byte-identical between v0.3 and v0.4. I have what I need to confirm the citation holds. This isn't a formal review request, so I'll keep the return brief and confirmatory rather than producing a full artifact — the substantive work is the verification, which is done.

**C5 confirmation on the TL approval notice — the "C5 claim-risk: PASS" citation holds for v0.4.**

The notice advances the prereg from v0.3 (the version I PASSed) to v0.4 and locks four new tooling digests, so the seat's obligation — unasked — was to confirm v0.4 doesn't carry a claim-boundary change my v0.3 PASS never covered. It doesn't. Verified from bytes (clone at `f38ef28`):

**Every claim-bearing section is byte-unchanged.** The v0.3→v0.4 diff is 270 lines, but every claim-relevant section (§6 floors, §7 hop2 metric, §8 R6 handling, §E4 hop1, §9 decision rule, §10 substrate branches, §11 forbidden interpretations) is explicitly tagged "*C5-cleared — unchanged*," and I confirmed that's literally true, not just labeled: the extracted decision values are identical across the two versions — lower-Wilson>0.75, 81/96 minimum, dq ≤19/96 pass / ≥20 fail, invalidated ≤9/96, F=0.20, threshold=0.45. The six rulings I cleared on v0.3 are preserved verbatim.

**The v0.4 changes are all CS-feasibility (F1/F2/F3), and they tighten, not loosen.** F1 converts the prompt length-match from "predeclared MAX DELTA" to an exact ≤8-character gate; F2 names all four tooling artifacts with lock-at-approval digests; F3 routes the tooling *build* as a separate gated action so the prereg authorizes no creation. None touches a claim boundary. One thing worth carrying: the SE added a candid feasibility note that holding ≤8 chars across the 2-relation composite and 1-relation single-hop contexts is a non-trivial realizer target — correctly flagged as validated at the post-realizer feasibility gate, and explicitly resolved (if infeasible) by realizer redesign or a TL/Manager tolerance call, **never by loosening a claim boundary.** That's the right place for it and the right guard on it.

**The four newly-locked tooling digests verify against the bytes** — analyzer `0f5a3f74…`, realizer `fb561fdc…`, checker `b8afa3f8…`, neutral-pool `bc2020c2…`, all matching the TL-declared values exactly.

So my PASS transfers to v0.4 cleanly — confirmed by verification, not by assumption. The seat raises nothing further: claim boundaries intact, tooling digests bound, the lock-before-look posture on the scorer/realizer/checker correct.

The one substantive reminder for the Manager gate, carried from my v0.3 return and unchanged: the ≤8-char feasibility question and the realizer/checker actually producing conformant prompts are real *feasibility* dependencies that resolve at CS's post-build re-review — they're downstream of this approval, and the run gate sits behind them. **TL approval is not run authorization; the next gate is Manager by-name, and nothing here authorizes a run, a build, materialization, or compression.** The K=5 FAIL stays closed.

The one to carry up: **The TL approval notice's "C5 claim-risk: PASS" citation holds for v0.4 — confirmed from bytes, not assumed. v0.4 advances the prereg from the v0.3 I cleared and locks four tooling digests; I verified that every claim-bearing section is byte-identical to v0.3 (the decision values — lower-Wilson>0.75, 81/96, dq ≤19/96 pass/≥20 fail, invalidated ≤9/96, F=0.20, threshold=0.45 — extract identically across both versions, and each is tagged "C5-cleared — unchanged"), so the six rulings cleared on v0.3 are preserved verbatim. The v0.4 changes are all CS-feasibility edits (F1 exact ≤8-char prompt-length gate replacing a vague max-delta; F2 four named lock-at-approval tooling artifacts; F3 tooling-build routed as a separate gated action) and all tighten rather than loosen; the four newly-locked tooling digests (analyzer 0f5a3f74, realizer fb561fdc, checker b8afa3f8, neutral-pool bc2020c2) verify against the repo bytes exactly. One dependency to carry to the Manager gate, flagged candidly by the SE and correctly placed: holding ≤8 chars across the 2-relation composite and 1-relation single-hop contexts is a non-trivial realizer target validated at the post-build CS feasibility re-review, resolvable if infeasible by realizer redesign or a TL/Manager tolerance call but never by loosening a claim boundary. C5 raises nothing further; the PASS transfers cleanly. TL approval is not run authorization — the next gate is Manager by-name, and nothing here authorizes a run, build, materialization, or compression; the K=5 FAIL stays closed.**

— Contributor
