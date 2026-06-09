# Runner Amendment Lock Note — Two-Hop Level 1

**Date:** 2026-06-08
**Prepared by:** CS Engineer
**Authorization:** Manager memo — "FP16 Stage 1 Run Escalation — Disposition and Runner Amendment Authorization" 2026-06-08
**Disposition:** Voided run accepted as VOID; Option R1 authorized; rerun authorized under amended runner

---

## 1. Voided run artifact

```
Path:    tier0-run/RESULTS-TWOHOP-L1-cell01-1780911140.json
Status:  VOID — environment / runner incompatibility

Rationale:
  96/96 outputs begin with ANSWER:
  The model followed the format prefix in every case.
  Format failures were caused by trailing continuation / EOS mishandling under
  mlx_lm 0.8.0 with Qwen2.5-Instruct raw prompts (no chat template applied).
  This is a serving-stack / runner-mode incompatibility, not interpretable
  model constructibility behavior.

Use restriction:
  This artifact may be cited only as an environment/runner disposition record.
  It may not be used as Stage 1 data, Gate 1 evidence, constructibility evidence,
  or model-behavior evidence.
```

---

## 2. Old runner path and hash

```
Path: tier0-run/runner_twohop_l1.py
Hash: sha256:ed2fbdc3e21375060f15a0645da111c24db890b840d9be476ee24d8bb06c5aaf
```

---

## 3. Amended runner path and new hash

```
Path: tier0-run/runner_twohop_l1.py   (same path — in-place amendment)
Hash: sha256:f346e4f2cf93b881e129ba25bea469e2f6349ce1b6d430f8ddfb7269f3d0d7ce
```

---

## 4. Exact code change summary

Three targeted changes. All other runner logic, constants, and provenance checks unchanged.

### Change 1 — Step 4 import (line ~201)

```python
# Before:
from mlx_lm import load, generate

# After:
from mlx_lm import load, stream_generate
```

### Change 2 — Dry-run section: prompt rendering display added

Added after Step 3 dry-run check, before the `return`:

```python
template_dr = PROMPT_TEMPLATE_PATH.read_text()
print("Rendering sample prompts (item[0], 4 query types) — chat-template format check:")
sample_item = items[0]
for qt in QUERY_TYPES:
    raw_text = render_prompt(sample_item, qt, template_dr)
    if tokenizer is not None and getattr(tokenizer, "chat_template", None) is not None:
        chat_text = tokenizer.apply_chat_template(
            [{"role": "user", "content": raw_text}],
            add_generation_prompt=True, tokenize=False,
        )
        print(f"  [{qt}] chat_template: OK  raw={len(raw_text)}chars  formatted={len(chat_text)}chars")
    else:
        print(f"  [{qt}] no chat_template  raw={len(raw_text)}chars")
```

### Change 3 — Inference loop: replace `generate()` with chat-template + `stream_generate()` (Step 6)

```python
# Before:
raw_output = generate(
    model, tokenizer,
    prompt=prompt,
    temp=DECODING_SETTINGS["temperature"],
    max_tokens=DECODING_SETTINGS["max_tokens"],
    verbose=False,
).strip()

# After:
chat_prompt = prompt
if getattr(tokenizer, "chat_template", None) is not None:
    chat_prompt = tokenizer.apply_chat_template(
        [{"role": "user", "content": prompt}],
        add_generation_prompt=True, tokenize=False,
    )
raw_output = ""
for _seg in stream_generate(
    model, tokenizer,
    prompt=chat_prompt,
    max_tokens=DECODING_SETTINGS["max_tokens"],
    temp=DECODING_SETTINGS["temperature"],
):
    raw_output += _seg
raw_output = raw_output.strip()
```

**Invariants preserved by amendment:**
- `prompt_hash_rendered` is still computed from the raw rendered text (before chat-template encoding), preserving content-level prompt identity
- `DECODING_SETTINGS["temperature"] = 0.0` — deterministic greedy decoding unchanged
- `max_tokens = 16` unchanged
- Scoring: `classify_output(raw_output, item, qt)` — scorer contract unchanged; format regex `^ANSWER:\s+[A-Z]{4,8}$` applied to the raw model output as before
- No answer-specific cleanup; no first-line extraction; no post-hoc filtering

