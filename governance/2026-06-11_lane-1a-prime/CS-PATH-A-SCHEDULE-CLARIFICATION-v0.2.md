# CS Path A Schedule Clarification (v0.2)

```text
SCHEDULE-DEGENERACY FORENSIC CLARIFICATION — NO SUCCESSOR EXECUTION REQUESTED
SUPERSEDES v0.1 (adds TL §6 item 4 + splits TL §6 item 6 vs §6 item 7)
PATH A RESULT IS HELD; recharacterization required (NS-owned) before any citation
SEALED LOCK-RECORD v1.0 UNCHANGED · SEALED SCHEDULE UNCHANGED
D4-A AND D4-B ARTIFACTS UNMUTATED
NO MODEL · NO MODEL LOADED · NO NEW SWEEP_ID · NO SWEEP EXECUTION
CS SEMANTIC-READ FAILURE ACKNOWLEDGED (CS multi-touch)
```

To: Team Lead · Cc: Manager, New Senior Engineer, Senior Engineer, Contributor 5
From: CS Engineer
Date: 2026-06-12
Re: TL §6 7-item scope (supersedes Manager §18 5-item scope); CS schedule clarification for Path A HOLD package

CS files v0.2 of the schedule clarification under TL filter §6. v0.1
(sha256 `22a5ec5c…`) covered Manager §18's 5-item scope (rung_schedule
mapping, per_rung_default behavior, per-rung deviations, what changes
for true breadth, whether sealed bytes are touched). TL §6 expands to
7 items: (a) adds item 4 — **whether the schedule intentionally or
unintentionally defines rung uniformity** — and (b) splits TL §6 item
6 ("whether such change touches sealed artifacts") from TL §6 item 7
("whether true breadth requires supersession") as separate
disposition steps.

v0.2 covers all 7 TL items, retains the forensic content from v0.1,
adds §5.5 with a design-trace through the lock chain, and is filed
alongside v0.1 (v0.1 retained per "supersede, don't rewrite"
convention; v0.2 is active).

---

## §1. Path

```text
governance/2026-06-11_lane-1a-prime/CS-PATH-A-SCHEDULE-CLARIFICATION-v0.2.md
```

## §2. sha256

(Computed at commit time; reported in CS delivery message.)

## §3. Commit SHA

(Reported after this commit lands.)

Prior file:
- `CS-PATH-A-SCHEDULE-CLARIFICATION-v0.1.md` sha256 `22a5ec5c41859f8aafc9adf0b9be0ea108c5bc9864ee395454de3511120d41a0` · commit `e57b1dbd89ef02a15af280fe84810f849189d31e` · status SUPERSEDED by v0.2; retained.

## §4. Scope (TL §6 7-item compliance)

CS addresses each of TL §6's seven items in turn, with direct byte
evidence from the sealed schedule and the materialized Path A
manifests.

---

## §5. Findings (TL §6 items 1–4)

### 5.1 Item 1 — rung_schedule mapping

Sealed `STRATIFIED_RECIPE_SCHEDULE.json` (sha256
`7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5`),
lines 20–29:

```json
"rung_schedule": {
  "L01": "per_rung_default",
  "L02": "per_rung_default",
  "L03": "per_rung_default",
  "L04": "per_rung_default",
  "L05": "per_rung_default",
  "L06": "per_rung_default",
  "L07": "per_rung_default",
  "L08": "per_rung_default"
}
```

Every rung label maps to the literal string `"per_rung_default"`.

### 5.2 Item 2 — per_rung_default behavior

Sealed schedule, lines 6–19:

```json
"per_rung_default": {
  "n_answerable": 80,
  "n_null": 16,
  "distractor_count": 4,
  "stratified_answerable_counts": {
    "gold_at_last_position": 12,
    "gold_at_salient_endpoint": 12,
    "gold_in_prefix_neighborhood": 12,
    "gold_recency_adjacent": 12,
    "no_structural_feature": 32
  },
  ...
}
```

One construction: 80 answerable + 16 NULL = 96; 4 distractors per
item; 5-stratum disjoint shortcut layout (12/12/12/12/32);
deterministic seed expansion.

The sealed schedule encodes the answerable/NULL count axis and the
stratified shortcut-feature axis. It does **not** encode any of the
structural-difficulty axes D2 named (distractor count beyond 4, key
confusability, context load) — those fields do not exist in the
sealed JSON.

