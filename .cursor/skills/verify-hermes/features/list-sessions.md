# List sessions

List sessions prints recent entries from the SQLite session store so a user can see which agent conversations exist under the current `HERMES_HOME` — the closest CLI stand-in today for F-01 agent-visibility discovery (TUI `/agents` and Desktop Agents panel are interactive surfaces, not this recipe).

## Sub-features

- `sessions-list-run` executes `hermes sessions list` successfully.
- `sessions-list-limit` accepts `--limit` and still exits successfully.
- `sessions-empty-home` on a fresh verify home reports `No sessions found.` (or an empty table) without failing.

## How to get to it (user POV)

- Run `hermes sessions list` in a terminal.
- Run `hermes sessions --help` and pick `list`, optionally with `--limit N` or `--source cli`.

## Driving it with control-hermes

Preconditions:

- Launch + doctor-ok for `$RUN_ID`.
- Do not require model API keys or a running gateway.

- **List sessions.** Run `control-hermes run --run-id "$RUN_ID" -- sessions list --limit 5`. Exit code `0`.
- **Fresh-home empty store.** On a newly launched verify home, transcript contains `No sessions found.` (or shows zero session rows). That empty result is a successful proof of the command path.
- **Proof.** Keep the `*sessions_list*` transcript under `/tmp/hermes-verify-evidence/$RUN_ID/`.

## Gotchas

- This is observational session history, not live subagent progress. Live parent→child visibility lives in TUI `/agents` and the Desktop Agents panel (out of default CLI map scope).
- `hermes sessions browse` is interactive — do not use it in control-hermes recipes.
- A non-empty list requires prior chat/gateway activity under this `HERMES_HOME`; do not treat an empty fresh home as a failed proof.
