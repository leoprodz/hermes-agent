# Show version

Show version prints the installed Hermes Agent version, install method, and related runtime identity so a user can confirm which build they are running.

## Sub-features

- `version-command` runs `hermes version` and exits successfully.
- `version-banner` includes the `Hermes Agent v` identity string.
- `version-install` reports install directory / method for this checkout.

## How to get to it (user POV)

- Run `hermes version` in a terminal from an installed Hermes environment.
- Run `hermes --help` and note the top-level `version` subcommand, then invoke it.

## Driving it with control-hermes

Preconditions:

- `control-hermes launch --run-id "$RUN_ID"` completed with `ready:`.
- `control-hermes doctor --run-id "$RUN_ID"` printed `doctor-ok`.

- **Run version.** Ask Hermes for its version. Run `control-hermes run --run-id "$RUN_ID" -- version`. Exit code `0`. Transcript contains `Hermes Agent v` and a version like `0.19.0`.
- **Confirm checkout install.** In the same transcript, expect install identity for this environment (for example `Install method: git` and `Install directory: /workspace` when driving via `uv run` from this checkout).
- **Proof.** Keep the helper transcript under `/tmp/hermes-verify-evidence/$RUN_ID/` whose filename contains `version`. That file is the proof artifact.

## Gotchas

- `hermes --version` may exist as a top-level flag; this map's primary entry is the `version` subcommand.
- Do not scrape GitHub for version. The proof is the local CLI output.
- A green unit test that imports `__version__` is not this feature.
