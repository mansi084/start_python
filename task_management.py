def add_task(tasks):
    total_tasks= int(input("Enter number of tasks you want to enter : "))
    for i in range(1,total_tasks+1):
        task_name = input(f'Enter task number {i} : ') 
        tasks.append(task_name)

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

        

        

