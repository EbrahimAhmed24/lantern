import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load():
    if not TASKS_FILE.exists():
        return []

    with TASKS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save(tasks):
    with TASKS_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, sort_keys=True)
