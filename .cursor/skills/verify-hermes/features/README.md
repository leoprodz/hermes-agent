# Hermes CLI verification map

This directory is the maintained source for verifying user-facing Hermes CLI behavior in this repo. Read the index before driving, then use the matching feature file as the recipe.

## Baseline preconditions

- Work from the repo root with `uv` available (`PATH` includes `$HOME/.local/bin` if needed).
- Launch via `.cursor/skills/verify-hermes/scripts/control-hermes launch --run-id "$RUN_ID"`.
- `HERMES_HOME` must be `/tmp/hermes-verify-$RUN_ID` (never the developer's `~/.hermes`).
- Run `control-hermes doctor --run-id "$RUN_ID"` and require `doctor-ok`.
- Never drive an instance whose home you did not create in this verification run.
- Chat, gateway, dashboard, and desktop are out of scope for these recipes unless a feature file explicitly says otherwise.

## Driving conventions

- Start every recipe from a freshly launched home unless its preconditions say otherwise.
- Run every `hermes` invocation through `control-hermes run --run-id "$RUN_ID" -- …`.
- Treat commands as literal. Keep flags and values unchanged.
- Prefer stable CLI strings (`Hermes Agent v`, config path prefix, `✓ Set`, printed `config get` values) over ANSI color codes.
- Restore mutated config keys after a mutation recipe, or discard the whole home in cleanup.
- Do not remove proof artifacts during cleanup.

## Proof and skip reporting

- Capture command, stdout/stderr, and exit code (helper transcripts under `/tmp/hermes-verify-evidence/$RUN_ID/`).
- Mutation proof includes a second read of the stored value.
- Record the feature ID and entry point with every artifact.
- Report an unreachable path with the attempted command and unmet precondition.
- Do not report a skipped entry point as verified through a different path.

## Feature entry contract

Each feature file starts with an H1 title and one paragraph describing the user-visible behavior. It then uses exactly four H2 sections in this order:

1. `Sub-features`
2. `How to get to it (user POV)`
3. `Driving it with control-hermes`
4. `Gotchas`

## Features

- [Show version](./show-version.md) — install identity and version string from the CLI.
- [Run doctor](./run-doctor.md) — configuration/dependency diagnostics users run when setup looks wrong.
- [Show status](./show-status.md) — component status overview without starting the gateway.
- [Get and set config](./get-set-config.md) — read and write a config value under an isolated home.
- [List sessions](./list-sessions.md) — session-store listing under an isolated home (F-01 CLI foothold).

## TODO — deferred F-01 surfaces (next map candidates)

Proposed after walking `hermes --help` for agents / delegation / desktop visibility. Do **not** treat these as verified until each has its own feature file + control-hermes transcript.

1. **List profiles** (`hermes profile list`) — multi-instance roster; shows `◆default` / gateway column on a fresh home.
2. **Show delegation toolset** (`hermes tools list --platform cli`) — prove the `delegation` toolset line is present/enabled for CLI (config knobs via `hermes config get delegation.*` as a sibling entry if needed).
3. **Out of CLI default scope (document only):** TUI `/agents` overlay and Desktop Agents panel — live subagent trees need interactive/PTY or Electron; not driveable by the default control-hermes recipes until a dedicated harness exists.
