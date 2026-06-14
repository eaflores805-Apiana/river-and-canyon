# C6 Proposal Archive — Pre-Lock Instrument Validation Addendum work-trail

Filed by CS Engineer, 2026-06-11. Three-way hash verified against
apiana-papers/C6_Proposal/ originals.

This subfolder archives the complete drafting chain for the
**Pre-Lock Instrument Validation Addendum** — from Contributor 6's
original proposal, through Senior routing recommendation, four New
Senior draft revisions (v0.1 → v0.2 → v0.3 → v0.4 → v0.4.1), Senior
step-3 review of v0.1, and the E21 self-application disposition
table prepared as part of the adoption package.

## Chronology and routing record

| # | File | sha256 (first 16) | Description |
|---|---|---|---|
| 1 | `SENIOR-ROUTING-REC-C6-PROPOSAL-2026-06-10.md` | `565654cfc9767c3e…` | Senior recommendation: **accept C6 content; merge into the routed addendum task; do not authorize a parallel packet.** §1 enumerates C6's 5 components and their 1:1 mapping into the addendum's Section A/B/C structure. §4 records the scope caution: the `scrambled_binding_retrieval` reframing may not be used to retroactively reinterpret Lane 1a control numbers as a positive rebinding finding. |
| 2 | `INPUTS-PACKAGE-INSTRUMENT-VALIDATION-ADDENDUM-v2-2026-06-11.md` | `6e116a7c04f854f1…` | Updated inputs package to New Senior incorporating the C6 source-6 addition. Distinct from the original inputs package (sha256 `3896fab1…`) CS filed earlier; both retained for audit completeness. |
| 3 | `SENIOR-REVIEW-ADDENDUM-v0.1-2026-06-10.md` | `166e7d54e31fe87c…` | Senior step-3 review of v0.1. Verdict: **PASS for CS review, with two required revisions** (frozen-term preservation via the ill-formed umbrella; per-policy oracle precision). D2 ancestor quote verified verbatim against released v1.1 manuscript. §"Commendations" enumerates four original contributions of the draft. |
| 4 | `PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM-v0.2-2026-06-11.md` | `7b590b88893cd0fd…` | v0.2 — incorporates Senior's two required revisions from v0.1 review. |
| 5 | `PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM-v0.3-CANONICAL-2026-06-11.md` | `88c1de9c926c8e94…` | v0.3 — applies five Team Lead filter edits. **This is the canonical-bytes copy** of what CS earlier filed at `PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM-v0.3-2026-06-11.md` from conversation-shared text; the canonical-bytes hash is the authoritative one. (CS's earlier filing carries CS-added routing scaffolding; this archive copy has source bytes only.) |
| 6 | `NEW-SENIOR-ROUTING-v0.3-TO-SENIOR-2026-06-11.md` | `c8837d133bcf5c1f…` | New Senior's routing of v0.3 to Senior for conceptual review (step 3 of the path). |
| 7 | `PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM-v0.4-2026-06-11.md` | `23bd73d820614bb5…` | v0.4 — **consolidated team/outside review round, edits E1–E21.** New A6 (final-manifest re-verification), strengthened Lane 1a citation, B2 non-claim, oracle-case completeness, B4-Q5 tightened, diagnostic-only loophole closed, per-class remediation rules, pilot iteration logging, standardized enforcement language, offline-execution qualifiers, deferred-item inheritance, §8 citation adoption check (E19 = CS), path hardening (E20 = CS). |
| 8 | `PRE-LOCK-INSTRUMENT-VALIDATION-ADDENDUM-v0.4.1-2026-06-11.md` | `c3e88fd32de08d8f…` | **CURRENT CANDIDATE for CS review** — clarifies that Manager decline-with-rationale cannot preserve dead, tautological, or malformed rules in an active eliminative path. No other substantive change from v0.4. |
| 9 | `ADOPTION-PACKAGE-T4-DISPOSITION-TABLE-2026-06-11.md` | `61f33100ff00ee6f…` | **E21 adoption package** — T4 self-application disposition table. Records all review findings + dispositions to date. **CS items deferred with owner:** E19 (§8 D2 ancestor verification — preliminary CS pass at commit `67c9bd5` + author verification on released bytes); E20 (path convention codification vehicle). Plus C5-x pointer note: "C5 intake memo's committed repo path was not located this session — CS to attach the reference at adoption." |

## Routing posture (updated)

The earlier filing of v0.3 with CS-added routing scaffolding placed
the addendum at "Senior conceptual review IN FLIGHT; CS HOLDS."
Updated picture from the T4 disposition table:

| Step | Status |
|---|---|
| 1. New Senior drafts | DONE through v0.4.1 |
| 2. Team Lead filter | PASS (v0.2 → v0.3) |
| 3. Senior conceptual review of v0.3 | Effectively folded into the E1–E21 consolidated round per the T4 table |
| 3.5 Team Lead + outside consolidated edit round | DONE (incorporated as v0.4) |
| 3.6 Manager decline-rationale clarification | DONE (incorporated as v0.4.1) |
| **4. CS review (implementability + path + templates)** | **POSITIONED (current step)** — E19 and E20 are deferred items owned by CS |
| 5. Manager adoption decision | PENDING (after CS review) |

## CS items owed to the adoption package

Per the T4 disposition table:

1. **E19** — `§8 D2 ancestor verification vs v1.1 tag.` Preliminary CS
   pass at commit `67c9bd5` was incorporated as evidence. Formal check
   at adoption time.
2. **E20** — `Resolved path recorded in adoption commit; codification
   vehicle choice.` CS implementability review per §5 of the
   consolidated memo. Adoption condition. CS prior pre-verification:
   `governance/standing/` convention is in force; proposed path
   consistent. Codification vehicle (extend `STANDING-REVIEW-DISCIPLINE.md`
   vs new `STANDING-PATH-CONVENTIONS.md`) is the open choice.
3. **C5-x** — pointer note that the C5 intake memo's committed repo
   path was not located. CS records: parallel question already filed
   in `TEAMLEAD-DIRECTION-CLOSE-OUT-ADOPTION-PATH-2026-06-10.md`
   "Open question to Manager." Same materials referenced from two
   different adoption tracks; CS unable to locate standalone copies.

CS does not act on E19/E20 formal closure or on adoption commit until
Manager directs.

— CS Engineer, 2026-06-11
