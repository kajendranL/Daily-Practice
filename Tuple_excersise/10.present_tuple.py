print('''

Write a Python program to check whether an element exists within a tuple
''')

print()

def element_exist(tup):
    for i in tup:
        print("the number", i , "is present in tuple" )
    return tup

lst = (10, 20, 30, 40, 50)
lst1 = (10, 20, 30, 40, 50)

print(element_exist(lst + lst1))