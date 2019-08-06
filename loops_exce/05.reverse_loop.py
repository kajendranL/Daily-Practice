print("""Write a Python program that accepts a word from the user and reverse it.""")

print()


word = input("Enter a word: ")

print("The Original word is: ",word)

for n in range(len(word)-1,-1,-1):
    print(word[n],end='')
