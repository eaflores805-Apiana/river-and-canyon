# CS Acknowledgement — Lane 1a Design Packet v0.3 (Consolidated; B1–B5 Corrections)

From: CS Engineer
To: Senior Engineer
Cc: Team Lead, Manager
Date: 2026-06-10
Status: v0.3 received, hash-verified, committed; B1–B5 absorption analysis below; v0.1 CS artifacts marked superseded-by-this-pointer; step 3 production will produce against v0.3 (no intermediate v0.2 CS docs)

---

## 1. Receipt and hash verification

```text
Source: apiana-papers/Lane1a/LANE1A-DESIGN-PACKET-v0.3.md
sha256: f1280a8563bbb48c5592c35c809be6c739859234cbf33b64a3786c6e5df67bab

Filed at: governance/2026-06-10_lane1a/DESIGN-PACKET-v0.3.md
sha256: f1280a8563bbb48c5592c35c809be6c739859234cbf33b64a3786c6e5df67bab

Match: PASS (3-way: source / target / no Senior-quoted prefix in v0.3
                memo — this is a direct file delivery rather than a
                G1 enumeration memo)
```

## 2. v0.3 changelog absorption

v0.3 supersedes v0.1 (Senior also references an interim v0.2 consolidated
on Senior side after my 9-item CS return). The consolidation incorporates
**all nine CS-return items adopted at v0.1 → v0.2** plus **five new B-series
corrections at v0.2 → v0.3**.

### 2.1 v0.1 → v0.2 (CS's nine items — all adopted)

Confirmed adoption matches CS-RETURN-DESIGN-PACKET-v0.1.md exactly:

| CS item | v0.2 form |
|---|---|
| 5a — SE_diff formula | Locked: `sqrt(SE(strict)² + SE(control)²)` |
| 5b — N_effective for headroom | Locked: `80 − void_count_answerable` |
| 5c — abstention_rate_se field | Added to per-rung schema |
| 5d — extended-context | 2,048 tokens |
| 5e — ladder top D | held at 16 |
| 5f — no-re-execution rule | New §1.12 |
| 6a — selective re-execution | Closed by 5f + total-attempt audit counting |
| 6b — outcome-statement determinism | Locked as boolean K-rule in §1.9 |
| 6c — plot prohibitions in code | NotImplementedError per form (§1.8) |

### 2.2 v0.2 → v0.3 (B1–B5: five new corrections from incoming + outgoing Senior collaboration)

Each is absorbed, with implications for what CS will write at step 3.
**The v0.1 CS execution-packet draft body had stale text on several of
these and is therefore superseded by v0.3 design packet + this
acknowledgement** for step-3 production purposes. CS will write step 3
against v0.3, not v0.1.

---

#### B1 — Gap sign convention FIX (dead-rule correction)

**v0.3 §1.6:** *"`strict_content_gap_instability`: gap ≥ 0.15, where
**gap := content_acc − strict_acc** (sign convention locked;
strict-correct implies content-correct, so strict ≤ content always —
the prior 'strict − content' phrasing was a dead rule, corrected
here). Unit test: content 0.90 / strict 0.70 attaches the label."*

**CS analysis.** Senior caught a real defect: my v0.1 CS execution-packet
draft §3 pseudocode had the OLD sign convention
(`strict_acc - content_acc >= 0.15`). Under the strict-implies-content
implication, that expression is non-positive on every well-scored item
and the label was unreachable. **The v0.1 CS draft has the dead rule.**

**Step-3 implementation.**
- `classification_criteria.yaml` will encode `gap := content_acc - strict_acc`.
- `analyzer.py` label-assignment pseudocode will read:
  ```python
  gap = rung_record.content_acc - rung_record.strict_acc
  if gap >= 0.15:
      labels.append("strict_content_gap_instability")
  ```
- `test_lane1a_packet.py` will include Senior's exact unit test:
  *content 0.90 / strict 0.70 → gap 0.20 → label attaches.*

#### B2 — Inconclusive-preempts rule

**v0.3 §1.6:** *"**Preempt rule (B2):** these checks evaluate FIRST;
if any fires, the rung's labels are exactly
`["inconclusive_not_actionable"]` and no other classification rule is
evaluated — an unmeasurable rung supports no elimination. Unit test
included."*

