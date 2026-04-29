# file: todo_cli.py
from todo_backend import *

def show_tasks():
    tasks = get_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for i, t in enumerate(tasks):
        print(f"{i}. {t['task']} [{t['status']}]")

def main():
    while True:
        print("\n--- TO-DO LIST CLI ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Complete")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            show_tasks()
            idx = int(input("Enter index to update: "))
            new_task = input("Enter new task: ")
            update_task(idx, new_task)

        elif choice == "4":
            show_tasks()
            idx = int(input("Enter index to delete: "))
            delete_task(idx)

        elif choice == "5":
            show_tasks()
            idx = int(input("Enter index to mark complete: "))
            mark_complete(idx)

        elif choice == "6":
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
