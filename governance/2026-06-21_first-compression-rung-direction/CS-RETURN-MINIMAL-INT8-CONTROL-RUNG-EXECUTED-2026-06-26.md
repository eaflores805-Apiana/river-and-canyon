# CS RETURN — MINIMAL INT8 CONTROL RUNG EXECUTED

**Date:** 2026-06-26
**From:** CS Engineer
**To:** Manager; Cc: Team Lead, Senior Engineer, C5
**Re:** Execution return for the Manager-authorized minimal INT8 control rung
**Status:** **EXECUTED — instrument-validation readout produced; fail-closed distinctions preserved.** Run-once; not iterated.

**Governing object:** `ONE-PAGE-INT8-CONTROL-RUNG-SPEC-v0.1` (sha256 `8b1a2f14c9e2c52c8442a21bf4402b2dc1a300c64bf65fee955758803b695647`)
**Authorization:** Manager Decision 2026-06-26 — "Authorize Minimal INT8 Control Rung" (by name). Heavier five-gate `FIRST-COMPRESSION-RUNG-AUTHORIZATION-PACKET` route superseded for this rung; retained as historical context.

---

## Required return fields

```text
run directory ........... experiments/2026-06-26_first-compression-rung/
run commit .............. b766f9aa71450c0cd515b28fee31d16a11ca6265
final remote HEAD ....... b766f9aa71450c0cd515b28fee31d16a11ca6265  (this CS-RETURN HEAD-fill commit follows)
clean-fetch confirm ..... PASS — see §clean-fetch below
```

## §clean-fetch verification (post-push)

```text
Fetched origin/main fresh and recomputed the run output content-sha256 from origin blobs:
  fp16_raw_outputs.json   faf461ef…  ✓ matches MANIFEST
  int8_raw_outputs.json   d382838058… ✓ matches MANIFEST
  fp16_scored.json        8db448f2…  ✓ matches MANIFEST
  int8_scored.json        8db448f2…  ✓ matches MANIFEST (identical to fp16_scored)
  CS-RETURN present on origin/main                                     ✓
  INT8 weights ABSENT from origin/main (gitignored, not committed)     ✓ (as intended)
Run committed at b766f9aa; this HEAD-fill commit lands immediately after and is reported in the
turn summary. Bytes verify from the shared remote on clean fetch → FILED.
```

### Pre-run INT8 weight presence confirmation (the required gate)
```text
Required check: INT8 model weights present and loadable on the run machine — PASS.
- model.safetensors PRESENT (3,279,142,791 bytes) and staged into the locked INT8 dir.
- INT8 dir config.json / model.safetensors.index.json / generation_config.json /
  tokenizer_config.json verified BYTE-IDENTICAL to the repo's locked INT8 target
  (sha-equal, all four) — the staged weights are the SAME locked target, NOT a substitution.
- Loadability confirmed empirically at run start: INT8 loaded in 2.0s, FP16 in 3.9s (mlx_lm 0.31.3).
- No substitute INT8 model or alternate quantization path was used.
```

### Model / quantization path
```text
FP16 baseline : Qwen/Qwen2.5-3B-Instruct  (HF cache snapshot revision
                aa8e72537993ba99e69dfaafa59ed015b17504d1 — the locked revision)
INT8 stress   : tier0-run/Qwen2.5-3B-Instruct-mlx-int8  (MLX INT8 of the same revision)
decode        : greedy (temperature 0.0, max_tokens 16), identical params both arms
mlx_lm 0.31.3 · Python 3.13.3 · macOS-26.5.1-arm64 (Apple Silicon) · n=8 matched items
```

### Scorer / prompt / item hashes (re-verified at run time; recorded in MANIFEST.json)
```text
scorer            sha256:b65c6803017b8b04ac25d4bd84c5fb5ff61692ed41d609e099b181fa58e4ddde  (byte-locked Cell03)
prompt_template   sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
items_file        sha256:7d5099cbdccf1f2175e6c693ea851cab73109665d3420be345a475bf835240a1
preregistration   sha256:3fb4dbd4d8daf19be31e95a395abe65175c5968cd3f1b6d50ac08e0bfd4bed03
```

