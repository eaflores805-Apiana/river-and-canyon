# Open Question — The Uneven-Support Pattern (a thing to ponder, not a finding)

*A side note, not a result. This is a parking space for an idea worth returning to, recorded with both its appeal and its trap so that a later reading gets the honest version of each. It is not in the protocol, not in Tier 0, not a claim about model internals, and not part of the analogy's two pressure-test survivors. It is a question to think about — nothing here is established.*

**Status: v1.0 — parked open question** (stable, but not "locked" the way the protocol is; open questions are allowed to evolve). **The one-line guardrail for this whole branch: *reach is not validity.*** The raw object to think against is [`carved-path-pattern-list.md`](carved-path-pattern-list.md).

---

## The idea, stated plainly

The carving analogy, beyond its two durable survivors, can be used to generate a long list of failure patterns — shallow paths, weak bridges, shortcut trenches, forked paths, crossed paths, collapsed walls, and so on. Each one *seems* to map onto a real LLM error mode. The tempting inference is that the analogy is unusually generative.

There may be a deeper and more interesting idea underneath that temptation — but it is not the one it first looks like.

## The trap (record this first, so it isn't forgotten)

The surface version — "the analogy generated ~30 patterns that match ~30 real LLM errors, therefore it captures something real" — does not survive scrutiny, for one decisive reason: **the matching is post-hoc.** The patterns were named to fit errors already known, not predicted before they were observed. And every match reduces to a failure family the field already established without any analogy: compositional-generalization failure, shortcut learning, prompt/format sensitivity, context contamination, fluency–correctness dissociation, autoregressive error cascade.

The high match count is therefore not a strength signal. It is the opposite. **A frame flexible enough to be draped over almost any known failure mode after the fact has correspondingly little discriminating power** — it cannot be wrong, which means it cannot be evidence. This is the same reason the 7-type (then 30-type) defect taxonomy was retired across the pressure tests. Any future version of this idea has to clear that bar first: *what does it forbid?* If it forbids nothing, it is unfalsifiable, however rich it looks.

## The part actually worth pondering

Set the LLM-specific table aside. The residue worth thinking about is more general and more honest:

> Is "how a learned pathway fails when its support is uneven" a real abstract pattern that recurs across very different substrates — language models, human habits, motor skills, footpaths and roads, organizational workflows, manufacturing process windows?

That question has some pull, because the vocabulary does seem to transfer: under-reinforced routes are fragile, over-reinforced ones are rigid and over-applied, poorly-connected ones fail at handoffs, and all of them degrade under stress. The phrase "path of least resistance" is a cliché precisely because the intuition is old and broad.

But pull is not evidence, and the honest status of even this version is: **unproven, possibly unfalsifiable as stated, and not obviously testable.** It may be a genuine structural regularity; it may just be that "things that are unevenly built fail unevenly" is true by near-tautology and feels deep because it is vague. The work to make it more than a shower thought would be to state it in a form that *forbids* some observable outcome — and it is not at all clear that form exists.

**A candidate explanation for the pull — and the overclaim to avoid.** There is a real reason the carving vocabulary transfers as readily as it does: physical paths, learned behaviors, and model training can all be described, at a high level, as constrained optimization processes shaped by uneven support — erosion and trail formation, gradient descent, and habit formation are not literally the same kind of system, but they share that coarse description. Systems of that kind tend to share gross structural features — basins where many paths converge, ridges that require precision to stay on, brittle low-density routes versus over-determined high-density ones, sequential error propagation, interference when too much is forced through limited capacity. So the match-rate is better explained by "these are both constrained optimizations on uneven landscapes" than by anything mystical, and that is genuinely why the morphology seems to recur across substrates (models, habits, roads, workflows). **But this is a shared *abstraction*, not a demonstrated isomorphism.** The tempting next step — "it is not a metaphor, it is literally the same vector calculus, the systems are structurally identical" — overshoots: calculus also describes orbits and population dynamics, and we do not call orbits and rabbits isomorphic. Sharing a mathematical *framework* (cost minimization) is not the same as a structure-preserving map between two specific systems, which no one here has shown. So the honest form of the insight is: *the analogy transfers because cost-minimization-on-uneven-terrain is a broad abstraction many systems share — which explains the reach and, again, is a caution about discriminating power, not a secret rigor that upgrades the analogy to mechanism.*

