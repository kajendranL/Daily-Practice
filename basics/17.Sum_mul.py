print("Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.")

print()

def sum_num(x,y,z):

    sum = x + y + z

    if x == y == z:
        sum = sum*3

        return sum

    else:
        return x+y+z

print(sum_num(1,2,3))
print(sum_num(5,5,5))



