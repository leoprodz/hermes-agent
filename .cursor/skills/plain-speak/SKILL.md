---
name: plain-speak
description: Translate tech talk into plain language for non-developers.
disable-model-invocation: true
---

# Plain speak

Turn technical explanations into language a non-developer can use to decide or act. No jargon wall. No talking down.

## When to use

- User says they are not a developer, or asks “explain simply / in human terms.”
- You just used git, APIs, PRs, envs, CLIs, agents, skills, etc., and need a second pass.
- A concept must stick (what to keep, what to ignore, what to do next).

**Not this skill:** cleaning AI writing style → `/unslop`. Restating only your *last* reply in fewer words → `/bro`. Teaching how a subsystem works in depth → `/teach`.

## Relationship to `/bro`

| | `/bro` | `/plain-speak` |
|---|---|---|
| Scope | Rewrite the last message | Explain a concept, decision, or passage |
| Output | Same content, simpler | Analogy + what it means for them + next step |
| Tone | Brief restatement | Patient translation |

If they only said “say that again without jargon,” `/bro` is enough. If they need to *understand a system*, use this.

## How to rewrite

1. **Name the thing in everyday words first.** One or two sentences. Lead with meaning, not the tech name.
2. **One analogy max**, from daily life (folders, shared docs, assistants, kitchens). Drop it if it fights the idea.
3. **Then map the tech terms** only if they will see them again: “In the tool this is called X.”
4. **Say what to do / not worry about.** Non-devs need the decision, not the mechanism.
5. **Keep respect.** Never “basically” as a brush-off. Never fake-ELI5 cuteness. Adult plain language.

## Shape of a good answer

```text
[Plain meaning in 1–3 sentences]

[Optional: one analogy]

[Only if useful: “When you hear ___, it means ___.”]

[What matters for you / what you can ignore]
```

## Forbidden

- Stacking undefined acronyms (PR, CI, SHA, RPC) without a plain gloss on first use.
- “Simply configure the toolchain…” — still tech.
- Longer than the original unless the original was a pile of terms that needed unpacking.
- Inventing product behavior to make the analogy prettier.

## Examples

**Bad:** “`.cursor/` is gitignored so it won’t be in the remote after clone.”

**Good:** “Some files in this project are set aside as ‘local only’ — like sticky notes on your desk that don’t go into the shared binder. `.cursor/` is that pile. `notes/` is binder material: if we save it to the shared project, it shows up on another computer too.”

**Bad:** “Build the Lever means prefer a deterministic harness over stochastic agent improvisation.”

**Good:** “Build the Lever means: give the assistant a small remote control that always works the same way, instead of asking it to invent a new recipe every time. That remote control is usually a tiny command-line tool.”
