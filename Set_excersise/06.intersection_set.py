print('''

Write a Python program to create an intersection of sets
''')

print(

)


def set_math_func(x, y):
    # Union
    a = x.union(y)
    b = x | y
    print("The union of x and y is :", a)
    print("The union of x and y is :", b)

    # comon details
    # intersection

    c = x.intersection(y)
    d = x & y
    print("The intersection  of x and y is :", c)

    # Difference
    e = x.difference(y)
    e = x - y
    f = y.difference(x)
    f = y - x
    print("The difference between x and y is :", e)
    print("The difference between y and x is :", f)

    # symmetric difference
    # unique elements

    g = x.symmetric_difference(y)
    h = x ^ y
    print("The symmetric difference between x and y is :", g)




x1 = {10, 20, 30, 40}
y1 = {30, 40, 50, 60}

print(set_math_func(x1, y1))
