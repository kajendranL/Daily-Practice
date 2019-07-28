print('''Write a Python program to print the numbers of a 
specified list after removing even numbers from it.''')

print()

def remove_even(list):
    r_even = 1
    for s in list:
        if s % 2 != 0:
            print(s)


print(remove_even([1,2,3,4,5,6,7,8,9,10,12,14,15,13,19,17]))


print()

num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)
