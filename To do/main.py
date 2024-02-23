tasks = []
print("Stay on track, get it done! Your ultimate to-do list guide.")


def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task {task} added to the list")


def display_task():
    if not tasks:
        print("There are no current task")
    else:
        for index, task in enumerate(tasks):
            print(f"{index}. {task}")


def delete_task():
    display_task()
    try:
        task_to_delete = int(input("No. of task to delete: "))
        if task_to_delete >= 0 and task_to_delete < len(tasks):
            tasks.pop(task_to_delete)
            print(f"Task {task_to_delete} has been removed")
        else:
            print(f"Task {task_to_delete} not found")
    except:
        print("Invalid Input")


while True:
    print("Please select one of the following option")
    print("-----------------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. Display tasks")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        delete_task()
    elif choice == 3:
        display_task()
    elif choice == 4:
        break
    else:
        print("Invalid input! Please try again")
