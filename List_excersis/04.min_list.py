print("Get the smallest number from a list")

print()

def min_list(list):

    min = list[0]

    for a in list:
        if a < min:
            min = a

    return min

print(min_list([65,23,89,62,54,74,12,16]))