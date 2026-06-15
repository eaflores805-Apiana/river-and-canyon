# PRE-REGISTRATION — TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1

**Locked BEFORE any results are seen.** River and Canyon program. This document declares the task construction, conditions, metrics, classifier, and decision rules for a single FP16-only characterization sweep, so the result can come back any of its pre-declared shapes and be reported honestly. **It runs no model and contains no results.**

**Author / status:** Senior-drafted (model-free). **Execution is not performed here and is not the Senior's to perform** — the run is CS's, on the real machine, and only after the Manager explicitly authorizes this specific named run by name (Route GREEN). Classified as an **exploratory characterization / finding-track study, NOT Lane 4 certification evidence** unless the Manager separately classifies it.

**Run name:** TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1.
**Run dir (created at execution):** `experiments/<date>_terminal-attraction-bounds-sweep/`.

---

## 0. Three approvals this needs (kept distinct)

1. **Proposal approval** — TL/Manager agree this is well-formed and worth running. (This document.)
2. **Run authorization** — Manager authorizes this named run *by name*; it is model-facing, so it goes through the standing gate (lock-before-look, Manager-by-name, Process Acceleration suspended for model-facing gates). The Senior advises and does not authorize.
3. **Ordering decision** — this is seam-adjacent characterization; the route is YELLOW, instrument-first, and the next *build* of record is G6. Running this **before** G6 is an explicit reorder the Manager makes on purpose. Default order: G6 first; this study is parked beside the CAL-Q finding track until the order makes room. It is a **standalone artifact, not a subsection of G6** (G6 is model-free; nesting a model-facing run inside it would break that boundary).

---

## 1. Purpose, and the question it serves

This study measures **how strong terminal attraction is and where its bounds are**, as **input to the substrate-viability question** — *is terminal attraction defeatable by construction on Qwen2.5-3B, or is it a property of the substrate?* It is **not** a repair of Two-Hop L1 and **not** a search for a passing composition baseline. Terminal attraction is the **dependent variable** here, not a confound to be screened out.

The two readings it is designed to discriminate, with their guards pre-declared so they cannot decay under interpretation:

- **If attraction scales smoothly with clutter** → distractor salience is a real, **designable lever** — *demonstrated a lever, not demonstrated sufficient*, and not valid down to the distinguishability floor (§7). "Lever" must never be restated as "fix."
- **If attraction is already maxed at one chain** → the confound is **deeper than distractor count** — a *behavioral* statement only: "not driven by distractor count on this task family," **never** "architectural / training-distribution / inside the model." Mechanism is out of bounds (§9).

A third knob is included because clutter alone underdetermines the answer: a one-knob sweep cannot separate *number-of-competing-terminals* salience from *position/recency* salience (the model may be keying on a last-token endpoint, not on chain count). See §3.

---

## 2. Model, runtime, decoding

```text
Model:      Qwen2.5-3B-Instruct, FP16 only (HF cache; loader mlx_lm.load("Qwen/Qwen2.5-3B-Instruct")).
            FP16 ONLY — no INT8, no compression arm. This study makes no compression claim of any kind.
Runtime:    mlx_lm 0.31.3 (recorded in manifest).
Decoding:   greedy / deterministic — temperature = 0.0, max_tokens = 16. Identical for every condition.
Prompt:     REUSE the v0.1 run's prompt template, read-only (manifest prompt_template
            sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e). No template variation;
            the template is held fixed so it is not a hidden variable.
```

## 3. Design — 3 × 2 factorial (two knobs)

```text
Knob 1 — CLUTTER (competing-chain count k): k ∈ {1, 3, 5}.
Knob 2 — TARGET-TERMINAL POSITION: {EARLY, LATE} — where the target chain's terminal fact
         ("B maps to C") sits in the shuffled fact block (first third vs last third).

6 cells = {1,3,5} × {EARLY, LATE}. n = 12 items per cell (proposed; adjustable at authorization).
72 items total × 3 query types = 216 generations. Est. wall-clock ~1 hour (one-time model load + ~0.25s/gen class).
```

What each contrast isolates:

- **Across clutter at fixed position** → does attraction scale with the number of competing terminals? (distractor-count effect)
- **Across position at fixed clutter** → does attraction depend on where the target terminal sits? (position/recency effect)
- **Interaction** → does position matter more under high clutter?

