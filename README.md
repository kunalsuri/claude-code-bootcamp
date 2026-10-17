<div align="center">

# 🚀 Claude Code Bootcamp

**Plan → Test → Build → Review → Ship**

A hands-on workflow for coding with Claude Code. Built for first-timers.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC?logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/license-Apache%202.0-green)

</div>

## ⚡ Quickstart

1. 🍴 **Fork** this repo and clone it.
2. 📦 Install [Claude Code](https://claude.com/claude-code), then `pip install pytest`.
3. 🧠 Run `claude`, then type `/init`.
4. 🐛 Open [exercise 01](exercises/01-fix-a-bug/README.md).

## 🗂️ What's inside

| | Path | What it is |
|---|---|---|
| 📄 | [cheatsheet.md](cheatsheet.md) | One page of slash commands |
| 🧩 | [template/CLAUDE.md](template/CLAUDE.md) | Copy into any project |
| 🎮 | [docs/index.html](docs/index.html) | Interactive demo of both exercises |
| 🐛 | [exercises/01-fix-a-bug](exercises/01-fix-a-bug/README.md) | Fix a bug, test first |
| ✨ | [exercises/02-build-a-feature](exercises/02-build-a-feature/README.md) | Plan, build and review a feature |

## 🔁 The workflow

| Step | | Do this |
|---|---|---|
| 1 | 🛠️ **Setup** | `/init`, add your hard rules to `CLAUDE.md` |
| 2 | 🗺️ **Design** | Plan mode (`Shift+Tab`) before non-trivial changes |
| 3 | 🔴 **Test first** | Write a failing test |
| 4 | 🟢 **Implement** | Make it pass |
| 5 | 🔍 **Debug** | Reproduce, isolate, fix (`engineering:debug`) |
| 6 | ✂️ **Polish** | `/simplify` |
| 7 | ✅ **Verify** | `/run`, `/code-review`, `/security-review` |
| 8 | 📦 **Ship** | Push, read CI |

> 💡 **Short on time?** Run `/init`, test before code, `/code-review` before every push.

## 🔌 Optional plugins

Run `/plugin` to browse. Handy for coding: `engineering`, `claude-code-setup`, `skill-doctor`.

## 📜 License

Apache 2.0. See [LICENSE](LICENSE).
