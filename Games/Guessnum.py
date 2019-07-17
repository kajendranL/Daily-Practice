# guess the number

import random

guessTaken = 0

name = input("please enter your name:  ")
print("Hi", name, "Welcome to the 'Guess the number' game, Please wait while the Game is loading........")

number = random.randint(1,20)

print("Well",name, "Can you guess the number i am thinking off now? ")

for guessTaken in range(6):
    guess = int(input("Please enter your guess here :  "))

    if guess < number:
        print(name, "your guessed", guess, "This number is too low")
    elif guess > number:
        print("Your guess is too high")
    if guess == number:
        guessTaken = guessTaken+1
        print(name,"you guessed it right in",guessTaken, "guesses")
        break
    else:
        print("your guess is wrong" "I was thinking",guess, "Nice playing with you")

