# Packet-Stage Concern Register v0.1 — Lane 1a′

```text
DRAFT / REVIEW ONLY
D2 PACKAGE-ASSEMBLY ARTIFACT
NO D2 AUTHORIZATION GRANTED
NO EXECUTION AUTHORIZED
NO SWEEP_ID CREATED
NO MODEL RUNS
NO DATA GENERATED
NO VALIDATION OUTPUTS POPULATED
```

From: CS Engineer
To: Team Lead, New Senior Engineer
Cc: Senior Engineer, Contributor 5, Contributor 6, Manager
Date: 2026-06-11
Re: Packet-Stage Concern Register v0.1 — Lane 1a′ (D2 package-assembly artifact)
Status: First version; consolidated catalog of all packet-stage concerns with proposed dispositions

---

## 1. Scope

This register catalogs every packet-stage concern raised during the
Lane 1a′ design-proposal / D1 packet-preparation / D2 package-assembly
cycle, with the proposed disposition for each. It is the
single-source-of-truth for what the D2 review must consider and what
must follow into D3 / D4 / D5.

Per Team Lead D2 package assembly authorization §7: "CS owns ...
implementation concern register." CS owns this artifact.

Per Team Lead §4 (carry-forward concerns): every AL-* item, every
CS note (IS-7/8/9), and every OPT-* item is dispositioned here.

---

## 2. CS alignment carry-forward concerns (AL-*)

These six concerns emerged from CS's D1 Bundle interface alignment
(commits `f32646f` and `47c744d`) and have been incorporated into the
D2 package-assembly CS artifacts.

| ID | Concern | Source | v0.2 disposition | Location | Status |
|---|---|---|---|---|---|
| **AL-Q1** | Standalone-runner skeleton exposes a no-model assembly dry-run | CS v0.1 alignment Q1 | **INCORPORATED**: `render_prompt()` interface + `--dry-run` wrapper flag added | CS-EP v0.2 §3.1 | RESOLVED for D2 |
| **AL-Q2-schema** | Layer-2 schema enforcement of the no-elimination-references-scrambled-control rule (sidecar + per-rung schema enum + `additionalProperties: false`) | CS v0.1 alignment Q2 | **INCORPORATED**: schemas with closed-enum on elimination basis policies; control names structurally unrepresentable | CS-EP v0.2 §7.2 | RESOLVED for D2 |
| **AL-Q4** | `copy_completion` agreement-rate diagnostic placement | CS v0.1 alignment Q4 | **INCORPORATED**: diagnostic-sidecar pattern; `DIAGNOSTIC` artifact label; typed-boundary disjoint from union envelope | CS-EP v0.2 §5.1; Non-Auth v0.2 §6 | RESOLVED for D2 |
| **AL-Q5-opt** | LOCK-RECORD optional per-table validation_artifact_hashes sub-block | CS v0.1 alignment Q5 (offered as optional) | **INCORPORATED** per Team Lead D2 carry-forward request | LOCK-RECORD v0.2 §2.1 | RESOLVED for D2 |
| **AL-INH-1** | CS co-ownership of per-stratum aggregation semantics (INH-1) | CS v0.1 alignment §2 edit #3 | **ACCEPTED**: CS co-owns analysis-script per-stratum aggregation; joint disposition with NS at D2 decision memo | T4 row INH-1 (NS Bundle v0.3 §V) + CS-EP analysis_script | RESOLVED for D2 (co-ownership confirmed); SUBSTANTIVE DISPOSITION pending joint proposal |
| **AL-INH-2** | CS co-ownership of outcome-chooser totality (INH-2) | CS v0.1 alignment §2 edit #3 | **ACCEPTED**: CS co-owns outcome-chooser code + fixed-language emission; joint disposition with NS at D2 decision memo | T4 row INH-2 (NS Bundle v0.3 §V) + CS-EP outcome_chooser | RESOLVED for D2 (co-ownership confirmed); SUBSTANTIVE DISPOSITION pending joint proposal |

---

## 3. CS notes (IS-*)

These three CS notes were added during the CS v0.2 review of the Lane
1a′ Design Proposal. NS Bundle v0.3 §I.4 + Part II A6 block now cite
each one inline by name.

