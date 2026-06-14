# CAL-Q-FORMAT-SENSITIVE-ABSTENTION-FINDING-v0.1

**Version:** v0.1. River and Canyon program. Finding track (NOT a rescue track). Preserves the CAL-Q mechanism finding from the closed D4 certification-readiness route.
**Status:** model-free finding record. Preserves an observation; defines the allowed claim and the forbidden claims; specifies what future diagnostics would be required before generalizing. Authorizes nothing. Anchored on origin/main HEAD 4456d5a.
**Route context:** the Manager has CLOSED D4 as the current certification-readiness baseline route (disposition: PIVOT / valuable negative result). No further D4 repair is authorized. This artifact preserves the finding the pivot produced.
Owner/drafter: Senior Engineer · CS: executed the run + independently identified the format-coupling mechanism (verified) · Team Lead: routing · Manager: requested this finding record + owns any future finding-track authorization.

---

## 1. Executive summary

The final D4 calibration candidate, CAL-Q, replaced the direct query with an
in-prompt code-book alias-decode query, holding list content identical to CAL-B.
It produced the program's first sub-ceiling clean point (0.975 → 0.650) but
collapsed defective abstention from 0.925 to 0.000 — on identical content, with
only the query format changed. The disciplined reading: **in the D4 key-value
family, direct-query defective abstention was robust across content-lever
variants, but did not transfer to the code-book query format. The first query-side
lever that produced meaningful clean difficulty also collapsed defective
abstention to zero. This suggests abstention behavior in this construct is
format-sensitive and may be coupled to retrieval difficulty.** This is a finding
to preserve carefully, scoped exactly to what the bytes license — not a general
claim about models or abstention.

## 2. Evidence base

```text
Five candidates, 3B/FP16, n=40 per member, byte-verified (HEAD 4456d5a):
  cand   query form   clean   def-abstention   false-emission
  CAL-A  direct       1.000   0.900            0.100
  CAL-B  direct       0.975   0.925            0.075
  CAL-C  direct       0.950   0.875            0.125
  CAL-E  direct       0.975   0.900            0.100
  CAL-Q  code book    0.650   0.000            1.000
BINDING PAIR: CAL-B and CAL-Q share IDENTICAL content (list_len 13, slots 8–11,
near-miss 2); they differ ONLY in query format (direct vs in-prompt code-book
alias-decode). Abstention went 0.925 → 0.000 across that single difference.
Per-item confirmation: all 40 CAL-Q defective items emitted a single-letter value,
0 emitted any abstention form (no "none"/"NONE"); format_abstention_artifact = 0.0
(this is model behavior, not a scorer artifact — contrast CAL-E, where 13
"failures" were lowercase-none mis-scores).
Run records: cal-q_run.json (90de7fd0), CS-CAL-Q-RUN-REPORT-v0.1.md (c64c8bda),
cal-q defective/clean outputs in sweep_outputs/.
```

## 3. What CAL-Q showed

```text
- The code-book query DID move clean off the ceiling — the first time any lever in
  the program produced a sub-ceiling clean point (0.650). Content levers never did.
- It simultaneously collapsed defective abstention to 0.000: the model emitted a
  value on every key-absent item instead of abstaining.
- Reading both members: clean's 14 wrong items and all 40 defective items emit
  single-letter values — the same output mode. Under the code-book format the model
  shifted from "look up the key; abstain if absent" to "decode and emit SOME value,"
  emitting REGARDLESS of key presence.
- Clean 0.650 and defective abstention 0.000 are therefore THE SAME EFFECT, not two
  independent ones: the added difficulty displaced the abstention behavior rather
  than loading an intact lookup-and-abstain process.
```

## 4. Why D4 closes as a certification route

