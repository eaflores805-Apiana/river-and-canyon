# CS Filing Return + Feasibility Glance — ONE-PAGE-INT8-CONTROL-RUNG-SPEC v0.1

**Date:** 2026-06-26
**From:** CS Engineer
**To:** Team Lead, Manager; Cc: Senior Engineer, C5
**Re:** Byte-faithful filing of `ONE-PAGE-INT8-CONTROL-RUNG-SPEC-v0.1.md`; CS feasibility glance result; governance-path flag (lighter path proposed — Manager decision required)
**Status:** **FILED + GLANCE COMPLETE (3/4 PASS, 1 run-machine caveat).** Authorizes nothing. The proposed lighter governance path is **not adopted by this return** — that is the Manager's (TL-routed) call. No run authorized.

---

## Record status

```text
Senior delivered a SECOND, lighter governance object for the first INT8 touch:
  - ONE-PAGE-INT8-CONTROL-RUNG-SPEC-v0.1  (this doc)  — proposes: CS glance + Manager by-name,
                                                        NO five-gate loop, NO C5 (unless new claim language)
  - vs. the existing FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET-v0.3 (parked at C5 gate-2)

These are two DIFFERENT governance weights for the same rung. Choosing between them MODIFIES the
Manager's own 2026-06-21 five-gate direction and stands C5 down from a review it has prepared — so
it is a Manager decision, ideally TL-acknowledged. CS files the proposal and runs the glance; CS
does not adopt the path or retire C5.
```

## 1. Filing (byte-faithful)

```text
ONE-PAGE-INT8-CONTROL-RUNG-SPEC-v0.1.md   sha256 8b1a2f14c9e2c52c8442a21bf4402b2dc1a300c64bf65fee955758803b695647
```

Filed verbatim from the inbox into the direction directory. **Note:** Senior did not include a SHA256SUMS file with this delivery (the packets had one); the digest above is CS-computed from the delivered bytes and recorded here as the hash of record. If Senior holds a different declared digest, flag a mismatch.

## 2. CS feasibility glance — the four checks the spec asks for

The spec defines the glance as: *artifacts present · scorer pinned · paths correct · INT8 quantization target available.* Result:

```text
1. Artifacts present + hashes match (recomputed from repo @ HEAD 4a4b5bd8):
     prereg          3fb4dbd4…  ✓   (experiments/2026-06-15_minimal-fp16-int8-twohop-l1/PREREGISTRATION.md)
     scorer          b65c6803…  ✓   (tier0-run/scorer_twohop_l1.py)            ← Cell03 scorer, pinned
     items_file      7d5099cb…  ✓   (tier0-run/items_twohop_l1_cell03.json)
     prompt_template c8a81a29…  ✓   (tier0-run/prompt_template_twohop_l1.txt)
     smoke_test      58749ca8…  ✓   (tier0-run/smoke_test_twohop_l1.py)
   PASS — all five declared hashes resolve to present, tracked files.

2. Scorer pinned:  PASS  — byte-locked Cell03 scorer b65c6803; any change voids the gate.

3. Paths correct:  PASS  — target run dir convention experiments/<date>_first-compression-rung/;
                            2026-06-15 reference run present; sealed bytes not touched.

4. INT8 quantization target available:  PARTIAL — RUN-MACHINE CONFIRMATION REQUIRED.
     tier0-run/Qwen2.5-3B-Instruct-mlx-int8/ exists and is git-tracked for its
     config.json, model.safetensors.index.json, tokenizer_config.json, chat_template.jinja,
     generation_config.json (5+README).  BUT the weight shard model.safetensors is GITIGNORED
     ("# Model weights — do not commit") and is ABSENT from this clone. So the target's STRUCTURE
     is confirmed; its WEIGHTS cannot be confirmed from the repo and must be verified present on the
     RUN MACHINE (HF cache / local int8 dir) before the run. This is expected, not a defect — but the
     glance cannot rubber-stamp "available" from the clone alone.
```

**Glance verdict:** the three repo-confirmable checks PASS; the fourth is structurally PASS but requires a run-machine weights check at run time. The feasibility surface is clean; the only open item is a physical-presence check that lives on the run machine, not in git.

## 3. One thing the spec gets right (worth recording)

The spec specifies a **FRESH run** (retain raw outputs for BOTH conditions; compute byte-identity — you do not "retain both" or "compute byte-check" on an adoption). Going fresh **moots C5's item-5 adoption concern entirely** — that concern was specifically about adopting the already-disposed 2026-06-15 bytes as the rung. A fresh, language-locked control run has no lock-after-look surface. This is the cleaner of the two paths C5 itself named.

## 4. Governance-path flag + CS recommendation (Manager's decision, not CS's)

The lighter path is **defensible**: the honest content is a null-stress machinery/calibration check, the claim-risk surface genuinely collapses for a fresh run under the tight allowed/forbidden language lists, and over-governing a calibration is real friction. CS does **not**, however, adopt it unilaterally. If the Manager chooses it, CS recommends three conditions:

```text
(a) RETAIN one C5 tripwire, made concrete: CS performs a LANGUAGE-CONFORMANCE CHECK on the
    result writeup before filing it — verifying it uses ONLY the spec's allowed-language list and
    contains NONE of the forbidden phrasings. Any deviation trips the result to C5 before it is
    filed. This keeps "no C5 unless new claim language" honest by naming who judges it (CS at
    file-time) and what happens on a trip (C5).
(b) DISPOSITION the v0.3 packet explicitly. It is currently parked at C5 gate-2. If the control-rung
    path is adopted, the Manager should state whether v0.3 is SUPERSEDED by this spec or RETAINED as
    the heavier alternative — so the record does not carry two live governing objects for one rung.
(c) The run begins ONLY at Manager by-name authorization. This glance is a feasibility return; it is
    not a run authorization, and it does not by itself stand C5 down.
```

**CS lean:** adopt the lighter path *with guard (a) and disposition (b)*. The fresh-run framing removes the specific high-stakes risk C5 flagged, and the language locks plus a CS conformance check cover what remains. But the path-switch is the Manager's to make (TL-routed), because it changes the 2026-06-21 direction and retires a prepared C5 review.

---

## Non-authorizations (carried forward)

```text
- First INT8 rung: packet-authoring lifted; the RUN remains NOT AUTHORIZED until Manager by-name
  authorization (whichever path governs). This glance authorizes no run.
- INT4 fully blocked. No composition / seam / Claim C claim. No M5 experiment. No V3 retry.
  No construction redesign. Fail-closed on unqualified hop1/composite.
- Path A FP16 K=5 FAIL stays closed. tier0-run sealed (except the read of the INT8 target at run time).
  Paper 2 v1.0/v1.2 + Paper 3 tags preserved.
```

---

— CS Engineer, 2026-06-26
