---
name: verify-hermes
description: "Drive Hermes Agent's real CLI the way a user does — isolated HERMES_HOME, doctor checks, command transcripts as proof. Use when proving CLI/config/status behavior in this repo; not for unit tests or mocked argparse."
---

# verify-hermes

Hermes Agent is primarily a **CLI** (`hermes`) with secondary surfaces (interactive chat/TUI, messaging gateway, dashboard, desktop). This skill verifies the **CLI surface** — the path every install touches first. Chat, gateway, and desktop need credentials or long-lived processes; they are noted below but not the default drive target.

Agents read this cold mid-task. Follow Launch → Doctor → Drive → Evidence → Cleanup in order.

## Launch

Hermes CLI is not a long-lived server for these checks. "Launch" means: disposable home + working `uv run hermes` from the repo root.

```bash
RUN_ID="verify-$(date -u +%Y%m%dT%H%M%S)"
export PATH="$HOME/.local/bin:$PATH"
cd /workspace   # repo root
.cursor/skills/verify-hermes/scripts/control-hermes launch --run-id "$RUN_ID"
```

Ready when the helper prints `ready: isolated HERMES_HOME at /tmp/hermes-verify-$RUN_ID` and `hermes config path` resolves under that directory.

Always set `HERMES_HOME=/tmp/hermes-verify-$RUN_ID` (the helper does this for `run`/`doctor`). Never drive the developer's real `~/.hermes`.

Teardown of the home dir is Cleanup. Keep evidence.

**Secondary surfaces (out of default scope):**

| Surface | Start hint | Why not default |
|---|---|---|
| Chat / TUI | `hermes chat` / `hermes --tui` | Needs model API keys; interactive PTY |
| Gateway | `hermes gateway` | Needs platform tokens; systemd user service |
| Dashboard | `hermes dashboard` / `hermes serve` | SPA + API; heavier deps |
| Desktop | `apps/desktop` | Electron; separate package |

## Doctor

Read-only. Run before any drive when state looks wrong, and once after Launch.

```bash
.cursor/skills/verify-hermes/scripts/control-hermes doctor --run-id "$RUN_ID"
```

Pass criteria:

- Exit 0 from the helper (`doctor-ok: instance at … worth driving`)
- `hermes version` succeeds
- `hermes config path` is under `/tmp/hermes-verify-$RUN_ID/`
- Artifacts written under `/tmp/hermes-verify-evidence/$RUN_ID/` (`doctor-version.txt`, `doctor.txt`, `doctor-config-path.txt`)

`hermes doctor` itself may list missing API keys or optional tools — that is expected on a fresh home. Do **not** treat missing OpenRouter/Telegram tokens as a failed doctor for CLI verification. Fail only when version/config isolation breaks or the helper exits non-zero on those checks.

## Drive

Use the helper so every command is isolated and transcripted:

```bash
.cursor/skills/verify-hermes/scripts/control-hermes run --run-id "$RUN_ID" -- version
.cursor/skills/verify-hermes/scripts/control-hermes run --run-id "$RUN_ID" -- doctor
.cursor/skills/verify-hermes/scripts/control-hermes run --run-id "$RUN_ID" -- status
.cursor/skills/verify-hermes/scripts/control-hermes run --run-id "$RUN_ID" -- config get display.skin
.cursor/skills/verify-hermes/scripts/control-hermes run --run-id "$RUN_ID" -- config set display.skin default
```

Prefer exact subcommands from the feature map over inventing flags. Read `features/README.md`, then the feature file for the behavior under test. Drive the **user** path (`hermes …`), not Python imports of `hermes_cli.*`.

Do not run two drives that share one `HERMES_HOME`. Parallel runs need distinct `--run-id` values (separate homes). Two agents must not share `/tmp/hermes-verify-$RUN_ID`.

## Evidence

Proof lives in `/tmp/hermes-verify-evidence/$RUN_ID/` (print with `control-hermes evidence-dir --run-id "$RUN_ID"`).

Standards:

- Capture the **command + stdout/stderr + exit code** (the helper writes this into each `*.txt`).
- Exercise the real user path (`uv run hermes …` via the helper), not internal setters or pytest fixtures.
- For mutations (`config set`), prove with a second read (`config get` / `config show`) showing the stored value.
- Record which feature file and entry point you drove.
- Screenshots are N/A for default CLI proofs. Terminal transcripts are the proof.
- Do not treat unit-test green as CLI proof.

## Cleanup

```bash
.cursor/skills/verify-hermes/scripts/control-hermes cleanup --run-id "$RUN_ID"
```

Removes only `/tmp/hermes-verify-$RUN_ID`. **Never** deletes `/tmp/hermes-verify-evidence/$RUN_ID/`. Never `pkill hermes` by name — these CLI checks should not leave daemons; if you started gateway/dashboard outside this skill, stop that PID explicitly and leave it out of default recipes.

## Helpers

| Helper | Role |
|---|---|
| `.cursor/skills/verify-hermes/scripts/control-hermes` | launch / doctor / run / cleanup / evidence-dir |

```bash
chmod +x .cursor/skills/verify-hermes/scripts/control-hermes
.cursor/skills/verify-hermes/scripts/control-hermes --help
```

Requires: `uv` on `PATH`, repo checkout at `/workspace` (or run from repo root — helper resolves root relative to the script).

## Feature map

Maintained recipes: [`features/README.md`](features/README.md). A proof that drives one convenient entry point is incomplete when the map lists others for that feature.
