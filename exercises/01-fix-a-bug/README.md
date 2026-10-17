# Exercise 1: Fix a bug, test first

**Project:** `textstats.py`, two small text helpers. All tests pass, but `word_count` has a bug.

**Skills practiced:** `/init`, failing test first, `/simplify`, `/code-review`.

## Steps

1. In this folder, run `pip install pytest` and `python -m pytest`. Everything passes.
2. Start `claude` and run `/init`. Read the `CLAUDE.md` it creates. Add the rule "write a failing test before the code".
3. Try `word_count("")` and `word_count("a  b")` in your head. Are the answers right?
4. Ask Claude: *"Add failing tests for word_count edge cases (empty string, extra spaces, newlines). Don't fix the code yet."*
5. Run `python -m pytest`. You should see red. That proves the tests catch the bug.
6. Ask Claude: *"Now fix word_count so the tests pass."*
7. Run `/simplify`, then `/code-review`.

## Done when

- New tests fail before the fix and pass after.
- You can explain the bug in one sentence.

## Stretch

Add `average_word_length` the same way: test first.
