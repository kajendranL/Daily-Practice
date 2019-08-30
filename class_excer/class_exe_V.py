#Exercise 13 – Calculate the Number of Letters and Digits

class LettersDigits():
    def __init__(self):
        pass

    def letters_digits(self, sentence):
        digits_letters = {"Letters":0, "Digits":0}
        upper_lower = {"Upper":0, "Lower":0}

        for x in sentence:
            if x.isalpha():
                digits_letters["Letters"]+=1
            if x.isdigit():
                digits_letters["Digits"]+=1
            if x.isupper():
                upper_lower["Upper"]+=1
            elif x.islower():
                upper_lower["Lower"]+=1
            else:
                pass
        return digits_letters, upper_lower


ld=LettersDigits()

sentence = """In this Python exercise, write a Python program that will 
    accept a few sentences as input from a user and print the 
sentences in upper case after user input. Take a look into the 
upper case function in Python and how to store values 
from user input 1234567890-=-098765432123456789876543"""

print(ld.letters_digits(sentence))
