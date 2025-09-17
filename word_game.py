import random
easy = ["apple", "ball", "cat", "dog", "egg", "fish", "goat", "hat", "ice", "jug", "kite",
        "lion", "moon", "nest", "orange", "pen", "queen", "rat", "sun", "tree"]

medium = ["planet", "garden", "silver", "bridge", "happy", "yellow", "school", "friend", "winter",
        "summer", "dream", "family", "forest", "castle", "mountain", "river", "travel", 
        "music", "future", "wonder"]

hard = ["labyrinth", "enigmatic", "phantasm", "quarantine", "xylophone", "zephyr", 
        "cryptic", "paradox", "serendipity", "obsidian", "mythical", "chimera", "eloquent", 
        "vortex", "inception", "mirage", "utopia", "dystopia", "reverie", "ephemeral"]

def main():
    print("WELCOME TO THE PASSWORD GUESSING GAME")
    user_input = input("Select the difficulty level (easy/medium/hard) : ").strip().lower()
    if user_input == "easy":
        password = random.choice(easy)
    elif user_input == "easy":
        password = random.choice(medium)
    elif user_input == "hard":
        password = random.choice(hard)
    else:
        print("Invalid choice. Defaulting to easy.")
        password = random.choice(easy)
    print("There are ",len(password)," letters in the word")

    attempt=0

    while True:
        user_guess = input("Guess the word : ").strip().lower()
        if user_guess == password:
            print("Congratulations! You have guessed the right word in ",attempt, " attempts.")
            break
        else:
            hint = ""
            for i in range(len(user_guess)):
                if i < len(user_guess) and user_guess[i]== password:
                    hint+=password[i]
                else:
                    hint+="_"

            print("Hint : ",hint)   
               
    print("Game over!")  

main()