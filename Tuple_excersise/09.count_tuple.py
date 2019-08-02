print('''
Write a Python program to find the repeated items of a tuple.
''')

print()

def count_tuple(t):
    print("The total count of 10 is ", t.count(t[1]))
    print(len(t))
    print(t.index(50))


lst = (10, 20, 30, 40, 50)
lst1 = (10, 20, 30, 40, 50)

print(count_tuple(lst+lst1))
