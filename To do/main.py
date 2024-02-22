tasks = []
print("Stay on track, get it done! Your ultimate to-do list guide.")


def addtask(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task {task} added to the list")

def deletetask(task):
     #displaytask()
    try:
        task_to_delete = int(input("No. of task to delete: "))
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
        addtask(tasks)
    elif choice == 2:
        #deletetask()
    elif choice == 3:
        #displaytask()
    elif choice == 4:
        break
    else:
        print("Invalid input! Please try again")