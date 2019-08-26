print('''

Write a Python program to create a shallow copy of sets. 

Note : Shallow copy is a bit-wise copy of an object. 
A new object is created that has an exact copy of the values in 
the original object.

''')

print(



)

def copy_set(n):

    # Copy
    c1 = n.copy()
    print(c1)

    print()
    # Frozen set

    c3 = frozenset(n)
    print(c3)
    print()

    #len of set
    c5 = len(n)
    print("The lenth of the set is: ", c5)

    # Max and Min of set
    print()
    c4 = max(n)
    c5 = min(n)

    print("The max value in the set is: ", c4)
    print(c5, "is the min value in the given set")
    print()
        # Clear
    c2 = n.clear()
    print(c2)





copy = {10,11,22,33,44,55,66,77,88,99}
print(copy_set(copy))