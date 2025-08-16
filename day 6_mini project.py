tasks = []  # List to store tasks

# Function to add a task
def add_task(task_name):
    task = {"task": task_name, "status": "pending"}
    tasks.append(task)
    print("Task added:", task_name)

# Function to complete a task
def complete_task(task_name):
    def mark_done(task):  # Nested function
        if task["task"] == task_name:
            task["status"] = "done"
            return True
        return False

    for t in tasks:
        if mark_done(t):
            print("Task completed:", task_name)
            return
    print("Task not found:", task_name)

# Function to show all tasks
def show_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour Tasks:")
    for t in tasks:
        print("-", t["task"], ":", t["status"])

# Main interactive menu
def menu():
    while True:
        print("\n----- TO-DO LIST MENU -----")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Show Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == "2":
            task_name = input("Enter task name to complete: ")
            complete_task(task_name)
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            print("Exiting To-Do List. Bye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

# Start the program
menu()
