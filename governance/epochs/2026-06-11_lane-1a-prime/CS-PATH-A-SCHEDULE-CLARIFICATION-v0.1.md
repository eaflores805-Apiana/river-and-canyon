# CS Path A Schedule Clarification (v0.1)

```text
SCHEDULE-DEGENERACY FORENSIC CLARIFICATION — NO SUCCESSOR EXECUTION REQUESTED
PATH A RESULT IS HELD (not discarded); recharacterization required before any citation
SEALED LOCK-RECORD v1.0 UNCHANGED · D4-A AND D4-B ARTIFACTS UNMUTATED
NO MODEL · NO MODEL LOADED · NO NEW SWEEP_ID · NO SWEEP EXECUTION
CS SEMANTIC-READ FAILURE ACKNOWLEDGED
```

To: Team Lead · Cc: Manager, New Senior Engineer, Senior Engineer, Contributor 5
From: CS Engineer
Date: 2026-06-12
Re: Manager §18 / §19 CS deliverable — Path A schedule clarification (#1 in the return order)

CS files the schedule clarification memo per Manager direction. The
sealed schedule's rung-uniform mapping is documented with direct
byte-level evidence from the committed manifests; the consequences for
the Path A characterization are stated honestly; the conditions under
which a true breadth attempt would touch sealed bytes are flagged
explicitly. CS acknowledges this was a semantic-read failure on the
CS side — the breadth concept was not inspected against the sealed
schedule before authoring the Path A runner and the readiness packet
v0.1.1.

This memo is forensic clarification only. It authorizes no execution.
It proposes no schedule change. It does not draft Path A HOLD
disposition language (that is NS-owned per Manager §18). It does not
re-route Path A for citation; it provides the schedule-side evidence
that the held characterization rests on.

---

## §1. Path

```text
governance/2026-06-11_lane-1a-prime/CS-PATH-A-SCHEDULE-CLARIFICATION-v0.1.md
```

## §2. sha256

(Computed at commit time; reported in CS delivery message.)

## §3. Commit SHA

(Reported after this commit lands.)

(Prior HEAD: `70b461db1c59cfd160e4b8edc425271cd420ce8e` — the commit
containing the Path A run outputs + return memo that triggered NS's
schedule-degeneracy finding.)

## §4. Scope

Forensic clarification of the sealed `STRATIFIED_RECIPE_SCHEDULE.json`
artifact (sha256 `7ad3ccddecd070074e666ffaf2178aa0afd3cfda78fc08ef375fe68a907130c5`)
and the materialized Path A manifests, addressing:

- rung_schedule mapping (literal mapping of L01–L08 to recipe blocks)
- per_rung_default behavior (what one rung instance contains)
- whether any per-rung deviations exist
- what would need to change for true breadth
- whether that change touches sealed artifacts

This is the CS semantic-read pass that should have happened before
the Path A readiness packet routed to Manager.

## §5. What is established (the forensic findings)

### 5.1 Sealed `rung_schedule` is rung-uniform

Direct quote from the sealed schedule (sha256 `7ad3ccdd…`), lines 20–29:

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

Every rung label maps to the literal string `"per_rung_default"`. No
per-rung deviations exist in the sealed JSON.

### 5.2 `per_rung_default` is one fixed construction

Direct quote from the sealed schedule, lines 6–19:

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
  "stratified_sum_must_equal_n_answerable": 80,
  "disjointness_constraint": "..."
}
```

One fixed construction: 80 answerable + 16 NULL = 96 per rung;
4 distractors per item; stratified counts 12/12/12/12/32; disjoint
stratum assignment shuffled by the locked seed.

There is **no structural axis** in the sealed schedule that varies
across rungs: not context length, not distractor count, not
key-token length, not stratum counts, not NULL fraction, not
shortcut-policy hit rate. The schedule defines one construction, named
once, and assigns it eight rung labels.

### 5.3 Materialized manifests confirm rung-uniform task content

CS performed a direct byte comparison of the Path A materialized
manifests across rungs. Methodology: strip each record of the
`rung_id` field and the `metadata` block (which carries the per-rung
construction_recipe_hash and the iteration_index); compare the
remaining task-content fields (`context_block`, `queried_key`, `gold`,
`stratum`) across rungs.

Result:

```python
L01_task_content == L02_task_content == L08_task_content
# (and pairwise for all 8 rungs)
# Result: True for every pair.
```

The 96 task records in L01's manifests are **byte-identical** to the
96 task records in L02's manifests, and to L08's, and to every
intermediate rung. The first answerable record in every rung has the
same `context_block.real_pair_block.pairs[0] = {key_token_ids: [194],
value_token_ids: [16]}`, the same `queried_key.key_token_ids = [98]`,
and the same `gold.value_token_ids = [9]`. The same byte-identity
holds for every record at every index in every rung.

What differs across rungs:

```text
- record["rung_id"]                              ("L01" vs "L02" vs ...)
- record["metadata"]["construction_recipe_hash"]  (different per rung;
                                                   includes rung_id
                                                   in the hashed dict)