| ID | Concern | v0.2 disposition | Location | Status |
|---|---|---|---|---|
| **IS-7** | A6 drift tolerance must be pre-declared per anti-tuning rule | **CLARIFIED**: `declared_drift_tolerance` field present in T1 A6 drift block (NS Bundle v0.3 Part II); CS-EP v0.2 §8 verifies pre-declaration timestamp at packet seal | CS-EP v0.2 §8; NS Bundle v0.3 Part II A6 block | RESOLVED for D2 (slot declared; value declared at packet stage) |
| **IS-8** | Operation-equivalence consequence requires lock-time hard refusal at code level | **CLARIFIED**: NS Bundle v0.3 §I.4 inline cites "(IS-8: CS implements this as a lock-time hard refusal at code level — a battery containing an operation-equivalent policy cannot seal.)"; CS-EP v0.2 §9 implements as `PacketLockRefused` raise | CS-EP v0.2 §9; NS Bundle v0.3 §I.4 | RESOLVED for D2 |
| **IS-9** | Equality-predicate veto path reservation | **CLARIFIED**: NS Bundle v0.3 §I.4 inline cites "(IS-9: CS retains a reserved veto/stricter-rule path on this predicate through packet review)"; CS proposes no stricter rule at v0.2 | CS-EP v0.2 §4; NS Bundle v0.3 §I.4 | RESOLVED for D2 (reservation recorded; CS does not exercise at v0.2; reserves through packet review) |

---

## 4. NS Bundle v0.2 → v0.3 packet-stage concerns (Bundle §VI items)

NS Bundle v0.3 §VI enumerates open issues; each is dispositioned here.

| ID | Concern | v0.2 / v0.3 disposition | Location |
|---|---|---|---|
| Bundle §VI #1 | Prompt-shell visibility for `unconditioned_token_prior` (drives baseline derivation) | OPEN; **joint recommendation to accompany D2 decision memo** (NS + CS co-draft) | T2 plan + CS-EP §4 manifest interface admits the field |
| Bundle §VI #2 | T1 cap values + statistical rationale | OPEN; declared at packet stage pre-pilot; D2 reviews the declarations, not results | T1 plan (NS) + CS-EP §8 reads declared values |
| Bundle §VI #3 | INH-1 / INH-2 / INH-3 dispositions | OPEN; INH-1/2 disposition proposals to be co-drafted by NS + CS for D2 decision memo; INH-3 Wilson is a **proposal**, not a selection | T4 (NS Bundle v0.3 §V) |
| Bundle §VI #4 | D4 token-prior gate | OPEN; opened by name at sweep-execution authorization only; LOCK-RECORD §2 `token_prior_authorization` slot present | LOCK-RECORD v0.2 §2 + §5 |
| Bundle §VI #5 #3 (mixture-oracle ceremony) | Mixture-oracle commit-and-hash ceremony | OPEN; CS-EP §11 sibling-artifact tests bind mixture-oracle hash into LOCK-RECORD; ceremony spec at T1 plan | CS-EP v0.2 §11 |
| Bundle §VI #5 #4 (A6 mechanics) | A6 final-manifest re-verification mechanics | RESOLVED (structure); concrete tolerance value at T1 plan | CS-EP v0.2 §8 |
| Bundle §VI #5 #5 (ideal-witness format) | Synthetic ideal-witness record format | OPEN at NS T3 plan; CS-EP §15 reserves test class | T3 plan (NS Bundle v0.3 §IV) |
| Bundle §VI #5 #6 (pilot-log template location) | Pilot-iteration logging schema/template location | RESOLVED: `governance/standing/templates/` post-PA-3 from addendum adoption | CS-EP v0.2 §13 |
| Bundle §VI #5 #7 (evidence-bundle labels) | Validation artifact labels + evidence-bundle exclusion | RESOLVED: `SYNTHETIC` / `RECONNAISSANCE` / `DIAGNOSTIC` labels enforced at code level | CS-EP v0.2 §12; Non-Auth v0.2 §6 |

---

## 5. T4 inherited open items (INH-1/2/3 from v1 close-out)

| ID | Item | Owner | Status | Proposed disposition (at D2 decision memo) |
|---|---|---|---|---|
| **INH-1** | Per-diagnostic stratum semantics — which diagnostics compute over 96 / 80 / 16; which use per-stratum N_effective | New Senior + CS | OPEN | Co-drafted proposal forthcoming; CS implementation footprint: `manifest_record.stratum` field + per-stratum aggregation in analysis script |
| **INH-2** | Outcome-chooser totality — non-eliminated predicate, RFI-only behavior, inconclusive class, fixed language | New Senior + CS | OPEN | Co-drafted proposal forthcoming; CS implementation footprint: outcome-chooser code; fixed-language emission as typed-string constant |
| **INH-3** | SE interval method — Wilson / Jeffreys / other, never silently Wald | New Senior + CS | OPEN | **Wilson is a proposal for review, not a selection under D1 or D2 package assembly**; final method declared at packet-stage T1 plan |

