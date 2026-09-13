"""``hermes agents`` — F-01 discovery tip for live agent visibility.

There is no live agents roster on the CLI today. This command exists so
``hermes agents --help`` (and a bare ``hermes agents``) point humans to
where that visibility already lives: TUI ``/agents`` and Desktop ``/agents``.
"""

from __future__ import annotations

from typing import Callable

# Stable string for verify-hermes / control-hermes proofs. Keep wording tight.
AGENTS_VISIBILITY_TIP = (
    "Live agent visibility today: TUI /agents (alias /tasks); "
    "Desktop /agents panel. CLI has no live roster yet."
)


def cmd_agents(_args) -> None:
    """Print the discovery tip and exit successfully."""
    print(AGENTS_VISIBILITY_TIP)


def build_agents_parser(subparsers, *, cmd_agents: Callable = cmd_agents) -> None:
    """Attach the ``agents`` subcommand to ``subparsers``."""
    agents_parser = subparsers.add_parser(
        "agents",
        help="Where to watch live agents (TUI / Desktop pointer)",
        description=(
            "Point to where live agent / subagent visibility lives today. "
            "This CLI command does not list running agents."
        ),
        epilog=AGENTS_VISIBILITY_TIP,
        formatter_class=__import__("argparse").RawDescriptionHelpFormatter,
    )
    agents_parser.set_defaults(func=cmd_agents)
