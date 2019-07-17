# simple guessing game

Question = "What is the capital of Tamil Nadu?"
Answer = "Chennai"

user_input = "start"
Press = input ("Please type 'start' to being the game:" )
if user_input == "start":
    print(Question,)
    Answer = input("Enter your answer here: ")
else:
    print("Type in 'Start' to begin the game")

while Answer != "Chennai":
    print("That is a wrong answer, Please try again")
    print(Question,)
    break


