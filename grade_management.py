def add_grades(grades):
    st_name = input("Enter whose grades you want to enter : ")
    st_grade = input("Enter grades : ")
    grades[st_name] = st_grade

def view_grades(grades):
    print(f"Here are the grades: \n{grades}")

def update_grades(grades):
    update = input("Enter whose grade you want to update : ")
    grades[update] = input("Enter the new grades : ")

def delete_grades(grades):
    item = input("Enter the student name whose marks you want to delete : ")
    del(grades[item])   

def exit_app():
    print("Thank you for using the app!")
    
def grade():
    grades = {}
    print("-----WELCOME TO STUDENT GRADE MANAGEMENT SYSTEM-----\n")
    while True:
        operation = int(input("Enter 1-Add / 2-Update / 3-Delete / 4-View / 5-Exit : "))
        if operation == 1:
            add_grades(grades)

        elif operation == 2:
            update_grades(grades)

        elif operation == 3:
            delete_grades(grades)

        elif operation == 4:
            view_grades(grades)

        elif operation == 5:
            exit_app()
            break

grade()

        

        

