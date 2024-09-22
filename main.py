import json
import argparse

tasks = []

# Load tasks from JSON file
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            global tasks
            tasks = json.load(file)
    except FileNotFoundError:
        tasks.clear()

# Save tasks to JSON file
def save_tasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description):
    task_id = len(tasks) + 1
    tasks.append({
        "id": task_id,
        "description": description,
        "status": "todo"  # default status is 'todo'
    })
    save_tasks()
    print(f"Task added successfully (ID: {task_id})")

# Update a task's description
def update_task(task_id, new_description):
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks()
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Task with ID {task_id} not found.")

# Delete a task
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks()
    print(f"Task {task_id} deleted successfully.")

# Mark a task as in progress
def mark_in_progress(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            save_tasks()
            print(f"Task {task_id} marked as in-progress.")
            return
    print(f"Task with ID {task_id} not found.")

# Mark a task as done
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            save_tasks()
            print(f"Task {task_id} marked as done.")
            return
    print(f"Task with ID {task_id} not found.")

# List all tasks
def list_tasks(status=None):
    if status:
        filtered_tasks = [task for task in tasks if task["status"] == status]
    else:
        filtered_tasks = tasks

    if not filtered_tasks:
        print(f"No tasks with status '{status}' found." if status else "No tasks found.")
        return

    for task in filtered_tasks:
        print(f"{task['id']}. {task['description']} [{task['status']}]")

# Main CLI function to parse and execute commands
def main():
    load_tasks()

    parser = argparse.ArgumentParser(prog='task-cli')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', type=str, help='Description of the task')

    # Update command
    parser_update = subparsers.add_parser('update', help='Update an existing task')
    parser_update.add_argument('id', type=int, help='ID of the task to update')
    parser_update.add_argument('description', type=str, help='New description of the task')

    # Delete command
    parser_delete = subparsers.add_parser('delete', help='Delete a task')
    parser_delete.add_argument('id', type=int, help='ID of the task to delete')

    # Mark as in-progress command
    parser_mark_in_progress = subparsers.add_parser('mark-in-progress', help='Mark a task as in-progress')
    parser_mark_in_progress.add_argument('id', type=int, help='ID of the task to mark as in-progress')

    # Mark as done command
    parser_mark_done = subparsers.add_parser('mark-done', help='Mark a task as done')
    parser_mark_done.add_argument('id', type=int, help='ID of the task to mark as done')

    # List tasks command
    parser_list = subparsers.add_parser('list', help='List tasks')
    parser_list.add_argument('status', nargs='?', type=str, choices=['todo', 'in-progress', 'done'], help='Filter tasks by status')

    # Parse the arguments
    args = parser.parse_args()

    # Execute based on command
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'mark-in-progress':
        mark_in_progress(args.id)
    elif args.command == 'mark-done':
        mark_done(args.id)
    elif args.command == 'list':
        list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