**The cleaner durable form: parameters, not defects.** If anything from the carving analogy is worth keeping as a *lens*, it is probably not the list of failure shapes but the small set of **parameters** underneath them. A "defect" smuggles in a claim that something went wrong internally (the mechanism overclaim the boundary forbids); a "parameter" only names an observable property of behavior. The thirty surface patterns appear to be expressions of perhaps seven such parameters: **support/frequency, margin/depth, variability/width, connection/continuity, competition/branching, interference/intersection, and stress-resistance/erosion.** That small grammar is the better explanation for the high match-rate — the analogy was never listing thirty distinct things; it was re-combining seven parameters, which is why it can generate so many visible failures. This reframing is genuinely cleaner and fits the boundary exactly: the analogy *suggests candidate behavioral parameters*, the protocol keeps only what can be measured, and mechanism stays blocked. Put most compactly: the analogy is **less true but more useful** — not a map of the machine, but a generator of rulers. Less true because it is no longer treated as a picture of internals; more useful because it yields measurable behavioral dimensions.

But the same discipline applies, and it cuts a useful way here. A parameter earns attention only if it can be phrased as a measurement that *forbids an outcome* — and when each of these is made measurable, it lands on something already in scope: **depth** = "does behavior survive quantization?" is literally Tier 0; **width** = paraphrase/format invariance is prompt sensitivity (field-owned); **interference** = distractor sensitivity is context contamination (field-owned); **frequency** = "do high-frequency patterns retain better than rare ones?" is the coverage/Zipf question (field-owned). So the parameter grammar adds no new claim — it is a *generative lens* whose good outputs point at measurements the protocol or the field already has. That is exactly its proper value: a cleaner way to see why the known measurements cluster, not a new program to build. The sharpened ponderable is therefore not "is there a grammar?" but: *here is the candidate grammar — which of its seven parameters can be stated so as to forbid an outcome, and which are just vocabulary?* The clearest candidates are margin/depth and connection/continuity; they align with the project's live measurement target (stress-retention) and the compositional-seam diagnostic respectively. The retention-≠-correctness survivor stays *separate* from this grammar on purpose: it is a metric boundary — a statement about what the retention measure can and cannot see — not a path parameter, and folding it into the parameter list would blur the cleanest distinction the project has.

## Why it is parked here and not elsewhere

- **Not in the protocol / Tier 0 / diagnostic addendum** — those stay strictly non-analogical and measurement-bound. This idea is the opposite of measurement-ready.
- **Not in the papers** — they are posted, and this is too unformed (and too close to the retired taxonomy) to add to a live document.
- **Not a claim-ledger row** — it is not a claim; it is a question. The ledger notes only that the analogy's exploratory output does not upgrade its claim status.
- **Here, as an open question** — because it is worth returning to *as a thinking prompt*, and the honest way to keep a tempting-but-unproven idea is to write down both why it is tempting and why it has not earned more than a parking space.

The full raw pattern list this note refers to — the ~30 carved-path patterns laid out as an object to think against — is in [`carved-path-pattern-list.md`](carved-path-pattern-list.md). It is a thinking tool, not a finding; read it only alongside this framing.

## If this is ever picked back up

The first test is not "does it generate matches" (it always will — that is the trap). The first test is: **state one outcome the pattern forbids.** If that can be done, there may be something here. If it cannot, it stays a pleasant cross-domain intuition — enjoyed, not claimed.

*A note to think with, Apiana AI. Not a finding. Recorded so the idea is not lost and not overclaimed.*