**CS analysis.** My v0.1 CS draft pseudocode allowed multi-attach
including `inconclusive_not_actionable` alongside other labels. Senior's
B2 is the right discipline: an unmeasurable rung cannot eliminate
anything by definition (the void-exceeded measurement is too unreliable
to support even an elimination decision). Multi-attaching gives the
appearance of "ruled out by X AND inconclusive" which mixes
measurement-validity concerns with content concerns.

**Step-3 implementation.**
- `analyzer.py` label-assignment will be restructured to evaluate
  inconclusive checks FIRST:
  ```python
  def assign_labels(rung_record):
      # B2 preempt — evaluate measurement validity first
      if (rung_record.void_count > 5
          or rung_record.harness_anomaly_flag
          or rung_record.missing_required_outputs):
          return ["inconclusive_not_actionable"]
      # Only if measurement is valid do the content-class rules evaluate
      labels = []
      # ... (other rules per §1.6) ...
      if len(labels) == 0:
          labels.append("requires_further_investigation")
      return sorted(labels)
  ```
- `test_lane1a_packet.py` will include a unit test: rung with
  void_count=6 attaches *only* `inconclusive_not_actionable` even if
  other classification rules would fire.

#### B3 — Control scoring stratum pinned to 80 answerable-mirroring controls

**v0.3 §1.5(c):** *"token-prior-control accuracy with SE — computed
over the 80 answerable-mirroring controls only (denominator 80 −
void_count_control); the 16 NULL-mirroring controls are retained as
descriptive abstention-prior data and enter no accuracy statistic
('correct' is ill-defined for a scrambled-binding NULL)."*

**v0.3 §1.6 also clarifies:** *"For the headroom rule,
N_effective = 80 − void_count_answerable (NULL-stratum items and
their voids do not enter strict-accuracy headroom). The per-rung void
budget of 5 counts ALL voids (answerable + NULL)."*

**CS analysis.** This is a refinement of CS recommendation 5a/5b. My
v0.1 CS draft `classification_criteria.yaml` had
`se_control_denom: "N_c_eff = 96 - void_count_control"` — the
denominator was 96 (total control prompts). Senior pins this to 80
(answerable-mirroring controls only). The 16 NULL-mirroring controls
have undefined "correctness" under scrambled bindings — they would
only inject noise into control_acc.

The per-rung void budget clarification (counts ALL voids) is also a
correction: my v0.1 draft was ambiguous; v0.3 makes it explicit.

**Step-3 implementation.**
- `classification_criteria.yaml`:
  ```yaml
  se_diff_formula:
    expression: "sqrt(SE(strict)^2 + SE(control)^2)"
    se_strict_denom: "N_s_eff = 80 - void_count_answerable"
    se_control_denom: "N_c_eff = 80 - void_count_control_answerable_mirror"
  insufficient_measurement_headroom:
    rule: "strict_acc >= 1 - 3 * SE(strict_acc, N_effective)"
    N_effective: "80 - void_count_answerable"
  void_budget:
    rule: "void_count_total > 5 -> inconclusive_not_actionable"
    threshold: 5
    counts: "ALL voids (answerable + NULL)"
  ```
- `manifest_generator.py` will tag each control prompt as either
  `answerable_mirror` (the 80) or `null_mirror` (the 16) so the
  analyzer can partition without re-deriving from item-IDs.
- The §13 manifest recipe is updated to note this scoring partition
  (a one-sentence amendment; the recipe builds 96 prompts per control,
  but only 80 enter the accuracy statistic).
- Per-rung schema: `control_acc` and `control_acc_se` are explicitly
  documented as computed over the 80 answerable-mirror controls only.

#### B4 — Token-prior authorization slot in LOCK-RECORD

**v0.3 §1.11:** *"The LOCK-RECORD must carry the line
`Token-prior control authorization: <explicit Manager citation |
offline fallback>` — the sweep's token-prior controls are model runs
in the class the standing locks name as 'unconditioned token-prior
runs,' and that lock is resolved BY NAME inside the artifact the
Manager confirms; absent an explicit citation, the sweep falls back to
offline dummy-policy controls only and per-rung control generations are
removed from the plan."*

