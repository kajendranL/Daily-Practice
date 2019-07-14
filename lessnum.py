'''write a program that prints out all the elements of the list that are less than 5.'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

print()
# Write this in one line of Python.

print([i for i in a if i < 5])

print()
'''Ask the user for a number and return a list that contains only elements from the 
original list a that are smaller than that number given by the user'''

num = int(input("Enter a number: "))
for i in a:
    if i < num:
        print(i)

