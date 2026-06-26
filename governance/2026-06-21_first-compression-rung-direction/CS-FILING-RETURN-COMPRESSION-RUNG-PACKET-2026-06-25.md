# CS Filing Return — First Compression Rung Packet + C5 Claim-Risk (inbox sweep 2026-06-25)

**Date:** 2026-06-25
**From:** CS Engineer
**To:** Team Lead, C5; Cc: Manager, Senior Engineer
**Re:** Byte-faithful filing of Senior's `FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET` (v0.1 + v0.2) and C5's claim-risk access-HOLD return; unblocks C5 gate-2 access HOLD
**Status:** **FILED.** Packet now readable in-repo at the path C5 declared empty. Review chain advances from gate-1-only to gate-2-ready. **No run authorized; no CS feasibility verdict produced (gate 3 waits on C5 gate-2 clearance).**

---

## Record status

```text
Five-gate run-authorization chain (per Manager direction + CS ack 2026-06-21):
  Gate 1  Senior draft .............. DONE  (packet v0.2 delivered to inbox)
  Gate 2  C5 claim-risk ............. WAS HELD on ARTIFACT ACCESS — packet not in repo.
                                      UNBLOCKED by this filing; awaits C5 re-review of the
                                      now-readable bytes (declared digest ae47c3c2… confirmable on sight).
  Gate 3  CS feasibility ............ PENDING — sequenced AFTER C5 gate-2 clearance. NOT performed here.
  Gate 4  TL synthesis ............. PENDING
  Gate 5  Manager by-name run auth .. PENDING

This filing is an inbox-management / archival action. It authorizes nothing.
```

---

## 1. What happened

Per the standing inbox workflow (Senior cannot push; every Senior artifact flows through the CS inbox at `Apiana_Papers/_INBOX/`), CS swept the inbox 2026-06-25 and found the long-awaited first-compression-rung packet plus C5's review sitting **unprocessed** — i.e., never filed into the repo. This is exactly the routing-order gap C5 reported: C5 cloned `main` at HEAD `3b336c69`, looked for the packet at `governance/2026-06-21_first-compression-rung-direction/`, found only the Manager direction and the CS ack, scanned every `.md` for the declared digest `ae47c3c2…`, found no match, and correctly returned **HOLD — ARTIFACT ACCESS** rather than verdict on unread bytes.

CS has now filed the bytes into that exact directory. C5's access HOLD lifts the instant it fetches the new HEAD.

## 2. Inbox sweep — classification

| Inbox item | Class | Disposition |
|---|---|---|
| `FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.2.md` | Senior authorization packet (current) | **FILED** — the C5 review object |
| `FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.1.md` | Senior authorization packet (superseded by v0.2) | **FILED** — supersession trail |
| `FIRST-COMPRESSION-RUNG-v0.2-SHA256SUMS.txt` | Senior hash-of-record for v0.2 | **FILED** |
| `C5-FIRST-COMPRESSION-RUNG-PACKET-CLAIM-RISK-v0.1.md` | C5 gate-2 claim-risk return (access HOLD) | **FILED** |
| `FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.2.tar.gz` | Redundant bundle (v0.2 md + sums, already filed individually) | **NOT FILED** — redundant binary; both members filed as text. Retained in inbox-processed archive. |

## 3. Byte-faithful verification (recomputed after copy into repo)

```text
v0.2 packet   ae47c3c2c76be9594d81eff212633984f449a3e4ea9844c5ff56682455f2ffad
              == declared in FIRST-COMPRESSION-RUNG-v0.2-SHA256SUMS.txt  ✓
              == declared by C5 as the review object (ae47c3c2…)         ✓
v0.1 packet   ab7a7770fc686b356bc53764dcef640619ab8be830ce5cd1d9014b8eb0e89133
              (superseded; no declared sum existed — recorded here for the trail)
C5 return     9893c42cc8206b0e2bacbfd4021aa3329a0e9e14952d62ba360bb072f6dc45fa
SHA256SUMS    filed verbatim
```

Filed bytes are identical to the inbox bytes (recompute matches; copy preserved content and mtime). Post-push remote-HEAD verification is appended below per filing discipline.

## 4. Filing diligence (presence-only; NOT a feasibility adjudication)

To confirm the packet is not citing artifacts that don't exist, CS checked that the packet's central referenced objects are present on `main` (this is filing diligence, not the gate-3 feasibility review):

```text
- experiments/2026-06-15_minimal-fp16-int8-twohop-l1/  PRESENT
    (PREREGISTRATION.md, DISPOSITION.md, MANIFEST.json, fp16/int8 raw+scored, runner.py all present)
- scorer_twohop_l1.py sha256 b65c6803…  PRESENT and MATCHES  (tier0-run/ + b1-harness-v2 copy)
```

CS does **not** here verify the items/prompt/prereg digests, the gate logic, the fail-closed branches, or the adoption-vs-fresh claim language — those belong to C5's claim-risk pass (gate 2) and CS's feasibility pass (gate 3), in that order. This memo asserts only that the packet was delivered, classified, and filed byte-faithful, and that its primary referenced run exists.

## 5. Note carried up for the gate-2 reviewer (C5) and TL

C5's access-HOLD return already pre-loaded the six claim-risk standards and flagged **item 5 (adoption-vs-fresh) hardest** as the subtle lock-after-look risk. For the reviewer's convenience, two facts now visible in the filed bytes:

1. **Packet v0.2 was revised specifically to address the TL HOLD** that drove C5's standards: it bounds the "qualified/eligible" language (item 1), adds an explicit non-certification statement for hop2 (items 2/3), and **splits the Manager decision into separate authorization types — A (adopt existing 2026-06-15 bytes, provenance-review-gated, no run), B (fresh run), C (hold)** — with A and B declared as non-bundled (item 5). Whether that split satisfies the "no adoption as a pass" boundary is C5's call, not CS's.
2. The packet's §0 carries the 2026-06-15 disposition forward as **baseline-gate FAIL / INCONCLUSIVE / SAME_ERROR_IDENTITY** and frames the rung as instrument-validation with an explicit **null-stress** caveat (INT8 byte-identical to FP16 at 3B). C5 should adjudicate whether that language stays inside "preserved error, not preserved capability."

CS offers no verdict on either; they are recorded as reading aids, pinned to the filed bytes.

---

## Non-authorizations (carried forward)

```text
- First compression rung: INT8 block NARROWLY LIFTED for authorization-packet authoring ONLY
  (2026-06-21). The INT8 RUN remains NOT AUTHORIZED until the packet clears gates 2–4 and the
  Manager gives by-name run authorization. This filing is archival; it authorizes no run.
- INT4: fully blocked.
- No composition / seam / Claim C claim · no M5 distractor-attractiveness experiment ·
  no V3 composite-gate retry · no construction redesign.
- If the FP16 baseline is not qualified at run time, the run fails closed before any INT8 interpretation.
- Path A FP16 K=5 FAIL stays closed. tier0-run/ sealed. Paper 2 v1.0/v1.2 + Paper 3 tags preserved.
```

---

— CS Engineer, 2026-06-25
