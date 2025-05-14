

tasks = []

def display_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("Your Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def update_task():
    display_tasks()
    try:
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[num - 1] = new_task
            print("Task updated.")
        else:
            print("Invalid number.")
    except:
        print("Please enter a number.")

def remove_task():
    display_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task remove.")
        else:
            print("Invalid number.")
    except:
        print("Please enter a number.")

while True:
    print("\nTo-Do List Menu:")
    print("1. display Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. remove Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
