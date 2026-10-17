# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A teaching repo for Claude Code beginners: a workflow (plan, test first, implement, review, ship), a one-page `cheatsheet.md`, a reusable `template/CLAUDE.md`, and two self-contained Python exercises. `docs/` holds a static `index.html`; `scripts/` and `utils/` are empty.

## Layout

- `exercises/01-fix-a-bug/`: `textstats.py` (`word_count`, `longest_word`) and its tests. Has its own `CLAUDE.md`.
- `exercises/02-build-a-feature/`: `todo.py`, an argparse to-do CLI storing tasks in `todo.json` (path overridable with the `TODO_FILE` env var), and `test_todo.py`.
- Each exercise is independent and has a `README.md` with the student steps. Don't share code between them.

## Commands

Python 3.10+, standard library plus `pytest` (`pip install pytest`). There is no repo-wide build, lint, or config.

- Run an exercise's tests from inside its folder: `python -m pytest`
- Run one test: `python -m pytest test_textstats.py::<test_name>`
- Try the CLI: `python todo.py add "buy milk"` then `python todo.py list`

Tests import modules by bare name (`from textstats import ...`), so run pytest from the exercise folder, not the repo root.

## Rules

- Write a failing test before the code, and confirm it fails before fixing.
- Exercises are written for beginners: keep code and tests plain and short, and don't refactor an exercise past what its README asks for.
- The exercise READMEs describe a step-by-step flow; keep README steps and the code in sync when changing either.
- Keep `README.md` short and non-verbose.
- No new dependencies without asking.
