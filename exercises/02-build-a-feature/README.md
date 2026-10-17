# Exercise 2: Plan, build and review a feature

**Project:** `todo.py`, a command-line to-do list with `add` and `list`.

**Skills practiced:** plan mode, test first, `/run`, `/code-review`, `/security-review`.

## Try it

```bash
python todo.py add "buy milk"
python todo.py list
```

## Your feature: `done`

Add `python todo.py done 1` to mark task 1 as done.

1. Start `claude` and press Shift+Tab to enter **plan mode**.
2. Ask: *"Plan a `done <number>` command for todo.py. Cover bad input like 0, 99 or 'abc'."* Read the plan. Edit it if you disagree, then approve.
3. Ask: *"Write failing tests for the plan first."* Run `python -m pytest` and confirm they fail.
4. Ask: *"Implement it so the tests pass."*
5. Run `/run` and try it in the terminal for real.
6. Run `/code-review` and `/security-review`. Read every finding; fix the ones that are real.

## Done when

- `done 1` shows `1. [x] buy milk` in `list`.
- Bad numbers give a clear error, not a crash with a traceback.
- Tests pass and you ran both reviews.

## Stretch

Add `delete <number>` using the same loop. Notice how much faster the second time is.
