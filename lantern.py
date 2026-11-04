import argparse
import storage
from export import export_tasks_csv

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="command")

add_parser = sub.add_parser("add")
add_parser.add_argument("title")

list_parser = sub.add_parser("list")
list_parser.add_argument("--sort", action="store_true", help="sort tasks by title")
list_parser.add_argument("--done", action="store_true")

export_parser = sub.add_parser("export")
export_parser.add_argument("--csv", action="store_true")

args = parser.parse_args()

if args.command == "add":
    print("Adding task:", args.title)

elif args.command == "list":
    tasks = storage.load()

    if args.done:
        tasks = [task for task in tasks if task.get("done")]

    if args.sort:
        tasks = sorted(tasks, key=lambda task: task["title"].casefold())

    if not tasks:
        print("No tasks yet. Add one with: lantern add <title>")
    else:
        for task in tasks:
            print(task["title"])

elif args.command == "export":
    if args.csv:
        tasks = storage.load()
        export_tasks_csv(tasks)