### 5.3 Item 3 — whether any per-rung deviations exist

**No.** The rung_schedule maps every rung to the same string. The
per_rung_default block specifies one construction. There is no
per-rung deviation in the sealed schedule along any axis.

Direct byte verification of materialized Path A manifests confirms
this propagated through implementation. Stripping `rung_id` and
`metadata` blocks from each record:

```python
L01_task_content == L02_task_content == ... == L08_task_content
# True for every pair (CS verified 2026-06-12 via direct comparison
# of pilot_manifests_L01.json + path_a_run/manifests/L0k/pilot_manifests_L0k.json)
```

Every answerable record at every index is byte-identical across all
8 rungs in `context_block`, `queried_key`, `gold`, `stratum`. First
answerable record everywhere: `pairs[0]={key:[194], value:[16]}`,
`queried_key=[98]`, `gold=[9]`. What differs across rungs:

```text
- record["rung_id"]                              (string label, "L01" vs "L02" vs ...)
- record["metadata"]["construction_recipe_hash"] (per-rung, because rung_id is
                                                  hashed in to compute it)
- record["metadata"]["iteration_index"]          (0 throughout this run)
```

These are metadata-only differences. The model received the same 96
problems eight times.

### 5.4 Consequence for Path A's "L01–L08 breadth" characterization

The Path A "L01–L08 breadth" characterization is **not supported** by
the sealed schedule or by the materialized manifests:

- Sealed schedule: one construction × eight labels.
- Materialized manifests: one set of task records × eight labels.
- Path A run: same 96 problems presented 8 times under different rung
  labels.

The identical per-rung NW intervals `[0.9159, 0.9978]` and identical
per-rung accuracies (candidate 1.0000, TP control 0.0125) are direct
consequences of identical task content + greedy decoding, not
consequences of the model surviving structurally distinct rungs.

This matches NS's finding: "the committed schedule did not
instantiate the breadth concept the packet claimed."

### 5.5 Item 4 — intentional or unintentional rung-uniformity

This is the new item TL §6 adds. CS distinguishes **two axes of
intent** and finds the answer differs on each.

#### 5.5.1 Design-trace through the lock chain

Direct quotes from each document (chronological):

**(a) D1 / Lane 1a' Prime Design Proposal v0.2** (governance, line 67):

```text
single-hop key→value retrieval over freshly constructed synthetic
entity manifests; the 8-rung ladder L01–L08 over distractor count
D ∈ {4, 8, 16} × key confusability K ∈ {low, high} × context load
X ∈ {base, extended}; neutral rung IDs;
```

D2 declares the L01–L08 ladder explicitly as a **3-axis Cartesian
product over D, K, X**. Per-rung structural variation is part of
the design definition.

**(b) D2 Design Packet Bundle v0.3** (governance, line 52):

```text
I.3 Task family, ladder, recipe. Single-hop key→value retrieval,
fresh synthetic manifests; 8-rung ladder L01–L08 over
D ∈ {4,8,16} × K ∈ {low,high} × X ∈ {base,extended}; neutral IDs.
Construction carried as working basis, not proven sound ...
N=96/rung (80/16) carried as proposal, not locked; final N, split,
and void budget confirmed at packet validation.
```

D2 packet bundle carries the D × K × X ladder forward verbatim.

**(c) PH5-1 Joint Lock Event Record** (lines 58–66; pre-corrective
hash `ef8b0724…`):

```text
Per-rung stratified counts (80 answerable + 16 NULL per rung):
at_last_position:       20 items
at_salient_endpoint:    20 items
in_prefix_neighborhood: 20 items
at_none_of_these:       20 items
```

PH5-1 sealed a **4-stratum 20/20/20/20** recipe at hash `ef8b0724…`.
Lock event scope, per the PH5-1 record §1c and the SEALED
LOCK-RECORD v1.0 §SEALING SCOPE, is *instrument state only*. The
validation pilot/final manifests sealed at PH5-1 cover **L01 only**
(`pilot_manifests_L01.json` + `final_manifests_L01.json`,
sha256 `afe0e545…`). No L02–L08 manifests are sealed.

**(d) Run-3 corrective sealing** (current schedule hash `7ad3ccdd…`):

After PH5-1, run-2 surfaced the recency_excluding_target shortcut
gap. The corrective run-3 sealing replaced the 4-stratum recipe with
the current 5-stratum disjoint recipe (12/12/12/12/32). The sealed
schedule's `rationale` field describes the change:

```text
The previous 4-stratum recipe (run-2) had no recency_adjacent
stratum, leaving recency_excluding_target's hit rate dependent on
incidental adjacency in the random fill — that has been corrected
here at the design level.
```

Run-3 scope was therefore stratified-counts only, not the D × K × X
ladder. The `rung_schedule` field's mapping of all 8 rungs to one
default block was carried into the run-3 sealing as the
default-uniform position; the per-rung-deviation infrastructure is
present (per the `rationale` line: "per-rung-class counts will be
substituted only if a specific rung cannot host the disjoint
schedule (anticipated constructible on L01..L08)") but unused.

**(e) Sealed LOCK-RECORD v1.0** (line 6):

```text
SEALING SCOPE: INSTRUMENT STATE ONLY
```

LOCK-RECORD v1.0 §SEALING SCOPE confirms the lock chain sealed
instrument state only — not the rung ladder. The L02–L08 manifests
were never sealed and were never materialized until the Path A run
itself.

#### 5.5.2 The two-axis answer

**Axis A — Stratified-counts axis (run-3 scope).** Rung uniformity
along this axis is **INTENTIONAL**. The sealed schedule's `rationale`
field declares the per-rung-default position by design ("counts are
construction constants — identical across pilot and final by
design") and provides an explicit deviation mechanism only for
non-constructibility. Run-3 was sealed as a stratified-counts
correction, and the uniform default was a deliberate choice within
that scope.

**Axis B — D × K × X structural ladder (D2 scope).** Rung uniformity
along this axis is **UNINTENTIONAL** with respect to D2's design
declaration. D2 (and the D2 packet bundle) declared L01–L08 as a
Cartesian product over D × K × X with neutral rung IDs. The sealed
schedule has no fields for D, K, or X — the structural axes D2
named — so the structural ladder was **never instantiated in the
sealed bytes**. The schedule has the infrastructure to vary
stratified counts per rung; it has no infrastructure to vary D, K,
or X per rung.

#### 5.5.3 Where the drift happened

The design-to-implementation drift between D2 ("L01–L08 over
D × K × X") and the sealed schedule (one D × K × X corner, no per-rung
variation) was not caused by any single decision visible in the lock
chain. CS reads the drift as a **scope gap**:

- D2 declared the ladder.
- PH5-1 sealed the *instrument validation* on L01 — one corner — and
  the recipe was correctly scoped to stratified-counts (because the
  instrument validation is about A1–A6 conformance, not ladder
  traversal).
- Run-3 corrected the stratified-counts axis; ladder traversal was
  out of run-3 scope.
- LOCK-RECORD v1.0 §SEALING SCOPE: "instrument state only" — sealing
  scope did not include the D × K × X ladder.
- After the lock, **no document established the L02–L08 schedule
  along D × K × X**. The Path A readiness packet inherited the L01–L08
  list, assumed it carried D2's ladder semantics, and routed to
  execution without a semantic-read pass against the sealed schedule.

The drift therefore did not happen at any single document. It
happened in the **absence** of a between-the-locks document that
extended the schedule from L01 (sealed instrument-validation corner)
to L01–L08 (the D × K × X ladder D2 named). The Path A readiness
packet treated the absence as if it were a presence.

#### 5.5.4 CS multi-touch acknowledgment

CS had multiple touches where this could have been caught:

1. CS-IMPLEMENTABILITY-REVIEW-DESIGN-PROPOSAL v0.1/v0.2 (D1 review).
2. CS-D2-PACKAGE-ASSEMBLY-SUMMARY (D2 implementation).
3. CS-CO-SIGNATURE-T3-BOUNDS-AND-ORC10 + CS co-signature of the
   sealed schedule at PH5-1 (lock event).
4. CS-D4-READINESS-RUNTIME-SLOTS v0.1/v0.2 (D4 readiness).
5. CS-PATH-A-READINESS-PACKET-STATE-VERIFICATION v0.1 (Path A
   readiness verification).
6. CS-authored Path A runner (L01–L08 loop without semantic-read of
   the sealed schedule).

At any of these six touches, a semantic-read against D2's L01–L08
declaration would have surfaced the drift. CS performed path/hash
verification at all six and semantic verification at none. This is
exactly the failure class Manager §6 names.

This is not a CS-exclusive failure (D2 design owner, lock co-signers,
TL filter, Manager authorization all had opportunities), but CS
takes the share of the failure that is in CS scope and acknowledges
it.

## §6. Item 5 — what would need to change for true breadth

A true breadth attempt under D2's L01–L08 ladder requires the sealed
schedule to encode per-rung variation along structural axes. The
axes D2 named:

```text
D ∈ {4, 8, 16}            (distractor count)
K ∈ {low, high}            (key confusability)
X ∈ {base, extended}       (context load)
```

would require, at minimum, that the sealed `rung_schedule` map L01
through L08 to eight distinct blocks each specifying its D / K / X
corner (or a less-than-8 enumeration that NS / Senior judges
sufficient). CS does not propose the specific enumeration — that is
NS / Senior / Manager design territory.

Other axes a breadth attempt might use instead (or in addition) per
NS's H1/H3 disposition:

```text
- per-rung context length (number of pairs per item)
- per-rung structural-feature distribution (stratum counts vary)
- per-rung NULL fraction
- per-rung difficulty family (retrieval vs reasoning vs composition)
- per-rung adversarial structural-feature density
```

Any such schedule requires fields in the sealed JSON that do not
currently exist.

## §7. Item 6 — whether the change touches sealed artifacts

**Yes — directly.** Adding per-rung D/K/X (or any other
structural-variation axis) requires modifying the
`STRATIFIED_RECIPE_SCHEDULE.json` byte content:

- The `rung_schedule` field would need 8 distinct values, not 8
  copies of `"per_rung_default"`.
- The schedule would need per-rung blocks (or a parametric
  resolution) that the current `per_rung_default` does not provide.
- New top-level fields for D, K, X (or an equivalent per-rung axis
  encoding) would need to be added.

Any of these changes the JSON bytes, which changes the sha256, which:

```text
- breaks the PH5-4 pre-flight refusal hash check
  (current sealed value 7ad3ccdd... → some new hash)
- breaks the LOCK-RECORD v1.0 binding (which records 7ad3ccdd... as
  the bound schedule sha256)
- breaks the preconditions_path_a.json lock_event_hashes binding
- breaks D4-A and D4-B preflight bindings as well (those also bind
  to the current sealed hash)
```

A change to the sealed schedule is therefore a **sealed-byte
change**, not an in-place edit. Per the project's standing rule, no
sealed byte changes in place.

## §8. Item 7 — whether true breadth requires supersession

**Yes — supersession-class.** Per Manager §9 severity rubric:

```text
SEMANTIC MISMATCH: committed bytes verify; execution may be faithful;
                   artifact does not instantiate the concept claimed
                   by the packet.
Default: HOLD.
Escalation: SUPERSESSION if a sealed artifact must change.
```

Path A meets the SEMANTIC MISMATCH default (current HOLD). A true
breadth attempt meets the SUPERSESSION escalation because the
sealed `STRATIFIED_RECIPE_SCHEDULE.json` must change for any per-rung
D × K × X (or other structural axis) variation to be encoded.

Supersession procedure (CS describes only; does not request, draft,
pre-stage, or initiate):

```text
1. Manager decision to pursue supersession.
2. NS / Senior design the schedule v2 enumerating per-rung axes.
3. NS / Senior submit schedule v2 for D2-equivalent pre-lock review
   under the reinstated original gate-by-gate discipline (Manager
   §4 ten-step sequence).
4. Fresh PH5-1-class joint lock event:
   - NS + CS + TL co-signature on the new sealed schedule hash.
   - Manager sealing authorization.
   - Re-seal LOCK-RECORD pointing to the new schedule hash.
5. Fresh A1–A6 instrument validation on the new schedule (or a
   subset rung; NS to scope).
6. Only after the new LOCK-RECORD is sealed: any model-facing
   execution may be authorized, subject to the full original
   gate-by-gate sequence.
```

The current sealed LOCK-RECORD v1.0 `51e18fa9…` and sealed schedule
`7ad3ccdd…` remain unchanged throughout the supersession
procedure — supersession does not alter sealed bytes; it produces a
new sealed record alongside the old one, both retained under the
project's supersede-don't-rewrite convention.

**CS proposes no supersession in this memo.** The above is procedural
description for the disposition package; the decision to pursue
supersession rests with Manager.

## §9. What is established (closed list)

```text
- Sealed rung_schedule is rung-uniform (all L01..L08 → "per_rung_default")
- per_rung_default is one fixed construction
- Materialized Path A manifests are byte-identical in task content across all 8 rungs
- Path A characterization "L01–L08 breadth" is not supported by the sealed bytes
- Rung-uniformity is INTENTIONAL on the stratified-counts axis (run-3 scope)
- Rung-uniformity is UNINTENTIONAL on the D × K × X axis (D2 design scope)
- D2 declared L01–L08 as a D × K × X ladder; the sealed schedule does not encode D, K, or X
- Drift happened in the absence of a between-the-locks ladder document, not at any single failed document
- Any change to encode true breadth touches the sealed STRATIFIED_RECIPE_SCHEDULE bytes
- Any such change is supersession-class under Manager §9 severity rubric
- CS semantic-read failure acknowledged across six CS-scope touches
```

## §10. What is NOT established (closed list)

```text
- This memo does NOT propose a corrected schedule. NS / Senior / Manager own that.
- This memo does NOT recharacterize the held Path A result. NS owns H1.
- This memo does NOT rule on the TP-banner artifact-class question. NS owns H2.
- This memo does NOT propose any successor execution.
- This memo does NOT propose any sealed-byte change.
- This memo does NOT initiate supersession.
- This memo does NOT close the Path A HOLD.
- This memo does NOT assert the held Path A result is meaningless;
  Manager §7 already provides the only acceptable characterization
  ("instrument did not attach any elimination label under the
  active six-criterion set for an L01-equivalent surface repeated
  under eight rung labels"), which CS accepts as binding.
- This memo does NOT assert that D2's D × K × X ladder is the only
  possible breadth axis. Other axes are available; NS / Senior /
  Manager design judgment governs which is correct.
- This memo does NOT assign blame for the drift to any single role.
  CS acknowledges its share; other shares are noted but not adjudicated.
```

## §11. Whether any successor execution is requested

**NO.**

## §12. Whether any sealed artifact supersession is required

**Per this memo: no.** True breadth would require supersession;
this memo does not initiate it. The decision rests with Manager
under the reinstated original gate-by-gate discipline.

The current sealed bytes remain sealed and unchanged.

## §13. Cross-references

- v0.1 (superseded): `CS-PATH-A-SCHEDULE-CLARIFICATION-v0.1.md`
  sha256 `22a5ec5c41859f8aafc9adf0b9be0ea108c5bc9864ee395454de3511120d41a0`
  commit `e57b1dbd89ef02a15af280fe84810f849189d31e`
- TL filter (driving doc): TL-PATH-A-HOLD-DISPOSITION-FILTER 2026-06-12
- NS HOLD disposition: `NEW-SENIOR-PATH-A-HOLD-DISPOSITION-v0.1.md`
  (referenced by TL filter; not directly read by CS for this memo)
- Manager Process Acceleration Suspension notice: 2026-06-12
- Sealed schedule: `experiments/2026-06-11_lane-1a-prime/validation/STRATIFIED_RECIPE_SCHEDULE.json`
  sha256 `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5`
- Sealed LOCK-RECORD v1.0: `governance/2026-06-11_lane-1a-prime/LANE1A-PRIME-SEALED-LOCK-RECORD-v1.0.md`
  sha256 `51e18fa9f45379a37aaac6f33b2bcef442e3dff6eeb0268ad073ac04423d1935`
- D2 ladder declaration: `LANE1A-PRIME-DESIGN-PROPOSAL-v0.2.md` line 67
- D2 packet bundle ladder restatement: `D2-DESIGN-PACKET-BUNDLE-v0.3.md` line 52
- PH5-1 lock event: `PH5-1-JOINT-LOCK-EVENT-RECORD-2026-06-11.md` §1c (lines 58–66)

## §14. Standing carry (non-authorizations, verbatim)

This schedule clarification memo does not authorize: any execution;
any model load; any new sweep_id; any sealed-byte change; any Path A
recharacterization (NS-owned); any successor execution; any
schedule supersession; any successor model-facing work of any kind.

The Path A HOLD remains active. The sealed LOCK-RECORD v1.0
`51e18fa9…` UNCHANGED. The sealed schedule `7ad3ccdd…` UNCHANGED.
All successor gates CLOSED.

— CS Engineer, 2026-06-12 (TL §6 7-item compliance; semantic-read failure acknowledged across six CS touches; supersedes v0.1)
