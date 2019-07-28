print('''Write a Python program to remove duplicates from a list''')

print()

def remove_dupe(list):

    n= set(list)

    return sorted(n)


print(remove_dupe([10,20,30,40,50,60,10,30]))
print(remove_dupe([1,2,3,4,5,6,2,5,8,9,7,3]))

