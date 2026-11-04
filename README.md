# lantern

A simple python command-line task tracker

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/EbrahimAhmed24/lantern.git
   ```

2. Navigate to the project directory:

   ```bash
   cd lantern
   ```

3. Make sure Python 3 is installed.

## Usage

Run the application using:

```bash
python lantern.py <command>
```

Available commands:

* `python lantern.py add "Task title"`: Add a new task.
* `python lantern.py list`: Display all tasks.
* `python lantern.py list --done`: Display completed tasks only.
* `python lantern.py list --sort`: Display tasks sorted alphabetically by title.
* `python lantern.py export --csv`: Export tasks as CSV.

Tasks are stored locally in `tasks.json`.

For more details, see the [Usage Guide](docs/usage.md).

## Team

| Name | GitHub Username |
|---|---|
| Ashraqat Mohamed | ashraqt-1026 |
| Ebrahim Ahmed | EbrahimAhmed24 |

[Contributing Guidelines](CONTRIBUTING.md)
