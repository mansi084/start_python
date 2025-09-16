import random
subjects = ["APJ Abdul Kalam", "Mahatma Gandhi", "Sachin Tendulkar",
            "Ratan Tata", "Sundar Pichai", "Virat Kohli", "Lata Mangeshkar", 
            "Indira Gandhi", "Bengal Tiger", "Indian Elephant"]

verbs = ["Runs", "Eats", "Sleeps", "celebrates", "Reads", "Jumps", "Sings", "Plays", "shouts", "Swims"] 

places = ["at Red Fort", "in Mumbai", "on the table", "under the tree", "near India Gate", "beside the river",
           "inside the temple", "over the bridge", "between the hills", "around the park"]

all_headlines = []

while True:
    user_ask = input("Do you want to personalise? (yes/no) : ").strip().lower()
    if user_ask=="no":
        subject=random.choice(subjects)
        verb=random.choice(verbs).lower()
        place=random.choice(places)
        Headline = f"BREAKING NEWS :  {subject} {verb} {place}"
        
    else:
        user_subject = input("Enter the subject : ")
        user_object=input("Enter the object : ")
        verb=random.choice(verbs).lower()
        Headline = f"BREAKING NEWS :  {user_subject} {verb} {user_object}"
    print("\n"+ Headline)
    all_headlines.append(Headline)

    user_input=input("Do you want another headline? (yes/no) : ").strip().lower() 
    if user_input == "no":
        break  

user_save = input("Do you want to save all these headlines? (yes/no) : ").strip().lower()
if user_save=="yes":
    with open("saved_headlines.text","w") as f:
        f.write("\n".join(all_headlines))
        print("Headlines saved!")
   

print("Thank you!")