**CS analysis.** This is a critical insight Senior caught. The
standing non-authorizations card includes:

> *"unconditioned token-prior runs — D1 token-prior control may
> require a preflight run; that run is **not** pre-authorized by
> Paper 3 — it requires separate Manager authorization at
> candidate-selection time."*

The Lane 1a sweep's 96-prompt token-prior controls per rung *are*
unconditioned token-prior runs by that definition. Without explicit
Manager authorization at first-data-access time, executing them
violates the standing lock. Senior's resolution:

- **Path A (preferred):** Manager confirmation memo at step 5 cites
  authorization for the Lane 1a token-prior controls by name; the
  LOCK-RECORD records the citation.
- **Path B (fallback):** Manager confirmation does NOT cite token-prior
  authorization; the sweep falls back to offline dummy-policy controls
  only (the existing five declared policies in `dummy_policies.py`);
  per-rung token-prior control generations are removed from the
  execution plan.

Either way, the resolution is BY NAME inside the LOCK-RECORD, visible
to any auditor.

**Step-3 implementation.**
- `LOCK-RECORD.md` template adds a required field:
  ```text
  Token-prior control authorization: <citation>
  ```
- `lane1a_runner_wrapper.py` reads this field at startup:
  ```python
  if lock_record.token_prior_control_authorization in (None, "", "offline_fallback"):
      # B4 fallback: do NOT generate token-prior controls
      skip_control_generation = True
  ```
- If skipped, the `accuracy_indistinguishable_from_token_prior` label
  becomes unattachable (control_acc is undefined); the rule still
  exists in `classification_criteria.yaml` but `analyzer.py` records
  `control_acc: null` and skips the rule, recording an explicit note
  in the sweep record that the rule was unevaluable on this sweep due
  to offline fallback.
- The compute envelope changes: 1,536 → 768 (only candidate
  generations) under fallback; the audit log records this.

This is a meaningful packet-design fork. **CS recommends flagging this
to Manager NOW** so the authorization decision is in hand before step 3
finishes (the LOCK-RECORD field needs the answer to be entered before
the lock).

#### B5 — Survivor-order unit test + total_attempts semantics pinned

**v0.3 §1.7:** *"Survivors are stored as an unordered set serialized
in rung-ID order (unit-tested);"*
**v0.3 §1.12:** *"total_attempt_count must equal
planned_generation_count (8 rungs × 96 items × 2 conditions = 1,536 —
candidate AND control generations both count; semantics pinned in
AUDIT-LOG-FORMAT.md)"*

**CS analysis.** Two pins that strengthen what my v0.1 draft had:

- My v0.1 draft mentioned ladder-order presentation but did not
  specify a unit test. v0.3 makes it a test obligation.
- My v0.1 audit log schema had `total_attempts` as
  `{type: integer, minimum: 8}` (one attempt per rung minimum). v0.3
  pins this to 1,536 (or 768 under B4 fallback) by counting **every
  generation including controls**.

**Step-3 implementation.**
- `test_lane1a_packet.py` includes a unit test asserting `survivors`
  in any sweep record is in alphabetical rung-ID order (`L01 < L02 <
  ... < L08`); the test fails if any sort by statistic is detected.
- `AUDIT-LOG-FORMAT.md` pins the semantics:
  ```text
  total_attempts = candidate_generations + control_generations
  Under full plan (Path A in B4):   8 × 96 × 2 = 1,536
  Under fallback (Path B in B4):    8 × 96 × 1 =   768  (controls skipped)
  ```
- Sweep-level schema field `planned_generation_count` is added so the
  closing check `total_attempt_count == planned_generation_count` is
  schema-validated.

#### C1–C3 routed to §13 recipe (CS confirms)

v0.3 changelog: *"C1–C3 routed to the normative recipe (§13 of the CS
execution packet, per intent-confirmation A2/A3)."*

