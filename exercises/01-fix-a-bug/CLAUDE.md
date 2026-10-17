# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Exercise 1 of the Claude Code Bootcamp (repo root is `../..`; sibling exercise: `../02-build-a-feature`). It's a teaching project: `textstats.py` has two small text helpers (`word_count`, `longest_word`) with a deliberate bug in `word_count`, which splits on `" "` instead of whitespace, so `""`, repeated spaces and newlines give wrong counts. The exercise flow is in `README.md`.

## Commands

Requires Python 3.10+ and `pip install pytest`. Standard library only otherwise.

- Run all tests: `python -m pytest`
- Run one test: `python -m pytest test_textstats.py::<test_name>`

## Rules

- Write a failing test before the code. Confirm it fails (red) before fixing.
- The exercise expects new `word_count` edge-case tests (empty string, extra spaces, newlines) to be added and shown failing before the fix is made. Don't fix the bug in the same step as adding tests unless asked.
- Keep changes small; no new dependencies.
- Public functions get a docstring.
- Run `/code-review` on the diff before saying "done".
