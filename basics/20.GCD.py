print("Write a Python program to compute the greatest common divisor (GCD) of two positive integers")

print()

def gcd(x,y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range (int(y / 2),0, -1):
        if x % k == 0 and y % k ==0:
            gcd = k
            break
    return gcd

print(gcd(12, 3))

print(gcd(4, 6))

print()


# computes Greatest Common Factor GCF / Greatest Common Divisor GCD of two numbers
# useful for reducing fractions

def gcf(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    for x in range(num1, 0, -1):
        if num1 % x == 0 and num2 % x == 0:
            return x


num1 = 18
num2 = 204
print(str(gcf(num1, num2)))