---

## 5. mlx_lm version used

```
mlx_lm version: 0.19.3
stream_generate: confirmed present
generate_step accepts temp=: confirmed (inspect.signature shows 'temp' as first kwarg)
```

---

## 6. Tokenizer / chat-template source

```
Tokenizer:     Qwen/Qwen2.5-3B-Instruct (FP16, HuggingFace)
File:          ~/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/
               snapshots/aa8e72537993ba99e69dfaafa59ed015b17504d1/tokenizer.json
Hash:          sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
Chat template: tokenizer.chat_template attribute (Qwen2.5-Instruct format)
               Wraps content in <|im_start|>user ... <|im_end|> / <|im_start|>assistant
               add_generation_prompt=True appends <|im_start|>assistant\n
               tokenize=False returns formatted string for passage to stream_generate
EOS token:     <|im_end|> (id 151645) — stream_generate stops when token == eos_token_id
```

---

## 7. Dry-run confirmation (amended runner)

```
python runner_twohop_l1.py --dry-run

Step 1: Recording provenance hashes...
  runner_hash:           sha256:f346e4f2cf93b881e129ba25bea469e2f6349ce1b6d430f8ddfb7269f3d0d7ce
  manifest_hash:         sha256:00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28
  validator_hash:        sha256:bcc26ca04b0c5a21db496d08c9307d2e6257315a9376f04473ea68ae36ca349b
  scorer_hash:           sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd
  prompt_template_hash:  sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
  validator_hash: OK
  scorer_hash: OK
Step 2: Loading and validating manifest...
  validate_manifest(): 24/24 pass
Step 3: Confirming FP16 tokenizer hash...
  tokenizer_hash: sha256:c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
  tokenizer_hash: OK
Dry-run mode: provenance and manifest checks complete.
Rendering sample prompts (item[0], 4 query types) — chat-template format check:
  [hop1]          chat_template: OK  raw=438chars  formatted=586chars
  [hop2]          chat_template: OK  raw=437chars  formatted=585chars
  [composite]     chat_template: OK  raw=463chars  formatted=611chars
  [negative_graph] chat_template: OK  raw=442chars  formatted=590chars
No model inference performed.
runner_hash: sha256:f346e4f2cf93b881e129ba25bea469e2f6349ce1b6d430f8ddfb7269f3d0d7ce

Result: PASSES
```

---

## 8. Invariance confirmation

```
Cell JSON (items_twohop_l1_cell01.json):
  Hash:    sha256:00a7adf88165a174b66c5f6045282d37c6c9efb63c3823eff666e00cb8024a28
  Status:  UNCHANGED — same locked cell as void run

Scorer (scorer_twohop_l1.py):
  Hash:    sha256:060afad9db6fc56dc222d8dc1e856fa28fd379811269d899317dbd660c4a91bd
  Status:  UNCHANGED — same amended locked scorer as void run

Thresholds (THRESHOLD-PROPOSAL-TWOHOP-L1.md):
  Status:  UNCHANGED — Revision 2 locked thresholds; no threshold changes

Prompt template (prompt_template_twohop_l1.txt):
  Hash:    sha256:c8a81a299d28c3fd47f4d6fc90c4c57537885d07f01464e68d6fbe2e94a2510e
  Status:  UNCHANGED — same locked template; prompt intent preserved

Prompt content: raw rendered text (before chat-template encoding) is unchanged.
  The chat template adds Qwen2.5-Instruct formatting markers only; it does not
  alter the facts, query, or answer-format instruction contained in the prompt.
```

---

## 9. Updated EXPERIMENT_LOG.md entry

EXPERIMENT_LOG.md updated 2026-06-08:
- Authorization boundary section updated: Stage 1 execution authorized; voided run documented; runner amendment documented; rerun authorized
- Key Files table updated: runner hash corrected to sha256:f346e4f2...; scorer hash corrected to sha256:060afad9...; cell JSON hash corrected to sha256:00a7adf8...; voided run artifact row added; this lock note row added

---

**Runner amendment locked. Rerun authorized under amended runner.**

— CS Engineer, 2026-06-08
