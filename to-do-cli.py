import json
import argparse


tasks = []


# Load tasks from json file
def loadTasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            global tasks
            tasks = json.load(file)
    except FileNotFoundError:
        tasks.clear()


# Save tasks to json file
def saveTasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


# Add tasks
def addTask(description):
    task_id = len(tasks) + 1
    tasks.append(
        {
            "id": task_id,
            "description": description,
            "status": "todo",
        }
    )
    saveTasks()
    print(f"Task added successfully (ID: {task_id})")


# Update tasks
def updateTask(task_id, task_description):
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = task_description
            saveTasks()
            print(f"Task has been updated successfully")
            return
    print(f"Task id not found within database")


# Delete tasks
def deleteTask(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    saveTasks()
    print(f"Task {task_id} deleted successfully.")


# Mark task as in progress
def inProgressTask(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            saveTasks()
            print(f"Task status has been updated to in progress successfully")
            return
    print(f"Task id not found within database")


# Mark task as done
def doneTask(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            saveTasks()
            print(f"Task status has been updated to done successfully")
            return
    print(f"Task id not found within database")
    

# List tasks controller
def listTasks(task_status):
    
    if task_status == "all":
      listAll()
    if task_status == "todo":
      listTodo()
    if task_status == "in-progress":
      listJustInProgress()
    if task_status == "done":
      listDone()

# List all
def listAll():
    global tasks
    for task in tasks:
        print(task)

# List todo
def listTodo():
    global tasks
    for task in tasks:
        if task["status"] == "todo":
          print(task)


# List just in progress 
def listJustInProgress():
    global tasks
    for task in tasks:
        if task["status"] == "in-progress":
          print(task)

# List just done
def listDone():
    global tasks
    for task in tasks:
        if task["status"] == "done":
          print(task)


# Main
def main():
    loadTasks()

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
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="Which task id")

    # inprogress command
    parser_inprogress = subparsers.add_parser("mark-in-progress", help="Set task as in progress")
    parser_inprogress.add_argument("id", type=int, help="Id for the task to change to in progress")

    # Done command
    parser_done = subparsers.add_parser("mark-done", help="Set task as done")
    parser_done.add_argument("id", type=int, help="Id for the task to change to done")

    # List all tasks
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("status", type=str, help="Input the fitler for the list")

    # Parse the arguments
    args = parser.parse_args()

    # Execute on users input
    if args.command == "add":
        addTask(args.description)
    if args.command == "update":
        updateTask(args.id, args.description)
    if args.command == "delete":
        deleteTask(args.id)
    if args.command == "mark-in-progress":
        inProgressTask(args.id)
    if args.command == "mark-done":
        doneTask(args.id)
    if args.command == "list":
        listTasks(args.status)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
