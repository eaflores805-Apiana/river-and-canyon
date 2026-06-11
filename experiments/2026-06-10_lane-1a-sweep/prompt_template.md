# Lane 1a Prompt Template (locked; hash-recorded in LOCK-RECORD.md)

Format contract: every prompt is a single string with the structure below.
Trailing whitespace stripped. No system message; no role separators
beyond what the Qwen2.5-3B-Instruct tokenizer expects for plain text input.

```
You are answering retrieval queries against a fixed list of key-value pairs.
Respond with exactly the value associated with the queried key, on a single line,
with no additional text. If the queried key does not appear in the list, respond
with NULL on a single line.

List:
{IN_CONTEXT_LIST}

Queried key: {QUERIED_KEY}
Answer:
```

## Substitution rules

- `{IN_CONTEXT_LIST}` — newline-separated `key: value` pairs, one per
  line, in the order given by the manifest (which is deterministically
  permuted by `manifest_generator.py` from the per-rung seed).
- `{QUERIED_KEY}` — the single key whose value the model is asked to
  produce (or NULL if absent).

## Format contract preservation

The template is bit-identical across:
- Answerable items (queried key in list; expected answer is the value).
- NULL items (queried key absent from list; expected answer is NULL).
- Answerable-mirror controls (scrambled bindings; queried key in list).
- Null-mirror controls (scrambled bindings; queried key absent from list).

The model receives the same prompt structure in every case. Only the
binding content varies. This is required by Lane 1a's token-prior
control discipline (any structural difference would confound the
control with the candidate).

## Extended-context padding (X = extended)

For rungs with X = extended (L07, L08), the manifest generator prepends
deterministically-generated tokenization-stable padding lines to bring
the total prompt length to `extended_context_target_tokens` (2,048 by
locked criteria). Padding lines are formatted to match `key: value`
syntax to preserve the format contract; the queried key is never in
the padding by construction.

## Locked
Edits after lock are prohibited; corrections require a new sweep packet
with a new LOCK-RECORD.
