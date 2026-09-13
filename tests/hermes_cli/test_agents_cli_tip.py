"""Unit coverage for the F-01 ``hermes agents`` discovery tip."""

from __future__ import annotations

import argparse

from hermes_cli.subcommands.agents import (
    AGENTS_VISIBILITY_TIP,
    build_agents_parser,
    cmd_agents,
)


def test_agents_visibility_tip_names_tui_and_desktop():
    assert "TUI /agents" in AGENTS_VISIBILITY_TIP
    assert "Desktop /agents" in AGENTS_VISIBILITY_TIP
    assert "Live agent visibility today" in AGENTS_VISIBILITY_TIP


def test_agents_help_epilog_includes_tip():
    parser = argparse.ArgumentParser(prog="hermes")
    sub = parser.add_subparsers(dest="command")
    build_agents_parser(sub)
    help_text = sub.choices["agents"].format_help()
    assert AGENTS_VISIBILITY_TIP in help_text


def test_cmd_agents_prints_tip(capsys):
    cmd_agents(argparse.Namespace())
    out = capsys.readouterr().out
    assert AGENTS_VISIBILITY_TIP in out
