# CS Verification — Tier 1 Instrument Repo Structure v0.3

**Author:** CS Engineer
**Date:** 2026-06-14
**Routed to:** Team Lead → Senior, Manager
**In response to:** `MANAGER-DIRECTION-TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.3-VERIFICATION-2026-06-14.md` (Manager direction, this turn)
**Artifact verified:** `governance/2026-06-11_lane-1a-prime/certification-readiness/TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.3.md` (sha256 `d691ded890d324fc8a418564be93a6b80448ff3af9fb8e51ef279ed55e96c1a0`)

---

## §0. Verdict (Manager's return format)

```text
PASS:
  v0.3 resolves the remaining cleanup notes and is safe to use as the final
  repo-organization plan before artifact inventory.
```

Both v0.2 polish notes are fully resolved. Four-track separation unchanged. G6 routing distinction preserved. Placeholder honesty intact. Move-time inventory requirement intact. Closed gates substantively intact. File-move boundary observed. No structural blocker; no informational notes this turn that warrant further revision.

---

## §1. Anchor and sealed-bytes posture

Spec §0 anchors on `origin/main HEAD efefc0b` — two commits stale (current HEAD after the prior v0.2-verification commit is `b78ae0a`). Intervening commits added only the v0.1 and v0.2 spec packets + their CS verifications; no anchor-load-bearing content shifted. Sealed bytes UNCHANGED (≈73rd survival check):

