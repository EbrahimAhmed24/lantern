import argparse
import storage

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="command")

add_parser = sub.add_parser("add")
add_parser.add_argument("title")

list_parser = sub.add_parser("list")
list_parser.add_argument("--done", action="store_true")

args = parser.parse_args()

if args.command == "add":
    print("Adding task:", args.title)

elif args.command == "list":
    tasks = storage.load()

    if args.done:
        tasks = [task for task in tasks if task["done"]]

    for task in tasks:
        print(task["title"])
        