Coarse by design (n = 12 → rate resolution ≈ 0.083). This is a directional characterization sweep, not a powered test (§10).

## 4. Task construction (deterministic; CS materializes and commits BEFORE the run)

Each **item** contains:

```text
- 1 TARGET chain:   A -> B -> C, expressed as two facts:  "A links to B."  and  "B maps to C."
- (k - 1) DISTRACTOR chains: A' -> B' -> C', same two-fact form (k = clutter level).
- 2 fixed "holds" distractor facts:  "W holds V."  — guarantee non-chain salient tokens even at k = 1
  (the distinguishability floor; never removed — see §7).
Tokens:  random unique 5-letter uppercase tokens, role-disjoint within an item; no token reused across
         roles in the same item. (Role-prefix convention from the v0.1 family — A-tokens "ZA…", B-tokens
         "ZB…" — may be preserved for readability; not load-bearing.)
Fact order: all facts shuffled within the item, EXCEPT the target chain's "B maps to C" fact is forced into
         the first third (EARLY) or last third (LATE) of the block per the cell. All other facts fill the rest.
Queries (all three asked per item, matching v0.1):
   hop1       — target A -> ?   (expected B, the INTERMEDIATE — never a terminal)
   hop2       — target B -> ?   (expected C; single-fact control)
   composite  — target A -> ?   (expected C; requires chaining)
```

Determinism / provenance: CS generates the full 72-item set with the committed generator at a **fixed seed**, writes it to `items_materialized.json`, and **commits + hashes that materialized file before the run** (this directly closes the v0.1 items-file locatability gap — the run reads the committed bytes, never a regenerated set).

## 5. Scoring and the pre-declared classifier

Two instruments, both hashed, both fixed before look:

**(a) Locked scorer — correctness columns, read-only.** Use `tier0-run/scorer_twohop_l1.py` (sha256 `b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde`), unmodified, for per-item correct/incorrect on each query type.

**(b) Pre-registered structural classifier — the attraction meter.** The scorer's categories do not cleanly tag "returned the target chain's terminal on a hop1 query," which is the central quantity. The following classification is **locked here, before any results**, and computed from the raw outputs plus the known chain structure:

```python
def classify(token, query_type, target_A, target_B, target_C, all_terminals, all_intermediates):
    # all_terminals     = {C of every chain in the item}  (target + distractor chains)
    # all_intermediates = {B of every chain in the item}
    if token == "NULL":                       return "ABSTAIN"
    if query_type == "hop1":                   # expected = target_B (an INTERMEDIATE; never a terminal)
        if token == target_B:                  return "CORRECT"
        if token == target_C:                  return "TARGET_TERMINAL_GRAB"   # clean attraction signal
        if token in all_terminals:             return "DECOY_TERMINAL_GRAB"
        if token == target_A:                  return "ANCHOR_ECHO"
        return "OTHER"
    if query_type == "hop2":                   # expected = target_C (single-fact control)
        if token == target_C:                  return "CORRECT"
        if token in all_terminals:             return "OTHER_TERMINAL"
        return "OTHER"
    if query_type == "composite":              # expected = target_C (requires chaining)
        if token == target_C:                  return "CORRECT"            # NOTE: at k=1, ambiguous — see §6
        if token in all_terminals:             return "DECOY_TERMINAL_GRAB"
        if token in all_intermediates:         return "STOPPED_SHORT"
        return "OTHER"
```

The classifier script is committed and hashed before the run; its hash is recorded in the manifest.

## 6. Metrics (per cell, pre-declared)

```text
PRIMARY (clean attraction meter — valid at ALL clutter levels):
  hop1 TARGET_TERMINAL_GRAB rate   = count(TARGET_TERMINAL_GRAB) / n        [on hop1, answer is an
                                                                             intermediate, so a terminal
                                                                             return is unambiguous attraction]
SECONDARY:
  hop1 ABSTAIN rate, hop1 CORRECT rate (expected ~0)
  hop2 CORRECT rate                 [CONTROL: confirms the model is functioning in this cell — a single-fact
                                     lookup it can do; if hop2 collapses, the cell is suspect, not informative]
SEAM-CONTEXT:
  composite CORRECT rate, composite DECOY_TERMINAL_GRAB rate (k>=3), composite ABSTAIN rate
```