```text
A certification baseline needs a construct that is BOTH off-ceiling (room to
measure a stress drop) AND preserves defective discrimination (so the thing being
measured stays intact). The full sweep shows neither lever class delivers both:
  - CONTENT levers (CAL-A/B/C/E): preserve discrimination (~0.90) but cannot move
    clean off the ceiling (all ≥ 0.95).
  - QUERY-SIDE lever (CAL-Q): moves clean off the ceiling but collapses
    discrimination (0.000).
Across five candidates spanning four content-lever variants and one query-side
lever, this task family at 3B/FP16 has no construct satisfying both. Per the
pre-declared CAL-Q rule, the PIVOT condition ("query-side difficulty fails to move
clean off ceiling WITHOUT breaking discrimination") is met. D4 is closed as the
current certification-readiness baseline route — a valuable negative result, not a
failed experiment.
```

## 5. Mechanism hypothesis: format-sensitive abstention / difficulty–abstention coupling

```text
HYPOTHESIS (stated as a hypothesis, not a finding): the model's defective
abstention pathway ("I can't find the key → return NONE") appears COUPLED to the
direct-query format — the distribution under which it was presumably trained to
abstain. When the query moved to the code-book alias-decode format (outside that
distribution) AND retrieval difficulty rose, the abstention behavior did not
transfer; the model defaulted to emitting a value.
TWO COUPLED FACTORS, not cleanly separated by this single run:
  (a) FORMAT: the code-book query is a different prompt structure from the direct
      query under which abstention is robust.
  (b) DIFFICULTY: the decode step also raised retrieval difficulty.
CAL-Q changed BOTH at once, so it CANNOT separate "abstention is format-bound"
from "abstention degrades as retrieval difficulty rises." The honest statement is
the conjunction: under this construct, abstention is format-sensitive and may be
coupled to retrieval difficulty. Disentangling (a) from (b) requires the
diagnostics in §9.
```

## 6. Allowed claims

```text
These are licensed by the bytes and may be stated:
  A1. In the D4 key-value family at 3B/FP16, direct-query defective abstention was
      robust (~0.90) across all four content-lever variants tested.
  A2. That abstention did NOT transfer to the in-prompt code-book query format: on
      identical content, abstention went 0.925 (direct) → 0.000 (code-book).
  A3. The first query-side lever that produced meaningful clean difficulty (clean
      0.975 → 0.650) also collapsed defective abstention to zero.
  A4. This suggests, as a hypothesis, that abstention behavior in this construct is
      format-sensitive and may be coupled to retrieval difficulty.
  A5. Across the five candidates tested, this task family at 3B/FP16 did not yield a
      construct that is both off-ceiling and discrimination-preserving (a scoped
      negative result about THIS family under THESE levers).
All allowed claims are scoped to: the D4 key-value family, 3B/FP16, the five
candidates run, and the two lever classes tested.
```

## 7. Forbidden claims

```text
These are NOT licensed and must not be stated (per Manager):
  F1. "Models cannot abstain." (CAL-A/B/C/E show robust abstention under direct query.)
  F2. "All absence-defined tasks fail." (One family, one model, two lever classes.)
  F3. "No task family can host a clean baseline." (Only THIS family was tested.)
  F4. "The seam is false." (No certified compression rung ever ran; the seam is
      UNANSWERED, not answered.)
  F5. "Compression fragility has been tested." (The program never reached stress;
      it remains PRE-STRESS.)
  F6. "D4 can never work under a fundamentally different structure." (Only the
      tested levers are exhausted; a different construction is untested.)
ADDITIONAL forbidden over-reaches:
  F7. "Abstention is not a real capability." (It is robust within the direct-query
      basin; the finding is about TRANSFER, not existence.)
  F8. "The format-coupling mechanism is established." (It is a HYPOTHESIS; CAL-Q
      confounds format with difficulty — see §5, §9.)
```

## 8. Implications for future task-family design

