# Senior Re-Delivery Note — G1 Handoff Artifacts (per Team Lead memo, 2026-06-10)

From: Senior Engineer
To: CS Engineer; Cc: Team Lead, Manager
Status: Re-delivery executed; G1 closure pending CS on-disk verification

**1. Drop location.** Files placed by Manager (direct upload) at the preferred location:
`Apiana_Papers/certification_before_retention/paper3-certification-before-retention/cutover-final-2026-06-10/`
— CS: if the Manager used a different path, the filenames and hashes below identify the correct
versions regardless; verify by hash, not by location. **Note: the Manager's upload may predate the
content updates in items 1–3 below (hashes changed today). Verify against THESE hashes; if the on-disk
copies show the older prefixes (13377b12 / 19d81157 / d3919288), request the refreshed bundle
`river-and-canyon-cutover-final-2026-06-10.zip` from the Manager — it contains all five files at the
hashes enumerated here.**

**2–5. Enumeration (filename · intended path/use · full sha256 · supersession):**

1. `PROJECT-MAP-2026-06-10.md`
   → `governance/passdown/2026-06-10_project-map.md`
   sha256 `f4886a980ccf173c0a43e0c0a66f84f4354e4e2f85e45d3a87ab27127c77fb6e`
   **Supersedes** committed `a2050a4d…` AND the previously reported uncommitted `13377b12…`. Now
   contains the full tightened Lane 1a doctrine including a verbatim doctrine-summary line carrying
   every required phrase from the Team Lead's §2 list (rule-out/rule-in, pre-candidate, unordered
   survivor set, negative-use only, no gate-verdict-shaped labels, no heatmaps/contours/certification
   bands/promising-region overlays, B1 v2 provenance if ever separately authorized).
   **Commit now.**

2. `PASSDOWN-2026-06-10.md`
   → `governance/passdown/2026-06-10_senior-passdown.md`
   sha256 `e0444f8cf12024ab5dd7f13644799cd46e3d68ef4a4e93a3a1a397e407890b8f`
   **Supersedes** committed `7095e11a…` AND the previously reported uncommitted `19d81157…`. Now opens
   with a CURRENT STATE ADDENDUM containing every item on the Team Lead's §3 list, with one
   Manager-directed correction to that list: Draft 2 is no longer "owned by the incoming Senior seat"
   — per explicit Manager direction of 2026-06-10, the outgoing seat produced Draft 2 (now in team
   review) and the incoming Senior starts clean at the next task boundary. Also includes: Draft 1
   exists; failure-mode standard applies; vehicle principle; whitespace-collapsed pre-tag check; Q2
   adjudication open; Lane 1a proposed/not authorized; all gates closed.
   **Commit now.**

3. `RESPONSE-TO-INCOMING-SENIOR-DRAFT1.md`
   → intended use: Senior-to-Senior continuity / review-record material.
   sha256 `46ca29279490b01ca147cb001b20ec4061ecc032ee2248c589606771255f2cbf`
   (recomputed at routing time per the memo's instruction; prior `d3919288…` is stale.)
   Supersedes nothing committed (never delivered).
   **HOLD — do not commit now.** Archive with the v1.1 review records when that directory opens
   (intended archive path: `governance/2026-06-10_paper3-v1.1-review/RESPONSE-TO-INCOMING-SENIOR-
   DRAFT1.md`), with the annotation that its §§6–7 routing is partially superseded by the Manager seat
   direction recorded in artifact 2.

**Additionally enumerated (new, same drop — the live v1.1 review package):**

4. `PAPER3-certification-before-retention-DRAFT2-v1.1.md`
   → intended use: team review; commits at RC per the rail, not before.
   sha256 `154da80267bc457f47ecaa8d9e9d8b4b7ecc8284ced51951df6f3caff1cf8ecf`
   Supersedes Draft 1 (chat-delivered, never committed — correct per rail). **HOLD until RC.**

5. `PAPER3-v1.1-DRAFT2-SUBMISSION-MEMO.md`
   → intended use: team review input; archive with v1.1 review records.
   sha256 `a7512f1a113473e7f8684ff84c9feb7ec2d2a308fb261ac8c29b1b3a7ce7380b`
   Supersedes nothing. **HOLD for v1.1 review archive.**

**6. Intentionally held:** items 3–5, as stated, with named archive intents.

**7. Open under G1 after this delivery:** items 1–2 until CS reports commit SHAs at the intended paths
with hash verification; items 3–5 then convert to tracked-held status (open-by-design with named
destinations, closing at v1.1 review archival and RC respectively). Per the rule: this note is intent;
CS's on-disk verification and commit SHAs are delivery.

— Senior Engineer, 2026-06-10
