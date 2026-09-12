# Show status

Show status prints a snapshot of Hermes components (providers, terminal backend, messaging platforms, gateway, jobs, sessions) without starting the messaging gateway.

## Sub-features

- `status-run` executes `hermes status` successfully.
- `status-sections` shows labeled sections a user can scan (providers, platforms, gateway, sessions).
- `status-gateway-stopped` on a fresh verify home reports gateway not running.

## How to get to it (user POV)

- Run `hermes status` in a terminal.
- Follow doctor output tips that suggest `Run 'hermes doctor' for detailed diagnostics` / setup — status is the lighter companion overview.

## Driving it with control-hermes

Preconditions:

- Launch + doctor-ok for `$RUN_ID`.
- Do not start `hermes gateway` for this recipe.

- **Run status.** Run `control-hermes run --run-id "$RUN_ID" -- status`. Exit code `0`.
- **Scan sections.** Transcript includes messaging platform lines and a gateway status. On a fresh home expect gateway `stopped` / not configured platforms marked unset.
- **Proof.** Keep the `*status*` transcript under `/tmp/hermes-verify-evidence/$RUN_ID/`.

## Gotchas

- Status is observational. It must not start the gateway as a side effect.
- "Not configured" for Telegram/Discord/etc. is the expected fresh-home state, not a failed proof.
- Do not confuse `hermes status` with `hermes gateway status` (gateway subcommand); this feature is the top-level `status` command.
