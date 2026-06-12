# Lane 1a′ Prime — Path A Readiness Packet (v0.1.1)

*v0.1.1 patches v0.1 (sha256 `f23b40d0e9f8d9b67b3df73eae4a32ca6efaf39664e8f387cf5ae93e94688cc9`) with the one TL-required generator-path correction: `d4_runner/validation.py` → `lane1a_prime/validation.py`. Generator sha256 (`db69519f…`) unchanged. No other substantive content changed. v0.1 retained.*

```text
PATH A READINESS PACKET — DECISION PREPARATION ONLY; NOTHING EXECUTES; APPROVAL NOT PRESUMED
NO MODEL · NO SWEEP_ID · NO SWEEP EXECUTION · NO TP GENERATIONS · NO QUANTIZATION · CLAIM C INACTIVE
SUPERSESSION REQUIRED: NO — materialization adds new files; no sealed byte changes
```

*New Senior Engineer (design side) with CS values from the D4-A/D4-B records, 2026-06-11. Path A
question, in the accepted criteria-firing form: **do the declared elimination criteria fire across
breadth (L02–L08)?***

## 1. Current sealed instrument state

Sealed LOCK-RECORD v1.0 `51e18fa9…1935` at instrument-state commit `2b17ed9`, byte-identical
through every check since sealing (six and counting). Locked: oracle verdict table `9c6cbda9…` ·
T3 bounds `45565d0b…` · stratified recipe schedule `7ad3ccdd…` (all eight rungs declared:
contamination rates 0.30 / 0.15×3, envelope 0.60, item-label disjointness) · L01 manifests
`afe0e545…` (pilot = final). Per the accepted scope determination: the eight-rung surface lies
within the sealed declarative state; **the eight rung task instances are CS-confirmed buildable
inside the sealed record**; materialization of L02–L08 is the fork this packet specifies.

## 2. D4-B accepted bounded result (carried exactly)

> The instrument did not attach any elimination label under the active six-criterion set.
> Accepted interpretation: the result was not explained by the declared shortcut battery or by the
> candidate's own measured token prior. **This is the strongest permitted interpretation. It may
> not be strengthened.**

Repetition guard remains in force: D4-A and D4-B are two non-eliminations on the same narrow L01
surface; they do not aggregate. Path A does not extend a streak; it asks a new question on seven
new rungs.

## 3. Path A empirical question

Do the declared elimination criteria fire across breadth? Each rung is adjudicated **separately**
under the full six-criterion set; there is no cross-rung aggregation, no composite score, no
"survival count." Criteria firing at any rung is a first-class measured outcome,
three-branch-interpretable by standing rule — not a failure.

## 4–5. Proposed extent and TP status

**Extent: L01–L08.** L01 uses the **sealed manifests** (`afe0e545…`) — never regenerated; the A6
check covers L01 against the seal as in both pilots. L02–L08 are newly materialized per §9.
Per-rung load: 96 records each (80 answerable / 16 NULL per the sealed recipe) → 768 candidate
inferences. **TP status: ACTIVE** (proposed; decided only by the checklist) — one control
generation per item shell per rung under the locked no-bindings template (`af55f975…`) → 768
control generations; 1,536 inferences total. Per-rung candidate-vs-control comparison under the
locked Newcombe–Wilson rule and locked 0.10 margin; the D4-B-measured L01 prior is **not** reused
— each rung's control is measured fresh (the TP guard forbids reuse, and rung shells differ).

## 6–7. Model / runner / framework / decoding proposal

Default posture per Manager §9, no blocker found: Qwen2.5-3B-Instruct **bf16**, snapshot pinned to
the authorized `abee745b…9b20` (computed-equals-authorized pre-flight, B1 v2 routine); `mlx_lm
0.31.3` under the committed Option A pin-substitution chain (re-pin check abort armed); decoding
config hash `a20391d8…` unchanged; single greedy pass; no retries; no adaptive continuation.
**Per-run runner provenance:** a new committed `lane1a_runner_pathA.py` (own file, own hash,
ledger-recorded at execution), carrying the patched report emitter — all four TP fields in every
emitted report, **missing field = abort**, per the grace-spent rule now standing.

## 8–10. Generator, materialization, and manifest-hash plan (the §4 requirements)

```text
generator path:        experiments/2026-06-11_lane-1a-prime/lane1a_prime/validation.py
generator sha256:      db69519f… (hash-pinned; recorded in ledger; ABORT on mismatch at pre-flight)
generation command:    python validation.py --materialize L02-L08 --schedule <sealed schedule path>
                       --seed <locked seed> --out path_a_run/manifests/
locked seed:           declared in this packet's authorized successor (single integer, fixed
                       before any generation; recorded in ledger)
two-pass discipline:   PILOT materialization at readiness-confirmation (post-authorization,
                       pre-model-load) → per-rung sha256 recorded; FINAL materialization
                       immediately before inference → per-rung sha256 recomputed;
                       PILOT must equal FINAL byte-for-byte (locked seed ⇒ deterministic);
                       ABORT on any per-rung mismatch
per-rung hash record:  manifest_L0k.sha256 for k=2..8 written to the execution ledger BEFORE the
                       first inference of that rung; L01 records the sealed hash afe0e545…
A6 drift check:        every rung re-verified post-run against its pre-inference hash; L01
                       additionally against the seal; drift tolerance 0.0 as in both pilots
recipe conformance:    per-rung post-generation audit — counts (80/16), contamination rates vs
                       sealed schedule, item-label disjointness — ABORT on any deviation
```

