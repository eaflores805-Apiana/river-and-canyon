# Carved-Path Pattern List — a thinking tool

*A reference object, not a finding. This is the full raw output of the carving analogy used as a pattern generator — laid out so it can be examined and thought against. It is **not** a taxonomy, **not** evidence of model internals, and **not** a protocol category list. Its companion framing — including why the high match-rate is a caution rather than a credential — is in [`open-question-uneven-support.md`](open-question-uneven-support.md). Read that first; this list only makes honest sense alongside it.*

---

## How to read this list (the one thing that matters)

Every row below "matches" a real LLM error. That is exactly why the list must be read carefully: **the matching is post-hoc.** Each pattern was named to fit an error already known, not predicted in advance — and every match reduces to a failure family the field established without any analogy. So the list is not a scorecard showing the analogy is right (a frame that fits everything proves nothing). It is a record of the analogy's *generative reach*, kept as raw material for thinking, with the understanding that **reach is not validity.**

The two right-hand columns are deliberately not "does this error exist / how strong is the match" (the original framing, which dresses post-hoc fit as confirmation). They are: the **field-established family** the pattern collapses into, and its **status** — which is the same for almost every row, on purpose.

---

## The list

| # | Carved-path pattern | Behavioral error it suggests | Field-established family it reduces to | Status |
|---|---|---|---|---|
| 1 | Shallow groove | Vague, generic answer; loses specificity under stress | Stress-retention loss | post-hoc; field-owned |
| 2 | Incomplete groove | Starts correctly, fails before completing | First-error-step / truncated execution | post-hoc; field-owned |
| 3 | Discontinuous groove | Does A and B alone, fails A→B chain | Compositional-generalization failure | post-hoc; field-owned, possible test target |
| 4 | Mis-carved groove | Consistently follows a wrong heuristic | Shortcut learning | post-hoc; field-owned, correctness-guard required |
| 5 | Stray groove | Veers off-topic / irrelevant association | Perturbation / attention drift | post-hoc; field-owned |
| 6 | Over-deep groove | Overuses a memorized pattern inappropriately | Memorization / over-application | post-hoc; field-owned |
| 7 | Crossed grooves | Context conflict causes answer flip | Context contamination | post-hoc; field-owned |
| 8 | Braided grooves | Two patterns interfere; output blends them | Interference / fact mixing | post-hoc; field-owned |
| 9 | Eroded groove | Weakens under quantization, pruning, noise, long context | Stress-retention loss | post-hoc; field-owned |
| 10 | Narrow ridge / tight channel | Exact symbolic task fails from tiny perturbation | Perturbation sensitivity | post-hoc; field-owned |
| 11 | Wide basin | Fluency survives while precision decays | Fluency–correctness dissociation | post-hoc; field-owned |
| 12 | Forked path | Unstable answers across paraphrases | Prompt / paraphrase sensitivity | post-hoc; field-owned |
| 13 | False outlet | Coherent reasoning, wrong final answer | Fluency–correctness dissociation | post-hoc; field-owned |
| 14 | Dead end | Repeats, stalls, refuses, cannot continue | Degeneration / refusal | post-hoc; field-owned (looser fit) |
| 15 | Loop in path | Repetition loops / circular reasoning | Degeneration | post-hoc; field-owned |
| 16 | Blocked channel | Safety/format constraint blocks a possible answer | Refusal / format constraint | post-hoc; field-owned (looser fit) |
| 17 | Weak bridge | Intermediate state not preserved across steps | Chain / state-transfer failure | post-hoc; field-owned |
| 18 | Over-smoothed channel | Collapses distinctions, treats cases as same | Over-generalization | post-hoc; field-owned |
| 19 | Rough walls | Small wording → large output variation | Perturbation sensitivity | post-hoc; field-owned |
| 20 | Sediment / debris | Irrelevant context contaminates answer | Context contamination | post-hoc; field-owned |
| 21 | Shortcut trench | Exploits benchmark artifact / position cue | Shortcut learning / benchmark artifact | post-hoc; field-owned |
| 22 | Flooded channel | High-probability language overwhelms rare correct answer | Frequency bias | post-hoc; field-owned |
| 23 | Dry channel | Rare task/domain answered poorly | Long-tail / coverage weakness | post-hoc; field-owned |
| 24 | Parallel grooves | Plausible completions compete; framing decides | Prompt sensitivity | post-hoc; field-owned |
| 25 | Collapsed wall | One error cascades into many | Autoregressive error cascade | post-hoc; field-owned (confound-controlled) |
| 26 | Uneven depth | Easy cases survive stress; hard cases collapse | Stress-retention loss | post-hoc; field-owned |
| 27 | Wrong merge point | Combines facts from different entities/events | Interference / fact mixing | post-hoc; field-owned |
| 28 | Path too short | Local reasoning works, long-horizon fails | Composition / long-horizon failure | post-hoc; field-owned |
| 29 | Overfit groove | Works on benchmark format, fails reformat | Overfitting to format | post-hoc; field-owned |
| 30 | Hidden sinkhole | Fluent, confident, subtly false | Fluency–correctness dissociation | post-hoc; field-owned |

---

## What the list collapses to

Thirty rows reduce to about seven field-established families. This is the actual content — the rest is vocabulary:

- **Stress-retention loss** — rows 1, 9, 26 (and the project's one analytic survivor lives near here)
- **Composition / state-transfer failure** — rows 3, 17, 28
- **Shortcut / robust-wrong behavior** — rows 4, 21
- **Perturbation / prompt sensitivity** — rows 5, 10, 12, 19, 24
- **Interference / contamination** — rows 7, 8, 20, 27
- **Fluency–correctness dissociation** — rows 11, 13, 30, 22
- **Autoregressive error cascade** — rows 2, 25

None of these were discovered by the analogy. All were established by the field. The list shows the analogy can be *mapped onto* them, fluently — which is the generative reach worth thinking about, and the unfalsifiability worth being wary of, in equal measure.

---

## Using this to think differently (the legitimate purpose)

This is the part that makes the object worth keeping. As a thinking tool — not a claim — the list invites a few genuinely open questions:

- Is there a *generative grammar* under the seven families — a smaller set of underlying failure modes (under-support, over-support, poor-connection, interference, stress) that the thirty surface patterns are combinations of?
- Does the same small grammar describe failure in *other* learned systems (habits, motor skills, roads, workflows)? — the cross-domain question parked in the open-question note.
- For any row: **what observation would make it false?** Most rows, as written, forbid nothing. The ones that could be sharpened into a forbidden outcome are the only ones with any future. (Row 3 / composition and row 4 / shortcut are the closest, which is why they are the two pressure-test survivors.)

The discipline, carried from everything else: a row earns its way out of "thinking tool" only by becoming a behavioral signature with a control and a falsification path — at which point the carving vocabulary is dropped and only the measurement remains.

*A reference to think with, Apiana AI. Not a finding, not a taxonomy, not evidence. Companion to `open-question-uneven-support.md`.*
