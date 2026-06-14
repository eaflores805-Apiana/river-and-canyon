# CS Verification — Tier 1 Instrument Repo Structure v0.1

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior, Manager
**In response to:** `MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-VERIFICATION-2026-06-14.md` (Manager direction, this turn)
**Artifact verified:** `governance/2026-06-11_lane-1a-prime/certification-readiness/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.1.md` (sha256 `2048396dd358c03df4e90096afba7cbe5751fe6b3d8cfe3609682ee8d4dc1c69`)

---

## §0. Verdict (Manager's return format)

```text
PASS:
  Structure preserves track separation and is safe to use as the repo-organization plan.
```

The proposed structure cleanly separates the four tracks (Tier-1 instrument / CAL-Q finding / Paper B / D4-closed) into distinct top-level trees, routes every CS-known existing artifact to exactly one home, marks every not-yet-existing artifact as a placeholder, and explicitly reserves `/implementation/` without authorizing a build. Sources of truth are preserved. D4 is contained as history. No structural blocker.

CS surfaces **four informational notes** for an optional v0.2 polish (none rises to HOLD or FAIL):

1. §2 cites `PAPER-A-DRAFT-v1.0.md (464a8889)` — the hash `464a8889…` was the **pre-swap** bundle paper.md; the current canonical Paper A v1.0 source has sha256 `4272e12a…` (and the bundle paper.md was swapped to match, per the prior CS sweep). The actual filename in the revisions chain is `PAPER-A-v1.0.md` (no `-DRAFT-`). Recommend v0.2 update: `PAPER-A-v1.0.md (4272e12a…)`.
2. §5 phrasing on G6 ("G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md → /tier-1-instrument/specs/" and "(and G6 gets a module home) → /tier-1-instrument/modules/g6-standing-rejection-audit/") is correct in intent but could be read as double-homing. Recommend v0.2 wording: "the spec FILE lives in /tier-1-instrument/specs/; the module work directory /tier-1-instrument/modules/g6-standing-rejection-audit/ is a TRACKING home (own README + future design work), not a copy of the spec file."
3. Manager's closed-gate list (15 items) includes "No file moves until separate approval." The substantive rule is in the spec (§0 "moves no bytes by itself"; §5 "This document authorizes the PLAN, not a silent move") but is NOT in the spec's §10 closed-gate list (14 items). Recommend v0.2 add the move-closure line to §10 for completeness.
4. §5's existing-artifact table enumerates the major items (Paper A bundle, Tool Spec, G6 Spec, CAL-Q plan, paper governance memos, CS verification memos, INDEX). It does NOT explicitly enumerate dozens of in-flight `certification-readiness/` artifacts (TIER-1-PRIOR-ART-AND-AUDIENCE-CHECK, POST-D4-STRATEGIC-POSITION, BASELINE-GATE-DIAGNOSIS-*, CAL-A/B/C/E artifacts, MANAGER-DIRECTIONs, the v0.6–v1.0 paper revision chain, etc.). The "one track, one directory tree" routing rule handles them implicitly, but the actual move (separately authorized) will need a complete artifact-inventory + per-file routing pass. Not a structure defect; a move-time discipline note.

These notes are informational. The structure as written can be approved.

---

## §1. Anchor and sealed-bytes posture

