# Hermes frictions (learning backlog)

Curriculum for poteto-mode labs. One friction → one lab → evidence.

## F-01 — Bot Mode: see other bots messaging (Grokbot-like)

**Status:** exploring  
**Surface:** Hermes “bots” experience vs Grokbot multi-bot visibility  
**Pain:** In Grokbot I talk to one bot and, in other windows, I can see which bots are messaging whom — that visibility is progress. In Hermes I don’t get that same experience.  
**Desired:** Explore whether Hermes can grow a feature close to that: primary chat + panes/windows showing inter-bot traffic / progress.  
**Success (verifiable):** A written feasibility note with (1) what Hermes has today, (2) whether any Grokbot repo/docs exist to compare, (3) closest Hermes surfaces to extend, (4) a smallest shippable slice.

### Findings (living)

#### Hermes today (repo map)

- **“Bot Mode” in Hermes ≠ Grokbot.** It mostly means WhatsApp deployment mode (`WHATSAPP_MODE=bot` vs `self-chat`).
- Closest multi-agent visibility is **`/agents` + `delegate_task`**: parent→child tree, TUI overlay, Desktop Agents panel + spectator windows — **not** peer bot↔bot chat panes.
- Real bot↔bot can happen on **Slack/Feishu** (`allow_bots`) but only in the external channel — Hermes UI does not mirror “who → whom.”
- **Kanban/Swarm** = async board/blackboard, not live messaging panes.
- Gap vs target: primary chat is strong; **peer multi-bot conversational visibility panes are missing** (net-new product surface). Best extension points: Desktop panes + `/agents` event plumbing.

#### Grokbot comparison

- **Official Grok Bot is closed.** No `xai-org/grok-bot` (or Cursor) open monorepo. Learn from [docs](https://docs.x.ai/grok-bot/chat-and-collaboration) + [design essay](https://x.ai/news/designing-grok-bot), not a fork.
- **UX model (public):** messaging app of persistent bots — sidebar roster, one open primary chat, group chats where handoffs are visible in-transcript, bot↔bot DMs async, avatar/attention states for progress. Explicitly rejects assignment-board dashboards.
- **Not multi-window “who’s DMing whom” as the core metaphor** — progress = roster attention + shared group transcript + optional computer side preview.
- **OSS clones (shape, not forks):** OpenMausBot (roster messaging UX), Rakazo (peer delegation + computers), GawkBot; plus RE of Electron 0.18 (research only).
- **Open multi-agent UIs closest to the desire:** AutoGen Studio Observe/message graph, CopilotKit supervisor + live `delegations[]` log, Magentic-UI orchestrator + specialist steps, dewitt/swarm multi-pane Observe.

#### Feasibility for Hermes

| Have | Gap |
|---|---|
| Primary chat (CLI/TUI/Desktop) | Peer bot↔bot as first-class Hermes UI events |
| `/agents` parent→child tree + spectator | Roster of named bots with attention states |
| Platform `allow_bots` (Slack/Feishu) | In-app mirror of who→whom |
| Kanban/Swarm async | Live group-transcript handoffs |

**Smallest shippable slice (candidate lab):**  
Desktop/TUI **activity feed pane** fed by existing `subagent.*` / delegation events (and later platform bot traffic): while you stay in one primary session, a side pane shows `from → to · status · summary` — CopilotKit-style delegation log, not a Grok clone.

### Next lab

`/poteto-mode` spike: **inter-agent activity feed** on top of current `/agents` events. Verify with `verify-hermes` where CLI-visible; Desktop pane is a follow-up if the event shape is right.