**Validity caveat, pre-declared (not the seam gate).** This is FP16-only characterization, so the v1.0 seam runs' "contaminated FP16 baseline ⇒ INCONCLUSIVE" disqualifier **does not apply** — measuring attraction is the goal. The two validity checks that *do* apply: (1) the **hop2 control** must show the model can do single-fact retrieval in each cell, else that cell is uninterpretable; (2) **composite CORRECT at k = 1 is distinguishability-limited** — with one chain, the only chain-terminal present is the answer, so a composite "correct" cannot be separated from a target-terminal grab (the i06 problem, generalized). composite@k=1 is therefore reported but **flagged uninterpretable for retrieval competence**; the **hop1 grab rate is the clean meter** at k = 1.

## 7. The distinguishability floor (binding constraint)

Distractor terminals (other chains and/or "holds" facts) are **never fully removed** in any cell. A construction with a single salient token cannot distinguish retrieval from grabbing, so any "success" there is unfalsifiable. This is why k = 1 still carries 2 "holds" distractor facts, and why the clean attraction read leans on hop1 (intermediate target) rather than composite (terminal target).

## 8. Pre-declared readings and the decision point

Computed on the **primary metric** (hop1 target-terminal-grab rate) across clutter at each position, plus the position contrast. Thresholds chosen NOW, coarse, directional:

```text
SMOOTH SCALING   hop1 grab rate rises with k (>= +0.25 from k=1 to k=5, monotone-ish across both positions).
                 READING: distractor salience is a designable LEVER — demonstrated a lever, NOT sufficient,
                 NOT valid down to the distinguishability floor. "Lever" never restated as "fix."
MAXED AT k=1     hop1 grab rate already substantial at k=1 (>= 0.50) and roughly flat across k.
                 READING: attraction is NOT distractor-count-driven; "deeper than distractor count on this
                 task family" — BEHAVIORAL only, never a mechanism/architecture/training claim.
POSITION EFFECT  hop1 grab (and/or composite decoy-grab) differs by EARLY vs LATE at fixed k (>= 0.25 gap).
                 READING: attraction is position/recency-sensitive, separable from clutter.
FLAT / MIXED     none of the above cleanly holds. READING: report as-is; a flat result is a result.
```

**Decision point (genuinely open; made at evaluation, not now).** The Manager evaluates the 6-cell table against these readings and chooses among: (a) **bank and move on** — the bounds are characterized, return to the instrument-first order (G6); (b) **design a powered follow-up** under separate authorization; (c) **substrate conclusion** — if attraction is not distractor-driven and not position-defeatable, the seam likely needs a *different task family*, not a different prompt (a publishable negative for the seam program). A flat/uninformative result routes to (a). No second sweep runs without re-authorization (§14).

## 9. Forbidden interpretations (binding on the writeup)

```text
The result must NOT be reported as, or used to claim:
  - Claim C progressed / a compositional seam demonstrated / Paper B activated
  - any compression or compression-robustness claim (this run is FP16-only)
  - a certified-baseline claim, or "we found the prompt fix" / a passing composition baseline
  - "Qwen2.5 can / cannot do two-hop reasoning" (a model-capability claim — out of bounds)
  - ANY mechanism claim (attention pattern, architecture, training distribution). "Deeper than distractor
    count" is behavioral only.
  - "designable lever" without "demonstrated a lever, not sufficient, not to the distinguishability floor"
  - any product- or funder-facing result
The honest output is: a 6-cell table of the §6 metrics, which §8 reading holds, the validity flags
(hop2 control; composite@k=1 distinguishability-limited), and an open decision — nothing about the model's
internals or the seam's truth.
```

## 10. Pre-declared limits

```text
- n = 12/cell -> rate resolution ~0.083; directional, not powered. A borderline trend is NOT a finding;
  it routes to "bank, or design a powered follow-up," never to an asserted scaling law.
- One model, one synthetic task family, FP16, characterization only. Results hold for THIS construction
  family on THIS model; they do not generalize without separately-authorized work.
- Behavioral metrology: this measures what the model does, never why it does it.
```

## 11. Provenance requirements (HARD — the v1.0-run lessons, baked as preconditions)

