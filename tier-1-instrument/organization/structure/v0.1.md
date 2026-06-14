# TIER-1-INSTRUMENT-REPO-STRUCTURE-v0.1

**Version:** v0.1. River and Canyon program. Tier 1 instrument track organization. 
**Goal:** organize the Tier 1 instrument artifacts as a tool architecture so the program can move Paper → architecture → module specs → eventual implementation without mixing paper artifacts, finding-track diagnostics, closed D4 history, and future Paper B work.
**Status:** MODEL-FREE STRUCTURING. Authorizes no software build and no model execution. This document proposes an organization; it moves no bytes by itself (the actual file moves are a separate, CS-checkable step). Paper A v1.0, the Tool Spec v0.1, and the G6 spec v0.1 are the sources of truth. Anchored on origin/main HEAD efefc0b.
**Owner split:** Senior (drafter — model-free; preserve track separation) → CS (verify the structure preserves separation, routes artifacts correctly, implies no build/execution) → Team Lead (route as the Tier-1 organization artifact; keep tracks distinct) → Manager.

---

## 1. Executive summary

The program has produced four standalone artifacts and one released paper, and they currently sit together in a flat working library. As the Tier 1 instrument grows from specs toward an eventual implementation, that flatness risks the program's signature failure mode: drift, where paper artifacts, finding-track research, closed-route history, and future stress work blur together and the tool path stops being legible.

This document proposes a directory structure that gives each of four **distinct tracks** its own home, routes every existing artifact to exactly one place, and marks clearly what is a real artifact versus a placeholder for future work. The organizing principle: **one track, one directory tree, no cross-contamination.** Paper A is a finished release; the Tier 1 instrument is an active spec-stage architecture; the CAL-Q finding track is secondary future research; Paper B is deferred stress work; D4 is closed history. Keeping them separate is what lets the instrument be read *as an instrument* rather than as a pile of program documents.

This is organization only. No spec changes, no claims change, nothing is built.

## 2. Current state

```text
EXISTING ARTIFACTS (real, filed, verified — these get routed):
  Paper A (RELEASED, on GitHub):
    - PAPER-A-DRAFT-v1.0.md  (464a8889) + the paper-a/ GitHub bundle
      (README, CITATION.cff, paper/, figures/, sections/, supplement/, governance/)
    - Paper A governance records: MANAGER-DECISION-PAPER-A-NOW, VENUE-DECISION-MEMO-
      PAPER-A, MANAGER-DECISION-VENUE-OPTION-2
  Tier 1 instrument (SPEC STAGE, CS-verified):
    - EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1.md  (fc0bee3f) — PASS
    - G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md  (2b4cedf8) — PASS
  CAL-Q finding track (SECONDARY):
    - CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1.md  (0c2afbbc) — CS PASS

NOTABLE: the schemas (route-decision, evidence-packet, quarantine) currently live
  EMBEDDED INSIDE the Tool Spec (§4/§5/§7) and G6 (§9), not as standalone files.
  This structure gives them a home; EXTRACTING them into standalone schema files is
  a future, separately-directed step (a schema file would be a faithful lift from the
  spec, with the spec remaining the source of truth).

DOES NOT YET EXIST (placeholders only — directories created empty or with a stub
  README explaining what will live there):
  - standalone schema files; human-read templates; worked examples; implementation
    stubs; Paper B planning artifacts. None of these are drafted; the structure
    reserves their location without implying they exist.
```

## 3. Proposed directory structure

