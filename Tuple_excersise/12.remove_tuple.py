print('''

 Write a Python program to remove an item from a tuple.

''')

print(


)

def remove_tup(tup):
    tup = sorted(tup)
    print("Original Tuple")
    print(tup)
    tup = tup[:2] + tup[3:]
    print("After removing")
    return tup



lst = (10, 20, 30, 40, 50)
lst1 = (10, 20, 30, 40, 50)

print(remove_tup(lst + lst1))