Spec §0 anchors on `origin/main HEAD efefc0b` — current at draft time (matches my most recent push). Sealed bytes UNCHANGED (≈71st survival check):

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`) UNCHANGED.

## §2. Required checks (Manager §"Required checks", items 1–15)

| # | Check | Spec evidence | Verdict |
|---|---|---|---|
| 1 | Paper A release artifacts have a clear home under `/papers/paper-a-before-retention/` | §3 defines `/papers/paper-a-before-retention/` with README + CITATION.cff + paper/ + figures/ + sections/ + supplement/ + governance/. §4: "the FINISHED Paper A release, exactly as bundled for GitHub. This tree is a completed deliverable; it is not edited as part of instrument work. It is the instrument's SOURCE OF TRUTH but lives in its own track so instrument churn never touches the released paper." | **PASS** |
| 2 | Tier 1 instrument artifacts have a clear home under `/tier-1-instrument/` | §3 defines `/tier-1-instrument/` as a top-level directory with README + ROADMAP + specs/ + schemas/ + modules/ + human-read-templates/ + examples/ + implementation/ + archive/. §4: "The ACTIVE track: the reusable validity-gate architecture and its module specs, plus reserved homes for schemas, templates, examples, and (future) implementation." | **PASS** |
| 3 | Tool Spec v0.1 and G6 Spec v0.1 route under `/tier-1-instrument/specs/` | §3 specs/: `eval-validity-gate-tool-spec-v0.1.md`, `g6-standing-rejection-audit-spec-v0.1.md`, README.md (index + CS-verification status). §5: both spec files mapped to `/tier-1-instrument/specs/`. | **PASS** |
| 4 | Future schemas / modules / human-read templates / examples / implementation stubs clearly marked as placeholders | §3 marks schemas/ "(PLACEHOLDER until extracted)", schemas/README "schemas currently embedded in specs §4/§5/§7/§9; extraction is future"; human-read-templates/ "(PLACEHOLDER — none drafted)"; examples/ "(PLACEHOLDER)"; implementation/ "(PLACEHOLDER — EXPLICITLY NOT A BUILD)". §4 reinforces all. §7 explicit: "files do not exist yet; extracting them from the specs is a future documentation step." | **PASS** |
| 5 | `/implementation/` is reserved only and does not imply a software build | §3 implementation/: "future code/pseudo-interface (PLACEHOLDER — EXPLICITLY NOT A BUILD)" / README: "no software here yet; G6 impl DESIGN is the next model-free target." §4: "reserved for future pseudo-interface / code. EXPLICITLY NOT A BUILD today; holds only a stub README until separately authorized." §7: "/tier-1-instrument/implementation/ is a RESERVED, EMPTY location with a stub README. Creating the directory is not starting a build; it is reserving where a future, separately-authorized build would live." | **PASS** |
| 6 | CAL-Q finding-track artifacts route under `/finding-tracks/cal-q-format-sensitive-abstention/` | §3 `/finding-tracks/cal-q-format-sensitive-abstention/`: `cal-q-finding-diagnostic-plan-v0.1.md` + README. §5: CAL-Q plan mapped to that exact path. | **PASS** |
| 7 | CAL-Q is not filed as a D4 rescue | §3 README content for the finding-track dir: "NOT Tier 1; NOT a D4 rescue." §4: "Explicitly NOT part of the Tier 1 instrument and explicitly NOT a D4 rescue." | **PASS** |
| 8 | Paper B planning is separate under `/paper-b/planning/` | §3 `/paper-b/planning/`: README "no artifacts yet; requires separate authorization; stress work, not spec work." §4: "Future Paper B: the certified-baseline → compression-stress → retention-interpretation loop. DEFERRED; requires separate authorization; this is stress work (it will need runs when authorized), distinct from the model-free spec work." | **PASS** |
| 9 | D4 materials route only to historical archive | §3 `/archive/d4-closed-route/`: README "D4 is closed as a certification-readiness route; here for history; NOT reopened." §4: "D4 historical evidence ONLY. … Retained for provenance; never reopened by anything in this structure." §6: "D4 materials: HISTORICAL ONLY in /archive/d4-closed-route/. Closed route; kept for provenance; not reopened." | **PASS** |
| 10 | D4 remains closed and is not reopened by this structure | §4, §6, §10 all preserve D4 closure. No directory provides a path that would reopen D4 (no `/d4/active/` or `/d4/redesign/`); only the archive home exists. | **PASS** |
| 11 | No artifact is double-homed | §5 maps each existing artifact to exactly one destination. G6 has both a spec-file home (`/tier-1-instrument/specs/`) AND a module-work directory (`/tier-1-instrument/modules/g6-standing-rejection-audit/`) — but per §3 the module dir holds a README + future design work, NOT a copy of the spec file. This is not double-homing the spec FILE; it is one file (in /specs/) plus a sibling module-tracking directory. **Wording in §5 could be tighter** (see §0 informational note 2), but the structure itself does not double-home any artifact. | **PASS** (with §0 note 2) |
| 12 | No existing artifact is dropped | §5 enumerates the major existing artifacts (Paper A bundle + governance, Tool Spec, G6 Spec, CAL-Q plan, CS verification memos, INDEX). The "one track, one directory tree" principle (§3 organizing line) provides a routing rule for unenumerated artifacts. **Move-time risk** (see §0 informational note 4): the existing `certification-readiness/` directory contains dozens of additional in-flight artifacts not explicitly listed in §5; a complete artifact-inventory + per-file routing pass will be needed when the move is separately authorized. As a STRUCTURE check (this verification), §5's table + the routing rule together are sufficient to avoid silent drops; as an EXECUTION check (move-time), CS will need to re-verify a complete inventory. | **PASS** (with §0 note 4) |
| 13 | Paper A / Tool Spec / G6 Spec remain sources of truth for their respective tracks | §0: "Paper A v1.0, the Tool Spec v0.1, and the G6 spec v0.1 are the sources of truth." §2 NOTABLE: "the spec remaining the source of truth." §7: "the specs remain the source of truth either way." §9: "Paper A / Tool Spec / G6 remain the sources of truth." Four reaffirmations across the document. | **PASS** |
| 14 | Schema files are described as future lifts from specs, not as existing artifacts | §2 NOTABLE: "schemas (route-decision, evidence-packet, quarantine) currently live EMBEDDED INSIDE the Tool Spec (§4/§5/§7) and G6 (§9), not as standalone files. … EXTRACTING them into standalone schema files is a future, separately-directed step (a schema file would be a faithful lift from the spec, with the spec remaining the source of truth)." §3 schemas/ marked PLACEHOLDER until extracted; schemas/README explicit. §4 schemas/: "lifted from the specs … PLACEHOLDER until extraction is directed." §7: "schemas/ files do not exist yet; extracting them from the specs is a future documentation step, not a build, and the specs remain the source of truth either way." Four reaffirmations. | **PASS** |
| 15 | The structure implies no model execution / software build / benchmark packaging / public/funder release | §0: "Authorizes no software build and no model execution." §7: "This document is ORGANIZATION. It creates no software and runs no model." §10 closed-gate list: 14 items including "No software implementation / No public benchmark packaging / No funder-facing release / No SBIR submission / No model execution." §8: the named "next model-free target" (G6 implementation design) is explicitly framed as model-free design, NOT code or a run, and "This document does NOT draft that target; it only reserves its home and names it as next." | **PASS** |

All 15 numbered checks: **PASS** (with the four §0 informational notes flagged on items 11, 12, and on the version-reference quality of §2 and the §10 list composition).

## §3. Closed-gates perimeter (Manager §"Closed gates")

| Manager-required closure | Spec §10 entry | Match |
|---|---|---|
| No model execution | No model execution | **Match** |
| No new run | No new run | **Match** |
| No D4 rescue | No D4 rescue | **Match** |
| No CAL-Q rerun | No CAL-Q rerun | **Match** |
| No certification run | No certification run | **Match** |
| No compression | No compression | **Match** |
| No INT8 / INT4 stress | No INT8 / INT4 stress | **Match** |
| No second compression rung | No second compression rung | **Match** |
| No full ladder | No full ladder | **Match** |
| No Claim C activation | No Claim C activation | **Match** |
| No public benchmark packaging | No public benchmark packaging | **Match** |
| No funder-facing release | No funder-facing release | **Match** |
| No SBIR submission | No SBIR submission | **Match** |
| No software implementation | No software implementation | **Match** |
| **No file moves until separate approval** | NOT in §10 list — but substantively present in §0 ("moves no bytes by itself") and §5 ("This document authorizes the PLAN, not a silent move") | **Substantively PASS, list-omission INFORMATIONAL** (see §0 note 3) |

14 of 15 verbatim in §10; the 15th is substantively present elsewhere but missing from the closed-gate list itself. **PASS** with §0 note 3.

## §4. Track-separation principle — verified

Manager's organizing principle: "one track, one directory tree, no cross-contamination."

The four tracks land in four distinct top-level trees:

| Track | Top-level tree | Status |
|---|---|---|
| Paper A (FINISHED release) | `/papers/paper-a-before-retention/` | Released, complete, maintained |
| Tier 1 instrument (ACTIVE) | `/tier-1-instrument/` | Spec-stage with placeholders for future modules/schemas/templates/examples/impl |
| CAL-Q finding (SECONDARY future research) | `/finding-tracks/cal-q-format-sensitive-abstention/` | Plan filed; alive but not Tier-1 |
| Paper B (DEFERRED stress work) | `/paper-b/planning/` | Empty + stub README; requires separate authorization |
| D4-closed (HISTORICAL only) | `/archive/d4-closed-route/` | Closed route; here for provenance; not reopened |

No directory cross-references force a track-blur (e.g., no `/tier-1-instrument/d4-residuals/` or `/finding-tracks/tier-1-overlap/`). The structure operationalizes Manager's principle. **PASS.**

## §5. Standard forbidden-phrasings perimeter — PASS

Grep across the structure spec for the standard binding-forbidden phrasings (`model passed` / `capability established` / `candidate certified` / `task family viable` / `Claim C progressed` / `seam evidence` / `public benchmark result` / `certification achieved` / `compression-robust` / `not shortcut-driven` / `breadth passed`). **Zero matches.**

The spec is purely organizational and does not assert any of the forbidden claims. **PASS.**

## §6. File-move boundary observed

Per Manager: "This direction does NOT authorize file moves yet. … Actual git moves, if any, should be a separate CS-checkable step after Manager approval."

CS has not moved any file in response to the structure spec. This CS verification creates only three documents (Manager direction filed verbatim, the structure spec filed in `certification-readiness/`, this verification memo) and updates INDEX. The directory `/tier-1-instrument/` is NOT created; the directory `/finding-tracks/` is NOT created; the directory `/paper-b/` is NOT created; the directory `/archive/d4-closed-route/` is NOT created. The current `papers/05_paper-a-before-retention/` directory is NOT renamed. No artifact in `certification-readiness/` is moved. **File-move boundary observed.**

## §7. Final verdict

```text
PASS:
  Structure preserves track separation and is safe to use as the repo-organization plan.
```

**No blockers. Four informational v0.2 polish notes recorded in §0** — none rises to HOLD or FAIL. The structure as written can be approved as the organization plan; the actual move is a separately-authorized step that CS will verify against a complete artifact inventory + hash-preservation check when directed.

CS does NOT decide:
- Whether to approve the structure (Manager — pending this verification).
- Whether to authorize the actual move (Manager — separate step).
- Whether the v0.2 informational notes warrant a v0.2 revision before move-authorization or can be folded into the move-time checklist (Senior + Manager).
- The §8-named "next model-free target" (G6 implementation design): this verification only confirms its home is reserved without implication of authorization (Manager).

— CS Engineer, 2026-06-14
