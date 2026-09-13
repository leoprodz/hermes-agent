# pstack labs — from Lauren’s articles → Hermes experiments

**Articles (full text):** [`pstack-articles/`](./pstack-articles/) · index [`notes/README.md`](./README.md)

Through-line: **F-01** (Grokbot-like bot visibility) + this repo.  
Harness: `verify-hermes` / `control-hermes` (Lauren’s `/control-app` equivalent).  
Mode setup: light `inherit-parent` in `~/.cursor/rules/pstack-models.mdc`.

Copy a prompt into a **new chat** unless the lab says “same chat.” Prefer starting with `/poteto-mode` when the lab is multi-step.

### How Leo learns these labs (agents: read this)

On “vamos con Lab X” (new chat or same): **brief first, apply only after he says so.**

Required briefing shape (same as Lab D pre-brief): prior-labs table → **contrast** (forma no recomendada vs forma pstack) → name the pieces → why it matters for understanding pstack → scope / what to ignore → ask “¿Arrancamos?”

Durable rule: `.cursor/rules/pstack-lab-teaching.mdc`.

Legend: ✅ done · ⏭ next · 🔒 later (needs more setup)

---

## Already done

| Article beat | Lab | Status |
|---|---|---|
| `/setup-pstack` | Light inherit-parent | ✅ |
| `/create-verification-skill` | `.cursor/skills/verify-hermes/` + prove version | ✅ |
| Feature Map seed | 4 CLI features under `verify-hermes/features/` | ✅ |
| Lab C — Maintain the map | `list-sessions.md` + F-01 TODOs in README | ✅ |
| Cloud agents > worktrees | Cloud subagents for Grokbot research | ✅ (taste) |

---

## Part 1 — Verification is all you need

### Lab A — Close the loop (feel the bottleneck) ⏭
**Skill:** none (baseline)  
**Experience:** one CLI flow without verification; note where *you* were the checker.

```text
Run `hermes config set display.skin default` under a disposable HERMES_HOME
yourself (no verify-hermes). Tell me every place a human had to look to know
it worked. Do not use control-hermes.
```

**Done when:** short list of bottlenecks (exit code, file path, get vs set…).

---

### Lab B — Build the Lever (use the CLI, don’t paste markdown)
**Principle:** Build the Lever · harness: `control-hermes`  
**Experience:** agent drives Hermes only via the helper.

```text
/poteto-mode
Use only `.cursor/skills/verify-hermes` + `control-hermes`.
Launch an isolated home, doctor, then drive features/get-set-config.md
end to end. Show me the evidence paths. Cleanup home; keep evidence.
```

**Done when:** evidence under `/tmp/hermes-verify-evidence/<id>/` proves set→get without you opening the YAML.

---

### Lab C — Maintain the map ✅
**Skill:** `/maintain-verification-skill`  
**Experience:** map drifts; maintenance catches it.

```text
/maintain-verification-skill
Our verify-hermes map only covers CLI version/doctor/status/config.
Walk the real `hermes --help` surface and propose the next 3 feature files
that matter for F-01 (agents / delegation / desktop agents panel).
Update the map only for ONE new feature you can prove today with control-hermes
or a documented CLI command. Prove it. Leave the rest as TODO in features/README.md.
```

**Done when:** one new feature file + proof transcript; README lists deferred F-01 surfaces.

---

### Lab D — `/poteto-mode` + verify (feature recipe from Pt.1)
**Skills:** `/poteto-mode`, `verify-hermes`  
Lauren’s pattern adapted:

```text
/poteto-mode
Add a tiny CLI nicety that helps F-01 discovery: make `hermes agents --help`
(or the real agents/status command that exists) print one extra line pointing
humans to where live agent visibility lives today (TUI /agents, Desktop /agents).
Use verify-hermes for any hermes CLI checks. Show evidence. No Desktop UI work yet.
```

**Done when:** behavior proven via `control-hermes` (or equivalent CLI evidence), tiny diff.

---

### Lab E — `/swarm` + verification (sample size)
**Skill:** `/swarm`  
Lauren: fan-out verification to confirm no regression.

```text
/poteto-mode
After Lab D (or on current main), /swarm 3 workers:
each launches its own RUN_ID via control-hermes and runs
version + doctor + config get/set recipes from verify-hermes/features.
Aggregate: all green or list failures with evidence paths.
Do not use worktrees; prefer parallel Task/cloud workers with isolated HERMES_HOME.
```

**Done when:** 3 independent evidence dirs; one summary table.

---

### Lab F — Cloud agent build (optional, when Desktop enters)
**When:** you tackle Desktop activity-feed UI.  
Lauren’s cloud prompt adapted:

```text
Spawn a cloud agent:
/poteto-mode prototype a read-only "inter-agent activity" side pane concept
for Desktop Agents. use verify-hermes for CLI contracts; for UI, capture
screenshots. Do not merge. Open a draft PR or leave a branch.
```

🔒 until Labs B–E feel easy.

---

## Part 2 — Supervising someone smarter than you

