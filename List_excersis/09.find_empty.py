print('''Write a Python program to check a list is empty or not.''')

print()

def find_empty(list):

    if list == []:
        return True
    else:
        return False

print(find_empty([]))

print(find_empty([(1,2),()]))