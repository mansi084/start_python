HISTORY = "history.txt"

def show_history():
    file = open(HISTORY,'r')
    lines = file.readlines()
    if len(lines)==0:
        print("No history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY,'w')
    file.close()
    print("History cleared!")

def exit():
    print("Thank you. Goodbye!")
    
def save_to_history(equation, result):
    file = open("HISTORY.txt",'a')
    file.write(equation + "=" + str(result) +"\n")
    file.close()

def calculation(user_input):
    parts = user_input.split()
    if len(parts) == 3:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
        if op == "+":
            res = num1 + num2
        elif  op == "-":
            res = num1 - num2
        elif op == "*":
            res = num1 * num2
        elif op == "**":
            res = pow(num1,num2)
        elif op == "/":
            if num2 != 0:
                res = num1 / num2
            elif num2 == 0:
                res = "division cannot occur with 0"
        print(res)       
        save_to_history(user_input,res) 

    else:
        print("invalid format")
        return

def main():
    print("----------SIMPLE CALCULATOR----------")
    while True:
        user_input = input("Enter calculation(+ - / * **) or command(exit,history,clear) : ")
        if user_input == "exit":
            exit()
            break
        elif user_input == "clear":
            clear_history()

        elif user_input == "history":
            show_history()

        else:
            calculation(user_input)

main()


            
                   
























         


    
