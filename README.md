# Claude Code Bootcamp

A repeatable workflow for coding with Claude Code: plan, test first, implement, review, ship.
For students who have never used it. Practice beats reading, so most of this repo is exercises.

## 5-minute quickstart

1. **Fork** this repo, then clone your fork.
2. Install Claude Code and open a terminal in the repo folder.
3. Run `claude`, then type `/init`.

That's it. Next, open [exercises/01-fix-a-bug](exercises/01-fix-a-bug/README.md).

You'll need Python 3.10+ and `pip install pytest`.

## What's in here

| Path | What it is |
|---|---|
| [cheatsheet.md](cheatsheet.md) | One page of slash commands. Print or pin it. |
| [template/CLAUDE.md](template/CLAUDE.md) | Copy into any project and edit. |
| [exercises/01-fix-a-bug](exercises/01-fix-a-bug/README.md) | Fix a bug test-first. |
| [exercises/02-build-a-feature](exercises/02-build-a-feature/README.md) | Plan, build and review a small feature. |

## The workflow

1. **Setup (once per repo):** `/init`, then put your hard rules in `CLAUDE.md`.
2. **Design:** use plan mode (Shift+Tab) before changing anything non-trivial.
3. **Test first:** write a failing test before the code.
4. **Implement:** make the test pass.
5. **Something breaks:** reproduce, isolate, fix (`engineering:debug`).
6. **Polish:** `/simplify`.
7. **Verify:** `/run`, then `/code-review` and `/security-review`.
8. **Ship:** push, read CI.

If you only do three things: run `/init`, write a failing test before the code, run `/code-review` before every push.

## Optional plugins

Run `/plugin` to browse. Useful for coding: `engineering` (testing-strategy, debug, architecture, documentation, deploy-checklist), `claude-code-setup` (claude-automation-recommender), `skill-doctor`. Skip the sales, finance and productivity plugins.

## License

Apache 2.0, see [LICENSE](LICENSE).
