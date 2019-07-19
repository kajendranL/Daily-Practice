print('''Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.''')

fname = input(" Enter first  name: ")
lastname = input(" Enter last   name: ")

print("First name and last name reversed")
print(lastname , fname)

print()
print()

#Reversed name is

name = (input("Enter your name"))
rev = name.split(" ")

print("The reversed name is", rev[-1], rev[0])
