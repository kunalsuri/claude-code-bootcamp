# Claude Code Cheatsheet

| Command | Use it to |
|---|---|
| `/init` | Create `CLAUDE.md`, the rules Claude reads every session |
| `/code-review` | Find bugs in your diff before you push |
| `/simplify` | Clean up reuse and efficiency issues |
| `/security-review` | Check for injection, leaked secrets, unsafe input |
| `/run` | Launch the real app and see the change working |
| `/plugin` | Browse and install plugins |
| `/clear` | Start a fresh conversation (do this between tasks) |
| `/help` | List every command |

**Plan mode:** press Shift+Tab to cycle modes. Claude proposes a plan; you approve before it edits.

## The loop

1. Plan  2. Failing test  3. Make it pass  4. `/simplify`  5. `/run`  6. `/code-review`  7. Push

## Good prompts

- Say what "done" looks like: "the new test passes and the old ones still do".
- Point at files: "see `todo.py`".
- One task per conversation. `/clear` when you switch.