- record["metadata"]["iteration_index"]           (unchanged here, 0)
```

These are metadata-only differences. They change the manifest's
sha256 (because the JSON bytes differ) but they **do not change what
task the model sees**. The model received the same 96 problems eight
times.

### 5.4 Consequence for Path A's "L01–L08 breadth" characterization

The Path A characterization "L01–L08 breadth" is **not supported** by
the sealed schedule or by the materialized manifests. Per the
forensic findings above:

- The sealed schedule encodes one construction, replicated under
  eight labels.
- The materialized manifests encode one set of 96 task records,
  replicated under eight rung labels with only metadata differences.
- The Path A model run therefore presented the model with the same
  task content 8 times — once per rung label — and obtained the
  expected deterministic-greedy outcome each time.

The 8 per-rung NW intervals (`[0.9159, 0.9978]` identically across
all 8 rungs) and the identical per-rung candidate / TP control
accuracies (1.0000 / 0.0125) are **direct consequences of identical
task content + deterministic decoding**, not consequences of the
model surviving structurally distinct rungs.

This matches NS's finding verbatim: "the committed schedule did not
instantiate the breadth concept the packet claimed." The semantic
mismatch is between (a) what the readiness packet language and the
Path A runner promised ("L01–L08 breadth") and (b) what the sealed
bytes encode (one construction, eight labels).

## §6. What would need to change for true breadth

For a true breadth test, the sealed schedule would need to encode
**structural variation across rungs**. CS enumerates the categories
that could provide breadth without claiming which is correct (that is
NS / Senior / Manager design territory, not CS forensic territory):

### 6.1 Per-rung context length

```text
L01: n_answerable=80, distractor_count=4   → 5 pairs per item (current default)
L02: n_answerable=80, distractor_count=6   → 7 pairs per item
...
L08: n_answerable=80, distractor_count=16  → 17 pairs per item
```

Increasing distractor count per rung increases context length,
testing whether the model's retrieval breaks at deeper contexts.

### 6.2 Per-rung key complexity

```text
L01: 1-token queried_key + 4 distractors with 1-token keys
L02: 2-token queried_key, prefix-neighbor density per stratum
...
L08: 3+ token keys, multiple prefix-neighbor competitors
```

Increasing key complexity per rung tests prefix-confusion resilience
at higher rung indices.

### 6.3 Per-rung structural-feature distribution

```text
L01: 12/12/12/12/32 (current — light shortcut signal)
L02: 16/16/16/16/16 (heavier shortcut signal)
...
L08: 20/20/20/20/0 (saturated shortcut signal; no clean-no-feature items)
```

Increasing structural-feature density per rung tests whether the
candidate's separation from the policy envelope holds as the envelope
expands.

### 6.4 Per-rung NULL fraction

```text
L01: 16 NULL of 96 (current)
L02: 24 NULL of 96
...
L08: 48 NULL of 96
```

Increasing NULL share tests the NULL-stratum behavior at higher
abstention demand.

### 6.5 Per-rung anything else

Other axes a schedule could vary across rungs: token-prior baseline
shifts; declared-policy envelope shifts; difficulty by recipe family
(retrieval vs reasoning vs composition); cross-construction tests
within the lane.

CS does not assert which axis would constitute "correct" breadth.
That decision rests with NS / Senior / Manager design judgment under
the original gate-by-gate discipline Manager just reinstated. CS
flags only that the **current sealed schedule does not encode any of
these axes**, and that no Path A run under the current sealed
schedule can produce a breadth finding.

## §7. Whether the change touches sealed artifacts

**YES.** Any of the per-rung axis changes in §6 would require
modifying the `rung_schedule` field of the sealed
`STRATIFIED_RECIPE_SCHEDULE.json`. The current sealed value maps
every rung to the same string `"per_rung_default"`; per-rung
variation requires per-rung blocks (or different string identifiers)
in the `rung_schedule` field, which would change the JSON bytes.

Changing the sealed JSON bytes changes its sha256, which:

- Breaks the PH5-4 pre-flight refusal hash check (`7ad3ccdd…` →
  some-new-hash) — the existing runner aborts.
- Breaks the LOCK-RECORD v1.0 binding (which records `7ad3ccdd…` as
  the bound schedule sha256).
- Therefore requires a **fresh joint lock event** (PH5-1-class
  procedure: NS + CS + TL co-signature on the new sealed schedule
  hash, then a re-sealing of the LOCK-RECORD pointing to the new
  hash, then Manager sealing authorization).

This is **supersession-class** work, not an in-place edit. Per
Manager direction §8 and §9 (Path A HOLD handling and severity
rubric), the appropriate severity is:

```text
SEMANTIC MISMATCH — committed bytes verify; execution may be faithful;
                    artifact does not instantiate the concept claimed
                    by the packet.
