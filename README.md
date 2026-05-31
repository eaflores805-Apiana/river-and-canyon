# The River and the Canyon

**A Physical Blueprint for Large Language Models**

E. A. Flores · Apiana AI, Inc. · May 2026

---

Most explanations of large language models are either too loose (a "digital
brain that thinks") or too dense (a wall of linear algebra). This paper takes a
third path: it maps the real operations of a transformer onto one sustained
physical picture — weights as a frozen, solid mountain, activations as water
flowing over it, training as the slow carving of the rock, inference as water
finding paths across stone that no longer moves.

The governing distinction is permanence: grooves carved by training are
permanent, channels laid down by attention are not — and that single axis is
exactly the difference between weights and activations. The picture is held
consistently from tokenization through attention, the residual stream, and the
feed-forward block, and on into production techniques — KV caching,
FlashAttention, LoRA, grouped-query attention — and finally to where it breaks,
in a candid account of superposition, discreteness, and the decoder-only
assumption.

It is written for the technically literate non-specialist who wants an intuition
they can reason from, debug with, and explain to others.

---

**[Read the paper (PDF)](the-river-and-the-canyon.pdf)**

*Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — share and adapt with attribution, non-commercial use only.*
