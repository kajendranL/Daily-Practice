print(''' Write a Python program to create a tuple with numbers and print one item.''')

print()

def print_one (a):
    return a

b = (10, 10.5, (3+4j), True, 'Kajendran')

print("The given tuple is ")

print(print_one(b))

print(b[1]," at the index of", b.index(10.5))
print(b[-1])

