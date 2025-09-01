todo_list = {}

def show_menu():
    print("\n--- TO-DO LIST APP ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_task():
    if not todo_list:
        print("Task list empty!!!")
    else:
         # i=1, (task, done) = (todo_list.items()): give first item  
         for i, (task, done) in enumerate(todo_list.items(), 1):
            # <value_if_true> if <condition> else <value_if_false>
            status = "✅" if done else "❌"
            print(f"{i}. {task} [{status}]")

def add_task():
    task = input("Enter a task: ").strip()
    if task:
       todo_list[task] = False
       print(f"Task: \"{task}\" added") 
    else:
        print("Task can't be empty.") 

def complete_task():
    task_name = input("Enter the task marked as completed: ").strip()
    if (task_name in todo_list):
        todo_list[task_name] = True
        print(f"Task: \"{task_name}\" completed")
    else:
        print("Task not found") 

def delete_task():
    remove_task = input("Enter the exact task to delete: ").strip()
    if (remove_task in todo_list):
        todo_list.pop(remove_task)
        print("Task deleted successfully")
    else:
        print("Task not found")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ").strip()

    if(choice == '1'):
        view_task()
    elif(choice == '2'):
        add_task()
    elif(choice == '3'):
        complete_task()
    elif(choice == '4'):
        delete_task()
    elif(choice == '5'):
        print("GoodBye: Have a nice day")
        break
    else:
        print("Invalid option. Please choose 1-5.")