### Raw outputs (retained, E3)
```text
fp16_raw_outputs.json   sha256:faf461ef1f169ee63fb971fbfb84964b3259e7788aa6b30e08fb0bc217cfa283
int8_raw_outputs.json   sha256:d382838058e852c1e2fd770533234a673aba470ec1cd6bac1283a20044939236
NOTE: the two raw-output FILE hashes differ ONLY because each file embeds its own timestamp_utc.
      The generation CONTENT is byte-identical across arms — verified by direct per-generation
      string comparison (see byte-identity below), and the scored-file hashes are equal.
```

### Scored counts
```text
fp16_scored.json  sha256:8db448f21af1e5feafe5fa31b6c15fd739202ba68c666f399fce084a6ff1ebce
int8_scored.json  sha256:8db448f21af1e5feafe5fa31b6c15fd739202ba68c666f399fce084a6ff1ebce   (IDENTICAL)

           hop1     hop2     composite
FP16       0/8      8/8      1/8
INT8       0/8      8/8      1/8
```

### Byte-identity match rate
```text
FP16-vs-INT8 raw-output byte-identity: 24/24 generations identical · match_rate 1.0000 · zero mismatches.
chat-prompt sha identical across arms: yes (same prompts on both arms).
```

### hop2 readout (the permitted output)
```text
The INT8 control rung produced a bounded hop2-only instrument-validation readout: FP16 8/8 and INT8 8/8,
byte-identical. Per the carried-forward 2026-06-15 disposition, these hop2 outputs are single-fact
retrieval, NOT chain composition — legitimate but not load-bearing, not evidence of two-hop reasoning.
INT8 produced no behavioral perturbation in this setup.
```

### hop1 fail-closed disposition
```text
hop1 0/8 — unqualified; logged, fail-closed. No INT8 retention claim produced for hop1.
```

### composite fail-closed disposition
```text
composite 1/8 — unqualified (unmet hop1 precondition); logged, fail-closed. No INT8 retention claim
produced for composite. The instrument preserved the fail-closed distinction between the readout-eligible
hop2 and the unqualified hop1/composite.
```

### Boundary confirmations
```text
- No INT4 was run.                                  CONFIRMED (FP16 + INT8 only)
- No construction redesign occurred.                CONFIRMED (locked n=8 c03_i01..i08; same items/prompts/scorer)
- No Claim C / seam / composition claim was made.   CONFIRMED (single-hop hop2 readout only; see DISPOSITION.md)
- 2026-06-15 sealed bytes untouched.                CONFIRMED (ran in a fresh dir with a byte-identical runner copy)
- Staged weights NOT committed.                      CONFIRMED (symlinks removed post-run; only run-dir artifacts staged)
```

## Allowed-language conformance check (CS, pre-file)

CS checked this return and `experiments/2026-06-26_first-compression-rung/DISPOSITION.md` against the spec's allowed/forbidden lists. The readout uses only the three allowed statements (bounded hop2 instrument-validation readout; no behavioral perturbation in this setup; fail-closed distinctions preserved). None of the forbidden phrasings appear (no "preserves reasoning/capability," "robust to quantization," "composition survived," "seam tested," "Claim C moved," "V3 fixed," "M5 resolved," "INT4 would behave the same"). **No new claim language introduced → no C5 routing required** per the spec's tripwire.

## What this rung established (and did not)

It validated the instrument's mechanics on the readout-eligible target and its fail-closed behavior on the unqualified types, under INT8 at 3B, on n=8, once. INT8 applied no perturbation here (byte-identical), so this is a calibration result, not a retention-decay demonstration — a meaningful decay test would need a harsher rung (INT4), which is out of scope and remains blocked.

---

## Non-authorizations (carried forward)

```text
- INT4 fully blocked. No composition / seam / Claim C / capability / mechanism / certification claim.
- No M5 experiment · no V3 retry · no construction redesign.
- Path A FP16 K=5 FAIL stays closed. tier0-run sealed. Paper 2 v1.0/v1.2 + Paper 3 tags preserved.
- This was a control / calibration rung only; it authorizes nothing downstream.
```

---

— CS Engineer, 2026-06-26
