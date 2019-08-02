print("Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20")

print()


def twosum(x,y):
    sum = x + y

    if sum in range (15, 20):
       return 20
    else:
        return sum



print(twosum(12, 2,))
print(twosum(15, 15,))
print(twosum(9, 5, ))