CS confirms the routing. The §13 normative recipe v0.1
(`governance/2026-06-10_lane1a/EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.1.md`,
filed at commit `48ee825`) is the recipe of record. CS will issue a
minor §13 v0.2 amendment for the B3 scoring partition note
(answerable_mirror vs null_mirror tagging in manifest construction) at
step 3 production time, alongside the script bodies.

---

## 3. Status of v0.1 CS artifacts (superseded for step-3 purposes)

| File | Status |
|---|---|
| `governance/2026-06-10_lane1a/CS-EXECUTION-PACKET-DRAFT-v0.1.md` | **Superseded by v0.3 design packet + this acknowledgement for step-3 purposes.** Content stays in git for historical audit (Senior reviewed bit-identical bytes at `b0b7c263…` to confirm intent preservation). At step 3, CS produces locked artifacts against v0.3, not v0.1; the §3 label-assignment pseudocode (gap sign + B2 preempt) and §2 control-denominator (96 → 80) and §9 LOCK-RECORD template (add B4 line) and §8 audit-log semantics (total_attempts 1,536) are all corrected at step 3 directly. |
| `governance/2026-06-10_lane1a/EXECUTION-PACKET-SEC13-MANIFEST-RECIPE-v0.1.md` | **Holds as recipe of record.** B3-driven minor amendment (control prompt tagging answerable_mirror vs null_mirror) will be applied as a recipe §13 v0.2 at step 3 production time. Senior's eight requirements are all still satisfied; no recipe-design change. |
| `governance/2026-06-10_lane1a/CS-RESPONSE-SENIOR-INTENT-CONFIRMATION-2026-06-10.md` | **Holds.** Case B declaration (wrapper needed) and step-3 plan still apply; the wrapper now also enforces the B4 token-prior-auth conditional path. |

## 4. Open item for Manager (B4 decision needed before LOCK-RECORD)

**Decision required:** before `LOCK-RECORD.md` can be sealed at step 3,
Manager must answer one question:

```text
For the Lane 1a sweep, the per-rung token-prior controls (16 NULL-mirror
+ 80 answerable-mirror = 96 prompts/rung × 8 rungs = 768 generations)
are unconditioned token-prior runs in the standing-non-authorizations
sense.

Option A: Manager cites authorization explicitly in the Lane 1a
          first-data-access confirmation; LOCK-RECORD line reads
          "Token-prior control authorization: Manager confirmation
          memo of 2026-06-XX, §X" (specific citation).
          Total generations: 1,536.
          Control-based label "accuracy_indistinguishable_from_token_prior"
          is evaluable.

Option B: No explicit token-prior authorization cited.
          LOCK-RECORD line reads
          "Token-prior control authorization: offline_fallback"
          (no in-model control runs).
          Total generations: 768 (candidate only).
          Control-based label "accuracy_indistinguishable_from_token_prior"
          is recorded as "not evaluated" on every rung.
          The other four classification rules (envelope, headroom, gap,
          abstention contract) operate as designed.
```

Either path is faithful to the doctrine. CS does not have a strong
preference but flags the question so Manager has it in hand before the
LOCK-RECORD-sealing step.

## 5. CS step-3 production status

```text
Senior v0.3 design packet:        FILED at governance/2026-06-10_lane1a/DESIGN-PACKET-v0.3.md
                                   sha256 f1280a8563bbb48c5592c35c809be6c739859234cbf33b64a3786c6e5df67bab
CS Acknowledgement of v0.3:       FILED (this memo)
B1-B5 absorption:                 COMPLETE; step-3 production will implement directly
Case B wrapper:                   still required (B1 v2 surface unchanged)
§13 normative recipe v0.1:        holds; v0.2 minor amendment at step 3 (B3 control tagging)
B4 token-prior auth:              OPEN for Manager decision before LOCK-RECORD seal
CS step-3 production:             ready to execute on go-ahead
First data access:                NOT AUTHORIZED
```

**CS posture: HOLD for (a) B4 token-prior authorization decision from
Manager, AND (b) go-ahead to execute step-3 production.**

Default if both arrive before next CS session: CS proceeds with
single-cycle step-3 production incorporating all v0.3 B-series fixes,
producing artifacts 3–20 in one commit cycle, LOCK-RECORD sealed last.

— CS Engineer, 2026-06-10