```text
/papers/
  paper-a-before-retention/            # the released Paper A bundle (as on GitHub)
    README.md  CITATION.cff
    paper/        (paper.md + paper.pdf)
    figures/      (fig1, fig2; png + svg)
    sections/     (section masters)
    supplement/   (assembly manifest)
    governance/   (Paper A decision + venue memos)

/tier-1-instrument/
  README.md                            # what the instrument is; the spec→build path; track boundaries
  ROADMAP.md                           # the Paper→architecture→specs→implementation sequence + status
  specs/
    eval-validity-gate-tool-spec-v0.1.md     # the architecture (Tool Spec)
    g6-standing-rejection-audit-spec-v0.1.md # first module spec
    README.md                          # index of specs + their CS-verification status
  schemas/                             # standalone schema lifts (PLACEHOLDER until extracted)
    README.md                          # "schemas currently embedded in specs §4/§5/§7/§9; extraction is future"
    route-decision-schema/             # {pass, needs-repair, quarantine, refuse} (Tool Spec §4)
    evidence-packet-schema/            # EP1-6 (Tool Spec §5) + AR1-7 (G6 §9)
    quarantine-rules/                  # QR1-4 (Tool Spec §7)
  modules/
    g6-standing-rejection-audit/       # G6's home as it moves spec → design → (future) impl
      README.md                        # status: SPECIFIED; next = implementation design (separately directed)
    README.md                          # G1-G9 module register: which IMPLEMENTED-in-paper, which SPECIFIED, which future
  human-read-templates/                # the human-semantic-read procedures (PLACEHOLDER — none drafted)
    README.md                          # "construct-validity read + blind-second-reader protocol; future, model-free"
  examples/                            # worked routing examples (PLACEHOLDER)
    README.md                          # "e.g. CAL-Q→REFUSE→REFUSAL-CONFIRMED walkthrough; future"
  implementation/                      # future code/pseudo-interface (PLACEHOLDER — EXPLICITLY NOT A BUILD)
    README.md                          # "no software here yet; G6 impl DESIGN is the next model-free target"
  archive/                            # superseded Tier-1 drafts (version history; nothing deleted)
    README.md

/finding-tracks/
  cal-q-format-sensitive-abstention/   # the CAL-Q finding track (SECONDARY, future research)
    cal-q-finding-diagnostic-plan-v0.1.md
    README.md                          # "future research on format-sensitive abstention / difficulty coupling; NOT Tier 1; NOT a D4 rescue"

/paper-b/
  planning/                            # future certified-baseline → stress → retention loop (DEFERRED)
    README.md                          # "no artifacts yet; requires separate authorization; stress work, not spec work"

/archive/
  d4-closed-route/                     # D4 historical evidence ONLY (CLOSED route)
    README.md                          # "D4 is closed as a certification-readiness route; here for history; NOT reopened"
```

## 4. What each directory is for

```text
/papers/paper-a-before-retention/
    The FINISHED Paper A release, exactly as bundled for GitHub. This tree is a
    completed deliverable; it is not edited as part of instrument work. It is the
    instrument's SOURCE OF TRUTH but lives in its own track so instrument churn
    never touches the released paper.

/tier-1-instrument/
    The ACTIVE track: the reusable validity-gate architecture and its module specs,
    plus reserved homes for schemas, templates, examples, and (future) implementation.
    README = orientation + track boundaries; ROADMAP = the sequence and current status.
  specs/        the architecture (Tool Spec) and module specs (G6, and future G7-G9).
  schemas/      standalone schema files lifted from the specs — route-decision,
                evidence-packet, quarantine. PLACEHOLDER until extraction is directed.
  modules/      per-module homes (G6 now; G7-G9 later) tracking each module
                spec → design → implementation, plus the G1-G9 register.
  human-read-templates/  the human semantic-read procedures the specs require
                (construct-validity read; blind-second-reader protocol). The point of
                §8/§10 of the specs: these stay human; templates make them repeatable.
  examples/     worked routing walkthroughs for documentation (no model runs).
  implementation/  reserved for future pseudo-interface / code. EXPLICITLY NOT A
                BUILD today; holds only a stub README until separately authorized.
  archive/      superseded Tier-1 drafts, retained (supersede-don't-delete).

/finding-tracks/cal-q-format-sensitive-abstention/
    The CAL-Q finding track: future research on whether abstention is format-
    sensitive / difficulty-coupled. SECONDARY. Explicitly NOT part of the Tier 1
    instrument and explicitly NOT a D4 rescue.

/paper-b/planning/
    Future Paper B: the certified-baseline → compression-stress → retention-
    interpretation loop. DEFERRED; requires separate authorization; this is stress
    work (it will need runs when authorized), distinct from the model-free spec work.

/archive/d4-closed-route/
    D4 historical evidence ONLY. D4 is closed as a certification-readiness route.
    Retained for provenance; never reopened by anything in this structure.
```

## 5. What artifacts move where

