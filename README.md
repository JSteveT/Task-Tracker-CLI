# Task Tracker CLI Project

## Overview

**Task Tracker** is a command-line interface (CLI) tool that helps you manage and track tasks effectively. With this project, you can add, update, delete tasks, and track their progress using simple command-line commands. All tasks are stored in a JSON file, allowing easy management without the need for a database or external tools.

This project is designed to improve your skills in handling user inputs, working with the file system, and building practical CLI applications.

https://roadmap.sh/projects/task-tracker

## Features

- **Add a Task**: Create a new task with a description.
- **Update a Task**: Modify the description of an existing task.
- **Delete a Task**: Remove a task by its unique ID.
- **Mark Task as In Progress**: Update the status of a task to 'in-progress'.
- **Mark Task as Done**: Update the status of a task to 'done'.
- **List All Tasks**: Show all tasks with their current statuses.
- **Filter Tasks**: List tasks by their status, whether they are 'done', 'in-progress', or 'to-do'.

## Task Properties

Each task contains the following attributes:

- **id**: A unique identifier for each task.
- **description**: A short description of the task.
- **status**: The current status of the task (`todo`, `in-progress`, `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

## Example Commands

Here are some example commands and their expected outputs:

### Adding a new task
```bash
/bin/python3 to-do-cli.py add "Buy groceries"
```

### Updating a task
```bash
/bin/python3 to-do-cli.py update 1 "Buy groceries"
```

### Deleting a task
```bash
/bin/python3 to-do-cli.py delete 1
```

### Mark task as in progress
```bash
/bin/python3 to-do-cli.py mark-in-progress 1
```

### Mark task as done
```bash
/bin/python3 to-do-cli.py mark-done 1
```

### List all tasks
```bash
/bin/python3 to-do-cli.py list all
```

### Filter tasks todo, inprogress, and done
```bash
/bin/python3 to-do-cli.py list todo
/bin/python3 to-do-cli.py list in-progress
/bin/python3 to-do-cli.py list done
```
