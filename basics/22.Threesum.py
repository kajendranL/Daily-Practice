print("Write a Python program to sum of three given integers. However, if two values are equal sum will be zero")

print()


def threesum(x,y,z):
    if x ==y or x == z or y ==z:
        sum = 0

    else:
        sum = x + y + z

    return sum


print(threesum(1, 2, 3))
print(threesum(5, 5, 0))
print(threesum(9, 5, 3))