```text
1. items_materialized.json committed and sha256 recorded in the manifest (NO generator-only reference;
   the run reads the committed bytes). [closes the v0.1 items-file locatability gap]
2. FP16 weight provenance RECORDED in the manifest: sha256 of the weight shards, OR the pinned HF revision
   commit hash. [closes the v0.1 weight-bytes-not-pinned gap]
3. Classifier script + locked scorer committed; both hashes in the manifest. Scorer used READ-ONLY.
4. Prompt template reused from v0.1 (sha c8a81a29…), recorded.
5. Manifest anchored to THIS pre-registration's sha256.
6. New dated run dir only; NO sealed-byte movement; 4-of-4 sealed paths byte-identical, verified post-run.
```

## 12. Execution order (for CS, after Manager by-name authorization — NOT performed here)

```text
1. Create run dir; commit THIS pre-registration first (locked before any run).
2. [Manager authorizes this named run BY NAME -> Route GREEN.]
3. Generate the 72-item set at the fixed seed -> items_materialized.json; commit + hash.
4. Load FP16 model; record weight provenance (shard sha256s or HF revision) in the manifest.
5. Run all 6 cells x 12 items x 3 query types, greedy -> raw_outputs.json (raw E3, per cell or unified).
6. Score with the locked scorer (read-only) -> correctness columns.
7. Run the §5 pre-registered classifier -> attraction-type columns; assemble the 6-cell §6 table.
8. Validity checks: hop2 control rate per cell; flag composite@k=1 distinguishability-limited.
9. Manifest: sha256 every input + output; mlx_lm 0.31.3, machine id, decoding params, n, seed, prompt/scorer/
   classifier/items hashes; anchored to this pre-reg's sha.
10. Disposition: the 6-cell table + which §8 reading holds + the open decision; report per §9.
11. Commit, push, verify; return PASS in TL's exact return format.
```

## 13. Boundaries held throughout

```text
no INT8 / no compression arm · no certification · no Lane 4 classification · no Claim C / Paper B ·
no model-capability claim · no mechanism claim · no sealed-byte movement (new dated dir only) ·
no product/funder claim · distinguishability floor preserved in every cell.
```

## 14. Stop-rule

One sweep. Six cells. Evaluate against §8, decide at §8's decision point. **A flat result is a result.** No second sweep, no added knob, no n increase without fresh Manager authorization. This is a bounded scoping study, not the front of an open-ended thread.

---

*PRE-REGISTRATION — TERMINAL-ATTRACTION-BOUNDS-SWEEP-v0.1 (Senior-drafted; model-free; the before-you-look LOCK): Qwen2.5-3B-Instruct FP16 only, mlx_lm 0.31.3, greedy (temp 0.0 / max_tokens 16), reusing the v0.1 prompt template (read-only). A 3×2 factorial — clutter (competing-chain count k ∈ {1,3,5}) × target-terminal position (early/late) — n=12/cell, 72 items, 216 generations, ~1h. Primary metric: hop1 TARGET_TERMINAL_GRAB rate (clean attraction meter; the intermediate is never a terminal). Secondary: hop1 abstain/correct, hop2 correct (functioning control). Seam-context: composite correct / decoy-grab / abstain (composite@k=1 flagged distinguishability-limited; this is NOT the seam disqualifier gate — attraction is the dependent variable). Locked scorer (sha b65c6803…) read-only for correctness; a pre-declared structural classifier supplies attraction typing. Pre-declared readings with decay-guards: SMOOTH SCALING ⇒ "lever, not sufficient, not to the distinguishability floor"; MAXED AT k=1 ⇒ "deeper than distractor count, behavioral not mechanistic"; POSITION EFFECT ⇒ recency-sensitive; FLAT/MIXED ⇒ a result. §10 limits (coarse n; one model/family; behavioral only). §9 forbidden interpretations (no compression / Claim C / Paper B / capability / mechanism / certified-baseline / product-funder). §11 provenance preconditions (materialized items committed+hashed; weight bytes/revision recorded; classifier+scorer hashed; manifest anchored). §12 execution order for CS AFTER by-name authorization. Three distinct approvals: proposal, by-name run authorization, and an explicit ordering decision vs the G6-first default. Exploratory characterization / finding-track, NOT Lane 4. Standalone artifact, not a G6 subsection. Stop-rule: one sweep, decide, no second sweep without re-authorization. EXECUTION NOT PERFORMED HERE and not the Senior's to perform.*
