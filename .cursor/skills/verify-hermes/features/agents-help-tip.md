# Agents help tip

Agents help tip is a CLI discovery pointer for F-01: `hermes agents` / `hermes agents --help` tell a human where live agent visibility lives today (TUI `/agents`, Desktop `/agents`), without claiming the CLI has a live roster.

## Sub-features

- `agents-run` executes `hermes agents` successfully and prints the visibility tip.
- `agents-help` runs `hermes agents --help` and includes the same tip in the help epilog.
- `agents-no-roster` does not invent a live agent table on the CLI.

## How to get to it (user POV)

- Run `hermes agents` or `hermes agents --help` in a terminal.
- From top-level `hermes --help`, pick the `agents` subcommand.

## Driving it with control-hermes

Preconditions:

- Launch + doctor-ok for `$RUN_ID`.
- Do not require model API keys, gateway, or Desktop.

- **Run agents tip.** Run `control-hermes run --run-id "$RUN_ID" -- agents`. Exit code `0`. Transcript contains `Live agent visibility today` and both `TUI /agents` and `Desktop /agents`.
- **Help epilog.** Run `control-hermes run --run-id "$RUN_ID" -- agents --help`. Exit code `0`. Same tip strings appear.
- **Proof.** Keep the `*agents*` transcripts under `/tmp/hermes-verify-evidence/$RUN_ID/`.

## Gotchas

- This command is a signpost, not a live feed. Do not expect parent→child task rows here.
- Live trees stay in TUI `/agents` (alias `/tasks`) and the Desktop `/agents` panel — still out of default control-hermes drive scope.
- Do not confuse with slash `/agents` inside an interactive chat session; this recipe is the top-level CLI subcommand only.
