print("Multiplies all the items in a list")

print()

def mult_list(items):

###
    mul = 1

    for i in items:

        mul *= i

    return mul

print("The multiplied list is", mult_list([1,2,6,6,8,4,-6]))