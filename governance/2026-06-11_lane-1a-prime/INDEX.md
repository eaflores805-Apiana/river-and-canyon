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
| 2026-06-12 | CS | CS → Manager | `CS-STANDARD-RETURN-TEMPLATE-v1.0-DELIVERY-v0.1.md` | FILED (return) | `9e8872d7790d9292` | Manager §14 7-item process artifact return (path, sha256, owner, scope, what-standardizes, what-doesn't-authorize, exit conditions). |
| 2026-06-12 | Manager | Manager → CS+NS | (received via session; mirror filed inline as MANAGER notice not separately committed) | (notice; no separate mirror) | — | Process Acceleration Protocols notice — directs preparation of 7 process artifacts; authorizes no execution. |
| 2026-06-12 | Manager | Manager → CS+NS | `MANAGER-PATH-A-AUTHORIZATION-2026-06-12.md` (TBD if mirror needed) | (received via session; Path A authorization) | — | Manager Path A authorization: all 4 boxes approved; model exec + sweep_id + L01-L08 + TP by name. |
| 2026-06-12 | CS | CS → Manager | `LANE1A-PRIME-PATH-A-RUN-RETURN-v0.1.md` | **HELD** (NS verification found schedule-degeneracy; cannot be cited as breadth) | `f8bf37ee509f8ef9` | Manager §8 31-item Path A run return. 8 rungs × 192 inferences = 1,536 total; **the run was an L01-equivalent surface repeated 8 times under different rung labels**, NOT a breadth test. Sealed schedule maps all rungs to per_rung_default. Held pending NS H1/H2/H3 disposition. |
| 2026-06-12 | NS | NS → CS+TL | (NS Path A HOLD memo — to be filed) | HOLD on Path A (schedule-degeneracy) | — | NS verification finding: committed bytes verify but artifact does not instantiate the breadth concept the packet claimed. Originated Manager §1 reasoning for suspending acceleration. |
| 2026-06-12 | Manager | Manager → all | (Process Acceleration Suspension notice; mirror TBD) | NOTICE | — | Manager suspends process acceleration for all model-facing gates; reinstates original gate-by-gate discipline; mandates semantic-read of load-bearing artifacts before Manager routing. |
| 2026-06-12 | CS | CS → TL | `CS-PATH-A-SCHEDULE-CLARIFICATION-v0.1.md` | FILED (Manager §19 return #1) | `[computed at commit]` | CS forensic clarification of the sealed schedule. Documents rung_schedule rung-uniform mapping + byte-identical task content across all 8 rungs (only rung_id and metadata.construction_recipe_hash differ). True breadth requires sealed-byte change → supersession-class. CS semantic-read failure acknowledged. |
| 2026-06-11 | CS | CS → all | `INDEX.md` (this file) | LIVE | (self-referencing) | Canonical project INDEX. CS seeds with new rows it files; Senior merges workspace catalog at next pass. |

## Gate state (carried verbatim from Senior's workspace `FULL-DOCUMENT-INDEX.md`; update at each project state change)

D1 ✓ · D2 ✓ · PH5-1 ✓ · run-3 complete (run of record; 12/12, drift 0.0000, 6/6 PASS) · D3 ACCEPTED ✓ · sealing package PASS ✓ · LOCK-RECORD v1.0 SEALED ✓ · D4-A complete · **D5 ACCEPTED** · D4-B COMPLETE + NS-VERIFIED · **D5-B ACCEPTED** · **D4 synthesis v0.3 ACCEPTED by Manager 2026-06-11** · Path A readiness packet v0.1.1 filed; Manager-accepted 2026-06-12 (all 4 boxes) · Path A EXECUTED 2026-06-12 · **Path A HELD by NS verification 2026-06-12 — schedule-degeneracy finding: sealed schedule maps all rungs to `per_rung_default`; task content byte-identical across rungs; result is L01-equivalent surface × 8 relabelings, NOT a breadth test** · **Manager Process Acceleration SUSPENDED for model-facing gates 2026-06-12; original gate-by-gate discipline reinstated; semantic-read of load-bearing artifacts now MANDATORY before Manager routing** · CS schedule-clarification memo filed (#1 in Manager §19 return order) · awaiting NS Path A HOLD disposition (H1 recharacterization, H2 TP-banner artifact class, H3 schedule-degeneracy/supersession); awaiting C5 claim-risk addendum; awaiting TL revised process note · LANE STATE: D4-A / D4-B / D4 synthesis accepted records remain bounded and auditable; Path A run retained but cannot be characterized as breadth; any true breadth attempt is supersession-class work pending Manager direction; all successor gates closed (true breadth rerun / L02–L08 / TP / quantization / INT8 / INT4 / stress-retention / candidate selection / threshold work / Claim C / benchmark / funder release / SBIR).

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

— Last touched: CS, 2026-06-12 (Path A HOLD: schedule-degeneracy finding; CS schedule-clarification memo filed #1 in Manager §19 return order; semantic-read failure acknowledged; acceleration suspended; original gate discipline reinstated)
