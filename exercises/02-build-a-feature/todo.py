"""A tiny command-line to-do list. Tasks are stored in todo.json."""

import argparse
import json
import os

DATA_FILE = os.environ.get("TODO_FILE", "todo.json")


def load_tasks():
    """Return the list of tasks from disk (empty list if no file yet)."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def save_tasks(tasks):
    """Write the list of tasks to disk."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(title):
    """Add a new task and return it."""
    tasks = load_tasks()
    task = {"title": title, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    return task


def format_tasks(tasks):
    """Return the tasks as numbered lines, one per task."""
    return "\n".join(
        f"{i}. [{'x' if t['done'] else ' '}] {t['title']}"
        for i, t in enumerate(tasks, start=1)
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description="Tiny to-do list")
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add", help="add a task")
    add.add_argument("title")
    sub.add_parser("list", help="show all tasks")
    args = parser.parse_args(argv)

    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        print(format_tasks(load_tasks()))


if __name__ == "__main__":
    main()
