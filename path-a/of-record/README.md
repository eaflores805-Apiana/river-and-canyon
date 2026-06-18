# Path A — Of-Record

Definition-of-record + locked preregistration for **Path A constructibility**.
Artifacts here are **of-record**: elevated by Manager + Team Lead authorization;
the in-review iterations are retained in `path-a/in-review/` as the version trail.

## Of-record artifacts

| File | sha256 | Status |
|---|---|---|
| `TARGET-CONSTRUCT-DEFINITION-v0.4.md` | `4b616afb919114ee6e0b524e030172cc6f9a96ea8e206fc65bcbd0571eb23c29` | **definition-of-record** for Path A. Gate-before-construction rule surface. v0.4 narrow patches over v0.3: (1) dominance threshold 0.25 promoted from scorer code into the definition (R11, §8.3, checklist #7); (2) real-run fixture-mode guard added (checklist #11). No do-not-alter invariant changed. |
| `PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3.md` | `d9bd9b219badd25901811ddfbb43b811a04750a77723f6a1f076c7dd641f091c` | **superseded by v0.4** (binding-patch successor; instrument byte-binding only). Retained byte-identical as the prior-of-record version trail per the no-history-rewrite discipline. The §15 byte-binding block in v0.3 pins stale inspector/constants digests (`be50c08c…` / `614d185d…`) that no longer exist at HEAD; consult v0.4 below for the corrected, current-HEAD binding. All other v0.3 content carried forward unchanged in v0.4. |
| `PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4.md` | `c61a3256d26e0ed0226e46a60d9b701baddfe3006249db687f221aea57315955` | **preregistration-of-record** (binding-patch successor to v0.3) — **finalized filled bytes**. Re-pins inspector → `cb4b0b60bd6dc2b5…` and constants → `1d761c3d1c56e7ac…` (current HEAD, K-sweep additive sweep-mode patch — REAL-RUN/V3 gate behavior verified preserved by Senior byte-audit and confirmed by CS V3 real-run param-deviation fixture, sole C9 REJECT, `_expected_match: true`). Supersedes `PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.3.md` (sha `d9bd9b21…`). **No values, thresholds, outcome rules, scoring categories, controls, or stop-rules changed; only the two byte-binding digests moved to match HEAD.** Re-lock authority: Manager + Team Lead, 2026-06-16 (`governance/2026-06-16_v3-byte-audit-close/MANAGER-TL-RE-LOCK-v0.4-2026-06-16.md`). **Correction note:** the prior of-record elevation on 2026-06-17 landed the pre-fill binding-patch bytes (sha `bfb4404a…`) which contained the `<v0.3 of-record digest>` placeholder; finalized filled bytes (this row, sha `c61a3256…`) replaced them under TL corrective action 2026-06-17 (`governance/2026-06-16_v3-byte-audit-close/TL-CORRECTIVE-ACTION-FINALIZE-V0.4-2026-06-17.md`). No science change. **Locking this shell does not authorize a run.** A run requires separate Manager by-name authorization with lock-before-look discipline. |
| `PHILOSOPHY-DECISION-RECORD-PATH-A-GATE-STANDARD-v0.1.md` | `2e1b9ee9a37708b4dab9f7cacc1fa7d76abad80caddedd6b690db8c0cd917f5e` | **RATIFIED / FILED decision artifact** — Manager commits to **foreclose-all** as the Path A gate standard (a composition gate is valid only if only traversal can select the answer). **Make-identity-easy** (tags / distinct topics / grouped topology) considered-and-rejected on standard grounds (adds a non-traversal route, weakens the construct the gate measures). **V3** named as the current candidate vehicle that conforms — **not certified**. Floor check remains the empirical question (does hop2 clear its floor under competition on V3?); V3 may still fail; substrate-infeasibility remains a valid outcome and never a license to loosen the standard. Cites v0.4 binding `c61a3256…` (§3). Route (§4): foreclose-all commitment → V3 candidate → build open slots → floor-check prereg → Manager by-name authorization → CS run → SE verification; **each step its own gate; this filing enacts none of them.** Ratification authority: Manager + Team Lead, TL clearance memo 2026-06-17 (`governance/2026-06-17_path-a-philosophy-ratification/TL-CLEARANCE-PHILOSOPHY-RECORD-2026-06-17.md`). **Authorizes NO build, item generation, prompt generation, model run, compression, Claim C, Paper B, capability claim, or mechanism claim.** Path A FP16 K=5 FAIL stays closed. |

## Authority + sequencing

- TL ACTION 2026-06-15 ("Elevate v0.4 and Lock Prereg v0.3") relayed Manager approval.
- Atomic of-record commit: this filing + the `path-a/inspector/constants.py` `DOMINANT_RATE_THRESHOLD_PROVENANCE.status` update from `"FLAGGED FOR PROMOTION"` to `"PROMOTED"` (per the CS prior recommendation to bundle atomically).
- In-review trail preserved at `path-a/in-review/`; README there now marks the elevated bytes with pointers to `path-a/of-record/`.
- **Manager + Team Lead, 2026-06-16 ("Re-Lock of Corrected V3 Instrument Byte Binding")** re-locked the corrected V3 binding as `PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4`, byte-identical to the Senior-drafted binding patch at `path-a/in-review/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4-binding-patch.md` (sha `bfb4404a…`). Scope: instrument byte-binding block only; no values/thresholds/outcome rules/categories/controls/stop-rules changed. Per the re-lock memo, Senior is cleared to draft the philosophy decision record (foreclose-all standard, V3 vehicle, route: audit → build → floor-check) — which remains a decision artifact and does not by itself authorize build or run.

## What this changes

- The dominance threshold (0.25) is now declared in the definition, not buried in scorer code. The provenance flag in `constants.py` reads `"PROMOTED"` referencing v0.4 by digest.
- The real-run fixture-mode guard (`_fixture_mode: true` is inadmissible for real-run pre-registration) is now a definition-level admissibility requirement, complementing the software-level enforcement (inspector C9 + evaluator LOCK_VIOLATION).
- The preregistration shell v0.3 is now the locked declaration; per its §17 stop-rule, no post-hoc change to construction / gate / scoring / invalidators / floor / threshold / dominance threshold / analysis unit after results are seen. Re-runs require a new locked pre-registration.

## What this does NOT change / authorize

- **NOT a certified baseline** — definition v0.4 defines the bar a run must clear; locking the prereg does not meet it.
- **NOT a run authorization** — model execution requires separate Manager by-name authorization.
- **NOT Claim C / Paper B / compression / capability / mechanism claim** of any kind.
- The substrate-infeasibility branch (definition §8.5) remains pre-committed but does NOT fire from a single run.

## Boundaries (carried)

```text
no items ; no concrete token lists ; no prompt templates ; no model run ;
no compression rung ; no certified baseline ; no Claim C ; no Paper B ;
no model-capability claim ; no mechanism / architecture / training-distribution claim.
```

— CS Engineer, 2026-06-15 (filed under TL ACTION + Manager approval for of-record elevation)

**Elevation addendum 2026-06-17:** `PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4.md` elevated to of-record byte-identical to the Senior-drafted in-review binding patch, per Manager + Team Lead re-lock memo dated 2026-06-16 (`governance/2026-06-16_v3-byte-audit-close/MANAGER-TL-RE-LOCK-v0.4-2026-06-16.md`). v0.3 remains in this directory marked as superseded — retained byte-identical as the prior-of-record version trail per the no-history-rewrite discipline (corrections file as superseding commits).

— CS Engineer, 2026-06-17

**Corrective addendum 2026-06-17:** the initial elevation above landed the *pre-fill* binding-patch bytes (sha `bfb4404a…`) which contained the `<v0.3 of-record digest>` placeholder Senior had not yet filled. Per TL corrective action 2026-06-17 (`governance/2026-06-16_v3-byte-audit-close/TL-CORRECTIVE-ACTION-FINALIZE-V0.4-2026-06-17.md`), both the of-record copy here and the in-review copy at `path-a/in-review/PREREGISTRATION-PATH-A-CONSTRUCTIBILITY-v0.4-binding-patch.md` were replaced byte-identical with Senior's **finalized filled** v0.4 bytes (sha `c61a3256d26e0ed0226e46a60d9b701baddfe3006249db687f221aea57315955`). The finalized bytes fill the placeholder with the v0.3 of-record digest `d9bd9b219badd25901811ddfbb43b811a04750a77723f6a1f076c7dd641f091c`. **No values, thresholds, outcome rules, scoring categories, controls, stop-rules, or forbidden interpretations changed.** Clerical correction only.

— CS Engineer, 2026-06-17

**Philosophy decision record addendum 2026-06-17:** `PHILOSOPHY-DECISION-RECORD-PATH-A-GATE-STANDARD-v0.1.md` (sha `2e1b9ee9a37708b4dab9f7cacc1fa7d76abad80caddedd6b690db8c0cd917f5e`) filed of-record per Manager + Team Lead clearance (`governance/2026-06-17_path-a-philosophy-ratification/TL-CLEARANCE-PHILOSOPHY-RECORD-2026-06-17.md`). Status: **RATIFIED / FILED**. The record commits foreclose-all as the Path A gate standard, names V3 as the conforming candidate vehicle (not certified), and records make-identity-easy as considered-and-rejected. It is a decision artifact only — it does not authorize build, item generation, prompt generation, model run, compression, Claim C, Paper B, capability claim, or mechanism claim. The floor check remains the empirical question; V3 may still fail; substrate-infeasibility is a valid outcome. Each step in the §4 route requires its own gate; this filing enacts none of them.

— CS Engineer, 2026-06-17
