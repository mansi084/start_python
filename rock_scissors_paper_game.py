import random
options = ['rock','paper','scissors']

while True:
    system_choice = random.choice(options)
    user_choice = input("Choose Rock/ Paper/Scissors (to end the game enter 'EXIT') : ").lower().strip()
    if user_choice=="exit":
        print("Thank you for playing the game.")
        break
    else:
        print("Computer : ",system_choice,"\tYou : ",user_choice)

        if system_choice == user_choice:
            print("It's a tie!")

        if system_choice == "rock":
            if user_choice == "scissors":
                print(f"{system_choice} breaks {user_choice}, COMPUTER WINS!")
            elif user_choice == "paper":
                print(f"{user_choice} covers {system_choice}, YOU WIN!")
            elif user_choice != "rock":
                print("Enter valid input..")

        if system_choice == "scissors":
            if user_choice == "rock":
                print(f"{user_choice} breaks {system_choice}, YOU WIN!")
            elif user_choice == "paper":
                print(f"{system_choice} cuts {user_choice}, COMPUTER WINS!")
            elif user_choice != "scissors":
                print("Enter valid input..")

        if system_choice == "paper":
            if user_choice == "rock":
                print(f"{system_choice} covers {user_choice}, COMPUTER WINS!")
            elif user_choice == "scissors":
                print(f"{user_choice} cuts {system_choice}, YOU WIN!")
            elif user_choice != "paper":
                print("Enter valid input..")
