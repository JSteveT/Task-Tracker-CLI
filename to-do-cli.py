import json
import argparse

tasks = []


# Load tasks from json file
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            global tasks
            tasks = json.load(file)
    except FileNotFoundError:
        tasks.clear()


# Save tasks to json file
def save_tasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


# Add tasks
def add_task(description):
    task_id = len(tasks) + 1
    tasks.append(
        {
            "id": task_id,
            "description": description,
            "status": "default",
        }
    )
    save_tasks()
    print(f"Task added successfully (ID: {task_id})")


# Update tasks
def update_task(task_id, task_description):
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = task_description
            save_tasks()
            print(f"Task has been updated successfully")
            return
    print(f"Task id not found within database")

# Delete tasks

# Mark task as in progress

# Mark task as done

# List all tasks


# Main
def main():
    load_tasks()

    parser = argparse.ArgumentParser(prog="task-cli")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Description of the task")

    # Update command
    parser_update = subparsers.add_parser("update", help="Update a task")
    parser_update.add_argument("id", type=int, help="Which task id")
    parser_update.add_argument("description", type=str, help="Description of the task")

    # Delete command

    # List command

    # Parse the arguments
    args = parser.parse_args()

    # Execute on users input
    if args.command == "add":
        add_task(args.description)
    if args.command == "update":
        update_task(args.id, args.description)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
