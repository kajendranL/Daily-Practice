'''Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user
'''


def odd_even(n):
    if n % 2 == 0:
        print(n, "is an even number")
    else:
        print(n, "is an odd number")


num = int(input("Enter a number: "))
odd_even(num)



print()

# similar to above one
num = int(input("Enter a number"))
check = int(input("Enter a number to divide"))


def even_odd(num, check):
    if num % 4 == 0:
        print(num, "is multiple of '4'")
    elif num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is not an even number")
    if num % check == 0:
        print(num, "is evenly divided by", check)
    else:
        print(num, "is not evenly divided by", check)


even_odd(num, check)
