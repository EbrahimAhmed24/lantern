import argparse

from storage import load

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="command")

add_parser = sub.add_parser("add")
add_parser.add_argument("title")

list_parser = sub.add_parser("list")

args = parser.parse_args()

if args.command == "add":
    print("Adding task:", args.title)
elif args.command == "list":
    tasks = load()
    if not tasks:
        print("No tasks yet. Add one with: lantern add <title>")
    else:
        print("Listing tasks")