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
| 2026-06-11 | NS | NS → CS+TL | `LANE1A-PRIME-D4-SYNTHESIS-AND-NEXT-QUESTIONS-v0.2.md` | SUPERSEDED by v0.2.1 | `22bc922ba7c05a90` | NS-finalized synthesis with C5 adversarial layer merged. C5 wording edits E1–E3 applied as v0.2.1 per TL direction. |
| 2026-06-11 | CS | CS → TL | `LANE1A-PRIME-D4-SYNTHESIS-AND-NEXT-QUESTIONS-v0.2.1.md` | ACTIVE | `1900fc1fd24ede11` | E1 (breadth wording), E2 (transfer wording), E3 (constructibility-name collision) applied verbatim; no other content change; v0.2 retained. |
| 2026-06-11 | CS | CS → TL | `CS-D4-SYNTHESIS-v0.2.1-FILING-RETURN-v0.1.md` | FILED (return) | `[computed at commit]` | TL §7 10-item return for the v0.2.1 patch filing. |
| 2026-06-11 | CS | CS → all | `INDEX.md` (this file) | LIVE | (self-referencing) | Canonical project INDEX. CS seeds with new rows it files; Senior merges workspace catalog at next pass. |

## Gate state (carried verbatim from Senior's workspace `FULL-DOCUMENT-INDEX.md`; update at each project state change)

D1 ✓ · D2 ✓ · PH5-1 ✓ · run-3 complete (run of record; 12/12, drift 0.0000, 6/6 PASS) · incidental dispositioned ✓ · D3 ACCEPTED ✓ · sealing package PASS ✓ · LOCK-RECORD v1.0 SEALED ✓ · D4-A complete · **D5 ACCEPTED — D4-A record closed as finished auditable unit** · **D4-B COMPLETE + NS-VERIFIED (9b0e0ee)**: six-criterion vs real model; candidate 80/80, TP control 1/80 = 0.0125, NW diff [0.9159, 0.9978] independently recomputed; TP did not fire; NOT_RULED_OUT; banner deviation did NOT recur; per-run runner provenance · Manager-accepted · **D5-B ACCEPTED — D4-B LIFECYCLE CLOSED** · **D4 synthesis v0.2.1 filed (C5 wording edits E1–E3 applied; awaiting TL filter)** · LANE AT FULL REST AGAIN: two complete model-facing lifecycles closed (D4-A five-criterion, D4-B six-criterion w/ measured TP), both bounded, both auditable · TP guard binding for all future reference · all successor gates closed by name (successor D4 / L02–L08 / further TP / quantization / Claim C / benchmark / funder-facing release / SBIR submission).

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

— Last touched: CS, 2026-06-11 (seed pass at canonical repo path)
