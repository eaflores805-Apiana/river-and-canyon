# CS Verification — Tier 1 Instrument Repo Structure v0.2

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior, Manager
**In response to:** `MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.2-VERIFICATION-2026-06-14.md` (Manager direction, this turn)
**Artifact verified:** `governance/2026-06-11_lane-1a-prime/certification-readiness/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.2.md` (sha256 `bc9a4014d7ac1dcb88380798517f95178555639bf1cdbc71bb34fb292905a31c`)

---

## §0. Verdict (Manager's return format)

```text
PASS:
  v0.2 resolves prior polish notes and is safe to use as the repo-organization plan.
```

All four prior CS polish notes from v0.1 are resolved. Four-track separation intact. Placeholder honesty preserved. Source-of-truth hierarchy explicit. File-move boundary observed (CS moved no file this turn). No structural blocker.

CS surfaces **two minor informational notes** for an optional v0.3 polish (neither rises to HOLD or FAIL):

1. **Header/version-line mismatch.** Line 1 of v0.2 still reads `# TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.1` while the version block on line 3 says `**Version:** v0.2`. Recommend v0.3 update line 1 to `v0.2`. (Same class of issue as the recurring header/footer mismatch CS previously caught on Paper A v0.4/v0.5.)
2. **v0.2 §2 introduces a "working master PAPER-A-DRAFT-v1.0.md (464a8889)" line.** No such file exists in the repo: the sha256 `464a8889…` was the pre-swap bundle `paper.md`, which was overwritten by the v1.0 source (`4272e12a…`) during the prior bundle-swap commit. There is no `PAPER-A-DRAFT-v1.0.md` (with `-DRAFT-`) anywhere in the library, and the `464a8889` sha is no longer present on disk. The release-artifact attribution in §2/§5 (Manager check #1) IS correctly done; the additional working-master line introduces a phantom file that could confuse a move-time inventory pass. Recommend v0.3 either remove this line or replace it with a note that the prior `464a8889` paper.md has been superseded and is retained only as a hash reference.

Beyond these two notes, v0.2 is clean. The structure can be approved.

---

## §1. Anchor and sealed-bytes posture

Spec §0 anchors on `origin/main HEAD efefc0b` — one commit stale (current HEAD after the prior v0.1-verification commit is `7c4f4c2`). Intervening commit added only the v0.1 spec + its Manager direction + its CS verification; no anchor-load-bearing content shifted. Sealed bytes UNCHANGED (≈72nd survival check):

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`) UNCHANGED.

## §2. Required verification — four prior notes resolution

| Prior note | Manager-required v0.2 fix | v0.2 evidence | Verdict |
|---|---|---|---|
| 1 (Paper A reference) | release artifact is `PAPER-A-v1.0.md`; no `-DRAFT-` in release filename; canonical sha256 `4272e12a…` | §2: "the release artifact is `PAPER-A-v1.0.md` (paper.md in the bundle, sha256 `4272e12a…`; note: no '-DRAFT-' in the release filename)." §5: "`PAPER-A-v1.0.md (release artifact) + paper-a/ bundle  ->  /papers/paper-a-before-retention/`." Release-artifact filename and sha both corrected. | **PASS** (with §0 note 2 on the extra "working master" line) |
| 2 (G6 routing language) | spec FILE → `/specs/`; module-work directory → `/modules/`; not treated as the same thing | §5: "`G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md (spec FILE)  ->  /tier-1-instrument/specs/`" with parenthetical "(G6 also gets a module-WORK directory for design/status -> /tier-1-instrument/modules/g6-standing-rejection-audit/ as it moves spec → design → impl; the spec FILE stays in /specs/ and is referenced from the module directory)." Distinction between FILE and DIRECTORY now explicit and unambiguous. | **PASS** |
| 3 (Closed gates) | "No file moves until separately approved" appears in §10 | §10 final line (verbatim): "No file moves until separately approved." | **PASS** |
| 4 (Move-time inventory) | before reorganization, CS must produce complete artifact inventory including unenumerated `certification-readiness/` materials; no artifact may be dropped, duplicated, or routed into the wrong track | §5 closing NOTE: "MOVE-TIME INVENTORY (per CS): this table enumerates the MAJOR artifacts. When the move is authorized, it must be preceded by a COMPLETE artifact-inventory pass — the `governance/.../certification-readiness/` tree alone holds dozens of unenumerated run-record and rescore files that must each be routed under the 'one track, one directory tree' rule (most are Paper A / D4-historical evidence). No file is moved until that full inventory is reconciled against this structure." | **PASS** |

All four prior notes **fully resolved**.

## §3. Track-separation check (Manager §"Track-separation check")

Manager-required four-track destinations match spec §3 verbatim:

| Track | Manager-required path | Spec §3 path | Match |
|---|---|---|---|
| Paper A | `/papers/paper-a-before-retention/` | `/papers/paper-a-before-retention/` | **Exact** |
| Tier 1 instrument | `/tier-1-instrument/` | `/tier-1-instrument/` | **Exact** |
| CAL-Q finding | `/finding-tracks/cal-q-format-sensitive-abstention/` | `/finding-tracks/cal-q-format-sensitive-abstention/` | **Exact** |
| Paper B | `/paper-b/planning/` | `/paper-b/planning/` | **Exact** |
| D4 history | `/archive/d4-closed-route/` | `/archive/d4-closed-route/` | **Exact** |

Manager-required confirmations:

| Manager-required confirmation | Spec evidence | Verdict |
|---|---|---|
| Paper A remains a finished release, not an active instrument workspace | §4: "the FINISHED Paper A release, exactly as bundled for GitHub. This tree is a completed deliverable; it is not edited as part of instrument work." | **PASS** |
| Tier 1 instrument is the active tool-spec and module-spec track | §4: "The ACTIVE track: the reusable validity-gate architecture and its module specs, plus reserved homes for schemas, templates, examples, and (future) implementation." | **PASS** |
| CAL-Q finding diagnostics remain secondary future research | §3 CAL-Q dir comment: "SECONDARY, future research." §4: "The CAL-Q finding track: future research on whether abstention is format-sensitive / difficulty-coupled. SECONDARY." | **PASS** |
| CAL-Q is not filed as D4 rescue | §3 CAL-Q README content: "NOT Tier 1; NOT a D4 rescue." §4: "Explicitly NOT part of the Tier 1 instrument and explicitly NOT a D4 rescue." | **PASS** |
| Paper B remains deferred stress-rung planning only | §3 `/paper-b/planning/` README: "no artifacts yet; requires separate authorization; stress work, not spec work." §4: "DEFERRED; requires separate authorization; this is stress work (it will need runs when authorized), distinct from the model-free spec work." | **PASS** |
| D4 remains historical archive only and is not reopened | §3 D4-archive README: "D4 is closed as a certification-readiness route; here for history; NOT reopened." §4: "D4 historical evidence ONLY. … Retained for provenance; never reopened by anything in this structure." §6: "D4 materials: HISTORICAL ONLY in /archive/d4-closed-route/. Closed route; kept for provenance; not reopened." | **PASS** |

All six confirmations: **PASS.** Four-track separation **intact**.

## §4. Placeholder honesty check (Manager §"Placeholder honesty check")

| Manager-required placeholder marking | Spec evidence | Verdict |
|---|---|---|
| schemas | §3 schemas/: "(PLACEHOLDER until extracted)"; schemas/README: "schemas currently embedded in specs §4/§5/§7/§9; extraction is future." §4: "PLACEHOLDER until extraction is directed." | **PASS** |
| human-read templates | §3 human-read-templates/: "(PLACEHOLDER — none drafted)"; README: "construct-validity read + blind-second-reader protocol; future, model-free." | **PASS** |
| worked examples | §3 examples/: "(PLACEHOLDER)"; README: "e.g. CAL-Q→REFUSE→REFUSAL-CONFIRMED walkthrough; future." | **PASS** |
| implementation stubs | §3 implementation/: "(PLACEHOLDER — EXPLICITLY NOT A BUILD)"; README: "no software here yet; G6 impl DESIGN is the next model-free target." | **PASS** |
| Paper B planning artifacts | §3 `/paper-b/planning/` README: "no artifacts yet; requires separate authorization; stress work, not spec work." | **PASS** |

**`/tier-1-instrument/implementation/` reserved-not-built check:** §3 "(PLACEHOLDER — EXPLICITLY NOT A BUILD)"; §4: "reserved for future pseudo-interface / code. EXPLICITLY NOT A BUILD today; holds only a stub README until separately authorized."; §7: "RESERVED, EMPTY location with a stub README. Creating the directory is not starting a build; it is reserving where a future, separately-authorized build would live." **PASS.**

## §5. Source-of-truth check (Manager §"Source-of-truth check")

| Manager-required source-of-truth statement | Spec evidence | Verdict |
|---|---|---|
| Paper A v1.0 = source of truth for the instrument paper and scope | §0: "Paper A v1.0, the Tool Spec v0.1, and the G6 spec v0.1 are the sources of truth." §4: "It is the instrument's SOURCE OF TRUTH but lives in its own track so instrument churn never touches the released paper." §9: "Paper A / Tool Spec / G6 remain the sources of truth." | **PASS** |
| EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1 = source of truth for Tier 1 tool architecture | §0 (above); §2 NOTABLE: "the spec remaining the source of truth"; §7: "the specs remain the source of truth either way"; §9 (above) | **PASS** |
| G6-STANDING-REJECTION-AUDIT-SPEC-v0.1 = source of truth for G6 module spec | §0 (above); §9 (above); §3 modules/g6-standing-rejection-audit/ uses spec status as canonical reference | **PASS** |
| Schema files (when extracted later) = faithful lifts from specs, NOT independent sources of truth | §2 NOTABLE: "EXTRACTING them into standalone schema files is a future, separately-directed step (a schema file would be a faithful lift from the spec, with the spec remaining the source of truth)." §4: "lifted from the specs." §7: "the specs remain the source of truth either way." §9: "the schemas are described as lifts from them (spec wins on any disagreement)." Four reaffirmations. | **PASS** |

Source-of-truth hierarchy preserved exactly as Manager requires.

## §6. Closed-gates perimeter (Manager §"Closed gates")

Manager's v0.2 closed-gate list (16 items including this turn's two additions: "No file moves" + "No directory creation"):

| Manager-required closure | Spec §10 entry | Match |
|---|---|---|
| No file moves | "No file moves until separately approved." | **Match** (worded as "until separately approved"; substantively equivalent) |
| No directory creation | NOT explicitly in §10 list | **Substantively present, list-omission INFORMATIONAL** — the spec creates no directory by itself (§0: "moves no bytes by itself"; §7: "Creating the directory is not starting a build; it is reserving where a future, separately-authorized build would live" — note this refers to the FUTURE directory creation as part of the move, which is itself gated by "No file moves until separately approved"). A v0.3 could add the literal line for completeness. |
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

15 of 16 verbatim in §10; "No directory creation" is substantively covered by the file-moves closure (creating placeholder directories is part of the move) but is not literally listed. Marked **INFORMATIONAL** — does not block.

## §7. Standard forbidden-phrasings perimeter — PASS

Grep across v0.2 for the standard binding-forbidden phrasings (`model passed` / `capability established` / `candidate certified` / `task family viable` / `Claim C progressed` / `seam evidence` / `public benchmark result` / `certification achieved` / `compression-robust` / `not shortcut-driven` / `breadth passed`). **Zero matches.**

## §8. File-move boundary observed

Per Manager: "This direction does not authorize file moves. Please verify v0.2 only."

CS has not moved any file in response to v0.2. This CS verification creates only three documents (Manager direction filed verbatim, the v0.2 structure spec filed in `certification-readiness/`, this verification memo) and updates INDEX. No directory is created at `/tier-1-instrument/`, `/finding-tracks/`, `/paper-b/`, or `/archive/d4-closed-route/`. The current `papers/05_paper-a-before-retention/` directory is NOT renamed. No artifact in `certification-readiness/` is moved. **File-move boundary observed.**

The v0.1 spec is retained on disk (supersede-don't-rewrite). v0.2 is filed alongside v0.1; both versions are tracked.

## §9. Final verdict

```text
PASS:
  v0.2 resolves prior polish notes and is safe to use as the repo-organization plan.
```

**No blockers.** All four prior CS polish notes from v0.1 fully resolved. Four-track separation intact. Placeholder honesty preserved. Source-of-truth hierarchy explicit. Forbidden-language perimeter clean. File-move boundary observed.

**Two minor informational v0.3 polish notes** (neither rises to HOLD or FAIL):
1. Line-1 title still reads `v0.1` though version block says `v0.2` (header/version-line mismatch).
2. §2 "working master PAPER-A-DRAFT-v1.0.md (464a8889)" references a file that does not exist in the library (the `464a8889` sha was the pre-swap bundle `paper.md`, now superseded by `4272e12a…`).

CS does NOT decide:
- Whether to approve v0.2 as the structure plan (Manager — pending this verification's PASS).
- Whether to authorize the complete artifact inventory for move planning (Manager — Manager's next decision per direction).
- Whether the two v0.3 polish notes warrant a v0.3 revision before inventory authorization (Senior + Manager — both are cosmetic; can be addressed in v0.3 or folded into move-time discipline).
- The eventual move authorization (Manager — separate step from inventory).

— CS Engineer, 2026-06-14
