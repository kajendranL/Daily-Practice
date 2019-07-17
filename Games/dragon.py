import random
import time

def displayintro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')

    print()

def chosecave():
    cave=''
    while cave !='1' and cave != '2':
        print("Which cave will you chose? (1 or 2)")
        cave=input("Chose wisely")
    return cave

def checkcave(chosencave):



    print("you approach the cave")
    time.sleep(2)
    print("It is dark and spooky")
    time.sleep(2)
    print("you hear heavy breathing of a dragon")
    time.sleep(2)
    print("boom! the dragon appears in front of you! It opens it jaws!!!")
    time.sleep(2)

    friendlycave = random.randint(1, 2)
    if chosencave == str(friendlycave):
        print("Hello, here is my treasures that i wish to share with you")
    else:
        print("Awrgh! The dragon bites you and gobbles in one bite")


playagain = 'Yes'
while playagain == 'yes' or 'Yes' or 'y' or'Y':
    displayintro()
    cavenumber = chosecave()
    checkcave = cavenumber


    print("Do you wanna play again?(Yes or No)")
    playagain = input()