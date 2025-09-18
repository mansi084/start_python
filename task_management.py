def add_task(tasks):
    while True:
        user_input = input("Keep entering tasks or type done to stop entering : ").lower().strip()
        if user_input == "done":
            break
        else:
            tasks.append(user_input)

def view_task(tasks):
    print(f"Here are the tasks: \n{tasks}")

def update_task(tasks):
    update = input("Enter the task number you want to update : ")
    idx = tasks.index(update)
    tasks[idx] = input("Enter the new task : ")

def delete_task(tasks):
    item = input("Enter the task number you want to delete : ")
    tasks.remove(item)   

def exit_app():
    print("Thank you for using the app!")
    
def task():
    tasks = []
    print("-----WELCOME TO TASK MANAGEMENT APP-----\n")
    while True:
        operation = int(input("Enter 1-Add / 2-Update / 3-Delete / 4-View / 5-Exit : "))
        if operation == 1:
            add_task(tasks)

        elif operation == 2:
            update_task(tasks)

        elif operation == 3:
            delete_task(tasks)

        elif operation == 4:
            view_task(tasks)

        elif operation == 5:
            exit_app()
            break

task()

        

        