```text
If a future certification baseline is attempted (in this or another family), this
finding implies:
  - A difficulty lever must be checked for whether it preserves the MEASURED
    BEHAVIOR (here, abstention), not just whether it lowers clean accuracy. CAL-Q
    lowered clean by DESTROYING the measured behavior — a construct-validity failure
    of the lever, not a valid difficulty increase.
  - Abstention robustness measured under one prompt format should NOT be assumed to
    hold under another. Any baseline relying on abstention must verify abstention
    survives the specific query format used for the stress test.
  - Off-ceiling difficulty and preserved discrimination should be demonstrated
    TOGETHER in the SAME construct before it is treated as a calibration baseline;
    they were achievable separately here but never jointly.
```

## 9. Minimal future diagnostics (before any generalization)

```text
To upgrade the §5 hypothesis toward a finding, the minimum required (each gated,
none authorized here):
  D-1. SEPARATE format from difficulty. Run a query-format change that does NOT
       raise retrieval difficulty (e.g., a trivial alias where code A → key is a
       one-step restatement), and a difficulty increase that does NOT change format.
       If abstention collapses under format-change-at-constant-difficulty, the
       coupling is to FORMAT; if under difficulty-at-constant-format, to DIFFICULTY.
  D-2. A GENTLER closed-world lever (e.g., confirm-then-return: "first confirm K is
       present, then return its value") to test whether SOME query-side difficulty
       preserves abstention, or whether ANY departure from the direct-query format
       collapses it. (Note: this would require Manager re-authorization, as CAL-Q was
       the FINAL D4 rescue; named here as a diagnostic, not proposed as a rescue.)
  D-3. CROSS-MODEL check: does the same format-coupling appear in other models, or
       is it specific to Qwen2.5-3B's training distribution?
  D-4. CROSS-FAMILY check: does abstention show the same format-sensitivity in a
       different absence-defined task (not key-value lookup)?
Until at least D-1 is run, the claim ceiling is the §6 allowed list — specifically
A4 stays a HYPOTHESIS.
```

## 10. Relation to Tier 1 eval-validity auditing

```text
This finding is itself a Tier 1 eval-validity result, and supports the pivot:
  - It is a concrete demonstration of WHY a stress-retention program could
    MISMEASURE on this family: if one built a "does the model abstain under
    compression?" eval using a code-book-style prompt, one would measure an
    abstention collapse that is (at least partly) a FORMAT artifact, not a
    compression effect — and wrongly attribute it to fragility.
  - This is exactly the class of error the program's methodology layer catches
    (survival≠correctness, the parser-bug catch, the lever-validity failure here):
    a measured degradation that is an artifact of the measurement setup, not the
    thing of interest.
  - It strengthens the case that the INSTRUMENT (eval-validity auditing) is a
    deliverable independent of whether the seam is ever measured: the program can
    show, with evidence, how absence-defined evals go wrong.
```

## 11. Closed gates

```text
No new D4 run · No CAL-Q rerun · No certification run · No compression · No
INT8/INT4 stress · No second compression rung · No full ladder · No candidate
certification · No ranking · No Claim C activation · No public benchmark packaging
· No funder-facing release · No SBIR submission. This finding record is model-free
(a read of the completed CAL-Q run). The §9 diagnostics are named, not authorized;
each requires separate Manager authorization + route-state GREEN.
```

---

## Note on scope discipline

```text
This record's entire job is to preserve a real, interesting finding WITHOUT
letting it inflate. The finding is genuinely notable — abstention may not be
portable across prompt formats when retrieval difficulty rises — and that is
exactly the kind of result that invites over-generalization ("models can't
abstain," "absence tasks don't work"). The allowed/forbidden split (§6/§7) and the
required diagnostics (§9) exist so the finding survives as what it is: a scoped,
hypothesis-level observation about one task family on one model under one lever,
which would need D-1 at minimum before any broader claim. The discipline that
closed D4 honestly is the same discipline that keeps this finding honest.
```

— Senior Engineer
