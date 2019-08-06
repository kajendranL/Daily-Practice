print('''
Write a Python program to get the Fibonacci series between 0 to 50.

Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
Every next number is found by adding up the two numbers before it

''')

print()

x,y = 0,1

while y<50:
    print(y)
    x,y = y,x+y


print()



# Fibonacci using for loops


num= int(input("Input a number (min2): "))
zero = 0
first = 1

print(zero,',',first, end=',')

for i in range(2,num):
    next = zero + first
    print(next ,end=',')
    zero = first
    first = next