**Supersession determination: NONE REQUIRED.** Materialization writes new files under
`path_a_run/manifests/`; the sealed L01 manifests, schedule, bounds, and oracle table are read,
never written. If any step were found to require changing a sealed byte, the run stops and a
supersession requirement returns to the Manager instead of execution — that stop-rule is armed in
the runner's pre-flight.

## 11–12. Output directory and sweep_id proposals

`experiments/2026-06-11_lane-1a-prime/path_a_run/` with `manifests/`, per-rung
`L0k/candidate_outputs/` + `L0k/tp_control_outputs/`, per-rung reports, and run-level ledger /
pre-flight / A6 / IVR. Sweep_ids (issued only on authorization):
`lane1a-prime-pathA-cand-<date>-<seed>` and `lane1a-prime-pathA-tp-<date>-<seed>`.

## 13–15. Stopping rules, abort rules, INCONCLUSIVE

Fixed extent: 8 rungs × 96 × 2 arms; no enlargement, no early success-stopping; rungs execute in
schedule order. **Aborts (fail-closed, run-terminating):** all D4-B aborts (pre-flight hash
refusal; A6 drift; candidate or TP batch schema failure; artifact hash mismatch; runner/model
identity mismatch; unhandled exception; missing TP field in any emitted report) **plus** generator
hash mismatch; pilot≠final manifest mismatch; per-rung recipe-conformance failure; sealed-byte
write attempt. An abort mid-schedule retains all completed-rung artifacts; completed rungs remain
reportable as completed, uncompleted rungs as NOT RUN — no silent rerun, no patching, abort package
to verification. **INCONCLUSIVE** is a valid terminal outcome per rung and for the run; never
escaped by retry, enlargement, or tuning.

## 16. Expected artifacts

Generator log + pinned-hash record; 7 materialized manifests + per-rung hashes (pilot and final);
1,536 raw outputs; per-rung candidate and TP predictions; per-rung six-criterion T3 (TP row live)
+ per-rung comparison artifacts (NW CI, locked margin); run-level execution ledger, pre-flight
log, A6 re-verification, IVR; per-run runner file. Every report carries the four TP fields in
ACTIVE form.

## 17. Post-run verification plan

NS full G1 byte verification (every path+hash recomputed); **independent recomputation of all
eight per-rung NW intervals from raw counts**; sealed-record re-hash; constraint audit from
ledger; generator/manifest chain audit (pinned hash → pilot → final → A6); emitter-field audit
across every report; criteria-firing language audit. Team Lead filter; Manager review. No Path A
result citable before verification and filter.

## 18. Non-claim block

Path A, even if approved and even if no criterion fires at any rung, would not establish: model
capability, model incapability, candidate certification, task-family viability, certification
readiness, retention-under-compression, Claim C progress, seam evidence, public benchmark status.
Forbidden phrasings remain prohibited: model passed · capability established · not shortcut-driven
· candidate certified · task family viable · Claim C progressed · seam evidence · public benchmark
result · certification achieved. The instrument may rule out; it may not rule in. Reportable only
as not explained by the declared shortcut battery; never as not shortcut-driven. Eight
non-eliminations, should they occur, are eight rung-local bounded sentences — they do not
aggregate (OC3).

## 19. Constructibility-risk guard

D4-B L01 NOT_RULED_OUT does not prove a full candidate can certify; does not prove task-family
viability across L01–L08; does not prove model capability; is not stress-retention evidence; is
not Claim C progress. **Every Path A outcome** — including criteria firing at every rung above
L01 — remains interpretable across threshold miscalibration · gate-design defect · genuine
constructibility barrier at model/task/scale; the third branch first-class, not presumed, not a
failure.

## 20. Manager decision checklist (unbundled; approve one, all, or none)

```text
[ ] authorize model execution           [ ] decline model execution
[ ] authorize sweep_id creation         [ ] decline sweep_id creation
[ ] authorize L01–L08 sweep execution   [ ] decline L01–L08 sweep execution
[ ] authorize token-prior generations   [ ] decline token-prior generations
    by name
```

Coherence notes for an informed choice: the first three are jointly required for any breadth run;
granting them while declining TP yields a five-criterion breadth run (valid, but surrenders the
measured-control strength D4-B established); declining L01–L08 while granting the rest is
incoherent for this packet (the L01-only forms were D4-A/D4-B). Materialization (§8–10) occurs
only inside an authorized run, after pre-flight, before model load.

**Readiness recommendation: READY for Manager decision.** Generator and manifests fully specified;
no supersession required; no blocker found against the §9 default posture.

Confirmations: no execution occurred; no new sweep_id; no additional model execution; no
additional token-prior generations; no quantization or stress testing; Claim C inactive.

— New Senior Engineer (to Team Lead for filter; the decision is the Manager's)
— Generator-path correction applied 2026-06-12 (CS, patch-level per TL §4; no other content change)
