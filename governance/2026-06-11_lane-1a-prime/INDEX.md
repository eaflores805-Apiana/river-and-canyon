# Lane 1a' Prime — Project INDEX

*Canonical project file. Six-column flat catalog + gate-state paragraph at the bottom.*

## Convention

Supersede, don't rewrite — every version retained; status is the single source of truth for which file is live. G1: nothing here is delivered until a repo commit SHA confirms it. A document isn't "filed" until its INDEX row is written; a row exists for every file in this project's directory.

## Maintainership

Project file, primarily maintained by Senior. CS adds rows for memos it files directly — Manager-direction mirrors, NS/C5 mirrors, return memos, verification co-signs. Senior's workspace catalog (`FULL-DOCUMENT-INDEX.md` in C6_Proposal workspace, sha256 `[per Senior's index]`) carries the fuller historical trail; it will merge into this canonical file on Senior's next pass. Until then, this file is **partial — the recent CS-filed rows are accurate; older rows live in the workspace catalog**.

## Status vocabulary (closed list; don't invent new statuses)

`ACTIVE` · `SUPERSEDED by <vN>` · `DISPOSITIONED` · `DELIVERED` · `ABSORBED into <doc>` · `WITHDRAWN` · `HISTORICAL` · `DRAFT` · `FILED` · `MIRROR`

## Table

| Date | Author | Routed to | Document | Status | sha256(16) | Notes |
|---|---|---|---|---|---|---|
| 2026-06-11 | NS | NS → CS+TL | `LANE1A-PRIME-D4-SYNTHESIS-AND-NEXT-QUESTIONS-v0.2.md` | SUPERSEDED by v0.3 | `22bc922ba7c05a90` | NS-finalized synthesis with C5 adversarial layer merged. Retained. |
| 2026-06-11 | CS | CS → TL | `LANE1A-PRIME-D4-SYNTHESIS-AND-NEXT-QUESTIONS-v0.2.1.md` | SUPERSEDED by v0.3 (parallel CS patch) | `1900fc1fd24ede11` | CS interim patch applying E1-E3 to v0.2; superseded by NS workspace v0.3 (same E1-E3 + optional N1; NS authored as synthesis lead = canonical). Retained. |
| 2026-06-11 | CS | CS → TL | `CS-D4-SYNTHESIS-v0.2.1-FILING-RETURN-v0.1.md` | FILED (return) | `0f7f712f8ebcc399` | TL §7 10-item return for the v0.2.1 patch filing. Retained; superseded as v0.2.1 was. |
| 2026-06-11 | NS | NS → CS+TL → Manager | `LANE1A-PRIME-D4-SYNTHESIS-AND-NEXT-QUESTIONS-v0.3.md` | ACCEPTED (Manager) | `674c98c86ed4f613` | NS workspace v0.3: applies E1, E2, E3 exactly + optional N1. Manager-accepted 2026-06-11 as bounded D4 synthesis + advisory next-questions record. |
| 2026-06-11 | CS | CS → TL | `CS-D4-SYNTHESIS-v0.3-STATE-VERIFICATION-v0.1.md` | DISPOSITIONED (TL filter PASS; Manager accepted v0.3) | `3b346bb22e1fd329` | TL §6 state-verification co-sign for v0.3: VERIFIED. Routed up; Manager acceptance followed. |
| 2026-06-11 | Manager | Manager → all | `MANAGER-D4-SYNTHESIS-v0.3-ACCEPTANCE-2026-06-11.md` | MIRROR (canonical CS mirror of Manager memo) | `1cd123c34237f587` | Manager final disposition: D4 synthesis v0.3 ACCEPTED as bounded interpretation + advisory next-questions record; authorizes no execution. |
| 2026-06-12 | NS | NS → CS+TL | `LANE1A-PRIME-PATH-A-READINESS-PACKET-v0.1.md` | SUPERSEDED by v0.1.1 (generator-path correction) | `f23b40d0e9f8d9b6` | NS-drafted Path A readiness packet. Generator-path string error (d4_runner/ → lane1a_prime/) caught at CS state-verification; corrected via v0.1.1 patch per TL §4. Retained. |
| 2026-06-12 | CS | CS → TL | `CS-PATH-A-READINESS-PACKET-STATE-VERIFICATION-v0.1.md` | DISPOSITIONED (TL: VERIFIED WITH ONE CORRECTION REQUIRED) | `c9a1cd1df3028fdc` | TL §8 state-verification co-sign for v0.1: VERIFIED with one minor finding (path string). TL elevated finding to required correction; CS applied as v0.1.1. |
| 2026-06-12 | CS | CS → TL | `LANE1A-PRIME-PATH-A-READINESS-PACKET-v0.1.1.md` | ACTIVE | `cf21aaa1b7fbda47` | TL-required patch: generator path corrected `d4_runner/validation.py` → `lane1a_prime/validation.py`. Generator hash `db69519f…` unchanged. No other substantive content changed. |
| 2026-06-12 | CS | CS → TL | `CS-PATH-A-READINESS-PACKET-v0.1.1-FILING-RETURN-v0.1.md` | FILED (return) | `8a689b1827046dd9` | TL §5 14-item return for the v0.1.1 patch filing. |
| 2026-06-12 | CS | CS → Manager | `../standing/STANDARD-RETURN-TEMPLATE-v1.0.md` (cross-project) | DRAFT (awaiting TL filter under PROCESS-ACCELERATION-ADOPTION-MEMO) | `488a5cc147b7f11b` | CS deliverable per Manager §13 / §14 process-acceleration notice. Consolidates STANDARD-RETURN-TEMPLATE + 3 CS conventions (artifact-hash-table, G1 enumeration, test-log/assertion). Cross-project; lives in `governance/standing/`. |
| 2026-06-12 | CS | CS → Manager | `CS-STANDARD-RETURN-TEMPLATE-v1.0-DELIVERY-v0.1.md` | FILED (return) | `[computed at commit]` | Manager §14 7-item process artifact return (path, sha256, owner, scope, what-standardizes, what-doesn't-authorize, exit conditions). |
| 2026-06-11 | CS | CS → all | `INDEX.md` (this file) | LIVE | (self-referencing) | Canonical project INDEX. CS seeds with new rows it files; Senior merges workspace catalog at next pass. |

## Gate state (carried verbatim from Senior's workspace `FULL-DOCUMENT-INDEX.md`; update at each project state change)

D1 ✓ · D2 ✓ · PH5-1 ✓ · run-3 complete (run of record; 12/12, drift 0.0000, 6/6 PASS) · incidental dispositioned ✓ · D3 ACCEPTED ✓ · sealing package PASS ✓ · LOCK-RECORD v1.0 SEALED ✓ · D4-A complete · **D5 ACCEPTED — D4-A record closed as finished auditable unit** · **D4-B COMPLETE + NS-VERIFIED (9b0e0ee)**: six-criterion vs real model; candidate 80/80, TP control 1/80 = 0.0125, NW diff [0.9159, 0.9978] independently recomputed; TP did not fire; NOT_RULED_OUT; banner deviation did NOT recur; per-run runner provenance · Manager-accepted · **D5-B ACCEPTED — D4-B LIFECYCLE CLOSED** · **D4 synthesis v0.3 ACCEPTED by Manager 2026-06-11** (bounded interpretation + advisory next-questions record; authorizes no execution) · **Path A readiness packet v0.1.1 filed 2026-06-12 (L01-L08 with TP active proposed; supersession NONE REQUIRED; Manager checklist unbundled; TL-required generator-path correction applied; v0.1 retained; awaiting TL filter + Manager decision)** · LANE STATE: two complete model-facing lifecycles closed (D4-A five-criterion, D4-B six-criterion w/ measured TP); D4 synthesis accepted; Path A readiness prepared; no successor execution authorized · TP guard binding for all future reference · all successor gates closed by name (Path A / L02–L08 / further TP / quantization / Claim C / benchmark / funder-facing release / SBIR submission).

## Where canonical artifacts live

- **Sealed instrument:** `experiments/2026-06-11_lane-1a-prime/validation/` (3 lock-event artifacts; bound by sealed LOCK-RECORD v1.0 sha256 `51e18fa9…`)
- **D4-A run-of-record:** `experiments/2026-06-11_lane-1a-prime/d4_a_pilot/`
- **D4-B run-of-record:** `experiments/2026-06-11_lane-1a-prime/d4_b_pilot/`
- **Runners:** `experiments/2026-06-11_lane-1a-prime/d4_runner/`
- **Governance memos:** `governance/2026-06-11_lane-1a-prime/`
- **Sealed LOCK-RECORD v1.0:** `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md` (sha256 `51e18fa9…`, ≈15 survival checks)

## Standing constraints (carried by reference)

- All successor model-facing gates CLOSED until Manager separately approves by name.
- D4 token-prior authorization slot remains UNOPENED for any further use.
- Claim C INACTIVE.
- Forbidden phrasings (binding for all future references to D4-A / D4-B): `model passed` · `capability established` · `not shortcut-driven` · `candidate certified` · `task family viable` · `Claim C progressed` · `seam evidence` · `public benchmark result` · `certification achieved`.

— Last touched: CS, 2026-06-12 (STANDARD-RETURN-TEMPLATE-v1.0 filed under governance/standing/ per Manager process-acceleration §13/§14; CS delivery memo added; awaiting TL filter under PROCESS-ACCELERATION-ADOPTION-MEMO)
