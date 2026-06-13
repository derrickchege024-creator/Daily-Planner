import json
import os

tasks = []

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✓" if t.get("done") else " "
        print(f"{i}. [{status}] {t.get('title')}")

tasks = load_tasks()

def add_tasks(tasks):
    title = input("Enter task title: ").strip()
    if title == "":
        print("Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f'Task "{title}" added!')

def complete_task(tasks):
    show_tasks(tasks)
    if len(tasks) == 0:
        return
    choice = input("Enter task number to mark as done: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.")
        return
    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("Task number out of range.")
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f'Task "{tasks[index]["title"]}" marked as done!')

def delete_task(tasks):
    show_tasks(tasks)
    if len(tasks) == 0:
        return
    choice = input("Enter task number to delete: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.")
        return
    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("Task number out of range.")
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f'Task "{removed["title"]}" deleted.')

def main():
    global tasks
    tasks = load_tasks()
    print("Welcome to your daily planner!")

    while True:
        print("---- MENU ----")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! Stay productive.")
            break
        else:
            print("Invalid option. Please choose 1 to 5.")

if __name__ == "__main__":
    main()