### Lab G — Indirect prompt (restate first)
**Pattern:** no leading the witness.

```text
/poteto-mode
Read notes/hermes-frictions.md F-01 and the exploration notes there.
Restate in your own words, in plain English, what the underlying product gap is
— before proposing any solution. Do not design yet.
```

**Done when:** you correct or accept the restatement; mismatch caught *before* code.

---

### Lab H — `/how` (runtime mechanics)
```text
/how does Hermes subagent / delegate_task progress get to the TUI /agents overlay
and the Desktop Agents panel? Trace events end to end with file citations.
```

**Done when:** you can sketch the event path in 5 boxes without opening the chat.

---

### Lab I — `/why` (intent / history)
```text
/why do child subagents strip send_message / peer chat capabilities?
What failure modes was that protecting? Cite commits/PRs/docs if present.
```

**Done when:** tradeoff is clear (loops, side effects) — grounds F-01 design constraints.

---

### Lab J — `/teach` (compress for you + agent)
```text
/teach me how Hermes multi-agent visibility works today versus what Grok Bot’s
public docs describe (roster + group handoffs). Use /how and /why underneath.
No implementation. I want the mental model.
```

**Done when:** 1-page mental model you trust enough to brief a spike.

---

### Lab K — `/recall` (context across chats)
Use after you’ve done G–J in prior chats:

```text
/recall our F-01 exploration and pstack labs so far, then outline the smallest
spike for an inter-agent activity feed using existing subagent events.
```

**Done when:** spike outline cites prior evidence, not a cold restart.

---

### Lab L — Plan with code (`prototype` playbook)
**Playbook:** `prototype` (via `/poteto-mode`)

```text
/poteto-mode prototype 2–3 options for showing inter-agent activity while I stay
in one primary Hermes session:
A) TUI-only feed under /agents
B) Desktop side pane on Agents route
C) CLI `hermes agents activity --follow` transcript feed
For each: sketch UX in markdown + name the event sources. Prefer throwaway
sketches over abstract architecture. Use verify-hermes where CLI is involved.
I will pick; do not implement the full feature yet.
```

**Done when:** you choose A/B/C from artifacts, not vibes.

---

### Lab M — `/architect` (measure twice)
```text
/architect the chosen option from Lab L for an inter-agent activity feed.
Ground with /how on existing subagent events. Competing design runners OK.
Scrap if types need `any` escape hatches. Stop at sketch + proof plan;
implementation is the next poteto-mode feature playbook.
```

**Done when:** typed sketch + verification plan; no giant abstract design doc.

---

### Lab N — README / tutorial-driven (API surface)
**Skill:** `/technical-writing`

```text
/technical-writing
Write a short tutorial (Diátaxis tutorial mode only) for a future user:
"How to watch other agents while you talk to one" — as if the feature existed
with the Lab M sketch. No implementation dump. This tutorial is the contract.
```

**Done when:** tutorial is the acceptance test for the later feature PR.

---

### Lab O — Turn design into verified plan
```text
/poteto-mode turn the Lab M/N design into a plan of small PRs.
Every task must end in proof (verify-hermes and/or UI evidence).
Tests alone are not enough. First PR must be the thinnest vertical slice.
```

**Done when:** checklist of PRs each with a proof step.

---

## Suggested order (this week)

1. **B** — feel the lever (`control-hermes`)  
2. **G** — restate F-01  
3. **H → I → J** — how / why / teach (same afternoon)  
4. **L** — prototype options  
5. **M → N → O** — architect → tutorial contract → plan  
6. Then a **feature** `/poteto-mode` that implements PR1 with verify-hermes  
7. **C + E** interleaved whenever the map or confidence needs sharpening  

Skip Dr Eggbot for now (Grok Bot roster tooling). Skip heavy Desktop until L picks B.

---

## Prompt cheat sheet (Lauren → Hermes)

| Lauren said | You run |
|---|---|
| `/control-app` | `verify-hermes` / `control-hermes` |
| `/poteto-mode build … use /control-app` | Lab D |
| `/swarm` + verify | Lab E |
| restate Slack thread | Lab G with `notes/hermes-frictions.md` |
| `/how` `/why` `/teach` `/recall` | Labs H–K |
| `/poteto-mode prototype …` | Lab L |
| `/architect …` | Lab M |
| `/technical-writing` tutorial first | Lab N |
| `/poteto-mode turn this design into a plan` | Lab O |
| `/maintain-verification-skill` | Lab C |

---

## Log

After each lab, append one line to `notes/hermes-frictions.md` or here:

```text
- Lab X · YYYY-MM-DD · learned: … · evidence: …
```

- Lab C · 2026-09-13 · learned: next F-01 CLI footholds are sessions list (proven), profile list + tools delegation line (TODO); live `/agents`/Desktop stay out of default CLI map · evidence: `/tmp/hermes-verify-evidence/labc-proof-20260913T012115/` (`*sessions_list*`) · map: `.cursor/skills/verify-hermes/features/list-sessions.md`