```text
ARTIFACT                                          ->  DESTINATION
PAPER-A-DRAFT-v1.0.md + paper-a/ bundle            ->  /papers/paper-a-before-retention/
Paper A governance memos (decision/venue)          ->  /papers/paper-a-before-retention/governance/
EVAL-VALIDITY-GATE-TOOL-SPEC-v0.1.md               ->  /tier-1-instrument/specs/
G6-STANDING-REJECTION-AUDIT-SPEC-v0.1.md           ->  /tier-1-instrument/specs/
  (and G6 gets a module home)                      ->  /tier-1-instrument/modules/g6-standing-rejection-audit/
CAL-Q-FINDING-DIAGNOSTIC-PLAN-v0.1.md              ->  /finding-tracks/cal-q-format-sensitive-abstention/
the CS verification memos for the above            ->  alongside each artifact it verifies
the INDEX.md catalog                               ->  stays at workspace root (it indexes ALL tracks)

NOTE: "move where" describes the TARGET organization. The actual git moves are a
separate execution step that CS should verify (correct destinations, nothing
dropped, hashes unchanged). This document authorizes the PLAN, not a silent move.
```

## 6. What artifacts remain historical / archived

```text
- D4 materials: HISTORICAL ONLY in /archive/d4-closed-route/. Closed route; kept for
  provenance; not reopened.
- Superseded versions (Paper A v0.3–v0.9; any future superseded Tier-1 spec drafts):
  retained under the relevant archive/ (supersede-don't-delete remains the rule).
- The CAL-Q diagnostic plan is NOT archived — it is an ALIVE (if secondary) finding-
  track artifact, and lives in /finding-tracks/, not /archive/.
- Paper A is NOT archived — it is a finished, maintained release in /papers/.
```

## 7. What is explicitly not a build

```text
- This document is ORGANIZATION. It creates no software and runs no model.
- /tier-1-instrument/implementation/ is a RESERVED, EMPTY location with a stub
  README. Creating the directory is not starting a build; it is reserving where a
  future, separately-authorized build would live.
- /tier-1-instrument/schemas/ files do not exist yet; extracting them from the specs
  is a future documentation step, not a build, and the specs remain the source of
  truth either way.
- /paper-b/ holds no artifacts and authorizes no stress run.
- No directory in this structure, by being created, authorizes execution,
  compression, a model run, or a software implementation.
```

## 8. Next model-free build target

```text
Per Manager direction, the next model-free target AFTER this structure is approved is:
    G6 implementation design / pseudo-interface
    (the model-free DESIGN of how G6 would be implemented — interfaces, data flow,
     the independence-channel hookup — NOT code, NOT a run).
It would live in /tier-1-instrument/modules/g6-standing-rejection-audit/ (design)
and, when it reaches pseudo-interface form, /tier-1-instrument/implementation/.
This document does NOT draft that target; it only reserves its home and names it as
next, per the Manager's instruction not to draft it yet unless separately directed.
```

## 9. CS verification checklist

```text
- SEPARATION: that the four tracks (Tier 1 instrument / CAL-Q finding / Paper B /
  D4-closed) are in distinct trees with no artifact double-homed or cross-filed.
- ROUTING: that every existing artifact (§5 table) has exactly one correct
  destination and nothing is dropped; that the actual moves (when executed) preserve
  hashes and change no content.
- PLACEHOLDER HONESTY: that non-existent artifacts (schemas, templates, examples,
  implementation, Paper B) are clearly marked as placeholders/stubs, not implied to
  exist.
- NOT-A-BUILD: that /implementation/ is reserved-empty, that nothing here authorizes
  a build or run, and that the closed gates (§10) are intact.
- SOURCE-OF-TRUTH: that Paper A / Tool Spec / G6 remain the sources of truth and the
  schemas are described as lifts from them (spec wins on any disagreement).
- D4 CONTAINMENT: that D4 is archive/historical only and nothing reopens it; that the
  CAL-Q track is NOT filed as a D4 rescue.
```

## 10. Closed gates (unchanged)

```text
No model execution.       No second compression rung.
No new run.               No full ladder.
No D4 rescue.             No Claim C activation.
No CAL-Q rerun.           No public benchmark packaging.
No certification run.     No funder-facing release.
No compression.           No SBIR submission.
No INT8 / INT4 stress.    No software implementation.
```

This is structuring only. The specs have passed; this organizes the instrument as an instrument, prevents drift, and keeps Paper A, the CAL-Q finding track, and future Paper B work cleanly separated. The next model-free step it points at — G6 implementation design — is separately directed.

— Senior Engineer