Per addendum §7 C1: every must-fix is dispositioned before lock. None
of INH-1/2/3 may carry into packet lock without disposition.

---

## 6. Optional implementation suggestions (OPT-*)

Per Team Lead §4: optional suggestions labeled optional and must not
block D2 unless CS or Team Lead elevates them.

| ID | Suggestion | Source | CS recommendation | Status |
|---|---|---|---|---|
| **OPT-1** | Bundle adds 1-sentence link to CS-owned D1 artifacts so the work-trail closes both directions | CS v0.1 alignment | NS Bundle v0.3 Part VIII achieves this via cross-review record (`47c744d`); OPT-1 effectively addressed | RESOLVED via §VIII |
| **OPT-2** | T4 table adds `commit_or_file_reference` column per addendum C1 schema | CS v0.1 alignment | Nice-to-have at packet stage when T4 starts receiving non-INH rows from packet reviews | OPEN; non-blocking |
| **OPT-3** | T1 A6 drift block pairs with IS-7 pre-declared tolerance values placeholder | CS v0.1 alignment | NS Bundle v0.3 Part II A6 block now contains the `declared_drift_tolerance` field per IS-7 — OPT-3 effectively addressed | RESOLVED via §II |

OPT-2 remains the only OPT-* in OPEN status. CS does not elevate it
to a D2 blocker; it can land at packet stage when T4 receives its
first packet-review row.

---

## 7. Summary: D2 status

| Item class | Total | RESOLVED for D2 | OPEN at D2 | OPEN past D2 |
|---|---|---|---|---|
| AL-* (CS alignment) | 6 | 6 | 0 | 0 |
| IS-* (CS notes) | 3 | 3 | 0 | 0 |
| Bundle §VI (NS open issues) | 9 | 5 | 4 | 0 |
| T4 INH-* (v1 close-out inherited) | 3 | 0 | 3 | 0 |
| OPT-* (optional) | 3 | 2 | 1 (non-blocking) | 0 |
| **Total** | **24** | **16** | **8** | **0** |

**Eight items remain OPEN at D2 review time.** None blocks the D2
review; rather, the D2 review is precisely the gate at which the
Manager reviews these eight items and decides whether to grant D2
packet-preparation / validation-packet authorization.

**Items resolving at D2 review:**
- Bundle §VI #1 (prompt-shell visibility): joint NS+CS recommendation
- Bundle §VI #2 (T1 cap values): NS declared values at packet stage
- Bundle §VI #3 (INH dispositions): co-drafted NS+CS proposals
- Bundle §VI #4 (D4 token-prior gate): remains gated; not resolved at D2; resolved at D4 when Manager opens it by name
- T4 INH-1, INH-2, INH-3: co-drafted dispositions at D2 decision memo

**Items resolving past D2 (post-D2 packet preparation):**
- Concrete values bound into LOCK-RECORD at packet seal (D2 → D3
  transition or later); not under D2 package assembly itself.

---

## 8. Boundaries preserved

```text
No execution authorized.
No new sweep_id.
No model runs.
No data generation.
No execution packet execution.
No offline pilot execution.
No oracle pre-flight execution.
No candidate selection.
No candidate ranking.
No threshold-sheet work.
No certification evaluation.
No stress-retention testing.
No B1 v2.1 implementation.
No Paper 3 revision.
No Claim C activation.
No Fork A reactivation.
No Paper 6 activation.
No public benchmark packaging.
```

All execution gates remain CLOSED.

---

## 9. CS sign-off

```text
Register status:                  v0.1 — first version
D2 authorization granted:         NO
Execution authorized:             NO
sweep_id created:                 NO
Model runs:                       NO
Data generated:                   NO
Validation outputs populated:     NO

Concerns cataloged:               24
Resolved for D2:                  16
Open at D2 (for Manager review):  8
Open past D2 (packet stage):      0

Next:                             Manager D2 decision memo cites this
                                   register as the consolidated view
                                   of what D2 must consider. CS holds
                                   for Team Lead filter on the
                                   assembled D2 package.
```

— CS Engineer, 2026-06-11
