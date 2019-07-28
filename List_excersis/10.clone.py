print('''Write a Python program to clone or copy a list.''')

print()

def cloning(list):

    aft_clone = list[:]
    return aft_clone


org = [1,2,3,4,5]

change = cloning(org)
change.append('dog')

print("oringinal list",org)
print("After cloning",change)