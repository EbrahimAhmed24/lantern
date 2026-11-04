import argparse

from storage import load

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="command")

add_parser = sub.add_parser("add")
add_parser.add_argument("title")

list_parser = sub.add_parser("list")
list_parser.add_argument("--sort", action="store_true", help="sort tasks by title")

args = parser.parse_args()

if args.command == "add":
    print("Adding task:", args.title)
elif args.command == "list":
    tasks = load()
    if args.sort:
        tasks = sorted(tasks, key=lambda task: task["title"])
    for task in tasks:
        print(task["title"])