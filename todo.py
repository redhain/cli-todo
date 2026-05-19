import json
import sys
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os .path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_tasks(title):
    tasks = load_tasks()

    tasks.append({
        "title": title,
        "done": False
    })

    save_tasks(tasks)

    print(f'Task added: "{title}"')

def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f"{index}. [{status}] {task['title']}")


def mark_done(index):
    tasks = load_tasks()

    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print("Task completed.")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()

    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f'Deleted: "{removed["title"]}"')
    else:
        print("Invalid task number.")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("   python todo.py add tasks")
        print("   python todo.py list")
        print("   python todo.py done <number>")
        print("   python todo.py delete <number>")
        return

    command = sys.argv[1]

    if command == "add":
        title = " ".join(sys.argv[2:])
        add_tasks(title)

    elif command == "list":
        list_tasks()

    elif command == "done":
        mark_done(int(sys.argv[2]))

    elif command == "delete":
        delete_task(int(sys.argv[2]))

    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()