Default: HOLD.
Escalation: SUPERSESSION (sealed artifact must change for any true
            breadth attempt).
```

**CS does not draft, request, propose, or pre-stage a supersession.**
The current sealed schedule remains sealed and unchanged. Any future
true breadth attempt is a separate Manager decision that begins with
NS / Senior / Manager design judgment, not with CS implementation.

## §8. What is NOT established

- This memo does NOT propose a corrected schedule. Schedule design is
  not a CS deliverable. NS / Senior / Manager own that.
- This memo does NOT recharacterize the held Path A result. NS owns
  H1 result recharacterization per Manager §18 NS assignment.
- This memo does NOT rule on the TP-banner artifact-class question
  (H2). NS owns that ruling.
- This memo does NOT propose any successor execution.
- This memo does NOT propose any sealed-byte change.
- This memo does NOT close the Path A HOLD. The HOLD remains active
  per Manager §8 until NS completes the disposition memo
  (NEW-SENIOR-PATH-A-HOLD-DISPOSITION-v0.1.md).
- This memo does NOT claim that the held Path A result is meaningless.
  Manager §7 already recharacterizes it as "the instrument did not
  attach any elimination label under the active six-criterion set for
  an L01-equivalent surface repeated under eight rung labels" — a
  valid instrument finding about the schedule layer. CS accepts that
  framing.

## §9. Whether any successor execution is requested

**NO.** No execution is requested or implied by this memo.

## §10. Whether any sealed artifact supersession is required

**NOT BY THIS MEMO.** This memo establishes that any future true
breadth attempt would require supersession, but does not request,
propose, or initiate supersession. The current sealed schedule
remains sealed and unchanged.

If Manager later wishes to pursue true breadth, the path forward
begins with NS / Senior / Manager design judgment on the breadth
axis, then proceeds through a fresh joint lock event under the
reinstated original gate-by-gate discipline (Manager §4 ten-step
sequence).

---

## §11. CS semantic-read failure — acknowledgment and lessons

CS authored:

- the Path A readiness packet draft contributions (which carried
  forward into NS's v0.1)
- the Path A runner (`lane1a_runner_path_a.py`) with the explicit
  loop `for rung in ['L01','L02','L03','L04','L05','L06','L07','L08']`
- the §13 manifest hash table with 8 distinct per-rung sha256s

All three artifacts treated "L01–L08" as a list of structurally
distinct rungs without ever reading the sealed schedule to confirm
that the rung labels corresponded to structural variation. The
sealed schedule has been on disk and committed since the PH5-1 lock
event (commit `5a12ee8`, 2026-06-11); a semantic-read by CS at
**any** of the following points would have caught the mismatch:

1. Path A readiness packet drafting (would have flagged the breadth
   claim before NS finalized v0.1).
2. Path A runner authoring (would have flagged before the runner
   committed).
3. Path A pre-flight runtime check (would have surfaced as a
   precondition refusal).
4. Path A run-return memo drafting (would have caught the identical
   NW intervals as a degeneracy signal, not a "confirmation").

CS failed to perform this semantic-read at all four points.
Path/hash verification passed each time; semantic verification was
never attempted on the CS side. This is exactly the failure class
Manager §6 names: "a path/hash match is insufficient if the
artifact's meaning has not been checked."

CS commits to integrating Manager's §6 semantic-read requirement
into the STANDARD-RETURN-TEMPLATE-v1.0 §G exit conditions: any
return that asserts a structural property of a sealed artifact
(breadth, transfer, contamination, certification readiness,
constructibility, etc.) **exits the template path** and requires
explicit citation of the semantic-read finding. CS will refresh the
template (v1.0.1) once this clarification is filtered.

## §12. Standing carry (non-authorizations, verbatim)

This schedule clarification memo does not authorize: any execution;
any model load; any new sweep_id; any sealed-byte change; any Path A
re-characterization (NS-owned); any successor execution; any
schedule supersession; any successor model-facing work of any kind.

The Path A HOLD remains active. The sealed LOCK-RECORD v1.0
`51e18fa9…` UNCHANGED. The sealed schedule `7ad3ccdd…` UNCHANGED.
All successor gates CLOSED.

— CS Engineer, 2026-06-12 (semantic-read failure acknowledged; forensic clarification only)