- `experiments/2026-06-10_lane-1a-sweep/LOCK-RECORD.md` (`5b557ae2…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json` (`7ad3ccdd…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/ORACLE_VERDICT_TABLE.json` (`9c6cbda9…`) UNCHANGED.
- `experiments/2026-06-11_lane-1a-prime/validation/T3_BOUNDS_DECLARATION.json` (`45565d0b…`) UNCHANGED.

## §2. Required checks (Manager §"Required checks", items 1–7)

### §2.1 Check 1 — Header/version consistency

| Element | v0.3 evidence | Verdict |
|---|---|---|
| Line-1 title says v0.3 | `# TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.3` (line 1) | **PASS** |
| Version block says v0.3 | `**Version:** v0.3.` (line 3) | **PASS** |
| No lingering v0.1/v0.2 title mismatch | Line 1 and version block both say v0.3; grep across v0.3 for "v0.1" returns only historical references (the v0.2 footer summary and the v0.3 footer's "lagged at v0.1 across the v0.2 bump"), no live version-self-reference at v0.1/v0.2 | **PASS** |

The v0.3 version block also adds a forward-looking "REVISION CHECK" reminder: *"on every version bump, update the line-1 TITLE and the version block together — title-version lag has recurred."* Good revision-discipline note; not a defect to flag. **Check 1: PASS.**

### §2.2 Check 2 — Paper A routing clarity

| Element | v0.3 evidence | Verdict |
|---|---|---|
| Release artifact remains `PAPER-A-v1.0.md` | §2: "the release artifact is `PAPER-A-v1.0.md`"; §5: "`PAPER-A-v1.0.md (release artifact) + paper-a/ bundle  ->  /papers/paper-a-before-retention/`" | **PASS** |
| Release hash remains `4272e12a…` | §2: "sha256 `4272e12a…`" | **PASS** |
| No `-DRAFT-` release filename introduced | §2: "note: no '-DRAFT-' in the release filename"; grep across v0.3 for `-DRAFT-`: zero live release-artifact uses (only the v0.3-footer's historical mention of the dropped `PAPER-A-DRAFT-v1.0.md` line, where it is now correctly excluded) | **PASS** |
| Prior working-master / `464a8889` reference no longer creates move-time ambiguity | §2 replaces the bonus working-master line with: "(The editable working draft remains in the library and is not a release artifact; only the RELEASE artifact is routed here, to avoid double-counting at move time.)" — no hash citation, no filename, no routing ambiguity. v0.3 footer note #2 explicitly states the rationale: "in a routing document, citing a working-master hash beside the release artifact invites move-time double-counting (the value `464a8889` was also the pre-swap bundle `paper.md` hash, now superseded by the release artifact's `4272e12a`); §2 now routes the release artifact only, removing the ambiguity." | **PASS** |

**Check 2: PASS.** v0.2 polish note #2 fully resolved.

### §2.3 Check 3 — Four-track separation unchanged

| Track | v0.3 §3 path | Match against v0.2/v0.1 | Verdict |
|---|---|---|---|
| Paper A release artifacts | `/papers/paper-a-before-retention/` | Unchanged | **PASS** |
| Tier 1 instrument | `/tier-1-instrument/` | Unchanged | **PASS** |
| CAL-Q finding diagnostics | `/finding-tracks/cal-q-format-sensitive-abstention/` | Unchanged | **PASS** |
| Paper B planning | `/paper-b/planning/` | Unchanged | **PASS** |
| D4 historical archive | `/archive/d4-closed-route/` | Unchanged | **PASS** |

§§3–6 are byte-for-byte unchanged from v0.2 (verified by spot-comparison; the v0.3 diff against v0.2 is confined to line 1 + §2 + the v0.3-footer note). **Check 3: PASS.**

### §2.4 Check 4 — G6 routing remains clear

| Element | v0.3 evidence | Verdict |
|---|---|---|
| G6 spec FILE routes to `/tier-1-instrument/specs/` | §5: "`G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md (spec FILE)  ->  /tier-1-instrument/specs/`" | **PASS** |
| G6 module-work directory routes to `/tier-1-instrument/modules/g6-standing-rejection-audit/` | §5: "(G6 also gets a module-WORK directory for design/status  ->  /tier-1-instrument/modules/g6-standing-rejection-audit/ as it moves spec → design → impl; the spec FILE stays in /specs/ and is referenced from the module directory)" | **PASS** |
| Spec file and module-work directory not treated as same artifact | §5 wording (above) explicit on the distinction; §3 modules/g6-standing-rejection-audit/ holds README only (status + future design), not a copy of the spec file | **PASS** |

§5 wording on the G6 distinction is unchanged from v0.2 (which already PASS-ed on this check). **Check 4: PASS.**

### §2.5 Check 5 — Placeholder honesty intact

| Element | v0.3 evidence | Verdict |
|---|---|---|
| Schemas are future lifts from specs | §2 NOTABLE: "schemas... currently live EMBEDDED INSIDE the Tool Spec (§4/§5/§7) and G6 (§9), not as standalone files... EXTRACTING them into standalone schema files is a future, separately-directed step"; §3 schemas/ "(PLACEHOLDER until extracted)"; §3 schemas/README: "schemas currently embedded in specs §4/§5/§7/§9; extraction is future"; §4 schemas/: "PLACEHOLDER until extraction is directed"; §7 explicit | **PASS** |
| Human-read templates are future | §3 human-read-templates/ "(PLACEHOLDER — none drafted)"; README: "construct-validity read + blind-second-reader protocol; future, model-free" | **PASS** |
| Examples are future | §3 examples/ "(PLACEHOLDER)"; README: "future" | **PASS** |
| Implementation is placeholder only | §3 implementation/ "(PLACEHOLDER — EXPLICITLY NOT A BUILD)"; §4 reaffirms; §7 explicit "RESERVED, EMPTY location with a stub README. Creating the directory is not starting a build" | **PASS** |
| Paper B planning artifacts not implied to exist | §3 `/paper-b/planning/` README: "no artifacts yet; requires separate authorization; stress work, not spec work"; §4 "DEFERRED" | **PASS** |

All §§3/4/7 placeholder markings unchanged from v0.2. **Check 5: PASS.**

### §2.6 Check 6 — Move-time inventory requirement intact

| Element | v0.3 evidence | Verdict |
|---|---|---|
| Before reorganization, CS must produce complete artifact inventory | §5 closing NOTE: "When the move is authorized, it must be preceded by a COMPLETE artifact-inventory pass" | **PASS** |
| Inventory must include unenumerated `certification-readiness/` materials | §5 closing NOTE (continued): "the `governance/.../certification-readiness/` tree alone holds dozens of unenumerated run-record and rescore files that must each be routed under the 'one track, one directory tree' rule (most are Paper A / D4-historical evidence)" | **PASS** |
| No artifact may be dropped, duplicated, or routed into wrong track | §5 closing NOTE (continued): "No file is moved until that full inventory is reconciled against this structure"; "one track, one directory tree" rule applies to every artifact; §9 SEPARATION/ROUTING checklist items reinforce | **PASS** |

§5 closing NOTE byte-identical to v0.2. **Check 6: PASS.**

### §2.7 Check 7 — Closed gates intact

| Manager-required closed-gate | Spec §10 evidence | Verdict |
|---|---|---|
| No file moves | "No file moves until separately approved." | **PASS** |
| No directory creation | NOT literally in §10; substantively closed via §0 ("moves no bytes by itself"), §7 ("Creating the directory is not starting a build; it is reserving where a future, separately-authorized build would live") — the spec itself creates no directory | **Substantively PASS** (literal §10 line still absent; pre-existing INFORMATIONAL, unchanged from v0.2) |
| No software implementation | "No software implementation" | **PASS** |
| No model execution | "No model execution" | **PASS** |
| No D4 rescue | "No D4 rescue" | **PASS** |
| No CAL-Q rerun | "No CAL-Q rerun" | **PASS** |
| No Paper B stress work | NOT literally in §10; substantively closed via §10 closures on its constituent activities (No compression / No INT8 / INT4 stress / No second compression rung / No full ladder / No certification run) + §4 Paper B "DEFERRED; requires separate authorization; this is stress work (it will need runs when authorized)" — Paper B stress work is closed by closure of all its constituent activities and by Paper B being held in `/paper-b/planning/` with no artifacts | **Substantively PASS** (literal line absent; consistent with the closure pattern) |

5 of 7 Manager check-7 items are verbatim in §10; 2 ("No directory creation" and "No Paper B stress work") are substantively closed by structure but not literally listed. This is a pre-existing pattern carried unchanged from v0.2; CS already flagged the "No directory creation" omission as INFORMATIONAL on v0.2 and Manager has not asked v0.3 to address it. **Check 7: substantively PASS** with continuing informational note that §10's literal list could optionally enumerate these two for completeness; not a blocker.

## §3. Standard forbidden-phrasings perimeter — PASS

Grep across v0.3 for the standard binding-forbidden phrasings (`model passed` / `capability established` / `candidate certified` / `task family viable` / `Claim C progressed` / `seam evidence` / `public benchmark result` / `certification achieved` / `compression-robust` / `not shortcut-driven` / `breadth passed`): **zero matches.** v0.3 introduces no new content (the only substantive deltas are line-1 title correction and §2 working-master line removal), so the forbidden-language perimeter is identical to v0.2 (which CS already verified PASS).

## §4. v0.2 → v0.3 diff sanity-check

Per the v0.3 footer note, the v0.3 changes are confined to:
1. Line-1 title corrected from `v0.1` to `v0.3` (one-line change).
2. §2 "working master" bonus line removed; replaced with the routing-only note "(The editable working draft remains in the library and is not a release artifact; only the RELEASE artifact is routed here, to avoid double-counting at move time.)"
3. v0.2 footer summary added (alongside the new v0.3 footer summary).

CS spot-comparison confirms §§3–10 are byte-identical to v0.2. No track-separation change, no routing change, no closed-gate change, no source-of-truth change. The v0.3 diff is exactly the surface CLEANUP pass Manager requested. **No drift.**

## §5. File-move boundary observed

Per Manager: "This direction does not authorize file moves. Closed: No file moves. No directory creation. …"

CS has not moved any file in response to v0.3. This CS verification creates only three documents (Manager direction filed verbatim, the v0.3 structure spec filed in `certification-readiness/`, this verification memo) and updates INDEX. No directory created at `/tier-1-instrument/`, `/finding-tracks/`, `/paper-b/`, `/archive/d4-closed-route/`. The current `papers/05_paper-a-before-retention/` directory is NOT renamed. No artifact in `certification-readiness/` is moved. **File-move boundary observed.**

v0.1 and v0.2 are retained alongside v0.3 (supersede-don't-rewrite). All three versions are tracked.

## §6. Final verdict

```text
PASS:
  v0.3 resolves the remaining cleanup notes and is safe to use as the final
  repo-organization plan before artifact inventory.
```

**No blockers. No new informational polish notes this turn** — the two §2.7 substantive-PASS items (literal "No directory creation" and "No Paper B stress work" lines absent from §10) are pre-existing informational notes carried unchanged from v0.2 and not raised in Manager's v0.3 checklist.

The structure is at PASS through three revisions. Per Manager's "Next decision if PASS" note, the next Manager decision is whether to authorize:

```text
COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.1
```

which is the inventory step (a separate model-free document), not the move itself.

CS does NOT decide:
- Whether to approve v0.3 as the final pre-inventory structure plan (Manager — pending this verification's PASS).
- Whether to authorize `COMPLETE-ARTIFACT-INVENTORY-FOR-REPO-MOVE-v0.1` (Manager — next decision per direction).
- Whether the persistent §10-list-completeness informational notes warrant a v0.4 (Senior + Manager — cosmetic only; can be addressed in v0.4 or folded into the inventory document's closed-gate list).
- Whether the eventual repo move authorization (still a separate later step after inventory).

— CS Engineer, 2026-06-14
