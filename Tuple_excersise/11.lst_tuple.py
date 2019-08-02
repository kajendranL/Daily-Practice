print("""

Write a Python program to convert a list to a tuple

""")

print(

)


def lst_tuple(tup):
    tup1 = list(tup)
    print(sorted(tup1))
    print(type(tup1))

    return tup

lst = (10, 20, 30, 40, 50)
lst1 = (10, 20, 30, 40, 50)

print(lst_tuple(lst + lst1))
