print("Get the largest number from a list")

print()

def max_list(items):

    max = items[0]

    for a in items:

        if a > max:

            max = a

    return max

print(max_list([41,45,60,97,63,5,4,7]))
