print("Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference")

print()

def difference(n):
    if n<= 17:
        return 17-n
    else:
        return (n-17)*2

print(difference(32))
print(difference(17))
print(difference(22))
