# Run doctor

Run doctor checks configuration and dependencies and prints a human-readable report so a user can see what is healthy, missing, or optional.

## Sub-features

- `doctor-run` executes `hermes doctor` and returns to the shell.
- `doctor-report` prints sectioned diagnostics (tools, skills hub, memory, issues list).
- `doctor-fresh-home` works on a disposable `HERMES_HOME` without requiring API keys.

## How to get to it (user POV)

- Run `hermes doctor` after install or when something feels misconfigured.
- Follow README / setup tips that say `Run 'hermes doctor' for detailed diagnostics`.

## Driving it with control-hermes

Preconditions:

- Fresh launch for this `$RUN_ID`.
- Doctor helper already passed (`doctor-ok`) so isolation is confirmed.

- **Run doctor.** Run `control-hermes run --run-id "$RUN_ID" -- doctor`. Exit code `0` on a normal checkout even when optional tools/keys are missing.
- **Read the report.** Transcript includes diagnostic sections (for example tool marks `✓` / `⚠`) and may list issues such as missing `.env` or API keys.
- **Isolation check.** Transcript or companion `doctor-config-path` evidence shows config under `/tmp/hermes-verify-$RUN_ID/`, not `~/.hermes`.
- **Proof.** Keep the `*doctor*` transcript in `/tmp/hermes-verify-evidence/$RUN_ID/`. Missing OpenRouter/Telegram keys are **not** failures for this feature; a non-zero exit or crash is.

## Gotchas

- `hermes doctor --fix` mutates the environment (symlinks, repairs). Do not use `--fix` in the default proof; it is a different, destructive path.
- Optional tool warnings (`browser-cdp`, `web` missing keys) are expected on a bare verify home.
- Do not require a fully configured production `.env` to call doctor "verified".
