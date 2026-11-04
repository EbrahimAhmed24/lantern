import csv
import sys


def export_tasks_csv(tasks):
    writer = csv.DictWriter(
        sys.stdout,
        fieldnames=["title", "done"]
    )

    writer.writeheader()
    writer.writerows(tasks)
