# Get and set config

Get and set config lets a user read and write configuration values under their Hermes home so settings persist in `config.yaml` without hand-editing YAML.

## Sub-features

- `config-path` prints the active config file path.
- `config-set` writes a value and confirms with a success line.
- `config-get` prints the resolved value for a key.
- `config-show` renders a human configuration summary that reflects the change.

## How to get to it (user POV)

- Run `hermes config path` to see which file is active.
- Run `hermes config set <key> <value>` then `hermes config get <key>`.
- Run `hermes config show` to review a summary.

## Driving it with control-hermes

Preconditions:

- Launch + doctor-ok for `$RUN_ID`.
- Use only the isolated home. Key under test: `display.skin`.

- **Show path.** Run `control-hermes run --run-id "$RUN_ID" -- config path`. Exit code `0`. Stdout is `/tmp/hermes-verify-$RUN_ID/config.yaml`.
- **Set value.** Run `control-hermes run --run-id "$RUN_ID" -- config set display.skin default`. Exit code `0`. Stdout contains `✓ Set display.skin = default` (or equivalent success) and the isolated config path.
- **Get value.** Run `control-hermes run --run-id "$RUN_ID" -- config get display.skin`. Exit code `0`. Stdout is `default`.
- **Show summary.** Run `control-hermes run --run-id "$RUN_ID" -- config show`. Exit code `0`. Paths section lists the isolated config file.
- **Proof.** Keep the `config_set`, `config_get`, and `config_path` transcripts. Mutation is proven only when `get` matches what `set` wrote.

## Gotchas

- Without `HERMES_HOME` isolation you will mutate the developer's real config — always go through `control-hermes`.
- `config edit` opens an editor; do not use it in unattended verification.
- Some keys may coerce or validate values. Assert the `get` output, not only the `set` success line.
- Cleanup may delete the whole verify home instead of unsetting the key; either is fine. Evidence must remain.
